---
title: Kleene's fixed point theorem
summary: Every total computable transformation of indices has a fixed point up to the function computed; the version with parameters; self-referential programs and applications.
duration: 45
prerequisites: [universal-program-smn, ce-sets]
---

Kleene's fixed point theorem, also called the **recursion theorem**, states that every total computable transformation of indices has a fixed point, in the sense that some index and its image compute the same function. Its main use is to build programs that refer to their own index: one may define a program by a description that mentions its own index, and the theorem guarantees that such a program exists. This device is used throughout computability theory, from Rice's theorem to the constructions of the theory of c.e. degrees.

## The theorem

:::theorem[Fixed point theorem]{#thm-fixed-point}
For every total computable function $f : \nat \to \nat$, there is $e \in \nat$ such that $\Phi_{f(e)} = \Phi_e$.
:::

The equality is between partial functions: $\Phi_{f(e)}(x) \simeq \Phi_e(x)$ for every $x$. In general $f(e) \neq e$; the fixed point is **extensional**, at the level of the functions computed. A transformation such as $f(e) = e + 1$ has no fixed point in the literal sense, but by the theorem there is an $e$ such that the programs $e$ and $e + 1$ compute the same function.

**The idea of the proof.** We look for a program $e$ that behaves like the program $f(e)$, for instance a program that computes $f(e)$ and then runs the program with that index. Such a program needs its own index, and it cannot contain it literally: the index is computed from the text of the program, and writing it into the text changes it. The proof replaces the literal index by a computation. For each $n$, the program $d(n)$ computes $\Phi_n(n)$ and runs the program with that index; its text contains $n$, not $\Phi_n(n)$. It remains to choose $n$ so that $\Phi_n(n) = f(d(n))$, and the diagonal choice $n = v$, for an index $v$ of $f \circ d$, does it. The program $d(v)$ then computes $f(d(v))$, the image of its own index, and runs it.

:::proof{of=thm-fixed-point}
By :ref{#cor-smn-parameters}, there is a total computable function $d$ such that for all $n$ and $x$,
$$
\Phi_{d(n)}(x) \simeq \Phi_{\Phi_n(n)}(x),
$$
where the right-hand side is undefined if $\Phi_n(n)\diverge$: the program $d(n)$, on input $x$, computes $\Phi_n(n)$, and if this halts with value $m$, runs $\Phi_m$ on $x$. The function $f \circ d$ is total computable; let $v$ be an index of it, so that $\Phi_v(n) = f(d(n))$ for every $n$, and $\Phi_v$ is total. Let $e = d(v)$. Then
$$
\Phi_e = \Phi_{d(v)} = \Phi_{\Phi_v(v)} = \Phi_{f(d(v))} = \Phi_{f(e)},
$$
where the second equality uses $\Phi_v(v)\converge$, which holds since $\Phi_v$ is total.
:::

The proof is a diagonal argument. Consider the table whose row $n$ is the function $\Phi_{\Phi_n(n)}$, the function computed by the program found on the diagonal. The transformation $f$ applied along the diagonal gives the row $v$; so the row $v$ is both $\Phi_{\Phi_v(v)}$, by definition of the table, and $\Phi_{f(d(v))}$, by the choice of $v$. Where Cantor's argument uses a transformation without fixed point to obtain a contradiction, here every transformation is shown to have a fixed point, as in the reading of the diagonal argument given by :ref{#cor-lawvere}. This reading of the proof as a "diagonal argument that fails" is due to Owings.

:::figure[Owings' matrix. The entry in row $n$ and column $x$ is the index $\Phi_n(x)$, standing for the function it computes (the entry is undefined if $\Phi_n(x)\diverge$). The shaded diagonal is the row of $d$: the program $d(n)$ computes the same function as the index $\Phi_n(n)$. Row $v$, with $\Phi_v = f \circ d$, is the diagonal transformed by $f$. Row $v$ meets the diagonal at column $v$, where $\Phi_v(v) = f(d(v))$: the functions computed by $d(v)$ and by $f(d(v))$ coincide.]
<svg class="fig" viewBox="0 0 560 250" width="560" role="img" aria-label="A matrix whose entry in row n and column x is the index Phi_n(x); the diagonal is the row of the function d; row v is the diagonal transformed by f; they meet at the entry (v, v)"><text x="265.0" y="12" text-anchor="middle" class="label">column x</text><text x="109.0" y="26" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="187.0" y="26" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="265.0" y="26" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="343.0" y="26" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="447.0" y="26" text-anchor="middle" class="math muted" font-size="13">v</text><text x="56" y="56" text-anchor="end" class="label">row <tspan class="mrm" font-size="14">0</tspan></text><rect x="70" y="34" width="78" height="34" class="cell head-cell"/><text x="109.0" y="56" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">(0)</tspan></text><rect x="148" y="34" width="78" height="34" class="cell"/><text x="187.0" y="56" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">(1)</tspan></text><rect x="226" y="34" width="78" height="34" class="cell"/><text x="265.0" y="56" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">(2)</tspan></text><rect x="304" y="34" width="78" height="34" class="cell"/><text x="343.0" y="56" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">(3)</tspan></text><rect x="408" y="34" width="78" height="34" class="cell"/><text x="447.0" y="56" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">(<tspan class="math">v</tspan>)</tspan></text><text x="394" y="56" text-anchor="middle" class="mrm muted" font-size="13">⋯</text><text x="56" y="90" text-anchor="end" class="label">row <tspan class="mrm" font-size="14">1</tspan></text><rect x="70" y="68" width="78" height="34" class="cell"/><text x="109.0" y="90" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3">(0)</tspan></text><rect x="148" y="68" width="78" height="34" class="cell head-cell"/><text x="187.0" y="90" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3">(1)</tspan></text><rect x="226" y="68" width="78" height="34" class="cell"/><text x="265.0" y="90" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3">(2)</tspan></text><rect x="304" y="68" width="78" height="34" class="cell"/><text x="343.0" y="90" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3">(3)</tspan></text><rect x="408" y="68" width="78" height="34" class="cell"/><text x="447.0" y="90" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3">(<tspan class="math">v</tspan>)</tspan></text><text x="394" y="90" text-anchor="middle" class="mrm muted" font-size="13">⋯</text><text x="56" y="124" text-anchor="end" class="label">row <tspan class="mrm" font-size="14">2</tspan></text><rect x="70" y="102" width="78" height="34" class="cell"/><text x="109.0" y="124" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">2</tspan><tspan dy="-3">(0)</tspan></text><rect x="148" y="102" width="78" height="34" class="cell"/><text x="187.0" y="124" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">2</tspan><tspan dy="-3">(1)</tspan></text><rect x="226" y="102" width="78" height="34" class="cell head-cell"/><text x="265.0" y="124" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">2</tspan><tspan dy="-3">(2)</tspan></text><rect x="304" y="102" width="78" height="34" class="cell"/><text x="343.0" y="124" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">2</tspan><tspan dy="-3">(3)</tspan></text><rect x="408" y="102" width="78" height="34" class="cell"/><text x="447.0" y="124" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">2</tspan><tspan dy="-3">(<tspan class="math">v</tspan>)</tspan></text><text x="394" y="124" text-anchor="middle" class="mrm muted" font-size="13">⋯</text><text x="56" y="158" text-anchor="end" class="label">row <tspan class="mrm" font-size="14">3</tspan></text><rect x="70" y="136" width="78" height="34" class="cell"/><text x="109.0" y="158" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">3</tspan><tspan dy="-3">(0)</tspan></text><rect x="148" y="136" width="78" height="34" class="cell"/><text x="187.0" y="158" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">3</tspan><tspan dy="-3">(1)</tspan></text><rect x="226" y="136" width="78" height="34" class="cell"/><text x="265.0" y="158" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">3</tspan><tspan dy="-3">(2)</tspan></text><rect x="304" y="136" width="78" height="34" class="cell head-cell"/><text x="343.0" y="158" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">3</tspan><tspan dy="-3">(3)</tspan></text><rect x="408" y="136" width="78" height="34" class="cell"/><text x="447.0" y="158" text-anchor="middle" class="mrm" font-size="13">Φ<tspan font-size="9" dy="3">3</tspan><tspan dy="-3">(<tspan class="math">v</tspan>)</tspan></text><text x="394" y="158" text-anchor="middle" class="mrm muted" font-size="13">⋯</text><text x="56" y="218" text-anchor="end" class="label">row <tspan class="math" font-size="14">v</tspan></text><rect x="70" y="196" width="78" height="34" class="cell"/><rect x="70" y="196" width="78" height="34" class="soft-fill" fill-opacity="0.5"/><text x="109.0" y="218" text-anchor="middle" class="mrm" font-size="13"><tspan class="math">f</tspan>(<tspan class="math">d</tspan>(0))</text><rect x="148" y="196" width="78" height="34" class="cell"/><rect x="148" y="196" width="78" height="34" class="soft-fill" fill-opacity="0.5"/><text x="187.0" y="218" text-anchor="middle" class="mrm" font-size="13"><tspan class="math">f</tspan>(<tspan class="math">d</tspan>(1))</text><rect x="226" y="196" width="78" height="34" class="cell"/><rect x="226" y="196" width="78" height="34" class="soft-fill" fill-opacity="0.5"/><text x="265.0" y="218" text-anchor="middle" class="mrm" font-size="13"><tspan class="math">f</tspan>(<tspan class="math">d</tspan>(2))</text><rect x="304" y="196" width="78" height="34" class="cell"/><rect x="304" y="196" width="78" height="34" class="soft-fill" fill-opacity="0.5"/><text x="343.0" y="218" text-anchor="middle" class="mrm" font-size="13"><tspan class="math">f</tspan>(<tspan class="math">d</tspan>(3))</text><rect x="408" y="196" width="78" height="34" class="cell head-cell"/><text x="447.0" y="218" text-anchor="middle" class="mrm" font-size="13"><tspan class="math">f</tspan>(<tspan class="math">d</tspan>(<tspan class="math">v</tspan>))</text><text x="394" y="218" text-anchor="middle" class="mrm muted" font-size="13">⋯</text><text x="109.0" y="188" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><text x="187.0" y="188" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><text x="265.0" y="188" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><text x="343.0" y="188" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><text x="447.0" y="188" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><rect x="405" y="193" width="84" height="40" class="track-outline"/></svg>
:::

:::quiz[the proof of the theorem]
Why is the function $d$ total, although $\Phi_n(n)$ may diverge?

- [x] Computing $d(n)$ only produces an index, by the SMN theorem; the computation of $\Phi_n(n)$ is performed by the program $d(n)$ when it runs, not when its index is computed.

  The divergence of $\Phi_n(n)$ is pushed inside the program whose index is returned.
- [ ] Because $f$ is total.

  $d$ does not involve $f$.
- [ ] Because $\Phi_n(n)$ converges for every $n$.

  It does not; otherwise the halting problem would be trivial.

---

Where does the proof use that $f$ is total?

- [x] To make $\Phi_v = f \circ d$ total, so that $\Phi_v(v)$ converges and $\Phi_{d(v)} = \Phi_{\Phi_v(v)}$ is the function of an actual index.

  If $f$ were partial, the same argument shows: if $f(e)\converge$, then $\Phi_{f(e)} = \Phi_e$, for $e = d(v)$.
- [ ] To show that $d$ is total.

  $d$ is obtained from the SMN theorem alone and does not involve $f$; it is total whatever $f$ is.
- [ ] To apply the SMN theorem.

  SMN applies to all partial computable functions.

---

Which index is the fixed point?

- [x] $d(v)$, where $v$ is an index of $f \circ d$.

  The program $d(v)$ computes $\Phi_v(v) = f(d(v))$ and then runs it: it runs its own transform.
- [ ] $v$.

  $\Phi_v = f \circ d$ is a total function with values indices, unrelated in general to $\Phi_{f(v)}$.
- [ ] $f(v)$.

  $f(v)$ is the image of $v$, which is in general unrelated to the function $\Phi_v = f \circ d$; the fixed point is $d(v)$.
:::

:::corollary{#cor-self-reference}
For every partial computable $g : \nat^2 \rightharpoonup \nat$, there is $e$ such that $\Phi_e(x) \simeq g(e, x)$ for every $x$.
:::

:::proof{of=cor-self-reference}
By :ref{#cor-smn-parameters}, there is a total computable $s$ with $\Phi_{s(n)}(x) \simeq g(n, x)$. By :ref{#thm-fixed-point}, there is $e$ with $\Phi_e = \Phi_{s(e)}$, that is, $\Phi_e(x) \simeq g(e, x)$.
:::

The corollary is the form in which the theorem is used. To build a program with a property, describe its behavior as an algorithm that may use **its own index $e$** as a known value; the corollary provides such an $e$. The description must be uniform in $e$, that is, define a partial computable function $g(e, x)$.

:::example{#ex-fixed-point-programs}
1. *A program that outputs its own index.* With $g(e, x) = e$, there is $e$ such that $\Phi_e(x) = e$ for every $x$. In a programming language, this is a **quine**, a program that prints its own text.
2. *A program halting only on its own index.* With $g(e, x) \simeq 0$ if $x = e$ and undefined otherwise, there is $e$ with $W_e = \{ e \}$.
3. *Two consecutive indices of the same function.* With $f(e) = e + 1$, there is $e$ with $\Phi_e = \Phi_{e+1}$.
:::

:::remark[Fixed points and paradoxes]{#rem-fixed-point-paradox}
The corollary allows self-referential definitions that look paradoxical, such as a program $e$ with $\Phi_e(x) \simeq \Phi_e(x) + 1$, obtained from $g(e, x) \simeq \Phi_e(x) + 1$. There is no contradiction: the equation forces $\Phi_e(x)\diverge$ for every $x$, and is then satisfied, both sides being undefined. Partial functions absorb self-reference, as in :ref{#prop-diagonal-partial}; the paradoxes of Russell or of the liar would arise only if every program had to produce a value.
:::

:::quiz[self-reference]
By :ref{#cor-self-reference}, there is $e$ with $\Phi_e(x) \simeq \Phi_e(x) + 1$ for all $x$. What follows?

- [x] $\Phi_e(x)\diverge$ for every $x$.

  If $\Phi_e(x)\converge = y$, then $y = y + 1$. The two sides can only agree by being both undefined.
- [ ] The corollary is contradictory.

  The relation $\simeq$ holds when both sides are undefined.
- [ ] $\Phi_e(x) = 0$ for every $x$.

  Then the right-hand side would be $1$.

---

Let $e$ be given by the corollary with $g(e, x) \simeq 0$ if $x \neq e$ and undefined if $x = e$. What is $W_e$?

- [x] $\nat \setminus \{ e \}$.

  The program $e$ halts on every input except its own index.
- [ ] $\{ e \}$.

  This is the opposite case, in the example above.
- [ ] It depends on whether $e \in \emptyset'$.

  $e \notin W_e$ by construction, so in fact $e \notin \emptyset'$.
:::

## Fixed points with parameters

The fixed point can be found uniformly in a parameter.

:::theorem[Fixed point theorem with parameters]{#thm-fixed-point-parameters}
For every total computable $f : \nat^2 \to \nat$, there is a total computable $n : \nat \to \nat$ such that $\Phi_{n(y)} = \Phi_{f(y, n(y))}$ for every $y$.
:::

:::proof{of=thm-fixed-point-parameters}
Follow the proof of :ref{#thm-fixed-point}, uniformly in $y$. Let $d$ be as in that proof. By :ref{#cor-smn-parameters} applied to $(y, m) \mapsto f(y, d(m))$, there is a total computable $v$ with $\Phi_{v(y)}(m) = f(y, d(m))$ for all $y$ and $m$. Let $n(y) = d(v(y))$. Since $\Phi_{v(y)}$ is total,
$$
\Phi_{n(y)} = \Phi_{d(v(y))} = \Phi_{\Phi_{v(y)}(v(y))} = \Phi_{f(y, d(v(y)))} = \Phi_{f(y, n(y))}.
$$
:::

:::proposition{#prop-infinitely-many-fixed-points}
Every total computable $f$ has infinitely many fixed points: for every $k$, there is $e \geq k$ with $\Phi_{f(e)} = \Phi_e$.
:::

:::proof{of=prop-infinitely-many-fixed-points}
The finitely many functions $\Phi_0, \dots, \Phi_{k-1}$ are not all the partial computable functions, since the constant functions are infinitely many and pairwise distinct, so there is an index $c$ with $\Phi_c \neq \Phi_i$ for every $i < k$. Let $g(x) = c$ for $x < k$ and $g(x) = f(x)$ for $x \geq k$; $g$ is total computable, the finite case distinction being computable. Let $e$ be a fixed point of $g$. If $e < k$, then $\Phi_e = \Phi_{g(e)} = \Phi_c$, contradicting the choice of $c$. So $e \geq k$, and $\Phi_e = \Phi_{g(e)} = \Phi_{f(e)}$.
:::

The proof uses the index $c$ as a fixed number; it need not be found by an algorithm, since only the computability of $g$ matters, and $g$ is computable for every value of the constant $c$.

:::quiz[infinitely many fixed points]
In the proof of :ref{#prop-infinitely-many-fixed-points}, why can $g$ not have a fixed point $e < k$?

- [x] Because then $\Phi_e = \Phi_c$, while $c$ was chosen so that $\Phi_c$ differs from $\Phi_0, \dots, \Phi_{k-1}$.
- [ ] Because $g(e) = c \neq e$.

  The fixed point theorem gives $\Phi_{g(e)} = \Phi_e$, not $g(e) = e$; the inequality $c \neq e$ alone is not a contradiction.
- [ ] Because $f$ has no fixed point below $k$.

  $f$ may well have fixed points below $k$; the proof finds one above $k$.
:::

## Applications

The fixed point theorem gives short proofs of results that otherwise require explicit diagonal constructions. Here is the undecidability of the halting problem again, and a result on the indices of a fixed function.

:::proposition{#prop-halting-via-fixed-point}
1. The halting set $\emptyset'$ is not computable.
2. For every $a$, the set $\{ e : \Phi_e = \Phi_a \}$ is not computable.
:::

:::proof{of=prop-halting-via-fixed-point}
1. Suppose $\emptyset'$ is computable. By :ref{#cor-self-reference}, there is $e$ such that $\Phi_e(x) \simeq 0$ if $e \notin \emptyset'$, and $\Phi_e(x)$ is undefined if $e \in \emptyset'$; the definition is uniform in $e$, since membership in $\emptyset'$ is decided by an algorithm. If $e \in \emptyset'$, then $\Phi_e(e)\diverge$, so $e \notin \emptyset'$; if $e \notin \emptyset'$, then $\Phi_e(e) = 0$, so $e \in \emptyset'$. Both cases are contradictory.
2. Let $P = \{ e : \Phi_e = \Phi_a \}$, suppose it computable, and fix $b$ with $\Phi_b \neq \Phi_a$, for instance an index of a function differing from $\Phi_a$ at $0$. Let $f(x) = b$ if $x \in P$ and $f(x) = a$ otherwise, a total computable function. For a fixed point $e$ of $f$: if $e \in P$ then $\Phi_e = \Phi_{f(e)} = \Phi_b \neq \Phi_a$, so $e \notin P$; if $e \notin P$ then $\Phi_e = \Phi_a$, so $e \in P$.
:::

The second argument works for every set of indices that is closed under equality of the functions computed and is neither empty nor everything. This is Rice's theorem, the subject of the next lesson.

## Exercises

::::exercise{difficulty=1}
Show that there is $e$ such that $\Phi_e(x) = e + x$ for all $x$, and $e$ such that $W_e = \{ 0, 1, \dots, e \}$.

:::solution
Apply :ref{#cor-self-reference} to $g(e, x) = e + x$, and to $g(e, x) \simeq 0$ if $x \leq e$, undefined otherwise. Both are partial computable functions of $(e, x)$.
:::
::::

::::exercise{difficulty=2}
Show that there is no total computable $f$ such that, for every $e$, the sets $W_{f(e)}$ and $W_e$ differ by exactly one element. Show also that the conclusion of the fixed point theorem cannot be strengthened to $f(e) = e$.

:::solution
A fixed point $e$ of $f$ satisfies $\Phi_{f(e)} = \Phi_e$, hence $W_{f(e)} = W_e$, which contradicts the hypothesis. For the second statement, $f(e) = e + 1$ is total computable, and $f(e) \neq e$ for every $e$: the fixed point given by the theorem is extensional only.
:::
::::

::::exercise{difficulty=3}
An index $e$ is **minimal** if $\Phi_i \neq \Phi_e$ for every $i < e$. Show that the set of minimal indices contains no infinite c.e. subset.

:::hint
Given an infinite c.e. set $A$ of minimal indices, consider the function sending $e$ to an element of $A$ greater than $e$, and apply the fixed point theorem.
:::

:::solution
Let $A$ be an infinite c.e. set of minimal indices, and $h$ a total computable function with range $A$. Let $f(e) = h(\mu m\ [h(m) > e])$, a total computable function, since $A$ is infinite; its values lie in $A$ and $f(e) > e$. Let $e$ be a fixed point of $f$. Then $e < f(e)$ and $\Phi_e = \Phi_{f(e)}$, so $f(e)$ is not minimal, although it belongs to $A$.
:::
::::

## Notes and references

The fixed point theorem was proved by Kleene in 1938, in a paper on notations for ordinals, where it is used to define functions by effective transfinite recursion; Kleene's form is :ref{#cor-self-reference}. The formulation for transformations of indices is the one of Rogers' book. Owings explained the proof as a diagonal argument that fails, as in the figure above. The result on minimal indices goes back to Blum (1967), in a paper on the size of programs. Soare's textbook treats the theorem in Section 2.2: the proof (Theorem 2.2.1), Owings' matrix (Section 2.2.4), the version with parameters (Theorem 2.2.6) and minimal indices (Exercise 2.2.9). Moschovakis surveys the many uses of the theorem, and Terwijn the many fixed point theorems of computability theory and of the theory of numberings that extend it.

- S. C. Kleene, *On notation for ordinal numbers*, Journal of Symbolic Logic 3 (1938), 150–155.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- J. C. Owings, Jr., *Diagonalization and the recursion theorem*, Notre Dame Journal of Formal Logic 14 (1973), 95–99.
- M. Blum, *On the size of machines*, Information and Control 11 (1967), 257–265.
- Y. N. Moschovakis, *Kleene's amazing second recursion theorem*, Bulletin of Symbolic Logic 16 (2010), 189–239.
- S. A. Terwijn, *Fixed point theorems in computability theory*, preprint, arXiv:2402.03069, 2024.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 2.2.
- B. Monin and L. Patey, *Computability theory*, chapter *Foundations of computability*, section *Kleene's fixed point theorem*.
