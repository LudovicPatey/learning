# Generates the inline SVG figures of the course on jump cone avoidance.
# Usage: python3 scripts/figures/jump-cone-avoidance.py out.json
# Paste each figure into the lesson that uses it:
#   lifted-question    -> sigma2-questions.md
#   decision-tree      -> cohesiveness-second-jump.md
#   partition-regular  -> largeness.md
#   cohesive-choices   -> cohesive-classes.md
#   pigeon-condition   -> pigeonhole-forcing.md
#   case-split         -> pigeons-non-high.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def box(x, y, w, h, lines, cls='state', size=None):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>']
    n = len(lines)
    for k, t in enumerate(lines):
        ty = y + h / 2 + (k - (n - 1) / 2) * 16 + 4
        s.append(f'<text x="{x + w / 2:.1f}" y="{ty:.1f}" text-anchor="middle" class="label">{t}</text>')
    return ''.join(s)


def arrow(x1, y1, x2, y2, mid, cls='ink-stroke'):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" stroke-width="1.2" marker-end="url(#{mid})"/>'


# ---------------------------------------------------------------- the lifted question
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The two answers of the lifted question at a condition c: either some extension d and some m answer negatively about not psi(m), and an extension e forces psi(m) on all members; or every extension answers positively about every not psi(m), the conditions forcing not psi(m) are dense below c, and the generic set satisfies for all y not psi(y)">']
s.append('<defs>' + marker('jc-lq-arr') + '</defs>')
s.append(box(220, 10, 160, 40, ['condition c', 'φ = ∃y ψ(y), ψ ∈ Π⁰₁']))
s.append(box(20, 100, 240, 40, ['some d ≤ c and m with', 'd ?⊬ ¬ψ(m)'], cls='node'))
s.append(box(20, 190, 240, 40, ['e ≤ d: every member', 'of e satisfies ψ(m), hence φ']))
s.append(box(340, 100, 240, 40, ['every d ≤ c and every m:', 'd ?⊢ ¬ψ(m)'], cls='node'))
s.append(box(340, 190, 240, 40, ['for each m, forcing ¬ψ(m) is dense', 'below c: generic G satisfies ¬φ']))
s.append(arrow(270, 52, 160, 96, 'jc-lq-arr'))
s.append(arrow(330, 52, 440, 96, 'jc-lq-arr'))
s.append(arrow(140, 142, 140, 186, 'jc-lq-arr'))
s.append(arrow(460, 142, 460, 186, 'jc-lq-arr'))
s.append('<text x="150" y="80" text-anchor="end" class="label">c ?⊢ φ</text>')
s.append('<text x="450" y="80" class="label">c ?⊬ φ</text>')
s.append('</svg>')
out['lifted-question'] = ''.join(s)

# ---------------------------------------------------------------- the tree of decisions
path = [0, 1, 1]           # the path P, first three decisions
s = ['<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The binary tree of decisions: each node rho is labeled by the set R_rho; a path P is drawn in the accent color, and the condition (sigma, n) uses the reservoir R of P restricted to n">']
levels = 4
W = 600
Y0, DY = 26, 58


def nx(depth, idx):
    return 90 + (idx + 0.5) * (W - 90) / (2 ** depth)


nodes = []
for d in range(levels):
    for idx in range(2 ** d):
        nodes.append((d, idx))
on_path = set()
idx = 0
on_path.add((0, 0))
for d, b in enumerate(path):
    idx = 2 * idx + b
    on_path.add((d + 1, idx))
for d, idx in nodes:
    if d + 1 < levels:
        for b in (0, 1):
            c = (d + 1, 2 * idx + b)
            cls = 'accent-stroke' if ((d, idx) in on_path and c in on_path) else 'muted-stroke'
            sw = 2 if cls == 'accent-stroke' else 1
            s.append(f'<line x1="{nx(d, idx):.1f}" y1="{Y0 + d * DY + 10}" x2="{nx(d + 1, 2 * idx + b):.1f}" y2="{Y0 + (d + 1) * DY - 12}" class="{cls}" stroke-width="{sw}"/>')
for d, idx in nodes:
    x, y = nx(d, idx), Y0 + d * DY
    bits = format(idx, 'b').zfill(d) if d > 0 else ''
    cls = 'head-cell' if (d, idx) in on_path else 'cell'
    w = 34 + 8 * d
    s.append(f'<rect x="{x - w / 2:.1f}" y="{y - 11}" width="{w}" height="22" rx="4" class="{cls}"/>')
    label = 'ℕ' if d == 0 else bits
    if d == 0:
        s.append(f'<text x="{x:.1f}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="13">ℕ</text>')
    else:
        s.append(f'<text x="{x:.1f}" y="{y + 5}" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">{bits}</tspan></text>')
s.append(f'<text x="20" y="{Y0 + 5}" class="label">level 0</text>')
s.append(f'<text x="20" y="{Y0 + DY + 5}" class="label">split by R₀</text>')
s.append(f'<text x="20" y="{Y0 + 2 * DY + 5}" class="label">by R₁</text>')
s.append(f'<text x="20" y="{Y0 + 3 * DY + 5}" class="label">by R₂</text>')
s.append(f'<text x="300" y="{Y0 + 3 * DY + 40}" text-anchor="middle" class="label">the path P = 011⋯ (highlighted); the condition (σ, 3) has reservoir R₀₁₁ = R₀ ∩ R₁ᶜ ∩ R₂ᶜ</text>')
s.append('</svg>')
out['decision-tree'] = ''.join(s)

# ---------------------------------------------------------------- a 2-cover of a member of a partition regular class
X = [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24]
Y0set = {1, 4, 7, 9, 13, 16, 21, 24}
X0, CW = 50, 21
s = ['<svg class="fig" viewBox="0 0 600 196" width="600" role="img" aria-label="A set X in a partition regular class P, split into two parts Y0 and Y1; at least one of the parts belongs to P">']
for n in range(0, 26, 2):
    s.append(f'<text x="{X0 + n * CW + CW / 2:.1f}" y="16" text-anchor="middle" class="mrm muted" font-size="10">{n}</text>')
rows = [('X', lambda n: n in X, 'ink-fill'), ('Y₀', lambda n: n in Y0set, 'accent-fill'), ('Y₁', lambda n: n in X and n not in Y0set, 'ink-fill')]
for r, (name, pred, cls) in enumerate(rows):
    y = 40 + 40 * r
    s.append(f'<text x="{X0 - 12}" y="{y + 5}" text-anchor="end" class="math" font-size="14">{name[0]}<tspan class="mrm" font-size="10" dy="3">{name[1:]}</tspan></text>')
    s.append(f'<line x1="{X0}" y1="{y}" x2="{X0 + 26 * CW}" y2="{y}" class="axis"/>')
    for n in range(26):
        cx = X0 + n * CW + CW / 2
        if pred(n):
            s.append(f'<circle cx="{cx:.1f}" cy="{y}" r="5" class="{cls}"/>')
    s.append(f'<text x="{X0 + 26 * CW + 6}" y="{y + 5}" class="mrm muted" font-size="13">⋯</text>')
s.append('<text x="300" y="168" text-anchor="middle" class="label">X ∈ 𝒫 and X ⊆ Y₀ ∪ Y₁: then Y₀ ∈ 𝒫 or Y₁ ∈ 𝒫</text>')
s.append('<text x="300" y="186" text-anchor="middle" class="label">for the infinite sets: one part is infinite; for 𝓛<tspan font-size="9" dy="3">Z</tspan><tspan dy="-3">: one part meets Z infinitely often</tspan></text>')
s.append('</svg>')
out['partition-regular'] = ''.join(s)

# ---------------------------------------------------------------- the choices of a cohesive class
choices = [0, 1, 0, 0, 1]   # 0: intersect with L(Z_k), 1: with L(complement of Z_k)
SUB = '₀₁₂₃₄₅'
s = ['<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="A decreasing sequence of classes U_S0, U_S1, and so on; at step k the class is intersected with L of Z_k or L of the complement of Z_k, the set P choosing a large intersection">']
s.append('<defs>' + marker('jc-cc-arr', 'muted-fill') + '</defs>')
BW, GAP, BX = 70, 36, 14
for k in range(len(choices) + 1):
    x = BX + k * (BW + GAP)
    cls = 'head-cell' if k == len(choices) else 'cell'
    s.append(f'<rect x="{x}" y="70" width="{BW}" height="40" rx="6" class="{cls}"/>')
    s.append(f'<text x="{x + BW / 2}" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S{SUB[k]}</tspan></text>')
    if k < len(choices):
        side = choices[k]
        ax = x + BW + 2
        s.append(f'<line x1="{ax}" y1="90" x2="{ax + GAP - 4}" y2="90" class="muted-stroke" stroke-width="1.2" marker-end="url(#jc-cc-arr)"/>')
        cx = x + BW + GAP / 2
        up_cls = 'label' if side == 0 else 'label muted'
        dn_cls = 'label' if side == 1 else 'label muted'
        s.append(f'<text x="{cx:.1f}" y="40" text-anchor="middle" class="{up_cls}">𝓛(Z{SUB[k]})</text>')
        s.append(f'<text x="{cx:.1f}" y="146" text-anchor="middle" class="{dn_cls}">𝓛(Z{SUB[k]}ᶜ)</text>')
        mark_y = 52 if side == 0 else 128
        s.append(f'<circle cx="{cx:.1f}" cy="{mark_y}" r="4" class="accent-fill"/>')
s.append('<text x="300" y="180" text-anchor="middle" class="label">at each step, P chooses one of the two classes whose intersection with the current class is large (dot)</text>')
s.append('<text x="300" y="200" text-anchor="middle" class="label">Zᶜ is the complement of Z; the intersection of the sequence is 𝓜-cohesive</text>')
s.append('</svg>')
out['cohesive-choices'] = ''.join(s)

# ---------------------------------------------------------------- a condition of the pigeonhole forcing
N = 24
A = {0, 2, 3, 5, 8, 9, 11, 12, 14, 15, 17, 18, 20, 22, 23}
sig0 = {0, 3}
sig1 = {1, 4}
L = 6                       # min of the reservoir
Xres = {6, 8, 9, 10, 12, 13, 15, 16, 17, 19, 20, 21, 23}
X0, CW = 60, 21
s = ['<svg class="fig" viewBox="0 0 600 266" width="600" role="img" aria-label="A condition with two stems, a subset of A and a subset of its complement, and a common reservoir X; the reservoir is split by A into the parts X intersected with A0 and with A1">']
for n in range(0, N, 2):
    s.append(f'<text x="{X0 + n * CW + CW / 2:.1f}" y="16" text-anchor="middle" class="mrm muted" font-size="10">{n}</text>')
y = 34
s.append(f'<text x="{X0 - 10}" y="{y + 14}" text-anchor="end" class="math" font-size="14">A</text>')
for n in range(N):
    cls = 'cell head-cell' if n in A else 'cell'
    s.append(f'<rect x="{X0 + n * CW}" y="{y}" width="{CW}" height="20" class="{cls}"/>')
for r, (nm, sg) in enumerate([('σ₀', sig0), ('σ₁', sig1)]):
    y = 76 + 30 * r
    s.append(f'<text x="{X0 - 10}" y="{y + 14}" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">{nm[1]}</tspan></text>')
    for n in range(L):
        s.append(f'<rect x="{X0 + n * CW}" y="{y}" width="{CW}" height="20" class="cell"/>')
        s.append(f'<text x="{X0 + n * CW + CW / 2:.1f}" y="{y + 14}" text-anchor="middle" class="mrm" font-size="11">{1 if n in sg else 0}</text>')
rows = [('X', lambda n: n in Xres, 'ink-fill'), ('X ∩ A₀', lambda n: n in Xres and n in A, 'accent-fill'), ('X ∩ A₁', lambda n: n in Xres and n not in A, 'ink-fill')]
for r, (nm, pred, cls) in enumerate(rows):
    y = 160 + 26 * r
    s.append(f'<text x="{X0 - 10}" y="{y + 4}" text-anchor="end" class="label">{nm}</text>')
    s.append(f'<line x1="{X0 + L * CW}" y1="{y}" x2="{X0 + N * CW}" y2="{y}" class="axis"/>')
    for n in range(L, N):
        if pred(n):
            s.append(f'<circle cx="{X0 + n * CW + CW / 2:.1f}" cy="{y}" r="4.5" class="{cls}"/>')
    s.append(f'<text x="{X0 + N * CW + 6}" y="{y + 5}" class="mrm muted" font-size="13">⋯</text>')
s.append(f'<line x1="{X0 + L * CW}" y1="70" x2="{X0 + L * CW}" y2="220" class="ink-stroke" stroke-width="1" stroke-dasharray="4 3"/>')
s.append('<text x="300" y="248" text-anchor="middle" class="label">shaded cells: elements of A; σ₀ ⊆ A₀ = A, σ₁ ⊆ A₁ = Aᶜ; side i is valid if X ∩ Aᵢ ∈ 𝒰</text>')
s.append('</svg>')
out['pigeon-condition'] = ''.join(s)

# ---------------------------------------------------------------- the case split of the final proof
s = ['<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="The case split of the proof: if some condition has an invalid side, work on the other side with the question on one side; otherwise use the disjunctive question and Lachlan disjunction">']
s.append('<defs>' + marker('jc-cs-arr') + '</defs>')
s.append(box(170, 8, 260, 40, ['does some condition p₀', 'have an invalid side 1 − i?']))
s.append(box(20, 92, 260, 54, ['case A: work below p₀', 'side i valid in every extension', 'question on side i with a witness 𝒱'], cls='node'))
s.append(box(320, 92, 260, 54, ['case B: both sides always valid', 'disjunctive question', 'requirements on side 0 or side 1'], cls='node'))
s.append(box(20, 196, 260, 48, ['the stems on side i give an infinite', 'subset G of Aᵢ with C ≰ G′']))
s.append(box(320, 196, 260, 48, ['Lachlan’s disjunction: G₀ ⊆ A₀ with C ≰ G₀′', 'or G₁ ⊆ A₁ with C ≰ G₁′']))
s.append(arrow(260, 50, 160, 88, 'jc-cs-arr'))
s.append(arrow(340, 50, 440, 88, 'jc-cs-arr'))
s.append(arrow(150, 148, 150, 192, 'jc-cs-arr'))
s.append(arrow(450, 148, 450, 192, 'jc-cs-arr'))
s.append('<text x="200" y="74" text-anchor="end" class="label">yes</text>')
s.append('<text x="400" y="74" class="label">no</text>')
s.append('</svg>')
out['case-split'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
