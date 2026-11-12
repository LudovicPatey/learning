# Generates the inline SVG figures of the course Ramsey's theorem for pairs.
# Usage: python3 scripts/figures/ramsey-theorem.py out.json
# Paste each figure into the lesson that uses it:
#   erdos-rado          -> jockusch.md
#   mathias-condition   -> cohesiveness.md
#   stable-coloring     -> stable-colorings.md
#   lex-monotone        -> stable-colorings.md
#   seetapun-proof      -> seetapun.md
# The output is deterministic: every loop runs over sorted or ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, s, x, y, size=16, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')


# ---------------------------------------------------------------- the Erdős–Radó tree
# Coloring of pairs: f({x, y}) = 1 if x + 2 divides y, 0 otherwise (x < y).
def f2(x, y):
    return 1 if y % (x + 2) == 0 else 0


N = 14
children = {(0,): []}
for s_ in range(1, N):
    node = (0,)
    while True:
        pat = tuple(f2(m, s_) for m in node)
        nxt = None
        for c in children[node]:
            if tuple(f2(m, c[-1]) for m in node) == pat:
                nxt = c
                break
        if nxt is None:
            new = node + (s_,)
            children[node].append(new)
            children[new] = []
            break
        node = nxt

# layout: leaves get consecutive x positions, inner nodes are centered over their children
xs = {}
leaf_count = [0]


def place(n):
    if not children[n]:
        xs[n] = leaf_count[0]
        leaf_count[0] += 1
    else:
        for c in children[n]:
            place(c)
        xs[n] = sum(xs[c] for c in children[n]) / len(children[n])


place((0,))
L = leaf_count[0]
X0, DX, Y0, DY = 60, 480 / (L - 1), 30, 56
path = (0, 1, 5, 11, 13)


def P(n):
    return X0 + xs[n] * DX, Y0 + (len(n) - 1) * DY


nodes = sorted(children, key=lambda t: (len(t), t))
s = ['<svg class="fig" viewBox="0 0 600 330" width="600" role="img" aria-label="The Erdős–Radó tree of a coloring of pairs after the insertion of the numbers 0 to 13">']
for n in nodes:
    if len(n) == 1:
        continue
    (x1, y1), (x2, y2) = P(n[:-1]), P(n)
    on = path[:len(n)] == n
    cls = 'accent-stroke' if on else 'ink-stroke'
    sw = '2.2' if on else '1.2'
    s.append(f'<line x1="{x1:.1f}" y1="{y1 + 11}" x2="{x2:.1f}" y2="{y2 - 11}" class="{cls}" stroke-width="{sw}"/>')
for n in nodes:
    x, y = P(n)
    on = path[:len(n)] == n
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="11" class="{"head-cell" if on else "node"}"/>')
    s.append(f'<text x="{x:.1f}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="13">{n[-1]}</text>')
    if len(n) > 1:
        pat = ''.join(str(f2(m, n[-1])) for m in n[:-1])
        s.append(f'<text x="{x + 15:.1f}" y="{y - 8}" class="mrm muted" font-size="10">{pat}</text>')
for n in nodes:
    if not children[n]:
        x, y = P(n)
        s.append(f'<text x="{x:.1f}" y="{y + 28}" text-anchor="middle" class="mrm muted" font-size="12">⋮</text>')
s.append('<text x="20" y="300" class="label">small digits: the pattern of a node over its parent σ, the colors of its pairs with σ(0), σ(1), …</text>')
s.append('<text x="20" y="318" class="label">highlighted: the branch 0, 1, 5, 11, 13, pre-homogeneous so far</text>')
s.append('</svg>')
out['erdos-rado'] = ''.join(s)

# ---------------------------------------------------------------- a Mathias condition and an extension
W, x0 = 22, 60
sigma = [0, 1, 0, 0, 1, 0]
X = [7, 9, 12, 13, 16, 18, 21]
tau_len = 13
tau_new = [9, 12]
Y = [16, 21]
ncell = 23


def row(y, length, ones, reservoir, label):
    r = [f'<text x="{x0 - 10}" y="{y + 15}" text-anchor="end" class="label">{label}</text>']
    for i in range(ncell):
        x = x0 + i * W
        if i < length:
            cls = 'cell head-cell' if i in ones else 'cell'
            r.append(f'<rect x="{x}" y="{y}" width="{W}" height="{W}" class="{cls}"/>')
            r.append(f'<text x="{x + W/2}" y="{y + 15}" text-anchor="middle" class="mrm" font-size="12">{1 if i in ones else 0}</text>')
        elif i in reservoir:
            r.append(f'<circle cx="{x + W/2}" cy="{y + W/2}" r="5" class="accent-fill"/>')
        else:
            r.append(f'<circle cx="{x + W/2}" cy="{y + W/2}" r="2" class="muted-fill"/>')
    r.append(f'<text x="{x0 + ncell * W + 6}" y="{y + 15}" class="mrm muted" font-size="14">⋯</text>')
    return r


s = ['<svg class="fig" viewBox="0 0 600 196" width="600" role="img" aria-label="A Mathias condition: a finite string followed by a reservoir; an extension decides more bits, adding only elements of the reservoir, and shrinks the reservoir">']
for i in range(0, ncell, 2):
    s.append(f'<text x="{x0 + i * W + W/2}" y="20" text-anchor="middle" class="mrm muted" font-size="10">{i}</text>')
s += row(30, len(sigma), [i for i, b in enumerate(sigma) if b], X, '(σ, X)')
s += row(100, tau_len, [i for i, b in enumerate(sigma) if b] + tau_new, Y, '(τ, Y)')
for i in tau_new:
    xx = x0 + i * W + W / 2
    s.append(f'<line x1="{xx}" y1="58" x2="{xx}" y2="96" class="accent-stroke" stroke-width="1.2" stroke-dasharray="3 3"/>')
s.append(f'<rect x="{x0}" y="150" width="14" height="14" class="cell head-cell"/><text x="{x0 + 20}" y="162" class="label">elements of the finite part</text>')
s.append(f'<circle cx="{x0 + 237}" cy="157" r="5" class="accent-fill"/><text x="{x0 + 248}" y="162" class="label">elements of the reservoir</text>')
s.append(f'<text x="{x0}" y="186" class="label">τ adds 9 and 12, both taken from X; the new reservoir Y is a subset of X above |τ| = 13</text>')
s.append('</svg>')
out['mathias-condition'] = ''.join(s)

# ---------------------------------------------------------------- a stable coloring and its limit set
A = {0, 2, 3, 6}
settle = {0: 3, 1: 5, 2: 2, 3: 9, 4: 6, 5: 4, 6: 10, 7: 8}
R, C = 8, 13
c, gx, gy = 26, 70, 40


def fcol(x, y):
    return (1 if x in A else 0) if y > settle[x] else (0 if x in A else 1)


s = ['<svg class="fig" viewBox="0 0 520 300" width="520" role="img" aria-label="A table of the colors of the pairs x less than y; each row is eventually constant, and its final value is the limit color of x">']
s.append(f'<text x="{gx + c * C / 2}" y="16" text-anchor="middle" class="math" font-size="14">y</text>')
for y in range(1, C + 1):
    s.append(f'<text x="{gx + (y - 1) * c + c/2}" y="{gy - 8}" text-anchor="middle" class="mrm muted" font-size="11">{y}</text>')
s.append(f'<text x="{gx - 34}" y="{gy - 8}" text-anchor="middle" class="math" font-size="14">x</text>')
for x in range(R):
    yy = gy + x * c
    s.append(f'<text x="{gx - 34}" y="{yy + 17}" text-anchor="middle" class="mrm muted" font-size="11">{x}</text>')
    for y in range(1, C + 1):
        xx = gx + (y - 1) * c
        if y <= x:
            continue
        v = fcol(x, y)
        s.append(f'<rect x="{xx}" y="{yy}" width="{c}" height="{c}" class="{"cell head-cell" if v else "cell"}"/>')
        s.append(f'<text x="{xx + c/2}" y="{yy + 17}" text-anchor="middle" class="mrm" font-size="12">{v}</text>')
    s.append(f'<text x="{gx + C * c + 8}" y="{yy + 17}" class="mrm muted" font-size="13">⋯</text>')
    lv = 1 if x in A else 0
    lx = gx + C * c + 40
    s.append(f'<rect x="{lx}" y="{yy}" width="{c}" height="{c}" class="{"cell head-cell" if lv else "cell"}"/>')
    s.append(f'<text x="{lx + c/2}" y="{yy + 17}" text-anchor="middle" class="mrm" font-size="12">{lv}</text>')
s.append(f'<text x="{gx + C * c + 40 + c/2}" y="{gy - 8}" text-anchor="middle" class="label">limit</text>')
s.append(f'<text x="{gx - 40}" y="{gy + R * c + 28}" class="label">row x lists f({{x, y}}) for y &gt; x; after finitely many changes it is constant.</text>')
s.append(f'<text x="{gx - 40}" y="{gy + R * c + 46}" class="label">The last column is the limit set: here A = {{0, 2, 3, 6}} on the rows shown.</text>')
s.append('</svg>')
out['stable-coloring'] = ''.join(s)

# ---------------------------------------------------------------- lexicographically decreasing rows
vecs = ['11010', '10111', '10101', '10011', '01110', '01101', '01011', '01010']
c, gx, gy = 30, 90, 44
s = ['<svg class="fig" viewBox="0 0 520 330" width="520" role="img" aria-label="The rows (R_0(a_n), R_1(a_n), …) of a homogeneous set of color 0 decrease lexicographically; the first difference between consecutive rows is a drop">']
for i in range(len(vecs[0])):
    s.append(sub('R', str(i), gx + i * c + c/2, gy - 12, 14))
s.append(f'<text x="{gx + 5 * c + 12}" y="{gy - 12}" class="mrm muted" font-size="14">⋯</text>')
for n, v in enumerate(vecs):
    yy = gy + n * c
    s.append(sub('a', str(n), gx - 26, yy + 20, 14))
    first = None
    if n > 0:
        prev = vecs[n - 1]
        first = next(i for i in range(len(v)) if v[i] != prev[i])
    for i, b in enumerate(v):
        xx = gx + i * c
        cls = 'cell head-cell' if i == first else 'cell'
        s.append(f'<rect x="{xx}" y="{yy}" width="{c}" height="{c}" class="{cls}"/>')
        s.append(f'<text x="{xx + c/2}" y="{yy + 20}" text-anchor="middle" class="mrm" font-size="14">{b}</text>')
    s.append(f'<text x="{gx + 5 * c + 12}" y="{yy + 20}" class="mrm muted" font-size="14">⋯</text>')
s.append(f'<text x="{gx + 2.5 * c}" y="{gy + len(vecs) * c + 22}" text-anchor="middle" class="mrm muted" font-size="14">⋮</text>')
tx = gx + 6 * c + 20
s.append(f'<rect x="{tx}" y="{gy + 4}" width="16" height="16" class="cell head-cell"/>')
s.append(f'<text x="{tx + 24}" y="{gy + 17}" class="label">first index where a row differs</text>')
s.append(f'<text x="{tx + 24}" y="{gy + 33}" class="label">from the previous one: 1 becomes 0</text>')
s.append(f'<text x="{tx}" y="{gy + 70}" class="label">column 0 drops at most once;</text>')
s.append(f'<text x="{tx}" y="{gy + 86}" class="label">column k rises only when a</text>')
s.append(f'<text x="{tx}" y="{gy + 102}" class="label">column j &lt; k drops, so it</text>')
s.append(f'<text x="{tx}" y="{gy + 118}" class="label">changes finitely often</text>')
s.append('</svg>')
out['lex-monotone'] = ''.join(s)

# ---------------------------------------------------------------- the structure of the proof of Seetapun's theorem
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The proof of Seetapun theorem: a cohesive set makes the coloring stable, the pigeonhole principle on its limit set gives a subset, from which a homogeneous set is computed; each step keeps C out of the cone">']
s.append('<defs>' + marker('rt-arr') + '</defs>')
def seg(parts):
    """parts: list of (text, kind) with kind 'm' (math italic), 'r' (roman), 's' (subscript, roman), 'si' (subscript, italic)."""
    r = []
    for txt, kind in parts:
        if kind == 'm':
            r.append(f'<tspan class="math">{txt}</tspan>')
        elif kind == 'si':
            r.append(f'<tspan class="math" font-size="9" dy="3">{txt}</tspan><tspan dy="-3">\u200b</tspan>')
        elif kind == 's':
            r.append(f'<tspan class="mrm" font-size="9" dy="3">{txt}</tspan><tspan dy="-3">\u200b</tspan>')
        else:
            r.append(f'<tspan class="mrm">{txt}</tspan>')
    return ''.join(r)


boxes = [
    (30, [('f', 'm'), (', computable in ', 'r'), ('Z', 'm')]),
    (100, [('G', 'm'), (' cohesive for (', 'r'), ('R', 'm'), ('x', 'si'), ('),  ', 'r'), ('C', 'm'), (' ≰ ', 'r'), ('Z', 'm'), (' ⊕ ', 'r'), ('G', 'm')]),
    (170, [('K', 'm'), (' ⊆ ', 'r'), ('A', 'm'), ('g', 'si'), (' or ', 'r'), ('K', 'm'), (' ∩ ', 'r'), ('A', 'm'), ('g', 'si'), (' = ∅,  ', 'r'), ('C', 'm'), (' ≰ ', 'r'), ('Z', 'm'), (' ⊕ ', 'r'), ('G', 'm'), (' ⊕ ', 'r'), ('K', 'm')]),
    (240, [('H', 'm'), (' homogeneous for ', 'r'), ('f', 'm'), (',  ', 'r'), ('H', 'm'), (' ≤', 'r'), ('T', 's'), (' ', 'r'), ('Z', 'm'), (' ⊕ ', 'r'), ('G', 'm'), (' ⊕ ', 'r'), ('K', 'm')]),
]
notes = ['', 'Mathias forcing: cone avoidance for COH; g = f on pairs of G is stable',
         'strong cone avoidance for the pigeonhole principle, on the limit set of g',
         'thin out K along the stable coloring g']
bx, bw, bh = 20, 340, 40
for y, parts in boxes:
    s.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="6" class="cell"/>')
    s.append(f'<text x="{bx + bw/2}" y="{y + 25}" text-anchor="middle" font-size="13" xml:space="preserve">{seg(parts)}</text>')
for i in range(1, len(boxes)):
    y1, y2 = boxes[i - 1][0] + bh, boxes[i][0]
    s.append(f'<line x1="{bx + bw/2}" y1="{y1}" x2="{bx + bw/2}" y2="{y2 - 2}" class="ink-stroke" stroke-width="1.3" marker-end="url(#rt-arr)"/>')
    s.append(f'<text x="{bx + bw/2 + 12}" y="{(y1 + y2) / 2 + 4}" class="label">{notes[i]}</text>')
s.append('</svg>')
out['seetapun-proof'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
