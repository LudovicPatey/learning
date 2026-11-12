# Generates the inline SVG figures of the course on effective forcing.
# Usage: python3 scripts/figures/effective-forcing.py out.json
# Paste each figure into the lesson that uses it:
#   four-notions        -> notions-of-forcing.md
#   escape-tree         -> sacks-forcing.md
#   question-density    -> forcing-question.md
# The output is deterministic: every loop runs over sorted or ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def strings(n):
    return [format(i, f'0{n}b') for i in range(2 ** n)] if n else ['']


# ---------------------------------------------------------------- four notions of forcing
# Each class is drawn through its strings of length DEPTH that are prefixes of members,
# as dyadic intervals of Cantor space ordered from 0 (left) to 1 (right).
DEPTH = 6


def cohen(prefix):
    return lambda s: s.startswith(prefix) or prefix.startswith(s)


def no11(s):
    return '11' not in s


def js_c(s):
    return no11(s)


def js_d(s):
    return no11(s) and (len(s) < 2 or s[1] == '0')


def doubled(s):
    # the f-tree T(rho) = rho with every bit doubled: X(2i) = X(2i+1)
    return all(s[2 * i] == s[2 * i + 1] for i in range(len(s) // 2))


def sacks_c(s):
    return doubled(s)


def sacks_d(s):
    return doubled(s) and s.startswith('00')


def mathias_c(s):
    # (empty string, even numbers): ones only at even positions
    return all(s[i] == '0' or i % 2 == 0 for i in range(len(s)))


def mathias_d(s):
    # ("1", multiples of 4 that are at least 4)
    return s.startswith('1') and all(s[i] == '0' or (i % 4 == 0 and i >= 4) for i in range(1, len(s)))


rows = [
    ('Cohen', 'σ = 01', 'τ = 0110', cohen('01'), cohen('0110')),
    ('Jockusch–Soare', 'no two consecutive 1s', 'and X(1) = 0', js_c, js_d),
    ('computable Sacks', 'T(ρ): bits of ρ doubled', 'full subtree above T(0)', sacks_c, sacks_d),
    ('computable Mathias', '(ε, even numbers)', '(1, multiples of 4 from 4)', mathias_c, mathias_d),
]
L, R = 240, 580
W = (R - L) / 2 ** DEPTH
s = ['<svg class="fig" viewBox="0 0 600 330" width="600" role="img" aria-label="For four notions of forcing, a condition and an extension, each drawn as the set of strings of length six that are prefixes of its members">']
y = 22
s.append(f'<text x="{L}" y="{y - 8}" class="mrm muted" font-size="11">0</text>')
s.append(f'<text x="{R}" y="{y - 8}" text-anchor="end" class="mrm muted" font-size="11">1</text>')
for name, cdesc, ddesc, fc, fd in rows:
    s.append(f'<text x="10" y="{y + 22}" class="label">{name}</text>')
    for k, (f, desc) in enumerate([(fc, cdesc), (fd, ddesc)]):
        yy = y + k * 30
        s.append(f'<line x1="{L}" y1="{yy + 7}" x2="{R}" y2="{yy + 7}" class="axis"/>')
        cls = 'cell' if k == 0 else 'cell head-cell'
        run = None
        cells = [f(t) for t in strings(DEPTH)]
        cells.append(False)
        for i, inside in enumerate(cells):
            if inside and run is None:
                run = i
            if not inside and run is not None:
                s.append(f'<rect x="{L + run * W:.1f}" y="{yy}" width="{(i - run) * W:.1f}" height="14" class="{cls}"/>')
                run = None
        lab = '[c]' if k == 0 else '[d]'
        s.append(f'<text x="{L - 8}" y="{yy + 12}" text-anchor="end" class="mrm" font-size="12">{lab}</text>')
    s.append(f'<text x="10" y="{y + 38}" class="label" font-size="10">c: {cdesc}</text>')
    s.append(f'<text x="10" y="{y + 52}" class="label" font-size="10">d: {ddesc}</text>')
    y += 76
s.append('</svg>')
out['four-notions'] = ''.join(s)

# ---------------------------------------------------------------- the escape tree of the Sacks argument
# T is the identity tree, drawn to depth 4. R(rho) = T(d(rho)), d inserts a 0 after every bit.
# The escape node of R(rho) is T(d(rho) 0 1).
D = 4
LX, RX, TOP, STEP = 30, 570, 26, 52


def pos(t):
    idx = int(t, 2) if t else 0
    return LX + (idx + 0.5) * (RX - LX) / 2 ** len(t), TOP + STEP * len(t)


def dmap(rho):
    return ''.join(b + '0' for b in rho)


rnodes = {dmap(r) for k in range(3) for r in strings(k)}
redges = set()
for k in range(1, 3):
    for r in strings(k):
        a, b = dmap(r[:-1]), dmap(r)
        for j in range(len(a) + 1, len(b) + 1):
            redges.add(b[:j])
escapes = [dmap(r) + '01' for r in strings(1)] + [dmap('') + '01']
escapes = sorted(set(e for e in escapes if len(e) <= D))
s = ['<svg class="fig" viewBox="0 0 600 316" width="600" role="img" aria-label="A binary tree of depth four; the nodes of a subtree R are highlighted, and for each node of R a node of the tree whose cylinder avoids the paths of R">']
for t in [x for k in range(1, D + 1) for x in strings(k)]:
    (x1, y1), (x2, y2) = pos(t[:-1]), pos(t)
    if t in redges:
        s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="accent-stroke" stroke-width="2.4"/>')
    else:
        s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="muted-stroke" stroke-width="1"/>')
for t in [x for k in range(D + 1) for x in strings(k)]:
    x, yy = pos(t)
    if t in rnodes:
        s.append(f'<circle cx="{x:.1f}" cy="{yy}" r="5.5" class="accent-fill"/>')
    elif t in escapes:
        s.append(f'<rect x="{x - 5:.1f}" y="{yy - 5}" width="10" height="10" class="node"/>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{yy}" r="2.5" class="muted-fill"/>')
labels = {'': 'R(ε)', '00': 'R(0)', '10': 'R(1)', '01': 'τ_ε', '0001': 'τ₀', '1001': 'τ₁'}
for t in sorted(labels):
    x, yy = pos(t)
    lab = labels[t]
    if lab.startswith('τ'):
        base, sub_ = 'τ', lab[1:].replace('_', '')
        s.append(f'<text x="{x:.1f}" y="{yy + 22}" text-anchor="middle" class="math" font-size="14">{base}'
                 f'<tspan class="mrm" font-size="9" dy="4">{sub_}</tspan></text>')
    else:
        s.append(f'<text x="{x + 9:.1f}" y="{yy - 7}" class="math" font-size="13">R<tspan class="mrm">{lab[1:]}</tspan></text>')
s.append(f'<circle cx="40" cy="296" r="5" class="accent-fill"/><text x="52" y="300" class="label">nodes R(ρ) = T(ρ(0) 0 ρ(1) 0 …), |ρ| ≤ 2</text>')
s.append(f'<rect x="335" y="291" width="10" height="10" class="node"/><text x="352" y="300" class="label">τ<tspan font-size="9" dy="3">ρ</tspan><tspan dy="-3"> = T(… 0 1): no path of R extends it</tspan></text>')
s.append('</svg>')
out['escape-tree'] = ''.join(s)

# ---------------------------------------------------------------- the density argument of the forcing question
s = ['<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="The density argument: the set U of numbers m such that c answers yes to the question about phi(m) differs from A; an element of the difference gives an extension forcing phi(m) with m outside A, or not phi(m) with m in A">']
s.append('<defs>' + marker('ef-arr') + '</defs>')


def box(x, y, w, h, lines, cls='state'):
    r = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>']
    for i, ln in enumerate(lines):
        r.append(f'<text x="{x + w / 2}" y="{y + 20 + 16 * i}" text-anchor="middle" class="label">{ln}</text>')
    return ''.join(r)


s.append(box(200, 10, 200, 56, ['condition c', 'U = { m : c ?⊢ φ(m) } is Σ⁰ₙ']))
s.append(box(20, 128, 240, 56, ['m ∈ U, m ∉ A', 'd ≤ c with d ⊩ φ(m)']))
s.append(box(340, 128, 240, 56, ['m ∈ A, m ∉ U', 'd ≤ c with d ⊩ ¬φ(m)']))
s.append('<line x1="270" y1="68" x2="160" y2="124" class="ink-stroke" stroke-width="1.2" marker-end="url(#ef-arr)"/>')
s.append('<line x1="330" y1="68" x2="440" y2="124" class="ink-stroke" stroke-width="1.2" marker-end="url(#ef-arr)"/>')
s.append('<text x="300" y="104" text-anchor="middle" class="label">A is not Σ⁰ₙ, so U ≠ A</text>')
s.append('<text x="300" y="206" text-anchor="middle" class="label">either way, φ does not define A from a generic set below d</text>')
s.append('</svg>')
out['question-density'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
