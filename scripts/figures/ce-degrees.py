# Generates the inline SVG figure of the course on Post's problem.
# Usage: python3 scripts/figures/ce-degrees.py out.json
import json, sys
out = {}

def sub(base, s, x, y, size=16, anchor='end'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="math" font-size="{size}">{base}'
            f'<tspan class="mrm" font-size="{int(size*0.68)}" dy="4">{s}</tspan></text>')

# ---------------------------------------------------------------- a run of a finite injury construction
# Events per requirement: ('w', stage) new witness, ('a', stage) action, ('i', stage) initialization.
rows = [
    [('w', 1), ('a', 3)],
    [('w', 1), ('i', 3), ('w', 4), ('a', 7)],
    [('w', 1), ('i', 3), ('w', 4), ('i', 7), ('w', 8), ('a', 10)],
    [('w', 1), ('i', 3), ('w', 4), ('i', 7), ('w', 8), ('i', 10), ('w', 11)],
]
x0, dx, y0, dy = 70, 38, 40, 40
T = 13
s = ['<svg class="fig" viewBox="0 0 590 250" width="590" role="img" aria-label="A run of a finite injury construction: each action initializes all requirements of lower priority, which then choose new witnesses">']
for t in range(T):
    x = x0 + dx * t
    s.append(f'<text x="{x}" y="{y0 - 18}" text-anchor="middle" class="mrm muted" font-size="11">{t}</text>')
    s.append(f'<line x1="{x}" y1="{y0 - 8}" x2="{x}" y2="{y0 + dy * (len(rows) - 1) + 10}" class="axis" stroke-dasharray="2 4"/>')
s.append(f'<text x="{x0 + dx * (T - 1) + 14}" y="{y0 - 18}" class="label">stage</text>')
for r, ev in enumerate(rows):
    y = y0 + dy * r
    s.append(sub('R', str(r), x0 - 22, y + 5))
    # active segments between a witness and the next event
    for (k, t), nxt in zip(ev, ev[1:] + [(None, T - 0.5)]):
        if k == 'w':
            xa, xb = x0 + dx * t, x0 + dx * nxt[1]
            s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="accent-stroke" stroke-width="2"/>')
        if k == 'a':
            xa, xb = x0 + dx * t, x0 + dx * (T - 0.5)
            s.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" class="ink-stroke" stroke-width="3"/>')
    for k, t in ev:
        x = x0 + dx * t
        if k == 'w':
            s.append(f'<circle cx="{x}" cy="{y}" r="5" class="node"/>')
        elif k == 'a':
            s.append(f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" class="accent-fill"/>')
        else:
            s.append(f'<path d="M{x-5},{y-5} L{x+5},{y+5} M{x-5},{y+5} L{x+5},{y-5}" class="ink-stroke" stroke-width="1.8"/>')
ly = y0 + dy * len(rows) + 6
s.append(f'<circle cx="{x0}" cy="{ly}" r="5" class="node"/><text x="{x0 + 12}" y="{ly + 4}" class="label">new witness</text>')
s.append(f'<rect x="{x0 + 112}" y="{ly - 6}" width="12" height="12" class="accent-fill"/><text x="{x0 + 130}" y="{ly + 4}" class="label">action (enumeration and restraint)</text>')
s.append(f'<path d="M{x0 + 345},{ly - 5} L{x0 + 355},{ly + 5} M{x0 + 345},{ly + 5} L{x0 + 355},{ly - 5}" class="ink-stroke" stroke-width="1.8"/><text x="{x0 + 362}" y="{ly + 4}" class="label">initialization</text>')
s.append('</svg>')
out['injury-run'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
print('\n'.join(f'{k}: {len(v)} chars' for k, v in out.items()))
