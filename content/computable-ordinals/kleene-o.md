---
title: Computable ordinals and Kleene's O
summary: Computable well-orderings and the Church–Kleene ordinal; Kleene's system of notations O; addition of notations by the recursion theorem; the Markwald–Kleene theorem that the constructive ordinals are exactly the computable ones; relativization.
duration: 40
prerequisites: [ordinals, fundamentals/fixed-point]
---

Only countably many ordinals can be described by an algorithm. There are two natural ways of doing so. In Cantor's spirit, an ordinal is **computable** if it is the order type of a computable well-ordering of numbers. In von Neumann's spirit, an ordinal is **constructive** if it has a **notation**: a number that tells whether the ordinal is zero, a successor or a limit, and in the last two cases gives notations for its predecessor or for a sequence converging to it. Kleene's system $\mathcal O$ of notations makes the second idea precise. The two notions define the same ordinals, whose supremum is the Church–Kleene ordinal $\omega_1^{\mathrm{CK}}$.

## Computable well-orderings

:::definition{#def-computable-ordinal}
An ordinal $\alpha$ is **computable** if it is the order type of a computable relation $R \subseteq \nat \times \nat$ that well-orders its field $F = \{ x : (x, x) \in R \}$: $R \subseteq F \times F$, and $(x, y) \in R$ means $x \leq_R y$. The same convention defines c.e. well-orderings and, without the well-foundedness condition, computable and c.e. linear orders.
:::

:::proposition{#prop-computable-ordinals-basic}
1. If $\alpha$ is computable and $\beta < \alpha$, then $\beta$ is computable.
2. If $\alpha$ and $\beta$ are computable, so are $\alpha + \beta$ and $\alpha \cdot \beta$.
3. From an index of a c.e. linear order with infinite field, one computes an index of a computable linear order of $\nat$ isomorphic to it. In particular, the order type of every c.e. well-ordering is computable.
:::

:::proof{of=prop-computable-ordinals-basic}
1. If $\beta < \alpha = |R|$, then $\beta$ is the type of the initial segment of $R$ below some element $a$, defined by the computable relation $\{ (x, y) \in R : (y, a) \in R,\ y \neq a \}$.
2. Represent $\alpha + \beta$ on the disjoint union of the fields, coded by $\langle 0, x \rangle$ and $\langle 1, y \rangle$, with all elements of the first copy below those of the second; and $\alpha \cdot \beta$ on pairs $\langle x, y \rangle$ ordered by comparing $y$ first and then $x$ (the anti-lexicographic order).
3. Let $R$ be a c.e. linear order of its field $F = \{ x : (x, x) \in R \}$, which is c.e. If $F$ is infinite, let $f(n)$ be the $n$-th element of $F$ in order of enumeration, repetitions omitted: $f$ is a computable bijection from $\nat$ onto $F$, and $S = \{ (m, n) : (f(m), f(n)) \in R \}$ is a c.e. linear order of $\nat$ isomorphic to $R$. It is computable: for $m \neq n$, exactly one of $(m, n)$ and $(n, m)$ belongs to $S$, so $S$ is decided by waiting until one of them is enumerated. This procedure is uniform in an index of $R$. If $R$ is a well-ordering with finite field, its type is finite, hence computable.
:::

:::definition{#def-omega1ck}
The **Church–Kleene ordinal** $\omega_1^{\mathrm{CK}}$ is the least ordinal that is not computable.
:::

By (1), the computable ordinals are exactly the ordinals below $\omega_1^{\mathrm{CK}}$. There are countably many computable relations, so $\omega_1^{\mathrm{CK}}$ is countable. By (2), it is a limit ordinal, closed under addition and multiplication. One can show that it is also closed under exponentiation, a fact we do not use; the first exercise shows that $\varepsilon_0$ is computable.

## Kleene's O

:::definition[Kleene]{#def-kleene-o}
The set $\mathcal O \subseteq \nat$ of **notations**, the map $a \mapsto |a|$ from $\mathcal O$ to ordinals, and the relation $<_{\mathcal O}$ are defined simultaneously as the least sets satisfying:

1. $1 \in \mathcal O$ and $|1| = 0$;
2. if $a \in \mathcal O$, then $2^a \in \mathcal O$, $|2^a| = |a| + 1$, and $b <_{\mathcal O} 2^a$ if and only if $b = a$ or $b <_{\mathcal O} a$;
3. if $\Phi_e$ is total, $\Phi_e(n) \in \mathcal O$ and $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$ for every $n$, then $3 \cdot 5^e \in \mathcal O$, $|3 \cdot 5^e| = \sup_n |\Phi_e(n)|$, and $b <_{\mathcal O} 3 \cdot 5^e$ if and only if $b <_{\mathcal O} \Phi_e(n)$ for some $n$.

An ordinal is **constructive** if it is $|a|$ for some $a \in \mathcal O$.
:::

A notation tells which case applies, by its prime factorization, and gives the predecessor or a fundamental sequence. The cases are exclusive on $\mathcal O$: $1 = 2^0$, but $0 \notin \mathcal O$, so $1$ is not of the form $2^a$ with $a \in \mathcal O$. A finite ordinal $n$ has exactly one notation, obtained from $1$ by $n$ applications of $a \mapsto 2^a$, but every infinite constructive ordinal has infinitely many: a limit has one for each program of each of its fundamental sequences, and $\lambda + n$ has one for each notation of $\lambda$. The relation $<_{\mathcal O}$ is a partial order on $\mathcal O$ with $b <_{\mathcal O} a \Rightarrow |b| < |a|$, but two notations of the same ordinal on different branches are incomparable.

:::proposition{#prop-kleene-o-basic}
1. For $a \in \mathcal O$, the set $\{ b : b <_{\mathcal O} a \}$ is well-ordered by $<_{\mathcal O}$, with order type $|a|$, and $\{ |b| : b <_{\mathcal O} a \} = |a|$. In particular the constructive ordinals are closed downward.
2. There is a c.e. relation $R$ such that for every $a \in \mathcal O$ and every $b$, $b <_{\mathcal O} a$ if and only if $(b, a) \in R$.
:::

:::proof{of=prop-kleene-o-basic}
1. By induction along the inductive definition. For $1$, the set is empty. For $2^a$, the set is $\{ b : b <_{\mathcal O} a \} \cup \{ a \}$, of type $|a| + 1$, with ordinals $|a| \cup \{ |a| \} = |a| + 1$. For $3 \cdot 5^e$, the set is the increasing union of the sets below $\Phi_e(n)$, each an initial segment of the next one by the induction hypothesis and the fact that $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$; its type and its set of ordinals are the supremum $\sup_n |\Phi_e(n)|$.
2. Let $R$ be the least relation containing, for every $a \geq 1$, the pair $(a, 2^a)$ and the pairs $(b, 2^a)$ with $(b, a) \in R$, and containing $(b, 3 \cdot 5^e)$ whenever $\Phi_e(n)\converge$ and $(b, \Phi_e(n)) \in R$ or $b = \Phi_e(n)$, for some $n$. It is generated by c.e. rules, so it is c.e. By induction on $a \in \mathcal O$, $R(\cdot, a)$ is $\{ b : b <_{\mathcal O} a \}$; the restriction $a \geq 1$ ensures that $R(\cdot, 1)$ is empty.
:::

The relation $<_{\mathcal O}$ is therefore c.e. on each initial segment, uniformly in a notation of its upper bound. The set $\mathcal O$ itself is not c.e., nor even arithmetic: the next lesson shows that it is $\Pi^1_1$ but not $\Sigma^1_1$ (:ref{#cor-boundedness}).

## From notations to well-orderings and back

:::proposition{#prop-constructive-computable}
Every constructive ordinal is computable. Moreover, there is a total computable function that maps every $a \in \mathcal O$ to an index of a computable well-ordering of type $|a|$.
:::

:::proof{of=prop-constructive-computable}
Let $R$ be the c.e. relation of :ref{#prop-kleene-o-basic} (2), and let $S_a$ be the set of pairs $(b, c)$ with $(b, a) \in R$, $(c, a) \in R$, and $b = c$ or $(b, c) \in R$. It is c.e., uniformly in $a$. For $a \in \mathcal O$, every $c <_{\mathcal O} a$ is in $\mathcal O$, so $S_a$ is the order $\leq_{\mathcal O}$ on $\{ b : b <_{\mathcal O} a \}$, a well-ordering of type $|a|$ by :ref{#prop-kleene-o-basic} (1).

It is decidable whether $a$ is one of the notations $1, 2^1, 2^{2^1}, \dots$ of the finite ordinals; if it is the notation of $n$, output a fixed index of the usual order on $\{ 0, \dots, n - 1 \}$. Otherwise, if $a \in \mathcal O$, the sequence $a, a_1, a_2, \dots$ with $a = 2^{a_1}$, $a_1 = 2^{a_2}$, … reaches a notation $3 \cdot 5^e \leq_{\mathcal O} a$, so $|a| \geq \omega$ and $S_a$ has an infinite field; output the index given by :ref{#prop-computable-ordinals-basic} (3) for $S_a$. This function is total computable, and its value on $a \in \mathcal O$ is an index of a computable well-ordering of type $|a|$.
:::

The converse requires arithmetic on notations, defined by the recursion theorem.

:::lemma{#lem-notation-sum}
There is a total computable function $+_{\mathcal O}$ such that for all $a, b \in \mathcal O$, $a +_{\mathcal O} b \in \mathcal O$, $|a +_{\mathcal O} b| = |a| + |b|$, $a \leq_{\mathcal O} a +_{\mathcal O} b$, $a <_{\mathcal O} a +_{\mathcal O} b$ when $b \neq 1$, and $a +_{\mathcal O} c <_{\mathcal O} a +_{\mathcal O} b$ whenever $c <_{\mathcal O} b$.
:::

:::proof{of=lem-notation-sum}
By the recursion theorem (:ref{#cor-self-reference}), applied to a pair $(a, b)$ as input, there is a partial computable function $+_{\mathcal O}$ satisfying
$$
\begin{aligned}
a +_{\mathcal O} 1 &= a, \\
a +_{\mathcal O} 2^c &= 2^{a +_{\mathcal O} c} \quad \text{for } c \geq 1, \\
a +_{\mathcal O} 3 \cdot 5^e &= 3 \cdot 5^{h(a, e)},
\end{aligned}
$$
where $h(a, e)$ is an index of the function $n \mapsto a +_{\mathcal O} \Phi_e(n)$, computed from $a$, $e$ and the index of $+_{\mathcal O}$ given by the recursion theorem, and $a +_{\mathcal O} b = 1$ for all other $b$. It is total, by induction on $b$: the successor case calls the function on $c < 2^c$, and the limit case only computes an index, without evaluating $\Phi_e$.

The properties are proved by induction on $b \in \mathcal O$. For $b = 1$ they are immediate. For $b = 2^c$ with $c \in \mathcal O$, the notation $a +_{\mathcal O} b = 2^{a +_{\mathcal O} c}$ belongs to $\mathcal O$, with $|a +_{\mathcal O} b| = |a| + |c| + 1 = |a| + |b|$, and $a \leq_{\mathcal O} a +_{\mathcal O} c <_{\mathcal O} a +_{\mathcal O} b$; if $d <_{\mathcal O} b$, then $d \leq_{\mathcal O} c$, so $a +_{\mathcal O} d \leq_{\mathcal O} a +_{\mathcal O} c <_{\mathcal O} a +_{\mathcal O} b$. For $b = 3 \cdot 5^e$, the terms $a +_{\mathcal O} \Phi_e(n)$ are in $\mathcal O$, and $a +_{\mathcal O} \Phi_e(n) <_{\mathcal O} a +_{\mathcal O} \Phi_e(n+1)$ by the last property for $\Phi_e(n+1)$; so $a +_{\mathcal O} b \in \mathcal O$, and $|a +_{\mathcal O} b| = \sup_n (|a| + |\Phi_e(n)|) = |a| + |b|$, since addition is continuous in its right argument. If $d <_{\mathcal O} b$, then $d <_{\mathcal O} \Phi_e(n)$ for some $n$, and $a +_{\mathcal O} d <_{\mathcal O} a +_{\mathcal O} \Phi_e(n) <_{\mathcal O} a +_{\mathcal O} b$. Finally $a \leq_{\mathcal O} a +_{\mathcal O} \Phi_e(0) <_{\mathcal O} a +_{\mathcal O} b$.
:::

:::lemma{#lem-notation-sup}
There is a total computable function $u$ such that if $W_e \subseteq \mathcal O$, then $u(e) \in \mathcal O$ and $|u(e)| \geq |c|$ for every $c \in W_e$.
:::

:::proof{of=lem-notation-sup}
Let $d_n$ be the sum, with $+_{\mathcal O}$ in the order of enumeration, of the elements of $W_{e,n}$, and $d_n = 1$ if $W_{e,n}$ is empty. Let $c_0 = 1$ and $c_{n+1} = c_n +_{\mathcal O} 2^{d_n}$. Then $c_n <_{\mathcal O} c_{n+1}$ by :ref{#lem-notation-sum}, the function $n \mapsto c_n$ is total computable with an index computed from $e$, and $u(e) = 3 \cdot 5^{(\text{this index})}$ belongs to $\mathcal O$ when $W_e \subseteq \mathcal O$. Every $c \in W_e$ is in some $W_{e,n}$, and $|c_{n+1}| \geq |d_n| \geq |c|$, since $|x +_{\mathcal O} y| = |x| + |y| \geq |y|$.
:::

:::theorem[Markwald, Kleene]{#thm-markwald}
Every computable ordinal is constructive: from an index of a computable well-ordering $R$, one computes $a \in \mathcal O$ with $|a| \geq |R|$.
:::

:::proof{of=thm-markwald}
By the recursion theorem (:ref{#cor-self-reference}), there is a total computable function $g$ such that $g(x) = u(i_x)$, where $i_x$ is an index of the c.e. set $\{ 2^{g(y)} : y <_R x \}$, computed from $x$ and an index of $g$. We show by induction along the well-ordering $R$ that $g(x) \in \mathcal O$ and $|g(x)| \geq |R_{<x}|$, the type of the initial segment below $x$. If this holds for all $y <_R x$, then $W_{i_x} \subseteq \mathcal O$, and by :ref{#lem-notation-sup}, $g(x) \in \mathcal O$ and $|g(x)| \geq |g(y)| + 1 \geq |R_{<y}| + 1$ for all $y <_R x$; the supremum of the right-hand side is $|R_{<x}|$. Finally $a = u(i)$, with $i$ an index of $\{ 2^{g(x)} : x \text{ in the field of } R \}$, satisfies $|a| \geq |R|$. Since the constructive ordinals are closed downward, $|R|$ is constructive.
:::

:::corollary{#cor-constructive-computable}
The constructive ordinals are exactly the computable ordinals, that is, the ordinals below $\omega_1^{\mathrm{CK}}$.
:::

The two conversions are uniform, but the second one only gives an upper bound $|a| \geq |R|$. An exact uniform conversion is impossible (see the exercises): a notation contains more information than a well-ordering, namely the decomposition of the ordinal into successor and limit steps.

:::quiz[notations]
In the proof of :ref{#thm-markwald}, why does the set $W_{i_x}$ contain $2^{g(y)}$ rather than $g(y)$?

- [x] To obtain $|g(x)| \geq |g(y)| + 1$ for $y <_R x$, which is needed to reach the type $|R_{<x}| = \sup_{y <_R x} (|R_{<y}| + 1)$.
- [ ] Because $g(y)$ might not belong to $\mathcal O$.

  By the induction hypothesis, $g(y) \in \mathcal O$; the successor is needed for the inequality.
- [ ] To make the set $W_{i_x}$ infinite.

  The set may be finite; the function $u$ handles finite sets.

---

Why does the definition of $g$ not require deciding whether $R$ is a well-ordering?

- [x] Because $g$ is total for every $R$, by the recursion theorem; the well-ordering hypothesis is used only in the proof that its values are notations.
- [ ] Because every computable linear order is a well-ordering.

  Many computable linear orders, such as the order of $\mathbb Q$, are not well-orderings.
- [ ] Because $u$ checks that its input is a subset of $\mathcal O$.

  $u$ checks nothing; its output is a notation only when the input set consists of notations.
:::

## Relativization

All definitions relativize to an oracle $X$: an ordinal is **$X$-computable** if it is the type of an $X$-computable well-ordering, $\mathcal O^X$ is defined with $\Phi^X_e$ in place of $\Phi_e$, and the results of this lesson hold relative to $X$. The least non-$X$-computable ordinal is written $\omega_1^X$. It is countable for every $X$, and every countable ordinal is $X$-computable for some $X$, namely for a set coding a well-ordering of that type; so $\omega_1$ is the supremum of the ordinals $\omega_1^X$. One has $\omega_1^X = \omega_1^{\mathrm{CK}}$ for many non-computable $X$, for instance every arithmetic $X$, and $\omega_1^X > \omega_1^{\mathrm{CK}}$ for $X = \mathcal O$. Both facts rely on the next lesson. If $X$ is arithmetic and $W$ is an $X$-computable well-ordering of type at least $\omega_1^{\mathrm{CK}}$, then a computable linear order is a well-ordering if and only if it embeds into $W$, a $\Sigma^1_1$ condition since $X$ is arithmetic; this contradicts :ref{#prop-pi11-not-sigma11}. For $\mathcal O$, the set $\mathrm{WO}$ of indices of computable well-orderings is $\Pi^1_1$, hence computable in $\mathcal O$ by the $\Pi^1_1$-completeness of $\mathcal O$ (admitted in the next lesson), and the well-orderings with indices $e \in \mathrm{WO}$, placed one after the other in increasing order of $e$, form an $\mathcal O$-computable well-ordering of type at least $\omega_1^{\mathrm{CK}}$.

## Exercises

::::exercise{difficulty=1}
Show that $\varepsilon_0 = \sup \{ \omega, \omega^\omega, \omega^{\omega^\omega}, \dots \}$ is computable.

:::solution
By the recursion theorem, as in :ref{#lem-notation-sum}, there is a total computable function $p$ with $p(1) = 2^1$ (the notation of $1$), $p(2^c) = 3 \cdot 5^{k(c)}$ for $c \geq 1$, where $\Phi_{k(c)}(0) = p(c)$ and $\Phi_{k(c)}(n+1) = \Phi_{k(c)}(n) +_{\mathcal O} p(c)$, and $p(3 \cdot 5^e) = 3 \cdot 5^{k'(e)}$ with $\Phi_{k'(e)}(n) = p(\Phi_e(n))$. By induction on $b \in \mathcal O$, $p(b) \in \mathcal O$, $|p(b)| = \omega^{|b|}$, and $c <_{\mathcal O} b$ implies $p(c) <_{\mathcal O} p(b)$. For $b = 2^c$: $p(c) \neq 1$ since $|p(c)| \geq 1$, so by :ref{#lem-notation-sum} the notations $\Phi_{k(c)}(n)$ are $<_{\mathcal O}$-increasing, of types $\omega^{|c|} \cdot (n+1)$, with supremum $\omega^{|c| + 1}$; and $c' \leq_{\mathcal O} c$ gives $p(c') \leq_{\mathcal O} p(c) = \Phi_{k(c)}(0) <_{\mathcal O} p(b)$. For $b = 3 \cdot 5^e$, the sequence $p(\Phi_e(n))$ is $<_{\mathcal O}$-increasing by the induction hypothesis, and its supremum is $\omega^{|b|}$ by continuity of exponentiation.

Let $x_0 = p(2^1)$, a notation for $\omega$, and $x_{n+1} = x_n +_{\mathcal O} p(x_n)$. Then $x_n <_{\mathcal O} x_{n+1}$, since $p(x_n) \neq 1$, and $|x_{n+1}| \geq \omega^{|x_n|}$, so $|x_n|$ is at least the tower $\omega^{\omega^{\cdots}}$ of height $n + 1$. The sequence $(x_n)$ is computable, and $3 \cdot 5^e$ for an index $e$ of it is a notation of an ordinal at least $\varepsilon_0$. The constructive ordinals being closed downward, $\varepsilon_0$ is constructive, hence computable by :ref{#prop-constructive-computable}.
:::
::::

::::exercise{difficulty=2}
Show that there is a total computable function $f$ such that $f(n)$ is an index of a computable well-ordering of type $\omega + 1$ if $n \in \emptyset'$, and of type $\omega$ otherwise. Deduce that no partial computable function maps every index of a computable well-ordering to a notation for its exact order type.

:::solution
Call a number $x$ **special** if $n$ enters $\emptyset'$ exactly at stage $x$ of a fixed enumeration; whether $x$ is special is decidable, and there is at most one special number. Let $f(n)$ be an index of the order on $\nat$ in which a special number, if there is one, is the largest element, and the other numbers are ordered as usual. It is computable, uniformly in $n$. Its type is $\omega + 1$ if $n \in \emptyset'$, and $\omega$ otherwise.

Suppose that $h$ maps indices of well-orderings to notations of their exact types. Then $h(f(n))$ is a notation for $\omega$ or for $\omega + 1$, and a notation for $\omega + 1$ has the form $2^c$, while a notation for $\omega$ has the form $3 \cdot 5^e$. So $n \in \emptyset'$ if and only if $h(f(n))$ is a power of $2$, which would make $\emptyset'$ computable.
:::
::::

## Notes and references

Church and Kleene (1936–1938) introduced constructive ordinals and the system $\mathcal O$; Markwald (1954) proved that computable and constructive ordinals coincide. Sacks's monograph is the standard reference for higher computability theory.

- S. C. Kleene, *On notation for ordinal numbers*, Journal of Symbolic Logic 3 (1938), 150–155.
- H. Rogers, Jr., *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967, Chapter 11.
- G. E. Sacks, *Higher Recursion Theory*, Perspectives in Mathematical Logic, Springer, 1990.
