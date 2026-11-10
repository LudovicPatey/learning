---
title: Arithmetic definability
summary: The arithmetic sets are the sets definable in the language of arithmetic; Σ₁-definable means c.e.; truth in ℕ is not arithmetic, and the first incompleteness theorem.
duration: 40
prerequisites: [post-theorem, models-of-computation/coding-sequences]
---

The name of the arithmetic hierarchy comes from logic: its sets are exactly the sets definable by a first-order formula in the language of arithmetic, with addition and multiplication, interpreted in the natural numbers. The number of quantifier alternations of the formula is the level in the hierarchy. The difficult direction is to express computations by formulas, which is done with Gödel's β-function. Two classical results follow: truth in $\nat$ cannot be defined in arithmetic (Tarski), and no computably axiomatized theory proves all true sentences of arithmetic (Gödel).

## The language of arithmetic

The **language of arithmetic** has a constant $0$, a unary function symbol $S$, binary function symbols $+$ and $\cdot$, and a binary relation symbol $<$, together with equality. **Terms** are built from variables and $0$ with $S$, $+$ and $\cdot$; **formulas** from equations $t_1 = t_2$ and inequalities $t_1 < t_2$ between terms with $\neg$, $\wedge$, $\vee$, $\to$, $\exists x$ and $\forall x$. Formulas are interpreted in the **standard model** $\nat$, with the usual operations. For a formula $\varphi(x_1, \dots, x_k)$ and integers $\vec n$, we write $\nat \models \varphi(\vec n)$ if $\varphi$ holds in $\nat$ when $x_i$ is interpreted as $n_i$. The **numeral** of $n$ is the term $\bar n = S(S(\cdots S(0) \cdots))$ with $n$ symbols $S$.

:::definition{#def-definable}
A relation $A \subseteq \nat^k$ is **definable** (in arithmetic) if there is a formula $\varphi(x_1, \dots, x_k)$ with $\vec n \in A \iff \nat \models \varphi(\vec n)$ for every $\vec n$.
:::

:::definition{#def-bounded-formula}
A formula is **bounded** if every quantifier in it has the form $\exists y\, (y < t \wedge \cdots)$ or $\forall y\, (y < t \to \cdots)$, written $\exists y < t$ and $\forall y < t$, where $t$ is a term not containing $y$. A **$\Sigma_1$ formula** is a formula $\exists y_1 \cdots \exists y_m\ \theta$ with $\theta$ bounded, and a relation is **$\Sigma_1$-definable** if it is defined by a $\Sigma_1$ formula.
:::

:::lemma{#lem-bounded-computable}
Every relation defined by a bounded formula is primitive recursive.
:::

:::proof{of=lem-bounded-computable}
The value of a term is a primitive recursive function of its variables, by induction on the term, since successor, addition and multiplication are primitive recursive. The relations $=$ and $<$ are primitive recursive, and primitive recursive relations are closed under Boolean operations and bounded quantifiers whose bound is a primitive recursive function of the free variables (:ref{#cor-pr-bounded-quantifiers}). The result follows by induction on the formula.
:::

:::lemma[Closure of Σ₁-definable relations]{#lem-sigma1-closure}
The $\Sigma_1$-definable relations are closed under conjunction, disjunction, existential quantification, bounded existential quantification, and bounded universal quantification $\forall z < t$.
:::

:::proof{of=lem-sigma1-closure}
For conjunction and disjunction, rename the bound variables apart and move the existential quantifiers to the front: $\exists \vec y\ \theta \wedge \exists \vec z\ \eta$ is equivalent to $\exists \vec y\, \exists \vec z\, (\theta \wedge \eta)$. Existential quantification is immediate, and $\exists z < t\ \exists \vec y\ \theta$ is equivalent to $\exists z\, \exists \vec y\, (z < t \wedge \theta)$. For bounded universal quantification, the **collection** principle holds in $\nat$:
$$
\nat \models \forall z < t\ \exists \vec y\ \theta \iff \nat \models \exists b\ \forall z < t\ \exists \vec y < b\ \theta,
$$
where $\exists \vec y < b$ abbreviates $\exists y_1 < b \cdots \exists y_m < b$. From left to right, choose witnesses for each of the finitely many values of $z$ and let $b$ exceed all of them. The right-hand side is a $\Sigma_1$ formula.
:::

The equivalences are equivalences **in $\nat$**: the formulas are not syntactically $\Sigma_1$, but they define the same relations as $\Sigma_1$ formulas. This is all that matters for definability.

## Computations are Σ₁-definable

:::theorem{#thm-pr-sigma1}
For every primitive recursive function $f : \nat^k \to \nat$, the graph $\{ (\vec x, y) : f(\vec x) = y \}$ is $\Sigma_1$-definable.
:::

:::proof{of=thm-pr-sigma1}
By induction on the definition of $f$ as a primitive recursive function. The basic functions have the bounded definitions $y = 0$, $y = S(x)$ and $y = x_i$.

*Composition.* If $f(\vec x) = h(g_1(\vec x), \dots, g_m(\vec x))$ and the graphs of $h$ and of the $g_i$ are defined by $\Sigma_1$ formulas $\psi_h$ and $\psi_{g_i}$, then
$$
f(\vec x) = y \iff \exists z_1 \cdots \exists z_m\ \Big( \textstyle\bigwedge_i \psi_{g_i}(\vec x, z_i) \wedge \psi_h(\vec z, y) \Big),
$$
which is $\Sigma_1$-definable by :ref{#lem-sigma1-closure}.

*Primitive recursion.* Let $f(\vec x, 0) = g(\vec x)$ and $f(\vec x, n + 1) = h(\vec x, n, f(\vec x, n))$. A computation of $f(\vec x, n)$ is the finite sequence of values $f(\vec x, 0), \dots, f(\vec x, n)$, which by Gödel's lemma (:ref{#lem-beta}) is represented by two integers $c, d$ through the β-function $\beta(c, d, i) = c \bmod (1 + (i + 1) d)$ (:ref{#def-beta}). The graph of $\beta$ is defined by the bounded formula
$$
\beta(c, d, i) = r \iff \exists q < c + 1\ \ \big( c = q \cdot (1 + (i + 1) d) + r \ \wedge\ r < 1 + (i + 1) d \big).
$$
Then $f(\vec x, n) = y$ if and only if there are $c$ and $d$ such that $\beta(c, d, 0) = g(\vec x)$, such that $\beta(c, d, i + 1) = h(\vec x, i, \beta(c, d, i))$ for every $i < n$, and such that $\beta(c, d, n) = y$. Indeed, if these conditions hold, the values $\beta(c, d, i)$ are $f(\vec x, i)$ by induction on $i \leq n$; conversely, Gödel's lemma provides $c$ and $d$ encoding the sequence $f(\vec x, 0), \dots, f(\vec x, n)$. Written with the formulas for the graphs of $g$, $h$ and $\beta$, each condition is $\Sigma_1$-definable, the second one by bounded universal quantification over a $\Sigma_1$-definable relation. By :ref{#lem-sigma1-closure}, the graph of $f$ is $\Sigma_1$-definable.
:::

:::corollary{#cor-sigma1-ce}
A relation is $\Sigma_1$-definable if and only if it is c.e. Every computable relation is defined both by a $\Sigma_1$ formula and by the negation of a $\Sigma_1$ formula.
:::

:::proof{of=cor-sigma1-ce}
A $\Sigma_1$-definable relation is the projection of a relation defined by a bounded formula, which is computable by :ref{#lem-bounded-computable}; so it is c.e. Conversely, by :ref{#thm-kleene-normal-form-proof}, $x \in W_e$ if and only if $\exists s\ T(e, x, s)$, with $T$ primitive recursive. If $\chi$ is the characteristic function of $T$, then $T(e, x, s) \iff \chi(e, x, s) = 1$, and the graph of $\chi$ is $\Sigma_1$-definable by :ref{#thm-pr-sigma1}; so $W_e$ is $\Sigma_1$-definable. A computable relation and its complement are c.e., which gives the second statement.
:::

:::quiz[computations are Σ₁-definable]
In the case of primitive recursion, why is the β-function needed?

- [x] To quantify over the whole finite sequence of intermediate values $f(\vec x, 0), \dots, f(\vec x, n)$ with a fixed number of quantifiers, here two, over integers.

  The length of the sequence depends on $n$; the β-function codes sequences of any length by two numbers, with a bounded formula for decoding.
- [ ] Because the language has no symbol for $f$.

  This is the general problem; the specific difficulty of primitive recursion is the sequence of unbounded length.
- [ ] To make the formula bounded.

  The resulting formula is $\Sigma_1$, not bounded.

---

Where is the collection principle used in the proof of :ref{#thm-pr-sigma1}?

- [x] In the condition "for every $i < n$, $\beta(c, d, i + 1) = h(\vec x, i, \beta(c, d, i))$", a bounded universal quantifier in front of a $\Sigma_1$ formula.
- [ ] In the case of composition.

  Composition only uses conjunctions and existential quantifiers.
- [ ] In the definition of the graph of $\beta$.

  That definition is bounded.
:::

## Definable sets are arithmetic

:::theorem{#thm-definable-arithmetic}
A relation is definable in arithmetic if and only if it is arithmetic. More precisely, for $n \geq 1$, a relation is $\Sigma^0_n$ if and only if it is defined by a formula $\exists y_1\, \forall y_2 \cdots Q y_n\ \varphi$ where $\varphi$ is a $\Sigma_1$ formula or the negation of one, according to the parity of $n$.
:::

:::proof{of=thm-definable-arithmetic}
If $A$ is $\Sigma^0_n$, then $\vec x \in A \iff \exists y_1\, \forall y_2 \cdots Q y_n\ R(\vec x, \vec y)$ with $R$ computable, and $R$ is defined both by a $\Sigma_1$ formula and by the negation of one (:ref{#cor-sigma1-ce}); choosing the first when $Q$ is $\exists$ and the second when $Q$ is $\forall$, and contracting the last quantifier with the formula, gives a definition of the stated form.

Conversely, the relations defined by formulas are arithmetic, by induction on formulas. Atomic formulas define computable relations. The arithmetic relations are closed under complement, since $\Sigma^0_n$ and $\Pi^0_n$ are complements of each other and $\Pi^0_n \subseteq \Sigma^0_{n+1}$; under finite unions and intersections, since a $\Sigma^0_m$ and a $\Sigma^0_n$ relation are both $\Sigma^0_{\max(m, n)}$; and under quantification, since $\exists y$ applied to a $\Sigma^0_n$ relation gives a $\Sigma^0_n$ relation, and $\forall y$ applied to a $\Sigma^0_n$ relation gives a $\Pi^0_{n+1}$ relation (:ref{#prop-hierarchy-closure}).
:::

## Truth is not arithmetic

Formulas are finite strings over a finite alphabet, and we fix a computable coding $\varphi \mapsto \ulcorner \varphi \urcorner$ of formulas by integers, under which the usual syntactic operations are computable. In particular, given $\ulcorner \varphi(x) \urcorner$ and $n$, the code of the sentence $\varphi(\bar n)$ is computable.

:::theorem[Tarski]{#thm-tarski}
The set $\mathrm{True} = \{ \ulcorner \varphi \urcorner : \varphi \text{ is a sentence and } \nat \models \varphi \}$ is not arithmetic. In particular, it is not definable in arithmetic.
:::

:::proof{of=thm-tarski}
Every arithmetic set $A$ is many-one reducible to $\mathrm{True}$: if $\varphi(x)$ defines $A$, then $n \in A \iff \ulcorner \varphi(\bar n) \urcorner \in \mathrm{True}$, and $n \mapsto \ulcorner \varphi(\bar n) \urcorner$ is computable. Suppose $\mathrm{True}$ is $\Sigma^0_n$. The set $\emptyset^{(n+1)}$ is arithmetic, so it reduces to $\mathrm{True}$, and it would be $\Sigma^0_n$ by :ref{#prop-sigma1-delta1}. But $\Sigma^0_n \subseteq \Pi^0_{n+1}$, and $\emptyset^{(n+1)}$ is not $\Pi^0_{n+1}$ (:ref{#cor-hierarchy-strict}). The second statement follows by :ref{#thm-definable-arithmetic}.
:::

The set $\mathrm{True}$ is in fact Turing equivalent to $\emptyset^{(\omega)} = \{ \langle n, x \rangle : x \in \emptyset^{(n)} \}$, the uniform join of all the finite jumps: deciding the truth of a sentence with $n$ quantifier alternations requires $\emptyset^{(n)}$, uniformly in $n$. We admit this refinement; it is the starting point of the hyperarithmetic hierarchy, which continues the jump along computable ordinals.

:::corollary[First incompleteness theorem]{#cor-incompleteness}
Let $T$ be a set of sentences true in $\nat$ whose set of theorems is c.e. Then some true sentence is not a theorem of $T$.
:::

:::proof{of=cor-incompleteness}
The set of theorems of $T$ is c.e., hence $\Sigma^0_1$, and it is contained in $\mathrm{True}$, since the theorems of a set of true sentences are true. If it were equal to $\mathrm{True}$, then $\mathrm{True}$ would be $\Sigma^0_1$, contradicting :ref{#thm-tarski}.
:::

For a theory given by a computable set of axioms, the set of theorems is c.e., since proofs are finite objects whose correctness is decidable; we admit this, which belongs to a course on logic. Gödel's original theorem is stronger in two respects: it only assumes the consistency of $T$ (or its $\omega$-consistency), not its truth, and it produces an explicit unprovable sentence.

:::quiz[Tarski and Gödel]
Why does the proof of :ref{#thm-tarski} use the set $\emptyset^{(n+1)}$ rather than $\emptyset^{(n)}$?

- [x] Because $\emptyset^{(n)}$ is $\Sigma^0_n$, so reducing it to a $\Sigma^0_n$ set gives no contradiction; $\emptyset^{(n+1)}$ is not even $\Pi^0_{n+1}$, hence not $\Sigma^0_n$.
- [ ] Because $\emptyset^{(n)}$ is not arithmetic.

  It is $\Sigma^0_n$.
- [ ] Because $\emptyset^{(n)}$ does not reduce to $\mathrm{True}$.

  Every arithmetic set reduces to $\mathrm{True}$.

---

Which property of $T$ is used in :ref{#cor-incompleteness} to conclude that the theorems of $T$ form a proper subset of $\mathrm{True}$?

- [x] That the set of theorems is $\Sigma^0_1$, while $\mathrm{True}$ is not arithmetic.

  The inclusion uses the truth of the axioms; the strictness uses only the complexity of the set of theorems.
- [ ] That $T$ is finite.

  $T$ may be infinite, as long as its theorems are c.e.
- [ ] That $T$ is consistent.

  Consistency follows from truth, but the argument uses truth and complexity.
:::

## Exercises

::::exercise{difficulty=1}
Show that the graph of exponentiation $\{ (x, z, y) : y = x^z \}$ is $\Sigma_1$-definable, by a direct use of the β-function.

:::solution
$y = x^z$ if and only if there are $c, d$ with $\beta(c, d, 0) = 1$, $\beta(c, d, i + 1) = \beta(c, d, i) \cdot x$ for all $i < z$, and $\beta(c, d, z) = y$. Each condition is $\Sigma_1$-definable, using the bounded definition of the graph of $\beta$; the second one by :ref{#lem-sigma1-closure}. The same proof as in :ref{#thm-pr-sigma1} shows that this defines the graph.
:::
::::

::::exercise{difficulty=1}
Show that a set is computable if and only if it is defined both by a $\Sigma_1$ formula and by the negation of a $\Sigma_1$ formula.

:::solution
By :ref{#cor-sigma1-ce}, a set defined by a $\Sigma_1$ formula is c.e., and a set defined by the negation of a $\Sigma_1$ formula is co-c.e.; a set that is both is computable (:ref{#prop-computable-iff-ce-coce}). The converse is the second statement of the corollary.
:::
::::

::::exercise{difficulty=2}
Show that the set of codes of true $\Sigma_1$ sentences is $\Sigma^0_1$-complete.

:::solution
The truth of a bounded sentence is decidable, uniformly in its code, by evaluating it: the quantifiers range over finite sets, whose bounds are values of closed terms. A $\Sigma_1$ sentence $\exists \vec y\ \theta$ is true if and only if some tuple $\vec m$ makes $\theta(\vec{\bar m})$ true, which is a c.e. condition on the code. For completeness, let $\psi(e, x)$ be a $\Sigma_1$ formula defining the relation $\exists s\ T(e, x, s)$, by :ref{#cor-sigma1-ce}. Then $e \in \emptyset' \iff \ulcorner \psi(\bar e, \bar e) \urcorner$ is a true $\Sigma_1$ sentence, and $e \mapsto \ulcorner \psi(\bar e, \bar e) \urcorner$ is computable.
:::
::::

## Notes and references

The β-function and the representation of recursive functions in arithmetic are due to Gödel (1931). The undefinability of truth is due to Tarski (1933, published in German in 1936). The equivalence between definability and the arithmetic hierarchy is due to Kleene (1943) and Mostowski (1947). Smoryński's book and Kaye's book on models of Peano arithmetic give detailed treatments.

- K. Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte für Mathematik und Physik 38 (1931), 173–198.
- A. Tarski, *Der Wahrheitsbegriff in den formalisierten Sprachen*, Studia Philosophica 1 (1936), 261–405.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
- C. Smoryński, *Logical Number Theory I*, Springer, 1991.
