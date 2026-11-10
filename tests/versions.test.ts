import fs from "node:fs";
import path from "node:path";
import { beforeEach, describe, expect, it } from "vitest";
import { useFixtureContent, stripTags } from "./helpers";
import { allVersions, compareVersions, hasVersion, latestVersion, listVersions } from "@/lib/versions";
import { releaseCourse, ReleaseError } from "@/lib/release";
import { getCatalog, renderLesson } from "@/lib/content";

let root: string;
beforeEach(() => {
  root = useFixtureContent();
});

const text = async (id: string, version?: string) => {
  const r = await renderLesson(id, version ? { course: id.split("/")[0], version } : undefined);
  return r ? r.segments.map((s) => (s.type === "html" ? s.html : "")).join("\n") : "";
};

describe("compareVersions", () => {
  it("compares numerically", () => {
    expect(compareVersions("1.10", "1.9")).toBeGreaterThan(0);
    expect(compareVersions("1.0", "1.0.0")).toBe(0);
    expect(compareVersions("0.9", "1.0")).toBeLessThan(0);
  });
});

describe("releaseCourse", () => {
  it("snapshots the working copy and records the release", () => {
    const info = releaseCourse({ course: "alpha", version: "1.0", notes: "First", date: "2026-01-02" });
    expect(info).toEqual({ version: "1.0", date: "2026-01-02", notes: "First" });
    expect(fs.existsSync(path.join(root, "_versions/alpha/1.0/one.md"))).toBe(true);
    expect(fs.existsSync(path.join(root, "_versions/alpha/1.0/_course.yaml"))).toBe(true);
    expect(listVersions("alpha")).toEqual([info]);
    expect(latestVersion("alpha")?.version).toBe("1.0");
    expect(hasVersion("alpha", "1.0")).toBe(true);
    expect(allVersions()).toEqual([{ course: "alpha", version: "1.0" }]);
  });

  it("refuses malformed, duplicate or older versions", () => {
    expect(() => releaseCourse({ course: "alpha", version: "v1" })).toThrow(ReleaseError);
    releaseCourse({ course: "alpha", version: "1.1" });
    expect(() => releaseCourse({ course: "alpha", version: "1.1" })).toThrow(/already exists/);
    expect(() => releaseCourse({ course: "alpha", version: "1.0" })).toThrow(/greater/);
    expect(() => releaseCourse({ course: "nope", version: "1.0" })).toThrow(/Unknown course/);
  });

  it("lists versions most recent first", () => {
    releaseCourse({ course: "alpha", version: "1.0" });
    releaseCourse({ course: "alpha", version: "1.2" });
    releaseCourse({ course: "alpha", version: "1.10" });
    expect(listVersions("alpha").map((v) => v.version)).toEqual(["1.10", "1.2", "1.0"]);
  });
});

describe("rendering released versions", () => {
  it("keeps the released text when the working copy changes", async () => {
    releaseCourse({ course: "alpha", version: "1.0" });
    const file = path.join(root, "alpha/one.md");
    fs.writeFileSync(file, fs.readFileSync(file, "utf8").replace("Intro with", "Revised intro with"));

    expect(stripTags(await text("alpha/one"))).toContain("Revised intro");
    const old = stripTags(await text("alpha/one", "1.0"));
    expect(old).toContain("Intro with");
    expect(old).not.toContain("Revised");
  });

  it("marks lessons with their version and keeps links inside the release", async () => {
    releaseCourse({ course: "alpha", version: "1.0" });
    const meta = getCatalog({ course: "alpha", version: "1.0" }).lessons.get("alpha/one")!;
    expect(meta.version).toBe("1.0");
    expect(meta.file).toContain(path.join("_versions", "alpha", "1.0"));
    const h = await text("alpha/one", "1.0");
    expect(h).toContain('href="/courses/alpha/v/1.0/two#lem-two"');
  });

  it("does not affect other courses", async () => {
    releaseCourse({ course: "alpha", version: "1.0" });
    const cat = getCatalog({ course: "alpha", version: "1.0" });
    expect(cat.lessons.get("beta/three")?.version).toBeUndefined();
  });
});
