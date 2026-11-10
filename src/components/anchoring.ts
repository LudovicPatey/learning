// Text-quote anchoring of comments (same idea as the W3C Web Annotation
// TextQuoteSelector used by Hypothesis): a comment stores the selected text,
// a little context before/after it, and its approximate position. On load we
// search the lesson text for the quote, so comments survive edits elsewhere.

import type { Anchor } from "@/lib/comment-types";

// Text that is not part of the visible reading flow.
const SKIP = ".katex-mathml, .no-annotate, script, style, button, input, textarea, select";

export type TextIndex = { text: string; nodes: Text[]; starts: number[] };

export function buildIndex(root: HTMLElement): TextIndex {
  const nodes: Text[] = [];
  const starts: number[] = [];
  let text = "";
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(n) {
      const p = n.parentElement;
      return !p || p.closest(SKIP) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
    },
  });
  while (walker.nextNode()) {
    const n = walker.currentNode as Text;
    nodes.push(n);
    starts.push(text.length);
    text += n.data;
  }
  return { text, nodes, starts };
}

function pointToOffset(idx: TextIndex, container: Node, offset: number): number {
  if (container.nodeType === Node.TEXT_NODE) {
    const i = idx.nodes.indexOf(container as Text);
    if (i >= 0) return idx.starts[i] + offset;
  }
  const point = document.createRange();
  point.setStart(container, offset);
  for (let i = 0; i < idx.nodes.length; i++) {
    if (point.comparePoint(idx.nodes[i], 0) >= 0) return idx.starts[i];
  }
  return idx.text.length;
}

function offsetsToRange(idx: TextIndex, start: number, end: number): Range | null {
  const r = document.createRange();
  let okStart = false;
  for (let i = 0; i < idx.nodes.length; i++) {
    const s = idx.starts[i];
    const len = idx.nodes[i].data.length;
    if (!okStart && start >= s && start < s + len) {
      r.setStart(idx.nodes[i], start - s);
      okStart = true;
    }
    if (okStart && end > s && end <= s + len) {
      r.setEnd(idx.nodes[i], end - s);
      return r;
    }
  }
  return null;
}

const mathBox = (n: Node | null) => {
  const el = n?.nodeType === Node.ELEMENT_NODE ? (n as Element) : n?.parentElement;
  return el?.closest(".katex-display") ?? el?.closest(".katex") ?? null;
};

/** Never cut a formula in half: extend the selection to whole formulas. */
function snapToMath(range: Range, root: HTMLElement) {
  const a = mathBox(range.startContainer);
  if (a && root.contains(a)) range.setStartBefore(a);
  const b = mathBox(range.endContainer);
  if (b && root.contains(b)) range.setEndAfter(b);
}

/** Selected content as readable text, with formulas turned back into $TeX$. */
function displayText(range: Range): string {
  const frag = range.cloneContents();
  frag.querySelectorAll(".katex").forEach((k) => {
    const tex = k.querySelector('annotation[encoding="application/x-tex"]')?.textContent ?? "";
    const display = k.parentElement?.classList.contains("katex-display");
    k.replaceWith(document.createTextNode(display ? ` $$${tex}$$ ` : `$${tex}$`));
  });
  frag.querySelectorAll(SKIP).forEach((n) => n.parentNode?.removeChild(n));
  return (frag.textContent ?? "").replace(/\s+/g, " ").trim().slice(0, 2000);
}

export function selectionInside(root: HTMLElement): Range | null {
  const sel = window.getSelection();
  if (!sel || sel.rangeCount === 0 || sel.isCollapsed) return null;
  const r = sel.getRangeAt(0);
  if (!root.contains(r.commonAncestorContainer)) return null;
  return r;
}

export function rangeToAnchor(root: HTMLElement, selected: Range): Anchor | null {
  const range = selected.cloneRange();
  snapToMath(range, root);
  const idx = buildIndex(root);
  const s = pointToOffset(idx, range.startContainer, range.startOffset);
  const e = pointToOffset(idx, range.endContainer, range.endOffset);
  if (e <= s) return null;
  const exact = idx.text.slice(s, e);
  if (!exact.trim()) return null;
  return {
    exact,
    prefix: idx.text.slice(Math.max(0, s - 32), s),
    suffix: idx.text.slice(e, e + 32),
    position: s,
    display: displayText(range),
  };
}

function commonSuffix(a: string, b: string) {
  let n = 0;
  while (n < a.length && n < b.length && a[a.length - 1 - n] === b[b.length - 1 - n]) n++;
  return n;
}
function commonPrefix(a: string, b: string) {
  let n = 0;
  while (n < a.length && n < b.length && a[n] === b[n]) n++;
  return n;
}

/** Find the best occurrence of the quote. Returns null when the passage no longer exists. */
export function anchorToRange(idx: TextIndex, a: Anchor): Range | null {
  let best = -1;
  let bestScore = -Infinity;
  for (let i = idx.text.indexOf(a.exact); i !== -1; i = idx.text.indexOf(a.exact, i + 1)) {
    const before = idx.text.slice(Math.max(0, i - a.prefix.length), i);
    const after = idx.text.slice(i + a.exact.length, i + a.exact.length + a.suffix.length);
    const score = commonSuffix(before, a.prefix) + commonPrefix(after, a.suffix) - Math.abs(i - a.position) / 10000;
    if (score > bestScore) {
      bestScore = score;
      best = i;
    }
  }
  return best < 0 ? null : offsetsToRange(idx, best, best + a.exact.length);
}

export function caretAt(x: number, y: number): { node: Node; offset: number } | null {
  const d = document as Document & {
    caretPositionFromPoint?: (x: number, y: number) => { offsetNode: Node; offset: number } | null;
    caretRangeFromPoint?: (x: number, y: number) => Range | null;
  };
  if (d.caretPositionFromPoint) {
    const p = d.caretPositionFromPoint(x, y);
    return p ? { node: p.offsetNode, offset: p.offset } : null;
  }
  const r = d.caretRangeFromPoint?.(x, y);
  return r ? { node: r.startContainer, offset: r.startOffset } : null;
}
