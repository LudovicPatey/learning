---
title: Solovay functions and random sums
summary: A computable function f with a finite sum of 2^(-f(n)) is a Solovay function, tight for K infinitely often, if and only if this sum is Martin-Löf random (Bienvenu, Downey); computable upper bounds for K that are tight infinitely often exist.
duration: 30
prerequisites: [kucera-slaman, kolmogorov-complexity/prefix-free-symmetry]
---

The function $K$ is not computable, and no computable function is equal to $K$ up to a constant. But some computable functions $f$ bound $K$ from above, $K(n) \leq^+ f(n)$, and are **tight** infinitely often: $f(n) \leq^+ K(n)$ for infinitely many $n$. Solovay built such functions, now called **Solovay functions**; the course on K-trivial sets uses them to give a computable form of the definition of K-triviality.

A computable bound $f$ for $K$ is the same as a computable function with $\sum_n 2^{-f(n)} < \infty$, by the KC theorem. Bienvenu and Downey found that whether such a bound is tight infinitely often depends only on the real $\sum_n 2^{-f(n)}$: $f$ is a Solovay function if and only if this sum is random. The proof is an application of the Kučera–Slaman theorem in one direction, and of a conditional version of the KC theorem in the other. It shows how the theory of left-c.e. reals can answer a question that does not mention them.

## Computable upper bounds for K

:::definition[Solovay]{#def-solovay-bound}
A **Solovay function** is a computable function $f : \nat \to \nat$ such that $K(n) \leq^+ f(n)$ for every $n$, and $f(n) \leq^+ K(n)$ for infinitely many $n$, that is, $\liminf_n (f(n) - K(n)) < \infty$.
:::

This is the notion of the course on K-trivial sets, where a particular Solovay function is built. For instance, $f(n) = 2 \lfloor \log(n + 1) \rfloor + 2$ satisfies the first condition but not the second, since $K(n) \leq^+ \log n + 2 \log \log n$ for $n \geq 4$ (:ref{#ex-k-iterated-log}).

:::proposition{#prop-computable-bound}
For a computable function $f$, $K(n) \leq^+ f(n)$ for every $n$ if and only if $\sum_n 2^{-f(n)} < \infty$.
:::

:::proof{of=prop-computable-bound}
If $K(n) \leq f(n) + c$ for every $n$, then $\sum_n 2^{-f(n)} \leq 2^c \sum_n 2^{-K(n)} \leq 2^c$, by :ref{#prop-k-basic} (4). Conversely, if $\sum_n 2^{-f(n)} \leq 2^d$, the requests $(n, f(n) + d)$ form a bounded computable request set, and :ref{#thm-kc} gives $K(n) \leq^+ f(n) + d$.
:::

## The theorem of Bienvenu and Downey

:::theorem[Bienvenu, Downey]{#thm-bienvenu-downey}
Let $f$ be a computable function with $\alpha = \sum_n 2^{-f(n)} < \infty$. Then $f$ is a Solovay function if and only if $\alpha$ is Martin-Löf random.
:::

Both directions say that the first bits of $\alpha$ and the tail of the series $\sum_n 2^{-K(n)}$ control each other. If $\alpha$ is not random, it has short descriptions of its prefixes $\alpha \uh k$, and each such prefix tells how far to go in the series $\sum 2^{-f(n)}$ for the tail to be smaller than $2^{-k}$; beyond that point, the KC theorem compresses every $n$ by about $k$ bits, given $\alpha \uh k$. So $K(n) \leq f(n) - c$ for almost all $n$. If $\alpha$ is random, it is Ω-like, and its prefixes tell how far to go in the enumeration of $\dom U$ for the remaining weight, which bounds the tail of $\sum 2^{-K(n)}$, to be smaller than about $2^{-k}$; if $f$ were much larger than $K$ almost everywhere, the tail of $\sum 2^{-f(n)}$ would be much smaller, and $\alpha \uh k$ would determine more bits of $\alpha$, which contradicts randomness.

:::proof{of=thm-bienvenu-downey}
Let $S_m = \sum_{n < m} 2^{-f(n)}$, a computable non-decreasing sequence of rationals with limit $\alpha$.

*If $\alpha$ is not random, $f$ is not a Solovay function.* For a string $\rho$, let $m(\rho)$ be the least $m$, if any, with $S_m > 0.\rho - 2^{-|\rho|}$. Let $S$ be the c.e. set of triples $(n, f(n) - |\rho| + 1, \rho)$ with $m(\rho)$ defined, $n \geq m(\rho)$ and $f(n) - |\rho| + 1 \geq 0$, and $R$ its truncation, as in :ref{#lem-conditional-kc} and the remark following it. For $\rho = \alpha \uh k$, we have $0.\rho \leq \alpha$, so $m(\rho)$ is defined, and
$$
\sum_{n \geq m(\rho)} 2^{-f(n)} = \alpha - S_{m(\rho)} < \alpha - 0.\rho + 2^{-k} \leq 2^{-k+1};
$$
so the weight of $S_\rho$ is less than $2^{-k+1} 2^{k-1} = 1$, and $R_\rho = S_\rho$. By :ref{#lem-conditional-kc}, there is $b$ such that for every $k$ and every $n \geq m(\alpha \uh k)$ with $f(n) \geq k - 1$,
$$
K(n \mid \alpha \uh k) \leq f(n) - k + b.
$$
The prefix-free machine that, on input $\mu\nu$ with $\mu$ in the domain of $U$, outputs $U_{\mathrm c}(\nu, U(\mu))$ shows that $K(n) \leq^+ K(\rho) + K(n \mid \rho)$ for all $n$ and $\rho$. Let $c$ be given. Since $\alpha$ is not random, there is $k$ with $K(\alpha \uh k) \leq k - c$, by the Levin–Schnorr theorem (:ref{#thm-levin-schnorr}). Then for all $n \geq m(\alpha \uh k)$ with $f(n) \geq k - 1$,
$$
K(n) \leq K(\alpha \uh k) + f(n) - k + b + b' \leq f(n) - c + b + b',
$$
where $b'$ is the constant of the machine. Since $\sum_n 2^{-f(n)} < \infty$, $f(n) \to \infty$, so the condition $f(n) \geq k - 1$ holds for almost all $n$. So $f(n) - K(n) \geq c - b - b'$ for almost all $n$. As $c$ is arbitrary, $f(n) - K(n) \to \infty$, and $f$ is not a Solovay function.

*If $\alpha$ is random, $f$ is a Solovay function.* By :ref{#prop-computable-bound}, $K \leq^+ f$. Suppose that $f(n) - K(n) \to \infty$; we show that $\alpha$ is not random. By :ref{#thm-kucera-slaman}, $\Omega \leq_S \alpha$: there are $d$ and a partial computable $g$ with $g(q) \leq \Omega$ and $\Omega - g(q) < 2^d(\alpha - q)$ for every rational $q < \alpha$.

Given $\rho = \alpha \uh k$, the rational $q = 0.\rho$ satisfies $q < \alpha$ and $\alpha - q < 2^{-k}$, since $\alpha$ is irrational. So $\Omega - g(q) < 2^{d - k}$. Search for a stage $s$ with $\Omega_s \geq g(q)$; if $g(q) = \Omega$, then $\Omega$ would be rational, which it is not, so $g(q) < \Omega$ and the search terminates. Let $t$ be larger than $s$ and than every number output by a description in the domain of $U$ converging by stage $s$. Then the shortest descriptions of the numbers $n \geq t$ converge after stage $s$, so
$$
\sum_{n \geq t} 2^{-K(n)} \leq \Omega - \Omega_s < 2^{d - k}.
$$
The number $t = t(\rho)$ is computed from $\rho$. Fix $c$, and let $N$ be such that $f(n) \geq K(n) + c + d$ for $n \geq N$. If $t(\alpha \uh k) \geq N$, then
$$
\alpha - S_{t(\alpha \uh k)} = \sum_{n \geq t(\alpha \uh k)} 2^{-f(n)} \leq 2^{-c-d} \sum_{n \geq t(\alpha \uh k)} 2^{-K(n)} < 2^{-k-c}.
$$
The numbers $t(\alpha \uh k)$ tend to infinity with $k$: they are at least the stage $s$, and $\Omega - \Omega_s < 2^{d-k}$ forces $s \to \infty$. So for all $k$ larger than some $k_c$, the rational $S_{t(\alpha \uh k)}$, computed from $\alpha \uh k$, is within $2^{-k-c}$ below $\alpha$, and $\alpha \uh (k + c)$ is one of the at most two strings $\tau$ of length $k + c$ with $[0.\tau, 0.\tau + 2^{-k-c})$ meeting $[S_{t(\alpha \uh k)}, S_{t(\alpha \uh k)} + 2^{-k-c})$. A description of $\alpha \uh k$, a description of $c$ and one bit describe $\alpha \uh (k + c)$, by a prefix-free machine independent of $c$:
$$
K(\alpha \uh (k + c)) \leq K(\alpha \uh k) + K(c) + e \leq K(\alpha \uh k) + 2 \log c + e'
$$
for $k \geq k_c$, with constants $e, e'$ independent of $c$ and $k$. Choose $c \geq 2$ with $2 \log c + e' \leq c/2$. By induction on $j$, $K(\alpha \uh (k_c + jc)) \leq K(\alpha \uh k_c) + jc/2$, so $K(\alpha \uh m) \leq m/2 + O(1)$ for infinitely many $m$, and $\alpha$ is not random by the Levin–Schnorr theorem.
:::

:::quiz[the theorem of Bienvenu and Downey]
In the first part of the proof of :ref{#thm-bienvenu-downey}, why are the requests issued with the condition $\rho = \alpha \uh k$, rather than without condition?

- [x] The point $m(\rho)$ beyond which the tail of the series is smaller than $2^{-k+1}$ is computed from $\rho$; without $\rho$, the requests of length $f(n) - k + 1$ could not be restricted to the tail, and their weight would not be bounded.
- [ ] Because $K(n \mid \rho) \leq K(n)$.

  This inequality holds but plays no role; the proof needs the reverse kind of bound, an upper bound on $K(n)$.
- [ ] Because $\alpha$ is computable from $\rho$.

  $\rho$ is a finite prefix of $\alpha$, which is not computable when it is random; only a rational approximation of $\alpha$ is obtained.

---

In the second part, where is the Kučera–Slaman theorem used?

- [x] To convert a prefix of $\alpha$ into a good lower approximation of $\Omega$, which bounds the tail of $\sum_n 2^{-K(n)}$ through the remaining weight of the domain of $U$.
- [ ] To show that $\alpha$ is left-c.e.

  $\alpha$ is left-c.e. by definition, as the limit of the partial sums $S_m$.
- [ ] To show that $K \leq^+ f$.

  This is :ref{#prop-computable-bound}, which uses the KC theorem only.
:::

## Existence of Solovay functions

:::corollary[Solovay]{#cor-solovay-functions-exist}
There is a Solovay function.
:::

:::proof{of=cor-solovay-functions-exist}
By the proof of :ref{#thm-left-ce-halting}, there is a computable sequence $(n_i)$ with $\sum_i 2^{-n_i} = \Omega$. The function $f(i) = n_i$ is computable, and $\sum_i 2^{-f(i)} = \Omega$ is random, so $f$ is a Solovay function by :ref{#thm-bienvenu-downey}.
:::

The corollary shows that a computable sequence of numbers whose probabilities $2^{-n_i}$ add up to a random real cannot be compressed, at infinitely many places, by more than a constant: the decomposition of $\Omega$ into powers of $2$ is a computable sequence of description lengths that $K$ matches infinitely often. Bienvenu and Downey also deduced that there are non-decreasing Solovay functions, from a computable non-increasing sequence of powers of $2$ with a random sum (Downey–Hirschfeldt, Corollary 9.4.2).

::::exercise[Computable sums]{#ex-computable-sum-not-solovay difficulty=1 objective="Apply the theorem of Bienvenu and Downey to show that simple computable bounds are not tight."}
Show that if $f$ is computable and $\sum_n 2^{-f(n)}$ is a computable real, then $f(n) - K(n) \to \infty$. Apply this to $f(n) = 2 \lfloor \log(n + 1) \rfloor + 2$ and to $f(n) = \lfloor \log(n + 1) \rfloor + 2 \lfloor \log(\lfloor \log(n+1) \rfloor + 1) \rfloor + 2$.

:::solution
A computable real is not random, so by :ref{#thm-bienvenu-downey}, $f$ is not a Solovay function; since $K \leq^+ f$ by :ref{#prop-computable-bound}, this means $f(n) - K(n) \to \infty$. For $f(n) = 2\ell + 2$ with $\ell = \lfloor \log(n + 1) \rfloor$, there are $2^\ell$ numbers $n$ with a given $\ell$, namely $2^\ell - 1 \leq n < 2^{\ell + 1} - 1$, so $\sum_n 2^{-f(n)} = \sum_\ell 2^\ell 2^{-2\ell - 2} = \sum_\ell 2^{-\ell - 2} = \tfrac12$, a computable real. For the second function, with $m = \lfloor \log(\ell + 1) \rfloor$, the sum is $\sum_\ell 2^\ell 2^{-\ell - 2m - 2} = \sum_\ell 2^{-2 \lfloor \log(\ell+1) \rfloor - 2}$, which is $\sum_m 2^m 2^{-2m-2} = \tfrac12$ by the same computation. So $f(n) - K(n) \to \infty$ for both functions.
:::
::::

## Notes and references

Solovay functions are due to Solovay (1975), who built one explicitly. The characterization by random sums is due to Bienvenu and Downey (2009); Downey and Hirschfeldt present it as Theorem 9.4.1, with the proof followed here. Bienvenu, Downey, Nies and Merkle (2015) survey the applications of Solovay functions, including the characterization of K-triviality by a computable bound used in the course on K-trivial sets.

- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished notes, IBM Thomas J. Watson Research Center, 1975.
- L. Bienvenu and R. Downey, *Kolmogorov complexity and Solovay functions*, in: STACS 2009, Leibniz International Proceedings in Informatics 3, 2009, 147–158.
- L. Bienvenu, R. Downey, A. Nies and W. Merkle, *Solovay functions and their applications in algorithmic randomness*, Journal of Computer and System Sciences 81 (2015), 1575–1591.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 9.4.

:::::exercises
::::exercise{#ex-solovay-shift difficulty=1 objective="Check that Solovay functions are stable under bounded perturbations and computable reorderings."}
Let $f$ be a Solovay function. Show that $f + c$ is a Solovay function for every constant $c$, and that $f \circ \pi$ is a Solovay function for every computable permutation $\pi$ of $\nat$.

:::solution
$K \leq^+ f + c$ and $f + c \leq^+ K$ at the same arguments as $f$. For $f \circ \pi$: $K(n) \leq^+ K(\pi(n))$, since $n = \pi^{-1}(\pi(n))$ is computed from $\pi(n)$, and $K(\pi(n)) \leq^+ f(\pi(n))$; so $K \leq^+ f \circ \pi$. If $f(m) \leq K(m) + c$ for infinitely many $m$, then for $n = \pi^{-1}(m)$, $f(\pi(n)) \leq K(m) + c \leq K(n) + c + O(1)$, since $m = \pi(n)$ is computed from $n$; these $n$ are infinitely many. Alternatively, $\sum_n 2^{-f(\pi(n))} = \sum_m 2^{-f(m)}$ and :ref{#thm-bienvenu-downey} applies, and for $f + c$, $\sum 2^{-f(n) - c} = 2^{-c}\sum 2^{-f(n)}$ is random if and only if $\sum 2^{-f(n)}$ is, by :ref{#ex-solovay-examples} and :ref{#cor-above-random}.
:::
::::

::::exercise{#ex-solovay-interleave difficulty=2 objective="Check a closure property of Solovay functions in two ways, directly and through the sums."}
Let $f$ be a Solovay function and $h$ a computable function with $\sum_n 2^{-h(n)} < \infty$. Let $k(2n) = f(n)$ and $k(2n + 1) = h(n)$. Show that $k$ is a Solovay function, first directly, then with :ref{#thm-bienvenu-downey}.

:::solution
*Directly.* The maps $n \mapsto 2n$ and $n \mapsto 2n + 1$ and their inverses on even and odd numbers are computable, so $K(2n) =^+ K(n) =^+ K(2n + 1)$. Hence $K(2n) \leq^+ f(n) = k(2n)$, and $K(2n + 1) \leq^+ h(n) = k(2n + 1)$ by :ref{#prop-computable-bound}. At the infinitely many $n$ with $f(n) \leq K(n) + c$, we get $k(2n) \leq K(2n) + c + O(1)$.

*Through the sums.* $\sum_m 2^{-k(m)} = \sum_n 2^{-f(n)} + \sum_n 2^{-h(n)}$. The first sum is random by :ref{#thm-bienvenu-downey}, and the second is left-c.e. If the total is less than $1$, it is random by :ref{#cor-random-left-ce} (2); in general, it is a random real plus a left-c.e. real, and the same argument, $\Omega \leq_S \sum 2^{-f(n)} \leq_S \sum 2^{-k(m)}$ by :ref{#prop-solovay-join}, with :ref{#cor-above-random}, shows that it is random whatever its integer part, since the fractional part of a real has the same Solovay degree when the integer part is fixed. By :ref{#thm-bienvenu-downey}, $k$ is a Solovay function.
:::
::::
:::::
