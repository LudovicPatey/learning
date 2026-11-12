---
title: Σ⁰₁ separation and the Heine–Borel theorem
summary: WKL₀ is equivalent over RCA₀ to Σ⁰₁ separation and to the Heine–Borel covering theorem for [0, 1]; a survey of other theorems of analysis, algebra and logic equivalent to WKL₀.
duration: 50
prerequisites: [wkl0]
---

The reversals to $\mathsf{WKL}_0$ follow a different pattern from those to $\mathsf{ACA}_0$. One starts from an arbitrary infinite binary tree $T$, or from two disjoint $\Sigma^0_1$ properties, and builds an instance of the theorem whose solutions yield a path through $T$ or a separating set. The coding must not produce a single answer, such as the range of an injection, since $\mathsf{WKL}_0$ does not prove that such answers exist; it must preserve the freedom of choice between many paths. In computability-theoretic terms, the instances obtained from computable data have solutions of PA degree, and no better.

This lesson proves two equivalences. The first, with $\Sigma^0_1$ separation, is the formal version of the characterization of PA degrees by separating sets, and is the most convenient form of $\mathsf{WKL}$ for further reversals. The second, with the Heine–Borel theorem, is the prototype of the equivalences between $\mathsf{WKL}_0$ and compactness theorems of analysis.

## Σ⁰₁ separation

The **$\Sigma^0_1$ separation** scheme consists of the universal closures of
$$
\neg \exists n\, (\varphi(n) \wedge \psi(n)) \rightarrow \exists X\, \forall n\, \big( (\varphi(n) \rightarrow n \in X) \wedge (\psi(n) \rightarrow n \notin X) \big),
$$
for $\Sigma^0_1$ formulas $\varphi, \psi$, possibly with parameters. Its computability-theoretic form is the existence of separating sets for disjoint c.e. sets, one of the characterizations of PA degrees (:ref{#thm-pa-characterization}).

**Example.** With $\varphi(e) \equiv \Phi_e(e)\converge = 0$ and $\psi(e) \equiv \Phi_e(e)\converge = 1$, a separating set $X$ satisfies $X(e) \neq \Phi_e(e)$ whenever $\Phi_e(e)$ converges to $0$ or $1$; its characteristic function is DNC. No computable set separates these two formulas, so $\Sigma^0_1$ separation fails in $\mathrm{REC}$. Separation for $\Sigma^0_1$ formulas is also much weaker than comprehension: the formula $\varphi$ alone, with $\psi$ false, is separated by $\nat$, which carries no information.

**Intuition.** A separating set is a path through the tree of finite partial guesses that are not yet refuted, which gives the forward direction. Conversely, to find a path through an infinite binary tree $T$, one must decide at each node $\sigma$ whether to go to $\sigma 0$ or to $\sigma 1$. The only bad decision is to enter a successor that is not extendible to every length, and this is detected at a finite stage. So the two $\Sigma^0_1$ properties "$\sigma 0$ dies before $\sigma 1$" and "$\sigma 1$ dies before $\sigma 0$" are disjoint, and a set separating them tells the path where to go.

:::theorem{#thm-wkl-separation}
Over $\mathsf{RCA}_0$, $\mathsf{WKL}$ is equivalent to $\Sigma^0_1$ separation.
:::

:::proof{of=thm-wkl-separation}
($\Rightarrow$) Write $\varphi(n) \equiv \exists k\, \theta(n, k)$ and $\psi(n) \equiv \exists k\, \eta(n, k)$, with $\theta, \eta$ bounded. Let $T$ be the set of strings $\sigma$ such that for all $n, k < |\sigma|$, $\theta(n, k) \rightarrow \sigma(n) = 1$ and $\eta(n, k) \rightarrow \sigma(n) = 0$. It exists by $\Delta^0_1$ comprehension and is a tree. It is infinite: for each $m$, the string $\sigma$ of length $m$ with $\sigma(n) = 1$ if and only if $\theta(n, k)$ for some $k < m$ belongs to $T$, since no $n$ has witnesses for both formulas. A path $X$ separates: if $\varphi(n)$ with witness $k$, then $X(n) = 1$, by considering a prefix of length larger than $n$ and $k$; similarly for $\psi$.

($\Leftarrow$) Let $T$ be an infinite binary tree. For a string $\sigma$, say that $\sigma$ is **extendible to length $n$** if some $\tau \succeq \sigma$ of length $n$ belongs to $T$, a bounded property. Let
$$
\varphi(\sigma) \equiv \exists n\, (\sigma 0 \text{ is not extendible to length } n \wedge \sigma 1 \text{ is extendible to length } n),
$$
and $\psi(\sigma)$ the same with $0$ and $1$ exchanged, the lengths $n$ being larger than $|\sigma|$. They are disjoint: if $\varphi(\sigma)$ with $n$ and $\psi(\sigma)$ with $n'$, say $n \leq n'$, then $\sigma 0$ is extendible to length $n'$, hence to length $n$, a contradiction; the case $n' \leq n$ is symmetric. Let $S$ separate them, with $\varphi(\sigma) \rightarrow \sigma \in S$ and $\psi(\sigma) \rightarrow \sigma \notin S$. Define $P$ by $P \uh (k+1) = (P \uh k)\, i$ with $i = 1$ if $P \uh k \in S$ and $i = 0$ otherwise; it exists by $\Delta^0_1$ comprehension.

Let $E(\sigma)$ be the $\Pi^0_1$ property "$\sigma$ is extendible to every length". We show $E(P \uh k)$ for every $k$ by $\Pi^0_1$ induction (:ref{#prop-pi01-induction}). $E(\varepsilon)$ holds since $T$ is infinite. Suppose $E(\sigma)$ with $\sigma = P \uh k$. If neither $\sigma 0$ nor $\sigma 1$ had $E$, there would be lengths beyond which neither is extendible, and $\sigma$ would not be extendible beyond their maximum. If only $\sigma 1$ has $E$, then $\varphi(\sigma)$ holds, so $\sigma \in S$ and $P$ chooses $\sigma 1$; if only $\sigma 0$ has $E$, then $\psi(\sigma)$, $\sigma \notin S$, and $P$ chooses $\sigma 0$. If both have $E$, either choice works. So $E(P \uh (k+1))$. In particular every $P \uh k$ belongs to $T$, and $P$ is a path.
:::

:::figure[The reversal of :ref{#thm-wkl-separation} on a small tree. Dashed nodes are not extendible to every length. At a node where exactly one successor is extendible to every length, the other one dies at a finite length, one of the formulas $\varphi(\sigma)$, $\psi(\sigma)$ holds, and the separating set $S$ is forced to choose correctly; where both are extendible, $S$ is free.]
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="A binary tree: at the root only the right successor is extendible to every length, so the separating set sends the path to the right; at the node 1 both successors are extendible and either choice is correct"><line x1="190.0" y1="28" x2="105.0" y2="80" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="190.0" y1="28" x2="275.0" y2="80" class="accent-stroke" stroke-width="2.2"/><line x1="105.0" y1="80" x2="62.5" y2="132" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="105.0" y1="80" x2="147.5" y2="132" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="275.0" y1="80" x2="232.5" y2="132" class="accent-stroke" stroke-width="2.2"/><line x1="275.0" y1="80" x2="317.5" y2="132" class="ink-stroke" stroke-width="1.2"/><line x1="62.5" y1="132" x2="41.2" y2="184" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="232.5" y1="132" x2="211.2" y2="184" class="accent-stroke" stroke-width="2.2"/><line x1="232.5" y1="132" x2="253.8" y2="184" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="317.5" y1="132" x2="296.2" y2="184" class="ink-stroke" stroke-width="1.2"/><line x1="317.5" y1="132" x2="338.8" y2="184" class="ink-stroke" stroke-width="1.2"/><line x1="211.2" y1="184" x2="200.6" y2="236" class="accent-stroke" stroke-width="2.2"/><line x1="211.2" y1="184" x2="221.9" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="253.8" y1="184" x2="243.1" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="296.2" y1="184" x2="285.6" y2="236" class="ink-stroke" stroke-width="1.2"/><line x1="296.2" y1="184" x2="306.9" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="338.8" y1="184" x2="328.1" y2="236" class="ink-stroke" stroke-width="1.2"/><line x1="338.8" y1="184" x2="349.4" y2="236" class="ink-stroke" stroke-width="1.2"/><circle cx="190.0" cy="28" r="4" class="accent-fill"/><circle cx="105.0" cy="80" r="3" class="muted-fill"/><circle cx="275.0" cy="80" r="4" class="accent-fill"/><circle cx="62.5" cy="132" r="3" class="muted-fill"/><circle cx="147.5" cy="132" r="3" class="muted-fill"/><circle cx="232.5" cy="132" r="4" class="accent-fill"/><circle cx="317.5" cy="132" r="3.5" class="ink-fill"/><circle cx="41.2" cy="184" r="3" class="muted-fill"/><circle cx="211.2" cy="184" r="4" class="accent-fill"/><circle cx="253.8" cy="184" r="3" class="muted-fill"/><circle cx="296.2" cy="184" r="3.5" class="ink-fill"/><circle cx="338.8" cy="184" r="3.5" class="ink-fill"/><circle cx="200.6" cy="236" r="4" class="accent-fill"/><circle cx="221.9" cy="236" r="3" class="muted-fill"/><circle cx="243.1" cy="236" r="3" class="muted-fill"/><circle cx="285.6" cy="236" r="3.5" class="ink-fill"/><circle cx="306.9" cy="236" r="3" class="muted-fill"/><circle cx="328.1" cy="236" r="3.5" class="ink-fill"/><circle cx="349.4" cy="236" r="3.5" class="ink-fill"/><text x="200.6" y="256" text-anchor="middle" class="mrm" font-size="12">⋮</text><text x="285.6" y="256" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="328.1" y="256" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="349.4" y="256" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="200.0" y="22" class="mrm" font-size="13">ε</text><line x1="196.0" y1="28" x2="376" y2="44" class="muted-stroke" stroke-width="0.8" stroke-dasharray="2 3"/><text x="380" y="40" class="label">only 1 is extendible to every length:</text><text x="380" y="55" class="label">φ(ε) holds, so ε ∈ S: go to 1</text><line x1="281.0" y1="80" x2="376" y2="114" class="muted-stroke" stroke-width="0.8" stroke-dasharray="2 3"/><text x="380" y="110" class="label">both successors are extendible:</text><text x="380" y="125" class="label">either choice made by S is correct</text><line x1="238.5" y1="132" x2="376" y2="184" class="muted-stroke" stroke-width="0.8" stroke-dasharray="2 3"/><text x="380" y="180" class="label">only 100 is extendible (101 dies):</text><text x="380" y="195" class="label">ψ(10) holds, so 10 ∉ S: go to 100</text><line x1="24" y1="278" x2="44" y2="278" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="282" class="label">not extendible to every length</text><line x1="270" y1="278" x2="290" y2="278" class="accent-stroke" stroke-width="2.2"/><text x="296" y="282" class="label">the path P defined from S</text></svg>
:::

The separating set $S$ is used only along the path, and only at the nodes where a wrong choice is possible. The verification uses induction for a $\Pi^0_1$ formula, which $\mathsf{RCA}_0$ proves; the definition of $P$ uses only $\Delta^0_1$ comprehension relative to $S$.

:::quiz[Σ⁰₁ separation]
In the reversal of :ref{#thm-wkl-separation}, what does the separating set $S$ decide?

- [x] At each node $\sigma$, which successor to follow: it is correct whenever exactly one successor is extendible to every length, which is the only case where a choice matters.
- [ ] Which nodes belong to $T$.

  Membership in $T$ is decidable from $T$; the separating set decides directions.
- [ ] Which nodes are extendible to every length.

  This is a $\Pi^0_1$ property; $S$ only approximates it in the cases where exactly one successor fails.

---

Why is $\Pi^0_1$ induction needed in the verification?

- [x] Because the property "extendible to every length" is $\Pi^0_1$, and it must be propagated along all prefixes of $P$.
- [ ] Because $P$ is defined by recursion.

  The existence of $P$ follows from $\Delta^0_1$ comprehension; induction is used to prove that it is a path.
- [ ] Because $T$ is infinite.

  Infiniteness gives the base case only.

---

Why are $\varphi(\sigma)$ and $\psi(\sigma)$ disjoint?

- [x] Because extendibility is monotone in the length: if $\sigma 0$ is extendible to length $n'$ and $n \leq n'$, it is extendible to length $n$; so $\sigma 0$ cannot die at $n$ and survive at $n'$.
- [ ] Because $T$ is infinite.

  Disjointness holds for every tree, finite or not; it uses only that $T$ is closed under prefixes.
- [ ] Because $\sigma 0$ and $\sigma 1$ are incompatible.

  Incompatibility alone says nothing about the lengths at which the two successors die.
:::

::::exercise{difficulty=2}
Show that $\mathsf{WKL}$ is equivalent over $\mathsf{RCA}_0$ to the statement: for every pair of injective functions $f, g$ with disjoint ranges, there is a set $X$ containing the range of $f$ and disjoint from the range of $g$.

:::solution
The statement follows from $\Sigma^0_1$ separation with $\varphi(n) \equiv \exists i\, f(i) = n$ and $\psi(n) \equiv \exists i\, g(i) = n$. Conversely, let $\exists k\, \theta(n, k)$ and $\exists k\, \eta(n, k)$ be disjoint $\Sigma^0_1$ formulas. Let $f(\langle n, k \rangle) = 2n + 1$ if $k$ is the least witness of $\theta(n, k)$, and $f(\langle n, k \rangle) = 4 \langle n, k \rangle$ otherwise; let $g(\langle n, k \rangle) = 2n + 1$ if $k$ is the least witness of $\eta(n, k)$, and $g(\langle n, k \rangle) = 4 \langle n, k \rangle + 2$ otherwise. Both are injective, as in :ref{#thm-aca-equivalents}. Their ranges are disjoint: odd values $2n + 1$ come from $f$ only if $\theta$ has a witness for $n$, and from $g$ only if $\eta$ has one, which never happen together; the even values of $f$ are multiples of $4$ and those of $g$ are not. If $X$ contains the range of $f$ and avoids the range of $g$, the set $\{ n : 2n + 1 \in X \}$ separates the two formulas.
:::
::::

## The Heine–Borel theorem

The **Heine–Borel theorem** for $[0, 1]$ states: if a sequence of open intervals $(a_i, b_i)$ with rational endpoints covers $[0, 1]$, that is, every real $x \in [0, 1]$ lies in some $(a_i, b_i)$, then finitely many of them cover $[0, 1]$.

**Intuition.** The forward direction is the classical proof by bisection: if no finite subfamily covers, the dyadic intervals that are not covered by the first intervals of the sequence form an infinite binary tree, and a path converges to a point that is covered by no interval. For the reversal, the paths through a binary tree must be turned into points of $[0, 1]$, and the nodes outside the tree into open intervals. Binary expansions do not work well, because neighboring dyadic intervals share an endpoint; the Cantor middle-thirds set separates the pieces of each level by gaps, which can be covered by additional intervals that contain no point of the Cantor set.

:::theorem[Friedman]{#thm-wkl-heine-borel}
Over $\mathsf{RCA}_0$, $\mathsf{WKL}$ is equivalent to the Heine–Borel theorem for $[0, 1]$.
:::

:::proof{of=thm-wkl-heine-borel}
For a binary string $\sigma$, let $I_\sigma$ be the closed dyadic interval $[0.\sigma, 0.\sigma + 2^{-|\sigma|}]$.

($\Rightarrow$) Let $(a_i, b_i)$ cover $[0, 1]$, and suppose that no finite subfamily does. Let $T$ be the set of strings $\sigma$ such that $I_\sigma \not\subseteq \bigcup_{i < |\sigma|} (a_i, b_i)$, a decidable condition on rational intervals. $T$ is a tree, since $I_\tau \supseteq I_\sigma$ and fewer intervals are used for a prefix $\tau$ of $\sigma$. It is infinite: for each $n$, the finite union $\bigcup_{i < n} (a_i, b_i)$ misses some point of $[0, 1]$, which can be taken rational, as an endpoint of the uncovered set, and this point lies in some $I_\sigma$ with $|\sigma| = n$, so $\sigma \in T$. By $\mathsf{WKL}$, $T$ has a path $X$. The real $x = \sum_i X(i) 2^{-i-1}$ lies in every $I_{X \uh n}$. It is covered by some $(a_i, b_i)$, so $(x - \delta, x + \delta) \subseteq (a_i, b_i)$ for some $\delta > 0$. For $n > i$ with $2^{-n} < \delta$, $I_{X \uh n} \subseteq (a_i, b_i)$, contradicting $X \uh n \in T$.

($\Leftarrow$) Let $T$ be an infinite binary tree, and suppose that it has no path. We use the Cantor middle-thirds set: for a string $\sigma$, let $C_\sigma$ be the closed interval of length $3^{-|\sigma|}$ with left endpoint $\sum_{i < |\sigma|} 2\sigma(i) 3^{-i-1}$. Consider the following intervals:

- for each string $\sigma \notin T$, the open interval $U_\sigma$ obtained by enlarging $C_\sigma$ by $3^{-|\sigma|-1}$ on each side;
- the open middle thirds removed in the construction of the Cantor set, at every level.

The sequence of these intervals exists by $\Delta^0_1$ comprehension. It covers $[0, 1]$: a real $x$ outside the removed middle thirds lies in $\bigcap_n C_{X \uh n}$ for some $X$, which can be found by deciding at each level whether $x$ is in the left or the right third; since $X$ is not a path of $T$, some $X \uh n \notin T$, and $x \in C_{X \uh n} \subseteq U_{X \uh n}$. By Heine–Borel, finitely many intervals cover $[0, 1]$; let $n$ exceed the lengths of the strings $\sigma$ whose intervals $U_\sigma$ are used. For a string $\tau$ of length $n$, the left endpoint $c$ of $C_\tau$ is a point of the Cantor set, so it lies in none of the middle thirds, and it is covered by some $U_\sigma$ in the finite family. The interval $U_\sigma$ meets the Cantor set only in $C_\sigma$, because the neighboring intervals of level $|\sigma|$ are at distance at least $3^{-|\sigma|}$. So $c \in C_\sigma$, which means that $\sigma$ is a prefix of $\tau 0 0 \cdots$; since $|\sigma| < n$, $\sigma \preceq \tau$. As $\sigma \notin T$ and $T$ is a tree, $\tau \notin T$. So $T$ has no string of length $n$, contradicting its infiniteness.
:::

:::figure[The cover of the reversal of :ref{#thm-wkl-heine-borel}, for a tree $T$ whose strings are $\varepsilon, 0, 1, 00, 10, 11$. Shaded intervals $C_\sigma$ are those of strings of $T$. Each minimal string $\sigma \notin T$ gives an open interval $U_\sigma$, slightly larger than $C_\sigma$ but still disjoint from the other pieces of the Cantor set; the removed middle thirds cover the rest. Only the intervals of minimal strings and the first middle thirds are drawn: the others are contained in them.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The intervals of the Cantor set at levels 0 to 3; the strings outside the tree give enlarged open intervals, which together with the removed middle thirds cover the unit interval"><text x="28" y="35" text-anchor="end" class="label">0</text><rect x="40.0" y="22" width="520.0" height="18" class="cell head-cell"/><text x="300.0" y="35" text-anchor="middle" class="mrm" font-size="11">ε</text><text x="28" y="71" text-anchor="end" class="label">1</text><rect x="40.0" y="58" width="173.3" height="18" class="cell head-cell"/><text x="126.7" y="71" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="386.7" y="58" width="173.3" height="18" class="cell head-cell"/><text x="473.3" y="71" text-anchor="middle" class="mrm" font-size="11">1</text><text x="28" y="107" text-anchor="end" class="label">2</text><rect x="40.0" y="94" width="57.8" height="18" class="cell head-cell"/><text x="68.9" y="107" text-anchor="middle" class="mrm" font-size="11">00</text><rect x="155.6" y="94" width="57.8" height="18" class="cell"/><text x="184.4" y="107" text-anchor="middle" class="mrm" font-size="11">01</text><rect x="386.7" y="94" width="57.8" height="18" class="cell head-cell"/><text x="415.6" y="107" text-anchor="middle" class="mrm" font-size="11">10</text><rect x="502.2" y="94" width="57.8" height="18" class="cell head-cell"/><text x="531.1" y="107" text-anchor="middle" class="mrm" font-size="11">11</text><text x="28" y="143" text-anchor="end" class="label">3</text><rect x="40.0" y="130" width="19.3" height="18" class="cell"/><text x="49.6" y="143" text-anchor="middle" class="mrm" font-size="11">000</text><rect x="78.5" y="130" width="19.3" height="18" class="cell"/><text x="88.1" y="143" text-anchor="middle" class="mrm" font-size="11">001</text><rect x="155.6" y="130" width="19.3" height="18" class="cell"/><rect x="194.1" y="130" width="19.3" height="18" class="cell"/><rect x="386.7" y="130" width="19.3" height="18" class="cell"/><text x="396.3" y="143" text-anchor="middle" class="mrm" font-size="11">100</text><rect x="425.2" y="130" width="19.3" height="18" class="cell"/><text x="434.8" y="143" text-anchor="middle" class="mrm" font-size="11">101</text><rect x="502.2" y="130" width="19.3" height="18" class="cell"/><text x="511.9" y="143" text-anchor="middle" class="mrm" font-size="11">110</text><rect x="540.7" y="130" width="19.3" height="18" class="cell"/><text x="550.4" y="143" text-anchor="middle" class="mrm" font-size="11">111</text><text x="28" y="12" text-anchor="end" class="label">level</text><line x1="40" y1="226" x2="560" y2="226" class="axis"/><line x1="40.0" y1="222" x2="40.0" y2="230" class="ink-stroke" stroke-width="1"/><text x="40.0" y="244" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="560.0" y1="222" x2="560.0" y2="230" class="ink-stroke" stroke-width="1"/><text x="560.0" y="244" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="33.6" y1="186" x2="65.7" y2="186" class="accent-stroke" stroke-width="3"/><line x1="40.0" y1="182" x2="40.0" y2="190" class="accent-stroke" stroke-width="1"/><line x1="59.3" y1="182" x2="59.3" y2="190" class="accent-stroke" stroke-width="1"/><line x1="72.1" y1="200" x2="104.2" y2="200" class="accent-stroke" stroke-width="3"/><line x1="78.5" y1="196" x2="78.5" y2="204" class="accent-stroke" stroke-width="1"/><line x1="97.8" y1="196" x2="97.8" y2="204" class="accent-stroke" stroke-width="1"/><line x1="136.3" y1="186" x2="232.6" y2="186" class="accent-stroke" stroke-width="3"/><line x1="155.6" y1="182" x2="155.6" y2="190" class="accent-stroke" stroke-width="1"/><line x1="213.3" y1="182" x2="213.3" y2="190" class="accent-stroke" stroke-width="1"/><line x1="380.2" y1="200" x2="412.3" y2="200" class="accent-stroke" stroke-width="3"/><line x1="386.7" y1="196" x2="386.7" y2="204" class="accent-stroke" stroke-width="1"/><line x1="405.9" y1="196" x2="405.9" y2="204" class="accent-stroke" stroke-width="1"/><line x1="418.8" y1="186" x2="450.9" y2="186" class="accent-stroke" stroke-width="3"/><line x1="425.2" y1="182" x2="425.2" y2="190" class="accent-stroke" stroke-width="1"/><line x1="444.4" y1="182" x2="444.4" y2="190" class="accent-stroke" stroke-width="1"/><line x1="495.8" y1="200" x2="527.9" y2="200" class="accent-stroke" stroke-width="3"/><line x1="502.2" y1="196" x2="502.2" y2="204" class="accent-stroke" stroke-width="1"/><line x1="521.5" y1="196" x2="521.5" y2="204" class="accent-stroke" stroke-width="1"/><line x1="534.3" y1="186" x2="566.4" y2="186" class="accent-stroke" stroke-width="3"/><line x1="540.7" y1="182" x2="540.7" y2="190" class="accent-stroke" stroke-width="1"/><line x1="560.0" y1="182" x2="560.0" y2="190" class="accent-stroke" stroke-width="1"/><line x1="213.3" y1="216" x2="386.7" y2="216" class="muted-stroke" stroke-width="3"/><line x1="97.8" y1="216" x2="155.6" y2="216" class="muted-stroke" stroke-width="3"/><line x1="444.4" y1="216" x2="502.2" y2="216" class="muted-stroke" stroke-width="3"/><line x1="59.3" y1="216" x2="78.5" y2="216" class="muted-stroke" stroke-width="3"/><line x1="174.8" y1="216" x2="194.1" y2="216" class="muted-stroke" stroke-width="3"/><line x1="405.9" y1="216" x2="425.2" y2="216" class="muted-stroke" stroke-width="3"/><line x1="521.5" y1="216" x2="540.7" y2="216" class="muted-stroke" stroke-width="3"/><rect x="40" y="272" width="16" height="10" class="cell head-cell"/><text x="62" y="281" class="label">strings of T</text><line x1="170" y1="277" x2="190" y2="277" class="accent-stroke" stroke-width="3"/><text x="196" y="281" class="label">U for minimal σ ∉ T</text><line x1="340" y1="277" x2="360" y2="277" class="muted-stroke" stroke-width="3"/><text x="366" y="281" class="label">removed middle thirds</text></svg>
:::

The figure shows the mechanism of the contradiction: if finitely many $U_\sigma$ cover the Cantor set, the strings $\sigma$ involved bar every long string from $T$. Many verifications in this proof, such as the existence of the uncovered rational point and the case distinction on $x$, require care in $\mathsf{RCA}_0$; they are carried out in Simpson, Lemma IV.1.1 and Theorem IV.1.2, where the reversal uses the same Cantor set coding.

:::quiz[the Heine–Borel theorem]
In the reversal of :ref{#thm-wkl-heine-borel}, why is each $C_\sigma$ enlarged to an open interval $U_\sigma$ by only $3^{-|\sigma|-1}$ on each side?

- [x] So that $U_\sigma$ is open and covers the points of $C_\sigma$, while meeting no other piece of the Cantor set at level $|\sigma|$: these are at distance at least $3^{-|\sigma|}$.
- [ ] So that the intervals $U_\sigma$ are pairwise disjoint.

  $U_\sigma$ and $U_\tau$ overlap when $\sigma \preceq \tau$; what matters is that $U_\sigma$ contains no point of the Cantor set outside $C_\sigma$.
- [ ] So that the total length of the cover is less than $1$.

  The cover must cover $[0, 1]$; its total length plays no role.

---

Where is the hypothesis that $T$ has no path used?

- [x] To show that the intervals cover the points of the Cantor set: such a point determines a sequence $X$, which is not a path, so some $X \uh n \notin T$.
- [ ] To show that the sequence of intervals exists.

  The sequence is defined from $T$ by $\Delta^0_1$ comprehension, whether or not $T$ has a path.
- [ ] To show that $T$ has no string of length $n$.

  This uses the finite subcover, which exists by the Heine–Borel theorem once the family is known to cover $[0, 1]$.
:::

## Other equivalents

The following theorems are also equivalent to $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$; we admit the proofs, in Simpson, Chapter IV.

| Area | Statement equivalent to $\mathsf{WKL}_0$ | Simpson |
| --- | --- | --- |
| Analysis | every continuous function on $[0, 1]$ is bounded; it is uniformly continuous | Theorem IV.2.3 |
| Logic | Gödel's completeness theorem for countable languages; Lindenbaum's lemma | Theorem IV.3.3 |
| Algebra | every countable commutative ring has a prime ideal | Theorem IV.6.4 |
| Topology | Brouwer's fixed point theorem for the unit square | Theorem IV.7.7 |
| Functional analysis | the Hahn–Banach theorem for separable Banach spaces | Theorems IV.9.3–IV.9.4 |

Several of these reversals, such as the one for prime ideals, go through $\Sigma^0_1$ separation in the form of the exercise above, with two injections with disjoint ranges; others, such as the one for Brouwer's theorem, start from an infinite binary tree with no path, as in the proof of :ref{#thm-wkl-heine-borel}. The usual proofs of all these theorems use compactness, in the form of a finite subcover or of a path through an infinite binary tree of choices.

## Notes and references

$\Sigma^0_1$ separation is Simpson, Lemma IV.4.4, which also contains the form with injections of the exercise; the main results of Section IV.4 are from Friedman, Simpson and Smith (1983). The equivalence with the Heine–Borel theorem was announced by Friedman (1976) (Simpson, Theorem IV.1.2 and notes to Section IV.1). Dzhafarov and Mummert, Sections 5.6.2 and 10.5, and Hirschfeldt, Section 4.4, give the same equivalences.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Chapter IV.
- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- H. Friedman, S. G. Simpson and R. L. Smith, *Countable algebra and set existence axioms*, Annals of Pure and Applied Logic 25 (1983), 141–181.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.6.2 and 10.5.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 4.4.
