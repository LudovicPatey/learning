"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { KIND_LABELS, type ActivityDTO, type CommentDTO, type EndorsementDTO } from "@/lib/comment-types";
import { renderMathText } from "./math-text";
import { OrcidIcon } from "./OrcidIcon";

export type AccountRefs = {
  lessons: Record<string, { title: string; course: string; href: string }>;
  exercises: Record<string, { number: string; title?: string; lesson: string; hash: string }>;
};

type Me = { orcid: string; name: string; isAdmin: boolean };

const STATUS: Record<string, string> = { open: "Open", resolved: "Resolved", declined: "Declined" };

export function AccountView({ refs }: { refs: AccountRefs }) {
  const [me, setMe] = useState<Me | null | undefined>(undefined);
  const [activity, setActivity] = useState<ActivityDTO | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/auth/me")
      .then((r) => r.json())
      .then((d) => {
        setMe(d.user ?? null);
        if (!d.user) return;
        return fetch("/api/me/activity")
          .then((r) => (r.ok ? r.json() : Promise.reject()))
          .then(setActivity);
      })
      .catch(() => setError("Your remarks and endorsements could not be loaded."));
  }, []);

  if (me === undefined && !error) return <p className="muted">Loading…</p>;
  if (error) return <p className="catalog-empty">{error}</p>;
  if (!me) {
    return (
      <div className="account-signin">
        <p>Sign in with ORCID to see your remarks and endorsements.</p>
        <a className="btn btn-orcid" href="/api/auth/orcid/login?returnTo=%2Faccount%2F">
          <OrcidIcon size={16} /> Sign in with ORCID
        </a>
      </div>
    );
  }
  if (!activity) return <p className="muted">Loading…</p>;

  const threads = activity.comments.filter((c) => c.parentId == null);
  const replies = activity.comments.filter((c) => c.parentId != null);

  return (
    <div className="account">
      <p className="account-who">
        Signed in as{" "}
        <a href={`https://orcid.org/${me.orcid}`} target="_blank" rel="noreferrer">
          <OrcidIcon size={14} /> {me.name}
        </a>{" "}
        <span className="muted">({me.orcid})</span>
      </p>

      <section className="section">
        <div className="section-head">
          <h2>Endorsed exercises ({activity.endorsements.length})</h2>
        </div>
        {activity.endorsements.length === 0 ? (
          <p className="muted">
            You have not endorsed any exercise. The <Link href="/exercises">exercise catalogue</Link> lists them all.
          </p>
        ) : (
          <ul className="account-list">
            {activity.endorsements.map((e) => (
              <EndorsementItem key={e.exercise} e={e} refs={refs} />
            ))}
          </ul>
        )}
      </section>

      <section className="section">
        <div className="section-head">
          <h2>Remarks ({threads.length})</h2>
        </div>
        {threads.length === 0 ? (
          <p className="muted">You have not written any remark. To write one, select a passage in a lesson.</p>
        ) : (
          <ul className="account-list">
            {threads.map((c) => (
              <CommentItem key={c.id} c={c} refs={refs} />
            ))}
          </ul>
        )}
      </section>

      {replies.length > 0 && (
        <section className="section">
          <div className="section-head">
            <h2>Replies ({replies.length})</h2>
          </div>
          <ul className="account-list">
            {replies.map((c) => (
              <CommentItem key={c.id} c={c} refs={refs} />
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}

function EndorsementItem({ e, refs }: { e: EndorsementDTO; refs: AccountRefs }) {
  const ex = refs.exercises[e.exercise];
  const lesson = ex && refs.lessons[ex.lesson];
  if (!ex || !lesson) {
    return (
      <li className="account-item">
        <span className="muted">Exercise #{e.exercise}, which no longer exists</span> · {e.createdAt.slice(0, 10)}
      </li>
    );
  }
  return (
    <li className="account-item">
      <Link href={`${lesson.href}#${e.exercise}`}>
        Exercise {ex.number}
        {ex.title ? ` (${ex.title})` : ""}
      </Link>{" "}
      of <em>{lesson.title}</em> <span className="muted">({lesson.course})</span>
      <span className="muted small"> · endorsed {e.createdAt.slice(0, 10)}</span>
      {e.contentHash && e.contentHash !== ex.hash && (
        <span className="endorse-old small"> · the exercise has changed since; check the new version to renew the endorsement</span>
      )}
    </li>
  );
}

function CommentItem({ c, refs }: { c: CommentDTO; refs: AccountRefs }) {
  const lesson = refs.lessons[c.lessonId];
  return (
    <li className="account-item">
      <div className="account-item-head">
        {c.parentId == null && <span className={`chip chip-static kind-${c.kind}`}>{KIND_LABELS[c.kind]}</span>}
        {c.parentId == null && <span className="chip chip-static">{STATUS[c.status]}</span>}
        {lesson ? (
          <Link href={`${lesson.href}#remark-${c.id}`}>
            {lesson.title} <span className="muted">({lesson.course})</span>
          </Link>
        ) : (
          <span className="muted">{c.lessonId} (lesson removed)</span>
        )}
        <span className="muted small"> · {c.createdAt.slice(0, 10)}</span>
      </div>
      {c.anchor && <blockquote className="c-quote account-quote" dangerouslySetInnerHTML={{ __html: renderMathText(c.anchor.display) }} />}
      <div className="account-body" dangerouslySetInnerHTML={{ __html: renderMathText(c.body) }} />
    </li>
  );
}
