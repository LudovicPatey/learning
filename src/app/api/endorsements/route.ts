import { NextResponse } from "next/server";
import { currentUser, sameOrigin } from "@/lib/auth";
import { getCatalog } from "@/lib/content";
import { listEndorsements, setEndorsement } from "@/lib/comments";

// GET  /api/endorsements                         {endorsements, me}
// POST /api/endorsements  {exercise, endorse}    {endorsements}
export async function GET() {
  return NextResponse.json({ endorsements: listEndorsements(), me: await currentUser() });
}

export async function POST(req: Request) {
  if (!sameOrigin(req)) return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  const me = await currentUser();
  if (!me) return NextResponse.json({ error: "Sign in with ORCID to endorse an exercise." }, { status: 401 });
  const body = (await req.json().catch(() => null)) as Record<string, unknown> | null;
  if (!body) return NextResponse.json({ error: "Invalid JSON" }, { status: 400 });
  const exercise = getCatalog().exercises.get(String(body.exercise ?? ""));
  if (!exercise) return NextResponse.json({ error: "Unknown exercise" }, { status: 404 });
  setEndorsement(me.id, exercise.id, exercise.hash, body.endorse === true);
  return NextResponse.json({ endorsements: listEndorsements() });
}
