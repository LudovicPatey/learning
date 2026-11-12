---
title: Statistical laws and Solovay tests
summary: Random sequences satisfy the law of large numbers and are normal; Solovay tests, with summable measures, define Martin-Löf randomness; Kurtz randomness and weakly 1-generic sequences.
duration: 40
prerequisites: [martin-lof-tests]
---

Martin-Löf's definition was designed so that random sequences satisfy every effective law of probability. This lesson proves the first of them, the law of large numbers, and its extension to blocks, normality. The argument suggests a second kind of test, in which the measures of the components are only required to be summable. Solovay showed that these tests define the same random sequences; they are the most convenient tool to show that a given sequence is not random, and they are used in the rest of the course.

## The law of large numbers

A random sequence should contain asymptotically as many zeros as ones. This is the law of large numbers, and it follows from a bound on the number of strings with a deviating frequency of ones. The proof is the model of every argument of this kind: a classical estimate of probability bounds the measure of the sequences whose prefix of length $m$ deviates, the bound is summable in $m$, and the tails of the sum give a test.

:::fact[Hoeffding's inequality]{#fact-hoeffding}
For every $\varepsilon > 0$ and $m \geq 1$, the number of strings $\sigma$ of length $m$ with
$$
\left| \frac{|\{ i < m : \sigma(i) = 1 \}|}{m} - \frac{1}{2} \right| > \varepsilon
$$
is at most $2^{m+1} e^{-2 m \varepsilon^2}$.
:::

This is a classical estimate of probability theory, admitted here: it is the case of fair coin tosses of the inequality of Hoeffding (1963), and also follows from the Chernoff bound. A weaker bound, sufficient for the argument below, can be obtained from Markov's inequality applied to the fourth moment of the number of ones.

:::proposition{#prop-large-numbers}
If $X$ is Martin-Löf random, then $\lim_{m} \frac{1}{m} |\{ i < m : X(i) = 1 \}| = \frac{1}{2}$.
:::

:::proof{of=prop-large-numbers}
Fix a rational $\varepsilon > 0$, let $C_m$ be the computable set of strings of length $m$ described in :ref{#fact-hoeffding}, and let $\mathcal V_n = \bigcup_{m > n} [C_m]^{\prec}$, a uniformly $\Sigma^0_1$ sequence. Let $a = e^{-2\varepsilon^2} < 1$. By subadditivity,
$$
\lambda(\mathcal V_n) \leq \sum_{m > n} 2^{-m} \cdot 2^{m+1} a^m = \frac{2 a^{n+1}}{1 - a}.
$$
One computes rationals $q_n$ with $2a^{n+1} / (1 - a) \leq q_n \leq 2a^{n+1} / (1-a) + 2^{-n}$; they tend to $0$. If the frequency of ones in $X \uh m$ differs from $\frac12$ by more than $\varepsilon$ for infinitely many $m$, then $X \in \mathcal V_n$ for every $n$, and $X$ is not random by :ref{#lem-test-bound}. A random $X$ therefore has frequencies eventually within $\varepsilon$ of $\frac12$, for every rational $\varepsilon > 0$.
:::

The same argument, with Hoeffding's inequality for the independent events "the $i$-th block is $\tau$", each of probability $2^{-k}$, applies to blocks: for a random $X$ and a string $\tau$ of length $k$, the frequency of the occurrences of $\tau$ among the blocks $X(ik) \cdots X(ik + k - 1)$ tends to $2^{-k}$. Since the tails of a random sequence are random (:ref{#ex-tails}), the same holds for the blocks starting at the positions $ik + r$, for each $r < k$; so $\tau$ occurs at a position $i < m$ with frequency tending to $2^{-k}$. Random sequences are therefore **normal** in base $2$ in the sense of Borel.

## Solovay tests

The rate $2^{-n}$ in the definition of tests is convenient for building a universal test, but proving that a given sequence is not random is often easier with a summability condition. In the proof of :ref{#prop-large-numbers}, the classes $[C_m]^{\prec}$ have summable measures, and a sequence that deviates infinitely often belongs to infinitely many of them; the test $(\mathcal V_n)$ was obtained from them by taking tails of the union. Solovay tests take such sequences of classes as tests in their own right.

:::definition[Solovay]{#def-solovay-test}
A **Solovay test** is a uniformly $\Sigma^0_1$ sequence $(\mathcal S_n)$ with $\sum_n \lambda(\mathcal S_n) < \infty$. A sequence $X$ is **captured** by the test if $X \in \mathcal S_n$ for infinitely many $n$.
:::

The class captured by a Solovay test is null: it is contained in $\bigcup_{n \geq m} \mathcal S_n$ for every $m$, whose measure is at most $\sum_{n \geq m} \lambda(\mathcal S_n)$, the tail of a convergent series. This is the (first) **Borel–Cantelli lemma**. A Martin-Löf test is a Solovay test, with $\sum_n 2^{-n} = 2$, and a sequence in all its components is in infinitely many. The converse requires an argument.

For the converse, the idea is to count, for each sequence, the number of classes $\mathcal S_n$ containing it. The average of this number over all sequences is $\sum_n \lambda(\mathcal S_n)$, finite, so the sequences belonging to many classes form a class of small measure, and the sequences captured belong to all of these. :ref{#fig-solovay-counting} shows the count on clopen classes.

:::figure[The counting step of the proof of :ref{#thm-solovay} on four clopen classes $\mathcal S_0, \dots, \mathcal S_3$, unions of cylinders of length $4$, with $2^k = 2$. Each cylinder is counted once for each class containing it; the cylinders counted at least twice form $D$. The sum of the counts, divided by $16$, is the sum of the measures, so $\lambda([D]^{\prec})$ is at most half of it.]{#fig-solovay-counting}
<svg class="fig" viewBox="0 0 600 234" width="600" role="img" aria-label="Four clopen classes drawn as unions of cylinders of length 4; below them, the number of classes containing each cylinder, and the cylinders counted at least twice, which form D"><text x="150.0" y="16.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="530.0" y="16.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="20.0" y="40.0" text-anchor="start" class="math" font-size="15">S<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="150" y="24" width="380" height="22" class="cell"/><rect x="151.0" y="25" width="21.8" height="20" class="soft-fill"/><rect x="174.8" y="25" width="21.8" height="20" class="soft-fill"/><rect x="198.5" y="25" width="21.8" height="20" class="soft-fill"/><rect x="222.2" y="25" width="21.8" height="20" class="soft-fill"/><rect x="436.0" y="25" width="21.8" height="20" class="soft-fill"/><rect x="459.8" y="25" width="21.8" height="20" class="soft-fill"/><text x="538" y="39" class="label">6/16</text><text x="20.0" y="70.0" text-anchor="start" class="math" font-size="15">S<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="150" y="54" width="380" height="22" class="cell"/><rect x="198.5" y="55" width="21.8" height="20" class="soft-fill"/><rect x="222.2" y="55" width="21.8" height="20" class="soft-fill"/><rect x="246.0" y="55" width="21.8" height="20" class="soft-fill"/><rect x="341.0" y="55" width="21.8" height="20" class="soft-fill"/><rect x="364.8" y="55" width="21.8" height="20" class="soft-fill"/><text x="538" y="69" class="label">5/16</text><text x="20.0" y="100.0" text-anchor="start" class="math" font-size="15">S<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="150" y="84" width="380" height="22" class="cell"/><rect x="222.2" y="85" width="21.8" height="20" class="soft-fill"/><rect x="364.8" y="85" width="21.8" height="20" class="soft-fill"/><rect x="483.5" y="85" width="21.8" height="20" class="soft-fill"/><rect x="507.2" y="85" width="21.8" height="20" class="soft-fill"/><text x="538" y="99" class="label">4/16</text><text x="20.0" y="130.0" text-anchor="start" class="math" font-size="15">S<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="150" y="114" width="380" height="22" class="cell"/><rect x="269.8" y="115" width="21.8" height="20" class="soft-fill"/><rect x="459.8" y="115" width="21.8" height="20" class="soft-fill"/><text x="538" y="129" class="label">2/16</text><text x="20" y="163" class="label">multiplicity</text><text x="161.9" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="185.6" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="209.4" y="163.0" text-anchor="middle" class="mrm" font-size="12">2</text><text x="233.1" y="163.0" text-anchor="middle" class="mrm" font-size="12">3</text><text x="256.9" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="280.6" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="304.4" y="163.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="328.1" y="163.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="351.9" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="375.6" y="163.0" text-anchor="middle" class="mrm" font-size="12">2</text><text x="399.4" y="163.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="423.1" y="163.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="446.9" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="470.6" y="163.0" text-anchor="middle" class="mrm" font-size="12">2</text><text x="494.4" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="518.1" y="163.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="20" y="193" class="label">D (at least 2)</text><rect x="150" y="178" width="380" height="22" class="cell"/><rect x="198.5" y="179" width="21.8" height="20" class="head-cell"/><rect x="222.2" y="179" width="21.8" height="20" class="head-cell"/><rect x="364.8" y="179" width="21.8" height="20" class="head-cell"/><rect x="459.8" y="179" width="21.8" height="20" class="head-cell"/><text x="538" y="193" class="label">4/16</text><text x="150" y="222" class="label">sum of the measures: 17/16; measure of D: 4/16 ≤ (17/16)/2</text></svg>
:::

:::theorem[Solovay]{#thm-solovay}
A sequence is Martin-Löf random if and only if it is not captured by any Solovay test.
:::

:::proof{of=thm-solovay}
($\Leftarrow$) A Martin-Löf test is a Solovay test, and a sequence captured by it as a Martin-Löf test is captured by it as a Solovay test.

($\Rightarrow$) Let $(\mathcal S_n)$ be a Solovay test, and let $d$ be such that $\sum_n \lambda(\mathcal S_n) \leq 2^d$. Let $\mathcal V_k$ be the class of sequences that belong to $\mathcal S_n$ for at least $2^k$ values of $n$. A sequence captured by the Solovay test belongs to every $\mathcal V_k$. We show that $(\mathcal V_{k + d})_k$ is a Martin-Löf test.

Fix an enumeration of the c.e. set defining $(\mathcal S_n)$. For a stage $s$, let $\mathcal S_{n,s}$ be the clopen class generated by the strings enumerated into the $n$-th component by stage $s$, for $n \leq s$, and $\mathcal S_{n,s} = \emptyset$ for $n > s$. Delaying the enumeration of each string $\sigma$ to a stage at least $|\sigma|$ does not change the classes $\mathcal S_n$; so we may assume that the strings enumerated by stage $s$ have length at most $s$. Each $\mathcal S_{n,s}$ is then a union of cylinders $[\tau]$ with $|\tau| = s$. Let $D_s$ be the set of strings $\tau$ of length $s$ such that $[\tau] \subseteq \mathcal S_{n,s}$ for at least $2^k$ values of $n$; it is computable from $s$ and $k$. Counting pairs $(\tau, n)$ with $|\tau| = s$ and $[\tau] \subseteq \mathcal S_{n,s}$ in two ways gives
$$
2^k\, |D_s| \leq \sum_{|\tau| = s} |\{ n : [\tau] \subseteq \mathcal S_{n,s} \}| = \sum_{n \leq s} 2^s \lambda(\mathcal S_{n,s}) \leq 2^s \cdot 2^d,
$$
so $\lambda([D_s]^{\prec}) \leq 2^{d - k}$. The classes $[D_s]^{\prec}$ increase with $s$, since the classes $\mathcal S_{n,s}$ do. If $X$ belongs to $2^k$ classes $\mathcal S_n$, all these memberships are witnessed at some stage $s$, and then $X \uh s \in D_s$. So $\mathcal V_k = \bigcup_s [D_s]^{\prec}$: it is uniformly $\Sigma^0_1$, and $\lambda(\mathcal V_k) \leq 2^{d-k}$ by continuity. Hence $(\mathcal V_{k+d})_k$ is a Martin-Löf test, and it captures every sequence captured by $(\mathcal S_n)$.
:::

The counting step is Markov's inequality: the average number of classes $\mathcal S_n$ containing a sequence is $\sum_n \lambda(\mathcal S_n)$, so the sequences belonging to $2^k$ of them have measure at most $2^{-k}$ times this sum.

:::quiz[Solovay tests]
In the proof of :ref{#thm-solovay}, why is the constant $d$ not required to be computable from the test?

- [x] Because $d$ is a single number: for a fixed $d$, the sequence $(\mathcal V_{k+d})_k$ is uniformly $\Sigma^0_1$, and its existence is all that is needed.
- [ ] Because the sum $\sum_n \lambda(\mathcal S_n)$ is computable.

  The sum is only left-c.e. in general; the argument does not need its value.
- [ ] Because $d$ is always $0$.

  The sum of the measures may exceed $1$; $d$ compensates for it.

---

Why are the clopen approximations $\mathcal S_{n,s}$ used, rather than the classes $\mathcal S_n$ directly?

- [x] To reduce the measure estimate to a finite count over the strings of length $s$, and to obtain $\mathcal V_k$ as an effective union of clopen classes.
- [ ] Because the classes $\mathcal S_n$ are not measurable.

  Open classes are Borel, hence measurable.
- [ ] To make the classes $\mathcal S_n$ pairwise disjoint.

  They overlap in general; the count handles the overlaps.
:::

## Exercises

::::exercise{difficulty=1}
Let $X$ be Martin-Löf random, and let $f$ be a computable function such that $\sum_n 2^{-f(n)} < \infty$. Show that for almost every $n$, the bits $X(n), X(n+1), \dots, X(n + f(n) - 1)$ are not all $0$. Deduce that a random sequence has no run of zeros of length $2 \log n$ starting at a position $n$, for almost every $n$, where $\log$ is the logarithm in base $2$.

:::solution
Let $\mathcal S_n$ be the clopen class of the sequences $Y$ with $Y(n + i) = 0$ for every $i < f(n)$. It is computable from $n$, and $\lambda(\mathcal S_n) = 2^{-f(n)}$. So $(\mathcal S_n)$ is a Solovay test, and by :ref{#thm-solovay} $X$ belongs to only finitely many $\mathcal S_n$. For the second statement, take $f(n) = \lceil 2 \log n \rceil$ for $n \geq 2$ (and $f(0) = f(1) = 1$): then $2^{-f(n)} \leq n^{-2}$, which is summable.
:::
::::

::::exercise{#ex-kurtz difficulty=2}
A sequence $G$ is **weakly 1-generic** if it meets every dense c.e. set of strings $W$: some prefix of $G$ belongs to $W$. A sequence is **Kurtz random** if it belongs to no null $\Pi^0_1$ class. Show that every Martin-Löf random sequence is Kurtz random, that every weakly 1-generic sequence is Kurtz random, and that no weakly 1-generic sequence is Martin-Löf random.

:::solution
A null $\Pi^0_1$ class $\mathcal P$ is covered by clopen classes $[F_n]^{\prec}$ of measure at most $2^{-n}$, computable from $n$ (second exercise of :ref{to="martin-lof-randomness/measure"}); this is a Martin-Löf test, so random sequences avoid $\mathcal P$.

Let $\mathcal P = [T]$ be null, with $T$ computable. The set $W$ of strings not in $T$ is computable. It is dense: if some $\sigma$ had all its extensions in $T$, then $[\sigma] \subseteq \mathcal P$ and $\lambda(\mathcal P) \geq 2^{-|\sigma|}$. A weakly 1-generic $G$ has a prefix outside $T$, so $G \notin \mathcal P$.

For each $n$, the set $D_n$ of strings $\tau$ of length at least $n$ with at least $\frac{2}{3}|\tau|$ ones is computable and dense: a string $\sigma$ is extended by $\sigma 1^k$ with $k = \max(2|\sigma|, n)$, which has at least $k \geq \frac{2}{3}(|\sigma| + k)$ ones. A weakly 1-generic $G$ meets every $D_n$, so the frequency of ones in $G \uh m$ is at least $\frac{2}{3}$ for infinitely many $m$. By :ref{#prop-large-numbers}, $G$ is not random.
:::
::::

## Notes and references

The law of large numbers for random sequences is the example that motivated Martin-Löf (1966). Normal numbers were introduced by Borel (1909), who proved that almost every real is normal; that Martin-Löf random sequences are normal is folklore. Solovay tests and :ref{#thm-solovay} come from Solovay's unpublished notes of 1975 on Chaitin's work. Kurtz (1981) introduced the randomness notion of the last exercise, which is studied further in the course on notions of randomness. Downey and Hirschfeldt present Solovay tests in Section 6.2 (Definition 6.2.7, Theorem 6.2.8) and Kurtz randomness in Section 7.2; Nies proves the law of large numbers through incompressibility (Proposition 3.2.13), and treats Solovay tests in Proposition 3.2.19 and Kurtz randomness and weak genericity in Section 3.5.

- P. Martin-Löf, *The definition of random sequences*, Information and Control 9 (1966), 602–619.
- W. Hoeffding, *Probability inequalities for sums of bounded random variables*, Journal of the American Statistical Association 58 (1963), 13–30.
- É. Borel, *Les probabilités dénombrables et leurs applications arithmétiques*, Rendiconti del Circolo Matematico di Palermo 27 (1909), 247–271.
- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished notes, 1975.
- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana–Champaign, 1981.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 6.2 and 7.2.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 3.2 and 3.5.
