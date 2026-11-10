"use client";

import { useEffect, useState } from "react";
import { bibtexEntry, type CitationData } from "@/lib/citation";

/** "Cite" button: permanent link and BibTeX entry for the lesson. */
export function CitePanel({ data }: { data: CitationData }) {
  const [origin, setOrigin] = useState("");
  const [copied, setCopied] = useState<string | null>(null);
  useEffect(() => setOrigin(window.location.origin), []);

  const url = origin + data.path;
  const bib = bibtexEntry({ ...data, url });

  async function copy(what: string, value: string) {
    try {
      await navigator.clipboard.writeText(value);
      setCopied(what);
      setTimeout(() => setCopied(null), 1500);
    } catch {}
  }

  return (
    <details className="cite">
      <summary className="btn btn-small">Cite</summary>
      <div className="cite-panel">
        {data.version ? (
          <p className="small">
            Permanent link to <strong>version {data.version}</strong>
            {data.date ? ` (${data.date})` : ""}. The text at this address will not change.
          </p>
        ) : (
          <p className="small">
            This course has no released version yet: the text at this address may change. Cite a released version when one exists.
          </p>
        )}
        <div className="cite-row">
          <code>{url}</code>
          <button className="btn btn-small" onClick={() => copy("url", url)}>
            {copied === "url" ? "Copied" : "Copy"}
          </button>
        </div>
        <div className="cite-row cite-bib">
          <pre>{bib}</pre>
          <button className="btn btn-small" onClick={() => copy("bib", bib)}>
            {copied === "bib" ? "Copied" : "Copy BibTeX"}
          </button>
        </div>
        <p className="small muted">To cite a single statement, use the # link that appears next to its heading.</p>
      </div>
    </details>
  );
}
