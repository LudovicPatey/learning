// Creating releases (command line only: never imported by the web application,
// so that its filesystem writes are not bundled into the server).
import fs from "node:fs";
import path from "node:path";
import YAML from "yaml";
import { VERSION_PATTERN, compareVersions, contentDir, listVersions, versionDir, versionsRoot, type VersionInfo } from "./versions.ts";

export class ReleaseError extends Error {}

/**
 * Freeze the working copy of a course as a new version.
 * Throws a ReleaseError if the version is malformed, already exists, or is not
 * greater than the latest release.
 */
export function releaseCourse(opts: { course: string; version: string; notes?: string; date?: string; root?: string }): VersionInfo {
  const root = opts.root ?? contentDir();
  const { course, version } = opts;
  const src = path.join(root, course);
  if (!fs.existsSync(path.join(src, "_course.yaml"))) throw new ReleaseError(`Unknown course "${course}"`);
  if (!VERSION_PATTERN.test(version)) throw new ReleaseError(`Version must look like 1.0 or 1.0.2, got "${version}"`);
  const existing = listVersions(course, root);
  if (existing.some((v) => v.version === version)) throw new ReleaseError(`Version ${version} of ${course} already exists`);
  const latest = existing[0];
  if (latest && compareVersions(version, latest.version) <= 0) {
    throw new ReleaseError(`Version ${version} must be greater than the latest release ${latest.version}`);
  }
  const dest = versionDir(course, version, root);
  if (fs.existsSync(dest)) throw new ReleaseError(`Directory ${dest} already exists`);

  fs.mkdirSync(dest, { recursive: true });
  for (const f of fs.readdirSync(src)) {
    if (f === "_course.yaml" || f.endsWith(".md")) fs.copyFileSync(path.join(src, f), path.join(dest, f));
  }
  const info: VersionInfo = {
    version,
    date: opts.date ?? new Date().toISOString().slice(0, 10),
    notes: opts.notes ?? "",
  };
  const file = path.join(versionsRoot(root), course, "versions.yaml");
  const list = fs.existsSync(file) ? ((YAML.parse(fs.readFileSync(file, "utf8")) ?? []) as VersionInfo[]) : [];
  list.push(info);
  fs.writeFileSync(file, YAML.stringify(list));
  return info;
}
