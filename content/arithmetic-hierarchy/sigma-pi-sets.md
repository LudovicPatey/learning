---
title: Σ⁰ₙ and Π⁰ₙ sets
summary: The arithmetic hierarchy defined by alternations of quantifiers over computable relations; normal forms, closure properties, relativization and many-one reductions.
duration: 40
prerequisites: [turing-degrees/turing-jump, fundamentals/complete-sets]
---

The c.e. sets are the sets defined by an existential quantifier over a computable relation (:ref{#thm-ce-characterizations}). Allowing more quantifiers, alternating between $\exists$ and $\forall$, gives a classification of sets by the complexity of their definitions: the **arithmetic hierarchy**, due to Kleene and Mostowski. The set $\mathrm{Tot}$ of indices of total functions, for instance, is defined by "$\forall x\ \exists s$, the computation $\Phi_e(x)$ converges at stage $s$": a universal quantifier followed by an existential one, over a computable relation. This lesson defines the hierarchy and establishes the closure properties used to place sets in it. The next lesson relates it to the Turing jump.

A quantifier over $\nat$ in front of a computable relation can be read as an unbounded search. A $\Sigma^0_1$ statement $\exists y\ R(x, y)$ is confirmed after finitely many steps when it is true, but is never refuted. A $\Pi^0_2$ statement $\forall y\ \exists z\ R(x, y, z)$ asks that infinitely many such searches all succeed: no finite amount of computation confirms it or refutes it. Each new alternation adds one level of this kind of uncertainty; Post's theorem, in the next lesson, makes this precise by showing that each alternation costs exactly one jump.

## Definition

:::definition{#def-arithmetic-hierarchy}
Let $n \geq 1$ and $k \geq 1$. A relation $A \subseteq \nat^k$ is

1. **$\Sigma^0_n$** if there is a computable relation $R \subseteq \nat^{k + n}$ such that
$$
\vec x \in A \iff \exists y_1\ \forall y_2\ \exists y_3 \cdots Q y_n\ \ R(\vec x, y_1, \dots, y_n),
$$
with $n$ alternating quantifiers, the last one $Q$ being $\exists$ if $n$ is odd and $\forall$ if $n$ is even;
2. **$\Pi^0_n$** if the same holds with the quantifiers $\forall y_1\ \exists y_2 \cdots$, starting with a universal one;
3. **$\Delta^0_n$** if it is both $\Sigma^0_n$ and $\Pi^0_n$.

By convention, the $\Sigma^0_0$, $\Pi^0_0$ and $\Delta^0_0$ relations are the computable relations. A relation is **arithmetic** if it is $\Sigma^0_n$ for some $n$.
:::

The superscript $0$ indicates that the quantifiers range over integers, that is, first-order objects; the analytic hierarchy $\Sigma^1_n$, studied in the course on higher computability, quantifies over sets of integers. Some authors use $\Delta_0$ for the relations defined by formulas with bounded quantifiers only; these are particular computable relations.

:::example{#ex-arithmetic-examples}
1. A set is $\Sigma^0_1$ if it is of the form $\{ x : \exists y\ R(x, y) \}$ with $R$ computable: these are exactly the c.e. sets (:ref{#thm-ce-characterizations}).
2. $\mathrm{Tot} = \{ e : \forall x\ \exists s\ \Phi_e(x)[s]\converge \}$ is $\Pi^0_2$, since the relation $\Phi_e(x)[s]\converge$ is computable (:ref{#prop-stage-properties}).
3. $\mathrm{Fin} = \{ e : W_e \text{ is finite} \} = \{ e : \exists n\ \forall x\ \forall s\ (x > n \to \Phi_e(x)[s]\diverge) \}$ is $\Sigma^0_2$, once the two universal quantifiers are merged (see below).
4. $\mathrm{Cof} = \{ e : W_e \text{ is cofinite} \} = \{ e : \exists n\ \forall x\ \exists s\ (x \leq n \vee \Phi_e(x)[s]\converge) \}$ is $\Sigma^0_3$.
:::

:::figure[The first levels of the arithmetic hierarchy. Each level $\Delta^0_n$ is contained in $\Sigma^0_n$ and in $\Pi^0_n$, and both are contained in $\Delta^0_{n+1}$. All inclusions are strict, as shown in the next lesson.]
<svg class="fig" viewBox="0 0 590 186" width="590" role="img" aria-label="The arithmetic hierarchy: each Delta level is included in the Sigma and Pi levels, which are included in the next Delta level"><defs><marker id="ah-arith" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><line x1="57.2" y1="86.3" x2="101.3" y2="51.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="57.2" y1="113.7" x2="101.3" y2="149.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="137.2" y1="49.7" x2="181.3" y2="85.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="137.2" y1="150.3" x2="181.3" y2="115.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="217.2" y1="86.3" x2="261.3" y2="51.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="217.2" y1="113.7" x2="261.3" y2="149.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="297.2" y1="49.7" x2="341.3" y2="85.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="297.2" y1="150.3" x2="341.3" y2="115.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="377.2" y1="86.3" x2="421.3" y2="51.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="377.2" y1="113.7" x2="421.3" y2="149.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="457.2" y1="49.7" x2="501.3" y2="85.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><line x1="457.2" y1="150.3" x2="501.3" y2="115.0" class="muted-stroke" stroke-width="1.3" marker-end="url(#ah-arith)"/><rect x="20" y="82" width="40" height="36" rx="8" class="soft-fill"/><text x="37" y="105" text-anchor="middle" class="mrm" font-size="19">Δ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">1</tspan></text><text x="117" y="41" text-anchor="middle" class="mrm" font-size="19">Σ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">1</tspan></text><text x="117" y="169" text-anchor="middle" class="mrm" font-size="19">Π<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">1</tspan></text><rect x="180" y="82" width="40" height="36" rx="8" class="soft-fill"/><text x="197" y="105" text-anchor="middle" class="mrm" font-size="19">Δ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">2</tspan></text><text x="277" y="41" text-anchor="middle" class="mrm" font-size="19">Σ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">2</tspan></text><text x="277" y="169" text-anchor="middle" class="mrm" font-size="19">Π<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">2</tspan></text><rect x="340" y="82" width="40" height="36" rx="8" class="soft-fill"/><text x="357" y="105" text-anchor="middle" class="mrm" font-size="19">Δ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">3</tspan></text><text x="437" y="41" text-anchor="middle" class="mrm" font-size="19">Σ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">3</tspan></text><text x="437" y="169" text-anchor="middle" class="mrm" font-size="19">Π<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">3</tspan></text><rect x="500" y="82" width="40" height="36" rx="8" class="soft-fill"/><text x="517" y="105" text-anchor="middle" class="mrm" font-size="19">Δ<tspan font-size="12" dy="-8">0</tspan><tspan font-size="12" dx="-7" dy="15">4</tspan></text><text x="556" y="105" class="mrm muted" font-size="18">⋯</text></svg>
:::

## Normal forms

:::proposition{#prop-hierarchy-basic}
Let $n \geq 1$.

1. A relation is $\Sigma^0_n$ if and only if its complement is $\Pi^0_n$.
2. Every $\Sigma^0_n$ or $\Pi^0_n$ relation is $\Delta^0_{n+1}$.
3. *Contraction.* If $\vec x \in A \iff \exists y_1 \exists y_2\ P(\vec x, y_1, y_2)$ with $P$ a $\Pi^0_{n-1}$ relation, then $\vec x \in A \iff \exists z\ P(\vec x, \pi_0(z), \pi_1(z))$; dually for universal quantifiers. Consequently, a relation defined by a prefix of quantifiers over a computable relation is $\Sigma^0_n$ if the prefix starts with $\exists$ and has $n$ blocks of quantifiers of the same kind, and $\Pi^0_n$ if it starts with $\forall$ and has $n$ blocks.
:::

:::proof{of=prop-hierarchy-basic}
1. The negation of $\exists y_1\ \forall y_2 \cdots R$ is $\forall y_1\ \exists y_2 \cdots \neg R$, and the complement of a computable relation is computable.
2. Add a dummy quantifier: if $\vec x \in A \iff \exists y_1 \cdots Q y_n\ R$, then $\vec x \in A \iff \forall y_0\ \exists y_1 \cdots Q y_n\ R$ and $\vec x \in A \iff \exists y_1 \cdots Q y_n\ Q' y_{n+1}\ R$, where $R$ does not depend on $y_0$ or $y_{n+1}$. The first form is $\Pi^0_{n+1}$, the second $\Sigma^0_{n+1}$. The case of $\Pi^0_n$ relations is symmetric.
3. The pairing function is a bijection, so $\exists y_1 \exists y_2$ ranges over the same pairs as $\exists z$ with $(y_1, y_2) = (\pi_0(z), \pi_1(z))$. The relation $P(\vec x, \pi_0(z), \pi_1(z))$ is $\Pi^0_{n-1}$: substitute $\pi_0(z), \pi_1(z)$ for $y_1, y_2$ in the computable relation of a normal form of $P$, which gives a computable relation, since $\pi_0$ and $\pi_1$ are computable. So merging two adjacent quantifiers of the same kind does not change the level. Applying this to the quantifiers of a prefix over a computable relation, which may stand anywhere in the prefix, merges each block into a single quantifier.
:::

:::quiz[normal forms]
What is the level of $\{ x : \exists y_1\ \exists y_2\ \forall y_3\ \exists y_4\ R(x, y_1, y_2, y_3, y_4) \}$, for $R$ computable?

- [x] $\Sigma^0_3$: the prefix has three blocks, $\exists\exists$, $\forall$, $\exists$, starting with $\exists$.
- [ ] $\Sigma^0_4$, since there are four quantifiers.

  Only the alternations count; adjacent quantifiers of the same kind are merged by pairing.
- [ ] $\Pi^0_3$.

  The prefix starts with an existential quantifier.

---

Why is every $\Pi^0_1$ set also $\Sigma^0_2$?

- [x] A dummy existential quantifier can be added in front: $\forall y\ R(x, y)$ is equivalent to $\exists z\ \forall y\ R(x, y)$.
- [ ] Because every $\Pi^0_1$ set is c.e.

  The complement of the halting set is $\Pi^0_1$ and not c.e.
- [ ] Because the universal quantifier can be turned into an existential one by pairing.

  Pairing merges adjacent quantifiers of the same kind; it never changes a universal quantifier into an existential one.
:::

## Closure properties

To place a set in the hierarchy, one writes a definition and counts alternations. This is justified by the following closure properties.

:::proposition{#prop-hierarchy-closure}
Let $n \geq 1$. The $\Sigma^0_n$ relations and the $\Pi^0_n$ relations are closed under:

1. finite unions and intersections;
2. substitution of total computable functions: if $A \subseteq \nat^m$ is $\Sigma^0_n$ and $g_1, \dots, g_m : \nat^k \to \nat$ are total computable, then $\{ \vec x : (g_1(\vec x), \dots, g_m(\vec x)) \in A \}$ is $\Sigma^0_n$, and likewise for $\Pi^0_n$;
3. bounded quantifiers $\exists z < y$ and $\forall z < y$.

Moreover, $\Sigma^0_n$ relations are closed under existential quantification $\exists y$, and $\Pi^0_n$ relations under universal quantification $\forall y$.
:::

:::proof{of=prop-hierarchy-closure}
By induction on $n$. For $n = 1$, the $\Sigma^0_1$ relations are the c.e. relations, and their closure under finite unions and intersections, substitution (preimages under computable functions), projection and bounded universal quantification is :ref{#prop-ce-closure}; bounded existential quantification $\exists z < y\ P$ is the projection $\exists z\ (z < y \wedge P)$. The $\Pi^0_1$ case follows by complementation, using item 1 of :ref{#prop-hierarchy-basic}.

Suppose the statement holds for $n$, and let $A$ and $B$ be $\Sigma^0_{n+1}$: $\vec x \in A \iff \exists y\ P(\vec x, y)$ and $\vec x \in B \iff \exists y\ Q(\vec x, y)$, with $P$ and $Q$ in $\Pi^0_n$ (by definition, after grouping the quantifiers following the first one).

1. $\vec x \in A \cap B \iff \exists z\ \big(P(\vec x, \pi_0(z)) \wedge Q(\vec x, \pi_1(z))\big)$, and $\vec x \in A \cup B \iff \exists y\ (P(\vec x, y) \vee Q(\vec x, y))$. The relations inside are $\Pi^0_n$ by the induction hypothesis (substitution, then intersection or union).
2. $(g_1(\vec x), \dots) \in A \iff \exists y\ P(g_1(\vec x), \dots, y)$, and the relation inside is $\Pi^0_n$ by the induction hypothesis.
3. $\exists z < w\ \exists y\ P(\vec x, z, y) \iff \exists u\ (\pi_0(u) < w \wedge P(\vec x, \pi_0(u), \pi_1(u)))$, which is $\Sigma^0_{n+1}$. For the bounded universal quantifier, the key equivalence is
$$
\forall z < w\ \ \exists y\ P(\vec x, z, y) \iff \exists v\ \ \forall z < w\ \ \exists y < v\ \ P(\vec x, z, y).
$$
From left to right, choose for each of the finitely many $z < w$ a witness $y_z$, and let $v$ exceed all of them; the converse is clear. By the induction hypothesis, $\exists y < v\ P$ is $\Pi^0_n$ (bounded quantification), then $\forall z < w\ \exists y < v\ P$ is $\Pi^0_n$ (bounded quantification again), so the right-hand side is $\Sigma^0_{n+1}$.

Existential quantification: $\exists u\ \exists y\ P(\vec x, u, y)$ is contracted to a single quantifier. The $\Pi^0_{n+1}$ case follows by complementation.
:::

The equivalence used for the bounded universal quantifier is called **collection**: finitely many witnesses can be bounded by a single number. It fails for unbounded quantifiers, which is why $\forall z\ \exists y$ cannot in general be rewritten as $\exists v\ \forall z$. Soare proves the same closure by another route: the finitely many witnesses $y_z$, $z < w$, are coded by a single finite sequence $\sigma$, and $\forall z < w\ \exists y\ P$ becomes $\exists \sigma\ \forall z < w\ P(\vec x, z, \sigma(z))$.

Together with item 3 of :ref{#prop-hierarchy-basic}, these closure properties justify the method of **quantifier counting**, used throughout the course: write a definition of the set from relations already placed in the hierarchy, using connectives, bounded quantifiers and unbounded quantifiers; move the unbounded quantifiers to the front; and count the blocks.

:::example{#ex-inclusion-pi2}
The relation $\{ (a, b) : W_a \subseteq W_b \}$ is $\Pi^0_2$. Indeed,
$$
W_a \subseteq W_b \iff \forall x\ \big( x \notin W_a \vee x \in W_b \big) \iff \forall x\ \big( \forall s\ \Phi_a(x)[s]\diverge \ \vee\ \exists t\ \Phi_b(x)[t]\converge \big).
$$
The disjunction is of a $\Pi^0_1$ and a $\Sigma^0_1$ relation, both $\Pi^0_2$ (item 2 of :ref{#prop-hierarchy-basic}), so it is $\Pi^0_2$ by closure under unions, and so is its universal closure. Explicitly, the prefix $\forall x\ [\forall s \vee \exists t]$ becomes $\forall x\ \forall s\ \exists t$, a $\Pi^0_2$ prefix. Consequently $\{ (a, b) : W_a = W_b \}$ is $\Pi^0_2$, as an intersection of two $\Pi^0_2$ relations, and the set $\{ e : W_e = \nat \}$ is $\Pi^0_2$, by substitution of a fixed index of $\nat$.
:::

:::quiz[the closure properties]
In the collection equivalence, why must the quantifier $\forall z < w$ be bounded?

- [x] Because a bound $v$ for all the witnesses $y_z$ exists only when there are finitely many of them.

  For $\forall z\ \exists y$, the witnesses may be unbounded, as in $\forall z\ \exists y\ (y > z)$.
- [ ] Because $P$ is only defined for $z < w$.

  $P$ is defined for all values of its arguments; the bound concerns the quantifier, not the relation.
- [ ] Because otherwise the relation would not be computable.

  The issue is the equivalence, not computability.

---

Let $C \subseteq \nat^2$ be a $\Sigma^0_2$ relation. Which of these sets are guaranteed to be $\Sigma^0_2$ by :ref{#prop-hierarchy-closure}?

- [x] $\{ x : \exists y\ (x, y) \in C \}$.

  Existential quantification preserves $\Sigma^0_2$.
- [x] $\{ x : \forall y < x\ \ (x, y) \in C \}$.

  Bounded universal quantification preserves $\Sigma^0_2$, by collection.
- [ ] $\{ x : \forall y\ (x, y) \in C \}$.

  An unbounded universal quantifier in front of a $\Sigma^0_2$ relation gives a $\Pi^0_3$ relation in general.
- [x] $\{ x : (x, 2x + 1) \in C \}$.

  Substitution of total computable functions.
:::

::::exercise{#ex-small-ce-sets difficulty=1 objective="Place index sets defined by the size of $W_e$ by counting quantifiers."}
Show that $\{ e : W_e = \emptyset \}$ is $\Pi^0_1$, that $\{ e : |W_e| \geq 2 \}$ is $\Sigma^0_1$, and that $\{ e : |W_e| = 2 \}$ is $\Delta^0_2$.

:::solution
$W_e = \emptyset \iff \forall x\ \forall s\ \Phi_e(x)[s]\diverge$. Next, $|W_e| \geq 2 \iff \exists x\ \exists x'\ \exists s\ (x \neq x' \wedge \Phi_e(x)[s]\converge \wedge \Phi_e(x')[s]\converge)$. Finally, $|W_e| = 2$ is the intersection of $|W_e| \geq 2$, which is $\Sigma^0_1$, and of the complement of $|W_e| \geq 3$, which is $\Pi^0_1$ by the same argument. Both are $\Delta^0_2$, and $\Delta^0_2$ is closed under intersection.
:::
::::

::::exercise{#ex-rec-sigma3 difficulty=2 objective="Place the set of indices of computable c.e. sets at the third level by quantifying over characteristic indices."}
Show that $\{ e : W_e \text{ is computable} \}$ is $\Sigma^0_3$.

:::solution
Let $E(e, i, x)$ be the relation
$$
\big(x \in W_e \wedge \exists s\ \Phi_i(x)[s]\converge = 1\big) \vee \big(x \notin W_e \wedge \exists s\ \Phi_i(x)[s]\converge = 0\big).
$$
Then $W_e$ is computable if and only if $\exists i\ \forall x\ E(e, i, x)$: if $\forall x\ E(e, i, x)$, then $\Phi_i$ is total with values in $\{0, 1\}$ and computes $W_e$; conversely, an index of the characteristic function of $W_e$ satisfies $\forall x\ E(e, i, x)$. The relation $E$ is a Boolean combination of $\Sigma^0_1$ relations, hence $\Delta^0_2$ and in particular $\Pi^0_2$. So $\forall x\ E$ is $\Pi^0_2$, and $\exists i\ \forall x\ E$ is $\Sigma^0_3$.
:::
::::

## Relativization and reductions

:::definition{#def-relativized-hierarchy}
For $X \in \cs$, the classes $\Sigma^0_n(X)$, $\Pi^0_n(X)$ and $\Delta^0_n(X)$ are defined as in :ref{#def-arithmetic-hierarchy}, with $X$-computable relations in place of computable ones.
:::

All the results above relativize. In particular, the $\Sigma^0_1(X)$ sets are the $X$-c.e. sets, and the $\Delta^0_1(X)$ sets are the $X$-computable sets.

:::proposition{#prop-sigma1-delta1}
1. A set is $\Sigma^0_1$ if and only if it is c.e., and $\Delta^0_1$ if and only if it is computable.
2. If $A \leq_m B$ and $B$ is $\Sigma^0_n(X)$, then $A$ is $\Sigma^0_n(X)$; likewise for $\Pi^0_n(X)$ and $\Delta^0_n(X)$.
:::

:::proof{of=prop-sigma1-delta1}
1. The first statement is :ref{#thm-ce-characterizations}. A set is $\Delta^0_1$ if and only if it and its complement are c.e., that is, if and only if it is computable (:ref{#prop-computable-iff-ce-coce}).
2. If $f$ reduces $A$ to $B$, then $A = \{ x : f(x) \in B \}$, and the result is the substitution property of :ref{#prop-hierarchy-closure}, relativized to $X$.
:::

Many-one reducibility preserves the levels of the hierarchy, while Turing reducibility does not: every set is Turing equivalent to its complement, and the complement of a $\Sigma^0_1$ set that is not computable is not $\Sigma^0_1$. This is why completeness at a level of the hierarchy is defined with many-one reductions.

:::definition{#def-sigma-n-complete}
A set $A$ is **$\Sigma^0_n$-complete** if it is $\Sigma^0_n$ and $B \leq_m A$ for every $\Sigma^0_n$ set $B$; **$\Pi^0_n$-complete** sets are defined similarly.
:::

By :ref{#thm-halting-complete}, $\emptyset'$ is $\Sigma^0_1$-complete, and so its complement is $\Pi^0_1$-complete, since $A \leq_m B$ if and only if $\nat \setminus A \leq_m \nat \setminus B$. A $\Sigma^0_n$-complete set is not $\Pi^0_n$ as soon as some $\Sigma^0_n$ set is not $\Pi^0_n$; the next lesson shows that this is always the case.

## Notes and references

The arithmetic hierarchy was introduced independently by Kleene (1943) and Mostowski (1947). The notation $\Sigma^0_n$, $\Pi^0_n$ brings out the analogy with the Borel hierarchy of descriptive set theory, of which the arithmetic hierarchy is the effective counterpart. Soare's *Turing Computability*, Section 4.1, treats the definition and the closure properties (Theorem 4.1.4) and places $\mathrm{Fin}$, $\mathrm{Cof}$ and $\mathrm{Rec}$ by quantifier counting; the inclusion relation of :ref{#ex-inclusion-pi2} is his Proposition 4.1.7. Shorter treatments are in Downey and Hirschfeldt, Section 2.5, and Nies, Section 1.4. Monin and Patey present the closure properties in terms of uniform unions and intersections.

- S. C. Kleene, *Recursive predicates and quantifiers*, Transactions of the American Mathematical Society 53 (1943), 41–73.
- A. Mostowski, *On definable sets of positive integers*, Fundamenta Mathematicae 34 (1947), 81–112.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 4.1.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.5.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.4.
- B. Monin and L. Patey, *Computability theory*, chapter *Arithmetic hierarchy*.

:::::exercises
::::exercise{#ex-countable-unions difficulty=1 objective="See by a counting argument why closure under existential quantification concerns uniform unions only."}
Show that for each $n$ there are only countably many $\Sigma^0_n$ sets, and deduce that the $\Sigma^0_n$ sets are not closed under arbitrary countable unions.

:::solution
A $\Sigma^0_n$ set is determined by a computable relation, which has an index; so there are countably many. Hence there are countably many arithmetic sets, as a countable union of countable classes, and some set $A$ is not arithmetic, by :ref{#thm-cantor-diagonal}. But $A = \bigcup_{x \in A} \{ x \}$ is a countable union of finite sets, which are computable, hence $\Sigma^0_n$. The closure under existential quantification only applies to **uniform** unions, $\bigcup_y \{ x : (x, y) \in B \}$ with $B$ a single $\Sigma^0_n$ relation.
:::
::::

::::exercise{#ex-place-sets difficulty=1 objective="Write definitions of index sets and relations with the least number of quantifier blocks."}
Give an upper bound in the arithmetic hierarchy for each of the following sets, by writing a definition and counting quantifiers.

1. $\{ e : \text{the range of } \Phi_e \text{ is infinite} \}$.
2. $\{ e : \Phi_e \text{ is total and strictly increasing} \}$.
3. $\{ (a, b) : W_a \cap W_b = \emptyset \}$.
4. $\{ e : \Phi_e(e)\converge \text{ and } \Phi_e(e) \in W_e \}$.

:::solution
1. The range of $\Phi_e$ is infinite if and only if it contains numbers larger than every $n$:
$$
\forall n\ \exists x\ \exists s\ \big( \Phi_e(x)[s]\converge \wedge \Phi_e(x)[s] > n \big).
$$
The relation inside is computable, so after contraction of $\exists x\, \exists s$ the set is $\Pi^0_2$.
2. $\Phi_e$ is total and strictly increasing if and only if $\forall x\ \exists s\ \Phi_e(x)[s]\converge$ and
$$
\forall x\ \forall s\ \big( \Phi_e(x)[s]\converge \wedge \Phi_e(x + 1)[s]\converge \to \Phi_e(x)[s] < \Phi_e(x + 1)[s] \big).
$$
A single stage $s$ suffices in the second condition: if both computations converge, they have both converged at the larger of their two halting stages, by monotonicity. The set is the intersection of a $\Pi^0_2$ and a $\Pi^0_1$ set, hence $\Pi^0_2$.
3. $W_a \cap W_b = \emptyset$ if and only if $\forall x\ \forall s\ \neg (\Phi_a(x)[s]\converge \wedge \Phi_b(x)[s]\converge)$, by the same remark on stages; the relation is $\Pi^0_1$.
4. The condition is $\exists s\ \exists t\ \exists y\ (\Phi_e(e)[s]\converge = y \wedge \Phi_e(y)[t]\converge)$, so the set is $\Sigma^0_1$.
:::
::::

::::exercise{#ex-partial-substitution difficulty=2 objective="See where totality is needed in the closure of the hierarchy under substitution."}
For a partial computable function $\psi$ and $A \subseteq \nat$, let $\psi^{-1}[A] = \{ x : \psi(x)\converge \text{ and } \psi(x) \in A \}$.

1. Show that if $A$ is $\Sigma^0_n$ with $n \geq 1$, then $\psi^{-1}[A]$ is $\Sigma^0_n$, and that if $A$ is $\Pi^0_n$ with $n \geq 2$, then $\psi^{-1}[A]$ is $\Pi^0_n$.
2. Show that there are a partial computable $\psi$ and a $\Pi^0_1$ set $A$ such that $\psi^{-1}[A]$ is not $\Pi^0_1$.

:::solution
Let $c$ be an index of $\psi$, and $G = \{ (x, y) : \exists s\ \Phi_c(x)[s]\converge = y \}$ its graph, a $\Sigma^0_1$ relation.

1. If $A$ is $\Sigma^0_n$, then $x \in \psi^{-1}[A] \iff \exists y\ \big( (x, y) \in G \wedge y \in A \big)$. The relation inside is the intersection of two $\Sigma^0_n$ relations, since $\Sigma^0_1 \subseteq \Sigma^0_n$, and $\Sigma^0_n$ is closed under existential quantification. If $A$ is $\Pi^0_n$ with $n \geq 2$, use the fact that $G$ is the graph of a function:
$$
x \in \psi^{-1}[A] \iff x \in \mathrm{dom}(\psi) \wedge \forall y\ \big( (x, y) \notin G \vee y \in A \big).
$$
Here $\mathrm{dom}(\psi)$ is $\Sigma^0_1$ and $\nat^2 \setminus G$ is $\Pi^0_1$, and both are $\Pi^0_n$ by item 2 of :ref{#prop-hierarchy-basic}, since $n \geq 2$. By :ref{#prop-hierarchy-closure}, the right-hand side is $\Pi^0_n$.
2. Let $\psi(x) \simeq 0$ if $\Phi_x(x)\converge$, undefined otherwise, and $A = \nat$, which is computable, hence $\Pi^0_1$. Then $\psi^{-1}[A] = \emptyset'$. If it were $\Pi^0_1$, it would be $\Delta^0_1$, hence computable (:ref{#prop-sigma1-delta1}), which it is not.

So the restriction to total functions in :ref{#prop-hierarchy-closure} matters only at the level $\Pi^0_1$: the domain of $\psi$, which is $\Sigma^0_1$, is absorbed by every level above.
:::
::::

::::exercise{#ex-collection-sequences difficulty=1 objective="Prove closure under bounded universal quantification by coding the finitely many witnesses into one finite sequence."}
Fix a computable bijection between $\nat$ and the finite sequences of integers, under which the length $|\sigma|$ and the function $(\sigma, z) \mapsto \sigma(z)$ (with value $0$ when $z \geq |\sigma|$) are computable. Let $n \geq 1$ and let $P \subseteq \nat^{k+2}$ be a $\Pi^0_n$ relation. Show that
$$
\forall z < w\ \exists y\ P(\vec x, z, y) \iff \exists \sigma\ \big( |\sigma| = w \wedge \forall z < w\ P(\vec x, z, \sigma(z)) \big),
$$
and deduce, using only the closure of $\Pi^0_n$ under substitution and bounded quantification, that the left-hand side defines a $\Sigma^0_{n+1}$ relation of $(\vec x, w)$.

:::solution
From left to right, choose for each $z < w$ a witness $y_z$ with $P(\vec x, z, y_z)$, and let $\sigma = (y_0, \dots, y_{w-1})$; for $w = 0$, take the empty sequence. From right to left, $y = \sigma(z)$ is a witness for each $z < w$.

The relation $(\vec x, z, \sigma) \mapsto P(\vec x, z, \sigma(z))$ is $\Pi^0_n$, by substitution of the total computable function $(\sigma, z) \mapsto \sigma(z)$. By bounded universal quantification, $\forall z < w\ P(\vec x, z, \sigma(z))$ is $\Pi^0_n$ as a relation of $(\vec x, w, \sigma)$. The relation $|\sigma| = w$ is computable, hence $\Pi^0_n$, and the intersection is $\Pi^0_n$. Its projection along $\sigma$ is $\Sigma^0_{n+1}$. This is the route followed by Soare (2016, Theorem 4.1.4).
:::
::::

::::exercise{#ex-total-graph-delta difficulty=1 objective="Show that a total function with a $\Sigma^0_n$ graph has a $\Delta^0_n$ graph, and see why totality is needed."}
Let $n \geq 1$ and let $f : \nat \to \nat$ be a total function whose graph $G_f = \{ (x, y) : f(x) = y \}$ is $\Sigma^0_n$. Show that $G_f$ is $\Delta^0_n$. Show that the hypothesis that $f$ is total cannot be dropped, already for $n = 1$.

:::solution
Since $f$ is total, $f(x) \neq y$ if and only if $f(x) = z$ for some $z \neq y$:
$$
(x, y) \notin G_f \iff \exists z\ \big( z \neq y \wedge (x, z) \in G_f \big).
$$
The right-hand side is $\Sigma^0_n$ by closure under intersection with a computable relation and existential quantification. So the complement of $G_f$ is $\Sigma^0_n$, that is, $G_f$ is $\Pi^0_n$, and it is $\Delta^0_n$. For $n = 1$ this shows that a total function with a c.e. graph has a computable graph, hence is computable, as $f(x) = \mu y\ (x, y) \in G_f$.

For a partial function the argument fails at the first step. Let $\psi(x) \simeq 0$ if $x \in \emptyset'$, undefined otherwise. Its graph $\{ (x, 0) : x \in \emptyset' \}$ is $\Sigma^0_1$. It is not $\Pi^0_1$: otherwise $\emptyset' = \{ x : (x, 0) \in G_\psi \}$ would be $\Pi^0_1$ by substitution, hence computable.
:::
::::

::::exercise{#ex-pr-normal-form difficulty=2 objective="Strengthen the normal form of the hierarchy to a primitive recursive matrix, using Kleene's normal form theorem."}
Show that in :ref{#def-arithmetic-hierarchy}, for $n \geq 1$, the computable relation $R$ can be taken primitive recursive: every $\Sigma^0_n$ relation $A \subseteq \nat^k$ is of the form $\{ \vec x : \exists y_1\ \forall y_2 \cdots Q y_n\ R(\vec x, y_1, \dots, y_n) \}$ with $R$ primitive recursive, and likewise for $\Pi^0_n$.

:::solution
By induction on $n$, for all arities $k$ simultaneously; the $\Pi^0_n$ case follows from the $\Sigma^0_n$ case by complementation, since the complement of a primitive recursive relation is primitive recursive.

For $n = 1$, $A$ is c.e., so the set $\{ \langle \vec x \rangle : \vec x \in A \}$ of codes of its tuples, with the iterated pairing function, is c.e., hence equal to $W_e$ for some $e$. By Kleene's normal form theorem, $z \in W_e \iff \exists s\ T(e, z, s)$ with $T$ primitive recursive. Then $\vec x \in A \iff \exists s\ T(e, \langle \vec x \rangle, s)$, and $(\vec x, s) \mapsto T(e, \langle \vec x \rangle, s)$ is primitive recursive, since the pairing function is.

Suppose the result holds for $n$, and let $A$ be $\Sigma^0_{n+1}$: $\vec x \in A \iff \exists y\ P(\vec x, y)$ with $P$ a $\Pi^0_n$ relation of arity $k + 1$. By the induction hypothesis applied to $P$, $P(\vec x, y) \iff \forall y_1\ \exists y_2 \cdots Q' y_n\ R'(\vec x, y, y_1, \dots, y_n)$ with $R'$ primitive recursive. Then $\vec x \in A \iff \exists y\ \forall y_1 \cdots Q' y_n\ R'(\vec x, y, y_1, \dots, y_n)$: a prefix of $n + 1$ alternating quantifiers starting with $\exists$, followed by a primitive recursive relation.
:::
::::

::::exercise{#ex-projection-complement difficulty=1 objective="Characterize the arithmetic relations as the closure of the computable relations under projection and complementation."}
Show that a relation is arithmetic if and only if it can be obtained from a computable relation by finitely many applications of projection, $B \mapsto \{ \vec x : \exists y\ (\vec x, y) \in B \}$, and complementation.

:::solution
Let $\mathcal C$ be the class of relations obtained in this way. Every computable relation is $\Sigma^0_1$, hence arithmetic. The arithmetic relations are closed under projection, since $\Sigma^0_n$ is closed under existential quantification, and under complementation, since the complement of a $\Sigma^0_n$ relation is $\Pi^0_n$, hence $\Sigma^0_{n+1}$ (:ref{#prop-hierarchy-basic}). So every relation in $\mathcal C$ is arithmetic.

Conversely, we show by induction on $n \geq 1$ that every $\Sigma^0_n$ relation is in $\mathcal C$. A $\Sigma^0_1$ relation is the projection of a computable relation. A $\Sigma^0_{n+1}$ relation is the projection of a $\Pi^0_n$ relation $P$, whose complement is $\Sigma^0_n$, hence in $\mathcal C$ by the induction hypothesis; so $P$ is in $\mathcal C$, and so is its projection. The computable relations, the $\Sigma^0_0$ relations, are in $\mathcal C$ by definition. This is Soare (2016), Exercise 4.1.10.
:::
::::

::::exercise{#ex-separable-sigma3 difficulty=2 objective="Place a property of pairs of c.e. sets at the third level by quantifying over characteristic indices."}
Two c.e. sets $W_a$ and $W_b$ are **computably separable** if there is a computable set $R$ with $W_a \subseteq R$ and $W_b \cap R = \emptyset$. Show that $\{ \langle a, b \rangle : W_a \text{ and } W_b \text{ are computably separable} \}$ is $\Sigma^0_3$.

:::solution
The pair is computably separable if and only if there is $i$ such that $\Phi_i$ is the characteristic function of such a set $R$, that is,
$$
\begin{aligned}
\exists i\ \Big[ &\forall x\ \exists s\ \big(\Phi_i(x)[s]\converge \wedge \Phi_i(x)[s] \leq 1\big) \\
&\wedge \forall x\ \big( x \notin W_a \vee \exists s\ \Phi_i(x)[s]\converge = 1 \big) \wedge \forall x\ \big( x \notin W_b \vee \exists s\ \Phi_i(x)[s]\converge = 0 \big) \Big].
\end{aligned}
$$
If $i$ satisfies the three conditions, $R = \{ x : \Phi_i(x) = 1 \}$ is computable, contains $W_a$ and is disjoint from $W_b$; conversely, an index of the characteristic function of a separating set satisfies them. The first condition is $\Pi^0_2$. In the second and the third, the disjunction of a $\Pi^0_1$ and a $\Sigma^0_1$ relation is $\Pi^0_2$, and so is its universal closure. The conjunction is $\Pi^0_2$, and the existential quantifier over $i$ gives a $\Sigma^0_3$ relation of $(a, b)$. The set of codes $\langle a, b \rangle$ is $\Sigma^0_3$ by substitution of the projections $\pi_0$ and $\pi_1$. This is Soare (2016), Exercise 4.1.12.
:::
::::

::::exercise[Unique witnesses]{#ex-unique-witness difficulty=3 objective="Choose least witnesses, coded in a finite sequence, so that a $\Sigma^0_{n+1}$ set is a projection with unique witnesses."}
Let $n \geq 1$. Show that every $\Sigma^0_{n+1}$ set $A$ is of the form $\{ x : \exists w\ P'(x, w) \}$ with $P'$ a $\Pi^0_n$ relation such that for every $x$ there is at most one $w$ with $P'(x, w)$.

:::solution
Write $x \in A \iff \exists y\ P(x, y)$ with $P$ in $\Pi^0_n$. The complement of $P$ is $\Sigma^0_n$: $\neg P(x, y) \iff \exists z\ Q(x, y, z)$ with $Q$ in $\Pi^0_{n-1}$ (computable if $n = 1$). Use the coding of finite sequences of :ref{#ex-collection-sequences}. The idea is to accept only the least $y$ with $P(x, y)$, and to certify that the smaller $y'$ fail by giving, for each of them, the least $z$ with $Q(x, y', z)$. Let $P'(x, \langle y, \sigma \rangle)$ hold if
$$
P(x, y) \wedge |\sigma| = y \wedge \forall y' < y\ \Big( Q(x, y', \sigma(y')) \wedge \forall z < \sigma(y')\ \neg Q(x, y', z) \Big).
$$

*Complexity.* $Q(x, y', \sigma(y'))$ is $\Pi^0_{n-1}$ by substitution, and $\forall z < \sigma(y')\ \neg Q(x, y', z)$ is $\Sigma^0_{n-1}$ by bounded quantification; for $n = 1$ both are computable. Both are $\Pi^0_n$ (item 2 of :ref{#prop-hierarchy-basic}), and so is their conjunction, then its bounded universal quantification over $y' < y$. With $P$ and the computable condition $|\sigma| = y$, the relation $P'$ is $\Pi^0_n$.

*Same projection.* If $P'(x, \langle y, \sigma \rangle)$, then $P(x, y)$, so $x \in A$. Conversely, if $x \in A$, let $y$ be least with $P(x, y)$. For each $y' < y$, $\neg P(x, y')$, so there is $z$ with $Q(x, y', z)$; let $\sigma(y')$ be the least one. Then $P'(x, \langle y, \sigma \rangle)$.

*Uniqueness.* If $P'(x, \langle y, \sigma \rangle)$, then $Q(x, y', \sigma(y'))$, hence $\neg P(x, y')$, for every $y' < y$, while $P(x, y)$: so $y$ is the least $y$ with $P(x, y)$. Then $|\sigma| = y$ and each $\sigma(y')$ is the least $z$ with $Q(x, y', z)$, so $\sigma$ is determined, and so is $w = \langle y, \sigma \rangle$.
:::
::::
:::::
