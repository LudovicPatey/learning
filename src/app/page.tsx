import Link from "next/link";
import { courseDepths, courseStats, getCatalog, renderLesson } from "@/lib/content";
import { CourseMap, type MapCourse } from "@/components/CourseMap";
import { TuringTape } from "@/components/TuringTape";
import { Quiz } from "@/components/Quiz";
import { renderMathText } from "@/components/math-text";

const SAMPLE_LESSON = "fundamentals/halting-problem";

export default async function Home() {
  const { areas, courses, lessons } = getCatalog();
  const depth = courseDepths();
  const color = new Map(areas.map((a) => [a.id, a.color]));

  const mapCourses: MapCourse[] = courses.map((c) => {
    const s = courseStats(c.id);
    return {
      id: c.id,
      title: c.title,
      summary: c.summary,
      area: c.area,
      color: color.get(c.area) ?? "#4f46e5",
      status: c.status,
      depth: depth.get(c.id) ?? 0,
      lessons: s.lessons,
      minutes: s.minutes,
      prerequisites: c.prerequisites,
    };
  });

  const available = courses.filter((c) => c.status === "available");
  const totalQuestions = [...lessons.values()].reduce((s, l) => s + l.quizCount, 0);
  const firstCourse = available.find((c) => (depth.get(c.id) ?? 0) === 0) ?? available[0];

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
              classical computability theory and its applications to algorithmic randomness, reverse mathematics and higher
              computability.
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
            <h2>Courses and prerequisites</h2>
            <p>
              Each course consists of a few lessons on a single topic. Arrows indicate prerequisites; hovering over a course highlights
              the courses it depends on and those depending on it. Courses in preparation have a dashed border.
            </p>
          </div>
          <CourseMap courses={mapCourses} areas={areas.map((a) => ({ id: a.id, title: a.title, color: a.color }))} />
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
