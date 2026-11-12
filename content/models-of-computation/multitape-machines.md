---
title: Variants of Turing machines
summary: Multi-tape machines and their simulation by single-tape machines; other variants of the model, which compute the same partial functions.
duration: 35
prerequisites: [programming-turing-machines]
---

The definition of Turing machines involves arbitrary choices: one tape, one head, a tape infinite in both directions, deterministic transitions. If the class of computable functions depended on them, it would be a poor candidate for a definition of computability. This lesson shows that it does not, by the technique of **simulation**: a machine of the richer model is imitated, step by step, by a machine of the poorer one, which stores the richer data structure in a coded form. The same technique proves, in the lesson :ref{to="models-of-computation/equivalence-of-models"}, that Turing machines compute every function computed by a register machine.

## Multi-tape machines

A natural extension gives the machine several tapes, each with its own head.

:::definition{#def-multitape}
A **$k$-tape Turing machine** is defined as in :ref{#def-turing-machine}, except that the transition function has the form
$$
\delta : (Q \setminus \{q_h\}) \times \Gamma^k \to Q \times \Gamma^k \times \{L, S, R\}^k,
$$
where $S$ means that the head stays in place. A configuration consists of a state, $k$ tapes and $k$ head positions. By convention all heads start on cell $0$, the input is written on tape $1$ as in :ref{#def-tm-computes}, the other tapes are initially blank, and the output is read on tape $1$: the machine computes $y$ if it halts with tape $1$ and head $1$ in a standard final configuration with output $y$, whatever the contents of the other tapes.
:::

Multi-tape machines are much easier to program, because a second tape can serve as scratch memory without disturbing the first.

:::example{#ex-two-tape-doubling}
The following $2$-tape machine computes $x \mapsto 2x$. Write $n = x + 1$, so that tape $1$ initially holds $1^n$ and the output must be $1^{2n - 1}$. An entry gives the next state, the pair of symbols written, and the pair of moves; pairs of scanned symbols not listed do not occur.

| state | scanned | next | written | moves |
| --- | --- | --- | --- | --- |
| $q_0$ | $(1, \sqcup)$ | $q_1$ | $(1, \sqcup)$ | $(R, S)$ |
| $q_1$ | $(1, \sqcup)$ | $q_1$ | $(1, 1)$ | $(R, R)$ |
| $q_1$ | $(\sqcup, \sqcup)$ | $q_2$ | $(\sqcup, \sqcup)$ | $(S, L)$ |
| $q_2$ | $(\sqcup, 1)$ | $q_2$ | $(1, \sqcup)$ | $(R, L)$ |
| $q_2$ | $(\sqcup, \sqcup)$ | $q_3$ | $(\sqcup, \sqcup)$ | $(L, S)$ |
| $q_3$ | $(1, \sqcup)$ | $q_3$ | $(1, \sqcup)$ | $(L, S)$ |
| $q_3$ | $(\sqcup, \sqcup)$ | $q_h$ | $(\sqcup, \sqcup)$ | $(R, S)$ |

In state $q_1$ the machine copies the last $n - 1$ symbols of the input to cells $0, \dots, n - 2$ of tape $2$, and reaches cell $n$ of tape $1$. In state $q_2$, head $2$ moves left over this copy, erasing it, while head $1$ appends one $1$ per erased symbol, on cells $n, \dots, 2n - 2$. In state $q_3$, head $1$ returns to cell $0$. The final tape $1$ is $1^{2n - 1}$, tape $2$ is blank, and the computation takes about $4n$ steps. The single-tape machine of :ref{#prop-tm-doubling} needs a number of steps of the order of $n^2$, because its single head must travel between the input and the copy for every symbol.
:::

How can one head do the work of $k$ heads? The obstacle is that the $k$ heads of $M$ scan $k$ cells that may be far apart, and a single head can only see one cell at a time. The simulation stores the $k$ tapes one above the other, marks the cells scanned by the $k$ heads, and replaces each step of $M$ by a sweep over the used part of the tape, which first reads the $k$ marked symbols and then updates them.

:::figure[The simulation of a $3$-tape machine: each cell of the single tape stores one cell of every tape, together with a mark telling whether the corresponding head is there.]
<svg class="fig" viewBox="0 0 600 205" width="600" role="img" aria-label="Three tapes encoded as three tracks of one tape"><defs><marker id="ah-tracks" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="8" y="54" class="label">tape 1</text><rect x="60" y="34" width="30" height="30" rx="2" class="cell"/><text x="75.0" y="54" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="90" y="34" width="30" height="30" rx="2" class="cell"/><text x="105.0" y="54" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="120" y="34" width="30" height="30" rx="2" class="cell head-cell"/><text x="135.0" y="54" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="150" y="34" width="30" height="30" rx="2" class="cell"/><text x="165.0" y="54" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="180" y="34" width="30" height="30" rx="2" class="cell"/><text x="195.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="210" y="34" width="30" height="30" rx="2" class="cell"/><text x="225.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><path d="M129.0,21 L141.0,21 L135.0,31 z" class="accent-fill"/><text x="8" y="110" class="label">tape 2</text><rect x="60" y="90" width="30" height="30" rx="2" class="cell"/><text x="75.0" y="110" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="90" y="90" width="30" height="30" rx="2" class="cell head-cell"/><text x="105.0" y="110" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="120" y="90" width="30" height="30" rx="2" class="cell"/><text x="135.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="150" y="90" width="30" height="30" rx="2" class="cell"/><text x="165.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="180" y="90" width="30" height="30" rx="2" class="cell"/><text x="195.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="210" y="90" width="30" height="30" rx="2" class="cell"/><text x="225.0" y="110" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><path d="M99.0,77 L111.0,77 L105.0,87 z" class="accent-fill"/><text x="8" y="166" class="label">tape 3</text><rect x="60" y="146" width="30" height="30" rx="2" class="cell"/><text x="75.0" y="166" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="90" y="146" width="30" height="30" rx="2" class="cell"/><text x="105.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="120" y="146" width="30" height="30" rx="2" class="cell"/><text x="135.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="150" y="146" width="30" height="30" rx="2" class="cell"/><text x="165.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="180" y="146" width="30" height="30" rx="2" class="cell head-cell"/><text x="195.0" y="166" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="210" y="146" width="30" height="30" rx="2" class="cell"/><text x="225.0" y="166" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><path d="M189.0,133 L201.0,133 L195.0,143 z" class="accent-fill"/><line x1="255" y1="104" x2="315" y2="104" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-tracks)"/><text x="335" y="22" class="label">one tape, three tracks</text><rect x="335" y="34" width="44" height="34" class="cell"/><text x="357.0" y="56" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="335" y="68" width="44" height="34" class="cell"/><text x="357.0" y="90" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="335" y="102" width="44" height="34" class="cell"/><text x="357.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="335" y="34" width="44" height="102" class="track-outline"/><rect x="379" y="34" width="44" height="34" class="cell"/><text x="401.0" y="56" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="379" y="68" width="44" height="34" class="cell head-cell"/><text x="401.0" y="90" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="379" y="102" width="44" height="34" class="cell"/><text x="401.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="379" y="34" width="44" height="102" class="track-outline"/><rect x="423" y="34" width="44" height="34" class="cell head-cell"/><text x="445.0" y="56" text-anchor="middle" class="mrm" font-size="15">b</text><rect x="423" y="68" width="44" height="34" class="cell"/><text x="445.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="423" y="102" width="44" height="34" class="cell"/><text x="445.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="423" y="34" width="44" height="102" class="track-outline"/><rect x="467" y="34" width="44" height="34" class="cell"/><text x="489.0" y="56" text-anchor="middle" class="mrm" font-size="15">a</text><rect x="467" y="68" width="44" height="34" class="cell"/><text x="489.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="467" y="102" width="44" height="34" class="cell"/><text x="489.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="467" y="34" width="44" height="102" class="track-outline"/><rect x="511" y="34" width="44" height="34" class="cell"/><text x="533.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="511" y="68" width="44" height="34" class="cell"/><text x="533.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="511" y="102" width="44" height="34" class="cell head-cell"/><text x="533.0" y="124" text-anchor="middle" class="mrm" font-size="15">c</text><rect x="511" y="34" width="44" height="102" class="track-outline"/><rect x="555" y="34" width="44" height="34" class="cell"/><text x="577.0" y="56" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="555" y="68" width="44" height="34" class="cell"/><text x="577.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="555" y="102" width="44" height="34" class="cell"/><text x="577.0" y="124" text-anchor="middle" class="mrm muted" font-size="15">⊔</text><rect x="555" y="34" width="44" height="102" class="track-outline"/><text x="335" y="160" class="label">a shaded cell carries the head mark of its track</text></svg>
:::

:::theorem{#thm-multitape-simulation}
Every partial function computed by a $k$-tape Turing machine is computed by a $1$-tape Turing machine.
:::

:::proof{of=thm-multitape-simulation}
Let $M$ be a $k$-tape machine with alphabet $\Gamma$. The idea is to store the $k$ tapes on $k$ **tracks** of a single tape. Let the new alphabet be $\Gamma \cup (\Gamma \times \{0, 1\})^k$: a cell of the simulating machine $N$ contains either a symbol of $\Gamma$, or a $k$-tuple of pairs $(a_i, m_i)$ where $a_i$ is the content of the corresponding cell of tape $i$ and $m_i = 1$ indicates that the head of tape $i$ is at this cell. This alphabet is finite.

$N$ first converts cell $0$ into this format: it replaces the symbol $a$ there by $((a, 1), (\sqcup, 1), \dots, (\sqcup, 1))$, since all heads of $M$ start on cell $0$. Then $N$ simulates each step of $M$ as follows. The state of $M$ is stored in the state of $N$. $N$ sweeps over the zone of the tape visited so far, from left to right, and collects in its state the symbols under the $k$ marked heads; there are finitely many possibilities, so they can be stored in the state. Knowing the state of $M$ and the scanned symbols, $N$ determines the transition of $M$. It then sweeps back from right to left, updating the symbol under each marked head and moving each mark by one cell according to the transition. When a mark must move onto a cell containing a plain symbol $a$ of $\Gamma$ — a cell that no head has visited yet — $N$ first replaces it by $((a, 0), (\sqcup, 0), \dots, (\sqcup, 0))$; this is the correct content, since an unvisited cell of tape $1$ still holds its input symbol and an unvisited cell of another tape is blank. Since all heads start on cell $0$ and move by one cell at a time, the converted cells always form an interval containing $0$, bordered by plain symbols, so $N$ recognizes the ends of the zone it must sweep. When $M$ halts, $N$ converts the tape back, keeping only track $1$, moves the head to the position of head $1$, and halts.

By induction on the number of steps, after the simulation of $t$ steps of $M$, the tracks of $N$ contain the tapes of $M$ after $t$ steps, with the heads correctly marked, and the cells outside the converted zone hold the unvisited part of tape $1$. Hence, if $M$ halts, the final tape and head position of $N$ are those of tape $1$ of $M$, so $N$ halts in a standard final configuration exactly when $M$ does, with the same output; and if $M$ does not halt, neither does $N$.
:::

:::quiz[the multi-tape simulation]
Why can the symbols under the $k$ heads be "stored in the state" of $N$ during a sweep?

- [x] There are only $|\Gamma|^k$ possible tuples of scanned symbols, so $N$ can have one copy of its sweeping states for each tuple collected so far, together with the current state of $M$.

  This keeps the set of states of $N$ finite: a sweeping state records a state of $M$ and, for each head, either the symbol already collected or the fact that it has not been met yet, so there are about $|Q| \cdot (|\Gamma| + 1)^k$ of them.
- [ ] Because $N$ has $k$ tapes as well.

  $N$ has a single tape.
- [ ] Because the heads of $M$ are always on the same cell.

  The heads of $M$ move independently.

---

If $M$ halts after $t$ steps, roughly how many steps does $N$ take?

- [x] $O(t^2)$, since after $t$ steps the visited zone has length $O(t)$ and each simulated step costs a constant number of sweeps over it.
- [ ] $O(t)$.

  Each simulated step may require a sweep over the whole visited zone, of length $O(t)$, so the cost is not constant per step.
- [ ] $O(2^t)$.

  The visited zone grows at most linearly, so each simulated step costs $O(t)$, for $O(t^2)$ in total.
:::

## Other variants

The same method — encode the richer structure on one tape, simulate step by step — shows that the following variants compute exactly the Turing-computable functions:

- machines whose tape is infinite only to the right (fold the two-way tape on itself, using two tracks);
- machines with a two-dimensional tape (store the finite non-blank region row by row);
- machines with the alphabet $\{\sqcup, 1\}$ only (encode each symbol of a larger alphabet by a fixed-length block of $\sqcup$ and $1$);
- **non-deterministic** machines, where $\delta$ is a relation, and a function value is accepted if *some* computation produces it, provided the function is well defined (simulate all computations in breadth-first order, using a third tape).

Some care is needed with the input and output conventions in each case, but no new idea. The exercises below treat the first variant.

The variants also show what the definition does **not** depend on. Every model above is still a finite control acting locally on a discrete memory, which is why each simulates the others. The lesson :ref{to="models-of-computation/church-turing-thesis"} returns to the question of which features of a model are responsible for this robustness.

## Exercises

::::exercise{difficulty=2 #ex-one-way-tape}
A **one-way** machine has a tape indexed by $\nat$ instead of $\mathbb{Z}$; a move to the left on cell $0$ leaves the head on cell $0$. Show that the computation of an ordinary machine $M$ from a configuration whose tape is blank on the negative cells can be simulated step by step by a one-way machine.

:::hint
Fold the tape at cell $0$: store cell $p \geq 0$ of $M$ on an upper track and cell $-p - 1$ on a lower track, and keep in the state the track on which the head of $M$ currently is.
:::

:::solution
The one-way machine $N$ uses cell $0$ for an end marker $\triangleright$, and stores in cell $j \geq 1$ the pair $(\tau(j - 1), \tau(-j))$: position $p \geq 0$ of $M$ is the upper track of cell $p + 1$, and position $p < 0$ is the lower track of cell $-p$. $N$ starts by shifting the contents of its tape one cell to the right, writing $\triangleright$ on cell $0$ and pairing each symbol with $\sqcup$, which is correct since the negative cells of $M$ are blank. Its states are the states of $M$ together with a flag *up* or *down*, and a step of $M$ is simulated as follows: read and write the component given by the flag; on the upper track move as $M$ moves, on the lower track move in the opposite direction. When the head arrives on $\triangleright$, it has just left the position $0$ to the left (flag *up*) or the position $-1$ to the right (flag *down*); $N$ then switches the flag and moves back right onto cell $1$, which holds both positions $0$ and $-1$. By induction on the number of steps, after each simulated step the two tracks hold the tape of $M$, the head of $N$ is on the cell holding the position of the head of $M$, and the flag tells which track. The head of $N$ is on cell $0$ only between these two moves, and leaves it to the right, so the convention for left moves on cell $0$ is never used.
:::
::::

::::exercise{difficulty=2}
Describe a $2$-tape machine computing $(x, y) \mapsto x \cdot y$, and estimate its number of steps.

:::solution
Use an auxiliary symbol $\#$ and a marker $X$. First copy $\ulcorner y \urcorner$ to tape $2$ without its last $1$, starting on cell $0$, erasing it from tape $1$, and replace the last $1$ of $\ulcorner x \urcorner$ (cell $x$) by $\#$. Now tape $1$ holds $1^x \#$ on cells $0, \dots, x$, tape $2$ holds $y$ ones on cells $0, \dots, y - 1$, and the output will be built on tape $1$ from cell $x + 1$ on. Each round starts with head $1$ on the leftmost $1$ of the first block and head $2$ on cell $0$: replace this $1$ by $X$, move head $1$ right past $\#$ to the first blank after the output zone, then move both heads right together while head $2$ reads $1$, writing a $1$ with head $1$ at each step; finally return head $2$ to cell $0$, and head $1$ left to the rightmost $X$ and one cell further right. When head $1$ starts a round on $\#$, all $x$ rounds are done and the output zone holds $xy$ ones: append one more $1$ (unary convention), go back to cell $-1$, and move right erasing the $X$s and $\#$, halting on cell $x + 1$, the first cell of $\ulcorner xy \urcorner$. The contents of tape $2$ do not matter. The first phase takes $O(x + y)$ steps, and each round $O(x + y + xy)$ steps, since head $1$ crosses the output zone twice; the total is $O(x^2(y + 1) + y)$ steps.
:::
::::


## Notes and references

The simulation of multi-tape machines by single-tape machines, with a quadratic slowdown, is due to Hartmanis and Stearns, who used it in the foundational paper of complexity theory. The study of such simulations and of their cost belongs to complexity theory, where the robustness of the class of polynomial-time computable functions plays the role that the robustness of the computable functions plays here.

- J. Hartmanis, R. E. Stearns, *On the computational complexity of algorithms*, Transactions of the American Mathematical Society 117 (1965), 285–306.
- M. Sipser, *Introduction to the Theory of Computation*, 3rd edition, Cengage, 2012, chapter 3.
