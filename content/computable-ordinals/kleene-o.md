---
title: Computable ordinals and Kleene's O
summary: Computable well-orderings and the Church–Kleene ordinal; Kleene's system of notations O; addition of notations by the recursion theorem; the Markwald–Kleene theorem that the constructive ordinals are exactly the computable ones; relativization.
duration: 40
prerequisites: [ordinals, fundamentals/fixed-point]
---

Only countably many ordinals can be described by an algorithm. There are two natural ways of doing so. In Cantor's spirit, an ordinal is **computable** if it is the order type of a computable well-ordering of numbers. In von Neumann's spirit, an ordinal is **constructive** if it has a **notation**: a number that tells whether the ordinal is zero, a successor or a limit, and in the last two cases gives notations for its predecessor or for a sequence converging to it. Kleene's system $\mathcal O$ of notations makes the second idea precise. The two notions define the same ordinals, whose supremum is the Church–Kleene ordinal $\omega_1^{\mathrm{CK}}$.

## Computable well-orderings

:::definition{#def-computable-ordinal}
An ordinal $\alpha$ is **computable** if it is the order type of a computable relation $R \subseteq \nat \times \nat$ that well-orders its field $\{ x : (x, x) \in R \}$, the relation $(x, y) \in R$ meaning $x \leq_R y$.
:::

:::proposition{#prop-computable-ordinals-basic}
1. If $\alpha$ is computable and $\beta < \alpha$, then $\beta$ is computable.
2. If $\alpha$ and $\beta$ are computable, so are $\alpha + \beta$ and $\alpha \cdot \beta$.
3. A c.e. relation that well-orders its field is a computable relation when the field is computable; and every order type of a c.e. well-ordering is computable.
:::

:::proof{of=prop-computable-ordinals-basic}
1. If $\beta < \alpha = |R|$, then $\beta$ is the type of the initial segment of $R$ below some element $a$, defined by the computable relation $\{ (x, y) \in R : (y, a) \in R,\ y \neq a \}$.
2. Represent $\alpha + \beta$ on the disjoint union of the fields, coded by $\langle 0, x \rangle$ and $\langle 1, y \rangle$, with all elements of the first copy below those of the second; and $\alpha \cdot \beta$ on pairs $\langle x, y \rangle$ ordered by comparing $y$ first and then $x$ (the anti-lexicographic order).
3. If $R$ is a c.e. linear order of a field $F$, then for $x \neq y$ in $F$, $(x, y) \notin R$ if and only if $(y, x) \in R$, a c.e. condition; so $R$ restricted to $F \times F$ is computable relative to $F$. The field of a c.e. relation is c.e.; if it is infinite, a computable bijection between $\nat$ and the field, listing it in order of enumeration, transports $R$ to a c.e., hence computable, well-ordering of $\nat$. If it is finite, the type is finite.
:::

:::definition{#def-omega1ck}
The **Church–Kleene ordinal** $\omega_1^{\mathrm{CK}}$ is the least ordinal that is not computable.
:::

By (1), the computable ordinals are exactly the ordinals below $\omega_1^{\mathrm{CK}}$. There are countably many computable relations, so $\omega_1^{\mathrm{CK}}$ is countable. By (2), it is a limit ordinal, closed under addition and multiplication; in fact $\alpha^\beta$ and all ordinals obtained by "explicit" constructions such as $\varepsilon_0$ are computable.

## Kleene's O

:::definition[Kleene]{#def-kleene-o}
The set $\mathcal O \subseteq \nat$ of **notations**, the map $a \mapsto |a|$ from $\mathcal O$ to ordinals, and the relation $<_{\mathcal O}$ are defined simultaneously as the least sets satisfying:

1. $1 \in \mathcal O$ and $|1| = 0$;
2. if $a \in \mathcal O$, then $2^a \in \mathcal O$, $|2^a| = |a| + 1$, and $b <_{\mathcal O} 2^a$ if and only if $b = a$ or $b <_{\mathcal O} a$;
3. if $\Phi_e$ is total, $\Phi_e(n) \in \mathcal O$ and $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$ for every $n$, then $3 \cdot 5^e \in \mathcal O$, $|3 \cdot 5^e| = \sup_n |\Phi_e(n)|$, and $b <_{\mathcal O} 3 \cdot 5^e$ if and only if $b <_{\mathcal O} \Phi_e(n)$ for some $n$.

An ordinal is **constructive** if it is $|a|$ for some $a \in \mathcal O$.
:::

A notation tells which case applies, by its prime factorization, and gives the predecessor or a fundamental sequence. Each constructive ordinal has many notations: limits have infinitely many, through different programs for their fundamental sequences. The relation $<_{\mathcal O}$ is a partial order on $\mathcal O$ with $b <_{\mathcal O} a \Rightarrow |b| < |a|$, but two notations of the same ordinal on different branches are incomparable.

:::proposition{#prop-kleene-o-basic}
1. For $a \in \mathcal O$, the set $\{ b : b <_{\mathcal O} a \}$ is well-ordered by $<_{\mathcal O}$, with order type $|a|$, and $\{ |b| : b <_{\mathcal O} a \} = |a|$. In particular the constructive ordinals are closed downward.
2. There is a c.e. relation $R$ such that for every $a \in \mathcal O$ and every $b$, $b <_{\mathcal O} a$ if and only if $(b, a) \in R$.
:::

:::proof{of=prop-kleene-o-basic}
1. By induction along the inductive definition. For $1$, the set is empty. For $2^a$, the set is $\{ b : b <_{\mathcal O} a \} \cup \{ a \}$, of type $|a| + 1$, with ordinals $|a| \cup \{ |a| \} = |a| + 1$. For $3 \cdot 5^e$, the set is the increasing union of the sets below $\Phi_e(n)$, each an initial segment of the next one by the induction hypothesis and the fact that $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$; its type and its set of ordinals are the supremum $\sup_n |\Phi_e(n)|$.
2. Let $R$ be the least relation containing $(a, 2^a)$ and $(b, 2^a)$ whenever $(b, a) \in R$, and containing $(b, 3 \cdot 5^e)$ whenever $\Phi_e(n)\converge$ and $(b, \Phi_e(n)) \in R$ or $b = \Phi_e(n)$, for some $n$. It is generated by c.e. rules, so it is c.e. By induction on $a \in \mathcal O$, $R(\cdot, a)$ is $\{ b : b <_{\mathcal O} a \}$.
:::

The relation $<_{\mathcal O}$ is therefore c.e. on each initial segment, uniformly in a notation of its upper bound. The set $\mathcal O$ itself is not c.e.; the next lesson shows that it is $\Pi^1_1$-complete.

## From notations to well-orderings and back

:::proposition{#prop-constructive-computable}
Every constructive ordinal is computable. Moreover, from $a \in \mathcal O$ one computes an index of a c.e. well-ordering of type $|a|$.
:::

:::proof{of=prop-constructive-computable}
By :ref{#prop-kleene-o-basic}, the restriction of $<_{\mathcal O}$ to $\{ b : b <_{\mathcal O} a \}$ is a c.e. well-ordering of type $|a|$, uniformly in $a$. By :ref{#prop-computable-ordinals-basic} (3), its type is computable.
:::

The converse requires arithmetic on notations, defined by the recursion theorem.

:::lemma{#lem-notation-sum}
There is a total computable function $+_{\mathcal O}$ such that for all $a, b \in \mathcal O$, $a +_{\mathcal O} b \in \mathcal O$, $|a +_{\mathcal O} b| = |a| + |b|$, $a \leq_{\mathcal O} a +_{\mathcal O} b$, and $a <_{\mathcal O} a +_{\mathcal O} b$ when $b \neq 1$.
:::

:::proof{of=lem-notation-sum}
By the recursion theorem (:ref{#thm-fixed-point}) with parameters, there is a total computable function satisfying
$$
a +_{\mathcal O} 1 = a, \qquad a +_{\mathcal O} 2^c = 2^{a +_{\mathcal O} c}, \qquad a +_{\mathcal O} 3 \cdot 5^e = 3 \cdot 5^{h(a, e)},
$$
where $h(a, e)$ is an index of the function $n \mapsto a +_{\mathcal O} \Phi_e(n)$, and $a +_{\mathcal O} b = 1$ for other $b$. Totality: the function only evaluates itself through indices, without computing $\Phi_e$. The properties are proved by induction on $b \in \mathcal O$: for $b = 3 \cdot 5^e$, the sequence $a +_{\mathcal O} \Phi_e(n)$ is $<_{\mathcal O}$-increasing by the induction hypothesis applied below each $\Phi_e(n+1)$, its terms are in $\mathcal O$, and its supremum is $\sup_n (|a| + |\Phi_e(n)|) = |a| + |b|$.
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
By the recursion theorem, there is a total computable function $g$ such that $g(x) = u(i_x)$, where $i_x$ is an index of the c.e. set $\{ 2^{g(y)} : y <_R x \}$, computed from $x$ and an index of $g$. We show by induction along the well-ordering $R$ that $g(x) \in \mathcal O$ and $|g(x)| \geq |R_{<x}|$, the type of the initial segment below $x$. If this holds for all $y <_R x$, then $W_{i_x} \subseteq \mathcal O$, and by :ref{#lem-notation-sup}, $g(x) \in \mathcal O$ and $|g(x)| \geq |g(y)| + 1 \geq |R_{<y}| + 1$ for all $y <_R x$; the supremum of the right-hand side is $|R_{<x}|$. Finally $a = u(i)$, with $i$ an index of $\{ 2^{g(x)} : x \text{ in the field of } R \}$, satisfies $|a| \geq |R|$. Since the constructive ordinals are closed downward, $|R|$ is constructive.
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

All definitions relativize to an oracle $X$: an ordinal is **$X$-computable** if it is the type of an $X$-computable well-ordering, $\mathcal O^X$ is defined with $\Phi^X_e$ in place of $\Phi_e$, and the results of this lesson hold relative to $X$. The least non-$X$-computable ordinal is written $\omega_1^X$. It is countable for every $X$, and every countable ordinal is $X$-computable for some $X$, namely for a set coding a well-ordering of that type; so $\omega_1$ is the supremum of the ordinals $\omega_1^X$. One has $\omega_1^X = \omega_1^{\mathrm{CK}}$ for many non-computable $X$, for instance every arithmetic $X$, and $\omega_1^X > \omega_1^{\mathrm{CK}}$ for $X = \mathcal O$.

## Exercises

::::exercise{difficulty=1}
Show that $\varepsilon_0 = \sup \{ \omega, \omega^\omega, \omega^{\omega^\omega}, \dots \}$ is computable.

:::solution
By :ref{#lem-notation-sum} and the recursion theorem, one defines a computable function on notations $a \mapsto \omega^a$, with $\omega^1 = 2^1$ (a notation for $1$), $\omega^{2^c} = 3 \cdot 5^{k(c)}$ where $\Phi_{k(c)}(n)$ is the sum of $n + 1$ copies of $\omega^c$, and $\omega^{3 \cdot 5^e} = 3 \cdot 5^{k'(e)}$ with $\Phi_{k'(e)}(n) = \omega^{\Phi_e(n)}$. Iterating from a notation of $\omega$ gives a computable $<_{\mathcal O}$-increasing sequence of notations for $\omega, \omega^\omega, \dots$, and $3 \cdot 5^e$ for an index $e$ of this sequence is a notation for $\varepsilon_0$. By :ref{#prop-constructive-computable}, $\varepsilon_0$ is computable.
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
