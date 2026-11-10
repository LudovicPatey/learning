---
title: The Posner–Robinson theorem
summary: Coding a set into a 1-generic set so that it can be decoded with any non-computable set; the Posner–Robinson join theorem and Friedberg's jump inversion theorem.
duration: 35
prerequisites: [one-genericity]
---

Genericity is usually a tool for building sets with few computational abilities. Combined with **coding**, it also produces sets with prescribed strength. The idea is to build a 1-generic set $G$ that carries a given set $Z$ in its bits, in such a way that the coding can be read back with the help of an arbitrary non-computable set $A$. The resulting theorem, due in this form to Jockusch and Shore, has two classical consequences: the Posner–Robinson theorem, which says that every non-computable set joins with some set to compute the jump of the latter, and Friedberg's jump inversion theorem, admitted in the course on Turing degrees, which says that every degree above $\obf'$ is a jump.

:::theorem[Jockusch–Shore]{#thm-jockusch-shore}
Let $A$ and $Z$ be sets, with $A$ not computable. There is a 1-generic set $G$ such that $Z \leq_T A \oplus G$ and $G \leq_T A \oplus Z \oplus \emptyset'$.
:::

## The construction

We may assume that $A$ is not c.e. Indeed, if $A$ is c.e., then its complement is not c.e., since $A$ is not computable; and the complement is Turing equivalent to $A$, so it can replace $A$ in the statement. Fix an enumeration $(W_e)$ of the c.e. sets of strings.

We build strings $\sigma_0 \preceq \sigma_1 \preceq \cdots$, starting with $\sigma_0 = \varepsilon$, and let $G$ be their limit. At step $e$, given $\sigma_e$, write $i = Z(e)$ and consider the set
$$
D_e = \{ m : \text{some extension of } \sigma_e\, i\, 0^m\, 1 \text{ belongs to } W_e \}.
$$
It is c.e. Since $A$ is not c.e., $A \neq D_e$; so there is $m$ with either $m \in D_e \setminus A$ or $m \in A \setminus D_e$. Let $m$ be the least such number.

- If $m \in D_e \setminus A$, let $\sigma_{e+1}$ be the first extension of $\sigma_e\, i\, 0^m\, 1$ enumerated into $W_e$. Then $G$ meets $W_e$.
- If $m \in A \setminus D_e$, let $\sigma_{e+1} = \sigma_e\, i\, 0^m\, 1$. Then no extension of $\sigma_{e+1}$ belongs to $W_e$: $\sigma_{e+1}$ avoids $W_e$.

:::proof{of=thm-jockusch-shore}
*$G$ is 1-generic.* At each step $e$, $G$ meets $W_e$ or has a prefix avoiding it, so $G$ meets $W_e \cup W_e^\perp$.

*$G \leq_T A \oplus Z \oplus \emptyset'$.* The bit $Z(e)$ is read from $Z$. The membership $m \in D_e$ is a c.e. question, answered by $\emptyset'$, and $m \in A$ is answered by $A$; so the least $m$ is found. In the first case, the first extension enumerated into $W_e$ is found by a computable search. So the sequence $(\sigma_e)$ is computable in $A \oplus Z \oplus \emptyset'$.

*$Z \leq_T A \oplus G$.* We compute the sequence $(\sigma_e)$ from $A \oplus G$, by induction. Suppose $\sigma_e$ is known. The bit of $G$ following $\sigma_e$ is $Z(e)$. Then read the number $m$ of zeros that follow, up to the next $1$; by construction it is the number chosen at step $e$. If $m \in A$, step $e$ was in the second case, and $\sigma_{e+1} = \sigma_e\, Z(e)\, 0^m\, 1$. If $m \notin A$, step $e$ was in the first case, so $m \in D_e$, and $\sigma_{e+1}$ is the first extension of $\sigma_e\, Z(e)\, 0^m\, 1$ enumerated into $W_e$, found by a computable search, which terminates. Hence $A \oplus G$ computes every bit $Z(e)$.
:::

The decoding uses $A$ for a single question at each step: is $m$ in $A$? The construction chose $m$ precisely so that the answer distinguishes the two cases, which is possible because $A$ is not c.e. A c.e. set $A$ could coincide with $D_e$, leaving no such $m$.

:::quiz[the Jockusch–Shore construction]
Why does the construction need $A$ not to be c.e., rather than only non-computable?

- [x] Because it needs, at each step, a number on which $A$ and the c.e. set $D_e$ differ; if $A$ were c.e., it could equal $D_e$.

  The reduction to the non-c.e. case is harmless, since a non-computable c.e. set has a non-c.e. complement of the same degree.
- [ ] Because otherwise $G$ would not be 1-generic.

  Genericity is ensured in both cases at each step; the hypothesis is used to choose $m$.
- [ ] Because $\emptyset'$ cannot answer questions about c.e. sets.

  It can: membership in a c.e. set is a c.e. question.

---

When decoding, why does $m \notin A$ imply that step $e$ was in the first case?

- [x] The chosen $m$ is either in $D_e \setminus A$ (first case) or in $A \setminus D_e$ (second case); if $m \notin A$, only the first is possible.
- [ ] Because $m \notin A$ implies $m \notin D_e$.

  The opposite holds in the first case: $m \in D_e$ and $m \notin A$.
- [ ] Because the second case never happens.

  It happens whenever the least disagreement between $A$ and $D_e$ is an element of $A$.
:::

## Consequences

:::corollary[Posner–Robinson]{#cor-posner-robinson}
For every non-computable set $A$, there is a set $G$ with $A \oplus G \geq_T G'$. If moreover $A \leq_T \emptyset'$, then $A \oplus G \equiv_T G'$.
:::

:::proof{of=cor-posner-robinson}
Apply :ref{#thm-jockusch-shore} with $Z = \emptyset'$: $G$ is 1-generic, $\emptyset' \leq_T A \oplus G$, and $G \leq_T A \oplus \emptyset'$. Since $G$ is 1-generic, $G' \leq_T G \oplus \emptyset'$ (:ref{#thm-generic-low}), and $G \oplus \emptyset' \leq_T A \oplus G$. If $A \leq_T \emptyset'$, then $A \leq_T \emptyset' \leq_T G'$ and $G \leq_T G'$, so $A \oplus G \leq_T G'$.
:::

So every non-computable set, however weak, bridges the gap between some set and its jump. For a low non-computable $A$, this gives a set $G$ with $A \oplus G \equiv_T G' \geq_T \emptyset'$ while $A$ alone is far from $\emptyset'$.

:::corollary[Friedberg's jump inversion theorem]{#cor-jump-inversion}
For every set $Z \geq_T \emptyset'$, there is a 1-generic set $G$ with $G' \equiv_T Z$, and moreover $G \oplus \emptyset' \equiv_T Z$.
:::

:::proof{of=cor-jump-inversion}
Apply :ref{#thm-jockusch-shore} with $A = \emptyset'$, which is not computable: $G$ is 1-generic, $Z \leq_T \emptyset' \oplus G$ and $G \leq_T \emptyset' \oplus Z \oplus \emptyset' \equiv_T Z$. Hence $G \oplus \emptyset' \equiv_T Z$, and $G' \leq_T G \oplus \emptyset'$ since $G$ is 1-generic (:ref{#thm-generic-low}). The converse $G \oplus \emptyset' \leq_T G'$ holds for every set, so $G' \equiv_T Z$.
:::

:::corollary{#cor-high-not-dnc}
There is a high set that computes no DNC function; in particular, a high set that is not Turing complete.
:::

:::proof{of=cor-high-not-dnc}
By :ref{#cor-jump-inversion} with $Z = \emptyset''$, there is a 1-generic $G$ with $G' \equiv_T \emptyset''$, so $G$ is high. By :ref{#thm-generic-not-dnc}, $G$ computes no DNC function; since $\emptyset'$ computes one, $G$ does not compute $\emptyset'$.
:::

This gives a second construction of high incomplete sets, after :ref{#cor-high-incomplete}; the generic set obtained is even computable in $\emptyset''$.

## Exercises

::::exercise{difficulty=1}
Show that every set $Z \geq_T \emptyset'$ is the join of $\emptyset'$ with a set $G$ such that $G \not\geq_T \emptyset'$.

:::solution
Take $G$ as in :ref{#cor-jump-inversion}: $Z \equiv_T G \oplus \emptyset'$, and $G$ is 1-generic, so it computes no DNC function, hence not $\emptyset'$.
:::
::::

::::exercise{difficulty=1}
Let $A \leq_T \emptyset'$ be non-computable. Show that there is a low 1-generic set $G$ with $A \oplus G \equiv_T \emptyset'$.

:::solution
Apply :ref{#thm-jockusch-shore} with $Z = \emptyset'$. Then $G$ is 1-generic, $\emptyset' \leq_T A \oplus G$, and $G \leq_T A \oplus \emptyset' \equiv_T \emptyset'$. Hence $A \oplus G \leq_T \emptyset'$, so $A \oplus G \equiv_T \emptyset'$. Since $G$ is 1-generic and $\Delta^0_2$, $G' \leq_T G \oplus \emptyset' \equiv_T \emptyset'$ by :ref{#thm-generic-low}, so $G$ is low.
:::
::::

## Notes and references

Posner and Robinson proved their join theorem in 1981, answering a question on the degrees below $\obf'$. The general form with an arbitrary coded set $Z$ and the use of 1-generic sets is due to Jockusch and Shore (1984). Friedberg's jump inversion theorem dates from 1957.

- D. B. Posner and R. W. Robinson, *Degrees joining to 0′*, Journal of Symbolic Logic 46 (1981), 714–722.
- C. G. Jockusch and R. A. Shore, *Pseudo-jump operators II: transfinite iterations, hierarchies and minimal covers*, Journal of Symbolic Logic 49 (1984), 1205–1236.
- R. M. Friedberg, *A criterion for completeness of degrees of unsolvability*, Journal of Symbolic Logic 22 (1957), 159–160.
