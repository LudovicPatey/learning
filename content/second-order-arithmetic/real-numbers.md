---
title: Real numbers in RCA₀
summary: Real numbers as fast Cauchy sequences of rationals; order is Σ⁰₁ and equality Π⁰₁; RCA₀ proves completeness for sequences with a modulus of convergence; Specker sequences show that RCA₀ does not prove the monotone convergence theorem.
duration: 25
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

::::exercise{#ex-left-ce-specker difficulty=2 objective="Characterize the left-c.e. reals as limits of computable non-decreasing sequences, and recognize Specker sequences among them."}
A real $x$ is **left-c.e.** if the set of rationals $q < x$ is c.e. Show that $x$ is left-c.e. if and only if it is the limit of a computable non-decreasing sequence of rationals. Deduce that every non-computable left-c.e. real, such as Chaitin's halting probability $\Omega$ of the course on Kolmogorov complexity, is the limit of a Specker sequence.

:::solution
If $x$ is the limit of a computable non-decreasing sequence $(x_n)$ of rationals, then $q < x$ if and only if $q < x_n$ for some $n$: each $x_n$ is at most $x$, and if $q < x$, then $x_n > q$ for $n$ large. This is a c.e. condition on $q$. Conversely, let $q_0, q_1, \dots$ be a computable enumeration of the non-empty c.e. set $L = \{ q : q < x \}$, and $x_n = \max_{i \leq n} q_i$. The sequence $(x_n)$ is computable, non-decreasing and bounded by $x$; for $\varepsilon > 0$, some rational of $(x - \varepsilon, x)$ belongs to $L$, so $x_n > x - \varepsilon$ for $n$ large. Hence $x_n \to x$.

If $x$ is moreover not computable, such a sequence, bounded by any rational above $x$, is a Specker sequence. The real $\Omega$ is the limit of the computable non-decreasing sequence $(\Omega_s)$ of rationals, and it is not computable, since $\Omega \equiv_T \emptyset'$, as shown in the course on Kolmogorov complexity.
:::
::::

## Notes and references

The representation of reals by fast Cauchy sequences used here is the Cauchy representation of computable analysis, where it is compared with other representations, such as decimal expansions (:ref{to="computable-analysis/representations"}).

The coding of reals follows Simpson, Section II.4 (Definition II.4.4), and Dzhafarov–Mummert, Sections 10.1–10.2. Completeness for sequences with a modulus, :ref{#prop-rca-complete}, is Dzhafarov–Mummert, Exercise 10.9.2; Simpson proves the related nested interval completeness, Theorem II.4.8. Specker (1949) constructed computable monotone bounded sequences without computable limit, one of the first results of computable analysis; the construction is Simpson's Example II.4.7, and the equivalence of monotone convergence with $\mathsf{ACA}_0$ is Simpson, Theorem III.2.2, and Dzhafarov–Mummert, Theorem 10.2.4. Hirst (2007) compares the representations of reals by fast Cauchy sequences, decimal expansions and Dedekind cuts in reverse mathematics: single reals can be converted in $\mathsf{RCA}_0$, while converting sequences of reals between some representations requires $\mathsf{WKL}_0$ or $\mathsf{ACA}_0$. Computable analysis studies the reals under these codings; see Weihrauch's book.

- E. Specker, *Nicht konstruktiv beweisbare Sätze der Analysis*, Journal of Symbolic Logic 14 (1949), 145–158.
- J. L. Hirst, *Representations of reals in reverse mathematics*, Bulletin of the Polish Academy of Sciences, Mathematics 55 (2007), 303–316.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections II.4 and III.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 10.1–10.2.
- K. Weihrauch, *Computable Analysis*, Springer, 2000.

:::::exercises
::::exercise{#ex-real-order-limits difficulty=1 objective="Check that the order and equality of coded reals agree with those of their limits, and read off their complexity."}
For a real $x = (q_k)$ in the sense of :ref{#def-real-rca}, let $\hat x = \lim_k q_k$. Show that $x < y$ if and only if $\hat x < \hat y$, and $x =_{\mathbb R} y$ if and only if $\hat x = \hat y$. Deduce that exactly one of $x < y$, $x =_{\mathbb R} y$, $y < x$ holds, and write $x < y$ as a $\Sigma^0_1$ formula and $x =_{\mathbb R} y$ as a $\Pi^0_1$ formula with parameters $x, y$.

:::solution
Let $x = (q_k)$ and $y = (p_k)$. Letting $l \to \infty$ in $|q_k - q_l| \leq 2^{-k}$ gives $|q_k - \hat x| \leq 2^{-k}$, and similarly for $y$.

- If $q_k + 2^{-k+1} < p_k$, then $\hat x \leq q_k + 2^{-k} < p_k - 2^{-k} \leq \hat y$. Conversely, if $\hat x < \hat y$, take $k$ with $2^{-k+2} < \hat y - \hat x$; then $q_k + 2^{-k+1} \leq \hat x + 2^{-k} + 2^{-k+1} < \hat y - 2^{-k} \leq p_k$, so $x < y$.
- If $\hat x = \hat y$, then $|q_k - p_k| \leq |q_k - \hat x| + |\hat y - p_k| \leq 2^{-k+1}$ for every $k$. Conversely, if $|q_k - p_k| \leq 2^{-k+1}$ for every $k$, then $|\hat x - \hat y| \leq 2^{-k} + 2^{-k+1} + 2^{-k}$ for every $k$, so $\hat x = \hat y$.

Exactly one of $\hat x < \hat y$, $\hat x = \hat y$, $\hat y < \hat x$ holds, hence exactly one of the three relations between $x$ and $y$. With the sequences coded by their graphs, $x < y$ is $\exists k\, \exists a\, \exists b\, (\langle k, a \rangle \in x \wedge \langle k, b \rangle \in y \wedge a + 2^{-k+1} < b)$ and $x =_{\mathbb R} y$ is $\forall k\, \forall a\, \forall b\, \big( (\langle k, a \rangle \in x \wedge \langle k, b \rangle \in y) \rightarrow |a - b| \leq 2^{-k+1} \big)$, where $a, b$ range over (codes of) rationals and the comparisons of rationals are bounded.
:::
::::

::::exercise{#ex-real-equality-transitive difficulty=1 objective="Prove that equality of reals is transitive from the definition, by an argument that does not use limits and therefore works in $\mathsf{RCA}_0$."}
Show directly from :ref{#def-real-rca}, without using limits, that if $x =_{\mathbb R} y$ and $y =_{\mathbb R} z$, then $x =_{\mathbb R} z$.

:::solution
Let $x = (q_k)$, $y = (p_k)$, $z = (r_k)$, and fix $k$. For every $j \geq k$,
$$
\begin{aligned}
|q_k - r_k| &\leq |q_k - q_j| + |q_j - p_j| + |p_j - r_j| + |r_j - r_k| \\
&\leq 2^{-k} + 2^{-j+1} + 2^{-j+1} + 2^{-k} = 2^{-k+1} + 2^{-j+2}.
\end{aligned}
$$
A rational $a$ such that $a \leq b + 2^{-j+2}$ for every $j$ satisfies $a \leq b$, so $|q_k - r_k| \leq 2^{-k+1}$. The direct estimate through $p_k$ alone would only give $2^{-k+2}$; passing through a finer precision $j$ is what preserves the factor $2$.
:::
::::

::::exercise{#ex-cauchy-modulus difficulty=2 objective="Relate computable limits to computable moduli of convergence, and show by a halting-time construction that the converse fails."}
A **modulus of convergence** of a convergent sequence of rationals $(x_n)$ with limit $x$ is a function $h$ with $|x_n - x| \leq 2^{-k}$ for all $k$ and all $n \geq h(k)$.

1. Show that if a computable sequence of rationals has a computable modulus of convergence, its limit is a computable real.
2. Give a computable sequence of rationals that converges to $0$ and has no computable modulus of convergence.
3. Deduce that the sequence of :ref{#prop-specker} has no computable modulus of convergence.

:::solution
1. Let $p_k = x_{h(k+1)}$, a computable sequence. Then $|p_k - x| \leq 2^{-k-1}$, so for $k \leq l$, $|p_k - p_l| \leq 2^{-k-1} + 2^{-l-1} \leq 2^{-k}$: $(p_k)$ is a computable real with limit $x$.
2. Let $x_n = \sum \{ 2^{-e} : e \leq n \text{ and } \Phi_e(e) \text{ halts at stage } n \text{ exactly} \}$, where "at stage $n$ exactly" means at stage $n$ and not before. The sequence is computable, and each $e$ contributes to at most one term. Given $k$, let $N$ exceed the halting stages of the finitely many $e \leq k + 1$ in $\emptyset'$; for $n \geq N$, $0 \leq x_n \leq \sum_{e \geq k + 2} 2^{-e} = 2^{-k-1}$. So $x_n \to 0$. Suppose $h$ is a computable modulus. If $\Phi_e(e)$ halts at stage $s$ exactly with $s \geq \max(e, h(e+1))$, then $x_s \geq 2^{-e} > 2^{-e-1}$, while $s \geq h(e + 1)$ gives $x_s \leq 2^{-e-1}$, a contradiction. So $e \in \emptyset'$ if and only if $\Phi_e(e)$ halts before stage $\max(e, h(e+1))$, which is decidable: a contradiction.
3. The sequence of :ref{#prop-specker} is computable and its limit is not a computable real; by item 1, it has no computable modulus.

Item 2 shows that a computable limit does not give a computable modulus: the information is in the rate of convergence, not in the limit.
:::
::::

::::exercise{#ex-nested-intervals-rca difficulty=2 objective="Carry out a completeness argument in $\mathsf{RCA}_0$, by computing the speed of convergence from the data."}
Show that $\mathsf{RCA}_0$ proves the following nested interval principle. Let $(a_n)$ and $(b_n)$ be sequences of rationals with $a_n \leq a_{n+1} \leq b_{n+1} \leq b_n$ for every $n$, and such that for every $k$ there is $n$ with $b_n - a_n < 2^{-k}$. Then there is a real $x$ with $a_n \leq x \leq b_n$ for every $n$, where a rational $q$ is identified with the real $(q, q, \dots)$ and $x \leq y$ means $\neg (y < x)$. Why does this not contradict :ref{#prop-specker}?

:::solution
By induction, $a_n \leq a_m$ and $b_m \leq b_n$ for $n \leq m$, and $a_m \leq b_n$ for all $m, n$ (both are between $a_{\max(m, n)}$ and $b_{\max(m, n)}$); so $b_n - a_n$ is non-increasing. Let $n_k$ be the least $n$ with $b_n - a_n < 2^{-k}$. It exists by hypothesis and the least number principle (:ref{#ex-pi01-lnp}), and the graph of $k \mapsto n_k$ is defined by the bounded formula $b_n - a_n < 2^{-k} \wedge \forall m < n\ b_m - a_m \geq 2^{-k}$, so the function exists by $\Delta^0_1$ comprehension. It is non-decreasing, since $b_n - a_n$ is non-increasing. Let $p_k = a_{n_k}$. For $k \leq l$,
$$
p_k = a_{n_k} \leq a_{n_l} = p_l \leq b_{n_l} \leq b_{n_k} < a_{n_k} + 2^{-k} = p_k + 2^{-k},
$$
so $|p_k - p_l| < 2^{-k}$ and $x = (p_k)$ is a real.

Suppose $x < a_n$: $p_k + 2^{-k+1} < a_n$ for some $k$. If $n \leq n_k$, then $a_n \leq a_{n_k} = p_k$; if $n > n_k$, then $a_n \leq b_n \leq b_{n_k} < p_k + 2^{-k}$. Both contradict the assumption, so $a_n \leq x$. Suppose $b_n < x$: $b_n + 2^{-k+1} < p_k$ for some $k$; but $p_k = a_{n_k} \leq b_n$. So $x \leq b_n$.

For the Specker sequence $(a_n)$, the hypothesis would require a sequence $(b_n)$ of upper bounds approaching it, with the condition on $b_n - a_n$; the proof computes a real from both sequences. In $\mathrm{REC}$, no computable such $(b_n)$ exists, since the limit is not computable.

Adapted from Simpson, Theorem II.4.8, and Dzhafarov–Mummert, Exercise 10.9.4, which state it for sequences of reals.
:::
::::

::::exercise{#ex-reals-uncountable-rca difficulty=2 objective="Formalize Cantor's diagonal argument for the reals in $\mathsf{RCA}_0$, making each choice decidable from approximations."}
Show that $\mathsf{RCA}_0$ proves: for every sequence of reals $(r_i)$ there is a real $x$ with $x \neq r_i$ for every $i$. Deduce that no computable sequence of reals contains every computable real.

:::solution
Write $r_i = (q_{i,k})_k$. Define rationals $a_0 = 0$, $b_0 = 1$, and, with $L = b_i - a_i = 3^{-i}$ and $q = q_{i, 2i + 4}$:
$$
(a_{i+1}, b_{i+1}) = \begin{cases} (a_i + 2L/3,\ b_i) & \text{if } q < a_i + L/2, \\ (a_i,\ a_i + L/3) & \text{otherwise.} \end{cases}
$$
The comparison is between rationals, so the sequence is defined by primitive recursion relative to $(r_i)$ and exists in $\mathsf{RCA}_0$. Since $2^{-2i-4} \cdot 6 < 2^{-2i} \leq 3^{-i}$, we have $2^{-2i-4} < L/6$, and $|r_i - q| \leq 2^{-2i-4}$. In the first case, $r_i \leq q + 2^{-2i-4} < a_i + L/2 + L/6 = a_{i+1}$; in the second, $r_i \geq q - 2^{-2i-4} > a_i + L/3 = b_{i+1}$.

The intervals are nested and $b_n - a_n = 3^{-n} < 2^{-k}$ for $n = k + 1$, so :ref{#ex-nested-intervals-rca} gives a real $x$ with $a_n \leq x \leq b_n$ for every $n$. For each $i$, either $r_i < a_{i+1} \leq x$ or $x \leq b_{i+1} < r_i$; in both cases $x \neq r_i$.

Applied in the ω-model $\mathrm{REC}$, a computable sequence of reals belongs to $\mathrm{REC}$, and the real $x$ of the model is a computable real, different from every $r_i$ by absoluteness.

Adapted from Simpson, Theorem II.4.9, and Dzhafarov–Mummert, Exercise 10.9.5; Simpson's proof keeps the outer quarters of each interval instead of the outer thirds.
:::
::::
:::::
