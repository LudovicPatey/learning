# Generates the inline SVG figure of the course on the arithmetic hierarchy.
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

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
