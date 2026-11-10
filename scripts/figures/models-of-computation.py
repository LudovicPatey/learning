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

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
