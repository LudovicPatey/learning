---
title: Complexity of initial segments
summary: The complexity of the initial segments of an infinite sequence; computable sequences have minimal complexity; every sequence has prefixes compressible by any constant; the lower envelope of the complexity of numbers.
duration: 35
prerequisites: [plain-complexity]
---

An infinite binary sequence $X$ is described by its initial segments $X \uh n$. If $X$ is computable, these segments carry no more information than their length. One would like to call $X$ random when, on the contrary, its initial segments are incompressible. This lesson shows that plain complexity is not suited to this purpose: every sequence, however irregular, has initial segments compressible by any given constant. The reason is that a description of length $\ell$ also conveys the number $\ell$; the next lesson removes this effect.

## Computable sequences

:::proposition{#prop-computable-segments}
If $X$ is computable, then $C(X \uh n) =^+ C(n)$. In particular $C(X \uh n) \leq^+ \log n$ for $n \geq 1$.
:::

:::proof{of=prop-computable-segments}
The function $n \mapsto X \uh n$ is computable, so $C(X \uh n) \leq^+ C(n)$ by :ref{#prop-c-basic}. The function $\sigma \mapsto |\sigma|$ is computable, so $C(n) \leq^+ C(X \uh n)$.
:::

Chaitin proved the converse, a characterization of the computable sequences by the complexity of their initial segments. Its proof requires a counting lemma on the number of descriptions of a string and a careful analysis of c.e. trees of bounded width; it is admitted here.

:::theorem[Chaitin]{#thm-chaitin-computable}
For a sequence $X$, the following are equivalent:

1. $X$ is computable;
2. $C(X \uh n) \leq^+ C(n)$;
3. $C(X \uh n) \leq^+ \log n$, for $n \geq 1$.
:::

The implications (1 ⇒ 2 ⇒ 3) follow from :ref{#prop-computable-segments} and $C(n) \leq^+ \log n$. For (3 ⇒ 1), see the book of Downey and Hirschfeldt, Section 3.4, or Li and Vitányi, Section 2.3. An exercise below shows that $\log n$ cannot be replaced by $2 \log n$: the characteristic sequence of a c.e. set satisfies $C(A \uh n) \leq^+ 2 \log n$.

## Oscillation

:::theorem[Martin-Löf]{#thm-oscillation}
For every sequence $X$ and every $k$, there are infinitely many $n$ with $C(X \uh n) \leq n - k$.
:::

:::proof{of=thm-oscillation}
Let $M$ be the machine that, on input $\alpha$, outputs $\beta\alpha$, where $\beta$ is the string associated with the number $|\alpha|$. Let $c$ be such that $C \leq C_M + c$.

Let $m \geq k + c$. Let $\beta = X \uh m$, and let $N$ be the number associated with $\beta$, so that $N \geq 2^m - 1$. Let $\alpha$ be the string of length $N$ such that $\beta\alpha = X \uh (m + N)$. Since the string associated with $|\alpha| = N$ is $\beta$, $M(\alpha) = \beta\alpha = X \uh (m + N)$. Hence
$$
C(X \uh (m + N)) \leq N + c = (m + N) - m + c \leq (m + N) - k.
$$
Each $m \geq k + c$ gives a length $n = m + N \geq m + 2^m - 1$; these lengths are unbounded, so there are infinitely many of them.
:::

The prefix $X \uh m$, read as a number $N$, announces the length of the next block. A description of the block alone then suffices, since its length restores the prefix. The proof gives more: the deficiency at length $n = m + N$ is $m - c$, and $m$ is about $\log N$, so $C(X \uh n) \leq n - \log n + O(1)$ for infinitely many $n$.

:::corollary{#cor-no-c-random}
No sequence $X$ satisfies $C(X \uh n) \geq n - c$ for every $n$, whatever the constant $c$.
:::

The incompressible strings of :ref{#prop-incompressible-count} cannot be the initial segments of a single sequence at all lengths. A definition of random sequences through compressibility must use another complexity. Prefix-free complexity, introduced in the next lesson, does not suffer from this effect, and a sequence is random in the sense of the following course when $K(X \uh n) \geq n - c$ for all $n$.

:::quiz[the oscillation theorem]
In the proof of :ref{#thm-oscillation}, why can the machine $M$ recover $X \uh m$ from $\alpha$ alone?

- [x] Because $\alpha$ was chosen of length $N$, the number coded by $X \uh m$; the length of the input is information available to the machine.
- [ ] Because $X$ is computable.

  The theorem holds for every sequence $X$; the machine $M$ does not depend on $X$.
- [ ] Because $\alpha$ contains $X \uh m$ as a prefix.

  $\alpha$ is the block following $X \uh m$, not a string containing it.

---

Why does the argument not show that $C(X \uh n) \leq n - k$ for all large $n$?

- [x] Because it only applies at the lengths $m + N$ determined by the prefixes of $X$; at other lengths, initial segments may be incompressible.
- [ ] Because the constant $c$ depends on $X$.

  The constant $c$ depends only on the machine $M$, which is the same for all sequences.
- [ ] Because $m$ must be larger than $N$.

  On the contrary, $N \geq 2^m - 1$ is much larger than $m$.
:::

## The lower envelope of the complexity of numbers

For each $k$, only finitely many numbers $n$ satisfy $C(n) \leq k$, since they have descriptions of length at most $k$. So $C(n)$ tends to infinity. It does so more slowly than any computable function tending to infinity.

:::theorem[Kolmogorov]{#thm-c-envelope}
Let $\mu(n) = \min \{ C(m) : m \geq n \}$. Then $\mu$ is non-decreasing and unbounded. For every total computable non-decreasing unbounded function $\varphi$, $\mu(n) < \varphi(n)$ for all large enough $n$.
:::

:::proof{of=thm-c-envelope}
The function $\mu$ is non-decreasing by definition, and unbounded since $\{ m : C(m) \leq k \}$ is finite for each $k$.

Let $h(k)$ be the least $x$ with $\varphi(x) > k$; it is total computable, since $\varphi$ is unbounded. By :ref{#prop-c-basic}, there is $c$ with $C(h(k)) \leq \log (k + 1) + c$ for every $k$. Let $n \geq h(0)$, and let $k$ be such that $h(k) \leq n < h(k+1)$; it exists since $h$ is non-decreasing and unbounded. Then $\varphi(n) > k$, since $n \geq h(k)$, and $h(k+1) \geq n$, so $\mu(n) \leq C(h(k+1)) \leq \log(k + 2) + c$. For $n$ large, $k$ is large, and $\log(k + 2) + c < k < \varphi(n)$.
:::

In particular, $C(n)$ is small for infinitely many $n$ in a range where $\log n$ is large: $C(2^{2^j}) \leq^+ \log j$, for instance. The function $\mu$ is a typical example of a function that tends to infinity, but slower than every computable function tending to infinity; it is computable in $\emptyset'$.

:::quiz[the lower envelope]
In the proof of :ref{#thm-c-envelope}, why does the number $h(k+1)$ have small complexity?

- [x] Because it is computed from $k + 1$ by a fixed algorithm, so its complexity is at most that of $k + 1$ up to a constant, which is at most about $\log k$.
- [ ] Because $h(k + 1)$ is small.

  It may be very large; its complexity is small because it has a short description.
- [ ] Because $\varphi$ is non-decreasing.

  Monotonicity is used to locate $n$ between $h(k)$ and $h(k+1)$, not to bound the complexity.
:::

## Exercises

::::exercise{difficulty=1}
Show that for every $c$ there are strings $\sigma$, $\tau$ with $C(\sigma\tau) > C(\sigma) + C(\tau) + c$.

:::solution
Let $M$ and $c_M$ be as in the proof of :ref{#thm-oscillation}, and $d$ such that $C(\rho) \leq |\rho| + d$ for every $\rho$. Let $m > c + c_M + d$ and $L = m + 2^{m+1}$. Let $\gamma$ be a string of length $L$ with $C(\gamma) \geq L$ (:ref{#prop-incompressible-count}). Let $N$ be the number associated with $\gamma \uh m$; then $N < 2^{m+1} - 1$, so $m + N \leq L$. Write $\gamma = \sigma\tau$ with $|\sigma| = m + N$. As in the proof of the theorem, $C(\sigma) \leq |\sigma| - m + c_M$, and $C(\tau) \leq |\tau| + d$. Hence $C(\sigma) + C(\tau) + c \leq L - m + c_M + d + c < L \leq C(\sigma\tau)$.
:::
::::

::::exercise{difficulty=2}
Let $A$ be a c.e. set. Show that $C(A \uh n) \leq^+ 2 \log n$ for $n \geq 1$.

:::hint
$A \uh n$ is determined by $n$ and the number of elements of $A$ below $n$. Code these two numbers by two strings whose lengths are linked, so that no separator is needed.
:::

:::solution
Let $k = |A \cap \{0, \dots, n-1\}|$. Given $n$ and $k$, enumerate $A$ until $k$ elements smaller than $n$ have appeared; these are exactly the elements of $A$ below $n$, so $A \uh n$ is computed. Let $\beta$ be the string associated with $n$, of length $\ell = \lfloor \log(n+1) \rfloor$, and let $\kappa$ be the binary representation of $k$ padded with leading zeros to length $\ell + 1$; this is possible since $k \leq n < 2^{\ell + 1}$. The machine that, on an input of odd length $2\ell + 1$, splits it into $\beta$ of length $\ell$ and $\kappa$ of length $\ell + 1$, and runs the enumeration above, outputs $A \uh n$ on the input $\beta\kappa$. So $C(A \uh n) \leq^+ 2\ell + 1 \leq^+ 2 \log n$. Since non-computable c.e. sets exist, this shows that the bound $\log n$ of :ref{#thm-chaitin-computable} cannot be replaced by $2 \log n$.
:::
::::

## Notes and references

The oscillation theorem is due to Martin-Löf (1966), who introduced at the same time the definition of randomness through effective tests, treated in the next course. Chaitin's characterization of the computable sequences dates from 1976; a form with conditional complexity is due to Loveland (1969). The bound for c.e. sets is due to Barzdin (1968). The lower envelope theorem is in Zvonkin and Levin's survey (1970).

- P. Martin-Löf, *The definition of random sequences*, Information and Control 9 (1966), 602–619.
- G. J. Chaitin, *Information-theoretic characterizations of recursive infinite strings*, Theoretical Computer Science 2 (1976), 45–48.
- A. K. Zvonkin and L. A. Levin, *The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms*, Russian Mathematical Surveys 25 (1970), 83–124.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010.
