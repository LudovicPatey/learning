import { NextResponse } from "next/server";
import { endSession, sameOrigin } from "@/lib/auth";

export async function POST(req: Request) {
  if (!sameOrigin(req)) return new NextResponse("Forbidden", { status: 403 });
  await endSession();
  return NextResponse.json({ ok: true });
}
