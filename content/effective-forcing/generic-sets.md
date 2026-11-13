---
title: Sufficiently generic sets
summary: Properties of every sufficiently generic set; density below a condition; earlier constructions recast as density statements for Cohen, Jockusch–Soare, computable Sacks and computable Mathias forcing; uniformly effectively dense families and effective generic sequences; arithmetic formulas about the generic set.
duration: 40
prerequisites: [notions-of-forcing, arithmetic-hierarchy/post-theorem, cohen-genericity/baire-category, pi01-classes/basis-theorems, immunity-growth/computably-dominated]
---

The previous lesson showed that every countable family of dense sets is met by some filter, and that the filter determines a set. This lesson introduces the language used for the rest of the course: a property holds for **every sufficiently generic set** if some countable family of dense sets forces it. It recasts the constructions of earlier courses in this language, and then measures their effectiveness: when the dense sets can be met by an $A$-computable procedure, the generic filter can be taken $A$-computable. The last section fixes the formulas used to state properties of generic sets.

## Sufficiently generic sets

:::definition{#def-generic-notion}
A property holds for **every sufficiently generic set** (for a notion of forcing $\mathbb P$) if there is a countable family $\mathcal D$ of dense sets such that $G_F$ has the property for every $\mathcal D$-generic filter $F$. It holds for every sufficiently generic set **below** a condition $c$ if this holds for the $\mathcal D$-generic filters containing $c$.
:::

As in :ref{#def-sufficiently-generic}, countably many properties that hold for every sufficiently generic set hold simultaneously for every sufficiently generic set, by merging the families. For Cohen forcing, a filter meeting every $S_n$ is the set of prefixes of $G_F$, so a set is $\mathcal D$-generic in the sense of :ref{#def-d-generic} exactly when its filter of prefixes is $\mathcal D$-generic: the two definitions agree.

The density of a set below a condition suffices for the generic filters containing that condition.

:::lemma{#lem-dense-below}
Let $D$ be dense below $c$. Every sufficiently generic filter containing $c$ meets $D$.
:::

:::proof{of=lem-dense-below}
Let $Q$ be the set of conditions incompatible with $c$. The set $D \cup Q$ is dense: a condition $d$ is either incompatible with $c$, hence in $Q$, or has a common extension $d'$ with $c$, which has an extension in $D$ since $d' \leq c$. A filter meeting $D \cup Q$ and containing $c$ does not meet $Q$, since any two of its elements are compatible. So it meets $D$.
:::

:::quiz[density below a condition]
In :ref{#lem-dense-below}, why can a filter containing $c$ not meet the set $Q$ of conditions incompatible with $c$?

- [x] Because any two elements of a filter have a common extension, so every element of the filter is compatible with $c$.
- [ ] Because $Q$ is not dense.

  $Q$ alone is usually not dense; the argument uses that $D \cup Q$ is dense, and that a filter through $c$ avoids $Q$.
- [ ] Because $c \in D$.

  Nothing says that $c$ belongs to $D$.
:::

## Examples from earlier courses

The previous courses proved many density statements without the vocabulary of forcing. Rephrased, they give properties of the sufficiently generic sets. Each item names the dense sets; the technique is always the same, **genericity by density**: a property holds for every sufficiently generic set as soon as, for each of countably many requirements, the conditions all of whose members satisfy the requirement form a dense set.

:::example{#ex-generic-notions}
1. **Cohen forcing.** Every sufficiently generic set is not computable, and does not compute a given non-computable set (:ref{#ex-generic-properties}).
2. **Jockusch–Soare forcing.** Every sufficiently generic set is computably dominated: by the proof of :ref{#thm-dominated-basis}, for each $e$ the set of classes $\mathcal Q$ such that either $\Phi^X_e(m)\diverge$ for some $m$ and every $X \in \mathcal Q$, or $\Phi^X_e$ is total for every $X \in \mathcal Q$, is dense; in the second case :ref{#lem-uniform-bound} gives a computable bound for every member. Similarly, by :ref{#lem-uniform-cone}, every sufficiently generic set does not compute a given non-computable set. A sufficiently generic set may be computable: if $Y$ is computable, $\{ Y \}$ is a condition, and every filter containing it determines $Y$. Below a condition without computable member, every sufficiently generic set is non-computable.
3. **Computable Sacks forcing.** Every sufficiently generic set is non-computable and computably dominated, by :ref{#lem-ftree-noncomputable} and :ref{#lem-ftree-domination}: each lemma says that a set of conditions is dense.
4. **Computable Mathias forcing.** Every sufficiently generic set is infinite: given $(\sigma, X)$ and $m$, adding to $\sigma$ an element $n > m$ of $X$, and removing from $X$ the numbers up to $n$, gives an extension all of whose members have an element above $m$. For every computable sequence of sets $\vec R = (R_i)$, every sufficiently generic set is **$\vec R$-cohesive**, that is, $G \subseteq^* R_i$ or $G \subseteq^* \overline{R_i}$ for every $i$ (the notion is studied in :ref{to="ramsey-theorem/cohesiveness"}): one of $X \cap R_i$ and $X \setminus R_i$ is infinite, so $(\sigma, X \cap R_i)$ or $(\sigma, X \setminus R_i)$ is an extension, with a computable reservoir, and its members $G$ satisfy $G \subseteq^* R_i$ or $G \subseteq^* \overline{R_i}$.
:::

## Effective genericity

The properties of sufficiently generic sets in :ref{#ex-generic-notions} forget the effectiveness of the constructions they come from. It is recovered by measuring how hard it is to find extensions in the dense sets.

:::theorem{#thm-effective-generic}
Let $\mathbb P$ be a notion of forcing whose conditions are given by codes, that is, by a partial map from $\nat$ onto $\mathbb P$. Let $A$ be a set, and $D_0, D_1, \dots$ dense sets such that some partial $A$-computable function $h$ satisfies $h(c, i) \leq c$ and $h(c, i) \in D_i$ for every code $c$ and every $i$. Then for every condition $c$ there is an $A$-computable sequence of codes of conditions $c = c_0 \geq c_1 \geq \cdots$ generating a filter that meets every $D_i$.
:::

:::proof{of=thm-effective-generic}
Let $c_{i+1} = h(c_i, i)$. The function $h$ is defined on codes of conditions, so the sequence is defined, and computed by iterating $h$.
:::

The dense sets of such a family are said to be **uniformly $A$-effectively dense**. Whether the set $G_F$ is then computable in $A$ depends on the notion of forcing: one must also extract prefixes of $G_F$ from the conditions.

:::example{#ex-low-basis-forcing}
The low basis theorem (:ref{#thm-low-basis}) is an instance with $A = \emptyset'$ and Jockusch–Soare forcing, a condition being given by an index of a computable tree. For each $e$, let $D_e$ be the set of classes $\mathcal Q$ such that $\Phi^X_e(e)\converge$ for every member $X$, or $\Phi^X_e(e)\diverge$ for every member. Given $\mathcal Q$, the oracle $\emptyset'$ decides whether $\mathcal Q \cap \{ X : \Phi^X_e(e)\diverge \}$ is empty (:ref{#prop-pi01-emptiness}), and returns this class if it is non-empty, $\mathcal Q$ otherwise. Likewise $\emptyset'$ finds a string $\sigma$ of length $n$ with $\mathcal Q \cap [\sigma] \neq \emptyset$, so the sets $S_n$ are uniformly $\emptyset'$-effectively dense. Along the resulting $\emptyset'$-computable sequence, the prefixes of $G_F$ and the decisions about $\Phi^{G_F}_e(e)$ are computed by $\emptyset'$; so $G_F$ is low.
:::

:::quiz[effective genericity]
In :ref{#ex-low-basis-forcing}, why does the oracle $\emptyset'$ suffice to find, from an index of $\mathcal Q$, an extension in $D_e$?

- [x] Because the only choice is whether the $\Pi^0_1$ class $\mathcal Q \cap \{ X : \Phi^X_e(e)\diverge \}$ is empty, and emptiness of a $\Pi^0_1$ class is $\Sigma^0_1$, uniformly in an index; an index of that class is computed from indices of $\mathcal Q$ and $\Phi_e$.
- [ ] Because $\emptyset'$ computes a member of $\mathcal Q$.

  It does, by the low basis theorem, but the argument does not use a member: the extension is a class, found from its index.
- [ ] Because every class $\mathcal Q$ already belongs to $D_e$.

  A class may have members on which $\Phi_e(e)$ converges and members on which it diverges; it is then not in $D_e$.
:::

## Formulas about the generic set

The properties of generic sets studied in the rest of the course are expressed by formulas in a normal form adapted to oracle computations, with one unbounded quantifier per level. The letter $G$ stands for the set being built. The next lesson defines, for each such formula, which conditions force it.

:::definition{#def-forcing-formula}
The **formulas** of level $n \geq 1$, with free number variables $\vec x$, are defined as follows.

1. A **$\Sigma^0_1$ formula** is an expression $\Phi^G_e(\vec x)\converge$, and a **$\Pi^0_1$ formula** an expression $\Phi^G_e(\vec x)\diverge$, where $e$ is an index of a Turing functional.
2. A **$\Sigma^0_{n+1}$ formula** is an expression $\exists y\ \psi(\vec x, y)$ with $\psi$ a $\Pi^0_n$ formula, and a **$\Pi^0_{n+1}$ formula** an expression $\forall y\ \psi(\vec x, y)$ with $\psi$ a $\Sigma^0_n$ formula.

A **sentence** is a formula whose free variables have been replaced by numbers. For a set $X$, $X \models \varphi$ means that $\varphi$ is true when $G$ is interpreted by $X$. The **negation** $\neg \varphi$ of a formula is the formula of the dual class obtained by exchanging $\converge$ and $\diverge$, and $\exists$ and $\forall$.
:::

So $\neg \neg \varphi = \varphi$, the negation of a $\Sigma^0_n$ formula is $\Pi^0_n$, and $X \models \neg \varphi$ if and only if $X \not\models \varphi$. Formulas are finite objects and are coded by numbers.

These formulas express all arithmetic properties. By the relativization of :ref{#thm-ce-characterizations}, the $\Sigma^0_1(X)$ relations are the domains of the functionals $\Phi^X_e$, and by :ref{#def-relativized-hierarchy} and induction on $n$, a relation $R(\vec x)$ is $\Sigma^0_n(X)$ if and only if $R = \{ \vec m : X \models \varphi(\vec m) \}$ for some $\Sigma^0_n$ formula $\varphi(\vec x)$. Moreover, the proof of Post's theorem (:ref{#thm-post}) is uniform in the oracle, so for each $n \geq 1$ there is a single $\Sigma^0_n$ formula $\theta_n(x)$ such that $m \in X^{(n)} \iff X \models \theta_n(m)$ for every set $X$.

:::example{#ex-forcing-formulas}
1. "$e \in G'$" is the $\Sigma^0_1$ sentence $\Phi^G_e(e)\converge$.
2. Let $\Phi_a$ be the functional that on input $x$ searches for $y > x$ with $G(y) = 1$. Then "$G$ is infinite" is the $\Pi^0_2$ sentence $\forall x\ \Phi^G_a(x)\converge$, and "$G$ is finite" is its negation $\exists x\ \Phi^G_a(x)\diverge$.
3. "$\Phi^G_e$ is total" is the $\Pi^0_2$ sentence $\forall x\ \Phi^G_e(x)\converge$.
4. Formulas may also be built with functionals of an oracle $Z \oplus G$ for a fixed set $Z$; everything in this course relativizes to such formulas. The later courses of the track work with these formulas throughout, writing for instance "$\Phi^{Z \oplus G}_e(x)\converge = v$" for the $\Sigma^0_1$ sentence expressing that the computation converges with value $v$.
:::

## Exercises

::::exercise{difficulty=1}
Show that for computable Sacks forcing, for every countable family of sets $(A_k)$, every sufficiently generic set differs from every $A_k$. Show that this fails for Jockusch–Soare forcing.

:::solution
Given a computable f-tree $T$ and a set $A$, the nodes $T(0)$ and $T(1)$ are incompatible, so one of them, $T(i)$, is not a prefix of $A$. The full subtree above $T(i)$ is an extension whose paths all differ from $A$. So the set of conditions all of whose members differ from $A_k$ is dense, for each $k$. For Jockusch–Soare forcing, take for $(A_k)$ the computable sets. For every countable family $\mathcal D$ of dense sets, :ref{#lem-rasiowa-sikorski} gives a $\mathcal D$-generic filter containing the condition $\{ A_0 \}$, and its generic set is $A_0$. So no family $\mathcal D$ makes all $\mathcal D$-generic sets differ from every $A_k$.
:::
::::

## Notes and references

The phrase "sufficiently generic" is standard; see Jockusch (1980) for Cohen forcing and Dzhafarov and Mummert (Section 7.3) in general. Effective forms of the existence of generic filters are given by Hirschfeldt (Section 2.3, Proposition 2.7) and by Dzhafarov and Mummert (Theorem 7.5.6, existence of effective generics); the low basis theorem is due to Jockusch and Soare (1972). The examples are taken from the courses on Cohen genericity, on $\Pi^0_1$ classes and on immunity and growth, where they are proved without forcing vocabulary; Monin and Patey, chapter *Effective forcing*, section *Fundamentals of forcing*, present them in the same way.

- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 2.3.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 7.3 and 7.5.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Fundamentals of forcing*.
