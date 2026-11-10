import { NextResponse } from "next/server";
import { devLoginEnabled } from "@/lib/orcid";
import { upsertUser, startSession, safeReturnTo } from "@/lib/auth";

// Local development only: signs in as ORCID's documented fictitious researcher.
export async function GET(req: Request) {
  if (!devLoginEnabled()) return new NextResponse("Not found", { status: 404 });
  const user = upsertUser("0000-0002-1825-0097", "Josiah Carberry (dev login)");
  await startSession(user.id);
  const returnTo = safeReturnTo(new URL(req.url).searchParams.get("returnTo"));
  return NextResponse.redirect(new URL(returnTo, req.url));
}
