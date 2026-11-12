# Generates the inline SVG figures of the course Computable analysis.
# Usage: python3 scripts/figures/computable-analysis.py out.json
# Paste each figure into the lesson that uses it:
#   use-continuity        -> type-two-computability.md
#   decimal-one           -> representations.md
#   prefix-interval       -> real-functions.md
#   lebesgue-number       -> continuous-functions.md
#   closed-choice-tree    -> closed-sets-and-choice.md
#   ivt-polygons          -> intermediate-value-theorem.md
# The output is deterministic.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def label(t, x, y, anchor='start'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="label">{t}</text>'


def math(t, x, y, size=15, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{t}</text>'


def mrm(t, x, y, size=13, anchor='middle', extra=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="mrm{extra}" font-size="{size}">{t}</text>'


def sub(base, s, x, y, size=15, anchor='middle'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size * 0.68)}" dy="4">{s}</tspan></text>')


def fmt(v):
    return f'{v:.1f}'


# ---------------------------------------------------------------- continuity of a type-2 computation
# F(p)(n) = p(n) + p(n+1); p and q agree below u = 5, so F(p) and F(q) agree below 4.
p = [3, 1, 4, 1, 5, 9, 2, 6, 5]
q = [3, 1, 4, 1, 5, 0, 0, 7, 1]
Fp = [p[i] + p[i + 1] for i in range(8)]
Fq = [q[i] + q[i + 1] for i in range(8)]
u, n_agree = 5, 4
W = 30
s = ['<svg class="fig" viewBox="0 0 640 250" width="640" role="img" aria-label="Two inputs p and q agree on their first five values; the function F(p)(n) = p(n) + p(n+1) gives outputs that agree on their first four values">',
     '<defs>' + marker('ah-cont2', 'muted-fill') + '</defs>']


def row(vals, x0, y, name, nhl, cls_hl, cls_rest, nshow):
    r = [math(name, x0 - 14, y + 20, 16, 'end')]
    for i in range(nshow):
        cl = cls_hl if i < nhl else cls_rest
        r.append(f'<rect x="{x0 + i * W}" y="{y}" width="{W}" height="30" class="{cl}"/>')
        r.append(mrm(str(vals[i]), x0 + i * W + W / 2, y + 20, 15))
    r.append(mrm('⋯', x0 + nshow * W + 12, y + 20, 15, extra=' muted'))
    return r


xin, xout = 50, 380
s += row(p, xin, 50, 'p', u, 'cell head-cell', 'cell', 8)
s += row(q, xin, 130, 'q', u, 'cell head-cell', 'cell', 8)
s += row(Fp, xout, 50, 'F<tspan class="mrm">(</tspan>p<tspan class="mrm">)</tspan>', n_agree, 'cell head-cell', 'cell', 6)
s += row(Fq, xout, 130, 'F<tspan class="mrm">(</tspan>q<tspan class="mrm">)</tspan>', n_agree, 'cell head-cell', 'cell', 6)
for i in range(8):
    s.append(mrm(str(i), xin + i * W + W / 2, 42, 11, extra=' muted'))
for i in range(6):
    s.append(mrm(str(i), xout + i * W + W / 2, 42, 11, extra=' muted'))
s.append(f'<path d="M{xin},{94} L{xin},{102} L{xin + u * W},{102} L{xin + u * W},{94}" class="accent-stroke" stroke-width="1.4"/>')
s.append(label('p ↾ 5 = q ↾ 5', xin + u * W / 2, 120, 'middle'))
s.append(f'<path d="M{xout},{94} L{xout},{102} L{xout + n_agree * W},{102} L{xout + n_agree * W},{94}" class="accent-stroke" stroke-width="1.4"/>')
s.append(label('F(p) ↾ 4 = F(q) ↾ 4', xout + n_agree * W / 2, 120, 'middle'))
s.append(f'<line x1="{xin + 8 * W + 26}" y1="65" x2="{xout - 60}" y2="65" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-cont2)"/>')
s.append(f'<line x1="{xin + 8 * W + 26}" y1="145" x2="{xout - 60}" y2="145" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-cont2)"/>')
s.append(label('Φ', (xin + 8 * W + 26 + xout - 60) / 2, 58, 'middle'))
s.append(label('Φ', (xin + 8 * W + 26 + xout - 60) / 2, 138, 'middle'))
s.append(label('The output F(p)(n) = p(n) + p(n + 1) is computed with use n + 2: the first four outputs read only p ↾ 5,', 320, 205, 'middle'))
s.append(label('so every input that agrees with p below 5 has the same first four outputs.', 320, 225, 'middle'))
s.append('</svg>')
out['use-continuity'] = ''.join(s)

# ---------------------------------------------------------------- the decimal representation at 1
X0, X1 = 60, 580
lo, hi = 0.96, 1.04


def pxd(x):
    return X0 + (x - lo) / (hi - lo) * (X1 - X0)


s = ['<svg class="fig" viewBox="0 0 640 200" width="640" role="img" aria-label="Around the real 1, every neighborhood contains reals below 1, whose decimal expansions begin with 0, and reals above 1, whose decimal expansions begin with 1">']
y = 90
s.append(f'<line x1="{X0 - 10}" y1="{y}" x2="{X1 + 10}" y2="{y}" class="axis"/>')
for t in [0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.03]:
    s.append(f'<line x1="{fmt(pxd(t))}" y1="{y - 4}" x2="{fmt(pxd(t))}" y2="{y + 4}" class="ink-stroke" stroke-width="1"/>')
    s.append(mrm(f'{t:.2f}', pxd(t), y + 20, 12))
d = 0.012
s.append(f'<rect x="{fmt(pxd(1 - d))}" y="{y - 30}" width="{fmt(pxd(1 + d) - pxd(1 - d))}" height="18" class="cell head-cell"/>')
s.append(label('reals with a name extending the prefix', pxd(1), y - 38, 'middle'))
s.append(f'<circle cx="{fmt(pxd(1))}" cy="{y}" r="4" class="accent-fill"/>')
s.append(f'<line x1="{fmt(pxd(lo + 0.002))}" y1="{y + 40}" x2="{fmt(pxd(1) - 3)}" y2="{y + 40}" class="muted-stroke" stroke-width="3"/>')
s.append(f'<line x1="{fmt(pxd(1) + 3)}" y1="{y + 40}" x2="{fmt(pxd(hi - 0.002))}" y2="{y + 40}" class="accent-stroke" stroke-width="3"/>')
s.append(label('y &lt; 1: integer part 0', pxd(0.98), y + 60, 'middle'))
s.append(label('y &gt; 1: integer part 1', pxd(1.02), y + 60, 'middle'))
s.append(label('1 has the two decimal names 0.999… and 1.000…', pxd(1), y + 88, 'middle'))
s.append('</svg>')
out['decimal-one'] = ''.join(s)

# ---------------------------------------------------------------- U_sigma for a prefix of a Cauchy name
qs = [1.0, 0.5, 0.75, 0.625]
lo, hi = -0.1, 2.1
X0, X1 = 70, 590


def pxu(x):
    return X0 + (x - lo) / (hi - lo) * (X1 - X0)


s = ['<svg class="fig" viewBox="0 0 640 260" width="640" role="img" aria-label="The open intervals of radius 2 to the minus k around the first four terms of a Cauchy name, and their intersection U sigma">']
for k, qk in enumerate(qs):
    yy = 30 + k * 38
    a, b = qk - 2 ** (-k), qk + 2 ** (-k)
    s.append(f'<line x1="{fmt(pxu(a))}" y1="{yy}" x2="{fmt(pxu(b))}" y2="{yy}" class="ink-stroke" stroke-width="2"/>')
    s.append(f'<circle cx="{fmt(pxu(a))}" cy="{yy}" r="3.5" class="node"/>')
    s.append(f'<circle cx="{fmt(pxu(b))}" cy="{yy}" r="3.5" class="node"/>')
    s.append(f'<circle cx="{fmt(pxu(qk))}" cy="{yy}" r="3" class="accent-fill"/>')
    s.append(sub('q', str(k), pxu(qk), yy - 9, 14))
    s.append(mrm(f'k = {k}', 30, yy + 5, 12, 'start'))
yy = 30 + 4 * 38 + 6
a, b = 0.5, 0.75
s.append(f'<rect x="{fmt(pxu(a))}" y="{yy - 9}" width="{fmt(pxu(b) - pxu(a))}" height="18" class="cell head-cell"/>')
s.append(sub('U', 'σ', pxu(b) + 10, yy + 5, 15, 'start'))
for t in [0, 0.5, 1, 1.5, 2]:
    s.append(f'<line x1="{fmt(pxu(t))}" y1="{yy + 28}" x2="{fmt(pxu(t))}" y2="{yy + 34}" class="ink-stroke" stroke-width="1"/>')
    s.append(mrm(f'{t:g}', pxu(t), yy + 50, 12))
s.append(f'<line x1="{X0 - 6}" y1="{yy + 31}" x2="{X1 + 6}" y2="{yy + 31}" class="axis"/>')
s.append(f'<line x1="{fmt(pxu(a))}" y1="{yy + 9}" x2="{fmt(pxu(a))}" y2="{yy + 31}" class="muted-stroke" stroke-dasharray="2 3"/>')
s.append(f'<line x1="{fmt(pxu(b))}" y1="{yy + 9}" x2="{fmt(pxu(b))}" y2="{yy + 31}" class="muted-stroke" stroke-dasharray="2 3"/>')
s.append('</svg>')
out['prefix-interval'] = ''.join(s)

# ---------------------------------------------------------------- a finite cover of [0,1] and its Lebesgue number
cover = [(0.1, 0.18), (0.36, 0.14), (0.58, 0.16), (0.84, 0.2)]
X0, X1 = 70, 570


def px1(x):
    return X0 + x * (X1 - X0)


def margin(x):
    return max(r - abs(x - a) for a, r in cover)


s = ['<svg class="fig" viewBox="0 0 640 270" width="640" role="img" aria-label="Four open intervals covering the unit interval, and the function giving the distance from a point to the boundary of the best interval containing it; its minimum is a Lebesgue number of the cover">']
for i, (a, r) in enumerate(cover):
    yy = 30 + (i % 2) * 22
    s.append(f'<line x1="{fmt(px1(max(a - r, -0.08)))}" y1="{yy}" x2="{fmt(px1(min(a + r, 1.08)))}" y2="{yy}" class="accent-stroke" stroke-width="2.5"/>')
    s.append(f'<circle cx="{fmt(px1(a - r))}" cy="{yy}" r="3.5" class="node"/>')
    s.append(f'<circle cx="{fmt(px1(a + r))}" cy="{yy}" r="3.5" class="node"/>')
    s.append(sub('J', str(i), px1(a), yy - 8, 13))
base, scale = 210, 500
s.append(f'<line x1="{X0 - 10}" y1="{base}" x2="{X1 + 20}" y2="{base}" class="axis"/>')
s.append(f'<line x1="{X0}" y1="{base}" x2="{X0}" y2="{base - 120}" class="axis"/>')
pts = ' '.join(f'{px1(i / 400):.1f},{base - scale * margin(i / 400):.1f}' for i in range(401))
s.append(f'<polyline points="{pts}" class="ink-stroke" stroke-width="1.6"/>')
xs = [i / 4000 for i in range(4001)]
xm = min(xs, key=margin)
dm = margin(xm)
s.append(f'<line x1="{X0}" y1="{fmt(base - scale * dm)}" x2="{X1}" y2="{fmt(base - scale * dm)}" class="muted-stroke" stroke-dasharray="4 3"/>')
s.append(f'<circle cx="{fmt(px1(xm))}" cy="{fmt(base - scale * dm)}" r="3.5" class="accent-fill"/>')
s.append(math('δ', X0 - 8, base - scale * dm + 5, 14, 'end'))
s.append(mrm('0', X0, base + 18, 12))
s.append(mrm('1', X1, base + 18, 12))
s.append(label('m(x) = max over i of (r − |x − a|) for the intervals (a − r, a + r) of the cover', 320, 250, 'middle'))
s.append('</svg>')
out['lebesgue-number'] = ''.join(s)

# ---------------------------------------------------------------- the tree of closed choice
J = [(0.4, 0.8), (-1.0, 0.3), (0.85, 2.0)]
A = [(0.3, 0.4), (0.8, 0.85)]
X0, X1 = 70, 570


def px2(x):
    return X0 + x * (X1 - X0)


def covered_closed(a, b, n):
    # a closed interval [a,b] is covered iff every point is in some open interval
    pts = sorted(set([a, b] + [t for iv in J[:n] for t in iv if a <= t <= b]))
    probes = pts + [(pts[i] + pts[i + 1]) / 2 for i in range(len(pts) - 1)]
    return all(any(c < t < d for c, d in J[:n]) for t in probes)


s = ['<svg class="fig" viewBox="0 0 640 300" width="640" role="img" aria-label="Dyadic intervals at levels 0 to 3; those not covered by the first n enumerated intervals are the nodes of the tree. The closed set A lies in the shaded nodes.">']
for n in range(4):
    yy = 22 + n * 34
    s.append(mrm(f'n = {n}', 20, yy + 14, 12, 'start'))
    for k in range(2 ** n):
        a, b = k / 2 ** n, (k + 1) / 2 ** n
        inT = not covered_closed(a, b, n)
        cl = 'cell head-cell' if inT else 'cell'
        s.append(f'<rect x="{fmt(px2(a))}" y="{yy}" width="{fmt(px2(b) - px2(a))}" height="20" class="{cl}"/>')
        nm = ''.join(str((k >> (n - 1 - j)) & 1) for j in range(n)) or 'ε'
        s.append(mrm(nm, (px2(a) + px2(b)) / 2, yy + 14, 11, extra='' if inT else ' muted'))
yy = 175
s.append(f'<line x1="{X0 - 10}" y1="{yy + 70}" x2="{X1 + 10}" y2="{yy + 70}" class="axis"/>')
for t in [0, 0.25, 0.5, 0.75, 1]:
    s.append(f'<line x1="{fmt(px2(t))}" y1="{yy + 66}" x2="{fmt(px2(t))}" y2="{yy + 74}" class="ink-stroke" stroke-width="1"/>')
    s.append(mrm(f'{t:g}', px2(t), yy + 90, 12))
for i, (c, d) in enumerate(J):
    y2 = yy + 10 + i * 16
    s.append(f'<line x1="{fmt(px2(max(c, -0.06)))}" y1="{y2}" x2="{fmt(px2(min(d, 1.06)))}" y2="{y2}" class="muted-stroke" stroke-width="3"/>')
    s.append(sub('J', str(i), (px2(max(c, -0.06)) + px2(min(d, 1.06))) / 2, y2 - 5, 13))
for c, d in A:
    s.append(f'<line x1="{fmt(px2(c))}" y1="{yy + 70}" x2="{fmt(px2(d))}" y2="{yy + 70}" class="accent-stroke" stroke-width="4"/>')
s.append(math('A', px2(0.35), yy + 62, 14))
s.append(math('A', px2(0.775), yy + 62, 14, 'end'))
s.append(label('Shaded: the dyadic intervals of level n not covered by the first n intervals J.', 320, 288, 'middle'))
s.append('</svg>')
out['closed-choice-tree'] = ''.join(s)

# ---------------------------------------------------------------- the polygons g_a of the intermediate value theorem
X0, X1 = 60, 300
YT, YB = 30, 190
s = ['<svg class="fig" viewBox="0 0 640 250" width="640" role="img" aria-label="The polygon g_a through (0, -1), (1/3, a), (2/3, a) and (1, 1): for a = 0 its zeros form the interval [1/3, 2/3], for positive a there is a single zero below 1/3, for negative a a single zero above 2/3">']


def panel(ox, a, title):
    r = []

    def X(x):
        return ox + x * 160

    def Y(v):
        return (YT + YB) / 2 - v * 70

    r.append(f'<line x1="{X(0) - 6}" y1="{Y(0)}" x2="{X(1) + 10}" y2="{Y(0)}" class="axis"/>')
    r.append(f'<line x1="{X(0)}" y1="{Y(1.1)}" x2="{X(0)}" y2="{Y(-1.1)}" class="axis"/>')
    for t, lab in [(1 / 3, '1/3'), (2 / 3, '2/3'), (1, '1')]:
        r.append(f'<line x1="{fmt(X(t))}" y1="{Y(0) - 3}" x2="{fmt(X(t))}" y2="{Y(0) + 3}" class="ink-stroke" stroke-width="1"/>')
        r.append(mrm(lab, X(t), Y(-1.1) + 14, 11))
    pts = [(0, -1), (1 / 3, a), (2 / 3, a), (1, 1)]
    r.append('<polyline points="' + ' '.join(f'{X(x):.1f},{Y(v):.1f}' for x, v in pts) + '" class="ink-stroke" stroke-width="1.8"/>')
    if a == 0:
        r.append(f'<line x1="{fmt(X(1 / 3))}" y1="{Y(0)}" x2="{fmt(X(2 / 3))}" y2="{Y(0)}" class="accent-stroke" stroke-width="4"/>')
    elif a > 0:
        z = (1 / 3) * 1 / (1 + a)
        r.append(f'<circle cx="{fmt(X(z))}" cy="{Y(0)}" r="4" class="accent-fill"/>')
    else:
        z = 2 / 3 + (1 / 3) * (-a) / (1 - a)
        r.append(f'<circle cx="{fmt(X(z))}" cy="{Y(0)}" r="4" class="accent-fill"/>')
    r.append(label(title, X(0.5), 228, 'middle'))
    return r


s += panel(40, 0.0, 'a = 0: zeros [1/3, 2/3]')
s += panel(250, 0.25, 'a > 0: one zero below 1/3')
s += panel(460, -0.25, 'a &lt; 0: one zero above 2/3')
s.append('</svg>')
out['ivt-polygons'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
