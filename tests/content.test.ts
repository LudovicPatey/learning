import { beforeEach, describe, expect, it } from "vitest";
import { useFixtureContent, stripTags } from "./helpers";
import {
  courseDepths,
  courseLessons,
  courseStats,
  dependents,
  getCatalog,
  getCourse,
  kindLabel,
  lessonHref,
  nextCourses,
  renderLesson,
} from "@/lib/content";

beforeEach(() => {
  useFixtureContent();
});

const html = async (id: string) => {
  const r = await renderLesson(id);
  if (!r) throw new Error(`no lesson ${id}`);
  return r;
};
const allHtml = (r: Awaited<ReturnType<typeof html>>) => r.segments.map((s) => (s.type === "html" ? s.html : "")).join("\n");

describe("catalog", () => {
  it("reads areas, courses and lessons in order", () => {
    const cat = getCatalog();
    expect(cat.areas.map((a) => a.id)).toEqual(["logic"]);
    expect(cat.courses.map((c) => c.id)).toEqual(["alpha", "beta"]);
    expect(courseLessons("alpha").map((l) => l.slug)).toEqual(["one", "two"]);
    expect(getCourse("alpha")?.authors).toEqual(["Ada Lovelace"]);
  });

  it("ignores directories starting with an underscore", () => {
    expect(getCatalog().courses.find((c) => c.id.startsWith("_"))).toBeUndefined();
  });

  it("computes lesson metadata", () => {
    const one = getCatalog().lessons.get("alpha/one")!;
    expect(one.index).toBe(0);
    expect(one.quizCount).toBe(2);
    expect(one.sections).toEqual(["First section", "Second section"]);
    const two = getCatalog().lessons.get("alpha/two")!;
    expect(two.prerequisites).toEqual(["alpha/one"]);
    expect(getCatalog().lessons.get("beta/three")!.prerequisites).toEqual(["alpha/two"]);
  });

  it("numbers labels by lesson", () => {
    const { labels } = getCatalog();
    expect(labels.get("def-widget")?.number).toBe("1.1");
    expect(labels.get("thm-main")?.number).toBe("1.2");
    expect(labels.get("lem-two")?.number).toBe("2.1");
    expect(labels.get("thm-main")?.titleText).toBe("Main theorem");
  });

  it("computes statistics and course graph", () => {
    expect(courseStats("alpha")).toEqual({ lessons: 2, minutes: 25, questions: 2 });
    expect(courseDepths().get("alpha")).toBe(0);
    expect(courseDepths().get("beta")).toBe(1);
    expect(nextCourses("alpha").map((c) => c.id)).toEqual(["beta"]);
    expect(dependents("alpha/two").map((l) => l.id)).toEqual(["beta/three"]);
  });

  it("has no catalog warnings for valid fixtures", () => {
    expect(getCatalog().warnings).toEqual([]);
  });

  it("builds lesson URLs", () => {
    expect(lessonHref("alpha/one")).toBe("/courses/alpha/one");
    expect(lessonHref("alpha/one", "1.0")).toBe("/courses/alpha/v/1.0/one");
  });

  it("labels kinds", () => {
    expect(kindLabel("theorem")).toBe("Theorem");
    expect(kindLabel("proof")).toBe("Proof");
  });
});

describe("rendering", () => {
  it("returns null for unknown lessons", async () => {
    expect(await renderLesson("alpha/nope")).toBeNull();
  });

  it("renders numbered statements and sections", async () => {
    const r = await html("alpha/one");
    const h = allHtml(r);
    expect(h).toContain('class="env env-definition"');
    expect(stripTags(h)).toContain("Definition 1.1");
    expect(stripTags(h)).toContain("Theorem 1.2");
    expect(h).toMatch(/class="sec-num">1\.1</);
    expect(r.headings.map((x) => x.id)).toEqual(["first-section", "second-section"]);
  });

  it("renders proofs with a reference to their statement", async () => {
    const h = allHtml(await html("alpha/one"));
    expect(h).toMatch(/env-proof[\s\S]*Proof of <a href="#thm-main"[^>]*>Theorem 1\.2<\/a>/);
  });

  it("resolves references within and across lessons and courses", async () => {
    const one = allHtml(await html("alpha/one"));
    expect(one).toContain('href="#def-widget"');
    expect(one).toContain('href="/courses/alpha/two#lem-two"');
    expect(stripTags(one)).toContain("Lemma 2.1");

    const three = allHtml(await html("beta/three"));
    // across courses, the title is used rather than a number
    expect(three).toContain('href="/courses/alpha/one#thm-main"');
    expect(stripTags(three)).toContain("Main theorem");
    expect(three).toContain('href="/courses/alpha/one"');
  });

  it("reports unknown references as warnings", async () => {
    const r = await html("alpha/two");
    expect(r.warnings).toEqual(["Unknown reference #does-not-exist"]);
    expect(allHtml(r)).toContain("ref-missing");
  });

  it("extracts quizzes as separate segments", async () => {
    const r = await html("alpha/one");
    const quizzes = r.segments.filter((s) => s.type === "quiz");
    expect(quizzes).toHaveLength(1);
    const q = quizzes[0].type === "quiz" ? quizzes[0].quiz : null;
    expect(q?.title).toBe("the main proof");
    expect(q?.questions).toHaveLength(2);
    expect(q?.questions[0].multi).toBe(false);
    expect(q?.questions[0].options.map((o) => o.correct)).toEqual([true, false]);
    expect(stripTags(q!.questions[0].options[0].explanationHtml)).toContain("Because.");
    expect(q?.questions[1].multi).toBe(true);
    expect(stripTags(q!.questions[1].discussionHtml)).toContain("Discussion text.");
  });

  it("renders solutions as collapsed details", async () => {
    const h = allHtml(await html("alpha/one"));
    expect(h).toMatch(/<details class="env env-solution"/);
    expect(h).toContain("★★");
  });

  it("typesets mathematics with the book macros", async () => {
    const h = allHtml(await html("alpha/one"));
    expect(h).toContain('class="katex"');
    expect(h).not.toContain("katex-error");
    expect(h).toContain("\\converge"); // TeX source kept in the MathML annotation
  });

  it("applies typographic quotes outside of mathematics", async () => {
    const h = allHtml(await html("alpha/one"));
    expect(h).toContain("“quotes”");
    expect(h).toContain("apostrophe’s");
  });

  it("provides hover previews of referenced statements", async () => {
    const r = await html("alpha/one");
    expect(Object.keys(r.refPreviews).sort()).toEqual(["def-widget", "lem-two", "thm-main"]);
    expect(r.refPreviews["lem-two"].href).toBe("/courses/alpha/two#lem-two");
    expect(r.refPreviews["lem-two"].html).toContain("env-lemma");
  });

  it("computes a stable content hash", async () => {
    const a = await html("alpha/one");
    const b = await html("alpha/one");
    expect(a.contentHash).toMatch(/^[0-9a-f]{16}$/);
    expect(a.contentHash).toBe(b.contentHash);
  });
});
