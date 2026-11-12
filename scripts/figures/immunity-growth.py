# Generates the inline SVG figures of the course Immunity and growth of functions.
# Usage: python3 scripts/figures/immunity-growth.py out.json
import json, sys
out = {}

def sub(base, s, x, y, size=15, anchor='middle', cls='math'):
    # a symbol with a subscript, e.g. F_3
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

# ---------------------------------------------------------------- a disjoint strong array of intervals
# Boundaries h^(n)(0) for h(x) = g(x) + x + 1; the block [14, 20) misses A.
bounds = [0, 2, 5, 9, 14, 20, 27, 35]
A = {1, 3, 6, 8, 11, 21, 25, 30, 33}
empty = 4
c, x0, y0 = 16, 20, 70
N = bounds[-1]
s = [f'<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="The numbers 0 to {N - 1} cut into consecutive blocks F_0, F_1, and so on; the elements of A are shaded; the block F_4 contains no element of A">']
for i in range(N):
    cls = 'cell head-cell' if i in A else 'cell'
    s.append(f'<rect x="{x0 + c*i}" y="{y0}" width="{c}" height="{c}" class="{cls}"/>')
    if i % 5 == 0:
        s.append(f'<text x="{x0 + c*i + c/2}" y="{y0 + c + 14}" text-anchor="middle" class="mrm muted" font-size="10">{i}</text>')
s.append(f'<text x="{x0 + c*N + 6}" y="{y0 + 12}" class="mrm muted" font-size="14">⋯</text>')
for n in range(len(bounds) - 1):
    a, b = bounds[n], bounds[n + 1]
    xa, xb = x0 + c*a + 2, x0 + c*b - 2
    cl = 'accent-stroke' if n == empty else 'ink-stroke'
    sw = '1.8' if n == empty else '1.1'
    s.append(f'<path d="M{xa},{y0 - 6} L{xa},{y0 - 12} L{xb},{y0 - 12} L{xb},{y0 - 6}" class="{cl}" stroke-width="{sw}"/>')
    s.append(sub('F', str(n), (xa + xb) / 2, y0 - 20, 14))
xa, xb = x0 + c*bounds[empty], x0 + c*bounds[empty + 1]
s.append(f'<text x="{xa}" y="{y0 + c + 34}" text-anchor="middle" class="math" font-size="13">x</text>')
s.append(f'<text x="{xb}" y="{y0 + c + 34}" text-anchor="middle" class="math" font-size="13">h<tspan class="mrm">(</tspan>x<tspan class="mrm">)</tspan></text>')
s.append(f'<line x1="{xa}" y1="{y0 + c + 2}" x2="{xa}" y2="{y0 + c + 22}" class="accent-stroke" stroke-dasharray="2 2"/>')
s.append(f'<line x1="{xb}" y1="{y0 + c + 2}" x2="{xb}" y2="{y0 + c + 22}" class="accent-stroke" stroke-dasharray="2 2"/>')
s.append(f'<rect x="{x0}" y="{y0 + c + 46}" width="12" height="12" class="cell head-cell"/><text x="{x0 + 18}" y="{y0 + c + 56}" class="label">element of A</text>')
s.append(f'<text x="{x0 + 130}" y="{y0 + c + 56}" class="label">F₄ = [x, h(x)) contains no element of A</text>')
s.append('</svg>')
out['strong-array'] = ''.join(s)

# ---------------------------------------------------------------- deficient and non-deficient stages
vals = [5, 9, 2, 12, 7, 3, 15, 10, 8, 18, 11, 20, 14, 16, 22, 19]
S = len(vals)
nondef = [t for t in range(S) if all(vals[u] > vals[t] for u in range(t + 1, S))]
x0, dx, ybase, dy = 60, 32, 276, 10
s = ['<svg class="fig" viewBox="0 0 600 322" width="600" role="img" aria-label="The values a(s) of an enumeration plotted against the stage s; the non-deficient stages, after which only larger values are enumerated, are highlighted and their values increase">']
s.append(f'<line x1="{x0 - 10}" y1="{ybase}" x2="{x0 + dx*S}" y2="{ybase}" class="axis"/>')
s.append(f'<line x1="{x0 - 10}" y1="{ybase}" x2="{x0 - 10}" y2="{ybase - dy*24}" class="axis"/>')
s.append(f'<text x="{x0 + dx*S + 6}" y="{ybase + 4}" class="math" font-size="14">s</text>')
s.append(f'<text x="{x0 - 14}" y="{ybase - dy*24 - 6}" class="math" font-size="14">a<tspan class="mrm">(</tspan>s<tspan class="mrm">)</tspan></text>')
for t in range(S):
    s.append(f'<text x="{x0 + dx*t}" y="{ybase + 16}" text-anchor="middle" class="mrm muted" font-size="10">{t}</text>')
for t in nondef:
    x, y = x0 + dx*t, ybase - dy*vals[t]
    s.append(f'<line x1="{x}" y1="{y}" x2="{x0 + dx*(S - 0.5)}" y2="{y}" class="accent-stroke" stroke-dasharray="3 3" stroke-width="1"/>')
pts = ' '.join(f'{x0 + dx*t},{ybase - dy*vals[t]}' for t in nondef)
s.append(f'<polyline points="{pts}" class="accent-stroke" stroke-width="1.6"/>')
for t in range(S):
    x, y = x0 + dx*t, ybase - dy*vals[t]
    if t in nondef:
        s.append(f'<circle cx="{x}" cy="{y}" r="5" class="accent-fill"/>')
    else:
        s.append(f'<circle cx="{x}" cy="{y}" r="4" class="node"/>')
ly = ybase + 36
s.append(f'<circle cx="{x0}" cy="{ly}" r="5" class="accent-fill"/><text x="{x0 + 12}" y="{ly + 4}" class="label">non-deficient stage: every later value is larger (dashed line)</text>')
s.append(f'<circle cx="{x0 + 370}" cy="{ly}" r="4" class="node"/><text x="{x0 + 382}" y="{ly + 4}" class="label">deficient stage</text>')
s.append('</svg>')
out['deficiency'] = ''.join(s)

# ---------------------------------------------------------------- an f-tree inside the full binary tree
depth = 5
W = 600
def pos(st):
    d = len(st)
    idx = int(st, 2) if st else 0
    return 20 + (idx + 0.5) * (W - 40) / (2 ** d), 30 + d * 44
T = {'': '', '0': '001', '1': '10', '00': '00100', '01': '0011', '10': '1010', '11': '10111'}
nodes = set(T.values())
on = set()
for v in nodes:
    for k in range(len(v) + 1):
        on.add(v[:k])
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="An f-tree: the nodes T(rho) are strings placed in the full binary tree; T(rho 0) and T(rho 1) are incompatible extensions of T(rho)">']
allstr = ['']
for d in range(1, depth + 1):
    allstr += [format(i, f'0{d}b') for i in range(2 ** d)]
for st in allstr:
    if st == '':
        continue
    (x1, y1), (x2, y2) = pos(st[:-1]), pos(st)
    if st in on:
        s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="accent-stroke" stroke-width="2"/>')
    else:
        s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="muted-stroke" stroke-width="0.8"/>')
for st in allstr:
    x, y = pos(st)
    if st not in nodes:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="2" class="muted-fill"/>')
for rho, v in T.items():
    x, y = pos(v)
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="5.5" class="node"/>')
    r = 'ε' if rho == '' else rho
    val = 'ε' if v == '' else v
    s.append(f'<text x="{x + 10:.1f}" y="{y + 4}" class="math" font-size="13">T<tspan class="mrm">({r}) = {val}</tspan></text>')
s.append('<line x1="24" y1="290" x2="44" y2="290" class="accent-stroke" stroke-width="2"/><text x="50" y="294" class="label">prefixes of the nodes of T</text>')
s.append('<circle cx="250" cy="290" r="5.5" class="node"/><text x="262" y="294" class="label">a node of T</text>')
s.append('</svg>')
out['f-tree'] = ''.join(s)

# ---------------------------------------------------------------- hyperimmune versus dominant
def panel(ox, title, f, g, n0=None):
    p = []
    w, h, n = 250, 150, 21
    sx = w / (n - 1)
    def X(i): return ox + 30 + sx * i
    def Y(v): return 30 + h - v * h / 30
    p.append(f'<line x1="{ox + 30}" y1="{30 + h}" x2="{ox + 30 + w + 8}" y2="{30 + h}" class="axis"/>')
    p.append(f'<line x1="{ox + 30}" y1="{30 + h}" x2="{ox + 30}" y2="22" class="axis"/>')
    p.append(f'<text x="{ox + 30 + w + 12}" y="{34 + h}" class="math" font-size="13">n</text>')
    p.append(f'<text x="{ox + 30 + w/2}" y="14" text-anchor="middle" class="label">{title}</text>')
    p.append('<polyline points="' + ' '.join(f'{X(i):.1f},{Y(g[i]):.1f}' for i in range(n)) + '" class="ink-stroke" stroke-width="1.3"/>')
    p.append('<polyline points="' + ' '.join(f'{X(i):.1f},{Y(f[i]):.1f}' for i in range(n)) + '" class="accent-stroke" stroke-width="1.8"/>')
    for i in range(n):
        if f[i] > g[i]:
            p.append(f'<circle cx="{X(i):.1f}" cy="{Y(f[i]):.1f}" r="3" class="accent-fill"/>')
    if n0 is not None:
        p.append(f'<line x1="{X(n0):.1f}" y1="{30 + h}" x2="{X(n0):.1f}" y2="40" class="muted-stroke" stroke-dasharray="3 3"/>')
        p.append(f'<text x="{X(n0):.1f}" y="{30 + h + 16}" text-anchor="middle" class="math" font-size="13">n<tspan class="mrm" font-size="9" dy="3">0</tspan></text>')
    return p
g = [3 + 0.9 * i for i in range(21)]
fh = [1, 2, 1, 2, 9, 2, 1, 3, 2, 2, 3, 17, 3, 2, 4, 3, 3, 3, 4, 29, 4]
fd = [0.5, 0.6, 1, 1.4, 2, 3, 4.5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25.5, 27, 28.5, 29.5]
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="Left: a hyperimmune function exceeds a computable function g at infinitely many points but may stay small elsewhere. Right: a dominant function is above g from some point n0 on">']
s += panel(0, 'hyperimmune: above g infinitely often', fh, g)
s += panel(300, 'dominant: above g from some point on', fd, g, n0=10)
s.append('<line x1="150" y1="222" x2="170" y2="222" class="ink-stroke" stroke-width="1.3"/><text x="176" y="226" class="label">a computable function g</text>')
s.append('<line x1="340" y1="222" x2="360" y2="222" class="accent-stroke" stroke-width="1.8"/><text x="366" y="226" class="label">the function f</text>')
s.append('</svg>')
out['growth'] = ''.join(s)

# ---------------------------------------------------------------- the stages in Arslanov's criterion
vals = ['3', '3', '7', '7', '7', '4', '4', '4', '4', '4', '4', '4']
sn = 5
c, x0, y0 = 36, 160, 40
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Two rows indexed by stages: the approximations f_t(p(n)), constant from the stage s(n) on, and the membership of n in the halting set at stage t, which can only change before s(n)">']
for t in range(len(vals)):
    s.append(f'<text x="{x0 + c*t + c/2}" y="{y0 - 10}" text-anchor="middle" class="mrm muted" font-size="11">{t}</text>')
s.append(f'<text x="{x0 - 10}" y="{y0 - 10}" text-anchor="end" class="label">stage t</text>')
s.append(f'<text x="{x0 - 10}" y="{y0 + 23}" text-anchor="end" class="math" font-size="14">f<tspan class="mrm" font-size="10" dy="4">t</tspan><tspan class="mrm" dy="-4">(</tspan>p<tspan class="mrm">(</tspan>n<tspan class="mrm">))</tspan></text>')
s.append(f'<text x="{x0 - 10}" y="{y0 + c + 23}" text-anchor="end" class="label">is n in ∅′ at stage t?</text>')
for t, v in enumerate(vals):
    cls = 'cell head-cell' if t >= sn else 'cell'
    s.append(f'<rect x="{x0 + c*t}" y="{y0}" width="{c}" height="{c}" class="{cls}"/>')
    s.append(f'<text x="{x0 + c*t + c/2}" y="{y0 + 23}" text-anchor="middle" class="mrm" font-size="15">{v}</text>')
    b = '1' if t >= 3 else '0'
    s.append(f'<rect x="{x0 + c*t}" y="{y0 + c}" width="{c}" height="{c}" class="cell"/>')
    s.append(f'<text x="{x0 + c*t + c/2}" y="{y0 + c + 23}" text-anchor="middle" class="mrm" font-size="15">{b}</text>')
xs = x0 + c*sn
s.append(f'<line x1="{xs}" y1="{y0 - 4}" x2="{xs}" y2="{y0 + 2*c + 26}" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/>')
s.append(f'<text x="{xs}" y="{y0 + 2*c + 42}" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm">(</tspan>n<tspan class="mrm">)</tspan></text>')
s.append(f'<text x="20" y="{y0 + 2*c + 66}" class="label">from s(n) on, the approximation equals f(p(n)); an entry of n into ∅′</text>')
s.append(f'<text x="20" y="{y0 + 2*c + 82}" class="label">after s(n) would make p(n) a fixed point of f, so it does not happen</text>')
s.append('</svg>')
out['arslanov'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
