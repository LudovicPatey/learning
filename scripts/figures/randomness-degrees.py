# Generates the inline SVG figures of the course on random sequences and Turing degrees.
# Usage: python3 scripts/figures/randomness-degrees.py out.json
# Paste each figure into the lesson that uses it:
#   stephan-interval                  -> stephan-theorem.md
#   nu-representation                 -> computable-measures.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

# ---------------------------------------------------------------- Stephan's construction on an interval
cells = ['0', '1', '1', None, None, None, None, None]   # values of f defined so far
x0, w = 70, 40
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="A row of cells for the numbers of the interval I e, with f defined on the first three; below, a bar of measure divided into discarded classes for each defined value and a remaining class of measure at most 2 to the minus e minus 1">']
s.append('<text x="20" y="40" class="label">I_e</text>')
for i, v in enumerate(cells):
    cls = 'cell head-cell' if v is not None else 'cell'
    s.append(f'<rect x="{x0 + i * w}" y="24" width="{w}" height="26" class="{cls}"/>')
for i, v in enumerate(cells):
    if v is not None:
        s.append(f'<text x="{x0 + i * w + w // 2}" y="42" text-anchor="middle" class="mrm" font-size="13">{v}</text>')
a = cells.index(None)
s.append(f'<text x="{x0 + a * w + w // 2}" y="42" text-anchor="middle" class="math" font-size="13">?</text>')
s.append(f'<text x="{x0 + a * w + w // 2}" y="66" text-anchor="middle" class="label">a_s</text>')
s.append('<text x="420" y="42" class="label">values of f defined so far</text>')
s.append('<text x="20" y="116" class="label">measure</text>')
bars = [(70, 90, 'soft-fill', 'K₁'), (160, 70, 'soft-fill', 'K₂'), (230, 80, 'soft-fill', 'K₃'),
        (310, 60, 'accent-fill', '≤ 2⁻ᵉ⁻¹'), (370, 180, 'cell', 'Φ_e not total on I_e')]
for x, bw, cls, _ in bars:
    s.append(f'<rect x="{x}" y="100" width="{bw}" height="26" class="{cls}"/>')
for x, bw, _, lab in bars:
    s.append(f'<text x="{x + bw // 2}" y="118" text-anchor="middle" class="label">{lab}</text>')
s.append('<text x="70" y="150" class="label">shaded: discarded classes, each of measure ≥ 2⁻ᵉ⁻², pairwise disjoint;</text>')
s.append('<text x="70" y="168" class="label">accent: oracles still consistent with f, of measure ≤ 2⁻ᵉ⁻¹ once the interval is settled</text>')
s.append('</svg>')
out['stephan-interval'] = ''.join(s)

# ---------------------------------------------------------------- the nu-representation for the Bernoulli measure 2/3
L, R = 40, 560
def X(t):
    return round(L + (R - L) * t)
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The unit interval divided at one third into the intervals of 0 and 1, and the interval of 1 divided at five ninths into the intervals of 10 and 11; a point alpha in the interval of 10">']
s.append(f'<line x1="{L}" y1="50" x2="{R}" y2="50" class="axis"/>')
s.append(f'<rect x="{X(0)}" y="40" width="{X(1/3) - X(0)}" height="20" class="cell"/>')
s.append(f'<rect x="{X(1/3)}" y="40" width="{X(1) - X(1/3)}" height="20" class="cell head-cell"/>')
s.append(f'<text x="{(X(0) + X(1/3)) // 2}" y="55" text-anchor="middle" class="mrm" font-size="12">(0)</text>')
s.append(f'<text x="{(X(1/3) + X(1)) // 2}" y="55" text-anchor="middle" class="mrm" font-size="12">(1)</text>')
s.append(f'<rect x="{X(1/3)}" y="90" width="{X(5/9) - X(1/3)}" height="20" class="soft-fill"/>')
s.append(f'<rect x="{X(5/9)}" y="90" width="{X(1) - X(5/9)}" height="20" class="cell"/>')
s.append(f'<text x="{(X(1/3) + X(5/9)) // 2}" y="105" text-anchor="middle" class="mrm" font-size="12">(10)</text>')
s.append(f'<text x="{(X(5/9) + X(1)) // 2}" y="105" text-anchor="middle" class="mrm" font-size="12">(11)</text>')
for t, lab, y in [(0, '0', 80), (1/3, '1/3', 80), (5/9, '5/9', 130), (1, '1', 80)]:
    s.append(f'<text x="{X(t)}" y="{y}" text-anchor="middle" class="mrm muted" font-size="11">{lab}</text>')
xa = 290
s.append(f'<circle cx="{xa}" cy="100" r="4" class="accent-fill"/>')
s.append(f'<text x="{xa}" y="150" text-anchor="middle" class="math" font-size="14">α</text>')
s.append(f'<line x1="{xa}" y1="106" x2="{xa}" y2="136" class="muted-stroke" stroke-dasharray="3 3"/>')
s.append('</svg>')
out['nu-representation'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
