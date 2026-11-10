import katex from "katex";
import { macros } from "@/lib/katex-macros";

const ESC: Record<string, string> = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
const escape = (s: string) => s.replace(/[&<>"']/g, (c) => ESC[c]);

/** Render user text safely: HTML is escaped, $…$ and $$…$$ are typeset with KaTeX. */
export function renderMathText(src: string): string {
  const out: string[] = [];
  const re = /\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g;
  let last = 0;
  for (let m = re.exec(src); m; m = re.exec(src)) {
    out.push(escape(src.slice(last, m.index)).replace(/\n/g, "<br>"));
    const tex = m[1] ?? m[2];
    out.push(
      katex.renderToString(tex, {
        displayMode: m[1] !== undefined,
        throwOnError: false,
        macros: macros(),
        trust: false,
        maxSize: 10,
        maxExpand: 200,
      }),
    );
    last = m.index + m[0].length;
  }
  out.push(escape(src.slice(last)).replace(/\n/g, "<br>"));
  return out.join("");
}
