import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterAll, beforeAll, describe, expect, it, vi } from "vitest";

// A fresh SQLite database for this file, set before the modules are loaded.
const dbDir = fs.mkdtempSync(path.join(os.tmpdir(), "cl-db-"));
process.env.DATABASE_PATH = path.join(dbDir, "test.db");

const { safeReturnTo, sameOrigin, upsertUser } = await import("@/lib/auth");
const { createComment, deleteComment, getCommentDTO, listThreads, parseAnchor, updateComment } = await import("@/lib/comments");
const { exchangeCode, orcidConfig } = await import("@/lib/orcid");

afterAll(() => fs.rmSync(dbDir, { recursive: true, force: true }));

describe("safeReturnTo", () => {
  it.each([
    ["/courses/x", "/courses/x"],
    ["/courses/x?y=1#z", "/courses/x?y=1#z"],
    ["//evil.com", "/"],
    ["https://evil.com", "/"],
    ["/\\evil.com", "/"],
    [null, "/"],
    ["", "/"],
  ])("%s -> %s", (input, expected) => {
    expect(safeReturnTo(input)).toBe(expected);
  });
});

describe("sameOrigin", () => {
  const req = (headers: Record<string, string>) => new Request("http://localhost:3000/api/x", { method: "POST", headers });
  it("accepts same-origin and origin-less requests", () => {
    expect(sameOrigin(req({ origin: "http://localhost:3000", host: "localhost:3000" }))).toBe(true);
    expect(sameOrigin(req({ host: "localhost:3000" }))).toBe(true);
  });
  it("rejects cross-site requests", () => {
    expect(sameOrigin(req({ origin: "https://evil.com", host: "localhost:3000" }))).toBe(false);
    expect(sameOrigin(req({ origin: "not a url", host: "localhost:3000" }))).toBe(false);
  });
});

describe("parseAnchor", () => {
  it("validates and truncates", () => {
    expect(parseAnchor(null)).toBeNull();
    expect(parseAnchor({ exact: "   " })).toBeNull();
    const a = parseAnchor({ exact: "abc", prefix: "x".repeat(100), suffix: "y", position: 3.7, display: "" })!;
    expect(a.prefix).toHaveLength(64);
    expect(a.position).toBe(3);
    expect(a.display).toBe("abc");
    expect(parseAnchor({ exact: "abc", position: -5 })!.position).toBe(0);
  });
});

describe("users and comments", () => {
  let aliceId: number;
  let bobId: number;

  beforeAll(() => {
    process.env.ADMIN_ORCIDS = "0000-0000-0000-0002";
    aliceId = upsertUser("0000-0000-0000-0001", "Alice").id;
    bobId = upsertUser("0000-0000-0000-0002", "Bob").id;
  });

  it("upserts users by ORCID iD and flags maintainers", () => {
    const again = upsertUser("0000-0000-0000-0001", "Alice Updated");
    expect(again.id).toBe(aliceId);
    expect(again.name).toBe("Alice Updated");
    expect(again.isAdmin).toBe(false);
    expect(upsertUser("0000-0000-0000-0002", "Bob").isAdmin).toBe(true);
  });

  it("creates threads with replies, updates and deletes them", () => {
    const anchor = { exact: "text", prefix: "", suffix: "", position: 0, display: "text" };
    const id = createComment({ lessonId: "c/l", userId: aliceId, parentId: null, kind: "typo", body: "Fix", anchor, contentHash: "h" });
    const reply = createComment({ lessonId: "c/l", userId: bobId, parentId: id, kind: "suggestion", body: "Done", anchor: null, contentHash: null });

    const me = { id: aliceId, orcid: "0000-0000-0000-0001", name: "Alice", isAdmin: false };
    const threads = listThreads("c/l", me);
    expect(threads).toHaveLength(1);
    expect(threads[0].mine).toBe(true);
    expect(threads[0].anchor).toEqual(anchor);
    expect(threads[0].replies.map((r) => r.id)).toEqual([reply]);
    expect(threads[0].replies[0].mine).toBe(false);
    expect(listThreads("other/lesson", me)).toEqual([]);

    updateComment(id, { status: "resolved", body: "Fixed typo" });
    const dto = getCommentDTO(id, me)!;
    expect(dto.status).toBe("resolved");
    expect(dto.body).toBe("Fixed typo");

    deleteComment(id);
    expect(getCommentDTO(id, me)).toBeNull();
    expect(getCommentDTO(reply, me)).toBeNull(); // replies are deleted with their thread
  });
});

describe("ORCID", () => {
  it("is disabled without credentials", () => {
    delete process.env.ORCID_CLIENT_ID;
    expect(orcidConfig().enabled).toBe(false);
  });

  it("exchanges a code for a validated ORCID iD", async () => {
    // stray whitespace in pasted credentials is removed (a trailing line break once broke sign-in)
    process.env.ORCID_CLIENT_ID = " id";
    process.env.ORCID_CLIENT_SECRET = "secret\n";
    process.env.ORCID_BASE_URL = "https://sandbox.orcid.org/ ";
    const fetchMock = vi.fn(async () => new Response(JSON.stringify({ orcid: "0000-0002-1825-009X", name: " Jo " }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);
    const res = await exchangeCode("abc", new Request("http://localhost:3000/api/auth/orcid/callback"));
    expect(res).toEqual({ orcid: "0000-0002-1825-009X", name: "Jo" });
    const [url, init] = fetchMock.mock.calls[0] as unknown as [string, RequestInit];
    expect(url).toBe("https://sandbox.orcid.org/oauth/token");
    expect(String(init.body)).toContain("redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fapi%2Fauth%2Forcid%2Fcallback");
    expect(String(init.body)).toContain("client_id=id&client_secret=secret&");
    vi.unstubAllGlobals();
  });

  it("rejects malformed responses", async () => {
    vi.stubGlobal("fetch", vi.fn(async () => new Response(JSON.stringify({ orcid: "bogus" }), { status: 200 })));
    await expect(exchangeCode("abc", new Request("http://localhost/"))).rejects.toThrow(/valid iD/);
    vi.stubGlobal("fetch", vi.fn(async () => new Response("no", { status: 401 })));
    await expect(exchangeCode("abc", new Request("http://localhost/"))).rejects.toThrow(/401/);
    vi.unstubAllGlobals();
  });
});
