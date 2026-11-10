// Quiz progress, kept in the reader's browser for now.
// (Later: sync to the server for signed-in users.)

const PREFIX = "cl:quiz:";
export const PROGRESS_EVENT = "cl-progress";

export type QuizState = "correct" | "attempted";

export function readProgress(key: string): QuizState | null {
  try {
    return (localStorage.getItem(PREFIX + key) as QuizState | null) ?? null;
  } catch {
    return null;
  }
}

export function writeProgress(key: string, state: QuizState) {
  try {
    localStorage.setItem(PREFIX + key, state);
  } catch {}
  window.dispatchEvent(new Event(PROGRESS_EVENT));
}

/** Number of questions of a lesson answered correctly. */
export function solvedCount(lessonId: string): number {
  let n = 0;
  try {
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k?.startsWith(`${PREFIX}${lessonId}#`) && localStorage.getItem(k) === "correct") n++;
    }
  } catch {}
  return n;
}
