# Generates the inline SVG figures of the course on martingales.
# Usage: python3 scripts/figures/martingales.py out.json
# Paste each figure into the lesson that uses it:
#   betting-tree        -> betting-strategies.md
#   savings-plot        -> ville-theorem.md
#   exit-timeline       -> cr-construction.md
#   success-panels      -> schnorr-randomness.md
#   hierarchy           -> randomness-hierarchy.md
# The output is deterministic: every loop runs over ordered data.
import json, math, sys
from fractions import Fraction as Fr
out = {}


def mtext(txt, x, y, size=14, anchor='start', cls='math'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{txt}</text>'


def sub(base, s, x, y, size=14, anchor='start'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size * 0.7)}" dy="4">{s}</tspan></text>')


def frac(q):
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


# ---------------------------------------------------------------- betting tree (betting-strategies)
# Proportional strategy: bet 1/3 of the capital on the bit 1.  Initial capital 1.
# The prefix-free set S of the minimal strings with capital at least b = 10/9 is {1, 011}.
delta = Fr(1, 3)
b = Fr(10, 9)
depth = 3


def cap(s):
    v = Fr(1)
    for c in s:
        v *= (1 + delta) if c == '1' else (1 - delta)
    return v


strings = [''] + [format(i, f'0{d}b') for d in range(1, depth + 1) for i in range(2 ** d)]
S = [s for s in strings if cap(s) >= b and not any(cap(s[:j]) >= b for j in range(len(s)))]
W0, H0 = 600, 300
leaf_x = [55 + i * 70 for i in range(2 ** depth)]


def pos(s):
    d = len(s)
    idx = int(s, 2) if s else 0
    span = 2 ** (depth - d)
    x = sum(leaf_x[idx * span:(idx + 1) * span]) / span
    return x, 34 + d * 70


def below_S(s):
    return any(s.startswith(t) and s != t for t in S)


p = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="Binary tree of depth three labelled by the capital of the strategy that bets one third of its capital on the bit 1; '
     'the strings 1 and 011, the first where the capital reaches 10/9, are highlighted">']
for s in strings:
    if s:
        x0, y0 = pos(s[:-1])
        x1, y1 = pos(s)
        cls = 'muted-stroke' if below_S(s) else 'ink-stroke'
        p.append(f'<line x1="{x0:.1f}" y1="{y0 + 6}" x2="{x1:.1f}" y2="{y1 - 16}" class="{cls}" stroke-width="1"/>')
        p.append(mtext(s[-1], (x0 + x1) / 2 + (-9 if s[-1] == '0' else 5), (y0 + y1) / 2 - 2, 11, 'middle', 'mrm'))
for s in strings:
    x, y = pos(s)
    txt = frac(cap(s))
    w = 12 + 7 * len(txt)
    if s in S:
        p.append(f'<rect x="{x - w / 2:.1f}" y="{y - 14}" width="{w:.1f}" height="20" rx="3" class="head-cell"/>')
    elif below_S(s):
        p.append(f'<rect x="{x - w / 2:.1f}" y="{y - 14}" width="{w:.1f}" height="20" rx="3" class="soft-fill"/>')
    p.append(mtext(txt, x, y + 1, 13, 'middle', 'mrm'))
    if len(s) == depth:
        p.append(mtext(s, x, y + 20, 10, 'middle', 'mrm'))
    else:
        p.append(mtext(s if s else 'ε', x - w / 2 - 4, y + 1, 10, 'end', 'mrm' if s else 'math'))
p.append(f'<rect x="60" y="{H0 - 20}" width="22" height="14" rx="3" class="head-cell"/>')
p.append(f'<text x="88" y="{H0 - 9}" class="label">first strings with capital ≥ 10/9: the set S</text>')
p.append(f'<rect x="360" y="{H0 - 20}" width="22" height="14" rx="3" class="soft-fill"/>')
p.append(f'<text x="388" y="{H0 - 9}" class="label">extensions of S</text>')
p.append('</svg>')
out['betting-tree'] = ''.join(p)
lhs = sum(Fr(1, 2 ** len(t)) * cap(t) for t in S)
print('S =', S, ' sum 2^-|t| d(t) =', lhs, ' measure =', sum(Fr(1, 2 ** len(t)) for t in S))

# ---------------------------------------------------------------- savings trick (ville-theorem)
# Capital of d along one sequence: doubling up to peaks 4, 8, 16, 32, then halving down to 1/4.
d = [1.0]
for peak in [2, 3, 4, 5]:
    while d[-1] < 2 ** peak:
        d.append(d[-1] * 2)
    while d[-1] > 0.25:
        d.append(d[-1] / 2)


def savings(d):
    res = []
    for n in range(len(d)):
        tot = 0.0
        for k in range(60):
            fr = next((m for m in range(n + 1) if d[m] > 2 ** k), None)
            tot += 2 ** -k * (d[fr] if fr is not None else d[n])
        res.append(tot)
    return res


dp = savings(d)
W0, H0 = 600, 250
x0, x1, ytop, ybot = 50, 570, 20, 210
N = len(d) - 1
ymax = 32


def px(n):
    return x0 + (x1 - x0) * n / N


def py(v):
    return ybot - (ybot - ytop) * v / ymax


p = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="Capital of a martingale along one sequence, with higher and higher peaks followed by falls to one quarter, '
     'and the capital of the savings martingale, which never falls by more than 2 and tends to infinity">']
p.append(f'<line x1="{x0}" y1="{ybot}" x2="{x1 + 8}" y2="{ybot}" class="axis"/>')
p.append(f'<line x1="{x0}" y1="{ybot}" x2="{x0}" y2="{ytop - 6}" class="axis"/>')
for v in [0, 8, 16, 24, 32]:
    p.append(mtext(str(v), x0 - 8, py(v) + 4, 11, 'end', 'mrm'))
    if v:
        p.append(f'<line x1="{x0}" y1="{py(v):.1f}" x2="{x1}" y2="{py(v):.1f}" class="muted-stroke" stroke-width="0.5" stroke-dasharray="2 4"/>')
p.append(mtext('n', x1 + 12, ybot + 4, 14))
pts = ' '.join(f'{px(n):.1f},{py(v):.1f}' for n, v in enumerate(d))
p.append(f'<polyline points="{pts}" class="ink-stroke" stroke-width="1.3"/>')
pts = ' '.join(f'{px(n):.1f},{py(v):.1f}' for n, v in enumerate(dp))
p.append(f'<polyline points="{pts}" class="accent-stroke" stroke-width="2"/>')
p.append(f'<line x1="150" y1="{H0 - 14}" x2="172" y2="{H0 - 14}" class="ink-stroke" stroke-width="1.3"/>')
p.append(mtext('d', 178, H0 - 10, 13))
p.append(f'<text x="188" y="{H0 - 10}" class="label">(X↾n)</text>')
p.append(f'<line x1="330" y1="{H0 - 14}" x2="352" y2="{H0 - 14}" class="accent-stroke" stroke-width="2"/>')
p.append(f'<text x="358" y="{H0 - 10}" class="math" font-size="13">d<tspan class="mrm" font-size="10" dy="-6">+</tspan></text>')
p.append(f'<text x="374" y="{H0 - 10}" class="label">(X↾n), with savings</text>')
p.append('</svg>')
out['savings-plot'] = ''.join(p)
print('savings values:', [round(v, 2) for v in dp])

# ---------------------------------------------------------------- exit timeline (cr-construction)
# Index e enters the combined martingale at position 2^e and leaves at its exit position t_e,
# the first n at which psi_e is not n-good; None means that it has not left by position 32.
exits = [None, 6, None, 11, None]
W0, H0 = 600, 250
x0, x1 = 70, 570
P = 32
top = 30
row_h = 30


def qx(n):
    return x0 + (x1 - x0) * n / P


p = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="For each index e from 0 to 4, the interval of positions during which e belongs to the set of active indices: '
     'it starts at 2 to the e and ends at the exit position, if any; a vertical line at position 24">']
p.append('<defs><marker id="mg-exit-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs>')
yb = top + row_h * len(exits) + 6
p.append(f'<line x1="{x0}" y1="{yb}" x2="{x1 + 6}" y2="{yb}" class="axis"/>')
for n in [0, 1, 2, 4, 8, 16, 24, 32]:
    p.append(f'<line x1="{qx(n):.1f}" y1="{yb}" x2="{qx(n):.1f}" y2="{yb + 4}" class="axis"/>')
    p.append(mtext(str(n), qx(n), yb + 17, 11, 'middle', 'mrm'))
p.append(f'<text x="{x1 + 2}" y="{yb + 34}" class="label" text-anchor="end">position n</text>')
for e, t in enumerate(exits):
    y = top + e * row_h
    p.append(mtext(f'e = {e}', 14, y + 14, 13, 'start', 'mrm'))
    a = qx(2 ** e)
    p.append(f'<circle cx="{a:.1f}" cy="{y + 10}" r="3.5" class="accent-fill"/>')
    if t is None:
        p.append(f'<line x1="{a:.1f}" y1="{y + 10}" x2="{qx(P) + 4:.1f}" y2="{y + 10}" class="accent-stroke" stroke-width="2.2" marker-end="url(#mg-exit-arrow)"/>')
    else:
        b_ = qx(t)
        p.append(f'<line x1="{a:.1f}" y1="{y + 10}" x2="{b_:.1f}" y2="{y + 10}" class="accent-stroke" stroke-width="2.2"/>')
        p.append(f'<line x1="{b_:.1f}" y1="{y + 4}" x2="{b_:.1f}" y2="{y + 16}" class="ink-stroke" stroke-width="1.6"/>')
        p.append(f'<text x="{b_ + 6:.1f}" y="{y + 14}" class="label">exit at {t}</text>')
xn = qx(24)
p.append(f'<line x1="{xn:.1f}" y1="{top - 8}" x2="{xn:.1f}" y2="{yb}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3"/>')
p.append(mtext('n = 24', xn, top - 14, 12, 'middle', 'mrm'))
p.append(f'<text x="{x0}" y="{H0 - 6}" class="label">X↾24 is computed from 24 and the exit data of e = 0, …, 4: (none, 6, none, 11, none)</text>')
p.append('</svg>')
out['exit-timeline'] = ''.join(p)

# ---------------------------------------------------------------- Schnorr and Kurtz success (schnorr-randomness)
W0, H0 = 600, 240


def panel(ox, title, dvals, hvals, marks):
    q = []
    w, h = 250, 160
    yb_ = 30 + h
    N_ = len(hvals) - 1
    vmax = max(max(dvals), max(hvals)) * 1.05

    def X(n):
        return ox + w * n / N_

    def Y(v):
        return yb_ - h * v / vmax
    q.append(f'<line x1="{ox}" y1="{yb_}" x2="{ox + w + 8}" y2="{yb_}" class="axis"/>')
    q.append(f'<line x1="{ox}" y1="{yb_}" x2="{ox}" y2="24" class="axis"/>')
    q.append(mtext('n', ox + w + 12, yb_ + 4, 13))
    q.append(f'<text x="{ox + w / 2:.1f}" y="14" text-anchor="middle" class="label">{title}</text>')
    pts = ' '.join(f'{X(n):.1f},{Y(v):.1f}' for n, v in enumerate(hvals))
    q.append(f'<polyline points="{pts}" class="ink-stroke" stroke-width="1.3"/>')
    pts = ' '.join(f'{X(n):.1f},{Y(v):.1f}' for n, v in enumerate(dvals))
    q.append(f'<polyline points="{pts}" class="accent-stroke" stroke-width="1.8"/>')
    for n in marks:
        q.append(f'<circle cx="{X(n):.1f}" cy="{Y(dvals[n]):.1f}" r="3" class="accent-fill"/>')
    return q


Nn = 40
hv = [math.floor(math.log2(n + 2)) for n in range(Nn + 1)]
# left: the capital touches the order infinitely often (at the marked points) and is small elsewhere
peaks = {6: 3.4, 15: 4.3, 27: 5.2, 38: 5.6}
dl = []
for n in range(Nn + 1):
    base = 0.6 + 0.4 * math.sin(n / 2.0) ** 2
    for c, v in peaks.items():
        base = max(base, v - 1.1 * abs(n - c))
    dl.append(base)
# right: the capital stays above the order at every n
dr = [hv[n] + 0.4 + 0.5 * math.sin(n / 1.7) ** 2 + 0.03 * n for n in range(Nn + 1)]
p = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="Two plots of the capital of a computable martingale along a sequence against a computable order h. Left: the '
     'capital reaches the order at infinitely many points, the failure of Schnorr randomness. Right: the capital is above the order '
     'at every point, the failure of Kurtz randomness">']
p += panel(30, 'not Schnorr random: d ≥ h infinitely often', dl, hv, sorted(peaks))
p += panel(330, 'not Kurtz random: d ≥ h everywhere', dr, hv, [])
p.append(f'<line x1="170" y1="{H0 - 14}" x2="192" y2="{H0 - 14}" class="ink-stroke" stroke-width="1.3"/>')
p.append(f'<text x="198" y="{H0 - 10}" class="label">the order h(n)</text>')
p.append(f'<line x1="330" y1="{H0 - 14}" x2="352" y2="{H0 - 14}" class="accent-stroke" stroke-width="1.8"/>')
p.append(f'<text x="358" y="{H0 - 10}" class="label">the capital d(X↾n)</text>')
p.append('</svg>')
out['success-panels'] = ''.join(p)

# ---------------------------------------------------------------- hierarchy (randomness-hierarchy)
boxes = [
    ('Martin-Löf random', 'no c.e. martingale succeeds'),
    ('computably random', 'no computable martingale succeeds'),
    ('Schnorr random', 'no computable d, order h with d ≥ h infinitely often'),
    ('Kurtz random', 'no computable d, order h with d ≥ h everywhere'),
]
notes = [
    'strict: a Δ⁰₂ example (lesson 5)',
    'strict: admitted (high degrees)',
    'strict: weakly 1-generic sequences',
]
W0 = 600
bw, bh, gap = 300, 46, 34
bx = 150
top = 12
H0 = top + len(boxes) * bh + (len(boxes) - 1) * gap + 12
p = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="Four boxes from top to bottom: Martin-Löf, computable, Schnorr and Kurtz randomness, each with its martingale '
     'characterization, joined by implication arrows with the reason why each implication is strict; a bracket marks that the '
     'first three notions coincide outside the high degrees">']
p.append('<defs><marker id="mg-hier-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs>')
ys = []
for i, (name, cond) in enumerate(boxes):
    y = top + i * (bh + gap)
    ys.append(y)
    p.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="4" class="cell"/>')
    p.append(f'<text x="{bx + 12}" y="{y + 19}" font-size="13">{name}</text>')
    p.append(f'<text x="{bx + 12}" y="{y + 37}" class="label">{cond}</text>')
for i, note in enumerate(notes):
    ya = ys[i] + bh
    yb_ = ys[i + 1]
    xm = bx + bw / 2
    p.append(f'<line x1="{xm}" y1="{ya + 2}" x2="{xm}" y2="{yb_ - 3}" class="ink-stroke" stroke-width="1.3" marker-end="url(#mg-hier-arrow)"/>')
    p.append(f'<text x="{xm + 10}" y="{(ya + yb_) / 2 + 4:.1f}" class="label">{note}</text>')
xb = bx - 14
y_a, y_b = ys[0] + 6, ys[2] + bh - 6
p.append(f'<path d="M{xb},{y_a} L{xb - 8},{y_a} L{xb - 8},{y_b} L{xb},{y_b}" class="accent-stroke" stroke-width="1.5"/>')
p.append(f'<text x="{xb - 16}" y="{(y_a + y_b) / 2 - 6:.1f}" text-anchor="end" class="label">equal for sequences</text>')
p.append(f'<text x="{xb - 16}" y="{(y_a + y_b) / 2 + 10:.1f}" text-anchor="end" class="label">that are not high</text>')
p.append('</svg>')
out['hierarchy'] = ''.join(p)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
