import { NextResponse } from "next/server";
import { cookies } from "next/headers";
import { exchangeCode, appUrl } from "@/lib/orcid";
import { upsertUser, startSession, safeReturnTo } from "@/lib/auth";

export async function GET(req: Request) {
  const url = new URL(req.url);
  const jar = await cookies();
  let saved: { state?: string; returnTo?: string } = {};
  try {
    saved = JSON.parse(jar.get("cl_oauth")?.value ?? "{}");
  } catch {}
  jar.delete({ name: "cl_oauth", path: "/api/auth/orcid" });

  const fail = (msg: string) => NextResponse.redirect(new URL(`/signin-error?reason=${encodeURIComponent(msg)}`, appUrl(req)));

  if (url.searchParams.get("error")) return fail(url.searchParams.get("error_description") ?? "ORCID sign-in was cancelled.");
  const code = url.searchParams.get("code");
  const state = url.searchParams.get("state");
  if (!code || !state || !saved.state || state !== saved.state) return fail("The sign-in request expired or was tampered with. Please try again.");

  try {
    const { orcid, name } = await exchangeCode(code, req);
    const user = upsertUser(orcid, name);
    await startSession(user.id);
  } catch (e) {
    console.error(e);
    return fail("Could not verify your ORCID iD. Please try again.");
  }
  return NextResponse.redirect(new URL(safeReturnTo(saved.returnTo), appUrl(req)));
}
