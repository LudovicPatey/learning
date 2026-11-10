import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // better-sqlite3 is a native module and must stay on the Node side.
  serverExternalPackages: ["better-sqlite3"],
  // Pin the project root (a package-lock.json higher up would confuse auto-detection).
  turbopack: { root: import.meta.dirname },
};

export default nextConfig;
