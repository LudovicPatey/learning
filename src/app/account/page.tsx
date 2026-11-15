import type { Metadata } from "next";
import { getCatalog, lessonHref } from "@/lib/content";
import { AccountView, type AccountRefs } from "@/components/AccountView";

export const metadata: Metadata = { title: "My remarks and endorsements" };

// A static page: the remarks and endorsements are loaded in the browser from
// /api/me/activity; the titles of lessons and exercises are written in the page.
export default function AccountPage() {
  const { courses, lessons, exercises } = getCatalog();
  const courseTitle = new Map(courses.map((c) => [c.id, c.title]));
  const refs: AccountRefs = {
    lessons: Object.fromEntries(
      [...lessons.values()].map((l) => [l.id, { title: l.title, course: courseTitle.get(l.course) ?? l.course, href: lessonHref(l.id) }]),
    ),
    exercises: Object.fromEntries(
      [...exercises.values()].map((e) => [e.id, { number: e.number, title: e.title, lesson: e.lessonId, hash: e.hash }]),
    ),
  };
  return (
    <div className="page account-page">
      <div className="section-head">
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", margin: "8px 0 12px" }}>My remarks and endorsements</h1>
        <p>The remarks you have written on the lessons, with their replies, and the exercises you have endorsed.</p>
      </div>
      <AccountView refs={refs} />
    </div>
  );
}
