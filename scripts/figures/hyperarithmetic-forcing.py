# Generates the inline SVG figures of the course on forcing over the hyperarithmetic sets.
# Usage: python3 scripts/figures/hyperarithmetic-forcing.py out.json
# Paste each figure into the lesson that uses it:
#   fusion                            -> minimal-hyperdegree.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

# ---------------------------------------------------------------- the fusion sequence of lem-hyp-fusion
W, X0 = 520, 40
levels = 4
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="Nested conditions: the condition P at the top is split into two disjoint conditions Q(1,0) and Q(1,1), each forcing phi 0; each of them is split again into two conditions forcing phi 1, and so on; the limit Q is the class of sets lying in one condition at every level">']
for i in range(levels):
    n = 2 ** i
    w = W / n
    y = 30 + 48 * i
    for j in range(n):
        x = X0 + j * w + 4 * i
        cls = 'cell head-cell' if i == 0 else ('soft-fill' if i % 2 else 'cell')
        s.append(f'<rect x="{x:.1f}" y="{y}" width="{w - 8 * i:.1f}" height="26" rx="3" class="{cls}"/>')
        if i <= 2:
            lab = 'P = Q₀,₀' if i == 0 else f'Q{"₀₁₂₃"[i]},{"₀₁₂₃₄₅₆₇"[j]}'
            s.append(f'<text x="{x + (w - 8 * i) / 2:.1f}" y="{y + 18}" text-anchor="middle" class="label">{lab}</text>')
    if i:
        s.append(f'<text x="{X0 + W + 6}" y="{y + 18}" class="label">⊩ φ{"₀₁₂"[i - 1]}</text>')
s.append('<text x="300" y="222" text-anchor="middle" class="label">Q = the sets that lie in some condition of every level: a hyperarithmetic perfect class forcing every φᵢ</text>')
s.append('</svg>')
out['fusion'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
