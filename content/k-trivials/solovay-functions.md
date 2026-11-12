---
title: Weak truth-table reductions and Solovay functions
summary: K-triviality is preserved by weak truth-table reductions, so no K-trivial set is weak truth-table complete; a computable Solovay function can replace K(n) in the definition, and every K-trivial set is an isolated path of a c.e. tree.
duration: 35
prerequisites: [k-trivial-sets]
---

The definition of K-triviality compares $K(A \uh n)$ with $K(n)$, two functions that are not computable, at every length $n$. This lesson shows that the definition is robust in two directions. First, a reduction that reads a computably bounded part of the oracle preserves K-triviality; as a consequence, a K-trivial set cannot compute $\emptyset'$ by such a reduction, since $\emptyset'$ computes the random sequence $\Omega$ in this way. Second, $K(n)$ can be replaced by a computable function, a Solovay function, which agrees with $K$ up to a constant on infinitely many arguments. The second result turns the tree of :ref{#cor-k-trivial-delta2}, computable in $\emptyset'$, into a c.e. tree.

## Weak truth-table reductions

A Turing reduction $\Phi^X = Y$ is a **weak truth-table** reduction, and we write $Y \leq_{wtt} X$, if there is a computable function $\gamma$ such that the computation $\Phi^X(i)$ only queries the oracle below $\gamma(i)$, for every $i$. Many-one reductions (:ref{#def-many-one}) are weak truth-table reductions. With a computable bound on the use, $Y \uh n$ is computed from $X \uh \gamma'(n)$ for a computable $\gamma'$, and initial segment complexity can only decrease, up to the complexity of the change of length.

:::proposition{#prop-k-trivial-wtt}
If $A$ is K-trivial and $B \leq_{wtt} A$, then $B$ is K-trivial.
:::

:::proof{of=prop-k-trivial-wtt}
Let $B = \Phi^A$ with use bounded by the computable function $\gamma$. Let $h(n) = n + \max \{ \gamma(i) : i < n \}$, with $\max \emptyset = 0$; $h$ is computable, strictly increasing, and $h(n) \geq \gamma(i)$ for every $i < n$. Given the string $A \uh h(n)$, one computes its length $h(n)$, then $n$ as the unique number with this image under $h$, then $B \uh n$ by running $\Phi$ on the inputs $i < n$ with the oracle $A \uh h(n)$. So $K(B \uh n) \leq^+ K(A \uh h(n))$. Since $A$ is K-trivial and $h(n)$ is computed from $n$,
$$
K(B \uh n) \leq^+ K(A \uh h(n)) \leq^+ K(h(n)) \leq^+ K(n).
$$
:::

:::quiz[closure under weak truth-table reductions]
In the proof of :ref{#prop-k-trivial-wtt}, why is $h$ chosen strictly increasing?

- [x] So that $n$ is computed from the length $h(n)$ of the string $A \uh h(n)$: a description of $A \uh h(n)$ then yields $B \uh n$, without a separate description of $n$.
- [ ] So that $h(n) \geq \gamma(i)$ for $i < n$.

  This bound comes from the maximum in the definition of $h$; monotonicity is needed to recover $n$.
- [ ] So that $K(h(n)) \leq^+ K(n)$.

  This holds for every computable function $h$, increasing or not.
:::

The key point is that $n$ is recovered from the length of $A \uh h(n)$. For a Turing reduction the use is not computably bounded, and this argument fails. Downward closure under Turing reducibility is nevertheless true; it is a consequence of the main theorem of the last lesson.

:::corollary{#cor-k-trivial-wtt-incomplete}
No K-trivial set is weak truth-table complete: if $A$ is K-trivial, then $\emptyset' \not\leq_{wtt} A$.
:::

:::proof{of=cor-k-trivial-wtt-incomplete}
We show that $\Omega \leq_{wtt} \emptyset'$; since $\Omega$ is not K-trivial (:ref{#ex-k-trivial}), $\emptyset' \leq_{wtt} A$ would make $\Omega$ K-trivial by :ref{#prop-k-trivial-wtt}, as $\leq_{wtt}$ is transitive. The set $D$ of pairs $\langle j, k \rangle$ with $j\, 2^{-k} < \Omega$ is c.e., since $\Omega$ is the limit of the non-decreasing computable sequence $(\Omega_s)$: $j\,2^{-k} < \Omega$ if and only if $j\,2^{-k} < \Omega_s$ for some $s$. So $D \leq_m \emptyset'$ via a computable $f$ (:ref{#thm-halting-complete}). Since $\Omega$ is irrational (:ref{#thm-omega}), the prefix $\Omega \uh k$ is the binary expansion of length $k$ of the largest $j < 2^k$ with $\langle j, k \rangle \in D$, so it is computed from $\emptyset'$ by querying the positions $f(\langle j, k \rangle)$ for $j < 2^k$, a computable bound on the use.
:::

The last lesson gives a second proof of this corollary, without $\Omega$, by a method that is the starting point of the proof that K-trivial sets are Turing incomplete.

## Solovay functions

The function $K$ is not computable, but some computable functions bound it from above and agree with it, up to a constant, infinitely often. They give a definition of K-triviality with a computable bound.

:::definition{#def-solovay-function}
A **Solovay function** is a computable function $g : \nat \to \nat$ such that $K(m) \leq^+ g(m)$ for every $m$, and $g(m) \leq^+ K(m)$ for infinitely many $m$.
:::

The bound $2\lfloor \log(m + 1) \rfloor + 2$ satisfies the first condition by :ref{#prop-k-basic} (2), but not the second, since $K(m) \leq^+ \log m + 2 \log \log m$ for every $m \geq 4$ (apply :ref{#prop-k-basic} (2) to the string associated with $m$, of length about $\log m$). A Solovay function must be tight at infinitely many arguments; Solovay's idea is to make the argument $m$ encode a shortest description of a number together with its stage of convergence.

Fix a computable bijection $\langle \tau, n, t \rangle$ between $\bstr \times \nat \times \nat$ and $\nat$, with $\langle \tau, n, t \rangle \geq n$.

:::proposition[Solovay]{#prop-solovay-function}
Let $g(m) = |\tau|$ if $m = \langle \tau, n, t \rangle$ and $t$ is the least stage with $U(\tau)[t]\converge = n$, and $g(m) = 2\lfloor \log(m+1) \rfloor + 2$ otherwise. Then $g$ is a Solovay function. Moreover, if $\tau$ is a shortest description of $n$ and $m = \langle \tau, n, t \rangle$ is as in the first case, then $g(m) = K(n)$.
:::

:::proof{of=prop-solovay-function}
The function $g$ is computable, since it is decidable whether $U(\tau)$ converges for the first time at stage $t$ with output $n$.

*$K \leq^+ g$.* In the second case, let $\ell = \lfloor \log(m+1) \rfloor$ be the length of the string associated with $m$. By :ref{#prop-k-basic} (2), $K(m) \leq^+ \ell + 2 \log \ell \leq^+ 2\ell + 2 = g(m)$. In the first case, let $M$ be the machine that, on input $\tau$, waits for the least stage $t$ with $U(\tau)[t]\converge$ and outputs $\langle \tau, U(\tau), t \rangle$. It has the domain of $U$, so it is prefix-free, and $K(m) \leq^+ |\tau| = g(m)$.

*$g \leq^+ K$ infinitely often.* Let $\tau$ be a shortest description of $n$, $t$ its stage of convergence and $m = \langle \tau, n, t \rangle$. Then $g(m) = |\tau| = K(n)$, and $K(n) \leq^+ K(m)$ since $n$ is computed from $m$. There is one such $m$ for each $n$, so infinitely many.
:::

A Solovay function is a computable substitute for $K$ along infinitely many arguments. Bienvenu and Downey observed that it can replace $K(n)$ in the definition of K-triviality.

:::proposition[Bienvenu, Downey]{#prop-solovay-ktrivial}
Let $g$ be the Solovay function of :ref{#prop-solovay-function}. A set $A$ is K-trivial if and only if $K(A \uh m) \leq^+ g(m)$ for every $m$.
:::

:::proof{of=prop-solovay-ktrivial}
($\Rightarrow$) $K(A \uh m) \leq^+ K(m) \leq^+ g(m)$.

($\Leftarrow$) Let $c$ be such that $K(A \uh m) \leq g(m) + c$ for every $m$. Given $n$, let $\tau$ be a shortest description of $n$, $t$ its stage of convergence, and $m = \langle \tau, n, t \rangle \geq n$. Then $K(A \uh m) \leq g(m) + c = K(n) + c$. The string $A \uh n$ is computed from $A \uh m$ by truncation to the length $n$, and $n$ is computed from $m$; so $K(A \uh n) \leq^+ K(A \uh m) \leq^+ K(n)$, with a constant independent of $n$.
:::

:::quiz[Solovay functions and K-triviality]
In the proof of ($\Leftarrow$) in :ref{#prop-solovay-ktrivial}, why is the bound applied at the argument $m = \langle \tau, n, t \rangle$ rather than at $n$?

- [x] Because $g(m) = K(n)$, whereas $g(n)$ may exceed $K(n)$ by an unbounded amount; the prefix $A \uh n$ is then read off $A \uh m$, since $m \geq n$.
- [ ] Because $m$ is computable from $n$.

  It is not: $\tau$ is a shortest description of $n$, which cannot be found computably. The proof only uses that $n$ is computable from $m$.
- [ ] Because $K(m) = K(n)$.

  The proof does not compare $K(m)$ with $K(n)$; it compares $g(m)$ with $K(n)$.
:::

The proof of ($\Leftarrow$) uses the tight arguments $m$ only: the bound at $m = \langle \tau, n, t \rangle$ controls the prefix of length $n \leq m$. Since $g$ is computable and $K$ is approximable from above, the strings $\sigma$ with $K(\sigma \uh m) \leq g(m) + c$ for every $m \leq |\sigma|$ form a c.e. tree, whose paths are exactly the sets satisfying the bound of the proposition with constant $c$. These paths are K-trivial with a constant that depends only on $c$, so there are finitely many of them by :ref{#cor-k-trivial-delta2}. A K-trivial set is thus an isolated path of a c.e. tree, where the definition only gives a tree computable in $\emptyset'$. Bienvenu, Downey, Merkle and Nies used this to give an elementary proof that every K-trivial set is computable from a c.e. K-trivial set, namely a set coding a suitable c.e. tree of this kind. Nies had proved the stronger statement with truth-table reducibility, from the converse of :ref{#thm-obey-ktrivial} of the next lesson. Both proofs are admitted here (Bienvenu, Downey, Merkle and Nies 2015, Corollary 4.13; Nies, Corollary 5.5.3).

## Exercises

::::exercise{difficulty=1}
Show that no K-trivial set is Martin-Löf random, and that if $A$ is K-trivial and $Z$ is random, then neither $A \oplus Z$ nor $\{ 2^i : i \in Z \}$ is K-trivial.

:::solution
A random set satisfies $K(Z \uh n) \geq n - O(1)$, whereas a K-trivial set satisfies $K(A \uh n) \leq^+ 2 \log n$; so no set is both. The set $Z = \{ n : 2n + 1 \in A \oplus Z \}$ is many-one reducible to $A \oplus Z$, and $Z = \{ i : 2^i \in B \}$ for $B = \{ 2^i : i \in Z \}$, so $Z \leq_{wtt} A \oplus Z$ and $Z \leq_{wtt} B$. If one of these sets were K-trivial, so would be $Z$, by :ref{#prop-k-trivial-wtt}, contradicting the first statement.
:::
::::

::::exercise{difficulty=1}
Let $g : \nat \to \nat$ be computable. Show that $K \leq^+ g$ if and only if $\sum_m 2^{-g(m)} < \infty$. Deduce that a computable function $g$ is a Solovay function if and only if $\sum_m 2^{-g(m)} < \infty$ and $g(m) \leq^+ K(m)$ for infinitely many $m$.

:::solution
If $K(m) \leq g(m) + c$ for every $m$, then $\sum_m 2^{-g(m)} \leq 2^c \sum_m 2^{-K(m)} \leq 2^c$, by :ref{#prop-k-basic} (4). Conversely, let $S = \sum_m 2^{-g(m)} < \infty$, and $k$ with $S \leq 2^k$. The requests $(m, g(m) + k)$ form a computable request set of weight $2^{-k} S \leq 1$, so $K(m) \leq^+ g(m) + k$ by the KC theorem (:ref{#thm-kc}). The second statement follows from :ref{#def-solovay-function}.
:::
::::

## Notes and references

Weak truth-table reducibility was introduced by Friedberg and Rogers (1959). The closure of the K-trivial sets under weak truth-table reducibility and the weak truth-table incompleteness of K-trivial sets are in Nies, Proposition 5.2.18. Solovay functions are from Solovay's manuscript (1975); Bienvenu and Downey (2009) proved :ref{#prop-solovay-ktrivial}, with a proof due to Merkle, and Bienvenu, Merkle and Nies showed that every Solovay function, and more generally every right-c.e. function that is an infinitely often tight upper bound for $K$, can replace $K$ in the definition of K-triviality. The journal paper of Bienvenu, Downey, Merkle and Nies (2015) collects these results, with the elementary proof that every K-trivial set is computable from a c.e. K-trivial set (Corollary 4.13). The equivalence of the first exercise is the definition of Solovay functions used by Downey and Hirschfeldt.

The material is in Nies, *Computability and Randomness*, Section 5.2 (Proposition 5.2.18), and in Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Section 3.12 (Theorem 3.12.1, Definition 3.12.3) and Section 11.1.3 (Theorems 11.1.8 and 11.1.9).

- R. M. Friedberg and H. Rogers, Jr., *Reducibility and completeness for sets of integers*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 5 (1959), 117–125.
- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished manuscript, IBM Thomas J. Watson Research Center, 1975.
- L. Bienvenu and R. Downey, *Kolmogorov complexity and Solovay functions*, STACS 2009, 147–158.
- L. Bienvenu, R. Downey, A. Nies and W. Merkle, *Solovay functions and their applications in algorithmic randomness*, Journal of Computer and System Sciences 81 (2015), 1575–1591.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 5.2.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.12 and 11.1.
