# Generates the inline SVG figures of the course on higher randomness.
# Usage: python3 scripts/figures/higher-randomness.py out.json
# Paste each figure into the lesson that uses it:
#   stage-measure          -> pi11-classes.md
#   universal-trimming     -> higher-tests.md
#   majority-vote          -> hyperdegrees.md
#   randomness-hierarchy   -> hyperdegrees.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def omega(x, y, sup, size=15, anchor='middle'):
    """omega_1 with a superscript (CK, X, ...), in KaTeX fonts."""
    sup_cls = 'mrm' if sup == 'CK' else 'math'
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">ω'
            f'<tspan class="mrm" font-size="{int(size * 0.68)}" dy="4">1</tspan>'
            f'<tspan class="{sup_cls}" font-size="{int(size * 0.62)}" dy="-11">{sup}</tspan></text>')


def label(txt, x, y, anchor='start'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="label">{txt}</text>'


# ---------------------------------------------------------------- measures of the stages of a Pi11 class
# The measure of the stage A_alpha as a function of alpha: nondecreasing, with jumps at stages below
# omega_1^CK accumulating at omega_1^CK, and constant afterwards (Sacks-Tanaka).
X0, XCK, X1, Y0 = 110, 360, 570, 220
TOP = 0.8
def ypos(v):
    return Y0 - 160 * v

s = ['<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="The measure of the stage of a Pi11 class as a function of the stage: a nondecreasing step function that reaches the measure of the class at omega one CK and is constant afterwards">']
s.append(f'<line x1="{X0}" y1="{Y0}" x2="{X1 - 30}" y2="{Y0}" class="axis"/>')
s.append(f'<line x1="{X1 - 30}" y1="{Y0}" x2="{X1}" y2="{Y0}" class="axis" stroke-dasharray="2 3"/>')
s.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="40" class="axis"/>')
# dashed level lambda(A)
s.append(f'<line x1="{X0}" y1="{ypos(TOP):.1f}" x2="{X1}" y2="{ypos(TOP):.1f}" class="muted-stroke" stroke-width="1" stroke-dasharray="4 4"/>')
s.append(label('measure', X0 - 8, ypos(TOP) - 3, 'end'))
s.append(label('of the class', X0 - 8, ypos(TOP) + 11, 'end'))
s.append(f'<text x="{X0 - 8}" y="{Y0 + 5}" text-anchor="end" class="mrm" font-size="14">0</text>')
# step function
pts = []
x_prev, v_prev = X0, 0.0
K = 14
for k in range(K):
    x = X0 + (XCK - X0) * (1 - 0.72 ** (k + 1))
    v = TOP * (1 - 0.62 ** (k + 1))
    pts.append((x_prev, v_prev, x))
    x_prev, v_prev = x, v
for (xa, v, xb) in pts:
    s.append(f'<line x1="{xa:.1f}" y1="{ypos(v):.1f}" x2="{xb:.1f}" y2="{ypos(v):.1f}" class="accent-stroke" stroke-width="2"/>')
for i in range(1, len(pts)):
    xa, v, _ = pts[i]
    s.append(f'<line x1="{xa:.1f}" y1="{ypos(pts[i - 1][1]):.1f}" x2="{xa:.1f}" y2="{ypos(v):.1f}" class="accent-stroke" stroke-width="1" stroke-dasharray="2 2"/>')
s.append(f'<line x1="{XCK}" y1="{ypos(TOP):.1f}" x2="{X1}" y2="{ypos(TOP):.1f}" class="accent-stroke" stroke-width="2"/>')
s.append(f'<circle cx="{XCK}" cy="{ypos(TOP):.1f}" r="3.5" class="accent-fill"/>')
# ticks
for x in (X0, XCK):
    s.append(f'<line x1="{x}" y1="{Y0}" x2="{x}" y2="{Y0 + 6}" class="axis"/>')
s.append(f'<line x1="{XCK}" y1="{Y0}" x2="{XCK}" y2="{ypos(TOP):.1f}" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/>')
s.append(f'<text x="{X0}" y="{Y0 + 24}" text-anchor="middle" class="mrm" font-size="14">0</text>')
s.append(omega(XCK, Y0 + 26, 'CK'))
s.append(omega(X1, Y0 + 26, '', anchor='end'))
s.append(label('measure of the stage, as a function of the stage α', X0 + 8, 40))
s.append(label('jumps at countably many stages,', 196, 194))
s.append(label('accumulating at the limit', 196, 210))
s.append(label('no new measure after this point:', XCK + 14, ypos(TOP) + 30))
s.append(label('later members lie in a null class', XCK + 14, ypos(TOP) + 46))
s.append('</svg>')
out['stage-measure'] = ''.join(s)

# ---------------------------------------------------------------- trimming of a component of the universal test
# Strings of V_{e,n} entering at increasing stages, with their measures; the bound 2^-n is 0.40.
strings = [(90, 0.10), (150, 0.08), (215, 0.12), (285, 0.06), (350, 0.09), (420, 0.03), (490, 0.05)]
BOUND = 0.40
XA, XB, YA = 50, 560, 220
def yt(v):
    return YA - 300 * v

s = ['<svg class="fig" viewBox="0 0 600 296" width="600" role="img" aria-label="Strings entering a Pi11 set at increasing stages; the cumulative measure grows by steps; strings entering before the measure exceeds the bound are kept, the others are discarded">']
s.append(f'<line x1="{XA}" y1="{YA}" x2="{XB}" y2="{YA}" class="axis"/>')
s.append(f'<line x1="{XA}" y1="{YA}" x2="{XA}" y2="30" class="axis"/>')
s.append(f'<line x1="{XA}" y1="{yt(BOUND):.1f}" x2="{XB}" y2="{yt(BOUND):.1f}" class="ink-stroke" stroke-width="1" stroke-dasharray="5 4"/>')
s.append(f'<text x="{XA - 6}" y="{yt(BOUND) + 5:.1f}" text-anchor="end" class="mrm" font-size="13">2<tspan font-size="9" dy="-7">−</tspan><tspan class="math" font-size="9">n</tspan></text>')
cum = 0.0
x_prev = XA
for i, (x, m) in enumerate(strings):
    new = cum + m
    kept = new <= BOUND + 1e-9
    s.append(f'<line x1="{x_prev}" y1="{yt(cum):.1f}" x2="{x}" y2="{yt(cum):.1f}" class="accent-stroke" stroke-width="1.6"/>')
    s.append(f'<line x1="{x}" y1="{yt(cum):.1f}" x2="{x}" y2="{yt(new):.1f}" class="accent-stroke" stroke-width="1.6"/>')
    cls = 'accent-fill' if kept else 'muted-stroke'
    extra = '' if kept else ' stroke-width="1.4"'
    s.append(f'<circle cx="{x}" cy="{YA}" r="5" class="{cls}"{extra}/>')
    s.append(f'<text x="{x}" y="{YA + 24}" text-anchor="middle" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="4">{i + 1}</tspan></text>')
    cum, x_prev = new, x
s.append(f'<line x1="{x_prev}" y1="{yt(cum):.1f}" x2="{XB}" y2="{yt(cum):.1f}" class="accent-stroke" stroke-width="1.6"/>')
s.append(f'<text x="{XB}" y="{YA + 24}" text-anchor="end" class="math" font-size="14">ρ</text>')
s.append(label('measure of the strings of stage at most ρ', XA + 8, 30))
s.append(label('kept (filled): the measure up to their stage is at most the bound', XA + 8, 272))
s.append(label('discarded (hollow)', XA + 8, 288))
s.append('</svg>')
out['universal-trimming'] = ''.join(s)

# ---------------------------------------------------------------- the majority vote in a cylinder
LX, RX = 90, 420
def px(f):
    return LX + (RX - LX) * f

K_pieces = [(0.00, 0.30), (0.36, 0.60), (0.68, 0.86)]
P_right = [(0.00, 0.33), (0.36, 0.64), (0.68, 0.90), (0.95, 0.97)]
P_wrong = [(0.33, 0.36), (0.64, 0.68), (0.90, 0.95)]
rows = [
    ('[σ]', None, 44),
    ('𝒦 ∩ [σ]', K_pieces, 94),
    ('right', P_right, 144),
    ('wrong', P_wrong, 194),
]
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="A cylinder; the part of the cone class in it occupies more than half; the class of oracles giving the right bit contains it and has relative measure above one half; the class giving the wrong bit is disjoint from it and has relative measure below one half">']
for name, pieces, y in rows:
    s.append(f'<rect x="{LX}" y="{y - 9}" width="{RX - LX}" height="18" class="cell"/>')
    if pieces:
        fill = 'soft-fill' if name != 'wrong' else 'muted-fill'
        if name == 'right':
            fill = 'accent-fill'
        for a, b in pieces:
            s.append(f'<rect x="{px(a):.1f}" y="{y - 9}" width="{px(b) - px(a):.1f}" height="18" class="{fill}"/>')
s.append(f'<text x="{LX - 10}" y="{44 + 5}" text-anchor="end" class="math" font-size="15"><tspan class="mrm">[</tspan>σ<tspan class="mrm">]</tspan></text>')
s.append(label('cone class', LX - 10, 94 + 4, 'end'))
s.append(label('right bit', LX - 10, 144 + 4, 'end'))
s.append(label('wrong bit', LX - 10, 194 + 4, 'end'))
s.append(label('relative measure &gt; 1/2', RX + 12, 94 + 4))
s.append(label('contains it: &gt; 1/2', RX + 12, 144 + 4))
s.append(label('disjoint from it: &lt; 1/2', RX + 12, 194 + 4))
s.append('</svg>')
out['majority-vote'] = ''.join(s)

# ---------------------------------------------------------------- the hierarchy of randomness notions
boxes = [
    'Π¹₁-random',
    'Π¹₁-Martin-Löf random',
    'Δ¹₁-random  =  Σ¹₁-random',
    'n-random for every n',
    'Martin-Löf random',
]
notes = [
    'OMEGA',
    '',
    'Martin-Löf random relative to every hyperarithmetic set',
    '',
    '',
]
seps = [
    'strict: a Π¹₁-Martin-Löf random Z with O ≤h Z',
    'strict: Hjorth and Nies',
    'strict: Ω relative to ∅⁽ω⁾',
    'strict: Ω',
]
BX, BW, BH, GAP, Y = 30, 230, 30, 26, 14
s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Five randomness notions in a column, from Pi11-randomness at the top to Martin-Loef randomness at the bottom, each implying the next; no implication reverses">']
s.append('<defs>' + marker('hr-hier-arrow') + '</defs>')
for i, b in enumerate(boxes):
    y = Y + i * (BH + GAP)
    s.append(f'<rect x="{BX}" y="{y}" width="{BW}" height="{BH}" rx="4" class="cell"/>')
    s.append(f'<text x="{BX + BW / 2}" y="{y + 20}" text-anchor="middle" font-size="14">{b}</text>')
    if notes[i] == 'OMEGA':
        s.append(f'<text x="{BX + BW + 14}" y="{y + 19}" class="label">= Δ¹₁-random and <tspan class="math" font-size="14">ω</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="math" font-size="9" dy="-9">X</tspan><tspan class="mrm" font-size="14" dy="6"> = </tspan><tspan class="math" font-size="14">ω</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="mrm" font-size="9" dy="-9">CK</tspan></text>')
    elif notes[i]:
        s.append(label('= ' + notes[i], BX + BW + 14, y + 19))
    if i < len(boxes) - 1:
        ya, yb = y + BH, y + BH + GAP
        s.append(f'<line x1="{BX + BW / 2}" y1="{ya + 2}" x2="{BX + BW / 2}" y2="{yb - 2}" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/>')
        s.append(label(seps[i], BX + BW / 2 + 12, ya + GAP / 2 + 4))
s.append('</svg>')
out['randomness-hierarchy'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
