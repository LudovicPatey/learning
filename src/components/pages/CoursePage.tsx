import Link from "next/link";
import { notFound } from "next/navigation";
import { courseHref, courseLessons, courseStats, getArea, getCourse, getTrack, lessonHref, nextCourses, type VersionSel } from "@/lib/content";
import { hasVersion, listVersions } from "@/lib/versions";
import { CourseProgressCard, StepDot } from "@/components/progress-ui";
import { renderMathText } from "@/components/math-text";

function MiniCourse({ id }: { id: string }) {
  const c = getCourse(id);
  if (!c) return null;
  const area = getArea(c.area);
  return (
    <Link href={`/courses/${c.id}`} className="mini-course" style={{ ["--area" as string]: area?.color }}>
      {c.title}
      {c.status === "planned" && <span className="status-soon">Soon</span>}
    </Link>
  );
}

/** A course page: the working copy, or a released version when `version` is given. */
export async function CoursePage({ id, version }: { id: string; version?: string }) {
  if (version && !hasVersion(id, version)) notFound();
  const sel: VersionSel = version ? { course: id, version } : undefined;
  const course = getCourse(id, sel);
  if (!course) notFound();
  const area = getArea(course.area);
  const lessons = courseLessons(id, sel);
  const stats = courseStats(id, sel);
  const after = nextCourses(id);
  const releases = listVersions(id);
  const thisRelease = version ? releases.find((r) => r.version === version) : undefined;

  return (
    <>
      {thisRelease && (
        <div className="version-banner page-banner" role="note">
          <div>
            <strong>Version {thisRelease.version}</strong> of “{course.title}”, released {thisRelease.date}. This text is frozen.
          </div>
          <Link href={courseHref(id)}>Working version →</Link>
        </div>
      )}
      <section className="course-hero" style={{ ["--area" as string]: area?.color }}>
        <div className="course-hero-inner">
          <div>
            <nav className="breadcrumb">
              <Link href="/courses">Courses</Link>
              <span>/</span>
              <span className="area-chip">{area?.title}</span>
              <span>/</span>
              <span>{getTrack(getCourse(id)?.track)?.title ?? "Specialized course"}</span>
            </nav>
            <h1>{course.title}</h1>
            <p className="lead">{course.summary}</p>
            <div className="course-pills">
              <span className="pill">{course.level}</span>
              {course.status !== "planned" && (
                <>
                  <span className="pill">{stats.lessons} lessons</span>
                  {stats.minutes > 0 && <span className="pill">≈ {Math.round(stats.minutes / 5) * 5} min</span>}
                  <span className="pill">{stats.questions} questions</span>
                </>
              )}
              {course.status === "planned" && <span className="pill">In preparation</span>}
            </div>
          </div>
          {lessons.length > 0 && (
            <CourseProgressCard lessons={lessons.map((l) => ({ id: l.id, title: l.title, href: lessonHref(l.id, version), quizCount: l.quizCount }))} />
          )}
        </div>
      </section>

      <div className="course-body">
        <div>
          {course.description && <p className="course-description">{course.description}</p>}
          <h2>Contents</h2>
          {lessons.length === 0 ? (
            <div className="planned-box">
              This course is in preparation.
            </div>
          ) : (
            <ol className="timeline">
              {lessons.map((l, i) => (
                <li key={l.id}>
                  <Link href={lessonHref(l.id, version)}>
                    <StepDot lessonId={l.id} total={l.quizCount} n={i + 1} />
                    <div>
                      <h3>{l.title}</h3>
                      <p>{l.summary}</p>
                      {l.sections.length > 0 && (
                        <ol className="toc-mini">
                          {l.sections.map((sec, j) => (
                            <li key={j}>
                              <span className="sec-num">
                                {i + 1}.{j + 1}
                              </span>{" "}
                              <span dangerouslySetInnerHTML={{ __html: renderMathText(sec) }} />
                            </li>
                          ))}
                        </ol>
                      )}
                    </div>
                    <span className="step-meta">{l.duration ? `${l.duration} min` : ""}</span>
                  </Link>
                </li>
              ))}
            </ol>
          )}
        </div>

        <aside>
          {course.objectives.length > 0 && (
            <div className="side-card">
              <h2>Learning objectives</h2>
              <ul className="objectives">
                {course.objectives.map((o) => (
                  <li key={o}>{o}</li>
                ))}
              </ul>
            </div>
          )}
          <div className="side-card">
            <h2>Prerequisites</h2>
            {course.prerequisites.length ? (
              course.prerequisites.map((p) => <MiniCourse key={p} id={p} />)
            ) : (
              <p className="muted" style={{ margin: 0 }}>
                None.
              </p>
            )}
          </div>
          <div className="side-card">
            <h2>Versions</h2>
            <ul className="version-list">
              <li className={!version ? "current" : ""}>
                <Link href={courseHref(id)}>Working version</Link>
                <span className="small muted">latest text, may change</span>
              </li>
              {releases.map((r) => (
                <li key={r.version} className={version === r.version ? "current" : ""}>
                  <Link href={courseHref(id, r.version)}>Version {r.version}</Link>
                  <span className="small muted">
                    {r.date}
                    {r.notes ? ` — ${r.notes}` : ""}
                  </span>
                </li>
              ))}
            </ul>
            {releases.length === 0 && <p className="small muted">No released version yet.</p>}
          </div>
          {after.length > 0 && (
            <div className="side-card">
              <h2>Followed by</h2>
              {after.map((c) => (
                <MiniCourse key={c.id} id={c.id} />
              ))}
            </div>
          )}
        </aside>
      </div>
    </>
  );
}
