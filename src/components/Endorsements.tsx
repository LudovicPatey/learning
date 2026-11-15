"use client";

// Endorsements of exercises: a signed-in reader states that they have checked the
// exercise and its solution (as on the RM Zoo). Shown in the head of each exercise
// of a lesson and in the exercise catalogue.

import { useCallback, useEffect, useRef, useState } from "react";
import type { EndorsementDTO } from "@/lib/comment-types";

type Me = { orcid: string; name: string; isAdmin: boolean };

export type EndorsementState = {
  loaded: boolean;
  me: Me | null;
  /** Endorsements grouped by exercise label. */
  byExercise: Map<string, EndorsementDTO[]>;
  /** Endorse (true) or withdraw (false); resolves to an error message, or null. */
  toggle: (exercise: string, endorse: boolean) => Promise<string | null>;
};

function group(list: EndorsementDTO[]): Map<string, EndorsementDTO[]> {
  const m = new Map<string, EndorsementDTO[]>();
  for (const e of list) m.set(e.exercise, [...(m.get(e.exercise) ?? []), e]);
  return m;
}

/** Loads all endorsements once (the list is small: one entry per person and exercise). */
export function useEndorsements(enabled = true): EndorsementState {
  const [loaded, setLoaded] = useState(false);
  const [me, setMe] = useState<Me | null>(null);
  const [byExercise, setByExercise] = useState<Map<string, EndorsementDTO[]>>(new Map());

  useEffect(() => {
    if (!enabled) return;
    fetch("/api/endorsements")
      .then((r) => (r.ok ? r.json() : { endorsements: [], me: null }))
      .then((d) => {
        setByExercise(group(d.endorsements ?? []));
        setMe(d.me ?? null);
      })
      .catch(() => {})
      .finally(() => setLoaded(true));
  }, [enabled]);

  const toggle = useCallback(async (exercise: string, endorse: boolean) => {
    try {
      const r = await fetch("/api/endorsements", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ exercise, endorse }),
      });
      const d = await r.json();
      if (!r.ok) return String(d.error ?? "The endorsement could not be saved.");
      setByExercise(group(d.endorsements ?? []));
      return null;
    } catch {
      return "The endorsement could not be saved.";
    }
  }, []);

  return { loaded, me, byExercise, toggle };
}

/**
 * The endorsement mark of one exercise: a check mark with the number of endorsers, which
 * opens the list of endorsers and the button to endorse or withdraw.
 */
export function EndorseControl({
  exercise,
  currentHash,
  state,
}: {
  exercise: string;
  /** Hash of the current text of the exercise: endorsements of another text are marked. */
  currentHash?: string;
  state: EndorsementState;
}) {
  const [open, setOpen] = useState(false);
  const [pos, setPos] = useState<{ left: number; top: number; width: number } | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const ref = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    if (!open) return;
    const close = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    const esc = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    // close when the page scrolls away from the mark (small scrolls, such as the one
    // bringing the mark into view, keep it open)
    const y0 = window.scrollY;
    const hide = () => {
      if (Math.abs(window.scrollY - y0) > 40) setOpen(false);
    };
    document.addEventListener("mousedown", close);
    document.addEventListener("keydown", esc);
    window.addEventListener("scroll", hide, { passive: true });
    const resize = () => setOpen(false);
    window.addEventListener("resize", resize);
    return () => {
      document.removeEventListener("mousedown", close);
      document.removeEventListener("keydown", esc);
      window.removeEventListener("scroll", hide);
      window.removeEventListener("resize", resize);
    };
  }, [open]);

  // The popover is placed in the viewport, below the mark, without overflowing the window.
  function toggleOpen(button: HTMLElement) {
    if (open) return setOpen(false);
    const r = button.getBoundingClientRect();
    const width = Math.min(340, window.innerWidth - 16);
    setPos({ left: Math.max(8, Math.min(r.left, window.innerWidth - width - 8)), top: r.bottom + 6, width });
    setOpen(true);
  }

  const list = state.byExercise.get(exercise) ?? [];
  const mine = state.me ? list.find((e) => e.author.orcid === state.me!.orcid) : undefined;
  const outdated = (e: EndorsementDTO) => Boolean(currentHash && e.contentHash && e.contentHash !== currentHash);
  const current = list.filter((e) => !outdated(e)).length;
  const cls = current === 0 ? "none" : current === 1 ? "one" : "several";
  const label =
    list.length === 0
      ? "Not endorsed yet"
      : `Checked by ${list.length} ${list.length === 1 ? "reader" : "readers"}${current < list.length ? ` (${list.length - current} on an earlier version)` : ""}`;

  async function act(endorse: boolean) {
    setBusy(true);
    setError(await state.toggle(exercise, endorse));
    setBusy(false);
  }

  return (
    <span className="endorse" ref={ref}>
      <button
        type="button"
        className={`endorse-mark endorse-${cls}${mine ? " endorse-mine" : ""}`}
        aria-expanded={open}
        aria-label={`${label}. Show the endorsements`}
        title={label}
        onClick={(e) => toggleOpen(e.currentTarget)}
      >
        ✓{list.length > 0 && <span className="endorse-count">{list.length}</span>}
      </button>
      {open && pos && (
        <span className="endorse-pop" role="dialog" aria-label="Endorsements of this exercise" style={pos}>
          <span className="endorse-pop-head">Endorsements</span>
          <span className="endorse-pop-text">An endorsement states that the reader has checked the exercise and its solution.</span>
          {list.length > 0 ? (
            <span className="endorse-list">
              {list.map((e) => (
                <span key={e.author.orcid} className="endorse-person">
                  <a href={`https://orcid.org/${e.author.orcid}`} target="_blank" rel="noreferrer">
                    {e.author.name}
                  </a>
                  <span className="muted small"> · {e.createdAt.slice(0, 10)}</span>
                  {outdated(e) && <span className="endorse-old"> · earlier version</span>}
                </span>
              ))}
            </span>
          ) : (
            <span className="muted small">No endorsement yet.</span>
          )}
          {!state.loaded ? null : state.me ? (
            mine && !outdated(mine) ? (
              <button type="button" className="btn btn-small" disabled={busy} onClick={() => act(false)}>
                Withdraw my endorsement
              </button>
            ) : (
              <button type="button" className="btn btn-small btn-primary" disabled={busy} onClick={() => act(true)}>
                {mine ? "I have checked the new version" : "I have checked this exercise and its solution"}
              </button>
            )
          ) : (
            <a className="btn btn-small" href={`/api/auth/orcid/login?returnTo=${encodeURIComponent(currentPath(exercise))}`}>
              Sign in with ORCID to endorse
            </a>
          )}
          {error && <span className="endorse-error">{error}</span>}
        </span>
      )}
    </span>
  );
}

function currentPath(exercise: string): string {
  if (typeof window === "undefined") return "/";
  const { pathname, search } = window.location;
  return pathname.startsWith("/courses/") ? `${pathname}${search}#${exercise}` : `${pathname}${search}`;
}
