// ORCID iD mark (green circle with "iD"), drawn inline.
export function OrcidIcon({ size = 16 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 256 256" aria-hidden className="orcid-icon">
      <circle cx="128" cy="128" r="128" fill="#A6CE39" />
      <g fill="#fff">
        <rect x="70" y="77" width="17" height="105" />
        <circle cx="78.5" cy="56" r="11" />
        <path d="M108 77h45c43 0 62 31 62 52.5 0 23.5-18.5 52.5-62 52.5h-45V77Zm17 89h27c38 0 46.5-29 46.5-36.5 0-12.5-8-36.5-46.5-36.5h-27v73Z" />
      </g>
    </svg>
  );
}
