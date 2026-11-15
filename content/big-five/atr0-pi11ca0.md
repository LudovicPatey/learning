---
title: Transfinite recursion and Π¹₁ comprehension
summary: Countable well-orderings in second-order arithmetic; the systems ATR₀ and Π¹₁-CA₀; Π¹₁-CA₀ is equivalent to the existence of the set of ill-founded trees in a sequence; a survey of the theorems equivalent to ATR₀ and Π¹₁-CA₀.
duration: 50
prerequisites: [wkl0]
---

The last two systems of the Big Five go beyond the arithmetic sets. $\mathsf{ATR}_0$ allows arithmetic definitions to be iterated along any countable well-ordering, and corresponds to the hyperarithmetic sets studied in the higher computability track. $\Pi^1_1\text{-}\mathsf{CA}_0$ allows definitions by a universal quantifier over sets, and corresponds to the hyperjump. They are needed for the theory of countable well-orderings, for descriptive set theory of the reals, and for parts of the theory of countable abelian groups. This lesson defines both systems, proves one characteristic equivalence, and surveys the rest; most of the proofs are long and are admitted with references.

## Well-orderings

A **countable linear order** is coded by a set $W \subseteq \nat \times \nat$ whose field $F_W = \{ i : (i, i) \in W \}$ is linearly ordered by $i \leq_W j \iff (i, j) \in W$. It is a **well-ordering** if every non-empty subset of its field has a $\leq_W$-least element; in second-order arithmetic, this is expressed by
$$
\mathrm{WO}(W) \equiv \forall X \subseteq F_W\, \big(\exists i\ i \in X \rightarrow \exists i \in X\ \forall j \in X\ i \leq_W j\big),
$$
a $\Pi^1_1$ formula, where $X \subseteq F_W$ abbreviates the arithmetic formula $\forall i\, (i \in X \rightarrow i \in F_W)$. Equivalently, over $\mathsf{ACA}_0$, there is no infinite descending sequence in $F_W$.

**Examples.** The order $\omega$ is coded by $\{ (i, j) : i \leq j \}$. The order $\omega + \omega$ is coded by putting the even numbers, in their usual order, before the odd numbers: $2i \leq_W 2j + 1$ for all $i, j$, and the usual order inside each half. Both are well-orderings. The order $\omega^*$, coded by $\{ (i, j) : j \leq i \}$, is a computable linear order that is not a well-ordering: $\nat$ itself has no least element. More interesting are computable linear orders with no computable descending sequence that are nevertheless not well-orderings; they are the source of the subtleties of $\mathsf{ATR}_0$, and reappear at the end of the lesson.

**Intuition.** Arithmetic comprehension applies an arithmetic operator, such as the jump, once; finitely many applications are obtained by repeating it. To apply the jump $\omega$ times, and then again, one needs a single set that records all the stages, column by column, together with the condition that each column is obtained from the previous ones. The index set of the columns must be well-ordered: the condition at column $j$ refers to the columns below $j$, and only along a well-ordering does this recursion determine a unique set. Along an ill-founded order, the conditions may have no solution, or many.

For a set $H$ and $j \in F_W$, write $H^{[j]}$ for the column $\{ n : \langle j, n \rangle \in H \}$ and $H^{[<j]} = \{ \langle i, n \rangle \in H : i <_W j \}$.

:::definition{#def-atr0}
Let $\theta(n, j, Y)$ be an arithmetic formula, possibly with other parameters. A set $H$ is a **$\theta$-hierarchy along** $W$ if $H^{[j]} = \{ n : \theta(n, j, H^{[<j]}) \}$ for every $j \in F_W$, and $H$ has no elements outside the columns of $F_W$. **Arithmetic transfinite recursion** is the scheme: for every well-ordering $W$, there is a $\theta$-hierarchy along $W$. $\mathsf{ATR}_0$ is $\mathsf{ACA}_0$ together with this scheme.
:::

The typical instance is the **jump hierarchy**: with $\theta(n, j, Y) \equiv n \in Y'$, the column $j$ is the jump of the join of the previous columns, and the hierarchy iterates the Turing jump along $W$. Along $\omega$, its column $j$ is Turing equivalent to $\emptyset^{(j+1)}$, so the hierarchy is Turing equivalent to $\emptyset^{(\omega)}$ and does not exist in $\mathrm{ARITH}$; so $\mathsf{ACA}_0$ does not prove $\mathsf{ATR}_0$.

:::figure[A jump hierarchy along the well-ordering $\omega + 2$, coded for instance by putting two numbers after all the others. Column $j$ is the jump of the join of the columns below $j$. Column $\omega$ is the first one that is not defined from finitely many earlier columns: it is the jump of the join of all of them, and computes $\emptyset^{(\omega)}$.]
<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="A jump hierarchy along the well-ordering omega+2: each column is the jump of the join of the previous columns"><defs><marker id="ah-jh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="40" y1="150" x2="560" y2="150" class="axis"/><rect x="54" y="58" width="32" height="84" class="cell"/><line x1="70" y1="146" x2="70" y2="154" class="ink-stroke" stroke-width="1"/><text x="70" y="172" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="114" y="58" width="32" height="84" class="cell"/><line x1="130" y1="146" x2="130" y2="154" class="ink-stroke" stroke-width="1"/><text x="130" y="172" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="174" y="58" width="32" height="84" class="cell"/><line x1="190" y1="146" x2="190" y2="154" class="ink-stroke" stroke-width="1"/><text x="190" y="172" text-anchor="middle" class="mrm" font-size="14">2</text><rect x="234" y="58" width="32" height="84" class="cell"/><line x1="250" y1="146" x2="250" y2="154" class="ink-stroke" stroke-width="1"/><text x="250" y="172" text-anchor="middle" class="mrm" font-size="14">3</text><rect x="404" y="58" width="32" height="84" class="cell head-cell"/><line x1="420" y1="146" x2="420" y2="154" class="ink-stroke" stroke-width="1"/><text x="420" y="172" text-anchor="middle" class="mrm" font-size="14">ω</text><rect x="484" y="58" width="32" height="84" class="cell"/><line x1="500" y1="146" x2="500" y2="154" class="ink-stroke" stroke-width="1"/><text x="500" y="172" text-anchor="middle" class="mrm" font-size="14">ω+1</text><text x="335" y="104" text-anchor="middle" class="mrm" font-size="16">⋯</text><text x="335" y="172" text-anchor="middle" class="mrm" font-size="14">⋯</text><path d="M54,50 L54,42 L266,42 L266,50" class="muted-stroke" fill="none" stroke-width="1"/><text x="160" y="34" text-anchor="middle" class="label">the columns j &lt; ω</text><path d="M266,46 C330,46 400,34 418,52" class="accent-stroke" fill="none" stroke-width="1.4" marker-end="url(#ah-jh)"/><text x="420" y="28" text-anchor="middle" class="label">column ω: the jump of their join</text><path d="M430,52 Q465,34 494,52" class="ink-stroke" fill="none" stroke-width="1.2" marker-end="url(#ah-jh)"/></svg>
:::

Uniqueness is the key to the theory. Two $\theta$-hierarchies along the same well-ordering are equal: otherwise the set of $j$ at which their columns differ exists by arithmetic comprehension, and at its $\leq_W$-least element the two columns are defined by $\theta$ from the same earlier columns. This argument, induction along $W$ for an arithmetic property, is **arithmetic transfinite induction**, valid in $\mathsf{ACA}_0$ (Simpson, Lemma V.2.1); it recurs in every proof about hierarchies.

:::definition{#def-pi11-ca0}
$\Pi^1_1\text{-}\mathsf{CA}_0$ is $\mathsf{ACA}_0$ together with the comprehension scheme for $\Pi^1_1$ formulas.
:::

Comprehension for $\Pi^1_1$ formulas gives comprehension for $\Sigma^1_1$ formulas, by complementation. $\Pi^1_1\text{-}\mathsf{CA}_0$ proves $\mathsf{ATR}_0$; Simpson states it in Section I.11, and it also follows from his Theorem V.5.1, since $\Sigma^1_1$ separation is a consequence of $\Sigma^1_1$ comprehension. We sketch a direct argument and admit the details. Let $W$ be a well-ordering and, for $j \in F_W$, call a $\theta$-hierarchy along the initial segment $\{ i : i <_W j \}$ a hierarchy *below* $j$. Two hierarchies below $j$ are equal, by arithmetic transfinite induction as above. By $\Sigma^1_1$ comprehension, the set $J$ of $j \in F_W$ having a hierarchy below $j$ exists. If $F_W \setminus J$ were non-empty, its least element $j$ would have hierarchies below every $i <_W j$, unique and therefore compatible, and the set $\{ \langle i, n \rangle : i <_W j \wedge \exists Y\, (Y \text{ is a hierarchy below } i \wedge \theta(n, i, Y)) \}$, which exists by $\Sigma^1_1$ comprehension, would be a hierarchy below $j$. So $J = F_W$, and the same $\Sigma^1_1$ definition without the bound $i <_W j$ gives a $\theta$-hierarchy along $W$. :ref{#ex-sigma11-omega-jump} is the case of the jump hierarchy along $\omega$.

::::exercise{#ex-atr-omega-jump difficulty=1 objective="Apply arithmetic transfinite recursion along $\omega$ to the jump, to obtain the ω-jump of any set."}
Show that $\mathsf{ATR}_0$ proves that for every set $X$, the ω-jump $X^{(\omega)} = \bigoplus_n X^{(n)}$ exists.

:::solution
The order $\omega$, coded by $\{ (i, j) : i \leq j \}$, exists and is a well-ordering: a non-empty set of numbers has a least element, by $\Sigma^0_1$ induction. Let
$$
\theta(n, j, Y) \equiv (j = 0 \wedge n \in X) \vee \big(j > 0 \wedge \Phi^{Y^{[j-1]}}_n(n)\converge\big),
$$
an arithmetic formula. A $\theta$-hierarchy $H$ along $\omega$ satisfies $H^{[0]} = X$ and $H^{[j+1]} = (H^{[j]})'$, since the columns of $H^{[<j+1]}$ are those of $H$ below $j+1$. By arithmetic induction, $H^{[j]} = X^{(j)}$ for every $j$, so $H = X^{(\omega)}$.
:::
::::

::::exercise{#ex-sigma11-omega-jump difficulty=2 objective="Build the ω-jump with $\Sigma^1_1$ comprehension from the unique finite jump sequences, as in the proof that $\Pi^1_1\text{-}\mathsf{CA}_0$ proves $\mathsf{ATR}_0$."}
Show that $\mathsf{ACA}_0$ together with $\Sigma^1_1$ comprehension proves that $X^{(\omega)}$ exists for every $X$.

:::solution
Call $Y$ a **jump sequence of length $n$** for $X$ if $Y^{[0]} = X$, $Y^{[k+1]} = (Y^{[k]})'$ for $k < n$, and $Y$ has no other columns; this is an arithmetic property of $Y$ and $n$. By arithmetic induction, any two jump sequences of length $n$ are equal. The $\Sigma^1_1$ formula $\exists Y\, (Y \text{ is a jump sequence of length } n)$ holds for $n = 0$, and if $Y$ is one of length $n$, the set obtained by adding the column $(Y^{[n]})'$, which exists by arithmetic comprehension, is one of length $n + 1$. Induction for this $\Sigma^1_1$ formula follows from $\Sigma^1_1$ comprehension and the induction axiom (:ref{#prop-induction-comprehension}), so jump sequences of every length exist. Now
$$
\{ \langle n, e \rangle : \exists Y\, (Y \text{ is a jump sequence of length } n \wedge e \in Y^{[n]}) \}
$$
exists by $\Sigma^1_1$ comprehension, and it is $X^{(\omega)}$.
:::
::::

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

The statement of :ref{#thm-pi11-trees} even implies arithmetic comprehension, so that the equivalence holds over $\mathsf{RCA}_0$ (Simpson, Lemma VI.1.1): the tree of strings $\tau$ such that $g(m) \neq k$ for every $m < |\tau|$ has a path if and only if $k$ is not in the range of $g$, so the statement applied to these trees yields the range of an arbitrary function $g$, and :ref{#thm-aca-equivalents} applies.

In computability-theoretic terms, the set of indices of computable ill-founded trees is $\Sigma^1_1$-complete, and its complement is many-one equivalent to Kleene's $\mathcal O$. The **hyperjump** of $X$ is the set of indices of $X$-computable well-founded trees. An ω-model $\mathcal M$ of $\Pi^1_1\text{-}\mathsf{CA}_0$ contains, for each $X \in \mathcal M$, the set of indices of $X$-computable trees with no path in $\mathcal M$. When $\mathcal M$ is a **β-model**, that is, when every tree of $\mathcal M$ with a path has a path in $\mathcal M$, this set is the hyperjump of $X$, and $\mathcal M$ is closed under the hyperjump. An arbitrary ω-model of $\Pi^1_1\text{-}\mathsf{CA}_0$ need not be: the intersection of all of them is the class $\mathrm{HYP}$ of hyperarithmetic sets, which does not contain $\mathcal O$, a result of Gandy, Kreisel and Tait (1960) that we admit (Simpson, Corollary VIII.6.6 and notes to Section VIII.6).

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

The following equivalences are admitted here, with the references of Simpson's monograph. Most of them were announced by Friedman (1975, 1976); the others are due to Steel, to Simpson, and to Friedman, Simpson and Smith (1983). The base theory is $\mathsf{RCA}_0$ unless $\mathsf{ACA}_0$ is indicated.

| System | Equivalent statement | Simpson |
| --- | --- | --- |
| $\mathsf{ATR}_0$ | any two countable well-orderings are comparable | Theorem V.6.8 |
| | $\Sigma^1_1$ separation | Theorem V.5.1 |
| | every closed subset of $2^\nat$ or $\nat^\nat$ with uncountably many points has a non-empty perfect subset (over $\mathsf{ACA}_0$) | Theorem V.5.5 |
| | every countable reduced abelian $p$-group has an Ulm resolution | Theorem V.7.3 |
| | open determinacy in $\nat^\nat$ | Theorem V.8.7 |
| $\Pi^1_1\text{-}\mathsf{CA}_0$ | every tree in $\nat^{<\nat}$ has a perfect kernel | Theorem VI.1.3 |
| | the Cantor–Bendixson theorem: every closed subset of $2^\nat$ or $\nat^\nat$ is the union of a perfect closed set and a countable set (over $\mathsf{ACA}_0$) | Theorem VI.1.6 |
| | every countable abelian group is the direct sum of a divisible group and a reduced group | Theorem VI.4.1 |

The statements about $\mathsf{ATR}_0$ concern countable ordinals, explicitly (comparability, Ulm invariants) or through the ranks of well-founded trees (perfect subsets, open games): $\mathsf{ATR}_0$ is the weakest of the five systems in which countable well-orderings can be compared. Those about $\Pi^1_1\text{-}\mathsf{CA}_0$ ask for a set defined by a quantifier over all paths of a tree, such as the set of nodes above which the tree has a perfect subtree.

A more recent line of work characterizes these systems by **well-ordering principles**, statements of the form "if $X$ is a well-ordering, then so is $F(X)$". $\mathsf{ACA}_0$ is equivalent to such a principle with $F(X) = 2^X$ (Girard 1987; see Hirst 1994, Theorem 2.6, and Simpson, Remark V.6.10), $\mathsf{ATR}_0$ with the Veblen function $\varphi(X, 0)$ (Friedman; proof by Marcone and Montalbán 2011), and $\Pi^1_1\text{-}\mathsf{CA}_0$ with an operation of higher type (Freund 2019).

## ω-models and the separation of the systems

The ω-models of these systems are studied with the tools of higher computability. The class $\mathrm{HYP}$ of hyperarithmetic sets is the intersection of all ω-models of $\mathsf{ATR}_0$, but is not itself a model: there are computable linear orders that have no hyperarithmetic descending sequence but are not well-orderings, the **pseudo-well-orderings**, and they prevent $\mathrm{HYP}$ from satisfying arithmetic transfinite recursion. Consequently $\mathsf{ATR}_0$ has no least ω-model. The failure of arithmetic transfinite recursion in $\mathrm{HYP}$ is proved in the course on hyperarithmetic sets, using Harrison's pseudo-well-orderings and the Enderton–Putnam theorem (:ref{to="hyperarithmetic/pseudo-well-orderings"}); here we admit it, together with the fact that $\mathrm{HYP}$ is the intersection of all ω-models of $\mathsf{ATR}_0$ (Simpson, Proposition V.2.6 and Corollary VIII.6.6).

The five systems are linearly ordered by strength:
$$
\mathsf{RCA}_0 \subsetneq \mathsf{WKL}_0 \subsetneq \mathsf{ACA}_0 \subsetneq \mathsf{ATR}_0 \subsetneq \Pi^1_1\text{-}\mathsf{CA}_0,
$$
where each inclusion is strict. The separations are summarized below.

| Separation | Witness | Reference |
| --- | --- | --- |
| $\mathsf{RCA}_0 \nvdash \mathsf{WKL}_0$ | the ω-model $\mathrm{REC}$ | :ref{#cor-rca-not-wkl} |
| $\mathsf{WKL}_0 \nvdash \mathsf{ACA}_0$ | a Scott ideal of low sets | :ref{#thm-low-scott} |
| $\mathsf{ACA}_0 \nvdash \mathsf{ATR}_0$ | the ω-model $\mathrm{ARITH}$ | :ref{#cor-aca-jump-ideal} |
| $\mathsf{ATR}_0 \nvdash \Pi^1_1\text{-}\mathsf{CA}_0$ | $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the consistency of $\mathsf{ATR}_0$ | Simpson, Theorems VII.2.7 and VII.2.10 |

The last separation uses Gödel's second incompleteness theorem: $\Pi^1_1\text{-}\mathsf{CA}_0$ proves that every set belongs to a countable coded β-model, and every such model satisfies $\mathsf{ATR}_0$, so $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the consistency of $\mathsf{ATR}_0$. A separation by ω-models also exists: a countable β-model of $\mathsf{ATR}_0$ that is not a model of $\Pi^1_1\text{-}\mathsf{CA}_0$ (Simpson, Corollary VII.2.11).

## Notes and references

$\mathsf{ATR}_0$ was introduced by Friedman (1975, 1976) and by Steel in his thesis (1976) (Simpson, notes to Section V.2); early versions of the equivalence with the comparability of well-orderings are due to both (notes to Section V.6). The normal form is Simpson, Lemma V.1.4, and arithmetic transfinite induction Lemma V.2.1; :ref{#thm-pi11-trees} is Lemma VI.1.1. Simpson's monograph covers both systems in Chapters V and VI, and their models in Chapters VII and VIII. Dzhafarov and Mummert, Sections 5.8 and 12.1, and Hirschfeldt, Section 10.3, give shorter introductions. Montalbán's survey discusses the many theorems of $\mathsf{ATR}_0$ strength found since, and open questions about them.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Chapters V–VIII.
- H. Friedman, *Some systems of second order arithmetic and their use*, Proceedings of the International Congress of Mathematicians, Vancouver, 1974, vol. 1, 1975, 235–242.
- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- J. R. Steel, *Determinateness and Subsystems of Analysis*, PhD thesis, University of California, Berkeley, 1976.
- R. O. Gandy, G. Kreisel and W. W. Tait, *Set existence*, Bulletin de l'Académie Polonaise des Sciences, Série des Sciences Mathématiques, Astronomiques et Physiques 8 (1960), 577–582.
- J.-Y. Girard, *Proof Theory and Logical Complexity*, vol. 1, Bibliopolis, 1987.
- J. L. Hirst, *Reverse mathematics and ordinal exponentiation*, Annals of Pure and Applied Logic 66 (1994), 1–18.
- A. Marcone and A. Montalbán, *The Veblen functions for computability theorists*, Journal of Symbolic Logic 76 (2011), 575–602.
- A. Freund, *Π¹₁-comprehension as a well-ordering principle*, Advances in Mathematics 355 (2019), 106767.
- A. Montalbán, *Open questions in reverse mathematics*, Bulletin of Symbolic Logic 17 (2011), 431–454.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.8 and 12.1.

:::::exercises
::::exercise{#ex-wo-descending difficulty=1 objective="Compare the two definitions of well-ordering in $\mathsf{ACA}_0$, and locate the use of arithmetic comprehension."}
Let $W$ be a countable linear order. Show in $\mathsf{ACA}_0$ that $\mathrm{WO}(W)$ holds if and only if there is no function $d : \nat \to F_W$ with $d(k+1) <_W d(k)$ for every $k$. Show that the implication from the absence of descending sequences to $\mathrm{WO}(W)$ is provable in $\mathsf{RCA}_0$.

:::solution
Suppose $\mathrm{WO}(W)$, and let $d$ be a descending sequence. Its range $X = \{ i : \exists k\ d(k) = i \}$ exists by arithmetic comprehension, for a $\Sigma^0_1$ formula; it is a non-empty subset of $F_W$. Its least element $i = d(k)$ would satisfy $i \leq_W d(k+1)$, while $d(k+1) <_W d(k)$, a contradiction.

Conversely, work in $\mathsf{RCA}_0$, and suppose that $X \subseteq F_W$ is non-empty and has no $\leq_W$-least element. Let $d(0)$ be the least element of $X$ in the usual order of $\nat$, and $d(k+1)$ the least $j \in X$, in the usual order, with $j <_W d(k)$. Such a $j$ exists: $d(k) \in X$ is not $\leq_W$-least in $X$, so some $j \in X$ satisfies $d(k) \not\leq_W j$, that is, $j <_W d(k)$, since $W$ is linear. The function $d$ is defined by primitive recursion with searches that terminate, relative to $X \oplus W$, so it exists by $\Delta^0_1$ comprehension, and it is a descending sequence.

Simpson (Definition V.1.1) takes the absence of descending sequences as the definition of a well-ordering; by this exercise the two definitions agree over $\mathsf{ACA}_0$.
:::
::::

::::exercise{#ex-wo-sum difficulty=1 objective="Check the definition of a well-ordering on the sum of two well-orderings, which generalizes the example $\omega + \omega$."}
For countable linear orders $V$ and $W$, let $V + W$ be the order with field $\{ 2i : i \in F_V \} \cup \{ 2j + 1 : j \in F_W \}$, in which $2i \leq 2i'$ if $i \leq_V i'$, $2j + 1 \leq 2j' + 1$ if $j \leq_W j'$, and $2i \leq 2j + 1$ for all $i \in F_V$, $j \in F_W$. Show in $\mathsf{RCA}_0$ that $V + W$ exists and is a linear order, and that it is a well-ordering if $V$ and $W$ are.

:::solution
The set of pairs defining $V + W$ is given by a bounded formula with parameters $V$ and $W$, so it exists by $\Delta^0_1$ comprehension. Reflexivity, antisymmetry, transitivity and totality on the field reduce to those of $V$ and $W$, case by case on the parity of the elements: two even elements compare as in $V$, two odd ones as in $W$, and an even element is below every odd element.

Let $X$ be a non-empty subset of the field. The sets $X_0 = \{ i : 2i \in X \}$ and $X_1 = \{ j : 2j + 1 \in X \}$ exist by $\Delta^0_1$ comprehension. If $X_0$ is non-empty, it has a $\leq_V$-least element $i$, and $2i$ is the least element of $X$: it is below the other even elements of $X$ by the choice of $i$, and below all odd elements. Otherwise $X$ has only odd elements, $X_1$ is non-empty and has a $\leq_W$-least element $j$, and $2j + 1$ is the least element of $X$.
:::
::::

::::exercise{#ex-hierarchy-ill-founded difficulty=2 objective="See on the order $\omega^*$ why hierarchies need a well-ordering: along an ill-founded order they may fail to be unique, or fail to exist."}
Let $W$ be the order $\omega^*$, coded by $\{ (i, j) : j \leq i \}$, so that $i <_W j$ if and only if $i > j$, and $H^{[<j]}$ consists of the columns $i > j$ of $H$.

1. Let $\theta_1(n, j, Y) \equiv \exists i\ \langle i, n \rangle \in Y$. Show that for every set $A$, the set $H_A = \{ \langle j, n \rangle : n \in A \}$ is a $\theta_1$-hierarchy along $W$.
2. Let $\theta_2(n, j, Y) \equiv \neg \exists i\ \langle i, n \rangle \in Y$. Show that there is no $\theta_2$-hierarchy along $W$.
3. Explain where the argument for the uniqueness of hierarchies along a well-ordering fails in the first case.

:::solution
1. The field of $W$ is $\nat$, and every column of $H_A$ is $A$. For each $j$, $H_A^{[<j]} = \{ \langle i, n \rangle : i > j,\ n \in A \}$, so $\theta_1(n, j, H_A^{[<j]})$ holds if and only if $n \in A$, taking $i = j + 1$. So the column $j$ is $\{ n : \theta_1(n, j, H_A^{[<j]}) \}$, as required. Different sets $A$ give different hierarchies.
2. Suppose $H$ is a $\theta_2$-hierarchy. Fix $n$, and let $c_j = 1$ if $n \in H^{[j]}$ and $c_j = 0$ otherwise. The definition says: $c_j = 1$ if and only if $c_i = 0$ for every $i > j$. If all $c_i$ are $0$, this gives $c_0 = 1$, a contradiction. So some $c_i = 1$; then $c_{i'} = 0$ for every $i' > i$, and in particular, for $j = i + 1$, all $c_{i'}$ with $i' > j$ are $0$, which gives $c_{i+1} = 1$, a contradiction.
3. The argument considers the set of columns at which two hierarchies differ, which is non-empty, and takes its $\leq_W$-least element. For $H_A$ and $H_B$ with $A \neq B$, this set is all of $\nat$, which has no $\leq_W$-least element, since every $j$ has $j + 1 <_W j$. The proof breaks down exactly because $W$ is not a well-ordering.
:::
::::

::::exercise{#ex-pi11-leftmost-path difficulty=2 objective="Use $\Sigma^1_1$ comprehension to form the set of nodes that lie on a path, and find the leftmost path of an ill-founded tree."}
For functions $P \neq Q$ from $\nat$ to $\nat$, say that $P$ is **to the left of** $Q$ if $P(k) < Q(k)$ at the least $k$ with $P(k) \neq Q(k)$. Show in $\Pi^1_1\text{-}\mathsf{CA}_0$ that every ill-founded tree $T \subseteq \nat^{<\nat}$ has a **leftmost path**, a path that is to the left of every other path.

:::solution
Let $I$ be the set of $\sigma \in T$ such that some path of $T$ extends $\sigma$. It is defined by a $\Sigma^1_1$ formula, so it exists by $\Sigma^1_1$ comprehension, a consequence of $\Pi^1_1$ comprehension. The empty string is in $I$, since $T$ is ill-founded. If $\sigma \in I$, with a path $Q$ extending $\sigma$, then $\sigma\, Q(|\sigma|) \in I$; so every node of $I$ has an immediate successor in $I$.

Define $P$ by letting $P(k)$ be the least $m$ such that $(P \uh k)\, m \in I$. By induction on $k$, $P \uh k \in I$ and the search for $P(k)$ terminates, so $P$ exists by $\Delta^0_1$ comprehension relative to $I$, and it is a path of $T$, since $I \subseteq T$. Let $Q \neq P$ be a path, and $k$ the least position where they differ. Then $(P \uh k)\, Q(k) = Q \uh (k+1)$ is in $I$, since $Q$ extends it; by the choice of $P(k)$, $P(k) \leq Q(k)$, so $P(k) < Q(k)$, and $P$ is to the left of $Q$.

For binary trees, arithmetic comprehension suffices (:ref{#ex-leftmost-path-aca}): extendibility to every length is then a $\Pi^0_1$ property, while lying on a path of a tree in $\nat^{<\nat}$ is $\Sigma^1_1$. Compare Dzhafarov and Mummert, Exercise 5.13.23 (2).
:::
::::

::::exercise{#ex-beta-model-wo difficulty=2 objective="Relate well-orderings in an ω-model to true well-orderings, and use a pseudo-well-ordering to show that $\mathrm{ARITH}$ is not a β-model."}
Let $\mathcal M$ be an ω-model of $\mathsf{ACA}_0$ and $W \in \mathcal M$ a countable linear order.

1. Show that if $W$ is a well-ordering, then $\mathcal M \models \mathrm{WO}(W)$.
2. Show that if $\mathcal M$ is a β-model and $\mathcal M \models \mathrm{WO}(W)$, then $W$ is a well-ordering.
3. Admit that there is a computable linear order that is not a well-ordering and has no hyperarithmetic descending sequence. Deduce that $\mathrm{ARITH}$ is not a β-model.

:::solution
1. $\mathrm{WO}(W)$ is $\forall X\, \alpha(X, W)$ with $\alpha$ arithmetic. If $W$ is a well-ordering, $\alpha(X, W)$ is true for every set $X$, in particular for every $X \in \mathcal M$, and then $\mathcal M \models \alpha(X, W)$ by absoluteness (:ref{#prop-omega-absolute}). So $\mathcal M \models \mathrm{WO}(W)$.
2. Suppose $W$ is not a well-ordering. By :ref{#ex-wo-descending}, applied in $\mathcal P(\nat)$, which satisfies $\mathsf{ACA}_0$, there is a descending sequence $d$. Let $T$ be the tree of finite sequences $\sigma \in \nat^{<\nat}$ such that $\sigma(k) \in F_W$ for every $k < |\sigma|$ and $\sigma(k+1) <_W \sigma(k)$ for every $k + 1 < |\sigma|$. It is computable from $W$, so $T \in \mathcal M$, and $d$ is a path. Since $\mathcal M$ is a β-model, $T$ has a path $d' \in \mathcal M$, which is a descending sequence of $W$, also in the sense of $\mathcal M$ by absoluteness. By :ref{#ex-wo-descending}, applied in $\mathcal M$, $\mathcal M \models \neg \mathrm{WO}(W)$.
3. Let $W$ be such an order. It is computable, so $W \in \mathrm{ARITH}$, and $\mathrm{ARITH}$ is an ω-model of $\mathsf{ACA}_0$ (:ref{#cor-aca-jump-ideal}). Every arithmetic set is hyperarithmetic, so $\mathrm{ARITH}$ contains no descending sequence of $W$, and by :ref{#ex-wo-descending}, applied in $\mathrm{ARITH}$, $\mathrm{ARITH} \models \mathrm{WO}(W)$. If $\mathrm{ARITH}$ were a β-model, $W$ would be a well-ordering by part 2, a contradiction.

So in a β-model of $\mathsf{ACA}_0$, the formula $\mathrm{WO}$ is absolute for the orders of the model; part 3 shows that an arbitrary ω-model of $\mathsf{ACA}_0$ need not have this property.
:::
::::
:::::
