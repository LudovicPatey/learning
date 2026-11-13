---
title: Indiscernible types and automorphism groups
summary: Realizations of a minimal type are indiscernible; realizing a minimal type along a linear order gives a model that is the ground model followed by one gap for each element of the order; every completion of PA has models whose automorphism group is that of any given linear order, and rigid models of every infinite cardinality.
duration: 30
prerequisites: [minimal-types]
---

A minimal type $p$ over a model $M$ of $\mathrm{PA}$ is realized at most once in each gap, and it decides, by a single formula, every definable family of formulas. These two properties together make its realizations **indiscernible**: any two increasing tuples of realizations have the same type over $M$. One can then realize $p$ along an arbitrary linear order $(I, <)$, one realization $d_i$ for each $i \in I$, and the model generated is $M$ followed by one gap for each $i$. Indiscernibility turns every automorphism of $(I, <)$ into an automorphism of the model, and rarity shows that there are no others, since an automorphism must permute the realizations of $p$. This is Gaifman's construction of models of $\mathrm{PA}$ with prescribed automorphism groups.

Throughout, $M$ is a model of $\mathrm{PA}$ and $p$ a minimal $M$-type (:ref{#def-ee-minimal-type}); $\mathrm{cl}_K(A)$ is the definable closure, as in the previous lesson.

## Indiscernibility

:::proposition{#prop-ee-indiscernible}
Let $p$ be a minimal $M$-type, $K \succcurlyeq M$, and $c_0 < \cdots < c_n$, $d_0 < \cdots < d_n$ elements of $K$ realizing $p$. Then $(c_0, \dots, c_n)$ and $(d_0, \dots, d_n)$ have the same type over $M$.
:::

:::proof{of=prop-ee-indiscernible}
By induction on $n$. For $n = 0$, both types are $p$. Assume the statement for $n$, and let $c_0 < \cdots < c_{n+1}$ and $d_0 < \cdots < d_{n+1}$ realize $p$; write $\bar c = (c_0, \dots, c_n)$ and $\bar d = (d_0, \dots, d_n)$. Let $\varphi(\bar v, v_{n+1}, w)$ be a formula and $a \in M$. By strong definability, applied to $\varphi$ as a formula in $v_{n+1}$ with parameters $(\bar v, w)$, there is $\theta(v, b) \in p$, with $b \in M$, such that $M$ satisfies, for all $\bar v, w$,
$$
\exists u\ \Big( \forall v' \geq u\ \big(\theta(v', b) \rightarrow \varphi(\bar v, v', w)\big) \vee \forall v' \geq u\ \big(\theta(v', b) \rightarrow \neg \varphi(\bar v, v', w)\big) \Big).
$$
Let $t(\bar v, w, z)$ be the least such $u$ with $b$ replaced by $z$ ($0$ if none), and $t'(\bar v) = \max_{w, z \leq v_0} t(\bar v, w, z)$, a Skolem function. The property inside $\exists u$ is preserved when $u$ increases, and $a, b \in M$ are below $c_0$ and $d_0$; so, in $K$, it holds at $u = t'(\bar c)$ for $\bar v = \bar c$, $w = a$, $z = b$, and at $u = t'(\bar d)$ for $\bar d$.

By rarity, $t'(\bar c) < c_{n+1}$: with the one-variable Skolem function $T(x) = \max_{\bar y \leq x} t'(\bar y)$, $t'(\bar c) \leq T(c_n)$, and :ref{#lem-ee-rare-syntactic} for $T$ gives $T(c_n) < c_{n+1}$. Similarly $t'(\bar d) < d_{n+1}$.

Suppose $K \models \varphi(\bar c, c_{n+1}, a)$. Since $c_{n+1} \geq t'(\bar c)$ and $K \models \theta(c_{n+1}, b)$, the second disjunct fails at $\bar c$, so $K \models \psi(\bar c)$, where $\psi(\bar v)$ is $\forall v' \geq t'(\bar v)\ (\theta(v', b) \rightarrow \varphi(\bar v, v', a))$, a formula with parameters $a, b \in M$. By the induction hypothesis, $K \models \psi(\bar d)$, and with $d_{n+1} \geq t'(\bar d)$ and $\theta(d_{n+1}, b)$, $K \models \varphi(\bar d, d_{n+1}, a)$. The converse is symmetric.
:::

:::quiz[indiscernibility]
In the proof of :ref{#prop-ee-indiscernible}, why is $t'(\bar c) < c_{n+1}$?

- [x] By rarity: $t'(\bar c) \leq T(c_n)$ for a one-variable Skolem function $T$, and the formula $\theta \in p$ given by :ref{#lem-ee-rare-syntactic} for $T$ holds of both $c_n < c_{n+1}$, so $T(c_n) < c_{n+1}$.
- [ ] By strong definability, which gives the bound $t'$.

  Strong definability gives the formula $\theta(v, b)$ and the eventual bound $t'(\bar v)$; it does not compare $t'(\bar c)$ with the next realization.
- [ ] Because $t'(\bar c) \in M$ and $c_{n+1} > M$.

  The value $t'(\bar c)$ depends on $\bar c$ and is in general not in $M$; what bounds it is a Skolem function of $c_n$.
:::

## Realizations along a linear order

:::theorem[Gaifman]{#thm-ee-linear-order}
Let $p$ be a minimal $M$-type and $(I, <)$ a linear order. There are $K \succcurlyeq M$ and elements $d_i \in K$, $i \in I$, such that, with $D = \{ d_i : i \in I \}$:

1. $K = \mathrm{cl}_K(M \cup D)$;
2. $d_i < d_j$ if and only if $i < j$;
3. $K = M \cup \bigcup_{i \in I} \mathrm{gap}(d_i)$;
4. the elements of $K$ that realize $p$ are exactly the $d_i$.
:::

:::proof{of=thm-ee-linear-order}
The elementary diagram of $M$, the sets $p(d_i)$ and the sentences $d_i < d_j$ for $i < j$ are finitely satisfiable: a finite part involves finitely many formulas of $p$, whose conjunction $\theta$ defines an unbounded set, and finitely many indices, to which increasing solutions of $\theta$ in $M$ can be assigned. Let $K' \succcurlyeq M$ satisfy them, and $K = \mathrm{cl}_{K'}(M \cup D) \preccurlyeq K'$. Items 1 and 2 hold.

For 3, let $c \in K$; then $c \in K_0 = \mathrm{cl}_K(M \cup \{ d_{i_0}, \dots, d_{i_n} \})$ for some $i_0 < \cdots < i_n$. Let $N_0 = M$ and $N_{k+1} = \mathrm{cl}_K(N_k \cup \{ d_{i_k} \})$. Every element of $N_k$, $k \geq 1$, is $t(\bar m, d_{i_0}, \dots, d_{i_{k-1}})$ with $\bar m \in M$, so it is at most $T(d_{i_{k-1}})$ for the one-variable Skolem function $T(x) = \max_{\bar y \leq x} t(\bar y)$, since $\bar m < d_{i_0}$; and $T(d_{i_{k-1}}) < d_{i_k}$ by rarity. So $d_{i_k} > N_k$, and its type over $N_k$ is an unbounded extension of $p$, strongly definable by :ref{#ex-ee-sd-preserved}. By :ref{#prop-ee-one-gap}, $N_{k+1} = N_k \cup \mathrm{gap}^{N_{k+1}}(d_{i_k})$. Hence $K_0 = N_{n+1} = M \cup \bigcup_{k \leq n} \mathrm{gap}^{K_0}(d_{i_k})$, and gaps are the same in $K_0$ and in $K$ (remark after :ref{#lem-ee-gap-criterion}). So $c \in M$ or $c \in \mathrm{gap}^K(d_{i_k})$ for some $k$.

For 4, let $c \in K$ realize $p$. Then $c \notin M$, as $p$ is unbounded, so $c \in \mathrm{gap}(d_i)$ for some $i$ by 3, and $c = d_i$ by rarity.
:::

## Automorphism groups

:::corollary[Gaifman]{#cor-ee-automorphisms}
For every complete extension $T$ of $\mathrm{PA}$ and every linear order $(I, <)$, there is a model $K$ of $T$ whose automorphism group is isomorphic to the automorphism group of $(I, <)$.
:::

:::proof{of=cor-ee-automorphisms}
Let $N \models T$, and let $M$ be the set of elements of $N$ definable without parameters; $M \preccurlyeq N$ by :ref{#lem-ee-mp}, and every element of $M$ is definable without parameters in $M$. Let $p$ be a minimal $M$-type and $K$ given by :ref{#thm-ee-linear-order}. Then $K \models T$, and $K = \mathrm{cl}_K(D)$, since $M = \mathrm{cl}_K(\emptyset)$.

An automorphism $g$ of $K$ fixes the elements of $M$, which are definable without parameters in $K$; so it preserves the formulas of $p$, maps $D$ onto $D$ by item 4, and preserves the order. Let $\hat g(i) = j$ when $g(d_i) = d_j$; $\hat g$ is an automorphism of $(I, <)$, and $g \mapsto \hat g$ is a group homomorphism. It is injective: an automorphism that fixes $D$ fixes $\mathrm{cl}_K(D) = K$. It is onto: given an automorphism $f$ of $(I, <)$, set $g(t(d_{i_0}, \dots, d_{i_n})) = t(d_{f(i_0)}, \dots, d_{f(i_n)})$ for $i_0 < \cdots < i_n$. Two descriptions of elements, and any formula about them, involve finitely many indices, which can be listed in increasing order; $f$ maps this list to an increasing list, and by :ref{#prop-ee-indiscernible} the two tuples have the same type. So $g$ is well defined and elementary, and it is a bijection, with inverse given by $f^{-1}$.
:::

:::quiz[automorphism groups]
In the proof of :ref{#cor-ee-automorphisms}, why does an automorphism $g$ of $K$ map $D$ onto $D$?

- [x] The elements of $M$ are definable without parameters, so $g$ fixes them and preserves every formula of $p$; it maps realizations of $p$ to realizations of $p$, and by item 4 of :ref{#thm-ee-linear-order} these are exactly the $d_i$.
- [ ] Because $K = \mathrm{cl}_K(D)$.

  This shows that $g$ is determined by its values on $D$, which gives injectivity of $g \mapsto \hat g$, not that $g$ preserves $D$.
- [ ] Because automorphisms preserve gaps.

  They do, but a gap contains many elements besides $d_i$; rarity, through item 4, is what singles out $d_i$ in its gap.
:::

With $(I, <)$ an infinite cardinal, which has no non-trivial automorphism, every completion of $\mathrm{PA}$ has rigid models of every infinite cardinality: $K = \mathrm{cl}_K(D)$ has the cardinality of $I$. Gaifman also obtained, from the same models, that for every set $I$ the lattice of elementary substructures of a suitable model of $T$ is isomorphic to the Boolean algebra of subsets of $I$; we state this without proof (Wong, Corollary 11.13). Schmerl (2002) extended the corollary to a much larger class of groups (Wong, Further comments to Lecture 11).

## Notes and references

The results of this lesson are due to Gaifman (1976). :ref{#prop-ee-indiscernible} is Wong's Proposition 11.7, whose proof follows Lemma 3.1.19 of Kossak and Schmerl; :ref{#thm-ee-linear-order} is Wong's Theorem 11.10, and :ref{#cor-ee-automorphisms} his Corollary 11.14. The lattice theorem is Wong's Corollary 11.13. Wong's Proposition 11.12 states converses: an unbounded indiscernible type is minimal (Kossak and Schmerl, Lemmas 3.1.13 and 3.1.18). Schmerl's theorem is reported in Wong's Further comments to Lecture 11.

- H. Gaifman, *Models and types of Peano's arithmetic*, Annals of Mathematical Logic 9 (1976), 223–306.
- J. H. Schmerl, *Automorphism groups of models of Peano arithmetic*, Journal of Symbolic Logic 67 (2002), 1249–1264.
- R. Kossak and J. H. Schmerl, *The Structure of Models of Peano Arithmetic*, Oxford Logic Guides 50, Clarendon Press, 2006.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 11.
