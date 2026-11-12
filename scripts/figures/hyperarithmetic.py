# Generates the inline SVG figures of the course on hyperarithmetic sets.
# Usage: python3 scripts/figures/hyperarithmetic.py out.json
# Paste each figure into the lesson that uses it:
#   h-chain        -> h-sets.md
#   matching       -> spector-uniqueness.md
#   ranks          -> kleene-theorem.md
#   harrison       -> sigma11-classes.md
# The output is deterministic: every loop runs over ordered data.
import json, sys
out = {}


def marker(mid, cls='ink-fill'):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
            f'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="{cls}"/></marker>')


def sub(base, s, x, y, size=15, anchor='middle', cls='math', sup=''):
    t = (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{base}')
    if sup:
        t += f'<tspan class="mrm" font-size="{int(size * 0.75)}" dy="-6">{sup}</tspan>'
        if s:
            t += f'<tspan class="mrm" font-size="{int(size * 0.68)}" dy="10">{s}</tspan>'
    elif s:
        t += f'<tspan class="mrm" font-size="{int(size * 0.68)}" dy="4">{s}</tspan>'
    return t + '</text>'


# ---------------------------------------------------------------- the H-sets along a notation of omega + 2
s = ['<svg class="fig" viewBox="0 0 600 226" width="600" role="img" aria-label="The notations below a notation of omega plus 2, in a row, with the H-set of each notation below it; the limit notation gathers the H-sets of the finite notations as columns">']
s.append('<defs>' + marker('ah-hchain', 'muted-fill') + '</defs>')
xs = [40, 100, 160, 220, 400, 470, 540]
ords = ['0', '1', '2', '3', 'ω', 'ω+1', 'ω+2']
hs = [('∅', ''), ('∅', '′'), ('∅', '″'), ('∅', '‴'), ('', ''), ('', ''), ('', '')]
y = 80
s.append(f'<line x1="{xs[0]}" y1="{y}" x2="{xs[3]}" y2="{y}" class="ink-stroke" stroke-width="1.3"/>')
s.append(f'<line x1="{xs[3]}" y1="{y}" x2="{xs[3] + 50}" y2="{y}" class="ink-stroke" stroke-width="1.3" stroke-dasharray="3 4"/>')
s.append(f'<text x="{xs[3] + 85}" y="{y + 5}" text-anchor="middle" class="mrm" font-size="15">⋯</text>')
s.append(f'<line x1="{xs[4]}" y1="{y}" x2="{xs[6]}" y2="{y}" class="ink-stroke" stroke-width="1.3"/>')
for i, x in enumerate(xs):
    cls = 'accent-fill' if i == 4 else 'ink-fill'
    s.append(f'<circle cx="{x}" cy="{y}" r="5" class="{cls}"/>')
    s.append(f'<text x="{x}" y="{y - 16}" text-anchor="middle" class="mrm" font-size="14">{ords[i]}</text>')
# H-sets of finite notations
for i in range(4):
    base, pr = hs[i]
    s.append(f'<text x="{xs[i]}" y="{y + 34}" text-anchor="middle" class="mrm" font-size="15">{base}{pr}</text>')
s.append(sub('H', 'u', xs[4], y + 34))
s.append(f'<text x="{xs[5]}" y="{y + 34}" text-anchor="middle" class="math" font-size="15">H<tspan class="mrm" font-size="10" dy="4">u</tspan><tspan class="mrm" font-size="12" dy="-10">′</tspan></text>')
s.append(f'<text x="{xs[6]}" y="{y + 34}" text-anchor="middle" class="math" font-size="15">H<tspan class="mrm" font-size="10" dy="4">u</tspan><tspan class="mrm" font-size="12" dy="-10">″</tspan></text>')
# the finite H-sets become columns of H_u
for i in range(4):
    x = xs[i]
    s.append(f'<path d="M{x},{y + 44} Q{(x + xs[4]) / 2},{y + 125 - 8 * i} {xs[4] - 6},{y + 46}" fill="none" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3" marker-end="url(#ah-hchain)"/>')
s.append(f'<text x="300" y="{y + 132}" text-anchor="middle" class="label">the H-set of the notation of <tspan class="math" font-size="14">k</tspan> is a column of <tspan class="math" font-size="14">H</tspan><tspan class="mrm" font-size="10" dy="4">u</tspan></text>')
s.append(f'<text x="{xs[4]}" y="{y - 40}" text-anchor="middle" class="label">limit: columns</text>')
s.append(f'<text x="505" y="{y - 40}" text-anchor="middle" class="label">successors: jumps</text>')
s.append(f'<text x="130" y="{y - 40}" text-anchor="middle" class="label">finite ordinals: finite jumps</text>')
s.append('</svg>')
out['h-chain'] = ''.join(s)

# ---------------------------------------------------------------- the successor-into-limit case of Spector's theorem
s = ['<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Two branches of O: above, the notation a equal to 2 to the c; below, the fundamental sequence of the limit notation b; the notation c is matched with a term b_m of larger ordinal">']
s.append('<defs>' + marker('ah-match') + '</defs>')
ytop, ybot = 50, 140
# top branch: c then a = 2^c
s.append(f'<line x1="40" y1="{ytop}" x2="250" y2="{ytop}" class="ink-stroke" stroke-width="1.3" stroke-dasharray="3 4"/>')
s.append(f'<line x1="250" y1="{ytop}" x2="330" y2="{ytop}" class="ink-stroke" stroke-width="1.3"/>')
s.append(f'<circle cx="250" cy="{ytop}" r="5" class="ink-fill"/>')
s.append(f'<circle cx="330" cy="{ytop}" r="5" class="accent-fill"/>')
s.append(sub('c', '', 250, ytop - 14))
s.append(f'<text x="330" y="{ytop - 14}" text-anchor="middle" class="math" font-size="15">a<tspan class="mrm"> = 2</tspan><tspan class="math" font-size="11" dy="-7">c</tspan></text>')
# bottom branch: b_0 < b_1 < b_2 < ... -> b
bx = [60, 150, 240, 330]
s.append(f'<line x1="40" y1="{ybot}" x2="400" y2="{ybot}" class="ink-stroke" stroke-width="1.3"/>')
s.append(f'<line x1="400" y1="{ybot}" x2="480" y2="{ybot}" class="ink-stroke" stroke-width="1.3" stroke-dasharray="3 4"/>')
for i, x in enumerate(bx):
    s.append(f'<circle cx="{x}" cy="{ybot}" r="4.5" class="ink-fill"/>')
    lab = 'm' if i == 3 else str(i)
    s.append(sub('b', lab, x, ybot + 24))
s.append(f'<text x="365" y="{ybot + 24}" text-anchor="middle" class="mrm" font-size="15">⋯</text>')
s.append(f'<circle cx="540" cy="{ybot}" r="5" class="accent-fill"/>')
s.append(f'<text x="540" y="{ybot + 24}" text-anchor="middle" class="math" font-size="15">b<tspan class="mrm"> = 3·5</tspan><tspan class="math" font-size="11" dy="-7">f</tspan></text>')
s.append(f'<text x="508" y="{ybot + 5}" text-anchor="middle" class="mrm" font-size="15">⋯</text>')
# matching
s.append(f'<line x1="252" y1="{ytop + 8}" x2="328" y2="{ybot - 9}" class="ink-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-match)"/>')
s.append(f'<text x="306" y="{(ytop + ybot) / 2 + 4}" text-anchor="start" class="label">least <tspan class="math" font-size="14">m</tspan> with <tspan class="mrm" font-size="14">|</tspan><tspan class="math" font-size="14">c</tspan><tspan class="mrm" font-size="14">| &lt; |</tspan><tspan class="math" font-size="14">b</tspan><tspan class="math" font-size="10" dy="4">m</tspan><tspan class="mrm" font-size="14" dy="-4">|</tspan>, found by <tspan class="math" font-size="14">H</tspan><tspan class="math" font-size="10" dy="4">b</tspan></text>')
s.append(f'<text x="40" y="{ytop - 22}" class="label">branch of a</text>')
s.append(f'<text x="40" y="{ybot - 14}" class="label">branch of b</text>')
s.append('</svg>')
out['matching'] = ''.join(s)

# ---------------------------------------------------------------- a well-founded tree with the ranks of its nodes
# Node -> list of children; the rank of a node is sup(rank(child) + 1).
children = {
    '': ['0', '1', '2'],
    '0': [], '1': ['10', '11'], '2': ['20'],
    '10': [], '11': ['110'], '20': ['200', '201'],
    '110': [], '200': [], '201': ['2010'], '2010': [],
}
rank = {}


def rk(n):
    if n not in rank:
        rank[n] = max([rk(c) + 1 for c in children[n]], default=0)
    return rank[n]


order = ['', '0', '1', '2', '10', '11', '20', '110', '200', '201', '2010']
for n in order:
    rk(n)
pos = {'': (300, 30), '0': (120, 90), '1': (300, 90), '2': (480, 90),
       '10': (250, 150), '11': (350, 150), '20': (480, 150),
       '110': (350, 210), '200': (430, 210), '201': (530, 210), '2010': (530, 270)}
s = ['<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="A finite well-founded tree; each node is labeled with its rank, the supremum of the ranks of its children plus one">']
for n in order:
    for c in children[n]:
        (x1, y1), (x2, y2) = pos[n], pos[c]
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ink-stroke" stroke-width="1.2"/>')
for n in order:
    x, y = pos[n]
    cls = 'accent-fill' if n == '' else 'ink-fill'
    s.append(f'<circle cx="{x}" cy="{y}" r="4.5" class="{cls}"/>')
    s.append(f'<text x="{x + 10}" y="{y - 6}" class="mrm" font-size="13">{rank[n]}</text>')
s.append(f'<text x="{pos[""][0] - 12}" y="{pos[""][1] + 4}" text-anchor="end" class="mrm" font-size="13">ε</text>')
s.append('<text x="40" y="270" class="label">leaves have rank 0;</text>')
s.append('<text x="40" y="286" class="label">a node has rank sup(rank of child + 1)</text>')
s.append('</svg>')
out['ranks'] = ''.join(s)

def ck(x, y, anchor='middle', pre='', post=''):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="mrm" font-size="14">{pre}<tspan class="math">ω</tspan>'
            f'<tspan font-size="10" dy="4">1</tspan><tspan font-size="9" dy="-11">CK</tspan><tspan dy="7">{post}</tspan></text>')


# ---------------------------------------------------------------- the order type of a Harrison order
s = ['<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="A Harrison order: a well-founded initial segment of type omega one CK, then densely many copies of omega one CK, then a final well-ordered segment; a descending sequence lies in the ill-founded part">']
y = 60
s.append(f'<line x1="30" y1="{y}" x2="220" y2="{y}" class="accent-stroke" stroke-width="3"/>')
s.append(f'<line x1="232" y1="{y}" x2="500" y2="{y}" class="ink-stroke" stroke-width="1.4"/>')
for k in range(12):
    x = 236 + k * 22
    s.append(f'<line x1="{x}" y1="{y - 6}" x2="{x}" y2="{y + 6}" class="muted-stroke" stroke-width="1"/>')
s.append(f'<line x1="512" y1="{y}" x2="570" y2="{y}" class="ink-stroke" stroke-width="3"/>')
# a descending sequence in the ill-founded part, converging to the cut after the well-founded part
for k, x in enumerate([470, 400, 340, 300, 276, 262, 254]):
    s.append(f'<circle cx="{x}" cy="{y + 22}" r="3" class="ink-fill"/>')
s.append(f'<text x="244" y="{y + 26}" text-anchor="end" class="mrm" font-size="12">⋯</text>')
s.append(f'<text x="125" y="{y - 14}" text-anchor="middle" class="label">well-founded part W</text>')
s.append(ck(125, y + 28))
s.append(f'<text x="366" y="{y - 14}" text-anchor="middle" class="label">copies of the type of W, indexed by η</text>')
s.append(ck(541, y - 14, pre='<tspan class="math">ρ</tspan> &lt; '))
s.append(f'<text x="366" y="{y + 50}" text-anchor="middle" class="label">a descending sequence: it is not hyperarithmetic</text>')
s.append(ck(300, y + 80, pre='order type ', post=' · (1 + <tspan class="math">η</tspan>) + <tspan class="math">ρ</tspan>'))
s.append('</svg>')
out['harrison'] = ''.join(s)

json.dump(out, open(sys.argv[1], 'w'))
