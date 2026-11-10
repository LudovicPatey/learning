"use client";

import Link from "next/link";
import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";

export type MapCourse = {
  id: string;
  title: string;
  summary: string;
  area: string;
  color: string;
  status: "available" | "draft" | "planned";
  depth: number;
  lessons: number;
  minutes: number;
  prerequisites: string[];
};
export type MapArea = { id: string; title: string; color: string };

type Edge = { from: string; to: string; d: string };

/** Courses laid out in swimlanes (one row per area) and columns (prerequisite depth). */
export function CourseMap({ courses, areas }: { courses: MapCourse[]; areas: MapArea[] }) {
  const boxRef = useRef<HTMLDivElement>(null);
  const cardRefs = useRef(new Map<string, HTMLElement>());
  const [edges, setEdges] = useState<Edge[]>([]);
  const [size, setSize] = useState({ w: 0, h: 0 });
  const [hover, setHover] = useState<string | null>(null);
  const [area, setArea] = useState<string | null>(null);

  const maxDepth = Math.max(0, ...courses.map((c) => c.depth));
  const byId = useMemo(() => new Map(courses.map((c) => [c.id, c])), [courses]);

  // Ancestors and descendants of the hovered course, for highlighting its path.
  const related = useMemo(() => {
    if (!hover) return null;
    const s = new Set<string>([hover]);
    const up = (id: string) => byId.get(id)?.prerequisites.forEach((p) => !s.has(p) && (s.add(p), up(p)));
    const down = (id: string) => courses.forEach((c) => c.prerequisites.includes(id) && !s.has(c.id) && (s.add(c.id), down(c.id)));
    up(hover);
    down(hover);
    return s;
  }, [hover, byId, courses]);

  const layout = useCallback(() => {
    const box = boxRef.current;
    if (!box) return;
    const b = box.getBoundingClientRect();
    const next: Edge[] = [];
    for (const c of courses) {
      const to = cardRefs.current.get(c.id);
      if (!to) continue;
      for (const p of c.prerequisites) {
        const from = cardRefs.current.get(p);
        if (!from) continue;
        const r1 = from.getBoundingClientRect();
        const r2 = to.getBoundingClientRect();
        const x1 = r1.right - b.left;
        const y1 = r1.top + r1.height / 2 - b.top;
        const x2 = r2.left - b.left;
        const y2 = r2.top + r2.height / 2 - b.top;
        const dx = Math.max(24, (x2 - x1) / 2);
        next.push({ from: p, to: c.id, d: `M${x1},${y1} C${x1 + dx},${y1} ${x2 - dx},${y2} ${x2},${y2}` });
      }
    }
    setEdges(next);
    setSize({ w: box.scrollWidth, h: box.scrollHeight });
  }, [courses]);

  useLayoutEffect(layout, [layout]);
  useEffect(() => {
    const ro = new ResizeObserver(layout);
    if (boxRef.current) ro.observe(boxRef.current);
    document.fonts?.ready.then(layout);
    return () => ro.disconnect();
  }, [layout]);

  const colTitle = (d: number) => (d === 0 ? "No prerequisites" : d === 1 ? "Foundations" : d <= 3 ? "Intermediate" : "Advanced");

  return (
    <div>
      {areas.length > 1 && (
      <div className="map-toolbar" role="group" aria-label="Filter by area">
        <button className="chip" aria-pressed={area === null} onClick={() => setArea(null)}>
          All areas
        </button>
        {areas.map((a) => (
          <button key={a.id} className="chip" aria-pressed={area === a.id} onClick={() => setArea(area === a.id ? null : a.id)}>
            <span style={{ width: 8, height: 8, borderRadius: 99, background: a.color }} /> {a.title}
          </button>
        ))}
      </div>
      )}
      <div className="map-scroll">
        <div
          ref={boxRef}
          className="course-map"
          style={{ gridTemplateColumns: `repeat(${maxDepth + 1}, minmax(230px, 1fr))`, gridAutoFlow: "row" }}
        >
          <svg className="map-lines" width={size.w} height={size.h} aria-hidden>
            {edges.map((e) => {
              const hot = related && related.has(e.from) && related.has(e.to);
              const dim = (related && !hot) || (area && byId.get(e.to)?.area !== area);
              return <path key={`${e.from}-${e.to}`} d={e.d} className={`${hot ? "hot" : ""} ${dim ? "dim" : ""}`} />;
            })}
          </svg>
          {Array.from({ length: maxDepth + 1 }, (_, d) => (
            <div key={d} className="map-col" style={{ gridColumn: d + 1, gridRow: 1 }}>
              <div className="map-col-title">{d === 0 || colTitle(d) !== colTitle(d - 1) ? colTitle(d) : " "}</div>
              {courses
                .filter((c) => c.depth === d)
                .map((c) => {
                  const dim = (related && !related.has(c.id)) || (area !== null && c.area !== area);
                  return (
                    <Link
                      key={c.id}
                      href={`/courses/${c.id}`}
                      ref={(el) => {
                        if (el) cardRefs.current.set(c.id, el);
                        else cardRefs.current.delete(c.id);
                      }}
                      className={`course-card ${c.status === "planned" ? "is-planned" : ""} ${dim ? "is-dim" : ""} ${hover === c.id ? "is-hot" : ""}`}
                      style={{ ["--area" as string]: c.color }}
                      onMouseEnter={() => setHover(c.id)}
                      onMouseLeave={() => setHover(null)}
                      onFocus={() => setHover(c.id)}
                      onBlur={() => setHover(null)}
                    >
                      <h3>{c.title}</h3>
                      <p>{c.summary}</p>
                      <div className="course-card-meta">
                        {c.status === "planned" ? (
                          <span className="status-soon">In preparation</span>
                        ) : (
                          <>
                            <span>{c.lessons} lessons</span>
                            {c.minutes > 0 && <span>· {Math.round(c.minutes / 5) * 5} min</span>}
                          </>
                        )}
                      </div>
                    </Link>
                  );
                })}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
