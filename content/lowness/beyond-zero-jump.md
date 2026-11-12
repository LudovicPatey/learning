---
title: Beyond the halting set
summary: A set PA relative to ∅′ chooses a true statement among two Π⁰₂ statements one of which is true; weakly low bases, where the jump of a solution is computed by any set PA relative to ∅′; they give low₂ solutions and ω-models of low₂ sets; cohesiveness admits a weakly low basis (Jockusch–Stephan) but no low basis.
duration: 45
prerequisites: [coded-ideals, ramsey-theorem/cohesiveness, pi01-classes/basis-theorems]
---

Cohesiveness does not admit a low basis (:ref{#prop-coh-no-low}), and the obstacle was located in the second lesson: the jump of a Mathias generic set is decided by $\emptyset'$, but the choice of a reservoir, $X \cap R$ or $X \setminus R$, requires knowing which of two $\Pi^0_2$ statements is true. The choice does not require knowing **whether** each statement is true: it is enough to name one true statement among two, when one of them is known to be true. This is a task that a set PA relative to $\emptyset'$ performs, as a set PA relative to $\emptyset$ chooses between two $\Pi^0_1$ statements.

PA sets are weak in many respects: by the basis theorems, some are low, some are computably dominated, and some avoid any given non-computable set (:ref{#cor-pa-basis}). Relativized to $\emptyset'$, a set $P$ PA relative to $\emptyset'$ can be chosen with $P' \leq_T \emptyset''$: it is then barely more than $\emptyset'$. A construction that works with such a $P$ instead of $\emptyset'$ gives a solution whose jump is computed by $P$, which is close to being low. This lesson sets up the notion and proves it for cohesiveness; the next two lessons prove it for Ramsey's theorem for pairs.

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

In :ref{#lem-pa-between}, why is $Q$ defined as $X \oplus Q_0$ rather than as $Q_0$?

- [x] Because a function DNC relative to $X$ need not compute $X$, and the lemma requires $X \leq_T Q$; with the join, $R \in D^Q$ is DNC relative to a set computing $X$.
- [ ] Because $Q_0$ is not PA relative to $X$.

  It is, since it is a member of $D^X$.
- [ ] Because $P$ does not compute $Q_0$.

  It does, as part of the member $Q_0 \oplus R$.
:::

## Weakly low bases

:::definition{#def-weakly-low-basis}
A problem $\mathsf P$ **admits a weakly low basis** if for every set $Z$, every set $P$ PA relative to $Z'$ and every $Z$-computable instance $X$ of $\mathsf P$, there is a solution $Y$ to $X$ with $(Y \oplus Z)' \leq_T P$.
:::

A low basis is a weakly low basis, since $P$ computes $Z'$. The definition does not obviously give a property that can be iterated, since the oracle $P$ is PA relative to $Z'$, while after adding $Y$ one would need an oracle PA relative to $(Y \oplus Z)'$. The following proposition shows that this is automatic, and lists the consequences that make weakly low bases useful.

:::proposition{#prop-weakly-low-properties}
Let $\mathsf P$ admit a weakly low basis, let $Z$ be a set and $X$ a $Z$-computable instance.
1. For every $P$ PA relative to $Z'$, $X$ has a solution $Y$ such that $P$ is PA relative to $(Y \oplus Z)'$.
2. $X$ has a solution $Y$ with $(Y \oplus Z)'' \leq_T Z''$.
3. For every set $C \not\leq_T Z'$, $X$ has a solution $Y$ with $C \not\leq_T (Y \oplus Z)'$.
:::

:::proof{of=prop-weakly-low-properties}
1. By :ref{#lem-pa-between} applied to $Z'$ and $P$, there is $Q$ PA relative to $Z'$ such that $P$ is PA relative to $Q$. By the weakly low basis, applied with $Q$, $X$ has a solution $Y$ with $(Y \oplus Z)' \leq_T Q$. Then $P$ is PA relative to $(Y \oplus Z)'$, which is computable in $Q$.
2. By the low basis theorem relativized to $Z'$, applied to the non-empty $\Pi^0_1(Z')$ class of $\{0, 1\}$-valued functions DNC relative to $Z'$, there is $P$ PA relative to $Z'$ with $P' \leq_T Z''$. A solution $Y$ with $(Y \oplus Z)' \leq_T P$ satisfies $(Y \oplus Z)'' \leq_T P' \leq_T Z''$.
3. By the cone avoidance basis theorem relativized to $Z'$, there is $P$ PA relative to $Z'$ with $C \not\leq_T P$. A solution with $(Y \oplus Z)' \leq_T P$ works.
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

- [x] Because a solution with jump computable in $P$ gives no PA set relative to its jump below $P$; computing the jump in $Q$, relative to which $P$ is PA, leaves $P$ PA relative to the jump.
- [ ] Because $P$ is not PA relative to $Z'$.

  It is, by hypothesis.
- [ ] Because $Q$ is low relative to $Z'$.

  Nothing is assumed about the jump of $Q$.
:::

## Cohesiveness

The following theorem is the case of cohesiveness. It was proved by Jockusch and Stephan in the form of :ref{#cor-coh-bounds}, through the class of decisions of a sequence and Friedberg's jump inversion. The proof given here is a direct forcing argument, due to Cholak, Jockusch and Slaman, and it is the model for the next lesson.

:::theorem[Jockusch, Stephan]{#thm-coh-weakly-low}
Let $Z$ be a set, $\vec R = (R_i)$ a $Z$-computable sequence of sets, and $P$ PA relative to $Z'$. There is an $\vec R$-cohesive set $G$ with $(G \oplus Z)' \leq_T P$. So $\mathsf{COH}$ admits a weakly low basis.
:::

:::proof{of=thm-coh-weakly-low}
We write the proof for $Z = \emptyset$; it relativizes, with reservoirs computable in $Z$ and functionals with oracle $G \oplus Z$. Use computable Mathias forcing, with conditions $(\sigma, X)$ coded by $\langle \sigma, b \rangle$ with $b$ a $\Delta^0_1$ index of $X$, as in :ref{#def-coded-forcing}. We apply :ref{#thm-jump-control} with the oracle $P$.

*The jump.* Computable Mathias forcing decides the jump $\emptyset'$-effectively (:ref{#prop-jump-decision-examples}), hence $P$-effectively, since $P$ computes $\emptyset'$.

*Prefixes and infinity.* The sets $S_n$, and the sets of conditions whose string has at least $n$ elements, are uniformly computably dense (:ref{#prop-jump-decision-examples}).

*Cohesiveness.* For each $i$, let $E_i$ be the set of conditions $(\sigma, X)$ with $X \subseteq R_i$ or $X \subseteq \overline{R_i}$. Given a code $\langle \sigma, b \rangle$ and $i$, compute codes of the $\Pi^0_2$ sentences $\varphi$: "$X \cap R_i$ is infinite" and $\psi$: "$X \setminus R_i$ is infinite". Since $X$ is infinite, at least one is true. Let $g$ be the $P$-computable function of :ref{#lem-pa-choice}. If $g(\varphi, \psi) = 0$, return a code of $(\sigma, X \cap R_i)$; otherwise a code of $(\sigma, X \setminus R_i)$. The returned reservoir is infinite, computable, with a $\Delta^0_1$ index computable from $b$ and $i$, so the result is a code of an extension of $(\sigma, X)$ in $E_i$. The sets $E_i$ are uniformly $P$-effectively dense.

By :ref{#thm-jump-control}, there is a set $G$, a member of every condition of a filter meeting all these sets, with $G' \leq_T P$. It is infinite. For each $i$, some condition $(\sigma, X)$ of the filter lies in $E_i$, and $G \setminus \sigma \subseteq X$, so $G \subseteq^* R_i$ or $G \subseteq^* \overline{R_i}$.
:::

:::corollary{#cor-coh-weakly-not-low}
$\mathsf{COH}$ admits a weakly low basis, but not a low basis. There is an ω-model of $\mathsf{RCA}_0 + \mathsf{COH}$ consisting of low₂ sets.
:::

:::proof{of=cor-coh-weakly-not-low}
The first statement is :ref{#thm-coh-weakly-low} and :ref{#prop-coh-no-low}. The second is :ref{#thm-weakly-low-model}, with $P$ PA relative to $\emptyset'$ and $P' \leq_T \emptyset''$, which exists by the low basis theorem relativized to $\emptyset'$.
:::

The theorem is optimal for cohesiveness. By :ref{#prop-coh-no-low}, there is a computable sequence all of whose cohesive sets have a jump PA relative to $\emptyset'$. For such a sequence, the jump of a cohesive set is itself a set PA relative to $\emptyset'$: the oracle used in the construction cannot be replaced by anything weaker in this sense. Comparing the two proofs: the proof of :ref{#cor-coh-bounds} decides the sides of the sets $R_i$ all at once, as a member of a $\Pi^0_1(\emptyset')$ class, and then builds the cohesive set from an approximation; the forcing proof interleaves the choices of sides with the decisions of the jump, and uses the PA set only for the choices.

:::quiz[cohesiveness]
In the proof of :ref{#thm-coh-weakly-low}, which steps need the oracle $P$ rather than $\emptyset'$?

- [x] Only the cohesiveness steps, where one of $X \cap R_i$ and $X \setminus R_i$ must be named as infinite.
- [ ] The decisions of the jump.

  They are $\emptyset'$-effective, by :ref{#prop-jump-decision-examples}.
- [ ] The infinity steps.

  They are computable: a search through the reservoir finds new elements.

---

Why does the proof not need to know which of $X \cap R_i$ and $X \setminus R_i$ are infinite?

- [x] Because a condition needs an infinite reservoir, and one infinite side is enough; the other side may be infinite too, and its fate does not matter.
- [ ] Because both sides are always infinite.

  If $X \subseteq^* R_i$, the side $X \setminus R_i$ is finite.
- [ ] Because $P$ decides both.

  $P$ does not decide $\Pi^0_2$ sentences in general; it only chooses a true one among two.
:::

## Exercises

::::exercise{difficulty=2}
Let $P$ be a set that computes a function $g$ with the property of :ref{#lem-pa-choice}. Show that $P$ is PA relative to $\emptyset'$.

:::solution
Let $A$ and $B$ be disjoint $\emptyset'$-c.e. sets. For each $n$, the sentences $\varphi_n$: "$n \notin A$" and $\psi_n$: "$n \notin B$" are $\Pi^0_2$ by Post's theorem, with codes computable from $n$, and at least one is true since $A \cap B = \emptyset$. Let $C = \{ n : g(\varphi_n, \psi_n) = 1 \}$, computable in $P$. If $n \in A$, then $\varphi_n$ is false, so $g(\varphi_n, \psi_n) = 1$ and $n \in C$. If $n \in B$, then $\psi_n$ is false, so $g(\varphi_n, \psi_n) = 0$ and $n \notin C$. So $P$ computes a separating set for every pair of disjoint $\emptyset'$-c.e. sets, and is PA relative to $\emptyset'$ by :ref{#thm-pa-characterization} relativized.
:::
::::

::::exercise{difficulty=2}
A set is **r-cohesive** if it is cohesive for the sequence of all computable sets. Let $P$ be PA relative to $\emptyset'$. Show that there is an r-cohesive set $G$ with $G' \leq_T P$. (Use a low PA set $Y$, and show that it computes a sequence of sets containing every computable set.)

:::solution
Let $Y$ be low and PA (:ref{#cor-pa-basis}). For each $e$, the partial computable function $\Phi_e$, restricted to the inputs where it converges with value in $\{0, 1\}$, has a total $Y$-computable extension $R_e$, uniformly in $e$: the class of total extensions is a non-empty $\Pi^0_1$ class, uniformly in $e$, and the proof of :ref{#thm-pa-characterization} is uniform. If $\Phi_e$ is the characteristic function of a set, $R_e$ is this set. So $(R_e)$ is a $Y$-computable sequence containing every computable set. Since $Y$ is low, $Y' \leq_T \emptyset'$, and $P$ is PA relative to $Y'$. By :ref{#thm-coh-weakly-low} relativized to $Y$, there is an $(R_e)$-cohesive set $G$ with $(G \oplus Y)' \leq_T P$. It is r-cohesive, and $G' \leq_T P$.
:::
::::

::::exercise{difficulty=1}
Let $\mathsf P$ and $\mathsf Q$ admit weakly low bases. Show that the problem whose instances are pairs $X_0 \oplus X_1$ of an instance of $\mathsf P$ and an instance of $\mathsf Q$, with solutions $Y_0 \oplus Y_1$, admits a weakly low basis.

:::solution
Let $Z$ compute $X_0 \oplus X_1$ and $P$ be PA relative to $Z'$. By item 1 of :ref{#prop-weakly-low-properties}, $X_0$ has a solution $Y_0$ such that $P$ is PA relative to $(Y_0 \oplus Z)'$. Apply the weakly low basis of $\mathsf Q$ relative to $Y_0 \oplus Z$, which computes $X_1$, with the same $P$: $X_1$ has a solution $Y_1$ with $(Y_1 \oplus Y_0 \oplus Z)' \leq_T P$. Then $((Y_0 \oplus Y_1) \oplus Z)' \leq_T P$.
:::
::::

## Notes and references

The notion of a weakly low basis, the invariance of :ref{#prop-weakly-low-properties} and its consequences follow the section *Beyond ∅′* of the chapter *Lowness* of Patey's monograph. :ref{#lem-pa-between} is the density of PA degrees, due to Simpson (Hirschfeldt, Theorem 4.26; Dzhafarov and Mummert, Proposition 2.8.26); the choice of a true statement by a PA set is Theorem 2.8.25 (4) of Dzhafarov and Mummert, relativized, and the discussion before Theorem 6.44 of Hirschfeldt. :ref{#thm-coh-weakly-low} is due to Jockusch and Stephan (1993); the forcing proof given here is that of Cholak, Jockusch and Slaman (2001), presented by Hirschfeldt as the proof of Theorem 6.44 and by Dzhafarov and Mummert as Lemma 8.5.11 and Theorem 7.5.15. The second exercise is the remark after Theorem 6.44 of Hirschfeldt.

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 4.5 and 6.5.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 2.8, 7.5 and 8.5.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, sections *Beyond ∅′* and *Ramsey's theorem for pairs*.
