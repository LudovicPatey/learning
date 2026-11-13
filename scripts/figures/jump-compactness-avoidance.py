# Generates the inline SVG figures of the course on jump compactness avoidance.
# Usage: python3 scripts/figures/jump-compactness-avoidance.py out.json
# Paste each figure into the lesson that uses it:
#   product-cover     -> product-largeness.md
#   product-merging   -> product-mathias.md
#   meta-index        -> meta-conditions.md
#   weak-merging      -> meta-questions.md
#   valid-tree        -> delta2-jump-pa.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def box(x, y, w, h, lines, cls='state'):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>']
    n = len(lines)
    for k, t in enumerate(lines):
        ty = y + h / 2 + (k - (n - 1) / 2) * 16 + 4
        s.append(f'<text x="{x + w / 2:.1f}" y="{ty:.1f}" text-anchor="middle" class="label">{t}</text>')
    return ''.join(s)


def arrow(x1, y1, x2, y2, mid, cls='ink-stroke'):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" stroke-width="1.2" marker-end="url(#{mid})"/>'


def text(x, y, t, cls='label', anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{t}</text>'


# ---------------------------------------------------------------- product cover
# The 2-cover R, complement of R, and the four functions j : {0,1} -> 2 for the class L_R x L_coR.
R = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="The cover of the natural numbers by R and its complement, and the four ways to assign a part to each of the two coordinates; only the assignment of R to coordinate 0 and the complement of R to coordinate 1 gives a pair in the class L_R times L of the complement of R">']
x0, cw = 60, 30
s.append(text(30, 34, 'n', 'math'))
for k, b in enumerate(R):
    s.append(text(x0 + k * cw + cw / 2, 34, str(k), 'mrm muted'))
    cls = 'cell head-cell' if b else 'cell'
    s.append(f'<rect x="{x0 + k * cw}" y="42" width="{cw}" height="24" class="{cls}"/>')
    s.append(text(x0 + k * cw + cw / 2, 59, 'R' if b else '·', 'label'))
s.append(text(x0 + len(R) * cw + 14, 59, '⋯', 'mrm muted'))
s.append(text(300, 90, 'shaded: R; blank: the complement of R', 'label'))
rows = [('j = (0, 0)', '(R, R)', 'second coordinate misses the complement', False),
        ('j = (1, 1)', '(R̄, R̄)', 'first coordinate misses R', False),
        ('j = (0, 1)', '(R, R̄)', 'in the class', True),
        ('j = (1, 0)', '(R̄, R)', 'misses both', False)]
for k, (a, b, c, ok) in enumerate(rows):
    y = 108 + k * 28
    s.append(text(110, y + 16, a, 'label'))
    s.append(box(170, y, 110, 22, [b], cls='node' if ok else 'state'))
    s.append(text(300, y + 16, c, 'label', 'start'))
s.append('</svg>')
out['product-cover'] = ''.join(s)

# ---------------------------------------------------------------- product merging
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Merging by duplication: a condition with index set I and two negative answers giving classes A_0 and A_1 is extended by a condition with index set I times 0,1 whose slice 0 ranges over A_0 and slice 1 over A_1, with the same stem and copied reservoirs">']
s.append('<defs>' + marker('jca-pm-arr') + '</defs>')
s.append(box(200, 10, 200, 52, ['p = (σ, X⃗, S), index set I', 'p ?⊬ φ₀ and p ?⊬ φ₁']))
s.append(box(20, 100, 200, 44, ['𝒜₀ = 𝒜(p, φ₀) large'], cls='node'))
s.append(box(380, 100, 200, 44, ['𝒜₁ = 𝒜(p, φ₁) large'], cls='node'))
s.append(box(130, 186, 340, 52, ['q = (σ, X⃗ duplicated, T), index set I·{0, 1}', 'slice 0 ∈ 𝒜₀, slice 1 ∈ 𝒜₁']))
s.append(arrow(250, 64, 140, 96, 'jca-pm-arr'))
s.append(arrow(350, 64, 460, 96, 'jca-pm-arr'))
s.append(arrow(140, 146, 230, 182, 'jca-pm-arr'))
s.append(arrow(460, 146, 370, 182, 'jca-pm-arr'))
s.append(text(300, 132, '𝒜₀ ∩ 𝒜₁ need not be large', 'label'))
s.append('</svg>')
out['product-merging'] = ''.join(s)

# ---------------------------------------------------------------- meta index sets
s = ['<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="The index set I_0 with the single element epsilon, the index set I_1 with elements 0, 1, 2, and its three branches; with the coloring 0 to 0, 1 to 1, 2 to 0, the branch 0, 2 is monochromatic">']
s.append(text(60, 30, '𝕀₀', 'label'))
s.append(f'<circle cx="300" cy="26" r="13" class="state"/>')
s.append(text(300, 31, 'ε', 'math'))
s.append(text(60, 100, '𝕀₁', 'label'))
col = {0: 0, 1: 1, 2: 0}
xs = {0: 200, 1: 300, 2: 400}
for a in (0, 1, 2):
    s.append(f'<line x1="300" y1="39" x2="{xs[a]}" y2="83" class="muted-stroke" stroke-width="1"/>')
    cls = 'node' if col[a] == 0 else 'state'
    s.append(f'<circle cx="{xs[a]}" cy="96" r="13" class="{cls}"/>')
    s.append(text(xs[a], 101, str(a), 'mrm'))
    s.append(text(xs[a], 128, f'color {col[a]}', 'label'))
branches = [((0, 1), False), ((0, 2), True), ((1, 2), False)]
for k, ((a, b), mono) in enumerate(branches):
    x = 120 + k * 150
    s.append(box(x, 150, 120, 44, [f'branch {{{a}, {b}}}', 'monochromatic' if mono else 'two colors'],
                 cls='node' if mono else 'state'))
s.append('</svg>')
out['meta-index'] = ''.join(s)

# ---------------------------------------------------------------- weak merging
s = ['<svg class="fig" viewBox="0 0 600 240" width="600" role="img" aria-label="Weak merging at level 0: three negative answers give classes A_0, A_1, A_2; the extension has three copies of the reservoir, slice a ranging over A_a, and each branch a, b of I_1 promises the negations of phi_a and phi_b">']
s.append('<defs>' + marker('jca-wm-arr') + '</defs>')
s.append(box(170, 10, 260, 44, ['c of level 0: c ?⊬ φ₀, φ₁, φ₂']))
for a in range(3):
    x = 40 + a * 190
    s.append(box(x, 84, 140, 36, [f'𝒜{"₀₁₂"[a]} large'], cls='node'))
    s.append(arrow(300, 56, x + 70, 80, 'jca-wm-arr'))
for k, (a, b) in enumerate([(0, 1), (0, 2), (1, 2)]):
    x = 40 + k * 190
    s.append(box(x, 170, 140, 52, [f'branch {{{a}, {b}}}', f'promises ¬φ{"₀₁₂"[a]}, ¬φ{"₀₁₂"[b]}']))
    s.append(arrow(40 + a * 190 + 70, 122, x + 50, 166, 'jca-wm-arr', 'muted-stroke'))
    s.append(arrow(40 + b * 190 + 70, 122, x + 90, 166, 'jca-wm-arr', 'muted-stroke'))
s.append('</svg>')
out['weak-merging'] = ''.join(s)

# ---------------------------------------------------------------- tree of valid parts
cols = [['({ε}, 0)', '({ε}, 1)'],
        ['({ε}, 0)', '({ε}, 1)'],
        ['({0,1}, 0)', '({0,2}, 1)', '({1,2}, 1)'],
        ['({0,2}, 1)', '({1,2}, 1)'],
        ['({0,2}, 1)']]
parent = [None, [0, 1], [0, 1, 1], [1, 2], [0]]
path = [1, 1, 1, 0, 0]
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="Columns of valid parts of the meta-conditions c_0 to c_4, each part joined to its ancestor; some parts lose validity and have no descendants; a path through the columns is drawn in the accent color">']
X0, DX, Y0, DY = 60, 120, 50, 50
for t, c in enumerate(cols):
    s.append(text(X0 + t * DX, 22, f'c{"₀₁₂₃₄"[t]}', 'label'))
for t in range(1, len(cols)):
    for k, p in enumerate(parent[t]):
        on = (path[t] == k and path[t - 1] == p)
        cls = 'accent-stroke' if on else 'muted-stroke'
        s.append(f'<line x1="{X0 + (t - 1) * DX + 44}" y1="{Y0 + p * DY}" x2="{X0 + t * DX - 44}" y2="{Y0 + k * DY}" class="{cls}" stroke-width="{2 if on else 1}"/>')
for t, c in enumerate(cols):
    for k, lab in enumerate(c):
        cls = 'node' if path[t] == k else 'state'
        s.append(box(X0 + t * DX - 44, Y0 + k * DY - 14, 88, 28, [lab], cls=cls))
s.append(text(300, 212, 'level 0 for c₀, c₁; level 1 from c₂ on, after a weak merging step', 'label'))
s.append('</svg>')
out['valid-tree'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
