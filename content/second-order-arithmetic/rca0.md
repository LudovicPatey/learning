---
title: The base theory RCA₀
summary: Δ⁰₁ comprehension and Σ⁰₁ induction; consequences of Σ⁰₁ induction; the ω-models of RCA₀ are the Turing ideals; the computable sets form the least ω-model, and non-provability in RCA₀ follows from computability-theoretic constructions.
duration: 35
prerequisites: [language-and-models, pi01-classes/computable-members]
---

The base theory of reverse mathematics should be weak enough to leave the interesting theorems unprovable, and strong enough to carry out the codings of mathematical objects. Friedman's choice is $\mathsf{RCA}_0$, for **recursive comprehension axiom**: it asserts the existence of the sets computable from given sets, and allows induction for properties that can be verified by a search. Its ω-models are exactly the classes of sets closed under relative computability and join.

## The system

:::definition{#def-rca0}
The **$\Delta^0_1$ comprehension scheme** consists of the universal closures of
$$
\forall n\, (\varphi(n) \leftrightarrow \psi(n)) \rightarrow \exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n)),
$$
for $\varphi$ a $\Sigma^0_1$ formula and $\psi$ a $\Pi^0_1$ formula in which $X$ does not occur free. The system $\mathsf{RCA}_0$ consists of the basic axioms, the $\Sigma^0_1$ induction scheme, and the $\Delta^0_1$ comprehension scheme.
:::

Being $\Delta^0_1$ is not a syntactic property, so the scheme asks for a $\Sigma^0_1$ and a $\Pi^0_1$ definition and assumes their equivalence. The subscript $0$ records the restriction of induction to $\Sigma^0_1$ formulas. The induction axiom is the instance of $\Sigma^0_1$ induction for the bounded formula $n \in X$, so $\mathsf{RCA}_0$ proves it.

Induction for $\Sigma^0_1$ formulas extends to their negations.

:::proposition{#prop-pi01-induction}
$\mathsf{RCA}_0$ proves the $\Pi^0_1$ induction scheme.
:::

:::proof{of=prop-pi01-induction}
Let $\psi$ be $\Pi^0_1$ with $\psi(0)$ and $\forall n\, (\psi(n) \rightarrow \psi(n+1))$, and suppose $\neg \psi(a)$ for some $a$. Let $\varphi(m)$ be the formula $m \leq a \rightarrow \neg \psi(a - m)$, where $a - m$ is the subtraction, defined for $m \leq a$; $\varphi$ is equivalent to a $\Sigma^0_1$ formula. Then $\varphi(0)$ holds. If $\varphi(m)$ and $m + 1 \leq a$, then $\neg \psi(a - m)$, and $\neg \psi(a - m - 1)$ follows from the hypothesis applied to $n = a - m - 1$. So $\varphi(m+1)$. By $\Sigma^0_1$ induction, $\varphi(a)$ holds, that is, $\neg \psi(0)$, a contradiction.
:::

The development of arithmetic in $\mathsf{RCA}_0$ follows the usual lines: one defines pairing, finite sequences and finite sets coded by numbers, and shows that every primitive recursive function has a $\Sigma^0_1$ definition that $\mathsf{RCA}_0$ proves to be total. In particular, the relation $\Phi^X_e(n)[s]\converge = m$ of :ref{#def-finite-oracle} is expressed by a bounded formula, and "$\Phi^X_e(n)\converge = m$" by a $\Sigma^0_1$ formula. We admit this development, which is routine but long; see Simpson, *Subsystems of Second Order Arithmetic*, Section II.3. One of its consequences is **bounded $\Sigma^0_1$ comprehension**: for every $\Sigma^0_1$ formula $\varphi$ and every $n$, there is a finite set equal to $\{ i < n : \varphi(i) \}$. Its proof uses $\Sigma^0_1$ induction in an essential way.

## ω-models and Turing ideals

:::definition{#def-turing-ideal}
A **Turing ideal** is a non-empty class $\mathcal I \subseteq \mathcal P(\nat)$ such that $X \oplus Y \in \mathcal I$ for all $X, Y \in \mathcal I$, and $Y \in \mathcal I$ whenever $Y \leq_T X \in \mathcal I$.
:::

:::theorem[Friedman]{#thm-rca-turing-ideal}
An ω-model $\mathcal S$ satisfies $\mathsf{RCA}_0$ if and only if $\mathcal S$ is a Turing ideal.
:::

:::proof{of=thm-rca-turing-ideal}
By :ref{#prop-omega-absolute}, every ω-model satisfies the basic axioms and the full induction scheme, so only $\Delta^0_1$ comprehension matters.

($\Rightarrow$) Let $X, Y \in \mathcal S$. The set $X \oplus Y$ is defined by a bounded formula with parameters $X, Y$, which is both $\Sigma^0_1$ and $\Pi^0_1$; by comprehension in $\mathcal S$ it belongs to $\mathcal S$. Let $Y \leq_T X \in \mathcal S$. Then $Y$ and its complement are $X$-c.e., so there are a $\Sigma^0_1$ formula $\varphi$ and a $\Pi^0_1$ formula $\psi$ with parameter $X$ that both define $Y$ in $\nat$. By absoluteness, $\mathcal S \models \forall n\, (\varphi(n) \leftrightarrow \psi(n))$, so comprehension gives a set $Z \in \mathcal S$ with $\mathcal S \models \forall n\, (n \in Z \leftrightarrow \varphi(n))$, and $Z = Y$ by absoluteness again.

($\Leftarrow$) Let $\varphi$ be $\Sigma^0_1$ and $\psi$ be $\Pi^0_1$, with set parameters $A_1, \dots, A_k \in \mathcal S$ and number parameters, such that $\mathcal S \models \forall n\, (\varphi(n) \leftrightarrow \psi(n))$. By absoluteness, $\varphi$ and $\psi$ define the same set $Y$ in $\nat$; it is c.e. and co-c.e. relative to $A = A_1 \oplus \cdots \oplus A_k \in \mathcal S$, hence $Y \leq_T A$ and $Y \in \mathcal S$. By absoluteness, $Y$ witnesses the instance of comprehension in $\mathcal S$.
:::

The class $\mathrm{REC}$ of computable sets is a Turing ideal, and it is contained in every Turing ideal, since a Turing ideal contains some set, which computes every computable set. So $\mathrm{REC}$ is the **least ω-model** of $\mathsf{RCA}_0$. Combined with the completeness theorem, this gives a method for unprovability: if a statement fails in $\mathrm{REC}$, it is not provable in $\mathsf{RCA}_0$.

:::corollary{#cor-rca-not-wkl}
$\mathsf{RCA}_0$ proves neither "every set has a Turing jump" nor "every infinite binary tree has an infinite path".
:::

:::proof{of=cor-rca-not-wkl}
Both statements fail in $\mathrm{REC}$. The jump of $\emptyset$ is not computable, so "there is $Y$ with $Y = \{ e : \Phi_e(e)\converge \}$", an instance of the first statement with an arithmetic matrix, is false in $\mathrm{REC}$ by absoluteness. There is an infinite computable binary tree without computable paths, whose paths are the members of $\mathrm{DNC}_2$ (:ref{#thm-dnc2-no-computable}); in $\mathrm{REC}$ this tree is infinite, by absoluteness, and has no path.
:::

:::quiz[Turing ideals]
In the proof of :ref{#thm-rca-turing-ideal} ($\Leftarrow$), where is it used that $\mathcal S$ is an ω-model?

- [x] To transfer the equivalence of $\varphi$ and $\psi$ from $\mathcal S$ to $\nat$, so that they define a set that is c.e. and co-c.e. relative to the parameters.
- [ ] To ensure that $\mathcal S$ is closed under join.

  Closure under join is the hypothesis that $\mathcal S$ is a Turing ideal.
- [ ] To ensure that $\varphi$ is $\Sigma^0_1$.

  The syntactic form of $\varphi$ does not depend on the model.

---

Why does an unprovability result obtained with $\mathrm{REC}$ hold for $\mathsf{RCA}_0$ and not only for its ω-models?

- [x] By the completeness theorem: a sentence provable in $\mathsf{RCA}_0$ holds in every model, in particular in the ω-model $\mathrm{REC}$.
- [ ] Because every model of $\mathsf{RCA}_0$ is an ω-model.

  There are many non-standard models; one model where the sentence fails suffices.
- [ ] Because $\mathrm{REC}$ is the least ω-model.

  Minimality is not needed: any model of $\mathsf{RCA}_0$ in which the sentence fails gives unprovability.
:::

## The role of induction

In ω-models, induction is free. In general models, the restriction to $\Sigma^0_1$ induction has real consequences: there are models of $\mathsf{RCA}_0$ in which $\Sigma^0_2$ induction fails, and statements of combinatorics, such as the infinite pigeonhole principle for arbitrarily many colors, are equivalent over $\mathsf{RCA}_0$ to forms of induction or bounding. These phenomena require non-standard models, and are studied in Hájek and Pudlák's monograph. The first-order part of $\mathsf{RCA}_0$ is exactly the arithmetic theory $\mathrm{I}\Sigma_1$: every arithmetic sentence provable in $\mathsf{RCA}_0$ is provable from the basic axioms and $\Sigma_1$ induction (Friedman); we admit this conservation result.

## Exercises

::::exercise{difficulty=1}
Show that the union of an increasing sequence of Turing ideals is a Turing ideal, and deduce that for every sequence $Z_0 \leq_T Z_1 \leq_T \cdots$, the class $\{ X : \exists n\ X \leq_T Z_n \}$ is an ω-model of $\mathsf{RCA}_0$.

:::solution
Let $\mathcal I = \bigcup_n \mathcal I_n$. If $X, Y \in \mathcal I$, both belong to some $\mathcal I_n$, since the sequence increases, so $X \oplus Y \in \mathcal I_n \subseteq \mathcal I$. If $Y \leq_T X \in \mathcal I_n$, then $Y \in \mathcal I_n$. The classes $\{ X : X \leq_T Z_n \}$ are Turing ideals, increasing with $n$, so their union is a Turing ideal, and an ω-model of $\mathsf{RCA}_0$ by :ref{#thm-rca-turing-ideal}.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{RCA}_0$ proves the **$\Pi^0_1$ least number principle**: if $\psi$ is $\Pi^0_1$ and $\psi(a)$ holds for some $a$, then there is a least $n$ with $\psi(n)$.

:::solution
Suppose that $\psi(a)$ holds and there is no least $n$ with $\psi(n)$. Let $\varphi(m)$ be $\forall k \leq m\ \neg \psi(k)$; it is equivalent to a $\Pi^0_1$ formula, since a bounded universal quantifier in front of a universal formula can be merged with it: $\forall k \leq m\, \forall x\, \theta \leftrightarrow \forall x\, \forall k \leq m\, \theta$. If $\psi(0)$ held, $0$ would be the least $n$ with $\psi(n)$; so $\varphi(0)$. If $\varphi(m)$ and $\psi(m+1)$, then $m+1$ would be least; so $\varphi(m)$ implies $\varphi(m+1)$. By :ref{#prop-pi01-induction}, $\varphi(a)$ holds, contradicting $\psi(a)$.
:::
::::

## Notes and references

Friedman introduced $\mathsf{RCA}$ with full induction, and the restricted system $\mathsf{RCA}_0$ appears in Friedman (1976) and in Simpson's work. The conservation of $\mathsf{RCA}_0$ over $\mathrm I\Sigma_1$ is due to Friedman; a proof is in Simpson, Section IX.1.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Chapters II and IX.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993.
