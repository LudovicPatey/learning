// Checks the real course content: every lesson renders cleanly. This test
// fails when a lesson contains a broken reference, a malformed quiz or a
// formula KaTeX cannot typeset — run it before every commit.
import { describe, expect, it } from "vitest";
import { getCatalog, renderLesson } from "@/lib/content";
import { allVersions } from "@/lib/versions";

delete process.env.CONTENT_DIR;
const catalog = getCatalog();

describe("course content", () => {
  it("has a consistent catalog", () => {
    expect(catalog.warnings).toEqual([]);
    expect(catalog.lessons.size).toBeGreaterThan(0);
  });

  it.each([...catalog.lessons.keys()])("%s renders without warnings", async (id) => {
    const r = (await renderLesson(id))!;
    expect(r.warnings).toEqual([]);
    for (const s of r.segments) {
      if (s.type === "html") expect(s.html).not.toContain("katex-error");
      else {
        for (const q of s.quiz.questions) {
          expect(q.options.length).toBeGreaterThanOrEqual(2);
          expect(q.options.some((o) => o.correct)).toBe(true);
          expect(JSON.stringify(q)).not.toContain("katex-error");
        }
      }
    }
  });

  it("gives every lesson a title, a summary and a duration", () => {
    for (const l of catalog.lessons.values()) {
      expect(l.title, l.id).not.toBe(l.slug);
      expect(l.summary, l.id).not.toBe("");
      expect(l.duration, l.id).toBeGreaterThan(0);
    }
  });

  it.each(allVersions().map((v) => [v.course, v.version]))("released version %s %s renders", async (course, version) => {
    const cat = getCatalog({ course, version });
    for (const l of cat.lessons.values()) {
      if (l.course !== course) continue;
      const r = (await renderLesson(l.id, { course, version }))!;
      expect(r.warnings, l.id).toEqual([]);
    }
  });
});
