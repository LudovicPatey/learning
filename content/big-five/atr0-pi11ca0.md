---
title: Transfinite recursion and Π¹₁ comprehension
summary: Countable well-orderings in second-order arithmetic; the systems ATR₀ and Π¹₁-CA₀; Π¹₁-CA₀ is equivalent to the existence of the set of ill-founded trees in a sequence; a survey of the theorems equivalent to ATR₀ and Π¹₁-CA₀.
duration: 35
prerequisites: [wkl0]
---

The last two systems of the Big Five go beyond the arithmetic sets. $\mathsf{ATR}_0$ allows arithmetic definitions to be iterated along any countable well-ordering, and corresponds to the hyperarithmetic sets studied in the higher computability track. $\Pi^1_1\text{-}\mathsf{CA}_0$ allows definitions by a universal quantifier over sets, and corresponds to the hyperjump. They are needed for the theory of countable well-orderings, for descriptive set theory of the reals, and for parts of the theory of countable abelian groups. This lesson defines both systems, proves one characteristic equivalence, and surveys the rest; most of the proofs are long and are admitted with references.

## Well-orderings

A **countable linear order** is coded by a set $W \subseteq \nat \times \nat$ whose field $F_W = \{ i : (i, i) \in W \}$ is linearly ordered by $i \leq_W j \iff (i, j) \in W$. It is a **well-ordering** if every non-empty subset of its field has a $\leq_W$-least element; in second-order arithmetic, this is expressed by
$$
\mathrm{WO}(W) \equiv \forall X \subseteq F_W\, \big(\exists i\ i \in X \rightarrow \exists i \in X\ \forall j \in X\ i \leq_W j\big),
$$
a $\Pi^1_1$ formula, where $X \subseteq F_W$ abbreviates the arithmetic formula $\forall i\, (i \in X \rightarrow i \in F_W)$. Equivalently, over $\mathsf{ACA}_0$, there is no infinite descending sequence in $F_W$.

For a set $H$ and $j \in F_W$, write $H^{[j]}$ for the column $\{ n : \langle j, n \rangle \in H \}$ and $H^{[<j]} = \{ \langle i, n \rangle \in H : i <_W j \}$.

:::definition{#def-atr0}
Let $\theta(n, j, Y)$ be an arithmetic formula, possibly with other parameters. A set $H$ is a **$\theta$-hierarchy along** $W$ if $H^{[j]} = \{ n : \theta(n, j, H^{[<j]}) \}$ for every $j \in F_W$, and $H$ has no elements outside the columns of $F_W$. **Arithmetic transfinite recursion** is the scheme: for every well-ordering $W$, there is a $\theta$-hierarchy along $W$. $\mathsf{ATR}_0$ is $\mathsf{ACA}_0$ together with this scheme.
:::

The typical instance is the **jump hierarchy**: with $\theta(n, j, Y) \equiv n \in Y'$, the column $j$ is the jump of the join of the previous columns, and the hierarchy iterates the Turing jump along $W$. Along $\omega$, its column $j$ is Turing equivalent to $\emptyset^{(j+1)}$, so the hierarchy is Turing equivalent to $\emptyset^{(\omega)}$ and does not exist in $\mathrm{ARITH}$; so $\mathsf{ACA}_0$ does not prove $\mathsf{ATR}_0$.

:::definition{#def-pi11-ca0}
$\Pi^1_1\text{-}\mathsf{CA}_0$ is $\mathsf{ACA}_0$ together with the comprehension scheme for $\Pi^1_1$ formulas.
:::

Comprehension for $\Pi^1_1$ formulas gives comprehension for $\Sigma^1_1$ formulas, by complementation. $\Pi^1_1\text{-}\mathsf{CA}_0$ proves $\mathsf{ATR}_0$. We sketch the argument and admit the details (Simpson, Section V.1). Let $W$ be a well-ordering and, for $j \in F_W$, call a $\theta$-hierarchy along the initial segment $\{ i : i <_W j \}$ a hierarchy *below* $j$. Two hierarchies below $j$ are equal: otherwise the set of $i$ where their columns differ, which exists by arithmetic comprehension, would have a $<_W$-least element, at which the two columns are defined by $\theta$ from the same previous columns. By $\Sigma^1_1$ comprehension, the set $J$ of $j \in F_W$ having a hierarchy below $j$ exists. If $F_W \setminus J$ were non-empty, its least element $j$ would have hierarchies below every $i <_W j$, unique and therefore compatible, and the set $\{ \langle i, n \rangle : i <_W j \wedge \exists Y\, (Y \text{ is a hierarchy below } i \wedge \theta(n, i, Y)) \}$, which exists by $\Sigma^1_1$ comprehension, would be a hierarchy below $j$. So $J = F_W$, and the same $\Sigma^1_1$ definition without the bound $i <_W j$ gives a $\theta$-hierarchy along $W$. The second exercise below is the case of the jump hierarchy along $\omega$.

## Π¹₁ comprehension and trees

A tree $T \subseteq \nat^{<\nat}$ is **ill-founded** if it has an infinite path, and **well-founded** otherwise. Having a path is a $\Sigma^1_1$ property of $T$. Conversely, every $\Sigma^1_1$ property is of this form.

:::fact[Kleene normal form]{#fact-kleene-normal-form}
For every $\Sigma^1_1$ formula $\varphi(n)$, possibly with parameters, there is a sequence of trees $(T_n)$ in $\nat^{<\nat}$, defined from the parameters by a $\Delta^0_1$ formula, uniformly in $n$, such that $\mathsf{ACA}_0$ proves: for every $n$, $\varphi(n)$ holds if and only if $T_n$ is ill-founded.
:::

The proof introduces Skolem functions for the arithmetic matrix of $\varphi$, which exist by arithmetic comprehension, and codes the set witnessing $\varphi$ together with these functions into a tree of finite approximations; it is admitted here (Simpson, Lemma V.1.4). In the higher computability track, the same normal form, without second-order arithmetic, shows that the $\Sigma^1_1$ sets are the projections of $\Pi^0_1$ classes.

:::theorem{#thm-pi11-trees}
Over $\mathsf{ACA}_0$, $\Pi^1_1\text{-}\mathsf{CA}_0$ is equivalent to the statement: for every sequence of trees $(T_n)$ in $\nat^{<\nat}$, the set $\{ n : T_n \text{ is ill-founded} \}$ exists.
:::

:::proof{of=thm-pi11-trees}
($\Rightarrow$) The set is defined by the $\Sigma^1_1$ formula "$T_n$ has a path", and exists by $\Sigma^1_1$ comprehension, a consequence of $\Pi^1_1$ comprehension.

($\Leftarrow$) Let $\psi(n)$ be $\Pi^1_1$; then $\neg \psi(n)$ is equivalent to a $\Sigma^1_1$ formula. By :ref{#fact-kleene-normal-form}, there is a sequence of trees $(T_n)$, which exists by $\Delta^0_1$ comprehension, such that $\neg \psi(n)$ if and only if $T_n$ is ill-founded. The set $I = \{ n : T_n \text{ is ill-founded} \}$ exists by hypothesis, and $\{ n : \psi(n) \} = \nat \setminus I$ exists by $\Delta^0_1$ comprehension.
:::

In computability-theoretic terms, the set of indices of computable ill-founded trees is $\Sigma^1_1$-complete, and its complement is many-one equivalent to Kleene's $\mathcal O$. The **hyperjump** of $X$ is the set of indices of $X$-computable well-founded trees. An ω-model $\mathcal M$ of $\Pi^1_1\text{-}\mathsf{CA}_0$ contains, for each $X \in \mathcal M$, the set of indices of $X$-computable trees with no path in $\mathcal M$. When $\mathcal M$ is a **β-model**, that is, when every tree of $\mathcal M$ with a path has a path in $\mathcal M$, this set is the hyperjump of $X$, and $\mathcal M$ is closed under the hyperjump. An arbitrary ω-model of $\Pi^1_1\text{-}\mathsf{CA}_0$ need not be: the intersection of all of them is the class $\mathrm{HYP}$ of hyperarithmetic sets, which does not contain $\mathcal O$, a result of Gandy, Kreisel and Tait that we admit (Simpson, Chapter VIII).

:::quiz[Π¹₁ comprehension]
Why is the statement of :ref{#thm-pi11-trees} about **sequences** of trees rather than single trees?

- [x] Because a set of indices is needed: for a single tree, "it is ill-founded" is a single true or false statement, not a set to be formed.
- [ ] Because single trees always have paths.

  Well-founded trees have no path; the issue is what comprehension produces.
- [ ] Because sequences of trees are not arithmetic.

  A sequence of trees is a set like any other.

---

In the direction ($\Leftarrow$), where is arithmetic comprehension used?

- [x] In the normal form, to prove that $\neg \psi(n)$ implies that $T_n$ is ill-founded: the Skolem functions for the arithmetic matrix, which form a path of $T_n$ together with the witnessing set, exist by arithmetic comprehension.
- [ ] To form the sequence of trees.

  The trees are defined from the parameters by a $\Delta^0_1$ formula, uniformly in $n$; they exist by $\Delta^0_1$ comprehension.
- [ ] To decide whether each tree is well-founded.

  This is a $\Pi^1_1$ question, answered by the hypothesis, not by arithmetic comprehension.
- [ ] To take the complement of $I$.

  The complement is formed by $\Delta^0_1$ comprehension.
:::

## A survey of equivalents

The following equivalences over $\mathsf{RCA}_0$ are due to Friedman, Simpson, Steel and others; they are admitted here, with the references of Simpson's monograph.

| System | Equivalent statements |
| --- | --- |
| $\mathsf{ATR}_0$ | any two countable well-orderings are comparable (Friedman); every uncountable closed subset of $\mathbb R$ has a perfect subset; $\Sigma^1_1$ separation; Lusin's separation theorem; Ulm's theorem for countable reduced abelian $p$-groups (Chapter V) |
| $\Pi^1_1\text{-}\mathsf{CA}_0$ | the Cantor–Bendixson theorem: every closed subset of $\mathbb R$ is the union of a perfect set and a countable set; every countable abelian group is the direct sum of a divisible group and a reduced group; every tree in $\nat^{<\nat}$ has a perfect kernel (Chapter VI) |

The ω-models of these systems are studied with the tools of higher computability. The class $\mathrm{HYP}$ is also the intersection of all ω-models of $\mathsf{ATR}_0$, but is not itself a model: there are computable linear orders that have no hyperarithmetic descending sequence but are not well-orderings, the **pseudo-well-orderings**, and they prevent $\mathrm{HYP}$ from satisfying arithmetic transfinite recursion. Consequently $\mathsf{ATR}_0$ has no least ω-model. The failure of arithmetic transfinite recursion in $\mathrm{HYP}$ is discussed in the course on hyperarithmetic sets (:ref{to="hyperarithmetic/sigma11-classes"}); we admit these results (Simpson, Chapter VIII).

The five systems are linearly ordered by strength:
$$
\mathsf{RCA}_0 \subsetneq \mathsf{WKL}_0 \subsetneq \mathsf{ACA}_0 \subsetneq \mathsf{ATR}_0 \subsetneq \Pi^1_1\text{-}\mathsf{CA}_0,
$$
where each inclusion is strict. The first three separations were proved with ω-models: $\mathrm{REC}$ (:ref{#cor-rca-not-wkl}), a Scott ideal of low sets (:ref{#thm-low-scott}), and $\mathrm{ARITH}$. The last one holds because $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the existence of an ω-model of $\mathsf{ATR}_0$, hence the consistency of $\mathsf{ATR}_0$; we admit it (Simpson, Section VII.2).

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{ATR}_0$ proves that for every set $X$, the ω-jump $X^{(\omega)} = \bigoplus_n X^{(n)}$ exists.

:::solution
The order $\omega$, coded by $\{ (i, j) : i \leq j \}$, exists and is a well-ordering: a non-empty set of numbers has a least element, by $\Sigma^0_1$ induction. Let
$$
\theta(n, j, Y) \equiv (j = 0 \wedge n \in X) \vee \big(j > 0 \wedge \Phi^{Y^{[j-1]}}_n(n)\converge\big),
$$
an arithmetic formula. A $\theta$-hierarchy $H$ along $\omega$ satisfies $H^{[0]} = X$ and $H^{[j+1]} = (H^{[j]})'$, since the columns of $H^{[<j+1]}$ are those of $H$ below $j+1$. By arithmetic induction, $H^{[j]} = X^{(j)}$ for every $j$, so $H = X^{(\omega)}$.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{ACA}_0$ together with $\Sigma^1_1$ comprehension proves that $X^{(\omega)}$ exists for every $X$.

:::solution
Call $Y$ a **jump sequence of length $n$** for $X$ if $Y^{[0]} = X$, $Y^{[k+1]} = (Y^{[k]})'$ for $k < n$, and $Y$ has no other columns; this is an arithmetic property of $Y$ and $n$. By arithmetic induction, any two jump sequences of length $n$ are equal. The $\Sigma^1_1$ formula $\exists Y\, (Y \text{ is a jump sequence of length } n)$ holds for $n = 0$, and if $Y$ is one of length $n$, the set obtained by adding the column $(Y^{[n]})'$, which exists by arithmetic comprehension, is one of length $n + 1$. Induction for this $\Sigma^1_1$ formula follows from $\Sigma^1_1$ comprehension and the induction axiom (:ref{#prop-induction-comprehension}), so jump sequences of every length exist. Now
$$
\{ \langle n, e \rangle : \exists Y\, (Y \text{ is a jump sequence of length } n \wedge e \in Y^{[n]}) \}
$$
exists by $\Sigma^1_1$ comprehension, and it is $X^{(\omega)}$.
:::
::::

## Notes and references

Friedman introduced $\mathsf{ATR}_0$ and proved the equivalence with the comparability of well-orderings. Simpson's monograph covers both systems in Chapters V and VI, and their ω-models in Chapters VII and VIII. Montalbán's survey discusses the many theorems of $\mathsf{ATR}_0$ strength found since.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009.
- H. Friedman, *Systems of second order arithmetic with restricted induction*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- A. Montalbán, *Open questions in reverse mathematics*, Bulletin of Symbolic Logic 17 (2011), 431–454.
