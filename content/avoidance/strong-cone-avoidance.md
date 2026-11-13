---
title: Strong cone avoidance
summary: Every set is Δ⁰₂ relative to some set avoiding a given cone, so that strong cone avoidance only needs to be checked on Δ⁰₂ instances; cohesiveness admits strong cone avoidance, with reservoirs that only avoid the cone.
duration: 40
prerequisites: [forcing-question-method, ramsey-theorem/cone-avoidance, turing-degrees/low-and-high]
---

Strong cone avoidance (:ref{#def-cone-avoidance-problem}) quantifies over arbitrary instances. Two difficulties follow. An arbitrary instance is not computable in the oracle $Z$, so the question of the previous lesson cannot read it; and the reservoirs of a Mathias-type construction can no longer be kept simple, since intersecting a reservoir with an arbitrary set produces an arbitrary set. This lesson treats both. The first part shows that the complexity of an instance is no obstacle as long as one only asks it to be a limit: every set is $\Delta^0_2$ relative to some set that avoids a given cone, and strong cone avoidance therefore reduces to $\Delta^0_2$ instances. The second part proves that cohesiveness admits strong cone avoidance, with reservoirs that are only required to avoid the cone, an essential use of the class $\mathcal M$ of :ref{#def-question-local}.

As in the previous lesson, a set $Z$ is fixed and the sentences are built with functionals of the oracle $Z \oplus G$.

## Every set is Δ⁰₂ relative to a cone-avoiding set

The construction of :ref{#thm-high-cone-avoidance} fixes the columns of a set one after the other to the values of $\emptyset''$, so that the set computes an approximation of $\emptyset''$ in the limit, and diagonalizes against the computations of $C$ in between. The same construction works for an arbitrary set in place of $\emptyset''$. We recast it as a notion of forcing with a forcing question, so that the diagonalization is :ref{#thm-local-cone-avoidance}.

:::theorem{#thm-delta2-cone-avoidance}
Let $Z$ be a set, $C$ a set with $C \not\leq_T Z$, and $A$ an arbitrary set. There is a set $G$ with $C \not\leq_T Z \oplus G$ and $A \leq_T G'$.
:::

:::proof{of=thm-delta2-cone-avoidance}
*The notion of forcing.* The conditions are the pairs $(\sigma, m)$ of a string and a number, with members
$$
[\sigma, m] = \{ X \succeq \sigma : X(\langle x, y \rangle) = A(x) \text{ for every } \langle x, y \rangle \geq |\sigma| \text{ with } x < m \},
$$
and $(\tau, n) \leq (\sigma, m)$ if $n \geq m$ and $[\tau, n] \subseteq [\sigma, m]$. The class $[\sigma, m]$ is closed and non-empty. Refinement holds: if a member $X$ of $(\sigma, m)$ extends a string $\rho$, then $(X \uh \max(|\sigma|, |\rho|), m)$ is an extension all of whose members extend $\rho$. So this is a notion of forcing (:ref{#def-forcing-notion}). For fixed $m$, the relation "$(\tau, m) \leq (\sigma, m)$" holds if and only if $\sigma \preceq \tau$ and $\tau(\langle x, y \rangle) = A(x)$ for the positions $|\sigma| \leq \langle x, y \rangle < |\tau|$ with $x < m$: it is decidable from the finite string $A \uh m$.

*The question.* For a $\Sigma^0_1$ sentence $\varphi = \Phi^{Z \oplus G}_e(\vec m)\converge$, let $(\sigma, m) \mathrel{?{\vdash}} \varphi$ if $\Phi^{Z \oplus \tau}_e(\vec m)\converge$ for some $\tau$ with $(\tau, m) \leq (\sigma, m)$. If so, every member of $(\tau, m)$ extends $\tau$ and satisfies $\varphi$, by the use principle. If not, $(\sigma, m)$ forces $\neg \varphi$: a member $X$ with $\Phi^{Z \oplus X}_e(\vec m)\converge$ with use $u$ would give $\tau = X \uh \max(u, |\sigma|)$ with $(\tau, m) \leq (\sigma, m)$ and a convergent computation. The relation is $\Sigma^0_1(Z)$, since the search over $\tau$ is decidable once $A \uh m$ is known. So the question is $\Sigma^0_1(\{ Z \})$-preserving.

*Conclusion.* By :ref{#thm-local-cone-avoidance} with $\mathcal M = \{ Z \}$, every sufficiently generic $G$ satisfies $C \not\leq_T Z \oplus G$. For each $k$, the set of conditions $(\sigma, m)$ with $m \geq k$ is dense, since $(\sigma, k)$ extends $(\sigma, m)$ when $k \geq m$. If $G$ is also generic for these sets, then for each $x$ the filter contains some $(\sigma, m)$ with $m > x$, and $G \in [\sigma, m]$, so $G(\langle x, y \rangle) = A(x)$ for all but finitely many $y$. The sets $G_y = \{ x : \langle x, y \rangle \in G \}$ form a $G$-computable approximation of $A$, so $A \leq_T G'$ by the limit lemma relativized to $G$ (:ref{#thm-limit-lemma}).
:::

The question does not mention $A$ beyond the finite string $A \uh m$, which is why its answers are $\Sigma^0_1(Z)$ although $A$ is arbitrary. Different conditions use different finite strings, so the question is $\Sigma^0_1(Z)$ for each condition, not uniformly in the condition; :ref{#def-question-local} asks for no more. The theorem says that the complexity of a set is no obstacle to cone avoidance as long as one only asks for the set to be a limit: every set is $\Delta^0_2$ relative to some set that avoids a given cone. This is the link between computational and combinatorial strength announced in the first lesson: an arbitrary instance can be replaced by an instance that is $\Delta^0_2$ relative to a harmless oracle.

:::corollary{#cor-strong-delta2}
A problem $\mathsf P$ admits strong cone avoidance if and only if for every set $Z$, every $C \not\leq_T Z$ and every instance $X$ of $\mathsf P$ with $X \leq_T Z'$, there is a solution $Y$ to $X$ with $C \not\leq_T Z \oplus Y$.
:::

:::proof{of=cor-strong-delta2}
The forward direction is a special case. Conversely, let $C \not\leq_T Z$ and let $X$ be any instance. By :ref{#thm-delta2-cone-avoidance} with $Z$ and the set $A = X$, there is $G$ with $C \not\leq_T Z \oplus G$ and $X \leq_T G' \leq_T (Z \oplus G)'$. The hypothesis, applied with $Z \oplus G$ in place of $Z$, gives a solution $Y$ with $C \not\leq_T Z \oplus G \oplus Y$, hence $C \not\leq_T Z \oplus Y$.
:::

The corollary is consistent with the table of :ref{#ex-cone-avoidance-problems}: the failure of strong cone avoidance for $\mathsf{RT}^2_2$ is witnessed by a coloring computable in $\emptyset'$, and the one for $\mathsf{WKL}$ by a tree computable in $C$, which is computable in $Z'$ for a suitable $Z$ with $C \not\leq_T Z$ by the theorem. In Seetapun's theorem (:ref{#thm-seetapun}), the pigeonhole principle is applied to the limit set of a stable coloring, a set that is $\Delta^0_2$ relative to the sets built so far. By the corollary, requiring the Dzhafarov–Jockusch theorem for such sets only is no weaker than requiring it for all sets.

:::quiz[every set is Δ⁰₂ relative to a cone-avoiding set]
Why is the question of :ref{#thm-delta2-cone-avoidance} $\Sigma^0_1(Z)$, although the members of the conditions are defined from the arbitrary set $A$?

- [x] Because the extensions $(\tau, m)$ with the same second component only depend on the finite string $A \uh m$, which can be built into the search.
- [ ] Because $A$ is computable in $Z$.

  $A$ is arbitrary.
- [ ] Because the question searches through all extensions $(\tau, n)$ with $n \geq m$.

  Extensions with larger $n$ would involve more of $A$; the question only uses those with the same $m$.
:::

## Strong cone avoidance of cohesiveness

The second part uses the class $\mathcal M$ of :ref{#def-question-local} in an essential way: the reservoirs are only required to avoid the cone, and their complexity is otherwise arbitrary. Recall that a set $G$ is cohesive for a sequence $\vec R = (R_n)$ if it is infinite and, for each $n$, $G \subseteq^* R_n$ or $G \subseteq^* \overline{R_n}$ (:ref{#def-cohesive}).

:::theorem[Wang]{#thm-coh-strong-cone}
$\mathsf{COH}$ admits strong cone avoidance: for every set $Z$, every $C \not\leq_T Z$ and every sequence of sets $\vec R$, there is an $\vec R$-cohesive set $G$ with $C \not\leq_T Z \oplus G$.
:::

:::proof{of=thm-coh-strong-cone}
*The notion of forcing.* The conditions are the Mathias conditions $(\sigma, X)$ (:ref{#def-mathias-condition}) such that $C \not\leq_T Z \oplus X$, with the order and members of :ref{#ex-forcing-notions}, item 4. Refinement holds as for computable Mathias forcing, since removing finitely many elements from a reservoir does not change its degree. Let $\mathcal M = \{ Z \oplus X : C \not\leq_T Z \oplus X \}$.

*The question.* For a $\Sigma^0_1$ sentence $\varphi$, let $(\sigma, X) \mathrel{?{\vdash}} \varphi$ if some string $\tau$ compatible with $(\sigma, X)$ satisfies $\varphi$, that is, makes the computation converge with oracle $Z \oplus \tau$. The proof of :ref{#prop-mathias-question} shows that this is a forcing question; it does not use the computability of $X$. Compatibility with $(\sigma, X)$ is decidable in $X$, so the relation is $\Sigma^0_1(Z \oplus X)$ with $Z \oplus X \in \mathcal M$. By :ref{#thm-local-cone-avoidance}, every sufficiently generic $G$ satisfies $C \not\leq_T Z \oplus G$.

*Cohesiveness.* Fix $n$ and a condition $(\sigma, X)$. Let $p$ be the enumeration of $X$ in increasing order, and $A = \{ k : p(k) \in R_n \}$. By the Dzhafarov–Jockusch theorem (:ref{#thm-dj-cone-avoidance}) relative to $Z \oplus X$, there is an infinite set $H$, contained in $A$ or in $\overline A$, with $C \not\leq_T Z \oplus X \oplus H$. The set $Y = p[H]$ is an infinite subset of $X$, contained in $R_n$ or in $\overline{R_n}$, and computable in $X \oplus H$; so $C \not\leq_T Z \oplus Y$, and $(\sigma, Y)$ is a condition extending $(\sigma, X)$. All its members $G$ satisfy $G \subseteq^* R_n$ or $G \subseteq^* \overline{R_n}$. So the set of conditions with this property is dense, for each $n$.

*Infinity.* Given $(\sigma, X)$ and $k$, adding to $\sigma$ an element of $X$ above $k$, and removing from $X$ the numbers up to it, gives an extension all of whose members have an element above $k$.

A set generic for all these dense sets is infinite, $\vec R$-cohesive, and does not compute $C$ together with $Z$.
:::

Strong cone avoidance of cohesiveness contrasts with :ref{#thm-coh-cone-avoidance}, where the sequence is computable in $Z$ and the reservoirs can be kept computable in $Z$. Here the sets $R_n$ are arbitrary, so their intersections with a reservoir are not simple, and the reservoirs are only required to satisfy the property that is being preserved. The step that shrinks a reservoir is an instance of the pigeonhole principle, applied to an arbitrary set: strong cone avoidance of $\mathsf{COH}$ is inherited from strong cone avoidance of $\mathsf{RT}^1_2$. This is the general pattern for Mathias-type notions: the reservoirs are taken in a class defined by the weakness property, and the operations on reservoirs must preserve that class.

:::quiz[strong cone avoidance of cohesiveness]
Why can the reservoir $X \cap R_n$, or $X \setminus R_n$, not be used directly as the new reservoir in the proof of :ref{#thm-coh-strong-cone}?

- [x] Because $R_n$ is arbitrary, so these sets may compute $C$ together with $Z$, and the new condition would not be a condition.
- [ ] Because neither of them is infinite.

  One of them is infinite.
- [ ] Because the question would no longer be a forcing question.

  The question is a forcing question for every Mathias condition; the issue is the class $\mathcal M$.
:::

## Exercises

::::exercise{difficulty=1}
Show that if $\mathsf P_0$ and $\mathsf P_1$ admit strong cone avoidance, so does $\mathsf P_0 \times \mathsf P_1$ (:ref{#prop-cone-avoidance-product}).

:::solution
Let $C \not\leq_T Z$ and let $X_0 \oplus X_1$ be any instance. Strong cone avoidance of $\mathsf P_0$ gives a solution $Y_0$ to $X_0$ with $C \not\leq_T Z \oplus Y_0$. Strong cone avoidance of $\mathsf P_1$ relative to $Z \oplus Y_0$ gives a solution $Y_1$ to $X_1$ with $C \not\leq_T Z \oplus Y_0 \oplus Y_1$. The proof is the one of :ref{#prop-cone-avoidance-product}, without the hypothesis that the instance is computable in $Z$.
:::
::::

::::exercise{difficulty=2}
Using :ref{#thm-local-cone-avoidance} and Mathias forcing, show that for every set $Z$, every $C \not\leq_T Z$ and every infinite set $A$ with $C \not\leq_T Z \oplus A$, there is an infinite set $G \subseteq A$ that is **high relative to $Z$**, that is, $(Z \oplus G)' \geq_T Z''$, and such that $C \not\leq_T Z \oplus G$.

:::solution
Use Mathias forcing with conditions $(\sigma, X)$ such that $X \subseteq A$, $X$ is infinite and $X \leq_T Z \oplus A$. The question of :ref{#prop-mathias-question}, with functionals of the oracle $Z \oplus G$, is a forcing question whatever the reservoir; it is $\Sigma^0_1(Z \oplus X)$, since compatibility with $(\sigma, X)$ is decidable in $X$, and $C \not\leq_T Z \oplus X$ since $Z \oplus X \leq_T Z \oplus A$; by :ref{#thm-local-cone-avoidance}, $C \not\leq_T Z \oplus G$ for every sufficiently generic $G$. Every condition's members $G$ satisfy $G \setminus \sigma \subseteq A$, and sufficiently generic sets are infinite, so $G \subseteq^* A$; replacing $G$ by $G \cap A$, a finite modification, keeps all properties. For highness, repeat the proof of :ref{#prop-mathias-dominant} with $Z$-computable functions $h$: the thinned reservoir is computable in $X \oplus Z$, hence in $Z \oplus A$. So the principal function of $G$ eventually dominates every $Z$-computable function, and $(Z \oplus G)' \geq_T Z''$ by Martin's theorem relativized to $Z$ (:ref{#thm-martin-domination}).
:::
::::

## Notes and references

:ref{#thm-delta2-cone-avoidance} is the theorem on high sets of :ref{to="turing-degrees/low-and-high"} for an arbitrary set, relativized; the monograph presents it in the section *First examples* of the chapter *Cone avoidance*, building directly the approximation by forcing. In the more general form where a closed class without $Z$-computable member is avoided, Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022, Lemma 2.8) attribute it to Patey. Strong cone avoidance of $\mathsf{COH}$ is due to Wang (2014); the proof through Mathias conditions whose reservoirs avoid the cone, using strong cone avoidance of the pigeonhole principle for the density of cohesiveness, follows an exercise of the same chapter (section *Seetapun's theorem*). The strong cone avoidance of the pigeonhole principle is due to Dzhafarov and Jockusch (2009).

- W. Wang, *Some logically weak Ramseyan theorems*, Advances in Mathematics 261 (2014), 1–25.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, sections *First examples* and *Seetapun's theorem*.
