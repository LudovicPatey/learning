# Generates the inline SVG figures of the course Oracles and Turing degrees.
# Usage: python3 scripts/figures/turing-degrees.py out.json
import json, sys
out = {}

def sub(base, s, x, y, size=16, anchor='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

# ---------------------------------------------------------------- oracle machine and use
s = ['<svg class="fig" viewBox="0 0 600 254" width="600" role="img" aria-label="An oracle machine: a work tape, a read-only oracle tape holding the bits of X, and a finite control; the cells read form the use">']
w = 34
# work tape
s.append('<text x="10" y="44" class="label">work tape</text>')
work = ['⊔', '1', '1', '1', '⊔', '1', '1', '⊔', '⊔', '⊔']
for i, c in enumerate(work):
    x = 120 + i * w
    s.append(f'<rect x="{x}" y="24" width="{w}" height="{w}" class="{"cell head-cell" if i == 3 else "cell"}"/>')
    s.append(f'<text x="{x + w/2}" y="47" text-anchor="middle" class="mrm{" muted" if c == "⊔" else ""}" font-size="16">{c}</text>')
s.append(f'<text x="{120 + len(work)*w + 8}" y="47" class="mrm muted" font-size="16">⋯</text>')
# oracle tape
s.append('<text x="10" y="196" class="label">oracle tape</text>')
bits = '0110100101'
for i, b in enumerate(bits):
    x = 120 + i * w
    read = i < 5
    s.append(f'<rect x="{x}" y="176" width="{w}" height="{w}" class="{"cell head-cell" if i == 4 else "cell"}"/>')
    s.append(f'<text x="{x + w/2}" y="199" text-anchor="middle" class="mrm{"" if read else " muted"}" font-size="16">{b}</text>')
    s.append(f'<text x="{x + w/2}" y="226" text-anchor="middle" class="mrm muted" font-size="11">{i}</text>')
s.append(f'<text x="{120 + len(bits)*w + 8}" y="199" class="mrm muted" font-size="16">⋯</text>')
# use bracket
s.append(f'<path d="M122,240 L122,246 L{120 + 5*w - 2},246 L{120 + 5*w - 2},240" class="accent-stroke" stroke-width="1.4"/>')
s.append(f'<text x="{120 + 5*w + 8}" y="248" class="label">cells read so far: the use</text>')
# finite control
cx = 120 + 3 * w + w / 2
s.append(f'<rect x="{cx - 60}" y="90" width="150" height="54" rx="8" class="soft-fill accent-stroke" stroke-width="1.3"/>')
s.append(f'<text x="{cx + 15}" y="113" text-anchor="middle" class="label">finite control</text>')
s.append(sub('q', '2', cx + 15, 134, 18))
s.append(f'<line x1="{cx}" y1="58" x2="{cx}" y2="90" class="accent-stroke" stroke-width="1.4" stroke-dasharray="4 3"/>')
ox = 120 + 4 * w + w / 2
s.append(f'<line x1="{ox}" y1="144" x2="{ox}" y2="176" class="accent-stroke" stroke-width="1.4" stroke-dasharray="4 3"/>')
s.append('<text x="346" y="112" class="label">δ(q, a, b) = (q′, a′, D, D′):</text>')
s.append('<text x="346" y="128" class="label">read a on the work tape and b = X(k)</text>')
s.append('<text x="346" y="144" class="label">on the oracle tape; write a′, move both heads</text>')
s.append('</svg>')
out['oracle-machine'] = ''.join(s)

# ---------------------------------------------------------------- a Delta^0_2 approximation
rows = ['1001100', '1101000', '1101010', '0101010', '0111010', '0110010', '0110011', '0110011']
c, x0, y0 = 30, 90, 40
s = ['<svg class="fig" viewBox="0 0 420 330" width="420" role="img" aria-label="A table of approximations A_s; each column eventually stops changing">']
for j in range(len(rows[0])):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{y0 - 12}" text-anchor="middle" class="math muted" font-size="13">{j}</text>')
s.append(f'<text x="{x0 - 50}" y="{y0 - 12}" class="label">stage</text>')
final = rows[-1]
# last stage at which column j changes
last_change = []
for j in range(len(final)):
    lc = 0
    for t in range(1, len(rows)):
        if rows[t][j] != rows[t-1][j]:
            lc = t
    last_change.append(lc)
for t, r in enumerate(rows):
    y = y0 + c * t
    s.append(sub('A', str(t), x0 - 30, y + 20, 15))
    for j, b in enumerate(r):
        changed = t > 0 and rows[t-1][j] != b
        settled = t >= last_change[j]
        cls = 'cell head-cell' if changed else 'cell'
        s.append(f'<rect x="{x0 + c*j}" y="{y}" width="{c}" height="{c}" class="{cls}"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{y + 20}" text-anchor="middle" class="mrm{"" if settled else " muted"}" font-size="15">{b}</text>')
yy = y0 + c * len(rows) + 22
s.append(f'<text x="{x0 + 3*c + c/2}" y="{yy - 6}" text-anchor="middle" class="mrm muted" font-size="15">⋮</text>')
s.append(f'<line x1="{x0}" y1="{yy + 2}" x2="{x0 + c*len(final)}" y2="{yy + 2}" class="axis"/>')
s.append(f'<text x="{x0 - 30}" y="{yy + 26}" text-anchor="middle" class="math" font-size="15">A</text>')
for j, b in enumerate(final):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{yy + 26}" text-anchor="middle" class="mrm" font-size="15" font-weight="600">{b}</text>')
s.append(f'<text x="{x0 + c*len(final) + 12}" y="{y0 + 60}" class="label">shaded: a bit that</text>')
s.append(f'<text x="{x0 + c*len(final) + 12}" y="{y0 + 76}" class="label">changes at this stage</text>')
s.append('</svg>')
out['delta2-table'] = ''.join(s)


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

def pair(x, y):
    return (x + y) * (x + y + 1) // 2 + y

# ---------------------------------------------------------------- the join X + Y
X, Y = '101100', '001011'
w = 30
s = ['<svg class="fig" viewBox="0 0 520 210" width="520" role="img" aria-label="The join of X and Y: the bits of X are placed at the even positions and the bits of Y at the odd positions">',
     '<defs>' + marker('ah-join', 'muted-fill') + '</defs>']
xs0, ys0 = 70, 300
s.append(f'<text x="{xs0 - 14}" y="40" text-anchor="end" class="math" font-size="17">X</text>')
s.append(f'<text x="{ys0 - 14}" y="40" text-anchor="end" class="math" font-size="17">Y</text>')
for i in range(6):
    s.append(f'<rect x="{xs0 + i*w}" y="20" width="{w}" height="{w}" class="cell"/>')
    s.append(f'<text x="{xs0 + i*w + w/2}" y="41" text-anchor="middle" class="mrm" font-size="15">{X[i]}</text>')
    s.append(f'<rect x="{ys0 + i*w}" y="20" width="{w}" height="{w}" class="cell head-cell"/>')
    s.append(f'<text x="{ys0 + i*w + w/2}" y="41" text-anchor="middle" class="mrm" font-size="15">{Y[i]}</text>')
j0, jy = 80, 140
s.append(f'<text x="{j0 - 10}" y="{jy + 21}" text-anchor="end" class="math" font-size="17">X<tspan class="mrm"> ⊕ </tspan>Y</text>')
for k in range(12):
    i = k // 2
    b = X[i] if k % 2 == 0 else Y[i]
    cls = 'cell' if k % 2 == 0 else 'cell head-cell'
    s.append(f'<rect x="{j0 + k*w}" y="{jy}" width="{w}" height="{w}" class="{cls}"/>')
    s.append(f'<text x="{j0 + k*w + w/2}" y="{jy + 21}" text-anchor="middle" class="mrm" font-size="15">{b}</text>')
    s.append(f'<text x="{j0 + k*w + w/2}" y="{jy + w + 16}" text-anchor="middle" class="mrm muted" font-size="11">{k}</text>')
    sx = (xs0 if k % 2 == 0 else ys0) + i*w + w/2
    s.append(f'<line x1="{sx}" y1="52" x2="{j0 + k*w + w/2}" y2="{jy - 3}" class="muted-stroke" stroke-width="1" marker-end="url(#ah-join)"/>')
s.append(f'<text x="{j0}" y="{jy + w + 36}" class="label">position 2n holds X(n), position 2n + 1 holds Y(n)</text>')
s.append('</svg>')
out['join'] = ''.join(s)

# ---------------------------------------------------------------- the first jumps
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The degrees 0, 0 prime, 0 double prime and 0 triple prime on a vertical axis, with the sets located at each level">']
ax = 120
levels = [(270, '0', '', 'computable sets'),
          (180, '0', '′', '∅′ and the Turing complete c.e. sets'),
          (90, '0', '″', 'Tot, Inf, Fin'),
          (20, '0', '‴', '⋯')]
s.append(f'<line x1="{ax}" y1="12" x2="{ax}" y2="280" class="axis"/>')
for y, b, pr, lab in levels:
    s.append(f'<circle cx="{ax}" cy="{y}" r="5" class="node"/>')
    s.append(f'<text x="{ax - 14}" y="{y + 6}" text-anchor="end" class="mrm" font-size="17" font-weight="700">{b}<tspan font-weight="400">{pr}</tspan></text>')
    s.append(f'<text x="{ax + 16}" y="{y + 4}" class="label">{lab}</text>')
# brackets: sets computable in 0' and in 0''
bx = 430
s.append(f'<path d="M{bx},272 L{bx + 8},272 L{bx + 8},178 L{bx},178" class="accent-stroke" stroke-width="1.3"/>')
s.append(f'<text x="{bx + 14}" y="222" class="label">computable</text>')
s.append(f'<text x="{bx + 14}" y="238" class="label">in ∅′</text>')
bx2 = 510
s.append(f'<path d="M{bx2},272 L{bx2 + 8},272 L{bx2 + 8},88 L{bx2},88" class="accent-stroke" stroke-width="1.3"/>')
s.append(f'<text x="{bx2 + 14}" y="126" class="label">computable</text>')
s.append(f'<text x="{bx2 + 14}" y="142" class="label">in ∅″</text>')
s.append(f'<text x="{ax + 16}" y="220" class="label">strictly between: the Kleene–Post sets,</text>')
s.append(f'<text x="{ax + 16}" y="236" class="label">the non-computable low sets</text>')
s.append('</svg>')
out['jump-ladder'] = ''.join(s)

# ---------------------------------------------------------------- frames of the computation function
rows = [(3, 5, 8), (4, 6, 9), (5, 9, 12), (6, 9, 13), (7, 12, 15)]  # (x, c(x), f(x))
x0, dx, y0, dy, T = 80, 26, 40, 34, 17
s = ['<svg class="fig" viewBox="0 0 560 250" width="560" role="img" aria-label="For each x, the frame of stages from x to f(x) contains the stage c(x), at which the approximation is correct below x">']
for t in range(T):
    xx = x0 + dx * t
    s.append(f'<text x="{xx}" y="{y0 - 16}" text-anchor="middle" class="mrm muted" font-size="11">{t}</text>')
    s.append(f'<line x1="{xx}" y1="{y0 - 8}" x2="{xx}" y2="{y0 + dy * (len(rows) - 1) + 10}" class="axis" stroke-dasharray="2 4"/>')
s.append(f'<text x="{x0 + dx * (T - 1) + 14}" y="{y0 - 16}" class="label">stage</text>')
for r, (x, c, f) in enumerate(rows):
    y = y0 + dy * r
    s.append(f'<text x="{x0 - 52}" y="{y + 5}" class="math" font-size="15">x</text><text x="{x0 - 40}" y="{y + 5}" class="mrm" font-size="15">= {x}</text>')
    s.append(f'<rect x="{x0 + dx * x - 4}" y="{y - 7}" width="{dx * (f - x) + 8}" height="14" rx="7" class="soft-fill"/>')
    s.append(f'<line x1="{x0 + dx * x}" y1="{y}" x2="{x0 + dx * f}" y2="{y}" class="accent-stroke" stroke-width="2"/>')
    s.append(f'<circle cx="{x0 + dx * c}" cy="{y}" r="5" class="accent-fill"/>')
ly = y0 + dy * len(rows) + 4
s.append(f'<rect x="{x0}" y="{ly - 7}" width="40" height="14" rx="7" class="soft-fill"/><line x1="{x0 + 4}" y1="{ly}" x2="{x0 + 36}" y2="{ly}" class="accent-stroke" stroke-width="2"/>')
s.append(f'<text x="{x0 + 48}" y="{ly + 4}" class="label">the frame of stages t with x ≤ t ≤ f(x)</text>')
s.append(f'<circle cx="{x0 + 300}" cy="{ly}" r="5" class="accent-fill"/><text x="{x0 + 312}" y="{ly + 4}" class="label">the stage c(x)</text>')
s.append('</svg>')
out['frames'] = ''.join(s)

# ---------------------------------------------------------------- Kleene-Post construction
# segments: (kind, length, label); kinds: ext (search), diag (diagonal bit), pad (appended 0)
A = [('ext', 4, 'R0'), ('pad', 1, ''), ('diag', 1, 'S0'), ('pad', 1, ''), ('ext', 3, 'R1'), ('pad', 1, '')]
B = [('diag', 1, 'R0'), ('pad', 1, ''), ('ext', 5, 'S0'), ('pad', 1, ''), ('diag', 1, 'R1'), ('pad', 1, '')]
w = 26
s = ['<svg class="fig" viewBox="0 0 520 200" width="520" role="img" aria-label="The first three steps of the Kleene–Post construction: each step extends one string by a search and the other by one diagonal bit">',
     '<defs>' + marker('ah-kp', 'ink-fill') + '</defs>']
def bar(segs, y0, name):
    s.append(f'<text x="64" y="{y0 + 18}" text-anchor="end" class="math" font-size="17">{name}</text>')
    x = 80
    pos = []
    for kind, L, lab in segs:
        for i in range(L):
            cls = {'ext': 'cell head-cell', 'diag': 'cell', 'pad': 'cell'}[kind]
            s.append(f'<rect x="{x + i*w}" y="{y0}" width="{w}" height="{w}" class="{cls}"/>')
            if kind == 'pad':
                s.append(f'<text x="{x + i*w + w/2}" y="{y0 + 18}" text-anchor="middle" class="mrm muted" font-size="14">0</text>')
            if kind == 'diag':
                s.append(f'<rect x="{x + 4}" y="{y0 + 4}" width="{w - 8}" height="{w - 8}" class="accent-fill" opacity="0.85"/>')
        if lab:
            s.append(sub(lab[0], lab[1], x + L*w/2, y0 - 10 if name == "A" else y0 + w + 20, 15).replace('class="math"', 'class="math muted"'))
        pos.append((kind, x, L))
        x += L * w
    s.append(f'<text x="{x + 8}" y="{y0 + 18}" class="mrm muted" font-size="15">⋯</text>')
    return pos
pa = bar(A, 40, 'A')
pb = bar(B, 120, 'B')
# arrow: computation on A's R0 extension decides the diagonal bit of B
_, xa, La = pa[0]
_, xb, _ = pb[0]
s.append(f'<path d="M{xa + La*w/2},{66} C{xa + La*w/2},{96} {xb + w/2},{90} {xb + w/2},{118}" class="ink-stroke" stroke-width="1.2" marker-end="url(#ah-kp)"/>')
_, xb2, Lb2 = pb[2]
_, xa2, _ = pa[2]
s.append(f'<path d="M{xb2 + Lb2*w/2},{118} C{xb2 + Lb2*w/2},{90} {xa2 + w/2},{96} {xa2 + w/2},{68}" class="ink-stroke" stroke-width="1.2" marker-end="url(#ah-kp)"/>')
s.append('<rect x="300" y="176" width="14" height="14" class="cell head-cell"/><text x="320" y="187" class="label">extension found by search</text>')
s.append('<rect x="80" y="176" width="14" height="14" class="cell"/><rect x="83" y="179" width="8" height="8" class="accent-fill"/><text x="100" y="187" class="label">diagonal bit</text>')
s.append('<text x="190" y="187" class="label">0: padding</text>')
s.append('</svg>')
out['kleene-post'] = ''.join(s)

# ---------------------------------------------------------------- conditions of the high construction
L, m = 16, 2
limit = '10'   # values of the column limits for x < m
rowsN, colsN = 5, 10
cw = 32
x0, y0 = 70, 34
import random
random.seed(3)
s = ['<svg class="fig" viewBox="0 0 520 260" width="520" role="img" aria-label="Positions of A arranged in columns; the positions coded below the length of sigma are fixed by sigma, and beyond them the first m columns are fixed to their limit">']
for y in range(colsN):
    s.append(f'<text x="{x0 + y*cw + cw/2}" y="{y0 - 10}" text-anchor="middle" class="math muted" font-size="13">{y}</text>')
s.append(f'<text x="{x0 + colsN*cw + 8}" y="{y0 - 10}" class="math" font-size="13">y</text>')
for x in range(rowsN):
    yy = y0 + x*cw
    s.append(f'<text x="{x0 - 50}" y="{yy + 21}" class="math" font-size="14">x</text><text x="{x0 - 38}" y="{yy + 21}" class="mrm" font-size="14">= {x}</text>')
    for y in range(colsN):
        p = pair(x, y)
        xx = x0 + y*cw
        if p < L:
            s.append(f'<rect x="{xx}" y="{yy}" width="{cw}" height="{cw}" class="cell"/>')
            s.append(f'<text x="{xx + cw/2}" y="{yy + 21}" text-anchor="middle" class="mrm" font-size="14">{random.choice("01")}</text>')
        elif x < m:
            s.append(f'<rect x="{xx}" y="{yy}" width="{cw}" height="{cw}" class="cell head-cell"/>')
            s.append(f'<text x="{xx + cw/2}" y="{yy + 21}" text-anchor="middle" class="mrm" font-size="14">{limit[x]}</text>')
        else:
            s.append(f'<rect x="{xx}" y="{yy}" width="{cw}" height="{cw}" class="cell"/>')
            s.append(f'<text x="{xx + cw/2}" y="{yy + 21}" text-anchor="middle" class="mrm muted" font-size="14">·</text>')
    s.append(f'<text x="{x0 + colsN*cw + 8}" y="{yy + 21}" class="mrm muted" font-size="15">⋯</text>')
ly = y0 + rowsN*cw + 22
s.append(f'<rect x="{x0}" y="{ly - 11}" width="14" height="14" class="cell"/><text x="{x0 + 20}" y="{ly}" class="label">fixed by σ (code below |σ|)</text>')
s.append(f'<rect x="{x0 + 200}" y="{ly - 11}" width="14" height="14" class="cell head-cell"/><text x="{x0 + 220}" y="{ly}" class="label">fixed to ∅″(x), for x &lt; m</text>')
s.append(f'<text x="{x0}" y="{ly + 20}" class="label">· free; here |σ| = {L}, m = {m}, ∅″(0) = 1, ∅″(1) = 0</text>')
s.append('</svg>')
out['high-columns'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
