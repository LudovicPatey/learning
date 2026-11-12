---
title: Well-orderings and ordinals
summary: Well-orderings, the comparison theorem, ordinals as canonical order types, transfinite induction and recursion, ordinal arithmetic, and the countable ordinals.
duration: 45
prerequisites: [arithmetic-hierarchy/sigma-pi-sets]
---

Higher computability iterates the operations of classical computability theory, such as the Turing jump, along transfinite sequences. The jump can be iterated $n$ times for each $n$, then once more to collect all the finite iterates in a single set $\emptyset^{(\omega)}$, then again from there, and so on. The positions in such a sequence are ordinals, and the iterations are defined by transfinite recursion. This lesson recalls the facts about ordinals that the track uses. We work in ordinary set theory with the axiom of choice. The proofs are standard; those that belong to set theory rather than to computability are given in outline, with full details in any textbook of set theory, for instance Kunen's or Jech's.

## Well-orderings

The natural numbers support proofs by induction and definitions by recursion because every non-empty set of numbers has a least element. Well-orderings are the linear orders with this property; they are the orders along which induction and recursion make sense.

:::definition{#def-well-ordering}
A **well-ordering** is a linear order $(A, <)$ in which every non-empty subset has a least element. Equivalently, under the axiom of dependent choice, there is no infinite descending sequence $a_0 > a_1 > \cdots$.
:::

:::example{#ex-well-orderings}
1. Every finite linear order, and $(\nat, <)$, are well-orderings.
2. Order $\nat$ by putting $0$ after all the other numbers: $1 < 2 < 3 < \cdots < 0$. Every non-empty subset still has a least element (the least positive number in it, or $0$ if it is $\{ 0 \}$), so this is a well-ordering, with a largest element.
3. Order $\nat$ by putting the even numbers first, then the odd numbers: $0 < 2 < 4 < \cdots < 1 < 3 < 5 < \cdots$. This is a well-ordering: two copies of $\nat$, one after the other.
4. $(\mathbb Z, <)$, $(\nat, >)$ and $(\mathbb Q \cap [0, 1], <)$ are linear orders that are not well-orderings: $\mathbb Z$ and $(\nat, >)$ have no least element, and in $\mathbb Q \cap [0, 1]$ the subset of positive elements has none.
:::

The second equivalent form is the one used in practice: to show that an order is a well-ordering, one shows that it admits no infinite descending sequence. The equivalence is the second exercise. For $a \in A$, the **initial segment** $A_{<a} = \{ b \in A : b < a \}$ is again well-ordered. An **isomorphism** of linear orders is an order-preserving bijection.

:::lemma{#lem-wo-rigid}
Let $(A, <)$ be a well-ordering.

1. If $f : A \to A$ is strictly increasing, then $f(a) \geq a$ for every $a$.
2. $A$ is not isomorphic to any of its proper initial segments, and the only automorphism of $A$ is the identity.
:::

:::proof{of=lem-wo-rigid}
1. If $f(a) < a$ for some $a$, let $a$ be the least such element. Then $f(f(a)) < f(a)$ since $f$ is increasing, so $f(a)$ is a smaller element with the same property, a contradiction.
2. An isomorphism $f : A \to A_{<a}$ would satisfy $f(a) < a$, contradicting (1). If $f$ is an automorphism, (1) applies to $f$ and $f^{-1}$, so $f(a) \geq a$ and $f^{-1}(a) \geq a$, hence $f(a) = a$.
:::

The well-ordering hypothesis is needed: on $\mathbb Z$, the map $n \mapsto n - 1$ is a strictly increasing automorphism with $f(n) < n$ for every $n$, and $(\mathbb Q, <)$ is isomorphic to its proper initial segment $\{ q : q < 0 \}$.

Two well-orderings can always be compared. The idea of the proof is to match the least element of $A$ with the least element of $B$, the next one with the next one, and so on through the transfinite; the matching stops when one of the two orders is exhausted. The formal proof defines the matching at once, by the rigidity lemma.

:::theorem[Comparison]{#thm-wo-comparison}
For any two well-orderings $A$ and $B$, exactly one of the following holds: $A$ is isomorphic to $B$; $A$ is isomorphic to a proper initial segment of $B$; $B$ is isomorphic to a proper initial segment of $A$. The isomorphism is unique.
:::

:::proof{of=thm-wo-comparison}
Let $f$ be the set of pairs $(a, b)$ such that $A_{<a}$ and $B_{<b}$ are isomorphic. By :ref{#lem-wo-rigid}, $f$ is the graph of an injective partial function, order-preserving, whose domain is an initial segment of $A$ and whose range is an initial segment of $B$. If both were proper, with least elements $a$ outside the domain and $b$ outside the range, then $f$ would be an isomorphism between $A_{<a}$ and $B_{<b}$, so $(a, b) \in f$, a contradiction. Uniqueness and exclusivity follow from :ref{#lem-wo-rigid}.
:::

## Ordinals

**Ordinals** are canonical representatives of the isomorphism types of well-orderings. In von Neumann's definition, an ordinal is a set that is transitive and well-ordered by $\in$; each ordinal $\alpha$ is the set of smaller ordinals, $\alpha = \{ \beta : \beta < \alpha \}$. Thus $0 = \emptyset$, $1 = \{ 0 \}$, $2 = \{ 0, 1 \}$, and $\omega = \{ 0, 1, 2, \dots \}$. We admit the following facts:

- every well-ordering $A$ is isomorphic to a unique ordinal, its **order type** $|A|$;
- the ordinals are well-ordered by $<$ (any set of ordinals has a least element, and a supremum, its union);
- the **successor** of $\alpha$ is $\alpha + 1 = \alpha \cup \{ \alpha \}$, and a non-zero ordinal that is not a successor is a **limit**; $\omega = \nat$ is the least limit ordinal.

By the comparison theorem, $|A| \leq |B|$ if and only if $A$ is isomorphic to an initial segment of $B$, or equivalently if there is an order-preserving injection from $A$ into $B$. (Given an injection $f$, the image $f(A)$ is a well-ordering isomorphic to $A$, and its type is at most $|B|$: otherwise $B$ would be isomorphic to a proper initial segment of $f(A)$, below some $f(a)$, and the composite of this isomorphism with the inclusion would be a strictly increasing map $g : B \to B$ with $g(f(a)) < f(a)$, contradicting :ref{#lem-wo-rigid} (1).)

:::proposition[Transfinite induction and recursion]{#prop-transfinite}
1. If a property holds of $\alpha$ whenever it holds of all $\beta < \alpha$, then it holds of every ordinal.
2. For every operation $G$ on sets, there is a unique operation $F$ on ordinals with $F(\alpha) = G(F \uh \alpha)$ for every $\alpha$, where $F \uh \alpha$ is the restriction of $F$ to the ordinals smaller than $\alpha$.
:::

:::proof{of=prop-transfinite}
1. If the property failed, a least counterexample $\alpha$ would exist, and the property would hold of all $\beta < \alpha$, hence of $\alpha$.
2. Uniqueness by (1): two such operations agree on $\alpha$ if they agree below $\alpha$. For existence, the functions $f$ defined on some ordinal $\gamma$ and satisfying $f(\alpha) = G(f \uh \alpha)$ for $\alpha < \gamma$ are pairwise compatible, by uniqueness, and every $\gamma$ is the domain of one of them, by induction; $F$ is their union. The replacement axiom guarantees that these functions are sets.
:::

Transfinite induction and recursion are the techniques of the whole track. Their effective versions, in which the recursion is carried out by a program that calls itself through the recursion theorem, appear in the lesson on Kleene's $\mathcal O$ and are used throughout the course on hyperarithmetic sets.

Recursion usually distinguishes three cases: a value at $0$, a rule for successors, and a rule for limits, typically a supremum. For example, **ordinal addition** is defined by $\alpha + 0 = \alpha$, $\alpha + (\beta + 1) = (\alpha + \beta) + 1$ and $\alpha + \lambda = \sup_{\beta < \lambda} (\alpha + \beta)$ for limit $\lambda$; multiplication and exponentiation follow the same pattern, with $\alpha \cdot 0 = 0$, $\alpha \cdot (\beta + 1) = \alpha \cdot \beta + \alpha$, $\alpha^0 = 1$ and $\alpha^{\beta + 1} = \alpha^\beta \cdot \alpha$, and suprema at limits. The sum $\alpha + \beta$ is the order type of a copy of $\alpha$ followed by a copy of $\beta$, and $\alpha \cdot \beta$ the type of $\beta$ copies of $\alpha$, placed one after the other: the pairs $(x, y)$ with $x \in \alpha$ and $y \in \beta$, compared first by $y$, then by $x$.

:::example{#ex-ordinal-arithmetic}
The orders of :ref{#ex-well-orderings} (2) and (3) have types $\omega + 1$ and $\omega \cdot 2 = \omega + \omega$. The type of $\nat \times \nat$, with pairs compared first by their second component, is $\omega \cdot \omega = \omega^2$: it consists of $\omega$ copies of $\omega$. These operations are not commutative: $1 + \omega = \omega < \omega + 1$, since a single element followed by a copy of $\nat$ is again a copy of $\nat$; and $2 \cdot \omega = \omega < \omega \cdot 2$, since $\omega$ copies of a two-element order form a copy of $\nat$.
:::

:::figure[Four well-orderings, read from left to right. Each increasing sequence of dots accumulates at a limit point, which is not an element of the order. The element after a limit point, as in $\omega + 1$ or at the start of the second copy in $\omega \cdot 2$, has infinitely many predecessors but no immediate predecessor.]
<svg class="fig" viewBox="0 0 620 224" width="620" role="img" aria-label="Four well-orderings drawn as dots from left to right: omega, omega plus one, omega times two, omega squared"><text x="96" y="35" text-anchor="end" font-size="17"><tspan class="math">ω</tspan></text><line x1="114" y1="30" x2="590" y2="30" class="axis"/><circle cx="120.0" cy="30" r="3.2" class="ink-fill"/><circle cx="216.0" cy="30" r="3.2" class="ink-fill"/><circle cx="281.3" cy="30" r="3.2" class="ink-fill"/><circle cx="325.7" cy="30" r="3.2" class="ink-fill"/><circle cx="355.9" cy="30" r="3.2" class="ink-fill"/><circle cx="376.4" cy="30" r="3.2" class="ink-fill"/><circle cx="390.3" cy="30" r="3.2" class="ink-fill"/><circle cx="399.8" cy="30" r="3.2" class="ink-fill"/><circle cx="406.3" cy="30" r="3.2" class="ink-fill"/><circle cx="410.7" cy="30" r="3.2" class="ink-fill"/><circle cx="413.7" cy="30" r="3.2" class="ink-fill"/><text x="96" y="81" text-anchor="end" font-size="17"><tspan class="math">ω</tspan><tspan class="mrm"> + 1</tspan></text><line x1="114" y1="76" x2="590" y2="76" class="axis"/><circle cx="120.0" cy="76" r="3.2" class="ink-fill"/><circle cx="216.0" cy="76" r="3.2" class="ink-fill"/><circle cx="281.3" cy="76" r="3.2" class="ink-fill"/><circle cx="325.7" cy="76" r="3.2" class="ink-fill"/><circle cx="355.9" cy="76" r="3.2" class="ink-fill"/><circle cx="376.4" cy="76" r="3.2" class="ink-fill"/><circle cx="390.3" cy="76" r="3.2" class="ink-fill"/><circle cx="399.8" cy="76" r="3.2" class="ink-fill"/><circle cx="406.3" cy="76" r="3.2" class="ink-fill"/><circle cx="410.7" cy="76" r="3.2" class="ink-fill"/><circle cx="413.7" cy="76" r="3.2" class="ink-fill"/><circle cx="450.0" cy="76" r="4.2" class="accent-fill"/><text x="464.0" y="80.0" text-anchor="start" class="label" font-size="12">largest element</text><text x="96" y="127" text-anchor="end" font-size="17"><tspan class="math">ω</tspan><tspan class="mrm"> · 2</tspan></text><line x1="114" y1="122" x2="590" y2="122" class="axis"/><circle cx="120.0" cy="122" r="3.2" class="ink-fill"/><circle cx="184.0" cy="122" r="3.2" class="ink-fill"/><circle cx="227.5" cy="122" r="3.2" class="ink-fill"/><circle cx="257.1" cy="122" r="3.2" class="ink-fill"/><circle cx="277.2" cy="122" r="3.2" class="ink-fill"/><circle cx="290.9" cy="122" r="3.2" class="ink-fill"/><circle cx="300.2" cy="122" r="3.2" class="ink-fill"/><circle cx="306.6" cy="122" r="3.2" class="ink-fill"/><circle cx="310.9" cy="122" r="3.2" class="ink-fill"/><circle cx="313.8" cy="122" r="3.2" class="ink-fill"/><circle cx="315.8" cy="122" r="3.2" class="ink-fill"/><circle cx="350.0" cy="122" r="3.2" class="ink-fill"/><circle cx="414.0" cy="122" r="3.2" class="ink-fill"/><circle cx="457.5" cy="122" r="3.2" class="ink-fill"/><circle cx="487.1" cy="122" r="3.2" class="ink-fill"/><circle cx="507.2" cy="122" r="3.2" class="ink-fill"/><circle cx="520.9" cy="122" r="3.2" class="ink-fill"/><circle cx="530.2" cy="122" r="3.2" class="ink-fill"/><circle cx="536.6" cy="122" r="3.2" class="ink-fill"/><circle cx="540.9" cy="122" r="3.2" class="ink-fill"/><circle cx="543.8" cy="122" r="3.2" class="ink-fill"/><circle cx="545.8" cy="122" r="3.2" class="ink-fill"/><text x="96" y="173" text-anchor="end" font-size="17"><tspan class="math">ω</tspan><tspan class="mrm" font-size="11" dy="-7">2</tspan></text><line x1="114" y1="168" x2="590" y2="168" class="axis"/><circle cx="120.0" cy="168" r="3.2" class="ink-fill"/><circle cx="150.7" cy="168" r="3.2" class="ink-fill"/><circle cx="171.6" cy="168" r="3.2" class="ink-fill"/><circle cx="185.8" cy="168" r="3.2" class="ink-fill"/><circle cx="195.5" cy="168" r="3.2" class="ink-fill"/><circle cx="202.0" cy="168" r="3.2" class="ink-fill"/><circle cx="206.5" cy="168" r="3.2" class="ink-fill"/><circle cx="209.5" cy="168" r="3.2" class="ink-fill"/><circle cx="211.6" cy="168" r="3.2" class="ink-fill"/><circle cx="213.0" cy="168" r="3.2" class="ink-fill"/><circle cx="214.0" cy="168" r="3.2" class="ink-fill"/><circle cx="232.0" cy="168" r="3.2" class="ink-fill"/><circle cx="262.7" cy="168" r="3.2" class="ink-fill"/><circle cx="283.6" cy="168" r="3.2" class="ink-fill"/><circle cx="297.8" cy="168" r="3.2" class="ink-fill"/><circle cx="307.5" cy="168" r="3.2" class="ink-fill"/><circle cx="314.0" cy="168" r="3.2" class="ink-fill"/><circle cx="318.5" cy="168" r="3.2" class="ink-fill"/><circle cx="321.5" cy="168" r="3.2" class="ink-fill"/><circle cx="323.6" cy="168" r="3.2" class="ink-fill"/><circle cx="325.0" cy="168" r="3.2" class="ink-fill"/><circle cx="326.0" cy="168" r="3.2" class="ink-fill"/><circle cx="344.0" cy="168" r="3.2" class="ink-fill"/><circle cx="374.7" cy="168" r="3.2" class="ink-fill"/><circle cx="395.6" cy="168" r="3.2" class="ink-fill"/><circle cx="409.8" cy="168" r="3.2" class="ink-fill"/><circle cx="419.5" cy="168" r="3.2" class="ink-fill"/><circle cx="426.0" cy="168" r="3.2" class="ink-fill"/><circle cx="430.5" cy="168" r="3.2" class="ink-fill"/><circle cx="433.5" cy="168" r="3.2" class="ink-fill"/><circle cx="435.6" cy="168" r="3.2" class="ink-fill"/><circle cx="437.0" cy="168" r="3.2" class="ink-fill"/><circle cx="438.0" cy="168" r="3.2" class="ink-fill"/><circle cx="456.0" cy="168" r="3.2" class="ink-fill"/><circle cx="486.7" cy="168" r="3.2" class="ink-fill"/><circle cx="507.6" cy="168" r="3.2" class="ink-fill"/><circle cx="521.8" cy="168" r="3.2" class="ink-fill"/><circle cx="531.5" cy="168" r="3.2" class="ink-fill"/><circle cx="538.0" cy="168" r="3.2" class="ink-fill"/><circle cx="542.5" cy="168" r="3.2" class="ink-fill"/><circle cx="545.5" cy="168" r="3.2" class="ink-fill"/><circle cx="547.6" cy="168" r="3.2" class="ink-fill"/><circle cx="549.0" cy="168" r="3.2" class="ink-fill"/><circle cx="550.0" cy="168" r="3.2" class="ink-fill"/><text x="572.0" y="173.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text></svg>
:::

:::quiz[ordinals]
In the proof of :ref{#lem-wo-rigid} (1), where is the well-ordering hypothesis used?

- [x] To take the least $a$ with $f(a) < a$; then $f(a)$ is a smaller element with the same property.
- [ ] To show that $f$ is injective.

  A strictly increasing function is injective in any linear order.
- [ ] To show that $f(a) \in A$.

  This is the hypothesis $f : A \to A$.

---

Why is $1 + \omega = \omega$?

- [x] Because a single element followed by a copy of $\nat$ is again an infinite increasing sequence without last element, isomorphic to $\nat$ by the shift $n \mapsto n + 1$.
- [ ] Because addition of ordinals is commutative.

  It is not: $\omega + 1 \neq \omega$, since $\omega + 1$ has a largest element.
- [ ] Because $1$ is finite.

  Finite ordinals are not absorbed on the right: $\omega + 1 > \omega$.
:::

## Countable ordinals

An ordinal is **countable** if it is a countable set; equivalently, it is the order type of a well-ordering of a subset of $\nat$, or of $\nat$ itself when it is infinite. Every countable ordinal is therefore coded by a set of numbers: a set $W \subseteq \nat \times \nat$ that is a well-ordering of its field. The orders of :ref{#ex-well-orderings} and :ref{#ex-ordinal-arithmetic} code $\omega + 1$, $\omega \cdot 2$ and $\omega^2$ in this way. The countable ordinals are closed under addition, multiplication, exponentiation and countable suprema.

:::proposition{#prop-omega1}
There is an uncountable ordinal. The least one, $\omega_1$, is the set of countable ordinals.
:::

:::proof{of=prop-omega1}
The countable ordinals form a set: each is the order type of a well-ordering of a subset of $\nat$, and these well-orderings form a set. This set is downward closed and well-ordered, so it is an ordinal $\omega_1$. If $\omega_1$ were countable, it would belong to itself, which is impossible for an ordinal: $\alpha < \alpha$ fails.
:::

This is the first appearance in the track of an argument that recurs: a set of ordinals that is downward closed is itself an ordinal, and therefore cannot belong to the set. The Church–Kleene ordinal $\omega_1^{\mathrm{CK}}$ of the next lesson is obtained in the same way from the computable well-orderings.

A countable union of countable sets being countable, every countable set of countable ordinals is bounded below $\omega_1$; this uses the axiom of choice. Since there are only countably many algorithms, only countably many countable ordinals can be the order types of computable well-orderings: the next lesson studies them.

## Exercises

::::exercise{difficulty=1}
Show that every ordinal $\alpha$ can be written uniquely as $\alpha = \lambda + n$ with $\lambda$ zero or a limit ordinal and $n \in \nat$.

:::solution
Let $\lambda$ be the largest ordinal $\leq \alpha$ that is zero or a limit; it exists since the supremum of limit ordinals below or equal to $\alpha$ is zero or a limit. If $\lambda + n \leq \alpha$ for every $n \in \nat$, then $\lambda + \omega = \sup_n (\lambda + n) \leq \alpha$ would be a limit larger than $\lambda$. So there is a least $n$ with $\lambda + (n + 1) > \alpha$; then $\lambda + n \leq \alpha < (\lambda + n) + 1$, and $\alpha = \lambda + n$, since no ordinal lies strictly between $\beta$ and $\beta + 1$. Uniqueness: if $\lambda + n = \lambda' + n'$ with $\lambda < \lambda'$, then $\lambda' \leq \lambda + n$ would be a limit of the form $\lambda + k$, $k \leq n$, which is a successor unless $k = 0$; so $\lambda = \lambda'$, and $n = n'$ by cancellation.
:::
::::

::::exercise{difficulty=2}
Show that a linear order $(A, <)$ is a well-ordering if and only if it has no infinite descending sequence, using the axiom of dependent choice for the converse.

:::solution
A descending sequence has no least element, so a well-ordering has none. Conversely, if a non-empty $S \subseteq A$ has no least element, then every $a \in S$ has some $b \in S$ with $b < a$; dependent choice gives a sequence $a_0 > a_1 > \cdots$ in $S$.
:::
::::

::::exercise{difficulty=1}
Show that the order on $\nat \times \nat$ in which pairs are compared first by their second component, then by their first one, is a well-ordering, and that the lexicographic order on $\nat \times \{ 0, 1 \}$ (compare the first component first) has type $\omega$.

:::solution
A descending sequence $(x_k, y_k)$ has non-increasing second components, which are therefore eventually constant; from then on the first components decrease strictly, which is impossible in $\nat$. For the second order, $(n, i) \mapsto 2n + i$ is an isomorphism onto $(\nat, <)$: it is the computation $2 \cdot \omega = \omega$ of :ref{#ex-ordinal-arithmetic}.
:::
::::

## Notes and references

Cantor introduced ordinals as order types of well-orderings (1883, 1897); von Neumann's definition dates from 1923. The comparison theorem is due to Cantor. Monin and Patey present von Neumann's and Cantor's approaches to ordinals side by side, with ordinal arithmetic and transfinite recursion, in their chapter on transfinite numbers.

- K. Kunen, *Set Theory*, College Publications, 2011.
- T. Jech, *Set Theory*, 3rd millennium edition, Springer, 2003.
- B. Monin and L. Patey, *Computability theory*, chapter *Transfinite numbers*, sections *Ordinals* and *Induction and transfinite recurrence*.
