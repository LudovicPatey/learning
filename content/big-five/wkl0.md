---
title: Weak König's lemma
summary: The system WKL₀; its ω-models are the Scott ideals; there is a Scott ideal of low sets, so WKL₀ does not prove ACA₀; WKL₀ is equivalent to Σ⁰₁ separation and to the Heine–Borel covering theorem for [0, 1].
duration: 40
prerequisites: [aca0, pi01-classes/pa-degrees]
---

Weak König's lemma, the statement that every infinite binary tree has an infinite path, is the set-existence principle behind compactness arguments. The system $\mathsf{WKL}_0$ lies strictly between $\mathsf{RCA}_0$ and $\mathsf{ACA}_0$, and its computability-theoretic counterpart is the notion of PA degree. It is equivalent to many theorems of analysis and algebra that are proved by compactness: the Heine–Borel theorem, the boundedness of continuous functions on $[0, 1]$, the existence of prime ideals in countable commutative rings, Gödel's completeness theorem for countable languages.

## The system and its ω-models

:::definition{#def-wkl0}
**Weak König's lemma** ($\mathsf{WKL}$) is the statement: every infinite tree $T \subseteq 2^{<\nat}$ has an infinite path. $\mathsf{WKL}_0$ is $\mathsf{RCA}_0 + \mathsf{WKL}$.
:::

Being infinite and being a path are arithmetic properties, so $\mathsf{WKL}$ is a $\Pi^1_2$ statement: for every tree, if it is infinite, there exists a path.

:::definition{#def-scott-ideal}
A **Scott ideal** is a Turing ideal $\mathcal I$ such that every infinite binary tree $T \in \mathcal I$ has an infinite path in $\mathcal I$.
:::

:::proposition{#prop-wkl-scott}
1. An ω-model satisfies $\mathsf{WKL}_0$ if and only if it is a Scott ideal.
2. A Turing ideal $\mathcal I$ is a Scott ideal if and only if for every $X \in \mathcal I$ there is $Y \in \mathcal I$ that is PA relative to $X$.
:::

:::proof{of=prop-wkl-scott}
1. By :ref{#thm-rca-turing-ideal} and absoluteness: a tree in the model is infinite in the model if and only if it is infinite, and a set of the model is a path in the model if and only if it is a path.
2. ($\Rightarrow$) Given $X \in \mathcal I$, the $X$-computable tree whose paths are the $\{0, 1\}$-valued functions DNC relative to $X$ belongs to $\mathcal I$ and is infinite, so it has a path $Y \in \mathcal I$, which is PA relative to $X$. ($\Leftarrow$) Let $T \in \mathcal I$ be an infinite binary tree, and $Y \in \mathcal I$ PA relative to $T$. By the relativization of :ref{#thm-pa-characterization}, $Y$ computes a path of $T$, which belongs to $\mathcal I$.
:::

$\mathrm{REC}$ is not a Scott ideal (:ref{#cor-rca-not-wkl}), so $\mathsf{RCA}_0$ does not prove $\mathsf{WKL}_0$. $\mathsf{ACA}_0$ proves $\mathsf{WKL}_0$, since $\mathsf{WKL}$ is a special case of König's lemma (:ref{#thm-konig-aca}). Correspondingly, a jump ideal is a Scott ideal, since $X'$ computes a path through every infinite $X$-computable binary tree, the leftmost one. The converse fails.

:::theorem{#thm-low-scott}
There is a Scott ideal all of whose members are low. Consequently $\mathsf{WKL}_0$ does not prove $\mathsf{ACA}_0$.
:::

:::proof{of=thm-low-scott}
Define sets $Z_0 = \emptyset$ and $Z_{n+1} = Z_n \oplus P_n$, where $P_n$ is PA relative to $Z_n$ and satisfies $(Z_n \oplus P_n)' \leq_T Z_n'$. Such a $P_n$ exists by the low basis theorem (:ref{#thm-low-basis}) relativized to $Z_n$, applied to the non-empty $\Pi^0_1(Z_n)$ class of $\{0,1\}$-valued functions DNC relative to $Z_n$. By induction, $Z_n' \leq_T \emptyset'$ for every $n$.

Let $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$. It is a Turing ideal, since the sequence $Z_n$ is increasing. It is a Scott ideal: if $X \leq_T Z_n$, then $P_n \leq_T Z_{n+1}$ is in $\mathcal I$ and PA relative to $Z_n$, hence relative to $X$, and :ref{#prop-wkl-scott} (2) applies. Every $X \in \mathcal I$ satisfies $X' \leq_T Z_n' \leq_T \emptyset'$, so $X$ is low. In particular $\emptyset' \notin \mathcal I$, and $\mathcal I$ is not a jump ideal: it is an ω-model of $\mathsf{WKL}_0$ in which $\mathsf{ACA}_0$ fails.
:::

The proof is typical of separations in reverse mathematics: one closes a model under the solutions of a problem while preserving a computability-theoretic weakness, here lowness, that excludes the stronger principle.

:::quiz[models of WKL₀]
In the proof of :ref{#thm-low-scott}, why is $(Z_n \oplus P_n)' \leq_T Z_n'$ required rather than $P_n$ low?

- [x] Because the join of two low sets need not be low: $Z_{n+1}$ is the join of $Z_n$ and $P_n$, and it is the jump of this join that must stay below $\emptyset'$.
- [ ] Because $P_n$ cannot be low.

  It is low: $P_n' \leq_T (Z_n \oplus P_n)' \leq_T Z_n' \leq_T \emptyset'$. The lowness of $P_n$ alone would not suffice, since the join of two low sets need not be low.
- [ ] Because $Z_n$ is not low.

  Every $Z_n$ is low, by the inductive use of this condition.

---

Why does $\mathcal I$ not satisfy $\mathsf{ACA}_0$?

- [x] Because $\mathsf{ACA}_0$ would put $\emptyset'$ into the model, and every member of $\mathcal I$ is low, while $\emptyset'$ is not.
- [ ] Because $\mathcal I$ is countable.

  $\mathrm{ARITH}$ is countable and satisfies $\mathsf{ACA}_0$.
- [ ] Because some infinite tree in $\mathcal I$ has no path in $\mathcal I$.

  $\mathcal I$ is a Scott ideal: every infinite binary tree in it has a path in it.
:::

## Σ⁰₁ separation

The **$\Sigma^0_1$ separation** scheme consists of the universal closures of
$$
\neg \exists n\, (\varphi(n) \wedge \psi(n)) \rightarrow \exists X\, \forall n\, \big( (\varphi(n) \rightarrow n \in X) \wedge (\psi(n) \rightarrow n \notin X) \big),
$$
for $\Sigma^0_1$ formulas $\varphi, \psi$. Its computability-theoretic form is the existence of separating sets for disjoint c.e. sets, one of the characterizations of PA degrees.

:::theorem{#thm-wkl-separation}
Over $\mathsf{RCA}_0$, $\mathsf{WKL}$ is equivalent to $\Sigma^0_1$ separation.
:::

:::proof{of=thm-wkl-separation}
($\Rightarrow$) Write $\varphi(n) \equiv \exists k\, \theta(n, k)$ and $\psi(n) \equiv \exists k\, \eta(n, k)$, with $\theta, \eta$ bounded. Let $T$ be the set of strings $\sigma$ such that for all $n, k < |\sigma|$, $\theta(n, k) \rightarrow \sigma(n) = 1$ and $\eta(n, k) \rightarrow \sigma(n) = 0$. It exists by $\Delta^0_1$ comprehension and is a tree. It is infinite: for each $m$, the string $\sigma$ of length $m$ with $\sigma(n) = 1$ if and only if $\theta(n, k)$ for some $k < m$ belongs to $T$, since no $n$ has witnesses for both formulas. A path $X$ separates: if $\varphi(n)$ with witness $k$, then $X(n) = 1$, by considering a prefix of length larger than $n$ and $k$; similarly for $\psi$.

($\Leftarrow$) Let $T$ be an infinite binary tree. For a string $\sigma$, say that $\sigma$ is **extendible to length $n$** if some $\tau \succeq \sigma$ of length $n$ belongs to $T$, a bounded property. Let
$$
\varphi(\sigma) \equiv \exists n\, (\sigma 0 \text{ is not extendible to length } n \wedge \sigma 1 \text{ is extendible to length } n),
$$
and $\psi(\sigma)$ the same with $0$ and $1$ exchanged, the lengths $n$ being larger than $|\sigma|$. They are disjoint: if $\varphi(\sigma)$ with $n$ and $\psi(\sigma)$ with $n'$, say $n \leq n'$, then $\sigma 0$ is extendible to length $n'$, hence to length $n$, a contradiction; the case $n' \leq n$ is symmetric. Let $S$ separate them, with $\varphi(\sigma) \rightarrow \sigma \in S$ and $\psi(\sigma) \rightarrow \sigma \notin S$. Define $P$ by $P \uh (k+1) = (P \uh k)\, i$ with $i = 1$ if $P \uh k \in S$ and $i = 0$ otherwise; it exists by $\Delta^0_1$ comprehension.

Let $E(\sigma)$ be the $\Pi^0_1$ property "$\sigma$ is extendible to every length". We show $E(P \uh k)$ for every $k$ by $\Pi^0_1$ induction (:ref{#prop-pi01-induction}). $E(\varepsilon)$ holds since $T$ is infinite. Suppose $E(\sigma)$ with $\sigma = P \uh k$. If neither $\sigma 0$ nor $\sigma 1$ had $E$, there would be lengths beyond which neither is extendible, and $\sigma$ would not be extendible beyond their maximum. If only $\sigma 1$ has $E$, then $\varphi(\sigma)$ holds, so $\sigma \in S$ and $P$ chooses $\sigma 1$; if only $\sigma 0$ has $E$, then $\psi(\sigma)$, $\sigma \notin S$, and $P$ chooses $\sigma 0$. If both have $E$, either choice works. So $E(P \uh (k+1))$. In particular every $P \uh k$ belongs to $T$, and $P$ is a path.
:::

:::quiz[Σ⁰₁ separation]
In the reversal of :ref{#thm-wkl-separation}, what does the separating set $S$ decide?

- [x] At each node $\sigma$, which successor to follow: it is correct whenever exactly one successor is extendible to every length, which is the only case where a choice matters.
- [ ] Which nodes belong to $T$.

  Membership in $T$ is decidable from $T$; the separating set decides directions.
- [ ] Which nodes are extendible to every length.

  This is a $\Pi^0_1$ property; $S$ only approximates it in the cases where exactly one successor fails.

---

Why is $\Pi^0_1$ induction needed in the verification?

- [x] Because the property "extendible to every length" is $\Pi^0_1$, and it must be propagated along all prefixes of $P$.
- [ ] Because $P$ is defined by recursion.

  The existence of $P$ follows from $\Delta^0_1$ comprehension; induction is used to prove that it is a path.
- [ ] Because $T$ is infinite.

  Infiniteness gives the base case only.
:::

## The Heine–Borel theorem

The **Heine–Borel theorem** for $[0, 1]$ states: if a sequence of open intervals $(a_i, b_i)$ with rational endpoints covers $[0, 1]$, that is, every real $x \in [0, 1]$ lies in some $(a_i, b_i)$, then finitely many of them cover $[0, 1]$.

:::theorem[Friedman]{#thm-wkl-heine-borel}
Over $\mathsf{RCA}_0$, $\mathsf{WKL}$ is equivalent to the Heine–Borel theorem for $[0, 1]$.
:::

:::proof{of=thm-wkl-heine-borel}
For a binary string $\sigma$, let $I_\sigma$ be the closed dyadic interval $[0.\sigma, 0.\sigma + 2^{-|\sigma|}]$.

($\Rightarrow$) Let $(a_i, b_i)$ cover $[0, 1]$, and suppose that no finite subfamily does. Let $T$ be the set of strings $\sigma$ such that $I_\sigma \not\subseteq \bigcup_{i < |\sigma|} (a_i, b_i)$, a decidable condition on rational intervals. $T$ is a tree, since $I_\tau \supseteq I_\sigma$ and fewer intervals are used for a prefix $\tau$ of $\sigma$. It is infinite: for each $n$, the finite union $\bigcup_{i < n} (a_i, b_i)$ misses some point of $[0, 1]$, which can be taken rational, as an endpoint of the uncovered set, and this point lies in some $I_\sigma$ with $|\sigma| = n$, so $\sigma \in T$. By $\mathsf{WKL}$, $T$ has a path $X$. The real $x = \sum_i X(i) 2^{-i-1}$ lies in every $I_{X \uh n}$. It is covered by some $(a_i, b_i)$, so $(x - \delta, x + \delta) \subseteq (a_i, b_i)$ for some $\delta > 0$. For $n > i$ with $2^{-n} < \delta$, $I_{X \uh n} \subseteq (a_i, b_i)$, contradicting $X \uh n \in T$.

($\Leftarrow$) Let $T$ be an infinite binary tree, and suppose that it has no path. We use the Cantor middle-thirds set: for a string $\sigma$, let $C_\sigma$ be the closed interval of length $3^{-|\sigma|}$ with left endpoint $\sum_{i < |\sigma|} 2\sigma(i) 3^{-i-1}$. Consider the following intervals:

- for each string $\sigma \notin T$, the open interval $U_\sigma$ obtained by enlarging $C_\sigma$ by $3^{-|\sigma|-1}$ on each side;
- the open middle thirds removed in the construction of the Cantor set, at every level.

The sequence of these intervals exists by $\Delta^0_1$ comprehension. It covers $[0, 1]$: a real $x$ outside the removed middle thirds lies in $\bigcap_n C_{X \uh n}$ for some $X$, which can be found by deciding at each level whether $x$ is in the left or the right third; since $X$ is not a path of $T$, some $X \uh n \notin T$, and $x \in C_{X \uh n} \subseteq U_{X \uh n}$. By Heine–Borel, finitely many intervals cover $[0, 1]$; let $n$ exceed the lengths of the strings $\sigma$ whose intervals $U_\sigma$ are used. For a string $\tau$ of length $n$, the left endpoint $c$ of $C_\tau$ is a point of the Cantor set, so it lies in none of the middle thirds, and it is covered by some $U_\sigma$ in the finite family. The interval $U_\sigma$ meets the Cantor set only in $C_\sigma$, because the neighboring intervals of level $|\sigma|$ are at distance at least $3^{-|\sigma|}$. So $c \in C_\sigma$, which means that $\sigma$ is a prefix of $\tau 0 0 \cdots$; since $|\sigma| < n$, $\sigma \preceq \tau$. As $\sigma \notin T$ and $T$ is a tree, $\tau \notin T$. So $T$ has no string of length $n$, contradicting its infiniteness.
:::

The ternary coding avoids a difficulty of binary expansions: in $[0, 1]$, the dyadic intervals $I_{\sigma 0}$ and $I_{\sigma 1}$ share an endpoint, and a real may have two expansions, while the Cantor set separates the pieces of each level by gaps. Many verifications in this proof, such as the existence of the uncovered rational point and the use of the case distinction on $x$, require care in $\mathsf{RCA}_0$; they are carried out in Simpson, Section IV.1.

## Conservation and other equivalents

$\mathsf{WKL}_0$ proves no new arithmetic sentence: by a theorem of Harrington, every $\Pi^1_1$ sentence provable in $\mathsf{WKL}_0$ is provable in $\mathsf{RCA}_0$. The proof uses a forcing argument over non-standard models; it is given in the specialized course on induction and conservation (:ref{to="induction-conservation/harrington"}). So compactness arguments, though non-constructive, do not increase the arithmetic consequences of the base theory; $\mathsf{WKL}_0$ is moreover $\Pi^0_2$-conservative over primitive recursive arithmetic, a partial realization of Hilbert's program.

The following are also equivalent to $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$ (Simpson, Chapter IV): every continuous function on $[0, 1]$ is bounded; every continuous function on $[0, 1]$ attains its maximum; Gödel's completeness theorem for countable languages; every countable commutative ring has a prime ideal; Brouwer's fixed point theorem; the Hahn–Banach theorem for separable Banach spaces.

## Exercises

::::exercise{difficulty=1}
Show that there is no least ω-model of $\mathsf{WKL}_0$, but that the intersection of all ω-models of $\mathsf{WKL}_0$ is $\mathrm{REC}$.

:::solution
For every non-computable set $C$ there is a Scott ideal not containing $C$: build the sequence $Z_n$ of :ref{#thm-low-scott} with $P_n$ PA relative to $Z_n$ and $C \not\leq_T Z_n \oplus P_n$, using the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $Z_n$; by induction $C \not\leq_T Z_n$ for every $n$. So every non-computable set is missing from some ω-model of $\mathsf{WKL}_0$, and the intersection of all of them is $\mathrm{REC}$, which is not a model. A least ω-model would be contained in this intersection, hence equal to $\mathrm{REC}$, a contradiction.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{WKL}$ is equivalent over $\mathsf{RCA}_0$ to the statement: for every pair of injective functions $f, g$ with disjoint ranges, there is a set $X$ containing the range of $f$ and disjoint from the range of $g$.

:::solution
The statement follows from $\Sigma^0_1$ separation with $\varphi(n) \equiv \exists i\, f(i) = n$ and $\psi(n) \equiv \exists i\, g(i) = n$. Conversely, let $\exists k\, \theta(n, k)$ and $\exists k\, \eta(n, k)$ be disjoint $\Sigma^0_1$ formulas. Let $f(\langle n, k \rangle) = 2n + 1$ if $k$ is the least witness of $\theta(n, k)$, and $f(\langle n, k \rangle) = 4 \langle n, k \rangle$ otherwise; let $g(\langle n, k \rangle) = 2n + 1$ if $k$ is the least witness of $\eta(n, k)$, and $g(\langle n, k \rangle) = 4 \langle n, k \rangle + 2$ otherwise. Both are injective, as in :ref{#thm-aca-equivalents}. Their ranges are disjoint: odd values $2n + 1$ come from $f$ only if $\theta$ has a witness for $n$, and from $g$ only if $\eta$ has one, which never happen together; the even values of $f$ are multiples of $4$ and those of $g$ are not. If $X$ contains the range of $f$ and avoids the range of $g$, the set $\{ n : 2n + 1 \in X \}$ separates the two formulas.
:::
::::

## Notes and references

Friedman (1976) identified $\mathsf{WKL}_0$ and proved the equivalence with the Heine–Borel theorem. The characterization of its ω-models by Scott ideals goes back to Scott (1962). Harrington's conservation theorem is unpublished; Simpson's monograph presents it. The $\Pi^0_2$ conservation over primitive recursive arithmetic is due to Friedman; Sieg gave a proof-theoretic proof.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Chapter IV.
- H. Friedman, *Systems of second order arithmetic with restricted induction*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- W. Sieg, *Fragments of arithmetic*, Annals of Pure and Applied Logic 28 (1985), 33–71.
