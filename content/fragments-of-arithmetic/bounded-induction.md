---
title: Bounded induction and cuts
summary: Induction schemes over PA⁻ and the theory IΔ₀; least number principle, division with remainder and pairing in IΔ₀; the order type of countable non-standard models of IΔ₀; cuts; cuts closed under addition and multiplication are models of IΔ₀.
duration: 40
prerequisites: [bounded-formulas]
---

The algebraic theory $\mathrm{PA}^-$ does not prove that every number is even or odd. Induction for bounded formulas, the weakest form of induction in this course, proves this and the elementary facts of number theory that involve quantities bounded by polynomials. This lesson develops bounded induction far enough to describe the order of its non-standard models, and introduces the central objects of the model theory of arithmetic: **cuts**, initial segments of a model closed under successor. Cuts closed under addition and multiplication are themselves models of bounded induction; the next lesson uses them to show that bounded induction proves nothing beyond polynomial growth.

## Induction schemes

:::definition{#def-induction-scheme}
Let $\Gamma$ be a class of formulas of $\mathcal L_A$. The **induction scheme** for $\Gamma$ consists of the universal closures of
$$
\big(\varphi(0, \bar p) \wedge \forall x\, (\varphi(x, \bar p) \rightarrow \varphi(x + 1, \bar p))\big) \rightarrow \forall x\ \varphi(x, \bar p)
$$
for $\varphi(x, \bar p) \in \Gamma$, and $\mathrm I\Gamma$ is $\mathrm{PA}^-$ together with this scheme. In particular, $\mathrm I\Delta_0$ is **bounded induction**, $\mathrm I\Sigma_n$ and $\mathrm I\Pi_n$ are $\Sigma_n$ and $\Pi_n$ induction, and **Peano arithmetic** $\mathrm{PA}$ is $\mathrm{PA}^-$ together with induction for all formulas.
:::

The variables $\bar p$ are **parameters**: in a model $M$, an instance says that a set defined by a formula of $\Gamma$ with parameters from $M$, if it contains $0$ and is closed under successor, contains every element of $M$. $\mathrm{PA}$ is equivalent to its usual axiomatization by the recursion equations for successor, addition and multiplication and induction, since induction proves the laws of $\mathrm{PA}^-$ (Hájek and Pudlák, Theorem I.1.10, for open induction); for the same reason $\mathrm I\Delta_0$ is the theory $\mathsf I\Delta^0_0$ of the course on induction and conservation, restricted to formulas without set variables.

:::proposition{#prop-idelta0-basic}
$\mathrm I\Delta_0$ proves:

1. the **least number principle** for $\Delta_0$ formulas: $\exists x\ \varphi(x) \rightarrow \exists x\, (\varphi(x) \wedge \forall y < x\ \neg \varphi(y))$, for every $\Delta_0$ formula $\varphi$, with parameters;
2. **division with remainder**: $0 < y \rightarrow \exists q < x + 1\ \exists r < y\ (x = q \cdot y + r)$, and $q$ and $r$ are unique;
3. every $x$ is even or odd: $\exists y < x + 1\ (x = y + y \vee x = y + y + 1)$.
:::

:::proof{of=prop-idelta0-basic}
1. Let $\varphi(c)$, and suppose that no $x$ is a least element satisfying $\varphi$. Let $\psi(x) \equiv \forall y < x + 1\ \neg \varphi(y)$, a $\Delta_0$ formula. Then $\psi(0)$, since otherwise $\varphi(0)$ and $0$ is least, nothing being below $0$. If $\psi(x)$ and $\varphi(x + 1)$, then $x + 1$ is least, since every $y < x + 1$ satisfies $y \leq x$ (:ref{#lem-pam-basic}); so $\psi(x) \rightarrow \psi(x + 1)$. By bounded induction, $\psi(c)$ holds, which contradicts $\varphi(c)$.

2. Fix $y > 0$ and apply induction on $x$ to the $\Delta_0$ formula $\exists q < x + 1\ \exists r < y\ (x = q y + r)$, with parameter $y$. For $x = 0$, take $q = r = 0$. Let $x = q y + r$ with $r < y$; then $r + 1 \leq y$. If $r + 1 < y$, then $x + 1 = q y + (r + 1)$. If $r + 1 = y$, then $x + 1 = (q + 1) y + 0$. In both cases the new quotient is at most $x + 1$, since $q \leq q y \leq x$. For uniqueness, if $q y + r = q' y + r'$ with $r, r' < y$ and $q < q'$, then $q' y \geq (q + 1) y = q y + y > q y + r$, so $q' y + r' > q y + r$, a contradiction; so $q = q'$, and $r = r'$ by cancellation of addition, which holds in $\mathrm{PA}^-$ by trichotomy and the monotonicity axiom.

3. Division by $2$ gives $x = 2 q + r$ with $r < 2$, so $r = 0$ or $r = 1$ by :ref{#lem-pam-basic}, and $2q = q + q$.
:::

The pattern of these proofs recurs in the whole course. To prove a statement by induction inside a weak theory, one chooses an auxiliary formula, here $\psi$ or the formula with the bounds $q < x + 1$ and $r < y$, and checks that it belongs to the class for which induction is available. A bound on the witnesses is what keeps the auxiliary formula bounded. The other elementary laws of arithmetic are obtained in the same way; we use in particular the following fact, whose proof is a similar computation.

:::fact[Pairing]{#fact-pairing}
Let $\langle x, y \rangle = \frac{(x + y)(x + y + 1)}{2} + y$. The relation $z = \langle x, y \rangle$ is defined by the $\Delta_0$ formula $z + z = (x + y)(x + y + 1) + y + y$, and $\mathrm I\Delta_0$ proves that it is a bijection between pairs and numbers, with $x, y \leq \langle x, y \rangle$, and that $\langle x, y \rangle < \langle x', y' \rangle$ whenever $x \leq x'$, $y \leq y'$ and $(x, y) \neq (x', y')$.
:::

Hájek and Pudlák prove this in open induction (Theorem I.1.18). Tuples are coded by iterated pairs, $\langle x_1, \dots, x_{k+1} \rangle = \langle \langle x_1, \dots, x_k \rangle, x_{k+1} \rangle$; this is the Cantor pairing function of the course on models of computation (:ref{#def-cantor-pairing}), now used inside arbitrary models.

## The order of a non-standard model

Division by two already determines the order of a countable non-standard model of $\mathrm I\Delta_0$. Call two elements $a, b$ of a model $M$ of $\mathrm{PA}^-$ **close** if $a \leq b + k$ and $b \leq a + k$ for some standard $k$. Closeness is an equivalence relation, and its classes, the **blocks**, are convex. The standard part is one block. By :ref{#ex-pam-predecessors}, every non-standard $a$ has predecessors $a - k$ for all standard $k$; so the block of a non-standard $a$ is $\{ a - k : k \in \nat \} \cup \{ a + k : k \in \nat \}$, ordered like $\mathbb Z$. The blocks are linearly ordered by the order of $M$.

:::theorem{#thm-order-type}
Let $M$ be a non-standard model of $\mathrm I\Delta_0$. The set of non-standard blocks of $M$, with the induced order, is a dense linear order without least or greatest element. If $M$ is countable, the order of $M$ is isomorphic to $\nat$ followed by $\mathbb Q$ copies of $\mathbb Z$, the order type written $\nat + \mathbb Z \cdot \mathbb Q$.
:::

:::proof{of=thm-order-type}
Let $a$ be non-standard. *No greatest block:* $a + a$ is not close to $a$, since $a + a \leq a + k$ would give $a \leq k$. *No least non-standard block:* by :ref{#prop-idelta0-basic}, $a = 2q + r$ with $r \leq 1$. Then $q$ is non-standard, since otherwise $a \leq 2q + 1$ would be standard; and $q$ is not close to $a$, since $a = q + (q + r)$ and $q + r$ is non-standard. So the block of $q$ is a non-standard block below that of $a$.

*Density:* let $a < b$ be non-standard and not close, and write $a + b = 2c + r$ with $r \leq 1$. Then $a \leq c$, since $2c + r = a + b > 2a$ and $r \leq 1$. Let $d = b - a$, which is non-standard. From $2c + r = 2a + d$ we get $2(c - a) + r = d$, so $c - a$ is non-standard: if it were a standard $k$, then $d = 2k + r$ would be standard. Similarly $2(b - c) = d + r$, so $b - c$ is non-standard. Hence the block of $c$ lies strictly between those of $a$ and $b$.

If $M$ is countable, the order of non-standard blocks is a countable dense linear order without endpoints, hence isomorphic to $\mathbb Q$ by Cantor's back-and-forth theorem. Choosing in each block an element and the corresponding copy of $\mathbb Z$ gives the isomorphism.
:::

:::figure[The order of a non-standard model of $\mathrm I\Delta_0$. Below the block of $a$ lies the block of $\lfloor a/2 \rfloor$; between the blocks of $a$ and $b$ lies the block of $\lfloor (a + b)/2 \rfloor$; above them lies the block of $2b$. These three facts use only division by two.]
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The order of a non-standard model of bounded induction: the standard numbers, followed by copies of the integers, called blocks; below the block of a lies the block of half of a, between the blocks of a and b lies the block of their mean, above b lies the block of 2b"><line x1="18" y1="70" x2="108" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="26" cy="70" r="3.5" class="accent-fill"/><text x="26" y="58" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="50" cy="70" r="3.5" class="accent-fill"/><text x="50" y="58" text-anchor="middle" class="mrm" font-size="13">1</text><circle cx="74" cy="70" r="3.5" class="accent-fill"/><text x="74" y="58" text-anchor="middle" class="mrm" font-size="13">2</text><circle cx="98" cy="70" r="3.5" class="accent-fill"/><text x="98" y="58" text-anchor="middle" class="mrm" font-size="13">3</text><text x="124.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="170" y1="70" x2="222" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="180" cy="70" r="2.5" class="node"/><circle cx="212" cy="70" r="2.5" class="node"/><circle cx="196" cy="70" r="3.5" class="accent-fill"/><text x="196.0" y="56.0" text-anchor="middle" class="math" font-size="13">⌊a/2⌋</text><text x="243.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="264" y1="70" x2="316" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="274" cy="70" r="2.5" class="node"/><circle cx="306" cy="70" r="2.5" class="node"/><circle cx="290" cy="70" r="3.5" class="accent-fill"/><text x="290.0" y="56.0" text-anchor="middle" class="math" font-size="13">a</text><text x="337.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="358" y1="70" x2="410" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="368" cy="70" r="2.5" class="node"/><circle cx="400" cy="70" r="2.5" class="node"/><circle cx="384" cy="70" r="3.5" class="accent-fill"/><text x="384.0" y="56.0" text-anchor="middle" class="math" font-size="13">⌊(a+b)/2⌋</text><text x="431.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="452" y1="70" x2="504" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="462" cy="70" r="2.5" class="node"/><circle cx="494" cy="70" r="2.5" class="node"/><circle cx="478" cy="70" r="3.5" class="accent-fill"/><text x="478.0" y="56.0" text-anchor="middle" class="math" font-size="13">b</text><text x="525.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="538" y1="70" x2="582" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="544" cy="70" r="2.5" class="node"/><circle cx="576" cy="70" r="2.5" class="node"/><circle cx="560" cy="70" r="3.5" class="accent-fill"/><text x="560.0" y="56.0" text-anchor="middle" class="math" font-size="13">2b</text><path d="M20,88 L20,94 L110,94 L110,88" class="muted-stroke" stroke-width="1.2"/><text x="65.0" y="112" text-anchor="middle" class="label">standard numbers</text><path d="M170,88 L170,94 L222,94 L222,88" class="muted-stroke" stroke-width="1.2"/><text x="196.0" y="112" text-anchor="middle" class="label">a block</text><text x="330" y="140" text-anchor="middle" class="label">each block is a copy of ℤ; the blocks are densely ordered, without endpoints</text></svg>
:::

:::quiz[the order type]
In the proof of :ref{#thm-order-type}, which axiom beyond $\mathrm{PA}^-$ is used, and is it needed?

- [x] Division by two, from bounded induction; without it the theorem fails: in $\mathbb Z[X]^+$ (:ref{#ex-zx-plus}), the elements of degree one form the blocks of $X, 2X, 3X, \dots$, and no block lies strictly between those of $X$ and $2X$.

  An element strictly between the blocks of $X$ and $2X$ would be a polynomial $mX + k$ with $1 < m < 2$.
- [ ] The least number principle for $\Delta_0$ formulas, to find the least element of a block.

  Blocks have no least element; the proof never looks for one.
- [ ] Induction for $\Sigma_1$ formulas, to show that $q$ is non-standard.

  That $q$ is non-standard follows from $a \leq 2q + 1$ and the closure of the standard part under addition.
:::

## Cuts

:::definition{#def-cut}
A **cut** of a model $M$ of $\mathrm{PA}^-$ is a nonempty subset $I \subseteq M$ that is an initial segment ($b < a \in I$ implies $b \in I$) and is closed under successor ($a \in I$ implies $a + 1 \in I$). It is **proper** if $I \neq M$.
:::

The standard part is a cut of every model of $\mathrm{PA}^-$, proper if the model is non-standard. Induction forbids definable proper cuts: if $\varphi(x, \bar p)$ defines a proper cut, the corresponding instance of induction fails. This is the basic link between induction and cuts, developed in :ref{to="definable-cuts"}. Here we need the converse kind of statement: some cuts are themselves models of bounded induction. For this, we rewrite the axioms of $\mathrm I\Delta_0$ in a form that passes to substructures.

:::lemma{#lem-idelta0-pi1}
$\mathrm I\Delta_0$ is equivalent to a set of $\Pi_1$ sentences: every axiom of each is provable from the other.
:::

:::proof{of=lem-idelta0-pi1}
The axioms of $\mathrm{PA}^-$ are universal sentences, except the axiom of differences, which is equivalent over the other axioms to the $\Pi_1$ sentence $\forall x\, \forall y\, (x < y \rightarrow \exists z < y + 1\ (x + z + 1 = y))$, since $z \leq x + z + 1$. Replace each instance of bounded induction, for $\varphi(x, \bar p)$, by the $\Pi_1$ sentence
$$
\forall \bar p\ \forall a\ \Big(\big(\varphi(0, \bar p) \wedge \forall x < a\ (\varphi(x, \bar p) \rightarrow \varphi(x + 1, \bar p))\big) \rightarrow \varphi(a, \bar p)\Big).
$$
It implies the original instance, since the hypothesis of the original instance gives the hypothesis of this one for every $a$. Conversely, assume the original instances, the hypothesis of the new one for some $a$, and apply induction to the $\Delta_0$ formula $\psi(x) \equiv x < a + 1 \rightarrow \varphi(x, \bar p)$. Then $\psi(0)$ holds; if $\psi(x)$ and $x + 1 < a + 1$, then $x < a$, so $\varphi(x)$ and then $\varphi(x + 1)$. So $\psi(a)$, that is $\varphi(a, \bar p)$.
:::

:::lemma{#lem-cut-model}
Let $M$ be a model of $\mathrm I\Delta_0$ and $I$ a cut of $M$ closed under addition and multiplication. Then $I$ is a substructure of $M$, $I \subseteq_e M$, and $I$ is a model of $\mathrm I\Delta_0$.
:::

:::proof{of=lem-cut-model}
The cut contains $0$, being a nonempty initial segment, and $1 = 0 + 1$; it is closed under the operations by hypothesis, so it is a substructure, and an end extension by definition. Every $\Pi_1$ sentence true in $M$ is true in $I$ by :ref{#cor-sigma1-upward}, and $\mathrm I\Delta_0$ is equivalent to a set of $\Pi_1$ sentences by :ref{#lem-idelta0-pi1}.
:::

## Exercises

::::exercise{#ex-ldelta0-idelta0 difficulty=1 objective="Reverse the proof of the least number principle to derive bounded induction from it."}
Show that, conversely to :ref{#prop-idelta0-basic}, the least number principle for $\Delta_0$ formulas implies bounded induction over $\mathrm{PA}^-$.

:::solution
Let $\varphi$ be $\Delta_0$ with $\varphi(0)$ and $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$, and suppose $\neg \varphi(c)$. The least $m$ with $\neg \varphi(m)$ is not $0$, so $m = m' + 1$ for some $m'$ (axiom 5 with $0 < m$), and $\varphi(m')$ by minimality, since $m' < m$. Then $\varphi(m)$: a contradiction.
:::
::::

## Notes and references

Parikh (1971) introduced $\mathrm I\Delta_0$. The elementary properties of addition, multiplication and order are proved from open induction by Hájek and Pudlák (Theorem I.1.10), the least number principle for bounded formulas is their Theorem I.1.22, and pairing their Theorem I.1.18. The order type $\nat + \mathbb Z \cdot \mathbb Q$ of countable non-standard models is classical; the proof uses only division by two. That $\mathrm I\Delta_0$ has a $\Pi_1$ axiomatization, and its consequence for cuts, are used in Hájek and Pudlák's proof of Parikh's theorem (Theorem V.1.4).

- R. Parikh, *Existence and feasibility in arithmetic*, Journal of Symbolic Logic 36 (1971), 494–508.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(a), and Chapter V, Section 1.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 2 and 3.

:::::exercises
::::exercise{#ex-idelta0-prime-divisor difficulty=1 objective="Apply the least number principle for bounded formulas to find a prime divisor."}
Show that $\mathrm I\Delta_0$ proves that every $x > 1$ has a prime divisor: some $p \leq x$ with $p \mid x$ and $1 < p \wedge \forall y < p\ \forall z < p\ \neg (y \cdot z = p)$, where $d \mid x$ is the bounded formula $\exists q < x + 1\ (q \cdot d = x)$.

:::solution
Fix $x > 1$ and let $\varphi(d) \equiv 1 < d \wedge d \mid x$, a $\Delta_0$ formula with parameter $x$. It holds at $d = x$, with $q = 1$. By the least number principle (:ref{#prop-idelta0-basic}), it has a least element $p$; then $p \leq x$. Suppose $y \cdot z = p$ with $y, z < p$. Neither factor is $0$, since $p \neq 0$, and $y \neq 1$, since otherwise $z = p$. So $1 < y < p$. If $q \cdot p = x$, then $(q z) \cdot y = x$, and $q z \leq x$ since $y \geq 1$; so $y \mid x$, and $\varphi(y)$ with $y < p$ contradicts the minimality of $p$. Hence $p$ is prime.
:::
::::

::::exercise{#ex-idelta0-sqrt difficulty=1 objective="Define the integer square root by a least number argument with a bounded formula."}
Show that $\mathrm I\Delta_0$ proves $\forall x\ \exists y < x + 1\ \big(y \cdot y \leq x \wedge x < (y + 1) \cdot (y + 1)\big)$.

:::solution
Fix $x$ and let $\varphi(y) \equiv x < (y + 1) \cdot (y + 1)$, bounded with parameter $x$. It holds at $y = x$, since $(x + 1)(x + 1) = x \cdot x + x + x + 1 > x$ by :ref{#ex-pam-cancellation}. Let $y$ be the least element satisfying $\varphi$, so $y \leq x$. If $y = 0$, then $x < 1$, so $x = 0$ and $y \cdot y = 0 \leq x$. Otherwise $y = y' + 1$, and $\neg \varphi(y')$ by minimality, that is $(y' + 1)(y' + 1) \leq x$, which is $y \cdot y \leq x$.
:::
::::

::::exercise{#ex-idelta0-sqrt2 difficulty=2 objective="Prove the irrationality of $\sqrt 2$ in bounded induction by a minimal counterexample, and compare with the model of $\mathrm{PA}^-$ in which it fails." lessons="pa-minus"}
Show that $\mathrm I\Delta_0$ proves $\forall x\ \forall y\ \big(x \cdot x = 2 \cdot y \cdot y \rightarrow x = 0\big)$, where $2 = 1 + 1$. By :ref{#ex-pam-sqrt2}, $\mathrm{PA}^-$ does not prove it.

:::solution
First, if $x \cdot x$ is even then $x$ is even. By :ref{#prop-idelta0-basic}, $x = 2q + r$ with $r \leq 1$. If $r = 1$, then $x \cdot x = 2(2q^2 + 2q) + 1$. No element is both $2u$ and $2v + 1$, by the uniqueness of division by $2$; so $x \cdot x$ is not even.

Suppose $x \cdot x = 2 y y$ with $x > 0$. Then $y \leq x$: otherwise $y \cdot y > x \cdot x \geq y \cdot y$ by :ref{#ex-pam-cancellation}. Let $\varphi(x) \equiv 0 < x \wedge \exists y < x + 1\ (x \cdot x = 2 \cdot y \cdot y)$, a bounded formula. It has a least element $x_0$, with some $y_0 \leq x_0$. Since $x_0 \cdot x_0$ is even, $x_0 = 2 x_1$, and $4 x_1 x_1 = 2 y_0 y_0$, so $y_0 \cdot y_0 = 2 x_1 x_1$ by cancellation of $2$. Here $y_0 > 0$, since otherwise $x_0 \cdot x_0 = 0$ and $x_0 = 0$. Moreover $y_0 < x_0$: we have $x_0 \cdot x_0 = y_0 y_0 + y_0 y_0 > y_0 y_0$, as $y_0 y_0 > 0$, and $y_0 \geq x_0$ would give $y_0 y_0 \geq x_0 x_0$. So $\varphi(y_0)$ holds, with the witness $x_1$, which is at most $y_0$ by the bound $y \leq x$ proved above, and $y_0 < x_0$: a contradiction with the minimality of $x_0$.
:::
::::

::::exercise{#ex-ldelta0-greatest difficulty=1 objective="Derive a greatest number principle for bounded formulas from the least number principle, a step used in later lessons."}
Show that $\mathrm I\Delta_0$ proves, for every $\Delta_0$ formula $\delta(x)$ with parameters: if $\delta(x)$ holds for some $x \leq a$, then there is a greatest $x \leq a$ with $\delta(x)$.

:::solution
Let $\psi(y) \equiv y \leq a \wedge \forall x < a + 1\ (\delta(x) \rightarrow x \leq y)$, a bounded formula: $y$ is an upper bound of the elements $x \leq a$ satisfying $\delta$. It holds at $y = a$. Let $y$ be its least element (:ref{#prop-idelta0-basic}). We show $\delta(y)$. Let $x_1 \leq a$ satisfy $\delta$. If $y = 0$, then $x_1 \leq 0$, so $x_1 = y$ and $\delta(y)$. Otherwise $y = y' + 1$. If $\neg \delta(y)$, every $x \leq a$ with $\delta(x)$ satisfies $x \leq y$ and $x \neq y$, hence $x \leq y'$ by :ref{#lem-pam-basic}; and $y' \leq a$; so $\psi(y')$, contradicting minimality. So $y$ satisfies $\delta$ and bounds every $x \leq a$ that does.
:::
::::

::::exercise{#ex-cut-examples difficulty=1 objective="Compute examples of cuts in a non-standard model and check their closure properties."}
Let $M$ be a non-standard model of $\mathrm I\Delta_0$ and $a \in M$ non-standard. Show that $I = \{ b \in M : b < k \cdot a \text{ for some } k \in \nat \}$ is a proper cut of $M$ closed under addition but not under multiplication, and that $J = \{ b \in M : b < a^k \text{ for some } k \in \nat \}$, with $a^k = a \cdots a$ ($k$ factors), is a cut closed under addition and multiplication.

:::solution
Both sets are initial segments by definition. $I$ contains $a$, since $a < 2a$. If $b < k a$ and $b' < k' a$, then $b + b' < (k + k') a$, and $b + 1 < k a + a = (k + 1) a$ since $1 \leq a$; so $I$ is closed under successor and addition. It does not contain $a \cdot a$: if $a \cdot a < k \cdot a$, then $a < \bar k$ by the monotonicity axiom, since otherwise $\bar k \leq a$ would give $k a \leq a a$; and $a$ is non-standard. So $I$ is proper and not closed under multiplication.

For $J$: if $b < a^k$ and $b' < a^{k'}$, then $b \cdot b' < a^{k + k'}$ (if $b' = 0$ because $a^{k+k'} > 0$; otherwise $b b' < a^k b' < a^k a^{k'}$). For addition, $b + b' < 2 a^{\max(k, k')} \leq a^{\max(k, k') + 1}$, since $2 \leq a$. So $J$ is closed under addition, hence under successor, and under multiplication.
:::
::::

::::exercise{#ex-cut-intersection difficulty=1 objective="Check that the standard part is the least cut and that cuts are closed under unions and intersections."}
Let $M$ be a model of $\mathrm{PA}^-$. Show that every cut of $M$ contains the standard part, and that the union and the intersection of a nonempty family of cuts are cuts. Deduce that, if $M$ is non-standard, the standard part is the intersection of all proper cuts of $M$.

:::solution
A cut $I$ is nonempty and an initial segment, so it contains $0$; being closed under successor, it contains every $\bar k^M$, by induction on $k$ in the metatheory. Let $(I_j)_{j \in J}$ be a nonempty family of cuts. The union and the intersection contain $0$; if $b < a$ and $a$ is in the union, $a \in I_j$ for some $j$, so $b \in I_j$; if $a$ is in the intersection, $b \in I_j$ for every $j$; closure under successor is checked in the same way. If $M$ is non-standard, the standard part is a proper cut, and it is contained in every cut, so it is the intersection of all proper cuts.
:::
::::
:::::
