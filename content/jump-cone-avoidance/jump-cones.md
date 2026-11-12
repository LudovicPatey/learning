---
title: Jump cone avoidance
summary: A problem admits jump cone avoidance if its instances have solutions whose jump avoids a given cone; weakly low bases give it for free; jump cone avoidance gives solutions that are not high; strong jump cone avoidance reduces to Δ⁰₃ instances, which is where second-jump control becomes necessary.
duration: 45
prerequisites: [lowness/ramsey-pairs-low2, effective-forcing/mathias-forcing, avoidance/forcing-question-method, cohen-genericity/posner-robinson, immunity-growth/domination, pi01-classes/basis-theorems]
---

The previous courses of the track controlled the first jump of the solutions of a problem: cone avoidance says that a solution does not compute a given set, and lowness that its jump is no more complex than $\emptyset'$. This course controls the **second jump**: it builds solutions $Y$ such that $Y'$ does not compute a given set, or, equivalently, such that the set is not $\Delta^0_2(Y)$. The main example is the jump of $\emptyset'$: a solution $Y$ with $\emptyset'' \not\leq_T Y'$ is a solution that is **not high**.

Second-jump control is first-jump control one level up, with the same three-case argument and the same forcing questions, now for $\Sigma^0_2$ sentences. The difficulty is not in the abstract argument but in the design of the notion of forcing: a $\Sigma^0_2$ question quantifies over the extensions of a condition, and is of the right complexity only if the partial order is simple enough. Computable Mathias forcing, the basic tool for combinatorial principles, fails at this level, since its sufficiently generic sets are high (:ref{#prop-mathias-dominant}). The course follows the chapter *Jump cone avoidance* of Patey's monograph. This lesson sets up the definitions, collects the cases that first-jump control already settles, and isolates what remains: the pigeonhole principle for arbitrary sets, the subject of the last three lessons, which prove the theorem of Monin and Patey that every set has an infinite subset, of itself or of its complement, that is not high.

## Jump cone avoidance

By Post's theorem relativized (:ref{#thm-post}), a set $C$ is $\Delta^0_2(Y)$ if and only if $C \leq_T Y'$. The definitions are stated in the second form.

:::definition{#def-jump-cone-avoidance}
A problem $\mathsf P$ admits **jump cone avoidance** if for every set $Z$, every set $C$ with $C \not\leq_T Z'$ and every $Z$-computable instance $X$ of $\mathsf P$, there is a solution $Y$ to $X$ with $C \not\leq_T (Z \oplus Y)'$. It admits **strong jump cone avoidance** if the same holds for every instance $X$, computable in $Z$ or not.
:::

The definition is the one of cone avoidance (:ref{#def-cone-avoidance-problem}) one jump up: the hypothesis $C \not\leq_T Z$ becomes $C \not\leq_T Z'$, and the conclusion $C \not\leq_T Z \oplus Y$ becomes $C \not\leq_T (Z \oplus Y)'$. It is relativized for the same reason: to add solutions one after the other, as in the following exercise on products, and to build ω-models.

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

Item 3 shows that cone avoidance does not imply jump cone avoidance. Item 4 is the starting point of the third lesson.

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

Item 1 of :ref{#ex-jca-problems} says that jump cone avoidance often comes from an effective construction at the first level: a solution whose jump is computed by a set $P$ PA relative to $Z'$ inherits the weakness of $P$. Monin and Patey recommend this route as the first one to try, since second-jump control by forcing is technically much heavier. It has two limitations.

The first is that it does not combine with cone avoidance. For $\mathsf{WKL}$, the low basis theorem gives a path $G$ with $D \not\leq_T G'$ for a given $D \not\leq_T \emptyset'$, and the cone avoidance basis theorem a path with $C \not\leq_T G$ for a given non-computable $C$; but a low path computes no non-computable set $C$ only if $C$ is not computable in any low set, and a path with $G' \leq_T P$ may compute $C \leq_T \emptyset'$, since $P$ computes $\emptyset'$. Obtaining both properties at once is a genuine second-jump argument; it is done in the next lesson for $\mathsf{WKL}$ and in the third for $\mathsf{COH}$.

The second limitation is that weakly low bases concern $Z$-computable instances. For instances that are not computable in $Z$, the solution cannot be built effectively relative to $Z$. The next section measures the gap for strong jump cone avoidance.

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

For the pigeonhole principle, the corollary places the difficulty precisely. Instances computable in $Z'$, that is, $\Delta^0_2(Z)$ sets, are handled by the theorem of Cholak, Jockusch and Slaman: $\mathsf D^2_2$ admits a weakly low basis (:ref{#thm-d22-weakly-low}), hence jump cone avoidance, and its instances relative to $Z$ are the $\Delta^0_2(Z)$ sets. Strong jump cone avoidance requires the same for $\Delta^0_3(Z)$ sets. Such a set is not the limit of a $Z$-computable approximation, and a solution cannot be produced by a first-jump construction relative to a set PA relative to $Z'$: the reservoirs of the Dzhafarov–Jockusch forcing must now be chosen with information about $Z''$. This is what the last three lessons do.

:::quiz[Δ⁰₃ instances]
In the proof of :ref{#thm-delta3-jump-cone}, what does jump inversion contribute?

- [x] It turns the set $Z' \oplus H$, which avoids the cone and computes $A$ in its jump, into the jump of a set $Z \oplus G$, so that the avoidance moves from the set to its jump and the computation of $A$ from the jump to the double jump.
- [ ] It makes $G$ avoid the cone above $C$.

  The avoidance is inherited from $H$; jump inversion only places $Z' \oplus H$ as a jump.
- [ ] It makes $G$ low.

  $G$ is far from low: its jump computes $Z'$ and $H$.

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

::::exercise{difficulty=1}
Show that if $\mathsf P$ and $\mathsf Q$ admit jump cone avoidance, so does their product, whose instances are the pairs $X_0 \oplus X_1$ of an instance of $\mathsf P$ and an instance of $\mathsf Q$, and whose solutions are the pairs $Y_0 \oplus Y_1$ of solutions.

:::solution
Let $Z$ be a set, $C \not\leq_T Z'$, and $X_0 \oplus X_1$ a $Z$-computable instance. Jump cone avoidance of $\mathsf P$ gives a solution $Y_0$ to $X_0$ with $C \not\leq_T (Z \oplus Y_0)'$. The instance $X_1$ is computable in $Z \oplus Y_0$, and $C \not\leq_T (Z \oplus Y_0)'$, so jump cone avoidance of $\mathsf Q$, applied with $Z \oplus Y_0$ in place of $Z$, gives a solution $Y_1$ with $C \not\leq_T (Z \oplus Y_0 \oplus Y_1)'$. Then $Y_0 \oplus Y_1$ is a solution, and $C \not\leq_T (Z \oplus Y_0 \oplus Y_1)'$.
:::
::::

::::exercise{difficulty=2}
A problem $\mathsf P$ **preserves jump hyperimmunity** if for every set $Z$, every function $f$ hyperimmune relative to $Z'$ and every $Z$-computable instance $X$, there is a solution $Y$ such that $f$ is hyperimmune relative to $(Z \oplus Y)'$. Show that a problem with a weakly low basis preserves jump hyperimmunity.

:::solution
By the computably dominated basis theorem (:ref{#thm-dominated-basis}) relativized to $Z'$, applied to the non-empty $\Pi^0_1(Z')$ class of $\{0, 1\}$-valued functions DNC relative to $Z'$, there is a set $P$ PA relative to $Z'$ such that every $P$-computable function is dominated by a $Z'$-computable function. The weakly low basis gives a solution $Y$ with $(Z \oplus Y)' \leq_T P$. Let $g$ be a $(Z \oplus Y)'$-computable function. It is $P$-computable, so there is a $Z'$-computable $h$ with $g(n) \leq h(n)$ for every $n$. Since $f$ is hyperimmune relative to $Z'$, $h$ does not dominate $f$: $f(n) > h(n) \geq g(n)$ for infinitely many $n$. So $g$ does not dominate $f$, and $f$ is hyperimmune relative to $(Z \oplus Y)'$.
:::
::::

::::exercise{difficulty=2}
Let $\mathsf P$ admit jump cone avoidance. Show that there is a Turing ideal satisfying $\mathsf P$ none of whose members is high. Deduce that $\mathsf{DOM}$ (:ref{#ex-jca-problems}) is not ω-reducible to $\mathsf P$, and that the ideal does not contain $\emptyset'$.

:::solution
Let $\mathcal W$ be the class of sets $Y$ with $\emptyset'' \not\leq_T Y'$. It is closed downward under Turing reducibility, since $W \leq_T Y$ implies $W' \leq_T Y'$, and it contains $\emptyset$. Let $Z \in \mathcal W$ and $X \leq_T Z$ an instance. The set $C = \emptyset''$ satisfies $C \not\leq_T Z'$, so jump cone avoidance gives a solution $Y$ with $\emptyset'' \not\leq_T (Z \oplus Y)'$, that is, $Z \oplus Y \in \mathcal W$. So $\mathsf P$ preserves $\mathcal W$ (:ref{#def-weakness}), and :ref{#lem-preservation-ideal} gives a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf P$. The instance $\emptyset \in \mathcal I$ of $\mathsf{DOM}$ has no solution in $\mathcal I$, since a dominant function is high by Martin's theorem, so $\mathcal I$ does not satisfy $\mathsf{DOM}$; an ideal satisfying $\mathsf P$ in which some instance of $\mathsf{DOM}$ has no solution witnesses that $\mathsf{DOM} \not\leq_\omega \mathsf P$. Finally $\emptyset'$ is high, so $\emptyset' \notin \mathcal I$.
:::
::::

## Notes and references

Jump cone avoidance, its strong version, the remark that a weakly low basis gives jump cone avoidance, and the exercise on jump hyperimmunity follow the sections *Context and motivation* and *Use first-jump control* of the chapter *Jump cone avoidance* of Patey's monograph, where the reduction to first-jump control is recommended as the first approach. :ref{#thm-delta3-jump-cone} and :ref{#cor-strong-jca-delta3} are the second-level analogues of :ref{#thm-delta2-cone-avoidance} and :ref{#cor-strong-delta2}, obtained here by combining them with jump inversion. Highness and Martin's domination theorem are presented by Hirschfeldt (Section 2.1, Theorem 2.2), who also records, in Section 6.4, that before the results of this course it was open whether some $\Delta^0_2$ set might have only high $\Delta^0_2$ subsets of itself or its complement. The theorem that every set has an infinite subset, of itself or of its complement, that is not high is due to Monin and Patey (2019); the same paper proves that every $\Delta^0_3$ set has an infinite low₃ subset of itself or of its complement, which is not proved in this course.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- R. Downey, D. R. Hirschfeldt, S. Lempp and R. Solomon, *A Δ⁰₂ set with no infinite low subset in either it or its complement*, Journal of Symbolic Logic 66 (2001), 1371–1381.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 2.1 and 6.4.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, sections *Context and motivation* and *Use first-jump control*.
