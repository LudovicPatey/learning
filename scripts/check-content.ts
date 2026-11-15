// Validates all lessons: missing files, unknown references, malformed quizzes,
// exercises without label or objective.
// Usage: npm run check-content                     (all lessons)
//        npm run check-content -- --course <id>    (the lessons of one course, and the catalog warnings about it)
//        npm run check-content -- <id>             (print rendered HTML of one lesson)
import { getCatalog, renderLesson } from "../src/lib/content.ts";

const cat = getCatalog();
const args = process.argv.slice(2);
const courseFlag = args.indexOf("--course");
const course = courseFlag >= 0 ? args[courseFlag + 1] : undefined;
const only = courseFlag >= 0 ? undefined : args[0];
if (course && !cat.courses.some((c) => c.id === course)) {
  console.log(`Unknown course "${course}"`);
  process.exit(1);
}
// a warning about the course names one of its lessons ("course/slug"), not a course whose id ends with it
const courseRe = course ? new RegExp(`(^|[\\s"'(])${course.replace(/[-]/g, "\\-")}[/:]`) : null;
const mentions = (w: string) => !courseRe || courseRe.test(w);
let problems = cat.warnings.filter(mentions);
for (const id of cat.lessons.keys()) {
  if (only && id !== only) continue;
  if (course && !id.startsWith(`${course}/`)) continue;
  const r = await renderLesson(id);
  if (!r) continue;
  problems.push(...r.warnings.map((w) => `${id}: ${w}`));
  if (only) {
    for (const s of r.segments) console.log(s.type === "html" ? s.html : JSON.stringify(s.quiz, null, 2));
  }
}
console.log(`${cat.courses.length} courses, ${cat.lessons.size} lessons, ${cat.labels.size} labels, ${cat.exercises.size} exercises`);
if (problems.length) {
  console.log(`\n${problems.length} problem(s)${course ? ` in ${course}` : ""}:`);
  for (const p of problems) console.log("  - " + p);
  process.exit(1);
}
console.log(course ? `Content OK for ${course}` : "Content OK");
