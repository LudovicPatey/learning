---
title: Real numbers in RCA₀
summary: Real numbers as fast Cauchy sequences of rationals; order is Σ⁰₁ and equality Π⁰₁; RCA₀ proves completeness for sequences with a modulus of convergence; Specker sequences show that RCA₀ does not prove the monotone convergence theorem.
duration: 30
prerequisites: [rca0]
---

Second-order arithmetic speaks only of numbers and sets of numbers. To formalize analysis, one codes real numbers, sequences of reals and continuous functions by sets of numbers. The codings are chosen so that the basic operations are computable relative to the codes, and so that the basic relations have low complexity: $x < y$ is $\Sigma^0_1$, which is what $\Delta^0_1$ comprehension can use. This lesson codes the real numbers, proves in $\mathsf{RCA}_0$ the completeness of the reals for sequences with a modulus of convergence, and shows that the monotone convergence theorem is not provable there; it will turn out to be equivalent to arithmetic comprehension. The next lesson treats continuous functions.

The proofs in $\mathsf{RCA}_0$ follow a common pattern, the **coding technique** of the whole track. A classical construction is examined step by step, and every set it builds is shown to be computable from sets already given, usually by exhibiting a $\Sigma^0_1$ and a $\Pi^0_1$ definition. Where this fails, as for the limit of a monotone sequence, an ω-model shows that it must fail.

## Real numbers

Rational numbers are coded by numbers through a computable bijection between $\nat$ and $\mathbb Q$; in $\mathsf{RCA}_0$ one proves that they form an ordered field with decidable equality and order. Sequences of rationals are coded by sets, a function $f : \nat \to \nat$ being identified with its graph.

:::definition{#def-real-rca}
In $\mathsf{RCA}_0$, a **real number** is a sequence of rationals $x = (q_k)_{k \in \nat}$ such that $|q_k - q_l| \leq 2^{-k}$ for all $k \leq l$. Two reals $x = (q_k)$ and $y = (p_k)$ are **equal**, $x =_{\mathbb R} y$, if $|q_k - p_k| \leq 2^{-k+1}$ for all $k$, and $x < y$ if $q_k + 2^{-k+1} < p_k$ for some $k$.
:::

The sequence $(q_k)$ represents its limit, and its $k$-th term lies within $2^{-k}$ of it. Two approximations of the same limit at precision $2^{-k}$ may differ by $2^{-k+1}$, whence the factor $2$ in the definition of equality: the sequences $(2^{-k})_k$ and $(-2^{-k})_k$ are both reals with limit $0$, and they are equal. As in this example, a real number has many representations, and equality is an equivalence relation rather than identity; Simpson explains why equivalence classes, which are not sets of numbers, cannot be used instead (remark after Definition II.4.4).

The fixed rate of convergence $2^{-k}$ makes the relation $x < y$ a $\Sigma^0_1$ property of $x$ and $y$, and equality a $\Pi^0_1$ property. Equality cannot be decided from representations, even for a computable sequence of reals.

:::example{#ex-real-equality}
For each $e$, let $x_e = (q_{e,k})_k$, where $q_{e,k} = 2^{-s}$ if $\Phi_e(e)$ halts at a stage $s \leq k$, with $s$ least, and $q_{e,k} = 0$ otherwise. Each $x_e$ is a real: for $k \leq l$, the terms $q_{e,k}$ and $q_{e,l}$ differ only if the halting stage $s$ satisfies $k < s \leq l$, and then by $2^{-s} < 2^{-k}$. The double sequence is computable, and $x_e = 0$ if and only if $\Phi_e(e)$ diverges. So the set $\{ e : x_e = 0 \}$ is the complement of $\emptyset'$: no algorithm decides, from a representation of a real, whether it is $0$.
:::

The sum, product and absolute value of reals are defined termwise, with an adjustment of indices so that the rate $2^{-k}$ is preserved (for instance $x + y = (q_{k+1} + p_{k+1})_k$), and $\mathsf{RCA}_0$ proves that the reals form an ordered field. A **sequence of reals** is a double sequence $(q_{n,k})$ such that each $(q_{n,k})_k$ is a real.

Without the rate of convergence, a Cauchy sequence of rationals would still determine a limit, but the order would no longer be $\Sigma^0_1$, and the limit of a computable Cauchy sequence need not be a computable real: a Specker sequence, constructed below, is an example.

:::proposition{#prop-rca-complete}
$\mathsf{RCA}_0$ proves: if $(x_n)$ is a sequence of reals and $|x_n - x_m| \leq 2^{-n}$ for all $n \leq m$, then $(x_n)$ converges to a real $x$, that is, $|x_n - x| \leq 2^{-n}$ for every $n$.
:::

:::proof{of=prop-rca-complete}
Write $x_n = (q_{n,k})_k$, and let $p_k = q_{k+2, k+2}$; the sequence $(p_k)$ exists by $\Delta^0_1$ comprehension. For $k \leq l$,
$$
\begin{aligned}
|p_k - p_l| &\leq |q_{k+2,k+2} - x_{k+2}| + |x_{k+2} - x_{l+2}| + |x_{l+2} - q_{l+2,l+2}| \\
&\leq 2^{-k-2} + 2^{-k-2} + 2^{-l-2} \leq 2^{-k},
\end{aligned}
$$
where the outer terms use $|q_j - y| \leq 2^{-j}$ for a real $y = (q_j)$, and the middle term uses the hypothesis; so $x = (p_k)$ is a real. For each $n$ and $k \geq n$, $|x_n - p_k| \leq |x_n - x_{k+2}| + |x_{k+2} - q_{k+2,k+2}| \leq 2^{-n} + 2^{-k-2}$, and $|p_k - x| \leq 2^{-k}$, so $|x_n - x| \leq 2^{-n} + 2^{-k-2} + 2^{-k}$ for every $k \geq n$, that is, $|x_n - x| \leq 2^{-n}$.
:::

The rate $2^{-n}$ plays the role of a modulus of convergence: the limit is computed from the sequence. Without a modulus, the existence of the limit requires more than $\mathsf{RCA}_0$.

## Specker sequences

The monotone convergence theorem states that every bounded non-decreasing sequence of reals converges. It is true in $\mathcal P(\nat)$, but fails in the ω-model $\mathrm{REC}$.

:::proposition[Specker]{#prop-specker}
There is a computable non-decreasing sequence of rationals in $[0, 1]$ whose limit is not a computable real. Consequently $\mathsf{RCA}_0$ does not prove the monotone convergence theorem.
:::

:::proof{of=prop-specker}
Let $f$ be a computable injective function with range $\emptyset'$, and $x_n = \sum_{i \leq n} 2^{-f(i) - 1}$. The sequence is computable, non-decreasing, bounded by $\sum_m 2^{-m-1} = 1$, and converges to $x = \sum_{m \in \emptyset'} 2^{-m-1}$. If $x$ were computable, given $m$ one could compute $n$ such that $x - x_n < 2^{-m-1}$; then $m \in \emptyset'$ if and only if $m = f(i)$ for some $i \leq n$, since a later $f(i) = m$ would add $2^{-m-1}$ to the remaining sum. So $\emptyset'$ would be computable.

In $\mathrm{REC}$, the sequence $(x_n)$ exists, and it is bounded and non-decreasing by absoluteness. It has no limit in the model: "$y$ is the limit of $(x_n)$" is arithmetic, so a limit $y \in \mathrm{REC}$ would be a computable real equal to $x$. So the monotone convergence theorem fails in the ω-model $\mathrm{REC}$ of $\mathsf{RCA}_0$.
:::

:::quiz[Specker sequences]
In the proof of :ref{#prop-specker}, why does $x - x_n < 2^{-m-1}$ imply that $m$ is not of the form $f(i)$ with $i > n$?

- [x] Because $x - x_n = \sum_{i > n} 2^{-f(i) - 1}$, and a term with $f(i) = m$ would make this sum at least $2^{-m-1}$.
- [ ] Because $f$ is increasing.

  $f$ is only injective. If it were increasing, its range would be computable, and the limit would be a computable real.
- [ ] Because $x_n$ is a rational number.

  Rationality of $x_n$ plays no role; the argument compares the tail of the series with one of its terms.

---

Why does the failure of the monotone convergence theorem in $\mathrm{REC}$ need only the arithmetic definition of "limit"?

- [x] Because a limit $y \in \mathrm{REC}$ of $(x_n)$ in the sense of the model would, by absoluteness, be a limit in reality, hence equal to the non-computable real $x$.
- [ ] Because $\mathrm{REC}$ is closed under limits of sequences.

  It is not: the Specker sequence belongs to $\mathrm{REC}$ and its limit does not.
- [ ] Because the sequence $(x_n)$ is not in $\mathrm{REC}$.

  The sequence is computable, so it belongs to $\mathrm{REC}$; only its limit is missing.
:::

A computable non-decreasing bounded sequence of rationals whose limit is not computable is called a **Specker sequence**. The same construction, carried out for an arbitrary injective function, shows that the monotone convergence theorem implies the existence of the ranges of injective functions, and thus arithmetic comprehension; this reversal is proved in the course on the Big Five (:ref{#thm-monotone-aca}).

## Exercises

::::exercise{difficulty=2}
A real $x$ is **left-c.e.** if the set of rationals $q < x$ is c.e. Show that $x$ is left-c.e. if and only if it is the limit of a computable non-decreasing sequence of rationals. Deduce that every non-computable left-c.e. real, such as Chaitin's halting probability $\Omega$ (a forward pointer to the course on Kolmogorov complexity, :ref{#thm-omega}), is the limit of a Specker sequence.

:::solution
If $x$ is the limit of a computable non-decreasing sequence $(x_n)$ of rationals, then $q < x$ if and only if $q < x_n$ for some $n$: each $x_n$ is at most $x$, and if $q < x$, then $x_n > q$ for $n$ large. This is a c.e. condition on $q$. Conversely, let $q_0, q_1, \dots$ be a computable enumeration of the non-empty c.e. set $L = \{ q : q < x \}$, and $x_n = \max_{i \leq n} q_i$. The sequence $(x_n)$ is computable, non-decreasing and bounded by $x$; for $\varepsilon > 0$, some rational of $(x - \varepsilon, x)$ belongs to $L$, so $x_n > x - \varepsilon$ for $n$ large. Hence $x_n \to x$.

If $x$ is moreover not computable, such a sequence, bounded by any rational above $x$, is a Specker sequence. The real $\Omega$ is the limit of the computable non-decreasing sequence $(\Omega_s)$ of rationals, and it is not computable, since $\Omega \equiv_T \emptyset'$ (:ref{#thm-omega}).
:::
::::

## Notes and references

The coding of reals follows Simpson, Section II.4 (Definition II.4.4), and Dzhafarov–Mummert, Sections 10.1–10.2. Completeness for sequences with a modulus, :ref{#prop-rca-complete}, is Dzhafarov–Mummert, Exercise 10.9.2; Simpson proves the related nested interval completeness, Theorem II.4.8. Specker (1949) constructed computable monotone bounded sequences without computable limit, one of the first results of computable analysis; the construction is Simpson's Example II.4.7, and the equivalence of monotone convergence with $\mathsf{ACA}_0$ is Simpson, Theorem III.2.2, and Dzhafarov–Mummert, Theorem 10.2.4. Hirst (2007) compares the representations of reals by fast Cauchy sequences, decimal expansions and Dedekind cuts in reverse mathematics: single reals can be converted in $\mathsf{RCA}_0$, while converting sequences of reals between some representations requires $\mathsf{WKL}_0$ or $\mathsf{ACA}_0$. Computable analysis studies the reals under these codings; see Weihrauch's book.

- E. Specker, *Nicht konstruktiv beweisbare Sätze der Analysis*, Journal of Symbolic Logic 14 (1949), 145–158.
- J. L. Hirst, *Representations of reals in reverse mathematics*, Bulletin of the Polish Academy of Sciences, Mathematics 55 (2007), 303–316.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections II.4 and III.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 10.1–10.2.
- K. Weihrauch, *Computable Analysis*, Springer, 2000.
