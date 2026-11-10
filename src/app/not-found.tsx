import Link from "next/link";

export default function NotFound() {
  return (
    <div className="not-found">
      <h1>Page not found</h1>
      <p>The requested page does not exist.</p>
      <p style={{ marginTop: 24, display: "flex", gap: 10, justifyContent: "center", flexWrap: "wrap" }}>
        <Link className="btn btn-primary" href="/">
          Home
        </Link>
        <Link className="btn" href="/courses">
          All courses
        </Link>
      </p>
    </div>
  );
}
