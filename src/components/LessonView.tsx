"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { createPortal } from "react-dom";
import type { RefPreview, Segment } from "@/lib/content";
import type { Anchor, CommentDTO, CommentKind } from "@/lib/comment-types";
import { Quiz } from "./Quiz";
import { anchorToRange, buildIndex, caretAt, rangeToAnchor, selectionInside } from "./anchoring";
import { CommentsPanel, type Draft, type Me } from "./CommentsPanel";

const HL_ALL = "cl-comment";
const HL_ACTIVE = "cl-comment-active";

function setHighlights(ranges: Range[], active: Range | null) {
  if (typeof CSS === "undefined" || !("highlights" in CSS)) return;
  CSS.highlights.set(HL_ALL, new Highlight(...ranges));
  if (active) CSS.highlights.set(HL_ACTIVE, new Highlight(active));
  else CSS.highlights.delete(HL_ACTIVE);
}

export function LessonView({
  lessonId,
  contentHash,
  segments,
  refPreviews = {},
  readOnly = false,
}: {
  lessonId: string;
  contentHash: string;
  segments: Segment[];
  refPreviews?: Record<string, RefPreview>;
  /** Archived versions are read-only: no comments. */
  readOnly?: boolean;
}) {
  const articleRef = useRef<HTMLElement>(null);
  const wrapRef = useRef<HTMLDivElement>(null);
  const draftKey = `cl:draft:${lessonId}`;

  const [me, setMe] = useState<Me | null>(null);
  const [threads, setThreads] = useState<CommentDTO[]>([]);
  const [loaded, setLoaded] = useState(false);
  const [ranges, setRanges] = useState<Map<number, Range | null>>(new Map());
  const [activeId, setActiveId] = useState<number | null>(null);
  const [draft, setDraft] = useState<Draft | null>(null);
  const [selButton, setSelButton] = useState<{ x: number; y: number } | null>(null);
  const [panelOpen, setPanelOpen] = useState(false);
  const [showResolved, setShowResolved] = useState(false);
  const [domVersion, setDomVersion] = useState(0);
  const [slot, setSlot] = useState<HTMLElement | null>(null);
  const [preview, setPreview] = useState<{ id: string; x: number; y: number } | null>(null);
  const hideTimer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);

  useEffect(() => setSlot(document.getElementById("comments-slot")), []);

  // Load comments + restore an unsent draft (e.g. after signing in).
  useEffect(() => {
    if (readOnly) return;
    fetch(`/api/comments?lesson=${encodeURIComponent(lessonId)}`)
      .then((r) => r.json())
      .then((d) => {
        setThreads(d.threads ?? []);
        setMe(d.me ?? null);
      })
      .finally(() => setLoaded(true));
    try {
      const saved = sessionStorage.getItem(draftKey);
      if (saved) {
        setDraft(JSON.parse(saved));
        setPanelOpen(true);
      }
    } catch {}
  }, [lessonId, draftKey, readOnly]);

  useEffect(() => {
    try {
      if (draft) sessionStorage.setItem(draftKey, JSON.stringify(draft));
      else sessionStorage.removeItem(draftKey);
    } catch {}
  }, [draft, draftKey]);

  // Re-anchor when the comments or the article DOM change (quizzes re-render parts of it).
  useEffect(() => {
    const el = articleRef.current;
    if (!el) return;
    let t: ReturnType<typeof setTimeout>;
    const obs = new MutationObserver(() => {
      clearTimeout(t);
      t = setTimeout(() => setDomVersion((v) => v + 1), 150);
    });
    obs.observe(el, { childList: true, subtree: true, characterData: true });
    return () => {
      obs.disconnect();
      clearTimeout(t);
    };
  }, []);

  useEffect(() => {
    const el = articleRef.current;
    if (!el) return;
    const idx = buildIndex(el);
    const m = new Map<number, Range | null>();
    for (const th of threads) m.set(th.id, th.anchor ? anchorToRange(idx, th.anchor) : null);
    setRanges(m);
  }, [threads, domVersion]);

  const visibleThreads = useMemo(() => threads.filter((t) => showResolved || t.status === "open"), [threads, showResolved]);

  useEffect(() => {
    const all = visibleThreads.map((t) => ranges.get(t.id)).filter(Boolean) as Range[];
    const draftRange = draft?.anchor && articleRef.current ? anchorToRange(buildIndex(articleRef.current), draft.anchor) : null;
    setHighlights(all, (activeId != null ? ranges.get(activeId) : null) ?? draftRange ?? null);
  }, [visibleThreads, ranges, activeId, draft]);

  useEffect(() => () => setHighlights([], null), []);

  // Floating "comment" button next to a text selection.
  useEffect(() => {
    if (readOnly) return;
    const update = () => {
      const el = articleRef.current;
      const wrap = wrapRef.current;
      if (!el || !wrap) return;
      const r = selectionInside(el);
      if (!r) return setSelButton(null);
      const rect = r.getBoundingClientRect();
      const base = wrap.getBoundingClientRect();
      setSelButton({ x: Math.min(rect.right, base.right) - base.left, y: rect.top - base.top });
    };
    const later = () => setTimeout(update, 0);
    const onSelChange = () => {
      if (window.getSelection()?.isCollapsed) setSelButton(null);
    };
    document.addEventListener("mouseup", later);
    document.addEventListener("keyup", later);
    document.addEventListener("touchend", later);
    document.addEventListener("selectionchange", onSelChange);
    return () => {
      document.removeEventListener("mouseup", later);
      document.removeEventListener("keyup", later);
      document.removeEventListener("touchend", later);
      document.removeEventListener("selectionchange", onSelChange);
    };
  }, [readOnly]);

  function startComment() {
    const el = articleRef.current;
    const r = el && selectionInside(el);
    if (!el || !r) return;
    const anchor = rangeToAnchor(el, r);
    if (!anchor) return;
    setDraft({ anchor, body: draft?.body ?? "", kind: draft?.kind ?? "suggestion" });
    setActiveId(null);
    setPanelOpen(true);
    setSelButton(null);
    window.getSelection()?.removeAllRanges();
  }

  const focusThread = useCallback(
    (id: number, scrollText: boolean) => {
      setActiveId(id);
      setPanelOpen(true);
      if (scrollText) {
        const r = ranges.get(id);
        if (r) {
          const rect = r.getBoundingClientRect();
          window.scrollTo({ top: window.scrollY + rect.top - window.innerHeight / 3, behavior: "smooth" });
        }
      } else {
        requestAnimationFrame(() => document.getElementById(`thread-${id}`)?.scrollIntoView({ block: "nearest", behavior: "smooth" }));
      }
    },
    [ranges],
  );

  // Hovering (or focusing) a cross-reference shows the referenced statement.
  function showPreview(target: EventTarget | null) {
    const a = (target as HTMLElement | null)?.closest?.("a.ref") as HTMLAnchorElement | null;
    const wrap = wrapRef.current;
    if (!a || !wrap) return;
    const id = decodeURIComponent(a.hash.slice(1));
    if (!refPreviews[id]) return;
    clearTimeout(hideTimer.current);
    const r = a.getBoundingClientRect();
    const base = wrap.getBoundingClientRect();
    const width = Math.min(460, window.innerWidth - 32);
    const x = Math.max(0, Math.min(r.left - base.left, base.width - width));
    setPreview({ id, x, y: r.bottom - base.top + 8 });
  }
  function hidePreviewSoon() {
    clearTimeout(hideTimer.current);
    hideTimer.current = setTimeout(() => setPreview(null), 220);
  }

  // Clicking highlighted text opens its thread.
  function onArticleClick(e: React.MouseEvent) {
    if (!window.getSelection()?.isCollapsed) return;
    if ((e.target as HTMLElement).closest("a, button, input, label, summary")) return;
    const p = caretAt(e.clientX, e.clientY);
    if (!p) return;
    const hit = visibleThreads.find((t) => {
      const r = ranges.get(t.id);
      try {
        return r?.isPointInRange(p.node, p.offset);
      } catch {
        return false;
      }
    });
    if (hit) focusThread(hit.id, false);
    else setActiveId(null);
  }

  // Sort threads in reading order; detached ones last.
  const ordered = useMemo(() => {
    return [...visibleThreads].sort((a, b) => {
      const ra = ranges.get(a.id);
      const rb = ranges.get(b.id);
      if (ra && rb) return ra.compareBoundaryPoints(Range.START_TO_START, rb);
      if (ra) return -1;
      if (rb) return 1;
      return a.id - b.id;
    });
  }, [visibleThreads, ranges]);

  const openCount = threads.filter((t) => t.status === "open").length;

  return (
    <div className="lesson-wrap" ref={wrapRef}>
      <article
        className="lesson-body"
        ref={articleRef}
        onClick={onArticleClick}
        onMouseOver={(e) => showPreview(e.target)}
        onMouseOut={(e) => {
          if ((e.target as HTMLElement).closest?.("a.ref")) hidePreviewSoon();
        }}
        onFocus={(e) => showPreview(e.target)}
        onBlur={hidePreviewSoon}
      >
        {segments.map((s, i) =>
          s.type === "html" ? (
            <div key={i} className="segment" dangerouslySetInnerHTML={{ __html: s.html }} />
          ) : (
            <Quiz key={i} quiz={s.quiz} lessonId={lessonId} />
          ),
        )}
      </article>

      {preview && refPreviews[preview.id] && (
        <div
          className="ref-preview no-annotate"
          role="tooltip"
          style={{ left: preview.x, top: preview.y }}
          onMouseEnter={() => clearTimeout(hideTimer.current)}
          onMouseLeave={hidePreviewSoon}
        >
          {refPreviews[preview.id].lessonId !== lessonId && (
            <div className="ref-preview-from">
              From <a href={refPreviews[preview.id].href}>{refPreviews[preview.id].lessonTitle}</a> ·{" "}
              {refPreviews[preview.id].courseTitle}
            </div>
          )}
          <div dangerouslySetInnerHTML={{ __html: refPreviews[preview.id].html }} />
        </div>
      )}

      {selButton && (
        <button
          className="sel-comment-btn no-annotate"
          style={{ left: selButton.x, top: selButton.y }}
          onMouseDown={(e) => e.preventDefault()}
          onClick={startComment}
          title="Comment on the selected passage"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" aria-hidden>
            <path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z" />
          </svg>
          Comment
        </button>
      )}

      {!readOnly && (
      <button className="panel-toggle no-annotate" onClick={() => setPanelOpen((o) => !o)} aria-expanded={panelOpen}>
        Remarks{openCount ? ` (${openCount})` : ""}
      </button>
      )}

      {slot && !readOnly && createPortal(
      <CommentsPanel
        open={panelOpen}
        onClose={() => setPanelOpen(false)}
        lessonId={lessonId}
        contentHash={contentHash}
        me={me}
        loaded={loaded}
        threads={ordered}
        anchored={(id) => Boolean(ranges.get(id))}
        activeId={activeId}
        onFocus={(id) => focusThread(id, true)}
        draft={draft}
        setDraft={setDraft}
        showResolved={showResolved}
        setShowResolved={setShowResolved}
        onCreated={(c) => {
          setThreads((t) => [...t, c]);
          setDraft(null);
          setActiveId(c.id);
        }}
        onChanged={(c) =>
          setThreads((ts) =>
            ts.map((t) => (t.id === c.id ? { ...c, replies: t.replies } : { ...t, replies: t.replies.map((r) => (r.id === c.id ? c : r)) })),
          )
        }
        onReplied={(parentId, c) => setThreads((ts) => ts.map((t) => (t.id === parentId ? { ...t, replies: [...t.replies, c] } : t)))}
        onDeleted={(id) =>
          setThreads((ts) => ts.filter((t) => t.id !== id).map((t) => ({ ...t, replies: t.replies.filter((r) => r.id !== id) })))
        }
      />,
      slot)}
    </div>
  );
}

export type { Anchor, CommentKind };
