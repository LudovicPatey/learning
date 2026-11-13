# Generates the inline SVG figures of the course on custom separations and forcing design.
# Usage: python3 scripts/figures/separation-design.py out.json
# Paste each figure into the lesson that uses it:
#   em-condition    -> erdos-moser-design.md
#   split-triple    -> chain-antichain.md
#   cb-columns      -> separating-instances.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(name, index, x, y, size=14, anchor='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="math" font-size="{size}">{name}'
            f'<tspan class="mrm" font-size="{size - 4}" dy="3">{index}</tspan></text>')


# ---------------------------------------------------------------- an EM condition
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="An Erdős–Moser condition: four stem elements above a reservoir; each stem element either beats every reservoir element or is beaten by every reservoir element">']
s.append('<defs>' + marker('sd-em-arr') + '</defs>')
stem = [(120, 'down'), (220, 'up'), (320, 'down'), (420, 'up')]
s.append('<text x="40" y="64" class="label">stem σ</text>')
for k, (x, d) in enumerate(stem):
    s.append(f'<circle cx="{x}" cy="60" r="14" class="state"/>')
    s.append(sub('a', k + 1, x, 65))
# arrows inside the stem: a transitive order a1 -> a2 -> a3 -> a4 (drawn as arcs over the nodes)
for (x1, _), (x2, _) in zip(stem, stem[1:]):
    s.append(f'<path d="M{x1 + 10},46 Q{(x1 + x2) / 2},18 {x2 - 10},46" fill="none" class="muted-stroke" '
             f'stroke-width="1.1" marker-end="url(#sd-em-arr)"/>')
# reservoir box
s.append('<rect x="80" y="150" width="400" height="56" rx="10" class="cell"/>')
s.append('<text x="40" y="184" class="label">X</text>')
for x in range(100, 470, 24):
    s.append(f'<circle cx="{x}" cy="178" r="3.5" class="accent-fill"/>')
for x, d in stem:
    if d == 'down':
        s.append(f'<line x1="{x}" y1="76" x2="{x}" y2="146" class="ink-stroke" stroke-width="1.4" marker-end="url(#sd-em-arr)"/>')
    else:
        s.append(f'<line x1="{x}" y1="148" x2="{x}" y2="78" class="ink-stroke" stroke-width="1.4" marker-end="url(#sd-em-arr)"/>')
s.append('<text x="500" y="110" class="label">arrow down:</text>')
s.append('<text x="500" y="126" class="label">beats all of X</text>')
s.append('<text x="500" y="150" class="label">arrow up:</text>')
s.append('<text x="500" y="166" class="label">beaten by all</text>')
s.append('<text x="80" y="234" class="label">(b): for every y ∈ X, the set σ ∪ {y} contains no 3-cycle</text>')
s.append('</svg>')
out['em-condition'] = ''.join(s)

# ---------------------------------------------------------------- a split triple
s = ['<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="A split triple: an ascending block at the bottom, an antichain block in the middle, a descending block at the top; every element of a lower block is below every element of a higher block in the partial order">']
rows = [(220, 'ρ', '0', 'ascending', [150, 230, 310]),
        (140, 'ρ', '2', 'antichain', [130, 210, 290, 370]),
        (60, 'ρ', '1', 'descending', [170, 250, 330])]
pos = {}
for y, n, i, lab, xs in rows:
    s.append(sub(n, i, 60, y + 5))
    s.append(f'<text x="420" y="{y + 5}" class="label">{lab}</text>')
    pos[i] = [(x, y) for x in xs]
# order lines: every element of rho_0 below every element of rho_2, and of rho_2 below rho_1
for a, b in (('0', '2'), ('2', '1')):
    for (x1, y1) in pos[a]:
        for (x2, y2) in pos[b]:
            s.append(f'<line x1="{x1}" y1="{y1 - 9}" x2="{x2}" y2="{y2 + 9}" class="muted-stroke" stroke-width="0.8"/>')
# chains inside rho_0 and rho_1 (ascending: increasing in the order as numbers grow)
for i in ('0', '1'):
    pts = pos[i]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        s.append(f'<line x1="{x1 + 9}" y1="{y1}" x2="{x2 - 9}" y2="{y2}" class="accent-stroke" stroke-width="1.6"/>')
for i in ('0', '2', '1'):
    for (x, y) in pos[i]:
        s.append(f'<circle cx="{x}" cy="{y}" r="8" class="state"/>')
s.append('<text x="60" y="258" class="label">lines: the order of P between blocks (lower is smaller); thick lines: comparabilities inside a block</text>')
s.append('</svg>')
out['split-triple'] = ''.join(s)

# ---------------------------------------------------------------- columns of the c.b.-immune set
mu = [2, 3, 5, 4, 7, 6]          # heights of the cuts mu(i), with mu(i) > i
holes = {1: [1], 2: [0, 3], 4: [2, 5], 5: [1]}   # elements of W, at most i in column i
CW, CH, X0, Y0 = 52, 22, 110, 220
s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Columns X0 to X5; each column is filled up to the height mu(i), with a few holes for the elements of W; the elements above the cut are not in A">']
for i, m in enumerate(mu):
    x = X0 + i * (CW + 14)
    for k in range(8):
        y = Y0 - (k + 1) * CH
        if k < m and k not in holes.get(i, []):
            cls = 'cell head-cell'
        else:
            cls = 'cell'
        s.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" class="{cls}"/>')
    s.append(f'<line x1="{x - 4}" y1="{Y0 - m * CH}" x2="{x + CW + 4}" y2="{Y0 - m * CH}" class="accent-stroke" stroke-width="2"/>')
    s.append(sub('X', i, x + CW / 2, Y0 + 22))
s.append(f'<text x="{X0 - 12}" y="{Y0 - 4}" text-anchor="end" class="label">height 0</text>')
s.append(f'<text x="{X0 - 12}" y="{Y0 - 8 * CH + 14}" text-anchor="end" class="label">height 7</text>')
s.append('<rect x="110" y="262" width="12" height="12" class="cell head-cell"/>')
s.append('<text x="128" y="272" class="label">element of A</text>')
s.append('<line x1="240" y1="268" x2="266" y2="268" class="accent-stroke" stroke-width="2"/>')
s.append('<text x="272" y="272" class="label">cut at μ(i)</text>')
s.append('<text x="370" y="272" class="label">empty below the cut: element of W</text>')
s.append('</svg>')
out['cb-columns'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
