---
title: Stable linear orders
summary: In a computable stable linear order, the elements with finitely many predecessors form a Δ⁰₂ set whose complement is hyperimmune unless a computable solution exists; so every computable stable linear order has a low ascending or descending sequence (Hirschfeldt–Shore).
duration: 20
prerequisites: [weak-preservation, low-bases]
---

This lesson applies :ref{#thm-cohyperimmune-low} to a combinatorial problem, the ascending–descending sequence principle for stable linear orders. The problem itself says nothing about hyperimmunity. The hypothesis appears through a case distinction: either the order has a computable solution, or the two natural halves of the order are immune, and then, by the structure of stable orders, hyperimmune. In the second case, Jockusch's theorem applies to one half. The resulting low basis separates the problem from cohesiveness and from Ramsey's theorem for pairs.

## Ascending and descending sequences

A linear order $\mathcal L = (\nat, <_{\mathcal L})$ is **stable** if every element has finitely many $<_{\mathcal L}$-predecessors or finitely many $<_{\mathcal L}$-successors. Let $A$ be the set of elements with finitely many predecessors, and $A^*$ the set of elements with finitely many successors. An **ascending sequence** is an infinite set on which $<_{\mathcal L}$ agrees with the natural order, and a **descending sequence** an infinite set on which it agrees with the reverse order. $\mathsf{SADS}$ is the problem whose instances are stable linear orders and whose solutions are their ascending and descending sequences.

:::proposition{#prop-stable-order-parts}
Let $\mathcal L$ be a computable stable linear order.
1. $\nat = A \sqcup A^*$, every element of $A$ is $<_{\mathcal L}$-below every element of $A^*$, and $A$ and $A^*$ are $\Delta^0_2$.
2. Every infinite subset $H$ of $A$ computes an ascending sequence contained in $H$, and every infinite subset of $A^*$ computes a descending sequence.
3. If $A^*$ is infinite and immune, it is hyperimmune; the same holds for $A$.
:::

:::proof{of=prop-stable-order-parts}
1. An element has finitely many predecessors or finitely many successors, by stability, and not both, since $\nat$ is infinite. If $x \in A$ and $y \in A^*$ with $y <_{\mathcal L} x$, the infinitely many predecessors of $y$ would be predecessors of $x$; so $x <_{\mathcal L} y$. The relation "$x$ has finitely many predecessors" is $\Sigma^0_2$, as is "$x$ has finitely many successors"; each of $A$ and $A^*$ is $\Sigma^0_2$ with $\Sigma^0_2$ complement, hence $\Delta^0_2$.
2. Let $h_0$ be the least element of $H$, and $h_{k+1}$ the least element of $H$ larger than $h_k$ in both orders. It exists: $h_k \in A$ has finitely many predecessors, so all but finitely many elements of the infinite set $H$ are $<_{\mathcal L}$-above it. The sequence is $H$-computable. The case of $A^*$ is symmetric.
3. Let $(F_n)$ be a disjoint strong array each of whose members meets $A^*$. Let $m_n$ be the $<_{\mathcal L}$-largest element of $F_n$; it is $<_{\mathcal L}$-above an element of $A^*$, so it belongs to $A^*$ by item 1. The function $n \mapsto m_n$ is computable and injective, since the sets $F_n$ are disjoint, so its range is an infinite c.e. subset of $A^*$, and $A^*$ is not immune. For $A$, take the $<_{\mathcal L}$-smallest elements.
:::

:::theorem[Hirschfeldt, Shore]{#thm-sads-low}
Every computable stable linear order has a low ascending or descending sequence. Consequently $\mathsf{SADS}$ admits a low basis.
:::

:::proof{of=thm-sads-low}
Let $\mathcal L$ be a computable stable linear order. If $A$ has an infinite c.e. subset, it has an infinite computable subset (see :ref{#def-immune}), which computes an ascending sequence by item 2 of :ref{#prop-stable-order-parts}; this sequence is computable, hence low. The same holds if $A^*$ has an infinite c.e. subset. Otherwise neither $A$ nor $A^*$ has an infinite c.e. subset. Neither is finite, since the other one would then be cofinite; so both are immune. By item 3, $A^*$ is hyperimmune. The set $A$ is $\Delta^0_2$, hence $\Sigma^0_2$, with hyperimmune complement $A^*$; by :ref{#thm-cohyperimmune-low}, it has an infinite low subset $H$, which computes an ascending sequence, low since it is computable in $H$. The proof relativizes to every set $Z$ and every $Z$-computable stable order, with $(Z \oplus H)' \leq_T Z'$, which gives the low basis.
:::

The theorem is sharp in two directions. Tennenbaum and Denisov built a computable linear order of type $\omega + \omega^*$, which is stable, with no computable ascending or descending sequence (Hirschfeldt, Theorem 9.11 and Exercise 9.12), so the solutions cannot be made computable. And for the problem $\mathsf{ADS}$, in which the order need not be stable, Hirschfeldt and Shore showed that some computable linear order has no low ascending or descending sequence (Hirschfeldt, Exercise 9.6, through Herrmann's partial order). By :ref{#cor-low-basis-separations} and :ref{#thm-sads-low}, $\mathsf{SADS}$ implies neither $\mathsf{COH}$ nor $\mathsf{RT}^2_2$ in ω-models, and $\mathsf{WKL}_0 + \mathsf{SADS}$ has an ω-model of low sets (:ref{#ex-wkl-sads-low-model}).

:::quiz[stable linear orders]
In item 3 of :ref{#prop-stable-order-parts}, why is the $<_{\mathcal L}$-largest element of $F_n$ in $A^*$?

- [x] Because $F_n$ contains an element of $A^*$, the largest element is above it, and $A^*$ is closed upward in $<_{\mathcal L}$ by item 1.
- [ ] Because $F_n$ is contained in $A^*$.

  $F_n$ only meets $A^*$; it may contain elements of $A$.
- [ ] Because the sets $F_n$ are disjoint.

  Disjointness makes the elements $m_n$ distinct; it does not place them in $A^*$.
:::

## Exercises

::::exercise{#ex-sads-solutions difficulty=1 objective="Identify the solutions of a stable linear order with the infinite subsets of its two halves."}
Let $\mathcal L$ be a computable stable linear order, with $A$ and $A^*$ as above. Show that every ascending sequence is contained in $A$, and every descending sequence in $A^*$. Deduce that the solutions of $\mathsf{SADS}$ for $\mathcal L$ are, up to Turing equivalence, the infinite subsets of $A$ and of $A^*$.

:::solution
Let $H$ be an ascending sequence and $h \in H$. The elements of $H$ larger than $h$ are infinitely many, and they are $<_{\mathcal L}$-above $h$; so $h$ has infinitely many successors, and $h \notin A^*$, that is, $h \in A$. The case of descending sequences is symmetric. So every solution is an infinite subset of $A$ or of $A^*$; conversely, by item 2 of :ref{#prop-stable-order-parts}, every infinite subset of $A$ or of $A^*$ computes a solution contained in it.
:::
::::

::::exercise{#ex-wkl-sads-low-model difficulty=1 objective="Combine the low bases of two problems into an ω-model of low sets satisfying both."}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{SADS}$ consisting of low sets.

:::solution
Let $\mathsf P$ be the problem whose instances are pairs $T \oplus \mathcal L$ of an infinite binary tree and a stable linear order, with solutions $X \oplus H$ of a path of $T$ and a solution for $\mathcal L$. It admits a low basis: given a set $Z$ computing $T \oplus \mathcal L$, the low basis theorem relativized to $Z$ gives a path $X$ with $(Z \oplus X)' \leq_T Z'$, and :ref{#thm-sads-low} relativized to $Z \oplus X$ gives a solution $H$ with $(Z \oplus X \oplus H)' \leq_T (Z \oplus X)' \leq_T Z'$. By :ref{#thm-low-basis-model} with $Z = \emptyset$, there is a Turing ideal of low sets satisfying $\mathsf P$. It satisfies $\mathsf{WKL}$ and $\mathsf{SADS}$, since every tree and every stable order of the ideal is a component of an instance of $\mathsf P$ in the ideal, paired with a fixed computable instance of the other problem.
:::
::::

## Notes and references

:ref{#thm-sads-low} is due to Hirschfeldt and Shore (2007). Hirschfeldt presents it as Theorem 9.19, for linear orders of type $\omega + \omega^*$, with a direct proof by forcing in Exercise 9.20; the derivation from Jockusch's theorem follows the section *Weak preservation* of the chapter *Lowness* of Patey's monograph, where it is an exercise. Dzhafarov and Mummert state that $\mathsf{SADS}$ admits low solutions as a consequence of their Theorem 9.2.19 on the stable chain–antichain principle. Hirschfeldt and Shore also proved that some computable linear order has no low ascending or descending sequence (Hirschfeldt, Exercise 9.6), through the partial order of Herrmann (2001).

- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- E. Herrmann, *Infinite chains and antichains in computable partial orderings*, Journal of Symbolic Logic 66 (2001), 923–934.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 9.1.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 9.2.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, section *Weak preservation*.

:::::exercises
::::exercise{#ex-stable-order-types difficulty=1 objective="Characterize stable linear orders by their order types, and recognize stability on examples."}
1. Show that a linear order on $\nat$ is stable if and only if its order type is $\omega + m$, $n + \omega^*$ or $\omega + \omega^*$, for some finite $n$ and $m$.
2. Let $x <_{\mathcal L} y$ hold if $x$ is even and $y$ odd, or $x$ and $y$ have the same parity and $x < y$. Is $\mathcal L$ stable? Same question when, for two odd numbers, $x <_{\mathcal L} y$ if $x > y$. Give $A$ and $A^*$ when the order is stable.

:::solution
1. Let $\mathcal L$ be stable. If $y <_{\mathcal L} x \in A$, the predecessors of $y$ are predecessors of $x$, so $y \in A$: $A$ is an initial segment, and by item 1 of :ref{#prop-stable-order-parts}, $\mathcal L$ is $A$ followed by $A^*$. If $x <_{\mathcal L} y$ are in $A$, the predecessors of $y$ include those of $x$ and $x$ itself; so the map sending $x \in A$ to its number of predecessors is injective, and its range is downward closed, since the predecessors of an element with $k$ predecessors have $0, \dots, k - 1$ predecessors. So $A$ has type $\omega$ if it is infinite, and a finite type otherwise; symmetrically, $A^*$ has type $\omega^*$ or a finite type. Since $\nat$ is infinite, one of them is infinite, and the type is one of the three listed. Conversely, in each of these types, the elements of the $\omega$ part and of a finite final part have finitely many predecessors, and those of the $\omega^*$ part and of a finite initial part have finitely many successors.
2. The first order has type $\omega + \omega$. An odd number has infinitely many predecessors, the even numbers, and infinitely many successors, the larger odd numbers: the order is not stable. The second order has type $\omega + \omega^*$; it is stable, with $A$ the set of even numbers and $A^*$ the set of odd numbers.
:::
::::

::::exercise{#ex-stable-order-approximation difficulty=1 objective="Compute an explicit $\Delta^0_2$ approximation of the half of a stable order with finitely many predecessors."}
Let $\mathcal L$ be a computable stable linear order. For $x, s \in \nat$, let $A_s(x) = 1$ if $x$ has fewer $<_{\mathcal L}$-predecessors than $<_{\mathcal L}$-successors among the numbers $y < s$, and $A_s(x) = 0$ otherwise. Show that $A(x) = \lim_s A_s(x)$ for every $x$.

:::solution
The function $(x, s) \mapsto A_s(x)$ is computable. Let $x \in A$, with $p$ predecessors. Since $\nat$ is infinite and $x \notin A^*$, $x$ has infinitely many successors, so for all large $s$, more than $p$ of them are below $s$, while at most $p$ predecessors are; then $A_s(x) = 1$. Let $x \in A^*$, with $q$ successors: for all large $s$, more than $q$ predecessors are below $s$, so $A_s(x) = 0$. This gives again, by the limit lemma, that $A$ is $\Delta^0_2$.
:::
::::

::::exercise{#ex-td-halves-hyperimmune difficulty=1 objective="Locate the halves of a computable order of type ω + ω* without computable solutions in the hierarchy of immunity."}
Let $\mathcal L$ be a computable linear order of type $\omega + \omega^*$ with no computable ascending or descending sequence, as built by Tennenbaum and Denisov. Show that $A$ and $A^*$ are hyperimmune, and that neither is c.e.

:::solution
If $A$ had an infinite c.e. subset, it would have an infinite computable subset, which computes an ascending sequence by item 2 of :ref{#prop-stable-order-parts}; this sequence would be computable. So $A$ is immune, and it is infinite since the type is $\omega + \omega^*$. By item 3 of :ref{#prop-stable-order-parts}, $A$ is hyperimmune. The same argument applies to $A^*$. An infinite c.e. set is not immune, so neither $A$ nor $A^*$ is c.e. In the proof of :ref{#thm-sads-low}, such an order is in the second case.
:::
::::

::::exercise{#ex-ads-via-coh difficulty=2 objective="Reduce ascending and descending sequences in arbitrary linear orders to the stable case through a cohesive set." lessons="ramsey-theorem/cohesiveness"}
Let $\mathcal L$ be a computable linear order on $\nat$, and $R_x = \{ y : x <_{\mathcal L} y \}$. Let $C$ be an $\vec R$-cohesive set, and $p$ its increasing enumeration. Show that the order $i \prec j \iff p(i) <_{\mathcal L} p(j)$ is a $C$-computable stable linear order, and that $p$ maps its ascending and descending sequences to ascending and descending sequences of $\mathcal L$. Deduce that every computable linear order has an ascending or descending sequence computable in $C \oplus H$ for some cohesive set $C$ and some set $H$ low over $C$.

:::solution
The order $\prec$ is linear, and computable in $C$ since $p$ is. Let $i \in \nat$ and $x = p(i)$. By cohesiveness, $C \subseteq^* R_x$ or $C \subseteq^* \overline{R_x}$. In the first case, all but finitely many $y \in C$ are $<_{\mathcal L}$-above $x$, so $i$ has finitely many $\prec$-predecessors; in the second case, all but finitely many $y \in C$ satisfy $y \leq_{\mathcal L} x$, so $i$ has finitely many $\prec$-successors. So $\prec$ is stable. If $S$ is an ascending sequence for $\prec$ and $i < j$ are in $S$, then $p(i) < p(j)$ and $p(i) <_{\mathcal L} p(j)$; so $p[S]$ is an ascending sequence of $\mathcal L$, computable in $C \oplus S$. The descending case is symmetric.

The sequence $\vec R$ is computable, so it has a cohesive set $C$ (:ref{#prop-cohesive-exists}). By :ref{#thm-sads-low}, relativized to $C$, the order $\prec$ has an ascending or descending sequence $H$ with $(C \oplus H)' \leq_T C'$, and $p[H] \leq_T C \oplus H$. Adapted from Hirschfeldt (2014), Exercise 9.17, which shows that cohesiveness yields a stable suborder of every linear order.
:::
::::

::::exercise{#ex-delta2-degree-ce-in-low difficulty=2 objective="Derive from the low basis for stable linear orders that every $\Delta^0_2$ degree contains a set c.e. in a low set."}
Harizanov proved, and we admit, that for every $\Delta^0_2$ set $D$ there is a computable linear order of type $\omega + \omega^*$ whose half $A$ is Turing equivalent to $D$. Deduce that every $\Delta^0_2$ degree contains a set that is c.e. relative to some low set.

:::solution
Let $\mathcal L$ be such an order, with halves $A$ and $A^* = \overline A$, both Turing equivalent to $D$. By :ref{#thm-sads-low}, $\mathcal L$ has a low ascending or descending sequence $H$. Suppose $H$ is ascending, so that $H \subseteq A$ (:ref{#ex-sads-solutions}). We claim that $A = \{ x : \exists h \in H\ x \leq_{\mathcal L} h \}$, a set c.e. relative to $H$. If $x \leq_{\mathcal L} h \in A$, then $x \in A$, since $A$ is an initial segment. If $x \in A$, then $x$ has finitely many predecessors, and $H$ is infinite, so some $h \in H$ is not a predecessor of $x$, that is, $x \leq_{\mathcal L} h$. Symmetrically, if $H$ is descending, $A^* = \{ x : \exists h \in H\ h \leq_{\mathcal L} x \}$ is c.e. relative to $H$. In both cases a set of the degree of $D$ is c.e. relative to the low set $H$. The argument is due to Jockusch, as reported by Hirschfeldt (2014) at the end of Section 9.1, after Harizanov (1998).
:::
::::
:::::
