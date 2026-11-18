# Generates the inline SVG figures of the course on arithmetical transfinite recursion.
# Usage: python3 scripts/figures/transfinite-recursion.py out.json
# Paste each figure into the lesson that uses it:
#   kb-order                          -> well-orderings.md
#   perfect-subtree                   -> pseudohierarchies.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

# ---------------------------------------------------------------- the Kleene-Brouwer order of a small tree
# nodes: name -> (x, y); edges parent -> child; rank in the KB order (1 = least)
nodes = {
    '': (300, 40), '0': (190, 110), '1': (420, 110),
    '00': (130, 180), '01': (250, 180), '10': (420, 180),
    '000': (130, 250),
}
kb = ['000', '00', '01', '0', '10', '1', '']
s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="A finite tree with root, nodes 0 and 1, nodes 00, 01 and 10, and node 000. Each node carries its position in the Kleene-Brouwer order: 000 is first, then 00, 01, 0, 10, 1, and the root is last; the order lists the children from left to right before the node itself">']
for name, (x, y) in nodes.items():
    if name:
        px, py = nodes[name[:-1]]
        s.append(f'<line x1="{px}" y1="{py + 14}" x2="{x}" y2="{y - 14}" class="muted-stroke" stroke-width="1.3"/>')
for name, (x, y) in nodes.items():
    s.append(f'<circle cx="{x}" cy="{y}" r="14" class="node"/>')
    s.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="13">{kb.index(name) + 1}</text>')
    lab = '⟨⟩' if name == '' else '⟨' + ','.join(name) + '⟩'
    s.append(f'<text x="{x + 20}" y="{y - 8}" class="label">{lab}</text>')
s.append('<text x="300" y="284" text-anchor="middle" class="label">numbers: positions in the Kleene–Brouwer order, from the least (1) to the greatest (7)</text>')
s.append('</svg>')
out['kb-order'] = ''.join(s)

# ---------------------------------------------------------------- building a perfect subtree along a descending sequence
# levels of the construction: tau at depth d lies in A_{g(d)}
pts = {'': (300, 40)}
xs = {0: [300], 1: [180, 420], 2: [120, 240, 360, 480]}
names = {0: [''], 1: ['0', '1'], 2: ['00', '01', '10', '11']}
ys = {0: 40, 1: 120, 2: 200}
s = ['<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="A binary splitting: the node tau of the empty string lies in A of g of 0; it has two incompatible extensions tau 0 and tau 1 in A of g of 1, each of which has two incompatible extensions in A of g of 2, and so on. The nodes are joined by paths of the tree, drawn as curves">']
for d in (1, 2):
    for k, name in enumerate(names[d]):
        x, y = xs[d][k], ys[d]
        px, py = xs[d - 1][k // 2], ys[d - 1]
        s.append(f'<path d="M{px},{py + 12} C{px},{py + 45} {x},{y - 45} {x},{y - 12}" class="muted-stroke" fill="none" stroke-width="1.3"/>')
for d in (0, 1, 2):
    for k, name in enumerate(names[d]):
        x, y = xs[d][k], ys[d]
        s.append(f'<circle cx="{x}" cy="{y}" r="11" class="node"/>')
        lab = 'τ' + ('' if name == '' else '') 
        s.append(f'<text x="{x + 16}" y="{y + 4}" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">{name if name else "⟨⟩"}</tspan></text>')
for d, lab in ((0, 'in A_g(0)'), (1, 'in A_g(1)'), (2, 'in A_g(2)')):
    s.append(f'<text x="590" y="{ys[d] + 4}" text-anchor="end" class="label">{lab}</text>')
for x in xs[2]:
    s.append(f'<line x1="{x}" y1="214" x2="{x}" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/>')
s.append('<text x="300" y="260" text-anchor="middle" class="label">each node of level d lies in A_g(d) ⊆ A′_g(d+1), so it splits inside A_g(d+1)</text>')
s.append('</svg>')
out['perfect-subtree'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
