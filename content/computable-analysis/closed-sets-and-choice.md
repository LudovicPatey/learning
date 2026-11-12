---
title: Closed sets and closed choice
summary: Closed subsets of the unit interval given by negative information; co-c.e. closed sets are exactly the zero sets of computable functions; problems on represented spaces; choosing a point in a non-empty closed set is Weihrauch equivalent to weak König's lemma.
duration: 45
prerequisites: [continuous-functions, reducibilities/parallelization]
---

The previous lesson showed that the maximum value of a continuous function on $[0, 1]$ is computable from the function. A point where the maximum is attained, or a zero of the function, is another matter. The set of such points is closed, and it is described by **negative information**: an algorithm can enumerate the points that are not zeros, by finding non-zero values, but never certify that a point is one. This lesson studies closed sets given in this way, the effective counterpart of $\Pi^0_1$ classes, and the problem of choosing a point in a non-empty closed set. This problem, **closed choice**, is Weihrauch equivalent to weak König's lemma, and it serves as an upper bound for the theorems of analysis classified in the next two lessons. To state the equivalence, Weihrauch reducibility is extended from problems on sets of numbers to problems on represented spaces.

## Closed sets with negative information

:::definition{#def-closed-negative}
The representation $\psi_>$ of the closed subsets of $[0, 1]$ is defined by $\psi_>(p) = A$ if each $p(i)$ codes a pair $(c_i, d_i)$ of rationals and
$$
[0, 1] \setminus A = [0, 1] \cap \bigcup_{i \,:\, c_i < d_i} (c_i, d_i).
$$
A closed set $A \subseteq [0, 1]$ is **co-c.e. closed**, or **effectively closed**, if it has a computable $\psi_>$-name.
:::

A name lists rational open intervals that exhaust the complement of $A$; pairs with $c_i \geq d_i$ stand for the empty interval and allow the name of $[0, 1]$ itself. Every closed set has a name, since its complement is a union of rational open intervals. A name gives information on what is not in $A$, and never confirms that a point belongs to $A$: whether $A$ is empty is not decided by any finite part of a name, since the first $n$ intervals of a name of $\emptyset$ may leave a point uncovered.

The definition extends to any computable metric space, with rational balls in place of rational intervals. In Cantor space with the metric of :ref{#ex-computable-metric-spaces}, the open ball of radius $2^{-n}$ around $\sigma 0^\infty$ is the cylinder of the first $n+1$ bits of $\sigma 0^\infty$, so the rational balls are the cylinders, and the co-c.e. closed sets are the classes whose complement is a c.e. union of cylinders: the $\Pi^0_1$ classes (:ref{#prop-pi01-equivalent}). Co-c.e. closed sets of a computable metric space are the analogue of $\Pi^0_1$ classes, and the results below are their counterparts in $[0, 1]$.

:::example{#ex-co-ce-closed}
1. For a computable $x \in [0, 1]$, $\{ x \}$ is co-c.e. closed: from a name $(q_k)$ of $x$, list the intervals $(-1, q_k - 2^{-k})$ and $(q_k + 2^{-k}, 2)$. Their union is $\mathbb R \setminus \{ x \}$: none of them contains $x$, since $|q_k - x| \leq 2^{-k}$, and every $y \neq x$ lies in one of them for $k$ with $2^{-k+1} < |y - x|$.
2. If $a \leq b$ are reals in $[0, 1]$, $a$ left-c.e. and $b$ right-c.e., then $[a, b]$ is co-c.e. closed: list $(-1, q)$ for the rationals $q < a$ and $(q, 2)$ for the rationals $q > b$, which are enumerated by :ref{#def-left-right}.
3. If $f \in C[0, 1]$ is computable, then its zero set $f^{-1}(0)$ is co-c.e. closed, by the next theorem.
:::

:::theorem{#thm-zero-sets}
1. The map $f \mapsto f^{-1}(0)$ is $(\delta_C, \psi_>)$-computable.
2. There is an algorithm which, given a $\psi_>$-name of a closed set $A \subseteq [0, 1]$, computes a $\delta_C$-name of a function $f \in C[0, 1]$ with $f \geq 0$ and $f^{-1}(0) = A$.

In particular, a closed set $A \subseteq [0, 1]$ is co-c.e. closed if and only if it is the zero set of a computable function.
:::

:::proof{of=thm-zero-sets}
1. By :ref{#thm-cauchy-rectangle}, a rectangle name of $f$ is computed from a $\delta_C$-name. List the intervals $(a - r, a + r)$ of the listed rectangles $(a, r, b, s)$ with $b - s > 0$ or $b + s < 0$. On such an interval, $f \geq b - s > 0$ or $f \leq b + s < 0$, so it contains no zero. Conversely, if $f(x) \neq 0$, some listed rectangle has $|x - a| < r$ and $s < |f(x)|/2$; since $|f(x) - b| \leq s$, it satisfies $b - s > 0$ if $f(x) > 0$, and $b + s < 0$ if $f(x) < 0$. So the listed intervals cover exactly the points of $[0, 1]$ where $f$ does not vanish.

2. For $i \in \nat$, let $h_i(x) = \min(1, \max(0, \min(x - c_i, d_i - x)))$, a tent function, positive exactly on $(c_i, d_i)$, and identically $0$ if $c_i \geq d_i$. Let $f = \sum_i 2^{-i-1} h_i$ on $[0, 1]$. The partial sums $F_n = \sum_{i < n} 2^{-i-1} h_i$ are rational polygons computed from the name, and $d(F_n, f) \leq \sum_{i \geq n} 2^{-i-1} = 2^{-n}$; so $d(F_k, F_l) \leq 2^{-k}$ for $k \leq l$, and $(F_n)$ is a $\delta_C$-name of $f$. A point $x \in [0, 1]$ satisfies $f(x) = 0$ if and only if $h_i(x) = 0$ for every $i$, that is, $x$ lies in none of the intervals $(c_i, d_i)$, that is, $x \in A$.
:::

## Problems on represented spaces

The problems of :ref{to="reducibilities/omega-reducibility"} have sets of numbers as instances and solutions. In analysis, instances and solutions are reals, functions or closed sets, given through names.

:::definition{#def-problem-represented}
Let $(X, \delta_X)$ and $(Y, \delta_Y)$ be represented spaces.
1. A **problem** $\mathsf P :\subseteq X \rightrightarrows Y$ consists of a set $\dom \mathsf P \subseteq X$ of **instances** and, for each instance $x$, a non-empty set $\mathsf P(x) \subseteq Y$ of **solutions**. A **realizer** of $\mathsf P$ is a function $F :\subseteq \bs \to \bs$ such that $F(p)$ is a name of a solution to $x$ for every name $p$ of an instance $x$. The problem is **computable** if it has a computable realizer.
2. For problems $\mathsf P :\subseteq X \rightrightarrows Y$ and $\mathsf Q :\subseteq Z \rightrightarrows W$, $\mathsf P$ is **Weihrauch reducible** to $\mathsf Q$, $\mathsf P \leq_W \mathsf Q$, if there are computable $\Phi, \Psi :\subseteq \bs \to \bs$ such that, for every name $p$ of an instance $x$ of $\mathsf P$, $\Phi(p)$ is a name of an instance $z$ of $\mathsf Q$, and for every name $q$ of a solution to $z$, $\Psi(\langle p, q \rangle)$ is a name of a solution to $x$. The reduction is **strong**, $\mathsf P \leq_{sW} \mathsf Q$, if $\Psi$ only uses $q$.
:::

The definition is :ref{#def-weihrauch} applied to the problem on names: its instances are the names of the instances of $\mathsf P$, coded as sets through their graphs, and the solutions to a name $p$ of $x$ are the names of the solutions to $x$. The problems of the course on reducibilities, such as $\mathsf{WKL}$, $\mathsf{LLPO}$, $\mathsf{LPO}$ and $\mathsf J$, are problems on represented spaces in which sets and trees are represented by their characteristic functions, and all their reductions remain valid. The degree of a problem on represented spaces depends on the representations, as the comparison of Cauchy and decimal names showed: they are part of the problem.

## Closed choice

:::definition{#def-closed-choice}
**Closed choice** on $[0, 1]$ is the problem $\mathsf C_{[0,1]}$ whose instances are the non-empty closed sets $A \subseteq [0, 1]$, represented by $\psi_>$, and whose solutions to $A$ are the points of $A$, represented by $\rho$.
:::

Every instance has solutions, but a name of $A$ only says where the points of $A$ are not. The proof that closed choice reduces to weak König's lemma builds the tree of dyadic intervals that are not yet known to be disjoint from $A$ (:ref{#fig-closed-choice-tree}). The converse codes a tree into a closed subset of the Cantor set, as in the reversal of the Heine–Borel theorem.

:::figure[The tree of the proof of :ref{#thm-closed-choice-wkl} for $A = [0.3, 0.4] \cup [0.8, 0.85]$, given by the intervals $J_0 = (0.4, 0.8)$, $J_1 = (-1, 0.3)$ and $J_2 = (0.85, 2)$, enumerated in this order. A string $\sigma$ of length $n$ is a node when the dyadic interval $I_\sigma$ is not covered by $J_0, \dots, J_{n-1}$. The intervals of the nodes always contain the points of $A$, and the paths converge to points of $A$.]{#fig-closed-choice-tree}
<svg class="fig" viewBox="0 0 640 300" width="640" role="img" aria-label="Dyadic intervals at levels 0 to 3; those not covered by the first n enumerated intervals are the nodes of the tree. The closed set A lies in the shaded nodes."><text x="20.0" y="36.0" text-anchor="start" class="mrm" font-size="12">n = 0</text><rect x="70.0" y="22" width="500.0" height="20" class="cell head-cell"/><text x="320.0" y="36.0" text-anchor="middle" class="mrm" font-size="11">ε</text><text x="20.0" y="70.0" text-anchor="start" class="mrm" font-size="12">n = 1</text><rect x="70.0" y="56" width="250.0" height="20" class="cell head-cell"/><text x="195.0" y="70.0" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="320.0" y="56" width="250.0" height="20" class="cell head-cell"/><text x="445.0" y="70.0" text-anchor="middle" class="mrm" font-size="11">1</text><text x="20.0" y="104.0" text-anchor="start" class="mrm" font-size="12">n = 2</text><rect x="70.0" y="90" width="125.0" height="20" class="cell"/><text x="132.5" y="104.0" text-anchor="middle" class="mrm muted" font-size="11">00</text><rect x="195.0" y="90" width="125.0" height="20" class="cell head-cell"/><text x="257.5" y="104.0" text-anchor="middle" class="mrm" font-size="11">01</text><rect x="320.0" y="90" width="125.0" height="20" class="cell"/><text x="382.5" y="104.0" text-anchor="middle" class="mrm muted" font-size="11">10</text><rect x="445.0" y="90" width="125.0" height="20" class="cell head-cell"/><text x="507.5" y="104.0" text-anchor="middle" class="mrm" font-size="11">11</text><text x="20.0" y="138.0" text-anchor="start" class="mrm" font-size="12">n = 3</text><rect x="70.0" y="124" width="62.5" height="20" class="cell"/><text x="101.2" y="138.0" text-anchor="middle" class="mrm muted" font-size="11">000</text><rect x="132.5" y="124" width="62.5" height="20" class="cell"/><text x="163.8" y="138.0" text-anchor="middle" class="mrm muted" font-size="11">001</text><rect x="195.0" y="124" width="62.5" height="20" class="cell head-cell"/><text x="226.2" y="138.0" text-anchor="middle" class="mrm" font-size="11">010</text><rect x="257.5" y="124" width="62.5" height="20" class="cell head-cell"/><text x="288.8" y="138.0" text-anchor="middle" class="mrm" font-size="11">011</text><rect x="320.0" y="124" width="62.5" height="20" class="cell"/><text x="351.2" y="138.0" text-anchor="middle" class="mrm muted" font-size="11">100</text><rect x="382.5" y="124" width="62.5" height="20" class="cell"/><text x="413.8" y="138.0" text-anchor="middle" class="mrm muted" font-size="11">101</text><rect x="445.0" y="124" width="62.5" height="20" class="cell head-cell"/><text x="476.2" y="138.0" text-anchor="middle" class="mrm" font-size="11">110</text><rect x="507.5" y="124" width="62.5" height="20" class="cell"/><text x="538.8" y="138.0" text-anchor="middle" class="mrm muted" font-size="11">111</text><line x1="60" y1="245" x2="580" y2="245" class="axis"/><line x1="70.0" y1="241" x2="70.0" y2="249" class="ink-stroke" stroke-width="1"/><text x="70.0" y="265.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="195.0" y1="241" x2="195.0" y2="249" class="ink-stroke" stroke-width="1"/><text x="195.0" y="265.0" text-anchor="middle" class="mrm" font-size="12">0.25</text><line x1="320.0" y1="241" x2="320.0" y2="249" class="ink-stroke" stroke-width="1"/><text x="320.0" y="265.0" text-anchor="middle" class="mrm" font-size="12">0.5</text><line x1="445.0" y1="241" x2="445.0" y2="249" class="ink-stroke" stroke-width="1"/><text x="445.0" y="265.0" text-anchor="middle" class="mrm" font-size="12">0.75</text><line x1="570.0" y1="241" x2="570.0" y2="249" class="ink-stroke" stroke-width="1"/><text x="570.0" y="265.0" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="270.0" y1="185" x2="470.0" y2="185" class="muted-stroke" stroke-width="3"/><text x="370.0" y="180.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">0</tspan></text><line x1="40.0" y1="201" x2="220.0" y2="201" class="muted-stroke" stroke-width="3"/><text x="130.0" y="196.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">1</tspan></text><line x1="495.0" y1="217" x2="600.0" y2="217" class="muted-stroke" stroke-width="3"/><text x="547.5" y="212.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">2</tspan></text><line x1="220.0" y1="245" x2="270.0" y2="245" class="accent-stroke" stroke-width="4"/><line x1="470.0" y1="245" x2="495.0" y2="245" class="accent-stroke" stroke-width="4"/><text x="245.0" y="237.0" text-anchor="middle" class="math" font-size="14">A</text><text x="457.5" y="237.0" text-anchor="end" class="math" font-size="14">A</text><text x="320.0" y="288.0" text-anchor="middle" class="label">Shaded: the dyadic intervals of level n not covered by the first n intervals J.</text></svg>
:::

:::theorem[Brattka, de Brecht, Pauly]{#thm-closed-choice-wkl}
$\mathsf C_{[0,1]} \equiv_{sW} \mathsf{WKL}$.
:::

:::proof{of=thm-closed-choice-wkl}
For a binary string $\sigma$, let $I_\sigma = [\sum_{i < |\sigma|} \sigma(i)\, 2^{-i-1},\ \sum_{i < |\sigma|} \sigma(i)\, 2^{-i-1} + 2^{-|\sigma|}]$, the closed dyadic interval of the reals whose binary expansions may begin with $\sigma$.

($\mathsf C_{[0,1]} \leq_{sW} \mathsf{WKL}$) Let $(c_i, d_i)_i$ be a name of $A$, and let $T$ be the set of strings $\sigma$ such that $I_\sigma$ is not included in $\bigcup_{i < |\sigma|,\, c_i < d_i} (c_i, d_i)$. It is decidable, uniformly in the name, by :ref{#lem-effective-heine-borel} (1). It is a tree: if $\tau \in T$ and $\sigma \preceq \tau$, then $I_\tau \subseteq I_\sigma$ and fewer intervals are used for $\sigma$, so $I_\sigma$ is not covered either. It is infinite: if $x \in A$, then for every $n$ some $\sigma$ of length $n$ has $x \in I_\sigma$, and $I_\sigma$ is not covered by intervals disjoint from $A$. Let $X$ be a path through $T$ and $x = \sum_i X(i)\, 2^{-i-1}$, so that $x \in I_{X \uh n}$ for every $n$. If $x \notin A$, then $x \in (c_i, d_i)$ for some $i$; for $n > i$ large enough, $2^{-n}$ is smaller than the distance from $x$ to the endpoints $c_i, d_i$, so $I_{X \uh n} \subseteq (c_i, d_i)$, and $X \uh n \notin T$, a contradiction. So $x \in A$, and $x$ is computed from $X$ alone, by the partial sums of the binary expansion.

($\mathsf{WKL} \leq_{sW} \mathsf C_{[0,1]}$) For a string $\sigma$, let $K_\sigma = [l_\sigma, l_\sigma + 3^{-|\sigma|}]$ with $l_\sigma = \sum_{i < |\sigma|} 2\sigma(i)\, 3^{-i-1}$, the interval of level $|\sigma|$ of the Cantor set $\mathcal K$, and let $\iota(X) = \sum_i 2X(i)\, 3^{-i-1}$. Given an infinite binary tree $T$, list (a) for each string $\tau$ the open middle third $(l_\tau + 3^{-|\tau|-1},\ l_\tau + 2 \cdot 3^{-|\tau|-1})$, and the intervals $(-1, 0)$ and $(1, 2)$; (b) for each $\sigma \notin T$ the interval $(l_\sigma - 3^{-|\sigma|-1},\ l_\sigma + 3^{-|\sigma|} + 3^{-|\sigma|-1})$. The intervals (a) cover the complement of $\mathcal K$. An interval (b) meets $\mathcal K$ only inside $K_\sigma$, since the other intervals of level $|\sigma|$ are at distance at least $3^{-|\sigma|}$ from $K_\sigma$; and $K_\sigma \cap \mathcal K = \iota[[\sigma]]$ contains no point of $\iota[[T]]$, since no path of $T$ extends $\sigma$. Conversely, a point $\iota(X)$ with $X \notin [T]$ lies in $K_{X \uh n}$ for some $X \uh n \notin T$. So the list is a $\psi_>$-name of $\iota[[T]]$, which is non-empty by weak König's lemma. Given a point $y \in \iota[[T]]$, compute $X$ with $\iota(X) = y$ bit by bit: once $X \uh n$ is known, $y$ lies in $K_{X \uh n \, 0}$ or $K_{X \uh n \, 1}$, two intervals at distance $3^{-n-1}$, and an approximation of $y$ within $3^{-n-2}$ decides which. Then $X \in [T]$, and $X$ is computed from $y$ alone.
:::

The first half is a uniform version of the compactness of $[0, 1]$: the tree records the finite stages at which the enumeration has not yet covered a dyadic interval, and a path is a sequence of choices that are never refuted. By :ref{#thm-wkl-llpo}, closed choice is thus equivalent to $\widehat{\mathsf{LLPO}}$: choosing a point in a closed subset of $[0, 1]$ amounts to countably many binary choices made in parallel.

:::quiz[closed choice]
In the proof that $\mathsf C_{[0,1]} \leq_{sW} \mathsf{WKL}$, why does a string of length $n$ only test the first $n$ intervals of the name?

- [x] Because membership in $T$ must be decidable; with finitely many intervals, coverage of $I_\sigma$ is decided by :ref{#lem-effective-heine-borel}, while coverage by all intervals of the name is only semi-decidable.
- [ ] Because the other intervals may intersect $A$.

  No interval of the name intersects $A$.
- [ ] Because the tree must be finite.

  The tree is infinite; that is why it has a path.

---

In the proof that $\mathsf{WKL} \leq_{sW} \mathsf C_{[0,1]}$, why is the Cantor set used rather than binary expansions in $[0, 1]$?

- [x] Because the backward functional must recover $X$ from the point $\iota(X)$, and in the Cantor set the intervals $K_{\sigma 0}$ and $K_{\sigma 1}$ are separated by a gap; with binary expansions, a dyadic rational has two expansions, and no finite approximation decides between them.
- [ ] Because the Cantor set is closed.

  $[0, 1]$ is closed as well; the gaps are what matter.
- [ ] Because $\iota$ is not continuous.

  $\iota$ is continuous, and even computable.
:::

## Exercises

::::exercise{difficulty=1}
Show that a closed set $A \subseteq [0, 1]$ is co-c.e. closed if and only if the set of pairs of rationals $c \leq d$ with $[c, d] \cap A = \emptyset$ is c.e.

:::solution
If the set of such pairs is c.e., list the corresponding open intervals $(c, d)$; every $x \in [0, 1] \setminus A$ lies in the interior of a rational closed interval disjoint from the closed set $A$, so the union of the listed intervals is the complement of $A$ in $[0, 1]$. Conversely, given a computable name of $A$, $[c, d] \cap A = \emptyset$ holds if and only if $[c, d] \cap [0, 1]$ is covered by finitely many listed intervals, by compactness; this is c.e. by :ref{#lem-effective-heine-borel} (1), applied to the closed interval $[\max(c, 0), \min(d, 1)]$ when it is non-empty.
:::
::::

::::exercise{difficulty=2}
**Unique choice.** Show that there is an algorithm which, given a $\psi_>$-name of a singleton $\{ x \} \subseteq [0, 1]$, computes a Cauchy name of $x$. Deduce that if a computable $f \in C[0, 1]$ has a unique zero, this zero is computable.

:::solution
Given $k$, search for a rational $c$ and $n$ such that the first $n$ intervals of the name cover $[0, 1] \setminus (c - 2^{-k}, c + 2^{-k})$, a union of at most two rational closed intervals; this is decidable by :ref{#lem-effective-heine-borel} (1). The search terminates: for a rational $c$ with $|c - x| < 2^{-k-1}$, the compact set $[0, 1] \setminus (c - 2^{-k}, c + 2^{-k})$ does not contain $x$, so it is covered by the intervals of the name, hence by finitely many of them. Any $c$ found satisfies $x \in (c - 2^{-k}, c + 2^{-k})$, since $x$ is not covered. The rationals $c$ found for each $k$ form a Cauchy name by :ref{#lem-cauchy-variants}. For the consequence, apply this to a computable name of the zero set (:ref{#thm-zero-sets}). The algorithm is uniform: unique choice on $[0, 1]$ is computable, while closed choice is not.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{LLPO} \leq_{sW} \mathsf C_{[0,1]}$ directly: from an instance $p$ of $\mathsf{LLPO}$, compute a name of a non-empty closed set $A_p \subseteq [0, 1]$ such that every point of $A_p$ below $1/2$ indicates one solution and every point above $1/2$ the other.

:::solution
Let $A_p = [0, 1/3] \cup [2/3, 1]$ if $p$ has no $1$; $A_p = [2/3, 1]$ if the $1$ of $p$ is at an even position; $A_p = [0, 1/3]$ if it is at an odd position. A name lists $(1/3, 2/3)$, and, if $p(n) = 1$ is found with $n$ even (respectively odd), the interval $(-1, 2/3)$ (respectively $(1/3, 2)$); until then, it lists empty pairs. Given $x \in A_p$, decide whether $x < 1/2$ or $x > 1/2$ from an approximation within $1/12$, since $x \notin (1/3, 2/3)$. If $x > 1/2$, then $p$ has no $1$ at an odd position, and the solution is $1$; if $x < 1/2$, then $p$ has no $1$ at an even position, and the solution is $0$. This also follows from :ref{#thm-closed-choice-wkl} and $\mathsf{LLPO} \leq_W \widehat{\mathsf{LLPO}} \equiv_W \mathsf{WKL}$.
:::
::::

## Notes and references

Representations of closed and compact subsets of Euclidean space by positive and negative information are Weihrauch, Sections 5.1–5.2 (Definition 5.1.1), and the representation of zero sets is his Theorem 6.2.9; Brattka and Presser (2003) treat closed subsets of computable metric spaces. Isolated zeros of computable functions are computable (Weihrauch, Corollary 6.3.9). Choice problems were first studied in the Weihrauch degrees by Gherardi and Marcone (2009) and by Brattka and Gherardi (2011); the equivalence $\mathsf C_{[0,1]} \equiv_{sW} \mathsf{WKL}$ is due to Brattka, de Brecht and Pauly (2012, Corollary 4.6), and is stated in Brattka, Gherardi and Pauly, Theorem 7.23 and Corollary 7.24, with the general form: choice on a computably compact computable metric space reduces to $\mathsf{WKL}$, and is equivalent to it when the space is rich, that is, contains a computable copy of Cantor space.

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Sections 5.1, 5.2, 6.2 and 6.3.
- V. Brattka and G. Gherardi, *Effective choice and boundedness principles in computable analysis*, Bulletin of Symbolic Logic 17 (2011), 73–117.
- V. Brattka, M. de Brecht and A. Pauly, *Closed choice and a uniform low basis theorem*, Annals of Pure and Applied Logic 163 (2012), 986–1008.
- G. Gherardi and A. Marcone, *How incomputable is the separable Hahn–Banach theorem?*, Notre Dame Journal of Formal Logic 50 (2009), 393–425.
- V. Brattka, G. Gherardi and A. Pauly, *Weihrauch complexity in computable analysis*, in V. Brattka and P. Hertling (eds.), *Handbook of Computability and Complexity in Analysis*, Springer, 2021, 367–417.
- V. Brattka and G. Presser, *Computability on subsets of metric spaces*, Theoretical Computer Science 305 (2003), 43–76.
