import Link from "next/link";
import type { Metadata } from "next";
import { courseStats, getCatalog } from "@/lib/content";

export const metadata: Metadata = { title: "Courses" };

export default function CoursesPage() {
  const { areas, courses } = getCatalog();
  return (
    <div className="page">
      <div className="section-head">
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", margin: "8px 0 12px" }}>All courses</h1>
        <p>
          Courses are grouped by area. The <Link href="/#map">course map</Link> shows their prerequisites.
        </p>
      </div>
      {areas.map((a) => {
        const list = courses.filter((c) => c.area === a.id);
        if (!list.length) return null;
        return (
          <section key={a.id} className="area-block" style={{ ["--area" as string]: a.color }}>
            <h2>{a.title}</h2>
            <p>{a.description}</p>
            <div className="course-grid">
              {list.map((c) => {
                const s = courseStats(c.id);
                return (
                  <Link
                    key={c.id}
                    href={`/courses/${c.id}`}
                    className={`course-card ${c.status === "planned" ? "is-planned" : ""}`}
                    style={{ ["--area" as string]: a.color }}
                  >
                    <h3>{c.title}</h3>
                    <p>{c.summary}</p>
                    <div className="course-card-meta">
                      <span>{c.level}</span>
                      {c.status === "planned" ? (
                        <span className="status-soon">In preparation</span>
                      ) : (
                        <>
                          <span>· {s.lessons} lessons</span>
                          <span>· {s.questions} questions</span>
                        </>
                      )}
                    </div>
                  </Link>
                );
              })}
            </div>
          </section>
        );
      })}
    </div>
  );
}
