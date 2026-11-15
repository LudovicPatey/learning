---
title: The Ackermann function in IΣ₁ and IΣ₂
summary: The converse of the previous lesson, due to Parsons, Mints and Takeuti, is stated and proved later in the track; a Σ₁ definition of the Ackermann function by finite computations; IΣ₁ proves that it defines a partial function and that each row is total, but not that the function is total; IΣ₂ proves it, by Π₂ induction on the first argument.
duration: 35
prerequisites: [provably-total, models-of-computation/ackermann-function, fragments-of-arithmetic/coding]
---

The previous lesson showed that every primitive recursive function is provably total in $\mathrm I\Sigma_1$. The converse holds as well: a function provably total in $\mathrm I\Sigma_1$ is primitive recursive. This lesson states it and draws the consequence for the Ackermann function, a total computable function that is not primitive recursive. The function has a natural $\Sigma_1$ definition, by **finite computations**: finite sets of triples $\langle x, y, z \rangle$ in which each triple is justified by the defining equations from other triples of the set. $\mathrm I\Sigma_1$ proves that this definition gives a partial function, and that each row $A(m, \cdot)$, for a standard $m$, is total; it does not prove that all rows are total at once. That statement is proved by an induction on $x$ for the $\Pi_2$ formula "row $x$ is total", available in $\mathrm I\Sigma_2$. The gap between "each row" and "all rows" is the gap between finitely many $\Sigma_1$ inductions and one $\Pi_2$ induction.

## The converse

:::theorem[Parsons; Mints; Takeuti]{#thm-pmt}
A function is provably total in $\mathrm I\Sigma_1$ if and only if it is primitive recursive.
:::

The direction from right to left is :ref{#thm-pr-provably-total}. The direction from left to right is proved in the last course of this track, on independence results, by the method of indicators of Paris and Kirby (:ref{#thm-isigma1-envelope}). There, a function provably total in $\mathrm I\Sigma_1$ is shown to be bounded by a function of a fast-growing hierarchy $F_n$, each of which is primitive recursive: otherwise a countable non-standard model of the theory of $\nat$ would contain a cut that satisfies $\mathrm I\Sigma_1$ and is not closed under the function, as in the proof of Parikh's theorem. A $\Sigma_1$ definition together with a primitive recursive bound then gives a primitive recursive definition, by bounded minimization. In this course, the direction from left to right is used only in :ref{#cor-ack-isigma1} below, and nowhere else.

Parsons (1970) first obtained the converse from his theorem that $\mathrm I\Sigma_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic; Mints and Takeuti gave proof-theoretic proofs.

:::corollary{#cor-ack-isigma1}
No $\Sigma_1$ definition of the Ackermann function (:ref{#def-ackermann}) is proved by $\mathrm I\Sigma_1$ to define a total function.
:::

:::proof{of=cor-ack-isigma1}
By :ref{#thm-pmt}, the Ackermann function would be primitive recursive, contradicting :ref{#cor-ack-not-pr}.
:::

## A definition by finite computations

A finite computation of the Ackermann function is a finite set of triples, each of which follows from triples of the same set by one of the three equations of :ref{#def-ackermann}.

:::definition{#def-ack-computation}
Let $\mathrm{Comp}(c)$ be the bounded formula saying that $c$ codes a finite set of triples $\langle x, y, z \rangle$ such that every triple in $c$ is **justified** in $c$: either $x = 0$ and $z = y + 1$; or $x = x' + 1$, $y = 0$ and $\langle x', 1, z \rangle \in c$; or $x = x' + 1$, $y = y' + 1$ and there is $w$ with $\langle x, y', w \rangle \in c$ and $\langle x', w, z \rangle \in c$. A $c$ with $\mathrm{Comp}(c)$ is a **computation**. Let
$$
\alpha(x, y, z) \equiv \exists c\ \big( \mathrm{Comp}(c) \wedge \langle x, y, z \rangle \in c \big),
$$
a $\Sigma_1$ formula.
:::

The quantifiers of $\mathrm{Comp}$ range over elements of $c$, which are smaller than $c$, so $\mathrm{Comp}$ is bounded. The definition only requires each triple to be justified; it does not require the computation to be complete or minimal, and any union of computations is a computation.

:::example{#ex-ack-computation}
The set $\{ \langle 0, 1, 2 \rangle, \langle 1, 0, 2 \rangle, \langle 0, 2, 3 \rangle, \langle 1, 1, 3 \rangle \}$ is a computation. The triples with $x = 0$ are justified by the first clause; $\langle 1, 0, 2 \rangle$ by the second, from $\langle 0, 1, 2 \rangle$; and $\langle 1, 1, 3 \rangle$ by the third, with $w = 2$, from $\langle 1, 0, 2 \rangle$ and $\langle 0, 2, 3 \rangle$. So $\alpha(1, 1, 3)$ holds, in accordance with $A(1, 1) = 3$.
:::

:::figure[The computation of :ref{#ex-ack-computation}. An arrow goes from a triple to the triples that justify it, labelled by the clause of :ref{#def-ack-computation} that is used.]
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="A computation of A(1,1) = 3: the triple (1,1,3) is justified by (1,0,2) and (0,2,3); the triple (1,0,2) is justified by (0,1,2); the triples (0,1,2) and (0,2,3) are justified by the first clause"><defs><marker id="tp-ack-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="252.0" y="21.0" width="96" height="30" rx="4" class="cell"/><text x="300.0" y="41.0" text-anchor="middle" class="mrm" font-size="14">⟨1, 1, 3⟩</text><rect x="132.0" y="97.0" width="96" height="30" rx="4" class="cell"/><text x="180.0" y="117.0" text-anchor="middle" class="mrm" font-size="14">⟨1, 0, 2⟩</text><rect x="372.0" y="97.0" width="96" height="30" rx="4" class="cell head-cell"/><text x="420.0" y="117.0" text-anchor="middle" class="mrm" font-size="14">⟨0, 2, 3⟩</text><rect x="132.0" y="173.0" width="96" height="30" rx="4" class="cell head-cell"/><text x="180.0" y="193.0" text-anchor="middle" class="mrm" font-size="14">⟨0, 1, 2⟩</text><line x1="276.0" y1="51.0" x2="204.0" y2="96.0" class="ink-stroke" stroke-width="1" marker-end="url(#tp-ack-arrow)"/><text x="222.0" y="69.5" text-anchor="end" class="label">⟨x, y′, w⟩</text><line x1="324.0" y1="51.0" x2="396.0" y2="96.0" class="ink-stroke" stroke-width="1" marker-end="url(#tp-ack-arrow)"/><text x="378.0" y="69.5" text-anchor="start" class="label">⟨x′, w, z⟩</text><line x1="180.0" y1="127.0" x2="180.0" y2="172.0" class="ink-stroke" stroke-width="1" marker-end="url(#tp-ack-arrow)"/><text x="168.0" y="153.5" text-anchor="end" class="label">⟨x′, 1, z⟩</text><text x="250" y="193" text-anchor="start" class="label">highlighted: x = 0, justified by the first clause</text></svg>
:::

:::proposition{#prop-ack-computations}
1. In $\nat$, $\alpha(x, y, z)$ holds if and only if $A(x, y) = z$.
2. $\mathrm I\Sigma_1$ proves that $\alpha$ defines a partial function: $\forall x\ \forall y\ \forall z\ \forall z'\ \big( \alpha(x, y, z) \wedge \alpha(x, y, z') \rightarrow z = z' \big)$.
3. For every $m \in \nat$, $\mathrm I\Sigma_1$ proves $\forall y\ \exists z\ \alpha(\bar m, y, z)$, where $\bar m$ is the numeral of $m$.
4. $\mathrm I\Sigma_2$ proves $\forall x\ \forall y\ \exists z\ \alpha(x, y, z)$.
:::

:::proof{of=prop-ack-computations}
1. Every triple of a computation is correct, by induction on $\langle x, y \rangle$ in the lexicographic order, using the defining equations. Conversely, the set of triples used in the evaluation of $A(x, y)$ by the equations is a computation.

2. Work in $\mathrm I\Sigma_1$. The union of two computations is a computation, since justifications are preserved when the set is enlarged, and it is coded by :ref{#thm-delta0-comprehension}; so it suffices to show that a single computation $c$ is functional. Suppose not. By the least number principle for bounded formulas, with parameter $c$, let $x$ be least such that $c$ contains two triples $\langle x, y, z \rangle$ and $\langle x, y, z' \rangle$ with $z \neq z'$ for some $y$, and then $y$ least for this $x$. If $x = 0$, then $z = y + 1 = z'$. If $x = x' + 1$ and $y = 0$, then $\langle x', 1, z \rangle$ and $\langle x', 1, z' \rangle$ are in $c$, a conflict at $x' < x$. If $x = x' + 1$ and $y = y' + 1$, the two triples are justified by $w$ and $w'$ with $\langle x, y', w \rangle, \langle x, y', w' \rangle \in c$, so $w = w'$ by the minimality of $y$, and then $\langle x', w, z \rangle$ and $\langle x', w, z' \rangle$ are in $c$, a conflict at $x' < x$. Each case contradicts the choice of $x$ and $y$.

3. By induction on $m$ in the metatheory. For $m = 0$, the computation $\{ \langle 0, y, y + 1 \rangle \}$ works. Assume that $\mathrm I\Sigma_1$ proves $\forall y\ \exists z\ \alpha(\bar m, y, z)$, and prove $\forall y\ \exists z\ \alpha(\overline{m + 1}, y, z)$ by $\Sigma_1$ induction on $y$. For $y = 0$, take a computation $c$ containing $\langle \bar m, 1, z \rangle$ and add $\langle \overline{m + 1}, 0, z \rangle$. If $c$ contains $\langle \overline{m + 1}, y, w \rangle$, take a computation $c'$ containing $\langle \bar m, w, z \rangle$, given by the hypothesis on $m$, and add $\langle \overline{m + 1}, y + 1, z \rangle$ to $c \cup c'$. Each new triple is justified in the new set, so the new set is a computation.

4. The same argument, with $x$ a variable instead of a numeral. Apply induction, in $\mathrm I\Sigma_2$, to
$$
\tau(x) \equiv \forall y\ \exists z\ \alpha(x, y, z),
$$
a $\Pi_2$ formula; $\Pi_2$ induction is available by :ref{#thm-fo-isigma-ipi}. The case $x = 0$ and the induction step are those of item 3, with $\tau(x)$ as the hypothesis on $x$; the induction on $y$ inside the step is $\Sigma_1$, with $x$ as a parameter.
:::

Items 3 and 4 differ only in the place of the induction on the first argument. In item 3 it is carried out in the metatheory, and produces for each $m$ a separate proof, made of $m + 1$ inductions for $\Sigma_1$ formulas; in item 4 it is a single induction inside the theory, for the $\Pi_2$ formula $\tau$. By :ref{#cor-ack-isigma1}, item 4 cannot be proved in $\mathrm I\Sigma_1$: the rows are provably total one by one, as the rows $A(m, \cdot)$ are primitive recursive one by one (:ref{#ex-ack-row-pr}), but not uniformly. This is a first instance of a general phenomenon studied at the end of the track: the provably total functions of $\mathrm I\Sigma_{n+1}$ grow faster than those of $\mathrm I\Sigma_n$.

:::quiz[the Ackermann function in fragments]
In the proof that a computation is functional, why is $y$ chosen least for the least $x$?

- [x] In the third case, the two triples are justified by $\langle x, y', w \rangle$ and $\langle x, y', w' \rangle$, a possible conflict at the same $x$ and at $y' < y$; minimality of $y$ gives $w = w'$.
- [ ] To treat the case $x = 0$.

  For $x = 0$, the first clause determines $z = y + 1$, whatever $y$ is.
- [ ] To treat the case $y = 0$.

  For $y = 0$, the justifying triples are at $x' < x$, and minimality of $x$ suffices.

---

Why does the argument of item 3 not give item 4 in $\mathrm I\Sigma_1$?

- [x] Item 4 needs an induction on $x$ for $\forall y\ \exists z\ \alpha(x, y, z)$, a $\Pi_2$ formula; item 3 replaces it, for each standard $m$, by $m + 1$ inductions for $\Sigma_1$ formulas, which cannot be done for a variable $x$.
- [ ] Because $\alpha$ is not a $\Sigma_1$ formula.

  It is: an unbounded $\exists c$ in front of a bounded formula.
- [ ] Because $\mathrm I\Sigma_1$ does not prove that $\alpha$ defines a partial function.

  It does, by item 2; functionality plays no role in totality.
:::

## Exercises

::::exercise{#ex-tp-ack-increasing difficulty=2 objective="Prove a property of all triples of a computation by the least number principle, as in the proof of functionality."}
Show that $\mathrm I\Sigma_1$ proves $\forall x\ \forall y\ \forall z\ \big( \alpha(x, y, z) \rightarrow y < z \big)$, the formalized form of $A(x, y) > y$.

:::solution
Let $c$ be a computation; we show that every triple $\langle x, y, z \rangle \in c$ has $y < z$. Suppose not. By the least number principle for bounded formulas, with parameter $c$, let $x$ be least such that some triple $\langle x, y, z \rangle \in c$ has $z \leq y$, and $y$ least for this $x$. If $x = 0$, then $z = y + 1 > y$. If $x = x' + 1$ and $y = 0$, then $\langle x', 1, z \rangle \in c$, and $1 < z$ by the minimality of $x$, so $z > 0 = y$. If $x = x' + 1$ and $y = y' + 1$, there is $w$ with $\langle x, y', w \rangle \in c$ and $\langle x', w, z \rangle \in c$; by the minimality of $y$ and of $x$, $y' < w$ and $w < z$, so $z \geq y' + 2 > y$. Each case contradicts the choice of $x$ and $y$.
:::
::::

## Notes and references

The characterization of the provably total functions of $\mathrm I\Sigma_1$ is due to Parsons (1970), through his conservation theorem, and was reproved by Mints and by Takeuti; Hájek and Pudlák prove it by indicators (Corollary IV.3.7, credited there to Takeuti and Mints), in the sharper form that a defining formula is provably equivalent to the formula of a primitive recursive derivation. The proof by indicators is :ref{#thm-isigma1-envelope} in the course on independence. The definition of the Ackermann function by finite computations is the one used for the fast-growing hierarchy in the same course.

- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, Amsterdam, 1970, 459–473.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 3.
- G. Takeuti, *Proof Theory*, North-Holland, 1975.

:::::exercises
::::exercise{#ex-tp-ack-equations difficulty=1 objective="Check that the formula $\alpha$ satisfies the defining equations of the Ackermann function in $\mathrm I\Sigma_1$, wherever its values exist."}
Show that $\mathrm I\Sigma_1$ proves, for all $x, y, z$:

1. $\alpha(0, y, z) \leftrightarrow z = y + 1$;
2. $\alpha(x + 1, 0, z) \leftrightarrow \alpha(x, 1, z)$;
3. $\alpha(x + 1, y + 1, z) \leftrightarrow \exists w\ \big( \alpha(x + 1, y, w) \wedge \alpha(x, w, z) \big)$.

Deduce that $\mathrm I\Sigma_2$ proves that $\alpha$ defines a total function satisfying the three equations of :ref{#def-ackermann}.

:::solution
Work in $\mathrm I\Sigma_1$. Recall from the proof of :ref{#prop-ack-computations} that justifications are preserved when a computation is enlarged, so that the union of computations is a computation, and that adding to a computation a triple justified in the enlarged set gives a computation; the enlarged sets are coded, by :ref{#thm-delta0-comprehension} or item 4 of :ref{#lem-ack-basic}.

*From left to right.* Let $c$ be a computation containing the triple on the left. The triple is justified in $c$, and since $0 \neq x' + 1$ and $y + 1 \neq 0$ in $\mathrm{PA}^-$, only one clause of :ref{#def-ack-computation} can justify it: the first for $\langle 0, y, z \rangle$, which gives $z = y + 1$; the second for $\langle x + 1, 0, z \rangle$, which gives $\langle x, 1, z \rangle \in c$; the third for $\langle x + 1, y + 1, z \rangle$, which gives $w$ with $\langle x + 1, y, w \rangle, \langle x, w, z \rangle \in c$. The triples found are in the computation $c$, so $\alpha$ holds for them.

*From right to left.* 1. The set $\{ \langle 0, y, y + 1 \rangle \}$ is a computation. 2. If $c$ is a computation containing $\langle x, 1, z \rangle$, then $c \cup \{ \langle x + 1, 0, z \rangle \}$ is one, the new triple being justified by the second clause. 3. If $c$ and $c'$ are computations containing $\langle x + 1, y, w \rangle$ and $\langle x, w, z \rangle$, then $c \cup c' \cup \{ \langle x + 1, y + 1, z \rangle \}$ is one, the new triple being justified by the third clause.

In $\mathrm I\Sigma_2$, items 2 and 4 of :ref{#prop-ack-computations} give $\forall x\ \forall y\ \exists! z\ \alpha(x, y, z)$. Writing $A(x, y)$ for this $z$, the three equivalences become $A(0, y) = y + 1$, $A(x + 1, 0) = A(x, 1)$ and $A(x + 1, y + 1) = A(x, A(x + 1, y))$, the $w$ of item 3 being $A(x + 1, y)$ by uniqueness. So the Ackermann function is provably total in $\mathrm I\Sigma_2$, together with its equations.
:::
::::

::::exercise{#ex-tp-ack-monotone difficulty=1 objective="Combine functionality with the inequality $A(x, y) > y$ to prove monotonicity in the second argument inside $\mathrm I\Sigma_1$."}
Show that $\mathrm I\Sigma_1$ proves $\forall x\ \forall y\ \forall z\ \forall z'\ \big( \alpha(x, y, z) \wedge \alpha(x, y + 1, z') \rightarrow z < z' \big)$.

:::solution
Work in $\mathrm I\Sigma_1$. Let $c$ and $c'$ be computations containing $\langle x, y, z \rangle$ and $\langle x, y + 1, z' \rangle$; their union $d$ is a computation containing both. If $x = 0$, then $z = y + 1 < y + 2 = z'$. If $x = x' + 1$, the triple $\langle x, y + 1, z' \rangle$ is justified in $d$ by the third clause: there is $w$ with $\langle x, y, w \rangle \in d$ and $\langle x', w, z' \rangle \in d$. By item 2 of :ref{#prop-ack-computations}, $w = z$. By :ref{#ex-tp-ack-increasing}, applied to $\langle x', w, z' \rangle$, $w < z'$. So $z < z'$.
:::
::::

::::exercise{#ex-tp-ack-first-column difficulty=2 objective="Apply the Parsons–Mints–Takeuti theorem to a function built from the Ackermann function, through its definition by computations."}
Show that $\mathrm I\Sigma_1$ does not prove $\forall x\ \exists z\ \alpha(x, 0, z)$, although it proves $\exists z\ \alpha(\bar m, 0, z)$ for every $m \in \nat$.

:::solution
The second statement is a special case of item 3 of :ref{#prop-ack-computations}. Suppose that $\mathrm I\Sigma_1 \vdash \forall x\ \exists z\ \alpha(x, 0, z)$. The formula $\alpha(x, 0, z)$ is $\Sigma_1$; by item 1 of :ref{#prop-ack-computations} it defines in $\nat$ the graph of $g(x) = A(x, 0)$; and by item 2, $\mathrm I\Sigma_1$ proves that it has at most one $z$ for each $x$. So $\mathrm I\Sigma_1 \vdash \forall x\ \exists! z\ \alpha(x, 0, z)$, and $g$ is provably total in $\mathrm I\Sigma_1$. By :ref{#thm-pmt}, $g$ is primitive recursive, which contradicts :ref{#ex-ack-first-column}. The same argument applies to the diagonal $x \mapsto A(x, x)$, by :ref{#cor-ack-not-pr}.
:::
::::

::::exercise{#ex-tp-ack-cut difficulty=2 objective="Turn the induction step of the $\Pi_2$ induction into a $\Pi_2$-definable proper cut in a model of $\mathrm I\Sigma_1$." lessons="fragments-of-arithmetic/definable-cuts"}
Let $\tau(x) \equiv \forall y\ \exists z\ \alpha(x, y, z)$, as in the proof of :ref{#prop-ack-computations}.

1. Show that $\mathrm I\Sigma_1 \vdash \forall x\ (\tau(x) \rightarrow \tau(x + 1))$.
2. Show that there is a model $M$ of $\mathrm I\Sigma_1$ in which $I = \{ a \in M : M \models \forall x \leq a\ \tau(x) \}$ is a proper cut, and that $I$ is $\Pi_2$-definable in $M$ without parameters. Why does this not contradict item 4 of :ref{#prop-ack-computations}?

:::solution
1. This is the induction step of item 4, carried out in $\mathrm I\Sigma_1$: assume $\tau(x)$, and prove $\forall y\ \exists z\ \alpha(x + 1, y, z)$ by $\Sigma_1$ induction on $y$, with the parameter $x$. For $y = 0$, $\tau(x)$ gives a computation $c$ containing some $\langle x, 1, z \rangle$, and $c \cup \{ \langle x + 1, 0, z \rangle \}$ is a computation. If a computation $c$ contains $\langle x + 1, y, w \rangle$, then $\tau(x)$ gives a computation $c'$ containing some $\langle x, w, z \rangle$, and $c \cup c' \cup \{ \langle x + 1, y + 1, z \rangle \}$ is a computation. The only use of $\tau(x)$ is as a hypothesis; no induction on $x$ is made.

2. By :ref{#cor-ack-isigma1} and item 2 of :ref{#prop-ack-computations}, $\mathrm I\Sigma_1$ does not prove $\forall x\ \tau(x)$: otherwise it would prove $\forall x\ \forall y\ \exists! z\ \alpha(x, y, z)$. By the completeness theorem, there are $M \models \mathrm I\Sigma_1$ and $b \in M$ with $M \models \neg \tau(b)$. The set $I$ is an initial segment by definition. It contains $0$, since $\{ \langle 0, y, y + 1 \rangle \}$ is a computation for every $y$. If $a \in I$, then $\tau(a)$, so $\tau(a + 1)$ by item 1, and $a + 1 \in I$. So $I$ is a cut, and $b \notin I$, so $I \neq M$. The formula $\forall x \leq a\ \forall y\ \exists z\ \alpha(x, y, z)$ is equivalent to $\forall y\ \forall x \leq a\ \exists z\ \alpha(x, y, z)$, and $\forall x \leq a\ \exists z\ \alpha(x, y, z)$ is $\Sigma_1$ in $\mathrm I\Sigma_1$ by Parsons' lemma (:ref{#lem-fo-collection-closure}) and :ref{#thm-fo-parsons}; so $I$ is $\Pi_2$-definable without parameters.

There is no contradiction: $M$ satisfies $\mathrm I\Sigma_1$ but not $\mathrm I\Sigma_2$. In a model of $\mathrm I\Sigma_2$, no proper cut is $\Pi_2$-definable (:ref{to="fragments-of-arithmetic/definable-cuts"}), and $\Pi_2$ induction applied to $\tau$, which is what item 4 does, is the statement that $I = M$.
:::
::::
:::::
