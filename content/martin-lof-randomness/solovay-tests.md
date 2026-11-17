---
title: Statistical laws and Solovay tests
summary: Random sequences satisfy the law of large numbers and are normal; Solovay tests, with summable measures, define Martin-Löf randomness; Kurtz randomness and weakly 1-generic sequences.
duration: 30
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

::::exercise{#ex-solovay-runs difficulty=1 objective="Use a Solovay test to bound the length of the runs of zeros of a random sequence."}
Let $X$ be Martin-Löf random, and let $f$ be a computable function such that $\sum_n 2^{-f(n)} < \infty$. Show that for almost every $n$, the bits $X(n), X(n+1), \dots, X(n + f(n) - 1)$ are not all $0$. Deduce that a random sequence has no run of zeros of length $2 \log n$ starting at a position $n$, for almost every $n$, where $\log$ is the logarithm in base $2$.

:::solution
Let $\mathcal S_n$ be the clopen class of the sequences $Y$ with $Y(n + i) = 0$ for every $i < f(n)$. It is computable from $n$, and $\lambda(\mathcal S_n) = 2^{-f(n)}$. So $(\mathcal S_n)$ is a Solovay test, and by :ref{#thm-solovay} $X$ belongs to only finitely many $\mathcal S_n$. For the second statement, take $f(n) = \lceil 2 \log n \rceil$ for $n \geq 2$ (and $f(0) = f(1) = 1$): then $2^{-f(n)} \leq n^{-2}$, which is summable.
:::
::::

::::exercise{#ex-kurtz difficulty=2 objective="Compare Martin-Löf randomness, Kurtz randomness and weak 1-genericity."}
A sequence $G$ is **weakly 1-generic** if it meets every dense c.e. set of strings $W$: some prefix of $G$ belongs to $W$. A sequence is **Kurtz random** if it belongs to no null $\Pi^0_1$ class. Show that every Martin-Löf random sequence is Kurtz random, that every weakly 1-generic sequence is Kurtz random, and that no weakly 1-generic sequence is Martin-Löf random.

:::solution
A null $\Pi^0_1$ class $\mathcal P$ is covered by clopen classes $[F_n]^{\prec}$ of measure at most $2^{-n}$, computable from $n$ (:ref{#ex-null-pi01-cover}); this is a Martin-Löf test, so random sequences avoid $\mathcal P$.

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

:::::exercises
::::exercise{#ex-fourth-moment difficulty=2 objective="Prove the law of large numbers with an elementary moment bound and a Solovay test, without Hoeffding's inequality."}
For a string $\sigma$ of length $m \geq 1$, let $S(\sigma) = \sum_{i < m} (2\sigma(i) - 1)$, the number of ones minus the number of zeros.

1. Show that $\sum_{|\sigma| = m} S(\sigma)^4 = 2^m (3m^2 - 2m)$.
2. Deduce that for $\varepsilon > 0$, the number of strings $\sigma$ of length $m$ whose frequency of ones differs from $\frac12$ by more than $\varepsilon$ is less than $2^m \cdot 3 / (16 \varepsilon^4 m^2)$.
3. Deduce :ref{#prop-large-numbers} from :ref{#thm-solovay}.

:::solution
1. Write $y_i(\sigma) = 2\sigma(i) - 1 \in \{ -1, 1 \}$, so that $S(\sigma)^4 = \sum_{i, j, k, l < m} y_i(\sigma) y_j(\sigma) y_k(\sigma) y_l(\sigma)$. Fix a quadruple $(i, j, k, l)$. If some index $a$ occurs an odd number of times in it, the map that flips the bit $a$ is a bijection of $2^m$ that changes the sign of the product, so the sum of the product over $\sigma \in 2^m$ is $0$. Otherwise each index occurs an even number of times, the product is $1$, and the sum is $2^m$. The quadruples of the second kind are those with four equal indices ($m$ of them) and those with two distinct indices occurring twice each: there are $3$ ways to split the four places into two pairs and $m(m-1)$ ordered choices of two distinct indices, giving $3m(m-1)$. The total is $2^m (m + 3m(m-1)) = 2^m(3m^2 - 2m)$.
2. The number of ones in $\sigma$ is $(S(\sigma) + m)/2$, so its frequency differs from $\frac12$ by $|S(\sigma)|/(2m)$. If this exceeds $\varepsilon$, then $S(\sigma)^4 > 16 \varepsilon^4 m^4$. If $N$ strings have this property, then $16 \varepsilon^4 m^4 N < 2^m(3m^2 - 2m) \leq 3 m^2 2^m$ when $N > 0$, and the bound follows.
3. Fix a rational $\varepsilon > 0$, let $C_m$ be the computable set of the strings of length $m$ whose frequency of ones differs from $\frac12$ by more than $\varepsilon$, and $\mathcal S_m = [C_m]^{\prec}$. Then $\lambda(\mathcal S_m) = 2^{-m}|C_m| \leq 3/(16\varepsilon^4 m^2)$, which is summable, so $(\mathcal S_m)$ is a Solovay test. A random $X$ belongs to finitely many $\mathcal S_m$, by :ref{#thm-solovay}: for almost every $m$, the frequency of ones in $X \uh m$ is within $\varepsilon$ of $\frac12$.

Compare Nies 2009, Exercise 3.2.26, which asks for a proof of the law of large numbers with Solovay tests.
:::
::::

::::exercise{#ex-solovay-strings difficulty=1 objective="Reduce Solovay tests to lists of strings with summable weights."}
Show that a sequence $X$ is Martin-Löf random if and only if, for every c.e. set $W \subseteq \nat \times \bstr$ with $\sum_{(i, \sigma) \in W} 2^{-|\sigma|} < \infty$, there are only finitely many pairs $(i, \sigma) \in W$ with $\sigma \prec X$. (The first coordinate allows a string to be listed several times.)

:::solution
($\Rightarrow$) Let $X$ be random and $W$ as in the statement. Fix an enumeration of $W$ without repetitions, and let $\mathcal S_j = [\sigma_j]$ if the $j$-th pair $(i_j, \sigma_j)$ is enumerated, and $\mathcal S_j = \emptyset$ if $W$ has at most $j$ elements. The sequence $(\mathcal S_j)$ is uniformly $\Sigma^0_1$, and $\sum_j \lambda(\mathcal S_j) = \sum_{(i, \sigma) \in W} 2^{-|\sigma|} < \infty$. By :ref{#thm-solovay}, $X$ belongs to finitely many $\mathcal S_j$, that is, $\sigma \prec X$ for finitely many pairs $(i, \sigma) \in W$.

($\Leftarrow$) Suppose that $X$ is not random. By :ref{#thm-solovay}, it is captured by a Solovay test $(\mathcal S_n)$. By :ref{#lem-prefix-free-generator}, applied uniformly in $n$, there are c.e. prefix-free sets $W_n$, uniformly in $n$, with $\mathcal S_n = [W_n]^{\prec}$. Let $W = \{ (n, \sigma) : \sigma \in W_n \}$; it is c.e., and its weight is $\sum_n \lambda(\mathcal S_n) < \infty$. For each of the infinitely many $n$ with $X \in \mathcal S_n$, some $\sigma \in W_n$ is a prefix of $X$, and these pairs $(n, \sigma)$ are distinct.
:::
::::

::::exercise{#ex-many-intersections difficulty=2 objective="Apply the counting argument of Solovay's theorem to finitely many classes of large measure."}
Let $\mathcal C_1, \dots, \mathcal C_N$ be Borel classes with $\lambda(\mathcal C_i) \geq \varepsilon$ for every $i$, and let $k \in \nat$ with $N \varepsilon > k$. Show that there is a set $F \subseteq \{ 1, \dots, N \}$ with $k + 1$ elements such that $\lambda(\bigcap_{i \in F} \mathcal C_i) > 0$. For instance, among five classes of measure at least $\frac12$, three have an intersection of positive measure.

:::solution
For $G \subseteq \{ 1, \dots, N \}$, let $\mathcal A_G$ be the class of the sequences that belong to $\mathcal C_i$ exactly for $i \in G$. The $2^N$ classes $\mathcal A_G$ are Borel, pairwise disjoint, with union $\cs$, so $\sum_G \lambda(\mathcal A_G) = 1$. Each $\mathcal C_i$ is the disjoint union of the classes $\mathcal A_G$ with $i \in G$, so, counting the pairs $(i, G)$ with $i \in G$ in two ways,
$$
\sum_{i = 1}^N \lambda(\mathcal C_i) = \sum_G |G|\, \lambda(\mathcal A_G).
$$
If $\lambda(\mathcal A_G) = 0$ for every $G$ with $|G| \geq k + 1$, the right-hand side is at most $k \sum_G \lambda(\mathcal A_G) = k$, whereas the left-hand side is at least $N\varepsilon > k$. So some $G$ with at least $k + 1$ elements has $\lambda(\mathcal A_G) > 0$. Any $F \subseteq G$ with $k + 1$ elements works, since $\mathcal A_G \subseteq \bigcap_{i \in F} \mathcal C_i$. In the example, $N = 5$, $\varepsilon = \frac12$ and $k = 2$.

This is the counting step of :ref{#thm-solovay}, or Markov's inequality, for the number of classes containing a sequence. Adapted from Nies 2009, Exercise 1.9.15.
:::
::::

::::exercise{#ex-normal-offsets difficulty=1 objective="Complete the passage from block frequencies to the frequency of occurrences at all positions in the proof of normality."}
Let $X$ be a sequence and $\tau$ a string of length $k \geq 1$. For $r < k$ and $N \in \nat$, let $a_r(N)$ be the number of $i < N$ such that $X(ik + r) \cdots X(ik + r + k - 1) = \tau$, and suppose that $a_r(N)/N$ tends to $2^{-k}$ for every $r < k$. Let $b(m)$ be the number of positions $j < m$ such that $X(j) \cdots X(j + k - 1) = \tau$. Show that $b(m)/m$ tends to $2^{-k}$.

:::solution
Every $j$ is written uniquely as $j = ik + r$ with $r < k$. For $m > r$, the number of $i$ with $ik + r < m$ is $N_r(m) = \lceil (m - r)/k \rceil$, so
$$
b(m) = \sum_{r < k} a_r(N_r(m)), \qquad \frac{b(m)}{m} = \sum_{r < k} \frac{a_r(N_r(m))}{N_r(m)} \cdot \frac{N_r(m)}{m}
$$
for $m \geq k$. Since $m/k - 1 \leq N_r(m) \leq m/k + 1$, $N_r(m)$ tends to infinity and $N_r(m)/m$ tends to $1/k$. So each of the $k$ terms tends to $2^{-k}/k$, and $b(m)/m$ tends to $2^{-k}$.
:::
::::
:::::
