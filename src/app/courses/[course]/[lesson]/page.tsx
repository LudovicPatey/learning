import type { Metadata } from "next";
import { getCatalog } from "@/lib/content";
import { LessonPage } from "@/components/pages/LessonPage";

// Unknown parameters are rendered on demand and answered with a 404 by the page.

export function generateStaticParams() {
  return [...getCatalog().lessons.values()].map((l) => ({ course: l.course, lesson: l.slug }));
}

export async function generateMetadata({ params }: PageProps<"/courses/[course]/[lesson]">): Promise<Metadata> {
  const { course, lesson } = await params;
  const l = getCatalog().lessons.get(`${course}/${lesson}`);
  return { title: l?.title ?? "Lesson", description: l?.summary };
}

export default async function Page({ params }: PageProps<"/courses/[course]/[lesson]">) {
  const { course, lesson } = await params;
  return <LessonPage courseId={course} slug={lesson} />;
}
