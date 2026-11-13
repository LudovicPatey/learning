# Generates the inline SVG figures of the course Truth definitions and provability in fragments.
# Usage: python3 scripts/figures/truth-and-provability.py out.json
# Paste each figure into the lesson that uses it:
#   ack-computation -> ackermann-isigma.md
# The output is deterministic.
import json, sys
out = {}


def box(cx, cy, text, head=False, w=96, h=30):
    cls = 'cell head-cell' if head else 'cell'
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w}" height="{h}" rx="4" class="{cls}"/>'
            f'<text x="{cx:.1f}" y="{cy + 5:.1f}" text-anchor="middle" class="mrm" font-size="14">{text}</text>')


def arrow(x1, y1, x2, y2, mid_label=None, dx=0, dy=0, anchor='middle'):
    s = (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="ink-stroke" '
         f'stroke-width="1" marker-end="url(#tp-ack-arrow)"/>')
    if mid_label:
        mx, my = (x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy
        s += f'<text x="{mx:.1f}" y="{my:.1f}" text-anchor="{anchor}" class="label">{mid_label}</text>'
    return s


# ---------------------------------------------------------------- a computation of A(1, 1) = 3
# The computation c = {(0,1,2), (1,0,2), (0,2,3), (1,1,3)}; an arrow goes from a triple to the
# triples that justify it. Triples with x = 0 are justified by the first clause (highlighted).
s = ['<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="A computation of A(1,1) = 3: the triple (1,1,3) is justified by (1,0,2) and (0,2,3); the triple (1,0,2) is justified by (0,1,2); the triples (0,1,2) and (0,2,3) are justified by the first clause">']
s.append('<defs><marker id="tp-ack-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs>')
top, mid, bot = (300, 36), (180, 112), (180, 188)
right = (420, 112)
s.append(box(*top, '⟨1, 1, 3⟩'))
s.append(box(*mid, '⟨1, 0, 2⟩'))
s.append(box(*right, '⟨0, 2, 3⟩', head=True))
s.append(box(*bot, '⟨0, 1, 2⟩', head=True))
# third clause: (x, y'+1, z) from (x, y', w) and (x', w, z), here w = 2
s.append(arrow(276, 51, 204, 96, '⟨x, y′, w⟩', dx=-18, dy=-4, anchor='end'))
s.append(arrow(324, 51, 396, 96, '⟨x′, w, z⟩', dx=18, dy=-4, anchor='start'))
# second clause: (x'+1, 0, z) from (x', 1, z)
s.append(arrow(180, 127, 180, 172, '⟨x′, 1, z⟩', dx=-12, dy=4, anchor='end'))
s.append(f'<text x="250" y="{bot[1] + 5}" text-anchor="start" class="label">highlighted: x = 0, justified by the first clause</text>')
s.append('</svg>')
out['ack-computation'] = ''.join(s)

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '/dev/stdout'
    with open(path, 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
