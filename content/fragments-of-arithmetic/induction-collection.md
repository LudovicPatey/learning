---
title: Induction, least numbers and collection
summary: The schemes IΣₙ, IΠₙ, LΣₙ, LΠₙ and BΣₙ in first-order arithmetic; Σₙ and Πₙ induction are equivalent; collection closes Σₙ and Πₙ under bounded quantification (Parsons); IΣₙ proves BΣₙ (Parsons) and the least number principles; BΣₙ₊₁ proves IΣₙ (Paris and Kirby); the hierarchy and its strictness.
duration: 50
prerequisites: [bounded-induction]
---

Bounded induction is too weak to prove that exponentiation is total; $\Sigma_1$ induction proves it. This lesson sets up the hierarchy of fragments between $\mathrm I\Delta_0$ and $\mathrm{PA}$: induction, least number principles and collection for formulas of each level $\Sigma_n$ or $\Pi_n$. The result is a single chain
$$
\mathrm I\Delta_0 \;\Leftarrow\; \mathrm B\Sigma_1 \;\Leftarrow\; \mathrm I\Sigma_1 \;\Leftarrow\; \mathrm B\Sigma_2 \;\Leftarrow\; \mathrm I\Sigma_2 \;\Leftarrow\; \cdots,
$$
in which induction and collection alternate, and each $\mathrm I\Sigma_n$ may be replaced by $\mathrm I\Pi_n$, $\mathrm L\Sigma_n$ or $\mathrm L\Pi_n$.

All the proofs follow one pattern, already met in lesson 2: an instance of a scheme is proved by applying induction to an auxiliary formula, and the work is to check that this formula belongs to the class for which induction is available. A bounded universal quantifier in front of a $\Sigma_n$ formula is the obstacle, and **collection** is the axiom that removes it. The course on induction and conservation (:ref{to="induction-conservation/induction-collection"}) proves the same results for formulas of second-order arithmetic; the proofs below are written for $\mathcal L_A$ and do not depend on it.

## The schemes

:::definition{#def-fo-schemes}
Let $\Gamma$ be a class of formulas of $\mathcal L_A$. The theory $\mathrm L\Gamma$ is $\mathrm{PA}^-$ together with the universal closures of the **least number principle**
$$
\exists x\ \varphi(x, \bar p) \rightarrow \exists x\ \big(\varphi(x, \bar p) \wedge \forall y < x\ \neg \varphi(y, \bar p)\big)
$$
for $\varphi \in \Gamma$, and $\mathrm B\Gamma$ is $\mathrm I\Delta_0$ together with the universal closures of the **collection** scheme
$$
\forall x < a\ \exists y\ \varphi(x, y, \bar p) \rightarrow \exists b\ \forall x < a\ \exists y < b\ \varphi(x, y, \bar p)
$$
for $\varphi \in \Gamma$. Induction schemes are those of :ref{#def-induction-scheme}.
:::

Collection says that a definable multi-valued function on a bounded domain $[0, a)$ has bounded values. In $\nat$ every instance holds, since $[0, a)$ is finite; for a standard $a$, each instance is provable in $\mathrm I\Delta_0$, by a proof with $a$ cases. In a non-standard model, $a$ may be non-standard, and collection becomes a real axiom. The converse implication of each instance is logically valid.

With the pairing function of :ref{#fact-pairing}, a block of quantifiers of the same kind can be **contracted** to one quantifier without changing the class: if $\varphi(\bar y)$ is $\Pi_n$, then $\exists \bar y\ \varphi(\bar y)$ is equivalent in $\mathrm I\Delta_0$ to $\exists w\ \forall \bar y \leq w\ (w = \langle \bar y \rangle \rightarrow \varphi(\bar y))$, since $w$ determines $\bar y$ and $\bar y \leq w$; and the bounded universal quantifier in front of a $\Pi_n$ formula keeps it $\Pi_n$, logically (lesson 1). So we may assume that every block has one quantifier, and that collection is stated for a single $y$.

## Σₙ and Πₙ induction

:::theorem[Paris, Kirby]{#thm-fo-isigma-ipi}
For every $n \geq 1$, $\mathrm I\Sigma_n$ and $\mathrm I\Pi_n$ are equivalent over $\mathrm I\Delta_0$.
:::

To derive an instance for a $\Pi_n$ formula from $\Sigma_n$ induction, the induction is run downwards. If $\varphi$ fails at $a$, the statement "$\varphi$ fails at $a - y$" has the complexity of $\neg \varphi$, which is $\Sigma_n$; it holds at $y = 0$ and propagates up to $y = a$, which gives a failure at $0$.

:::proof{of=thm-fo-isigma-ipi}
Assume $\mathrm I\Sigma_n$. Let $\varphi$ be $\Pi_n$, with $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$, and suppose $\neg \varphi(a)$. Let
$$
\theta(y) \equiv y \leq a \rightarrow \exists x \leq a\ (x + y = a \wedge \neg \varphi(x)).
$$
Since $\neg \varphi$ is equivalent to a $\Sigma_n$ formula, and $\exists x \leq a$ in front of a $\Sigma_n$ formula keeps it $\Sigma_n$, $\theta$ is $\Sigma_n$. We have $\theta(0)$, with $x = a$. Assume $\theta(y)$ and $y + 1 \leq a$; take $x$ with $x + y = a$ and $\neg \varphi(x)$. Since $y < a$, $x \neq 0$, so $x = x' + 1$, and $\neg \varphi(x')$, since $\varphi(x')$ would give $\varphi(x)$. As $x' + (y + 1) = a$, $\theta(y + 1)$ holds. By $\Sigma_n$ induction, $\theta(a)$: some $x$ with $x + a = a$, that is $x = 0$, satisfies $\neg \varphi(x)$, a contradiction.

Assume $\mathrm I\Pi_n$. Let $\varphi$ be $\Sigma_n$, with $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$, and suppose $\neg \varphi(a)$. The formula
$$
\eta(y) \equiv y \leq a \rightarrow \forall x \leq a\ (x + y = a \rightarrow \neg \varphi(x))
$$
is $\Pi_n$. It holds at $0$. If $\eta(y)$, $y + 1 \leq a$ and $x + (y + 1) = a$, then $(x + 1) + y = a$, so $\neg \varphi(x + 1)$, hence $\neg \varphi(x)$; so $\eta(y + 1)$. By $\Pi_n$ induction, $\eta(a)$, which gives $\neg \varphi(0)$: a contradiction.
:::

The guard $y \leq a$ is needed because $a - y$ exists only for $y \leq a$; without it, the step from $y$ to $y + 1$ fails for $y \geq a$.

## Collection and bounded quantifiers

:::lemma[Parsons]{#lem-fo-collection-closure}
Let $n \geq 1$. Over $\mathrm B\Sigma_n$, every formula obtained from $\Sigma_n$ formulas by $\wedge$, $\vee$, bounded quantifiers and $\exists$ is equivalent to a $\Sigma_n$ formula, and every formula obtained from $\Pi_n$ formulas by $\wedge$, $\vee$, bounded quantifiers and $\forall$ is equivalent to a $\Pi_n$ formula.
:::

:::proof{of=lem-fo-collection-closure}
The statement for $\Pi_n$ follows from the one for $\Sigma_n$ by negation, and it suffices to treat one operation at a time, by induction on $n$. Conjunction, disjunction and $\exists$ are handled by renaming bound variables and merging blocks. For $n = 1$, $\exists x < t\ \exists y\ \delta$ is $\exists y\ \exists x < t\ \delta$, and $\forall x < t\ \exists y\ \delta$, with $\delta$ bounded, is equivalent by collection to $\exists b\ \forall x < t\ \exists y < b\ \delta$, which is $\Sigma_1$; the converse implication is logical.

Assume the lemma for $n$, and $\mathrm B\Sigma_{n+1}$, which contains $\mathrm B\Sigma_n$. A $\Sigma_{n+1}$ formula is $\exists y\ \psi$ with $\psi \in \Pi_n$. Conjunctions of two such formulas are $\exists y\, \exists z\, (\psi \wedge \psi')$, and $\psi \wedge \psi'$ is $\Pi_n$; similarly for disjunctions. The formula $\exists x < t\ \exists y\ \psi$ is $\exists y\ \exists x < t\ \psi$, and $\exists x < t\ \psi$ is $\Pi_n$ by the lemma for $n$. Finally, by $\mathrm B\Sigma_{n+1}$ applied to $\psi$, $\forall x < t\ \exists y\ \psi$ is equivalent to $\exists b\ \forall x < t\ \exists y < b\ \psi$, and the bounded quantifiers in front of $\psi$ give a $\Pi_n$ formula by the lemma for $n$.
:::

The lemma explains why collection appears at all: it is exactly what makes the classes $\Sigma_n$ and $\Pi_n$ insensitive to bounded quantifiers, as they are in $\nat$.

## Induction implies collection

:::theorem[Parsons]{#thm-fo-parsons}
For every $n \geq 1$, $\mathrm I\Sigma_n$ proves $\mathrm B\Sigma_n$.
:::

The common bound is found by induction on the size of the domain: if the witnesses for $x < c$ are bounded by $b$, those for $x < c + 1$ are bounded by $\max(b, w + 1)$, where $w$ is a witness for $c$. The statement "the witnesses for $x < c$ have a common bound" is $\Sigma_n$ provided the bounded quantifier $\forall x < c$ can be absorbed, which uses collection one level down.

:::proof{of=thm-fo-parsons}
By induction on $n$. Assume $\mathrm I\Sigma_n$; if $n \geq 2$, then $\mathrm I\Sigma_{n-1}$ holds, hence $\mathrm B\Sigma_{n-1}$ by the induction hypothesis, and :ref{#lem-fo-collection-closure} applies at level $n - 1$.

Let $\forall x < a\ \exists y\ \varphi(x, y)$ with $\varphi = \exists z\ \psi(x, y, z)$ and $\psi \in \Pi_{n-1}$ (bounded if $n = 1$). Let $\chi(x, w) \equiv \exists y < w\ \exists z < w\ \psi(x, y, z)$; it is $\Pi_{n-1}$ in $\mathrm B\Sigma_{n-1}$, or bounded if $n = 1$, and $\forall x < a\ \exists w\ \chi(x, w)$. Let
$$
\theta(c) \equiv c \leq a \rightarrow \exists b\ \forall x < c\ \exists w < b\ \chi(x, w).
$$
The formula after $\exists b$ is $\Pi_{n-1}$ by the same argument, so $\theta$ is $\Sigma_n$. Then $\theta(0)$ holds with $b = 0$. If $\theta(c)$ and $c + 1 \leq a$, let $b$ be the bound for $c$ and $w_0$ satisfy $\chi(c, w_0)$; then $\max(b, w_0 + 1)$ is a bound for $c + 1$. By $\Sigma_n$ induction, $\theta(a)$: some $b$ satisfies $\forall x < a\ \exists w < b\ \chi(x, w)$, hence $\forall x < a\ \exists y < b\ \varphi(x, y)$.
:::

:::quiz[induction implies collection]
Why does the proof of :ref{#thm-fo-parsons} for $\Sigma_n$ formulas use $\mathrm B\Sigma_{n-1}$?

- [x] To see that $\forall x < c\ \exists w < b\ \chi(x, w)$ is $\Pi_{n-1}$, so that $\theta$ is $\Sigma_n$ and $\Sigma_n$ induction applies to it.
- [ ] To find the witness $w_0$ for $c$.

  It comes from the hypothesis $\forall x < a\ \exists w\ \chi(x, w)$, since $c < a$.
- [ ] To conclude from $\theta(a)$.

  The conclusion is logical once $\theta(a)$ holds.
:::

## Least number principles

:::proposition{#prop-fo-least-number}
For every $n \geq 1$, the theories $\mathrm I\Sigma_n$, $\mathrm I\Pi_n$, $\mathrm L\Sigma_n$ and $\mathrm L\Pi_n$ are equivalent over $\mathrm I\Delta_0$.
:::

:::proof{of=prop-fo-least-number}
*$\mathrm L\Pi_n$ implies $\mathrm I\Sigma_n$, and $\mathrm L\Sigma_n$ implies $\mathrm I\Pi_n$.* If induction fails for $\varphi$, with $\neg \varphi(a)$, let $m$ be least with $\neg \varphi(m)$; then $m \neq 0$, $m = m' + 1$ with $\varphi(m')$, hence $\varphi(m)$, a contradiction. The negation of a $\Sigma_n$ formula is $\Pi_n$, and conversely.

*$\mathrm I\Sigma_n$ implies $\mathrm L\Pi_n$.* Let $\varphi$ be $\Pi_n$ with $\varphi(c)$ and no least element. Let $\theta(x) \equiv \forall y < x + 1\ \neg \varphi(y)$; it is $\Sigma_n$ by :ref{#lem-fo-collection-closure}, since $\mathrm I\Sigma_n$ proves $\mathrm B\Sigma_n$ (:ref{#thm-fo-parsons}). If $\varphi(0)$, then $0$ is least; so $\theta(0)$. If $\theta(x)$ and $\varphi(x + 1)$, then $x + 1$ is least; so $\theta(x) \rightarrow \theta(x + 1)$. By induction $\theta(c)$, contradicting $\varphi(c)$.

*$\mathrm I\Pi_n$ implies $\mathrm L\Sigma_n$*, by the same argument for $\varphi \in \Sigma_n$; now $\theta$ is $\Pi_n$ logically, a bounded universal quantifier in front of a $\Pi_n$ formula. With :ref{#thm-fo-isigma-ipi}, the four schemes are equivalent.
:::

For $n = 0$, the equivalence of $\mathrm I\Delta_0$ and $\mathrm L\Delta_0$ was proved in lesson 2.

## Collection implies induction

:::theorem[Paris, Kirby]{#thm-fo-paris-kirby}
For every $n \geq 0$, $\mathrm B\Sigma_{n+1}$ proves $\mathrm I\Sigma_n$.
:::

To prove $\varphi(a)$ for $\varphi = \exists y\ \psi$ by induction, one would like to carry the witnesses along. Collection, applied to all the steps below $a$ at once, gives a single bound $b$ on the witnesses needed; then "$\varphi(x)$ has a witness below $b$" has lower complexity, and induction one level down applies.

:::proof{of=thm-fo-paris-kirby}
For $n = 0$, $\mathrm B\Sigma_1$ contains $\mathrm I\Delta_0$ by definition. Let $n \geq 1$, by induction on $n$; $\mathrm B\Sigma_{n+1}$ contains $\mathrm B\Sigma_n$, so it proves $\mathrm I\Sigma_{n-1}$ by the induction hypothesis, hence $\mathrm I\Pi_{n-1}$ (:ref{#thm-fo-isigma-ipi}, or trivially if $n = 1$).

Let $\varphi(x) \equiv \exists y\ \psi(x, y)$ with $\psi \in \Pi_{n-1}$, assume $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$, and fix $a$. For every $x < a$ there is $u$ with
$$
\forall y\ \neg \psi(x, y) \;\vee\; \psi(x + 1, u):
$$
if $\varphi(x)$ fails, any $u$ will do; otherwise $\varphi(x + 1)$ provides $u$. This formula is $\Pi_n$, hence $\Sigma_{n+1}$, and collection gives $b_0$ such that for every $x < a$ some $u < b_0$ satisfies it. Let $y_0$ satisfy $\psi(0, y_0)$ and $b = \max(b_0, y_0 + 1)$. Let
$$
\theta(x) \equiv x \leq a \rightarrow \exists u < b\ \psi(x, u),
$$
which is bounded if $n = 1$, and $\Pi_{n-1}$ by :ref{#lem-fo-collection-closure} in $\mathrm B\Sigma_{n-1}$ if $n \geq 2$. Then $\theta(0)$ holds. If $\theta(x)$ and $x + 1 \leq a$, some $u < b$ satisfies $\psi(x, u)$, so the first disjunct fails at $x$, and $\psi(x + 1, u')$ for some $u' < b_0 \leq b$: this is $\theta(x + 1)$. By $\Pi_{n-1}$ induction, $\theta(a)$, hence $\varphi(a)$.
:::

:::quiz[collection implies induction]
Why does the formula to which collection is applied contain the disjunct $\forall y\ \neg \psi(x, y)$?

- [x] Collection needs a witness $u$ for every $x < a$, while $\varphi(x + 1)$ is known only when $\varphi(x)$ holds; the disjunct makes the formula true at the $x$ where $\varphi(x)$ fails. It raises the complexity to $\Pi_n$, which is why collection for $\Sigma_{n+1}$ formulas is needed.
- [ ] To make the formula $\Sigma_n$.

  Without the disjunct the formula $\psi(x + 1, u)$ is $\Pi_{n-1}$, which is simpler; the disjunct makes it $\Pi_n$.
- [ ] Because $\varphi(x)$ fails for some $x < a$.

  The proof shows that $\varphi$ holds below $a$; the disjunct is needed before this is known.
:::

## The hierarchy

Together, for every $n \geq 1$, over $\mathrm I\Delta_0$:
$$
\mathrm I\Sigma_{n+1} \;\Rightarrow\; \mathrm B\Sigma_{n+1} \;\Rightarrow\; \mathrm I\Sigma_n \;\Rightarrow\; \mathrm B\Sigma_n,
$$
and each $\mathrm I\Sigma_n$ may be replaced by $\mathrm I\Pi_n$, $\mathrm L\Sigma_n$ or $\mathrm L\Pi_n$. None of these implications reverses: for every $n$, there is a model of $\mathrm I\Sigma_n$ in which $\mathrm B\Sigma_{n+1}$ fails, and a model of $\mathrm B\Sigma_{n+1}$ in which $\mathrm I\Sigma_{n+1}$ fails. The first is the model of the $\Sigma_{n+1}$-definable elements of a suitable model of $\mathrm{PA}$, built in the lesson :ref{to="induction-conservation/separations"} of the course on induction and conservation; the second is due to Paris and Kirby (1978), and is admitted there. We use the strictness only in remarks and exercises. Lesson 7 gives a second proof of $\mathrm B\Sigma_{n+1} \Rightarrow \mathrm I\Sigma_n$ in the presence of exponentiation, through coded sets.

## Exercises

::::exercise{#ex-fo-bsigma-bpi difficulty=1}
Show that, over $\mathrm I\Delta_0$, $\mathrm B\Sigma_{n+1}$ is equivalent to $\mathrm B\Pi_n$ for every $n \geq 1$.

:::solution
Every $\Pi_n$ formula is $\Sigma_{n+1}$, so $\mathrm B\Sigma_{n+1}$ implies $\mathrm B\Pi_n$. Conversely, let $\varphi(x, y) \equiv \exists z\ \psi(x, y, z)$ with $\psi \in \Pi_n$ and $\forall x < a\ \exists y\ \varphi(x, y)$. Let $\psi'(x, w) \equiv \forall y \leq w\ \forall z \leq w\ (w = \langle y, z \rangle \rightarrow \psi(x, y, z))$, which is $\Pi_n$ logically. Then $\forall x < a\ \exists w\ \psi'(x, w)$, and $\mathrm B\Pi_n$ gives $b$ with $\forall x < a\ \exists w < b\ \psi'(x, w)$. If $w = \langle y, z \rangle < b$, then $y \leq w < b$ and $\varphi(x, y)$.
:::
::::

::::exercise{difficulty=2}
Show that $\mathrm I\Sigma_n$ proves the **order induction** scheme $\forall x\, \big((\forall y < x\ \varphi(y)) \rightarrow \varphi(x)\big) \rightarrow \forall x\ \varphi(x)$ for $\Sigma_n$ formulas $\varphi$, $n \geq 1$.

:::solution
Fix $z$, and let $\theta(x) \equiv x \leq z \rightarrow \forall y < x\ \varphi(y)$, which is $\Sigma_n$ by :ref{#lem-fo-collection-closure} and :ref{#thm-fo-parsons}. Then $\theta(0)$; if $\theta(x)$ and $x + 1 \leq z$, then $\forall y < x\ \varphi(y)$, so $\varphi(x)$ by hypothesis, and $\theta(x + 1)$. By induction $\theta(z)$, and $\varphi(z)$ by hypothesis.
:::
::::

## Notes and references

The hierarchy of induction and collection is due to Paris and Kirby (1978), building on Parsons (1970), who introduced collection, proved that it closes $\Sigma_n$ and $\Pi_n$ under bounded quantification, and proved $\mathrm I\Sigma_{n+1} \Rightarrow \mathrm B\Sigma_{n+1}$. The proofs follow Wong's Lecture 2 (Theorems 2.2, 2.3 and the exercise 2.10) and Hájek and Pudlák, Chapter I, Section 2(a) (Theorems I.2.4–I.2.5, Lemmas I.2.8–I.2.15). The same results for second-order arithmetic are in the course on induction and conservation.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 2(a).
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 2.
