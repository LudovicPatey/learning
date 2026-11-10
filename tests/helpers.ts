import fs from "node:fs";
import os from "node:os";
import path from "node:path";

/** Copy the fixture content tree to a fresh temporary directory and point the loader at it. */
export function useFixtureContent(): string {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "cl-content-"));
  fs.cpSync(path.join(__dirname, "fixtures", "content"), dir, { recursive: true });
  process.env.CONTENT_DIR = dir;
  return dir;
}

export function stripTags(html: string): string {
  return html.replace(/<[^>]+>/g, "");
}
