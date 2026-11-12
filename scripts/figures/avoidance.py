# Generates the inline SVG figures of the course on cone avoidance and the forcing question.
# Usage: python3 scripts/figures/avoidance.py out.json
# Paste each figure into the lesson that uses it:
#   dividing-line        -> forcing-question-method.md
#   seetapun-condition   -> seetapun-forcing.md
#   avoidance-relations  -> hyperimmunities.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


# ---------------------------------------------------------------- the dividing line of a forcing question
L, M1, M2, R = 40, 200, 400, 560
s = ['<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="The conditions are divided into those forcing phi, those forcing its negation, and those deciding neither; the Jockusch-Soare question answers yes only on the first part, the Cohen question on the first two parts">']
s.append('<defs>' + marker('av-dl-arr', 'accent-fill') + '</defs>')
s.append(f'<rect x="{L}" y="70" width="{M1 - L}" height="36" class="cell head-cell"/>')
s.append(f'<rect x="{M1}" y="70" width="{M2 - M1}" height="36" class="cell"/>')
s.append(f'<rect x="{M2}" y="70" width="{R - M2}" height="36" class="state"/>')
s.append(f'<text x="{(L + M1) / 2}" y="93" text-anchor="middle" class="label">c ⊩ φ</text>')
s.append(f'<text x="{(M1 + M2) / 2}" y="93" text-anchor="middle" class="label">c forces neither φ nor ¬φ</text>')
s.append(f'<text x="{(M2 + R) / 2}" y="93" text-anchor="middle" class="label">c ⊩ ¬φ</text>')
for x, name in ((M1, 'Jockusch–Soare question'), (M2, 'Cohen question')):
    s.append(f'<line x1="{x}" y1="48" x2="{x}" y2="128" class="ink-stroke" stroke-width="1.4" stroke-dasharray="5 4"/>')
    s.append(f'<text x="{x}" y="38" text-anchor="middle" class="label">{name}</text>')
for y, x2, txt in ((156, M1, 'Jockusch–Soare: yes'), (196, M2, 'Cohen: yes')):
    s.append(f'<line x1="{L}" y1="{y}" x2="{x2}" y2="{y}" class="accent-stroke" stroke-width="2" marker-start="url(#av-dl-arr)" marker-end="url(#av-dl-arr)"/>')
    s.append(f'<text x="{(L + x2) / 2}" y="{y - 7}" text-anchor="middle" class="label">{txt}</text>')
    s.append(f'<text x="{(x2 + R) / 2}" y="{y - 7}" text-anchor="middle" class="label muted">no</text>')
s.append(f'<text x="300" y="228" text-anchor="middle" class="label">conditions, for a fixed Σ⁰₁ sentence φ</text>')
s.append('</svg>')
out['dividing-line'] = ''.join(s)

# ---------------------------------------------------------------- a condition of the Seetapun forcing
X0, CW = 60, 21          # left edge and cell width
N = 24                   # positions 0..23
STEM = 6                 # |sigma_0| = |sigma_1| = 6
ELL = 14                 # the bound l of the positive answer
sigma0 = [1, 4]
sigma1 = [2]
X = [7, 8, 10, 11, 13, 15, 16, 18, 19, 21, 22]
F = [x for x in X if x < ELL]
beta = {7: 0, 8: 1, 10: 0, 11: 1, 13: 0}     # the color f({a, y}) for y in Y
Y = [16, 19, 22]


def cx(n):
    return X0 + n * CW + CW / 2


s = ['<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="A condition of the Seetapun forcing: two stems, homogeneous for colors 0 and 1, and a reservoir; for a positive answer, the finite part of the reservoir below l is split according to the colors towards a thinned reservoir Y above l">']
for n in range(0, N, 2):
    s.append(f'<text x="{cx(n):.1f}" y="18" text-anchor="middle" class="mrm muted" font-size="10">{n}</text>')
rows = [(48, 'σ₀', sigma0), (82, 'σ₁', sigma1)]
for y, lab, elems in rows:
    s.append(f'<text x="{X0 - 10}" y="{y + 4}" text-anchor="end" class="math" font-size="14">{lab[0]}<tspan class="mrm" font-size="10" dy="3">{lab[1]}</tspan></text>')
    for n in range(STEM):
        cls = 'cell head-cell' if n in elems else 'cell'
        s.append(f'<rect x="{X0 + n * CW}" y="{y - 10}" width="{CW}" height="20" class="{cls}"/>')
        s.append(f'<text x="{cx(n):.1f}" y="{y + 4}" text-anchor="middle" class="mrm" font-size="11">{1 if n in elems else 0}</text>')
# the reservoir, shared by the two stems
y = 116
s.append(f'<text x="{X0 - 10}" y="{y + 4}" text-anchor="end" class="math" font-size="14">X</text>')
for n in range(STEM, N):
    if n in X:
        s.append(f'<circle cx="{cx(n):.1f}" cy="{y}" r="5" class="accent-fill"/>')
    else:
        s.append(f'<circle cx="{cx(n):.1f}" cy="{y}" r="2" class="muted-fill"/>')
s.append(f'<text x="{X0 + N * CW + 6}" y="{y + 4}" class="mrm muted" font-size="13">⋯</text>')
# after a positive answer: F split by colors, Y thinned above l
y = 176
s.append(f'<text x="{X0 - 10}" y="{y + 4}" text-anchor="end" class="label">split</text>')
for n in range(STEM, N):
    if n in F:
        s.append(f'<rect x="{X0 + n * CW + 1}" y="{y - 10}" width="{CW - 2}" height="20" class="cell"/>')
        s.append(f'<text x="{cx(n):.1f}" y="{y + 4}" text-anchor="middle" class="mrm" font-size="11">{beta[n]}</text>')
    elif n in Y:
        s.append(f'<circle cx="{cx(n):.1f}" cy="{y}" r="5" class="accent-fill"/>')
    elif n >= ELL and n in X:
        s.append(f'<circle cx="{cx(n):.1f}" cy="{y}" r="5" class="muted-stroke" fill="none"/>')
    else:
        s.append(f'<circle cx="{cx(n):.1f}" cy="{y}" r="2" class="muted-fill"/>')
s.append(f'<text x="{X0 + N * CW + 6}" y="{y + 4}" class="mrm muted" font-size="13">⋯</text>')
xl = X0 + ELL * CW
s.append(f'<line x1="{xl}" y1="100" x2="{xl}" y2="196" class="ink-stroke" stroke-width="1.2" stroke-dasharray="4 3"/>')
s.append(f'<text x="{xl + 4}" y="104" class="math" font-size="13">ℓ</text>')
s.append('<text x="60" y="222" class="label">σ₀ is homogeneous for color 0, σ₁ for color 1; every y ∈ X has color i with all of σᵢ</text>')
s.append('<text x="60" y="242" class="label">split: each a ∈ X below ℓ has the shown color with every y ∈ Y (filled); open circles leave the reservoir</text>')
s.append('</svg>')
out['seetapun-condition'] = ''.join(s)

# ---------------------------------------------------------------- relations between avoidance properties
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Relations between the avoidance properties of a problem: strong cone avoidance implies cone avoidance; cone avoidance is equivalent to preservation of one non-Sigma01 definition and to preservation of one hyperimmunity; forcing questions with the right properties give each preservation property">']
s.append('<defs>' + marker('av-rel-arr') + '</defs>')


def box(x, y, w, h, lines, cls='state'):
    r = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>']
    top = y + h / 2 - 8 * (len(lines) - 1) + 4
    for i, ln in enumerate(lines):
        r.append(f'<text x="{x + w / 2}" y="{top + 16 * i}" text-anchor="middle" class="label">{ln}</text>')
    return ''.join(r)


def arrow(x1, y1, x2, y2, dashed=False):
    d = ' stroke-dasharray="5 4"' if dashed else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.3"{d} '
            f'marker-end="url(#av-rel-arr)"/>')


s.append(box(225, 14, 150, 40, ['strong cone avoidance']))
s.append(box(225, 112, 150, 40, ['cone avoidance']))
s.append(box(10, 104, 170, 56, ['preservation of 1', 'non-Σ⁰₁ definition']))
s.append(box(420, 104, 170, 56, ['preservation of 1', 'hyperimmunity']))
s.append(box(10, 222, 170, 56, ['Σ⁰₁-preserving', 'forcing question'], 'cell'))
s.append(box(420, 222, 170, 56, ['Σ⁰₁-preserving compact', 'forcing question'], 'cell'))
s.append(arrow(300, 56, 300, 108))
# non-Sigma01 <-> cone
s.append(arrow(182, 124, 221, 124))
s.append(arrow(223, 140, 184, 140, dashed=True))
# hyperimmunity <-> cone
s.append(arrow(418, 124, 379, 124))
s.append(arrow(377, 140, 416, 140, dashed=True))
s.append(arrow(95, 220, 95, 164))
s.append(arrow(505, 220, 505, 164))
s.append('<line x1="200" y1="262" x2="240" y2="262" class="ink-stroke" stroke-width="1.3"/>')
s.append('<text x="248" y="266" class="label">proved in the course</text>')
s.append('<line x1="200" y1="284" x2="240" y2="284" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4"/>')
s.append('<text x="248" y="288" class="label">admitted (Downey et al.)</text>')
s.append('</svg>')
out['avoidance-relations'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
