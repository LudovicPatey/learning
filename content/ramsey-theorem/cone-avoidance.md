---
title: Strong cone avoidance for the pigeonhole principle
summary: The forcing of Dzhafarov and Jockusch, with two sets built at once and a disjunctive question; strong cone avoidance for the infinite pigeonhole principle, for instances of any complexity.
duration: 25
prerequisites: [mathias-cohesiveness]
---

The previous lesson built, by Mathias forcing, cohesive sets that avoid a given cone, which is the first task of the decomposition of Ramsey's theorem for pairs. The second task is the harder one: an infinite subset of the limit set of a stable coloring, or of its complement, that does not compute $C$. The limit set is $\Delta^0_2$ relative to the cohesive set, and nothing better is known about it. We therefore prove cone avoidance for the infinite pigeonhole principle for **arbitrary** instances, whatever their complexity: this is **strong cone avoidance**. The proof is a Mathias forcing that builds two sets at once, with a forcing question of a new kind, the **disjunctive question**.

## The theorem of Dzhafarov and Jockusch

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

::::exercise{#ex-pigeonhole-one-side difficulty=1 objective="See why strong cone avoidance for the pigeonhole principle cannot prescribe the side of the solution."}
Show that there is an infinite set $A$ all of whose infinite subsets compute a given set $C$, and explain why this does not contradict :ref{#thm-dj-cone-avoidance}.

:::solution
Let $A = \{ \langle C \uh n \rangle : n \in \nat \}$, the set of codes of the prefixes of $C$, with a coding in which longer strings have larger codes. An infinite subset of $A$ contains codes of arbitrarily long prefixes of $C$, so it computes $C$: to find $C(x)$, search for an element coding a string of length larger than $x$. If $C$ is not computable, :ref{#thm-dj-cone-avoidance} with $Z = \emptyset$ gives an infinite subset of $A$ or of $\overline{A}$ that does not compute $C$; it cannot be a subset of $A$, so it is a subset of $\overline{A}$. There is no contradiction: the theorem only guarantees a solution on one of the two sides, without saying which.
:::
::::

## Notes and references

Cone avoidance for arbitrary problems, and the forcing question as the general method to establish it, are the subject of the course on cone avoidance (:ref{to="avoidance/avoidance-properties"}).

Strong cone avoidance for the pigeonhole principle is due to Dzhafarov and Jockusch (2009) (Hirschfeldt, Lemma 6.63, whose proof uses reservoirs that do not compute $C$ and the cone avoidance basis theorem instead of a Scott ideal; Dzhafarov–Mummert, Lemma 8.5.7). Our presentation with a Scott ideal follows the section *Infinite pigeonhole principle and cone avoidance* of Monin and Patey. The combination of two lists of requirements into disjunctions is called Lachlan's disjunction by Dzhafarov and Mummert (Lemma 8.3.7).

- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.

:::::exercises
::::exercise{#ex-dj-k-colors difficulty=1 objective="Extend strong cone avoidance for the pigeonhole principle to finitely many colors by induction."}
Let $Z$ be a set, $C \not\leq_T Z$, $k \geq 2$, and $\nat = A_0 \sqcup \cdots \sqcup A_{k-1}$ a partition. Show that some $A_i$ has an infinite subset $H$ with $C \not\leq_T Z \oplus H$.

:::solution
By induction on $k$, for all $Z$ simultaneously. For $k = 2$, this is :ref{#thm-dj-cone-avoidance} with $A = A_0$. For $k + 1$ parts, apply :ref{#thm-dj-cone-avoidance} to $A_0$: there is an infinite set $H$ with $C \not\leq_T Z \oplus H$, contained in $A_0$, in which case we are done, or in $A_1 \cup \cdots \cup A_k$. In the second case, let $p$ enumerate $H$ in increasing order and $B_i = \{ n : p(n) \in A_i \}$ for $1 \leq i \leq k$, a partition of $\nat$ into $k$ parts. By the induction hypothesis with $Z \oplus H$ in place of $Z$, some $B_i$ has an infinite subset $L$ with $C \not\leq_T Z \oplus H \oplus L$. Then $p[L]$ is an infinite subset of $A_i$, computable in $H \oplus L$, so $C \not\leq_T Z \oplus p[L]$. Adapted from Hirschfeldt, *Slicing the Truth*, Exercise 6.70.
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
