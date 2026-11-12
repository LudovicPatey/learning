// ORCID OAuth 2.0 (three-legged, "/authenticate" scope).
// Docs: https://info.orcid.org/documentation/integration-guide/
export function orcidConfig() {
  // trimmed, as in deploy/api/lib.php: stray whitespace in pasted credentials makes ORCID reject them
  const clientId = process.env.ORCID_CLIENT_ID?.trim();
  const clientSecret = process.env.ORCID_CLIENT_SECRET?.trim();
  const base = (process.env.ORCID_BASE_URL ?? "https://orcid.org").trim().replace(/\/$/, "");
  const scope = process.env.ORCID_SCOPE ?? "/authenticate";
  return { clientId, clientSecret, base, scope, enabled: Boolean(clientId && clientSecret) };
}

/** Dev login is a stand-in for ORCID during local development only. */
export const devLoginEnabled = () => process.env.NODE_ENV === "development";

export function appUrl(req: Request): string {
  if (process.env.APP_URL) return process.env.APP_URL.replace(/\/$/, "");
  return new URL(req.url).origin;
}

export function redirectUri(req: Request) {
  return `${appUrl(req)}/api/auth/orcid/callback`;
}

export async function exchangeCode(code: string, req: Request): Promise<{ orcid: string; name: string }> {
  const cfg = orcidConfig();
  const res = await fetch(`${cfg.base}/oauth/token`, {
    method: "POST",
    headers: { Accept: "application/json", "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: cfg.clientId!,
      client_secret: cfg.clientSecret!,
      grant_type: "authorization_code",
      code,
      redirect_uri: redirectUri(req),
    }),
    cache: "no-store",
  });
  if (!res.ok) throw new Error(`ORCID token exchange failed (${res.status})`);
  const data = (await res.json()) as { orcid?: string; name?: string };
  if (!data.orcid || !/^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$/.test(data.orcid)) throw new Error("ORCID response had no valid iD");
  return { orcid: data.orcid, name: data.name?.trim() || data.orcid };
}
