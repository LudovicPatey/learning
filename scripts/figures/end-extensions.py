# Generates the inline SVG figures of the course End extensions of models of PA.
# Usage: python3 scripts/figures/end-extensions.py out.json
# Paste each figure into the lesson that uses it:
#   guesses   -> low-basis-isigma1.md
#   act       -> arithmetized-completeness.md
#   cohesive  -> macdowell-specker.md
#   gap       -> gaps.md
#   rare      -> minimal-types.md
# The output is deterministic.
import json, sys
out = {}


def mtext(x, y, body, size=14, anchor='middle', cls='math'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{body}</text>'


def label(x, y, body, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="label">{body}</text>'


def dot(x, y, cls='accent-fill', r=3.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>'


def line(x1, y1, x2, y2, cls='ink-stroke', w=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" stroke-width="{w}"{d}/>'


def bracket(x1, x2, yb, text, up=False, cls='muted-stroke'):
    d = 6 if up else -6
    ty = yb - 10 if up else yb + 18
    return (f'<path d="M{x1:.1f},{yb + d:.1f} L{x1:.1f},{yb:.1f} L{x2:.1f},{yb:.1f} L{x2:.1f},{yb + d:.1f}" class="{cls}" fill="none" stroke-width="1.2"/>'
            + label((x1 + x2) / 2, ty, text))


def cutmark(x, y, h=22):
    return line(x, y - h, x, y + h, 'accent-stroke', 1.6, '4 3')


# ---------------------------------------------------------------- guesses of the low basis theorem
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The tree of guesses of length at most 3; the least admissible guesses 0, 01, 010 form a branch, and the guess 00 is rejected because its tree is bounded">']
pos = {'': (300, 225)}
order = ['0', '1', '00', '01', '10', '11', '010', '011', '100', '101', '110', '111']
for c in order:
    px, py = pos[c[:-1]]
    spread = 140 / (2 ** (len(c) - 1))
    pos[c] = (px + (spread if c[-1] == '1' else -spread), py - 62)
chosen = {'', '0', '01', '010'}
for c in order:
    (x1, y1), (x2, y2) = pos[c[:-1]], pos[c]
    if c in chosen:
        s.append(line(x1, y1, x2, y2, 'accent-stroke', 2.2))
    elif c.startswith('00'):
        s.append(line(x1, y1, x2, y2, 'muted-stroke', 1.0, '3 3'))
    else:
        s.append(line(x1, y1, x2, y2, 'muted-stroke', 1.2))
for c in [''] + order:
    x, y = pos[c]
    if c in chosen:
        s.append(dot(x, y, 'accent-fill', 4.5))
    else:
        s.append(dot(x, y, 'node', 3.5))
    if c:
        s.append(mtext(x, y - 10, c, 12, cls='mrm'))
x, y = pos['00']
s.append(f'<path d="M{x - 6:.1f},{y - 6:.1f} L{x + 6:.1f},{y + 6:.1f} M{x - 6:.1f},{y + 6:.1f} L{x + 6:.1f},{y - 6:.1f}" class="ink-stroke" stroke-width="1.6"/>')
s.append(label(x - 4, y + 22, 'T₀₀ bounded: rejected'))
s.append(label(300, 244, 'empty guess: T itself'))
s.append(label(520, 40, 'c₃ = 010', 'middle'))
s.append(label(520, 102, 'c₂ = 01', 'middle'))
s.append(label(520, 164, 'c₁ = 0', 'middle'))
s.append('</svg>')
out['guesses'] = ''.join(s)


# ---------------------------------------------------------------- the arithmetized completeness theorem
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The model K built from constants contains M as an initial segment: the constant c_a names a, and the elements below a are the constants c_i for i below a">']
y = 80
s.append(line(20, y, 580, y))
s.append(dot(24, y))
s.append(mtext(24, y - 14, '0', 13, cls='mrm'))
for x in (70, 110, 150, 190):
    s.append(dot(x, y, 'accent-fill', 3.5))
s.append(mtext(130, y - 14, 'c<tspan class="mrm" font-size="10" dy="3">i</tspan>', 13))
s.append(dot(240, y, 'ink-fill', 4))
s.append(mtext(240, y - 14, 'a = [c<tspan class="mrm" font-size="10" dy="3">a</tspan><tspan dy="-3">]</tspan>', 13))
s.append(cutmark(330, y))
s.append(mtext(330, y - 30, 'M', 14))
for x in (400, 460, 520):
    s.append(dot(x, y, 'node', 3.5))
s.append(bracket(22, 236, y + 22, 'every [c] &lt; a equals some [cᵢ], i &lt; a'))
s.append(bracket(336, 578, y + 22, 'new elements: classes of other constants'))
s.append(label(300, 26, 'K = constants of the Henkin language, modulo provable equality in H'))
s.append('</svg>')
out['act'] = ''.join(s)


# ---------------------------------------------------------------- cohesive sets
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Three refinement steps: at each step the current set is split by R_z and an unbounded half is kept; the elements h_0, h_1, h_2 are chosen increasing in the kept halves">']
rows = [(40, 'S', [(60, 580)]), (90, 'S ∩ R₀', [(60, 140), (230, 330), (420, 580)]),
        (140, 'S ∩ R₀ ∖ R₁', [(100, 140), (260, 330), (470, 580)])]
for (yy, name, segs) in rows:
    s.append(line(60, yy, 580, yy, 'muted-stroke', 1.0, '2 4'))
    for (a, b) in segs:
        s.append(line(a, yy, b, yy, 'accent-stroke', 3.0))
    s.append(label(30, yy - 8, name, 'start'))
s.append(dot(80, 40, 'ink-fill', 4))
s.append(mtext(80, 30, 'h<tspan class="mrm" font-size="10" dy="3">0</tspan>', 13))
s.append(dot(250, 90, 'ink-fill', 4))
s.append(mtext(250, 80, 'h<tspan class="mrm" font-size="10" dy="3">1</tspan>', 13))
s.append(dot(300, 140, 'ink-fill', 4))
s.append(mtext(300, 130, 'h<tspan class="mrm" font-size="10" dy="3">2</tspan>', 13))
s.append(label(300, 180, 'all later elements of H lie in R₀ and outside R₁'))
s.append('</svg>')
out['cohesive'] = ''.join(s)


# ---------------------------------------------------------------- one new gap
s = ['<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The extension M(p/d) consists of M followed by the gap of d, between M[d] and the bound given by Skolem functions of d">']
y = 70
s.append(line(20, y, 560, y))
s.append(dot(24, y))
s.append(mtext(24, y - 14, '0', 13, cls='mrm'))
s.append(cutmark(240, y))
s.append(mtext(240, y - 30, 'M = M(p)[d]', 13))
s.append(dot(330, y, 'accent-fill', 4.5))
s.append(mtext(330, y - 14, 'd', 14))
for x in (290, 380, 440, 500):
    s.append(dot(x, y, 'node', 3))
s.append(mtext(540, y - 14, 't(d)', 13))
s.append(line(540, y - 6, 540, y + 6, 'ink-stroke', 1.4))
s.append(bracket(22, 236, y + 24, 'M: below every Skolem function of d'))
s.append(bracket(246, 556, y + 24, 'gap(d): c ≤ s(d) and t(c) ≥ d'))
s.append('</svg>')
out['gap'] = ''.join(s)


# ---------------------------------------------------------------- rare types
s = ['<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="Consecutive solutions of theta are far apart; if c lies in the gap of d, no solution of theta lies between c and d, so d is the least solution of theta above c">']
y = 80
s.append(line(20, y, 580, y))
for x in (60, 330):
    s.append(dot(x, y, 'node', 4))
s.append(mtext(60, y - 14, 'v′', 13))
s.append(f'<path d="M60,{y + 8} C120,{y + 50} 240,{y + 50} 300,{y + 8}" class="accent-stroke" fill="none" stroke-width="1.4"/>')
s.append(label(180, y + 58, 't*(v′) &lt; next solution'))
s.append(dot(250, y, 'ink-fill', 4))
s.append(mtext(250, y - 14, 'c', 14))
s.append(dot(330, y, 'accent-fill', 5))
s.append(mtext(330, y - 14, 'd', 14))
s.append(dot(540, y, 'node', 4))
s.append(bracket(240, 470, y - 34, 'gap(d)', up=True))
s.append(label(410, y + 30, 'no solution of θ in [c, d)'))
s.append(label(300, 150, 'discs: solutions of θ; d = (min v ≥ c) θ(v)'))
s.append('</svg>')
out['rare'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
