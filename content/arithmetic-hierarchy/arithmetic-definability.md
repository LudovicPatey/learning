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

A terminating computation is a finite object, and checking that a given finite object is a correct computation only requires looking at its finitely many steps. So "the computation of $f(\vec x)$ ends with the value $y$" should be expressible as "there exists a finite sequence $c$ such that $c$ is a correct computation of $f(\vec x)$ ending with $y$", with an existential quantifier over $c$ followed by a check in which every quantifier is bounded by $c$. The difficulty is that the language has no symbol for finite sequences, only $0$, $S$, $+$, $\cdot$ and $<$. Gödel's β-function solves it: finite sequences of any length are coded by pairs of numbers, and the decoding is defined by a bounded formula. The proof below applies this idea to primitive recursive functions, by induction on their definition; the normal form theorem then reduces arbitrary computations to them.

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
A $\Sigma_1$-definable relation is the projection of a relation defined by a bounded formula, which is computable by :ref{#lem-bounded-computable}; so it is c.e. Conversely, by :ref{#thm-kleene-normal-form-proof}, $x \in W_e$ if and only if $\exists s\ T_1(e, x, s)$, with $T_1$ primitive recursive. If $\chi$ is the characteristic function of $T_1$, then $T_1(e, x, s) \iff \chi(e, x, s) = 1$, and the graph of $\chi$ is $\Sigma_1$-definable by :ref{#thm-pr-sigma1}; so $W_e$ is $\Sigma_1$-definable. For a c.e. relation of arity $k$, the same argument applies with $T_k$, since a c.e. relation is the domain of a partial computable function of $k$ arguments. A computable relation and its complement are c.e., which gives the second statement.
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

::::exercise{#ex-exp-beta difficulty=1 objective="Apply the β-function directly to define the graph of exponentiation by a $\Sigma_1$ formula."}
Show that the graph of exponentiation $\{ (x, z, y) : y = x^z \}$ is $\Sigma_1$-definable, by a direct use of the β-function.

:::solution
$y = x^z$ if and only if there are $c, d$ with $\beta(c, d, 0) = 1$, $\beta(c, d, i + 1) = \beta(c, d, i) \cdot x$ for all $i < z$, and $\beta(c, d, z) = y$. Each condition is $\Sigma_1$-definable, using the bounded definition of the graph of $\beta$; the second one by :ref{#lem-sigma1-closure}. The same proof as in :ref{#thm-pr-sigma1} shows that this defines the graph.
:::
::::

## Definable sets are arithmetic

:::theorem{#thm-definable-arithmetic}
A relation is definable in arithmetic if and only if it is arithmetic. More precisely, for $n \geq 1$, a relation is $\Sigma^0_n$ if and only if it is defined by a formula $\exists y_1\, \forall y_2 \cdots Q y_n\ \varphi$ where $\varphi$ is a $\Sigma_1$ formula or the negation of one, according to the parity of $n$.
:::

:::proof{of=thm-definable-arithmetic}
If $A$ is $\Sigma^0_n$, then $\vec x \in A \iff \exists y_1\, \forall y_2 \cdots Q y_n\ R(\vec x, \vec y)$ with $R$ computable, and $R$ is defined both by a $\Sigma_1$ formula and by the negation of one (:ref{#cor-sigma1-ce}); choosing the first when $Q$ is $\exists$ ($n$ odd) and the second when $Q$ is $\forall$ ($n$ even) gives a definition of the stated form. Conversely, in a formula of the stated form, $\varphi$ defines a $\Sigma^0_1$ relation when $n$ is odd and a $\Pi^0_1$ relation when $n$ is even (:ref{#cor-sigma1-ce}). Then $Q y_n\ \varphi$ defines a relation of the same class, by :ref{#prop-hierarchy-closure}, and each of the $n - 1$ remaining quantifiers, of the kind opposite to the one after it, raises the level by one: $\forall y$ in front of a $\Sigma^0_k$ relation gives a $\Pi^0_{k+1}$ relation, and $\exists y$ in front of a $\Pi^0_k$ relation a $\Sigma^0_{k+1}$ relation. The relation defined is therefore $\Sigma^0_n$.

For the first statement, it remains to show that every definable relation is arithmetic, by induction on formulas. Atomic formulas define computable relations. The arithmetic relations are closed under complement, since $\Sigma^0_n$ and $\Pi^0_n$ are complements of each other and $\Pi^0_n \subseteq \Sigma^0_{n+1}$; under finite unions and intersections, since a $\Sigma^0_m$ and a $\Sigma^0_n$ relation are both $\Sigma^0_{\max(m, n)}$; and under quantification, since $\exists y$ applied to a $\Sigma^0_n$ relation gives a $\Sigma^0_n$ relation, and $\forall y$ applied to a $\Sigma^0_n$ relation gives a $\Pi^0_{n+1}$ relation (:ref{#prop-hierarchy-closure}).
:::

## Truth is not arithmetic

Formulas are finite strings over a finite alphabet, and we fix a computable coding $\varphi \mapsto \ulcorner \varphi \urcorner$ of formulas by integers, under which the usual syntactic operations are computable. In particular, given $\ulcorner \varphi(x) \urcorner$ and $n$, the code of the sentence $\varphi(\bar n)$ is computable.

:::theorem[Tarski]{#thm-tarski}
The set $\mathrm{True} = \{ \ulcorner \varphi \urcorner : \varphi \text{ is a sentence and } \nat \models \varphi \}$ is not arithmetic. In particular, it is not definable in arithmetic.
:::

:::proof{of=thm-tarski}
Every arithmetic set $A$ is many-one reducible to $\mathrm{True}$: by :ref{#thm-definable-arithmetic}, some formula $\varphi(x)$ defines $A$, and $n \in A \iff \ulcorner \varphi(\bar n) \urcorner \in \mathrm{True}$, and $n \mapsto \ulcorner \varphi(\bar n) \urcorner$ is computable. Suppose $\mathrm{True}$ is $\Sigma^0_n$. The set $\emptyset^{(n+1)}$ is arithmetic, so it reduces to $\mathrm{True}$, and it would be $\Sigma^0_n$ by :ref{#prop-sigma1-delta1}. But $\Sigma^0_n \subseteq \Pi^0_{n+1}$, and $\emptyset^{(n+1)}$ is not $\Pi^0_{n+1}$ (:ref{#cor-hierarchy-strict}). The second statement follows by :ref{#thm-definable-arithmetic}.
:::

The set $\mathrm{True}$ is in fact Turing equivalent to $\emptyset^{(\omega)} = \{ \langle n, x \rangle : x \in \emptyset^{(n)} \}$, the uniform join of all the finite jumps: the truth of a prenex sentence with $n$ blocks of quantifiers can be decided with the oracle $\emptyset^{(n)}$, uniformly in $n$, and conversely $\emptyset^{(n)}$ is reducible to $\mathrm{True}$, uniformly in $n$. We admit this refinement (see Rogers' book); it is the starting point of the hyperarithmetic hierarchy, which continues the jump along computable ordinals.

:::corollary[First incompleteness theorem]{#cor-incompleteness}
Let $T$ be a set of sentences true in $\nat$ whose set of theorems is c.e. Then some true sentence is not a theorem of $T$.
:::

:::proof{of=cor-incompleteness}
The set of theorems of $T$ is c.e., hence $\Sigma^0_1$, and it is contained in $\mathrm{True}$, since the theorems of a set of true sentences are true. If it were equal to $\mathrm{True}$, then $\mathrm{True}$ would be $\Sigma^0_1$, contradicting :ref{#thm-tarski}.
:::

For a theory given by a computable set of axioms, the set of theorems is c.e., since proofs are finite objects whose correctness is decidable; we admit this, which belongs to a course on logic. Gödel's original theorem is stronger in two respects: for theories that contain a weak fragment of arithmetic, it assumes only the $\omega$-consistency of $T$, not its truth (Rosser (1936) weakened this hypothesis to consistency), and it produces an explicit unprovable sentence.

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

::::exercise{#ex-true-sigma1 difficulty=2 objective="Show that truth for $\Sigma_1$ sentences is $\Sigma^0_1$-complete, by evaluating bounded sentences and arithmetizing the halting set."}
Show that the set of codes of true $\Sigma_1$ sentences is $\Sigma^0_1$-complete.

:::solution
The truth of a bounded sentence is decidable, uniformly in its code, by evaluating it: the quantifiers range over finite sets, whose bounds are values of closed terms. A $\Sigma_1$ sentence $\exists \vec y\ \theta$ is true if and only if some tuple $\vec m$ makes $\theta(\vec{\bar m})$ true, which is a c.e. condition on the code. For completeness, let $\psi(e, x)$ be a $\Sigma_1$ formula defining the relation $\exists s\ T(e, x, s)$, by :ref{#cor-sigma1-ce}. Then $e \in \emptyset' \iff \ulcorner \psi(\bar e, \bar e) \urcorner$ is a true $\Sigma_1$ sentence, and $e \mapsto \ulcorner \psi(\bar e, \bar e) \urcorner$ is computable.
:::
::::

## Notes and references

The β-function and the representation of recursive functions in arithmetic are due to Gödel (1931). The undefinability of truth is due to Tarski (1933, published in German in 1936). The equivalence between definability and the arithmetic hierarchy is due to Kleene (1943) and Mostowski (1947). Smoryński's book and Kaye's book on models of Peano arithmetic give detailed treatments; the definability of computable relations is Theorem 3.3 in Kaye's book, as cited by Nies (Section 1.4). Monin and Patey prove the representation of primitive recursive functions with the β-function in the section on Gödel's incompleteness theorems of their chapter *Formal interlude*, where the hierarchy of formulas is also compared with the arithmetic hierarchy.

- K. Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte für Mathematik und Physik 38 (1931), 173–198.
- A. Tarski, *Der Wahrheitsbegriff in den formalisierten Sprachen*, Studia Philosophica 1 (1936), 261–405.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
- C. Smoryński, *Logical Number Theory I*, Springer, 1991.
- J. B. Rosser, *Extensions of some theorems of Gödel and Church*, Journal of Symbolic Logic 1 (1936), 87–91.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.4.
- B. Monin and L. Patey, *Computability theory*, chapter *Formal interlude*.

:::::exercises
::::exercise{#ex-computable-sigma1 difficulty=1 objective="Characterize the computable sets by $\Sigma_1$ definitions of the set and of its complement."}
Show that a set is computable if and only if it is defined both by a $\Sigma_1$ formula and by the negation of a $\Sigma_1$ formula.

:::solution
By :ref{#cor-sigma1-ce}, a set defined by a $\Sigma_1$ formula is c.e., and a set defined by the negation of a $\Sigma_1$ formula is co-c.e.; a set that is both is computable (:ref{#prop-computable-iff-ce-coce}). The converse is the second statement of the corollary.
:::
::::

::::exercise{#ex-bounded-definitions difficulty=1 objective="Write bounded formulas for basic arithmetic relations, choosing the bounds of the quantifiers."}
Write bounded formulas defining in $\nat$ the following relations, where $1$ abbreviates the numeral $S(0)$.

1. $x \leq y$.
2. $x$ divides $y$.
3. $x$ is prime.
4. $x$ is a power of $2$.

:::solution
1. $x < y \vee x = y$.
2. $\exists q < S(y)\ (q \cdot x = y)$. If $x$ divides $y$, then $y = q x$ for some $q$; if $y = 0$, take $q = 0$; if $y > 0$, then $x \geq 1$ and $q \leq y$. So the bound $q < S(y)$ loses no witness.
3. $1 < x \wedge \forall u < x\ \forall v < x\ \neg (u \cdot v = x)$. If $x > 1$ is composite, $x = u v$ with $1 < u, v < x$. Conversely, if $x = u v$ with $u, v < x$, then $u, v \geq 2$ (if $u \leq 1$, then $u v = x$ forces $v = x$ or $x = 0$), so $x$ is composite. Hence the formula holds exactly for the primes.
4. $0 < x \wedge \forall u < S(x)\ \forall v < S(x)\ \big( u \cdot v = x \to (u = 1 \vee \exists w < u\ (u = w + w)) \big)$: every divisor of $x$ other than $1$ is even. A positive integer is a power of $2$ if and only if it has no odd divisor larger than $1$, by uniqueness of the prime decomposition; and the divisors $u$ of $x > 0$, with their cofactors $v$, are at most $x$.
:::
::::

::::exercise{#ex-beta-example difficulty=1 objective="Compute codes of a short sequence by the β-function, and compare with the pair given by the proof of Gödel's lemma."}
Consider the sequence $(2, 1, 0)$.

1. Check that $\beta(56, 2, i) = 2, 1, 0$ for $i = 0, 1, 2$.
2. Show that no pair $(c, d)$ with $d \leq 1$ codes this sequence, and that $56$ is the least $c$ such that $(c, 2)$ codes it.
3. Compute the value of $d$ given by the proof of :ref{#lem-beta}, and the least $c$ that works with it.

:::solution
1. The moduli are $1 + (i + 1) \cdot 2 = 3, 5, 7$, and $56 = 18 \cdot 3 + 2 = 11 \cdot 5 + 1 = 8 \cdot 7$.
2. With $d = 0$ every modulus is $1$, and $\beta(c, 0, i) = 0$. With $d = 1$ the first modulus is $2$, so $\beta(c, 1, 0) \leq 1 < 2$. With $d = 2$, the conditions are $c \equiv 2 \pmod 3$, $c \equiv 1 \pmod 5$, $c \equiv 0 \pmod 7$; since $3, 5, 7$ are pairwise coprime, by the Chinese remainder theorem they determine $c$ modulo $105$, so $56$, which satisfies them and is less than $105$, is the least solution.
3. The proof takes $m = \max(3, 2, 1, 0) = 3$ and $d = 3! = 6$. The moduli are $7, 13, 19$, and the conditions are $c \equiv 2 \pmod 7$, $c \equiv 1 \pmod{13}$, $c \equiv 0 \pmod{19}$. The multiples of $19$ that are $\equiv 1 \pmod{13}$ are those $19 k$ with $6 k \equiv 1 \pmod{13}$, that is $k \equiv 11 \pmod{13}$, which gives $c \equiv 209 \pmod{247}$. Then $209 + 247 j \equiv 6 + 2 j \pmod 7$, which is $2$ for $j \equiv 5 \pmod 7$. So $c = 209 + 5 \cdot 247 = 1444$, the least solution modulo $7 \cdot 13 \cdot 19 = 1729$. Check: $1444 = 206 \cdot 7 + 2 = 111 \cdot 13 + 1 = 76 \cdot 19$. The proof of the lemma aims at a uniform argument, not at small codes.
:::
::::

::::exercise[Truth at each level]{#ex-true-sigma-n difficulty=2 objective="Show that truth for prenex sentences with n quantifier alternations is $\Sigma^0_n$-complete, and derive Tarski's theorem again."}
For $n \geq 1$, call a sentence **strictly $\Sigma_n$** if it is of the form $\exists y_1\ \forall y_2 \cdots Q y_n\ \theta$, with $n$ single alternating quantifiers and $\theta$ bounded. Let $\mathrm{Tr}_n$ be the set of codes of the true strictly $\Sigma_n$ sentences.

1. Show that $\mathrm{Tr}_n$ is $\Sigma^0_n$-complete.
2. Deduce that $\mathrm{True}$ is not $\Sigma^0_n$ for any $n$.

:::solution
1. *Upper bound.* The set $S_n$ of codes of strictly $\Sigma_n$ sentences is computable, and so is the function that sends the code of $\exists y_1 \cdots Q y_n\ \theta$ and integers $m_1, \dots, m_n$ to the code of the bounded sentence $\theta(\bar m_1, \dots, \bar m_n)$ (with value the code of $0 = S(0)$ when the first argument is not in $S_n$). The truth of a bounded sentence is decidable, uniformly in its code, as in :ref{#ex-true-sigma1}. Since every element of $\nat$ is the value of a numeral, a sentence $\exists y\ \varphi(y)$ is true if and only if $\varphi(\bar m)$ is true for some $m$, and similarly for $\forall$. Hence $e \in \mathrm{Tr}_n$ if and only if $e \in S_n$ and $\exists m_1\ \forall m_2 \cdots Q m_n$ the bounded sentence computed from $(e, m_1, \dots, m_n)$ is true: a computable relation preceded by $n$ alternating quantifiers, so $\mathrm{Tr}_n$ is $\Sigma^0_n$.

   *Lower bound.* Let $A$ be $\Sigma^0_n$. By :ref{#thm-definable-arithmetic}, $A$ is defined by a formula $\exists y_1\ \forall y_2 \cdots Q y_n\ \varphi(x, \vec y)$ with $\varphi$ a $\Sigma_1$ formula $\exists \vec z\ \eta$, $\eta$ bounded, if $n$ is odd, and the negation of one if $n$ is even. If $n$ is odd, $Q$ is $\exists$, and in $\nat$
$$
\exists y_n\ \exists \vec z\ \eta \iff \exists w\ \exists y_n < w\ \exists z_1 < w \cdots \exists z_k < w\ \eta,
$$
   with $w$ a new variable: take $w$ larger than the witnesses. If $n$ is even, $Q$ is $\forall$, and $\forall y_n\ \neg \exists \vec z\ \eta$ is equivalent to $\forall w\ \forall y_n < w\ \forall z_1 < w \cdots \forall z_k < w\ \neg \eta$. In both cases $A$ is defined by a strictly $\Sigma_n$ formula $\psi(x)$, obtained by replacing $Q y_n\ \varphi$ by the formula with the single quantifier on $w$. Then $x \in A \iff \ulcorner \psi(\bar x) \urcorner \in \mathrm{Tr}_n$, and $x \mapsto \ulcorner \psi(\bar x) \urcorner$ is computable.
2. $\mathrm{Tr}_{n+1} = \mathrm{True} \cap S_{n+1}$. If $\mathrm{True}$ were $\Sigma^0_n$, then $\mathrm{Tr}_{n+1}$ would be $\Sigma^0_n$, as the intersection with a computable set, hence $\Pi^0_{n+1}$. But a $\Sigma^0_{n+1}$-complete set is not $\Pi^0_{n+1}$, since $\emptyset^{(n+1)}$ reduces to it and is not $\Pi^0_{n+1}$ (:ref{#cor-hierarchy-strict}).
:::
::::

::::exercise{#ex-incompleteness-pi1 difficulty=2 objective="Find the unprovable true sentences of the incompleteness theorem among the negations of $\Sigma_1$ sentences."}
Let $T$ be as in :ref{#cor-incompleteness}: a set of sentences true in $\nat$ whose set of theorems is c.e. Show that some true sentence of the form $\neg \sigma$, with $\sigma$ a $\Sigma_1$ sentence, is not a theorem of $T$.

:::solution
By :ref{#cor-sigma1-ce}, there is a $\Sigma_1$ formula $\psi(e, x)$ defining the relation $x \in W_e$. Let $\sigma_e$ be the $\Sigma_1$ sentence $\psi(\bar e, \bar e)$, so that $\sigma_e$ is true if and only if $e \in \emptyset'$. The map $e \mapsto \ulcorner \neg \sigma_e \urcorner$ is computable.

Suppose that every true sentence $\neg \sigma_e$ is a theorem of $T$. Since the theorems of $T$ are true, $e \notin \emptyset' \iff \neg \sigma_e \text{ is true} \iff \neg \sigma_e$ is a theorem of $T$. The set of theorems is c.e., so $\{ e : \neg \sigma_e \text{ is a theorem} \}$ is c.e., as the preimage of a c.e. set by a computable function. Then $\nat \setminus \emptyset'$ would be c.e., and $\emptyset'$ computable: a contradiction.

The sentence $\neg \sigma_e$ states that the computation $\Phi_e(e)$ does not halt. So the unprovable true sentences can be chosen of a very simple form, equivalent in $\nat$ to $\forall s$ followed by a bounded formula.
:::
::::
:::::
