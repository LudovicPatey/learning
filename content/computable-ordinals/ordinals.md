---
title: Well-orderings and ordinals
summary: Well-orderings, order isomorphisms and ordinals; the comparison theorem; transfinite induction and recursion; ordinal arithmetic; countable ordinals and ω₁.
duration: 35
prerequisites: [arithmetic-hierarchy/sigma-pi-sets]
---

Higher computability iterates the operations of classical computability theory, such as the Turing jump, along transfinite sequences. The indices of these sequences are ordinals. This lesson recalls the facts about ordinals that the track uses. We work in ordinary set theory with the axiom of choice; the proofs are standard and are given in outline, with full details in any textbook of set theory, for instance Kunen's or Jech's.

## Well-orderings

:::definition{#def-well-ordering}
A **well-ordering** is a linear order $(A, <)$ in which every non-empty subset has a least element. Equivalently, under the axiom of dependent choice, there is no infinite descending sequence $a_0 > a_1 > \cdots$.
:::

For $a \in A$, the **initial segment** $A_{<a} = \{ b \in A : b < a \}$ is again well-ordered. An **isomorphism** of linear orders is an order-preserving bijection.

:::lemma{#lem-wo-rigid}
Let $(A, <)$ be a well-ordering.

1. If $f : A \to A$ is strictly increasing, then $f(a) \geq a$ for every $a$.
2. $A$ is not isomorphic to any of its proper initial segments, and the only automorphism of $A$ is the identity.
:::

:::proof{of=lem-wo-rigid}
1. If $f(a) < a$ for some $a$, let $a$ be the least such element. Then $f(f(a)) < f(a)$ since $f$ is increasing, so $f(a)$ is a smaller element with the same property, a contradiction.
2. An isomorphism $f : A \to A_{<a}$ would satisfy $f(a) < a$, contradicting (1). If $f$ is an automorphism, (1) applies to $f$ and $f^{-1}$, so $f(a) \geq a$ and $f^{-1}(a) \geq a$, hence $f(a) = a$.
:::

:::theorem[Comparison]{#thm-wo-comparison}
For any two well-orderings $A$ and $B$, exactly one of the following holds: $A$ is isomorphic to $B$; $A$ is isomorphic to a proper initial segment of $B$; $B$ is isomorphic to a proper initial segment of $A$. The isomorphism is unique.
:::

:::proof{of=thm-wo-comparison}
Let $f$ be the set of pairs $(a, b)$ such that $A_{<a}$ and $B_{<b}$ are isomorphic. By :ref{#lem-wo-rigid}, $f$ is the graph of an injective partial function, order-preserving, whose domain is an initial segment of $A$ and whose range is an initial segment of $B$. If both were proper, with least elements $a$ outside the domain and $b$ outside the range, then $f$ would be an isomorphism between $A_{<a}$ and $B_{<b}$, so $(a, b) \in f$, a contradiction. Uniqueness and exclusivity follow from :ref{#lem-wo-rigid}.
:::

## Ordinals

**Ordinals** are canonical representatives of the isomorphism types of well-orderings. In von Neumann's definition, an ordinal is a set that is transitive and well-ordered by $\in$; each ordinal $\alpha$ is the set of smaller ordinals, $\alpha = \{ \beta : \beta < \alpha \}$. We admit the following facts:

- every well-ordering $A$ is isomorphic to a unique ordinal, its **order type** $|A|$;
- the ordinals are well-ordered by $<$ (any set of ordinals has a least element, and a supremum, its union);
- $0 = \emptyset$, the **successor** of $\alpha$ is $\alpha + 1 = \alpha \cup \{ \alpha \}$, and a non-zero ordinal that is not a successor is a **limit**; $\omega = \nat$ is the least limit ordinal.

By the comparison theorem, $|A| \leq |B|$ if and only if $A$ is isomorphic to an initial segment of $B$, or equivalently if there is an order-preserving injection from $A$ into $B$.

:::proposition[Transfinite induction and recursion]{#prop-transfinite}
1. If a property holds of $\alpha$ whenever it holds of all $\beta < \alpha$, then it holds of every ordinal.
2. For every operation $G$ on sets, there is a unique operation $F$ on ordinals with $F(\alpha) = G(F \uh \alpha)$ for every $\alpha$, where $F \uh \alpha$ is the restriction of $F$ to the ordinals smaller than $\alpha$.
:::

:::proof{of=prop-transfinite}
1. If the property failed, a least counterexample $\alpha$ would exist, and the property would hold of all $\beta < \alpha$, hence of $\alpha$.
2. Uniqueness by (1): two such operations agree on $\alpha$ if they agree below $\alpha$. For existence, the functions $f$ defined on some ordinal $\gamma$ and satisfying $f(\alpha) = G(f \uh \alpha)$ for $\alpha < \gamma$ are pairwise compatible, by uniqueness, and every $\gamma$ is the domain of one of them, by induction; $F$ is their union. The replacement axiom guarantees that these functions are sets.
:::

Recursion usually distinguishes three cases: a value at $0$, a rule for successors, and a rule for limits, typically a supremum. For example, **ordinal addition** is defined by $\alpha + 0 = \alpha$, $\alpha + (\beta + 1) = (\alpha + \beta) + 1$ and $\alpha + \lambda = \sup_{\beta < \lambda} (\alpha + \beta)$ for limit $\lambda$; multiplication and exponentiation follow the same pattern, with $\alpha \cdot (\beta + 1) = \alpha \cdot \beta + \alpha$ and $\alpha^{\beta + 1} = \alpha^\beta \cdot \alpha$. The sum $\alpha + \beta$ is the order type of a copy of $\alpha$ followed by a copy of $\beta$, and $\alpha \cdot \beta$ the type of $\beta$ copies of $\alpha$. These operations are not commutative: $1 + \omega = \omega < \omega + 1$, and $2 \cdot \omega = \omega < \omega \cdot 2$.

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

An ordinal is **countable** if it is a countable set; equivalently, it is the order type of a well-ordering of a subset of $\nat$, or of $\nat$ itself when it is infinite. Every countable ordinal is therefore coded by a set of numbers: a set $W \subseteq \nat \times \nat$ that is a well-ordering of its field. The countable ordinals are closed under addition, multiplication, exponentiation and countable suprema.

:::proposition{#prop-omega1}
There is an uncountable ordinal. The least one, $\omega_1$, is the set of countable ordinals.
:::

:::proof{of=prop-omega1}
The countable ordinals form a set: each is the order type of a well-ordering of a subset of $\nat$, and these well-orderings form a set. This set is downward closed and well-ordered, so it is an ordinal $\omega_1$. If $\omega_1$ were countable, it would belong to itself, which is impossible for an ordinal: $\alpha < \alpha$ fails.
:::

Since there are only countably many algorithms, only countably many countable ordinals can be the order types of computable well-orderings: the next lesson studies them. A countable union of countable sets being countable, every countable set of countable ordinals is bounded below $\omega_1$; this uses the axiom of choice.

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

## Notes and references

Cantor introduced ordinals as order types of well-orderings (1883, 1897); von Neumann's definition dates from 1923. The comparison theorem is due to Cantor.

- K. Kunen, *Set Theory*, College Publications, 2011.
- T. Jech, *Set Theory*, 3rd millennium edition, Springer, 2003.
