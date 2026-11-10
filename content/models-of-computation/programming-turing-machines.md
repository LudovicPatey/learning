---
title: Programming Turing machines
summary: Auxiliary symbols, sequential composition of machines, translation invariance, multi-tape machines and their simulation by single-tape machines.
duration: 40
prerequisites: [turing-machines]
---

Writing Turing machines directly is laborious, but a few techniques make it systematic. This lesson presents them and proves that several natural extensions of the model compute no new functions.

## Auxiliary symbols: a doubling machine

The alphabet may contain symbols other than $\sqcup$ and $1$. They serve as **markers** recording which part of the input has already been processed. As an example, we compute $x \mapsto 2x$. On input $\ulcorner x \urcorner = 1^{n}$ with $n = x + 1$, the output must be $\ulcorner 2x \urcorner = 1^{2n - 1}$.

The machine works in two phases. In the first phase, it repeatedly replaces the leftmost unmarked $1$ by $X$ and appends a $Y$ to the right end of the tape contents. After $n$ rounds the tape contains $X^n Y^n$. In the second phase, it turns every $Y$ into $1$, erases the last symbol, and moves left turning every $X$ into $1$. The alphabet is $\{\sqcup, 1, X, Y\}$:

| | $1$ | $X$ | $Y$ | $\sqcup$ |
| --- | --- | --- | --- | --- |
| $q_0$ | $(q_1, X, R)$ | — | $(q_3, 1, R)$ | — |
| $q_1$ | $(q_1, 1, R)$ | — | $(q_1, Y, R)$ | $(q_2, Y, L)$ |
| $q_2$ | $(q_2, 1, L)$ | $(q_0, X, R)$ | $(q_2, Y, L)$ | — |
| $q_3$ | — | — | $(q_3, 1, R)$ | $(q_4, \sqcup, L)$ |
| $q_4$ | $(q_5, \sqcup, L)$ | — | — | — |
| $q_5$ | $(q_5, 1, L)$ | $(q_5, 1, L)$ | — | $(q_h, \sqcup, R)$ |

Entries marked — are never used; to make $\delta$ total, set them to $(q_h, \sqcup, R)$, say.

:::proposition{#prop-tm-doubling}
This machine computes $x \mapsto 2x$.
:::

:::proof{of=prop-tm-doubling}
Let $n = x + 1$. We show by induction on $j \in \{0, \dots, n\}$ that the machine reaches the configuration in state $q_0$ with tape $X^j 1^{n-j} Y^j$ written from cell $0$ and the head on cell $j$. For $j = 0$ this is the initial configuration. Suppose it holds for some $j < n$. Cell $j$ contains $1$: the machine writes $X$ and enters $q_1$, which moves right across $1^{n-j-1} Y^j$ to the first blank, at cell $n + j$, writes $Y$ there, and enters $q_2$. In state $q_2$ the head moves left across $Y$s and $1$s until it reaches the $X$ on cell $j$, and enters $q_0$ on cell $j + 1$. The tape is now $X^{j+1} 1^{n-j-1} Y^{j+1}$, as required.

For $j = n$, the tape is $X^n Y^n$ and the head scans the first $Y$, on cell $n$, in state $q_0$. The machine writes $1$ and enters $q_3$, which turns the remaining $Y$s into $1$s and reaches the blank on cell $2n$. It then erases cell $2n - 1$, which contains $1$, and enters $q_5$ on cell $2n - 2$. Note that $2n - 2 \geq 0$. State $q_5$ moves left, turning $1$s and $X$s into $1$s, down to cell $-1$, and halts on cell $0$. The final tape is $1^{2n - 1}$ on cells $0, \dots, 2n - 2$, that is $\ulcorner 2x \urcorner$.
:::

:::quiz[the doubling machine]
Why does the machine need the marker $Y$, rather than appending $1$s directly?

- [x] Appended $1$s would be indistinguishable from the unprocessed $1$s of the input, so in state $q_0$ the machine could not detect when all input symbols have been marked.

  The first $Y$ marks the boundary between the input and the copy.
- [ ] To ensure the machine never moves to the left of cell $0$.

  It does move to cell $-1$, in the last phase.
- [ ] Because the alphabet must contain at least four symbols.

  Any alphabet containing $\sqcup$ and $1$ is allowed.

---

How many steps does the first phase take, as a function of $n = x + 1$?

- [x] Of the order of $n^2$: round $j$ crosses about $2(n - j) + 2j = 2n$ cells, twice.

  The machine is quadratic. Unary arithmetic on Turing machines is slow, but computability ignores running time.
- [ ] Of the order of $n$.
- [ ] Of the order of $2^n$.
:::

## Translation invariance

The behavior of a machine depends only on the relative position of the head and the symbols. Formally, for a tape $\tau$ and $d \in \mathbb{Z}$, let $\tau^{+d}$ be the translated tape $\tau^{+d}(i) = \tau(i - d)$.

:::lemma{#lem-tm-translation}
If $(q, \tau, h) \vdash (q', \tau', h')$, then $(q, \tau^{+d}, h + d) \vdash (q', \tau'^{+d}, h' + d)$ for every $d \in \mathbb{Z}$. Consequently, the computation from a translated configuration is the translation of the original computation, and halts after the same number of steps.
:::

:::proof{of=lem-tm-translation}
The symbol scanned in the translated configuration is $\tau^{+d}(h + d) = \tau(h)$, so the same transition $(q', b, D)$ is applied. The new tape coincides with $\tau^{+d}$ except at $h + d$ where it contains $b$, which is exactly $\tau'^{+d}$, and the new head position is $h' + d$. The second statement follows by induction on the number of steps.
:::

## Sequential composition

The standard final configuration of a machine is, up to translation, an initial configuration on the output. This allows us to run machines one after the other.

:::proposition{#prop-tm-composition}
Let $M$ and $N$ be Turing machines computing $f : \nat \rightharpoonup \nat$ and $g : \nat \rightharpoonup \nat$. There is a Turing machine $M ; N$ computing $g \circ f$.
:::

:::proof{of=prop-tm-composition}
By :ref{#ex-tm-clean-halt} below, we may assume that every halting computation of $M$ on an input $\ulcorner x \urcorner$ ends in a standard final configuration.

Rename the states of $N$ so that they are disjoint from those of $M$, and take the union of the alphabets. The machine $M ; N$ has the states of both machines, initial state $q_0^M$, halting state $q_h^N$, and the transitions of both machines, except that every transition of $M$ entering $q_h^M$ is redirected to $q_0^N$. Entries for symbols of one machine absent from the alphabet of the other are set arbitrarily; they are never used, since $M$ only sees its own symbols, and $N$ is started on a tape containing only $\sqcup$ and $1$.

On input $x$, the machine $M ; N$ first behaves like $M$. If $f(x)\diverge$, then $M$ does not halt, and neither does $M ; N$. If $f(x)\converge = y$, then $M ; N$ enters $q_0^N$ with a tape containing exactly $\ulcorner y \urcorner$, starting at the head position $h$. This is the initial configuration of $N$ on input $y$, translated by $h$. By :ref{#lem-tm-translation}, the remaining computation is the translation by $h$ of the computation of $N$ on input $y$. Since translations preserve standard final configurations, $M ; N$ halts in a standard final configuration with output $g(y)$ if $g(y)\converge$, and otherwise it does not. Hence $M ; N$ computes $g \circ f$.
:::

::::exercise{difficulty=2 #ex-tm-clean-halt}
Show that for every machine $M$ there is a machine $\widehat M$ with $\varphi^{(1)}_{\widehat M} = \varphi^{(1)}_M$ such that every halting computation of $\widehat M$ on an input $\ulcorner x \urcorner$ ends in a standard final configuration.

:::hint
Let $\widehat M$ maintain two end markers delimiting the part of the tape visited so far, and check, before halting, whether the tape between the markers has the form of an output.
:::

:::solution
Let $\widehat M$ first write a marker $\triangleleft$ on cell $-1$ and a marker $\triangleright$ after the input, then simulate $M$. Whenever the simulated head reaches a marker, the marker is moved one cell further (shifting it is easy since it is at the end of the visited zone), and the cell it occupied is treated as blank. When $M$ would enter $q_h$, $\widehat M$ instead enters a checking phase: it records whether the scanned cell holds a $1$ preceded by a blank, then scans the zone between the markers and verifies that it contains exactly one block of $1$s, starting at the remembered position, and blanks elsewhere. If the check succeeds, it erases the markers, returns to the first $1$, and halts. If it fails, it enters a state which moves right forever. Then $\widehat M$ halts only in standard configurations, and does so exactly when $M$ halts in a standard configuration, with the same output.
:::
::::

Composition with functions of several arguments, such as $h(f(x), g(x))$, can be handled similarly, using a machine that copies its input. The details are tedious and teach little. We will obtain closure under composition much more easily from the equivalence with the recursive functions, proved later in this course.

:::quiz[sequential composition]
In the proof of :ref{#prop-tm-composition}, what is :ref{#lem-tm-translation} used for?

- [x] When $M$ halts, its output block starts at the head position $h$, which may differ from $0$. Translation invariance shows that $N$ behaves on this configuration as on its initial configuration on input $f(x)$.
- [ ] To show that $M$ halts.

  Whether $M$ halts is given by the hypothesis on $M$.
- [ ] To rename the states of $N$.

  Renaming states is a syntactic operation; it has nothing to do with tapes.
:::

## Multi-tape machines

A natural extension gives the machine several tapes, each with its own head.

:::definition{#def-multitape}
A **$k$-tape Turing machine** is defined as in :ref{#def-turing-machine}, except that the transition function has the form
$$
\delta : (Q \setminus \{q_h\}) \times \Gamma^k \to Q \times \Gamma^k \times \{L, S, R\}^k,
$$
where $S$ means that the head stays in place. A configuration consists of a state, $k$ tapes and $k$ head positions. By convention the input is written on tape $1$, the other tapes are initially blank, and the output is read on tape $1$.
:::

Multi-tape machines are much easier to program. For instance, a $2$-tape machine can copy its input to tape $2$ in a single left-to-right pass.

:::figure[The simulation of a $3$-tape machine: each cell of the single tape stores one cell of every tape, together with a mark telling whether the corresponding head is there.]
<svg class="fig" viewBox="0 0 600 205" width="600" role="img" aria-label="Three tapes encoded as three tracks of one tape"><defs><marker id="ah-tracks" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="8" y="54" class="label">tape 1</text><rect x="60" y="34" width="30" height="30" rx="2" class="cell"/><text x="75.0" y="54" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="90" y="34" width="30" height="30" rx="2" class="cell"/><text x="105.0" y="54" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="120" y="34" width="30" height="30" rx="2" class="cell head-cell"/><text x="135.0" y="54" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="150" y="34" width="30" height="30" rx="2" class="cell"/><text x="165.0" y="54" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="180" y="34" width="30" height="30" rx="2" class="cell"/><text x="195.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="210" y="34" width="30" height="30" rx="2" class="cell"/><text x="225.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><path d="M129.0,21 L141.0,21 L135.0,31 z" class="accent-fill"/><text x="8" y="110" class="label">tape 2</text><rect x="60" y="90" width="30" height="30" rx="2" class="cell"/><text x="75.0" y="110" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="90" y="90" width="30" height="30" rx="2" class="cell head-cell"/><text x="105.0" y="110" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="120" y="90" width="30" height="30" rx="2" class="cell"/><text x="135.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="150" y="90" width="30" height="30" rx="2" class="cell"/><text x="165.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="180" y="90" width="30" height="30" rx="2" class="cell"/><text x="195.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="210" y="90" width="30" height="30" rx="2" class="cell"/><text x="225.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><path d="M99.0,77 L111.0,77 L105.0,87 z" class="accent-fill"/><text x="8" y="166" class="label">tape 3</text><rect x="60" y="146" width="30" height="30" rx="2" class="cell"/><text x="75.0" y="166" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="90" y="146" width="30" height="30" rx="2" class="cell"/><text x="105.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="120" y="146" width="30" height="30" rx="2" class="cell"/><text x="135.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="150" y="146" width="30" height="30" rx="2" class="cell"/><text x="165.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="180" y="146" width="30" height="30" rx="2" class="cell head-cell"/><text x="195.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="210" y="146" width="30" height="30" rx="2" class="cell"/><text x="225.0" y="166" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><path d="M189.0,133 L201.0,133 L195.0,143 z" class="accent-fill"/><line x1="255" y1="104" x2="315" y2="104" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-tracks)"/><text x="335" y="22" class="label">one tape, three tracks</text><rect x="335" y="34" width="44" height="34" class="cell"/><text x="357.0" y="56" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="335" y="68" width="44" height="34" class="cell"/><text x="357.0" y="90" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="335" y="102" width="44" height="34" class="cell"/><text x="357.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="335" y="34" width="44" height="102" class="track-outline"/><rect x="379" y="34" width="44" height="34" class="cell"/><text x="401.0" y="56" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="379" y="68" width="44" height="34" class="cell head-cell"/><text x="401.0" y="90" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="379" y="102" width="44" height="34" class="cell"/><text x="401.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="379" y="34" width="44" height="102" class="track-outline"/><rect x="423" y="34" width="44" height="34" class="cell head-cell"/><text x="445.0" y="56" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="423" y="68" width="44" height="34" class="cell"/><text x="445.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="423" y="102" width="44" height="34" class="cell"/><text x="445.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="423" y="34" width="44" height="102" class="track-outline"/><rect x="467" y="34" width="44" height="34" class="cell"/><text x="489.0" y="56" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="467" y="68" width="44" height="34" class="cell"/><text x="489.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="467" y="102" width="44" height="34" class="cell"/><text x="489.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="467" y="34" width="44" height="102" class="track-outline"/><rect x="511" y="34" width="44" height="34" class="cell"/><text x="533.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="511" y="68" width="44" height="34" class="cell"/><text x="533.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="511" y="102" width="44" height="34" class="cell head-cell"/><text x="533.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="511" y="34" width="44" height="102" class="track-outline"/><rect x="555" y="34" width="44" height="34" class="cell"/><text x="577.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="555" y="68" width="44" height="34" class="cell"/><text x="577.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="555" y="102" width="44" height="34" class="cell"/><text x="577.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="555" y="34" width="44" height="102" class="track-outline"/><text x="335" y="160" class="label">a shaded cell carries the head mark of its track</text></svg>
:::

:::theorem{#thm-multitape-simulation}
Every partial function computed by a $k$-tape Turing machine is computed by a $1$-tape Turing machine.
:::

:::proof{of=thm-multitape-simulation}
Let $M$ be a $k$-tape machine with alphabet $\Gamma$. The idea is to store the $k$ tapes on $k$ **tracks** of a single tape. Let the new alphabet be $\Gamma \cup (\Gamma \times \{0, 1\})^k$: a cell of the simulating machine $N$ contains either a symbol of $\Gamma$, or a $k$-tuple of pairs $(a_i, m_i)$ where $a_i$ is the content of the corresponding cell of tape $i$ and $m_i = 1$ indicates that the head of tape $i$ is at this cell. This alphabet is finite.

$N$ first converts its input into this format: it replaces each input symbol $a$ by $((a, m), (\sqcup, m), \dots, (\sqcup, m))$, where $m = 1$ on cell $0$ and $m = 0$ elsewhere. Then $N$ simulates each step of $M$ as follows. The state of $M$ is stored in the state of $N$. $N$ sweeps over the zone of the tape visited so far, from left to right, and collects in its state the symbols under the $k$ marked heads; there are finitely many possibilities, so they can be stored in the state. Knowing the state of $M$ and the scanned symbols, $N$ determines the transition of $M$. It then sweeps back from right to left, updating the symbol under each marked head and moving each mark by one cell according to the transition. When $N$ meets a cell containing a plain symbol of $\Gamma$ — that is, a part of the tape not yet visited — it first converts it to the track format. When $M$ halts, $N$ converts the tape back, keeping only track $1$, moves the head to the position of head $1$, and halts.

By induction on the number of steps, after the simulation of $t$ steps of $M$, the tracks of $N$ contain the tapes of $M$ after $t$ steps, with the heads correctly marked. Hence $N$ computes the same function as $M$. (To ensure that $N$ halts in a standard configuration exactly when $M$ does, one proceeds as in :ref{#ex-tm-clean-halt}.)
:::

:::quiz[the multi-tape simulation]
Why can the symbols under the $k$ heads be "stored in the state" of $N$ during a sweep?

- [x] There are only $|\Gamma|^k$ possible tuples of scanned symbols, so $N$ can have one copy of its sweeping states for each tuple collected so far, together with the current state of $M$.

  This keeps the set of states of $N$ finite: it is roughly $|Q| \cdot (|\Gamma| + 1)^k$ times larger than that of $M$.
- [ ] Because $N$ has $k$ tapes as well.

  $N$ has a single tape.
- [ ] Because the heads of $M$ are always on the same cell.

  The heads of $M$ move independently.

---

If $M$ halts after $t$ steps, roughly how many steps does $N$ take?

- [x] $O(t^2)$, since after $t$ steps the visited zone has length $O(t)$ and each simulated step costs a constant number of sweeps over it.
- [ ] $O(t)$.
- [ ] $O(2^t)$.
:::

## Other variants

The same method — encode the richer structure on one tape, simulate step by step — shows that the following variants compute exactly the Turing-computable functions:

- machines whose tape is infinite only to the right (fold the two-way tape on itself, using two tracks);
- machines with a two-dimensional tape (store the finite non-blank region row by row);
- machines with the alphabet $\{\sqcup, 1\}$ only (encode each symbol of a larger alphabet by a fixed-length block of $\sqcup$ and $1$);
- **non-deterministic** machines, where $\delta$ is a relation, and a function value is accepted if *some* computation produces it, provided the function is well defined (simulate all computations in breadth-first order, using a third tape).

Some care is needed with the input and output conventions in each case, but no new idea.

## Exercises

::::exercise{difficulty=1}
Design a $1$-tape machine computing $x \mapsto x \bmod 2$, and prove it correct.

:::solution
Erase the input from left to right, alternating between two states $e$ (even number of $1$s erased so far) and $o$ (odd). Since $\ulcorner x \urcorner$ has $x + 1$ ones, at the first blank the state is $o$ if $x$ is even and $e$ if $x$ is odd. In state $o$ at the blank, write a single $1$ (output $0$); in state $e$, write $1$, move right, write $1$, move left (output $1$). Then halt with the head on the first $1$. A formal proof proceeds by induction on the number of erased cells, as in :ref{#prop-tm-doubling}.
:::
::::

::::exercise{difficulty=2}
Describe a $2$-tape machine computing $(x, y) \mapsto x \cdot y$, and estimate its number of steps.

:::solution
Copy $\ulcorner y \urcorner$ to tape $2$ and erase it from tape $1$, together with the first $1$ of $\ulcorner x \urcorner$ and of the copy, so that tape $1$ holds $x$ ones and tape $2$ holds $y$ ones. Write the output on a third zone of tape $2$, to the right of a separator: for each $1$ of tape $1$, erase it and append a copy of the block of tape $2$ to the output zone by scanning the block once. Finally add one $1$ for the unary convention and move the result to tape $1$. Each of the $x$ rounds costs $O(x + y + xy)$ steps (the head must travel back and forth), so the total is $O(x^2 y)$ steps.
:::
::::
