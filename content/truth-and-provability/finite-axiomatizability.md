---
title: Finite axiomatizability and the hierarchy in models
summary: Every Σₙ formula is equivalent in IΣ₁ to one with quantifiers bounded by variables, hence to an instance of Sat_Σₙ; for n ≥ 1, IΣₙ is axiomatized by finitely many theorems of IΣ₁ and one instance of induction for Sat_Σₙ; Peano arithmetic is not axiomatized by sentences of bounded complexity (Rabin); in every model of IΣ₁, some Πₙ-definable set is not Σₙ-definable with parameters.
duration: 45
prerequisites: [truth-definitions]
---

Peano arithmetic is axiomatized by infinitely many instances of induction, and no finite set of its theorems axiomatizes it (Ryll-Nardzewski, 1952). Each fragment $\mathrm I\Sigma_n$ is also given by infinitely many instances, one for each $\Sigma_n$ formula. The partial truth definition of the previous lesson collapses this infinity: a single $\Sigma_n$ formula, $\mathrm{Sat}_{\Sigma_n}$, represents all the others, and one instance of induction for it gives induction for every $\Sigma_n$ formula. This lesson draws this consequence and two others: Peano arithmetic is not axiomatized by sentences of bounded quantifier complexity, and the arithmetic hierarchy is proper in every model of $\mathrm I\Sigma_1$, not only in $\nat$.

## Induction for formulas with bounds by variables

The general form of Tarski's scheme (:ref{#cor-snowing-general}) uses the instances of collection of :ref{#lem-variable-bounds}, which depend on the formula. The following lemma shows that induction for $\Sigma^*_n$ formulas provides them.

:::lemma{#lem-isigma-star}
For $n \geq 1$, let $\mathrm I\Sigma^*_n$ be $\mathrm{PA}^-$ together with induction for $\Sigma^*_n$ formulas. Then $\mathrm I\Sigma^*_n$ proves the collection scheme $\mathrm B\Delta^*_0$, and $\mathrm I\Sigma^*_n$ and $\mathrm I\Sigma_n$ are equivalent.
:::

:::proof{of=lem-isigma-star}
Since every $\Sigma^*_n$ formula is $\Sigma_n$, $\mathrm I\Sigma_n$ contains $\mathrm I\Sigma^*_n$. We follow the proof of Parsons' theorem (:ref{#thm-fo-parsons}). Let $\delta(x, \bar y)$ be in $\Delta^*_0$, with parameters, and assume $\forall x < a\ \exists \bar y\ \delta(x, \bar y)$. Apply induction on $c$ to
$$
\theta(c) \equiv a < c \vee \exists b\ \forall x < c\ \exists \bar y < b\ \delta(x, \bar y),
$$
which is $\Sigma^*_1$ after moving $\exists b$ to the front, since its bounded quantifiers are bounded by the variables $c$ and $b$. Then $\theta(0)$ holds. Assume $\theta(c)$. If $a < c + 1$, then $\theta(c + 1)$ holds by its first disjunct. Otherwise $c < a$, so $\theta(c)$ holds by its second disjunct, with some bound $b$; let $\bar y_0$ be witnesses for $x = c$. Then the maximum of $b$ and of the $y_{0,i} + 1$ is a bound for $c + 1$, since every $x < c + 1$ is below $c$ or equal to $c$. By induction, $\theta(a)$ holds, which is the instance of collection. So $\mathrm I\Sigma^*_n$ proves $\mathrm B\Delta^*_0$. By :ref{#lem-variable-bounds}, every $\Sigma_n$ formula is then equivalent in $\mathrm I\Sigma^*_n$ to a $\Sigma^*_n$ formula with the same free variables, and its instances of induction follow from those of the equivalent formula.
:::

## Finite axiomatizability

:::theorem{#thm-isigma-finite}
For every $n \geq 1$, $\mathrm I\Sigma_n$ is finitely axiomatizable: it is equivalent to a theory consisting of finitely many sentences.
:::

The idea is to choose once and for all a finite part $T_0$ of $\mathrm I\Sigma_1$ that proves Tarski's conditions for $\mathrm{Sat}_{\Sigma_n}$. Over $T_0$, every $\Sigma^*_n$ formula $\varphi$ is equivalent to $\mathrm{Sat}_{\Sigma_n}(\ulcorner \varphi \urcorner, \cdot)$, so its induction instance is the instance of the single sentence "induction holds for $\mathrm{Sat}_{\Sigma_n}(z, \cdot)$, for every $z$" at $z = \ulcorner \varphi \urcorner$.

:::proof{of=thm-isigma-finite}
Let $\sigma_n(z, e)$ be a $\Sigma_n$ formula equivalent to $\mathrm{Sat}_{\Sigma_n}(z, e)$ in $\mathrm I\Sigma_1$ (:ref{#thm-sat-n}), and let $\chi(x, z, e)$ be the $\Sigma_n$ formula $\exists e'\ (e' = e[0 := x] \wedge \sigma_n(z, e'))$, with the relation $e' = e[0 := x]$ written in its $\Sigma_1$ form. Let $\mathrm{Ind}_n$ be the universal closure of the instance of induction for $\chi$ in the variable $x$:
$$
\forall z\ \forall e\ \Big( \big(\chi(0, z, e) \wedge \forall x\ (\chi(x, z, e) \rightarrow \chi(x + 1, z, e))\big) \rightarrow \forall x\ \chi(x, z, e) \Big).
$$
Let $T_0$ consist of $\mathrm{PA}^-$, the finitely many sentences provable in $\mathrm I\Sigma_1$ used in :ref{#cor-snowing} for the formulas $\mathrm{Sat}_{\Sigma_m}$, $\mathrm{Sat}_{\Pi_m}$, $m \leq n$, the equivalence of $\sigma_n$ with $\mathrm{Sat}_{\Sigma_n}$, and the basic properties of assignments: $e(i)$ is defined for all $e$ and $i$, concatenations $s^\frown v$ exist, and $e[0 := x]$ is a sequence whose value at $0$ is $x$ and whose other values are those of $e$. Let $A = T_0 \cup \{ \mathrm{Ind}_n \}$, a finite theory.

Every sentence of $A$ is provable in $\mathrm I\Sigma_n$: those of $T_0$ in $\mathrm I\Sigma_1$, and $\mathrm{Ind}_n$ is an instance of $\Sigma_n$ induction. Conversely, let $\varphi(v_0, v_1, \dots, v_k)$ be a $\Sigma^*_n$ formula, with $v_0$ as the induction variable and $v_1, \dots, v_k$ as parameters, after renaming. By :ref{#cor-snowing}, $T_0$ proves $\forall e\ (\varphi(e) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(\ulcorner \varphi \urcorner, e))$. Given values $\bar p$ of the parameters, let $e = \langle 0, \bar p \rangle$; then $T_0$ proves $\varphi(x, \bar p) \leftrightarrow \chi(x, \ulcorner \varphi \urcorner, e)$ for every $x$, since $e[0 := x]$ has the values $x, \bar p$. So the instance of induction for $\varphi$ follows from $\mathrm{Ind}_n$ applied to $z = \ulcorner \varphi \urcorner$ and this $e$. Hence $A$ proves $\mathrm I\Sigma^*_n$, and $\mathrm I\Sigma_n$ by :ref{#lem-isigma-star}.
:::

:::quiz[finite axiomatizability]
Why does the proof need :ref{#lem-isigma-star}, rather than applying :ref{#cor-snowing} directly to every $\Sigma_n$ formula?

- [x] For an arbitrary $\Sigma_n$ formula, the equivalence with an instance of $\mathrm{Sat}_{\Sigma_n}$ goes through :ref{#lem-variable-bounds}, whose proof uses instances of collection that depend on the formula; they are not among the finitely many axioms of $A$, and the lemma derives them from induction for $\Sigma^*_n$ formulas, which $A$ proves.
- [ ] Because $\mathrm{Sat}_{\Sigma_n}$ only applies to sentences.

  It applies to formulas with free variables, through the assignment $e$.
- [ ] Because $\mathrm{Ind}_n$ is not an instance of $\Sigma_n$ induction.

  It is one, for the $\Sigma_n$ formula $\chi$ with the parameters $z$ and $e$.

---

Why does the argument fail for $n = 0$?

- [x] The finite part $T_0$ of $\mathrm I\Sigma_1$ is not available in $\mathrm I\Delta_0$, and the truth definition for bounded formulas is $\Delta_1$, not bounded, so induction for it is not an instance of bounded induction.
- [ ] Because there are only finitely many $\Delta_0$ formulas.

  There are infinitely many.
- [ ] Because $\mathrm I\Delta_0$ is known not to be finitely axiomatizable.

  Whether $\mathrm I\Delta_0$ is finitely axiomatizable is an open problem; the argument simply does not apply.
:::

The finite axiomatizability of $\mathrm I\Delta_0$ is open, and related to questions of computational complexity; that of $\mathrm I\Delta_0 + \mathrm{exp}$ was proved by Gaifman and Dimitracopoulos (1982), with a truth definition for bounded formulas in $\mathrm I\Delta_0 + \mathrm{exp}$ (Hájek and Pudlák, bibliographical remarks to Chapter V).

## Consequences for Peano arithmetic

Since $\mathrm{PA}$ is the union of the increasing sequence of theories $\mathrm I\Sigma_n$, each of which is finitely axiomatizable, $\mathrm{PA}$ is finitely axiomatizable if and only if $\mathrm I\Sigma_n$ proves all of $\mathrm{PA}$ for some $n$: a finite axiomatization of $\mathrm{PA}$ is provable from finitely many instances of induction, all in some $\mathrm I\Sigma_n$, and conversely $\mathrm I\Sigma_n$ is finitely axiomatizable. So $\mathrm{PA}$ is finitely axiomatizable if and only if the hierarchy of induction schemes collapses. Ryll-Nardzewski's theorem is thus equivalent to the strictness of the hierarchy, proved by models of definable elements in the lesson :ref{to="induction-conservation/separations"} of the course on induction and conservation. We use the results of that lesson, as a pointer, for a stronger statement.

:::theorem[Rabin]{#thm-rabin}
For every $m \in \nat$, $\mathrm{PA}$ is not equivalent to any set of $\Pi_m$ sentences.
:::

:::proof{of=thm-rabin}
Suppose that a set $S$ of $\Pi_m$ sentences is equivalent to $\mathrm{PA}$. Let $M$ be a model of $\mathrm{PA}$ with a non-standard element defined by a bounded formula, and let $K = K_{m+1}(M)$ be the set of its $\Sigma_{m+1}$-definable elements. By the lesson :ref{to="induction-conservation/separations"} of the course on induction and conservation, such an $M$ exists and $K$ is a $\Sigma_{m+1}$-elementary substructure of $M$: $\Sigma_{m+1}$ formulas with parameters in $K$ have the same truth value in $K$ and in $M$. Hence every $\Pi_{m+2}$ sentence $\forall \bar x\ \sigma(\bar x)$ true in $M$, with $\sigma \in \Sigma_{m+1}$, is true in $K$; in particular every sentence of $S$, which is true in $M$ since $M \models \mathrm{PA}$. So $K \models S$, hence $K \models \mathrm{PA}$. But $K$ does not satisfy $\mathrm B\Sigma_{m+1}$, by the main theorem of the same lesson, while $\mathrm{PA}$ proves it: a contradiction.
:::

Every sentence is equivalent to a prenex sentence, hence is $\Pi_m$ for some $m$; the theorem says that no bound on $m$ works for all the axioms. In particular, $\mathrm{PA}$ is not finitely axiomatizable. A finer form of the strictness of the hierarchy, which we do not prove, compares consistency strength: $\mathrm I\Sigma_{n+1}$ proves the consistency of $\mathrm I\Sigma_n$ (Hájek and Pudlák, Corollary I.4.34), so $\mathrm I\Sigma_n$ does not prove $\mathrm I\Sigma_{n+1}$, by Gödel's second theorem applied to $\mathrm I\Sigma_n$. The proof of Hájek and Pudlák uses the partial truth definitions of the previous lesson and the arithmetization of provability.

## The hierarchy is proper in every model

In $\nat$, the classes $\Sigma^0_n$ and $\Pi^0_n$ differ (:ref{#cor-hierarchy-strict}). The universal formulas give the same conclusion in every model of $\mathrm I\Sigma_1$, for definability with parameters, by Cantor's diagonal argument.

:::theorem{#thm-hierarchy-proper}
Let $M$ be a model of $\mathrm I\Sigma_1$ and $n \geq 1$. There is a set $D \subseteq M$, $\Pi_n$-definable in $M$ without parameters, that is not $\Sigma_n$-definable in $M$ with parameters. Consequently, the complement of $D$ is $\Sigma_n$-definable and not $\Pi_n$-definable, and $\Sigma_n$-definability with parameters is strictly weaker than $\Sigma_{n+1}$-definability in $M$.
:::

:::proof{of=thm-hierarchy-proper}
Writing $w = \langle a, c \rangle$, let
$$
D = \{ w \in M : M \models \neg \mathrm{Sat}_{\Sigma_n}(a, \langle w, c \rangle) \},
$$
where $\langle w, c \rangle$ is the assignment with values $w$ at $v_0$ and $c$ at $v_1$. It is defined without parameters by $\forall a \leq w\ \forall c \leq w\ \forall e\ \big( (w = \langle a, c \rangle \wedge e = \langle w, c \rangle) \rightarrow \neg \mathrm{Sat}_{\Sigma_n}(a, e) \big)$, which is $\Pi_n$ in $\mathrm I\Sigma_1$, since the relation $e = \langle w, c \rangle$ is bounded; so $D$ is $\Pi_n$-definable. Suppose that $D = \{ x : M \models \psi(x, \bar d) \}$ with $\psi$ in $\Sigma_n$ and parameters $\bar d$. Replacing the tuple $\bar d$ by the single number $c = \langle \bar d \rangle$ and decoding it with bounded formulas, we may assume a single parameter: $D = \{ x : M \models \psi(x, c) \}$, with $\psi(v_0, v_1)$ in $\Sigma_n$. By :ref{#cor-snowing-general}, there is a standard code $a$ of a $\Sigma^*_n$ formula such that $M \models \psi(x, y) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(a, \langle x, y \rangle)$ for all $x, y$. Let $w = \langle a, c \rangle$. Then $w \in D$ if and only if $M \models \psi(w, c)$, if and only if $M \models \mathrm{Sat}_{\Sigma_n}(a, \langle w, c \rangle)$, if and only if $w \notin D$, by the definition of $D$: a contradiction.

The complement of $D$ is $\Sigma_n$-definable, and if it were $\Pi_n$-definable with parameters, $D$ would be $\Sigma_n$-definable. Finally $D$ is $\Pi_n$-definable, hence $\Sigma_{n+1}$-definable, and not $\Sigma_n$-definable.
:::

:::quiz[the diagonal argument]
In the proof of :ref{#thm-hierarchy-proper}, why does $D$ diagonalize over pairs $w = \langle a, c \rangle$ rather than over codes $a$ alone?

- [x] To handle definitions with parameters: the parameter $c$ of the hypothetical definition is built into the diagonal element $w$, so one set $D$ defeats every $\Sigma_n$ definition with every parameter.
- [ ] Because codes of formulas are pairs.

  Codes are pairs, but this plays no role; any element can be paired with any $c$.
- [ ] To make $D$ definable without parameters.

  The set $\{ a : \neg \mathrm{Sat}_{\Sigma_n}(a, \langle a \rangle) \}$ would also be definable without parameters; but it would only defeat definitions without parameters.

---

Where is it used that $M$ satisfies $\mathrm I\Sigma_1$?

- [x] To have, for the formula $\psi$, a standard code $a$ with $\psi(x, y) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(a, \langle x, y \rangle)$ in $M$: the scheme of :ref{#cor-snowing-general} is proved in $\mathrm I\Sigma_1$.
- [ ] To make $D$ nonempty.

  Whether $D$ is empty plays no role: the contradiction is obtained at the single element $w = \langle a, c \rangle$.
- [ ] To decode the parameter tuple.

  Decoding pairs only needs $\mathrm I\Delta_0$.
:::

For $M = \nat$, the theorem gives again that $\Sigma^0_n \neq \Pi^0_n$. In a non-standard model, the statement is about definability with arbitrary parameters, which may be non-standard: no parameter, however large, makes a $\Sigma_n$ formula define $D$.

## Exercises

::::exercise{difficulty=2}
Show that for every $n \geq 1$, $\mathrm B\Sigma_{n+1}$ is finitely axiomatizable.

:::solution
By :ref{#thm-fo-paris-kirby}, $\mathrm B\Sigma_{n+1}$ proves $\mathrm I\Sigma_n$, hence $\mathrm I\Sigma_1$ and the finitely many axioms $A_n$ of :ref{#thm-isigma-finite} for $\mathrm I\Sigma_n$. Let $\pi_n(z, e)$ be a $\Pi_n$ formula equivalent to $\mathrm{Sat}_{\Pi_n}$ in $\mathrm I\Sigma_1$, and $C_n$ the instance of collection, with parameters $z$ and $e$, for the formula $\exists e'\ (e' = e[0 := x][1 := y] \wedge \pi_n(z, e'))$, equivalent in $\mathrm I\Sigma_1$ to a $\Pi_n$ formula, in the variables $x$ and $y$. Then $A_n \cup \{ C_n \}$ is contained in $\mathrm B\Sigma_{n+1}$, since the formula of $C_n$ is an existential quantification of a conjunction of a $\Delta_1$ and a $\Pi_n$ formula, hence $\Sigma_{n+1}$. Conversely, $A_n \cup \{ C_n \}$ proves $\mathrm I\Sigma_n$, and for every $\Pi_n$ formula $\varphi(x, y, \bar p)$, $\mathrm I\Sigma_1$ proves $\varphi$ equivalent to $\mathrm{Sat}_{\Pi_n}(\ulcorner \varphi^* \urcorner, \langle x, y, \bar p \rangle)$, by :ref{#cor-snowing-general}; so the instance of collection for $\varphi$ follows from $C_n$. This gives $\mathrm B\Pi_n$, which is equivalent to $\mathrm B\Sigma_{n+1}$ by :ref{#ex-fo-bsigma-bpi}.
:::
::::


## Notes and references

The finite axiomatizability of $\mathrm I\Sigma_n$ and $\mathrm B\Sigma_{n+1}$, for $n \geq 1$, is Theorem I.2.52 of Hájek and Pudlák, who remark that it is an easy consequence of partial truth definitions and that it is difficult to say who first observed it; their proof is sketched, and the treatment of bounds by variables (:ref{#lem-isigma-star}) is added here. That $\mathrm{PA}$ is not finitely axiomatizable is due to Ryll-Nardzewski (1952), and that it is not axiomatizable by sentences of bounded complexity to Rabin (1961), according to the introduction of Hájek and Pudlák; the proof given here, by models of definable elements, uses the separation of the course on induction and conservation. The provability of $\mathrm{Con}(\mathrm I\Sigma_n)$ in $\mathrm I\Sigma_{n+1}$ is Corollary I.4.34 of Hájek and Pudlák, related there to Leivant (1981) and, for a proof-theoretic proof, Takeuti.

- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Introduction, Chapter I, Sections 2(c) and 4.
- C. Ryll-Nardzewski, *The role of the axiom of induction in elementary arithmetic*, Fundamenta Mathematicae 39 (1952), 239–263.
- M. O. Rabin, *Non-standard models and independence of the induction axiom*, in Essays on the Foundations of Mathematics, Magnes Press, Jerusalem, 1961, 287–299.
- H. Gaifman and C. Dimitracopoulos, *Fragments of Peano's arithmetic and the MRDP theorem*, in Logic and Algorithmic, Monographies de L'Enseignement Mathématique 30, Genève, 1982, 187–206.
