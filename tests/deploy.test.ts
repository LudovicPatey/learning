import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { BUILD_STAMP, REQUIRED, buildFingerprint, buildIsCurrent, changedFiles, curlConfig, deployFiles, remotePath, sftpBatch, updatedManifest } from "@/lib/deploy";

const dirs: string[] = [];
afterEach(() => {
  for (const d of dirs.splice(0)) fs.rmSync(d, { recursive: true, force: true });
});

/** A minimal out/ directory with the required files and the given extra files. */
function makeOut(extra: Record<string, string> = {}): string {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "cl-out-"));
  dirs.push(dir);
  for (const [rel, text] of Object.entries({ ...Object.fromEntries(REQUIRED.map((r) => [r, `<${r}>`])), ...extra })) {
    fs.mkdirSync(path.dirname(path.join(dir, rel)), { recursive: true });
    fs.writeFileSync(path.join(dir, rel), text);
  }
  return dir;
}

describe("deployFiles", () => {
  it("lists every file of out/, scripts first, and skips .DS_Store", () => {
    const dir = makeOut({ "_next/static/a.js": "a", "courses/x/index.html": "x", ".DS_Store": "", "courses/.DS_Store": "" });
    const files = deployFiles(dir);
    const remotes = files.map((f) => f.remote);
    expect(remotes[0]).toBe("_next/static/a.js");
    expect(remotes).toContain("courses/x/index.html");
    expect(remotes).toContain(".htaccess");
    expect(remotes.some((r) => r.endsWith(".DS_Store"))).toBe(false);
    expect(files.find((f) => f.remote === "courses/x/index.html")).toMatchObject({ size: 1, hash: expect.stringMatching(/^[0-9a-f]{64}$/) });
  });

  it("refuses a config.php and requires the essential files", () => {
    expect(() => deployFiles(makeOut({ "api/config.php": "<?php return [];" }))).toThrow(/refusing to upload api\/config\.php/);
    const dir = makeOut();
    fs.rmSync(path.join(dir, "api", "lessons.json"));
    expect(() => deployFiles(dir)).toThrow(/missing .*lessons\.json/);
  });
});

describe("manifests", () => {
  it("selects the changed files and records the uploaded ones", () => {
    const files = deployFiles(makeOut({ "a.txt": "1", "b.txt": "2" }));
    const all = Object.fromEntries(files.map((f) => [f.remote, f.hash]));
    expect(changedFiles(files, {})).toHaveLength(files.length);
    expect(changedFiles(files, all)).toHaveLength(0);
    const stale = { ...all, "a.txt": "old" };
    expect(changedFiles(files, stale).map((f) => f.remote)).toEqual(["a.txt"]);
    expect(updatedManifest(stale, changedFiles(files, stale))).toEqual(all);
  });
});

describe("upload commands", () => {
  const files = [
    { local: "out/courses/x/index.html", remote: "courses/x/index.html" },
    { local: "out/.htaccess", remote: ".htaccess" },
  ];

  it("joins the remote directory and the path", () => {
    expect(remotePath("/learning/", "a/b")).toBe("learning/a/b");
    expect(remotePath("", "a")).toBe("a");
  });

  it("creates every parent directory before putting files, and never deletes", () => {
    const batch = sftpBatch(files, { dir: "learning" });
    const lines = batch.trim().split("\n");
    expect(lines.slice(0, 3)).toEqual(['-mkdir "learning"', '-mkdir "learning/courses"', '-mkdir "learning/courses/x"']);
    expect(lines.filter((l) => l.startsWith("put "))).toHaveLength(2);
    expect(batch).toContain(`"learning/courses/x/index.html"`);
    expect(batch).not.toMatch(/^(rm|rmdir|rename)\b/m);
  });

  it("puts the password in the curl configuration, with TLS required by default", () => {
    const conf = curlConfig(files, { host: "ftp.example.org", user: "me", password: 'p"w', dir: "learning" });
    expect(conf).toContain('user = "me:p\\"w"');
    expect(conf).toContain("ssl-reqd");
    expect(conf).toContain('url = "ftp://ftp.example.org/learning/courses/x/index.html"');
    expect(curlConfig(files, { host: "h", user: "u", password: "p", dir: "d", tls: false })).not.toContain("ssl-reqd");
  });
});

describe("buildFingerprint and buildIsCurrent", () => {
  function makeRepo(): string {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), "cl-repo-"));
    dirs.push(dir);
    for (const [rel, text] of Object.entries({ "content/a/one.md": "one", "src/x.ts": "x", "package.json": "{}", "tests/t.ts": "t" })) {
      fs.mkdirSync(path.dirname(path.join(dir, rel)), { recursive: true });
      fs.writeFileSync(path.join(dir, rel), text);
    }
    return dir;
  }

  it("changes with the content and the path of an input, not with other files", () => {
    const repo = makeRepo();
    const f0 = buildFingerprint(repo);
    expect(buildFingerprint(repo)).toBe(f0);
    fs.writeFileSync(path.join(repo, "tests/t.ts"), "changed");
    fs.writeFileSync(path.join(repo, "content/.DS_Store"), "");
    expect(buildFingerprint(repo)).toBe(f0);
    fs.writeFileSync(path.join(repo, "content/a/one.md"), "one!");
    const f1 = buildFingerprint(repo);
    expect(f1).not.toBe(f0);
    fs.renameSync(path.join(repo, "content/a/one.md"), path.join(repo, "content/a/two.md"));
    expect(buildFingerprint(repo)).not.toBe(f1);
    fs.writeFileSync(path.join(repo, ".env.local"), "NEXT_PUBLIC_X=1");
    expect(buildFingerprint(repo)).not.toBe(f1);
  });

  it("accepts out/ only when it is complete and stamped with the same fingerprint", () => {
    const out = makeOut();
    expect(buildIsCurrent(out, "abc")).toBe(false);
    fs.writeFileSync(path.join(out, BUILD_STAMP), "abc\n");
    expect(buildIsCurrent(out, "abc")).toBe(true);
    expect(buildIsCurrent(out, "abd")).toBe(false);
    fs.rmSync(path.join(out, "api", "exercises.json"));
    expect(buildIsCurrent(out, "abc")).toBe(false);
  });

  it("does not upload the stamp", () => {
    const out = makeOut({ [BUILD_STAMP]: "abc" });
    expect(deployFiles(out).map((f) => f.remote)).not.toContain(BUILD_STAMP);
  });
});
