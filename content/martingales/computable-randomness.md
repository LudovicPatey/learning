---
title: Computable randomness
summary: Sequences on which no computable martingale succeeds; rational-valued martingales suffice; there is no universal computable martingale; computably random sequences satisfy the law of large numbers and are characterized by the convergence of computable martingales.
duration: 30
prerequisites: [schnorr-theorem]
---

A c.e. martingale is a strategy whose bets are not known to the gambler: she only learns lower bounds on her capital. Schnorr argued that a betting strategy, as an algorithm, should compute its bets. Restricting to computable martingales gives a notion of randomness, computable randomness, that is implied by Martin-Löf randomness. This lesson proves its first properties: the reduction to rational values, the absence of a universal strategy, the law of large numbers, and the convergence of computable strategies along computably random sequences. The next lesson shows that the implication from Martin-Löf randomness is strict.

## Computable martingales

:::definition[Schnorr]{#def-computably-random}
A sequence is **computably random** if no computable martingale succeeds on it.
:::

By :ref{#def-ce-martingale}, the values of a computable martingale are computable reals, which an algorithm can only approximate. Rational values computed exactly are more convenient, and they suffice.

:::lemma[Schnorr]{#lem-rational-martingale}
For every computable martingale $d$ there is a martingale $f$ with rational values, such that $f(\sigma)$ is computable from $\sigma$ and $d(\sigma) < f(\sigma) < d(\sigma) + 1$ for every $\sigma$. In particular $S[f] = S[d]$.
:::

:::proof{of=lem-rational-martingale}
Choose a rational $f(\varepsilon)$ in the open interval $(d(\varepsilon), d(\varepsilon) + 1)$: such a rational can be found by searching, since strict inequalities between a rational and a computable real are verified by sufficiently good approximations. Suppose $f(\sigma)$ is defined, with $\delta = f(\sigma) - d(\sigma) \in (0, 1)$. We look for a rational $r$ with
$$
d(\sigma 0) < r < d(\sigma 0) + 1 \quad\text{and}\quad d(\sigma 1) < 2 f(\sigma) - r < d(\sigma 1) + 1.
$$
Such rationals exist: since $2 f(\sigma) = d(\sigma 0) + d(\sigma 1) + 2\delta$, the conditions hold for every $r$ with $|r - (d(\sigma 0) + \delta)| < \min(\delta, 1 - \delta)$. They form an open set of rationals, and the search for one of them, verifying the four strict inequalities on approximations, terminates. Let $f(\sigma 0) = r$ and $f(\sigma 1) = 2 f(\sigma) - r$. Then $f$ is a martingale, positive since $f > d \geq 0$, and $f$ is bounded along a sequence if and only if $d$ is.
:::

From now on, computable martingales are taken rational-valued whenever convenient. The first properties of computable randomness follow from the previous lessons.

:::proposition{#prop-cr-basic}
1. Every Martin-Löf random sequence is computably random.
2. For every computable martingale $d$, there is a computable sequence on which $d$ does not succeed. In particular, no computable martingale succeeds on every sequence that is not computably random.
3. No computable sequence is computably random.
:::

:::proof{of=prop-cr-basic}
1. A computable martingale is c.e.; apply :ref{#thm-schnorr-martingales}.
2. Let $f$ be as in :ref{#lem-rational-martingale}. The leftmost non-ascending path $X$ of $f$ (:ref{#lem-non-ascending}) is computable, since the comparisons $f((X \uh n) 0) \leq f(X \uh n)$ are between computable rationals, and $d(X \uh n) < f(X \uh n) \leq f(\varepsilon)$ for every $n$. By (3), the sequence $X$ is not computably random, and $d$ does not succeed on it.
3. If $X$ is computable, the martingale $E_X$ that bets its whole capital on $X(n)$ at every step, $E_X(\sigma) = 2^{|\sigma|}$ if $\sigma \prec X$ and $0$ otherwise, is computable and succeeds on $X$.
:::

Contrast (2) with the universal c.e. martingale of :ref{#cor-universal-ce-martingale}: there is no universal computable martingale. The theory of computable randomness has no universal object, which makes it harder; the construction of the next lesson replaces the universal object by a combination of countably many strategies, controlled by an oracle.

## The law of large numbers

The proportional strategy of :ref{#ex-martingales} detects an excess of ones, with a capital that grows exponentially.

:::lemma{#lem-proportional}
Let $\delta \in (0, \frac12]$ be rational. If a string $\sigma$ of length $n$ contains at least $(\frac12 + \delta) n$ ones, then $p_\delta(\sigma) \geq e^{5 \delta^2 n / 4}$.
:::

:::proof{of=lem-proportional}
The value $p_\delta(\sigma) = (1 + \delta)^k (1 - \delta)^{n-k}$ increases with the number $k$ of ones, so $p_\delta(\sigma) \geq e^{n g(\delta)}$ with
$$
g(\delta) = (\tfrac12 + \delta) \ln(1 + \delta) + (\tfrac12 - \delta) \ln(1 - \delta).
$$
For $0 \leq x \leq \frac12$, $\ln(1 + x) \geq x - \frac{x^2}{2}$ and $\ln(1 - x) \geq -x - x^2$: both differences vanish at $0$ and have derivatives $\frac{x^2}{1+x} \geq 0$ and $\frac{x(1 - 2x)}{1 - x} \geq 0$. Hence
$$
g(\delta) \geq (\tfrac12 + \delta)(\delta - \tfrac{\delta^2}{2}) - (\tfrac12 - \delta)(\delta + \delta^2) = \tfrac54 \delta^2 + \tfrac12 \delta^3 \geq \tfrac54 \delta^2.
$$
:::

:::proposition{#prop-cr-lln}
If $X$ is computably random, then the frequency of ones in $X \uh n$ tends to $\frac12$.
:::

:::proof{of=prop-cr-lln}
If not, there is a rational $\delta \in (0, \frac12]$ such that $X \uh n$ has at least $(\frac12 + \delta) n$ ones for infinitely many $n$, or at least $(\frac12 + \delta) n$ zeros for infinitely many $n$. In the first case, $p_\delta$ is computable and $p_\delta(X \uh n) \geq e^{5\delta^2 n/4}$ for infinitely many $n$ by :ref{#lem-proportional}, so $p_\delta$ succeeds on $X$. In the second case, the same holds for the strategy that bets the fraction $\delta$ of its capital on the bit $0$.
:::

The capital of $p_\delta$ is not only unbounded along such a sequence: it exceeds a computable function of $n$, $e^{5\delta^2 n/4}$, at infinitely many lengths. This additional information will show that the law of large numbers holds for the weaker notion of Schnorr randomness (:ref{to="martingales/schnorr-randomness"}). The following exercise extends the proposition to subsequences selected by computable rules.

::::exercise{#ex-church-stochastic difficulty=2 objective="Combine a computable selection rule with the proportional strategy to show that computably random sequences are Church stochastic."}
A **computable selection rule** is a computable function $s : \bstr \to \{0, 1\}$; it **selects** the position $n$ in $X$ if $s(X \uh n) = 1$. Let $X$ be computably random and $s$ a computable selection rule that selects infinitely many positions in $X$. Show that the frequency of ones among the first $m$ selected bits of $X$ tends to $\frac12$ as $m$ tends to infinity. (Computably random sequences are **Church stochastic**.)

:::solution
Suppose that for a rational $\delta \in (0, \frac12]$, infinitely often, at least $(\frac12 + \delta) m$ of the first $m$ selected bits are ones (the case of zeros is symmetric). Let $d(\varepsilon) = 1$, and at a string $\sigma$ with $s(\sigma) = 1$ bet the fraction $\delta$ of the capital on $1$: $d(\sigma 1) = (1 + \delta) d(\sigma)$, $d(\sigma 0) = (1 - \delta) d(\sigma)$; at a string with $s(\sigma) = 0$, do not bet. Then $d$ is a computable rational-valued martingale, and when the selected bits among the first $n$ positions of $X$ are $m$ in number with $k$ ones, $d(X \uh n) = (1 + \delta)^k (1 - \delta)^{m-k}$. By the computation of :ref{#lem-proportional}, this is at least $e^{5\delta^2 m/4}$ at infinitely many $n$, with $m$ tending to infinity. So $d$ succeeds on $X$, a contradiction.
:::
::::

## Convergence of computable martingales

Along a computably random sequence, a computable martingale is bounded. It also converges: a strategy whose capital oscillates can be turned into a strategy that profits from the oscillation.

:::theorem{#thm-cr-limits}
A sequence $X$ is computably random if and only if, for every computable martingale $d$, the limit $\lim_n d(X \uh n)$ exists and is finite.
:::

:::proof{of=thm-cr-limits}
($\Leftarrow$) A martingale with a finite limit along $X$ is bounded along $X$.

($\Rightarrow$) Let $X$ be computably random and $d$ a computable martingale. The capital $d(X \uh n)$ is bounded, since $X$ is computably random. Suppose it does not converge. Then there are rationals $r < s$ with $d(X \uh n) < r$ for infinitely many $n$ and $d(X \uh n) > s$ for infinitely many $n$; necessarily $r > 0$. Choose rationals $r < r_1 < s_1 < s$ and $\eta = 2^{-k}$ with $r_1 + \eta < s_1 - \eta$, $r + \eta < r_1$ and $s - \eta > s_1$, and let $q(\sigma)$ be a rational with $|q(\sigma) - d(\sigma)| \leq \eta$, computed from $\sigma$.

Define a martingale $\hat d$ with $\hat d(\varepsilon) = 1$ that alternates between two modes along each sequence. It starts in the **waiting** mode, in which it does not bet. When it reaches a string $\sigma_0$ with $q(\sigma_0) < r_1$, it switches to the **copying** mode, in which it bets like $d$, scaled by the factor $c = \hat d(\sigma_0)/(r_1 + \eta)$:
$$
\hat d(\sigma' i) = \hat d(\sigma') + c\, \big(d(\sigma' i) - d(\sigma')\big).
$$
When it reaches a string $\sigma$ with $q(\sigma) > s_1$, it returns to the waiting mode. The mode at a string is computed from the rationals $q$ on its prefixes, so $\hat d$ is a computable martingale. During a copying period started at $\sigma_0$, $\hat d(\sigma') = \hat d(\sigma_0) + c\,(d(\sigma') - d(\sigma_0)) \geq c\, d(\sigma') \geq 0$, since $c\, d(\sigma_0) < c\,(r_1 + \eta) = \hat d(\sigma_0)$; so $\hat d$ is non-negative.

Along $X$, the switches happen infinitely often: $d(X \uh n) < r$ gives $q(X \uh n) < r + \eta < r_1$, and $d(X \uh n) > s$ gives $q(X \uh n) > s - \eta > s_1$. A copying period that ends at $\sigma$ has $d(\sigma) > s_1 - \eta$, so it multiplies the capital of $\hat d$ by at least $(s_1 - \eta)/(r_1 + \eta) > 1$, and the waiting periods leave it unchanged. Hence $\hat d$ succeeds on $X$, a contradiction.
:::

The technique of the proof, **switching between strategies along a sequence** according to the values already observed, is a basic tool for computable martingales: a computable strategy may decide at each string, by a computation on the prefix, which of several strategies to follow. The savings trick of :ref{#prop-savings} is another instance.

:::quiz[convergence of computable martingales]
In the proof of :ref{#thm-cr-limits}, why does the new strategy copy $d$ only between a value below $r$ and a value above $s$?

- [x] So that each copying period multiplies its capital by more than $s/r > 1$, while the waiting periods, in which $d$ may lose, leave its capital unchanged.
- [ ] To keep $\hat d$ bounded by $d$.

  $\hat d$ grows unboundedly along $X$ while $d$ is bounded there.
- [ ] Because $d$ is not defined between the switching times.

  $d$ is total; the switching only selects the periods in which copying it is profitable.

---

Where is the computability of $d$ used?

- [x] To make $\hat d$ computable: the mode at a string is computed by comparing rational approximations of the values of $d$ on its prefixes with $r_1$ and $s_1$, and the bets are computed from the values of $d$.
- [ ] To show that $d$ is bounded along $X$.

  Boundedness follows from the computable randomness of $X$, applied to $d$.
- [ ] To find $r$ and $s$.

  The rationals $r$, $s$, $r_1$, $s_1$ are fixed numbers given by the failure of convergence; they need not be found effectively.
:::

## Notes and references

Computable randomness was introduced by Schnorr (1971), who also proved :ref{#lem-rational-martingale}. :ref{#thm-cr-limits} is folklore (Downey–Hirschfeldt, Theorem 7.1.3); the proof given here copies $d$ additively, which avoids dividing by values of $d$ that are only approximated. Church stochasticity goes back to Church (1940), who proposed computable selection rules to make von Mises's definition precise; the implication from computable randomness is discussed by Downey and Hirschfeldt in Section 7.4.1. Downey and Hirschfeldt present computable randomness in Section 7.1.1 (Definition 7.1.1, Proposition 7.1.2) and the absence of an effective enumeration of computable martingales in Proposition 7.1.12; Nies in Section 7.3 (Definition 7.3.1, Proposition 7.3.8, Proposition 7.3.9, Exercise 7.3.11).

- C.-P. Schnorr, *Zufälligkeit und Wahrscheinlichkeit*, Lecture Notes in Mathematics 218, Springer, 1971.
- C.-P. Schnorr, *A unified approach to the definition of a random sequence*, Mathematical Systems Theory 5 (1971), 246–258.
- A. Church, *On the concept of a random sequence*, Bulletin of the American Mathematical Society 46 (1940), 130–135.
- J. L. Doob, *Stochastic Processes*, Wiley, New York, 1953.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 7.1 and 7.4.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 7.3.

:::::exercises
::::exercise{#ex-cr-supermartingale difficulty=1 objective="Check that computable supermartingales define the same notion of randomness as computable martingales."}
Show that a sequence is computably random if and only if no computable supermartingale succeeds on it.

:::solution
A martingale is a supermartingale. Conversely, let $d$ be a computable supermartingale, and let $d'$ be the martingale of :ref{#lem-martingale-basic} (3), $d'(\sigma) = d(\sigma) + \sum_{\rho \prec \sigma} r(\rho)$ with $r(\rho) = d(\rho) - \frac12(d(\rho 0) + d(\rho 1))$. Each $r(\rho)$ is a computable real, uniformly in $\rho$, and the sum is finite, so $d'$ is a computable martingale; it is above $d$, so it succeeds wherever $d$ does.
:::
::::

::::exercise{#ex-cr-shift difficulty=1 objective="Transfer a computable strategy along a shift of the sequence, in both directions."}
Show that if $X$ is computably random, then so are $\sigma X$ for every string $\sigma$ and the tail $X(1) X(2) \cdots$.

:::solution
If a computable martingale $d$ succeeds on $\sigma X$, then $\rho \mapsto d(\sigma\rho)$ is a computable martingale that succeeds on $X$. If $d$ succeeds on the tail $Y$ of $X$, let $d'(\varepsilon) = d(\varepsilon)$ and $d'(i\rho) = d(\rho)$ for $i \in \{0, 1\}$: $d'$ does not bet on the first bit, then copies $d$. It is a computable martingale and $d'(X \uh (n+1)) = d(Y \uh n)$, so it succeeds on $X$.
:::
::::

::::exercise{#ex-cr-predictable difficulty=1 objective="Bet on a computable set of positions where the bits are known, and deduce that no c.e. set is computably random."}
1. Let $X$ be a sequence and $R = \{ r_0 < r_1 < \cdots \}$ an infinite computable set such that the function $i \mapsto X(r_i)$ is computable. Show that $X$ is not computably random.
2. Identifying a set with its characteristic sequence, deduce that no c.e. set and no co-c.e. set is computably random.

:::solution
1. Let $d(\varepsilon) = 1$. At a string $\sigma$ with $|\sigma| = r_i$, bet the whole capital on $X(r_i)$: $d(\sigma b) = 2 d(\sigma)$ if $b = X(r_i)$, and $d(\sigma b) = 0$ otherwise. At a string whose length is not in $R$, do not bet. Since $R$ is decidable and $i \mapsto X(r_i)$ is computable, $d$ is a computable rational-valued martingale, and $d(X \uh n) = 2^{|R \cap [0, n)|}$ tends to infinity.
2. Let $A$ be c.e. If $A$ is finite, it is computable, hence not computably random by :ref{#prop-cr-basic} (3). Otherwise, $A$ has an infinite computable subset $R$ (enumerate $A$ and keep each element larger than all the elements kept before), and $A(r) = 1$ for every $r \in R$; apply (1). If $A$ is co-c.e., apply the same argument to its complement, on which $A$ takes the value $0$.
:::
::::

::::exercise{#ex-cr-xor difficulty=1 objective="Transport a computable strategy along a computable bijection of Cantor space that preserves prefixes."}
Let $X$ be computably random and $C$ a computable sequence, and let $Y(n) = X(n) + C(n) \bmod 2$. Show that $Y$ is computably random.

:::solution
For a string $\sigma$, let $\sigma \oplus C$ be the string of the same length with $(\sigma \oplus C)(i) = \sigma(i) + C(i) \bmod 2$. The map $\sigma \mapsto \sigma \oplus C$ is computable, and $(\sigma i) \oplus C = (\sigma \oplus C)\, j$ with $j = i + C(|\sigma|) \bmod 2$, so it sends the two children of $\sigma$ to the two children of $\sigma \oplus C$. Let $d$ be a computable martingale that succeeds on $Y$, and $d'(\sigma) = d(\sigma \oplus C)$. Then $d'(\sigma 0) + d'(\sigma 1) = d((\sigma \oplus C) 0) + d((\sigma \oplus C) 1) = 2 d'(\sigma)$, $d'$ is computable, and $d'(X \uh n) = d(Y \uh n)$. So $d'$ succeeds on $X$, a contradiction.
:::
::::

::::exercise{#ex-cr-join difficulty=1 objective="Show that the halves of a computably random join are computably random, by a strategy that bets on even positions only."}
For sequences $A$ and $B$, let $A \oplus B$ be the sequence with $(A \oplus B)(2n) = A(n)$ and $(A \oplus B)(2n+1) = B(n)$.

1. Show that if $A \oplus B$ is computably random, then so are $A$ and $B$.
2. Show that $A \oplus A$ is not computably random, for any $A$.

:::solution
1. For a string $\sigma$, let $\sigma_{\mathrm{ev}} = \sigma(0) \sigma(2) \sigma(4) \cdots$, the string of its bits at even positions. Let $d$ be a computable martingale that succeeds on $A$, and $d'(\sigma) = d(\sigma_{\mathrm{ev}})$. If $|\sigma|$ is odd, $(\sigma i)_{\mathrm{ev}} = \sigma_{\mathrm{ev}}$, and $d'$ does not bet at $\sigma$; if $|\sigma|$ is even, $(\sigma i)_{\mathrm{ev}} = \sigma_{\mathrm{ev}}\, i$, and $d'(\sigma 0) + d'(\sigma 1) = 2 d(\sigma_{\mathrm{ev}})$. So $d'$ is a computable martingale, and $d'((A \oplus B) \uh 2n) = d(A \uh n)$ is unbounded. The case of $B$ uses the odd positions.
2. Let $d(\varepsilon) = 1$; at a string $\sigma$ of odd length $2k + 1$, bet the whole capital on the bit $\sigma(2k)$: $d(\sigma b) = 2 d(\sigma)$ if $b = \sigma(2k)$ and $0$ otherwise; at strings of even length, do not bet. Along $A \oplus A$, the bit at position $2k + 1$ equals the bit at position $2k$, so $d((A \oplus A) \uh 2n) = 2^n$.

Part (1) is the easy half of van Lambalgen's theorem for computable randomness (Downey–Hirschfeldt 2010, Theorem 7.1.13).
:::
::::

::::exercise{#ex-cr-no-enumeration difficulty=2 objective="Show that the computable martingales cannot be listed effectively, by combining a listing into one strategy and following its non-ascending path."}
Let $(d_e)$ be a sequence of martingales with rational values such that $(e, \sigma) \mapsto d_e(\sigma)$ is computable. Show that some computable martingale is different from every $d_e$.

:::solution
Let $c_e = d_e(\varepsilon) + 1$, a positive rational computed from $e$, and $D = \sum_e 2^{-e} d_e / c_e$. Its initial capital is at most $\sum_e 2^{-e} = 2$, so $D$ is a martingale by :ref{#lem-martingale-basic} (2). It is computable: by :ref{#lem-martingale-basic} (1), $d_e(\sigma)/c_e \leq 2^{|\sigma|} d_e(\varepsilon)/c_e < 2^{|\sigma|}$, so the terms with $e \geq N$ add up to less than $2^{|\sigma| + 1 - N}$ at $\sigma$, and the finite sum of the terms with $e < N$ is a rational computed from $\sigma$ and $N$. By :ref{#prop-cr-basic} (2), there is a computable sequence $X$ on which $D$ does not succeed. Since $d_e \leq 2^e c_e D$, no $d_e$ succeeds on $X$. The martingale $E_X$ of :ref{#prop-cr-basic} (3) is computable and succeeds on $X$, so it is different from every $d_e$.

Adapted from Downey–Hirschfeldt 2010, Proposition 7.1.12, and Nies 2009, Exercise 7.3.11.
:::
::::

::::exercise[Convergence of martingales]{#ex-doob-convergence difficulty=2 objective="Adapt the switching argument to arbitrary martingales and prove that a martingale converges along almost every sequence."}
Let $d$ be a martingale. Show that the class of the sequences $X$ such that $d(X \uh n)$ has no limit in $[0, \infty]$ is null. Deduce that $d(X \uh n)$ converges to a finite limit for almost every $X$.

:::solution
If $d(X \uh n)$ has no limit in $[0, \infty]$, then $\liminf_n d(X \uh n) < \limsup_n d(X \uh n)$, and there are rationals $r < s$ with $\liminf_n d(X \uh n) < r < s < \limsup_n d(X \uh n)$; then $r > 0$. Fix such rationals and define a martingale $\hat d$ with $\hat d(\varepsilon) = 1$ as in the proof of :ref{#thm-cr-limits}, with exact values. Scan the prefixes $\rho$ of a string in order of length: the mode is initially **waiting**; at a prefix $\rho$ in waiting mode with $d(\rho) < r$, the mode becomes **copying**, with the scaling factor $c = \hat d(\rho)/r$; at a prefix $\rho$ in copying mode with $d(\rho) > s$, the mode becomes waiting. At a string in waiting mode, $\hat d$ does not bet; at a string $\sigma'$ in copying mode, $\hat d(\sigma' i) = \hat d(\sigma') + c\,(d(\sigma' i) - d(\sigma'))$. The martingale equality holds in both modes.

During a copying period started at $\sigma_0$, $\hat d(\sigma') = \hat d(\sigma_0) + c\,(d(\sigma') - d(\sigma_0)) = c\,(r - d(\sigma_0)) + c\, d(\sigma') \geq c\, d(\sigma') \geq 0$, since $\hat d(\sigma_0) = c\, r$ and $d(\sigma_0) < r$. So $\hat d$ is non-negative, and a copying period that ends at $\sigma$ gives $\hat d(\sigma) \geq c\, d(\sigma) > c\, s = (s/r)\, \hat d(\sigma_0)$. Waiting periods leave the capital unchanged. Along $X$, $d$ falls below $r$ and rises above $s$ infinitely often, so infinitely many copying periods are completed, and the capital at the end of the $k$-th one is at least $(s/r)^k$. So $\hat d$ succeeds on $X$.

The class in question is therefore contained in the union, over the countably many pairs of rationals $r < s$, of the success sets of the corresponding martingales $\hat d$, each null by :ref{#prop-success-null}. Finally, the sequences along which $d(X \uh n)$ tends to $\infty$ are in $S[d]$, which is null. So the capital has a finite limit along almost every sequence.

This is Doob's martingale convergence theorem in the setting of this course; the switching argument is his upcrossing argument. The proof of :ref{#thm-cr-limits} is its effective version.
:::
::::
:::::
