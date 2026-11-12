---
title: Computable well-orderings
summary: Computable and c.e. well-orderings, their closure properties, the Church–Kleene ordinal, the index set WO, and the information that an index of a well-ordering does not reveal.
duration: 40
prerequisites: [ordinals, fundamentals/ce-sets]
---

Only countably many ordinals can be described by an algorithm. There are two natural ways of doing so. In Cantor's spirit, an ordinal is **computable** if it is the order type of a computable well-ordering of numbers. In von Neumann's spirit, an ordinal is **constructive** if it has a **notation**: a number that tells whether the ordinal is zero, a successor or a limit, and in the last two cases gives notations for its predecessor or for a sequence converging to it. This lesson studies the first notion; the next one introduces Kleene's system of notations and shows that the two notions define the same ordinals. The supremum of these ordinals is the Church–Kleene ordinal $\omega_1^{\mathrm{CK}}$, the ordinal along which the rest of the track iterates the jump.

## Computable well-orderings

:::definition{#def-computable-ordinal}
An ordinal $\alpha$ is **computable** if it is the order type of a computable relation $R \subseteq \nat \times \nat$ that well-orders its field $F = \{ x : (x, x) \in R \}$: $R \subseteq F \times F$, and $(x, y) \in R$ means $x \leq_R y$. The same convention defines c.e. well-orderings and, without the well-foundedness condition, computable and c.e. linear orders.
:::

The relation is reflexive, so that the field can be read off from it: a single element $x$ forms the well-ordering $\{ (x, x) \}$ of type $1$. A pair $(x, y)$ is coded by a number with a computable pairing function, so a relation is a set of numbers and the usual notions of computability apply to it.

:::example{#ex-computable-orders}
1. Every finite ordinal is computable, and so is $\omega$, the type of the usual order of $\nat$.
2. The orders of :ref{#ex-well-orderings} are computable: $1 < 2 < 3 < \cdots < 0$ has type $\omega + 1$, and the even numbers followed by the odd numbers form a computable well-ordering of type $\omega \cdot 2$.
3. Compare pairs $\langle x, y \rangle$ first by $y$, then by $x$. This is a computable well-ordering of $\nat$ of type $\omega^2$ (:ref{#ex-ordinal-arithmetic}).
4. The usual orders of $\mathbb Z$ and of $\mathbb Q$, transported to $\nat$ by a computable bijection, and the order $(\nat, >)$, are computable linear orders that are not well-orderings.
:::

To speak of all computable linear orders at once, we index them by programs.

:::definition{#def-wo}
For a number $e$, write $L_e$ for the relation $\{ (x, y) : \Phi_e(\langle x, y \rangle) = 1 \}$ when $\Phi_e$ is total with values in $\{ 0, 1 \}$. We say that $e$ is an **index of a computable linear order** if $\Phi_e$ is total, $\{ 0, 1 \}$-valued, and $L_e$ is a linear order of its field in the sense of :ref{#def-computable-ordinal}. Let
$$
\mathrm{WO} = \{ e : e \text{ is an index of a computable linear order and } L_e \text{ is a well-ordering} \}.
$$
For $e \in \mathrm{WO}$, the order type $|L_e|$ is a computable ordinal, and every computable ordinal is of this form.
:::

Being an index of a computable linear order is a $\Pi^0_2$ condition: totality is $\Pi^0_2$, and the axioms of a linear order are universal statements about the values of $\Phi_e$. Being a well-ordering is of a different nature, since it quantifies over all infinite descending sequences. The lesson on $\Pi^1_1$ sets shows that $\mathrm{WO}$ is not arithmetic, and is in fact $\Pi^1_1$-complete (:ref{#cor-pi11-complete}).

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

The third item is the reason why c.e. presentations will be used freely: a linear order that is merely enumerated is automatically decidable, because for two distinct elements, one of the two possible comparisons is eventually enumerated. The restriction to an infinite field makes the transformation uniform; the following lesson removes it, when needed, by placing a copy of $\omega$ in front of the order.

:::quiz[computable well-orderings]
In the proof of :ref{#prop-computable-ordinals-basic} (3), why is $S$ computable and not merely c.e.?

- [x] Because $S$ is a linear order of $\nat$: for $m \neq n$, exactly one of $(m, n)$ and $(n, m)$ is in $S$, and one of them is eventually enumerated, which decides both.
- [ ] Because the field $F$ is computable.

  $F$ is only c.e.; it is the bijection $f$, computed by enumerating $F$, that makes the field of $S$ equal to $\nat$.
- [ ] Because $R$ is a well-ordering.

  Well-foundedness plays no role: the argument works for every c.e. linear order with infinite field, for instance an order of type $\mathbb Q$.
:::

## The Church–Kleene ordinal

:::definition{#def-omega1ck}
The **Church–Kleene ordinal** $\omega_1^{\mathrm{CK}}$ is the least ordinal that is not computable.
:::

By :ref{#prop-computable-ordinals-basic} (1), the computable ordinals are exactly the ordinals below $\omega_1^{\mathrm{CK}}$: they form a downward closed set of ordinals, which is the ordinal $\omega_1^{\mathrm{CK}}$ itself, as in the proof of :ref{#prop-omega1}. There are countably many computable relations, so $\omega_1^{\mathrm{CK}}$ is countable. It is therefore the order type of some well-ordering of $\nat$, but of no computable one. By (2), it is a limit ordinal, closed under addition and multiplication. It is also closed under ordinal exponentiation, a fact we do not use; the first exercise shows that $\omega^n$ and $\omega^\omega$ are computable, and an exercise of the next lesson shows that $\varepsilon_0$, the least ordinal with $\omega^{\varepsilon_0} = \varepsilon_0$, is computable.

The ordinal $\omega_1^{\mathrm{CK}}$ is much larger than the ordinals one meets in arithmetic, such as $\varepsilon_0$, the ordinal of Gentzen's consistency proof for Peano arithmetic. It has, however, a precise computability-theoretic meaning: by Spector's boundedness theorem (:ref{#thm-boundedness}), the order types of a $\Sigma^1_1$ set of indices in $\mathrm{WO}$ are bounded below it, and the hyperarithmetic sets are exactly the sets obtained by iterating the jump along the computable ordinals.

## What an index does not reveal

An index of a computable well-ordering determines its order type, but this type cannot be read off computably from the index, even in the simplest cases. The following construction places one number at the end of the usual order of $\nat$ exactly when a computation halts.

:::proposition{#prop-wo-not-transparent}
There is a total computable function $f$ such that $f(n) \in \mathrm{WO}$ for every $n$, with $|L_{f(n)}| = \omega + 1$ if $n \in \emptyset'$ and $|L_{f(n)}| = \omega$ otherwise. Consequently, no partial computable function $\psi$ satisfies, for every $e \in \mathrm{WO}$, that $\psi(e)$ converges and equals $1$ if $L_e$ has a largest element and $0$ otherwise.
:::

:::proof{of=prop-wo-not-transparent}
Fix an enumeration of $\emptyset'$. Call a number $x$ **special** for $n$ if $n$ enters $\emptyset'$ exactly at stage $x$; whether $x$ is special for $n$ is decidable, and there is at most one special number. Let $L_{f(n)}$ be the order on $\nat$ in which the special number, if there is one, is the largest element, and the other numbers are ordered as usual. To compare $x$ and $y$, it suffices to decide whether $x$ or $y$ is special, so $f$ is total computable by the SMN theorem. If $n \notin \emptyset'$, the order is the usual order of $\nat$, of type $\omega$. If $n \in \emptyset'$, it is the usual order of $\nat \setminus \{ s \}$, of type $\omega$, followed by the special number $s$: its type is $\omega + 1$.

If $\psi$ existed, then $n \in \emptyset'$ if and only if $\psi(f(n)) = 1$, and $\psi \circ f$ would be a total computable function deciding $\emptyset'$.
:::

:::figure[The two possible orders $L_{f(n)}$. If $n$ never enters $\emptyset'$, the order is the usual one. If $n$ enters at stage $3$, the number $3$ is removed from its place and put after all the others.]
<svg class="fig" viewBox="0 0 600 132" width="600" role="img" aria-label="Two orders on the natural numbers: the usual order, and the usual order with the special number 3 moved to the end"><text x="132.0" y="45.0" text-anchor="end" class="label" font-size="12">n ∉ ∅′</text><line x1="144" y1="28" x2="144" y2="52" class="axis"/><text x="156.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">0</text><text x="190.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">1</text><text x="224.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">2</text><text x="258.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">3</text><text x="292.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">4</text><text x="326.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">5</text><text x="360.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">6</text><text x="394.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">7</text><text x="428.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">8</text><text x="462.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">9</text><text x="496.0" y="45.0" text-anchor="middle" class="mrm" font-size="15">10</text><text x="528.0" y="45.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="558.0" y="20.0" text-anchor="middle" class="label" font-size="12">type ω</text><text x="132.0" y="101.0" text-anchor="end" class="label" font-size="12">n ∈ ∅′ at stage 3</text><line x1="144" y1="84" x2="144" y2="108" class="axis"/><text x="156.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">0</text><text x="190.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">1</text><text x="224.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">2</text><text x="258.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">4</text><text x="292.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">5</text><text x="326.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">6</text><text x="360.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">7</text><text x="394.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">8</text><text x="428.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">9</text><text x="462.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">10</text><text x="496.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">11</text><text x="528.0" y="101.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><rect x="546" y="83" width="24" height="24" rx="4" class="head-cell"/><text x="558.0" y="101.0" text-anchor="middle" class="mrm" font-size="15">3</text><text x="558.0" y="76.0" text-anchor="middle" class="label" font-size="12">type ω + 1</text></svg>
:::

:::quiz[the order f(n)]
Why is the relation $L_{f(n)}$ computable, although $\emptyset'$ is not?

- [x] Because comparing $x$ and $y$ only requires knowing whether $x$ or $y$ is the stage at which $n$ enters $\emptyset'$, and this is decided by running the enumeration for $\max(x, y) + 1$ stages.
- [ ] Because $f(n)$ is computed only for $n \notin \emptyset'$.

  $f$ is total; the order $L_{f(n)}$ is computable for every $n$.
- [ ] Because $\emptyset'$ is computable relative to the order $L_{f(n)}$.

  This is true of the family of orders but irrelevant: the question is how each single order is decided.
:::

The proposition shows that a computable well-ordering hides the decomposition of its type into successor and limit steps: whether the type is a successor depends on whether the order has a largest element, a $\Sigma^0_2$ property of the index (second exercise) that no algorithm decides. Kleene's notations, introduced in the next lesson, make this decomposition explicit, at the price of a set of notations that is far from computable.

## Exercises

::::exercise{difficulty=2}
Show that $\omega^n$ is computable for every $n$, uniformly in $n$, and that $\omega^\omega = \sup_n \omega^n$ is computable.

:::solution
By induction, $\omega^n$ is the type of $\nat^n$ ordered anti-lexicographically (compare the last components first, then the previous ones): for $n = 0$ this is a one-element order, and $\nat^{n+1}$ ordered in this way is $\omega$ copies of $\nat^n$, of type $\omega^n \cdot \omega = \omega^{n+1}$, by the description of multiplication in the previous lesson. These orders are computable, uniformly in $n$ (code $\nat^n$ by sequence numbers of length $n$).

Let $S$ be their ordered sum: the elements are the pairs $\langle n, x \rangle$ with $x \in \nat^n$, compared first by $n$, then by the order of $\nat^n$. It is a computable linear order, and a well-ordering, since a descending sequence would have eventually constant first components and then descend in some $\nat^n$. Its type is at least $\omega^n$ for every $n$, since the block of index $n$ is a copy of $\nat^n$; so $|S| \geq \omega^\omega$. Conversely, the initial segment below an element of the block $n$ is contained in the blocks $0, \dots, n$, whose type $1 + \omega + \cdots + \omega^n$ is at most $\omega^n \cdot (n + 1) < \omega^{n+1}$. Every proper initial segment of $S$ therefore has type below $\omega^\omega$, and $|S| \leq \omega^\omega$.
:::
::::

::::exercise{difficulty=1}
Let $e$ be an index of a computable linear order. Show that "$L_e$ has a largest element" is a $\Sigma^0_2$ property of $e$, and that the set of elements of the field of $L_e$ that have an immediate predecessor is $\Sigma^0_2$, uniformly in $e$.

:::solution
$L_e$ has a largest element if and only if $\exists x\, [(x, x) \in L_e \wedge \forall y\, ((y, y) \in L_e \rightarrow (y, x) \in L_e)]$, where $(y, x) \in L_e$ means $\Phi_e(\langle y, x \rangle) = 1$, a computable relation of $e$, $x$, $y$ for indices of total functions. The form is $\exists \forall$, that is, $\Sigma^0_2$. An element $x$ has an immediate predecessor if and only if $\exists y\, [y <_{L_e} x \wedge \forall z\, \neg (y <_{L_e} z <_{L_e} x)]$, again $\Sigma^0_2$.
:::
::::

## Notes and references

Church and Kleene (1936–1938) introduced the constructive ordinals, and the ordinal $\omega_1^{\mathrm{CK}}$ is named after them. The notion of computable ordinal, defined from computable well-orderings, is the one used by Markwald (1954), who proved that it coincides with the notion of constructive ordinal (next lesson). Monin and Patey present computable and constructive ordinals in the section *Effective ordinals* of their chapter on transfinite numbers, including the observation that a c.e. linear order is computable. In Simpson's book, countable well-orderings are coded as in :ref{#def-computable-ordinal} (Definition V.1.1). Nies defines $\omega_1^{\mathrm{CK}}$ in Section 9.1, where c.e. indices of well-orderings play the role of $\mathrm{WO}$.

- H. Rogers, Jr., *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- B. Monin and L. Patey, *Computability theory*, chapter *Transfinite numbers*, section *Effective ordinals*.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section V.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.1.
