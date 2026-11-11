---
title: First-order parts and conservation
summary: Conservative extensions and ω-extensions; ACA₀ is conservative over Peano arithmetic and RCA₀ over IΣ₁ (Friedman), by expanding a model of arithmetic with its definable sets; the Jockusch–Solovay bound on the solutions provided by ACA₀, and the unprovability of ACA₀′.
duration: 40
prerequisites: [induction-collection, big-five/aca0]
---

A subsystem of second-order arithmetic proves sentences about sets, but also sentences about numbers alone. Its **first-order part** is the set of sentences of first-order arithmetic that it proves. This lesson identifies the first-order parts of $\mathsf{ACA}_0$ and $\mathsf{RCA}_0$: they are Peano arithmetic and $\mathrm I\Sigma_1$. The method is model-theoretic: a model of the first-order theory is expanded into a model of the second-order theory with the same numbers, by adding the sets that are definable in it.

## Conservative extensions

The language $\mathcal L_1$ of first-order arithmetic is $\mathcal L_2$ without set variables and without $\in$. **Peano arithmetic** $\mathrm{PA}$ consists of the basic axioms and the induction scheme for all formulas of $\mathcal L_1$, and $\mathrm I\Sigma_n$ of the basic axioms and induction for $\Sigma_n$ formulas of $\mathcal L_1$; formulas of $\mathcal L_1$ may contain number parameters only. The results of the first lesson apply to these theories, with the same proofs.

:::definition{#def-conservative}
Let $S$ and $T$ be theories, in languages $\mathcal L_S \subseteq \mathcal L_T$, and $\Gamma$ a set of sentences of $\mathcal L_S$. The theory $T$ is **$\Gamma$-conservative** over $S$ if every sentence of $\Gamma$ provable in $T$ is provable in $S$. If $T$ proves every axiom of $S$ and is conservative over $S$ for all sentences of $\mathcal L_S$, then $T$ is a **conservative extension** of $S$, and the theorems of $S$ are the **first-order part** of $T$ when $\mathcal L_S = \mathcal L_1$.
:::

:::definition{#def-omega-extension}
An $\mathcal L_2$-structure $\mathcal N$ is an **ω-extension** of an $\mathcal L_2$-structure $\mathcal M$ if both have the same first-order part, with the same operations, and the second-order part of $\mathcal M$ is included in that of $\mathcal N$. An $\mathcal L_2$-structure $\mathcal N$ is an ω-extension of an $\mathcal L_1$-structure $M$ if its first-order part is $M$.
:::

The name refers to the fact that the numbers are unchanged; an ω-extension need not be an ω-model. Satisfaction of an arithmetic formula, with parameters in the smaller structure, is the same in both structures, since set quantifiers do not occur and number quantifiers range over the same domain.

We use two facts from logic, for countable languages: the completeness theorem, already used in the course on second-order arithmetic, and the fact that a consistent theory has a **countable** model, which follows from the usual proof of completeness.

:::proposition{#prop-conservation-method}
Let $S$ be an $\mathcal L_1$-theory and $T$ an $\mathcal L_2$-theory. If every countable model of $S$ has an ω-extension that satisfies $T$, then $T$ is $\mathcal L_1$-conservative over $S$.
:::

:::proof{of=prop-conservation-method}
Let $\sigma$ be an $\mathcal L_1$ sentence not provable in $S$. Then $S + \neg \sigma$ is consistent, and has a countable model $M$. Let $\mathcal N$ be an ω-extension of $M$ satisfying $T$. Since $\sigma$ has no set variables, $\mathcal N \models \neg \sigma$. So $T + \neg \sigma$ has a model, and $T$ does not prove $\sigma$.
:::

## Peano arithmetic and ACA₀

:::theorem[Friedman]{#thm-aca0-pa}
$\mathsf{ACA}_0$ is a conservative extension of $\mathrm{PA}$.
:::

:::proof{of=thm-aca0-pa}
$\mathsf{ACA}_0$ proves the induction scheme for arithmetic formulas, in particular for all formulas of $\mathcal L_1$ (:ref{#def-aca0}). Conversely, let $M$ be a countable model of $\mathrm{PA}$, and let $\mathcal D$ be the class of subsets of $M$ definable in $M$ by a formula of $\mathcal L_1$ with parameters in $M$. Let $\mathcal N = (M, \mathcal D)$. We show $\mathcal N \models \mathsf{ACA}_0$, which proves the theorem by :ref{#prop-conservation-method}.

The basic axioms hold since $M$ satisfies them. Let $\varphi(n)$ be an arithmetic formula with set parameters $X_1, \dots, X_k \in \mathcal D$ and number parameters in $M$, and let $\delta_i(u)$ be an $\mathcal L_1$ formula with parameters defining $X_i$ in $M$. Replacing every atomic formula $t \in X_i$ by $\delta_i(t)$ gives an $\mathcal L_1$ formula $\varphi^*$ with parameters in $M$, and for every $n \in M$, $\mathcal N \models \varphi(n)$ if and only if $M \models \varphi^*(n)$, by induction on $\varphi$. So the set defined by $\varphi$ in $\mathcal N$ is defined by $\varphi^*$ in $M$, and belongs to $\mathcal D$: arithmetic comprehension holds. For the same reason, $\Sigma^0_1$ induction in $\mathcal N$ reduces to induction in $M$ for $\varphi^*$, which holds in $\mathrm{PA}$.
:::

So the arithmetic consequences of arithmetic comprehension are exactly the theorems of Peano arithmetic. The point of the proof is that the sets added are definable from the numbers, so that statements about them translate back into first-order statements.

## IΣ₁ and RCA₀

For $\mathsf{RCA}_0$, the analogous class consists of the $\Delta_1$-definable sets. A set $X \subseteq M$ is **$\Delta_1$-definable** in a model $M$ of $\mathcal L_1$ if there are a $\Sigma_1$ formula $\varphi$ and a $\Pi_1$ formula $\psi$ of $\mathcal L_1$, with parameters in $M$, such that $X = \{ n : M \models \varphi(n) \} = \{ n : M \models \psi(n) \}$. The same definition applies to $\Sigma^0_1$ and $\Pi^0_1$ formulas of $\mathcal L_2$ with parameters in an $\mathcal L_2$-structure. Substitution is now delicate: replacing $t \in X$ by a $\Sigma_1$ formula inside a bounded universal quantifier gives a formula that is not $\Sigma_1$, and collection is needed to restore the form.

:::lemma{#lem-delta1-substitution}
Let $\mathcal M$ be an $\mathcal L_2$-structure satisfying $\mathsf I\Delta^0_0 + \mathsf B\Sigma^0_1$, and $X_1, \dots, X_k \subseteq M$ sets $\Delta_1$-definable in $\mathcal M$. Let $\mathcal M'$ be the ω-extension of $\mathcal M$ obtained by adding $X_1, \dots, X_k$. For every $\Sigma^0_1$ formula $\theta$ with parameters in $\mathcal M'$, there is a $\Sigma^0_1$ formula $\theta^*$ with parameters in $\mathcal M$, with the same free variables, such that $\mathcal M' \models \forall \bar x\, (\theta \leftrightarrow \theta^*)$. The same holds for $\Pi^0_1$ formulas. If $\mathcal M$ is an $\mathcal L_1$-structure, in which case $\mathcal M'$ has $X_1, \dots, X_k$ as its only sets, $\theta^*$ is a formula of $\mathcal L_1$.
:::

:::proof{of=lem-delta1-substitution}
Let $\varphi_i$ and $\psi_i$ be $\Sigma^0_1$ and $\Pi^0_1$ formulas with parameters in $\mathcal M$ defining $X_i$. Write $\theta = \exists y\, \delta$ with $\delta$ bounded, and put $\delta$ in negation normal form, so that negations only apply to atomic formulas. Replace every atomic formula $t \in X_i$ by $\varphi_i(t)$, and every negated atomic formula $t \notin X_i$ by $\neg \psi_i(t)$, a $\Sigma^0_1$ formula. The result $\delta'$ has parameters in $\mathcal M$, and is equivalent to $\delta$ in $\mathcal M'$, since the replaced formulas are equivalent there. It is built from $\Sigma^0_1$ formulas by $\wedge$, $\vee$ and bounded quantifiers, so by :ref{#lem-collection-closure}, applied in $\mathcal M$, which satisfies $\mathsf B\Sigma^0_1$, it is equivalent in $\mathcal M$ to a $\Sigma^0_1$ formula $\delta^*$. The equivalence involves no $X_i$, so it also holds in $\mathcal M'$. Let $\theta^* = \exists y\, \delta^*$. For a $\Pi^0_1$ formula, apply the result to its negation. If $\mathcal M$ has no sets, the formulas $\varphi_i, \psi_i$ and the result are formulas of $\mathcal L_1$.
:::

:::theorem[Friedman]{#thm-rca0-isigma1}
$\mathsf{RCA}_0$ is a conservative extension of $\mathrm I\Sigma_1$.
:::

:::proof{of=thm-rca0-isigma1}
$\mathsf{RCA}_0$ proves $\Sigma^0_1$ induction, in particular for formulas of $\mathcal L_1$. Conversely, let $M$ be a countable model of $\mathrm I\Sigma_1$, and $\mathcal D$ the class of sets $\Delta_1$-definable in $M$. By :ref{#thm-induction-collection}, $M$ satisfies $\Sigma_1$ collection. Let $\mathcal N = (M, \mathcal D)$. Every formula with parameters in $\mathcal N$ uses finitely many sets of $\mathcal D$, so :ref{#lem-delta1-substitution} applies to it.

- *Basic axioms*: they hold in $M$.
- *$\Sigma^0_1$ induction*: let $\theta(x)$ be $\Sigma^0_1$ with parameters in $\mathcal N$, and $\theta^*$ the $\Sigma_1$ formula of $\mathcal L_1$ given by the lemma. Induction holds in $M$ for $\theta^*$, hence in $\mathcal N$ for $\theta$.
- *$\Delta^0_1$ comprehension*: let $\varphi$ be $\Sigma^0_1$ and $\psi$ be $\Pi^0_1$, with parameters in $\mathcal N$, such that $\mathcal N \models \forall n\, (\varphi(n) \leftrightarrow \psi(n))$. The lemma gives $\varphi^*$ in $\Sigma_1$ and $\psi^*$ in $\Pi_1$, both formulas of $\mathcal L_1$ that define the same set $X$ in $M$. So $X \in \mathcal D$, and $\mathcal N \models \forall n\, (n \in X \leftrightarrow \varphi(n))$.

So $\mathcal N \models \mathsf{RCA}_0$, and :ref{#prop-conservation-method} concludes.
:::

:::quiz[the first-order part of RCA₀]
In :ref{#lem-delta1-substitution}, why must the atomic formula $t \notin X_i$ be replaced by $\neg \psi_i(t)$ rather than by $\neg \varphi_i(t)$?

- [x] Because $\neg \varphi_i(t)$ is $\Pi^0_1$, while $\neg \psi_i(t)$ is $\Sigma^0_1$; using both definitions of a $\Delta_1$ set, every literal becomes $\Sigma^0_1$, and the result stays in the class closed under bounded quantification by collection.
- [ ] Because $\varphi_i$ does not define $X_i$.

  Both formulas define $X_i$; the choice is about complexity.
- [ ] Because negations are not allowed in $\Sigma^0_1$ formulas.

  Negations of atomic formulas are allowed in bounded formulas.

---

Where is $\Sigma_1$ collection in $M$ used in the proof of :ref{#thm-rca0-isigma1}?

- [x] To show that a formula built from $\Sigma_1$ formulas with bounded quantifiers is equivalent to a $\Sigma_1$ formula; without it, $\Sigma^0_1$ formulas with parameters in $\mathcal D$ would not translate into $\Sigma_1$ formulas of $M$.
- [ ] To show that $\mathcal D$ is countable.

  Countability follows from the countability of $M$ and of the set of formulas.
- [ ] To prove the basic axioms in $\mathcal N$.

  The basic axioms hold because they hold in $M$.
:::

$\mathsf{RCA}_0$ thus proves exactly the arithmetic sentences of $\mathrm I\Sigma_1$, and in particular, by the theorem of Paris and Kirby recalled in the previous lesson, it does not prove $\mathsf B\Sigma^0_2$. Parsons showed that $\mathrm I\Sigma_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic; a $\Pi_2$ sentence $\forall x\, \exists y\, \varphi(x, y)$, with $\varphi$ bounded, provable in $\mathsf{RCA}_0$ therefore has a primitive recursive witness function.

## The Jockusch–Solovay bound

$\mathsf{ACA}_0$ proves, for each standard $k$, that every set has a $k$-th jump. The next theorem shows that its theorems of the form "for every instance, there is a solution" always have solutions of bounded arithmetic complexity. We write $Y \leq_T X^{(k)}$ for the arithmetic formula "there is $Z$ coding the sequence $X, X', \dots, X^{(k)}$ and $Y \leq_T X^{(k)}$", and use the formalized version of Post's theorem: $\mathsf{ACA}_0$ proves that every set defined by a $\Sigma^0_k$ formula with set parameter $X$ is computable in $X^{(k)}$. We admit this formalization (Simpson, Section VIII.1).

:::theorem[Jockusch, Solovay]{#thm-jockusch-solovay}
Let $F(X)$ and $G(X, Y)$ be arithmetic formulas without other free variables. If $\mathsf{ACA}_0$ proves $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$, then there is $k \in \nat$ such that $\mathsf{ACA}_0$ proves $\forall X\, (F(X) \rightarrow \exists Y\, (Y \leq_T X^{(k)} \wedge G(X, Y)))$.
:::

:::proof{of=thm-jockusch-solovay}
Suppose the conclusion fails for every $k$. Add a set constant $C$ to the language, and let $\gamma_k$ be the sentence $\forall Y\, (Y \leq_T C^{(k)} \rightarrow \neg G(C, Y))$. For each $k$, $\mathsf{ACA}_0 + F(C) + \gamma_k$ is consistent. Since $\mathsf{ACA}_0$ proves $\gamma_{k+1} \rightarrow \gamma_k$, every finite subset of $\mathsf{ACA}_0 + F(C) + \{ \gamma_k : k \in \nat \}$ is consistent, so the whole theory has a model $\mathcal M = (M, \mathcal S, C)$ by compactness.

Let $\mathcal S'$ be the class of sets in $\mathcal S$ definable in $\mathcal M$ by an arithmetic formula with set parameter $C$ and number parameters, and $\mathcal M' = (M, \mathcal S')$. Then $\mathcal M' \models \mathsf{ACA}_0$: a set defined by an arithmetic formula with parameters in $\mathcal S'$ is, after substitution of their definitions, defined by an arithmetic formula with parameter $C$; it exists in $\mathcal S$ by arithmetic comprehension in $\mathcal M$, so it belongs to $\mathcal S'$; induction holds since $\mathcal S' \subseteq \mathcal S$.

The formula $F(C)$ is arithmetic and holds in $\mathcal M$, so it holds in $\mathcal M'$. Let $Y \in \mathcal S'$, defined by a $\Sigma^0_k$ formula with parameter $C$, for some standard $k$. By the formalized Post theorem, $\mathcal M \models Y \leq_T C^{(k)}$, so $\mathcal M \models \neg G(C, Y)$ by $\gamma_k$, and $\mathcal M' \models \neg G(C, Y)$. Hence $\mathcal M' \models F(C) \wedge \forall Y\, \neg G(C, Y)$, and $\mathsf{ACA}_0$ does not prove $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$, contrary to the hypothesis.
:::

Let $\mathsf{ACA}_0'$ be $\mathsf{RCA}_0$ together with the axiom "for every $n$ and every $X$, there is a sequence $Y_0, \dots, Y_n$ with $Y_0 = X$ and $Y_{i+1} = Y_i'$ for $i < n$". Every ω-model of $\mathsf{ACA}_0$ satisfies it, since it is closed under the jump and its numbers are standard.

:::corollary{#cor-aca0-prime}
$\mathsf{ACA}_0$ does not prove $\mathsf{ACA}_0'$.
:::

:::proof{of=cor-aca0-prime}
Let $F(X)$ be "the column $X^{[0]}$ is non-empty", and $G(X, Y)$ be "$Y$ codes a sequence $Y_0, \dots, Y_n$ with $Y_0 = X^{[1]}$, $Y_{i+1} = Y_i'$, where $n$ is the least element of $X^{[0]}$". Both are arithmetic, and $\mathsf{ACA}_0'$ proves $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$. If $\mathsf{ACA}_0$ proved it, then for some $k$ it would prove the version with $Y \leq_T X^{(k)}$, and this version would hold in the ω-model $\mathcal P(\nat)$. Take $X$ with $X^{[0]} = \{ k + 1 \}$ and $X^{[1]} = \emptyset$; then $X \equiv_T \emptyset$, and a solution $Y$ computes $\emptyset^{(k+1)}$ while $Y \leq_T X^{(k)} \equiv_T \emptyset^{(k)}$, which contradicts the jump theorem.
:::

The separation needs non-standard models: in a model of $\mathsf{ACA}_0 + \neg \mathsf{ACA}_0'$, some non-standard $n$ has no sequence of $n$ jumps, because the induction needed to iterate the jump $n$ times is not available.

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{WKL}_0$ is not $\mathcal L_1$-conservative over $\mathrm I\Sigma_1$ if and only if it proves an $\mathcal L_1$ sentence that $\mathsf{RCA}_0$ does not prove. Deduce from :ref{#thm-rca0-isigma1} that, to show that $\mathsf{WKL}_0$ is a conservative extension of $\mathrm I\Sigma_1$, it suffices to show that every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$.

:::solution
By :ref{#thm-rca0-isigma1}, the $\mathcal L_1$ sentences provable in $\mathsf{RCA}_0$ are those provable in $\mathrm I\Sigma_1$, and $\mathsf{WKL}_0$ proves all of them; this gives the first statement. Suppose every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$, and let $\sigma$ be an $\mathcal L_1$ sentence not provable in $\mathsf{RCA}_0$. A countable model of $\mathsf{RCA}_0 + \neg \sigma$ has an ω-extension satisfying $\mathsf{WKL}_0$, in which $\neg \sigma$ still holds, so $\mathsf{WKL}_0$ does not prove $\sigma$. With the first statement, $\mathsf{WKL}_0$ is a conservative extension of $\mathrm I\Sigma_1$.
:::
::::

::::exercise{difficulty=2}
Let $M$ be a countable model of $\mathrm I\Sigma_1$ and $\mathcal N = (M, \mathcal D)$ the model of the proof of :ref{#thm-rca0-isigma1}. Show that $\mathcal D$ is the least second-order part of a model of $\mathsf{RCA}_0$ with first-order part $M$: every model $(M, \mathcal S)$ of $\mathsf{RCA}_0$ satisfies $\mathcal D \subseteq \mathcal S$.

:::solution
Let $X \in \mathcal D$, defined in $M$ by a $\Sigma_1$ formula $\varphi$ and a $\Pi_1$ formula $\psi$ of $\mathcal L_1$. In $(M, \mathcal S)$, these formulas have the same meaning, since they contain no set variables, so $(M, \mathcal S) \models \forall n\, (\varphi(n) \leftrightarrow \psi(n))$. By $\Delta^0_1$ comprehension in $(M, \mathcal S)$, there is $Y \in \mathcal S$ with $(M, \mathcal S) \models \forall n\, (n \in Y \leftrightarrow \varphi(n))$, that is, $Y = X$. This is the analogue, for non-standard models, of the fact that the computable sets form the least ω-model of $\mathsf{RCA}_0$.
:::
::::

## Notes and references

Friedman announced the conservation results of this lesson in 1976; the proofs are in Simpson's monograph, Section IX.1. The Jockusch–Solovay theorem was observed independently by both authors; the proof presented here was communicated by Jockusch, and appears in a paper of Wang.

- H. Friedman, *Systems of second order arithmetic with restricted induction I, II* (abstracts), Journal of Symbolic Logic 41 (1976), 557–559.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Chapter IX.
- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
