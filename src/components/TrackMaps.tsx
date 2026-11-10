"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { CourseMap, type MapCourse } from "@/components/CourseMap";

export type TrackView = {
  id: string;
  title: string;
  description: string;
  color: string;
  courses: MapCourse[];
  /** Courses of other tracks that this track builds on. */
  external: { id: string; title: string; trackTitle?: string }[];
};

const STORAGE_KEY = "track-map:selected";

/** The dependency graph of one track at a time, with tabs to switch track. */
export function TrackMaps({ tracks, specializedCount }: { tracks: TrackView[]; specializedCount: number }) {
  const [selected, setSelected] = useState(tracks[0]?.id);
  useEffect(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved && tracks.some((t) => t.id === saved)) setSelected(saved);
    } catch {
      // storage unavailable: keep the default
    }
  }, [tracks]);
  const choose = (id: string) => {
    setSelected(id);
    try {
      localStorage.setItem(STORAGE_KEY, id);
    } catch {
      // ignore
    }
  };
  const track = tracks.find((t) => t.id === selected) ?? tracks[0];
  if (!track) return null;

  return (
    <div className="track-maps">
      <div className="track-tabs" role="tablist" aria-label="Learning tracks">
        {tracks.map((t) => (
          <button
            key={t.id}
            role="tab"
            aria-selected={t.id === track.id}
            className="track-tab"
            style={{ ["--area" as string]: t.color }}
            onClick={() => choose(t.id)}
          >
            <span className="track-dot" />
            {t.title}
            <span className="track-count">{t.courses.length}</span>
          </button>
        ))}
      </div>
      <div role="tabpanel" aria-label={track.title}>
        <p className="track-description">{track.description}</p>
        {track.external.length > 0 && (
          <p className="track-external">
            <span>Builds on</span>
            {track.external.map((e) => (
              <Link key={e.id} href={`/courses/${e.id}`} className="mini-course">
                {e.title}
                {e.trackTitle && <span className="track-external-of"> · {e.trackTitle}</span>}
              </Link>
            ))}
          </p>
        )}
        <CourseMap key={track.id} courses={track.courses} areas={[]} />
      </div>
      {specializedCount > 0 && (
        <p className="track-specialized">
          {specializedCount} specialized {specializedCount === 1 ? "course is" : "courses are"} not shown in the graphs.{" "}
          <Link href="/courses?kind=specialized">Browse them in the catalogue</Link>.
        </p>
      )}
    </div>
  );
}
