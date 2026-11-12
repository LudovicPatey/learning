---
title: The base theory PA⁻ and non-standard models
summary: The theory PA⁻ of the non-negative parts of discretely ordered rings; the standard numbers form an initial segment of every model; bounded, Σₙ and Πₙ formulas in arbitrary models; bounded formulas are absolute between a model and its end extensions, and PA⁻ proves every true Σ₁ sentence; first examples of non-standard models.
duration: 50
prerequisites: [arithmetic-hierarchy/arithmetic-definability]
---

This course studies theories of arithmetic and their **non-standard models**, and the fragments of Peano arithmetic obtained by restricting induction to formulas of bounded complexity. The track assumes first-order logic: the completeness, compactness and Löwenheim–Skolem theorems, and Gödel's incompleteness theorems. This lesson fixes an algebraic base theory and proves that the standard numbers sit at the bottom of every model, and that bounded formulas have the same meaning in a model and in its extensions at the top.

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

2. By induction on $k$. For $k = 0$, $\neg (x < 0)$ follows from $0 \leq x$ and the order axioms. Assume the statement for $k$, and let $x < \overline{k + 1} = \bar k + 1$. If $x < \bar k$, the induction hypothesis applies. Otherwise $x = \bar k$ or $\bar k < x$; in the second case $\bar k + 1 \leq x$ by item 1, which contradicts $x < \bar k + 1$. Conversely, each $\bar i$ with $i \leq k$ is less than $\overline{k+1}$ by item 3.
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

Blocks may be empty, so a $\Sigma_n$ or $\Pi_n$ formula is both $\Sigma_m$ and $\Pi_m$ for every $m > n$. Up to logical equivalence, conjunctions and disjunctions of $\Sigma_n$ formulas are $\Sigma_n$, negations of $\Sigma_n$ formulas are $\Pi_n$, and $\exists x < t$ in front of a $\Sigma_n$ formula, and $\forall x < t$ in front of a $\Pi_n$ formula, give again a $\Sigma_n$, respectively $\Pi_n$, formula, since the bounded quantifier merges with the first block and its guard $x < t$ moves into the matrix. The remaining case, $\forall x < t$ in front of a $\Sigma_n$ formula, is the subject of the collection schemes of lesson 4; it is not a logical equivalence.

:::example{#ex-delta0-examples}
1. "$x$ is prime" is defined in $\nat$ by the $\Delta_0$ formula $1 < x \wedge \forall y < x\ \forall z < x\ \neg(y \cdot z = x)$.
2. Every Δ₀ formula defines a primitive recursive relation in $\nat$ (:ref{#lem-bounded-computable}), and a relation on $\nat$ is $\Sigma_n$-definable if and only if it is $\Sigma^0_n$ in the sense of computability (:ref{#thm-definable-arithmetic}, after merging the quantifiers of the inner $\Sigma_1$ or $\Pi_1$ formula with the last block).
:::

## End extensions and bounded formulas

:::definition{#def-end-extension}
Let $M$ and $N$ be $\mathcal L_A$-structures. $N$ is an **end extension** of $M$, written $M \subseteq_e N$, if $M$ is a substructure of $N$ and an initial segment of it: if $a \in M$, $b \in N$ and $N \models b < a$, then $b \in M$.
:::

By :ref{#prop-standard-part}, every model of $\mathrm{PA}^-$ is an end extension of $\nat$. End extensions do not change the truth of bounded formulas: for a bounded quantifier $\exists y < t(\bar a)$ with $\bar a$ in $M$, the value $t(\bar a)$ and all the candidates below it lie in $M$.

:::figure[A bounded quantifier in an end extension. The value $t(\bar a)$ of a term at parameters $\bar a$ in $M$ lies in $M$, and so do all the elements below it. The new elements of $N$ lie above $M$ and are never inspected by $\exists y < t(\bar a)$ or $\forall y < t(\bar a)$.]
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="An end extension: the model M is an initial segment of N; the candidates y below t(a) for a bounded quantifier with parameters a in M all lie in M"><line x1="20" y1="70" x2="580" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="24" cy="70" r="3.5" class="accent-fill"/><text x="24" y="58" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="110" cy="70" r="3.5" class="accent-fill"/><text x="110.0" y="58.0" text-anchor="middle" class="math" font-size="14">a</text><circle cx="270" cy="70" r="3.5" class="accent-fill"/><text x="270.0" y="58.0" text-anchor="middle" class="math" font-size="14">t(a)</text><circle cx="140" cy="70" r="2.5" class="node"/><circle cx="170" cy="70" r="2.5" class="node"/><circle cx="200" cy="70" r="2.5" class="node"/><circle cx="230" cy="70" r="2.5" class="node"/><circle cx="255" cy="70" r="2.5" class="node"/><path d="M130,46 L130,40 L262,40 L262,46" class="muted-stroke" stroke-width="1.2"/><text x="196.0" y="30" text-anchor="middle" class="label">candidates y &lt; t(a): all in M</text><line x1="340" y1="48" x2="340" y2="92" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><circle cx="420" cy="70" r="3.5" class="node"/><circle cx="470" cy="70" r="3.5" class="node"/><circle cx="520" cy="70" r="3.5" class="node"/><path d="M380,46 L380,40 L560,40 L560,46" class="muted-stroke" stroke-width="1.2"/><text x="470.0" y="30" text-anchor="middle" class="label">new elements of N</text><path d="M22,86 L22,92 L334,92 L334,86" class="muted-stroke" stroke-width="1.2"/><text x="178.0" y="110" text-anchor="middle" class="label">M: an initial segment of N</text><path d="M22,120 L22,126 L578,126 L578,120" class="muted-stroke" stroke-width="1.2"/><text x="300.0" y="144" text-anchor="middle" class="label">N</text></svg>
:::

:::lemma[Absoluteness of bounded formulas]{#lem-delta0-absolute}
Let $M \subseteq_e N$. For every $\Delta_0$ formula $\delta(\bar x)$ and every tuple $\bar a$ of elements of $M$, $M \models \delta(\bar a)$ if and only if $N \models \delta(\bar a)$.
:::

:::proof{of=lem-delta0-absolute}
By induction on $\delta$. Since $M$ is a substructure of $N$, every term has the same value at $\bar a$ in $M$ and in $N$, and atomic formulas have the same truth value. The induction steps for $\neg$, $\wedge$ and $\vee$ are immediate. Let $\delta = \exists y < t(\bar x)\ \psi(y, \bar x)$, and let $c = t(\bar a)$, an element of $M$. If $M \models \delta(\bar a)$, some $b \in M$ with $b < c$ satisfies $M \models \psi(b, \bar a)$, hence $N \models \psi(b, \bar a)$ by the induction hypothesis, and $N \models \delta(\bar a)$. Conversely, if $N \models \psi(b, \bar a)$ for some $b \in N$ with $b < c$, then $b \in M$ since $M$ is an initial segment of $N$, and $M \models \psi(b, \bar a)$ by the induction hypothesis. The bounded universal quantifier is the negation of a bounded existential one.
:::

:::corollary{#cor-sigma1-upward}
Let $M \subseteq_e N$ and $\bar a \in M$. If $\sigma(\bar x)$ is $\Sigma_1$ and $M \models \sigma(\bar a)$, then $N \models \sigma(\bar a)$. If $\pi(\bar x)$ is $\Pi_1$ and $N \models \pi(\bar a)$, then $M \models \pi(\bar a)$.
:::

:::proof{of=cor-sigma1-upward}
Write $\sigma = \exists \bar y\ \delta(\bar x, \bar y)$ with $\delta$ bounded. Witnesses $\bar b \in M$ with $M \models \delta(\bar a, \bar b)$ satisfy $N \models \delta(\bar a, \bar b)$ by :ref{#lem-delta0-absolute}. The statement for $\Pi_1$ formulas is the contrapositive, applied to the negation.
:::

:::quiz[absoluteness of bounded formulas]
In the proof of :ref{#lem-delta0-absolute}, where is it used that $M$ is an initial segment of $N$, and not only a substructure?

- [x] In the case $\exists y < t$, to know that a witness $b \in N$ below $t(\bar a)$ belongs to $M$.
- [ ] To know that $t(\bar a)$ has the same value in $M$ and in $N$.

  This only uses that $M$ is a substructure: the operations of $M$ are those of $N$ restricted.
- [ ] In the case of atomic formulas $s < t$.

  The order of $M$ is the restriction of the order of $N$; no initial segment condition is needed.
:::

Applied to $\nat \subseteq_e M$, the corollary gives the first theorem of the subject.

:::theorem[Σ₁-completeness]{#thm-sigma1-complete}
Every $\Sigma_1$ sentence true in $\nat$ holds in every model of $\mathrm{PA}^-$, and is therefore provable in $\mathrm{PA}^-$. Every $\Pi_1$ sentence true in some model of $\mathrm{PA}^-$ is true in $\nat$.
:::

:::proof{of=thm-sigma1-complete}
Let $M \models \mathrm{PA}^-$. By :ref{#prop-standard-part}, $\nat$ is isomorphic to an initial segment of $M$ that is a substructure, so we may assume $\nat \subseteq_e M$. A $\Sigma_1$ sentence true in $\nat$ is true in $M$ by :ref{#cor-sigma1-upward}; by the completeness theorem, it is provable in $\mathrm{PA}^-$. The second statement is the contrapositive of the first, applied to the negation of the $\Pi_1$ sentence.
:::

The theorem does not extend to $\Pi_1$ sentences. By Gödel's second incompleteness theorem, the consistency of Peano arithmetic, a $\Pi_1$ sentence true in $\nat$, is not provable even in Peano arithmetic. The example below even gives a model of $\mathrm{PA}^-$ in which the true $\Pi_1$ sentence $\forall x\ \exists y < x + 1\ (x = y + y \vee x = y + y + 1)$, "every number is even or odd", fails.

## Non-standard models

:::example[An algebraic model]{#ex-zx-plus}
Order the polynomial ring $\mathbb Z[X]$ by declaring a polynomial positive when its leading coefficient is positive. It is discrete: if $0 < p < 1$, then $p$ and $1 - p$ have positive leading coefficients, which forces $p$ to be a constant, and there is no integer strictly between $0$ and $1$. Let $\mathbb Z[X]^+$ be the set of non-negative polynomials, with the induced operations and order. The axioms of :ref{#def-pa-minus} hold in it: those of items 1–4 and 6 hold in the non-negative part of every discretely ordered ring, and for item 5, if $p < q$ then $q - p \geq 1$ by discreteness, so $z = q - p - 1$ is non-negative and $p + z + 1 = q$.

So $\mathbb Z[X]^+$ is a model of $\mathrm{PA}^-$. Its standard part consists of the constant polynomials $0, 1, 2, \dots$, and $X$ is non-standard, since $X - k$ is positive for every $k$. The element $X$ is neither $y + y$ nor $y + y + 1$, because every polynomial $y + y$ has even coefficients and $y + y + 1$ has an odd constant term, while $X$ has the coefficient $1$ and the constant term $0$. So the $\Pi_1$ sentence "every number is even or odd" fails in $\mathbb Z[X]^+$, and $\mathrm{PA}^-$ does not prove it. The next lesson shows that induction for bounded formulas proves it.
:::

The compactness theorem gives non-standard models of every theory true in $\nat$. Let $c$ be a new constant. Every finite subset of $\mathrm{Th}(\nat) \cup \{ \bar k < c : k \in \nat \}$ has a model, namely $\nat$ with $c$ interpreted as a large number; by compactness and the Löwenheim–Skolem theorem, the whole set has a countable model $M$, and the interpretation of $c$ is non-standard. A model of Peano arithmetic need not: by Gödel's second incompleteness theorem, $\mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA})$ is consistent, and in any of its models the $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathrm{PA})$, false in $\nat$, holds. By :ref{#thm-sigma1-complete}, such a model is non-standard, and its witnesses of $\neg \mathrm{Con}(\mathrm{PA})$, codes of proofs of a contradiction, are non-standard elements.

## Exercises

::::exercise{difficulty=2}
Let $M$ be a model of $\mathrm{PA}^-$ and $a \in M$ a non-standard element. Show that for every $k \in \nat$ there is a unique $b \in M$ with $b + \bar k = a$, written $a - k$, and that it is non-standard. Deduce that $M$ has no least non-standard element.

:::solution
Since $a$ is non-standard, $\bar k < a$ by :ref{#prop-standard-part} and trichotomy. Axiom 5 gives $z$ with $\bar k + z + 1 = a$, so $b = z + 1$ satisfies $b + \bar k = a$. If $b + \bar k = b' + \bar k$ and $b < b'$, then $b + \bar k < b' + \bar k$ by item 4, a contradiction; so $b = b'$ by trichotomy. If $b$ were a numeral $\bar m$, then $a = \overline{m + k}$ by :ref{#lem-pam-basic}, a contradiction. For $k = 1$, $a - 1$ is a non-standard element below $a$, so no non-standard element is least.
:::
::::


## Notes and references

The axiomatization of $\mathrm{PA}^-$ is the one of Kaye's book, used in Wong's lecture notes (Lecture 2), which also note that $\mathrm{PA}^-$ proves all true $\Sigma_1$ sentences. Hájek and Pudlák prove the $\Sigma_1$-completeness of Robinson's arithmetic $\mathsf Q$ (Theorem I.1.8). The construction of a non-standard model of true arithmetic by compactness is in Hájek and Pudlák, Preliminaries, 0.29.

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 1 and 2.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Preliminaries (b) and Chapter I, Section 1(a).
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, Chapter 2.
