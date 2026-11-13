---
title: Weakly low bases
summary: A set PA relative to ∅′ chooses a true statement among two Π⁰₂ statements one of which is true; between a set and a set PA relative to it there is room for another PA step; weakly low bases, where the jump of a solution is computed by any set PA relative to ∅′, give low₂ solutions and ω-models of low₂ sets.
duration: 40
prerequisites: [forcing-the-jump, pi01-classes/pa-degrees, pi01-classes/basis-theorems, reducibilities/preservation]
---

Cohesiveness does not admit a low basis (:ref{#prop-coh-no-low}), and the obstacle was located in :ref{to="lowness/forcing-the-jump"}: the jump of a Mathias generic set is decided by $\emptyset'$, but the choice of a reservoir, $X \cap R$ or $X \setminus R$, requires knowing which of two $\Pi^0_2$ statements is true. The choice does not require knowing **whether** each statement is true: it is enough to name one true statement among two, when one of them is known to be true. This is a task that a set PA relative to $\emptyset'$ performs, as a set PA relative to $\emptyset$ chooses between two $\Pi^0_1$ statements.

PA sets are weak in many respects: by the basis theorems, some are low, some are computably dominated, and some avoid any given non-computable set (:ref{#cor-pa-basis}). Relativized to $\emptyset'$, a set $P$ PA relative to $\emptyset'$ can be chosen with $P' \leq_T \emptyset''$: it is then barely more than $\emptyset'$. A construction that works with such a $P$ instead of $\emptyset'$ gives a solution whose jump is computed by $P$, which is close to being low. This lesson proves the two properties of PA sets that such constructions use, defines the resulting notion of a weakly low basis, and derives its consequences. The next lessons prove that cohesiveness, the pigeonhole principle for $\Delta^0_2$ sets and Ramsey's theorem for pairs admit weakly low bases.

## Choosing between true statements

A set $P$ is **PA relative to $X$** if it computes a $\{0, 1\}$-valued function $f$ with $f(e) \neq \Phi^X_e(e)$ whenever $\Phi^X_e(e)$ converges (:ref{#ex-pa-relative}). Such a $P$ computes $X$, and it computes a member of every non-empty $\Pi^0_1(X)$ class, by :ref{#thm-pa-characterization} relativized; it is then PA relative to every $W \leq_T X$, since $\Pi^0_1(W)$ classes are $\Pi^0_1(X)$ classes.

:::lemma{#lem-pa-choice}
Let $P$ be PA relative to $\emptyset'$, and fix a coding of $\Pi^0_2$ sentences by numbers. There is a $P$-computable function $g$ such that for all $\Pi^0_2$ sentences $\varphi$ and $\psi$, at least one of which is true, $g(\varphi, \psi) = 0$ implies that $\varphi$ is true, and $g(\varphi, \psi) = 1$ implies that $\psi$ is true.
:::

:::proof{of=lem-pa-choice}
By Post's theorem, the set of codes of false $\Pi^0_2$ sentences is $\Sigma^0_2$, that is, $\emptyset'$-c.e.; fix an enumeration of it with oracle $\emptyset'$, by stages. Let $A$ be the set of pairs $(\varphi, \psi)$ such that $\psi$ is enumerated at some stage $s$ and $\varphi$ at no stage $t \leq s$, and $B$ the set of pairs such that $\varphi$ is enumerated at some stage $s$ and $\psi$ at no stage $t < s$. Both are $\emptyset'$-c.e., and they are disjoint: a pair in both would have $\psi$ enumerated before $\varphi$ and $\varphi$ enumerated before $\psi$. By :ref{#thm-pa-characterization} relativized to $\emptyset'$, $P$ computes a set $C$ with $A \subseteq C$ and $C \cap B = \emptyset$. Let $g(\varphi, \psi) = 0$ if $(\varphi, \psi) \in C$ and $1$ otherwise.

Let $\varphi$ and $\psi$ be sentences, at least one true. If both are true, there is nothing to prove. If $\psi$ is false and $\varphi$ true, then $\psi$ is enumerated and $\varphi$ never is, so $(\varphi, \psi) \in A \subseteq C$ and $g(\varphi, \psi) = 0$. If $\varphi$ is false and $\psi$ true, then $(\varphi, \psi) \in B$, so $(\varphi, \psi) \notin C$ and $g(\varphi, \psi) = 1$.
:::

The function $g$ does not decide the truth of the sentences: when both are true, it may answer either way, and it gives no information on a pair of false sentences. This is the behavior of a $\{0, 1\}$-valued DNC function, one jump up. The first exercise shows that the lemma characterizes the sets PA relative to $\emptyset'$.

:::example{#ex-pa-choice-infinite}
Let $X$ be an infinite computable set and $R$ a computable set, given by $\Delta^0_1$ indices. The sentences "$X \cap R$ is infinite" and "$X \setminus R$ is infinite" are $\Pi^0_2$, with codes computable from the indices, and at least one is true. A set $P$ PA relative to $\emptyset'$ names, uniformly in the indices, one of the two sets that is infinite. By contrast, deciding which of them are infinite requires $\emptyset''$ in general.
:::

The following lemma is a form of the density of PA degrees: between a set and a set PA relative to it, there is room for another PA step.

:::lemma[Simpson]{#lem-pa-between}
Let $P$ be PA relative to $X$. There is a set $Q$ with $X \leq_T Q \leq_T P$ such that $Q$ is PA relative to $X$ and $P$ is PA relative to $Q$.
:::

:::proof{of=lem-pa-between}
For a set $W$, let $D^W$ be the class of $\{0, 1\}$-valued functions DNC relative to $W$, a non-empty $\Pi^0_1(W)$ class, uniformly in $W$. The class of sets $Q_0 \oplus R$ with $Q_0 \in D^X$ and $R \in D^{X \oplus Q_0}$ is a non-empty $\Pi^0_1(X)$ class. Since $P$ is PA relative to $X$, it computes a member $Q_0 \oplus R$, and it computes $X$. Let $Q = X \oplus Q_0$. Then $X \leq_T Q \leq_T P$; $Q$ computes $Q_0 \in D^X$, so it is PA relative to $X$; and $P$ computes $R \in D^Q$, so it is PA relative to $Q$.
:::

:::quiz[choosing with a PA set]
In the proof of :ref{#lem-pa-choice}, what would go wrong if $A$ were defined as the set of pairs whose second sentence is false, and $B$ as the set of pairs whose first sentence is false?

- [x] The two sets would not be disjoint, since both sentences of a pair may be false, and a separating set would not exist in general.
- [ ] The sets would not be $\emptyset'$-c.e.

  They would be; disjointness is what fails.
- [ ] The function $g$ would not be total.

  A separating set gives a total function whenever it exists.

---

In the proof of :ref{#lem-pa-between}, why is $R$ required to be DNC relative to $X \oplus Q_0$, rather than relative to $X$?

- [x] So that $P$, which computes $R$, is PA relative to $Q = X \oplus Q_0$; a second function DNC relative to $X$ would only show again that $P$ is PA relative to $X$.
- [ ] So that the class of pairs is $\Pi^0_1(X)$.

  It would be $\Pi^0_1(X)$ in both cases; the condition on $R$ refers to $Q_0$, which is part of the member.
- [ ] So that $Q$ computes $R$.

  $Q$ does not compute $R$, and could not: no set computes a function DNC relative to itself.
:::

## Weakly low bases

:::definition{#def-weakly-low-basis}
A problem $\mathsf P$ **admits a weakly low basis** if for every set $Z$, every set $P$ PA relative to $Z'$ and every $Z$-computable instance $X$ of $\mathsf P$, there is a solution $Y$ to $X$ with $(Z \oplus Y)' \leq_T P$.
:::

:::example{#ex-weakly-low-problems}
1. $\mathsf{WKL}$ and $\mathsf{RT}^1_2$ admit weakly low bases, since they admit low bases (:ref{#ex-low-basis-problems}).
2. The jump $\mathsf J$ does not. By the low basis theorem relativized to $\emptyset'$, there is $P$ PA relative to $\emptyset'$ with $P' \leq_T \emptyset''$. The only solution to the instance $\emptyset$ is $\emptyset'$, and $\emptyset'' \leq_T P$ would give $\emptyset''' \leq_T P' \leq_T \emptyset''$, which is impossible.
3. $\mathsf{COH}$, $\mathsf D^2_2$ and $\mathsf{RT}^2_2$ admit weakly low bases, by the theorems of the next lessons, but no low bases.
:::

A low basis is a weakly low basis, since $P$ computes $Z'$. The definition does not obviously give a property that can be iterated, since the oracle $P$ is PA relative to $Z'$, while after adding $Y$ one would need an oracle PA relative to $(Z \oplus Y)'$. The following proposition shows that this is automatic, and lists the consequences that make weakly low bases useful.

:::proposition{#prop-weakly-low-properties}
Let $\mathsf P$ admit a weakly low basis, let $Z$ be a set and $X$ a $Z$-computable instance.
1. For every $P$ PA relative to $Z'$, $X$ has a solution $Y$ such that $P$ is PA relative to $(Z \oplus Y)'$.
2. $X$ has a solution $Y$ with $(Z \oplus Y)'' \leq_T Z''$.
3. For every set $C \not\leq_T Z'$, $X$ has a solution $Y$ with $C \not\leq_T (Z \oplus Y)'$.
:::

:::proof{of=prop-weakly-low-properties}
1. By :ref{#lem-pa-between} applied to $Z'$ and $P$, there is $Q$ PA relative to $Z'$ such that $P$ is PA relative to $Q$. By the weakly low basis, applied with $Q$, $X$ has a solution $Y$ with $(Z \oplus Y)' \leq_T Q$. Then $P$ is PA relative to $(Z \oplus Y)'$, which is computable in $Q$.
2. By the low basis theorem relativized to $Z'$, applied to the non-empty $\Pi^0_1(Z')$ class of $\{0, 1\}$-valued functions DNC relative to $Z'$, there is $P$ PA relative to $Z'$ with $P' \leq_T Z''$. A solution $Y$ with $(Z \oplus Y)' \leq_T P$ satisfies $(Z \oplus Y)'' \leq_T P' \leq_T Z''$.
3. By the cone avoidance basis theorem relativized to $Z'$, there is $P$ PA relative to $Z'$ with $C \not\leq_T P$. A solution with $(Z \oplus Y)' \leq_T P$ works.
:::

Item 2 is the reason for the name: a problem with a weakly low basis has **low₂ solutions** relative to its instances. Item 3 is a form of cone avoidance for the jump of the solution, a property studied in the later course on jump cone avoidance.

:::theorem{#thm-weakly-low-model}
Let $\mathsf P$ admit a weakly low basis, and let $P$ be PA relative to $\emptyset'$. There is a Turing ideal satisfying $\mathsf P$ such that $P$ is PA relative to $Y'$ for every member $Y$. If $P' \leq_T \emptyset''$, every member of this ideal is low₂.
:::

:::proof{of=thm-weakly-low-model}
Let $\mathcal W$ be the class of sets $Y$ such that $P$ is PA relative to $Y'$. It is closed downward: if $W \leq_T Y$, then $W' \leq_T Y'$, and $P$ is PA relative to $W'$. It contains $\emptyset$. By item 1 of :ref{#prop-weakly-low-properties}, $\mathsf P$ preserves $\mathcal W$: for $Z \in \mathcal W$ and a $Z$-computable instance, some solution $Y$ has $Z \oplus Y \in \mathcal W$. By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf P$. If $Y \in \mathcal I$, then $Y' \leq_T P$, so $Y'' \leq_T P' \leq_T \emptyset''$.
:::

In particular, if $\mathsf P$ is a $\Pi^1_2$ statement with a weakly low basis, $\mathsf{RCA}_0 + \mathsf P$ does not prove $\mathsf{ACA}_0$: a low₂ set does not compute $\emptyset'$, since otherwise $\emptyset''' \leq_T \emptyset''$.

:::quiz[weakly low bases]
In item 1 of :ref{#prop-weakly-low-properties}, why is the weakly low basis applied with $Q$ rather than with $P$?

- [x] Because $(Z \oplus Y)' \leq_T P$ does not make $P$ PA relative to $(Z \oplus Y)'$: the two could even be Turing equivalent, and no set is PA relative to itself. With $(Z \oplus Y)' \leq_T Q$, the set $P$ is PA relative to $Q$, hence relative to every set computable in $Q$.
- [ ] Because $P$ is not PA relative to $Z'$.

  It is, by hypothesis.
- [ ] Because $Q$ is low relative to $Z'$.

  Nothing is assumed about the jump of $Q$.
:::

## Exercises

::::exercise{difficulty=2}
Let $P$ be a set that computes a function $g$ with the property of :ref{#lem-pa-choice}. Show that $P$ is PA relative to $\emptyset'$.

:::solution
Let $A$ and $B$ be disjoint $\emptyset'$-c.e. sets. For each $n$, the sentences $\varphi_n$: "$n \notin A$" and $\psi_n$: "$n \notin B$" are $\Pi^0_2$ by Post's theorem, with codes computable from $n$, and at least one is true since $A \cap B = \emptyset$. Let $C = \{ n : g(\varphi_n, \psi_n) = 1 \}$, computable in $P$. If $n \in A$, then $\varphi_n$ is false, so $g(\varphi_n, \psi_n) = 1$ and $n \in C$. If $n \in B$, then $\psi_n$ is false, so $g(\varphi_n, \psi_n) = 0$ and $n \notin C$. So $P$ computes a separating set for every pair of disjoint $\emptyset'$-c.e. sets, and is PA relative to $\emptyset'$ by :ref{#thm-pa-characterization} relativized.
:::
::::

::::exercise{difficulty=1}
Let $\mathsf P$ and $\mathsf Q$ admit weakly low bases. Show that the problem whose instances are pairs $X_0 \oplus X_1$ of an instance of $\mathsf P$ and an instance of $\mathsf Q$, with solutions $Y_0 \oplus Y_1$, admits a weakly low basis.

:::solution
Let $Z$ compute $X_0 \oplus X_1$ and $P$ be PA relative to $Z'$. By item 1 of :ref{#prop-weakly-low-properties}, $X_0$ has a solution $Y_0$ such that $P$ is PA relative to $(Z \oplus Y_0)'$. Apply the weakly low basis of $\mathsf Q$ relative to $Z \oplus Y_0$, which computes $X_1$, with the same $P$: $X_1$ has a solution $Y_1$ with $(Z \oplus Y_0 \oplus Y_1)' \leq_T P$. Then $(Z \oplus (Y_0 \oplus Y_1))' \leq_T P$.
:::
::::

## Notes and references

The notion of a weakly low basis, the invariance of :ref{#prop-weakly-low-properties} and its consequences follow the section *Beyond ∅′* of the chapter *Lowness* of Patey's monograph. :ref{#lem-pa-between} is the density of PA degrees, due to Simpson (Hirschfeldt, Theorem 4.26; Dzhafarov and Mummert, Proposition 2.8.26). The choice of a true statement by a PA set is Theorem 2.8.25 (4) of Dzhafarov and Mummert, relativized, and is explained by Hirschfeldt in the discussion before Theorem 6.44. Hirschfeldt builds ω-models from basis theorems in Proposition 4.27, the method of :ref{#thm-weakly-low-model}.

- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 4.5 and 6.5.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 2.8.
- S. G. Simpson, *Degrees of unsolvability: a survey of results*, in *Handbook of Mathematical Logic*, North-Holland, 1977, 631–652.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, section *Beyond ∅′*.
