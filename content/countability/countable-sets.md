---
title: Countable sets
summary: Characterizations of countable sets; subsets of ℕ; products, unions, finite strings, rationals and algebraic numbers.
duration: 40
prerequisites: [cantor-bernstein]
---

A set is countable when its elements can be listed in a sequence indexed by integers. Countable sets are the natural setting of computation: inputs, outputs and programs are finite objects, and there are countably many of them. This lesson characterizes countable sets in several equivalent ways and shows that the sets built from integers by finite means — pairs, tuples, finite sequences, finite sets, rational and algebraic numbers — are all countable. The few uses of the axiom of choice are signaled explicitly.

## Definition and characterizations

:::definition{#def-countable}
A set $A$ is **countably infinite** if $|A| = |\nat|$. It is **countable** if it is finite or countably infinite, and **uncountable** otherwise.
:::

A bijection $e : \nat \to A$ is an **enumeration without repetition** of $A$, and is often written as a sequence $a_0, a_1, a_2, \dots$ with $a_n = e(n)$. The basic fact behind all characterizations is that the subsets of $\nat$ are countable.

:::lemma{#lem-subsets-of-n}
Every infinite set $S \subseteq \nat$ is countably infinite. More precisely, the **principal function** $p_S : \nat \to S$ defined by
$$
p_S(0) = \min S, \qquad p_S(n+1) = \min \{ s \in S : s > p_S(n) \}
$$
is a strictly increasing bijection, which enumerates $S$ in increasing order.
:::

:::proof{of=lem-subsets-of-n}
The minima exist. Indeed $S \neq \emptyset$; and if $S$ had no element greater than $p_S(n)$, then $S \subseteq \underline{p_S(n) + 1}$ would be finite, as a subset of a finite set (:ref{#ex-subset-finite}). By construction $p_S$ is strictly increasing, hence injective, and by induction $p_S(n) \geq n$ for all $n$.

For surjectivity, let $s \in S$. The values $p_S(0) < p_S(1) < \dots$ are unbounded since $p_S(n) \geq n$, so there is a least $n$ with $p_S(n) \geq s$. If $n = 0$, then $s \geq \min S = p_S(0)$ gives $s = p_S(0)$. If $n > 0$, then $p_S(n-1) < s \leq p_S(n)$, and $p_S(n)$ is by definition the least element of $S$ above $p_S(n-1)$, so $p_S(n) \leq s$, hence $s = p_S(n)$.
:::

:::proposition{#prop-countable-characterizations}
For every set $A$, the following are equivalent.

1. $A$ is countable.
2. $|A| \leq |\nat|$: there is an injection from $A$ into $\nat$.
3. $A = \emptyset$, or there is a surjection from $\nat$ onto $A$.
:::

:::proof{of=prop-countable-characterizations}
(1 ⇒ 2) A bijection with $\underline n \subseteq \nat$ or with $\nat$ is an injection into $\nat$.

(2 ⇒ 3) Suppose $A \neq \emptyset$, fix $a_0 \in A$, and let $i : A \to \nat$ be an injection. Define $s : \nat \to A$ by $s(n) = a$ if $n = i(a)$, which determines $a$ uniquely, and $s(n) = a_0$ if $n \notin i(A)$. Then $s(i(a)) = a$ for every $a$, so $s$ is surjective.

(3 ⇒ 2) The empty set injects into $\nat$. If $s : \nat \to A$ is surjective, then $|A| \leq |\nat|$ by :ref{#prop-surjection-subpotent}: the injection sends $a$ to the least $n$ with $s(n) = a$.

(2 ⇒ 1) If $i : A \to \nat$ is injective, then $A$ is equipotent to $S = i(A) \subseteq \nat$. If $S$ is finite, so is $A$. Otherwise $S$ is countably infinite by :ref{#lem-subsets-of-n}, and so is $A$.
:::

Characterization 3 is the one used most often: a non-empty set is countable when it can be listed as $a_0, a_1, a_2, \dots$, **repetitions allowed**. Removing the repetitions is done by the proof, by keeping only the first occurrence of each element.

:::corollary{#cor-subset-countable}
1. Every subset of a countable set is countable.
2. The image of a countable set under any function is countable.
:::

:::proof{of=cor-subset-countable}
1. If $B \subseteq A$ and $i : A \to \nat$ is injective, the restriction of $i$ to $B$ is injective.
2. Let $f$ be a function defined on a countable set $A$. If $A = \emptyset$, then $f(A) = \emptyset$. Otherwise, if $s : \nat \to A$ is surjective, then $f \circ s$ is a surjection from $\nat$ onto $f(A)$.
:::

:::quiz[the principal function of a set of integers]
In the proof of :ref{#lem-subsets-of-n}, where is the hypothesis "$S$ is infinite" used?

- [x] To guarantee that $S$ has elements above $p_S(n)$, so that $p_S(n+1)$ is defined.

  For a finite set, the construction stops after $|S|$ steps, and produces a bijection with $\underline{|S|}$ instead.
- [ ] To prove that $p_S$ is injective.

  Injectivity comes from $p_S$ being strictly increasing, which holds as long as it is defined.
- [ ] To prove that $p_S(n) \geq n$.

  This follows by induction from strict increase alone.

---

In the step (3 ⇒ 2) of :ref{#prop-countable-characterizations}, why is no axiom of choice needed to invert the surjection $s$?

- [x] The preimages $s^{-1}(\{a\})$ are non-empty sets of integers, which have least elements.

  The least element is a definite choice, made uniformly for all $a$.
- [ ] Because $A$ is countable.

  That is what is being proved.
- [ ] Because every surjection has a right inverse.

  For arbitrary sets, this statement is the axiom of choice itself.
:::

## The smallest infinity

:::proposition{#prop-n-smallest}
Every infinite set $A$ satisfies $|\nat| \leq |A|$.
:::

:::proof{of=prop-n-smallest}
We define an injection $a : \nat \to A$ by induction. Pick $a_0 \in A$, which exists since $\emptyset$ is finite. Having chosen pairwise distinct $a_0, \dots, a_n$, the set $\{a_0, \dots, a_n\}$ is finite, so it is not $A$; pick $a_{n+1} \in A \setminus \{a_0, \dots, a_n\}$. The elements $a_n$ are pairwise distinct by construction.
:::

This proof makes infinitely many arbitrary choices, one at each step, each depending on the previous ones. It uses the **axiom of dependent choice**, a weak form of the axiom of choice, and cannot be carried out in ZF alone: it is consistent with ZF that some infinite set of real numbers has no countably infinite subset (we admit this result of Cohen; a proof is in Jech's monograph on the axiom of choice). When $A$ comes with an injection into $\nat$ or with a linear order in which every non-empty subset has a least element, one can take $a_{n+1}$ to be the least element of $A \setminus \{a_0, \dots, a_n\}$, and no choice is needed; this is what :ref{#lem-subsets-of-n} does.

:::corollary{#cor-countably-infinite-minimal}
An infinite set is countable if and only if it is equipotent to each of its infinite subsets.
:::

:::proof{of=cor-countably-infinite-minimal}
If $A$ is countably infinite and $B \subseteq A$ is infinite, then $B$ is countable by :ref{#cor-subset-countable}, and infinite, so $|B| = |\nat| = |A|$. Conversely, if $A$ is infinite and equipotent to each of its infinite subsets, then by :ref{#prop-n-smallest} it has a subset $a(\nat)$ equipotent to $\nat$, and $|A| = |a(\nat)| = |\nat|$.
:::

## Pairs and tuples

:::proposition{#prop-nxn-countable}
The set $\nat \times \nat$ is countably infinite. An explicit bijection is **Cantor's pairing function**
$$
\langle x, y \rangle = \frac{(x+y)(x+y+1)}{2} + y.
$$
:::

:::figure[The pairs $(x, y)$ with $x + y \leq 4$, labeled by $\langle x, y \rangle$. The enumeration follows each diagonal upwards, then jumps to the next diagonal.]
<svg class="fig" viewBox="0 0 330 300" width="330" role="img" aria-label="Pairs of integers numbered along successive diagonals"><defs><marker id="ah-pair" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="42" y1="250" x2="302" y2="250" class="axis"/><line x1="60" y1="268" x2="60" y2="8" class="axis"/><text x="308" y="255" class="math" font-size="17">x</text><text x="55" y="2" class="math" font-size="17">y</text><text x="60" y="282" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="34" y="255" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="112" y="282" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="34" y="203" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="164" y="282" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="34" y="151" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="216" y="282" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="34" y="99" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="268" y="282" text-anchor="middle" class="mrm muted" font-size="13">4</text><text x="34" y="47" text-anchor="middle" class="mrm muted" font-size="13">4</text><line x1="75.0" y1="250.0" x2="95.0" y2="250.0" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-pair)"/><line x1="101.4" y1="239.4" x2="72.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="73.4" y1="204.7" x2="148.8" y2="242.4" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-pair)"/><line x1="153.4" y1="239.4" x2="124.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="101.4" y1="187.4" x2="72.0" y2="158.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="72.5" y1="154.3" x2="201.9" y2="240.6" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-pair)"/><line x1="205.4" y1="239.4" x2="176.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="153.4" y1="187.4" x2="124.0" y2="158.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="101.4" y1="135.4" x2="72.0" y2="106.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="72.0" y1="103.0" x2="254.4" y2="239.8" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-pair)"/><line x1="257.4" y1="239.4" x2="228.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="205.4" y1="187.4" x2="176.0" y2="158.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="153.4" y1="135.4" x2="124.0" y2="106.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><line x1="101.4" y1="83.4" x2="72.0" y2="54.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-pair)"/><circle cx="60" cy="250" r="14" class="node"/><text x="60" y="255" text-anchor="middle" class="mrm" font-size="14">0</text><circle cx="112" cy="250" r="14" class="node"/><text x="112" y="255" text-anchor="middle" class="mrm" font-size="14">1</text><circle cx="60" cy="198" r="14" class="node"/><text x="60" y="203" text-anchor="middle" class="mrm" font-size="14">2</text><circle cx="164" cy="250" r="14" class="node"/><text x="164" y="255" text-anchor="middle" class="mrm" font-size="14">3</text><circle cx="112" cy="198" r="14" class="node"/><text x="112" y="203" text-anchor="middle" class="mrm" font-size="14">4</text><circle cx="60" cy="146" r="14" class="node"/><text x="60" y="151" text-anchor="middle" class="mrm" font-size="14">5</text><circle cx="216" cy="250" r="14" class="node"/><text x="216" y="255" text-anchor="middle" class="mrm" font-size="14">6</text><circle cx="164" cy="198" r="14" class="node"/><text x="164" y="203" text-anchor="middle" class="mrm" font-size="14">7</text><circle cx="112" cy="146" r="14" class="node"/><text x="112" y="151" text-anchor="middle" class="mrm" font-size="14">8</text><circle cx="60" cy="94" r="14" class="node"/><text x="60" y="99" text-anchor="middle" class="mrm" font-size="14">9</text><circle cx="268" cy="250" r="14" class="node"/><text x="268" y="255" text-anchor="middle" class="mrm" font-size="14">10</text><circle cx="216" cy="198" r="14" class="node"/><text x="216" y="203" text-anchor="middle" class="mrm" font-size="14">11</text><circle cx="164" cy="146" r="14" class="node"/><text x="164" y="151" text-anchor="middle" class="mrm" font-size="14">12</text><circle cx="112" cy="94" r="14" class="node"/><text x="112" y="99" text-anchor="middle" class="mrm" font-size="14">13</text><circle cx="60" cy="42" r="14" class="node"/><text x="60" y="47" text-anchor="middle" class="mrm" font-size="14">14</text></svg>
:::

:::proof{of=prop-nxn-countable}
List the pairs diagonal by diagonal: first those with $x + y = 0$, then those with $x + y = 1$, and so on, each diagonal in order of increasing $y$:
$$
(0,0),\ (1,0),\ (0,1),\ (2,0),\ (1,1),\ (0,2),\ (3,0),\ \dots
$$
The diagonal $x + y = k$ contains the $k + 1$ pairs $(k, 0), (k-1, 1), \dots, (0, k)$, so the diagonals before it contain $1 + 2 + \dots + k = k(k+1)/2$ pairs, and $(x, y)$ is at position $k(k+1)/2 + y$ with $k = x + y$. Every pair lies on exactly one diagonal and appears once on it, so the listing is a bijection between $\nat \times \nat$ and $\nat$, and the position of $(x, y)$ is $\langle x, y \rangle$.
:::

The function and its inverses are studied as computable functions in the course on models of computation (:ref{#prop-cantor-pairing-bijection}).

:::quiz[the enumeration of pairs]
Why does the proof list the pairs diagonal by diagonal rather than row by row, $(0,0), (0,1), (0,2), \dots$ and then $(1,0), (1,1), \dots$?

- [x] Row by row, the first row is already infinite, so the pair $(1, 0)$ would never get a position.
- [ ] Row by row would list some pairs twice.

  It lists no pair twice; it never reaches the second row.
- [ ] Because the formula for $\langle x, y \rangle$ only works for diagonals.

  The formula is a consequence of the order chosen, not its reason.

---

What is $\langle 0, 3 \rangle$?

- [ ] $3$

  $3 = \langle 2, 0 \rangle$ is the position of the first pair of the diagonal $x + y = 2$.
- [ ] $6$

  $6 = \langle 3, 0 \rangle$ is the first pair of the diagonal $x + y = 3$; the pair $(0, 3)$ is the last one.
- [x] $9$

  The diagonal $x + y = 3$ starts at position $3 \cdot 4/2 = 6$ and lists $(3,0), (2,1), (1,2), (0,3)$ at positions $6, 7, 8, 9$.
- [ ] $10$

  $10 = \langle 4, 0 \rangle$ is the first pair of the next diagonal.
:::

:::corollary{#cor-product-countable}
1. If $A$ and $B$ are countable, so is $A \times B$.
2. For every $k \geq 1$, $\nat^k$ is countably infinite.
:::

:::proof{of=cor-product-countable}
1. If $i : A \to \nat$ and $j : B \to \nat$ are injections, then $(a, b) \mapsto \langle i(a), j(b) \rangle$ is an injection of $A \times B$ into $\nat$.
2. By induction on $k$, identifying $\nat^{k+1}$ with $\nat^k \times \nat$; the set is infinite since $\nat$ injects into it.
:::

Explicitly, a bijection $\nat^k \to \nat$ is obtained by iterating the pairing function: $\langle x_1, \dots, x_{k+1} \rangle = \langle \langle x_1, \dots, x_k \rangle, x_{k+1} \rangle$.

:::example{#ex-integers-rationals}
1. $\mathbb Z$ is countably infinite: $z \mapsto 2z$ for $z \geq 0$ and $z \mapsto -2z - 1$ for $z < 0$ is a bijection $\mathbb Z \to \nat$.
2. $\mathbb Q$ is countably infinite. The map $(p, q) \mapsto p/(q+1)$ is a surjection from $\mathbb Z \times \nat$, a countable set by the corollary, onto $\mathbb Q$, so $\mathbb Q$ is countable by :ref{#cor-subset-countable}; it is infinite since it contains $\nat$.
:::

## Unions

:::proposition{#prop-countable-union}
Let $(A_n)_{n \in \nat}$ be a sequence of sets, and let $(s_n)_{n \in \nat}$ be a sequence of functions such that each $s_n : \nat \to A_n$ is surjective. Then $\bigcup_n A_n$ is countable. In particular, a finite union of countable sets is countable.
:::

:::proof{of=prop-countable-union}
The map $\langle n, m \rangle \mapsto s_n(m)$ is a surjection from $\nat$ onto $\bigcup_n A_n$: every element of $A_n$ is some $s_n(m)$. For a finite union $A_0 \cup \dots \cup A_k$ of non-empty countable sets, fix surjections $s_0, \dots, s_k$ and let $A_n = A_k$ and $s_n = s_k$ for $n > k$, which does not change the union; the empty sets can be discarded beforehand.
:::

The hypothesis provides the enumerations $s_n$ along with the sets. The statement "a countable union of countable sets is countable", without given enumerations, requires choosing one enumeration of each $A_n$ among infinitely many possibilities. It is a consequence of the axiom of countable choice, and it is not provable in ZF: Feferman and Lévy showed that it is consistent with ZF that $\mathbb R$ is a countable union of countable sets. We admit this result. In practice, as in the examples below, the sets come with natural enumerations, and the proposition applies directly.

:::quiz[countable unions]
Where does the proof of :ref{#prop-countable-union} use that the enumerations $s_n$ are given as a sequence?

- [x] To define the single function $\langle n, m \rangle \mapsto s_n(m)$, which needs $s_n$ for all $n$ at once.

  Knowing that each $A_n$ has some enumeration does not provide a function $n \mapsto s_n$.
- [ ] To show that each $A_n$ is countable.

  That is part of the hypothesis.
- [ ] To show that the map is surjective.

  Surjectivity only uses that each $s_n$ is surjective, once the map is defined.
:::

## Finite strings and finite sets

An **alphabet** is a set $\Sigma$, whose elements are called **letters**. A **string** of length $k$ over $\Sigma$ is a finite sequence $w = a_1 a_2 \cdots a_k$ of letters, that is, a function $\{1, \dots, k\} \to \Sigma$; the string of length $0$ is the **empty string** $\varepsilon$. The set of strings over $\Sigma$ is written $\Sigma^*$.

:::proposition{#prop-strings-countable}
If $\Sigma$ is countable, then $\Sigma^*$ is countable. It is countably infinite if $\Sigma \neq \emptyset$.
:::

:::proof{of=prop-strings-countable}
Let $i : \Sigma \to \nat$ be an injection, and $p_1 = 2, p_2 = 3, p_3 = 5, \dots$ the primes. The map
$$
a_1 a_2 \cdots a_k \;\mapsto\; p_1^{\,i(a_1) + 1}\, p_2^{\,i(a_2) + 1} \cdots p_k^{\,i(a_k) + 1}
$$
sends $\varepsilon$ to $1$ and is injective by uniqueness of prime factorization: the code determines $k$, as the number of its distinct prime factors, and each $i(a_j)$, hence each $a_j$. If $a \in \Sigma$, the strings $a, aa, aaa, \dots$ are pairwise distinct, so $\Sigma^*$ is infinite.
:::

The exponents are shifted by one so that the code determines the length: without the shift, strings of letters $a$ with $i(a) = 0$ would all be coded by $1$.

:::corollary{#cor-finite-subsets}
The set $\mathcal P_{\mathrm{fin}}(\nat)$ of finite subsets of $\nat$ is countably infinite. An explicit bijection with $\nat$ is $F \mapsto \sum_{n \in F} 2^n$.
:::

:::proof{of=cor-finite-subsets}
Every integer has a unique binary expansion, and a finite set $F$ is exactly the set of positions of the digits $1$ in the binary expansion of $\sum_{n \in F} 2^n$.
:::

:::example{#ex-algebraic-numbers}
A real number is **algebraic** if it is a root of a non-zero polynomial with integer coefficients. The set of real algebraic numbers is countable. Indeed, a polynomial $c_0 + c_1 X + \dots + c_d X^d$ is determined by the string $c_0 c_1 \cdots c_d$ over the countable alphabet $\mathbb Z$, so there is a surjection $n \mapsto P_n$ from $\nat$ onto the non-zero polynomials, by :ref{#prop-strings-countable}. A non-zero polynomial $P_n$ has at most $\deg P_n$ real roots; list them in increasing order as $r_{n,0} < \dots < r_{n,k-1}$, and let $r_{n,m} = r_{n,k-1}$ for $m \geq k$ (if $P_n$ has no real root, let $r_{n,m} = 0$, which is algebraic). Then $\langle n, m \rangle \mapsto r_{n,m}$ is a surjection onto the real algebraic numbers. The ordering of the roots replaces an arbitrary choice of enumeration of each finite set of roots.
:::

The computational consequence of :ref{#prop-strings-countable} is the starting point of the last lesson: programs, in any programming language, are strings over a finite alphabet, so there are countably many of them, and countably many computable functions.

:::quiz[which sets are countable]
Which of these sets are countable?

- [x] The set of all programs of a given programming language.

  Programs are strings over a finite alphabet.
- [x] The set of finite subsets of $\nat$.

  By :ref{#cor-finite-subsets}.
- [x] The set of polynomials with rational coefficients.

  A polynomial is a string over the countable alphabet $\mathbb Q$.
- [ ] The set of **all** subsets of $\nat$.

  It is uncountable, by the diagonal argument of the next lesson.
- [x] The set of sequences $\nat \to \nat$ that are zero from some point on.

  Such a sequence is determined by the finite string of its values up to its last non-zero value.
:::

## Exercises

::::exercise{difficulty=1}
Let $s : \nat \to A$ be a surjection onto an infinite set $A$. Construct an explicit bijection between $\nat$ and $A$, without appealing to :ref{#prop-n-smallest}.

:::solution
Let $S = \{ n : s(n) \neq s(m) \text{ for all } m < n \}$ be the set of positions of first occurrences. The restriction of $s$ to $S$ is a bijection from $S$ onto $A$: it is surjective, since each $a \in A$ has a least $n$ with $s(n) = a$, and this $n$ is in $S$; it is injective, since two first occurrences of the same element would be equal. $S$ is infinite since $A$ is. So $s \circ p_S : \nat \to A$ is a bijection, where $p_S$ is the principal function of :ref{#lem-subsets-of-n}.
:::
::::

::::exercise{difficulty=1}
Show that the set of eventually periodic sequences $X : \nat \to \{0, 1\}$ is countable. (A sequence is **eventually periodic** if there are $n_0$ and $p \geq 1$ such that $X(n + p) = X(n)$ for all $n \geq n_0$.)

:::solution
An eventually periodic sequence is determined by two strings $u$ and $v$ over $\{0, 1\}$, with $v$ non-empty: its first $n_0$ values $u$, followed by $v$ repeated forever. So there is a surjection from a subset of $\{0, 1\}^* \times \{0, 1\}^*$, which is countable by :ref{#prop-strings-countable} and :ref{#cor-product-countable}, onto the set of eventually periodic sequences, which is therefore countable by :ref{#cor-subset-countable}.
:::
::::

::::exercise{#ex-dedekind-infinite difficulty=2}
Show that a set $A$ is infinite if and only if it is equipotent to a proper subset of itself. Which direction uses the axiom of choice?

:::solution
If $A$ is finite, it is not equipotent to a proper subset, by :ref{#cor-finite-cardinality}. Conversely, if $A$ is infinite, let $a : \nat \to A$ be an injection, given by :ref{#prop-n-smallest}. The map $h$ defined by $h(a_n) = a_{n+1}$ and $h(x) = x$ for $x \notin a(\nat)$ is a bijection from $A$ onto $A \setminus \{a_0\}$. Only the second direction uses choice, through :ref{#prop-n-smallest}.
:::
::::

::::exercise{difficulty=2}
A real number is **transcendental** if it is not algebraic. Show that every non-empty open interval contains a transcendental number, admitting that intervals are uncountable (this is proved in the next lessons).

:::solution
An open interval $(a, b)$ with $a < b$ is uncountable, while the algebraic numbers form a countable set by :ref{#ex-algebraic-numbers}. If $(a, b)$ contained only algebraic numbers, it would be countable, by :ref{#cor-subset-countable}.
:::
::::

## Notes and references

The countability of the algebraic numbers is the first result of Cantor's paper of 1874, which also proves, by a different argument than the diagonal one, that the real numbers are not countable; together, the two results give a new proof of the existence of transcendental numbers, first established by Liouville in 1844. The consistency of "$\mathbb R$ is a countable union of countable sets" with ZF is due to Feferman and Lévy (1963); a proof is in Jech's monograph on the axiom of choice.

- G. Cantor, *Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen*, Journal für die reine und angewandte Mathematik 77 (1874), 258–262.
- T. Jech, *The Axiom of Choice*, North-Holland, 1973.
- K. Hrbacek and T. Jech, *Introduction to Set Theory*, 3rd edition, Marcel Dekker, 1999.
