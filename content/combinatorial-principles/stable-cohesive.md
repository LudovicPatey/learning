---
title: Stable and cohesive parts
summary: ADS implies COH (Hirschfeldt, Shore), through the lexicographic order of the columns of a sequence of sets; ADS splits into its stable part SADS and its cohesive part CADS, and CAC into its stable part SCAC and ADS; SRT²₂ implies SADS and COH implies CADS; what is known about the separations.
duration: 35
prerequisites: [computable-orders, ramsey-theorem/cohesiveness]
---

The Cholak–Jockusch–Slaman decomposition splits $\mathsf{RT}^2_2$ into a stable part, which is about $\Delta^0_2$ sets, and a cohesive part, which makes an arbitrary coloring stable on an infinite set (:ref{#thm-rt22-decomposition}). The same idea applies to orders. This lesson first proves that $\mathsf{ADS}$ is strong enough to give cohesive sets, then splits $\mathsf{ADS}$ and $\mathsf{CAC}$ into stable and cohesive parts, and ends with what is known about the separations between the pieces.

## ADS implies cohesiveness

A sequence of sets $\vec R = (R_i)$ attaches to each number $x$ its **column** $\sigma_x = R_0(x) R_1(x) \cdots R_{x-1}(x)$, the binary string of length $x$ recording the membership of $x$ in the first $x$ sets. A set is cohesive when, for each $i$, the bit $\sigma_x(i)$ is eventually constant along the set. Order the strings **lexicographically**: $\sigma \leq_{\mathrm{lex}} \tau$ if $\sigma$ is a prefix of $\tau$, or $\sigma(j) < \tau(j)$ at the first position $j$ where they differ. This is a linear order of $\bstr$, and the columns are pairwise distinct, since they have different lengths.

:::theorem[Hirschfeldt, Shore]{#thm-ads-coh}
Over $\mathsf{RCA}_0$, $\mathsf{ADS}$ implies $\mathsf{COH}$. More precisely, for every sequence $\vec R$, every infinite ascending or descending sequence of the linear order $x \leq_L y \iff \sigma_x \leq_{\mathrm{lex}} \sigma_y$ is $\vec R$-cohesive.
:::

**Intuition.** Along an ascending sequence, the columns increase lexicographically. Truncate them at a fixed length $i + 1$: the truncations are non-decreasing, and take values in the finite set $2^{i+1}$, so they are eventually constant. Their last bit is $R_i(x)$.

:::proof{of=thm-ads-coh}
We argue in $\mathsf{RCA}_0$. Given $\vec R$, the map $x \mapsto \sigma_x$ exists by $\Delta^0_1$ comprehension, and so does $\leq_L$, which is a linear order of $\nat$ since $\leq_{\mathrm{lex}}$ is linear and $x \mapsto \sigma_x$ is injective. Let $S$ be an infinite ascending sequence, and fix $i$. For $x \in S$ with $x > i$, let $\tau_x = \sigma_x \uh (i + 1)$.

First, for $x < y$ in $S$, both larger than $i$, $\tau_x \leq_{\mathrm{lex}} \tau_y$. Indeed $\sigma_x <_{\mathrm{lex}} \sigma_y$, since $S$ is ascending. If $\sigma_x$ is a prefix of $\sigma_y$, then $\tau_x = \tau_y$. Otherwise, let $j$ be the first position where they differ, with $\sigma_x(j) < \sigma_y(j)$: if $j \leq i$, then $\tau_x <_{\mathrm{lex}} \tau_y$, and if $j > i$, then $\tau_x = \tau_y$.

The set $M = \{ \tau \in 2^{i+1} : \exists x \in S\, (x > i \wedge \tau_x = \tau) \}$ is a subset of the finite set $2^{i+1}$ defined by a $\Sigma^0_1$ formula; it exists by bounded $\Sigma^0_1$ comprehension, and it is non-empty since $S$ is infinite. Let $\tau$ be its lexicographically largest element, and $x_0 \in S$ with $x_0 > i$ and $\tau_{x_0} = \tau$. For every $y \in S$ with $y > x_0$, $\tau = \tau_{x_0} \leq_{\mathrm{lex}} \tau_y \leq_{\mathrm{lex}} \tau$, so $\tau_y = \tau$ and $R_i(y) = \tau_y(i) = \tau(i)$. So $S \subseteq^* R_i$ if $\tau(i) = 1$, and $S \subseteq^* \overline{R_i}$ if $\tau(i) = 0$. As $i$ is arbitrary, $S$ is $\vec R$-cohesive.

If $S$ is descending, the truncations are non-increasing for $\leq_{\mathrm{lex}}$, and the same argument applies with the lexicographically least element of $M$.
:::

:::quiz[the proof that ADS implies COH]
Why are the columns truncated at length $i + 1$, rather than compared as a whole?

- [x] Because the columns themselves are pairwise distinct and increase along $S$ without ever stabilizing; only their truncations to a fixed length take finitely many values, which makes them eventually constant.
- [ ] Because $\leq_{\mathrm{lex}}$ is not defined on strings of different lengths.

  It is: a prefix comes before its extensions.
- [ ] Because $\sigma_x(i)$ is undefined for $x \leq i$.

  This is a minor point, handled by considering only $x > i$. The truncation is needed for finiteness.

---

Where is $\Sigma^0_1$ induction used?

- [x] In bounded $\Sigma^0_1$ comprehension, which forms the finite set $M$ of truncations that occur in $S$, so that it has a largest element.
- [ ] To show that $\leq_L$ is a linear order.

  This follows from the properties of $\leq_{\mathrm{lex}}$ by a direct argument, without induction on a $\Sigma^0_1$ formula.
- [ ] To show that $S$ is infinite.

  $S$ is infinite by hypothesis.
:::

So $\mathsf{ADS}$, the weakest principle met so far, already solves countably many instances of the pigeonhole principle at once, up to finite error. By :ref{#prop-coh-no-low}, it follows that some computable linear order has no low ascending or descending sequence: the order built from the sequence of Jockusch and Stephan. This gives the result of Hirschfeldt and Shore mentioned in the previous lesson by a different route.

## Stable and cohesive parts of ADS

A linear order is stable when every element has finitely many predecessors or finitely many successors. Restricting $\mathsf{ADS}$ to these orders gives its stable part; the cohesive part asks for an infinite set on which the order becomes stable.

:::definition{#def-sads-cads}
$\mathsf{SADS}$ is $\mathsf{ADS}$ restricted to stable linear orders. $\mathsf{CADS}$ is the statement: every infinite linear order $(L, \leq_L)$ has an infinite subset $S \subseteq L$ such that $(S, \leq_L)$ is stable.
:::

:::proposition[Hirschfeldt, Shore]{#prop-ads-decomposition}
The following are provable in $\mathsf{RCA}_0$.
1. $\mathsf{ADS}$ is equivalent to $\mathsf{SADS} + \mathsf{CADS}$.
2. $\mathsf{SRT}^2_2$ implies $\mathsf{SADS}$.
3. $\mathsf{COH}$ implies $\mathsf{CADS}$.
:::

:::proof{of=prop-ads-decomposition}
1. A stable order is an infinite linear order, so $\mathsf{ADS}$ implies $\mathsf{SADS}$. Let $(L, \leq_L)$ be infinite, and $S \subseteq L$ an infinite set with $(S, \leq_L)$ stable. Then $(S, \leq_L)$ is a linear order whose ascending sequences are contained in $S$, hence ascending sequences of $L$, and the same holds for descending sequences; so $\mathsf{ADS}$ follows from $\mathsf{CADS}$ and $\mathsf{SADS}$ for $(S, \leq_L)$. Conversely, $\mathsf{ADS}$ gives an ascending or descending sequence $S$, and $(S, \leq_L)$ is stable, of type $\omega$ or $\omega^*$.
2. Let $(L, \leq_L)$ be stable, enumerated as $p_0 < p_1 < \cdots$. Color $\{ i, j \}$, for $i < j$, with $1$ if $p_i <_L p_j$ and $0$ otherwise. For each $i$, $p_i$ has finitely many predecessors, and then $\{ i, j \}$ has color $1$ for all large $j$, or finitely many successors, and the color is eventually $0$. So the coloring is stable, and its infinite homogeneous sets give ascending or descending sequences.
3. Let $(L, \leq_L)$ be infinite, enumerated as $p_0 < p_1 < \cdots$, and $R_i = \{ j : p_i <_L p_j \}$. By $\mathsf{COH}$, there is an infinite $\vec R$-cohesive set $C$. Let $S = \{ p_j : j \in C \}$. For $p_i \in S$, either $p_i <_L p_j$ for almost all $j \in C$, and $p_i$ has finitely many predecessors in $S$, or $p_j <_L p_i$ for almost all $j \in C$ (the case $j = i$ being a single exception), and $p_i$ has finitely many successors in $S$. So $(S, \leq_L)$ is stable.
:::

With :ref{#thm-ads-coh}, the four principles are related by
$$
\mathsf{ADS} \;\Longrightarrow\; \mathsf{COH} \;\Longrightarrow\; \mathsf{CADS}, \qquad \mathsf{ADS} \iff \mathsf{SADS} + \mathsf{CADS}, \qquad \mathsf{SRT}^2_2 \;\Longrightarrow\; \mathsf{SADS}.
$$
So $\mathsf{CADS}$ lies between $\mathsf{ADS}$ and $\mathsf{COH}$, and $\mathsf{ADS}$ is equivalent to $\mathsf{SADS} + \mathsf{COH}$. Hirschfeldt and Shore showed that $\mathsf{CADS}$ implies $\mathsf{COH}$ over $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$ (Dzhafarov–Mummert, Proposition 9.2.15); whether $\mathsf{RCA}_0$ suffices is listed as open by Hirschfeldt (Open Question 9.18). For ω-models, where $\mathsf B\Sigma^0_2$ holds, $\mathsf{CADS}$ and $\mathsf{COH}$ are equivalent.

## Stable and cohesive parts of CAC

In a partial order, an element can also be incomparable with almost everything. Let $(P, \leq_P)$ be infinite. An element $x$ is **small** if $x \leq_P y$ for almost every $y \in P$, **large** if $y \leq_P x$ for almost every $y$, and **isolated** if $x \mid_P y$ for almost every $y$.

:::definition{#def-scac}
An infinite partial order is **stable** if every element is small or isolated, or every element is large or isolated. $\mathsf{SCAC}$ is $\mathsf{CAC}$ restricted to stable partial orders.
:::

The definition asks for a uniform choice between small and large. The weaker condition that each element be small, large or isolated gives an equivalent principle over $\mathsf{RCA}_0$ (Jockusch, Kastermans, Lempp, Lerman and Solomon; :ref{#ex-weakly-stable}). In a stable partial order in which every element is small or isolated, an infinite set of small elements can be thinned to a chain, and an infinite set of isolated elements to an antichain, as for stable colorings.

:::proposition[Hirschfeldt, Shore]{#prop-cac-decomposition}
Over $\mathsf{RCA}_0$, $\mathsf{ADS}$ implies that every infinite partial order has an infinite subset on which it is stable. Consequently, $\mathsf{CAC}$ is equivalent to $\mathsf{SCAC} + \mathsf{ADS}$.
:::

:::proof{of=prop-cac-decomposition}
Let $(P, \leq_P)$ be infinite. By :ref{#ex-linear-extension}, it has a linear extension $\leq_L$. By $\mathsf{ADS}$, $\leq_L$ has an infinite ascending or descending sequence $S$; suppose it is ascending, the other case being symmetric. Enumerate $S$ as $s_0 < s_1 < \cdots$ and let $R_i = \{ j : s_i \mid_P s_j \}$. By :ref{#thm-ads-coh}, $\mathsf{COH}$ holds, so there is an infinite $\vec R$-cohesive set $C$; let $X = \{ s_j : j \in C \}$. Let $s_i \in X$. If $C \subseteq^* R_i$, then $s_i$ is incomparable with almost every element of $X$: it is isolated in $X$. Otherwise $s_i$ is comparable with almost every element $s_j$ of $X$; for $j > i$, $s_j$ is larger than $s_i$, so $s_i <_L s_j$, and since $\leq_L$ extends $\leq_P$, $s_j <_P s_i$ is impossible: $s_i <_P s_j$. So $s_i$ is small in $X$. Every element of $X$ is small or isolated in $X$, and $(X, \leq_P)$ is stable. If $S$ is descending, every element of $X$ is large or isolated.

For the equivalence: $\mathsf{CAC}$ implies $\mathsf{SCAC}$, and $\mathsf{ADS}$ by :ref{#prop-rt22-cac-ads}. Conversely, given $(P, \leq_P)$, $\mathsf{ADS}$ gives an infinite $X$ on which it is stable, and $\mathsf{SCAC}$ an infinite chain or antichain of $(X, \leq_P)$, which is one of $(P, \leq_P)$.
:::

The cohesive part of $\mathsf{CAC}$ is thus no new principle: it is $\mathsf{ADS}$ itself (the converse is :ref{#ex-ccac-ads}). The linear extension is what turns "comparable with almost everything" into "below almost everything": along an ascending sequence of $\leq_L$, a comparable later element can only be $\leq_P$-above.

:::quiz[stable parts of partial orders]
In the proof of :ref{#prop-cac-decomposition}, why does one take an ascending sequence of a **linear extension** of $\leq_P$, and not an arbitrary infinite set?

- [x] To orient the comparable pairs: if $s_i$ and $s_j$ are comparable and $s_i <_L s_j$, then $s_i <_P s_j$. Cohesiveness alone only makes each element eventually comparable or eventually incomparable; it does not decide between small and large.
- [ ] Because cohesive sets exist only for linear orders.

  Cohesiveness is about sequences of sets, not about orders.
- [ ] Because a linear extension has an infinite chain.

  Every subset of a linear order is a chain of it; this says nothing about $\leq_P$.
:::

## What separates the pieces

The implications above are all strict, except possibly between $\mathsf{CADS}$ and $\mathsf{COH}$ over $\mathsf{RCA}_0$. The separations use the techniques of the courses on lowness, avoidance and the design of separations, and we admit them.

| Separation | Method | Reference |
| --- | --- | --- |
| $\mathsf{SADS}$ does not imply $\mathsf{COH}$, nor $\mathsf{CADS}$ or $\mathsf{ADS}$ | $\mathsf{SADS}$ has low solutions, $\mathsf{COH}$ does not | Hirschfeldt–Shore; :ref{to="lowness/stable-linear-orders"} |
| $\mathsf{SCAC}$ does not imply $\mathsf{SRT}^2_2$ | $\mathsf{SCAC}$ has low solutions, $\mathsf{SRT}^2_2$ does not | Hirschfeldt–Shore; Downey, Hirschfeldt, Lempp, Solomon |
| $\mathsf{SADS}$ does not imply $\mathsf{WKL}_0$ | some computable stable order has no computably dominated solution | Csima–Mileti; :ref{#ex-sads-hyperimmune} |
| $\mathsf{CAC}$ does not imply $\mathsf{DNR}$, hence neither $\mathsf{WKL}_0$ nor $\mathsf{SRT}^2_2$ | preservation of the property of computing no DNC function | Hirschfeldt–Shore; :ref{to="dnr-wwkl"} |
| $\mathsf{COH}$ does not imply $\mathsf{SADS}$ | $\mathsf{SADS}$ implies $\mathsf B\Sigma^0_2$, $\mathsf{COH}$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$ | Chong–Lempp–Yang; Cholak–Jockusch–Slaman |
| $\mathsf{ADS}$ does not imply $\mathsf{SCAC}$, hence neither $\mathsf{CAC}$; a fortiori $\mathsf{SADS}$ does not imply $\mathsf{SCAC}$ | dependent hyperimmunity | Lerman–Solomon–Towsner; :ref{to="separation-design/separating-instances"} |

The first line is the reason the decomposition of $\mathsf{ADS}$ is better understood than that of $\mathsf{RT}^2_2$: for orders, the stable part provably does not imply the cohesive part, even in ω-models, while whether $\mathsf{SRT}^2_2$ implies $\mathsf{COH}$ in ω-models was open for a long time (Monin and Patey settled it in 2021; see the course on jump compactness avoidance).

::::exercise{#ex-sads-hyperimmune difficulty=2 objective="Show that a stable order without computable solutions has no computably dominated solution, and separate SADS from WKL₀ with an ω-model of computably dominated sets."}
1. Let $(L, \leq_L)$ be a computable stable linear order with no infinite computable ascending or descending sequence, such as the order of :ref{#thm-tennenbaum-denisov}. Show that no infinite ascending or descending sequence of $L$ is computably dominated.
2. Deduce, using :ref{#ex-dominated-scott}, that $\mathsf{WKL}_0$ does not prove $\mathsf{SADS}$.

:::solution
1. Let $S$ be an ascending sequence, so $S \subseteq A$ by :ref{#prop-stable-order-solutions}, and let $p_S$ list $S$ in increasing order. Suppose $S$ is computably dominated: some computable $g$ satisfies $p_S(n) \leq g(n)$ for every $n$. Define computable intervals $F_0 = [0, g(0)]$ and $F_{k+1} = [m_k, g(m_k)]$ with $m_k = \max F_k + 1$. Each $F_k$ meets $S$: $p_S(m) \geq m$ and $p_S(m) \leq g(m)$, so $p_S(m) \in [m, g(m)]$. Let $a_k$ be the $\leq_L$-least element of $F_k$. Since $F_k$ meets $A$, which is an initial segment of $L$, $a_k \in A$. The intervals are disjoint, so $k \mapsto a_k$ is computable and injective, and its range is an infinite computable subset of $A$ (its elements are listed in increasing order, since the intervals are). By :ref{#prop-stable-order-solutions}, this set computes an ascending sequence, which is computable: a contradiction. For a descending sequence, take the $\leq_L$-largest elements, which lie in the final segment $A^*$.
2. By :ref{#ex-dominated-scott}, there is a Scott ideal $\mathcal M$ all of whose members are computably dominated; it is an ω-model of $\mathsf{WKL}_0$ (:ref{#prop-wkl-scott}). The order of :ref{#thm-tennenbaum-denisov} is in $\mathcal M$, and by part 1 it has no solution in $\mathcal M$. So $\mathcal M \not\models \mathsf{SADS}$.

The argument is that of the proof that an immune part of a stable order is hyperimmune (Csima and Mileti; Dzhafarov–Mummert, Proposition 9.2.17).
:::
::::

## Notes and references

:ref{#thm-ads-coh}, :ref{#prop-ads-decomposition} and :ref{#prop-cac-decomposition} are due to Hirschfeldt and Shore (2007). The proofs follow Dzhafarov and Mummert, Theorem 9.2.8 and Propositions 9.2.13 and 9.2.15, and Hirschfeldt, Theorem 9.4 and Exercises 9.17 and 9.25. Dzhafarov and Mummert, Section 9.2.3, survey the separations; the low basis for $\mathsf{SCAC}$ is their Theorem 9.2.19, the preservation of non-DNC degrees their Theorem 9.2.21, and the bound on computably dominated solutions their Proposition 9.2.17, due to Csima and Mileti (2009). That $\mathsf{SADS}$ implies $\mathsf B\Sigma^0_2$ is due to Chong, Lempp and Yang (2010), improving Hirschfeldt and Shore's result for $\mathsf{ADS}$.

- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- B. F. Csima and J. R. Mileti, *The strength of the rainbow Ramsey theorem*, Journal of Symbolic Logic 74 (2009), 1310–1324.
- C. T. Chong, S. Lempp and Y. Yang, *On the role of the collection principle for Σ⁰₂-formulas in second-order reverse mathematics*, Proceedings of the American Mathematical Society 138 (2010), 1093–1100.
- C. G. Jockusch, B. Kastermans, S. Lempp, M. Lerman and R. Solomon, *Stability and posets*, Journal of Symbolic Logic 74 (2009), 693–711.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 9.1 and 9.2.1.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 9.2.

:::::exercises
::::exercise{#ex-weakly-stable difficulty=2 objective="Reduce weakly stable partial orders to stable ones by intersecting the order with the order of ℕ."}
An infinite partial order is **weakly stable** if every element is small, large or isolated. Show in $\mathsf{RCA}_0$ that $\mathsf{SCAC}$ implies that every infinite weakly stable partial order has an infinite chain or antichain.

:::solution
Let $(P, \leq_P)$ be weakly stable, and define $x \leq^*_P y$ if $x \leq_P y$ and $x \leq y$; it is a partial order, as in :ref{#prop-rt22-cac-ads}. A $\leq_P$-small element $x$ is $\leq^*_P$-small, since almost every $y$ satisfies $x \leq_P y$ and $x \leq y$. A $\leq_P$-large or $\leq_P$-isolated element is $\leq^*_P$-isolated: for almost every $y$, either $y <_P x$, and then $x \leq^*_P y$ would force $x = y$ while $y \leq^*_P x$ would force $y \leq x$, which holds only for finitely many $y$; or $x \mid_P y$. So $(P, \leq^*_P)$ is stable, with every element small or isolated.

By $\mathsf{SCAC}$, it has an infinite chain or antichain $S$. A $\leq^*_P$-chain is a $\leq_P$-chain. If $S$ is a $\leq^*_P$-antichain, its elements are not $\leq_P$-small in $P$ (a small element $x$ would be $\leq^*_P$-below almost every element of $S$), so they are $\leq_P$-large or $\leq_P$-isolated in $P$, hence also in $S$, and $(S, \leq_P)$ is a stable partial order in which every element is large or isolated. By $\mathsf{SCAC}$ again, it has an infinite chain or antichain, which is one of $(P, \leq_P)$.

This is due to Jockusch, Kastermans, Lempp, Lerman and Solomon (Dzhafarov–Mummert, Theorem 9.2.11).
:::
::::

::::exercise{#ex-ccac-ads difficulty=1 objective="Complete the identification of the cohesive part of CAC with ADS."}
Let $\mathsf{CCAC}$ be the statement that every infinite partial order has an infinite subset on which it is stable. Show in $\mathsf{RCA}_0$ that $\mathsf{CCAC}$ implies $\mathsf{ADS}$, so that $\mathsf{CCAC}$ and $\mathsf{ADS}$ are equivalent by :ref{#prop-cac-decomposition}.

:::solution
Let $(L, \leq_L)$ be an infinite linear order, and view it as a partial order. By $\mathsf{CCAC}$, there is an infinite $X \subseteq L$ on which $\leq_L$ is stable. Any two elements are comparable, so no element of $X$ is isolated in $X$. By the definition of stability, either every element of $X$ is small in $X$, or every element is large in $X$.

In the first case, let $h_0 = \min X$, and $h_{k+1}$ the least $y \in X$ with $y > h_k$ and $h_k <_L y$. It exists, since $h_k$ is $\leq_L$-below almost every element of $X$. The function $k \mapsto h_k$ is defined by primitive recursion with terminating searches relative to $X \oplus L$, so it exists in $\mathsf{RCA}_0$; it is increasing, and $h_k <_L h_{k+1}$ for every $k$, so by $\Sigma^0_0$ induction $h_k <_L h_l$ for all $k < l$. Its range is an infinite ascending sequence. In the second case, the same construction with $y <_L h_k$ gives a descending sequence.

The uniform choice in the definition of stable partial orders is what makes this work: a set on which every element is small or large, with both kinds present, need not be thinned to a solution without knowing which elements are small.
:::
::::

::::exercise{#ex-cads-type difficulty=1 objective="Check what CADS gives on examples of linear orders."}
For each of the following computable linear orders, give an infinite computable set on which the order is stable, or show that there is none.

1. The order of the rationals: a computable bijection between $\nat$ and $\mathbb Q$ transports the order of $\mathbb Q$ to $\nat$.
2. The order of type $\omega + \omega$ of :ref{#ex-stable-orders-examples} (1).

:::solution
1. Let $q_n$ be the rational coded by $n$. Choose $x_0 = 0$ and $x_{k+1}$ the least $n > x_k$ with $q_n > q_{x_k} + 1$: it exists since infinitely many rationals exceed any given one. The set $\{ x_k \}$ is computable, and on it the order agrees with the order of $\nat$: it has type $\omega$, so it is stable.
2. The set of odd numbers is computable, and the order restricted to it has type $\omega$, which is stable.

In both cases a computable ascending sequence exists, which is more than $\mathsf{CADS}$ asks.
:::
::::
:::::
