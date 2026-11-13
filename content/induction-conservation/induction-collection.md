---
title: Induction, collection and least numbers
summary: The schemes of Σ⁰ₙ and Π⁰ₙ induction, collection and least number principles; closure of the classes Σ⁰ₙ under bounded quantification in the presence of collection; Σ⁰ₙ and Π⁰ₙ induction are equivalent; Σ⁰ₙ induction implies Σ⁰ₙ collection and the least number principles.
duration: 50
prerequisites: [second-order-arithmetic/rca0]
---

In an ω-model, every form of induction holds, because the first-order part is the true $\nat$. In a model with non-standard numbers, induction may fail for complicated formulas: a formula may define a proper initial segment closed under successor, a **cut**, which contains $0$ but not every number. The axioms of $\mathsf{RCA}_0$ only grant induction for $\Sigma^0_1$ formulas, and many principles of ordinary mathematics turn out to be equivalent to forms of induction or of the related **collection** principle. This lesson and the next two set up the hierarchy of these schemes, following Paris and Kirby. This lesson proves that $\Sigma^0_n$ induction gives $\Pi^0_n$ induction, $\Sigma^0_n$ collection and the least number principles. The next lesson proves that collection gives induction one level down, and the third one that the resulting hierarchy is strict.

The proofs of this lesson all follow one pattern, which recurs in the whole course: to prove an instance of a scheme, one applies induction to an auxiliary formula, and the work consists in checking that the auxiliary formula still has the complexity allowed by the induction available. The main tool for this check is :ref{#lem-collection-closure}.

## The schemes

All formulas are formulas of $\mathcal L_2$, with number and set parameters (:ref{#def-l2}); the classes $\Sigma^0_n$ and $\Pi^0_n$ count blocks of quantifiers of the same kind as one, and their formulas are in prenex form with a bounded matrix.

:::definition{#def-induction-schemes}
Let $n \geq 0$ and $\Gamma$ be $\Sigma^0_n$ or $\Pi^0_n$. For every formula $\varphi \in \Gamma$, the universal closures of the following formulas form respectively the schemes $\mathsf I\Gamma$, $\mathsf B\Gamma$ and $\mathsf L\Gamma$:

1. **induction**: $(\varphi(0) \wedge \forall x\, (\varphi(x) \rightarrow \varphi(x+1))) \rightarrow \forall x\, \varphi(x)$;
2. **collection**: $\forall x < a\ \exists y\ \varphi(x, y) \rightarrow \exists b\ \forall x < a\ \exists y < b\ \varphi(x, y)$;
3. **least number principle**: $\exists x\, \varphi(x) \rightarrow \exists x\, (\varphi(x) \wedge \forall y < x\ \neg \varphi(y))$.

The theory $\mathsf I\Delta^0_0$ consists of the basic axioms (:ref{#def-z2}) and the scheme $\mathsf I\Sigma^0_0$ of induction for bounded formulas.
:::

The formula $\varphi$ may contain other free variables, which act as parameters. Collection says that a "finite" family of nonempty sets of witnesses has a common bound; here finite means indexed by the numbers below some $a$, which may be non-standard. In the true $\nat$, every instance of the three schemes holds. All theories in this course extend $\mathsf I\Delta^0_0$, and $\mathsf{RCA}_0$ contains $\mathsf I\Sigma^0_1$.

:::example{#ex-scheme-instances}
1. Let $\delta(x, y)$ be a bounded formula expressing that $y$ codes the sequence $(2^0, 2^1, \dots, 2^x)$, using the coding of finite sequences of $\mathsf{RCA}_0$. The instance of $\mathsf I\Sigma^0_1$ for $\exists y\ \delta(x, y)$ proves that exponentiation is total: the sequence for $x + 1$ is obtained from the sequence for $x$ by appending one term. By a theorem of Parikh (1971), which we admit, $\mathsf I\Delta^0_0$ does not prove that exponentiation is total: if $\mathsf I\Delta^0_0$ proves $\forall x\ \exists y\ \delta(x, y)$ with $\delta$ bounded, then $y$ can be bounded by a polynomial in $x$, whereas here $y \geq 2^x$. The difference between $\mathsf I\Delta^0_0$ and $\mathsf I\Sigma^0_1$ is thus a difference in the functions that can be proved total.
2. Let $a$ be a standard number $k$. If $\forall x < k\ \exists y\ \varphi(x, y)$, the basic axioms on $<$ show that the numbers below $k$ are $0, 1, \dots, k - 1$, and the maximum of $k$ witnesses, plus one, is a common bound. So every instance of collection with a standard bound is provable in $\mathsf I\Delta^0_0$, by a proof with $k$ cases. The scheme has content only for non-standard $a$, and only in non-standard models.
:::

:::fact{#fact-idelta0}
$\mathsf I\Delta^0_0$ proves the elementary properties of addition, multiplication and order: $<$ is a discrete linear order with least element $0$, every $x \neq 0$ is $y + 1$ for a unique $y$, $x \leq y$ if and only if $x + z = y$ for some $z$, which is then unique, polynomials with non-negative coefficients are monotone, and the pairing function $\langle u, v \rangle = \frac{(u + v)(u + v + 1)}{2} + v$ is a bijection, definable by a bounded formula, with $u, v \leq \langle u, v \rangle$.
:::

These properties are proved by bounded induction, in the same way as in Peano arithmetic; see Hájek and Pudlák, *Metamathematics of First-Order Arithmetic*, Chapter I. We use them freely.

## Bounded quantifiers and collection

A formula obtained from $\Sigma^0_n$ formulas by conjunction, disjunction, bounded quantification and existential quantification is not $\Sigma^0_n$ in general, because a bounded universal quantifier cannot be moved across an unbounded existential one. In the true $\nat$, $\forall x < a\ \exists y\ \varphi$ is equivalent to $\exists b\ \forall x < a\ \exists y < b\ \varphi$; this equivalence is exactly an instance of collection.

:::lemma[Parsons]{#lem-collection-closure}
Let $n \geq 1$. Over $\mathsf I\Delta^0_0 + \mathsf B\Sigma^0_n$:

1. every formula obtained from $\Sigma^0_n$ formulas by $\wedge$, $\vee$, bounded quantifiers $\exists x < t$, $\forall x < t$ and existential quantifiers is provably equivalent to a $\Sigma^0_n$ formula;
2. every formula obtained from $\Pi^0_n$ formulas by $\wedge$, $\vee$, bounded quantifiers and universal quantifiers is provably equivalent to a $\Pi^0_n$ formula.
:::

:::proof{of=lem-collection-closure}
Item 2 follows from item 1 by negation, since the negation of a $\Sigma^0_n$ formula is logically equivalent to a $\Pi^0_n$ formula. It suffices to treat one operation at a time. By renaming bound variables, $\exists y\, \alpha \wedge \exists z\, \beta$ is equivalent to $\exists y\, \exists z\, (\alpha \wedge \beta)$, and similarly for $\vee$; $\exists x < t\ \exists y\, \alpha$ is equivalent to $\exists y\ \exists x < t\ \alpha$; and an existential quantifier merges with the first block. We may also assume that the first block of a $\Sigma^0_n$ formula consists of a single quantifier: $\exists y_1\, \exists y_2\, \alpha$ is equivalent to $\exists w\ \exists y_1 < w\ \exists y_2 < w\ \alpha$, and $\exists y_1 < w\ \exists y_2 < w\ \alpha$, with $\alpha \in \Pi^0_{n-1}$, is bounded if $n = 1$ and equivalent to a $\Pi^0_{n-1}$ formula by item 2 for $n - 1$ if $n \geq 2$, in the induction below. The only non-trivial case is the bounded universal quantifier. We proceed by induction on $n$.

For $n = 1$, let $\varphi = \exists y\, \delta(x, y)$ with $\delta$ bounded. Then $\forall x < t\ \exists y\ \delta$ implies $\exists b\ \forall x < t\ \exists y < b\ \delta$ by $\mathsf B\Sigma^0_1$, and the converse is logical. The second formula is $\Sigma^0_1$.

Let $n \geq 1$, assume the lemma for $n$, and assume $\mathsf B\Sigma^0_{n+1}$, which contains $\mathsf B\Sigma^0_n$. A $\Sigma^0_{n+1}$ formula has the form $\exists y\, \psi$ with $\psi \in \Pi^0_n$. Conjunctions and disjunctions of $\Pi^0_n$ formulas, and bounded quantifications of them, are equivalent to $\Pi^0_n$ formulas by item 2 for $n$; so the easy cases above stay within $\Sigma^0_{n+1}$. For the bounded universal quantifier, $\forall x < t\ \exists y\ \psi(x, y)$ is equivalent to $\exists b\ \forall x < t\ \exists y < b\ \psi(x, y)$ by $\mathsf B\Sigma^0_{n+1}$ applied to $\psi$, which is $\Sigma^0_{n+1}$. By item 2 for $n$, $\forall x < t\ \exists y < b\ \psi$ is equivalent to a $\Pi^0_n$ formula, so the whole formula is equivalent to a $\Sigma^0_{n+1}$ formula.
:::

The lemma is the reason why collection appears at all in this course: whenever an argument puts a bounded quantifier in front of a $\Sigma^0_n$ formula, the result has the expected complexity only in the presence of $\mathsf B\Sigma^0_n$. The results of this lesson show that $\mathsf I\Sigma^0_n$ provides it.

## Σ⁰ₙ and Π⁰ₙ induction

:::theorem[Paris, Kirby]{#thm-isigma-ipi}
For every $n \geq 1$, $\mathsf I\Delta^0_0$ proves that $\mathsf I\Sigma^0_n$ and $\mathsf I\Pi^0_n$ are equivalent.
:::

The idea is to run the induction backwards. To derive a $\Pi^0_n$ instance from $\Sigma^0_n$ induction, assume that $\varphi$ fails at some $a$; the $\Sigma^0_n$ property "$\varphi$ fails at $a - y$" then propagates from $y = 0$ up to $y = a$, and gives a failure at $0$.

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

Both formulas $\theta$ and $\eta$ have the same complexity as the negation of $\varphi$, which is why the trick exchanges $\Sigma^0_n$ and $\Pi^0_n$. The guard $y \leq a$ is needed because the subtraction $a - y$ only makes sense below $a$.

## Induction implies collection

:::theorem[Paris, Kirby]{#thm-induction-collection}
For every $n \geq 1$, $\mathsf I\Delta^0_0 + \mathsf I\Sigma^0_n$ proves $\mathsf B\Sigma^0_n$.
:::

The proof finds the common bound by induction on the size of the family: if the witnesses for $x < c$ are bounded by $b$, those for $x < c + 1$ are bounded by $\max(b, w + 1)$, where $w$ is a witness for $c$. The formula "the witnesses for $x < c$ have a common bound" begins with $\exists b$, so it is $\Sigma^0_n$ provided the bounded quantifier $\forall x < c$ in front of the witness condition can be absorbed; for this the proof uses collection one level down, which is available by induction on $n$.

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

## Exercises

::::exercise{difficulty=1}
The **strong induction** scheme for a formula $\varphi$ is $\forall x\, ((\forall y < x\ \varphi(y)) \rightarrow \varphi(x)) \rightarrow \forall x\, \varphi(x)$. Show that $\mathsf I\Sigma^0_n$ proves strong induction for $\Sigma^0_n$ formulas, for every $n \geq 1$.

:::solution
Let $\varphi \in \Sigma^0_n$ satisfy the hypothesis, and fix $z$. Let $\theta(x) \equiv x \leq z \rightarrow \forall y < x\ \varphi(y)$. By :ref{#thm-induction-collection} and :ref{#lem-collection-closure}, $\theta$ is equivalent to a $\Sigma^0_n$ formula. We have $\theta(0)$. If $\theta(x)$ and $x + 1 \leq z$, then $\forall y < x\ \varphi(y)$, so $\varphi(x)$ by hypothesis, and $\forall y < x + 1\ \varphi(y)$: this is $\theta(x+1)$. By $\mathsf I\Sigma^0_n$, $\theta(z)$ holds, so $\forall y < z\ \varphi(y)$, and $\varphi(z)$ by hypothesis.
:::
::::

## Notes and references

The first-order counterparts of these schemes, and the hierarchy of induction and collection in models of first-order arithmetic, are developed in the track on models of arithmetic (:ref{to="fragments-of-arithmetic/induction-collection"}).

The hierarchy of induction and collection schemes is due to Paris and Kirby (1978), building on Parsons (1970), who introduced the collection schemes, proved that collection closes the classes $\Sigma_n$ under bounded quantification, and showed that $\mathrm I\Sigma_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic. Dzhafarov and Mummert, Section 6.1, present the same material in the setting of reverse mathematics, with attributions; Hájek and Pudlák's monograph is the standard reference, and Kaye's book gives a model-theoretic introduction. Parikh introduced $\mathsf I\Delta^0_0$ and proved that it does not prove the totality of exponentiation.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- R. Parikh, *Existence and feasibility in arithmetic*, Journal of Symbolic Logic 36 (1971), 494–508.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 6.1.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 2.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, chapters *Collection* and *Subsystems of Peano arithmetic*.
