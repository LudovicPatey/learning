---
title: Mathematics in RCA₀
summary: Coding real numbers and continuous functions in second-order arithmetic; RCA₀ proves the completeness of the reals for sequences with a modulus of convergence and the intermediate value theorem; Specker sequences show that RCA₀ does not prove the monotone convergence theorem.
duration: 35
prerequisites: [rca0]
---

Second-order arithmetic speaks only of numbers and sets of numbers. To formalize analysis, one codes real numbers, sequences of reals and continuous functions by sets of numbers, with codings chosen so that the basic operations are computable. This lesson presents these codings, proves two theorems of analysis in $\mathsf{RCA}_0$, and shows that a third one, the monotone convergence theorem, is not provable there. The latter will turn out to be equivalent to arithmetic comprehension.

## Real numbers

Rational numbers are coded by numbers through a computable bijection between $\nat$ and $\mathbb Q$; in $\mathsf{RCA}_0$ one proves that they form an ordered field with decidable equality and order. Sequences of rationals are coded by sets, a function $f : \nat \to \nat$ being identified with its graph.

:::definition{#def-real-rca}
In $\mathsf{RCA}_0$, a **real number** is a sequence of rationals $x = (q_k)_{k \in \nat}$ such that $|q_k - q_l| \leq 2^{-k}$ for all $k \leq l$. Two reals $x = (q_k)$ and $y = (p_k)$ are **equal**, $x =_{\mathbb R} y$, if $|q_k - p_k| \leq 2^{-k+1}$ for all $k$, and $x < y$ if $q_k + 2^{-k+1} < p_k$ for some $k$.
:::

The sequence $(q_k)$ represents its limit, and the fixed rate of convergence $2^{-k}$ makes the relation $x < y$ a $\Sigma^0_1$ property, and equality a $\Pi^0_1$ property. Equality is not decidable: no algorithm decides whether two given reals are equal, a phenomenon that will recur. The sum, product and absolute value of reals are defined termwise, with an adjustment of indices for the product, and $\mathsf{RCA}_0$ proves that the reals form an ordered field. A **sequence of reals** is a double sequence $(q_{n,k})$ such that each $(q_{n,k})_k$ is a real.

Without the rate of convergence, a Cauchy sequence of rationals would still determine a limit, but the order would no longer be $\Sigma^0_1$, and the limit of a computable Cauchy sequence need not be a computable real: a Specker sequence, constructed below, is an example.

:::proposition{#prop-rca-complete}
$\mathsf{RCA}_0$ proves: if $(x_n)$ is a sequence of reals and $|x_n - x_m| \leq 2^{-n}$ for all $n \leq m$, then $(x_n)$ converges to a real $x$, that is, $|x_n - x| \leq 2^{-n}$ for every $n$.
:::

:::proof{of=prop-rca-complete}
Write $x_n = (q_{n,k})_k$, and let $p_k = q_{k+2, k+2}$; the sequence $(p_k)$ exists by $\Delta^0_1$ comprehension. For $k \leq l$,
$$
|p_k - p_l| \leq |q_{k+2,k+2} - x_{k+2}| + |x_{k+2} - x_{l+2}| + |x_{l+2} - q_{l+2,l+2}| \leq 2^{-k-2} + 2^{-k-2} + 2^{-l-2} \leq 2^{-k},
$$
where the middle term uses the hypothesis, so $x = (p_k)$ is a real. For each $n$ and $k \geq n$, $|x_n - p_k| \leq |x_n - x_{k+2}| + |x_{k+2} - q_{k+2,k+2}| \leq 2^{-n} + 2^{-k-2}$; letting $k$ grow, $|x_n - x| \leq 2^{-n}$.
:::

The rate $2^{-n}$ plays the role of a modulus of convergence: the limit is computed from the sequence. Without a modulus, the existence of the limit requires more than $\mathsf{RCA}_0$.

## Continuous functions

A continuous function on $[0, 1]$ is determined by countable information: approximations of its values on small intervals.

:::definition{#def-continuous-code}
In $\mathsf{RCA}_0$, a **code** for a continuous function $f : [0, 1] \to \mathbb R$ is a set $\Phi$ of quadruples $(a, r, b, s)$ of rationals with $r, s > 0$, such that:

1. *consistency:* if $(a, r, b, s), (a', r', b', s') \in \Phi$ and $|a - a'| < r + r'$, then $|b - b'| \leq s + s'$;
2. *totality:* for every real $x \in [0, 1]$ and every $\varepsilon > 0$, there is $(a, r, b, s) \in \Phi$ with $|x - a| < r$ and $s < \varepsilon$.

The value $f(x)$ is the unique real $y$ such that $|y - b| \leq s$ for every $(a, r, b, s) \in \Phi$ with $|x - a| < r$.
:::

A quadruple $(a, r, b, s)$ asserts that $f$ maps the interval $(a - r, a + r)$ into $[b - s, b + s]$. Consistency makes these assertions compatible, and totality makes them precise enough at every point. $\mathsf{RCA}_0$ proves that $f(x)$ exists, uniformly in $x$, by searching for quadruples with smaller and smaller $s$, and that $f$ is continuous in the usual $\varepsilon$-$\delta$ sense. We admit these verifications (Simpson, Section II.6). Every continuous function on $[0, 1]$ has a code, and the codes of computable functions can be chosen computable.

## The intermediate value theorem

:::theorem{#thm-ivt-rca}
$\mathsf{RCA}_0$ proves the intermediate value theorem: if $f : [0, 1] \to \mathbb R$ is continuous with $f(0) < 0 < f(1)$, then $f(x) = 0$ for some $x \in [0, 1]$.
:::

:::proof{of=thm-ivt-rca}
If $f(q) = 0$ for some rational $q \in [0, 1]$, we are done. Otherwise, for every rational $q \in [0, 1]$, $f(q) < 0$ or $f(q) > 0$. Both relations are $\Sigma^0_1$ in $q$ and the code of $f$, and since exactly one holds, "$f(q) < 0$" is equivalent to the $\Pi^0_1$ formula "not $f(q) > 0$". By $\Delta^0_1$ comprehension, the set $N$ of rationals $q \in [0, 1]$ with $f(q) < 0$ exists.

Define rationals $a_0 = 0$, $b_0 = 1$, and, with $c_n = (a_n + b_n)/2$, $(a_{n+1}, b_{n+1}) = (c_n, b_n)$ if $c_n \in N$, and $(a_n, c_n)$ otherwise. The sequence is defined by primitive recursion relative to $N$, hence exists in $\mathsf{RCA}_0$, and an induction on the bounded formula expressing the recursion shows that $a_n \leq a_{n+1} < b_{n+1} \leq b_n$, $b_n - a_n = 2^{-n}$, $f(a_n) < 0$ and $f(b_n) > 0$ for every $n$. So $x = (a_n)$ is a real, and $(b_n)$ represents the same real.

Suppose $f(x) > 0$. By continuity, there is $\delta > 0$ with $f(y) > 0$ for every $y \in [0, 1]$ with $|y - x| < \delta$. For $n$ with $2^{-n} < \delta$, $|a_n - x| \leq 2^{-n} < \delta$, so $f(a_n) > 0$, a contradiction. Symmetrically, $f(x) < 0$ contradicts $f(b_n) > 0$. Since the order of the reals is total, $f(x) = 0$.
:::

The proof is not uniform: it distinguishes whether $f$ vanishes at a rational, a $\Sigma^0_1$ question that cannot be decided effectively. This is harmless in $\mathsf{RCA}_0$, which reasons classically, but shows that the zero cannot be computed from $f$ in general. The finer analysis of such uniformity questions is the subject of Weihrauch reducibility.

:::quiz[the intermediate value theorem]
In the proof of :ref{#thm-ivt-rca}, why is the case of a rational zero treated separately?

- [x] Because the set $N$ is defined by $\Delta^0_1$ comprehension only if $f(q) \neq 0$ for every rational $q$: then "$f(q) < 0$" has both a $\Sigma^0_1$ and a $\Pi^0_1$ definition.
- [ ] Because the bisection cannot find rational zeros.

  The issue is the definability of $N$, not the search.
- [ ] Because $f$ is not defined at rationals.

  A continuous function is defined at every real, rationals included.

---

Why does the existence of the sequence $(a_n, b_n)$ not require arithmetic comprehension?

- [x] Because it is computed by primitive recursion from the set $N$, which exists, and $\mathsf{RCA}_0$ proves the existence of sets computable from existing sets.
- [ ] Because it is finite.

  It is an infinite sequence; it exists because it is computable from $N$.
- [ ] Because $f$ is computable.

  $f$ is an arbitrary continuous function of the model; only computability relative to its code is used.
:::

## Specker sequences

The monotone convergence theorem states that every bounded non-decreasing sequence of reals converges. It is true in $\mathcal P(\nat)$, but fails in the ω-model $\mathrm{REC}$.

:::proposition[Specker]{#prop-specker}
There is a computable non-decreasing sequence of rationals in $[0, 1]$ whose limit is not a computable real. Consequently $\mathsf{RCA}_0$ does not prove the monotone convergence theorem.
:::

:::proof{of=prop-specker}
Let $f$ be a computable injective function with range $\emptyset'$, and $x_n = \sum_{i \leq n} 2^{-f(i) - 1}$. The sequence is computable, non-decreasing, bounded by $\sum_m 2^{-m-1} = 1$, and converges to $x = \sum_{m \in \emptyset'} 2^{-m-1}$. If $x$ were computable, given $m$ one could compute $n$ such that $x - x_n < 2^{-m-1}$; then $m \in \emptyset'$ if and only if $m = f(i)$ for some $i \leq n$, since a later $f(i) = m$ would add $2^{-m-1}$ to the remaining sum. So $\emptyset'$ would be computable.

In $\mathrm{REC}$, the sequence $(x_n)$ exists, is bounded and non-decreasing, by absoluteness, but has no limit in the model, since a limit in $\mathrm{REC}$ would be a computable real equal to $x$. So the monotone convergence theorem fails in the ω-model $\mathrm{REC}$ of $\mathsf{RCA}_0$.
:::

The same construction, carried out relative to an arbitrary set, shows that the monotone convergence theorem implies the existence of the ranges of injective functions, and thus arithmetic comprehension; this is proved in the course on the Big Five.

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{RCA}_0$ proves that every continuous function $f : [0, 1] \to \mathbb R$ with $f(0) < c < f(1)$ takes the value $c$, for every real $c$.

:::solution
The function $g(x) = f(x) - c$ is continuous, and a code for it is obtained from a code for $f$ and the real $c$ by $\Delta^0_1$ comprehension: replace each quadruple $(a, r, b, s)$ by $(a, r, b - q, s + 2^{-k+1})$ for the rational approximations $q = c_k$ of $c$, for all $k$. Then $g(0) < 0 < g(1)$, and :ref{#thm-ivt-rca} gives $x$ with $g(x) = 0$, that is, $f(x) = c$.
:::
::::

::::exercise{difficulty=2}
Show that the limit of a Specker sequence can be chosen to be $\Omega$, Chaitin's halting probability, and that every left-c.e. real is the limit of a computable non-decreasing sequence of rationals.

:::solution
By definition, a left-c.e. real is the limit of a computable non-decreasing sequence of rationals. Chaitin's $\Omega$ is left-c.e., as the limit of the computable non-decreasing sequence $\Omega_s$, and it is not computable, since it computes $\emptyset'$. So $(\Omega_s)$ is a Specker sequence with limit $\Omega$.
:::
::::

## Notes and references

The coding of reals and continuous functions follows Simpson's monograph, Sections II.4–II.6. Specker (1949) constructed computable monotone bounded sequences without computable limit, one of the first results of computable analysis. Computable analysis studies the reals and continuous functions under these codings; see Weihrauch's book.

- E. Specker, *Nicht konstruktiv beweisbare Sätze der Analysis*, Journal of Symbolic Logic 14 (1949), 145–158.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009.
- K. Weihrauch, *Computable Analysis*, Springer, 2000.
