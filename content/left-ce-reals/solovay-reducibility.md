---
title: Solovay reducibility
summary: Solovay reducibility compares reals by the speed at which they can be approximated; it implies Turing reducibility and the domination of initial segment complexity, addition is the join of the left-c.e. Solovay degrees, and Ω is complete.
duration: 35
prerequisites: [approximations, martin-lof-randomness/levin-schnorr]
---

Turing reducibility is too coarse to distinguish $\Omega$ from $\emptyset'$, or from any other complete left-c.e. real. Solovay introduced a reducibility that measures the **quality of approximations**: $\alpha$ is Solovay reducible to $\beta$ if a good approximation of $\beta$ from below can be converted effectively into an approximation of $\alpha$ from below that is as good, up to a multiplicative constant. On left-c.e. reals, this says that the approximation of $\alpha$ converges at least as fast as that of $\beta$, up to a constant factor and a computable change of stages.

The reducibility has three properties that make it the right tool here. It implies Turing reducibility. It implies the domination of the complexities of initial segments, $K(\alpha \uh n) \leq^+ K(\beta \uh n)$, so a real above a random real is random. And $\Omega$ is complete: every left-c.e. real is Solovay reducible to it, as every c.e. set is many-one reducible to $\emptyset'$. The next lesson shows that the random left-c.e. reals form exactly the top degree, which is the analogue of Myhill's theorem for the halting problem.

## Definition

:::definition[Solovay]{#def-solovay-reducible}
A real $\alpha$ is **Solovay reducible** to a real $\beta$, written $\alpha \leq_S \beta$, if there are a constant $c$ and a partial computable function $f : \mathbb Q \to \mathbb Q$ such that for every rational $q < \beta$, $f(q)$ is defined, $f(q) \leq \alpha$, and
$$
\alpha - f(q) < c\, (\beta - q).
$$
We write $\alpha \equiv_S \beta$ if $\alpha \leq_S \beta$ and $\beta \leq_S \alpha$.
:::

The function $f$ turns a lower approximation $q$ of $\beta$ with error $\beta - q$ into a lower approximation of $\alpha$ with error at most $c$ times larger. Downey and Hirschfeldt require $f(q) < \alpha$; the two definitions agree, since for an irrational $\alpha$ the rational $f(q)$ is never equal to $\alpha$, and a rational $\alpha$ is reducible to every real in both senses (with $f$ constant). The definition makes sense for all reals, but the reducibility is well behaved only on left-c.e. reals, for which it has a description by approximations.

:::proposition[Calude, Coles, Hertling, Khoussainov]{#prop-solovay-approximations}
Let $\alpha$ and $\beta$ be left-c.e. reals with approximations $(\alpha_s)$ and $(\beta_s)$. Then $\alpha \leq_S \beta$ if and only if there are a constant $c$ and a computable function $g$ such that
$$
\alpha - \alpha_{g(n)} < c\, (\beta - \beta_n) \quad \text{for every } n.
$$
In particular, the condition does not depend on the approximations chosen.
:::

:::proof{of=prop-solovay-approximations}
Suppose that $\alpha \leq_S \beta$ with $c$ and $f$. Given $n$, $\beta_n < \beta$ is a rational, so $f(\beta_n)$ is defined, and $f(\beta_n) \leq \alpha$. If $f(\beta_n) < \alpha$, search for $m$ with $\alpha_m \geq f(\beta_n)$, which exists, and let $g(n)$ be the first such $m$. Then $\alpha - \alpha_{g(n)} \leq \alpha - f(\beta_n) < c(\beta - \beta_n)$. The search fails only if $f(\beta_n) = \alpha$, which happens only for a rational $\alpha$; then $\alpha$ is computable, and $g$ can be taken with $\alpha - \alpha_{g(n)} < \beta_{n+1} - \beta_n$, as in :ref{#ex-computable-least}.

Conversely, given $c$ and $g$, define $f(q)$ for a rational $q$ by searching for $n$ with $q < \beta_n$, and letting $f(q) = \alpha_{g(n)}$ for the first such $n$. If $q < \beta$, such an $n$ exists, $f(q) \leq \alpha$, and $\alpha - f(q) < c(\beta - \beta_n) < c(\beta - q)$.
:::

The characterization is easier to use than the definition. For instance, **$\leq_S$ is transitive**: if $\alpha - \alpha_{g(n)} < c(\beta - \beta_n)$ and $\beta - \beta_{h(n)} < d(\gamma - \gamma_n)$, then $\alpha - \alpha_{g(h(n))} < c(\beta - \beta_{h(n)}) < cd(\gamma - \gamma_n)$.

:::example{#ex-solovay-examples}
Let $\alpha$ and $\beta$ be left-c.e. reals.

1. $\alpha \leq_S \alpha + \beta$, with $g(n) = n$ and $c = 2$: $\alpha - \alpha_n \leq (\alpha + \beta) - (\alpha_n + \beta_n) < 2((\alpha + \beta) - (\alpha_n + \beta_n))$, the last inequality because the difference is positive.
2. $\alpha \leq_S k\alpha$ and $k \alpha \leq_S \alpha$ for every positive rational $k$, with $g(n) = n$ and constants $1/k + 1$ and $k + 1$.
3. If $\alpha$ is computable, then $\alpha \leq_S \beta$ for every left-c.e. real $\beta$ (:ref{#ex-computable-least}).
:::

The intuition of :ref{#prop-solovay-approximations} is that $\beta$ converges at most as fast as $\alpha$. A real with a slowly converging approximation is above reals with fast approximations, and the computable reals, which have approximations with a computable rate of convergence (:ref{#ex-computable-modulus}), are at the bottom.

## Solovay reducibility, computation and complexity

:::proposition{#prop-solovay-turing}
If $\alpha \leq_S \beta$, then $\alpha \leq_T \beta$.
:::

:::proof{of=prop-solovay-turing}
Let $c$ and $f$ be as in the definition. With oracle $\beta$, compute for each $n$ the rational $q_n = 0.(\beta \uh (n+1)) - 2^{-n-1}$, which satisfies $q_n < \beta$ and $\beta - q_n < 2^{-n}$. Then $f(q_n) \leq \alpha$ and $\alpha - f(q_n) < c\, 2^{-n}$. So $\alpha$ is the limit of a $\beta$-computable sequence of rationals with a computable rate of convergence, and $\alpha$ is $\beta$-computable, as in :ref{#ex-computable-modulus} relativized.
:::

The converse fails: a c.e. set and the left-c.e. real it defines are Turing equivalent, but Solovay reducibility distinguishes Turing equivalent reals (:ref{#ex-solovay-strict}).

The connection with randomness comes from complexity. A real close to another real has, at each length, about the same initial segment.

:::lemma[Solovay]{#lem-close-strings}
For every $k$ there is a constant $c_k$ such that for all $n$ and all strings $\sigma$ and $\tau$ of length $n$, if $|0.\sigma - 0.\tau| < 2^{k - n}$, then $K(\tau) \leq K(\sigma) + c_k$ and $C(\tau) \leq C(\sigma) + c_k$.
:::

:::proof{of=lem-close-strings}
The strings $\tau$ of length $n$ with $|0.\sigma - 0.\tau| < 2^{k-n}$ are those whose numbers $\lfloor 2^n \cdot 0.\tau \rfloor$ differ from that of $\sigma$ by less than $2^k$; there are fewer than $2^{k+1}$ of them, and they are computed from $\sigma$. A machine that, on an input $\rho\, \mu$ with $\rho$ in the domain of $U$ and $|\mu| = k + 1$, outputs the string of number $\lfloor 2^n \cdot 0.U(\rho) \rfloor + j - 2^k$ and length $n = |U(\rho)|$, where $j$ is the number written by $\mu$ in binary, is prefix-free, since its domain consists of the elements of the domain of $U$ followed by exactly $k + 1$ bits, and it describes $\tau$ with $K(\sigma) + k + 1$ bits. The constant $c_k$ is $k + 1$ plus the coding constant of this machine, which depends on $k$. For $C$, use the plain machine that reads $\mu$ first and then applies the optimal plain machine $V$ to the rest of the input.
:::

:::theorem[Solovay]{#thm-solovay-complexity}
If $\alpha \leq_S \beta$, then $K(\alpha \uh n) \leq^+ K(\beta \uh n)$ and $C(\alpha \uh n) \leq^+ C(\beta \uh n)$.
:::

:::proof{of=thm-solovay-complexity}
Let $c$ and $f$ be as in the definition, and $k$ with $2c + 3 < 2^k$. Let $b_n = 0.(\beta \uh n) - 2^{-n}$, a rational with $b_n < \beta$ and $\beta - b_n \leq 2^{-n+1}$, computed from $\beta \uh n$. Then $f(b_n) \leq \alpha$ and $\alpha - f(b_n) < 2c\, 2^{-n}$. Let $r_n$ be $f(b_n)$ moved into the interval $[0, 1 - 2^{-n}]$, that is, $r_n = \min(\max(f(b_n), 0), 1 - 2^{-n})$; since $\alpha \in [0, 1]$, $|\alpha - r_n| \leq |\alpha - f(b_n)| + 2^{-n}$. Let $\tau_n$ be the string of length $n$ with $0.\tau_n \leq r_n < 0.\tau_n + 2^{-n}$. Then
$$
|0.(\alpha \uh n) - 0.\tau_n| \leq |0.(\alpha \uh n) - \alpha| + |\alpha - r_n| + |r_n - 0.\tau_n| < (1 + 2c + 1 + 1)\, 2^{-n} < 2^{k - n}.
$$
By :ref{#lem-close-strings}, $K(\alpha \uh n) \leq K(\tau_n) + c_k$. The string $\tau_n$ is computed from $\beta \uh n$ by a fixed partial computable function, so $K(\tau_n) \leq^+ K(\beta \uh n)$. The same argument applies to $C$.
:::

:::corollary{#cor-above-random}
If $\alpha$ is Martin-Löf random and $\alpha \leq_S \beta$, then $\beta$ is Martin-Löf random.
:::

:::proof{of=cor-above-random}
By the Levin–Schnorr theorem (:ref{#thm-levin-schnorr}), $K(\alpha \uh n) \geq n - O(1)$, so $K(\beta \uh n) \geq K(\alpha \uh n) - O(1) \geq n - O(1)$, and $\beta$ is random by the same theorem.
:::

:::quiz[Solovay reducibility and complexity]
In the proof of :ref{#thm-solovay-complexity}, why is :ref{#lem-close-strings} needed, rather than computing $\alpha \uh n$ directly from $\beta \uh n$?

- [x] From $\beta \uh n$ one obtains a rational within $c\, 2^{-n}$ of $\alpha$, which determines $\alpha \uh n$ only up to a bounded number of candidates; the lemma pays a constant to choose among them.
- [ ] Because $f$ is only partial.

  $f$ is defined on every rational below $\beta$, in particular on $0.(\beta \uh n)$ when $\beta$ is irrational.
- [ ] Because $\alpha$ may be rational.

  Rational reals are computable and cause no difficulty; the issue is the precision $c\, 2^{-n}$, which does not fix the first $n$ bits.
:::

## The degrees of left-c.e. reals

The equivalence classes of $\equiv_S$ are the **Solovay degrees**. On left-c.e. reals they have a least element, the degree of the computable reals, by :ref{#ex-computable-least}, and addition induces a join.

:::proposition[Solovay; Downey, Hirschfeldt, Nies]{#prop-solovay-join}
Let $\alpha$, $\beta$ and $\gamma$ be left-c.e. reals. Then $\alpha \leq_S \alpha + \beta$ and $\beta \leq_S \alpha + \beta$, and if $\alpha \leq_S \gamma$ and $\beta \leq_S \gamma$, then $\alpha + \beta \leq_S \gamma$. So addition induces the least upper bound on the Solovay degrees of left-c.e. reals.
:::

:::proof{of=prop-solovay-join}
The first part is :ref{#ex-solovay-examples}. For the second, let $\alpha - \alpha_{g(n)} < c(\gamma - \gamma_n)$ and $\beta - \beta_{h(n)} < d(\gamma - \gamma_n)$, and $m(n) = \max(g(n), h(n))$. With the approximation $(\alpha_s + \beta_s)$ of $\alpha + \beta$,
$$
(\alpha + \beta) - (\alpha_{m(n)} + \beta_{m(n)}) \leq (\alpha - \alpha_{g(n)}) + (\beta - \beta_{h(n)}) < (c + d)(\gamma - \gamma_n).
$$
:::

Here we allow left-c.e. reals larger than $1$; a real and its fractional part have the same Solovay degree when the integer part is fixed. The Solovay degrees of left-c.e. reals have also a greatest element, the degree of $\Omega$.

:::theorem[Solovay]{#thm-omega-complete}
Every left-c.e. real $\alpha \in [0, 1]$ satisfies $\alpha \leq_S \Omega$.
:::

The optimal machine $U$ simulates every prefix-free machine $M$ on the descriptions beginning with a code $0^e 1$ of $M$. If $\alpha = \Omega_M$, the part of $\Omega$ coming from these descriptions is $2^{-e-1}\alpha$, and its approximation is at least as good as the approximation of $\Omega$ itself. So $\Omega$ cannot converge faster than $2^{-e-1}\alpha$.

:::proof{of=thm-omega-complete}
If $\alpha$ is rational, it is computable and :ref{#ex-computable-least} applies. Otherwise, by :ref{#thm-left-ce-halting}, $\alpha = \Omega_M$ for a prefix-free machine $M = M_e$. In the proof of :ref{#thm-optimal-prefix-free}, $\hat M_e = M$ and $U(0^e 1 \tau) = M(\tau)$. Let
$$
a_s = 2^{e+1} \sum \{ 2^{-|\sigma|} : \sigma = 0^e 1 \tau,\ |\sigma| \leq s,\ U(\sigma)[s]\converge \},
$$
a computable non-decreasing sequence of rationals, with limit $\Omega_M = \alpha$. The descriptions in the domain of $U$ that are not counted in $\Omega_s$ include those of the form $0^e 1 \tau$ not counted in $a_s$, so $\Omega - \Omega_s \geq 2^{-e-1}(\alpha - a_s)$. Define $f(q)$ by searching for $s$ with $\Omega_s > q$ and letting $f(q) = a_s$. If $q < \Omega$, then $f(q) \leq \alpha$ and
$$
\alpha - f(q) \leq 2^{e+1} (\Omega - \Omega_s) < 2^{e+1} (\Omega - q).
$$
:::

By :ref{#cor-above-random}, every real Solovay above $\Omega$, left-c.e. or not, is random. A left-c.e. real that is Solovay complete, that is, Solovay above every left-c.e. real, is called **Ω-like**. Ω-like reals are random, and the next lesson proves the converse for left-c.e. reals.

::::exercise[The least degree]{#ex-computable-least difficulty=1 objective="Show that the computable reals form the least Solovay degree of left-c.e. reals."}
Let $\beta$ be a left-c.e. real, with approximation $(\beta_s)$. Show that every computable real $\alpha$ satisfies $\alpha \leq_S \beta$. Show that if $\alpha \leq_S \beta$ and $\beta$ is computable, then $\alpha$ is computable.

:::solution
Let $\alpha$ be computable, and let $(a_m)$ be a computable sequence of rationals with $|\alpha - a_m| < 2^{-m}$. The difference $\delta_n = \beta_{n+1} - \beta_n$ is a positive rational, computable from $n$, and $\beta - \beta_n > \delta_n$. Let $m(n)$ be the least $m$ with $2^{-m+1} < \delta_n$, and $f(n) = a_{m(n)} - 2^{-m(n)}$, a rational with $f(n) < \alpha$ and $\alpha - f(n) < 2^{-m(n)+1} < \delta_n < \beta - \beta_n$. Defining $f$ on all rationals $q$ by searching for $n$ with $q < \beta_n$ and taking $f(n)$, as in the proof of :ref{#prop-solovay-approximations}, gives $\alpha \leq_S \beta$ with $c = 1$. For the second statement, $\alpha \leq_T \beta$ by :ref{#prop-solovay-turing}, and $\beta$ is computable.
:::
::::

## Notes and references

Solovay reducibility was introduced by Solovay in unpublished notes (1975), with :ref{#lem-close-strings}, :ref{#thm-solovay-complexity} and :ref{#thm-omega-complete}; Solovay called the complete left-c.e. reals Ω-like. The characterization by approximations is due to Calude, Coles, Hertling and Khoussainov (1999). Downey, Hirschfeldt and Nies (2002) studied the structure of the Solovay degrees of left-c.e. reals: it is a dense distributive upper semilattice, in which every incomplete degree splits, and Downey, Hirschfeldt and LaForte showed that its first-order theory is undecidable (admitted; Downey–Hirschfeldt, Section 9.5). Solovay reducibility does not imply weak truth-table reducibility (Downey, Hirschfeldt and LaForte; Downey–Hirschfeldt, Theorem 9.1.6).

- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished notes, IBM Thomas J. Watson Research Center, 1975.
- C. S. Calude, R. J. Coles, P. H. Hertling and B. Khoussainov, *Degree-theoretic aspects of computably enumerable reals*, in: Models and Computability, London Mathematical Society Lecture Note Series 259, Cambridge University Press, 1999, 23–39.
- R. G. Downey, D. R. Hirschfeldt and A. Nies, *Randomness, computability, and density*, SIAM Journal on Computing 31 (2002), 1169–1183.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 9.1, 9.2 and 9.5.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 3.2.

:::::exercises
::::exercise{#ex-solovay-rational-shift difficulty=1 objective="Check that Solovay degrees ignore rational translations."}
Let $\alpha$ be a left-c.e. real and $q$ a rational with $\alpha + q \in [0, 1]$. Show that $\alpha + q \equiv_S \alpha$.

:::solution
$(\alpha_s + q)$ is an approximation of $\alpha + q$, and $(\alpha + q) - (\alpha_n + q) = \alpha - \alpha_n$. By :ref{#prop-solovay-approximations} with $g(n) = n$ and $c = 2$, each real is Solovay reducible to the other.
:::
::::

::::exercise{#ex-solovay-sum-characterization difficulty=2 objective="Prove the easy direction of the characterization of Solovay reducibility by sums."}
Let $\alpha$, $\beta$ and $\gamma$ be left-c.e. reals and $d$ a positive integer with $d\beta = \alpha + \gamma$. Show that $\alpha \leq_S \beta$. (Downey, Hirschfeldt and Nies proved the converse: if $\alpha \leq_S \beta$, then $d\beta - \alpha$ is left-c.e. for some $d$; admitted.)

:::solution
Let $(\alpha_s)$ and $(\gamma_s)$ be approximations, and $p_s = (\alpha_s + \gamma_s)/d$, a computable strictly increasing sequence with limit $\beta$. Then $\alpha - \alpha_s \leq (\alpha + \gamma) - (\alpha_s + \gamma_s) = d(\beta - p_s) < (d + 1)(\beta - p_s)$. By :ref{#prop-solovay-approximations}, applied with the approximation $(p_s)$ of $\beta$ and $g(n) = n$, $\alpha \leq_S \beta$. (Downey–Hirschfeldt, Theorem 9.1.8.)
:::
::::

::::exercise{#ex-solovay-product difficulty=1 objective="Show that multiplication also bounds its factors in the Solovay degrees."}
Let $\alpha$ and $\beta$ be left-c.e. reals with $\beta > 0$. Show that $\alpha \leq_S \alpha\beta$.

:::solution
Take approximations with $\beta_0 > 0$, which is possible since $\beta > 0$: drop the terms that are not positive. With the approximation $(\alpha_s \beta_s)$ of $\alpha\beta$, for non-negative $\alpha_s$,
$$
\alpha\beta - \alpha_s\beta_s = \beta(\alpha - \alpha_s) + \alpha_s(\beta - \beta_s) \geq \beta_0 (\alpha - \alpha_s).
$$
So $\alpha - \alpha_s \leq \beta_0^{-1}(\alpha\beta - \alpha_s\beta_s) < (\beta_0^{-1} + 1)(\alpha\beta - \alpha_s\beta_s)$, and :ref{#prop-solovay-approximations} applies with $g(n) = n$.
:::
::::

::::exercise{#ex-solovay-strict difficulty=2 objective="See that Solovay reducibility is finer than Turing reducibility on left-c.e. reals."}
Show that $\Omega \not\leq_S r_A$ for every c.e. set $A$, where $r_A = \sum_{n \in A} 2^{-n-1}$. Deduce that $r_{\emptyset'} \equiv_T \Omega$ but $r_{\emptyset'} <_S \Omega$.

:::solution
By :ref{#cor-above-random}, $\Omega \leq_S r_A$ would make $r_A$ random. But a c.e. set $A$ is not random: if $A$ is infinite, it has an infinite computable subset $\{a_0 < a_1 < \cdots\}$, and the classes $\{ X : X(a_i) = 1 \text{ for } i < n \}$ are uniformly $\Sigma^0_1$, in fact clopen, of measure $2^{-n}$, and contain $A$; if $A$ is finite, it is computable. The binary expansion of $r_A$ is $A$ when $A$ is infinite and coinfinite, so $r_A$ is not random, and neither is it when $A$ is finite or cofinite, since $r_A$ is then rational. So $\Omega \not\leq_S r_A$. For $A = \emptyset'$, the reals $r_{\emptyset'}$ and $\Omega$ are Turing equivalent to $\emptyset'$ (:ref{#thm-omega}), $r_{\emptyset'} \leq_S \Omega$ by :ref{#thm-omega-complete}, and $\Omega \not\leq_S r_{\emptyset'}$.
:::
::::

:::::
