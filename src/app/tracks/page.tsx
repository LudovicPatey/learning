import Link from "next/link";
import type { Metadata } from "next";
import { getCatalog } from "@/lib/content";
import { TrackMaps } from "@/components/TrackMaps";
import { trackViews } from "@/components/track-views";

export const metadata: Metadata = { title: "All tracks" };

export default function TracksPage() {
  const { courses, tracks } = getCatalog();
  const primary = tracks.filter((t) => t.primary);
  const secondary = tracks.filter((t) => !t.primary);
  const specializedCount = courses.filter((c) => !c.track).length;

  return (
    <div className="page">
      <div className="section-head">
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", margin: "8px 0 12px" }}>All tracks</h1>
        <p>
          A track is a sequence of short courses in one area. The primary tracks are the main sequences of the notes, also shown on
          the <Link href="/">home page</Link>; the secondary tracks are research-oriented continuations built on them. Arrows
          indicate prerequisites within a track. Courses outside every track are listed in the{" "}
          <Link href="/courses?kind=specialized">catalogue</Link>.
        </p>
      </div>

      <section className="section" style={{ marginTop: 24 }}>
        <div className="section-head">
          <h2>Primary tracks</h2>
        </div>
        <TrackMaps tracks={trackViews(primary)} label="Primary tracks" />
      </section>

      {secondary.length > 0 && (
        <section className="section">
          <div className="section-head">
            <h2>Secondary tracks</h2>
            <p>Each of these tracks starts from courses of the primary tracks, listed under “Builds on”.</p>
          </div>
          <TrackMaps tracks={trackViews(secondary)} label="Secondary tracks" storageKey="track-map:secondary" specializedCount={specializedCount} />
        </section>
      )}
    </div>
  );
}
