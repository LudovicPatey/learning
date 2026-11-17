---
title: A computably random sequence that is not Martin-Löf random
summary: A computably random sequence computable in ∅′ whose prefixes have complexity O((log n)²), built by diagonalizing against a combined martingale and compressing the construction; Martin-Löf randomness is strictly stronger than computable randomness.
duration: 30
prerequisites: [computable-randomness]
---

Every Martin-Löf random sequence is computably random. This lesson shows that the converse fails, by building a sequence that defeats all computable strategies at once while having very compressible prefixes. The construction is the first example of two techniques used throughout the study of weak randomness notions: diagonalize against a single **combined strategy**, along a path where its capital does not increase, and **compress the construction**, by observing that it uses little information about its oracle.

## The construction

A single computable martingale fails on its computable leftmost non-ascending path. To defeat all computable martingales at once, one would follow the non-ascending path of their weighted sum, but the sum cannot be computed: one cannot decide which partial computable functions are total martingales. With the oracle $\emptyset'$, one can decide whether a partial computable function is defined and satisfies the martingale equality **up to a given length**. The idea is to add the $e$-th candidate to the sum at position $2^e$, to drop it as soon as it fails to be a martingale on the next length, and to follow the non-ascending path of the current sum. Total martingales are never dropped, and their capital stays bounded. The sequence obtained is simple: its prefix of length $n$ is determined by $n$ and by the positions at which the $\log n$ or so candidates introduced so far were dropped, as in :ref{#fig-exit-timeline}. So its prefixes are compressible, and it is not Martin-Löf random.

Let $(\psi_e)$ be an effective enumeration of the partial computable functions from strings to non-negative rationals. Say that $e$ is **$n$-good** if $\psi_e(\sigma)$ is defined for every string $\sigma$ of length at most $n + 1$, and $\psi_e(\sigma 0) + \psi_e(\sigma 1) = 2 \psi_e(\sigma)$ for every $\sigma$ of length at most $n$. If $e$ is $n$-good, it is $m$-good for every $m \leq n$. Every rational-valued computable martingale is equal to some $\psi_e$, and this $e$ is $n$-good for every $n$. The relation "$e$ is $n$-good" is $\Sigma^0_1$, hence decidable in $\emptyset'$.

:::theorem{#thm-cr-not-mlr}
There is a computably random sequence $X \leq_T \emptyset'$ and a constant $c$ such that $K(X \uh n) \leq (\log(n+1) + 2)^2 + c$ for every $n$. In particular $X$ is not Martin-Löf random.
:::

:::proof{of=thm-cr-not-mlr}
*Construction.* For each $n$, let $A_n = \{ e : 2^e \leq n \text{ and } e \text{ is } n\text{-good} \}$, the set of **active** indices at position $n$; $A_0$ is empty. We define $X(n)$ and, when $n = 2^e$ and $e \in A_n$, a positive rational weight $w_e$, by recursion on $n$. Suppose $X \uh n$ is defined. If $n = 2^e$ and $e \in A_n$, let
$$
w_e = \frac{2^{-e}}{1 + \psi_e(X \uh n)}, \quad\text{so that } w_e\, \psi_e(X \uh 2^e) \leq 2^{-e}.
$$
Every $e \in A_n$ belongs to $A_{2^e}$, since goodness is preserved downwards, so $w_e$ is defined for all $e \in A_n$. For strings $\tau$ of length $n$ or $n + 1$, let $D_n(\tau) = \sum_{e \in A_n} w_e\, \psi_e(\tau)$, a finite sum of defined values. Let $X(n) = 0$ if $D_n((X \uh n) 0) \leq D_n(X \uh n)$, and $X(n) = 1$ otherwise. With $\emptyset'$ one computes $A_n$, and then the values needed; so $X \leq_T \emptyset'$.

*The combined capital stays below $2$.* Each $\psi_e$ with $e \in A_n$ satisfies the martingale equality at $X \uh n$, so $D_n((X \uh n) 0) + D_n((X \uh n) 1) = 2 D_n(X \uh n)$, and as in :ref{#lem-non-ascending}, $D_n(X \uh (n+1)) \leq D_n(X \uh n)$. An index active at position $n + 1$ was active at position $n$, unless $2^e = n + 1$; so
$$
D_{n+1}(X \uh (n+1)) \leq D_n(X \uh (n+1)) + \sum_{e : 2^e = n+1} w_e\, \psi_e(X \uh (n+1)) \leq D_n(X \uh n) + \sum_{e : 2^e = n + 1} 2^{-e}.
$$
By induction, $D_n(X \uh n) \leq \sum_{e : 2^e \leq n} 2^{-e} < 2$ for every $n$.

*$X$ is computably random.* Let $d$ be a computable martingale. By :ref{#lem-rational-martingale} it suffices to show that a rational-valued computable martingale $f \geq d$ is bounded along $X$. Let $e$ be such that $\psi_e = f$. Then $e \in A_n$ for every $n \geq 2^e$, so $w_e\, f(X \uh n) \leq D_n(X \uh n) < 2$, and $f(X \uh n) < 2/w_e$ for every $n \geq 2^e$.

*The prefixes of $X$ are compressible.* Fix $n \geq 1$. For each $e$ with $2^e \leq n$, there are $k(n) = \lfloor \log n \rfloor + 1$ of them, let $t_e$ be the least $m$ with $2^e \leq m \leq n$ such that $e$ is not $m$-good, or $t_e = n + 1$ if there is none: the **exit position** of $e$. Since goodness is preserved downwards, for every $m < n$,
$$
A_m = \{ e : 2^e \leq m < t_e \}.
$$
So $X \uh n$ is computable from $n$ and the numbers $t_e$, without oracle: for $m = 0, \dots, n - 1$, compute $A_m$ from the exit positions, the weights and the values $\psi_e(\tau)$ for $e \in A_m$ and $|\tau| \in \{m, m+1\}$, which are defined since $e$ is $m$-good, and then $X(m)$. Each $t_e$ is at most $n + 1$, and is written in binary with exactly $\ell(n) = \lfloor \log(n+1) \rfloor + 1$ bits.

Let $U$ be the optimal prefix-free machine. Define a machine $M$: on an input $\alpha\beta$ such that $U(\alpha) = n$ and $|\beta| = k(n)\, \ell(n)$, cut $\beta$ into $k(n)$ words of length $\ell(n)$, read them as the exit positions $t_e$, and output the string computed from $n$ and these numbers as above, if the computation halts. The domain of $M$ is prefix-free: if $\alpha\beta$ and $\alpha'\beta'$ are in it and comparable, then $\alpha$ and $\alpha'$ are comparable elements of the domain of $U$, hence equal, and $\beta$, $\beta'$ have the same length. With the true exit positions, $M$ outputs $X \uh n$. Hence, for a constant $c_M$ and every $n \geq 1$,
$$
K(X \uh n) \leq K(n) + k(n)\, \ell(n) + c_M \leq K(n) + (\log(n+1) + 1)^2 + c_M.
$$
By :ref{#prop-k-basic} (2), $K(n) \leq 2 \log(n+1) + c'$ for a constant $c'$, which gives the bound of the theorem, with $c$ also covering $n = 0$. Since $(\log(n+1) + 2)^2 + c < n - c''$ for all large $n$, whatever the constant $c''$, $X$ is not Martin-Löf random by the Levin–Schnorr theorem (:ref{#thm-levin-schnorr}).
:::

:::figure[The active indices in the proof of :ref{#thm-cr-not-mlr}. Index $e$ enters the combined martingale at position $2^e$ and leaves it at its exit position, the first $m$ such that $\psi_e$ is not defined, or not a martingale, on the strings of length at most $m + 1$; total martingales never leave. Up to position $n$, about $\log n$ indices have entered, and the exit positions, each written with about $\log n$ bits, determine $X \uh n$.]{#fig-exit-timeline}
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="For each index e from 0 to 4, the interval of positions during which e belongs to the set of active indices: it starts at 2 to the e and ends at the exit position, if any; a vertical line at position 24"><defs><marker id="mg-exit-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="70" y1="186" x2="576" y2="186" class="axis"/><line x1="70.0" y1="186" x2="70.0" y2="190" class="axis"/><text x="70.0" y="203.0" text-anchor="middle" class="mrm" font-size="11">0</text><line x1="85.6" y1="186" x2="85.6" y2="190" class="axis"/><text x="85.6" y="203.0" text-anchor="middle" class="mrm" font-size="11">1</text><line x1="101.2" y1="186" x2="101.2" y2="190" class="axis"/><text x="101.2" y="203.0" text-anchor="middle" class="mrm" font-size="11">2</text><line x1="132.5" y1="186" x2="132.5" y2="190" class="axis"/><text x="132.5" y="203.0" text-anchor="middle" class="mrm" font-size="11">4</text><line x1="195.0" y1="186" x2="195.0" y2="190" class="axis"/><text x="195.0" y="203.0" text-anchor="middle" class="mrm" font-size="11">8</text><line x1="320.0" y1="186" x2="320.0" y2="190" class="axis"/><text x="320.0" y="203.0" text-anchor="middle" class="mrm" font-size="11">16</text><line x1="445.0" y1="186" x2="445.0" y2="190" class="axis"/><text x="445.0" y="203.0" text-anchor="middle" class="mrm" font-size="11">24</text><line x1="570.0" y1="186" x2="570.0" y2="190" class="axis"/><text x="570.0" y="203.0" text-anchor="middle" class="mrm" font-size="11">32</text><text x="572" y="220" class="label" text-anchor="end">position n</text><text x="14.0" y="44.0" text-anchor="start" class="mrm" font-size="13">e = 0</text><circle cx="85.6" cy="40" r="3.5" class="accent-fill"/><line x1="85.6" y1="40" x2="574.0" y2="40" class="accent-stroke" stroke-width="2.2" marker-end="url(#mg-exit-arrow)"/><text x="14.0" y="74.0" text-anchor="start" class="mrm" font-size="13">e = 1</text><circle cx="101.2" cy="70" r="3.5" class="accent-fill"/><line x1="101.2" y1="70" x2="163.8" y2="70" class="accent-stroke" stroke-width="2.2"/><line x1="163.8" y1="64" x2="163.8" y2="76" class="ink-stroke" stroke-width="1.6"/><text x="169.8" y="74" class="label">exit at 6</text><text x="14.0" y="104.0" text-anchor="start" class="mrm" font-size="13">e = 2</text><circle cx="132.5" cy="100" r="3.5" class="accent-fill"/><line x1="132.5" y1="100" x2="574.0" y2="100" class="accent-stroke" stroke-width="2.2" marker-end="url(#mg-exit-arrow)"/><text x="14.0" y="134.0" text-anchor="start" class="mrm" font-size="13">e = 3</text><circle cx="195.0" cy="130" r="3.5" class="accent-fill"/><line x1="195.0" y1="130" x2="241.9" y2="130" class="accent-stroke" stroke-width="2.2"/><line x1="241.9" y1="124" x2="241.9" y2="136" class="ink-stroke" stroke-width="1.6"/><text x="247.9" y="134" class="label">exit at 11</text><text x="14.0" y="164.0" text-anchor="start" class="mrm" font-size="13">e = 4</text><circle cx="320.0" cy="160" r="3.5" class="accent-fill"/><line x1="320.0" y1="160" x2="574.0" y2="160" class="accent-stroke" stroke-width="2.2" marker-end="url(#mg-exit-arrow)"/><line x1="445.0" y1="22" x2="445.0" y2="186" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3"/><text x="445.0" y="16.0" text-anchor="middle" class="mrm" font-size="12">n = 24</text><text x="70" y="244" class="label">X↾24 is computed from 24 and the exit data of e = 0, …, 4: (none, 6, none, 11, none)</text></svg>
:::

The proof uses two recurring techniques. The **combined supermartingale**: rather than defeating the strategies one by one, the construction defeats a single weighted sum, which dominates each total strategy up to a constant. The **compression of the construction**: a sequence built by a construction that uses little information about its oracle has compressible prefixes. Since the information needed grows with the number of strategies introduced, slowing down the introduction, at positions given by a faster-growing computable function, gives smaller bounds: for every computable order $h$, there is a computably random $X$ with $K(X \uh n) \leq h(n) \log n$ for almost every $n$ (compare Nies, Theorem 7.4.8, who obtains $K(X \uh n \mid n) \leq h(n)$ by coding instead which candidates are total).

:::quiz[a computably random sequence that is not random]
In the proof of :ref{#thm-cr-not-mlr}, why is the weight $w_e$ divided by $1 + \psi_e(X \uh 2^e)$?

- [x] Because $\psi_e$ may already have a large capital at $X \uh 2^e$ when it enters the sum; the normalization bounds its contribution at entry by $2^{-e}$, so that the entries add at most $\sum_e 2^{-e}$ to the combined capital.
- [ ] To make $w_e\, \psi_e$ a martingale.

  Any positive multiple of a martingale is a martingale; the normalization controls the size at entry.
- [ ] Because $\psi_e(X \uh 2^e)$ may be $0$.

  The $1$ in the denominator avoids a division by $0$, but the division itself is for the bound at entry.

---

Why does the compression use the exit positions rather than the oracle $\emptyset'$?

- [x] Because only the answers to the questions "is $e$ $m$-good?" for the $k(n)$ indices introduced by position $n$ are used, and these answers are determined by $k(n)$ numbers at most $n + 1$.
- [ ] Because $X$ is computable.

  $X$ is computably random, hence not computable (:ref{#prop-cr-basic}).
- [ ] Because the exit positions are computable from $n$.

  They are not: they encode which partial computable functions converge, and are given to the machine as part of the description.

---

Why is $X$ not computably random if the index $e$ of a total martingale could leave the set of active indices?

- [x] This cannot happen: a total martingale is $n$-good for every $n$; the exits only remove functions that are not total martingales, and removing a non-negative term never increases the combined capital.
- [ ] Because it would then succeed on $X$.

  The question rests on a false premise: total martingales are never removed.
- [ ] Because $\emptyset'$ cannot decide totality.

  It cannot, and it does not need to: the construction only asks, for each $n$, a $\Sigma^0_1$ question.
:::

::::exercise{#ex-cr-slow-entry difficulty=2 objective="Slow down the introduction of candidates in the construction to make the prefixes of a computably random sequence as compressible as desired."}
Let $p$ be a computable strictly increasing function, and modify the construction of :ref{#thm-cr-not-mlr} so that the index $e$ enters at position $p(e)$ instead of $2^e$. Show that the sequence obtained is computably random, and that $K(X \uh n) \leq K(n) + k(n)\, \ell(n) + c$, where $k(n)$ is the number of $e$ with $p(e) \leq n$. Deduce that for every order $h$ there is a computably random sequence $X$ with $K(X \uh n) \leq h(n) \log n$ for almost every $n$.

:::solution
The proof of the theorem is unchanged, with $2^e$ replaced by $p(e)$: the combined capital is at most $\sum_e 2^{-e} = 2$, every total rational-valued martingale stays active from position $p(e)$ on, and $X \uh n$ is computed from $n$ and the exit positions of the $k(n)$ indices with $p(e) \leq n$, each written with $\ell(n) = \lfloor \log(n+1) \rfloor + 1$ bits. For the last statement, given an order $h$, let $p(e)$ be the least $n > p(e-1)$ (with $p(-1) = -1$) such that $h(n) \geq 4(e + 2)$. Then $k(n) \leq h(n)/4$ when $k(n) \geq 1$, and $K(X \uh n) \leq 2 \log(n+1) + \frac14 h(n) (\log(n+1) + 1) + c$, which is at most $h(n) \log n$ for almost every $n$, since $h$ is unbounded.
:::
::::

By a theorem of Nies, Stephan and Terwijn, proved in the last lesson (:ref{to="martingales/randomness-hierarchy"}), a computably random sequence that is not Martin-Löf random is high; so the sequence of the theorem is high, and Turing below $\emptyset'$.

## Notes and references

Schnorr (1971) proved that computable randomness is strictly weaker than Martin-Löf randomness. The construction of :ref{#thm-cr-not-mlr} follows the template of Nies (Section 7.4: the supermartingale that dominates every total candidate, the leftmost non-ascending path, and the compression lemma 7.4.10, in the proof of Theorem 7.4.8). The version given here decides the goodness of the candidates up to a given length with $\emptyset'$, which yields a sequence computable in $\emptyset'$, while Nies encodes which candidates are total and bounds the conditional complexity $K(X \uh n \mid n)$. Merkle showed that a computably random sequence can even satisfy $K(X \uh n \mid n) \leq h(n)$ for almost every $n$, simultaneously for every order $h$ (Nies, Theorem 7.4.11). Downey and Hirschfeldt treat the initial segment complexity of computably random sequences in Section 7.4.2.

- C.-P. Schnorr, *Zufälligkeit und Wahrscheinlichkeit*, Lecture Notes in Mathematics 218, Springer, 1971.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 7.4.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 7.4.

:::::exercises
::::exercise{#ex-cr-explicit-bound difficulty=1 objective="Extract from the construction an explicit bound on the capital of each computable martingale along the sequence."}
Let $X$ be the sequence built in the proof of :ref{#thm-cr-not-mlr}, and let $e$ be such that $\psi_e$ is a martingale with $\psi_e(\varepsilon) \leq 1$. Show that $\psi_e(X \uh n) < 2^{2^e + e + 2}$ for every $n$.

:::solution
By :ref{#lem-martingale-basic} (1), $\psi_e(\sigma) \leq 2^{|\sigma|}$ for every $\sigma$. If $n < 2^e$, then $\psi_e(X \uh n) \leq 2^n < 2^{2^e}$. If $n \geq 2^e$, then $e \in A_n$, since $\psi_e$ is $m$-good for every $m$, and the proof gives $w_e\, \psi_e(X \uh n) \leq D_n(X \uh n) < 2$; so
$$
\psi_e(X \uh n) < \frac{2}{w_e} = 2^{e+1} \big(1 + \psi_e(X \uh 2^e)\big) \leq 2^{e+1} \big(1 + 2^{2^e}\big) \leq 2^{2^e + e + 2}.
$$
The bound is computable from $e$; what cannot be computed is the set of indices $e$ to which it applies.
:::
::::

::::exercise{#ex-cr-omega-ce difficulty=2 objective="Approximate the construction by stages and count the mind changes, to see that the sequence has a computable approximation with a computable bound on the number of changes."}
A sequence $X$ is **$\omega$-c.e.** if there are a computable function $(n, s) \mapsto X_s(n) \in \{0, 1\}$ with $\lim_s X_s(n) = X(n)$ for every $n$, and a computable function $b$ such that $X_{s+1}(n) \neq X_s(n)$ for at most $b(n)$ numbers $s$. Show that the sequence $X$ of the proof of :ref{#thm-cr-not-mlr} is $\omega$-c.e.

:::solution
Say that $e$ is **$n$-good at stage $s$** if the computations of $\psi_e(\sigma)$ for $|\sigma| \leq n + 1$ all halt within $s$ steps and the martingale equalities hold for $|\sigma| \leq n$. This is decidable from $(e, n, s)$; it is preserved when $s$ increases and when $n$ decreases; and $e$ is $n$-good if and only if it is $n$-good at some stage.

Let $X_s$ be the result of the construction run with "$m$-good at stage $s$" in place of "$m$-good". All the values it uses are defined, since goodness at stage $s$ guarantees that the computations involved have halted; so $(n, s) \mapsto X_s(n)$ is computable.

Fix $n \geq 1$. For each $e$ with $2^e \leq n$, let $t_{e,s}$ be the least $m$ with $2^e \leq m \leq n$ such that $e$ is not $m$-good at stage $s$, or $n + 1$ if there is none. As in the compression part of the proof, the sets of active indices at positions $m \leq n$ at stage $s$ are $\{ e : 2^e \leq m < t_{e,s} \}$, and $X_s \uh (n+1)$ is computed from $n$ and the numbers $t_{e,s}$ by the same procedure at every stage. Since goodness at stage $s$ persists at later stages, $t_{e,s}$ is non-decreasing in $s$, with values between $2^e$ and $n + 1$: it changes at most $n$ times. So the tuple $(t_{e,s})_{2^e \leq n}$ changes at most $n (\lfloor \log n \rfloor + 1)$ times, and $X_s(n)$ can only change when the tuple does. For $s$ large, each $t_{e,s}$ equals the true exit position computed with $n$, since only finitely many computations are involved; then $X_s \uh (n+1) = X \uh (n+1)$. Hence $\lim_s X_s(n) = X(n)$, with at most $b(n) = n(\lfloor \log n \rfloor + 1)$ changes for $n \geq 1$ (and $b(0) = 0$, since $X_s(0) = 0$ at every stage).
:::
::::

::::exercise{#ex-cr-tot-oracle difficulty=2 objective="Run the construction with the oracle that knows which candidates are total martingales, and compare the complexity of the prefixes."}
Let $\mathrm{Mart}$ be the set of the indices $e$ such that $\psi_e$ is total and a martingale. Run the construction of :ref{#thm-cr-not-mlr} with $A_n = \{ e \in \mathrm{Mart} : 2^e \leq n \}$, keeping the weights and the choice of $X(n)$ unchanged.

1. Show that $\mathrm{Mart}$ is $\Pi^0_2$, and that the sequence $X$ obtained is computable in $\emptyset''$ and computably random.
2. Show that $X \uh n$ is computed from $n$ and the $k(n) = \lfloor \log n \rfloor + 1$ bits $\mathrm{Mart}(e)$, $2^e \leq n$, for $n \geq 1$. Deduce that $K(X \uh n) \leq 3 \log(n+1) + c$ for a constant $c$ and every $n \geq 1$.

:::solution
1. $e \in \mathrm{Mart}$ if and only if $e$ is $n$-good for every $n$; the relation "$e$ is $n$-good" is $\Sigma^0_1$, so $\mathrm{Mart}$ is $\Pi^0_2$, and $\emptyset''$ decides it. For $e \in \mathrm{Mart}$, the values of $\psi_e$ are computable; so the construction is computable in $\mathrm{Mart}$, hence in $\emptyset''$. Every active index is a total martingale and is never removed, so the argument of the proof applies without change: $D_n(X \uh (n+1)) \leq D_n(X \uh n)$, each entry adds at most $2^{-e}$, and $D_n(X \uh n) < 2$. Every rational-valued computable martingale is $\psi_e$ for some $e \in \mathrm{Mart}$, so it is bounded by $2/w_e$ along $X$ from position $2^e$ on; by :ref{#lem-rational-martingale}, $X$ is computably random.
2. Given $n$ and the bits $\mathrm{Mart}(e)$ for $2^e \leq n$, compute for $m = 0, \dots, n - 1$ the set $A_m = \{ e : 2^e \leq m,\ \mathrm{Mart}(e) = 1 \}$, the weights and $X(m)$; the values $\psi_e(\tau)$ needed are those of total functions, and the computation halts. The machine $M$ that, on an input $\alpha\beta$ with $U(\alpha) = n \geq 1$ and $|\beta| = k(n)$, reads $\beta$ as these bits and outputs the string computed, has a prefix-free domain, by the argument of the proof. Hence $K(X \uh n) \leq K(n) + k(n) + c_M$. Since $k(n) \leq \log(n+1) + 1$ and $K(n) \leq 2 \log(n+1) + c'$ by :ref{#prop-k-basic} (2), the bound follows.

The oracle $\emptyset''$ gives a better bound on the complexity, at the price of a sequence that need not be computable in $\emptyset'$. Nies (2009, Theorem 7.4.8) uses this version, with slower entries, to bound $K(X \uh n \mid n)$ by any order.
:::
::::

::::exercise[A partial computably random sequence that is not Martin-Löf random]{#ex-pcr-not-mlr difficulty=3 objective="Adapt the construction to partial computable martingales, deciding with $\emptyset'$ whether a candidate is defined along the sequence built so far."}
Using the notion of :ref{#ex-partial-martingale}, show that there is a partial computably random sequence $X \leq_T \emptyset'$ and a constant $c$ with $K(X \uh n) \leq (\log(n+1) + 2)^2 + c$ for every $n$. So partial computable randomness is strictly weaker than Martin-Löf randomness.

:::solution
Modify the construction of :ref{#thm-cr-not-mlr} by checking the candidates only along the sequence being built. Suppose $X \uh n$ is defined. Say that $e$ is **active at $n$** if $2^e \leq n$ and, for every $m$ with $2^e \leq m \leq n$, the values $\psi_e(X \uh m)$, $\psi_e((X \uh m) 0)$ and $\psi_e((X \uh m) 1)$ are defined and $\psi_e((X \uh m) 0) + \psi_e((X \uh m) 1) = 2 \psi_e(X \uh m)$. Given $X \uh n$, this is a $\Sigma^0_1$ question, decided by $\emptyset'$. If $e$ is active at $n + 1$ and $2^e \leq n$, it is active at $n$. Define the weights $w_e$ when $n = 2^e$ and $e$ is active at $n$, the function $D_n$ on $X \uh n$ and its two children, and $X(n)$, exactly as in the proof; all the values used are defined. So $X \leq_T \emptyset'$.

The argument for the combined capital is unchanged: each active index satisfies the martingale equality at $X \uh n$, so $D_n(X \uh (n+1)) \leq D_n(X \uh n)$, the indices active at $n + 1$ were active at $n$ except the one entering, and $D_n(X \uh n) < 2$ for every $n$.

$X$ is partial computably random. Let $d$ be a partial computable martingale that succeeds on $X$, and $e$ with $\psi_e = d$. Then $d(X \uh m)$ is defined for every $m$; since $d((X \uh m) 0)$ and $d((X \uh m) 1)$ are defined together, and one of them is $d(X \uh (m+1))$, both are defined and satisfy the martingale equality. So $e$ is active at every $n \geq 2^e$, and $d(X \uh n) < 2/w_e$ for $n \geq 2^e$: $d$ is bounded along $X$, a contradiction.

The compression is unchanged. For $n \geq 1$ and $2^e \leq n$, let $t_e$ be the least $m$ with $2^e \leq m \leq n$ such that $e$ is not active at $m$, or $n + 1$. The indices active at $m < n$ are those with $2^e \leq m < t_e$, and from $n$ and the numbers $t_e$ one computes $X \uh n$ without oracle: at each $m$, the values of $\psi_e$ needed for the active $e$ are defined, so their computations halt. The machine of the proof then gives the bound, and $X$ is not Martin-Löf random by :ref{#thm-levin-schnorr}.

Nies (2009, Theorem 7.4.15) obtains $K(X \uh n) \leq h(n) \log n$ for almost every $n$, for every order $h$, by a similar construction.
:::
::::
:::::
