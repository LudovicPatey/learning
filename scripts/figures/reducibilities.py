# Generates the inline SVG figures of the course Reducibilities between problems.
# Usage: python3 scripts/figures/reducibilities.py out.json
# Paste each figure into the lesson that uses it:
#   reduction-game                      -> omega-reducibility.md
#   computable-reduction, scott-tower   -> computable-reducibility.md
#   weihrauch-reduction, implications,
#   continuity                          -> weihrauch.md
#   wkl-llpo                            -> parallelization.md
# The output is deterministic.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def math(t, x, y, size=17, anchor='middle', extra=''):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="math" font-size="{size}"{extra}>{t}</text>'


def label(t, x, y, anchor='start'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="label">{t}</text>'


def arrow(x1, y1, x2, y2, mid, cls='ink-stroke', dash=False, sw=1.3):
    d = ' stroke-dasharray="5 4"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" stroke-width="{sw}"{d} '
            f'marker-end="url(#{mid})"/>')


# ---------------------------------------------------------------- the reduction game for KL and J
# Moves of G(J -> KL) in the proof that KL <=_omega J.
s = ['<svg class="fig" viewBox="0 0 600 282" width="600" role="img" aria-label="The moves of the game G(J to KL): Player 1 plays a tree T, Player 2 plays T and T prime as instances of the jump, Player 1 answers with T prime and T double prime, and Player 2 wins with a path computable in T double prime">',
     '<defs>' + marker('ah-game', 'muted-fill') + marker('ah-game-a', 'accent-fill') + '</defs>']
x1, x2 = 210, 390
s.append(label('Player 1', x1, 18, 'middle'))
s.append(label('Player 2', x2, 18, 'middle'))
moves = [
    (1, 'T', 'instance of KL', 50),
    (2, 'T', 'instance of J', 90),
    (1, "T′", 'solution', 130),
    (2, "T′", 'instance of J', 170),
    (1, "T″", 'solution', 210),
    (2, 'P', 'path through T', 250),
]
for k, (pl, t, lab, y) in enumerate(moves):
    x = x1 if pl == 1 else x2
    s.append(f'<rect x="{x - 26}" y="{y - 19}" width="52" height="28" rx="6" class="{"head-cell" if k == 5 else "cell"}"/>')
    s.append(math(t, x, y, 17))
    if pl == 1:
        s.append(label(lab, x - 36, y - 1, 'end'))
    else:
        s.append(label(lab, x + 36, y - 1, 'start'))
    if k + 1 < len(moves):
        ny = moves[k + 1][3]
        sx = x + (26 if pl == 1 else -26)
        ex = (x2 - 28) if pl == 1 else (x1 + 28)
        last = k + 1 == len(moves) - 1
        s.append(arrow(sx, y - 5, ex, ny - 7, 'ah-game-a' if last else 'ah-game',
                       'accent-stroke' if last else 'muted-stroke', sw=1.2))
for y0_, y1_, t in [(32, 58, 'start'), (72, 138, 'round 1'), (152, 218, 'round 2'), (232, 258, 'round 3')]:
    s.append(f'<line x1="40" y1="{y0_}" x2="40" y2="{y1_}" class="axis"/>')
    s.append(label(t, 48, (y0_ + y1_) / 2 + 4))
s.append(label('computable in T', x2 + 36, 104))
s.append(label('computable in T ⊕ T′', x2 + 36, 184))
s.append(label('computable in T ⊕ T′ ⊕ T″', x2 + 36, 264))
s.append('</svg>')
out['reduction-game'] = ''.join(s)


# ---------------------------------------------------------------- square diagrams of reductions
def title_svg(t, x, y):
    base, sub_ = t
    return (f'<text x="{x}" y="{y}" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" dx="5">≤</tspan>'
            f'<tspan class="mrm" font-size="11" dy="4">{sub_}</tspan><tspan dx="5" dy="-4">Q</tspan></text>')


def square(ox, title, fwd, back, uses_instance, mid, show_cols=True):
    """A reduction of P to Q drawn as a square: instances on top, solutions below."""
    r = []
    lx, rx, ty, by = ox + 90, ox + 250, 70, 200
    if show_cols:
        r.append(math('P', lx, 34, 18))
        r.append(math('Q', rx, 34, 18))
    r.append(title_svg(title, (lx + rx) / 2, 250))
    for (x, y, t, cl) in [(lx, ty, 'X', 'cell'), (rx, ty, 'X̃', 'cell'), (rx, by, 'Ỹ', 'cell'), (lx, by, 'Y', 'head-cell')]:
        r.append(f'<rect x="{x - 22}" y="{y - 20}" width="44" height="30" rx="6" class="{cl}"/>')
        r.append(math(t, x, y + 1, 17))
    # forward
    r.append(arrow(lx + 24, ty - 5, rx - 26, ty - 5, mid))
    r.append(label(fwd, (lx + rx) / 2, ty - 13, 'middle'))
    # solved by
    r.append(arrow(rx, ty + 12, rx, by - 23, mid, 'muted-stroke', dash=True))
    r.append(arrow(lx, ty + 12, lx, by - 23, mid, 'muted-stroke', dash=True))
    r.append(label('any solution', rx + 8, (ty + by) / 2 - 2))
    r.append(label('a solution', lx - 8, (ty + by) / 2 - 2, 'end'))
    # backward
    r.append(arrow(rx - 24, by - 5, lx + 26, by - 5, mid, 'accent-stroke', sw=1.6))
    r.append(label(back, (lx + rx) / 2, by + 24, 'middle'))
    if uses_instance:
        r.append(f'<path d="M{lx + 18},{ty + 12} C{lx + 70},{ty + 50} {lx + 80},{by - 40} {lx + 60},{by - 9}" '
                 f'class="accent-stroke" stroke-width="1.2" stroke-dasharray="2 3" marker-end="url(#{mid}a)"/>')
        r.append(label('X is used', lx + 80, ty + 62))
    return r


s = ['<svg class="fig" viewBox="0 0 660 262" width="660" role="img" aria-label="Diagrams of a computable reduction and of a strong computable reduction of P to Q">',
     '<defs>' + marker('ah-cred', 'ink-fill') + marker('ah-creda', 'accent-fill') + '</defs>']
s += square(0, ('P', 'c'), 'X computes', 'X ⊕ Ỹ computes', True, 'ah-cred')
s += square(320, ('P', 'sc'), 'X computes', 'Ỹ computes', False, 'ah-cred')
s.append('</svg>')
out['computable-reduction'] = ''.join(s)

s = ['<svg class="fig" viewBox="0 0 660 262" width="660" role="img" aria-label="Diagrams of a Weihrauch reduction and of a strong Weihrauch reduction of P to Q, with forward functional Phi and backward functional Psi">',
     '<defs>' + marker('ah-wred', 'ink-fill') + marker('ah-wreda', 'accent-fill') + '</defs>']
s += square(0, ('P', 'W'), 'X̃ = Φ(X)', 'Y = Ψ(X ⊕ Ỹ)', True, 'ah-wred')
s += square(320, ('P', 'sW'), 'X̃ = Φ(X)', 'Y = Ψ(Ỹ)', False, 'ah-wred')
s.append('</svg>')
out['weihrauch-reduction'] = ''.join(s)


# ---------------------------------------------------------------- the tower of Scott's theorem
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="The sets Z0 = A, Z1, Z2, Z3 of the proof of Scott theorem, each PA relative to the previous one and computing it, all computable in P">',
     '<defs>' + marker('ah-tower', 'muted-fill') + '</defs>']
xs = [70, 190, 310, 430]
names = ['A', 'Z₁', 'Z₂', 'Z₃']
for i, x in enumerate(xs):
    s.append(f'<rect x="{x - 30}" y="104" width="60" height="32" rx="6" class="cell"/>')
    if i == 0:
        s.append(math('Z₀ = A', x, 126, 15))
    else:
        s.append(math(names[i], x, 126, 16))
    if i > 0:
        s.append(arrow(xs[i - 1] + 32, 120, x - 32, 120, 'ah-tower', 'muted-stroke'))
        s.append(label('PA over', (xs[i - 1] + x) / 2, 112, 'middle'))
s.append(arrow(xs[-1] + 32, 120, 520, 120, 'ah-tower', 'muted-stroke', dash=True))
s.append(f'<text x="540" y="125" class="mrm muted" font-size="16">⋯</text>')
s.append(f'<rect x="250" y="20" width="60" height="32" rx="6" class="head-cell"/>')
s.append(math('P', 280, 42, 17))
for x in xs:
    s.append(f'<line x1="{x}" y1="102" x2="{280 + (x - 280) * 0.18:.1f}" y2="54" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/>')
s.append(label('P computes every Zᵢ: it computes one member of the Π⁰₁(A) class of such towers', 300, 164, 'middle'))
s.append(label('the Scott ideal is the class of sets computable in some Zᵢ', 300, 182, 'middle'))
s.append('</svg>')
out['scott-tower'] = ''.join(s)


# ---------------------------------------------------------------- implications between reducibilities
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="Implications between the reducibilities: strong Weihrauch implies Weihrauch and strong computable; each of these implies computable reducibility, which implies omega-reducibility">',
     '<defs>' + marker('ah-impl', 'ink-fill') + '</defs>']
nodes = {'sW': (70, 85, '≤sW'), 'W': (230, 35, '≤W'), 'sc': (230, 135, '≤sc'), 'c': (390, 85, '≤c'), 'w': (530, 85, '≤ω')}
for k, (x, y, t) in nodes.items():
    s.append(f'<rect x="{x - 32}" y="{y - 18}" width="64" height="32" rx="6" class="{"head-cell" if k == "sW" else "cell"}"/>')
    s.append(f'<text x="{x}" y="{y + 4}" text-anchor="middle" class="mrm" font-size="17">≤<tspan font-size="12" dy="4">{t[1:]}</tspan></text>')
for a, b in [('sW', 'W'), ('sW', 'sc'), ('W', 'c'), ('sc', 'c'), ('c', 'w')]:
    (xa, ya, _), (xb, yb, _) = nodes[a], nodes[b]
    dx, dy = xb - xa, yb - ya
    n = (dx * dx + dy * dy) ** 0.5
    sx, sy = xa + 36 * dx / n, ya + 20 * dy / n
    ex, ey = xb - 38 * dx / n, yb - 22 * dy / n
    s.append(arrow(round(sx, 1), round(sy, 1), round(ex, 1), round(ey, 1), 'ah-impl'))
s.append(label('uniform', 230, 12, 'middle'))
s.append(label('strong: the backward step does not use the instance', 230, 168, 'middle'))
s.append('</svg>')
out['implications'] = ''.join(s)


# ---------------------------------------------------------------- the continuity argument for RT^1_2
N, u, x, v = 14, 5, 7, 8
w, x0 = 30, 110
s = ['<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="The colorings f0 and f1 of the proof: they agree below the use u, so the functional puts x in both outputs, but x has color 0 for f1, which is 1 from v on">',
     '<defs>' + marker('ah-cont', 'accent-fill') + '</defs>']
for row, (name, y) in enumerate([('f₀', 40), ('f₁', 104)]):
    s.append(math(name, x0 - 24, y + 21, 17))
    for i in range(N):
        b = 0 if row == 0 or i < v else 1
        cls = 'cell head-cell' if (row == 1 and i >= v) else 'cell'
        s.append(f'<rect x="{x0 + i*w}" y="{y}" width="{w}" height="{w}" class="{cls}"/>')
        s.append(f'<text x="{x0 + i*w + w/2}" y="{y + 21}" text-anchor="middle" class="mrm" font-size="15">{b}</text>')
    s.append(f'<text x="{x0 + N*w + 8}" y="{y + 21}" class="mrm muted" font-size="16">⋯</text>')
for i in range(N):
    s.append(f'<text x="{x0 + i*w + w/2}" y="{34}" text-anchor="middle" class="mrm muted" font-size="11">{i}</text>')
# use bracket over f0
s.append(f'<path d="M{x0 + 2},{78} L{x0 + 2},{86} L{x0 + u*w - 2},{86} L{x0 + u*w - 2},{78}" class="accent-stroke" stroke-width="1.4"/>')
s.append(label('use u: read by the computation Φ(x) = 1', x0, 99).replace(f'y="99"', 'y="99" dx="0"'))
# x marker
xx = x0 + x*w + w/2
s.append(f'<circle cx="{xx}" cy="{55}" r="13" class="accent-stroke" stroke-width="1.6"/>')
s.append(f'<circle cx="{xx}" cy="{119}" r="13" class="accent-stroke" stroke-width="1.6"/>')
s.append(label('x', xx, 14, 'middle'))
# v marker
vx = x0 + v*w
s.append(f'<line x1="{vx}" y1="96" x2="{vx}" y2="146" class="ink-stroke" stroke-width="1.4"/>')
s.append(label('v', vx, 160, 'middle'))
s.append(label('f₀ is constant 0, and x ∈ Φ(f₀); f₁ agrees with f₀ below v ≥ u, so x ∈ Φ(f₁),', 300, 184, 'middle'))
s.append(label('but the only color with infinitely many elements is 1, while f₁(x) = 0', 300, 202, 'middle'))
s.append('</svg>')
out['continuity'] = ''.join(s)


# ---------------------------------------------------------------- WKL to parallel LLPO
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Left: a node sigma whose left successor dies at stage 2 while the right successor is extendible. Right: the instance q sigma of LLPO, with a single 1 at position 4 = 2 times 2 plus 0, whose only solution is 1">',
     '<defs>' + marker('ah-llpo', 'accent-fill') + '</defs>']
# tree part
root = (190, 30)
lvl = 44
nodes = {'': root}
def tpos(st):
    x = root[0]
    for k, c in enumerate(st):
        x += (-1 if c == '0' else 1) * 70 / (1.7 ** k)
    return round(x, 1), 30 + lvl * len(st)
dead_sub = ['0', '00', '01']
alive_sub = ['1', '10', '11', '100', '110', '111', '1000', '1100', '1110', '1111']
for st in dead_sub + alive_sub:
    (xa, ya), (xb, yb) = tpos(st[:-1]), tpos(st)
    cls = 'muted-stroke' if st[0] == '0' else ('accent-stroke' if st in ('1', '11', '111', '1111') else 'ink-stroke')
    sw = 2.0 if cls == 'accent-stroke' else 1.2
    dash = ' stroke-dasharray="3 3"' if st[0] == '0' else ''
    s.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" class="{cls}" stroke-width="{sw}"{dash}/>')
for st in [''] + dead_sub + alive_sub:
    xb, yb = tpos(st)
    s.append(f'<circle cx="{xb}" cy="{yb}" r="3.5" class="{"muted-fill" if st[:1] == "0" else "ink-fill"}"/>')
s.append(math('σ', root[0] + 12, root[1] - 4, 16, 'start'))
for st in ('00', '01'):
    xd, yd = tpos(st)
    s.append(f'<line x1="{xd - 7}" y1="{yd + 8}" x2="{xd + 7}" y2="{yd + 8}" class="muted-stroke" stroke-width="1.4"/>')
s.append(label('σ⌢0 dies at stage 2:', 16, 150, 'start'))
s.append(label('no extension of length |σ| + 3', 16, 166, 'start'))
s.append(f'<text x="{tpos("1111")[0]}" y="{tpos("1111")[1] + 22}" text-anchor="middle" class="mrm muted" font-size="15">⋮</text>')
# LLPO instance
qx, qy, cw = 372, 80, 25
s.append(math('q', qx - 18, qy + 19, 17, 'end'))
s.append(f'<text x="{qx - 18}" y="{qy + 24}" class="math" font-size="11">σ</text>')
for i in range(8):
    b = 1 if i == 4 else 0
    cls = 'cell head-cell' if i == 4 else 'cell'
    s.append(f'<rect x="{qx + i*cw}" y="{qy}" width="{cw}" height="{cw}" class="{cls}"/>')
    s.append(f'<text x="{qx + i*cw + cw/2}" y="{qy + 18}" text-anchor="middle" class="mrm" font-size="14">{b}</text>')
    s.append(f'<text x="{qx + i*cw + cw/2}" y="{qy + cw + 14}" text-anchor="middle" class="mrm muted" font-size="11">{i}</text>')
s.append(f'<text x="{qx + 8*cw + 6}" y="{qy + 18}" class="mrm muted" font-size="15">⋯</text>')
s.append(label('position 2s + i = 4: s = 2, i = 0', qx, qy - 14))
s.append(label('the only solution to this instance is 1:', qx, qy + 76))
s.append(label('the path is extended by σ⌢1', qx, qy + 94))
s.append('</svg>')
out['wkl-llpo'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False)
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
