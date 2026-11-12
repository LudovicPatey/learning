# Generates the inline SVG figures of the Countability and diagonalization course.
# Usage: python3 scripts/figures/countability.py out.json
# Paste each figure into the lesson that uses it (see the keys below).
import json, math, sys
out = {}

def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

def sub(base, s, x, y, size=17, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

def seg(x1, y1, x2, y2, r1, r2):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return x1 + ux * r1, y1 + uy * r1, x2 - ux * r2, y2 - uy * r2

# ---------------------------------------------------------------- equipotence: Galileo
s = ['<svg class="fig" viewBox="0 0 572 150" width="572" role="img" aria-label="Each integer n is matched with the square n squared, drawn among all integers">',
     '<defs>' + marker('ah-gal') + '</defs>']
s.append('<text x="4" y="22" class="label">n</text>')
s.append('<text x="4" y="138" class="label">n²</text>')
cw, bx, by = 20, 20, 104
for k in range(26):
    sq = int(math.isqrt(k)) ** 2 == k
    s.append(f'<rect x="{bx + cw*k}" y="{by}" width="{cw}" height="{cw}" class="{"cell head-cell" if sq else "cell"}"/>')
    s.append(f'<text x="{bx + cw*k + cw/2}" y="{by + 14}" text-anchor="middle" class="mrm{"" if sq else " muted"}" font-size="10.5">{k}</text>')
s.append(f'<text x="{bx + cw*26 + 6}" y="{by + 15}" class="mrm muted" font-size="15">⋯</text>')
for n in range(6):
    xt = 30 + 100 * n
    xb = bx + cw * n * n + cw / 2
    s.append(f'<circle cx="{xt}" cy="30" r="13" class="node"/>')
    s.append(f'<text x="{xt}" y="35" text-anchor="middle" class="mrm" font-size="14">{n}</text>')
    x1, y1, x2, y2 = seg(xt, 30, xb, by, 14, 3)
    s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/>')
s.append('<text x="550" y="35" class="mrm muted" font-size="15">⋯</text>')
s.append('</svg>')
out['galileo'] = ''.join(s)

# ---------------------------------------------------------------- Cantor–Bernstein: the sets C_n
s = ['<svg class="fig" viewBox="0 0 540 272" width="540" role="img" aria-label="The set A cut into bands C0, C1, C2, C3 and the rest; f maps each band onto the next">',
     '<defs>' + marker('ah-cb') + '</defs>']
x0, x1 = 80, 330
bands = [(16, 66, '0'), (66, 110, '1'), (110, 150, '2'), (150, 186, '3')]
for (ya, yb, i) in bands:
    s.append(f'<rect x="{x0}" y="{ya}" width="{x1-x0}" height="{yb-ya}" class="soft-fill"/>')
s.append(f'<rect x="{x0}" y="186" width="{x1-x0}" height="70" class="cell"/>')
s.append(f'<rect x="{x0}" y="16" width="{x1-x0}" height="240" class="track-outline"/>')
for (ya, yb, i) in bands[1:]:
    s.append(f'<line x1="{x0}" y1="{ya}" x2="{x1}" y2="{ya}" class="axis"/>')
s.append(f'<line x1="{x0}" y1="186" x2="{x1}" y2="186" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<text x="{(x0+x1)/2}" y="46" text-anchor="middle" class="math" font-size="17">C<tspan class="mrm" font-size="11" dy="4">0</tspan><tspan class="mrm" dy="-4"> = </tspan>A<tspan class="mrm"> ∖ </tspan>B</text>')
for (ya, yb, i) in bands[1:]:
    s.append(sub('C', i, (x0+x1)/2, (ya+yb)/2 + 4))
s.append(f'<text x="{(x0+x1)/2}" y="200" text-anchor="middle" class="mrm muted" font-size="13">⋮</text>')
s.append(f'<text x="{(x0+x1)/2}" y="226" text-anchor="middle" class="label">elements of B never reached from A ∖ B</text>')
s.append(f'<text x="{(x0+x1)/2}" y="242" text-anchor="middle" class="label">by iterating f: here h is the identity</text>')
mids = [(ya+yb)/2 for (ya, yb, i) in bands] + [198]
for a_, b_ in zip(mids, mids[1:]):
    s.append(f'<path d="M{x1+4},{a_} C{x1+40},{a_+6} {x1+40},{b_-6} {x1+6},{b_}" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cb)"/>')
    s.append(f'<text x="{x1+38}" y="{(a_+b_)/2 + 5}" class="math" font-size="15">f</text>')
s.append(f'<text x="{x1+70}" y="96" class="label">shaded: C = ⋃ Cₙ,</text>')
s.append(f'<text x="{x1+70}" y="112" class="label">where h = f</text>')
# brackets: B (inner) close to the box, A (outer) further left
s.append(f'<path d="M{x0-8},66 L{x0-14},66 L{x0-14},256 L{x0-8},256" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<text x="{x0-22}" y="166" text-anchor="end" class="math" font-size="17">B</text>')
s.append(f'<path d="M{x0-38},16 L{x0-44},16 L{x0-44},256 L{x0-38},256" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<text x="{x0-52}" y="142" text-anchor="end" class="math" font-size="17">A</text>')
s.append('</svg>')
out['cb-bands'] = ''.join(s)

# ---------------------------------------------------------------- Cantor–Bernstein: chains
s = ['<svg class="fig" viewBox="0 0 580 250" width="580" role="img" aria-label="Three kinds of chains of f and g and how the bijection pairs their elements">',
     '<defs>' + marker('ah-ch') + marker('ah-chm', 'muted-fill') + '</defs>']
def chain(y0, start, title, use_f, left_open=False):
    # alternate A (top row y0) and B (bottom row y0+40) dots
    s.append(f'<text x="0" y="{y0 + 4}" class="label">{title[0]}</text>')
    s.append(f'<text x="0" y="{y0 + 20}" class="label">{title[1]}</text>')
    s.append(f'<text x="0" y="{y0 + 36}" class="label">{title[2]}</text>')
    pts = []
    side = start
    for i in range(7):
        x = 210 + 52 * i
        y = y0 if side == 'A' else y0 + 40
        pts.append((x, y, side))
        side = 'B' if side == 'A' else 'A'
    for (xa, ya, sa), (xb, yb, sb) in zip(pts, pts[1:]):
        is_f = sa == 'A'
        paired = (is_f and use_f) or ((not is_f) and not use_f)
        x1_, y1_, x2_, y2_ = seg(xa, ya, xb, yb, 6, 8)
        if paired and is_f:
            s.append(f'<line x1="{x1_:.1f}" y1="{y1_:.1f}" x2="{x2_:.1f}" y2="{y2_:.1f}" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/>')
            lab = 'f'
        elif paired:
            # the pair (x, g^{-1}(x)) goes from the A-point back to the B-point
            r1, r2, r3, r4 = seg(xb, yb, xa, ya, 6, 8)
            s.append(f'<line x1="{r1:.1f}" y1="{r2:.1f}" x2="{r3:.1f}" y2="{r4:.1f}" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/>')
            lab = 'g⁻¹'
        else:
            s.append(f'<line x1="{x1_:.1f}" y1="{y1_:.1f}" x2="{x2_:.1f}" y2="{y2_:.1f}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/>')
            lab = 'f' if is_f else 'g'
        s.append(f'<text x="{(xa+xb)/2 + (9 if is_f else -9)}" y="{(ya+yb)/2 + 4}" text-anchor="middle" class="math muted" font-size="12">{lab}</text>')
    for (x, y, sd) in pts:
        s.append(f'<circle cx="{x}" cy="{y}" r="4.5" class="{"ink-fill" if sd == "A" else "node"}"/>')
    s.append(f'<text x="{pts[-1][0] + 18}" y="{y0 + 24}" class="mrm muted" font-size="15">⋯</text>')
    if left_open:
        s.append(f'<text x="{pts[0][0] - 30}" y="{y0 + 24}" class="mrm muted" font-size="15">⋯</text>')
    else:
        s.append(f'<circle cx="{pts[0][0]}" cy="{pts[0][1]}" r="9" class="accent-stroke" stroke-width="1.2"/>')
s.append('<text x="196" y="14" text-anchor="end" class="label">A</text>')
s.append('<text x="196" y="54" text-anchor="end" class="label">B</text>')
chain(10, 'A', ('starts in A ∖ g(B):', 'every element of A', 'goes to its image by f'), True)
chain(92, 'B', ('starts in B ∖ f(A):', 'every element of A', 'goes to its preimage by g'), False)
chain(174, 'A', ('has no first element:', 'preimage by g', '(the choice of the proof)'), False, left_open=True)
s.append('</svg>')
out['cb-chains'] = ''.join(s)

# ---------------------------------------------------------------- countable sets: Cantor pairing
def pair(x, y):
    n = x + y
    return n * (n + 1) // 2 + y
N = 4
ox, oy, d = 60, 250, 52
P = lambda x, y: (ox + d * x, oy - d * y)
s = ['<svg class="fig" viewBox="0 0 330 300" width="330" role="img" aria-label="Pairs of integers numbered along successive diagonals">', '<defs>' + marker('ah-pair') + '</defs>']
s.append(f'<line x1="{ox-18}" y1="{oy}" x2="{ox + d*N + 34}" y2="{oy}" class="axis"/>')
s.append(f'<line x1="{ox}" y1="{oy+18}" x2="{ox}" y2="{oy - d*N - 34}" class="axis"/>')
s.append(f'<text x="{ox + d*N + 40}" y="{oy+5}" class="math" font-size="17">x</text>')
s.append(f'<text x="{ox-5}" y="{oy - d*N - 40}" class="math" font-size="17">y</text>')
for i in range(N + 1):
    s.append(f'<text x="{ox + d*i}" y="{oy + 32}" text-anchor="middle" class="mrm muted" font-size="13">{i}</text>')
    s.append(f'<text x="{ox - 26}" y="{oy - d*i + 5}" text-anchor="middle" class="mrm muted" font-size="13">{i}</text>')
order = [(n - y, y) for n in range(N + 1) for y in range(n + 1)]
for (a, b) in zip(order, order[1:]):
    (xa, ya), (xb, yb) = P(*a), P(*b)
    same = sum(a) == sum(b)
    x1_, y1_, x2_, y2_ = seg(xa, ya, xb, yb, 15, 17)
    cls = 'accent-stroke' if same else 'muted-stroke'
    dash = '' if same else ' stroke-dasharray="3 3"'
    s.append(f'<line x1="{x1_:.1f}" y1="{y1_:.1f}" x2="{x2_:.1f}" y2="{y2_:.1f}" class="{cls}" stroke-width="1.4"{dash} marker-end="url(#ah-pair)"/>')
for (x, y) in order:
    cx_, cy_ = P(x, y)
    s.append(f'<circle cx="{cx_}" cy="{cy_}" r="14" class="node"/>')
    s.append(f'<text x="{cx_}" y="{cy_+5}" text-anchor="middle" class="mrm" font-size="14">{pair(x, y)}</text>')
s.append('</svg>')
out['pairing'] = ''.join(s)

# ---------------------------------------------------------------- diagonal argument: the table
rows = ['0110100', '1101001', '0000110', '1011011', '0101010']
c, x0, y0 = 30, 70, 34
ncol = len(rows[0])
s = ['<svg class="fig" viewBox="0 0 400 270" width="400" role="img" aria-label="Rows X0 to X4 of a table of bits; the diagonal is marked; the sequence Y flips each diagonal bit">']
for j in range(ncol):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{y0 - 10}" text-anchor="middle" class="mrm muted" font-size="12">{j}</text>')
s.append(f'<text x="{x0 + c*ncol + 14}" y="{y0 - 10}" class="mrm muted" font-size="12">⋯</text>')
for i, r in enumerate(rows):
    y = y0 + c * i
    s.append(sub('X', str(i), 34, y + 20, 16))
    for j, b in enumerate(r):
        s.append(f'<rect x="{x0 + c*j}" y="{y}" width="{c}" height="{c}" class="{"cell head-cell" if i == j else "cell"}"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{y + 20}" text-anchor="middle" class="mrm{"" if i == j else " muted"}" font-size="15">{b}</text>')
    s.append(f'<text x="{x0 + c*ncol + 14}" y="{y + 20}" class="mrm muted" font-size="15">⋯</text>')
s.append(f'<text x="{x0 + 2*c + c/2}" y="{y0 + c*len(rows) + 16}" text-anchor="middle" class="mrm muted" font-size="15">⋮</text>')
yy = y0 + c * len(rows) + 34
s.append(f'<line x1="{x0}" y1="{yy - 8}" x2="{x0 + c*ncol}" y2="{yy - 8}" class="axis"/>')
s.append(f'<text x="34" y="{yy + 20}" text-anchor="middle" class="math" font-size="16">Y</text>')
for j in range(ncol):
    if j < len(rows):
        b = '1' if rows[j][j] == '0' else '0'
        s.append(f'<rect x="{x0 + c*j}" y="{yy}" width="{c}" height="{c}" class="cell head-cell"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{yy + 20}" text-anchor="middle" class="mrm" font-size="15" font-weight="600">{b}</text>')
    else:
        s.append(f'<rect x="{x0 + c*j}" y="{yy}" width="{c}" height="{c}" class="cell"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{yy + 20}" text-anchor="middle" class="mrm muted" font-size="15">⋯</text>')
s.append(f'<text x="{x0 + c*ncol + 14}" y="{yy + 20}" class="label">Y(n) = 1 − Xₙ(n)</text>')
s.append('</svg>')
out['diagonal'] = ''.join(s)

# ---------------------------------------------------------------- continuum: coding N^N into 2^N
vals = [2, 0, 3, 1]
s = ['<svg class="fig" viewBox="0 0 560 120" width="560" role="img" aria-label="The function 2, 0, 3, 1 coded as the bit sequence 1 1 0 0 1 1 1 0 1 0">']
c, x, y = 34, 20, 20
for i, v in enumerate(vals):
    start = x
    for _ in range(v):
        s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" class="cell"/>')
        s.append(f'<text x="{x + c/2}" y="{y + 23}" text-anchor="middle" class="mrm" font-size="16">1</text>')
        x += c
    s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" class="cell head-cell"/>')
    s.append(f'<text x="{x + c/2}" y="{y + 23}" text-anchor="middle" class="mrm" font-size="16">0</text>')
    x += c
    end = x
    s.append(f'<path d="M{start + 3},{y + c + 8} L{start + 3},{y + c + 14} L{end - 3},{y + c + 14} L{end - 3},{y + c + 8}" class="muted-stroke" stroke-width="1.1"/>')
    s.append(f'<text x="{(start + end)/2}" y="{y + c + 34}" text-anchor="middle" class="math" font-size="15">f<tspan class="mrm">({i}) = {v}</tspan></text>')
    x += 6
s.append(f'<text x="{x + 8}" y="{y + 23}" class="mrm muted" font-size="16">⋯</text>')
s.append('</svg>')
out['code-baire'] = ''.join(s)

# ---------------------------------------------------------------- continuum: the Cantor set
s = ['<svg class="fig" viewBox="0 0 540 172" width="540" role="img" aria-label="The first four stages of the construction of the Cantor set, with binary labels">']
L, R = 50, 530
def intervals(n):
    iv = [(0.0, 1.0, '')]
    for _ in range(n):
        nxt = []
        for (a, b, w) in iv:
            t = (b - a) / 3
            nxt += [(a, a + t, w + '0'), (b - t, b, w + '1')]
        iv = nxt
    return iv
for n in range(4):
    y = 22 + 42 * n
    s.append(sub('A', str(n), 20, y + 6, 16))
    for (a, b, w) in intervals(n):
        xa, xb = L + (R - L) * a, L + (R - L) * b
        s.append(f'<rect x="{xa:.1f}" y="{y - 4}" width="{xb - xa:.1f}" height="8" rx="1.5" class="{"accent-fill" if n else "ink-fill"}"/>')
        if 1 <= n <= 3:
            fs = 12 if n < 3 else 9.5
            s.append(f'<text x="{(xa + xb)/2:.1f}" y="{y + 20}" text-anchor="middle" class="mrm muted" font-size="{fs}">{w}</text>')
s.append(f'<text x="{L}" y="12" text-anchor="middle" class="mrm muted" font-size="12">0</text>')
s.append(f'<text x="{R}" y="12" text-anchor="middle" class="mrm muted" font-size="12">1</text>')
s.append('</svg>')
out['cantor-set'] = ''.join(s)

# ---------------------------------------------------------------- countable sets: first occurrences
lst = ['a', 'b', 'a', 'c', 'b', 'd', 'a', 'e', 'c', 'f']
elems = ['a', 'b', 'c', 'd', 'e', 'f']
c, x0, yc = 40, 80, 40
first = {}
for i, a in enumerate(lst):
    first.setdefault(a, i)
s = ['<svg class="fig" viewBox="0 0 520 200" width="520" role="img" aria-label="A listing with repetitions; the first occurrence of each element is shaded and each element points to it">',
     '<defs>' + marker('ah-fo') + '</defs>']
s.append(f'<text x="{x0 - 14}" y="{yc - 12}" text-anchor="end" class="math" font-size="16">n</text>')
s.append(f'<text x="{x0 - 14}" y="{yc + 26}" text-anchor="end" class="math" font-size="16">s<tspan class="mrm">(</tspan>n<tspan class="mrm">)</tspan></text>')
for i, a in enumerate(lst):
    fo = first[a] == i
    s.append(f'<text x="{x0 + c*i + c/2}" y="{yc - 12}" text-anchor="middle" class="mrm muted" font-size="12">{i}</text>')
    s.append(f'<rect x="{x0 + c*i}" y="{yc}" width="{c}" height="{c}" class="{"cell head-cell" if fo else "cell"}"/>')
    s.append(f'<text x="{x0 + c*i + c/2}" y="{yc + 26}" text-anchor="middle" class="math{"" if fo else " muted"}" font-size="17">{a}</text>')
s.append(f'<text x="{x0 + c*len(lst) + 8}" y="{yc + 26}" class="mrm muted" font-size="16">⋯</text>')
yn = 160
s.append(f'<text x="{x0 - 14}" y="{yn + 6}" text-anchor="end" class="math" font-size="16">A</text>')
for k, a in enumerate(elems):
    xn = x0 + 20 + 72 * k
    xt = x0 + c * first[a] + c / 2
    s.append(f'<circle cx="{xn}" cy="{yn}" r="14" class="node"/>')
    s.append(f'<text x="{xn}" y="{yn + 6}" text-anchor="middle" class="math" font-size="17">{a}</text>')
    x1_, y1_, x2_, y2_ = seg(xn, yn, xt, yc + c, 15, 3)
    s.append(f'<line x1="{x1_:.1f}" y1="{y1_:.1f}" x2="{x2_:.1f}" y2="{y2_:.1f}" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/>')
s.append(f'<text x="{x0 + 20 + 72*(len(elems) - 1) + 26}" y="{yn + 6}" class="mrm muted" font-size="16">⋯</text>')
s.append('</svg>')
out['first-occurrences'] = ''.join(s)

# ---------------------------------------------------------------- continuum: the join
X, Y = '1011', '0010'
c = 34
s = ['<svg class="fig" viewBox="0 0 470 200" width="470" role="img" aria-label="The bits of X go to the even positions and the bits of Y to the odd positions of the join">']
xr, yX, yY, yZ = 120, 20, 146, 84
s.append(f'<text x="60" y="{yX + 23}" text-anchor="middle" class="math" font-size="16">X</text>')
s.append(f'<text x="60" y="{yY + 23}" text-anchor="middle" class="math" font-size="16">Y</text>')
s.append(f'<text x="60" y="{yZ + 23}" text-anchor="middle" class="math" font-size="16">X<tspan class="mrm"> ⊕ </tspan>Y</text>')
zx0 = 110
for n in range(4):
    xa = xr + 2 * c * n + c / 2
    for (row, yrow, shade, pos) in ((X, yX, True, 2 * n), (Y, yY, False, 2 * n + 1)):
        s.append(f'<rect x="{xa - c/2}" y="{yrow}" width="{c}" height="{c}" class="{"cell head-cell" if shade else "cell"}"/>')
        s.append(f'<text x="{xa}" y="{yrow + 23}" text-anchor="middle" class="mrm" font-size="16">{row[n]}</text>')
        zx = zx0 + c * pos + c / 2
        if shade:
            s.append(f'<line x1="{xa}" y1="{yrow + c}" x2="{zx}" y2="{yZ}" class="muted-stroke" stroke-width="1.1"/>')
        else:
            s.append(f'<line x1="{xa}" y1="{yrow}" x2="{zx}" y2="{yZ + c}" class="muted-stroke" stroke-width="1.1"/>')
for pos in range(8):
    b = X[pos // 2] if pos % 2 == 0 else Y[pos // 2]
    zx = zx0 + c * pos
    s.append(f'<rect x="{zx}" y="{yZ}" width="{c}" height="{c}" class="{"cell head-cell" if pos % 2 == 0 else "cell"}"/>')
    s.append(f'<text x="{zx + c/2}" y="{yZ + 23}" text-anchor="middle" class="mrm" font-size="16">{b}</text>')
    s.append(f'<text x="{zx + c - 4}" y="{yZ + c - 3}" text-anchor="end" class="mrm muted" font-size="8.5">{pos}</text>')
s.append(f'<text x="{zx0 + 8*c + 8}" y="{yZ + 23}" class="mrm muted" font-size="16">⋯</text>')
s.append(f'<text x="{xr + 8*c - c/2 + 8}" y="{yX + 23}" class="mrm muted" font-size="16">⋯</text>')
s.append(f'<text x="{xr + 8*c - c/2 + 8}" y="{yY + 23}" class="mrm muted" font-size="16">⋯</text>')
s.append('</svg>')
out['join'] = ''.join(s)

# ---------------------------------------------------------------- diagonalization and computation: the partial table
U = '↑'
rows = [['2', U, '0', '5', '1', '3'], ['0', U, '4', U, '2', U], ['1', '1', '7', '0', '0', '0'],
        [U, '6', '2', U, '3', '2'], ['4', '0', '0', '1', '0', U]]
d = [str(int(r[i]) + 1) if r[i] != U else U for i, r in enumerate(rows)]
rowc = d + [U]
c, x0, y0 = 34, 90, 34
cols = [0, 1, 2, 3, 4, None, 'c']
def colx(j):
    return x0 + c * j
s = ['<svg class="fig" viewBox="0 0 400 290" width="400" role="img" aria-label="A table of values of partial computable functions, some undefined; the row of the diagonal function d has an undefined entry on the diagonal">']
for j, h in enumerate(cols):
    if h is None:
        s.append(f'<text x="{colx(j) + c/2}" y="{y0 - 10}" text-anchor="middle" class="mrm muted" font-size="13">⋯</text>')
    else:
        s.append(f'<text x="{colx(j) + c/2}" y="{y0 - 10}" text-anchor="middle" class="{"math" if h == "c" else "mrm"} muted" font-size="13">{h}</text>')
def drow(y, label, vals, diag):
    s.append(label)
    for j, h in enumerate(cols):
        if h is None:
            s.append(f'<text x="{colx(j) + c/2}" y="{y + 22}" text-anchor="middle" class="mrm muted" font-size="15">⋯</text>')
            continue
        v = vals[j if j < 5 else 5]
        hd = (j == diag)
        s.append(f'<rect x="{colx(j)}" y="{y}" width="{c}" height="{c}" class="{"cell head-cell" if hd else "cell"}"/>')
        s.append(f'<text x="{colx(j) + c/2}" y="{y + 22}" text-anchor="middle" class="mrm{"" if hd else " muted"}" font-size="15">{v}</text>')
for i, r in enumerate(rows):
    y = y0 + c * i
    drow(y, sub('Φ', str(i), 50, y + 22, 16, cls='mrm'), r, i)
yd = y0 + c * 5
s.append(f'<text x="{colx(2) + c/2}" y="{yd + 20}" text-anchor="middle" class="mrm muted" font-size="15">⋮</text>')
yc_ = yd + 34
s.append(f'<text x="50" y="{yc_ + 22}" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="math" font-size="11" dy="4">c</tspan><tspan dy="-4"> = </tspan><tspan class="math">d</tspan></text>')
drow(yc_, '', rowc, 6)
s.append('</svg>')
out['partial-table'] = ''.join(s)

# ---------------------------------------------------------------- finite extensions: the stages
blocks = ['01', '100', '1', '0110']
c, x0, y0 = 28, 70, 18
s = ['<svg class="fig" viewBox="0 0 520 210" width="520" role="img" aria-label="Successive strings of a finite extension construction, each extending the previous one by a block">']
pre = ''
for k, b in enumerate(blocks):
    y = y0 + 40 * k
    s.append(sub('σ', str(k + 1), 34, y + 19, 16, cls='mrm'))
    for i, ch in enumerate(pre + b):
        new = i >= len(pre)
        s.append(f'<rect x="{x0 + c*i}" y="{y}" width="{c}" height="{c}" class="{"cell head-cell" if new else "cell"}"/>')
        s.append(f'<text x="{x0 + c*i + c/2}" y="{y + 19}" text-anchor="middle" class="mrm{"" if new else " muted"}" font-size="14">{ch}</text>')
    pre += b
    s.append(f'<text x="{x0 + c*len(pre) + 12}" y="{y + 19}" class="label">secures</text>')
    s.append(sub('R', str(k), x0 + c*len(pre) + 66, y + 19, 15, anchor='start'))
y = y0 + 40 * len(blocks)
s.append(f'<text x="34" y="{y + 19}" text-anchor="middle" class="math" font-size="16">Y</text>')
for i, ch in enumerate(pre):
    s.append(f'<rect x="{x0 + c*i}" y="{y}" width="{c}" height="{c}" class="cell"/>')
    s.append(f'<text x="{x0 + c*i + c/2}" y="{y + 19}" text-anchor="middle" class="mrm" font-size="14">{ch}</text>')
s.append(f'<text x="{x0 + c*len(pre) + 10}" y="{y + 19}" class="mrm muted" font-size="15">⋯</text>')
s.append('</svg>')
out['finite-extension'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
