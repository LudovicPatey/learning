---
title: Induction, collection and least numbers
summary: The schemes of Σ⁰ₙ and Π⁰ₙ induction, collection and least number principles; closure of the classes Σ⁰ₙ under bounded quantification in the presence of collection; Σ⁰ₙ and Π⁰ₙ induction are equivalent; the hierarchy IΣ⁰ₙ₊₁ ⇒ BΣ⁰ₙ₊₁ ⇒ IΣ⁰ₙ.
duration: 40
prerequisites: [second-order-arithmetic/rca0]
---

In an ω-model, every form of induction holds, because the first-order part is the true $\nat$. In a model with non-standard numbers, induction may fail for complicated formulas: a formula may define a proper initial segment closed under successor, a **cut**, which contains $0$ but not every number. The axioms of $\mathsf{RCA}_0$ only grant induction for $\Sigma^0_1$ formulas, and many principles of ordinary mathematics turn out to be equivalent to forms of induction or of the related **collection** principle. This lesson sets up the hierarchy of these schemes, following Paris and Kirby.

## The schemes

All formulas are formulas of $\mathcal L_2$, with number and set parameters (:ref{#def-l2}); the classes $\Sigma^0_n$ and $\Pi^0_n$ count blocks of quantifiers of the same kind as one.

:::definition{#def-induction-schemes}
Let $n \geq 0$ and $\Gamma$ be $\Sigma^0_n$ or $\Pi^0_n$. For every formula $\varphi \in \Gamma$, the universal closures of the following formulas form respectively the schemes $\mathsf I\Gamma$, $\mathsf B\Gamma$ and $\mathsf L\Gamma$:

1. **induction**: $(\varphi(0) \wedge \forall x\, (\varphi(x) \rightarrow \varphi(x+1))) \rightarrow \forall x\, \varphi(x)$;
2. **collection**: $\forall x < a\ \exists y\ \varphi(x, y) \rightarrow \exists b\ \forall x < a\ \exists y < b\ \varphi(x, y)$;
3. **least number principle**: $\exists x\, \varphi(x) \rightarrow \exists x\, (\varphi(x) \wedge \forall y < x\ \neg \varphi(y))$.

The theory $\mathsf I\Delta^0_0$ consists of the basic axioms (:ref{#def-z2}) and the scheme $\mathsf I\Sigma^0_0$ of induction for bounded formulas.
:::

The formula $\varphi$ may contain other free variables, which act as parameters. Collection says that a "finite" family of nonempty sets of witnesses has a common bound; here finite means indexed by the numbers below some $a$, which may be non-standard. In the true $\nat$, every instance of the three schemes holds. All theories in this course extend $\mathsf I\Delta^0_0$, and $\mathsf{RCA}_0$ contains $\mathsf I\Sigma^0_1$.

:::fact{#fact-idelta0}
$\mathsf I\Delta^0_0$ proves the elementary properties of addition, multiplication and order: $<$ is a discrete linear order with least element $0$, every $x \neq 0$ is $y + 1$ for a unique $y$, $x \leq y$ if and only if $x + z = y$ for some $z$, which is then unique, polynomials with non-negative coefficients are monotone, and the pairing function $\langle u, v \rangle = \frac{(u + v)(u + v + 1)}{2} + v$ is a bijection, definable by a bounded formula, with $u, v \leq \langle u, v \rangle$.
:::

These properties are proved by bounded induction, in the same way as in Peano arithmetic; see Kaye, *Models of Peano Arithmetic*, Chapter 2. We use them freely.

A formula obtained from $\Sigma^0_n$ formulas by conjunction, disjunction, bounded quantification and existential quantification is not $\Sigma^0_n$ in general, because a bounded universal quantifier cannot be moved across an unbounded existential one. In the true $\nat$, $\forall x < a\ \exists y\ \varphi$ is equivalent to $\exists b\ \forall x < a\ \exists y < b\ \varphi$; this equivalence is exactly an instance of collection.

:::lemma{#lem-collection-closure}
Let $n \geq 1$. Over $\mathsf I\Delta^0_0 + \mathsf B\Sigma^0_n$:

1. every formula obtained from $\Sigma^0_n$ formulas by $\wedge$, $\vee$, bounded quantifiers $\exists x < t$, $\forall x < t$ and existential quantifiers is provably equivalent to a $\Sigma^0_n$ formula;
2. every formula obtained from $\Pi^0_n$ formulas by $\wedge$, $\vee$, bounded quantifiers and universal quantifiers is provably equivalent to a $\Pi^0_n$ formula.
:::

:::proof{of=lem-collection-closure}
Item 2 follows from item 1 by negation, since the negation of a $\Sigma^0_n$ formula is logically equivalent to a $\Pi^0_n$ formula. It suffices to treat one operation at a time. By renaming bound variables, $\exists y\, \alpha \wedge \exists z\, \beta$ is equivalent to $\exists y\, \exists z\, (\alpha \wedge \beta)$, and similarly for $\vee$; $\exists x < t\ \exists y\, \alpha$ is equivalent to $\exists y\ \exists x < t\ \alpha$; and an existential quantifier merges with the first block. We may also assume that the first block of a $\Sigma^0_n$ formula consists of a single quantifier: $\exists y_1\, \exists y_2\, \alpha$ is equivalent to $\exists w\ \exists y_1 < w\ \exists y_2 < w\ \alpha$, and $\exists y_1 < w\ \exists y_2 < w\ \alpha$, with $\alpha \in \Pi^0_{n-1}$, is bounded if $n = 1$ and equivalent to a $\Pi^0_{n-1}$ formula by item 2 for $n - 1$ if $n \geq 2$, in the induction below. The only non-trivial case is the bounded universal quantifier. We proceed by induction on $n$.

For $n = 1$, let $\varphi = \exists y\, \delta(x, y)$ with $\delta$ bounded. Then $\forall x < t\ \exists y\ \delta$ implies $\exists b\ \forall x < t\ \exists y < b\ \delta$ by $\mathsf B\Sigma^0_1$, and the converse is logical. The second formula is $\Sigma^0_1$.

Let $n \geq 1$, assume the lemma for $n$, and assume $\mathsf B\Sigma^0_{n+1}$, which contains $\mathsf B\Sigma^0_n$. A $\Sigma^0_{n+1}$ formula has the form $\exists y\, \psi$ with $\psi \in \Pi^0_n$. Conjunctions and disjunctions of $\Pi^0_n$ formulas, and bounded quantifications of them, are equivalent to $\Pi^0_n$ formulas by item 2 for $n$; so the easy cases above stay within $\Sigma^0_{n+1}$. For the bounded universal quantifier, $\forall x < t\ \exists y\ \psi(x, y)$ is equivalent to $\exists b\ \forall x < t\ \exists y < b\ \psi(x, y)$ by $\mathsf B\Sigma^0_{n+1}$ applied to $\psi$, which is $\Sigma^0_{n+1}$. By item 2 for $n$, $\forall x < t\ \exists y < b\ \psi$ is equivalent to a $\Pi^0_n$ formula, so the whole formula is equivalent to a $\Sigma^0_{n+1}$ formula.
:::

## Σ⁰ₙ and Π⁰ₙ induction

:::theorem[Paris, Kirby]{#thm-isigma-ipi}
For every $n \geq 1$, $\mathsf I\Delta^0_0$ proves that $\mathsf I\Sigma^0_n$ and $\mathsf I\Pi^0_n$ are equivalent.
:::

:::proof{of=thm-isigma-ipi}
($\mathsf I\Sigma^0_n \Rightarrow \mathsf I\Pi^0_n$) Let $\varphi$ be $\Pi^0_n$ with $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x+1))$, and suppose that $\neg \varphi(a)$. Let
$$
\theta(y) \equiv y \leq a \rightarrow \exists x\, (x + y = a \wedge \neg \varphi(x)).
$$
The formula $\neg \varphi$ is equivalent to a $\Sigma^0_n$ formula, and the conjunction with the bounded formula $x + y = a$ can be moved inside its innermost block; so $\theta$ is equivalent to a $\Sigma^0_n$ formula. We have $\theta(0)$, with $x = a$. Suppose $\theta(y)$, and let $y + 1 \leq a$. Then $y < a$, and there is $x$ with $x + y = a$ and $\neg \varphi(x)$; $x \neq 0$, since $y < a$, so $x = x' + 1$. Since $\varphi(x')$ would imply $\varphi(x)$, we have $\neg \varphi(x')$, and $x' + (y + 1) = a$: this is $\theta(y + 1)$. By $\mathsf I\Sigma^0_n$, $\theta(a)$ holds, which gives $x$ with $x + a = a$, so $x = 0$, and $\neg \varphi(0)$: a contradiction.

($\mathsf I\Pi^0_n \Rightarrow \mathsf I\Sigma^0_n$) Let $\varphi$ be $\Sigma^0_n$ with $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x+1))$, and suppose $\neg \varphi(a)$. Let
$$
\eta(y) \equiv y \leq a \rightarrow \forall x\, (x + y = a \rightarrow \neg \varphi(x)),
$$
equivalent to a $\Pi^0_n$ formula. Then $\eta(0)$ holds since $\neg \varphi(a)$. Suppose $\eta(y)$ and $y + 1 \leq a$, and let $x + (y + 1) = a$. Then $(x + 1) + y = a$, so $\neg \varphi(x + 1)$, hence $\neg \varphi(x)$. So $\eta(y+1)$. By $\mathsf I\Pi^0_n$, $\eta(a)$ holds, and with $x = 0$ it gives $\neg \varphi(0)$: a contradiction.
:::

The proof reverses the direction of the induction: the property "$a - y$ fails" is propagated from $y = 0$ up to $y = a$. Both formulas $\theta$ and $\eta$ have the same complexity as the negation of $\varphi$, which is why the trick exchanges $\Sigma^0_n$ and $\Pi^0_n$.

## Induction implies collection

:::theorem[Paris, Kirby]{#thm-induction-collection}
For every $n \geq 1$, $\mathsf I\Delta^0_0 + \mathsf I\Sigma^0_n$ proves $\mathsf B\Sigma^0_n$.
:::

:::proof{of=thm-induction-collection}
By induction on $n$. Assume $\mathsf I\Sigma^0_n$, and, if $n \geq 2$, the theorem for $n - 1$, so that $\mathsf B\Sigma^0_{n-1}$ holds and :ref{#lem-collection-closure} applies to $\Pi^0_{n-1}$ formulas.

Let $\varphi(x, y) \equiv \exists z\, \psi(x, y, z)$ with $\psi \in \Pi^0_{n-1}$ (bounded if $n = 1$), and suppose that $\forall x < a\ \exists y\ \varphi(x, y)$. Let
$$
\chi(x, w) \equiv \exists y < w\ \exists z < w\ \psi(x, y, z).
$$
It is equivalent to a $\Pi^0_{n-1}$ formula: for $n = 1$ it is bounded, and for $n \geq 2$ by :ref{#lem-collection-closure}. Moreover $\forall x < a\ \exists w\ \chi(x, w)$: take $w$ larger than a witness $y$ and a witness $z$. Let
$$
\theta(c) \equiv c \leq a \rightarrow \exists b\ \forall x < c\ \exists w < b\ \chi(x, w).
$$
The formula $\forall x < c\ \exists w < b\ \chi$ is equivalent to a $\Pi^0_{n-1}$ formula, by the same argument, so $\theta$ is equivalent to a $\Sigma^0_n$ formula. Then $\theta(0)$ holds with $b = 0$. Suppose $\theta(c)$ and $c + 1 \leq a$; let $b$ be given by $\theta(c)$, and $w_0$ with $\chi(c, w_0)$, which exists since $c < a$. Then $b' = \max(b, w_0 + 1)$ witnesses $\theta(c+1)$. By $\mathsf I\Sigma^0_n$, $\theta(a)$ holds: there is $b$ such that for every $x < a$ some $w < b$ satisfies $\chi(x, w)$, hence some $y < w < b$ satisfies $\varphi(x, y)$.
:::

:::quiz[induction implies collection]
In the proof of :ref{#thm-induction-collection}, why does the formula $\theta(c)$ carry the hypothesis $c \leq a$?

- [x] The induction step needs a witness $w_0$ with $\chi(c, w_0)$, and the hypothesis $\forall x < a\ \exists w\ \chi(x, w)$ provides one only for $c < a$; without the guard, the step from $c$ to $c + 1$ could fail for $c \geq a$.
- [ ] To make $\theta$ equivalent to a $\Sigma^0_n$ formula.

  The guard is a bounded formula; the formula without it has the same complexity.
- [ ] Because $\mathsf I\Sigma^0_n$ only gives induction up to a fixed bound.

  $\mathsf I\Sigma^0_n$ gives $\forall c\ \theta(c)$ for the formula as written; the bound $a$ comes from the instance of collection, not from the induction scheme.

---

Why does the proof for $\Sigma^0_n$ formulas use $\mathsf B\Sigma^0_{n-1}$?

- [x] To show that $\theta$ is equivalent to a $\Sigma^0_n$ formula: the bounded quantifiers in front of the $\Pi^0_{n-1}$ formula $\psi$ must be absorbed, by :ref{#lem-collection-closure}.
- [ ] To find the witness $w_0$.

  The witness comes from the hypothesis $\forall x < a\ \exists y\ \varphi$.
- [ ] To conclude from $\theta(a)$.

  The conclusion is logical once $\theta(a)$ is established.
:::

## Least number principles

:::proposition{#prop-least-number}
For every $n \geq 1$, the schemes $\mathsf I\Sigma^0_n$, $\mathsf I\Pi^0_n$, $\mathsf L\Sigma^0_n$ and $\mathsf L\Pi^0_n$ are equivalent over $\mathsf I\Delta^0_0$.
:::

:::proof{of=prop-least-number}
($\mathsf L\Pi^0_n \Rightarrow \mathsf I\Sigma^0_n$) Let $\varphi \in \Sigma^0_n$ with $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x+1))$, and suppose $\neg \varphi(a)$. By $\mathsf L\Pi^0_n$ applied to the $\Pi^0_n$ formula $\neg \varphi$, there is a least $m$ with $\neg \varphi(m)$. Then $m \neq 0$, so $m = m' + 1$ with $\varphi(m')$, hence $\varphi(m)$: a contradiction. The same argument gives $\mathsf L\Sigma^0_n \Rightarrow \mathsf I\Pi^0_n$.

($\mathsf I\Sigma^0_n \Rightarrow \mathsf L\Pi^0_n$) Let $\varphi \in \Pi^0_n$ with $\varphi(c)$, and suppose there is no least $x$ with $\varphi(x)$. Let $\theta(x) \equiv \forall y \leq x\ \neg \varphi(y)$. By :ref{#thm-induction-collection}, $\mathsf B\Sigma^0_n$ holds, so $\theta$ is equivalent to a $\Sigma^0_n$ formula by :ref{#lem-collection-closure}. If $\varphi(0)$, then $0$ is least; so $\theta(0)$. If $\theta(x)$ and $\varphi(x+1)$, then $x + 1$ is least; so $\theta(x)$ implies $\theta(x+1)$. By induction, $\theta(c)$ holds, contradicting $\varphi(c)$.

($\mathsf I\Pi^0_n \Rightarrow \mathsf L\Sigma^0_n$) The same argument, with $\varphi \in \Sigma^0_n$: the formula $\forall y \leq x\ \neg \varphi(y)$ is equivalent to a $\Pi^0_n$ formula, since $\mathsf I\Pi^0_n$ implies $\mathsf I\Sigma^0_n$ by :ref{#thm-isigma-ipi}, hence $\mathsf B\Sigma^0_n$.

Combined with :ref{#thm-isigma-ipi}, the four schemes are equivalent.
:::

The least number principle gives the model-theoretic meaning of induction. If $\mathsf I\Sigma^0_n$ fails, some $\Sigma^0_n$ formula $\varphi$ holds at $0$, is preserved by successor, and fails somewhere; the set of numbers below every failure is then a cut, and its complement has no least element. In a model of $\mathsf I\Sigma^0_n$, no $\Sigma^0_n$ or $\Pi^0_n$ formula defines a cut. For instance, in a non-standard model of $\mathsf I\Sigma^0_n$, the standard numbers $\{ 0, 1, 2, \dots \}$ form a cut, so they are not definable by such a formula: if a $\Sigma^0_n$ or $\Pi^0_n$ formula holds for every standard number, it holds for some non-standard number. This is the **overspill** principle.

## Collection implies induction

:::theorem[Paris, Kirby]{#thm-collection-induction}
For every $n \geq 1$, $\mathsf I\Delta^0_0 + \mathsf B\Sigma^0_{n+1}$ proves $\mathsf I\Sigma^0_n$.
:::

:::proof{of=thm-collection-induction}
By induction on $n$. Assume $\mathsf B\Sigma^0_{n+1}$; it contains $\mathsf B\Sigma^0_n$ and $\mathsf B\Sigma^0_{n-1}$. When $n \geq 2$, the induction hypothesis (the theorem for $n - 1$, applied to $\mathsf B\Sigma^0_n$) gives $\mathsf I\Sigma^0_{n-1}$, hence also $\mathsf I\Pi^0_{n-1}$ by :ref{#thm-isigma-ipi}.

Let $\varphi(x) \equiv \exists y\, \psi(x, y)$ with $\psi \in \Pi^0_{n-1}$, suppose $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x+1))$, and fix $a$. For every $x \leq a$ there is $u$ with $\forall y\, \neg \psi(x, y) \vee \psi(x + 1, u)$. This formula is equivalent to a $\Pi^0_n$ formula, hence is $\Sigma^0_{n+1}$, and $\mathsf B\Sigma^0_{n+1}$ gives a bound $b_0$. Let $y_0$ be such that $\psi(0, y_0)$, and $b = \max(b_0, y_0 + 1)$. Then for every $x < a$,
$$
\exists y < b\ \psi(x, y) \rightarrow \exists u < b\ \psi(x + 1, u).
$$
Indeed, if $\psi(x, y)$, the first disjunct fails, so $\psi(x + 1, u)$ for some $u < b_0 \leq b$. Let
$$
\theta(x) \equiv x \leq a \rightarrow \exists u < b\ \psi(x, u).
$$
For $n = 1$, $\theta$ is bounded; for $n \geq 2$, it is equivalent to a $\Pi^0_{n-1}$ formula by :ref{#lem-collection-closure}. We have $\theta(0)$, since $y_0 < b$, and $\theta(x) \rightarrow \theta(x+1)$ by the display. By $\mathsf I\Delta^0_0$ or $\mathsf I\Pi^0_{n-1}$, $\theta(a)$ holds, so $\varphi(a)$.
:::

The idea is that collection bounds, uniformly for $x \leq a$, the witnesses needed to pass from $x$ to $x + 1$. Once the witnesses are bounded, the induction becomes an induction on a formula of lower complexity.

We obtain the hierarchy, for every $n \geq 1$, over $\mathsf I\Delta^0_0$:
$$
\mathsf I\Sigma^0_{n+1} \;\Rightarrow\; \mathsf B\Sigma^0_{n+1} \;\Rightarrow\; \mathsf I\Sigma^0_n \;\Rightarrow\; \mathsf B\Sigma^0_n.
$$
Paris and Kirby showed that none of these implications reverses: for every $n \geq 1$, there are models of $\mathsf I\Sigma^0_n$ in which $\mathsf B\Sigma^0_{n+1}$ fails, and models of $\mathsf B\Sigma^0_n$ in which $\mathsf I\Sigma^0_n$ fails. The constructions use non-standard models of arithmetic and are admitted here (Hájek and Pudlák, Chapter IV). Slaman proved that $\mathsf B\Sigma^0_n$ is equivalent to induction for $\Delta^0_n$ formulas, over $\mathsf I\Delta^0_0$ with the totality of exponentiation.

:::quiz[collection implies induction]
In the proof of :ref{#thm-collection-induction}, why is the formula $\theta$ of lower complexity than $\varphi$?

- [x] Because the unbounded existential quantifier $\exists y$ of $\varphi$ is replaced by a bounded one, $\exists u < b$, the bound being provided by collection; bounded quantifiers in front of $\Pi^0_{n-1}$ formulas are absorbed.
- [ ] Because $\theta$ only concerns $x \leq a$.

  The restriction to $x \leq a$ is needed to apply collection, but it does not change the complexity.
- [ ] Because $\psi$ is bounded.

  $\psi$ is only bounded for $n = 1$.

---

Why is the witness $y_0$ for $\varphi(0)$ added to the bound?

- [x] Because collection only bounds the witnesses for the steps from $x$ to $x + 1$; the base case $\theta(0)$ needs a witness for $\varphi(0)$ below $b$.
- [ ] Because $b_0$ might be $0$.

  Even a positive $b_0$ could be smaller than every witness of $\varphi(0)$.
- [ ] To make $\theta$ a $\Sigma^0_n$ formula.

  The bound does not affect the complexity.
:::

## Exercises

::::exercise{#ex-bsigma-bpi difficulty=1}
Show that, over $\mathsf I\Delta^0_0$, $\mathsf B\Sigma^0_{n+1}$ is equivalent to $\mathsf B\Pi^0_n$ for every $n \geq 1$.

:::solution
Every $\Pi^0_n$ formula is $\Sigma^0_{n+1}$, so $\mathsf B\Sigma^0_{n+1}$ implies $\mathsf B\Pi^0_n$. Conversely, assume $\mathsf B\Pi^0_n$, and let $\varphi(x, y) \equiv \exists z\, \psi(x, y, z)$ with $\psi \in \Pi^0_n$, such that $\forall x < a\ \exists y\ \varphi(x, y)$. Using the pairing function of :ref{#fact-idelta0}, let
$$
\psi'(x, w) \equiv \forall u \leq w\ \forall v \leq w\ (w = \langle u, v \rangle \rightarrow \psi(x, u, v)).
$$
Since every $w$ is the pair of unique $u, v \leq w$, $\psi'(x, w)$ holds if and only if $\psi(x, u, v)$ for the components of $w$. Since exactly one pair $(u, v)$ satisfies $w = \langle u, v \rangle$, the prefix $\forall u \leq w\ \forall v \leq w\ (w = \langle u, v \rangle \rightarrow \cdot)$ amounts to substituting the components of $w$, and commutes with every quantifier of $\psi$: moving it down to the bounded matrix of $\psi$, $\psi'$ is equivalent to a $\Pi^0_n$ formula, without any use of collection. Now $\forall x < a\ \exists w\ \psi'(x, w)$, so $\mathsf B\Pi^0_n$ gives $b$ with $\forall x < a\ \exists w < b\ \psi'(x, w)$. If $w = \langle u, v \rangle < b$, then $u \leq w < b$ and $\varphi(x, u)$. So $\forall x < a\ \exists y < b\ \varphi(x, y)$.
:::
::::

::::exercise{difficulty=1}
The **strong induction** scheme for a formula $\varphi$ is $\forall x\, ((\forall y < x\ \varphi(y)) \rightarrow \varphi(x)) \rightarrow \forall x\, \varphi(x)$. Show that $\mathsf I\Sigma^0_n$ proves strong induction for $\Sigma^0_n$ formulas, for every $n \geq 1$.

:::solution
Let $\varphi \in \Sigma^0_n$ satisfy the hypothesis, and fix $z$. Let $\theta(x) \equiv x \leq z \rightarrow \forall y < x\ \varphi(y)$. By :ref{#thm-induction-collection} and :ref{#lem-collection-closure}, $\theta$ is equivalent to a $\Sigma^0_n$ formula. We have $\theta(0)$. If $\theta(x)$ and $x + 1 \leq z$, then $\forall y < x\ \varphi(y)$, so $\varphi(x)$ by hypothesis, and $\forall y < x + 1\ \varphi(y)$: this is $\theta(x+1)$. By $\mathsf I\Sigma^0_n$, $\theta(z)$ holds, so $\forall y < z\ \varphi(y)$, and $\varphi(z)$ by hypothesis.
:::
::::

## Notes and references

The hierarchy of induction and collection schemes is due to Paris and Kirby (1978), building on Parsons (1970), who showed that $\mathrm I\Sigma_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic. Hájek and Pudlák's monograph is the standard reference; Kaye's book gives a model-theoretic introduction.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I.2 and Chapter IV.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, Chapters 2 and 10.
- T. A. Slaman, *Σₙ-bounding and Δₙ-induction*, Proceedings of the American Mathematical Society 132 (2004), 2449–2456.
