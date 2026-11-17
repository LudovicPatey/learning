---
title: Left-c.e. reals
summary: Left-c.e. reals through left cuts, increasing approximations and sums; their Turing degrees are the c.e. degrees; a left-c.e. real whose binary expansion is not c.e.; left-c.e. reals are the halting probabilities of prefix-free machines.
duration: 40
prerequisites: [martin-lof-randomness/measure, kolmogorov-complexity/coding-theorem]
---

The halting probability $\Omega$ is approximated from below by the rationals $\Omega_s$, and cannot be approximated from above. Reals of this kind, the **left-c.e. reals**, play in algorithmic randomness the role that c.e. sets play in computability theory. A c.e. set is the domain of a machine; a left-c.e. real is the halting probability of a prefix-free machine, the measure of the domain. The random left-c.e. reals will turn out to be exactly the halting probabilities of optimal machines, and they are all equivalent for a reducibility that measures the speed of approximations. This course develops that theory, after Solovay, Kučera and Slaman, and Downey, Hirschfeldt and Nies.

This first lesson collects the basic facts. A left-c.e. real has several equivalent definitions, by its left cut, by approximations and by sums. Its Turing degree is c.e., but its binary expansion need not be a c.e. set. The last section shows that the left-c.e. reals of $[0, 1]$ are exactly the halting probabilities of prefix-free machines, and that the halting probability of a machine computes its domain.

## Definitions

We identify a sequence $X \in \cs$ with the real $0.X = \sum_i X(i) 2^{-i-1}$ of $[0, 1]$. Every real of $[0, 1)$ has a unique binary expansion that does not end with infinitely many $1$s, and a real is identified with this expansion; the only reals with two expansions are the dyadic rationals, which are computable and play no role. Unless stated otherwise, the reals of this course are in $[0, 1]$. The **left cut** of a real $\alpha$ is $L(\alpha) = \{ q \in \mathbb Q : q < \alpha \}$.

:::proposition[Soare]{#prop-left-ce}
For a real $\alpha$, the following are equivalent:

1. $L(\alpha)$ is c.e.;
2. $\alpha$ is the limit of a computable non-decreasing sequence of rationals;
3. $\alpha$ is the limit of a computable strictly increasing sequence of rationals;
4. $\alpha = \sum_n r_n$ for a computable sequence of non-negative rationals $(r_n)$.

A real with these properties is **left-c.e.**; a real $\alpha$ is **right-c.e.** if $-\alpha$ is left-c.e.
:::

:::proof{of=prop-left-ce}
(1 ⇒ 2) $L(\alpha)$ is not empty. Let $q_0, q_1, \dots$ be a computable enumeration of it, possibly with repetitions, and $p_s = \max_{t \leq s} q_t$. Then $(p_s)$ is non-decreasing, $p_s < \alpha$, and $\sup_s p_s = \sup L(\alpha) = \alpha$.

(2 ⇒ 3) If $(p_s)$ is non-decreasing with limit $\alpha$, then $p_s - 2^{-s}$ is strictly increasing, with the same limit.

(3 ⇒ 4) Replace $p_s$ by $\max(p_s, 0)$, which gives a non-decreasing sequence with the same limit, since $\alpha \geq 0$. Take $r_0 = p_0$ and $r_{n+1} = p_{n+1} - p_n$.

(4 ⇒ 1) Let $S_k = \sum_{n < k} r_n$. Then $q < \alpha$ if and only if $q < S_k$ for some $k$: the partial sums are non-decreasing with limit $\alpha$, so if $q < \alpha$ some $S_k$ exceeds $q$, and conversely $S_k \leq \alpha$. So $L(\alpha)$ is c.e.
:::

Whenever we mention a left-c.e. real $\alpha$, we fix a computable strictly increasing sequence of rationals $\alpha_0 < \alpha_1 < \cdots$ with limit $\alpha$, its **approximation**. For $\Omega$, this is $\Omega_s$, up to the shift of (2 ⇒ 3). Examples of left-c.e. reals are the measures of $\Sigma^0_1$ classes, the halting probabilities $\Omega_M$ of prefix-free machines (:ref{#ex-omega-ce-set}), and the reals $r_A = \sum_{n \in A} 2^{-n-1}$ for c.e. sets $A$ (:ref{#prop-measure-effective}).

A real is computable if and only if it is both left-c.e. and right-c.e.: with approximations from below and from above, compute both until they are $2^{-n}$-close. The binary expansion and the left cut carry the same information.

:::proposition{#prop-cut-expansion}
For every irrational $\alpha \in (0, 1)$, the binary expansion of $\alpha$ and the left cut $L(\alpha)$ are Turing equivalent, uniformly. Consequently, the Turing degree of a left-c.e. real is a c.e. degree, and every c.e. degree contains a left-c.e. real.
:::

:::proof{of=prop-cut-expansion}
Let $X$ be the binary expansion of $\alpha$, and $x_n = 0.(X \uh n)$, so that $x_n < \alpha < x_n + 2^{-n}$, the inequalities being strict since $\alpha$ is irrational. Given a rational $q$, compute $x_0, x_1, \dots$ from $X$ until $q \leq x_n$, in which case $q < \alpha$, or $q \geq x_n + 2^{-n}$, in which case $q > \alpha$. One of the two happens, since $q \neq \alpha$. Conversely, $X \uh n$ is the string $\sigma$ of length $n$ with $0.\sigma \in L(\alpha)$ and $0.\sigma + 2^{-n} \notin L(\alpha)$: decide these two memberships for the $2^n$ strings of length $n$.

If $\alpha$ is left-c.e., $L(\alpha)$ is c.e., so $\alpha$ has the c.e. degree of $L(\alpha)$ when $\alpha$ is irrational; rational reals are computable. If $A$ is c.e., infinite and coinfinite, the binary expansion of $r_A$ is $A$, and $r_A$ is left-c.e.; finite and cofinite sets are computable.
:::

## Binary expansions of left-c.e. reals

A c.e. set $A$, read as a binary expansion, gives a left-c.e. real $r_A$: enumerating an element changes a bit from $0$ to $1$ and increases the real. The converse fails. In an approximation of a left-c.e. real, a bit can change from $1$ to $0$, provided a more significant bit changes from $0$ to $1$, as in a carry. A real is **strongly c.e.** if its binary expansion is a c.e. set.

:::theorem[Soare]{#thm-not-strongly-ce}
There is a left-c.e. real that is not strongly c.e.
:::

The proof builds the expansion by pairs of bits. The pair at positions $2e$ and $2e + 1$ starts as $01$, and changes once to $10$ if the number $2e + 1$ is enumerated into $W_e$, the $e$-th c.e. set. The change increases the real, since $0.10$ exceeds $0.01$ in each block, and it makes the bit at position $2e + 1$ differ from its membership in $W_e$.

:::proof{of=thm-not-strongly-ce}
For each $s$, let $A_s$ be the set of the numbers $2e$ with $e < s$ and $2e + 1 \in W_{e, s}$, and of the numbers $2e + 1$ with $e < s$ and $2e + 1 \notin W_{e, s}$, where $W_{e, s}$ is the finite part of $W_e$ enumerated by stage $s$. Each $A_s$ is a finite set contained in $\{0, \dots, 2s - 1\}$, uniformly computable, so $q_s = \sum_{n \in A_s} 2^{-n-1}$ is a computable sequence of rationals.

*The sequence is non-decreasing.* From stage $s$ to $s + 1$, the block of $e = s$ is added, with bit $1$ at position $2s$ or $2s + 1$, and each block $e < s$ either stays the same or changes from $01$ to $10$ once and for all, when $2e + 1$ enters $W_e$. Such a change adds $2^{-2e-1} - 2^{-2e-2} > 0$. So $q_s \leq q_{s+1}$.

*The limit.* Let $A$ contain $2e$ if $2e + 1 \in W_e$, and $2e + 1$ otherwise. For each $n$, the restriction $A_s \cap \{0, \dots, n\}$ is eventually constant, equal to $A \cap \{0, \dots, n\}$, since each block changes at most once. So $q_s$ converges to $r_A = \sum_{n \in A} 2^{-n-1}$, which is left-c.e. The set $A$ contains exactly one element of each block, so it has infinitely many elements outside it and is the binary expansion of $r_A$.

*Not c.e.* For every $e$, $2e + 1 \in A$ if and only if $2e + 1 \notin W_e$. So $A \neq W_e$.
:::

Calude, Hertling, Khoussainov and Wang characterized the binary expansions of left-c.e. reals by this carry phenomenon (:ref{#ex-almost-ce}).

The left-c.e. reals are closed under addition and multiplication of non-negative reals: if $\alpha_s \to \alpha$ and $\beta_s \to \beta$ are non-decreasing approximations, so are $\alpha_s + \beta_s$ and, for non-negative terms, $\alpha_s \beta_s$. They are not closed under subtraction: $\alpha - \beta$ is a difference of left-c.e. reals, and Ambos-Spies, Weihrauch and Zheng showed that the differences of left-c.e. reals form a field that contains reals that are neither left-c.e. nor right-c.e. (admitted; Downey–Hirschfeldt, Theorems 5.1.10 and 5.4.6).

## Halting probabilities

For a prefix-free machine $M$, the halting probability $\Omega_M = \sum_{\tau \in \dom M} 2^{-|\tau|}$ is the measure of the $\Sigma^0_1$ class generated by $\dom M$. The next theorem says that every left-c.e. real is of this form, so left-c.e. reals correspond to domains of prefix-free machines as c.e. sets correspond to domains of machines.

:::theorem{#thm-left-ce-halting}
For a real $\alpha \in [0, 1]$, the following are equivalent:

1. $\alpha$ is left-c.e.;
2. $\alpha = \Omega_M$ for a prefix-free machine $M$;
3. $\alpha$ is the weight $\sum_{\tau \in W} 2^{-|\tau|}$ of a c.e. prefix-free set $W$;
4. $\alpha$ is the weight of a computable prefix-free set;
5. $\alpha = \lambda(\mathcal U)$ for a $\Sigma^0_1$ class $\mathcal U$.
:::

:::proof{of=thm-left-ce-halting}
(1 ⇒ 2) Let $(p_s)$ be a computable non-decreasing sequence of rationals with limit $\alpha$ and $p_0 = 0$, and let $d_s = \lfloor 2^s p_s \rfloor / 2^s$, the largest dyadic rational of denominator $2^s$ below $p_s$. Then $(d_s)$ is non-decreasing, since $2^{s+1} p_{s+1} \geq 2 \cdot 2^s p_s$ gives $\lfloor 2^{s+1} p_{s+1} \rfloor \geq 2 \lfloor 2^s p_s \rfloor$, and $p_s - 2^{-s} < d_s \leq p_s$, so $d_s \to \alpha$. Each difference $d_{s+1} - d_s$ is a dyadic rational, hence a finite sum of distinct powers $2^{-k}$, read off its binary expansion. Listing these powers for $s = 0, 1, \dots$ gives a computable sequence $(n_i)$ with $\sum_i 2^{-n_i} = \alpha \leq 1$. The requests $(\varepsilon, n_i)$ form a bounded c.e. request set of weight $\alpha$. The machine $M$ built in the proof of :ref{#thm-kc} assigns to each request its own string of the requested length, and has no other element in its domain; so $\Omega_M = \sum_i 2^{-n_i} = \alpha$.

(2 ⇒ 3) Take $W = \dom M$.

(3 ⇒ 4) Let $W$ be enumerated with at most one new element per stage. When $\sigma$ enters $W$ at stage $s$, put into $B$ all the extensions of $\sigma$ of length $\max(|\sigma|, s)$. Their total weight is $2^{-|\sigma|}$, and strings coming from incomparable strings of $W$ are incomparable, so $B$ is prefix-free with the same weight as $W$. It is computable: a string $\tau$ is in $B$ if and only if some $\sigma \preceq \tau$ enters $W$ at a stage $s \leq |\tau|$ with $|\tau| = \max(|\sigma|, s)$, which is decided by running the enumeration for $|\tau|$ stages.

(4 ⇒ 5) The class generated by a prefix-free set $B$ has measure equal to its weight, since the cylinders $[\tau]$, $\tau \in B$, are pairwise disjoint; and it is $\Sigma^0_1$ when $B$ is c.e.

(5 ⇒ 1) This is :ref{#prop-measure-effective}.
:::

The halting probability of a machine encodes its domain in a compressed form, as $\Omega$ encodes the domain of $U$ in :ref{#thm-omega}.

:::proposition{#prop-omega-m-domain}
For every prefix-free machine $M$ and every $n$, the first $n$ bits of $\Omega_M$ determine, uniformly in $n$ and an index of $M$, the set of strings of length at most $n$ in the domain of $M$, provided $\Omega_M$ is irrational. In particular, the domain of $M$ is Turing reducible to $\Omega_M$, with a computable bound on the use.
:::

:::proof{of=prop-omega-m-domain}
Let $\Omega_{M, s} = \sum \{ 2^{-|\tau|} : |\tau| \leq s,\ M(\tau)[s]\converge \}$. Given the first $n$ bits of $\Omega_M$, let $q$ be the dyadic rational they define, so that $q < \Omega_M < q + 2^{-n}$. Search for a stage $s \geq n$ with $\Omega_{M, s} > q$. A string of length at most $n$ in the domain of $M$ that converges after stage $s$ would give $\Omega_M \geq \Omega_{M, s} + 2^{-n} > q + 2^{-n}$, which is false. So the strings of length at most $n$ in the domain are those that converge by stage $s$. To decide whether $\tau \in \dom M$, use the first $|\tau|$ bits of $\Omega_M$.
:::

:::quiz[halting probabilities]
In the proof of :ref{#prop-omega-m-domain}, why is the stage $s$ chosen with $\Omega_{M, s} > q$, and not merely $\Omega_{M, s} \geq q$?

- [x] With the strict inequality, a new string of length at most $n$ would push $\Omega_M$ to at least $q + 2^{-n}$, contradicting $\Omega_M < q + 2^{-n}$; with $\Omega_{M, s} = q$, the remaining weight could still be close to $2^{-n}$.
- [ ] Because $\Omega_{M, s}$ is always irrational.

  $\Omega_{M, s}$ is a finite sum of powers of $2$, a dyadic rational.
- [ ] To ensure that the search terminates.

  The search for $\Omega_{M, s} > q$ terminates because $\Omega_M > q$; a weaker condition would terminate too.

---

In the proof of (3 ⇒ 4) in :ref{#thm-left-ce-halting}, why is a string $\sigma$ entering $W$ at stage $s$ replaced by its extensions of length $\max(|\sigma|, s)$?

- [x] So that membership in $B$ of a string $\tau$ only depends on the first $|\tau|$ stages of the enumeration, which makes $B$ computable, while the weight is unchanged.
- [ ] To make $B$ prefix-free.

  $W$ is already prefix-free, and $B$ would be prefix-free with any choice of lengths.
- [ ] To make the weight of $B$ smaller than that of $W$.

  The extensions of $\sigma$ of a fixed length have total weight exactly $2^{-|\sigma|}$.
:::

Applied to the optimal machine, :ref{#prop-omega-m-domain} gives $\emptyset' \leq_T \Omega$ with a computable bound on the use, through the domain of $U$. Conversely, the binary expansion $X$ of an irrational left-c.e. real $\alpha$ is computable from $\emptyset'$ with a computable bound on the use. For each $n$, the numbers $\lfloor 2^n \alpha_s \rfloor$ are non-decreasing in $s$, bounded by $2^n$, with limit $\lfloor 2^n \alpha \rfloor$, the number written by $X \uh n$. For $k \leq 2^n$, the question whether $\lfloor 2^n \alpha_s \rfloor \geq k$ for some $s$ is $\Sigma^0_1$, and $X \uh n$ is the binary representation of the largest $k$ with a positive answer. The $2^n + 1$ questions are computed from $n$. A Turing reduction whose use is bounded by a computable function is a **weak truth-table** reduction, written $\leq_{wtt}$. So **every left-c.e. real is weak truth-table reducible to $\emptyset'$**, and $\Omega \equiv_{wtt} \emptyset'$.

::::exercise[Almost c.e. sets]{#ex-almost-ce difficulty=2 objective="Characterize the binary expansions of left-c.e. reals by the carry property of their approximations."}
A set $A$ is **almost c.e.** if it has a computable approximation $(A_s)$, by finite sets, with $\lim_s A_s(n) = A(n)$ for every $n$, such that whenever $A_s(n) = 1$ and $A_{s+1}(n) = 0$, there is $m < n$ with $A_s(m) = 0$ and $A_{s+1}(m) = 1$. Show that an irrational real $\alpha \in (0,1)$ is left-c.e. if and only if its binary expansion is almost c.e.

:::hint
For finite sets $F$ and $G$, compare $\sum_{n \in F} 2^{-n-1}$ and $\sum_{n \in G} 2^{-n-1}$ through the first position where $F$ and $G$ differ.
:::

:::solution
For finite sets $F \neq G$, let $m$ be the least element of their symmetric difference. Then $\sum_{n \in G} 2^{-n-1} > \sum_{n \in F} 2^{-n-1}$ if and only if $m \in G$, since the bits after $m$ contribute less than $2^{-m-1}$ in absolute value. Hence $\sum_{G} \geq \sum_F$ if and only if every $n \in F \setminus G$ is preceded by some $m < n$ in $G \setminus F$.

Let $\alpha$ be left-c.e. with approximation $(\alpha_s)$, and let $A_s$ be the finite set with $\sum_{n \in A_s} 2^{-n-1} = \lfloor 2^s \alpha_s \rfloor 2^{-s}$, read off the first $s$ bits. These values are non-decreasing in $s$ (as in the proof of :ref{#thm-left-ce-halting}), so by the first paragraph $(A_s)$ has the carry property. Since $\alpha$ is irrational, for each $n$ the first $n$ bits of the approximations eventually agree with those of $\alpha$, so $A_s(n) \to A(n)$, where $A$ is the binary expansion. Conversely, if $A$ is almost c.e. with approximation $(A_s)$, the rationals $q_s = \sum_{n \in A_s \cap \{0, \dots, s\}} 2^{-n-1}$ are non-decreasing by the first paragraph, applied to $A_s \cap \{0, \dots, s\}$ and $A_{s+1} \cap \{0, \dots, s+1\}$ (the new position $s + 1$ can only add a bit), and they converge to $0.A$ since each bit converges. So $0.A$ is left-c.e. (Calude, Hertling, Khoussainov and Wang; Downey–Hirschfeldt, Theorem 5.1.7.)
:::
::::

## Notes and references

The characterizations of left-c.e. reals by cuts, approximations and sums go back to Soare (1969), who also built a left-c.e. real that is not strongly c.e. Calude, Hertling, Khoussainov and Wang (2001) characterized their expansions as almost c.e. sets, and the equivalence with halting probabilities and measures of $\Sigma^0_1$ classes assembles work of several authors (Downey–Hirschfeldt, Theorem 5.1.11). Left-c.e. reals are often called c.e. reals, or lower semicomputable reals.

- R. I. Soare, *Recursion theory and Dedekind cuts*, Transactions of the American Mathematical Society 140 (1969), 271–294.
- C. S. Calude, P. H. Hertling, B. Khoussainov and Y. Wang, *Recursively enumerable reals and Chaitin Ω numbers*, Theoretical Computer Science 255 (2001), 125–149.
- K. Ambos-Spies, K. Weihrauch and X. Zheng, *Weakly computable real numbers*, Journal of Complexity 16 (2000), 676–690.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 5.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.8.

:::::exercises
::::exercise{#ex-left-ce-closure difficulty=1 objective="Check the closure properties of left-c.e. reals from their approximations."}
Let $\alpha$ and $\beta$ be left-c.e. reals in $[0, 1]$. Show that $\alpha + \beta$, $\alpha\beta$, $\max(\alpha, \beta)$ and $\min(\alpha, \beta)$ are left-c.e. Show that if $(\alpha^{(k)})_k$ is a sequence of reals of $[0, 1]$ that are left-c.e. uniformly in $k$, then $\sum_k 2^{-k-1} \alpha^{(k)}$ is left-c.e.

:::solution
Let $(\alpha_s)$ and $(\beta_s)$ be non-decreasing approximations with non-negative terms. Then $\alpha_s + \beta_s$, $\alpha_s \beta_s$, $\max(\alpha_s, \beta_s)$ and $\min(\alpha_s, \beta_s)$ are computable and non-decreasing, since these operations are monotone on non-negative reals, and they converge to the corresponding operations on the limits, by continuity. For the series, let $(\alpha^{(k)}_s)$ be uniformly computable non-decreasing approximations with values in $[0, 1]$ and let $p_s = \sum_{k \leq s} 2^{-k-1} \alpha^{(k)}_s$. Then $p_s \leq p_{s+1}$, as both the number of terms and each term increase. For every $k_0$, $\liminf_s p_s \geq \sum_{k \leq k_0} 2^{-k-1} \alpha^{(k)}$, and $p_s \leq \sum_k 2^{-k-1} \alpha^{(k)}$ for every $s$; letting $k_0 \to \infty$, $p_s$ converges to the sum.
:::
::::

::::exercise{#ex-computable-modulus difficulty=1 objective="Characterize the computable reals among the left-c.e. reals by a computable rate of convergence."}
Let $\alpha$ be left-c.e., with approximation $(\alpha_s)$. Show that $\alpha$ is computable if and only if there is a computable function $f$ with $\alpha - \alpha_{f(n)} < 2^{-n}$ for every $n$.

:::solution
If $f$ exists, then $\alpha_{f(n)}$ is a rational within $2^{-n}$ of $\alpha$, computed from $n$, so $\alpha$ is computable: for a rational $q \neq \alpha$, compute $\alpha_{f(n)}$ for $n = 0, 1, \dots$ until $q < \alpha_{f(n)}$, or $q \geq \alpha_{f(n)} + 2^{-n}$; this decides $L(\alpha)$ except at $q = \alpha$, and a rational $\alpha$ is computable anyway. Conversely, if $\alpha$ is computable, let $(a_n)$ be a computable sequence of rationals with $|\alpha - a_n| < 2^{-n-1}$, and let $f(n)$ be the least $s$ with $\alpha_s > a_n - 2^{-n-1}$. It exists, since $\alpha > a_n - 2^{-n-1}$ and $\alpha_s \to \alpha$, and $\alpha - \alpha_{f(n)} < \alpha - a_n + 2^{-n-1} < 2^{-n}$.
:::
::::

::::exercise{#ex-measure-least-element difficulty=2 objective="Relate left-c.e. reals to the leftmost paths of computable trees."}
Show that an irrational real $\alpha \in (0, 1)$ is left-c.e. if and only if its binary expansion is the leftmost path of an infinite computable tree.

:::solution
Let $T$ be an infinite computable tree and $X$ its leftmost path, and let $\tau_s$ be the leftmost string of length $s$ in $T$, which exists since $T$ is infinite and closed under prefixes. The string $\tau_{s+1} \uh s$ is in $T$ and has length $s$, so it is not to the left of $\tau_s$; hence $0.\tau_s \leq 0.(\tau_{s+1} \uh s) \leq 0.\tau_{s+1}$, and $(0.\tau_s)$ is a computable non-decreasing sequence of rationals. Fix $n$. A string of length $n$ to the left of $X \uh n$ has only finitely many extensions in $T$, since otherwise, by König's lemma, it would be extended by a path to the left of $X$. So for large $s$, $\tau_s \uh n$ is not to the left of $X \uh n$; and $\tau_s$ is not to the right of $X \uh s \in T$. Hence $\tau_s \uh n = X \uh n$ for large $s$, and $0.\tau_s \to 0.X$.

Conversely, let $\alpha$ be left-c.e., with approximation $(\alpha_s)$, and let $T = \{ \sigma : 0.\sigma + 2^{-|\sigma|} > \alpha_{|\sigma|} \}$. It is computable, and closed under prefixes since $0.(\sigma \uh n) + 2^{-n} \geq 0.\sigma + 2^{-|\sigma|}$ and $\alpha_n \leq \alpha_{|\sigma|}$ for $n \leq |\sigma|$. If $0.Y \geq \alpha$, then $0.(Y \uh n) + 2^{-n} \geq 0.Y \geq \alpha > \alpha_n$ for every $n$, so $Y$ is a path. If $0.Y < \alpha$, then $0.(Y \uh n) + 2^{-n}$ tends to $0.Y$ and $\alpha_n$ to $\alpha$, so $0.(Y \uh n) + 2^{-n} \leq \alpha_n$ for large $n$, and $Y$ is not a path. So the paths of $T$ are the sequences $Y$ with $0.Y \geq \alpha$. The expansion $X$ of $\alpha$ is one of them, and a sequence $Y$ to the left of $X$ satisfies $0.Y \leq 0.X$, with equality only if $0.X$ is a dyadic rational, which it is not; so $X$ is the leftmost path. (Downey–Hirschfeldt, Theorem 5.1.11.)
:::
::::
:::::
