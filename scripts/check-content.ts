// Validates all lessons: missing files, unknown references, malformed quizzes.
// Usage: npm run check-content            (all lessons)
//        npm run check-content -- <id>    (print rendered HTML of one lesson)
import { getCatalog, renderLesson } from "../src/lib/content.ts";

const cat = getCatalog();
let problems = [...cat.warnings];
const only = process.argv[2];
for (const id of cat.lessons.keys()) {
  if (only && id !== only) continue;
  const r = await renderLesson(id);
  if (!r) continue;
  problems.push(...r.warnings.map((w) => `${id}: ${w}`));
  if (only) {
    for (const s of r.segments) console.log(s.type === "html" ? s.html : JSON.stringify(s.quiz, null, 2));
  }
}
console.log(`${cat.courses.length} courses, ${cat.lessons.size} lessons, ${cat.labels.size} labels`);
if (problems.length) {
  console.log(`\n${problems.length} problem(s):`);
  for (const p of problems) console.log("  - " + p);
  process.exit(1);
}
console.log("Content OK");
