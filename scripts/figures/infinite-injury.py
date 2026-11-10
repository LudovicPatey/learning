# Generates the inline SVG figure of the course on infinite injury arguments:
# the first levels of the tree of strategies of the minimal pair construction.
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

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
