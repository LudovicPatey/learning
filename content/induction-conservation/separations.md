---
title: Separating the hierarchy
summary: The Σₙ₊₁-definable elements of a model of Peano arithmetic form a model of IΣₙ in which Σₙ₊₁ collection fails (Parsons, Paris–Kirby); the hierarchy of induction and collection is strict, and Peano arithmetic is not finitely axiomatizable.
duration: 25
prerequisites: [definable-elements]
---

The previous lesson showed that the set $K_{n+1}(M)$ of $\Sigma_{n+1}$-definable elements of a model $M$ of Peano arithmetic is a $\Sigma_{n+1}$-elementary substructure of $M$. This lesson shows that it satisfies $\Sigma_n$ induction and fails $\Sigma_{n+1}$ collection, when it contains a non-standard element $b$. Induction survives because the failure point of an instance of $\Sigma_n$ induction is given by a $\Sigma_{n+1}$ formula, which has a witness in $K_{n+1}(M)$. Collection fails because every element of $K_{n+1}(M)$ has a name, a formula, whose code is a standard number: all the names lie below $b$, and they name elements far above $b$. A bounded set of names mapped onto an unbounded set of elements is exactly a failure of collection.

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

Together with the lesson on collection and induction, the two theorems show that all the implications of the hierarchy are strict:
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


::::exercise{#ex-idelta0-not-bdelta0 difficulty=1 objective="Read off from the separation theorem that bounded induction does not prove collection for bounded formulas, and locate the step of the proof of induction ⇒ collection that fails at level $0$."}
Show that $\mathrm I\Delta_0$ does not prove collection for bounded formulas: there are a model of $\mathrm I\Delta_0$, a bounded formula $\delta(x, w)$ with parameters and an element $a$ such that $\forall x < a\ \exists w\ \delta(x, w)$ holds but $\exists b\ \forall x < a\ \exists w < b\ \delta(x, w)$ fails. Where does the proof of :ref{#thm-induction-collection} break down for $n = 0$?

:::solution
By :ref{#thm-isigma-not-bsigma} with $n = 0$, there is a model $K$ of $\mathrm I\Sigma_0 = \mathrm I\Delta_0$ in which an instance of $\mathrm B\Sigma_1$ fails: for some $\Sigma_1$ formula $\varphi(x, y) \equiv \exists z_1 \cdots \exists z_k\ \delta_0(x, y, \bar z)$, with $\delta_0$ bounded and parameters in $K$, and some $a$, $K \models \forall x < a\ \exists y\ \varphi(x, y)$, but no $b$ bounds witnesses $y$ for all $x < a$. Using an iterated pairing function (:ref{#fact-idelta0}), let $\delta(x, w)$ say that $w = \langle y, \bar z \rangle$ for some $y, \bar z \leq w$ with $\delta_0(x, y, \bar z)$; it is bounded, and $K \models \forall x < a\ \exists w\ \delta(x, w)$. If some $b$ satisfied $\forall x < a\ \exists w < b\ \delta(x, w)$, then for each $x < a$ the first component $y \leq w < b$ of such a $w$ would be a witness of $\varphi(x, y)$ below $b$, which is impossible.

In the proof of :ref{#thm-induction-collection}, the induction is applied to $\theta(c) \equiv c \leq a \rightarrow \exists b\ \forall x < c\ \exists w < b\ \chi(x, w)$. For $n = 0$, $\chi$ is bounded, but the unbounded quantifier $\exists b$ makes $\theta$ a $\Sigma_1$ formula, to which $\mathrm I\Delta_0$ does not apply. The bound $b$ is precisely what cannot be found by bounded induction.
:::
::::

## Notes and references

Partial truth definitions, which these separations use, are constructed in the course on truth definitions and provability (:ref{to="truth-and-provability/truth-definitions"}).

The existence of models of $\mathrm I\Sigma_n$ in which $\mathrm B\Sigma_{n+1}$ fails is due to Parsons (1970); the proof by definable elements is that of Paris and Kirby (1978), who also proved that $\mathrm B\Sigma_n$ does not prove $\mathrm I\Sigma_n$. The presentation follows Dzhafarov and Mummert, Section 6.3, with a direct proof that $K_{n+1}(M)$ satisfies $\mathrm I\Sigma_n$.

- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- C. Ryll-Nardzewski, *The role of the axiom of induction in elementary arithmetic*, Fundamenta Mathematicae 39 (1952), 239–263.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 6.2–6.3.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapters I and IV.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, chapters *Satisfaction* and *Subsystems of Peano arithmetic*.

:::::exercises
::::exercise{#ex-elementary-cut-collection difficulty=2 objective="Show that $\Sigma_{n+1}$-elementary initial segments satisfy $\Sigma_{n+1}$ collection, and deduce that the model of definable elements is not an initial segment."}
Let $M$ be a model of $\mathrm{PA}$, $n \geq 0$, and $K \prec_{\Sigma_{n+1}} M$ a substructure that is a proper initial segment of $M$: if $y \in K$ and $x < y$ in $M$, then $x \in K$, and $K \neq M$. Show that $K$ satisfies $\mathrm B\Sigma_{n+1}$. Deduce that if $K_{n+1}(M)$ contains a non-standard element, it is not an initial segment of $M$.

:::solution
Every $c \in M \setminus K$ is greater than every element of $K$, since $c \leq y \in K$ would give $c \in K$. Let $\varphi(x, y)$ be $\Sigma_{n+1}$ with parameters $\bar d$ in $K$, and $a \in K$ with $K \models \forall x < a\ \exists y\ \varphi(x, y)$. Fix $c \in M \setminus K$.

*In $M$, the witnesses are bounded by $c$.* Let $x < a$ in $M$; then $x \in K$, and there is $y \in K$ with $K \models \varphi(x, y)$, hence $M \models \varphi(x, y)$ by elementarity, and $y < c$. So $M \models \forall x < a\ \exists y < c\ \varphi(x, y)$.

*The bound comes down to $K$.* In $M$, which satisfies $\mathrm B\Sigma_{n+1}$, the formula $\forall x < u\ \exists y < v\ \varphi(x, y)$ is equivalent to a $\Sigma_{n+1}$ formula $\rho(u, v)$ by :ref{#lem-collection-closure}. So $M \models \exists v\ \rho(a, v)$, a $\Sigma_{n+1}$ formula with parameters in $K$, and $K \models \exists v\ \rho(a, v)$ by elementarity: there is $b \in K$ with $K \models \rho(a, b)$, hence $M \models \rho(a, b)$, that is, $M \models \forall x < a\ \exists y < b\ \varphi(x, y)$. For $x < a$, the witness $y < b$ belongs to $K$, since $K$ is an initial segment, and $K \models \varphi(x, y)$ by elementarity. So $K \models \forall x < a\ \exists y < b\ \varphi(x, y)$.

The equivalence between $\rho$ and the bounded formula is used only in $M$, so no collection is assumed in $K$.

*Consequence.* $K_{n+1}(M) \prec_{\Sigma_{n+1}} M$ by :ref{#lem-kn-elementary}, and it is not equal to $M$, since by :ref{#thm-isigma-not-bsigma} it fails $\mathrm B\Sigma_{n+1}$ while $M$ satisfies it. If it were an initial segment of $M$, it would satisfy $\mathrm B\Sigma_{n+1}$ by the first part, contradicting the same theorem.
:::
::::
:::::
