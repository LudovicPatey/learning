---
title: Relative randomness and van Lambalgen's theorem
summary: Martin-Löf randomness relative to an oracle; van Lambalgen's theorem that a join is random exactly when its halves are random, the second relative to the first; consequences for the Turing degrees of random sequences; 2-randomness.
duration: 35
prerequisites: [martin-lof-randomness/levin-schnorr]
---

Randomness relative to an oracle $X$ asks a sequence to pass all tests that $X$ can enumerate. The stronger the oracle, the fewer random sequences. Van Lambalgen's theorem describes how relative randomness interacts with the join: a sequence $A \oplus B$ is random if and only if $A$ is random and $B$ is random relative to $A$. The theorem has strong consequences for the degrees of random sequences, and it shows that randomness relative to $\emptyset'$, called 2-randomness, behaves well.

## Relative randomness

:::definition{#def-relative-ml}
Let $X$ be a set. A **Martin-Löf test relative to $X$** is a sequence of classes $(\mathcal U_n)$, uniformly $\Sigma^0_1(X)$, with $\lambda(\mathcal U_n) \leq 2^{-n}$. A sequence is **Martin-Löf random relative to $X$**, or **$X$-random**, if it passes every such test. The class of $X$-random sequences is written $\mathrm{MLR}^X$. A sequence is **$n$-random** if it is random relative to $\emptyset^{(n-1)}$.
:::

All results of the course on Martin-Löf randomness relativize: there is a universal test relative to $X$, $\mathrm{MLR}^X$ is conull, and $Z \in \mathrm{MLR}^X$ if and only if $K^X(Z \uh n) \geq n - O(1)$, where $K^X$ is prefix-free complexity relative to $X$. If $Y \leq_T X$, every test relative to $Y$ is a test relative to $X$, so $\mathrm{MLR}^X \subseteq \mathrm{MLR}^Y$.

Two facts of measure theory are used below. They concern a class $\mathcal W \subseteq \cs$ seen as a class of pairs, through the identification of $X \oplus Y$ with $(X, Y)$, and its sections $\mathcal W_X = \{ Y : X \oplus Y \in \mathcal W \}$.

:::fact[Fubini]{#fact-fubini}
For every open class $\mathcal W$, the function $X \mapsto \lambda(\mathcal W_X)$ is measurable and $\lambda(\mathcal W) = \int \lambda(\mathcal W_X)\, dX$. In particular, for every $q > 0$, $\lambda(\{ X : \lambda(\mathcal W_X) > q \}) \leq \lambda(\mathcal W) / q$.
:::

This is Fubini's theorem for the product of two copies of the uniform measure, which is the uniform measure under the identification; the second statement is Markov's inequality. Both are admitted. Note that if $\mathcal W$ is $\Sigma^0_1$, then $\mathcal W_X$ is $\Sigma^0_1(X)$ uniformly in $X$, and $\{ X : \lambda(\mathcal W_X) > q \}$ is $\Sigma^0_1$, uniformly in a rational $q$, since $\lambda(\mathcal W_X)$ is left-c.e. relative to $X$, uniformly.

Every oracle-dependent sequence of classes can be trimmed into a test for every oracle, as in the construction of the universal test (:ref{#thm-universal-test}): from an oracle machine enumerating $\mathcal V^X_n$, one computes another enumerating $\widehat{\mathcal V}^X_n \subseteq \mathcal V^X_n$, with $\lambda(\widehat{\mathcal V}^X_n) \leq 2^{-n}$ for every $X$, and $\widehat{\mathcal V}^X_n = \mathcal V^X_n$ whenever $\lambda(\mathcal V^X_n) \leq 2^{-n}$.

## Van Lambalgen's theorem

:::theorem[van Lambalgen]{#thm-van-lambalgen}
For all sets $A$ and $B$, $A \oplus B$ is Martin-Löf random if and only if $A$ is Martin-Löf random and $B$ is Martin-Löf random relative to $A$.
:::

:::proof{of=thm-van-lambalgen}
($\Rightarrow$) Suppose $A$ is captured by a test $(\mathcal U_n)$. Then $A \oplus B$ belongs to the classes $\{ X \oplus Y : X \in \mathcal U_n \}$, which are uniformly $\Sigma^0_1$ with the same measures; so $A \oplus B$ is not random. Suppose $B$ is captured by a test relative to $A$; by trimming, we may assume it is given by an oracle machine $X \mapsto (\mathcal V^X_n)$ with $\lambda(\mathcal V^X_n) \leq 2^{-n}$ for every $X$. Let $\mathcal W_n = \{ X \oplus Y : Y \in \mathcal V^X_n \}$, uniformly $\Sigma^0_1$. By :ref{#fact-fubini}, $\lambda(\mathcal W_n) = \int \lambda(\mathcal V^X_n)\, dX \leq 2^{-n}$, and $A \oplus B \in \bigcap_n \mathcal W_n$.

($\Leftarrow$) Suppose $A \oplus B \in \bigcap_n \mathcal U_n$ for a Martin-Löf test $(\mathcal U_n)$, and $A$ random. For each $n$, let $\mathcal V^X_n = (\mathcal U_{2n})_X = \{ Y : X \oplus Y \in \mathcal U_{2n} \}$, and $\mathcal S_n = \{ X : \lambda(\mathcal V^X_n) > 2^{-n} \}$. The classes $\mathcal S_n$ are uniformly $\Sigma^0_1$, and $\lambda(\mathcal S_n) \leq 2^{-2n} / 2^{-n} = 2^{-n}$ by :ref{#fact-fubini}. So $(\mathcal S_n)$ is a Solovay test, and since $A$ is random, $A \notin \mathcal S_n$ for all $n \geq N$, for some $N$ (:ref{#thm-solovay}). For $n \geq N$, $\lambda(\mathcal V^A_n) \leq 2^{-n}$, so $(\mathcal V^A_{n+N})_n$ is a Martin-Löf test relative to $A$. It captures $B$, since $A \oplus B \in \mathcal U_{2n}$ for every $n$. So $B$ is not random relative to $A$.
:::

The theorem is symmetric in a non-obvious way: $A \oplus B$ is random if and only if $B \oplus A$ is, so $A$ is random and $B$ is $A$-random if and only if $B$ is random and $A$ is $B$-random. Random sequences are **mutually random** in this sense.

:::quiz[van Lambalgen's theorem]
In the direction ($\Leftarrow$) of :ref{#thm-van-lambalgen}, why is the randomness of $A$ needed?

- [x] To exclude the oracles $X$ for which the sections $\mathcal V^X_n$ are too large: these oracles form a Solovay test, which $A$ passes, so for large $n$ the sections at $A$ have the measure required by a test.
- [ ] To make the classes $\mathcal V^A_n$ uniformly $\Sigma^0_1(A)$.

  They are uniformly $\Sigma^0_1(A)$ for every $A$; the issue is their measure.
- [ ] To show that $B$ is random.

  The conclusion is that $B$ is not random relative to $A$; the randomness of $A$ is a hypothesis of the contrapositive.

---

Why is $\mathcal U_{2n}$ used to define $\mathcal V^X_n$, rather than $\mathcal U_n$?

- [x] So that Markov's inequality gives $\lambda(\mathcal S_n) \leq 2^{-2n} / 2^{-n} = 2^{-n}$, a summable bound; with $\mathcal U_n$, the bound would be $1$.
- [ ] Because $\mathcal U_n$ might not contain $A \oplus B$.

  $A \oplus B$ belongs to every component.
- [ ] To make the test decreasing.

  Monotonicity is not used.
:::

:::corollary{#cor-van-lambalgen}
1. If $A \oplus B$ is random, then $A$ and $B$ are Turing incomparable.
2. A sequence $A$ is 2-random if and only if $A \oplus \Omega$ is random, where $\Omega$ is Chaitin's halting probability. In particular, no 2-random sequence computes $\emptyset'$.
:::

:::proof{of=cor-van-lambalgen}
1. If $B \leq_T A$, then $B$ is not random relative to $A$: the classes $[B \uh n]$ form a test relative to $A$. By the theorem, $A \oplus B$ is not random. If $A \leq_T B$, apply the same argument to $B \oplus A$, which is random as the image of $A \oplus B$ under the computable measure-preserving map exchanging even and odd positions.
2. Since $\Omega \equiv_T \emptyset'$ (:ref{#thm-omega}), randomness relative to $\Omega$ is randomness relative to $\emptyset'$. By the theorem applied to $\Omega \oplus A$, this sequence is random if and only if $A$ is random relative to $\Omega$, since $\Omega$ is random (:ref{#cor-omega-random}); and $\Omega \oplus A$ is random if and only if $A \oplus \Omega$ is. If a 2-random $A$ computed $\emptyset'$, then $A \geq_T \Omega$, contradicting (1) for the random sequence $A \oplus \Omega$.
:::

## 2-randomness

The 2-random sequences avoid every null class that is effectively null relative to $\emptyset'$. They are much less powerful than arbitrary random sequences: by :ref{#cor-van-lambalgen} (2), a 2-random sequence does not compute $\emptyset'$, whereas $\Omega$ is random and computes it. Kurtz (1981) showed that every 2-random sequence has hyperimmune degree, and Kautz (1991) that every 2-random sequence $A$ satisfies $A' \equiv_T A \oplus \emptyset'$; we admit both results. Miller (2004) and Nies, Stephan and Terwijn (2005) characterized 2-randomness by plain complexity: $A$ is 2-random if and only if $C(A \uh n) \geq n - O(1)$ for infinitely many $n$.

## Exercises

::::exercise{difficulty=1}
Let $Z$ be random, $Z_0 = \{ n : 2n \in Z \}$ and $Z_1 = \{ n : 2n + 1 \in Z \}$. Show that $Z_0$ and $Z_1$ are random, and Turing incomparable.

:::solution
$Z = Z_0 \oplus Z_1$. By :ref{#thm-van-lambalgen}, $Z_0$ is random and $Z_1$ is random relative to $Z_0$, hence random. By :ref{#cor-van-lambalgen} (1), they are Turing incomparable.
:::
::::

::::exercise{difficulty=1}
Show that if $A$ is random and $B$ is random relative to $A$, then $B$ is random and $A$ is random relative to $B$.

:::solution
By :ref{#thm-van-lambalgen}, $A \oplus B$ is random. The map $X \oplus Y \mapsto Y \oplus X$ is computable and preserves the measure, so it maps Martin-Löf tests to Martin-Löf tests; hence $B \oplus A$ is random. By :ref{#thm-van-lambalgen} again, $B$ is random and $A$ is random relative to $B$.
:::
::::

## Notes and references

Van Lambalgen proved his theorem in his thesis (1987). The theorem fails for some other randomness notions, such as Schnorr randomness, in one direction. Kurtz's thesis (1981) and Kautz's thesis (1991) contain the basic results on $n$-randomness.

- M. van Lambalgen, *Random sequences*, PhD thesis, University of Amsterdam, 1987.
- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois, 1981.
- J. S. Miller, *Every 2-random real is Kolmogorov random*, Journal of Symbolic Logic 69 (2004), 907–913.
- A. Nies, F. Stephan and S. A. Terwijn, *Randomness, relativization and Turing degrees*, Journal of Symbolic Logic 70 (2005), 515–535.
