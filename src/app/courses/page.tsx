import Link from "next/link";
import type { Metadata } from "next";
import { courseLessons, courseStats, getCatalog } from "@/lib/content";
import { CourseCatalog, type CatalogEntry } from "@/components/CourseCatalog";

export const metadata: Metadata = { title: "Course catalogue" };

const LEVELS = ["Introductory", "Intermediate", "Advanced"];

export default function CoursesPage() {
  const { areas, courses, tracks } = getCatalog();
  const areaById = new Map(areas.map((a) => [a.id, a]));
  const trackById = new Map(tracks.map((t) => [t.id, t]));
  const trackRank = new Map(tracks.flatMap((t, i) => t.courses.map((c, j) => [c, i * 1000 + j] as const)));

  // Courses of the tracks first, in track order, then specialized courses by area and order.
  const sorted = [...courses].sort((a, b) => {
    const ra = trackRank.get(a.id) ?? 1e6;
    const rb = trackRank.get(b.id) ?? 1e6;
    if (ra !== rb) return ra - rb;
    return a.area.localeCompare(b.area) || a.order - b.order || a.title.localeCompare(b.title);
  });

  const entries: CatalogEntry[] = sorted.map((c) => {
    const s = courseStats(c.id);
    const area = areaById.get(c.area);
    const track = c.track ? trackById.get(c.track) : undefined;
    const lessonText = courseLessons(c.id)
      .map((l) => `${l.title} ${l.summary}`)
      .join(" ");
    return {
      id: c.id,
      title: c.title,
      summary: c.summary,
      area: c.area,
      color: area?.color ?? "#4f46e5",
      level: c.level,
      status: c.status,
      trackTitle: track?.title,
      lessons: s.lessons,
      minutes: s.minutes,
      searchText: [c.title, c.summary, c.description, area?.title ?? "", track?.title ?? "", ...c.objectives, lessonText].join(" "),
    };
  });
  const levels = LEVELS.filter((l) => courses.some((c) => c.level === l)).concat(
    [...new Set(courses.map((c) => c.level))].filter((l) => !LEVELS.includes(l)),
  );

  return (
    <div className="page">
      <div className="section-head">
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", margin: "8px 0 12px" }}>Course catalogue</h1>
        <p>
          All courses, including the specialized courses that do not belong to a main track. The search covers titles, summaries,
          objectives and lesson titles. The <Link href="/#map">learning tracks</Link> show the main sequences and their prerequisites.
        </p>
      </div>
      <CourseCatalog entries={entries} areas={areas.map((a) => ({ id: a.id, title: a.title, color: a.color }))} levels={levels} />
    </div>
  );
}
