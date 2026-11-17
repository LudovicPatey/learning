---
title: Indiscernible types and automorphism groups
summary: Realizations of a minimal type are indiscernible; realizing a minimal type along a linear order gives a model that is the ground model followed by one gap for each element of the order; every completion of PA has models whose automorphism group is that of any given linear order, and rigid models of every infinite cardinality.
duration: 25
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

::::exercise{#ex-ee-aut-examples difficulty=1 objective="Compute the automorphism groups given by Gaifman's construction for simple linear orders."}
Let $T$ be a complete extension of $\mathrm{PA}$, and let $M$ and $K$ be as in the proof of :ref{#cor-ee-automorphisms} for a linear order $(I, <)$.

1. Show that if $(I, <)$ is a well-order, then $K$ is rigid.
2. Show that if $(I, <) = (\mathbb Z, <)$, the automorphism group of $K$ is isomorphic to $(\mathbb Z, +)$.
3. Show that $|K| = \max(\aleph_0, |I|)$, and deduce that $T$ has rigid models of every infinite cardinality.

:::solution
By :ref{#cor-ee-automorphisms}, it suffices to compute the automorphism group of $(I, <)$.

1. Let $f$ be an automorphism of $(I, <)$ with $f \neq \mathrm{id}$, and $i$ the least element with $f(i) \neq i$. If $f(i) < i$, then $f(f(i)) = f(i)$ by minimality, and $f$ is not injective. If $f(i) > i$, let $k = f^{-1}(i)$; then $f(k) = i < f(i)$, so $k < i$, hence $f(k) = k$ by minimality, and $k = i$, a contradiction. So $f = \mathrm{id}$.
2. An automorphism $f$ of $(\mathbb Z, <)$ maps $n + 1$, the least element above $n$, to the least element above $f(n)$, so $f(n + 1) = f(n) + 1$ and $f(n) = n + f(0)$ for all $n$. Conversely each translation is an automorphism, and $f \mapsto f(0)$ is an isomorphism onto $(\mathbb Z, +)$.
3. $M$ is countable, since its elements are defined by formulas without parameters, and infinite, since it contains $\nat$. $K = \mathrm{cl}_K(M \cup D)$ consists of the values of Skolem functions at finite tuples of $M \cup D$, so $|K| \leq \max(\aleph_0, |I|)$; and $K$ contains $M$ and the $|I|$ distinct elements $d_i$. For an infinite cardinal $\kappa$, take $(I, <) = (\kappa, <)$, a well-order: $K \models T$ is rigid and has cardinality $\kappa$.
:::
::::

## Notes and references

The results of this lesson are due to Gaifman (1976). :ref{#prop-ee-indiscernible} is Wong's Proposition 11.7, whose proof follows Lemma 3.1.19 of Kossak and Schmerl; :ref{#thm-ee-linear-order} is Wong's Theorem 11.10, and :ref{#cor-ee-automorphisms} his Corollary 11.14. The lattice theorem is Wong's Corollary 11.13. Wong's Proposition 11.12 states converses: an unbounded indiscernible type is minimal (Kossak and Schmerl, Lemmas 3.1.13 and 3.1.18). Schmerl's theorem is reported in Wong's Further comments to Lecture 11.

- H. Gaifman, *Models and types of Peano's arithmetic*, Annals of Mathematical Logic 9 (1976), 223–306.
- J. H. Schmerl, *Automorphism groups of models of Peano arithmetic*, Journal of Symbolic Logic 67 (2002), 1249–1264.
- R. Kossak and J. H. Schmerl, *The Structure of Models of Peano Arithmetic*, Oxford Logic Guides 50, Clarendon Press, 2006.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 11.

:::::exercises
::::exercise[Two indiscernibles]{#ex-ee-two-indiscernibles difficulty=2 objective="Use rarity and indiscernibility to separate the models generated by two realizations of a minimal type."}
Let $p$ be a minimal $M$-type and $K$, $d_0 < d_1$ as in :ref{#thm-ee-linear-order} for $I = \{0, 1\}$. Write $\mathrm{cl}(A)$ for $\mathrm{cl}_K(M \cup A)$. Show that $d_1 \notin \mathrm{cl}(\{d_0\})$, that $d_0 \notin \mathrm{cl}(\{d_1\})$, and that $\mathrm{cl}(\{d_0\}) \cap \mathrm{cl}(\{d_1\}) = M$. Deduce that $M$, $\mathrm{cl}(\{d_0\})$, $\mathrm{cl}(\{d_1\})$ and $K$ are four distinct elementary substructures of $K$ containing $M$.

:::solution
*$d_1 \notin \mathrm{cl}(\{d_0\})$.* The elements of $\mathrm{cl}(\{d_0\})$ are below $d_1$ by :ref{#ex-ee-rare-spread}.

*$d_0 \notin \mathrm{cl}(\{d_1\})$.* Suppose $d_0 = t(\bar m, d_1)$ with $t$ Skolem and $\bar m \in M$. The type $p$ has an unbounded extension to $K$ (section on extensions of types in the lesson on gaps); let $e$ realize it in some $K'' \succcurlyeq K$. Then $e > K$, and $e$ realizes $p$. In $K''$, the pairs $(d_0, d_1)$, $(d_0, e)$ and $(d_1, e)$ are increasing pairs of realizations of $p$, so they have the same type over $M$ by :ref{#prop-ee-indiscernible}. The formula $v_0 = t(\bar m, v_1)$ belongs to the type of $(d_0, d_1)$, hence $d_0 = t(\bar m, e)$ and $d_1 = t(\bar m, e)$, so $d_0 = d_1$, a contradiction.

*Intersection.* $\mathrm{cl}(\{d_i\}) = M(p / d_i)$, since $d_i$ realizes $p$, and by :ref{#prop-ee-one-gap} it is contained in $M \cup \mathrm{gap}(d_i)$, the gap being computed in $\mathrm{cl}(\{d_i\})$, or equivalently in $K$ (remark after :ref{#lem-ee-gap-criterion}). The gaps of $d_0$ and $d_1$ are disjoint, since $d_0 \notin \mathrm{gap}(d_1)$ by rarity. So the intersection is $M$.

*Four models.* All four are elementary substructures of $K$ (:ref{#lem-ee-mp}). $M$ differs from the others, which contain $d_0$ or $d_1$; $\mathrm{cl}(\{d_0\})$ and $\mathrm{cl}(\{d_1\})$ differ from each other and from $K$ by the first two statements. Gaifman's lattice theorem, stated in the lesson, says that there are no others.
:::
::::

::::exercise{#ex-ee-aut-rationals difficulty=2 objective="Describe how automorphisms of Gaifman's models act on gaps, and find the elements they all fix."}
Let $T$ be a complete extension of $\mathrm{PA}$, and $M$, $K$ as in the proof of :ref{#cor-ee-automorphisms} for $(I, <) = (\mathbb Q, <)$.

1. Show that every automorphism $g$ of $K$ maps $\mathrm{gap}(d_i)$ onto $\mathrm{gap}(d_{\hat g(i)})$.
2. Show that the elements of $K$ fixed by every automorphism are exactly the elements of $M$.

:::solution
1. $g$ preserves the order and the Skolem functions, which are defined without parameters: $g(t(x)) = t(g(x))$. By :ref{#lem-ee-gap-criterion}, $c \in \mathrm{gap}(d_i)$ if and only if $t(c) \geq d_i$ and $s(d_i) \geq c$ for some Skolem $t, s$, which is equivalent to $t(g(c)) \geq g(d_i)$ and $s(g(d_i)) \geq g(c)$, that is, $g(c) \in \mathrm{gap}(d_{\hat g(i)})$. So $g$ maps $\mathrm{gap}(d_i)$ into $\mathrm{gap}(d_{\hat g(i)})$, and $g^{-1}$ maps it back, since $\widehat{g^{-1}} = \hat g^{-1}$.
2. The elements of $M$ are definable without parameters, so they are fixed. Let $c \in K \setminus M$; by item 3 of :ref{#thm-ee-linear-order}, $c \in \mathrm{gap}(d_i)$ for some $i \in \mathbb Q$. The translation $f(x) = x + 1$ is an automorphism of $(\mathbb Q, <)$, and by :ref{#cor-ee-automorphisms} there is an automorphism $g$ of $K$ with $\hat g = f$. By item 1, $g(c) \in \mathrm{gap}(d_{i+1})$, which is disjoint from $\mathrm{gap}(d_i)$ by rarity; so $g(c) \neq c$.
:::
::::

::::exercise{#ex-ee-cuts-initial-segments difficulty=3 objective="Determine the elementary cuts of the models generated by a minimal type along a linear order."}
Let $p$ be a minimal $M$-type, and $K$, $(d_i)_{i \in I}$ as in :ref{#thm-ee-linear-order}. For $J \subseteq I$, let $D_J = \{ d_j : j \in J \}$. Show that $J \mapsto \mathrm{cl}_K(M \cup D_J)$ is a bijection from the initial segments of $(I, <)$ onto the elementary cuts of $K$ containing $M$ (in the sense of :ref{#ex-ee-gap-cuts}), and that $\mathrm{cl}_K(M \cup D_J) = M \cup \bigcup_{j \in J} \mathrm{gap}(d_j)$.

:::solution
*Order of the gaps.* For $i \neq j$, $\mathrm{gap}(d_i) \cap \mathrm{gap}(d_j) = \emptyset$ by rarity. Gaps are convex, and two disjoint convex sets $A \ni a$, $B \ni b$ with $a < b$ satisfy $A < B$: if $y \in B$, $x \in A$ and $y \leq x$, then either $b \leq x$, and $b$ lies between $a$ and $x$, so $b \in A$; or $x < b$, and $x$ lies between $y$ and $b$, so $x \in B$. So $\mathrm{gap}(d_i) < \mathrm{gap}(d_j)$ for $i < j$, and $M < \mathrm{gap}(d_i)$ since $M \subseteq K[d_i]$ (proof of :ref{#prop-ee-one-gap}).

*Where the elements are generated.* Let $c \in \mathrm{gap}(d_i)$. Then $c = t(\bar m, d_{i_0}, \dots, d_{i_n})$ with $i_0 < \cdots < i_n$, and we may assume that $i$ is one of the $i_k$. With the models $N_k$ of the proof of :ref{#thm-ee-linear-order}, let $k$ be least with $c \in N_{k+1}$. Since $c \notin M = N_0$, $c \in N_{k+1} \setminus N_k \subseteq \mathrm{gap}(d_{i_k})$, so $\mathrm{gap}(d_{i_k}) = \mathrm{gap}(d_i)$ and $i_k = i$. Hence $c \in \mathrm{cl}_K(M \cup \{ d_j : j \leq i \})$.

*The cut of $J$.* Let $J$ be an initial segment and $E_J = M \cup \bigcup_{j \in J} \mathrm{gap}(d_j)$. By the previous paragraph, $E_J \subseteq \mathrm{cl}_K(M \cup D_J)$. Conversely, an element $t(\bar m, d_{j_0}, \dots, d_{j_n})$ with $j_0 < \cdots < j_n$ in $J$ lies in the model $N_{n+1}$ built from these indices, which is $M \cup \bigcup_{k \leq n} \mathrm{gap}(d_{j_k})$; so it is in $E_J$. $E_J$ is an initial segment of $K$: if $x < y$ with $y \in \mathrm{gap}(d_j)$, $j \in J$, then $x \in M$ or $x \in \mathrm{gap}(d_i)$ for some $i$ (item 3), and $i \leq j$ by the order of the gaps, so $i \in J$. And $\mathrm{cl}_K(M \cup D_J) \preccurlyeq K$ by :ref{#lem-ee-mp}. So $E_J$ is an elementary cut.

*Every cut.* Let $E \supseteq M$ be an elementary cut of $K$, and $J = \{ j : d_j \in E \}$, an initial segment of $I$ since $E$ is an initial segment. By :ref{#ex-ee-gap-cuts}, $E$ contains $K(c) \supseteq \mathrm{gap}(c)$ for each $c \in E$, so with item 3 of the theorem, $E = M \cup \bigcup_{j \in J} \mathrm{gap}(d_j) = E_J$. Distinct initial segments $J \neq J'$ give distinct cuts, since $d_j \in E_J$ if and only if $j \in J$, the gaps being disjoint.
:::
::::

::::exercise{#ex-ee-linear-order-unique difficulty=2 objective="Extend indiscernibility across two elementary extensions and deduce that Gaifman's model depends only on the order type."}
Let $p$ be a minimal $M$-type.

1. Let $K, K' \succcurlyeq M$, and let $c_0 < \cdots < c_n$ in $K$ and $d_0 < \cdots < d_n$ in $K'$ realize $p$. Show that $K \models \varphi(\bar c)$ if and only if $K' \models \varphi(\bar d)$, for every formula $\varphi(\bar v)$ with parameters in $M$.
2. Let $K = \mathrm{cl}_K(M \cup D)$ and $K' = \mathrm{cl}_{K'}(M \cup D')$ be given by :ref{#thm-ee-linear-order} for linear orders $(I, <)$ and $(I', <)$, and $f : I \to I'$ an isomorphism. Show that there is an isomorphism from $K$ onto $K'$ that is the identity on $M$ and maps $d_i$ to $d'_{f(i)}$.

:::solution
1. Follow the proof of :ref{#prop-ee-indiscernible}, by induction on $n$, with $\bar c$ in $K$ and $\bar d$ in $K'$. For $n = 0$, both realize $p$. In the induction step, the formula $\theta(v, b) \in p$, the Skolem functions $t'$ and $T$, and the formula $\psi(\bar v)$ are defined from $M$ alone. The defining sentence of strong definability and the sentence of :ref{#lem-ee-rare-syntactic} for $T$ have parameters in $M$ and hold in $M$, hence in $K$ and in $K'$; so $t'(\bar c) < c_{n+1}$ in $K$ and $t'(\bar d) < d_{n+1}$ in $K'$. If $K \models \varphi(\bar c, c_{n+1}, a)$, then $K \models \psi(\bar c)$, so $K' \models \psi(\bar d)$ by the induction hypothesis, and $K' \models \varphi(\bar d, d_{n+1}, a)$. The converse is symmetric.
2. Set $g(t(\bar m, d_{i_0}, \dots, d_{i_n})) = t(\bar m, d'_{f(i_0)}, \dots, d'_{f(i_n)})$ for Skolem $t$, $\bar m \in M$ and $i_0 < \cdots < i_n$; every element of $K$ has this form, since $K = \mathrm{cl}_K(M \cup D)$. Finitely many such descriptions and a formula about them involve finitely many indices; list them in increasing order, $j_0 < \cdots < j_r$. Then $f(j_0) < \cdots < f(j_r)$, and by item 1 the tuples $(d_{j_0}, \dots, d_{j_r})$ and $(d'_{f(j_0)}, \dots, d'_{f(j_r)})$ satisfy the same formulas with parameters in $M$. So $g$ is well defined and preserves all formulas, hence it is injective and preserves the operations and the order. It is onto, since $K' = \mathrm{cl}_{K'}(M \cup D')$ and $f$ is onto, and it is the identity on $M$, given by constant functions. In particular, the model of :ref{#thm-ee-linear-order} is determined, up to isomorphism over $M$, by $p$ and the order type of $(I, <)$.
:::
::::
:::::
