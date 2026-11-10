import crypto from "node:crypto";
import { cookies } from "next/headers";
import { db } from "./db.ts";

export type User = { id: number; orcid: string; name: string; isAdmin: boolean };

const SESSION_COOKIE = "cl_session";
const SESSION_DAYS = 30;

const sha256 = (s: string) => crypto.createHash("sha256").update(s).digest("hex");

function adminOrcids(): Set<string> {
  return new Set((process.env.ADMIN_ORCIDS ?? "").split(",").map((s) => s.trim()).filter(Boolean));
}

function toUser(row: { id: number; orcid: string; name: string }): User {
  return { ...row, isAdmin: adminOrcids().has(row.orcid) };
}

export function upsertUser(orcid: string, name: string): User {
  const row = db()
    .prepare(
      `INSERT INTO users (orcid, name, last_login_at) VALUES (?, ?, datetime('now'))
       ON CONFLICT(orcid) DO UPDATE SET name = excluded.name, last_login_at = datetime('now')
       RETURNING id, orcid, name`,
    )
    .get(orcid, name) as { id: number; orcid: string; name: string };
  return toUser(row);
}

export async function startSession(userId: number) {
  const token = crypto.randomBytes(32).toString("base64url");
  const expires = new Date(Date.now() + SESSION_DAYS * 86400_000);
  db().prepare("INSERT INTO sessions (token_hash, user_id, expires_at) VALUES (?, ?, ?)").run(sha256(token), userId, expires.toISOString());
  (await cookies()).set(SESSION_COOKIE, token, {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    expires,
  });
}

export async function currentUser(): Promise<User | null> {
  const token = (await cookies()).get(SESSION_COOKIE)?.value;
  if (!token) return null;
  const row = db()
    .prepare(
      `SELECT u.id, u.orcid, u.name FROM sessions s JOIN users u ON u.id = s.user_id
       WHERE s.token_hash = ? AND s.expires_at > ?`,
    )
    .get(sha256(token), new Date().toISOString()) as { id: number; orcid: string; name: string } | undefined;
  return row ? toUser(row) : null;
}

export async function endSession() {
  const jar = await cookies();
  const token = jar.get(SESSION_COOKIE)?.value;
  if (token) db().prepare("DELETE FROM sessions WHERE token_hash = ?").run(sha256(token));
  jar.delete(SESSION_COOKIE);
}

/** Only allow same-site relative paths as post-login destinations. */
export function safeReturnTo(value: string | null | undefined): string {
  if (!value || !value.startsWith("/") || value.startsWith("//") || value.includes("\\")) return "/";
  return value;
}

/** Reject cross-site state-changing requests (defence in depth on top of SameSite cookies). */
export function sameOrigin(req: Request): boolean {
  const origin = req.headers.get("origin");
  if (!origin) return true; // same-origin fetches from older browsers may omit it; SameSite=Lax still applies
  try {
    return new URL(origin).host === (req.headers.get("x-forwarded-host") ?? req.headers.get("host"));
  } catch {
    return false;
  }
}
