import Link from "next/link";
import type { Metadata } from "next";
import { getCatalog, lessonHref, renderInlineMarkdown } from "@/lib/content";
import { ExerciseCatalog, type ExerciseEntry } from "@/components/ExerciseCatalog";

export const metadata: Metadata = { title: "Exercise catalogue" };

export default async function ExercisesPage() {
  const { areas, courses, lessons, tracks, exercises } = getCatalog();
  const color = new Map(areas.map((a) => [a.id, a.color]));

  const entries: ExerciseEntry[] = [];
  for (const ex of exercises.values()) {
    entries.push({
      id: ex.id,
      number: ex.number,
      title: ex.title,
      objectiveHtml: ex.objective ? await renderInlineMarkdown(ex.objective) : "",
      objectiveText: ex.objective,
      difficulty: ex.difficulty,
      featured: ex.featured,
      hash: ex.hash,
      creditHtml: await renderInlineMarkdown(ex.creditText),
      credited: Boolean(ex.credit),
      course: ex.course,
      href: `${lessonHref(ex.lessonId)}#${ex.id}`,
      lessons: ex.lessons.map((id) => ({ id, title: lessons.get(id)?.title ?? id, href: lessonHref(id) })),
    });
  }
  const courseList = courses
    .filter((c) => entries.some((e) => e.course === c.id))
    .map((c) => ({ id: c.id, title: c.title, color: color.get(c.area) ?? "#4f46e5", track: c.track }));
  const trackList = tracks.map((t) => ({ id: t.id, title: t.title, primary: t.primary }));

  return (
    <div className="page">
      <div className="section-head">
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", margin: "8px 0 12px" }}>Exercise catalogue</h1>
        <p>
          All exercises of the courses, with their objective and the lessons they are associated with. Featured exercises appear in
          the text of their lesson; the others are collected at the end of the lesson, under “Further exercises”. Every exercise has
          a solution and a credit: the published work it comes from, or “Written for this course” (see the{" "}
          <Link href="/credits">credits</Link>). Readers signed in with ORCID can endorse an exercise once they have checked it and its solution; the{" "}
          <Link href="/account">account page</Link> lists one&apos;s endorsements and remarks.
        </p>
      </div>
      <ExerciseCatalog entries={entries} courses={courseList} tracks={trackList} />
    </div>
  );
}
