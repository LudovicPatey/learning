import { beforeEach, describe, expect, it } from "vitest";
import fs from "node:fs";
import path from "node:path";
import { useFixtureContent } from "./helpers";
import { matchesQuery, normalizeForSearch, parseTracks, trackGraph, trackOfCourse, type Track } from "@/lib/tracks";
import { getCatalog } from "@/lib/content";

const courses = [
  { id: "a", prerequisites: [] },
  { id: "b", prerequisites: ["a"] },
  { id: "c", prerequisites: ["b"] },
  { id: "x", prerequisites: ["c"] },
  { id: "y", prerequisites: ["x", "b"] },
  { id: "z", prerequisites: ["y", "a"] },
];
const track: Track = { id: "t", title: "T", area: "logic", description: "", courses: ["x", "y", "z"] };

describe("trackGraph", () => {
  it("keeps only the edges inside the track", () => {
    expect(trackGraph(track, courses).edges).toEqual([
      ["x", "y"],
      ["y", "z"],
    ]);
  });

  it("computes depths from internal prerequisites only", () => {
    const { depth } = trackGraph(track, courses);
    expect([...depth.entries()]).toEqual([
      ["x", 0],
      ["y", 1],
      ["z", 2],
    ]);
  });

  it("reduces external prerequisites to the minimal ones", () => {
    // x needs c, y needs b, z needs a; but c depends on b and b on a, so c suffices.
    expect(trackGraph(track, courses).external).toEqual(["c"]);
  });

  it("ignores unknown prerequisites and survives cycles", () => {
    const cyc = [
      { id: "p", prerequisites: ["q", "missing"] },
      { id: "q", prerequisites: ["p"] },
    ];
    const g = trackGraph({ ...track, courses: ["p", "q"] }, cyc);
    expect(g.external).toEqual([]);
    expect(g.depth.size).toBe(2);
  });
});

describe("parseTracks", () => {
  it("reports unknown courses, areas and duplicates", () => {
    const warnings: string[] = [];
    const t = parseTracks(
      [
        { id: "t", area: "logic", courses: ["a", "nope"] },
        { id: "t", area: "mystery", courses: [] },
      ],
      new Set(["a"]),
      new Set(["logic"]),
      warnings,
    );
    expect(t[0].courses).toEqual(["a"]);
    expect(warnings).toEqual([
      'content/tracks.yaml: track "t" lists unknown course "nope"',
      'content/tracks.yaml: duplicate track "t"',
      'content/tracks.yaml: track "t" has unknown area "mystery"',
    ]);
  });

  it("assigns each course to its first track", () => {
    const m = trackOfCourse([
      { ...track, id: "one", courses: ["a", "b"] },
      { ...track, id: "two", courses: ["b", "c"] },
    ]);
    expect(m.get("b")).toBe("one");
    expect(m.get("c")).toBe("two");
    expect(m.has("z")).toBe(false);
  });
});

describe("search", () => {
  it("ignores case, accents and punctuation", () => {
    expect(normalizeForSearch("Gödel's β-function")).toBe("godel s β function");
    expect(matchesQuery("Kleene's fixed point theorem", "fixed KLEENE")).toBe(true);
    expect(matchesQuery("Kleene's fixed point theorem", "fixed rice")).toBe(false);
    expect(matchesQuery("anything", "  ")).toBe(true);
  });

  it("matches Greek letters written with indices", () => {
    expect(matchesQuery("Π⁰₁ classes", "π01")).toBe(true);
  });
});

describe("tracks in the catalog", () => {
  let root: string;
  beforeEach(() => {
    root = useFixtureContent();
  });

  it("marks courses of a track, and leaves the others specialized", () => {
    const cat = getCatalog();
    expect(cat.tracks.map((t) => t.id)).toEqual(["main"]);
    expect(cat.courses.find((c) => c.id === "alpha")?.track).toBe("main");
    expect(cat.courses.find((c) => c.id === "beta")?.track).toBeUndefined();
    expect(cat.warnings).toEqual([]);
  });

  it("works without a tracks file", () => {
    fs.rmSync(path.join(root, "tracks.yaml"));
    const cat = getCatalog();
    expect(cat.tracks).toEqual([]);
    expect(cat.courses.every((c) => c.track === undefined)).toBe(true);
  });
});
