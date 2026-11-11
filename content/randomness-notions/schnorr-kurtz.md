---
title: Schnorr and Kurtz randomness
summary: Kurtz randomness, avoiding null Π⁰₁ classes, and Schnorr randomness, passing Martin-Löf tests of computable measure; the implications between the notions; weakly 1-generic sets are Kurtz random but not Schnorr random; in computably dominated degrees, Kurtz randomness implies Martin-Löf randomness.
duration: 30
prerequisites: [weak-2-randomness, immunity-growth/immune-sets]
---

Martin-Löf randomness requires the measures of the components of a test to be bounded by $2^{-n}$, but not to be known. Schnorr argued that a test whose measures cannot be computed is not fully effective, and proposed to require them to be computable. Weakening further, Kurtz considered the null classes that are closed and effectively given. This lesson compares these notions with Martin-Löf randomness, and shows that they collapse on computably dominated sequences.

## Definitions

:::definition{#def-schnorr-kurtz}
1. A sequence is **Kurtz random**, or **weakly random**, if it belongs to no null $\Pi^0_1$ class.
2. A **Schnorr test** is a Martin-Löf test $(\mathcal U_n)$ such that the reals $\lambda(\mathcal U_n)$ are computable, uniformly in $n$. A sequence is **Schnorr random** if it passes every Schnorr test.
:::

:::proposition{#prop-notions-implications}
Every weakly 2-random sequence is Martin-Löf random; every Martin-Löf random sequence is Schnorr random; every Schnorr random sequence is Kurtz random.
:::

:::proof{of=prop-notions-implications}
The first implication is :ref{#prop-weak-2-position} (1), and the second holds since Schnorr tests are Martin-Löf tests. For the third, let $\mathcal P = [T]$ be a null $\Pi^0_1$ class, with $T$ computable. By the second exercise of :ref{to="martin-lof-randomness/measure"}, there are finite sets $F_n$, computable from $n$, with $\mathcal P \subseteq [F_n]^{\prec}$ and $\lambda([F_n]^{\prec}) \leq 2^{-n}$. The measures of these clopen classes are rationals computed from $F_n$, so $([F_n]^{\prec})$ is a Schnorr test, and it captures every member of $\mathcal P$.
:::

The law of large numbers holds for Schnorr random sequences. The proof of :ref{#prop-large-numbers} uses, for a fixed rational $\varepsilon > 0$, the classes $\mathcal V_n = \bigcup_{m > n} [C_m]^{\prec}$, and the number $a = e^{-2\varepsilon^2} < 1$. Their measures are computable: the measure of the clopen class $\bigcup_{n < m \leq M} [C_m]^{\prec}$ is a rational computable from $n$ and $M$, and it differs from $\lambda(\mathcal V_n)$ by at most the tail $\sum_{m > M} 2^{-m} |C_m| \leq 2a^{M+1}/(1-a)$, which tends to $0$ computably. The subsequence $(\mathcal V_{m_n})_n$ built in :ref{#lem-test-bound} is then a Schnorr test, and it captures every sequence whose frequencies of ones deviate from $\frac12$ by more than $\varepsilon$ infinitely often. Kurtz random sequences need not satisfy it.

:::proposition{#prop-generic-kurtz}
Every weakly 1-generic sequence is Kurtz random, and no weakly 1-generic sequence is Schnorr random.
:::

:::proof{of=prop-generic-kurtz}
The first statement is the third exercise of :ref{to="martin-lof-randomness/martin-lof-tests"}. For the second, a weakly 1-generic sequence has frequencies of ones at least $\frac{2}{3}$ at infinitely many lengths, by the same exercise, so it fails the law of large numbers, hence a Schnorr test.
:::

The other implications are strict as well. A Schnorr random sequence need not be Martin-Löf random: Nies, Stephan and Terwijn (2005) showed that every high degree contains a Schnorr random sequence that is not Martin-Löf random, and that conversely a Schnorr random sequence that is not high is Martin-Löf random. These results are admitted.

## Collapse in computably dominated degrees

:::theorem[Nies, Stephan, Terwijn]{#thm-kurtz-ml-dominated}
If $Z$ is computably dominated and Kurtz random, then $Z$ is Martin-Löf random.
:::

:::proof{of=thm-kurtz-ml-dominated}
Suppose that $Z$ is captured by a Martin-Löf test $(\mathcal U_n)$; we show that $Z$ lies in a null $\Pi^0_1$ class. Let $\mathcal U_{n,s}$ be the clopen approximation of $\mathcal U_n$ at stage $s$, with $\mathcal U_n = \bigcup_s \mathcal U_{n,s}$. Let $f(n)$ be the least $s$ with $Z \in \mathcal U_{n,s}$; it exists since $Z \in \mathcal U_n$, and $f$ is computable in $Z$. Since $Z$ is computably dominated, there is a computable function $g$ and a number $N$ with $f(n) \leq g(n)$ for all $n \geq N$. Then $Z \in \mathcal U_{n, g(n)}$ for every $n \geq N$, so $Z$ belongs to
$$
\mathcal P = \bigcap_{n \geq N} \mathcal U_{n, g(n)}.
$$
Each $\mathcal U_{n, g(n)}$ is a clopen class computable uniformly in $n$, so $\mathcal P$ is a $\Pi^0_1$ class, and $\lambda(\mathcal P) \leq \lambda(\mathcal U_n) \leq 2^{-n}$ for every $n \geq N$, so $\mathcal P$ is null. Hence $Z$ is not Kurtz random.
:::

The proof converts the time at which $Z$ enters each component into a computable bound; once the stages are bounded, the test becomes a closed null class. For computably dominated sequences, Kurtz, Schnorr and Martin-Löf randomness therefore coincide.

:::quiz[the collapse theorem]
In the proof of :ref{#thm-kurtz-ml-dominated}, why is the class $\mathcal P$ closed, while $\bigcap_n \mathcal U_n$ is only $\Pi^0_2$?

- [x] Because each component is replaced by a finite stage of its enumeration, a clopen class computable uniformly in $n$, and an effective intersection of clopen classes is $\Pi^0_1$.
- [ ] Because $\mathcal U_n$ is decreasing.

  The test need not be decreasing; the closedness comes from the finite stages.
- [ ] Because $Z$ is computably dominated.

  Domination makes $Z$ belong to $\mathcal P$; the closedness of $\mathcal P$ comes from the computability of $g$.

---

Where is the computable domination of $Z$ used?

- [x] To bound the $Z$-computable function $f$, giving the entry stages, by a computable $g$, so that the bounded stages define a computable sequence of clopen classes containing $Z$.
- [ ] To show that $\mathcal P$ is null.

  Nullness follows from the bounds $\lambda(\mathcal U_n) \leq 2^{-n}$.
- [ ] To show that $f$ is total.

  $f$ is total since $Z$ belongs to every $\mathcal U_n$.
:::

## Exercises

::::exercise{difficulty=1}
Show that every computably dominated Martin-Löf random sequence is weakly 2-random, and that no computably dominated sequence is 2-random.

:::solution
A computably dominated random sequence computes no non-computable c.e. set, as shown in the second exercise of :ref{to="randomness-notions/weak-2-randomness"}, so it is weakly 2-random by :ref{#thm-dnwy}. By Kurtz's theorem, admitted in :ref{to="randomness-notions/relative-randomness"}, 2-random sequences have hyperimmune degree, so they are not computably dominated.
:::
::::

::::exercise{difficulty=2}
Show that there is a Kurtz random sequence computable in $\emptyset'$ that is not Martin-Löf random.

:::solution
By :ref{#prop-1-generic}, there is a 1-generic set $G \leq_T \emptyset'$. It is weakly 1-generic, since a dense set of strings has no string without an extension in it, hence Kurtz random by :ref{#prop-generic-kurtz}, and not Schnorr random, hence not Martin-Löf random.
:::
::::

## Notes and references

Schnorr (1971) introduced his notion in a critique of Martin-Löf's definition, and characterized it by martingales with computable rates of success. Kurtz (1981) introduced weak randomness. Nies, Stephan and Terwijn (2005) proved the collapse in computably dominated (hyperimmune-free) degrees and the relation with highness. Downey and Hirschfeldt's book contains the full hierarchy, including computable randomness, defined by computable martingales.

- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois, 1981.
- C.-P. Schnorr, *Zufälligkeit und Wahrscheinlichkeit*, Lecture Notes in Mathematics 218, Springer, 1971.
- A. Nies, F. Stephan and S. A. Terwijn, *Randomness, relativization and Turing degrees*, Journal of Symbolic Logic 70 (2005), 515–535.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Chapter 7.
