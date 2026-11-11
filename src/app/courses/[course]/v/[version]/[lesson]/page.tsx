import type { Metadata } from "next";
import { getCatalog } from "@/lib/content";
import { allVersions, withExportPlaceholder } from "@/lib/versions";
import { LessonPage } from "@/components/pages/LessonPage";

// Unknown parameters are rendered on demand and answered with a 404 by the page.

export function generateStaticParams() {
  return withExportPlaceholder(
    allVersions().flatMap(({ course, version }) =>
      [...getCatalog({ course, version }).lessons.values()]
        .filter((l) => l.course === course)
        .map((l) => ({ course, version, lesson: l.slug })),
    ),
    { course: "none", version: "none", lesson: "none" },
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
