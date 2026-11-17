# Generates the inline SVG figures of the course on admissible sets and constructibility.
# Usage: python3 scripts/figures/admissible-sets.py out.json
# Paste each figure into the lesson that uses it:
#   standard-part                     -> constructible-hierarchy.md
#   l-ladder                          -> hyp-in-l.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

# ---------------------------------------------------------------- the ordinals of an omega-model of KP
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The ordinals of an omega-model of KP on a line: an initial segment of standard ordinals, from 0 through omega to at least the Church-Kleene ordinal, isomorphic to the ordinal of the standard part; then non-standard ordinals with no least element, each having a non-standard ordinal below it">']
s.append('<defs>' + marker('sp-arrow', 'muted-fill') + '</defs>')
s.append('<line x1="40" y1="80" x2="300" y2="80" class="accent-stroke" stroke-width="3"/>')
s.append('<line x1="330" y1="80" x2="570" y2="80" class="muted-stroke" stroke-width="3" stroke-dasharray="7 5"/>')
for x, lab in ((40, '0'), (90, 'ω'), (250, 'ω₁ᶜᵏ')):
    s.append(f'<line x1="{x}" y1="72" x2="{x}" y2="88" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<text x="{x}" y="106" text-anchor="middle" class="math">{lab}</text>')
s.append('<text x="170" y="56" text-anchor="middle" class="label">standard ordinals: the ordinals of N</text>')
s.append('<text x="450" y="56" text-anchor="middle" class="label">non-standard ordinals</text>')
for x in (560, 500, 440, 380):
    s.append(f'<path d="M{x},92 Q{x - 30},118 {x - 56},92" class="muted-stroke" fill="none" stroke-width="1.1" marker-end="url(#sp-arrow)"/>')
s.append('<text x="300" y="150" text-anchor="middle" class="label">every non-standard ordinal has a non-standard ordinal below it: there is no least one</text>')
s.append('<text x="300" y="166" text-anchor="middle" class="label">for an ω-model, ω is standard, and o(N) ≥ ω₁ᶜᵏ</text>')
s.append('</svg>')
out['standard-part'] = ''.join(s)

# ---------------------------------------------------------------- levels of L and the classes of subsets of N
ticks = [(50, '0'), (150, 'ω'), (230, 'ω+1'), (520, 'ω₁ᶜᵏ')]
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="The constructible hierarchy on a line: L zero is empty; L omega is HF, over which the Sigma-1 relations on numbers are the c.e. relations; L omega plus one contains the arithmetic sets; L at the Church-Kleene ordinal has the hyperarithmetic sets as its subsets of N, and over it the Sigma-1 relations on numbers are the Pi-1-1 relations">']
s.append('<line x1="50" y1="70" x2="560" y2="70" class="ink-stroke" stroke-width="1.5"/>')
s.append('<line x1="300" y1="70" x2="470" y2="70" class="muted-stroke" stroke-width="1.5" stroke-dasharray="4 4"/>')
for x, sub in ticks:
    s.append(f'<line x1="{x}" y1="62" x2="{x}" y2="78" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<text x="{x}" y="46" text-anchor="middle" class="math">L<tspan class="mrm" font-size="11" dy="4">{sub}</tspan></text>')
s.append('<rect x="100" y="100" width="110" height="52" rx="4" class="soft-fill"/>')
s.append('<text x="155" y="118" text-anchor="middle" class="label">Σ₁ over HF</text><text x="155" y="136" text-anchor="middle" class="label">= c.e.</text>')
s.append('<rect x="215" y="100" width="120" height="52" rx="4" class="soft-fill"/>')
s.append('<text x="275" y="118" text-anchor="middle" class="label">new reals:</text><text x="275" y="136" text-anchor="middle" class="label">arithmetic sets</text>')
s.append('<rect x="430" y="100" width="160" height="70" rx="4" class="soft-fill"/>')
s.append('<text x="510" y="118" text-anchor="middle" class="label">reals in it = HYP</text><text x="510" y="136" text-anchor="middle" class="label">Σ₁ over it = Π¹₁</text><text x="510" y="154" text-anchor="middle" class="label">admissible</text>')
s.append('<text x="385" y="58" text-anchor="middle" class="label">no admissible level</text>')
s.append('<text x="150" y="92" text-anchor="middle" class="label">= HF</text>')
s.append('<text x="300" y="184" text-anchor="middle" class="label">ω and ω₁ᶜᵏ are the first two admissible ordinals</text>')
s.append('</svg>')
out['l-ladder'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
