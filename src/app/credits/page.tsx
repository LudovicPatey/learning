import Link from "next/link";
import type { Metadata } from "next";
import { getCatalog, renderInlineMarkdown } from "@/lib/content";
import type { SourceKind } from "@/lib/credits";

export const metadata: Metadata = { title: "Credits" };

const KIND_TITLE: Record<SourceKind, string> = {
  book: "Books",
  monograph: "Monographs and books in preparation",
  "lecture-notes": "Lecture notes and courses",
  survey: "Surveys and tutorials",
  article: "Articles",
};
const KIND_ORDER: SourceKind[] = ["book", "monograph", "lecture-notes", "survey", "article"];

/** The works the tracks, courses and exercises are based on, with where each is used. */
export default async function CreditsPage() {
  const { courses, tracks, exercises, sources } = getCatalog();
  const uses = new Map<string, { tracks: { id: string; title: string }[]; main: { id: string; title: string }[]; consulted: { id: string; title: string }[]; exercises: number }>();
  const use = (id: string) => {
    if (!uses.has(id)) uses.set(id, { tracks: [], main: [], consulted: [], exercises: 0 });
    return uses.get(id)!;
  };
  for (const t of tracks) for (const c of t.credits) use(c.source).tracks.push({ id: t.id, title: t.title });
  for (const course of courses)
    for (const c of course.credits) use(c.source)[c.role === "main" ? "main" : "consulted"].push({ id: course.id, title: course.title });
  for (const e of exercises.values()) if (e.credit?.source) use(e.credit.source).exercises += 1;
  const original = [...exercises.values()].filter((e) => !e.credit).length;

  const entries = await Promise.all(
    [...sources.values()].map(async (s) => ({ ...s, citationHtml: await renderInlineMarkdown(s.citation), use: use(s.id) })),
  );
  const groups = KIND_ORDER.map((k) => ({
    kind: k,
    items: entries.filter((e) => e.kind === k).sort((a, b) => a.short.localeCompare(b.short)),
  })).filter((g) => g.items.length > 0);

  return (
    <div className="page credits-page">
      <div className="section-head">
        <h1 style={{ fontSize: "clamp(2rem, 4vw, 2.8rem)", margin: "8px 0 12px" }}>Credits</h1>
        <p>
          The courses are new texts, written for this site, but they are based on published works: the order of topics, many
          proofs and some exercises come from the books, lecture notes and articles below. Each track and each course lists its
          sources; each exercise states whether it comes from a published work or was written for its course. The references at the
          end of each lesson give the sources of its results, with precise locations.
        </p>
        <p className="small muted">
          {exercises.size - original} of the {exercises.size} exercises are credited to a published work: taken from it, adapted from
          it, proving one of its results, or close to one of its exercises. The {original} others were written for this site.
        </p>
      </div>

      {groups.map((g) => (
        <section key={g.kind} className="section">
          <h2>{KIND_TITLE[g.kind]}</h2>
          <ul className="credits-sources">
            {g.items.map((s) => (
              <li key={s.id} id={s.id}>
                <div className="credit-citation" dangerouslySetInnerHTML={{ __html: s.citationHtml }} />
                {s.url && (
                  <div className="small">
                    <a href={s.url}>{s.url}</a>
                  </div>
                )}
                <div className="credits-uses small">
                  {s.use.tracks.length > 0 && (
                    <div>
                      <span className="credit-role">Tracks</span>{" "}
                      {s.use.tracks.map((t, i) => (
                        <span key={t.id}>
                          {i > 0 && " · "}
                          <Link href="/tracks">{t.title}</Link>
                        </span>
                      ))}
                    </div>
                  )}
                  {s.use.main.length > 0 && (
                    <div>
                      <span className="credit-role">Main source of</span>{" "}
                      {s.use.main.map((c, i) => (
                        <span key={c.id}>
                          {i > 0 && " · "}
                          <Link href={`/courses/${c.id}`}>{c.title}</Link>
                        </span>
                      ))}
                    </div>
                  )}
                  {s.use.consulted.length > 0 && (
                    <div>
                      <span className="credit-role">Consulted for</span>{" "}
                      {s.use.consulted.map((c, i) => (
                        <span key={c.id}>
                          {i > 0 && " · "}
                          <Link href={`/courses/${c.id}`}>{c.title}</Link>
                        </span>
                      ))}
                    </div>
                  )}
                  {s.use.exercises > 0 && (
                    <div>
                      <span className="credit-role">Exercises</span> {s.use.exercises} exercise{s.use.exercises === 1 ? "" : "s"} credited to
                      this work
                    </div>
                  )}
                </div>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
