# Generates the inline SVG figures of the course Oracles and Turing degrees.
# Usage: python3 scripts/figures/turing-degrees.py out.json
import json, sys
out = {}

def sub(base, s, x, y, size=16, anchor='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

# ---------------------------------------------------------------- oracle machine and use
s = ['<svg class="fig" viewBox="0 0 600 254" width="600" role="img" aria-label="An oracle machine: a work tape, a read-only oracle tape holding the bits of X, and a finite control; the cells read form the use">']
w = 34
# work tape
s.append('<text x="10" y="44" class="label">work tape</text>')
work = ['⊔', '1', '1', '1', '⊔', '1', '1', '⊔', '⊔', '⊔']
for i, c in enumerate(work):
    x = 120 + i * w
    s.append(f'<rect x="{x}" y="24" width="{w}" height="{w}" class="{"cell head-cell" if i == 3 else "cell"}"/>')
    s.append(f'<text x="{x + w/2}" y="47" text-anchor="middle" class="mrm{" muted" if c == "⊔" else ""}" font-size="16">{c}</text>')
s.append(f'<text x="{120 + len(work)*w + 8}" y="47" class="mrm muted" font-size="16">⋯</text>')
# oracle tape
s.append('<text x="10" y="196" class="label">oracle tape</text>')
bits = '0110100101'
for i, b in enumerate(bits):
    x = 120 + i * w
    read = i < 5
    s.append(f'<rect x="{x}" y="176" width="{w}" height="{w}" class="{"cell head-cell" if i == 4 else "cell"}"/>')
    s.append(f'<text x="{x + w/2}" y="199" text-anchor="middle" class="mrm{"" if read else " muted"}" font-size="16">{b}</text>')
    s.append(f'<text x="{x + w/2}" y="226" text-anchor="middle" class="mrm muted" font-size="11">{i}</text>')
s.append(f'<text x="{120 + len(bits)*w + 8}" y="199" class="mrm muted" font-size="16">⋯</text>')
# use bracket
s.append(f'<path d="M122,240 L122,246 L{120 + 5*w - 2},246 L{120 + 5*w - 2},240" class="accent-stroke" stroke-width="1.4"/>')
s.append(f'<text x="{120 + 5*w + 8}" y="248" class="label">cells read so far: the use</text>')
# finite control
cx = 120 + 3 * w + w / 2
s.append(f'<rect x="{cx - 60}" y="90" width="150" height="54" rx="8" class="soft-fill accent-stroke" stroke-width="1.3"/>')
s.append(f'<text x="{cx + 15}" y="113" text-anchor="middle" class="label">finite control</text>')
s.append(sub('q', '2', cx + 15, 134, 18))
s.append(f'<line x1="{cx}" y1="58" x2="{cx}" y2="90" class="accent-stroke" stroke-width="1.4" stroke-dasharray="4 3"/>')
ox = 120 + 4 * w + w / 2
s.append(f'<line x1="{ox}" y1="144" x2="{ox}" y2="176" class="accent-stroke" stroke-width="1.4" stroke-dasharray="4 3"/>')
s.append('<text x="346" y="112" class="label">δ(q, a, b) = (q′, a′, D, D′):</text>')
s.append('<text x="346" y="128" class="label">read a on the work tape and b = X(k)</text>')
s.append('<text x="346" y="144" class="label">on the oracle tape; write a′, move both heads</text>')
s.append('</svg>')
out['oracle-machine'] = ''.join(s)

# ---------------------------------------------------------------- a Delta^0_2 approximation
rows = ['1001100', '1101000', '1101010', '0101010', '0111010', '0110010', '0110011', '0110011']
c, x0, y0 = 30, 90, 40
s = ['<svg class="fig" viewBox="0 0 420 330" width="420" role="img" aria-label="A table of approximations A_s; each column eventually stops changing">']
for j in range(len(rows[0])):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{y0 - 12}" text-anchor="middle" class="math muted" font-size="13">{j}</text>')
s.append(f'<text x="{x0 - 50}" y="{y0 - 12}" class="label">stage</text>')
final = rows[-1]
# last stage at which column j changes
last_change = []
for j in range(len(final)):
    lc = 0
    for t in range(1, len(rows)):
        if rows[t][j] != rows[t-1][j]:
            lc = t
    last_change.append(lc)
for t, r in enumerate(rows):
    y = y0 + c * t
    s.append(sub('A', str(t), x0 - 30, y + 20, 15))
    for j, b in enumerate(r):
        changed = t > 0 and rows[t-1][j] != b
        settled = t >= last_change[j]
        cls = 'cell head-cell' if changed else 'cell'
        s.append(f'<rect x="{x0 + c*j}" y="{y}" width="{c}" height="{c}" class="{cls}"/>')
        s.append(f'<text x="{x0 + c*j + c/2}" y="{y + 20}" text-anchor="middle" class="mrm{"" if settled else " muted"}" font-size="15">{b}</text>')
yy = y0 + c * len(rows) + 22
s.append(f'<text x="{x0 + 3*c + c/2}" y="{yy - 6}" text-anchor="middle" class="mrm muted" font-size="15">⋮</text>')
s.append(f'<line x1="{x0}" y1="{yy + 2}" x2="{x0 + c*len(final)}" y2="{yy + 2}" class="axis"/>')
s.append(f'<text x="{x0 - 30}" y="{yy + 26}" text-anchor="middle" class="math" font-size="15">A</text>')
for j, b in enumerate(final):
    s.append(f'<text x="{x0 + c*j + c/2}" y="{yy + 26}" text-anchor="middle" class="mrm" font-size="15" font-weight="600">{b}</text>')
s.append(f'<text x="{x0 + c*len(final) + 12}" y="{y0 + 60}" class="label">shaded: a bit that</text>')
s.append(f'<text x="{x0 + c*len(final) + 12}" y="{y0 + 76}" class="label">changes at this stage</text>')
s.append('</svg>')
out['delta2-table'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
