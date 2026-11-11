// Upload the site to the web hosting (docs/DEPLOY.md): builds out/ with
// scripts/build-static.ts, then uploads the files of out/ that changed since the
// last deployment. Nothing is ever deleted on the server; its api/config.php and
// the remarks (in learning-data/, outside the web root) are never touched.
//
//   npm run deploy -- [--dry-run] [--all] [--no-build] [--protocol sftp|ftp] [--host H] [--user U] [--dir learning] [--no-tls]
//
//   --dry-run   build and list what would be uploaded, upload nothing
//   --all       upload every file, not only those changed since the last deployment
//   --no-build  use out/ as it is
//
// Settings are read from cache/deploy.json (git-ignored), e.g.
//   { "protocol": "sftp", "host": "ftp.clusterXXX.hosting.ovh.net", "user": "LOGIN", "dir": "learning" }
// sftp: OpenSSH sftp (OVH web hosting accepts it with the FTP password, which ssh
//       asks in the terminal; an SSH key works too). The default.
// ftp:  FTP with TLS through curl, for hosts that support it (OVH does not); the
//       password is asked (or LEARNING_FTP_PASSWORD), never stored.
// The hashes of the uploaded files are kept in cache/deploy-manifest.json.
import { execFileSync, spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { changedFiles, curlConfig, deployFiles, sftpBatch, updatedManifest, type Manifest } from "../src/lib/deploy.ts";

const root = path.resolve(import.meta.dirname, "..");
process.chdir(root);
const usage = "npm run deploy -- [--dry-run] [--all] [--no-build] [--protocol sftp|ftp] [--host H] [--user U] [--dir learning] [--no-tls]";

// ---- options -------------------------------------------------------------------
const argv = process.argv.slice(2);
const flags = new Set<string>();
const values = new Map<string, string>();
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (["--dry-run", "--all", "--no-build", "--no-tls"].includes(a)) flags.add(a);
  else if (["--protocol", "--host", "--user", "--dir"].includes(a) && i + 1 < argv.length) values.set(a, argv[++i]);
  else {
    console.error(`Unknown option ${a}\nUsage: ${usage}`);
    process.exit(1);
  }
}
const saved = fs.existsSync("cache/deploy.json") ? JSON.parse(fs.readFileSync("cache/deploy.json", "utf8")) : {};
const opt = {
  protocol: values.get("--protocol") ?? saved.protocol ?? "sftp",
  host: values.get("--host") ?? saved.host,
  user: values.get("--user") ?? saved.user,
  dir: values.get("--dir") ?? saved.dir ?? "learning",
  tls: !flags.has("--no-tls") && saved.tls !== false,
};
const dry = flags.has("--dry-run");
if (!["ftp", "sftp"].includes(opt.protocol)) {
  console.error("--protocol: ftp or sftp");
  process.exit(1);
}
if (!dry && (!opt.host || !opt.user)) {
  console.error(
    'No host/user: create cache/deploy.json, e.g.\n  { "protocol": "sftp", "host": "ftp.clusterXXX.hosting.ovh.net", "user": "LOGIN", "dir": "learning" }\n(the FTP host and login are in the OVH control panel: Web hosting → FTP-SSH)',
  );
  process.exit(1);
}

// ---- build and checks ----------------------------------------------------------
try {
  const dirty = execFileSync("git", ["status", "--porcelain", "--", "content", "src", "deploy", "scripts"], { encoding: "utf8" }).trim();
  if (dirty) console.warn(`! uncommitted changes (the live site will differ from GitHub):\n${dirty.split("\n").map((l) => "    " + l).join("\n")}`);
} catch {
  /* not a git checkout */
}
if (!flags.has("--no-build")) {
  const r = spawnSync("node", ["--experimental-strip-types", "--no-warnings", "scripts/build-static.ts"], { stdio: "inherit" });
  if (r.status !== 0) {
    console.error("The build failed: nothing uploaded.");
    process.exit(1);
  }
}

const files = deployFiles("out");
const target = `${opt.protocol}://${opt.user ?? "?"}@${opt.host ?? "?"}/${opt.dir}`;
const manifestFile = "cache/deploy-manifest.json";
const manifests: Record<string, Manifest> = fs.existsSync(manifestFile) ? JSON.parse(fs.readFileSync(manifestFile, "utf8")) : {};
const manifest = flags.has("--all") ? {} : (manifests[target] ?? {});
const todo = changedFiles(files, manifest);
const mb = (list: { size: number }[]) => (list.reduce((s, f) => s + f.size, 0) / 1e6).toFixed(1);

console.log(`\n${files.length} files in out/ (${mb(files)} MB); ${todo.length} to upload (${mb(todo)} MB) → ${target}`);
for (const f of todo.slice(0, 40)) console.log(`  ${f.remote}`);
if (todo.length > 40) console.log(`  … and ${todo.length - 40} more`);
console.log("Nothing is deleted on the server; api/config.php and learning-data/ are not touched.");
if (dry || todo.length === 0) {
  console.log(dry ? "(dry run: nothing uploaded)" : "Nothing to upload.");
  process.exit(0);
}

// ---- upload --------------------------------------------------------------------
if (opt.protocol === "ftp") {
  const password = process.env.LEARNING_FTP_PASSWORD || (await askHidden(`FTP password for ${opt.user}@${opt.host}: `));
  const r = spawnSync("curl", ["-K", "-"], { input: curlConfig(todo, { ...opt, password }) + "fail-early\n", stdio: ["pipe", "inherit", "inherit"] });
  if (r.status !== 0) {
    console.error(`curl failed (exit ${r.status}).${opt.tls ? " If the server does not support TLS (OVH does not), use --protocol sftp rather than --no-tls, which sends the password in clear." : ""}`);
    process.exit(1);
  }
} else {
  // batch commands on stdin (`-b -`): sftp stops at the first failed upload and exits
  // with an error, so that the manifest only records what is online; BatchMode=no
  // lets ssh ask the password on the terminal
  const r = spawnSync("sftp", ["-o", "BatchMode=no", "-o", "ConnectTimeout=20", "-b", "-", `${opt.user}@${opt.host}`], {
    input: sftpBatch(todo, opt),
    stdio: ["pipe", "inherit", "inherit"],
  });
  if (r.status !== 0) {
    console.error(`sftp failed (exit ${r.status}); the manifest is unchanged, so the next deployment uploads these files again.`);
    process.exit(1);
  }
}
manifests[target] = updatedManifest(manifest, todo);
fs.mkdirSync("cache", { recursive: true });
fs.writeFileSync(manifestFile, JSON.stringify(manifests, null, 1) + "\n");
console.log(`✓ ${todo.length} files uploaded. Reload the site without cache to check.`);

function askHidden(prompt: string): Promise<string> {
  return new Promise((resolve) => {
    const { stdin, stdout } = process;
    if (!stdin.isTTY) {
      console.error("No terminal to ask the password: set LEARNING_FTP_PASSWORD.");
      process.exit(1);
    }
    stdout.write(prompt);
    stdin.setRawMode(true);
    stdin.resume();
    stdin.setEncoding("utf8");
    let s = "";
    const on = (ch: string) => {
      if (ch === "\r" || ch === "\n") {
        stdin.setRawMode(false);
        stdin.pause();
        stdin.off("data", on);
        stdout.write("\n");
        resolve(s);
      } else if (ch === "\u0003") {
        stdout.write("\n");
        process.exit(130);
      } else if (ch === "\u007f") s = s.slice(0, -1);
      else s += ch;
    };
    stdin.on("data", on);
  });
}
