"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

// Client component: the reason is read in the browser, so that the page also
// works in the static export served by the PHP hosting (docs/DEPLOY.md).
export default function SignInError() {
  const [reason, setReason] = useState<string | null>(null);
  useEffect(() => setReason(new URLSearchParams(window.location.search).get("reason")), []);
  return (
    <div className="not-found">
      <h1>Sign-in failed</h1>
      <p>{reason ?? "Something went wrong while signing in with ORCID."}</p>
      <p style={{ marginTop: 24 }}>
        <Link className="btn btn-primary" href="/">
          Back to the home page
        </Link>
      </p>
    </div>
  );
}
