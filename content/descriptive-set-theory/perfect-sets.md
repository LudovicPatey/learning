---
title: Countable Σ¹₁ classes
summary: Σ¹₁ singletons are hyperarithmetic; the class of hyperarithmetic sets is Π¹₁; by the effective perfect set theorem, a Σ¹₁ class with a non-hyperarithmetic member contains a perfect closed subclass, so countable Σ¹₁ classes consist of hyperarithmetic sets.
duration: 30
prerequisites: [norms, hyperarithmetic/sigma11-classes]
---

Classical descriptive set theory proves that an analytic subset of the reals is either countable or contains a perfect closed subset, hence has the cardinality of the continuum: analytic sets satisfy the continuum hypothesis. The effective version, due to Harrison, identifies the countable $\Sigma^1_1$ classes: their members are all hyperarithmetic. A $\Sigma^1_1$ class with at least one non-hyperarithmetic member has continuum many members.

## Σ¹₁ singletons

Recall that a class $\mathcal A \subseteq \cs$ is $\Sigma^1_1$ if it is defined by a formula $\exists Y\, \varphi(X, Y)$ with $\varphi$ arithmetic, possibly with number parameters (:ref{#def-sigma11-class}), and that it is then the projection of the set of paths of a computable tree $S$ of pairs: $X \in \mathcal A$ if and only if $(X, f)$ is a path of $S$ for some $f \in \nat^\nat$.

:::proposition{#prop-sigma11-singleton}
1. If $\{ X \}$ is a $\Sigma^1_1$ class, then $X$ is hyperarithmetic.
2. The class $\mathrm{HYP}$ of hyperarithmetic sets is $\Pi^1_1$.
:::

:::proof{of=prop-sigma11-singleton}
1. Let $\{ X \} = \{ Z : \exists Y\, \varphi(Z, Y) \}$. Then $n \in X$ if and only if $\exists Z\, \exists Y\, (\varphi(Z, Y) \wedge n \in Z)$, a $\Sigma^1_1$ condition, and if and only if $\forall Z\, \forall Y\, (\varphi(Z, Y) \rightarrow n \in Z)$, a $\Pi^1_1$ condition, since $X$ is the only $Z$ with a witness $Y$. So $X$ is $\Delta^1_1$, hence hyperarithmetic by :ref{#thm-kleene-delta11}.
2. This is the second exercise of :ref{to="hyperarithmetic/kleene-theorem"}: $X$ is hyperarithmetic if and only if there are $a$ and $e$ with $a \in \mathcal O$ and, for every $Y$ that is an H-sequence along $a$, $X = \Phi^{Y^{[a]}}_e$. By :ref{#lem-h-sequence-unique}, this expresses $X \leq_T H_a$, and the formula is $\Pi^1_1$.
:::

In particular, the class of non-hyperarithmetic sets is $\Sigma^1_1$. By contrast, there are $\Pi^1_1$ singletons that are not hyperarithmetic; $\mathcal O$ is one of them. We admit this fact (Sacks, *Higher Recursion Theory*, Section I.1).

## The effective perfect set theorem

Recall that a class $\mathcal P \subseteq \cs$ is **perfect** if it is non-empty, closed and has no isolated member (:ref{#def-isolated}). A perfect class has the cardinality of the continuum (:ref{#thm-perfect-continuum}); in the proof below, this is seen directly, since the perfect class is the image of an injective continuous map from $\cs$.

:::theorem[Harrison]{#thm-effective-perfect-set}
If a $\Sigma^1_1$ class $\mathcal A$ has a member that is not hyperarithmetic, then $\mathcal A$ contains a non-empty perfect closed class. In particular, $\mathcal A$ has the cardinality of the continuum.
:::

:::proof{of=thm-effective-perfect-set}
Let $\mathcal B = \mathcal A \setminus \mathrm{HYP}$. It is a non-empty $\Sigma^1_1$ class, by :ref{#prop-sigma11-singleton}, and the projection of the paths of a computable tree $S$ of pairs $u = (\sigma, \tau) \in 2^{<\nat} \times \nat^{<\nat}$ with $|\sigma| = |\tau|$. For such a pair, let $\mathcal B_u$ be the class of sets $X$ such that $(X, f)$ is a path of $S$ extending $u$ for some $f$; it is a $\Sigma^1_1$ class, with the finite object $u$ as a parameter, included in $\mathcal B$. Call $u$ **good** if $\mathcal B_u$ is non-empty. A good pair belongs to $S$, and the empty pair is good.

*Splitting.* Let $u$ be good. The class $\mathcal B_u$ is $\Sigma^1_1$ and contains only non-hyperarithmetic sets, so by :ref{#prop-sigma11-singleton} (1) it is not a singleton: it contains $X \neq X'$, with witnesses $f$ and $f'$. Let $k$ be such that $X(k) \neq X'(k)$, and $m > \max(k, |u|)$. Then $u_0 = (X \uh m, f \uh m)$ and $u_1 = (X' \uh m, f' \uh m)$ are good, extend $u$, and their first components are incompatible.

*Construction.* Define good pairs $u_s$ for $s \in 2^{<\nat}$ by $u_\emptyset = (\emptyset, \emptyset)$, and, given $u_s$, let $u_{s0}$ and $u_{s1}$ be the two pairs given by the splitting step. For $Z \in \cs$, the pairs $u_{Z \uh n}$ are increasing, and their lengths increase strictly, so they converge to a pair $(X_Z, f_Z)$. Every prefix of $(X_Z, f_Z)$ is a prefix of a good pair, hence belongs to the tree $S$; so $(X_Z, f_Z)$ is a path of $S$, and $X_Z \in \mathcal B \subseteq \mathcal A$.

*The image is perfect.* If $Z \neq Z'$, let $s$ be their longest common prefix; then $X_Z$ and $X_{Z'}$ extend the first components of $u_{s0}$ and $u_{s1}$, which are incompatible, so $X_Z \neq X_{Z'}$. The map $Z \mapsto X_Z$ is continuous, since $X_Z \uh n$ only depends on $Z \uh n$, because the first component of $u_{Z \uh n}$ has length at least $n$. Its image $\mathcal P$ is therefore compact, hence closed. It has no isolated point: for $Z \in \cs$ and $n \in \nat$, let $Z'$ differ from $Z$ only at position $n$; then $X_{Z'} \neq X_Z$, and both extend the first component of $u_{Z \uh n}$, of length at least $n$. So $\mathcal P$ is a non-empty perfect closed subclass of $\mathcal A$, in bijection with $\cs$.
:::

:::corollary{#cor-countable-sigma11}
1. Every member of a countable $\Sigma^1_1$ class is hyperarithmetic.
2. If a computable tree $T \subseteq \nat^{<\nat}$ has countably many paths, they are all hyperarithmetic. A computable tree with a path but no hyperarithmetic path, as in :ref{#thm-no-hyp-path}, has continuum many paths.
:::

:::proof{of=cor-countable-sigma11}
1. This is the contrapositive of :ref{#thm-effective-perfect-set}.
2. The class of graphs of the paths of $T$ is arithmetic, hence $\Sigma^1_1$, and in bijection with the set of paths; a path is hyperarithmetic if and only if its graph is. Item 1 gives the first statement. For the second, the class of graphs has a non-hyperarithmetic member, so it has the cardinality of the continuum by :ref{#thm-effective-perfect-set}.
:::

The construction is not effective: choosing good pairs requires deciding a $\Sigma^1_1$ property. It can be carried out with the oracle $\mathcal O$: the set of good pairs is $\Sigma^1_1$, so its complement is many-one reducible to $\mathcal O$, and choosing at each step the first suitable pairs $u_{s0}, u_{s1}$ in a fixed enumeration makes the map $Z \mapsto X_Z$ computable in $\mathcal O$. Since $\Pi^0_1$ classes are $\Sigma^1_1$, the corollary applies to them: all members of a countable $\Pi^0_1$ class are hyperarithmetic. This complements :ref{#cor-countable-computable}, which only gives a computable member.

:::quiz[the perfect set theorem]
In the splitting step of :ref{#thm-effective-perfect-set}, why does $\mathcal B_u$ have at least two members?

- [x] Because it is a non-empty $\Sigma^1_1$ class of non-hyperarithmetic sets, and a $\Sigma^1_1$ class with exactly one member has a hyperarithmetic member.
- [ ] Because $\mathcal B$ is uncountable.

  This is the conclusion of the theorem, not a hypothesis.
- [ ] Because $S$ is infinitely branching.

  Two different paths may project to the same set; the splitting must happen in the first component, which is ensured by the singleton argument.

---

Why is the class $\mathcal A \setminus \mathrm{HYP}$ used, rather than $\mathcal A$ itself?

- [x] So that every non-empty $\Sigma^1_1$ subclass built in the construction avoids hyperarithmetic sets, and therefore splits; $\mathcal A$ may have isolated hyperarithmetic members.
- [ ] Because $\mathcal A$ is not $\Sigma^1_1$.

  $\mathcal A$ is $\Sigma^1_1$ by hypothesis.
- [ ] To make the construction effective.

  The construction is not effective in either case.
:::

## Exercises

::::exercise{difficulty=1}
Show that a $\Sigma^1_1$ class is countable if and only if all its members are hyperarithmetic. Let $S_e$ be the computable tree of pairs with index $e$, and $\mathcal A_e$ the projection of its paths. Show that $\{ e : \mathcal A_e \text{ is countable} \}$ is $\Pi^1_1$.

:::solution
The class $\mathrm{HYP}$ is countable (:ref{#prop-hyp-ideal}), since every hyperarithmetic set is computable in some $H_a$ by some functional. With :ref{#cor-countable-sigma11}, a $\Sigma^1_1$ class is countable if and only if it is included in $\mathrm{HYP}$. So, for an index $e$ of a tree of pairs, $\mathcal A_e$ is countable if and only if $\forall X\, \forall f\, ((X, f) \text{ is a path of } S_e \rightarrow X \in \mathrm{HYP})$. Being an index of a computable tree of pairs and being a path are arithmetic, and $X \in \mathrm{HYP}$ is $\Pi^1_1$ by :ref{#prop-sigma11-singleton}, so the whole formula is $\Pi^1_1$.
:::
::::

::::exercise{difficulty=2}
Show that the class of sets that are not hyperarithmetic contains a perfect closed class, and deduce that there are continuum many sets $X$ such that $X$ is not hyperarithmetic.

:::solution
By :ref{#prop-sigma11-singleton}, the class $\cs \setminus \mathrm{HYP}$ is $\Sigma^1_1$, and it is non-empty, since $\mathrm{HYP}$ is countable. By :ref{#thm-effective-perfect-set}, it contains a non-empty perfect closed class, which is in bijection with $\cs$ by the proof of the theorem.
:::
::::

## Notes and references

The perfect set theorem for analytic sets is due to Suslin (1917). Its effective form, with the characterization of the countable $\Sigma^1_1$ classes, is due to Harrison (1967); Sacks and Kechris gave versions with the Gandy–Harrington topology, which also gives the stronger statement that a $\Sigma^1_1$ class with a non-hyperarithmetic member has a perfect subclass of sets that are hyperarithmetically incomparable.

- J. Harrison, *Some applications of recursive pseudo-well-orderings*, PhD thesis, Stanford University, 1967.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Chapter III.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Section 29.
