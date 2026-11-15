---
title: Arithmetic with a top
summary: Initial segments [0, a] of models of arithmetic as structures with a top element, and their coded expansions; truth in a coded expansion is computed by bounded formulas, and the least number principle holds for all formulas; every model of arithmetic with a top is an initial segment of a model of bounded induction (Paris); cuts in such structures, k-Ramsey, k-extendable and k-restrainable cuts, and the indicators for BΣₖ₊₁ (Paris), stated.
duration: 45
prerequisites: [ph-unprovable, cuts-and-extensions/wkl-regular-cuts, truth-and-provability/bounded-satisfaction]
---

All the constructions of this course take place inside a bounded interval. The cut of :ref{#thm-kirby-paris-cut} lies below $F_\nu(a)$ and uses only coded functions with values below it; the indiscernibles of :ref{#thm-ph-indicator} lie in $[a, b]$; and the combinatorial statements themselves, such as $[a, b] \to_* (k)^n_c$, speak about $[0, b]$ and its coded subsets. Paris made this explicit by studying **models of arithmetic with a top**: structures $[0, a]$, finite from the point of view of the surrounding model but possibly with a non-standard top $a$, in which addition and multiplication are partial. This lesson presents the framework, proves its basic property, and describes, without proofs, how Paris and Hájek–Pudlák use it to obtain indicators for every level of the hierarchy of fragments.

## Initial segments with a top

Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $a \in M$. The set $[0, a]$ is a structure for the language $\mathcal L_{\mathrm{top}} = \{ +, \times, <, \top \}$, in which $+$ and $\times$ are ternary relations ($x + y = z$ holds when $x, y, z \leq a$ and the equation holds in $M$), $<$ is the order, and the constant $\top$ denotes $a$. Addition and multiplication are partial: $a + 1$ does not exist in $[0, a]$.

:::definition{#def-coded-expansion}
An **$M$-coded expansion** of $[0, a]$ is a structure $A = ([0, a], R_1, \dots, R_m)$ for a finite language $\mathcal L \supseteq \mathcal L_{\mathrm{top}}$, where each $R_i \subseteq [0, a]^{n_i}$ is coded in $M$: $R_i = \{ \bar x \leq a : \langle \bar x \rangle \in r_i \}$ for some $r_i \in M$ (:ref{#def-ack-membership}).
:::

:::example{#ex-coded-expansion}
1. A coloring $f : [[0, a]]^n \to c$ coded in $M$, with $c \leq a$, gives the coded expansion $([0, a], G_f)$, where $G_f$ is the graph of $f$ on increasing tuples.
2. The relation $[x, b] \to_* (k)^n_c$, for $x, k, n, c \leq b$, quantifies over colorings of $[[x, b]]^n$ and subsets of $[x, b]$. A subset of $[0, b]$ is coded by a number below $2^{b+1}$, so these objects are elements of $[0, 2^{b+1}]$ rather than of $[0, b]$. Statements about the coded subsets of $[0, b]$, and about the colorings of $[[x, b]]^n$, are first-order statements about a larger structure $[0, e]$, where $e$ is given by a term in exponentiation from $b$ and the codes live.
:::

The top element bounds every quantifier. So truth in a coded expansion reduces to bounded truth in $M$, which is why the structure behaves well even when $a$ is non-standard.

:::proposition[Lessan]{#prop-top-truth}
Let $M \models \mathrm I\Delta_0 + \mathrm{exp}$, $a \in M$, and $A$ an $M$-coded expansion of $[0, a]$ given by codes $\bar r$. For every formula $\theta(\bar x)$ of $\mathcal L$ there is a bounded formula $\hat\theta(u, \bar w, \bar x)$ of $\mathcal L_A$ such that for all $\bar x \leq a$,
$$
A \models \theta(\bar x) \iff M \models \hat\theta(a, \bar r, \bar x).
$$
Consequently $A$ satisfies the least number principle for all formulas of $\mathcal L$, with parameters: if $A \models \theta(x, \bar z)$ for some $x$, there is a least such $x$.
:::

:::proof{of=prop-top-truth}
Define $\hat\theta$ by recursion on $\theta$, with the variable $u$ standing for $a$ and $w_i$ for $r_i$: the atomic formulas $x + y = z$, $x \times y = z$ and $x < y$ are translated by themselves, $x = \top$ by $x = u$, and $R_i(\bar x)$ by $\langle \bar x \rangle \in w_i$; connectives are kept, and $\forall y\ \theta$ becomes $\forall y < u + 1\ \hat\theta$, and similarly for $\exists$. The equivalence holds for atomic formulas since $A$ is a substructure of $M$ for the relations, and the codes $r_i$ define the $R_i$; it passes through connectives, and through quantifiers because the elements of $A$ are exactly the elements of $M$ below $a + 1$.

For the least number principle, let $A \models \theta(x_1, \bar z)$. Then $M \models \hat\theta(a, \bar r, x_1, \bar z)$, a bounded formula, and by the least number principle for bounded formulas in $M$ (:ref{#prop-idelta0-basic}) there is a least $x_0 \leq x_1$ with $M \models \hat\theta(a, \bar r, x_0, \bar z)$. By the equivalence, $x_0$ is the least element of $A$ satisfying $\theta(\cdot, \bar z)$.
:::

The proposition concerns standard formulas $\theta$. With the bounded satisfaction formula $\mathrm{Sat}_0$ of :ref{to="truth-and-provability/bounded-satisfaction"}, the translation can be applied to non-standard formulas: in a model of $\mathrm I\Sigma_1$, satisfaction in $A$ is $\Delta_1$, uniformly in the code of the formula, and the least number principle holds for non-standard formulas as well (Wong, Proposition 13.1, after Lessan). With overspill this also shows that $A$ is recursively saturated when $a$ is non-standard; recursive saturation is studied in another course of this track.

:::quiz[truth with a top]
In the proof of :ref{#prop-top-truth}, why is the least number principle available in $A$ for *all* formulas, although $M$ only satisfies bounded induction?

- [x] Every formula of $A$ is translated into a bounded formula of $M$, because every quantifier of $A$ ranges below $a + 1$; the least number principle of $M$ for bounded formulas then applies.
- [ ] Because $A$ is finite.

  If $a$ is non-standard, $A$ is infinite; it is finite only from the point of view of $M$.
- [ ] Because $A$ is a model of $\mathrm{PA}$.

  $A$ is not even closed under successor; the axioms of $\mathrm{PA}$ make no sense in it.
:::

## Arithmetic with a top as a theory

Hájek and Pudlák (Chapter I, Section 2(e), and Chapter IV, Section 2(a)) axiomatize these structures. The theory $\mathrm{TA}'$, **arithmetic with a top**, in the relational language, says that $<$ is a discrete linear order with a least and a largest element, that successor, addition and multiplication are partial functions obeying the usual recursion equations where they are defined, and that the least number principle holds for all bounded formulas of the relational language (here every formula is equivalent to a bounded one, because of the top). By :ref{#prop-top-truth}, whose proof for the language $\mathcal L_{\mathrm{top}}$ without coded relations uses only $\mathrm I\Delta_0$, every $[0, a]$ in a model of $\mathrm I\Delta_0$ is a model of $\mathrm{TA}'$. The converse is due to Paris.

:::theorem[Paris]{#thm-top-segment}
Every model $B$ of $\mathrm{TA}'$ is isomorphic to an initial segment $[0, a]$ of a model $K$ of $\mathrm I\Delta_0$.
:::

We admit this theorem. The model $K$ consists of the finite sequences, of standard length, of elements of $B$, read as numbers written in base $a$, where $a$ is the top of $B$, with the elements of $B$ below $a$ as digits; its order is lexicographic, and addition and multiplication are computed by the school algorithms, with carries. The structures $B_n$ of sequences of length at most $n$ are definable in $B$ with $n$-tuples, so bounded induction in $K$ reduces to the least number principle in $B$ (Hájek and Pudlák, Theorem IV.2.2 and Lemmas 2.5–2.7; Wong, Lecture 13, Further exercises). As a consequence, $\mathrm{TA}'$ and bounded induction prove the same sentences of a restricted syntactic form (Hájek and Pudlák, Corollary IV.2.3), which is how arithmetic with a top is used in bounded arithmetic.

## Cuts in models with a top

A **cut** of a model $B$ of $\mathrm{TA}'$ is a nonempty initial segment with no largest element; it is **short** if it is closed under addition and multiplication and, for some $a \in B$ above the cut, $2^{2^a}$ exists in $B$, so that the subsets of $[0, a]$ and the functions on them are coded in $B$ (Hájek and Pudlák, Definition IV.2.10). The notions of :ref{to="cuts-and-extensions/semiregular-cuts"} transfer: the coded subsets $\mathrm{Cod}(B/I)$ of a short cut $I$, semiregularity, and the theorem that a short cut is semiregular if and only if it satisfies $\Sigma_1$ induction with coded set parameters (Hájek and Pudlák, Theorem IV.2.16). This is the setting in which :ref{#thm-kirby-paris-cut} takes place: its cut is a short cut of $[0, F_\nu(a)]$: if no element above the cut satisfied $2^{2^y} \leq F_\nu(a)$, the largest $y$ with $2^{2^y} \leq F_\nu(a)$ would be in the cut, and so would $2^{2^{y+1}} > F_\nu(a)$, since the cut satisfies $\mathrm I\Sigma_1$.

Paris introduced finer notions to obtain cuts satisfying $\mathrm B\Sigma_{k+1}$. For a coded set $X \subseteq I^{k+1}$, "$X$ is $(k+1)$-unbounded in $I$" means that the set of $x_0$ such that $\{ (x_1, \dots, x_k) : (x_0, \dots, x_k) \in X \}$ is $k$-unbounded is unbounded in $I$, with 1-unbounded meaning unbounded.

:::definition[Paris]{#def-ramsey-cut}
Let $I$ be a short cut of a model $B$ of $\mathrm{TA}'$ and $k \geq 1$.

1. $I$ is **$k$-Ramsey** if for every $a \in I$ and every coded $F : I^k \to [0, a)$ some $F^{-1}(j)$ is $k$-unbounded in $I$.
2. A **$k$-extending chain** over $I$ is a sequence $K_0 \prec_I K_1 \prec_I \cdots \prec_I K_k$ of models of $\mathrm{TA}'$ in which $I$ is a short cut, each $K_i$ is a $\Delta_0$-elementary substructure of $K_{i+1}$, no new element is added below the elements of $I$, and some new element is added between $I$ and $K_i \setminus I$. $I$ is **$k$-extendable** over $M$ if there is such a chain with $K_0 = M$, and **$k$-restrainable** in $M$ if there is one with $K_k = M$.
:::

The $1$-Ramsey cuts are the regular cuts of :ref{#def-regular-cut}. The following theorem is the base of Paris's indicators; we admit it.

:::theorem[Paris]{#thm-ramsey-cuts}
Let $I$ be a short cut of a model of $\mathrm{TA}'$ and $k \geq 1$.

1. $I$ is $k$-Ramsey if and only if $I$ satisfies $\mathrm B\Sigma_{k+1}$ with coded set parameters.
2. If $I$ is $k$-extendable or $k$-restrainable, then $I$ is $k$-Ramsey, hence $I \models \mathrm B\Sigma_{k+1}$.
:::

Item 1 is Hájek and Pudlák, Theorem IV.2.21, which combines Ramsey-type principles for coded sets with the equivalence of Lemma IV.2.18; for $k = 1$ it is the characterization of regular cuts stated in :ref{to="cuts-and-extensions/wkl-regular-cuts"}. Item 2 is Theorem IV.2.22 and the discussion in IV.3.11, IV.3.14–3.15. Restrainable cuts are built by **Paris sequences**: inside $[a, b]$, a sequence $g$ of non-standard length and a $k$-tuple $h$ above it such that each element $h_j$ cannot be defined, by small formulas with parameters from an initial part of $g$ and from $h_{j+1}, \dots, h_{k-1}$, between $g$ and $h_j$. These are a form of the diagonal indiscernibles of lesson 6, adapted to a fixed number $k$ of levels.

:::theorem[Paris]{#thm-paris-bsigma-indicator}
For each $k \geq 1$, the formula "$[x, y] \to_* (k + 2)^{k+1}_c$", with $c$ the number of colors, gives, after the normalization of :ref{#def-indicator}, an indicator both for $\mathrm I\Sigma_k$ and for $\mathrm B\Sigma_{k+1}$. Consequently $\mathrm I\Sigma_k$ does not prove $\forall x\ \forall c\ \exists y\ [x, y] \to_* (k + 2)^{k+1}_c$, and the functions $x \mapsto$ least $y$ with $[x, y] \to_* (k+2)^{k+1}_n$, $n \in \nat$, bound all functions provably total in $\mathrm I\Sigma_k$.
:::

This is Hájek and Pudlák, Theorem IV.3.20 and Corollary IV.3.21, admitted here. Together with :ref{#thm-ph-indicator}, it gives the level-by-level picture announced in lesson 7: colorings of $(k+1)$-sets with relatively large homogeneous sets mark the strength of $\mathrm I\Sigma_k$, and all arities together the strength of $\mathrm{PA}$.

## Exercises

::::exercise{#ex-top-no-definable-cut difficulty=1 objective="Derive from the least number principle in $[0, a]$ that it has no proper definable cut."}
Let $M \models \mathrm I\Delta_0 + \mathrm{exp}$ and $a \in M$ non-standard. Show that $[0, a]$, as an $\mathcal L_{\mathrm{top}}$-structure, has no proper definable cut: no formula $\theta(x, \bar z)$ with parameters defines in $[0, a]$ an initial segment closed under successor other than $[0, a]$. Deduce that the standard part $\nat$ is not definable in $[0, a]$.

:::solution
Let $C$ be defined by $\theta(x, \bar z)$, an initial segment with $x + 1 \in C$ for every $x \in C$ with $x < a$, and suppose $C \neq [0, a]$. By :ref{#prop-top-truth}, the complement of $C$, defined by $\neg \theta$, has a least element $x_0$; $x_0 \neq 0$ since $C$ is nonempty, and $x_0 - 1 \in C$ gives $x_0 \in C$. The standard part is an initial segment closed under successor, and it is proper since $a$ is non-standard; so it is not definable.
:::
::::

## Notes and references

Initial segments with a top and the least number principle for them go back to Lessan's thesis (1978); the presentation follows Wong's Lecture 13 (Proposition 13.1 and the Further exercises, with Theorem 13.11, credited there to Paris through Cégielski, McAloon and Wilmers) and Hájek and Pudlák, Chapter IV, Section 2. Extendable, restrainable and Ramsey cuts, Paris sequences and the indicators for $\mathrm B\Sigma_{k+1}$ are due to Paris (1980, 1981); they are in Hájek and Pudlák, Chapter IV, Sections 2(c) and 3(b)–(c). Wong's Lecture 13 continues with Ajtai's completeness theorem for definable proofs in structures with a top and its application to the complexity of the parity function (Ajtai 1983, 2007; Garlík), which belong to the interface with complexity theory.

- J. B. Paris, *A hierarchy of cuts in models of arithmetic*, in Model Theory of Algebra and Arithmetic, Lecture Notes in Mathematics 834, Springer, 1980, 312–337.
- J. B. Paris, *Some conservation results for fragments of arithmetic*, in Model Theory and Arithmetic, Lecture Notes in Mathematics 890, Springer, 1981, 251–262.
- P. Cégielski, K. McAloon and G. Wilmers, *Modèles récursivement saturés de l'addition et de la multiplication des entiers naturels*, in Logic Colloquium '80, North-Holland, 1982, 57–68.
- H. Lessan, *Models of arithmetic*, PhD thesis, University of Manchester, 1978.
- M. Ajtai, *Σ¹₁-formulae on finite structures*, Annals of Pure and Applied Logic 24 (1983), 1–48.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Sections 2 and 3.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 13.

:::::exercises
::::exercise{#ex-top-induction difficulty=1 objective="Derive an induction scheme up to the top from the least number principle in a structure with a top."}
Let $A = [0, a]$ be an $M$-coded expansion, with $M \models \mathrm I\Delta_0 + \mathrm{exp}$, and $\theta(x, \bar z)$ a formula of $\mathcal L$ with parameters in $A$. Suppose that $A \models \theta(0, \bar z)$ and that, for every $x < a$, $A \models \theta(x, \bar z)$ implies $A \models \theta(x + 1, \bar z)$. Show that $A \models \theta(x, \bar z)$ for every $x \in A$, in particular for $x = a$.

:::solution
Otherwise $\neg \theta(\cdot, \bar z)$ has a solution in $A$, hence a least one $x_0$, by :ref{#prop-top-truth}. Then $x_0 \neq 0$, so $x_0 = x + 1$ with $x < x_0 \leq a$, and $A \models \theta(x, \bar z)$ by minimality; the hypothesis gives $A \models \theta(x_0, \bar z)$, a contradiction. The successor $x + 1$ exists in $A$ because $x < a$, and the clause &quot;$\theta(x + 1)$&quot; is written in the relational language as $\exists y\ (x + 1 = y \wedge \theta(y))$, where $1$ is definable as the least element above $0$.
:::
::::

::::exercise{#ex-top-definable-elements difficulty=1 objective="Write definitions without parameters of elements near the top and of halves and square roots of the top, in the relational language."}
Let $a \geq 2$. Show that the elements $a - n$ for standard $n \leq a$, the integer part of $a / 2$ and the integer part of $\sqrt a$ are definable in the $\mathcal L_{\mathrm{top}}$-structure $[0, a]$ without parameters.

:::solution
$0$ is the least element and $1$ the least element above $0$. The element $a - 1$ is the unique $x$ with $x + 1 = \top$, and by induction in the metatheory, $a - (n + 1)$ is the unique $x$ with $x + 1 = a - n$, using the definition of $a - n$. The integer part of $a / 2$ is the unique $x$ such that $\exists y\ (x + x = y \wedge (y = \top \vee y + 1 = \top))$: $x + x$ must exist and be $a$ or $a - 1$. The integer part of $\sqrt a$ is the unique $x$ such that $\exists z\ (x \times x = z)$ and $\neg \exists w\ \exists z\ (x + 1 = w \wedge w \times w = z)$: the first clause says $x^2 \leq a$; the integer part $r$ of $\sqrt a$ satisfies $r + 1 \leq a$ and $(r + 1)^2 > a$, so it satisfies both clauses; any $x$ satisfying the first clause has $x \leq r$ (and $x < a$, since $a^2 > a$), so $x + 1$ exists, and the second clause forces $(x + 1)^2 > a$, that is $x \geq r$.
:::
::::

::::exercise{#ex-top-overspill difficulty=1 objective="Derive overspill in a structure with a non-standard top from the absence of definable proper cuts."}
Let $M \models \mathrm I\Delta_0 + \mathrm{exp}$, $a \in M$ non-standard, and $\theta(x, \bar z)$ a formula of $\mathcal L_{\mathrm{top}}$ with parameters in $[0, a]$ such that $[0, a] \models \theta(n, \bar z)$ for every standard $n$. Show that $[0, a] \models \theta(x, \bar z)$ for some non-standard $x$.

:::solution
Let $D = \{ x \leq a : [0, a] \models \forall y \leq x\ \theta(y, \bar z) \}$, a definable initial segment that contains every standard number. If $D$ contained only standard numbers, it would be the standard part, which is closed under successor and proper; by :ref{#ex-top-no-definable-cut} it is not definable, a contradiction. So $D$ contains a non-standard $x$, and $[0, a] \models \theta(x, \bar z)$.
:::
::::

::::exercise{#ex-top-ramsey-monotone difficulty=2 objective="Unfold the definition of $k$-Ramsey cuts, and show that $2$-Ramsey cuts are $1$-Ramsey by a coloring that ignores a coordinate."}
Let $I$ be a short cut of a model $B$ of $\mathrm{TA}'$. Show that a set $X \subseteq I^2$ of the form $I \times Y$ is $2$-unbounded in $I$ if and only if $Y$ is unbounded in $I$, and that $X = \{ (x_0, x_1) : x_1 < x_0 \}$ is not $2$-unbounded. Deduce that every $2$-Ramsey cut is $1$-Ramsey.

:::solution
For $X = I \times Y$, every section $\{ x_1 : (x_0, x_1) \in X \}$ is $Y$. If $Y$ is unbounded, the set of $x_0$ with an unbounded section is $I$, which is unbounded; otherwise it is empty. For $X = \{ (x_0, x_1) : x_1 < x_0 \}$, each section is bounded by $x_0 \in I$, so no section is unbounded.

Let $I$ be $2$-Ramsey, $a \in I$ and $F : I \to [0, a)$ coded. Let $F'(x_0, x_1) = F(x_1)$; it is coded, its graph being obtained from that of $F$ by a bounded definition. Some $F'^{-1}(j) = I \times F^{-1}(j)$ is $2$-unbounded, so $F^{-1}(j)$ is unbounded in $I$, by the first part. So $I$ is $1$-Ramsey.
:::
::::
:::::
