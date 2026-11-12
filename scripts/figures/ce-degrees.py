# Generates the inline SVG figures of the course on Post's problem and the priority method.
# Usage: python3 scripts/figures/ce-degrees.py out.json
import json, sys
out = {}

def sub(base, s, x, y, size=16, anchor='end'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

# ---------------------------------------------------------------- a run of a finite injury construction
# Events per requirement: ('w', stage) new witness, ('a', stage) action, ('i', stage) initialization.
rows = [
    [('w', 1), ('a', 3)],
    [('w', 1), ('i', 3), ('w', 4), ('a', 7)],
    [('w', 1), ('i', 3), ('w', 4), ('i', 7), ('w', 8), ('a', 10)],
    [('w', 1), ('i', 3), ('w', 4), ('i', 7), ('w', 8), ('i', 10), ('w', 11)],
]
x0, dx, y0, dy = 70, 38, 40, 40
T = 13
s = ['<svg class="fig" viewBox="0 0 590 250" width="590" role="img" aria-label="A run of a finite injury construction: each action initializes all requirements of lower priority, which then choose new witnesses">']
for t in range(T):
    x = x0 + dx * t
    s.append(f'<text x="{x}" y="{y0 - 18}" text-anchor="middle" class="mrm muted" font-size="11">{t}</text>')
    s.append(f'<line x1="{x}" y1="{y0 - 8}" x2="{x}" y2="{y0 + dy * (len(rows) - 1) + 10}" class="axis" stroke-dasharray="2 4"/>')
s.append(f'<text x="{x0 + dx * (T - 1) + 14}" y="{y0 - 18}" class="label">stage</text>')
for r, ev in enumerate(rows):
    y = y0 + dy * r
    s.append(sub('R', str(r), x0 - 22, y + 5))
    # active segments between a witness and the next event
    for (k, t), nxt in zip(ev, ev[1:] + [(None, T - 0.5)]):
        if k == 'w':
            xa, xb = x0 + dx * t, x0 + dx * nxt[1]
            s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="accent-stroke" stroke-width="2"/>')
        if k == 'a':
            xa, xb = x0 + dx * t, x0 + dx * (T - 0.5)
            s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="ink-stroke" stroke-width="3"/>')
    for k, t in ev:
        x = x0 + dx * t
        if k == 'w':
            s.append(f'<circle cx="{x}" cy="{y}" r="5" class="node"/>')
        elif k == 'a':
            s.append(f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" class="accent-fill"/>')
        else:
            s.append(f'<path d="M{x-5},{y-5} L{x+5},{y+5} M{x-5},{y+5} L{x+5},{y-5}" class="ink-stroke" stroke-width="1.8"/>')
ly = y0 + dy * len(rows) + 6
s.append(f'<circle cx="{x0}" cy="{ly}" r="5" class="node"/><text x="{x0 + 12}" y="{ly + 4}" class="label">new witness</text>')
s.append(f'<rect x="{x0 + 112}" y="{ly - 6}" width="12" height="12" class="accent-fill"/><text x="{x0 + 130}" y="{ly + 4}" class="label">action (enumeration and restraint)</text>')
s.append(f'<path d="M{x0 + 345},{ly - 5} L{x0 + 355},{ly + 5} M{x0 + 345},{ly + 5} L{x0 + 355},{ly - 5}" class="ink-stroke" stroke-width="1.8"/><text x="{x0 + 362}" y="{ly + 4}" class="label">initialization</text>')
s.append('</svg>')
out['injury-run'] = ''.join(s)

def sub2(base, s, x, y, size=15, anchor='middle', cls='math'):
    # a symbol with a subscript, e.g. W_3 or A_s
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

def arrow_marker(mid):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker>')

# ---------------------------------------------------------------- Post's simple set
# Each W_e (e <= 4) is drawn on 0..14; x_e is the element above 2e found by the search.
W = [[0, 2, 5, 13], [1, 6, 9], [3, 4, 11], [1, 5], [6, 9, 14]]
X = [2, 6, 11, None, 9]
N, c, x0, y0, dy = 15, 26, 70, 40, 32
s = ['<svg class="fig" viewBox="0 0 590 245" width="590" role="img" aria-label="Post\'s simple set: each W_e contributes at most one element, and only an element greater than 2e">']
for k in range(N):
    s.append(f'<text x="{x0 + c*k + c/2}" y="{y0 - 10}" text-anchor="middle" class="mrm muted" font-size="11">{k}</text>')
for e, (we, xe) in enumerate(zip(W, X)):
    y = y0 + dy * e
    s.append(sub2('W', str(e), x0 - 26, y + 17, 16))
    for k in range(N):
        cl = 'cell head-cell' if k == xe else 'cell'
        s.append(f'<rect x="{x0 + c*k}" y="{y}" width="{c}" height="{c - 4}" class="{cl}"/>')
        if k <= 2 * e:
            s.append(f'<rect x="{x0 + c*k + 3}" y="{y + 3}" width="{c - 6}" height="{c - 10}" class="muted-fill" opacity="0.25"/>')
        if k in we:
            s.append(f'<circle cx="{x0 + c*k + c/2}" cy="{y + (c - 4)/2}" r="4" class="ink-fill"/>')
    bx = x0 + c * (2 * e + 1)
    s.append(f'<line x1="{bx}" y1="{y - 3}" x2="{bx}" y2="{y + c - 1}" class="accent-stroke" stroke-width="2"/>')
    note = f'<tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">{e}</tspan><tspan dy="-3"> = {xe}</tspan>' if xe is not None else f'<tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">{e}</tspan><tspan dy="-3"> undefined</tspan>'
    s.append(f'<text x="{x0 + c*N + 14}" y="{y + 15}" class="label">{note}</text>')
y = y0 + dy * len(W) + 8
s.append(f'<text x="{x0 - 26}" y="{y + 17}" text-anchor="middle" class="math" font-size="16">S</text>')
for k in range(N):
    cl = 'cell head-cell' if k in X else 'cell'
    s.append(f'<rect x="{x0 + c*k}" y="{y}" width="{c}" height="{c - 4}" class="{cl}"/>')
    if k in X:
        s.append(f'<circle cx="{x0 + c*k + c/2}" cy="{y + (c - 4)/2}" r="4" class="accent-fill"/>')
s.append(f'<text x="{x0 + c*N + 14}" y="{y + 15}" class="label">contributions of e ≤ 4</text>')
s.append('</svg>')
out['post-simple'] = ''.join(s)

# ---------------------------------------------------------------- the strategy of R_2e and freshness
N, c, x0 = 20, 23, 60
yA, yB = 52, 150
u, xw, st, xhi = 9, 6, 13, 3
s = ['<svg class="fig" viewBox="0 0 590 230" width="590" role="img" aria-label="The action of R_2e: its witness x enters B, the oracle A is frozen below the use u, and the requirements of lower priority later use only fresh numbers, greater than the stage">']
s.append('<defs>' + arrow_marker('ce-fm-arrow') + '</defs>')
for name, y in (('A', yA), ('B', yB)):
    s.append(f'<text x="{x0 - 26}" y="{y + 16}" text-anchor="middle" class="math" font-size="17">{name}</text>')
    for k in range(N):
        s.append(f'<rect x="{x0 + c*k}" y="{y}" width="{c}" height="{c}" class="cell"/>')
    for k in range(st + 1, N):
        s.append(f'<rect x="{x0 + c*k + 3}" y="{y + 3}" width="{c - 6}" height="{c - 6}" class="soft-fill"/>')
    s.append(f'<text x="{x0 + c*N + 8}" y="{y + 16}" class="mrm muted" font-size="15">⋯</text>')
for k in range(N):
    s.append(f'<text x="{x0 + c*k + c/2}" y="{yA - 8}" text-anchor="middle" class="mrm muted" font-size="10">{k}</text>')
# use bracket on A
s.append(f'<path d="M{x0 + 2},{yA + c + 6} L{x0 + 2},{yA + c + 12} L{x0 + c*u - 2},{yA + c + 12} L{x0 + c*u - 2},{yA + c + 6}" class="accent-stroke" stroke-width="1.6"/>')
s.append(f'<text x="{x0 + c*u/2}" y="{yA + c + 28}" text-anchor="middle" class="label">below the use <tspan class="math" font-size="13">u</tspan>: kept fixed (restraint)</text>')
# witness on B
s.append(f'<rect x="{x0 + c*xw}" y="{yB}" width="{c}" height="{c}" class="cell head-cell"/>')
s.append(f'<text x="{x0 + c*xw + c/2}" y="{yB + 16}" text-anchor="middle" class="mrm" font-size="13">1</text>')
s.append(f'<text x="{x0 + c*xw + c/2}" y="{yB + c + 16}" text-anchor="middle" class="math" font-size="14">x</text>')
s.append(f'<line x1="{x0 + c*xw + c/2}" y1="{yA + c + 34}" x2="{x0 + c*xw + c/2}" y2="{yB - 4}" class="ink-stroke" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#ce-fm-arrow)"/>')
s.append(f'<text x="{x0 + c*xw + c/2 + 8}" y="{yB - 14}" class="label"><tspan class="mrm" font-size="13">Φ</tspan><tspan class="math" dy="-6" font-size="10">A</tspan><tspan class="mrm" font-size="8" dy="3">s</tspan><tspan class="mrm" font-size="13" dy="3">(</tspan><tspan class="math" font-size="13">x</tspan><tspan class="mrm" font-size="13">) = 0</tspan> at stage <tspan class="math" font-size="13">s</tspan>: enumerate <tspan class="math" font-size="13">x</tspan> into <tspan class="math" font-size="13">B</tspan></text>')
# fresh region
s.append(f'<text x="{x0 + c*(st + 1)}" y="{yB + c + 16}" class="label">numbers &gt; s: fresh witnesses</text>')
s.append(f'<text x="{x0 + c*(st + 1)}" y="{yB + c + 31}" class="label">of lower priority</text>')
# higher priority witness inside the frozen part
s.append(f'<path d="M{x0 + c*xhi + 6},{yA + 6} L{x0 + c*xhi + c - 6},{yA + c - 6} M{x0 + c*xhi + 6},{yA + c - 6} L{x0 + c*xhi + c - 6},{yA + 6}" class="ink-stroke" stroke-width="1.6"/>')
s.append(f'<text x="{x0}" y="{yB + c + 50}" class="label">× a witness of higher priority, chosen before stage s, may still enter below <tspan class="math" font-size="13">u</tspan>: an injury</text>')
s.append('</svg>')
out['fm-strategy'] = ''.join(s)

# ---------------------------------------------------------------- walls of the low simple set
x0, sc, y0, dy = 80, 15, 40, 30
M = 30
walls = [5, 0, 12, 22]
Wpts, chosen = [2, 9, 14, 25], 14
s = ['<svg class="fig" viewBox="0 0 590 236" width="590" role="img" aria-label="The restraints of the negative requirements as walls: P_2 enumerates an element of W_2 beyond the walls of N_0, N_1, N_2 and beyond 4, possibly injuring N_3">']
for k in range(0, M + 1, 5):
    s.append(f'<text x="{x0 + sc*k}" y="{y0 - 14}" text-anchor="middle" class="mrm muted" font-size="11">{k}</text>')
    s.append(f'<line x1="{x0 + sc*k}" y1="{y0 - 8}" x2="{x0 + sc*k}" y2="{y0 + dy*5 - 6}" class="axis" stroke-dasharray="2 4"/>')
for i, r in enumerate(walls):
    y = y0 + dy * i
    s.append(sub2('N', str(i), x0 - 30, y + 14, 16))
    cl = 'soft-fill accent-stroke' if i <= 2 else 'muted-fill'
    if r > 0:
        s.append(f'<rect x="{x0}" y="{y + 2}" width="{sc*r}" height="14" class="{cl}" stroke-width="1"/>')
        s.append(f'<text x="{x0 + sc*r + 6}" y="{y + 14}" class="label">r = {r}</text>')
    else:
        s.append(f'<text x="{x0 + 4}" y="{y + 14}" class="label">r = 0 (no computation)</text>')
y = y0 + dy * 4
s.append(sub2('W', '2', x0 - 30, y + 14, 16))
s.append(f'<line x1="{x0}" y1="{y + 9}" x2="{x0 + sc*M}" y2="{y + 9}" class="axis"/>')
for p in Wpts:
    cl = 'accent-fill' if p == chosen else 'ink-fill'
    s.append(f'<circle cx="{x0 + sc*p}" cy="{y + 9}" r="{6 if p == chosen else 4}" class="{cl}"/>')
bound = max(walls[:3] + [4])
s.append(f'<line x1="{x0 + sc*bound}" y1="{y0 - 6}" x2="{x0 + sc*bound}" y2="{y + 24}" class="accent-stroke" stroke-width="2"/>')
def ms(base, k, after):
    # an italic letter with a roman subscript, followed by label text (non-breaking spaces survive)
    return (f'<tspan class="math" font-size="14">{base}</tspan><tspan class="mrm" font-size="9" dy="3">{k}</tspan>'
            '<tspan dy="-3">' + after.replace(' ', '\u00a0') + '</tspan>')
s.append(f'<text x="{x0}" y="{y + 36}" class="label">' + ms('P', 2, ' enumerates the least element of ') + ms('W', 2, ' beyond 4 and beyond the walls of ')
         + ms('N', 0, ', ') + ms('N', 1, ', ') + ms('N', 2, ';') + '</text>')
s.append(f'<text x="{x0}" y="{y + 54}" class="label">the wall of ' + ms('N', 3, ', of lower priority, is ignored, and ') + ms('N', 3, ' is injured') + '</text>')
s.append('</svg>')
out['walls'] = ''.join(s)

# ---------------------------------------------------------------- length of agreement in the Sacks strategy
c = 26
def panel(x0, title, Bv, Pv, l, prot, note):
    s = []
    y0 = 52
    s.append(f'<text x="{x0 + c*4}" y="20" text-anchor="middle" class="label">{title}</text>')
    for k in range(len(Bv)):
        s.append(f'<text x="{x0 + c*k + c/2}" y="{y0 - 8}" text-anchor="middle" class="mrm muted" font-size="11">{k}</text>')
    rows = [(Bv, 'B'), (Pv, 'P')]
    for r, (vals, name) in enumerate(rows):
        y = y0 + r * (c + 4)
        for k, v in enumerate(vals):
            cl = 'cell'
            if k == l:
                cl = 'cell head-cell'
            s.append(f'<rect x="{x0 + c*k}" y="{y}" width="{c}" height="{c}" class="{cl}"/>')
            s.append(f'<text x="{x0 + c*k + c/2}" y="{y + 18}" text-anchor="middle" class="mrm" font-size="14">{v}</text>')
    # agreement bracket
    yb = y0 + 2 * (c + 4) + 4
    if l > 0:
        s.append(f'<path d="M{x0 + 2},{yb} L{x0 + 2},{yb + 6} L{x0 + c*l - 2},{yb + 6} L{x0 + c*l - 2},{yb}" class="ink-stroke" stroke-width="1.3"/>')
        s.append(f'<text x="{x0 + c*l/2}" y="{yb + 20}" text-anchor="middle" class="label">agreement, l = {l}</text>')
    # protected uses
    yp = yb + 32
    s.append(f'<rect x="{x0}" y="{yp}" width="{c*prot}" height="12" class="soft-fill accent-stroke" stroke-width="1"/>')
    s.append(f'<text x="{x0}" y="{yp + 28}" class="label">{note}</text>')
    return s

s = ['<svg class="fig" viewBox="0 0 590 200" width="590" role="img" aria-label="The length of agreement between the reduction and B at two stages; when a number enters B below the length of agreement, the computation there becomes a disagreement and remains protected">']
s.append('<text x="40" y="74" text-anchor="end" class="math" font-size="15">B<tspan class="mrm" font-size="10" dy="4">t</tspan></text>')
s.append('<text x="40" y="104" text-anchor="end" class="mrm" font-size="15">Φ<tspan class="math" font-size="10" dy="-6">A</tspan><tspan class="mrm" font-size="8" dy="3">i,t</tspan></text>')
s += panel(56, 'stage t = s', list('00100100'), list('001001↑0'), 6, 6, 'protected: the uses at x &lt; 6')
s += panel(338, 'stage t > s, after 3 has entered B', list('00110100'), list('001001↑0'), 3, 4, 'protected: the uses at x ≤ 3')
s.append('</svg>')
out['agreement'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
