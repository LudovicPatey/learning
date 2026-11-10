"use client";

import { useEffect, useState } from "react";
import { OrcidIcon } from "./OrcidIcon";

type Me = { orcid: string; name: string; isAdmin: boolean };

export function UserMenu() {
  const [state, setState] = useState<{ user: Me | null; devLogin: boolean; orcidConfigured: boolean } | null>(null);
  const [returnTo, setReturnTo] = useState("/");

  useEffect(() => {
    setReturnTo(window.location.pathname + window.location.search);
    fetch("/api/auth/me")
      .then((r) => r.json())
      .then(setState)
      .catch(() => setState({ user: null, devLogin: false, orcidConfigured: false }));
  }, []);

  if (!state) return <div className="user-menu" />;
  if (!state.user) {
    return (
      <div className="user-menu">
        <a className="btn btn-orcid btn-small" href={`/api/auth/orcid/login?returnTo=${encodeURIComponent(returnTo)}`}>
          <OrcidIcon size={16} /> Sign in with ORCID
        </a>
        {!state.orcidConfigured && state.devLogin && <span className="dev-tag" title="ORCID is not configured: sign-in uses a local test account">dev</span>}
      </div>
    );
  }
  return (
    <div className="user-menu">
      <a className="user-name" href={`https://orcid.org/${state.user.orcid}`} target="_blank" rel="noreferrer" title={state.user.orcid}>
        <OrcidIcon size={16} /> {state.user.name}
      </a>
      {state.user.isAdmin && <span className="dev-tag">maintainer</span>}
      <button
        className="link-btn"
        onClick={async () => {
          await fetch("/api/auth/logout", { method: "POST" });
          window.location.reload();
        }}
      >
        Sign out
      </button>
    </div>
  );
}
