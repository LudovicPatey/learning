import katex from "katex";
import { describe, expect, it } from "vitest";
import { bibtexEntry, citationKey } from "@/lib/citation";
import { katexMacros, macros } from "@/lib/katex-macros";
import { renderMathText } from "@/components/math-text";

const base = {
  path: "/courses/c/v/1.0/l",
  courseId: "c",
  courseTitle: "Models of computation",
  lessonSlug: "l",
  lessonTitle: "Turing machines & tapes",
  lessonNumber: 2,
  authors: ["A. Turing", "A. Church"],
  url: "https://example.org/courses/c/v/1.0/l",
};

describe("citation", () => {
  it("builds keys including the version", () => {
    expect(citationKey({ courseId: "c", lessonSlug: "l", version: "1.0" })).toBe("c-l-v1.0");
    expect(citationKey({ courseId: "c", lessonSlug: "l" })).toBe("c-l");
  });

  it("produces a BibTeX entry for a release", () => {
    const bib = bibtexEntry({ ...base, version: "1.0", date: "2026-03-01" });
    expect(bib).toMatch(/^@misc\{c-l-v1\.0,/);
    expect(bib).toContain("author = {A. Turing and A. Church}");
    expect(bib).toContain("title = {{Turing machines \\& tapes}}");
    expect(bib).toContain("version 1.0");
    expect(bib).toContain("year = {2026}");
    expect(bib).toContain(`url = {${base.url}}`);
    expect(bib).not.toContain("Unreleased");
  });

  it("flags unreleased working versions and omits empty authors", () => {
    const bib = bibtexEntry({ ...base, authors: [] });
    expect(bib).not.toContain("author");
    expect(bib).toContain("Unreleased working version");
  });
});

describe("KaTeX macros", () => {
  it.each(Object.keys(katexMacros))("%s renders without error", (name) => {
    const args = (katexMacros[name].match(/#\d/g) ?? []).length;
    const tex = name + "{x}".repeat(args);
    expect(() => katex.renderToString(tex, { macros: macros(), throwOnError: true })).not.toThrow();
  });

  it("gives a fresh macro table each time", () => {
    const m = macros();
    m["\\nat"] = "changed";
    expect(macros()["\\nat"]).toBe("\\mathbb{N}");
  });
});

describe("renderMathText (user comments)", () => {
  it("escapes HTML", () => {
    const out = renderMathText('<script>alert("x")</script> & co');
    expect(out).not.toContain("<script>");
    expect(out).toContain("&lt;script&gt;");
    expect(out).toContain("&amp; co");
  });

  it("typesets inline and display math", () => {
    const out = renderMathText("Let $\\Phi_e(x)\\converge$ and $$x^2$$");
    expect(out).toContain('class="katex"');
    expect(out).toContain("katex-display");
    expect(out).not.toContain("katex-error");
  });

  it("keeps line breaks", () => {
    expect(renderMathText("a\nb")).toBe("a<br>b");
  });

  it("does not execute untrusted commands", () => {
    const out = renderMathText("$\\href{javascript:alert(1)}{x}$");
    expect(out).not.toContain('href="javascript');
  });
});
