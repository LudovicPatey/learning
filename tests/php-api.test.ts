// The PHP remarks server of the live site (deploy/api/), run with `php -S`. It must
// answer the same URLs with the same JSON as the Next.js API (src/app/api/), whose
// client code is shared. Skipped when PHP is not installed.
import { spawn, spawnSync, type ChildProcess } from "node:child_process";
import fs from "node:fs";
import net from "node:net";
import os from "node:os";
import path from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

const hasPhp = spawnSync("php", ["-v"]).status === 0;
const ADMIN = "0000-0002-1825-0097"; // the dev login account (ORCID's fictitious researcher)
const OTHER = "0000-0000-0000-0001";
const TOKEN = "test-admin-token";

let server: ChildProcess;
let base = "";
let tmp = "";
let cookie = "";

async function freePort(): Promise<number> {
  return new Promise((resolve) => {
    const s = net.createServer();
    s.listen(0, "127.0.0.1", () => {
      const port = (s.address() as net.AddressInfo).port;
      s.close(() => resolve(port));
    });
  });
}

async function call(method: string, url: string, body?: unknown, headers: Record<string, string> = {}) {
  const res = await fetch(base + url, {
    method,
    redirect: "manual",
    headers: { ...(cookie ? { cookie } : {}), ...(body !== undefined ? { "content-type": "application/json" } : {}), ...headers },
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });
  const set = res.headers.get("set-cookie");
  if (set) {
    const m = /cl_session=([^;]*)/.exec(set);
    if (m) cookie = m[1] === "deleted" || m[1] === "" ? "" : `cl_session=${m[1]}`;
  }
  const text = await res.text();
  let json: any = null;
  try {
    json = JSON.parse(text);
  } catch {}
  return { status: res.status, json, location: res.headers.get("location") };
}

describe.skipIf(!hasPhp)("PHP remarks server", () => {
  beforeAll(async () => {
    tmp = fs.mkdtempSync(path.join(os.tmpdir(), "cl-php-"));
    fs.writeFileSync(path.join(tmp, "lessons.json"), JSON.stringify({ "c/l": "hash1", "c/m": "hash2" }));
    fs.writeFileSync(
      path.join(tmp, "config.php"),
      `<?php return ['data_dir' => ${JSON.stringify(path.join(tmp, "data"))}, 'lessons_json' => ${JSON.stringify(path.join(tmp, "lessons.json"))},
        'dev_login' => true, 'admin_orcids' => ['${ADMIN}'], 'admin_token' => '${TOKEN}'];`,
    );
    const port = await freePort();
    base = `http://127.0.0.1:${port}`;
    server = spawn("php", ["-S", `127.0.0.1:${port}`, path.join(__dirname, "fixtures", "php-router.php")], {
      env: { ...process.env, LEARNING_CONFIG: path.join(tmp, "config.php") },
      stdio: "ignore",
    });
    for (let i = 0; i < 50; i++) {
      try {
        await fetch(`${base}/api/auth/me`);
        return;
      } catch {
        await new Promise((r) => setTimeout(r, 100));
      }
    }
    throw new Error("php -S did not start");
  });

  afterAll(() => {
    server?.kill();
    fs.rmSync(tmp, { recursive: true, force: true });
  });

  const anchor = { exact: "passage", prefix: "a ", suffix: " b", position: 12.9, display: "passage" };

  it("answers anonymous requests", async () => {
    const me = await call("GET", "/api/auth/me");
    expect(me.json).toEqual({ user: null, orcidConfigured: false, devLogin: true });
    expect((await call("GET", "/api/comments?lesson=c/l")).json).toEqual({ threads: [], me: null });
    expect((await call("GET", "/api/comments?lesson=nope")).status).toBe(404);
    expect((await call("POST", "/api/comments", { lessonId: "c/l", body: "x", anchor })).status).toBe(401);
    expect((await call("GET", "/api/nothing")).status).toBe(404);
  });

  it("signs in with the dev login, keeping only safe return paths", async () => {
    const evil = await call("GET", "/api/auth/dev-login?returnTo=//evil.com");
    expect(evil.location).toBe(`${base}/`);
    const r = await call("GET", "/api/auth/dev-login?returnTo=/courses/c/l");
    expect(r.status).toBe(302);
    expect(r.location).toBe(`${base}/courses/c/l`);
    expect((await call("GET", "/api/auth/me")).json.user).toEqual({ orcid: ADMIN, name: "Josiah Carberry (dev login)", isAdmin: true });
    // without ORCID credentials, the ORCID login falls back to the dev login
    expect((await call("GET", "/api/auth/orcid/login?returnTo=/x")).location).toBe(`${base}/api/auth/dev-login?returnTo=%2Fx`);
  });

  it("creates threads and replies with the DTO of the Next.js API", async () => {
    expect((await call("POST", "/api/comments", { lessonId: "c/l", body: "x", anchor }, { origin: "https://evil.com" })).status).toBe(403);
    expect((await call("POST", "/api/comments", { lessonId: "c/l", body: "x" })).status).toBe(400); // no anchor
    expect((await call("POST", "/api/comments", { lessonId: "c/l", body: " ", anchor })).status).toBe(400);

    const created = await call("POST", "/api/comments", { lessonId: "c/l", body: " Typo here ", kind: "typo", anchor }, { origin: base });
    expect(created.status).toBe(201);
    const c = created.json.comment;
    expect(Object.keys(c).sort()).toEqual(
      ["anchor", "author", "body", "contentHash", "createdAt", "id", "kind", "lessonId", "mine", "parentId", "replies", "status", "updatedAt"].sort(),
    );
    expect(c).toMatchObject({ lessonId: "c/l", parentId: null, kind: "typo", body: "Typo here", status: "open", contentHash: "hash1", mine: true, replies: [] });
    expect(c.anchor).toEqual({ ...anchor, position: 12 });
    expect(c.author).toEqual({ name: "Josiah Carberry (dev login)", orcid: ADMIN });
    expect(Number.isNaN(Date.parse(c.createdAt))).toBe(false);

    const reply = (await call("POST", "/api/comments", { lessonId: "c/l", body: "Agreed", parentId: c.id, kind: "error", anchor })).json.comment;
    expect(reply).toMatchObject({ parentId: c.id, kind: "suggestion", anchor: null, contentHash: null });
    expect((await call("POST", "/api/comments", { lessonId: "c/l", body: "x", parentId: reply.id })).status).toBe(400); // reply to a reply
    expect((await call("POST", "/api/comments", { lessonId: "c/m", body: "x", parentId: c.id })).status).toBe(400); // other lesson

    const list = (await call("GET", "/api/comments?lesson=c/l")).json;
    expect(list.threads).toHaveLength(1);
    expect(list.threads[0].replies.map((r: { id: number }) => r.id)).toEqual([reply.id]);
    expect(list.me.orcid).toBe(ADMIN);
  });

  it("edits, changes the status and deletes, with the permissions of the Next.js API", async () => {
    const [thread] = (await call("GET", "/api/comments?lesson=c/l")).json.threads;
    expect((await call("PATCH", `/api/comments/${thread.id}`, { body: "Typo fixed?" })).json.comment.body).toBe("Typo fixed?");
    expect((await call("PATCH", `/api/comments/${thread.id}`, { status: "resolved" })).json.comment.status).toBe("resolved");
    expect((await call("PATCH", `/api/comments/${thread.id}`, { status: "maybe" })).status).toBe(400);
    expect((await call("PATCH", `/api/comments/${thread.replies[0].id}`, { status: "resolved" })).status).toBe(400);
    expect((await call("PATCH", "/api/comments/9999", { body: "x" })).status).toBe(404);

    // a remark by someone else: the maintainer may not edit it, but may delete it
    const file = path.join(tmp, "data", "remarks.json");
    const store = JSON.parse(fs.readFileSync(file, "utf8"));
    store.users[OTHER] = { name: "Alice" };
    store.comments.push({ ...store.comments[0], id: store.nextId, orcid: OTHER, body: "Hers" });
    store.nextId++;
    fs.writeFileSync(file, JSON.stringify(store));
    const hers = store.nextId - 1;
    expect((await call("PATCH", `/api/comments/${hers}`, { body: "Mine now" })).status).toBe(403);
    const listed = (await call("GET", "/api/comments?lesson=c/l")).json.threads.find((t: { id: number }) => t.id === hers);
    expect(listed).toMatchObject({ mine: false, author: { name: "Alice", orcid: OTHER } });
    expect((await call("DELETE", `/api/comments/${hers}`)).json).toEqual({ ok: true });

    // deleting a thread deletes its replies
    expect((await call("DELETE", `/api/comments/${thread.id}`, undefined, { origin: "https://evil.com" })).status).toBe(403);
    expect((await call("DELETE", `/api/comments/${thread.id}`)).json).toEqual({ ok: true });
    expect((await call("GET", "/api/comments?lesson=c/l")).json.threads).toEqual([]);
    expect(JSON.parse(fs.readFileSync(file, "utf8")).comments).toEqual([]);
  });

  it("exports the remarks with the admin token only", async () => {
    expect((await call("GET", "/api/admin/export")).status).toBe(403);
    expect((await call("GET", "/api/admin/export", undefined, { authorization: "Bearer wrong" })).status).toBe(403);
    const r = await call("GET", "/api/admin/export", undefined, { authorization: `Bearer ${TOKEN}` });
    expect(r.status).toBe(200);
    expect(r.json).toMatchObject({ comments: [], users: { [ADMIN]: { name: "Josiah Carberry (dev login)" } } });
  });

  it("signs out", async () => {
    expect((await call("POST", "/api/auth/logout")).json).toEqual({ ok: true });
    cookie = "";
    expect((await call("GET", "/api/auth/me")).json.user).toBeNull();
  });
});
