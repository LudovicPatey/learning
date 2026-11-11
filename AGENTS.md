# Guidelines for contributors and AI assistants

This file is the memory of the project. Read it fully before changing anything, and keep it up to date when a decision changes. `CLAUDE.md` includes it.

## What this project is

**Computability Theory** is an online platform of course notes for **master's students who will do research in mathematical logic**: computability theory first, then algorithmic randomness, reverse mathematics and higher computability. It is a long-term project. Reliability, maintainability and the quality of the mathematics matter more than features.

The book sources in `external-data/` (Monin & Patey, *Computability theory*) set the expected level of precision. Courses are new texts, not transcriptions of the book.

## Non-negotiable principles

### Tone and content

- **Register: lecture notes.** Sober, precise, scientific. No marketing phrasing, no exclamation marks, no rhetorical questions, no jokes, no hype adjectives ("powerful", "amazing", "remarkably"). Summaries state what the lesson contains ("Non-trivial index sets are not computable."), they do not sell it.
- **Level of detail: a graduate course.** Full definitions with all conventions made explicit (input/output conventions, partiality), complete proofs, worked examples verified in detail, exercises with solutions. A course may take several hours.
- **Mathematical correctness first.** Every statement, proof, quiz answer and explanation must be checked. When a result is admitted without proof, say so explicitly and give a reference.
- **American spelling** (formalize, behavior), en dashes for ranges (1931–1936), em dashes without surrounding hyphens.
- **Small courses, small lessons.** A course is a short series of lessons on one topic; a lesson treats one notion or theorem (25–45 minutes of reading for the detailed courses). Prerequisites are explicit, at both levels.
- **Tracks and specialized courses.** `content/tracks.yaml` lists the main learning tracks, each an ordered sequence of core courses in one area. The home page shows one dependency graph per track, with only the edges inside the track; prerequisites on other tracks are shown as "Builds on". A course in no track is a **specialized course**: it appears in the searchable catalogue (`/courses`) and on course pages, never in the graphs. Keep tracks short enough to be readable; add new advanced topics as specialized courses unless they belong to a main sequence.

### Comprehension questions (quizzes)

- They are **collapsed by default** and must never interrupt the reading flow. Place a `:::quiz[title]` block right after the proof it tests.
- Questions target **one step of an argument** (where a hypothesis is used, why a function is total), not recall. Every option, right or wrong, has a justification. A wrong option without an indented explanation is reported by `npm run check-content`; a correct option may carry its justification in its own text.

### Typography (book quality)

- Sans-serif reading font (Inter), **justified and hyphenated** text, measure of about 70 characters.
- Statements in the style of `amsthm`: run-in bold head, italic statement for theorem-like environments, upright for definitions; proofs visually attached to their statement and ending with ∎.
- Numbering is per lesson: "Theorem 7.4" is the 4th numbered statement of lesson 7; sections are "7.2". It is computed automatically: never write numbers by hand, use `:ref{#label}`.
- Tables in booktabs style. Figures are inline SVG using the `fig-*` classes so that they work in light and dark mode.
- **A single KaTeX version.** The HTML is generated server-side by `rehype-katex` and styled by `katex/dist/katex.min.css`; both must come from the same `katex` package (`npm ls katex` must show one version). A mismatch produces misplaced accents and oversized subscripts.

### Versions and citations

- The working copy of a course (`content/<course>/`) may change at any time.
- A **release** freezes it: `npm run release -- <course> <version> "<notes>"` copies it to `content/_versions/<course>/<version>/` and records it in `versions.yaml`.
- **Released versions are immutable.** Never edit files under `content/_versions/`. To fix an error, make a new release. Permanent URLs: `/courses/<course>/v/<version>/<lesson>#<label>`.
- Labels (`{#thm-...}`) are part of the public interface: renaming or deleting a label breaks citations of future versions; keep them stable.

### Engineering

- **Every change comes with tests.** Run `npm run verify` (type-check, unit tests, content check) before considering a task done. New library code gets unit tests in `tests/`; bugs get a regression test.
- Keep library code (`src/lib/`) free of React and framework code where possible, so it stays testable.
- Do not add dependencies without need. Pin exact behavior-sensitive packages (KaTeX).
- The live site is a static export served by PHP hosting (`docs/DEPLOY.md`): pages must not use request-time data, and every change to the API (`src/app/api/`) must be made to its PHP version (`deploy/api/`) as well.
- Security: user-written text is rendered only through `renderMathText` (escapes HTML, KaTeX with `trust: false`). Lesson content is trusted (it comes from the repository). Mutating API routes check `sameOrigin` and the session.

## Architecture

| Path | Role |
| --- | --- |
| `content/areas.yaml` | Research areas (title, color) |
| `content/tracks.yaml` | Main learning tracks: ordered core courses; other courses are specialized |
| `content/<course>/_course.yaml` | Course metadata: title, area, level, prerequisites, objectives, authors, ordered lessons |
| `content/<course>/<slug>.md` | One lesson: YAML frontmatter + Markdown with math and directives |
| `content/_versions/<course>/` | Released versions (immutable) and `versions.yaml` |
| `src/lib/content.ts` | Catalog loading, Markdown → HTML pipeline (remark/rehype), numbering, references, quizzes, previews |
| `src/lib/tracks.ts` | Tracks: parsing, per-track dependency graphs, catalogue search (pure, tested) |
| `src/lib/versions.ts`, `release.ts` | Versions: listing and comparing (site); creating releases (CLI only) |
| `src/lib/citation.ts` | BibTeX and citation keys |
| `src/lib/katex-macros.ts` | LaTeX macros available in lessons (from the book's preamble) |
| `src/lib/db.ts`, `auth.ts`, `orcid.ts`, `comments.ts` | SQLite storage, sessions, ORCID OAuth, reader remarks (development server) |
| `deploy/api/` | The same API in PHP, for the live site on PHP hosting; keep it in step with `src/app/api/` (`tests/php-api.test.ts`) |
| `src/lib/deploy.ts`, `scripts/build-static.ts`, `scripts/deploy.ts` | Static export and upload to the web hosting: `docs/DEPLOY.md` |
| `src/components/pages/` | Lesson and course pages, shared by current and released versions |
| `src/components/LessonView.tsx`, `anchoring.ts`, `CommentsPanel.tsx` | Reading view, text-anchored remarks |
| `src/app/globals.css` | All styles (design tokens at the top, light and dark) |
| `tests/` | Vitest unit tests; `tests/fixtures/content` is a miniature content tree |
| `scripts/` | `check-content.ts`, `release-course.ts`; `figures/` holds the generators of the inline SVG figures (edit the generator, re-run it, paste the output) |

## Writing lessons

See `README.md` for the full syntax. In short:

```md
---
title: The Ackermann function
summary: One factual sentence.
duration: 40
prerequisites: [coding-sequences]          # same course, or course/slug
---

## Section title

:::theorem[Optional name]{#thm-label}
Statement with $math$. Book macros (\nat, \converge, \Phi_e …) are available.
:::

:::proof{of=thm-label}
…
:::

:::quiz[the proof of the majorization theorem]
Question?

- [x] Correct option.

  Why it is correct.
- [ ] Wrong option.

  Why it is wrong.
:::
```

Figures: inline SVG inside `:::figure[caption]` (no blank lines inside the SVG). Use the `fig` class on `<svg>` and the classes `cell`, `head-cell`, `state`, `node`, `accent-fill`, `soft-fill`, `muted-fill`, `accent-stroke`, `ink-stroke`, `muted-stroke`, `math` (KaTeX italic font), `mrm` (KaTeX roman), `label` — never hard-coded colors — so that figures work in dark mode. Markers need unique ids per figure.

Kinds: `definition theorem lemma proposition corollary fact example remark notation exercise question conjecture` (numbered), `proof solution hint aside figure quiz`. Nest a solution in an exercise with a four-colon outer fence (`::::exercise`). Long displayed formulas must be split with `aligned` or `gathered` so they fit the measure.

## Commands

```bash
npm run dev            # development server
npm run verify         # type-check + tests + content check: run before finishing any task
npm test               # unit tests only
npm run check-content  # validates all lessons (broken references, malformed quizzes)
npm run release -- models-of-computation 1.1 "Corrections in lesson 7"
npm run build
npm run build:static          # static site for the web hosting, in out/; npm run preview:static serves it
npm run deploy -- --dry-run   # build the static site (out/) and list what would be uploaded
npm run deploy                # upload it to the web hosting (docs/DEPLOY.md)
```
