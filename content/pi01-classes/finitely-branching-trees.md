---
title: Finitely branching trees
summary: Trees of sequences of integers; König's lemma; computably bounded trees behave like binary trees; a computable finitely branching tree whose paths all compute ∅′; the strength needed for König's lemma.
duration: 35
prerequisites: [pa-degrees]
---

Binary trees model problems with two choices at each step. Many problems have more: a coloring of a graph with $k$ colors, a function bounded by a known bound, or a sequence of integers with no a priori bound at all. This lesson considers trees of finite sequences of integers. When the branching is bounded by a computable function, nothing changes: the paths of such a tree are, up to a computable coding, the members of a $\Pi^0_1$ class. When the branching is finite but not computably bounded, König's lemma still guarantees a path, but finding one may require computing the halting set.

## Trees of integers

Write $\nat^{<\nat}$ for the set of finite sequences of integers, with the same notation as for binary strings, and $\nat^\nat$ for **Baire space**, the set of infinite sequences of integers. A **tree** is a subset $T \subseteq \nat^{<\nat}$ closed under prefixes, and a **path** through $T$ is a sequence $P \in \nat^\nat$ all of whose prefixes belong to $T$. A tree is **finitely branching** if every node $\sigma \in T$ has finitely many immediate successors $\sigma v \in T$. It is **computably bounded** if there is a computable function $g$ with $\sigma(n) < g(n)$ for every $\sigma \in T$ and $n < |\sigma|$.

:::lemma[König's lemma]{#lem-konig}
Every infinite finitely branching tree has a path.
:::

:::proof{of=lem-konig}
Call a node **large** if infinitely many nodes of $T$ extend it. The root is large. If $\sigma$ is large, then since the nodes extending $\sigma$, other than $\sigma$, extend one of its finitely many successors, one successor is large. Define $P(n)$ as the least $v$ such that $(P \uh n)\, v$ is large. By induction every prefix of $P$ is large, hence in $T$.
:::

The hypothesis of finite branching is necessary: the tree $\{ \sigma : \sigma(i) \geq |\sigma| \text{ for all } i < |\sigma| \}$ is infinite and has no path (see :ref{#lem-weak-konig}).

## Coding into binary trees

We code a sequence of integers by a binary sequence, writing each value in unary followed by a separator:
$$
c(\sigma) = 1^{\sigma(0)}\, 0\, 1^{\sigma(1)}\, 0 \cdots 1^{\sigma(n-1)}\, 0, \qquad c(P) = 1^{P(0)}\, 0\, 1^{P(1)}\, 0 \cdots
$$
The map $c$ is a computable bijection from $\nat^\nat$ onto the sequences with infinitely many zeros, and $P \equiv_T c(P)$, uniformly (see :ref{#prop-baire-cantor}).

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

:::theorem{#thm-finitely-branching-jump}
There is a computable finitely branching tree $T$, in which every node has at most two successors, with exactly one path, and this path computes $\emptyset'$.
:::

:::proof{of=thm-finitely-branching-jump}
Let $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$, and for $n \in \emptyset'$ let $s_n$ be the least $s$ with $n \in \emptyset'_s$. Let $T$ be the set of sequences $\sigma$ such that for every $n < |\sigma|$, either $\sigma(n) = \langle 1, s \rangle$ where $s$ is the least stage with $n \in \emptyset'_s$, or $\sigma(n) = \langle 0, 0 \rangle$ and $n \notin \emptyset'_{|\sigma|}$.

$T$ is computable: each condition is decidable. It is closed under prefixes, since $n \notin \emptyset'_{|\sigma|}$ implies $n \notin \emptyset'_{|\tau|}$ for $\tau \preceq \sigma$. Each node has at most two successors, since at position $n$ only the values $\langle 0, 0 \rangle$ and $\langle 1, s_n \rangle$ are possible.

The sequence $P$ with $P(n) = \langle 1, s_n \rangle$ for $n \in \emptyset'$ and $P(n) = \langle 0, 0 \rangle$ for $n \notin \emptyset'$ is a path: every prefix satisfies the conditions. Conversely, let $Q$ be a path. If $Q(n) = \langle 1, s \rangle$, then $n \in \emptyset'$. If $Q(n) = \langle 0, 0 \rangle$, then $n \notin \emptyset'_\ell$ for every $\ell > n$, so $n \notin \emptyset'$. Hence $Q = P$, and $\emptyset'(n)$ is the first component of $P(n)$.
:::

:::corollary{#cor-pa-not-enough}
There is a low PA set that computes no path through some infinite computable finitely branching tree.
:::

:::proof{of=cor-pa-not-enough}
A low set does not compute $\emptyset'$ (:ref{#prop-low-basic}). Take a low PA set (:ref{#cor-pa-basis}) and the tree of :ref{#thm-finitely-branching-jump}.
:::

The tree has as simple a shape as a binary tree: each node has at most two successors. What makes it harder is the lack of information about the successors: given a node, no algorithm bounds the values of its successors. The bound is computable in $\emptyset'$, which leads to the following characterization.

:::theorem{#thm-konig-strength}
A set $X$ computes a path through every infinite computable finitely branching tree if and only if $X$ is PA relative to $\emptyset'$.
:::

:::proof{of=thm-konig-strength}
($\Leftarrow$) Let $T$ be an infinite computable finitely branching tree. The binary tree $S$ of :ref{#prop-finitely-branching-coding} is c.e., hence computable in $\emptyset'$, and $[S] = c([T])$ is non-empty. So $[S]$ is a non-empty $\Pi^0_1(\emptyset')$ class, and $X$, being PA relative to $\emptyset'$, computes a member $c(P)$, by :ref{#thm-pa-characterization} relativized to $\emptyset'$. Then $X$ computes $P$.

($\Rightarrow$) By the same characterization relativized, it suffices to show that $X$ computes a member of every non-empty $\Pi^0_1(\emptyset')$ class $[U]$, with $U$ a binary tree computable in $\emptyset'$. By the limit lemma, $U$ has a $\Delta^0_2$ approximation $(U_s)$; replacing $U_s$ by the set of strings of length at most $s$ all of whose prefixes are in $U_s$, we may assume that each $U_s$ is a tree contained in $2^{\leq s}$, and it is still an approximation of $U$. Let $V = \bigcup_s U_s$.

*$[V] = [U]$.* Since $U \subseteq V$, $[U] \subseteq [V]$. Let $Y \in [V]$ and $m \in \nat$. For each $t \geq m$, $Y \uh t$ belongs to some $U_s$, with $s \geq t$ since $U_s \subseteq 2^{\leq s}$, and then $Y \uh m \in U_s$. So $Y \uh m \in U_s$ for infinitely many $s$, hence $Y \uh m \in U$, as $(U_s)$ converges.

*A finitely branching tree.* For $\sigma \in V$, let $f(\sigma)$ be the least $s$ with $\sigma \in U_s$. Let $T$ be the set of sequences $\langle \sigma(0), m_0 \rangle \cdots \langle \sigma(n-1), m_{n-1} \rangle$ such that, for every $i < n$, $m_i = f(\sigma \uh (i+1))$. $T$ is computable, since $m_i = f(\sigma \uh (i+1))$ is decided by testing $\sigma \uh (i+1) \in U_{m_i}$ and $\sigma \uh (i+1) \notin U_s$ for $s < m_i$. It is a tree, and each node has at most two successors, one for each bit. Its paths are the sequences $\langle Y(0), f(Y \uh 1) \rangle \langle Y(1), f(Y \uh 2) \rangle \cdots$ for $Y \in [V]$, and each such path computes $Y$ by reading the first components. It is infinite since $[V] = [U] \neq \emptyset$.

So $X$ computes a path through $T$, hence a member of $[U]$.
:::

So the computational strength of König's lemma for computable finitely branching trees is that of PA degrees relative to $\emptyset'$, while weak König's lemma, for binary trees, corresponds to the PA degrees. In reverse mathematics, this difference is the difference between the systems $\mathsf{ACA}_0$ and $\mathsf{WKL}_0$.

## Exercises

::::exercise{difficulty=1}
Show that every infinite computable finitely branching tree has a path computable in $\emptyset''$.

:::solution
$\emptyset''$ is PA relative to $\emptyset'$: the function $f(e) = 1$ if $\Phi^{\emptyset'}_e(e)\converge = 0$, and $f(e) = 0$ otherwise, is computable in $\emptyset''$ and is $\mathrm{DNC}_2$ relative to $\emptyset'$. Apply :ref{#thm-konig-strength}.
:::
::::

::::exercise{difficulty=2}
Show that if $X$ is PA relative to $\emptyset'$, then $X$ computes $\emptyset'$.

:::solution
By the second exercise of :ref{to="pi01-classes/pa-degrees"} relativized to $\emptyset'$, a set that is PA relative to $\emptyset'$ computes $\emptyset'$. Alternatively, $X$ computes a path through the tree of :ref{#thm-finitely-branching-jump}, by :ref{#thm-konig-strength}, and this path computes $\emptyset'$.
:::
::::

## Notes and references

König's lemma is due to Kőnig (1927). The coding of computably bounded trees and the analysis of finitely branching trees are standard; Jockusch and Soare (1972) and Simpson's book on reverse mathematics treat these questions, the latter in the setting of second-order arithmetic.

- D. Kőnig, *Über eine Schlussweise aus dem Endlichen ins Unendliche*, Acta Scientiarum Mathematicarum (Szeged) 3 (1927), 121–130.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009.
