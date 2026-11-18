# Generates the inline SVG figures of the course on computable structures.
# Usage: python3 scripts/figures/computable-structures.py out.json
# Paste each figure into the lesson that uses it:
#   back-and-forth                    -> back-and-forth.md
# The output is deterministic: every loop runs over fixed, ordered data.
import json, sys
out = {}

def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')

# ---------------------------------------------------------------- one step forth in two copies of the rationals
yA, yB = 70, 190
A = [(90, 'a₁'), (230, 'a₂'), (420, 'a₃')]
B = [(130, 'b₁'), (300, 'b₂'), (470, 'b₃')]
new_a = (330, 'a')        # lies between a2 and a3
cands = [(360, ''), (390, 'b'), (430, '')]   # elements of B between b2 and b3; b is the first found
s = ['<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="Two copies of the rationals drawn as horizontal lines. A finite partial isomorphism matches a1, a2, a3 with b1, b2, b3. A new element a of the first copy lies between a2 and a3; the search finds an element b of the second copy between b2 and b3, and a is matched with b">']
s.append('<defs>' + marker('bf-arrow', 'accent-fill') + '</defs>')
for y, lab in ((yA, 'copy 𝒜'), (yB, 'copy ℬ')):
    s.append(f'<line x1="66" y1="{y}" x2="560" y2="{y}" class="muted-stroke" stroke-width="1.2"/>')
    s.append(f'<text x="8" y="{y + 4}" class="label">{lab}</text>')
for (xa, la), (xb, lb) in zip(A, B):
    s.append(f'<line x1="{xa}" y1="{yA + 8}" x2="{xb}" y2="{yB - 8}" class="muted-stroke" stroke-width="1.1" stroke-dasharray="4 3"/>')
    s.append(f'<circle cx="{xa}" cy="{yA}" r="6" class="node"/><text x="{xa}" y="{yA - 14}" text-anchor="middle" class="math">{la}</text>')
    s.append(f'<circle cx="{xb}" cy="{yB}" r="6" class="node"/><text x="{xb}" y="{yB + 24}" text-anchor="middle" class="math">{lb}</text>')
xa, la = new_a
s.append(f'<circle cx="{xa}" cy="{yA}" r="7" class="head-cell"/><text x="{xa}" y="{yA - 14}" text-anchor="middle" class="math">{la}</text>')
s.append(f'<rect x="306" y="{yB - 12}" width="158" height="24" rx="5" class="soft-fill"/>')
for x, l in cands:
    cls = 'head-cell' if l else 'node'
    s.append(f'<circle cx="{x}" cy="{yB}" r="{7 if l else 5}" class="{cls}"/>')
    if l:
        s.append(f'<text x="{x}" y="{yB + 24}" text-anchor="middle" class="math">{l}</text>')
s.append(f'<line x1="{xa}" y1="{yA + 9}" x2="388" y2="{yB - 11}" class="accent-stroke" stroke-width="1.8" marker-end="url(#bf-arrow)"/>')
s.append(f'<text x="592" y="252" text-anchor="end" class="label">search ℬ for an element between b₂ and b₃</text>')
s.append(f'<text x="8" y="252" class="label">dashed: the partial isomorphism p</text>')
s.append('</svg>')
out['back-and-forth'] = ''.join(s)

with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
