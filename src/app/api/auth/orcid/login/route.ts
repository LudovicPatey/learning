import crypto from "node:crypto";
import { NextResponse } from "next/server";
import { orcidConfig, redirectUri, devLoginEnabled } from "@/lib/orcid";
import { safeReturnTo } from "@/lib/auth";

export async function GET(req: Request) {
  const url = new URL(req.url);
  const returnTo = safeReturnTo(url.searchParams.get("returnTo"));
  const cfg = orcidConfig();
  if (!cfg.enabled) {
    if (devLoginEnabled()) {
      return NextResponse.redirect(new URL(`/api/auth/dev-login?returnTo=${encodeURIComponent(returnTo)}`, req.url));
    }
    return new NextResponse("ORCID sign-in is not configured (set ORCID_CLIENT_ID and ORCID_CLIENT_SECRET).", { status: 503 });
  }
  const state = crypto.randomBytes(16).toString("base64url");
  const authorize = new URL(`${cfg.base}/oauth/authorize`);
  authorize.search = new URLSearchParams({
    client_id: cfg.clientId!,
    response_type: "code",
    scope: cfg.scope,
    redirect_uri: redirectUri(req),
    state,
  }).toString();
  const res = NextResponse.redirect(authorize);
  res.cookies.set("cl_oauth", JSON.stringify({ state, returnTo }), {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/api/auth/orcid",
    maxAge: 600,
  });
  return res;
}
