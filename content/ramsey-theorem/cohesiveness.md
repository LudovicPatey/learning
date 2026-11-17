---
title: Cohesive sets
summary: Cohesive sets and the principle COH; a set computes a cohesive set for a computable sequence if and only if its jump computes a path through a Π⁰₁(∅′) class of decisions; cohesive sets for computable sequences can be low₂ but not always low.
duration: 35
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
2. $P$ computes $\emptyset'$ (:ref{#ex-pa-relative}). By Friedberg's jump inversion theorem (admitted in :ref{to="turing-degrees/low-and-high"}), there is $X$ with $X' \equiv_T P$. By (1), $X$ computes a cohesive set $C$, and $C' \leq_T X' \equiv_T P$. By the low basis theorem relativized to $\emptyset'$, $P$ can be chosen with $P' \leq_T \emptyset''$; then $C'' \leq_T P' \leq_T \emptyset''$.
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

::::exercise{#ex-high-computes-cohesive difficulty=1 objective="Apply the characterization by decisions to show that high sets compute cohesive sets."}
A set $X$ is **high** if $\emptyset'' \leq_T X'$. Show that every high set computes a cohesive set for every computable sequence.

:::solution
The class $\mathcal C(\vec R)$ has a member computable in $\emptyset''$, the sequence $P$ of the proof of :ref{#prop-cohesive-exists}. So $X'$ computes a member, and :ref{#prop-coh-decisions} applies.
:::
::::

## Notes and references

The low₂ bound for Ramsey's theorem for pairs is proved in the course on lowness (:ref{to="lowness/cjs-theorem"}); control of the second jump of cohesive sets is studied in the course on jump cone avoidance (:ref{to="jump-cone-avoidance/cohesiveness-second-jump"}).

Cohesive sets were studied by Jockusch and Stephan (1993), who proved :ref{#prop-coh-no-low} and both parts of :ref{#cor-coh-bounds}, the second in the form $C' \leq_T P$ for every $P$ PA relative to $\emptyset'$ (Hirschfeldt, Theorems 6.34, 6.44 and 6.45; Dzhafarov–Mummert, Theorem 8.4.13). The characterization by the class $\mathcal C(\vec R)$, :ref{#prop-coh-decisions} and its converse, is due independently to Brattka and Rakotoniaina and to Patey; our presentation follows the section *Cohesiveness principle* of Monin and Patey. The construction of cohesive sets below $\vec R''$ is classical (Hirschfeldt, §6.4–6.5, Exercise 6.42 and the discussion before it). The decomposition of Ramsey's theorem for pairs, which motivates the principle, is due to Cholak, Jockusch and Slaman (2001).

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- V. Brattka and T. Rakotoniaina, *On the uniform computational content of Ramsey's theorem*, Journal of Symbolic Logic 82 (2017), 1278–1316.
- L. Patey, *The weakness of being cohesive, thin or free in reverse mathematics*, Israel Journal of Mathematics 216 (2016), 905–955.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.

:::::exercises
::::exercise{#ex-cohesive-subsets difficulty=1 objective="Check two closure properties of cohesiveness from the definition."}
Show that every infinite subset of an $\vec R$-cohesive set is $\vec R$-cohesive, and that a set is r-cohesive if and only if it is cohesive for the sequence of all computable sets $(\Phi_e)$, where $\Phi_e$ is replaced by $\emptyset$ when it is not the characteristic function of a set.

:::solution
If $C \subseteq^* R_i$ and $D \subseteq C$, then $D \setminus R_i \subseteq C \setminus R_i$ is finite. The second statement is the definition: the sequence lists every computable set, together with copies of $\emptyset$, for which cohesiveness is automatic since $C \subseteq \overline{\emptyset}$.
:::
::::

::::exercise{#ex-cohesive-divisibility difficulty=1 objective="Recognize cohesive sets for a concrete sequence and compute their decisions."}
Let $R_i = \{ x : i + 1 \text{ divides } x \}$.

1. Show that $\{ k! : k \geq 1 \}$ and the set of prime numbers are $\vec R$-cohesive, and compute, for each of them, the sequence $P$ with $P(i) = 1$ if the set is almost contained in $R_i$ and $P(i) = 0$ otherwise.
2. Show that the set of odd numbers is not $\vec R$-cohesive.

:::solution
1. For $k \geq i + 1$, $i + 1$ divides $k!$, so $\{ k! : k \geq 1 \} \subseteq^* R_i$ for every $i$, and $P = 111\cdots$. The set is infinite, since $k! < (k+1)!$ for $k \geq 1$. Every prime belongs to $R_0 = \nat$. For $i \geq 1$, a prime $p$ belongs to $R_i$ only if $p = i + 1$, so the primes are almost contained in $\overline{R_i}$, and $P = 1000\cdots$.
2. The odd multiples of $3$ ($3, 9, 15, \dots$) and the odd numbers not divisible by $3$ ($1, 5, 7, \dots$) are both infinite, so $R_2$ splits the odd numbers into two infinite parts.
:::
::::

::::exercise{#ex-decision-class-pi01 difficulty=1 objective="Complete the step showing that the class of decisions of a computable sequence is $\Pi^0_1(\emptyset')$."}
Let $\vec R$ be a computable sequence. Show that $P \in \mathcal C(\vec R)$ if and only if $R^{P \uh n}$ has at least $n$ elements for every $n$, and deduce that $\mathcal C(\vec R)$ is a $\Pi^0_1(\emptyset')$ class.

:::solution
If every $R^{P \uh n}$ is infinite, each has at least $n$ elements. Conversely, suppose that $R^{P \uh n}$ is finite for some $n$, with $N$ elements. For $m \geq \max(n, N + 1)$, $R^{P \uh m} \subseteq R^{P \uh n}$ has at most $N < m$ elements. So the condition fails for $m$.

The sets $R^\sigma$ are computable, uniformly in $\sigma$, so "$R^\sigma$ has at least $n$ elements" is a $\Sigma^0_1$ property of $(\sigma, n)$, decided by $\emptyset'$. The tree $T = \{ \sigma : R^{\sigma \uh n} \text{ has at least } n \text{ elements for every } n \leq |\sigma| \}$ is therefore $\emptyset'$-computable, and $\mathcal C(\vec R)$ is the class of its paths.
:::
::::

::::exercise{#ex-decision-class-singleton difficulty=1 objective="Compute the class of decisions of a sequence that approximates the halting set."}
Let $R_i = \{ s : i \in \emptyset'_s \}$, where $(\emptyset'_s)$ is the usual increasing approximation of $\emptyset'$. Show that $\mathcal C(\vec R) = \{ \emptyset' \}$ and that every infinite set is $\vec R$-cohesive. Check that this agrees with :ref{#prop-coh-decisions}.

:::solution
If $i \in \emptyset'$, then $i \in \emptyset'_s$ for all large $s$, and $R_i$ is cofinite; otherwise $R_i = \emptyset$. Let $P \in \mathcal C(\vec R)$. If $P(i) = 1$ and $i \notin \emptyset'$, then $R^{P \uh (i + 1)} \subseteq R_i = \emptyset$; if $P(i) = 0$ and $i \in \emptyset'$, then $R^{P \uh (i + 1)} \subseteq \overline{R_i}$, which is finite. Both contradict $P \in \mathcal C(\vec R)$, so $P = \emptyset'$. Conversely, $R^{\emptyset' \uh n}$ is the intersection of finitely many cofinite sets and complements of the empty set, so it is cofinite, and $\emptyset' \in \mathcal C(\vec R)$.

Every $R_i$ is finite or cofinite, so every infinite set is cohesive (:ref{#ex-cohesive}). Accordingly, :ref{#prop-coh-decisions} says that a set $X$ computes a cohesive set if and only if $X'$ computes $\emptyset'$, which holds for every $X$.
:::
::::

::::exercise{#ex-coh-all-sequences difficulty=2 objective="Derive the degrees that compute cohesive sets for all computable sequences, and see that cohesiveness never forces highness."}
1. Show that a set $X$ computes a cohesive set for every computable sequence if and only if $X'$ is PA relative to $\emptyset'$.
2. Show that every computable sequence has a cohesive set that is not high, that is, whose jump does not compute $\emptyset''$.

:::solution
1. If $X'$ is PA relative to $\emptyset'$, $X$ computes a cohesive set for every computable sequence by :ref{#cor-coh-bounds} (1). Conversely, let $\vec R$ be the sequence of :ref{#prop-coh-no-low}, and $C \leq_T X$ an $\vec R$-cohesive set. Then $C' \leq_T X'$, and $C'$ computes a $\{0, 1\}$-valued function DNC relative to $\emptyset'$, so $X'$ does too: $X'$ is PA relative to $\emptyset'$.
2. By :ref{#cor-coh-bounds} (2), there is a cohesive set $C$ with $C'' \leq_T \emptyset''$. If $\emptyset'' \leq_T C'$, then $\emptyset''' \leq_T C'' \leq_T \emptyset''$, by monotonicity of the jump, which is impossible.

Item 1 does not need the admitted converse of :ref{#cor-coh-bounds} (1), which concerns a single sequence; it uses only the particular sequence of :ref{#prop-coh-no-low}.
:::
::::

::::exercise{#ex-cohesive-union difficulty=1 objective="Relate the union of two cohesive sets to their sequences of decisions."}
For an $\vec R$-cohesive set $C$, let $P_C(i) = 1$ if $C \subseteq^* R_i$ and $P_C(i) = 0$ otherwise. Show that for $\vec R$-cohesive sets $C$ and $D$, the set $C \cup D$ is $\vec R$-cohesive if and only if $P_C = P_D$.

:::solution
Since $C$ is infinite, it cannot be almost contained in both $R_i$ and $\overline{R_i}$; so $P_C(i) = 0$ means $C \subseteq^* \overline{R_i}$. If $P_C = P_D$, then for each $i$, $C$ and $D$ are almost contained in the same set $R_i$ or $\overline{R_i}$, and so is $C \cup D$, which is infinite. Conversely, if $C \cup D$ is cohesive, then $C$ and $D$ are infinite subsets of it: if $C \cup D \subseteq^* R_i$, then $C \subseteq^* R_i$ and $D \subseteq^* R_i$, so $P_C(i) = P_D(i) = 1$; if $C \cup D \subseteq^* \overline{R_i}$, then both are almost contained in $\overline{R_i}$, and $P_C(i) = P_D(i) = 0$.
:::
::::

::::exercise{#ex-computable-cohesive-delta2 difficulty=2 objective="Characterize the computable sequences with a computable cohesive set through their class of decisions."}
Let $\vec R$ be a computable sequence. Show that $\vec R$ has a computable cohesive set if and only if $\mathcal C(\vec R)$ has a $\Delta^0_2$ member. For the sequence of :ref{#prop-coh-no-low}, show directly that every member of $\mathcal C(\vec R)$ is DNC relative to $\emptyset'$, and deduce again that it has no computable cohesive set.

:::solution
Apply :ref{#prop-coh-decisions} with $X = \emptyset$: a computable cohesive set exists if and only if $\emptyset'$ computes a member of $\mathcal C(\vec R)$, that is, if and only if $\mathcal C(\vec R)$ has a $\Delta^0_2$ member.

Now let $R_e = \{ s : \Phi^{\emptyset'_s}_e(e)[s]\converge = 0 \}$ and $P \in \mathcal C(\vec R)$. If $\Phi^{\emptyset'}_e(e)\converge = 0$, $R_e$ is cofinite (proof of :ref{#prop-coh-no-low}), so $P(e) = 1$: otherwise $R^{P \uh (e + 1)} \subseteq \overline{R_e}$ would be finite. If $\Phi^{\emptyset'}_e(e)$ converges to $v \neq 0$, $R_e$ is finite, so $P(e) = 0 \neq v$. In both cases $P(e) \neq \Phi^{\emptyset'}_e(e)$: $P$ is DNC relative to $\emptyset'$. No $\Delta^0_2$ function is DNC relative to $\emptyset'$, so $\mathcal C(\vec R)$ has no $\Delta^0_2$ member, and $\vec R$ has no computable cohesive set (compare Hirschfeldt, *Slicing the Truth*, Exercise 6.33).
:::
::::

::::exercise{#ex-r-cohesive-immune difficulty=1 objective="Show that r-cohesive sets are immune while their complements are not."}
Let $C$ be r-cohesive. Show that $C$ has no infinite computable subset, and that $\overline{C}$ has one. Deduce that $C$ is not computable.

:::solution
Let $D \subseteq C$ be infinite and computable, with elements $d_0 < d_1 < \cdots$, and $D_0 = \{ d_{2j} : j \in \nat \}$, an infinite and coinfinite computable set. Since $C$ is r-cohesive, $C \subseteq^* D_0$ or $C \subseteq^* \overline{D_0}$. In the first case, $\{ d_{2j + 1} : j \in \nat \} \subseteq C \setminus D_0$ is finite; in the second, $D_0 = C \cap D_0$ is finite. Both are absurd.

Let $E$ be the set of even numbers. If $C \subseteq^* E$, then $\overline{C}$ contains all odd numbers except finitely many; otherwise $C \subseteq^* \overline{E}$, and $\overline{C}$ contains all even numbers except finitely many. In both cases, $\overline{C}$ has an infinite computable subset. If $C$ were computable, it would be an infinite computable subset of itself.
:::
::::
:::::
