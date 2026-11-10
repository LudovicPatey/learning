"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { PROGRESS_EVENT, solvedCount } from "./progress";

type LessonRef = { id: string; title: string; href: string; quizCount: number };

/** Re-renders whenever quiz progress changes (in this tab or another). */
function useProgressTick() {
  const [tick, setTick] = useState(0);
  useEffect(() => {
    const bump = () => setTick((t) => t + 1);
    bump();
    window.addEventListener(PROGRESS_EVENT, bump);
    window.addEventListener("storage", bump);
    return () => {
      window.removeEventListener(PROGRESS_EVENT, bump);
      window.removeEventListener("storage", bump);
    };
  }, []);
  return tick;
}

function lessonState(id: string, total: number): "done" | "partial" | "" {
  const n = solvedCount(id);
  if (total > 0 && n >= total) return "done";
  return n > 0 ? "partial" : "";
}

/** A numbered step dot that turns green when all questions of the lesson are solved. */
export function StepDot({ lessonId, total, n, className = "step-num" }: { lessonId: string; total: number; n: number; className?: string }) {
  const tick = useProgressTick();
  const state = tick ? lessonState(lessonId, total) : "";
  return (
    <span className={`${className} ${state}`} title={state === "done" ? "All questions solved" : undefined}>
      {state === "done" ? "✓" : n}
    </span>
  );
}

/** Course progress bar with a Start / Continue button. */
export function CourseProgressCard({ lessons }: { lessons: LessonRef[] }) {
  const tick = useProgressTick();
  const total = lessons.reduce((s, l) => s + l.quizCount, 0);
  const solved = tick ? lessons.reduce((s, l) => s + Math.min(solvedCount(l.id), l.quizCount), 0) : 0;
  const started = solved > 0;
  const next = lessons.find((l) => lessonState(l.id, l.quizCount) !== "done") ?? lessons[0];
  const pct = total ? Math.round((100 * solved) / total) : 0;

  if (!lessons.length) return null;
  return (
    <div className="course-start">
      <div className="progress-label">
        <span>Progress</span>
        <span>
          {solved}/{total} questions answered
        </span>
      </div>
      <div className="progress">
        <i style={{ width: `${pct}%` }} />
      </div>
      <Link className="btn btn-primary btn-lg" href={next.href}>
        {started ? (pct === 100 ? "Review" : "Continue") : "Start"}
      </Link>
      {started && pct < 100 && <span className="small muted">Next: {next.title}</span>}
      <span className="small muted">Progress is saved in this browser.</span>
    </div>
  );
}

/** Thin bar at the top of the window showing how far the reader has scrolled. */
export function ReadProgress() {
  const [w, setW] = useState(0);
  useEffect(() => {
    const on = () => {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      setW(h > 0 ? Math.min(100, (100 * window.scrollY) / h) : 0);
    };
    on();
    window.addEventListener("scroll", on, { passive: true });
    window.addEventListener("resize", on);
    return () => {
      window.removeEventListener("scroll", on);
      window.removeEventListener("resize", on);
    };
  }, []);
  return <div className="read-progress" style={{ width: `${w}%` }} aria-hidden />;
}
