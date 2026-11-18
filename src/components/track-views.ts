// Server-side data of the track graphs (home page and page of all tracks).
import { courseStats, getCatalog } from "@/lib/content";
import { trackGraph, type Track } from "@/lib/tracks";
import type { MapCourse } from "@/components/CourseMap";
import type { TrackView } from "@/components/TrackMaps";

export function trackViews(tracks: Track[]): TrackView[] {
  const { areas, courses, tracks: all, sources } = getCatalog();
  const color = new Map(areas.map((a) => [a.id, a.color]));
  const byId = new Map(courses.map((c) => [c.id, c]));
  const trackTitle = new Map(all.map((t) => [t.id, t.title]));
  return tracks.map((t) => {
    const g = trackGraph(t, courses);
    const inTrack = new Set(t.courses);
    const mapCourses: MapCourse[] = t.courses.map((id) => {
      const c = byId.get(id)!;
      const s = courseStats(id);
      return {
        id,
        title: c.title,
        summary: c.summary,
        area: c.area,
        color: color.get(c.area) ?? "#4f46e5",
        status: c.status,
        depth: g.depth.get(id) ?? 0,
        lessons: s.lessons,
        minutes: s.minutes,
        prerequisites: c.prerequisites.filter((p) => inTrack.has(p)),
      };
    });
    return {
      id: t.id,
      title: t.title,
      description: t.description,
      color: color.get(t.area) ?? "#4f46e5",
      courses: mapCourses,
      credits: t.credits.map((c) => ({ id: c.source, short: sources.get(c.source)?.short ?? c.source, role: c.role })),
      external: g.external.map((id) => {
        const c = byId.get(id)!;
        return { id, title: c.title, trackTitle: c.track ? trackTitle.get(c.track) : undefined };
      }),
    };
  });
}
