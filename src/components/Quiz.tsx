"use client";

import { useEffect, useId, useState } from "react";
import type { QuizData, QuizQuestion } from "@/lib/content";
import { readProgress, writeProgress } from "./progress";

type Phase = "answering" | "wrong" | "correct" | "revealed";

function Question({ q, index, total, storageKey }: { q: QuizQuestion; index: number; total: number; storageKey: string }) {
  const name = useId();
  const [selected, setSelected] = useState<Set<number>>(new Set());
  const [phase, setPhase] = useState<Phase>("answering");
  const [solvedBefore, setSolvedBefore] = useState(false);

  useEffect(() => setSolvedBefore(readProgress(storageKey) === "correct"), [storageKey]);

  const correctSet = q.options.flatMap((o, i) => (o.correct ? [i] : []));
  const locked = phase === "correct" || phase === "revealed";

  function toggle(i: number) {
    if (locked) return;
    setPhase("answering");
    setSelected((prev) => {
      if (!q.multi) return new Set([i]);
      const next = new Set(prev);
      if (next.has(i)) next.delete(i);
      else next.add(i);
      return next;
    });
  }

  function check() {
    const ok = selected.size === correctSet.length && correctSet.every((i) => selected.has(i));
    setPhase(ok ? "correct" : "wrong");
    if (ok) {
      writeProgress(storageKey, "correct");
      setSolvedBefore(true);
    } else if (readProgress(storageKey) !== "correct") writeProgress(storageKey, "attempted");
  }

  function reset() {
    setSelected(new Set());
    setPhase("answering");
  }

  return (
    <div className={`quiz-q phase-${phase}`}>
      <div className="quiz-q-head no-annotate">
        <span>
          Question {index + 1}
          {total > 1 ? ` of ${total}` : ""}
        </span>
        <span className="quiz-q-hint">{q.multi ? "Select all that apply" : "Select one answer"}</span>
        {solvedBefore && phase === "answering" && <span className="quiz-badge">answered correctly before</span>}
      </div>
      <div className="quiz-stem" dangerouslySetInnerHTML={{ __html: q.stemHtml }} />
      <ul className="quiz-options">
        {q.options.map((o, i) => {
          const isSel = selected.has(i);
          const showTruth = phase === "correct" || phase === "revealed";
          const cls = [
            "quiz-option",
            isSel ? "is-selected" : "",
            phase !== "answering" && isSel && o.correct ? "is-correct" : "",
            phase !== "answering" && isSel && !o.correct ? "is-wrong" : "",
            showTruth && !isSel && o.correct ? "is-missed" : "",
          ].join(" ");
          const showExplanation = o.explanationHtml && (showTruth || (phase === "wrong" && isSel));
          return (
            <li key={i} className={cls}>
              <label
                onClick={(e) => {
                  // Selecting text to comment on it should not toggle the answer.
                  if (!window.getSelection()?.isCollapsed) e.preventDefault();
                }}
              >
                <input
                  type={q.multi ? "checkbox" : "radio"}
                  name={name}
                  checked={isSel}
                  disabled={locked}
                  onChange={() => toggle(i)}
                />
                <span className="quiz-option-text" dangerouslySetInnerHTML={{ __html: o.html }} />
              </label>
              {showExplanation && <div className="quiz-expl" dangerouslySetInnerHTML={{ __html: o.explanationHtml }} />}
            </li>
          );
        })}
      </ul>
      <div className="quiz-actions no-annotate">
        {phase === "answering" && (
          <button className="btn btn-primary" disabled={selected.size === 0} onClick={check}>
            Check
          </button>
        )}
        {phase === "wrong" && (
          <>
            <span className="quiz-verdict wrong">Incorrect.</span>
            <button className="btn" onClick={reset}>
              Try again
            </button>
            <button className="btn btn-ghost" onClick={() => setPhase("revealed")}>
              Show answer
            </button>
          </>
        )}
        {phase === "correct" && <span className="quiz-verdict correct">Correct.</span>}
        {locked && (
          <button className="btn btn-ghost" onClick={reset}>
            Reset
          </button>
        )}
      </div>
      {locked && q.discussionHtml && <div className="quiz-discussion" dangerouslySetInnerHTML={{ __html: q.discussionHtml }} />}
    </div>
  );
}

/**
 * Comprehension questions. Collapsed by default to a single line, so that they
 * stay next to the proof they refer to without interrupting the reading.
 */
export function Quiz({ quiz, lessonId, defaultOpen = false }: { quiz: QuizData; lessonId: string; defaultOpen?: boolean }) {
  const [open, setOpen] = useState(defaultOpen);
  const [solved, setSolved] = useState(0);
  const keys = quiz.questions.map((_, i) => `${lessonId}#${quiz.id}#${i}`);
  const n = quiz.questions.length;

  useEffect(() => {
    const update = () => setSolved(keys.filter((k) => readProgress(k) === "correct").length);
    update();
    window.addEventListener("cl-progress", update);
    return () => window.removeEventListener("cl-progress", update);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [lessonId, quiz.id]);

  return (
    <aside className={`quiz ${open ? "is-open" : "is-closed"}`} id={quiz.id} aria-label="Comprehension questions">
      <button className="quiz-title no-annotate" aria-expanded={open} onClick={() => setOpen((o) => !o)}>
        <span className="quiz-chevron" aria-hidden>
          ▸
        </span>
        <span className="quiz-name">{quiz.title ? `Questions on ${quiz.title}` : "Comprehension questions"}</span>
        <span className="quiz-count">
          {n} question{n > 1 ? "s" : ""}
          {solved > 0 && ` · ${solved} answered`}
        </span>
      </button>
      {open && (
        <div className="quiz-body">
          {quiz.questions.map((q, i) => (
            <Question key={i} q={q} index={i} total={n} storageKey={keys[i]} />
          ))}
        </div>
      )}
    </aside>
  );
}
