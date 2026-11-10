import type { Metadata } from "next";
import { getCourse } from "@/lib/content";
import { allVersions } from "@/lib/versions";
import { CoursePage } from "@/components/pages/CoursePage";

// Unknown parameters are rendered on demand and answered with a 404 by the page.

export function generateStaticParams() {
  return allVersions().map((v) => ({ course: v.course, version: v.version }));
}

export async function generateMetadata({ params }: PageProps<"/courses/[course]/v/[version]">): Promise<Metadata> {
  const { course, version } = await params;
  const c = getCourse(course, { course, version });
  return { title: c ? `${c.title} (version ${version})` : "Course" };
}

export default async function Page({ params }: PageProps<"/courses/[course]/v/[version]">) {
  const { course, version } = await params;
  return <CoursePage id={course} version={version} />;
}
