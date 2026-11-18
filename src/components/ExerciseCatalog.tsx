"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { matchesQuery } from "@/lib/tracks";
import { EndorseControl, useEndorsements } from "./Endorsements";

export type ExerciseEntry = {
  id: string;
  number: string;
  title?: string;
  objectiveHtml: string;
  objectiveText: string;
  /** The sentence crediting the exercise, as HTML. */
  creditHtml: string;
  /** Whether the exercise comes from a published work. */
  credited: boolean;
  difficulty?: number;
  featured: boolean;
  hash: string;
  course: string;
  href: string;
  lessons: { id: string; title: string; href: string }[];
};

type CourseRef = { id: string; title: string; color: string; track?: string };
type TrackRef = { id: string; title: string; primary: boolean };

const PAGE = 120;

/** Searchable, filterable list of all exercises, grouped by course. */
export function ExerciseCatalog({ entries, courses, tracks }: { entries: ExerciseEntry[]; courses: CourseRef[]; tracks: TrackRef[] }) {
  const [query, setQuery] = useState("");
  const [track, setTrack] = useState("all");
  const [course, setCourse] = useState("all");
  const [lesson, setLesson] = useState<string | null>(null);
  const [difficulty, setDifficulty] = useState("all");
  const [kind, setKind] = useState<"all" | "featured" | "further">("all");
  const [endorsed, setEndorsed] = useState<"all" | "yes" | "no">("all");
  const [limit, setLimit] = useState(PAGE);
  const endorsements = useEndorsements();

  // Initial filters from the URL: /exercises?course=fundamentals, ?lesson=fundamentals/halting-problem, ?track=higher
  useEffect(() => {
    const p = new URLSearchParams(window.location.search);
    const c = p.get("course");
    const t = p.get("track");
    const l = p.get("lesson");
    const q = p.get("q");
    if (c && courses.some((x) => x.id === c)) setCourse(c);
    if (t && (t === "specialized" || tracks.some((x) => x.id === t))) setTrack(t);
    if (l && entries.some((e) => e.lessons.some((x) => x.id === l))) setLesson(l);
    if (q) setQuery(q);
  }, [courses, tracks, entries]);

  const courseById = useMemo(() => new Map(courses.map((c) => [c.id, c])), [courses]);
  const shownCourses = courses.filter((c) => track === "all" || (track === "specialized" ? !c.track : c.track === track));

  const shown = useMemo(
    () =>
      entries.filter((e) => {
        const c = courseById.get(e.course);
        if (track !== "all" && (track === "specialized" ? c?.track : c?.track !== track)) return false;
        if (course !== "all" && e.course !== course) return false;
        if (lesson && !e.lessons.some((l) => l.id === lesson)) return false;
        if (difficulty !== "all" && String(e.difficulty ?? "") !== difficulty) return false;
        if (kind !== "all" && e.featured !== (kind === "featured")) return false;
        if (endorsed !== "all" && endorsements.loaded) {
          const has = (endorsements.byExercise.get(e.id) ?? []).length > 0;
          if (has !== (endorsed === "yes")) return false;
        }
        const text = [e.title ?? "", e.objectiveText, c?.title ?? "", ...e.lessons.map((l) => l.title)].join(" ");
        return matchesQuery(text, query);
      }),
    [entries, courseById, track, course, lesson, difficulty, kind, endorsed, endorsements, query],
  );

  useEffect(() => setLimit(PAGE), [track, course, lesson, difficulty, kind, endorsed, query]);

  // group the visible part by course, keeping the order of the entries
  const groups: { course: CourseRef; items: ExerciseEntry[] }[] = [];
  for (const e of shown.slice(0, limit)) {
    const last = groups[groups.length - 1];
    if (last && last.course.id === e.course) last.items.push(e);
    else groups.push({ course: courseById.get(e.course)!, items: [e] });
  }
  const lessonTitle = lesson ? entries.flatMap((e) => e.lessons).find((l) => l.id === lesson)?.title : undefined;
  const featuredCount = shown.filter((e) => e.featured).length;

  return (
    <div>
      <div className="catalog-controls">
        <input
          className="catalog-search"
          type="search"
          placeholder="Search objectives, titles, lessons…"
          aria-label="Search the exercises"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="catalog-filters" role="group" aria-label="Filters">
          <select
            aria-label="Track"
            value={track}
            onChange={(e) => {
              setTrack(e.target.value);
              setCourse("all");
            }}
          >
            <option value="all">All tracks</option>
            {tracks.map((t) => (
              <option key={t.id} value={t.id}>
                {t.title}
                {t.primary ? "" : " (secondary)"}
              </option>
            ))}
            <option value="specialized">Specialized courses</option>
          </select>
          <select aria-label="Course" value={course} onChange={(e) => setCourse(e.target.value)}>
            <option value="all">All courses</option>
            {shownCourses.map((c) => (
              <option key={c.id} value={c.id}>
                {c.title}
              </option>
            ))}
          </select>
          <select aria-label="Difficulty" value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
            <option value="all">All difficulties</option>
            <option value="1">★ Routine</option>
            <option value="2">★★ Standard</option>
            <option value="3">★★★ Hard</option>
          </select>
          <select aria-label="Place" value={kind} onChange={(e) => setKind(e.target.value as typeof kind)}>
            <option value="all">Featured and further</option>
            <option value="featured">Featured (in the text)</option>
            <option value="further">Further exercises</option>
          </select>
          <select aria-label="Endorsements" value={endorsed} onChange={(e) => setEndorsed(e.target.value as typeof endorsed)}>
            <option value="all">Endorsed or not</option>
            <option value="yes">Endorsed</option>
            <option value="no">Not endorsed yet</option>
          </select>
        </div>
      </div>
      {lesson && (
        <p className="catalog-lesson-filter">
          Exercises associated with the lesson <strong>{lessonTitle}</strong>.{" "}
          <button className="link-btn" onClick={() => setLesson(null)}>
            Show all lessons
          </button>
        </p>
      )}
      <p className="catalog-count" aria-live="polite">
        {shown.length} {shown.length === 1 ? "exercise" : "exercises"} ({featuredCount} featured)
      </p>
      {shown.length === 0 ? (
        <p className="catalog-empty">No exercise matches these criteria.</p>
      ) : (
        groups.map((g) => (
          <section key={`${g.course.id}-${g.items[0].id}`} className="exercise-group" style={{ ["--area" as string]: g.course.color }}>
            <h2 className="exercise-group-title">
              <Link href={`/courses/${g.course.id}`}>{g.course.title}</Link>
            </h2>
            <ul className="exercise-list">
              {g.items.map((e) => (
                <li key={e.id} className="exercise-item">
                  <div className="exercise-item-head">
                    <Link href={e.href} className="exercise-item-name">
                      Exercise {e.number}
                      {e.title && <span className="exercise-item-title"> ({e.title})</span>}
                    </Link>
                    {e.difficulty && (
                      <span className="env-difficulty" title={`Difficulty ${e.difficulty}/3`}>
                        {"★".repeat(e.difficulty)}
                      </span>
                    )}
                    {e.featured ? <span className="catalog-tag">Featured</span> : <span className="catalog-tag muted-tag">Further</span>}
                    <EndorseControl exercise={e.id} currentHash={e.hash} state={endorsements} />
                  </div>
                  {e.objectiveHtml ? (
                    <div className="exercise-item-objective" dangerouslySetInnerHTML={{ __html: e.objectiveHtml }} />
                  ) : (
                    <div className="exercise-item-objective muted">No objective stated.</div>
                  )}
                  <div className={`exercise-item-credit small${e.credited ? "" : " muted"}`}>
                    <span className="exercise-item-credit-label">Credit.</span> <span dangerouslySetInnerHTML={{ __html: e.creditHtml }} />
                  </div>
                  <div className="exercise-item-lessons small">
                    {e.lessons.length > 1 ? "Lessons: " : "Lesson: "}
                    {e.lessons.map((l, i) => (
                      <span key={l.id}>
                        {i > 0 && " · "}
                        <Link href={l.href}>{l.title}</Link>
                      </span>
                    ))}
                  </div>
                </li>
              ))}
            </ul>
          </section>
        ))
      )}
      {shown.length > limit && (
        <p style={{ textAlign: "center" }}>
          <button className="btn" onClick={() => setLimit((l) => l + PAGE)}>
            Show more ({shown.length - limit} remaining)
          </button>
        </p>
      )}
    </div>
  );
}
