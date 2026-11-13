---
title: Separating the Erdős–Moser theorem from Ramsey's theorem for pairs
summary: A computable stable coloring of pairs, built from a Δ⁰₂ partition into two hyperimmune sets, defeats two hyperimmunities, so SRT²₂ does not follow from EM; RT²₂ is EM plus ADS, so ADS does not follow from EM either.
duration: 35
prerequisites: [erdos-moser-hyperimmunities, turing-degrees/limit-computability]
---

The previous lesson proved that $\mathsf{EM}$ preserves countably many hyperimmunities at once, while the disjunctive question of $\mathsf{RT}^2_2$ preserves one. This lesson gives the second half of the separation (:ref{to="separation-design/custom-properties"}): an instance of $\mathsf{RT}^2_2$, computable and even stable, all of whose solutions destroy one of two given hyperimmunities. It then splits $\mathsf{RT}^2_2$ into $\mathsf{EM}$ and the ascending–descending sequence principle, which yields a second separation without further work.

## Ramsey's theorem for pairs does not preserve two hyperimmunities

The separating instance comes from a $\Delta^0_2$ partition of $\nat$ into two hyperimmune sets, through a stable coloring. The partition is built by a finite extension argument with oracle $\emptyset'$: each requirement asks a $\Sigma^0_1$ question about a candidate array, and either finds a block far enough to be put on the other side, or learns that the candidate is not an array.

:::lemma{#lem-sd-bihyperimmune}
There is a $\Delta^0_2$ set $A$ such that $A$ and $\overline A$ are hyperimmune.
:::

:::proof{of=lem-sd-bihyperimmune}
Write $A^0 = A$ and $A^1 = \overline A$. We build $A$ by finite extensions $\sigma_0 \preceq \sigma_1 \preceq \cdots$ computed with oracle $\emptyset'$, satisfying for each $e$ and $i < 2$ the requirement $R_{e,i}$: if $\Phi_e$ is a disjoint strong array $(F_n)$, then $F_n \cap A^i = \emptyset$ for some $n$. At the step for $R_{e,i}$, with current string $\sigma$, ask $\emptyset'$ whether there is $n$ with $\Phi_e(n)\converge$ and $F_n$ empty or $\min F_n \geq |\sigma|$, a $\Sigma^0_1$ question. If so, find such an $n$ and extend $\sigma$ so that the elements of $F_n$ are outside $A^i$, the positions in between being set to $0$; this satisfies $R_{e,i}$. If not, $\Phi_e$ is not a disjoint strong array, and $R_{e,i}$ holds vacuously: a total sequence of pairwise disjoint finite sets has only finitely many members meeting $[0, |\sigma|)$. In both cases, then append the bits $1$ and $0$, adding one element to $A$ and one to $\overline A$. The construction is computable in $\emptyset'$, so $A$ is $\Delta^0_2$; $A$ and $\overline A$ are infinite by the last clause, and every requirement is satisfied.
:::

:::proposition{#prop-sd-rt22-two}
There are two hyperimmune functions $h_0, h_1$ and a computable stable coloring $f : [\nat]^2 \to 2$ such that, for each $i < 2$, $h_i$ is not $H$-hyperimmune for any infinite set $H$ homogeneous for $f$ with color $i$. So $\mathsf{RT}^2_2$, and even its restriction $\mathsf{SRT}^2_2$ to stable colorings, does not admit preservation of $2$ hyperimmunities.
:::

:::proof{of=prop-sd-rt22-two}
Let $A$ be as in :ref{#lem-sd-bihyperimmune}, with a computable approximation $(A_s)$ (:ref{#thm-limit-lemma}), and let $f(\{ x, y \}) = A_y(x)$ for $x < y$. It is computable and stable, with limit $\lim_y f(\{ x, y \}) = A(x)$. Let $h_1 = p_A$ and $h_0 = p_{\overline A}$, the principal functions; they are hyperimmune by :ref{#thm-hyperimmune-principal}. If $H$ is infinite and homogeneous with color $1$, every $x \in H$ has $f(\{ x, y \}) = 1$ for the infinitely many $y > x$ in $H$, so $A(x) = 1$: $H \subseteq A$. Then $p_H(n) \geq p_A(n)$ for every $n$, and $p_H$, computable in $H$, dominates $h_1$. The case of color $0$ is symmetric.
:::

:::quiz[the stable coloring]
In the proof of :ref{#prop-sd-rt22-two}, why does an infinite set $H$ homogeneous with color $1$ make $h_1$ fail to be $H$-hyperimmune?

- [x] Because $H \subseteq A$ by stability, so the $n$-th element of $H$ is at least the $n$-th element of $A$, and $p_H$, computable in $H$, dominates $p_A = h_1$.
- [ ] Because $H$ computes $A$.

  It need not; a subset of $A$ is enough to compute a function dominating $p_A$.
- [ ] Because $A$ is $\Delta^0_2$.

  The complexity of $A$ makes $f$ computable; it plays no role in the domination.
:::

:::corollary[Lerman, Solomon, Towsner]{#cor-sd-em-not-srt22}
$\mathsf{SRT}^2_2 \not\leq_\omega \mathsf{EM}$: there is an ω-model of $\mathsf{RCA}_0 + \mathsf{EM}$ that is not a model of $\mathsf{SRT}^2_2$, hence not of $\mathsf{RT}^2_2$.
:::

:::proof{of=cor-sd-em-not-srt22}
Let $h_0, h_1$ be as in :ref{#prop-sd-rt22-two} and $\mathcal W$ the class of sets $W$ such that $h_0$ and $h_1$ are $W$-hyperimmune. By :ref{#thm-sd-em-hyperimmunities}, $\mathsf{EM}$ preserves $\mathcal W$. The set $\emptyset$ belongs to $\mathcal W$ and computes the stable coloring $f$, every solution $H$ of which has $H \notin \mathcal W$. So $\mathsf{SRT}^2_2$ does not preserve $\mathcal W$, and :ref{#thm-preservation-separation} applies.
:::

Cone avoidance, PA avoidance and preservation of one hyperimmunity, which both problems admit, do not see this separation; it only uses that the question of $\mathsf{RT}^2_2$ chooses its side.

## Ramsey's theorem as a conjunction

Let $\mathcal L = (\nat, <_{\mathcal L})$ be a linear order. As in :ref{to="lowness/stable-linear-orders"}, an **ascending sequence** is an infinite set on which $<_{\mathcal L}$ agrees with the order of $\nat$, and a **descending sequence** an infinite set on which it agrees with the reverse order. The **ascending–descending sequence principle** $\mathsf{ADS}$ is the problem whose instances are the linear orders on $\nat$ and whose solutions are their ascending and descending sequences; it is studied in :ref{to="separation-design/ascending-descending"}.

:::proposition{#prop-sd-rt22-em-ads}
A Turing ideal satisfies $\mathsf{RT}^2_2$ if and only if it satisfies $\mathsf{EM}$ and $\mathsf{ADS}$.
:::

:::proof{of=prop-sd-rt22-em-ads}
($\Rightarrow$) By :ref{#prop-sd-em-rt22}, and since a linear order $\mathcal L$ computes the coloring with $f(\{ x, y \}) = 1$ if and only if $x <_{\mathcal L} y$, for $x < y$, whose homogeneous sets are ascending (color $1$) or descending (color $0$). ($\Leftarrow$) Let $f$ be a coloring in the ideal, and $T$ the tournament with $T(x, y)$ if and only if $f(\{ x, y \}) = 1$, for $x < y$. Let $H$ be an infinite transitive set in the ideal, $h$ its enumeration in increasing order, and $\mathcal L$ the linear order on $\nat$ with $m <_{\mathcal L} n$ if and only if $T(h(m), h(n))$; it belongs to the ideal. Let $S$ be an ascending or descending sequence of $\mathcal L$ in the ideal. If $S$ is ascending, then for $m < n$ in $S$, $T(h(m), h(n))$ with $h(m) < h(n)$, so $f(\{ h(m), h(n) \}) = 1$; so $h[S]$ is homogeneous with color $1$. If $S$ is descending, $h[S]$ is homogeneous with color $0$.
:::

:::corollary[Lerman, Solomon, Towsner]{#cor-sd-ads-not-em}
$\mathsf{ADS} \not\leq_\omega \mathsf{EM}$.
:::

:::proof{of=cor-sd-ads-not-em}
Otherwise every Turing ideal satisfying $\mathsf{EM}$ would satisfy $\mathsf{ADS}$, hence $\mathsf{RT}^2_2$ by :ref{#prop-sd-rt22-em-ads}, contradicting :ref{#cor-sd-em-not-srt22}.
:::

So Ramsey's theorem for pairs splits into a part about transitivity and a part about orders. The first has the compactness of $\mathsf{RT}^2_2$: $\mathsf{EM}$ implies the Ramsey-type weak König lemma, by a theorem of Bienvenu, Patey and Shafer, and of Flood and Towsner, which we admit. The second has none: $\mathsf{ADS}$ follows from $\mathsf{CAC}$ (:ref{to="separation-design/ascending-descending"}), which does not even imply $\mathsf{DNC}$, as :ref{to="separation-design/separating-instances"} shows.

## Exercises

::::exercise{#exr-rt22-two-among-three difficulty=2}
Say that a problem $\mathsf P$ admits **preservation of $\ell$ among $k$ hyperimmunities** if for every set $Z$, all $Z$-hyperimmune functions $h_0, \dots, h_{k-1}$ and every instance $X \leq_T Z$, there are a solution $Y$ and a set $F \subseteq \{ 0, \dots, k - 1 \}$ with $\ell$ elements such that $h_j$ is $(Z \oplus Y)$-hyperimmune for every $j \in F$.

1. Show that $\mathsf{RT}^2_3$ does not admit preservation of $3$ among $3$ hyperimmunities.
2. Show that $\mathsf{RT}^2_2$ admits preservation of $2$ among $3$ hyperimmunities.

:::solution
1. As in :ref{#lem-sd-bihyperimmune}, build with oracle $\emptyset'$ a partition $\nat = A_0 \sqcup A_1 \sqcup A_2$ into three hyperimmune $\Delta^0_2$ sets: the requirement for $e$ and $i < 3$ puts the elements of the block found into $A_{i+1 \bmod 3}$, and each step adds one element to each part. Take computable approximations $(A_{0,s})$ and $(A_{1,s})$ of $A_0$ and $A_1$, and for $x < y$ let $f(\{ x, y \}) = 0$ if $x \in A_{0,y}$, $f(\{ x, y \}) = 1$ if $x \in A_{1,y} \setminus A_{0,y}$, and $f(\{ x, y \}) = 2$ otherwise. Then $\lim_y f(\{ x, y \}) = j$ for $x \in A_j$, and as in :ref{#prop-sd-rt22-two}, an infinite set $H$ homogeneous with color $j$ is contained in $A_j$, so $p_H$ dominates $h_j = p_{A_j}$. The functions $h_0, h_1, h_2$ are hyperimmune (:ref{#thm-hyperimmune-principal}), and every solution destroys one of them.

2. Let $h_0, h_1, h_2$ be $Z$-hyperimmune and $f$ a $Z$-computable coloring of pairs. By :ref{#exr-wkl-hyperimmunities} and :ref{#lem-scott-preservation}, there is a Scott ideal $\mathcal M$ containing $Z$ such that every $h_j$ is $X$-hyperimmune for every $X \in \mathcal M$. If an infinite homogeneous set for $f$ belongs to $\mathcal M$, it preserves the three hyperimmunities. Otherwise, run the construction of item 2 of :ref{#thm-hyperimmunity-examples} with reservoirs in $\mathcal M$ and, for each pair $(e_0, e_1)$ and each $j < 3$, a task forcing on some side $i$ that $\Phi^{Z \oplus G_i}_{e_i}$ is partial or below $h_j$ at some point. For each $j$, Lachlan's disjunction (:ref{#lem-disjunctive-construction}) gives a side $s(j)$ such that $h_j$ is $(Z \oplus G_{s(j)})$-hyperimmune. Two of the three indices $j$ have the same side $s$, and $G_s$ is the solution sought. The same argument gives $\lceil k/2 \rceil$ among $k$, for every $k$.
:::
::::

## Notes and references

The separation of $\mathsf{EM}$ from $\mathsf{RT}^2_2$ through preservation of hyperimmunities follows the section *Erdős–Moser theorem* of the chapter *Custom properties* of Patey's monograph and Patey (2017), who proves :ref{#prop-sd-rt22-two}; the monograph also states :ref{#exr-rt22-two-among-three}, from Patey's thesis. The separation itself is due to Lerman, Solomon and Towsner (2013), with an iterated forcing; their result gives an ω-model of $\mathsf{EM}$ that is not a model of $\mathsf{SRT}^2_2$ (Hirschfeldt, *Slicing the Truth*, Theorem 9.31). The decomposition $\mathsf{RT}^2_2 \leftrightarrow \mathsf{EM} \wedge \mathsf{ADS}$ over $\mathsf{RCA}_0$ is Exercise 9.30 of Hirschfeldt, "noted by several people", and is attributed to Montalbán by Bovykin and Weiermann (2017). That $\mathsf{EM}$ implies $\mathsf{RWKL}$ is due to Bienvenu, Patey and Shafer (2017), and independently to Flood and Towsner (2016).

- L. Patey, *Lowness and avoidance*, chapter *Custom properties*, section *Erdős–Moser theorem*.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- M. Lerman, R. Solomon and H. Towsner, *Separating principles below Ramsey's theorem for pairs*, Journal of Mathematical Logic 13 (2013), 1350007.
- A. Bovykin and A. Weiermann, *The strength of infinitary Ramseyan principles can be accessed by their densities*, Annals of Pure and Applied Logic 168 (2017), 1700–1709.
- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71.
- S. Flood and H. Towsner, *Separating principles below WKL₀*, Mathematical Logic Quarterly 62 (2016), 507–529.
- L. Patey, *The reverse mathematics of Ramsey-type theorems*, PhD thesis, Université Paris Diderot, 2016.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Section 9.2.2.
