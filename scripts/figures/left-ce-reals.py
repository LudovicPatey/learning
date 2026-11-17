# Generates the inline SVG figures of the course on left-c.e. reals and Ω.
# Usage: python3 scripts/figures/left-ce-reals.py out.json
# Paste each figure into the lesson that uses it:
#   kucera-slaman-test                -> kucera-slaman.md
#   dhn-procedure                     -> random-sums.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, index, size=14):
    return f'<text x="{{x}}" y="{{y}}" text-anchor="middle" class="math" font-size="{size}">{base}<tspan font-size="{size - 4}" dy="4">{index}</tspan></text>'


# ---------------------------------------------------------------- the Kučera–Slaman test
# Active stages: position of the approximation and length of the interval placed above it.
stages = [(80, 90, 's₀', 'β_s₀ − β₀'), (230, 140, 's₁', 'β_s₁ − β_s₀'), (420, 60, 's₂', 'β_s₂ − β_s₁')]
y = 110
s = ['<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="On a line, the approximations alpha at stages s zero, s one, s two increase; above each, an interval of length 2 to the minus n times the increment of beta; each next approximation lies beyond the previous interval">']
s.append('<defs>' + marker('ks-arrow') + '</defs>')
s.append(f'<line x1="30" y1="{y}" x2="570" y2="{y}" class="axis"/>')
for x, w, _, _ in stages:
    s.append(f'<rect x="{x}" y="{y - 10}" width="{w}" height="20" class="soft-fill"/>')
for x, w, st, _ in stages:
    s.append(f'<circle cx="{x}" cy="{y}" r="4" class="ink-fill"/>')
    s.append(f'<text x="{x}" y="{y + 30}" text-anchor="middle" class="math" font-size="14">α<tspan font-size="10" dy="4">{st}</tspan></text>')
s.append(f'<circle cx="530" cy="{y}" r="4" class="accent-fill"/>')
s.append(f'<text x="530" y="{y + 30}" text-anchor="middle" class="math" font-size="14">α</text>')
for x, w, _, lab in stages:
    s.append(f'<text x="{x + w / 2:g}" y="{y - 20}" text-anchor="middle" class="label">2⁻ⁿ({lab})</text>')
for (x0, w0, _, _), (x1, _, _, _) in zip(stages, stages[1:]):
    mid0, mid1 = x0 + (x1 - x0) / 3, x0 + 2 * (x1 - x0) / 3
    s.append(f'<path d="M{x0},58 C{mid0 + 0:g},{30 if x1 - x0 < 170 else 28} {mid1:g},{30 if x1 - x0 < 170 else 28} {x1 - 2},52" class="muted-stroke" stroke-width="1.1" marker-end="url(#ks-arrow)"/>')
s.append('<text x="300" y="176" text-anchor="middle" class="label">shaded: the class U_n; α ∉ U_n, so every approximation outside U_n eventually jumps past the last interval</text>')
s.append('</svg>')
out['kucera-slaman-test'] = ''.join(s)

# ---------------------------------------------------------------- the procedure of Downey, Hirschfeldt and Nies
alphas = [(140, 's'), (200, 's+1'), (240, 's+2'), (300, 's+3')]
tiles = [(100, 90), (190, 60), (250, 90)]
s = ['<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="Two lines: the upper shows the approximations of alpha inside the interval I i at stages s, s plus one, and so on; the lower shows beta s and consecutive intervals J of lengths k times the increments of alpha, covering up to beta s plus k times alpha minus alpha s, which contains beta">']
s.append('<defs>' + marker('dhn-arrow') + '</defs>')
s.append('<text x="20" y="40" class="label">α</text><line x1="40" y1="60" x2="570" y2="60" class="axis"/>')
s.append('<rect x="90" y="50" width="420" height="20" class="soft-fill"/><text x="300" y="44" text-anchor="middle" class="label">I_i</text>')
for x, _ in alphas:
    s.append(f'<circle cx="{x}" cy="60" r="3.5" class="ink-fill"/>')
s.append('<circle cx="420" cy="60" r="4.5" class="accent-fill"/>')
for x, st in alphas:
    s.append(f'<text x="{x}" y="88" text-anchor="middle" class="math" font-size="13">α<tspan font-size="9" dy="3">{st}</tspan></text>')
s.append('<text x="420" y="88" text-anchor="middle" class="math" font-size="13">α</text>')
s.append('<text x="20" y="150" class="label">β</text><line x1="40" y1="170" x2="570" y2="170" class="axis"/>')
for x, w in tiles:
    s.append(f'<rect x="{x}" y="160" width="{w}" height="20" class="cell head-cell"/>')
s.append('<circle cx="100" cy="170" r="3.5" class="ink-fill"/><text x="100" y="198" text-anchor="middle" class="math" font-size="13">β<tspan font-size="9" dy="3">s</tspan></text>')
s.append('<circle cx="300" cy="170" r="4.5" class="accent-fill"/><text x="300" y="198" text-anchor="middle" class="math" font-size="13">β</text>')
s.append('<text x="145" y="154" text-anchor="middle" class="label">k(α_s+1 − α_s)</text><text x="300" y="154" text-anchor="middle" class="label">…</text>')
s.append('<line x1="140" y1="96" x2="104" y2="156" class="muted-stroke" stroke-dasharray="3 3"/>')
s.append('<text x="470" y="198" text-anchor="middle" class="label">s ∈ S: β − β_s &lt; k(α − α_s)</text>')
s.append('</svg>')
out['dhn-procedure'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
