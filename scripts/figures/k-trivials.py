# Generates the inline SVG figures of the course on K-trivial sets.
# Usage: python3 scripts/figures/k-trivials.py out.json
# Paste each figure into the lesson that uses it:
#   bounded-width-tree   -> k-trivial-sets.md
#   standard-cost        -> cost-functions.md
#   hungry-sets          -> lowness.md
#   amplification        -> ktrivial-lowness.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def mtext(txt, x, y, size=14, anchor='start', cls='math'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{txt}</text>'


def sub(base, s, x, y, size=14, anchor='start'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size * 0.7)}" dy="4">{s}</tspan></text>')


def dyadic_center(s, left, right):
    d = len(s)
    idx = int(s, 2) if s else 0
    return left + (idx + 0.5) * (right - left) / (2 ** d)


def interval(s, left, right):
    d = len(s)
    idx = int(s, 2) if s else 0
    w = (right - left) / (2 ** d)
    return left + idx * w, left + (idx + 1) * w


# ---------------------------------------------------------------- the tree T_b has bounded width
# Two infinite paths, 0010110... and 0011010..., which separate at level 4; the branch through 1
# dies at level 5.  Every level has at most three nodes.
levels = [
    [''],
    ['0', '1'],
    ['00', '10'],
    ['001', '100'],
    ['0010', '0011', '1001'],
    ['00101', '00110', '10010'],
    ['001011', '001101'],
    ['0010110', '0011010'],
]
paths = ['0010110', '0011010']
TL, TR = 20, 430
dy = 34
top = 22
s = ['<svg class="fig" viewBox="0 0 600 320" width="600" role="img" '
     'aria-label="A tree with at most three nodes at each level, two infinite paths that separate at level 4, '
     'and a branch through 1 that dies at level 5">']
for n in range(1, len(levels)):
    for v in levels[n]:
        p = v[:-1]
        x1, y1 = dyadic_center(p, TL, TR), top + (n - 1) * dy
        x2, y2 = dyadic_center(v, TL, TR), top + n * dy
        on = any(q.startswith(v) for q in paths)
        cls = 'accent-stroke' if on else 'ink-stroke'
        s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{2 if on else 1.1}"/>')
for n, lev in enumerate(levels):
    for v in lev:
        x, y = dyadic_center(v, TL, TR), top + n * dy
        on = any(q.startswith(v) for q in paths)
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="{"accent-fill" if on else "ink-fill"}"/>')
        has_child = n + 1 < len(levels) and any(w[:-1] == v for w in levels[n + 1])
        if not has_child and n + 1 < len(levels):
            s.append(f'<line x1="{x - 7:.1f}" y1="{y + 9}" x2="{x + 7:.1f}" y2="{y + 9}" class="ink-stroke" stroke-width="1.4"/>')
for q in paths:
    x = dyadic_center(q, TL, TR)
    s.append(f'<text x="{x:.1f}" y="{top + (len(levels) - 1) * dy + 22}" text-anchor="middle" class="mrm" font-size="13">⋮</text>')
for n, lev in enumerate(levels):
    y = top + n * dy
    s.append(f'<text x="470" y="{y + 4}" class="label">level {n}: {len(lev)} node{"s" if len(lev) > 1 else ""}</text>')
ysep = top + 4 * dy
s.append(f'<line x1="{TL}" y1="{ysep - 17}" x2="590" y2="{ysep - 17}" class="muted-stroke" stroke-width="1" stroke-dasharray="4 3"/>')
s.append(f'<text x="{TL}" y="{top + (len(levels) - 1) * dy + 44}" class="label">'
         'accent: the two infinite paths; bars: nodes without successors</text>')
s.append('</svg>')
out['bounded-width-tree'] = ''.join(s)

# ---------------------------------------------------------------- the standard cost function
# Stage s + 1 = 12; the approximation changes at position x = 4.  The weights 2^{-K_s(n)} of the
# lengths n = 1, ..., 12 are drawn as bars; those with n > x form c_K(x, s + 1).
As = '010011010010'
As1 = '010001110011'
x = min(i for i in range(len(As)) if As[i] != As1[i])
Kvals = [2, 3, 4, 3, 5, 4, 6, 5, 6, 7, 6, 7]  # K_{s+1}(n) for n = 1, ..., 12 (illustrative values)
CL, CW = 110, 38
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" '
     'aria-label="Two consecutive approximations of A that first differ at position 4; below, bars of height '
     'proportional to 2 to the minus K_s of n for the lengths n from 1 to 12, the bars for n greater than 4 being '
     'highlighted: their sum is the cost">']
for row, (name, st) in enumerate([('s', As), ('s+1', As1)]):
    y = 20 + row * 32
    s.append(sub('A', name, 20, y + 17, 15))
    for i, c in enumerate(st):
        cls = 'head-cell' if (row == 1 and As[i] != As1[i]) else 'cell'
        s.append(f'<rect x="{CL + i * CW}" y="{y}" width="{CW}" height="24" class="{cls}"/>')
        s.append(mtext(c, CL + i * CW + CW / 2, y + 17, 13, 'middle', 'mrm'))
for i in range(len(As)):
    s.append(f'<text x="{CL + i * CW + CW / 2:.1f}" y="96" text-anchor="middle" class="label">{i}</text>')
s.append(f'<text x="20" y="96" class="label">position</text>')
base = 250
for n in range(1, len(As) + 1):
    h = 140 * 2 ** (-(Kvals[n - 1] - 2))
    xb = CL + n * CW - 7
    cls = 'soft-fill' if n <= x else 'accent-fill'
    s.append(f'<rect x="{xb:.1f}" y="{base - h:.1f}" width="14" height="{h:.1f}" class="{cls}"/>')
    s.append(f'<text x="{xb + 7:.1f}" y="{base + 16}" text-anchor="middle" class="label">{n}</text>')
s.append(f'<line x1="{CL}" y1="{base}" x2="{CL + len(As) * CW + 10}" y2="{base}" class="axis"/>')
s.append(f'<text x="20" y="{base + 16}" class="label">length n</text>')
s.append(f'<text x="20" y="{base - 90}" class="label">weight</text>')
s.append('<text x="20" y="' + str(base - 70) + '" class="math" font-size="13">2<tspan class="mrm" font-size="9" dy="-6">−K</tspan>'
         '<tspan class="mrm" font-size="7" dy="3">s+1</tspan><tspan class="mrm" font-size="9" dy="-3">(n)</tspan></text>')
s.append(f'<line x1="{CL + x * CW:.1f}" y1="84" x2="{CL + x * CW:.1f}" y2="{base}" class="muted-stroke" stroke-width="1" stroke-dasharray="4 3"/>')
s.append(f'<text x="{CL + x * CW + 6:.1f}" y="120" class="label">prefixes of length n &gt; {x} change</text>')
s.append(f'<text x="{CL}" y="{base + 40}" class="label">highlighted: the lengths n with x &lt; n ≤ s + 1; '
         f'the sum of their weights is the cost</text>')
s.append('</svg>')
out['standard-cost'] = ''.join(s)

# ---------------------------------------------------------------- hungry sets
# Cantor space drawn as [0, 1], cut into cylinders of length 5.  Three hungry sets of true
# computations (rho a prefix of A) and one of a computation with rho not a prefix of A.
HL, HR = 150, 520
rows = [
    ('true, target 2⁻³', ['00000', '00001', '00010', '00011'], 'full', True),
    ('true, target 2⁻³', ['01000', '01001'], 'half full', True),
    ('true, target 2⁻⁴', ['10100', '10101'], 'full', True),
    ('false, target 2⁻³', ['11000', '11001', '11010'], '3/4 full', False),
]
s = ['<svg class="fig" viewBox="0 0 600 260" width="600" role="img" '
     'aria-label="Cantor space as an interval; four hungry sets made of disjoint cylinders of length 5, three of them '
     'attached to computations with an oracle prefix of A and one not; the union of the first three is the class V_d, '
     'which does not contain the sequence Z">']
s.append(mtext('0', HL, 16, 12, 'middle', 'mrm'))
s.append(mtext('1', HR, 16, 12, 'middle', 'mrm'))
for i, (lab, cyl, target, true) in enumerate(rows):
    y = 26 + i * 34
    s.append(f'<text x="10" y="{y + 15}" class="label">{lab}</text>')
    s.append(f'<rect x="{HL}" y="{y}" width="{HR - HL}" height="22" class="cell"/>')
    for c in cyl:
        a, b = interval(c, HL, HR)
        s.append(f'<rect x="{a + 1:.1f}" y="{y + 1}" width="{b - a - 2:.1f}" height="20" class="{"head-cell" if true else "soft-fill"}"/>')
    s.append(f'<text x="{HR + 6}" y="{y + 15}" class="label">{target}</text>')
y = 26 + len(rows) * 34 + 10
s.append(sub('V', 'd', 10, y + 16, 15))
s.append(f'<rect x="{HL}" y="{y}" width="{HR - HL}" height="22" class="cell"/>')
for lab, cyl, target, true in rows:
    if true:
        for c in cyl:
            a, b = interval(c, HL, HR)
            s.append(f'<rect x="{a + 1:.1f}" y="{y + 1}" width="{b - a - 2:.1f}" height="20" class="head-cell"/>')
zx = interval('01110', HL, HR)[0] + 5
s.append(f'<line x1="{zx:.1f}" y1="{y - 4}" x2="{zx:.1f}" y2="{y + 30}" class="accent-stroke" stroke-width="2"/>')
s.append(mtext('Z', zx, y + 46, 15, 'middle'))
s.append(f'<text x="{HL}" y="{y + 66}" class="label">bottom row: the union of the hungry sets of true computations; Z avoids it</text>')
s.append('</svg>')
out['hungry-sets'] = ''.join(s)

# ---------------------------------------------------------------- amplification
# k = 4 versions of A_s restricted to n = 14 at the stages s_0 < s_1 < s_2 < s_3; the versions
# differ below the use bound gamma = 6, since they compute different values of B on x_0, ..., x_3.
versions = [
    '00101101001101',
    '01100101001101',
    '01101100011101',
    '11001010011100',
]
VL, VW = 200, 26
G = 6
s = ['<svg class="fig" viewBox="0 0 600 236" width="600" role="img" '
     'aria-label="Four versions of the prefix of length n of the approximation of A, one per stage s_i; they differ '
     'in the first gamma positions, since they compute different values of B on the followers; each has a description '
     'of length at most 2j">']
s.append(f'<text x="{VL + G * VW / 2:.0f}" y="10" text-anchor="middle" class="label">positions below the use bound</text>')
for i, v in enumerate(versions):
    y = 16 + i * 34
    s.append(sub('A', f's{chr(0x2080 + i)}', 10, y + 17, 14))
    s.append(mtext('↾ n', 40, y + 17, 14, 'start', 'mrm'))
    s.append(f'<text x="78" y="{y + 17}" class="label">{i} follower{"s" if i != 1 else ""} in B</text>')
    for p, c in enumerate(v):
        s.append(f'<rect x="{VL + p * VW}" y="{y}" width="{VW}" height="24" class="{"head-cell" if p < G else "cell"}"/>')
        s.append(mtext(c, VL + p * VW + VW / 2, y + 17, 13, 'middle', 'mrm'))
y = 16 + len(versions) * 34 + 14
s.append(f'<text x="{VL}" y="{y}" class="label">0</text>')
s.append(f'<text x="{VL + G * VW}" y="{y}" text-anchor="middle" class="label">γ</text>')
s.append(f'<text x="{VL + len(versions[0]) * VW}" y="{y}" text-anchor="middle" class="label">n</text>')
s.append(f'<text x="{VL}" y="{y + 26}" class="label">pairwise distinct strings of length n, each of complexity at most 2j:</text>')
s.append(f'<text x="{VL}" y="{y + 42}" class="label">together they use at least k · 2⁻²ʲ of the domain of U</text>')
s.append('</svg>')
out['amplification'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
