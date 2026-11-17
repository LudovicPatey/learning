# Generates the inline SVG figures of the course on Σ¹₁ classes and the hyperjump.
# Usage: python3 scripts/figures/sigma11-basis.py out.json
# Paste each figure into the lesson that uses it:
#   tree-morphism                     -> hyperjump.md
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

# ---------------------------------------------------------------- a morphism between trees, following the proof of lem-tree-morphism
def marker(mid, cls='accent-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')
S = {'ε': (140, 50, 2), '0': (100, 120, 1), '1': (180, 120, 0), '00': (100, 190, 0)}
T = {'ε': (450, 50, 2), '0': (400, 120, 1), '1': (460, 120, 0), '2': (520, 120, 0), '00': (370, 190, 0), '01': (430, 190, 0)}
f = [('ε', 'ε', 0), ('0', '0', -45), ('1', '0', 30), ('00', '00', 0)]
s = ['<svg class="fig" viewBox="0 0 600 240" width="600" role="img" aria-label="Two trees S and T with their ranks; dashed arrows map each node of S to a node of T of the same length and of rank at least as large; both children of the root of S are mapped to the same child of the root of T">']
s.append('<defs>' + marker('tm-arrow') + '</defs>')
for tree, name, x in ((S, 'S', 40), (T, 'T', 580)):
    s.append(f'<text x="{x}" y="30" text-anchor="middle" class="math">{name}</text>')
    for k, (cx, cy, _) in tree.items():
        if k != 'ε':
            px, py, _ = tree[k[:-1] or 'ε']
            s.append(f'<line x1="{px}" y1="{py}" x2="{cx}" y2="{cy}" class="ink-stroke" stroke-width="1.2"/>')
    for k, (cx, cy, r) in tree.items():
        s.append(f'<circle cx="{cx}" cy="{cy}" r="9" class="node"/>')
        s.append(f'<text x="{cx}" y="{cy + 4}" text-anchor="middle" class="mrm" font-size="11">{r}</text>')
for a, b, bend in f:
    x0, y0, _ = S[a]
    x1, y1, _ = T[b]
    mx, my = (x0 + x1) / 2, y0 + bend
    s.append(f'<path d="M{x0 + 11},{y0} Q{mx:g},{my} {x1 - 12},{y1}" class="accent-stroke" fill="none" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#tm-arrow)"/>')
s.append('<text x="300" y="232" text-anchor="middle" class="label">numbers in the nodes: ranks; dashed arrows: the morphism f</text>')
s.append('</svg>')
out['tree-morphism'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
