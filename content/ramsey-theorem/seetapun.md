---
title: Seetapun's theorem
summary: Cone avoidance for cohesiveness by Mathias forcing; strong cone avoidance for the infinite pigeonhole principle by the forcing of Dzhafarov and Jockusch; Seetapun's theorem that every computable coloring of pairs has a homogeneous set not computing a given non-computable set; RT²₂ does not imply ACA₀.
duration: 45
prerequisites: [cohesiveness]
---

By Jockusch's bounds, some computable colorings of pairs have no homogeneous set computable in $\emptyset'$, while some computable coloring of triples forces all its infinite homogeneous sets to compute $\emptyset'$. Seetapun (1995) showed that pairs behave differently: for every non-computable set $C$, every computable coloring of pairs has an infinite homogeneous set that does not compute $C$. In particular, Ramsey's theorem for pairs does not imply $\mathsf{ACA}_0$. We follow the proof of Dzhafarov and Jockusch (2009), which goes through the decomposition of the previous lesson: cohesive sets can avoid cones, and the infinite pigeonhole principle avoids cones for **arbitrary** instances.

Throughout, a set is identified with its characteristic sequence, and a finite string $\sigma$ with the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$.

## Mathias forcing

:::definition{#def-mathias-condition}
A **Mathias condition** is a pair $(\sigma, X)$ with $\sigma$ a string and $X$ an infinite set with $\min X \geq |\sigma|$. A string $\tau$ is **compatible** with $(\sigma, X)$ if $\sigma \preceq \tau$ and every $n$ with $|\sigma| \leq n < |\tau|$ and $\tau(n) = 1$ belongs to $X$. A condition $(\tau, Y)$ **extends** $(\sigma, X)$ if $\tau$ is compatible with $(\sigma, X)$ and $Y \subseteq X$. A set $G$ **satisfies** $(\sigma, X)$ if every prefix of $G$ of length at least $|\sigma|$ is compatible with it, that is, $\sigma \prec G$ and $G \setminus \sigma \subseteq X$.
:::

The string $\sigma$ is the part of $G$ already decided, and the **reservoir** $X$ contains the elements that may still be added. A condition $(\tau, Y)$ extending $(\sigma, X)$ is satisfied only by sets satisfying $(\sigma, X)$.

## Cone avoidance for cohesiveness

:::theorem{#thm-coh-cone-avoidance}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable sequence $\vec R$ has a cohesive set $G$ with $C \not\leq_T Z \oplus G$.
:::

:::proof{of=thm-coh-cone-avoidance}
We build a sequence of Mathias conditions $(\sigma_0, X_0) \geq (\sigma_1, X_1) \geq \cdots$, with $(\sigma_0, X_0) = (\varepsilon, \nat)$ and **all reservoirs $Z$-computable**, and let $G = \bigcup_s \sigma_s$, assuming the strings grow unboundedly. Then $G$ satisfies every condition. The steps of the construction handle, in a fixed order, three kinds of tasks.

*Infinity.* Given $(\sigma, X)$, let $n = \min X$, and pass to $(\tau, X \setminus \{0, \dots, n\})$, where $\tau$ extends $\sigma$ by zeros up to position $n$, and $\tau(n) = 1$. The set $G$ then contains $n$.

*Cohesiveness for $R_i$.* One of $X \cap R_i$ and $X \setminus R_i$ is infinite; pass to $(\sigma, Y)$ with $Y$ that set, which is $Z$-computable. Then $G \setminus \sigma \subseteq Y$, so $G \subseteq^* R_i$ or $G \subseteq^* \overline{R_i}$.

*The requirement $\Phi^{Z \oplus G}_e \neq C$.* Given $(\sigma, X)$, consider the following cases.

1. There are $x$ and a string $\tau$ compatible with $(\sigma, X)$ with $\Phi^{Z \oplus \tau}_e(x)\converge \neq C(x)$. Pass to $(\tau, X \setminus \{0, \dots, |\tau|\})$. Every $G$ satisfying it has $\Phi^{Z \oplus G}_e(x) \neq C(x)$, by the use principle.
2. There is $x$ such that $\Phi^{Z \oplus \tau}_e(x)$ diverges for every $\tau$ compatible with $(\sigma, X)$. Keep $(\sigma, X)$. Every $G$ satisfying it has $\Phi^{Z \oplus G}_e(x)\diverge$: a convergent computation would converge with a prefix of $G$, which is compatible.
3. Otherwise, for every $x$ some compatible $\tau$ gives a convergent computation, and all such computations give $C(x)$. Then $C \leq_T Z$: given $x$, search, with $Z$ and the $Z$-computable set $X$, for a compatible $\tau$ with $\Phi^{Z \oplus \tau}_e(x)\converge$, and output its value. This case is excluded by hypothesis.

The resulting set $G$ is infinite, cohesive, and satisfies $\Phi^{Z \oplus G}_e \neq C$ for every $e$.
:::

The reservoirs must stay $Z$-computable for case 3 to give a reduction to $Z$. This is possible because the cohesiveness steps only intersect the reservoir with sets computable in $Z$.

:::quiz[cone avoidance for cohesiveness]
In the proof of :ref{#thm-coh-cone-avoidance}, why must the reservoirs be $Z$-computable?

- [x] Because in case 3, the search for compatible strings must be carried out with oracle $Z$, to conclude that $C \leq_T Z$, which contradicts the hypothesis.
- [ ] Because the cohesive set must be $Z$-computable.

  The cohesive set is not $Z$-computable in general; only the reservoirs are.
- [ ] Because Mathias conditions require computable reservoirs.

  The definition allows arbitrary infinite reservoirs; the restriction is chosen for this proof.

---

In case 2, why does keeping the condition unchanged suffice?

- [x] Because every set satisfying the condition has its prefixes compatible with it, so a convergent computation on such a set would give a compatible string with a convergent computation.
- [ ] Because $C$ is not computable.

  This hypothesis is used in case 3; case 2 holds for every $C$.
- [ ] Because the construction will later remove $x$ from the reservoir.

  The divergence is already forced; nothing further is needed.
:::

## Strong cone avoidance for the pigeonhole principle

The infinite pigeonhole principle for two colors asks, given a set $A$, for an infinite subset of $A$ or of $\overline{A}$. When $A$ is computable, $A$ or $\overline A$ itself is a computable solution. When $A$ is arbitrary, a solution may be forced to be complex: some infinite set $A$ has only infinite subsets computing a given set (see the exercises). The theorem of Dzhafarov and Jockusch says that the two sides cannot both be forced.

:::lemma{#lem-scott-cone}
For every set $Z$ and every $C \not\leq_T Z$, there is a Scott ideal containing $Z$ and not containing $C$.
:::

:::proof{of=lem-scott-cone}
Let $Z_0 = Z$, and $Z_{n+1} = Z_n \oplus P_n$ with $P_n$ PA relative to $Z_n$ and $C \not\leq_T Z_n \oplus P_n$, by the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $Z_n$. The ideal $\{ X : \exists n\ X \leq_T Z_n \}$ is a Scott ideal by :ref{#prop-wkl-scott}, as in :ref{#thm-low-scott}, and does not contain $C$.
:::

:::theorem[Dzhafarov, Jockusch]{#thm-dj-cone-avoidance}
Let $Z$ be a set and $C \not\leq_T Z$. For every set $A$, there is an infinite set $H$ with $H \subseteq A$ or $H \subseteq \overline{A}$, and $C \not\leq_T Z \oplus H$.
:::

:::proof{of=thm-dj-cone-avoidance}
Write $A^0 = A$ and $A^1 = \overline{A}$. Let $\mathcal I$ be a Scott ideal containing $Z$ and not $C$ (:ref{#lem-scott-cone}). If some infinite subset $H$ of $A^0$ or of $A^1$ belongs to $\mathcal I$, then $Z \oplus H \in \mathcal I$, so $C \not\leq_T Z \oplus H$, and we are done. Assume from now on:

(H) no infinite subset of $A^0$ or of $A^1$ belongs to $\mathcal I$.

We build two sets $G^0 \subseteq A^0$ and $G^1 \subseteq A^1$ simultaneously, with **conditions** $(\sigma_0, \sigma_1, X)$: $X \in \mathcal I$ is infinite with $\min X \geq |\sigma_0|, |\sigma_1|$, and the finite set $\sigma_i$ is contained in $A^i$, for $i < 2$. A condition $(\tau_0, \tau_1, Y)$ extends $(\sigma_0, \sigma_1, X)$ if each $(\tau_i, Y)$ extends $(\sigma_i, X)$ as Mathias conditions. The sets $G^i$ are the unions of the strings $\sigma_i$ along a sequence of conditions.

*Infinity.* Given a condition and $i < 2$, the set $X \cap A^i$ is infinite: otherwise $X$ minus finitely many elements would be an infinite subset of $A^{1-i}$ in $\mathcal I$, contradicting (H). Let $n \in X \cap A^i$, extend $\sigma_i$ by zeros and then $1$ at position $n$, and replace $X$ by $X \setminus \{0, \dots, n\}$.

*The requirement $\mathcal R_{e_0, e_1}$: $\Phi^{Z \oplus G^0}_{e_0} \neq C$ or $\Phi^{Z \oplus G^1}_{e_1} \neq C$.* Fix a condition $c = (\sigma_0, \sigma_1, X)$. For $x \in \nat$ and $v < 2$, say that $c$ **answers** $(x, v)$ if for every partition $\nat = U^0 \sqcup U^1$, there are $i < 2$ and a string $\tau$ compatible with $(\sigma_i, X \cap U^i)$ (compatibility is defined as for Mathias conditions, even if $X \cap U^i$ is finite) with $\Phi^{Z \oplus \tau}_{e_i}(x)\converge = v$.

The set of partitions, coded as $U^0$, for which this fails is a $\Pi^0_1(Z \oplus X)$ class: failure means that every $\tau$ compatible with $(\sigma_i, X \cap U^i)$, for both $i$, gives no convergent computation with value $v$, and each instance of this condition involves finitely many bits of $U^0$. By compactness, $c$ answers $(x, v)$ if and only if this class is empty, a $\Sigma^0_1(Z \oplus X)$ property of $(x, v)$. Let $W$ be the set of pairs answered by $c$; it is c.e. in $Z \oplus X$, which is a member of $\mathcal I$.

1. If $(x, 1 - C(x)) \in W$ for some $x$: apply the definition to the partition $(A^0, A^1)$. There are $i$ and $\tau$ compatible with $(\sigma_i, X \cap A^i)$ with $\Phi^{Z \oplus \tau}_{e_i}(x)\converge = 1 - C(x)$. The new elements of $\tau$ lie in $A^i$. Replacing $\sigma_i$ by $\tau$ and $X$ by $X \setminus \{0, \dots, |\tau|\}$ gives an extension forcing $\Phi^{Z \oplus G^i}_{e_i}(x) \neq C(x)$.
2. If $(x, C(x)) \notin W$ for some $x$: the $\Pi^0_1(Z \oplus X)$ class of partitions witnessing it is non-empty, and since $\mathcal I$ is a Scott ideal containing $Z \oplus X$, it has a member $U^0 \in \mathcal I$, with $U^1 = \overline{U^0}$. For some $i$, $X \cap U^i$ is infinite; it belongs to $\mathcal I$. The condition $(\sigma_0, \sigma_1, X \cap U^i)$ extends $c$, and every $G^i$ satisfying $(\sigma_i, X \cap U^i)$ has $\Phi^{Z \oplus G^i}_{e_i}(x) \neq C(x)$, divergent or different: a convergent computation with value $C(x)$ would come from a compatible string.
3. Otherwise, every $x$ has some $v$ with $(x, v) \in W$, and only $v = C(x)$ occurs. Then $C$ is computable in $Z \oplus X \in \mathcal I$, by enumerating $W$: so $C \in \mathcal I$, a contradiction.

*Conclusion.* Build a sequence of conditions that handles infinity for both sides and every requirement $\mathcal R_{e_0, e_1}$ in turn, and let $G^0$, $G^1$ be the limits. Both are infinite, $G^i \subseteq A^i$, and every requirement holds. If $\Phi^{Z \oplus G^0}_{e_0} = C$ for some $e_0$, then $\Phi^{Z \oplus G^1}_{e_1} \neq C$ for every $e_1$, so $C \not\leq_T Z \oplus G^1$. Otherwise $C \not\leq_T Z \oplus G^0$. Either $H = G^0$ or $H = G^1$ works.
:::

The heart of the proof is the **disjunctive question**: instead of asking whether some extension inside $A^i$ forces a convergence, which is too complex since $A$ is arbitrary, one asks whether every partition of $\nat$ allows a convergence on one side. A positive answer applies in particular to $(A^0, A^1)$; a negative answer is witnessed by a partition in the Scott ideal, and the reservoir is shrunk to a side of this partition. The new reservoir is thus a solution, in $\mathcal I$, of the instance $U^0$ of the pigeonhole principle, and (H) ensures that it still meets both $A^0$ and $A^1$ infinitely often.

:::quiz[the Dzhafarov–Jockusch forcing]
Why is the question "does every partition allow a convergence on one side" used, rather than "does some extension inside $A^i$ give a convergence"?

- [x] Because the second question involves the arbitrary set $A$ and has no useful bound on its complexity, whereas the first one is $\Sigma^0_1$ in $Z \oplus X$ by compactness, so case 3 yields $C \leq_T Z \oplus X$.
- [ ] Because $A$ may be finite.

  $A$ or its complement is infinite; the issue is the complexity of $A$.
- [ ] Because extensions inside $A^i$ do not exist.

  They exist by (H); the question is how to decide among them effectively.

---

Where is it used that $\mathcal I$ is a Scott ideal?

- [x] In case 2, to find a partition in $\mathcal I$ witnessing the negative answer, so that the new reservoir $X \cap U^i$ remains in $\mathcal I$.
- [ ] To ensure that $A$ belongs to $\mathcal I$.

  $A$ is arbitrary and usually not in $\mathcal I$.
- [ ] In case 1, to find the string $\tau$.

  In case 1, the string comes from the definition applied to $(A^0, A^1)$.
:::

## Seetapun's theorem

:::theorem[Seetapun]{#thm-seetapun}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$.
:::

:::proof{of=thm-seetapun}
The sequence $R_x = \{ y : f(\{ x, y \}) = 1 \}$ is $Z$-computable. By :ref{#thm-coh-cone-avoidance}, it has a cohesive set $G$ with $C \not\leq_T Z \oplus G$. Let $p$ enumerate $G$ in increasing order, and $g(\{ i, j \}) = f(\{ p(i), p(j) \})$; it is a stable coloring (:ref{#thm-rt22-decomposition}), computable in $Z \oplus G$. By :ref{#thm-dj-cone-avoidance} with $Z \oplus G$ in place of $Z$, applied to the limit set $A_g$, there is an infinite set $K$ contained in $A_g$ or in its complement with $C \not\leq_T Z \oplus G \oplus K$. By :ref{#prop-srt-d22} (2), $g \oplus K$ computes an infinite homogeneous set $L$ for $g$, and $H = p[L]$ is homogeneous for $f$, computable in $Z \oplus G \oplus K$. So $C \not\leq_T Z \oplus H$.
:::

:::corollary[Seetapun]{#cor-rt22-not-aca}
There is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ not containing $\emptyset'$. Consequently $\mathsf{RT}^2_2$ does not imply $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
:::

:::proof{of=cor-rt22-not-aca}
Build sets $Z_0 = \emptyset \leq_T Z_1 \leq_T \cdots$ with $\emptyset' \not\leq_T Z_n$. Fix an enumeration of all pairs $(e, m)$ in which each pair appears infinitely often. At stage $n$, take the next pair $(e, m)$ with $m \leq n$. If $\Phi^{Z_m}_e$ is a coloring of $[\nat]^2$ with two colors, it is $Z_n$-computable, and :ref{#thm-seetapun} gives an infinite homogeneous set $H$ with $\emptyset' \not\leq_T Z_n \oplus H$; let $Z_{n+1} = Z_n \oplus H$. Otherwise $Z_{n+1} = Z_n$.

The class $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$ is a Turing ideal not containing $\emptyset'$. Every coloring in $\mathcal I$ is $\Phi^{Z_m}_e$ for some $e, m$, and is handled at some stage, so it has a homogeneous set in $\mathcal I$. By absoluteness, $\mathcal I$ satisfies $\mathsf{RT}^2_2$, and it is not a jump ideal.
:::

Together with :ref{#cor-wkl-not-rt22}, Seetapun's theorem shows that $\mathsf{RT}^2_2$ escapes the Big Five: it lies strictly below $\mathsf{ACA}_0$ and is not provable in $\mathsf{WKL}_0$. Liu (2012) proved that it does not imply $\mathsf{WKL}_0$ either, by showing that the infinite pigeonhole principle avoids PA degrees in the sense of :ref{#thm-dj-cone-avoidance}; this is admitted here. Ramsey's theorem for pairs is the first and most studied of a large family of combinatorial principles, the **reverse mathematics zoo**, many of which lie strictly below $\mathsf{ACA}_0$ without being equivalent to any of the Big Five.

## Exercises

::::exercise{difficulty=1}
Show that there is an infinite set $A$ all of whose infinite subsets compute a given set $C$, and explain why this does not contradict :ref{#thm-dj-cone-avoidance}.

:::solution
Let $A = \{ \langle C \uh n \rangle : n \in \nat \}$, the set of codes of the prefixes of $C$, with a coding in which longer strings have larger codes. An infinite subset of $A$ contains codes of arbitrarily long prefixes of $C$, so it computes $C$: to find $C(x)$, search for an element coding a string of length larger than $x$. If $C$ is not computable, :ref{#thm-dj-cone-avoidance} with $Z = \emptyset$ gives an infinite subset of $A$ or of $\overline{A}$ that does not compute $C$; it cannot be a subset of $A$, so it is a subset of $\overline{A}$. There is no contradiction: the theorem only guarantees a solution on one of the two sides, without saying which.
:::
::::

::::exercise{difficulty=2}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{RT}^2_2$ not containing $\emptyset'$.

:::solution
Combine the constructions of :ref{#lem-scott-cone} and :ref{#cor-rt22-not-aca}: at even stages, add a set $P$ PA relative to $Z_n$ with $\emptyset' \not\leq_T Z_n \oplus P$, by the relativized cone avoidance basis theorem; at odd stages, handle the next coloring with :ref{#thm-seetapun}. The resulting Turing ideal is a Scott ideal, satisfies $\mathsf{RT}^2_2$, and does not contain $\emptyset'$.
:::
::::

## Notes and references

Seetapun's theorem appeared in Seetapun and Slaman (1995); the original proof is a direct forcing argument. The proof given here is due to Dzhafarov and Jockusch (2009), with the cohesiveness step of Cholak, Jockusch and Slaman (2001). Liu's theorem appeared in 2012. The surveys of Hirschfeldt and of Dzhafarov and Mummert describe the reverse mathematics zoo.

- D. Seetapun and T. A. Slaman, *On the strength of Ramsey's theorem*, Notre Dame Journal of Formal Logic 36 (1995), 570–582.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
