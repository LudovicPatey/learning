# Generates the inline SVG figures of the course on the fundamentals of computability.
# Usage: python3 scripts/figures/fundamentals.py out.json
# Paste each figure into the lesson that uses it (see the keys below):
#   stages            programs-as-numbers   approximation of W_e by stages
#   smn-tape          universal-program-smn the machine P_x ; M_e of the SMN theorem
#   halting-diagonal  halting-problem       the diagonal argument for the halting set
#   reduction         halting-problem       a many-one reduction
#   dovetailing       ce-sets               the enumeration of (2 => 3)
#   classes           ce-completeness       computable, c.e. and co-c.e. sets
#   owings            fixed-point           Owings' matrix for the fixed point theorem
import json, math, sys
out = {}

def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

def sub(base, s, x, y, size=16, anchor='middle', cls='math', extra=''):
    # base with a roman subscript s, then optional roman text extra
    t = (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
         f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan>')
    if extra:
        t += f'<tspan class="mrm" dy="-4">{extra}</tspan>'
    return t + '</text>'

def seg(x1, y1, x2, y2, r1, r2):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return x1 + ux * r1, y1 + uy * r1, x2 - ux * r2, y2 - uy * r2

# ---------------------------------------------------------------- stages: approximation of W_e
# conv[x] = least stage s with Phi_e(x)[s] converging (None: not by the last stage drawn).
conv = {0: 3, 1: 2, 2: 6, 3: None, 4: 9, 5: 7, 6: None, 7: 11, 8: 10, 9: None, 10: 12, 11: None}
NX, NS, c, x0, y0 = 12, 13, 26, 64, 40
hl = 8
s = ['<svg class="fig" viewBox="0 0 560 420" width="560" role="img" aria-label="A table of inputs x against stages s; the cells where the computation on x has converged by stage s are shaded; they form columns that start at the stage of convergence and never stop">']
s.append(f'<text x="{x0 + NX*c/2}" y="14" text-anchor="middle" class="label">input x</text>')
for x in range(NX):
    s.append(f'<text x="{x0 + c*x + c/2}" y="{y0 - 8}" text-anchor="middle" class="mrm muted" font-size="12">{x}</text>')
s.append(f'<text x="14" y="{y0 + NS*c/2}" text-anchor="middle" class="label" transform="rotate(-90 14 {y0 + NS*c/2})">stage s</text>')
for t in range(NS):
    y = y0 + c * t
    s.append(f'<text x="{x0 - 10}" y="{y + 17}" text-anchor="end" class="mrm muted" font-size="12">{t}</text>')
    for x in range(NX):
        if x >= t:
            continue
        done = conv[x] is not None and conv[x] <= t
        s.append(f'<rect x="{x0 + c*x}" y="{y}" width="{c}" height="{c}" class="{"cell head-cell" if done else "cell"}"/>')
# staircase: boundary of the region x < s
pts = []
for t in range(NS):
    pts.append((x0 + c * t, y0 + c * t))
    pts.append((x0 + c * t, y0 + c * (t + 1)))
pts.append((x0 + c * NX, y0 + c * NX))
d = 'M' + ' L'.join(f'{a},{b}' for a, b in pts)
s.append(f'<path d="{d}" class="ink-stroke" stroke-width="1.6"/>')
s.append(f'<rect x="{x0 - 3}" y="{y0 + c*hl - 3}" width="{c*NX + 6}" height="{c + 6}" class="track-outline"/>')
s.append(f'<text x="{x0 + c*NX + 12}" y="{y0 + c*hl + 17}" class="math" font-size="15">W<tspan class="mrm" font-size="10" dy="4">e</tspan><tspan class="mrm" dy="-4">[8] = {{0, 1, 2, 5}}</tspan></text>')
s.append(f'<text x="{x0 + c*NX + 12}" y="{y0 + 40}" class="label">only inputs x &lt; s</text>')
s.append(f'<text x="{x0 + c*NX + 12}" y="{y0 + 56}" class="label">can have converged</text>')
yb = y0 + c * NS + 22
for x in range(NX):
    if conv[x] is None:
        s.append(f'<text x="{x0 + c*x + c/2}" y="{yb}" text-anchor="middle" class="mrm muted" font-size="14">?</text>')
s.append(f'<text x="{x0 + c*NX + 12}" y="{yb}" class="label">no convergence yet: undecided</text>')
s.append('</svg>')
out['stages'] = ''.join(s)

# ---------------------------------------------------------------- SMN: the machine P_x ; M_e
def tape(y, cells, head, lo, hi, label):
    r = [f'<text x="0" y="{y + 20}" class="label">{label}</text>']
    for i in range(lo, hi + 1):
        xx = 150 + 30 * (i - lo)
        sym = cells.get(i, '⊔')
        r.append(f'<rect x="{xx}" y="{y}" width="30" height="30" rx="2" class="{"cell head-cell" if i == head else "cell"}"/>')
        r.append(f'<text x="{xx + 15}" y="{y + 20}" text-anchor="middle" class="mrm{"" if sym == "1" else " muted"}" font-size="15">{sym}</text>')
    hx = 150 + 30 * (head - lo) + 15
    r.append(f'<path d="M{hx - 6},{y - 13} L{hx + 6},{y - 13} L{hx},{y - 3} z" class="accent-fill"/>')
    return r
lo, hi = -6, 5
xv, yv = 2, 2
s = ['<svg class="fig" viewBox="0 0 520 240" width="520" role="img" aria-label="The tape before and after the machine P_x, for x = 2 and y = 2: P_x writes the block of x in front of the block of y and stops on its first cell">']
for i in range(lo, hi + 1):
    s.append(f'<text x="{150 + 30*(i - lo) + 15}" y="16" text-anchor="middle" class="mrm muted" font-size="11">{str(i).replace("-", "−")}</text>')
top = {i: '1' for i in range(0, yv + 1)}
s += tape(42, top, 0, lo, hi, 'input y = 2')
bot = dict(top)
for i in range(2, xv + 3):
    bot[-i] = '1'
h = -xv - 2
s += tape(152, bot, h, lo, hi, 'after Pₓ')
# braces under the blocks
def brace(i1, i2, y, txt):
    a = 150 + 30 * (i1 - lo) + 3
    b = 150 + 30 * (i2 - lo) + 27
    return (f'<path d="M{a},{y} L{a},{y + 6} L{b},{y + 6} L{b},{y}" class="muted-stroke" stroke-width="1.1"/>'
            f'<text x="{(a + b)/2}" y="{y + 24}" text-anchor="middle" class="mrm" font-size="14">{txt}</text>')
s.append(brace(0, yv, 78, '⌜y⌝'))
s.append(brace(-xv - 2, -2, 188, '⌜x⌝'))
s.append(brace(0, yv, 188, '⌜y⌝'))
s.append('<line x1="300" y1="104" x2="300" y2="132" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-smn)"/>')
s.insert(1, '<defs>' + marker('ah-smn') + '</defs>')
s.append('<text x="312" y="122" class="label">Pₓ writes ⌜x⌝ ⊔ in front of the input</text>')
s.append(f'<text x="{150 + 30*(h - lo)}" y="236" class="label">the head is on h = −x − 2, where Mₑ starts</text>')
s.append('</svg>')
out['smn-tape'] = ''.join(s)

# ---------------------------------------------------------------- halting: the diagonal table
conv_tab = ['↓↑↓↓↑↓↑', '↑↑↓↑↓↓↓', '↓↓↓↑↑↓↑', '↑↓↓↑↓↑↓', '↓↓↑↓↓↓↑', '↑↑↑↓↓↑↓']
c, x0, y0 = 34, 80, 34
ncol = len(conv_tab[0])
s = ['<svg class="fig" viewBox="0 0 440 330" width="440" role="img" aria-label="A table whose row e lists whether Phi_e converges or diverges on each input; the diagonal is marked; the row D reverses each diagonal entry">']
s.append(f'<text x="{x0 + ncol*c/2}" y="12" text-anchor="middle" class="label">input x</text>')
for j in range(ncol):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{y0 - 8}" text-anchor="middle" class="mrm muted" font-size="12">{j}</text>')
for i, r in enumerate(conv_tab):
    y = y0 + c * i
    s.append(sub('Φ', str(i), 40, y + 22, 16, cls='mrm'))
    for j, b in enumerate(r):
        s.append(f'<rect x="{x0 + c*j}" y="{y}" width="{c}" height="{c}" class="{"cell head-cell" if i == j else "cell"}"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{y + 23}" text-anchor="middle" class="mrm{"" if i == j else " muted"}" font-size="17">{b}</text>')
    s.append(f'<text x="{x0 + c*ncol + 12}" y="{y + 22}" class="mrm muted" font-size="15">⋯</text>')
s.append(f'<text x="{x0 + 3*c + c/2}" y="{y0 + c*len(conv_tab) + 16}" text-anchor="middle" class="mrm muted" font-size="15">⋮</text>')
yy = y0 + c * len(conv_tab) + 34
s.append(f'<line x1="{x0}" y1="{yy - 8}" x2="{x0 + c*ncol}" y2="{yy - 8}" class="axis"/>')
s.append(f'<text x="40" y="{yy + 22}" text-anchor="middle" class="math" font-size="16">D</text>')
for j in range(ncol):
    if j < len(conv_tab):
        b = '↑' if conv_tab[j][j] == '↓' else '↓'
        s.append(f'<rect x="{x0 + c*j}" y="{yy}" width="{c}" height="{c}" class="cell head-cell"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{yy + 23}" text-anchor="middle" class="mrm" font-size="17" font-weight="600">{b}</text>')
    else:
        s.append(f'<rect x="{x0 + c*j}" y="{yy}" width="{c}" height="{c}" class="cell"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{yy + 23}" text-anchor="middle" class="mrm muted" font-size="15">⋯</text>')
s.append(f'<text x="{x0 + c*ncol + 12}" y="{yy + 16}" class="label">D(x)↓ if and only if</text>')
s.append(f'<text x="{x0 + c*ncol + 12}" y="{yy + 32}" class="label">Φₓ(x)↑</text>')
s.append('</svg>')
out['halting-diagonal'] = ''.join(s)

# ---------------------------------------------------------------- a many-one reduction
s = ['<svg class="fig" viewBox="0 0 470 250" width="470" role="img" aria-label="Two copies of the integers, each split into a set and its complement; the reduction f sends the elements of A into B and the other elements outside B">',
     '<defs>' + marker('ah-red', 'accent-fill') + '</defs>']
L, R, top, hgt, w = 60, 300, 30, 200, 110
for (bx, name) in ((L, 'A'), (R, 'B')):
    s.append(f'<rect x="{bx}" y="{top}" width="{w}" height="{hgt}" rx="6" class="track-outline"/>')
    s.append(f'<rect x="{bx}" y="{top}" width="{w}" height="{hgt*0.45:.0f}" rx="6" class="soft-fill"/>')
    s.append(f'<line x1="{bx}" y1="{top + hgt*0.45:.0f}" x2="{bx + w}" y2="{top + hgt*0.45:.0f}" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<text x="{bx + w/2}" y="{top - 10}" text-anchor="middle" class="math" font-size="16">ℕ</text>')
    s.append(f'<text x="{bx + 14}" y="{top + 24}" class="math" font-size="16">{name}</text>')
    s.append(f'<text x="{bx + 14}" y="{top + hgt - 12}" class="mrm" font-size="15">ℕ ∖ <tspan class="math">{name}</tspan></text>')
left = [(115, 62), (95, 100), (130, 140), (100, 178), (135, 195)]
right = [(355, 70), (355, 70), (370, 160), (340, 185), (370, 160)]
for (a, b) in zip(left, right):
    x1, y1, x2, y2 = seg(a[0], a[1], b[0], b[1], 6, 8)
    s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-red)"/>')
for p in left + [(340, 185), (355, 70), (370, 160)]:
    s.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="4.5" class="ink-fill"/>')
for p in [(385, 100), (330, 104), (395, 205)]:
    s.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="4.5" class="muted-fill"/>')
s.append('<text x="235" y="118" text-anchor="middle" class="math" font-size="16">f</text>')
s.append('<text x="300" y="248" class="label">grey points: not values of f</text>')
s.append('</svg>')
out['reduction'] = ''.join(s)

# ---------------------------------------------------------------- dovetailing
def pair(x, y):
    n = x + y
    return n * (n + 1) // 2 + y
N = 5
wit = {(0, 2), (2, 1), (3, 0), (2, 3), (4, 3)}
c, x0, y0 = 40, 70, 30
s = ['<svg class="fig" viewBox="0 0 470 290" width="470" role="img" aria-label="A grid of pairs (x, y) numbered in the order of the pairing function; the cells where y is a witness for x are shaded; column 1 has no shaded cell">']
s.append(f'<text x="{x0 + N*c/2}" y="14" text-anchor="middle" class="label">element x</text>')
for x in range(N):
    s.append(f'<text x="{x0 + c*x + c/2}" y="{y0 - 4}" text-anchor="middle" class="mrm muted" font-size="12">{x}</text>')
s.append(f'<text x="18" y="{y0 + N*c/2}" text-anchor="middle" class="label" transform="rotate(-90 18 {y0 + N*c/2})">witness y</text>')
for y in range(N):
    s.append(f'<text x="{x0 - 10}" y="{y0 + c*y + 25}" text-anchor="end" class="mrm muted" font-size="12">{y}</text>')
    for x in range(N):
        on = (x, y) in wit
        s.append(f'<rect x="{x0 + c*x}" y="{y0 + c*y}" width="{c}" height="{c}" class="{"cell head-cell" if on else "cell"}"/>')
        s.append(f'<text x="{x0 + c*x + c/2}" y="{y0 + c*y + 25}" text-anchor="middle" class="mrm{"" if on else " muted"}" font-size="14">{pair(x, y)}</text>')
for x in range(N):
    s.append(f'<text x="{x0 + c*x + c/2}" y="{y0 + c*N + 18}" text-anchor="middle" class="mrm muted" font-size="14">⋮</text>')
seq = []
for n in range(15):
    for x in range(N):
        for y in range(N):
            if pair(x, y) == n:
                seq.append(str(x) if (x, y) in wit else 'a')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 20}" class="label">f(0), f(1), …, f(14):</text>')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 42}" class="mrm" font-size="14">{", ".join(seq[:8])},</text>')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 62}" class="mrm" font-size="14">{", ".join(seq[8:])}, …</text>')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 100}" class="label">column 1 has no witness:</text>')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 116}" class="label">1 ∉ A, and a search through</text>')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 132}" class="label">this column alone would</text>')
s.append(f'<text x="{x0 + c*N + 20}" y="{y0 + 148}" class="label">never end</text>')
s.append('</svg>')
out['dovetailing'] = ''.join(s)

# ---------------------------------------------------------------- computable, c.e. and co-c.e. sets
s = ['<svg class="fig" viewBox="0 0 520 250" width="520" role="img" aria-label="Two overlapping regions, the c.e. sets and the co-c.e. sets, inside the box of all sets; their intersection is the computable sets">']
s.append('<rect x="4" y="4" width="512" height="242" rx="8" class="track-outline"/>')
s.append('<text x="18" y="26" class="label">all subsets of ℕ</text>')
s.append('<ellipse cx="200" cy="128" rx="140" ry="88" class="soft-fill" fill-opacity="0.6"/>')
s.append('<ellipse cx="320" cy="128" rx="140" ry="88" class="soft-fill" fill-opacity="0.6"/>')
s.append('<ellipse cx="200" cy="128" rx="140" ry="88" class="accent-stroke" stroke-width="1.3"/>')
s.append('<ellipse cx="320" cy="128" rx="140" ry="88" class="accent-stroke" stroke-width="1.3"/>')
s.append('<text x="112" y="92" text-anchor="middle" class="label">c.e.</text>')
s.append('<text x="408" y="92" text-anchor="middle" class="label">co-c.e.</text>')
s.append('<text x="260" y="88" text-anchor="middle" class="label">computable</text>')
s.append('<text x="260" y="122" text-anchor="middle" class="mrm" font-size="15">∅, ℕ, evens</text>')
s.append('<text x="130" y="128" text-anchor="middle" class="mrm" font-size="15">∅′, <tspan class="math">H</tspan></text>')
s.append('<text x="130" y="152" text-anchor="middle" class="mrm" font-size="13">{<tspan class="math">e</tspan> : <tspan class="math">W</tspan><tspan class="math" font-size="9" dy="3">e</tspan><tspan dy="-3"> ≠ ∅}</tspan></text>')
s.append('<text x="390" y="128" text-anchor="middle" class="mrm" font-size="15">ℕ ∖ ∅′</text>')
s.append('<text x="390" y="152" text-anchor="middle" class="mrm" font-size="13">{<tspan class="math">e</tspan> : <tspan class="math">W</tspan><tspan class="math" font-size="9" dy="3">e</tspan><tspan dy="-3"> = ∅}</tspan></text>')
s.append('<text x="500" y="26" text-anchor="end" class="label">neither: <tspan class="mrm" font-size="14">Tot, Inf</tspan></text>')
s.append('</svg>')
out['classes'] = ''.join(s)

# ---------------------------------------------------------------- Owings' matrix
rows = ['0', '1', '2', '3', 'v']
cols = ['0', '1', '2', '3', 'v']
cw, ch, x0, y0 = 78, 34, 70, 34
s = ['<svg class="fig" viewBox="0 0 560 250" width="560" role="img" aria-label="A matrix whose entry in row n and column x is the index Phi_n(x); the diagonal is the row of the function d; row v is the diagonal transformed by f; they meet at the entry (v, v)">']
s.append(f'<text x="{x0 + 2.5*cw}" y="12" text-anchor="middle" class="label">column x</text>')
def gap(k):
    return 1 if k >= 4 else 0
def X(j): return x0 + cw * j + 26 * gap(j)
def Y(i): return y0 + ch * i + 26 * gap(i)
for j, cl in enumerate(cols):
    s.append(f'<text x="{X(j) + cw/2}" y="{y0 - 8}" text-anchor="middle" class="{"math" if cl == "v" else "mrm"} muted" font-size="13">{cl}</text>')
for i, rl in enumerate(rows):
    s.append(f'<text x="{x0 - 14}" y="{Y(i) + 22}" text-anchor="end" class="label">row <tspan class="{"math" if rl == "v" else "mrm"}" font-size="14">{rl}</tspan></text>')
    for j, cl in enumerate(cols):
        diag = i == j
        rowv = rl == 'v'
        klass = 'cell head-cell' if diag else 'cell'
        s.append(f'<rect x="{X(j)}" y="{Y(i)}" width="{cw}" height="{ch}" class="{klass}"/>')
        if rowv and not diag:
            s.append(f'<rect x="{X(j)}" y="{Y(i)}" width="{cw}" height="{ch}" class="soft-fill" fill-opacity="0.5"/>')
        if rowv:
            vv = '<tspan class="math">v</tspan>'
            arg = cl if cl != 'v' else vv
            txt = f'<tspan class="math">f</tspan>(<tspan class="math">d</tspan>({arg}))'
        else:
            nn = rl if rl != 'v' else '<tspan class="math">v</tspan>'
            xx = cl if cl != 'v' else '<tspan class="math">v</tspan>'
            txt = f'Φ<tspan font-size="9" dy="3">{nn}</tspan><tspan dy="-3">({xx})</tspan>'
        s.append(f'<text x="{X(j) + cw/2}" y="{Y(i) + 22}" text-anchor="middle" class="mrm" font-size="13">{txt}</text>')
    s.append(f'<text x="{X(4) - 14}" y="{Y(i) + 22}" text-anchor="middle" class="mrm muted" font-size="13">⋯</text>')
for j in range(5):
    s.append(f'<text x="{X(j) + cw/2}" y="{Y(4) - 8}" text-anchor="middle" class="mrm muted" font-size="13">⋮</text>')
s.append(f'<rect x="{X(4) - 3}" y="{Y(4) - 3}" width="{cw + 6}" height="{ch + 6}" class="track-outline"/>')
s.append('</svg>')
out['owings'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
print(', '.join(f'{k}: {len(v)} chars' for k, v in out.items()))
