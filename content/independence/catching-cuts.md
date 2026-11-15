---
title: Catching a semiregular cut
summary: Between a and F_ν(a), for ν non-standard, a countable model of IΣ₁ contains a semiregular cut, hence a cut satisfying IΣ₁ (Kirby and Paris); the proof is a construction by finite extensions along a decreasing index.
duration: 30
prerequisites: [fast-growing, cuts-and-extensions/semiregular-cuts]
---

The previous lesson defined the functions $F_k$ and showed that $\mathrm I\Sigma_1$ proves the totality of each of them. This lesson proves the combinatorial core of the method of Paris and Kirby: if $b = F_\nu(a)$ for a non-standard index $\nu$, a countable model of $\mathrm I\Sigma_1$ contains a semiregular cut between $a$ and $b$. Such a cut satisfies $\Sigma_1$ induction (:ref{#thm-semireg-isigma1}). The next lesson turns this into the unprovability in $\mathrm I\Sigma_1$ of the totality of all the $F_k$, and into a bound on the functions provably total in $\mathrm I\Sigma_1$.

## The idea

Let $M$ be a countable model of $\mathrm I\Sigma_1$, $a \geq 1$ in $M$, and $\nu$ non-standard with $s = F_\nu(a)$ defined. Since $s = F_{\nu-1}^{(a)}(a + 1)$, the iterates of $F_{\nu - 1}$ divide $[a + 1, s]$ into $a$ consecutive pieces, each of the form $[t, F_{\nu-1}(t)]$: the same shape as the whole, with the index lowered by one. A coded function with domain smaller than $a$ misses some piece, by the pigeonhole principle, and we continue inside it. Since $\nu - k$ is non-standard for every standard $k$, the process never stops, and since $M$ is countable, each coded function is handled at some stage.

## The construction

:::figure[The construction of :ref{#thm-kirby-paris-cut}. At stage $k$, the iterates of $F_{\nu - k - 1}$ divide $[r_k + 1, s_k)$ into $r_k$ pieces of increasing length; the values of the coded function $f_k$ (squares) meet fewer than $r_k$ pieces, and a piece that contains none, magnified in the next row, becomes $[r_{k+1}, s_{k+1}]$. The cut $I$ is the supremum of the left endpoints $r_k$.]
<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="Three stages of the construction: the interval from r_k to s_k is divided into pieces of increasing length by the iterates of F_{nu-k-1}; the values of the coded function f_k are marked; a piece containing no value is magnified in the next row and becomes the next interval"><rect x="310" y="30" width="100" height="20" class="accent-fill" fill-opacity="0.18"/><line x1="310.0" y1="52.0" x2="100.0" y2="118.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="410.0" y1="52.0" x2="500.0" y2="118.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="40.0" y1="40.0" x2="560.0" y2="40.0" class="ink-stroke" stroke-width="1.4"/><line x1="40.0" y1="33.0" x2="40.0" y2="47.0" class="ink-stroke" stroke-width="1.4"/><line x1="560.0" y1="33.0" x2="560.0" y2="47.0" class="ink-stroke" stroke-width="1.4"/><text x="40.0" y="64.0" text-anchor="middle" class="math" font-size="14">r<tspan class="mrm" font-size="10" dy="3">k</tspan></text><text x="560.0" y="64.0" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm" font-size="10" dy="3">k</tspan></text><line x1="62.0" y1="34.0" x2="62.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="90.0" y1="34.0" x2="90.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="126.0" y1="34.0" x2="126.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="172.0" y1="34.0" x2="172.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="232.0" y1="34.0" x2="232.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="310.0" y1="34.0" x2="310.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><line x1="410.0" y1="34.0" x2="410.0" y2="46.0" class="muted-stroke" stroke-width="1.2"/><rect x="46.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="72.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="146.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="266.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="446.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="516.5" y="36.5" width="7" height="7" class="muted-fill"/><rect x="240" y="120" width="60" height="20" class="accent-fill" fill-opacity="0.18"/><line x1="240.0" y1="142.0" x2="180.0" y2="208.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="300.0" y1="142.0" x2="420.0" y2="208.0" class="accent-stroke" stroke-width="1.0" stroke-dasharray="3 3"/><line x1="100.0" y1="130.0" x2="500.0" y2="130.0" class="ink-stroke" stroke-width="1.4"/><line x1="100.0" y1="123.0" x2="100.0" y2="137.0" class="ink-stroke" stroke-width="1.4"/><line x1="500.0" y1="123.0" x2="500.0" y2="137.0" class="ink-stroke" stroke-width="1.4"/><text x="100.0" y="154.0" text-anchor="middle" class="math" font-size="14">r<tspan class="mrm" font-size="10" dy="3">k+1</tspan></text><text x="500.0" y="154.0" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm" font-size="10" dy="3">k+1</tspan></text><line x1="116.0" y1="124.0" x2="116.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><line x1="136.0" y1="124.0" x2="136.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><line x1="162.0" y1="124.0" x2="162.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><line x1="196.0" y1="124.0" x2="196.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><line x1="240.0" y1="124.0" x2="240.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><line x1="300.0" y1="124.0" x2="300.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><line x1="380.0" y1="124.0" x2="380.0" y2="136.0" class="muted-stroke" stroke-width="1.2"/><rect x="104.5" y="126.5" width="7" height="7" class="muted-fill"/><rect x="146.5" y="126.5" width="7" height="7" class="muted-fill"/><rect x="216.5" y="126.5" width="7" height="7" class="muted-fill"/><rect x="336.5" y="126.5" width="7" height="7" class="muted-fill"/><rect x="436.5" y="126.5" width="7" height="7" class="muted-fill"/><line x1="180.0" y1="220.0" x2="420.0" y2="220.0" class="ink-stroke" stroke-width="1.4"/><line x1="180.0" y1="213.0" x2="180.0" y2="227.0" class="ink-stroke" stroke-width="1.4"/><line x1="420.0" y1="213.0" x2="420.0" y2="227.0" class="ink-stroke" stroke-width="1.4"/><text x="180.0" y="244.0" text-anchor="middle" class="math" font-size="14">r<tspan class="mrm" font-size="10" dy="3">k+2</tspan></text><text x="420.0" y="244.0" text-anchor="middle" class="math" font-size="14">s<tspan class="mrm" font-size="10" dy="3">k+2</tspan></text><text x="580.0" y="16.0" text-anchor="end" class="label">squares: values of the coded function</text><text x="580.0" y="250.0" text-anchor="end" class="label">I = sup of the r_k</text></svg>
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

*Stage $k$.* Write $r = r_k$ and $\mu = \nu - k - 1$. By item 3 of :ref{#fact-fgh-formal}, $\mathrm{It}(\mu, r, r + 1, s_k)$, so by :ref{#lem-fgh-isigma1} there is a strictly increasing coded sequence $t$ of length $r + 1$ with $(t)_0 = r + 1$, $(t)_{j+1} = F_\mu((t)_j)$ and $(t)_r = s_k$. The pieces $J_i = [(t)_i, (t)_{i+1})$, for $i < r$, are pairwise disjoint subintervals of $[r + 1, s_k)$. Let $d_k$ be the length of the domain of $f_k$. If $d_k \geq r$, let $i = 0$. Otherwise, some piece $J_i$ contains no value $f_k(x)$, $x < d_k$: if each piece contained one, the sequence $g$ of length $r$ given by $g(i) =$ the least $x < d_k$ with $f_k(x) \in J_i$ would be coded, by :ref{#prop-seq-basic} (its graph is defined by a bounded formula with the parameters $t$ and $f_k$), with values below $d_k \leq r - 1$; by the finite pigeonhole principle (:ref{#ex-finite-pigeonhole}), $g(i) = g(j)$ for some $i < j$, and $f_k(g(i))$ would lie in $J_i \cap J_j = \emptyset$. Choose such an $i$, and let
$$
r_{k+1} = (t)_i, \qquad s_{k+1} = (t)_{i+1} = F_\mu(r_{k+1}) = F_{\nu - (k+1)}(r_{k+1}).
$$
Then $r_{k+1} \geq r + 1 > r_k$ and $s_{k+1} \leq (t)_r = s_k$, and in the case $d_k < r_k$, no value of $f_k$ lies in $[r_{k+1}, s_{k+1})$.

*The cut.* Let $I = \{ x \in M : x < r_k \text{ for some } k \in \nat \}$. It is an initial segment, closed under successor because the sequence $(r_k)$ is strictly increasing, and $a = r_0 < r_1$ is in $I$. For all $j, k$, $r_k < s_j$: if $k \geq j$, then $r_k < s_k \leq s_j$; if $k < j$, then $r_k < r_j < s_j$. So no $s_j$ is in $I$; in particular $F_\nu(a) = s_0 \notin I$, and $I$ is a proper cut.

*Semiregularity.* Let $f$ be a coded function with domain $d \in I$. Then $d < r_j$ for some $j$, and $f = f_k$ for some $k \geq j$, so $d < r_k$. Let $v = f(x)$ be a value in $I$. Since $s_{k+1} \notin I$, $v < s_{k+1}$; by the choice of the piece, $v \notin [r_{k+1}, s_{k+1})$; so $v < r_{k+1}$. The element $r_{k+1} \in I$ bounds the values of $f$ in $I$. By :ref{#thm-semireg-isigma1}, $I \models \mathrm I\Sigma_1$.
:::

The proof is a **construction by finite extensions**, as in computability theory: each stage meets one requirement (the values of $f_k$ in $I$ are bounded), and the requirements are listed with repetitions. The recursion on $k$ is external to $M$; only each stage is carried out inside $M$.

The hypothesis that $\nu$ is non-standard cannot be dropped. If $\nu = k$ is standard and $I \models \mathrm I\Sigma_1$ is a cut containing $a$, then $I \models F_k(a) = z$ for some $z \in I$ (:ref{#lem-fgh-isigma1}); this computation is a computation in $M$ (:ref{#cor-sigma1-upward}), and by functionality $z = F_k(a)$, so $F_k(a) \in I$. No cut satisfying $\mathrm I\Sigma_1$ separates $a$ from $F_k(a)$.

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

::::exercise{#ex-two-semiregular-cuts difficulty=2 objective="Apply the theorem inside the pieces of the decomposition of $F_\nu(a)$ to find several semiregular cuts in the same interval."}
Let $M$ be a countable model of $\mathrm I\Sigma_1$, $a \geq 2$ in $M$, and $\nu \in M$ non-standard with $F_\nu(a){\downarrow}$. Show that there are two distinct semiregular cuts $I_0 \subsetneq I_1$ of $M$ that contain $a$ and not $F_\nu(a)$.

:::solution
By item 3 of :ref{#fact-fgh-formal} and :ref{#lem-fgh-isigma1}, there is a strictly increasing coded sequence $t$ of length $a + 1$ with $(t)_0 = a + 1$, $(t)_{j+1} = F_{\nu-1}((t)_j)$ for $j < a$, and $(t)_a = F_\nu(a)$, as in the proof of :ref{#thm-kirby-paris-cut}. The index $\nu - 1$ is non-standard, and $(t)_0, (t)_1 \geq 1$. Apply :ref{#thm-kirby-paris-cut} to $(t)_0$ and $\nu - 1$: there is a semiregular cut $I_0$ with $(t)_0 \in I_0$ and $(t)_1 = F_{\nu-1}((t)_0) \notin I_0$. Apply it to $(t)_1$ and $\nu - 1$: there is a semiregular cut $I_1$ with $(t)_1 \in I_1$ and $(t)_2 \notin I_1$. Both contain $a < (t)_0 < (t)_1$. Since $a \geq 2$, $(t)_2 \leq (t)_a = F_\nu(a)$, so $F_\nu(a) \notin I_1$, and $F_\nu(a) \notin I_0$ since $(t)_1 < F_\nu(a)$. Finally $(t)_1 \in I_1 \setminus I_0$; as cuts are linearly ordered by inclusion, $I_0 \subsetneq I_1$.
:::
::::

## Notes and references

:ref{#thm-kirby-paris-cut} is due to Kirby and Paris (1977). The proof follows Wong's proof of his Theorem 5.6, with two changes: the index is lowered at each stage instead of being obtained by a new overspill, which avoids the monotonicity of the hierarchy in its index inside the model (a statement whose proof would need $\Pi_2$ induction), and the pieces are chosen with left end above $r_k$, so that the left ends increase strictly. Hájek and Pudlák obtain the same cuts through the indicators of their Chapter IV, Section 3.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 3.

:::::exercises
::::exercise{#ex-catching-left-ends difficulty=1 objective="See why the pieces are chosen with left end above $r_k$, by dropping this condition."}
Consider a variant of the proof of :ref{#thm-kirby-paris-cut} in which the pieces at stage $k$ may start at $r_k$ itself, so that only $r_k \leq r_{k+1}$ is guaranteed. Show that if the sequence $(r_k)$ is eventually constant, the set $I = \{ x : x < r_k \text{ for some } k \}$ is not a cut. Which step of the actual proof excludes this?

:::solution
Suppose $r_k = r$ for all $k \geq k_0$. Since $(r_k)$ is non-decreasing, $r_k \leq r$ for every $k$, so $I = \{ x : x < r \}$. As $a \geq 1$ and $r \geq a$, $r - 1 \in I$ while $(r - 1) + 1 = r \notin I$: $I$ is not closed under successor. In the proof, the pieces lie in $[r_k + 1, s_k)$, since $(t)_0 = r_k + 1$; so $r_{k+1} = (t)_i \geq r_k + 1$, and the left ends increase strictly.
:::
::::

::::exercise{#ex-catching-countable-family difficulty=1 objective="Locate the use of countability in the construction, by running it for a countable family of coded functions in an arbitrary model."}
Let $M$ be a model of $\mathrm I\Sigma_1$ of any cardinality, $a \geq 1$ in $M$, $\nu \in M$ non-standard with $F_\nu(a){\downarrow}$, and $\mathcal C$ a countable set of coded functions of $M$. Show that there is a cut $I$ with $a \in I$ and $F_\nu(a) \notin I$ such that, for every $f \in \mathcal C$ whose domain is in $I$, the values of $f$ in $I$ are bounded in $I$.

:::solution
We may assume $\mathcal C$ nonempty, adding a function if needed. Let $(f_k)_{k \in \nat}$ enumerate $\mathcal C$ with each member repeated infinitely often, and run the construction of the proof of :ref{#thm-kirby-paris-cut} with this sequence. Each stage only uses that $f_k$ is a coded function of $M$, and the facts on the cut $I$ (initial segment, closed under successor, $a \in I$, no $s_j$ in $I$) do not depend on the enumeration. The argument of the paragraph on semiregularity applies to each $f \in \mathcal C$ with domain in $I$, since $f = f_k$ for infinitely many $k$. Countability of $M$ was used only to enumerate all coded functions.
:::
::::

::::exercise[The Kirby–Paris theorem without indicators]{#ex-catching-direct-kp difficulty=2 objective="Read the unprovability of the totality of the hierarchy directly off the cut, when the index lies in the cut." lessons="fast-growing"}
Let $M$ be a countable model of $\mathrm I\Sigma_1$, $a \geq 1$ in $M$, and $\nu \leq a$ non-standard with $F_\nu(a){\downarrow}$; let $I$ be the cut given by :ref{#thm-kirby-paris-cut}. Show that $I \models \neg \exists y\ F_\nu(a) = y$. Deduce, using a countable non-standard model of the theory of $\nat$, that $\mathrm I\Sigma_1$ does not prove $\forall k\ \forall x\ F_k(x){\downarrow}$.

:::solution
Since $\nu \leq a \in I$, the parameters $\nu$ and $a$ are in $I$. Suppose $I \models F_\nu(a) = z$ with $z \in I$. The formula $\mathrm{It}(\nu, 1, a, z)$ is $\Sigma_1$, so it holds in $M$ (:ref{#cor-sigma1-upward}), and functionality in $M$ (:ref{#fact-fgh-formal}) gives $z = F_\nu(a) \notin I$: a contradiction.

The sentence $\forall k\ \forall x\ F_k(x){\downarrow}$ is true in $\nat$, since $\mathrm{It}$ defines the functions $F_k$ there. Let $M$ be a countable non-standard model of the theory of $\nat$, given by compactness and the Löwenheim–Skolem theorem; it satisfies $\mathrm I\Sigma_1$ and the sentence. Choose $a$ non-standard and $\nu = a$; then $F_\nu(a){\downarrow}$ in $M$. The cut $I$ satisfies $\mathrm I\Sigma_1$ and, by the first part, not the sentence. So $\mathrm I\Sigma_1$ does not prove it. The next lesson obtains the same result from the general theorem on indicators.
:::
::::

::::exercise{#ex-catching-dominates difficulty=1 objective="Derive from the theorem a comparison of $F_\nu(a)$ with the standard levels of the hierarchy, without monotonicity in the index inside the model." lessons="fast-growing"}
Let $M$ be a countable model of $\mathrm I\Sigma_1$, $a \geq 1$ in $M$, and $\nu$ non-standard with $F_\nu(a){\downarrow}$. Show that $F_k(a) < F_\nu(a)$ for every standard $k$.

:::solution
Let $I$ be the cut of :ref{#thm-kirby-paris-cut}: $a \in I$, $F_\nu(a) \notin I$ and $I \models \mathrm I\Sigma_1$. For standard $k$, $I \models F_k(a) = z$ for some $z \in I$, by :ref{#lem-fgh-isigma1}; this $\Sigma_1$ fact goes up to $M$ (:ref{#cor-sigma1-upward}), and functionality in $M$ gives $z = F_k(a)$. So $F_k(a) \in I$, and since $I$ is an initial segment not containing $F_\nu(a)$, $F_k(a) < F_\nu(a)$. No comparison of $F_k$ and $F_\nu$ inside $M$ was used.
:::
::::
:::::
