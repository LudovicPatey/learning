// Reading time of a lesson (AGENTS.md, "Small courses, small lessons").
// Pure functions, tested in tests/reading-time.test.ts; used by scripts/check-content.ts
// and scripts/durations.ts.
//
// The reading time counts the text that is open when the page loads: the body of the
// lesson without its frontmatter, the lines of inline SVG, the collapsed blocks
// (quizzes, solutions, hints) and the block of further exercises. Formulas count as
// words. The stated duration is the reading time at 55 words per minute, rounded to a
// multiple of 5 minutes.

export const WORDS_PER_MINUTE = 55;
/** Longest stated duration of a lesson, in minutes. */
export const MAX_DURATION = 45;
const COLLAPSED = /^(:{3,})(quiz|solution|hint)\b/;

/** The words of the text open when the page loads (see above). */
export function openTextWords(source: string): number {
  const lines = source.replace(/\r\n?/g, "\n").split("\n");
  let i = 0;
  if (lines[0]?.trim() === "---") {
    i = 1;
    while (i < lines.length && lines[i].trim() !== "---") i++;
    i++;
  }
  let words = 0;
  let svg = false;
  let closing: RegExp | null = null;
  for (; i < lines.length; i++) {
    const line = lines[i];
    if (closing) {
      if (closing.test(line)) closing = null;
      continue;
    }
    if (/^:{5,}exercises\b/.test(line)) break;
    if (svg || /<svg\b/.test(line)) {
      svg = !/<\/svg>/.test(line);
      continue;
    }
    const m = COLLAPSED.exec(line);
    if (m) {
      // a container closes at a fence of at least as many colons
      closing = new RegExp(`^:{${m[1].length},}\\s*$`);
      continue;
    }
    words += line.split(/\s+/).filter(Boolean).length;
  }
  return words;
}

/** The stated duration for `words` of open text: minutes rounded to a multiple of 5, at least 5. */
export function durationFor(words: number): number {
  return Math.max(5, Math.round(words / WORDS_PER_MINUTE / 5) * 5);
}
