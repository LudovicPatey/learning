---
title: Cohesive sets
summary: Cohesive sets and the principle COH; a set computes a cohesive set for a computable sequence if and only if its jump computes a path through a Π⁰₁(∅′) class of decisions; cohesive sets for computable sequences can be low₂ but not always low.
duration: 40
prerequisites: [jockusch]
---

The proof of Ramsey's theorem for pairs through pre-homogeneous sets mixes two different tasks. The first is to make the coloring **stable**, so that each element has a limit color; the second is to choose an infinite set of elements with the same limit color. Cholak, Jockusch and Slaman (2001) isolated the two tasks as separate principles. This lesson studies the first one, the **cohesiveness principle**: given countably many sets, find an infinite set that each of them splits in a trivial way. The next lesson studies stable colorings and shows how the two principles combine into Ramsey's theorem for pairs.

## Cohesive sets

Write $X \subseteq^* Y$ if $X \setminus Y$ is finite.

:::definition{#def-cohesive}
Let $\vec R = (R_i)_{i \in \nat}$ be a sequence of sets. An infinite set $C$ is **$\vec R$-cohesive** if for every $i$, $C \subseteq^* R_i$ or $C \subseteq^* \overline{R_i}$. The **cohesiveness principle** $\mathsf{COH}$ states that every sequence of sets has a cohesive set.
:::

A cohesive set cannot be split by any of the sets $R_i$ into two infinite parts. Each $R_i$ is a $2$-coloring of $\nat$, and a cohesive set is an infinite set on which every one of these colorings is constant up to finitely many exceptions: it solves countably many instances of the pigeonhole principle at once, up to finite error. The finite error is necessary, since the sets $R_i = \{ i \}$ have no infinite set homogeneous for all of them. Every infinite subset of an $\vec R$-cohesive set is $\vec R$-cohesive. Sets cohesive for the sequence of all computable sets are called **r-cohesive**; they are the computability-theoretic analogues of non-principal ultrafilters, restricted to countably many sets.

:::example{#ex-cohesive}
1. If each $R_i$ is finite or cofinite, every infinite set is $\vec R$-cohesive.
2. Let $R_i$ be the set of numbers whose binary expansion has the digit $1$ at position $i$. The set $C = \{ 2^k : k \in \nat \}$ is cohesive: for every $i$, $2^k \notin R_i$ for $k > i$, so $C \subseteq^* \overline{R_i}$. The set of odd numbers is not: it is split by $R_1$ into two infinite parts.
3. Some computable sequences have no computable cohesive set, and even no low one (:ref{#prop-coh-no-low} below).
:::

To build a cohesive set, one decides, for each $i$ in turn, on which side of $R_i$ the set will eventually lie. For a string $\sigma \in 2^{<\nat}$, let
$$
R^\sigma = \bigcap_{i < |\sigma|,\ \sigma(i) = 1} R_i \ \cap \bigcap_{i < |\sigma|,\ \sigma(i) = 0} \overline{R_i},
$$
the set of numbers that agree with the decisions $\sigma$. A decision is acceptable if $R^\sigma$ is infinite. Since $R^\sigma = R^{\sigma 0} \sqcup R^{\sigma 1}$, every acceptable decision has an acceptable extension, and the infinite sequences of acceptable decisions form the class
$$
\mathcal C(\vec R) = \{ P \in \cs : R^{P \uh n} \text{ is infinite for every } n \}.
$$

:::proposition{#prop-cohesive-exists}
Every sequence $\vec R$ has an $\vec R$-cohesive set computable in $\vec R''$.
:::

:::proof{of=prop-cohesive-exists}
Define a sequence $P \in \cs$ by $P(i) = 1$ if $R^{(P \uh i) 1}$ is infinite, and $P(i) = 0$ otherwise. By induction, each $R^{P \uh i}$ is infinite, so $P \in \mathcal C(\vec R)$. Each decision asks whether an $\vec R$-computable set, given by an index computed from the previous decisions, is infinite: a $\Pi^0_2(\vec R)$ question, answered by $\vec R''$. Let $c_i$ be the least element of $R^{P \uh (i + 1)}$ larger than $c_{i-1}$, and $C = \{ c_0 < c_1 < \cdots \}$. For each $i$, all $c_j$ with $j \geq i$ belong to $R^{P \uh (j+1)} \subseteq R^{P \uh (i+1)}$, which is contained in $R_i$ or in $\overline{R_i}$. So $C$ is cohesive, and $\vec R''$-computable.
:::

## The decision class

The proof of :ref{#prop-cohesive-exists} uses $\vec R''$ to find a member $P$ of $\mathcal C(\vec R)$, and then only $\vec R \oplus P$ to build the cohesive set. The following characterization shows that much less is needed. For a computable sequence, $\mathcal C(\vec R)$ is a $\Pi^0_1(\emptyset')$ class: $P \in \mathcal C(\vec R)$ if and only if $R^{P \uh n}$ has at least $n$ elements for every $n$, and each of these conditions is decided by $\emptyset'$. It is non-empty by the remark above.

:::proposition{#prop-coh-decisions}
Let $\vec R$ be a computable sequence of sets. A set $X$ computes an $\vec R$-cohesive set if and only if $X'$ computes a member of $\mathcal C(\vec R)$.
:::

:::proof{of=prop-coh-decisions}
($\Rightarrow$) Let $C \leq_T X$ be cohesive, and let $P(i) = 1$ if $C \subseteq^* R_i$, and $P(i) = 0$ otherwise. For every $n$, $C \subseteq^* R^{P \uh n}$, as a finite intersection of sets almost containing $C$, so $R^{P \uh n}$ is infinite and $P \in \mathcal C(\vec R)$. Let $c_0 < c_1 < \cdots$ enumerate $C$. Then $P(i) = \lim_s R_i(c_s)$, a limit of a $C$-computable function; by the limit lemma relativized to $C$, $P \leq_T C' \leq_T X'$.

($\Leftarrow$) Let $P \in \mathcal C(\vec R)$ with $P \leq_T X'$. By the limit lemma relativized to $X$, there is an $X$-computable function $g$ with $\lim_t g(i, t) = P(i)$ for every $i$. Define $x_0 < x_1 < \cdots$ computably in $X$: at step $s$, search for a string $\sigma$ of length $s$ and a number $x$, larger than $x_{s-1}$ if $s > 0$, with $x \in R^\sigma$ and $g(i, x) = \sigma(i)$ for all $i < s$, and let $x_s$ be the $x$ found. The search terminates: there is $t_0$ such that $g(i, t) = P(i)$ for all $t > t_0$ and $i < s$, and since $R^{P \uh s}$ is infinite, any $x \in R^{P \uh s}$ above $t_0$ and $x_{s-1}$ works with $\sigma = P \uh s$. Let $C = \{ x_s : s \in \nat \}$, an infinite $X$-computable set. Fix $i$, and $t_1$ with $g(i, t) = P(i)$ for $t > t_1$. For every $s > i$ with $x_s > t_1$, the string $\sigma$ found at step $s$ satisfies $\sigma(i) = g(i, x_s) = P(i)$, and $x_s \in R^\sigma$; so $x_s \in R_i$ if $P(i) = 1$, and $x_s \notin R_i$ if $P(i) = 0$. All but finitely many $s$ qualify, so $C \subseteq^* R_i$ or $C \subseteq^* \overline{R_i}$.
:::

The idea of ($\Leftarrow$) is that $X$ does not need to know the decisions $P$: it uses the approximation $g(i, x)$ at the very number $x$ it is about to add. Late elements are added under correct guesses, and early mistakes only cost finitely many elements. The proposition says that $\mathsf{COH}$ for computable instances behaves like weak König's lemma one jump up, with the caveat that the jump is taken of the solution, not of an oracle above $\emptyset'$.

:::corollary[Jockusch, Stephan]{#cor-coh-bounds}
Let $\vec R$ be a computable sequence.
1. Every set $X$ such that $X'$ is PA relative to $\emptyset'$ computes an $\vec R$-cohesive set. In particular $\emptyset'$ computes one.
2. For every set $P$ PA relative to $\emptyset'$, there is an $\vec R$-cohesive set $C$ with $C' \leq_T P$. There is a cohesive set $C$ with $C'' \leq_T \emptyset''$ (a **low₂** set).
:::

:::proof{of=cor-coh-bounds}
1. A set PA relative to $\emptyset'$ computes a member of every non-empty $\Pi^0_1(\emptyset')$ class (:ref{#thm-pa-characterization}, relativized). Apply :ref{#prop-coh-decisions}. The set $\emptyset'' = (\emptyset')'$ is PA relative to $\emptyset'$.
2. $P$ computes $\emptyset'$ (second exercise of :ref{to="pi01-classes/pa-degrees"}). By Friedberg's jump inversion theorem (admitted in :ref{to="turing-degrees/low-and-high"}), there is $X$ with $X' \equiv_T P$. By (1), $X$ computes a cohesive set $C$, and $C' \leq_T X' \equiv_T P$. By the low basis theorem relativized to $\emptyset'$, $P$ can be chosen with $P' \leq_T \emptyset''$; then $C'' \leq_T P' \leq_T \emptyset''$.
:::

The converse of (1) also holds: every non-empty $\Pi^0_1(\emptyset')$ class is $\mathcal C(\vec R)$ for some computable sequence $\vec R$ (Brattka and Rakotoniaina; Patey), so a set computes a cohesive set for every computable sequence if and only if its jump is PA relative to $\emptyset'$ (Jockusch and Stephan). We admit it. The next proposition proves the special case that matters for reverse mathematics.

:::proposition[Jockusch, Stephan]{#prop-coh-no-low}
There is a computable sequence $\vec R$ such that the jump of every $\vec R$-cohesive set is PA relative to $\emptyset'$. In particular, no $\vec R$-cohesive set is low, and $\mathsf{WKL}_0$ does not prove $\mathsf{COH}$.
:::

:::proof{of=prop-coh-no-low}
Let $R_e = \{ s : \Phi^{\emptyset'_s}_e(e)[s]\converge = 0 \}$, a computable sequence. If $\Phi^{\emptyset'}_e(e)$ converges with use $u$, then for all large $s$, $\emptyset'_s$ agrees with $\emptyset'$ below $u$ and the computation converges in $s$ steps, so $\Phi^{\emptyset'_s}_e(e)[s] = \Phi^{\emptyset'}_e(e)$. Hence $R_e$ is cofinite if $\Phi^{\emptyset'}_e(e)\converge = 0$, and finite if $\Phi^{\emptyset'}_e(e)$ converges to another value.

Let $C$ be cohesive, and $P(e) = 1$ if $C \subseteq^* R_e$, and $P(e) = 0$ otherwise. As in the proof of :ref{#prop-coh-decisions}, $P \leq_T C'$. If $\Phi^{\emptyset'}_e(e)\converge = 0$, then $C \subseteq^* R_e$ and $P(e) = 1$; if $\Phi^{\emptyset'}_e(e)$ converges to $v \neq 0$, then $C \subseteq^* \overline{R_e}$ and $P(e) = 0 \neq v$. So $P$ is a $\{0, 1\}$-valued function DNC relative to $\emptyset'$, and $C'$ is PA relative to $\emptyset'$. No $\emptyset'$-computable function is DNC relative to $\emptyset'$, so $C' \not\leq_T \emptyset'$. Finally, the ω-model of :ref{#thm-low-scott} consists of low sets and satisfies $\mathsf{WKL}_0$; it contains $\vec R$ and no $\vec R$-cohesive set.
:::

:::quiz[cohesive sets and their jumps]
In the proof of :ref{#prop-coh-decisions} ($\Rightarrow$), why is $P$ computable in $C'$ rather than in $C$?

- [x] Because $P(i)$ is the eventual value of $R_i(c_s)$ along the enumeration of $C$; the limit lemma relativized to $C$ computes such a limit from $C'$, and $C$ alone cannot tell when the values have stabilized.
- [ ] Because $\vec R$ is computable only in $\emptyset'$.

  $\vec R$ is computable by hypothesis.
- [ ] Because $C$ is not computable.

  Even for a computable cohesive set, the decisions are in general only limit computable.

---

In the proof of :ref{#prop-coh-no-low}, what would go wrong if $R_e$ were defined from $\Phi^{\emptyset'}_e(e)$ itself rather than from its stage-$s$ approximations?

- [x] The sequence $\vec R$ would no longer be computable, and the proposition would say nothing about computable instances.
- [ ] The function $P$ would no longer be DNC relative to $\emptyset'$.

  It would still be; the point of the approximations is the computability of $\vec R$.
- [ ] Cohesive sets would no longer exist.

  Every sequence has cohesive sets (:ref{#prop-cohesive-exists}).
:::

## Exercises

::::exercise{difficulty=1}
Show that every infinite subset of an $\vec R$-cohesive set is $\vec R$-cohesive, and that a set is r-cohesive if and only if it is cohesive for the sequence of all computable sets $(\Phi_e)$, where $\Phi_e$ is replaced by $\emptyset$ when it is not the characteristic function of a set.

:::solution
If $C \subseteq^* R_i$ and $D \subseteq C$, then $D \setminus R_i \subseteq C \setminus R_i$ is finite. The second statement is the definition: the sequence lists every computable set, together with copies of $\emptyset$, for which cohesiveness is automatic since $C \subseteq \overline{\emptyset}$.
:::
::::

::::exercise{difficulty=1}
A set $X$ is **high** if $\emptyset'' \leq_T X'$. Show that every high set computes a cohesive set for every computable sequence.

:::solution
The class $\mathcal C(\vec R)$ has a member computable in $\emptyset''$, the sequence $P$ of the proof of :ref{#prop-cohesive-exists}. So $X'$ computes a member, and :ref{#prop-coh-decisions} applies.
:::
::::

## Notes and references

Cohesive sets were studied by Jockusch and Stephan (1993), who proved :ref{#prop-coh-no-low} and both parts of :ref{#cor-coh-bounds}, the second in the form $C' \leq_T P$ for every $P$ PA relative to $\emptyset'$ (Hirschfeldt, Theorems 6.34, 6.44 and 6.45; Dzhafarov–Mummert, Theorem 8.4.13). The characterization by the class $\mathcal C(\vec R)$, :ref{#prop-coh-decisions} and its converse, is due independently to Brattka and Rakotoniaina and to Patey; our presentation follows the section *Cohesiveness principle* of Monin and Patey. The construction of cohesive sets below $\vec R''$ is classical (Hirschfeldt, §6.4–6.5, Exercise 6.42 and the discussion before it). The decomposition of Ramsey's theorem for pairs, which motivates the principle, is due to Cholak, Jockusch and Slaman (2001).

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- V. Brattka and T. Rakotoniaina, *On the uniform computational content of Ramsey's theorem*, Journal of Symbolic Logic 82 (2017), 1278–1316.
- L. Patey, *The weakness of being cohesive, thin or free in reverse mathematics*, Israel Journal of Mathematics 216 (2016), 905–955.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.
