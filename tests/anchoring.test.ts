// @vitest-environment jsdom
import { beforeEach, describe, expect, it } from "vitest";
import { anchorToRange, buildIndex, rangeToAnchor } from "@/components/anchoring";

let root: HTMLElement;

beforeEach(() => {
  document.body.innerHTML = `
    <article id="a">
      <p id="p1">The halting problem is undecidable.</p>
      <p id="p2">Let <span class="katex"><span class="katex-mathml"><math><semantics><mi>e</mi><annotation encoding="application/x-tex">e</annotation></semantics></math></span><span class="katex-html">e</span></span> be a code. The problem is hard.</p>
      <p id="p3">The problem is hard.</p>
      <button class="no-annotate">Check</button>
    </article>`;
  root = document.getElementById("a")!;
});

function selectText(el: Element, from: string, to?: string): Range {
  const textNode = [...el.childNodes].find((n) => n.nodeType === Node.TEXT_NODE && n.textContent!.includes(from)) as Text;
  const start = textNode.data.indexOf(from);
  const r = document.createRange();
  r.setStart(textNode, start);
  r.setEnd(textNode, start + (to ?? from).length);
  return r;
}

describe("buildIndex", () => {
  it("skips MathML and interface elements", () => {
    const idx = buildIndex(root);
    expect(idx.text).not.toContain("Check");
    // the formula appears once (from the HTML rendering), not twice
    expect(idx.text.match(/Let e be/g)).toHaveLength(1);
  });
});

describe("text quote anchors", () => {
  it("round-trips a selection", () => {
    const anchor = rangeToAnchor(root, selectText(document.getElementById("p1")!, "halting problem"))!;
    expect(anchor.exact).toBe("halting problem");
    expect(anchor.display).toBe("halting problem");
    const r = anchorToRange(buildIndex(root), anchor)!;
    expect(r.toString()).toBe("halting problem");
  });

  it("uses context to choose between repeated passages", () => {
    const p3 = document.getElementById("p3")!;
    const anchor = rangeToAnchor(root, selectText(p3, "problem is hard"))!;
    const r = anchorToRange(buildIndex(root), anchor)!;
    expect(r.startContainer.parentElement?.id).toBe("p3");
  });

  it("survives edits elsewhere in the document", () => {
    const anchor = rangeToAnchor(root, selectText(document.getElementById("p3")!, "problem is hard"))!;
    document.getElementById("p1")!.textContent = "A completely different first paragraph, much longer than before.";
    const r = anchorToRange(buildIndex(root), anchor)!;
    expect(r.startContainer.parentElement?.id).toBe("p3");
  });

  it("returns null when the passage disappeared", () => {
    const anchor = rangeToAnchor(root, selectText(document.getElementById("p1")!, "undecidable"))!;
    document.getElementById("p1")!.textContent = "Rewritten.";
    expect(anchorToRange(buildIndex(root), anchor)).toBeNull();
  });

  it("extends selections to whole formulas and shows them as TeX", () => {
    const p2 = document.getElementById("p2")!;
    const r = document.createRange();
    r.setStart(p2.firstChild!, 0); // "Let "
    const htmlPart = p2.querySelector(".katex-html")!.firstChild!;
    r.setEnd(htmlPart, 0); // inside the formula
    const anchor = rangeToAnchor(root, r)!;
    expect(anchor.exact).toBe("Let e");
    expect(anchor.display).toBe("Let $e$");
  });

  it("rejects empty selections", () => {
    const r = document.createRange();
    r.setStart(document.getElementById("p1")!.firstChild!, 3);
    r.collapse(true);
    expect(rangeToAnchor(root, r)).toBeNull();
  });
});
