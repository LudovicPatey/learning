"use client";

import { useEffect, useState } from "react";

/** The current lesson's sections, highlighting the one being read. */
export function SectionNav({ headings }: { headings: { id: string; text: string }[] }) {
  const [active, setActive] = useState<string | null>(null);
  useEffect(() => {
    const els = headings.map((h) => document.getElementById(h.id)).filter(Boolean) as HTMLElement[];
    if (!els.length) return;
    const onScroll = () => {
      let cur: string | null = null;
      for (const el of els) if (el.getBoundingClientRect().top < 140) cur = el.id;
      setActive(cur);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, [headings]);
  if (!headings.length) return null;
  return (
    <ol className="toc-sections">
      {headings.map((h) => (
        <li key={h.id}>
          <a href={`#${h.id}`} className={active === h.id ? "is-active" : ""}>
            {h.text}
          </a>
        </li>
      ))}
    </ol>
  );
}
