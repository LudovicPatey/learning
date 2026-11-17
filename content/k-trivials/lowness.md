---
title: Lowness for randomness
summary: Relativized prefix-free complexity and randomness; sets that are low for K, low for Martin-Löf randomness, and bases for randomness; the implications between these notions and K-triviality; sets that are low for K are low.
duration: 20
prerequisites: [k-trivial-sets, martin-lof-randomness/randomness-and-degrees]
---

An oracle $A$ can be used to compress strings and to test sequences for randomness. A set is **low** for a relativizable notion if, used as an oracle, it does not change the notion, as a low set in the usual sense does not change the halting problem up to Turing equivalence. For prefix-free complexity and Martin-Löf randomness, the low sets are exactly the K-trivial sets. This lesson introduces three lowness notions and proves the easy implications between them and K-triviality. The next lesson proves that the three notions are equivalent, by the hungry sets argument of Hirschfeldt, Nies and Stephan, and the last lesson discusses the converse implication from K-triviality, the central theorem of the subject.

The three notions express weakness in different ways. Lowness for K and lowness for randomness say that $A$ is useless as an oracle for compressing strings or for detecting patterns in sequences. Being a base for randomness says that $A$ is computed by many oracles, in a sense that $A$ itself can measure. The hungry sets argument of the next lesson converts the third kind of weakness into the first.

## Relativized complexity and randomness

An **oracle prefix-free machine** is an oracle machine $M$ such that, for every oracle $X$, the domain of $M^X$ is prefix-free. The constructions of :ref{to="kolmogorov-complexity/prefix-free-complexity"} relativize uniformly: there is an oracle prefix-free machine $U$ such that, for every oracle prefix-free machine $M$, there is $c$ with $K_{U^X} \leq K_{M^X} + c$ for every oracle $X$. We write $K^A = K_{U^A}$, and $\mathrm{MLR}^A$ for the class of sequences passing every Martin-Löf test relative to $A$, the tests whose components are uniformly $\Sigma^0_1(A)$. The results of the course on Martin-Löf randomness relativize, by the same proofs; in particular $Z \in \mathrm{MLR}^A$ if and only if $K^A(Z \uh n) \geq n - O(1)$, and $\sum_{\tau \in \dom U^A} 2^{-|\tau|} \leq 1$.

If $B \leq_T A$, then $K^A \leq^+ K^B$, since a machine with oracle $A$ can simulate $U^B$; in particular $K^A \leq^+ K$. So oracles can only make complexity smaller and randomness harder.

For a string $\rho$, we write $U^\rho(\tau)\converge = x$ when the computation of $U$ on input $\tau$ with oracle $\rho$ halts with output $x$ and its use is exactly $|\rho|$, in the sense of :ref{#def-use}. The set of triples $(\rho, \tau, x)$ with $U^\rho(\tau)\converge = x$ is c.e., and for every oracle $X$ and every $\tau \in \dom U^X$, there is exactly one $\rho \prec X$ with $U^\rho(\tau)\converge$, namely $X \uh u$ for the use $u$ of the computation.

## Three lowness notions

:::definition{#def-lowness-randomness}
Let $A$ be a set.

1. $A$ is **low for K** if $K(\sigma) \leq^+ K^A(\sigma)$ for every string $\sigma$.
2. $A$ is **low for Martin-Löf randomness** if $\mathrm{MLR}^A = \mathrm{MLR}$.
3. $A$ is a **base for randomness** if $A \leq_T Z$ for some $Z \in \mathrm{MLR}^A$.
:::

Every computable set has the three properties. For a non-computable set $A$, the sequences computing $A$ form a null class (:ref{#thm-sacks}); a base for randomness is a set computed by some sequence that is nevertheless random relative to $A$. In other words, $A$ cannot cover the null class of the sequences that compute it by a Martin-Löf test relative to $A$.

:::example{#ex-lowness}
The halting set $\emptyset'$ has none of the three properties. Let $\omega$ be the binary expansion of $\Omega$, which is computable in $\emptyset'$ (:ref{#thm-omega}). With oracle $\emptyset'$, the prefix $\omega \uh n$ is computed from $n$, so $K^{\emptyset'}(\omega \uh n) \leq^+ K^{\emptyset'}(n) \leq^+ 2 \log n$, whereas $K(\omega \uh n) \geq n - O(1)$. So $\emptyset'$ is not low for K, and $\omega$ is random but not random relative to $\emptyset'$, by the relativized Levin–Schnorr theorem: $\emptyset'$ is not low for randomness. By the hungry sets theorem of the next lesson, $\emptyset'$ is not a base for randomness either. The same argument applies to every set that computes $\Omega$, that is, to every Turing complete set.
:::

:::proposition{#prop-lowness-implications}
1. If $A$ is low for K, then $A$ is K-trivial.
2. If $A$ is low for K, then $A$ is low for Martin-Löf randomness.
3. If $A$ is low for Martin-Löf randomness, then $A$ is a base for randomness.
4. The sets that are low for K are closed downward under $\leq_T$.
:::

:::proof{of=prop-lowness-implications}
1. With oracle $A$, the string $A \uh n$ is computed from $n$, so $K^A(A \uh n) \leq^+ K^A(n) \leq^+ K(n)$. If $A$ is low for K, then $K(A \uh n) \leq^+ K^A(A \uh n) \leq^+ K(n)$.
2. $\mathrm{MLR}^A \subseteq \mathrm{MLR}$ for every $A$, since a test without oracle is a test relative to $A$. Conversely, let $Z \in \mathrm{MLR}$, so that $K(Z \uh n) \geq n - c$. If $A$ is low for K, then $K^A(Z \uh n) \geq K(Z \uh n) - d \geq n - c - d$, and $Z \in \mathrm{MLR}^A$ by the relativized Levin–Schnorr theorem.
3. By the Kučera–Gács theorem (:ref{#thm-kucera-gacs}), some $Z \in \mathrm{MLR}$ computes $A$, and $\mathrm{MLR} = \mathrm{MLR}^A$.
4. If $B \leq_T A$ and $A$ is low for K, then $K \leq^+ K^A \leq^+ K^B$.
:::

:::quiz[the implications between lowness notions]
In the proof of :ref{#prop-lowness-implications} (2), where is it used that $A$ is low for K?

- [x] To transfer the bound $K(Z \uh n) \geq n - c$ to $K^A(Z \uh n) \geq n - c - d$, which gives $Z \in \mathrm{MLR}^A$ by the relativized Levin–Schnorr theorem.
- [ ] To show that $\mathrm{MLR}^A \subseteq \mathrm{MLR}$.

  This inclusion holds for every oracle $A$, since a test without oracle is a test relative to $A$.
- [ ] To find a random sequence that computes $A$.

  This is the step of (3), given by the Kučera–Gács theorem for every set.

---

In the proof of (3), why is the Kučera–Gács theorem needed?

- [x] It provides a random sequence $Z$ that computes $A$; since $A$ is low for randomness, $Z$ is random relative to $A$.
- [ ] Because $A$ is $\Delta^0_2$.

  The Kučera–Gács theorem applies to every set, and (3) does not use that $A$ is $\Delta^0_2$.
- [ ] Because the random sequences form a class of measure $1$.

  If $A$ is not computable, the sequences that compute $A$ form a null class, so measure alone does not give a random sequence computing $A$.
:::

Implications (2) and (3) only relativize known results. A base for randomness is computed by a sequence that is random relative to it, and the next lesson shows that this weak form of lowness already implies lowness for K. The converse of (1), that every K-trivial set is low for K, is discussed in the last lesson.

## Exercises

::::exercise{#ex-lowk-low difficulty=2 objective="Combine lowness for K with the use principle to show that the jump of a set low for K is computable in $\emptyset'$."}
Show that every set that is low for K is low, that is, $A' \leq_T \emptyset'$.

:::hint
For $e \in A'$, the use of the computation $\Phi^A_e(e)$ gives a prefix of $A$ with a short description relative to $A$.
:::

:::solution
Let $A$ be low for K; it is K-trivial, hence $\Delta^0_2$. Let $g$ be the partial $A$-computable function with $g(e) = A \uh u$ when $\Phi^A_e(e)\converge$ with use $u$. Then $K^A(g(e)) \leq^+ K^A(e) \leq^+ K(e)$ for $e \in A'$, since $g$ is computable in $A$. By :ref{#prop-k-basic} (2), $K(e) \leq^+ 2 \lfloor \log(e+1) \rfloor$. Since $A$ is low for K, there is $c$ with $K(g(e)) \leq h(e)$ for every $e \in A'$, where $h(e) = 2 \lfloor \log(e+1) \rfloor + c$ is computable.

With oracle $\emptyset'$, decide $e \in A'$ as follows: for each string $\sigma$ of length at most $h(e)$, decide whether $U(\sigma)$ converges; if it does, with output $\rho$, decide whether $\rho \prec A$, which is possible since $A \leq_T \emptyset'$, and whether $\Phi^\rho_e(e)\converge$, a $\Sigma^0_1$ question. Answer yes if some $\sigma$ passes all three tests. If $e \in A'$, then a shortest description of $g(e)$ passes them. Conversely, if $\rho \prec A$ and $\Phi^\rho_e(e)\converge$, then $\Phi^A_e(e)\converge$ by the use principle. So $A' \leq_T \emptyset'$.
:::
::::

## Notes and references

Lowness for Martin-Löf randomness was introduced by Zambella (1990), who asked whether a non-computable set has this property; Kučera and Terwijn (1999) built a non-computable c.e. set that is low for randomness. Lowness for K is due to Muchnik (unpublished, around 1999), who built a non-computable c.e. set low for K. Bases for randomness were introduced by Kučera (1993). Nies (Proposition 5.1.2) shows that sets that are low for K are generalized low, $A' \leq_T A \oplus \emptyset'$, in a uniform way; with :ref{#cor-k-trivial-delta2}, this gives :ref{#ex-lowk-low}.

The lowness notions and the implications between them are in Nies, *Computability and Randomness*, Section 5.1 (Definitions 5.1.1, 5.1.7 and 5.1.18, Fact 5.1.8, Proposition 5.2.3), and in Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Sections 11.2 and 11.7 (Definitions 11.2.1, 11.2.3 and 11.7.1).

- D. Zambella, *On sequences with simple initial segments*, ILLC Technical Report ML-1990-05, University of Amsterdam, 1990.
- A. Kučera, *On relative randomness*, Annals of Pure and Applied Logic 63 (1993), 61–67.
- A. Kučera and S. A. Terwijn, *Lowness for the class of random sets*, Journal of Symbolic Logic 64 (1999), 1396–1402.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 5.1.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 11.2 and 11.7.

:::::exercises
::::exercise{#ex-random-not-low difficulty=1 objective="Check on random sets that the oracle of a lowness notion must not be able to compress itself."}
Show that no Martin-Löf random set is low for K, and that no Martin-Löf random set is low for Martin-Löf randomness.

:::solution
Let $Z$ be random. With oracle $Z$, the prefix $Z \uh n$ is computed from $n$, so $K^Z(Z \uh n) \leq^+ K^Z(n) \leq^+ K(n) \leq^+ 2 \log n$ for $n \geq 2$, by :ref{#prop-k-basic} (2). By the Levin–Schnorr theorem, $K(Z \uh n) \geq n - O(1)$. So $K(Z \uh n) - K^Z(Z \uh n)$ is unbounded, and $Z$ is not low for K. Moreover $K^Z(Z \uh n) - n$ is not bounded from below, so $Z \notin \mathrm{MLR}^Z$ by the relativized Levin–Schnorr theorem, while $Z \in \mathrm{MLR}$: $Z$ is not low for Martin-Löf randomness. The case of bases for randomness is treated after the hungry sets theorem.
:::
::::

::::exercise{#ex-lowness-downward difficulty=1 objective="Check that lowness for randomness and being a base for randomness are closed downward under Turing reducibility."}
Let $A \leq_T B$. Show that if $B$ is low for Martin-Löf randomness, then so is $A$, and that if $B$ is a base for randomness, then so is $A$.

:::solution
A Martin-Löf test relative to $A$ is a test relative to $B$, since a uniformly $\Sigma^0_1(A)$ sequence of classes is uniformly $\Sigma^0_1(B)$ when $A \leq_T B$. So $\mathrm{MLR}^B \subseteq \mathrm{MLR}^A \subseteq \mathrm{MLR}$. If $\mathrm{MLR}^B = \mathrm{MLR}$, then $\mathrm{MLR}^A = \mathrm{MLR}$. If $B \leq_T Z$ with $Z \in \mathrm{MLR}^B$, then $A \leq_T Z$ and $Z \in \mathrm{MLR}^A$.
:::
::::

::::exercise[Lowness for plain complexity]{#ex-low-for-c difficulty=1 objective="Show with Chaitin's theorem that the analogue of lowness for K with plain complexity holds only for computable sets."}
Let $C^A$ be plain complexity relative to $A$, defined from an optimal oracle machine as $K^A$ is. Say that $A$ is **low for C** if $C(\sigma) \leq^+ C^A(\sigma)$ for every string $\sigma$. Show that every set that is low for C is computable.

:::solution
With oracle $A$, the string $A \uh n$ is computed from $n$, so $C^A(A \uh n) \leq^+ C^A(n)$, and $C^A(n) \leq^+ C(n)$, since a machine with oracle $A$ can ignore its oracle. If $A$ is low for C, then $C(A \uh n) \leq^+ C^A(A \uh n) \leq^+ C(n)$. By :ref{#thm-chaitin-computable}, $A$ is computable. The same argument with $K$ gives :ref{#prop-lowness-implications} (1); the difference is that K-triviality, unlike its analogue for $C$, does not imply computability. (Adapted from Nies 2009, Exercise 5.2.22.)
:::
::::

::::exercise[Few sets for each constant]{#ex-lowk-few difficulty=2 objective="Use the uniformity of the relativized optimal machine to bound the number of sets that are low for K with a given constant."}
Say that $A$ is low for K **with constant** $c$ if $K(\sigma) \leq K^A(\sigma) + c$ for every $\sigma$. Show that there is a constant $d$ such that, for every $c$, every set that is low for K with constant $c$ is K-trivial with constant $c + d$. Deduce that only finitely many sets are low for K with constant $c$.

:::solution
Let $M$ be the oracle machine that, with oracle $X$ and input $\tau$, computes $n = U^X(\tau)$ and outputs $X \uh n$, and $N$ the oracle machine that ignores its oracle and behaves as $U$. For every oracle $X$, the domains of $M^X$ and $N^X$ are those of $U^X$ and $U$, which are prefix-free. By the optimality of $U$ among oracle prefix-free machines, there are $d_1$ and $d_2$, independent of $X$, with $K^X(X \uh n) \leq K^X(n) + d_1$ and $K^X(n) \leq K(n) + d_2$ for every $X$ and $n$.

If $A$ is low for K with constant $c$, then for every $n$
$$
K(A \uh n) \leq K^A(A \uh n) + c \leq K^A(n) + c + d_1 \leq K(n) + c + d_1 + d_2,
$$
so $d = d_1 + d_2$ works. By :ref{#cor-k-trivial-delta2}, fewer than $2^{c + d + c'}$ sets are K-trivial with constant $c + d$, where $c'$ is the constant of :ref{#thm-k-trivial-count}; so fewer than $2^{c + d + c'}$ sets are low for K with constant $c$.
:::
::::

::::exercise[Sets low for K compute no DNC function]{#ex-lowk-not-dnc difficulty=2 objective="Combine lowness for K with the characterization of DNC degrees by complex functions."}
Admit the theorem of Kjos-Hanssen, Merkle and Stephan, proved in the course on Martin-Löf randomness: a set $X$ computes a diagonally non-computable function if and only if $X$ computes a function $f : \nat \to \bstr$ with $K(f(n)) \geq n$ for every $n$. Show that no set that is low for K computes a diagonally non-computable function. Deduce that no set that is low for K computes a Martin-Löf random set.

:::solution
Let $A$ be low for K, and let $f \leq_T A$ be a function from $\nat$ to strings. With oracle $A$, $f(n)$ is computed from $n$, so $K^A(f(n)) \leq^+ K^A(n) \leq^+ K(n) \leq^+ 2 \log n$ for $n \geq 2$. Since $A$ is low for K, $K(f(n)) \leq^+ K^A(f(n)) \leq^+ 2 \log n$, which is less than $n$ for all large $n$. So $A$ computes no function $f$ with $K(f(n)) \geq n$ for every $n$, and by the theorem, no diagonally non-computable function.

If $A$ computed a random set $Z$, let $c$ be such that $K(Z \uh m) \geq m - c$ for every $m$ (Levin–Schnorr). The function $f(n) = Z \uh (n + c)$ is computable in $Z$, hence in $A$, and $K(f(n)) \geq n$ for every $n$, contradicting the first part. This agrees with :ref{#prop-lowness-implications} (4) and :ref{#ex-random-not-low}: a set computed by a set low for K is low for K, and a random set is not.
:::
::::
:::::
