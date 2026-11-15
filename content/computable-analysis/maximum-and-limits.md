---
title: The maximum and monotone convergence
summary: Finding a point where a continuous function attains its maximum is Weihrauch equivalent to weak König's lemma, and some computable functions attain their maximum only at non-computable points; the monotone convergence theorem is equivalent to the jump; a comparison of the classifications of the course with reverse mathematics.
duration: 40
prerequisites: [intermediate-value-theorem, pi01-classes/basis-theorems, big-five/aca0-reversals, reducibilities/parallelization]
---

The two theorems of this lesson are proved classically by compactness and by completeness. A continuous function on $[0, 1]$ attains its maximum: its maximum value is computable (:ref{#thm-modulus-max}), but a point where it is attained is found only through a use of compactness, and the problem is equivalent to weak König's lemma. A bounded non-decreasing sequence of reals converges: its limit is computed from the jump of the sequence, and the problem is equivalent to the jump; this is Specker's construction, made uniform. The lesson ends with a table of the classifications of the course and a comparison with reverse mathematics, where the same theorems are equivalent to $\mathsf{WKL}_0$ and $\mathsf{ACA}_0$.

## The maximum

:::definition{#def-max-problem}
The problem $\mathsf{MAX}$ has as instances all $f \in C[0, 1]$, represented by $\delta_C$, and as solutions to $f$ the points $x \in [0, 1]$ with $f(x) = \max_{y \in [0, 1]} f(y)$.
:::

:::theorem{#thm-max-wkl}
$\mathsf{MAX} \equiv_{sW} \mathsf{WKL}$.
:::

:::proof{of=thm-max-wkl}
($\mathsf{MAX} \leq_{sW} \mathsf C_{[0,1]}$) Given $f$, compute $M = \max f$ by :ref{#thm-modulus-max} and a rectangle name of $f$ by :ref{#thm-cauchy-rectangle}. List the intervals $(a - r, a + r)$ of the listed rectangles $(a, r, b, s)$ with $b + s < M$; this condition is semi-decidable by :ref{#prop-order-undecidable}, so the list is computed by dovetailing (repeating an empty pair while nothing has been found). On such an interval $f \leq b + s < M$. Conversely, if $f(x) < M$, a listed rectangle with $|x - a| < r$ and $s < (M - f(x))/2$ satisfies $b + s \leq f(x) + 2s < M$. So the list is a $\psi_>$-name of the set of maximum points, which is non-empty, and every point of it is a solution. By :ref{#thm-closed-choice-wkl}, $\mathsf{MAX} \leq_{sW} \mathsf{WKL}$.

($\mathsf C_{[0,1]} \leq_{sW} \mathsf{MAX}$) Given a name of a non-empty closed $A$, compute $f \geq 0$ with $f^{-1}(0) = A$ by :ref{#thm-zero-sets}, and its opposite $-f$. Since $A \neq \emptyset$, the maximum of $-f$ is $0$, attained exactly on $A$. So the maximum points of $-f$ are the points of $A$, and the backward functional is the identity.
:::

The classical existence proof of a maximum point takes the supremum and uses compactness to find a point where it is attained. The first reduction follows the same path, and isolates the use of compactness in a single instance of closed choice. The theorem has non-uniform consequences, obtained by applying the reductions to computable instances.

:::corollary{#cor-max-points}
1. There is a computable $f \in C[0, 1]$ whose maximum is attained only at non-computable points.
2. Every computable $f \in C[0, 1]$ attains its maximum at a low point, that is, a point with a Cauchy name of low Turing degree.
:::

:::proof{of=cor-max-points}
1. Let $T$ be an infinite computable binary tree with no computable path (:ref{#thm-dnc2-no-computable}). The forward functionals of :ref{#thm-closed-choice-wkl} and :ref{#thm-max-wkl} turn $T$ into a computable instance $f$ of $\mathsf{MAX}$: the composition of the reductions $\mathsf{WKL} \leq_{sW} \mathsf C_{[0,1]} \leq_{sW} \mathsf{MAX}$. If $f$ had a computable maximum point, the backward functionals would compute a path through $T$ from it.
2. By the reduction $\mathsf{MAX} \leq_{sW} \mathsf{WKL}$, a computable $f$ gives a computable infinite binary tree, which has a low path by the low basis theorem (:ref{#thm-low-basis}); the backward functional computes a name of a maximum point from it, of degree at most low.
:::

Item 1 is due to Lacombe (1957) and Specker (1959). It shows that the theorem "a continuous function on $[0, 1]$ attains its maximum" fails in the ω-model $\mathrm{REC}$, in the version with codes; in reverse mathematics, it is equivalent to weak König's lemma over $\mathsf{RCA}_0$ (Simpson, Theorem IV.2.3). The equivalence of :ref{#thm-max-wkl} refines both facts: the reduction to $\mathsf{WKL}$ is uniform, and it uses a single instance.

:::quiz[the maximum]
In the proof that $\mathsf{MAX} \leq_{sW} \mathsf C_{[0,1]}$, why is the maximum value $M$ computed first?

- [x] Because the name of the set of maximum points lists the intervals on which $f$ is certainly below $M$; without $M$, no finite information shows that a point is not a maximum point.
- [ ] Because $\mathsf{MAX}$ asks for the maximum value.

  The solutions are points, not the value; the value serves to describe the set of points.
- [ ] Because the set of maximum points is open.

  It is closed, and described by its open complement.

---

Why does item 1 of :ref{#cor-max-points} not contradict :ref{#thm-modulus-max}?

- [x] Because the maximum value of a computable $f$ is computable, while the points where it is attained need not be: computing the value does not locate a point.
- [ ] Because the function of item 1 is not continuous.

  It is computable, hence continuous.
- [ ] Because the maximum of the function of item 1 is not attained.

  A continuous function on $[0, 1]$ attains its maximum; here only at non-computable points.
:::

::::exercise{#ex-unique-max difficulty=1 objective="Compute a unique maximum point by unique choice, in contrast with the general case." lessons="closed-sets-and-choice"}
Show that if a computable $f \in C[0, 1]$ attains its maximum at a single point, this point is computable, uniformly in a name of $f$ among the functions with a unique maximum point.

:::solution
The proof of :ref{#thm-max-wkl} computes, from a name of $f$, a $\psi_>$-name of the set of maximum points. When this set is a singleton, :ref{#ex-unique-choice} computes its point. Both steps are uniform.
:::
::::

## The monotone convergence theorem

:::definition{#def-mct-problem}
The problem $\mathsf{MCT}$ has as instances the bounded non-decreasing sequences of reals $(x_n)$, represented by $\rho^\omega$, and as solution the limit $\lim_n x_n$.
:::

The limit is unique, so $\mathsf{MCT}$ is a single-valued problem; its difficulty is the absence of a rate of convergence (:ref{#prop-effective-limit}). Specker's sequence (:ref{#prop-specker}) shows that it is not computable, even on computable instances. The uniform version of Specker's construction gives its exact degree. We use the jump $\mathsf J$ and its parallel form $\widehat{\mathsf{LPO}}$ (:ref{#thm-jump-lpo}), and the reals $x_A = \sum_{n \in A} 2 \cdot 3^{-n-1}$ of :ref{#ex-computable-reals}.

:::theorem{#thm-mct-jump}
$\mathsf{MCT} \equiv_{sW} \mathsf J$.
:::

:::proof{of=thm-mct-jump}
($\mathsf{MCT} \leq_{sW} \mathsf J$) Let $x = \lim_n x_n = \sup_n x_n$. For a rational $q$, $q < x$ if and only if $x_n > q$ for some $n$, if and only if some term $q_{n,k}$ of the given name of some $x_n$ satisfies $q_{n,k} - 2^{-k} > q$. Let $p_q(s) = 1$ if such $n, k \leq s$ exist, and $p_q(s) = 0$ otherwise. The sequence $(p_q)_q$, indexed by the rationals, is an instance of $\widehat{\mathsf{LPO}}$ computed from the name, and its solution is the set $L = \{ q : q < x \}$. From $L$, compute for each $k$ the unique integer $j$ with $j 2^{-k} \in L$ and $(j + 1) 2^{-k} \notin L$, by testing $j = 0, -1, 1, -2, 2, \dots$; then $x - 2^{-k} \leq j 2^{-k} < x$, and :ref{#lem-cauchy-variants} gives a Cauchy name of $x$, computed from $L$ alone. Since $\widehat{\mathsf{LPO}} \leq_{sW} \mathsf J$ (:ref{#thm-jump-lpo} and the remark after it), $\mathsf{MCT} \leq_{sW} \mathsf J$.

($\mathsf J \leq_{sW} \mathsf{MCT}$) Given $X$, let $x_n = \sum \{ 2 \cdot 3^{-e-1} : e < n,\ \Phi^X_e(e)[n]\converge \}$. These rationals are computed from $X$, they form a non-decreasing sequence bounded by $1$, and their limit is $x_{X'} = \sum_{e \in X'} 2 \cdot 3^{-e-1}$. By :ref{#ex-computable-reals} (3), $X'$ is computed from any Cauchy name of $x_{X'}$, uniformly: the decoding procedure of the example is the same for every set.
:::

The second reduction is Specker's construction (:ref{#prop-specker}), with the set $X'$ in place of $\emptyset'$ and a coding by ternary digits that makes the decoding uniform. The theorem refines the reverse-mathematical equivalence of the monotone convergence theorem with $\mathsf{ACA}_0$ (:ref{#thm-monotone-aca}): a single application of the jump suffices, uniformly, and is necessary.

:::quiz[the monotone convergence theorem]
In the proof that $\mathsf{MCT} \leq_{sW} \mathsf J$, why is the set $L = \{ q : q < x \}$ enough to compute $x$, while a left name of $x$ is not (:ref{#prop-left-right})?

- [x] Because $L$ is given as a set, with its complement: the test $(j+1) 2^{-k} \notin L$ provides upper bounds, which a list of the elements of $L$ never does.
- [ ] Because $L$ is computable.

  $L$ is computed by the jump of the instance; it is not computable in general.
- [ ] Because the sequence is non-decreasing.

  Monotonicity is used to show that $q < x$ is a $\Sigma^0_1$ question; the upper bounds come from the complement of $L$.

---

Where does the proof that $\mathsf J \leq_{sW} \mathsf{MCT}$ use the digits $0$ and $2$ in base $3$?

- [x] In the decoding: the possible values of the tail of the series are separated by gaps, so finite approximations of the limit determine the digits one by one, whatever the set $X'$ is.
- [ ] In the monotonicity of $(x_n)$.

  Any series with non-negative terms gives a non-decreasing sequence of partial sums.
- [ ] In the computation of the $x_n$ from $X$.

  The $x_n$ are computed for any choice of positive terms; the gaps matter only for the decoding.
:::

## Classification and reverse mathematics

The following table collects the classifications of the course. The last column gives the subsystem of second-order arithmetic equivalent to the theorem over $\mathsf{RCA}_0$, or $\mathsf{RCA}_0$ when it is provable there.

| Problem | Weihrauch degree | Computable instances | Reverse mathematics |
| --- | --- | --- | --- |
| $\mathsf{IVT}$ for zero sets with empty interior | computable | computable solutions | $\mathsf{RCA}_0$ |
| $\mathsf{IVT}$, $\mathsf{BFT}_1$ | $\mathsf{CC}_{[0,1]}$, strictly between $\mathsf{LLPO}$ and $\mathsf{WKL}$ | computable solutions | $\mathsf{RCA}_0$ |
| $\mathsf C_{[0,1]}$, $\mathsf{MAX}$, $\mathsf{BFT}_n$ for $n \geq 2$ | $\mathsf{WKL}$ | low solutions, not always computable | $\mathsf{WKL}_0$ |
| $\mathsf{MCT}$ | $\mathsf J$ | solutions computable in $\emptyset'$, not always computable | $\mathsf{ACA}_0$ |

The columns agree on the coarse level: the problems equivalent to $\mathsf{WKL}$ or $\mathsf J$ come from theorems equivalent to $\mathsf{WKL}_0$ or $\mathsf{ACA}_0$. This is not a general law, but the reductions of the course are effective versions of the proofs of reverse mathematics, as the proofs of :ref{#thm-mct-jump} and :ref{#thm-monotone-aca} show. The Weihrauch degrees are finer in two ways. They separate problems that admit computable solutions: the intermediate value theorem and its restriction to zero sets with empty interior are both provable in $\mathsf{RCA}_0$, but only the second is computable. And they distinguish a problem from its parallelization: the intermediate value theorem is provable in $\mathsf{RCA}_0$, while its parallelization is as strong as $\mathsf{WKL}$; in reverse mathematics, the sequential version of a theorem is a different statement, to be analyzed separately. Conversely, reverse mathematics sees the induction and the compactness used in correctness proofs, which computable analysis takes for granted: the computability of the maximum value of a function given by a code relies on the Heine–Borel theorem (:ref{#thm-modulus-max}).

## Notes and references

The classification of the maximum is stated in Brattka, Gherardi and Pauly, Theorem 8.3, with a reference to Brattka (2016); computable functions attaining their maximum only at non-computable points are due to Lacombe (1957) and Specker (1959) (Brattka, Gherardi and Pauly, Corollary 8.4). The monotone convergence theorem is equivalent to the limit map by Brattka, Gherardi and Marcone (2012, Fact 11.26) and Brattka and Gherardi (2011, Proposition 3.8), and the limit is equivalent to the jump (Brattka, Gherardi and Pauly, Theorem 8.9); the same authors show that the Bolzano–Weierstrass theorem is equivalent to the jump of $\mathsf{WKL}$. Specker's original construction is :ref{#prop-specker}. In reverse mathematics, the intermediate value theorem is Simpson, Theorem II.6.6, the monotone convergence theorem Theorem III.2.2, the maximum Theorem IV.2.3, and the Brouwer fixed point theorem Theorem IV.7.7; Dzhafarov and Mummert compare reverse mathematics and Weihrauch reducibility throughout their book.

- V. Brattka, G. Gherardi and A. Pauly, *Weihrauch complexity in computable analysis*, in *Handbook of Computability and Complexity in Analysis*, Springer, 2021, 367–417.
- V. Brattka, *Computability and analysis, a historical approach*, in *Pursuit of the Universal (CiE 2016)*, Lecture Notes in Computer Science 9709, Springer, 2016, 45–57.
- V. Brattka, G. Gherardi and A. Marcone, *The Bolzano–Weierstrass theorem is the jump of weak Kőnig's lemma*, Annals of Pure and Applied Logic 163 (2012), 623–655.
- V. Brattka and G. Gherardi, *Effective choice and boundedness principles in computable analysis*, Bulletin of Symbolic Logic 17 (2011), 73–117.
- E. Specker, *Nicht konstruktiv beweisbare Sätze der Analysis*, Journal of Symbolic Logic 14 (1949), 145–158.
- E. Specker, *Der Satz vom Maximum in der rekursiven Analysis*, in A. Heyting (ed.), *Constructivity in Mathematics*, North-Holland, 1959, 254–265.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections II.6, III.2, IV.2 and IV.7.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.

:::::exercises
::::exercise{#ex-lim-jump difficulty=3 objective="Compute limits without a rate of convergence from the jump, and classify the limit operation."}
The problem $\mathsf{lim}_{\mathbb R}$ has as instances the convergent sequences of reals, represented by $\rho^\omega$, and as solution their limit. Show that $\mathsf{lim}_{\mathbb R} \equiv_W \mathsf J$.

:::solution
$\mathsf{MCT}$ is a restriction of $\mathsf{lim}_{\mathbb R}$, so $\mathsf J \leq_W \mathsf{lim}_{\mathbb R}$ by :ref{#thm-mct-jump}. Conversely, let $(x_n)$ converge, with names $(q_{n,k})_k$. For $k, n \in \nat$, the statement "$|x_m - x_{m'}| \leq 2^{-k}$ for all $m, m' \geq n$" is $\Pi^0_1$ relative to the name, uniformly in $k$ and $n$, since $|x_m - x_{m'}| > 2^{-k}$ is semi-decidable (:ref{#prop-order-undecidable}). So the jump of the name decides it, uniformly. With the jump, compute for each $k$ the least $n_k$ for which it holds, which exists since the sequence is Cauchy. Then $|x_{n_k} - x| \leq 2^{-k}$, and the sequence $(x_{n_{k+1}})_k$ satisfies the hypothesis of :ref{#prop-effective-limit}, which computes the limit. The backward functional uses the name of the sequence and its jump.
:::
::::

::::exercise{#ex-ivt-max difficulty=1 objective="Reduce the intermediate value theorem and the Brouwer fixed point theorem in dimension one to the maximum directly." lessons="intermediate-value-theorem"}
Show that $\mathsf{IVT} \leq_{sW} \mathsf{MAX}$ and $\mathsf{BFT}_1 \leq_{sW} \mathsf{MAX}$ by direct reductions, with the identity as backward functional.

:::solution
Given an instance $f$ of $\mathsf{IVT}$, pass $-|f|$. Its values are $\leq 0$, and it vanishes at some point by the intermediate value theorem, so its maximum is $0$, attained exactly at the zeros of $f$. If $(P_k)$ is a $\delta_C$-name of $f$, then $-|P_k|$ is a rational polygon, with the rational zeros of $P_k$ as additional breakpoints, and $d(-|P_k|, -|f|) \leq d(P_k, f)$; so $(-|P_k|)$ is a $\delta_C$-name of $-|f|$. For $\mathsf{BFT}_1$, pass $x \mapsto -|f(x) - x|$, with the name $(-|P_k(x) - x|)_k$: its maximum points are the fixed points of $f$, which exist by the intermediate value theorem applied to $x - f(x)$. These reductions are also consequences of :ref{#thm-ivt-llpo-wkl}, :ref{#thm-brouwer-one} and :ref{#thm-max-wkl}.
:::
::::

::::exercise{#ex-least-max-point difficulty=2 objective="Show that the least maximum point of a function is computable from below only." lessons="closed-sets-and-choice"}
For $f \in C[0, 1]$, let $m(f)$ be the least point where $f$ attains its maximum. Show that $f \mapsto m(f)$ is $(\delta_C, \rho_<)$-computable, and that it is not $(\delta_C, \rho)$-continuous.

:::solution
The proof of :ref{#thm-max-wkl} computes, from a name of $f$, a $\psi_>$-name of the non-empty closed set $A$ of maximum points, and $m(f) = \min A$. A rational $q$ satisfies $q < \min A$ if and only if $q < 0$, or $q \geq 0$ and $[0, q] \cap A = \emptyset$, which is semi-decidable by compactness and :ref{#lem-effective-heine-borel} (1), as in :ref{#ex-closed-max} (1) with the order reversed. This gives a left name of $m(f)$.

Suppose that a continuous $F$ maps $\delta_C$-names of $f$ to Cauchy names of $m(f)$. Let $p$ be the name of the function $0$ whose terms are all the polygon $0$; then $m(0) = 0$, and the term of index $3$ of $F(p)$ is a rational $r$ with $|r| \leq 1/8$. By continuity there is $m$ such that the term of index $3$ of $F(q)$ is $r$ for every name $q \in [p \uh m]$. Let $h$ be the rational polygon with vertices $(0, 0)$, $(1/4, 0)$, $(1/2, 2^{-m})$, $(3/4, 0)$ and $(1, 0)$. Then $d(0, h) = 2^{-m} \leq 2^{-k}$ for $k < m$, so the sequence $q$ of polygons $0, \dots, 0, h, h, \dots$, with $m$ terms $0$, is a $\delta_C$-name of $h$ extending $p \uh m$. The only maximum point of $h$ is $1/2$, so $|r - 1/2| \leq 1/8$, which contradicts $|r| \leq 1/8$.
:::
::::

::::exercise{#ex-sup-mct difficulty=1 objective="Show that the supremum of a bounded sequence of reals has the same Weihrauch degree as monotone convergence." lessons="real-functions"}
Let $\mathsf{SUP}$ be the problem whose instances are the bounded sequences of reals, represented by $\rho^\omega$, with solution their supremum. Show that $\mathsf{SUP} \equiv_{sW} \mathsf{MCT}$, hence $\mathsf{SUP} \equiv_{sW} \mathsf J$.

:::solution
For a non-decreasing sequence, the supremum is the limit, so $\mathsf{MCT}$ is a restriction of $\mathsf{SUP}$ and the identity functionals reduce it. Conversely, given a bounded sequence $(x_n)$, compute $y_n = \max_{i \leq n} x_i$, uniformly in $n$ by :ref{#thm-arithmetic-computable}. The sequence $(y_n)$ is non-decreasing and bounded, and $\lim_n y_n = \sup_n x_n$, so the backward functional is the identity. Conclude with :ref{#thm-mct-jump}. Compare with :ref{#ex-sup-left-ce}: the supremum is computable from below, and the jump is what provides upper bounds.
:::
::::

::::exercise{#ex-max-dominated difficulty=1 objective="Combine the reduction of the maximum to weak König's lemma with another basis theorem." lessons="pi01-classes/basis-theorems"}
Show that every computable $f \in C[0, 1]$ attains its maximum at a point with a Cauchy name of computably dominated degree.

:::solution
By the reduction $\mathsf{MAX} \leq_{sW} \mathsf{WKL}$ of :ref{#thm-max-wkl}, a computable name of $f$ gives a computable infinite binary tree $T$, and the backward functional computes a Cauchy name of a maximum point of $f$ from every path through $T$. By the computably dominated basis theorem (:ref{#thm-dominated-basis}), $T$ has a path $X$ of computably dominated degree. The name $q$ computed from $X$ satisfies $q \leq_T X$, and every function computable from $q$ is computable from $X$, hence dominated by a computable function: $q$ has computably dominated degree. With :ref{#cor-max-points} (2), every computable $f$ thus has a maximum point with a low name and a maximum point with a computably dominated name, which may be different points.
:::
::::

::::exercise{#ex-max-below-mct difficulty=1 objective="Compare the two classifications of the lesson in the Weihrauch degrees."}
Show that $\mathsf{MAX} <_W \mathsf{MCT}$, that is, $\mathsf{MAX} \leq_W \mathsf{MCT}$ and $\mathsf{MCT} \not\leq_W \mathsf{MAX}$.

:::solution
By :ref{#thm-max-wkl} and :ref{#thm-mct-jump}, it suffices to show $\mathsf{WKL} \leq_W \mathsf J$ and $\mathsf J \not\leq_W \mathsf{WKL}$. Given an infinite binary tree $T$, the set of nodes of $T$ with infinitely many extensions in $T$ is $\Pi^0_1$ relative to $T$, uniformly, since a node has infinitely many extensions in the finitely branching tree $T$ if and only if it has extensions in $T$ of every length; so it is decided by $T'$, uniformly. From $T'$, compute the path that starts at the root, which has infinitely many extensions since $T$ is infinite, and always moves to the left successor if it has infinitely many extensions, and to the right one otherwise; the right one then has infinitely many extensions. This is a path through $T$, so $\mathsf{WKL} \leq_W \mathsf J$.

If $\mathsf J \leq_W \mathsf{WKL}$, then $\mathsf{LPO} \leq_W \widehat{\mathsf{LPO}} \leq_W \mathsf J \leq_W \mathsf{WKL}$ by :ref{#thm-jump-lpo}, which contradicts :ref{#ex-lpo-not-wkl}.
:::
::::
:::::
