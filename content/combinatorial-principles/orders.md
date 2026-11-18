---
title: Chains, antichains, ascending and descending sequences
summary: The chain–antichain principle CAC and the ascending–descending sequence principle ADS; RT²₂ implies CAC and CAC implies ADS over RCA₀; stable linear orders, their two parts, and their solutions.
duration: 25
prerequisites: [ramsey-theorem/stable-colorings]
---


Ramsey's theorem for pairs was the first theorem of ordinary mathematics found to lie outside the linear chain of the Big Five: it is strictly weaker than $\mathsf{ACA}_0$ (Seetapun) and does not follow from $\mathsf{WKL}_0$. Hirschfeldt and Shore (2007) observed that several of its classical consequences are themselves of this kind, and began a systematic study of the principles below $\mathsf{RT}^2_2$. The first two come from order theory: every infinite partial order has an infinite chain or an infinite antichain, and every infinite linear order has an infinite ascending or descending sequence. This lesson places them below $\mathsf{RT}^2_2$ and describes the solutions of the simplest kind of linear orders, the stable ones; the next lesson shows that the principles are not provable in $\mathsf{RCA}_0$.

## Partial and linear orders

Throughout this course, orders are orders of sets of natural numbers. We write $\leq$ for the usual order of $\nat$ and keep "least" and "increasing" for it; orders of other kinds carry a subscript.

:::definition{#def-orders-rca}
In $\mathsf{RCA}_0$, a **partial order** is a pair $(P, \leq_P)$ of sets, with $P \subseteq \nat$ and $\leq_P \subseteq P \times P$ reflexive, antisymmetric and transitive. It is **infinite** if $P$ is infinite, and **linear** if any two elements are comparable. We write $x <_P y$ if $x \leq_P y$ and $x \neq y$, and $x \mid_P y$ if $x$ and $y$ are incomparable.

1. A **chain** is a set $S \subseteq P$ whose elements are pairwise comparable, and an **antichain** is a set $S \subseteq P$ whose distinct elements are pairwise incomparable.
2. For a linear order $(L, \leq_L)$, a set $S \subseteq L$ is an **ascending sequence** if $x <_L y$ for all $x < y$ in $S$, and a **descending sequence** if $y <_L x$ for all $x < y$ in $S$.
:::

An ascending sequence is thus a set on which the order of $L$ agrees with the order of $\nat$, and a descending sequence a set on which it agrees with the reverse order. Listing an infinite ascending sequence in increasing order gives a function $n \mapsto x_n$ with $x_0 <_L x_1 <_L \cdots$; conversely, such a function can be thinned to a set with the same property (:ref{#ex-ads-functions}). The formulation by sets fits the comparison with Ramsey's theorem, whose solutions are also sets.

:::definition{#def-cac-ads}
The **chain–antichain principle** $\mathsf{CAC}$ states that every infinite partial order has an infinite chain or an infinite antichain. The **ascending–descending sequence principle** $\mathsf{ADS}$ states that every infinite linear order has an infinite ascending or an infinite descending sequence.
:::

:::example{#ex-orders-solutions}
1. Order $\nat \setminus \{ 0 \}$ by divisibility. The powers of $2$ form an infinite chain, and the primes an infinite antichain.
2. Let $x \leq_L y$ if $x$ is even and $y$ odd, or $x$ and $y$ are both even and $x \leq y$, or both odd and $y \leq x$. This linear order puts the even numbers, in their usual order, before the odd numbers, in the reverse order: its order type is $\omega + \omega^*$. Every infinite set of even numbers is an ascending sequence and every infinite set of odd numbers a descending sequence. There are no others: if an ascending sequence $S$ contained an odd number $o$, every larger element of $S$ would be $<_L$-above $o$, hence an odd number smaller than $o$; so $S$ would be finite. Symmetrically, a descending sequence contains only odd numbers.
:::

:::proposition[Hirschfeldt, Shore]{#prop-rt22-cac-ads}
Over $\mathsf{RCA}_0$, $\mathsf{RT}^2_2$ implies $\mathsf{CAC}$, and $\mathsf{CAC}$ implies $\mathsf{ADS}$.
:::

:::proof{of=prop-rt22-cac-ads}
Let $(P, \leq_P)$ be an infinite partial order, and let $p_0 < p_1 < \cdots$ enumerate $P$ in increasing order, which is possible in $\mathsf{RCA}_0$ since $P$ is infinite. Color $\{ i, j \}$ with $1$ if $p_i$ and $p_j$ are comparable and with $0$ otherwise; the coloring exists by $\Delta^0_1$ comprehension. If $H$ is an infinite homogeneous set, $\{ p_i : i \in H \}$ is an infinite chain if the color is $1$, and an infinite antichain if it is $0$.

Let $(L, \leq_L)$ be an infinite linear order. Define a partial order on $L$ by
$$
x \leq_P y \iff x \leq y \text{ and } x \leq_L y.
$$
It is reflexive. It is antisymmetric, since $x \leq_P y \leq_P x$ gives $x \leq y \leq x$. It is transitive, since both $\leq$ and $\leq_L$ are. Let $S$ be an infinite chain, and $x < y$ in $S$. Then $x$ and $y$ are $\leq_P$-comparable, and $y \leq_P x$ is impossible since $x < y$; so $x \leq_P y$, hence $x <_L y$, and $S$ is an ascending sequence. Let $S$ be an infinite antichain and $x < y$ in $S$. Then $x \not\leq_P y$, so $x \not\leq_L y$, that is, $y <_L x$: $S$ is a descending sequence.
:::

The partial order of the second part records whether two numbers are ordered by $\leq_L$ in the same way as by $\leq$, or in the opposite way. This comparison of an order with the order of $\nat$ recurs in all the work on $\mathsf{CAC}$ and $\mathsf{ADS}$. It also gives a direct proof that $\mathsf{RT}^2_2$ implies $\mathsf{ADS}$: color $\{ x, y \}$, for $x < y$, with $1$ if $x <_L y$ and $0$ otherwise. The homogeneous sets are exactly the ascending and descending sequences, and the coloring is **transitive**: if $\{ x, y \}$ and $\{ y, z \}$ have color $i$, for $x < y < z$, so does $\{ x, z \}$. In fact $\mathsf{ADS}$ is equivalent to $\mathsf{RT}^2_2$ restricted to transitive colorings (:ref{#ex-ads-transitive}).

:::quiz[the proof that CAC implies ADS]
In the proof of :ref{#prop-rt22-cac-ads}, why is the partial order defined by $x \leq y$ **and** $x \leq_L y$, and not simply by $x \leq_L y$?

- [x] Because a chain of $\leq_L$ alone is any subset of $L$: the order is linear. The conjunction with $\leq$ makes a chain a set on which the two orders agree, and an antichain a set on which they disagree.
- [ ] Because $\leq_L$ is not transitive.

  It is a linear order, hence transitive; the issue is that every set is a chain for it.
- [ ] Because the conjunction is needed for antisymmetry.

  $\leq_L$ is already antisymmetric. The conjunction is needed so that chains and antichains carry information.
:::

## Stable linear orders

An element of an infinite linear order $L$ may have finitely many predecessors, finitely many successors, or infinitely many of both. The order is **stable** if the third case never occurs. Let then
$$
A = \{ x \in L : x \text{ has finitely many } <_L\text{-predecessors} \}, \qquad A^* = L \setminus A.
$$
The elements of $A^*$ have finitely many successors, since they have infinitely many predecessors. For $x \in A$ and $y \in A^*$, $x <_L y$: otherwise the infinitely many predecessors of $y$ would precede $x$. So $L$ is $A$ followed by $A^*$, and if both are infinite, $L$ has order type $\omega + \omega^*$. The order of :ref{#ex-orders-solutions} (2) is of this kind, with $A$ the even numbers.

:::proposition{#prop-stable-order-solutions}
Let $L$ be a stable linear order. Every ascending sequence is contained in $A$, and every descending sequence in $A^*$. Conversely, every infinite set $H \subseteq A$ computes, together with $L$, an ascending sequence contained in $H$, and every infinite subset of $A^*$ computes a descending sequence in it.
:::

:::proof{of=prop-stable-order-solutions}
If $S$ is an ascending sequence and $x \in S$, the infinitely many elements of $S$ larger than $x$ are $<_L$-successors of $x$; so $x$ does not have finitely many successors, and $x \in A$. The case of descending sequences is symmetric. Let $H \subseteq A$ be infinite. Let $h_0 = \min H$, and $h_{k+1}$ the least element of $H$ larger than $h_k$ with $h_k <_L h_{k+1}$. It exists: $h_k$ has finitely many predecessors, so all but finitely many elements of $H$ are $<_L$-successors of $h_k$. The set $\{ h_k : k \in \nat \}$ is computable in $H \oplus L$, increasing in both orders, and contained in $H$.
:::

So for a computable stable order, the solutions to $\mathsf{ADS}$ are, up to Turing equivalence, the infinite subsets of $A$ and of $A^*$, exactly as the solutions to a computable stable coloring are the infinite subsets of its limit set and of the complement (:ref{#prop-srt-d22}). The set $A$ is $\Delta^0_2$: "$x$ has finitely many predecessors" is $\Sigma^0_2$, and its negation is equivalent to "$x$ has finitely many successors", also $\Sigma^0_2$.

::::exercise{#ex-linear-extension difficulty=1 objective="Build a linear extension of a partial order by inserting the elements one at a time, a construction used in the next lesson."}
Show in $\mathsf{RCA}_0$ that every partial order $(P, \leq_P)$ has a **linear extension**: a linear order $\leq_L$ of $P$ such that $x \leq_P y$ implies $x \leq_L y$. In particular, every computable partial order has a computable linear extension.

:::solution
Define $\leq_L$ on $P_s = P \cap \{ 0, \ldots, s - 1 \}$ by recursion on $s$, starting from the empty order. If $s \notin P$, nothing changes. If $s \in P$, given a linear extension of $\leq_P$ on $P_s$, let $x$ be the $\leq_L$-largest element of $P_s$ with $x <_P s$, if there is one, and insert $s$ immediately after $x$; if there is none, insert $s$ before all elements.

The new order extends $\leq_P$ on $P_{s+1}$. Every $y <_P s$ satisfies $y \leq_L x$, by the choice of $x$, so $y <_L s$. Let $y \in P_s$ with $s <_P y$. Every $x' \in P_s$ with $x' <_P s$ satisfies $x' <_P y$ by transitivity, so $x' <_L y$ since the order on $\{ 0, \ldots, s - 1 \}$ extends $\leq_P$. Hence, if $s$ was inserted after $x$, $y$ is $<_L$-above $x$, and therefore above $s$, which was inserted immediately after $x$; if $s$ was inserted first, $s <_L y$ as well.

The recursion defines the finite orders as codes, by primitive recursion relative to $P$ and $\leq_P$, so $\leq_L$ exists by $\Delta^0_1$ comprehension: $x \leq_L y$ is decided at step $\max(x, y) + 1$ and never changes.
:::
::::

## Notes and references

$\mathsf{CAC}$ and $\mathsf{ADS}$ were formulated and placed below $\mathsf{RT}^2_2$ by Hirschfeldt and Shore (2007); :ref{#prop-rt22-cac-ads} follows Dzhafarov and Mummert, Propositions 9.2.4 and 9.2.5, and Hirschfeldt, Exercise 9.3. The classical principle behind $\mathsf{CAC}$ is Dilworth's theorem on finite partial orders, and behind $\mathsf{ADS}$ the Erdős–Szekeres theorem (:ref{#ex-erdos-szekeres}). Stable linear orders are studied in Hirschfeldt, Section 9.1, and Dzhafarov and Mummert, Section 9.2.2.

- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 9.1.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 9.2.

:::::exercises
::::exercise{#ex-ads-functions difficulty=1 objective="Check that the formulations of ADS by sets and by sequences are equivalent over RCA₀."}
Show in $\mathsf{RCA}_0$: if a linear order $(L, \leq_L)$ has a function $f : \nat \to L$ with $f(n) <_L f(n+1)$ for every $n$, then it has an infinite ascending sequence in the sense of :ref{#def-orders-rca}. State and prove the converse.

:::solution
The function $f$ is injective, since $f(m) <_L f(n)$ for $m < n$ by transitivity. Define $n_0 = 0$ and $n_{k+1}$ the least $n > n_k$ with $f(n) > f(n_k)$. It exists: the values $f(n)$, $n > n_k$, are pairwise distinct, so they cannot all lie in the finite set $\{ 0, \ldots, f(n_k) \}$. The function $g(k) = f(n_k)$ is defined by primitive recursion with terminating searches relative to $f$, so it exists in $\mathsf{RCA}_0$, and it is strictly increasing. Its range $S$ exists by $\Delta^0_1$ comprehension: $x \in S$ if and only if $g(k) = x$ for some $k \leq x$. For $x = g(k) < y = g(l)$ in $S$, $k < l$, hence $n_k < n_l$ and $f(n_k) <_L f(n_l)$: $S$ is an ascending sequence, and it is infinite.

Conversely, if $S$ is an infinite ascending sequence, the function listing $S$ in increasing order exists in $\mathsf{RCA}_0$, and it is $<_L$-increasing. The same holds for descending sequences with the reverse order.
:::
::::

::::exercise{#ex-ads-transitive difficulty=2 objective="Characterize ADS as Ramsey's theorem for transitive colorings, by building a linear order whose solutions are homogeneous."}
A coloring $c : [\nat]^2 \to 2$ is **transitive** if for $x < y < z$ and each color $i$, $c(\{ x, y \}) = c(\{ y, z \}) = i$ implies $c(\{ x, z \}) = i$.

1. Show that $\mathsf{RT}^2_2$ restricted to transitive colorings implies $\mathsf{ADS}$ over $\mathsf{RCA}_0$.
2. Let $c$ be transitive. Build $\leq_L$ on $\nat$ by inserting $s$ at step $s$: if some $x < s$ has $c(\{ x, s \}) = 1$, insert $s$ immediately after the $\leq_L$-largest such $x$; otherwise, insert $s$ before all elements. Show that for $y < w$, $y <_L w$ implies $c(\{ y, w \}) = 1$, and $w <_L y$ implies $c(\{ y, w \}) = 0$.
3. Deduce that $\mathsf{ADS}$ implies $\mathsf{RT}^2_2$ restricted to transitive colorings over $\mathsf{RCA}_0$.

:::solution
1. Given $(L, \leq_L)$, enumerate $L$ as $p_0 < p_1 < \cdots$ and color $\{ i, j \}$, $i < j$, with $1$ if $p_i <_L p_j$ and $0$ otherwise. The coloring is transitive, since $<_L$ and its reverse are transitive. An infinite homogeneous set $H$ gives the ascending sequence $\{ p_i : i \in H \}$ for color $1$, and a descending one for color $0$.
2. First, $w <_L y$ implies $c(\{ y, w \}) = 0$: if $c(\{ y, w \}) = 1$, then at step $w$ the element $y$ is a candidate, and $w$ is inserted immediately after the $\leq_L$-largest candidate $x$, so $y \leq_L x <_L w$.

   Suppose now that some pair $y < w$ has $y <_L w$ and $c(\{ y, w \}) = 0$, and take one with $w$ least, by the least number principle for a bounded formula. Since $y <_L w$, $w$ was not inserted first: it was inserted immediately after the $\leq_L$-largest $x < w$ with $c(\{ x, w \}) = 1$, and $y \leq_L x$, with $y \neq x$ since $c(\{ y, w \}) = 0$. If $x < y$: then $y <_L x$, so by the first part $c(\{ x, y \}) = 0$, and transitivity for color $0$ gives $c(\{ x, w \}) = 0$, a contradiction. If $y < x$: if $c(\{ y, x \}) = 1$, transitivity for color $1$ with $c(\{ x, w \}) = 1$ gives $c(\{ y, w \}) = 1$, a contradiction; so $c(\{ y, x \}) = 0$, and the pair $y < x$ has $y <_L x$ and color $0$, with $x < w$, contradicting the minimality of $w$.
3. The order of part 2 exists by $\Delta^0_1$ comprehension, as in :ref{#ex-linear-extension}. If $S$ is an infinite ascending sequence, every pair $y < w$ of $S$ has $y <_L w$, hence color $1$ by part 2; if $S$ is descending, every pair has color $0$. So $S$ is homogeneous.

Dzhafarov and Mummert, Proposition 9.2.7, give this construction. The minimal counterexample is taken over all pairs, not only pairs of $S$: the element $x$ found in the argument need not belong to $S$.
:::
::::

::::exercise{#ex-erdos-szekeres difficulty=1 objective="Prove the finite version of ADS, the Erdős–Szekeres theorem, by labeling each element with the length of the longest ascending sequence ending there."}
Let $\leq_L$ be a linear order of $\{ 0, \ldots, n^2 \}$. Show that there is an ascending or a descending sequence of $n + 1$ elements, in the sense of :ref{#def-orders-rca}. Show that $n^2 + 1$ cannot be replaced by $n^2$.

:::solution
For each $x$, let $\ell(x)$ be the largest size of an ascending sequence whose largest element is $x$. If $\ell(x) \geq n + 1$ for some $x$, we are done. Otherwise $\ell$ takes values in $\{ 1, \ldots, n \}$ on $n^2 + 1$ elements, so some value $k$ is taken by $n + 1$ elements $x_0 < \cdots < x_n$. For $i < j$, if $x_i <_L x_j$, an ascending sequence of size $k$ ending at $x_i$, extended by $x_j$, would be ascending of size $k + 1$ ending at $x_j$; so $x_j <_L x_i$. The elements $x_0, \ldots, x_n$ form a descending sequence.

For $n^2$ elements, write $x = qn + r$ with $0 \leq r < n$, and let $x <_L y$ if $q < q'$, or $q = q'$ and $r > r'$, for $y = q'n + r'$: $n$ blocks of $n$ consecutive numbers, the blocks in increasing order, each block reversed. A descending sequence lies in one block, so has at most $n$ elements; an ascending sequence has at most one element per block, so at most $n$ elements.
:::
::::

::::exercise{#ex-stable-orders-examples difficulty=1 objective="Recognize stable linear orders and their two parts on examples."}
For each of the following computable linear orders of $\nat$, say whether it is stable, and if so give $A$ and $A^*$.

1. $x <_L y$ if $x$ is odd and $y$ even, or both have the same parity and $x < y$.
2. The order of the integers: $2k + 1 <_L 2k - 1 <_L \cdots <_L 1 <_L 0 <_L 2 <_L 4 <_L \cdots$, that is, the odd numbers in decreasing order followed by the even numbers in increasing order.
3. The order of :ref{#ex-orders-solutions} (2).

:::solution
1. The odd numbers, in increasing order, come first: every odd number has finitely many predecessors. An even number $y$ has all odd numbers as predecessors, and infinitely many successors (the larger even numbers). So the order, of type $\omega + \omega$, is not stable.
2. An odd number has infinitely many successors (all even numbers) and infinitely many predecessors (the larger odd numbers). The order, of type $\omega^* + \omega$, is not stable.
3. It is stable, with $A$ the even numbers and $A^*$ the odd numbers.
:::
::::
:::::
