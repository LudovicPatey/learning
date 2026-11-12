---
title: Classifying index sets
summary: Upper bounds by counting quantifiers, lower bounds by reductions; Fin is Σ⁰₂-complete, Tot and Inf are Π⁰₂-complete.
duration: 25
prerequisites: [post-theorem, fundamentals/rice-theorem]
---

Rice's theorem says that no non-trivial index set is computable. The arithmetic hierarchy measures how far from computable they are. To **classify** a set is to find the level of the hierarchy at which it is complete. This involves two steps: an upper bound, obtained by writing a definition and counting quantifiers, and a lower bound, obtained by reducing a complete set of that level to it. This lesson presents the method and classifies the basic index sets of the first two levels; the next lesson treats the third level. By Post's theorem, the classification also determines the Turing degrees of these sets.

## The method

If $A$ is $\Sigma^0_n$-complete, then by :ref{#thm-post}, $A \equiv_m \emptyset^{(n)}$, so $A \equiv_T \emptyset^{(n)}$, and $A$ is not $\Pi^0_n$ (:ref{#cor-hierarchy-strict}). Hence to show that a set $B$ is $\Sigma^0_n$-complete, it suffices to show that $B$ is $\Sigma^0_n$ and that $A \leq_m B$ for some $\Sigma^0_n$-complete set $A$, or directly that every $\Sigma^0_n$ set reduces to $B$. Reductions are built with the SMN theorem, in the parameter form (:ref{#cor-smn-parameters}): from $x$, one computes an index of a c.e. set or partial computable function whose behavior encodes the membership of $x$ in the given set.

The lower bound is the part that requires an idea. A $\Sigma^0_n$ definition of $A$ is a statement about $x$ with $n$ alternating quantifiers; the reduction must turn it into a property of a single c.e. set $V_x$, built uniformly in $x$, such as "$V_x$ is finite". The outer quantifiers of the definition are matched with the quantifiers hidden in that property: "$W_e$ is finite" is $\exists n\ \forall x > n\ \forall s$, so at level $2$ the witness $y$ of $\exists y\ \forall z$ must become a bound beyond which $V_x$ stops growing. At level $3$, in the next lesson, the reduction is no longer a direct translation of the definition: $V_x$ is built by a construction in stages.

## The second level

:::theorem{#thm-fin-complete}
The set $\mathrm{Fin} = \{ e : W_e \text{ is finite} \}$ is $\Sigma^0_2$-complete, and $\mathrm{Inf} = \nat \setminus \mathrm{Fin}$ is $\Pi^0_2$-complete.
:::

:::proof{of=thm-fin-complete}
The set $V_x$ below grows as long as no candidate witness $y$ has been found that survives all tests $z$: it contains $n$ as soon as every $y < n$ has failed some test. A true witness $y_0$ never fails, which caps $V_x$ at $y_0$.

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
$\mathrm{Tot}$ is $\Pi^0_2$ by :ref{#ex-arithmetic-examples}. The reduction lets the universal quantifier $\forall y$ of a $\Pi^0_2$ definition become the universal quantifier "for every input" of totality. Let $A$ be $\Pi^0_2$: $x \in A \iff \forall y\ \exists z\ R(x, y, z)$ with $R$ computable. Let $f$ be computable with $\Phi_{f(x)}(y) \simeq \mu z\ R(x, y, z)$. Then $\Phi_{f(x)}$ is total if and only if every $y$ has a witness $z$, that is, if and only if $x \in A$.
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

## Exercises

::::exercise{difficulty=1}
Show that $\{ e : W_e = \nat \}$ is $\Pi^0_2$-complete, and that $\{ e : W_e \neq \emptyset \}$ is $\Sigma^0_1$-complete.

:::solution
$W_e = \nat \iff \forall x\ \exists s\ \Phi_e(x)[s]\converge$, a $\Pi^0_2$ condition, and $W_e = \mathrm{dom}(\Phi_e)$, so the reduction of :ref{#thm-tot-complete} also reduces every $\Pi^0_2$ set to this set. The set $\{ e : W_e \neq \emptyset \}$ is $\Sigma^0_1$, and $\emptyset'$ reduces to it by :ref{#prop-halting-variants}.
:::
::::

::::exercise{difficulty=1}
Show that $\mathrm{Fin}$ is not $\Pi^0_2$, and deduce again that $\mathrm{Tot}$ is not computable in $\emptyset'$.

:::solution
If $\mathrm{Fin}$ were $\Pi^0_2$, every $\Sigma^0_2$ set, being many-one reducible to $\mathrm{Fin}$, would be $\Pi^0_2$ by :ref{#prop-sigma1-delta1}, contradicting :ref{#cor-hierarchy-strict}. If $\mathrm{Tot}$ were computable in $\emptyset'$, it would be $\Delta^0_2$ by :ref{#thm-post}, hence $\Sigma^0_2$; since every $\Pi^0_2$ set reduces to $\mathrm{Tot}$, every $\Pi^0_2$ set would be $\Sigma^0_2$, and by complementation every $\Sigma^0_2$ set would be $\Pi^0_2$, which was just excluded.
:::
::::

::::exercise{difficulty=1}
Show that the relation $\{ (a, b) : W_a \subseteq W_b \}$ is $\Pi^0_2$-complete, in the sense that the set $\{ \langle a, b \rangle : W_a \subseteq W_b \}$ is.

:::solution
It is $\Pi^0_2$ by :ref{#ex-inclusion-pi2}. Fix an index $c$ with $W_c = \nat$. Then $W_e = \nat \iff W_c \subseteq W_e$, so $e \mapsto \langle c, e \rangle$ reduces $\{ e : W_e = \nat \}$, which is $\Pi^0_2$-complete by the first exercise, to the set.
:::
::::

::::exercise{difficulty=2}
Show that the set $\{ e : \Phi_e \text{ is total and constant} \}$ is $\Pi^0_2$-complete.

:::solution
$\Phi_e$ is total and constant if and only if $\Phi_e$ is total and $\forall x\ \forall y\ \forall s\ \big( \Phi_e(x)[s]\converge \wedge \Phi_e(y)[s]\converge \to \Phi_e(x)[s] = \Phi_e(y)[s] \big)$; this is the conjunction of a $\Pi^0_2$ and a $\Pi^0_1$ condition, hence $\Pi^0_2$. For completeness, let $A = \{ x : \forall y\ \exists z\ R(x, y, z) \}$ with $R$ computable, and let $f$ be computable with $\Phi_{f(x)}(y) \simeq 0$ if $\exists z\ R(x, y, z)$, the program searching for $z$ and diverging if there is none. Then $\Phi_{f(x)}$ is defined exactly on the $y$ that have a witness, and takes the value $0$ there; it is total and constant if and only if $x \in A$.
:::
::::

## Notes and references

The classification of $\mathrm{Fin}$, $\mathrm{Inf}$ and $\mathrm{Tot}$ is standard. Soare's *Turing Computability* proves it in Section 4.3.1 (Theorem 4.3.2), by a single reduction that sends $\Pi^0_2$ instances to indices of $\nat$ and $\Sigma^0_2$ instances to indices of finite sets; Downey and Hirschfeldt state it as Theorem 2.6.5, and Nies lists it in Exercise 1.4.20.

- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 4.3.1.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.6.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.4.
