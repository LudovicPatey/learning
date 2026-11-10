// Course versions.
//
// The working copy of a course lives in content/<course>/. A *release* freezes
// it: the files are copied, unchanged, to content/_versions/<course>/<version>/
// and the release is recorded in content/_versions/<course>/versions.yaml.
// Released versions are immutable, so that a permalink such as
//   /courses/<course>/v/<version>/<lesson>#<label>
// keeps pointing to the same text forever (for citations).

import fs from "node:fs";
import path from "node:path";
import YAML from "yaml";

export type VersionInfo = { version: string; date: string; notes: string };

export const VERSION_PATTERN = /^\d+\.\d+(\.\d+)?$/;

export function contentDir(): string {
  return process.env.CONTENT_DIR ?? path.join(process.cwd(), "content");
}

export function versionsRoot(root = contentDir()): string {
  return path.join(root, "_versions");
}

export function versionDir(course: string, version: string, root = contentDir()): string {
  return path.join(versionsRoot(root), course, version);
}

/** Compare dotted version numbers numerically: 1.10 > 1.9. */
export function compareVersions(a: string, b: string): number {
  const pa = a.split(".").map(Number);
  const pb = b.split(".").map(Number);
  for (let i = 0; i < Math.max(pa.length, pb.length); i++) {
    const d = (pa[i] ?? 0) - (pb[i] ?? 0);
    if (d !== 0) return d;
  }
  return 0;
}

/** Released versions of a course, most recent first. */
export function listVersions(course: string, root = contentDir()): VersionInfo[] {
  const file = path.join(versionsRoot(root), course, "versions.yaml");
  if (!fs.existsSync(file)) return [];
  const raw = (YAML.parse(fs.readFileSync(file, "utf8")) ?? []) as Partial<VersionInfo>[];
  return raw
    .filter((v) => v && typeof v.version === "string" && VERSION_PATTERN.test(v.version))
    .filter((v) => fs.existsSync(versionDir(course, v.version!, root)))
    .map((v) => ({ version: v.version!, date: String(v.date ?? ""), notes: String(v.notes ?? "") }))
    .sort((a, b) => compareVersions(b.version, a.version));
}

export function latestVersion(course: string, root = contentDir()): VersionInfo | undefined {
  return listVersions(course, root)[0];
}

export function hasVersion(course: string, version: string, root = contentDir()): boolean {
  return listVersions(course, root).some((v) => v.version === version);
}

/** All (course, version) pairs, for static generation. */
export function allVersions(root = contentDir()): { course: string; version: string }[] {
  const base = versionsRoot(root);
  if (!fs.existsSync(base)) return [];
  return fs
    .readdirSync(base, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .flatMap((d) => listVersions(d.name, root).map((v) => ({ course: d.name, version: v.version })));
}
