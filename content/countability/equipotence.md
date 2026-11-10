---
title: Equipotence and subpotence
summary: Comparison of sets by bijections and injections; finite sets and the pigeonhole principle.
duration: 35
---

In the *Dialogues Concerning Two New Sciences* (1638), Galileo observes that every integer is the root of exactly one square and every square has exactly one root, so that there should be as many squares as integers; yet the squares form a proper part of the integers, so that there should be fewer of them. He concludes that the attributes "equal", "greater" and "smaller" do not apply to infinite quantities.

Cantor kept the first intuition as a definition: two sets have the same size when their elements can be matched one-to-one. The second intuition, that a proper part is smaller than the whole, is then a theorem about finite sets which fails for infinite ones. This lesson sets up the definitions and proves the facts about finite sets that the comparison relies on.

## Functions and inverses

All functions in this course are total: a function $f : A \to B$ assigns to every $a \in A$ an element $f(a) \in B$. For $X \subseteq A$, the **image** of $X$ is $f(X) = \{f(a) : a \in X\}$, and for $Y \subseteq B$ the **preimage** of $Y$ is $f^{-1}(Y) = \{a \in A : f(a) \in Y\}$. The identity function of $A$ is written $\mathrm{id}_A$.

:::definition{#def-injective}
A function $f : A \to B$ is

1. **injective** if for all $a, a' \in A$, $a \neq a'$ implies $f(a) \neq f(a')$;
2. **surjective** if $f(A) = B$, that is, every $b \in B$ is of the form $f(a)$;
3. **bijective** if it is both injective and surjective.
:::

A composition of injections is an injection, and a composition of surjections is a surjection: if $f : A \to B$ and $g : B \to C$ are surjective and $c \in C$, pick $b$ with $g(b) = c$, then $a$ with $f(a) = b$. Hence a composition of bijections is a bijection.

:::lemma{#lem-inverses}
Let $f : A \to B$.

1. If $A \neq \emptyset$, then $f$ is injective if and only if there is $g : B \to A$ with $g \circ f = \mathrm{id}_A$ (a **left inverse**).
2. If there is $g : B \to A$ with $f \circ g = \mathrm{id}_B$ (a **right inverse**), then $f$ is surjective.
3. $f$ is bijective if and only if there is $g : B \to A$ with $g \circ f = \mathrm{id}_A$ and $f \circ g = \mathrm{id}_B$. Such a $g$ is unique; it is written $f^{-1}$ and is itself a bijection.
:::

:::proof{of=lem-inverses}
1. Suppose $f$ injective, and fix $a_0 \in A$. For $b \in f(A)$ there is exactly one $a$ with $f(a) = b$, by injectivity; let $g(b)$ be this $a$. For $b \notin f(A)$, let $g(b) = a_0$. Then $g(f(a)) = a$ for every $a \in A$. Conversely, if $g \circ f = \mathrm{id}_A$ and $f(a) = f(a')$, then $a = g(f(a)) = g(f(a')) = a'$.
2. Every $b \in B$ equals $f(g(b))$, so it lies in $f(A)$.
3. If $f$ is bijective, define $g(b)$ as the unique $a$ with $f(a) = b$; both identities hold. Conversely, the first identity gives injectivity, as in item 1, and the second gives surjectivity, by item 2. If $g$ and $g'$ both satisfy the two identities, then $g = g \circ (f \circ g') = (g \circ f) \circ g' = g'$. Finally $f^{-1}$ has $f$ as a two-sided inverse, so it is bijective.
:::

:::remark{#rem-right-inverse-choice}
The converse of item 2 — every surjection $f : A \to B$ has a right inverse — requires choosing, for each $b \in B$, one element of the non-empty set $f^{-1}(\{b\})$. For arbitrary sets, this is exactly the **axiom of choice**. No choice is needed when $A \subseteq \nat$: take $g(b)$ to be the *least* element of $f^{-1}(\{b\})$. This device, replacing an arbitrary choice by a least element, is used repeatedly in this course.
:::

:::quiz[the construction of a left inverse]
In item 1, where is the hypothesis $A \neq \emptyset$ used?

- [x] To define $g(b)$ for the elements $b \in B$ outside the image of $f$.

  The value $a_0$ is arbitrary, but some element of $A$ is needed. If $A = \emptyset$ and $B \neq \emptyset$, the empty function $A \to B$ is injective and has no left inverse, since there is no function from a non-empty set to $\emptyset$.
- [ ] To prove that $g(f(a)) = a$.

  This identity only concerns elements of the image of $f$, where $g$ is defined through injectivity.
- [ ] To prove the converse implication.

  The converse holds for every $A$: if $g \circ f = \mathrm{id}_A$, then $f$ is injective.
:::

## Equipotence

:::definition{#def-equipotent}
Two sets $A$ and $B$ are **equipotent** if there is a bijection from $A$ to $B$. We then write $|A| = |B|$.
:::

:::proposition{#prop-equipotence-equivalence}
For all sets $A$, $B$, $C$: $|A| = |A|$; if $|A| = |B|$ then $|B| = |A|$; if $|A| = |B|$ and $|B| = |C|$ then $|A| = |C|$.
:::

:::proof{of=prop-equipotence-equivalence}
The identity $\mathrm{id}_A$ is a bijection. If $f : A \to B$ is a bijection, so is $f^{-1} : B \to A$, by :ref{#lem-inverses}. A composition of bijections is a bijection.
:::

:::figure[Galileo's matching. The integer $n$ is sent to $n^2$; the squares, shaded, form a proper subset of $\nat$, which is nevertheless equipotent to $\nat$.]
<svg class="fig" viewBox="0 0 572 150" width="572" role="img" aria-label="Each integer n is matched with the square n squared, drawn among all integers"><defs><marker id="ah-gal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="4" y="22" class="label">n</text><text x="4" y="138" class="label">n²</text><rect x="20" y="104" width="20" height="20" class="cell head-cell"/><text x="30.0" y="118" text-anchor="middle" class="mrm" font-size="10.5">0</text><rect x="40" y="104" width="20" height="20" class="cell head-cell"/><text x="50.0" y="118" text-anchor="middle" class="mrm" font-size="10.5">1</text><rect x="60" y="104" width="20" height="20" class="cell"/><text x="70.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">2</text><rect x="80" y="104" width="20" height="20" class="cell"/><text x="90.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">3</text><rect x="100" y="104" width="20" height="20" class="cell head-cell"/><text x="110.0" y="118" text-anchor="middle" class="mrm" font-size="10.5">4</text><rect x="120" y="104" width="20" height="20" class="cell"/><text x="130.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">5</text><rect x="140" y="104" width="20" height="20" class="cell"/><text x="150.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">6</text><rect x="160" y="104" width="20" height="20" class="cell"/><text x="170.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">7</text><rect x="180" y="104" width="20" height="20" class="cell"/><text x="190.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">8</text><rect x="200" y="104" width="20" height="20" class="cell head-cell"/><text x="210.0" y="118" text-anchor="middle" class="mrm" font-size="10.5">9</text><rect x="220" y="104" width="20" height="20" class="cell"/><text x="230.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">10</text><rect x="240" y="104" width="20" height="20" class="cell"/><text x="250.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">11</text><rect x="260" y="104" width="20" height="20" class="cell"/><text x="270.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">12</text><rect x="280" y="104" width="20" height="20" class="cell"/><text x="290.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">13</text><rect x="300" y="104" width="20" height="20" class="cell"/><text x="310.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">14</text><rect x="320" y="104" width="20" height="20" class="cell"/><text x="330.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">15</text><rect x="340" y="104" width="20" height="20" class="cell head-cell"/><text x="350.0" y="118" text-anchor="middle" class="mrm" font-size="10.5">16</text><rect x="360" y="104" width="20" height="20" class="cell"/><text x="370.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">17</text><rect x="380" y="104" width="20" height="20" class="cell"/><text x="390.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">18</text><rect x="400" y="104" width="20" height="20" class="cell"/><text x="410.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">19</text><rect x="420" y="104" width="20" height="20" class="cell"/><text x="430.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">20</text><rect x="440" y="104" width="20" height="20" class="cell"/><text x="450.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">21</text><rect x="460" y="104" width="20" height="20" class="cell"/><text x="470.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">22</text><rect x="480" y="104" width="20" height="20" class="cell"/><text x="490.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">23</text><rect x="500" y="104" width="20" height="20" class="cell"/><text x="510.0" y="118" text-anchor="middle" class="mrm muted" font-size="10.5">24</text><rect x="520" y="104" width="20" height="20" class="cell head-cell"/><text x="530.0" y="118" text-anchor="middle" class="mrm" font-size="10.5">25</text><text x="546" y="119" class="mrm muted" font-size="15">⋯</text><circle cx="30" cy="30" r="13" class="node"/><text x="30" y="35" text-anchor="middle" class="mrm" font-size="14">0</text><line x1="30.0" y1="44.0" x2="30.0" y2="101.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/><circle cx="130" cy="30" r="13" class="node"/><text x="130" y="35" text-anchor="middle" class="mrm" font-size="14">1</text><line x1="119.7" y1="39.5" x2="52.2" y2="102.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/><circle cx="230" cy="30" r="13" class="node"/><text x="230" y="35" text-anchor="middle" class="mrm" font-size="14">2</text><line x1="218.1" y1="37.3" x2="112.6" y2="102.4" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/><circle cx="330" cy="30" r="13" class="node"/><text x="330" y="35" text-anchor="middle" class="mrm" font-size="14">3</text><line x1="318.1" y1="37.3" x2="212.6" y2="102.4" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/><circle cx="430" cy="30" r="13" class="node"/><text x="430" y="35" text-anchor="middle" class="mrm" font-size="14">4</text><line x1="419.7" y1="39.5" x2="352.2" y2="102.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/><circle cx="530" cy="30" r="13" class="node"/><text x="530" y="35" text-anchor="middle" class="mrm" font-size="14">5</text><line x1="530.0" y1="44.0" x2="530.0" y2="101.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-gal)"/><text x="550" y="35" class="mrm muted" font-size="15">⋯</text></svg>
:::

:::example{#ex-equipotent-sets}
1. $\nat$ and the set of squares $\{n^2 : n \in \nat\}$ are equipotent, via $n \mapsto n^2$, which is injective on $\nat$ since squaring is strictly increasing on non-negative numbers.
2. $\nat$ and $\nat \setminus \{0\}$ are equipotent, via $n \mapsto n + 1$; more generally, $\nat$ and $\nat \setminus \{0, \dots, k-1\}$ via $n \mapsto n + k$.
3. $\nat$ and the set $E$ of even numbers are equipotent, via $n \mapsto 2n$.
4. The open interval $(-1, 1)$ and $\mathbb R$ are equipotent, via $x \mapsto x / (1 - |x|)$. Its inverse is $y \mapsto y / (1 + |y|)$: if $y = x/(1-|x|)$, then $y$ has the sign of $x$ and $|y| = |x|/(1 - |x|)$, so that $|x| = |y|/(1 + |y|)$ and $x = y/(1+|y|)$. Since every non-empty open interval $(a, b)$ is equipotent to $(-1, 1)$ by an affine map, all non-empty open intervals are equipotent to $\mathbb R$.
:::

In each of the first three examples, a set is equipotent to a proper subset of itself. This is the phenomenon Galileo found paradoxical, and the next section shows that it cannot happen for finite sets.

:::remark
The notation $|A| = |B|$ suggests an equality between two objects, the **cardinalities** of $A$ and $B$. A cardinality can be defined as a set (in ZFC, the least ordinal equipotent to $A$), but this course does not need it: the relation $|A| = |B|$ is defined directly, and $|A|$ on its own is only a notation.
:::

:::quiz[the definition of equipotence]
Which of these functions show that $\nat$ and the set $E = \{0, 2, 4, \dots\}$ are equipotent?

- [x] $n \mapsto 2n$, from $\nat$ to $E$.

  It is injective, and every even number $2k$ is the image of $k$.
- [ ] $n \mapsto n + 2$, from $\nat$ to $E$.

  It does not map into $E$: $1 \mapsto 3$.
- [x] $m \mapsto m/2$, from $E$ to $\nat$.

  It is the inverse of $n \mapsto 2n$, hence a bijection. A bijection in either direction suffices, by symmetry.
- [ ] $n \mapsto 4n$, from $\nat$ to $E$.

  It is injective but not surjective, since $2 \neq 4n$ for every $n$. It only shows that $E$ is at least as large as $\nat$, in the sense of the last section.
:::

## Finite sets

For $n \in \nat$, write $\underline n = \{0, 1, \dots, n - 1\}$, so that $\underline 0 = \emptyset$.

:::definition{#def-finite}
A set $A$ is **finite** if $|A| = |\underline n|$ for some $n \in \nat$, and **infinite** otherwise.
:::

That $n$ is determined by $A$ — the number of elements of $A$ — is a consequence of the following principle.

:::lemma[Pigeonhole principle]{#lem-pigeonhole}
For all $m > n$, there is no injection from $\underline m$ into $\underline n$.
:::

:::proof{of=lem-pigeonhole}
By induction on $n$. For $n = 0$: since $m > 0$, the set $\underline m$ contains $0$, and there is no function at all from a non-empty set into $\underline 0 = \emptyset$.

Suppose the statement holds for $n$, and let $f : \underline m \to \underline{n+1}$ be injective, with $m > n + 1$. If $n \notin f(\underline m)$, then $f$ maps $\underline m$ injectively into $\underline n$, which contradicts the induction hypothesis since $m > n$. Otherwise $n = f(k)$ for a unique $k < m$. Let $\tau : \underline m \to \underline m$ exchange $k$ and $m - 1$ and fix every other element. Then $f \circ \tau$ is injective and sends $m - 1$ to $n$; by injectivity, it sends no element of $\underline{m-1}$ to $n$. So its restriction to $\underline{m-1}$ is an injection into $\underline n$, with $m - 1 > n$, which contradicts the induction hypothesis.
:::

:::corollary{#cor-finite-cardinality}
1. If $|\underline m| = |\underline n|$, then $m = n$.
2. If $A$ is finite, $A$ is not equipotent to any proper subset $B \subsetneq A$.
3. $\nat$ is infinite.
:::

:::proof{of=cor-finite-cardinality}
1. If $m \neq n$, say $m > n$, a bijection $\underline m \to \underline n$ would be an injection, contradicting :ref{#lem-pigeonhole}.
2. Let $\beta : A \to \underline n$ be a bijection, and suppose $h : A \to B$ is a bijection onto $B \subsetneq A$. Pick $a \in A \setminus B$. Then $n \geq 1$; let $\sigma$ be the permutation of $\underline n$ exchanging $\beta(a)$ and $n - 1$. The map $\sigma \circ \beta$ is a bijection $A \to \underline n$ sending $a$ to $n - 1$, so it sends $B \subseteq A \setminus \{a\}$ into $\underline{n-1}$. Then $\sigma \circ \beta \circ h \circ \beta^{-1} \circ \sigma^{-1}$ is an injection from $\underline n$ into $\underline{n-1}$, a contradiction.
3. By item 2, since $\nat$ is equipotent to its proper subset $\nat \setminus \{0\}$.
:::

So a finite set has a well-defined number of elements, and Galileo's matching is a property of infinite sets only. Dedekind took the converse as a definition: a set is *Dedekind-infinite* if it is equipotent to a proper subset. That every infinite set is Dedekind-infinite uses the axiom of choice (in a weak form); see :ref{#ex-dedekind-infinite} in the lesson on countable sets.

:::quiz[the proof of the pigeonhole principle]
Why does the induction step compose $f$ with the exchange $\tau$, instead of restricting $f$ to $\underline{m-1}$ directly?

- [x] Because $f$ need not send $m - 1$ to $n$; after the exchange, the only element sent to $n$ is $m - 1$, which is removed by the restriction.

  Restricting $f$ itself to $\underline{m-1}$ could leave $k$, with $f(k) = n$, in the domain, so the restriction would not map into $\underline n$.
- [ ] Because the restriction of an injection need not be injective.

  The restriction of an injection is always an injection.
- [ ] To make $f$ surjective.

  Surjectivity plays no role in the argument.

---

In which case of the induction step is the hypothesis $m > n + 1$ used to get $m - 1 > n$?

- [ ] Only in the case $n \notin f(\underline m)$.

  In that case, the induction hypothesis is applied with $m$ itself, which only needs $m > n$.
- [x] In the case $n \in f(\underline m)$, where the induction hypothesis is applied to $\underline{m-1}$.

  The restriction is an injection $\underline{m-1} \to \underline n$, and the induction hypothesis applies only if $m - 1 > n$.
:::

## Subpotence

Intuitively, $B$ is at least as large as $A$ if every element of $A$ can be given its own representative in $B$.

:::definition{#def-subpotent}
A set $A$ is **subpotent** to a set $B$ if there is an injection from $A$ into $B$. We then write $|A| \leq |B|$, and $|A| \nleq |B|$ otherwise. We write $|A| < |B|$ if $|A| \leq |B|$ and $|A| \neq |B|$.
:::

If $A \subseteq B$, the inclusion map shows $|A| \leq |B|$. By :ref{#lem-pigeonhole}, $|\underline n| < |\underline m|$ whenever $n < m$.

:::proposition{#prop-subpotent-transitive}
The relation $\leq$ is reflexive and transitive: $|A| \leq |A|$, and if $|A| \leq |B|$ and $|B| \leq |C|$, then $|A| \leq |C|$. Moreover, it is compatible with equipotence: if $|A| = |A'|$ and $|B| = |B'|$, then $|A| \leq |B|$ if and only if $|A'| \leq |B'|$.
:::

:::proof{of=prop-subpotent-transitive}
The identity is an injection. If $f : A \to B$ and $g : B \to C$ are injections and $x \neq y$ in $A$, then $f(x) \neq f(y)$ by injectivity of $f$, hence $g(f(x)) \neq g(f(y))$ by injectivity of $g$; so $g \circ f$ is an injection. For the last statement, if $\alpha : A' \to A$ and $\beta : B \to B'$ are bijections and $f : A \to B$ is an injection, then $\beta \circ f \circ \alpha : A' \to B'$ is an injection; the converse is symmetric.
:::

:::quiz[the proof of transitivity]
Suppose that $f : A \to B$ is only **surjective** and $g : B \to C$ is injective. What does the argument give?

- [ ] $g \circ f$ is injective, so $|A| \leq |C|$.

  The first step fails: $x \neq y$ no longer implies $f(x) \neq f(y)$.
- [ ] $g \circ f$ is a bijection between $A$ and $C$.

  Neither injectivity nor surjectivity of $g \circ f$ follows.
- [x] No relation between $|A|$ and $|C|$.

  The argument uses the injectivity of both maps. For instance, with $A = \nat$, $B = \underline 1$, $C = \underline 1$, one has a surjection $A \to B$, an injection $B \to C$, and $|A| \nleq |C|$.
:::

Surjections compare sets in the opposite direction, at least when the domain is a set of integers.

:::proposition{#prop-surjection-subpotent}
If $A \subseteq \nat$ and $f : A \to B$ is surjective, then $|B| \leq |A|$.
:::

:::proof{of=prop-surjection-subpotent}
For $b \in B$, the set $f^{-1}(\{b\})$ is a non-empty set of integers; let $g(b)$ be its least element. Then $f(g(b)) = b$, so $g$ has a left inverse and is injective by :ref{#lem-inverses}.
:::

For arbitrary $A$, the same statement holds under the axiom of choice (:ref{#rem-right-inverse-choice}). Two questions remain. Is $\leq$ antisymmetric, that is, do $|A| \leq |B|$ and $|B| \leq |A|$ imply $|A| = |B|$? This is the Cantor–Bernstein theorem of the next lesson. Is there a pair of infinite sets with $|A| < |B|$? This is Cantor's diagonal argument, three lessons ahead.

## Exercises

::::exercise{difficulty=1}
Let $b \notin A$. Show that if $|\nat| \leq |A|$, then $|A \cup \{b\}| = |A|$.

:::solution
Let $i : \nat \to A$ be an injection. Define $h : A \cup \{b\} \to A$ by $h(b) = i(0)$, $h(i(n)) = i(n+1)$ for $n \in \nat$, and $h(x) = x$ for $x \in A \setminus i(\nat)$. This is well defined since $i$ is injective. It is injective, since it is injective on each of the three pieces $\{b\}$, $i(\nat)$ and $A \setminus i(\nat)$, whose images $\{i(0)\}$, $i(\nat \setminus \{0\})$ and $A \setminus i(\nat)$ are disjoint. It is surjective, since these three images cover $A$.
:::
::::

::::exercise{difficulty=1}
Show that every subset of a finite set is finite.

:::solution
It suffices to treat subsets $S \subseteq \underline m$, by transporting through a bijection. By induction on $m$: for $m = 0$, $S = \emptyset = \underline 0$. If $S \subseteq \underline{m+1}$, then $S' = S \setminus \{m\} \subseteq \underline m$ is in bijection with some $\underline k$ via some $\beta$, by the induction hypothesis. If $m \notin S$, then $S = S'$. Otherwise, extend $\beta$ by $m \mapsto k$; this is a bijection from $S$ to $\underline{k+1}$.
:::
::::

::::exercise{difficulty=2}
Show that if $A$ is finite and $f : A \to A$ is injective, then $f$ is surjective. Show that this fails for $A = \nat$.

:::solution
If $f$ were injective and not surjective, then $f$ would be a bijection from $A$ onto the proper subset $f(A) \subsetneq A$, which contradicts :ref{#cor-finite-cardinality}. For $A = \nat$, the successor $n \mapsto n + 1$ is injective and not surjective.
:::
::::

## Notes and references

The passage on squares and roots is in the First Day of Galileo's *Discorsi* (1638). Cantor introduced the comparison of sets by one-to-one correspondences in his papers of 1874 and 1878, under the name *Mächtigkeit* (power); the term "equipotent" derives from it. Dedekind defined infinite sets as those equipotent to a proper subset in *Was sind und was sollen die Zahlen?* (1888). For a systematic treatment of cardinality in axiomatic set theory, see Hrbacek and Jech.

- G. Galilei, *Discorsi e dimostrazioni matematiche intorno a due nuove scienze*, Leiden, 1638.
- G. Cantor, *Ein Beitrag zur Mannigfaltigkeitslehre*, Journal für die reine und angewandte Mathematik 84 (1878), 242–258.
- R. Dedekind, *Was sind und was sollen die Zahlen?*, Vieweg, Braunschweig, 1888.
- K. Hrbacek and T. Jech, *Introduction to Set Theory*, 3rd edition, Marcel Dekker, 1999.
