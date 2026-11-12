# Generates the inline SVG figures of the course Fragments of arithmetic.
# Usage: python3 scripts/figures/fragments-of-arithmetic.py out.json
# Paste each figure into the lesson that uses it:
#   end-extension   -> pa-minus.md
#   blocks          -> bounded-induction.md
#   parikh-cut      -> parikh.md
#   bits            -> coding.md
#   records         -> coded-sets.md
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


def sup(s, size=10):
    return f'<tspan class="mrm" font-size="{size}" dy="-6">{s}</tspan><tspan dy="6"> </tspan>'


def dots(x, y):
    return f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" class="mrm" font-size="14">⋯</text>'


# ---------------------------------------------------------------- end extension and bounded quantifiers
s = ['<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="An end extension: the model M is an initial segment of N; the candidates y below t(a) for a bounded quantifier with parameters a in M all lie in M">']
y = 70
s.append(f'<line x1="20" y1="{y}" x2="580" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<circle cx="24" cy="{y}" r="3.5" class="accent-fill"/>')
s.append(f'<text x="24" y="{y - 12}" text-anchor="middle" class="mrm" font-size="13">0</text>')
s.append(f'<circle cx="110" cy="{y}" r="3.5" class="accent-fill"/>')
s.append(mtext(110, y - 12, 'a', 14))
s.append(f'<circle cx="270" cy="{y}" r="3.5" class="accent-fill"/>')
s.append(mtext(270, y - 12, 't(a)', 14))
for x in (140, 170, 200, 230, 255):
    s.append(f'<circle cx="{x}" cy="{y}" r="2.5" class="node"/>')
s.append(bracket(130, 262, y - 30, 'candidates y &lt; t(a): all in M', up=True))
s.append(f'<line x1="340" y1="{y - 22}" x2="340" y2="{y + 22}" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/>')
for x in (420, 470, 520):
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="node"/>')
s.append(bracket(380, 560, y - 30, 'new elements of N', up=True))
s.append(bracket(22, 334, y + 22, 'M: an initial segment of N'))
s.append(bracket(22, 578, y + 56, 'N'))
s.append('</svg>')
out['end-extension'] = ''.join(s)


# ---------------------------------------------------------------- order type: N followed by densely ordered copies of Z
s = ['<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The order of a non-standard model of bounded induction: the standard numbers, followed by copies of the integers, called blocks; below the block of a lies the block of half of a, between the blocks of a and b lies the block of their mean, above b lies the block of 2b">']
y = 70
s.append(f'<line x1="18" y1="{y}" x2="108" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
for i in range(4):
    x = 26 + 24 * i
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="accent-fill"/>')
    s.append(f'<text x="{x}" y="{y - 12}" text-anchor="middle" class="mrm" font-size="13">{i}</text>')
s.append(dots(124, y))
centers = [(196, '⌊a/2⌋'), (290, 'a'), (384, '⌊(a+b)/2⌋'), (478, 'b'), (560, '2b')]
for k, (cx, lab) in enumerate(centers):
    half = 26 if k < 4 else 22
    s.append(f'<line x1="{cx - half}" y1="{y}" x2="{cx + half}" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
    for dx in (-16, 16):
        s.append(f'<circle cx="{cx + dx}" cy="{y}" r="2.5" class="node"/>')
    s.append(f'<circle cx="{cx}" cy="{y}" r="3.5" class="accent-fill"/>')
    s.append(mtext(cx, y - 14, lab, 13))
    if k < 4:
        s.append(dots(cx + 47, y))
s.append(bracket(20, 110, y + 24, 'standard numbers'))
s.append(bracket(170, 222, y + 24, 'a block'))
s.append(f'<text x="330" y="{y + 70}" text-anchor="middle" class="label">each block is a copy of ℤ; the blocks are densely ordered, without endpoints</text>')
s.append('</svg>')
out['blocks'] = ''.join(s)


# ---------------------------------------------------------------- the cut of Parikh's theorem
s = ['<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The cut I of the proof of Parikh&apos;s theorem: the elements below the values t(a) of the terms at a; it is closed under addition and multiplication, and contains no y with theta(a, y), whose witnesses all lie above I">']
y = 70
s.append(f'<line x1="20" y1="{y}" x2="580" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<circle cx="24" cy="{y}" r="3.5" class="accent-fill"/>')
s.append(f'<text x="24" y="{y - 12}" text-anchor="middle" class="mrm" font-size="13">0</text>')
s.append(dots(70, y))
pts = [(130, 'a'), (190, 'a' + sup('2')), (245, 'a' + sup('3')), (295, 'a' + sup('4'))]
for x, lab in pts:
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="accent-fill"/>')
    s.append(mtext(x, y - 12, lab, 14))
s.append(dots(330, y))
s.append(f'<line x1="360" y1="{y - 22}" x2="360" y2="{y + 22}" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/>')
for x in (430, 490, 545):
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="node"/>')
s.append(bracket(405, 565, y - 30, 'all y with θ(a, y)', up=True))
s.append(bracket(22, 354, y + 22, 'the cut I: below some t(a)'))
s.append(bracket(366, 578, y + 22, 'M ∖ I'))
s.append('</svg>')
out['parikh-cut'] = ''.join(s)


# ---------------------------------------------------------------- Ackermann coding: binary digits, split at k = 5
c, k = 365, 5
nbits = 10
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The binary digits of c = 365 = 2 to the 5 times 11 plus 13; the set coded by c is 0, 2, 3, 5, 6, 8; the digits below position 5 are those of 13, the digits from position 5 on are those of 11, shifted by 5">']
w, x0, yb = 44, 70, 52
for j in range(nbits):
    pos = nbits - 1 - j
    x = x0 + j * w
    bit = (c >> pos) & 1
    cls = 'cell' if bit == 0 else 'cell'
    s.append(f'<rect x="{x}" y="{yb}" width="{w}" height="34" class="{cls}"/>')
    if bit:
        s.append(f'<rect x="{x + 4}" y="{yb + 4}" width="{w - 8}" height="26" class="soft-fill"/>')
    s.append(f'<text x="{x + w / 2:.1f}" y="{yb + 23}" text-anchor="middle" class="mrm" font-size="15">{bit}</text>')
    s.append(f'<text x="{x + w / 2:.1f}" y="{yb + 52}" text-anchor="middle" class="mrm" font-size="12">{pos}</text>')
split_x = x0 + (nbits - k) * w
s.append(f'<line x1="{split_x}" y1="{yb - 14}" x2="{split_x}" y2="{yb + 40}" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/>')
s.append(bracket(x0 + 2, split_x - 4, yb - 10, 'u = 11: k + j ∈ c iff j ∈ u', up=True))
s.append(bracket(split_x + 4, x0 + nbits * w - 2, yb - 10, 'q = 13: i ∈ c iff i ∈ q, for i &lt; k', up=True))
s.append(f'<text x="30" y="{yb + 52}" text-anchor="middle" class="label">position</text>')
s.append(f'<text x="300" y="{yb + 100}" text-anchor="middle" class="label">c = 365 = 2⁵ · 11 + 13, and the set coded by c is {{0, 2, 3, 5, 6, 8}}</text>')
s.append('</svg>')
out['bits'] = ''.join(s)


# ---------------------------------------------------------------- records: the proof that coded Delta_{n+1} sets give collection
f = [3, 7, 2, 9, 4, 5, 11, 6, 8, 3, 7, 5, 6, 4]
a = len(f) - 1
theta = [x for x in range(len(f)) if all(f[z] <= f[x] for z in range(x, len(f)))]
wmin = min(theta)
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="The values f(x) of the least witness function for x up to a; the points x where f(x) is at least f on the interval from x to a are highlighted; w is the least of them, and b = f(w) bounds f everywhere">']
X0, Y0, dx, dy = 60, 190, 36, 13
s.append(f'<line x1="{X0 - 10}" y1="{Y0}" x2="{X0 + dx * a + 24}" y2="{Y0}" class="axis"/>')
s.append(f'<line x1="{X0 - 10}" y1="{Y0}" x2="{X0 - 10}" y2="{Y0 - dy * 12 - 6}" class="axis"/>')
for x, v in enumerate(f):
    px, py = X0 + dx * x, Y0 - dy * v
    s.append(f'<line x1="{px}" y1="{Y0}" x2="{px}" y2="{py}" class="muted-stroke" stroke-width="1"/>')
    if x in theta:
        s.append(f'<circle cx="{px}" cy="{py}" r="4.5" class="accent-fill"/>')
    else:
        s.append(f'<circle cx="{px}" cy="{py}" r="4" class="node"/>')
bw = Y0 - dy * f[wmin]
s.append(f'<line x1="{X0 - 10}" y1="{bw}" x2="{X0 + dx * a + 24}" y2="{bw}" class="accent-stroke" stroke-width="1.2" stroke-dasharray="4 3"/>')
s.append(mtext(X0 - 22, bw + 5, 'b', 14))
s.append(mtext(X0 + dx * wmin, Y0 + 18, 'w', 14))
s.append(mtext(X0 + dx * a, Y0 + 18, 'a − 1', 14))
s.append(f'<text x="{X0 - 10}" y="{Y0 + 18}" text-anchor="middle" class="mrm" font-size="13">0</text>')
s.append(mtext(X0 - 30, Y0 - dy * 12, 'f(x)', 13))
s.append(f'<circle cx="300" cy="18" r="4.5" class="accent-fill"/><text x="310" y="22" class="label">f(x) ≥ f(x′) for all x′ ∈ [x, a)</text>')
s.append('</svg>')
out['records'] = ''.join(s)


json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
