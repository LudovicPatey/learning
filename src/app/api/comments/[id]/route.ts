import { NextResponse } from "next/server";
import { currentUser, sameOrigin } from "@/lib/auth";
import { COMMENT_STATUSES, deleteComment, getComment, getCommentDTO, updateComment, type CommentStatus } from "@/lib/comments";

type Ctx = { params: Promise<{ id: string }> };

async function load(req: Request, ctx: Ctx) {
  if (!sameOrigin(req)) return { error: NextResponse.json({ error: "Forbidden" }, { status: 403 }) };
  const me = await currentUser();
  if (!me) return { error: NextResponse.json({ error: "Not signed in" }, { status: 401 }) };
  const row = getComment(Number((await ctx.params).id));
  if (!row) return { error: NextResponse.json({ error: "Not found" }, { status: 404 }) };
  return { me, row };
}

export async function PATCH(req: Request, ctx: Ctx) {
  const r = await load(req, ctx);
  if ("error" in r) return r.error;
  const { me, row } = r;
  const body = (await req.json().catch(() => ({}))) as Record<string, unknown>;

  if (body.status !== undefined) {
    if (!me.isAdmin) return NextResponse.json({ error: "Only maintainers can change the status." }, { status: 403 });
    if (!COMMENT_STATUSES.includes(body.status as CommentStatus) || row.parent_id != null) {
      return NextResponse.json({ error: "Invalid status" }, { status: 400 });
    }
    updateComment(row.id, { status: body.status as CommentStatus });
  }
  if (body.body !== undefined) {
    if (row.user_id !== me.id) return NextResponse.json({ error: "You can only edit your own comments." }, { status: 403 });
    const text = typeof body.body === "string" ? body.body.trim() : "";
    if (!text || text.length > 5000) return NextResponse.json({ error: "Comment must be between 1 and 5000 characters." }, { status: 400 });
    updateComment(row.id, { body: text });
  }
  return NextResponse.json({ comment: getCommentDTO(row.id, me) });
}

export async function DELETE(req: Request, ctx: Ctx) {
  const r = await load(req, ctx);
  if ("error" in r) return r.error;
  if (r.row.user_id !== r.me.id && !r.me.isAdmin) return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  deleteComment(r.row.id);
  return NextResponse.json({ ok: true });
}
