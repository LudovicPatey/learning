---
title: Relatively intrinsically c.e. relations
summary: Relations that are c.e. in every copy of a structure; computable infinitary Σ₁ formulas; the theorem of Ash, Knight, Manasse, Slaman and Chisholm that a relation is relatively intrinsically c.e. if and only if it is definable by such a formula with parameters, proved by building a copy that fails to make the relation c.e. unless a tuple forces it; the uniform version; the sets of numbers coded by a structure (Knight).
duration: 40
prerequisites: [computable-structures/back-and-forth]
---

Some relations on a structure are c.e. in every copy, for a reason that has nothing to do with the copy: in a vector space, linear dependence is found by searching for a vanishing linear combination; in a group, an element is torsion if some power of it is the identity. In each case, a disjunction of existential formulas explains the enumeration. This lesson shows that such an explanation always exists: a relation is c.e. in all copies exactly when it is defined by a computable disjunction of existential formulas, possibly with parameters. The proof is the prototype of many arguments of the subject: try to build a copy in which the relation is not c.e.; the failure of this attempt produces the definition.

## Definitions and examples

Throughout, $\mathcal A$ is an ω-presentation of a $\tau$-structure, and relations are subsets of $A^{<\nat}$, the set of finite tuples; this includes the $n$-ary relations, and several relations of different arities at once. For a copy $\mathcal B$ of $\mathcal A$ and an isomorphism, the image of $R$ is a relation $R^{\mathcal B}$ on $\mathcal B$; we write $(\mathcal B, R^{\mathcal B}) \cong (\mathcal A, R)$.

:::definition{#def-rice}
A relation $R \subseteq A^{<\nat}$ is **relatively intrinsically c.e.**, or **r.i.c.e.**, if for every copy $(\mathcal B, R^{\mathcal B})$ of $(\mathcal A, R)$, the set $R^{\mathcal B}$ (of tuples of numbers) is c.e. in $D(\mathcal B)$. It is **relatively intrinsically computable** if $R^{\mathcal B}$ is computable in $D(\mathcal B)$ for every copy; equivalently, if $R$ and its complement are r.i.c.e.
:::

The definition depends only on the isomorphism type of $(\mathcal A, R)$: the copies of a structure are all ω-presentations isomorphic to it. "Relatively" refers to the oracle $D(\mathcal B)$: the relation must be c.e. relative to each copy, not only in the computable copies.

:::example{#ex-rice-relations}
1. In a $\mathbb Q$-vector space, with scalar multiplications as unary functions, the set $\mathrm{LD}$ of linearly dependent tuples is r.i.c.e.: in a copy $\mathcal V$, enumerate a tuple when a non-trivial rational combination of it is found to vanish, which $D(\mathcal V)$ can check.
2. In a linear order, the complement of the **adjacency** relation, $\neg\mathrm{Adj}(a, b)$, which holds when $b \leq a$ or some $c$ lies strictly between $a$ and $b$, is r.i.c.e.: it has the existential definition $b \leq a \vee \exists c\,(a < c < b)$.
3. Let $\mathcal A$ be a linear order with the adjacency relation added to the vocabulary, and $R$ the set of pairs $a < b$ such that the number of elements between them is finite and belongs to $\emptyset'$. In a copy, wait for a chain $a = a_0, a_1, \ldots, a_{n+1} = b$ of adjacent elements, then for $n$ to enter $\emptyset'$. So $R$ is r.i.c.e., although it is not definable by any single existential formula: it is the infinite disjunction over $n \in \emptyset'$ of the existential formulas saying that there is such a chain of length $n + 1$.
:::

The last example shows the kind of definition that suffices.

:::definition{#def-sigma-c-1}
A **computable infinitary $\Sigma_1$ formula**, or **$\Sigma^c_1$ formula**, is a disjunction
$$
\psi(\bar x) \equiv \bigvee_{i \in I} \exists \bar y_i\ \varphi_i(\bar x, \bar y_i),
$$
over a c.e. set $I$ of indices, of existential formulas with quantifier-free $\varphi_i$, all with the same finitely many free variables $\bar x$. It holds of $\bar a$ if some disjunct does. A relation $R \subseteq A^{<\nat}$ is **$\Sigma^c_1$-definable with parameters** if there are a tuple $\bar p$ and a computable sequence $(\psi_n)$ of $\Sigma^c_1$ formulas, $\psi_n$ with $|\bar p| + n$ free variables, such that $\bar b \in R \iff \mathcal A \models \psi_{|\bar b|}(\bar p, \bar b)$.
:::

The $\Sigma^c_1$ formulas can be listed effectively: the $e$-th formula with $j$ free variables is the disjunction of the existential formulas whose indices are in $W_e$. Satisfaction is c.e. uniformly: there is a c.e. operator $W$ such that, for every ω-presentation $\mathcal B$, $(e, \bar b) \in W^{D(\mathcal B)}$ if and only if $\mathcal B$ satisfies the $e$-th formula at $\bar b$. Indeed, an existential formula holds of $\bar b$ if and only if its quantifier-free matrix holds of $\bar b$ and some tuple of witnesses, which $D(\mathcal B)$ can check. Consequently, a relation that is $\Sigma^c_1$-definable with parameters $\bar p$ is r.i.c.e.: in a copy $\mathcal B$, with $\bar q$ the image of $\bar p$, the relation is enumerated by $W^{D(\mathcal B)}$ with the finite tuple $\bar q$ as extra information.

## The characterization

:::theorem[Ash, Knight, Manasse, Slaman; Chisholm]{#thm-akms-chisholm-1}
A relation $R \subseteq A^{<\nat}$ is r.i.c.e. if and only if it is $\Sigma^c_1$-definable in $\mathcal A$ with parameters.
:::

**Intuition.** We build a copy $\mathcal B$ of $\mathcal A$, as the pull-back of an enumeration $g$, and try to diagonalize against every c.e. operator $W_e$: we look for a finite part $\bar q$ of the enumeration that makes $W_e^{D(\mathcal B)}$ enumerate a tuple outside $R$. Since $R$ is r.i.c.e., some $W_e$ enumerates $R^{\mathcal B}$, and the diagonalization fails for that $e$ at some stage, with $g$ extending a tuple $\bar p$. Failing means that no extension of $\bar p$ makes $W_e$ err. So every tuple that $W_e$ enumerates along some extension of $\bar p$ is in $R$, and conversely every tuple of $R$ is enumerated along a long enough part of $g$. "Enumerated along some extension of $\bar p$" is a $\Sigma^c_1$ property with parameters $\bar p$.

:::proof{of=thm-akms-chisholm-1}
We have seen that definable relations are r.i.c.e. Conversely, let $R$ be r.i.c.e.; we may assume $\tau$ relational. For a finite tuple $\bar q$ of elements of $\mathcal A$, let $D_{\mathcal A}(\bar q)$ be its finite atomic diagram, so that a pull-back $g^{-1}(\mathcal A)$ of an enumeration $g = \bigcup_s \bar p_s$ has atomic diagram $\bigcup_s D_{\mathcal A}(\bar p_s)$. For a tuple $\bar j = (j_1, \ldots, j_\ell)$ of numbers below $|\bar q|$, write $\bar q_{\bar j} = (q_{j_1}, \ldots, q_{j_\ell})$. Let
$$
Q_e = \{ \bar q \in A^{<\nat} : \text{some } \bar j \text{ with entries below } |\bar q| \text{ satisfies } \bar j \in W_e^{D_{\mathcal A}(\bar q)} \text{ and } \bar q_{\bar j} \notin R \},
$$
where $W_e^\sigma$ is the finite set enumerated by $W_e$ with the finite oracle $\sigma$ in $|\sigma|$ steps.

*Construction.* Let $\bar p_0$ be empty. At stage $s + 1 = 2e + 1$, append to $\bar p_s$ the $e$-th element of $A$ if it is not already there. At stage $s + 1 = 2e$, if some $\bar q \supseteq \bar p_s$ belongs to $Q_e$, let $\bar p_{s+1}$ be such a $\bar q$; otherwise let $\bar p_{s+1} = \bar p_s$. Let $g = \bigcup_s \bar p_s$, which is onto, and $\mathcal B = g^{-1}(\mathcal A)$, a congruence ω-presentation of $\mathcal A$ (the definition of r.i.c.e. may equivalently use congruence presentations, which have injective quotients computable from them). Then $R^{\mathcal B} = g^{-1}(R)$, the set of $\bar j$ with $g(\bar j) \in R$.

*Some stage fails.* If at stage $2e$ some $\bar q \in Q_e$ was chosen, then $\bar q \subseteq g$, the tuple $\bar j$ witnessing $\bar q \in Q_e$ belongs to $W_e^{D(\mathcal B)}$, since $D_{\mathcal A}(\bar q) \subseteq D(\mathcal B)$, and $g(\bar j) = \bar q_{\bar j} \notin R$: so $W_e^{D(\mathcal B)} \neq R^{\mathcal B}$. Since $R$ is r.i.c.e., $R^{\mathcal B} = W_e^{D(\mathcal B)}$ for some $e$; at stage $2e$, no extension of $\bar p = \bar p_{2e - 1}$ was in $Q_e$.

*The definition.* Let $S$ be the set of tuples $\bar q_{\bar j}$ such that $\bar q \supseteq \bar p$ and $\bar j \in W_e^{D_{\mathcal A}(\bar q)}$. Then $S = R$. If $\bar a \in R$, write $\bar a = g(\bar j)$; then $\bar j \in W_e^{D(\mathcal B)}$, so $\bar j \in W_e^{D_{\mathcal A}(\bar q)}$ for a long enough initial segment $\bar q$ of $g$, which extends $\bar p$; so $\bar a \in S$. Conversely, if $\bar a = \bar q_{\bar j} \in S$ were not in $R$, then $\bar q \in Q_e$, contradicting the choice of $e$. Finally, $S$ is $\Sigma^c_1$-definable with parameters $\bar p$:
$$
\bar a \in S \iff \bigvee_{(\sigma, \bar j)} \exists \bar q\, \big( \bar q \supseteq \bar p \wedge \bar q_{\bar j} = \bar a \wedge \sigma \subseteq D_{\mathcal A}(\bar q) \big),
$$
where the disjunction ranges over the pairs of a finite string $\sigma$ and a tuple $\bar j$ with $\bar j \in W_e^\sigma$, a c.e. set; each disjunct is existential, since "$\sigma \subseteq D_{\mathcal A}(\bar q)$" is a quantifier-free formula of $\bar q$, the conjunction of the atomic facts and negated atomic facts that $\sigma$ records.
:::

:::quiz[the characterization of r.i.c.e. relations]
Where does the proof use that $R$ is r.i.c.e. in every copy, and not only in the computable ones?

- [x] The copy $\mathcal B$ built in the proof is computable from the enumeration $g$, which is built by searching through $Q_e$, a set that depends on $R$; $\mathcal B$ need not be computable, and the hypothesis must apply to it.
- [ ] To make the stages $2e + 1$ possible.

  The odd stages only make $g$ onto; they use nothing about $R$.
- [ ] To show that $S \subseteq R$.

  This uses only the failure of the diagonalization at stage $2e$.

---

Where do the parameters $\bar p$ come from?

- [x] They are the part of the enumeration built before the stage at which the diagonalization against the correct operator $W_e$ fails; below $\bar p$, other operators may have been defeated, and the definition must start from where the failure occurred.
- [ ] They are the elements of $R$.

  $\bar p$ is a tuple of the structure, not necessarily related to $R$.
- [ ] They make the formula computable.

  The formula is computable for any $\bar p$; the parameters make it correct.
:::

When no parameters are needed, the enumeration is uniform across copies. A relation $R$ is **uniformly r.i.c.e.** if a single c.e. operator $W$ satisfies $R^{\mathcal B} = W^{D(\mathcal B)}$ for every copy $(\mathcal B, R^{\mathcal B})$.

:::corollary{#cor-uniform-rice}
A relation is uniformly r.i.c.e. if and only if it is $\Sigma^c_1$-definable without parameters.
:::

:::proof{of=cor-uniform-rice}
Definable relations are uniformly r.i.c.e., by the uniform satisfaction operator. Conversely, let $W_e$ witness uniformity. No tuple $\bar q$ is in $Q_e$: an enumeration $g$ extending it gives a copy in which $W_e$ enumerates a tuple outside $R$. So the last part of the proof applies with $\bar p$ empty.
:::

## Sets coded by a structure

A set $X \subseteq \nat$ is **c.e.-coded** by $\mathcal A$ if $X$ is c.e. in every copy of $\mathcal A$. In the group $G_X$ of :ref{#ex-computable-structures}, $X$ is c.e.-coded. What can a structure code? An obvious source: the **existential type** of a tuple $\bar p$, the set $\exists\text{-}\mathrm{tp}_{\mathcal A}(\bar p)$ of indices of existential formulas true of $\bar p$, is enumerated by every copy that knows where $\bar p$ is. Anything that can be enumerated from this type is coded too. This is made precise by enumeration reducibility: $X \leq_e Y$ if there is a c.e. set $\Psi$ of pairs $(n, F)$, $F$ a finite set, such that $n \in X$ if and only if $(n, F) \in \Psi$ for some $F \subseteq Y$. Then every enumeration of $Y$ computes an enumeration of $X$.

:::corollary[Knight]{#cor-knight-ce-coded}
A set $X$ is c.e.-coded by $\mathcal A$ if and only if $X \leq_e \exists\text{-}\mathrm{tp}_{\mathcal A}(\bar p)$ for some tuple $\bar p$.
:::

:::proof{of=cor-knight-ce-coded}
If $X \leq_e \exists\text{-}\mathrm{tp}_{\mathcal A}(\bar p)$, every copy enumerates the existential type of the image of $\bar p$, hence enumerates $X$. Conversely, let $X$ be c.e.-coded, and let $R_X$ be the set of tuples whose length belongs to $X$. In a copy $\mathcal B$, a tuple of length $n$ is in $R_X$ if and only if $n \in X$, which is c.e. in $D(\mathcal B)$; so $R_X$ is r.i.c.e., and by :ref{#thm-akms-chisholm-1} it is $\Sigma^c_1$-definable with some parameters $\bar p$, which we may assume non-empty. Let $\bar b_n$ be the tuple of length $n$ all of whose entries are $p_0$. Then $n \in X$ if and only if $\mathcal A \models \psi_n(\bar p, \bar b_n)$, that is, if and only if one of the existential disjuncts of $\psi_n$, with $\bar b_n$ replaced by copies of $p_0$, is true of $\bar p$. The indices of these existential formulas of $\bar p$ form a c.e. set computable from $n$, so $n \in X$ if and only if some index in this set belongs to $\exists\text{-}\mathrm{tp}_{\mathcal A}(\bar p)$: an enumeration reduction in which every finite set $F$ is a singleton.
:::

So existential types are, up to enumeration reducibility, all that a structure codes in the c.e. sense. For instance, if $\mathcal A$ has a computable copy, every existential type is c.e., and so is every c.e.-coded set.

::::exercise{#ex-sigma-c-1-examples difficulty=1 objective="Write Σᶜ₁ definitions of natural relations, and check that they are r.i.c.e."}
Give $\Sigma^c_1$ definitions without parameters of: the torsion elements of a group; the pairs of vertices joined by a path in a graph; the elements of a field that are algebraic over the prime field.

:::solution
Torsion: $\bigvee_{n \geq 1} x^n = e$, where $x^n$ is the product of $n$ copies of $x$; each disjunct is quantifier-free. Connectedness: $\bigvee_{n \geq 0} \exists z_1 \ldots z_n\, (x E z_1 \wedge z_1 E z_2 \wedge \cdots \wedge z_n E y)$, with the case $n = 0$ read as $x E y$, and $x = y$ added as a disjunct. Algebraic elements: $\bigvee_{p} p(x) = 0$, over the non-zero polynomials $p$ with integer coefficients, written with the field operations and the constants $0$ and $1$; the list of these polynomials is computable. In each case the definition is a computable list of existential formulas, so the relation is uniformly r.i.c.e. by :ref{#cor-uniform-rice}.
:::
::::

## Notes and references

The definition of r.i.c.e. relations and :ref{#thm-akms-chisholm-1} are due to Ash, Knight, Manasse and Slaman (1989) and, independently, Chisholm (1990), for $n$-ary relations; the proof given here, by a failed diagonalization, follows Montalbán, Theorem II.16, who works with subsets of $\nat \times A^{<\nat}$. :ref{#cor-knight-ce-coded} is Knight (1986), in the form of Montalbán, Corollary II.23 (see also Ash–Knight, Theorem 10.17). The full theorem, for relations that are intrinsically $\Sigma^0_\alpha$ and computable infinitary $\Sigma_\alpha$ formulas, belongs to the theory beyond one jump, planned as a later course of the track.

- C. J. Ash, J. F. Knight, M. Manasse and T. A. Slaman, *Generic copies of countable structures*, Annals of Pure and Applied Logic 42 (1989), 195–205.
- J. Chisholm, *Effective model theory vs. recursive model theory*, Journal of Symbolic Logic 55 (1990), 1168–1191.
- J. F. Knight, *Degrees coded in jumps of orderings*, Journal of Symbolic Logic 51 (1986), 1034–1042.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Chapter II, Section II.1.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 10.

:::::exercises
::::exercise{#ex-rice-closure difficulty=1 objective="Check closure properties of r.i.c.e. relations through their syntactic characterization."}
Show that the r.i.c.e. relations on a structure are closed under finite unions and intersections, and under existential projection: if $R \subseteq A^{n+1}$ is r.i.c.e., so is $\{ \bar a : \exists b\ (\bar a, b) \in R \}$.

:::solution
By :ref{#thm-akms-chisholm-1}, take $\Sigma^c_1$ definitions with parameters $\bar p$ and $\bar p'$; use the parameters $\bar p \bar p'$ for both. A union is defined by the disjunction of the two computable disjunctions, which is again a computable disjunction. An intersection: a conjunction $\bigvee_i \exists \bar y\, \varphi_i \wedge \bigvee_j \exists \bar z\, \chi_j$ is equivalent to $\bigvee_{(i, j)} \exists \bar y \bar z\, (\varphi_i \wedge \chi_j)$, a computable disjunction of existential formulas. Projection: $\exists b \bigvee_i \exists \bar y\, \varphi_i(\bar a, b, \bar y)$ is equivalent to $\bigvee_i \exists b \bar y\, \varphi_i$. One can also argue directly from the definition: in each copy, the two relations are c.e. in the diagram, and c.e. sets are closed under these operations.
:::
::::

::::exercise{#ex-uniform-vs-parameters difficulty=2 objective="See that parameters may be necessary, with a relation that is r.i. computable but not uniformly r.i.c.e."}
Let $\mathcal A = (\nat; S)$, where $S$ is the successor relation. Show that the set $\{ 0 \}$ is relatively intrinsically computable, but not uniformly r.i.c.e.

:::solution
In a copy $\mathcal B$, with $b$ the image of $0$, the set $\{ b \}$ is computable, given the single number $b$; so $\{ 0 \}$ is r.i. computable, and it is $\Sigma^c_1$-definable with the parameter $0$, by the formula $x = p$. It is not $\Sigma^c_1$-definable without parameters. The map $n \mapsto n + 1$ is an embedding of $(\nat; S)$ into itself, since $S(n, m) \iff S(n + 1, m + 1)$, and existential formulas are preserved by embeddings: an existential formula true of $0$ is true of $1$. So every $\Sigma^c_1$ formula without parameters true of $0$ is true of $1$, and none defines $\{ 0 \}$. By :ref{#cor-uniform-rice}, $\{ 0 \}$ is not uniformly r.i.c.e.: no single operator finds the root in every copy, although every copy finds it once told where it is.
:::
::::
:::::
