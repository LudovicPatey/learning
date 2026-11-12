---
title: Computably enumerable sets
summary: Equivalent characterizations of the computably enumerable sets, the dovetailing technique, and the comparison with computable sets.
duration: 40
prerequisites: [halting-problem]
---

The halting set is not computable, but membership in it can be confirmed: if $\Phi_e(e)\converge$, simulating the computation eventually establishes it. Sets with this property are the **computably enumerable** sets. They are the sets that an algorithm can list, the domains of partial computable functions, and the projections of computable relations. Examples outside computability theory include the set of theorems of a computably axiomatized theory, and the set of solvable Diophantine equations. This lesson proves the equivalence of these descriptions and compares c.e. sets with computable sets. The proofs rely on one technique, **dovetailing**: infinitely many searches, any of which may fail to terminate, are interleaved so that each of them receives infinitely many steps. The next lesson studies the closure properties of the class and shows that the halting set is its hardest member.

## Definition and characterizations

:::definition{#def-ce}
The **$e$-th computably enumerable set** is $W_e = \mathrm{dom}(\Phi_e) = \{ x : \Phi_e(x)\converge \}$. A set $A \subseteq \nat$ is **computably enumerable**, or **c.e.**, if $A = W_e$ for some $e$. Its approximation at stage $s$ is $W_e[s] = \{ x : \Phi_e(x)[s]\converge \}$.
:::

Older texts say *recursively enumerable*, or *r.e.* By the conventions on stages (:ref{#def-stage}), $W_e[s]$ is a finite subset of $\{0, \dots, s - 1\}$, computable from $e$ and $s$, and $W_e[0] \subseteq W_e[1] \subseteq \cdots$ with $\bigcup_s W_e[s] = W_e$.

:::example{#ex-ce-sets}
1. The halting set is c.e.: $\emptyset' = \{ e : e \in W_e \}$ is the domain of the partial computable function $e \mapsto \Phi_e(e)$. So are the general halting set $H$ and the set $\{ e : W_e \neq \emptyset \}$, by the next lesson.
2. Every computable set $A$ is c.e.: it is the domain of the program that computes $\chi_A(x)$, halts if the value is $1$ and loops otherwise. In particular every finite set is c.e.
3. The set of perfect squares is $W_e$ for the program of the quiz on closure properties of the first lesson, which searches for a square root.
4. If $P(x, y_1, \dots, y_k)$ is a polynomial with integer coefficients, the set $\{ x \in \nat : P(x, \vec y) = 0 \text{ for some } \vec y \in \nat^k \}$ is c.e.: a program can try all tuples $\vec y$ in turn, and halt when it finds a zero. By the theorem of Matiyasevich mentioned in the previous lesson, every c.e. set is of this form.
:::

:::definition{#def-ce-approx}
A **c.e. approximation** of a set $A$ is a uniformly computable sequence of sets $A_0 \subseteq A_1 \subseteq A_2 \subseteq \cdots$ with $\bigcup_s A_s = A$.
:::

The approximation must be increasing: an element, once enumerated, stays. Without this condition the definition describes a larger class. For instance, the sets $A_s = \{ e : \Phi_e(e)[s]\diverge \}$ form a uniformly computable, decreasing sequence with $\bigcap_s A_s = \nat \setminus \emptyset'$, and $\nat \setminus \emptyset'$ is not c.e. (:ref{#thm-halting-ce} below). The sets that are pointwise limits of uniformly computable sequences, with finitely many changes at each point, are the $\Delta^0_2$ sets of Shoenfield's limit lemma (:ref{#thm-limit-lemma}).

A relation $R \subseteq \nat^k$ is c.e. if the set $\{ \langle x_1, \dots, x_k \rangle : \vec x \in R \}$ is.

:::theorem{#thm-ce-characterizations}
For every $A \subseteq \nat$, the following are equivalent.

1. $A$ is computably enumerable.
2. $A = \{ x : \exists y\ R(x, y) \}$ for some computable relation $R \subseteq \nat^2$.
3. $A = \emptyset$, or $A$ is the range of a total computable function.
4. $A$ is the range of a partial computable function.
5. $A$ has a c.e. approximation.

Moreover, in item 2 the relation $R$ can be taken primitive recursive.
:::

:::proof{of=thm-ce-characterizations}
(1 ⇒ 2) If $A = W_e$, then $x \in A \iff \exists s\ \Phi_e(x)[s]\converge$, and the relation $\Phi_e(x)[s]\converge$ of $x$ and $s$ is primitive recursive (:ref{#prop-stage-properties}).

(2 ⇒ 3) Suppose $A \neq \emptyset$ and fix $a \in A$. Let $f(n) = \pi_0(n)$ if $R(\pi_0(n), \pi_1(n))$, and $f(n) = a$ otherwise. This $f$ is total computable, its values lie in $A$, and every $x \in A$ is a value: if $R(x, y)$, then $x = f(\langle x, y \rangle)$.

(3 ⇒ 4) A total function is partial, and $\emptyset$ is the range of the nowhere defined function.

(4 ⇒ 1) Let $A$ be the range of $\Phi_i$. The partial function $g(x) \simeq \mu n\ [\Phi_i(\pi_0(n))[\pi_1(n)]\converge = x]$ is partial computable, by :ref{#prop-computable-closure} and :ref{#prop-stage-properties}. It is defined if and only if $\Phi_i(y)\converge = x$ for some $y$, that is, if and only if $x \in A$. So $A = \mathrm{dom}(g)$ is c.e.

(1 ⇒ 5) If $A = W_e$, the sequence $(W_e[s])_s$ is a c.e. approximation.

(5 ⇒ 2) If $(A_s)$ is a c.e. approximation, then $x \in A \iff \exists s\ x \in A_s$, and the relation $x \in A_s$ is computable.
:::

Item 2 says that the c.e. sets are the sets definable by an **existential** quantifier over a computable relation: they are the $\Sigma^0_1$ sets of the arithmetic hierarchy. Item 3 justifies the name: a non-empty c.e. set is listed, possibly with repetitions, by an algorithm $f(0), f(1), f(2), \dots$. The proof of (2 ⇒ 3) runs through all pairs $(x, y)$ in the order of the pairing function, which interleaves the searches for witnesses of all $x$ at once. This technique is called **dovetailing**: running the searches one after the other would fail, since the search for a witness of some $x \notin A$ never ends.

:::figure[Dovetailing in the proof of (2 ⇒ 3), for a relation $R$ whose pairs $(x, y)$ with $x, y \leq 4$ are shown. Each cell carries the number $\langle x, y \rangle$, and is shaded when $R(x, y)$. The function $f$ examines the cells in the order of these numbers: $f(\langle x, y \rangle) = x$ on a shaded cell, and $f(n) = a$, a fixed element of $A$, elsewhere. In this example column $1$ contains no witness at all; a search through it alone would never end, but $f$ only spends one argument on each of its cells.]
<svg class="fig" viewBox="0 0 470 290" width="470" role="img" aria-label="A grid of pairs (x, y) numbered in the order of the pairing function; the cells where y is a witness for x are shaded; column 1 has no shaded cell"><text x="170.0" y="14" text-anchor="middle" class="label">element x</text><text x="90.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">0</text><text x="130.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">1</text><text x="170.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">2</text><text x="210.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">3</text><text x="250.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">4</text><text x="18" y="130.0" text-anchor="middle" class="label" transform="rotate(-90 18 130.0)">witness y</text><text x="60" y="55" text-anchor="end" class="mrm muted" font-size="12">0</text><rect x="70" y="30" width="40" height="40" class="cell"/><text x="90.0" y="55" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="110" y="30" width="40" height="40" class="cell"/><text x="130.0" y="55" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="150" y="30" width="40" height="40" class="cell"/><text x="170.0" y="55" text-anchor="middle" class="mrm muted" font-size="14">3</text><rect x="190" y="30" width="40" height="40" class="cell head-cell"/><text x="210.0" y="55" text-anchor="middle" class="mrm" font-size="14">6</text><rect x="230" y="30" width="40" height="40" class="cell"/><text x="250.0" y="55" text-anchor="middle" class="mrm muted" font-size="14">10</text><text x="60" y="95" text-anchor="end" class="mrm muted" font-size="12">1</text><rect x="70" y="70" width="40" height="40" class="cell"/><text x="90.0" y="95" text-anchor="middle" class="mrm muted" font-size="14">2</text><rect x="110" y="70" width="40" height="40" class="cell"/><text x="130.0" y="95" text-anchor="middle" class="mrm muted" font-size="14">4</text><rect x="150" y="70" width="40" height="40" class="cell head-cell"/><text x="170.0" y="95" text-anchor="middle" class="mrm" font-size="14">7</text><rect x="190" y="70" width="40" height="40" class="cell"/><text x="210.0" y="95" text-anchor="middle" class="mrm muted" font-size="14">11</text><rect x="230" y="70" width="40" height="40" class="cell"/><text x="250.0" y="95" text-anchor="middle" class="mrm muted" font-size="14">16</text><text x="60" y="135" text-anchor="end" class="mrm muted" font-size="12">2</text><rect x="70" y="110" width="40" height="40" class="cell head-cell"/><text x="90.0" y="135" text-anchor="middle" class="mrm" font-size="14">5</text><rect x="110" y="110" width="40" height="40" class="cell"/><text x="130.0" y="135" text-anchor="middle" class="mrm muted" font-size="14">8</text><rect x="150" y="110" width="40" height="40" class="cell"/><text x="170.0" y="135" text-anchor="middle" class="mrm muted" font-size="14">12</text><rect x="190" y="110" width="40" height="40" class="cell"/><text x="210.0" y="135" text-anchor="middle" class="mrm muted" font-size="14">17</text><rect x="230" y="110" width="40" height="40" class="cell"/><text x="250.0" y="135" text-anchor="middle" class="mrm muted" font-size="14">23</text><text x="60" y="175" text-anchor="end" class="mrm muted" font-size="12">3</text><rect x="70" y="150" width="40" height="40" class="cell"/><text x="90.0" y="175" text-anchor="middle" class="mrm muted" font-size="14">9</text><rect x="110" y="150" width="40" height="40" class="cell"/><text x="130.0" y="175" text-anchor="middle" class="mrm muted" font-size="14">13</text><rect x="150" y="150" width="40" height="40" class="cell head-cell"/><text x="170.0" y="175" text-anchor="middle" class="mrm" font-size="14">18</text><rect x="190" y="150" width="40" height="40" class="cell"/><text x="210.0" y="175" text-anchor="middle" class="mrm muted" font-size="14">24</text><rect x="230" y="150" width="40" height="40" class="cell head-cell"/><text x="250.0" y="175" text-anchor="middle" class="mrm" font-size="14">31</text><text x="60" y="215" text-anchor="end" class="mrm muted" font-size="12">4</text><rect x="70" y="190" width="40" height="40" class="cell"/><text x="90.0" y="215" text-anchor="middle" class="mrm muted" font-size="14">14</text><rect x="110" y="190" width="40" height="40" class="cell"/><text x="130.0" y="215" text-anchor="middle" class="mrm muted" font-size="14">19</text><rect x="150" y="190" width="40" height="40" class="cell"/><text x="170.0" y="215" text-anchor="middle" class="mrm muted" font-size="14">25</text><rect x="190" y="190" width="40" height="40" class="cell"/><text x="210.0" y="215" text-anchor="middle" class="mrm muted" font-size="14">32</text><rect x="230" y="190" width="40" height="40" class="cell"/><text x="250.0" y="215" text-anchor="middle" class="mrm muted" font-size="14">40</text><text x="90.0" y="248" text-anchor="middle" class="mrm muted" font-size="14">⋮</text><text x="130.0" y="248" text-anchor="middle" class="mrm muted" font-size="14">⋮</text><text x="170.0" y="248" text-anchor="middle" class="mrm muted" font-size="14">⋮</text><text x="210.0" y="248" text-anchor="middle" class="mrm muted" font-size="14">⋮</text><text x="250.0" y="248" text-anchor="middle" class="mrm muted" font-size="14">⋮</text><text x="290" y="50" class="label">f(0), f(1), …, f(14):</text><text x="290" y="72" class="mrm" font-size="14">a, a, a, a, a, 0, 3, 2,</text><text x="290" y="92" class="mrm" font-size="14">a, a, a, a, a, a, a, …</text><text x="290" y="130" class="label">column 1 has no witness:</text><text x="290" y="146" class="label">1 ∉ A, and a search through</text><text x="290" y="162" class="label">this column alone would</text><text x="290" y="178" class="label">never end</text></svg>
:::

:::quiz[the characterizations]
In (2 ⇒ 3), why does $f$ test single pairs $n = \langle x, y \rangle$, instead of searching for a witness $y$ of each $x$ in turn?

- [x] A search for a witness of some $x \notin A$ never terminates, and would block the enumeration of all later elements; testing one pair at a time keeps $f$ total.
- [ ] To make $f$ injective.

  $f$ is not injective: it takes the value $a$ infinitely often.
- [ ] Because $R$ is only defined on pairs.

  $R$ is a relation on pairs either way; the issue is termination.

---

In (4 ⇒ 1), what does the search $\mu n\ [\Phi_i(\pi_0(n))[\pi_1(n)]\converge = x]$ range over?

- [x] Pairs $(y, s)$ of an argument and a stage, until a computation $\Phi_i(y)$ is found to converge to $x$ at stage $s$.

  Searching over arguments $y$ only, by computing $\Phi_i(0), \Phi_i(1), \dots$, could get stuck on a divergent computation.
- [ ] Indices of programs computing $x$.

  The search ranges over arguments and stages of the fixed function $\Phi_i$; indices of other programs play no role.
- [ ] Stages at which $x$ enters $W_i$.

  This would describe the domain of $\Phi_i$, not its range.
:::

:::proposition{#prop-ce-range}
An infinite set $A$ is computably enumerable if and only if it is the range of an injective total computable function.
:::

:::proof{of=prop-ce-range}
The range of a total computable function is c.e. by :ref{#thm-ce-characterizations}. Conversely, let $f$ be total computable with range $A$. Define $g(0) = f(0)$, and $g(n+1) = f(m_{n+1})$, where $m_{n+1}$ is the least $m$ with $f(m) \notin \{ g(0), \dots, g(n) \}$. The search terminates since $A$ is infinite, so $g$ is total computable, and it is injective by construction. Let $m_0 = 0$. By induction on $n$, $\{ f(0), \dots, f(m_n) \} = \{ g(0), \dots, g(n) \}$: the values $f(m)$ for $m_n < m < m_{n+1}$ are already listed, by minimality of $m_{n+1}$. Hence $m_0 < m_1 < \cdots$, and every value of $f$ is a value of $g$.
:::

## Computable and c.e. sets

:::proposition{#prop-computable-iff-ce-coce}
A set $A$ is computable if and only if both $A$ and $\nat \setminus A$ are computably enumerable.
:::

:::proof{of=prop-computable-iff-ce-coce}
If $A$ is computable, $A = \{ x : \exists y\ \chi_A(x) = 1 \}$ is the projection of a computable relation (with a dummy variable), hence c.e.; and $\nat \setminus A$ is computable as well.

Conversely, let $A = W_a$ and $\nat \setminus A = W_b$. On input $x$, search for the least $s$ such that $x \in W_a[s]$ or $x \in W_b[s]$, and output $1$ in the first case, $0$ in the second. The search terminates, since $x$ belongs to one of the two sets and hence appears in its approximation at some stage; the two cases do not overlap, since the sets are disjoint. So this algorithm computes $\chi_A$.
:::

:::theorem{#thm-halting-ce}
The halting set $\emptyset'$ is computably enumerable, and its complement $\nat \setminus \emptyset'$ is not.
:::

:::proof{of=thm-halting-ce}
$\emptyset' = \{ e : \exists s\ \Phi_e(e)[s]\converge \}$ is c.e. If its complement were c.e., then $\emptyset'$ would be computable by :ref{#prop-computable-iff-ce-coce}, contradicting :ref{#thm-halting}.
:::

So the computable sets form a proper subclass of the c.e. sets, and the c.e. sets are not closed under complement. A set whose complement is c.e. is called **co-c.e.**

:::quiz[computable and c.e. sets]
In the proof of :ref{#prop-computable-iff-ce-coce}, why are the two approximations examined stage by stage, rather than by running $\Phi_a(x)$ to completion first?

- [x] If $x \notin A$, the computation of $\Phi_a(x)$ never halts, and the algorithm would never consider $W_b$.

  Examining both at each stage is a form of dovetailing.
- [ ] Because $\Phi_a$ is total.

  $\Phi_a$ diverges exactly outside $A$.
- [ ] To output the answer faster.

  Speed is irrelevant; termination is the point.

---

Which statements are correct?

- [x] Every computable set is c.e., but not conversely.
- [x] If $A$ is c.e. and not computable, then $\nat \setminus A$ is not c.e.
- [ ] The complement of a c.e. set is never c.e.

  It is c.e. exactly when the set is computable.
- [ ] Every subset of a c.e. set is c.e.

  $\nat$ is c.e., and $\nat \setminus \emptyset'$ is a subset of it which is not c.e.
:::

## Exercises

::::exercise{difficulty=1}
An infinite set $A$ is **enumerable in increasing order** if $A = f(\nat)$ for some total computable $f$ with $f(n) < f(n+1)$ for all $n$. Show that an infinite set is computable if and only if it is enumerable in increasing order.

:::solution
If $A$ is infinite and computable, its principal function $p_A$ (:ref{#lem-subsets-of-n}) is computable, by $p_A(0) = \mu x\, (x \in A)$ and $p_A(n+1) = \mu x\, (x > p_A(n) \wedge x \in A)$, and it enumerates $A$ in increasing order. Conversely, to decide whether $x \in A$, compute $f(0), f(1), \dots$ until a value greater than $x$ appears, which happens since $f(n) \geq n$; then $x \in A$ if and only if $x$ is among the values computed, since later values are larger.
:::
::::

::::exercise{difficulty=1}
Show that every infinite c.e. set contains an infinite computable subset.

:::solution
Let $f$ be a total computable function with range $A$. Let $g(0) = f(0)$, and $g(n+1) = f(m)$ for the least $m$ with $f(m) > g(n)$, which exists since $A$ is infinite. Then $g$ is total computable and strictly increasing, and its range is an infinite subset of $A$, computable by the previous exercise.
:::
::::

## Notes and references

Computably enumerable sets were introduced in the 1930s, in the work of Church, Kleene and Post on recursive functions; Post's paper of 1944 made them a subject of study in their own right. The characterization of computable sets as the c.e. sets with a c.e. complement is due to Post (1944). In Soare's textbook, the material of this lesson is in Sections 1.6.1 and 2.1: the normal form theorem (Theorem 2.1.3), the listing theorem (Theorem 2.1.10) and the complementation theorem (Theorem 2.1.14). Soare's earlier book is the standard reference for the theory of c.e. sets.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 1.6 and 2.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Foundations of computability*, section *Computably enumerable sets*.
