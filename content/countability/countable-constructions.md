---
title: Countable constructions
summary: Products, countable unions with given enumerations and finite strings over countable sets are countable; so are the finite sets of integers, the rationals and the algebraic numbers.
duration: 40
prerequisites: [countable-sets, models-of-computation/what-is-an-algorithm]
---

The previous lesson reduced countability to the existence of a listing, possibly with repetitions. This lesson shows that the sets built from integers by finite means — pairs, tuples, finite sequences, finite sets, rational and algebraic numbers — are countable, by exhibiting such listings. Two ideas recur: **dovetailing**, which merges infinitely many infinite lists into one, and **coding** by integers, which replaces a finite object by a number from which it can be recovered. Both are used constantly in computability theory, where every finite object is identified with a code. The one place where the axiom of choice threatens to enter, countable unions, is singled out.

## Pairs and tuples

The pairs $(x, y)$ fill an infinite grid, and listing them row by row fails: the first row is already infinite, so the second row is never reached. The way out is to list the grid along finite pieces that together cover it, here the diagonals $x + y = k$. At each stage only finitely many pairs are listed, and every pair is reached at some stage. This idea, interleaving infinitely many infinite tasks so that each receives attention infinitely often, is called **dovetailing**; in computability theory, it is used to run infinitely many computations in parallel, for instance in the search of :ref{#prop-selection} in the course on fundamentals, which runs through the pairs (witness, number of steps) along an enumeration of $\nat \times \nat$.

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
1. $\mathbb Z$ is countably infinite, by :ref{#ex-countable-sets}.
2. $\mathbb Q$ is countably infinite, although between two rationals there are infinitely many others, so that no listing of $\mathbb Q$ can respect its order. The map $(p, q) \mapsto p/(q+1)$ is a surjection from $\mathbb Z \times \nat$, a countable set by the corollary, onto $\mathbb Q$, so $\mathbb Q$ is countable by :ref{#cor-subset-countable}; it is infinite since it contains $\nat$.
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

The computational consequence of :ref{#prop-strings-countable} is the starting point of the lesson on diagonalization and computation: programs, in any programming language, are strings over a finite alphabet, so there are countably many of them, and countably many computable functions.

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
Show that the set of eventually periodic sequences $X : \nat \to \{0, 1\}$ is countable. (A sequence is **eventually periodic** if there are $n_0$ and $p \geq 1$ such that $X(n + p) = X(n)$ for all $n \geq n_0$.)

:::solution
An eventually periodic sequence is determined by two strings $u$ and $v$ over $\{0, 1\}$, with $v$ non-empty: its first $n_0$ values $u$, followed by $v$ repeated forever. So there is a surjection from a subset of $\{0, 1\}^* \times \{0, 1\}^*$, which is countable by :ref{#prop-strings-countable} and :ref{#cor-product-countable}, onto the set of eventually periodic sequences, which is therefore countable by :ref{#cor-subset-countable}.
:::
::::

::::exercise{difficulty=1}
Show that $(x, y) \mapsto 2^x (2y + 1) - 1$ is a bijection from $\nat \times \nat$ onto $\nat$.

:::solution
Every integer $m \geq 1$ can be written uniquely as $m = 2^x q$ with $q$ odd: $x$ is the number of times $2$ divides $m$, and $q = m / 2^x$. Writing $q = 2y + 1$, every $m \geq 1$ is $2^x(2y+1)$ for exactly one pair $(x, y)$. Hence $(x, y) \mapsto 2^x(2y+1)$ is a bijection onto $\nat \setminus \{0\}$, and subtracting $1$ gives a bijection onto $\nat$.
:::
::::

::::exercise{difficulty=2}
A real number is **transcendental** if it is not algebraic. Show that every non-empty open interval contains a transcendental number, admitting that intervals are uncountable (this is proved in the next lessons).

:::solution
An open interval $(a, b)$ with $a < b$ is uncountable, while the algebraic numbers form a countable set by :ref{#ex-algebraic-numbers}. If $(a, b)$ contained only algebraic numbers, it would be countable, by :ref{#cor-subset-countable}.
:::
::::

## Notes and references

The countability of the algebraic numbers is the first result of Cantor's paper of 1874, which also proves, by a different argument than the diagonal one, that the real numbers are not countable; together, the two results give a new proof of the existence of transcendental numbers, first established by Liouville in 1844. Gray discusses the paper and shows that the transcendental numbers it produces can be computed. The consistency of "$\mathbb R$ is a countable union of countable sets" with ZF is due to Feferman and Lévy (1963); a proof is in Jech's monograph on the axiom of choice. Monin and Patey (chapter *Cantor's infinity*, section *Countable sets*) treat pairs and countable unions in the same way.

- G. Cantor, *Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen*, Journal für die reine und angewandte Mathematik 77 (1874), 258–262.
- R. Gray, *Georg Cantor and transcendental numbers*, American Mathematical Monthly 101 (1994), 819–832.
- T. Jech, *The Axiom of Choice*, North-Holland, 1973.
- K. Hrbacek and T. Jech, *Introduction to Set Theory*, 3rd edition, Marcel Dekker, 1999.
- B. Monin and L. Patey, *Computability theory*, chapter *Cantor's infinity*.
