# Generates the inline SVG figures of the course on infinite injury arguments:
#   tree       the first levels of the tree of strategies (trees-of-strategies)
#   agreement  the preservation of agreement between expansionary stages (minimal-pairs)
#   regions    the nodes that may act between two alpha-expansionary stages (minimal-pair-verification)
#   column     a column of H at the action of a P-node below an infinitary outcome (high-incomplete-verification)
# Usage: python3 scripts/figures/infinite-injury.py out.json
import json, sys
out = {}

# Levels: N_0, R_0, S_0, N_1, R_1. Only N nodes branch (outcomes oo < f).
levels = ['N', 'R', 'S', 'N', 'R']
reqs = ['N<tspan class="mrm" font-size="10" dy="4">0</tspan>',
        'R<tspan class="mrm" font-size="10" dy="4">0</tspan>',
        'S<tspan class="mrm" font-size="10" dy="4">0</tspan>',
        'N<tspan class="mrm" font-size="10" dy="4">1</tspan>',
        'R<tspan class="mrm" font-size="10" dy="4">1</tspan>']
Y = [34 + 46 * k for k in range(5)]
X = {0: [250], 1: [130, 370], 2: [130, 370], 3: [130, 370], 4: [70, 190, 310, 430]}
# Strings over {i, f} (i stands for the infinite outcome) for the nodes of each level.
nodes = {0: [''], 1: ['i', 'f'], 2: ['if', 'ff'], 3: ['iff', 'fff'], 4: ['iffi', 'ifff', 'fffi', 'ffff']}
true_path = 'iffi'  # a possible true path, drawn in the accent color

def on_path(s):
    return true_path.startswith(s)

def pos(s):
    k = len(s)
    return X[k][nodes[k].index(s)], Y[k]

s = ['<svg class="fig" viewBox="0 0 590 250" width="590" role="img" aria-label="The first levels of the tree of strategies of the minimal pair construction: each N node has two outcomes, infinite on the left and finite on the right; the other nodes have one outcome">']
for k in range(1, 5):
    for c in nodes[k]:
        p = c[:-1]
        (x1, y1), (x2, y2) = pos(p), pos(c)
        cl = 'accent-stroke' if on_path(c) else 'muted-stroke'
        w = '2.4' if on_path(c) else '1.3'
        s.append(f'<line x1="{x1}" y1="{y1 + 7}" x2="{x2}" y2="{y2 - 7}" class="{cl}" stroke-width="{w}"/>')
        if levels[k - 1] == 'N':
            lab = '∞' if c[-1] == 'i' else 'f'
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            dx = -12 if c[-1] == 'i' else 8
            fam = 'mrm' if c[-1] == 'i' else 'math'
            s.append(f'<text x="{mx + dx:.0f}" y="{my + 2:.0f}" class="{fam}" font-size="14">{lab}</text>')
for k in range(5):
    for c in nodes[k]:
        x, y = pos(c)
        cl = 'accent-fill' if on_path(c) else 'node'
        s.append(f'<circle cx="{x}" cy="{y}" r="6" class="{cl}"/>')
for x, _ in [pos(c) for c in nodes[4]]:
    s.append(f'<line x1="{x}" y1="{Y[4] + 8}" x2="{x}" y2="{Y[4] + 26}" class="muted-stroke" stroke-width="1.3" stroke-dasharray="2 3"/>')
for k in range(5):
    s.append(f'<text x="520" y="{Y[k] + 5}" class="math" font-size="16">{reqs[k]}</text>')
    s.append(f'<line x1="470" y1="{Y[k]}" x2="505" y2="{Y[k]}" class="axis" stroke-dasharray="2 4"/>')
s.append('</svg>')
out['tree'] = ''.join(s)


def sub(base, s, x, y, size=15, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

def arrow_marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

# ---------------------------------------------------------------- agreement: preservation lemma
# Stages s_0 < s_1 < s_2 < s_3; between s_k and s_{k+1} one side is unchanged below s_k.
xs = [110, 230, 350, 470]
yA, yB = 50, 125
kept = ['A', 'B', 'A']          # side unchanged below s_k between s_k and s_{k+1}
s = ['<svg class="fig" viewBox="0 0 590 230" width="590" role="img" aria-label="Four expansionary stages; at each of them the computations on the A side and on the B side agree; between two consecutive stages one side is unchanged below the earlier stage, and the common value is carried along a zigzag path">']
s.append('<defs>' + arrow_marker('ii-agr-arrow', 'accent-fill') + '</defs>')
s.append(f'<text x="30" y="{yA + 5}" class="label">A side</text>')
s.append(f'<text x="30" y="{yB + 5}" class="label">B side</text>')
for k in range(3):
    xa, xb = xs[k] + 9, xs[k + 1] - 9
    for side, y in (('A', yA), ('B', yB)):
        if kept[k] == side:
            s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="accent-stroke" stroke-width="2.4" marker-end="url(#ii-agr-arrow)"/>')
        else:
            s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 4"/>')
for k, x in enumerate(xs):
    on = [kept[k - 1] if k > 0 else None, kept[k] if k < 3 else None]
    s.append(f'<line x1="{x - 2}" y1="{yA + 9}" x2="{x - 2}" y2="{yB - 9}" class="accent-stroke" stroke-width="1.6"/>')
    s.append(f'<line x1="{x + 2}" y1="{yA + 9}" x2="{x + 2}" y2="{yB - 9}" class="accent-stroke" stroke-width="1.6"/>')
    s.append(f'<circle cx="{x}" cy="{yA}" r="6" class="node"/>')
    s.append(f'<circle cx="{x}" cy="{yB}" r="6" class="node"/>')
    s.append(sub('s', str(k), x, yB + 34))
    s.append(f'<line x1="{x}" y1="{yB + 12}" x2="{x}" y2="{yB + 18}" class="axis"/>')
s.append(f'<line x1="{xs[0] - 30}" y1="{yB + 15}" x2="{xs[-1] + 40}" y2="{yB + 15}" class="axis"/>')
s.append(f'<text x="{xs[-1] + 46}" y="{yB + 19}" class="label">stages</text>')
ly = yB + 66
s.append(f'<line x1="40" y1="{ly}" x2="80" y2="{ly}" class="accent-stroke" stroke-width="2.4"/><text x="88" y="{ly + 4}" class="label">unchanged below the earlier stage</text>')
s.append(f'<line x1="310" y1="{ly}" x2="350" y2="{ly}" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 4"/><text x="358" y="{ly + 4}" class="label">may change</text>')
s.append(f'<line x1="38" y1="{ly + 22}" x2="38" y2="{ly + 36}" class="accent-stroke" stroke-width="1.6"/><line x1="42" y1="{ly + 22}" x2="42" y2="{ly + 36}" class="accent-stroke" stroke-width="1.6"/><text x="52" y="{ly + 33}" class="label">agreement at an expansionary stage</text>')
s.append('</svg>')
out['agreement'] = ''.join(s)

# ---------------------------------------------------------------- regions around an N-node alpha
s = ['<svg class="fig" viewBox="0 0 600 315" width="600" role="img" aria-label="The node alpha on the true path, its prefixes, the subtrees below its two outcomes, and the nodes to its left and to its right, with what each group can do between two consecutive alpha-expansionary stages">']
rx, ry = 300, 36
ax, ay = 300, 112
ix, fx, cy, by = 240, 360, 160, 252   # children of alpha, top and base of their subtrees
w = 52                                # half-width of a subtree at its base
s.append(f'<polygon points="{rx - 12},{ry} {ax - 14},{ay + 4} {ix - w - 6},{by} 30,{by}" class="cell" stroke-dasharray="3 3"/>')
s.append(f'<polygon points="{rx + 12},{ry} {ax + 14},{ay + 4} {fx + w + 6},{by} 570,{by}" class="cell" stroke-dasharray="3 3"/>')
s.append(f'<polygon points="{ix},{cy + 8} {ix - w},{by} {ix + w},{by}" class="soft-fill"/>')
s.append(f'<polygon points="{fx},{cy + 8} {fx - w},{by} {fx + w},{by}" class="cell"/>')
s.append(f'<line x1="{rx}" y1="{ry}" x2="{ax}" y2="{ay}" class="accent-stroke" stroke-width="2.4"/>')
s.append(f'<circle cx="{rx}" cy="{ry}" r="5" class="accent-fill"/>')
s.append(f'<circle cx="{rx}" cy="{(ry + ay) // 2}" r="5" class="accent-fill"/>')
for (x, lab, fam) in ((ix, '∞', 'mrm'), (fx, 'f', 'math')):
    s.append(f'<line x1="{ax}" y1="{ay + 6}" x2="{x}" y2="{cy - 6}" class="ink-stroke" stroke-width="1.4"/>')
    mx = (ax + x) / 2 + (-16 if lab == '∞' else 8)
    s.append(f'<text x="{mx:.0f}" y="{(ay + cy) / 2:.0f}" class="{fam}" font-size="14">{lab}</text>')
    s.append(f'<circle cx="{x}" cy="{cy}" r="6" class="node"/>')
s.append(f'<circle cx="{ax}" cy="{ay}" r="7" class="accent-fill"/>')
s.append(f'<text x="{ax + 14}" y="{ay + 2}" class="math" font-size="16">α</text>')
def lines(x, y, txt, anchor='middle'):
    return ''.join(f'<text x="{x}" y="{y + 15 * i}" text-anchor="{anchor}" class="label">{t}</text>' for i, t in enumerate(txt))
s.append(lines(300, 16, ['prefixes of α: no action after s*']))
s.append(lines(110, 212, ['left of α: not', 'visited after s*']))
s.append(lines(490, 212, ['right of α: initialized', 'at each α-exp. stage']))
s.append(lines(ix, by + 22, ['below α⁀∞: act only', 'at α-exp. stages']))
s.append(lines(fx, by + 22, ['below α⁀f: initialized', 'at each α-exp. stage']))
s.append('</svg>')
out['regions'] = ''.join(s)

# ---------------------------------------------------------------- a column of H at the action of beta
def pair(x, y):
    return (x + y) * (x + y + 1) // 2 + y
e, s0, R, top = 1, 10, 3, 30
x0, u = 40, 17
yl = 90
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="The numbers of column 1 on the number line; at stage s_0 all of them with second coordinate below s_0 are in H except those below the restraint R; the restraint of beta is s_0">']
s.append(f'<rect x="{x0}" y="{yl - 26}" width="{u * s0}" height="52" class="soft-fill"/>')
s.append(f'<line x1="{x0}" y1="{yl}" x2="{x0 + u * top + 10}" y2="{yl}" class="axis"/>')
for n in range(0, top + 1, 5):
    s.append(f'<line x1="{x0 + u * n}" y1="{yl - 4}" x2="{x0 + u * n}" y2="{yl + 4}" class="axis"/>')
    s.append(f'<text x="{x0 + u * n}" y="{yl + 22}" text-anchor="middle" class="mrm muted" font-size="12">{n}</text>')
for X, lab, y in ((R, 'R', yl - 34), (s0, 's', yl - 34)):
    s.append(f'<line x1="{x0 + u * X}" y1="{yl - 28}" x2="{x0 + u * X}" y2="{yl + 28}" class="ink-stroke" stroke-width="1.4" stroke-dasharray="3 3"/>')
s.append(f'<text x="{x0 + u * R}" y="{yl - 34}" text-anchor="middle" class="math" font-size="15">R<tspan class="mrm" font-size="10" dy="4">α</tspan></text>')
s.append(f'<text x="{x0 + u * s0}" y="{yl - 34}" text-anchor="middle" class="math" font-size="15">s<tspan class="mrm" font-size="10" dy="4">0</tspan><tspan class="mrm" font-size="15" dy="-4">&#160;=&#160;</tspan>r<tspan class="mrm" font-size="10" dy="4">β</tspan></text>')
y = 0
while pair(e, y) <= top:
    n = pair(e, y)
    cls = 'node' if n < R else 'accent-fill'
    s.append(f'<circle cx="{x0 + u * n}" cy="{yl}" r="6" class="{cls}"/>')
    y += 1
ly = 150
s.append(f'<circle cx="{x0 + 6}" cy="{ly}" r="6" class="accent-fill"/><text x="{x0 + 18}" y="{ly + 4}" class="label">in H after the visit of α at stage <tspan class="math">s</tspan><tspan font-size="9" dy="3">0</tspan></text>')
s.append(f'<circle cx="{x0 + 246}" cy="{ly}" r="6" class="node"/><text x="{x0 + 258}" y="{ly + 4}" class="label">kept out by a restraint of higher priority</text>')
s.append(f'<rect x="{x0}" y="{ly + 16}" width="12" height="12" class="soft-fill"/><text x="{x0 + 18}" y="{ly + 26}" class="label">protected by β: contains the use of its computation</text>')
s.append('</svg>')
out['column'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
