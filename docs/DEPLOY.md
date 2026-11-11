# Deployment

The live site runs on PHP web hosting (OVH), which cannot run Node.js. It is
therefore deployed in two parts, modeled on the RM Zoo:

- the **course notes** as a static export of the Next.js site (plain HTML, one
  directory per page, built by `npm run build:static` into `out/`);
- the **reader remarks** (ORCID sign-in, comments) by a small PHP server in
  `deploy/api/`, which answers the same URLs with the same JSON as the Next.js
  API of `src/app/api/`. The browser code is the same in development and in
  production; only the server behind `/api/` changes.

The site's folder must be the root of its domain (a subdomain such as
`learning.example.org`), since pages use absolute paths.

## Deploying

```bash
npm run verify                    # as before every commit
npm run deploy -- --dry-run       # build out/ and list what would be uploaded
npm run deploy                    # build out/ and upload what changed
```

To try the built site before uploading it, `npm run build:static` then
`npm run preview:static` serves `out/` on <http://localhost:8137> with PHP's
built-in server, as the hosting does: static pages, and the PHP remarks server
under `/api/` with the dev login (remarks stored in `cache/preview-data/`).

`npm run deploy` builds `out/` with `scripts/build-static.ts`, then uploads over
SFTP the files of `out/` whose content changed since the last deployment to the
same target. The hashes of the uploaded files are kept in
`cache/deploy-manifest.json`; `--all` uploads everything again (after a manual
change on the server, for instance). Nothing is ever deleted on the server:
files of older builds stay there, unused. A failed upload stops the transfer and
leaves the manifest unchanged.

Settings are read from `cache/deploy.json` (git-ignored):

```json
{ "protocol": "sftp", "host": "ftp.clusterXXX.hosting.ovh.net", "user": "LOGIN", "dir": "learning" }
```

`dir` is the site's folder, relative to the FTP home directory. With SFTP, ssh
asks the FTP password in the terminal (an SSH key works too). `--protocol ftp`
uses FTP with TLS through curl, for hosts that support it (OVH does not); the
password is then asked, or read from `LEARNING_FTP_PASSWORD`, and never stored.
Every option can also be given on the command line: `--host`, `--user`, `--dir`.

What is uploaded, and only that: the files of `out/`, that is the static export,
`api/index.php`, `api/lib.php`, `api/.htaccess`, `api/config.example.php`,
`api/lessons.json` (the lessons that accept remarks, with the hash of their
source) and the root `.htaccess` (`deploy/htaccess.txt`: HTTPS redirect, 404
page, compression, caching). A file named `config.php` is never uploaded, and
nothing outside `out/` is (in particular not `external-data/`).

## Setting up the remarks server (once)

1. In the OVH control panel, attach the subdomain to the folder `learning/`
   (Multisite), with HTTPS.
2. Register an ORCID public API client at <https://orcid.org/developer-tools>,
   with the redirect URI `https://<site>/api/auth/orcid/callback`.
3. Deploy once, then on the server copy `learning/api/config.example.php` to
   `learning/api/config.php` and fill in the ORCID client, the maintainers'
   ORCID iDs (`admin_orcids`) and, optionally, an `admin_token` for exports.
   `config.php` is not overwritten by later deployments.
4. Check `https://<site>/api/auth/me`: it answers
   `{"user":null,"orcidConfigured":true,"devLogin":false}`.

Remarks and sessions are stored in `learning-data/` next to the site's folder,
outside the web root (`data_dir` in `config.php` to change it). To download them:

```bash
curl -H "Authorization: Bearer <admin_token>" https://<site>/api/admin/export > remarks.json
```

## Keeping the two servers in step

The API exists twice: in TypeScript (`src/app/api/`, `src/lib/auth.ts`,
`comments.ts`, `orcid.ts`), used by `npm run dev`, and in PHP (`deploy/api/`),
used by the live site. A change to one must be made to the other.
`tests/php-api.test.ts` runs the PHP server with `php -S` and checks its routes,
permissions and JSON against the contract of the TypeScript API; it is skipped
when PHP is not installed.

Static export constraints (checked by `npm run build:static`): pages must not use
request-time data (cookies, headers, search parameters on the server), and every
dynamic route needs `generateStaticParams()`. The routes of released versions use
`withExportPlaceholder()` (`src/lib/versions.ts`) while no version exists.
