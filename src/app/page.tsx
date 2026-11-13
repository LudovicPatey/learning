import Link from "next/link";
import { courseStats, getCatalog, renderLesson } from "@/lib/content";
import { trackGraph } from "@/lib/tracks";
import type { MapCourse } from "@/components/CourseMap";
import { TrackMaps, type TrackView } from "@/components/TrackMaps";
import { TuringTape } from "@/components/TuringTape";
import { Quiz } from "@/components/Quiz";
import { renderMathText } from "@/components/math-text";

const SAMPLE_LESSON = "fundamentals/halting-problem";

export default async function Home() {
  const { areas, courses, lessons, tracks } = getCatalog();
  const color = new Map(areas.map((a) => [a.id, a.color]));
  const byId = new Map(courses.map((c) => [c.id, c]));
  const trackTitle = new Map(tracks.map((t) => [t.id, t.title]));

  const trackViews: TrackView[] = tracks.map((t) => {
    const g = trackGraph(t, courses);
    const inTrack = new Set(t.courses);
    const mapCourses: MapCourse[] = t.courses.map((id) => {
      const c = byId.get(id)!;
      const s = courseStats(id);
      return {
        id,
        title: c.title,
        summary: c.summary,
        area: c.area,
        color: color.get(c.area) ?? "#4f46e5",
        status: c.status,
        depth: g.depth.get(id) ?? 0,
        lessons: s.lessons,
        minutes: s.minutes,
        prerequisites: c.prerequisites.filter((p) => inTrack.has(p)),
      };
    });
    return {
      id: t.id,
      title: t.title,
      description: t.description,
      color: color.get(t.area) ?? "#4f46e5",
      courses: mapCourses,
      external: g.external.map((id) => {
        const c = byId.get(id)!;
        return { id, title: c.title, trackTitle: c.track ? trackTitle.get(c.track) : undefined };
      }),
    };
  });
  const specializedCount = courses.filter((c) => !c.track).length;

  const available = courses.filter((c) => c.status === "available");
  const totalQuestions = [...lessons.values()].reduce((s, l) => s + l.quizCount, 0);
  const firstTrack = tracks[0];
  const firstCourse = (firstTrack && byId.get(firstTrack.courses[0])) ?? available[0];

  const sample = await renderLesson(SAMPLE_LESSON);
  const sampleQuiz = sample?.segments.find((s) => s.type === "quiz");

  return (
    <>
      <section className="hero">
        <div className="hero-inner">
          <div>
            <span className="eyebrow">Course notes in mathematical logic</span>
            <h1>Computability Theory</h1>
            <p className="lead">
              Lecture notes for master's students in logic, organized as short courses with explicit prerequisites. They cover
              classical computability theory and its applications to algorithmic randomness, reverse mathematics, higher
              computability and effective forcing, and the model theory of first-order arithmetic.
            </p>
            <div className="hero-ctas">
              {firstCourse && (
                <Link className="btn btn-primary btn-lg" href={`/courses/${firstCourse.id}`}>
                  Begin with {firstCourse.title}
                </Link>
              )}
              <Link className="btn btn-lg" href="/courses">
                All courses
              </Link>
            </div>
            <dl className="hero-stats">
              <div>
                <dt>Courses available</dt>
                <dd>{available.length}</dd>
              </div>
              <div>
                <dt>Lessons</dt>
                <dd>{lessons.size}</dd>
              </div>
              <div>
                <dt>Comprehension questions</dt>
                <dd>{totalQuestions}</dd>
              </div>
            </dl>
          </div>
          <TuringTape />
        </div>
      </section>

      <div className="page">
        <section id="map" className="section" style={{ marginTop: 24 }}>
          <div className="section-head">
            <h2>Learning tracks</h2>
            <p>
              Each track is a main sequence of short courses. Arrows indicate prerequisites within the track; hovering over a course
              highlights the courses it depends on and those depending on it. Courses in preparation have a dashed border. All
              courses, including specialized ones, are listed in the <Link href="/courses">catalogue</Link>.
            </p>
          </div>
          <TrackMaps tracks={trackViews} specializedCount={specializedCount} />
        </section>

        {sampleQuiz && sampleQuiz.type === "quiz" && (
          <section className="section">
            <div className="try-grid">
              <div>
                <div className="section-head">
                  <h2>Example of a comprehension question</h2>
                  <p>
                    From the lesson <Link href={`/courses/${SAMPLE_LESSON}`}>The halting problem</Link>. The question refers to the
                    following proof.
                  </p>
                </div>
                <div
                  className="try-context"
                  dangerouslySetInnerHTML={{
                    __html: renderMathText(
                      "Suppose that $\\emptyset' = \\{e : \\Phi_e(e)\\converge\\}$ is computable. Let $D$ be the algorithm which, on input $x$, decides whether $x \\in \\emptyset'$, enters an infinite loop if so, and halts with output $0$ otherwise; let $d$ be an index of $D$.\n\nThen $\\Phi_d(x)\\converge \\iff \\Phi_x(x)\\diverge$ for every $x$, and taking $x = d$ yields a contradiction.",
                    ),
                  }}
                />
              </div>
              <Quiz quiz={sampleQuiz.quiz} lessonId={SAMPLE_LESSON} defaultOpen />
            </div>
          </section>
        )}

        <section className="section">
          <div className="contrib">
            <div>
              <h2>Contributing</h2>
              <p>
                The notes are maintained collaboratively. To report an error or propose an improvement, select the relevant passage
                in a lesson, choose the type of remark, and sign in with ORCID. Remarks are visible to all readers and are reviewed
                by the maintainers.
              </p>
            </div>
            <ol className="contrib-steps">
              <li>Select a passage or a formula in a lesson.</li>
              <li>Choose the type of remark: typo, unclear argument, mathematical error, suggestion, or question.</li>
              <li>Sign in with ORCID and submit.</li>
            </ol>
          </div>
        </section>
      </div>
    </>
  );
}
