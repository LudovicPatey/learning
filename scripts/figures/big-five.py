# Generates the inline SVG figures of the course on the Big Five.
# Usage: python3 scripts/figures/big-five.py out.json
# Paste each figure into the lesson that uses it:
#   konig-tree                 -> aca0-reversals.md
#   separation-choice          -> separation-heine-borel.md
#   cantor-cover               -> separation-heine-borel.md
#   jump-hierarchy             -> atr0-pi11ca0.md
# The output is deterministic: every loop runs over sorted or ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, s, x, y, size=16, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')


# ---------------------------------------------------------------- the tree of the reversal of Koenig's lemma
# f(0), f(1), ... ; 3 and 5 are not in the range.
F = [2, 0, 4, 1, 6, 7, 8, 9, 10, 11]
DEPTH = 5


def in_tree(sig):
    n = len(sig)
    for m in range(n):
        v = sig[m]
        if v > 0:
            if not (v - 1 < len(F) and F[v - 1] == m):
                return False
        elif any(F[i] == m for i in range(n)):
            return False
    return True


def children(sig):
    res = []
    for v in range(0, len(F) + 1):
        if in_tree(sig + (v,)):
            res.append(sig + (v,))
    return res


nodes = [()]
frontier = [()]
for d in range(DEPTH):
    nxt = []
    for sig in frontier:
        nxt += children(sig)
    nodes += nxt
    frontier = nxt
path = tuple(frontier[0])  # the unique node of length DEPTH
assert len(frontier) == 1

# horizontal positions: leaves in order, parents centered
leaves = [n for n in nodes if not any(len(m) == len(n) + 1 and m[:-1] == n for m in nodes)]
xs = {}
for k, lf in enumerate(sorted(leaves)):
    xs[lf] = 70 + k * 120
for d in range(DEPTH - 1, -1, -1):
    for n in nodes:
        if len(n) == d and n not in xs:
            ch = [m for m in nodes if len(m) == d + 1 and m[:-1] == n]
            xs[n] = sum(xs[c] for c in ch) / len(ch)


def kpos(n):
    return xs[n], 76 + len(n) * 46


alive = {path[:k] for k in range(DEPTH + 1)}
s = ['<svg class="fig" viewBox="0 0 600 360" width="600" role="img" aria-label="The tree of the reversal of König’s lemma for an injection f: the nodes that guess a value 0 too early die, and the unique infinite path lists, at each position m, either i+1 with f(i)=m or 0">']
for n in sorted(nodes, key=lambda n: (len(n), n)):
    if n == ():
        continue
    (x1, y1), (x2, y2) = kpos(n[:-1]), kpos(n)
    on = n in alive
    cls = 'accent-stroke' if on else 'muted-stroke'
    dash = '' if on else ' stroke-dasharray="3 3"'
    sw = '2.2' if on else '1.2'
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{sw}"{dash}/>')
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    s.append(f'<text x="{mx + (8 if x2 >= x1 else -8):.1f}" y="{my + 4}" text-anchor="{"start" if x2 >= x1 else "end"}" class="mrm" font-size="13">{n[-1]}</text>')
for n in sorted(nodes, key=lambda n: (len(n), n)):
    x, y = kpos(n)
    if n in alive:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="accent-fill"/>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.5" class="muted-fill"/>')
x, y = kpos(path)
s.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm" font-size="12">⋮</text>')
s.append(f'<text x="{kpos(())[0] + 10:.1f}" y="{kpos(())[1] - 6}" class="mrm" font-size="13">ε</text>')
for m in range(DEPTH):
    s.append(f'<text x="560" y="{76 + m * 46 + 28}" text-anchor="end" class="label">position {m}</text>')
# the values of f
s.append('<text x="20" y="20" class="label">the injection f:</text>')
for i in range(6):
    s.append(f'<text x="{20 + i * 62}" y="{38 + 0}" class="math" font-size="14">f<tspan class="mrm">({i}) = {F[i]}</tspan></text>')
s.append('<line x1="24" y1="346" x2="44" y2="346" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="350" class="label">0 guessed at m, then f(i) = m appears</text>')
s.append('<line x1="320" y1="346" x2="340" y2="346" class="accent-stroke" stroke-width="2.2"/><text x="346" y="350" class="label">the unique infinite path</text>')
s.append('</svg>')
out['konig-tree'] = ''.join(s)

# ---------------------------------------------------------------- the choices made by a separating set
# infinite branches: extensions of 100, 1011, 11 ; finite parts drawn dashed
D2 = 4
infinite = ['1000', '1100', '1110', '1111']
finite = ['0', '00', '000', '01', '1001', '101', '1010', '1101']
tree2 = {''}
for w in infinite + finite:
    for k in range(len(w) + 1):
        tree2.add(w[:k])
aliveset = {w[:k] for w in infinite for k in range(len(w) + 1)}
P = '1000'


def bpos(s_):
    d = len(s_)
    idx = int(s_, 2) if s_ else 0
    return 20 + (idx + 0.5) * 340 / (2 ** d), 28 + d * 52


s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="A binary tree: at the root only the right successor is extendible to every length, so the separating set sends the path to the right; at the node 1 both successors are extendible and either choice is correct">']
for n in sorted(tree2, key=lambda n: (len(n), n)):
    if n == '':
        continue
    (x1, y1), (x2, y2) = bpos(n[:-1]), bpos(n)
    if P.startswith(n):
        cls, sw, dash = 'accent-stroke', '2.2', ''
    elif n in aliveset:
        cls, sw, dash = 'ink-stroke', '1.2', ''
    else:
        cls, sw, dash = 'muted-stroke', '1.2', ' stroke-dasharray="3 3"'
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{sw}"{dash}/>')
for n in sorted(tree2, key=lambda n: (len(n), n)):
    x, y = bpos(n)
    if P.startswith(n):
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="accent-fill"/>')
    elif n in aliveset:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.5" class="ink-fill"/>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3" class="muted-fill"/>')
for w in infinite:
    x, y = bpos(w)
    s.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm{"" if w == P else " muted"}" font-size="12">⋮</text>')
s.append(f'<text x="{bpos("")[0] + 10:.1f}" y="{bpos("")[1] - 6}" class="mrm" font-size="13">ε</text>')
notes = [
    ('', 'only 1 is extendible to every length:', 'φ(ε) holds, so ε ∈ S: go to 1'),
    ('1', 'both successors are extendible:', 'either choice made by S is correct'),
    ('10', 'only 100 is extendible (101 dies):', 'ψ(10) holds, so 10 ∉ S: go to 100'),
]
for k, (n, a, b) in enumerate(notes):
    x, y = bpos(n)
    ty = 40 + k * 70
    s.append(f'<line x1="{x + 6:.1f}" y1="{y}" x2="376" y2="{ty + 4}" class="muted-stroke" stroke-width="0.8" stroke-dasharray="2 3"/>')
    s.append(f'<text x="380" y="{ty}" class="label">{a}</text>')
    s.append(f'<text x="380" y="{ty + 15}" class="label">{b}</text>')
s.append('<line x1="24" y1="278" x2="44" y2="278" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="282" class="label">not extendible to every length</text>')
s.append('<line x1="270" y1="278" x2="290" y2="278" class="accent-stroke" stroke-width="2.2"/><text x="296" y="282" class="label">the path P defined from S</text>')
s.append('</svg>')
out['separation-choice'] = ''.join(s)

# ---------------------------------------------------------------- the cover of [0,1] built from a tree
L, R = 40, 560
W = R - L


def cint(sig):
    a = sum(2 * int(c) * 3 ** (-(i + 1)) for i, c in enumerate(sig))
    return a, a + 3 ** (-len(sig))


def X(t):
    return L + t * W


T3 = {'', '0', '1', '00', '10', '11'}
minimal = sorted({w for w in ['01', '000', '001', '100', '101', '110', '111']}, key=lambda w: cint(w)[0])
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The intervals of the Cantor set at levels 0 to 3; the strings outside the tree give enlarged open intervals, which together with the removed middle thirds cover the unit interval">']
for d in range(4):
    y = 22 + d * 36
    s.append(f'<text x="{L - 12}" y="{y + 13}" text-anchor="end" class="label">{d}</text>')
    for k in range(2 ** d):
        sig = format(k, f'0{d}b') if d else ''
        a, b = cint(sig)
        cls = 'cell head-cell' if sig in T3 else 'cell'
        s.append(f'<rect x="{X(a):.1f}" y="{y}" width="{X(b) - X(a):.1f}" height="18" class="{cls}"/>')
        if d <= 2 or sig in minimal:
            lab = sig if sig else 'ε'
            s.append(f'<text x="{(X(a) + X(b)) / 2:.1f}" y="{y + 13}" text-anchor="middle" class="mrm" font-size="11">{lab}</text>')
s.append(f'<text x="{L - 12}" y="12" text-anchor="end" class="label">level</text>')
# the cover
yc = 186
s.append(f'<line x1="{L}" y1="{yc + 40}" x2="{R}" y2="{yc + 40}" class="axis"/>')
for t, lab in [(0, '0'), (1, '1')]:
    s.append(f'<line x1="{X(t):.1f}" y1="{yc + 36}" x2="{X(t):.1f}" y2="{yc + 44}" class="ink-stroke" stroke-width="1"/>')
    s.append(f'<text x="{X(t):.1f}" y="{yc + 58}" text-anchor="middle" class="mrm" font-size="12">{lab}</text>')
for k, w in enumerate(minimal):
    a, b = cint(w)
    e = 3 ** (-len(w) - 1)
    yy = yc + (k % 2) * 14
    s.append(f'<line x1="{X(a - e):.1f}" y1="{yy}" x2="{X(b + e):.1f}" y2="{yy}" class="accent-stroke" stroke-width="3"/>')
    s.append(f'<line x1="{X(a):.1f}" y1="{yy - 4}" x2="{X(a):.1f}" y2="{yy + 4}" class="accent-stroke" stroke-width="1"/>')
    s.append(f'<line x1="{X(b):.1f}" y1="{yy - 4}" x2="{X(b):.1f}" y2="{yy + 4}" class="accent-stroke" stroke-width="1"/>')
# middle thirds of levels 0 to 2 (deeper ones are inside the U_sigma)
for d in range(3):
    for k in range(2 ** d):
        sig = format(k, f'0{d}b') if d else ''
        a, b = cint(sig)
        l3 = (b - a) / 3
        s.append(f'<line x1="{X(a + l3):.1f}" y1="{yc + 30}" x2="{X(a + 2 * l3):.1f}" y2="{yc + 30}" class="muted-stroke" stroke-width="3"/>')
s.append(f'<rect x="{L}" y="272" width="16" height="10" class="cell head-cell"/><text x="{L + 22}" y="281" class="label">strings of T</text>')
s.append(f'<line x1="{L + 130}" y1="277" x2="{L + 150}" y2="277" class="accent-stroke" stroke-width="3"/><text x="{L + 156}" y="281" class="label">U for minimal σ ∉ T</text>')
s.append(f'<line x1="{L + 300}" y1="277" x2="{L + 320}" y2="277" class="muted-stroke" stroke-width="3"/><text x="{L + 326}" y="281" class="label">removed middle thirds</text>')
s.append('</svg>')
out['cantor-cover'] = ''.join(s)

# ---------------------------------------------------------------- a jump hierarchy along omega + 2
pts = [('0', 70), ('1', 130), ('2', 190), ('3', 250), ('ω', 420), ('ω+1', 500)]
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="A jump hierarchy along the well-ordering omega+2: each column is the jump of the join of the previous columns">',
     '<defs>' + marker('ah-jh') + '</defs>']
ybase = 150
s.append(f'<line x1="40" y1="{ybase}" x2="560" y2="{ybase}" class="axis"/>')
for lab, x in pts:
    s.append(f'<rect x="{x - 16}" y="{ybase - 92}" width="32" height="84" class="cell{" head-cell" if lab == "ω" else ""}"/>')
    s.append(f'<line x1="{x}" y1="{ybase - 4}" x2="{x}" y2="{ybase + 4}" class="ink-stroke" stroke-width="1"/>')
    s.append(f'<text x="{x}" y="{ybase + 22}" text-anchor="middle" class="mrm" font-size="14">{lab}</text>')
s.append(f'<text x="335" y="{ybase - 46}" text-anchor="middle" class="mrm" font-size="16">⋯</text>')
s.append(f'<text x="335" y="{ybase + 22}" text-anchor="middle" class="mrm" font-size="14">⋯</text>')
# bracket over the columns below omega, and the arrow to column omega
s.append(f'<path d="M54,{ybase - 100} L54,{ybase - 108} L266,{ybase - 108} L266,{ybase - 100}" class="muted-stroke" fill="none" stroke-width="1"/>')
s.append(f'<text x="160" y="{ybase - 116}" text-anchor="middle" class="label">the columns j &lt; ω</text>')
s.append(f'<path d="M266,{ybase - 104} C330,{ybase - 104} 400,{ybase - 116} 418,{ybase - 98}" class="accent-stroke" fill="none" stroke-width="1.4" marker-end="url(#ah-jh)"/>')
s.append(f'<text x="420" y="{ybase - 122}" text-anchor="middle" class="label">column ω: the jump of their join</text>')
s.append(f'<path d="M430,{ybase - 98} Q465,{ybase - 116} 494,{ybase - 98}" class="ink-stroke" fill="none" stroke-width="1.2" marker-end="url(#ah-jh)"/>')
s.append('</svg>')
out['jump-hierarchy'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
