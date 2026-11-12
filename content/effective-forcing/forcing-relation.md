---
title: The forcing relation
summary: Arithmetic formulas about the generic set; the forcing relation of a notion of forcing; extension, consistency and density; forcing implies truth for generic sets; n-generic filters; forcing as density.
duration: 45
prerequisites: [notions-of-forcing, arithmetic-hierarchy/post-theorem, cohen-genericity/one-genericity]
---

In the previous lesson each property of generic sets was obtained from an ad hoc dense set. The **forcing relation** gives such dense sets uniformly for all properties expressed by arithmetic formulas. A condition $c$ forces a formula $\varphi$, written $c \Vdash \varphi$, if $c$ guarantees that $\varphi$ will hold for the set built, provided the construction continues generically. For formulas with at most one unbounded quantifier this can be required of all members of $c$. For more complex formulas it cannot: in Cohen forcing, no string has only infinite sets as members, yet every sufficiently generic set is infinite. The definition therefore says that $c$ forces a universal statement if no extension of $c$ forces a counterexample. The main theorem of the lesson, that forcing implies truth for generic sets, justifies this choice.

## Formulas about the generic set

We use formulas in a normal form adapted to oracle computations. The letter $G$ stands for the set being built.

:::definition{#def-forcing-formula}
The **formulas** of level $n \geq 1$, with free number variables $\vec x$, are defined as follows.

1. A **$\Sigma^0_1$ formula** is an expression $\Phi^G_e(\vec x)\converge$, and a **$\Pi^0_1$ formula** an expression $\Phi^G_e(\vec x)\diverge$, where $e$ is an index of a Turing functional.
2. A **$\Sigma^0_{n+1}$ formula** is an expression $\exists y\ \psi(\vec x, y)$ with $\psi$ a $\Pi^0_n$ formula, and a **$\Pi^0_{n+1}$ formula** an expression $\forall y\ \psi(\vec x, y)$ with $\psi$ a $\Sigma^0_n$ formula.

A **sentence** is a formula whose free variables have been replaced by numbers. For a set $X$, $X \models \varphi$ means that $\varphi$ is true when $G$ is interpreted by $X$. The **negation** $\neg \varphi$ of a formula is the formula of the dual class obtained by exchanging $\converge$ and $\diverge$, and $\exists$ and $\forall$.
:::

So $\neg \neg \varphi = \varphi$, the negation of a $\Sigma^0_n$ formula is $\Pi^0_n$, and $X \models \neg \varphi$ if and only if $X \not\models \varphi$. Formulas are finite objects and are coded by numbers.

These formulas express all arithmetic properties. Fix a set $X$. By the relativization of :ref{#thm-ce-characterizations}, the $\Sigma^0_1(X)$ relations are the domains of the functionals $\Phi^X_e$; a $\Pi^0_n(X)$ relation is the complement of a $\Sigma^0_n(X)$ relation, and a $\Sigma^0_{n+1}(X)$ relation is a projection of a $\Pi^0_n(X)$ relation (:ref{#def-relativized-hierarchy}). By induction on $n$, a relation $R(\vec x)$ is $\Sigma^0_n(X)$ if and only if $R = \{ \vec m : X \models \varphi(\vec m) \}$ for some $\Sigma^0_n$ formula $\varphi(\vec x)$. Moreover, the proof of Post's theorem (:ref{#thm-post}) is uniform in the oracle, so for each $n \geq 1$ there is a single $\Sigma^0_n$ formula $\theta_n(x)$ such that $m \in X^{(n)} \iff X \models \theta_n(m)$ for every set $X$.

:::example{#ex-forcing-formulas}
1. "$e \in G'$" is the $\Sigma^0_1$ sentence $\Phi^G_e(e)\converge$.
2. Let $\Phi_a$ be the functional that on input $x$ searches for $y > x$ with $G(y) = 1$. Then "$G$ is infinite" is the $\Pi^0_2$ sentence $\forall x\ \Phi^G_a(x)\converge$, and "$G$ is finite" is its negation $\exists x\ \Phi^G_a(x)\diverge$.
3. "$\Phi^G_e$ is total" is the $\Pi^0_2$ sentence $\forall x\ \Phi^G_e(x)\converge$.
4. Formulas may also be built with functionals of an oracle $G \oplus Z$ for a fixed set $Z$; everything in this course relativizes to such formulas.
:::

## The forcing relation

:::definition{#def-forcing-relation}
Let $(\mathbb P, \leq, [\cdot])$ be a notion of forcing. The relation $c \Vdash \varphi$, read "$c$ **forces** $\varphi$", between conditions and sentences of level at least $1$ is defined by induction on the level.

1. If $\varphi$ is $\Sigma^0_1$ or $\Pi^0_1$, then $c \Vdash \varphi$ if every member of $c$ satisfies $\varphi$.
2. If $\varphi = \exists y\ \psi(y)$ is $\Sigma^0_{n+1}$, then $c \Vdash \varphi$ if $c \Vdash \psi(m)$ for some $m$.
3. If $\varphi = \forall y\ \psi(y)$ is $\Pi^0_{n+1}$, then $c \Vdash \varphi$ if there are no $d \leq c$ and $m$ with $d \Vdash \neg \psi(m)$.

A condition **decides** $\varphi$ if it forces $\varphi$ or $\neg \varphi$.
:::

At level $1$ the definition is the one used for strings in :ref{#prop-force-sigma1}: the convergence or divergence of a computation is forced if it holds for all members. The existential clause asks for an explicit witness. The universal clause is the only one that refers to extensions: $c$ forces $\forall y\ \psi(y)$ if, however the construction continues below $c$, it never reaches a condition that forces a counterexample.

:::example{#ex-forcing-relation}
1. **Cohen forcing.** Every string $\sigma$ forces "$G$ is infinite", $\forall x\ \Phi^G_a(x)\converge$ in the notation of :ref{#ex-forcing-formulas}. Indeed $\tau \Vdash \Phi^G_a(m)\diverge$ would mean that no member of $\tau$ has an element above $m$, which fails for the member $\tau 1 1 \cdots$. But the finite set $\sigma 0 0 \cdots$ is a member of $\sigma$: forcing a $\Pi^0_2$ sentence does not make it true for all members.
2. **Jockusch–Soare forcing.** A class $\mathcal P$ forces "$\Phi^G_e$ is total" if and only if $\Phi^X_e$ is total for every $X \in \mathcal P$. If $\Phi^X_e(m)\diverge$ for some $X \in \mathcal P$, the non-empty $\Pi^0_1$ class $\mathcal P \cap \{ X : \Phi^X_e(m)\diverge \}$ is an extension forcing $\Phi^G_e(m)\diverge$. Conversely, an extension forcing $\Phi^G_e(m)\diverge$ has a member, which is a member of $\mathcal P$.
3. **Computable Sacks forcing.** Let $T$ be a computable f-tree, $L = \bigcup_k T(0^k)$ its leftmost path, and $\Phi_e$ the functional such that $\Phi^X_e(x)$ searches for $k$ with $X \uh |T(0^k)| \neq T(0^k)$. Then $\Phi^X_e$ is total if and only if $X \neq L$. No subtree $S$ of $T$ forces $\Phi^G_e(m)\diverge$, since $S$ has paths other than $L$; so $T$ forces "$\Phi^G_e$ is total", although $L$ is a member of $T$ for which it fails. Unlike Jockusch–Soare forcing, a computable perfect tree cannot remove a single path.
:::

The second example shows a feature of forcing with $\Pi^0_1$ classes that lesson 4 develops: $\Pi^0_2$ sentences of this form are forced only when they hold for all members.

:::proposition{#prop-forcing-basic}
Let $c$ be a condition and $\varphi$ a sentence of level $n \geq 1$.

1. (**Extension**) If $c \Vdash \varphi$ and $d \leq c$, then $d \Vdash \varphi$.
2. (**Consistency**) $c$ does not force both $\varphi$ and $\neg \varphi$.
3. If $\varphi$ is $\Sigma^0_n$ and no extension of $c$ forces $\varphi$, then $c \Vdash \neg \varphi$.
4. (**Density**) The set $D_\varphi$ of conditions that decide $\varphi$ is dense.
:::

:::proof{of=prop-forcing-basic}
1. By induction on $n$. At level $1$, $[d] \subseteq [c]$. If $c \Vdash \psi(m)$, then $d \Vdash \psi(m)$ by induction. If no extension of $c$ forces $\neg \psi(m)$, then neither does any extension of $d$, which is an extension of $c$.
2. At level $1$, $[c]$ has a member, which satisfies exactly one of $\varphi$ and $\neg \varphi$. At level $n + 1$, one of the two sentences is $\exists y\ \psi(y)$ and the other is $\forall y\ \neg \psi(y)$. If $c \Vdash \psi(m)$, then $d = c$ is an extension of $c$ that forces $\neg \neg \psi(m) = \psi(m)$, so $c$ does not force $\forall y\ \neg \psi(y)$.
3. At level $1$, $\varphi$ is $\Phi^G_e(\vec m)\converge$. Suppose some member $X$ of $c$ satisfies $\varphi$, with use $u$. By refinement there is $d \leq c$ with $[d] \subseteq [X \uh u]$, and by the use principle (:ref{#thm-use-principle}) every member of $d$ satisfies $\varphi$; this contradicts the hypothesis. So every member satisfies $\neg \varphi$. At level $n + 1$, $\varphi = \exists y\ \psi(y)$. If some $d \leq c$ forced $\neg \neg \psi(m) = \psi(m)$, it would force $\varphi$. So $c \Vdash \forall y\ \neg \psi(y) = \neg \varphi$.
4. Since $D_\varphi = D_{\neg \varphi}$, we may assume that $\varphi$ is $\Sigma^0_n$. Given $c$, either some extension of $c$ forces $\varphi$, or $c$ forces $\neg \varphi$ by item 3.
:::

Item 3 fails for $\Pi^0_n$ sentences: a condition none of whose extensions forces a $\Pi^0_n$ sentence need not force its negation, which is existential and requires a witness (second exercise).

:::quiz[the basic properties of forcing]
In item 3 of :ref{#prop-forcing-basic}, at level $1$, where is the refinement property of the notion of forcing used?

- [x] To pass from one member $X$ of $c$ on which the computation converges to an extension all of whose members extend $X \uh u$, and on which the computation therefore converges.
- [ ] To show that $c$ has a member.

  Conditions have members by definition.
- [ ] To show that the use $u$ exists.

  The use exists because the computation converges.

---

Why does consistency at level $n + 1$ follow from the case $d = c$ in the universal clause?

- [x] Because $\forall y\ \neg \psi(y)$ forbids every extension of $c$, including $c$ itself, from forcing $\psi(m)$; and $c \Vdash \exists y\ \psi(y)$ provides such an $m$.
- [ ] Because $c$ has no extensions.

  Every condition extends itself, and usually has many other extensions.
- [ ] By consistency at level $1$ applied to $\psi(m)$.

  The argument does not need the induction hypothesis.
:::

## Forcing and truth

A generic filter decides every sentence, and the decisions it makes are correct for the set it determines.

:::definition{#def-n-generic-notion}
Let $n \geq 1$. A filter is **$n$-generic** (for $\mathbb P$) if it meets the sets $S_k$ of :ref{#lem-generic-set} and the sets $D_\varphi$ for all sentences $\varphi$ of level at most $n$. A set is $n$-generic for $\mathbb P$ if it is $G_F$ for an $n$-generic filter $F$.
:::

There are countably many sentences, so by :ref{#lem-rasiowa-sikorski} every condition belongs to an $n$-generic filter, and to a filter that is $n$-generic for every $n$. For Cohen forcing, the next lesson shows that this notion coincides with the $n$-genericity of :ref{#def-relative-genericity}.

:::theorem[Forcing and truth]{#thm-forcing-truth}
Let $F$ be an $n$-generic filter and $\varphi$ a sentence of level $k \leq n$.

1. If some $c \in F$ forces $\varphi$, then $G_F \models \varphi$.
2. $G_F \models \varphi$ if and only if some $c \in F$ forces $\varphi$.
:::

:::proof{of=thm-forcing-truth}
1. By induction on $k$, for all sentences of level $k$ at once. At level $1$, $G_F$ is a member of $c$ by :ref{#lem-generic-set}, so it satisfies $\varphi$. If $\varphi = \exists y\ \psi(y)$, then $c \Vdash \psi(m)$ for some $m$, and $G_F \models \psi(m)$ by the induction hypothesis. Let $\varphi = \forall y\ \psi(y)$ and $m \in \nat$. The sentence $\psi(m)$ has level $k - 1 \leq n$, so $F$ contains a condition $d$ deciding it, and a common extension $e \in F$ of $c$ and $d$, which decides $\psi(m)$ by extension. It does not force $\neg \psi(m)$, since $e \leq c$ and $c \Vdash \varphi$. So $e \Vdash \psi(m)$, and $G_F \models \psi(m)$ by the induction hypothesis. Hence $G_F \models \varphi$.
2. One direction is item 1. Conversely, $F$ contains a condition $c$ deciding $\varphi$. If $c \Vdash \neg \varphi$, item 1 applied to $\neg \varphi$, of the same level, gives $G_F \models \neg \varphi$. So if $G_F \models \varphi$, then $c \Vdash \varphi$.
:::

The proof of item 1 uses genericity only in the universal clause, and only for the sentences $\psi(m)$: a condition forcing $\forall y\ \psi(y)$ leaves open which of its members will be built, but no generic filter through it can choose a counterexample, since choosing one would mean passing through a condition that forces it.

:::quiz[forcing and truth]
In the proof of :ref{#thm-forcing-truth}, why is the condition $e$ taken as a common extension of $c$ and $d$, rather than $d$ itself?

- [x] Because the hypothesis $c \Vdash \forall y\ \psi(y)$ only constrains extensions of $c$, and $d$ need not extend $c$.
- [ ] Because $d$ might not belong to $F$.

  $d$ is chosen in $F$; the point is its relation to $c$.
- [ ] Because $d$ might not decide $\psi(m)$.

  $d$ is chosen in $D_{\psi(m)}$, so it decides $\psi(m)$.

---

Which property of the generic set $G_F$ does the theorem give for a $2$-generic filter of Cohen forcing?

- [x] $G_F$ is infinite, since every string forces "$G$ is infinite", a $\Pi^0_2$ sentence.
- [ ] $G_F$ is finite.

  No string forces "$G$ is finite", since every string forces its negation.
- [ ] Nothing, since some members of every string are finite.

  The theorem concerns the generic set, not all members of a condition.
:::

The forcing relation can also be characterized without reference to the syntax of the formula, by density.

:::corollary{#cor-forcing-density}
Let $c$ be a condition and $\varphi$ a sentence of level $n$. The following are equivalent:

1. $G_F \models \varphi$ for every $n$-generic filter $F$ containing $c$;
2. the set of conditions forcing $\varphi$ is dense below $c$.
:::

:::proof{of=cor-forcing-density}
(2 ⇒ 1) Let $F$ be $n$-generic with $c \in F$. It contains a condition $d$ deciding $\varphi$, and a common extension $e$ of $c$ and $d$, which decides $\varphi$. If $e \Vdash \neg \varphi$, then by extension no extension of $e$ forces $\varphi$, contradicting the density below $c$. So $e \Vdash \varphi$, and $G_F \models \varphi$ by :ref{#thm-forcing-truth}.

(1 ⇒ 2) Let $d \leq c$. By density, some $e \leq d$ decides $\varphi$. If $e \Vdash \neg \varphi$, an $n$-generic filter containing $e$ contains $c$, since filters are closed upward, and its set satisfies $\neg \varphi$, contradicting 1. So $e \Vdash \varphi$.
:::

Condition 1 depends only on the class $\{ X : X \models \varphi \}$, not on the formula. Two formulas of level $n$ that define the same class may be forced by different conditions, but they are forced densely below the same conditions. This is the sense in which the syntactic definition of forcing is harmless.

## Exercises

::::exercise{difficulty=1}
In Cohen forcing, let $\varphi$ be the $\Sigma^0_2$ sentence $\exists y\ \psi(y)$, where $\psi(y)$ is a $\Pi^0_1$ formula expressing "$G(0) = y$". Show that the empty string does not force $\varphi$, although every string of length $1$ does. Conclude that the set of conditions forcing a $\Sigma^0_2$ sentence may be dense below a condition that does not force it.

:::solution
The members of the empty string are all sets, and both values of $G(0)$ occur, so the empty string forces no $\psi(m)$, hence not $\varphi$. The string $i$ forces $\psi(i)$, since all its members have $G(0) = i$; so it forces $\varphi$. Every string has an extension of length at least $1$, so the set of conditions forcing $\varphi$ is dense below the empty string.
:::
::::

::::exercise{#exr-weak-forcing difficulty=2}
Say that $c$ **weakly forces** $\varphi$ if the set of conditions forcing $\varphi$ is dense below $c$. Show that forcing implies weak forcing, and that for a $\Pi^0_n$ sentence $\varphi$, $n \geq 1$, weak forcing implies forcing. Deduce, with the first exercise, that item 3 of :ref{#prop-forcing-basic} fails for $\Pi^0_2$ sentences.

:::solution
If $c \Vdash \varphi$, every extension forces $\varphi$, so the set is dense below $c$.

Let $\varphi$ be $\Pi^0_n$ and suppose $c$ weakly forces it. For $n = 1$, let $\varphi = \Phi^G_e(\vec m)\diverge$, and suppose a member $X$ of $c$ has $\Phi^X_e(\vec m)\converge$ with use $u$. By refinement some $d \leq c$ has all its members extending $X \uh u$, so they all satisfy $\neg \varphi$; an extension of $d$ forcing $\varphi$ would have a member satisfying $\varphi$, in $[d]$. This is a contradiction, so $c \Vdash \varphi$. For $n \geq 2$, let $\varphi = \forall y\ \psi(y)$ and suppose $d \leq c$ forces $\neg \psi(m)$. Some $e \leq d$ forces $\varphi$; it also forces $\neg \psi(m)$ by extension, while $e \Vdash \varphi$ forbids $e$ itself from forcing $\neg \psi(m)$. So $c \Vdash \varphi$.

In the first exercise, the $\Pi^0_2$ sentence $\neg \varphi$ is forced by no extension of the empty string, since every string of length $1$ forces $\varphi$ and extension and consistency forbid both. But the empty string does not force $\neg \neg \varphi = \varphi$.
:::
::::

## Notes and references

The forcing relation for arithmetic was defined by Feferman (1965), with atomic formulas $n \in G$ at the base and a clause for negation; Downey and Hirschfeldt reproduce this definition for Cohen forcing (Section 2.24, footnote to Definition 2.24.1), and Dzhafarov and Mummert (Section 7.4, Definition 7.4.1, Theorem 7.4.6) give it for arbitrary notions of forcing, with the corresponding theorem on forcing and truth. The definition used here, in which formulas of level $1$ are forced when all members satisfy them, is the syntactic forcing relation of Monin and Patey, chapter *Effective forcing*, section *Forcing relation*; it suits notions of forcing whose conditions are classes. The relation defined in this way is often called **strong forcing**; the weak forcing of :ref{#exr-weak-forcing} is the version common in set theory.

- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.24.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 7.4.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Forcing relation*.
