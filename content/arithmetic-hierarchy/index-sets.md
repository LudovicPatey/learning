---
title: Classifying index sets
summary: Upper bounds by counting quantifiers, lower bounds by reductions; Fin is Σ⁰₂-complete, Tot and Inf are Π⁰₂-complete.
duration: 20
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

::::exercise{#ex-wnat-complete difficulty=1 objective="Adapt the reductions of the lesson to the index sets of $\nat$ and of the nonempty c.e. sets."}
Show that $\{ e : W_e = \nat \}$ is $\Pi^0_2$-complete, and that $\{ e : W_e \neq \emptyset \}$ is $\Sigma^0_1$-complete.

:::solution
$W_e = \nat \iff \forall x\ \exists s\ \Phi_e(x)[s]\converge$, a $\Pi^0_2$ condition, and $W_e = \mathrm{dom}(\Phi_e)$, so the reduction of :ref{#thm-tot-complete} also reduces every $\Pi^0_2$ set to this set. The set $\{ e : W_e \neq \emptyset \}$ is $\Sigma^0_1$, and $\emptyset'$ reduces to it by :ref{#prop-halting-variants}.
:::
::::

::::exercise{#ex-total-constant difficulty=2 objective="Combine an upper bound by quantifier counting with a reduction by SMN for an index set of total functions."}
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

:::::exercises
::::exercise{#ex-fin-not-pi2 difficulty=1 objective="Deduce non-membership in a level from completeness at the dual level."}
Show that $\mathrm{Fin}$ is not $\Pi^0_2$, and deduce again that $\mathrm{Tot}$ is not computable in $\emptyset'$.

:::solution
If $\mathrm{Fin}$ were $\Pi^0_2$, every $\Sigma^0_2$ set, being many-one reducible to $\mathrm{Fin}$, would be $\Pi^0_2$ by :ref{#prop-sigma1-delta1}, contradicting :ref{#cor-hierarchy-strict}. If $\mathrm{Tot}$ were computable in $\emptyset'$, it would be $\Delta^0_2$ by :ref{#thm-post}, hence $\Sigma^0_2$; since every $\Pi^0_2$ set reduces to $\mathrm{Tot}$, every $\Pi^0_2$ set would be $\Sigma^0_2$, and by complementation every $\Sigma^0_2$ set would be $\Pi^0_2$, which was just excluded.
:::
::::

::::exercise{#ex-inclusion-complete difficulty=1 objective="Obtain a completeness result for a relation by fixing one of its arguments."}
Show that the relation $\{ (a, b) : W_a \subseteq W_b \}$ is $\Pi^0_2$-complete, in the sense that the set $\{ \langle a, b \rangle : W_a \subseteq W_b \}$ is.

:::solution
It is $\Pi^0_2$ by :ref{#ex-inclusion-pi2}. Fix an index $c$ with $W_c = \nat$. Then $W_e = \nat \iff W_c \subseteq W_e$, so $e \mapsto \langle c, e \rangle$ reduces $\{ e : W_e = \nat \}$, which is $\Pi^0_2$-complete by :ref{#ex-wnat-complete}, to the set.
:::
::::

::::exercise{#ex-inf-tot-direct difficulty=1 objective="Build direct many-one reductions between Inf and Tot with SMN."}
Show directly, without the classification of the lesson, that $\mathrm{Inf} \leq_m \mathrm{Tot}$ and $\mathrm{Tot} \leq_m \mathrm{Inf}$.

:::solution
By :ref{#cor-smn-parameters}, there is a computable $f$ such that $\Phi_{f(e)}(n)$ searches for $x > n$ and $s$ with $\Phi_e(x)[s]\converge$, and outputs $0$ when it finds them; it diverges if there are none. Then $\Phi_{f(e)}$ is total if and only if for every $n$ there is an element of $W_e$ larger than $n$, that is, if and only if $W_e$ is infinite.

Conversely, the relation $\{ (e, n) : \forall m \leq n\ \Phi_e(m)\converge \}$ is c.e., by bounded universal quantification (:ref{#prop-ce-closure}), so there is a computable $g$ with $W_{g(e)} = \{ n : \forall m \leq n\ \Phi_e(m)\converge \}$. If $\Phi_e$ is total, $W_{g(e)} = \nat$. If $\Phi_e(m)\diverge$, then $W_{g(e)} \subseteq \{ 0, \dots, m - 1 \}$ is finite. So $e \in \mathrm{Tot} \iff g(e) \in \mathrm{Inf}$.
:::
::::

::::exercise{#ex-ran-infinite difficulty=1 objective="Transfer a completeness result from domains to ranges by a reduction."}
Show that $\{ e : \text{the range of } \Phi_e \text{ is infinite} \}$ is $\Pi^0_2$-complete.

:::solution
The set is $\Pi^0_2$ by :ref{#ex-place-sets}. By :ref{#cor-smn-parameters}, there is a computable $f$ such that $\Phi_{f(e)}(x)$ waits until $x$ is enumerated into $W_e$ and then outputs $x$; it diverges if $x \notin W_e$. The range of $\Phi_{f(e)}$ is $W_e$, so $e \in \mathrm{Inf} \iff f(e)$ belongs to the set. Since $\mathrm{Inf}$ is $\Pi^0_2$-complete (:ref{#thm-fin-complete}), so is the set.
:::
::::

::::exercise[One reduction for the second level]{#ex-separating-reduction difficulty=2 objective="Build one reduction that sends a $\Pi^0_2$ set to indices of $\nat$ and its complement to indices of finite sets, and use it to classify several index sets at once."}
1. Show that for every $\Pi^0_2$ set $A$ there is a computable $f$ such that $W_{f(x)} = \nat$ if $x \in A$, and $W_{f(x)}$ is finite if $x \notin A$.
2. Let $B$ be a set of indices that contains every index of $\nat$ and no index of a finite set. Show that every $\Pi^0_2$ set is many-one reducible to $B$.
3. Deduce that $\{ e : W_e \text{ contains every even number} \}$ is $\Pi^0_2$-complete, and that $\mathrm{Fin}$, $\mathrm{Inf}$ and $\{ e : W_e = \nat \}$ are complete at their levels.

:::solution
1. Write $x \in A \iff \forall y\ \exists z\ R(x, y, z)$ with $R$ computable, and let $f$ be computable with $W_{f(x)} = \{ n : \forall y < n\ \exists z\ R(x, y, z) \}$; the relation is c.e. by bounded quantification. If $x \in A$, every $n$ satisfies the condition, and $W_{f(x)} = \nat$. If $x \notin A$, some $y_0$ has no witness $z$, and no $n > y_0$ satisfies the condition, so $W_{f(x)} \subseteq \{ 0, \dots, y_0 \}$.
2. With $f$ as in item 1, $x \in A$ implies $W_{f(x)} = \nat$, so $f(x) \in B$, and $x \notin A$ implies that $W_{f(x)}$ is finite, so $f(x) \notin B$. Hence $f$ reduces $A$ to $B$.
3. The set $E = \{ e : \forall m\ \exists s\ \Phi_e(2m)[s]\converge \}$ is $\Pi^0_2$, and it contains every index of $\nat$ and no index of a finite set, so it is $\Pi^0_2$-complete by item 2. The same holds for $\mathrm{Inf}$ and for $\{ e : W_e = \nat \}$, which are $\Pi^0_2$. For $\mathrm{Fin}$, the same $f$ reduces the complement of any $\Pi^0_2$ set, that is, any $\Sigma^0_2$ set, to $\mathrm{Fin}$.

This is the form in which Soare (2016, Theorem 4.3.2) proves the classification. The function $f$ is the reduction of the proof of :ref{#thm-fin-complete}, applied to the complement of $A$.
:::
::::

::::exercise{#ex-singleton-index difficulty=1 objective="Show by two reductions that an index set can be $\Delta^0_2$ without being $\Sigma^0_1$ or $\Pi^0_1$."}
Let $B = \{ e : W_e = \{ 0 \} \}$. Show that $B$ is $\Delta^0_2$, and that it is neither $\Sigma^0_1$ nor $\Pi^0_1$.

:::solution
$e \in B$ if and only if $\exists s\ \Phi_e(0)[s]\converge$ and $\forall x\ \forall s\ (x = 0 \vee \Phi_e(x)[s]\diverge)$: the intersection of a $\Sigma^0_1$ and a $\Pi^0_1$ set, both $\Delta^0_2$, so $B$ is $\Delta^0_2$.

By :ref{#cor-smn-parameters}, there is a computable $f$ such that $\Phi_{f(k)}(0)\converge$, $\Phi_{f(k)}(1)$ converges if and only if $\Phi_k(k)\converge$ (it runs $\Phi_k(k)$), and $\Phi_{f(k)}(x)\diverge$ for $x \geq 2$. Then $W_{f(k)} = \{ 0 \}$ if $k \notin \emptyset'$ and $W_{f(k)} = \{ 0, 1 \}$ if $k \in \emptyset'$, so $f$ reduces $\nat \setminus \emptyset'$ to $B$. If $B$ were $\Sigma^0_1$, the complement of $\emptyset'$ would be $\Sigma^0_1$ (:ref{#prop-sigma1-delta1}), and $\emptyset'$ would be computable.

Similarly, there is a computable $g$ such that $\Phi_{g(k)}(0)$ converges if and only if $\Phi_k(k)\converge$, and $\Phi_{g(k)}(x)\diverge$ for $x \geq 1$. Then $W_{g(k)} = \{ 0 \}$ if $k \in \emptyset'$ and $W_{g(k)} = \emptyset$ otherwise, so $g$ reduces $\emptyset'$ to $B$. If $B$ were $\Pi^0_1$, $\emptyset'$ would be $\Pi^0_1$, hence $\Delta^0_1$, hence computable.
:::
::::

::::exercise{#ex-low-tot difficulty=2 objective="Use Post's theorem relativized to a low oracle to classify a relativized index set at the second level." lessons="post-theorem"}
A set $A$ is low if $A' \leq_T \emptyset'$. Show that if $A$ is low, then $\mathrm{Tot}^A = \{ e : \Phi^A_e \text{ is total} \}$ is $\Pi^0_2$-complete.

:::solution
*Upper bound.* $e \in \mathrm{Tot}^A \iff \forall x\ \exists s\ \Phi^A_e(x)[s]\converge$, so $\mathrm{Tot}^A$ is $\Pi^0_2(A)$, and its complement is $\Sigma^0_2(A)$, that is, $A'$-c.e. by :ref{#thm-post} relativized to $A$. Write the complement as $\mathrm{dom}(\Phi^{A'}_i)$ and $A' = \Phi^{\emptyset'}_j$. The $\emptyset'$-machine that runs $\Phi_i$ and answers each oracle question by computing $\Phi^{\emptyset'}_j$, which is total, has the same domain. So the complement of $\mathrm{Tot}^A$ is $\emptyset'$-c.e., that is, $\Sigma^0_2$ by :ref{#thm-post}, and $\mathrm{Tot}^A$ is $\Pi^0_2$.

*Lower bound.* By the SMN theorem for oracle machines, there is a computable $f$ such that $\Phi^X_{f(e)}(x) \simeq \Phi_e(x)$ for every oracle $X$: the program $f(e)$ ignores its oracle. Then $e \in \mathrm{Tot} \iff f(e) \in \mathrm{Tot}^A$, and $\mathrm{Tot}$ is $\Pi^0_2$-complete (:ref{#thm-tot-complete}).

For $A = \emptyset'$, which is not low, the set $\mathrm{Tot}^{\emptyset'}$ is $\Pi^0_3$-complete, as shown in the next lesson.
:::
::::
:::::
