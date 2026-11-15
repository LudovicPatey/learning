---
title: Ramsey's theorem in the arithmetic hierarchy
summary: Ramsey's theorem for n-tuples; pre-homogeneous sets and the Erdős–Radó tree; every coloring of n-tuples has a homogeneous set computable in any degree PA over its (n−1)-st jump.
duration: 50
prerequisites: [big-five/wkl0]
---

Ramsey's theorem states that every finite coloring of the $n$-element subsets of $\nat$ has an infinite set on which the coloring is constant. Jockusch (1972) determined how complex such sets must be for computable colorings: homogeneous sets can be found computably in any degree PA over $\obf^{(n-1)}$, but not, in general and for $n \geq 2$, at the level $\Sigma^0_n$. This lesson proves the upper bound, through pre-homogeneous sets and a finitely branching tree. The next one proves the lower bound, and shows that for $n \geq 3$ homogeneous sets can be forced to compute $\emptyset'$, which makes Ramsey's theorem for triples equivalent to $\mathsf{ACA}_0$. For pairs, the two bounds leave a gap, which the rest of the course explores.

## Statements

For a set $X$ and $n \geq 1$, $[X]^n$ is the set of $n$-element subsets of $X$, identified with increasing tuples $x_1 < \cdots < x_n$. A **$k$-coloring** of $[X]^n$ is a function $f : [X]^n \to k = \{ 0, \dots, k-1 \}$. A set $H \subseteq X$ is **homogeneous** for $f$ if $f$ is constant on $[H]^n$; the constant value is the **color** of $H$ (when $|H| \geq n$).

:::definition{#def-rt}
$\mathsf{RT}^n_k$ is the statement: every coloring $f : [\nat]^n \to k$ has an infinite homogeneous set.
:::

:::example{#ex-rt-colorings}
1. Let $f(\{ x, y \}) = 1$ if $x$ and $y$ have the same parity, and $0$ otherwise. The even numbers and the odd numbers form infinite homogeneous sets of color $1$. A homogeneous set of color $0$ has at most two elements, since among three numbers two have the same parity. So the color of an infinite homogeneous set cannot be prescribed in advance.
2. The number of colors must be finite. Let $f(\{ x, y \}) = \min(x, y)$, a coloring of $[\nat]^2$ with infinitely many colors. For $x < y < z$, $f(\{ x, y \}) = x \neq y = f(\{ y, z \})$, so no homogeneous set has three elements.
3. For $n = 1$, a coloring is a function $f : \nat \to k$, and the theorem says that some color is taken infinitely often. This is the **infinite pigeonhole principle**.
:::

In reverse mathematics, colorings and homogeneous sets are sets, and $\mathsf{RT}^n_k$ is a $\Pi^1_2$ statement. In computability theory, one asks how complex homogeneous sets must be relative to $f$.

:::proposition{#prop-rt-basic}
1. $\mathsf{RCA}_0$ proves $\mathsf{RT}^1_k$ for every standard $k$.
2. Over $\mathsf{RCA}_0$, $\mathsf{RT}^n_2$ implies its version for colorings of $[X]^n$, for every infinite set $X$.
3. For every standard $n \geq 1$ and $k \geq 2$, $\mathsf{RCA}_0$ proves $\mathsf{RT}^n_2 \rightarrow \mathsf{RT}^n_k$.
:::

:::proof{of=prop-rt-basic}
1. For $f : \nat \to k$, the sets $C_i = \{ x : f(x) = i \}$ exist. If all were finite, bounded by $b_i$, then $\max_i b_i$ would bound $\nat$. So some $C_i$ is infinite, and it is homogeneous.
2. Let $p$ enumerate $X$ in increasing order; it exists in $\mathsf{RCA}_0$ when $X$ is infinite. Apply $\mathsf{RT}^n_2$ to $g(\{ x_1, \dots, x_n \}) = f(\{ p(x_1), \dots, p(x_n) \})$, and take the image of a homogeneous set under $p$.
3. By induction on $k$ in the metatheory. Given $f : [\nat]^n \to k + 1$, merge the colors $k - 1$ and $k$, and apply $\mathsf{RT}^n_k$ to obtain an infinite $H$. If its color is less than $k - 1$, $H$ is homogeneous for $f$; otherwise $f$ takes only the values $k - 1$ and $k$ on $[H]^n$, and (2) gives a homogeneous subset.
:::

The number of colors is irrelevant for provability, as long as it is a fixed standard number; we focus on two colors. The induction in (3) is carried out outside $\mathsf{RCA}_0$, one $k$ at a time: whether $\mathsf{RCA}_0$ proves $\forall k\, \mathsf{RT}^1_k$ is a question about induction, answered in the course on induction and conservation.

## Pre-homogeneous sets and the upper bound

The classical proof of Ramsey's theorem for $(n+1)$-tuples chooses elements $a_0 < a_1 < \cdots$ one at a time. After $a_i$ is chosen, it applies $\mathsf{RT}^n$ to the coloring $\vec x \mapsto f(\{ a_i \} \cup \vec x)$ of the remaining candidates, and keeps an infinite homogeneous set as the new reservoir of candidates. The color of a tuple then depends only on its least element, and the pigeonhole principle finishes the proof. From the point of view of complexity, this is expensive: each reservoir is obtained by an application of the $n$ case relative to the previous reservoir, and the complexity accumulates along the whole construction (see :ref{#ex-classical-ramsey-proof} for the case of pairs).

The proof of Erdős and Radó reverses the roles. It makes the color of an $(n+1)$-tuple depend only on its **first $n$ elements**, using only applications of the pigeonhole principle, which are organized in a single finitely branching tree. A single application of the $n$ case then finishes the proof.

:::definition{#def-pre-homogeneous}
A set $X$ is **pre-homogeneous** for $f : [\nat]^{n+1} \to k$ if, for all $x_1 < \cdots < x_n$ in $X$, the color $f(\{ x_1, \dots, x_n, y \})$ is the same for all $y \in X$ with $y > x_n$.
:::

On an infinite pre-homogeneous set $X$, the **induced coloring** $g(\{ x_1, \dots, x_n \}) = f(\{ x_1, \dots, x_n, y \})$, for any $y \in X$ above $x_n$, is well defined and computable in $f \oplus X$, and every set $H \subseteq X$ homogeneous for $g$ is homogeneous for $f$. For instance, for the coloring $f(\{ x, y \}) = 1$ if $\min(x, y)$ is even, and $0$ otherwise, every set is pre-homogeneous, with induced coloring $g(x) = 1$ if $x$ is even; the even numbers form a homogeneous set for $g$, hence for $f$. For the parity coloring of :ref{#ex-rt-colorings}, the set $\{ 0, 1, 2 \}$ is not pre-homogeneous, since $f(\{ 0, 1 \}) = 0 \neq 1 = f(\{ 0, 2 \})$, while the even numbers are. In general a pre-homogeneous set must be built.

:::proposition[Erdős, Radó]{#prop-erdos-rado-tree}
For every coloring $f : [\nat]^{n+1} \to k$, there is an infinite, finitely branching, $f$-computable tree $T \subseteq \nat^{<\nat}$ of strictly increasing sequences whose infinite paths are pre-homogeneous for $f$. Every set PA relative to $f'$ computes an infinite pre-homogeneous set for $f$.
:::

:::proof{of=prop-erdos-rado-tree}
We build $T$ by inserting the numbers $0, 1, 2, \dots$ one at a time. The first $n$ numbers form a single branch $\langle 0, 1, \dots, n - 1 \rangle$. To insert $s \geq n$, start at this branch and descend: at a node $\sigma$, call **pattern** of a number $a$ over $\sigma$ the tuple of colors $f(\{ \sigma(m_1), \dots, \sigma(m_n), a \})$ for $m_1 < \cdots < m_n < |\sigma|$. If $\sigma$ has an immediate successor $\sigma\, a$ in the current tree such that $a$ and $s$ have the same pattern over $\sigma$, move to $\sigma\, a$; otherwise add $\sigma\, s$ to the tree and stop.

*$T$ is $f$-computable and infinite.* To decide whether a sequence $\sigma\, s$ belongs to $T$, simulate the insertion of $0, \dots, s$. Every number is inserted, so $T$ is infinite.

*$T$ is finitely branching.* Two immediate successors $\sigma a$ and $\sigma b$ of a node, with $a < b$, have different patterns over $\sigma$: otherwise $b$ would have moved to $\sigma a$ instead of creating $\sigma b$. So $\sigma$ has at most $k^{\binom{|\sigma|}{n}}$ successors.

*Paths are pre-homogeneous.* Let $P$ be an infinite path, $j < j'$, $a = P(j)$ and $b = P(j')$. When $b$ was inserted, it descended along $P \uh j'$, hence moved from $P \uh j$ to $P \uh (j + 1) = (P \uh j)\, a$, so $a$ and $b$ have the same pattern over $P \uh j$. For $x_1 < \cdots < x_n$ in the range of $P$, at positions $m_1 < \cdots < m_n$, and $y = P(j)$, $y' = P(j')$ with $m_n < j < j'$, this gives $f(\{ x_1, \dots, x_n, y \}) = f(\{ x_1, \dots, x_n, y' \})$.

*Computing a path.* The number of successors of each node is bounded, but their values are not: whether $\sigma$ has a successor above a given number is a $\Sigma^0_1(f)$ question. With $f'$, one computes, for each node, the finite list of its successors. Coding each successor by its rank in this list, the paths of $T$ correspond, computably in $f'$, to the paths of an $f'$-computable tree in $\prod_\sigma k^{\binom{|\sigma|}{n}}$, a $\Pi^0_1(f')$ class after coding into Cantor space. It is non-empty by König's lemma. A set PA relative to $f'$ computes a member of it (:ref{#thm-pa-characterization}, relativized), and it computes $f'$ itself (:ref{#ex-pa-relative}, relativized to $f'$), so it computes a path of $T$.
:::

:::figure[The Erdős–Radó tree of the coloring of pairs $f(\{ x, y \}) = 1$ if $x + 2$ divides $y$, and $0$ otherwise, after the insertion of $0, \dots, 13$. A node $\sigma a$ is labeled $a$; the digits next to it are its pattern over $\sigma$. For instance, $13$ descends from $0$ to $1$ (pattern $0$), to $5$ (pattern $00$), to $11$ (pattern $000$), and creates a new node, since $11$ has no successor yet. Along the highlighted branch, the color of $\{ x, y \}$ does not depend on the larger element $y$.]
<svg class="fig" viewBox="0 0 600 330" width="600" role="img" aria-label="The Erdős–Radó tree of a coloring of pairs after the insertion of the numbers 0 to 13"><line x1="300.0" y1="41" x2="132.0" y2="75" class="accent-stroke" stroke-width="2.2"/><line x1="300.0" y1="41" x2="468.0" y2="75" class="ink-stroke" stroke-width="1.2"/><line x1="132.0" y1="97" x2="60.0" y2="131" class="ink-stroke" stroke-width="1.2"/><line x1="132.0" y1="97" x2="204.0" y2="131" class="accent-stroke" stroke-width="2.2"/><line x1="468.0" y1="97" x2="396.0" y2="131" class="ink-stroke" stroke-width="1.2"/><line x1="468.0" y1="97" x2="540.0" y2="131" class="ink-stroke" stroke-width="1.2"/><line x1="60.0" y1="153" x2="60.0" y2="187" class="ink-stroke" stroke-width="1.2"/><line x1="204.0" y1="153" x2="156.0" y2="187" class="ink-stroke" stroke-width="1.2"/><line x1="204.0" y1="153" x2="252.0" y2="187" class="accent-stroke" stroke-width="2.2"/><line x1="396.0" y1="153" x2="348.0" y2="187" class="ink-stroke" stroke-width="1.2"/><line x1="396.0" y1="153" x2="444.0" y2="187" class="ink-stroke" stroke-width="1.2"/><line x1="540.0" y1="153" x2="540.0" y2="187" class="ink-stroke" stroke-width="1.2"/><line x1="252.0" y1="209" x2="252.0" y2="243" class="accent-stroke" stroke-width="2.2"/><circle cx="300.0" cy="30" r="11" class="head-cell"/><text x="300.0" y="35" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="132.0" cy="86" r="11" class="head-cell"/><text x="132.0" y="91" text-anchor="middle" class="mrm" font-size="13">1</text><text x="147.0" y="78" class="mrm muted" font-size="10">0</text><circle cx="468.0" cy="86" r="11" class="node"/><text x="468.0" y="91" text-anchor="middle" class="mrm" font-size="13">2</text><text x="483.0" y="78" class="mrm muted" font-size="10">1</text><circle cx="60.0" cy="142" r="11" class="node"/><text x="60.0" y="147" text-anchor="middle" class="mrm" font-size="13">3</text><text x="75.0" y="134" class="mrm muted" font-size="10">01</text><circle cx="204.0" cy="142" r="11" class="head-cell"/><text x="204.0" y="147" text-anchor="middle" class="mrm" font-size="13">5</text><text x="219.0" y="134" class="mrm muted" font-size="10">00</text><circle cx="396.0" cy="142" r="11" class="node"/><text x="396.0" y="147" text-anchor="middle" class="mrm" font-size="13">4</text><text x="411.0" y="134" class="mrm muted" font-size="10">11</text><circle cx="540.0" cy="142" r="11" class="node"/><text x="540.0" y="147" text-anchor="middle" class="mrm" font-size="13">6</text><text x="555.0" y="134" class="mrm muted" font-size="10">10</text><circle cx="60.0" cy="198" r="11" class="node"/><text x="60.0" y="203" text-anchor="middle" class="mrm" font-size="13">9</text><text x="75.0" y="190" class="mrm muted" font-size="10">010</text><circle cx="156.0" cy="198" r="11" class="node"/><text x="156.0" y="203" text-anchor="middle" class="mrm" font-size="13">7</text><text x="171.0" y="190" class="mrm muted" font-size="10">001</text><circle cx="252.0" cy="198" r="11" class="head-cell"/><text x="252.0" y="203" text-anchor="middle" class="mrm" font-size="13">11</text><text x="267.0" y="190" class="mrm muted" font-size="10">000</text><circle cx="348.0" cy="198" r="11" class="node"/><text x="348.0" y="203" text-anchor="middle" class="mrm" font-size="13">8</text><text x="363.0" y="190" class="mrm muted" font-size="10">110</text><circle cx="444.0" cy="198" r="11" class="node"/><text x="444.0" y="203" text-anchor="middle" class="mrm" font-size="13">12</text><text x="459.0" y="190" class="mrm muted" font-size="10">111</text><circle cx="540.0" cy="198" r="11" class="node"/><text x="540.0" y="203" text-anchor="middle" class="mrm" font-size="13">10</text><text x="555.0" y="190" class="mrm muted" font-size="10">100</text><circle cx="252.0" cy="254" r="11" class="head-cell"/><text x="252.0" y="259" text-anchor="middle" class="mrm" font-size="13">13</text><text x="267.0" y="246" class="mrm muted" font-size="10">0001</text><text x="60.0" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="156.0" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="348.0" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="444.0" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="540.0" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="252.0" y="282" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="20" y="300" class="label">small digits: the pattern of a node over its parent σ, the colors of its pairs with σ(0), σ(1), …</text><text x="20" y="318" class="label">highlighted: the branch 0, 1, 5, 11, 13, pre-homogeneous so far</text></svg>
:::

The last step of the proof is :ref{#thm-konig-strength} relativized to $f$. The tree is computable and all its paths are good; the only difficulty is that it is finitely branching without a computable bound on the values of the successors, which in general costs one jump (:ref{#thm-finitely-branching-jump}).

:::theorem[Jockusch]{#thm-jockusch-upper}
For every $n \geq 1$, every coloring $f : [\nat]^n \to k$ has an infinite homogeneous set computable in every set that is PA relative to $f^{(n-1)}$. In particular, every computable coloring of $[\nat]^n$ has an infinite homogeneous set computable in $\emptyset^{(n)}$.
:::

:::proof{of=thm-jockusch-upper}
By induction on $n$, for all colorings $f$ simultaneously. For $n = 1$, $f$ itself computes a homogeneous set, and a set PA relative to $f$ computes $f$.

For $n = 2$, let $P$ be PA relative to $f'$. By :ref{#prop-erdos-rado-tree}, $P$ computes an infinite pre-homogeneous set $X$, the induced coloring $g$ of $[X]^1$ is computable in $P$, and so is a homogeneous set for $g$, which is homogeneous for $f$.

For $n + 1$ with $n \geq 2$, let $P_1$ be PA relative to $f^{(n)}$. By the low basis theorem relativized to $f'$, there is $P_0$ PA relative to $f'$ with $P_0' \leq_T f''$; then $P_0^{(n-1)} \leq_T f^{(n)}$, since $n - 1 \geq 1$. $P_0$ computes an infinite pre-homogeneous set $X$ and the induced coloring $g$ of $[X]^n$, so $g^{(n-1)} \leq_T P_0^{(n-1)} \leq_T f^{(n)}$, and $P_1$ is PA relative to $g^{(n-1)}$. By the induction hypothesis, applied to $g$ transported to $[\nat]^n$ through the enumeration of $X$, $P_1$ computes an infinite homogeneous set for the transported coloring; its image under the enumeration of $X$ is computable in $P_1$, since $X \leq_T P_0 \leq_T f'' \leq_T P_1$, and it is homogeneous for $g$, hence for $f$.

For the last statement, $\emptyset^{(n)}$ is PA relative to $\emptyset^{(n-1)}$: it computes a $\{0, 1\}$-valued function DNC relative to $\emptyset^{(n-1)}$.
:::

The proof uses two techniques of the course on Π⁰₁ classes: **basis theorems**, here the low basis theorem relativized, to keep the jumps of the intermediate sets under control, and the universality of PA degrees, which allows one oracle to compute a member of every non-empty class at the relevant level.

Jockusch proved more precisely that every computable coloring of $[\nat]^n$ has a $\Pi^0_n$ infinite homogeneous set. For pairs, one builds, computably in $\emptyset'$, an infinite pre-homogeneous set together with the set of its elements of a given limit color so that both are $\Pi^0_2$; we do not reproduce the construction (Jockusch 1972; Dzhafarov–Mummert, Lemma 8.1.2 and Theorem 8.1.1).

:::quiz[the Erdős–Radó tree]
In the proof of :ref{#prop-erdos-rado-tree}, why is $f'$ needed to compute a path, although the tree is $f$-computable and finitely branching?

- [x] Because the number of successors of a node is bounded, but not their values: deciding whether a node has a successor above a given number is a $\Sigma^0_1(f)$ question, and $f'$ is needed to list the successors.
- [ ] Because the tree is not $f$-computable.

  Membership in the tree is decided by simulating the insertion process.
- [ ] Because pre-homogeneity is a $\Pi^0_2$ property.

  Every path is pre-homogeneous; the issue is to find a path.

---

In the proof of :ref{#thm-jockusch-upper}, why is the case $n = 2$ treated separately?

- [x] Because the inequality $P_0^{(n-1)} \leq_T f^{(n)}$ obtained from $P_0' \leq_T f''$ requires $n - 1 \geq 1$; for pairs, a single set PA relative to $f'$ computes both the pre-homogeneous set and the homogeneous set.
- [ ] Because $\mathsf{RT}^2_2$ is not provable in $\mathsf{ACA}_0$.

  It is provable in $\mathsf{ACA}_0$; the case distinction concerns the jump inequalities.
- [ ] Because the Erdős–Radó tree does not exist for pairs.

  It exists for every $n$.
:::

::::exercise{#ex-homogeneous-jump-bound difficulty=1 objective="Combine the upper bound with the low basis theorem to bound the jump of a homogeneous set."}
Show that every computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ with $H' \leq_T \emptyset''$.

:::solution
By the low basis theorem relativized to $\emptyset'$, there is a set $P$ PA relative to $\emptyset'$ with $P' \leq_T \emptyset''$. By :ref{#thm-jockusch-upper}, $P$ computes an infinite homogeneous set $H$, and $H' \leq_T P' \leq_T \emptyset''$.
:::
::::

::::exercise{#ex-classical-ramsey-proof difficulty=2 objective="Measure the complexity of the classical proof of Ramsey's theorem and see why it accumulates jumps."}
Carry out the classical proof described at the beginning of this section for a computable coloring $f : [\nat]^2 \to 2$, and show that it produces an infinite homogeneous set computable in $\emptyset''$. Explain why the same proof, for colorings of triples, gives no arithmetic bound.

:::solution
Let $I_0 = \nat$. Given an infinite computable set $I_i$, let $a_i = \min I_i$ and choose $c_i < 2$ such that $I_{i+1} = \{ y \in I_i : y > a_i,\ f(\{ a_i, y \}) = c_i \}$ is infinite; one of the two values works. Each $I_{i+1}$ is computable, uniformly in the previous choices, and whether a computable set given by an index is infinite is a $\Pi^0_2$ question, answered by $\emptyset''$. So the sequences $(a_i)$ and $(c_i)$ are computable in $\emptyset''$. For $i < j$, $a_j \in I_{i+1}$, so $f(\{ a_i, a_j \}) = c_i$. One of the sets $\{ a_i : c_i = 0 \}$ and $\{ a_i : c_i = 1 \}$ is infinite; it is homogeneous and computable in $\emptyset''$.

For triples, the reservoir $I_{i+1}$ is an infinite homogeneous set for the coloring $\{ y, z \} \mapsto f(\{ a_i, y, z \})$ restricted to $I_i$, which is only $I_i$-computable. The case of pairs relativized to $I_i$ gives $I_{i+1} \leq_T I_i''$, so the bound on $I_i$ grows by two jumps at each step, and the construction of the whole sequence is not bounded by any finite jump.
:::
::::

## Notes and references

Ramsey (1930) proved his theorem as a lemma in a decision procedure for a fragment of first-order logic. The tree argument is due to Erdős and Radó (1956), and Jockusch (1972) obtained the upper bounds of this lesson. Hirschfeldt compares the three classical proofs of Ramsey's theorem from the point of view of their complexity (*Slicing the Truth*, §6.1; the classical proof, its ∅″ bound for pairs as Exercise 6.4, and a tree proof close to the one above) and proves the upper bounds in §6.2 (Theorems 6.9, 6.20 and 6.21). Dzhafarov and Mummert treat the upper bounds in §8.1, including the $\Pi^0_n$ bound (Theorem 8.1.1). Monin and Patey treat the same material in the section *Ramsey's theorem in the arithmetic hierarchy* of their chapter *Ramsey's theorem*.

- F. P. Ramsey, *On a problem of formal logic*, Proceedings of the London Mathematical Society (2) 30 (1930), 264–286.
- P. Erdős and R. Rado, *A partition calculus in set theory*, Bulletin of the American Mathematical Society 62 (1956), 427–489.
- C. G. Jockusch, Jr., *Ramsey's theorem and recursion theory*, Journal of Symbolic Logic 37 (1972), 268–280.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.

:::::exercises
::::exercise{#ex-er-tree-examples difficulty=1 objective="Compute the Erdős–Radó tree of two colorings of pairs and read homogeneous sets off its paths."}
Compute the Erdős–Radó tree of :ref{#prop-erdos-rado-tree} for the following colorings of pairs, determine its infinite paths and, for each path, the induced coloring and an infinite homogeneous set.

1. The parity coloring of :ref{#ex-rt-colorings}: $f(\{ x, y \}) = 1$ if $x$ and $y$ have the same parity, and $0$ otherwise.
2. A coloring with $f(\{ x, y \}) = g(x)$ for $x < y$, where $g : \nat \to 2$ is a fixed function.

:::solution
Here $n = 1$: the tree starts with the branch $\langle 0 \rangle$, and the pattern of $a$ over a node $\sigma$ is the tuple $(f(\{ \sigma(m), a \}))_{m < |\sigma|}$.

1. We show by induction on $s \geq 2$ that, after the insertion of $0, \dots, s$, the tree consists of the two branches $\langle 0, 1, 3, 5, \dots \rangle$, listing $0$ and the odd numbers up to $s$, and $\langle 0, 2, 4, \dots \rangle$, listing the even numbers up to $s$. The number $1$ creates $\langle 0, 1 \rangle$, and $2$, whose pattern $f(\{ 0, 2 \}) = 1$ over $\langle 0 \rangle$ differs from the pattern $0$ of $1$, creates $\langle 0, 2 \rangle$. For $s \geq 3$ odd, the pattern of $s$ over $\langle 0 \rangle$ is $0$, that of $1$, so $s$ moves to $\langle 0, 1 \rangle$. Over a node $\sigma$ of the odd branch, every odd number $a > \max \sigma$ has the pattern $(0, 1, \dots, 1)$: color $0$ with $0$ and $1$ with the odd entries. So $s$ has the same pattern as the unique successor of each node of the odd branch, descends to its last node, and creates a new node there. The case of $s$ even is symmetric: over a node of the even branch, every even $a$ has the pattern $(1, \dots, 1)$.

   The infinite paths are $P_1 = \{ 0 \} \cup \{ \text{odd numbers} \}$ and $P_2 = \{ \text{even numbers} \}$. On $P_1$, the induced coloring is $g(0) = 0$ and $g(x) = 1$ for $x$ odd; the odd numbers are homogeneous for it, hence for $f$, with color $1$. On $P_2$, the induced coloring is constantly $1$, and $P_2$ itself is homogeneous.
2. The pattern of $a$ over $\sigma$ is $(g(\sigma(0)), \dots, g(\sigma(|\sigma| - 1)))$, which does not depend on $a$. By induction on $s$, the tree after the insertion of $0, \dots, s$ is the single branch $\langle 0, 1, \dots, s \rangle$: the number $s$ has the same pattern as the unique successor of each node, descends to the node $\langle 0, \dots, s - 1 \rangle$, which has no successor, and creates $\langle 0, \dots, s \rangle$. The only infinite path is $\nat$, so every set is pre-homogeneous, with induced coloring $g$, and $\{ x : g(x) = i \}$ is an infinite homogeneous set for a value $i$ taken infinitely often.
:::
::::

::::exercise{#ex-prehomogeneous-larger difficulty=1 objective="Check the definition of pre-homogeneity on colorings of pairs that depend only on the larger element."}
Let $g : \nat \to 2$ and $f(\{ x, y \}) = g(y)$ for $x < y$.

1. Show that a set $X$ is pre-homogeneous for $f$ if and only if $g$ is constant on $X \setminus \{ \min X \}$.
2. Show that every infinite pre-homogeneous set for $f$ is homogeneous for $f$.
3. Show, for an arbitrary coloring $h : [\nat]^{n+1} \to k$, that every subset of a pre-homogeneous set is pre-homogeneous, with the restricted induced coloring.

:::solution
1. $X$ is pre-homogeneous if and only if, for every $x \in X$, the value $g(y)$ is the same for all $y \in X$ with $y > x$. If $g$ is constant on $X \setminus \{ \min X \}$, this holds, since every $y \in X$ above some $x \in X$ differs from $\min X$. Conversely, taking $x = \min X$ shows that $g$ is constant on $X \setminus \{ \min X \}$ (the empty set is pre-homogeneous and satisfies both conditions).
2. Let $X$ be infinite and pre-homogeneous, and $c$ the constant value of $g$ on $X \setminus \{ \min X \}$. For $x < y$ in $X$, $y \neq \min X$, so $f(\{ x, y \}) = g(y) = c$.
3. Let $X$ be pre-homogeneous for $h$ and $Y \subseteq X$. For $x_1 < \cdots < x_n$ in $Y$ and $y, y'$ in $Y$ above $x_n$, all these numbers belong to $X$, so $h(\{ x_1, \dots, x_n, y \}) = h(\{ x_1, \dots, x_n, y' \})$. The induced coloring of $Y$ is the restriction of that of $X$ to $[Y]^n$.
:::
::::

::::exercise{#ex-rt-four-colors difficulty=1 objective="Reduce four colors to two by applying Ramsey's theorem to the binary digits of the colors."}
Prove in $\mathsf{RCA}_0$ that $\mathsf{RT}^n_2$ implies $\mathsf{RT}^n_4$, by applying $\mathsf{RT}^n_2$ to the two binary digits of the colors. Deduce that $\mathsf{RT}^n_2$ implies $\mathsf{RT}^n_{2^m}$ for every standard $m$.

:::solution
Let $f : [\nat]^n \to 4$, and write $f = 2 b_1 + b_0$ with $b_0, b_1 : [\nat]^n \to 2$, which exist by $\Delta^0_1$ comprehension. By $\mathsf{RT}^n_2$, $b_1$ has an infinite homogeneous set $H_1$. By :ref{#prop-rt-basic} (2), the restriction of $b_0$ to $[H_1]^n$ has an infinite homogeneous set $H \subseteq H_1$. On $[H]^n$, both digits are constant, so $f$ is constant.

For $2^m$ colors, argue by induction on $m$ in the metatheory: a coloring $f$ with $2^{m+1}$ colors is $f = 2^{m} b + r$ with $b < 2$ and $r < 2^m$; apply $\mathsf{RT}^n_2$ to $b$, then the induction hypothesis to $r$ restricted to the homogeneous set, through :ref{#prop-rt-basic} (2). Compared with the proof of :ref{#prop-rt-basic} (3), the number of applications of $\mathsf{RT}^n_2$ is $m$ instead of $2^m - 1$. Compare Hirschfeldt, *Slicing the Truth*, Exercise 6.2.
:::
::::

::::exercise{#ex-infinite-colors-canonical difficulty=1 objective="See what survives of the pigeonhole principle when the number of colors is infinite."}
Show that for every function $f : \nat \to \nat$, there is an infinite set $H$, computable in $f$, on which $f$ is either constant or injective.

:::solution
If some value $c$ is taken infinitely often, $H = \{ x : f(x) = c \}$ is infinite, computable in $f$, and $f$ is constant on it. Otherwise every fiber $f^{-1}(c)$ is finite. Let $x_0 = 0$ and $x_{j+1}$ be the least $x > x_j$ with $f(x) \notin \{ f(x_0), \dots, f(x_j) \}$: it exists, since the union of the fibers of $f(x_0), \dots, f(x_j)$ is finite. The set $H = \{ x_j : j \in \nat \}$ is infinite, computable in $f$, and $f$ is injective on it. The choice between the two cases is not effective, but each case gives an $f$-computable set. This is the case $n = 1$ of the canonical Ramsey theorem of Erdős and Rado: the min-coloring of :ref{#ex-rt-colorings} shows that for pairs, constant and injective are not the only possible behaviors.
:::
::::

::::exercise{#ex-er-tree-path-0pp difficulty=2 objective="Compute a path through a finitely branching tree with two jumps, without PA degrees."}
Let $f : [\nat]^{n+1} \to k$ be computable and $T$ its Erdős–Radó tree. Show directly, without using PA degrees, that $\emptyset''$ computes an infinite path of $T$.

:::solution
Call a node $\tau \in T$ **extendible** if it has extensions in $T$ of arbitrarily large length. The tree $T$ is computable, so "some node of length at least $m$ extends $\tau$" is a $\Sigma^0_1$ property of $(\tau, m)$, extendibility is $\Pi^0_2$, and $\emptyset''$ decides it.

The initial branch $\langle 0, \dots, n - 1 \rangle$ is extendible: $T$ is infinite and each of its levels is finite, since $T$ is finitely branching, so $T$ has nodes of every length, and those of length at least $n$ extend the initial branch. Every extendible node $\tau$ has an extendible immediate successor: otherwise each of its finitely many successors $\tau a_1, \dots, \tau a_r$ has a bound $m_j$ on the lengths of its extensions, and a node extending $\tau$ of length larger than $|\tau|$ and than every $m_j$ would extend some $\tau a_j$, which is impossible.

Define the path $P$ computably in $\emptyset''$: starting from the initial branch, at an extendible node $\tau$, search through $a = 0, 1, 2, \dots$ for the least $a$ with $\tau a \in T$ and $\tau a$ extendible, and move to $\tau a$. The search terminates by the previous paragraph. The union of these nodes is an infinite path of $T$, hence an infinite pre-homogeneous set. Compared with :ref{#prop-erdos-rado-tree}, $\emptyset''$ is PA relative to $\emptyset'$, so the bound is the same; the proof avoids PA degrees but gives no low or cone-avoiding paths.
:::
::::
:::::
