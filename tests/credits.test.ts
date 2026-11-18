import { beforeEach, describe, expect, it } from "vitest";
import { exerciseCreditText, parseCredits, parseExerciseCredits, parseSources } from "@/lib/credits";
import { getCatalog, renderLesson } from "@/lib/content";
import { parseTracks } from "@/lib/tracks";
import { useFixtureContent } from "./helpers";

const rawSources = [
  { id: "s1", short: "Smith 2001", kind: "book", citation: "J. Smith, *Logic*, 2001." },
  { id: "s2", short: "Jones, Notes", kind: "lecture-notes", citation: "K. Jones, *Notes*." },
];

describe("parseSources", () => {
  it("reads works by id", () => {
    const w: string[] = [];
    const m = parseSources(rawSources, w);
    expect(w).toEqual([]);
    expect(m.get("s1")).toEqual({ id: "s1", short: "Smith 2001", kind: "book", citation: "J. Smith, *Logic*, 2001.", url: undefined });
  });

  it("reports duplicates, unknown kinds and missing fields", () => {
    const w: string[] = [];
    parseSources([{ id: "a", short: "A", citation: "A." }, { id: "a", kind: "poem", short: "A", citation: "A." }, { id: "b" }, {}], w);
    expect(w).toEqual([
      'content/sources.yaml: duplicate work "a"',
      'content/sources.yaml: work "a" has unknown kind "poem" (book, monograph, lecture-notes, article, survey)',
      'content/sources.yaml: work "b" needs a short name and a citation',
      "content/sources.yaml: a work has no id",
    ]);
  });
});

describe("parseCredits", () => {
  const sources = parseSources(rawSources, []);

  it("puts main sources first and defaults the role to main", () => {
    const w: string[] = [];
    const c = parseCredits([{ source: "s2", role: "consulted" }, { source: "s1", note: " Chapter 1. " }], "x", sources, w);
    expect(w).toEqual([]);
    expect(c).toEqual([
      { source: "s1", role: "main", note: "Chapter 1." },
      { source: "s2", role: "consulted", note: undefined },
    ]);
  });

  it("reports unknown works and roles", () => {
    const w: string[] = [];
    const c = parseCredits([{ source: "nope" }, { source: "s1", role: "inspiration" }], "course/_course.yaml", sources, w);
    expect(c.map((x) => x.source)).toEqual(["s1"]);
    expect(w).toEqual([
      'course/_course.yaml: credits name unknown work "nope" (see content/sources.yaml)',
      'course/_course.yaml: credit of "s1" has unknown role "inspiration" (main or consulted)',
    ]);
  });

  it("is used by tracks, which must have credits", () => {
    const w: string[] = [];
    const t = parseTracks(
      [
        { id: "t", area: "a", courses: [], credits: [{ source: "s1" }] },
        { id: "u", area: "a", courses: [] },
      ],
      new Set(),
      new Set(["a"]),
      w,
      sources,
    );
    expect(t[0].credits).toEqual([{ source: "s1", role: "main", note: undefined }]);
    expect(w).toEqual(['content/tracks.yaml: track "u" has no credits (add credits: with the works the track is based on)']);
  });
});

describe("exercise credits", () => {
  const sources = parseSources(rawSources, []);

  it("parses the map of labels and writes the credit sentence", () => {
    const w: string[] = [];
    const m = parseExerciseCredits(
      {
        "ex-a": { source: "s1", relation: "adapted", where: "Exercise 2.3" },
        "ex-b": { source: "s2" },
        "ex-c": { cite: "Jockusch and Soare (1972)", relation: "result", where: "Theorem 2.1" },
        "ex-d": { source: "s1", relation: "related", where: "Example 4" },
      },
      "c/_exercise-credits.yaml",
      sources,
      w,
    );
    expect(w).toEqual([]);
    expect(exerciseCreditText(m.get("ex-a"), sources)).toBe("Adapted from Smith 2001, Exercise 2.3.");
    expect(exerciseCreditText(m.get("ex-b"), sources)).toBe("From Jones, Notes.");
    expect(exerciseCreditText(m.get("ex-c"), sources)).toBe("The result is from Jockusch and Soare (1972), Theorem 2.1.");
    expect(exerciseCreditText(m.get("ex-d"), sources)).toBe("Related to Smith 2001, Example 4.");
    expect(exerciseCreditText(undefined, sources)).toBe("Written for this course.");
  });

  it("reports malformed entries", () => {
    const w: string[] = [];
    parseExerciseCredits({ "ex-a": { relation: "copied" }, "ex-b": { source: "zzz" } }, "f", sources, w);
    expect(w).toEqual([
      'f: #ex-a has unknown relation "copied" (from, adapted, result, related)',
      "f: #ex-a needs a source or a cite",
      'f: #ex-b names unknown work "zzz" (see content/sources.yaml)',
    ]);
    expect(parseExerciseCredits(["x"], "f", sources, w).size).toBe(0);
  });
});

describe("credits in the catalog", () => {
  beforeEach(() => {
    useFixtureContent();
  });

  it("attaches credits to tracks, courses and exercises", () => {
    const cat = getCatalog();
    expect(cat.warnings).toEqual([]);
    expect(cat.sources.get("book-a")?.short).toBe("Author 2000");
    expect(cat.tracks[0].credits.map((c) => c.source)).toEqual(["book-a"]);
    const alpha = cat.courses.find((c) => c.id === "alpha")!;
    expect(alpha.credits).toEqual([
      { source: "book-a", role: "main", note: "Chapters 1–2." },
      { source: "notes-b", role: "consulted", note: undefined },
    ]);
    expect(cat.exercises.get("ex-do-it")?.creditText).toBe("Adapted from Author 2000, Exercise 1.2.");
    expect(cat.exercises.get("ex-other")?.creditText).toBe("Written for this course.");
  });

  it("does not change the hash of a credited exercise", () => {
    // the credit lives in _exercise-credits.yaml, outside the source of the exercise
    const ex = getCatalog().exercises.get("ex-do-it")!;
    expect(ex.credit?.source).toBe("book-a");
    expect(ex.hash).toMatch(/^[0-9a-f]+$/);
  });

  it("shows the credit below the objective of an exercise", async () => {
    const r = await renderLesson("alpha/one");
    const html = r!.segments.map((s) => (s.type === "html" ? s.html : "")).join("");
    expect(html).toMatch(/env-objective[\s\S]*env-credit[\s\S]*Credit\.[\s\S]*Adapted from Author 2000, Exercise 1\.2\./);
  });
});
