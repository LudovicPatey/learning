# Generates the inline SVG figures of the course Recursive saturation.
# Usage: python3 scripts/figures/recursive-saturation.py out.json
# Paste each figure into the lesson that uses it (placeholder {{FIG:name}}):
#   zigzag     -> back-and-forth.md
#   friedman   -> friedman-embedding.md
#   smorynski  -> automorphisms.md
#   ranks      -> satisfaction-classes.md
#   lachlan    -> lachlan.md
# The output is deterministic.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def mtext(x, y, body, size=14, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="math" font-size="{size}">{body}</text>'


def label(x, y, body, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="label">{body}</text>'


def dot(x, y, cls='accent-fill', r=3.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}"/>'


def line(x1, y1, x2, y2, cls='ink-stroke', w=1.2, dash=None, mark=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = f' marker-end="url(#{mark})"' if mark else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" stroke-width="{w}"{d}{m}/>'


def sub(base, s, size=14):
    return f'{base}<tspan class="mrm" font-size="{size - 4}" dy="3">{s}</tspan>'


def cutmark(x, y, h=22):
    return line(x, y - h, x, y + h, 'accent-stroke', 1.6, '4 3')


# ---------------------------------------------------------------- back-and-forth
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="Back-and-forth between M and N: forth steps send the next element of M to an element of N with the same type over the previous ones, back steps find a preimage in M for the next element of N">',
     '<defs>' + marker('rs-zz') + '</defs>']
yM, yN = 50, 150
s.append(line(40, yM, 570, yM))
s.append(line(40, yN, 570, yN))
s.append(mtext(22, yM + 5, 'M', 15))
s.append(mtext(22, yN + 5, 'N', 15))
pairs = [(90, 300, 'f'), (450, 140, 'b'), (230, 490, 'f'), (360, 220, 'b'), (520, 400, 'f')]
for k, (xm, xn, kind) in enumerate(pairs):
    s.append(dot(xm, yM, 'accent-fill'))
    s.append(dot(xn, yN, 'accent-fill'))
    if kind == 'f':
        s.append(line(xm, yM + 6, xn, yN - 7, 'ink-stroke', 1.3, None, 'rs-zz'))
    else:
        s.append(line(xn, yN - 6, xm, yM + 7, 'ink-stroke', 1.3, '5 3', 'rs-zz'))
    s.append(mtext(xm, yM - 12, sub('r', str(k), 13), 13))
    s.append(mtext(xn, yN + 22, sub('s', str(k), 13), 13))
s.append(label(300, 185, 'solid: forth (next element of M); dashed: back (next element of N)'))
s.append('</svg>')
out['zigzag'] = ''.join(s)


# ---------------------------------------------------------------- Friedman's embedding
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Friedman embedding: M is mapped onto a proper initial segment of N lying below an element d; forth steps send elements of M below d, back steps give preimages to elements of N below the image">',
     '<defs>' + marker('rs-fe') + '</defs>']
yM, yN = 50, 140
s.append(line(40, yM, 570, yM))
s.append(line(40, yN, 570, yN))
s.append(mtext(22, yM + 5, 'M', 15))
s.append(mtext(22, yN + 5, 'N', 15))
s.append(dot(44, yM, 'ink-fill', 3))
s.append(dot(44, yN, 'ink-fill', 3))
for xm, xn in ((120, 90), (250, 160), (400, 230), (530, 290)):
    s.append(dot(xm, yM, 'accent-fill'))
    s.append(dot(xn, yN, 'accent-fill'))
    s.append(line(xm, yM + 6, xn, yN - 7, 'ink-stroke', 1.2, None, 'rs-fe'))
s.append(cutmark(330, yN, 16))
s.append(f'<path d="M44,{yN + 22} L44,{yN + 28} L326,{yN + 28} L326,{yN + 22}" class="muted-stroke" stroke-width="1.2"/>')
s.append(label(185, yN + 46, 'the image f[M]: a proper initial segment'))
s.append(dot(450, yN, 'ink-fill', 4))
s.append(mtext(450, yN - 12, 'd', 14))
s.append(label(450, yN + 46, 'all of f[M] and its Σ₁ witnesses lie below d'))
s.append('</svg>')
out['friedman'] = ''.join(s)


# ---------------------------------------------------------------- Smorynski
s = ['<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="An automorphism g fixing the exponential cut I pointwise and moving some element below every element above I">',
     '<defs>' + marker('rs-sm', 'accent-fill') + '</defs>']
y = 90
s.append(line(20, y, 580, y))
for x in (40, 80, 120, 160, 200, 240):
    s.append(dot(x, y, 'muted-fill', 3))
    s.append(f'<path d="M{x - 6},{y - 6} C{x - 8},{y - 26} {x + 8},{y - 26} {x + 6},{y - 8}" class="muted-stroke" fill="none" stroke-width="1"/>')
s.append(cutmark(280, y))
s.append(mtext(280, y + 38, 'I', 14))
for x1, x2 in ((320, 350), (400, 380), (450, 500), (540, 520)):
    s.append(dot(x1, y, 'accent-fill'))
    s.append(dot(x2, y, 'node', 3))
    s.append(f'<path d="M{x1},{y - 7} Q{(x1 + x2) / 2},{y - 40} {x2},{y - 8}" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#rs-sm)"/>')
s.append(label(140, y + 40, 'below I: g(x) = x'))
s.append(label(440, y + 40, 'above I: moved points below every element'))
s.append('</svg>')
out['smorynski'] = ''.join(s)


# ---------------------------------------------------------------- ranks in Enayat-Visser
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="A finite set of formulas ordered by the direct subformula relation, with ranks 0 to 3; the sets U are defined rank by rank, from S0 at rank 0 for formulas of F0 and by the Tarski clauses above">']
nodes = {'a': (110, 190, 0, 'in F₀: from S₀'), 'b': (250, 190, 0, 'atomic: by its clause'), 'c': (430, 190, 0, 'other: ∅'),
         'd': (180, 130, 1, ''), 'e': (430, 130, 1, ''), 'f': (300, 70, 2, ''), 'g': (300, 20, 3, '')}
edges = [('d', 'a'), ('d', 'b'), ('e', 'c'), ('f', 'd'), ('f', 'e'), ('g', 'f')]
for u, v in edges:
    (x1, y1, _, _), (x2, y2, _, _) = nodes[u], nodes[v]
    s.append(line(x1, y1 + 6, x2, y2 - 6, 'muted-stroke', 1.2))
for k, (x, yy, r, txt) in nodes.items():
    s.append(dot(x, yy, 'accent-fill' if r == 0 else 'node', 4.5))
    if txt:
        s.append(label(x, yy + 24, txt))
for r, yy in ((0, 190), (1, 130), (2, 70), (3, 20)):
    s.append(label(560, yy + 4, f'rank {r}', 'end'))
s.append(label(80, 70, 'above rank 0:', 'start'))
s.append(label(80, 86, 'by the Tarski clauses', 'start'))
s.append('</svg>')
out['ranks'] = ''.join(s)


# ---------------------------------------------------------------- Lachlan
s = ['<svg class="fig" viewBox="0 0 600 210" width="600" role="img" aria-label="The sets B_i along the indices: B_i equals A_i for standard i; at a non-standard index nu, B_nu is A_m, and each step down lowers m by one until A_1 is reached at a non-standard index, which is impossible">',
     '<defs>' + marker('rs-la') + '</defs>']
y = 120
s.append(line(20, y, 580, y))
for k, x in enumerate((40, 90, 140, 190)):
    s.append(dot(x, y, 'accent-fill'))
    s.append(mtext(x, y + 22, sub('B', str(k), 13), 13))
    s.append(mtext(x, y - 14, sub('A', str(k), 13), 13))
s.append(label(115, y + 50, 'standard indices: Bᵢ = Aᵢ'))
s.append(cutmark(260, y, 18))
s.append(mtext(260, y + 40, 'ℕ', 13))
xs = (360, 420, 480, 540)
labs = ('A<tspan class="mrm" font-size="10" dy="3">1</tspan>', 'A<tspan class="mrm" font-size="10" dy="3">2</tspan>', '⋯', 'A<tspan class="mrm" font-size="10" dy="3">m</tspan>')
idx = ('ν−m+1', '', '', 'ν')
for x, lb, ix in zip(xs, labs, idx):
    s.append(dot(x, y, 'node', 3.5))
    s.append(mtext(x, y - 14, lb, 13))
    if ix:
        s.append(f'<text x="{x}" y="{y + 22}" text-anchor="middle" class="math" font-size="13">{ix}</text>')
for x1, x2 in ((540, 480), (480, 420), (420, 360)):
    s.append(f'<path d="M{x1},{y - 30} Q{(x1 + x2) / 2},{y - 58} {x2 + 4},{y - 32}" class="ink-stroke" fill="none" stroke-width="1.2" marker-end="url(#rs-la)"/>')
s.append(label(450, y - 70, 'each step down lowers the index by one'))
s.append(label(450, y + 50, 'at a non-standard index, A₁ cannot occur'))
s.append('</svg>')
out['lachlan'] = ''.join(s)


json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
