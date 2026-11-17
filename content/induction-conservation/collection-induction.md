---
title: Cuts, collection and the hierarchy
summary: Overspill in models of Σ⁰ₙ induction; Σ⁰ₙ₊₁ collection implies Σ⁰ₙ induction; the hierarchy IΣ⁰ₙ₊₁ ⇒ BΣ⁰ₙ₊₁ ⇒ IΣ⁰ₙ; Σ⁰ₙ₊₁ collection is Π⁰ₙ collection.
duration: 20
prerequisites: [induction-collection, second-order-arithmetic/nonstandard-models]
---

The previous lesson went up from induction: $\mathsf I\Sigma^0_n$ proves $\mathsf B\Sigma^0_n$. This lesson goes the other way: collection for $\Sigma^0_{n+1}$ formulas proves induction for $\Sigma^0_n$ formulas, so that induction and collection alternate in a single chain. Both directions are best understood in non-standard models, where a failure of induction is a definable cut. The lesson starts with this picture and its main consequence, the overspill principle.

## Cuts and overspill

The least number principle (:ref{#prop-least-number}) gives the model-theoretic meaning of induction. If $\mathsf I\Sigma^0_n$ fails, some $\Sigma^0_n$ formula $\varphi$ holds at $0$, is preserved by successor, and fails somewhere. The set $I$ of numbers below every failure contains $0$, is closed under successor, and is not the whole model: it is a **cut**, and the set of failures has no least element, since the predecessor of a least failure would satisfy $\varphi$.

:::figure[A failure of $\Sigma^0_n$ induction in a non-standard model. The formula $\varphi$ holds at $0$ and is preserved by successor, but fails at some non-standard numbers. The numbers below every failure form a cut $I$, which contains the standard numbers and some non-standard ones; the failures have no least element.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="A non-standard model in which a formula phi holds at 0, is preserved by successor, and fails at some non-standard numbers; the numbers below every failure form a cut, and the failures have no least element"><line x1="20" y1="70" x2="166" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="30" cy="70" r="3.5" class="accent-fill"/><text x="30" y="58" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="60" cy="70" r="3.5" class="accent-fill"/><text x="60" y="58" text-anchor="middle" class="mrm" font-size="13">1</text><circle cx="90" cy="70" r="3.5" class="accent-fill"/><text x="90" y="58" text-anchor="middle" class="mrm" font-size="13">2</text><circle cx="120" cy="70" r="3.5" class="accent-fill"/><text x="120" y="58" text-anchor="middle" class="mrm" font-size="13">3</text><circle cx="150" cy="70" r="3.5" class="accent-fill"/><text x="150" y="58" text-anchor="middle" class="mrm" font-size="13">4</text><text x="186" y="74" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="214" y1="70" x2="274" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="224" cy="70" r="3.5" class="accent-fill"/><circle cx="244" cy="70" r="3.5" class="accent-fill"/><circle cx="264" cy="70" r="3.5" class="accent-fill"/><text x="287" y="74" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="306" y1="70" x2="366" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="316" cy="70" r="3.5" class="accent-fill"/><circle cx="336" cy="70" r="3.5" class="accent-fill"/><circle cx="356" cy="70" r="3.5" class="accent-fill"/><text x="379" y="74" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="420" y1="70" x2="480" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="430" cy="70" r="3.5" class="node"/><circle cx="450" cy="70" r="3.5" class="node"/><circle cx="470" cy="70" r="3.5" class="node"/><text x="493" y="74" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="504" y1="70" x2="564" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="514" cy="70" r="3.5" class="node"/><circle cx="534" cy="70" r="3.5" class="node"/><circle cx="554" cy="70" r="3.5" class="node"/><text x="577" y="74" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="404" y1="40" x2="404" y2="100" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><path d="M22,90 L22,96 L392,96 L392,90" class="muted-stroke" stroke-width="1.2"/><text x="207.0" y="114" text-anchor="middle" class="label">the cut I: numbers below every failure</text><path d="M416,90 L416,96 L584,96 L584,90" class="muted-stroke" stroke-width="1.2"/><text x="500.0" y="114" text-anchor="middle" class="label">failures: no least element</text><path d="M22,46 L22,40 L170,40 L170,46" class="muted-stroke" stroke-width="1.2"/><text x="96.0" y="30" text-anchor="middle" class="label">standard numbers</text><circle cx="150" cy="146" r="3.5" class="accent-fill"/><text x="160" y="150" class="label">φ holds</text><circle cx="300" cy="146" r="3.5" class="node"/><text x="310" y="150" class="label">φ fails</text></svg>
:::

Conversely, in a model of $\mathsf I\Sigma^0_n$, no $\Sigma^0_n$ or $\Pi^0_n$ formula, with parameters, defines a proper cut. In particular, in a non-standard model of $\mathsf I\Sigma^0_n$, the standard numbers $\{ 0, 1, 2, \dots \}$ form a cut, so they are not definable by such a formula. For $n = 1$ this is the overspill principle of the course on second-order arithmetic (:ref{#prop-overspill}); the same proof gives it at every level.

:::proposition[Overspill for Σ⁰ₙ formulas]{#prop-overspill-n}
Let $n \geq 1$, let $\mathcal M$ be a non-standard model of $\mathsf I\Delta^0_0 + \mathsf I\Sigma^0_n$, and let $\varphi(x)$ be a $\Sigma^0_n$ or $\Pi^0_n$ formula with parameters in $\mathcal M$. If $\mathcal M \models \varphi(k)$ for every standard $k$, then $\mathcal M \models \varphi(c)$ for some non-standard $c$.
:::

:::proof{of=prop-overspill-n}
Suppose that $\varphi(c)$ fails for every non-standard $c$. Then $\varphi$ defines the set of standard numbers in $\mathcal M$, which contains $0$ and is closed under successor, since the successor of a standard number is standard. By $\mathsf I\Sigma^0_n$, or $\mathsf I\Pi^0_n$ by :ref{#thm-isigma-ipi}, $\varphi$ holds at every element of $\mathcal M$, including the non-standard ones: a contradiction.
:::

The hypothesis on the complexity of $\varphi$ cannot be dropped: the model of $\mathsf B\Sigma^0_n + \neg \mathsf I\Sigma^0_n$ of the next lesson (:ref{#thm-bsigma-not-isigma}) satisfies $\mathsf I\Sigma^0_{n-1}$, and its standard numbers are defined in it by a $\Sigma^0_n$ formula, so overspill fails there for this $\Sigma^0_n$ formula (Dzhafarov and Mummert, proof of Theorem 6.3.5).

## Collection implies induction

:::theorem[Paris, Kirby]{#thm-collection-induction}
For every $n \geq 1$, $\mathsf I\Delta^0_0 + \mathsf B\Sigma^0_{n+1}$ proves $\mathsf I\Sigma^0_n$.
:::

To prove $\varphi(a)$ for a $\Sigma^0_n$ formula $\varphi = \exists y\, \psi$ by induction, one would like to carry along the witnesses $y$. The step from $x$ to $x + 1$ produces a new witness, but nothing bounds it uniformly. Collection, applied to the whole family of steps below $a$, gives a single bound $b$ on the witnesses that are needed; once the witnesses are bounded by $b$, the statement "$\varphi(x)$ has a witness below $b$" has lower complexity, and the induction available one level down applies.

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

---

Why does the disjunct $\forall y\, \neg \psi(x, y)$ appear in the formula to which collection is applied?

- [x] Because collection needs a witness $u$ for every $x \leq a$, and $\varphi(x + 1)$ is only known when $\varphi(x)$ holds; the disjunct makes the formula true, with any $u$, at the $x$ where $\varphi(x)$ fails.
- [ ] To make the formula $\Pi^0_n$.

  Without the disjunct, $\psi(x + 1, u)$ is $\Pi^0_{n-1}$, which is simpler; the disjunct raises the complexity to $\Pi^0_n$, which is why collection for $\Sigma^0_{n+1}$ formulas is needed.
- [ ] Because $\varphi(x)$ fails for some $x \leq a$.

  The proof shows that $\varphi(x)$ holds for every $x \leq a$; the disjunct is needed before this is known.
:::

The third question explains the shift of index: the formula to which collection is applied quantifies over all potential witnesses of $\varphi(x)$, which costs one quantifier more than $\varphi$ itself.

## The hierarchy

Together with :ref{#thm-induction-collection}, the theorem gives, for every $n \geq 1$, over $\mathsf I\Delta^0_0$:
$$
\mathsf I\Sigma^0_{n+1} \;\Rightarrow\; \mathsf B\Sigma^0_{n+1} \;\Rightarrow\; \mathsf I\Sigma^0_n \;\Rightarrow\; \mathsf B\Sigma^0_n.
$$
By :ref{#prop-least-number}, each $\mathsf I\Sigma^0_n$ may be replaced by $\mathsf I\Pi^0_n$, $\mathsf L\Sigma^0_n$ or $\mathsf L\Pi^0_n$, and by :ref{#ex-bsigma-bpi} below, each $\mathsf B\Sigma^0_{n+1}$ by $\mathsf B\Pi^0_n$.

:::figure[The hierarchy of induction and collection, over $\mathsf I\Delta^0_0 = \mathsf I\Sigma^0_0$; each scheme implies the one to its left. None of the implications reverses. Below, the position of some systems of the reverse mathematics track: the first-order parts of $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$ are $\mathrm I\Sigma_1$ (lessons on first-order parts and on Harrington's theorem); $\mathsf{RT}^2_2$ proves $\mathsf B\Sigma^0_2$ but not $\mathsf I\Sigma^0_2$ (lesson on the pigeonhole principle); $\mathsf{ACA}_0$ proves induction for all arithmetic formulas.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="The chain I Sigma 0, B Sigma 1, I Sigma 1, B Sigma 2, I Sigma 2, B Sigma 3, each implied by the next one; the implications from B Sigma n+1 to I Sigma n are strict by the models of definable elements; RCA0 and WKL0 prove I Sigma 1, RT22 proves B Sigma 2 but not I Sigma 2"><defs><marker id="ic-h-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="18" y="70" width="62" height="34" rx="4" class="cell"/><text x="49.0" y="92.0" text-anchor="middle" class="mrm" font-size="16">IΣ<tspan font-size="10" dy="5">0</tspan></text><rect x="106" y="70" width="62" height="34" rx="4" class="cell"/><text x="137.0" y="92.0" text-anchor="middle" class="mrm" font-size="16">BΣ<tspan font-size="10" dy="5">1</tspan></text><rect x="194" y="70" width="62" height="34" rx="4" class="cell"/><text x="225.0" y="92.0" text-anchor="middle" class="mrm" font-size="16">IΣ<tspan font-size="10" dy="5">1</tspan></text><rect x="282" y="70" width="62" height="34" rx="4" class="cell"/><text x="313.0" y="92.0" text-anchor="middle" class="mrm" font-size="16">BΣ<tspan font-size="10" dy="5">2</tspan></text><rect x="370" y="70" width="62" height="34" rx="4" class="cell"/><text x="401.0" y="92.0" text-anchor="middle" class="mrm" font-size="16">IΣ<tspan font-size="10" dy="5">2</tspan></text><rect x="458" y="70" width="62" height="34" rx="4" class="cell"/><text x="489.0" y="92.0" text-anchor="middle" class="mrm" font-size="16">BΣ<tspan font-size="10" dy="5">3</tspan></text><line x1="104" y1="87" x2="84" y2="87" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-h-arrow)"/><line x1="192" y1="87" x2="172" y2="87" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-h-arrow)"/><line x1="280" y1="87" x2="260" y2="87" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-h-arrow)"/><line x1="368" y1="87" x2="348" y2="87" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-h-arrow)"/><line x1="456" y1="87" x2="436" y2="87" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-h-arrow)"/><text x="534" y="92" class="mrm" font-size="15">⋯</text><line x1="93.0" y1="106" x2="93.0" y2="122" class="accent-stroke" stroke-width="1.2"/><line x1="269.0" y1="106" x2="269.0" y2="122" class="accent-stroke" stroke-width="1.2"/><line x1="445.0" y1="106" x2="445.0" y2="122" class="accent-stroke" stroke-width="1.2"/><text x="269.0" y="138" text-anchor="middle" class="label">strict: models of definable elements (next lesson)</text><line x1="181.0" y1="68" x2="181.0" y2="54" class="muted-stroke" stroke-width="1.2"/><line x1="357.0" y1="68" x2="357.0" y2="54" class="muted-stroke" stroke-width="1.2"/><text x="269.0" y="48" text-anchor="middle" class="label">strict as well (Paris and Kirby; admitted)</text><text x="225.0" y="174" text-anchor="middle" class="label">RCA₀, WKL₀</text><line x1="225.0" y1="160" x2="225.0" y2="150" class="muted-stroke" stroke-dasharray="2 2"/><text x="323.0" y="174" text-anchor="middle" class="label">RT²₂ (not IΣ₂)</text><line x1="313.0" y1="160" x2="313.0" y2="150" class="muted-stroke" stroke-dasharray="2 2"/><text x="540" y="174" text-anchor="end" class="label">ACA₀: all of them</text></svg>
:::

None of these implications reverses. The next lesson builds, for every $n \geq 0$, a model of $\mathsf I\Sigma^0_n$ in which $\mathsf B\Sigma^0_{n+1}$ fails; models of $\mathsf B\Sigma^0_n$ in which $\mathsf I\Sigma^0_n$ fails also exist, and are admitted. A finer analysis is due to Slaman (2004): over $\mathsf I\Delta^0_0$ together with the totality of exponentiation, $\mathsf B\Sigma^0_n$ is equivalent to induction for $\Delta^0_n$ formulas, that is, for $\Sigma^0_n$ formulas that are equivalent, in the model at hand, to $\Pi^0_n$ formulas. So collection is itself an induction scheme, for a class of formulas that contains the $\Sigma^0_{n-1}$ and $\Pi^0_{n-1}$ formulas and is contained in $\Sigma^0_n$.

::::exercise{#ex-bsigma-bpi difficulty=1 objective="Contract a block of existential quantifiers with the pairing function, to reduce $\Sigma^0_{n+1}$ collection to $\Pi^0_n$ collection."}
Show that, over $\mathsf I\Delta^0_0$, $\mathsf B\Sigma^0_{n+1}$ is equivalent to $\mathsf B\Pi^0_n$ for every $n \geq 1$.

:::solution
Every $\Pi^0_n$ formula is $\Sigma^0_{n+1}$, so $\mathsf B\Sigma^0_{n+1}$ implies $\mathsf B\Pi^0_n$. Conversely, assume $\mathsf B\Pi^0_n$, and let $\varphi(x, y) \equiv \exists z\, \psi(x, y, z)$ with $\psi \in \Pi^0_n$, such that $\forall x < a\ \exists y\ \varphi(x, y)$. Using the pairing function of :ref{#fact-idelta0}, let
$$
\psi'(x, w) \equiv \forall u \leq w\ \forall v \leq w\ (w = \langle u, v \rangle \rightarrow \psi(x, u, v)).
$$
Since every $w$ is the pair of unique $u, v \leq w$, $\psi'(x, w)$ holds if and only if $\psi(x, u, v)$ for the components of $w$. Since exactly one pair $(u, v)$ satisfies $w = \langle u, v \rangle$, the prefix $\forall u \leq w\ \forall v \leq w\ (w = \langle u, v \rangle \rightarrow \cdot)$ amounts to substituting the components of $w$, and commutes with every quantifier of $\psi$: moving it down to the bounded matrix of $\psi$, $\psi'$ is equivalent to a $\Pi^0_n$ formula, without any use of collection. Now $\forall x < a\ \exists w\ \psi'(x, w)$, so $\mathsf B\Pi^0_n$ gives $b$ with $\forall x < a\ \exists w < b\ \psi'(x, w)$. If $w = \langle u, v \rangle < b$, then $u \leq w < b$ and $\varphi(x, u)$. So $\forall x < a\ \exists y < b\ \varphi(x, y)$.
:::
::::

## Notes and references

The implication from collection to induction is due to Paris and Kirby (1978), as is the strictness of the hierarchy, proved in the next lesson; Dzhafarov and Mummert (Theorem 6.1.3 and Section 6.3) give both, with attributions, and call it the Kirby–Paris hierarchy.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 6.1–6.3.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 2, and Chapter IV.
- T. A. Slaman, *Σₙ-bounding and Δₙ-induction*, Proceedings of the American Mathematical Society 132 (2004), 2449–2456.

:::::exercises
::::exercise{#ex-overspill-diagonal difficulty=2 objective="Apply overspill to a bounded formula with a set parameter, to extend a property of the standard numbers to a non-standard initial segment."}
Let $\mathcal M$ be a non-standard model of $\mathsf I\Delta^0_0 + \mathsf I\Sigma^0_1$ and $f \in \mathcal M$ a function with $f(k) \leq k$ for every standard $k$. Show that there is a non-standard $c$ with $f(x) \leq x$ for every $x \leq c$.

:::solution
Since $f$ is a function, $f(x) \leq x$ is expressed by the bounded formula $\exists y \leq x\ (\langle x, y \rangle \in f)$. So $\varphi(c) \equiv \forall x \leq c\ \exists y \leq x\ (\langle x, y \rangle \in f)$ is bounded, with parameter $f$, hence $\Sigma^0_1$. For every standard $k$, $\varphi(k)$ holds, since every $x \leq k$ is standard. By :ref{#prop-overspill-n}, $\varphi(c)$ holds for some non-standard $c$.
:::
::::

::::exercise{#ex-ldelta0-lsigma difficulty=2 objective="Check that bounded induction gives the least number principle for bounded formulas, and place the least number principles below collection."}
Show that $\mathsf I\Delta^0_0$ proves the least number principle $\mathsf L\Delta^0_0$ for bounded formulas. Deduce that $\mathsf I\Delta^0_0 + \mathsf B\Sigma^0_{n+1}$ proves $\mathsf L\Sigma^0_n$ for every $n \geq 0$.

:::solution
Given a bounded $\varphi$ with $\varphi(c)$ and no least witness, the formula $\forall y \leq x\ \neg \varphi(y)$ is bounded, holds at $0$, and is preserved by successor, as in the proof of :ref{#prop-least-number}; bounded induction then gives $\neg \varphi(c)$. No collection is needed, because a bounded quantifier in front of a bounded formula gives a bounded formula. For $n \geq 1$, $\mathsf B\Sigma^0_{n+1}$ proves $\mathsf I\Sigma^0_n$ by :ref{#thm-collection-induction}, which proves $\mathsf L\Sigma^0_n$ by :ref{#prop-least-number}; for $n = 0$, $\mathsf L\Sigma^0_0$ is $\mathsf L\Delta^0_0$.
:::
::::

::::exercise{#ex-strong-collection difficulty=2 objective="Show that the strong form of collection, which needs no hypothesis on the instance, already implies induction at the same level."}
The **strong collection** scheme for a formula $\varphi(x, y)$ is
$$
\forall a\ \exists b\ \forall x < a\ \bigl(\exists y\ \varphi(x, y) \rightarrow \exists y < b\ \varphi(x, y)\bigr).
$$
Unlike $\mathsf B\Sigma^0_n$, it makes no assumption on the $x < a$: it bounds the witnesses of those $x$ that have one. Let $n \geq 1$. Show that $\mathsf I\Delta^0_0$ together with strong collection for $\Pi^0_{n-1}$ formulas (bounded formulas if $n = 1$) proves $\mathsf I\Sigma^0_n$.

:::solution
Strong collection for a formula implies collection for it: if every $x < a$ has a witness, the bound $b$ works for all of them. For $n \geq 2$ we first collect the induction and collection available one level down. The hypothesis contains $\mathsf B\Pi^0_{n-1}$, which is equivalent to $\mathsf B\Sigma^0_n$ by :ref{#ex-bsigma-bpi}; so $\mathsf I\Sigma^0_{n-1}$ holds by :ref{#thm-collection-induction}, hence $\mathsf B\Sigma^0_{n-1}$ by :ref{#thm-induction-collection} and $\mathsf I\Pi^0_{n-1}$ by :ref{#thm-isigma-ipi}.

Now let $\varphi(x) \equiv \exists y\, \psi(x, y)$ with $\psi \in \Pi^0_{n-1}$ (bounded if $n = 1$), suppose $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$, and fix $a$. Strong collection for $\psi$, with the bound $a + 1$, gives $b$ such that every $x \leq a$ with $\varphi(x)$ has a witness $y < b$. Let
$$
\theta(x) \equiv x \leq a \rightarrow \exists y < b\ \psi(x, y).
$$
For $n = 1$ it is bounded; for $n \geq 2$ it is equivalent to a $\Pi^0_{n-1}$ formula by :ref{#lem-collection-closure}. Since $\varphi(0)$ holds, $0$ has a witness below $b$, so $\theta(0)$. If $\theta(x)$ and $x + 1 \leq a$, then $\varphi(x)$, hence $\varphi(x + 1)$, and $x + 1 \leq a$ has a witness below $b$: $\theta(x + 1)$. By $\mathsf I\Delta^0_0$ or $\mathsf I\Pi^0_{n-1}$, $\theta(a)$ holds, so $\varphi(a)$.

The proof is that of :ref{#thm-collection-induction}, where the disjunct $\forall y\, \neg \psi(x, y)$ was needed to apply ordinary collection; strong collection makes it unnecessary, which is why no index is lost. Conversely, $\mathsf I\Sigma^0_n$ proves strong collection for $\Pi^0_{n-1}$ formulas. Adapted from Hájek and Pudlák, Chapter I, Lemma 2.29; Lemma 2.27 there proves the converse.
:::
::::

::::exercise{#ex-bounded-functions difficulty=2 objective="Characterize $\Sigma^0_n$ collection by the boundedness of $\Sigma^0_n$-definable functions on bounded domains, using least witnesses."}
Let $n \geq 1$, and write $\mathsf I\Sigma^0_0$ for $\mathsf I\Delta^0_0$. Show that over $\mathsf I\Delta^0_0 + \mathsf I\Sigma^0_{n-1}$, $\mathsf B\Sigma^0_n$ is equivalent to the following statement, for all $\Sigma^0_n$ formulas $\theta(x, y)$: if $\forall x < a\ \exists! y\ \theta(x, y)$, then $\exists c\ \forall x < a\ \exists y < c\ \theta(x, y)$. In words: a $\Sigma^0_n$-definable function on $[0, a)$ has a bounded range.

:::solution
Collection implies the statement, since $\exists!$ implies $\exists$. Conversely, assume the statement. By :ref{#ex-bsigma-bpi}, or by the same contraction of quantifiers when $n = 1$, it suffices to prove $\mathsf B\Pi^0_{n-1}$ (collection for bounded formulas if $n = 1$). Let $\varphi(x, y)$ be $\Pi^0_{n-1}$ with $\forall x < a\ \exists y\ \varphi(x, y)$, and let
$$
\theta(x, y) \equiv x < a \wedge \varphi(x, y) \wedge \forall y' < y\ \neg \varphi(x, y').
$$
For $n = 1$ it is bounded. For $n \geq 2$, $\mathsf I\Sigma^0_{n-1}$ proves $\mathsf B\Sigma^0_{n-1}$ (:ref{#thm-induction-collection}), so the last conjunct, a bounded universal quantifier in front of a $\Sigma^0_{n-1}$ formula, is equivalent to a $\Sigma^0_{n-1}$ formula (:ref{#lem-collection-closure}), and $\theta$, a conjunction of $\Pi^0_{n-1}$ and $\Sigma^0_{n-1}$ formulas, is equivalent to a $\Sigma^0_n$ formula.

For $x < a$, there is a least $y$ with $\varphi(x, y)$: by $\mathsf L\Delta^0_0$ (:ref{#ex-ldelta0-lsigma}) if $n = 1$, and by $\mathsf L\Pi^0_{n-1}$ (:ref{#prop-least-number}) if $n \geq 2$. It satisfies $\theta(x, y)$, and it is the only such $y$: if $y_1 < y_2$ both satisfied $\theta(x, \cdot)$, the last conjunct for $y_2$ would give $\neg \varphi(x, y_1)$. So $\forall x < a\ \exists! y\ \theta(x, y)$, and the statement gives $c$ with $\forall x < a\ \exists y < c\ \theta(x, y)$, hence $\forall x < a\ \exists y < c\ \varphi(x, y)$.

Adapted from Dzhafarov and Mummert, Proposition 6.2.4.
:::
::::

::::exercise{#ex-overspill-columns difficulty=1 objective="Apply overspill at the right level of the hierarchy to a $\Pi^0_2$ property."}
Let $\mathcal M$ be a non-standard model of $\mathsf{RCA}_0 + \mathsf I\Sigma^0_2$, and $X$ a set of $\mathcal M$ such that, for every standard $i$, the column $X^{[i]} = \{ j : \langle i, j \rangle \in X \}$ is unbounded in $M$. Show that there is a non-standard $c$ such that $X^{[i]}$ is unbounded for every $i \leq c$. Why does the overspill principle of the course on second-order arithmetic (:ref{#prop-overspill}) not suffice?

:::solution
Let $\psi(c) \equiv \forall i \leq c\ \forall m\ \exists j\ (j > m \wedge \langle i, j \rangle \in X)$. The bounded quantifier $\forall i \leq c$ merges with $\forall m$, so $\psi$ is a $\Pi^0_2$ formula with parameter $X$. For a standard $c$, every $i \leq c$ is standard, so $\psi(c)$ holds. By :ref{#prop-overspill-n} with $n = 2$, $\psi(c)$ holds for some non-standard $c$.

:ref{#prop-overspill} concerns $\Sigma^0_1$ and $\Pi^0_1$ formulas and uses only $\mathsf I\Sigma^0_1$; the property "the column $i$ is unbounded" is $\Pi^0_2$, and overspill for it requires $\mathsf I\Sigma^0_2$.
:::
::::

::::exercise{#ex-overspill-limits difficulty=2 objective="Combine Parsons' lemma with overspill for a $\Sigma^0_2$ property involving a bounded universal quantifier."}
Let $\mathcal M$ be a non-standard model of $\mathsf{RCA}_0 + \mathsf I\Sigma^0_2$, and $f : M \times M \to M$ a function of $\mathcal M$ such that, for every standard $x$, the limit $\lim_s f(x, s)$ exists in $\mathcal M$, that is, $\mathcal M \models \exists t\ \forall s \geq t\ f(x, s) = f(x, t)$. Show that there is a non-standard $c$ such that $\lim_s f(x, s)$ exists for every $x \leq c$. Where is collection used?

:::solution
Since $f$ is a total function, $f(x, s) = f(x, t)$ is equivalent to the $\Pi^0_1$ formula $\forall u\ \forall v\ ((\langle \langle x, s \rangle, u \rangle \in f \wedge \langle \langle x, t \rangle, v \rangle \in f) \rightarrow u = v)$. So $\lambda(x) \equiv \exists t\ \forall s\ (s < t \vee f(x, s) = f(x, t))$ is equivalent to a $\Sigma^0_2$ formula. The formula $\psi(c) \equiv \forall x \leq c\ \lambda(x)$ puts a bounded universal quantifier in front of it. Since $\mathcal M$ satisfies $\mathsf I\Sigma^0_2$, it satisfies $\mathsf B\Sigma^0_2$ (:ref{#thm-induction-collection}), and $\psi$ is equivalent in $\mathcal M$ to a $\Sigma^0_2$ formula by :ref{#lem-collection-closure}. For standard $c$, $\psi(c)$ holds by hypothesis, so by :ref{#prop-overspill-n} with $n = 2$, $\psi(c)$ holds for some non-standard $c$.

Collection is used to see that $\psi$ is $\Sigma^0_2$: without it, $\psi$ is only $\Pi^0_3$, and overspill at level 2 does not apply. Compare with :ref{#ex-overspill-columns}, where the property is $\Pi^0_2$ and the bounded quantifier is absorbed by logic.
:::
::::
:::::
