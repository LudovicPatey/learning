// Credits: the works that tracks, courses and exercises are based on.
//
// content/sources.yaml is a shared bibliography of the works credited on the site
// (books, monographs, lecture notes, articles). Tracks (content/tracks.yaml) and
// courses (content/<course>/_course.yaml) list their sources under `credits:`.
// Exercises are credited in content/<course>/_exercise-credits.yaml, a map from
// exercise labels to their source; the credits are kept outside the exercises so
// that crediting an exercise does not change its hash (endorsements refer to it).
// An exercise that is not listed was written for this course.
//
// This module is pure (no file system), so that it can be unit-tested.

export type SourceKind = "book" | "monograph" | "lecture-notes" | "article" | "survey";

export type Source = {
  id: string;
  /** Short name used in credits, e.g. "Soare 2016". */
  short: string;
  /** Full bibliographic entry, in Markdown. */
  citation: string;
  kind: SourceKind;
  url?: string;
};

/** A work a track or a course is based on. */
export type Credit = {
  source: string;
  /** "main": the track or course follows it; "consulted": compared and used for some parts. */
  role: "main" | "consulted";
  /** What was taken from it, in Markdown (chapters, order of topics, proofs). */
  note?: string;
};

/**
 * How an exercise relates to its source: taken from an exercise of the work ("from"),
 * adapted from an exercise or a proof of it ("adapted"), proving a result stated or
 * proved there ("result"), or close to an exercise or a result of it ("related").
 */
export type ExerciseRelation = "from" | "adapted" | "result" | "related";

export type ExerciseCredit = {
  relation: ExerciseRelation;
  /** Id of a work of sources.yaml, or undefined when `cite` names a work not in it. */
  source?: string;
  /** A work named in full, for articles not in sources.yaml, e.g. "Jockusch and Soare (1972)". */
  cite?: string;
  /** Location in the work, e.g. "Exercise 4.2.3" or "Theorem 9.1". */
  where?: string;
};

const KINDS: SourceKind[] = ["book", "monograph", "lecture-notes", "article", "survey"];
const RELATIONS: ExerciseRelation[] = ["from", "adapted", "result", "related"];

/** Parse sources.yaml (a list of works), reporting malformed and duplicate entries. */
export function parseSources(raw: unknown, warnings: string[]): Map<string, Source> {
  const out = new Map<string, Source>();
  if (raw == null) return out;
  if (!Array.isArray(raw)) {
    warnings.push("content/sources.yaml must be a list of works");
    return out;
  }
  for (const s of raw as any[]) {
    const id = String(s?.id ?? "");
    if (!id) {
      warnings.push("content/sources.yaml: a work has no id");
      continue;
    }
    if (out.has(id)) warnings.push(`content/sources.yaml: duplicate work "${id}"`);
    const kind = String(s.kind ?? "book") as SourceKind;
    if (!KINDS.includes(kind)) warnings.push(`content/sources.yaml: work "${id}" has unknown kind "${kind}" (${KINDS.join(", ")})`);
    const short = String(s.short ?? "");
    const citation = String(s.citation ?? "");
    if (!short || !citation) warnings.push(`content/sources.yaml: work "${id}" needs a short name and a citation`);
    out.set(id, { id, short: short || id, citation: citation || short || id, kind, url: s.url ? String(s.url) : undefined });
  }
  return out;
}

/** Parse the `credits:` list of a track or a course. `where` names it in warnings. */
export function parseCredits(raw: unknown, where: string, sources: Map<string, Source>, warnings: string[]): Credit[] {
  if (raw == null) return [];
  if (!Array.isArray(raw)) {
    warnings.push(`${where}: credits must be a list`);
    return [];
  }
  const out: Credit[] = [];
  for (const c of raw as any[]) {
    const source = String(c?.source ?? "");
    if (!sources.has(source)) {
      warnings.push(`${where}: credits name unknown work "${source}" (see content/sources.yaml)`);
      continue;
    }
    const role = c.role == null ? "main" : String(c.role);
    if (role !== "main" && role !== "consulted") warnings.push(`${where}: credit of "${source}" has unknown role "${role}" (main or consulted)`);
    out.push({ source, role: role === "consulted" ? "consulted" : "main", note: c.note ? String(c.note).trim() : undefined });
  }
  // main sources first, file order otherwise
  return [...out.filter((c) => c.role === "main"), ...out.filter((c) => c.role === "consulted")];
}

/** Parse a course's _exercise-credits.yaml: a map from exercise labels to credits. */
export function parseExerciseCredits(
  raw: unknown,
  where: string,
  sources: Map<string, Source>,
  warnings: string[],
): Map<string, ExerciseCredit> {
  const out = new Map<string, ExerciseCredit>();
  if (raw == null) return out;
  if (typeof raw !== "object" || Array.isArray(raw)) {
    warnings.push(`${where}: must be a map from exercise labels to credits`);
    return out;
  }
  for (const [label, v] of Object.entries(raw as Record<string, any>)) {
    const relation = String(v?.relation ?? "from") as ExerciseRelation;
    if (!RELATIONS.includes(relation)) warnings.push(`${where}: #${label} has unknown relation "${relation}" (${RELATIONS.join(", ")})`);
    const source = v?.source != null ? String(v.source) : undefined;
    const cite = v?.cite != null ? String(v.cite) : undefined;
    if (source && !sources.has(source)) warnings.push(`${where}: #${label} names unknown work "${source}" (see content/sources.yaml)`);
    if (!source && !cite) warnings.push(`${where}: #${label} needs a source or a cite`);
    out.set(label, {
      relation: RELATIONS.includes(relation) ? relation : "from",
      source: source && sources.has(source) ? source : undefined,
      cite: cite ?? (source && !sources.has(source) ? source : undefined),
      where: v?.where != null ? String(v.where) : undefined,
    });
  }
  return out;
}

/** The sentence crediting an exercise, in Markdown. */
export function exerciseCreditText(credit: ExerciseCredit | undefined, sources: Map<string, Source>): string {
  if (!credit) return "Written for this course.";
  const work = (credit.source ? sources.get(credit.source)?.short : undefined) ?? credit.cite ?? "";
  const ref = credit.where ? `${work}, ${credit.where}` : work;
  if (credit.relation === "adapted") return `Adapted from ${ref}.`;
  if (credit.relation === "result") return `The result is from ${ref}.`;
  if (credit.relation === "related") return `Related to ${ref}.`;
  return `From ${ref}.`;
}
