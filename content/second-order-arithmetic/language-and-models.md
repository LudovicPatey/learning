---
title: The language and models of second-order arithmetic
summary: The two-sorted language of second-order arithmetic, its formula classes, the axioms of Z₂, Henkin structures and ω-models, absoluteness of arithmetic formulas, and the program of reverse mathematics.
duration: 35
prerequisites: [arithmetic-hierarchy/arithmetic-definability]
---

Reverse mathematics asks which set-existence axioms are needed to prove a given theorem of ordinary mathematics. The framework, proposed by Friedman (1975) and developed by Simpson, is **second-order arithmetic**: a theory of natural numbers and sets of natural numbers. Countable objects of analysis, algebra and combinatorics (real numbers, continuous functions on the reals, countable groups, colorings of pairs) can be coded by sets of numbers, so that their theorems become statements of second-order arithmetic. One then works in a weak **base theory** and proves equivalences between theorems and axioms. An empirical observation is that most of the theorems studied so far are either provable in the base theory or equivalent over it to one of four stronger systems; together with the base theory, these form the **Big Five**.

This lesson fixes the language, the axioms and the models. Throughout, the reader is assumed to know the language of first-order arithmetic and the arithmetic hierarchy (:ref{to="arithmetic-hierarchy/arithmetic-definability"}).

## The language

:::definition{#def-l2}
The language $\mathcal L_2$ of second-order arithmetic has two sorts of variables: **number variables** $x, y, z, \dots$, intended to range over $\nat$, and **set variables** $X, Y, Z, \dots$, intended to range over subsets of $\nat$. Its non-logical symbols are the constants $0, 1$, the binary function symbols $+, \cdot$, the binary relation symbols $=, <$ on numbers, and the membership symbol $\in$ between a number and a set.

- **Terms** are built from number variables and constants with $+$ and $\cdot$; there are no set terms other than set variables.
- **Atomic formulas** are $t_1 = t_2$, $t_1 < t_2$ and $t \in X$, for terms $t_1, t_2, t$ and a set variable $X$.
- **Formulas** are built from atomic formulas with the connectives and the quantifiers $\forall x, \exists x$ over numbers and $\forall X, \exists X$ over sets.
:::

Equality between sets is not primitive; $X = Y$ abbreviates $\forall n\, (n \in X \leftrightarrow n \in Y)$.

Formulas are classified by their quantifiers, allowing free variables of both sorts, called **parameters**.

- A formula is **bounded**, or $\Sigma^0_0 = \Pi^0_0 = \Delta^0_0$, if all its quantifiers are number quantifiers of the form $\forall x < t$ or $\exists x < t$, with $t$ a term not containing $x$.
- A formula is $\Sigma^0_{n+1}$ if it has the form $\exists x\, \varphi$ with $\varphi$ a $\Pi^0_n$ formula, and $\Pi^0_{n+1}$ if it has the form $\forall x\, \varphi$ with $\varphi$ a $\Sigma^0_n$ formula; blocks of quantifiers of the same kind count as one.
- A formula is **arithmetic** if it contains no set quantifier. It may contain free set variables.
- A formula is $\Sigma^1_1$ if it has the form $\exists X\, \varphi$ with $\varphi$ arithmetic, and $\Pi^1_1$ if it has the form $\forall X\, \varphi$ with $\varphi$ arithmetic; similarly for $\Sigma^1_n$ and $\Pi^1_n$.

With a set parameter $A$, the $\Sigma^0_1$ formulas define exactly the $A$-c.e. sets: this is the relativization of :ref{#cor-sigma1-ce}, by the same proof. Consequently the $\Sigma^0_n$ formulas with parameter $A$ define the $\Sigma^0_n(A)$ sets of :ref{#def-relativized-hierarchy}.

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

The parameters of $\varphi$ are universally quantified: comprehension asserts that, for all values of the other free variables, the set defined by $\varphi$ exists. Comprehension for formulas with set quantifiers is **impredicative**: the set $X$ is defined by quantifying over all sets, including $X$ itself. The subsystems studied in reverse mathematics restrict comprehension, and induction with it.

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

Satisfaction $\mathcal M \models \varphi$ is defined as usual, the set quantifiers ranging over $\mathcal S$ only. Such structures are **Henkin structures**; a structure with $\mathcal S = \mathcal P(M)$ is a **full** structure. With Henkin semantics, the logic of $\mathcal L_2$ is essentially first-order logic with two sorts, and enjoys the completeness theorem: a sentence is provable in a theory $T$ if and only if it holds in every model of $T$. We admit this result: it is the completeness theorem for many-sorted first-order logic, which reduces to the one-sorted case by adding a unary predicate for each sort (see Simpson, *Subsystems of Second Order Arithmetic*, Section I.2, for $\mathcal L_2$-structures). In particular, to show that $T$ does not prove $\varphi$, it suffices to exhibit a model of $T$ in which $\varphi$ fails.

:::definition{#def-omega-model}
An **ω-model** is a structure whose first-order part is $\nat$ with the usual operations and order. It is determined by its second-order part $\mathcal S \subseteq \mathcal P(\nat)$, and we identify the two.
:::

The structure $\mathcal P(\nat)$ is the intended model of $\mathsf Z_2$. A model whose first-order part is not isomorphic to $\nat$ contains **non-standard** numbers. Such models are needed to separate systems that differ only by their induction axioms, since every ω-model satisfies full induction (:ref{#prop-omega-absolute}); most separations between the systems of this track are nevertheless obtained with ω-models.

:::proposition{#prop-omega-absolute}
Let $\mathcal S \subseteq \mathcal P(\nat)$ be an ω-model.

1. For every arithmetic formula $\varphi(X_1, \dots, X_k, n_1, \dots, n_l)$ and all $A_1, \dots, A_k \in \mathcal S$ and $n_1, \dots, n_l \in \nat$, $\mathcal S \models \varphi(A, n)$ if and only if $\varphi(A, n)$ holds in the full structure $\mathcal P(\nat)$.
2. $\mathcal S$ satisfies the basic axioms and the induction scheme for all formulas of $\mathcal L_2$.
:::

:::proof{of=prop-omega-absolute}
1. By induction on $\varphi$: atomic formulas are evaluated in $\nat$ with the same parameters; the connectives commute with satisfaction; number quantifiers range over $\nat$ in both structures. Set quantifiers do not occur.
2. The basic axioms hold in $\nat$. For induction, let $\varphi(n)$ be any formula with parameters in $\mathcal S$, true at $0$ and preserved by successor in $\mathcal S$. The set $\{ n \in \nat : \mathcal S \models \varphi(n) \}$ contains $0$ and is closed under successor, so it is $\nat$, by induction in the metatheory.
:::

Item 1 is the reason why computability theory is the natural tool for ω-models: an arithmetic statement about sets of the model means the same thing inside the model and in reality. A $\Sigma^1_1$ statement, on the other hand, may be true in $\mathcal P(\nat)$ and false in $\mathcal S$, if its witnesses are missing from $\mathcal S$.

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

## The program

A subsystem $T$ of $\mathsf Z_2$ **proves** a statement $\varphi$ if $\varphi$ is derivable from the axioms of $T$. Two statements $\varphi$ and $\psi$ are **equivalent over** $T$ if $T$ proves $\varphi \leftrightarrow \psi$. The typical result of reverse mathematics has the form: a theorem $\varphi$ of ordinary mathematics, suitably coded, is provable in a system $S$, and conversely $\varphi$ implies the axioms of $S$ over the base theory $\mathsf{RCA}_0$. Since $\varphi$ implies the axioms of $S$ over $\mathsf{RCA}_0$, these axioms are necessary to prove $\varphi$ over $\mathsf{RCA}_0$. The axioms are proved from the theorem: hence the name *reverse* mathematics.

The five systems of the Big Five are, in increasing strength:

| System | Main axiom | Computability counterpart |
| --- | --- | --- |
| $\mathsf{RCA}_0$ | $\Delta^0_1$ comprehension | computable sets |
| $\mathsf{WKL}_0$ | weak König's lemma | PA degrees |
| $\mathsf{ACA}_0$ | arithmetic comprehension | the Turing jump |
| $\mathsf{ATR}_0$ | arithmetic transfinite recursion | hyperarithmetic sets |
| $\Pi^1_1\text{-}\mathsf{CA}_0$ | $\Pi^1_1$ comprehension | the hyperjump |

The next lesson introduces $\mathsf{RCA}_0$; the others are the subject of the course on the Big Five. Ramsey's theorem for pairs, studied in the last course of the track, is the main exception to the Big Five phenomenon.

## Exercises

::::exercise{difficulty=1}
Show that $\mathcal P(\nat)$ is a model of $\mathsf Z_2$, and that the class of arithmetic sets is an ω-model of arithmetic comprehension, that is, of the comprehension scheme for arithmetic formulas.

:::solution
In $\mathcal P(\nat)$, every formula with parameters defines a subset of $\nat$, which belongs to $\mathcal P(\nat)$; the other axioms hold by :ref{#prop-omega-absolute}. Let $\mathcal A$ be the class of arithmetic sets, and $\varphi(n)$ an arithmetic formula with parameters $A_1, \dots, A_k \in \mathcal A$. By :ref{#prop-omega-absolute}, $\mathcal A \models \varphi(n)$ if and only if $\varphi(n)$ is true. Each $A_i$ is $\Sigma^0_{m}$ for some $m$, so substituting arithmetic definitions of the $A_i$ in $\varphi$ shows that $\{ n : \varphi(n) \}$ is arithmetic, hence belongs to $\mathcal A$.
:::
::::

::::exercise{difficulty=2}
Show that a $\Pi^1_1$ sentence true in $\mathcal P(\nat)$ is true in every ω-model, and that a $\Sigma^1_1$ sentence true in some ω-model is true in $\mathcal P(\nat)$. Give a $\Sigma^1_1$ sentence that is true in $\mathcal P(\nat)$ and false in the ω-model $\mathcal S$ of the computable sets.

:::solution
Let $\forall X\, \varphi(X)$ be true in $\mathcal P(\nat)$, with $\varphi$ arithmetic, and let $\mathcal S$ be an ω-model. For every $A \in \mathcal S$, $\varphi(A)$ is true, so $\mathcal S \models \varphi(A)$ by :ref{#prop-omega-absolute}; hence $\mathcal S \models \forall X\, \varphi(X)$. If $\mathcal S \models \exists X\, \varphi(X)$, a witness $A \in \mathcal S$ satisfies $\varphi(A)$ in reality, so the sentence is true in $\mathcal P(\nat)$.

The sentence "there is a set $X$ such that, for every $e$, if $\Phi_e$ is total with values in $\{0, 1\}$ then $X(n) \neq \Phi_e(n)$ for some $n$" is $\Sigma^1_1$: the relation $\Phi_e(n)\converge = m$ is $\Sigma^0_1$, so the matrix is arithmetic. It is true in $\mathcal P(\nat)$, since non-computable sets exist, and false in $\mathcal S$, since every member of $\mathcal S$ is equal to some total $\Phi_e$.
:::
::::

## Notes and references

Second-order arithmetic was introduced by Hilbert and Bernays in the *Grundlagen der Mathematik* (1934–1939), who showed that much of analysis can be developed in it. Friedman (1975) initiated reverse mathematics, and Simpson's monograph is its standard reference; Hirschfeldt's and Dzhafarov–Mummert's books emphasize the computability-theoretic side.

- H. Friedman, *Some systems of second order arithmetic and their use*, Proceedings of the International Congress of Mathematicians, Vancouver, 1974, vol. 1, 235–242.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.
