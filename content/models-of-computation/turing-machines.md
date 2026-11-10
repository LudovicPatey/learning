---
title: Turing machines
summary: Formal definition of Turing machines, configurations and computations, input and output conventions, and two machines verified in detail.
duration: 35
prerequisites: [what-is-an-algorithm]
---

Turing's 1936 model arises from an analysis of a human computing with pencil and paper. The paper is replaced by a one-dimensional **tape** divided into cells, each holding one symbol from a finite alphabet. The person's attention is a **head** scanning one cell at a time. Their state of mind, which can only take finitely many values, is the **state** of the machine. At each step, the action depends only on the current state and on the scanned symbol, and consists in writing a symbol, moving one cell left or right, and changing state.


:::figure[The components of a Turing machine. The head scans one cell; the finite control holds the current state; each step is determined by the state and the scanned symbol.]
<svg class="fig" viewBox="0 0 540 230" width="540" role="img" aria-label="A Turing machine: tape, head and finite control"><text x="12" y="74" class="mrm muted" font-size="18">⋯</text><rect class="cell" x="30" y="46" width="42" height="42" rx="3"/><text x="51.0" y="74" text-anchor="middle" class="mrm muted" font-size="18">⊔</text><rect class="cell" x="72" y="46" width="42" height="42" rx="3"/><text x="93.0" y="74" text-anchor="middle" class="mrm muted" font-size="18">⊔</text><rect class="cell" x="114" y="46" width="42" height="42" rx="3"/><text x="135.0" y="74" text-anchor="middle" class="mrm " font-size="18">1</text><rect class="cell" x="156" y="46" width="42" height="42" rx="3"/><text x="177.0" y="74" text-anchor="middle" class="mrm " font-size="18">1</text><rect class="cell head-cell" x="198" y="46" width="42" height="42" rx="3"/><text x="219.0" y="74" text-anchor="middle" class="mrm " font-size="18">1</text><rect class="cell" x="240" y="46" width="42" height="42" rx="3"/><text x="261.0" y="74" text-anchor="middle" class="mrm muted" font-size="18">⊔</text><rect class="cell" x="282" y="46" width="42" height="42" rx="3"/><text x="303.0" y="74" text-anchor="middle" class="mrm " font-size="18">1</text><rect class="cell" x="324" y="46" width="42" height="42" rx="3"/><text x="345.0" y="74" text-anchor="middle" class="mrm " font-size="18">1</text><rect class="cell" x="366" y="46" width="42" height="42" rx="3"/><text x="387.0" y="74" text-anchor="middle" class="mrm muted" font-size="18">⊔</text><rect class="cell" x="408" y="46" width="42" height="42" rx="3"/><text x="429.0" y="74" text-anchor="middle" class="mrm muted" font-size="18">⊔</text><rect class="cell" x="450" y="46" width="42" height="42" rx="3"/><text x="471.0" y="74" text-anchor="middle" class="mrm muted" font-size="18">⊔</text><text x="500" y="74" class="mrm muted" font-size="18">⋯</text><path d="M210.0,24 L228.0,24 L219.0,40 z" class="accent-fill"/><text x="219.0" y="18" text-anchor="middle" class="label">head</text><text x="408" y="34" text-anchor="middle" class="label">tape</text><line x1="219.0" y1="88" x2="219.0" y2="140" class="accent-stroke" stroke-width="1.5" stroke-dasharray="4 3"/><rect x="139.0" y="140" width="160" height="72" rx="10" class="soft-fill accent-stroke" stroke-width="1.5"/><text x="219.0" y="160" text-anchor="middle" class="label">finite control</text><text x="219.0" y="194" text-anchor="middle" class="math" font-size="24">q<tspan class="mrm" font-size="14" dy="4">3</tspan></text><text x="330" y="160" class="math" font-size="17">δ<tspan class="mrm">(</tspan>q<tspan class="mrm">,</tspan> a<tspan class="mrm">) = (</tspan>q<tspan class="mrm">′,</tspan> b<tspan class="mrm">,</tspan> D<tspan class="mrm">)</tspan></text><text x="330" y="184" class="label">read a, write b,</text><text x="330" y="201" class="label">move one cell in direction D,</text><text x="330" y="218" class="label">enter the state q′</text></svg>
:::
## Definition

:::definition{#def-turing-machine}
A **Turing machine** is a tuple $M = (Q, \Gamma, \delta, q_0, q_h)$ where

- $Q$ is a finite set of **states**, with an **initial state** $q_0 \in Q$ and a **halting state** $q_h \in Q$, $q_h \neq q_0$;
- $\Gamma$ is a finite **alphabet** containing at least the **blank** symbol $\sqcup$ and the symbol $1$;
- $\delta : (Q \setminus \{q_h\}) \times \Gamma \to Q \times \Gamma \times \{L, R\}$ is the **transition function**.
:::

An entry $\delta(q, a) = (q', b, D)$ reads: *in state $q$, scanning $a$, write $b$, move in direction $D$, and enter state $q'$*. Since $\delta$ is defined on all pairs $(q, a)$ with $q \neq q_h$, the machine can always perform a step unless it is in the halting state. A machine is a finite object: it can be written as a finite table, and there are only countably many machines (up to renaming of states and symbols).

To describe the state of a computation, we index the cells of the tape by $\mathbb{Z}$.

:::definition{#def-tm-configuration}
A **tape** is a function $\tau : \mathbb{Z} \to \Gamma$ such that $\tau(i) = \sqcup$ for all but finitely many $i$. A **configuration** of $M$ is a triple $C = (q, \tau, h)$ where $q \in Q$, $\tau$ is a tape and $h \in \mathbb{Z}$ is the **head position**. The configuration is **halting** if $q = q_h$.

If $C = (q, \tau, h)$ is not halting and $\delta(q, \tau(h)) = (q', b, D)$, the **successor** of $C$ is the configuration $C' = (q', \tau', h')$ where
$$
\tau'(i) = \begin{cases} b & \text{if } i = h, \\ \tau(i) & \text{otherwise,} \end{cases} \qquad h' = \begin{cases} h - 1 & \text{if } D = L, \\ h + 1 & \text{if } D = R. \end{cases}
$$
We write $C \vdash_M C'$, or simply $C \vdash C'$.
:::

Every non-halting configuration has exactly one successor, and a halting configuration has none: Turing machines are **deterministic**.

:::definition{#def-tm-run}
The **computation** of $M$ from a configuration $C_0$ is the sequence $C_0 \vdash C_1 \vdash C_2 \vdash \cdots$, which is either infinite, or finite and ends with the first halting configuration $C_t$. In the second case we say that $M$ **halts** from $C_0$ after $t$ steps, with **final configuration** $C_t$.
:::

## Computing functions

To compute functions on integers we fix conventions for representing inputs and outputs on the tape. We use unary notation, representing $x \in \nat$ by $x + 1$ consecutive $1$s:
$$
\ulcorner x \urcorner = 1^{x+1}.
$$
Using $x+1$ rather than $x$ symbols ensures that every number, including $0$, occupies at least one cell, so that a tuple of numbers separated by single blanks can be read unambiguously.

:::definition{#def-tm-computes}
Let $M$ be a Turing machine and $k \geq 1$.

- The **initial configuration** on input $\vec x = (x_1, \dots, x_k)$ is $(q_0, \tau_{\vec x}, 0)$, where the tape $\tau_{\vec x}$ contains the word $\ulcorner x_1 \urcorner \sqcup \ulcorner x_2 \urcorner \sqcup \cdots \sqcup \ulcorner x_k \urcorner$ written from cell $0$ onwards, and blanks elsewhere.
- A configuration $(q_h, \tau, h)$ is a **standard final configuration with output $y$** if $\tau(i) = 1$ for $h \leq i \leq h + y$ and $\tau(i) = \sqcup$ for all other $i$: the tape contains exactly $\ulcorner y \urcorner$, and the head scans its first cell.

The partial function $\varphi^{(k)}_M : \nat^k \rightharpoonup \nat$ **computed by $M$** is defined by: $\varphi^{(k)}_M(\vec x)\converge = y$ if the computation of $M$ from the initial configuration on input $\vec x$ halts in a standard final configuration with output $y$, and $\varphi^{(k)}_M(\vec x)\diverge$ otherwise.

A partial function $f : \nat^k \rightharpoonup \nat$ is **Turing-computable** if $f = \varphi^{(k)}_M$ for some machine $M$.
:::

Note that $\varphi^{(k)}_M(\vec x)$ is undefined both when the computation does not halt and when it halts in a non-standard configuration. With this convention every machine computes exactly one $k$-ary partial function, for each $k$.

:::remark
The precise conventions — unary or binary notation, a tape infinite in one or both directions, a cleaned tape at the end or not — vary between textbooks. They change the machines, but not the class of Turing-computable functions. The robustness of the class under such changes is discussed in the next lesson.
:::

## First example: the successor function

Let $M_S$ be the machine with states $\{q_0, q_1, q_h\}$, alphabet $\{\sqcup, 1\}$, and transitions

| | $1$ | $\sqcup$ |
| --- | --- | --- |
| $q_0$ | $(q_0, 1, R)$ | $(q_1, 1, L)$ |
| $q_1$ | $(q_1, 1, L)$ | $(q_h, \sqcup, R)$ |

:::figure[State diagram of $M_S$. An edge labelled $a / b, D$ from $q$ to $q'$ means $\delta(q, a) = (q', b, D)$; the halting state is circled twice.]
<svg class="fig" viewBox="0 0 540 175" width="540" role="img" aria-label="State diagram of the successor machine"><defs><marker id="ah-succ" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="40" y1="110" x2="92" y2="110" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-succ)"/><text x="44" y="102" class="label">start</text><circle cx="120" cy="110" r="26" class="state"/><text x="120" y="115" text-anchor="middle" class="math" font-size="17">q<tspan class="mrm" font-size="10" dy="4">0</tspan></text><circle cx="300" cy="110" r="26" class="state"/><text x="300" y="115" text-anchor="middle" class="math" font-size="17">q<tspan class="mrm" font-size="10" dy="4">1</tspan></text><circle cx="460" cy="110" r="26" class="state"/><circle cx="460" cy="110" r="21" class="state-inner"/><text x="460" y="115" text-anchor="middle" class="math" font-size="17">q<tspan class="mrm" font-size="10" dy="4">h</tspan></text><line x1="147" y1="110" x2="272" y2="110" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-succ)"/><text x="209.5" y="101" text-anchor="middle" class="mrm" font-size="15">⊔ / 1, L</text><line x1="327" y1="110" x2="432" y2="110" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-succ)"/><text x="379.5" y="101" text-anchor="middle" class="mrm" font-size="15">⊔ / ⊔, R</text><path d="M108,87 C80,28 160,28 132,86" class="ink-stroke" fill="none" stroke-width="1.4" marker-end="url(#ah-succ)"/><text x="120" y="38" text-anchor="middle" class="mrm" font-size="15">1 / 1, R</text><path d="M288,87 C260,28 340,28 312,86" class="ink-stroke" fill="none" stroke-width="1.4" marker-end="url(#ah-succ)"/><text x="300" y="38" text-anchor="middle" class="mrm" font-size="15">1 / 1, L</text></svg>
:::

In state $q_0$ the head runs right across the input. On the first blank it writes a $1$ and turns back in state $q_1$, runs left to the blank preceding the block, and steps back onto the first $1$.

:::proposition{#prop-tm-successor}
$M_S$ computes the successor function: $\varphi^{(1)}_{M_S}(x) = x + 1$ for every $x$.
:::

:::proof{of=prop-tm-successor}
Write $\tau_n$ for the tape containing $1$s exactly on the cells $0, \dots, n$. The initial configuration on input $x$ is $(q_0, \tau_x, 0)$. For $i \leq x$, the cell $i$ contains $1$, so by the first transition
$$
(q_0, \tau_x, 0) \vdash (q_0, \tau_x, 1) \vdash \cdots \vdash (q_0, \tau_x, x+1).
$$
Cell $x+1$ is blank, so the next configuration is $(q_1, \tau_{x+1}, x)$. For $0 \leq i \leq x$ the cell $i$ contains $1$, so
$$
(q_1, \tau_{x+1}, x) \vdash (q_1, \tau_{x+1}, x - 1) \vdash \cdots \vdash (q_1, \tau_{x+1}, -1).
$$
Cell $-1$ is blank, so the next configuration is $(q_h, \tau_{x+1}, 0)$. This is a standard final configuration with output $x + 1$, reached after $2x + 4$ steps.
:::

The proof follows a pattern used for all such verifications: describe the configurations at the beginning and at the end of each phase of the computation, and check each phase by induction on the number of steps.

:::quiz[the successor machine]
What is $\varphi^{(2)}_{M_S}(x, y)$, the binary function computed by the same machine?

- [x] $x + y + 2$.

  On input $\ulcorner x \urcorner \sqcup \ulcorner y \urcorner$, the head stops in state $q_0$ on the separator (cell $x+1$), writes a $1$ there, and returns to cell $0$. The final tape contains $x + y + 3$ consecutive $1$s, a standard configuration with output $x + y + 2$.
- [ ] $x + 1$.

  The machine does not stop at the end of the input but at the first blank, which is the separator.
- [ ] It is undefined everywhere.

  The final configuration is standard.
:::

## Second example: addition

The machine $M_+$ below computes $(x, y) \mapsto x + y$. On input $\ulcorner x \urcorner \sqcup \ulcorner y \urcorner$, it replaces the separating blank by a $1$, which produces a block of $x + y + 3$ ones; it then erases the last two $1$s and returns to the beginning of the block.

| | $1$ | $\sqcup$ |
| --- | --- | --- |
| $q_0$ | $(q_0, 1, R)$ | $(q_1, 1, R)$ |
| $q_1$ | $(q_1, 1, R)$ | $(q_2, \sqcup, L)$ |
| $q_2$ | $(q_3, \sqcup, L)$ | $(q_h, \sqcup, R)$ |
| $q_3$ | $(q_4, \sqcup, L)$ | $(q_h, \sqcup, R)$ |
| $q_4$ | $(q_4, 1, L)$ | $(q_h, \sqcup, R)$ |

The entries $\delta(q_2, \sqcup)$ and $\delta(q_3, \sqcup)$ are never used on inputs of the required form; they are only there to make $\delta$ total.

:::proposition{#prop-tm-addition}
$M_+$ computes addition: $\varphi^{(2)}_{M_+}(x, y) = x + y$ for all $x, y$.
:::

:::proof{of=prop-tm-addition}
The initial tape has $1$s on the cells $0, \dots, x$ and $x + 2, \dots, x + y + 2$, and a blank on cell $x + 1$. In state $q_0$ the head moves right to cell $x + 1$, writes $1$ there and moves to cell $x + 2$ in state $q_1$. Now the tape contains $1$s exactly on $0, \dots, x + y + 2$. In state $q_1$ the head moves right to cell $x + y + 3$, which is blank, and moves back to cell $x + y + 2$ in state $q_2$. It erases this cell and moves to cell $x + y + 1$ in state $q_3$. Since $x + y + 1 \geq 1$, this cell contains $1$; it is erased and the head moves to cell $x + y$ in state $q_4$. The tape now contains $1$s exactly on $0, \dots, x + y$. As in the previous proof, $q_4$ runs left to cell $-1$, and the machine halts with the head on cell $0$. The final configuration is standard with output $x + y$.
:::

:::quiz[the addition machine]
In the proof, where is the inequality $x + y + 1 \geq 1$ used?

- [x] To know that cell $x + y + 1$ still contains a $1$ when the machine enters state $q_3$, so that the transition $\delta(q_3, 1)$ applies.
- [ ] To ensure that the machine halts in state $q_4$.

  Termination of the last phase only uses that the block of $1$s is finite.
- [ ] To guarantee that the separator cell $x + 1$ is blank.

  That is part of the input convention.

---

Suppose we had represented $x$ by $x$ ones instead of $x + 1$. What would go wrong with the input convention for two arguments?

- [x] Zero would be represented by an empty block, so blocks could no longer be delimited.

  For instance, the inputs $(1)$, $(1, 0)$ and $(1, 0, 0)$ would all give the tape with a single $1$ on cell $0$, and $(0, 0)$ would give the blank tape. A machine scanning the tape could not tell where the input ends.
- [ ] Nothing: unary with $x$ ones works equally well for several arguments.

  With $x$ ones, the number $0$ would be written as an empty block, and inputs such as $(1)$ and $(1, 0)$ would give the same tape.
- [ ] The successor machine would no longer be correct.

  The successor machine can be adapted; the issue is the representation of tuples.
:::

## Exercises

::::exercise{difficulty=1}
Give a machine computing the constant function $x \mapsto 0$, and prove that it is correct.

:::solution
The machine must erase all $1$s but the first and return to cell $0$:

| | $1$ | $\sqcup$ |
| --- | --- | --- |
| $q_0$ | $(q_1, 1, R)$ | $(q_h, \sqcup, R)$ |
| $q_1$ | $(q_1, \sqcup, R)$ | $(q_2, \sqcup, L)$ |
| $q_2$ | $(q_3, 1, L)$ | $(q_2, \sqcup, L)$ |
| $q_3$ | $(q_h, 1, R)$ | $(q_h, \sqcup, R)$ |

On input $x$ the head steps from cell $0$ to cell $1$ in state $q_1$, erases cells $1, \dots, x$ and reaches the blank cell $x + 1$, moves back to cell $x$ in state $q_2$, moves left over the blanks $x, \dots, 1$ to cell $0$, which contains $1$, moves to cell $-1$ in state $q_3$, and finally halts on cell $0$. The tape contains a single $1$ on cell $0$: the output is $0$. The entries $\delta(q_0, \sqcup)$ and $\delta(q_3, 1)$ are never used.
:::
::::

::::exercise{difficulty=1}
Give a machine computing the projection $(x, y) \mapsto x$.

:::solution
Run right to the separator, step over it, erase the block $\ulcorner y \urcorner$ until reaching the blank after it, then run left over blanks until the last $1$ of $\ulcorner x \urcorner$, then left over the $1$s to cell $-1$, and step right:

| | $1$ | $\sqcup$ |
| --- | --- | --- |
| $q_0$ | $(q_0, 1, R)$ | $(q_1, \sqcup, R)$ |
| $q_1$ | $(q_1, \sqcup, R)$ | $(q_2, \sqcup, L)$ |
| $q_2$ | $(q_3, 1, L)$ | $(q_2, \sqcup, L)$ |
| $q_3$ | $(q_3, 1, L)$ | $(q_h, \sqcup, R)$ |

In state $q_2$, the head moves left over the erased cells and the separator until it reaches cell $x$, the last $1$ of the first block.
:::
::::

::::exercise{difficulty=1}
Show that every Turing-computable partial function is computed by infinitely many machines. Show that there are only countably many Turing-computable partial functions $\nat \rightharpoonup \nat$, and deduce that there is a total function $\nat \to \nat$ which is not Turing-computable.

:::solution
Adding to a machine states that are never entered does not change its computations, so each computable function has infinitely many machines. Up to renaming, a machine is determined by finitely many data — the numbers of states and symbols, and the table of $\delta$ — so it can be described by a finite string over a finite alphabet, and there are countably many machines; hence countably many computable functions. The set of total functions $\nat \to \nat$ is uncountable (by a diagonal argument, see :ref{to="countability/diagonal-argument"}), so some total function is not computable.
:::
::::

## Notes and references

Turing's machines (1936) differ from ours in inessential details: they compute infinite binary sequences rather than functions, and halting plays no role. Post introduced an almost identical model independently in the same year. The conventions used here — unary notation with $x+1$ strokes and a standard final configuration — follow Boolos, Burgess and Jeffrey.

- E. L. Post, *Finite combinatory processes — formulation 1*, Journal of Symbolic Logic 1 (1936), 103–105.
- G. Boolos, J. Burgess, R. Jeffrey, *Computability and Logic*, 5th edition, Cambridge University Press, 2007.
