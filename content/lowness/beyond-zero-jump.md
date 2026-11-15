---
title: Weakly low cohesive sets
summary: For every computable sequence of sets and every set P PA relative to ∅′, there is a cohesive set whose jump is computed by P (Jockusch–Stephan), by a forcing argument in which P is used only to choose the reservoirs; so cohesiveness admits a weakly low basis, but no low basis.
duration: 20
prerequisites: [weakly-low-bases, ramsey-theorem/cohesiveness]
---

The previous lesson reduced the construction of a cohesive set with a jump computed by $P$ to two facts: the jump of a Mathias generic set is decided by $\emptyset'$ (:ref{#prop-jump-decision-examples}), and the side of each set $R_i$ can be chosen by $P$ (:ref{#ex-pa-choice-infinite}). This lesson writes out the construction. It is short, but it is the model for the next lesson, where the reservoirs are no longer computable and the forcing question is disjunctive; the structure of the proof, a $P$-computable sequence of codes in which $P$ is used only to choose among $\Pi^0_2$ statements, is the same.

## Cohesiveness

The following theorem is the case of cohesiveness. It was proved by Jockusch and Stephan in the form of :ref{#cor-coh-bounds}, through the class of decisions of a sequence and Friedberg's jump inversion. The proof given here is a direct forcing argument, due to Cholak, Jockusch and Slaman.

:::theorem[Jockusch, Stephan]{#thm-coh-weakly-low}
Let $Z$ be a set, $\vec R = (R_i)$ a $Z$-computable sequence of sets, and $P$ PA relative to $Z'$. There is an $\vec R$-cohesive set $G$ with $(Z \oplus G)' \leq_T P$. So $\mathsf{COH}$ admits a weakly low basis.
:::

:::proof{of=thm-coh-weakly-low}
We write the proof for $Z = \emptyset$; it relativizes, with reservoirs computable in $Z$ and functionals with oracle $Z \oplus G$. Use computable Mathias forcing, with conditions $(\sigma, X)$ coded by $\langle \sigma, b \rangle$ with $b$ a $\Delta^0_1$ index of $X$, as in :ref{#def-coded-forcing}. We apply :ref{#thm-jump-control} with the oracle $P$.

*The jump.* Computable Mathias forcing decides the jump $\emptyset'$-effectively (:ref{#prop-jump-decision-examples}), hence $P$-effectively, since $P$ computes $\emptyset'$.

*Prefixes and infinity.* The sets $S_n$, and the sets of conditions whose stem has at least $n$ elements, are uniformly computably dense (:ref{#prop-jump-decision-examples} and the remark after it).

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

::::exercise{#ex-r-cohesive-weakly-low difficulty=2 objective="Relativize the weakly low basis of cohesiveness to a low PA set, to build an r-cohesive set with a jump computed by a given set PA relative to $\emptyset'$."}
A set is **r-cohesive** if it is cohesive for the sequence of all computable sets. Let $P$ be PA relative to $\emptyset'$. Show that there is an r-cohesive set $G$ with $G' \leq_T P$. (Use a low PA set $Y$, and show that it computes a sequence of sets containing every computable set.)

:::solution
Let $Y$ be low and PA (:ref{#cor-pa-basis}). For each $e$, the partial computable function $\Phi_e$, restricted to the inputs where it converges with value in $\{0, 1\}$, has a total $Y$-computable extension $R_e$, uniformly in $e$: the class of total extensions is a non-empty $\Pi^0_1$ class, uniformly in $e$, and the proof of :ref{#thm-pa-characterization} is uniform. If $\Phi_e$ is the characteristic function of a set, $R_e$ is this set. So $(R_e)$ is a $Y$-computable sequence containing every computable set. Since $Y$ is low, $Y' \leq_T \emptyset'$, and $P$ is PA relative to $Y'$. By :ref{#thm-coh-weakly-low} relativized to $Y$, there is an $(R_e)$-cohesive set $G$ with $(Y \oplus G)' \leq_T P$. It is r-cohesive, and $G' \leq_T P$.
:::
::::

## Notes and references

:ref{#thm-coh-weakly-low} is due to Jockusch and Stephan (1993). The forcing proof given here is that of Cholak, Jockusch and Slaman (2001), presented by Hirschfeldt as the proof of Theorem 6.44 and by Dzhafarov and Mummert as Theorem 7.5.15 and Lemma 8.5.11; the presentation follows the sections *Beyond ∅′* and *Ramsey's theorem for pairs* of the chapter *Lowness* of Patey's monograph, which notes that the forcing proof is close to the original one, with $P$ in place of a $\Delta^0_2$ approximation of $P$. :ref{#ex-r-cohesive-weakly-low} is the remark after Theorem 6.44 of Hirschfeldt.

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 6.5.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 7.5 and 8.5.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, sections *Beyond ∅′* and *Ramsey's theorem for pairs*.

:::::exercises
::::exercise{#ex-coh-construction-decisions difficulty=1 objective="Relate the choices of reservoirs in the forcing proof to the class of decisions of the sequence." lessons="ramsey-theorem/cohesiveness"}
In the proof of :ref{#thm-coh-weakly-low}, let $d(i) = 1$ if the reservoir chosen at the step for $E_i$ is $X \cap R_i$, and $d(i) = 0$ otherwise. Show that $d$ is computable in $P$, that it belongs to the class $\mathcal C(\vec R)$ of acceptable decisions of :ref{to="ramsey-theorem/cohesiveness"}, and that $G \subseteq^* R_i$ if and only if $d(i) = 1$.

:::solution
The sequence of codes is $P$-computable, and so is the record of the choices made at the steps for the sets $E_i$; so $d \leq_T P$. Let $n \in \nat$, and let $(\sigma, X)$ be a condition of the sequence built after the steps for $E_0, \dots, E_{n-1}$. Its reservoir is contained in the reservoir chosen at each of these steps, hence in $R_i$ if $d(i) = 1$ and in $\overline{R_i}$ if $d(i) = 0$, for every $i < n$: so $X \subseteq R^{d \uh n}$, and $R^{d \uh n}$ is infinite. So $d \in \mathcal C(\vec R)$. Finally, $G \setminus \sigma \subseteq X$ for the condition $(\sigma, X)$ reached after the step for $E_i$, so $G \subseteq^* R_i$ if $d(i) = 1$ and $G \subseteq^* \overline{R_i}$ if $d(i) = 0$; since $G$ is infinite, not both hold. The forcing proof thus also produces a $P$-computable member of the $\Pi^0_1(\emptyset')$ class of decisions, but chooses it step by step, interleaved with the decisions of the jump.
:::
::::

::::exercise{#ex-coh-jumps-below-pa difficulty=2 objective="Combine the weakly low basis of cohesiveness with the density of PA degrees, below every set PA relative to $\emptyset'$."}
Let $\vec R$ be the computable sequence of :ref{#prop-coh-no-low}, and $P$ a set PA relative to $\emptyset'$. Show that there is an $\vec R$-cohesive set $G$ such that $G'$ is PA relative to $\emptyset'$ and $G' <_T P$.

:::solution
By :ref{#lem-pa-between} applied to $\emptyset'$ and $P$, there is $Q$ PA relative to $\emptyset'$ with $Q \leq_T P$ such that $P$ is PA relative to $Q$. By :ref{#thm-coh-weakly-low} with the oracle $Q$, there is an $\vec R$-cohesive set $G$ with $G' \leq_T Q \leq_T P$. By :ref{#prop-coh-no-low}, $G'$ is PA relative to $\emptyset'$. The set $P$ is PA relative to $Q$, hence relative to $G' \leq_T Q$, so it computes a $\{0, 1\}$-valued function DNC relative to $G'$; such a function is not computable in $G'$. So $P \not\leq_T G'$, and $G' <_T P$. In particular, no set PA relative to $\emptyset'$ is of least degree among the jumps of $\vec R$-cohesive sets below it.
:::
::::

::::exercise{#ex-coh-low-decidable-atoms difficulty=2 objective="Locate the use of the PA oracle by showing that cohesive sets can be made low when $\emptyset'$ decides which Boolean combinations of the sequence are infinite."}
Let $\vec R$ be a computable sequence such that the set of strings $\sigma$ for which $R^\sigma$ is infinite is computable in $\emptyset'$ (notation of :ref{to="ramsey-theorem/cohesiveness"}). Show that $\vec R$ has a low cohesive set. Deduce that for the sequence of :ref{#prop-coh-no-low}, this set of strings is not computable in $\emptyset'$.

:::solution
Restrict computable Mathias forcing to the conditions $(\tau, X)$ with $X = R^\sigma \setminus \{ 0, \dots, m \}$ infinite, for some string $\sigma$ and some $m \geq |\tau|$, coded by $\langle \tau, \sigma, m \rangle$; a $\Delta^0_1$ index of $X$ is computable from the code. The extension relation and the members are those of Mathias forcing. In the proof of :ref{#prop-jump-decision-examples}, the decision of the jump and the sets $S_n$ replace a reservoir $X$ by $X \setminus \{ 0, \dots, k \}$, which keeps this form; so this notion decides the jump $\emptyset'$-effectively, and the sets $S_n$ and the sets of conditions with at least $n$ elements in the stem are uniformly computably dense. For each $i$, let $E_i$ be the set of conditions with a code $\langle \tau, \sigma, m \rangle$ such that $|\sigma| > i$. Given a code with $|\sigma| \leq i$, extend $\sigma$ one bit at a time: since $R^\rho = R^{\rho 0} \cup R^{\rho 1}$, if $R^\rho$ is infinite, one of $R^{\rho 0}$ and $R^{\rho 1}$ is, and $\emptyset'$ tells which by hypothesis. This gives $\sigma' \succeq \sigma$ of length $i + 1$ with $R^{\sigma'}$ infinite, and $\langle \tau, \sigma', m \rangle$ is a code of an extension, since $R^{\sigma'} \subseteq R^\sigma$. So the sets $E_i$ are uniformly $\emptyset'$-effectively dense. By :ref{#thm-jump-control}, there is a set $G$ with $G' \leq_T \emptyset'$, infinite, a member of a condition $(\tau, R^\sigma \setminus \{ 0, \dots, m \})$ with $|\sigma| > i$ for each $i$; then $G \setminus \tau \subseteq R^\sigma$, which is contained in $R_i$ or in $\overline{R_i}$. So $G$ is a low cohesive set. Since the sequence of :ref{#prop-coh-no-low} has no low cohesive set, its set of strings $\sigma$ with $R^\sigma$ infinite is not computable in $\emptyset'$.
:::
::::
:::::
