---
title: Σ⁰ₙ and Π⁰ₙ sets
summary: The arithmetic hierarchy defined by alternations of quantifiers over computable relations; normal forms, closure properties, relativization and many-one reductions.
duration: 35
prerequisites: [turing-degrees/turing-jump]
---

The c.e. sets are the sets defined by an existential quantifier over a computable relation (:ref{#thm-ce-characterizations}). Allowing more quantifiers, alternating between $\exists$ and $\forall$, gives a classification of sets by the complexity of their definitions: the **arithmetic hierarchy**, due to Kleene and Mostowski. The set $\mathrm{Tot}$ of indices of total functions, for instance, is defined by "$\forall x\ \exists s$, the computation $\Phi_e(x)$ converges at stage $s$": a universal quantifier followed by an existential one, over a computable relation. This lesson defines the hierarchy and establishes the closure properties used to place sets in it. The next lesson relates it to the Turing jump.

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
3. The pairing function is a bijection, so $\exists y_1 \exists y_2$ ranges over the same pairs as $\exists z$ with $(y_1, y_2) = (\pi_0(z), \pi_1(z))$. Substituting the computable functions $\pi_0, \pi_1$ in a computable relation gives a computable relation, so merging two adjacent quantifiers of the same kind does not change the level. Repeating this merges each block into a single quantifier.
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
- [ ] Because $\Pi^0_1$ sets are computable in $\emptyset'$.

  This is true, but the statement is about forms of definitions, and follows directly from adding a quantifier.
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

The equivalence used for the bounded universal quantifier is called **collection**: finitely many witnesses can be bounded by a single number. It fails for unbounded quantifiers, which is why $\forall z\ \exists y$ cannot in general be rewritten as $\exists v\ \forall z$.

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

## Exercises

::::exercise{difficulty=1}
Show that $\{ e : W_e = \emptyset \}$ is $\Pi^0_1$, that $\{ e : |W_e| \geq 2 \}$ is $\Sigma^0_1$, and that $\{ e : |W_e| = 2 \}$ is $\Delta^0_2$.

:::solution
$W_e = \emptyset \iff \forall x\ \forall s\ \Phi_e(x)[s]\diverge$. Next, $|W_e| \geq 2 \iff \exists x\ \exists x'\ \exists s\ (x \neq x' \wedge \Phi_e(x)[s]\converge \wedge \Phi_e(x')[s]\converge)$. Finally, $|W_e| = 2$ is the intersection of $|W_e| \geq 2$, which is $\Sigma^0_1$, and of the complement of $|W_e| \geq 3$, which is $\Pi^0_1$ by the same argument. Both are $\Delta^0_2$, and $\Delta^0_2$ is closed under intersection.
:::
::::

::::exercise{difficulty=1}
Show that for each $n$ there are only countably many $\Sigma^0_n$ sets, and deduce that the $\Sigma^0_n$ sets are not closed under arbitrary countable unions.

:::solution
A $\Sigma^0_n$ set is determined by a computable relation, which has an index; so there are countably many. Hence some set $A$ is not arithmetic, by :ref{#thm-cantor-diagonal}. But $A = \bigcup_{x \in A} \{ x \}$ is a countable union of finite sets, which are computable, hence $\Sigma^0_n$. The closure under existential quantification only applies to **uniform** unions, $\bigcup_y \{ x : (x, y) \in B \}$ with $B$ a single $\Sigma^0_n$ relation.
:::
::::

::::exercise{difficulty=2}
Show that $\{ e : W_e \text{ is computable} \}$ is $\Sigma^0_3$.

:::solution
Let $E(e, i, x)$ be the relation
$$
\big(x \in W_e \wedge \exists s\ \Phi_i(x)[s]\converge = 1\big) \vee \big(x \notin W_e \wedge \exists s\ \Phi_i(x)[s]\converge = 0\big).
$$
Then $W_e$ is computable if and only if $\exists i\ \forall x\ E(e, i, x)$: if $\forall x\ E(e, i, x)$, then $\Phi_i$ is total with values in $\{0, 1\}$ and computes $W_e$; conversely, an index of the characteristic function of $W_e$ satisfies $\forall x\ E(e, i, x)$. The relation $E$ is a Boolean combination of $\Sigma^0_1$ relations, hence $\Delta^0_2$ and in particular $\Pi^0_2$. So $\forall x\ E$ is $\Pi^0_2$, and $\exists i\ \forall x\ E$ is $\Sigma^0_3$.
:::
::::

## Notes and references

The arithmetic hierarchy was introduced independently by Kleene (1943) and Mostowski (1947). The notation $\Sigma^0_n$, $\Pi^0_n$ is due to Addison, by analogy with the Borel hierarchy of descriptive set theory, of which it is the effective counterpart. Rogers' and Soare's textbooks treat the hierarchy in detail.

- S. C. Kleene, *Recursive predicates and quantifiers*, Transactions of the American Mathematical Society 53 (1943), 41–73.
- A. Mostowski, *On definable sets of positive integers*, Fundamenta Mathematicae 34 (1947), 81–112.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
