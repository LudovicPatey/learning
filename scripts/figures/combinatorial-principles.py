# Generates the inline SVG figures of the course on combinatorial principles below
# Ramsey's theorem for pairs.
# Usage: python3 scripts/figures/combinatorial-principles.py out.json
# Paste each figure into the lesson that uses it:
#   cut-construction                  -> orders.md
#   tournament                        -> erdos-moser.md
#   zoo                               -> ads-dnr.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

# ---------------------------------------------------------------- the cut construction (Tennenbaum, Denisov)
# Elements of the finite order at stage s, from left to right, with their roles.
# roles: 'a' protected on the left by a stronger requirement, 'b' protected on the right,
# 'u', 'v' the two elements of W_e chosen by R_e, '' an ordinary element.
elements = ['', '', 'a', '', 'u', '', '', 'v', '', 'b', '', '']
x0, dx, y = 50, 46, 92
old_cut = 7.5   # the cut before R_e acts: between positions 7 and 8
new_cut = 4.5   # after: immediately after u
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="The finite linear order at a stage, drawn from left to right, with a cut separating the left part from the right part. Two elements protected by stronger requirements bound an interval; the requirement R e picks two elements u and v of W e inside this interval and moves the cut to immediately after u">']
s.append('<defs>' + marker('cc-arrow', 'accent-fill') + '</defs>')
left = x0 + 2 * dx
right = x0 + 9 * dx
s.append(f'<rect x="{left + 8}" y="{y - 22}" width="{right - left - 16}" height="44" rx="6" class="soft-fill"/>')
s.append(f'<line x1="{x0 - 20}" y1="{y}" x2="{x0 + 11 * dx + 20}" y2="{y}" class="muted-stroke" stroke-width="1"/>')
for i, role in enumerate(elements):
    cx = x0 + i * dx
    if role in ('a', 'b'):
        s.append(f'<circle cx="{cx}" cy="{y}" r="8" class="head-cell"/>')
    elif role in ('u', 'v'):
        s.append(f'<circle cx="{cx}" cy="{y}" r="8" class="node"/>')
        s.append(f'<circle cx="{cx}" cy="{y}" r="3.5" class="ink-fill"/>')
    else:
        s.append(f'<circle cx="{cx}" cy="{y}" r="5" class="node"/>')
    if role:
        s.append(f'<text x="{cx}" y="{y + 30}" text-anchor="middle" class="math">{role}</text>')
oc = x0 + old_cut * dx
nc = x0 + new_cut * dx
s.append(f'<line x1="{oc}" y1="{y - 40}" x2="{oc}" y2="{y + 40}" class="muted-stroke" stroke-width="1.6" stroke-dasharray="5 4"/>')
s.append(f'<text x="{oc}" y="{y - 46}" text-anchor="middle" class="label">old cut</text>')
s.append(f'<line x1="{nc}" y1="{y - 40}" x2="{nc}" y2="{y + 40}" class="ink-stroke" stroke-width="1.8"/>')
s.append(f'<text x="{nc}" y="{y - 46}" text-anchor="middle" class="label">new cut</text>')
s.append(f'<path d="M{oc - 6},{y + 46} Q{(oc + nc) / 2},{y + 66} {nc + 6},{y + 46}" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#cc-arrow)"/>')
s.append(f'<text x="{(left + right) / 2}" y="{y + 84}" text-anchor="middle" class="label">the interval of R_e: strictly between the protected elements of stronger requirements</text>')
s.append(f'<text x="{x0 - 20}" y="24" class="label">left part: guessed in A</text>')
s.append(f'<text x="{x0 + 11 * dx + 20}" y="24" text-anchor="end" class="label">right part: guessed in A*</text>')
s.append('</svg>')
out['cut-construction'] = ''.join(s)

# ---------------------------------------------------------------- a tournament on five vertices
import math
arcs = [(0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3), (3, 4), (4, 0), (4, 1), (2, 4)]
transitive = {(0, 1), (1, 3), (0, 3)}
cx, cy, R = 300, 128, 92
pos = {}
for v in range(5):
    a = -math.pi / 2 + 2 * math.pi * v / 5
    pos[v] = (round(cx + R * math.cos(a), 1), round(cy + R * math.sin(a), 1))
s = ['<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="A tournament on five vertices, numbered 0 to 4, drawn on a pentagon with an arrow from each winner to each loser. The arrows among 0, 1 and 3 are highlighted: 0 beats 1, 1 beats 3 and 0 beats 3, a transitive subtournament. The vertices 0, 1 and 2 form a cycle">']
s.append('<defs>' + marker('em-arrow', 'muted-fill') + marker('em-arrow-a', 'accent-fill') + '</defs>')
for (u, v) in arcs:
    (x1, y1), (x2, y2) = pos[u], pos[v]
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    a1 = (round(x1 + 15 * ux, 1), round(y1 + 15 * uy, 1))
    a2 = (round(x2 - 17 * ux, 1), round(y2 - 17 * uy, 1))
    if (u, v) in transitive:
        s.append(f'<line x1="{a1[0]}" y1="{a1[1]}" x2="{a2[0]}" y2="{a2[1]}" class="accent-stroke" stroke-width="2.2" marker-end="url(#em-arrow-a)"/>')
    else:
        s.append(f'<line x1="{a1[0]}" y1="{a1[1]}" x2="{a2[0]}" y2="{a2[1]}" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/>')
for v in range(5):
    x, y = pos[v]
    cls = 'head-cell' if v in (0, 1, 3) else 'node'
    s.append(f'<circle cx="{x}" cy="{y}" r="13" class="{cls}"/>')
    s.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="14">{v}</text>')
s.append('<text x="30" y="60" class="label">an arrow x → y: x beats y</text>')
s.append('<text x="30" y="80" class="label">highlighted: {0, 1, 3}, transitive</text>')
s.append('<text x="30" y="100" class="label">0 → 1 → 2 → 0: a cycle</text>')
s.append('</svg>')
out['tournament'] = ''.join(s)

# ---------------------------------------------------------------- the zoo below RT22 and WKL0
nodes = {
    'ACA': (330, 34, 'ACA₀'),
    'RT22': (250, 98, 'RT²₂'), 'WKL': (500, 98, 'WKL₀'),
    'CAC': (100, 162, 'CAC'), 'SRT22': (250, 162, 'SRT²₂'), 'EM': (370, 162, 'EM'), 'WWKL': (500, 162, 'WWKL₀'),
    'ADS': (60, 228, 'ADS'), 'SCAC': (190, 228, 'SCAC'), 'DNR': (450, 240, 'DNR'),
    'COH': (40, 294, 'COH'), 'SADS': (160, 294, 'SADS'),
    'CADS': (40, 358, 'CADS'),
}
edges = [('ACA', 'RT22'), ('ACA', 'WKL'), ('RT22', 'CAC'), ('RT22', 'SRT22'), ('RT22', 'EM'),
         ('WKL', 'WWKL'), ('WWKL', 'DNR'), ('CAC', 'ADS'), ('CAC', 'SCAC'), ('SRT22', 'SCAC'),
         ('SCAC', 'SADS'), ('ADS', 'SADS'), ('ADS', 'COH'), ('SRT22', 'DNR'), ('EM', 'DNR')]
dashed = [('COH', 'CADS')]
W, H = 56, 26
s = ['<svg class="fig" viewBox="0 0 600 390" width="600" role="img" aria-label="A diagram of implications between principles: ACA0 implies RT22 and WKL0; RT22 implies CAC, SRT22 and EM; WKL0 implies WWKL0, which implies DNR; CAC implies ADS and SCAC; SRT22 implies SCAC and DNR; EM implies DNR; SCAC and ADS imply SADS; ADS implies COH, which implies CADS">']
s.append('<defs>' + marker('zoo-arrow', 'ink-fill') + marker('zoo-arrow-m', 'muted-fill') + '</defs>')
def seg(a, b):
    (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
    import math
    dx, dy = x2 - x1, y2 - y1
    # shorten the segment so that it starts and ends on the boxes
    def cut(dx, dy):
        tx = (W / 2) / abs(dx) if dx else 1e9
        ty = (H / 2) / abs(dy) if dy else 1e9
        return min(tx, ty)
    c = cut(dx, dy)
    return (round(x1 + dx * c, 1), round(y1 + dy * c, 1), round(x2 - dx * (c + 0.06), 1), round(y2 - dy * (c + 0.06), 1))
for a, b in edges:
    x1, y1, x2, y2 = seg(a, b)
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/>')
for a, b in dashed:
    x1, y1, x2, y2 = seg(a, b)
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#zoo-arrow-m)"/>')
for k, (x, y, lab) in nodes.items():
    cls = 'head-cell' if k in ('ACA', 'WKL') else 'cell'
    s.append(f'<rect x="{x - W / 2}" y="{y - H / 2}" width="{W}" height="{H}" rx="5" class="{cls}"/>')
    s.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="14">{lab}</text>')
s.append('<text x="590" y="320" text-anchor="end" class="label">arrow: implication over RCA₀</text>')
s.append('<text x="590" y="338" text-anchor="end" class="label">solid arrows are strict</text>')
s.append('<text x="590" y="356" text-anchor="end" class="label">dashed: strictness unknown</text>')
s.append('</svg>')
out['zoo'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
