import { NextResponse } from "next/server";
import { currentUser, sameOrigin } from "@/lib/auth";
import { getLesson, renderLesson } from "@/lib/content";
import { COMMENT_KINDS, createComment, getComment, getCommentDTO, listThreads, parseAnchor, type CommentKind } from "@/lib/comments";

export async function GET(req: Request) {
  const lessonId = new URL(req.url).searchParams.get("lesson") ?? "";
  if (!getLesson(lessonId)) return NextResponse.json({ error: "Unknown lesson" }, { status: 404 });
  const me = await currentUser();
  return NextResponse.json({ threads: listThreads(lessonId, me), me });
}

export async function POST(req: Request) {
  if (!sameOrigin(req)) return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  const me = await currentUser();
  if (!me) return NextResponse.json({ error: "Sign in with ORCID to comment." }, { status: 401 });

  const body = (await req.json().catch(() => null)) as Record<string, unknown> | null;
  if (!body) return NextResponse.json({ error: "Invalid JSON" }, { status: 400 });

  const lessonId = String(body.lessonId ?? "");
  if (!getLesson(lessonId)) return NextResponse.json({ error: "Unknown lesson" }, { status: 404 });

  const text = typeof body.body === "string" ? body.body.trim() : "";
  if (!text || text.length > 5000) return NextResponse.json({ error: "Comment must be between 1 and 5000 characters." }, { status: 400 });

  let parentId: number | null = null;
  if (body.parentId != null) {
    const parent = getComment(Number(body.parentId));
    if (!parent || parent.lesson_id !== lessonId || parent.parent_id != null) {
      return NextResponse.json({ error: "Invalid parent comment" }, { status: 400 });
    }
    parentId = parent.id;
  }

  const anchor = parentId == null ? parseAnchor(body.anchor) : null;
  if (parentId == null && !anchor) return NextResponse.json({ error: "Select a passage of the lesson to comment on." }, { status: 400 });

  const kind: CommentKind = COMMENT_KINDS.includes(body.kind as CommentKind) ? (body.kind as CommentKind) : "suggestion";
  const rendered = parentId == null ? await renderLesson(lessonId) : null;

  const id = createComment({ lessonId, userId: me.id, parentId, kind: parentId ? "suggestion" : kind, body: text, anchor, contentHash: rendered?.contentHash ?? null });
  return NextResponse.json({ comment: getCommentDTO(id, me) }, { status: 201 });
}
