---
title: Programming Turing machines
summary: Auxiliary symbols used as markers, translation invariance, and the sequential composition of machines.
duration: 35
prerequisites: [turing-machines]
---

Writing Turing machines directly is laborious, but a few techniques make it systematic: auxiliary symbols used as markers, the observation that a machine only depends on relative positions, and the composition of machines. This lesson presents them on examples; the next one uses them to show that richer models of machines compute no new functions.

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

:::figure[The doubling machine on input $2$ ($n = 3$): the tape at the beginning of each round $j$, in state $q_0$ with the head on cell $j$, and the final configuration. The invariant of the proof below is the tape $X^j 1^{n-j} Y^j$.]
<svg class="fig" viewBox="0 0 400 244" width="400" role="img" aria-label="Tape of the doubling machine at the start of each round, and at the end"><text x="138.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="174.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="210.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="246.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="282.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">4</text><text x="318.0" y="24" text-anchor="middle" class="mrm muted" font-size="13">5</text><text x="20" y="57.0" text-anchor="start" font-size="15"><tspan class="math">j</tspan><tspan class="mrm"> = 0</tspan></text><text x="88" y="57.0" text-anchor="middle" font-size="16"><tspan class="math">q</tspan><tspan class="mrm" font-size="10" dy="4">0</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect class="cell head-cell" x="120" y="36" width="36" height="32" rx="2"/><text x="138.0" y="58.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="156" y="36" width="36" height="32" rx="2"/><text x="174.0" y="58.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="192" y="36" width="36" height="32" rx="2"/><text x="210.0" y="58.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="228" y="36" width="36" height="32" rx="2"/><text x="246.0" y="58.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect class="cell" x="264" y="36" width="36" height="32" rx="2"/><text x="282.0" y="58.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect class="cell" x="300" y="36" width="36" height="32" rx="2"/><text x="318.0" y="58.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><text x="20" y="97.0" text-anchor="start" font-size="15"><tspan class="math">j</tspan><tspan class="mrm"> = 1</tspan></text><text x="88" y="97.0" text-anchor="middle" font-size="16"><tspan class="math">q</tspan><tspan class="mrm" font-size="10" dy="4">0</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect class="cell" x="120" y="76" width="36" height="32" rx="2"/><text x="138.0" y="98.0" text-anchor="middle" class="mrm" font-size="16">X</text><rect class="cell head-cell" x="156" y="76" width="36" height="32" rx="2"/><text x="174.0" y="98.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="192" y="76" width="36" height="32" rx="2"/><text x="210.0" y="98.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="228" y="76" width="36" height="32" rx="2"/><text x="246.0" y="98.0" text-anchor="middle" class="mrm" font-size="16">Y</text><rect class="cell" x="264" y="76" width="36" height="32" rx="2"/><text x="282.0" y="98.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect class="cell" x="300" y="76" width="36" height="32" rx="2"/><text x="318.0" y="98.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><text x="20" y="137.0" text-anchor="start" font-size="15"><tspan class="math">j</tspan><tspan class="mrm"> = 2</tspan></text><text x="88" y="137.0" text-anchor="middle" font-size="16"><tspan class="math">q</tspan><tspan class="mrm" font-size="10" dy="4">0</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect class="cell" x="120" y="116" width="36" height="32" rx="2"/><text x="138.0" y="138.0" text-anchor="middle" class="mrm" font-size="16">X</text><rect class="cell" x="156" y="116" width="36" height="32" rx="2"/><text x="174.0" y="138.0" text-anchor="middle" class="mrm" font-size="16">X</text><rect class="cell head-cell" x="192" y="116" width="36" height="32" rx="2"/><text x="210.0" y="138.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="228" y="116" width="36" height="32" rx="2"/><text x="246.0" y="138.0" text-anchor="middle" class="mrm" font-size="16">Y</text><rect class="cell" x="264" y="116" width="36" height="32" rx="2"/><text x="282.0" y="138.0" text-anchor="middle" class="mrm" font-size="16">Y</text><rect class="cell" x="300" y="116" width="36" height="32" rx="2"/><text x="318.0" y="138.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><text x="20" y="177.0" text-anchor="start" font-size="15"><tspan class="math">j</tspan><tspan class="mrm"> = 3</tspan></text><text x="88" y="177.0" text-anchor="middle" font-size="16"><tspan class="math">q</tspan><tspan class="mrm" font-size="10" dy="4">0</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect class="cell" x="120" y="156" width="36" height="32" rx="2"/><text x="138.0" y="178.0" text-anchor="middle" class="mrm" font-size="16">X</text><rect class="cell" x="156" y="156" width="36" height="32" rx="2"/><text x="174.0" y="178.0" text-anchor="middle" class="mrm" font-size="16">X</text><rect class="cell" x="192" y="156" width="36" height="32" rx="2"/><text x="210.0" y="178.0" text-anchor="middle" class="mrm" font-size="16">X</text><rect class="cell head-cell" x="228" y="156" width="36" height="32" rx="2"/><text x="246.0" y="178.0" text-anchor="middle" class="mrm" font-size="16">Y</text><rect class="cell" x="264" y="156" width="36" height="32" rx="2"/><text x="282.0" y="178.0" text-anchor="middle" class="mrm" font-size="16">Y</text><rect class="cell" x="300" y="156" width="36" height="32" rx="2"/><text x="318.0" y="178.0" text-anchor="middle" class="mrm" font-size="16">Y</text><line x1="20" y1="191" x2="396" y2="191" class="axis"/><text x="20" y="217.0" class="label">halt</text><text x="88" y="217.0" text-anchor="middle" font-size="16"><tspan class="math">q</tspan><tspan class="mrm" font-size="10" dy="4">h</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect class="cell head-cell" x="120" y="196" width="36" height="32" rx="2"/><text x="138.0" y="218.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="156" y="196" width="36" height="32" rx="2"/><text x="174.0" y="218.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="192" y="196" width="36" height="32" rx="2"/><text x="210.0" y="218.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="228" y="196" width="36" height="32" rx="2"/><text x="246.0" y="218.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="264" y="196" width="36" height="32" rx="2"/><text x="282.0" y="218.0" text-anchor="middle" class="mrm" font-size="16">1</text><rect class="cell" x="300" y="196" width="36" height="32" rx="2"/><text x="318.0" y="218.0" text-anchor="middle" class="mrm muted" font-size="16">⊔</text></svg>
:::

:::proposition{#prop-tm-doubling}
This machine computes $x \mapsto 2x$.
:::

:::proof{of=prop-tm-doubling}
The proof follows the method of the previous lesson: state an **invariant**, a description of the configuration at the beginning of each round, and check by induction on the rounds that it is preserved. Let $n = x + 1$. We show by induction on $j \in \{0, \dots, n\}$ that the machine reaches the configuration in state $q_0$ with tape $X^j 1^{n-j} Y^j$ written from cell $0$ and the head on cell $j$. For $j = 0$ this is the initial configuration. Suppose it holds for some $j < n$. Cell $j$ contains $1$: the machine writes $X$ and enters $q_1$, which moves right across $1^{n-j-1} Y^j$ to the first blank, at cell $n + j$, writes $Y$ there, and enters $q_2$. In state $q_2$ the head moves left across $Y$s and $1$s until it reaches the $X$ on cell $j$, and enters $q_0$ on cell $j + 1$. The tape is now $X^{j+1} 1^{n-j-1} Y^{j+1}$, as required.

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

- [x] Of the order of $n^2$: in round $j$ the head goes from cell $j$ to cell $n + j$ and back, about $2n$ steps, and there are $n$ rounds.

  The machine is quadratic. Unary arithmetic on Turing machines is slow, but computability ignores running time.
- [ ] Of the order of $n$.

  Each of the $n$ rounds crosses about $2n$ cells, so the total is quadratic, not linear.
- [ ] Of the order of $2^n$.

  The number of rounds is $n$ and each costs $O(n)$ steps; nothing is exponential.
:::

## Translation invariance

The behavior of a machine depends only on the relative position of the head and the symbols. This is needed as soon as machines are combined: a machine which halts leaves its output wherever its head happens to be, and the next machine must be able to start from there as if from cell $0$. Formally, for a tape $\tau$ and $d \in \mathbb{Z}$, let $\tau^{+d}$ be the translated tape $\tau^{+d}(i) = \tau(i - d)$.

:::lemma{#lem-tm-translation}
If $(q, \tau, h) \vdash (q', \tau', h')$, then $(q, \tau^{+d}, h + d) \vdash (q', \tau'^{+d}, h' + d)$ for every $d \in \mathbb{Z}$. Consequently, the computation from a translated configuration is the translation of the original computation, and halts after the same number of steps.
:::

:::proof{of=lem-tm-translation}
The symbol scanned in the translated configuration is $\tau^{+d}(h + d) = \tau(h)$, so the same transition $(q', b, D)$ is applied. The new tape coincides with $\tau^{+d}$ except at $h + d$ where it contains $b$, which is exactly $\tau'^{+d}$, and the new head position is $h' + d$. The second statement follows by induction on the number of steps.
:::

## Sequential composition

The standard final configuration of a machine is, up to translation, an initial configuration on the output. This allows us to run machines one after the other: the only change needed is to replace the halting state of the first machine by the initial state of the second.

:::proposition{#prop-tm-composition}
Let $M$ and $N$ be Turing machines computing $f : \nat \rightharpoonup \nat$ and $g : \nat \rightharpoonup \nat$. There is a Turing machine $M ; N$ computing $g \circ f$.
:::

:::proof{of=prop-tm-composition}
By :ref{#ex-tm-clean-halt} below, we may assume that every halting computation of $M$ on an input $\ulcorner x \urcorner$ ends in a standard final configuration.

Rename the states of $N$ so that they are disjoint from those of $M$, and take the union of the alphabets. The machine $M ; N$ has the states of both machines, initial state $q_0^M$, halting state $q_h^N$, and the transitions of both machines, except that every transition of $M$ entering $q_h^M$ is redirected to $q_0^N$. The state $q_h^M$ is no longer entered; its transitions, now required since it is not the halting state of $M ; N$, are set arbitrarily. Entries for symbols of one machine absent from the alphabet of the other are set arbitrarily; they are never used, since $M$ only sees its own symbols, and $N$ is started on a tape containing only $\sqcup$ and $1$.

On input $x$, the machine $M ; N$ first behaves like $M$. If $f(x)\diverge$, then $M$ does not halt, and neither does $M ; N$. If $f(x)\converge = y$, then $M ; N$ enters $q_0^N$ with a tape containing exactly $\ulcorner y \urcorner$, starting at the head position $h$. This is the initial configuration of $N$ on input $y$, translated by $h$. By :ref{#lem-tm-translation}, the remaining computation is the translation by $h$ of the computation of $N$ on input $y$. Since translations preserve standard final configurations, $M ; N$ halts in a standard final configuration with output $g(y)$ if $g(y)\converge$, and otherwise it does not. Hence $M ; N$ computes $g \circ f$.
:::

::::exercise{#ex-tm-clean-halt difficulty=2 objective="Normalize a machine so that all its halting computations end in a standard configuration."}
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

## Exercises

::::exercise{#ex-tm-parity difficulty=1 objective="Use the finite control of a machine to count modulo $2$, and verify it by an invariant."}
Design a $1$-tape machine computing $x \mapsto x \bmod 2$, and prove it correct.

:::solution
Erase the input from left to right, alternating between a state $q_0$ (an even number of $1$s erased so far) and a state $q_1$ (an odd number). Since $\ulcorner x \urcorner$ has $x + 1$ ones, at the first blank the state is $q_1$ if $x$ is even and $q_0$ if $x$ is odd. In the first case write a single $1$ (output $0$); in the second, write two $1$s (output $1$); then halt with the head on the first $1$ written.

| | $1$ | $\sqcup$ |
| --- | --- | --- |
| $q_0$ | $(q_1, \sqcup, R)$ | $(q_2, 1, R)$ |
| $q_1$ | $(q_0, \sqcup, R)$ | $(q_3, 1, L)$ |
| $q_2$ | $(q_h, 1, L)$ | $(q_h, 1, L)$ |
| $q_3$ | $(q_h, 1, R)$ | $(q_h, \sqcup, R)$ |

By induction on $i \leq x + 1$, after $i$ steps the head is on cell $i$, the tape contains $1$s exactly on the cells $i, \dots, x$, and the state is $q_0$ if $i$ is even and $q_1$ if $i$ is odd. For $i = x + 1$ the head scans the blank cell $x + 1$ and the rest of the tape is blank. If $x$ is even, $x + 1$ is odd: the machine writes $1$ on cell $x + 1$, moves to cell $x$, which is blank, in state $q_3$, and halts on cell $x + 1$. The tape is $\ulcorner 0 \urcorner$ from the head. If $x$ is odd, the machine writes $1$ on cell $x + 1$ and moves to cell $x + 2$ in state $q_2$, which writes $1$ there and halts on cell $x + 1$. The tape is $\ulcorner 1 \urcorner$ from the head. The entries $\delta(q_2, 1)$ and $\delta(q_3, 1)$ are never used.
:::
::::

## Notes and references

Markers, subroutines and the composition of machines go back to Turing's paper of 1936, which builds its universal machine from "skeleton tables" that play the role of subroutines. Soare (§1.4) and Boolos, Burgess and Jeffrey (chapter 3) give further exercises in programming Turing machines.

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- R. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §1.4.
- G. Boolos, J. Burgess, R. Jeffrey, *Computability and Logic*, 5th edition, Cambridge University Press, 2007, chapter 3.

:::::exercises
::::exercise{#ex-tm-doubling-steps difficulty=2 objective="Count the steps of the doubling machine exactly from the invariant of its proof."}
Show that the doubling machine of :ref{#prop-tm-doubling} halts on input $x$ after exactly $2(x + 2)^2$ steps.

:::solution
Let $n = x + 1$. Round $j < n$ starts in state $q_0$ on cell $j$ with the tape $X^j 1^{n - j} Y^j$. It takes one step to write $X$ and move to cell $j + 1$; $n - 1$ steps in state $q_1$ to cross the cells $j + 1, \dots, n + j - 1$; one step to write $Y$ on cell $n + j$ and move to cell $n + j - 1$; $n - 1$ steps in state $q_2$ to move from cell $n + j - 1$ to cell $j$; and one step on the $X$ of cell $j$ to return to $q_0$ on cell $j + 1$. That is $2n + 1$ steps per round, and $n(2n + 1)$ for the first phase.

The second phase starts in state $q_0$ on cell $n$. It takes one step to turn the $Y$ of cell $n$ into $1$; $n - 1$ steps in state $q_3$ over the cells $n + 1, \dots, 2n - 1$; one step on the blank cell $2n$ to move back; one step to erase cell $2n - 1$; $2n - 1$ steps in state $q_5$ from cell $2n - 2$ to cell $-1$; and the halting step. That is $3n + 2$ steps. The total is $2n^2 + n + 3n + 2 = 2(n + 1)^2 = 2(x + 2)^2$. For $x = 0$ this gives $8$ steps, which can be checked directly.
:::
::::

::::exercise{#ex-tm-copy difficulty=2 objective="Program a copying machine with markers and an end symbol, and verify it by a round invariant."}
Design a machine which, started on $\ulcorner x \urcorner$ as in the initial configuration, halts with the tape $\ulcorner x \urcorner \sqcup \ulcorner x \urcorner$ written from cell $0$ and the head on cell $0$. Prove that it is correct.

:::solution
Let $n = x + 1$. The machine uses the symbols $X$, $Y$ and $\#$. It first writes $\#$ after the input and returns to cell $0$. Then, in each round, it marks the leftmost $1$ with $X$, goes right to the first blank, writes $Y$ there, and comes back to the rightmost $X$. When the leftmost unmarked symbol is $\#$, all $1$s have been copied; the machine turns the $Y$s into $1$s, then goes left turning $\#$ into a blank and the $X$s into $1$s, and halts on cell $0$.

| | $1$ | $X$ | $Y$ | $\#$ | $\sqcup$ |
| --- | --- | --- | --- | --- | --- |
| $p_0$ | $(p_0, 1, R)$ | | | | $(p_1, \#, L)$ |
| $p_1$ | $(p_1, 1, L)$ | | | | $(q_0, \sqcup, R)$ |
| $q_0$ | $(q_1, X, R)$ | | | $(q_3, \#, R)$ | |
| $q_1$ | $(q_1, 1, R)$ | | $(q_1, Y, R)$ | $(q_1, \#, R)$ | $(q_2, Y, L)$ |
| $q_2$ | $(q_2, 1, L)$ | $(q_0, X, R)$ | $(q_2, Y, L)$ | $(q_2, \#, L)$ | |
| $q_3$ | | | $(q_3, 1, R)$ | | $(q_4, \sqcup, L)$ |
| $q_4$ | $(q_4, 1, L)$ | $(q_4, 1, L)$ | | $(q_4, \sqcup, L)$ | $(q_h, \sqcup, R)$ |

The initial state is $p_0$, and the empty entries are never used (set them to $(q_h, \sqcup, R)$). In state $p_0$ the head crosses cells $0, \dots, n - 1$, writes $\#$ on cell $n$, and $p_1$ returns to cell $0$ in state $q_0$. We show by induction on $j \leq n$ that the machine reaches state $q_0$ on cell $j$ with the tape $X^j\, 1^{n - j}\, \#\, Y^j$ from cell $0$. For $j = 0$ this was just shown. If $j < n$, cell $j$ contains $1$; it is replaced by $X$, $q_1$ crosses $1^{n-j-1} \# Y^j$ to the blank cell $n + j + 1$ and writes $Y$ there, and $q_2$ goes back over $Y^{j+1}$, $\#$ and $1^{n-j-1}$ to the $X$ on cell $j$, and enters $q_0$ on cell $j + 1$. The tape is then $X^{j+1}\, 1^{n-j-1}\, \#\, Y^{j+1}$.

For $j = n$ the tape is $X^n \# Y^n$ and $q_0$ scans $\#$ on cell $n$. Then $q_3$ turns the cells $n + 1, \dots, 2n$ into $1$s and turns back on the blank cell $2n + 1$, and $q_4$ moves left from cell $2n$ to cell $-1$, turning $\#$ into a blank and each $X$ into $1$. It halts on cell $0$, with $1^n \sqcup 1^n$ on the cells $0, \dots, 2n$. Such a machine is the first step of a composition $h(f(x), g(x))$: it gives a copy of the input to each of the two computations.
:::
::::

::::exercise{#ex-tm-naive-composition difficulty=1 objective="See on an example why the composition of machines requires clean halting."}
Let $M$ have the single transition $\delta(q_0, a) = (q_h, \sqcup, R)$ for every symbol $a$, and let $N$ have the states $q_0, q_1, q_h$ and the transitions $\delta(q_0, a) = (q_1, 1, R)$ and $\delta(q_1, a) = (q_h, a, L)$ for every symbol $a$.

1. Determine $\varphi^{(1)}_M$ and $\varphi^{(1)}_N$.
2. Let $M ; N$ be built as in the proof of :ref{#prop-tm-composition}, but from $M$ itself, without applying :ref{#ex-tm-clean-halt} first. Show that $M ; N$ does not compute $\varphi^{(1)}_N \circ \varphi^{(1)}_M$.

:::solution
1. On input $x \geq 1$, $M$ erases cell $0$ and halts on cell $1$; the tape contains $1$s exactly on the cells $1, \dots, x$, a standard final configuration with output $x - 1$. On input $0$, it halts on cell $1$ with a blank tape, which is not standard. So $\varphi^{(1)}_M(x) = x - 1$ for $x \geq 1$, and $\varphi^{(1)}_M(0)\diverge$. On input $y$, $N$ rewrites the $1$ of cell $0$, steps right and back, and halts on cell $0$ with the tape unchanged: $\varphi^{(1)}_N$ is the identity.
2. Hence $\varphi^{(1)}_N \circ \varphi^{(1)}_M$ is undefined at $0$. But $M ; N$ on input $0$ reaches the initial state of $N$ on cell $1$ of a blank tape; $N$ then writes $1$ on cell $1$, moves to cell $2$, moves back to cell $1$ and halts. The tape contains a single $1$, under the head: $M ; N$ outputs $0$ on input $0$. The proof of :ref{#prop-tm-composition} needs every halting computation of $M$ to be standard: here $M$ halts in a non-standard configuration, which $N$ treats as a legitimate input.
:::
::::

::::exercise{#ex-tm-composition-arity difficulty=1 objective="Check that the composition of machines extends to a first machine with several arguments."}
Let $M$ compute $f : \nat^k \rightharpoonup \nat$ and $N$ compute $g : \nat \rightharpoonup \nat$. Show that some machine computes $g \circ f$, by indicating what changes in :ref{#ex-tm-clean-halt} and in the proof of :ref{#prop-tm-composition}.

:::solution
In :ref{#ex-tm-clean-halt}, the only use of the input is to place the right end marker after it. With $k$ arguments, $\widehat M$ crosses $k$ blocks of $1$s separated by single blanks, counting them in its state (which is possible since $k$ is fixed), and writes the marker after the $k$-th block. The rest of the construction is unchanged, so $\widehat M$ computes $f$ in arity $k$ and halts only in standard configurations. The proof of :ref{#prop-tm-composition} never uses the form of the input of $M$: when $\widehat M$ halts, the tape contains exactly $\ulcorner f(\vec x) \urcorner$ from the head, and by :ref{#lem-tm-translation} the machine $N$ then runs as on its initial configuration on $f(\vec x)$. Hence $\widehat M ; N$ computes $g \circ f$ in arity $k$.
:::
::::
:::::
