---
title: Indicators and the provably total functions of IΣ₁
summary: Indicators for cuts satisfying a theory T; the main theorem on indicators gives a true Π₂ sentence unprovable in T and a bound on the T-provably total functions; the hierarchy F_k gives an indicator for IΣ₁; hence IΣ₁ does not prove that all F_k are total, and every function provably total in IΣ₁ is primitive recursive (Parsons, Mints, Takeuti).
duration: 45
prerequisites: [fast-growing, models-of-computation/primitive-recursion]
---

The previous lesson found semiregular cuts between $a$ and $F_\nu(a)$, for non-standard $\nu$. Two consequences follow from this, by arguments that do not depend on the particular functions $F_k$: a true $\Pi_2$ sentence unprovable in $\mathrm I\Sigma_1$, and an upper bound on the growth of every function provably total in $\mathrm I\Sigma_1$. Paris and Kirby isolated the property used, which they called an **indicator**: a $\Sigma_1$ formula that measures how large an interval $[a, b]$ is, in such a way that the interval is "infinitely large" exactly when a cut satisfying the theory fits inside it. This lesson states the method in general, applies it to $\mathrm I\Sigma_1$, and completes the proof of the theorem of Parsons, Mints and Takeuti (:ref{#thm-pmt}). Lesson 5 applies it to Peano arithmetic.

## Growth of the hierarchy in the standard model

We first record how the functions $F_k$ of :ref{#def-fgh} compare in $\nat$.

:::lemma{#lem-fgh-monotone}
For all $k, x$ in $\nat$:

1. $F_k$ is strictly increasing, and $F_k^{(i)}(y) \geq y + i$;
2. $F_k(x) \leq F_{k+1}(x)$, and $F_{k+1}(x) \geq F_k(x) + x$ for $x \geq 1$.
:::

:::proof{of=lem-fgh-monotone}
1. By induction on $k$. For $F_0$ it is clear. If $F_k$ is strictly increasing with $F_k(y) > y$, its iterates are increasing in $y$ and $F_k^{(i)}(y) \geq y + i$. So $F_{k+1}(x + 1) = F_k^{(x)}(F_k(x + 2)) > F_k^{(x)}(x + 1) = F_{k+1}(x)$, since $F_k(x + 2) > x + 1$, and $F_{k+1}(x) \geq 2x + 1 > x$.
2. For $x = 0$, both sides equal $1$ (:ref{#ex-fgh-values}). For $x \geq 1$, $F_{k+1}(x) = F_k^{(x-1)}(F_k(x + 1)) \geq F_k(x + 1) + x - 1 \geq F_k(x) + x$, by item 1.
:::

## Indicators

Cuts are taken closed under addition and multiplication when we say that they satisfy a theory, so that they are substructures (:ref{#lem-cut-model}).

:::definition[Paris, Kirby]{#def-indicator}
Let $T$ be a theory in $\mathcal L_A$ containing $\mathrm I\Sigma_1$. An **indicator** for $T$ is a $\Sigma_1$ formula $\iota(x, y, c)$ such that $\mathrm I\Sigma_1 \vdash \iota(x, y, c) \rightarrow c \leq y$, and such that for every countable non-standard model $M$ of $\mathrm I\Sigma_1$ and all $a \leq b$ in $M$ with $a$ non-standard, the following are equivalent:

1. $M \models \iota(a, b, c)$ for some non-standard $c$;
2. there is a cut $I$ of $M$ with $a \in I$, $b \notin I$ and $I \models T$.
:::

One reads $\iota(a, b, c)$ as "$[a, b]$ is $c$-large". The condition $c \leq y$ is a normalization: a non-standard degree of largeness forces $b$ to be non-standard. Hájek and Pudlák use a function $Y(a, b)$ in place of the formula, and Wong a binary function with monotonicity conditions; the version with a third argument avoids having to define a maximum, which would not be $\Sigma_1$. The model $M$ is a model of $\mathrm I\Sigma_1$, not necessarily of $T$: this is needed in lesson 5, where cuts satisfying $\mathrm{PA}$ are found in models of much weaker theories.

:::theorem[Paris, Kirby]{#thm-indicator-main}
Let $\iota$ be an indicator for $T$.

1. If $T$ is consistent, $T$ does not prove $\forall x\ \forall c\ \exists y\ \iota(x, y, c)$.
2. If $\nat \models T$ and $f$ is provably total in $T$ (:ref{#def-provably-total}), there is $n \in \nat$ such that $\nat \models \neg \iota(x, f(x), n)$ for every $x$.
:::

:::proof{of=thm-indicator-main}
1. Suppose $T \vdash \forall x\ \forall c\ \exists y\ \iota(x, y, c)$. Let $M$ be a countable non-standard model of $T$, given by compactness, and $a \in M$ non-standard. By the least number principle for $\Sigma_1$ formulas (:ref{#prop-fo-least-number}), let $b$ be least with $M \models \iota(a, b, a)$; then $a \leq b$. Since $a$ is non-standard, there is a cut $I \models T$ with $a \in I$ and $b \notin I$. As $I \models T$, there is $y \in I$ with $I \models \iota(a, y, a)$. The formula $\iota$ is $\Sigma_1$, so $M \models \iota(a, y, a)$ (:ref{#cor-sigma1-upward}), and $y < b$ since $y \in I$ and $b \notin I$: this contradicts the minimality of $b$.

2. Let $\varphi_f$ be the $\Sigma_1$ formula with $T \vdash \forall x\ \exists! y\ \varphi_f(x, y)$. Suppose that for every $n$ there is $x \in \nat$ with $\nat \models \iota(x, f(x), n)$. Let $M$ be a countable non-standard model of the theory of $\nat$; it satisfies $T$ and $\mathrm I\Sigma_1$. The formula
$$
\theta(n) \equiv \exists x\ \exists y\ \big(\varphi_f(x, y) \wedge \iota(x, y, n)\big)
$$
is $\Sigma_1$ and true in $\nat$, hence in $M$, for every standard $n$. By overspill (:ref{#cor-overspill}), $M \models \theta(\nu)$ for some non-standard $\nu$: there are $x, y \in M$ with $\varphi_f(x, y)$ and $\iota(x, y, \nu)$. Then $y \geq \nu$ is non-standard. For standard $x$, the value of $f$ in $M$ is the standard number $f(x)$, since $\nat \models \varphi_f(x, f(x))$, $\Sigma_1$ formulas go up, and $\varphi_f$ defines a function in $M$; so $x$ is non-standard. By the indicator property there is a cut $I \models T$ with $x \in I$ and $y \notin I$. Since $I \models T$, some $y' \in I$ satisfies $I \models \varphi_f(x, y')$; then $M \models \varphi_f(x, y')$, and $y' = y$ by functionality in $M$, although $y' \in I$ and $y \notin I$. This contradiction proves the claim.
:::

The two parts use only the implication from 1 to 2 in :ref{#def-indicator}. The converse implication says that the indicator measures nothing else, and it shows that each instance $\forall x\ \exists y\ \iota(x, y, n)$, for standard $n$, is true in every model of $T$; for the indicators of this course it is proved directly. So the sentence of part 1 is a $\Pi_2$ sentence true in $\nat$, all of whose standard instances in $c$ are provable in $T$, and which is not provable in $T$.

:::quiz[the main theorem on indicators]
In part 1 of the proof of :ref{#thm-indicator-main}, why is $b$ chosen *least* with $\iota(a, b, a)$?

- [x] So that the witness $y$ found in the cut, which is below $b$, contradicts the choice of $b$. Without minimality, a witness below $b$ would contradict nothing.
- [ ] So that $b$ is non-standard.

  Any $b$ with $\iota(a, b, a)$ is at least $a$, hence non-standard.
- [ ] To apply overspill.

  Part 1 uses no overspill: the largeness $a$ is non-standard from the start.

---

In part 2, why must $x$ be non-standard before the indicator property can be applied?

- [x] :ref{#def-indicator} only requires the equivalence for non-standard $a$. The normalization $c \leq y$ makes $y = f(x)$ non-standard, and $f$ maps standard numbers to standard numbers, so $x$ is non-standard.
- [ ] Because a cut cannot contain a standard element.

  Every cut contains all standard elements.
- [ ] Because overspill only produces non-standard elements.

  Overspill produces the non-standard $\nu$; the element $x$ is a different element.
:::

## An indicator for IΣ₁

:::proposition{#prop-indicator-isigma1}
The formula $\iota_1(x, y, c) \equiv c \leq y \wedge \exists z \leq y\ F_c(x) = z$ is an indicator for $\mathrm I\Sigma_1$.
:::

:::proof{of=prop-indicator-isigma1}
The formula is $\Sigma_1$, and implies $c \leq y$. Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$ and $a \leq b$ in $M$, with $a$ non-standard.

(1 ⇒ 2) If $M \models \iota_1(a, b, c)$ with $c$ non-standard, then $F_c(a) \leq b$, and :ref{#thm-kirby-paris-cut}, with $\nu = c$ and $a \geq 1$, gives a semiregular cut $I$ with $a \in I$ and $F_c(a) \notin I$; then $b \notin I$, and $I \models \mathrm I\Sigma_1$.

(2 ⇒ 1) Let $I \models \mathrm I\Sigma_1$ be a cut with $a \in I$ and $b \notin I$. For standard $k$, $I \models F_k(a) = z$ for some $z \in I$, by :ref{#lem-fgh-isigma1}; then $M \models F_k(a) = z$ by :ref{#cor-sigma1-upward}, and $z < b$. So $M \models \iota_1(a, b, k)$ for every standard $k$. This is a $\Sigma_1$ formula in $k$ with parameters $a, b$, and overspill gives a non-standard $c$ with $M \models \iota_1(a, b, c)$.
:::

:::corollary[Kirby, Paris]{#cor-isigma1-fgh}
$\mathrm I\Sigma_1$ does not prove $\forall k\ \forall x\ F_k(x){\downarrow}$, although it proves $\forall x\ F_k(x){\downarrow}$ for each standard $k$.
:::

:::proof{of=cor-isigma1-fgh}
If $F_c(x)$ exists, then $y = \max(c, F_c(x))$ satisfies $\iota_1(x, y, c)$. So $\forall k\ \forall x\ F_k(x){\downarrow}$ implies $\forall x\ \forall c\ \exists y\ \iota_1(x, y, c)$ in $\mathrm I\Sigma_1$, and the latter is not provable, by part 1 of :ref{#thm-indicator-main}. The second statement is :ref{#lem-fgh-isigma1}.
:::

The true $\Pi_2$ sentence $\forall k\ \forall x\ F_k(x){\downarrow}$ is provable in $\mathrm I\Sigma_2$ (exercise of :ref{to="independence/fast-growing"}). Its unprovability in $\mathrm I\Sigma_1$ is proved without Gödel's incompleteness theorems: no consistency statement is involved, only the construction of a cut.

## The provably total functions of IΣ₁

Part 2 of :ref{#thm-indicator-main}, for the indicator $\iota_1$, bounds the provably total functions of $\mathrm I\Sigma_1$; a bound and a $\Sigma_1$ definition together give a primitive recursive definition.

:::theorem{#thm-isigma1-envelope}
Let $f : \nat \to \nat$ be provably total in $\mathrm I\Sigma_1$. Then there is $n \in \nat$ with $f(x) < F_n(x) + n$ for all $x$, and $f$ is primitive recursive.
:::

:::proof{of=thm-isigma1-envelope}
*The bound.* By part 2 of :ref{#thm-indicator-main} and :ref{#prop-indicator-isigma1}, there is $n$ such that $\iota_1(x, f(x), n)$ fails for every $x$: either $f(x) < n$ or $f(x) < F_n(x)$. In both cases $f(x) < F_n(x) + n$.

*Primitive recursiveness.* Let $\varphi_f(x, y) \equiv \exists w\ \delta(x, y, w)$, with $\delta$ bounded, be the $\Sigma_1$ formula of the definition (a block of existential quantifiers is contracted by pairing, :ref{#fact-pairing}). Let $\psi(x, u)$ be the bounded formula saying that $u = \langle y, w \rangle$ for some $y, w \leq u$ with $\delta(x, y, w)$, and that no $u' < u$ has this property. In $\mathrm I\Sigma_1$, $\exists y\ \varphi_f(x, y)$ gives some $u$ with the first property, and the least number principle for bounded formulas gives a unique $u$ with $\psi(x, u)$. So the function $g$ defined by $\psi$ is provably total in $\mathrm I\Sigma_1$, and by the first part $g(x) < F_m(x) + m$ for some $m$. In $\nat$, if $\psi(x, \langle y, w \rangle)$ then $\varphi_f(x, y)$, so $y = f(x)$. Hence
$$
f(x) = \mu y < B(x)\ \exists w < B(x)\ \psi\big(x, \langle y, w \rangle\big), \qquad B(x) = F_m(x) + m.
$$
The relation defined by $\psi$ is primitive recursive (:ref{#lem-bounded-computable}), $B$ is primitive recursive, and bounded quantification and bounded minimization preserve primitive recursiveness (:ref{#cor-pr-bounded-quantifiers}, :ref{#prop-pr-bounded-mu}); so $f$ is primitive recursive.
:::

With :ref{#thm-pr-provably-total} this proves :ref{#thm-pmt}: the functions provably total in $\mathrm I\Sigma_1$ are exactly the primitive recursive functions. Hájek and Pudlák (Corollary IV.3.7) obtain the sharper statement that the defining formula is provably equivalent to a primitive recursive derivation; we do not need it. Combining the two directions also gives a growth theorem without reference to provability.

:::corollary{#cor-pr-fgh-bound}
For every primitive recursive function $f : \nat \to \nat$ there is $n$ with $f(x) < F_n(x) + n$ for all $x$. The function $x \mapsto F_x(x)$ is not primitive recursive, and it is not provably total in $\mathrm I\Sigma_1$.
:::

:::proof{of=cor-pr-fgh-bound}
The first statement is :ref{#thm-isigma1-envelope} applied to $f$, which is provably total by :ref{#thm-pr-provably-total}. Suppose $F_x(x) < F_n(x) + n$ for all $x$. For $x \geq n + 1$, :ref{#lem-fgh-monotone} gives $F_x(x) \geq F_{n+1}(x) \geq F_n(x) + x > F_n(x) + n$, a contradiction. So $x \mapsto F_x(x)$ is not primitive recursive, hence not provably total in $\mathrm I\Sigma_1$, by :ref{#thm-isigma1-envelope}.
:::

The first statement is the analogue for the hierarchy $F_k$ of the majorization theorem for the Ackermann function (:ref{#thm-ack-majorization}); it was obtained here from a model-theoretic construction. The **method of indicators** has three steps, which lessons 3–5 repeat for Peano arithmetic: a combinatorial notion of largeness that $T$ proves for each standard degree; a construction of a cut satisfying $T$ inside any interval of non-standard largeness; and :ref{#thm-indicator-main}.

## Exercises

::::exercise{difficulty=1}
Show that for each standard $n$, $\mathrm I\Sigma_1 \vdash \forall x\ \exists y\ \iota_1(x, y, n)$, so that every standard instance of the sentence of :ref{#cor-isigma1-fgh} in the variable $c$ is provable.

:::solution
By :ref{#lem-fgh-isigma1}, $\mathrm I\Sigma_1$ proves that $F_n(x)$ exists; take $y = \max(n, F_n(x))$.
:::
::::

::::exercise{difficulty=2}
Let $T \supseteq \mathrm I\Sigma_1$ be true in $\nat$, with an indicator $\iota$ that is monotone in $y$: $\nat \models \iota(x, y, n) \wedge y \leq y' \rightarrow \iota(x, y', n)$. Suppose that $h_n(x) = $ the least $y$ with $\iota(x, y, n)$ exists for all $n, x$. Show that for every $T$-provably total $f$ there is $n$ with $f(x) < h_n(x)$ for every $x$. Explain why some monotonicity in $y$ is needed to turn part 2 of :ref{#thm-indicator-main} into a bound.

:::solution
Part 2 gives $n$ with $\neg \iota(x, f(x), n)$ for every $x$. By monotonicity, $\iota(x, y, n)$ holds for every $y \geq h_n(x)$; so $f(x) \geq h_n(x)$ would give $\iota(x, f(x), n)$; so $f(x) < h_n(x)$. Without monotonicity, $\neg \iota(x, f(x), n)$ only says that $f(x)$ avoids the set $\{ y : \iota(x, y, n) \}$, which may have gaps above its least element. For $\iota_1$, monotonicity in $y$ holds as soon as $y \geq n$, which is why the bound of :ref{#thm-isigma1-envelope} has the form $F_n(x) + n$.
:::
::::

## Notes and references

Indicators were introduced by Paris and Kirby; the definition and the main theorem are in Hájek and Pudlák, Chapter IV, Definition 3.9 and Theorem 3.10 (with a function $Y$ in place of the formula $\iota$), and in Wong's Lecture 5, Further exercises. The proof of part 2 follows Theorem IV.3.10 (iv), there stated as the existence of an envelope (Definition IV.3.3). The characterization of the provably total functions of $\mathrm I\Sigma_1$ is due to Parsons (1970), Mints (1971) and Takeuti; the proof by indicators is Hájek and Pudlák, Corollary IV.3.7. Kirby and Paris's survey (1982) and Bovykin's introduction (2009) present the method informally.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- L. A. S. Kirby and J. B. Paris, *Accessible independence results for Peano arithmetic*, Bulletin of the London Mathematical Society 14 (1982), 285–293.
- G. Mints, *Quantifier-free and one-quantifier systems*, Zapiski Nauchnykh Seminarov LOMI 20 (1971), 115–133; English translation in Journal of Soviet Mathematics 1 (1973), 71–84.
- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- A. Bovykin, *Brief introduction to unprovability*, in Logic Colloquium 2006, Lecture Notes in Logic 32, 2009, 38–64.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 3(a)–(b).
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
