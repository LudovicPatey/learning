# Generates the inline SVG figures of the course on effective descriptive set theory.
# Usage: python3 scripts/figures/descriptive-set-theory.py out.json
# Paste each figure into the lesson that uses it:
#   rank-map, reduction-stages        -> norms.md
#   uniformization-choice             -> uniformization.md
#   sigma11-splitting                 -> perfect-sets.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, s, x, y, size=16, anchor='middle', cls='math', scls='mrm'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="{scls}" font-size="{int(size * 0.68)}" dy="4">{s}</tspan></text>')


def dyadic_interval(s, left, right):
    d = len(s)
    idx = int(s, 2) if s else 0
    w = (right - left) / (2 ** d)
    return left + idx * w, left + (idx + 1) * w


# ---------------------------------------------------------------- a strictly monotone map between trees
# Trees drawn with the root at the top. Each node: name -> (x, y, rank, label).
S = {'': (110, 40, 2), 'a': (60, 110, 1), 'b': (160, 110, 0), 'c': (60, 180, 0)}
S_edges = [('', 'a'), ('', 'b'), ('a', 'c')]
T = {'': (430, 40, 3), 'p': (380, 110, 2), 'q': (500, 110, 0), 'r': (380, 180, 1), 't': (380, 250, 0)}
T_edges = [('', 'p'), ('', 'q'), ('p', 'r'), ('r', 't')]
g = [('', ''), ('a', 'p'), ('c', 'r'), ('b', 'q')]

s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Two trees S and T with the ranks of their nodes, and a strictly monotone map from S to T drawn as dashed arrows">']
s.append('<defs>' + marker('dst-rank-arrow', 'accent-fill') + '</defs>')
for tree, edges in ((S, S_edges), (T, T_edges)):
    for u, v in edges:
        x1, y1, _ = tree[u]
        x2, y2, _ = tree[v]
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.4"/>')
# the map, drawn behind the nodes
bends = {'': -40, 'a': 34, 'c': 30, 'b': -26}
for u, v in g:
    x1, y1, _ = S[u]
    x2, y2, _ = T[v]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + bends[u]
    s.append(f'<path d="M{x1 + 9},{y1} Q{mx:.1f},{my:.1f} {x2 - 10},{y2}" class="accent-stroke" stroke-width="1.2" '
             f'stroke-dasharray="4 3" marker-end="url(#dst-rank-arrow)"/>')
for tree, side in ((S, -1), (T, 1)):
    for name, (x, y, rk) in tree.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="6" class="node"/>')
        anchor = 'end' if side < 0 else 'start'
        s.append(f'<text x="{x + side * 11}" y="{y + 4}" text-anchor="{anchor}" class="mrm" font-size="12">{rk}</text>')
s.append('<text x="110" y="20" text-anchor="middle" class="math" font-size="16">S</text>')
s.append('<text x="430" y="20" text-anchor="middle" class="math" font-size="16">T</text>')
s.append('<text x="270" y="50" text-anchor="middle" class="math" font-size="15">g</text>')
s.append('<text x="20" y="286" class="label">numbers: the ranks of the nodes; ρ(S) = 2 ≤ ρ(T) = 3, and each node σ of S has rank at most that of g(σ)</text>')
s.append('</svg>')
out['rank-map'] = ''.join(s)

# ---------------------------------------------------------------- reduction by stage comparison
L, R, INF = 70, 400, 450
rows = [
    ('0', 60, 210, 'ρ₀ ≤ ρ₁: 0 ∈ B′'),
    ('1', None, 150, 'ρ₂ = ∞ > ρ₃: 1 ∈ C′'),
    ('2', 260, 260, 'ρ₄ = ρ₅: 2 ∈ B′'),
    ('3', None, None, 'both ∞: 3 ∉ B ∪ C'),
]
s = ['<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="For each n, the stages of 2n and 2n+1 on an ordinal axis; n goes to B prime when 2n arrives no later than 2n+1, and to C prime when 2n+1 arrives strictly first">']
for i, (n, a, b, note) in enumerate(rows):
    y = 34 + i * 46
    s.append(f'<line x1="{L}" y1="{y}" x2="{R}" y2="{y}" class="axis"/>')
    s.append(f'<line x1="{R}" y1="{y}" x2="{R + 18}" y2="{y}" class="axis" stroke-dasharray="2 3"/>')
    s.append(f'<text x="22" y="{y + 5}" class="math" font-size="15">n</text>')
    s.append(f'<text x="34" y="{y + 5}" class="mrm" font-size="15">= {n}</text>')
    pa = INF if a is None else L + a * (R - L) / 300
    pb = INF if b is None else L + b * (R - L) / 300
    if a == b:
        s.append(f'<circle cx="{pa:.1f}" cy="{y}" r="6" class="accent-fill"/>')
        s.append(f'<rect x="{pb - 4:.1f}" y="{y - 18}" width="8" height="8" class="ink-fill"/>')
    else:
        s.append(f'<circle cx="{pa:.1f}" cy="{y}" r="6" class="accent-fill"/>')
        s.append(f'<rect x="{pb - 5:.1f}" y="{y - 5}" width="10" height="10" class="ink-fill"/>')
    s.append(f'<text x="{INF + 26}" y="{y + 5}" class="label">{note}</text>')
y0 = 34 + 4 * 46 - 8
s.append(f'<text x="{L}" y="{y0}" text-anchor="middle" class="mrm" font-size="13">0</text>')
s.append(f'<text x="{R}" y="{y0}" text-anchor="middle" class="mrm" font-size="13">ω<tspan font-size="9" dy="-6">CK</tspan><tspan font-size="9" dy="9" dx="-12">1</tspan></text>')
s.append(f'<text x="{INF}" y="{y0}" text-anchor="middle" class="mrm" font-size="13">∞</text>')
s.append(f'<circle cx="{L + 4}" cy="{y0 + 18}" r="5" class="accent-fill"/><text x="{L + 14}" y="{y0 + 22}" class="label">stage of 2n (finite iff n ∈ B)</text>')
s.append(f'<rect x="{L + 220}" y="{y0 + 13}" width="10" height="10" class="ink-fill"/><text x="{L + 236}" y="{y0 + 22}" class="label">stage of 2n + 1 (finite iff n ∈ C)</text>')
s.append('</svg>')
out['reduction-stages'] = ''.join(s)

# ---------------------------------------------------------------- uniformization: least stage, then least m
stages = [None, 150, 70, None, 70, 110, None, 200]   # stage of <n, m>, None = infinity
X0, DX, Y0, H = 90, 52, 210, 150      # axis origin, column width, baseline, height of the ordinal axis
s = ['<svg class="fig" viewBox="0 0 600 306" width="600" role="img" aria-label="For a fixed n, the stage of each pair (n, m) plotted above m; the selected value is the least m among those whose pair enters at the least stage">']
top = Y0 - H
s.append(f'<line x1="{X0 - 20}" y1="{Y0}" x2="{X0 + DX * len(stages)}" y2="{Y0}" class="axis"/>')
s.append(f'<line x1="{X0 - 20}" y1="{Y0}" x2="{X0 - 20}" y2="{top}" class="axis"/>')
s.append(f'<line x1="{X0 - 20}" y1="{top - 30}" x2="{X0 + DX * len(stages)}" y2="{top - 30}" class="axis" stroke-dasharray="2 3"/>')
s.append(f'<text x="{X0 - 28}" y="{Y0 + 4}" text-anchor="end" class="mrm" font-size="13">0</text>')
s.append(f'<text x="{X0 - 28}" y="{top + 4}" text-anchor="end" class="mrm" font-size="13">ω<tspan font-size="9" dy="-6">CK</tspan><tspan font-size="9" dy="9" dx="-12">1</tspan></text>')
s.append(f'<text x="{X0 - 28}" y="{top - 26}" text-anchor="end" class="mrm" font-size="13">∞</text>')
alpha = min(v for v in stages if v is not None)
ya = Y0 - alpha * H / 220
s.append(f'<line x1="{X0 - 20}" y1="{ya:.1f}" x2="{X0 + DX * len(stages)}" y2="{ya:.1f}" class="muted-stroke" stroke-dasharray="4 3"/>')
s.append(f'<text x="{X0 - 28}" y="{ya + 4:.1f}" text-anchor="end" class="math" font-size="14">α</text>')
chosen = stages.index(alpha)
for m, v in enumerate(stages):
    x = X0 + DX * m + DX / 2 - 10
    s.append(f'<text x="{x:.1f}" y="{Y0 + 20}" text-anchor="middle" class="mrm" font-size="13">{m}</text>')
    y = top - 30 if v is None else Y0 - v * H / 220
    if v is not None:
        s.append(f'<line x1="{x:.1f}" y1="{Y0}" x2="{x:.1f}" y2="{y:.1f}" class="muted-stroke" stroke-width="1"/>')
    if m == chosen:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" class="accent-fill"/>')
    elif v is None:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="node"/>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="ink-fill"/>')
s.append(f'<text x="{X0 + DX * len(stages) / 2:.1f}" y="{Y0 + 42}" text-anchor="middle" class="math" font-size="15">m</text>')
s.append(f'<text x="{X0 - 20}" y="{Y0 + 70}" class="label">dots: the stage of ⟨n, m⟩; hollow dots at ∞: R(n, m) fails. Two pairs enter at the least stage α;</text>')
s.append(f'<text x="{X0 - 20}" y="{Y0 + 86}" class="label">f(n) = {chosen}, the least of them. The value 1, which enters later, is not chosen.</text>')
s.append('</svg>')
out['uniformization-choice'] = ''.join(s)

# ---------------------------------------------------------------- splitting of good pairs in a Sigma^1_1 class
# First components of the pairs u_s, as cylinders of Cantor space; each splits into two disjoint cylinders.
first = {'': '', '0': '00', '1': '10', '00': '0001', '01': '0011', '10': '1000', '11': '1011',
         '000': '000100', '001': '000111', '010': '001100', '011': '001110', '100': '100000', '101': '100011',
         '110': '101100', '111': '101111'}
L, R = 120, 580
s = ['<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="The first components of the good pairs u_s drawn as cylinders of Cantor space: each cylinder contains two disjoint cylinders, one for each extension of s">']
for d in range(4):
    y = 22 + d * 50
    s.append(f'<line x1="{L}" y1="{y + 10}" x2="{R}" y2="{y + 10}" class="axis"/>')
    s.append(f'<text x="20" y="{y + 15}" class="label">|s| = {d}</text>')
    for key in sorted(k for k in first if len(k) == d):
        a, b = dyadic_interval(first[key], L, R)
        s.append(f'<rect x="{a + 1:.1f}" y="{y}" width="{b - a - 2:.1f}" height="20" class="cell head-cell"/>')
        if d <= 2:
            s.append(sub('σ', key if key else 'ε', f'{(a + b) / 2:.1f}', y + 15, 13, 'middle'))
# a member X_Z: Z = 0110... selects 0 -> 01 -> 011
Z = '011'
a, b = dyadic_interval(first[Z], L, R)
xz = (a + b) / 2
y = 22 + 4 * 50
s.append(f'<text x="{xz:.1f}" y="{y - 14}" text-anchor="middle" class="mrm muted" font-size="12">⋮</text>')
s.append(f'<circle cx="{xz:.1f}" cy="{y + 2}" r="5" class="accent-fill"/>')
s.append(sub('X', 'Z', f'{xz + 10:.1f}', y + 7, 15, 'start'))
s.append(f'<text x="20" y="{y + 7}" class="label">Z = 011…</text>')
s.append('</svg>')
out['sigma11-splitting'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
