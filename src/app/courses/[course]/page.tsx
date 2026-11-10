import type { Metadata } from "next";
import { getCatalog, getCourse } from "@/lib/content";
import { CoursePage } from "@/components/pages/CoursePage";

export function generateStaticParams() {
  return getCatalog().courses.map((c) => ({ course: c.id }));
}

export async function generateMetadata({ params }: PageProps<"/courses/[course]">): Promise<Metadata> {
  const c = getCourse((await params).course);
  return { title: c?.title ?? "Course", description: c?.summary };
}

export default async function Page({ params }: PageProps<"/courses/[course]">) {
  const { course } = await params;
  return <CoursePage id={course} />;
}
