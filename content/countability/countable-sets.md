---
title: Countable sets
summary: Countable sets; countability of ℕ × ℕ, ℚ and the set of finite strings; Cantor's pairing function.
duration: 15
prerequisites: [cantor-bernstein]
---

A set is countable when its elements can be listed in a sequence $a_0, a_1, a_2, \dots$, possibly with repetitions. Countable sets are the relevant setting for computation: programs, inputs and outputs are finite objects, of which there are countably many.

:::definition{#def-countable}
A set $A$ is **countably infinite** if $|A| = |\nat|$. It is **countable** if it is finite or countably infinite, and **uncountable** otherwise.
:::

Equivalently, a non-empty set $A$ is countable if and only if there is a surjection $\nat \to A$: list the elements, repetitions allowed.

## The smallest infinity

:::proposition{#prop-n-smallest}
Every infinite set $A$ satisfies $|\nat| \leq |A|$.
:::

:::proof{of=prop-n-smallest}
Pick any $a_0 \in A$. Having chosen distinct $a_0, \dots, a_n$, the set $A \setminus \{a_0, \dots, a_n\}$ is non-empty since $A$ is infinite; pick $a_{n+1}$ in it. Then $n \mapsto a_n$ is injective.
:::

(In general, this proof uses the axiom of choice to make infinitely many choices. For subsets of $\nat$ we can always pick the *least* element, so no choice is needed.)

:::corollary{#cor-subset-countable}
Every subset of a countable set is countable.
:::

:::proof{of=cor-subset-countable}
Let $B \subseteq A$ with $A$ countable, and suppose $B$ infinite. Then $|B| \leq |A| \leq |\nat|$, and $|\nat| \leq |B|$ by :ref{#prop-n-smallest}. By :ref{#thm-cantor-bernstein}, $|B| = |\nat|$.
:::

## Pairs, rationals, strings

:::proposition{#prop-nxn-countable}
$\nat \times \nat$ is countably infinite.
:::

:::proof{of=prop-nxn-countable}
List the pairs diagonal by diagonal: first those with $x + y = 0$, then those with $x + y = 1$, and so on, each diagonal in order of increasing $y$:
$$
(0,0),\ (1,0),\ (0,1),\ (2,0),\ (1,1),\ (0,2),\ (3,0),\ \dots
$$
Each diagonal is finite, so every pair appears at a finite position, exactly once. The position of $(x, y)$ is
$$
\langle x, y \rangle = \frac{(x+y)(x+y+1)}{2} + y,
$$
since the diagonals before it contain $1 + 2 + \dots + (x+y) = \frac{(x+y)(x+y+1)}{2}$ pairs.
:::

:::quiz
Why does the proof list pairs **diagonal by diagonal** rather than row by row, $(0,0), (0,1), (0,2), \dots$ and then $(1,0), (1,1), \dots$?

- [x] Row by row, the first row is already infinite, so the pair $(1, 0)$ would never get a finite position.
- [ ] Row by row would list some pairs twice.

  It lists no pair twice — it just never reaches the second row.
- [ ] Because the formula for $\langle x, y \rangle$ only works for diagonals.

  The formula is a consequence of the choice of order, not its reason.

---

Using the formula, what is the position of $(0, 3)$?

- [ ] $3$
- [ ] $6$
- [x] $9$

  $x + y = 3$, so $\frac{3 \cdot 4}{2} + 3 = 9$: it is the last pair of the fourth diagonal $(3,0), (2,1), (1,2), (0,3)$, at positions $6, 7, 8, 9$.
- [ ] $10$
:::

By induction, $\nat^k$ is countable for every $k$. Many more sets follow:

- **The integers $\mathbb Z$**: list $0, 1, -1, 2, -2, \dots$
- **The rationals $\mathbb Q$**: the map $(p, q) \mapsto p / (q+1)$ from $\mathbb Z \times \nat$ onto $\mathbb Q$ is surjective, and $\mathbb Z \times \nat$ is countable.
- **The finite strings** over a finite or countable alphabet: there are countably many strings of each length $k$, and a countable union of countable sets is countable (list the $n$-th element of the $m$-th set at position $\langle m, n \rangle$).

:::quiz
Which of these sets are countable?

- [x] The set of all computer programs (finite strings over the keyboard alphabet).
- [x] The set of finite subsets of $\nat$.

  Each finite set $\{a_1 < \dots < a_k\}$ is described by a finite string.
- [x] The set of polynomials with integer coefficients.

  A polynomial is a finite list of integers.
- [ ] The set of **all** subsets of $\nat$.

  This is the subject of the next lesson.
:::

The first item has the following consequence: there are only countably many programs, hence only countably many computable functions. If there are uncountably many functions $\nat \to \nat$ — which the diagonal argument will show — then most functions are not computable.
