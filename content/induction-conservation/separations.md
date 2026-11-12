---
title: Separating the hierarchy
summary: Σₙ-elementary substructures; the Σₙ₊₁-definable elements of a model of Peano arithmetic form a model of IΣₙ in which Σₙ₊₁ collection fails (Parsons, Paris–Kirby); the hierarchy of induction and collection is strict, and Peano arithmetic is not finitely axiomatizable.
duration: 60
prerequisites: [collection-induction]
---

To show that a scheme does not prove another, one needs a model of the first in which the second fails. Every ω-model satisfies all the schemes, and so does every model of Peano arithmetic; the model must therefore be non-standard, and built so that some instances of induction fail. The method of this lesson is to start from a model $M$ of Peano arithmetic and keep only the elements that are definable by formulas of bounded complexity. Removing elements does not change the truth of simple formulas, so the simple instances of induction survive. But every remaining element now has a name, a formula, whose code is a standard number; all the names lie below any non-standard element $b$, and they name elements far above $b$. A bounded set of names mapped onto an unbounded set of elements is exactly a failure of collection.

The technique, models of definable elements, is a basic tool of the model theory of arithmetic; its key lemma is a version of the **Tarski–Vaught test** for elementary substructures.

## Arithmetic without sets

In this lesson and in the lesson on first-order parts, $\mathcal L_1$ is the language $\mathcal L_2$ without set variables and without $\in$, and the structures are $\mathcal L_1$-structures, consisting of numbers only. **Peano arithmetic** $\mathrm{PA}$ consists of the basic axioms and the induction scheme for all formulas of $\mathcal L_1$; $\mathrm I\Sigma_n$ and $\mathrm B\Sigma_n$ are the schemes of the first lesson restricted to formulas of $\mathcal L_1$, which may contain number parameters only. The results of the previous lessons apply to these theories, with the same proofs; in particular, a model of $\mathrm{PA}$ satisfies $\mathrm B\Sigma_n$ and the least number principles for every $n$, and :ref{#lem-collection-closure} applies in it at every level.

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

## Σₙ induction without Σₙ₊₁ collection

:::theorem[Parsons; Paris, Kirby]{#thm-isigma-not-bsigma}
Let $M$ be a model of $\mathrm{PA}$ with a non-standard element defined by a bounded formula, as in :ref{#lem-nonstandard-definable}, and $n \geq 0$. Then $K_{n+1}(M)$ is a countable model of $\mathrm I\Sigma_n$ in which $\mathrm B\Sigma_{n+1}$ fails. In particular, $\mathrm I\Sigma_n$ proves neither $\mathrm B\Sigma_{n+1}$ nor $\mathrm I\Sigma_{n+1}$.
:::

:::proof{of=thm-isigma-not-bsigma}
Let $K = K_{n+1}(M)$. It is countable, $K \prec_{\Sigma_{n+1}} M$ by :ref{#lem-kn-elementary}, and it satisfies the basic axioms by the remark after :ref{#def-sigma-elementary}. It contains a non-standard element $b$, since an element defined by a bounded formula is $\Sigma_{n+1}$-definable.

*$K$ satisfies $\mathrm I\Sigma_n$.* Let $\varphi(x, \bar y)$ be $\Sigma_n$ (bounded if $n = 0$), $\bar d$ a tuple of $K$, and suppose that $K \models \varphi(0, \bar d) \wedge \forall x\, (\varphi(x, \bar d) \rightarrow \varphi(x + 1, \bar d))$ and $K \models \neg \varphi(c, \bar d)$ for some $c \in K$. By elementarity, $M \models \varphi(0, \bar d)$ and $M \models \neg \varphi(c, \bar d)$. By induction in $M$, $M \models \exists x\, (\varphi(x, \bar d) \wedge \neg \varphi(x + 1, \bar d))$. The formula $\exists x\, (\varphi(x, \bar y) \wedge \neg \varphi(x + 1, \bar y))$ is equivalent to a $\Sigma_{n+1}$ formula, so item 2 of :ref{#lem-kn-elementary} gives $a \in K$ with $M \models \varphi(a, \bar d) \wedge \neg \varphi(a + 1, \bar d)$. By elementarity, this holds in $K$, which contradicts the hypothesis on $\varphi$ in $K$.

*$K$ does not satisfy $\mathrm B\Sigma_{n+1}$.* We admit the existence of partial truth definitions (Kaye, chapter *Satisfaction*; Hájek and Pudlák, Chapter I): there is a $\Sigma_{n+1}$ formula $\mathrm{Sat}(e, x)$ of $\mathcal L_1$ such that, for every $\Sigma_{n+1}$ formula $\varphi(x)$ of $\mathcal L_1$ with one free variable and code $e_\varphi$, $\mathrm{PA}$ proves $\forall x\, (\varphi(x) \leftrightarrow \mathrm{Sat}(e_\varphi, x))$. It is the formalized version of the universal $\Sigma^0_{n+1}$ set. Write $\mathrm{Sat}(e, x)$ as $\exists z\, \psi(e, x, z)$ with $\psi \in \Pi_n$, and let $\upsilon(e, x)$ say that $x$ is the first component of the least pair $\langle x, z \rangle$ satisfying $\psi(e, x, z)$:
$$
\upsilon(e, x) \equiv \exists z\, \bigl(\psi(e, x, z) \wedge \forall p < \langle x, z \rangle\ \neg \exists x' \leq p\ \exists z' \leq p\ (p = \langle x', z' \rangle \wedge \psi(e, x', z'))\bigr).
$$
By :ref{#lem-collection-closure} in $M$, $\upsilon$ is equivalent in $M$ to a $\Sigma_{n+1}$ formula $\upsilon^*$. In $M$:

- for every $e$, there is at most one $x$ with $\upsilon(e, x)$, since the least pair is unique;
- if $a \in K$ is defined by the $\Sigma_{n+1}$ formula $\varphi$, then $a$ is the only $x$ with $\mathrm{Sat}(e_\varphi, x)$, so $M \models \upsilon(e_\varphi, a)$.

Every element $a \leq b$ of $K$ is defined by some formula $\varphi$, so $M \models \upsilon^*(e_\varphi, a)$, hence $K \models \upsilon^*(e_\varphi, a)$ by elementarity; and $e_\varphi$, a standard number, is less than the non-standard $b$. Therefore
$$
K \models \forall x < b + 1\ \exists e < b\ \upsilon^*(e, x).
$$
Suppose that $K$ satisfies $\mathrm B\Sigma_{n+1}$. By :ref{#lem-collection-closure}, there is a $\Sigma_{n+1}$ formula $\sigma(u)$ such that $\mathrm I\Delta_0 + \mathrm B\Sigma_{n+1}$ proves $\forall u\, (\sigma(u) \leftrightarrow \forall x < u + 1\ \exists e < u\ \upsilon^*(e, x))$. This equivalence holds in $K$, which satisfies $\mathrm I\Delta_0$ by the first part, and in $M$. So $K \models \sigma(b)$, hence $M \models \sigma(b)$ by elementarity, and $M \models \forall x \leq b\ \exists e < b\ \upsilon(e, x)$. By the first property of $\upsilon$, the map sending $x \leq b$ to the least $e < b$ with $\upsilon(e, x)$ is injective. It is definable in $M$ and maps $b + 1$ elements into $b$ elements, which contradicts the finite pigeonhole principle, provable in $\mathrm{PA}$ for definable maps by induction on $b$ (Dzhafarov and Mummert, Proposition 6.2.7).

Finally, $\mathrm I\Sigma_{n+1}$ proves $\mathrm B\Sigma_{n+1}$ by :ref{#thm-induction-collection}, so it is not provable in $\mathrm I\Sigma_n$ either.
:::

:::figure[Why collection fails in $K = K_{n+1}(M)$. Each element of $K$, below or above the non-standard element $b$, is the value of a $\Sigma_{n+1}$ formula whose code is a standard number, hence less than $b$. Collection applied to "$x$ has a code below $b$", for $x \leq b$, would give the same statement in $M$, and an injection of $b + 1$ elements into $b$ elements.]
<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="Below, the standard numbers, used as codes e of formulas; above, the elements of K, standard and non-standard, each the value defined by some code; all codes lie below the non-standard element b, but the values are unbounded in K"><defs><marker id="ic-n-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="20" y1="50" x2="580" y2="50" class="ink-stroke" stroke-width="1.2"/><line x1="20" y1="150" x2="580" y2="150" class="ink-stroke" stroke-width="1.2"/><text x="24" y="36" class="label">values</text><text x="24" y="138" class="label">codes</text><circle cx="40" cy="150" r="3.5" class="accent-fill"/><circle cx="70" cy="150" r="3.5" class="accent-fill"/><circle cx="100" cy="150" r="3.5" class="accent-fill"/><circle cx="130" cy="150" r="3.5" class="accent-fill"/><circle cx="160" cy="150" r="3.5" class="accent-fill"/><text x="190" y="154" class="mrm" font-size="14">⋯</text><path d="M30,160 L30,166 L200,166 L200,160" class="muted-stroke" stroke-width="1.2"/><text x="115.0" y="184" text-anchor="middle" class="label">standard numbers</text><circle cx="330" cy="150" r="4.5" class="node"/><text x="330" y="138" text-anchor="middle" class="math" font-size="14">b</text><line x1="330" y1="150" x2="330" y2="50" class="muted-stroke" stroke-dasharray="3 3"/><circle cx="330" cy="50" r="4.5" class="node"/><text x="330" y="38" text-anchor="middle" class="math" font-size="14">b</text><circle cx="40" cy="50" r="3.5" class="ink-fill"/><circle cx="100" cy="50" r="3.5" class="ink-fill"/><circle cx="250" cy="50" r="3.5" class="ink-fill"/><circle cx="450" cy="50" r="3.5" class="ink-fill"/><circle cx="560" cy="50" r="3.5" class="ink-fill"/><text x="585" y="54" class="mrm" font-size="14">⋯</text><line x1="40" y1="145" x2="250" y2="56" class="ink-stroke" stroke-width="0.9" marker-end="url(#ic-n-arrow)"/><line x1="70" y1="145" x2="40" y2="56" class="ink-stroke" stroke-width="0.9" marker-end="url(#ic-n-arrow)"/><line x1="100" y1="145" x2="560" y2="56" class="ink-stroke" stroke-width="0.9" marker-end="url(#ic-n-arrow)"/><line x1="130" y1="145" x2="100" y2="56" class="ink-stroke" stroke-width="0.9" marker-end="url(#ic-n-arrow)"/><line x1="160" y1="145" x2="450" y2="56" class="ink-stroke" stroke-width="0.9" marker-end="url(#ic-n-arrow)"/><text x="300" y="212" text-anchor="middle" class="label">every element of K, below b or above it, is the value of a code below b</text></svg>
:::

:::quiz[definable elements]
In the proof of :ref{#thm-isigma-not-bsigma}, why does the argument for $\mathrm I\Sigma_n$ not prove $\mathrm I\Sigma_{n+1}$ in $K$?

- [x] For a $\Sigma_{n+1}$ formula $\varphi$, the formula $\exists x\, (\varphi(x) \wedge \neg \varphi(x + 1))$ is $\Sigma_{n+2}$; item 2 of :ref{#lem-kn-elementary} gives witnesses in $K = K_{n+1}(M)$ only for $\Sigma_{n+1}$ formulas.
- [ ] Because $M$ does not satisfy $\mathrm I\Sigma_{n+1}$.

  $M$ is a model of $\mathrm{PA}$, and satisfies induction for all formulas.
- [ ] Because $\Sigma_{n+1}$ formulas are not preserved between $K$ and $M$.

  They are, since $K \prec_{\Sigma_{n+1}} M$; the problem is the extra quantifier of the failure point.

---

Where is it used that $b$ is non-standard?

- [x] To have every code $e_\varphi$ below $b$: the codes are standard numbers, and every standard number is less than a non-standard one.
- [ ] To make $K$ countable.

  $K$ is countable because there are countably many formulas.
- [ ] To have $b \in K$.

  Every standard number belongs to $K$ as well; what matters is that $b$ exceeds all the codes.

---

Why is the statement "$\forall x < b + 1\ \exists e < b\ \upsilon^*(e, x)$" not transferred from $K$ to $M$ directly by elementarity?

- [x] Because it is not a $\Sigma_{n+1}$ formula: a bounded universal quantifier stands in front of a $\Sigma_{n+1}$ formula. Collection in $K$ would make it equivalent to one, which is how the contradiction arises.
- [ ] Because $b$ is not an element of $M$.

  $K \subseteq M$, so $b \in M$.
- [ ] Because it is false in $K$.

  It is true in $K$: every element of $K$ has a standard code.
:::

## The other separation

The second half of the strictness of the hierarchy is admitted.

:::theorem[Lessan; Paris, Kirby]{#thm-bsigma-not-isigma}
For every $n \geq 1$, there is a model of $\mathrm B\Sigma_n$ in which $\mathrm I\Sigma_n$ fails.
:::

The model is again built inside a model $M$ of $\mathrm{PA}$ with non-standard definable elements: one closes a set of $\Sigma_{n-1}$-definable elements alternately under definability with parameters and downwards, and takes the union. Closing downwards makes collection hold, as in a model of $\mathrm{PA}$; the standard numbers become definable by a $\Sigma_n$ formula, so $\mathrm I\Sigma_n$ fails. See Dzhafarov and Mummert, Theorem 6.3.5.

Together with the previous lesson, the two theorems show that all the implications of the hierarchy are strict:
$$
\mathrm I\Delta_0 \;\Leftarrow\; \mathrm B\Sigma_1 \;\Leftarrow\; \mathrm I\Sigma_1 \;\Leftarrow\; \mathrm B\Sigma_2 \;\Leftarrow\; \mathrm I\Sigma_2 \;\Leftarrow\; \cdots
$$
The separations transfer to second-order arithmetic: the lesson on first-order parts shows that every countable model of $\mathrm I\Sigma_1$ is the first-order part of a model of $\mathsf{RCA}_0$, so $\mathsf{RCA}_0$ does not prove $\mathsf B\Sigma^0_2$.

:::corollary[Ryll-Nardzewski]{#cor-pa-not-finite}
$\mathrm{PA}$ is not equivalent to any finite set of sentences.
:::

:::proof{of=cor-pa-not-finite}
Suppose $\mathrm{PA}$ were equivalent to finitely many sentences. Each of them is provable in $\mathrm{PA}$, from finitely many axioms, which all belong to $\mathrm I\Sigma_n$ for some $n$. So $\mathrm I\Sigma_n$ would prove all of $\mathrm{PA}$, in particular $\mathrm B\Sigma_{n+1}$, contradicting :ref{#thm-isigma-not-bsigma}.
:::

## Exercises

::::exercise{difficulty=1}
Let $M$ be a model of $\mathrm{PA}$ in which some $\Sigma_1$ sentence false in $\nat$ is true. Show that $K_1(M)$ contains a non-standard element.

:::solution
Suppose that every element of $K_1(M)$ is standard; since every standard number is definable, $K_1(M) = \nat$. By :ref{#lem-kn-elementary}, $K_1(M) \prec_{\Sigma_1} M$, so every $\Sigma_1$ sentence true in $M$ is true in $\nat$, contrary to the hypothesis. This gives a second proof of :ref{#lem-nonstandard-definable}, for $\Sigma_1$-definable elements.
:::
::::

## Notes and references

The existence of models of $\mathrm I\Sigma_n$ in which $\mathrm B\Sigma_{n+1}$ fails is due to Parsons (1970); the proof by definable elements is that of Paris and Kirby (1978), who also proved that $\mathrm B\Sigma_n$ does not prove $\mathrm I\Sigma_n$. The presentation follows Dzhafarov and Mummert, Section 6.3, with a direct proof that $K_{n+1}(M)$ satisfies $\mathrm I\Sigma_n$.

- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- C. Ryll-Nardzewski, *The role of the axiom of induction in elementary arithmetic*, Fundamenta Mathematicae 39 (1952), 239–263.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 6.2–6.3.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapters I and IV.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, chapters *Satisfaction* and *Subsystems of Peano arithmetic*.
