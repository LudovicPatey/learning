# Generates the inline SVG figure of the course on Pi^0_1 classes.
# Usage: python3 scripts/figures/pi01-classes.py out.json
import json, sys
out = {}

# A binary tree of depth 5. Nodes are strings; 'ext' nodes lie on infinite paths,
# 'dead' nodes are in the tree but have no infinite extension.
depth = 5
tree = set([''])
dead_roots = {'01', '110', '1111'}           # subtrees that die out
alive = set()
def add(s):
    tree.add(s)
# build: all strings extending '00' and '10' and '1110' are alive (fully branching where shown)
def gen(prefix, maxd):
    out_ = [prefix]
    if len(prefix) < maxd:
        out_ += gen(prefix + '0', maxd) + gen(prefix + '1', maxd)
    return out_
alive_prefixes = ['000', '001', '100', '101', '1110']
for p in alive_prefixes:
    for s in gen(p, depth):
        tree.add(s)
        alive.add(s)
    for k in range(len(p)):
        tree.add(p[:k]); alive.add(p[:k])
# dead branches: in the tree, but finite
dead = {'01', '010', '0101', '110', '1100', '1101', '11001', '1111', '11110'}
tree |= dead
# keep the picture readable: prune alive nodes below depth 4 except along the highlighted path
path = '00101'
W, H = 600, 250
def pos(s):
    d = len(s)
    idx = int(s, 2) if s else 0
    x = 20 + (idx + 0.5) * (W - 40) / (2 ** d)
    y = 22 + d * 46
    return x, y
s_ = ['<svg class="fig" viewBox="0 0 600 306" width="600" role="img" aria-label="A binary tree: some branches die out, the others extend to infinite paths; one path is highlighted">']
shown = {n for n in tree if len(n) <= 4 or n.startswith(path[:4])}
for n in sorted(shown, key=len):
    if n == '':
        continue
    p = n[:-1]
    (x1, y1), (x2, y2) = pos(p), pos(n)
    on_path = path.startswith(n)
    cls = 'accent-stroke' if on_path else ('muted-stroke' if n in dead else 'ink-stroke')
    dash = ' stroke-dasharray="3 3"' if n in dead else ''
    sw = '2.2' if on_path else '1.2'
    s_.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{sw}"{dash}/>')
for n in shown:
    x, y = pos(n)
    if n in dead:
        s_.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.5" class="muted-fill"/>')
    else:
        s_.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="{"accent-fill" if path.startswith(n) else "ink-fill"}"/>')
# ellipses below alive leaves at depth 4
for n in shown:
    if len(n) == 4 and n not in dead and not n.startswith(path[:4]):
        x, y = pos(n)
        s_.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm muted" font-size="12">⋮</text>')
x, y = pos(path)
s_.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm" font-size="12">⋮</text>')
s_.append(f'<text x="{x + 14:.1f}" y="{y + 22}" class="label">a path X</text>')
s_.append(f'<text x="{pos("")[0] + 10:.1f}" y="{pos("")[1] - 4}" class="mrm" font-size="13">ε</text>')
s_.append('<line x1="24" y1="296" x2="44" y2="296" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="300" class="label">a finite branch: no infinite extension</text>')
s_.append('<line x1="300" y1="296" x2="320" y2="296" class="accent-stroke" stroke-width="2.2"/><text x="326" y="300" class="label">initial segments of an infinite path</text>')
s_.append('</svg>')
out['binary-tree'] = ''.join(s_)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
