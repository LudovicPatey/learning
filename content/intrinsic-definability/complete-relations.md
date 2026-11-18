---
title: Complete relations and the jump of a relation
summary: The Kleene relation of a structure, which collects all relations definable by Σᶜ₁ formulas, is r.i.c.e. and complete among r.i.c.e. relations; the jump of a relation; the jump is never relatively intrinsically computable, by Kleene's diagonal argument; structural versus binary information; linear dependence is complete on ℚ-vector spaces, and adjacency on linear orders, by Dickson's lemma.
duration: 35
prerequisites: [intrinsic-relations]
---

In computability theory, the halting problem is the most complicated c.e. set, and the jump turns any set into a more complicated one. On a structure, the same roles are played by relations. This lesson defines the analogue of the halting problem, a relation that collects all $\Sigma^c_1$ definitions, shows that it is complete among r.i.c.e. relations and not relatively intrinsically computable, and identifies simpler complete relations in two classical classes: linear dependence for vector spaces, adjacency for linear orders. The second example uses a well-quasi-ordering argument that recurs in the subject.

In this lesson relations may carry a number coordinate: they are subsets of $\nat \times A^{<\nat}$. Such a relation is r.i.c.e. if its image in every copy is c.e. in the diagram, and the theorem of Ash, Knight, Manasse, Slaman and Chisholm (:ref{#thm-akms-chisholm-1}) holds with the same proof: there is a tuple $\bar p$ such that the sections $\{ \bar b : (m, \bar b) \in R \}$ are defined, uniformly in $m$, by $\Sigma^c_1$ formulas with parameters $\bar p$. A relation $R$ is **r.i. computable in** $Q$, written $R \leq_{rT} Q$, if $R^{\mathcal B}$ is computable in $D(\mathcal B) \oplus Q^{\mathcal B}$ for every copy $(\mathcal B, R^{\mathcal B}, Q^{\mathcal B})$ of $(\mathcal A, R, Q)$.

## The Kleene relation

Let $(\varphi^{c}_{i, j})_{i \in \nat}$ list the $\Sigma^c_1$ formulas with $j$ free variables, as in the previous lesson.

:::definition{#def-kleene-relation}
The **Kleene relation** of $\mathcal A$ is
$$
\vec K^{\mathcal A} = \{ (i, \bar b) \in \nat \times A^{<\nat} : \mathcal A \models \varphi^c_{i, |\bar b|}(\bar b) \}.
$$
A relation $R$ is **complete** if every r.i.c.e. relation is r.i. computable in $R$, and **r.i.c.e. complete** if moreover it is r.i.c.e.
:::

The Kleene relation is uniformly r.i.c.e., by the uniform satisfaction operator of $\Sigma^c_1$ formulas. Every r.i.c.e. relation reduces to it, with parameters.

:::lemma{#lem-kleene-complete}
For every r.i.c.e. relation $R \subseteq \nat \times A^{<\nat}$, there are a tuple $\bar a$ and a computable function $f$ such that $(m, \bar b) \in R \iff (f(m), \bar a \bar b) \in \vec K^{\mathcal A}$ for all $m$ and $\bar b$. Consequently, $\vec K^{\mathcal A}$ is r.i.c.e. complete.
:::

:::proof{of=lem-kleene-complete}
By :ref{#thm-akms-chisholm-1}, there are a tuple $\bar a$ and a computable function $(m, n) \mapsto e_{m, n}$ such that $(m, \bar b) \in R$ if and only if $\mathcal A \models \varphi^c_{e_{m, |\bar b|}, |\bar a| + |\bar b|}(\bar a, \bar b)$. The index depends on $|\bar b|$; to remove this dependence, recall that the $e$-th $\Sigma^c_1$ formula with $j$ free variables is the disjunction of the existential formulas with $j$ free variables whose indices $\langle i, j \rangle$ are in $W_e$. Let $f(m)$ be an index of a c.e. set containing, for each $n$, exactly the pairs $\langle i, |\bar a| + n \rangle$ of $W_{e_{m, n}}$. Then the $f(m)$-th formula with $|\bar a| + n$ free variables is the $e_{m, n}$-th one, for every $n$, which gives the equivalence. In a copy $\mathcal B$, with $\bar a'$ the image of $\bar a$, membership in $R^{\mathcal B}$ is decided by $\vec K^{\mathcal B}$ and the finite tuple $\bar a'$; so $R \leq_{rT} \vec K^{\mathcal A}$.
:::

The **jump** of a relation $Q$ is the Kleene relation of the expanded structure: $Q' = \vec K^{(\mathcal A, Q)}$. If $Q \leq_{rT} R$, then $Q' \leq_{rT} R'$ (:ref{#ex-jump-monotone}), so the jump is defined on the degrees of relations.

:::theorem[Montalbán; Vatev]{#thm-kleene-not-computable}
The Kleene relation $\vec K^{\mathcal A}$ is not relatively intrinsically computable. Consequently, for every relation $Q$, $Q <_{rT} Q'$.
:::

:::proof{of=thm-kleene-not-computable}
Suppose that the complement of $\vec K^{\mathcal A}$ is r.i.c.e. Then so is the relation
$$
\tilde R = \{ (i, \bar b) : \Phi_i(i)\converge \text{ and } (\Phi_i(i), \bar b \bar b) \notin \vec K^{\mathcal A} \},
$$
in which $\bar b \bar b$ is the tuple $\bar b$ repeated twice. By :ref{#lem-kleene-complete}, there are a total computable function $\Phi_e$ and a tuple $\bar a$ with $(i, \bar b) \in \tilde R \iff (\Phi_e(i), \bar a \bar b) \in \vec K^{\mathcal A}$. Take $i = e$ and $\bar b = \bar a$:
$$
(e, \bar a) \in \tilde R \iff (\Phi_e(e), \bar a \bar a) \in \vec K^{\mathcal A} \iff (e, \bar a) \notin \tilde R,
$$
a contradiction. For the second statement, $Q \leq_{rT} Q'$ since the atomic facts about $Q$ are among the $\Sigma^c_1$ facts of $(\mathcal A, Q)$, and $Q' \not\leq_{rT} Q$ by the first statement applied to $(\mathcal A, Q)$.
:::

:::quiz[the jump of a relation]
In the proof of :ref{#thm-kleene-not-computable}, why is the tuple $\bar b$ doubled in the definition of $\tilde R$?

- [x] So that the diagonal can feed the parameters $\bar a$ of the reduction back as the argument: the reduction prepends $\bar a$ to $\bar b$, and with $\bar b = \bar a$ the two tuples coincide.
- [ ] To make $\tilde R$ r.i.c.e.

  $\tilde R$ is r.i.c.e. because the complement of $\vec K^{\mathcal A}$ is assumed r.i.c.e.; the doubling plays no role in that.
- [ ] Because tuples of odd length are not allowed.

  All lengths are allowed; the doubling matches the form $\bar a \bar b$ of the reduction.
:::

## Structural and binary information

The halting problem, viewed as the relation $\emptyset' \times \{ \langle\rangle \}$, is always r.i.c.e., so every complete relation computes it. But it says nothing about the structure. A relation is **purely binary** if it is r.i. computable in $(\mathcal A, X)$ for some set $X \subseteq \nat$; a relation such as adjacency on a linear order, on the contrary, carries structural information. When only structure matters, one relativizes all notions to an arbitrary set: a relation is **structurally r.i.c.e.** if it is r.i.c.e. in $(\mathcal A, X)$ for some $X$, and **structurally complete** if every structurally r.i.c.e. relation is r.i. computable in $(\mathcal A, R, X)$ for some $X$. These are the "boldface" or "on a cone" versions of the notions, and they are the ones that classical algebraic examples realize.

:::proposition{#prop-ld-complete}
On a $\mathbb Q$-vector space, $\mathrm{LD} \oplus \emptyset'$ is r.i.c.e. complete; in particular $\mathrm{LD}$ is structurally complete.
:::

:::proof{of=prop-ld-complete}
Every countable $\mathbb Q$-vector space is isomorphic to $\mathbb Q^n$ for some $n \leq \omega$, which has a standard computable copy; take $n = \omega$, the finite case being simpler. Let $R$ be r.i.c.e., and $\mathcal W$ a copy. Using $\mathrm{LD}^{\mathcal W}$, list the elements of $\mathcal W$ and keep those independent of the previous ones: this computes a basis, hence an isomorphism $g : \mathbb Q^\omega \to \mathcal W$. The relation $g^{-1}(R^{\mathcal W})$ is the image of $R$ in the standard computable copy, so it is c.e., since $R$ is r.i.c.e., hence computable in $\emptyset'$. So $R^{\mathcal W}$ is computable in $g \oplus \emptyset'$, hence in $\mathrm{LD}^{\mathcal W} \oplus \emptyset' \oplus D(\mathcal W)$.
:::

The argument transfers relations through an isomorphism with a canonical copy, which the complete relation computes. The same works for algebraic independence in algebraically closed fields. For linear orders, there is no canonical copy, and the proof is of a different kind.

:::theorem[Montalbán]{#thm-adj-complete}
On a linear order, let $\overline{\mathrm{Adj}}$ be the adjacency relation together with the unary relations "first element" and "last element". Its complement $\neg\overline{\mathrm{Adj}}$ is r.i.c.e., and $\neg\overline{\mathrm{Adj}} \oplus \emptyset'$ is r.i.c.e. complete. In particular, adjacency is structurally complete.
:::

**Intuition.** It suffices to show that every $\Sigma^c_1$ formula about linear orders is equivalent to a finite combination of formulas of the form "there are at least $n$ elements between $x$ and $y$", and that $\emptyset'$ finds the combination. Each such formula is a finite statement about adjacency, so it is decidable from $\overline{\mathrm{Adj}}$. The finiteness comes from a well-quasi-ordering: the finite linear orders with $k$ named points are well-quasi-ordered by embedding, so every upward closed family of them has finitely many minimal elements.

:::proof{of=thm-adj-complete}
Let $\varphi(x_1, \ldots, x_k)$ be a $\Sigma^c_1$ formula in the vocabulary $\{ \leq \}$. A **$k$-pointed finite order** is a finite linear order with $k$ named elements, possibly equal. Up to isomorphism it is given by the order type $\pi$ of the named points (a weak ordering of $\{ 1, \ldots, k \}$) and the numbers $\bar n = (n_0, \ldots, n_k)$ of elements before the first point, between consecutive distinct points, and after the last; call it $L_{\pi, \bar n}$. If $\bar n \leq \bar m$ coordinatewise, $L_{\pi, \bar n}$ embeds into $L_{\pi, \bar m}$, preserving the points.

*Reduction to finite orders.* A $\Sigma^c_1$ formula holds of a tuple in a linear order if and only if one of its existential disjuncts holds of it in a finite suborder containing the tuple and the witnesses, and existential formulas are preserved by embeddings. So $\mathcal L \models \varphi(\bar c)$ if and only if some $L_{\pi, \bar n}$ embedding into $\mathcal L$ over $\bar c$ satisfies $\varphi$ at its points. The set $D$ of pairs $(\pi, \bar n)$ such that $L_{\pi, \bar n} \models \varphi$ is upward closed in $\bar n$, by preservation under embeddings.

*Finitely many minimal elements.* By Dickson's lemma, $\nat^{k+1}$ with the coordinatewise order has no infinite antichain and no infinite descending sequence, so for each $\pi$ the upward closed set $\{ \bar n : (\pi, \bar n) \in D \}$ has finitely many minimal elements $\bar d_1, \ldots, \bar d_\ell$. The oracle $\emptyset'$ finds them: membership in $D$ is c.e., and a candidate finite list is correct if all its members are in $D$ and every $\bar n$ above none of them is outside $D$; for a given list, the set of such $\bar n$ is a finite union of sets of the form $\{ \bar n : n_i < d_{j, i} \text{ for some } i \}$, and checking that none of them is in $D$ is a $\Pi^0_1$ condition. So
$$
\mathcal L \models \varphi(\bar c) \iff \bigvee_{(\pi, \bar d) \text{ minimal}} \psi_{\pi, \bar d}(\bar c),
$$
where $\psi_{\pi, \bar d}(\bar x)$ says that the points are ordered by $\pi$ and that there are at least $d_0$ elements before the first, at least $d_i$ between consecutive points, and at least $d_k$ after the last.

*Adjacency decides these formulas.* For $n \geq 1$, "at least $n$ elements between $x < y$" fails if and only if there is a chain $x = z_0 < z_1 < \cdots < z_j = y$ with $j \leq n$ in which consecutive elements are adjacent. In a copy, with $\overline{\mathrm{Adj}}$ given, search at the same time for $n$ elements between $x$ and $y$, and for such a chain: exactly one of the two searches succeeds. "At least $n$ elements before $x$" is decided similarly: search at the same time for $n$ elements below $x$, and for a first element $f$ (given by the unary relation) together with a short chain of adjacencies from $f$ to $x$; if there is no first element, the first search succeeds. So each $\psi_{\pi, \bar d}$ is decidable from $\overline{\mathrm{Adj}}$ in every copy, and every $\Sigma^c_1$ formula is decidable from $\overline{\mathrm{Adj}} \oplus \emptyset'$, uniformly once $\emptyset'$ has found the minimal elements. With the parameters of :ref{#thm-akms-chisholm-1}, every r.i.c.e. relation is r.i. computable in $\overline{\mathrm{Adj}} \oplus \emptyset'$, which has the same r.i. degree as $\neg\overline{\mathrm{Adj}} \oplus \emptyset'$. Finally, $\neg\overline{\mathrm{Adj}}$ is r.i.c.e., since each of its three parts is defined by an existential formula (for instance, $y$ is not first if and only if $\exists x\, x < y$), and so is $\emptyset'$.
:::

:::quiz[adjacency and Dickson's lemma]
Why does the proof need the minimal elements of $D$, rather than $D$ itself?

- [x] Because $D$ is infinite, and a disjunction over all its elements would be an infinite disjunction of existential formulas again; finitely many minimal elements give a finite formula in terms of "at least $n$ elements between", which adjacency decides.
- [ ] Because $D$ is not c.e.

  $D$ is c.e.; the issue is to obtain a finite description.
- [ ] Because Dickson's lemma says $D$ is finite.

  Dickson's lemma says every upward closed set has finitely many minimal elements; $D$ itself is usually infinite.
:::

::::exercise{#ex-jump-monotone difficulty=1 objective="Check that the jump of relations respects relative intrinsic computability."}
Show that if $Q \leq_{rT} R$, then $Q' \leq_{rT} R'$.

:::solution
In every copy, $Q^{\mathcal B}$ is computable in $D(\mathcal B) \oplus R^{\mathcal B}$, uniformly up to the finite parameters involved. The $\Sigma^c_1$ facts of $(\mathcal B, Q^{\mathcal B})$ are enumerated by searching for existential witnesses and checking atomic facts about $Q$, which $D(\mathcal B) \oplus R^{\mathcal B}$ decides. So $Q'$ is c.e. in $D(\mathcal B) \oplus R^{\mathcal B}$ for every copy: $Q'$ is r.i.c.e. in $(\mathcal A, R)$. By :ref{#lem-kleene-complete} applied to $(\mathcal A, R)$, every relation r.i.c.e. in $(\mathcal A, R)$ is r.i. computable in $R'$; so $Q' \leq_{rT} R'$.
:::
::::

## Notes and references

The Kleene relation, the jump of relations and :ref{#thm-kleene-not-computable} are from Montalbán (2012); Vatev (2011) proved the theorem for an equivalent notion of jump, through generic copies. :ref{#prop-ld-complete} and :ref{#thm-adj-complete} are Montalbán's Lemmas II.42 and II.43, whose proofs these follow; the relation $\overline{\mathrm{Adj}}$, with first and last elements, is his Definition II.44. The same well-quasi-ordering technique shows that the atom relation is structurally complete on Boolean algebras (Montalbán, Exercise II.46).

- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Chapter II, Sections II.2 and II.3.
- A. Montalbán, *Rice sequences of relations*, Philosophical Transactions of the Royal Society A 370 (2012), 3464–3487.
- S. Vatev, *Conservative extensions of abstract structures*, in *Models of Computation in Context (CiE 2011)*, Lecture Notes in Computer Science 6735, Springer, 2011, 300–309.

:::::exercises
::::exercise{#ex-dlo-complete difficulty=2 objective="Find the complete relation of a structure with effective quantifier elimination: on the rational order, the halting problem alone is complete."}
Let $\mathcal Q = (\mathbb Q; <)$. Using that every existential formula is equivalent in $\mathcal Q$ to a quantifier-free formula, computably found from it (quantifier elimination for dense linear orders without endpoints), show that the relation $\emptyset' \times \{ \langle\rangle \}$ is r.i.c.e. complete on $\mathcal Q$: every r.i.c.e. relation is r.i. computable in $\emptyset'$.

:::solution
Let $\psi(\bar x) = \bigvee_{i \in W} \exists \bar y\, \varphi_i$ be a $\Sigma^c_1$ formula with $k$ free variables. Each disjunct is equivalent to a quantifier-free formula $\chi_i(\bar x)$, computed from $i$. A quantifier-free formula in $\leq$ and $=$ depends only on the **pattern** of $\bar x$: which coordinates are equal and in which order they come. There are finitely many patterns $\rho$ for $k$ variables. The set $P_\psi$ of patterns $\rho$ such that some $\chi_i$ with $i \in W$ holds of the tuples of pattern $\rho$ is decidable from $\emptyset'$, since "some $i \in W$ has $\chi_i$ true at $\rho$" is a $\Sigma^0_1$ question for each of the finitely many $\rho$. Then $\mathcal Q \models \psi(\bar a)$ if and only if the pattern of $\bar a$ is in $P_\psi$, which every copy decides from its diagram. So every $\Sigma^c_1$ formula, uniformly in its index, is decidable in every copy $\mathcal B$ from $D(\mathcal B) \oplus \emptyset'$, and by :ref{#thm-akms-chisholm-1}, with parameters, so is every r.i.c.e. relation. Since $\emptyset'$ is always r.i.c.e., it is r.i.c.e. complete on $\mathcal Q$: the rational order carries no structural information beyond the binary information of $\emptyset'$.
:::
::::
:::::
