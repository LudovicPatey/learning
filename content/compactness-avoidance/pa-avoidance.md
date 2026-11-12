---
title: PA avoidance
summary: PA avoidance and strong PA avoidance as properties of problems; ω-models without PA sets; merging forcing questions relative to the condition and the abstract PA avoidance theorem; cohesiveness admits PA avoidance; every set is Δ⁰₂ relative to a non-PA set; PA avoidance implies cone avoidance.
duration: 45
prerequisites: [avoidance/forcing-question-method, cohen-genericity/posner-robinson, big-five/wkl0]
---

Weak König's lemma is the compactness principle of second-order arithmetic: over $\mathsf{RCA}_0$ it is equivalent to the Heine–Borel theorem for $[0, 1]$, to the completeness theorem for countable languages, and to many other theorems whose proofs use compactness. Its computable content is captured by one class of sets: a Turing ideal is a model of $\mathsf{WKL}_0$ exactly when it contains, for each of its members $X$, a set that is PA relative to $X$ (:ref{#prop-wkl-scott}). A theorem whose proof avoids compactness should therefore have computable instances with solutions that are not PA. This course studies when this is the case, and how to prove it. Its central result is Liu's theorem: every computable coloring of pairs has an infinite homogeneous set that is not PA, so that Ramsey's theorem for pairs does not imply weak König's lemma.

The method is the one of the course on cone avoidance: a notion of forcing whose generic sets are solutions, a forcing question whose answers are $\Sigma^0_1$ relative to the condition, and a three-case argument. What changes is the property of the question that is needed. To avoid a cone, the question must only be simple. To avoid PA degrees, it must also be able to force **two negative answers at once**. This lesson sets up the property of problems, proves the abstract theorem with this extra property, called merging, and derives the first examples.

## PA relative to a set

For a set $D$, let $J^D$ be the partial $D$-computable function defined by $J^D(x) = \Phi^D_x(x)$ if this computation converges with value $0$ or $1$, and undefined otherwise; write $J$ for $J^\emptyset$. A function $f : \nat \to \{0, 1\}$ is **diagonally non-computable relative to $D$**, or $\mathrm{DNC}_2$ relative to $D$, if $f(x) \neq J^D(x)$ whenever $J^D(x)$ is defined. This is the definition of :ref{#ex-pa-relative}: values of $\Phi^D_x(x)$ other than $0$ and $1$ never coincide with $f(x)$, so they can be ignored. A set $Y$ is **PA relative to $D$** if it computes such a function. Three facts are used constantly.

1. The class of sets that are PA relative to $D$ is closed upwards under Turing reducibility.
2. No set computable in $D$ is PA relative to $D$, by :ref{#thm-dnc2-no-computable} relativized; and $D'$ is PA relative to $D$.
3. The class $\mathrm{DNC}_2^D$ of the functions $\mathrm{DNC}_2$ relative to $D$ is a non-empty $\Pi^0_1(D)$ class, all of whose members are PA relative to $D$.

The partial function $J^D$ is used instead of $x \mapsto \Phi^D_x(x)$ because it has values in $\{0, 1\}$: if $J^D(x)$ is defined and $v \in \{0, 1\}$ differs from $1 - J^D(x)$, then $v = J^D(x)$. This simplifies all the case analyses of the course.

## PA avoidance for problems

:::definition{#def-pa-avoidance}
Let $\mathsf P$ be a problem (:ref{#def-problem}).

1. $\mathsf P$ admits **PA avoidance** if for all sets $D \leq_T Z$ such that $Z$ is not PA relative to $D$, and every instance $X \leq_T Z$ of $\mathsf P$, there is a solution $Y$ to $X$ such that $Z \oplus Y$ is not PA relative to $D$.
2. $\mathsf P$ admits **strong PA avoidance** if the same holds for **every** instance $X$ of $\mathsf P$.
:::

As for cone avoidance (:ref{#def-cone-avoidance-problem}), the set $Z$ bounds the instances and is added to the solution, and strong avoidance quantifies over all instances. The second parameter $D$ is new. Two values of $D$ are used. With $D = \emptyset$, the definition says that a problem never forces its solutions to be PA, even together with a non-PA set $Z$: this is the form that builds ω-models. With $D = Z$, it says that $Z \oplus Y$ is not PA relative to $Z$: this is the relativization of the case $D = Z = \emptyset$, and it is the form used to compare PA avoidance with cone avoidance at the end of the lesson. The definition with $D \leq_T Z$ arbitrary contains both, and is stable under the iterations of later proofs, where $Z$ grows and $D$ stays fixed.

The two special cases do not imply each other. A set that is PA relative to $Z$ computes $Z$ (:ref{#ex-pa-relative}) and a member of every $\Pi^0_1(Z)$ class, in particular of $\mathrm{DNC}_2$, so it is PA. The case $D = \emptyset$ thus has the stronger conclusion ($Z \oplus Y$ is not PA), but also the stronger hypothesis ($Z$ is not PA); the case $D = Z$ applies to every $Z$, but only says that $Z \oplus Y$ is not PA relative to $Z$. For instance, if $Z$ is PA, the case $D = \emptyset$ says nothing, while the case $D = Z$ still does.

PA avoidance is a family of preservation properties in the sense of :ref{#def-weakness}. For a set $D$, let
$$
\mathcal W_D = \{ Z : Z \oplus D \text{ is not PA relative to } D \}.
$$
If $Y \leq_T Z$ and $Z \in \mathcal W_D$, then $Y \oplus D \leq_T Z \oplus D$, so $Y \in \mathcal W_D$ by fact 1: each $\mathcal W_D$ is a weakness property. By fact 2, $D \in \mathcal W_D$, and $\mathcal W_\emptyset$ is the class of the sets that are not PA.

:::proposition{#prop-pa-avoidance-model}
1. A problem $\mathsf P$ admits PA avoidance if and only if it preserves $\mathcal W_D$ for every set $D$.
2. If $\mathsf P$ admits PA avoidance, there is a Turing ideal satisfying $\mathsf P$ that contains no PA set; it is not a Scott ideal.
3. If $\mathsf P$ admits PA avoidance and a problem $\mathsf Q$ has a computable instance all of whose solutions are PA, then $\mathsf Q \not\leq_\omega \mathsf P$. In particular $\mathsf{WKL} \not\leq_\omega \mathsf P$.
:::

:::proof{of=prop-pa-avoidance-model}
1. Suppose that $\mathsf P$ admits PA avoidance, let $Z \in \mathcal W_D$ and let $X \leq_T Z$ be an instance. The set $Z \oplus D$ computes $D$ and is not PA relative to $D$, and $X \leq_T Z \oplus D$, so there is a solution $Y$ such that $Z \oplus D \oplus Y$ is not PA relative to $D$, that is, $Z \oplus Y \in \mathcal W_D$. Conversely, if $D \leq_T Z$, then $Z \oplus D \equiv_T Z$, so "$Z$ is not PA relative to $D$" means $Z \in \mathcal W_D$, and preservation of $\mathcal W_D$ is the definition.
2. By item 1, $\mathsf P$ preserves $\mathcal W_\emptyset$, which contains $\emptyset$. By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W_\emptyset$ satisfying $\mathsf P$. It contains no set PA relative to $\emptyset \in \mathcal I$, so it is not a Scott ideal (:ref{#prop-wkl-scott}).
3. The problem $\mathsf Q$ does not preserve $\mathcal W_\emptyset$; apply :ref{#thm-preservation-separation}. The tree of $\mathrm{DNC}_2$ is a computable instance of $\mathsf{WKL}$ all of whose solutions are PA.
:::

When $\mathsf P$ comes from a $\Pi^1_2$ theorem, the first item gives an ω-model of $\mathsf{RCA}_0 + \mathsf P$ that is not a model of $\mathsf{WKL}_0$. This is how Ramsey's theorem for pairs will be separated from weak König's lemma.

## Merging forcing questions

Recall the three-case argument of :ref{#thm-local-cone-avoidance}. Given a condition $c$ and a functional $\Phi_e$, the set $U$ of pairs $(x, v)$ for which the forcing question answers yes about "$\Phi^{Z \oplus G}_e(x)\converge = v$" is $\Sigma^0_1$ relative to the condition. To prevent $\Phi^{Z \oplus G}_e$ from computing a set $C$, it suffices to find a wrong pair in $U$ or a right pair missing from $U$. To prevent $\Phi^{Z \oplus G}_e$ from being a $\mathrm{DNC}_2$ function, the first case is the same: a pair $(x, J(x))$ in $U$ lets one force $\Phi^{Z \oplus G}_e(x) = J(x)$. The second case is different. There is no right value to miss: if $J(x)$ is undefined, both values $0$ and $1$ are right. What one can hope for is a number $x$ such that **neither** $(x, 0)$ nor $(x, 1)$ is in $U$, and then one needs an extension that forces both negations at once, so that $\Phi^{Z \oplus G}_e(x)$ has no value in $\{0, 1\}$. Two separate extensions, one for each negation, are useless.

This is the property of :ref{#def-question-merging}: a forcing question is **merging** if, whenever $c \mathrel{?{\nvdash}} \varphi_0$ and $c \mathrel{?{\nvdash}} \varphi_1$ for two $\Sigma^0_1$ sentences, some extension of $c$ forces $\neg \varphi_0 \wedge \neg \varphi_1$. In this course, as in :ref{to="avoidance/forcing-question-method"}, a set $Z$ is fixed and the sentences are built with functionals of the oracle $Z \oplus G$.

:::theorem{#thm-local-pa-avoidance}
Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving merging forcing question (:ref{#def-question-local}), and let $D$ be a set such that no member of $\mathcal M$ is PA relative to $D$. For every sufficiently generic set $G$, $Z \oplus G$ is not PA relative to $D$.
:::

:::proof{of=thm-local-pa-avoidance}
For each $e$, let $E_e$ be the set of conditions $d$ for which there is $x$ such that either $J^D(x)$ is defined and $d \Vdash \Phi^{Z \oplus G}_e(x)\converge = J^D(x)$, or $d \Vdash \neg (\Phi^{Z \oplus G}_e(x)\converge = 0) \wedge \neg (\Phi^{Z \oplus G}_e(x)\converge = 1)$. On every member of a condition of $E_e$, $\Phi^{Z \oplus G}_e$ is not a $\mathrm{DNC}_2$ function relative to $D$: in the first case it agrees with $J^D$ at $x$, in the second it has no value in $\{0, 1\}$ at $x$.

We show that $E_e$ is dense. Let $c$ be a condition and $X \in \mathcal M$ as in :ref{#def-question-local}. The set
$$
U = \{ (x, v) \in \nat \times \{ 0, 1 \} : c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge = v \}
$$
is $\Sigma^0_1(X)$.

1. If $(x, J^D(x)) \in U$ for some $x$ with $J^D(x)$ defined, property 1 of the question gives an extension in $E_e$.
2. If $(x, 0) \notin U$ and $(x, 1) \notin U$ for some $x$, the question is merging, so some extension forces both negations, and belongs to $E_e$.
3. Otherwise, for every $x$ some $v < 2$ satisfies $(x, v) \in U$, and no such $v$ equals $J^D(x)$ when $J^D(x)$ is defined. Let $g(x)$ be the second coordinate of the first pair with first coordinate $x$ in an $X$-computable enumeration of $U$. Then $g$ is total, $X$-computable, $\{0, 1\}$-valued, and $g(x) \neq J^D(x)$ whenever $J^D(x)$ is defined. So $X$ is PA relative to $D$, which is excluded.

A set $G$ generic for the sets $E_e$ is a member of a condition of each $E_e$ (:ref{#lem-generic-set}), so no $\Phi^{Z \oplus G}_e$ is $\mathrm{DNC}_2$ relative to $D$.
:::

The theorem is :ref{#thm-question-pa} with two changes: the oracle $X$ depends on the condition, and case 3 is handled by a selection from $U$ instead of a self-referential index. The selection argument makes visible what case 3 produces: a $\{0, 1\}$-valued function that is computable in $X$ and differs from $J^D$ wherever $U$ contains only right pairs. It is this form of the argument that extends, in the next lesson, to questions that are not merging.

:::quiz[the abstract PA avoidance theorem]
In the proof of :ref{#thm-local-pa-avoidance}, why can case 2 not be handled with property 2 of the question alone?

- [x] Property 2 gives an extension forcing $\neg (\Phi^{Z \oplus G}_e(x)\converge = 0)$ and another one forcing $\neg (\Phi^{Z \oplus G}_e(x)\converge = 1)$; on the first, $\Phi^{Z \oplus G}_e(x)$ may still converge to $1$, which may be a correct value when $J^D(x)$ is undefined.
- [ ] Because property 2 only applies to $\Pi^0_1$ sentences.

  Property 2 applies to the $\Sigma^0_1$ sentences asked about; it gives an extension forcing their negations.
- [ ] Because $J^D(x)$ is not computable.

  The complexity of $J^D$ plays a role in case 3 only.

---

In case 3, why is the function $g$ total?

- [x] Because case 2 fails: for every $x$, one of $(x, 0)$ and $(x, 1)$ is in $U$, so the enumeration eventually lists a pair with first coordinate $x$.
- [ ] Because case 1 fails.

  The failure of case 1 makes the values of $g$ correct, not defined.
- [ ] Because $X$ is not PA relative to $D$.

  This hypothesis is what case 3 contradicts.
:::

## First examples

:::example{#ex-pa-avoidance-problems}
The following table collects the problems of :ref{#ex-cone-avoidance-problems}, with the results of this course.

| problem | PA avoidance | strong PA avoidance |
| --- | --- | --- |
| $\mathsf{RT}^1_2$ | yes (trivial) | yes, Liu (:ref{to="compactness-avoidance/liu-theorem"}) |
| $\mathsf{WKL}$ | no | no |
| $\mathsf{COH}$ | yes (:ref{#thm-coh-pa-avoidance}) | yes (:ref{to="compactness-avoidance/liu-theorem"}, exercise) |
| $\mathsf{RT}^2_2$ | yes, Liu (:ref{to="compactness-avoidance/liu-theorem"}) | no |
| $\mathsf{RT}^3_2$ | no | no |
| $\mathsf J$ | no | no |

1. **$\mathsf{RT}^1_2$.** A $Z$-computable set has a $Z$-computable solution $Y$, and $Z \oplus Y \equiv_T Z$ is not PA relative to $D$.
2. **$\mathsf{WKL}$.** The tree of $\mathrm{DNC}_2$ is computable, and all its paths are PA.
3. **$\mathsf{RT}^2_2$, $\mathsf{RT}^3_2$, $\mathsf J$.** Each has an instance all of whose solutions compute $\emptyset'$, which is PA: for $\mathsf{RT}^2_2$ an instance computable in $\emptyset'$, for the other two computable instances (:ref{#ex-cone-avoidance-problems}).
:::

Cone avoidance and PA avoidance differ only on $\mathsf{WKL}$ in this table. This is the expected picture: compactness is what PA avoidance detects.

:::theorem{#thm-coh-pa-avoidance}
$\mathsf{COH}$ admits PA avoidance.
:::

:::proof{of=thm-coh-pa-avoidance}
Let $D \leq_T Z$ with $Z$ not PA relative to $D$, and let $\vec R \leq_T Z$ be a sequence of sets. Use computable Mathias forcing relative to $Z$: the conditions are the Mathias conditions $(\sigma, X)$ with $X \leq_T Z$, and the question of :ref{#prop-mathias-question} for sentences with oracle $Z \oplus G$: $(\sigma, X) \mathrel{?{\vdash}} \varphi$ if some string $\tau$ compatible with $(\sigma, X)$ satisfies $\varphi$. It is $\Sigma^0_1(\mathcal M)$-preserving for the class $\mathcal M$ of the sets computable in $Z$, none of which is PA relative to $D$, by fact 1.

The question is merging. Suppose that $(\sigma, X) \mathrel{?{\nvdash}} \varphi_0$ and $(\sigma, X) \mathrel{?{\nvdash}} \varphi_1$: no string compatible with $(\sigma, X)$ satisfies $\varphi_0$ or $\varphi_1$. If a member $G$ of $(\sigma, X)$ satisfied $\varphi_i$, the use principle would give a prefix of $G$ satisfying $\varphi_i$, and every prefix of $G$ extending $\sigma$ is compatible with $(\sigma, X)$. So $(\sigma, X)$ itself forces $\neg \varphi_0 \wedge \neg \varphi_1$.

By :ref{#thm-local-pa-avoidance}, every sufficiently generic $G$ has $Z \oplus G$ not PA relative to $D$. The sets of conditions all of whose members are $\vec R$-cohesive for a given $R_n$, or have an element above a given $k$, are dense, as in the proof of :ref{#thm-coh-cone-avoidance}: the reservoir is replaced by $X \cap R_n$ or $X \setminus R_n$, which are computable in $Z$. So a sufficiently generic $G$ is an $\vec R$-cohesive set with $Z \oplus G$ not PA relative to $D$.
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

## Exercises

::::exercise{difficulty=1}
Show that if $\mathsf P_0$ and $\mathsf P_1$ admit PA avoidance, so does the product $\mathsf P_0 \times \mathsf P_1$ of :ref{#prop-cone-avoidance-product}, and that if $\mathsf P \leq_\omega \mathsf Q$ and $\mathsf Q$ admits PA avoidance, so does $\mathsf P$.

:::solution
Let $D \leq_T Z$ with $Z$ not PA relative to $D$, and $X_0 \oplus X_1 \leq_T Z$. PA avoidance of $\mathsf P_0$ gives $Y_0$ with $Z \oplus Y_0$ not PA relative to $D$. Then $D \leq_T Z \oplus Y_0$ and $X_1 \leq_T Z \oplus Y_0$, so PA avoidance of $\mathsf P_1$ relative to $Z \oplus Y_0$, with the same $D$, gives $Y_1$ with $Z \oplus Y_0 \oplus Y_1$ not PA relative to $D$. For the second statement, by :ref{#prop-pa-avoidance-model} (1) it suffices to show that $\mathsf P$ preserves each $\mathcal W_D$; this follows from the exercise of :ref{to="reducibilities/preservation"} stating that $\mathsf P \leq_\omega \mathsf Q$ and preservation of a weakness property by $\mathsf Q$ imply its preservation by $\mathsf P$.
:::
::::

## Notes and references

PA avoidance as a property of problems, with the parameter $D$, follows the chapter *Compactness avoidance* of Patey's monograph, section *PA avoidance*; the notion is implicit in Liu's separation of Ramsey's theorem for pairs from weak König's lemma (2012), and preservation of non-PA degrees is used as a separation tool by Dzhafarov and Mummert (Corollary 4.6.15). Merging forcing questions are defined in the same chapter (called $\Pi^0_1$-merging) and in the chapter *Effective forcing* of Monin and Patey. The reduction to Δ⁰₂ instances and the comparison with cone avoidance through the Posner–Robinson theorem are in the same section and in section *Comparing avoidances* of the monograph; :ref{#thm-delta2-pa-avoidance} is an exercise there. The Posner–Robinson theorem is due to Posner and Robinson (1981), in the form of Jockusch and Shore (1984).

- J. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- D. B. Posner and R. W. Robinson, *Degrees joining to 0′*, Journal of Symbolic Logic 46 (1981), 714–722.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 4.6.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, sections *PA avoidance* and *Comparing avoidances*.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Forcing question*.
