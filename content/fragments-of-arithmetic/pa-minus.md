---
title: The base theory PA⁻ and non-standard models
summary: The theory PA⁻ of the non-negative parts of discretely ordered rings; the standard numbers form an initial segment of every model; bounded, Σₙ and Πₙ formulas in arbitrary models; the model ℤ[X]⁺ and non-standard models of true arithmetic.
duration: 40
prerequisites: [arithmetic-hierarchy/arithmetic-definability]
---

This course studies theories of arithmetic and their **non-standard models**, and the fragments of Peano arithmetic obtained by restricting induction to formulas of bounded complexity. The track assumes first-order logic: the completeness, compactness and Löwenheim–Skolem theorems, and Gödel's incompleteness theorems. This lesson fixes an algebraic base theory, proves that the standard numbers sit at the bottom of every model, sets up the classes of formulas used throughout the course, and gives the first non-standard models. The next lesson shows that bounded formulas have the same meaning in a model and in its extensions at the top.

## The language and the base theory

The **language of arithmetic** $\mathcal L_A$ has constants $0$ and $1$, binary function symbols $+$ and $\cdot$, and a binary relation symbol $<$. The course on arithmetic definability used a successor symbol $S$ instead of $1$; the two languages define the same relations in every structure considered here, since $S(x)$ is the term $x + 1$ and $1$ is $S(0)$. We write $x \leq y$ for $x < y \vee x = y$. The **standard model** is $\nat$ with its usual operations and order. For $k \in \nat$, the **numeral** $\bar k$ is the term $0 + 1 + \cdots + 1$ with $k$ occurrences of $1$.

:::definition[PA⁻]{#def-pa-minus}
The theory $\mathrm{PA}^-$ consists of the universal closures of the following axioms:

1. $(x + y) + z = x + (y + z)$, $\ x + y = y + x$, $\ (x \cdot y) \cdot z = x \cdot (y \cdot z)$, $\ x \cdot y = y \cdot x$;
2. $x \cdot (y + z) = x \cdot y + x \cdot z$, $\ x + 0 = x$, $\ x \cdot 0 = 0$, $\ x \cdot 1 = x$;
3. $\neg (x < x)$, $\ x < y \wedge y < z \rightarrow x < z$, $\ x < y \vee x = y \vee y < x$;
4. $x < y \rightarrow x + z < y + z$, $\ 0 < z \wedge x < y \rightarrow x \cdot z < y \cdot z$;
5. $x < y \rightarrow \exists z\, (x + z + 1 = y)$;
6. $0 < 1$, $\ 0 < x \rightarrow 1 \leq x$, $\ 0 \leq x$.
:::

The models of $\mathrm{PA}^-$ are exactly the non-negative parts of discretely ordered commutative rings: rings with a compatible linear order in which $1$ is the least positive element. There is no induction in $\mathrm{PA}^-$; the fragments of Peano arithmetic add induction schemes to it.

:::lemma{#lem-pam-basic}
1. $\mathrm{PA}^-$ proves $x < y \rightarrow x + 1 \leq y$.
2. For every $k \in \nat$, $\mathrm{PA}^-$ proves $\forall x\, \big(x < \bar k \leftrightarrow (x = \bar 0 \vee x = \bar 1 \vee \cdots \vee x = \overline{k - 1})\big)$; for $k = 0$, the right-hand side is the empty disjunction, false.
3. For all $k, m \in \nat$, $\mathrm{PA}^-$ proves $\bar k + \bar m = \overline{k + m}$ and $\bar k \cdot \bar m = \overline{k m}$, and it proves $\bar k < \bar m$ when $k < m$.
:::

:::proof{of=lem-pam-basic}
1. If $x < y$, axiom 5 gives $z$ with $x + z + 1 = y$. By axiom 6, $0 \leq z$. If $z = 0$, then $y = x + 1$. If $0 < z$, then $0 + (x + 1) < z + (x + 1)$ by axiom 4, that is $x + 1 < y$, using commutativity and associativity.

3. By induction on $m$ in the metatheory. The numeral $\overline{m+1}$ is $\bar m + 1$, so $\bar k + \overline{m + 1} = (\bar k + \bar m) + 1 = \overline{k + m} + 1 = \overline{k + m + 1}$ by associativity, and $\bar k \cdot \overline{m + 1} = \bar k \cdot \bar m + \bar k \cdot 1 = \overline{km} + \bar k = \overline{km + k}$ by distributivity and the case of addition. If $k < m$, then $\bar m = \bar k + \overline{m - k}$, and $\overline{m - k} = \overline{m - k - 1} + 1$ is positive, since $0 \leq \overline{m - k - 1}$ gives $1 \leq \overline{m - k}$ by axiom 4 and $0 < 1$; so $\bar k + 0 < \bar k + \overline{m - k}$ by axiom 4.

2. By induction on $k$ in the metatheory. For $k = 0$, $\neg (x < 0)$ follows from $0 \leq x$ and the order axioms. Assume the statement for $k$, and let $x < \overline{k + 1} = \bar k + 1$. If $x < \bar k$, the induction hypothesis applies. Otherwise $x = \bar k$ or $\bar k < x$; in the second case $\bar k + 1 \leq x$ by item 1, which contradicts $x < \bar k + 1$. Conversely, each $\bar i$ with $i \leq k$ is less than $\overline{k+1}$ by item 3.
:::

:::quiz[the numerals in PA⁻]
Items 2 and 3 of :ref{#lem-pam-basic} are proved "by induction on $k$" or "on $m$". Why is this legitimate, although $\mathrm{PA}^-$ has no induction axiom?

- [x] The induction is carried out in the metatheory, over standard numbers: for each $k \in \nat$ it produces a separate proof in $\mathrm{PA}^-$ of the statement about the numeral $\bar k$. Nothing is claimed about non-standard elements.
- [ ] Because the statements are true in $\nat$, which is a model of $\mathrm{PA}^-$.

  Truth in $\nat$ does not give provability: "every number is even or odd" is true in $\nat$ and not provable in $\mathrm{PA}^-$ (:ref{#ex-zx-plus}).
- [ ] Because the induction is applied inside a model of $\mathrm{PA}^-$ to the set of numerals.

  In a non-standard model, the set of numerals contains $0$ and is closed under successor but is not the whole model; no induction inside $M$ could prove anything about it, and none is available in $\mathrm{PA}^-$.
:::

Write $\bar k^M$ for the value of $\bar k$ in a model $M$. The lemma gives at once:

:::proposition{#prop-standard-part}
For every model $M$ of $\mathrm{PA}^-$, the map $k \mapsto \bar k^M$ is an isomorphism of $\nat$ onto a substructure of $M$ that is an initial segment of $M$: every element of $M$ below a numeral is a numeral.
:::

The image is the **standard part** of $M$, written $\nat \subseteq M$; the other elements are **non-standard**, and greater than every standard number. The model is **standard** if it has no non-standard element, that is, if it is isomorphic to $\nat$.

## Formula classes in arbitrary models

The classes of formulas are those of the course on arithmetic definability (:ref{#def-bounded-formula}), now read in every $\mathcal L_A$-structure rather than in $\nat$ alone.

:::definition{#def-formula-classes}
A quantifier is **bounded** if it has the form $\exists x\, (x < t \wedge \cdots)$ or $\forall x\, (x < t \rightarrow \cdots)$, written $\exists x < t$ and $\forall x < t$, where $t$ is a term not containing $x$. A formula is **bounded**, or **$\Delta_0$**, if all its quantifiers are bounded. For $n \geq 1$, a **$\Sigma_n$ formula** has the form $\exists \bar x_1\, \forall \bar x_2 \cdots Q \bar x_n\ \delta$ and a **$\Pi_n$ formula** the form $\forall \bar x_1\, \exists \bar x_2 \cdots Q \bar x_n\ \delta$, with $n$ alternating blocks of unbounded quantifiers followed by a $\Delta_0$ formula $\delta$; we set $\Sigma_0 = \Pi_0 = \Delta_0$.

Let $T$ be a theory and $M$ a structure. A formula is **$\Sigma_n$ in $T$** if $T$ proves it equivalent to a $\Sigma_n$ formula, and **$\Delta_n$ in $T$** if it is both $\Sigma_n$ and $\Pi_n$ in $T$; similarly **in $M$**, with $M \models$ instead of $T \vdash$. A set $S \subseteq M^k$ is **$\Sigma_n$-definable in $M$** if $S = \{ \bar a \in M^k : M \models \varphi(\bar a, \bar c) \}$ for a $\Sigma_n$ formula $\varphi$ and **parameters** $\bar c \in M$; similarly for $\Pi_n$ and $\Delta_n$.
:::

Blocks may be empty, so a $\Sigma_n$ or $\Pi_n$ formula is both $\Sigma_m$ and $\Pi_m$ for every $m > n$. Up to logical equivalence, conjunctions and disjunctions of $\Sigma_n$ formulas are $\Sigma_n$, negations of $\Sigma_n$ formulas are $\Pi_n$, and $\exists x < t$ in front of a $\Sigma_n$ formula, and $\forall x < t$ in front of a $\Pi_n$ formula, give again a $\Sigma_n$, respectively $\Pi_n$, formula, since the bounded quantifier merges with the first block and its guard $x < t$ moves into the matrix. The remaining case, $\forall x < t$ in front of a $\Sigma_n$ formula, is the subject of the collection schemes of :ref{to="induction-collection"}; it is not a logical equivalence.

:::example{#ex-delta0-examples}
1. "$x$ is prime" is defined in $\nat$ by the $\Delta_0$ formula $1 < x \wedge \forall y < x\ \forall z < x\ \neg(y \cdot z = x)$.
2. Every $\Delta_0$ formula defines a primitive recursive relation in $\nat$ (:ref{#lem-bounded-computable}), and a relation on $\nat$ is $\Sigma_n$-definable if and only if it is $\Sigma^0_n$ in the sense of computability (:ref{#thm-definable-arithmetic}, after merging the quantifiers of the inner $\Sigma_1$ or $\Pi_1$ formula with the last block).
:::

## Non-standard models

The first non-standard model is algebraic. It shows how little $\mathrm{PA}^-$ proves: a simple $\Pi_1$ sentence true in $\nat$ fails in it.

:::example[An algebraic model]{#ex-zx-plus}
Order the polynomial ring $\mathbb Z[X]$ by declaring a polynomial positive when its leading coefficient is positive. It is discrete: if $0 < p < 1$, then $p$ and $1 - p$ have positive leading coefficients, which forces $p$ to be a constant, and there is no integer strictly between $0$ and $1$. Let $\mathbb Z[X]^+$ be the set of non-negative polynomials, with the induced operations and order. The axioms of :ref{#def-pa-minus} hold in it: those of items 1–4 and 6 hold in the non-negative part of every discretely ordered ring, and for item 5, if $p < q$ then $q - p \geq 1$ by discreteness, so $z = q - p - 1$ is non-negative and $p + z + 1 = q$.

So $\mathbb Z[X]^+$ is a model of $\mathrm{PA}^-$. Its standard part consists of the constant polynomials $0, 1, 2, \dots$, and $X$ is non-standard, since $X - k$ is positive for every $k$. The element $X$ is neither $y + y$ nor $y + y + 1$, because every polynomial $y + y$ has even coefficients and $y + y + 1$ has an odd constant term, while $X$ has the coefficient $1$ and the constant term $0$. So the $\Pi_1$ sentence
$$
\forall x\ \exists y < x + 1\ (x = y + y \vee x = y + y + 1),
$$
"every number is even or odd", true in $\nat$, fails in $\mathbb Z[X]^+$, and $\mathrm{PA}^-$ does not prove it. Induction for bounded formulas proves it (:ref{to="bounded-induction"}).
:::

The compactness theorem gives non-standard models of every theory true in $\nat$. Let $c$ be a new constant. Every finite subset of $\mathrm{Th}(\nat) \cup \{ \bar k < c : k \in \nat \}$ has a model, namely $\nat$ with $c$ interpreted as a large number; by compactness and the Löwenheim–Skolem theorem, the whole set has a countable model $M$. It satisfies every sentence true in $\nat$, and the interpretation of $c$ is non-standard. Such a model satisfies Peano arithmetic and every other sentence true in $\nat$; the next lesson gives non-standard models of Peano arithmetic in which a $\Sigma_1$ sentence false in $\nat$ holds.

## Exercises

::::exercise{#ex-pam-predecessors difficulty=2 objective="Use the axiom of differences and the standard part to show that non-standard elements have non-standard predecessors."}
Let $M$ be a model of $\mathrm{PA}^-$ and $a \in M$ a non-standard element. Show that for every $k \in \nat$ there is a unique $b \in M$ with $b + \bar k = a$, written $a - k$, and that it is non-standard. Deduce that $M$ has no least non-standard element.

:::solution
Since $a$ is non-standard, $\bar k < a$ by :ref{#prop-standard-part} and trichotomy. Axiom 5 gives $z$ with $\bar k + z + 1 = a$, so $b = z + 1$ satisfies $b + \bar k = a$. If $b + \bar k = b' + \bar k$ and $b < b'$, then $b + \bar k < b' + \bar k$ by item 4, a contradiction; so $b = b'$ by trichotomy. If $b$ were a numeral $\bar m$, then $a = \overline{m + k}$ by :ref{#lem-pam-basic}, a contradiction. For $k = 1$, $a - 1$ is a non-standard element, and $a - 1 < a$ by axiom 4, since $a = (a - 1) + 1$ and $0 < 1$; so no non-standard element is least.
:::
::::

## Notes and references

The axiomatization of $\mathrm{PA}^-$ is the one of Kaye's book (Chapter 2), used in Wong's lecture notes (Lecture 2). The construction of a non-standard model of true arithmetic by compactness is in Hájek and Pudlák, Preliminaries, 0.29.

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 1 and 2.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Preliminaries (b) and Chapter I, Section 1(a).
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, Chapter 2.

:::::exercises
::::exercise{#ex-pam-cancellation difficulty=1 objective="Derive the cancellation and monotonicity laws of addition and multiplication from the axioms of $\mathrm{PA}^-$."}
Show that $\mathrm{PA}^-$ proves:

1. $x + z = y + z \rightarrow x = y$, and $0 < z \wedge x \cdot z = y \cdot z \rightarrow x = y$;
2. $x \leq x + y$;
3. $x \leq y \wedge x' \leq y' \rightarrow x + x' \leq y + y'$, and $x \leq y \wedge x' \leq y' \rightarrow x \cdot x' \leq y \cdot y'$.

:::solution
The relation $\leq$ is transitive, by the transitivity of $<$ and the substitution of equals.

1. Suppose $x + z = y + z$ and $x \neq y$. By trichotomy, $x < y$ or $y < x$; by axiom 4, $x + z < y + z$ or $y + z < x + z$, and in both cases $x + z < x + z$, which contradicts irreflexivity. The second law is proved in the same way with the second part of axiom 4, which requires $0 < z$.

2. By axiom 6, $0 \leq y$. If $y = 0$, then $x + y = x$ by axiom 2. If $0 < y$, axiom 4 gives $0 + x < y + x$, that is $x < x + y$, by commutativity and $x + 0 = x$.

3. For addition, $x + x' \leq y + x'$ by axiom 4 if $x < y$, and trivially if $x = y$; likewise $y + x' \leq y + y'$, using commutativity; and $\leq$ is transitive. For multiplication, if $x' = 0$, then $x \cdot x' = 0 \leq y \cdot y'$ by axioms 2 and 6. If $0 < x'$, then $x \cdot x' \leq y \cdot x'$ by axiom 4 (or equality if $x = y$). If $y = 0$, then $y \cdot x' = 0 = y \cdot y'$; if $0 < y$, then $x' \cdot y \leq y' \cdot y$ by axiom 4 (or equality). By transitivity, $x \cdot x' \leq y \cdot y'$.
:::
::::

::::exercise[The irrationality of √2]{#ex-pam-sqrt2 difficulty=2 objective="Build a discretely ordered ring whose non-negative part refutes a universal sentence true in $\nat$."}
Let $R$ be the set of polynomials $p \in \mathbb R[X]$ whose constant term is an integer, ordered by declaring $p$ positive when its leading coefficient is positive. Show that $R$ is a discretely ordered ring, and that its non-negative part $R^+$ is a model of $\mathrm{PA}^-$ in which the universal sentence
$$
\forall x\ \forall y\ \big(x \cdot x = (1 + 1) \cdot y \cdot y \rightarrow x = 0\big),
$$
true in $\nat$, fails. Deduce that $\mathrm{PA}^-$ does not prove that $\sqrt 2$ is irrational in this form.

:::solution
The constant term of a sum or a product of polynomials is the sum or the product of their constant terms, so $R$ is a subring of $\mathbb R[X]$ containing $\mathbb Z$. On $\mathbb R[X]$, the positive polynomials, those with a positive leading coefficient, are closed under addition (if the degrees differ, the leading coefficient of the sum is that of the summand of larger degree; if they are equal, it is the sum of two positive numbers) and under multiplication (the leading coefficient of a product is the product of the leading coefficients), and every non-zero $p$ satisfies exactly one of $p > 0$ and $-p > 0$. Setting $p < q$ when $q - p$ is positive gives a linear order compatible with addition and with multiplication by positive elements; it restricts to $R$.

The order of $R$ is discrete. Let $0 < p < 1$ in $R$. If $p$ has degree at least $1$, then $1 - p$ has the leading coefficient of $-p$, which is negative, so $p > 1$, a contradiction. So $p$ is a constant, equal to its constant term, an integer strictly between $0$ and $1$: impossible.

As in :ref{#ex-zx-plus}, the axioms of items 1–4 and 6 of :ref{#def-pa-minus} hold in the non-negative part of every discretely ordered ring, and axiom 5 holds by discreteness: if $p < q$, then $q - p \geq 1$, so $z = q - p - 1$ is non-negative and $p + z + 1 = q$. So $R^+ \models \mathrm{PA}^-$.

The polynomials $x = \sqrt 2\, X$ and $y = X$ belong to $R^+$: their constant term is $0$ and their leading coefficient is positive. Then $x \neq 0$ and $x \cdot x = 2X^2 = (1 + 1) \cdot y \cdot y$, so the sentence fails in $R^+$. It is true in $\nat$, since $\sqrt 2$ is irrational. By the soundness of first-order logic, $\mathrm{PA}^-$ does not prove it. Bounded induction proves it, as shown in the further exercises of :ref{to="bounded-induction"}.
:::
::::

::::exercise{#ex-nonstandard-prime difficulty=1 objective="Transfer sentences true in $\nat$ to a non-standard model of true arithmetic to find non-standard elements with given properties."}
Let $M$ be a non-standard model of $\mathrm{Th}(\nat)$. Show that $M$ has a non-standard element satisfying the formula "$x$ is prime" of :ref{#ex-delta0-examples}, and a non-standard element divisible by every standard positive number.

:::solution
Write $\pi(p)$ for the formula $1 < p \wedge \forall y < p\ \forall z < p\ \neg (y \cdot z = p)$. Euclid's theorem gives the sentence $\forall x\ \exists p\ (x < p \wedge \pi(p))$, true in $\nat$, hence in $M$. Applied to a non-standard $a \in M$, it gives $p > a$ with $M \models \pi(p)$, and $p$ is non-standard, since the standard part is an initial segment (:ref{#prop-standard-part}).

The sentence $\forall x\ \exists y\ \big(0 < y \wedge \forall i < x + 1\ (0 < i \rightarrow \exists q < y + 1\ (q \cdot i = y))\big)$ is true in $\nat$, with $y = x!$ (and $y = 1$ for $x = 0$), hence in $M$. Applied to a non-standard $a$, it gives $y > 0$ divisible by every $i \leq a$, in particular by every standard $k \geq 1$, since $\bar k < a$. If $q \cdot \bar k = y$ with $y > 0$, then $q \geq 1$, so $y \geq \bar k$ by :ref{#ex-pam-cancellation}; as this holds for every $k$, $y$ is non-standard.
:::
::::

::::exercise{#ex-delta0-definitions difficulty=1 objective="Write bounded definitions of elementary relations of number theory, choosing the bounds of the quantifiers."}
Give $\Delta_0$ formulas that define in $\nat$: (a) $x$ divides $y$; (b) $x$ is a power of $2$; (c) $x$ and $y$ are coprime; (d) $y > 0$ and $z$ is the remainder of $x$ modulo $y$.

:::solution
(a) $x \mid y$ is $\exists q < y + 1\ (q \cdot x = y)$. If $y > 0$ and $q x = y$, then $x \geq 1$ and $q \leq y$; if $y = 0$, then $q = 0$ is a witness. For $x = 0$ the formula holds exactly when $y = 0$, as it should.

(b) $0 < x \wedge \forall d < x + 1\ \big(1 < d \wedge d \mid x \rightarrow \exists u < d\ (d = u + u)\big)$, with $d \mid x$ as in (a). If $x = 2^k$, every divisor $d > 1$ of $x$ is a power $2^j$ with $j \geq 1$, hence even. If $x > 0$ is not a power of $2$, it has an odd prime divisor $p \leq x$, and the formula fails at $d = p$.

(c) $\forall d < x + y + 1\ (d \mid x \wedge d \mid y \rightarrow d = 1)$. If $x$ and $y$ are not both $0$, every common divisor is at most $\max(x, y) \leq x + y$, and $d = 0$ is not a common divisor; so the formula says that $1$ is the only common divisor. If $x = y = 0$, the formula fails at $d = 0$, and indeed $0$ and $0$ are not coprime.

(d) $0 < y \wedge z < y \wedge \exists q < x + 1\ (x = q \cdot y + z)$, since the quotient is at most $x$.
:::
::::
:::::
