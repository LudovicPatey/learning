---
title: Partial truth definitions
summary: The partial truth definitions Sat_Σₙ and Sat_Πₙ, obtained from satisfaction for bounded formulas by quantifying over assignments; their complexity and Tarski's conditions in IΣ₁; every Σₙ formula is equivalent in IΣ₁ to an instance of Sat_Σₙ, through formulas whose quantifiers are bounded by variables.
duration: 40
prerequisites: [bounded-satisfaction]
---

The previous lesson defined satisfaction for bounded formulas by a formula $\mathrm{Sat}_0$ that is $\Delta_1$ in $\mathrm I\Sigma_1$. Unbounded quantifiers are now added one block at a time, by quantifying over assignments: a formula $\exists v_i\ \varphi$ is satisfied by $e$ if some assignment that differs from $e$ at most at $v_i$ satisfies $\varphi$. Each block adds one unbounded quantifier to the definition, which is where the complexity $\Sigma_n$ comes from. The consequences, in the next lesson, are the finite axiomatizability of $\mathrm I\Sigma_n$ and the properness of the arithmetic hierarchy in every model of $\mathrm I\Sigma_1$.

## Partial truth definitions

Unbounded quantifiers are evaluated by quantifying over assignments. For a $\Sigma^*_{n+1}$ formula $\exists v_{i_1} \cdots \exists v_{i_k}\ \psi$, satisfaction means that some modification of $e$ at the variables $v_{i_1}, \dots, v_{i_k}$ satisfies $\psi$. Inside a model, $k$ may be non-standard; the block is described by the sequence $d$ of its indices.

:::definition{#def-sat-n}
Let $\mathrm{Sat}_{\Sigma_0} = \mathrm{Sat}_{\Pi_0} = \mathrm{Sat}_0$. For $n \geq 0$, $\mathrm{Sat}_{\Sigma_{n+1}}(z, e)$ is the formula: $z \in \Sigma^*_{n+1}$, and there are $d$, $u$ and $e'$ such that $z$ consists of the maximal block of unbounded existential quantifiers on the variables listed by $d$ followed by the formula $u$, such that $e'(i) = e(i)$ for every $i$ not listed in $d$, and such that $\mathrm{Sat}_{\Pi_n}(u, e')$. The formula $\mathrm{Sat}_{\Pi_{n+1}}(z, e)$ is defined dually: $z \in \Pi^*_{n+1}$ decomposes as a maximal universal block listed by $d$ followed by $u$, and $\mathrm{Sat}_{\Sigma_n}(u, e')$ holds for every $e'$ that agrees with $e$ outside $d$.
:::

The relation between $z$, $d$ and $u$ is $\Delta_1$ in $\mathrm I\Sigma_1$, being defined by course-of-values recursion, and "$e'$ agrees with $e$ outside $d$" quantifies over all $i$; it suffices to quantify over $i$ below $\mathrm{lh}(e) + \mathrm{lh}(e')$, beyond which both values are $0$, so it is bounded.

:::example{#ex-sat-n-even}
Let $\varphi$ be the $\Sigma^*_1$ formula $\exists v_1\ (v_0 = v_1 + v_1)$. Its maximal existential block is $v_1$, so $d$ lists the index $1$, and $u$ is the code of the atomic formula $v_0 = v_1 + v_1$. By definition, $\mathrm{Sat}_{\Sigma_1}(\ulcorner \varphi \urcorner, e)$ holds if and only if some $e'$ that agrees with $e$ except possibly at $1$ satisfies $\mathrm{Sat}_0(u, e')$, that is, $e'(0) = e'(1) + e'(1)$. Since $e'(0) = e(0)$, this says that $e(0)$ is even, the value $e'(1)$ being half of it.
:::

:::theorem[Partial truth definitions]{#thm-sat-n}
For every $n \geq 1$:

1. $\mathrm{Sat}_{\Sigma_n}$ is $\Sigma_n$ in $\mathrm I\Sigma_1$, and $\mathrm{Sat}_{\Pi_n}$ is $\Pi_n$ in $\mathrm I\Sigma_1$;
2. $\mathrm I\Sigma_1$ proves Tarski's conditions for unbounded quantifiers: if $z = \ulcorner \exists v_i\ w \urcorner$ is in $\Sigma^*_n$, then $\mathrm{Sat}_{\Sigma_n}(z, e) \leftrightarrow \exists x\ \mathrm{Sat}_{\Sigma_n}(w, e[i := x])$; if $z \in \Sigma^*_n$ does not begin with an unbounded $\exists$, then $\mathrm{Sat}_{\Sigma_n}(z, e) \leftrightarrow \mathrm{Sat}_{\Pi_{n-1}}(z, e)$; and dually for $\mathrm{Sat}_{\Pi_n}$.
:::

:::proof{of=thm-sat-n}
1. By induction on $n$. For $n = 1$, $\mathrm{Sat}_{\Sigma_1}$ is an existential quantification of a conjunction of $\Delta_1$ formulas, the last one being $\mathrm{Sat}_0$, by :ref{#thm-sat0}; it is $\Sigma_1$. For $n + 1 \geq 2$, it is an existential quantification of the conjunction of a $\Delta_1$ formula, which is $\Pi_n$, and of $\mathrm{Sat}_{\Pi_n}$, which is $\Pi_n$ by the induction hypothesis; it is $\Sigma_{n+1}$. The case of $\mathrm{Sat}_{\Pi_n}$ is dual.

2. Let $z = \ulcorner \exists v_i\ w \urcorner \in \Sigma^*_n$. The maximal existential block of $z$ is $v_i$ followed by the maximal block of $w$, listed by $d_w$, and the remaining formula $u$ is the same. If $e'$ agrees with $e$ outside $\{ i \} \cup d_w$ and satisfies $u$, let $x = e'(i)$; then $e'$ agrees with $e[i := x]$ outside $d_w$, so $\mathrm{Sat}_{\Sigma_n}(w, e[i := x])$. Conversely, if $e'$ agrees with $e[i := x]$ outside $d_w$, it agrees with $e$ outside $\{ i \} \cup d_w$. If $z$ does not begin with an unbounded $\exists$, its block is empty, $u = z$, and $e'$ must agree with $e$ everywhere, so $\mathrm{Sat}_{\Sigma_n}(z, e) \leftrightarrow \mathrm{Sat}_{\Pi_{n-1}}(z, e)$, since the satisfaction formulas depend only on the values of the assignment. The dual statements are proved in the same way.
:::

:::quiz[partial truth definitions]
In the proof of the Tarski condition for $\exists v_i\ w$, why is the *maximal* existential block of $z$ used in :ref{#def-sat-n}?

- [x] To make the decomposition of $z$ unique, so that the definition does not depend on a choice; the block of $z = \exists v_i\ w$ is then $v_i$ followed by the block of $w$, which is what the proof uses.
- [ ] Because the matrix $u$ must be bounded.

  The matrix is $\Pi^*_{n-1}$, which for $n \geq 2$ may contain unbounded quantifiers.
- [ ] Because $\mathrm{Sat}_{\Sigma_n}$ would otherwise not be $\Sigma_n$.

  The complexity does not depend on the length of the block, which is quantified over through $e'$.
:::

The theorem gives the scheme that justifies the name truth definition. We write $\varphi(e)$ for $\exists \bar x\ (\bigwedge_{i \leq k} x_i = e(i) \wedge \varphi(\bar x))$, when the free variables of $\varphi$ are among $v_0, \dots, v_k$.

:::corollary[Tarski's scheme for Σₙ formulas]{#cor-snowing}
Let $n \geq 1$. For every $\Sigma^*_n$ formula $\varphi$, $\mathrm I\Sigma_1$ proves $\forall e\ \big(\varphi(e) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(\ulcorner \varphi \urcorner, e)\big)$, and similarly for $\Pi^*_n$ formulas and $\mathrm{Sat}_{\Pi_n}$. The proof uses only $\mathrm{PA}^-$, the characterizations of :ref{#fact-syntax} for $\mathrm{Val}$ and the decomposition of codes, the properties of assignments, and Tarski's conditions of :ref{#thm-sat0} and :ref{#thm-sat-n}: finitely many sentences provable in $\mathrm I\Sigma_1$. (The syntactic facts about the particular code $\ulcorner \varphi \urcorner$, such as $\ulcorner \varphi \urcorner \in \Sigma^*_n$, are true $\Sigma_1$ sentences, provable in $\mathrm{PA}^-$ by :ref{#thm-sigma1-complete}, once the equivalence of the $\Sigma_1$ and $\Pi_1$ definitions of :ref{#fact-syntax} is among these sentences.)
:::

:::proof{of=cor-snowing}
By induction on $\varphi$ in the metatheory, first through the $\Delta^*_0$ formulas, then through the blocks. For atomic formulas, :ref{#fact-syntax} gives $\mathrm{Val}(\ulcorner t \urcorner, e) = t(e)$; the connectives and bounded quantifiers follow from Tarski's conditions for $\mathrm{Sat}_0$, the induction hypothesis being applied to all assignments, in particular to $e[i := u]$. A $\Delta^*_0$ formula is also $\Sigma^*_n$ and $\Pi^*_n$, and the second Tarski condition of :ref{#thm-sat-n}, applied $n$ times, reduces $\mathrm{Sat}_{\Sigma_n}$ to $\mathrm{Sat}_0$ on it. For $\exists v_i\ w$, the condition gives $\mathrm{Sat}_{\Sigma_n}(\ulcorner \exists v_i\ w \urcorner, e) \leftrightarrow \exists x\ \mathrm{Sat}_{\Sigma_n}(\ulcorner w \urcorner, e[i := x])$, and the induction hypothesis for $w$, applied to $e[i := x]$, turns the right-hand side into $\exists x\ w(e[i := x])$, which is $(\exists v_i\ w)(e)$. A formula that does not begin with an unbounded $\exists$ is reduced to $\mathrm{Sat}_{\Pi_{n-1}}$, and the dual argument applies.
:::

For each $n \geq 1$, the formula $\mathrm{Sat}_{\Sigma_n}$ is thus universal for the $\Sigma^*_n$ formulas: in every model $M$ of $\mathrm I\Sigma_1$, every set defined by a $\Sigma^*_n$ formula with parameters $\bar c$ is $\{ x : M \models \mathrm{Sat}_{\Sigma_n}(a, \langle x, \bar c \rangle) \}$ for a standard number $a$, the code of a formula. It is the formalized counterpart of the universal $\Sigma^0_n$ sets of computability. It also applies to non-standard codes $a$, which are not codes of formulas of the metatheory: in a non-standard model, $\mathrm{Sat}_{\Sigma_n}(a, \cdot)$ is then a $\Sigma_n$-definable set with the parameter $a$, which in general is not defined by any standard formula with standard parameters. Satisfaction for non-standard formulas is a central tool of the later courses of the track.

## Bounds given by terms

The partial truth definitions apply to the formulas of the classes $\Sigma^*_n$, whose bounded quantifiers are bounded by variables. The following lemma shows that this costs nothing in $\mathrm I\Sigma_1$; it uses only the collection scheme for $\Delta^*_0$ formulas, with tuples of witnesses, which we write $\mathrm B\Delta^*_0$.

:::lemma{#lem-variable-bounds}
1. Every $\Delta_0$ formula is equivalent in $\mathrm{PA}^- + \mathrm B\Delta^*_0$ to a formula $\exists \bar w\ \delta_1$ and to a formula $\forall \bar w\ \delta_2$, with $\delta_1, \delta_2 \in \Delta^*_0$ and the same free variables.
2. For $n \geq 1$, every $\Sigma_n$ formula is equivalent in $\mathrm{PA}^- + \mathrm B\Delta^*_0$ to a $\Sigma^*_n$ formula, and every $\Pi_n$ formula to a $\Pi^*_n$ formula. Both theories are contained in $\mathrm I\Sigma_1$.
:::

:::proof{of=lem-variable-bounds}
1. By induction on the formula. Atomic formulas are in $\Delta^*_0$. Negation exchanges the two forms, and conjunction and disjunction preserve them after renaming the bound variables apart. Let $\theta \leftrightarrow \exists \bar u\ \theta_1 \leftrightarrow \forall \bar u\ \theta_2$, and consider $\exists x < t\ \theta$, with $w$ a new variable. Then $\exists x < t\ \theta$ is equivalent to $\exists w\ (w = t \wedge \exists x < w\ \exists \bar u\ \theta_1)$, hence logically to $\exists w\ \exists \bar u\ (w = t \wedge \exists x < w\ \theta_1)$, which has the first form. It is also equivalent to $\forall w\ (w = t \rightarrow \exists x < w\ \forall \bar u\ \theta_2)$. By $\mathrm B\Delta^*_0$ applied to $\neg \theta_2$, $\exists x < w\ \forall \bar u\ \theta_2$ is equivalent to $\forall v\ \exists x < w\ \forall \bar u < v\ \theta_2$: if every $x < w$ had some $\bar u$ with $\neg \theta_2$, collection would bound these witnesses by some $v$. So the formula is equivalent to $\forall w\ \forall v\ (w = t \rightarrow \exists x < w\ \forall \bar u < v\ \theta_2)$, which has the second form. The case $\forall x < t\ \theta$ is dual.

2. Write the $\Sigma_n$ formula as a block of quantifiers followed by a $\Delta_0$ formula $\delta$, and replace $\delta$ by the form of item 1 whose quantifiers are of the same kind as the last block; the new quantifiers merge with it. The resulting formula is $\Sigma^*_n$ after grouping the blocks. $\mathrm I\Sigma_1$ proves $\mathrm B\Sigma_1$, which contains $\mathrm B\Delta^*_0$.
:::

With :ref{#cor-snowing}, the lemma gives the general form of Tarski's scheme.

:::corollary{#cor-snowing-general}
For every $n \geq 1$ and every $\Sigma_n$ formula $\varphi(v_0, \dots, v_k)$, there is a $\Sigma^*_n$ formula $\varphi^*$ such that $\mathrm I\Sigma_1$ proves $\varphi(\bar v) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(\ulcorner \varphi^* \urcorner, \langle v_0, \dots, v_k \rangle)$; similarly for $\Pi_n$ formulas and $\mathrm{Sat}_{\Pi_n}$.
:::

So $\mathrm{Sat}_{\Sigma_n}$ is a **universal $\Sigma_n$ formula**: in a model $M$ of $\mathrm I\Sigma_1$, every $\Sigma_n$-definable set with parameters $\bar c$ is $\{ x : M \models \mathrm{Sat}_{\Sigma_n}(a, \langle x, \bar c \rangle) \}$ for a standard number $a$, the code of $\varphi^*$.

:::remark{#rem-variable-bounds-pr}
The translation $\varphi \mapsto \varphi^*$ given by the proof of :ref{#lem-variable-bounds} is primitive recursive on codes. It is defined by recursion on the formula: each clause of the proof builds the code of the translated formula from the codes of the translations of the immediate components, by pairing, by renaming bound variables apart and by choosing new variables. A variable new for a formula with code $z$ can be taken as $v_z$ or $v_{z + 1}$, since every variable $v_i$ occurring in it has $i < z$; renaming is itself a recursion on codes. So $\ulcorner \varphi \urcorner \mapsto \ulcorner \varphi^* \urcorner$ is defined by course-of-values recursion from primitive recursive operations, and it is primitive recursive (:ref{#thm-course-of-values}). By :ref{#cor-course-of-values-provable}, its restriction to the codes of $\Sigma_n$ formulas is represented in $\mathrm I\Sigma_1$ by a provably total function $t_n$ with a $\Delta_1$ graph, and for each standard $\varphi$ the equation $t_n(\ulcorner \varphi \urcorner) = \ulcorner \varphi^* \urcorner$ is a true $\Sigma_1$ sentence, hence provable in $\mathrm{PA}^-$ by :ref{#thm-sigma1-complete}. The equivalence of $\varphi$ and $\varphi^*$, on the other hand, is proved in $\mathrm I\Sigma_1$ only for each standard formula: the lemma is a scheme in the metatheory.
:::

## Exercises

::::exercise{#ex-tp-sigma1-truth-complete difficulty=1 objective="Use the partial truth definition $\mathrm{Sat}_{\Sigma_1}$ to show that truth for $\Sigma^*_1$ sentences is a complete c.e. set."}
Show that the set of codes of $\Sigma^*_1$ sentences true in $\nat$ is $\Sigma^0_1$, and that every set defined in $\nat$ by a $\Sigma^*_1$ formula with one free variable is many-one reducible to it.

:::solution
In $\nat$, a $\Sigma^*_1$ sentence $\varphi$ is true if and only if $\mathrm{Sat}_{\Sigma_1}(\ulcorner \varphi \urcorner, 0)$, by :ref{#cor-snowing}, since $\nat \models \mathrm I\Sigma_1$; the set of codes of $\Sigma^*_1$ sentences is computable; so the set is defined by a $\Sigma_1$ formula, and it is $\Sigma^0_1$ by :ref{#thm-definable-arithmetic}. Let $A$ be defined by the $\Sigma^*_1$ formula $\varphi(v_0)$, and write $\varphi = \exists \bar u\ \delta$ with $\delta \in \Delta^*_0$, the variables $\bar u$ being distinct from $v_0$. Then $n \in A$ if and only if the $\Sigma^*_1$ sentence $\exists v_0\ \exists \bar u\ (v_0 = \bar n \wedge \delta)$ is true, and its code is a computable function of $n$.
:::
::::

## Notes and references

Partial truth definitions were studied by Montague (1961) and, with their use for reflection principles, by Kreisel and Lévy (1968), according to the bibliographical remarks of Hájek and Pudlák. The formulas $\mathrm{Sat}_{\Sigma_n}$ follow Hájek and Pudlák (Definition I.1.74, Theorem I.1.75), and the scheme is their "it's snowing" lemma (Corollary I.1.76).

- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(d).
- R. Montague, *Semantical closure and non-finite axiomatizability I*, in Infinitistic Methods, Pergamon, 1961, 45–69.
- G. Kreisel and A. Lévy, *Reflection principles and their use for establishing the complexity of axiomatic systems*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 97–142.

:::::exercises
::::exercise{#ex-tp-sat-pi2-compute difficulty=1 objective="Unfold the definitions of $\mathrm{Sat}_{\Pi_2}$ and $\mathrm{Sat}_{\Sigma_1}$ on a formula with two blocks of unbounded quantifiers."}
Let $\varphi$ be the formula $\forall v_1\ \exists v_2\ (v_0 \cdot v_2 = v_1)$. Show that $\varphi \in \Pi^*_2$, and that, in every model of $\mathrm I\Sigma_1$, $\mathrm{Sat}_{\Pi_2}(\ulcorner \varphi \urcorner, e)$ holds if and only if $e(0) = 1$, by unfolding :ref{#def-sat-n}.

:::solution
The formula $\psi \equiv \exists v_2\ (v_0 \cdot v_2 = v_1)$ is $\Sigma^*_1$: a block $\exists v_2$ followed by an atomic formula, which is $\Delta^*_0$ and does not begin with an unbounded $\exists$. Since $\psi$ does not begin with an unbounded $\forall$, $\varphi = \forall v_1\ \psi$ is $\Pi^*_2$, its maximal universal block is $v_1$, and its matrix is $\psi$.

By :ref{#def-sat-n}, $\mathrm{Sat}_{\Pi_2}(\ulcorner \varphi \urcorner, e)$ holds if and only if $\mathrm{Sat}_{\Sigma_1}(\ulcorner \psi \urcorner, e')$ for every $e'$ that agrees with $e$ except possibly at $1$. In turn, $\mathrm{Sat}_{\Sigma_1}(\ulcorner \psi \urcorner, e')$ holds if and only if there is $e''$ that agrees with $e'$ except possibly at $2$ with $\mathrm{Sat}_0(\ulcorner v_0 \cdot v_2 = v_1 \urcorner, e'')$, that is, by the atomic condition and the characterization of $\mathrm{Val}$, with $e''(0) \cdot e''(2) = e''(1)$. Here $e''(0) = e(0)$ and $e''(1) = e'(1)$, and $e''(2)$ can take any value $y$, through $e'' = e'[2 := y]$; similarly $e'(1)$ can take any value $x$. So the condition says: for every $x$ there is $y$ with $e(0) \cdot y = x$. If $e(0) = 1$, take $y = x$. Conversely, the case $x = 1$ gives $e(0) \cdot y = 1$, and in $\mathrm{PA}^-$ this forces $e(0) = 1$: $e(0) \neq 0$ since $0 \cdot y = 0$, and if $e(0) > 1$ then $y \geq 1$ and $e(0) \cdot y \geq e(0) > 1$. So $\varphi(e)$ says that $e(0)$ divides every number, that is, $e(0) = 1$.
:::
::::

::::exercise{#ex-tp-variable-bounds-compute difficulty=1 objective="Apply the reduction of term bounds to bounds by variables to a concrete formula, and locate where collection is needed."}
Let $\psi(v_0)$ be the $\Delta_0$ formula $\forall v_1 < v_0\ \exists v_2 < v_1 + 1\ \theta$, where $\theta \equiv (v_1 = v_2 + v_2 \vee v_1 = v_2 + v_2 + 1)$. Following the proof of :ref{#lem-variable-bounds}, give a $\Pi^*_1$ formula and a $\Sigma^*_1$ formula equivalent to $\psi$ in $\mathrm{PA}^- + \mathrm B\Delta^*_0$. Show that for this formula the equivalences hold in $\mathrm{PA}^-$ alone.

:::solution
Let $w$ and $v$ be new variables. The inner formula $\exists v_2 < v_1 + 1\ \theta$ has a bound given by a term; it is equivalent, by logic, to $\exists w\ (w = v_1 + 1 \wedge \exists v_2 < w\ \theta)$ and to $\forall w\ (w = v_1 + 1 \rightarrow \exists v_2 < w\ \theta)$, with $\Delta^*_0$ matrices.

*$\Pi^*_1$ form.* Substituting the second form, $\psi$ is equivalent to $\forall v_1 < v_0\ \forall w\ (w = v_1 + 1 \rightarrow \exists v_2 < w\ \theta)$, hence, by logic, to
$$
\forall w\ \forall v_1 < v_0\ (w = v_1 + 1 \rightarrow \exists v_2 < w\ \theta),
$$
which is $\Pi^*_1$.

*$\Sigma^*_1$ form.* Substituting the first form, $\psi$ is equivalent to $\forall v_1 < v_0\ \exists w\ (w = v_1 + 1 \wedge \exists v_2 < w\ \theta)$, and the unbounded $\exists w$ must be moved in front of $\forall v_1 < v_0$. The proof does this by collection: the formula is equivalent in $\mathrm B\Delta^*_0$ to
$$
\exists v\ \forall v_1 < v_0\ \exists w < v\ (w = v_1 + 1 \wedge \exists v_2 < w\ \theta),
$$
which is $\Sigma^*_1$. From this formula back to $\psi$ is logic.

*Without collection.* For this formula, the witnesses can be bounded explicitly: if $v_1 < v_0$ and $w = v_1 + 1$, then $w < v_0 + 1$ in $\mathrm{PA}^-$. So $\psi$ implies the $\Sigma^*_1$ formula with $v = v_0 + 1$, in $\mathrm{PA}^-$. The explicit bound comes from the fact that the term $v_1 + 1$ is increasing in $v_1$ and that no unbounded witness occurs inside $\theta$. The proof of the lemma treats all $\Delta_0$ formulas uniformly, including those whose translation already has unbounded witnesses $\bar u$ in front of the matrix, and collection is what bounds these witnesses.
:::
::::

::::exercise{#ex-tp-sat-monotone difficulty=2 objective="Prove, by an induction in the metatheory, that the partial truth definitions agree with one another on the classes where several of them apply."}
Show that for every $n \in \nat$, $\mathrm I\Sigma_1$ proves: for every $e$, if $z \in \Sigma^*_n$ then $\mathrm{Sat}_{\Sigma_n}(z, e) \leftrightarrow \mathrm{Sat}_{\Sigma_{n+1}}(z, e)$, and if $z \in \Pi^*_n$ then $\mathrm{Sat}_{\Pi_n}(z, e) \leftrightarrow \mathrm{Sat}_{\Pi_{n+1}}(z, e)$. Use the facts on syntax that follow :ref{#def-delta0-star}, which $\mathrm I\Sigma_1$ proves: the classes are increasing, and the decomposition of a formula into its maximal block and the rest is unique.

:::solution
By induction on $n$ in the metatheory; we work in $\mathrm I\Sigma_1$.

*$n = 0$.* Let $z \in \Delta^*_0$. It has no unbounded quantifier, so as an element of $\Sigma^*_1$ its maximal existential block is empty and the rest is $z$ itself. By :ref{#def-sat-n}, $\mathrm{Sat}_{\Sigma_1}(z, e)$ holds if and only if $\mathrm{Sat}_0(z, e')$ for some $e'$ that agrees with $e$ at every $i$; such an $e'$ has the same values as $e$, and $\mathrm{Sat}_0$ depends only on the values, so this is $\mathrm{Sat}_0(z, e)$. The case of $\mathrm{Sat}_{\Pi_1}$ is the same, with "for every $e'$".

*From $n$ to $n + 1$.* Let $z \in \Sigma^*_{n+1}$, with maximal existential block listed by $d$ and rest $u \in \Pi^*_n$, which does not begin with an unbounded $\exists$. Since $u \in \Pi^*_{n+1}$ as well, $z \in \Sigma^*_{n+2}$ with the same decomposition, by uniqueness. So
$$
\begin{aligned}
\mathrm{Sat}_{\Sigma_{n+1}}(z, e) &\leftrightarrow \exists e'\ (e' \text{ agrees with } e \text{ outside } d \wedge \mathrm{Sat}_{\Pi_n}(u, e')) \\
&\leftrightarrow \exists e'\ (e' \text{ agrees with } e \text{ outside } d \wedge \mathrm{Sat}_{\Pi_{n+1}}(u, e')) \leftrightarrow \mathrm{Sat}_{\Sigma_{n+2}}(z, e),
\end{aligned}
$$
the middle equivalence by the induction hypothesis for $u \in \Pi^*_n$, applied to each $e'$. The case of $z \in \Pi^*_{n+1}$ is dual.

The induction is in the metatheory because $\mathrm{Sat}_{\Sigma_n}$ is a different formula for each $n$: there is no formula of $n$ to which an induction inside the theory could be applied.
:::
::::

::::exercise{#ex-tp-sat-n-free-variables difficulty=2 objective="Extend the dependence of satisfaction on the variables of the formula from bounded formulas to the partial truth definitions." lessons="bounded-satisfaction"}
Show that for every $n \in \nat$, $\mathrm I\Sigma_1$ proves: if $z \in \Sigma^*_n$ and $e(i) = e'(i)$ for every $i < z$, then $\mathrm{Sat}_{\Sigma_n}(z, e) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(z, e')$; and the same for $\Pi^*_n$ and $\mathrm{Sat}_{\Pi_n}$.

:::solution
By induction on $n$ in the metatheory; we work in $\mathrm I\Sigma_1$. The case $n = 0$ is :ref{#ex-tp-sat0-free-variables}.

Let $z \in \Sigma^*_{n+1}$, with maximal existential block listed by $d$ and rest $u \in \Pi^*_n$; then $u \leq z$, and every index listed in $d$ is the index of a variable of $z$, hence below $z$. Let $e$ and $e'$ agree below $z$, and suppose $\mathrm{Sat}_{\Sigma_{n+1}}(z, e)$: some $e_1$ agrees with $e$ outside $d$ and satisfies $\mathrm{Sat}_{\Pi_n}(u, e_1)$. Let $e_1'$ be the sequence of length $\max(\mathrm{lh}(e_1), \mathrm{lh}(e'))$ with $e_1'(i) = e_1(i)$ if $i$ is listed in $d$ and $e_1'(i) = e'(i)$ otherwise; it exists by item 2 of :ref{#prop-seq-basic}, the condition being bounded and the values bounded by the entries of $e_1$ and $e'$. For $i$ beyond this length, $e_1(i) = 0 = e'(i)$, so $e_1'(i) = e_1(i)$ if $i$ is in $d$ and $e_1'(i) = e'(i)$ otherwise, for every $i$. Then $e_1'$ agrees with $e'$ outside $d$. For $i < u$, either $i$ is listed in $d$ and $e_1'(i) = e_1(i)$, or $e_1'(i) = e'(i) = e(i) = e_1(i)$, since $i < z$. By the induction hypothesis for $u \in \Pi^*_n$, $\mathrm{Sat}_{\Pi_n}(u, e_1')$; so $\mathrm{Sat}_{\Sigma_{n+1}}(z, e')$. The converse exchanges $e$ and $e'$.

For $z \in \Pi^*_{n+1}$, suppose $\mathrm{Sat}_{\Pi_{n+1}}(z, e)$, and let $e_1'$ agree with $e'$ outside $d$. Define $e_1$ from $e_1'$ and $e$ as above, so that $e_1$ agrees with $e$ outside $d$ and with $e_1'$ below $u$. Then $\mathrm{Sat}_{\Sigma_n}(u, e_1)$, hence $\mathrm{Sat}_{\Sigma_n}(u, e_1')$ by the induction hypothesis. So $\mathrm{Sat}_{\Pi_{n+1}}(z, e')$.
:::
::::
:::::
