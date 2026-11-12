---
title: The base theory RCA₀
summary: Δ⁰₁ comprehension and Σ⁰₁ induction; consequences of Σ⁰₁ induction; the ω-models of RCA₀ are the Turing ideals; the computable sets form the least ω-model, and non-provability in RCA₀ follows from computability-theoretic constructions.
duration: 40
prerequisites: [language-and-models, pi01-classes/computable-members]
---

The base theory of reverse mathematics should be weak enough to leave the interesting theorems unprovable, and strong enough to carry out the codings of mathematical objects. Friedman's choice is $\mathsf{RCA}_0$, for **recursive comprehension axiom**: it asserts the existence of the sets computable from given sets, and allows induction for properties that can be verified by a search. Its ω-models are exactly the classes of sets closed under relative computability and join, the **Turing ideals**.

The resulting picture is the method of the whole track. To show that a theorem is provable in $\mathsf{RCA}_0$, one gives a proof whose constructions are computable relative to the data; to show that it is not, one finds a Turing ideal, usually the computable sets, in which some instance of the theorem has no solution.

## The system

:::definition{#def-rca0}
The **$\Delta^0_1$ comprehension scheme** consists of the universal closures of
$$
\forall n\, (\varphi(n) \leftrightarrow \psi(n)) \rightarrow \exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n)),
$$
for $\varphi$ a $\Sigma^0_1$ formula and $\psi$ a $\Pi^0_1$ formula in which $X$ does not occur free. The system $\mathsf{RCA}_0$ consists of the basic axioms, the $\Sigma^0_1$ induction scheme, and the $\Delta^0_1$ comprehension scheme.
:::

Being $\Delta^0_1$ is not a syntactic property, so the scheme asks for a $\Sigma^0_1$ and a $\Pi^0_1$ definition and assumes their equivalence. The subscript $0$ records the restriction of induction to $\Sigma^0_1$ formulas. The induction axiom is the instance of $\Sigma^0_1$ induction for the bounded formula $n \in X$, so $\mathsf{RCA}_0$ proves it.

The choice of $\Sigma^0_1$ induction is a compromise. Comprehension for computable sets, with the induction axiom, directly gives induction for $\Delta^0_1$ properties only (:ref{#prop-induction-comprehension}), and this does not suffice to justify definitions by recursion: Hirschfeldt and Shore showed that, over a weaker base, $\Sigma^0_1$ induction is equivalent to the existence of finite sequences defined by iterating a function given by a bounded formula. Induction for more complex formulas, on the other hand, is not needed for most of ordinary mathematics, and without it the first-order consequences of $\mathsf{RCA}_0$ are exactly those of $\Sigma^0_1$ induction (:ref{to="nonstandard-models"}).

:::example{#ex-rca-range}
$\mathsf{RCA}_0$ proves that a strictly increasing function $f : \nat \to \nat$ has a range. The range is defined by the $\Sigma^0_1$ formula $\exists i\, f(i) = n$. It is also defined by the bounded formula $\exists i \leq n\, f(i) = n$, since $f(i) \geq i$ for every $i$; this inequality is proved by $\Sigma^0_1$ induction on $i$ for the formula $\exists m\, (\langle i, m \rangle \in f \wedge m \geq i)$: $f(0) \geq 0$, and $f(i + 1) > f(i) \geq i$. A bounded formula is both $\Sigma^0_1$ and $\Pi^0_1$, so $\Delta^0_1$ comprehension applies. For an injective function that is not increasing, no bound on $i$ is available, and the range need not exist: this is the subject of :ref{to="big-five/aca0"}.
:::

Induction for $\Sigma^0_1$ formulas extends to their negations.

:::proposition{#prop-pi01-induction}
$\mathsf{RCA}_0$ proves the $\Pi^0_1$ induction scheme.
:::

:::proof{of=prop-pi01-induction}
Let $\psi$ be $\Pi^0_1$ with $\psi(0)$ and $\forall n\, (\psi(n) \rightarrow \psi(n+1))$, and suppose $\neg \psi(a)$ for some $a$. Let $\varphi(m)$ be the formula $m \leq a \rightarrow \neg \psi(a - m)$, where $a - m$ is the subtraction, defined for $m \leq a$; $\varphi$ is equivalent to a $\Sigma^0_1$ formula. Then $\varphi(0)$ holds. If $\varphi(m)$ and $m + 1 \leq a$, then $\neg \psi(a - m)$, and $\neg \psi(a - m - 1)$ follows from the hypothesis applied to $n = a - m - 1$. So $\varphi(m+1)$. By $\Sigma^0_1$ induction, $\varphi(a)$ holds, that is, $\neg \psi(0)$, a contradiction.
:::

The development of arithmetic in $\mathsf{RCA}_0$ follows the usual lines: one defines pairing, finite sequences and finite sets coded by numbers, and shows that every primitive recursive function has a $\Sigma^0_1$ definition that $\mathsf{RCA}_0$ proves to be total. In particular, the relation $\Phi^X_e(n)[s]\converge = m$ of :ref{#def-finite-oracle} is expressed by a $\Sigma^0_1$ formula that $\mathsf{RCA}_0$ proves equivalent to a $\Pi^0_1$ formula, and "$\Phi^X_e(n)\converge = m$" by a $\Sigma^0_1$ formula. We admit this development, which is routine but long; see Simpson, *Subsystems of Second Order Arithmetic*, Section II.3. One of its consequences is **bounded $\Sigma^0_1$ comprehension**: for every $\Sigma^0_1$ formula $\varphi$ and every $n$, there is a finite set equal to $\{ i < n : \varphi(i) \}$. Its proof uses $\Sigma^0_1$ induction in an essential way.

## ω-models and Turing ideals

:::definition{#def-turing-ideal}
A **Turing ideal** is a non-empty class $\mathcal I \subseteq \mathcal P(\nat)$ such that $X \oplus Y \in \mathcal I$ for all $X, Y \in \mathcal I$, and $Y \in \mathcal I$ whenever $Y \leq_T X \in \mathcal I$.
:::

:::example{#ex-turing-ideals}
For every set $A$, the class $\{ X : X \leq_T A \}$ is a Turing ideal, since $X, Y \leq_T A$ implies $X \oplus Y \leq_T A$; for $A$ computable, it is the class $\mathrm{REC}$ of computable sets. The classes of $\Delta^0_2$ sets and of arithmetic sets are Turing ideals. Both closure conditions are needed.

- The class of c.e. sets is closed under join but not downward: the complement of $\emptyset'$ is computable from $\emptyset'$ and is not c.e.
- If $A$ and $B$ are Turing incomparable, the class $\{ X : X \leq_T A \text{ or } X \leq_T B \}$ is closed downward but not under join: $A \oplus B \leq_T A$ would give $B \leq_T A$.
:::

:::theorem[Friedman]{#thm-rca-turing-ideal}
An ω-model $\mathcal S$ satisfies $\mathsf{RCA}_0$ if and only if $\mathcal S$ is a Turing ideal.
:::

:::proof{of=thm-rca-turing-ideal}
By :ref{#prop-omega-absolute}, every ω-model satisfies the basic axioms and the full induction scheme, so only $\Delta^0_1$ comprehension matters.

We use twice that the $\Sigma^0_1$ formulas with set parameters $A_1, \dots, A_k$ define exactly the sets c.e. relative to $A_1 \oplus \cdots \oplus A_k$ (relativization of :ref{#cor-sigma1-ce}), and that the $\Pi^0_1$ formulas define their complements.

($\Rightarrow$) The class $\mathcal S$ is non-empty: comprehension for the bounded formula $n \neq n$, used as both $\varphi$ and $\psi$, gives $\emptyset \in \mathcal S$. Let $X, Y \in \mathcal S$. The set $X \oplus Y$ is defined by a bounded formula with parameters $X, Y$, which is both $\Sigma^0_1$ and $\Pi^0_1$; by comprehension in $\mathcal S$ it belongs to $\mathcal S$. Let $Y \leq_T X \in \mathcal S$. Then $Y$ and its complement are $X$-c.e., so there are a $\Sigma^0_1$ formula $\varphi$ and a $\Pi^0_1$ formula $\psi$ with parameter $X$ that both define $Y$ in $\nat$. By absoluteness, $\mathcal S \models \forall n\, (\varphi(n) \leftrightarrow \psi(n))$, so comprehension gives a set $Z \in \mathcal S$ with $\mathcal S \models \forall n\, (n \in Z \leftrightarrow \varphi(n))$, and $Z = Y$ by absoluteness again.

($\Leftarrow$) Let $\varphi$ be $\Sigma^0_1$ and $\psi$ be $\Pi^0_1$, with set parameters $A_1, \dots, A_k \in \mathcal S$ and number parameters, such that $\mathcal S \models \forall n\, (\varphi(n) \leftrightarrow \psi(n))$. By absoluteness, $\varphi$ and $\psi$ define the same set $Y$ in $\nat$; it is c.e. and co-c.e. relative to $A = A_1 \oplus \cdots \oplus A_k \in \mathcal S$, hence $Y \leq_T A$ and $Y \in \mathcal S$ (if $k = 0$, $Y$ is computable and computable from any member of $\mathcal S$). By absoluteness, $Y$ witnesses the instance of comprehension in $\mathcal S$.
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

  Absoluteness is used again at the end, to see that $Y$ satisfies $\forall n\, (n \in Y \leftrightarrow \varphi(n))$ in $\mathcal S$.
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

In ω-models, induction is free, and all the arguments of this section concern only comprehension. In general models, the restriction to $\Sigma^0_1$ induction has real consequences: some models of $\mathsf{RCA}_0$ fail $\Sigma^0_2$ induction, and some statements of combinatorics are equivalent over $\mathsf{RCA}_0$ to forms of induction or bounding. The next lesson introduces the non-standard models in which these phenomena occur.

## Exercises

::::exercise{difficulty=1}
Show that the union of an increasing sequence of Turing ideals is a Turing ideal, and deduce that for every sequence $Z_0 \leq_T Z_1 \leq_T \cdots$, the class $\{ X : \exists n\ X \leq_T Z_n \}$ is an ω-model of $\mathsf{RCA}_0$.

:::solution
Let $\mathcal I = \bigcup_n \mathcal I_n$. If $X, Y \in \mathcal I$, both belong to some $\mathcal I_n$, since the sequence increases, so $X \oplus Y \in \mathcal I_n \subseteq \mathcal I$. If $Y \leq_T X \in \mathcal I_n$, then $Y \in \mathcal I_n$. The union is non-empty. The classes $\{ X : X \leq_T Z_n \}$ are Turing ideals, since $X, Y \leq_T Z_n$ implies $X \oplus Y \leq_T Z_n$ and $\leq_T$ is transitive; they increase with $n$, since $Z_n \leq_T Z_{n+1}$, so their union is a Turing ideal, and an ω-model of $\mathsf{RCA}_0$ by :ref{#thm-rca-turing-ideal}.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{RCA}_0$ proves the **$\Pi^0_1$ least number principle**: if $\psi$ is $\Pi^0_1$ and $\psi(a)$ holds for some $a$, then there is a least $n$ with $\psi(n)$.

:::solution
Write $\psi(n)$ as $\forall x\, \theta(n, x)$ with $\theta$ bounded ($x$ may be a block of variables; then $\exists x < s$ bounds each of them). Suppose that $\psi(a)$ holds and there is no least $n$ with $\psi(n)$. Let $\varphi(m)$ be the formula
$$
\exists s\, \forall k \leq m\, \exists x < s\ \neg \theta(k, x),
$$
which is $\Sigma^0_1$, and states that every $k \leq m$ fails $\psi$, with witnesses below a common bound $s$. If $\psi(0)$ held, $0$ would be the least $n$ with $\psi(n)$; so there is $x$ with $\neg \theta(0, x)$, and $s = x + 1$ witnesses $\varphi(0)$. If $s$ witnesses $\varphi(m)$, then $\neg \psi(k)$ for every $k \leq m$, so $\psi(m+1)$ fails, as $m + 1$ would otherwise be least; take $x$ with $\neg \theta(m + 1, x)$; then $\max(s, x + 1)$ witnesses $\varphi(m + 1)$. By $\Sigma^0_1$ induction, $\varphi(a)$ holds, so $\neg \psi(a)$, a contradiction.

The common bound $s$ is what keeps $\varphi$ in $\Sigma^0_1$: the formula $\forall k \leq m\ \neg \psi(k)$ is a bounded universal quantifier in front of a $\Sigma^0_1$ formula, and is not $\Sigma^0_1$ as written.
:::
::::

## Notes and references

Friedman introduced $\mathsf{RCA}_0$ (1976), in an equivalent form based on primitive recursion rather than $\Sigma^0_1$ induction; the present axiomatization is Simpson's (Definition II.1.5). The characterization of its ω-models (:ref{#thm-rca-turing-ideal}) is Simpson, Theorem II.1.7, and Dzhafarov–Mummert, Theorem 5.5.3. The formalization of primitive recursion and the $\Pi^0_1$ induction scheme are in Simpson, Section II.3 (Theorem II.3.4 and Corollary II.3.10, the latter proved there through bounded $\Sigma^0_1$ comprehension, Theorem II.3.9); Dzhafarov–Mummert discuss the choice of $\Sigma^0_1$ induction in their Section 6.6, where the result of Hirschfeldt and Shore is Theorem 6.6.1.

- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II* (abstracts), Journal of Symbolic Logic 41 (1976), 557–559.
- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections II.1–II.3.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 5.5 and Section 6.6.
