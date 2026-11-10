import Link from "next/link";
import { notFound } from "next/navigation";
import {
  courseHref,
  courseLessons,
  dependents,
  getArea,
  getCatalog,
  getCourse,
  lessonHref,
  nextCourses,
  renderLesson,
  type VersionSel,
} from "@/lib/content";
import { hasVersion, latestVersion, listVersions } from "@/lib/versions";
import type { CitationData } from "@/lib/citation";
import { LessonView } from "@/components/LessonView";
import { ReadProgress, StepDot } from "@/components/progress-ui";
import { SectionNav } from "@/components/SectionNav";
import { CitePanel } from "@/components/CitePanel";

/**
 * A lesson page. Without `version`, shows the working copy (with comments);
 * with `version`, shows the frozen text of that release (read-only).
 */
export async function LessonPage({ courseId, slug, version }: { courseId: string; slug: string; version?: string }) {
  if (version && !hasVersion(courseId, version)) notFound();
  const sel: VersionSel = version ? { course: courseId, version } : undefined;
  const id = `${courseId}/${slug}`;
  const rendered = await renderLesson(id, sel);
  const course = getCourse(courseId, sel);
  if (!rendered || !course) notFound();
  const { meta } = rendered;
  const { lessons } = getCatalog(sel);
  const area = getArea(course.area);

  const ordered = courseLessons(courseId, sel);
  const prev = ordered[meta.index - 1];
  const next = ordered[meta.index + 1];
  const usedIn = version ? [] : dependents(id).filter((l) => l.course !== courseId);
  const after = nextCourses(courseId);
  const href = (lessonId: string) => lessonHref(lessonId, lessonId.startsWith(`${courseId}/`) ? version : undefined);

  const releases = listVersions(courseId);
  const thisRelease = version ? releases.find((r) => r.version === version) : undefined;
  const latest = latestVersion(courseId);
  const existsInCurrent = Boolean(getCatalog().lessons.get(id));

  // What "Cite" points to: this release, or the latest release containing the lesson, or the working copy.
  let citeVersion = thisRelease;
  if (!citeVersion && latest && getCatalog({ course: courseId, version: latest.version }).lessons.has(id)) citeVersion = latest;
  const citation: CitationData = {
    path: lessonHref(id, citeVersion?.version),
    courseId,
    courseTitle: course.title,
    lessonSlug: slug,
    lessonTitle: meta.title,
    lessonNumber: meta.index + 1,
    authors: course.authors,
    version: citeVersion?.version,
    date: citeVersion?.date,
  };

  return (
    <>
      <ReadProgress />
      <div className="lesson-layout">
        <nav className="lesson-toc" aria-label="Course contents" style={{ ["--area" as string]: area?.color }}>
          <Link href={courseHref(courseId, version)} className="toc-course">
            <span className="area-chip" style={{ ["--area" as string]: area?.color }}>
              {area?.title}
            </span>
            <strong>{course.title}</strong>
            <span className="small muted">
              {ordered.length} lessons{version ? ` · version ${version}` : ""}
            </span>
          </Link>
          <ol>
            {ordered.map((l, i) => (
              <li key={l.id} className={l.id === id ? "current" : ""}>
                <Link href={href(l.id)}>
                  <StepDot className="dot" lessonId={l.id} total={l.quizCount} n={i + 1} />
                  {l.title}
                </Link>
                {l.id === id && <SectionNav headings={rendered.headings} />}
              </li>
            ))}
          </ol>
        </nav>

        <div className="lesson-main">
          {thisRelease && (
            <div className="version-banner" role="note">
              <div>
                <strong>Version {thisRelease.version}</strong> of “{course.title}”, released {thisRelease.date}. This text is frozen and
                will not change.
              </div>
              <Link href={existsInCurrent ? lessonHref(id) : courseHref(courseId)}>Current version →</Link>
            </div>
          )}

          <header className="lesson-header">
            <div className="lesson-header-top">
              <nav className="breadcrumb">
                <Link href="/courses">Courses</Link>
                <span>/</span>
                <Link href={courseHref(courseId, version)}>{course.title}</Link>
                {!version && latest && (
                  <>
                    <span>/</span>
                    <span className="muted">working version (last release {latest.version})</span>
                  </>
                )}
              </nav>
              <CitePanel data={citation} />
            </div>
            <div className="lesson-number">
              Lesson {meta.index + 1} <span>of {ordered.length}</span>
            </div>
            <h1>{meta.title}</h1>
            {meta.summary && <p className="lead">{meta.summary}</p>}
            <div className="lesson-facts">
              {meta.duration && <span className="pill">{meta.duration} min</span>}
              {meta.quizCount > 0 && (
                <span className="pill">
                  {meta.quizCount} question{meta.quizCount > 1 ? "s" : ""}
                </span>
              )}
            </div>
            {meta.prerequisites.length > 0 && (
              <div className="prereq-box">
                <strong>Before this lesson:</strong>
                {meta.prerequisites.map((p, i) => (
                  <span key={p}>
                    {i > 0 && " · "}
                    <Link href={href(p)}>{lessons.get(p)?.title ?? p}</Link>
                    {lessons.get(p) && lessons.get(p)!.course !== courseId && (
                      <span className="muted"> ({getCourse(lessons.get(p)!.course)?.title})</span>
                    )}
                  </span>
                ))}
              </div>
            )}
          </header>

          <details className="mobile-outline">
            <summary>
              {course.title} · lesson {meta.index + 1} of {ordered.length}
            </summary>
            <ol>
              {ordered.map((l) => (
                <li key={l.id} className={l.id === id ? "current" : ""}>
                  <Link href={href(l.id)}>{l.title}</Link>
                </li>
              ))}
            </ol>
          </details>

          {process.env.NODE_ENV === "development" && rendered.warnings.length > 0 && (
            <div className="dev-warnings">
              <strong>Content warnings (shown in development only)</strong>
              <ul>
                {rendered.warnings.map((w, i) => (
                  <li key={i}>{w}</li>
                ))}
              </ul>
            </div>
          )}

          <LessonView
            lessonId={id}
            contentHash={rendered.contentHash}
            segments={rendered.segments}
            refPreviews={rendered.refPreviews}
            readOnly={Boolean(version)}
          />

          <footer className="lesson-footer">
            {!next && (
              <div className="course-done">
                <h3>End of “{course.title}”</h3>
                <p>{after.length ? "Courses depending on this one:" : "This is the last lesson of the course."}</p>
                <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
                  {after.map((c) => (
                    <Link key={c.id} className="btn btn-small" href={courseHref(c.id)}>
                      {c.title}
                      {c.status === "planned" ? " (in preparation)" : ""}
                    </Link>
                  ))}
                  <Link className="btn btn-small btn-ghost" href="/#map">
                    Course map
                  </Link>
                </div>
              </div>
            )}
            {usedIn.length > 0 && (
              <div className="leads-to">
                <strong>Used in:</strong>{" "}
                {usedIn.map((l, i) => (
                  <span key={l.id}>
                    {i > 0 && " · "}
                    <Link href={lessonHref(l.id)}>{l.title}</Link>
                  </span>
                ))}
              </div>
            )}
            <div className="prev-next">
              {prev && (
                <Link href={href(prev.id)} className="pn prev">
                  <span className="small muted">← Previous</span>
                  {prev.title}
                </Link>
              )}
              {next && (
                <Link href={href(next.id)} className="pn next">
                  <span className="small muted">Next →</span>
                  {next.title}
                </Link>
              )}
            </div>
          </footer>
        </div>

        {/* The comments panel (client side) is rendered into this column. */}
        <div id="comments-slot" className="comments-slot" />
      </div>
    </>
  );
}
