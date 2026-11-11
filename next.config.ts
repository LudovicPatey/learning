import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import type { NextConfig } from "next";

// STATIC_EXPORT=1 (npm run build:static) builds the static site deployed to the
// PHP web hosting (docs/DEPLOY.md): plain HTML files in out/, one directory per
// page. The API route handlers (src/app/api/**/route.ts) are left out, since
// only .tsx files are read in that mode; on the server, the same URLs are
// served by the PHP implementation in deploy/api/.
const staticExport = process.env.STATIC_EXPORT === "1";

// The build id is written into every page. Deriving it from the code only (not
// from the content or the time) keeps the pages of unchanged lessons identical
// from one build to the next, so that the deployment only uploads what changed.
function codeHash(): string {
  const h = crypto.createHash("sha256");
  const walk = (p: string) => {
    if (fs.statSync(p).isDirectory()) for (const f of fs.readdirSync(p).sort()) walk(path.join(p, f));
    else h.update(p).update(fs.readFileSync(p));
  };
  for (const p of ["src", "package-lock.json", "next.config.ts"]) walk(path.join(import.meta.dirname, p));
  return h.digest("hex").slice(0, 20);
}

const nextConfig: NextConfig = {
  // better-sqlite3 is a native module and must stay on the Node side.
  serverExternalPackages: ["better-sqlite3"],
  // Pin the project root (a package-lock.json higher up would confuse auto-detection).
  turbopack: { root: import.meta.dirname },
  ...(staticExport
    ? { output: "export", trailingSlash: true, pageExtensions: ["tsx"], generateBuildId: async () => codeHash() }
    : {}),
};

export default nextConfig;
