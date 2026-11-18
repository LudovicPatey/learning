# Generates the inline SVG figures of the course on computable categoricity.
# Usage: python3 scripts/figures/computable-categoricity.py out.json
# Paste each figure into the lesson that uses it:
#   finite-adjacencies                -> classical-examples.md
#   omega-x                           -> dimension-and-degrees.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

# ---------------------------------------------------------------- a linear order with finitely many adjacencies
# Pieces from left to right: ('dense', x0, x1) is an interval of type eta; ('pt', x, label) an element of P.
pieces = [('dense', 40, 170), ('pt', 200, 'p₀'), ('pt', 240, 'p₁'), ('dense', 270, 380),
          ('pt', 410, 'p₂'), ('pt', 450, 'p₃'), ('dense', 480, 600), ('pt', 630, 'p₄')]
adjacent = [(200, 240), (410, 450)]
y = 80
s = ['<svg class="fig" viewBox="0 0 680 170" width="680" role="img" aria-label="A linear order drawn on a line. Five marked elements p0 to p4 belong to the finite set P: p0 and p1 are adjacent, and so are p2 and p3; p4 is the greatest element. To the left of p0, between p1 and p2, and between p3 and p4 lie intervals drawn as shaded bands, each a dense order without endpoints">']
for kind, *rest in pieces:
    if kind == 'dense':
        x0, x1 = rest
        s.append(f'<rect x="{x0}" y="{y - 9}" width="{x1 - x0}" height="18" rx="9" class="soft-fill"/>')
        s.append(f'<line x1="{x0 + 6}" y1="{y}" x2="{x1 - 6}" y2="{y}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="2 3"/>')
        s.append(f'<text x="{(x0 + x1) / 2}" y="{y + 34}" text-anchor="middle" class="math">η</text>')
for a, b in adjacent:
    s.append(f'<path d="M{a},{y - 12} Q{(a + b) / 2},{y - 34} {b},{y - 12}" fill="none" class="accent-stroke" stroke-width="1.6"/>')
for kind, *rest in pieces:
    if kind == 'pt':
        x, lab = rest
        s.append(f'<circle cx="{x}" cy="{y}" r="6" class="head-cell"/>')
        s.append(f'<text x="{x}" y="{y + 30}" text-anchor="middle" class="math">{lab}</text>')
s.append(f'<text x="8" y="160" class="label">shaded: dense intervals without endpoints</text>')
s.append(f'<text x="672" y="160" text-anchor="end" class="label">arcs: the adjacent pairs</text>')
s.append('</svg>')
out['finite-adjacencies'] = ''.join(s)

# ---------------------------------------------------------------- the copy omega_X: pairs (a_n, b_n), an element inserted when n enters X
y = 70
pairs = [(0, False), (1, True), (2, False), (3, True), (4, False)]   # (n, n in X)
s = ['<svg class="fig" viewBox="0 0 680 150" width="680" role="img" aria-label="The copy of omega built from a c.e. set X, drawn as a line of elements from left to right. For n from 0 to 4 there is a pair a_n, b_n. For n = 1 and n = 3, which belong to X, an extra element is inserted between a_n and b_n; for the other values of n, a_n and b_n stay adjacent. The line continues to the right">']
x = 40
for n, inx in pairs:
    xa, xb = x, x + (90 if inx else 60)
    s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="muted-stroke" stroke-width="1.2"/>')
    if not inx:
        s.append(f'<path d="M{xa},{y - 10} Q{(xa + xb) / 2},{y - 30} {xb},{y - 10}" fill="none" class="accent-stroke" stroke-width="1.6"/>')
    s.append(f'<circle cx="{xa}" cy="{y}" r="6" class="node"/><text x="{xa}" y="{y + 28}" text-anchor="middle" class="math">a{"₀₁₂₃₄"[n]}</text>')
    s.append(f'<circle cx="{xb}" cy="{y}" r="6" class="node"/><text x="{xb}" y="{y + 28}" text-anchor="middle" class="math">b{"₀₁₂₃₄"[n]}</text>')
    if inx:
        xm = (xa + xb) / 2
        s.append(f'<circle cx="{xm}" cy="{y}" r="6" class="head-cell"/>')
    if n < len(pairs) - 1:
        s.append(f'<line x1="{xb}" y1="{y}" x2="{xb + 40}" y2="{y}" class="muted-stroke" stroke-width="1.2"/>')
    x = xb + 40
s.append(f'<line x1="{x - 40}" y1="{y}" x2="{x}" y2="{y}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 4"/>')
s.append(f'<text x="8" y="140" class="label">arcs: pairs that stay adjacent (n not in X)</text>')
s.append(f'<text x="672" y="140" text-anchor="end" class="label">highlighted: element inserted when n enters X</text>')
s.append('</svg>')
out['omega-x'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
