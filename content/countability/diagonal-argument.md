---
title: The diagonal argument
summary: Cantor space; uncountability of the sets of binary sequences, of integer sequences, of power sets and of ℝ by diagonalization; a general form of the argument.
duration: 40
prerequisites: [countable-sets]
---

In 1891, Cantor gave a short proof that no sequence of infinite binary sequences contains all of them. The method, called **diagonalization**, is the most frequently used argument in computability theory: it shows that the halting problem is undecidable, that there are total computable functions which are not primitive recursive, and, in more elaborate forms, it underlies most constructions of non-computable sets. This lesson presents the argument, isolates its general form, and derives the uncountability of $2^\nat$, $\nat^\nat$, $\mathcal P(A)$ and $\mathbb R$.

## Cantor space

:::definition{#def-cantor-space}
**Cantor space** is the set $\cs$ of infinite binary sequences, that is, of functions $X : \nat \to \{0, 1\}$. For $X \in \cs$ and $n \in \nat$, the value $X(n)$ is the **$n$-th bit** of $X$, and one writes $X = X(0)\,X(1)\,X(2) \cdots$.
:::

A sequence $X \in \cs$ and the set $\{ n : X(n) = 1 \} \subseteq \nat$ determine each other: the map $X \mapsto \{ n : X(n) = 1 \}$ is a bijection from $\cs$ onto $\mathcal P(\nat)$, whose inverse sends a set to its **characteristic function**. In computability theory the two points of view are used interchangeably: the same letter $X$ denotes a subset of $\nat$ and its characteristic function, so that $n \in X$ if and only if $X(n) = 1$.

Finite binary strings are written $\sigma, \tau, \dots$; the set of finite binary strings is $2^{<\nat}$, the length of $\sigma$ is $|\sigma|$, and $X \upharpoonright n = X(0) \cdots X(n-1)$ is the **prefix** of length $n$ of $X$. By :ref{#prop-strings-countable}, $2^{<\nat}$ is countable.

## The diagonal argument

:::theorem[Cantor]{#thm-cantor-diagonal}
The set $\cs$ is uncountable: for every sequence $X_0, X_1, X_2, \dots$ of elements of $\cs$, the sequence $Y$ defined by
$$
Y(n) = 1 - X_n(n)
$$
is different from every $X_n$.
:::

:::proof{of=thm-cantor-diagonal}
For every $n$, the sequences $Y$ and $X_n$ differ at position $n$, since $Y(n) = 1 - X_n(n) \neq X_n(n)$. So $Y$ is none of the $X_n$. Hence no function $\nat \to \cs$ is surjective, and $\cs$, which is non-empty, is not countable by :ref{#prop-countable-characterizations}.
:::

:::figure[The sequences $X_n$ written as the rows of an infinite table. The sequence $Y$ is obtained by flipping the bits of the diagonal, so that it differs from row $n$ in column $n$.]
<svg class="fig" viewBox="0 0 400 270" width="400" role="img" aria-label="Rows X0 to X4 of a table of bits; the diagonal is marked; the sequence Y flips each diagonal bit"><text x="85.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">0</text><text x="115.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">1</text><text x="145.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">2</text><text x="175.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">3</text><text x="205.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">4</text><text x="235.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">5</text><text x="265.0" y="24" text-anchor="middle" class="mrm muted" font-size="12">6</text><text x="294" y="24" class="mrm muted" font-size="12">⋯</text><text x="34" y="54" text-anchor="middle" class="math" font-size="16">X<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="70" y="34" width="30" height="30" class="cell head-cell"/><text x="85.0" y="54" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="100" y="34" width="30" height="30" class="cell"/><text x="115.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="130" y="34" width="30" height="30" class="cell"/><text x="145.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="160" y="34" width="30" height="30" class="cell"/><text x="175.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="190" y="34" width="30" height="30" class="cell"/><text x="205.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="220" y="34" width="30" height="30" class="cell"/><text x="235.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="250" y="34" width="30" height="30" class="cell"/><text x="265.0" y="54" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="294" y="54" class="mrm muted" font-size="15">⋯</text><text x="34" y="84" text-anchor="middle" class="math" font-size="16">X<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="70" y="64" width="30" height="30" class="cell"/><text x="85.0" y="84" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="100" y="64" width="30" height="30" class="cell head-cell"/><text x="115.0" y="84" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="130" y="64" width="30" height="30" class="cell"/><text x="145.0" y="84" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="160" y="64" width="30" height="30" class="cell"/><text x="175.0" y="84" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="190" y="64" width="30" height="30" class="cell"/><text x="205.0" y="84" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="220" y="64" width="30" height="30" class="cell"/><text x="235.0" y="84" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="250" y="64" width="30" height="30" class="cell"/><text x="265.0" y="84" text-anchor="middle" class="mrm muted" font-size="15">1</text><text x="294" y="84" class="mrm muted" font-size="15">⋯</text><text x="34" y="114" text-anchor="middle" class="math" font-size="16">X<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="70" y="94" width="30" height="30" class="cell"/><text x="85.0" y="114" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="100" y="94" width="30" height="30" class="cell"/><text x="115.0" y="114" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="130" y="94" width="30" height="30" class="cell head-cell"/><text x="145.0" y="114" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="160" y="94" width="30" height="30" class="cell"/><text x="175.0" y="114" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="190" y="94" width="30" height="30" class="cell"/><text x="205.0" y="114" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="220" y="94" width="30" height="30" class="cell"/><text x="235.0" y="114" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="250" y="94" width="30" height="30" class="cell"/><text x="265.0" y="114" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="294" y="114" class="mrm muted" font-size="15">⋯</text><text x="34" y="144" text-anchor="middle" class="math" font-size="16">X<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="70" y="124" width="30" height="30" class="cell"/><text x="85.0" y="144" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="100" y="124" width="30" height="30" class="cell"/><text x="115.0" y="144" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="130" y="124" width="30" height="30" class="cell"/><text x="145.0" y="144" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="160" y="124" width="30" height="30" class="cell head-cell"/><text x="175.0" y="144" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="190" y="124" width="30" height="30" class="cell"/><text x="205.0" y="144" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="220" y="124" width="30" height="30" class="cell"/><text x="235.0" y="144" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="250" y="124" width="30" height="30" class="cell"/><text x="265.0" y="144" text-anchor="middle" class="mrm muted" font-size="15">1</text><text x="294" y="144" class="mrm muted" font-size="15">⋯</text><text x="34" y="174" text-anchor="middle" class="math" font-size="16">X<tspan class="mrm" font-size="10" dy="4">4</tspan></text><rect x="70" y="154" width="30" height="30" class="cell"/><text x="85.0" y="174" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="100" y="154" width="30" height="30" class="cell"/><text x="115.0" y="174" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="130" y="154" width="30" height="30" class="cell"/><text x="145.0" y="174" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="160" y="154" width="30" height="30" class="cell"/><text x="175.0" y="174" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="190" y="154" width="30" height="30" class="cell head-cell"/><text x="205.0" y="174" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="220" y="154" width="30" height="30" class="cell"/><text x="235.0" y="174" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="250" y="154" width="30" height="30" class="cell"/><text x="265.0" y="174" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="294" y="174" class="mrm muted" font-size="15">⋯</text><text x="145.0" y="200" text-anchor="middle" class="mrm muted" font-size="15">⋮</text><line x1="70" y1="210" x2="280" y2="210" class="axis"/><text x="34" y="238" text-anchor="middle" class="math" font-size="16">Y</text><rect x="70" y="218" width="30" height="30" class="cell head-cell"/><text x="85.0" y="238" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><rect x="100" y="218" width="30" height="30" class="cell head-cell"/><text x="115.0" y="238" text-anchor="middle" class="mrm" font-size="15" font-weight="600">0</text><rect x="130" y="218" width="30" height="30" class="cell head-cell"/><text x="145.0" y="238" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><rect x="160" y="218" width="30" height="30" class="cell head-cell"/><text x="175.0" y="238" text-anchor="middle" class="mrm" font-size="15" font-weight="600">0</text><rect x="190" y="218" width="30" height="30" class="cell head-cell"/><text x="205.0" y="238" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><rect x="220" y="218" width="30" height="30" class="cell"/><text x="235.0" y="238" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="250" y="218" width="30" height="30" class="cell"/><text x="265.0" y="238" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="294" y="238" class="label">Y(n) = 1 − Xₙ(n)</text></svg>
:::

The name of the argument comes from the table: the bits $X_n(n)$ form its diagonal. Two features matter. First, $Y$ is defined **from the sequence** $(X_n)$, explicitly: the proof does not only show that some sequence is missing, it computes one. Second, each $X_n$ is defeated at a position of its own, so that the constraints on $Y$ never conflict.

:::quiz[the diagonal argument]
Why is $Y$ made to differ from $X_n$ at position $n$, rather than at a single position $k$ for all rows?

- [x] Each row needs a position where $Y$ is forced to differ from it, and distinct rows must use distinct positions, or their constraints may conflict.

  The bit $Y(k)$ cannot differ both from a row with $X_m(k) = 0$ and from a row with $X_{m'}(k) = 1$.
- [ ] Because the diagonal is the only part of the table that is defined.

  Every entry $X_n(m)$ is defined.
- [ ] It does not matter; any fixed position would do.

  A single bit $Y(k)$ differs only from the rows $X_m$ with $X_m(k) \neq Y(k)$; the rows that agree with $Y$ at position $k$ are not defeated.

---

Can the argument be defeated by adding $Y$ to the list, for instance as $X'_0 = Y$ and $X'_{n+1} = X_n$?

- [x] No: the theorem applies to the new list as well, and produces a sequence $Y'$ that is not in it.

  The argument applies to every list, so no modification of a list can make it complete.
- [ ] Yes, which shows that $\cs$ is countable.

  The new list is again a sequence of elements of $\cs$, and the theorem produces an element missing from it; no list is complete.
- [ ] Only if $Y$ is equal to some $X_n$.

  By construction it is equal to none of them.

---

Let $X_n$ be the characteristic function of $\{n\}$, so that row $n$ has a single $1$, in column $n$. What is $Y$?

- [x] The sequence $000\cdots$, the characteristic function of $\emptyset$.

  Every diagonal bit is $1$, so every bit of $Y$ is $0$. Indeed $\emptyset$ is not a singleton.
- [ ] The sequence $111\cdots$.

  This would be obtained by copying the diagonal rather than flipping it.
- [ ] The sequence $1000\cdots$.

  This is $X_0$, which differs from $Y$ at position $0$.
:::

## A general form

The argument uses neither binary values nor the indexing by integers in an essential way. Its general form is the following.

:::proposition[Diagonal lemma]{#prop-diagonal-general}
Let $A$ and $B$ be sets, $F : A \times A \to B$ a function, and $\delta : B \to B$ a function without fixed point, that is, $\delta(b) \neq b$ for every $b \in B$. Then the function $g : A \to B$ defined by
$$
g(a) = \delta\big(F(a, a)\big)
$$
is different from each function $F(e, \cdot) : a \mapsto F(e, a)$, for $e \in A$.
:::

:::proof{of=prop-diagonal-general}
For $e \in A$, $g(e) = \delta(F(e, e)) \neq F(e, e)$, so $g$ and $F(e, \cdot)$ differ at $e$.
:::

A function $F : A \times A \to B$ is the same thing as a family $(F(e, \cdot))_{e \in A}$ of functions $A \to B$, indexed by $A$, that is, a function from $A$ to the set $B^A$ of functions from $A$ to $B$. The lemma says that such a family never contains all functions $A \to B$, as soon as $B$ has a fixed-point-free map. Read contrapositively:

:::corollary[Lawvere's fixed point theorem]{#cor-lawvere}
If there is a surjection from $A$ onto $B^A$, then every function $\delta : B \to B$ has a fixed point.
:::

:::proof{of=cor-lawvere}
Let $e \mapsto F_e$ be a surjection from $A$ onto $B^A$, and let $F(e, a) = F_e(a)$. If $\delta$ had no fixed point, the function $g$ of :ref{#prop-diagonal-general} would differ from every $F_e$, contradicting surjectivity.
:::

If $B$ has at least two elements $b_0 \neq b_1$, the map exchanging $b_0$ and $b_1$ and fixing every other element has no fixed point, so there is no surjection from $A$ onto $B^A$. The fixed point form is not a curiosity: Kleene's fixed point theorem in the course on fundamentals (:ref{#thm-fixed-point}) has the same structure, with a numbering of partial computable functions in place of the surjection, and with the conclusion that every total computable transformation $f$ of programs has a fixed point up to the function computed: $\Phi_{f(e)} = \Phi_e$ for some $e$.

:::example{#ex-diagonal-instances}
1. $A = \nat$, $B = \{0, 1\}$, $\delta(b) = 1 - b$, and $F(n, m) = X_n(m)$ gives :ref{#thm-cantor-diagonal}.
2. $A = B = \nat$, $\delta(b) = b + 1$: for every sequence $(f_n)$ of functions $\nat \to \nat$, the function $g(n) = f_n(n) + 1$ differs from every $f_n$. So the **Baire space** $\nat^\nat$ of functions $\nat \to \nat$ is uncountable.
3. $A$ arbitrary, $B = \{0, 1\}$: functions $A \to \{0, 1\}$ are characteristic functions of subsets of $A$; this gives the theorem of the next section.
:::

:::quiz[the diagonal lemma]
Why is the hypothesis that $\delta$ has no fixed point needed?

- [x] It guarantees $g(e) \neq F(e, e)$ for every $e$; if $\delta(b) = b$ for some $b$, then $g(e) = F(e, e)$ whenever $F(e, e) = b$.

  For instance, with $\delta$ the identity, $g$ is the diagonal $a \mapsto F(a, a)$ itself, which may well be one of the rows.
- [ ] To make $g$ well defined.

  $g$ is well defined for every function $\delta$.
- [ ] To make $g$ injective.

  Injectivity of $g$ plays no role.

---

For $B = \nat$ and $\delta(b) = b + 1$, which property of $g(n) = f_n(n) + 1$ goes beyond "$g$ differs from every $f_n$"?

- [x] $g(n) > f_n(n)$ for every $n$: $g$ exceeds each $f_n$ at its own diagonal position.

  This stronger form is the basis of growth arguments, in which one builds a function that exceeds each function of a list at some point, or eventually.
- [ ] $g(n) > f_m(n)$ for all $m$ and $n$.

  Only the diagonal values are controlled: $f_0$ may be much larger than $g$ at $n = 1$.
- [ ] $g$ is increasing.

  Nothing forces that.
:::

## Every set is smaller than its power set

:::theorem[Cantor]{#thm-cantor-powerset}
For every set $A$, there is no surjection from $A$ onto its power set $\mathcal P(A)$. Hence $|A| < |\mathcal P(A)|$.
:::

:::proof{of=thm-cantor-powerset}
Let $f : A \to \mathcal P(A)$, and let
$$
D = \{ a \in A : a \notin f(a) \}.
$$
If $D = f(d)$ for some $d \in A$, then $d \in D$ if and only if $d \notin f(d) = D$, a contradiction. So $D$ is not in the image of $f$. Finally, $a \mapsto \{a\}$ is an injection $A \to \mathcal P(A)$, so $|A| \leq |\mathcal P(A)|$; and $|A| \neq |\mathcal P(A)|$, since a bijection would be a surjection.
:::

:::quiz[the proof of Cantor's theorem]
How does this proof relate to the diagonal argument, when $A = \nat$?

- [x] The set $f(n)$ plays the role of the row $X_n$, and "$n \in D$ if and only if $n \notin f(n)$" is "flip the $n$-th bit of the $n$-th row".

  $D$ is the sequence $Y$ of the diagonal argument, seen as a set.
- [ ] $D$ corresponds to the first row of the table.

  $D$ corresponds to the diagonal sequence $Y$, built from all the rows, not to any single row.
- [ ] They are unrelated arguments; the second uses the axiom of choice.

  Neither proof uses the axiom of choice: $D$ is defined explicitly from $f$.

---

What is $D$ when $A = \nat$ and $f(n) = \{0, 1, \dots, n\}$?

- [x] $D = \emptyset$.

  Every $n$ belongs to $f(n)$. And indeed $\emptyset$ is not of the form $\{0, \dots, n\}$.
- [ ] $D = \nat$.

  $D$ consists of the $n$ with $n \notin f(n)$, and there is none.
- [ ] $D = \{0\}$.

  $0 \in f(0) = \{0\}$, so $0 \notin D$.
:::

Iterating, $\nat$, $\mathcal P(\nat)$, $\mathcal P(\mathcal P(\nat))$, … is a sequence of infinite sets of strictly increasing cardinalities: there is no largest cardinality.

:::remark[Russell's paradox]{#rem-russell}
Apply the proof to a hypothetical set $V$ of all sets, with $f$ the identity: every subset of $V$ is a set, hence an element of $V$, so $f(x) = x$ for $x \in \mathcal P(V)$ (and, say, $f(x) = \emptyset$ for the elements of $V$ that are not sets) is a surjection onto $\mathcal P(V)$. The diagonal set is $D = \{ x : x \notin x \}$, essentially Russell's set, and the contradiction is Russell's paradox (1901). In axiomatic set theory, the conclusion is that there is no set of all sets; the collection $\{x : x \notin x\}$ exists only as a class.
:::

## The real numbers

The diagonal argument gives a short proof of Cantor's first uncountability theorem (1874). Decimal expansions need some care, because some real numbers have two of them: $0.1999\cdots = 0.2000\cdots$. For a real number $x$ and $k \geq 1$, let
$$
d_k(x) = \lfloor 10^k x \rfloor - 10 \lfloor 10^{k-1} x \rfloor \in \{0, 1, \dots, 9\}
$$
be the $k$-th decimal digit of the fractional part $x - \lfloor x \rfloor$, in the expansion that does not end with infinitely many $9$s.

:::theorem[Cantor]{#thm-reals-uncountable}
The set $\mathbb R$ is uncountable: for every sequence $(x_n)_{n \in \nat}$ of real numbers, the number
$$
r = \sum_{n \in \nat} c_n \, 10^{-(n+1)}, \qquad c_n = \begin{cases} 4 & \text{if } d_{n+1}(x_n) = 5,\\ 5 & \text{otherwise,}\end{cases}
$$
is different from every $x_n$.
:::

:::proof{of=thm-reals-uncountable}
We first show $d_{k}(r) = c_{k-1}$ for every $k \geq 1$. For every $k \geq 0$, write
$$
10^k r = \sum_{n < k} c_n \, 10^{k-1-n} + t_k, \qquad t_k = \sum_{n \geq k} c_n \, 10^{k-1-n}.
$$
The first sum is an integer $N_k$, and since every $c_n$ lies in $\{4, 5\}$, the tail satisfies $0 < \tfrac49 \leq t_k \leq \tfrac59 < 1$. So $\lfloor 10^k r \rfloor = N_k$, and $d_k(r) = N_k - 10 N_{k-1} = c_{k-1}$.

Now if $r = x_n$, then $d_{n+1}(x_n) = d_{n+1}(r) = c_n$, which contradicts the definition of $c_n$, chosen different from $d_{n+1}(x_n)$.
:::

The digits $4$ and $5$ are chosen so that the tail $t_k$ stays below $1$, which makes $0.c_0c_1c_2\cdots$ the expansion of $r$ that does not end with $9$s; any two digits other than $9$ would do as well. The digit $9$ must be avoided: a rule that only requires $c_n \neq d_{n+1}(x_n)$ could produce $c_0 = 0$ and $c_n = 9$ for all $n \geq 1$, so that $r = 0.0999\cdots = 0.1$, while $x_0 = 0.1$ has $d_1(x_0) = 1 \neq c_0$.

:::quiz[the uncountability of the reals]
In the proof, where is it used that $c_n \in \{4, 5\}$, rather than merely $c_n \neq d_{n+1}(x_n)$?

- [x] To get $t_k < 1$, so that $\lfloor 10^k r \rfloor$ is the integer formed by the first $k$ digits $c_0, \dots, c_{k-1}$.

  With arbitrary digits, $t_k$ could equal $1$ (for digits all equal to $9$), and the digits $d_k(r)$ would no longer be the $c_{k-1}$.
- [ ] To ensure $r \in (0, 1)$.

  Every choice of digits gives $r \in [0, 1]$, and this is not used.
- [ ] To ensure that $r$ is irrational.

  The proof does not need $r$ to be irrational; for some sequences $(x_n)$, $r$ is rational.
:::

## Exercises

::::exercise{difficulty=1}
Show that the set of infinite subsets of $\nat$, and the set of strictly increasing functions $\nat \to \nat$, are uncountable.

:::solution
The map $X \mapsto \{ 2n + X(n) : n \in \nat \}$ is an injection of $\cs$ into the set of infinite subsets of $\nat$: the image contains exactly one element of $\{2n, 2n+1\}$ for each $n$, and $X(n)$ is its parity. Similarly, $X \mapsto (n \mapsto 2n + X(n))$ is an injection of $\cs$ into the set of strictly increasing functions, since $2n + X(n) \leq 2n + 1 < 2(n+1) + X(n+1)$. A set into which $\cs$ injects is uncountable, since otherwise $\cs$ would be countable by :ref{#cor-subset-countable}.
:::
::::

::::exercise{difficulty=2}
Show that the set of bijections $\nat \to \nat$ is uncountable.

:::solution
To $X \in \cs$, associate the permutation $\pi_X$ that exchanges $2n$ and $2n + 1$ when $X(n) = 1$, and fixes them when $X(n) = 0$. It is a bijection (it is its own inverse), and $X \mapsto \pi_X$ is injective, since $X(n) = 1$ if and only if $\pi_X(2n) = 2n + 1$. Conclude as in the previous exercise.
:::
::::

::::exercise{difficulty=2}
(Cantor's proof of 1874.) Let $(x_n)$ be a sequence of real numbers. Construct closed intervals $[a_0, b_0] \supseteq [a_1, b_1] \supseteq \cdots$ with $b_n - a_n = 3^{-n}$ and $x_n \notin [a_{n+1}, b_{n+1}]$, and deduce that some real number differs from every $x_n$. Which property of $\mathbb R$ is used?

:::solution
Start from $[a_0, b_0] = [0, 1]$. Given $[a_n, b_n]$, cut it into three closed thirds; $x_n$ belongs to at most two of them, since the first and the last third are disjoint. Let $[a_{n+1}, b_{n+1}]$ be the leftmost third not containing $x_n$. The sequence $(a_n)$ is non-decreasing and bounded by $b_0$, so it has a limit $r$, by the **completeness** of $\mathbb R$; and $a_m \leq r \leq b_m$ for every $m$, since $a_n \leq b_m$ for all $n$ and $m$. Then $r \in [a_{n+1}, b_{n+1}]$, so $r \neq x_n$, for every $n$. Over $\mathbb Q$, which is countable, the limit $r$ need not exist.
:::
::::

::::exercise{difficulty=2}
Let $(X_n)$ be a sequence of elements of $\cs$. Show that the set of $Y \in \cs$ different from every $X_n$ is uncountable.

:::solution
Let $M = \cs \setminus \{ X_n : n \in \nat \}$. It is non-empty by :ref{#thm-cantor-diagonal}. If it were countable, there would be a surjection $m \mapsto Z_m$ from $\nat$ onto $M$, and the sequence $X_0, Z_0, X_1, Z_1, \dots$, that is, $W_{2n} = X_n$ and $W_{2n+1} = Z_n$, would enumerate all of $\cs$, contradicting :ref{#thm-cantor-diagonal}. The lesson on the continuum shows more: $M$ is equipotent to $\cs$.
:::
::::

## Notes and references

The diagonal argument appears in Cantor's note of 1891, where it is applied to binary sequences and then to the power set of an arbitrary set. The 1874 proof of the uncountability of $\mathbb R$ uses nested intervals. The general form of the diagonal lemma and its fixed point reading are due to Lawvere, in the setting of cartesian closed categories; Yanofsky gives an elementary account, with applications to the paradoxes and to incompleteness. Russell communicated his paradox to Frege in a letter of 1902, and published it in the *Principles of Mathematics*.

- G. Cantor, *Über eine elementare Frage der Mannigfaltigkeitslehre*, Jahresbericht der Deutschen Mathematiker-Vereinigung 1 (1891), 75–78.
- F. W. Lawvere, *Diagonal arguments and cartesian closed categories*, in *Category Theory, Homology Theory and their Applications II*, Lecture Notes in Mathematics 92, Springer, 1969, 134–145.
- N. S. Yanofsky, *A universal approach to self-referential paradoxes, incompleteness and fixed points*, Bulletin of Symbolic Logic 9 (2003), 362–386.
- B. Russell, *The Principles of Mathematics*, Cambridge University Press, 1903.
