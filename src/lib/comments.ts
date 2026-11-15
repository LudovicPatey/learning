import { db } from "./db.ts";
import type { User } from "./auth.ts";

import {
  COMMENT_KINDS,
  COMMENT_STATUSES,
  type Anchor,
  type CommentDTO,
  type CommentKind,
  type CommentStatus,
  type EndorsementDTO,
} from "./comment-types.ts";
export { COMMENT_KINDS, COMMENT_STATUSES, type Anchor, type CommentDTO, type CommentKind, type CommentStatus, type EndorsementDTO };

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

/** All comments of one person (threads and replies), newest first. */
export function listUserComments(me: User): CommentDTO[] {
  const rows = db().prepare(`${SELECT} WHERE c.user_id = ? ORDER BY c.created_at DESC, c.id DESC`).all(me.id) as Row[];
  return rows.map((r) => toDTO(r, me));
}

// ---- endorsements

type EndorsementRow = { exercise_id: string; content_hash: string | null; created_at: string; name: string; orcid: string };
const SELECT_ENDORSEMENTS = `SELECT e.exercise_id, e.content_hash, e.created_at, u.name, u.orcid FROM endorsements e JOIN users u ON u.id = e.user_id`;
const endorsementDTO = (r: EndorsementRow): EndorsementDTO => ({
  exercise: r.exercise_id,
  contentHash: r.content_hash,
  createdAt: r.created_at + "Z",
  author: { name: r.name, orcid: r.orcid },
});

/** All endorsements, oldest first. */
export function listEndorsements(): EndorsementDTO[] {
  return (db().prepare(`${SELECT_ENDORSEMENTS} ORDER BY e.created_at, e.exercise_id, u.orcid`).all() as EndorsementRow[]).map(endorsementDTO);
}

/** The endorsements of one person, newest first. */
export function listUserEndorsements(userId: number): EndorsementDTO[] {
  return (db().prepare(`${SELECT_ENDORSEMENTS} WHERE e.user_id = ? ORDER BY e.created_at DESC, e.exercise_id`).all(userId) as EndorsementRow[]).map(
    endorsementDTO,
  );
}

/** Endorse an exercise (recording the version checked; endorsing again updates it), or withdraw. */
export function setEndorsement(userId: number, exerciseId: string, contentHash: string, endorse: boolean) {
  if (endorse) {
    db()
      .prepare(
        `INSERT INTO endorsements (user_id, exercise_id, content_hash) VALUES (?, ?, ?)
         ON CONFLICT(user_id, exercise_id) DO UPDATE SET content_hash = excluded.content_hash, created_at = datetime('now')`,
      )
      .run(userId, exerciseId, contentHash);
  } else {
    db().prepare(`DELETE FROM endorsements WHERE user_id = ? AND exercise_id = ?`).run(userId, exerciseId);
  }
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
