---
title: Theorems equivalent to ACA₀
summary: The monotone convergence theorem, the existence of torsion subgroups of countable abelian groups, and König's lemma are each equivalent to ACA₀ over RCA₀; each reversal codes the range of an injection into a computable instance.
duration: 50
prerequisites: [aca0, second-order-arithmetic/real-numbers, pi01-classes/finitely-branching-trees]
---

A **reversal** shows that a theorem, added to the base theory $\mathsf{RCA}_0$, proves the axioms used to prove it. For $\mathsf{ACA}_0$, all reversals of this lesson follow one pattern, already present in the computability-theoretic examples of earlier courses: one builds, from an injective function $f$, an instance of the theorem that is computable from $f$ and whose solutions compute the range of $f$; by :ref{#thm-aca-equivalents} (4), the theorem then implies $\mathsf{ACA}_0$. In computability-theoretic terms, the reversal is a uniform version of a construction of a computable instance all of whose solutions compute $\emptyset'$, with $\emptyset'$ replaced by an arbitrary set given by an enumeration. The work lies in checking that the argument uses only $\Delta^0_1$ comprehension and $\Sigma^0_1$ induction.

The three theorems come from analysis, algebra and combinatorics. They are representative of a list of several dozen statements equivalent to $\mathsf{ACA}_0$ (Simpson, Chapter III).

## Monotone convergence

**Intuition.** The limit of a bounded monotone sequence of rationals is determined by the set of rationals that some term exceeds, a $\Sigma^0_1$ set; arithmetic comprehension provides it. Conversely, the Specker sequence (:ref{#prop-specker}) adds $2^{-m-1}$ when $m$ is enumerated into $\emptyset'$, and its limit encodes $\emptyset'$: knowing the limit with precision $2^{-m-1}$ tells whether $m$ will still be enumerated. The reversal replaces $\emptyset'$ by the range of an arbitrary injection.

:::theorem{#thm-monotone-aca}
Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to the monotone convergence theorem: every bounded non-decreasing sequence of reals has a limit.
:::

:::proof{of=thm-monotone-aca}
($\Rightarrow$) Rescaling, we may assume $0 \leq x_n \leq 1$. By arithmetic comprehension, the set $S$ of rationals $q$ such that $x_n > q$ for some $n$ exists. For each $k$, let $q_k$ be the largest number of the form $j 2^{-k}$, with $-1 \leq j \leq 2^k$, that belongs to $S$; it exists since $-2^{-k} < x_0$, and the sequence $(q_k)$ exists by $\Delta^0_1$ comprehension relative to $S$. Some $x_n$ exceeds $q_k$, and no $x_n$ exceeds $q_k + 2^{-k}$: either $q_k + 2^{-k} \notin S$, or $q_k = 1$. For $k \leq l$, $q_k \leq q_l$, since $q_k$ is also of the form $j 2^{-l}$, and $q_l < q_k + 2^{-k}$, since some $x_n$ exceeds $q_l$. So $x = (q_k)$ is a real, with $q_k \leq x \leq q_k + 2^{-k}$. It is the limit: every $x_n$ satisfies $x_n \leq q_k + 2^{-k} \leq x + 2^{-k}$ for all $k$, hence $x_n \leq x$; and for each $k$ some $x_n > q_k \geq x - 2^{-k}$, so $x - x_m < 2^{-k}$ for all $m \geq n$, since the sequence is non-decreasing.

($\Leftarrow$) We prove (4) of :ref{#thm-aca-equivalents}. Let $f$ be injective, and $x_n = \sum_{i \leq n} 2^{-f(i)-1}$, as in :ref{#prop-specker}. It is non-decreasing and bounded by $1$; let $x$ be its limit. For each $m$, there is $n$ with $x - x_n < 2^{-m-1}$, and then $m$ is in the range of $f$ if and only if $m = f(i)$ for some $i \leq n$: an $i > n$ with $f(i) = m$ would give $x - x_n \geq x_i - x_n \geq 2^{-m-1}$. The condition $x - x_n < 2^{-m-1}$ is $\Sigma^0_1$ in $x$ and $(x_n)$. Hence
$$
\begin{aligned}
m \in \mathrm{ran}(f) &\iff \exists n\, \big(x - x_n < 2^{-m-1} \wedge \exists i \leq n\ f(i) = m\big), \\
m \notin \mathrm{ran}(f) &\iff \exists n\, \big(x - x_n < 2^{-m-1} \wedge \forall i \leq n\ f(i) \neq m\big),
\end{aligned}
$$
two $\Sigma^0_1$ formulas. In both lines, the left-to-right direction holds with any $n$ such that $x - x_n < 2^{-m-1}$, by the observation above for the first line; the right-to-left direction is immediate for the first line and is the observation above for the second. So the range exists by $\Delta^0_1$ comprehension.
:::

The forward direction uses arithmetic comprehension once, for the $\Sigma^0_1$ formula defining $S$; by :ref{#thm-aca-equivalents}, $\Sigma^0_1$ comprehension would suffice. The reversal shows that the converse is also true in a strong sense: one limit already yields the range of the injection.

:::quiz[monotone convergence]
In the reversal of :ref{#thm-monotone-aca}, why is the range of $f$ defined by a $\Pi^0_1$ formula as well as by a $\Sigma^0_1$ formula?

- [x] Because the limit $x$ bounds the remaining sum: once $x - x_n < 2^{-m-1}$, the value $m$ can no longer appear, so "$m \notin \mathrm{ran}(f)$" also has a witness $n$, which makes it $\Sigma^0_1$ and the range $\Pi^0_1$.
- [ ] Because $f$ is injective.

  Injectivity makes each value contribute once to the sum, but without the limit the complement of the range would not have a $\Sigma^0_1$ definition.
- [ ] Because the sequence $(x_n)$ is computable from $f$.

  This holds for every $f$, and for $f$ enumerating $\emptyset'$ the complement of the range is not c.e.; the limit $x$ is the additional information.
:::

## Torsion subgroups

The second example comes from algebra. A **countable abelian group** is coded in $\mathsf{RCA}_0$ by a set $A \subseteq \nat$ of elements together with the graph of the group operation and a neutral element, satisfying the group axioms. An element $a$ is **torsion** if $na = 0$ for some $n \geq 1$.

**Intuition.** Being torsion is a $\Sigma^0_1$ property of an element. In a group with a generator $x_m$ for each $m$, one can make $x_m$ torsion exactly when $m$ is enumerated in the range of $f$, by adding the relation $(2i+1) x_m = 0$ at the moment $f(i) = m$. The difficulty is that the elements of the group must form a set, so that equality must be decidable; this is achieved by choosing normal forms for which the relations are applied at a bounded cost.

:::theorem{#thm-torsion-aca}
Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to the statement: for every countable abelian group, the set of its torsion elements exists.
:::

:::proof{of=thm-torsion-aca}
($\Rightarrow$) The set $\{ a \in A : \exists n \geq 1\ na = 0 \}$ is defined by a $\Sigma^0_1$ formula; it exists by arithmetic comprehension.

($\Leftarrow$) We prove (4) of :ref{#thm-aca-equivalents}. Let $f$ be injective. The group $G$ is meant to be generated by elements $x_m$, $m \in \nat$, with the relations $(2i + 1) x_{f(i)} = 0$; we give its elements by normal forms. An element is a finite sequence of integers $(c_0, \dots, c_{l-1})$ with $c_{l-1} \neq 0$ (the empty sequence for $0$), representing $\sum_m c_m x_m$, such that for every $m < l$ and every $i < |c_m|$, $f(i) \neq m$. Since $f$ is injective, the condition says: if $m = f(i)$, then $|c_m| \leq i$, so $c_m$ lies in $\{-i, \dots, i\}$, a set of representatives modulo $2i + 1$. The set of elements exists by $\Delta^0_1$ comprehension, since the condition is bounded. The sum is computed coordinatewise: given $c_m + d_m = s$, if $f(i) = m$ for some $i < |s|$, a bounded search, replace $s$ by its representative modulo $2i + 1$ in $\{-i, \dots, i\}$; otherwise keep $s$; finally, remove the trailing zeros. In each coordinate this is the addition of $\mathbb Z$ if $m \notin \mathrm{ran}(f)$, and of $\mathbb Z / (2i+1)\mathbb Z$ if $m = f(i)$: when $m = f(i)$, both summands lie in $\{-i, \dots, i\}$, and the reduction applies exactly when the sum leaves this set. So $G$ satisfies the group axioms, coordinatewise, and $G$ exists by $\Delta^0_1$ comprehension.

Let $x_m$ be the element with $1$ at coordinate $m$ and $0$ elsewhere, reduced as above (it is $0$ if $m = f(0)$). If $m = f(i)$, then $(2i + 1) x_m = 0$. If $m \notin \mathrm{ran}(f)$, the coordinate $m$ of $n x_m$ is $n \neq 0$ for every $n \geq 1$, so $x_m$ is not torsion. Let $T$ be the set of torsion elements of $G$, given by the hypothesis. Then $\mathrm{ran}(f) = \{ m : x_m \in T \}$, which exists by $\Delta^0_1$ comprehension.
:::

The proof is a computable presentation of the group $\bigoplus_{m \notin \mathrm{ran}(f)} \mathbb Z \oplus \bigoplus_{i} \mathbb Z / (2i+1) \mathbb Z$ in which one cannot decide which summand $x_m$ generates. The choice of normal forms is what makes the presentation computable: a relation $(2i+1) x_m = 0$ added late, at a large $i$, affects only coefficients of absolute value larger than $i$, and checking for such relations requires a search bounded by the coefficients.

## König's lemma

A tree $T \subseteq \nat^{<\nat}$ is **finitely branching** if every node has finitely many immediate successors. **König's lemma** states that every infinite finitely branching tree has an infinite path. Weak König's lemma, the restriction to binary trees, is the subject of the next lessons. The computability-theoretic content of König's lemma was established in :ref{#thm-konig-strength}: the computable instances require exactly the sets that are PA relative to $\emptyset'$. The reverse mathematics version is the following.

**Intuition.** The classical proof follows the nodes that have infinitely many extensions, a $\Pi^0_2$ property; arithmetic comprehension provides the set of these nodes, and the path is then found by a search. For the reversal, the tree of :ref{#thm-finitely-branching-jump} is adapted to an arbitrary injection: at position $m$, a path must either name an $i$ with $f(i) = m$, or guess that there is none; a wrong guess is detected when $f(i) = m$ appears, and the node dies. Only the correct guesses survive forever, so the unique path encodes the range.

:::theorem{#thm-konig-aca}
Over $\mathsf{RCA}_0$, $\mathsf{ACA}_0$ is equivalent to König's lemma.
:::

:::proof{of=thm-konig-aca}
($\Rightarrow$) Let $T$ be infinite and finitely branching. By arithmetic comprehension, the set $E$ of nodes of $T$ with infinitely many extensions in $T$ exists. The root belongs to $E$. If $\sigma \in E$, one of its finitely many immediate successors belongs to $E$: otherwise each of them has finitely many extensions, and so would $\sigma$, by arithmetic induction on the number of successors. Define the path $P$ by $P \uh 0 = \varepsilon$ and $P \uh (n+1) = $ the first immediate successor of $P \uh n$ in $E$, in the order of codes; this is a search relative to $T \oplus E$ that terminates, so $P$ exists by $\Delta^0_1$ comprehension.

($\Leftarrow$) We prove (4) of :ref{#thm-aca-equivalents}. Let $f$ be injective. Let $T$ be the set of sequences $\sigma \in \nat^{<\nat}$ such that, for every $m < |\sigma|$, either $\sigma(m) = i + 1$ with $f(i) = m$, or $\sigma(m) = 0$ and $f(i) \neq m$ for every $i < |\sigma|$. It is a tree, defined by a bounded formula, and each node has at most two immediate successors, since $f$ is injective. It is infinite: for each $n$, the sequence $\sigma$ of length $n$ with $\sigma(m) = i + 1$ if $f(i) = m$ for some $i < n$, and $\sigma(m) = 0$ otherwise, belongs to $T$. Let $P$ be a path. If $P(m) = i + 1$, then $f(i) = m$. If $P(m) = 0$, then $f(i) \neq m$ for every $i$, since $P \uh n \in T$ for every $n > i$. So $\mathrm{ran}(f) = \{ m : P(m) \neq 0 \}$, which exists by $\Delta^0_1$ comprehension.
:::

:::figure[The beginning of the tree of the reversal of :ref{#thm-konig-aca}, for an injection with $f(0) = 2$, $f(1) = 0$, $f(2) = 4$, $f(3) = 1$, $f(i) > 4$ for $i \geq 4$, so that $3$ is not in the range. Each edge is labeled by the value it adds. The guess $0$ at position $1$ survives until length $3$, and dies at length $4$, when $f(3) = 1$ is taken into account.]
<svg class="fig" viewBox="0 0 600 360" width="600" role="img" aria-label="The tree of the reversal of König’s lemma for an injection f: the nodes that guess a value 0 too early die, and the unique infinite path lists, at each position m, either i+1 with f(i)=m or 0"><line x1="160.0" y1="76" x2="70.0" y2="122" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="107.0" y="103.0" text-anchor="end" class="mrm" font-size="13">0</text><line x1="160.0" y1="76" x2="250.0" y2="122" class="accent-stroke" stroke-width="2.2"/><text x="213.0" y="103.0" text-anchor="start" class="mrm" font-size="13">2</text><line x1="250.0" y1="122" x2="190.0" y2="168" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="212.0" y="149.0" text-anchor="end" class="mrm" font-size="13">0</text><line x1="250.0" y1="122" x2="310.0" y2="168" class="accent-stroke" stroke-width="2.2"/><text x="288.0" y="149.0" text-anchor="start" class="mrm" font-size="13">4</text><line x1="190.0" y1="168" x2="190.0" y2="214" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="198.0" y="195.0" text-anchor="start" class="mrm" font-size="13">1</text><line x1="310.0" y1="168" x2="310.0" y2="214" class="accent-stroke" stroke-width="2.2"/><text x="318.0" y="195.0" text-anchor="start" class="mrm" font-size="13">1</text><line x1="310.0" y1="214" x2="310.0" y2="260" class="accent-stroke" stroke-width="2.2"/><text x="318.0" y="241.0" text-anchor="start" class="mrm" font-size="13">0</text><line x1="310.0" y1="260" x2="310.0" y2="306" class="accent-stroke" stroke-width="2.2"/><text x="318.0" y="287.0" text-anchor="start" class="mrm" font-size="13">3</text><circle cx="160.0" cy="76" r="4" class="accent-fill"/><circle cx="70.0" cy="122" r="3.5" class="muted-fill"/><circle cx="250.0" cy="122" r="4" class="accent-fill"/><circle cx="190.0" cy="168" r="3.5" class="muted-fill"/><circle cx="310.0" cy="168" r="4" class="accent-fill"/><circle cx="190.0" cy="214" r="3.5" class="muted-fill"/><circle cx="310.0" cy="214" r="4" class="accent-fill"/><circle cx="310.0" cy="260" r="4" class="accent-fill"/><circle cx="310.0" cy="306" r="4" class="accent-fill"/><text x="310.0" y="326" text-anchor="middle" class="mrm" font-size="12">⋮</text><text x="170.0" y="70" class="mrm" font-size="13">ε</text><text x="560" y="104" text-anchor="end" class="label">position 0</text><text x="560" y="150" text-anchor="end" class="label">position 1</text><text x="560" y="196" text-anchor="end" class="label">position 2</text><text x="560" y="242" text-anchor="end" class="label">position 3</text><text x="560" y="288" text-anchor="end" class="label">position 4</text><text x="20" y="20" class="label">the injection f:</text><text x="20" y="38" class="math" font-size="14">f<tspan class="mrm">(0) = 2</tspan></text><text x="82" y="38" class="math" font-size="14">f<tspan class="mrm">(1) = 0</tspan></text><text x="144" y="38" class="math" font-size="14">f<tspan class="mrm">(2) = 4</tspan></text><text x="206" y="38" class="math" font-size="14">f<tspan class="mrm">(3) = 1</tspan></text><text x="268" y="38" class="math" font-size="14">f<tspan class="mrm">(4) = 6</tspan></text><text x="330" y="38" class="math" font-size="14">f<tspan class="mrm">(5) = 7</tspan></text><line x1="24" y1="346" x2="44" y2="346" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="350" class="label">0 guessed at m, then f(i) = m appears</text><line x1="320" y1="346" x2="340" y2="346" class="accent-stroke" stroke-width="2.2"/><text x="346" y="350" class="label">the unique infinite path</text></svg>
:::

The tree in the reversal has at most two immediate successors at each node, but their values are not bounded by a function computable from $f$: the successors of a node $\sigma$ of length $m$ are among $\sigma 0$ and $\sigma (i + 1)$ with $f(i) = m$. For trees with a bound computable from the tree, or for binary trees, the strength drops to weak König's lemma (:ref{#prop-finitely-branching-coding}; Simpson, Lemma IV.1.4).

:::quiz[König's lemma]
In the reversal of :ref{#thm-konig-aca}, why does a path $P$ with $P(m) = 0$ guarantee that $m$ is not in the range of $f$?

- [x] Because every prefix $P \uh n$ belongs to $T$, and membership in $T$ with $P(m) = 0$ requires $f(i) \neq m$ for all $i < n$; as $n$ is arbitrary, $f(i) \neq m$ for all $i$.
- [ ] Because $f$ is injective.

  Injectivity bounds the branching of $T$; the conclusion comes from the infinitely many prefixes of the path.
- [ ] Because $0$ is the leftmost choice.

  The path need not be leftmost; any path works.

---

In the forward direction, where is arithmetic comprehension used?

- [x] To form the set $E$ of nodes with infinitely many extensions, defined by a $\Pi^0_2$ formula relative to $T$.
- [ ] To show that $T$ is infinite.

  This is the hypothesis.
- [ ] To define the path by a search.

  Given $E$, the path is computed by a search, which only requires $\Delta^0_1$ comprehension.
:::

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{ACA}_0$ is equivalent over $\mathsf{RCA}_0$ to the statement: every bounded sequence of reals has a least upper bound.

:::solution
($\Rightarrow$) Let $(x_n)$ be bounded, rescaled into $[0, 1]$. The proof of the forward direction of :ref{#thm-monotone-aca} does not use monotonicity until its last sentence: it produces a real $x$ with $x_n \leq x$ for every $n$, and for every $k$ some $x_n > x - 2^{-k}$. So $x$ is an upper bound, and every $y < x$ is exceeded by some $x_n$, taking $k$ with $2^{-k} < x - y$. Hence $x$ is the least upper bound.

($\Leftarrow$) We prove the monotone convergence theorem. Let $(x_n)$ be non-decreasing and bounded, and $x$ its least upper bound. For every $k$, $x - 2^{-k}$ is not an upper bound, so some $x_n > x - 2^{-k}$, and then $x - 2^{-k} < x_n \leq x_m \leq x$ for every $m \geq n$. So $x$ is the limit, and :ref{#thm-monotone-aca} applies.
:::
::::

::::exercise{difficulty=2}
The Bolzano–Weierstrass theorem states that every sequence of reals in $[0, 1]$ has a subsequence converging to some real. Show that it is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.

:::solution
($\Rightarrow$) With arithmetic comprehension relative to the sequence, define nested closed dyadic intervals $J_0 = [0, 1] \supseteq J_1 \supseteq \cdots$, with $J_k$ of length $2^{-k}$ containing $x_n$ for infinitely many $n$: take the left half of $J_k$ if it contains infinitely many terms, an arithmetic property, and the right half otherwise. By a search, choose $n_0 < n_1 < \cdots$ such that $x_{n_k}$ lies within $2^{-k}$ of $J_k$, a $\Sigma^0_1$ condition satisfied by infinitely many indices. The left endpoints of the $J_k$ form a real $x$, which lies in every $J_k$; since $J_k$ has length $2^{-k}$, $|x_{n_k} - x| < 2^{-k+1}$, so the subsequence converges to $x$.

($\Leftarrow$) We prove the monotone convergence theorem and apply :ref{#thm-monotone-aca}. Let $(x_n)$ be non-decreasing, rescaled into $[0, 1]$, and let $(x_{n_k})$ converge to $x$. Every $x_m$ satisfies $x_m \leq x$: otherwise, all terms $x_{n_k}$ with $n_k \geq m$ would be at least $x_m > x$, and could not converge to $x$. Given $\varepsilon > 0$, choose $k$ with $x - x_{n_k} < \varepsilon$; then $0 \leq x - x_m < \varepsilon$ for every $m \geq n_k$. So $x$ is the limit of the whole sequence.
:::
::::

## Notes and references

The equivalences of this lesson are in Simpson's monograph, Chapter III: monotone convergence and least upper bounds in Theorem III.2.2, Bolzano–Weierstrass in Theorems III.2.2 and III.2.9, torsion subgroups in Theorem III.6.2, König's lemma in Theorem III.7.2. Most were stated by Friedman (1976); the algebraic ones are due to Friedman, Simpson and Smith (1983), whose paper also contains the existence of bases of countable vector spaces and of maximal ideals of countable commutative rings (Simpson, Theorems III.4.3 and III.5.5). Hirschfeldt, Section 4.3, describes the method of reversal used here and states König's lemma as an exercise; Dzhafarov and Mummert, Chapters 10 and 11, survey analysis and algebra.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Chapter III.
- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- H. Friedman, S. G. Simpson and R. L. Smith, *Countable algebra and set existence axioms*, Annals of Pure and Applied Logic 25 (1983), 141–181.
- E. Specker, *Nicht konstruktiv beweisbare Sätze der Analysis*, Journal of Symbolic Logic 14 (1949), 145–158.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 4.3.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Chapters 10 and 11.
