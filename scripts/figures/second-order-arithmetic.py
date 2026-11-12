# Generates the inline SVG figures of the course on second-order arithmetic.
# Usage: python3 scripts/figures/second-order-arithmetic.py out.json
# Paste each figure into the lesson that uses it:
#   nonstandard-model                 -> language-and-models.md
#   function-code, bisection          -> analysis-in-rca0.md
# The output is deterministic.
import json, math, sys
out = {}


def sub(base, s, x, y, size=15, anchor='middle', cls='math'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size * 0.68)}" dy="4">{s}</tspan></text>')


# ---------------------------------------------------------------- a non-standard first-order part
s = ['<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="The order of a non-standard model: the standard numbers, followed by blocks ordered like the integers">']
y = 60
# standard part
s.append(f'<line x1="20" y1="{y}" x2="196" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
for i in range(6):
    x = 30 + i * 30
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="accent-fill"/>')
    if i < 5:
        s.append(f'<text x="{x}" y="{y - 12}" text-anchor="middle" class="mrm" font-size="13">{i}</text>')
s.append(f'<text x="218" y="{y + 4}" text-anchor="middle" class="mrm" font-size="14">⋯</text>')
# Z-blocks
blocks = [(250, 'b'), (400, 'c')]
for cx, name in blocks:
    s.append(f'<line x1="{cx - 2}" y1="{y}" x2="{cx + 122}" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
    s.append(f'<text x="{cx - 14}" y="{y + 4}" text-anchor="middle" class="mrm" font-size="14">⋯</text>')
    s.append(f'<text x="{cx + 136}" y="{y + 4}" text-anchor="middle" class="mrm" font-size="14">⋯</text>')
    for j in range(5):
        x = cx + 10 + j * 25
        s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="ink-fill"/>')
    mid = cx + 60
    if name == 'c':
        s.append(f'<text x="{mid - 25}" y="{y - 12}" text-anchor="middle" class="math" font-size="13">c<tspan class="mrm">−1</tspan></text>')
        s.append(f'<text x="{mid}" y="{y - 12}" text-anchor="middle" class="math" font-size="13">c</text>')
        s.append(f'<text x="{mid + 25}" y="{y - 12}" text-anchor="middle" class="math" font-size="13">c<tspan class="mrm">+1</tspan></text>')
# braces (drawn as brackets)
def bracket(x1, x2, yb, text):
    return (f'<path d="M{x1},{yb - 6} L{x1},{yb} L{x2},{yb} L{x2},{yb - 6}" class="muted-stroke" stroke-width="1.2"/>'
            f'<text x="{(x1 + x2) / 2}" y="{yb + 18}" text-anchor="middle" class="label">{text}</text>')
s.append(bracket(22, 200, y + 26, 'standard part: 0, 1, 2, …'))
s.append(bracket(236, 540, y + 26, 'non-standard numbers: blocks ordered like ℤ'))
s.append(f'<text x="300" y="{y + 72}" text-anchor="middle" class="label">the standard part contains 0, is closed under successor, and is bounded by c</text>')
s.append('</svg>')
out['nonstandard-model'] = ''.join(s)


# ---------------------------------------------------------------- the function used in the two plots
def f(x):
    return (x - 0.6) + 0.12 * math.sin(7 * x)


X0, X1 = 70, 530      # pixel range of [0, 1]
YMIN, YMAX = -0.8, 0.55


def px(x):
    return X0 + x * (X1 - X0)


def py(v, top=20, bottom=250):
    return bottom - (v - YMIN) / (YMAX - YMIN) * (bottom - top)


def graph(top=20, bottom=250):
    pts = ' '.join(f'{px(i / 200):.1f},{py(f(i / 200), top, bottom):.1f}' for i in range(201))
    return f'<polyline points="{pts}" class="ink-stroke" stroke-width="1.8"/>'


def axes(top=20, bottom=250, ticks=True):
    r = [f'<line x1="{X0 - 10}" y1="{py(0, top, bottom):.1f}" x2="{X1 + 20}" y2="{py(0, top, bottom):.1f}" class="axis"/>',
         f'<line x1="{X0}" y1="{top - 5}" x2="{X0}" y2="{bottom}" class="axis"/>',
         f'<line x1="{X1}" y1="{py(0, top, bottom) - 4:.1f}" x2="{X1}" y2="{py(0, top, bottom) + 4:.1f}" class="axis"/>']
    if ticks:
        r.append(f'<text x="{X0 - 6}" y="{py(0, top, bottom) + 16:.1f}" text-anchor="end" class="mrm" font-size="13">0</text>')
        r.append(f'<text x="{X1}" y="{py(0, top, bottom) + 18:.1f}" text-anchor="middle" class="mrm" font-size="13">1</text>')
    return r


def frange(lo, hi):
    vals = [f(lo + (hi - lo) * i / 100) for i in range(101)]
    return min(vals), max(vals)


# ---------------------------------------------------------------- a code of a continuous function
s = ['<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="The graph of a continuous function and rectangles given by quadruples of a code; around a point x, narrower rectangles determine the value f(x)">']
s += axes(ticks=False)
s.append(f'<text x="{X1 + 6}" y="{py(0) + 18:.1f}" text-anchor="middle" class="mrm" font-size="13">1</text>')
boxes = []
# a few unrelated pieces of information
for a, r in [(0.12, 0.1), (0.62, 0.12), (0.88, 0.1)]:
    lo, hi = frange(a - r, a + r)
    boxes.append((a, r, (lo + hi) / 2, (hi - lo) / 2 + 0.04, 'muted-stroke', 1.1))
# a sequence of rectangles around x0
x0 = 0.32
for r, extra in [(0.12, 0.05), (0.06, 0.03), (0.025, 0.012)]:
    a = x0 + r / 3
    lo, hi = frange(a - r, a + r)
    boxes.append((a, r, (lo + hi) / 2, (hi - lo) / 2 + extra, 'accent-stroke', 1.5))
for a, r, b, sr, cls, w in boxes:
    s.append(f'<rect x="{px(a - r):.1f}" y="{py(b + sr):.1f}" width="{px(a + r) - px(a - r):.1f}" '
             f'height="{py(b - sr) - py(b + sr):.1f}" class="{cls}" stroke-width="{w}"/>')
s.append(graph())
# annotate the largest accent box
a, r, b, sr, _, _ = boxes[3]
yb = 268
s.append(f'<line x1="{px(a - r):.1f}" y1="{py(b - sr):.1f}" x2="{px(a - r):.1f}" y2="{yb - 12}" class="muted-stroke" stroke-dasharray="2 3"/>')
s.append(f'<line x1="{px(a + r):.1f}" y1="{py(b - sr):.1f}" x2="{px(a + r):.1f}" y2="{yb - 12}" class="muted-stroke" stroke-dasharray="2 3"/>')
s.append(f'<text x="{px(a - r):.1f}" y="{yb}" text-anchor="middle" class="math" font-size="13">a<tspan class="mrm"> − </tspan>r</text>')
s.append(f'<text x="{px(a + r):.1f}" y="{yb}" text-anchor="middle" class="math" font-size="13">a<tspan class="mrm"> + </tspan>r</text>')
s.append(f'<line x1="{X0}" y1="{py(b + sr):.1f}" x2="{px(a - r):.1f}" y2="{py(b + sr):.1f}" class="muted-stroke" stroke-dasharray="2 3"/>')
s.append(f'<line x1="{X0}" y1="{py(b - sr):.1f}" x2="{px(a - r):.1f}" y2="{py(b - sr):.1f}" class="muted-stroke" stroke-dasharray="2 3"/>')
s.append(f'<text x="{X0 - 6}" y="{py(b + sr) + 5:.1f}" text-anchor="end" class="math" font-size="13">b<tspan class="mrm"> + </tspan>s</text>')
s.append(f'<text x="{X0 - 6}" y="{py(b - sr) + 5:.1f}" text-anchor="end" class="math" font-size="13">b<tspan class="mrm"> − </tspan>s</text>')
# the point x0 and its value
s.append(f'<line x1="{px(x0):.1f}" y1="{py(0) - 4:.1f}" x2="{px(x0):.1f}" y2="{py(0) + 4:.1f}" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<text x="{px(x0):.1f}" y="{py(0) - 8:.1f}" text-anchor="middle" class="math" font-size="13">x</text>')
s.append(f'<circle cx="{px(x0):.1f}" cy="{py(f(x0)):.1f}" r="3.5" class="accent-fill"/>')
s.append(f'<text x="{px(1) + 14:.1f}" y="{py(f(1)) + 5:.1f}" text-anchor="middle" class="math" font-size="14">f</text>')
s.append('</svg>')
out['function-code'] = ''.join(s)

# ---------------------------------------------------------------- bisection in the intermediate value theorem
top, bottom = 20, 200
s = ['<svg class="fig" viewBox="0 0 600 350" width="600" role="img" aria-label="Bisection: the intervals [a_n, b_n] halve at each step and keep f(a_n) below 0 and f(b_n) above 0">']
s += axes(top, bottom)
s.append(graph(top, bottom))
a_, b_ = 0.0, 1.0
rows = []
for n in range(6):
    rows.append((a_, b_))
    c = (a_ + b_) / 2
    if f(c) < 0:
        a_ = c
    else:
        b_ = c
for n, (a_, b_) in enumerate(rows):
    yy = 222 + n * 20
    s.append(f'<line x1="{px(a_):.1f}" y1="{yy}" x2="{px(b_):.1f}" y2="{yy}" class="accent-stroke" stroke-width="2.2"/>')
    s.append(f'<line x1="{px(a_):.1f}" y1="{yy - 4}" x2="{px(a_):.1f}" y2="{yy + 4}" class="accent-stroke" stroke-width="1.5"/>')
    s.append(f'<line x1="{px(b_):.1f}" y1="{yy - 4}" x2="{px(b_):.1f}" y2="{yy + 4}" class="accent-stroke" stroke-width="1.5"/>')
    s.append(f'<text x="24" y="{yy + 4}" class="math" font-size="13">n<tspan class="mrm"> = {n}</tspan></text>')
    if n < 4:
        s.append(f'<circle cx="{px(a_):.1f}" cy="{py(f(a_), top, bottom):.1f}" r="3" class="ink-fill"/>')
        s.append(f'<circle cx="{px(b_):.1f}" cy="{py(f(b_), top, bottom):.1f}" r="3" class="accent-fill"/>')
s.append(sub('a', '2', px(rows[2][0]) - 4, 222 + 2 * 20 - 8, size=13, anchor='end'))
s.append(sub('b', '2', px(rows[2][1]) + 4, 222 + 2 * 20 - 8, size=13, anchor='start'))
s.append(f'<text x="{px(0.95):.1f}" y="{py(f(0.95), top, bottom) - 12:.1f}" text-anchor="middle" class="math" font-size="14">f</text>')
s.append(f'<circle cx="{X0 + 8}" cy="336" r="3" class="ink-fill"/><text x="{X0 + 16}" y="340" class="label">left endpoints: </text>')
s.append(f'<text x="{X0 + 110}" y="340" class="math" font-size="13">f<tspan class="mrm">(</tspan>a<tspan class="mrm" font-size="9" dy="3">n</tspan><tspan class="mrm" dy="-3">) &lt; 0</tspan></text>')
s.append(f'<circle cx="{X0 + 228}" cy="336" r="3" class="accent-fill"/><text x="{X0 + 236}" y="340" class="label">right endpoints: </text>')
s.append(f'<text x="{X0 + 338}" y="340" class="math" font-size="13">f<tspan class="mrm">(</tspan>b<tspan class="mrm" font-size="9" dy="3">n</tspan><tspan class="mrm" dy="-3">) &gt; 0</tspan></text>')
s.append('</svg>')
out['bisection'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
