---
title: The cardinality of the continuum
summary: The sets of binary sequences, of integer sequences, of real numbers and of real sequences are equipotent; removing a countable set does not change their cardinality; the continuum hypothesis.
duration: 35
prerequisites: [diagonal-argument]
---

The previous lesson exhibited several uncountable sets: Cantor space $\cs$, Baire space $\nat^\nat$, the power set $\mathcal P(\nat)$ and the real line $\mathbb R$. This lesson shows that they all have the same cardinality, called the cardinality of the continuum. The proofs are applications of the Cantor–Bernstein theorem: in each case, two injections are easy to write down, while an explicit bijection would be cumbersome. Along the way, we introduce two codings used throughout computability theory: the join of two sequences, and the coding of a sequence of sequences by a single one.

:::definition{#def-continuum}
A set $A$ has the **cardinality of the continuum** if $|A| = |\mathbb R|$.
:::

## Codings inside Cantor space

:::proposition{#prop-baire-cantor}
$|\nat^\nat| = |\cs|$.
:::

The inclusion $\cs \subseteq \nat^\nat$ gives one injection. For the other, a function $f : \nat \to \nat$ is coded by writing each value in unary, $f(n)$ ones, followed by a zero as a separator.

:::figure[The coding of Baire space into Cantor space. Each value $f(n)$ is written as a block of $f(n)$ ones, closed by a zero.]
<svg class="fig" viewBox="0 0 560 120" width="560" role="img" aria-label="The function 2, 0, 3, 1 coded as the bit sequence 1 1 0 0 1 1 1 0 1 0"><rect x="20" y="20" width="34" height="34" class="cell"/><text x="37.0" y="43" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="54" y="20" width="34" height="34" class="cell"/><text x="71.0" y="43" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="88" y="20" width="34" height="34" class="cell head-cell"/><text x="105.0" y="43" text-anchor="middle" class="mrm" font-size="16">0</text><path d="M23,62 L23,68 L119,68 L119,62" class="muted-stroke" stroke-width="1.1"/><text x="71.0" y="88" text-anchor="middle" class="math" font-size="15">f<tspan class="mrm">(0) = 2</tspan></text><rect x="128" y="20" width="34" height="34" class="cell head-cell"/><text x="145.0" y="43" text-anchor="middle" class="mrm" font-size="16">0</text><path d="M131,62 L131,68 L159,68 L159,62" class="muted-stroke" stroke-width="1.1"/><text x="145.0" y="88" text-anchor="middle" class="math" font-size="15">f<tspan class="mrm">(1) = 0</tspan></text><rect x="168" y="20" width="34" height="34" class="cell"/><text x="185.0" y="43" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="202" y="20" width="34" height="34" class="cell"/><text x="219.0" y="43" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="236" y="20" width="34" height="34" class="cell"/><text x="253.0" y="43" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="270" y="20" width="34" height="34" class="cell head-cell"/><text x="287.0" y="43" text-anchor="middle" class="mrm" font-size="16">0</text><path d="M171,62 L171,68 L301,68 L301,62" class="muted-stroke" stroke-width="1.1"/><text x="236.0" y="88" text-anchor="middle" class="math" font-size="15">f<tspan class="mrm">(2) = 3</tspan></text><rect x="310" y="20" width="34" height="34" class="cell"/><text x="327.0" y="43" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="344" y="20" width="34" height="34" class="cell head-cell"/><text x="361.0" y="43" text-anchor="middle" class="mrm" font-size="16">0</text><path d="M313,62 L313,68 L375,68 L375,62" class="muted-stroke" stroke-width="1.1"/><text x="344.0" y="88" text-anchor="middle" class="math" font-size="15">f<tspan class="mrm">(3) = 1</tspan></text><text x="392" y="43" class="mrm muted" font-size="16">⋯</text></svg>
:::

:::proof{of=prop-baire-cantor}
To $f \in \nat^\nat$, associate the sequence
$$
c(f) = 1^{f(0)}\, 0\, 1^{f(1)}\, 0\, 1^{f(2)}\, 0 \cdots \in \cs,
$$
where $1^k$ is the string of $k$ ones. Formally, $c(f)(m) = 0$ if and only if $m = z_n$ for some $n$, where $z_n = n + \sum_{i \leq n} f(i)$ is the position of the $n$-th zero. The sequence $c(f)$ has infinitely many zeros, at the positions $z_0 < z_1 < \cdots$, and $f$ is recovered from it: $f(0) = z_0$ and $f(n+1) = z_{n+1} - z_n - 1$ is the number of ones between two consecutive zeros. So $c$ is injective, and :ref{#thm-cantor-bernstein} applies.
:::

The map $c$ is a bijection from $\nat^\nat$ onto the set of sequences with infinitely many zeros, but it is not surjective onto $\cs$: the sequences with finitely many zeros, such as $0111\cdots$, are not codes. This is why Cantor–Bernstein is used.

:::definition{#def-join}
1. The **join** of $X, Y \in \cs$ is the sequence $X \oplus Y$ defined by $(X \oplus Y)(2n) = X(n)$ and $(X \oplus Y)(2n+1) = Y(n)$.
2. The **coding** of a sequence $(X_n)_{n \in \nat}$ of elements of $\cs$ is the sequence $\bigoplus_n X_n$ defined by $\big(\bigoplus_n X_n\big)(\langle n, m \rangle) = X_n(m)$, where $\langle \cdot, \cdot \rangle$ is Cantor's pairing function.
:::

:::proposition{#prop-cantor-powers}
The maps $(X, Y) \mapsto X \oplus Y$ and $(X_n)_n \mapsto \bigoplus_n X_n$ are bijections from $\cs \times \cs$ and from $(\cs)^\nat$ onto $\cs$. Hence $|\cs \times \cs| = |(\cs)^\nat| = |\cs|$.
:::

:::proof{of=prop-cantor-powers}
Every $Z \in \cs$ is $X \oplus Y$ for exactly one pair, namely $X(n) = Z(2n)$ and $Y(n) = Z(2n+1)$, since every integer is even or odd, and not both. Similarly, since $\langle \cdot, \cdot \rangle$ is a bijection $\nat^2 \to \nat$ (:ref{#prop-nxn-countable}), every $Z$ is $\bigoplus_n X_n$ for exactly one sequence, namely $X_n(m) = Z(\langle n, m \rangle)$.
:::

In computability theory, $X \oplus Y$ is the canonical way of giving two sets as a single oracle, and $\bigoplus_n X_n$ the way of giving a sequence of sets; the set $X_n$ is the **$n$-th column** of $\bigoplus_n X_n$.

:::quiz[codings inside Cantor space]
Why is the separator $0$ needed in the coding $c(f)$ of :ref{#prop-baire-cantor}?

- [x] Without separators, $1^{f(0)} 1^{f(1)} \cdots$ is $111\cdots$ for every $f$ with infinitely many non-zero values, so the coding would not be injective.

  The zeros mark where each value ends.
- [ ] To make $c(f)$ contain infinitely many ones.

  It need not: for the zero function, $c(f) = 000\cdots$. The separators give infinitely many zeros, not ones.
- [ ] To make $c$ surjective.

  The coding with separators is not surjective either: sequences with finitely many zeros are missed.

---

What is the $3$rd column of $Z = \bigoplus_n X_n$ when $Z$ is the characteristic function of the even numbers?

- [x] It depends on the parities of the numbers $\langle 3, m \rangle$; it is the set of $m$ such that $\langle 3, m \rangle$ is even.

  By definition $X_3(m) = Z(\langle 3, m \rangle)$. For instance $\langle 3, 0 \rangle = 6$ is even and $\langle 3, 1 \rangle = 11$ is odd, so $X_3(0) = 1$ and $X_3(1) = 0$.
- [ ] The even numbers.

  The columns are read along the pairing function, not along positions.
- [ ] The empty set, since $3$ is odd.

  The index $3$ of the column is not a position in $Z$.
:::

## The real line

:::theorem{#thm-continuum}
The sets $\cs$, $\mathcal P(\nat)$, $\nat^\nat$, $[0, 1]$ and $\mathbb R$ are pairwise equipotent.
:::

:::proof{of=thm-continuum}
We have $|\mathcal P(\nat)| = |\cs|$ by characteristic functions, $|\nat^\nat| = |\cs|$ by :ref{#prop-baire-cantor}, and $[0,1)$, $[0,1]$ and $\mathbb R$ are pairwise equipotent by :ref{#ex-intervals-equipotent}. It remains to show $|\cs| = |[0, 1)|$, and we give two injections.

*From $\cs$ to $[0, 1)$.* Let $t(X) = \sum_{n} X(n)\, 3^{-(n+1)}$, which lies in $[0, \tfrac12]$. If $X \neq Y$, let $n$ be the least position where they differ, say $X(n) = 0$ and $Y(n) = 1$. Then
$$
t(Y) - t(X) \;\geq\; 3^{-(n+1)} - \sum_{k > n} 3^{-(k+1)} \;=\; 3^{-(n+1)} - \tfrac12\, 3^{-(n+1)} \;>\; 0,
$$
since the terms at positions $k > n$ contribute at most $3^{-(k+1)}$ each to the difference. So $t$ is injective.

*From $[0, 1)$ to $\cs$.* For $x \in [0, 1)$, let $b(x)(k) = \lfloor 2^{k+1} x \rfloor - 2 \lfloor 2^k x \rfloor$, which is $0$ or $1$. By induction on $n$, $\lfloor 2^n x \rfloor = \sum_{k < n} b(x)(k)\, 2^{n-1-k}$: this holds for $n = 0$ since $\lfloor x \rfloor = 0$, and the inductive step is the definition of $b(x)(n)$. Hence the bits $b(x)$ determine every $\lfloor 2^n x \rfloor$, and therefore $x = \lim_n 2^{-n} \lfloor 2^n x \rfloor$, since $0 \leq x - 2^{-n} \lfloor 2^n x \rfloor < 2^{-n}$. So $b$ is injective.

By :ref{#thm-cantor-bernstein}, $|\cs| = |[0, 1)|$.
:::

The sequence $b(x)$ is the binary expansion of $x$ that does not end with infinitely many ones. The map $b$ is not surjective: the sequences ending with infinitely many ones are missed. The map $t$ uses base $3$ so that distinct sequences cannot produce the same number, which would happen in base $2$, where $0111\cdots$ and $1000\cdots$ both represent $\tfrac12$.

:::quiz[the proof of the theorem]
In the injectivity of $t$, why does base $3$ work where base $2$ fails?

- [x] In base $3$, the digit at the first difference contributes $3^{-(n+1)}$, while all later digits together contribute at most half of it; in base $2$, the later digits can contribute exactly $2^{-(n+1)}$ and compensate.

  This is the computation $\sum_{k > n} 3^{-(k+1)} = \tfrac12 \cdot 3^{-(n+1)}$, against $\sum_{k > n} 2^{-(k+1)} = 2^{-(n+1)}$.
- [ ] Because $3$ is odd.

  The digits are $0$ and $1$ in both cases; what matters is that the base exceeds $2$.
- [ ] Because $t(X) \leq \tfrac12$.

  The bound is a consequence of base $3$, not the reason for injectivity.
:::

:::corollary{#cor-continuum-powers}
$|\mathbb R \times \mathbb R| = |\mathbb R^\nat| = |\mathbb R|$, and $|\mathbb C| = |\mathbb R|$.
:::

:::proof{of=cor-continuum-powers}
Fix a bijection $\beta : \mathbb R \to \cs$, given by the theorem. Then $(x, y) \mapsto \beta(x) \oplus \beta(y)$ and $(x_n)_n \mapsto \bigoplus_n \beta(x_n)$ are bijections onto $\cs$, by :ref{#prop-cantor-powers}. Finally $\mathbb C$ is in bijection with $\mathbb R \times \mathbb R$.
:::

Cantor found this result in 1877, and wrote to Dedekind that he could see it but did not believe it: the plane has no more points than the line. No such bijection is a homeomorphism, by Brouwer's theorem on the invariance of dimension (1911), which we admit; cardinality ignores topology.

## Removing a countable set

:::proposition{#prop-cocountable}
If $M \subseteq \cs$ is countable, then $|\cs \setminus M| = |\cs|$. The same holds for $\mathbb R$ and every set of the cardinality of the continuum.
:::

:::proof{of=prop-cocountable}
Through the bijection of :ref{#prop-cantor-powers}, we may work in $\cs \times \cs$, with $M$ a countable subset of it. The set $M_0 = \{ X : (X, Y) \in M \text{ for some } Y \}$ of first coordinates is countable, as an image of $M$ (:ref{#cor-subset-countable}). By :ref{#thm-cantor-diagonal}, there is $X_0 \notin M_0$. Then $Y \mapsto (X_0, Y)$ is an injection of $\cs$ into $(\cs \times \cs) \setminus M$. The inclusion is an injection in the other direction, and :ref{#thm-cantor-bernstein} concludes. The last sentence follows by transporting through a bijection.
:::

:::corollary{#cor-transcendental-continuum}
The sets of irrational numbers and of transcendental numbers have the cardinality of the continuum.
:::

:::proof{of=cor-transcendental-continuum}
They are the complements in $\mathbb R$ of the countable sets $\mathbb Q$ and of the algebraic numbers (:ref{#ex-algebraic-numbers}).
:::

:::quiz[removing a countable set]
In the proof of :ref{#prop-cocountable}, why does one pass from $\cs$ to $\cs \times \cs$?

- [x] To have room: a whole copy $\{X_0\} \times \cs$ of $\cs$ avoids $M$ as soon as its first coordinate $X_0$ avoids the countable set $M_0$.

  In $\cs$ itself, one would need to find directly an injection of $\cs$ into the complement of $M$.
- [ ] Because $M$ is not countable in $\cs$.

  Countability does not depend on the bijection used to transport $M$.
- [ ] To apply the diagonal argument to pairs.

  The diagonal argument is applied to the first coordinates only.
:::

## Cantor space and the Cantor set

Cantor space and the real line have the same cardinality, but they are different as ordered or topological spaces. In the lexicographic order on $\cs$, defined by $X <_{\mathrm{lex}} Y$ if $X(n) < Y(n)$ at the first position $n$ where $X$ and $Y$ differ, the sequences $0111\cdots$ and $1000\cdots$ have nothing strictly between them, whereas between two real numbers there is always a third. The relevant geometric picture of $\cs$ is a subset of the line.

:::figure[The first stages of the construction of the Cantor set. Each interval of $A_n$ is labeled by the binary string of length $n$ recording the left or right choices that lead to it.]
<svg class="fig" viewBox="0 0 540 172" width="540" role="img" aria-label="The first four stages of the construction of the Cantor set, with binary labels"><text x="20" y="28" text-anchor="middle" class="math" font-size="16">A<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="50.0" y="18" width="480.0" height="8" rx="1.5" class="ink-fill"/><text x="20" y="70" text-anchor="middle" class="math" font-size="16">A<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="50.0" y="60" width="160.0" height="8" rx="1.5" class="accent-fill"/><text x="130.0" y="84" text-anchor="middle" class="mrm muted" font-size="12">0</text><rect x="370.0" y="60" width="160.0" height="8" rx="1.5" class="accent-fill"/><text x="450.0" y="84" text-anchor="middle" class="mrm muted" font-size="12">1</text><text x="20" y="112" text-anchor="middle" class="math" font-size="16">A<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="50.0" y="102" width="53.3" height="8" rx="1.5" class="accent-fill"/><text x="76.7" y="126" text-anchor="middle" class="mrm muted" font-size="12">00</text><rect x="156.7" y="102" width="53.3" height="8" rx="1.5" class="accent-fill"/><text x="183.3" y="126" text-anchor="middle" class="mrm muted" font-size="12">01</text><rect x="370.0" y="102" width="53.3" height="8" rx="1.5" class="accent-fill"/><text x="396.7" y="126" text-anchor="middle" class="mrm muted" font-size="12">10</text><rect x="476.7" y="102" width="53.3" height="8" rx="1.5" class="accent-fill"/><text x="503.3" y="126" text-anchor="middle" class="mrm muted" font-size="12">11</text><text x="20" y="154" text-anchor="middle" class="math" font-size="16">A<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="50.0" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="58.9" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">000</text><rect x="85.6" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="94.4" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">001</text><rect x="156.7" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="165.6" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">010</text><rect x="192.2" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="201.1" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">011</text><rect x="370.0" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="378.9" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">100</text><rect x="405.6" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="414.4" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">101</text><rect x="476.7" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="485.6" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">110</text><rect x="512.2" y="144" width="17.8" height="8" rx="1.5" class="accent-fill"/><text x="521.1" y="168" text-anchor="middle" class="mrm muted" font-size="9.5">111</text><text x="50" y="12" text-anchor="middle" class="mrm muted" font-size="12">0</text><text x="530" y="12" text-anchor="middle" class="mrm muted" font-size="12">1</text></svg>
:::

:::aside[The Cantor set]
Let $A_0 = [0, 1]$, and let $A_{n+1}$ be obtained from $A_n$ by removing the open middle third of each of its intervals, so that $A_1 = [0, \tfrac13] \cup [\tfrac23, 1]$ and $A_n$ is a union of $2^n$ closed intervals of length $3^{-n}$. The **Cantor set** is $\mathcal C = \bigcap_n A_n$. It is the set of real numbers of $[0, 1]$ having a ternary expansion with digits $0$ and $2$ only, and the map $X \mapsto \sum_n 2X(n)\, 3^{-(n+1)}$ is a bijection from $\cs$ onto $\mathcal C$, which preserves the lexicographic order. With the product topology on $\cs$, it is a homeomorphism; this explains the name of Cantor space. We admit these facts, which belong to a course on topology.
:::

## The continuum hypothesis

By :ref{#prop-n-smallest}, every infinite set has cardinality at least $|\nat|$, and $|\nat| < |\mathbb R|$. Cantor conjectured that there is nothing in between.

:::definition{#def-ch}
The **continuum hypothesis** is the statement: every infinite subset of $\mathbb R$ is either countable or of the cardinality of the continuum.
:::

The question remained open for decades, and was the first of the problems listed by Hilbert in 1900. Its status is now known, and we admit it.

:::remark{#rem-ch-independence}
The continuum hypothesis can be neither proved nor refuted from the axioms of ZFC, provided these axioms are consistent. Gödel showed in 1938 that it holds in the constructible universe $L$, so that it cannot be refuted; Cohen showed in 1963, by the method of **forcing**, that it cannot be proved. Forcing has since become a central tool of set theory, and effective versions of it are used in computability theory to build sets with prescribed properties.
:::

For sets of reals with a simple definition, the question has a positive answer. Cantor and Bendixson showed that every uncountable closed subset of $\mathbb R$ contains a copy of the Cantor set, hence has the cardinality of the continuum; this was extended to Borel sets by Alexandrov and Hausdorff, and to analytic sets by Suslin. We admit these results; they are proved in Kechris' book.

## Exercises

::::exercise{difficulty=1}
Show that $|\mathcal P(\nat \times \nat)| = |\mathcal P(\nat)|$, and that the set of all binary relations on $\nat$ has the cardinality of the continuum.

:::solution
A bijection $\nat \times \nat \to \nat$ induces a bijection between the power sets, by taking images. A binary relation on $\nat$ is a subset of $\nat \times \nat$, so the set of relations is $\mathcal P(\nat \times \nat)$, equipotent to $\mathcal P(\nat)$ and hence to $\mathbb R$ by :ref{#thm-continuum}.
:::
::::

::::exercise{difficulty=2}
Show that the set of continuous functions $\mathbb R \to \mathbb R$ has the cardinality of the continuum.

:::solution
Constant functions give an injection of $\mathbb R$. Conversely, a continuous function is determined by its values on $\mathbb Q$, since every real number is a limit of rational numbers. Fixing a bijection $q : \nat \to \mathbb Q$, the map $f \mapsto (f(q(n)))_n$ is therefore an injection into $\mathbb R^\nat$, which has the cardinality of the continuum by :ref{#cor-continuum-powers}. Conclude by :ref{#thm-cantor-bernstein}.
:::
::::

::::exercise{difficulty=2}
Show that the set of all functions $\mathbb R \to \mathbb R$ has a cardinality strictly greater than that of $\mathbb R$.

:::solution
The characteristic functions of subsets of $\mathbb R$ give an injection of $\mathcal P(\mathbb R)$ into the set $\mathbb R^{\mathbb R}$ of all functions. By :ref{#thm-cantor-powerset}, $|\mathbb R| < |\mathcal P(\mathbb R)| \leq |\mathbb R^{\mathbb R}|$. (In fact $|\mathbb R^{\mathbb R}| = |\mathcal P(\mathbb R)|$, since a function is a subset of $\mathbb R \times \mathbb R$, which is equipotent to $\mathbb R$.)
:::
::::

::::exercise{difficulty=2}
Give an explicit bijection between $\cs$ and the set of sequences with infinitely many zeros, using the coding $c$ of :ref{#prop-baire-cantor}. Deduce another proof that $|\nat^\nat| = |\cs|$.

:::solution
The set $M$ of sequences with finitely many zeros is countably infinite: each of them is $\sigma 111\cdots$ for a finite binary string $\sigma$, and there are infinitely many. Let $M_0, M_1, \dots$ be an enumeration of $M$ without repetition. The sequences $E_k = 0^k 1 0 0 0 \cdots$, for $k \in \nat$, are pairwise distinct and have infinitely many zeros. Define $\varphi : \cs \to \cs \setminus M$ by $\varphi(M_k) = E_{2k+1}$, $\varphi(E_k) = E_{2k}$, and $\varphi(X) = X$ for the other sequences. It is injective on each of the three pieces, whose images $\{E_{2k+1}\}$, $\{E_{2k}\}$ and $\cs \setminus (M \cup \{E_k\})$ are disjoint and cover $\cs \setminus M$; so $\varphi$ is a bijection onto the set of sequences with infinitely many zeros. Then $c^{-1} \circ \varphi$ is a bijection from $\cs$ onto $\nat^\nat$.
:::
::::

## Notes and references

The equipotence of the line and the plane is in Cantor's paper of 1878, after an exchange of letters with Dedekind in 1877. The continuum hypothesis is formulated in the same paper. Gödel's and Cohen's results are presented in Kunen's and Jech's textbooks on set theory; the perfect set property for closed, Borel and analytic sets is in Kechris' book.

- G. Cantor, *Ein Beitrag zur Mannigfaltigkeitslehre*, Journal für die reine und angewandte Mathematik 84 (1878), 242–258.
- K. Gödel, *The consistency of the axiom of choice and of the generalized continuum-hypothesis*, Proceedings of the National Academy of Sciences 24 (1938), 556–557.
- P. J. Cohen, *The independence of the continuum hypothesis*, Proceedings of the National Academy of Sciences 50 (1963), 1143–1148.
- K. Kunen, *Set Theory: An Introduction to Independence Proofs*, North-Holland, 1980.
- T. Jech, *Set Theory*, 3rd millennium edition, Springer, 2003.
- A. S. Kechris, *Classical Descriptive Set Theory*, Graduate Texts in Mathematics 156, Springer, 1995.
