// Lists the lessons whose stated duration differs from the reading time of their open
// text (src/lib/reading-time.ts), and with --write sets it in their frontmatter.
// Usage: npm run durations [-- --write]
import fs from "node:fs";
import { getCatalog } from "../src/lib/content.ts";
import { MAX_DURATION, durationFor, openTextWords } from "../src/lib/reading-time.ts";

const write = process.argv.includes("--write");
let changed = 0;
for (const l of getCatalog().lessons.values()) {
  const source = fs.readFileSync(l.file, "utf8");
  const words = openTextWords(source);
  const d = durationFor(words);
  if (d > MAX_DURATION) console.log(`  ! ${l.id}: ${words} words, ${d} minutes: too long, split it`);
  if (l.duration === d) continue;
  changed++;
  console.log(`  ${l.id}: ${l.duration ?? "-"} → ${d} (${words} words)`);
  if (!write) continue;
  const fm = /^---\n([\s\S]*?)\n---/.exec(source);
  if (!fm) throw new Error(`${l.file}: no frontmatter`);
  const head = /^duration:.*$/m.test(fm[1]) ? fm[1].replace(/^duration:.*$/m, `duration: ${d}`) : `${fm[1]}\nduration: ${d}`;
  fs.writeFileSync(l.file, source.replace(fm[0], `---\n${head}\n---`));
}
console.log(`${changed} lesson(s) with a different duration${write ? ": updated" : " (--write to update)"}.`);
