---
title: The language and models of second-order arithmetic
summary: The two-sorted language of second-order arithmetic, its formula classes, the axioms of Z₂, Henkin structures and ω-models, absoluteness of arithmetic formulas, and the program of reverse mathematics.
duration: 45
prerequisites: [arithmetic-hierarchy/arithmetic-definability]
---

Reverse mathematics asks which set-existence axioms are needed to prove a given theorem of ordinary mathematics. The framework, proposed by Friedman (1975) and developed by Simpson, is **second-order arithmetic**: a theory of natural numbers and sets of natural numbers. Countable objects of analysis, algebra and combinatorics (real numbers, continuous functions on the reals, countable groups, colorings of pairs) can be coded by sets of numbers, so that their theorems become statements of second-order arithmetic. One then works in a weak **base theory** and proves equivalences between theorems and axioms. An empirical observation is that most of the theorems studied so far are either provable in the base theory or equivalent over it to one of four stronger systems; together with the base theory, these form the **Big Five**.

This lesson fixes the language, the axioms and the models. The semantics is that of first-order logic with two sorts: set variables may range over any collection of sets, not necessarily all of them. This makes the completeness theorem available, and with it the main method for unprovability: build a model. The most useful models are the **ω-models**, whose numbers are the true natural numbers, and in which arithmetic statements mean what they mean in reality. Throughout, the reader is assumed to know the language of first-order arithmetic and the arithmetic hierarchy (:ref{to="arithmetic-hierarchy/arithmetic-definability"}).

## The language

:::definition{#def-l2}
The language $\mathcal L_2$ of second-order arithmetic has two sorts of variables: **number variables** $x, y, z, \dots$, intended to range over $\nat$, and **set variables** $X, Y, Z, \dots$, intended to range over subsets of $\nat$. Its non-logical symbols are the constants $0, 1$, the binary function symbols $+, \cdot$, the binary relation symbols $=, <$ on numbers, and the membership symbol $\in$ between a number and a set.

- **Terms** are built from number variables and constants with $+$ and $\cdot$; there are no set terms other than set variables.
- **Atomic formulas** are $t_1 = t_2$, $t_1 < t_2$ and $t \in X$, for terms $t_1, t_2, t$ and a set variable $X$.
- **Formulas** are built from atomic formulas with the connectives and the quantifiers $\forall x, \exists x$ over numbers and $\forall X, \exists X$ over sets.
:::

Equality between sets is not primitive; $X = Y$ abbreviates the $\Pi^0_1$ formula $\forall n\, (n \in X \leftrightarrow n \in Y)$, so that atomic formulas remain decidable relative to their parameters.

Formulas are classified by their quantifiers, allowing free variables of both sorts, called **parameters**.

- A formula is **bounded**, or $\Sigma^0_0 = \Pi^0_0 = \Delta^0_0$, if all its quantifiers are number quantifiers of the form $\forall x < t$ or $\exists x < t$, with $t$ a term not containing $x$.
- A formula is $\Sigma^0_{n+1}$ if it has the form $\exists x\, \varphi$ with $\varphi$ a $\Pi^0_n$ formula, and $\Pi^0_{n+1}$ if it has the form $\forall x\, \varphi$ with $\varphi$ a $\Sigma^0_n$ formula; blocks of quantifiers of the same kind count as one.
- A formula is **arithmetic** if it contains no set quantifier. It may contain free set variables.
- A formula is $\Sigma^1_1$ if it has the form $\exists X\, \varphi$ with $\varphi$ arithmetic, and $\Pi^1_1$ if it has the form $\forall X\, \varphi$ with $\varphi$ arithmetic; similarly for $\Sigma^1_n$ and $\Pi^1_n$.

A formula is often said to be $\Sigma^0_n$ when it is only equivalent to a $\Sigma^0_n$ formula; the equivalence must then hold in the theory at hand.

With a set parameter $A$, the $\Sigma^0_1$ formulas define exactly the $A$-c.e. sets: this is the relativization of :ref{#cor-sigma1-ce}, by the same proof. Consequently the $\Sigma^0_n$ formulas with parameter $A$ define the $\Sigma^0_n(A)$ sets of :ref{#def-relativized-hierarchy}.

:::example{#ex-formalization}
Pairs of numbers are coded by numbers with the term $\langle m, n \rangle = (m + n)^2 + m$, which is injective (Simpson, Theorem II.2.2, proves this in the base theory of the next lesson). A function $f : \nat \to \nat$ is coded by its graph $\{ \langle n, m \rangle : f(n) = m \}$, and "$X$ is (the graph of) a function from $\nat$ to $\nat$" is the $\Pi^0_2$ formula
$$
\forall n\, \exists m\, \langle n, m \rangle \in X \;\wedge\; \forall n\, \forall m\, \forall m'\, \big( (\langle n, m \rangle \in X \wedge \langle n, m' \rangle \in X) \rightarrow m = m' \big).
$$
"$X$ is infinite" is the $\Pi^0_2$ formula $\forall m\, \exists n\, (n > m \wedge n \in X)$. The statement "every function from $\nat$ to $\nat$ has a range" reads
$$
\forall X\, \Big( X \text{ is a function} \rightarrow \exists Y\, \forall m\, \big( m \in Y \leftrightarrow \exists n\, \langle n, m \rangle \in X \big) \Big),
$$
a $\Pi^1_2$ sentence once the arithmetic part is put in prenex form after $\exists Y$.
:::

Most theorems studied in reverse mathematics have this shape: $\forall X\, (\varphi(X) \rightarrow \exists Y\, \psi(X, Y))$ with $\varphi, \psi$ arithmetic. The sets $X$ satisfying $\varphi$ are the **instances** of the theorem, and the sets $Y$ with $\psi(X, Y)$ its **solutions**. This view of a theorem as a problem is developed in the course on reducibilities (:ref{to="reducibilities/weihrauch"}).

## The axioms

:::definition{#def-z2}
The **basic axioms** are the universal closures of
$$
\begin{gathered}
n + 1 \neq 0, \qquad m + 1 = n + 1 \rightarrow m = n, \qquad m + 0 = m, \qquad m + (n + 1) = (m + n) + 1, \\
m \cdot 0 = 0, \qquad m \cdot (n + 1) = (m \cdot n) + m, \qquad \neg (m < 0), \qquad m < n + 1 \leftrightarrow (m < n \vee m = n).
\end{gathered}
$$
The **induction axiom** is
$$
\forall X\, \big( (0 \in X \wedge \forall n\, (n \in X \rightarrow n + 1 \in X)) \rightarrow \forall n\, (n \in X) \big).
$$
For a class $\Gamma$ of formulas, the **$\Gamma$ comprehension scheme** consists of the universal closures of
$$
\exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n))
$$
for $\varphi \in \Gamma$ in which $X$ does not occur free. The **$\Gamma$ induction scheme** consists of the universal closures of
$$
(\varphi(0) \wedge \forall n\, (\varphi(n) \rightarrow \varphi(n+1))) \rightarrow \forall n\, \varphi(n)
$$
for $\varphi \in \Gamma$. **Second-order arithmetic** $\mathsf Z_2$ is the theory consisting of the basic axioms, the induction axiom, and the comprehension scheme for all formulas of $\mathcal L_2$.
:::

The parameters of $\varphi$ are universally quantified: comprehension asserts that, for all values of the other free variables, the set defined by $\varphi$ exists. For instance, the instance $\forall Y\, \exists X\, \forall n\, (n \in X \leftrightarrow n \notin Y)$, for the bounded formula $n \notin Y$ with parameter $Y$, asserts that every set has a complement. Comprehension for formulas with set quantifiers is **impredicative**: the set $X$ is defined by quantifying over all sets, including $X$ itself. The subsystems studied in reverse mathematics restrict comprehension, and induction with it.

:::proposition{#prop-induction-comprehension}
If $\Gamma$ comprehension holds, the induction axiom implies the $\Gamma$ induction scheme.
:::

:::proof{of=prop-induction-comprehension}
Let $\varphi \in \Gamma$ with $\varphi(0)$ and $\forall n\, (\varphi(n) \rightarrow \varphi(n+1))$. By $\Gamma$ comprehension, the set $X = \{ n : \varphi(n) \}$ exists. It contains $0$ and is closed under successor, so it contains every $n$ by the induction axiom: $\varphi(n)$ holds for all $n$.
:::

In particular $\mathsf Z_2$ proves the induction scheme for all formulas.

## Structures and ω-models

:::definition{#def-l2-structure}
An **$\mathcal L_2$-structure** is a tuple $\mathcal M = (M, \mathcal S, +^{\mathcal M}, \cdot^{\mathcal M}, <^{\mathcal M}, 0^{\mathcal M}, 1^{\mathcal M})$ where $M$ is a non-empty set, the **first-order part**, $\mathcal S \subseteq \mathcal P(M)$ is the **second-order part**, $+^{\mathcal M}, \cdot^{\mathcal M}$ are binary operations on $M$, $<^{\mathcal M}$ is a binary relation on $M$, and $0^{\mathcal M}, 1^{\mathcal M} \in M$. Number variables range over $M$, set variables over $\mathcal S$, and $\in$ is interpreted as membership.
:::

Satisfaction $\mathcal M \models \varphi$ is defined as usual, the set quantifiers ranging over $\mathcal S$ only. Such structures are **Henkin structures**; a structure with $\mathcal S = \mathcal P(M)$ is a **full** structure. With Henkin semantics, the logic of $\mathcal L_2$ is essentially first-order logic with two sorts, and enjoys the completeness theorem: a sentence is provable in a theory $T$ if and only if it holds in every model of $T$. We admit this result: it is the completeness theorem for many-sorted first-order logic, which reduces to the one-sorted case by adding a unary predicate for each sort (see Simpson, Section I.2, and Dzhafarov–Mummert, Theorem 5.1.5). In particular, to show that $T$ does not prove $\varphi$, it suffices to exhibit a model of $T$ in which $\varphi$ fails.

:::definition{#def-omega-model}
An **ω-model** is a structure whose first-order part is $\nat$ with the usual operations and order. It is determined by its second-order part $\mathcal S \subseteq \mathcal P(\nat)$, and we identify the two.
:::

The structure $\mathcal P(\nat)$ is the intended model of $\mathsf Z_2$. Other ω-models are the class $\mathrm{REC}$ of computable sets, the class of arithmetic sets, and the class $\{ X : X \leq_T A \}$ for a fixed set $A$. A model whose first-order part is not isomorphic to $\nat$ contains **non-standard** numbers. Such models are needed to separate systems that differ only by their induction axioms, since every ω-model satisfies full induction (:ref{#prop-omega-absolute}); most separations between the systems of this track are nevertheless obtained with ω-models.

:::proposition{#prop-omega-absolute}
Let $\mathcal S \subseteq \mathcal P(\nat)$ be an ω-model.

1. For every arithmetic formula $\varphi(X_1, \dots, X_k, n_1, \dots, n_l)$ and all $A_1, \dots, A_k \in \mathcal S$ and $n_1, \dots, n_l \in \nat$, $\mathcal S \models \varphi(A, n)$ if and only if $\varphi(A, n)$ holds in the full structure $\mathcal P(\nat)$.
2. $\mathcal S$ satisfies the basic axioms and the induction scheme for all formulas of $\mathcal L_2$.
:::

:::proof{of=prop-omega-absolute}
1. By induction on $\varphi$: atomic formulas are evaluated in $\nat$ with the same parameters; the connectives commute with satisfaction; number quantifiers range over $\nat$ in both structures. Set quantifiers do not occur.
2. The basic axioms hold in $\nat$. For induction, let $\varphi(n)$ be any formula with parameters in $\mathcal S$, true at $0$ and preserved by successor in $\mathcal S$. The set $\{ n \in \nat : \mathcal S \models \varphi(n) \}$ contains $0$ and is closed under successor, so it is $\nat$, by induction in the metatheory.
:::

Item 1, **absoluteness**, is the reason why computability theory is the natural tool for ω-models: an arithmetic statement about sets of the model means the same thing inside the model and in reality. It is used in nearly every argument about ω-models in this track. A $\Sigma^1_1$ statement, on the other hand, may be true in $\mathcal P(\nat)$ and false in $\mathcal S$, if its witnesses are missing from $\mathcal S$. Item 2 applies induction in the metatheory to a set that need not belong to $\mathcal S$; non-standard models, where this fails, are the subject of :ref{to="nonstandard-models"}.

:::quiz[ω-models]
Why does every ω-model satisfy the full induction scheme, while not every model of the basic axioms does?

- [x] Because the first-order part of an ω-model is the true $\nat$, where every set of numbers containing $0$ and closed under successor is $\nat$, whether or not it belongs to the model.
- [ ] Because ω-models satisfy full comprehension.

  An ω-model may contain only the computable sets; induction holds for reasons external to the model.
- [ ] Because induction is an arithmetic statement.

  Induction for formulas with set quantifiers is not arithmetic; it holds in ω-models by the argument in the metatheory.

---

Let $\mathcal S$ be an ω-model containing a set $A$. Why does $\mathcal S$ satisfy "the set $A$ is infinite" exactly when $A$ is infinite?

- [x] Because "$\forall m\, \exists n > m\ n \in A$" is arithmetic, and arithmetic formulas are absolute for ω-models.
- [ ] Because $\mathcal S$ contains all finite sets.

  An ω-model need not contain all finite sets, and none is involved: the statement quantifies over numbers only, and its truth in $\mathcal S$ is that of an arithmetic formula with parameter $A$.
- [ ] Because infinite sets are not definable in $\mathcal L_2$.

  Infiniteness is definable by an arithmetic formula.
:::

::::exercise{#ex-pi11-absolute difficulty=2 objective="Transfer $\Pi^1_1$ sentences from the full structure down to ω-models and $\Sigma^1_1$ sentences up, and see that $\Sigma^1_1$ sentences need not go down."}
Show that a $\Pi^1_1$ sentence true in $\mathcal P(\nat)$ is true in every ω-model, and that a $\Sigma^1_1$ sentence true in some ω-model is true in $\mathcal P(\nat)$. Give a $\Sigma^1_1$ sentence that is true in $\mathcal P(\nat)$ and false in the ω-model $\mathcal S$ of the computable sets.

:::solution
Let $\forall X\, \varphi(X)$ be true in $\mathcal P(\nat)$, with $\varphi$ arithmetic, and let $\mathcal S$ be an ω-model. For every $A \in \mathcal S$, $\varphi(A)$ is true, so $\mathcal S \models \varphi(A)$ by :ref{#prop-omega-absolute}; hence $\mathcal S \models \forall X\, \varphi(X)$. If $\mathcal S \models \exists X\, \varphi(X)$, a witness $A \in \mathcal S$ satisfies $\varphi(A)$ in reality, so the sentence is true in $\mathcal P(\nat)$.

The sentence "there is a set $X$ such that, for every $e$, if $\Phi_e$ is total with values in $\{0, 1\}$ then $X(n) \neq \Phi_e(n)$ for some $n$" is $\Sigma^1_1$: the relation $\Phi_e(n)\converge = m$ is $\Sigma^0_1$, so the matrix is arithmetic. It is true in $\mathcal P(\nat)$, since non-computable sets exist, and false in $\mathcal S$, since every member of $\mathcal S$ is equal to some total $\Phi_e$.
:::
::::

## The program

A subsystem $T$ of $\mathsf Z_2$ **proves** a statement $\varphi$ if $\varphi$ is derivable from the axioms of $T$. Two statements $\varphi$ and $\psi$ are **equivalent over** $T$ if $T$ proves $\varphi \leftrightarrow \psi$. The typical result of reverse mathematics has the form: a theorem $\varphi$ of ordinary mathematics, suitably coded, is provable in a system $S$, and conversely $\varphi$ implies the axioms of $S$ over the base theory $\mathsf{RCA}_0$. Since $\varphi$ implies the axioms of $S$ over $\mathsf{RCA}_0$, these axioms are necessary to prove $\varphi$ over $\mathsf{RCA}_0$. The axioms are proved from the theorem: hence the name *reverse* mathematics. For instance, the monotone convergence theorem for sequences of reals is provable with arithmetic comprehension and implies it over $\mathsf{RCA}_0$ (:ref{#thm-monotone-aca}, in the course on the Big Five); the lesson on real numbers in this course shows that it is not provable in $\mathsf{RCA}_0$ (:ref{to="real-numbers"}).

The five systems of the Big Five are, in increasing strength:

| System | Main axiom | Computability counterpart |
| --- | --- | --- |
| $\mathsf{RCA}_0$ | $\Delta^0_1$ comprehension | computable sets |
| $\mathsf{WKL}_0$ | weak König's lemma | PA degrees |
| $\mathsf{ACA}_0$ | arithmetic comprehension | the Turing jump |
| $\mathsf{ATR}_0$ | arithmetic transfinite recursion | hyperarithmetic sets |
| $\Pi^1_1\text{-}\mathsf{CA}_0$ | $\Pi^1_1$ comprehension | the hyperjump |

The next lessons introduce $\mathsf{RCA}_0$ and its models; the others are the subject of the course on the Big Five. Ramsey's theorem for pairs, studied in the course on Ramsey's theorem, is the main exception to the Big Five phenomenon.

## Notes and references

Second-order arithmetic was introduced by Hilbert and Bernays in the *Grundlagen der Mathematik* (1934–1939), whose Supplement IV outlines the development of analysis in it (Simpson, notes to Section I.2). Friedman (1975) initiated reverse mathematics, and Simpson's monograph is its standard reference; Hirschfeldt's and Dzhafarov–Mummert's books emphasize the computability-theoretic side. The axioms of :ref{#def-z2} are those of Simpson, Definition I.2.4; Dzhafarov–Mummert (Section 5.3) use instead the axioms of a discrete ordered semiring. :ref{#prop-omega-absolute} is a special case of their Exercise 5.13.1, and the view of theorems as problems is the subject of their Chapter 3.

- H. Friedman, *Some systems of second order arithmetic and their use*, Proceedings of the International Congress of Mathematicians, Vancouver, 1974, vol. 1, 235–242.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section I.2.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Chapter 4.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.1–5.3.

:::::exercises
::::exercise{#ex-z2-arith-models difficulty=1 objective="Check the comprehension scheme in two ω-models, using absoluteness."}
Show that $\mathcal P(\nat)$ is a model of $\mathsf Z_2$, and that the class of arithmetic sets is an ω-model of arithmetic comprehension, that is, of the comprehension scheme for arithmetic formulas.

:::solution
In $\mathcal P(\nat)$, every formula with parameters defines a subset of $\nat$, which belongs to $\mathcal P(\nat)$; the other axioms hold by :ref{#prop-omega-absolute}. Let $\mathcal A$ be the class of arithmetic sets, and $\varphi(n)$ an arithmetic formula with parameters $A_1, \dots, A_k \in \mathcal A$. By :ref{#prop-omega-absolute}, $\mathcal A \models \varphi(n)$ if and only if $\varphi(n)$ is true. Each $A_i$ is $\Sigma^0_{m}$ for some $m$, so substituting arithmetic definitions of the $A_i$ in $\varphi$ shows that $\{ n : \varphi(n) \}$ is arithmetic, hence belongs to $\mathcal A$.
:::
::::

::::exercise{#ex-classify-l2 difficulty=1 objective="Put formulas of $\mathcal L_2$ in prenex form and read off their class in the arithmetic and analytic hierarchies."}
Write each of the following formulas, with set parameters $X$ and $Y$, in prenex form, and give a class $\Sigma^0_n$, $\Pi^0_n$, $\Sigma^1_n$ or $\Pi^1_n$, with $n$ as small as the prenex form shows, to which it belongs. Use that the relation $\Phi^X_e(n)\converge = m$ is expressed by a $\Sigma^0_1$ formula $\exists s\, \theta(X, e, n, m, s)$ with $\theta$ bounded (relativization of :ref{#cor-sigma1-ce}).

1. $X \subseteq Y$.
2. $X$ is finite.
3. $Y = X'$, that is, $Y = \{ e : \Phi^X_e(e)\converge \}$.
4. There is a set that is not computable from $X$.
5. Every set has a Turing jump: $\forall Y\, \exists Z\ Z = Y'$.

:::solution
1. $\forall n\, (n \notin X \vee n \in Y)$, a $\Pi^0_1$ formula.
2. $\exists m\, \forall n\, (n \in X \rightarrow n < m)$, a $\Sigma^0_2$ formula.
3. Let $\exists s\, \theta(e, s)$ express $\Phi^X_e(e)\converge$, with $\theta$ bounded. The formula $\forall e\, (e \in Y \leftrightarrow \exists s\, \theta(e, s))$ is the conjunction, under $\forall e$, of $e \notin Y \vee \exists s\, \theta(e, s)$ and $\forall t\, \neg \theta(e, t) \vee e \in Y$. Since $s$ and $t$ do not occur in the other disjuncts, the quantifiers can be pulled out:
$$
\forall e\, \exists s\, \forall t\, \big( (e \notin Y \vee \theta(e, s)) \wedge (\neg \theta(e, t) \vee e \in Y) \big),
$$
a $\Pi^0_2$ formula.
4. "$\Phi^X_e = Y$" is $\forall n\, \big( (n \in Y \wedge \Phi^X_e(n)\converge = 1) \vee (n \notin Y \wedge \Phi^X_e(n)\converge = 0) \big)$, a $\Pi^0_2$ formula after pulling out the existential quantifiers of the two $\Sigma^0_1$ formulas. The sentence is $\exists Y\, \forall e\, \neg\, \Phi^X_e = Y$; its matrix is arithmetic ($\Pi^0_3$ in prenex form), so it is $\Sigma^1_1$.
5. $\forall Y\, \exists Z\, \chi(Y, Z)$ with $\chi$ the $\Pi^0_2$ formula of item 3, with $Y, Z$ in place of $X, Y$: a $\Pi^1_2$ sentence.
:::
::::

::::exercise{#ex-pairing-injective difficulty=1 objective="Verify the properties of the pairing function that allow quantifiers over the components of a pair to be bounded."}
Let $\langle m, n \rangle = (m + n)^2 + m$. Show that the map $(m, n) \mapsto \langle m, n \rangle$ is injective on $\nat^2$, that $m, n \leq \langle m, n \rangle$, and that $3$ is not of the form $\langle m, n \rangle$. Deduce that "$k$ is a pair" is expressed by a bounded formula.

:::solution
Let $s = m + n$ and $k = \langle m, n \rangle$. Then $s^2 \leq k = s^2 + m \leq s^2 + s < (s + 1)^2$, so $s$ is the unique number with $s^2 \leq k < (s + 1)^2$; it is determined by $k$, and so are $m = k - s^2$ and $n = s - m$. This proves injectivity. Clearly $m \leq k$, and $n \leq s \leq s^2 \leq k$, since $s \leq s^2$ for every $s \in \nat$. For $k = 3$, the only $s$ with $s^2 \leq 3 < (s+1)^2$ is $s = 1$, and $m = 3 - 1 = 2 > s$, so $3$ is not a pair. By the bound just proved, "$k$ is a pair" is expressed by the bounded formula $\exists m < k + 1\ \exists n < k + 1\ k = (m + n) \cdot (m + n) + m$.

The injectivity of this pairing function is Simpson, Theorem II.2.2, where it is proved in $\mathsf{RCA}_0$.
:::
::::

::::exercise{#ex-split-formalization difficulty=1 objective="Formalize a theorem as a problem with instances and solutions, and check it in ω-models of the form $\{ X : X \leq_T A \}$."}
Write the statement "every infinite set $X$ has an infinite subset $Y$ such that $X \setminus Y$ is infinite" in the form $\forall X\, (\varphi(X) \rightarrow \exists Y\, \psi(X, Y))$ with $\varphi, \psi$ arithmetic, and classify $\varphi$ and $\psi$. Show that it holds in the ω-model $\{ Z : Z \leq_T A \}$ for every set $A$.

:::solution
Take $\varphi(X) \equiv \forall m\, \exists n\, (n > m \wedge n \in X)$, a $\Pi^0_2$ formula, and
$$
\psi(X, Y) \equiv \forall n\, (n \in Y \rightarrow n \in X) \wedge \forall m\, \exists n\, (n > m \wedge n \in Y) \wedge \forall m\, \exists n\, (n > m \wedge n \in X \wedge n \notin Y),
$$
a conjunction of a $\Pi^0_1$ and two $\Pi^0_2$ formulas, hence $\Pi^0_2$ after pulling out the quantifiers.

Let $\mathcal S = \{ Z : Z \leq_T A \}$ and $X \in \mathcal S$ with $\mathcal S \models \varphi(X)$. By :ref{#prop-omega-absolute}, $X$ is infinite; list it as $x_0 < x_1 < \cdots$ and let $Y = \{ x_{2i} : i \in \nat \}$. Then $Y \leq_T X$: to decide whether $n \in Y$, check $n \in X$ and count the elements of $X$ below $n$ with the oracle $X$; $n \in Y$ if and only if $n \in X$ and this number is even. So $Y \leq_T A$ and $Y \in \mathcal S$. The set $Y$ is an infinite subset of $X$ and $X \setminus Y = \{ x_{2i+1} : i \in \nat \}$ is infinite, so $\psi(X, Y)$ holds, and $\mathcal S \models \psi(X, Y)$ by absoluteness.
:::
::::

::::exercise{#ex-pi12-omega-models difficulty=1 objective="Reduce the truth of a $\Pi^1_2$ statement in an ω-model to the existence of solutions in the model, and apply it to the computable sets."}
Let $\sigma$ be a sentence $\forall X\, (\varphi(X) \rightarrow \exists Y\, \psi(X, Y))$ with $\varphi, \psi$ arithmetic, and $\mathcal S$ an ω-model. Show that $\mathcal S \models \sigma$ if and only if every $X \in \mathcal S$ such that $\varphi(X)$ is true has some $Y \in \mathcal S$ such that $\psi(X, Y)$ is true. Deduce that the sentence "every function from $\nat$ to $\nat$ has a range" of :ref{#ex-formalization} is false in the ω-model $\mathrm{REC}$ of the computable sets.

:::solution
By definition of satisfaction, $\mathcal S \models \sigma$ if and only if for every $X \in \mathcal S$ with $\mathcal S \models \varphi(X)$ there is $Y \in \mathcal S$ with $\mathcal S \models \psi(X, Y)$. By :ref{#prop-omega-absolute}, $\mathcal S \models \varphi(X)$ if and only if $\varphi(X)$ is true, and likewise for $\psi(X, Y)$, which gives the equivalence.

Let $f$ be a computable injective function whose range is the halting set $\emptyset'$; it exists since $\emptyset'$ is c.e. and infinite. Its graph $X$ is computable, so $X \in \mathrm{REC}$, and $X$ is a function. A set $Y$ with $\forall m\, (m \in Y \leftrightarrow \exists n\, \langle n, m \rangle \in X)$ true is the range $\emptyset'$, which is not computable. So no solution lies in $\mathrm{REC}$, and the sentence is false there.
:::
::::

::::exercise{#ex-induction-not-comprehension difficulty=1 objective="See that the induction scheme does not imply comprehension, by an ω-model."}
:ref{#prop-induction-comprehension} derives induction from comprehension. Show that the converse fails: the basic axioms and the induction scheme for all formulas of $\mathcal L_2$ do not prove the comprehension scheme for arithmetic formulas.

:::solution
The ω-model $\mathrm{REC}$ satisfies the basic axioms and the induction scheme for all formulas, by :ref{#prop-omega-absolute}. It fails the instance $\exists Y\, \forall n\, (n \in Y \leftrightarrow \Phi_n(n)\converge)$ of arithmetic comprehension, where $\Phi_n(n)\converge$ is expressed by a $\Sigma^0_1$ formula: by absoluteness, a set $Y \in \mathrm{REC}$ satisfying the matrix in $\mathrm{REC}$ would be the halting set, which is not computable. By the completeness theorem, a sentence provable from the basic axioms and the induction scheme holds in $\mathrm{REC}$; so this instance is not provable.
:::
::::
:::::
