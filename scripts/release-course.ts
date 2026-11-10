// Freeze the working copy of a course as a new immutable version.
// Usage: npm run release -- <course> <version> "<release notes>"
//   e.g. npm run release -- models-of-computation 1.0 "First complete version"
import { releaseCourse, ReleaseError } from "../src/lib/release.ts";

const [course, version, ...notes] = process.argv.slice(2);
if (!course || !version) {
  console.error('Usage: npm run release -- <course> <version> "<release notes>"');
  process.exit(1);
}
try {
  const info = releaseCourse({ course, version, notes: notes.join(" ") });
  console.log(`Released ${course} ${info.version} (${info.date}).`);
  console.log(`Permanent URLs: /courses/${course}/v/${info.version}/<lesson>`);
} catch (e) {
  if (e instanceof ReleaseError) {
    console.error(`Release refused: ${e.message}`);
    process.exit(1);
  }
  throw e;
}
