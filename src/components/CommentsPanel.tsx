"use client";

import { useMemo, useState } from "react";
import { COMMENT_KINDS, KIND_LABELS, type Anchor, type CommentDTO, type CommentKind, type CommentStatus } from "@/lib/comment-types";
import { renderMathText } from "./math-text";
import { OrcidIcon } from "./OrcidIcon";

export type Me = { id: number; orcid: string; name: string; isAdmin: boolean };
export type Draft = { anchor: Anchor; body: string; kind: CommentKind };

function signInHref() {
  if (typeof window === "undefined") return "/api/auth/orcid/login";
  return `/api/auth/orcid/login?returnTo=${encodeURIComponent(window.location.pathname + window.location.search)}`;
}

function MathText({ text, className }: { text: string; className?: string }) {
  const html = useMemo(() => renderMathText(text), [text]);
  return <div className={className} dangerouslySetInnerHTML={{ __html: html }} />;
}

function when(iso: string) {
  const d = new Date(iso);
  const diff = (Date.now() - d.getTime()) / 1000;
  if (diff < 60) return "just now";
  if (diff < 3600) return `${Math.floor(diff / 60)} min ago`;
  if (diff < 86400) return `${Math.floor(diff / 3600)} h ago`;
  return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
}

async function api(url: string, method: string, body?: unknown) {
  const res = await fetch(url, { method, headers: { "Content-Type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error ?? `Request failed (${res.status})`);
  return data;
}

function Author({ c }: { c: CommentDTO }) {
  return (
    <span className="c-author">
      <a href={`https://orcid.org/${c.author.orcid}`} target="_blank" rel="noreferrer" title={`ORCID iD ${c.author.orcid}`}>
        <OrcidIcon size={13} />
        {c.author.name}
      </a>
      <span className="c-date">· {when(c.createdAt)}</span>
    </span>
  );
}

function SignInPrompt({ text }: { text: string }) {
  return (
    <a className="btn btn-orcid" href={signInHref()}>
      <OrcidIcon size={16} /> {text}
    </a>
  );
}

function Composer({ draft, setDraft, me, lessonId, onCreated }: {
  draft: Draft;
  setDraft: (d: Draft | null) => void;
  me: Me | null;
  lessonId: string;
  onCreated: (c: CommentDTO) => void;
}) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit() {
    setBusy(true);
    setError(null);
    try {
      const { comment } = await api("/api/comments", "POST", { lessonId, body: draft.body, kind: draft.kind, anchor: draft.anchor });
      onCreated(comment);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="composer">
      <div className="composer-title">New remark</div>
      <MathText className="c-quote" text={draft.anchor.display} />
      <div className="kind-picker" role="radiogroup" aria-label="Kind of suggestion">
        {COMMENT_KINDS.map((k) => (
          <button key={k} role="radio" aria-checked={draft.kind === k} className={`chip kind-${k}`} onClick={() => setDraft({ ...draft, kind: k })}>
            {KIND_LABELS[k]}
          </button>
        ))}
      </div>
      <textarea
        value={draft.body}
        onChange={(e) => setDraft({ ...draft, body: e.target.value })}
        placeholder="Describe the issue. LaTeX is supported: $\Phi_e(x)\converge$."
        rows={5}
        autoFocus
      />
      {draft.body.includes("$") && (
        <div className="composer-preview">
          <span>Preview</span>
          <MathText text={draft.body} />
        </div>
      )}
      {error && <div className="form-error">{error}</div>}
      <div className="composer-actions">
        {me ? (
          <button className="btn btn-primary" disabled={busy || !draft.body.trim()} onClick={submit}>
            {busy ? "Sending…" : "Submit"}
          </button>
        ) : (
          <SignInPrompt text="Sign in with ORCID to submit" />
        )}
        <button className="btn btn-ghost" onClick={() => setDraft(null)}>
          Cancel
        </button>
      </div>
      {!me && <p className="muted small">Your draft is kept while you sign in.</p>}
    </div>
  );
}

function ReplyForm({ parent, lessonId, onReplied }: { parent: CommentDTO; lessonId: string; onReplied: (c: CommentDTO) => void }) {
  const [body, setBody] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  return (
    <div className="reply-form">
      <textarea value={body} onChange={(e) => setBody(e.target.value)} placeholder="Reply…" rows={2} />
      {error && <div className="form-error">{error}</div>}
      {body.trim() && (
        <button
          className="btn btn-small"
          disabled={busy}
          onClick={async () => {
            setBusy(true);
            try {
              const { comment } = await api("/api/comments", "POST", { lessonId, body, parentId: parent.id });
              onReplied(comment);
              setBody("");
              setError(null);
            } catch (e) {
              setError((e as Error).message);
            } finally {
              setBusy(false);
            }
          }}
        >
          Reply
        </button>
      )}
    </div>
  );
}

const STATUS_LABEL: Record<CommentStatus, string> = { open: "Open", resolved: "Resolved", declined: "Declined" };

function Thread(props: {
  t: CommentDTO;
  active: boolean;
  anchored: boolean;
  outdated: boolean;
  me: Me | null;
  lessonId: string;
  onFocus: () => void;
  onChanged: (c: CommentDTO) => void;
  onReplied: (c: CommentDTO) => void;
  onDeleted: (id: number) => void;
}) {
  const { t, me } = props;
  const [error, setError] = useState<string | null>(null);

  async function setStatus(status: CommentStatus) {
    try {
      props.onChanged((await api(`/api/comments/${t.id}`, "PATCH", { status })).comment);
    } catch (e) {
      setError((e as Error).message);
    }
  }
  async function remove(id: number) {
    if (!confirm("Delete this comment?")) return;
    try {
      await api(`/api/comments/${id}`, "DELETE");
      props.onDeleted(id);
    } catch (e) {
      setError((e as Error).message);
    }
  }

  return (
    <li id={`thread-${t.id}`} className={`thread ${props.active ? "is-active" : ""} status-${t.status}`}>
      <button className="thread-quote" onClick={props.onFocus} disabled={!props.anchored} title={props.anchored ? "Show in the text" : undefined}>
        <MathText className="c-quote" text={t.anchor?.display ?? ""} />
      </button>
      <div className="thread-meta">
        <span className={`chip chip-static kind-${t.kind}`}>{KIND_LABELS[t.kind]}</span>
        {t.status !== "open" && <span className="chip chip-static">{STATUS_LABEL[t.status]}</span>}
        {!props.anchored && <span className="chip chip-static chip-warn" title="The quoted passage is no longer in the lesson">Detached</span>}
        {props.anchored && props.outdated && (
          <span className="chip chip-static" title="The lesson has been edited since this comment was written">
            Earlier version
          </span>
        )}
      </div>
      <div className="comment">
        <Author c={t} />
        <MathText className="c-body" text={t.body} />
      </div>
      {t.replies.map((r) => (
        <div key={r.id} className="comment reply">
          <Author c={r} />
          <MathText className="c-body" text={r.body} />
          {(r.mine || me?.isAdmin) && (
            <button className="link-btn" onClick={() => remove(r.id)}>
              Delete
            </button>
          )}
        </div>
      ))}
      {error && <div className="form-error">{error}</div>}
      <div className="thread-actions">
        {me?.isAdmin &&
          (t.status === "open" ? (
            <>
              <button className="link-btn" onClick={() => setStatus("resolved")}>
                Mark resolved
              </button>
              <button className="link-btn" onClick={() => setStatus("declined")}>
                Decline
              </button>
            </>
          ) : (
            <button className="link-btn" onClick={() => setStatus("open")}>
              Reopen
            </button>
          ))}
        {(t.mine || me?.isAdmin) && (
          <button className="link-btn danger" onClick={() => remove(t.id)}>
            Delete
          </button>
        )}
      </div>
      {props.active && me && <ReplyForm parent={t} lessonId={props.lessonId} onReplied={props.onReplied} />}
    </li>
  );
}

export function CommentsPanel(props: {
  open: boolean;
  onClose: () => void;
  lessonId: string;
  contentHash: string;
  me: Me | null;
  loaded: boolean;
  threads: CommentDTO[];
  anchored: (id: number) => boolean;
  activeId: number | null;
  onFocus: (id: number) => void;
  draft: Draft | null;
  setDraft: (d: Draft | null) => void;
  showResolved: boolean;
  setShowResolved: (v: boolean) => void;
  onCreated: (c: CommentDTO) => void;
  onChanged: (c: CommentDTO) => void;
  onReplied: (parentId: number, c: CommentDTO) => void;
  onDeleted: (id: number) => void;
}) {
  const { me } = props;
  return (
    <aside className={`comments-panel no-annotate ${props.open ? "is-open" : ""}`} aria-label="Remarks">
      <div className="panel-head">
        <h2>Remarks</h2>
        <label className="small">
          <input type="checkbox" checked={props.showResolved} onChange={(e) => props.setShowResolved(e.target.checked)} /> show closed
        </label>
        <button className="panel-close" onClick={props.onClose} aria-label="Close">
          ×
        </button>
      </div>

      {props.draft ? (
        <Composer draft={props.draft} setDraft={props.setDraft} me={me} lessonId={props.lessonId} onCreated={props.onCreated} />
      ) : (
        <p className="panel-help">
          To report an error or suggest an improvement, select the passage in the text and click <em>Comment</em>. Remarks are
          signed with an ORCID iD.
        </p>
      )}

      {!props.loaded ? (
        <p className="muted small">Loading…</p>
      ) : props.threads.length === 0 ? (
        <p className="muted small">{props.showResolved ? "No remarks." : "No open remarks."}</p>
      ) : (
        <ul className="threads">
          {props.threads.map((t) => (
            <Thread
              key={t.id}
              t={t}
              me={me}
              lessonId={props.lessonId}
              active={props.activeId === t.id}
              anchored={props.anchored(t.id)}
              outdated={Boolean(t.contentHash && t.contentHash !== props.contentHash)}
              onFocus={() => props.onFocus(t.id)}
              onChanged={props.onChanged}
              onReplied={(c) => props.onReplied(t.id, c)}
              onDeleted={props.onDeleted}
            />
          ))}
        </ul>
      )}
    </aside>
  );
}
