"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { matchesQuery } from "@/lib/tracks";

export type CatalogEntry = {
  id: string;
  title: string;
  summary: string;
  area: string;
  color: string;
  level: string;
  status: "available" | "draft" | "planned";
  /** Title of the track, or undefined for a specialized course. */
  trackTitle?: string;
  lessons: number;
  minutes: number;
  /** Text searched: titles, summaries, objectives and lesson titles. */
  searchText: string;
};

type Kind = "all" | "track" | "specialized";

/** Searchable, filterable list of all courses. */
export function CourseCatalog({ entries, areas, levels }: { entries: CatalogEntry[]; areas: { id: string; title: string; color: string }[]; levels: string[] }) {
  const [query, setQuery] = useState("");
  const [area, setArea] = useState<string>("all");
  const [kind, setKind] = useState<Kind>("all");
  const [level, setLevel] = useState<string>("all");
  const [hidePlanned, setHidePlanned] = useState(false);

  // Initial filters from the URL, e.g. /courses?kind=specialized or /courses?q=jump
  useEffect(() => {
    const p = new URLSearchParams(window.location.search);
    const q = p.get("q");
    const k = p.get("kind");
    const a = p.get("area");
    if (q) setQuery(q);
    if (k === "track" || k === "specialized") setKind(k);
    if (a && areas.some((x) => x.id === a)) setArea(a);
  }, [areas]);

  const shown = useMemo(
    () =>
      entries.filter(
        (e) =>
          (area === "all" || e.area === area) &&
          (kind === "all" || (kind === "track" ? !!e.trackTitle : !e.trackTitle)) &&
          (level === "all" || e.level === level) &&
          (!hidePlanned || e.status !== "planned") &&
          matchesQuery(e.searchText, query),
      ),
    [entries, area, kind, level, hidePlanned, query],
  );

  return (
    <div>
      <div className="catalog-controls">
        <input
          className="catalog-search"
          type="search"
          placeholder="Search courses, lessons, notions…"
          aria-label="Search the catalogue"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="catalog-filters" role="group" aria-label="Filters">
          <select aria-label="Area" value={area} onChange={(e) => setArea(e.target.value)}>
            <option value="all">All areas</option>
            {areas.map((a) => (
              <option key={a.id} value={a.id}>
                {a.title}
              </option>
            ))}
          </select>
          <select aria-label="Kind of course" value={kind} onChange={(e) => setKind(e.target.value as Kind)}>
            <option value="all">Tracks and specialized</option>
            <option value="track">Main tracks</option>
            <option value="specialized">Specialized</option>
          </select>
          <select aria-label="Level" value={level} onChange={(e) => setLevel(e.target.value)}>
            <option value="all">All levels</option>
            {levels.map((l) => (
              <option key={l} value={l}>
                {l}
              </option>
            ))}
          </select>
          <button className="chip" aria-pressed={hidePlanned} onClick={() => setHidePlanned(!hidePlanned)}>
            Available only
          </button>
        </div>
      </div>
      <p className="catalog-count" aria-live="polite">
        {shown.length} {shown.length === 1 ? "course" : "courses"}
      </p>
      {shown.length === 0 ? (
        <p className="catalog-empty">No course matches these criteria.</p>
      ) : (
        <ul className="catalog-list">
          {shown.map((e) => (
            <li key={e.id} className="catalog-item" style={{ ["--area" as string]: e.color }}>
              <Link href={`/courses/${e.id}`}>
                <span className="catalog-title">{e.title}</span>
                <span className="catalog-meta">
                  <span className="catalog-tag">{e.trackTitle ?? "Specialized"}</span>
                  <br />
                  {e.level}
                  {e.status === "planned" ? (
                    <>
                      {" · "}
                      <span className="status-soon">In preparation</span>
                    </>
                  ) : (
                    <>
                      {" · "}
                      {e.lessons} lessons
                      {e.minutes > 0 && <> · {Math.round(e.minutes / 5) * 5} min</>}
                    </>
                  )}
                </span>
                <span className="catalog-summary">{e.summary}</span>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
