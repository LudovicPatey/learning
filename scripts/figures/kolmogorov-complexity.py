# Generates the inline SVG figures of the course on Kolmogorov complexity.
# Usage: python3 scripts/figures/kolmogorov-complexity.py out.json
# Paste each figure into the lesson that uses it:
#   pair-description                  -> plain-complexity.md
#   lower-envelope                    -> non-computability.md
#   oscillation                       -> initial-segments.md
#   kraft                             -> prefix-free-complexity.md
#   kc-stages                         -> kc-theorem.md
#   omega-settled                     -> coding-theorem.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, math, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def brace(x1, x2, y, up=True, cls='ink-stroke'):
    """A square bracket from x1 to x2 at height y, opening towards the blocks."""
    d = -6 if up else 6
    return (f'<path d="M{x1:.1f},{y + d:.1f} L{x1:.1f},{y:.1f} L{x2:.1f},{y:.1f} L{x2:.1f},{y + d:.1f}" '
            f'class="{cls}" stroke-width="1.1"/>')


# ---------------------------------------------------------------- the description of a pair (plain complexity)
# Blocks: rho-bar, 01, alpha_0, alpha_1.
x0, y0, h = 20, 60, 30
blocks = [('ρ', 160, 'cell'), ('01', 34, 'cell head-cell'), ('α₀', 150, 'cell'), ('α₁', 190, 'cell')]
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="An input of the machine of the pair proposition: the length of the first description written with doubled bits, the separator 01, then the two descriptions">']
x = x0
pos = []
for name, w, cls in blocks:
    s.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" class="{cls}"/>')
    s.append(f'<text x="{x + w / 2}" y="{y0 + 20}" text-anchor="middle" class="math" font-size="16">{name}</text>')
    if name == 'ρ':
        s.append(f'<line x1="{x + w / 2 - 6}" y1="{y0 + 6}" x2="{x + w / 2 + 6}" y2="{y0 + 6}" class="ink-stroke" stroke-width="1"/>')
    pos.append((x, x + w))
    x += w
a, b = pos[0]
s.append(brace(a + 1, b - 1, y0 - 8))
s.append(f'<text x="{(a + b) / 2}" y="{y0 - 22}" text-anchor="middle" class="label">ℓ = |α₀|, bits doubled</text>')
a, b = pos[2]
s.append(brace(a + 1, b - 1, y0 - 8))
s.append(f'<text x="{(a + b) / 2}" y="{y0 - 22}" text-anchor="middle" class="label">shortest description of σ</text>')
a, b = pos[3]
s.append(brace(a + 1, b - 1, y0 - 8))
s.append(f'<text x="{(a + b) / 2}" y="{y0 - 22}" text-anchor="middle" class="label">shortest description of τ</text>')
a, b = pos[0]
s.append(brace(a + 1, b - 1, y0 + h + 8, up=False, cls='muted-stroke'))
s.append(f'<text x="{(a + b) / 2}" y="{y0 + h + 26}" text-anchor="middle" class="label">≈ 2 log C(σ) bits</text>')
a, b = pos[2][0], pos[3][1]
s.append(brace(a + 1, b - 1, y0 + h + 34, up=False, cls='muted-stroke'))
s.append(f'<text x="{(a + b) / 2}" y="{y0 + h + 52}" text-anchor="middle" class="label">C(σ) + C(τ) bits, split after the first ℓ</text>')
s.append('</svg>')
out['pair-description'] = ''.join(s)

# ---------------------------------------------------------------- the lower envelope of C (schematic)
# Illustrative values of C(m) for m = 1..N: about log m, with dips at numbers of a simple form.
N = 64
vals = []
for m in range(1, N + 1):
    v = int(math.log2(m)) + ((m * 37) % 5) // 2
    vals.append(v)
for m, v in [(16, 2), (24, 3), (32, 3), (40, 4), (48, 4), (56, 4), (64, 4)]:
    vals[m - 1] = v
env = [min(vals[i:]) for i in range(N)]
X0, Y0, dx, dy = 50, 230, 8, 22
s = ['<svg class="fig" viewBox="0 0 600 280" width="600" role="img" aria-label="Schematic values of C(m) as dots, close to log m, with occasional low values; the lower envelope mu(n), the minimum of C(m) over m at least n, is a slowly increasing staircase">']
s.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0 + dx * N + 14}" y2="{Y0}" class="axis"/>')
s.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0 - dy * 9}" class="axis"/>')
s.append(f'<text x="{X0 + dx * N + 20}" y="{Y0 + 4}" class="math" font-size="14">m</text>')
for k in range(0, 9, 2):
    s.append(f'<text x="{X0 - 8}" y="{Y0 - dy * k + 4}" text-anchor="end" class="mrm muted" font-size="10">{k}</text>')
for m in (1, 16, 32, 48, 64):
    s.append(f'<text x="{X0 + dx * m}" y="{Y0 + 16}" text-anchor="middle" class="mrm muted" font-size="10">{m}</text>')
# log m curve
pts = ' '.join(f'{X0 + dx * m:.1f},{Y0 - dy * math.log2(m):.1f}' for m in range(1, N + 1))
s.append(f'<polyline points="{pts}" class="muted-stroke" stroke-dasharray="4 3" stroke-width="1.1"/>')
s.append(f'<text x="{X0 + dx * N + 6}" y="{Y0 - dy * math.log2(N) - 6:.1f}" class="label">log m</text>')
# envelope staircase
d = f'M{X0 + dx * 1},{Y0 - dy * env[0]}'
for i in range(1, N):
    x = X0 + dx * (i + 1) - dx / 2
    d += f' L{x:.1f},{Y0 - dy * env[i - 1]} L{x:.1f},{Y0 - dy * env[i]}'
d += f' L{X0 + dx * N + 8},{Y0 - dy * env[-1]}'
s.append(f'<path d="{d}" class="accent-stroke" stroke-width="1.8"/>')
for m in range(1, N + 1):
    s.append(f'<circle cx="{X0 + dx * m}" cy="{Y0 - dy * vals[m - 1]}" r="2.6" class="ink-fill"/>')
s.append(f'<circle cx="{X0 + 20}" cy="{Y0 + 36}" r="2.6" class="ink-fill"/><text x="{X0 + 30}" y="{Y0 + 40}" class="label">C(m), schematic values</text>')
s.append(f'<line x1="{X0 + 210}" y1="{Y0 + 36}" x2="{X0 + 232}" y2="{Y0 + 36}" class="accent-stroke" stroke-width="1.8"/><text x="{X0 + 238}" y="{Y0 + 40}" class="label">μ(n) = min of C(m) over m ≥ n</text>')
s.append('</svg>')
out['lower-envelope'] = ''.join(s)

# ---------------------------------------------------------------- the oscillation theorem
x0, y0, h = 20, 62, 28
wb, wa = 90, 420
s = ['<svg class="fig" viewBox="0 0 600 168" width="600" role="img" aria-label="An initial segment of X cut into the prefix beta of length m and the block alpha of length N, where N is the number coded by beta; alpha alone is a description of beta alpha">']
s.append('<defs>' + marker('kc-osc-arrow') + '</defs>')
s.append(f'<rect x="{x0}" y="{y0}" width="{wb}" height="{h}" class="cell head-cell"/>')
s.append(f'<rect x="{x0 + wb}" y="{y0}" width="{wa}" height="{h}" class="cell"/>')
s.append(f'<text x="{x0 + wb + wa + 10}" y="{y0 + 19}" class="mrm" font-size="16">⋯</text>')
s.append(f'<text x="{x0 + wb / 2}" y="{y0 + 19}" text-anchor="middle" class="math" font-size="16">β</text>')
s.append(f'<text x="{x0 + wb + wa / 2}" y="{y0 + 19}" text-anchor="middle" class="math" font-size="16">α</text>')
s.append(brace(x0 + 1, x0 + wb - 1, y0 - 8))
s.append(f'<text x="{x0 + wb / 2}" y="{y0 - 20}" text-anchor="middle" class="label">X↾m, codes N</text>')
s.append(brace(x0 + wb + 1, x0 + wb + wa - 1, y0 - 8))
s.append(f'<text x="{x0 + wb + wa / 2}" y="{y0 - 20}" text-anchor="middle" class="label">the next N bits of X, N ≥ 2ᵐ − 1</text>')
s.append(brace(x0 + 1, x0 + wb + wa - 1, y0 + h + 8, up=False, cls='muted-stroke'))
s.append(f'<text x="{x0 + (wb + wa) / 2}" y="{y0 + h + 26}" text-anchor="middle" class="label">X↾(m + N): described by α alone, with N + c bits</text>')
xa = x0 + wb + wa / 2
s.append(f'<path d="M{xa - 60},{y0 + h + 52} C{xa - 200},{y0 + h + 66} {x0 + wb / 2 + 40},{y0 + h + 60} {x0 + wb / 2},{y0 + h + 34}" class="accent-stroke" stroke-width="1.2" marker-end="url(#kc-osc-arrow)"/>')
s.append(f'<text x="{xa - 52}" y="{y0 + h + 58}" class="label">the length |α| = N gives back β</text>')
s.append('</svg>')
out['oscillation'] = ''.join(s)

# ---------------------------------------------------------------- Kraft: prefix-free set and disjoint intervals
W = ['00', '010', '10', '110']
L, R = 40, 560
depth = 3


def tx(sg):
    d = len(sg)
    idx = int(sg, 2) if sg else 0
    return L + (idx + 0.5) * (R - L) / (2 ** d)


def ty(sg):
    return 24 + len(sg) * 44


nodes = ['']
for w in W:
    for k in range(1, len(w) + 1):
        if w[:k] not in nodes:
            nodes.append(w[:k])
others = ['011', '111']
for o in others:
    for k in range(1, len(o) + 1):
        if o[:k] not in nodes:
            nodes.append(o[:k])
nodes.sort(key=lambda n: (len(n), n))
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The prefix-free set 00, 010, 10, 110 as leaves of the binary tree, and the corresponding disjoint dyadic intervals of the unit interval, of total length 3/4">']
for n in nodes:
    if n == '':
        continue
    p = n[:-1]
    in_w = any(w.startswith(n) for w in W)
    cls = 'ink-stroke' if in_w else 'muted-stroke'
    dash = '' if in_w else ' stroke-dasharray="3 3"'
    s.append(f'<line x1="{tx(p):.1f}" y1="{ty(p)}" x2="{tx(n):.1f}" y2="{ty(n)}" class="{cls}" stroke-width="1.2"{dash}/>')
bar = 198
for n in nodes:
    if n in W:
        s.append(f'<circle cx="{tx(n):.1f}" cy="{ty(n)}" r="6" class="node"/>')
        s.append(f'<text x="{tx(n):.1f}" y="{ty(n) + 22}" text-anchor="middle" class="mrm" font-size="12">{n}</text>')
        s.append(f'<line x1="{tx(n):.1f}" y1="{ty(n) + 28}" x2="{tx(n):.1f}" y2="{bar - 2}" class="muted-stroke" stroke-dasharray="2 3"/>')
    elif n in others:
        s.append(f'<circle cx="{tx(n):.1f}" cy="{ty(n)}" r="3.5" class="muted-fill"/>')
    else:
        s.append(f'<circle cx="{tx(n):.1f}" cy="{ty(n)}" r="3.5" class="ink-fill"/>')
s.append(f'<text x="{tx("") + 10:.1f}" y="{ty("") - 4}" class="mrm" font-size="13">ε</text>')
s.append(f'<rect x="{L}" y="{bar}" width="{R - L}" height="22" class="cell"/>')
for w in W:
    d = len(w)
    idx = int(w, 2)
    a = L + idx * (R - L) / 2 ** d
    b = L + (idx + 1) * (R - L) / 2 ** d
    s.append(f'<rect x="{a + 1:.1f}" y="{bar}" width="{b - a - 2:.1f}" height="22" class="cell head-cell"/>')
    s.append(f'<text x="{(a + b) / 2:.1f}" y="{bar + 15}" text-anchor="middle" class="mrm" font-size="11">2⁻{"²" if d == 2 else "³"}</text>')
for v, lab in [(0, '0'), (0.5, '1/2'), (1, '1')]:
    x = L + v * (R - L)
    s.append(f'<text x="{x:.1f}" y="{bar + 38}" text-anchor="middle" class="mrm muted" font-size="11">{lab}</text>')
s.append(f'<text x="{L}" y="{bar + 62}" class="label">The interval of τ is the set of reals whose binary expansion begins with τ;</text>')
s.append(f'<text x="{L}" y="{bar + 78}" class="label">the intervals of a prefix-free set are disjoint, so their lengths add up to at most 1 (here 3/4).</text>')
s.append('</svg>')
out['kraft'] = ''.join(s)

# ---------------------------------------------------------------- stages of the KC construction
# Requests of lengths 2, 3, 1, 3 (total weight 1), served as in the proof.
reqs = [2, 3, 1, 3]
free = ['']
assigned = []
rows = [(list(free), list(assigned), None)]
for i, l in enumerate(reqs):
    cand = [f for f in free if len(f) <= l]
    rho = max(cand, key=len)
    k = l - len(rho)
    tau = rho + '0' * k
    free.remove(rho)
    free += [rho + '0' * j + '1' for j in range(k)]
    assigned.append((tau, i))
    rows.append((sorted(free), list(assigned), (l, rho, tau)))
L, R = 150, 580
s = ['<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="Five rows show the unit interval before and after each of four requests of lengths 2, 3, 1 and 3; assigned intervals are filled, free intervals are shaded and have pairwise distinct lengths">']
for r, (fr, asg, info) in enumerate(rows):
    y = 14 + r * 48
    if info is None:
        s.append(f'<text x="10" y="{y + 16}" class="label">start</text>')
    else:
        l, rho, tau = info
        s.append(f'<text x="10" y="{y + 10}" class="label">request {r}: length {l}</text>')
        s.append(f'<text x="10" y="{y + 26}" class="label">ρ = {rho or "ε"}, τ = {tau}</text>')
    for sg in fr:
        d = len(sg)
        idx = int(sg, 2) if sg else 0
        a = L + idx * (R - L) / 2 ** d
        b = L + (idx + 1) * (R - L) / 2 ** d
        s.append(f'<rect x="{a:.1f}" y="{y}" width="{b - a:.1f}" height="26" class="cell head-cell"/>')
        s.append(f'<text x="{(a + b) / 2:.1f}" y="{y + 17}" text-anchor="middle" class="mrm" font-size="12">{sg or "ε"}</text>')
    for sg, i in asg:
        d = len(sg)
        idx = int(sg, 2)
        a = L + idx * (R - L) / 2 ** d
        b = L + (idx + 1) * (R - L) / 2 ** d
        s.append(f'<rect x="{a:.1f}" y="{y}" width="{b - a:.1f}" height="26" class="cell"/>')
        s.append(f'<text x="{(a + b) / 2:.1f}" y="{y + 17}" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">{i}</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= {sg}</tspan></text>')
yl = 14 + len(rows) * 48 + 4
s.append(f'<rect x="{L}" y="{yl - 10}" width="14" height="12" class="cell head-cell"/><text x="{L + 20}" y="{yl}" class="label">free string</text>')
s.append(f'<rect x="{L + 120}" y="{yl - 10}" width="14" height="12" class="cell"/><text x="{L + 140}" y="{yl}" class="label">assigned to a request</text>')
s.append('</svg>')
out['kc-stages'] = ''.join(s)

# ---------------------------------------------------------------- settled stages for Omega
L, R = 40, 560
y = 92
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="On the real line, the dyadic interval from q to q plus 2 to the minus n contains Omega; once Omega_s exceeds q, a program of length at most n converging later would add at least 2 to the minus n and push the sum beyond q plus 2 to the minus n">']
s.append('<defs>' + marker('kc-omega-arrow', 'ink-fill') + marker('kc-omega-arrow2', 'ink-fill') + '</defs>')
xq, xq2 = 150, 410
xs, xo = 230, 330
s.append(f'<line x1="{L}" y1="{y}" x2="{R}" y2="{y}" class="axis"/>')
s.append(f'<rect x="{xq}" y="{y - 10}" width="{xq2 - xq}" height="20" class="soft-fill"/>')
for x, lab in [(xq, 'q'), (xq2, 'q + 2⁻ⁿ')]:
    s.append(f'<line x1="{x}" y1="{y - 14}" x2="{x}" y2="{y + 14}" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<text x="{x}" y="{y + 32}" text-anchor="middle" class="math" font-size="14">{lab}</text>')
s.append(f'<circle cx="{xs}" cy="{y}" r="4" class="ink-fill"/>')
s.append(f'<text x="{xs}" y="{y - 20}" text-anchor="middle" class="math" font-size="15">Ω<tspan class="mrm" font-size="10" dy="4">s</tspan></text>')
s.append(f'<circle cx="{xo}" cy="{y}" r="4" class="accent-fill"/>')
s.append(f'<text x="{xo}" y="{y - 20}" text-anchor="middle" class="math" font-size="15">Ω</text>')
xe = xs + (xq2 - xq) + 30
s.append(f'<path d="M{xs},{y + 46} L{xe},{y + 46}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#kc-omega-arrow)"/>')
s.append(f'<text x="{(xs + xe) / 2}" y="{y + 64}" text-anchor="middle" class="label">adding a new program of length ≤ n: at least 2⁻ⁿ, beyond q + 2⁻ⁿ</text>')
s.append(f'<text x="{L}" y="24" class="label">q = 0.ω<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">⋯ω</tspan><tspan font-size="9" dy="3">n−1</tspan><tspan dy="-3" dx="4">is read off the first n bits of Ω; the interval [q, q + 2⁻ⁿ) contains Ω.</tspan></text>')
s.append(f'<text x="{L}" y="42" class="label">At the first stage s with Ω<tspan font-size="9" dy="3">s</tspan><tspan dy="-3">\u00a0&gt; q,\u00a0every program of length ≤ n in the domain has converged.</tspan></text>')
s.append('</svg>')
out['omega-settled'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
