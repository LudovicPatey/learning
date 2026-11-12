# Generates the inline SVG figures of the course on notions of randomness.
# Usage: python3 scripts/figures/randomness-notions.py out.json
# Paste each figure into the lesson that uses it:
#   sections        -> relative-randomness.md
#   notions-map     -> schnorr-kurtz.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
from fractions import Fraction as Fr
out = {}


def mtext(txt, x, y, size=14, anchor='start', cls='math'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{txt}</text>'


def sub(base, s, x, y, size=14, anchor='start'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="math" font-size="{int(size * 0.72)}" dy="4">{s}</tspan></text>')


def interval(s):
    """The dyadic interval [a, b) of the reals whose binary expansion begins with s."""
    a = Fr(int(s, 2), 2 ** len(s)) if s else Fr(0)
    return a, a + Fr(1, 2 ** len(s))


# ---------------------------------------------------------------- sections (relative-randomness)
# An open class W of pairs (X, Y), a finite union of disjoint products of cylinders
# [sigma] x [tau]; under the identification of X (+) Y with (X, Y), the product
# [sigma] x [tau] with |sigma| = |tau| is the cylinder of sigma (+) tau.
rects = [('00', '1'), ('01', '11'), ('010', '0'), ('1', '000'), ('110', '1'), ('111', '01')]
q = Fr(1, 2)
A_col = '011'          # the column of the oracle A drawn as a vertical line
level = 3
cols = [format(i, f'0{level}b') for i in range(2 ** level)]


def section(col):
    return sum((Fr(1, 2 ** len(t)) for s, t in rects if col.startswith(s)), Fr(0))


sec = {c: section(c) for c in cols}
total = sum(sec.values()) / len(cols)
assert total == sum(Fr(1, 2 ** (len(s) + len(t))) for s, t in rects)   # Fubini on this example
assert sum(Fr(1, len(cols)) for c in cols if sec[c] > q) <= total / q  # Markov

x0, y0, side = 50, 22, 210            # left panel: the unit square, Y upwards
X = lambda v: x0 + float(v) * side
Y = lambda v: y0 + side - float(v) * side
p = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Left: an open class W in the unit square of pairs (X, Y), a union of rectangles, with the section W_A on a vertical line at X = A and, on the horizontal axis, the oracles X whose section has measure greater than q. Right: the measure of the section as a function of X, a step function whose integral is the measure of W, with the level q">']
p.append(f'<rect x="{x0}" y="{y0}" width="{side}" height="{side}" class="cell"/>')
for s, t in rects:
    a, b = interval(s)
    c, d = interval(t)
    p.append(f'<rect x="{X(a):.1f}" y="{Y(d):.1f}" width="{X(b) - X(a):.1f}" height="{Y(c) - Y(d):.1f}" class="head-cell"/>')
p.append(mtext('W', X(Fr(1, 8)), Y(Fr(3, 4)) + 5, 16, 'middle'))
# the section at A
a, b = interval(A_col)
xa = X((a + b) / 2)
p.append(f'<line x1="{xa:.1f}" y1="{y0 - 6}" x2="{xa:.1f}" y2="{y0 + side + 6}" class="ink-stroke" stroke-width="1" stroke-dasharray="3 3"/>')
for s, t in rects:
    if A_col.startswith(s):
        c, d = interval(t)
        p.append(f'<line x1="{xa:.1f}" y1="{Y(c):.1f}" x2="{xa:.1f}" y2="{Y(d):.1f}" class="ink-stroke" stroke-width="3.2"/>')
p.append(sub('W', 'A', xa + 7, Y(Fr(7, 8)) + 5, 15))
p.append(mtext('A', xa, y0 + side + 20, 14, 'middle'))
# the oracles with a large section, on the X axis
ybar = y0 + side + 34
for c in cols:
    if sec[c] > q:
        a, b = interval(c)
        p.append(f'<line x1="{X(a):.1f}" y1="{ybar}" x2="{X(b):.1f}" y2="{ybar}" class="accent-stroke" stroke-width="4"/>')
p.append(f'<line x1="{x0}" y1="{ybar}" x2="{x0 + side}" y2="{ybar}" class="axis"/>')
p.append(f'<text x="{x0 + side / 2:.1f}" y="{ybar + 18}" text-anchor="middle" class="label">the oracles <tspan class="math">X</tspan> with λ(<tspan class="math">W</tspan><tspan class="math" font-size="9" dy="3">X</tspan><tspan dy="-3">) &gt; </tspan><tspan class="math">q</tspan></text>')
p.append(mtext('X', x0 + side + 10, y0 + side + 5, 14))
p.append(mtext('Y', x0 - 16, y0 + 10, 14))
# right panel: the measure of the sections
rx0, ry0, rw, rh = 340, 22, 220, 210
RX = lambda v: rx0 + float(v) * rw
RY = lambda v: ry0 + rh - float(v) * rh
for c in cols:
    a, b = interval(c)
    cls = 'head-cell' if sec[c] > q else 'cell'
    p.append(f'<rect x="{RX(a):.1f}" y="{RY(sec[c]):.1f}" width="{RX(b) - RX(a):.1f}" height="{RY(0) - RY(sec[c]):.1f}" class="{cls}"/>')
p.append(f'<line x1="{rx0}" y1="{ry0 + rh}" x2="{rx0 + rw}" y2="{ry0 + rh}" class="axis"/>')
p.append(f'<line x1="{rx0}" y1="{ry0 + rh}" x2="{rx0}" y2="{ry0 - 4}" class="axis"/>')
p.append(f'<line x1="{rx0}" y1="{RY(q):.1f}" x2="{rx0 + rw}" y2="{RY(q):.1f}" class="ink-stroke" stroke-width="1" stroke-dasharray="4 3"/>')
p.append(mtext('q', rx0 - 8, RY(q) + 5, 14, 'end'))
p.append(mtext('1', rx0 - 8, RY(1) + 5, 13, 'end', 'mrm'))
p.append(mtext('X', rx0 + rw + 10, ry0 + rh + 5, 14))
a, b = interval(A_col)
p.append(mtext('A', RX((a + b) / 2), ry0 + rh + 20, 14, 'middle'))
p.append(f'<text x="{rx0 + rw / 2:.1f}" y="{ry0 + rh + 52}" text-anchor="middle" class="label">λ(<tspan class="math">W</tspan><tspan class="math" font-size="9" dy="3">X</tspan><tspan dy="-3">) as a function of </tspan><tspan class="math">X</tspan>; the area is λ(<tspan class="math">W</tspan>)</text>')
p.append('</svg>')
out['sections'] = ''.join(p)

# ---------------------------------------------------------------- notions map (schnorr-kurtz)
boxes = [
    ('2-random', 'Martin-Löf random relative to ∅′'),
    ('weakly 2-random', 'in no null Π⁰₂ class'),
    ('Martin-Löf random', 'passes every Martin-Löf test'),
    ('computably random', 'no computable martingale succeeds'),
    ('Schnorr random', 'passes every Schnorr test'),
    ('Kurtz random', 'in no null Π⁰₁ class'),
]
notes = [
    'strict: computably dominated random sequences',
    'strict: Ω, and every Δ⁰₂ random sequence',
    'strict: a Δ⁰₂ computably random sequence',
    'strict: admitted (in every high degree)',
    'strict: weakly 1-generic sequences',
]
bx, bw, bh, gap, top = 150, 230, 42, 26, 14
H = top + len(boxes) * bh + (len(boxes) - 1) * gap + 14
p = [f'<svg class="fig" viewBox="0 0 600 {H}" width="600" role="img" aria-label="Six notions of randomness from top to bottom: 2-random, weakly 2-random, Martin-Löf random, computably random, Schnorr random, Kurtz random, joined by implication arrows with the reason why each implication is strict. A bracket on the left marks that Martin-Löf, computable and Schnorr randomness coincide on sequences that are not high; a bracket on the right marks that weak 2-randomness and the four notions below it coincide on computably dominated sequences, where 2-randomness never holds">']
p.append('<defs><marker id="rn-map-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs>')
ys = []
for i, (name, cond) in enumerate(boxes):
    y = top + i * (bh + gap)
    ys.append(y)
    p.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="4" class="cell"/>')
    p.append(f'<text x="{bx + 12}" y="{y + 18}" font-size="13">{name}</text>')
    p.append(f'<text x="{bx + 12}" y="{y + 34}" class="label">{cond}</text>')
for i, note in enumerate(notes):
    ya = ys[i] + bh
    yb_ = ys[i + 1]
    xm = bx + 30
    p.append(f'<line x1="{xm}" y1="{ya + 2}" x2="{xm}" y2="{yb_ - 3}" class="ink-stroke" stroke-width="1.3" marker-end="url(#rn-map-arrow)"/>')
    p.append(f'<text x="{xm + 10}" y="{(ya + yb_) / 2 + 4:.1f}" class="label">{note}</text>')
# left bracket: Martin-Löf, computable, Schnorr coincide outside the high degrees
xb = bx - 12
y_a, y_b = ys[2] + 6, ys[4] + bh - 6
p.append(f'<path d="M{xb},{y_a} L{xb - 8},{y_a} L{xb - 8},{y_b} L{xb},{y_b}" class="accent-stroke" stroke-width="1.5"/>')
p.append(f'<text x="{xb - 16}" y="{(y_a + y_b) / 2 - 6:.1f}" text-anchor="end" class="label">equal on sequences</text>')
p.append(f'<text x="{xb - 16}" y="{(y_a + y_b) / 2 + 10:.1f}" text-anchor="end" class="label">that are not high</text>')
# right bracket: weak 2 down to Kurtz coincide on computably dominated sequences;
# its ends run at the height of the boxes, so they cross none of the notes
xr = 556
y_a, y_b = ys[1] + 6, ys[5] + bh - 6
p.append(f'<path d="M{bx + bw + 6},{y_a} L{xr},{y_a} L{xr},{y_b} L{bx + bw + 6},{y_b}" class="accent-stroke" stroke-width="1.5"/>')
ym = (y_a + y_b) / 2
p.append(f'<text x="{xr + 16}" y="{ym:.1f}" text-anchor="middle" transform="rotate(90 {xr + 16} {ym:.1f})" class="label">equal on computably dominated sequences</text>')
p.append('</svg>')
out['notions-map'] = ''.join(p)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
