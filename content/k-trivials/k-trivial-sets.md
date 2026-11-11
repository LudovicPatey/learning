---
title: K-trivial sets
summary: Sets whose initial segments are as simple as their lengths; Chaitin's counting theorem shows that there are countably many K-trivial sets, all of them Δ⁰₂; closure under join; Solovay functions and a characterization of K-triviality by a computable bound.
duration: 40
prerequisites: [martin-lof-randomness/levin-schnorr, kolmogorov-complexity/coding-theorem, pi01-classes/computable-members]
---

By the Levin–Schnorr theorem, a sequence is random when the complexity $K(X \uh n)$ of its initial segments is as large as possible, namely at least $n - O(1)$. This course studies the other extreme: the sets $A$ for which $K(A \uh n)$ is as small as possible. A computable set has $K(A \uh n) =^+ K(n)$ (:ref{#prop-k-segments-computable}): its initial segments contain no more information than their lengths. For plain complexity, the analogous condition characterizes the computable sets (:ref{#thm-chaitin-computable}). For prefix-free complexity it does not: the next lesson builds non-computable sets with the same complexity as computable ones. These **K-trivial** sets coincide with several notions of computational weakness relative to randomness, which is the subject of the last lesson.

Throughout, $K$ is the prefix-free complexity defined by an optimal prefix-free machine $U$, $\leq^+$ is inequality up to an additive constant, and a number $n$ is identified with the string associated with it, so that $K(n)$ is defined.

## Definition

:::definition{#def-k-trivial}
A set $A$ is **K-trivial** if there is a constant $b$ with $K(A \uh n) \leq K(n) + b$ for every $n$. We then say that $A$ is K-trivial **with constant** $b$.
:::

The opposite inequality $K(n) \leq^+ K(A \uh n)$ holds for every set, since $n = |A \uh n|$ is computed from $A \uh n$. A K-trivial set is far from random: $K(A \uh n) \leq^+ K(n) \leq^+ 2 \log n$ for $n \geq 2$, by :ref{#prop-k-basic} (2), whereas a random sequence $X$ satisfies $K(X \uh n) \geq n - O(1)$ by the Levin–Schnorr theorem.

:::proposition{#prop-k-trivial-basic}
1. Every computable set is K-trivial.
2. If $A$ is K-trivial, so are its complement and every finite variant of $A$.
:::

:::proof{of=prop-k-trivial-basic}
1. This is :ref{#prop-k-segments-computable}.
2. Exchanging $0$ and $1$ is a computable map sending $A \uh n$ to $\overline{A} \uh n$. If $B$ is a finite variant of $A$, then $B \uh n = h(A \uh n)$, where $h$ modifies the finitely many positions at which $A$ and $B$ differ. In both cases a computable function is applied, which increases $K$ by at most a constant.
:::

## Chaitin's counting theorem

The number of strings of length $n$ with complexity close to $K(n)$ is bounded independently of $n$.

:::theorem[Chaitin]{#thm-k-trivial-count}
There is a constant $c$ such that for all $n$ and $b$, fewer than $2^{b+c}$ strings $\sigma$ of length $n$ satisfy $K(\sigma) \leq K(n) + b$.
:::

:::proof{of=thm-k-trivial-count}
Let $M$ be the prefix-free machine $\tau \mapsto |U(\tau)|$, with the same domain as $U$. By the coding theorem (:ref{#thm-coding}), there is $c$ with $P_M(n) < 2^{c - K(n)}$ for every $n$; enlarging $c$ makes the inequality strict. Let $N$ be the number of strings $\sigma$ of length $n$ with $K(\sigma) \leq K(n) + b$. A shortest description of each of them is a description of $n$ for $M$, of length at most $K(n) + b$, and these descriptions are distinct. So $N\, 2^{-K(n) - b} \leq P_M(n) < 2^{c - K(n)}$, and $N < 2^{b + c}$.
:::

:::corollary[Chaitin]{#cor-k-trivial-delta2}
For every $b$, there are fewer than $2^{b+c}$ sets that are K-trivial with constant $b$, with $c$ as in :ref{#thm-k-trivial-count}. In particular, there are countably many K-trivial sets, and every K-trivial set is $\Delta^0_2$.
:::

:::proof{of=cor-k-trivial-delta2}
If $A_0, \dots, A_{N-1}$ are distinct sets that are K-trivial with constant $b$, their prefixes of some length $n$ are pairwise distinct, and they are $N$ strings of length $n$ with $K(\sigma) \leq K(n) + b$. So $N < 2^{b+c}$.

The function $K$ is computable in $\emptyset'$, since $K(\sigma) \leq k$ is a $\Sigma^0_1$ property of $(\sigma, k)$. So the set $T_b$ of strings $\sigma$ with $K(\sigma \uh m) \leq K(m) + b$ for every $m \leq |\sigma|$ is a tree computable in $\emptyset'$, and its paths are the sets that are K-trivial with constant $b$. The class $[T_b]$ is finite, so each of its members is isolated. By :ref{#prop-isolated-computable} relativized to $\emptyset'$, each member of $[T_b]$ is computable in $\emptyset'$.
:::

The same argument, applied to $C$ in place of $K$, is the first step of the proof of Chaitin's theorem on plain complexity; there, a further argument shows that the members of the corresponding tree are computable. For $K$ no such argument exists, since non-computable K-trivial sets exist.

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

  Some K-trivial sets are not computable, as shown in the next lesson.
:::

## Closure under join

The counting theorem allows one to describe $A \uh n$ by a shortest description of $n$ followed by a bounded amount of information.

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

The direct estimate $K(\langle \sigma, \sigma' \rangle) \leq^+ K(\sigma) + K(\sigma')$ only gives $2K(n)$; the proof avoids describing $n$ twice. Closure under Turing reducibility, the other half of the statement that the K-trivial sets form an ideal, is much harder; it is a consequence of the main theorem of the last lesson.

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

## Solovay functions

The function $K$ is not computable, but some computable functions bound it from above and agree with it, up to a constant, infinitely often.

:::definition{#def-solovay-function}
A **Solovay function** is a computable function $g : \nat \to \nat$ such that $K(m) \leq^+ g(m)$ for every $m$, and $g(m) \leq^+ K(m)$ for infinitely many $m$.
:::

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

Since $g$ is computable and $K$ is approximable from above, the strings $\sigma$ with $K(\sigma \uh m) \leq g(m) + c$ for every $m \leq |\sigma|$ form a c.e. tree, whose paths are exactly the sets satisfying the bound of the proposition with constant $c$; they are all K-trivial. Nies proved that every K-trivial set is computable from a c.e. K-trivial set, with the cost function method and the golden run construction mentioned in the last lesson; the c.e. trees above give another proof, based on the fact that a K-trivial set is an isolated path of such a tree. This theorem is admitted here (see Nies, *Lowness properties and randomness*, 2005, and Nies, *Computability and Randomness*, Chapter 5).

## Exercises

::::exercise{difficulty=1}
Show that if $A$ is K-trivial and $f$ is a computable strictly increasing function, then the set $B = \{ n : f(n) \in A \}$ is K-trivial.

:::solution
For $n \geq 1$, the string $B \uh n$ is computed from $A \uh (f(n-1) + 1)$, by reading the bits at positions $f(0), \dots, f(n-1)$. Let $h(0) = 0$ and $h(n) = f(n-1) + 1$ for $n \geq 1$, a computable strictly increasing function. Given the string $A \uh h(n)$, one computes its length $h(n)$, then $n$ as the unique number with this image under $h$, then $B \uh n$; so $K(B \uh n) \leq^+ K(A \uh h(n))$. Hence $K(B \uh n) \leq^+ K(A \uh h(n)) \leq^+ K(h(n)) \leq^+ K(n)$, since $h(n)$ is computed from $n$.
:::
::::

::::exercise{difficulty=1}
Show that no K-trivial set is Martin-Löf random, and that if $A$ is K-trivial and $Z$ is random, then $A \oplus Z$ is not K-trivial.

:::solution
A random set satisfies $K(Z \uh n) \geq n - O(1)$, whereas a K-trivial set satisfies $K(A \uh n) \leq^+ 2 \log n$; so no set is both. If $A \oplus Z$ were K-trivial, then $Z$ would be K-trivial as well: $Z = \{ n : 2n + 1 \in A \oplus Z \}$, and the first exercise applies with $f(n) = 2n + 1$. This contradicts the first statement.
:::
::::

## Notes and references

K-trivial sets appear in the work of Chaitin (1977), who proved :ref{#cor-k-trivial-delta2}, and in Solovay's unpublished manuscript (1975), which contains the construction of a non-computable K-trivial set given in the next lesson. The closure under join is due to Downey, Hirschfeldt, Nies and Stephan (2003). Solovay functions were studied by Bienvenu and Downey (2009), and Bienvenu, Merkle and Nies (2011) showed that every Solovay function can replace $K$ in the definition of K-triviality.

- G. J. Chaitin, *Algorithmic information theory*, IBM Journal of Research and Development 21 (1977), 350–359.
- R. G. Downey, D. R. Hirschfeldt, A. Nies and F. Stephan, *Trivial reals*, in: Proceedings of the 7th and 8th Asian Logic Conferences, 2003, 103–131.
- L. Bienvenu and R. Downey, *Kolmogorov complexity and Solovay functions*, STACS 2009, 147–158.
- L. Bienvenu, W. Merkle and A. Nies, *Solovay functions and K-triviality*, STACS 2011.
- A. Nies, *Lowness properties and randomness*, Advances in Mathematics 197 (2005), 274–305.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009.
