import { NextResponse } from "next/server";
import { currentUser } from "@/lib/auth";
import { listUserComments, listUserEndorsements } from "@/lib/comments";

// GET /api/me/activity   {comments, endorsements} of the signed-in person
export async function GET() {
  const me = await currentUser();
  if (!me) return NextResponse.json({ error: "Not signed in" }, { status: 401 });
  return NextResponse.json({ comments: listUserComments(me), endorsements: listUserEndorsements(me.id) });
}
