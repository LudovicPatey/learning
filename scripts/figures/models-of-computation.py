# Generates the inline SVG figures of the Models of computation course.
import json, sys
out = {}

def marker(mid, double=False):
    p = 'M0,1 L9,5 L0,9 z' if not double else 'M0,1 L7,5 L0,9 z M6,1 L13,5 L6,9 z'
    w = 14 if double else 10
    return f'<marker id="{mid}" viewBox="0 0 {w} 10" refX="{w-1}" refY="5" markerWidth="{w*0.8:.0f}" markerHeight="8" orient="auto-start-reverse"><path d="{p}" class="ink-fill"/></marker>'

def q(x, y, sub, size=17):
    return f'<text x="{x}" y="{y}" text-anchor="middle" class="math" font-size="{size}">q<tspan class="mrm" font-size="{int(size*0.62)}" dy="4">{sub}</tspan></text>'

# 1. Turing machine anatomy
cells = ['⊔','⊔','1','1','1','⊔','1','1','⊔','⊔','⊔']
w, x0, y0 = 42, 30, 46
s = ['<svg class="fig" viewBox="0 0 540 230" width="540" role="img" aria-label="A Turing machine: tape, head and finite control">']
s.append('<text x="12" y="74" class="mrm muted" font-size="18">⋯</text>')
for i, c in enumerate(cells):
    x = x0 + i * w
    cls = 'cell head-cell' if i == 4 else 'cell'
    s.append(f'<rect class="{cls}" x="{x}" y="{y0}" width="{w}" height="{w}" rx="3"/>')
    s.append(f'<text x="{x + w/2}" y="{y0 + 28}" text-anchor="middle" class="mrm {"muted" if c=="⊔" else ""}" font-size="18">{c}</text>')
s.append(f'<text x="{x0 + len(cells)*w + 8}" y="74" class="mrm muted" font-size="18">⋯</text>')
hx = x0 + 4 * w + w / 2
s.append(f'<path d="M{hx-9},{y0-22} L{hx+9},{y0-22} L{hx},{y0-6} z" class="accent-fill"/>')
s.append(f'<text x="{hx}" y="{y0-28}" text-anchor="middle" class="label">head</text>')
s.append(f'<text x="{x0 + 9*w}" y="{y0-12}" text-anchor="middle" class="label">tape</text>')
s.append(f'<line x1="{hx}" y1="{y0+w}" x2="{hx}" y2="140" class="accent-stroke" stroke-width="1.5" stroke-dasharray="4 3"/>')
s.append(f'<rect x="{hx-80}" y="140" width="160" height="72" rx="10" class="soft-fill accent-stroke" stroke-width="1.5"/>')
s.append(f'<text x="{hx}" y="160" text-anchor="middle" class="label">finite control</text>')
s.append(q(hx, 194, '3', 24))
s.append('<text x="330" y="160" class="math" font-size="17">δ<tspan class="mrm">(</tspan>q<tspan class="mrm">,</tspan> a<tspan class="mrm">) = (</tspan>q<tspan class="mrm">′,</tspan> b<tspan class="mrm">,</tspan> D<tspan class="mrm">)</tspan></text>')
for i, t in enumerate(['read a, write b,', 'move one cell in direction D,', "enter the state q′"]):
    s.append(f'<text x="330" y="{184 + i*17}" class="label">{t}</text>')
s.append('</svg>')
out['tm-anatomy'] = ''.join(s)

# 2. State diagram of the successor machine
s = ['<svg class="fig" viewBox="0 0 540 175" width="540" role="img" aria-label="State diagram of the successor machine">', '<defs>' + marker('ah-succ') + '</defs>']
cx = {'0': 120, '1': 300, 'h': 460}
cy = 110
s.append(f'<line x1="40" y1="{cy}" x2="{cx["0"]-28}" y2="{cy}" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-succ)"/>')
s.append(f'<text x="44" y="{cy-8}" class="label">start</text>')
for k in ['0', '1', 'h']:
    s.append(f'<circle cx="{cx[k]}" cy="{cy}" r="26" class="state"/>')
    if k == 'h':
        s.append(f'<circle cx="{cx[k]}" cy="{cy}" r="21" class="state-inner"/>')
    s.append(q(cx[k], cy + 5, k))
def edge(a, b, label):
    x1, x2 = cx[a] + 27, cx[b] - 28
    s.append(f'<line x1="{x1}" y1="{cy}" x2="{x2}" y2="{cy}" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-succ)"/>')
    s.append(f'<text x="{(x1+x2)/2}" y="{cy-9}" text-anchor="middle" class="mrm" font-size="15">{label}</text>')
def loop(a, label):
    c = cx[a]
    s.append(f'<path d="M{c-12},{cy-23} C{c-40},{cy-82} {c+40},{cy-82} {c+12},{cy-24}" class="ink-stroke" fill="none" stroke-width="1.4" marker-end="url(#ah-succ)"/>')
    s.append(f'<text x="{c}" y="{cy-72}" text-anchor="middle" class="mrm" font-size="15">{label}</text>')
edge('0', '1', '⊔ / 1, L')
edge('1', 'h', '⊔ / ⊔, R')
loop('0', '1 / 1, R')
loop('1', '1 / 1, L')
s.append('</svg>')
out['tm-successor'] = ''.join(s)

# 3. Cantor pairing grid
def pair(x, y):
    n = x + y
    return n * (n + 1) // 2 + y
N = 4
ox, oy, d = 60, 250, 52
P = lambda x, y: (ox + d * x, oy - d * y)
s = ['<svg class="fig" viewBox="0 0 330 300" width="330" role="img" aria-label="Cantor pairing: pairs numbered along diagonals">', '<defs>' + marker('ah-cantor') + '</defs>']
s.append(f'<line x1="{ox-18}" y1="{oy}" x2="{ox + d*N + 34}" y2="{oy}" class="axis"/>')
s.append(f'<line x1="{ox}" y1="{oy+18}" x2="{ox}" y2="{oy - d*N - 34}" class="axis"/>')
s.append(f'<text x="{ox + d*N + 40}" y="{oy+5}" class="math" font-size="17">x</text>')
s.append(f'<text x="{ox-5}" y="{oy - d*N - 40}" class="math" font-size="17">y</text>')
for i in range(N + 1):
    s.append(f'<text x="{ox + d*i}" y="{oy + 32}" text-anchor="middle" class="mrm muted" font-size="13">{i}</text>')
    s.append(f'<text x="{ox - 26}" y="{oy - d*i + 5}" text-anchor="middle" class="mrm muted" font-size="13">{i}</text>')
order = [(n - y, y) for n in range(N + 1) for y in range(n + 1)]
for (a, b) in zip(order, order[1:]):
    (x1, y1), (x2, y2) = P(*a), P(*b)
    same = sum(a) == sum(b)
    # shorten the segment so it stops at the circles
    import math
    L = math.hypot(x2 - x1, y2 - y1); r = 15
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    cls = 'accent-stroke' if same else 'muted-stroke'
    dash = '' if same else ' stroke-dasharray="3 3"'
    s.append(f'<line x1="{x1+ux*r:.1f}" y1="{y1+uy*r:.1f}" x2="{x2-ux*(r+2):.1f}" y2="{y2-uy*(r+2):.1f}" class="{cls}" stroke-width="1.4"{dash} marker-end="url(#ah-cantor)"/>')
for (x, y) in order:
    cxx, cyy = P(x, y)
    s.append(f'<circle cx="{cxx}" cy="{cyy}" r="14" class="node"/>')
    s.append(f'<text x="{cxx}" y="{cyy+5}" text-anchor="middle" class="mrm" font-size="14">{pair(x, y)}</text>')
s.append('</svg>')
out['cantor-pairing'] = ''.join(s)

# 4. Multi-tape simulation by tracks
tapes = [['a','b','b','a','⊔','⊔'], ['1','1','⊔','⊔','⊔','⊔'], ['⊔','c','c','c','c','⊔']]
heads = [2, 1, 4]
w = 30
s = ['<svg class="fig" viewBox="0 0 600 205" width="600" role="img" aria-label="Three tapes encoded as three tracks of one tape">', '<defs>' + marker('ah-tracks') + '</defs>']
for t, (tape, h) in enumerate(zip(tapes, heads)):
    y = 34 + t * 56
    s.append(f'<text x="8" y="{y+20}" class="label">tape {t+1}</text>')
    for i, c in enumerate(tape):
        x = 60 + i * w
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="2" class="cell{" head-cell" if i==h else ""}"/>')
        s.append(f'<text x="{x+w/2}" y="{y+20}" text-anchor="middle" class="mrm{" muted" if c=="⊔" else ""}" font-size="15">{c}</text>')
    hx = 60 + h * w + w / 2
    s.append(f'<path d="M{hx-6},{y-13} L{hx+6},{y-13} L{hx},{y-3} z" class="accent-fill"/>')
s.append('<line x1="255" y1="104" x2="315" y2="104" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-tracks)"/>')
tw, th = 44, 34
s.append(f'<text x="335" y="22" class="label">one tape, three tracks</text>')
for i in range(6):
    x = 335 + i * tw
    for t in range(3):
        y = 34 + t * th
        marked = heads[t] == i
        s.append(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" class="cell{" head-cell" if marked else ""}"/>')
        c = tapes[t][i]
        s.append(f'<text x="{x+tw/2}" y="{y+22}" text-anchor="middle" class="mrm{" muted" if c=="⊔" else ""}" font-size="15">{c}</text>')
    s.append(f'<rect x="{x}" y="34" width="{tw}" height="{3*th}" class="track-outline"/>')
s.append(f'<text x="335" y="{34+3*th+24}" class="label">a shaded cell carries the head mark of its track</text>')
s.append('</svg>')
out['tm-tracks'] = ''.join(s)

# 5. Church–Rosser diamond
s = ['<svg class="fig" viewBox="0 0 320 230" width="320" role="img" aria-label="Church–Rosser diamond">', '<defs>' + marker('ah-cr', True) + '</defs>']
pts = {'M': (160, 34), 'N1': (60, 116), 'N2': (260, 116), 'P': (160, 198)}
def lab(k, x, y):
    if k in ('N1', 'N2'):
        return f'<text x="{x}" y="{y+6}" text-anchor="middle" class="math" font-size="19">N<tspan class="mrm" font-size="12" dy="5">{k[1]}</tspan></text>'
    return f'<text x="{x}" y="{y+6}" text-anchor="middle" class="math" font-size="19">{k}</text>'
def arrow(a, b, dashed):
    (x1, y1), (x2, y2) = pts[a], pts[b]
    import math
    L = math.hypot(x2-x1, y2-y1); ux, uy = (x2-x1)/L, (y2-y1)/L; r = 20
    cls = 'muted-stroke' if dashed else 'ink-stroke'
    da = ' stroke-dasharray="5 4"' if dashed else ''
    s.append(f'<line x1="{x1+ux*r:.1f}" y1="{y1+uy*r:.1f}" x2="{x2-ux*(r+2):.1f}" y2="{y2-uy*(r+2):.1f}" class="{cls}" stroke-width="1.5"{da} marker-end="url(#ah-cr)"/>')
arrow('M', 'N1', False); arrow('M', 'N2', False); arrow('N1', 'P', True); arrow('N2', 'P', True)
for k, (x, y) in pts.items():
    s.append(lab(k, x, y))
s.append('<text x="160" y="120" text-anchor="middle" class="label">there exists</text>')
s.append('</svg>')
out['church-rosser'] = ''.join(s)

# ===================================================================== lessons 2-6 (revision of 2026-11-12)
# Helpers of this block are prefixed with a_ so that they do not clash with the others.
import math

def a_text(x, y, parts, size=16, anchor='middle', extra=''):
    """A <text> made of tspans; parts = [(string, cls, attrs)]."""
    body = ''.join(f'<tspan class="{c}"{(" " + a) if a else ""}>{t.replace(" ", chr(160))}</tspan>' for (t, c, a) in parts)
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}"{extra}>{body}</text>'

def a_sub(base, sub_parts, size=16):
    """Parts for base_{sub}, sub_parts = [(string, cls)]; the baseline is restored at the end."""
    small = int(size * 0.68)
    parts = [(base, 'math', '')]
    for k, (t, c) in enumerate(sub_parts):
        parts.append((t, c, f'font-size="{small}"' + (' dy="4"' if k == 0 else '')))
    parts.append((' ', 'mrm', 'dy="-4"'))
    return parts

def a_q(sub):
    return a_sub('q', [(sub, 'mrm')])

def a_tape_row(s, x0, y, cells, head, w=36, h=32):
    for i, c in enumerate(cells):
        x = x0 + i * w
        cls = 'cell head-cell' if i == head else 'cell'
        s.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="2"/>')
        muted = ' muted' if c == '⊔' else ''
        s.append(f'<text x="{x + w/2}" y="{y + h/2 + 6}" text-anchor="middle" class="mrm{muted}" font-size="16">{c}</text>')

# ---------------------------------------------------------------- a1. run of the successor machine on input 1
cols = [-1, 0, 1, 2, 3]
confs = [('0', {0, 1}, 0), ('0', {0, 1}, 1), ('0', {0, 1}, 2), ('1', {0, 1, 2}, 1),
         ('1', {0, 1, 2}, 0), ('1', {0, 1, 2}, -1), ('h', {0, 1, 2}, 0)]
w, h, x0, y0 = 36, 30, 110, 40
W = 470
s = [f'<svg class="fig" viewBox="0 0 {W} {y0 + len(confs)*h + 16}" width="{W}" role="img" aria-label="The seven configurations of the successor machine on input 1, one per row">']
s.append(f'<text x="22" y="{y0 - 12}" class="label">step</text>')
s.append(f'<text x="70" y="{y0 - 12}" text-anchor="middle" class="label">state</text>')
for j, c in enumerate(cols):
    s.append(f'<text x="{x0 + j*w + w/2}" y="{y0 - 12}" text-anchor="middle" class="mrm muted" font-size="13">{c}</text>')
for t, (q, ones, hd) in enumerate(confs):
    y = y0 + t * h
    s.append(f'<text x="30" y="{y + h/2 + 5}" text-anchor="middle" class="mrm" font-size="15">{t}</text>')
    s.append(a_text(70, y + h/2 + 5, a_q(q)))
    a_tape_row(s, x0, y, ['1' if c in ones else '⊔' for c in cols], cols.index(hd), w, h)
bx = x0 + len(cols) * w + 14
for (ta, tb, lines) in [(0, 2, ['run right', 'across the input']), (3, 5, ['write 1, then', 'run left']), (6, 6, ['standard final', 'configuration'])]:
    ya, yb = y0 + ta * h + 4, y0 + (tb + 1) * h - 4
    s.append(f'<path d="M{bx},{ya} L{bx+6},{ya} L{bx+6},{yb} L{bx},{yb}" class="muted-stroke" fill="none" stroke-width="1.2"/>')
    ym = (ya + yb) / 2
    for k, line in enumerate(lines):
        s.append(f'<text x="{bx + 16}" y="{ym - 2 + 14*k - (7 if len(lines) == 2 else 0)}" class="label">{line}</text>')
s.append('</svg>')
out['tm-successor-run'] = ''.join(s)

# ---------------------------------------------------------------- a2. rounds of the doubling machine on input 2
rows = [('j = 0', list('111⊔⊔⊔'), 0, '0'), ('j = 1', list('X11Y⊔⊔'), 1, '0'), ('j = 2', list('XX1YY⊔'), 2, '0'),
        ('j = 3', list('XXXYYY'), 3, '0'), ('halt', list('11111⊔'), 0, 'h')]
w, h, x0, y0 = 36, 32, 120, 36
W = 400
s = [f'<svg class="fig" viewBox="0 0 {W} {y0 + len(rows)*(h+8) + 8}" width="{W}" role="img" aria-label="Tape of the doubling machine at the start of each round, and at the end">']
for j in range(6):
    s.append(f'<text x="{x0 + j*w + w/2}" y="{y0 - 12}" text-anchor="middle" class="mrm muted" font-size="13">{j}</text>')
for r, (lab, cells, hd, q) in enumerate(rows):
    y = y0 + r * (h + 8)
    if r == len(rows) - 1:
        s.append(f'<line x1="20" y1="{y - 5}" x2="{x0 + 6*w + 60}" y2="{y - 5}" class="axis"/>')
    if lab == 'halt':
        s.append(f'<text x="20" y="{y + h/2 + 5}" class="label">{lab}</text>')
    else:
        s.append(a_text(20, y + h/2 + 5, [('j', 'math', ''), (' = ' + lab[-1], 'mrm', '')], 15, anchor='start'))
    s.append(a_text(88, y + h/2 + 5, a_q(q)))
    a_tape_row(s, x0, y, cells, hd, w, h)
s.append('</svg>')
out['tm-doubling-rounds'] = ''.join(s)

# ---------------------------------------------------------------- a3. register layout in the proof of closure under composition
def a_reg(sub_parts):
    return a_sub('R', sub_parts, 15)
boxes = [[('1', 'mrm')], [('2', 'mrm')], None, [('N', 'math')],
         [('N', 'math'), ('+1', 'mrm')], None, [('N', 'math'), ('+', 'mrm'), ('k', 'math')],
         [('N', 'math'), ('+', 'mrm'), ('k', 'math'), ('+1', 'mrm')], None, [('N', 'math'), ('+', 'mrm'), ('k', 'math'), ('+', 'mrm'), ('m', 'math')]]
widths = [46, 46, 34, 46, 62, 34, 62, 78, 34, 82]
x, y, h = 14, 40, 38
xs = []
s = ['<svg class="fig" viewBox="0 0 610 150" width="610" role="img" aria-label="Registers used in the proof: scratch registers, saved input, values of the g_i">']
for b, bw in zip(boxes, widths):
    xs.append((x, bw))
    if b is None:
        s.append(f'<text x="{x + bw/2}" y="{y + h/2 + 5}" text-anchor="middle" class="mrm muted" font-size="16">⋯</text>')
    else:
        s.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" rx="2" class="cell"/>')
        s.append(a_text(x + bw/2, y + h/2 + 5, a_reg(b)))
    x += bw + 4
groups = [(0, 3, ['the only registers that', a_sub('G', [('i', 'math')], 14) + [(' and ', 'mrm', ''), ('H', 'math', ''), (' mention', 'mrm', '')]]), (4, 6, ['saved input', a_sub('x', [('1', 'mrm')], 14) + [(', …, ', 'mrm', '')] + a_sub('x', [('k', 'math')], 14)]),
          (7, 9, ['values of', a_sub('g', [('1', 'mrm')], 14) + [(', …, ', 'mrm', '')] + a_sub('g', [('m', 'math')], 14)])]
for (a, b, lines) in groups:
    xa, xb = xs[a][0], xs[b][0] + xs[b][1]
    s.append(f'<path d="M{xa},{y + h + 8} L{xa},{y + h + 14} L{xb},{y + h + 14} L{xb},{y + h + 8}" class="muted-stroke" fill="none" stroke-width="1.2"/>')
    for k, line in enumerate(lines):
        if isinstance(line, str):
            s.append(f'<text x="{(xa + xb)/2}" y="{y + h + 32 + 16*k}" text-anchor="middle" class="label">{line}</text>')
        else:
            s.append(a_text((xa + xb)/2, y + h + 32 + 16*k, line, 14))
s.append(f'<text x="{(xs[4][0] + xs[6][0] + xs[6][1])/2}" y="{y - 12}" text-anchor="middle" class="label">not modified after the first transfers</text>')
s.append('</svg>')
out['urm-register-layout'] = ''.join(s)

# ---------------------------------------------------------------- a4. derivation tree of multiplication
def a_p(k, i, size=16):
    sm = int(size * 0.68)
    return [('p', 'math', ''), (str(k), 'mrm', f'font-size="{sm}" dy="-7"'), (str(i), 'mrm', f'font-size="{sm}" dx="-{sm*0.55:.1f}" dy="11"'), (' ', 'mrm', 'dy="-4"')]
M = lambda t: (t, 'math', '')
R = lambda t: (t, 'mrm', '')
nodes = {
    'mult': (290, 40, [M('x'), R(' · '), M('y')], 'primitive recursion'),
    'Z':    (170, 120, [M('Z')], 'basic'),
    'h':    (400, 120, [M('z'), R(' + '), M('x')], 'composition'),
    'plus': (260, 200, [M('x'), R(' + '), M('y')], 'primitive recursion'),
    'p33b': (420, 200, a_p(3, 3), 'basic'),
    'p31':  (520, 200, a_p(3, 1), 'basic'),
    'p11':  (180, 280, a_p(1, 1), 'basic'),
    'Sp':   (340, 280, [M('S'), R(' ∘ ')] + a_p(3, 3), 'composition'),
    'S':    (290, 360, [M('S')], 'basic'),
    'p33':  (390, 360, a_p(3, 3), 'basic'),
}
edges = [('mult', 'Z'), ('mult', 'h'), ('h', 'plus'), ('h', 'p33b'), ('h', 'p31'), ('plus', 'p11'), ('plus', 'Sp'), ('Sp', 'S'), ('Sp', 'p33')]
s = ['<svg class="fig" viewBox="0 0 600 395" width="600" role="img" aria-label="Derivation tree of multiplication: each node is obtained from its children by composition or primitive recursion">']
for (a, b) in edges:
    (x1, y1), (x2, y2) = nodes[a][:2], nodes[b][:2]
    s.append(f'<line x1="{x1}" y1="{y1 + 10}" x2="{x2}" y2="{y2 - 20}" class="muted-stroke" stroke-width="1.3"/>')
for k, (x, y, parts, scheme) in nodes.items():
    s.append(f'<rect x="{x - 42}" y="{y - 20}" width="84" height="30" rx="6" class="{"cell" if scheme == "basic" else "soft-fill accent-stroke"}" stroke-width="1.2"/>')
    s.append(a_text(x, y + 1, parts))
    if scheme != 'basic':
        left = k == 'plus'
        s.append(f'<text x="{x - 48 if left else x + 48}" y="{y}" text-anchor="{"end" if left else "start"}" class="label">{scheme}</text>')
s.append('</svg>')
out['pr-derivation-tree'] = ''.join(s)

# ---------------------------------------------------------------- a5. course-of-values recursion
s = ['<svg class="fig" viewBox="0 0 560 170" width="560" role="img" aria-label="The values f(0) to f(y-1) are packed into one code, from which h computes f(y), which is appended">',
     '<defs>' + marker('ah-cov') + '</defs>']
vals = [[M('f'), R('(0)')], [M('f'), R('(1)')], None, [M('f'), R('('), M('y'), R(' − 1)')]]
bw, x, y = 70, 20, 50
xs = []
for v in vals:
    if v is None:
        s.append(f'<text x="{x + 20}" y="{y + 22}" text-anchor="middle" class="mrm muted" font-size="16">⋯</text>')
        x += 40
        continue
    ww = bw if len(v) < 3 else 96
    s.append(f'<rect x="{x}" y="{y}" width="{ww}" height="32" rx="2" class="cell"/>')
    s.append(a_text(x + ww/2, y + 22, v, 15))
    xs.append((x, ww))
    x += ww + 4
xe = x
s.append(f'<rect x="{xe + 6}" y="{y}" width="70" height="32" rx="2" class="cell head-cell"/>')
s.append(a_text(xe + 41, y + 22, [M('f'), R('('), M('y'), R(')')], 15))
s.append(f'<path d="M20,{y - 8} L20,{y - 14} L{xe - 4},{y - 14} L{xe - 4},{y - 8}" class="accent-stroke" fill="none" stroke-width="1.3"/>')
s.append(f'<text x="{(20 + xe) / 2}" y="{y - 22}" text-anchor="middle" class="label">one integer: the code of all previous values</text>')
hx, hy = 250, 132
s.append(f'<rect x="{hx - 60}" y="{hy - 20}" width="120" height="32" rx="8" class="soft-fill accent-stroke" stroke-width="1.3"/>')
s.append(a_text(hx, hy + 2, [M('h'), R('('), M('y'), R(', ·)')], 15))
s.append(f'<path d="M{(20 + xe)/2},{y + 36} L{hx - 20},{hy - 24}" class="ink-stroke" fill="none" stroke-width="1.3" marker-end="url(#ah-cov)"/>')
s.append(f'<path d="M{hx + 62},{hy - 4} C{xe + 30},{hy} {xe + 41},{hy - 20} {xe + 41},{y + 38}" class="ink-stroke" fill="none" stroke-width="1.3" marker-end="url(#ah-cov)"/>')
s.append(f'<text x="{xe + 84}" y="{y + 14}" class="label">appended to</text>')
s.append(f'<text x="{xe + 84}" y="{y + 30}" class="label">the code</text>')
s.append('</svg>')
out['course-of-values'] = ''.join(s)

# ---------------------------------------------------------------------------
# Figures of lessons 8-12 (minimization, WHILE programs, lambda-calculus,
# lambda-definability, equivalence of the models). Added 2026-11-12.
import math

def arrow_line(x1, y1, x2, y2, mid, cls='ink-stroke', r1=0, r2=0, dash=''):
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    da = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1+ux*r1:.1f}" y1="{y1+uy*r1:.1f}" x2="{x2-ux*r2:.1f}" y2="{y2-uy*r2:.1f}" '
            f'class="{cls}" stroke-width="1.4"{da} marker-end="url(#{mid})"/>')

# 6. Minimization: the search stops at the first zero, or is stuck on a divergent value
s = ['<svg class="fig" viewBox="0 0 520 200" width="520" role="img" aria-label="Two runs of the search for the least zero">', '<defs>' + marker('ah-mu') + '</defs>']
w, x0 = 46, 150
for i in range(5):
    s.append(f'<text x="{x0 + i*w + w/2}" y="22" text-anchor="middle" class="math" font-size="16">y<tspan class="mrm"> = {i}</tspan></text>')
rows = [(52, ['4', '1', '0', '7', '0'], 2, 'f(x) = 2'), (132, ['3', '↑', '0', '0', '5'], 1, 'f(x)↑')]
for (y, vals, stop, res) in rows:
    s.append(f'<text x="12" y="{y+28}" class="label">{"run (a)" if stop == 2 else "run (b)"}</text>')
    for i, v in enumerate(vals):
        cls = 'cell head-cell' if i == stop else 'cell'
        muted = ' muted' if i > stop else ''
        s.append(f'<rect class="{cls}" x="{x0 + i*w}" y="{y}" width="{w}" height="{w}" rx="3"/>')
        s.append(f'<text x="{x0 + i*w + w/2}" y="{y+29}" text-anchor="middle" class="mrm{muted}" font-size="18">{v}</text>')
    for i in range(stop):
        cx1 = x0 + i*w + w/2; cx2 = cx1 + w
        s.append(f'<path d="M{cx1+6},{y-4} Q{(cx1+cx2)/2},{y-18} {cx2-6},{y-4}" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-mu)"/>')
    fx = 'f<tspan class="mrm">(</tspan>x<tspan class="mrm">)</tspan>'
    rest = res[4:].replace('=', '<tspan class="mrm">=</tspan>').replace('2', '<tspan class="mrm">2</tspan>').replace('↑', '<tspan class="mrm">↑</tspan>')
    s.append(f'<text x="{x0 + 5*w + 18}" y="{y+29}" class="math" font-size="17">{fx}{rest}</text>')
s.append(f'<text x="{x0}" y="194" class="label">values after the stopping point are never computed</text>')
s.append('</svg>')
out['mu-search'] = ''.join(s)

# 7. LOOP instruction compiled into a register machine program
s = ['<svg class="fig" viewBox="0 0 540 300" width="540" role="img" aria-label="Layout of the register machine program for a LOOP instruction">', '<defs>' + marker('ah-loopurm') + '</defs>']
instr = [('1', 'T(i+2, a)', 'save the number of iterations'), ('2', 'Z(b)', 'reset the counter'),
         ('3', 'J(a, b, t+6)', 'exit when the counter reaches it'), ('4 … t+3', 'Q* shifted by 3', 'body'),
         ('t+4', 'S(b)', 'count one iteration'), ('t+5', 'J(1, 1, 3)', 'back to the test'), ('t+6', '', 'next instruction')]
bx, bw, bh, y0 = 80, 200, 32, 18
ys = []
for k, (num, ins, com) in enumerate(instr):
    y = y0 + k * (bh + 8)
    ys.append(y)
    dash = ' stroke-dasharray="4 3"' if not ins else ''
    cls = 'cell head-cell' if k == 3 else 'cell'
    s.append(f'<rect class="{cls}" x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="3"{dash}/>')
    s.append(f'<text x="{bx+10}" y="{y+21}" class="mrm muted" font-size="13">{num}</text>')
    if ins:
        s.append(f'<text x="{bx+bw-12}" y="{y+21}" text-anchor="end" class="mrm" font-size="14">{ins}</text>')
    s.append(f'<text x="{bx+bw+62}" y="{y+21}" class="label">{com}</text>')
# exit arrow from 3 to t+6 on the right
ya, yb = ys[2] + bh/2, ys[6] + bh/2
s.append(f'<path d="M{bx+bw},{ya} C{bx+bw+50},{ya} {bx+bw+50},{yb} {bx+bw+4},{yb}" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-loopurm)"/>')
# back arrow from t+5 to 3 on the left
ya, yb = ys[5] + bh/2, ys[2] + bh/2
s.append(f'<path d="M{bx},{ya} C{bx-60},{ya} {bx-60},{yb} {bx-4},{yb}" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-loopurm)"/>')
s.append('</svg>')
out['loop-urm'] = ''.join(s)

# 8. Reduction graph of (λx.y)Ω
s = ['<svg class="fig" viewBox="0 0 460 150" width="460" role="img" aria-label="The two reductions of the term (λx.y)Ω">', '<defs>' + marker('ah-kom') + '</defs>']
term = '<tspan class="mrm">(</tspan>λx<tspan class="mrm">.</tspan>y<tspan class="mrm">)</tspan><tspan class="mrm">Ω</tspan>'
cx, cy = 130, 96
s.append(f'<rect class="node" x="{cx-58}" y="{cy-22}" width="116" height="40" rx="8"/>')
s.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" class="math" font-size="19">{term}</text>')
s.append(f'<rect class="node" x="350" y="{cy-22}" width="50" height="40" rx="8"/>')
s.append(f'<text x="375" y="{cy+5}" text-anchor="middle" class="math" font-size="19">y</text>')
s.append(arrow_line(cx+58, cy-2, 350, cy-2, 'ah-kom', r2=3))
s.append(f'<text x="{(cx+58+350)/2}" y="{cy-12}" text-anchor="middle" class="label">contract the outer redex</text>')
s.append(f'<path d="M{cx-22},{cy-23} C{cx-50},{cy-85} {cx+50},{cy-85} {cx+22},{cy-25}" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-kom)"/>')
s.append(f'<text x="{cx}" y="{cy-76}" text-anchor="middle" class="label">contract Ω</text>')
s.append('</svg>')
out['k-omega'] = ''.join(s)

# 9. Kleene's predecessor: iterating Φ on pairs
def nm(n):
    return f'<tspan class="mrm">{n}</tspan>'
s = ['<svg class="fig" viewBox="0 0 560 150" width="560" role="img" aria-label="Iteration of Φ on pairs of numerals">', '<defs>' + marker('ah-pred') + '</defs>']
pairs = [(0, 0), (0, 1), (1, 2), (2, 3)]
px = [60, 200, 340, 480]
py = 50
for (a, b), x in zip(pairs, px):
    s.append(f'<rect class="node" x="{x-44}" y="{py-20}" width="88" height="38" rx="8"/>')
    s.append(f'<text x="{x}" y="{py+6}" text-anchor="middle" class="mrm" font-size="18">({a}, {b})</text>')
for x1, x2 in zip(px, px[1:]):
    s.append(arrow_line(x1+44, py, x2-44, py, 'ah-pred', r1=2, r2=3))
    s.append(f'<text x="{(x1+x2)/2}" y="{py-10}" text-anchor="middle" class="math" font-size="16">Φ</text>')
s.append(arrow_line(480, py+18, 480, 118, 'ah-pred', r1=2, r2=2))
s.append(f'<text x="490" y="{py+50}" class="label">fst</text>')
s.append('<text x="480" y="138" text-anchor="middle" class="mrm" font-size="18">2</text>')
s.append(f'<text x="16" y="138" class="label">the pair after n steps is (n ∸ 1, n)</text>')
s.append('</svg>')
out['lambda-pred'] = ''.join(s)

# 10. Coding a configuration by two sequences
cells = ['⊔', 'a', 'b', 'c', 'd', 'e', 'f', '⊔']
w, x0, y0 = 46, 70, 40
s = ['<svg class="fig" viewBox="0 0 520 190" width="520" role="img" aria-label="A tape split at the head into a reversed left part and a right part">', '<defs>' + marker('ah-conf') + '</defs>']
s.append(f'<text x="{x0-24}" y="{y0+29}" class="mrm muted" font-size="18">⋯</text>')
for i, c in enumerate(cells):
    x = x0 + i * w
    cls = 'cell head-cell' if i == 4 else 'cell'
    s.append(f'<rect class="{cls}" x="{x}" y="{y0}" width="{w}" height="{w}" rx="3"/>')
    s.append(f'<text x="{x+w/2}" y="{y0+29}" text-anchor="middle" class="math{" muted" if c=="⊔" else ""}" font-size="18">{c}</text>')
s.append(f'<text x="{x0 + len(cells)*w + 8}" y="{y0+29}" class="mrm muted" font-size="18">⋯</text>')
hx = x0 + 4*w + w/2
s.append(f'<path d="M{hx-8},{y0-20} L{hx+8},{y0-20} L{hx},{y0-6} z" class="accent-fill"/>')
s.append(f'<text x="{hx}" y="{y0-26}" text-anchor="middle" class="label">head</text>')
# left part, read from the head leftwards
yl = y0 + w + 30
s.append(arrow_line(x0 + 4*w - 4, yl, x0 + 1*w + 6, yl, 'ah-conf', cls='ink-stroke'))
s.append(f'<text x="{x0 + 2.5*w}" y="{yl+30}" text-anchor="middle" class="math" font-size="17">ℓ <tspan class="mrm">= [</tspan>c<tspan class="mrm">, </tspan>b<tspan class="mrm">, </tspan>a<tspan class="mrm">]</tspan></text>')
s.append(arrow_line(x0 + 4*w + 4, yl, x0 + 7*w - 6, yl, 'ah-conf', cls='accent-stroke'))
s.append(f'<text x="{x0 + 5.5*w}" y="{yl+30}" text-anchor="middle" class="math" font-size="17">r <tspan class="mrm">= [</tspan>d<tspan class="mrm">, </tspan>e<tspan class="mrm">, </tspan>f<tspan class="mrm">]</tspan></text>')
s.append('</svg>')
out['tm-configuration-code'] = ''.join(s)

# 11. The cycle of implications of the equivalence theorem
s = ['<svg class="fig" viewBox="0 0 660 260" width="660" role="img" aria-label="Implications between the five models of computation">', '<defs>' + marker('ah-eqv') + '</defs>']
nodes = {'1': (100, 50, 'Turing machines'), '4': (370, 50, 'partial recursive'), '3': (370, 210, 'WHILE programs'),
         '2': (100, 210, 'register machines'), '5': (580, 50, 'λ-terms')}
nw, nh = 150, 38
def width(k):
    return 120 if k == '5' else nw
for k, (x, y, t) in nodes.items():
    s.append(f'<rect class="node" x="{x-width(k)/2}" y="{y-nh/2}" width="{width(k)}" height="{nh}" rx="8"/>')
    s.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">({k}) {t}</text>')
def e(a, b, lab, lx, ly, anchor='middle', dy=0):
    (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
    if y1 == y2:
        sx = 1 if x2 > x1 else -1
        s.append(arrow_line(x1 + sx*width(a)/2, y1 + dy, x2 - sx*width(b)/2, y2 + dy, 'ah-eqv', r1=2, r2=3))
    else:
        sy = 1 if y2 > y1 else -1
        s.append(arrow_line(x1, y1 + sy*nh/2, x2, y2 - sy*nh/2, 'ah-eqv', r1=2, r2=3))
    s.append(f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" class="label">{lab}</text>')
e('1', '4', 'arithmetization', 235, 40)
e('4', '3', 'compilation', 380, 134, 'start')
e('3', '2', 'translation', 235, 200)
e('2', '1', 'simulation', 90, 134, 'end')
e('4', '5', 'definability', 482, 32, dy=-8)
e('5', '4', 'normal order', 482, 82, dy=8)
s.append('</svg>')
out['equivalence-cycle'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
