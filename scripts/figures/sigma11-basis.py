# Generates the inline SVG figures of the course on Σ¹₁ classes and the hyperjump.
# Usage: python3 scripts/figures/sigma11-basis.py out.json
# Paste each figure into the lesson that uses it:
#   gandy-witnesses                   -> gandy-basis.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

# ---------------------------------------------------------------- trees of tuples in the Gandy basis theorem
cols = [(160, 40), (270, 60), (380, 80), (490, 100)]          # center and width of the nodes rho_0..rho_3
rows = [('f₁ = X', 'cell head-cell'), ('f₂: X ∈ A', 'cell'), ('f₃: step 0', 'soft-fill'), ('f₄: step 1', 'muted-fill')]
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="A table: columns are steps 0, 1, 2, 3; rows are coordinates f1 (the set X), f2 (witness of membership in A), f3 (witness for step 0), f4 (witness for step 1); each step adds one row; cells show prefixes of growing length">']
s.append('<text x="20" y="34" class="label">coordinate</text>')
for i, (cx, _) in enumerate(cols):
    s.append(f'<text x="{cx}" y="34" text-anchor="middle" class="label">ρ{"₀₁₂₃"[i]}</text>')
for r, (lab, _) in enumerate(rows):
    s.append(f'<text x="20" y="{64 + 30 * r}" class="label">{lab}</text>')
for i, (cx, w) in enumerate(cols):
    for r, (_, cls) in enumerate(rows[: i + 2]):
        s.append(f'<rect x="{cx - w // 2}" y="{50 + 30 * r}" width="{w}" height="20" class="{cls}"/>')
s.append('<text x="160" y="64" text-anchor="middle" class="mrm" font-size="11">ε</text><text x="160" y="94" text-anchor="middle" class="mrm" font-size="11">ε</text>')
s.append('<text x="20" y="186" class="label">soft: a witness that 0 ∉ O^X was found; muted: no witness for 1, a constant coordinate, and 1 ∈ O^X</text>')
s.append('</svg>')
out['gandy-witnesses'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
