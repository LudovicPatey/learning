# Generates the inline SVG figures of the course on the arithmetic hierarchy.
# Usage: python3 scripts/figures/arithmetic-hierarchy.py out.json
import json, sys
out = {}

def cls(letter, n, x, y):
    # A class name such as Sigma^0_n, centered at (x, y).
    return (f'<text x="{x}" y="{y}" text-anchor="middle" class="mrm" font-size="19">{letter}'
            f'<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">{n}</tspan></text>')

def marker(mid):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker>')

s = ['<svg class="fig" viewBox="0 0 590 186" width="590" role="img" aria-label="The arithmetic hierarchy: each Delta level is included in the Sigma and Pi levels, which are included in the next Delta level">',
     '<defs>' + marker('ah-arith') + '</defs>']
nodes = {}
x = 40
nodes['D1'] = (x, 100)
for n in range(1, 4):
    nodes[f'S{n}'] = (x + 80, 36)
    nodes[f'P{n}'] = (x + 80, 164)
    nodes[f'D{n+1}'] = (x + 160, 100)
    x += 160
def arrow(a, b):
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    import math
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    r1, r2 = 22, 24
    s.append(f'<line x1="{x1 + ux*r1:.1f}" y1="{y1 + uy*r1:.1f}" x2="{x2 - ux*r2:.1f}" y2="{y2 - uy*r2:.1f}" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/>')
for n in range(1, 4):
    arrow(f'D{n}', f'S{n}'); arrow(f'D{n}', f'P{n}')
    arrow(f'S{n}', f'D{n+1}'); arrow(f'P{n}', f'D{n+1}')
for k, (cx, cy) in nodes.items():
    letter = {'S': 'Σ', 'P': 'Π', 'D': 'Δ'}[k[0]]
    if k[0] == 'D':
        s.append(f'<rect x="{cx - 20}" y="{cy - 18}" width="40" height="36" rx="8" class="soft-fill"/>')
    s.append(cls(letter, k[1:], cx - 3, cy + 5))
s.append('<text x="556" y="105" class="mrm muted" font-size="18">⋯</text>')
s.append('</svg>')
out['hierarchy'] = ''.join(s)

# ---------------------------------------------------------------- the marker construction for Cof
# A run of the construction of V_x in the lesson on index sets. At stage s + 1 the
# least acting number n keeps the first n markers below s and enumerates the others.
acts = {4: 2, 6: 1, 8: 2, 10: 1, 12: 1}   # stage s + 1 -> least acting n
N, c, x0, y0 = 12, 30, 150, 40
V = set()
rows = []
for t in sorted(acts):
    s_ = t - 1
    n = acts[t]
    markers = [j for j in range(s_) if j not in V]
    new = set(markers[n:])
    V |= new
    rows.append((t, n, s_, set(V), new))
H = y0 + c * len(rows) + 46
s = [f'<svg class="fig" viewBox="0 0 {x0 + c*N + 20} {H}" width="{x0 + c*N + 20}" role="img" aria-label="A run of the marker construction: at each acting stage, the numbers below the stage outside V, except the first n, are enumerated into V">']
for j in range(N):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{y0 - 10}" text-anchor="middle" class="mrm muted" font-size="13">{j}</text>')
for i, (t, n, s_, Vt, new) in enumerate(rows):
    y = y0 + c * i
    s.append(f'<text x="10" y="{y + 20}" class="label">stage {t}: <tspan class="math" font-size="14">n</tspan><tspan class="mrm" font-size="14" dx="4">=&#160;{n}</tspan><tspan dx="4">acts</tspan></text>')
    rank = 0
    for j in range(N):
        x = x0 + c * j
        if j in new:
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" class="cell head-cell"/>')
        elif j in Vt:
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" class="cell"/>')
            s.append(f'<rect x="{x + 1}" y="{y + 1}" width="{c - 2}" height="{c - 2}" class="soft-fill"/>')
        elif j < s_:
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" class="cell"/>')
            s.append(f'<circle cx="{x + c/2}" cy="{y + c/2}" r="7" class="ink-stroke" stroke-width="1.3"/>')
            rank += 1
        else:
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" class="cell" stroke-dasharray="2 3"/>')
    # boundary of the numbers below s
    s.append(f'<line x1="{x0 + c*s_}" y1="{y - 2}" x2="{x0 + c*s_}" y2="{y + c + 2}" class="accent-stroke" stroke-width="2"/>')
yl = y0 + c * len(rows) + 26
lx = x0
s.append(f'<rect x="{lx}" y="{yl - 12}" width="16" height="16" class="cell head-cell"/>')
s.append(f'<text x="{lx + 22}" y="{yl + 1}" class="label">enumerated at this stage</text>')
lx += 170
s.append(f'<rect x="{lx}" y="{yl - 12}" width="16" height="16" class="cell"/><rect x="{lx + 1}" y="{yl - 11}" width="14" height="14" class="soft-fill"/>')
s.append(f'<text x="{lx + 22}" y="{yl + 1}" class="label">already in V</text>')
lx += 105
s.append(f'<circle cx="{lx + 8}" cy="{yl - 4}" r="7" class="ink-stroke" stroke-width="1.3"/>')
s.append(f'<text x="{lx + 22}" y="{yl + 1}" class="label">marker</text>')
s.append('</svg>')
out['markers'] = ''.join(s)

# ---------------------------------------------------------------- kinds of indices
def idx(letter, n, x, y, size=17):
    # Delta^0_n or Sigma^0_n followed by the word "index", centered at (x, y).
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}"><tspan class="mrm">{letter}</tspan>'
            f'<tspan class="mrm" font-size="{int(size*0.65)}" dy="-7">0</tspan><tspan class="mrm" font-size="{int(size*0.65)}" dx="-6" dy="12">{n}</tspan>'
            f'<tspan font-size="{size - 3}" dx="5" dy="-5">index</tspan></text>')
def word(t, x, y, size=14):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}">{t}</text>'
W, Hh = 600, 205
s = [f'<svg class="fig" viewBox="0 0 {W} {Hh}" width="{W}" role="img" aria-label="Conversions between kinds of indices: computable in one direction, not uniform in the other">',
     '<defs>' + marker('ah-idx') + '</defs>']
boxes = {'can': (75, 50), 'd1': (300, 50), 's1': (525, 50), 'low': (187, 145), 'd2': (412, 145)}
bw, bh = 136, 40
for k, (cx, cy) in boxes.items():
    s.append(f'<rect x="{cx - bw/2}" y="{cy - bh/2}" width="{bw}" height="{bh}" rx="8" class="node"/>')
s.append(word('canonical index', 75, 55))
s.append(idx('Δ', 1, 300, 56))
s.append(idx('Σ', 1, 525, 56))
s.append(word('lowness index', 187, 150))
s.append(idx('Δ', 2, 412, 151))
def harrow(a, b, dy, dashed, text):
    (x1, y1), (x2, y2) = boxes[a], boxes[b]
    sgn = 1 if x2 > x1 else -1
    xa, xb = x1 + sgn * bw/2 + sgn * 3, x2 - sgn * bw/2 - sgn * 5
    y = y1 + dy
    d = ' stroke-dasharray="4 3"' if dashed else ''
    cl = 'muted-stroke' if dashed else 'ink-stroke'
    s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="{cl}" stroke-width="1.3"{d} marker-end="url(#ah-idx)"/>')
    ty = y - 6 if dy < 0 else y + 15
    s.append(f'<text x="{(xa + xb)/2}" y="{ty}" text-anchor="middle" class="label">{text}</text>')
harrow('can', 'd1', -9, False, 'computable')
harrow('d1', 'can', 9, True, 'not uniform')
harrow('d1', 's1', -9, False, 'computable')
harrow('s1', 'd1', 9, True, 'not uniform')
harrow('low', 'd2', -9, False, 'computable')
harrow('d2', 'low', 9, True, 'not uniform')
s.append(f'<text x="{W/2}" y="{Hh - 6}" text-anchor="middle" class="label">solid: a computable conversion; dashed: no partial computable conversion exists</text>')
s.append('</svg>')
out['indices'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
