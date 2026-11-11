---
title: Ramsey's theorem in the arithmetic hierarchy
summary: Ramsey's theorem for n-tuples; pre-homogeneous sets and the Erdős–Radó tree; every coloring of n-tuples has a homogeneous set computable in any degree PA over its (n−1)-st jump; a computable coloring of pairs without Δ⁰₂ homogeneous set; Ramsey's theorem for triples is equivalent to ACA₀.
duration: 45
prerequisites: [big-five/wkl0]
---

Ramsey's theorem states that every finite coloring of the $n$-element subsets of $\nat$ has an infinite set on which the coloring is constant. Jockusch (1972) determined how complex such sets must be for computable colorings: homogeneous sets can be found computably in any degree PA over $\obf^{(n-1)}$, but not, in general and for $n \geq 2$, at the level $\Sigma^0_n$. For $n \geq 3$, this makes Ramsey's theorem equivalent to $\mathsf{ACA}_0$. For pairs, the analysis leaves a gap, which the rest of the course explores.

## Statements

For a set $X$ and $n \geq 1$, $[X]^n$ is the set of $n$-element subsets of $X$, identified with increasing tuples $x_1 < \cdots < x_n$. A **$k$-coloring** of $[X]^n$ is a function $f : [X]^n \to k = \{ 0, \dots, k-1 \}$. A set $H \subseteq X$ is **homogeneous** for $f$ if $f$ is constant on $[H]^n$.

:::definition{#def-rt}
$\mathsf{RT}^n_k$ is the statement: every coloring $f : [\nat]^n \to k$ has an infinite homogeneous set.
:::

In reverse mathematics, colorings and homogeneous sets are sets, and $\mathsf{RT}^n_k$ is a $\Pi^1_2$ statement. In computability theory, one asks how complex homogeneous sets must be relative to $f$. The case $n = 1$ is the **infinite pigeonhole principle**.

:::proposition{#prop-rt-basic}
1. $\mathsf{RCA}_0$ proves $\mathsf{RT}^1_k$ for every standard $k$.
2. Over $\mathsf{RCA}_0$, $\mathsf{RT}^n_2$ implies its version for colorings of $[X]^n$, for every infinite set $X$.
3. For every standard $n \geq 1$ and $k \geq 2$, $\mathsf{RCA}_0$ proves $\mathsf{RT}^n_2 \rightarrow \mathsf{RT}^n_k$.
:::

:::proof{of=prop-rt-basic}
1. For $f : \nat \to k$, the sets $C_i = \{ x : f(x) = i \}$ exist. If all were finite, bounded by $b_i$, then $\max_i b_i$ would bound $\nat$. So some $C_i$ is infinite, and it is homogeneous.
2. Let $p$ enumerate $X$ in increasing order; it exists in $\mathsf{RCA}_0$ when $X$ is infinite. Apply $\mathsf{RT}^n_2$ to $g(\{ x_1, \dots, x_n \}) = f(\{ p(x_1), \dots, p(x_n) \})$, and take the image of a homogeneous set under $p$.
3. By induction on $k$ in the metatheory. Given $f : [\nat]^n \to k + 1$, merge the colors $k - 1$ and $k$, and apply $\mathsf{RT}^n_k$ to obtain an infinite $H$. If its color is less than $k - 1$, $H$ is homogeneous for $f$; otherwise $f$ takes only the values $k - 1$ and $k$ on $[H]^n$, and (2) gives a homogeneous subset.
:::

The number of colors is irrelevant for provability, as long as it is a fixed standard number; we focus on two colors.

## Pre-homogeneous sets and the upper bound

A coloring of $(n+1)$-tuples reduces to a coloring of $n$-tuples on a well-chosen set.

:::definition{#def-pre-homogeneous}
A set $X$ is **pre-homogeneous** for $f : [\nat]^{n+1} \to k$ if, for all $x_1 < \cdots < x_n$ in $X$, the color $f(\{ x_1, \dots, x_n, y \})$ is the same for all $y \in X$ with $y > x_n$.
:::

On an infinite pre-homogeneous set $X$, the coloring $g(\{ x_1, \dots, x_n \}) = f(\{ x_1, \dots, x_n, y \})$, for any $y \in X$ above $x_n$, is well defined and computable in $f \oplus X$, and every set $H \subseteq X$ homogeneous for $g$ is homogeneous for $f$.

:::proposition[Erdős, Radó]{#prop-erdos-rado-tree}
For every coloring $f : [\nat]^{n+1} \to k$, there is an infinite, finitely branching, $f$-computable tree $T \subseteq \nat^{<\nat}$ of strictly increasing sequences whose infinite paths are pre-homogeneous for $f$. Every set PA relative to $f'$ computes an infinite pre-homogeneous set for $f$.
:::

:::proof{of=prop-erdos-rado-tree}
We build $T$ by inserting the numbers $0, 1, 2, \dots$ one at a time. The first $n$ numbers form a single branch $\langle 0, 1, \dots, n - 1 \rangle$. To insert $s \geq n$, start at this branch and descend: at a node $\sigma$, call **pattern** of a number $a$ over $\sigma$ the tuple of colors $f(\{ \sigma(m_1), \dots, \sigma(m_n), a \})$ for $m_1 < \cdots < m_n < |\sigma|$. If $\sigma$ has an immediate successor $\sigma\, a$ in the current tree such that $a$ and $s$ have the same pattern over $\sigma$, move to $\sigma\, a$; otherwise add $\sigma\, s$ to the tree and stop.

*$T$ is $f$-computable and infinite.* To decide whether a sequence $\sigma\, s$ belongs to $T$, simulate the insertion of $0, \dots, s$. Every number is inserted, so $T$ is infinite.

*$T$ is finitely branching.* Two immediate successors $\sigma a$ and $\sigma b$ of a node, with $a < b$, have different patterns over $\sigma$: otherwise $b$ would have moved to $\sigma a$ instead of creating $\sigma b$. So $\sigma$ has at most $k^{\binom{|\sigma|}{n}}$ successors.

*Paths are pre-homogeneous.* Let $P$ be an infinite path, $j < j'$, $a = P(j)$ and $b = P(j')$. When $b$ was inserted, it descended along $P \uh j'$, hence moved from $P \uh j$ to $P \uh (j + 1) = (P \uh j)\, a$, so $a$ and $b$ have the same pattern over $P \uh j$. For $x_1 < \cdots < x_n$ in the range of $P$, at positions $m_1 < \cdots < m_n$, and $y = P(j)$, $y' = P(j')$ with $m_n < j < j'$, this gives $f(\{ x_1, \dots, x_n, y \}) = f(\{ x_1, \dots, x_n, y' \})$.

*Computing a path.* The number of successors of each node is bounded, but their values are not: whether $\sigma$ has a successor above a given number is a $\Sigma^0_1(f)$ question. With $f'$, one computes, for each node, the finite list of its successors. Coding each successor by its rank in this list, the paths of $T$ correspond, computably in $f'$, to the paths of an $f'$-computable tree in $\prod_\sigma k^{\binom{|\sigma|}{n}}$, a $\Pi^0_1(f')$ class after coding into Cantor space. It is non-empty by König's lemma. A set PA relative to $f'$ computes a member of it (:ref{#thm-pa-characterization}, relativized), and it computes $f'$ itself (second exercise of :ref{to="pi01-classes/pa-degrees"}, relativized to $f'$), so it computes a path of $T$.
:::

:::theorem[Jockusch]{#thm-jockusch-upper}
For every $n \geq 1$, every coloring $f : [\nat]^n \to k$ has an infinite homogeneous set computable in every set that is PA relative to $f^{(n-1)}$. In particular, every computable coloring of $[\nat]^n$ has an infinite homogeneous set computable in $\emptyset^{(n)}$.
:::

:::proof{of=thm-jockusch-upper}
By induction on $n$, for all colorings $f$ simultaneously. For $n = 1$, $f$ itself computes a homogeneous set, and a set PA relative to $f$ computes $f$.

For $n = 2$, let $P$ be PA relative to $f'$. By :ref{#prop-erdos-rado-tree}, $P$ computes an infinite pre-homogeneous set $X$, the induced coloring $g$ of $[X]^1$ is computable in $P$, and so is a homogeneous set for $g$, which is homogeneous for $f$.

For $n + 1$ with $n \geq 2$, let $P_1$ be PA relative to $f^{(n)}$. By the low basis theorem relativized to $f'$, there is $P_0$ PA relative to $f'$ with $P_0' \leq_T f''$; then $P_0^{(n-1)} \leq_T f^{(n)}$, since $n - 1 \geq 1$. $P_0$ computes an infinite pre-homogeneous set $X$ and the induced coloring $g$ of $[X]^n$, so $g^{(n-1)} \leq_T P_0^{(n-1)} \leq_T f^{(n)}$, and $P_1$ is PA relative to $g^{(n-1)}$. By the induction hypothesis, applied to $g$ transported to $[\nat]^n$ through the enumeration of $X$, $P_1$ computes an infinite homogeneous set for the transported coloring; its image under the enumeration of $X$ is computable in $P_1$, since $X \leq_T P_0 \leq_T f'' \leq_T P_1$, and it is homogeneous for $g$, hence for $f$.

For the last statement, $\emptyset^{(n)}$ is PA relative to $\emptyset^{(n-1)}$: it computes a $\{0, 1\}$-valued function DNC relative to $\emptyset^{(n-1)}$.
:::

Jockusch proved more precisely that every computable coloring of $[\nat]^n$ has a $\Pi^0_n$ infinite homogeneous set. For pairs, one builds an infinite pre-homogeneous sequence and the set of its elements of a given limit color so that both are $\Pi^0_2$; we do not reproduce the construction (Jockusch 1972; Hirschfeldt, *Slicing the Truth*, Chapter 6).

:::quiz[the Erdős–Radó tree]
In the proof of :ref{#prop-erdos-rado-tree}, why is $f'$ needed to compute a path, although the tree is $f$-computable and finitely branching?

- [x] Because the number of successors of a node is bounded, but not their values: deciding whether a node has a successor above a given number is a $\Sigma^0_1(f)$ question, and $f'$ is needed to list the successors.
- [ ] Because the tree is not $f$-computable.

  Membership in the tree is decided by simulating the insertion process.
- [ ] Because pre-homogeneity is a $\Pi^0_2$ property.

  Every path is pre-homogeneous; the issue is to find a path.

---

In the proof of :ref{#thm-jockusch-upper}, why is the case $n = 2$ treated separately?

- [x] Because the inequality $P_0^{(n-1)} \leq_T f^{(n)}$ obtained from $P_0' \leq_T f''$ requires $n - 1 \geq 1$; for pairs, a single set PA relative to $f'$ computes both the pre-homogeneous set and the homogeneous set.
- [ ] Because $\mathsf{RT}^2_2$ is not provable in $\mathsf{ACA}_0$.

  It is provable in $\mathsf{ACA}_0$; the case distinction concerns the jump inequalities.
- [ ] Because the Erdős–Radó tree does not exist for pairs.

  It exists for every $n$.
:::

## The lower bound

:::theorem[Jockusch]{#thm-jockusch-no-delta2}
There is a computable coloring $f : [\nat]^2 \to 2$ with no infinite $\Delta^0_2$ homogeneous set, hence no infinite $\Sigma^0_2$ homogeneous set.
:::

:::proof{of=thm-jockusch-no-delta2}
For each $e$ and $s$, let $A_{e,s} = \{ x < s : \Phi^{\emptyset'_s}_e(x)[s]\converge = 1 \}$, where $\emptyset'_s$ is the stage $s$ approximation of $\emptyset'$. If $\Phi^{\emptyset'}_e$ is the characteristic function of a set $A$, then for every $x$, $x \in A_{e,s}$ for all large $s$ if $x \in A$, and $x \notin A_{e,s}$ for all large $s$ otherwise. Every $\Delta^0_2$ set is of this form, by the limit lemma.

Define $f(\{ x, s \})$ for $x < s$ at stage $s$: for $e = 0, 1, \dots, s - 1$ in turn, if $A_{e,s}$ has at least $2e + 2$ elements, choose the two least elements $a < b$ of $A_{e,s}$ for which $f(\{ a, s \})$ and $f(\{ b, s \})$ are not yet defined, and set $f(\{ a, s \}) = 0$ and $f(\{ b, s \}) = 1$. Before $e$ acts, at most $2e$ values $f(\{ x, s \})$ have been defined, so the two elements exist. All remaining values $f(\{ x, s \})$ are set to $0$. The coloring is computable.

Let $A = \Phi^{\emptyset'}_e$ be an infinite $\Delta^0_2$ set, and $n$ such that $A \cap \{0, \dots, n-1\}$ has exactly $2e + 2$ elements. For large enough $s \in A$, $A_{e,s} \cap \{0, \dots, n-1\} = A \cap \{0, \dots, n-1\}$. At stage $s$, the $2e + 2$ least elements of $A_{e,s}$ are those of $A$ below $n$, and $e$ chooses two of them, $a$ and $b$, with $f(\{ a, s \}) \neq f(\{ b, s \})$. Since $a, b, s \in A$, $A$ is not homogeneous.

Finally, every infinite $\Sigma^0_2$ set $B = \{ x : \exists y\, \forall z\, R(x, y, z) \}$, with $R$ computable, has an infinite $\Delta^0_2$ subset: with $\emptyset'$, search for pairs $(x, y)$ with $\forall z\, R(x, y, z)$, and keep an increasing sequence of the first coordinates found. A subset of a homogeneous set is homogeneous.
:::

The two bounds leave a gap at pairs: homogeneous sets for computable colorings can always be found below $\emptyset''$, and sometimes not below $\emptyset'$. What computational power is necessarily carried by every homogeneous set is the subject of the next two lessons.

:::quiz[the lower bound]
In the proof of :ref{#thm-jockusch-no-delta2}, why does the requirement for $e$ wait until $A_{e,s}$ has at least $2e + 2$ elements?

- [x] Because the requirements $e' < e$ may already have used up to $2e$ elements at stage $s$; with $2e + 2$ elements, two remain available for $e$.
- [ ] Because $A$ must have at least $2e + 2$ elements to be infinite.

  An infinite set has arbitrarily many elements; the bound is about sharing the stage $s$ among requirements.
- [ ] To ensure that $f$ is computable.

  $f$ is computable whatever the threshold; the threshold guarantees that two fresh elements exist.
:::

## Coding the jump into triples

The upper bound for triples is not only a bound on complexity: some computable colorings of triples force all their homogeneous sets to compute $\emptyset'$.

:::lemma{#lem-limit-coloring}
For every $\emptyset'$-computable coloring $h : [\nat]^n \to k$, there is a computable coloring $f : [\nat]^{n+1} \to k$ such that every infinite homogeneous set for $f$ is homogeneous for $h$.
:::

:::proof{of=lem-limit-coloring}
By the limit lemma, $h(\{ x_1, \dots, x_n \}) = \lim_t f(\{ x_1, \dots, x_n, t \})$ for a computable function $f$ defined for $x_1 < \cdots < x_n < t$; replacing the values outside $k$ by $0$, which does not change the limit, $f$ is a coloring $[\nat]^{n+1} \to k$. Let $H$ be infinite and homogeneous for $f$ with color $i$. For $x_1 < \cdots < x_n$ in $H$, take $t \in H$ large enough that $f(\{ x_1, \dots, x_n, t \}) = h(\{ x_1, \dots, x_n \})$; this value is $i$.
:::

:::proposition[Jockusch]{#prop-rt32-jump}
There is a computable coloring of $[\nat]^3$ with two colors all of whose infinite homogeneous sets compute $\emptyset'$.
:::

:::proof{of=prop-rt32-jump}
Let $m(x)$ be the least $s$ with $\emptyset'_s \cap \{0, \dots, x - 1\} = \emptyset' \cap \{0, \dots, x - 1\}$, a $\emptyset'$-computable function. Let $h(\{ x, y \}) = 1$ if $m(x) < y$ and $0$ otherwise, for $x < y$. An infinite homogeneous set $H$ for $h$ has color $1$: color $0$ would give $m(x) \geq y$ for all $y > x$ in $H$. So for consecutive elements $x < y$ of $H$, $\emptyset' \cap \{0, \dots, x-1\} = \emptyset'_y \cap \{0, \dots, x-1\}$, and $H$ computes $\emptyset'$. Apply :ref{#lem-limit-coloring}.
:::

## Reverse mathematics

:::theorem[Jockusch, Simpson]{#thm-rt3-aca}
For every standard $n \geq 3$, $\mathsf{RT}^n_2$ is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$. Moreover $\mathsf{ACA}_0$ proves $\mathsf{RT}^n_k$ for all standard $n$ and $k$.
:::

:::proof{of=thm-rt3-aca}
*$\mathsf{ACA}_0$ proves $\mathsf{RT}^n_k$*, by induction on $n$ in the metatheory. The case $n = 1$ is :ref{#prop-rt-basic}. Given $f : [\nat]^{n+1} \to k$, the Erdős–Radó tree exists by $\Delta^0_1$ comprehension, and $\mathsf{RCA}_0$ proves that it is infinite and finitely branching. By König's lemma (:ref{#thm-konig-aca}), it has a path, which is pre-homogeneous. The induction hypothesis, with :ref{#prop-rt-basic} (2), whose proof applies to any number of colors, gives a homogeneous set for the induced coloring.

*$\mathsf{RT}^3_2$ implies $\mathsf{ACA}_0$.* We prove that $X'$ exists, using :ref{#thm-aca-equivalents}. Define $f(\{ x, s, t \}) = 1$ for $x < s < t$ if every $e < x$ satisfies $\Phi^X_e(e)[s]\converge \leftrightarrow \Phi^X_e(e)[t]\converge$, and $0$ otherwise. Let $H$ be infinite and homogeneous. Its color is $1$: for $x \in H$, among $2^x + 1$ elements of $H$ above $x$, two have the same pattern of convergence for the indices $e < x$, by the finite pigeonhole principle, provable in $\mathsf{RCA}_0$. For each $e$, let $x_e$ be the least element of $H$ above $e$ and $s_e$ the least element of $H$ above $x_e$. If $\Phi^X_e(e)[t_0]\converge$ for some $t_0$, take $t \in H$ above $s_e$ and $t_0$, so that $\Phi^X_e(e)[t]\converge$; then $f(\{ x_e, s_e, t \}) = 1$ gives $\Phi^X_e(e)[s_e]\converge$. So $X' = \{ e : \Phi^X_e(e)[s_e]\converge \}$, which exists by $\Delta^0_1$ comprehension relative to $X \oplus H$.

For $n \geq 3$, $\mathsf{RT}^n_2$ implies $\mathsf{RT}^3_2$: a coloring $f$ of triples induces the coloring $\{ x_1, \dots, x_n \} \mapsto f(\{ x_1, x_2, x_3 \})$ of $n$-tuples, with the same infinite homogeneous sets.
:::

:::corollary{#cor-wkl-not-rt22}
$\mathsf{WKL}_0$ does not prove $\mathsf{RT}^2_2$.
:::

:::proof{of=cor-wkl-not-rt22}
By :ref{#thm-low-scott}, there is an ω-model of $\mathsf{WKL}_0$ consisting of low sets, hence of $\Delta^0_2$ sets. The computable coloring of :ref{#thm-jockusch-no-delta2} belongs to it and has no homogeneous set in it.
:::

The coloring of :ref{#prop-rt32-jump} has no analogue for pairs: by Seetapun's theorem, proved in the last lesson, every computable coloring of pairs has an infinite homogeneous set that does not compute $\emptyset'$.

:::quiz[RT³₂ and ACA₀]
In the proof of :ref{#thm-rt3-aca}, why must an infinite homogeneous set for $f$ have color $1$?

- [x] Because for each $x \in H$, the convergence patterns at stages in $H$ take at most $2^x$ values, so two stages $s < t$ in $H$ above $x$ share a pattern, and $f(\{ x, s, t \}) = 1$.
- [ ] Because $X'$ is infinite.

  The argument does not depend on $X'$; it is a counting argument on patterns.
- [ ] Because $f$ takes the value $1$ on infinitely many triples.

  Many colorings take both values infinitely often; homogeneity of $H$ together with the counting argument fixes the color.
:::

## Exercises

::::exercise{difficulty=1}
Show that for every $n \geq 2$ there is a computable coloring $f : [\nat]^n \to 2$ with no infinite $\Sigma^0_n$ homogeneous set.

:::solution
By induction on $n$, relativized to an arbitrary oracle $Z$: there is a $Z$-computable coloring of $[\nat]^n$ with no infinite $\Sigma^0_n(Z)$ homogeneous set. For $n = 2$, this is :ref{#thm-jockusch-no-delta2} relativized. Given the statement for $n$ and every oracle, apply it to $Z'$: there is a $Z'$-computable coloring $h$ of $[\nat]^n$ with no infinite $\Sigma^0_n(Z')$, that is $\Sigma^0_{n+1}(Z)$, homogeneous set. By :ref{#lem-limit-coloring} relativized to $Z$, there is a $Z$-computable coloring of $[\nat]^{n+1}$ whose infinite homogeneous sets are homogeneous for $h$.
:::
::::

::::exercise{difficulty=1}
Show that every computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ with $H' \leq_T \emptyset''$.

:::solution
By the low basis theorem relativized to $\emptyset'$, there is a set $P$ PA relative to $\emptyset'$ with $P' \leq_T \emptyset''$. By :ref{#thm-jockusch-upper}, $P$ computes an infinite homogeneous set $H$, and $H' \leq_T P' \leq_T \emptyset''$.
:::
::::

## Notes and references

Ramsey (1930) proved his theorem as a lemma in a decision procedure for a fragment of first-order logic. Specker (1971) built a computable coloring of pairs without computable infinite homogeneous set, and Jockusch (1972) obtained the bounds of this lesson. Simpson formalized the equivalence with $\mathsf{ACA}_0$. Hirschfeldt's book is the standard reference for the reverse mathematics of combinatorial principles.

- C. G. Jockusch, Jr., *Ramsey's theorem and recursion theory*, Journal of Symbolic Logic 37 (1972), 268–280.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
