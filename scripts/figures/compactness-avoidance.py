# Generates the inline SVG figures of the course on compactness avoidance.
# Usage: python3 scripts/figures/compactness-avoidance.py out.json
# Paste each figure into the lesson that uses it:
#   liu-valuations        -> weak-merging.md
#   splitting             -> partition-forcing.md
#   liu-structure         -> liu-theorem.md
#   avoidance-comparison  -> dnc-avoidance.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def box(x, y, w, h, lines, cls='state'):
    r = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>']
    top = y + h / 2 - 8 * (len(lines) - 1) + 4
    for i, ln in enumerate(lines):
        r.append(f'<text x="{x + w / 2:.1f}" y="{top + 16 * i:.1f}" text-anchor="middle" class="label">{ln}</text>')
    return ''.join(r)


def arrow(x1, y1, x2, y2, mid, dashed=False):
    d = ' stroke-dasharray="5 4"' if dashed else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.3"{d} '
            f'marker-end="url(#{mid})"/>')


def sub(base, idx, size=14):
    return f'{base}<tspan class="mrm" font-size="{size - 4}" dy="4">{idx}</tspan><tspan dy="-4"></tspan>'


# ---------------------------------------------------------------- Liu's lemma: safe sets and valuations
s = ['<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="The safe sets F0, F1, F2, F3 obtained by adding w0, w1, w2 one at a time, and the eight pairwise incompatible valuations with domain F3, none of which is in U">']
# left: the chain of safe sets
s.append('<text x="20" y="28" class="label">safe sets</text>')
chain = [('F₀ = ∅', 60), ('F₁ = {w₀}', 110), ('F₂ = {w₀, w₁}', 160), ('F₃ = {w₀, w₁, w₂}', 210)]
for txt, y in chain:
    s.append(f'<text x="20" y="{y}" class="label">{txt}</text>')
for (_, y1), (_, y2) in zip(chain, chain[1:]):
    s.append(f'<line x1="60" y1="{y1 + 8}" x2="60" y2="{y2 - 16}" class="muted-stroke" stroke-width="1.2"/>')
s.append('<text x="20" y="250" class="label">each step: the claim of the proof</text>')
# right: the binary tree of valuations on w0, w1, w2
X0, X1 = 250, 590
levels = [40, 100, 160, 220]
names = ['w₀', 'w₁', 'w₂']
nodes = {(): ((X0 + X1) / 2, levels[0])}
for depth in range(3):
    for path in sorted([p for p in nodes if len(p) == depth]):
        x, y = nodes[path]
        span = (X1 - X0) / 2 ** (depth + 2)
        for b in (0, 1):
            nx = x - span if b == 0 else x + span
            ny = levels[depth + 1]
            nodes[path + (b,)] = (nx, ny)
            s.append(f'<line x1="{x:.1f}" y1="{y + 4}" x2="{nx:.1f}" y2="{ny - 6}" class="ink-stroke" stroke-width="1.1"/>')
            # edge label: offset from the midpoint along the upward normal of the edge
            dx, dy = nx - x, ny - y
            norm = (dx * dx + dy * dy) ** 0.5
            ux, uy = (-dy / norm, dx / norm) if b == 0 else (dy / norm, -dx / norm)
            lx, ly = (x + nx) / 2 + 10 * ux, (y + ny) / 2 + 10 * uy
            s.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" class="mrm" font-size="12">{b}</text>')
    s.append(f'<text x="{X0 - 8}" y="{(levels[depth] + levels[depth + 1]) / 2 + 4:.1f}" text-anchor="end" class="math" font-size="13">{names[depth]}</text>')
for path, (x, y) in sorted(nodes.items()):
    if len(path) < 3:
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" class="muted-fill"/>')
    else:
        s.append(f'<rect x="{x - 9:.1f}" y="{y - 6}" width="18" height="16" class="cell head-cell"/>')
s.append(f'<text x="{(X0 + X1) / 2:.1f}" y="246" text-anchor="middle" class="label">the 2³ valuations with domain F₃:</text>')
s.append(f'<text x="{(X0 + X1) / 2:.1f}" y="262" text-anchor="middle" class="label">pairwise incompatible, none in U</text>')
s.append('</svg>')
out['liu-valuations'] = ''.join(s)

# ---------------------------------------------------------------- a splitting extension
N = 16
X = [
    [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
]


def f_of(mu):
    for s_ in range(len(mu)):
        for t in range(s_ + 1, len(mu)):
            if mu[s_] == mu[t]:
                return mu[s_], s_, t
    raise ValueError


XL, CW = 92, 30
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="A splitting extension with k equal to 2: three partitions X0, X1, X2 of the numbers 0 to 15 into two parts give the refined partition whose part of n is the triple of the values of X0, X1, X2 at n; the map f sends each triple to a value repeated in it">']
for n in range(N):
    s.append(f'<text x="{XL + n * CW + CW / 2:.1f}" y="18" text-anchor="middle" class="mrm muted" font-size="11">{n}</text>')
for r, row in enumerate(X):
    y = 30 + r * 30
    s.append(f'<text x="{XL - 10}" y="{y + 16}" text-anchor="end" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="4">{r}</tspan></text>')
    for n, v in enumerate(row):
        cls = 'cell head-cell' if v == 1 else 'cell'
        s.append(f'<rect x="{XL + n * CW}" y="{y}" width="{CW}" height="22" class="{cls}"/>')
        s.append(f'<text x="{XL + n * CW + CW / 2:.1f}" y="{y + 16}" text-anchor="middle" class="mrm" font-size="12">{v}</text>')
y = 132
s.append(f'<text x="{XL - 10}" y="{y + 16}" text-anchor="end" class="math" font-size="14">Y</text>')
for n in range(N):
    mu = tuple(X[r][n] for r in range(3))
    s.append(f'<rect x="{XL + n * CW}" y="{y}" width="{CW}" height="22" class="cell"/>')
    s.append(f'<text x="{XL + n * CW + CW / 2:.1f}" y="{y + 16}" text-anchor="middle" class="mrm" font-size="10">{"".join(map(str, mu))}</text>')
y = 172
s.append(f'<text x="{XL - 10}" y="{y + 16}" text-anchor="end" class="math" font-size="14">f(μ)</text>')
for n in range(N):
    mu = tuple(X[r][n] for r in range(3))
    v, _, _ = f_of(mu)
    cls = 'cell head-cell' if v == 1 else 'cell'
    s.append(f'<rect x="{XL + n * CW}" y="{y}" width="{CW}" height="22" class="{cls}"/>')
    s.append(f'<text x="{XL + n * CW + CW / 2:.1f}" y="{y + 16}" text-anchor="middle" class="mrm" font-size="12">{v}</text>')
s.append('<text x="20" y="222" class="label">Y(n) = (X₀(n), X₁(n), X₂(n)) is the part of n in the refined partition (8 parts);</text>')
s.append('<text x="20" y="240" class="label">part μ inherits the stem of part f(μ), a value taken twice by μ</text>')
s.append('</svg>')
out['splitting'] = ''.join(s)

# ---------------------------------------------------------------- structure of the proof of Liu's theorem
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Structure of the proof of Liu theorem: a computable coloring of pairs, a cohesive set by PA avoidance of COH, a stable coloring and its limit set, an infinite subset of the limit set or its complement by strong PA avoidance of the pigeonhole principle, which uses the Ramsey-type weak Konig lemma and Liu lemma, and finally a homogeneous set">']
s.append('<defs>' + marker('ca-st-arr') + '</defs>')
s.append(box(20, 20, 170, 46, ['f : [ℕ]² → 2', 'computable in Z']))
s.append(box(215, 20, 170, 46, ['cohesive set G', 'COH, PA avoidance']))
s.append(box(410, 20, 170, 46, ['limit set of the', 'stable coloring on G']))
s.append(box(410, 126, 170, 46, ['K ⊆ limit set or its', 'complement: RT¹₂ strong']))
s.append(box(410, 232, 170, 46, ['homogeneous set H', 'Z ⊕ H not PA over D']))
s.append(box(150, 126, 200, 46, ['weakly merging question', 'for RT¹₂ (Liu forcing)'], 'cell'))
s.append(box(20, 232, 170, 46, ['RWKL avoids PA', '(partition forcing)'], 'cell'))
s.append(box(215, 232, 170, 46, ["Liu's lemma", 'on valuations'], 'cell'))
s.append(arrow(192, 43, 211, 43, 'ca-st-arr'))
s.append(arrow(387, 43, 406, 43, 'ca-st-arr'))
s.append(arrow(495, 68, 495, 122, 'ca-st-arr'))
s.append(arrow(495, 174, 495, 228, 'ca-st-arr'))
s.append(arrow(352, 149, 406, 149, 'ca-st-arr'))
s.append(arrow(105, 230, 200, 176, 'ca-st-arr'))
s.append(arrow(300, 230, 270, 176, 'ca-st-arr'))
s.append(arrow(213, 255, 194, 255, 'ca-st-arr', dashed=True))
s.append('<text x="300" y="104" text-anchor="middle" class="label">each step keeps Z ⊕ (sets built) not PA relative to D</text>')
s.append('<text x="202" y="292" text-anchor="middle" class="label muted">dashed: RWKL avoidance uses Liu\'s lemma too</text>')
s.append('</svg>')
out['liu-structure'] = ''.join(s)

# ---------------------------------------------------------------- comparison of avoidance properties
s = ['<svg class="fig" viewBox="0 0 600 340" width="600" role="img" aria-label="Constant-bound trace avoidance implies PA avoidance, which implies cone avoidance; DNC avoidance implies cone avoidance. WWKL has PA avoidance but not c.b. trace avoidance; WKL has cone avoidance but not PA avoidance; RT22 has cone avoidance but not DNC avoidance. Finitely merging, merging and countably merging questions give c.b. trace, PA and DNC avoidance; countable merging also gives preservation of immunity">']
s.append('<defs>' + marker('ca-cmp-arr') + '</defs>')
s.append('<text x="105" y="18" text-anchor="middle" class="label muted">property of the question</text>')
s.append('<text x="410" y="18" text-anchor="middle" class="label muted">avoidance property</text>')
s.append(box(20, 30, 170, 40, ['finitely merging'], 'cell'))
s.append(box(20, 130, 170, 40, ['merging'], 'cell'))
s.append(box(20, 230, 170, 40, ['countably merging'], 'cell'))
s.append(box(330, 30, 160, 40, ['c.b. trace avoidance']))
s.append(box(330, 130, 160, 40, ['PA avoidance']))
s.append(box(330, 230, 160, 40, ['cone avoidance']))
s.append(box(510, 130, 80, 40, ['DNC', 'avoidance']))
s.append(arrow(192, 50, 326, 50, 'ca-cmp-arr'))
s.append(arrow(192, 150, 326, 150, 'ca-cmp-arr'))
s.append(arrow(410, 72, 410, 126, 'ca-cmp-arr'))
s.append(arrow(410, 172, 410, 226, 'ca-cmp-arr'))
s.append(arrow(530, 172, 472, 228, 'ca-cmp-arr'))
s.append('<path d="M192,262 C300,330 610,320 584,176" class="ink-stroke" stroke-width="1.3" fill="none" marker-end="url(#ca-cmp-arr)"/>')
s.append('<text x="418" y="104" class="label">converse fails: WWKL</text>')
s.append('<text x="402" y="204" text-anchor="end" class="label">converse fails: WKL</text>')
s.append('<text x="512" y="204" class="label">converse</text>')
s.append('<text x="512" y="219" class="label">fails: RT²₂</text>')
s.append('<text x="380" y="330" text-anchor="middle" class="label">countable merging also preserves immunity</text>')
s.append('</svg>')
out['avoidance-comparison'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
