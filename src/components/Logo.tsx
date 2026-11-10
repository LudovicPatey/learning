// Φₑ badge. Drawn as SVG so the subscript always sits inside the square.
export function Logo({ size = 32 }: { size?: number }) {
  return (
    <svg className="brand-logo" width={size} height={size} viewBox="0 0 32 32" aria-hidden>
      <defs>
        <linearGradient id="logo-grad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#4f46e5" />
          <stop offset="1" stopColor="#7c3aed" />
        </linearGradient>
      </defs>
      <rect width="32" height="32" rx="9" fill="url(#logo-grad)" />
      <text x="13" y="22.5" textAnchor="middle" fontFamily="Georgia, 'Times New Roman', serif" fontSize="19" fill="#fff">
        Φ
      </text>
      <text x="21.5" y="26" fontFamily="Georgia, 'Times New Roman', serif" fontStyle="italic" fontSize="11" fill="#fff">
        e
      </text>
    </svg>
  );
}
