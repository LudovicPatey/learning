---
title: Complexity of initial segments
summary: Computable sequences have initial segments of minimal complexity; every sequence has initial segments compressible by any constant, so plain complexity does not define random sequences.
duration: 30
prerequisites: [non-computability]
---

An infinite binary sequence $X$ is described by its initial segments $X \uh n$. If $X$ is computable, these segments carry no more information than their length. One would like to call $X$ random when, on the contrary, its initial segments are incompressible. This lesson studies the two extremes. At the low end, computable sequences have initial segments of minimal complexity; the next lesson proves Chaitin's converse. At the high end, the oscillation theorem shows that plain complexity is not suited to the definition of randomness: every sequence, however irregular, has initial segments compressible by any given constant. The reason is that a description of length $\ell$ also conveys the number $\ell$; the lesson on prefix-free complexity removes this effect.

## Computable sequences

:::proposition{#prop-computable-segments}
If $X$ is computable, then $C(X \uh n) =^+ C(n)$. In particular $C(X \uh n) \leq^+ \log n$ for $n \geq 1$.
:::

:::proof{of=prop-computable-segments}
The function $n \mapsto X \uh n$ is computable, so $C(X \uh n) \leq^+ C(n)$ by :ref{#prop-c-basic}. The function $\sigma \mapsto |\sigma|$ is computable, so $C(n) \leq^+ C(X \uh n)$.
:::

The constant depends on $X$: it is essentially the length of a program for $X$. Chaitin proved the converse: if $C(X \uh n) \leq^+ \log n$, then $X$ is computable (:ref{#thm-chaitin-computable}, proved in the next lesson). The bound $\log n$ cannot be replaced by $2 \log n$: an exercise below shows that the characteristic sequence of every c.e. set $A$ satisfies $C(A \uh n) \leq^+ 2 \log n$.

::::exercise{#ex-barzdins difficulty=2 objective="Use the enumeration of a c.e. set to describe its initial segments with about $2 \log n$ bits."}
Let $A$ be a c.e. set. Show that $C(A \uh n) \leq^+ 2 \log n$ for $n \geq 1$.

:::hint
$A \uh n$ is determined by $n$ and the number of elements of $A$ below $n$. Code these two numbers by two strings whose lengths are linked, so that no separator is needed.
:::

:::solution
Let $k = |A \cap \{0, \dots, n-1\}|$. Given $n$ and $k$, enumerate $A$ until $k$ elements smaller than $n$ have appeared; these are exactly the elements of $A$ below $n$, so $A \uh n$ is computed. Let $\beta$ be the string associated with $n$, of length $\ell = \lfloor \log(n+1) \rfloor$, and let $\kappa$ be the binary representation of $k$ padded with leading zeros to length $\ell + 1$; this is possible since $k \leq n < 2^{\ell + 1}$. The machine that, on an input of odd length $2\ell + 1$, splits it into $\beta$ of length $\ell$ and $\kappa$ of length $\ell + 1$, and runs the enumeration above, outputs $A \uh n$ on the input $\beta\kappa$. So $C(A \uh n) \leq^+ 2\ell + 1 \leq^+ 2 \log n$. Since non-computable c.e. sets exist, this shows that the bound $\log n$ of Chaitin's characterization of the computable sequences, proved in the next lesson, cannot be replaced by $2 \log n$.
:::
::::

## Oscillation

At the other extreme, one would like random sequences to satisfy $C(X \uh n) \geq n - c$ for every $n$. No sequence does. The idea of the proof is that an initial segment $X \uh m$, read as a number $N$, can serve as the length of the following block of $X$: a description of that block alone, of length $N$, then also conveys $X \uh m$.

:::figure[The oscillation theorem. The prefix $\beta = X \uh m$ codes a number $N \geq 2^m - 1$, and $\alpha$ is the block of the next $N$ bits. The machine $\alpha \mapsto \beta\alpha$, where $\beta$ is the string of the number $|\alpha|$, describes $X \uh (m + N)$ with $N$ bits, $m$ fewer than its length.]
<svg class="fig" viewBox="0 0 600 168" width="600" role="img" aria-label="An initial segment of X cut into the prefix beta of length m and the block alpha of length N, where N is the number coded by beta; alpha alone is a description of beta alpha"><defs><marker id="kc-osc-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="20" y="62" width="90" height="28" class="cell head-cell"/><rect x="110" y="62" width="420" height="28" class="cell"/><text x="540" y="81" class="mrm" font-size="16">⋯</text><text x="65.0" y="81" text-anchor="middle" class="math" font-size="16">β</text><text x="320.0" y="81" text-anchor="middle" class="math" font-size="16">α</text><path d="M21.0,48.0 L21.0,54.0 L109.0,54.0 L109.0,48.0" class="ink-stroke" stroke-width="1.1"/><text x="65.0" y="42" text-anchor="middle" class="label">X↾m, codes N</text><path d="M111.0,48.0 L111.0,54.0 L529.0,54.0 L529.0,48.0" class="ink-stroke" stroke-width="1.1"/><text x="320.0" y="42" text-anchor="middle" class="label">the next N bits of X, N ≥ 2ᵐ − 1</text><path d="M21.0,104.0 L21.0,98.0 L529.0,98.0 L529.0,104.0" class="muted-stroke" stroke-width="1.1"/><text x="275.0" y="116" text-anchor="middle" class="label">X↾(m + N): described by α alone, with N + c bits</text><path d="M260.0,142 C120.0,156 105.0,150 65.0,124" class="accent-stroke" stroke-width="1.2" marker-end="url(#kc-osc-arrow)"/><text x="268.0" y="148" class="label">the length |α| = N gives back β</text></svg>
:::

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

The proof gives more: the deficiency at length $n = m + N$ is $m - c$, and $m$ is about $\log N$, so $C(X \uh n) \leq n - \log n + O(1)$ for infinitely many $n$.

:::corollary{#cor-no-c-random}
No sequence $X$ satisfies $C(X \uh n) \geq n - c$ for every $n$, whatever the constant $c$.
:::

The incompressible strings of :ref{#prop-incompressible-count} cannot be the initial segments of a single sequence at all lengths. A definition of random sequences through compressibility must use another complexity. Prefix-free complexity, introduced two lessons below, does not suffer from this effect, and a sequence is random in the sense of the following course when $K(X \uh n) \geq n - c$ for all $n$. Plain complexity still detects randomness through infinitely many lengths: Nies, Stephan and Terwijn proved that $C(X \uh n) \geq n - c$ holds for some $c$ and infinitely many $n$ if and only if $X$ is random relative to the halting problem (2-random), a notion of the course on Martin-Löf randomness; this is not proved here.

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

::::exercise{#ex-concatenation difficulty=1 objective="Use the construction of the oscillation theorem to show that $C$ is not subadditive for concatenation."}
Show that for every $c$ there are strings $\sigma$, $\tau$ with $C(\sigma\tau) > C(\sigma) + C(\tau) + c$.

:::solution
Let $M$ and $c_M$ be as in the proof of :ref{#thm-oscillation}, and $d$ such that $C(\rho) \leq |\rho| + d$ for every $\rho$. Let $m > c + c_M + d$ and $L = m + 2^{m+1}$. Let $\gamma$ be a string of length $L$ with $C(\gamma) \geq L$ (:ref{#prop-incompressible-count}). Let $N$ be the number associated with $\gamma \uh m$; then $N < 2^{m+1} - 1$, so $m + N \leq L$. Write $\gamma = \sigma\tau$ with $|\sigma| = m + N$. As in the proof of the theorem, $C(\sigma) \leq |\sigma| - m + c_M$, and $C(\tau) \leq |\tau| + d$. Hence $C(\sigma) + C(\tau) + c \leq L - m + c_M + d + c < L \leq C(\sigma\tau)$.
:::
::::

## Notes and references

The oscillation theorem is due to Martin-Löf (1966), who introduced at the same time the definition of randomness through effective tests, treated in the next course; it is presented by Kolmogorov (1968) and in Downey–Hirschfeldt, Theorem 3.1.4, and refined in their Section 3.11. The bound for c.e. sets is due to Barzdins (1968) (Downey–Hirschfeldt, Theorem 16.1.1). The characterization of 2-randomness by plain complexity is due to Nies, Stephan and Terwijn (2005), with one implication obtained independently by Miller (2004); see Nies, Theorem 3.6.10.

- P. Martin-Löf, *The definition of random sequences*, Information and Control 9 (1966), 602–619.
- A. N. Kolmogorov, *Logical basis for information theory and probability theory*, IEEE Transactions on Information Theory 14 (1968), 662–664.
- J. Barzdins, *Complexity of programs to determine whether natural numbers not greater than n belong to a recursively enumerable set*, Soviet Mathematics Doklady 9 (1968), 1251–1254.
- A. Nies, F. Stephan and S. A. Terwijn, *Randomness, relativization and Turing degrees*, Journal of Symbolic Logic 70 (2005), 515–535.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.1, 3.11 and 16.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 3.6.

:::::exercises
::::exercise{#ex-uniform-deficiency difficulty=1 objective="Extract from the proof of the oscillation theorem a deficiency of $\log n$ with a constant independent of the sequence."}
Show that there is a constant $c$ such that, for every sequence $X$, there are infinitely many $n$ with $C(X \uh n) \leq n - \log n + c$.

:::solution
Let $M$ and $c_M$ be as in the proof of :ref{#thm-oscillation}; they do not depend on $X$. For $m \geq 1$, let $N$ be the number associated with $X \uh m$ and $n = m + N$. The proof gives $C(X \uh n) \leq N + c_M = n - m + c_M$. The string $X \uh m$ has length $m$, so $N \leq 2^{m+1} - 2$, and $n \leq m + 2^{m+1} \leq 2^{m+2}$, since $m \leq 2^{m+1}$. So $\log n \leq m + 2$, and $C(X \uh n) \leq n - \log n + c_M + 2$. Since $n \geq m$, the lengths $n$ obtained for $m = 1, 2, \dots$ are unbounded, and $c = c_M + 2$ works for every $X$.
:::
::::

::::exercise{#ex-computable-oscillation difficulty=1 objective="Locate the oscillation of $C(X \uh n)$ for a computable sequence $X$ between $\log \log n$ and $\log n$."}
Let $X$ be a computable sequence. Show that there is a constant $c$ such that $C(X \uh n) \geq \log n - c$ for infinitely many $n$, and $C(X \uh n) \leq \log \log n + c$ for infinitely many $n$.

:::solution
By :ref{#prop-computable-segments}, there is $c_1$ with $|C(X \uh n) - C(n)| \leq c_1$ for every $n$. For each $\ell \geq 1$, :ref{#prop-incompressible-count} gives a string of length $\ell$ with complexity at least $\ell$; it is the string of a number $n_\ell$ with $2^\ell - 1 \leq n_\ell \leq 2^{\ell + 1} - 2$, so $\log n_\ell < \ell + 1$. Then $C(X \uh n_\ell) \geq C(n_\ell) - c_1 \geq \ell - c_1 > \log n_\ell - 1 - c_1$, and the numbers $n_\ell$ are pairwise distinct.

For the second bound, let $n = 2^k$ with $k \geq 1$. The map $k \mapsto 2^k$ is computable, so by :ref{#prop-c-basic} there is $c_2$ with $C(2^k) \leq \log k + c_2$ for $k \geq 1$. Then $C(X \uh n) \leq C(n) + c_1 \leq \log k + c_2 + c_1 = \log \log n + c_1 + c_2$. So $c = c_1 + c_2 + 1$ works for both bounds.
:::
::::

::::exercise[Sparse sequences]{#ex-sparse-sequences difficulty=2 objective="Describe the initial segments of sparse sequences to see that a bound $2 \log n$ holds, with a single constant, for uncountably many sequences."}
For a set $A \subseteq \nat$, let $X_A$ be the characteristic sequence of $\{ 2^k : k \in A \}$. Show that there is a constant $c$, independent of $A$, such that $C(X_A \uh n) \leq 2 \log n + c$ for every $A$ and every $n \geq 1$. Deduce that uncountably many sequences $X$ satisfy $C(X \uh n) \leq 2 \log n + c$ for every $n \geq 1$.

:::solution
Let $n \geq 1$ and $m = \lceil \log n \rceil$. A number $k$ satisfies $2^k < n$ if and only if $k < \log n$, that is, $k < m$. So $X_A \uh n$ is determined by $n$ and $A \uh m$. Let $\beta$ be the string of $n$, of length $\ell = \lfloor \log(n+1) \rfloor$. Since $n < 2^{\ell+1}$, $m \leq \ell + 1$; let $\kappa = (A \uh m)\, 0^{\ell + 1 - m}$, of length $\ell + 1$.

Let $M$ be the machine that, on an input of odd length $2\ell + 1$, splits it into $\beta$ of length $\ell$ and $\kappa$ of length $\ell + 1$, lets $n$ be the number of $\beta$, outputs the empty string if $n = 0$, and otherwise outputs the string of length $n$ whose bit at position $j$ is $1$ if and only if $j = 2^k$ for some $k < \lceil \log n \rceil$ with $\kappa(k) = 1$. The machine does not depend on $A$, and $M(\beta\kappa) = X_A \uh n$. So $C(X_A \uh n) \leq 2\ell + 1 + c_M \leq 2 \log(n + 1) + 1 + c_M \leq 2 \log n + 3 + c_M$, and $c = 3 + c_M$ works.

The map $A \mapsto X_A$ is injective, and there are uncountably many sets $A$. By contrast, Chaitin's theorem, proved in the next lesson, shows that the sequences with $C(X \uh n) \leq^+ \log n$ are the computable ones, of which there are countably many.
:::
::::

::::exercise{#ex-segment-complexity difficulty=1 objective="Combine the Berry argument with the complexity of the initial segments of computable sequences."}
Let $X$ be a computable sequence. Show that the function $n \mapsto C(X \uh n)$ is not computable.

:::solution
By :ref{#prop-computable-segments}, there is $c$ with $|C(X \uh n) - C(n)| \leq c$ for every $n$. Suppose that $F(n) = C(X \uh n)$ is computable. Then $g(n) = \max(F(n) - c, 0)$, viewed as a function on strings through the identification of numbers with strings, is total computable and satisfies $g(n) \leq C(n)$. It is unbounded, since $g(n) \geq C(n) - 2c$ and $C$ is unbounded by :ref{#prop-incompressible-count}. This contradicts :ref{#thm-c-not-computable} (1).
:::
::::
:::::
