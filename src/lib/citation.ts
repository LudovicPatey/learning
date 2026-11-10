// Citation helpers (pure functions, shared by server and browser code).

export type CitationData = {
  path: string; // site-relative permanent path of the lesson
  courseId: string;
  courseTitle: string;
  lessonSlug: string;
  lessonTitle: string;
  lessonNumber: number;
  authors: string[];
  version?: string;
  date?: string; // release date, YYYY-MM-DD
};

const escapeBib = (s: string) => s.replace(/([{}%&$#_])/g, "\\$1");

/** Citation key such as `models-of-computation-ackermann-function-v1.0`. */
export function citationKey(d: Pick<CitationData, "courseId" | "lessonSlug" | "version">): string {
  return `${d.courseId}-${d.lessonSlug}${d.version ? `-v${d.version}` : ""}`;
}

export function bibtexEntry(d: CitationData & { url: string }): string {
  const fields: [string, string][] = [];
  if (d.authors.length) fields.push(["author", d.authors.map(escapeBib).join(" and ")]);
  fields.push(["title", `{${escapeBib(d.lessonTitle)}}`]);
  fields.push([
    "howpublished",
    `Lesson ${d.lessonNumber} of \\emph{${escapeBib(d.courseTitle)}}, Computability Theory course notes${d.version ? `, version ${d.version}` : ""}`,
  ]);
  if (d.date) fields.push(["year", d.date.slice(0, 4)]);
  fields.push(["url", d.url]);
  if (!d.version) fields.push(["note", "Unreleased working version"]);
  const body = fields.map(([k, v]) => `  ${k} = {${v}}`).join(",\n");
  return `@misc{${citationKey(d)},\n${body}\n}`;
}
