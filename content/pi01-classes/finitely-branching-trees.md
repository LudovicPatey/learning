---
title: Finitely branching trees
summary: Trees of sequences of integers; König's lemma; computably bounded trees behave like binary trees; a computable finitely branching tree whose paths all compute ∅′; the strength needed for König's lemma.
duration: 40
prerequisites: [pa-degrees]
---

Binary trees model problems with two choices at each step. Many problems have more: a coloring of a graph with $k$ colors, a function bounded by a known bound, or a sequence of integers with no a priori bound at all. This lesson considers trees of finite sequences of integers. When the branching is bounded by a computable function, nothing changes: the paths of such a tree are, up to a computable coding, the members of a $\Pi^0_1$ class. When the branching is finite but not computably bounded, König's lemma still guarantees a path, but finding one may require computing the halting set.

## Trees of integers

Write $\nat^{<\nat}$ for the set of finite sequences of integers, with the same notation as for binary strings, and $\nat^\nat$ for **Baire space**, the set of infinite sequences of integers. A **tree** is a subset $T \subseteq \nat^{<\nat}$ closed under prefixes, and a **path** through $T$ is a sequence $P \in \nat^\nat$ all of whose prefixes belong to $T$. A tree is **finitely branching** if every node $\sigma \in T$ has finitely many immediate successors $\sigma v \in T$. It is **computably bounded** if there is a computable function $g$ with $\sigma(n) < g(n)$ for every $\sigma \in T$ and $n < |\sigma|$.

For example, the set of strings $\sigma$ with $\sigma(n) \leq n$ for all $n < |\sigma|$ is a computably bounded tree, with $g(n) = n + 1$. The tree $\{ \varepsilon \} \cup \{ \langle m \rangle : m \in \nat \}$ of strings of length at most $1$ is infinite and not finitely branching, and it has no path. A computable finitely branching tree need not be computably bounded: in the tree of :ref{#thm-finitely-branching-jump} below, the values at position $n$ depend on the stage at which $n$ enters $\emptyset'$.

:::lemma[König's lemma]{#lem-konig}
Every infinite finitely branching tree has a path.
:::

:::proof{of=lem-konig}
Call a node **large** if infinitely many nodes of $T$ extend it. The root is large. If $\sigma$ is large, then since the nodes extending $\sigma$, other than $\sigma$, extend one of its finitely many successors, one successor is large. Define $P(n)$ as the least $v$ such that $(P \uh n)\, v$ is large. By induction every prefix of $P$ is large, hence in $T$.
:::

The hypothesis of finite branching is necessary: the tree $\{ \sigma : \sigma(i) \geq |\sigma| \text{ for all } i < |\sigma| \}$ is infinite and has no path (see the quiz after :ref{#lem-weak-konig}).

## Coding into binary trees

We code a sequence of integers by a binary sequence, writing each value in unary followed by a separator:
$$
c(\sigma) = 1^{\sigma(0)}\, 0\, 1^{\sigma(1)}\, 0 \cdots 1^{\sigma(n-1)}\, 0, \qquad c(P) = 1^{P(0)}\, 0\, 1^{P(1)}\, 0 \cdots
$$
This is the coding of :ref{#prop-baire-cantor}. The map $c$ is a bijection from $\nat^\nat$ onto the sequences with infinitely many zeros, and $P \equiv_T c(P)$, uniformly: each bit of $c(P)$ is computed from finitely many values of $P$, and $P(n)$ is the length of the $n$-th block of ones of $c(P)$.

:::proposition{#prop-finitely-branching-coding}
Let $T \subseteq \nat^{<\nat}$ be a computable finitely branching tree, and let $S$ be the set of binary strings that are prefixes of some $c(\sigma)$ with $\sigma \in T$.

1. $S$ is a c.e. binary tree, and $[S] = \{ c(P) : P \in [T] \}$.
2. If $T$ is computably bounded, then $S$ is computable, so $c([T])$ is a $\Pi^0_1$ class.
:::

:::proof{of=prop-finitely-branching-coding}
$S$ is closed under prefixes by definition. A binary string $\rho$ decomposes uniquely as $c(\tau)\, 1^k$, with $\tau$ the sequence of complete blocks and $k \geq 0$. Then $\rho \in S$ if and only if $\tau \in T$ and, in case $k > 0$, some $v \geq k$ has $\tau v \in T$. This is a c.e. condition, and it is decidable when $T$ is computably bounded by $g$, since then only the values $k \leq v < g(|\tau|)$ need to be tested.

If $P \in [T]$, every prefix of $c(P)$ is a prefix of some $c(P \uh n)$, so $c(P) \in [S]$. Conversely, let $Y \in [S]$. If $Y$ had only finitely many zeros, it would end with $1^\infty$ after some $c(\tau)$, and $\tau$ would have successors $\tau v \in T$ with arbitrarily large $v$, contradicting finite branching. So $Y = c(P)$ for some $P$, and every prefix $c(P \uh n)$ of $Y$ is in $S$, which by the decomposition means $P \uh n \in T$. So $P \in [T]$.
:::

:::corollary{#cor-bounded-pa}
Let $T$ be an infinite computable computably bounded tree. Every PA set computes a path through $T$, and $T$ has a low path and a computably dominated path.
:::

:::proof{of=cor-bounded-pa}
$c([T])$ is a non-empty $\Pi^0_1$ class by :ref{#prop-finitely-branching-coding} and :ref{#lem-konig}. A PA set computes a member $c(P)$ of it (:ref{#thm-pa-characterization}), hence the path $P$. Similarly, the basis theorems give a member $c(P)$ that is low, or computably dominated, and $P \equiv_T c(P)$.
:::

:::quiz[coding into binary trees]
Why does the coding write each value in unary, rather than in binary with a fixed number of bits?

- [x] Because no bound on the values is known in general; unary coding needs none, and finite branching is what excludes the infinite block $1^\infty$.

  With a computable bound $g$, a binary coding with $\lceil \log_2 g(n) \rceil$ bits at position $n$ would also work.
- [ ] Because unary coding is computable and binary coding is not.

  Both are computable when the number of bits is known.
- [ ] To make the tree $S$ finitely branching.

  $S$ is a binary tree in any case.

---

Where is it used that $T$ is finitely branching, in :ref{#prop-finitely-branching-coding}?

- [x] To exclude paths of $S$ ending with infinitely many ones, which would correspond to no sequence of integers.
- [ ] To show that $S$ is c.e.

  The description of $S$ as a c.e. set does not use finite branching.
- [ ] To show that $c$ is injective.

  Injectivity of the coding holds for all sequences.
:::

## Unbounded branching

For a computably bounded tree, an algorithm knows in advance which values may occur at each position, and the binary coding below exploits this. Without a computable bound, the values of the successors of a node can carry information, such as the stage at which a number enters $\emptyset'$, and a path must then decode this information.

:::theorem{#thm-finitely-branching-jump}
There is a computable finitely branching tree $T$, in which every node has at most two successors, with exactly one path, and this path computes $\emptyset'$.
:::

:::proof{of=thm-finitely-branching-jump}
Let $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$, and for $n \in \emptyset'$ let $s_n$ be the least $s$ with $n \in \emptyset'_s$. Let $T$ be the set of sequences $\sigma$ such that for every $n < |\sigma|$, either $\sigma(n) = \langle 1, s \rangle$ where $s$ is the least stage with $n \in \emptyset'_s$, or $\sigma(n) = \langle 0, 0 \rangle$ and $n \notin \emptyset'_{|\sigma|}$.

$T$ is computable: each condition is decidable. It is closed under prefixes, since $n \notin \emptyset'_{|\sigma|}$ implies $n \notin \emptyset'_{|\tau|}$ for $\tau \preceq \sigma$. Each node has at most two successors, since at position $n$ only the values $\langle 0, 0 \rangle$ and $\langle 1, s_n \rangle$ are possible.

The sequence $P$ with $P(n) = \langle 1, s_n \rangle$ for $n \in \emptyset'$ and $P(n) = \langle 0, 0 \rangle$ for $n \notin \emptyset'$ is a path: every prefix satisfies the conditions. Conversely, let $Q$ be a path. If $Q(n) = \langle 1, s \rangle$, then $n \in \emptyset'$. If $Q(n) = \langle 0, 0 \rangle$, then $n \notin \emptyset'_\ell$ for every $\ell > n$, so $n \notin \emptyset'$. Hence $Q = P$, and $\emptyset'(n)$ is the first component of $P(n)$.
:::

:::figure[The beginning of the tree of :ref{#thm-finitely-branching-jump}, for an enumeration in which, among $0, \dots, 4$, only $1$ and $3$ enter $\emptyset'$, at stages $3$ and $6$. At a position $n \in \emptyset'$, the wrong guess $\langle 0, 0 \rangle$ survives until length $s_n$ and then has no extension; the unique path guesses correctly everywhere. Strings of integers are drawn as in a binary tree, each edge labeled by the value it adds.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="A computable tree with two successors at most per node and a single path, which computes the halting set"><line x1="200.0" y1="24" x2="200.0" y2="72" class="accent-stroke" stroke-width="2.2"/><text x="208.0" y="52.0" class="mrm" font-size="12">⟨0, 0⟩</text><line x1="200.0" y1="72" x2="130.0" y2="120" class="ink-stroke" stroke-width="1.2"/><text x="157.0" y="100.0" text-anchor="end" class="mrm" font-size="12">⟨0, 0⟩</text><line x1="200.0" y1="72" x2="270.0" y2="120" class="accent-stroke" stroke-width="2.2"/><text x="243.0" y="100.0" text-anchor="start" class="mrm" font-size="12">⟨1, 3⟩</text><line x1="270.0" y1="120" x2="270.0" y2="168" class="accent-stroke" stroke-width="2.2"/><text x="278.0" y="148.0" class="mrm" font-size="12">⟨0, 0⟩</text><line x1="270.0" y1="168" x2="200.0" y2="216" class="ink-stroke" stroke-width="1.2"/><text x="227.0" y="196.0" text-anchor="end" class="mrm" font-size="12">⟨0, 0⟩</text><line x1="270.0" y1="168" x2="340.0" y2="216" class="accent-stroke" stroke-width="2.2"/><text x="313.0" y="196.0" text-anchor="start" class="mrm" font-size="12">⟨1, 6⟩</text><line x1="200.0" y1="216" x2="200.0" y2="264" class="ink-stroke" stroke-width="1.2"/><line x1="340.0" y1="216" x2="340.0" y2="264" class="accent-stroke" stroke-width="2.2"/><text x="348.0" y="244.0" class="mrm" font-size="12">⟨0, 0⟩</text><circle cx="200.0" cy="24" r="4" class="accent-fill"/><circle cx="200.0" cy="72" r="4" class="accent-fill"/><circle cx="130.0" cy="120" r="4" class="ink-fill"/><line x1="123.0" y1="130" x2="137.0" y2="130" class="ink-stroke" stroke-width="1.4"/><text x="130.0" y="146" text-anchor="middle" class="label">no successor:</text><text x="130.0" y="160" text-anchor="middle" class="label">1 enters at stage 3</text><circle cx="270.0" cy="120" r="4" class="accent-fill"/><circle cx="270.0" cy="168" r="4" class="accent-fill"/><circle cx="200.0" cy="216" r="4" class="ink-fill"/><circle cx="340.0" cy="216" r="4" class="accent-fill"/><circle cx="200.0" cy="264" r="4" class="ink-fill"/><circle cx="340.0" cy="264" r="4" class="accent-fill"/><text x="200.0" y="284" text-anchor="middle" class="label">no successor at length 6:</text><text x="200.0" y="298" text-anchor="middle" class="label">3 enters at stage 6</text><text x="340.0" y="284" text-anchor="middle" class="mrm" font-size="12">⋮</text><text x="352.0" y="286" class="label">the path P</text><text x="210.0" y="20" class="mrm" font-size="13">ε</text><text x="470" y="52" class="label">position 0</text><text x="470" y="100" class="label">position 1 ∈ ∅′</text><text x="470" y="148" class="label">position 2</text><text x="470" y="196" class="label">position 3 ∈ ∅′</text><text x="470" y="244" class="label">position 4</text></svg>
:::

:::corollary{#cor-pa-not-enough}
There is a low PA set that computes no path through some infinite computable finitely branching tree.
:::

:::proof{of=cor-pa-not-enough}
A low set does not compute $\emptyset'$ (:ref{#prop-low-basic}). Take a low PA set (:ref{#cor-pa-basis}) and the tree of :ref{#thm-finitely-branching-jump}.
:::

The tree has as simple a shape as a binary tree: each node has at most two successors. What makes it harder is the lack of information about the successors: given a node, no algorithm bounds the values of its successors. The bound is computable in $\emptyset'$, which leads to the following characterization.

:::theorem{#thm-konig-strength}
A set $X$ computes a path through every infinite computable finitely branching tree if and only if $X$ is PA relative to $\emptyset'$ (:ref{#ex-pa-relative}).
:::

:::proof{of=thm-konig-strength}
($\Leftarrow$) Let $T$ be an infinite computable finitely branching tree. The binary tree $S$ of :ref{#prop-finitely-branching-coding} is c.e., hence computable in $\emptyset'$, and $[S] = c([T])$ is non-empty. So $[S]$ is a non-empty $\Pi^0_1(\emptyset')$ class, and $X$, being PA relative to $\emptyset'$, computes a member $c(P)$, by :ref{#thm-pa-characterization} relativized to $\emptyset'$. Then $X$ computes $P$.

($\Rightarrow$) By the same characterization relativized, it suffices to show that $X$ computes a member of every non-empty $\Pi^0_1(\emptyset')$ class $[U]$, with $U$ a binary tree computable in $\emptyset'$. By the limit lemma (:ref{#thm-limit-lemma}), $U$ has a $\Delta^0_2$ approximation $(U_s)$; replacing $U_s$ by the set of strings of length at most $s$ all of whose prefixes are in $U_s$, we may assume that each $U_s$ is a tree contained in $2^{\leq s}$, and it is still an approximation of $U$. Let $V = \bigcup_s U_s$.

*$[V] = [U]$.* Since $U \subseteq V$, $[U] \subseteq [V]$. Let $Y \in [V]$ and $m \in \nat$. For each $t \geq m$, $Y \uh t$ belongs to some $U_s$, with $s \geq t$ since $U_s \subseteq 2^{\leq s}$, and then $Y \uh m \in U_s$. So $Y \uh m \in U_s$ for infinitely many $s$, hence $Y \uh m \in U$, as $(U_s)$ converges.

*A finitely branching tree.* For $\sigma \in V$, let $f(\sigma)$ be the least $s$ with $\sigma \in U_s$. Let $T$ be the set of sequences $\langle \sigma(0), m_0 \rangle \cdots \langle \sigma(n-1), m_{n-1} \rangle$ such that, for every $i < n$, $m_i = f(\sigma \uh (i+1))$. $T$ is computable, since $m_i = f(\sigma \uh (i+1))$ is decided by testing $\sigma \uh (i+1) \in U_{m_i}$ and $\sigma \uh (i+1) \notin U_s$ for $s < m_i$. It is a tree, and each node has at most two successors, one for each bit. Its paths are the sequences $\langle Y(0), f(Y \uh 1) \rangle \langle Y(1), f(Y \uh 2) \rangle \cdots$ for $Y \in [V]$, and each such path computes $Y$ by reading the first components. It is infinite since $[V] = [U] \neq \emptyset$.

So $X$ computes a path through $T$, hence a member of $[U]$.
:::

So the computational strength of König's lemma for computable finitely branching trees is that of PA degrees relative to $\emptyset'$, while weak König's lemma, for binary trees, corresponds to the PA degrees. In reverse mathematics, this difference is the difference between the systems $\mathsf{ACA}_0$ and $\mathsf{WKL}_0$.

## Exercises

::::exercise{#ex-konig-double-jump difficulty=1 objective="Apply the characterization of König's lemma to bound the paths of computable finitely branching trees by $\emptyset''$."}
Show that every infinite computable finitely branching tree has a path computable in $\emptyset''$.

:::solution
$\emptyset''$ is PA relative to $\emptyset'$: the function $f(e) = 1$ if $\Phi^{\emptyset'}_e(e)\converge = 0$, and $f(e) = 0$ otherwise, is computable in $\emptyset''$ and is $\mathrm{DNC}_2$ relative to $\emptyset'$. Apply :ref{#thm-konig-strength}.
:::
::::

## Notes and references

König's lemma is due to Kőnig (1927). The coding of computably bounded trees into binary trees goes back to Jockusch and Soare (1972); Hirschfeldt, *Slicing the Truth*, Exercise 3.25, credits it to their two papers. :ref{#thm-finitely-branching-jump} is stated as a known result by Jockusch, Lewis and Remmel (1991), who also proved the direction ($\Rightarrow$) of :ref{#thm-konig-strength}, in the form of a computable finitely branching tree for every $\emptyset'$-computable binary tree, with the same degrees of paths; Hirschfeldt presents both as Exercises 3.24 and 3.27, and the direction ($\Leftarrow$) as a relativization of Exercise 3.25. The construction of :ref{#thm-finitely-branching-jump} is the computability-theoretic content of Simpson's Theorem III.7.2, which shows that König's lemma for trees in which each node has at most two successors implies arithmetical comprehension over $\mathsf{RCA}_0$; the tree used there codes the range of a one-to-one function in the same way. In reverse mathematics, König's lemma is equivalent to $\mathsf{ACA}_0$ (Simpson, Section III.7) and weak König's lemma defines $\mathsf{WKL}_0$ (Simpson, Chapter IV).

- D. Kőnig, *Über eine Schlussweise aus dem Endlichen ins Unendliche*, Acta Scientiarum Mathematicarum (Szeged) 3 (1927), 121–130.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- C. G. Jockusch, A. Lewis and J. B. Remmel, *Π⁰₁-classes and Rado's selection principle*, Journal of Symbolic Logic 56 (1991), 684–693.
- D. R. Hirschfeldt, *Slicing the Truth*, Lecture Notes Series of the Institute for Mathematical Sciences, National University of Singapore, 28, World Scientific, 2015, Section 3.2.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section III.7 and Chapter IV.

:::::exercises
::::exercise{#ex-pa-jump-computes-jump difficulty=2 objective="See in two ways that a set PA relative to $\emptyset'$ computes $\emptyset'$."}
Show that if $X$ is PA relative to $\emptyset'$, then $X$ computes $\emptyset'$.

:::solution
By :ref{#ex-pa-relative}, applied with $\emptyset'$ in place of $X$, a set that is PA relative to $\emptyset'$ computes $\emptyset'$. Alternatively, $X$ computes a path through the tree of :ref{#thm-finitely-branching-jump}, by :ref{#thm-konig-strength}, and this path computes $\emptyset'$.
:::
::::

::::exercise{#ex-konig-double-jump-direct difficulty=1 objective="Compute a path through a finitely branching tree from $\emptyset''$ by deciding extendibility, without PA degrees."}
Let $T$ be an infinite computable finitely branching tree. Show that the set of extendible nodes of $T$ (the nodes through which some path passes) is $\Pi^0_2$, and deduce directly that $T$ has a path computable in $\emptyset''$.

:::solution
A node $\sigma \in T$ is extendible if and only if for every $n \geq |\sigma|$, some node of $T$ of length $n$ extends $\sigma$. The condition is necessary, by considering the prefixes of a path through $\sigma$. Conversely, if it holds, the tree $T_\sigma = \{ \tau \in T : \tau \preceq \sigma \text{ or } \sigma \preceq \tau \}$ is infinite and finitely branching, so it has a path $P$ by :ref{#lem-konig}; the prefixes of $P$ of length at least $|\sigma|$ are in $T_\sigma$, so they extend $\sigma$, and $P$ goes through $\sigma$. For fixed $\sigma$ and $n$, "some node of length $n$ extends $\sigma$" is $\Sigma^0_1$, since $T$ is computable but the values of the nodes are not bounded; so extendibility is $\Pi^0_2$, and $\emptyset''$ decides it, by Post's theorem. Let $P(n)$ be the least $v$ such that $(P \uh n)\, v$ is extendible. If $P \uh n$ is extendible, a path through it goes through one of its successors, so $v$ exists, and it is found by a search with $\emptyset''$. By induction, every $P \uh n$ is extendible, hence in $T$, and $P \leq_T \emptyset''$ is a path.
:::
::::

::::exercise{#ex-bound-computes-jump difficulty=1 objective="See that every bound on the tree of the lesson whose path computes $\emptyset'$ computes $\emptyset'$ itself."}
Let $T$ be the tree of :ref{#thm-finitely-branching-jump}. Show that every function $g$ such that $\sigma(n) < g(n)$ for all $\sigma \in T$ and $n < |\sigma|$ computes $\emptyset'$. Deduce that $T$ is not computably bounded.

:::solution
Let $P$ be the path of $T$. For $n \in \emptyset'$, the node $P \uh (n+1)$ has $P(n) = \langle 1, s_n \rangle$, so $g(n) > \langle 1, s_n \rangle \geq s_n$, since the Cantor pairing satisfies $\langle x, y \rangle \geq y$. Hence $n \in \emptyset'$ if and only if $\Phi_n(n)[g(n)]\converge$: if $n \in \emptyset'$, the computation converges at stage $s_n < g(n)$, hence at stage $g(n)$; the converse is clear. So $\emptyset' \leq_T g$, and no computable $g$ bounds $T$. Such a function exists computably in $\emptyset'$, for instance $g(n) = \langle 1, s_n \rangle + 1$ for $n \in \emptyset'$ and $g(n) = 1$ otherwise, using $\langle 0, 0 \rangle = 0$.
:::
::::

::::exercise{#ex-ce-trees difficulty=2 objective="Show that the classes $\Pi^0_1$ relative to $\emptyset'$ are the classes of paths through c.e. trees, using the approximation of the proof of the lesson."}
Show that a class $\mathcal P \subseteq \cs$ is $\Pi^0_1$ relative to $\emptyset'$, that is, of the form $[U]$ with $U$ a binary tree computable in $\emptyset'$, if and only if $\mathcal P = [V]$ for some c.e. binary tree $V$. Deduce that $X$ is PA relative to $\emptyset'$ if and only if $X$ computes a path through every infinite c.e. binary tree.

:::solution
A c.e. tree is computable in $\emptyset'$, so its class of paths is $\Pi^0_1$ relative to $\emptyset'$. Conversely, let $U$ be a binary tree computable in $\emptyset'$, and let $(U_s)$ and $V = \bigcup_s U_s$ be as in the proof of :ref{#thm-konig-strength}: each $U_s$ is a tree contained in $2^{\leq s}$, and $(U_s)$ is a computable approximation of $U$. Then $V$ is c.e., as a union of uniformly computable sets, and a tree, as a union of trees; and $[V] = [U]$ was shown in that proof.

If $X$ is PA relative to $\emptyset'$ and $V$ is an infinite c.e. tree, then $[V]$ is non-empty by :ref{#lem-weak-konig}, and $\Pi^0_1$ relative to $\emptyset'$, so $X$ computes a member of it, by :ref{#thm-pa-characterization} relativized to $\emptyset'$. Conversely, suppose that $X$ computes a path through every infinite c.e. binary tree. Every non-empty $\Pi^0_1(\emptyset')$ class is $[V]$ for a c.e. tree $V$, which is infinite since it has a path; so $X$ computes a member of every non-empty $\Pi^0_1(\emptyset')$ class, in particular of the class of $\{0, 1\}$-valued functions DNC relative to $\emptyset'$ (:ref{#thm-dnc2-no-computable} relativized), and $X$ is PA relative to $\emptyset'$. The tree of :ref{#ex-prefix-closure-jump} is a c.e. tree whose only path is $\emptyset'$.
:::
::::

::::exercise{#ex-konig-cone-avoidance difficulty=2 objective="Relativize the coding of finitely branching trees and the cone avoidance basis theorem to $\emptyset'$."}
Let $T$ be an infinite computable finitely branching tree, and $C$ a set with $C \not\leq_T \emptyset'$. Show that $T$ has a path $P$ such that $C \not\leq_T \emptyset' \oplus P$. Deduce that $T$ has a path that does not compute $\emptyset''$.

:::solution
Relativized to a set $A$, :ref{#lem-uniform-cone} says that if $\Phi^{A \oplus Y}_e = C$ for every member $Y$ of a non-empty class $[U]$, with $U$ an $A$-computable tree, then $C \leq_T A$: the search of its proof is computable in $A$. The proof of :ref{#thm-cone-avoidance-basis} then gives, for $C \not\leq_T A$, a member $Y$ of every non-empty $\Pi^0_1(A)$ class with $C \not\leq_T A \oplus Y$.

Let $S$ be the c.e. binary tree of :ref{#prop-finitely-branching-coding}. It is computable in $\emptyset'$, and $[S] = \{ c(P) : P \in [T] \}$ is non-empty by :ref{#lem-konig}. Apply the relativized theorem with $A = \emptyset'$: there is $Y = c(P) \in [S]$ with $C \not\leq_T \emptyset' \oplus Y$. Since $P \equiv_T c(P)$, $\emptyset' \oplus P \equiv_T \emptyset' \oplus Y$, and $C \not\leq_T \emptyset' \oplus P$. With $C = \emptyset''$, which is not computable in $\emptyset'$, the path $P$ does not compute $\emptyset''$, since otherwise $\emptyset' \oplus P$ would. Compare :ref{#thm-finitely-branching-jump}: a computable finitely branching tree can force all its paths to compute $\emptyset'$, but no set $C \not\leq_T \emptyset'$ is computable from $\emptyset' \oplus P$ for every path $P$. Adapted from Hirschfeldt, *Slicing the Truth*, Exercise 3.26.
:::
::::

::::exercise{#ex-konig-finitely-many-paths difficulty=2 objective="Relativize the computability of isolated members to $\emptyset'$ through the coding of finitely branching trees."}
Let $T$ be a computable finitely branching tree with finitely many paths. Show that each path of $T$ is computable in $\emptyset'$, and that $\emptyset'$ cannot be replaced by $\emptyset$.

:::solution
Let $S$ be the c.e. binary tree of :ref{#prop-finitely-branching-coding}, computable in $\emptyset'$. Its class of paths $\{ c(P) : P \in [T] \}$ is finite, since $c$ is injective. Relativized to $\emptyset'$, :ref{#prop-isolated-computable} and :ref{#cor-countable-computable} say that every member of a finite $\Pi^0_1(\emptyset')$ class is computable in $\emptyset'$: the proofs only use that non-extendibility in an $A$-computable tree is $\Sigma^0_1$ relative to $A$. So each $c(P)$, and hence each $P$, is computable in $\emptyset'$. The tree of :ref{#thm-finitely-branching-jump} has a single path, which computes $\emptyset'$, so it is not computable. Hirschfeldt, *Slicing the Truth*, Section 3.2, states this after Exercise 3.28.
:::
::::
:::::
