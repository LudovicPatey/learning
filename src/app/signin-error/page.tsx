import Link from "next/link";

export default async function SignInError({ searchParams }: PageProps<"/signin-error">) {
  const { reason } = await searchParams;
  return (
    <div className="not-found">
      <h1>Sign-in failed</h1>
      <p>{typeof reason === "string" ? reason : "Something went wrong while signing in with ORCID."}</p>
      <p style={{ marginTop: 24 }}>
        <Link className="btn btn-primary" href="/">
          Back to the home page
        </Link>
      </p>
    </div>
  );
}
