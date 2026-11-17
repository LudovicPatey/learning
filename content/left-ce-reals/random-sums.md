---
title: Sums of left-c.e. reals
summary: If a sum of two left-c.e. reals is Martin-Löf random, one of the two is random (Demuth; Downey, Hirschfeldt, Nies); the proof transfers a Solovay test along the stages at which one approximation dominates the other.
duration: 35
prerequisites: [kucera-slaman]
---

By the theorem of Kučera and Slaman, adding a left-c.e. real to a random left-c.e. real gives a random real. This lesson proves a converse: a random left-c.e. real cannot be split into two non-random left-c.e. reals. If $\alpha_0 + \alpha_1$ is random, then $\alpha_0$ or $\alpha_1$ is random. The statement fails for reals that are not left-c.e.: the bits of $\Omega$ at even positions and at odd positions give two non-random reals with sum $\Omega$ (:ref{#ex-interleaved-omega}). It is a structural property of the top Solovay degree: by a theorem of Downey, Hirschfeldt and Nies, every other degree of left-c.e. reals splits into two smaller degrees.

The result follows from a theorem of Downey, Hirschfeldt and Nies, with a remarkable hypothesis: if $\beta$ is random and the approximation of $\alpha$ is behind that of $\beta$, up to a factor, at **infinitely many** stages, then $\alpha$ is random. Solovay reducibility $\beta \leq_S \alpha$ asks for this at all stages; infinitely many suffice. The proof turns a Solovay test that covers $\alpha$ into a Solovay test that covers $\beta$. The difficulty is that the good stages are not computable, and the construction must guess them without paying too much for wrong guesses.

Throughout, $\alpha$ and $\beta$ are left-c.e. reals with strictly increasing approximations $(\alpha_s)$ and $(\beta_s)$.

## Solovay tests made of intervals

A **Solovay test of intervals** is a computable sequence $(I_i)$ of open intervals with rational endpoints with $\sum_i |I_i| < \infty$. An irrational real that belongs to infinitely many of the $I_i$ is not random: the corresponding classes of sequences form a Solovay test in the sense of :ref{#def-solovay-test}, and :ref{#thm-solovay} applies. Conversely:

:::lemma{#lem-interval-test}
If an irrational real $\alpha \in (0, 1)$ is not random, there is a Solovay test of intervals $(I_i)$ such that $\alpha \in I_i$ for infinitely many $i$.
:::

:::proof{of=lem-interval-test}
Let $(\mathcal U_n)$ be a Martin-Löf test with $\alpha \in \bigcap_n \mathcal U_n$, and let $W_n$ be c.e. prefix-free sets, uniformly, with $\mathcal U_n = [W_n]^{\prec}$ (:ref{#lem-prefix-free-generator}). List, for all $n$ and all $\sigma \in W_n$, the open intervals $(0.\sigma, 0.\sigma + 2^{-|\sigma|})$. Their total length is $\sum_n \lambda(\mathcal U_n) \leq \sum_n 2^{-n} = 2$. For each $n$, the binary expansion of $\alpha$ extends some $\sigma \in W_n$, so $0.\sigma \leq \alpha \leq 0.\sigma + 2^{-|\sigma|}$, with strict inequalities since $\alpha$ is irrational. So $\alpha$ is in at least one listed interval for each $n$, and in infinitely many terms of the list.
:::

## The theorem of Downey, Hirschfeldt and Nies

:::theorem[Downey, Hirschfeldt, Nies]{#thm-dhn-random}
Let $k > 0$ be a rational. If $\beta$ is random and $k(\alpha - \alpha_s) > \beta - \beta_s$ for infinitely many $s$, then $\alpha$ is random.
:::

Suppose that $\alpha$ is not random, covered infinitely often by a Solovay test of intervals $(I_i)$. If the set $G$ of the stages $s$ with $k(\alpha - \alpha_s) > \beta - \beta_s$ were computable, the test could be transferred: for each $i$, find $s \in G$ with $\alpha_s \in I_i$ and add to the new test the interval $[\beta_s, \beta_s + k|I_i|]$. If $\alpha \in I_i$, then $\beta - \beta_s < k(\alpha - \alpha_s) < k|I_i|$, so $\beta$ is covered, and the lengths have a finite sum. The set $G$ is not computable, but it can be replaced by the set $S$ of the stages $s$ at which the approximation of $k\alpha$ stays ahead of that of $\beta$ forever, $k(\alpha_t - \alpha_s) > \beta_t - \beta_s$ for all $t > s$. This set is co-c.e., and a wrong guess $s \notin S$ is detected at a stage $t$ after which no stage between $s$ and $t$ is in $S$ either. So the guesses can be made in increasing order, and their costs add up to at most $k|I_i|$.

The proof uses two lemmas. Let
$$
S = \{ s : k(\alpha_t - \alpha_s) > \beta_t - \beta_s \text{ for every } t > s \},
$$
$$
S[t] = \{ s < t : k(\alpha_u - \alpha_s) > \beta_u - \beta_s \text{ for every } u \text{ with } s < u \leq t \}.
$$
The sets $S[t]$ are uniformly computable, and $s \in S$ if and only if $s \in S[t]$ for every $t > s$.

:::lemma[Downey, Hirschfeldt, Nies]{#lem-dhn-s-infinite}
If $k(\alpha - \alpha_s) > \beta - \beta_s$ for infinitely many $s$ and $S$ is finite, then $\beta \leq_S \alpha$.
:::

:::proof{of=lem-dhn-s-infinite}
Let $r$ be larger than every element of $S$: for every $s > r$ there is $t > s$ with $k(\alpha_t - \alpha_s) \leq \beta_t - \beta_s$. Let $s_0 > r$ with $k(\alpha - \alpha_{s_0}) > \beta - \beta_{s_0}$, and let $s_{i+1}$ be the least $t > s_i$ with $k(\alpha_t - \alpha_{s_i}) \leq \beta_t - \beta_{s_i}$. The sequence $(s_i)$ is computable. By induction, $k(\alpha - \alpha_{s_i}) > \beta - \beta_{s_i}$ for every $i$: subtracting the inequality defining $s_{i+1}$,
$$
k(\alpha - \alpha_{s_{i+1}}) = k(\alpha - \alpha_{s_i}) - k(\alpha_{s_{i+1}} - \alpha_{s_i}) > (\beta - \beta_{s_i}) - (\beta_{s_{i+1}} - \beta_{s_i}) = \beta - \beta_{s_{i+1}}.
$$
Let $g(n)$ be the least $s_i \geq n$. Then $\beta - \beta_{g(n)} < k(\alpha - \alpha_{g(n)}) \leq k(\alpha - \alpha_n)$, and $\beta \leq_S \alpha$ by :ref{#prop-solovay-approximations}.
:::

:::lemma{#lem-dhn-leaving}
If $s \in S[t - 1]$ and $s \notin S[t]$, then no $u$ with $s < u < t$ belongs to $S[t]$; in particular, no such $u$ is in $S$.
:::

:::proof{of=lem-dhn-leaving}
Let $s < u < t$. Since $s \in S[t-1]$, $k(\alpha_u - \alpha_s) > \beta_u - \beta_s$. Since $s \notin S[t]$, $k(\alpha_t - \alpha_s) \leq \beta_t - \beta_s$. Subtracting, $k(\alpha_t - \alpha_u) < \beta_t - \beta_u$, so $u \notin S[t]$.
:::

:::proof{of=thm-dhn-random}
Suppose that $\beta$ is random and $\alpha$ is not. Then $\beta \not\leq_S \alpha$: otherwise $\alpha$ would be random by :ref{#cor-above-random}. By :ref{#lem-dhn-s-infinite}, $S$ is infinite. Moreover $k(\alpha - \alpha_s) > \beta - \beta_s$ for every $s \in S$. Indeed, for $s \in S$, the inequalities $k(\alpha_t - \alpha_s) > \beta_t - \beta_s$ give $k(\alpha - \alpha_s) \geq \beta - \beta_s$ in the limit, and equality would make $\beta - k\alpha$ rational, so that $\beta \leq_S k\alpha \leq_S \alpha$ by :ref{#ex-solovay-examples}, which is excluded.

Let $(I_i)$ be a Solovay test of intervals with $\alpha \in I_i$ for infinitely many $i$, given by :ref{#lem-interval-test} if $\alpha$ is irrational; if $\alpha$ is rational, take $I_i = (\alpha - 2^{-i}, \alpha + 2^{-i})$, which contains $\alpha$ for every $i$.

For each $i$, run the following procedure $P_i$, all procedures in parallel.

1. Wait for a stage $s$ with $\alpha_s \in I_i$. Let $t = s + 1$.
2. If $\alpha_t \notin I_i$, stop.
3. If $s \notin S[t]$, let $s = t$, then $t = s + 1$, and go to step 2. Otherwise, add to the new test the open interval
$$
J = \big( \beta_s + k(\alpha_{t-1} - \alpha_s),\ \beta_s + k(\alpha_t - \alpha_s) \big),
$$
let $t = t + 1$, and go to step 2.

The intervals $J$ are listed in a computable sequence $(J_m)$.

*The new test has finite total length.* The variable $t$ increases by one at each pass, and each value of $t$ produces at most one interval, of length at most $k(\alpha_t - \alpha_{t-1})$. All the values of $t$ used by $P_i$ satisfy $\alpha_t \in I_i$, and so do the values $t - 1$, starting from the first $s$. So the total length of the intervals produced by $P_i$ is at most $k$ times the increase of the approximation of $\alpha$ inside $I_i$, which is at most $k|I_i|$. The total length of the new test is at most $k \sum_i |I_i| < \infty$.

*$\beta$ is covered infinitely often.* Fix $i$ with $\alpha \in I_i$. The approximation $(\alpha_s)$ is increasing with limit $\alpha$, so step 1 terminates, and from then on every $\alpha_t$ lies between $\alpha_s$ and $\alpha$, hence in the interval $I_i$: the procedure never stops. Let $s^*$ be an element of $S$ larger than the first value of $s$. The variable $s$ only increases, and it changes from $s$ to $t$ only when $s \in S[t-1] \setminus S[t]$; by :ref{#lem-dhn-leaving}, $t \leq s^*$ in that case, since $s^* \in S$ is not in $(s, t)$, and $s \neq s^*$ since $s^* \in S[t]$. So $s$ changes finitely many times, and its final value $s_f$ satisfies $s_f \in S[t]$ for every $t > s_f$, that is, $s_f \in S$. From the stage at which $s$ takes the value $s_f$, the procedure adds the intervals $J$ for $t = s_f + 1, s_f + 2, \dots$, whose closures cover $[\beta_{s_f}, \beta_{s_f} + k(\alpha - \alpha_{s_f}))$. This interval contains $\beta$, since $\beta - \beta_{s_f} < k(\alpha - \alpha_{s_f})$, and $\beta$ is not an endpoint of any $J$, since $\beta$ is irrational. So $\beta$ belongs to an interval produced by $P_i$.

Since $\alpha \in I_i$ for infinitely many $i$, $\beta$ belongs to infinitely many terms of $(J_m)$, which is a Solovay test of intervals. So $\beta$ is not random, a contradiction.
:::

:::figure[The procedure $P_i$ in the proof of :ref{#thm-dhn-random}. While the guess $s$ stays in $S[t]$, the movements of $k\alpha_t$ since $s$ are copied above $\beta_s$; a wrong guess is abandoned for the current stage $t$, and by :ref{#lem-dhn-leaving} no element of $S$ is skipped.]
<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="Two lines: the upper shows the approximations of alpha inside the interval I i at stages s, s plus one, and so on; the lower shows beta s and consecutive intervals J of lengths k times the increments of alpha, covering up to beta s plus k times alpha minus alpha s, which contains beta"><defs><marker id="dhn-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="20" y="40" class="label">α</text><line x1="40" y1="60" x2="570" y2="60" class="axis"/><rect x="90" y="50" width="420" height="20" class="soft-fill"/><text x="300" y="44" text-anchor="middle" class="label">I_i</text><circle cx="140" cy="60" r="3.5" class="ink-fill"/><circle cx="200" cy="60" r="3.5" class="ink-fill"/><circle cx="240" cy="60" r="3.5" class="ink-fill"/><circle cx="300" cy="60" r="3.5" class="ink-fill"/><circle cx="420" cy="60" r="4.5" class="accent-fill"/><text x="140" y="88" text-anchor="middle" class="math" font-size="13">α<tspan font-size="9" dy="3">s</tspan></text><text x="200" y="88" text-anchor="middle" class="math" font-size="13">α<tspan font-size="9" dy="3">s+1</tspan></text><text x="240" y="88" text-anchor="middle" class="math" font-size="13">α<tspan font-size="9" dy="3">s+2</tspan></text><text x="300" y="88" text-anchor="middle" class="math" font-size="13">α<tspan font-size="9" dy="3">s+3</tspan></text><text x="420" y="88" text-anchor="middle" class="math" font-size="13">α</text><text x="20" y="150" class="label">β</text><line x1="40" y1="170" x2="570" y2="170" class="axis"/><rect x="100" y="160" width="90" height="20" class="cell head-cell"/><rect x="190" y="160" width="60" height="20" class="cell head-cell"/><rect x="250" y="160" width="90" height="20" class="cell head-cell"/><circle cx="100" cy="170" r="3.5" class="ink-fill"/><text x="100" y="198" text-anchor="middle" class="math" font-size="13">β<tspan font-size="9" dy="3">s</tspan></text><circle cx="300" cy="170" r="4.5" class="accent-fill"/><text x="300" y="198" text-anchor="middle" class="math" font-size="13">β</text><text x="145" y="154" text-anchor="middle" class="label">k(α_s+1 − α_s)</text><text x="300" y="154" text-anchor="middle" class="label">…</text><line x1="140" y1="96" x2="104" y2="156" class="muted-stroke" stroke-dasharray="3 3"/><text x="470" y="198" text-anchor="middle" class="label">s ∈ S: β − β_s &lt; k(α − α_s)</text></svg>
:::

:::quiz[the theorem of Downey, Hirschfeldt and Nies]
In the proof of :ref{#thm-dhn-random}, why can the guess $s$ not jump over an element of $S$?

- [x] The guess changes from $s$ to $t$ only when $s$ leaves $S[t]$ at stage $t$, and then, by :ref{#lem-dhn-leaving}, no stage strictly between $s$ and $t$ is in $S$.
- [ ] Because $S$ is computable.

  $S$ is co-c.e., not computable in general; the proof only uses the approximations $S[t]$.
- [ ] Because the guesses are made in increasing order.

  Increasing order alone would allow skipping; the lemma is what prevents it.

---

Where is the hypothesis that $k(\alpha - \alpha_s) > \beta - \beta_s$ for infinitely many $s$ used?

- [x] In :ref{#lem-dhn-s-infinite}, to show that $S$ is infinite, given that $\beta \not\leq_S \alpha$.
- [ ] To show that the new test has finite total length.

  The bound $k \sum_i |I_i|$ holds whatever the set of good stages.
- [ ] To show that $\beta$ is irrational.

  $\beta$ is irrational because it is random.
:::

## Splitting random left-c.e. reals

:::corollary[Demuth; Downey, Hirschfeldt, Nies]{#cor-demuth-split}
If $\alpha_0$ and $\alpha_1$ are left-c.e. reals and $\alpha_0 + \alpha_1$ is random, then $\alpha_0$ or $\alpha_1$ is random.
:::

:::proof{of=cor-demuth-split}
Let $\beta = \alpha_0 + \alpha_1$, with the approximation $\beta_s = \alpha_{0, s} + \alpha_{1, s}$. For each $s$, $\beta - \beta_s = (\alpha_0 - \alpha_{0, s}) + (\alpha_1 - \alpha_{1, s})$, so one of the two terms is at least $(\beta - \beta_s)/2$, and $3(\alpha_j - \alpha_{j, s}) > \beta - \beta_s$ for some $j < 2$, the difference being positive. So for some $j < 2$, this holds for infinitely many $s$. By :ref{#thm-dhn-random} with $k = 3$, $\alpha_j$ is random.
:::

With the theorem of Kučera and Slaman, this gives a description of the random left-c.e. reals inside the structure of Solovay degrees. Downey, Hirschfeldt and Nies proved that every left-c.e. real $\gamma$ that is not random splits: $\gamma = \alpha_0 + \alpha_1$ with left-c.e. reals $\alpha_0, \alpha_1 <_S \gamma$ (admitted; Downey–Hirschfeldt, Theorem 9.5.3). By the corollary, a random left-c.e. real does not split in this way, since a random summand would be Ω-like, hence of the same degree as $\gamma$. So a left-c.e. real is random if and only if it is not the sum of two left-c.e. reals of smaller Solovay degree: randomness of left-c.e. reals is definable in the order of Solovay degrees.

::::exercise[Interleaving the bits of Ω]{#ex-interleaved-omega difficulty=1 objective="See that the splitting theorem fails without the hypothesis that the summands are left-c.e."}
Let $\omega_0 \omega_1 \omega_2 \cdots$ be the binary expansion of $\Omega$, and let $\alpha = 0.\omega_0 0 \omega_2 0 \omega_4 \cdots$ and $\beta = 0.0 \omega_1 0 \omega_3 0 \cdots$. Show that $\alpha + \beta = \Omega$ and that neither $\alpha$ nor $\beta$ is random. Deduce that $\alpha$ and $\beta$ are not both left-c.e.

:::solution
The binary expansions of $\alpha$ and $\beta$ have no $1$ at a common position, so $\alpha + \beta = \sum_i \omega_i 2^{-i-1} = \Omega$. The bits of $\alpha$ at odd positions are $0$: the classes $\{ X : X(2i+1) = 0 \text{ for } i < n \}$ are clopen, uniformly computable, of measure $2^{-n}$, and contain the expansion of $\alpha$, so $\alpha$ is not random; similarly for $\beta$ with the even positions. If both were left-c.e., one of them would be random by :ref{#cor-demuth-split}. (Downey–Hirschfeldt, after Theorem 9.5.11.)
:::
::::

## Notes and references

The splitting corollary is stated without proof by Demuth (1988), and was rediscovered with a proof by Downey, Hirschfeldt and Nies (2002), from whom the theorem and its proof come; we follow the presentation of Downey and Hirschfeldt (Lemmas 9.5.6 and 9.5.7, Theorem 9.5.8 and Corollary 9.5.9). Downey, Hirschfeldt and Nies state the theorem in a slightly more general form, with $\beta - \beta_{f(s)}$ for an increasing computable function $f$, which reduces to the form given here by replacing $(\beta_s)$ with the approximation $(\beta_{f(s)})$. They also proved that the Solovay degrees of left-c.e. reals are dense, and that every incomplete degree splits over every lesser degree.

- O. Demuth, *Remarks on the structure of tt-degrees based on constructive measure theory*, Commentationes Mathematicae Universitatis Carolinae 29 (1988), 233–247.
- R. G. Downey, D. R. Hirschfeldt and A. Nies, *Randomness, computability, and density*, SIAM Journal on Computing 31 (2002), 1169–1183.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 9.5.

:::::exercises
::::exercise{#ex-finite-sums-random difficulty=1 objective="Extend the splitting corollary to finite sums."}
Show that if $\alpha_0, \dots, \alpha_m$ are left-c.e. reals and $\alpha_0 + \cdots + \alpha_m$ is random, then some $\alpha_j$ is random.

:::solution
By induction on $m$, the case $m = 0$ being trivial. For $m \geq 1$, the reals $\alpha_0 + \cdots + \alpha_{m-1}$ and $\alpha_m$ are left-c.e., by :ref{#ex-left-ce-closure}, and their sum is random. By :ref{#cor-demuth-split}, $\alpha_m$ is random, or $\alpha_0 + \cdots + \alpha_{m-1}$ is random, and in the second case the induction hypothesis gives a random $\alpha_j$ with $j < m$. Alternatively, apply :ref{#thm-dhn-random} directly with $k = m + 2$.
:::
::::

::::exercise{#ex-dhn-all-stages difficulty=1 objective="Compare the hypothesis of the theorem with Solovay reducibility."}
Show that if $k(\alpha - \alpha_s) > \beta - \beta_s$ for every $s$ and $\beta$ is random, then $\alpha$ is random, without using :ref{#thm-dhn-random}.

:::solution
The inequality for every $s$ gives $\beta \leq_S \alpha$ by :ref{#prop-solovay-approximations}, with $g(n) = n$ and constant $k$. So $\alpha$ is random by :ref{#cor-above-random}.
:::
::::

::::exercise{#ex-dhn-sign difficulty=2 objective="Show that, unless the two reals are Solovay equivalent, the comparison of their approximations from a fixed stage stabilizes."}
Fix $s$. Show that if $\beta \not\equiv_S \alpha$, then either $\beta_t - \beta_s < k(\alpha_t - \alpha_s)$ for all large $t$, or $\beta_t - \beta_s > k(\alpha_t - \alpha_s)$ for all large $t$.

:::solution
Otherwise there are infinitely many $t$ with $\beta_t - \beta_s \leq k(\alpha_t - \alpha_s)$ and infinitely many with $\beta_t - \beta_s \geq k(\alpha_t - \alpha_s)$. Taking limits along each set of stages, $\beta - \beta_s \leq k(\alpha - \alpha_s)$ and $\beta - \beta_s \geq k(\alpha - \alpha_s)$. So $\beta = k\alpha + q$ with the rational $q = \beta_s - k\alpha_s$. Then $\beta \equiv_S \alpha$: with the approximations $(k\alpha_t + q)$ of $\beta$ and $(\alpha_t)$ of $\alpha$, the differences to the limits are proportional, and :ref{#prop-solovay-approximations} applies in both directions, with $g(n) = n$ and constants $k + 1$ and $k^{-1} + 1$. (Downey–Hirschfeldt, Lemma 9.5.7.)
:::
::::
:::::
