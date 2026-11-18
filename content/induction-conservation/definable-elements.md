---
title: Models of definable elements
summary: Σₙ-elementary substructures; the Σₙ-definable elements of a model of Peano arithmetic form a Σₙ-elementary substructure, by a version of the Tarski–Vaught test; it may contain non-standard elements.
duration: 35
prerequisites: [collection-induction]
---

To show that a scheme does not prove another, one needs a model of the first in which the second fails. Every ω-model satisfies all the schemes, and so does every model of Peano arithmetic; the model must therefore be non-standard, and built so that some instances of induction fail. The method of this lesson and the next is to start from a model $M$ of Peano arithmetic and keep only the elements that are definable by formulas of bounded complexity. Removing elements does not change the truth of simple formulas, so the simple instances of induction survive; the next lesson shows that collection one level up fails.

This lesson builds the tool: the definable elements of $M$ form a substructure in which formulas of bounded complexity have the same truth value as in $M$. The technique, models of definable elements, is a basic tool of the model theory of arithmetic; its key lemma is a version of the **Tarski–Vaught test** for elementary substructures.

## Arithmetic without sets

In this lesson, the next one and the lesson on first-order parts, $\mathcal L_1$ is the language $\mathcal L_2$ without set variables and without $\in$, and the structures are $\mathcal L_1$-structures, consisting of numbers only. **Peano arithmetic** $\mathrm{PA}$ consists of the basic axioms and the induction scheme for all formulas of $\mathcal L_1$; $\mathrm I\Sigma_n$ and $\mathrm B\Sigma_n$ are the schemes of the first lesson restricted to formulas of $\mathcal L_1$, which may contain number parameters only. The results of the previous lessons apply to these theories, with the same proofs; in particular, a model of $\mathrm{PA}$ satisfies $\mathrm B\Sigma_n$ and the least number principles for every $n$, and :ref{#lem-collection-closure} applies in it at every level.

Besides :ref{#lem-collection-closure}, which holds in models of collection, we use operations on prenex formulas that are valid in **every** structure, because they are logical equivalences obtained by renaming bound variables and moving quantifiers:

- a conjunction or disjunction of two $\Sigma_k$ formulas is equivalent to a $\Sigma_k$ formula, and similarly for $\Pi_k$;
- a conjunction or disjunction of a $\Sigma_k$ formula and a $\Pi_k$ formula is equivalent to a $\Sigma_{k+1}$ formula, and to a $\Pi_{k+1}$ formula;
- the negation of a $\Sigma_k$ formula is equivalent to a $\Pi_k$ formula, and conversely;
- a $\Sigma_k$ or $\Pi_k$ formula is equivalent to a $\Sigma_m$ and to a $\Pi_m$ formula for every $m > k$, by adding vacuous quantifiers.

We use them without comment. We also use that every bounded sentence true in $\nat$ holds in every model of the basic axioms. This is proved by induction on the sentence: closed terms evaluate to numerals by the recursion equations for $+$ and $\cdot$, and a bounded quantifier $\forall x < k$ reduces to the $k$ cases $x = 0, \dots, x = k - 1$ by the two axioms on $<$. The same two axioms show that the standard numbers form an initial segment of every model of the basic axioms (:ref{to="second-order-arithmetic/nonstandard-models"}).

## Elementary substructures

:::definition{#def-sigma-elementary}
Let $M$ be an $\mathcal L_1$-structure. A **substructure** of $M$ is a subset $K \subseteq M$ containing $0$ and $1$ and closed under $+$ and $\cdot$, with the restricted operations and order. For $n \geq 0$, $K$ is a **$\Sigma_n$-elementary substructure**, written $K \prec_{\Sigma_n} M$, if for every $\Sigma_n$ formula $\theta(\bar x)$ and every tuple $\bar a$ of elements of $K$, $K \models \theta(\bar a)$ if and only if $M \models \theta(\bar a)$.
:::

Taking negations, the same then holds for $\Pi_n$ formulas. If $K \prec_{\Sigma_n} M$, every $\Pi_{n+1}$ sentence $\forall \bar x\, \sigma(\bar x)$ true in $M$, with $\sigma \in \Sigma_n$, is true in $K$: for $\bar a$ in $K$, $M \models \sigma(\bar a)$, so $K \models \sigma(\bar a)$. In particular, $K$ satisfies the basic axioms if $M$ does and $n \geq 1$, since they are $\Pi_1$ sentences.

:::example{#ex-standard-part-elementary}
Let $M$ be a non-standard model of the basic axioms, and $\nat \subseteq M$ its standard part. It is a substructure, and a $\Sigma_0$-elementary one, since bounded formulas with standard parameters are bounded sentences, and their truth in $M$ and in $\nat$ agree by the remark above. It is not $\Sigma_1$-elementary in general: the model $M$ of :ref{#lem-nonstandard-definable} below satisfies a $\Sigma_1$ sentence $\exists x\, \neg \delta(x)$, with $\delta$ bounded, that is false in $\nat$. The witnesses of $\Sigma_1$ sentences of $M$ may all be non-standard; a $\Sigma_1$-elementary substructure must contain some of them.
:::

## Definable elements

:::definition{#def-definable-elements}
Let $M$ be a model of $\mathrm{PA}$ and $n \geq 1$. An element $a \in M$ is **$\Sigma_n$-definable** in $M$ if there is a $\Sigma_n$ formula $\varphi(x)$ of $\mathcal L_1$, without parameters, such that $a$ is the only element of $M$ satisfying $\varphi$. The set of these elements is written $K_n(M)$.
:::

Every standard number $k$ belongs to $K_n(M)$, defined by the bounded formula $x = 1 + \cdots + 1$ with $k$ terms (or $x = 0$). Since there are countably many formulas, $K_n(M)$ is countable, and $K_n(M) \subseteq K_{n+1}(M)$. If $M = \nat$, then $K_n(\nat) = \nat$. In a non-standard model, $K_n(M)$ may contain non-standard elements:

:::lemma{#lem-nonstandard-definable}
There is a countable model $M$ of $\mathrm{PA}$ with a non-standard element that is defined in $M$ by a bounded formula.
:::

:::proof{of=lem-nonstandard-definable}
By Gödel's first incompleteness theorem, applied to the computably axiomatized theory $\mathrm{PA}$, which is true in $\nat$, there is a $\Pi_1$ sentence $\forall x\, \delta(x)$, with $\delta$ bounded, that is true in $\nat$ and not provable in $\mathrm{PA}$; the consistency of $\mathrm{PA}$ is one. So $\mathrm{PA} + \exists x\, \neg \delta(x)$ is consistent, and has a countable model $M$. By the least number principle in $M$, there is a least $a$ with $M \models \neg \delta(a)$; it is the only element satisfying the bounded formula $\neg \delta(x) \wedge \forall y < x\ \delta(y)$. If $a$ were a standard number $k$, then $\neg \delta(k)$, a bounded sentence false in $\nat$, would hold in $M$, while its negation $\delta(k)$, true in $\nat$, holds in $M$ by the remark above. So $a$ is non-standard.
:::

:::lemma{#lem-kn-elementary}
Let $M$ be a model of $\mathrm{PA}$, $n \geq 1$ and $K = K_n(M)$.

1. If $\psi(x, \bar y)$ is $\Sigma_n$, $\bar b$ is a tuple of $K$, and $a$ is the only element of $M$ with $M \models \psi(a, \bar b)$, then $a \in K$.
2. If $\exists x\, \varphi(x, \bar y)$ is $\Sigma_k$ for some $k \leq n$, $\bar b$ is a tuple of $K$, and $M \models \exists x\, \varphi(x, \bar b)$, then $M \models \varphi(a, \bar b)$ for some $a \in K$.
3. $K$ is a substructure of $M$, and $K \prec_{\Sigma_n} M$.
:::

Item 2 is the heart of the proof: a $\Sigma_n$ formula true in $M$ has a witness in $K$, namely its least witness, which is definable. Item 3 then follows by the argument of the Tarski–Vaught test, one quantifier at a time.

:::proof{of=lem-kn-elementary}
1. Let $\varphi_i(x)$ be a $\Sigma_n$ formula without parameters defining $b_i$. Then $a$ is the only element satisfying $\exists \bar y\, (\bigwedge_i \varphi_i(y_i) \wedge \psi(x, \bar y))$, since the $y_i$ are forced to be the $b_i$. This formula has no parameters and is equivalent to a $\Sigma_n$ formula, so $a \in K$.

2. We may assume $k \geq 1$. Write $\exists x\, \varphi$ as $\exists x\, \exists \bar u\, \psi(x, \bar u, \bar y)$ with $\psi \in \Pi_{k-1}$ (the block $\bar u$ may be empty). With an iterated pairing function, let
$$
\chi(p, \bar y) \equiv \exists x \leq p\ \exists \bar u \leq p\ (p = \langle x, \bar u \rangle \wedge \psi(x, \bar u, \bar y)).
$$
For $k = 1$ it is bounded; for $k \geq 2$, it is equivalent in $M$ to a $\Pi_{k-1}$ formula by :ref{#lem-collection-closure}, since $M$ satisfies $\mathrm B\Sigma_{k-1}$. Since $M \models \exists p\ \chi(p, \bar b)$, the least number principle in $M$ gives a least such $p$. It is the only element satisfying $\chi(p, \bar b) \wedge \forall q < p\ \neg \chi(q, \bar b)$, and the second conjunct is equivalent in $M$ to a $\Sigma_{k-1}$ formula, by :ref{#lem-collection-closure} again (or is bounded if $k = 1$). So $p$ is defined in $M$ by a formula equivalent to a $\Sigma_k$ formula, hence to a $\Sigma_n$ formula, with parameters $\bar b$; by item 1, $p \in K$. The first component $a$ of $p$ is the only element satisfying the bounded formula $\exists \bar u \leq p\ (p = \langle x, \bar u \rangle)$, so $a \in K$ by item 1, and $M \models \varphi(a, \bar b)$, the components $\bar u$ of $p$ being witnesses.

3. The numbers $0$ and $1$ are standard, so they belong to $K$. If $a, b \in K$, then $a + b$ is the only element $x$ with $x = a + b$, a bounded formula, so $a + b \in K$ by item 1, and similarly for $a \cdot b$.

   For elementarity, we show that $K \models \theta(\bar a) \leftrightarrow M \models \theta(\bar a)$ for every formula $\theta$ that is bounded, or $\Sigma_k$ or $\Pi_k$ for some $k \leq n$, and every tuple $\bar a$ of $K$. The subformulas of such a formula are again of this kind, writing $\exists x < t\ \psi$ as $\exists x\, (x < t \wedge \psi)$ and $\forall x < t\ \psi$ as $\forall x\, (x < t \rightarrow \psi)$. We proceed by induction on $\theta$. Atomic formulas have the same truth value in $K$ and $M$, since $K$ is a substructure, and the induction is immediate for the connectives.

   Let $\theta = \exists x\, \psi$; it is $\Sigma_k$ for some $k \leq n$ (a bounded existential quantifier gives a $\Sigma_1$ formula). If $K \models \theta(\bar a)$, a witness $c \in K$ satisfies $K \models \psi(c, \bar a)$, hence $M \models \psi(c, \bar a)$ by induction, and $M \models \theta(\bar a)$. If $M \models \theta(\bar a)$, item 2 gives $c \in K$ with $M \models \psi(c, \bar a)$, so $K \models \psi(c, \bar a)$ by induction, and $K \models \theta(\bar a)$.

   Let $\theta = \forall x\, \psi$, which is $\Pi_k$ for some $k \leq n$. If $M \models \theta(\bar a)$, then $M \models \psi(c, \bar a)$ for every $c \in K$, so $K \models \psi(c, \bar a)$ by induction, and $K \models \theta(\bar a)$. If $M \not\models \theta(\bar a)$, then $M \models \exists x\, \neg \psi(x, \bar a)$, and $\exists x\, \neg \psi$ is equivalent to a $\Sigma_k$ formula; item 2 gives $c \in K$ with $M \models \neg \psi(c, \bar a)$, so $K \models \neg \psi(c, \bar a)$ by induction, and $K \not\models \theta(\bar a)$.
:::

The only property of $M$ used is that every $\Sigma_n$ formula true in $M$ has a definable witness, given by the least number principle and collection in $M$; this is why $M$ is a model of $\mathrm{PA}$.

:::quiz[definable elements]
In item 2 of :ref{#lem-kn-elementary}, why does the proof take the least $p$ coding a witness, rather than any witness?

- [x] Item 1 applies only to an element that is the unique solution of a formula; the least $p$ is uniquely defined, by $\chi(p, \bar b) \wedge \forall q < p\ \neg \chi(q, \bar b)$.
- [ ] Because the least witness is standard.

  It need not be standard; it is definable, which is what membership in $K$ requires.
- [ ] To make $\chi$ bounded.

  $\chi$ is bounded by $p$ by construction; minimality is needed for uniqueness.

---

Where is collection used in item 2?

- [x] To show that $\chi$ and the formula "$\forall q < p\ \neg \chi(q, \bar b)$" are equivalent in $M$ to formulas of the right complexity, so that $p$ is defined by a $\Sigma_n$ formula.
- [ ] To show that the least $p$ exists.

  Existence of a least element comes from the least number principle, a form of induction.
- [ ] To show that $0$ and $1$ are in $K$.

  These are standard numbers, definable without collection.
:::


::::exercise{#ex-k1-nonstandard difficulty=1 objective="Use the $\Sigma_1$-elementarity of $K_1(M)$ to relate its non-standard elements to the false $\Sigma_1$ sentences true in $M$."}
Let $M$ be a model of $\mathrm{PA}$ in which some $\Sigma_1$ sentence false in $\nat$ is true. Show that $K_1(M)$ contains a non-standard element.

:::solution
Suppose that every element of $K_1(M)$ is standard; since every standard number is definable, $K_1(M) = \nat$. By :ref{#lem-kn-elementary}, $K_1(M) \prec_{\Sigma_1} M$, so every $\Sigma_1$ sentence true in $M$ is true in $\nat$, contrary to the hypothesis. This gives a second proof of :ref{#lem-nonstandard-definable}, for $\Sigma_1$-definable elements.
:::
::::

## Notes and references

Models of definable elements are the method of Paris and Kirby (1978) for the separations of the next lesson. Elementary substructures and the Tarski–Vaught test are standard in model theory; for arithmetic, see Kaye, chapter *Subsystems of Peano arithmetic*, and Hájek and Pudlák, Chapter IV. The presentation follows Dzhafarov and Mummert, Section 6.3.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 6.3.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, chapter *Subsystems of Peano arithmetic*.

:::::exercises
::::exercise{#ex-kn-closure difficulty=1 objective="Check closure properties of the model of definable elements with the first item of the main lemma."}
Let $M$ be a model of $\mathrm{PA}$, $n \geq 1$ and $K = K_n(M)$. Show:

1. if $a \in K$, then $\lfloor a / 2 \rfloor$ and the least prime number greater than $a$ belong to $K$;
2. if $K$ contains a non-standard element, the set of non-standard elements of $K$ has no least element;
3. $K$ satisfies every $\Pi_{n+1}$ sentence true in $M$, for instance "for every $x$ there is a prime number greater than $x$".

:::solution
1. The number $\lfloor a / 2 \rfloor$ is the only $x$ with $x + x = a \vee x + x + 1 = a$, a bounded formula with parameter $a$. Being prime is expressed by the bounded formula $\pi(p) \equiv 1 < p \wedge \forall u < p\ \forall v < p\ u \cdot v \neq p$. $\mathrm{PA}$ proves Euclid's theorem that there is a prime above every number, so $M$ has a prime above $a$, and by the least number principle in $M$ a least one, which is the only $p$ with $p > a \wedge \pi(p) \wedge \forall q < p\ (q > a \rightarrow \neg \pi(q))$. In both cases item 1 of :ref{#lem-kn-elementary} gives the result.
2. Let $b \in K$ be non-standard. Then $b \geq 1$, so $\lfloor b / 2 \rfloor < b$, and $\lfloor b / 2 \rfloor \in K$ by 1. If $\lfloor b / 2 \rfloor$ were a standard number $k$, then $b \leq 2k + 1$ would be standard. So below every non-standard element of $K$ there is another one.
3. By :ref{#lem-kn-elementary}, $K \prec_{\Sigma_n} M$, and the remark after :ref{#def-sigma-elementary} shows that $\Pi_{n+1}$ sentences go down from $M$ to $K$. The sentence $\forall x\ \exists p\ (p > x \wedge \pi(p))$ is $\Pi_2$, hence $\Pi_{n+1}$ up to vacuous quantifiers, and true in $M$.
:::
::::

::::exercise{#ex-kn-standard difficulty=2 objective="Characterize the models of $\mathrm{PA}$ whose $\Sigma_n$-definable elements are all standard, through the $\Pi_n$ sentences they satisfy."}
Let $M$ be a model of $\mathrm{PA}$ and $n \geq 1$. Show that $K_n(M)$ consists of the standard numbers if and only if $M$ satisfies every $\Pi_n$ sentence of $\mathcal L_1$ that is true in $\nat$.

:::solution
We first note that if $M$ satisfies every $\Pi_n$ sentence true in $\nat$, then it satisfies every $\Sigma_n$ sentence true in $\nat$. Such a sentence is $\exists y\, \psi(y)$, contracting the first block, with $\psi \in \Pi_{n-1}$ (bounded if $n = 1$); if $\nat \models \psi(k)$, then $\psi(k)$ is a $\Pi_{n-1}$ sentence, hence a $\Pi_n$ sentence after adding vacuous quantifiers, true in $\nat$, so $M \models \psi(k)$.

($\Leftarrow$) Let $a \in K_n(M)$, defined by a $\Sigma_n$ formula $\varphi(x)$ without parameters. The $\Sigma_n$ sentence $\exists x\, \varphi(x)$ holds in $M$. If it were false in $\nat$, its negation, equivalent to a $\Pi_n$ sentence, would be true in $\nat$, hence in $M$: a contradiction. So $\nat \models \varphi(k)$ for some $k \in \nat$. The $\Sigma_n$ sentence $\varphi(k)$ is true in $\nat$, so $M \models \varphi(k)$ by the first paragraph, and $a = k$ since $a$ is the only element satisfying $\varphi$. So $K_n(M) \subseteq \nat$; the converse inclusion always holds.

($\Rightarrow$) If $K_n(M)$ is the set of standard numbers, then, as a structure, it is $\nat$, and $\nat \prec_{\Sigma_n} M$ by :ref{#lem-kn-elementary}. Let $\sigma$ be a $\Pi_n$ sentence true in $\nat$. If $M \models \neg \sigma$, a $\Sigma_n$ sentence up to equivalence, then $\nat \models \neg \sigma$ by elementarity: a contradiction.

For $n = 1$, the direction ($\Rightarrow$) is the contrapositive of :ref{#ex-k1-nonstandard}.
:::
::::

::::exercise{#ex-kn-least difficulty=1 objective="Show that the model of definable elements is the least $\Sigma_n$-elementary substructure."}
Let $M$ be a model of $\mathrm{PA}$ and $n \geq 1$. Show that every substructure $K \prec_{\Sigma_n} M$ contains $K_n(M)$. With :ref{#lem-kn-elementary}, $K_n(M)$ is therefore the least $\Sigma_n$-elementary substructure of $M$.

:::solution
Let $a \in K_n(M)$, defined in $M$ by a $\Sigma_n$ formula $\varphi(x)$ without parameters. The sentence $\exists x\, \varphi(x)$ is equivalent to a $\Sigma_n$ sentence, since $n \geq 1$, and holds in $M$, so it holds in $K$ by elementarity: there is $c \in K$ with $K \models \varphi(c)$. By elementarity again, $M \models \varphi(c)$, and $c = a$ since $a$ is the only element of $M$ satisfying $\varphi$. So $a \in K$.
:::
::::
:::::
