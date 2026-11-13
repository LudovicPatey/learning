---
title: First consequences of PA avoidance
summary: The table of examples; cohesiveness admits PA avoidance; every set is Δ⁰₂ relative to a set that is not PA, so that strong PA avoidance reduces to Δ⁰₂ instances; PA avoidance implies cone avoidance, by the Posner–Robinson theorem.
duration: 30
prerequisites: [pa-avoidance, cohen-genericity/posner-robinson]
---

The previous lesson defined PA avoidance and proved that a merging forcing question whose answers are $\Sigma^0_1$ relative to the condition produces generic sets that are not PA relative to $D$ (:ref{#thm-local-pa-avoidance}). This lesson applies the theorem to the notions of forcing of the course on cone avoidance. The first examples are those of the table of cone avoidance; computable Mathias forcing gives the PA avoidance of cohesiveness; the forcing that makes an arbitrary set $\Delta^0_2$ reduces strong PA avoidance to $\Delta^0_2$ instances. The last section shows, with the Posner–Robinson theorem, that PA avoidance is a strengthening of cone avoidance; this is where the parameter $D$ of :ref{#def-pa-avoidance} is needed.

## First examples

:::example{#ex-pa-avoidance-problems}
The following table collects the problems of :ref{#ex-cone-avoidance-problems}, with the results of this course.

| problem | PA avoidance | strong PA avoidance |
| --- | --- | --- |
| $\mathsf{RT}^1_2$ | yes (trivial) | yes, Liu (:ref{#thm-rt12-strong-pa}) |
| $\mathsf{WKL}$ | no | no |
| $\mathsf{COH}$ | yes (:ref{#thm-coh-pa-avoidance}) | yes (:ref{to="compactness-avoidance/liu-theorem"}, exercise) |
| $\mathsf{RT}^2_2$ | yes, Liu (:ref{#thm-liu-rt22}) | no |
| $\mathsf{RT}^3_2$ | no | no |
| $\mathsf J$ | no | no |

1. **$\mathsf{RT}^1_2$ and $\mathsf{WKL}$.** See the remarks after :ref{#def-pa-avoidance}. Strong PA avoidance fails for $\mathsf{WKL}$ already with $D = Z = \emptyset$.
2. **$\mathsf{RT}^2_2$, $\mathsf{RT}^3_2$, $\mathsf J$.** Each has an instance all of whose solutions compute $\emptyset'$, which is PA: for $\mathsf{RT}^2_2$ an instance computable in $\emptyset'$, for the other two computable instances (:ref{#ex-cone-avoidance-problems}).
:::

Cone avoidance and PA avoidance differ only on $\mathsf{WKL}$ in this table. This is the expected picture: compactness is what PA avoidance detects.

:::theorem{#thm-coh-pa-avoidance}
$\mathsf{COH}$ admits PA avoidance.
:::

:::proof{of=thm-coh-pa-avoidance}
Let $D \leq_T Z$ with $Z$ not PA relative to $D$, and let $\vec R \leq_T Z$ be a sequence of sets. Use computable Mathias forcing relative to $Z$: the conditions are the Mathias conditions $(\sigma, X)$ with $X \leq_T Z$, and the question of :ref{#prop-mathias-question} for sentences with oracle $Z \oplus G$: $(\sigma, X) \mathrel{?{\vdash}} \varphi$ if some string $\tau$ compatible with $(\sigma, X)$ satisfies $\varphi$. It is $\Sigma^0_1(\mathcal M)$-preserving for the class $\mathcal M$ of the sets computable in $Z$, none of which is PA relative to $D$, by fact 1.

The question is merging. Suppose that $(\sigma, X) \mathrel{?{\nvdash}} \varphi_0$ and $(\sigma, X) \mathrel{?{\nvdash}} \varphi_1$: no string compatible with $(\sigma, X)$ satisfies $\varphi_0$ or $\varphi_1$. If a member $G$ of $(\sigma, X)$ satisfied $\varphi_i$, the use principle would give a prefix of $G$ satisfying $\varphi_i$, and every prefix of $G$ extending $\sigma$ is compatible with $(\sigma, X)$. So $(\sigma, X)$ itself forces $\neg \varphi_0 \wedge \neg \varphi_1$.

By :ref{#thm-local-pa-avoidance}, every sufficiently generic $G$ has $Z \oplus G$ not PA relative to $D$. For each $n$ and $k$, the conditions all of whose members are almost contained in $R_n$ or in $\overline{R_n}$, and those whose stem has an element above $k$, form dense sets, as in the proof of :ref{#thm-coh-cone-avoidance}: the reservoir is replaced by $X \cap R_n$ or $X \setminus R_n$, which are computable in $Z$. So a sufficiently generic $G$ is an $\vec R$-cohesive set with $Z \oplus G$ not PA relative to $D$.
:::

The unrelativized case is part of :ref{#thm-mathias-coh-preservation}, which shows that a sufficiently generic cohesive set computes no DNC function at all. The merging property explains the difference with weak König's lemma. A negative answer of the Mathias question is witnessed by the condition itself: no compatible string makes the computation converge, so nothing has to be chosen, and two negative answers are witnessed by the same condition. For Jockusch–Soare forcing, a negative answer is witnessed by cutting the class down to its members on which the computation diverges; two such cuts can be disjoint, and the question is not merging (see the discussion after :ref{#thm-question-pa}).

## Every set is Δ⁰₂ relative to a non-PA set

The construction of :ref{#thm-delta2-cone-avoidance}, which makes an arbitrary set $\Delta^0_2$ relative to a set avoiding a cone, also avoids PA degrees.

:::theorem{#thm-delta2-pa-avoidance}
Let $D \leq_T Z$ with $Z$ not PA relative to $D$, and let $A$ be an arbitrary set. There is a set $G$ such that $Z \oplus G$ is not PA relative to $D$ and $A \leq_T G'$.
:::

:::proof{of=thm-delta2-pa-avoidance}
Use the notion of forcing and the question of the proof of :ref{#thm-delta2-cone-avoidance}: conditions $(\sigma, m)$, and $(\sigma, m) \mathrel{?{\vdash}} \varphi$ if some $\tau$ with $(\tau, m) \leq (\sigma, m)$ satisfies $\varphi$. That proof shows that the question is $\Sigma^0_1(\{ Z \})$-preserving, and that if $(\sigma, m) \mathrel{?{\nvdash}} \varphi$, then $(\sigma, m)$ itself forces $\neg \varphi$. Applied to two sentences, the second fact shows that the question is merging, with $(\sigma, m)$ as the common extension. Since $Z$ is not PA relative to $D$, :ref{#thm-local-pa-avoidance} with $\mathcal M = \{ Z \}$ shows that $Z \oplus G$ is not PA relative to $D$ for every sufficiently generic $G$. The density argument of that proof gives $A \leq_T G'$ for every sufficiently generic $G$.
:::

:::corollary{#cor-strong-pa-delta2}
A problem $\mathsf P$ admits strong PA avoidance if and only if for all sets $D \leq_T Z$ such that $Z$ is not PA relative to $D$, every instance $X \leq_T Z'$ of $\mathsf P$ has a solution $Y$ such that $Z \oplus Y$ is not PA relative to $D$.
:::

:::proof{of=cor-strong-pa-delta2}
The forward direction is a special case. Conversely, let $D \leq_T Z$ with $Z$ not PA relative to $D$, and let $X$ be any instance. By :ref{#thm-delta2-pa-avoidance} with $A = X$, there is $G$ such that $Z \oplus G$ is not PA relative to $D$ and $X \leq_T G' \leq_T (Z \oplus G)'$. Since $D \leq_T Z \oplus G$, the hypothesis applies to $Z \oplus G$ and gives a solution $Y$ such that $Z \oplus G \oplus Y$ is not PA relative to $D$; by fact 1, neither is $Z \oplus Y$.
:::

The proof keeps the same $D$ and replaces $Z$ by $Z \oplus G$: this is the stability of the definition under iteration announced above. By the corollary, the instances of the pigeonhole principle that matter for strong PA avoidance are the $\Delta^0_2$ sets, which are the limit sets of stable colorings computable in $Z$.

## PA avoidance implies cone avoidance

A problem that avoids PA degrees avoids cones. The proof uses a set that turns a non-computable set into a jump, given by the Posner–Robinson theorem.

:::theorem{#thm-pa-implies-cone}
If a problem admits PA avoidance, it admits cone avoidance. If it admits strong PA avoidance, it admits strong cone avoidance.
:::

:::proof{of=thm-pa-implies-cone}
Let $C \not\leq_T Z$, and let $X$ be an instance of the problem, with $X \leq_T Z$ in the first case. By the Posner–Robinson theorem (:ref{#cor-posner-robinson}) relativized to $Z$, applied to $C$, which is not computable in $Z$, there is a set $G$ with $(Z \oplus G)' \leq_T C \oplus Z \oplus G$. Let $W = Z \oplus G$. Then $W$ is not PA relative to $W$ (fact 2), and $X \leq_T W$ in the first case. PA avoidance with $D = W$ and $W$ in place of $Z$ gives a solution $Y$ such that $W \oplus Y$ is not PA relative to $W$. If $C \leq_T Z \oplus Y$, then
$$
W' \leq_T C \oplus W \leq_T W \oplus Y,
$$
and $W'$ is PA relative to $W$ (fact 2), so $W \oplus Y$ would be PA relative to $W$ (fact 1). Hence $C \not\leq_T Z \oplus Y$.
:::

The converse fails: $\mathsf{WKL}$ admits cone avoidance (:ref{#thm-cone-avoidance-basis}) but not PA avoidance. PA avoidance is therefore a strictly stronger property, and every result of this course gives a cone avoidance result for free. The proof shows why the parameter $D$ is needed: the set relative to which PA degrees are avoided is the set $W = Z \oplus G$ given by the Posner–Robinson theorem.

:::quiz[PA avoidance and cone avoidance]
In the proof of :ref{#thm-pa-implies-cone}, why is PA avoidance applied with $D = W$ rather than with $D = \emptyset$?

- [x] Because PA avoidance requires $W$ not to be PA relative to $D$; with $D = W$ this always holds, whereas $W$ may be PA, and the contradiction uses $W'$, which is PA relative to $W$.
- [ ] Because $W$ is not computable.

  Computability of $W$ plays no role; the relative property is what matters.
- [ ] Because $X$ is computable in $W$ but not in $Z$.

  $X$ is computable in $Z$ in the first case, hence in $W$.

---

Why does the same proof give the strong version?

- [x] Because the instance $X$ is used only as an instance of the problem; strong PA avoidance applied to $W$ gives the solution $Y$ whatever the complexity of $X$.
- [ ] Because $X \leq_T W$ in all cases.

  For an arbitrary instance, $X$ need not be computable in $W$; strong avoidance does not need it.
- [ ] Because the Posner–Robinson theorem gives a strong form.

  The set $G$ is the same in both cases; only the avoidance property applied to $W$ changes.
:::

## Notes and references

The examples, the reduction of strong PA avoidance to $\Delta^0_2$ instances and the comparison with cone avoidance follow the chapter *Compactness avoidance* of Patey's monograph, sections *PA avoidance* and *Comparing avoidances*; :ref{#thm-delta2-pa-avoidance} is an exercise there. The analysis of the difference between Mathias forcing and Jockusch–Soare forcing through the merging property is from the same chapter, which places the forcing questions on a line from the most merging (Cohen, Mathias) to the least (Jockusch–Soare). The Posner–Robinson theorem is due to Posner and Robinson (1981); the relativized form used here, for an arbitrary non-computable set, is due to Jockusch and Shore (1984).

- D. B. Posner and R. W. Robinson, *Degrees joining to 0′*, Journal of Symbolic Logic 46 (1981), 714–722.
- C. G. Jockusch and R. A. Shore, *Pseudo-jump operators II: transfinite iterations, hierarchies and minimal covers*, Journal of Symbolic Logic 49 (1984), 1205–1236.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, sections *PA avoidance* and *Comparing avoidances*.
