// Builds the site deployed to the PHP web hosting (docs/DEPLOY.md) into out/:
//   1. the static export of the Next.js site (STATIC_EXPORT=1, see next.config.ts);
//   2. the remarks server (deploy/api/*.php), which serves the URLs of src/app/api/;
//   3. api/lessons.json, the lessons that accept remarks, with the hash of their source;
//   4. the root .htaccess (deploy/htaccess.txt).
// Usage: npm run build:static
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { getCatalog, renderLesson } from "../src/lib/content.ts";
import { allVersions } from "../src/lib/versions.ts";

const root = path.resolve(import.meta.dirname, "..");
const out = path.join(root, "out");

fs.rmSync(out, { recursive: true, force: true });
const r = spawnSync("npx", ["next", "build"], { cwd: root, stdio: "inherit", env: { ...process.env, STATIC_EXPORT: "1" } });
if (r.status !== 0) process.exit(r.status ?? 1);

// The placeholder page of the version routes, when no version is released yet.
if (allVersions().length === 0) fs.rmSync(path.join(out, "courses", "none"), { recursive: true, force: true });

// Remarks are accepted on the working copy only; the hash marks remarks made on an older text.
const lessons: Record<string, string> = {};
for (const id of [...getCatalog().lessons.keys()].sort()) {
  const rendered = await renderLesson(id);
  if (rendered) lessons[id] = rendered.contentHash;
}
fs.mkdirSync(path.join(out, "api"), { recursive: true });
fs.writeFileSync(path.join(out, "api", "lessons.json"), JSON.stringify(lessons, null, 1) + "\n");

for (const f of ["index.php", "lib.php", ".htaccess", "config.example.php"]) {
  fs.copyFileSync(path.join(root, "deploy", "api", f), path.join(out, "api", f));
}
fs.copyFileSync(path.join(root, "deploy", "htaccess.txt"), path.join(out, ".htaccess"));

console.log(`\nStatic site in out/: ${Object.keys(lessons).length} lessons accept remarks.`);
