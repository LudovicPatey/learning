# Generates the inline SVG figures of the course Cuts and extensions.
# Usage: python3 scripts/figures/cuts-and-extensions.py out.json
# Paste each figure into the lesson that uses it:
#   separation   -> standard-system.md
#   scott-branch -> weak-konig-cuts.md
#   semiregular  -> semiregular-cuts.md
#   cofinal      -> cofinal-extensions.md
#   splitting    -> collection-end-extensions.md
#   underspill   -> collection-end-extensions.md
# The output is deterministic.
import json, sys
out = {}


def bracket(x1, x2, yb, text, up=False, cls='muted-stroke'):
    d = 6 if up else -6
    ty = yb - 10 if up else yb + 18
    return (f'<path d="M{x1},{yb + d} L{x1},{yb} L{x2},{yb} L{x2},{yb + d}" class="{cls}" stroke-width="1.2"/>'
            f'<text x="{(x1 + x2) / 2:.1f}" y="{ty}" text-anchor="middle" class="label">{text}</text>')


def mtext(x, y, body, size=14, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{body}</text>'


def dot(x, y, cls='accent-fill', r=3.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>'


def line(x1, y1, x2, y2, cls='ink-stroke', w=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" stroke-width="{w}"{d}/>'


def cutmark(x, y, h=22):
    return line(x, y - h, x, y + h, 'accent-stroke', 1.6, '4 3')


# ---------------------------------------------------------------- the separation lemma
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The separation lemma: below the cut I the two disjoint sets A and B are defined by witnesses in I; overspill gives k above I below which no number has witnesses of both kinds; the set coded by d contains the numbers below k with an A-witness below k, hence all of A and nothing of B">']
y = 80
s.append(line(20, y, 580, y))
s.append(dot(24, y))
s.append('<text x="24" y="66" text-anchor="middle" class="mrm" font-size="13">0</text>')
for x in (60, 110, 170, 230):
    s.append(dot(x, y, 'accent-fill', 4))
for x in (85, 140, 200, 255):
    s.append(f'<rect x="{x - 4}" y="{y - 4}" width="8" height="8" class="muted-fill"/>')
s.append(cutmark(300, y))
s.append(mtext(300, y - 30, 'I', 14))
s.append(dot(450, y, 'ink-fill'))
s.append(mtext(450, y - 14, 'k', 14))
s.append(bracket(22, 294, y + 22, 'A (discs) and B (squares): witnesses in I'))
s.append(bracket(22, 446, y + 56, 'd codes {x &lt; k : some A-witness below k}'))
s.append(f'<text x="450" y="{y - 40}" text-anchor="middle" class="label">overspill: no x &lt; k has witnesses</text>')
s.append(f'<text x="450" y="{y - 26}" text-anchor="middle" class="label">of both kinds below k</text>')
s.append('</svg>')
out['separation'] = ''.join(s)


# ---------------------------------------------------------------- Scott: the branch below a node above the cut
s = ['<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="A binary tree drawn upwards; by overspill the tree has a node tau0 of a length above the cut I; its prefixes of lengths in I form an unbounded branch">']
levels = 6
base_y, dy = 230, 34
nodes = {(): (300, base_y)}
tree = [(), (0,), (1,), (0, 0), (0, 1), (1, 1), (0, 1, 0), (0, 1, 1), (1, 1, 0), (0, 1, 1, 0), (0, 1, 1, 1),
        (1, 1, 0, 1), (0, 1, 1, 0, 1), (0, 1, 1, 0, 0), (1, 1, 0, 1, 1), (0, 1, 1, 0, 1, 0), (0, 1, 1, 0, 0, 1)]
branch = {(), (0,), (0, 1), (0, 1, 1), (0, 1, 1, 0), (0, 1, 1, 0, 1), (0, 1, 1, 0, 1, 0)}
for t in tree[1:]:
    px, py = nodes[t[:-1]]
    spread = 150 / (1.7 ** (len(t) - 1))
    nodes[t] = (px + (spread if t[-1] else -spread), base_y - dy * len(t))
for t in tree[1:]:
    (x1, y1), (x2, y2) = nodes[t[:-1]], nodes[t]
    if t in branch:
        s.append(line(x1, y1, x2, y2, 'accent-stroke', 2.2))
    else:
        s.append(line(x1, y1, x2, y2, 'muted-stroke', 1.2))
for t in tree:
    x, yy = nodes[t]
    s.append(dot(x, yy, 'accent-fill' if t in branch else 'node', 3.5))
cut_y = base_y - dy * 3.5
s.append(line(60, cut_y, 560, cut_y, 'accent-stroke', 1.4, '5 4'))
s.append(f'<text x="40" y="{cut_y - 8:.1f}" class="label">lengths above I</text>')
s.append(f'<text x="40" y="{cut_y + 18:.1f}" class="label">lengths in I</text>')
tx, ty = nodes[(0, 1, 1, 0, 1, 0)]
s.append(mtext(tx + 18, ty + 4, 'τ<tspan class="mrm" font-size="10" dy="3">0</tspan>', 14))
s.append(f'<text x="470" y="{base_y - 10}" text-anchor="middle" class="label">the branch B: prefixes of τ₀</text>')
s.append('</svg>')
out['scott-branch'] = ''.join(s)


# ---------------------------------------------------------------- semiregular cut
s = ['<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="A coded function f with domain a in the cut I; the values of f that lie in I are bounded by some d in I, the other values lie above I">']
yl, yr = 180, 40
s.append(line(30, yl, 570, yl))
s.append(line(30, yr, 570, yr))
s.append('<text x="30" y="210" class="label">domain of f</text>')
s.append('<text x="570" y="24" text-anchor="end" class="label">values of f</text>')
s.append(dot(34, yl))
s.append(dot(170, yl, 'ink-fill'))
s.append(mtext(170, yl + 18, 'a', 14))
s.append(cutmark(330, yl, 14))
s.append(cutmark(330, yr, 14))
s.append(mtext(345, yl + 18, 'I', 13))
s.append(mtext(345, yr - 8, 'I', 13))
s.append(dot(240, yr, 'ink-fill'))
s.append(mtext(240, yr - 12, 'd', 14))
xs = [50, 66, 82, 98, 114, 130, 146, 160]
vals = [120, 520, 60, 455, 200, 560, 160, 390]
for x, v in zip(xs, vals):
    cls = 'accent-stroke' if v < 330 else 'muted-stroke'
    s.append(line(x, yl - 4, v, yr + 4, cls, 1.2))
    s.append(dot(x, yl, 'node', 2.5))
    s.append(dot(v, yr, 'accent-fill' if v < 330 else 'node', 3))
s.append(bracket(36, 236, yr + 22, 'values in I: all below d'))
s.append(bracket(340, 568, yr + 22, 'values above I'))
s.append('</svg>')
out['semiregular'] = ''.join(s)


# ---------------------------------------------------------------- cofinal extension: a witness function coded in M
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="A cofinal extension K of M: every element of K lies below an element a of M; a code s in M lists witnesses for all x below a, including the new elements of K below a">']
y = 70
s.append(line(20, y, 580, y))
for x in (40, 90, 150, 220, 300, 380, 460, 540):
    s.append(dot(x, y, 'accent-fill', 3.5))
for x in (120, 185, 260, 340, 420, 500):
    s.append(dot(x, y, 'node', 3))
s.append(dot(380, y, 'ink-fill', 4))
s.append(mtext(380, y - 14, 'a', 14))
s.append(bracket(22, 378, y + 22, 'x &lt; a in K: the code s in M gives witnesses (s)ₓ'))
s.append(f'<text x="300" y="{y + 72}" text-anchor="middle" class="label">discs: elements of M; circles: new elements of K, each below some element of M</text>')
s.append('</svg>')
out['cofinal'] = ''.join(s)


# ---------------------------------------------------------------- the splitting theorem
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="The splitting theorem: M is cofinal in its supremum in K, which is an initial segment of K">']
y = 70
s.append(line(20, y, 580, y))
for x in (40, 100, 170, 240, 310):
    s.append(dot(x, y, 'accent-fill', 3.5))
for x in (70, 135, 205, 280, 330):
    s.append(dot(x, y, 'node', 3))
s.append(cutmark(360, y))
for x in (420, 480, 540):
    s.append(dot(x, y, 'node', 3))
s.append(bracket(22, 354, y + 22, 'M̄ = sup_K M: below some element of M'))
s.append(bracket(22, 578, y + 58, 'K'))
s.append(bracket(366, 578, y - 26, 'K ∖ M̄: above all of M', up=True))
s.append(bracket(22, 354, y - 26, 'M (discs) is cofinal in M̄', up=True))
s.append('</svg>')
out['splitting'] = ''.join(s)


# ---------------------------------------------------------------- underspill in the proof of Paris-Kirby
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The proof that end extensions give collection: every b in K above M bounds witnesses for all x below a; underspill gives such a bound b0 inside M">']
y = 80
s.append(line(20, y, 580, y))
s.append(dot(24, y))
s.append('<text x="24" y="66" text-anchor="middle" class="mrm" font-size="13">0</text>')
s.append(dot(110, y, 'ink-fill'))
s.append(mtext(110, y - 14, 'a', 14))
s.append(dot(250, y, 'accent-fill', 4))
s.append(mtext(250, y - 14, 'b<tspan class="mrm" font-size="10" dy="3">0</tspan>', 14))
s.append(cutmark(330, y))
s.append(mtext(330, y - 30, 'M', 13))
for x in (400, 460, 520):
    s.append(dot(x, y, 'node', 3.5))
s.append(f'<path d="M460,{y + 8} C420,{y + 40} 300,{y + 40} 256,{y + 8}" class="accent-stroke" fill="none" stroke-width="1.4"/>')
s.append(f'<text x="355" y="{y + 52}" text-anchor="middle" class="label">underspill</text>')
s.append(bracket(370, 578, y - 26, 'every b ∈ K ∖ M bounds witnesses for x &lt; a', up=True))
s.append('</svg>')
out['underspill'] = ''.join(s)


json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
