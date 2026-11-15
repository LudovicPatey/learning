---
title: Mathias forcing and cone avoidance
summary: Mathias conditions; every computable sequence has a cohesive set avoiding a given cone; the forcing of Dzhafarov and Jockusch, and strong cone avoidance for the infinite pigeonhole principle, for instances of any complexity.
duration: 50
prerequisites: [stable-colorings]
---

The decomposition of the previous lesson splits the search for a homogeneous set of a coloring of pairs into two tasks: a cohesive set for the rows of the coloring, and an infinite subset of the limit set of the resulting stable coloring, or of its complement. This lesson shows that both tasks can be carried out without computing a given non-computable set $C$. The tool is **Mathias forcing**, the main method for building solutions of combinatorial principles. The two results are combined into Seetapun's theorem in the next lesson.

The second task is the harder one. The limit set is $\Delta^0_2$ relative to the cohesive set, and nothing better is known about it. We therefore prove cone avoidance for the infinite pigeonhole principle for **arbitrary** instances, whatever their complexity: this is **strong cone avoidance**.

## Mathias forcing

To build a set with a property such as "not computing $C$", the course has used finite extensions (:ref{to="turing-degrees/finite-extensions"}): the set is approximated by strings, and each requirement is forced by a finite piece of information. A cohesive set cannot be built this way, since a finite string commits to nothing about the future elements of the set, and cohesiveness is a property of the tail of the set. **Mathias forcing** adds to the string an infinite commitment: a **reservoir** from which all future elements must be taken.

Throughout, a set is identified with its characteristic sequence, and a finite string $\sigma$ with the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$.

:::definition{#def-mathias-condition}
A **Mathias condition** is a pair $(\sigma, X)$ with $\sigma$ a string and $X$ an infinite set with $\min X \geq |\sigma|$. A string $\tau$ is **compatible** with $(\sigma, X)$ if $\sigma \preceq \tau$ and every $n$ with $|\sigma| \leq n < |\tau|$ and $\tau(n) = 1$ belongs to $X$. A condition $(\tau, Y)$ **extends** $(\sigma, X)$ if $\tau$ is compatible with $(\sigma, X)$ and $Y \subseteq X$. A set $G$ **satisfies** $(\sigma, X)$ if every prefix of $G$ of length at least $|\sigma|$ is compatible with it, that is, $\sigma \prec G$ and $G \setminus \sigma \subseteq X$.
:::

The string $\sigma$ is the part of $G$ already decided, and the reservoir $X$ contains the elements that may still be added. A condition $(\tau, Y)$ extending $(\sigma, X)$ is satisfied only by sets satisfying $(\sigma, X)$.

:::figure[A Mathias condition $(\sigma, X)$ with $\sigma = 010010$, so that $G$ contains $1$ and $4$ and no other number below $6$, and an extension $(\tau, Y)$. The string $\tau$ adds $9$ and $12$, both taken from the reservoir, and the new reservoir $Y$ is an infinite subset of $X$ above $|\tau|$.]
<svg class="fig" viewBox="0 0 600 196" width="600" role="img" aria-label="A Mathias condition: a finite string followed by a reservoir; an extension decides more bits, adding only elements of the reservoir, and shrinks the reservoir"><text x="71.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="115.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="159.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="203.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="247.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="291.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="335.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="379.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="423.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="467.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">18</text><text x="511.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">20</text><text x="555.0" y="20" text-anchor="middle" class="mrm muted" font-size="10">22</text><text x="50" y="45" text-anchor="end" class="label">(σ, X)</text><rect x="60" y="30" width="22" height="22" class="cell"/><text x="71.0" y="45" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="82" y="30" width="22" height="22" class="cell head-cell"/><text x="93.0" y="45" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="104" y="30" width="22" height="22" class="cell"/><text x="115.0" y="45" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="126" y="30" width="22" height="22" class="cell"/><text x="137.0" y="45" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="148" y="30" width="22" height="22" class="cell head-cell"/><text x="159.0" y="45" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="170" y="30" width="22" height="22" class="cell"/><text x="181.0" y="45" text-anchor="middle" class="mrm" font-size="12">0</text><circle cx="203.0" cy="41.0" r="2" class="muted-fill"/><circle cx="225.0" cy="41.0" r="5" class="accent-fill"/><circle cx="247.0" cy="41.0" r="2" class="muted-fill"/><circle cx="269.0" cy="41.0" r="5" class="accent-fill"/><circle cx="291.0" cy="41.0" r="2" class="muted-fill"/><circle cx="313.0" cy="41.0" r="2" class="muted-fill"/><circle cx="335.0" cy="41.0" r="5" class="accent-fill"/><circle cx="357.0" cy="41.0" r="5" class="accent-fill"/><circle cx="379.0" cy="41.0" r="2" class="muted-fill"/><circle cx="401.0" cy="41.0" r="2" class="muted-fill"/><circle cx="423.0" cy="41.0" r="5" class="accent-fill"/><circle cx="445.0" cy="41.0" r="2" class="muted-fill"/><circle cx="467.0" cy="41.0" r="5" class="accent-fill"/><circle cx="489.0" cy="41.0" r="2" class="muted-fill"/><circle cx="511.0" cy="41.0" r="2" class="muted-fill"/><circle cx="533.0" cy="41.0" r="5" class="accent-fill"/><circle cx="555.0" cy="41.0" r="2" class="muted-fill"/><text x="572" y="45" class="mrm muted" font-size="14">⋯</text><text x="50" y="115" text-anchor="end" class="label">(τ, Y)</text><rect x="60" y="100" width="22" height="22" class="cell"/><text x="71.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="82" y="100" width="22" height="22" class="cell head-cell"/><text x="93.0" y="115" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="104" y="100" width="22" height="22" class="cell"/><text x="115.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="126" y="100" width="22" height="22" class="cell"/><text x="137.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="148" y="100" width="22" height="22" class="cell head-cell"/><text x="159.0" y="115" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="170" y="100" width="22" height="22" class="cell"/><text x="181.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="192" y="100" width="22" height="22" class="cell"/><text x="203.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="214" y="100" width="22" height="22" class="cell"/><text x="225.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="236" y="100" width="22" height="22" class="cell"/><text x="247.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="258" y="100" width="22" height="22" class="cell head-cell"/><text x="269.0" y="115" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="280" y="100" width="22" height="22" class="cell"/><text x="291.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="302" y="100" width="22" height="22" class="cell"/><text x="313.0" y="115" text-anchor="middle" class="mrm" font-size="12">0</text><rect x="324" y="100" width="22" height="22" class="cell head-cell"/><text x="335.0" y="115" text-anchor="middle" class="mrm" font-size="12">1</text><circle cx="357.0" cy="111.0" r="2" class="muted-fill"/><circle cx="379.0" cy="111.0" r="2" class="muted-fill"/><circle cx="401.0" cy="111.0" r="2" class="muted-fill"/><circle cx="423.0" cy="111.0" r="5" class="accent-fill"/><circle cx="445.0" cy="111.0" r="2" class="muted-fill"/><circle cx="467.0" cy="111.0" r="2" class="muted-fill"/><circle cx="489.0" cy="111.0" r="2" class="muted-fill"/><circle cx="511.0" cy="111.0" r="2" class="muted-fill"/><circle cx="533.0" cy="111.0" r="5" class="accent-fill"/><circle cx="555.0" cy="111.0" r="2" class="muted-fill"/><text x="572" y="115" class="mrm muted" font-size="14">⋯</text><line x1="269.0" y1="58" x2="269.0" y2="96" class="accent-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="335.0" y1="58" x2="335.0" y2="96" class="accent-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><rect x="60" y="150" width="14" height="14" class="cell head-cell"/><text x="80" y="162" class="label">elements of the finite part</text><circle cx="297" cy="157" r="5" class="accent-fill"/><text x="308" y="162" class="label">elements of the reservoir</text><text x="60" y="186" class="label">τ adds 9 and 12, both taken from X; the new reservoir Y is a subset of X above |τ| = 13</text></svg>
:::

:::example{#ex-mathias-coh}
For every set $R$ and every condition $(\sigma, X)$, one of $X \cap R$ and $X \setminus R$ is infinite, and $(\sigma, X \cap R)$ or $(\sigma, X \setminus R)$ is an extension. Every set $G$ satisfying it has $G \setminus \sigma$ contained in $R$ or in $\overline R$, so $G \subseteq^* R$ or $G \subseteq^* \overline R$. Shrinking the reservoir thus forces cohesiveness for one set at a time, by a single extension. With finite extensions alone, no condition forces $G \subseteq^* R$ for an infinite and coinfinite $R$.
:::

## Cone avoidance for cohesiveness

The cone avoidance theorem for finite extensions (:ref{#thm-cone-avoidance}) has a Mathias analogue. In the Cohen case, the decisive point was that, if no extension forces $\Phi^G_e \neq C$, then $C$ is computable, by a search through the extensions of a string. In the Mathias case the search runs through the strings compatible with a condition, and is effective only if the reservoir is: the reservoirs must therefore stay simple.

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

The reservoirs must stay $Z$-computable for case 3 to give a reduction to $Z$. This is possible because the cohesiveness steps only intersect the reservoir with sets computable in $Z$. The construction is not effective (the case distinction and the choice of the infinite side are not computable in $Z$), and it need not be: only the reservoirs must be simple, not the sequence of conditions.

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

::::exercise{#ex-coh-countable-cones difficulty=2 objective="Adapt Mathias cone avoidance to countably many cones at once."}
Let $Z$ be a set and $C_0, C_1, \dots$ sets with $C_j \not\leq_T Z$ for every $j$. Show that every $Z$-computable sequence $\vec R$ has a cohesive set $G$ with $C_j \not\leq_T Z \oplus G$ for every $j$.

:::solution
Run the construction of :ref{#thm-coh-cone-avoidance} with one requirement $\Phi^{Z \oplus G}_e \neq C_j$ for each pair $(e, j)$, handled in a fixed order together with the infinity and cohesiveness steps. Each requirement is satisfied as before: cases 1 and 2 extend or keep the condition, and case 3 would give $C_j \leq_T Z$. The reservoirs stay $Z$-computable throughout, since the hypothesis on $C_j$ is used only in case 3, for the current reservoir.
:::
::::

## Strong cone avoidance for the pigeonhole principle

The infinite pigeonhole principle for two colors asks, given a set $A$, for an infinite subset of $A$ or of $\overline{A}$. When $A$ is computable, $A$ or $\overline A$ itself is a computable solution. When $A$ is arbitrary, a solution may be forced to be complex: some infinite set $A$ has only infinite subsets computing a given set (:ref{#ex-pigeonhole-one-side}). The theorem of Dzhafarov and Jockusch says that the two sides cannot both be forced.

The proof builds a subset of $A$ and a subset of $\overline{A}$ at the same time, by Mathias forcing with a common reservoir, and satisfies, for every pair of indices $(e_0, e_1)$, the **disjunction** "$\Phi_{e_0}$ fails to compute $C$ from the first set, or $\Phi_{e_1}$ fails from the second". If every disjunction holds, one of the two sets avoids the cone: if the first set computes $C$ through some $e_0$, then every $e_1$ fails on the second set. This way of combining two lists of requirements is sometimes called **Lachlan's disjunction**. The obstacle is that $A$ may be arbitrarily complex, so a question about extensions inside $A$ cannot be answered with a simple oracle. The solution is to ask the question about **all** partitions of $\nat$ simultaneously, which removes $A$ from the question and makes it a $\Pi^0_1$ question, answered by compactness.

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

The heart of the proof is the **disjunctive question**: instead of asking whether some extension inside $A^i$ forces a convergence, which is too complex since $A$ is arbitrary, one asks whether every partition of $\nat$ allows a convergence on one side. A positive answer applies in particular to $(A^0, A^1)$; a negative answer is witnessed by a partition in the Scott ideal, and the reservoir is shrunk to a side of this partition. The new reservoir is thus a solution, in $\mathcal I$, of the instance $U^0$ of the pigeonhole principle, and (H) ensures that it still meets both $A^0$ and $A^1$ infinitely often. The Scott ideal plays the role that the $Z$-computable reservoirs played for cohesiveness: a class of simple sets, closed under the operations of the construction, in which case 3 yields a contradiction.

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

## Notes and references

Cone avoidance for arbitrary problems, and the forcing question as the general method to establish it, are the subject of the course on cone avoidance (:ref{to="avoidance/avoidance-properties"}).

Mathias forcing is studied as a notion of forcing in the course on effective forcing, where cone avoidance for cohesive sets is derived from a forcing question (:ref{#prop-mathias-question}, :ref{#thm-mathias-coh-preservation}), and where it is shown that no such question can preserve Σ⁰₂ properties (:ref{#cor-mathias-no-sigma2}).

Mathias forcing was introduced by Mathias in set theory; its computable version is presented by Hirschfeldt (§6.5, Definition 6.40 and Proposition 6.41) and by Dzhafarov and Mummert (Examples 7.2.5, 7.2.10 and 7.3.9). Cone avoidance for cohesiveness is attributed to Cholak, Jockusch and Slaman (2001) by Dzhafarov and Mummert (Lemma 8.5.6), and to Jockusch and Stephan (1993) by Hirschfeldt (Exercise 6.62). Strong cone avoidance for the pigeonhole principle is due to Dzhafarov and Jockusch (2009) (Hirschfeldt, Lemma 6.63, whose proof uses reservoirs that do not compute $C$ and the cone avoidance basis theorem instead of a Scott ideal; Dzhafarov–Mummert, Lemma 8.5.7). Our presentation with a Scott ideal follows the section *Infinite pigeonhole principle and cone avoidance* of Monin and Patey. The combination of two lists of requirements into disjunctions is called Lachlan's disjunction by Dzhafarov and Mummert (Lemma 8.3.7).

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.

:::::exercises
::::exercise{#ex-pigeonhole-one-side difficulty=1 objective="See why strong cone avoidance for the pigeonhole principle cannot prescribe the side of the solution."}
Show that there is an infinite set $A$ all of whose infinite subsets compute a given set $C$, and explain why this does not contradict :ref{#thm-dj-cone-avoidance}.

:::solution
Let $A = \{ \langle C \uh n \rangle : n \in \nat \}$, the set of codes of the prefixes of $C$, with a coding in which longer strings have larger codes. An infinite subset of $A$ contains codes of arbitrarily long prefixes of $C$, so it computes $C$: to find $C(x)$, search for an element coding a string of length larger than $x$. If $C$ is not computable, :ref{#thm-dj-cone-avoidance} with $Z = \emptyset$ gives an infinite subset of $A$ or of $\overline{A}$ that does not compute $C$; it cannot be a subset of $A$, so it is a subset of $\overline{A}$. There is no contradiction: the theorem only guarantees a solution on one of the two sides, without saying which.
:::
::::

::::exercise{#ex-mathias-extension difficulty=1 objective="Check the basic properties of Mathias conditions from the definition."}
1. Show that extension of Mathias conditions is transitive, and that if $(\tau, Y)$ extends $(\sigma, X)$, every set satisfying $(\tau, Y)$ satisfies $(\sigma, X)$.
2. Show that the class of sets satisfying $(\sigma, X)$ is a $\Pi^0_1(X)$ class with an infinite member.

:::solution
1. Let $(\rho, W)$ extend $(\tau, Y)$, which extends $(\sigma, X)$. Then $\sigma \preceq \tau \preceq \rho$ and $W \subseteq Y \subseteq X$. A position $n$ with $|\sigma| \leq n < |\rho|$ and $\rho(n) = 1$ is either below $|\tau|$, and then $\tau(n) = 1$ and $n \in X$, or at least $|\tau|$, and then $n \in Y \subseteq X$. So $\rho$ is compatible with $(\sigma, X)$. For the second statement, let $G$ satisfy $(\tau, Y)$. Then $\sigma \preceq \tau \prec G$, and every $n \geq |\sigma|$ in $G$ is a new element of $\tau$, hence in $X$, if $n < |\tau|$, and belongs to $Y \subseteq X$ otherwise.
2. The class is $\{ G : \sigma \prec G \text{ and } \forall n \geq |\sigma|\ (n \in G \rightarrow n \in X) \}$, an intersection of conditions each involving one bit of $G$ and decidable from $X$: a $\Pi^0_1(X)$ class. The set $\sigma \cup X$, that is, the set whose characteristic sequence extends $\sigma$ and coincides with $X$ above $|\sigma|$, is an infinite member, since $\min X \geq |\sigma|$.
:::
::::

::::exercise{#ex-dj-k-colors difficulty=1 objective="Extend strong cone avoidance for the pigeonhole principle to finitely many colors by induction."}
Let $Z$ be a set, $C \not\leq_T Z$, $k \geq 2$, and $\nat = A_0 \sqcup \cdots \sqcup A_{k-1}$ a partition. Show that some $A_i$ has an infinite subset $H$ with $C \not\leq_T Z \oplus H$.

:::solution
By induction on $k$, for all $Z$ simultaneously. For $k = 2$, this is :ref{#thm-dj-cone-avoidance} with $A = A_0$. For $k + 1$ parts, apply :ref{#thm-dj-cone-avoidance} to $A_0$: there is an infinite set $H$ with $C \not\leq_T Z \oplus H$, contained in $A_0$, in which case we are done, or in $A_1 \cup \cdots \cup A_k$. In the second case, let $p$ enumerate $H$ in increasing order and $B_i = \{ n : p(n) \in A_i \}$ for $1 \leq i \leq k$, a partition of $\nat$ into $k$ parts. By the induction hypothesis with $Z \oplus H$ in place of $Z$, some $B_i$ has an infinite subset $L$ with $C \not\leq_T Z \oplus H \oplus L$. Then $p[L]$ is an infinite subset of $A_i$, computable in $H \oplus L$, so $C \not\leq_T Z \oplus p[L]$. Adapted from Hirschfeldt, *Slicing the Truth*, Exercise 6.70.
:::
::::

::::exercise{#ex-coh-omega-model difficulty=2 objective="Iterate cone avoidance for cohesiveness to build an ω-model of COH without the halting set."}
Show directly from :ref{#thm-coh-cone-avoidance} that there is an ω-model of $\mathsf{RCA}_0 + \mathsf{COH}$ not containing $\emptyset'$.

:::solution
Identify a sequence of sets $\vec R$ with the set $\{ \langle i, x \rangle : x \in R_i \}$. Fix an enumeration of all pairs $(e, m)$ in which each pair appears infinitely often. Build sets $Z_0 = \emptyset \leq_T Z_1 \leq_T \cdots$ with $\emptyset' \not\leq_T Z_n$. At stage $n$, let $(e, m)$ be the $n$-th pair. If $m \leq n$ and $\Phi^{Z_m}_e$ is the characteristic function of a set, it codes a $Z_n$-computable sequence $\vec R$, and :ref{#thm-coh-cone-avoidance} with $Z = Z_n$ and $C = \emptyset'$ gives an $\vec R$-cohesive set $G$ with $\emptyset' \not\leq_T Z_n \oplus G$; let $Z_{n+1} = Z_n \oplus G$. Otherwise $Z_{n+1} = Z_n$.

The class $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$ is a Turing ideal, since the sequence is increasing, and does not contain $\emptyset'$. Every sequence in $\mathcal I$ is $\Phi^{Z_m}_e$ for some $e$ and $m$, and the pair $(e, m)$ is the $n$-th pair for some $n \geq m$, so the sequence has a cohesive set in $\mathcal I$. Cohesiveness is arithmetical, so $\mathcal I$ satisfies $\mathsf{COH}$, and as a Turing ideal it is an ω-model of $\mathsf{RCA}_0$.
:::
::::

::::exercise{#ex-lachlan-disjunction difficulty=1 objective="Check that the disjunctive requirements express exactly that one of two sets avoids the cone."}
Let $Z$, $C$, $G^0$ and $G^1$ be sets. Show that the requirements $\mathcal R_{e_0, e_1}$ of the proof of :ref{#thm-dj-cone-avoidance} hold for all $e_0, e_1$ if and only if $C \not\leq_T Z \oplus G^0$ or $C \not\leq_T Z \oplus G^1$.

:::solution
If $C \not\leq_T Z \oplus G^0$, then $\Phi^{Z \oplus G^0}_{e_0} \neq C$ for every $e_0$, so every requirement holds; similarly if $C \not\leq_T Z \oplus G^1$. Conversely, if $C = \Phi^{Z \oplus G^0}_{e_0}$ and $C = \Phi^{Z \oplus G^1}_{e_1}$, the requirement $\mathcal R_{e_0, e_1}$ fails. So the disjunctions are exactly as strong as the conclusion of the theorem, while each one concerns a single pair of indices and can be satisfied by a single extension.
:::
::::

::::exercise{#ex-dj-answer-sigma1 difficulty=2 objective="Complete the compactness step of the disjunctive question of Dzhafarov and Jockusch."}
In the proof of :ref{#thm-dj-cone-avoidance}, let $c = (\sigma_0, \sigma_1, X)$ be a condition. Show that the class of sets $U^0$ for which the partition $(U^0, \overline{U^0})$ witnesses that $c$ does not answer $(x, v)$ is a $\Pi^0_1(Z \oplus X)$ class, uniformly in $(x, v)$, and deduce that the set $W$ of pairs answered by $c$ is c.e. in $Z \oplus X$.

:::solution
For a string $\rho$, viewed as an initial segment of $U^0$, say that $\rho$ is **bad** if there are $i < 2$ and a string $\tau$ with $|\tau| \leq |\rho|$ such that $\sigma_i \preceq \tau$, every $n$ with $|\sigma_i| \leq n < |\tau|$ and $\tau(n) = 1$ belongs to $X$ and satisfies $\rho(n) = 1 - i$ (that is, $n \in U^i$), and $\Phi^{Z \oplus \tau}_{e_i}(x)$ converges to $v$ in at most $|\rho|$ steps. Being bad is decidable in $Z \oplus X$, uniformly in $(\rho, x, v)$: the search is bounded, and a bounded computation queries finitely many bits of $Z$. Badness is preserved by extension of $\rho$. A set $U^0$ has a bad prefix if and only if there are $i$ and $\tau$ compatible with $(\sigma_i, X \cap U^i)$ with $\Phi^{Z \oplus \tau}_{e_i}(x)\converge = v$: compatibility depends only on $U^i \uh |\tau|$, and a convergent computation converges in finitely many steps. So the class of partitions witnessing a negative answer is the class of paths of the $Z \oplus X$-computable tree of strings without bad prefix, a $\Pi^0_1(Z \oplus X)$ class.

By compactness (König's lemma for binary trees), this class is empty if and only if the tree is finite, that is, if and only if there is a length $\ell$ such that every string of length $\ell$ has a bad prefix. This is a $\Sigma^0_1(Z \oplus X)$ property of $(x, v)$, so $W$ is c.e. in $Z \oplus X$.
:::
::::
:::::
