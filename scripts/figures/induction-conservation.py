# Generates the inline SVG figures of the course Induction and conservation.
# Usage: python3 scripts/figures/induction-conservation.py out.json
# Paste each figure into the lesson that uses it:
#   cut             -> collection-induction.md
#   hierarchy       -> collection-induction.md
#   names           -> separations.md
#   lex-choice      -> forcing-subtrees.md
#   tower           -> harrington.md
# The output is deterministic.
import json, sys
out = {}


def sub(base, s, x, y, size=15, anchor='middle', cls='math'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size * 0.68)}" dy="4">{s}</tspan></text>')


def bracket(x1, x2, yb, text, up=False, cls='muted-stroke'):
    d = 6 if up else -6
    ty = yb - 10 if up else yb + 18
    return (f'<path d="M{x1},{yb + d} L{x1},{yb} L{x2},{yb} L{x2},{yb + d}" class="{cls}" stroke-width="1.2"/>'
            f'<text x="{(x1 + x2) / 2}" y="{ty}" text-anchor="middle" class="label">{text}</text>')


def arrow_marker(mid):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker>')


# ---------------------------------------------------------------- a failure of induction: a cut
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="A non-standard model in which a formula phi holds at 0, is preserved by successor, and fails at some non-standard numbers; the numbers below every failure form a cut, and the failures have no least element">']
y = 70
s.append(f'<line x1="20" y1="{y}" x2="166" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
for i in range(5):
    x = 30 + i * 30
    s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="accent-fill"/>')
    s.append(f'<text x="{x}" y="{y - 12}" text-anchor="middle" class="mrm" font-size="13">{i}</text>')
s.append(f'<text x="186" y="{y + 4}" text-anchor="middle" class="mrm" font-size="14">⋯</text>')
# blocks: two in the cut, two outside
blocks = [(214, True), (306, True), (420, False), (504, False)]
for cx, inside in blocks:
    s.append(f'<line x1="{cx}" y1="{y}" x2="{cx + 60}" y2="{y}" class="ink-stroke" stroke-width="1.2"/>')
    for j in range(3):
        x = cx + 10 + j * 20
        if inside:
            s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="accent-fill"/>')
        else:
            s.append(f'<circle cx="{x}" cy="{y}" r="3.5" class="node"/>')
    s.append(f'<text x="{cx + 73}" y="{y + 4}" text-anchor="middle" class="mrm" font-size="14">⋯</text>')
s.append(f'<line x1="404" y1="{y - 30}" x2="404" y2="{y + 30}" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/>')
s.append(bracket(22, 392, y + 26, 'the cut I: numbers below every failure'))
s.append(bracket(416, 584, y + 26, "failures: no least element"))
s.append(bracket(22, 170, y - 30, 'standard numbers', up=True))
s.append(f'<circle cx="150" cy="{y + 76}" r="3.5" class="accent-fill"/><text x="160" y="{y + 80}" class="label">φ holds</text>')
s.append(f'<circle cx="300" cy="{y + 76}" r="3.5" class="node"/><text x="310" y="{y + 80}" class="label">φ fails</text>')
s.append('</svg>')
out['cut'] = ''.join(s)


# ---------------------------------------------------------------- the hierarchy of induction and collection
def scheme(letter, n, x, y, size=16):
    # I Sigma_n or B Sigma_n, centered at x
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" class="mrm" font-size="{size}">{letter}Σ'
            f'<tspan font-size="{int(size * 0.68)}" dy="5">{n}</tspan></text>')


names = [('I', '0'), ('B', '1'), ('I', '1'), ('B', '2'), ('I', '2'), ('B', '3')]
w, gap, x0, yb = 62, 26, 18, 70
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="The chain I Sigma 0, B Sigma 1, I Sigma 1, B Sigma 2, I Sigma 2, B Sigma 3, each implied by the next one; the implications from B Sigma n+1 to I Sigma n are strict by the models of definable elements; RCA0 and WKL0 prove I Sigma 1, RT22 proves B Sigma 2 but not I Sigma 2">']
s.append('<defs>' + arrow_marker('ic-h-arrow') + '</defs>')
xs = []
for i, (L, n) in enumerate(names):
    x = x0 + i * (w + gap)
    xs.append(x)
    s.append(f'<rect x="{x}" y="{yb}" width="{w}" height="34" rx="4" class="cell"/>')
    s.append(scheme(L, n, x + w / 2, yb + 22))
for i in range(len(names) - 1):
    xa, xb = xs[i + 1] - 2, xs[i] + w + 2
    s.append(f'<line x1="{xa}" y1="{yb + 17}" x2="{xb + 2}" y2="{yb + 17}" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-h-arrow)"/>')
xe = xs[-1] + w + 14
s.append(f'<text x="{xe}" y="{yb + 22}" class="mrm" font-size="15">⋯</text>')
# strictness of the arrows B Sigma_{n+1} -> I Sigma_n: marks under them
for i in [1, 3, 5]:
    xm = (xs[i - 1] + w + xs[i]) / 2
    s.append(f'<line x1="{xm}" y1="{yb + 36}" x2="{xm}" y2="{yb + 52}" class="accent-stroke" stroke-width="1.2"/>')
s.append(f'<text x="{(xs[0] + xs[5]) / 2 + w / 2}" y="{yb + 68}" text-anchor="middle" class="label">strict: models of definable elements (next lesson)</text>')
for i in [2, 4]:
    xm = (xs[i - 1] + w + xs[i]) / 2
    s.append(f'<line x1="{xm}" y1="{yb - 2}" x2="{xm}" y2="{yb - 16}" class="muted-stroke" stroke-width="1.2"/>')
s.append(f'<text x="{(xs[1] + xs[4]) / 2 + w / 2}" y="{yb - 22}" text-anchor="middle" class="label">strict as well (Paris and Kirby; admitted)</text>')
# where the systems sit
yl = yb + 104
s.append(f'<text x="{xs[2] + w / 2}" y="{yl}" text-anchor="middle" class="label">RCA₀, WKL₀</text>')
s.append(f'<line x1="{xs[2] + w / 2}" y1="{yl - 14}" x2="{xs[2] + w / 2}" y2="{yb + 80}" class="muted-stroke" stroke-dasharray="2 2"/>')
s.append(f'<text x="{xs[3] + w / 2 + 10}" y="{yl}" text-anchor="middle" class="label">RT²₂ (not IΣ₂)</text>')
s.append(f'<line x1="{xs[3] + w / 2}" y1="{yl - 14}" x2="{xs[3] + w / 2}" y2="{yb + 80}" class="muted-stroke" stroke-dasharray="2 2"/>')
s.append(f'<text x="{xe + 6}" y="{yl}" text-anchor="end" class="label">ACA₀: all of them</text>')
s.append('</svg>')
out['hierarchy'] = ''.join(s)


# ---------------------------------------------------------------- definable elements and their names
s = ['<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="Below, the standard numbers, used as codes e of formulas; above, the elements of K, standard and non-standard, each the value defined by some code; all codes lie below the non-standard element b, but the values are unbounded in K">']
s.append('<defs>' + arrow_marker('ic-n-arrow') + '</defs>')
yt, ybot = 50, 150
s.append(f'<line x1="20" y1="{yt}" x2="580" y2="{yt}" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<line x1="20" y1="{ybot}" x2="580" y2="{ybot}" class="ink-stroke" stroke-width="1.2"/>')
s.append(f'<text x="24" y="{yt - 14}" class="label">values</text>')
s.append(f'<text x="24" y="{ybot - 12}" class="label">codes</text>')
# codes: standard numbers on the bottom line
codes = [40, 70, 100, 130, 160]
for i, x in enumerate(codes):
    s.append(f'<circle cx="{x}" cy="{ybot}" r="3.5" class="accent-fill"/>')
s.append(f'<text x="190" y="{ybot + 4}" class="mrm" font-size="14">⋯</text>')
s.append(bracket(30, 200, ybot + 16, 'standard numbers'))
xb = 330
s.append(f'<circle cx="{xb}" cy="{ybot}" r="4.5" class="node"/>')
s.append(f'<text x="{xb}" y="{ybot - 12}" text-anchor="middle" class="math" font-size="14">b</text>')
s.append(f'<line x1="{xb}" y1="{ybot}" x2="{xb}" y2="{yt}" class="muted-stroke" stroke-dasharray="3 3"/>')
s.append(f'<circle cx="{xb}" cy="{yt}" r="4.5" class="node"/>')
s.append(f'<text x="{xb}" y="{yt - 12}" text-anchor="middle" class="math" font-size="14">b</text>')
# values: elements of K, standard and non-standard, unbounded
vals = [40, 100, 250, 450, 560]
for x in vals:
    s.append(f'<circle cx="{x}" cy="{yt}" r="3.5" class="ink-fill"/>')
s.append(f'<text x="585" y="{yt + 4}" class="mrm" font-size="14">⋯</text>')
for i, (c, v) in enumerate(zip(codes, [250, 40, 560, 100, 450])):
    s.append(f'<line x1="{c}" y1="{ybot - 5}" x2="{v}" y2="{yt + 6}" class="ink-stroke" stroke-width="0.9" marker-end="url(#ic-n-arrow)"/>')
s.append(f'<text x="300" y="{ybot + 62}" text-anchor="middle" class="label">every element of K, below b or above it, is the value of a code below b</text>')
s.append('</svg>')
out['names'] = ''.join(s)


# ---------------------------------------------------------------- the lexicographic choice in the decision lemma
# b = 3; U = strings sigma of length 3 whose tree S_sigma is infinite (1^b always in U).
strings = [format(i, '03b') for i in range(8)]
U = {'011', '101', '110', '111'}
least = min(U)
c, x0, y0 = 60, 60, 54
s = ['<svg class="fig" viewBox="0 0 600 210" width="600" role="img" aria-label="The eight strings of length 3 in lexicographic order; those whose tree is infinite are marked; the least of them, 011, is chosen; its bit 0 at position 0 forces the formula to fail at 0, its bits 1 at positions 1 and 2 force it to hold there">']
s.append(f'<text x="{x0 - 8}" y="{y0 + 24}" text-anchor="end" class="math" font-size="15">σ</text>')
s.append(f'<text x="{x0 - 8}" y="{y0 + c + 20}" text-anchor="end" class="label">tree</text>')
for i, st in enumerate(strings):
    x = x0 + i * c
    cls = 'cell head-cell' if st == least else 'cell'
    s.append(f'<rect x="{x}" y="{y0}" width="{c}" height="36" class="{cls}"/>')
    s.append(f'<text x="{x + c / 2}" y="{y0 + 24}" text-anchor="middle" class="mrm" font-size="15">{st}</text>')
    lab = 'infinite' if st in U else 'finite'
    cl = 'label' if st in U else 'label muted'
    s.append(f'<text x="{x + c / 2}" y="{y0 + c + 20}" text-anchor="middle" class="{cl}">{lab}</text>')
xl = x0 + strings.index(least) * c + c / 2
s.append(f'<text x="{xl}" y="{y0 - 12}" text-anchor="middle" class="label">least in U</text>')
s.append(f'<line x1="{x0}" y1="{y0 + c + 34}" x2="{x0 + 8 * c}" y2="{y0 + c + 34}" class="axis"/>')
s.append(f'<text x="{x0 + 8 * c}" y="{y0 + c + 50}" text-anchor="end" class="label">lexicographic order →</text>')
s.append(f'<text x="{x0}" y="{y0 + c + 76}" class="label">bit 0 at a: every string of the tree avoids H(a, ·), so F(a, G) fails;</text>')
s.append(f'<text x="{x0}" y="{y0 + c + 94}" class="label">bit 1 at a: the smaller string with 0 at a and 1 after it is finite, so F(a, G) holds.</text>')
s.append('</svg>')
out['lex-choice'] = ''.join(s)


# ---------------------------------------------------------------- the tower of extensions in Harrington's theorem
s = ['<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="A chain of countable models M0, M1, M2, with the same numbers; at each step a path G through one tree is added; the union N is a model of WKL0">']
s.append('<defs>' + arrow_marker('ic-t-arrow') + '</defs>')
xs = [40, 170, 300, 430]
labs = ['0', '1', '2']
for i, x in enumerate(xs[:3]):
    s.append(f'<rect x="{x}" y="40" width="70" height="40" rx="4" class="cell"/>')
    s.append(sub('M', labs[i], x + 35, 66, 16))
    xa = x + 72
    xb = xs[i + 1] - 2 if i < 2 else xs[3] - 20
    s.append(f'<line x1="{xa}" y1="60" x2="{xb}" y2="60" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-t-arrow)"/>')
    s.append(f'<text x="{(xa + xb) / 2}" y="30" text-anchor="middle" class="label">add a path</text>')
s.append(f'<text x="{xs[3] - 8}" y="66" class="mrm" font-size="15">⋯</text>')
s.append(f'<rect x="{xs[3] + 30}" y="40" width="110" height="40" rx="4" class="cell head-cell"/>')
s.append(f'<text x="{xs[3] + 85}" y="66" text-anchor="middle" class="label">union N</text>')
s.append(f'<text x="300" y="110" text-anchor="middle" class="label">same numbers throughout; each step keeps Σ⁰₁ induction; the union satisfies WKL₀</text>')
s.append('</svg>')
out['tower'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
