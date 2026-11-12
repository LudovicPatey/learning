# Generates the inline SVG figures of the course Structure of the Turing degrees.
# Usage: python3 scripts/figures/degree-structure.py out.json
import json, sys
out = {}

def pair(k, y):
    # Cantor's pairing function, as in the course on countability
    return (k + y) * (k + y + 1) // 2 + y

def sub(base, s, x, y, size=14, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.7)}" dy="4">{s}</tspan></text>')

# ---------------------------------------------------------------- locked columns in the exact pair construction
# Stage s = 3, current string g_s of length 12: positions < 12 are decided,
# positions >= 12 in columns k < 3 must copy A_k, the others are free.
s_stage, length = 3, 12
rows, cols = 6, 10
c, x0, y0 = 34, 110, 30
s = [f'<svg class="fig" viewBox="0 0 600 320" width="600" role="img" aria-label="The positions of G arranged by column k and index y. Positions below the length of the current string are decided; beyond it, the positions of the columns k &lt; s must copy A_k, and the other columns are free">']
for k in range(rows):
    yy = y0 + c * (rows - 1 - k)
    s.append(f'<text x="{x0 - 10}" y="{yy + c/2 + 5}" text-anchor="end" class="label">column {k}</text>')
    for y in range(cols):
        p = pair(k, y)
        xx = x0 + c * y
        if p < length:
            cls = 'cell soft-fill'
            s.append(f'<rect x="{xx}" y="{yy}" width="{c}" height="{c}" class="cell"/>')
            s.append(f'<rect x="{xx + 3}" y="{yy + 3}" width="{c - 6}" height="{c - 6}" class="muted-fill" opacity="0.35"/>')
        elif k < s_stage:
            s.append(f'<rect x="{xx}" y="{yy}" width="{c}" height="{c}" class="cell head-cell"/>')
        else:
            s.append(f'<rect x="{xx}" y="{yy}" width="{c}" height="{c}" class="cell"/>')
        s.append(f'<text x="{xx + c/2}" y="{yy + c/2 + 4}" text-anchor="middle" class="mrm" font-size="11">{p}</text>')
for y in range(cols):
    s.append(f'<text x="{x0 + c*y + c/2}" y="{y0 + c*rows + 14}" text-anchor="middle" class="math" font-size="12">{y}</text>')
s.append(f'<text x="{x0 + c*cols + 8}" y="{y0 + c*rows + 14}" class="math" font-size="12">y</text>')
# separator between locked and free columns
ysep = y0 + c * (rows - s_stage)
s.append(f'<line x1="{x0 - 4}" y1="{ysep}" x2="{x0 + c*cols + 4}" y2="{ysep}" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/>')
s.append(f'<text x="{x0 + c*cols + 10}" y="{ysep + 4}" class="label">s = 3</text>')
ly = y0 + c * rows + 34
s.append(f'<rect x="{x0 - 90}" y="{ly}" width="14" height="14" class="cell"/><rect x="{x0 - 88}" y="{ly + 2}" width="10" height="10" class="muted-fill" opacity="0.35"/>')
s.append(f'<text x="{x0 - 70}" y="{ly + 11}" class="label">decided: position &lt; |g<tspan font-size="9" dy="3">s</tspan><tspan dy="-3">| = 12</tspan></text>')
s.append(f'<rect x="{x0 + 130}" y="{ly}" width="14" height="14" class="cell head-cell"/>')
s.append(f'<text x="{x0 + 150}" y="{ly + 11}" class="label">locked: copies A<tspan font-size="9" dy="3">k</tspan><tspan dy="-3">\u00a0for k &lt; 3</tspan></text>')
s.append(f'<rect x="{x0 + 330}" y="{ly}" width="14" height="14" class="cell"/>')
s.append(f'<text x="{x0 + 350}" y="{ly + 11}" class="label">free</text>')
s.append('</svg>')
out['locked-columns'] = ''.join(s)

# ---------------------------------------------------------------- embedding the diamond
order = {(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)}
s = ['<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="Left: the diamond order with 0 below 1 and 2, and 1 and 2 below 3. Right: the sets D_0 to D_3; the column m of D_n is the column G_m of a 1-generic set if m precedes n, and is empty otherwise">']
pos = {0: (110, 190), 1: (60, 115), 2: (160, 115), 3: (110, 40)}
for a, b in [(0, 1), (0, 2), (1, 3), (2, 3)]:
    (x1, y1), (x2, y2) = pos[a], pos[b]
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.3"/>')
for n, (x, y) in pos.items():
    s.append(f'<circle cx="{x}" cy="{y}" r="13" class="node"/>')
    s.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="14">{n}</text>')
s.append('<text x="110" y="214" text-anchor="middle" class="label">the order ⪯</text>')
cw, ch, gx, gy = 66, 30, 330, 30
for m in range(4):
    s.append(f'<text x="{gx + cw*m + cw/2}" y="{gy - 8}" text-anchor="middle" class="label">column {m}</text>')
for n in range(4):
    yy = gy + (ch + 12) * (3 - n)
    s.append(sub('D', str(n), gx - 22, yy + ch/2 + 3, 15))
    for m in range(4):
        xx = gx + cw * m
        if (m, n) in order:
            s.append(f'<rect x="{xx}" y="{yy}" width="{cw - 4}" height="{ch}" class="cell head-cell"/>')
            s.append(sub('G', str(m), xx + (cw - 4)/2, yy + ch/2 + 3, 14))
        else:
            s.append(f'<rect x="{xx}" y="{yy}" width="{cw - 4}" height="{ch}" class="cell"/>')
            s.append(f'<text x="{xx + (cw - 4)/2}" y="{yy + ch/2 + 5}" text-anchor="middle" class="mrm muted" font-size="14">∅</text>')
s.append('</svg>')
out['diamond'] = ''.join(s)

# ---------------------------------------------------------------- splitting and non-splitting trees
def tree_pos(ox, w, rho, top=40, dy=58):
    d = len(rho)
    idx = int(rho, 2) if rho else 0
    return ox + (idx + 0.5) * w / (2 ** d), top + d * dy

s = ['<svg class="fig" viewBox="0 0 600 272" width="600" role="img" aria-label="Left: an e-splitting tree; at each node, the two successors give different values of Phi_e at some input, and the values of Y select the branch followed by X. Right: a tree avoiding e-splits; all its nodes give compatible outputs">']
# left panel: e-splitting
W, OX = 280, 10
split = {'': ('0', '0', '1'), '0': ('1', '1', '0'), '1': ('1′', '0', '1'),
         '00': ('', '', ''), '01': ('2', '0', '1'), '10': ('', '', ''), '11': ('', '', '')}
path = ['', '0', '01', '011']
strs = [''] + ['0', '1'] + ['00', '01', '10', '11'] + ['010', '011']
for r in strs:
    if r == '':
        continue
    (x1, y1), (x2, y2) = tree_pos(OX, W, r[:-1]), tree_pos(OX, W, r)
    on = r in path
    cls = 'accent-stroke' if on else 'muted-stroke'
    sw = 2.2 if on else 1.1
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{sw}"/>')
for r in strs:
    x, y = tree_pos(OX, W, r)
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4.5" class="node"/>')
for r in ['', '0', '01']:
    x, y = tree_pos(OX, W, r)
    xin, v0, v1 = split[r]
    (xa, ya), (xb, yb) = tree_pos(OX, W, r + '0'), tree_pos(OX, W, r + '1')
    s.append(f'<text x="{(x + xa)/2 - 8:.1f}" y="{(y + ya)/2 + 2}" text-anchor="end" class="mrm" font-size="11">{v0}</text>')
    s.append(f'<text x="{(x + xb)/2 + 8:.1f}" y="{(y + yb)/2 + 2}" text-anchor="start" class="mrm" font-size="11">{v1}</text>')
    s.append(sub('x', xin, x, y - 10, 12))
x, y = tree_pos(OX, W, '011')
s.append(f'<text x="{x:.1f}" y="{y + 22}" text-anchor="middle" class="math" font-size="13">X</text>')
s.append(f'<text x="{OX + W/2}" y="16" text-anchor="middle" class="label">e-splitting, with Y = 0, 0, 1 at the three inputs</text>')
s.append(f'<text x="{OX + W/2}" y="262" text-anchor="middle" class="label">the values of Y choose the branch followed by X</text>')
# right panel: avoiding e-splits
OX2 = 310
outs = {'': '0', '0': '01', '1': '0', '00': '011', '01': '01', '10': '01', '11': '011',
        '000': '0110', '001': '011', '010': '011', '011': '0110', '100': '011', '101': '01', '110': '0110', '111': '011'}
allr = [''] + [format(i, f'0{d}b') for d in (1, 2, 3) for i in range(2 ** d)]
for r in allr:
    if r == '':
        continue
    (x1, y1), (x2, y2) = tree_pos(OX2, W, r[:-1]), tree_pos(OX2, W, r)
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="ink-stroke" stroke-width="1.1"/>')
for r in allr:
    x, y = tree_pos(OX2, W, r)
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4.5" class="node"/>')
    o = outs[r]
    if len(r) < 3:
        s.append(f'<text x="{x + 8:.1f}" y="{y + 4}" class="mrm" font-size="11">{o}</text>')
    else:
        s.append(f'<text x="{x:.1f}" y="{y + 18}" text-anchor="middle" class="mrm" font-size="10">{o}</text>')
s.append(f'<text x="{OX2 + W/2}" y="16" text-anchor="middle" class="label">avoiding e-splits: all outputs are compatible</text>')
s.append(f'<text x="{OX2 + W/2}" y="262" text-anchor="middle" class="label">they are prefixes of one computable sequence</text>')
s.append('</svg>')
out['splitting'] = ''.join(s)

# ---------------------------------------------------------------- the binary tree of strings for an antichain
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The strings sigma_rho for rho of length at most 2, arranged as a binary tree. At level 1, the step for e and the pair (0, 1) extends sigma_0 to a string tau on which Phi_e converges at x, and extends sigma_1 at position x by a bit different from the value">', '<defs><marker id="ds-anti-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs>']
P = {'': (300, 30), '0': (160, 95), '1': (440, 95), '00': (90, 190), '01': (230, 190), '10': (370, 190), '11': (510, 190)}
for r, (x2, y2) in P.items():
    if r == '':
        continue
    x1, y1 = P[r[:-1]]
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="accent-stroke" stroke-width="1.8"/>')
for r, (x, y) in P.items():
    s.append(f'<circle cx="{x}" cy="{y}" r="5" class="node"/>')
    lab = 'ε' if r == '' else r
    s.append(sub('σ', lab, x + 24 if r != '' else x + 22, y + 4, 15))
s.append('<line x1="182" y1="118" x2="415" y2="118" class="ink-stroke" stroke-width="1.1" stroke-dasharray="4 3" marker-end="url(#ds-anti-arrow)"/>')
s.append('<text x="300" y="222" text-anchor="middle" class="label">step for e and the pair (0, 1): σ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">\u00a0is extended so that the computation at x converges to v,</tspan></text>')
s.append('<text x="300" y="238" text-anchor="middle" class="label">and σ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3">\u00a0receives the bit 1 − v at the position x = |σ</tspan><tspan font-size="9" dy="3">1</tspan><tspan dy="-3">| (dashed arrow)</tspan></text>')
s.append('</svg>')
out['antichain'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False)
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
