---
title: Schnorr randomness
summary: Schnorr randomness, defined by computable martingales that succeed at a computable rate, is equivalent to passing all Martin-Löf tests of computable measure and all total Solovay tests; it implies the law of large numbers and has no universal test.
duration: 45
prerequisites: [computable-randomness]
---

A computable martingale that succeeds on a sequence makes its capital unbounded, but nothing says when: the gambler knows that she will eventually be rich, not how long it will take. Schnorr considered that an effective rejection of randomness should come with an effective rate, and that the same criticism applies to Martin-Löf tests, whose measures are bounded by $2^{-n}$ but not known. This lesson defines Schnorr randomness by martingales succeeding at a computable rate, and proves that it coincides with randomness for tests of computable measure, and for summable tests of computable total measure.

## Success at a computable rate

:::definition[Schnorr]{#def-schnorr-random}
An **order** is a computable non-decreasing unbounded function $h : \nat \to \nat$. A martingale $d$ **$h$-succeeds** on $X$ if $d(X \uh n) \geq h(n)$ for infinitely many $n$. A sequence $X$ is **Schnorr random** if no computable martingale $h$-succeeds on $X$ for any order $h$.
:::

If $d$ $h$-succeeds on $X$, then $d$ succeeds on $X$, so every computably random sequence is Schnorr random. Some authors define $h$-success by $\limsup_n d(X \uh n)/h(n) = \infty$. The notion of Schnorr randomness is the same: this condition implies $d(X \uh n) \geq h(n)$ infinitely often, and conversely, if $d(X \uh n) \geq h(n)$ infinitely often, then $d(X \uh n)/h'(n) \geq \sqrt{h(n)}$ at these $n$ for the order $h'(n) = \lfloor \sqrt{h(n)} \rfloor$, whenever $h(n) \geq 1$.

:::example{#ex-schnorr-success}
1. The proportional strategy $p_\delta$, for a rational $\delta \in (0, \frac12]$, $h$-succeeds on every sequence whose prefixes have at least $(\frac12 + \delta) n$ ones for infinitely many lengths $n$, with $h(n) = \lfloor (1 + \frac54 \delta^2)^n \rfloor$. Indeed $p_\delta(X \uh n) \geq e^{5\delta^2 n/4} \geq (1 + \frac54 \delta^2)^n$ at these lengths, by :ref{#lem-proportional} and $e^x \geq 1 + x$. So Schnorr random sequences satisfy the law of large numbers, as computably random ones do.
2. Let $X$ be computable and $E_X$ the martingale of :ref{#prop-cr-basic} (3). Then $E_X(X \uh n) = 2^n$, so $E_X$ $h$-succeeds on $X$ with $h(n) = 2^n$: computable sequences are not Schnorr random.
:::

:::figure[Two ways in which a computable martingale $d$ can defeat a sequence $X$ at the rate of an order $h$. Left: the capital reaches the order at infinitely many lengths (marked); $X$ is not Schnorr random. Right: the capital is above the order at every length; $X$ is not Kurtz random, a stronger failure studied in the last lesson.]{#fig-success-panels}
<svg class="fig" viewBox="0 0 600 240" width="600" role="img" aria-label="Two plots of the capital of a computable martingale along a sequence against a computable order h. Left: the capital reaches the order at infinitely many points, the failure of Schnorr randomness. Right: the capital is above the order at every point, the failure of Kurtz randomness"><line x1="30" y1="190" x2="288" y2="190" class="axis"/><line x1="30" y1="190" x2="30" y2="24" class="axis"/><text x="292.0" y="194.0" text-anchor="start" class="math" font-size="13">n</text><text x="155.0" y="14" text-anchor="middle" class="label">not Schnorr random: d ≥ h infinitely often</text><polyline points="30.0,162.8 36.2,162.8 42.5,135.6 48.8,135.6 55.0,135.6 61.2,135.6 67.5,108.4 73.8,108.4 80.0,108.4 86.2,108.4 92.5,108.4 98.8,108.4 105.0,108.4 111.2,108.4 117.5,81.2 123.8,81.2 130.0,81.2 136.2,81.2 142.5,81.2 148.8,81.2 155.0,81.2 161.2,81.2 167.5,81.2 173.8,81.2 180.0,81.2 186.2,81.2 192.5,81.2 198.8,81.2 205.0,81.2 211.2,81.2 217.5,53.9 223.8,53.9 230.0,53.9 236.2,53.9 242.5,53.9 248.8,53.9 255.0,53.9 261.2,53.9 267.5,53.9 273.8,53.9 280.0,53.9" class="ink-stroke" stroke-width="1.3"/><polyline points="30.0,173.7 36.2,171.2 42.5,166.0 48.8,162.8 55.0,157.3 61.2,127.4 67.5,97.5 73.8,127.4 80.0,157.3 86.2,163.3 92.5,163.7 98.8,168.3 105.0,162.8 111.2,132.9 117.5,102.9 123.8,73.0 130.0,102.9 136.2,132.9 142.5,162.8 148.8,173.6 155.0,170.5 161.2,165.3 167.5,162.8 173.8,165.3 180.0,138.3 186.2,108.4 192.5,78.4 198.8,48.5 205.0,78.4 211.2,108.4 217.5,138.3 223.8,168.2 230.0,172.8 236.2,168.2 242.5,157.3 248.8,127.4 255.0,97.5 261.2,67.6 267.5,37.6 273.8,67.6 280.0,97.5" class="accent-stroke" stroke-width="1.8"/><circle cx="67.5" cy="97.5" r="3" class="accent-fill"/><circle cx="123.8" cy="73.0" r="3" class="accent-fill"/><circle cx="198.8" cy="48.5" r="3" class="accent-fill"/><circle cx="267.5" cy="37.6" r="3" class="accent-fill"/><line x1="330" y1="190" x2="588" y2="190" class="axis"/><line x1="330" y1="190" x2="330" y2="24" class="axis"/><text x="592.0" y="194.0" text-anchor="start" class="math" font-size="13">n</text><text x="455.0" y="14" text-anchor="middle" class="label">not Kurtz random: d ≥ h everywhere</text><polyline points="330.0,168.5 336.2,168.5 342.5,147.1 348.8,147.1 355.0,147.1 361.2,147.1 367.5,125.6 373.8,125.6 380.0,125.6 386.2,125.6 392.5,125.6 398.8,125.6 405.0,125.6 411.2,125.6 417.5,104.1 423.8,104.1 430.0,104.1 436.2,104.1 442.5,104.1 448.8,104.1 455.0,104.1 461.2,104.1 467.5,104.1 473.8,104.1 480.0,104.1 486.2,104.1 492.5,104.1 498.8,104.1 505.0,104.1 511.2,104.1 517.5,82.7 523.8,82.7 530.0,82.7 536.2,82.7 542.5,82.7 548.8,82.7 555.0,82.7 561.2,82.7 567.5,82.7 573.8,82.7 580.0,82.7" class="ink-stroke" stroke-width="1.3"/><polyline points="330.0,160.0 336.2,156.0 342.5,128.1 348.8,126.2 355.0,130.5 361.2,134.8 367.5,111.6 373.8,105.2 380.0,101.1 386.2,103.7 392.5,109.0 398.8,109.6 405.0,104.0 411.2,98.4 417.5,77.3 423.8,82.5 430.0,85.3 436.2,81.4 442.5,74.9 448.8,72.9 455.0,77.1 461.2,81.6 467.5,80.0 473.8,73.5 480.0,69.4 486.2,71.8 492.5,77.1 498.8,77.9 505.0,72.4 511.2,66.7 517.5,45.4 523.8,50.6 530.0,53.5 536.2,49.8 542.5,43.3 548.8,41.1 555.0,45.2 561.2,49.7 567.5,48.3 573.8,41.9 580.0,37.6" class="accent-stroke" stroke-width="1.8"/><line x1="170" y1="226" x2="192" y2="226" class="ink-stroke" stroke-width="1.3"/><text x="198" y="230" class="label">the order h(n)</text><line x1="330" y1="226" x2="352" y2="226" class="accent-stroke" stroke-width="1.8"/><text x="358" y="230" class="label">the capital d(X↾n)</text></svg>
:::

## Schnorr tests

:::definition[Schnorr]{#def-schnorr-test}
A **Schnorr test** is a Martin-Löf test $(\mathcal U_n)$ such that the measures $\lambda(\mathcal U_n)$ are computable reals, uniformly in $n$. A class is **Schnorr null** if it is contained in $\bigcap_n \mathcal U_n$ for some Schnorr test.
:::

The tests of :ref{#ex-ml-tests} are Schnorr tests: their components are clopen, with rational measures. The equivalence of the two definitions of Schnorr randomness rests on two lemmas. The first makes the generators of a $\Sigma^0_1$ class decidable.

:::lemma{#lem-computable-generator}
From an index of a c.e. set of strings $W$ and a number $m$, one computes an index of a computable prefix-free set $R$ of strings of length at least $m$ with $[R]^{\prec} = [W]^{\prec}$.
:::

:::proof{of=lem-computable-generator}
We modify the construction of :ref{#lem-prefix-free-generator}, processing the elements of $W$ by stages of a computable enumeration $(W_s)$. Start with $R_0 = \emptyset$. At stage $s$, let $L_s$ be the maximum of $s$, $m$, the lengths of the strings of $W_{s+1} \setminus W_s$ and the lengths of the strings of $R_s$. For each $\sigma \in W_{s+1} \setminus W_s$ in turn, add to the current set every string $\tau \succeq \sigma$ of length $L_s$ with no prefix in the current set; let $R_{s+1}$ be the result, and $R = \bigcup_s R_s$. As in the original lemma, every added string has length at least that of all strings already present and no prefix among them, so $R$ is prefix-free; and every sequence extending an element of $W_{s+1}$ has a prefix in $R_{s+1}$, so $[R]^{\prec} = [W]^{\prec}$. A string added at stage $s$ has length $L_s \geq s$; so $\tau \in R$ if and only if $\tau \in R_{|\tau| + 1}$, which is decidable. All strings of $R$ have length at least $m$.
:::

The second lemma is the heart of the matter. A set of strings with finite computable weight $\sum 2^{-|\sigma|}$ is turned into a martingale, as in Ville's theorem, with a twist: a string of length $\ell$ is given a capital that grows with $\ell$. This is affordable because the weight of the long strings is small, and computably so.

:::lemma{#lem-weight-martingale}
Let $(R_n)$ be a uniformly computable sequence of sets of strings such that every element of $R_n$ has length at least $n$, and the **weight** $w = \sum_n \sum_{\sigma \in R_n} 2^{-|\sigma|}$ is finite and computable. Then there are a computable martingale $d$ and an order $h$ such that $d(\sigma) \geq h(|\sigma|)$ for every $n$ and every $\sigma \in R_n$.
:::

:::proof{of=lem-weight-martingale}
For each length $\ell$, the pairs $(n, \sigma)$ with $\sigma \in R_n$ and $|\sigma| = \ell$ have $n \leq \ell$; their weight $W(\ell) = 2^{-\ell} \sum_{n \leq \ell} |R_n \cap 2^\ell|$ is a rational computable from $\ell$. The tails $t(N) = \sum_{\ell \geq N} W(\ell) = w - \sum_{\ell < N} W(\ell)$ are computable reals, uniformly in $N$, and tend to $0$. Let $N_0 = 0$, and let $N_{k+1}$ be the first $N > N_k$ found, in a search through the pairs $(N, j)$, for which a rational approximation $a$ of $t(N)$ within $2^{-j}$ satisfies $a + 2^{-j} < 2^{-2(k+1)}$. The search terminates since $t(N)$ tends to $0$, and $t(N_k) < 2^{-2k}$ for $k \geq 1$. Let $g(\ell)$ be the largest $k$ with $N_k \leq \ell$, computable since $N_k \geq k$, and $h = 2^g$, an order.

Let $d$ be the sum, over all pairs $(n, \sigma)$ with $\sigma \in R_n$, of the martingales $2^{g(|\sigma|) - |\sigma|} E_\sigma$, where $E_\sigma$ is the elementary martingale of :ref{#ex-martingales}. Grouping the strings by length, the initial capital is
$$
\sum_\ell 2^{g(\ell)} W(\ell) = \sum_{k} 2^k \sum_{N_k \leq \ell < N_{k+1}} W(\ell) \leq w + \sum_{k \geq 1} 2^k\, t(N_k) \leq w + \sum_{k \geq 1} 2^{-k} = w + 1,
$$
so $d$ is a martingale by :ref{#lem-martingale-basic} (2). If $\sigma \in R_n$, the term of $(n, \sigma)$ alone gives $d(\sigma) \geq 2^{g(|\sigma|) - |\sigma|} E_\sigma(\sigma) = 2^{g(|\sigma|)} = h(|\sigma|)$.

It remains to compute $d(\tau)$. By the definition of $E_\sigma$,
$$
d(\tau) = \sum_{(n, \sigma) :\ \sigma \preceq \tau} 2^{g(|\sigma|)} + 2^{|\tau|} \sum_{(n, \sigma) :\ \sigma \succ \tau} 2^{g(|\sigma|) - |\sigma|}.
$$
The first sum is finite and computable. In the second, the terms with $|\sigma| \geq N_k$ add up to at most $2^{|\tau|} \sum_{j \geq k} 2^j t(N_j) \leq 2^{|\tau| + 1 - k}$, and the terms with $|\sigma| < N_k$ form a finite computable sum. Choosing $k$ large gives $d(\tau)$ to any precision.
:::

:::theorem[Schnorr]{#thm-schnorr-tests-martingales}
A class $\mathcal C \subseteq \cs$ is Schnorr null if and only if there are a computable martingale $d$ and an order $h$ such that $d$ $h$-succeeds on every member of $\mathcal C$. In particular, a sequence is Schnorr random if and only if it passes every Schnorr test.
:::

:::proof{of=thm-schnorr-tests-martingales}
($\Leftarrow$) Let $f \geq d$ be the rational-valued martingale of :ref{#lem-rational-martingale}; it $h$-succeeds wherever $d$ does. Let $c$ be a positive integer with $f(\varepsilon) \leq c$, $f' = f/c$, and $h'(n) = \lfloor h(n)/c \rfloor$, again an order; $f'$ $h'$-succeeds wherever $f$ $h$-succeeds. For each $i$, the set $G_i = \{ \sigma : f'(\sigma) \geq h'(|\sigma|) \geq 2^i \}$ is computable, uniformly in $i$; let $\mathcal U_i = [G_i]^{\prec}$. By :ref{#lem-kolmogorov-inequality} (2), $\lambda(\mathcal U_i) \leq \lambda(\{ X : \exists n\ f'(X \uh n) \geq 2^i \}) \leq 2^{-i}$. If $f'$ $h'$-succeeds on $X$, then for each $i$ there is $n$ with $h'(n) \geq 2^i$ and $f'(X \uh n) \geq h'(n)$, so $X \in \mathcal U_i$.

The measures are computable. Given $i$ and $j$, let $L$ be the least length with $h'(L) \geq 2^j$. The strings of $G_i$ of length at least $L$ have capital at least $2^j$, so the class they generate has measure at most $2^{-j}$, by Kolmogorov's inequality again. The strings of $G_i$ of length less than $L$ generate a clopen class whose measure is a rational computed from $i$ and $j$; it approximates $\lambda(\mathcal U_i)$ from below within $2^{-j}$. So $(\mathcal U_i)$ is a Schnorr test.

($\Rightarrow$) Let $(\mathcal U_n)$ be a Schnorr test. By :ref{#lem-computable-generator}, there are uniformly computable prefix-free sets $R_n$ with $[R_n]^{\prec} = \mathcal U_n$, whose strings have length at least $n$. The weight $\sum_n \sum_{\sigma \in R_n} 2^{-|\sigma|} = \sum_n \lambda(\mathcal U_n)$ is computable: its terms are computable uniformly, and the tail after $N$ is at most $2^{1-N}$. Let $d$ and $h$ be given by :ref{#lem-weight-martingale}. If $X \in \bigcap_n \mathcal U_n$, then for each $n$ some prefix $X \uh m_n$ belongs to $R_n$, with $m_n \geq n$; so infinitely many prefixes of $X$ belong to some $R_n$, and $d(X \uh m) \geq h(m)$ for each of them.
:::

The measures of a Schnorr test can moreover be taken equal to $2^{-n}$ (Schnorr; Downey–Hirschfeldt, Proposition 7.1.6).

:::quiz[Schnorr's theorem]
In the proof of ($\Leftarrow$), where is it used that $h$ is computable and unbounded?

- [x] To compute the measures: an unbounded computable $h'$ gives a computable length $L$ beyond which every string of $G_i$ has capital at least $2^j$, so that the long strings contribute at most $2^{-j}$.
- [ ] To show that $\lambda(\mathcal U_i) \leq 2^{-i}$.

  This bound comes from Kolmogorov's inequality and the condition $f' \geq 2^i$ on the strings of $G_i$; the order plays no role in it.
- [ ] To make $G_i$ computable.

  The computability of $G_i$ uses that $f'$ is rational-valued and computable, and that $h'$ is computable; unboundedness is not needed for it.

---

In :ref{#lem-weight-martingale}, why does the martingale give the string $\sigma$ the capital $2^{g(|\sigma|)}$ rather than $1$, as in Ville's theorem?

- [x] With capital $1$, a sequence with infinitely many prefixes in the sets $R_n$ would only make the capital unbounded; the factor $2^{g(|\sigma|)}$ makes the capital at such a prefix exceed an order, and it is affordable because the weight of the strings of length at least $N_k$ is below $2^{-2k}$.
- [ ] To make $d$ computable.

  The computability of $d$ comes from the computable tails of the weight; the factor is there for the rate.
- [ ] Because the sets $R_n$ are not prefix-free.

  They may be prefix-free or not; the lemma does not use prefix-freeness.
:::

## Total Solovay tests

The Solovay tests of :ref{#def-solovay-test} have components whose measures are only summable. Requiring the sum to be computable gives tests for Schnorr randomness; the argument above handles them directly.

:::theorem[Downey, Griffiths]{#thm-total-solovay}
A **total Solovay test** is a uniformly $\Sigma^0_1$ sequence $(\mathcal S_n)$ such that $\sum_n \lambda(\mathcal S_n)$ is finite and computable. A sequence $X$ is Schnorr random if and only if, for every total Solovay test $(\mathcal S_n)$, $X$ belongs to only finitely many classes $\mathcal S_n$.
:::

:::proof{of=thm-total-solovay}
($\Leftarrow$) A Schnorr test $(\mathcal U_n)$ is a total Solovay test, since its measures are uniformly computable and bounded by $2^{-n}$; a sequence captured by it belongs to all its components. Apply :ref{#thm-schnorr-tests-martingales}.

($\Rightarrow$) Let $(\mathcal S_n)$ be a total Solovay test, and let $R_n$ be given by :ref{#lem-computable-generator} for $\mathcal S_n$ and $m = n$. The weight $\sum_n \sum_{\sigma \in R_n} 2^{-|\sigma|} = \sum_n \lambda(\mathcal S_n)$ is computable. Let $d$ and $h$ be given by :ref{#lem-weight-martingale}. If $X$ belongs to $\mathcal S_n$ for infinitely many $n$, it has a prefix of length at least $n$ in $R_n$ for each of them, hence infinitely many prefixes in the sets $R_n$, and $d$ $h$-succeeds on $X$.
:::

Only the sum of the measures was used. The following form is used in the last lesson.

:::corollary{#cor-clopen-solovay}
Let $(F_n)$ be a computable sequence of finite sets of strings, given by canonical indices, with $\lambda([F_n]^{\prec}) \leq 2^{-n}$. A sequence that belongs to $[F_n]^{\prec}$ for infinitely many $n$ is not Schnorr random.
:::

:::proof{of=cor-clopen-solovay}
The measures $\lambda([F_n]^{\prec})$ are rationals computed from $n$, and the tail of their sum after $N$ is at most $2^{1-N}$; so the sum is computable, and $([F_n]^{\prec})$ is a total Solovay test.
:::

## No universal Schnorr test

:::proposition[Schnorr]{#prop-no-universal-schnorr}
For every computable martingale $d$ and every order $h$, there is a computable sequence on which $d$ does not $h$-succeed. So no Schnorr test captures every sequence that is not Schnorr random.
:::

:::proof{of=prop-no-universal-schnorr}
Let $f \geq d$ be rational-valued as in :ref{#lem-rational-martingale}, and $X$ its leftmost non-ascending path, which is computable (:ref{#prop-cr-basic} (2)). Then $d(X \uh n) \leq f(\varepsilon)$ for every $n$, and $h(n) > f(\varepsilon)$ for almost every $n$, since $h$ is unbounded. For the second statement, a Schnorr test is turned into such a pair $(d, h)$ by :ref{#thm-schnorr-tests-martingales}; it misses a computable sequence, which is not Schnorr random by :ref{#ex-schnorr-success} (2).
:::

:::quiz[total Solovay tests]
In the proof of ($\Rightarrow$) in :ref{#thm-total-solovay}, why does the construction of :ref{#lem-computable-generator} take $m = n$?

- [x] So that each string of $R_n$ has length at least $n$: for each length only finitely many pairs $(n, \sigma)$ occur, which :ref{#lem-weight-martingale} needs to compute the weights by length, and a sequence in infinitely many $\mathcal S_n$ has prefixes of unbounded length in the sets $R_n$.
- [ ] To make $\lambda(\mathcal S_n) \leq 2^{-n}$.

  The measures of a total Solovay test are not bounded by $2^{-n}$; lengthening the generators does not change the classes.
- [ ] Because the classes $\mathcal S_n$ must be disjoint.

  They may overlap; the lemma sums over pairs $(n, \sigma)$ and counts overlaps several times.
:::

## Exercises

::::exercise{difficulty=1}
Let $X$ be Schnorr random. Show that for almost every $n$, the bits $X(n), \dots, X(n + \lceil 2 \log n \rceil - 1)$ are not all $0$ (compare the exercise on runs of zeros of :ref{to="martin-lof-randomness/solovay-tests"}).

:::solution
For $n \geq 2$, let $\mathcal S_n$ be the clopen class of the sequences that vanish on these $\lceil 2 \log n \rceil$ positions; its measure is $2^{-\lceil 2 \log n \rceil} \leq n^{-2}$, a rational computed from $n$ (let $\mathcal S_0 = \mathcal S_1 = \emptyset$). The tail of $\sum_n \lambda(\mathcal S_n)$ after $N \geq 2$ is at most $\sum_{n \geq N} n^{-2} \leq 1/(N - 1)$, so the sum is computable, and $(\mathcal S_n)$ is a total Solovay test. By :ref{#thm-total-solovay}, $X$ belongs to only finitely many $\mathcal S_n$.
:::
::::

## Notes and references

Schnorr introduced his notion and proved :ref{#thm-schnorr-tests-martingales} and :ref{#prop-no-universal-schnorr} in his monograph (1971), as a critique of Martin-Löf's definition; his orders (Ordnungsfunktionen) are computable by definition. :ref{#thm-total-solovay} is due to Downey and Griffiths (2004), who also characterized Schnorr randomness by computable measure machines. :ref{#lem-weight-martingale} is a reformulation of Nies, Lemma 7.3.4, whose proof is followed here. Downey and Hirschfeldt present this material in Section 7.1 (Definitions 7.1.4–7.1.5, Theorem 7.1.7, Definition 7.1.9 and Theorem 7.1.10, Proposition 7.1.11); Nies defines Schnorr tests in Section 3.5 (Definition 3.5.8, Fact 3.5.9 for the absence of a universal test, Fact 3.5.10) and proves the martingale characterization in Section 7.3 (Theorem 7.3.3), where computable prefix-free generators are Fact 1.8.26.

- C.-P. Schnorr, *Zufälligkeit und Wahrscheinlichkeit*, Lecture Notes in Mathematics 218, Springer, 1971.
- R. G. Downey and E. J. Griffiths, *Schnorr randomness*, Journal of Symbolic Logic 69 (2004), 533–554.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 7.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 3.5 and 7.3.
