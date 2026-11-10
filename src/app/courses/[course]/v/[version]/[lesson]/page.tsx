import type { Metadata } from "next";
import { getCatalog } from "@/lib/content";
import { allVersions } from "@/lib/versions";
import { LessonPage } from "@/components/pages/LessonPage";

export const dynamicParams = false;

export function generateStaticParams() {
  return allVersions().flatMap(({ course, version }) =>
    [...getCatalog({ course, version }).lessons.values()]
      .filter((l) => l.course === course)
      .map((l) => ({ course, version, lesson: l.slug })),
  );
}

export async function generateMetadata({ params }: PageProps<"/courses/[course]/v/[version]/[lesson]">): Promise<Metadata> {
  const { course, version, lesson } = await params;
  const l = getCatalog({ course, version }).lessons.get(`${course}/${lesson}`);
  return { title: l ? `${l.title} (version ${version})` : "Lesson", description: l?.summary };
}

export default async function Page({ params }: PageProps<"/courses/[course]/v/[version]/[lesson]">) {
  const { course, version, lesson } = await params;
  return <LessonPage courseId={course} slug={lesson} version={version} />;
}
