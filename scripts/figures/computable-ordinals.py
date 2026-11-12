# Generates the inline SVG figures of the course on computable ordinals.
# Usage: python3 scripts/figures/computable-ordinals.py out.json
# Paste each figure into the lesson that uses it:
#   order-types                -> ordinals.md
#   special-last               -> computable-well-orderings.md
#   o-tree                     -> kleene-o.md
#   kb-order                   -> well-founded-trees.md
#   o-completeness             -> trees-and-pi11.md
#   spector                    -> boundedness.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='muted-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def text(x, y, body, cls='mrm', size=15, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{body}</text>'


def lsub(t):
    """A subscript inside a label (returns to the baseline afterwards)."""
    return f'<tspan font-size="9" dy="3">{t}</tspan><tspan dy="-3"> </tspan>'


def msub(base, t, size=15):
    return f'<tspan class="math">{base}</tspan><tspan class="math" font-size="{int(size * 0.7)}" dy="4">{t}</tspan>'


def sup(base, exp, size=15, base_cls='mrm'):
    """Inner markup for base^exp (the caller wraps it in a text element)."""
    return f'<tspan class="{base_cls}">{base}</tspan><tspan font-size="{int(size * 0.7)}" dy="-7">{exp}</tspan>'


# ---------------------------------------------------------------- order types
def omega_points(x0, width, n=11):
    """Positions of an omega-sequence compressed into [x0, x0 + width)."""
    pts, x, step = [], x0, width * 0.32
    for _ in range(n):
        pts.append(x)
        x += step
        step *= 0.68
    return pts


OM = '<tspan class="math">ω</tspan>'
rows = [
    ('w', OM, [(0, 300, False)], []),
    ('w+1', OM + '<tspan class="mrm">\u00a0+ 1</tspan>', [(0, 300, False)], [330]),
    ('w2', OM + '<tspan class="mrm">\u00a0· 2</tspan>', [(0, 200, False), (230, 200, False)], []),
    ('ww', OM + '<tspan class="mrm" font-size="11" dy="-7">2</tspan>', [(0, 96, False), (112, 96, False), (224, 96, False), (336, 96, False)], []),
]
X0, LW = 120, 470
H = 30 + 46 * len(rows) + 10
s = [f'<svg class="fig" viewBox="0 0 {X0 + LW + 30} {H}" width="{X0 + LW + 30}" role="img" '
     'aria-label="Four well-orderings drawn as dots from left to right: omega, omega plus one, omega times two, omega squared">']
for i, (name, shown, blocks, extra) in enumerate(rows):
    y = 30 + 46 * i
    s.append(f'<text x="{X0 - 24}" y="{y + 5}" text-anchor="end" font-size="17">{shown}</text>')
    s.append(f'<line x1="{X0 - 6}" y1="{y}" x2="{X0 + LW}" y2="{y}" class="axis"/>')
    for (bx, bw, _) in blocks:
        for x in omega_points(X0 + bx, bw):
            s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.2" class="ink-fill"/>')
    if name == 'ww':
        s.append(text(X0 + 452, y + 5, '⋯', 'mrm muted', 15))
    for ex in extra:
        s.append(f'<circle cx="{X0 + ex:.1f}" cy="{y}" r="4.2" class="accent-fill"/>')
        s.append(text(X0 + ex + 14, y + 4, 'largest element', 'label', 12, 'start'))
s.append('</svg>')
out['order-types'] = ''.join(s)

# ---------------------------------------------------------------- f(n): omega or omega + 1
N, c, x0 = 12, 34, 150
s = ['<svg class="fig" viewBox="0 0 600 132" width="600" role="img" '
     'aria-label="Two orders on the natural numbers: the usual order, and the usual order with the special number 3 moved to the end">']
labels = [('n ∉ ∅′', 'type ω', list(range(N)), None), ('n ∈ ∅′ at stage 3', 'type ω + 1', [k for k in range(N) if k != 3], 3)]
for i, (lab, typ, order, special) in enumerate(labels):
    y = 40 + 56 * i
    s.append(text(x0 - 18, y + 5, lab, 'label', 12, 'end'))
    s.append(f'<line x1="{x0 - 6}" y1="{y - 12}" x2="{x0 - 6}" y2="{y + 12}" class="axis"/>')
    for j, k in enumerate(order[:N - 1]):
        s.append(text(x0 + c * j + 6, y + 5, str(k), 'mrm', 15))
    s.append(text(x0 + c * (N - 1) + 4, y + 5, '⋯', 'mrm muted', 15))
    if special is not None:
        xs = x0 + c * (N - 1) + 34
        s.append(f'<rect x="{xs - 12}" y="{y - 13}" width="24" height="24" rx="4" class="head-cell"/>')
        s.append(text(xs, y + 5, str(special), 'mrm', 15))
    s.append(text(x0 + c * (N - 1) + 34, y - 20, typ, 'label', 12))
s.append('</svg>')
out['special-last'] = ''.join(s)

# ---------------------------------------------------------------- the partial order <_O
s = ['<svg class="fig" viewBox="0 0 600 214" width="600" role="img" '
     'aria-label="Kleene\'s O near omega: the chain of notations of the finite ordinals, and two notations of omega on different branches, each with its successors">',
     '<defs>' + marker('co-otree') + '</defs>']
fin = [('1', None), ('2', None), (sup('2', '2'), None), (sup('2', '4'), None)]
y0 = 120
xs = [40, 100, 160, 220]
for x, (lab, _) in zip(xs, fin):
    s.append(f'<circle cx="{x}" cy="{y0}" r="4" class="ink-fill"/>')
    s.append(f'<text x="{x}" y="{y0 + 24}" text-anchor="middle" class="mrm" font-size="15">{lab}</text>')
for a, b in zip(xs, xs[1:]):
    s.append(f'<line x1="{a + 6}" y1="{y0}" x2="{b - 7}" y2="{y0}" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/>')
s.append(text(262, y0 + 5, '⋯', 'mrm muted', 16))
for k, (y, e) in enumerate([(52, 'e'), (188, "e′")]):
    xl = 330
    s.append(f'<line x1="282" y1="{y0}" x2="{xl - 8}" y2="{y + (6 if y < y0 else -6)}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#co-otree)"/>')
    s.append(f'<circle cx="{xl}" cy="{y}" r="5" class="accent-fill"/>')
    lab = f'<tspan class="mrm">3·5</tspan><tspan class="math" font-size="10" dy="-7">{e}</tspan>'
    ly = y - 12 if y < y0 else y + 26
    s.append(f'<text x="{xl}" y="{ly}" text-anchor="middle" font-size="15">{lab}</text>')
    xprev = xl
    for j, xn in enumerate([420, 510]):
        s.append(f'<line x1="{xprev + 7}" y1="{y}" x2="{xn - 7}" y2="{y}" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/>')
        s.append(f'<circle cx="{xn}" cy="{y}" r="4" class="ink-fill"/>')
        xprev = xn
    s.append(text(560, y + 5, '⋯', 'mrm muted', 16))
    s.append(text(420, y - 12, '|·| = ω + 1', 'label', 12))
    s.append(text(510, y - 12, '|·| = ω + 2', 'label', 12))
s.append(text(130, y0 - 22, 'notations of 0, 1, 2, 3', 'label', 12))
s.append(text(332, y0 + 5, 'incomparable', 'label', 12, 'start'))
s.append('</svg>')
out['o-tree'] = ''.join(s)

# ---------------------------------------------------------------- Kleene-Brouwer order on a small tree
nodes = ['', '0', '00', '000', '01', '1', '2', '20']
pos = {'': (300, 34), '0': (150, 104), '1': (300, 104), '2': (450, 104),
       '00': (100, 174), '01': (200, 174), '20': (450, 174), '000': (100, 244)}


def kb_key(sig):
    # sigma <_KB tau iff sigma extends tau properly, or is to the left at the first difference.
    return [int(ch) for ch in sig] + [10 ** 6]


def kb_less(a, b):
    if len(a) > len(b) and a.startswith(b):
        return True
    for x, y in zip(a, b):
        if x != y:
            return x < y
    return False


order = sorted(nodes, key=lambda n: sum(1 for m in nodes if kb_less(m, n)))
kbpos = {n: i for i, n in enumerate(order)}


def rank(sig):
    ch = [m for m in nodes if len(m) == len(sig) + 1 and m.startswith(sig)]
    return max((rank(m) + 1 for m in ch), default=0)


s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" '
     'aria-label="A finite tree; each node carries its rank and its position in the Kleene-Brouwer ordering">']
for n in nodes:
    if n:
        (x1, y1), (x2, y2) = pos[n[:-1]], pos[n]
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.3"/>')
for n in nodes:
    x, y = pos[n]
    s.append(f'<circle cx="{x}" cy="{y}" r="13" class="node"/>')
    s.append(text(x, y + 5, str(kbpos[n]), 'mrm', 14))
    name = '⟨⟩' if n == '' else '⟨' + ','.join(n) + '⟩'
    s.append(text(x - 20, y + 5, name, 'mrm', 13, 'end'))
    s.append(text(x + 20, y + 5, f'rk {rank(n)}', 'label', 12, 'start'))
s.append('<circle cx="340" cy="244" r="11" class="node"/>')
s.append(text(358, 248, 'position in the Kleene–Brouwer order', 'label', 12, 'start'))
s.append(text(340, 276, 'rk: rank of the subtree above the node', 'label', 12, 'start'))
s.append('</svg>')
out['kb-order'] = ''.join(s)

# ---------------------------------------------------------------- the reduction of WF to O
s = ['<svg class="fig" viewBox="0 0 600 222" width="600" role="img" '
     'aria-label="The notation F(b, sigma) is the limit of a chain c0, c1, c2 starting above b; each step builds the notation of a subtree on top of the previous element of the chain">',
     '<defs>' + marker('co-red') + marker('co-red-acc', 'accent-fill') + '</defs>']
y = 120
pts = [(40, 'b'), (110, 'c0'), (250, 'c1'), (390, 'c2')]
for (xa, _), (xb, _) in zip(pts, pts[1:]):
    s.append(f'<line x1="{xa + 6}" y1="{y}" x2="{xb - 7}" y2="{y}" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-red)"/>')
s.append(f'<line x1="396" y1="{y}" x2="460" y2="{y}" class="ink-stroke" stroke-width="1.3" stroke-dasharray="4 3"/>')
for x, lab in pts:
    s.append(f'<circle cx="{x}" cy="{y}" r="4.5" class="ink-fill"/>')
    body = msub(lab[0], lab[1:], 16) if len(lab) > 1 else lab
    s.append(text(x, y + 26, body, 'math', 16))
s.append(f'<circle cx="540" cy="{y}" r="5.5" class="accent-fill"/>')
s.append(text(540, y + 26, 'F(b, σ)', 'math', 16))
s.append(text(500, y + 5, '⋯', 'mrm muted', 16))
for k, (xa, xb) in enumerate([(110, 250), (250, 390)]):
    xm = (xa + xb) / 2
    s.append(f'<path d="M{xa + 4},{y - 8} Q{xm - 30},{y - 70} {xm - 6},{y - 58}" class="accent-stroke" stroke-width="1.3" marker-end="url(#co-red-acc)"/>')
    s.append(f'<circle cx="{xm}" cy="{y - 56}" r="4" class="accent-fill"/>')
    s.append(f'<path d="M{xm + 6},{y - 54} Q{xm + 40},{y - 40} {xb - 6},{y - 9}" class="muted-stroke" stroke-width="1.2" marker-end="url(#co-red)"/>')
    s.append(f'<text x="{xm}" y="{y - 70}" text-anchor="middle" font-size="14"><tspan class="math">F</tspan><tspan class="mrm">(</tspan>'
             + msub('c', str(k), 14) + f'<tspan class="mrm" dy="-4">,\u00a0</tspan><tspan class="math">σ</tspan><tspan class="mrm">{k})</tspan></text>')
s.append(text(40, 186, 'For σk ∈ T, the notation of the subtree above σk is built on top of c'
              + lsub('k') + ', and c' + lsub('k+1') + ' is its successor;', 'label', 12, 'start'))
s.append(text(40, 204, 'for σk ∉ T, c' + lsub('k+1') + ' is the successor of c' + lsub('k')
              + '.', 'label', 12, 'start'))
s.append('</svg>')
out['o-completeness'] = ''.join(s)

# ---------------------------------------------------------------- Spector's argument
s = ['<svg class="fig" viewBox="0 0 600 150" width="600" role="img" '
     'aria-label="The order types of the members of A, drawn on the line of computable ordinals, are cofinal below omega one CK; every computable well-ordering embeds into one of them">',
     '<defs>' + marker('co-sp') + '</defs>']
y = 92
s.append(f'<line x1="30" y1="{y}" x2="520" y2="{y}" class="axis"/>')
s.append(f'<line x1="520" y1="{y - 10}" x2="520" y2="{y + 10}" class="ink-stroke" stroke-width="1.4"/>')
s.append(f'<text x="520" y="{y + 30}" text-anchor="middle" font-size="16"><tspan class="math">ω</tspan>'
         '<tspan class="mrm" font-size="11" dy="4">1</tspan><tspan class="mrm" font-size="10" dy="-11">CK</tspan></text>')
s.append(text(30, y + 30, '0', 'mrm', 15))
xs = [80, 170, 250, 318, 372, 414, 446, 470, 488, 500]
for x in xs:
    s.append(f'<circle cx="{x}" cy="{y}" r="4" class="accent-fill"/>')
s.append(text(250, y + 30, 'the types |L' + lsub('d') + '|, d ∈ A', 'label', 12))
s.append(f'<line x1="210" y1="{y - 34}" x2="210" y2="{y - 6}" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<text x="210" y="{y - 40}" text-anchor="middle" font-size="15"><tspan class="mrm">|</tspan>' + msub('L', 'e') + '<tspan class="mrm" dy="-4">|</tspan></text>')
s.append(f'<path d="M216,{y - 30} Q262,{y - 52} 312,{y - 10}" class="muted-stroke" stroke-width="1.2" marker-end="url(#co-sp)"/>')
s.append(text(330, y - 46, 'L' + lsub('e') + ' embeds into some L' + lsub('d'), 'label', 12, 'start'))
s.append('</svg>')
out['spector'] = ''.join(s)

with open(sys.argv[1], 'w') as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
