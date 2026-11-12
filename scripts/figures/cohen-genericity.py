# Generates the inline SVG figures of the course on Cohen genericity.
# Usage: python3 scripts/figures/cohen-genericity.py out.json
# Paste each figure into the lesson that uses it:
#   baire-splitting        -> baire-category.md
#   kurtz-blocks           -> weak-genericity.md
#   meet-or-avoid          -> one-genericity.md
#   jockusch-shore-coding  -> posner-robinson.md
#   genericity-hierarchy   -> n-genericity.md
# The output is deterministic.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, s, x, y, size=16, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')


def brace(x1, x2, y, label, up=False):
    """A horizontal bracket from x1 to x2 at height y, with a label below (or above)."""
    d = -6 if up else 6
    path = f'M{x1},{y} L{x1},{y + d} L{x2},{y + d} L{x2},{y}'
    ty = y + d + (-6 if up else 16)
    return (f'<path d="{path}" class="muted-stroke" stroke-width="1.2"/>'
            f'<text x="{(x1 + x2) / 2:.1f}" y="{ty}" text-anchor="middle" class="label">{label}</text>')


# ---------------------------------------------------------------- Baire category: the splitting construction
# Interval picture of the cylinders [sigma_rho]. Each row is one level; inside the
# half [sigma_rho i] (dashed) the construction chooses the cylinder of an extension
# in D_|rho| (solid).
L, R = 40, 520
rows_y = [36, 104, 172, 240]
# relative position of the chosen sub-interval inside each half, per string
choice = {'0': (0.10, 0.75), '1': (0.30, 0.90), '00': (0.20, 0.85), '01': (0.05, 0.60),
          '10': (0.35, 0.95), '11': (0.10, 0.70),
          '000': (0.2, 0.8), '001': (0.1, 0.7), '010': (0.3, 0.9), '011': (0.2, 0.75),
          '100': (0.1, 0.65), '101': (0.25, 0.85), '110': (0.3, 0.9), '111': (0.1, 0.6)}
iv = {'': (L, R)}
halves = {}
for depth in range(1, 4):
    for rho in sorted(k for k in iv if len(k) == depth - 1):
        a, b = iv[rho]
        m = (a + b) / 2
        for i, (l, r) in enumerate([(a, m), (m, b)]):
            key = rho + str(i)
            halves[key] = (l, r)
            p, q = choice[key]
            iv[key] = (l + p * (r - l), l + q * (r - l))
s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Nested cylinders in the proof of the Baire category theorem: each cylinder of the construction splits into two halves, and inside each half the construction chooses a smaller cylinder belonging to the next dense set">']
path = '01'
for depth in range(4):
    y = rows_y[depth]
    for rho in sorted(k for k in iv if len(k) == depth):
        a, b = iv[rho]
        if depth > 0:
            hl, hr = halves[rho]
            s.append(f'<line x1="{hl + 1:.1f}" y1="{y - 9}" x2="{hr - 1:.1f}" y2="{y - 9}" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/>')
            s.append(f'<line x1="{hl + 1:.1f}" y1="{y - 13}" x2="{hl + 1:.1f}" y2="{y - 5}" class="muted-stroke" stroke-width="1"/>')
            s.append(f'<line x1="{hr - 1:.1f}" y1="{y - 13}" x2="{hr - 1:.1f}" y2="{y - 5}" class="muted-stroke" stroke-width="1"/>')
        on = path.startswith(rho) and depth <= 2
        cls = 'accent-stroke' if on else 'ink-stroke'
        sw = 3 if on else 2
        s.append(f'<line x1="{a:.1f}" y1="{y}" x2="{b:.1f}" y2="{y}" class="{cls}" stroke-width="{sw}"/>')
        s.append(f'<line x1="{a:.1f}" y1="{y - 5}" x2="{a:.1f}" y2="{y + 5}" class="{cls}" stroke-width="1.2"/>')
        s.append(f'<line x1="{b:.1f}" y1="{y - 5}" x2="{b:.1f}" y2="{y + 5}" class="{cls}" stroke-width="1.2"/>')
        if depth <= 2:
            name = 'ε' if rho == '' else rho
            s.append(sub('σ', name, (a + b) / 2, y + 24, 15))
# labels on the right
s.append(f'<text x="{R + 18}" y="{rows_y[0] + 4}" class="label">[σ]</text>')
for d in range(1, 4):
    s.append(f'<text x="{R + 18}" y="{rows_y[d] + 4}" class="label">in D<tspan font-size="9" dy="3">{d - 1}</tspan></text>')
# the point G_X for X = 01...
a, b = iv['010']
gx = (a + b) / 2
s.append(f'<circle cx="{gx:.1f}" cy="{rows_y[3] + 26}" r="3.5" class="accent-fill"/>')
s.append(sub('G', 'X', gx, rows_y[3] + 46, 14))
s.append(f'<text x="{gx + 18:.1f}" y="{rows_y[3] + 46}" class="label">for X = 01…</text>')
s.append('</svg>')
out['baire-splitting'] = ''.join(s)

# ---------------------------------------------------------------- Kurtz: a block of zeros of prescribed length
w, x0, y0 = 26, 30, 40
s = ['<svg class="fig" viewBox="0 0 600 118" width="600" role="img" aria-label="A prefix of G: a string sigma of length n, followed by f(n) zeros and a one; the number of zeros after position n-1 is h(n) = f(n)">']
cells = ['σ'] * 5 + ['0'] * 9 + ['1', '·', '·', '·']
for i, c in enumerate(cells):
    x = x0 + i * w
    if c == 'σ':
        cls = 'cell'
        txt = ''
    elif c == '0':
        cls = 'cell head-cell'
        txt = '0'
    elif c == '1':
        cls = 'cell'
        txt = '1'
    else:
        cls = 'cell'
        txt = ''
    dash = ' stroke-dasharray="3 3"' if c == '·' else ''
    s.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{w}" class="{cls}"{dash}/>')
    if txt:
        s.append(f'<text x="{x + w / 2}" y="{y0 + 18}" text-anchor="middle" class="mrm" font-size="15">{txt}</text>')
s.append(f'<text x="{x0 + len(cells) * w + 8}" y="{y0 + 18}" class="mrm muted" font-size="15">⋯</text>')
s.append(f'<text x="{x0 + 2.5 * w}" y="{y0 + 18}" text-anchor="middle" class="math" font-size="16">σ</text>')
s.append(f'<text x="{x0 + 5 * w}" y="{y0 - 8}" text-anchor="middle" class="label">position n</text>')
s.append(f'<line x1="{x0 + 5 * w}" y1="{y0 - 4}" x2="{x0 + 5 * w}" y2="{y0 + w + 4}" class="accent-stroke" stroke-width="1.2" stroke-dasharray="2 2"/>')
s.append(brace(x0 + 1, x0 + 5 * w - 1, y0 + w + 6, 'G↾n = σ, of length n'))
s.append(brace(x0 + 5 * w + 1, x0 + 14 * w - 1, y0 + w + 6, 'f(n) zeros: h(n) = f(n)'))
s.append('</svg>')
out['kurtz-blocks'] = ''.join(s)

# ---------------------------------------------------------------- meet or avoid


def tree_panel(ox, mode):
    """A binary tree of depth 4 in a panel of width 270 starting at ox; the path of G is 0110."""
    depth = 4
    width = 260
    G = '0110'

    def pos(t):
        d = len(t)
        idx = int(t, 2) if t else 0
        return ox + (idx + 0.5) * width / (2 ** d), 30 + d * 44

    def strings(d):
        res = ['']
        for _ in range(d):
            res = [r + b for r in res for b in '01']
        return res
    allnodes = [t for d in range(depth + 1) for t in strings(d)]
    parts = []
    if mode == 'avoid':
        # shade the subtree of the prefix 01
        top = pos('01')
        lo = pos('0100')
        hi = pos('0111')
        parts.append(f'<path d="M{top[0]:.1f},{top[1] - 8} L{lo[0] - 10:.1f},{lo[1] + 10} L{hi[0] + 10:.1f},{hi[1] + 10} z" class="soft-fill"/>')
    W = {'meet': {'011', '10', '1101', '0010'}, 'avoid': {'0001', '10', '111', '0011'}}[mode]
    for t in allnodes:
        if t == '':
            continue
        (x1, y1), (x2, y2) = pos(t[:-1]), pos(t)
        on = G.startswith(t)
        cls = 'accent-stroke' if on else 'muted-stroke'
        sw = '2.2' if on else '1'
        parts.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{sw}"/>')
    for t in allnodes:
        x, y = pos(t)
        if t in W:
            parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="5" class="ink-fill"/>')
        elif G.startswith(t):
            parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.5" class="accent-fill"/>')
        else:
            parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="2.5" class="muted-fill"/>')
    gx, gy = pos(G)
    parts.append(f'<text x="{gx:.1f}" y="{gy + 22}" text-anchor="middle" class="math" font-size="15">G</text>')
    if mode == 'meet':
        x, y = pos('011')
        parts.append(f'<text x="{x + 10:.1f}" y="{y - 6}" class="label">prefix in W</text>')
        parts.append(f'<text x="{ox + width / 2}" y="16" text-anchor="middle" class="label">G meets W</text>')
    else:
        x, y = pos('01')
        parts.append(f'<text x="{x - 10:.1f}" y="{y - 6}" text-anchor="end" class="label">σ</text>')
        parts.append(f'<text x="{ox + width / 2}" y="16" text-anchor="middle" class="label">a prefix σ of G avoids W</text>')
    return parts


s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Two binary trees with the path of G. Left: a prefix of G belongs to W. Right: a prefix sigma of G has no extension in W; its subtree is shaded and contains no element of W">']
s += tree_panel(20, 'meet')
s += tree_panel(320, 'avoid')
s.append('<circle cx="190" cy="238" r="5" class="ink-fill"/>')
s.append('<text x="200" y="242" class="label">strings of W</text>')
s.append('<rect x="310" y="231" width="14" height="12" class="soft-fill"/>')
s.append('<text x="330" y="242" class="label">extensions of σ: none in W</text>')
s.append('</svg>')
out['meet-or-avoid'] = ''.join(s)

# ---------------------------------------------------------------- Jockusch-Shore coding block
s = ['<svg class="fig" viewBox="0 0 600 196" width="600" role="img" aria-label="The block added at step e: the string sigma_e, the bit Z(e), m zeros and a one; in the first case it is extended further to a string of W_e">',
     '<defs>' + marker('js-arrow', 'muted-fill') + '</defs>']
w = 24


def block(y, case):
    parts = []
    x = 20
    parts.append(f'<rect x="{x}" y="{y}" width="{4 * w}" height="{w}" class="cell"/>')
    parts.append(sub('σ', 'e', x + 2 * w, y + 17, 15))
    x += 4 * w
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" class="cell head-cell"/>')
    parts.append(f'<text x="{x + w / 2}" y="{y + 17}" text-anchor="middle" class="mrm" font-size="13">i</text>')
    zx = x + w
    for k in range(6):
        parts.append(f'<rect x="{zx + k * w}" y="{y}" width="{w}" height="{w}" class="cell"/>')
        parts.append(f'<text x="{zx + k * w + w / 2}" y="{y + 17}" text-anchor="middle" class="mrm" font-size="14">0</text>')
    ox = zx + 6 * w
    parts.append(f'<rect x="{ox}" y="{y}" width="{w}" height="{w}" class="cell"/>')
    parts.append(f'<text x="{ox + w / 2}" y="{y + 17}" text-anchor="middle" class="mrm" font-size="14">1</text>')
    end = ox + w

    def dlabel(x, yy, before, after):
        return (f'<text x="{x}" y="{yy}" class="label">{before}D<tspan font-size="9" dy="3">e</tspan>'
                f'<tspan dy="-3">{after}</tspan></text>')
    if case == 1:
        for k in range(5):
            parts.append(f'<rect x="{end + k * w}" y="{y}" width="{w}" height="{w}" class="cell" stroke-dasharray="3 3"/>')
        parts.append(f'<text x="{end + 2.5 * w}" y="{y + 17}" text-anchor="middle" class="math" font-size="15">τ</text>')
        parts.append(dlabel(end + 5 * w + 12, y + 16, 'm ∈ ', ' ∖ A'))
        parts.append(brace(end + 1, end + 5 * w - 1, y + w + 4, 'up to a string of W<tspan font-size="9" dy="3">e</tspan>'))
    else:
        parts.append(f'<text x="{end + 12}" y="{y + 16}" class="label">m ∈ A ∖ D<tspan font-size="9" dy="3">e</tspan>'
                     f'<tspan dy="-3">: stop; the string avoids W</tspan><tspan font-size="9" dy="3">e</tspan></text>')
    parts.append(brace(zx + 1, ox - 1, y + w + 4, 'm zeros'))
    return parts, x


p1, xi = block(30, 1)
p2, _ = block(118, 2)
s += p1 + p2
s.append(f'<text x="{xi + w / 2}" y="22" text-anchor="middle" class="label">i = Z(e)</text>')
s.append('<text x="20" y="22" class="label">case 1</text>')
s.append('<text x="20" y="110" class="label">case 2</text>')
s.append('</svg>')
out['jockusch-shore-coding'] = ''.join(s)

# ---------------------------------------------------------------- hierarchy of genericity notions
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The chain of implications: 2-generic implies weakly 2-generic implies 1-generic implies weakly 1-generic, with the sets separating each pair">',
     '<defs>' + marker('gh-arrow') + '</defs>']
names = [('weakly', '1-generic'), ('', '1-generic'), ('weakly', '2-generic'), ('', '2-generic')]
bw, gap, y = 104, 46, 34
xs = [14 + k * (bw + gap) for k in range(4)]
for (a, b), x in zip(names, xs):
    s.append(f'<rect x="{x}" y="{y}" width="{bw}" height="44" rx="6" class="state"/>')
    if a:
        s.append(f'<text x="{x + bw / 2}" y="{y + 19}" text-anchor="middle" class="label">{a}</text>')
        s.append(f'<text x="{x + bw / 2}" y="{y + 34}" text-anchor="middle" class="label">{b}</text>')
    else:
        s.append(f'<text x="{x + bw / 2}" y="{y + 27}" text-anchor="middle" class="label">{b}</text>')
for k in range(3):
    x1 = xs[k + 1] - 4
    x2 = xs[k] + bw + 4
    s.append(f'<line x1="{x1}" y1="{y + 22}" x2="{x2 + 2}" y2="{y + 22}" class="ink-stroke" stroke-width="1.3" marker-end="url(#gh-arrow)"/>')
s.append(f'<text x="{xs[3] + bw + 10}" y="{y + 26}" class="mrm muted" font-size="16">⋯</text>')
notes = [('not conversely: a weakly 1-generic', 'set of degree 0′'),
         ('not conversely: a 1-generic', 'set computable in ∅′'),
         ('not conversely: a weakly 2-generic', 'set of jump degree 0″')]
for k, (l1, l2) in enumerate(notes):
    cx = xs[k] + bw + gap / 2
    s.append(f'<line x1="{cx}" y1="{y + 30}" x2="{cx}" y2="{y + 58 + 34 * (k % 2)}" class="muted-stroke" stroke-width="1" stroke-dasharray="2 2"/>')
    ty = y + 72 + 34 * (k % 2)
    s.append(f'<text x="{cx}" y="{ty}" text-anchor="middle" class="label">{l1}</text>')
    s.append(f'<text x="{cx}" y="{ty + 14}" text-anchor="middle" class="label">{l2}</text>')
s.append('</svg>')
out['genericity-hierarchy'] = ''.join(s)

with open(sys.argv[1], 'w') as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
