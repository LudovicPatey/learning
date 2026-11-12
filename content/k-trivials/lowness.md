---
title: Lowness for randomness
summary: Relativized prefix-free complexity and randomness; sets that are low for K, low for Martin-Löf randomness, and bases for randomness; the implications between these notions and K-triviality; sets that are low for K are low.
duration: 30
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

::::exercise{difficulty=2}
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

Lowness for Martin-Löf randomness was introduced by Zambella (1990), who asked whether a non-computable set has this property; Kučera and Terwijn (1999) built a non-computable c.e. set that is low for randomness. Lowness for K is due to Muchnik (unpublished, around 1999), who built a non-computable c.e. set low for K. Bases for randomness were introduced by Kučera (1993). Nies (Proposition 5.1.2) shows that sets that are low for K are generalized low, $A' \leq_T A \oplus \emptyset'$, in a uniform way; with :ref{#cor-k-trivial-delta2}, this gives the exercise.

The lowness notions and the implications between them are in Nies, *Computability and Randomness*, Section 5.1 (Definitions 5.1.1, 5.1.7 and 5.1.18, Fact 5.1.8, Proposition 5.2.3), and in Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Sections 11.2 and 11.7 (Definitions 11.2.1, 11.2.3 and 11.7.1).

- D. Zambella, *On sequences with simple initial segments*, ILLC Technical Report ML-1990-05, University of Amsterdam, 1990.
- A. Kučera, *On relative randomness*, Annals of Pure and Applied Logic 63 (1993), 61–67.
- A. Kučera and S. A. Terwijn, *Lowness for the class of random sets*, Journal of Symbolic Logic 64 (1999), 1396–1402.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 5.1.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 11.2 and 11.7.
