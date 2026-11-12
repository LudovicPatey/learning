# Generates the inline SVG figures of the course on lowness and first-jump control.
# Usage: python3 scripts/figures/lowness.py out.json
# Paste each figure into the lesson that uses it:
#   jump-sequence       -> forcing-the-jump.md
#   hyperimmune-blocks  -> weak-preservation.md
#   scott-code          -> coded-ideals.md
#   side-grid           -> cjs-theorem.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, index, size=15, cls='math'):
    return (f'<tspan class="{cls}" font-size="{size}">{base}</tspan>'
            f'<tspan class="mrm" font-size="{size - 5}" dy="4">{index}</tspan><tspan dy="-4"> </tspan>')


# ---------------------------------------------------------------- an effective sequence of conditions
steps = [('c₀', 'start'), ('c₁', 'prefix'), ('c₂', 'decide e = 0'), ('c₃', 'dense set D₀'),
         ('c₄', 'prefix'), ('c₅', 'decide e = 1'), ('c₆', 'dense set D₁')]
W, GAP, X0 = 66, 16, 18
s = ['<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="A decreasing sequence of codes of conditions computed by the oracle A; the steps alternate between prefixes of the generic set, decisions of the jump and dense sets; the decisions are recorded as bits">']
s.append('<defs>' + marker('lw-js-arr', 'muted-fill') + '</defs>')
for k, (name, role) in enumerate(steps):
    x = X0 + k * (W + GAP)
    cls = 'head-cell' if role.startswith('decide') else 'cell'
    s.append(f'<rect x="{x}" y="40" width="{W}" height="40" rx="6" class="{cls}"/>')
    s.append(f'<text x="{x + W / 2}" y="65" text-anchor="middle" class="math" font-size="16">{name}</text>')
    s.append(f'<text x="{x + W / 2}" y="100" text-anchor="middle" class="label">{role}</text>')
    if k > 0:
        s.append(f'<line x1="{x - GAP + 2}" y1="60" x2="{x - 2}" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/>')
    if role.startswith('decide'):
        e = role[-1]
        bit = '1' if e == '0' else '0'
        s.append(f'<line x1="{x + W / 2}" y1="108" x2="{x + W / 2}" y2="140" class="accent-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/>')
        s.append(f'<text x="{x + W / 2}" y="158" text-anchor="middle" class="label">bit b = {bit}</text>')
s.append(f'<text x="300" y="24" text-anchor="middle" class="label">each code is computed by A from the previous one</text>')
s.append(f'<text x="300" y="188" text-anchor="middle" class="label">G′(e) = the bit recorded at the step deciding e: so G′ ≤ A</text>')
s.append(f'<text x="300" y="206" text-anchor="middle" class="label muted">c₀ ≥ c₁ ≥ c₂ ≥ ⋯, and G is the member of all of them</text>')
s.append('</svg>')
out['jump-sequence'] = ''.join(s)

# ---------------------------------------------------------------- the blocks of the co-hyperimmune argument
X0, CW, N = 40, 13.5, 40
SIG = 4                      # |sigma|
blocks = [(0, 9, [6, 8]), (9, 19, [14, 17]), (19, 32, [25, 29, 31])]   # (n_k, |mu|, elements of F_k)
outside = [8, 14, 29]        # one element of each block outside A


def bx(n):
    return X0 + n * CW


s = ['<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="Three strings extending sigma followed by blocks of zeros of increasing length; each makes the computation converge, and the positions where it adds elements form a finite set that meets the complement of A; the blocks are pairwise disjoint">']
for n in range(0, N, 4):
    s.append(f'<text x="{bx(n) + CW / 2:.1f}" y="18" text-anchor="middle" class="mrm muted" font-size="10">{n}</text>')
for k, (nk, mu, elems) in enumerate(blocks):
    y = 36 + 46 * k
    s.append(f'<text x="{X0 - 8}" y="{y + 14}" text-anchor="end" class="math" font-size="14">μ<tspan class="mrm" font-size="10" dy="4">{k}</tspan></text>')
    for n in range(mu):
        if n < SIG:
            cls = 'cell head-cell'
        elif n < SIG + nk:
            cls = 'cell'
        else:
            cls = 'cell'
        s.append(f'<rect x="{bx(n):.1f}" y="{y}" width="{CW}" height="20" class="{cls}"/>')
        if n >= SIG + nk and n in elems:
            mark = 'accent-fill' if n in outside else 'ink-fill'
            s.append(f'<circle cx="{bx(n) + CW / 2:.1f}" cy="{y + 10}" r="4" class="{mark}"/>')
    # bracket for the zeros
    if nk > 0:
        s.append(f'<path d="M{bx(SIG):.1f},{y + 26} L{bx(SIG):.1f},{y + 30} L{bx(SIG + nk):.1f},{y + 30} L{bx(SIG + nk):.1f},{y + 26}" class="muted-stroke" stroke-width="1"/>')
        s.append(f'<text x="{(bx(SIG) + bx(SIG + nk)) / 2:.1f}" y="{y + 41}" text-anchor="middle" class="label muted">0 repeated {nk} times</text>')
    s.append(f'<text x="{bx(mu) + 8:.1f}" y="{y + 14}" class="label">Φₑ converges</text>')
y = 180
s.append(f'<rect x="{X0}" y="{y}" width="{CW}" height="14" class="cell head-cell"/>')
s.append(f'<text x="{X0 + CW + 6}" y="{y + 11}" class="label">σ</text>')
s.append(f'<circle cx="{X0 + 60}" cy="{y + 7}" r="4" class="ink-fill"/>')
s.append(f'<text x="{X0 + 70}" y="{y + 11}" class="label">element added, in A</text>')
s.append(f'<circle cx="{X0 + 240}" cy="{y + 7}" r="4" class="accent-fill"/>')
s.append(f'<text x="{X0 + 250}" y="{y + 11}" class="label">element added, not in A</text>')
s.append(f'<text x="300" y="222" text-anchor="middle" class="label">each block F_k of added elements meets the complement of A, and the blocks are disjoint</text>')
s.append('</svg>')
out['hyperimmune-blocks'] = ''.join(s)

# ---------------------------------------------------------------- the columns of a code of a Scott ideal


def pair(a, b):
    return (a + b) * (a + b + 1) // 2 + b


def unpair(m):
    for a in range(m + 1):
        for b in range(m + 1):
            if pair(a, b) == m:
                return a, b


cols = []
for n in range(10):
    if n == 0:
        cols.append(('X', 'parameter'))
    elif n % 3 == 1:
        a, b = unpair((n - 1) // 3)
        cols.append((f'Z{a} ⊕ Z{b}', 'join'))
    elif n % 3 == 2:
        a, e = unpair((n - 2) // 3)
        cols.append((f'Φ{e}(Z{a})', 'reduction'))
    else:
        a = n // 3 - 1
        cols.append((f'DNC₂ over Z{a}', 'PA step'))

SUBS = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
s = ['<svg class="fig" viewBox="0 0 600 256" width="600" role="img" aria-label="The first ten columns of a member of the Scott class: column 0 is the parameter X; the other columns are, in turn, a join of two earlier columns, a set computed from an earlier column, and a function diagonally non-computable relative to an earlier column">']
s.append('<defs>' + marker('lw-sc-arr', 'muted-fill') + '</defs>')
X0, CW, Y0 = 30, 54, 40
for n, (what, kind) in enumerate(cols):
    x = X0 + n * CW
    cls = 'cell head-cell' if kind == 'PA step' else 'cell'
    s.append(f'<rect x="{x + 4}" y="{Y0}" width="{CW - 8}" height="120" rx="4" class="{cls}"/>')
    s.append(f'<text x="{x + CW / 2}" y="{Y0 - 10}" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">{n}</tspan></text>')
    lines = what.translate(SUBS).replace('Φ', 'Φ').split(' ')
    for j, w in enumerate(lines[:3]):
        s.append(f'<text x="{x + CW / 2}" y="{Y0 + 40 + 16 * j}" text-anchor="middle" class="label">{w}</text>')
    s.append(f'<text x="{x + CW / 2}" y="{Y0 + 150}" text-anchor="middle" class="label muted">{kind.split(" ")[0]}</text>')
s.append(f'<text x="300" y="{Y0 + 178}" text-anchor="middle" class="label">column 3⟨a, b⟩ + 1: join of columns a and b;  column 3⟨a, e⟩ + 2: Φₑ applied to column a;</text>')
s.append(f'<text x="300" y="{Y0 + 196}" text-anchor="middle" class="label">column 3a + 3: a {{0,1}}-valued function DNC relative to column a (Cantor pairing ⟨·,·⟩)</text>')
s.append('</svg>')
out['scott-code'] = ''.join(s)

# ---------------------------------------------------------------- the grid of sides in the CJS construction
R, C = 6, 9
side = {}
for e0 in range(R):
    for e1 in range(C):
        side[(e0, e1)] = 0 if (3 * e0 + e1 * e1 + 3 * e0 * e1) % 3 == 0 else 1
for e1 in range(C):
    side[(2, e1)] = 1                # row e0 = 2: always side 1
X0, Y0, CS = 150, 40, 30
s = ['<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="A table of the sides on which the pairs of indices are decided; the row of the index 2 contains only the side 1, so every index of side 1 is decided on side 1">']
s.append(f'<text x="{X0 + C * CS / 2}" y="{Y0 - 22}" text-anchor="middle" class="label">index e₁ of side 1</text>')
s.append(f'<text x="{X0 - 46}" y="{Y0 + R * CS / 2}" text-anchor="middle" class="label" transform="rotate(-90 {X0 - 46} {Y0 + R * CS / 2})">index e₀ of side 0</text>')
for e1 in range(C):
    s.append(f'<text x="{X0 + e1 * CS + CS / 2}" y="{Y0 - 6}" text-anchor="middle" class="mrm muted" font-size="11">{e1}</text>')
for e0 in range(R):
    s.append(f'<text x="{X0 - 12}" y="{Y0 + e0 * CS + CS / 2 + 4}" text-anchor="middle" class="mrm muted" font-size="11">{e0}</text>')
    for e1 in range(C):
        v = side[(e0, e1)]
        cls = 'cell head-cell' if v == 1 else 'cell'
        s.append(f'<rect x="{X0 + e1 * CS}" y="{Y0 + e0 * CS}" width="{CS}" height="{CS}" class="{cls}"/>')
        s.append(f'<text x="{X0 + e1 * CS + CS / 2}" y="{Y0 + e0 * CS + CS / 2 + 4}" text-anchor="middle" class="mrm" font-size="12">{v}</text>')
s.append(f'<rect x="{X0 - 3}" y="{Y0 + 2 * CS - 3}" width="{C * CS + 6}" height="{CS + 6}" fill="none" class="accent-stroke" stroke-width="2"/>')
s.append(f'<text x="{X0 + C * CS + 12}" y="{Y0 + 2 * CS + CS / 2 + 4}" class="label">only side 1</text>')
s.append(f'<text x="300" y="{Y0 + R * CS + 30}" text-anchor="middle" class="label">entry f(e₀, e₁): the side on which the pair is decided</text>')
s.append(f'<text x="300" y="{Y0 + R * CS + 48}" text-anchor="middle" class="label">a row with only 1s decides every e₁ on side 1; if there is none, every e₀ is decided on side 0</text>')
s.append('</svg>')
out['side-grid'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
