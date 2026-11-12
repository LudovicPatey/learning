# Generates the inline SVG figures of the course on Pi^0_1 classes.
# Usage: python3 scripts/figures/pi01-classes.py out.json
# Paste each figure into the lesson that uses it:
#   binary-tree, compactness          -> trees-and-classes.md
#   perfect-splitting                 -> computable-members.md
#   nested-classes                    -> basis-theorems.md
#   pa-characterizations              -> pa-degrees.md
#   jump-tree                         -> finitely-branching-trees.md
# The output is deterministic: every loop runs over sorted or ordered data.
import json, math, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, s, x, y, size=16, anchor='middle', cls='math'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')


def dyadic(s, left=20, right=580):
    """Center of the dyadic interval of the string s inside [left, right]."""
    d = len(s)
    idx = int(s, 2) if s else 0
    return left + (idx + 0.5) * (right - left) / (2 ** d)


def interval(s, left=20, right=580):
    d = len(s)
    idx = int(s, 2) if s else 0
    w = (right - left) / (2 ** d)
    return left + idx * w, left + (idx + 1) * w


def gen(prefix, maxd):
    res = [prefix]
    if len(prefix) < maxd:
        res += gen(prefix + '0', maxd) + gen(prefix + '1', maxd)
    return res


# ---------------------------------------------------------------- a binary tree with dead branches
depth = 5
tree = {''}
alive = set()
for p in ['000', '001', '100', '101', '1110']:
    for s_ in gen(p, depth):
        tree.add(s_)
        alive.add(s_)
    for k in range(len(p)):
        tree.add(p[:k])
        alive.add(p[:k])
dead = {'01', '010', '0101', '110', '1100', '1101', '11001', '1111', '11110'}
tree |= dead
path = '00101'


def pos(s):
    return dyadic(s), 22 + len(s) * 46


s = ['<svg class="fig" viewBox="0 0 600 306" width="600" role="img" aria-label="A binary tree: some branches die out, the others extend to infinite paths; one path is highlighted">']
shown = sorted((n for n in tree if len(n) <= 4 or n.startswith(path[:4])), key=lambda n: (len(n), n))
for n in shown:
    if n == '':
        continue
    (x1, y1), (x2, y2) = pos(n[:-1]), pos(n)
    on_path = path.startswith(n)
    cls = 'accent-stroke' if on_path else ('muted-stroke' if n in dead else 'ink-stroke')
    dash = ' stroke-dasharray="3 3"' if n in dead else ''
    sw = '2.2' if on_path else '1.2'
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{sw}"{dash}/>')
for n in shown:
    x, y = pos(n)
    if n in dead:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.5" class="muted-fill"/>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="{"accent-fill" if path.startswith(n) else "ink-fill"}"/>')
for n in shown:
    if len(n) == 4 and n not in dead and not n.startswith(path[:4]):
        x, y = pos(n)
        s.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm muted" font-size="12">⋮</text>')
x, y = pos(path)
s.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm" font-size="12">⋮</text>')
s.append(f'<text x="{x + 14:.1f}" y="{y + 22}" class="label">a path X</text>')
s.append(f'<text x="{pos("")[0] + 10:.1f}" y="{pos("")[1] - 4}" class="mrm" font-size="13">ε</text>')
s.append('<line x1="24" y1="296" x2="44" y2="296" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="300" class="label">a finite branch: no infinite extension</text>')
s.append('<line x1="300" y1="296" x2="320" y2="296" class="accent-stroke" stroke-width="2.2"/><text x="326" y="300" class="label">initial segments of an infinite path</text>')
s.append('</svg>')
out['binary-tree'] = ''.join(s)

# ---------------------------------------------------------------- compactness: a finite cover
W = ['1', '00', '011', '0100', '0101']
T = sorted({w[:k] for w in W for k in range(len(w))}, key=lambda n: (len(n), n))  # strings with no prefix in W
L, R = 20, 580


def cpos(s_):
    return dyadic(s_, L, R), 24 + len(s_) * 40


s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The strings without prefix in W form a finite tree; the cylinders of the strings of W cover Cantor space">']
for n in T + W:
    if n == '':
        continue
    (x1, y1), (x2, y2) = cpos(n[:-1]), cpos(n)
    cls = 'accent-stroke' if n in W else 'ink-stroke'
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="1.4"/>')
bar_y = 210
for w in W:
    x, y = cpos(w)
    s.append(f'<line x1="{x:.1f}" y1="{y + 6}" x2="{x:.1f}" y2="{bar_y - 2}" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/>')
for n in T:
    x, y = cpos(n)
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="ink-fill"/>')
for w in W:
    x, y = cpos(w)
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="5" class="node"/>')
    if w[-1] == '0':
        s.append(f'<text x="{x - 9:.1f}" y="{y - 5}" text-anchor="end" class="mrm" font-size="12">{w}</text>')
    else:
        s.append(f'<text x="{x + 9:.1f}" y="{y - 5}" class="mrm" font-size="12">{w}</text>')
s.append(f'<text x="{cpos("")[0] + 9:.1f}" y="{cpos("")[1] - 6}" class="mrm" font-size="13">ε</text>')
for w in sorted(W):
    a, b = interval(w, L, R)
    s.append(f'<rect x="{a + 1:.1f}" y="{bar_y}" width="{b - a - 2:.1f}" height="22" class="cell head-cell"/>')
    s.append(f'<text x="{(a + b) / 2:.1f}" y="{bar_y + 15}" text-anchor="middle" class="mrm" font-size="11">[{w}]</text>')
s.append(f'<text x="{L}" y="{bar_y + 46}" class="label">Cantor space, ordered from left (0) to right (1): the cylinders [σ], σ ∈ W, cover it</text>')
s.append(f'<circle cx="{L + 4}" cy="{bar_y + 66}" r="4" class="ink-fill"/><text x="{L + 14}" y="{bar_y + 70}" class="label">strings with no prefix in W: the finite tree T</text>')
s.append(f'<circle cx="{L + 324}" cy="{bar_y + 66}" r="5" class="node"/><text x="{L + 334}" y="{bar_y + 70}" class="label">strings of W</text>')
s.append('</svg>')
out['compactness'] = ''.join(s)

# ---------------------------------------------------------------- perfect splitting: the strings sigma_rho
split = {'': '', '0': '00', '1': '011', '00': '000', '01': '0011', '10': '01100', '11': '0111'}
D = 6


def ppos(s_):
    return dyadic(s_, 20, 580), 24 + len(s_) * 42


s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Strings sigma_rho: each one has two incompatible extensions sigma_rho0 and sigma_rho1 in the tree">']
edges = set()
for rho, sig in split.items():
    for k in range(1, len(sig) + 1):
        edges.add(sig[:k])
for n in sorted(edges, key=lambda n: (len(n), n)):
    (x1, y1), (x2, y2) = ppos(n[:-1]), ppos(n)
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="ink-stroke" stroke-width="1.3"/>')
# below the second level, the construction continues
for rho in ['00', '01', '10', '11']:
    x, y = ppos(split[rho])
    for d in (-1, 1):
        s.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x + d * 7:.1f}" y2="{y + 22}" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/>')
    s.append(f'<text x="{x:.1f}" y="{y + 40}" text-anchor="middle" class="mrm muted" font-size="12">⋮</text>')
named = {split[r] for r in split}
for n in sorted(edges | {''}, key=lambda n: (len(n), n)):
    if n in named:
        continue
    x, y = ppos(n)
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="2.5" class="ink-fill"/>')
for rho in sorted(split, key=lambda r: (len(r), r)):
    x, y = ppos(split[rho])
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="5" class="accent-fill"/>')
    lab = 'ε' if rho == '' else rho
    anchor = 'end' if rho in ('0', '00', '10') else 'start'
    dx = -9 if anchor == 'end' else 9
    s.append(sub('σ', lab, f'{x + dx:.1f}', y + 4, 15, anchor))
s.append('<circle cx="406" cy="70" r="5" class="accent-fill"/><text x="418" y="74" class="label">the strings σ<tspan font-size="9" dy="3">ρ</tspan></text>')
s.append('<circle cx="406" cy="92" r="2.5" class="ink-fill"/><text x="418" y="96" class="label">other nodes of T</text>')
s.append('</svg>')
out['perfect-splitting'] = ''.join(s)

# ---------------------------------------------------------------- nested Pi^0_1 classes (low basis theorem)
L, R = 60, 330
rows = [
    ('0', [(0.02, 0.30), (0.38, 0.62), (0.70, 0.98)], 'the given class'),
    ('1', [(0.04, 0.27), (0.72, 0.80), (0.85, 0.97)], 'step 0: Q₀ ≠ ∅, so P₁ = Q₀, J(0) = 0'),
    ('2', [(0.04, 0.27), (0.72, 0.80), (0.85, 0.97)], 'step 1: Q₁ = ∅, so P₂ = P₁, J(1) = 1'),
    ('3', [(0.10, 0.22), (0.87, 0.95)], 'step 2: Q₂ ≠ ∅, so P₃ = Q₂, J(2) = 0'),
]
s = ['<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="A decreasing sequence of classes P0, P1, P2, P3 drawn as unions of intervals of Cantor space, with the decision taken at each step">']
for i, (k, ivs, note) in enumerate(rows):
    y = 20 + i * 46
    s.append(f'<line x1="{L}" y1="{y + 9}" x2="{R}" y2="{y + 9}" class="axis"/>')
    for a, b in ivs:
        xa, xb = L + a * (R - L), L + b * (R - L)
        s.append(f'<rect x="{xa:.1f}" y="{y}" width="{xb - xa:.1f}" height="18" class="cell head-cell"/>')
    s.append(sub('P', k, 20, y + 14, 16))
    s.append(f'<text x="{R + 18}" y="{y + 14}" class="label">{note}</text>')
y = 20 + 4 * 46
s.append(f'<text x="{(L + R) / 2}" y="{y - 6}" text-anchor="middle" class="mrm muted" font-size="13">⋮</text>')
xX = L + 0.91 * (R - L)
s.append(f'<line x1="{L}" y1="{y + 9}" x2="{R}" y2="{y + 9}" class="axis"/>')
s.append(f'<circle cx="{xX:.1f}" cy="{y + 9}" r="4.5" class="accent-fill"/>')
s.append(f'<text x="{xX - 10:.1f}" y="{y + 14}" text-anchor="end" class="math" font-size="15">X</text>')
s.append(f'<text x="{R + 18}" y="{y + 14}" class="label">a member of every Pₑ: X′(e) = J(e) for all e</text>')
s.append('</svg>')
out['nested-classes'] = ''.join(s)

# ---------------------------------------------------------------- PA degrees: the characterizations
boxes = {
    'dnc': (20, 20, 'X computes a member of DNC₂', '(X is PA)'),
    'sep': (350, 20, 'X computes a separating set', 'for all disjoint c.e. A, B'),
    'pi01': (350, 150, 'X computes a member of every', 'non-empty Π⁰₁ class'),
    'pa': (20, 150, 'X computes a complete consistent', 'extension of Peano arithmetic'),
}
BW, BH = 230, 54
s = ['<svg class="fig" viewBox="0 0 600 226" width="600" role="img" aria-label="Four equivalent properties of a set X, with the implications proved in the lesson">',
     '<defs>' + marker('ah-pa') + '</defs>']
for key in ['dnc', 'sep', 'pi01', 'pa']:
    x, y, t1, t2 = boxes[key]
    s.append(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="6" class="state"/>')
    s.append(f'<text x="{x + BW / 2}" y="{y + 23}" text-anchor="middle" font-size="13">{t1}</text>')
    s.append(f'<text x="{x + BW / 2}" y="{y + 41}" text-anchor="middle" font-size="13">{t2}</text>')


def arrow(x1, y1, x2, y2, label, lx, ly, anchor='middle'):
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/>')
    s.append(f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" class="label">{label}</text>')


arrow(252, 47, 348, 47, 'SMN', 300, 40)
arrow(465, 76, 465, 148, 'race of enumerations', 473, 116, 'start')
arrow(348, 177, 252, 177, 'completions', 300, 170)
arrow(350, 152, 252, 74, 'DNC₂ is Π⁰₁', 318, 100, 'start')
s.append('<line x1="135" y1="148" x2="135" y2="76" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/>')
s.append('<text x="127" y="116" text-anchor="end" class="label">f(e) from</text>')
s.append('<text x="127" y="132" text-anchor="end" class="math" font-size="14">θ<tspan class="mrm" font-size="10" dy="4">e,0</tspan><tspan class="label" dy="-4"> ∈ S</tspan></text>')
s.append('</svg>')
out['pa-characterizations'] = ''.join(s)

# ---------------------------------------------------------------- the tree of a computable tree whose path computes 0'
# Example: among 0..4, only 1 and 3 enter 0', at stages 3 and 6.
stage = {1: 3, 3: 6}
Dmax = 5
nodes = {(): None}
frontier = [()]
for n in range(Dmax):
    new = []
    for sig in frontier:
        # successor <0,0>: allowed while n has not entered by length n+1
        if not (n in stage and stage[n] <= n + 1):
            new.append(sig + ('0',))
        if n in stage:
            new.append(sig + ('1',))
    # a node is in T only if every earlier position chosen <0,0> is still compatible with its length
    keep = []
    for sig in new:
        ok = all(not (c == '0' and i in stage and stage[i] <= len(sig)) for i, c in enumerate(sig))
        if ok:
            keep.append(sig)
    for sig in keep:
        nodes[sig] = None
    frontier = keep
true_path = tuple('1' if i in stage else '0' for i in range(Dmax))
xs = {}


def jx(sig):
    # horizontal position: shift right for each <1,s> choice, left for each wrong <0,0>
    x = 200.0
    for i, c in enumerate(sig):
        if i in stage:
            x += 70 if c == '1' else -70
    return x


s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="A computable tree with two successors at most per node and a single path, which computes the halting set">']
for sig in sorted(nodes, key=lambda t: (len(t), t)):
    if sig == ():
        continue
    par = sig[:-1]
    x1, y1, x2, y2 = jx(par), 24 + len(par) * 48, jx(sig), 24 + len(sig) * 48
    on = true_path[:len(sig)] == sig
    cls = 'accent-stroke' if on else 'ink-stroke'
    s.append(f'<line x1="{x1:.1f}" y1="{y1}" x2="{x2:.1f}" y2="{y2}" class="{cls}" stroke-width="{2.2 if on else 1.2}"/>')
    i = len(sig) - 1
    val = f'⟨1, {stage[i]}⟩' if sig[-1] == '1' else '⟨0, 0⟩'
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    if i in stage:
        anchor, dx = ('start', 8) if sig[-1] == '1' else ('end', -8)
        s.append(f'<text x="{mx + dx:.1f}" y="{my + 4}" text-anchor="{anchor}" class="mrm" font-size="12">{val}</text>')
    elif on:
        s.append(f'<text x="{mx + 8:.1f}" y="{my + 4}" class="mrm" font-size="12">{val}</text>')
for sig in sorted(nodes, key=lambda t: (len(t), t)):
    x, y = jx(sig), 24 + len(sig) * 48
    on = true_path[:len(sig)] == sig
    s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="{"accent-fill" if on else "ink-fill"}"/>')
    # leaves of the picture that have no successor in T
    has_child = any(len(t) == len(sig) + 1 and t[:len(sig)] == sig for t in nodes)
    if not has_child and len(sig) < Dmax:
        s.append(f'<line x1="{x - 7:.1f}" y1="{y + 10}" x2="{x + 7:.1f}" y2="{y + 10}" class="ink-stroke" stroke-width="1.4"/>')
        s.append(f'<text x="{x:.1f}" y="{y + 26}" text-anchor="middle" class="label">no successor:</text>')
        s.append(f'<text x="{x:.1f}" y="{y + 40}" text-anchor="middle" class="label">1 enters at stage 3</text>')
# the wrong branch at position 3 survives to length 5 and dies at length 6
for sig in nodes:
    if len(sig) == Dmax:
        x, y = jx(sig), 24 + Dmax * 48
        if sig == true_path:
            s.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="mrm" font-size="12">⋮</text>')
            s.append(f'<text x="{x + 12:.1f}" y="{y + 22}" class="label">the path P</text>')
        else:
            s.append(f'<text x="{x:.1f}" y="{y + 20}" text-anchor="middle" class="label">no successor at length 6:</text>')
            s.append(f'<text x="{x:.1f}" y="{y + 34}" text-anchor="middle" class="label">3 enters at stage 6</text>')
s.append(f'<text x="{jx(()) + 10:.1f}" y="{20}" class="mrm" font-size="13">ε</text>')
for n in range(Dmax):
    s.append(f'<text x="470" y="{24 + n * 48 + 28}" class="label">position {n}{" ∈ ∅′" if n in stage else ""}</text>')
s.append('</svg>')
out['jump-tree'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
