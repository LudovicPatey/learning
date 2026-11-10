// Content loading and rendering.
//
// Layout of the content folder:
//   content/areas.yaml             research areas (computability, randomness, ...)
//   content/<course>/_course.yaml  one small course: metadata + ordered lessons
//   content/<course>/<slug>.md     one lesson (frontmatter + Markdown)
//
// Lessons are Markdown with $math$ (book macros available), and directives:
//   :::theorem[Optional title]{#thm-id}   ... :::   (also lemma, definition, ...)
//   :::proof{of=thm-id}                   ... :::
//   :::quiz                               ... :::   (multiple-choice questions)
//   :ref{#thm-id}                          cross-reference, possibly to another lesson

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import matter from "gray-matter";
import YAML from "yaml";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import remarkDirective from "remark-directive";
import remarkSmartypants from "remark-smartypants";
import remarkRehype from "remark-rehype";
import rehypeRaw from "rehype-raw";
import rehypeKatex from "rehype-katex";
import { toHtml } from "hast-util-to-html";
import { visit, SKIP } from "unist-util-visit";
import type { Root as MdRoot } from "mdast";
import type { Root as HRoot, Element as HElement, ElementContent, RootContent } from "hast";
import { macros } from "./katex-macros.ts";
import { contentDir, versionDir } from "./versions.ts";

// ---------------------------------------------------------------- types

export type LessonMeta = {
  id: string; // "<course>/<slug>"
  course: string;
  slug: string;
  index: number; // position in the course, from 0
  title: string;
  summary: string;
  duration?: number; // minutes
  prerequisites: string[]; // lesson ids
  quizCount: number; // number of MCQ questions in the lesson
  sections: string[]; // titles of the level-2 headings
  file: string; // absolute path of the source file
  version?: string; // set when the lesson comes from a released version
};

/** Selects a released version of one course; other courses are read from their working copy. */
export type VersionSel = { course: string; version: string } | undefined;

export type Area = { id: string; title: string; description: string; color: string; order: number };

export type CourseStatus = "available" | "draft" | "planned";

export type Course = {
  id: string;
  title: string;
  area: string;
  summary: string;
  description: string;
  level: string;
  status: CourseStatus;
  order: number;
  prerequisites: string[]; // course ids
  objectives: string[];
  authors: string[];
  lessons: string[]; // slugs, in order
};

export type QuizOption = { html: string; correct: boolean; explanationHtml: string };
export type QuizQuestion = {
  stemHtml: string;
  multi: boolean;
  options: QuizOption[];
  discussionHtml: string;
};
export type QuizData = { id: string; title?: string; questions: QuizQuestion[] };

export type Segment = { type: "html"; html: string } | { type: "quiz"; quiz: QuizData };

export type RenderedLesson = {
  meta: LessonMeta;
  segments: Segment[];
  headings: { id: string; text: string }[];
  contentHash: string;
  warnings: string[];
  /** Rendered statements referenced from this lesson, for hover previews. */
  refPreviews: Record<string, RefPreview>;
};

export type RefPreview = { html: string; lessonId: string; href: string; lessonTitle: string; courseTitle: string };

type Label = {
  id: string;
  lessonId: string;
  kind: string;
  number?: string; // e.g. "7.3": lesson number, then position in the lesson
  title?: any[]; // mdast phrasing nodes of the title
  titleText?: string;
};

type Catalog = {
  areas: Area[];
  courses: Course[];
  lessons: Map<string, LessonMeta>;
  labels: Map<string, Label>;
  warnings: string[];
  /** Fingerprint of the content files this catalog was built from. */
  fingerprint: string;
};

// ---------------------------------------------------------------- environments

const NUMBERED: Record<string, string> = {
  definition: "Definition",
  theorem: "Theorem",
  lemma: "Lemma",
  proposition: "Proposition",
  corollary: "Corollary",
  fact: "Fact",
  example: "Example",
  remark: "Remark",
  notation: "Notation",
  exercise: "Exercise",
  question: "Question",
  conjecture: "Conjecture",
};
const UNNUMBERED: Record<string, string> = {
  proof: "Proof",
  solution: "Solution",
  hint: "Hint",
  aside: "Aside",
  figure: "Figure",
  quiz: "Check your understanding",
};

export function kindLabel(kind: string): string {
  return NUMBERED[kind] ?? UNNUMBERED[kind] ?? kind;
}


// ---------------------------------------------------------------- mdast helpers

function mdText(nodes: any[]): string {
  let s = "";
  for (const n of nodes) {
    if (n.type === "text") s += n.value;
    else if (n.type === "inlineMath") s += `$${n.value}$`;
    else if (n.type === "inlineCode") s += n.value;
    else if (n.children) s += mdText(n.children);
  }
  return s;
}

function slugify(s: string): string {
  return s
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/\$[^$]*\$/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

/** Pull out the `[label]` of a container directive (remark-directive stores it as a first paragraph). */
function takeDirectiveLabel(node: any): any[] | undefined {
  const first = node.children?.[0];
  if (first && first.type === "paragraph" && first.data?.directiveLabel) {
    node.children.shift();
    return first.children;
  }
  return undefined;
}

function peekDirectiveLabel(node: any): any[] | undefined {
  const first = node.children?.[0];
  if (first && first.type === "paragraph" && first.data?.directiveLabel) return first.children;
  return undefined;
}

/** A generic mdast node that becomes `<tag class=...>` in HTML. */
function block(tag: string, className: string[], children: any[], props: Record<string, unknown> = {}): any {
  return { type: "htmlBlock", data: { hName: tag, hProperties: { className, ...props } }, children };
}
function span(className: string[], children: any[], props: Record<string, unknown> = {}): any {
  return { type: "emphasis", data: { hName: "span", hProperties: { className, ...props } }, children };
}
const text = (value: string) => ({ type: "text", value });

/** Assign numbers to numbered environments, in document order (shared counter, like the book). */
function numberEnvironments(tree: MdRoot) {
  let n = 0;
  visit(tree, "containerDirective", (node: any) => {
    if (NUMBERED[node.name]) {
      n += 1;
      node.data = { ...(node.data ?? {}), envNumber: n };
    }
  });
}

function parser() {
  return unified().use(remarkParse).use(remarkGfm).use(remarkMath).use(remarkDirective).use(remarkSmartypants);
}

// ---------------------------------------------------------------- catalog

function readAreas(warnings: string[]): Area[] {
  const file = path.join(contentDir(), "areas.yaml");
  if (!fs.existsSync(file)) {
    warnings.push("content/areas.yaml is missing");
    return [];
  }
  const raw = YAML.parse(fs.readFileSync(file, "utf8")) ?? [];
  return (raw as any[]).map((a, i) => ({
    id: String(a.id),
    title: String(a.title ?? a.id),
    description: String(a.description ?? ""),
    color: String(a.color ?? "#4f46e5"),
    order: Number(a.order ?? i),
  }));
}

function readCourse(
  courseId: string,
  warnings: string[],
  dir = path.join(contentDir(), courseId),
  version?: string,
): { course: Course; lessons: LessonMeta[]; labels: Label[] } | null {
  const courseFile = path.join(dir, "_course.yaml");
  if (!fs.existsSync(courseFile)) return null;
  const raw = YAML.parse(fs.readFileSync(courseFile, "utf8")) ?? {};
  const slugs: string[] = (raw.lessons ?? []).map(String);
  const status: CourseStatus = raw.status === "planned" || raw.status === "draft" ? raw.status : slugs.length ? "available" : "planned";
  const course: Course = {
    id: courseId,
    title: String(raw.title ?? courseId),
    area: String(raw.area ?? ""),
    summary: String(raw.summary ?? ""),
    description: String(raw.description ?? raw.summary ?? ""),
    level: String(raw.level ?? "Introductory"),
    status,
    order: Number(raw.order ?? 100),
    prerequisites: (raw.prerequisites ?? []).map(String),
    objectives: (raw.objectives ?? []).map(String),
    authors: (raw.authors ?? []).map(String),
    lessons: slugs,
  };

  const lessons: LessonMeta[] = [];
  const labels: Label[] = [];
  slugs.forEach((slug, index) => {
    const file = path.join(dir, `${slug}.md`);
    if (!fs.existsSync(file)) {
      warnings.push(`${courseId}/_course.yaml lists "${slug}" but ${courseId}/${slug}.md does not exist`);
      return;
    }
    const { data, content } = matter(fs.readFileSync(file, "utf8"));
    const id = `${courseId}/${slug}`;
    const tree = parser().parse(content) as MdRoot;
    numberEnvironments(tree);
    let quizCount = 0;
    const sections: string[] = [];
    visit(tree, "heading", (node: any) => {
      if (node.depth === 2) sections.push(mdText(node.children));
    });
    visit(tree, "containerDirective", (node: any) => {
      if (node.name === "quiz") {
        quizCount += 1 + node.children.filter((c: any) => c.type === "thematicBreak").length;
      }
      const anchor = node.attributes?.id;
      if (anchor) {
        const title = peekDirectiveLabel(node);
        labels.push({ id: anchor, lessonId: id, kind: node.name, number: node.data?.envNumber ? `${index + 1}.${node.data.envNumber}` : undefined, title, titleText: title ? mdText(title) : undefined });
      }
    });
    lessons.push({
      id,
      course: courseId,
      slug,
      index,
      title: String(data.title ?? slug),
      summary: String(data.summary ?? ""),
      duration: data.duration ? Number(data.duration) : undefined,
      prerequisites: (data.prerequisites ?? []).map((p: string) => (p.includes("/") ? p : `${courseId}/${p}`)),
      quizCount,
      sections,
      file,
      version,
    });
  });
  for (const f of fs.readdirSync(dir)) {
    if (f.endsWith(".md") && !slugs.includes(f.slice(0, -3))) {
      warnings.push(`${courseId}/${f} is not listed in ${courseId}/_course.yaml`);
    }
  }
  return { course, lessons, labels };
}

function buildCatalog(sel?: VersionSel): Catalog {
  const warnings: string[] = [];
  const areas = readAreas(warnings).sort((a, b) => a.order - b.order);
  const courses: Course[] = [];
  const lessons = new Map<string, LessonMeta>();
  const labels = new Map<string, Label>();
  const root = contentDir();
  const dirs = fs.existsSync(root)
    ? fs.readdirSync(root, { withFileTypes: true }).filter((d) => d.isDirectory() && !d.name.startsWith("_") && !d.name.startsWith("."))
    : [];
  for (const d of dirs) {
    const res =
      sel && sel.course === d.name
        ? readCourse(d.name, warnings, versionDir(d.name, sel.version), sel.version)
        : readCourse(d.name, warnings);
    if (!res) continue;
    courses.push(res.course);
    for (const l of res.lessons) lessons.set(l.id, l);
    for (const lab of res.labels) {
      const prev = labels.get(lab.id);
      if (prev) warnings.push(`Duplicate label #${lab.id} in ${prev.lessonId} and ${lab.lessonId}`);
      else labels.set(lab.id, lab);
    }
  }
  const areaOrder = new Map(areas.map((a, i) => [a.id, i]));
  courses.sort((a, b) => (areaOrder.get(a.area) ?? 99) - (areaOrder.get(b.area) ?? 99) || a.order - b.order || a.title.localeCompare(b.title));
  const ids = new Set(courses.map((c) => c.id));
  for (const c of courses) {
    if (!areaOrder.has(c.area)) warnings.push(`${c.id}: unknown area "${c.area}" (see content/areas.yaml)`);
    for (const p of c.prerequisites) if (!ids.has(p)) warnings.push(`${c.id}: unknown prerequisite course "${p}"`);
  }
  for (const l of lessons.values()) {
    for (const p of l.prerequisites) {
      if (!lessons.has(p)) warnings.push(`${l.id}: unknown prerequisite "${p}"`);
    }
  }
  return { areas, courses, lessons, labels, warnings, fingerprint: contentFingerprint(sel) };
}

// Caching. Every cache is keyed by a fingerprint of the content files (paths,
// sizes and modification times), so an edited lesson is picked up on the next
// request while unchanged content is never parsed twice. Computing the
// fingerprint costs one stat per file.
const selKey = (sel?: VersionSel) => `${contentDir()}|${sel ? `${sel.course}@${sel.version}` : "current"}`;

function fingerprintDir(dir: string, out: string[]) {
  if (!fs.existsSync(dir)) return;
  for (const d of fs.readdirSync(dir, { withFileTypes: true })) {
    if (d.name.startsWith(".")) continue;
    const p = path.join(dir, d.name);
    if (d.isDirectory()) {
      if (d.name !== "_versions") fingerprintDir(p, out);
    } else if (/\.(md|ya?ml)$/.test(d.name)) {
      const st = fs.statSync(p);
      out.push(`${p}:${st.size}:${st.mtimeMs}`);
    }
  }
}

/** Fingerprint of the files a catalog depends on. Exported for tests. */
export function contentFingerprint(sel?: VersionSel): string {
  const out: string[] = [];
  fingerprintDir(contentDir(), out);
  if (sel) fingerprintDir(versionDir(sel.course, sel.version), out);
  return crypto.createHash("sha1").update(out.join("|")).digest("hex");
}

const catalogCache = new Map<string, { fp: string; catalog: Catalog }>();

export function getCatalog(sel?: VersionSel): Catalog {
  const key = selKey(sel);
  const fp = contentFingerprint(sel);
  const hit = catalogCache.get(key);
  if (hit?.fp === fp) return hit.catalog;
  const catalog = buildCatalog(sel);
  catalogCache.set(key, { fp, catalog });
  return catalog;
}

export function getCourse(id: string, sel?: VersionSel) {
  return getCatalog(sel).courses.find((c) => c.id === id);
}

export function getArea(id: string) {
  return getCatalog().areas.find((a) => a.id === id);
}

export function getLesson(id: string, sel?: VersionSel) {
  return getCatalog(sel).lessons.get(id);
}

export function courseLessons(courseId: string, sel?: VersionSel): LessonMeta[] {
  const cat = getCatalog(sel);
  const course = cat.courses.find((c) => c.id === courseId);
  if (!course) return [];
  return course.lessons.map((s) => cat.lessons.get(`${courseId}/${s}`)).filter(Boolean) as LessonMeta[];
}

export function courseStats(courseId: string, sel?: VersionSel) {
  const ls = courseLessons(courseId, sel);
  return {
    lessons: ls.length,
    minutes: ls.reduce((s, l) => s + (l.duration ?? 0), 0),
    questions: ls.reduce((s, l) => s + l.quizCount, 0),
  };
}

/** Longest chain of prerequisite courses below each course (0 = no prerequisites). */
export function courseDepths(): Map<string, number> {
  const { courses } = getCatalog();
  const byId = new Map(courses.map((c) => [c.id, c]));
  const depth = new Map<string, number>();
  const visit = (id: string, stack: Set<string>): number => {
    if (depth.has(id)) return depth.get(id)!;
    if (stack.has(id)) return 0; // cycle: ignore
    stack.add(id);
    const c = byId.get(id);
    const d = c && c.prerequisites.length ? 1 + Math.max(...c.prerequisites.filter((p) => byId.has(p)).map((p) => visit(p, stack)), -1) : 0;
    stack.delete(id);
    depth.set(id, d);
    return d;
  };
  for (const c of courses) visit(c.id, new Set());
  return depth;
}

/** Courses that list `id` as a prerequisite. */
export function nextCourses(id: string): Course[] {
  return getCatalog().courses.filter((c) => c.prerequisites.includes(id));
}

/** Lessons that list `id` as a prerequisite. */
export function dependents(id: string): LessonMeta[] {
  return [...getCatalog().lessons.values()].filter((l) => l.prerequisites.includes(id));
}

/** URL of a lesson; with a version, the permanent URL of that version. */
export function lessonHref(id: string, version?: string) {
  if (!version) return `/courses/${id}`;
  const [course, slug] = id.split("/");
  return `/courses/${course}/v/${version}/${slug}`;
}

export function courseHref(id: string, version?: string) {
  return version ? `/courses/${id}/v/${version}` : `/courses/${id}`;
}

// ---------------------------------------------------------------- rendering

type Ctx = { lessonId: string; catalog: Catalog; warnings: string[]; refs: Set<string>; sel?: VersionSel };

/** Links inside a released course stay inside the same release. */
function hrefIn(ctx: Ctx, lessonId: string) {
  const v = ctx.sel && lessonId.startsWith(`${ctx.sel.course}/`) ? ctx.sel.version : undefined;
  return lessonHref(lessonId, v);
}

function refNode(node: any, ctx: Ctx): any {
  const target: string | undefined = node.attributes?.id ?? node.attributes?.to;
  const custom = node.children?.length ? node.children : undefined;
  if (!target) {
    ctx.warnings.push(`:ref without target (use :ref{#label})`);
    return span(["ref-missing"], [text("??")]);
  }
  // Reference to a whole lesson
  const lesson = ctx.catalog.lessons.get(target) ?? ctx.catalog.lessons.get(`${ctx.lessonId.split("/")[0]}/${target}`);
  if (lesson) {
    return { type: "link", url: hrefIn(ctx, lesson.id), title: lesson.summary || null, children: custom ?? [{ type: "emphasis", children: [text(lesson.title)] }] };
  }
  const lab = ctx.catalog.labels.get(target);
  if (lab) ctx.refs.add(lab.id);
  if (!lab) {
    ctx.warnings.push(`Unknown reference #${target}`);
    return span(["ref-missing"], [text(`??${target}`)]);
  }
  const sameLesson = lab.lessonId === ctx.lessonId;
  const kind = kindLabel(lab.kind);
  const numbered = lab.number ? `${kind} ${lab.number}` : kind;
  const other = ctx.catalog.lessons.get(lab.lessonId);
  let children: any[];
  if (custom) children = custom;
  else if (sameLesson || other?.course === ctx.lessonId.split("/")[0]) children = [text(numbered)];
  else if (lab.title) children = structuredClone(lab.title);
  else children = [text(`${numbered} of “${other?.title ?? lab.lessonId}”`)];
  const tooltip = `${numbered}${lab.titleText ? ` (${lab.titleText})` : ""}${sameLesson ? "" : ` — ${other?.title ?? ""}`}`;
  return {
    type: "link",
    url: sameLesson ? `#${lab.id}` : `${hrefIn(ctx, lab.lessonId)}#${lab.id}`,
    title: tooltip,
    data: { hProperties: { className: ["ref", sameLesson ? "ref-local" : "ref-external"] } },
    children,
  };
}

function transformQuiz(node: any, index: number, ctx: Ctx) {
  const title = takeDirectiveLabel(node);
  const groups: any[][] = [[]];
  for (const c of node.children) {
    if (c.type === "thematicBreak") groups.push([]);
    else groups[groups.length - 1].push(c);
  }
  const questions = groups
    .filter((g) => g.length)
    .map((g, qi) => {
      let li = -1;
      g.forEach((c, i) => {
        if (c.type === "list") li = i;
      });
      if (li < 0) {
        ctx.warnings.push(`Quiz question ${qi + 1} has no list of options`);
        return block("div", ["quiz-question"], g);
      }
      const list = g[li];
      const correctCount = list.children.filter((it: any) => it.checked === true).length;
      if (correctCount === 0) ctx.warnings.push(`Quiz question ${qi + 1}: no option is marked correct with [x]`);
      const options = list.children.map((it: any) => {
        const [first, ...rest] = it.children;
        return block("div", ["quiz-option"], [block("div", ["quiz-option-text"], first ? [first] : []), block("div", ["quiz-option-expl"], rest)], {
          dataCorrect: it.checked === true ? "true" : "false",
        });
      });
      return block(
        "div",
        ["quiz-question"],
        [block("div", ["quiz-stem"], g.slice(0, li)), block("div", ["quiz-options"], options), block("div", ["quiz-discussion"], g.slice(li + 1))],
        { dataMulti: correctCount > 1 ? "true" : "false" },
      );
    });
  node.data = {
    hName: "div",
    hProperties: { className: ["quiz"], dataQuizId: node.attributes?.id ?? `quiz-${index}`, dataTitle: title ? mdText(title) : undefined },
  };
  node.children = questions;
}

function remarkEnvironments(ctx: Ctx) {
  return (tree: MdRoot) => {
    numberEnvironments(tree);

    // 1. inline directives (cross-references); unknown ones are put back as text
    visit(tree, (node: any, index, parent: any) => {
      if ((node.type === "textDirective" || node.type === "leafDirective") && parent && index !== undefined) {
        if (node.name === "ref" || node.name === "cref") {
          parent.children[index] = refNode(node, ctx);
        } else {
          const attrs = node.attributes && Object.keys(node.attributes).length ? "{…}" : "";
          const prefix = node.type === "leafDirective" ? "::" : ":";
          parent.children[index] = text(`${prefix}${node.name}${node.children?.length ? `[${mdText(node.children)}]` : ""}${attrs}`);
        }
        return SKIP;
      }
    });

    // 2. headings get ids, and level-2 headings are numbered "lesson.section"
    const lessonNo = (ctx.catalog.lessons.get(ctx.lessonId)?.index ?? 0) + 1;
    let section = 0;
    visit(tree, "heading", (node: any) => {
      if (node.depth >= 2) {
        node.data = { ...(node.data ?? {}), hProperties: { id: slugify(mdText(node.children)) } };
      }
      if (node.depth === 2) {
        section += 1;
        node.children.unshift(span(["sec-num"], [text(`${lessonNo}.${section}`)]), text("\u2002"));
      }
    });

    // 3. block environments
    let quizIndex = 0;
    visit(tree, "containerDirective", (node: any) => {
      const kind: string = node.name;
      const attrs = node.attributes ?? {};
      const id = attrs.id;
      if (kind === "quiz") {
        quizIndex += 1;
        transformQuiz(node, quizIndex, ctx);
        return;
      }
      if (!NUMBERED[kind] && !UNNUMBERED[kind]) {
        ctx.warnings.push(`Unknown block :::${kind} (rendered as a plain box)`);
      }
      const title = takeDirectiveLabel(node);

      if (kind === "figure") {
        node.data = { hName: "figure", hProperties: { className: ["env", "env-figure"], id } };
        if (title) node.children.push(block("figcaption", [], title));
        return;
      }

      const head: any[] = [];
      if (kind === "proof") {
        let label: any[] = [text("Proof")];
        if (title) label = title;
        else if (attrs.of) label = [text("Proof of "), refNode({ attributes: { id: attrs.of }, children: [] }, ctx)];
        head.push(span(["env-label"], label), text("."));
      } else {
        const number = node.data?.envNumber;
        head.push(span(["env-label"], [text(number ? `${kindLabel(kind)} ${lessonNo}.${number}` : kindLabel(kind))]));
        if (title) {
          if (kind === "aside" || kind === "solution" || kind === "hint") head.splice(0, 1, span(["env-label"], title));
          else head.push(text(" "), span(["env-title"], [text("("), ...title, text(")")]));
        }
        if (kind === "exercise" && attrs.difficulty) {
          const d = Math.max(1, Math.min(3, Number(attrs.difficulty) || 1));
          head.push(text(" "), span(["env-difficulty"], [text("★".repeat(d))], { title: `Difficulty ${d}/3` }));
        }
        if (kind !== "aside" && kind !== "solution" && kind !== "hint") head.push(text("."));
      }

      if (id) {
        head.push({
          type: "link",
          url: `#${id}`,
          title: "Link to this statement",
          data: { hProperties: { className: ["env-anchor", "no-annotate"] } },
          children: [text("#")],
        });
      }
      const collapsible = kind === "solution" || kind === "hint";
      const headNode = block(collapsible ? "summary" : "div", ["env-head"], head);
      node.children.unshift(headNode);
      node.data = {
        hName: collapsible ? "details" : "section",
        hProperties: { className: ["env", `env-${kind}`], id, dataKind: kind },
      };
    });
  };
}

function hasClass(n: any, cls: string): boolean {
  const c = n?.properties?.className;
  return Array.isArray(c) && c.includes(cls);
}
function findFirst(n: any, cls: string): HElement | undefined {
  if (hasClass(n, cls)) return n;
  for (const c of n.children ?? []) {
    const r = findFirst(c, cls);
    if (r) return r;
  }
  return undefined;
}
function directChildren(n: any, cls: string): HElement[] {
  return (n.children ?? []).filter((c: any) => hasClass(c, cls));
}
const inner = (n: HElement | undefined) => (n ? toHtml(n.children as ElementContent[]) : "");

function extractQuiz(el: HElement): QuizData {
  const questions: QuizQuestion[] = directChildren(el, "quiz-question").map((q: any) => ({
    stemHtml: inner(findFirst(q, "quiz-stem")),
    multi: q.properties?.dataMulti === "true",
    options: directChildren(findFirst(q, "quiz-options"), "quiz-option").map((o: any) => ({
      html: inner(findFirst(o, "quiz-option-text")),
      correct: o.properties?.dataCorrect === "true",
      explanationHtml: inner(findFirst(o, "quiz-option-expl")),
    })),
    discussionHtml: inner(findFirst(q, "quiz-discussion")),
  }));
  return {
    id: String(el.properties?.dataQuizId ?? "quiz"),
    title: el.properties?.dataTitle ? String(el.properties.dataTitle) : undefined,
    questions,
  };
}

async function renderTree(id: string, sel?: VersionSel) {
  const catalog = getCatalog(sel);
  const meta = catalog.lessons.get(id);
  if (!meta) return null;
  const source = fs.readFileSync(meta.file, "utf8");
  const { content } = matter(source);
  const ctx: Ctx = { lessonId: id, catalog, warnings: [], refs: new Set(), sel };

  const processor = parser()
    .use(remarkEnvironments, ctx)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .use(rehypeKatex, { macros: macros(), throwOnError: false, strict: false });

  const tree = (await processor.run(processor.parse(content))) as HRoot;
  return { meta, source, ctx, tree };
}

// Rendered trees, cached per lesson for a given state of the content.
const treeCache = new Map<string, { fp: string; value: Promise<Awaited<ReturnType<typeof renderTree>>> }>();

function cachedTree(id: string, sel?: VersionSel) {
  const fp = getCatalog(sel).fingerprint;
  const key = `${selKey(sel)}|${id}`;
  const hit = treeCache.get(key);
  if (hit?.fp === fp) return hit.value;
  const value = renderTree(id, sel);
  treeCache.set(key, { fp, value });
  value.catch(() => treeCache.delete(key));
  return value;
}

/** Rendered HTML of the labelled statements of one lesson. */
const previewCache = new Map<string, { fp: string; map: Map<string, string> }>();

async function lessonStatements(lessonId: string, sel?: VersionSel): Promise<Map<string, string>> {
  const { labels, fingerprint } = getCatalog(sel);
  const key = `${selKey(sel)}|${lessonId}`;
  const hit = previewCache.get(key);
  if (hit?.fp === fingerprint) return hit.map;
  const map = new Map<string, string>();
  const r = await cachedTree(lessonId, sel);
  if (r) {
    visit(r.tree, "element", (el: any) => {
      const anchor = el.properties?.id;
      if (anchor && labels.has(String(anchor)) && hasClass(el, "env")) map.set(String(anchor), toHtml(el));
    });
  }
  previewCache.set(key, { fp: fingerprint, map });
  return map;
}

/** Render a lesson of the working copy, or of a released version when `sel` is given. */
export async function renderLesson(id: string, sel?: VersionSel): Promise<RenderedLesson | null> {
  const r = await cachedTree(id, sel);
  if (!r) return null;
  const { meta, source, ctx, tree } = r;
  const catalog = ctx.catalog;

  const segments: Segment[] = [];
  let buffer: RootContent[] = [];
  const flush = () => {
    const html = toHtml(buffer as any).trim();
    if (html) segments.push({ type: "html", html });
    buffer = [];
  };
  for (const child of tree.children) {
    if (child.type === "element" && hasClass(child, "quiz")) {
      flush();
      segments.push({ type: "quiz", quiz: extractQuiz(child) });
    } else buffer.push(child);
  }
  flush();

  const headings: { id: string; text: string }[] = [];
  visit(tree, "element", (el: any) => {
    if (el.tagName === "h2" && el.properties?.id) {
      const t = toHtml(el.children).replace(/<[^>]+>/g, "");
      headings.push({ id: String(el.properties.id), text: t });
    }
  });

  return {
    meta,
    segments,
    headings,
    contentHash: contentHash(source),
    warnings: ctx.warnings,
    refPreviews: await refPreviewsFor(ctx, catalog),
  };
}

export function contentHash(source: string): string {
  return crypto.createHash("sha256").update(source).digest("hex").slice(0, 16);
}

async function refPreviewsFor(ctx: Ctx, catalog: Catalog): Promise<Record<string, RefPreview>> {
  if (!ctx.refs.size) return {};
  const out: Record<string, RefPreview> = {};
  for (const id of ctx.refs) {
    const lab = catalog.labels.get(id);
    const html = lab && (await lessonStatements(lab.lessonId, ctx.sel)).get(id);
    const lesson = lab && catalog.lessons.get(lab.lessonId);
    if (!html || !lesson) continue;
    out[id] = {
      html,
      lessonId: lesson.id,
      href: `${hrefIn(ctx, lesson.id)}#${id}`,
      lessonTitle: lesson.title,
      courseTitle: catalog.courses.find((c) => c.id === lesson.course)?.title ?? "",
    };
  }
  return out;
}
