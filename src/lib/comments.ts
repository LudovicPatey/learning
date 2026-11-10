import { db } from "./db.ts";
import type { User } from "./auth.ts";

import { COMMENT_KINDS, COMMENT_STATUSES, type Anchor, type CommentDTO, type CommentKind, type CommentStatus } from "./comment-types.ts";
export { COMMENT_KINDS, COMMENT_STATUSES, type Anchor, type CommentDTO, type CommentKind, type CommentStatus };

type Row = {
  id: number;
  lesson_id: string;
  parent_id: number | null;
  kind: CommentKind;
  body: string;
  anchor: string | null;
  status: CommentStatus;
  content_hash: string | null;
  created_at: string;
  updated_at: string;
  user_id: number;
  name: string;
  orcid: string;
};

const SELECT = `SELECT c.*, u.name, u.orcid FROM comments c JOIN users u ON u.id = c.user_id`;

function toDTO(r: Row, me: User | null): CommentDTO {
  return {
    id: r.id,
    lessonId: r.lesson_id,
    parentId: r.parent_id,
    kind: r.kind,
    body: r.body,
    anchor: r.anchor ? JSON.parse(r.anchor) : null,
    status: r.status,
    contentHash: r.content_hash,
    createdAt: r.created_at + "Z",
    updatedAt: r.updated_at + "Z",
    author: { name: r.name, orcid: r.orcid },
    mine: me?.id === r.user_id,
    replies: [],
  };
}

export function listThreads(lessonId: string, me: User | null): CommentDTO[] {
  const rows = db().prepare(`${SELECT} WHERE c.lesson_id = ? ORDER BY c.created_at, c.id`).all(lessonId) as Row[];
  const byId = new Map<number, CommentDTO>();
  const threads: CommentDTO[] = [];
  for (const r of rows) {
    const dto = toDTO(r, me);
    byId.set(dto.id, dto);
    if (dto.parentId == null) threads.push(dto);
    else byId.get(dto.parentId)?.replies.push(dto);
  }
  return threads;
}

export function getComment(id: number) {
  return db().prepare(`${SELECT} WHERE c.id = ?`).get(id) as Row | undefined;
}

export function getCommentDTO(id: number, me: User | null) {
  const r = getComment(id);
  return r ? toDTO(r, me) : null;
}

export function createComment(input: {
  lessonId: string;
  userId: number;
  parentId: number | null;
  kind: CommentKind;
  body: string;
  anchor: Anchor | null;
  contentHash: string | null;
}): number {
  const res = db()
    .prepare(
      `INSERT INTO comments (lesson_id, user_id, parent_id, kind, body, anchor, content_hash) VALUES (?, ?, ?, ?, ?, ?, ?)`,
    )
    .run(input.lessonId, input.userId, input.parentId, input.kind, input.body, input.anchor ? JSON.stringify(input.anchor) : null, input.contentHash);
  return Number(res.lastInsertRowid);
}

export function updateComment(id: number, patch: { body?: string; status?: CommentStatus }) {
  if (patch.body !== undefined) db().prepare(`UPDATE comments SET body = ?, updated_at = datetime('now') WHERE id = ?`).run(patch.body, id);
  if (patch.status !== undefined) db().prepare(`UPDATE comments SET status = ?, updated_at = datetime('now') WHERE id = ?`).run(patch.status, id);
}

export function deleteComment(id: number) {
  db().prepare(`DELETE FROM comments WHERE id = ?`).run(id);
}

const str = (v: unknown, max: number) => (typeof v === "string" ? v.slice(0, max) : "");

export function parseAnchor(v: unknown): Anchor | null {
  if (!v || typeof v !== "object") return null;
  const a = v as Record<string, unknown>;
  const exact = str(a.exact, 2000);
  if (!exact.trim()) return null;
  return {
    exact,
    prefix: str(a.prefix, 64),
    suffix: str(a.suffix, 64),
    position: Number.isFinite(a.position) ? Math.max(0, Math.floor(a.position as number)) : 0,
    display: str(a.display, 2000) || exact,
  };
}
