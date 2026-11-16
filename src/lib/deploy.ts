// What scripts/deploy.ts uploads to the live site, and how (docs/DEPLOY.md).
// Pure functions (apart from reading out/), tested in tests/deploy.test.ts.
//
// Everything comes from out/, built by scripts/build-static.ts, never from the
// rest of the repository (external-data/ holds copyrighted sources). The server's
// own api/config.php is never uploaded, and nothing is ever deleted on the server.
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

export type DeployFile = { local: string; remote: string; hash: string; size: number };

/** Files that must be in out/ for a deployment to make sense. */
export const REQUIRED = ["index.html", "404.html", ".htaccess", "api/index.php", "api/lib.php", "api/.htaccess", "api/lessons.json", "api/exercises.json"];
/** Fingerprint of the inputs of the last successful build, written by scripts/build-static.ts. */
export const BUILD_STAMP = ".build-inputs";
const SKIPPED = new Set([".DS_Store", BUILD_STAMP]);

/** Every file of out/, with its path on the server (relative to the site's folder). */
export function deployFiles(outDir = "out"): DeployFile[] {
  const files: DeployFile[] = [];
  const walk = (rel: string) => {
    for (const e of fs.readdirSync(path.join(outDir, rel), { withFileTypes: true })) {
      const r = rel ? `${rel}/${e.name}` : e.name;
      if (e.isDirectory()) walk(r);
      else if (!SKIPPED.has(e.name)) {
        if (/(^|\/)config\.php$/.test(r)) throw new Error(`refusing to upload ${r}`);
        const local = path.join(outDir, r);
        const data = fs.readFileSync(local);
        files.push({ local, remote: r, hash: crypto.createHash("sha256").update(data).digest("hex"), size: data.length });
      }
    }
  };
  for (const r of REQUIRED) if (!fs.existsSync(path.join(outDir, r))) throw new Error(`missing ${path.join(outDir, r)} (run npm run build:static)`);
  walk("");
  // Scripts and styles first, so that no uploaded page refers to a missing file.
  return files.sort((a, b) => Number(!a.remote.startsWith("_next/")) - Number(!b.remote.startsWith("_next/")) || a.remote.localeCompare(b.remote));
}

/** Manifest of a deployment: remote path → content hash of the uploaded file. */
export type Manifest = Record<string, string>;

/** The files whose content differs from what the manifest records as online. */
export function changedFiles(files: DeployFile[], manifest: Manifest): DeployFile[] {
  return files.filter((f) => manifest[f.remote] !== f.hash);
}

/** The manifest after a successful upload of `uploaded`. */
export function updatedManifest(manifest: Manifest, uploaded: DeployFile[]): Manifest {
  const m = { ...manifest };
  for (const f of uploaded) m[f.remote] = f.hash;
  return m;
}

const q = (s: string) => `"${String(s).replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
export const remotePath = (dir: string, remote: string) => [dir.replace(/^\/+|\/+$/g, ""), remote].filter(Boolean).join("/");

/**
 * Commands for OpenSSH sftp: creates the directories, parents first (a leading "-"
 * ignores "already exists"), then puts each file. No rm, no rename.
 */
export function sftpBatch(files: { local: string; remote: string }[], { dir }: { dir: string }): string {
  const dirs = new Set<string>();
  for (const f of files) {
    const parts = remotePath(dir, f.remote).split("/").slice(0, -1);
    for (let i = 1; i <= parts.length; i++) dirs.add(parts.slice(0, i).join("/"));
  }
  const sorted = [...dirs].sort((a, b) => a.split("/").length - b.split("/").length || a.localeCompare(b));
  const lines = sorted.map((d) => `-mkdir ${q(d)}`);
  for (const f of files) lines.push(`put ${q(path.resolve(f.local))} ${q(remotePath(dir, f.remote))}`);
  return lines.join("\n") + "\n";
}

/**
 * curl configuration (read from stdin with `curl -K -`, so that the password is not
 * on the command line) uploading every file over FTP, with TLS required unless
 * `tls` is false; curl creates missing directories and never deletes.
 */
export function curlConfig(
  files: { local: string; remote: string }[],
  { host, user, password, dir, tls = true }: { host: string; user: string; password: string; dir: string; tls?: boolean },
): string {
  const lines = [`user = ${q(`${user}:${password}`)}`, "ftp-create-dirs", "fail", "silent", "show-error"];
  if (tls) lines.push("ssl-reqd");
  for (const f of files) {
    lines.push(`upload-file = ${q(path.resolve(f.local))}`);
    lines.push(`url = ${q(`ftp://${host}/${encodeURI(remotePath(dir, f.remote))}`)}`);
  }
  return lines.join("\n") + "\n";
}

/**
 * What the static build depends on (relative to the repository): the lessons and
 * released versions, the site's code and styles, the PHP API, the build script, the
 * dependencies and the configuration. Tests and docs are not inputs.
 */
export const BUILD_INPUTS = [
  "content",
  "src",
  "public",
  "deploy",
  "scripts/build-static.ts",
  "next.config.ts",
  "package.json",
  "package-lock.json",
  "tsconfig.json",
  ".env",
  ".env.local",
  ".env.production",
  ".env.production.local",
];

/**
 * A hash of every file of `inputs` under `root` (paths and contents), and of the
 * Node version: equal fingerprints mean that the build would produce the same out/.
 * Missing inputs are skipped.
 */
export function buildFingerprint(root: string, inputs: string[] = BUILD_INPUTS): string {
  const h = crypto.createHash("sha256").update(`node ${process.version}\n`);
  const add = (rel: string) => {
    const abs = path.join(root, rel);
    let st: fs.Stats;
    try {
      st = fs.statSync(abs);
    } catch {
      return;
    }
    if (st.isDirectory()) {
      for (const name of fs.readdirSync(abs).sort()) if (!SKIPPED.has(name)) add(`${rel}/${name}`);
    } else {
      h.update(`${rel}\0${crypto.createHash("sha256").update(fs.readFileSync(abs)).digest("hex")}\n`);
    }
  };
  for (const r of inputs) add(r);
  return h.digest("hex");
}

/**
 * Whether out/ is a complete build of the current inputs: it has every required file
 * and the fingerprint recorded by its build equals `fingerprint`.
 */
export function buildIsCurrent(outDir: string, fingerprint: string): boolean {
  if (REQUIRED.some((r) => !fs.existsSync(path.join(outDir, r)))) return false;
  try {
    return fs.readFileSync(path.join(outDir, BUILD_STAMP), "utf8").trim() === fingerprint;
  } catch {
    return false;
  }
}
