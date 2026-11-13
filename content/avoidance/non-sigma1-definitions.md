---
title: Preservation of non-Σ⁰₁ definitions
summary: A problem preserves non-Σ⁰₁ definitions if its solutions never make a non-Σ⁰₁ set Σ⁰₁; this implies cone avoidance, and is equivalent to it by a theorem of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky; the forcing question proves it directly for WKL, COH, the pigeonhole principle and Ramsey's theorem for pairs.
duration: 45
prerequisites: [seetapun-forcing, arithmetic-hierarchy/post-theorem]
---

A set is computable if and only if it and its complement are $\Sigma^0_1$ (:ref{#thm-post}, for $n = 0$). Cone avoidance asks that a solution does not make a non-computable set computable; one may ask instead that it does not make a non-$\Sigma^0_1$ set $\Sigma^0_1$. Some sets simplify definitions in this sense: every $\Sigma^0_2$ set is $\Sigma^0_1(\emptyset')$. The resulting property of problems is called **preservation of non-$\Sigma^0_1$ definitions**. Its proofs by the forcing question are simpler than those of cone avoidance, since the set $U$ of the three-case argument is compared with a set of numbers rather than with a graph, and the property is the first level of a hierarchy, the preservation of non-$\Sigma^0_n$ definitions, that controls the iterated jumps of solutions.

## Definition and relation with cone avoidance

:::definition{#def-preserve-non-sigma1}
A problem $\mathsf P$ admits **preservation of non-$\Sigma^0_1$ definitions** if for every set $Z$, every set $C$ that is not $\Sigma^0_1(Z)$, and every instance $X \leq_T Z$ of $\mathsf P$, there is a solution $Y$ to $X$ such that $C$ is not $\Sigma^0_1(Z \oplus Y)$. It admits **strong** preservation of non-$\Sigma^0_1$ definitions if the same holds for every instance $X$.
:::

For a fixed $C$, the class $\{ Z : C \text{ is not } \Sigma^0_1(Z) \}$ is closed downwards under Turing reducibility, since a set that is $\Sigma^0_1(Y)$ is $\Sigma^0_1(Z)$ for every $Z \geq_T Y$. So, as for cone avoidance (:ref{#prop-cone-avoidance-preservation}), the definition asks that $\mathsf P$ preserve each of these weakness properties.

:::example{#ex-non-sigma1}
1. The problem $\mathsf J$ does not admit preservation of non-$\Sigma^0_1$ definitions: the complement of $\emptyset'$ is not $\Sigma^0_1$, but it is $\Sigma^0_1(\emptyset')$, and $\emptyset'$ is the only solution to the instance $\emptyset$.
2. Let $A$ be a c.e. set and $Y$ any set. Then $A \leq_T Y$ if and only if $\overline A$ is $\Sigma^0_1(Y)$, since $A$ is already $\Sigma^0_1(Y)$. For complements of c.e. sets, preserving non-$\Sigma^0_1$ definitions and avoiding cones are therefore the same requirement.
3. Preserving the definition of a set is a stronger requirement than avoiding its cone. If $C \leq_T Y$, then $C$ is $\Sigma^0_1(Y)$; but $C$ may be $\Sigma^0_1(Y)$ without being computable in $Y$. For instance $\emptyset''$ is not $\Sigma^0_1$, and it is $\Sigma^0_1(\emptyset')$ but not computable in $\emptyset'$.
:::

:::proposition{#prop-non-sigma1-cone}
If a problem admits preservation of non-$\Sigma^0_1$ definitions, it admits cone avoidance. The same holds for the strong versions.
:::

:::proof{of=prop-non-sigma1-cone}
Let $C \not\leq_T Z$ and $X \leq_T Z$ an instance. By Post's theorem relativized to $Z$, $C$ and $\overline C$ are not both $\Sigma^0_1(Z)$; let $D$ be one of them that is not. Preservation gives a solution $Y$ such that $D$ is not $\Sigma^0_1(Z \oplus Y)$. If $C \leq_T Z \oplus Y$, then $C$ and $\overline C$ would both be $\Sigma^0_1(Z \oplus Y)$, and so would $D$. So $C \not\leq_T Z \oplus Y$. The proof is the same for arbitrary instances.
:::

The converse also holds, but its proof is of a different nature. We state it without proof.

:::theorem[Downey, Greenberg, Harrison-Trainor, Patey, Turetsky]{#thm-non-sigma1-equivalence}
A problem admits cone avoidance if and only if it admits preservation of non-$\Sigma^0_1$ definitions.
:::

The difficult direction starts from a set $A$ that is not $\Sigma^0_1(Z)$ and builds a set $W$ and a set $C \not\leq_T Z \oplus W$ such that every set $G$ for which $A$ is $\Sigma^0_1(Z \oplus W \oplus G)$ computes $C$ together with $Z \oplus W$. Cone avoidance for $C$ relative to $Z \oplus W$ then gives preservation of the definition of $A$. The construction uses the structure of the enumeration degrees, and is beyond the scope of this course. In practice, when the property is needed, it is proved directly with a forcing question; the direct proofs below are no harder than those of cone avoidance.

## The abstract theorems

:::theorem{#thm-local-non-sigma1}
Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving forcing question (:ref{#def-question-local}), and let $C$ be a set that is not $\Sigma^0_1(X)$ for any $X \in \mathcal M$. For every sufficiently generic set $G$, $C$ is not $\Sigma^0_1(Z \oplus G)$.
:::

:::proof{of=thm-local-non-sigma1}
The sets $\Sigma^0_1(Z \oplus G)$ are the sets $W^{Z \oplus G}_e = \{ x : \Phi^{Z \oplus G}_e(x)\converge \}$. Fix $e$ and a condition $c$, with $X \in \mathcal M$ as in :ref{#def-question-local}. The set $U = \{ x : c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge \}$ is $\Sigma^0_1(X)$, so $U \neq C$. If $x \in U \setminus C$, property 1 gives an extension forcing $x \in W^{Z \oplus G}_e$; if $x \in C \setminus U$, property 2 gives an extension forcing $x \notin W^{Z \oplus G}_e$. In both cases every member $G$ of the extension satisfies $W^{Z \oplus G}_e \neq C$. A set generic for these dense sets, one for each $e$, has $W^{Z \oplus G}_e \neq C$ for every $e$.
:::

There are only two cases: the third case of the cone avoidance argument, where $U$ coincides with the object compared, is excluded at once by the hypothesis. For $\mathcal M = \{ \emptyset \}$ and $Z = \emptyset$ this is :ref{#thm-question-preservation} with $n = 1$. The disjunctive version is proved in the same way as :ref{#lem-disjunctive-cone}.

:::lemma{#lem-disjunctive-non-sigma1}
Let a disjunctive notion of forcing have a $\Sigma^0_1(\mathcal M)$-preserving disjunctive forcing question, and let $C$ be a set that is not $\Sigma^0_1(X)$ for any $X \in \mathcal M$. For every condition $c$ and all $e_0, e_1$, there are $d \leq c$ and $i < 2$ such that every member $G$ of side $i$ of $d$ satisfies $W^{Z \oplus G}_{e_i} \neq C$.
:::

:::proof{of=lem-disjunctive-non-sigma1}
Let $U$ be the set of $x$ such that $c \mathrel{?{\vdash}} (x \in W^{Z \oplus G}_{e_0})(G_0) \vee (x \in W^{Z \oplus G}_{e_1})(G_1)$, a $\Sigma^0_1(X)$ set for some $X \in \mathcal M$, hence different from $C$. If $x \in U \setminus C$, property 1 gives $d$ and $i$ with $d \Vdash x \in W^{Z \oplus G_i}_{e_i}$; if $x \in C \setminus U$, property 2 gives $d$ and $i$ with $d \Vdash x \notin W^{Z \oplus G_i}_{e_i}$.
:::

:::quiz[the abstract theorems]
Why does the proof of :ref{#thm-local-non-sigma1} need only two cases, while the proof of :ref{#thm-local-cone-avoidance} needs three?

- [x] Because $U$ is compared with $C$ itself, and $U \neq C$ follows directly from the complexity of $U$; in the cone avoidance proof, $U$ is compared with the graph of $C$, and the third case is the one where they coincide.
- [ ] Because $C$ is not computable.

  The hypothesis is that $C$ is not $\Sigma^0_1(X)$; non-computability alone would not exclude $U = C$.
- [ ] Because the formulas $x \in W^{Z \oplus G}_e$ are $\Pi^0_1$.

  They are $\Sigma^0_1$.
:::

## Applications

The class $\mathcal M$ is obtained by preserving the property along weak König's lemma, as in :ref{#lem-scott-cone}.

:::lemma{#lem-scott-preservation}
Let $\mathcal W$ be a weakness property preserved by $\mathsf{WKL}$. For every $Z \in \mathcal W$, there is a Scott ideal $\mathcal M \subseteq \mathcal W$ containing $Z$.
:::

:::proof{of=lem-scott-preservation}
By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal M \subseteq \mathcal W$ containing $Z$ and satisfying $\mathsf{WKL}$, that is, in which every infinite binary tree has an infinite path. This is a Scott ideal (:ref{#def-scott-ideal}).
:::

:::theorem{#thm-non-sigma1-examples}
1. $\mathsf{WKL}$ and $\mathsf{COH}$ admit preservation of non-$\Sigma^0_1$ definitions.
2. $\mathsf{RT}^1_2$ admits strong preservation of non-$\Sigma^0_1$ definitions.
3. $\mathsf{RT}^2_2$ admits preservation of non-$\Sigma^0_1$ definitions.
:::

:::proof{of=thm-non-sigma1-examples}
Fix $Z$ and a set $C$ that is not $\Sigma^0_1(Z)$, and let $\mathcal W = \{ X : C \text{ is not } \Sigma^0_1(X) \}$.

1. For $\mathsf{WKL}$, use Jockusch–Soare forcing relative to $Z$, inside the class of paths of a $Z$-computable infinite binary tree: its question at level $1$ (:ref{#thm-tree-question}), relativized, is $\Sigma^0_1(Z)$-preserving, and :ref{#thm-local-non-sigma1} with $\mathcal M = \{ Z \}$ gives a path $G$ with $C$ not $\Sigma^0_1(Z \oplus G)$. For $\mathsf{COH}$, use Mathias forcing with $Z$-computable reservoirs and the question of :ref{#prop-mathias-question}, relativized; sufficiently generic sets are cohesive (:ref{#ex-generic-notions}).
2. By item 1, $\mathsf{WKL}$ preserves $\mathcal W$, so :ref{#lem-scott-preservation} gives a Scott ideal $\mathcal M \subseteq \mathcal W$ containing $Z$. Use the Dzhafarov–Jockusch notion with reservoirs in $\mathcal M$ and its disjunctive question (first exercise of :ref{to="avoidance/disjunctive-question"}). If an infinite subset $H$ of $A$ or of $\overline A$ belongs to $\mathcal M$, then $Z \oplus H \in \mathcal M \subseteq \mathcal W$ and we are done. Otherwise both sides can always be extended, and :ref{#lem-disjunctive-non-sigma1}, with Lachlan's disjunction as in :ref{#lem-disjunctive-construction}, gives a side $G_i$, infinite and contained in $A$ or $\overline A$, such that $W^{Z \oplus G_i}_e \neq C$ for every $e$.
3. With the same $\mathcal M$, use the Seetapun forcing (:ref{#def-seetapun-forcing}) for a $Z$-computable coloring and its question (:ref{#lem-seetapun-question}). The proof of :ref{#thm-seetapun-direct} uses about $\mathcal M$ only that it is a Scott ideal containing $Z$ and that $C$ is not computable in its members, the latter in :ref{#lem-disjunctive-cone} and for the assumption (H). Replace :ref{#lem-disjunctive-cone} by :ref{#lem-disjunctive-non-sigma1}, and (H) by the same assumption for the new $\mathcal M$: an infinite homogeneous set $H \in \mathcal M$ gives $Z \oplus H \in \mathcal W$.
:::

The scheme is the same in the three items, and it will be the same for hyperimmunities: one first shows that $\mathsf{WKL}$ preserves the property, which provides the reservoirs; the notion of forcing that builds solutions comes with a question whose answers are $\Sigma^0_1$ relative to a reservoir; and the abstract theorem, simple or disjunctive, does the rest. Only the first step and the abstract theorem depend on the property.

:::quiz[applications]
In item 2 of the proof of :ref{#thm-non-sigma1-examples}, why must the Scott ideal $\mathcal M$ be built by preserving $\mathcal W$, rather than taken as in :ref{#lem-scott-cone}?

- [x] Because the abstract lemma needs $C$ to be non-$\Sigma^0_1$ relative to every member of $\mathcal M$; a Scott ideal avoiding a cone only guarantees that $C$ is not computable in its members.
- [ ] Because :ref{#lem-scott-cone} needs $C$ to be non-computable.

  $C$ is not $\Sigma^0_1(Z)$, hence not computable in $Z$, so :ref{#lem-scott-cone} would apply; the issue is what it guarantees.
- [ ] Because $\mathcal M$ must contain the instance $A$.

  $A$ is arbitrary and need not belong to $\mathcal M$.
:::

## One definition, not two

The disjunctive arguments preserve one non-$\Sigma^0_1$ definition at a time. To preserve two sets $C_0$ and $C_1$, Lachlan's disjunction gives a side $i_0$ on which $C_0$ is preserved and a side $i_1$ on which $C_1$ is preserved, and nothing forces $i_0 = i_1$ (last exercise of :ref{to="avoidance/disjunctive-question"}). For cones this limitation is only apparent: by a theorem of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky, avoidance of one cone implies avoidance of countably many. For non-$\Sigma^0_1$ definitions it is real: Patey proved that $\mathsf{RT}^2_2$ admits preservation of one but not of two non-$\Sigma^0_1$ definitions, while Wang proved that $\mathsf{WKL}$ and the Erdős–Moser theorem admit preservation of countably many. Preservation of several definitions is therefore a finer tool than cone avoidance, and it separates problems that cone avoidance cannot separate; such separations are the subject of the course on custom properties and forcing design of the track. Going up the arithmetic hierarchy, preservation of non-$\Sigma^0_n$ definitions controls the $(n-1)$-st jump of solutions; for computable Mathias forcing it already fails at $n = 2$ (:ref{#cor-mathias-no-sigma2}), which is the starting point of the course on jump cone avoidance.

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{WKL}$ and $\mathsf{COH}$ admit preservation of countably many non-$\Sigma^0_1$ definitions at once: for every $Z$ and every sequence of sets $C_0, C_1, \dots$, none of which is $\Sigma^0_1(Z)$, every $Z$-computable instance has a solution $Y$ such that no $C_j$ is $\Sigma^0_1(Z \oplus Y)$.

:::solution
In the proof of :ref{#thm-local-non-sigma1}, the dense sets for $C_j$ and $e$ form a countable family, indexed by the pairs $(j, e)$. A sufficiently generic set meets all of them. So every sufficiently generic set for Jockusch–Soare forcing inside the paths of the instance, or for Mathias forcing with $Z$-computable reservoirs, preserves all the definitions.
:::
::::

::::exercise{difficulty=2}
Show directly, without :ref{#thm-non-sigma1-equivalence}, that if $\mathsf P$ admits cone avoidance, then for every $Z$, every c.e. set $A \not\leq_T Z$ and every $Z$-computable instance $X$, there is a solution $Y$ such that $\overline A$ is not $\Sigma^0_1(Z \oplus Y)$. Why does this argument not prove the theorem?

:::solution
Cone avoidance gives $Y$ with $A \not\leq_T Z \oplus Y$. Since $A$ is $\Sigma^0_1$, hence $\Sigma^0_1(Z \oplus Y)$, the set $\overline A$ is not $\Sigma^0_1(Z \oplus Y)$: otherwise $A$ would be computable in $Z \oplus Y$ by Post's theorem relativized. The argument uses that $A$ is c.e., so that only one half of the description of $A$ is missing. A general non-$\Sigma^0_1(Z)$ set $C$ need not be the complement of a $Z$-c.e. set, and avoiding the cone above $C$ does not prevent $C$ from becoming $\Sigma^0_1(Z \oplus Y)$, as in item 3 of :ref{#ex-non-sigma1}.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{COH}$ admits strong preservation of non-$\Sigma^0_1$ definitions.

:::solution
Follow the proof of :ref{#thm-coh-strong-cone}, with conditions $(\sigma, X)$ such that $C$ is not $\Sigma^0_1(Z \oplus X)$, and $\mathcal M$ the class of these sets $Z \oplus X$. The question is $\Sigma^0_1(\mathcal M)$-preserving, so :ref{#thm-local-non-sigma1} applies. For the density of cohesiveness, use item 2 of :ref{#thm-non-sigma1-examples} relative to $Z \oplus X$: the set $\{ k : p(k) \in R_n \}$ has an infinite subset $H$, of it or of its complement, such that $C$ is not $\Sigma^0_1(Z \oplus X \oplus H)$, and $Y = p[H]$ is a new reservoir.
:::
::::

## Notes and references

Preservation of the arithmetic hierarchy was introduced by Wang, who used it to simplify separations involving the Erdős–Moser theorem; the property for one non-$\Sigma^0_1$ set, its consequence for cone avoidance and the abstract theorem with a $\Sigma^0_1$-preserving question follow the section *Preserving definitions* of the chapter *Cone avoidance* of Patey's monograph. The equivalence with cone avoidance is part of Theorem 2.1 of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022) (Lemma 2.13 and Corollary 2.18 there); its proof uses cototal enumeration degrees. That $\mathsf{RT}^2_2$ preserves one but not two non-$\Sigma^0_1$ definitions is the case $k = 1$ of a theorem of Patey (2016) on $\mathsf{RT}^2_{k+1,k}$, as quoted by Downey et al. (2022, Section 1.2).

- W. Wang, *The definability strength of combinatorial principles*, Journal of Symbolic Logic 81 (2016), no. 4, doi:10.1017/jsl.2016.10; arXiv:1408.1465.
- L. Patey, *The weakness of being cohesive, thin or free in reverse mathematics*, Israel Journal of Mathematics 216 (2016), 905–955.
- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Preserving definitions*.
