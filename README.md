# Computability Theory

An online course platform for computability theory and related fields (algorithmic randomness, reverse mathematics, higher computability).

- **Small courses.** Each course is a short series of lessons on one topic (e.g. *Models of computation*). Main courses are organized in learning tracks (`content/tracks.yaml`), each shown as a dependency graph on the home page; specialized courses are listed in the searchable catalogue only.
- **Small lessons.** Each lesson is one Markdown file covering one idea, with explicit prerequisites.
- **Check-up questions right after proofs.** Multiple-choice questions that test one step of the argument, with an explanation for every option.
- **Reader suggestions.** Readers select any passage, sign in with ORCID, and leave a typed suggestion (typo, unclear, mathematical error, …). Maintainers can resolve or decline them.

The book sources in `external-data/` served as a reference for the level of detail. The four tracks (computability, algorithmic randomness, reverse mathematics, higher computability; 19 core courses) and eight specialized courses are written. Each course has a design log, `content/<course>/_design.md`, and the tracks have `content/tracks-design.md`.

## Running it

```bash
npm install
npm run dev          # http://localhost:3000
```

Without ORCID credentials, "Sign in with ORCID" signs you in locally as a test account (development only).

To enable real ORCID sign-in, copy `.env.example` to `.env.local` and fill in:

- `ORCID_CLIENT_ID` / `ORCID_CLIENT_SECRET`: register a client at <https://orcid.org/developer-tools> (or the sandbox, <https://sandbox.orcid.org/developer-tools>, with `ORCID_BASE_URL=https://sandbox.orcid.org`).
- Redirect URI to register: `${APP_URL}/api/auth/orcid/callback`.
- `ADMIN_ORCIDS`: comma-separated ORCID iDs allowed to resolve or decline suggestions.

Comments and users are stored in SQLite (`data/app.db`, created automatically).

## Writing lessons

```
content/areas.yaml               # research areas (name, colour)
content/tracks.yaml              # learning tracks (ordered core courses)
content/<course>/_course.yaml    # one course: title, area, level, prerequisites, objectives, ordered lessons
content/<course>/<slug>.md       # one lesson
```

A course with no lessons (or `status: planned`) appears on the map as "coming soon". Example `_course.yaml`:

```yaml
title: Models of computation
area: computability
level: Introductory
prerequisites: []             # other course ids
summary: One sentence for cards.
description: A paragraph for the course page.
objectives: [Write and trace small Turing machines, …]
lessons: [what-is-an-algorithm, turing-machines, …]
```

A lesson starts with frontmatter:

```yaml
---
title: Kleene's fixed point theorem
summary: One-line description shown in lists.
duration: 20                              # minutes
prerequisites: [universal-program-smn]    # slugs in the same course, or "course/slug"
---
```

The body is Markdown with `$…$` / `$$…$$` math. The book's macros work as-is (`\nat`, `\converge`, `\diverge`, `\cs`, `\bstr`, `\uh`, `\RCA`, …); add more in `src/lib/katex-macros.ts`.

### Statements and proofs

```md
:::theorem[SMN theorem]{#thm-smn}
For all $m, n$ there is a total computable function …
:::

:::proof{of=thm-smn}
…
:::
```

Numbered kinds: `definition`, `theorem`, `lemma`, `proposition`, `corollary`, `fact`, `example`, `remark`, `notation`, `exercise`, `question`, `conjecture`.
Others: `proof`, `solution` and `hint` (collapsed), `aside`, `figure` (the `[label]` becomes the caption).
Exercises take `{difficulty=1}` to `3`. To nest a solution inside an exercise, give the outer block one more colon:

```md
::::exercise{difficulty=2}
Show that …

:::solution
…
:::
::::
```

### Cross-references

`:ref{#thm-smn}` links to any labelled block, **in any lesson**. In the same lesson it reads "Theorem 2"; in another lesson it shows the block's title. `:ref[custom text]{#thm-smn}` overrides the text, and `:ref{to="fundamentals/fixed-point"}` links to a lesson.

### Check-up questions

Place a `:::quiz` block just after the proof it tests. Options use task-list syntax, `[x]` marks the correct ones (several `[x]` means "select all that apply"). Indented paragraphs under an option are its explanation; paragraphs after the list are shown once the question is solved. Separate several questions with `---`.

```md
:::quiz
Why is $\Phi_a$ a total function?

- [x] Computing $\Phi_a(n)$ only produces a code; it never runs $\Phi_n(n)$.

  Divergence is pushed inside the program whose code is returned.
- [ ] Because $f$ is total.

  Totality of $f$ plays no role here.

---

Second question …
:::
```

### Checking content

```bash
npm run check-content                              # all lessons: broken refs, malformed quizzes, missing files
npm run check-content -- computability/fixed-point # also prints the rendered HTML
```

In development, the same warnings are shown at the top of the lesson page.

## Versions and citations

The working copy of a course may change at any time. To publish a citable version:

```bash
npm run release -- models-of-computation 1.0 "First complete version"
```

This copies the course to `content/_versions/models-of-computation/1.0/` and records it in `versions.yaml`. Released versions are **immutable**: never edit them, release a new version instead. Each lesson of a release has a permanent URL, `/courses/<course>/v/<version>/<lesson>`, and each labelled statement a permanent anchor (`#thm-...`). Archived pages show a banner linking to the current version and do not accept remarks. The **Cite** button of a lesson gives its permanent link and a BibTeX entry (add `authors: [...]` to `_course.yaml` to include authors).

## Tests

```bash
npm test          # unit tests (Vitest)
npm run verify    # type-check + unit tests + content check — run before every commit
```

`tests/` covers the content pipeline (on the miniature content tree in `tests/fixtures/content`), versions and citations, KaTeX macros, the anchoring of remarks (in a simulated browser), authentication helpers, the comment database and the ORCID token exchange. `tests/content-integrity.test.ts` renders every real lesson and fails on broken references, malformed quizzes or formulas KaTeX cannot typeset. A GitHub Actions workflow (`.github/workflows/ci.yml`) runs the same checks.

## Guidelines

`AGENTS.md` (included by `CLAUDE.md`) records the principles of the project — tone, level of detail, typography, versioning, testing — for human contributors and AI assistants.

## How suggestions stay attached to the text

A suggestion stores the selected text plus ~32 characters of context on each side and its approximate position (as in the W3C Web Annotation "text quote selector"). On load, the page searches for that quote, so suggestions survive edits elsewhere in the lesson. If the quoted passage itself is removed, the suggestion is kept and marked *Detached*; if the lesson changed since it was written, it is marked *Earlier version*. Selections always cover whole formulas, and quotes are shown with their LaTeX source re-typeset.

## Code map

| Path | What |
| --- | --- |
| `src/lib/content.ts` | Catalog loading, Markdown → HTML pipeline, numbering, references, quiz extraction |
| `src/lib/katex-macros.ts` | Book macros for KaTeX |
| `src/lib/db.ts`, `comments.ts`, `auth.ts`, `orcid.ts` | SQLite schema, comments, sessions, ORCID OAuth |
| `src/app/api/…` | Sign-in/out and comments API (development server) |
| `deploy/api/` | The same API in PHP, for the live site |
| `scripts/build-static.ts`, `scripts/deploy.ts` | Static export and deployment: [docs/DEPLOY.md](docs/DEPLOY.md) |
| `src/components/LessonView.tsx`, `CommentsPanel.tsx`, `anchoring.ts` | Selection, highlights, suggestion threads |
| `src/components/Quiz.tsx`, `progress.ts` | Check-up questions; progress kept in the browser |

## Deployment

The live site is a static export served by PHP web hosting, with a PHP version of the remarks API. `npm run deploy` builds it and uploads what changed over SFTP; see [docs/DEPLOY.md](docs/DEPLOY.md).

## Next steps

- Free-form answers checked by an AI model (the quiz block format is designed to gain new question types, e.g. `:::question{type=open}`).
- Save quiz progress server-side for signed-in readers.
- A LaTeX → lesson converter for the remaining chapters (TikZ figures need converting to SVG).
- Move from SQLite to Postgres when hosting on a platform without a persistent disk.
