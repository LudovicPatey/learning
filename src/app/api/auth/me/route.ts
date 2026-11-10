import { NextResponse } from "next/server";
import { currentUser } from "@/lib/auth";
import { orcidConfig, devLoginEnabled } from "@/lib/orcid";

export async function GET() {
  const user = await currentUser();
  return NextResponse.json({ user, orcidConfigured: orcidConfig().enabled, devLogin: devLoginEnabled() });
}
