---
title: The Levin–Schnorr theorem
summary: A sequence is Martin-Löf random if and only if its initial segments are incompressible for prefix-free complexity; Chaitin's Ω is random; the ample excess lemma and Chaitin's characterization of randomness by the growth of K(X↾n) − n.
duration: 45
prerequisites: [solovay-tests]
---

The course on Kolmogorov complexity proposed to call a sequence random when its initial segments are incompressible, and showed that plain complexity cannot be used for this purpose (:ref{#cor-no-c-random}). With prefix-free complexity, the proposal succeeds, and gives exactly the Martin-Löf random sequences. This theorem of Levin and Schnorr connects the measure-theoretic definition of the previous lesson with the definition by incompressibility. It shows at once that $\Omega$ is random, and leads to finer information on the complexity of random sequences.

Throughout, $K$ is the prefix-free complexity defined by an optimal prefix-free machine $U$, and $\leq^+$ denotes inequality up to an additive constant.

## Randomness and incompressibility

The two definitions meet through two facts about $K$, proved in the course on Kolmogorov complexity. First, the strings that are compressible by $c$ bits are rare, in a sense measured by the Kraft inequality, and they can be enumerated: so the sequences with a compressible prefix form a $\Sigma^0_1$ class of small measure. Second, the KC theorem allows one to build a prefix-free machine by listing the lengths of the descriptions one wants, provided that the total weight is at most $1$: the strings generating the components of a test are few, measured by the weight $2^{-|\sigma|}$, so they can be given shorter descriptions. :ref{#fig-excess} shows the dichotomy.

:::figure[A schematic picture of :ref{#thm-levin-schnorr} and :ref{#cor-k-excess}: the function $n \mapsto K(Z \uh n) - n$ for a random sequence (solid) is bounded from below, and in fact tends to infinity; for a non-random sequence (dashed), it falls below $-c$ for every $c$. The curves are drawn by hand and do not come from actual values of $K$, which is not computable.]{#fig-excess}
<svg class="fig" viewBox="0 0 600 280" width="600" role="img" aria-label="Schematic plot of K of the first n bits minus n against n: for a random sequence the curve stays above minus c and tends to infinity; for a non-random sequence it falls below every horizontal line"><line x1="60" y1="150" x2="580" y2="150" class="axis"/><line x1="60" y1="16" x2="60" y2="268" class="axis"/><text x="584.0" y="155.0" text-anchor="start" class="math" font-size="14">n</text><text x="52.0" y="155.0" text-anchor="end" class="mrm" font-size="12">0</text><line x1="60" y1="183.0" x2="570" y2="183.0" class="muted-stroke" stroke-dasharray="4 4"/><text x="52.0" y="188.0" text-anchor="end" class="math" font-size="13">−c</text><polyline points="60.0,170.9 62.5,155.7 65.1,144.1 67.7,135.1 70.2,128.4 72.8,124.0 75.3,121.6 77.8,121.1 80.4,122.1 83.0,124.1 85.5,126.7 88.0,129.2 90.6,131.3 93.2,132.5 95.7,132.4 98.2,131.0 100.8,128.2 103.3,124.1 105.9,119.0 108.5,113.4 111.0,107.6 113.5,102.2 116.1,97.5 118.7,94.0 121.2,91.8 123.8,91.1 126.3,91.9 128.8,93.9 131.4,96.8 133.9,100.3 136.5,103.9 139.1,107.2 141.6,109.6 144.2,111.0 146.7,111.0 149.2,109.7 151.8,107.1 154.3,103.4 156.9,98.9 159.4,94.0 162.0,89.2 164.6,84.9 167.1,81.5 169.7,79.3 172.2,78.3 174.8,78.7 177.3,80.3 179.8,83.0 182.4,86.3 184.9,89.9 187.5,93.4 190.1,96.3 192.6,98.3 195.2,99.1 197.7,98.7 200.2,97.0 202.8,94.2 205.3,90.5 207.9,86.3 210.4,81.9 213.0,77.8 215.6,74.3 218.1,71.8 220.7,70.5 223.2,70.4 225.8,71.5 228.3,73.7 230.8,76.6 233.4,80.0 235.9,83.4 238.5,86.5 241.1,88.8 243.6,90.2 246.2,90.5 248.7,89.6 251.2,87.5 253.8,84.5 256.4,80.9 258.9,76.9 261.4,73.0 264.0,69.5 266.6,66.8 269.1,65.1 271.6,64.5 274.2,65.1 276.8,66.7 279.3,69.2 281.9,72.2 284.4,75.5 286.9,78.6 289.5,81.2 292.1,83.0 294.6,83.8 297.1,83.5 299.7,82.1 302.2,79.8 304.8,76.7 307.4,73.2 309.9,69.5 312.4,66.1 315.0,63.2 317.6,61.2 320.1,60.2 322.6,60.3 325.2,61.4 327.8,63.3 330.3,66.0 332.9,69.0 335.4,72.0 337.9,74.7 340.5,76.8 343.1,78.0 345.6,78.3 348.1,77.5 350.7,75.7 353.2,73.2 355.8,70.1 358.4,66.7 360.9,63.4 363.4,60.5 366.0,58.3 368.6,56.9 371.1,56.5 373.6,57.1 376.2,58.6 378.8,60.8 381.3,63.5 383.9,66.3 386.4,69.0 388.9,71.3 391.5,72.8 394.1,73.5 396.6,73.3 399.1,72.1 401.7,70.1 404.2,67.4 406.8,64.4 409.4,61.3 411.9,58.4 414.4,56.0 417.0,54.4 419.6,53.6 422.1,53.7 424.6,54.7 427.2,56.4 429.8,58.8 432.3,61.4 434.9,64.0 437.4,66.3 439.9,68.1 442.5,69.2 445.1,69.4 447.6,68.7 450.1,67.2 452.7,65.0 455.2,62.3 457.8,59.5 460.4,56.7 462.9,54.2 465.4,52.3 468.0,51.2 470.6,50.9 473.1,51.5 475.6,52.8 478.2,54.7 480.8,57.1 483.3,59.5 485.9,61.9 488.4,63.8 490.9,65.1 493.5,65.7 496.1,65.5 498.6,64.5 501.1,62.7 503.7,60.4 506.2,57.8 508.8,55.2 511.4,52.7 513.9,50.7 516.5,49.3 519.0,48.7 521.5,48.8 524.1,49.7 526.6,51.3 529.2,53.3 531.8,55.6 534.3,57.8 536.9,59.8 539.4,61.4 542.0,62.3 544.5,62.4 547.0,61.8 549.6,60.5 552.1,58.6 554.7,56.3 557.2,53.8 559.8,51.4 562.4,49.4 564.9,47.8 567.5,46.8 570.0,46.6" class="accent-stroke" stroke-width="2"/><polyline points="60.0,165.4 62.5,158.3 65.1,153.3 67.7,149.4 70.2,146.2 72.8,143.5 75.3,141.2 77.8,139.1 80.4,137.3 83.0,135.6 85.5,134.1 88.0,132.7 90.6,131.4 93.2,130.2 95.7,129.1 98.2,128.0 100.8,127.0 103.3,126.1 105.9,125.2 108.5,124.4 111.0,123.5 113.5,122.8 116.1,122.0 118.7,121.3 121.2,120.7 123.8,120.1 126.3,119.7 128.8,119.5 131.4,119.7 133.9,120.6 136.5,122.4 139.1,125.7 141.6,130.7 144.2,137.8 146.7,147.0 149.2,158.0 151.8,169.9 154.3,181.5 156.9,191.2 159.4,197.5 162.0,199.5 164.6,196.7 167.1,189.5 169.7,179.0 172.2,166.6 174.8,153.9 177.3,142.0 179.8,131.9 182.4,124.0 184.9,118.1 187.5,113.9 190.1,111.2 192.6,109.5 195.2,108.3 197.7,107.6 200.2,107.1 202.8,106.7 205.3,106.3 207.9,106.0 210.4,105.7 213.0,105.5 215.6,105.2 218.1,104.9 220.7,104.6 223.2,104.4 225.8,104.1 228.3,103.8 230.8,103.6 233.4,103.3 235.9,103.1 238.5,102.8 241.1,102.6 243.6,102.4 246.2,102.1 248.7,101.9 251.2,101.7 253.8,101.5 256.4,101.2 258.9,101.0 261.4,100.9 264.0,100.8 266.6,100.9 269.1,101.3 271.6,102.3 274.2,104.2 276.8,107.6 279.3,113.0 281.9,121.0 284.4,132.1 286.9,146.3 289.5,163.2 292.1,181.3 294.6,198.9 297.1,213.8 299.7,223.6 302.2,227.0 304.8,223.3 307.4,213.0 309.9,197.9 312.4,179.9 315.0,161.4 317.6,144.2 320.1,129.6 322.6,118.1 325.2,109.7 327.8,104.0 330.3,100.3 332.9,98.0 335.4,96.6 337.9,95.8 340.5,95.4 343.1,95.1 345.6,94.9 348.1,94.7 350.7,94.5 353.2,94.4 355.8,94.2 358.4,94.1 360.9,93.9 363.4,93.8 366.0,93.6 368.6,93.5 371.1,93.4 373.6,93.2 376.2,93.1 378.8,92.9 381.3,92.8 383.9,92.7 386.4,92.5 388.9,92.4 391.5,92.3 394.1,92.1 396.6,92.0 399.1,91.9 401.7,91.7 404.2,91.6 406.8,91.5 409.4,91.4 411.9,91.2 414.4,91.1 417.0,91.0 419.6,90.9 422.1,90.7 424.6,90.6 427.2,90.5 429.8,90.4 432.3,90.3 434.9,90.2 437.4,90.1 439.9,90.1 442.5,90.1 445.1,90.4 447.6,91.1 450.1,92.5 452.7,95.1 455.2,99.6 457.8,106.7 460.4,117.1 462.9,131.6 465.4,150.0 468.0,171.8 470.6,195.2 473.1,218.0 475.6,237.2 478.2,250.0 480.8,254.5 483.3,249.8 485.9,236.8 488.4,217.4 490.9,194.4 493.5,170.7 496.1,148.7 498.6,130.1 501.1,115.5 503.7,104.8 506.2,97.5 508.8,92.8 511.4,90.0 513.9,88.4 516.5,87.5 519.0,87.0 521.5,86.7 524.1,86.5 526.6,86.4 529.2,86.3 531.8,86.2 534.3,86.1 536.9,86.0 539.4,85.9 542.0,85.8 544.5,85.7 547.0,85.6 549.6,85.5 552.1,85.5 554.7,85.4 557.2,85.3 559.8,85.2 562.4,85.1 564.9,85.0 567.5,84.9 570.0,84.8" class="ink-stroke" stroke-width="1.4" stroke-dasharray="5 3"/><text x="570.0" y="34.6" class="label" text-anchor="end">random: bounded below, tends to +∞</text><text x="391.5" y="249.0" class="label" text-anchor="end">not random: below −c for every c</text><text x="66" y="26" class="label">K(Z↾n) − n (schematic)</text></svg>
:::

:::theorem[Levin, Schnorr]{#thm-levin-schnorr}
A sequence $Z$ is Martin-Löf random if and only if there is a constant $c$ with $K(Z \uh n) \geq n - c$ for every $n$.
:::

:::proof{of=thm-levin-schnorr}
($\Rightarrow$) Suppose that for every $c$ there is $n$ with $K(Z \uh n) < n - c$. For each $c$, let $\mathcal V_c$ be the open class generated by the set of strings $\sigma$ with $K(\sigma) < |\sigma| - c$. This set is c.e., uniformly in $c$, since $K$ is approximable from above: $K(\sigma) < k$ if and only if $U(\tau)\converge = \sigma$ for some $\tau$ of length less than $k$. Let $W$ be the set of the minimal elements of this set, those with no proper prefix in it; it is prefix-free and generates $\mathcal V_c$. Then
$$
\lambda(\mathcal V_c) = \sum_{\sigma \in W} 2^{-|\sigma|} < \sum_{\sigma \in W} 2^{-K(\sigma) - c} \leq 2^{-c},
$$
by :ref{#prop-k-basic} (4), if $W$ is non-empty; otherwise $\lambda(\mathcal V_c) = 0$. So $(\mathcal V_c)$ is a Martin-Löf test, and $Z$ belongs to every $\mathcal V_c$ by hypothesis, so it is not random.

($\Leftarrow$) Suppose that $Z$ is captured by a Martin-Löf test $(\mathcal U_n)$. By :ref{#lem-prefix-free-generator}, there are c.e. prefix-free sets $W_n$, uniformly in $n$, with $\mathcal U_n = [W_n]^{\prec}$. Every $\sigma \in W_n$ satisfies $2^{-|\sigma|} \leq \lambda(\mathcal U_n) \leq 2^{-n}$, so $|\sigma| \geq n$. Enumerate the requests $(\sigma, |\sigma| - c)$ for $c \geq 1$ and $\sigma \in W_{2c}$; their lengths are at least $c$. Their weight is
$$
\sum_{c \geq 1} \sum_{\sigma \in W_{2c}} 2^{-|\sigma| + c} = \sum_{c \geq 1} 2^c \lambda(\mathcal U_{2c}) \leq \sum_{c \geq 1} 2^{-c} = 1.
$$
By the KC theorem (:ref{#thm-kc}), there is a constant $d$ with $K(\sigma) \leq |\sigma| - c + d$ for every $c \geq 1$ and $\sigma \in W_{2c}$. Since $Z \in \mathcal U_{2c}$, some prefix $Z \uh n$ belongs to $W_{2c}$, and $K(Z \uh n) \leq n - c + d$. As $c$ is arbitrary, no constant bounds $n - K(Z \uh n)$.
:::

The two directions use the two faces of $K$. Incompressibility fails on an effectively open class of small measure, because $K$ satisfies the Kraft inequality and is approximable from above. Conversely, the KC theorem turns a test into a machine that compresses the strings generating its components, the gain $c$ being paid for by the measure $2^{-2c}$ of the component used.

:::corollary{#cor-explicit-universal}
The classes $\mathcal V_c = [\{ \sigma : K(\sigma) < |\sigma| - c \}]^{\prec}$ form a universal Martin-Löf test.
:::

:::proof{of=cor-explicit-universal}
The first part of the proof shows that $(\mathcal V_c)$ is a Martin-Löf test. The second shows that if $Z$ is captured by some test, then for every $c$ there is $n$ with $K(Z \uh n) < n - c$, that is, $Z \in \mathcal V_c$.
:::

:::quiz[the Levin–Schnorr theorem]
In the direction ($\Rightarrow$) of the proof of :ref{#thm-levin-schnorr}, why is the generator $W$ taken prefix-free?

- [x] So that the measure of $\mathcal V_c$ is the sum of $2^{-|\sigma|}$ over $W$, which is then bounded by the Kraft inequality for $K$.
- [ ] So that $W$ is c.e.

  The set of minimal elements need not be c.e.; this is harmless, since $W$ only serves to compute a measure.
- [ ] So that the strings of $W$ have distinct complexities.

  Distinct strings may have the same complexity; the Kraft inequality sums over distinct strings, which is all that is needed.

---

In the direction ($\Leftarrow$), why is the component $\mathcal U_{2c}$ used to obtain a compression by $c$ bits, rather than $\mathcal U_c$?

- [x] Because compressing the strings of $W_c$ by $c$ bits would cost a weight $2^c \lambda(\mathcal U_c) \leq 1$ for each $c$, and the total weight could be infinite; with $\mathcal U_{2c}$, the cost is at most $2^{-c}$.
- [ ] Because $\mathcal U_c$ might not contain $Z$.

  $Z$ belongs to every component of the test.
- [ ] Because the strings of $W_c$ might have length less than $c$.

  They have length at least $c$; the issue is the total weight of the requests.
:::

## The halting probability is random

:::corollary[Chaitin]{#cor-omega-random}
The binary expansion of $\Omega$ is Martin-Löf random. In particular there is a random sequence Turing equivalent to $\emptyset'$, and a random left-c.e. real.
:::

:::proof{of=cor-omega-random}
By :ref{#thm-omega}, $K(\omega \uh n) \geq n - c$ for every $n$, and $\omega \equiv_T \emptyset'$. Apply :ref{#thm-levin-schnorr}.
:::

Random sequences can therefore be computationally powerful, unlike the low random sequences of :ref{#cor-mlr-structure}. Conversely, a left-c.e. real of $(0, 1)$ is random if and only if it is the halting probability of some optimal prefix-free machine. One direction is the argument of :ref{#thm-omega}, which applies to every optimal machine. The other combines two theorems on a notion of completeness for left-c.e. reals due to Solovay, not treated here: Calude, Hertling, Khoussainov and Wang (1998) proved that every Solovay complete left-c.e. real is a halting probability, and Kučera and Slaman (2001) that every random left-c.e. real is Solovay complete (Downey–Hirschfeldt, Theorems 9.2.2 and 9.2.3). This is admitted here.

## The ample excess lemma

The Levin–Schnorr theorem gives a lower bound $n - c$ on the complexity of the prefixes of a random sequence. The excess $K(Z \uh n) - n$ is in fact large for most $n$.

:::theorem[Ample excess lemma; Miller, Yu]{#thm-ample-excess}
A sequence $Z$ is Martin-Löf random if and only if $\sum_n 2^{n - K(Z \uh n)} < \infty$.
:::

:::proof{of=thm-ample-excess}
($\Leftarrow$) If the sum is at most $2^c$, each term is, so $K(Z \uh n) \geq n - c$ for every $n$, and $Z$ is random by :ref{#thm-levin-schnorr}.

($\Rightarrow$) For a string $\tau$ of length $N$, let $F(\tau) = \sum_{n \leq N} 2^{n - K(\tau \uh n)}$. For each $k$, let $D_N$ be the set of strings $\tau$ of length $N$ with $F(\tau) > 2^k$, and $\mathcal V_k = \bigcup_N [D_N]^{\prec}$. Since $K$ is approximable from above, $F(\tau)$ is the limit of a computable non-decreasing sequence of rationals, so $F(\tau) > 2^k$ is a $\Sigma^0_1$ property of $\tau$ and $k$, and $(\mathcal V_k)$ is uniformly $\Sigma^0_1$.

A string extending an element of $D_N$ has a larger value of $F$, so $[D_N]^{\prec} \subseteq [D_{N+1}]^{\prec}$. We bound the size of $D_N$ by summing $F$ over all strings of length $N$. Each string $\rho$ of length $n \leq N$ is the prefix of $2^{N - n}$ strings of length $N$, so
$$
2^k |D_N| < \sum_{|\tau| = N} F(\tau) = \sum_{n \leq N} \sum_{|\rho| = n} 2^{N-n}\, 2^{n - K(\rho)} = 2^N \sum_{|\rho| \leq N} 2^{-K(\rho)} \leq 2^N,
$$
when $D_N$ is non-empty, by :ref{#prop-k-basic} (4). Hence $\lambda([D_N]^{\prec}) \leq 2^{-k}$ for every $N$, and $\lambda(\mathcal V_k) \leq 2^{-k}$ by continuity. So $(\mathcal V_k)$ is a Martin-Löf test. If the sum diverges for $Z$, then $F(Z \uh N) > 2^k$ for some $N$, for every $k$, and $Z$ is captured.
:::

The proof is an averaging argument: the average of $\sum_n 2^{n - K(X \uh n)}$ over all sequences $X$ is $\sum_\rho 2^{-K(\rho)} \leq 1$, and the test collects the sequences on which the sum is large.

:::corollary[Chaitin]{#cor-k-excess}
A sequence $Z$ is Martin-Löf random if and only if $\lim_n (K(Z \uh n) - n) = +\infty$.
:::

:::proof{of=cor-k-excess}
If $Z$ is random, the terms $2^{n - K(Z \uh n)}$ of a convergent series tend to $0$, so $K(Z \uh n) - n$ tends to $+\infty$. Conversely, if the limit is infinite, $K(Z \uh n) - n$ is bounded from below, and $Z$ is random by :ref{#thm-levin-schnorr}.
:::

The lemma says more than the corollary. Let $A$ be the set of $n \geq 1$ with $K(Z \uh n) < n + \log n$. Each $n \in A$ contributes more than $1/n$ to the convergent series, so $\sum_{n \in A} 1/n < \infty$: for a random sequence, the excess falls below $\log n$ only on a sparse set of lengths.

:::quiz[the ample excess lemma]
In the proof of :ref{#thm-ample-excess}, why do the classes $[D_N]^{\prec}$ increase with $N$?

- [x] Because $F$ is a sum of non-negative terms over the prefixes, so a string extending $\tau$ has a value of $F$ at least $F(\tau)$; the extensions of length $N+1$ of an element of $D_N$ are in $D_{N+1}$.
- [ ] Because $K$ is non-decreasing along prefixes.

  $K$ is not monotone: a longer string may have a smaller complexity.
- [ ] Because $D_N$ is c.e.

  Being c.e. does not give monotonicity in $N$.

---

Where is the Kraft inequality for $K$ used?

- [x] In the bound $\sum_{|\rho| \leq N} 2^{-K(\rho)} \leq 1$, which controls the average of $F$ over the strings of length $N$.
- [ ] To show that $F(\tau) > 2^k$ is a $\Sigma^0_1$ property.

  This uses the approximation of $K$ from above, not the Kraft inequality.
- [ ] To show that the series converges for every sequence.

  The series diverges for non-random sequences, by the direction ($\Leftarrow$).
:::

## Exercises

::::exercise{difficulty=1}
Let $Z$ be Martin-Löf random and $f$ a strictly increasing computable function. Show that the sequence $Y = Z(f(0))\, Z(f(1))\, Z(f(2)) \cdots$ is random.

:::solution
For a string $\sigma$, the class of $X$ with $X(f(i)) = \sigma(i)$ for $i < |\sigma|$ is a clopen class $[\sigma]_f$ of measure $2^{-|\sigma|}$, computable from $\sigma$. If $Y$ is captured by $(\mathcal U_n)$, write $\mathcal U_n = [W_n]^{\prec}$ with $W_n$ c.e. prefix-free (:ref{#lem-prefix-free-generator}), and let $\mathcal V_n = \bigcup_{\sigma \in W_n} [\sigma]_f$. The classes $[\sigma]_f$, $\sigma \in W_n$, are pairwise disjoint since the strings are incomparable, so $\lambda(\mathcal V_n) = \lambda(\mathcal U_n) \leq 2^{-n}$. The sequence $(\mathcal V_n)$ is uniformly $\Sigma^0_1$, and it captures $Z$.
:::
::::

::::exercise{difficulty=2}
Let $Z$ be Martin-Löf random. Show that for almost every $n$, the bits $Z(n), \dots, Z(n + K(n) - 1)$ are not all $0$.

:::hint
Use a Solovay test whose $n$-th component has measure $2^{-K(n)}$.
:::

:::solution
Let $\mathcal S_n$ be the class of sequences $X$ with $X(n + i) = 0$ for every $i < K(n)$. It is the union over $s$ of the clopen classes defined with $K_s(n)$ instead of $K(n)$, where $K_s$ approximates $K$ from above; these increase with $s$, so $(\mathcal S_n)$ is uniformly $\Sigma^0_1$. Its measure is $2^{-K(n)}$, so $\sum_n \lambda(\mathcal S_n) \leq 1$ by the Kraft inequality. By :ref{#thm-solovay}, $Z$ belongs to only finitely many $\mathcal S_n$.
:::
::::

::::exercise{difficulty=2}
Identify a sequence $X$ with the real $0.X = \sum_i X(i) 2^{-i-1}$. Let $Z$ be random, and suppose that there is a computable sequence of rationals $(r_t)$ converging to $\alpha = 0.Z$ with $\sum_t |r_{t+1} - r_t| < \infty$. Show that $\alpha$ is left-c.e. or right-c.e.

:::solution
For rationals $a < b$, the class of $X$ with $a < 0.X < b$ is a $\Sigma^0_1$ class of measure at most $b - a$, uniformly in $a$ and $b$: it is generated by the strings $\sigma$ whose dyadic interval $[0.\sigma, 0.\sigma + 2^{-|\sigma|}]$ is contained in $(a, b)$. Let $\mathcal S_t$ be this class for the open interval with endpoints $r_t$ and $r_{t+1}$ (empty if they are equal). This is a Solovay test, so there is $t_0$ such that $\alpha$ lies strictly between $r_t$ and $r_{t+1}$ for no $t \geq t_0$. The real $\alpha$ is not rational: a sequence $X$ with $0.X$ rational is eventually periodic, hence computable, hence not random. So $\alpha \neq r_t$ for every $t$, and for $t \geq t_0$, $r_t$ and $r_{t+1}$ lie on the same side of $\alpha$. All $r_t$, $t \geq t_0$, are then on the same side. If they are below $\alpha$, the computable non-decreasing sequence $\max_{t_0 \leq u \leq t} r_u$ converges to $\alpha$, which is left-c.e.; if they are above, $\alpha$ is right-c.e. by the symmetric argument.
:::
::::

## Notes and references

The characterization of randomness by incompressibility was found independently by Levin (1973), with monotone complexity, and Schnorr (1973), with process complexity. The form with prefix-free complexity is credited to Schnorr and was published by Chaitin (1975), who defined randomness by the condition $K(Z \uh n) \geq n - c$ (Downey–Hirschfeldt, Definition 6.1.1 and Theorem 6.2.3; Nies, Theorem 3.2.9). :ref{#cor-k-excess} is due to Chaitin (1987); the ample excess lemma is due to Miller and Yu (2008) (Downey–Hirschfeldt, Theorem 6.6.1 and Corollary 6.6.2; Nies, Proposition 3.2.21 for the corollary). The randomness of $\Omega$ is Downey–Hirschfeldt, Theorem 6.1.3, and Nies, Theorem 3.2.11. The last exercise is due to Rettinger (unpublished; Downey–Hirschfeldt, Theorem 9.2.4; Nies, Proposition 3.2.32), and the second one is a variant of Nies, Proposition 3.2.20.

A third characterization of Martin-Löf randomness, by betting strategies, is due to Schnorr (1971): a sequence is random if and only if no c.e. martingale wins an unbounded capital on it (Downey–Hirschfeldt, Theorem 6.3.4). It is the subject of a forthcoming course of the track, on martingales.

- L. A. Levin, *On the notion of a random sequence*, Soviet Mathematics Doklady 14 (1973), 1413–1416.
- C.-P. Schnorr, *Process complexity and effective random tests*, Journal of Computer and System Sciences 7 (1973), 376–388.
- C.-P. Schnorr, *A unified approach to the definition of random sequences*, Mathematical Systems Theory 5 (1971), 246–258.
- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- G. J. Chaitin, *Incompleteness theorems for random reals*, Advances in Applied Mathematics 8 (1987), 119–146.
- J. S. Miller and L. Yu, *On initial segment complexity and degrees of randomness*, Transactions of the American Mathematical Society 360 (2008), 3193–3210.
- C. S. Calude, P. H. Hertling, B. Khoussainov and Y. Wang, *Recursively enumerable reals and Chaitin Ω numbers*, in: STACS 98, Lecture Notes in Computer Science 1373, Springer, 1998, 596–606.
- A. Kučera and T. A. Slaman, *Randomness and recursive enumerability*, SIAM Journal on Computing 31 (2001), 199–211.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 6.1–6.3, 6.6 and 9.2.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 3.2.
