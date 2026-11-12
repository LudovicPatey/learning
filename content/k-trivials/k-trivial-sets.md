---
title: K-trivial sets
summary: Sets whose initial segments are as simple as their lengths; Chaitin's counting theorem shows that there are countably many K-trivial sets, all of them Δ⁰₂; closure under join.
duration: 45
prerequisites: [martin-lof-randomness/levin-schnorr, kolmogorov-complexity/coding-theorem, pi01-classes/computable-members]
---

By the Levin–Schnorr theorem, a sequence is random when the complexity $K(X \uh n)$ of its initial segments is as large as possible, namely at least $n - O(1)$. This course studies the other extreme: the sets $A$ for which $K(A \uh n)$ is as small as possible. A computable set has $K(A \uh n) =^+ K(n)$ (:ref{#prop-k-segments-computable}): its initial segments contain no more information than their lengths. For plain complexity, the analogous condition characterizes the computable sets (:ref{#thm-chaitin-computable}). For prefix-free complexity it does not: the lesson on cost functions builds non-computable sets with the same complexity as computable ones. These **K-trivial** sets coincide with several notions of computational weakness relative to randomness, which is the subject of the last three lessons.

This lesson proves what can be obtained from the definition by counting descriptions: there are few K-trivial sets with a given constant, so they are all computable in $\emptyset'$; and the join of two K-trivial sets is K-trivial, by a description that pays for the common length only once.

Throughout, $K$ is the prefix-free complexity defined by an optimal prefix-free machine $U$, $\leq^+$ is inequality up to an additive constant, and a number $n$ is identified with the string associated with it, so that $K(n)$ is defined.

## Definition

:::definition{#def-k-trivial}
A set $A$ is **K-trivial** if there is a constant $b$ with $K(A \uh n) \leq K(n) + b$ for every $n$. We then say that $A$ is K-trivial **with constant** $b$.
:::

The opposite inequality $K(n) \leq^+ K(A \uh n)$ holds for every set, since $n = |A \uh n|$ is computed from $A \uh n$. So a K-trivial set is one for which $K(A \uh n) =^+ K(n)$: describing the first $n$ bits of $A$ costs no more than describing the number $n$. The function $K(n)$ is far from monotone: $K(2^k) \leq^+ K(k) \leq^+ 2 \log k$, whereas most numbers below $2^k$ have complexity at least $k - O(1)$, by counting descriptions. The definition asks that $A \uh n$ be simple exactly when $n$ is, and not only that $K(A \uh n)$ be small.

A K-trivial set is far from random: $K(A \uh n) \leq^+ K(n) \leq^+ 2 \log n$ for $n \geq 2$, by :ref{#prop-k-basic} (2), whereas a random sequence $X$ satisfies $K(X \uh n) \geq n - O(1)$ by the Levin–Schnorr theorem.

:::example{#ex-k-trivial}
1. Every computable set is K-trivial, by :ref{#prop-k-segments-computable}.
2. Chaitin's number $\Omega$ is not K-trivial: $K(\Omega \uh n) \geq n - c$ by :ref{#thm-omega}, and $n - c > 2\log n + O(1)$ for large $n$. Like a K-trivial set, $\Omega$ is computable in $\emptyset'$; the two notions are at opposite ends of the $\Delta^0_2$ sets.
3. Sets of small complexity need not be K-trivial. Let $X$ be random and $A = \{ 2^i : i \in X \}$. The prefix $A \uh n$ is computed from $n$ and $X \uh \ell$, where $\ell$ is the number of powers of $2$ below $n$, so $K(A \uh n) \leq^+ K(n) + \ell + 2 \log \ell \leq^+ 4 \log n$ by :ref{#prop-k-basic} (1) and (2), since $\ell \leq \log n + 1$. But $A$ is not K-trivial, as an exercise of the next lesson shows.
:::

:::proposition{#prop-k-trivial-basic}
1. Every computable set is K-trivial.
2. If $A$ is K-trivial, so are its complement and every finite variant of $A$.
:::

:::proof{of=prop-k-trivial-basic}
1. This is :ref{#prop-k-segments-computable}.
2. Exchanging $0$ and $1$ is a computable map sending $A \uh n$ to $\overline{A} \uh n$. If $B$ is a finite variant of $A$, then $B \uh n = h(A \uh n)$, where $h$ modifies the finitely many positions at which $A$ and $B$ differ. In both cases a computable function is applied, which increases $K$ by at most a constant.
:::

## Chaitin's counting theorem

The number of strings of length $n$ with complexity close to $K(n)$ is bounded independently of $n$. The idea is that a description of a string $\sigma$ of length $n$ is also a description of $n$, by composition with the length function. If many strings of length $n$ had descriptions of length about $K(n)$, then $n$ would have many descriptions of that length, and its algorithmic probability would be larger than $2^{-K(n)}$ by more than a constant factor, which the coding theorem forbids.

:::theorem[Chaitin]{#thm-k-trivial-count}
There is a constant $c$ such that for all $n$ and $b$, fewer than $2^{b+c}$ strings $\sigma$ of length $n$ satisfy $K(\sigma) \leq K(n) + b$.
:::

:::proof{of=thm-k-trivial-count}
Let $M$ be the prefix-free machine $\tau \mapsto |U(\tau)|$, with the same domain as $U$. By the coding theorem (:ref{#thm-coding}), there is $c$ with $P_M(n) < 2^{c - K(n)}$ for every $n$; enlarging $c$ makes the inequality strict. Let $N$ be the number of strings $\sigma$ of length $n$ with $K(\sigma) \leq K(n) + b$. A shortest description of each of them is a description of $n$ for $M$, of length at most $K(n) + b$, and these descriptions are distinct. So $N\, 2^{-K(n) - b} \leq P_M(n) < 2^{c - K(n)}$, and $N < 2^{b + c}$.
:::

:::corollary[Chaitin; Zambella]{#cor-k-trivial-delta2}
For every $b$, there are fewer than $2^{b+c}$ sets that are K-trivial with constant $b$, with $c$ as in :ref{#thm-k-trivial-count}. In particular, there are countably many K-trivial sets, and every K-trivial set is $\Delta^0_2$.
:::

:::proof{of=cor-k-trivial-delta2}
If $A_0, \dots, A_{N-1}$ are distinct sets that are K-trivial with constant $b$, their prefixes of some length $n$ are pairwise distinct, and they are $N$ strings of length $n$ with $K(\sigma) \leq K(n) + b$. So $N < 2^{b+c}$.

The function $K$ is computable in $\emptyset'$, since $K(\sigma) \leq k$ is a $\Sigma^0_1$ property of $(\sigma, k)$. So the set $T_b$ of strings $\sigma$ with $K(\sigma \uh m) \leq K(m) + b$ for every $m \leq |\sigma|$ is a tree computable in $\emptyset'$, and its paths are the sets that are K-trivial with constant $b$. The class $[T_b]$ is finite, so each of its members is isolated. By :ref{#prop-isolated-computable} relativized to $\emptyset'$, each member of $[T_b]$ is computable in $\emptyset'$.
:::

:::figure[The shape of the tree $T_b$. Each level has fewer than $2^{b+c}$ nodes, by the counting theorem, so $T_b$ has fewer than $2^{b+c}$ paths. Below the dashed line the paths are separated: a node there extends to at most one path, and $\emptyset'$, which decides membership in $T_b$, can follow a path by discarding the nodes whose subtree is finite.]
<svg class="fig" viewBox="0 0 600 320" width="600" role="img" aria-label="A tree with at most three nodes at each level, two infinite paths that separate at level 4, and a branch through 1 that dies at level 5"><line x1="225.0" y1="22" x2="122.5" y2="56" class="accent-stroke" stroke-width="2"/><line x1="225.0" y1="22" x2="327.5" y2="56" class="ink-stroke" stroke-width="1.1"/><line x1="122.5" y1="56" x2="71.2" y2="90" class="accent-stroke" stroke-width="2"/><line x1="327.5" y1="56" x2="276.2" y2="90" class="ink-stroke" stroke-width="1.1"/><line x1="71.2" y1="90" x2="96.9" y2="124" class="accent-stroke" stroke-width="2"/><line x1="276.2" y1="90" x2="250.6" y2="124" class="ink-stroke" stroke-width="1.1"/><line x1="96.9" y1="124" x2="84.1" y2="158" class="accent-stroke" stroke-width="2"/><line x1="96.9" y1="124" x2="109.7" y2="158" class="accent-stroke" stroke-width="2"/><line x1="250.6" y1="124" x2="263.4" y2="158" class="ink-stroke" stroke-width="1.1"/><line x1="84.1" y1="158" x2="90.5" y2="192" class="accent-stroke" stroke-width="2"/><line x1="109.7" y1="158" x2="103.3" y2="192" class="accent-stroke" stroke-width="2"/><line x1="263.4" y1="158" x2="257.0" y2="192" class="ink-stroke" stroke-width="1.1"/><line x1="90.5" y1="192" x2="93.7" y2="226" class="accent-stroke" stroke-width="2"/><line x1="103.3" y1="192" x2="106.5" y2="226" class="accent-stroke" stroke-width="2"/><line x1="93.7" y1="226" x2="92.1" y2="260" class="accent-stroke" stroke-width="2"/><line x1="106.5" y1="226" x2="104.9" y2="260" class="accent-stroke" stroke-width="2"/><circle cx="225.0" cy="22" r="4" class="accent-fill"/><circle cx="122.5" cy="56" r="4" class="accent-fill"/><circle cx="327.5" cy="56" r="4" class="ink-fill"/><circle cx="71.2" cy="90" r="4" class="accent-fill"/><circle cx="276.2" cy="90" r="4" class="ink-fill"/><circle cx="96.9" cy="124" r="4" class="accent-fill"/><circle cx="250.6" cy="124" r="4" class="ink-fill"/><circle cx="84.1" cy="158" r="4" class="accent-fill"/><circle cx="109.7" cy="158" r="4" class="accent-fill"/><circle cx="263.4" cy="158" r="4" class="ink-fill"/><circle cx="90.5" cy="192" r="4" class="accent-fill"/><circle cx="103.3" cy="192" r="4" class="accent-fill"/><circle cx="257.0" cy="192" r="4" class="ink-fill"/><line x1="250.0" y1="201" x2="264.0" y2="201" class="ink-stroke" stroke-width="1.4"/><circle cx="93.7" cy="226" r="4" class="accent-fill"/><circle cx="106.5" cy="226" r="4" class="accent-fill"/><circle cx="92.1" cy="260" r="4" class="accent-fill"/><circle cx="104.9" cy="260" r="4" class="accent-fill"/><text x="92.1" y="282" text-anchor="middle" class="mrm" font-size="13">⋮</text><text x="104.9" y="282" text-anchor="middle" class="mrm" font-size="13">⋮</text><text x="470" y="26" class="label">level 0: 1 node</text><text x="470" y="60" class="label">level 1: 2 nodes</text><text x="470" y="94" class="label">level 2: 2 nodes</text><text x="470" y="128" class="label">level 3: 2 nodes</text><text x="470" y="162" class="label">level 4: 3 nodes</text><text x="470" y="196" class="label">level 5: 3 nodes</text><text x="470" y="230" class="label">level 6: 2 nodes</text><text x="470" y="264" class="label">level 7: 2 nodes</text><line x1="20" y1="141" x2="590" y2="141" class="muted-stroke" stroke-width="1" stroke-dasharray="4 3"/><text x="20" y="304" class="label">accent: the two infinite paths; bars: nodes without successors</text></svg>
:::

The tree $T_b$ may have nodes without infinite extensions, and $\emptyset'$ cannot recognize them in general; the argument of :ref{#prop-isolated-computable} only uses that the number of paths is finite. The same argument, applied to $C$ in place of $K$, is the first step of the proof of Chaitin's theorem on plain complexity; there, a further argument shows that the members of the corresponding tree are computable. For $K$ no such argument exists, since non-computable K-trivial sets exist. Both parts of the proof use the counting theorem as a compactness principle: a constant bound on the width of a tree turns a property of all initial segments into a finite set of candidates.

:::quiz[the counting theorem]
In the proof of :ref{#thm-k-trivial-count}, why is the machine $M = |U|$ prefix-free?

- [x] Because its domain is the domain of $U$, which is prefix-free; the output is changed, not the domain.
- [ ] Because the length function is injective.

  It is not injective; many strings have the same length, which is precisely why $P_M(n)$ collects many descriptions.
- [ ] Because $M$ only accepts shortest descriptions.

  $M$ accepts every element of the domain of $U$.

---

In the proof of :ref{#cor-k-trivial-delta2}, why is each member of $[T_b]$ isolated?

- [x] Because $[T_b]$ is finite: the distinct members differ at some position, and a long enough prefix of a member is extended by no other member.
- [ ] Because $T_b$ is computable in $\emptyset'$.

  Computability of the tree does not make its paths isolated; finiteness does.
- [ ] Because K-trivial sets are computable.

  Some K-trivial sets are not computable, as shown in the lesson on cost functions.
:::

## Closure under join

The counting theorem allows one to describe $A \uh n$ by a shortest description of $n$ followed by a bounded amount of information: the position of $A \uh n$ in an enumeration of the fewer than $2^{b+c}$ candidates.

:::proposition{#prop-k-trivial-join}
If $A$ and $B$ are K-trivial, then $A \oplus B$ is K-trivial.
:::

:::proof{of=prop-k-trivial-join}
Let $b$ be a common constant for $A$ and $B$, $c$ as in :ref{#thm-k-trivial-count}, and $k = b + c$. For a string $\tau$ in the domain of $U$ with $U(\tau) = n$, let $S_\tau$ be the set of strings $\sigma$ of length $n$ with $K(\sigma) \leq |\tau| + b$, listed in the order in which they are found by a fixed enumeration; this list is c.e. uniformly in $\tau$. If $\tau$ is a shortest description of $n$, then $|S_\tau| < 2^k$, and $A \uh n$ and $B \uh n$ belong to $S_\tau$.

Let $M$ be the machine that, on input $\tau \beta \gamma$ with $\tau$ in the domain of $U$ and $|\beta| = |\gamma| = k$, reads $\beta$ and $\gamma$ as numbers $i, j < 2^k$, waits for the $i$-th and $j$-th elements $\sigma, \sigma'$ of the list $S_\tau$, and outputs the interleaving $\sigma \oplus \sigma'$ of length $2n$. Its domain is prefix-free, by the argument of :ref{#prop-k-basic} (1). With $\tau$ a shortest description of $n$, and $\beta, \gamma$ the positions of $A \uh n$ and $B \uh n$ in the list, $M(\tau\beta\gamma) = (A \oplus B) \uh 2n$. Hence
$$
K((A \oplus B) \uh 2n) \leq^+ K(n) + 2k.
$$
For an arbitrary length $m$, let $n = \lceil m/2 \rceil$. The string $(A \oplus B) \uh m$ is $(A \oplus B) \uh 2n$ if $m$ is even, and this string with its last bit removed if $m$ is odd; both operations are computable and do not require knowing $m$, so $K((A \oplus B) \uh m) \leq^+ K((A \oplus B) \uh 2n)$. Since $n$ is computed from $m$, $K(n) \leq^+ K(m)$. So $K((A \oplus B) \uh m) \leq^+ K(m)$.
:::

The direct estimate $K(\langle \sigma, \sigma' \rangle) \leq^+ K(\sigma) + K(\sigma')$ only gives $2K(n)$; the proof avoids describing $n$ twice. Closure under weak truth-table reducibility is proved in the next lesson. Closure under Turing reducibility, the other half of the statement that the K-trivial sets form an ideal, is much harder; it is a consequence of the main theorem of the last lesson.

:::quiz[closure under join]
In the proof of :ref{#prop-k-trivial-join}, why is the list $S_\tau$ enumerated rather than computed?

- [x] Because $K(\sigma) \leq |\tau| + b$ is only a $\Sigma^0_1$ property: the strings satisfying it can be listed, but one cannot know when the list is complete. The machine only needs to wait for the $i$-th element.
- [ ] Because $S_\tau$ is infinite.

  $S_\tau$ is a set of strings of length $n$, hence finite.
- [ ] Because $\tau$ is not a shortest description.

  The argument uses a shortest description $\tau$; the enumeration is needed whatever $\tau$ is.

---

Why are the indices $\beta$ and $\gamma$ written with exactly $k$ bits?

- [x] To keep the domain of $M$ prefix-free: after $\tau$, the machine knows that exactly $2k$ further bits must be read.
- [ ] Because $A \uh n$ is the $k$-th element of the list.

  Its position is some $i < 2^k$, which needs at most $k$ bits; the fixed length is about self-delimitation.
- [ ] Because $k$ is the complexity of $n$.

  $k = b + c$ is a constant, independent of $n$.
:::

## Exercises

::::exercise{difficulty=1}
Let $S$ be an infinite computable set, and suppose that $K(A \uh n) \leq K(n) + b$ for every $n \in S$. Show that $A$ is K-trivial.

:::solution
Let $h(n)$ be the $n$-th element of $S$ in increasing order; $h$ is computable and strictly increasing, so $h(n) \geq n$. Given $A \uh h(n)$, one computes its length $h(n)$, then $n$, then $A \uh n$ by truncation; so $K(A \uh n) \leq^+ K(A \uh h(n))$. Hence $K(A \uh n) \leq^+ K(A \uh h(n)) \leq K(h(n)) + b \leq^+ K(n)$, since $h(n)$ is computed from $n$.
:::
::::

::::exercise{difficulty=2}
Show that there is a constant $c'$ such that for every large enough $b$, at least $2^{b - 2 \log b - c'}$ sets are K-trivial with constant $b$. Compare with :ref{#cor-k-trivial-delta2}.

:::hint
For a string $\sigma$, consider the finite set $\sigma 0^\infty$, and bound its constant of K-triviality by $K(\sigma)$.
:::

:::solution
The prefix of length $n$ of $\sigma 0^\infty$ is computed from $\langle \sigma, n \rangle$: it is $\sigma \uh n$ if $n \leq |\sigma|$, and $\sigma 0^{n - |\sigma|}$ otherwise. By :ref{#prop-k-basic} (1), there is $r$ with $K((\sigma 0^\infty) \uh n) \leq K(\sigma) + K(n) + r$ for all $\sigma$ and $n$, so $\sigma 0^\infty$ is K-trivial with constant $K(\sigma) + r$. By :ref{#prop-k-basic} (2), there is $r'$ with $K(\sigma) \leq |\sigma| + 2 \log |\sigma| + r'$ for $|\sigma| \geq 2$. Let $\ell = b - \lceil 2 \log b \rceil - r - r'$. For $b$ large enough, $\ell \geq 2$ and $\ell + 2 \log \ell + r' + r \leq b$, so the $2^\ell$ sets $\sigma 0^\infty$ with $|\sigma| = \ell$ are K-trivial with constant $b$, and they are pairwise distinct. So there are at least $2^{b - 2 \log b - r - r' - 1}$ of them. The upper bound of :ref{#cor-k-trivial-delta2} is $2^{b + c}$: the number of sets that are K-trivial with constant $b$ is $2^{b - O(\log b)}$.
:::
::::

## Notes and references

Chaitin (1975) proved the counting theorem for prefix-free complexity, in the form "at most $2^{n - r + O(1)}$ strings of length $n$ have $K(\sigma) \leq n + K(n) - r$", of which :ref{#thm-k-trivial-count} is the case $r = n - b$. Chaitin (1977) proved that K-trivial sets are $\Delta^0_2$; Nies attributes this result, and the finiteness of the classes $[T_b]$, to Chaitin (1976), while Downey and Hirschfeldt attribute the bound $O(2^b)$ on the number of sets that are K-trivial with constant $b$ to Zambella (1990). The lower bound of the second exercise and the finer estimates of the function $b \mapsto |[T_b]|$ are due to Downey, Miller and Yu (Downey and Hirschfeldt, Section 11.1.4). A non-computable K-trivial set was first built by Solovay (1975), in an unpublished manuscript; the lesson on cost functions gives the cost function form of the construction. The closure under join is due to Downey, Hirschfeldt, Nies and Stephan (2003).

The basic facts of the lesson are in Nies, *Computability and Randomness*, Section 5.2 (Definition 5.2.1, Theorems 5.2.4 and 5.2.17), with the counting theorem as Theorem 2.2.26, and in Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Section 11.1 (Theorems 11.1.1 and 11.1.3, Proposition 11.1.4, Theorems 11.1.10 and 11.1.11), with the counting theorem as Theorem 3.7.6.

- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- G. J. Chaitin, *Information-theoretic characterizations of recursive infinite strings*, Theoretical Computer Science 2 (1976), 45–48.
- G. J. Chaitin, *Algorithmic information theory*, IBM Journal of Research and Development 21 (1977), 350–359, 496.
- D. Zambella, *On sequences with simple initial segments*, ILLC Technical Report ML-1990-05, University of Amsterdam, 1990.
- R. G. Downey, D. R. Hirschfeldt, A. Nies and F. Stephan, *Trivial reals*, in: Proceedings of the 7th and 8th Asian Logic Conferences, 2003, 103–131.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 2.2 and 5.2.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.7 and 11.1.
