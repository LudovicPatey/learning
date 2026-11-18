---
title: Intrinsic versus relatively intrinsic
summary: Relations that are c.e. in every computable copy (intrinsically c.e.) versus every copy (relatively intrinsically c.e.); the successor relation on ω is not intrinsically c.e., by a direct construction; the Ash–Nerode theorem, by which the two notions agree under a decidability condition, and Manasse's examples showing that the condition is needed; on an infinite-dimensional vector space, the intrinsically computable unary relations are the finite and cofinite ones.
duration: 25
prerequisites: [intrinsic-relations]
---

The definition of r.i.c.e. relations quantifies over all copies of a structure, computable or not. A more naive definition looks only at the computable copies. The two differ, and the difference is a recurring theme: the same distinction appears for categoricity in the next course. This lesson defines the naive notion, shows on an example how to defeat it by building a computable copy, states the theorem of Ash and Nerode that the two notions coincide under a decidability condition, and applies it to vector spaces.

:::definition{#def-intrinsically-ce}
Let $\mathcal A$ be a computable structure and $R$ a relation on it. $R$ is **intrinsically c.e.** if $R^{\mathcal B}$ is c.e. for every computable copy $(\mathcal B, R^{\mathcal B})$ of $(\mathcal A, R)$, and **intrinsically computable** if $R^{\mathcal B}$ is computable for every computable copy.
:::

Every r.i.c.e. relation is intrinsically c.e., since for a computable copy, c.e. in $D(\mathcal B)$ means c.e. By :ref{#thm-akms-chisholm-1}, so is every relation that is $\Sigma^c_1$-definable with parameters; such relations are also called **formally c.e.**

## A relation that is not intrinsically c.e.

On the order $\omega = (\nat; \leq)$, the complement of the successor relation $S$ is r.i.c.e.: $x$ and $y$ are not successive if $y \leq x$ or some $z$ lies between them. The relation $S$ itself is not even intrinsically c.e.

:::proposition{#prop-successor-not-ice}
There is a computable copy of $\omega$ in which the successor relation is not c.e.
:::

:::proof{of=prop-successor-not-ice}
We build a computable order $\mathcal B$ on $\nat$ by stages, as a finite order $\mathcal B_s$ at stage $s$, never changing the relative order of elements already placed. Requirement $\mathcal R_e$: $W_e$ is not the successor relation of $\mathcal B$. Its strategy: at stage $e$, add two new elements $u_e < v_e$ at the end of the order, with nothing between them. At later stages, new elements are added at the end, except as follows: if the pair $(u_e, v_e)$ appears in $W_{e,s}$, and nothing has yet been put between $u_e$ and $v_e$, add one new element between them, once.

The order is computable: the position of a new element relative to the old ones is decided when it is added. Every element has finitely many predecessors: the predecessors of an element $x$ added at stage $s$ are elements added before stage $s$, together with at most one element inserted into each of the finitely many pairs $(u_e, v_e)$ placed before $x$. So $\mathcal B \cong \omega$. For each $e$: if $(u_e, v_e) \in W_e$, an element was put between them, so $v_e$ is not the successor of $u_e$, and $W_e$ contains a non-successive pair; if $(u_e, v_e) \notin W_e$, nothing was put between them, so $v_e$ is the successor of $u_e$, and $W_e$ misses a successive pair. Either way $W_e$ is not the successor relation of $\mathcal B$.
:::

The proof needs no priority: each requirement has its own pair of elements and never interferes with the others. It shows that $S$ is not $\Sigma^c_1$-definable with parameters on $\omega$, by the theorem of Ash, Knight, Manasse, Slaman and Chisholm.

:::quiz[the successor relation]
Why does each requirement place its pair at the end of the order?

- [x] So that nothing has been decided about the elements between them: inserting one element later keeps the order linear, and each element still has finitely many predecessors.
- [ ] Because $W_e$ only enumerates pairs at the end.

  $W_e$ is arbitrary; the position is chosen so that the requirement can still act.
- [ ] To make the order computable.

  Any placement decided at the time an element is added keeps the order computable.
:::

## The Ash–Nerode theorem

When is every intrinsically c.e. relation formally c.e.? The proof of :ref{#thm-akms-chisholm-1} builds a copy that is in general not computable: at each stage it searches through extensions of a tuple, and the search asks whether some extension makes $W_e$ enumerate a tuple outside $R$, a question about $R$ that may be undecidable. When this question is decidable, the construction can be made computable, with a finite injury argument to handle the questions with negative answers.

:::theorem[Ash, Nerode]{#thm-ash-nerode}
Let $\mathcal A$ be a computable structure and $R$ a relation on $\mathcal A$ satisfying the following **effectiveness condition**: for every tuple $\bar c$ of $\mathcal A$ and every existential formula $\varphi(\bar c, \bar x)$, one can decide whether some tuple $\bar a \notin R$ satisfies $\varphi(\bar c, \bar a)$. Then $R$ is intrinsically c.e. if and only if it is formally c.e.
:::

The condition holds, for instance, if the existential diagram of $(\mathcal A, R)$ is computable. We admit the theorem; its proof is a finite injury construction of a computable copy, in which a witness mapped to an element of $R$ is moved outside $R$ when $W_e$ enumerates it, the effectiveness condition deciding whether the move is possible (Ash–Knight, Theorem 11.1). Manasse (1982) built examples showing that the condition cannot be dropped: there are relations that are intrinsically c.e. but not formally c.e. Harizanov (1991) strengthened the theorem: under the same kind of condition, if $R$ is not formally c.e., then for every c.e. set $S$ there is a computable copy in which the image of $R$ has the Turing degree of $S$ (Ash–Knight, Theorem 11.6).

Applying the theorem to $R$ and its complement gives the corresponding statement for computability: under the effectiveness condition for both, $R$ is intrinsically computable if and only if $R$ and its complement are formally c.e. (Ash–Knight, Corollary 11.2).

:::proposition[Ash, Nerode]{#prop-vector-space-intrinsic}
Let $\mathcal V$ be a computable $\mathbb Q$-vector space of infinite dimension, and $R$ a unary relation on it. Then $R$ is intrinsically computable if and only if $R$ is finite or cofinite.
:::

:::proof{of=prop-vector-space-intrinsic}
A finite or cofinite relation is defined by a quantifier-free formula with finitely many parameters, the exceptional elements, and so is its complement: it is intrinsically computable. Conversely, let $R$ be intrinsically computable, infinite and co-infinite; in particular $R$ is computable in $\mathcal V$. Vector spaces have effective quantifier elimination, and every set defined by a formula with one free variable and parameters $\bar c$ is either finite and contained in the span of $\bar c$, or cofinite, and one can decide which and list the finite ones. Since $R$ and its complement are infinite, a cofinite definable set meets both. So the effectiveness condition holds for $R$ and its complement: for a formula $\varphi(\bar c, x)$, if the set it defines is finite, list it and test its elements with the computable $R$; if it is cofinite, it meets the complement of $R$, and $R$. By the corollary of :ref{#thm-ash-nerode} for computability, $R$ and its complement are defined by $\Sigma^c_1$ formulas with some parameters $\bar c$. Each disjunct of these formulas defines a set that is contained in $R$ or in its complement, hence not cofinite, hence finite and contained in the span of $\bar c$. So $R$ and its complement are contained in the span of $\bar c$, which is a proper subspace since the dimension is infinite: a contradiction.
:::

So on an infinite-dimensional vector space, linear algebra gives no intrinsically computable unary relation beyond the trivial ones. The same holds for algebraically closed fields of infinite transcendence degree (Ash–Knight, Proposition 11.4).

::::exercise{#ex-multiples-vector difficulty=1 objective="Apply the classification of intrinsically computable relations on vector spaces to a natural relation."}
Let $\mathcal V$ be a computable $\mathbb Q$-vector space of infinite dimension and $v \neq 0$ in $\mathcal V$. Show that the set $\mathbb Q v$ of multiples of $v$ is r.i.c.e., but not intrinsically computable.

:::solution
It is defined with the parameter $v$ by the $\Sigma^c_1$ formula $\bigvee_{q \in \mathbb Q} x = q \cdot v$, so it is r.i.c.e. It is infinite and co-infinite, so by :ref{#prop-vector-space-intrinsic}, it is not intrinsically computable: some computable copy decides membership in the span of the image of $v$ only with a non-computable oracle.
:::
::::

## Notes and references

The distinction between intrinsic and relatively intrinsic notions goes back to Ash and Nerode (1981), who proved :ref{#thm-ash-nerode} and :ref{#prop-vector-space-intrinsic}; Ash, Knight, Manasse and Slaman (1989) and Chisholm (1990) introduced the relative notions, for which no condition is needed. :ref{#prop-successor-not-ice} is Ash–Knight, Section 11.1, Example 1. Manasse's counterexamples are in his thesis (1982); Harizanov's theorem is from Harizanov (1991).

- C. J. Ash and A. Nerode, *Intrinsically recursive relations*, in *Aspects of Effective Algebra*, Upside Down A Book Company, 1981, 26–41.
- V. S. Harizanov, *Some effects of Ash–Nerode and other decidability conditions on degree spectra*, Annals of Pure and Applied Logic 55 (1991), 51–65.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 11.

:::::exercises
::::exercise{#ex-successor-jump difficulty=1 objective="Locate the successor relation on ω in the arithmetic hierarchy relative to the copy."}
Show that on every copy $\mathcal B$ of $\omega$, the successor relation is co-c.e. in $D(\mathcal B)$, hence computable in $D(\mathcal B)'$; and that it is not uniformly computable in $D(\mathcal B)$ across copies.

:::solution
$(x, y)$ is not a successive pair if $y \leq x$ or some $z$ lies strictly between, a $\Sigma^0_1$ property of $D(\mathcal B)$: the successor relation is co-c.e. in $D(\mathcal B)$, hence computable in $D(\mathcal B)'$. If it were computable in $D(\mathcal B)$ for every copy, it would be c.e. in every computable copy, contradicting :ref{#prop-successor-not-ice}.
:::
::::
:::::
