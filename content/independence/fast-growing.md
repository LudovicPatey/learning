---
title: A fast-growing hierarchy and semiregular cuts
summary: The hierarchy of functions F_k, defined by iteration; its formalization in IΣ₁, which proves the totality of each F_k; between a and a value F_ν(a) with ν non-standard, a countable model of IΣ₁ contains a semiregular cut (Kirby and Paris); hence IΣ₁ does not prove that every F_k is total.
duration: 45
prerequisites: [cuts-and-extensions/semiregular-cuts, truth-and-provability/provably-total]
---

The course on truth and provability proved that $\mathrm I\Sigma_1$ proves the totality of every primitive recursive function, and stated the converse (:ref{#thm-pmt}). This course proves such unprovability results by the method of Paris and Kirby: to show that a theory $T$ does not prove that a function $f$ is total, one finds, inside a model of $T$, a cut that is again a model of $T$ and is not closed under $f$. The cut is caught in an interval $[a, b]$ that is large in a combinatorial sense.

This lesson treats the first case. We define fast-growing functions $F_k$ and show that if $b = F_\nu(a)$ for a non-standard index $\nu$, there is a semiregular cut between $a$ and $b$; such a cut satisfies $\Sigma_1$ induction (:ref{#thm-semireg-isigma1}). The track assumes first-order logic; compactness provides the countable non-standard models used throughout.

## The hierarchy

:::definition{#def-fgh}
The functions $F_k : \nat \to \nat$, for $k \in \nat$, are defined by
$$
F_0(x) = x + 1, \qquad F_{k+1}(x) = F_k^{(x)}(x + 1),
$$
where $g^{(i)}$ is the $i$-th iterate of $g$: $g^{(0)}(y) = y$ and $g^{(i+1)}(y) = g(g^{(i)}(y))$.
:::

Each step iterates the previous function a number of times equal to the argument. This is the hierarchy of Hájek and Pudlák (a finite part of the Schwichtenberg–Wainer hierarchy, II.3.22); Wong's Lecture 5 uses the variant $F_{k+1}(x) = F_k^{(x+1)}(x)$, which grows at the same rate. Our choice is dictated by lesson 6, where $F_k(x)$ turns out to be exactly the least $y$ such that $[x, y)$ is $\omega^k$-large.

:::example{#ex-fgh-values}
1. $F_1(x) = F_0^{(x)}(x + 1) = 2x + 1$.
2. By induction on $i$, $F_1^{(i)}(y) = 2^i (y + 1) - 1$; hence $F_2(x) = F_1^{(x)}(x + 1) = 2^x (x + 2) - 1$. For instance $F_2(1) = 5$, $F_2(2) = 15$, $F_2(3) = 39$.
3. $F_3(1) = F_2(2) = 15$, and $F_3(2) = F_2(F_2(3)) = F_2(39) = 2^{39} \cdot 41 - 1$. The function $F_3$ grows like a tower of exponentials of height $x$.
4. $F_k(0) = F_{k-1}^{(0)}(1) = 1$ for every $k \geq 1$. The hierarchy does not separate its members at $0$.
:::

Each $F_k$ is primitive recursive: $F_{k+1}(x) = G(x, x + 1)$, where $G(0, y) = y$ and $G(i + 1, y) = F_k(G(i, y))$ is a primitive recursion.

## Formalization in IΣ₁

Inside a model, $F_k(x)$ must be defined for non-standard $k$ as well. As for the Ackermann function, we use finite computations, as in the last exercise of :ref{to="truth-and-provability/provably-total"}.

:::fact{#fact-fgh-formal}
There is a $\Sigma_1$ formula $\mathrm{It}(k, i, x, y)$, read "$F_k^{(i)}(x) = y$", such that $\mathrm I\Sigma_1$ proves:

1. (**functionality**) $\mathrm{It}(k, i, x, y) \wedge \mathrm{It}(k, i, x, y') \rightarrow y = y'$;
2. (**iteration**) $\mathrm{It}(k, 0, x, y) \leftrightarrow y = x$, and $\mathrm{It}(k, i + 1, x, z) \leftrightarrow \exists y\ \big(\mathrm{It}(k, i, x, y) \wedge \mathrm{It}(k, 1, y, z)\big)$;
3. (**the hierarchy**) $\mathrm{It}(0, 1, x, y) \leftrightarrow y = x + 1$, and $\mathrm{It}(k + 1, 1, x, y) \leftrightarrow \mathrm{It}(k, x, x + 1, y)$.

In $\nat$, $\mathrm{It}(k, i, x, y)$ holds if and only if $F_k^{(i)}(x) = y$.
:::

The formula says that some **computation** contains $\langle k, i, x, y \rangle$: a coded finite set of quadruples each justified by the clauses 2–3 from other elements. Justification is bounded, so the formula is $\Sigma_1$; the proofs are those of the Ackermann exercise. We write $F_k(x) = y$ for $\mathrm{It}(k, 1, x, y)$, and $F_k(x){\downarrow}$ for $\exists y\ F_k(x) = y$.

:::lemma{#lem-fgh-isigma1}
$\mathrm I\Sigma_1$ proves:

1. if $F_k(y) = z$, then $z > y$; if $\mathrm{It}(k, i, x, y)$, then $y \geq x + i$;
2. if $\mathrm{It}(k, i, x, y)$, then there is a coded sequence $t$ of length $i + 1$ with $\mathrm{It}(k, j, x, (t)_j)$ for every $j \leq i$, and this sequence is strictly increasing.

Moreover, for every standard $k$, $\mathrm I\Sigma_1 \vdash \forall x\ F_k(x){\downarrow}$.
:::

:::proof{of=lem-fgh-isigma1}
1. Let $P(k) \equiv \forall y\ \forall z\ \big(F_k(y) = z \rightarrow z > y\big)$, a $\Pi_1$ formula. We prove $\forall k\ P(k)$ by $\Pi_1$ induction, available in $\mathrm I\Sigma_1$ by :ref{#thm-fo-isigma-ipi}. $P(0)$ holds by item 3 of :ref{#fact-fgh-formal}. Assume $P(k)$. By $\Pi_1$ induction on $i$, $\forall x\ \forall w\ (\mathrm{It}(k, i, x, w) \rightarrow w \geq x + i)$: the case $i = 0$ is item 2, and if $\mathrm{It}(k, i + 1, x, w)$, item 2 gives $v$ with $\mathrm{It}(k, i, x, v)$ and $F_k(v) = w$, so $w > v \geq x + i$ by $P(k)$. Now if $F_{k+1}(y) = z$, then $\mathrm{It}(k, y, y + 1, z)$, so $z \geq 2y + 1 > y$. This is $P(k + 1)$, and also proves the second claim.

2. Fix $k, i, x, y$ with $\mathrm{It}(k, i, x, y)$. First, every rank $j \leq i$ has an iterate: apply $\Sigma_1$ induction to $\rho(m) \equiv m \leq i \rightarrow \exists w\ \mathrm{It}(k, i - m, x, w)$. $\rho(0)$ is the hypothesis, and if $w$ witnesses $\rho(m)$ with $m + 1 \leq i$, the implication from left to right in item 2 of :ref{#fact-fgh-formal}, applied to the rank $i - m = (i - m - 1) + 1$, gives an iterate of rank $i - m - 1$. Then apply $\Sigma_1$ induction to
$$
\chi(j) \equiv j \leq i \rightarrow \exists t\ \big(\mathrm{Seq}(t, j + 1) \wedge \forall j' \leq j\ \mathrm{It}(k, j', x, (t)_{j'})\big),
$$
which is $\Sigma_1$ in $\mathrm I\Sigma_1$ by Parsons' lemma (:ref{#lem-fo-collection-closure}). For $j = 0$ take the sequence of length $1$ with entry $x$. For the step, the iterate of rank $j + 1 \leq i$ exists, and concatenation (:ref{#prop-seq-basic}) extends $t$. The sequence is strictly increasing by item 1, since consecutive entries satisfy $F_k((t)_j) = (t)_{j+1}$, by item 2 of :ref{#fact-fgh-formal} and functionality.

*Totality.* By induction on $k$ in the metatheory. $F_0$ is total by item 3. If $\mathrm I\Sigma_1 \vdash \forall y\ F_k(y){\downarrow}$, then $\Sigma_1$ induction on $i$, with item 2, gives $\forall i\ \forall x\ \exists y\ \mathrm{It}(k, i, x, y)$, and item 3 gives $\forall x\ F_{k+1}(x){\downarrow}$.
:::

The induction in the totality proof is in the metatheory, one proof for each $k$. A uniform proof would be an induction on $k$ for the $\Pi_2$ formula $\forall x\ F_k(x){\downarrow}$: $\mathrm I\Sigma_2$ can carry it out (exercise), and the next lesson shows that $\mathrm I\Sigma_1$ cannot.

:::quiz[the formalization of the hierarchy]
In the proof of :ref{#lem-fgh-isigma1}, item 1, why is the induction carried out on the formula $P(k)$, which says that every *existing* value $F_k(y)$ is above $y$, rather than on the statement that $F_k$ is total and increasing?

- [x] $P(k)$ is $\Pi_1$, so $\mathrm I\Sigma_1$ can induct on it; the statement "$F_k$ is total" is $\Pi_2$, and $\Pi_2$ induction is not available in $\mathrm I\Sigma_1$.
- [ ] Because $F_k$ is not total in models of $\mathrm I\Sigma_1$ for standard $k$.

  For standard $k$ it is total, by the last part of the lemma; the issue is the uniformity in $k$.
- [ ] Because $\Pi_1$ formulas are preserved in cuts.

  This is true but irrelevant here: the induction takes place in a single model.
:::

## Catching a semiregular cut

Let $M$ be a countable model of $\mathrm I\Sigma_1$, $a \geq 1$ in $M$, and $\nu$ non-standard with $s = F_\nu(a)$ defined. Since $s = F_{\nu-1}^{(a)}(a + 1)$, the iterates of $F_{\nu - 1}$ divide $[a + 1, s]$ into $a$ consecutive pieces, each of the form $[t, F_{\nu-1}(t)]$: the same shape as the whole, with the index lowered by one. A coded function with domain smaller than $a$ misses some piece, by the pigeonhole principle, and we continue inside it. Since $\nu - k$ is non-standard for every standard $k$, the process never stops, and since $M$ is countable, each coded function is handled at some stage.

:::figure[The construction of :ref{#thm-kirby-paris-cut}. At stage $k$, the interval $[r_k, s_k]$ is divided into $r_k$ pieces by the iterates of $F_{\nu - k - 1}$; the values of the coded function $f_k$ (squares) meet fewer than $r_k$ pieces, and a piece that contains none becomes $[r_{k+1}, s_{k+1}]$. The cut $I$ is the supremum of the left endpoints.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Three stages of the construction: the interval from r_k to s_k is divided into r_k pieces by the iterates of F_{nu-1}; the values of the coded function f_k are marked; a piece containing no value becomes the next interval"><line x1="40.0" y1="40.0" x2="560.0" y2="40.0" class="ink-stroke" stroke-width="1.4"/><line x1="40.0" y1="33.0" x2="40.0" y2="47.0" class="ink-stroke" stroke-width="1.4"/><line x1="560.0" y1="33.0" x2="560.0" y2="47.0" class="ink-stroke" stroke-width="1.4"/><text x="40.0" y="64.0" text-anchor="middle" class="math" font-size="14">r<tspan class="mrm" font-size="10" dy="3">k</tspan></text><text x="560.0" y="64.0" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm" font-size="10" dy="3">k</tspan></text><line x1="160.0" y1="120.0" x2="420.0" y2="120.0" class="ink-stroke" stroke-width="1.4"/><line x1="160.0" y1="113.0" x2="160.0" y2="127.0" class="ink-stroke" stroke-width="1.4"/><line x1="420.0" y1="113.0" x2="420.0" y2="127.0" class="ink-stroke" stroke-width="1.4"/><text x="160.0" y="144.0" text-anchor="middle" class="math" font-size="14">r<tspan class="mrm" font-size="10" dy="3">k+1</tspan></text><text x="420.0" y="144.0" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm" font-size="10" dy="3">k+1</tspan></text><line x1="230.0" y1="200.0" x2="330.0" y2="200.0" class="ink-stroke" stroke-width="1.4"/><line x1="230.0" y1="193.0" x2="230.0" y2="207.0" class="ink-stroke" stroke-width="1.4"/><line x1="330.0" y1="193.0" x2="330.0" y2="207.0" class="ink-stroke" stroke-width="1.4"/><text x="230.0" y="224.0" text-anchor="middle" class="math" font-size="14">r<tspan class="mrm" font-size="10" dy="3">k+2</tspan></text><text x="330.0" y="224.0" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm" font-size="10" dy="3">k+2</tspan></text><line x1="70.0" y1="34.0" x2="70.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="110.0" y1="34.0" x2="110.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="160.0" y1="34.0" x2="160.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="230.0" y1="34.0" x2="230.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="330.0" y1="34.0" x2="330.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="420.0" y1="34.0" x2="420.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><rect x="51.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="91.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="286.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="476.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="516.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="160" y="30" width="260" height="20" class="accent-fill" fill-opacity="0.18"/><line x1="160.0" y1="52.0" x2="160.0" y2="112.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="420.0" y1="52.0" x2="420.0" y2="112.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="185.0" y1="114.0" x2="185.0" y2="126.0" class="muted-stroke" stroke-width="1.2"/><line x1="230.0" y1="114.0" x2="230.0" y2="126.0" class="muted-stroke" stroke-width="1.2"/><line x1="330.0" y1="114.0" x2="330.0" y2="126.0" class="muted-stroke" stroke-width="1.2"/><rect x="171.5" y="116.5" width="7" height="7" class="muted-fill"/><rect x="366.5" y="116.5" width="7" height="7" class="muted-fill"/><rect x="396.5" y="116.5" width="7" height="7" class="muted-fill"/><rect x="230" y="110" width="100" height="20" class="accent-fill" fill-opacity="0.18"/><line x1="230.0" y1="132.0" x2="230.0" y2="192.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="330.0" y1="132.0" x2="330.0" y2="192.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><text x="580.0" y="20.0" text-anchor="end" class="label">squares: values of the coded function</text><text x="470.0" y="205.0" text-anchor="start" class="label">I = sup of the r_k</text></svg>
:::

:::theorem[Kirby, Paris]{#thm-kirby-paris-cut}
Let $M$ be a countable model of $\mathrm I\Sigma_1$, $a \geq 1$ in $M$, and $\nu \in M$ non-standard such that $F_\nu(a){\downarrow}$ in $M$. Then there is a semiregular cut $I$ of $M$ with $a \in I$ and $F_\nu(a) \notin I$. In particular $I \models \mathrm I\Sigma_1$.
:::

:::proof{of=thm-kirby-paris-cut}
Let $(f_k)_{k \in \nat}$ be an enumeration of the coded functions of $M$ (:ref{#def-semiregular}) in which each of them appears infinitely often; it exists since $M$ is countable. We build by recursion on $k \in \nat$ elements $r_k, s_k$ of $M$ such that
$$
r_0 = a, \qquad s_k = F_{\nu - k}(r_k), \qquad r_k < r_{k+1}, \qquad s_{k+1} \leq s_k .
$$
The index $\nu - k$ is non-standard, so it is at least $1$, and $r_k \geq a \geq 1$, so that there is at least one piece below. (For $a = 0$ the theorem fails: $F_\nu(0) = 1$.) For $k = 0$, $s_0 = F_\nu(a)$ exists by hypothesis.

*Stage $k$.* Write $r = r_k$ and $\mu = \nu - k - 1$. By item 3 of :ref{#fact-fgh-formal}, $\mathrm{It}(\mu, r, r + 1, s_k)$, so by :ref{#lem-fgh-isigma1} there is a strictly increasing coded sequence $t$ of length $r + 1$ with $(t)_0 = r + 1$, $(t)_{j+1} = F_\mu((t)_j)$ and $(t)_r = s_k$. The pieces $J_i = [(t)_i, (t)_{i+1})$, for $i < r$, are pairwise disjoint subintervals of $[r + 1, s_k)$. Let $d_k$ be the length of the domain of $f_k$. If $d_k \geq r$, let $i = 0$. Otherwise, some piece $J_i$ contains no value $f_k(x)$, $x < d_k$: if each piece contained one, the sequence $g$ of length $r$ given by $g(i) =$ the least $x < d_k$ with $f_k(x) \in J_i$ would be coded, by :ref{#prop-seq-basic} (its graph is defined by a bounded formula with the parameters $t$ and $f_k$), with values below $d_k \leq r - 1$; by the finite pigeonhole principle (exercise of :ref{to="fragments-of-arithmetic/coding"}), $g(i) = g(j)$ for some $i < j$, and $f_k(g(i))$ would lie in $J_i \cap J_j = \emptyset$. Choose such an $i$, and let
$$
r_{k+1} = (t)_i, \qquad s_{k+1} = (t)_{i+1} = F_\mu(r_{k+1}) = F_{\nu - (k+1)}(r_{k+1}).
$$
Then $r_{k+1} \geq r + 1 > r_k$ and $s_{k+1} \leq (t)_r = s_k$, and in the case $d_k < r_k$, no value of $f_k$ lies in $[r_{k+1}, s_{k+1})$.

*The cut.* Let $I = \{ x \in M : x < r_k \text{ for some } k \in \nat \}$. It is an initial segment, closed under successor because the sequence $(r_k)$ is strictly increasing, and $a = r_0 < r_1$ is in $I$. For all $j, k$, $r_k < s_j$: if $k \geq j$, then $r_k < s_k \leq s_j$; if $k < j$, then $r_k < r_j < s_j$. So no $s_j$ is in $I$; in particular $F_\nu(a) = s_0 \notin I$, and $I$ is a proper cut.

*Semiregularity.* Let $f$ be a coded function with domain $d \in I$. Then $d < r_j$ for some $j$, and $f = f_k$ for some $k \geq j$, so $d < r_k$. Let $v = f(x)$ be a value in $I$. Since $s_{k+1} \notin I$, $v < s_{k+1}$; by the choice of the piece, $v \notin [r_{k+1}, s_{k+1})$; so $v < r_{k+1}$. The element $r_{k+1} \in I$ bounds the values of $f$ in $I$. By :ref{#thm-semireg-isigma1}, $I \models \mathrm I\Sigma_1$.
:::

The proof is a **construction by finite extensions**, as in computability theory: each stage meets one requirement (the values of $f_k$ in $I$ are bounded), and the requirements are listed with repetitions. The recursion on $k$ is external to $M$; only each stage is carried out inside $M$.

:::quiz[catching a semiregular cut]
In the proof of :ref{#thm-kirby-paris-cut}, why does each function appear infinitely often in the enumeration?

- [x] A function $f_k$ is only handled when its domain is smaller than $r_k$. A function with domain $d \in I$ satisfies $d < r_k$ only from some stage on, so it must appear again at a later stage.
- [ ] To ensure that the sequence $(r_k)$ is unbounded in $M$.

  The sequence $(r_k)$ is bounded in $M$ by $s_0$; it is only unbounded in $I$, by definition of $I$.
- [ ] Because the enumeration of a countable set cannot be injective.

  An injective enumeration exists; the repetitions serve the condition on domains.

---

Where is it used that $\nu$ is non-standard?

- [x] At every standard stage $k$ the index $\nu - k$ must be at least $1$, so that $F_{\nu - k}(r_k)$ can be split into iterates of $F_{\nu - k - 1}$. If $\nu$ were standard, the construction would stop after $\nu$ stages.
- [ ] To make $F_\nu(a)$ non-standard.

  This is a consequence, but the construction uses the index itself at each stage.
- [ ] To apply the pigeonhole principle.

  The pigeonhole principle holds in $M$ for all elements.
:::

## Exercises

::::exercise{difficulty=2}
Show that $\mathrm I\Sigma_2$ proves $\forall k\ \forall x\ F_k(x){\downarrow}$.

:::solution
Apply $\Pi_2$ induction, available in $\mathrm I\Sigma_2$ by :ref{#thm-fo-isigma-ipi}, to $\tau(k) \equiv \forall x\ F_k(x){\downarrow}$. $\tau(0)$ holds by item 3 of :ref{#fact-fgh-formal}. Assume $\tau(k)$. By $\Sigma_1$ induction on $i$, with the parameter $k$ and the hypothesis $\tau(k)$, $\forall x\ \exists y\ \mathrm{It}(k, i, x, y)$ for every $i$: the step uses item 2. With $i = x$ and the point $x + 1$, item 3 gives $F_{k+1}(x){\downarrow}$. So $\tau(k + 1)$.
:::
::::

## Notes and references

The hierarchy is the finite part of the hierarchy of Hájek and Pudlák (Chapter II, 3.22), a variant of the hierarchy of Schwichtenberg and Wainer; Wong's Lecture 5 uses the closely related functions $F_{k+1}(x) = F_k^{(x+1)}(x)$, after Grzegorczyk (1953). :ref{#thm-kirby-paris-cut} and its consequence, the unprovability of the totality of all $F_k$ in $\mathrm I\Sigma_1$ (next lesson), are due to Kirby and Paris (1977); the proof follows Wong's proof of his Theorem 5.6, with the index lowered at each stage instead of a new overspill, which avoids the monotonicity of the hierarchy in its index inside the model. Hájek and Pudlák obtain the same results with the indicators of Chapter IV, Section 3.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- A. Grzegorczyk, *Some classes of recursive functions*, Rozprawy Matematyczne 4 (1953), 1–46.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter II, Section 3(d), and Chapter IV, Section 3.
