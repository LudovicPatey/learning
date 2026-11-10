---
title: Classifying index sets
summary: Upper bounds by counting quantifiers, lower bounds by reductions; Fin is Σ⁰₂-complete, Tot and Inf are Π⁰₂-complete, Cof is Σ⁰₃-complete.
duration: 45
prerequisites: [post-theorem, fundamentals/rice-theorem]
---

Rice's theorem says that no non-trivial index set is computable. The arithmetic hierarchy measures how far from computable they are. To **classify** a set is to find the level of the hierarchy at which it is complete. This involves two steps: an upper bound, obtained by writing a definition and counting quantifiers, and a lower bound, obtained by reducing a complete set of that level to it. This lesson classifies the basic index sets; by Post's theorem, the classification also determines their Turing degrees.

## The method

If $A$ is $\Sigma^0_n$-complete, then by :ref{#thm-post}, $A \equiv_m \emptyset^{(n)}$, so $A \equiv_T \emptyset^{(n)}$, and $A$ is not $\Pi^0_n$ (:ref{#cor-hierarchy-strict}). Hence to show that a set $B$ is $\Sigma^0_n$-complete, it suffices to show that $B$ is $\Sigma^0_n$ and that $A \leq_m B$ for some $\Sigma^0_n$-complete set $A$, or directly that every $\Sigma^0_n$ set reduces to $B$. Reductions are built with the SMN theorem, in the parameter form (:ref{#cor-smn-parameters}): from $x$, one computes an index of a c.e. set or partial computable function whose behavior encodes the membership of $x$ in the given set.

## The second level

:::theorem{#thm-fin-complete}
The set $\mathrm{Fin} = \{ e : W_e \text{ is finite} \}$ is $\Sigma^0_2$-complete, and $\mathrm{Inf} = \nat \setminus \mathrm{Fin}$ is $\Pi^0_2$-complete.
:::

:::proof{of=thm-fin-complete}
$\mathrm{Fin}$ is $\Sigma^0_2$ by :ref{#ex-arithmetic-examples}. Let $A$ be $\Sigma^0_2$: $x \in A \iff \exists y\ \forall z\ R(x, y, z)$ with $R$ computable. Consider the sets
$$
V_x = \{ n : \forall y < n\ \ \exists z\ \neg R(x, y, z) \}.
$$
The relation $n \in V_x$ is c.e., by closure under bounded quantification, so there is a computable $f$ with $W_{f(x)} = V_x$ for every $x$. If $x \notin A$, every $y$ has a $z$ with $\neg R(x, y, z)$, so $V_x = \nat$ is infinite. If $x \in A$, let $y_0$ be such that $\forall z\ R(x, y_0, z)$; then no $n > y_0$ belongs to $V_x$, so $V_x$ is finite. Hence $x \in A \iff f(x) \in \mathrm{Fin}$. The statement on $\mathrm{Inf}$ follows by complementation.
:::

:::theorem{#thm-tot-complete}
The set $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$ is $\Pi^0_2$-complete.
:::

:::proof{of=thm-tot-complete}
$\mathrm{Tot}$ is $\Pi^0_2$ by :ref{#ex-arithmetic-examples}. Let $A$ be $\Pi^0_2$: $x \in A \iff \forall y\ \exists z\ R(x, y, z)$ with $R$ computable. Let $f$ be computable with $\Phi_{f(x)}(y) \simeq \mu z\ R(x, y, z)$. Then $\Phi_{f(x)}$ is total if and only if every $y$ has a witness $z$, that is, if and only if $x \in A$.
:::

So $\mathrm{Fin}$, $\mathrm{Inf}$ and $\mathrm{Tot}$ are Turing equivalent to $\emptyset''$, as announced in :ref{#prop-tot-double-jump}. None of them is computable in $\emptyset'$.

:::quiz[the second level]
In the proof of :ref{#thm-fin-complete}, why is $V_x$ finite when $x \in A$?

- [x] A witness $y_0$ with $\forall z\ R(x, y_0, z)$ blocks every $n > y_0$, since the condition $\forall y < n\ \exists z\ \neg R(x, y, z)$ fails at $y = y_0$.
- [ ] Because $R$ is computable.

  Computability of $R$ makes $V_x$ c.e.; finiteness comes from the witness $y_0$.
- [ ] Because $V_x$ is a subset of $\{ 0, \dots, x \}$.

  No such bound holds in general; the bound is $y_0$.

---

Why is the search $\mu z\ R(x, y, z)$ in the proof of :ref{#thm-tot-complete} enough to reduce a $\Pi^0_2$ set to $\mathrm{Tot}$?

- [x] Because $\Phi_{f(x)}(y)$ converges exactly when $y$ has a witness, so totality expresses the universal quantifier over $y$.
- [ ] Because the search always terminates.

  It terminates only if a witness exists; this is what makes totality informative.
- [ ] Because $\mathrm{Tot}$ is $\Sigma^0_2$.

  $\mathrm{Tot}$ is $\Pi^0_2$, and not $\Sigma^0_2$.
:::

## The third level

:::theorem{#thm-cof-complete}
The set $\mathrm{Cof} = \{ e : W_e \text{ is cofinite} \}$ is $\Sigma^0_3$-complete.
:::

:::proof{of=thm-cof-complete}
$\mathrm{Cof}$ is $\Sigma^0_3$ by :ref{#ex-arithmetic-examples}. Let $A$ be $\Sigma^0_3$: $x \in A \iff \exists n\ P(x, n)$ with $P$ a $\Pi^0_2$ relation. By :ref{#thm-fin-complete}, $\mathrm{Inf}$ is $\Pi^0_2$-complete, so there is a computable $g$ with $P(x, n) \iff W_{g(x, n)}$ is infinite. We build, uniformly in $x$, a c.e. set $V_x$ which is cofinite if and only if some $W_{g(x, n)}$ is infinite.

*Construction.* We enumerate $V_x$ by stages, starting with $V_x[0] = \emptyset$. At stage $s + 1$, let $n$ be the least $n \leq s$ such that $W_{g(x, n)}[s + 1] \neq W_{g(x, n)}[s]$, if there is one; we say that $n$ **acts** at stage $s + 1$. In that case, list the elements of $\{0, \dots, s - 1\} \setminus V_x[s]$ in increasing order, and enumerate into $V_x$ all of them except the first $n$. If no $n \leq s$ acts, do nothing. The construction is computable uniformly in $x$, so there is a computable $h$ with $W_{h(x)} = V_x$.

The numbers not in $V_x$ at stage $s$, in increasing order, are called the **markers** at stage $s$. A stage at which $n$ acts keeps the first $n$ markers below $s$ and removes the others.

*If some $W_{g(x, n)}$ is infinite, $V_x$ is cofinite.* Fix such an $n$. Then $W_{g(x, n)}$ receives new elements at infinitely many stages, and at each of them some $n' \leq n$ acts. Suppose $m_0 < m_1 < \dots < m_n$ are $n + 1$ numbers outside $V_x$. Take a stage $s + 1$ with $s > m_n$ at which some $n' \leq n$ acts. The numbers $m_0, \dots, m_n$ are all below $s$ and outside $V_x[s]$, and $m_n$ is not among the first $n$ markers below $s$, since $m_0, \dots, m_{n-1}$ precede it. So $m_n$ is enumerated into $V_x$, a contradiction. Hence the complement of $V_x$ has at most $n$ elements.

*If every $W_{g(x, n)}$ is finite, $V_x$ is coinfinite.* We show that for every $k$, the $k$-th marker (counting from $0$) eventually reaches a final value. Only actions of some $n \leq k$ remove the $k$-th marker or a smaller one, since an action of $n$ keeps the first $n$ markers. Each $n \leq k$ acts only finitely often, since $W_{g(x, n)}$ is finite. After the last action of the numbers $n \leq k$, the first $k + 1$ markers are never removed: they are final. So the complement of $V_x$ contains the final values of all markers, and is infinite.

Hence $x \in A \iff h(x) \in \mathrm{Cof}$.
:::

The construction is a first example of a **marker argument**: each $n$ may, when it acts, destroy all markers beyond the $n$-th one. An $n$ that acts infinitely often eventually destroys all markers beyond the $n$-th; if every $n$ acts finitely often, each marker settles. Arguments of this kind, with priorities between the actors, are the subject of the course on Post's problem.

:::quiz[the marker argument]
Why does an action of $n$ keep the first $n$ markers instead of removing all of them?

- [x] So that the marker of rank $k$ can only be removed by actions of the finitely many $n \leq k$, which is what makes every marker settle when all the sets $W_{g(x, n)}$ are finite.

  Infinitely many different $n$ may act, each finitely often. If every action removed all markers, the markers would be disturbed infinitely often even when every $W_{g(x, n)}$ is finite, and $V_x$ could be cofinite in that case.
- [ ] To make $V_x$ c.e.

  $V_x$ is c.e. however the markers are handled.
- [ ] Because the first $n$ markers belong to $W_{g(x, n)}$.

  Markers are numbers outside $V_x$; they are unrelated to the elements of $W_{g(x, n)}$.

---

Why is the least acting $n$ chosen at each stage?

- [x] So that, at every stage where $W_{g(x, n)}$ receives a new element, the action keeps at most $n$ markers.

  The acting number $n'$ is then at most $n$; with another choice, a larger number could act at that stage and keep more markers.
- [ ] To make the construction terminate.

  Each stage is finite in any case.
- [ ] Because $W_{g(x, 0)}$ is always infinite.

  Nothing is assumed about $W_{g(x, 0)}$; any of the sets may be finite or infinite.
:::

## Summary

The following table collects the classification of the basic index sets. The sets marked as admitted are classified in the references; the others are classified in this lesson or its exercises.

| Set | Definition | Complete for |
| --- | --- | --- |
| $\emptyset'$, $\{ e : W_e \neq \emptyset \}$ | $\Phi_e(e)\converge$; $\exists x\ x \in W_e$ | $\Sigma^0_1$ |
| $\{ e : W_e = \emptyset \}$ | $\forall x\ x \notin W_e$ | $\Pi^0_1$ |
| $\mathrm{Fin}$ | $\exists n\ \forall x > n\ \ x \notin W_e$ | $\Sigma^0_2$ |
| $\mathrm{Inf}$, $\mathrm{Tot}$, $\{ e : W_e = \nat \}$ | $\forall n\ \exists x > n\ \ x \in W_e$; $\forall x\ \Phi_e(x)\converge$ | $\Pi^0_2$ |
| $\mathrm{Cof}$ | $\exists n\ \forall x > n\ \ x \in W_e$ | $\Sigma^0_3$ |
| $\mathrm{Rec} = \{ e : W_e \text{ computable} \}$ (admitted) | see :ref{to="arithmetic-hierarchy/sigma-pi-sets"} | $\Sigma^0_3$ |

The completeness of $\mathrm{Rec}$ requires a more elaborate construction; a proof is in Soare's book.

## Exercises

::::exercise{difficulty=1}
Show that $\{ e : W_e = \nat \}$ is $\Pi^0_2$-complete, and that $\{ e : W_e \neq \emptyset \}$ is $\Sigma^0_1$-complete.

:::solution
$W_e = \nat \iff \forall x\ \exists s\ \Phi_e(x)[s]\converge$, a $\Pi^0_2$ condition, and $W_e = \mathrm{dom}(\Phi_e)$, so the reduction of :ref{#thm-tot-complete} also reduces every $\Pi^0_2$ set to this set. The set $\{ e : W_e \neq \emptyset \}$ is $\Sigma^0_1$, and $\emptyset'$ reduces to it by :ref{#prop-halting-variants}.
:::
::::

::::exercise{difficulty=1}
Show that $\mathrm{Cof}$ is not $\Pi^0_3$, and that $\mathrm{Fin}$ is not $\Pi^0_2$.

:::solution
If $\mathrm{Cof}$ were $\Pi^0_3$, every $\Sigma^0_3$ set, being many-one reducible to $\mathrm{Cof}$, would be $\Pi^0_3$ by :ref{#prop-sigma1-delta1}, contradicting :ref{#cor-hierarchy-strict}. The same argument applies to $\mathrm{Fin}$ at level $2$.
:::
::::

::::exercise{difficulty=2}
Show that the set $\{ e : \Phi_e \text{ is total and constant} \}$ is $\Pi^0_2$-complete.

:::solution
$\Phi_e$ is total and constant if and only if $\Phi_e$ is total and $\forall x\ \forall y\ \forall s\ \big( \Phi_e(x)[s]\converge \wedge \Phi_e(y)[s]\converge \to \Phi_e(x)[s] = \Phi_e(y)[s] \big)$; this is the conjunction of a $\Pi^0_2$ and a $\Pi^0_1$ condition, hence $\Pi^0_2$. For completeness, let $A = \{ x : \forall y\ \exists z\ R(x, y, z) \}$ with $R$ computable, and let $f$ be computable with $\Phi_{f(x)}(y) \simeq 0$ if $\exists z\ R(x, y, z)$, the program searching for $z$ and diverging if there is none. Then $\Phi_{f(x)}$ is defined exactly on the $y$ that have a witness, and takes the value $0$ there; it is total and constant if and only if $x \in A$.
:::
::::

## Notes and references

The classification of the index sets of this lesson is presented in Rogers' and Soare's books. Marker arguments, of which the proof for $\mathrm{Cof}$ is a simple instance, are a basic tool in the study of c.e. sets.

- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
