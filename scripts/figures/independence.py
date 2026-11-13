# Generates the inline SVG figures of the course Indicators and independence.
# Usage: python3 scripts/figures/independence.py out.json
# Paste each figure into the lesson that uses it:
#   catching      -> fast-growing.md
#   indiscernible -> diagonal-indiscernibles.md
#   omega-large   -> alpha-large.md
# The output is deterministic.
import json, sys
out = {}


def mtext(x, y, body, size=14, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{body}</text>'


def label(x, y, body, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="label">{body}</text>'


def dot(x, y, cls='accent-fill', r=3.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>'


def line(x1, y1, x2, y2, cls='ink-stroke', w=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" stroke-width="{w}"{d}/>'


def sub(base, s, cls='math'):
    return f'{base}<tspan class="mrm" font-size="10" dy="3">{s}</tspan>'


# ---------------------------------------------------------------- catching a semiregular cut
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Three stages of the construction: the interval from r_k to s_k is divided into r_k pieces by the iterates of F_{nu-1}; the values of the coded function f_k are marked; a piece containing no value becomes the next interval">']
rows = [(40, 40, 560), (120, 160, 420), (200, 230, 330)]
names = ['k', 'k+1', 'k+2']
for (y, x1, x2), nm in zip(rows, names):
    s.append(line(x1, y, x2, y, 'ink-stroke', 1.4))
    s.append(line(x1, y - 7, x1, y + 7, 'ink-stroke', 1.4))
    s.append(line(x2, y - 7, x2, y + 7, 'ink-stroke', 1.4))
    s.append(mtext(x1, y + 24, sub('r', nm), 14))
    s.append(mtext(x2, y + 24, sub('s', nm), 14))
# pieces of the first interval
cuts = [40, 70, 110, 160, 230, 330, 420, 560]
for c in cuts[1:-1]:
    s.append(line(c, 34, c, 46, 'muted-stroke', 1.2))
for v in (55, 95, 290, 480, 520):
    s.append(f'<rect x="{v - 3.5}" y="{36.5}" width="7" height="7" class="muted-fill"/>')
s.append(f'<rect x="160" y="30" width="260" height="20" class="accent-fill" fill-opacity="0.18"/>')
s.append(line(160, 52, 160, 112, 'accent-stroke', 1.0, '3 3'))
s.append(line(420, 52, 420, 112, 'accent-stroke', 1.0, '3 3'))
# second interval pieces
cuts2 = [160, 185, 230, 330, 420]
for c in cuts2[1:-1]:
    s.append(line(c, 114, c, 126, 'muted-stroke', 1.2))
for v in (175, 370, 400):
    s.append(f'<rect x="{v - 3.5}" y="{116.5}" width="7" height="7" class="muted-fill"/>')
s.append(f'<rect x="230" y="110" width="100" height="20" class="accent-fill" fill-opacity="0.18"/>')
s.append(line(230, 132, 230, 192, 'accent-stroke', 1.0, '3 3'))
s.append(line(330, 132, 330, 192, 'accent-stroke', 1.0, '3 3'))
s.append(label(580, 20, 'squares: values of the coded function', 'end'))
s.append(label(470, 205, 'I = sup of the r_k', 'start'))
s.append('</svg>')
out['catching'] = ''.join(s)


# ---------------------------------------------------------------- diagonal indiscernibles
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="A set of diagonal indiscernibles h_0 &lt; h_1 &lt; ...; a parameter x below h_i; two increasing tuples above h_i satisfy the same formulas with parameter x; the cut I is the supremum of the h_i with standard index">']
y = 95
s.append(line(20, y, 580, y))
s.append(dot(24, y, 'ink-fill', 3))
s.append('<text x="24" y="81" text-anchor="middle" class="mrm" font-size="13">0</text>')
xs = [70, 120, 175, 235, 300, 370]
for i, x in enumerate(xs):
    s.append(dot(x, y, 'accent-fill', 4))
    s.append(mtext(x, y - 14, sub('h', str(i)), 14))
s.append('<text x="410" y="99" class="mrm" font-size="14">…</text>')
s.append(line(450, y - 24, 450, y + 24, 'accent-stroke', 1.6, '4 3'))
s.append(mtext(450, y - 32, 'I', 14))
s.append(dot(530, y, 'ink-fill', 3.5))
s.append(mtext(530, y - 14, 'b', 14))
s.append(dot(95, y, 'ink-fill', 3))
s.append(mtext(95, y + 22, 'x', 14))
# two tuples
s.append(f'<path d="M175,{y + 10} C200,{y + 40} 280,{y + 40} 300,{y + 10}" class="accent-stroke" fill="none" stroke-width="1.3"/>')
s.append(f'<path d="M235,{y + 10} C270,{y + 62} 340,{y + 62} 370,{y + 10}" class="muted-stroke" fill="none" stroke-width="1.3"/>')
s.append(label(240, y + 52, 'ȳ', 'middle'))
s.append(label(330, y + 70, 'z̄', 'middle'))
s.append(label(300, 30, 'x &lt; h₁: φ(x, ȳ) ↔ φ(x, z̄) for tuples above h₁', 'middle'))
s.append('</svg>')
out['indiscernible'] = ''.join(s)


# ---------------------------------------------------------------- an omega^2-large set
s = ['<svg class="fig" viewBox="0 0 600 140" width="600" role="img" aria-label="An omega squared large set with least element 3: after the first element, the set splits into three consecutive omega-large blocks, each with more elements than its least element">']
y = 70
s.append(line(20, y, 580, y, 'muted-stroke', 1.0))
pts = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
X = lambda v: 30 + (v - 3) * 26
# blocks: {4,..,8} (5 elements, min 4), {9..18} (10, min 9), {19..} need 20 elements: draw abridged
blocks = [(4, 8), (9, 18), (19, 23)]
s.append(dot(X(3), y, 'ink-fill', 4))
s.append(mtext(X(3), y - 14, '3', 13))
for (lo, hi) in blocks:
    for v in range(lo, hi + 1):
        s.append(dot(X(v), y, 'accent-fill', 3.5))
    s.append(f'<path d="M{X(lo) - 5},{y + 12} L{X(lo) - 5},{y + 18} L{X(hi) + 5},{y + 18} L{X(hi) + 5},{y + 12}" class="muted-stroke" stroke-width="1.2" fill="none"/>')
s.append(label((X(4) + X(8)) / 2, y + 36, '5 &gt; 4'))
s.append(label((X(9) + X(18)) / 2, y + 36, '10 &gt; 9'))
s.append(label((X(19) + X(23)) / 2 + 20, y + 36, '20 &gt; 19 (continues)'))
s.append(mtext(X(4), y - 14, '4', 13))
s.append(mtext(X(9), y - 14, '9', 13))
s.append(mtext(X(19), y - 14, '19', 13))
s.append(label(580, 20, 'three ω-large blocks after the least element 3', 'end'))
s.append('</svg>')
out['omega-large'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
