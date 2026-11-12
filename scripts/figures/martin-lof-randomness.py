# Generates the inline SVG figures of the course on Martin-Löf randomness.
# Usage: python3 scripts/figures/martin-lof-randomness.py out.json
# Paste each figure into the lesson that uses it:
#   prefix-free-generator   -> measure.md
#   solovay-counting        -> solovay-tests.md
#   excess-plot             -> levin-schnorr.md
#   kucera-gacs-coding      -> randomness-and-degrees.md
# The output is deterministic: every loop runs over ordered data.
import json, math, sys
out = {}

L, R = 150, 580  # horizontal extent of Cantor space, drawn as the unit interval


def interval(s, left=L, right=R):
    """Dyadic interval [0.s, 0.s + 2^-|s|] of the string s, scaled into [left, right]."""
    d = len(s)
    idx = int(s, 2) if s else 0
    w = (right - left) / (2 ** d)
    return left + idx * w, left + (idx + 1) * w


def mtext(txt, x, y, size=14, anchor='start', cls='math'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{txt}</text>'


def sub(base, s, x, y, size=14, anchor='start'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size * 0.7)}" dy="4">{s}</tspan></text>')


# ---------------------------------------------------------------- prefix-free generator (lemma 1.x)
# W is enumerated as 01, 0, 0110, 11; the construction of the lemma produces W' = {01, 00, 11}.
W = ['01', '0', '0110', '11']
Wp = []
rows = []
for sig in W:
    Lmax = max([len(sig)] + [len(t) for t in Wp])
    new = []
    for i in range(2 ** (Lmax - len(sig))):
        ext = format(i, f'0{Lmax - len(sig)}b') if Lmax > len(sig) else ''
        tau = sig + ext
        if not any(tau.startswith(p) for p in Wp):
            new.append(tau)
    rows.append((sig, list(Wp), new))
    Wp = Wp + new

row_h = 52
top = 30
s = [f'<svg class="fig" viewBox="0 0 600 {top + row_h * len(rows) + 34}" width="600" role="img" '
     'aria-label="Four stages of the construction of a prefix-free generator: at each stage the cylinder of the new string '
     'of W is shown above the current prefix-free set W prime, with the strings added at that stage highlighted">']
s.append(mtext('0', L, top - 14, 12, 'middle', 'mrm'))
s.append(mtext('1', R, top - 14, 12, 'middle', 'mrm'))
for i, (sig, old, new) in enumerate(rows):
    y = top + i * row_h
    s.append(f'<text x="10" y="{y + 12}" class="label">stage {i}</text>')
    s.append(sub('σ', str(i), 10, y + 34, 14))
    s.append(mtext(f'= {sig}', 30, y + 34, 13, 'start', 'mrm'))
    a, b = interval(sig)
    s.append(f'<line x1="{a + 1:.1f}" y1="{y + 4}" x2="{b - 1:.1f}" y2="{y + 4}" class="ink-stroke" stroke-width="2.2"/>')
    s.append(f'<line x1="{a + 1:.1f}" y1="{y}" x2="{a + 1:.1f}" y2="{y + 8}" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<line x1="{b - 1:.1f}" y1="{y}" x2="{b - 1:.1f}" y2="{y + 8}" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<rect x="{L}" y="{y + 16}" width="{R - L}" height="22" class="cell"/>')
    for t in sorted(old):
        a, b = interval(t)
        s.append(f'<rect x="{a + 1:.1f}" y="{y + 17}" width="{b - a - 2:.1f}" height="20" class="soft-fill"/>')
        s.append(mtext(t, (a + b) / 2, y + 31, 11, 'middle', 'mrm'))
    for t in new:
        a, b = interval(t)
        s.append(f'<rect x="{a + 1:.1f}" y="{y + 17}" width="{b - a - 2:.1f}" height="20" class="head-cell"/>')
        s.append(mtext(t, (a + b) / 2, y + 31, 11, 'middle', 'mrm'))
    if not new:
        s.append(f'<text x="{(L + R) / 2 + 80:.1f}" y="{y + 31}" class="label">nothing added</text>')
yl = top + row_h * len(rows) + 6
s.append(f'<line x1="{L}" y1="{yl}" x2="{L + 24}" y2="{yl}" class="ink-stroke" stroke-width="2.2"/>')
s.append(f'<text x="{L + 30}" y="{yl + 4}" class="label">cylinder of σ</text>')
s.append(f'<rect x="{L + 130}" y="{yl - 7}" width="22" height="14" class="soft-fill"/>')
s.append(f'<text x="{L + 158}" y="{yl + 4}" class="label">W′ before the stage</text>')
s.append(f'<rect x="{L + 290}" y="{yl - 7}" width="22" height="14" class="head-cell"/>')
s.append(f'<text x="{L + 318}" y="{yl + 4}" class="label">strings added</text>')
s.append('</svg>')
out['prefix-free-generator'] = ''.join(s)

# ---------------------------------------------------------------- Solovay tests: counting multiplicities
# Four clopen classes S_0, ..., S_3, unions of cylinders of length 4.  With 2^k = 2, the
# strings of D_s are those whose cylinder lies in at least two classes.
S = [
    ['0000', '0001', '0010', '0011', '1100', '1101'],
    ['0010', '0011', '0100', '1000', '1001'],
    ['0011', '1001', '1110', '1111'],
    ['0101', '1101'],
]
cells = [format(i, '04b') for i in range(16)]
SR = 530  # right end of the bars, leaving room for the measures
count = {c: sum(1 for cl in S if c in cl) for c in cells}
row_h = 30
top = 24
h = top + row_h * (len(S) + 2) + 30
s = [f'<svg class="fig" viewBox="0 0 600 {h}" width="600" role="img" '
     'aria-label="Four clopen classes drawn as unions of cylinders of length 4; below them, the number of classes containing '
     'each cylinder, and the cylinders counted at least twice, which form D">']
s.append(mtext('0', L, top - 8, 12, 'middle', 'mrm'))
s.append(mtext('1', SR, top - 8, 12, 'middle', 'mrm'))
for n, cl in enumerate(S):
    y = top + n * row_h
    s.append(sub('S', str(n), 20, y + 16, 15))
    s.append(f'<rect x="{L}" y="{y}" width="{SR - L}" height="22" class="cell"/>')
    for c in cl:
        a, b = interval(c, L, SR)
        s.append(f'<rect x="{a + 1:.1f}" y="{y + 1}" width="{b - a - 2:.1f}" height="20" class="soft-fill"/>')
    s.append(f'<text x="{SR + 8}" y="{y + 15}" class="label">{len(cl)}/16</text>')
y = top + len(S) * row_h + 4
s.append(f'<text x="20" y="{y + 15}" class="label">multiplicity</text>')
for c in cells:
    a, b = interval(c, L, SR)
    s.append(mtext(str(count[c]), (a + b) / 2, y + 15, 12, 'middle', 'mrm'))
y += row_h
s.append(f'<text x="20" y="{y + 15}" class="label">D (at least 2)</text>')
s.append(f'<rect x="{L}" y="{y}" width="{SR - L}" height="22" class="cell"/>')
for c in cells:
    if count[c] >= 2:
        a, b = interval(c, L, SR)
        s.append(f'<rect x="{a + 1:.1f}" y="{y + 1}" width="{b - a - 2:.1f}" height="20" class="head-cell"/>')
nD = sum(1 for c in cells if count[c] >= 2)
total = sum(count.values())
s.append(f'<text x="{SR + 8}" y="{y + 15}" class="label">{nD}/16</text>')
s.append(f'<text x="{L}" y="{y + 44}" class="label">sum of the measures: {total}/16; measure of D: {nD}/16 ≤ ({total}/16)/2</text>')
s.append('</svg>')
out['solovay-counting'] = ''.join(s)

# ---------------------------------------------------------------- Levin–Schnorr: schematic excess plot
W0, H0 = 600, 280
x0, x1 = 60, 570
yzero = 150
scale = 11  # pixels per unit of K(Z|n) - n
N = 200


def px(n):
    return x0 + (x1 - x0) * n / N


def py(v):
    return yzero - v * scale


def rnd(n):
    # schematic: tends to infinity like log n, with bounded oscillations, never below -3
    return 1.6 * math.log2(n + 2) - 3.5 + 1.4 * math.sin(n / 3.1) * math.exp(-n / 260)


def nonrnd(n):
    # schematic: drops below -c for larger and larger c (dips at lengths 40, 90, 160)
    def base(m):
        return 1.1 * math.log2(m + 2) - 2.5
    v = base(n)
    for centre, target in ((40, -4.5), (95, -7), (165, -9.5)):
        v -= (base(centre) - target) * math.exp(-((n - centre) / 6.0) ** 2)
    return v


s = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="Schematic plot of K of the first n bits minus n against n: for a random sequence the curve stays above minus c '
     'and tends to infinity; for a non-random sequence it falls below every horizontal line">']
s.append(f'<line x1="{x0}" y1="{yzero}" x2="{x1 + 10}" y2="{yzero}" class="axis"/>')
s.append(f'<line x1="{x0}" y1="16" x2="{x0}" y2="{H0 - 12}" class="axis"/>')
s.append(mtext('n', x1 + 14, yzero + 5, 14))
s.append(mtext('0', x0 - 8, yzero + 5, 12, 'end', 'mrm'))
yc = py(-3)
s.append(f'<line x1="{x0}" y1="{yc:.1f}" x2="{x1}" y2="{yc:.1f}" class="muted-stroke" stroke-dasharray="4 4"/>')
s.append(mtext('−c', x0 - 8, yc + 5, 13, 'end', 'math'))
pts = ' '.join(f'{px(n):.1f},{py(rnd(n)):.1f}' for n in range(0, N + 1))
s.append(f'<polyline points="{pts}" class="accent-stroke" stroke-width="2"/>')
pts = ' '.join(f'{px(n):.1f},{py(nonrnd(n)):.1f}' for n in range(0, N + 1))
s.append(f'<polyline points="{pts}" class="ink-stroke" stroke-width="1.4" stroke-dasharray="5 3"/>')
s.append(f'<text x="{px(200):.1f}" y="{py(rnd(200)) - 12:.1f}" class="label" text-anchor="end">random: bounded below, tends to +∞</text>')
s.append(f'<text x="{px(130):.1f}" y="{py(-9):.1f}" class="label" text-anchor="end">not random: below −c for every c</text>')
s.append(f'<text x="{x0 + 6}" y="26" class="label">K(Z↾n) − n (schematic)</text>')
s.append('</svg>')
out['excess-plot'] = ''.join(s)

# ---------------------------------------------------------------- Kučera–Gács coding
# Level 0: sigma_0 is the empty string; its 8 extensions of length m_1, of which the
# accented ones belong to A_0(sigma_0).  X(0) = 1: sigma_1 is the rightmost one.
# Level 1: the 8 extensions of sigma_1 of length m_2 (drawn with the same width);
# X(1) = 0: sigma_2 is the leftmost element of A_1(sigma_1).
W0, H0 = 600, 320
s = [f'<svg class="fig" viewBox="0 0 {W0} {H0}" width="{W0}" role="img" '
     'aria-label="Two steps of the Kučera–Gács coding: among the extensions of sigma_n of the next length, those of large '
     'relative measure are marked; sigma_n+1 is the leftmost of them if X(n) is 0 and the rightmost if X(n) is 1">']
s.append('<defs><marker id="mlr-kg-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs>')
levels = [
    {'y': 70, 'parent_x': 300, 'A': [1, 4, 6], 'bit': 1, 'name': '0'},
    {'y': 210, 'A': [2, 3, 7], 'bit': 0, 'name': '1'},
]
cw, gap = 50, 6
row_w = 8 * cw + 7 * gap
left = (W0 - row_w) / 2
parent = (300, 22)
s.append(f'<circle cx="{parent[0]}" cy="{parent[1]}" r="5" class="node"/>')
s.append(sub('σ', '0', parent[0] + 12, parent[1] + 5, 15))
for li, lev in enumerate(levels):
    y = lev['y']
    xs = [left + i * (cw + gap) for i in range(8)]
    for i, x in enumerate(xs):
        s.append(f'<line x1="{parent[0]:.1f}" y1="{parent[1] + 5}" x2="{x + cw / 2:.1f}" y2="{y}" class="muted-stroke" stroke-width="0.8"/>')
    for i, x in enumerate(xs):
        cls = 'head-cell' if i in lev['A'] else 'cell'
        s.append(f'<rect x="{x:.1f}" y="{y}" width="{cw}" height="24" class="{cls}"/>')
    chosen = max(lev['A']) if lev['bit'] == 1 else min(lev['A'])
    cx = xs[chosen] + cw / 2
    other = min(lev['A']) if lev['bit'] == 1 else max(lev['A'])
    s.append(f'<text x="{xs[other] + cw / 2:.1f}" y="{y + 40}" text-anchor="middle" class="label">{"leftmost" if lev["bit"] == 1 else "rightmost"}</text>')
    s.append(f'<text x="{cx:.1f}" y="{y + 40}" text-anchor="middle" class="label">{"rightmost" if lev["bit"] == 1 else "leftmost"}</text>')
    s.append(f'<line x1="{cx:.1f}" y1="{y + 46}" x2="{cx:.1f}" y2="{y + 64}" class="accent-stroke" stroke-width="1.6" marker-end="url(#mlr-kg-arrow)"/>')
    s.append(sub('σ', str(li + 1), cx + 8, y + 62, 15))
    s.append(f'<text x="{left + row_w + 8:.1f}" y="{y + 16}" class="label">X({lev["name"]}) = {lev["bit"]}</text>')
    parent = (cx, y + 70)
s.append(f'<rect x="{left:.1f}" y="{H0 - 18}" width="22" height="14" class="head-cell"/>')
s.append(f'<text x="{left + 28:.1f}" y="{H0 - 7}" class="label">extensions τ with large relative measure: the set A</text>')
s.append('</svg>')
out['kucera-gacs-coding'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
