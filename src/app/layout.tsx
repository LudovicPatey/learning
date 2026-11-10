import type { Metadata } from "next";
import Link from "next/link";
import { Inter, JetBrains_Mono } from "next/font/google";
import "katex/dist/katex.min.css";
import "./globals.css";
import { UserMenu } from "@/components/UserMenu";
import { Logo } from "@/components/Logo";
import { ThemeToggle, themeScript } from "@/components/ThemeToggle";
import { SITE_NAME, SITE_TAGLINE } from "@/lib/site";

const sans = Inter({ subsets: ["latin"], variable: "--font-sans", display: "swap", axes: ["opsz"] });
const mono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono-face", display: "swap" });

export const metadata: Metadata = {
  title: { default: SITE_NAME, template: `%s · ${SITE_NAME}` },
  description: SITE_TAGLINE,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${sans.variable} ${mono.variable}`} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>
        <header className="site-header">
          <div className="site-header-inner">
            <Link href="/" className="brand">
              <Logo />
              <span className="brand-name">{SITE_NAME}</span>
            </Link>
            <nav className="site-nav">
              <Link href="/courses">Courses</Link>
              <Link href="/#map">Course map</Link>
            </nav>
            <ThemeToggle />
            <UserMenu />
          </div>
        </header>
        <main>{children}</main>
        <footer className="site-footer">
          <div className="site-footer-inner">
            <div>
              <strong>{SITE_NAME}</strong>
              <br />
              Course notes in mathematical logic.
            </div>
            <div>
              To report an error, select the passage in a lesson.
              <br />
              Remarks are signed with an ORCID iD.
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
