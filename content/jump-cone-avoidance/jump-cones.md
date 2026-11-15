---
title: Jump cone avoidance
summary: Jump cone avoidance, its relation with weakly low bases and non-high solutions, and the reduction of its strong version to Δ⁰₃ instances.
duration: 45
prerequisites: [lowness/ramsey-pairs-low2, effective-forcing/mathias-forcing, avoidance/strong-cone-avoidance, cohen-genericity/posner-robinson, immunity-growth/domination, pi01-classes/basis-theorems]
---

The previous courses of the track controlled the first jump of solutions: cone avoidance and lowness. This course controls the **second jump**: it builds solutions $Y$ such that $Y'$ does not compute a given set, or, equivalently, such that the set is not $\Delta^0_2(Y)$. The main example is the jump of $\emptyset'$: a solution $Y$ with $\emptyset'' \not\leq_T Y'$ is a solution that is **not high**.

Second-jump control is first-jump control one level up, with the same three-case argument and the same forcing questions, now for $\Sigma^0_2$ sentences. The difficulty lies in the design of the notion of forcing: a $\Sigma^0_2$ question quantifies over the extensions of a condition, and has the right complexity only if the partial order is simple enough. Computable Mathias forcing fails at this level, since its sufficiently generic sets are high (:ref{#prop-mathias-dominant}). This lesson sets up the definitions, collects the cases that first-jump control settles, and isolates what remains: the pigeonhole principle for arbitrary sets, treated in the last lessons of the course.

## Jump cone avoidance

By Post's theorem relativized (:ref{#thm-post}), a set $C$ is $\Delta^0_2(Y)$ if and only if $C \leq_T Y'$. The definitions are stated in the second form.

:::definition{#def-jump-cone-avoidance}
A problem $\mathsf P$ admits **jump cone avoidance** if for every set $Z$, every set $C$ with $C \not\leq_T Z'$ and every $Z$-computable instance $X$ of $\mathsf P$, there is a solution $Y$ to $X$ with $C \not\leq_T (Z \oplus Y)'$. It admits **strong jump cone avoidance** if the same holds for every instance $X$, computable in $Z$ or not.
:::

The definition is the one of cone avoidance (:ref{#def-cone-avoidance-problem}) one jump up: the hypothesis $C \not\leq_T Z$ becomes $C \not\leq_T Z'$, and the conclusion $C \not\leq_T Z \oplus Y$ becomes $C \not\leq_T (Z \oplus Y)'$. It is relativized for the same reason: to add solutions one after the other, as in :ref{#ex-jca-products}, and to build ω-models.

A set $Y$ is **high relative to $Z$** if $Z'' \leq_T (Z \oplus Y)'$; for $Z = \emptyset$, this is highness (:ref{#def-high}). By Martin's theorem relativized (:ref{#thm-martin-domination}), $Y$ is high relative to $Z$ if and only if $Z \oplus Y$ computes a function that eventually dominates every $Z$-computable function.

:::proposition{#prop-jca-not-high}
If $\mathsf P$ admits jump cone avoidance, then every $Z$-computable instance of $\mathsf P$ has a solution that is not high relative to $Z$. If $\mathsf P$ admits strong jump cone avoidance, this holds for every instance.
:::

:::proof{of=prop-jca-not-high}
Take $C = Z''$. Then $C \not\leq_T Z'$ by the jump theorem relativized (:ref{#thm-jump}). A solution $Y$ with $Z'' \not\leq_T (Z \oplus Y)'$ is not high relative to $Z$.
:::

:::example{#ex-jca-problems}
1. **Problems with a weakly low basis.** If $\mathsf P$ admits a weakly low basis (:ref{#def-weakly-low-basis}), it admits jump cone avoidance: by item 3 of :ref{#prop-weakly-low-properties}, a set $P$ PA relative to $Z'$ with $C \not\leq_T P$ exists by the cone avoidance basis theorem relativized to $Z'$, and a solution with $(Z \oplus Y)' \leq_T P$ works. This covers $\mathsf{WKL}$, $\mathsf{RT}^1_2$ for $Z$-computable instances, $\mathsf{COH}$ (:ref{#thm-coh-weakly-low}), $\mathsf D^2_2$ (:ref{#thm-d22-weakly-low}) and $\mathsf{RT}^2_2$ (:ref{#thm-rt22-weakly-low}).
2. **The jump.** The problem $\mathsf J$, whose solution to $X$ is $X'$, does not admit jump cone avoidance: for $Z = \emptyset$ and $C = \emptyset''$, the only solution $\emptyset'$ of the instance $\emptyset$ has $\emptyset'' \leq_T (\emptyset')'$.
3. **Domination.** Let $\mathsf{DOM}$ be the problem whose instances are all sets $X$, a solution to $X$ being a function that eventually dominates every $X$-computable function. It admits cone avoidance: given $Z$, $C \not\leq_T Z$ and $X \leq_T Z$, :ref{#thm-delta2-cone-avoidance} applied to the set $Z''$ gives $G$ with $C \not\leq_T Z \oplus G$ and $Z'' \leq_T G' \leq_T (Z \oplus G)'$; by Martin's theorem relativized, $Z \oplus G$ computes a function dominating every $Z$-computable function, hence every $X$-computable one. It does not admit jump cone avoidance: every solution to the instance $\emptyset$ is a dominant function, and computes a set that is high, by Martin's theorem.
4. **Computable Mathias forcing** produces high sets (:ref{#prop-mathias-dominant}); so it cannot be the notion of forcing behind a proof of jump cone avoidance, although it gives cone avoidance for $\mathsf{COH}$.
:::

Item 3 shows that cone avoidance does not imply jump cone avoidance. Item 4 is the starting point of :ref{to="jump-cone-avoidance/cohesiveness-second-jump"}.

:::quiz[jump cone avoidance]
In :ref{#prop-jca-not-high}, why is $C = Z''$ an admissible choice?

- [x] Because the definition requires $C \not\leq_T Z'$, and $Z'' \not\leq_T Z'$ by the jump theorem relativized to $Z$.
- [ ] Because $Z''$ is not computable.

  Non-computability is the hypothesis of cone avoidance; here the hypothesis is one jump up.
- [ ] Because $Z''$ is $\Delta^0_3(Z)$.

  Every set computable in $Z''$ is; the relevant point is that $Z''$ is not $\Delta^0_2(Z)$.

---

In item 1 of :ref{#ex-jca-problems}, why is the set $P$ chosen by the cone avoidance basis theorem relativized to $Z'$, rather than by the low basis theorem relativized to $Z'$?

- [x] Because the solution only satisfies $(Z \oplus Y)' \leq_T P$, so $P$ itself must not compute $C$; the cone avoidance basis theorem, applied to the $\Pi^0_1(Z')$ class of $\{0,1\}$-valued functions DNC relative to $Z'$, gives such a $P$ for any $C \not\leq_T Z'$.
- [ ] Because a set PA relative to $Z'$ cannot be low relative to $Z'$.

  It can: this is item 2 of :ref{#prop-weakly-low-properties}. A set $P$ low over $Z'$ avoids $Z''$, but not every set $C \not\leq_T Z'$; for instance, it computes $P$ itself.
- [ ] Because the low basis theorem does not relativize.

  It relativizes.
:::

## What first-jump control gives

Item 1 of :ref{#ex-jca-problems} says that jump cone avoidance often comes from an effective construction at the first level: a solution whose jump is computed by a set $P$ PA relative to $Z'$ inherits the weakness of $P$. Monin and Patey recommend this route as the first one to try, since second-jump control by forcing is technically much heavier. It has two limitations. It gives no control over the sets that the solution itself computes, so it does not combine jump cone avoidance with cone avoidance; this is treated for $\mathsf{WKL}$ and $\mathsf{COH}$ in :ref{to="jump-cone-avoidance/wkl-two-cones"} and :ref{to="jump-cone-avoidance/cohesiveness-second-jump"}. And weakly low bases concern $Z$-computable instances: for other instances, the solution cannot be built effectively relative to $Z$. The next section measures this gap.

## Strong jump cone avoidance and Δ⁰₃ instances

Strong cone avoidance reduces to $\Delta^0_2(Z)$ instances (:ref{#cor-strong-delta2}), because every set is $\Delta^0_2$ relative to a set avoiding a given cone (:ref{#thm-delta2-cone-avoidance}). One jump up, the same holds with $\Delta^0_3$ instances, through Friedberg's jump inversion theorem.

:::theorem{#thm-delta3-jump-cone}
Let $Z$ be a set, $C$ a set with $C \not\leq_T Z'$, and $A$ an arbitrary set. There is a set $G$ with $C \not\leq_T (Z \oplus G)'$ and $A \leq_T (Z \oplus G)''$.
:::

:::proof{of=thm-delta3-jump-cone}
By :ref{#thm-delta2-cone-avoidance} with $Z'$ in place of $Z$, there is a set $H$ with $C \not\leq_T Z' \oplus H$ and $A \leq_T H'$. Let $W = Z' \oplus H$, a set computing $Z'$. By Friedberg's jump inversion theorem relativized to $Z$ (:ref{#cor-jump-inversion}), there is a set $G$ with $(Z \oplus G)' \equiv_T W$. Then $C \not\leq_T (Z \oplus G)'$, and $A \leq_T H' \leq_T W' \equiv_T (Z \oplus G)''$.
:::

:::corollary{#cor-strong-jca-delta3}
A problem $\mathsf P$ admits strong jump cone avoidance if and only if for every set $Z$, every $C \not\leq_T Z'$ and every instance $X$ with $X \leq_T Z''$, there is a solution $Y$ to $X$ with $C \not\leq_T (Z \oplus Y)'$.
:::

:::proof{of=cor-strong-jca-delta3}
The forward direction is a special case. Conversely, let $C \not\leq_T Z'$ and let $X$ be any instance. By :ref{#thm-delta3-jump-cone} with $A = X$, there is $G$ with $C \not\leq_T (Z \oplus G)'$ and $X \leq_T (Z \oplus G)''$. The hypothesis, applied with $Z \oplus G$ in place of $Z$, gives a solution $Y$ with $C \not\leq_T (Z \oplus G \oplus Y)'$, hence $C \not\leq_T (Z \oplus Y)'$.
:::

For the pigeonhole principle, the corollary places the difficulty precisely. The instances computable in $Z'$, that is, the $\Delta^0_2(Z)$ sets, are handled by the theorem of Cholak, Jockusch and Slaman: by :ref{#thm-d22-weakly-low} and item 3 of :ref{#prop-weakly-low-properties}, every $\Delta^0_2(Z)$ set has an infinite subset $Y$, of itself or of its complement, with $C \not\leq_T (Z \oplus Y)'$. Strong jump cone avoidance requires the same for $\Delta^0_3(Z)$ sets. Such a set has in general no $Z$-computable approximation, and the solution cannot be produced by a first-jump construction relative to a set PA relative to $Z'$. This is what the last lessons of the course do.

:::quiz[Δ⁰₃ instances]
In the proof of :ref{#thm-delta3-jump-cone}, what does jump inversion contribute?

- [x] It turns the set $Z' \oplus H$, which avoids the cone and computes $A$ in its jump, into the jump of a set $Z \oplus G$, so that the avoidance moves from the set to its jump and the computation of $A$ from the jump to the double jump.
- [ ] It makes $G$ avoid the cone above $C$.

  The avoidance is inherited from $H$; jump inversion only places $Z' \oplus H$ as a jump.
- [ ] It makes $G$ low.

  Nothing makes $G$ low: its jump computes $Z' \oplus H$, and its double jump computes $A$, which may be any set.

---

In the proof of :ref{#cor-strong-jca-delta3}, why does the hypothesis apply to the instance $X$ with $Z \oplus G$ in place of $Z$?

- [x] Because $X \leq_T (Z \oplus G)''$ and $C \not\leq_T (Z \oplus G)'$, which are the two requirements of the hypothesis for the set $Z \oplus G$.
- [ ] Because $X$ is computable in $Z \oplus G$.

  It need not be; it is only $\Delta^0_3$ relative to $Z \oplus G$.
- [ ] Because jump cone avoidance is closed under joins.

  The argument uses only that the hypothesis holds for every set in place of $Z$.
:::

## Limits

Two examples show that, for the pigeonhole principle, "not high" is the natural bound.

By the theorem of Downey, Hirschfeldt, Lempp and Solomon (:ref{#thm-dhls}), some $\Delta^0_2$ set has no infinite low subset of itself or of its complement; so the solutions cannot be required to be low, even for $\Delta^0_2$ instances. For arbitrary instances, they cannot even be required to be low₂.

:::example{#ex-no-low2-subset}
Let $A$ be 1-generic relative to $\emptyset''$ (:ref{#def-relative-genericity}). No infinite subset of $A$ or of $\overline A$ is low₂. Indeed, a low₂ set $H$ satisfies $H \leq_T H'' \leq_T \emptyset''$. If $H$ is infinite and $\emptyset''$-computable, the set of strings $\sigma$ with $\sigma(n) = 0$ for some $n \in H$, $n < |\sigma|$, is $\emptyset''$-computable and dense: every string can be extended to length $n + 1$, with value $0$ at $n$, for some $n \in H$ beyond its length. So $A$ meets it, and $H \not\subseteq A$. In the same way, with value $1$, $H \not\subseteq \overline A$.
:::

The argument uses only that $A$ and $\overline A$ have no infinite $\Delta^0_3$ subset: $A$ is **bi-immune relative to $\emptyset''$**. Lowness properties of the solutions require some definability of the instance; avoidance properties, such as cone avoidance and jump cone avoidance, do not.

## Exercises

::::exercise{#ex-jca-products difficulty=1 objective="Add solutions one after the other with the relativized definition of jump cone avoidance."}
Show that if $\mathsf P$ and $\mathsf Q$ admit jump cone avoidance, so does their product, whose instances are the pairs $X_0 \oplus X_1$ of an instance of $\mathsf P$ and an instance of $\mathsf Q$, and whose solutions are the pairs $Y_0 \oplus Y_1$ of solutions.

:::solution
Let $Z$ be a set, $C \not\leq_T Z'$, and $X_0 \oplus X_1$ a $Z$-computable instance. Jump cone avoidance of $\mathsf P$ gives a solution $Y_0$ to $X_0$ with $C \not\leq_T (Z \oplus Y_0)'$. The instance $X_1$ is computable in $Z \oplus Y_0$, and $C \not\leq_T (Z \oplus Y_0)'$, so jump cone avoidance of $\mathsf Q$, applied with $Z \oplus Y_0$ in place of $Z$, gives a solution $Y_1$ with $C \not\leq_T (Z \oplus Y_0 \oplus Y_1)'$. Then $Y_0 \oplus Y_1$ is a solution, and $C \not\leq_T (Z \oplus Y_0 \oplus Y_1)'$.
:::
::::

::::exercise{#ex-jca-jump-hyperimmunity difficulty=2 objective="Transfer a domination property from a set PA relative to $Z'$ to the jump of a solution, with the computably dominated basis theorem."}
A problem $\mathsf P$ **preserves jump hyperimmunity** if for every set $Z$, every function $f$ hyperimmune relative to $Z'$ and every $Z$-computable instance $X$, there is a solution $Y$ such that $f$ is hyperimmune relative to $(Z \oplus Y)'$. Show that a problem with a weakly low basis preserves jump hyperimmunity.

:::solution
By the computably dominated basis theorem (:ref{#thm-dominated-basis}) relativized to $Z'$, applied to the non-empty $\Pi^0_1(Z')$ class of $\{0, 1\}$-valued functions DNC relative to $Z'$, there is a set $P$ PA relative to $Z'$ such that every $P$-computable function is dominated by a $Z'$-computable function. The weakly low basis gives a solution $Y$ with $(Z \oplus Y)' \leq_T P$. Let $g$ be a $(Z \oplus Y)'$-computable function. It is $P$-computable, so there is a $Z'$-computable $h$ with $g(n) \leq h(n)$ for every $n$. Since $f$ is hyperimmune relative to $Z'$, $h$ does not dominate $f$: $f(n) > h(n) \geq g(n)$ for infinitely many $n$. So $g$ does not dominate $f$, and $f$ is hyperimmune relative to $(Z \oplus Y)'$.
:::
::::

## Notes and references

Jump cone avoidance, its strong version, the remark that a weakly low basis gives it, and :ref{#ex-jca-jump-hyperimmunity} follow the sections *Context and motivation* and *Use first-jump control* of the chapter *Jump cone avoidance* of Patey's monograph. :ref{#thm-delta3-jump-cone} and :ref{#cor-strong-jca-delta3} are the second-level analogues of :ref{#thm-delta2-cone-avoidance} and :ref{#cor-strong-delta2}, obtained here with jump inversion. Highness and Martin's domination theorem are in Hirschfeldt (Section 2.1, Theorem 2.2), who also notes, in Section 6.4, that some set might have only high infinite $\Delta^0_2$ subsets of itself or of its complement; the theorem of this course produces subsets that are not high, but not $\Delta^0_2$ ones. The theorem that every set has an infinite subset, of itself or of its complement, that is not high is due to Monin and Patey (2019); the same paper proves that every $\Delta^0_3$ set has an infinite low₃ subset of itself or of its complement, which is not proved here.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- R. Downey, D. R. Hirschfeldt, S. Lempp and R. Solomon, *A Δ⁰₂ set with no infinite low subset in either it or its complement*, Journal of Symbolic Logic 66 (2001), 1371–1381.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 2.1 and 6.4.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, sections *Context and motivation* and *Use first-jump control*.

:::::exercises
::::exercise[Problems with a single solution]{#ex-jca-single-solution difficulty=2 objective="See with the Posner–Robinson theorem that a problem whose only solution is a non-computable set fails jump cone avoidance, even when that set is low."}
Let $\mathsf P$ be the problem with the single instance $\emptyset$, whose single solution is a fixed set $Y$. Show that $\mathsf P$ admits jump cone avoidance if and only if $Y$ is computable. Why is the choice $Z = \emptyset$ not enough when $Y$ is low?

:::solution
If $Y$ is computable, then $(Z \oplus Y)' \equiv_T Z'$ for every $Z$, so every $C \not\leq_T Z'$ satisfies $C \not\leq_T (Z \oplus Y)'$.

Conversely, let $Y$ be non-computable. By the Posner–Robinson theorem (:ref{#cor-posner-robinson}) applied to $A = Y$, there is a set $G$ with $Y \oplus G \equiv_T G'$. Take $Z = G$ and $C = G''$. Then $C \not\leq_T G'$ by the jump theorem (:ref{#thm-jump}), the instance $\emptyset$ is $G$-computable, and its only solution satisfies $(G \oplus Y)' \equiv_T (G')' = G''$, which computes $C$. So jump cone avoidance fails.

With $Z = \emptyset$, the hypothesis is $C \not\leq_T \emptyset'$ and the conclusion $C \not\leq_T Y'$. If $Y$ is low, $Y' \leq_T \emptyset'$, and every admissible $C$ satisfies the conclusion. The failure appears only relative to an oracle $Z$ such that $Z \oplus Y$ is much stronger than $Z$; this is why the definition is relativized.
:::
::::

::::exercise[Jump DNC avoidance]{#ex-jca-jump-dnc difficulty=2 objective="Separate the consequences of a low basis from those of a weakly low basis with a jump version of DNC avoidance."}
Say that a set $W$ is **DNC over** a set $D$ if $W$ computes a function $f$ with $f(e) \neq \Phi^D_e(e)$ for every $e$ such that $\Phi^D_e(e)\converge$. A problem $\mathsf P$ admits **jump DNC avoidance** if for every set $Z$, every set $D$ such that $Z'$ is not DNC over $D$, and every $Z$-computable instance $X$, there is a solution $Y$ to $X$ such that $(Z \oplus Y)'$ is not DNC over $D$.

1. Show that a problem with a low basis (:ref{#def-low-basis-problem}) admits jump DNC avoidance.
2. Show that $\mathsf{COH}$ admits a weakly low basis but not jump DNC avoidance.

:::solution
1. Let $Z$, $D$ and $X$ be as in the definition, and $Y$ a solution with $(Z \oplus Y)' \leq_T Z'$. Every function computable in $(Z \oplus Y)'$ is computable in $Z'$, so none of them is DNC relative to $D$, and $(Z \oplus Y)'$ is not DNC over $D$.
2. $\mathsf{COH}$ admits a weakly low basis by :ref{#thm-coh-weakly-low}. Take $Z = \emptyset$ and $D = \emptyset'$. The set $\emptyset'$ is not DNC over $\emptyset'$: if $f = \Phi^{\emptyset'}_e$ is total, then $f(e) = \Phi^{\emptyset'}_e(e)$. Let $\vec R$ be the computable sequence of :ref{#prop-coh-no-low}. The jump of every $\vec R$-cohesive set $Y$ is PA relative to $\emptyset'$, hence computes a $\{0, 1\}$-valued function DNC relative to $\emptyset'$, so $Y'$ is DNC over $\emptyset'$. So the instance $\vec R$ has no solution as required.

A weakly low basis bounds the jump of a solution by an arbitrary set PA relative to $Z'$; such a set is itself DNC over $Z'$, which is why the property is not inherited. Adapted from an exercise of the chapter *Jump cone avoidance* of Patey's monograph.
:::
::::

::::exercise[Generic sets relative to an arbitrary instance]{#ex-jca-generic difficulty=2 objective="Build a solution by finite extensions without any definability of the instance, and obtain strong jump cone avoidance for a problem of genericity."}
Let $\mathsf{GEN}_2$ be the problem whose instances are all sets $X$, a solution to $X$ being a set that is 1-generic relative to $X'$. Show that $\mathsf{GEN}_2$ admits strong jump cone avoidance.

:::solution
Fix $Z$, a set $C \not\leq_T Z'$ and an instance $X$. We build $G = \bigcup_s \sigma_s$, a union of strings $\sigma_0 \preceq \sigma_1 \preceq \cdots$, handling once each of the following countably many requirements, one at each step.

- For an $X'$-c.e. set of strings $W$: if some $\tau \succeq \sigma_s$ is in $W$, let $\sigma_{s+1} = \tau$; otherwise $\sigma_s$ has no extension in $W$, and $\sigma_{s+1} = \sigma_s$.
- For a $Z$-c.e. set of strings $W$: the same.
- For an index $e$: we ensure $\Phi^{Z' \oplus G}_e \neq C$. If there are $x$ and $\tau \succeq \sigma_s$ with $\Phi^{Z' \oplus \tau}_e(x)\converge \neq C(x)$, the oracle queries to the second component being below $|\tau|$, let $\sigma_{s+1} = \tau$. If there is $x$ such that no $\tau \succeq \sigma_s$ makes $\Phi^{Z' \oplus \tau}_e(x)$ converge, let $\sigma_{s+1} = \sigma_s$; then $\Phi^{Z' \oplus G}_e(x)\diverge$, since a convergent computation would only use a prefix of $G$ extending $\sigma_s$. In the remaining case, for every $x$ some $\tau \succeq \sigma_s$ makes the computation converge, and every convergent value is $C(x)$; searching for such a $\tau$ computes $C$ from $Z'$, which is excluded.

The set $G$ is 1-generic relative to $X'$, so it is a solution to $X$. It is 1-generic relative to $Z$, so $(Z \oplus G)' \leq_T G \oplus Z'$ by :ref{#lem-relative-generic-low}. Since $C \not\leq_T Z' \oplus G$, we get $C \not\leq_T (Z \oplus G)'$.

The construction is not effective in any oracle; it only uses that the requirements are countably many. This is the remark at the end of the lesson: avoidance properties do not require the instance to be definable.
:::
::::

::::exercise[Transfer along computable reductions]{#ex-jca-computable-reduction difficulty=1 objective="Check that jump cone avoidance is inherited along computable reductions, and see why the strong version needs strong reductions."}
Let $\mathsf P \leq_c \mathsf Q$ (:ref{#def-computable-reducible}). Show that if $\mathsf Q$ admits jump cone avoidance, so does $\mathsf P$. Show that if $\mathsf P \leq_{sc} \mathsf Q$ and $\mathsf Q$ admits strong jump cone avoidance, so does $\mathsf P$. Where does the argument for the strong version fail with $\leq_c$?

:::solution
Let $Z$ be a set, $C \not\leq_T Z'$ and $X$ a $Z$-computable instance of $\mathsf P$. The instance $\widetilde X$ of $\mathsf Q$ given by the reduction is computable in $X$, hence in $Z$. Jump cone avoidance of $\mathsf Q$ gives a solution $\widetilde Y$ with $C \not\leq_T (Z \oplus \widetilde Y)'$. The set $X \oplus \widetilde Y$ computes a solution $Y$ to $X$; then $Y \leq_T Z \oplus \widetilde Y$, so $(Z \oplus Y)' \leq_T (Z \oplus \widetilde Y)'$ and $C \not\leq_T (Z \oplus Y)'$.

For the strong version, $X$ is arbitrary and $\widetilde X$ too; strong jump cone avoidance of $\mathsf Q$ gives $\widetilde Y$ with $C \not\leq_T (Z \oplus \widetilde Y)'$. With $\leq_{sc}$, $\widetilde Y$ alone computes a solution $Y$, and the same computation concludes. With $\leq_c$, the solution is computed by $X \oplus \widetilde Y$, and the bound becomes $(Z \oplus Y)' \leq_T (Z \oplus X \oplus \widetilde Y)'$, about which nothing is known, since $X$ need not be computable in $Z$.
:::
::::
:::::
