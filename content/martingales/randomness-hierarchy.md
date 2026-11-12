---
title: The hierarchy of randomness notions
summary: Kurtz randomness characterized by martingales that stay above an order; Martin-Löf, computable, Schnorr and Kurtz randomness form a strict hierarchy; outside the high degrees, Schnorr randomness implies Martin-Löf randomness; partial computable and Kolmogorov–Loveland randomness, and the open question whether the latter equals Martin-Löf randomness.
duration: 45
prerequisites: [schnorr-randomness, cr-construction, martin-lof-randomness/solovay-tests, immunity-growth/domination, turing-degrees/finite-extensions]
---

The previous lessons defined three notions of randomness by betting strategies of decreasing power: c.e. martingales for Martin-Löf randomness, computable martingales for computable randomness, computable martingales with a computable rate of success for Schnorr randomness. Kurtz randomness, defined in :ref{#ex-kurtz} by null $\Pi^0_1$ classes, fits at the bottom of this scale, as Wang showed. This lesson compares the four notions, proves the separations that can be proved at this level, and shows, following Nies, Stephan and Terwijn, that the three upper notions differ only on high sequences. It ends with stronger betting strategies and the main open question of the area.

## Kurtz randomness and martingales

Recall from :ref{#ex-kurtz} that a sequence is **Kurtz random** if it belongs to no null $\Pi^0_1$ class. Schnorr randomness requires that a computable strategy stays below an order from some point on; Kurtz randomness only requires that it does not stay above an order everywhere.

:::theorem[Wang]{#thm-kurtz-martingales}
A sequence $X$ is not Kurtz random if and only if there are a computable martingale $d$ and an order $h$ such that $d(X \uh n) \geq h(n)$ for every $n$.
:::

:::proof{of=thm-kurtz-martingales}
($\Rightarrow$) Let $X \in [T]$, with $T$ a computable tree and $\lambda([T]) = 0$. For each $n$, let $m_n$ be the least $m$ with $|T \cap 2^m| \leq 2^{m-n}$; it exists since $2^{-m} |T \cap 2^m|$ tends to $\lambda([T]) = 0$ (:ref{#prop-measure-effective} (2)), and it is computable. Let $F_n = T \cap 2^{m_n}$, so that $[T] \subseteq [F_n]^{\prec}$ and $\lambda([F_n]^{\prec}) \leq 2^{-n}$. Since $X \in [T]$, every level of $T$ is non-empty, so $2^{m_n - n} \geq 1$ and $m_n \geq n$. Let
$$
d = \sum_n \sum_{\sigma \in F_n} 2^{-m_n} E_\sigma.
$$
Its initial capital is $\sum_n \lambda([F_n]^{\prec}) \leq 2$, so it is a martingale. It is computable: at a string $\tau$, the pairs $(n, \sigma)$ with $m_n \leq |\tau|$ have $n \leq |\tau|$ and give a finite computable sum, and those with $m_n > |\tau|$ contribute at most $2^{|\tau|} \lambda([F_n]^{\prec} \cap [\tau]) \leq 2^{|\tau| - n}$ each, so the terms with $n \geq N$ add up to at most $2^{|\tau| + 1 - N}$. For every $n$, $X \uh m_n \in F_n$, and the term of $(n, X \uh m_n)$ equals $1$ at every $X \uh m$ with $m \geq m_n$. So $d(X \uh m) \geq h(m)$, where $h(m) = |\{ n : m_n \leq m \}|$ is computable, non-decreasing, and unbounded: an order.

($\Leftarrow$) Let $f \geq d$ be rational-valued as in :ref{#lem-rational-martingale}, $c$ a positive integer with $f(\varepsilon) \leq c$, $f' = f/c$ and $h' = \lfloor h/c \rfloor$, so that $f'(X \uh n) \geq h'(n)$ for every $n$. For each $k$, let $g(k)$ be the least $n$ with $h'(n) \geq 2^k$, a computable function, and let
$$
\mathcal P = \{ Y : \forall k\ f'(Y \uh g(k)) \geq 2^k \}.
$$
Each condition is decidable from $Y \uh g(k)$, and only finitely many $k$ have $g(k) \leq \ell$ for a given $\ell$; so $\mathcal P$ is the class of paths of a computable tree, a $\Pi^0_1$ class. It contains $X$, since $f'(X \uh g(k)) \geq h'(g(k)) \geq 2^k$. For each $k$, $\mathcal P \subseteq \{ Y : \exists n\ f'(Y \uh n) \geq 2^k \}$, of measure at most $2^{-k}$ by :ref{#lem-kolmogorov-inequality} (2); so $\mathcal P$ is null, and $X$ is not Kurtz random.
:::

The condition "for every $n$" can be replaced by "for almost every $n$": if $d(X \uh n) \geq h(n)$ for $n \geq n_0$, the order equal to $0$ below $n_0$ and to $h$ elsewhere works for every $n$. The martingale characterizations now read as follows, with $d$ ranging over computable martingales and $h$ over orders.

| notion | the sequence $X$ is not random if |
| --- | --- |
| Martin-Löf | some c.e. martingale is unbounded along $X$ |
| computable | some computable $d$ is unbounded along $X$ |
| Schnorr | some $d$, $h$ have $d(X \uh n) \geq h(n)$ for infinitely many $n$ |
| Kurtz | some $d$, $h$ have $d(X \uh n) \geq h(n)$ for almost every $n$ |

:::proposition{#prop-hierarchy}
Every Martin-Löf random sequence is computably random, every computably random sequence is Schnorr random, and every Schnorr random sequence is Kurtz random.
:::

:::proof{of=prop-hierarchy}
Read the table from the bottom: a capital above an order at almost every $n$ is above it at infinitely many $n$; a capital above an order infinitely often is unbounded; and a computable martingale is c.e. The first implication is also :ref{#prop-cr-basic} (1).
:::

:::figure[The four notions of randomness defined by martingales, with the reasons why each implication is strict. The first three coincide on sequences that are not high (:ref{#thm-nst-nonhigh}); Kurtz randomness differs from Schnorr randomness already on low sequences.]{#fig-hierarchy}
<svg class="fig" viewBox="0 0 600 310" width="600" role="img" aria-label="Four boxes from top to bottom: Martin-Löf, computable, Schnorr and Kurtz randomness, each with its martingale characterization, joined by implication arrows with the reason why each implication is strict; a bracket marks that the first three notions coincide outside the high degrees"><defs><marker id="mg-hier-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="150" y="12" width="300" height="46" rx="4" class="cell"/><text x="162" y="31" font-size="13">Martin-Löf random</text><text x="162" y="49" class="label">no c.e. martingale succeeds</text><rect x="150" y="92" width="300" height="46" rx="4" class="cell"/><text x="162" y="111" font-size="13">computably random</text><text x="162" y="129" class="label">no computable martingale succeeds</text><rect x="150" y="172" width="300" height="46" rx="4" class="cell"/><text x="162" y="191" font-size="13">Schnorr random</text><text x="162" y="209" class="label">no computable d, order h with d ≥ h infinitely often</text><rect x="150" y="252" width="300" height="46" rx="4" class="cell"/><text x="162" y="271" font-size="13">Kurtz random</text><text x="162" y="289" class="label">no computable d, order h with d ≥ h everywhere</text><line x1="300.0" y1="60" x2="300.0" y2="89" class="ink-stroke" stroke-width="1.3" marker-end="url(#mg-hier-arrow)"/><text x="310.0" y="79.0" class="label">strict: a Δ⁰₂ example (lesson 5)</text><line x1="300.0" y1="140" x2="300.0" y2="169" class="ink-stroke" stroke-width="1.3" marker-end="url(#mg-hier-arrow)"/><text x="310.0" y="159.0" class="label">strict: admitted (high degrees)</text><line x1="300.0" y1="220" x2="300.0" y2="249" class="ink-stroke" stroke-width="1.3" marker-end="url(#mg-hier-arrow)"/><text x="310.0" y="239.0" class="label">strict: weakly 1-generic sequences</text><path d="M136,18 L128,18 L128,212 L136,212" class="accent-stroke" stroke-width="1.5"/><text x="120" y="109.0" text-anchor="end" class="label">equal for sequences</text><text x="120" y="125.0" text-anchor="end" class="label">that are not high</text></svg>
:::

## Separations

:::proposition{#prop-kurtz-not-schnorr}
Every weakly 1-generic sequence is Kurtz random and not Schnorr random. There is such a sequence that is computable in $\emptyset'$ and low.
:::

:::proof{of=prop-kurtz-not-schnorr}
Weakly 1-generic sequences are Kurtz random by :ref{#ex-kurtz}. Let $G$ be weakly 1-generic. For each $n$, the computable set of strings of length at least $n$ with at least two thirds of ones is dense, as shown in the solution of :ref{#ex-kurtz}; so infinitely many prefixes of $G$ have at least $(\frac12 + \frac16)$ times their length of ones. By :ref{#ex-schnorr-success} (1), the proportional strategy $p_{1/6}$ $h$-succeeds on $G$ for an order $h$, and $G$ is not Schnorr random. Finally, a 1-generic set $G \leq_T \emptyset'$ exists by :ref{#prop-1-generic}; it is weakly 1-generic, since a dense set of strings contains extensions of every string, and it is low, as shown in :ref{to="turing-degrees/low-and-high"}.
:::

The separation of computable randomness from Martin-Löf randomness is :ref{#thm-cr-not-mlr}: a sequence computable in $\emptyset'$ whose prefixes have complexity $O((\log n)^2)$. The separation of Schnorr randomness from computable randomness is harder and admitted here: Wang (1996, 1999) built a Schnorr random sequence that is not computably random, and Nies, Stephan and Terwijn (2005) showed that every high degree contains one, as well as a computably random sequence that is not Martin-Löf random (Downey–Hirschfeldt, Theorem 8.11.6; Nies, Theorems 7.5.9 and 7.5.10). Their constructions combine the technique of :ref{#thm-cr-not-mlr} with a dominant function computed by the high degree, which bounds the running times of the total candidate martingales, and, for the separation of Schnorr from computable randomness, with deterministic bits placed so sparsely that no computable strategy exploits them at a computable rate.

## Randomness outside the high degrees

Why high degrees? A sequence $X$ that is captured by a Martin-Löf test enters each component at some stage, and the function giving these stages is computable from $X$. If $X$ is not high, this function does not dominate every computable function, by Martin's theorem; a computable function exceeds it infinitely often, and cutting the test at these computable stages gives a test with clopen components, of computable measure, that still captures $X$ infinitely often.

:::theorem[Nies, Stephan, Terwijn]{#thm-nst-nonhigh}
If $X$ is Schnorr random and not high, then $X$ is Martin-Löf random.
:::

:::proof{of=thm-nst-nonhigh}
Suppose that $X$ is not Martin-Löf random, captured by a Martin-Löf test $(\mathcal U_n)$, and not high. Let $\mathcal U_{n,s}$ be the clopen class generated by the strings enumerated into the $n$-th component by stage $s$. Let $f(n)$ be the least $s$ with $X \in \mathcal U_{n,s}$; it exists since $X \in \mathcal U_n$, and $f \leq_T X$. Since $X$ is not high, $f$ is not dominant (:ref{#thm-martin-domination}): there is a computable function $g$ with $g(n) > f(n)$ for infinitely many $n$. The classes $\mathcal U_{n, g(n)}$ are clopen, computed from $n$, of measure at most $\lambda(\mathcal U_n) \leq 2^{-n}$, and $X \in \mathcal U_{n, g(n)}$ whenever $g(n) > f(n)$, since the classes $\mathcal U_{n,s}$ increase with $s$. By :ref{#cor-clopen-solovay}, $X$ is not Schnorr random.
:::

:::corollary{#cor-nst}
1. On sequences that are not high, Martin-Löf, computable and Schnorr randomness coincide.
2. A computably dominated Schnorr random sequence is Martin-Löf random.
3. The computably random sequence of :ref{#thm-cr-not-mlr} is high.
:::

:::proof{of=cor-nst}
(1) follows from the theorem and :ref{#prop-hierarchy}. For (2), a computably dominated set is not high (:ref{#cor-high-hyperimmune}). For (3), the sequence is computably random, hence Schnorr random, and not Martin-Löf random.
:::

By the theorem of Nies, Stephan and Terwijn quoted above, the converse holds: each high degree contains a Schnorr random sequence that is not computably random, and a computably random sequence that is not Martin-Löf random. So the high degrees are exactly the degrees in which the three notions can be separated. Kurtz randomness behaves differently: by :ref{#prop-kurtz-not-schnorr} it differs from Schnorr randomness on a low sequence, while on computably dominated sequences it implies Martin-Löf randomness, a theorem of the same authors proved in the course on notions of randomness (:ref{to="randomness-notions/schnorr-kurtz"}).

:::quiz[randomness outside the high degrees]
In the proof of :ref{#thm-nst-nonhigh}, why is the test $(\mathcal U_{n, g(n)})$ not a Martin-Löf test capturing $X$?

- [x] Because $X$ belongs to $\mathcal U_{n, g(n)}$ only for the infinitely many $n$ with $g(n) > f(n)$, not for every $n$; this is why a Solovay-type test is used.
- [ ] Because its components are not $\Sigma^0_1$.

  They are clopen and computed from $n$, hence uniformly $\Sigma^0_1$.
- [ ] Because its measures are not bounded by $2^{-n}$.

  $\mathcal U_{n, g(n)} \subseteq \mathcal U_n$, so the bound holds.

---

Where is the hypothesis that $X$ is not high used?

- [x] To find a computable $g$ that exceeds the $X$-computable function $f$ infinitely often: by Martin's theorem, a set that is not high computes no dominant function.
- [ ] To show that $f$ is total.

  $f$ is total because $X$ is captured by the test.
- [ ] To show that the classes $\mathcal U_{n,s}$ are clopen.

  They are clopen for every test: they are generated by finitely many strings.
:::

## Beyond computable strategies

Martin-Löf randomness is defined by strategies whose capital is only approximable; computable randomness by strategies whose bets are computed. Between the two, several notions of betting have been studied.

A **partial computable martingale** (:ref{#ex-partial-martingale}) may leave its capital undefined: it may wait forever before deciding its bet at some string, and it only succeeds along sequences on which it is defined. Every Martin-Löf random sequence is **partial computably random**, by the same exercise, and every partial computably random sequence is computably random. Both implications are strict: Nies (Theorems 7.4.15 and 7.5.7) builds a partial computably random sequence whose prefixes have complexity at most $h(n) \log n$ for every order $h$, hence not Martin-Löf random, and a computably random sequence that is not partial computably random.

A **nonmonotonic** betting strategy, introduced by Muchnik, Semenov and Uspensky (1998), chooses at each step which position of the sequence to bet on next, as a function of the bits it has seen, and may thus visit the positions in any order. A sequence is **Kolmogorov–Loveland random** if no partial computable nonmonotonic strategy succeeds on it. Every Martin-Löf random sequence is Kolmogorov–Loveland random (Muchnik, Semenov and Uspensky; Downey–Hirschfeldt, Theorem 7.5.5), and Kolmogorov–Loveland randomness implies partial computable randomness, since a monotonic strategy is a special case.

:::question{#q-kl-mlr}
Is every Kolmogorov–Loveland random sequence Martin-Löf random?
:::

The question is open. A positive answer would characterize Martin-Löf randomness by strategies whose bets are computable, answering Schnorr's critique without weakening the notion. Merkle, Miller, Nies, Reimann and Stephan (2006) showed that Kolmogorov–Loveland random sequences are close to Martin-Löf random ones: if $Z_0 \oplus Z_1$ is Kolmogorov–Loveland random, then $Z_0$ or $Z_1$ is Martin-Löf random. Most researchers expect a negative answer (Nies, introduction to Chapter 7).

## Exercises

::::exercise{difficulty=1}
Let $X$ be a sequence with $X(2^k) = 0$ for every $k$. Give a computable martingale $d$ and an order $h$ with $d(X \uh n) \geq h(n)$ for every $n$, and deduce from :ref{#thm-kurtz-martingales} that $X$ is not Kurtz random. Find the null $\Pi^0_1$ class directly.

:::solution
Let $d$ bet its whole capital on $0$ at the positions $2^k$ and not bet elsewhere: $d(\varepsilon) = 1$, $d(\sigma 0) = 2 d(\sigma)$ and $d(\sigma 1) = 0$ if $|\sigma|$ is a power of $2$, and $d(\sigma 0) = d(\sigma 1) = d(\sigma)$ otherwise. Along $X$, $d(X \uh n) = 2^{h(n)}$, where $h(n)$ is the number of $k$ with $2^k < n$, an order; so $d(X \uh n) \geq h(n)$. The class $\{ Y : \forall k\ Y(2^k) = 0 \}$ is $\Pi^0_1$, contains $X$, and has measure at most $2^{-m}$ for every $m$, as it is contained in the clopen class of the sequences vanishing at $2^0, \dots, 2^{m-1}$.
:::
::::

::::exercise{difficulty=2}
Show that a Schnorr random sequence Turing equivalent to a c.e. set is high. (Use the exercise of :ref{to="martin-lof-randomness/random-dnc"} on random sequences of c.e. degree.)

:::solution
Let $X$ be Schnorr random with $X \equiv_T A$, $A$ c.e. If $X$ is not high, it is Martin-Löf random by :ref{#thm-nst-nonhigh}; a random sequence of c.e. degree is Turing equivalent to $\emptyset'$, by the exercise; and $\emptyset'$ is high, since $\emptyset'' \leq_T (\emptyset')'$. This contradicts the assumption that $X$ is not high.
:::
::::

::::exercise{difficulty=1}
Kurtz's original definition: show that a sequence is Kurtz random if and only if it belongs to every $\Sigma^0_1$ class of measure $1$.

:::solution
The complement of a $\Sigma^0_1$ class is a $\Pi^0_1$ class (:ref{#prop-pi01-equivalent}), and conversely; a class has measure $1$ if and only if its complement is null. So avoiding every null $\Pi^0_1$ class is the same as belonging to every $\Sigma^0_1$ class of measure $1$.
:::
::::

## Notes and references

Kurtz (1981) introduced the notion bearing his name, in the form of the last exercise. :ref{#thm-kurtz-martingales} is due to Wang (1996); the proof of ($\Rightarrow$) follows Downey, Griffiths and Reid (Downey–Hirschfeldt, Theorem 7.2.13), and the proof of ($\Leftarrow$) builds the $\Pi^0_1$ class directly. :ref{#thm-nst-nonhigh} and its converse are due to Nies, Stephan and Terwijn (2005); the proof follows Nies (Proposition 3.5.13) and Downey–Hirschfeldt (Theorem 8.11.2), who derive it from total Solovay tests. The separation of Schnorr and computable randomness is due to Wang (1996, 1999); the separations among left-c.e. reals are due to Downey, Griffiths and LaForte (2004) (Downey–Hirschfeldt, Section 8.11.2). Nonmonotonic randomness and :ref{#q-kl-mlr} come from Muchnik, Semenov and Uspensky (1998) (Downey–Hirschfeldt, Section 7.5; Nies, Section 7.6, Definition 7.6.19 and Theorem 7.6.21 for the result on halves).

- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana–Champaign, 1981.
- Y. Wang, *Randomness and complexity*, PhD thesis, University of Heidelberg, 1996.
- Y. Wang, *A separation of two randomness concepts*, Information Processing Letters 69 (1999), 115–118.
- A. Nies, F. Stephan and S. A. Terwijn, *Randomness, relativization and Turing degrees*, Journal of Symbolic Logic 70 (2005), 515–535.
- An. A. Muchnik, A. L. Semenov and V. A. Uspensky, *Mathematical metaphysics of randomness*, Theoretical Computer Science 207 (1998), 263–317.
- W. Merkle, J. S. Miller, A. Nies, J. Reimann and F. Stephan, *Kolmogorov–Loveland randomness and stochasticity*, Annals of Pure and Applied Logic 138 (2006), 183–210.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 7.2, 7.5 and 8.11.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 3.5 and 7.4–7.6.
