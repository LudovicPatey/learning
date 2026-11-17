---
title: Demuth's theorem
summary: A non-computable set truth-table reducible to a Martin-Löf random sequence is Turing equivalent to a random sequence (Demuth). Consequences include random degrees all of whose non-zero predecessors are random, Ω is not truth-table complete, and a c.e. set that is weak truth-table complete but not truth-table complete.
duration: 20
prerequisites: [computable-measures, immunity-growth/hypersimple-sets, immunity-growth/computably-dominated, stephan-theorem, left-ce-reals/approximations]
---

The random degrees are not closed downward: every random sequence computes a DNC function, and random sequences below $\emptyset'$ compute non-computable c.e. sets, which are not of random degree by Kučera's theorem (:ref{#thm-kucera-ce-random}). Demuth found that they are closed downward for a stronger reducibility. If $B \leq_{tt} A$ for a random sequence $A$, and $B$ is not computable, then $B$ is Turing equivalent to a random sequence. Information extracted from a random sequence by a truth-table reduction, which must give an answer for every oracle, is again random, up to Turing equivalence.

The proof, due to Kautz, transports the measure. A truth-table functional $\Phi$ maps the uniform measure to a computable measure $\nu$, the probability that $\Phi^X$ extends a given string when $X$ is chosen at random. The image of a random sequence is $\nu$-random, since tests pull back along $\Phi$. By the theorem of Levin and Kautz of the previous lesson, a non-computable $\nu$-random sequence is Turing equivalent to a random sequence.

## The theorem

Recall that $B \leq_{tt} A$ if $B = \Phi^A$ for a Turing functional $\Phi$ such that $\Phi^X$ is total for every oracle $X$ (:ref{to="immunity-growth/hypersimple-sets"}). By compactness, the use of $\Phi^X(n)$ is then bounded by a computable function of $n$, independent of $X$.

:::theorem[Demuth]{#thm-demuth}
Let $A$ be Martin-Löf random and $B \leq_{tt} A$ not computable. Then there is a random sequence $C \equiv_T B$.
:::

:::proof{of=thm-demuth}
Let $\Phi$ be a functional, total on every oracle, with $\Phi^A = B$, and let $\gamma$ be a computable function bounding the use of $\Phi^X(n)$ for every $X$. For a string $\sigma$ of length $n$, let
$$
\rho(\sigma) = \lambda(\{ X : \Phi^X \uh n = \sigma \}).
$$
Whether $\Phi^X \uh n = \sigma$ depends only on $X \uh \delta(n)$, where $\delta(n) = \max_{i < n} \gamma(i)$, so the class is clopen and $\rho(\sigma)$ is a rational, computable from $\sigma$. Moreover $\rho(\varepsilon) = 1$ and $\rho(\sigma) = \rho(\sigma 0) + \rho(\sigma 1)$, since $\Phi^X$ is total and, replacing every value other than $0$ by $1$, $\{0, 1\}$-valued. So $\rho$ is a computable premeasure; let $\nu$ be its measure. Then $\nu(\mathcal V) = \lambda(\{ X : \Phi^X \in \mathcal V \})$ for every $\Sigma^0_1$ class $\mathcal V$, since this holds for cylinders and the generators can be taken prefix-free.

*$B$ is $\nu$-random.* Let $(\mathcal V_n)$ be a $\nu$-test, and $\mathcal U_n = \{ X : \Phi^X \in \mathcal V_n \}$. The classes $\mathcal U_n$ are uniformly $\Sigma^0_1$: $X \in \mathcal U_n$ if and only if $\Phi^X$ extends a generator of $\mathcal V_n$, which is witnessed by a finite part of $X$. And $\lambda(\mathcal U_n) = \nu(\mathcal V_n) \leq 2^{-n}$. So $(\mathcal U_n)$ is a Martin-Löf test, and $A$ passes it. So $B = \Phi^A$ passes $(\mathcal V_n)$.

*Conclusion.* $B$ is $\nu$-random and not computable. By :ref{#thm-levin-kautz} (2), the common point $\alpha$ of the intervals $(B \uh n)_\nu$ is a random real with $\alpha \equiv_T B$. Let $C$ be its binary expansion.
:::

:::quiz[Demuth's theorem]
In the proof of :ref{#thm-demuth}, where is it used that the reduction is a truth-table reduction and not an arbitrary Turing reduction?

- [x] To make $\rho$ a computable premeasure: the measure of the oracles $X$ with $\Phi^X \uh n = \sigma$ is then a computable rational, and the values $\rho(\sigma 0) + \rho(\sigma 1)$ add up to $\rho(\sigma)$ because $\Phi^X$ is total for every $X$.
- [ ] To show that the classes $\mathcal U_n$ are $\Sigma^0_1$.

  The preimage of a $\Sigma^0_1$ class by any Turing functional is $\Sigma^0_1$.
- [ ] To show that $B$ is not computable.

  This is a hypothesis of the theorem.
:::

For a Turing reduction, the measure $\rho(\sigma)$ of the oracles computing an extension of $\sigma$ is only left-c.e., and the oracles on which $\Phi$ is partial take away measure; the theorem fails, since non-computable c.e. sets computable from random sequences are not of random degree.

## Consequences

:::corollary[Kautz]{#cor-kautz-random-cone}
There is a random sequence $A$ such that every non-computable set $B \leq_T A$ is Turing equivalent to a random sequence.
:::

:::proof{of=cor-kautz-random-cone}
By the computably dominated basis theorem (:ref{#thm-dominated-basis}) applied to a non-empty $\Pi^0_1$ class of random sequences (:ref{#cor-mlr-structure}), there is a computably dominated random sequence $A$. By :ref{#thm-dominated-tt}, every $B \leq_T A$ satisfies $B \leq_{tt} A$, and :ref{#thm-demuth} applies.
:::

:::corollary[Calude, Nies]{#cor-omega-not-tt-complete}
1. If $\alpha$ is a left-c.e. real that is neither computable nor Turing complete, then $\alpha \not\leq_{tt} \Omega$.
2. $\Omega$ is not truth-table complete: $\emptyset' \not\leq_{tt} \Omega$.
:::

:::proof{of=cor-omega-not-tt-complete}
1. The real $\alpha$ has a c.e. degree (:ref{#prop-cut-expansion}). If $\alpha \leq_{tt} \Omega$, then by :ref{#thm-demuth}, $\alpha$ is Turing equivalent to a random sequence $C$; then $C$ has c.e. degree and is not Turing complete, which contradicts :ref{#thm-kucera-ce-random}.
2. By :ref{#cor-kucera-post}, there is a low simple c.e. set $D$, which is neither computable nor complete. If $\emptyset' \leq_{tt} \Omega$, then $D \leq_{tt} \Omega$, since every c.e. set is many-one reducible to $\emptyset'$. The binary expansion of the left-c.e. real $r_D = \sum_{n \in D} 2^{-n-1}$ is $D$, so $r_D \leq_{tt} \Omega$, contradicting 1.
:::

:::corollary[Lachlan]{#cor-lachlan-wtt-tt}
There is a c.e. set that is weak truth-table complete but not truth-table complete.
:::

:::proof{of=cor-lachlan-wtt-tt}
Let $Q$ be the set of dyadic rationals $q$ with $q < \Omega$, coded as numbers; it is c.e. For a dyadic rational $q = j 2^{-n}$, $q < \Omega$ holds if and only if $q \leq 0.(\Omega \uh n)$, since $\Omega$ is irrational; this is a truth-table condition on the first $n$ bits of $\Omega$, so $Q \leq_{tt} \Omega$. Conversely, the first $n$ bits of $\Omega$ are the binary representation of the largest $j < 2^n$ with $j 2^{-n} \in Q$, a truth-table condition on $Q$; so $\Omega \leq_{tt} Q$. Since $\Omega \equiv_{wtt} \emptyset'$ (lesson :ref{to="left-ce-reals/approximations"}), $Q$ is weak truth-table complete, and since $\emptyset' \not\leq_{tt} \Omega$, it is not truth-table complete.
:::

::::exercise[Truth-table images of Ω]{#ex-tt-below-omega difficulty=1 objective="Apply Demuth's theorem to sets truth-table below Ω."}
Show that every non-computable set $B \leq_{tt} \Omega$ is Turing equivalent to a random sequence, and that $B$ is Turing complete if it has c.e. degree.

:::solution
$\Omega$ is random, so the first statement is :ref{#thm-demuth}. If moreover $B$ has c.e. degree, the random sequence $C \equiv_T B$ has c.e. degree, and is Turing complete by :ref{#thm-kucera-ce-random}.
:::
::::

## Notes and references

Demuth's theorem is from his 1988 paper; the proof through measures is due to Kautz (1991), as presented by Downey and Hirschfeldt (Theorem 8.6.1 and Corollaries 8.6.2–8.6.4). Calude and Nies (1997) proved that $\Omega$ is not truth-table complete; Lachlan's theorem (1968) originally had a direct, harder proof, and the proof here was pointed out by Nies. Bienvenu and Porter showed that the Turing equivalence cannot be replaced by weak truth-table equivalence: some $B \leq_{tt} \Omega$ is not weak truth-table equivalent to any random sequence (Downey–Hirschfeldt, after Theorem 8.6.1).

- O. Demuth, *Remarks on the structure of tt-degrees based on constructive measure theory*, Commentationes Mathematicae Universitatis Carolinae 29 (1988), 233–247.
- S. M. Kautz, *Degrees of random sets*, PhD thesis, Cornell University, 1991.
- C. S. Calude and A. Nies, *Chaitin Ω numbers and strong reducibilities*, Journal of Universal Computer Science 3 (1997), 1162–1166.
- A. H. Lachlan, *Complete recursively enumerable sets*, Proceedings of the American Mathematical Society 19 (1968), 99–102.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 8.6.

:::::exercises
::::exercise{#ex-demuth-columns difficulty=1 objective="Recover a known closure property of random sequences from Demuth's theorem."}
Let $A$ be random. Show without van Lambalgen's theorem that each column $A^{[i]} = \{ n : \langle i, n \rangle \in A \}$ is Turing equivalent to a random sequence, and that so is the sequence of the bits of $A$ at even positions.

:::solution
The maps $A \mapsto A^{[i]}$ and $A \mapsto (A(2n))_n$ are truth-table reductions: each bit of the output is a bit of the oracle. The images are not computable: if $A^{[i]}$ were computable, the classes $\{ X : X^{[i]} \uh n = A^{[i]} \uh n \}$ would be uniformly clopen of measure $2^{-n}$ and capture $A$; similarly for the even bits. By :ref{#thm-demuth}, they are Turing equivalent to random sequences. (Van Lambalgen's theorem gives more: they are random themselves.)
:::
::::

::::exercise{#ex-demuth-hyperimmune-free difficulty=2 objective="Combine Demuth's theorem with Kučera's theorem to compare the cones below random sequences."}
Let $A$ be a computably dominated random sequence. Show that $A$ computes no non-computable c.e. set, and deduce that $A$ is not computable in $\emptyset'$.

:::solution
If $B \leq_T A$ is c.e. and not computable, then $B \leq_{tt} A$ by :ref{#thm-dominated-tt}, so $B$ is Turing equivalent to a random sequence $C$ by :ref{#thm-demuth}. Then $C$ has c.e. degree, so $C \equiv_T \emptyset'$ by :ref{#thm-kucera-ce-random}, and $\emptyset' \equiv_T B \leq_T A$. A computably dominated set does not compute $\emptyset'$: the settling-time function of $\emptyset'$ would be computable in $A$ and dominated by a computable function, which would make $\emptyset'$ computable, as in :ref{#ex-stephan-above-incomplete}. So $A$ computes no non-computable c.e. set. By :ref{#cor-kucera-post} (1), a random sequence computable in $\emptyset'$ computes a simple c.e. set; so $A \not\leq_T \emptyset'$.
:::
::::
:::::
