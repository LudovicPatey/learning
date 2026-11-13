---
title: Satisfaction for bounded formulas
summary: Codes of formulas and assignments in IΣ₁; quantifiers bounded by variables; satisfaction for bounded formulas through finite tables, Δ₁ in IΣ₁, with Tarski's conditions.
duration: 45
prerequisites: [provably-total, fragments-of-arithmetic/coded-sets]
---

By Tarski's theorem (:ref{#thm-tarski}), truth in $\nat$ for all sentences of arithmetic is not definable by any formula. Truth for sentences of bounded complexity is definable: the set of true $\Sigma_n$ sentences is $\Sigma^0_n$, so some $\Sigma_n$ formula defines it in $\nat$. This lesson and the next construct such formulas, the **partial truth definitions** $\mathrm{Sat}_{\Sigma_n}(z, e)$, "the $\Sigma_n$ formula coded by $z$ is satisfied by the assignment coded by $e$", and prove in $\mathrm I\Sigma_1$ that they satisfy Tarski's inductive conditions. Their use is in non-standard models, where formulas may have non-standard codes and the construction must be justified by proofs from axioms.

This lesson treats bounded formulas, which are evaluated by finite **tables** whose existence is proved by $\Sigma_1$ induction. The next lesson adds unbounded quantifiers, by quantifying over assignments.

## Codes, assignments, and bounds by variables

The variables of $\mathcal L_A$ are $v_0, v_1, \dots$. Terms and formulas are coded with the pairing function of :ref{#fact-pairing}: $\ulcorner v_i \urcorner = \langle 0, i \rangle$, $\ulcorner 0 \urcorner = \langle 1, 0 \rangle$, $\ulcorner 1 \urcorner = \langle 1, 1 \rangle$, $\ulcorner s + t \urcorner = \langle 2, \ulcorner s \urcorner, \ulcorner t \urcorner \rangle$, and similarly with the tags $3$ to $8$ for $\cdot$, $=$, $<$, $\neg$, $\wedge$, $\vee$; $\ulcorner \exists v_i < v_j\ \varphi \urcorner = \langle 9, i, j, \ulcorner \varphi \urcorner \rangle$ and $\ulcorner \forall v_i < v_j\ \varphi \urcorner = \langle 10, i, j, \ulcorner \varphi \urcorner \rangle$; $\ulcorner \exists v_i\ \varphi \urcorner = \langle 11, i, \ulcorner \varphi \urcorner \rangle$ and $\ulcorner \forall v_i\ \varphi \urcorner = \langle 12, i, \ulcorner \varphi \urcorner \rangle$. The codes of the immediate components of a term or formula are smaller than its code, and $\ulcorner v_i \urcorner \geq i$; so every variable $v_i$ occurring in a formula with code $z$ has $i < z$. Formulas are built with $\neg$, $\wedge$ and $\vee$; the bounded quantifiers have their own tags, and only bounds by variables are coded, for the reason explained below.

An **assignment** is any number $e$, read as the function $i \mapsto e(i)$, where $e(i) = (e)_i$ if $e$ is a sequence of length greater than $i$, and $e(i) = 0$ otherwise. For $i$ and $u$, $e[i := u]$ is the sequence of length $\max(\mathrm{lh}(e), i + 1)$, where $\mathrm{lh}(e) = 0$ if $e$ is not a sequence, that agrees with $e$ except at $i$, where its value is $u$; it exists in $\mathrm I\Delta_0 + \mathrm{exp}$ by :ref{#prop-seq-basic}. Every formula of this lesson depends on $e$ only through the values $e(i)$.

:::fact[Arithmetization of syntax]{#fact-syntax}
There are $\Delta_1$ definitions in $\mathrm I\Sigma_1$ of the set of codes of terms, of the set $\Delta^*_0$ of codes of formulas whose quantifiers are all bounded by variables, of the sets $\Sigma^*_n$ and $\Pi^*_n$ below for each $n \in \nat$, and of the function $\mathrm{Val}(t, e)$, the value of the term coded by $t$ under $e$, such that $\mathrm I\Sigma_1$ proves their recursive characterizations: for instance $\mathrm{Val}(\ulcorner v_i \urcorner, e) = e(i)$, $\mathrm{Val}(\ulcorner 1 \urcorner, e) = 1$ and $\mathrm{Val}(\langle 2, s, t \rangle, e) = \mathrm{Val}(s, e) + \mathrm{Val}(t, e)$. For each standard term $t(v_0, \dots, v_k)$, $\mathrm I\Sigma_1$ proves $\mathrm{Val}(\ulcorner t \urcorner, e) = t(e(0), \dots, e(k))$.
:::

These notions are defined by course-of-values recursion on codes, and :ref{#cor-course-of-values-provable} gives the $\Delta_1$ definitions and their characterizations; the last statement follows by induction on $t$ in the metatheory. The details are routine, and we refer to Hájek and Pudlák (I.1.60–I.1.69) for them.

:::definition{#def-delta0-star}
$\Delta^*_0$ is the class of formulas whose quantifiers are bounded quantifiers $\exists v_i < v_j$ and $\forall v_i < v_j$, with $i \neq j$; atomic formulas $s = t$ and $s < t$ may contain arbitrary terms. Let $\Sigma^*_0 = \Pi^*_0 = \Delta^*_0$. A formula is $\Sigma^*_{n+1}$ if it is $\exists v_{i_1} \cdots \exists v_{i_k}\ \psi$ with $k \geq 0$ and $\psi$ a $\Pi^*_n$ formula that does not begin with an unbounded $\exists$; dually, it is $\Pi^*_{n+1}$ if it is $\forall v_{i_1} \cdots \forall v_{i_k}\ \psi$ with $\psi$ a $\Sigma^*_n$ formula that does not begin with an unbounded $\forall$.
:::

The block $\exists v_{i_1} \cdots \exists v_{i_k}$ is then the maximal block of unbounded existential quantifiers at the front of the formula, and the decomposition is unique. Every $\Sigma^*_n$ formula is a $\Sigma_n$ formula, and the classes are increasing: $\Sigma^*_n \cup \Pi^*_n \subseteq \Sigma^*_{n+1} \cap \Pi^*_{n+1}$. Bounds by variables keep the evaluation inside a fixed interval: under an assignment with values below $r$, a variable bounded by $v_j$ takes values below $e(j) < r$, while a bound given by a term could take values far above $r$. The restriction costs nothing: in $\mathrm I\Sigma_1$, every $\Sigma_n$ formula is equivalent to a $\Sigma^*_n$ formula (next lesson).

## Satisfaction for bounded formulas

Satisfaction for bounded formulas is defined by recursion on formulas: the value at $\exists v_i < v_j\ \varphi$ under $e$ is computed from the values at $\varphi$ under the assignments $e[i := u]$, $u < e(j)$. This recursion cannot be handled directly by :ref{#cor-course-of-values-provable}, because the pairs $\langle \varphi, e[i := u] \rangle$ need not be smaller than $\langle z, e \rangle$: the assignment changes. The solution is to compute all values at once, for all formulas below a bound $p$ and all assignments with values below a bound $r$, in a finite table.

:::definition{#def-sat-table}
Let $p, r$ be numbers. A **satisfaction table** for $(p, r)$ is a coded set $q$ of triples $\langle z, e, b \rangle$ with $b \leq 1$, containing exactly one triple for each $z < p$ in $\Delta^*_0$ and each sequence $e$ of length $p$ with values below $r$, and no other triple; we write $q(z, e) = b$, and $q(z, e') = q(z, e)$ for any assignment $e'$ with $e'(i) = e(i)$ for $i < p$. The table must satisfy **Tarski's conditions**: for every such $z$ and $e$,

1. $q(\ulcorner s = t \urcorner, e) = 1$ if and only if $\mathrm{Val}(s, e) = \mathrm{Val}(t, e)$, and similarly for $<$;
2. $q(\ulcorner \neg \varphi \urcorner, e) = 1 - q(\ulcorner \varphi \urcorner, e)$, and $\wedge$, $\vee$ correspond to the minimum and the maximum;
3. $q(\ulcorner \exists v_i < v_j\ \varphi \urcorner, e) = 1$ if and only if $q(\ulcorner \varphi \urcorner, e[i := u]) = 1$ for some $u < e(j)$, and dually for $\forall v_i < v_j$.

We write $\mathrm{Tab}(q, p, r)$.
:::

:::example{#ex-table-even}
Let $z$ be the code of $\exists v_1 < v_0\ (v_0 = v_1 + v_1)$, and $q$ a table for $(p, r)$ with $z < p$. For an assignment $e$ of length $p$ with values below $r$, item 3 gives $q(z, e) = 1$ if and only if $q(\ulcorner v_0 = v_1 + v_1 \urcorner, e[1 := u]) = 1$ for some $u < e(0)$, and item 1 turns this into $e(0) = u + u$ for some $u < e(0)$: $e(0)$ is even and non-zero. :::

In item 3, the subformula has a smaller code, and $i < p$; the assignment $e[i := u]$ has values below $r$ on $[0, p)$, since $u < e(j) < r$. So all the values required are entries of the table. The formula $\mathrm{Tab}(q, p, r)$ is obtained from $\Delta_1$ formulas by bounded quantifiers over $z < p$, over the sequences $e$, whose codes are bounded by :ref{#prop-seq-basic}, and over the elements of $q$; so it is $\Delta_1$ in $\mathrm I\Sigma_1$ by Parsons' lemma, in both directions.

:::lemma{#lem-sat-tables}
$\mathrm I\Sigma_1$ proves:

1. (**uniqueness**) if $\mathrm{Tab}(q, p, r)$ and $\mathrm{Tab}(q', p', r')$, $z < \min(p, p')$, $e$ has values below $r$ on $[0, p)$, $e'$ has values below $r'$ on $[0, p')$, and $e(i) = e'(i)$ for every $i < z$, then $q(z, e) = q'(z, e')$;
2. (**existence**) for all $p$ and $r$, there is $q$ with $\mathrm{Tab}(q, p, r)$.
:::

:::proof{of=lem-sat-tables}
1. Suppose not, and let $z$ be least for which there are assignments $e$ and $e'$, as in the statement, with $q(z, e) \neq q'(z, e')$. The assignments can be taken as sequences of lengths $p$ and $p'$, whose codes are bounded, so the set of such $z$ is $\Delta_1$ in $\mathrm I\Sigma_1$, and it has a least element by the least number principle for $\Sigma_1$ formulas. If $z$ is atomic, both values are given by item 1 of the definition, from $\mathrm{Val}$, which depends only on the values at the indices of the variables of the terms, all below $z$. If $z$ is a negation, conjunction or disjunction, its components are smaller than $z$, so $e$ and $e'$ agree below them, and the values at the components agree, hence those at $z$. If $z = \ulcorner \exists v_i < v_j\ \varphi \urcorner$, then $j < z$, so $e(j) = e'(j)$; for $u < e(j)$, the assignments $e[i := u]$ and $e'[i := u]$ satisfy the hypothesis of the statement at $\ulcorner \varphi \urcorner < z$, so $q$ and $q'$ agree on them, and item 3 gives the same value at $z$; the case of $\forall v_i < v_j$ is the same. In all cases this contradicts the choice of $z$.

2. Fix $r$ and apply $\Sigma_1$ induction on $p$ to $\exists q\ \mathrm{Tab}(q, p, r)$. For $p = 0$, the table is empty. Let $q$ be a table for $(p, r)$. Define $q'$ on the formulas $z < p + 1$ in $\Delta^*_0$ and the sequences $e$ of length $p + 1$ with values below $r$: for $z < p$, let $q'(z, e) = q(z, e)$, which depends only on $e \restriction p$; if $p$ itself is in $\Delta^*_0$, define $q'(p, e)$ by the condition of the definition that corresponds to the form of $p$, from the values of $q'$ at its components, which are below $p$. The set of triples so described is defined by a formula that is $\Delta_1$ in $\mathrm I\Sigma_1$, and it is bounded, by :ref{#prop-seq-basic}; by :ref{#thm-friedman-coded} with $n = 1$, its piece below that bound is coded, and this piece is the whole set. Tarski's conditions hold at $z = p$ by construction, and at $z < p$ because they hold for $q$, since for $i < z$ the assignments $e[i := u]$ and $(e \restriction p)[i := u]$ have the same values below $p$.
:::

:::definition{#def-sat0}
$\mathrm{Sat}_0(z, e)$ is the formula: $z \in \Delta^*_0$, and there are $q, p, r$ with $\mathrm{Tab}(q, p, r)$, $z < p$, $e(i) < r$ for every $i < p$, and $q(z, e) = 1$.
:::

:::theorem{#thm-sat0}
$\mathrm{Sat}_0$ is $\Delta_1$ in $\mathrm I\Sigma_1$, and $\mathrm I\Sigma_1$ proves Tarski's conditions for it: for $z \in \Delta^*_0$ and every assignment $e$, $\mathrm{Sat}_0$ satisfies the three conditions of :ref{#def-sat-table} with $\mathrm{Sat}_0(\cdot, e)$ in place of $q(\cdot, e) = 1$, for instance
$$
\mathrm{Sat}_0(\ulcorner \exists v_i < v_j\ \varphi \urcorner, e) \leftrightarrow \exists u < e(j)\ \mathrm{Sat}_0(\ulcorner \varphi \urcorner, e[i := u]).
$$
:::

:::proof{of=thm-sat0}
As written, $\mathrm{Sat}_0$ is $\Sigma_1$ in $\mathrm I\Sigma_1$. Given $z$ and $e$, the numbers $p = z + 1$ and $r = 1 + \max_{i < p} e(i)$ satisfy the conditions of the definition, and a table for $(p, r)$ exists by :ref{#lem-sat-tables}. By uniqueness, applied with $e' = e$, all tables satisfying the conditions give the same value at $(z, e)$. So $\mathrm{Sat}_0(z, e)$ is also equivalent to: $z \in \Delta^*_0$, and for all $q, p, r$, if $\mathrm{Tab}(q, p, r)$, $z < p$ and $e(i) < r$ for $i < p$, then $q(z, e) = 1$, a $\Pi_1$ formula. For Tarski's conditions, take this table: it applies to $(z, e)$ and to all the pairs used by the condition at $z$, such as $(\varphi, e[i := u])$ for $u < e(j)$, since these assignments have values below $r$ on $[0, p)$. The conditions for $\mathrm{Sat}_0$ are then those of the table.
:::

:::quiz[satisfaction tables]
Where does the construction of $\mathrm{Sat}_0$ use $\Sigma_1$ induction, beyond the facts on syntax?

- [x] In the existence of tables, proved by induction on $p$ for the $\Sigma_1$ formula $\exists q\ \mathrm{Tab}(q, p, r)$; and, through $\mathrm B\Sigma_1$ and Parsons' lemma, to see that $\mathrm{Tab}$ is $\Delta_1$.
- [ ] In the uniqueness of tables only.

  Uniqueness uses the least number principle for a formula that is $\Delta_1$ in $\mathrm I\Sigma_1$, but existence uses $\Sigma_1$ induction as well, and it is the essential use: a table is a single object containing all the values below $(p, r)$.
- [ ] In the definition of $\mathrm{Sat}_{\Sigma_n}$ for $n \geq 1$.

  Unbounded quantifiers are handled by quantifying over assignments; no induction is used at that step.

---

Why are tables indexed by a bound $r$ on the values of assignments?

- [x] Because a table must be a finite object, a coded set, and the assignments with values below $r$ on $[0, p)$ are finitely many in the sense of the model; with bounds by variables, the evaluation of a formula under such an assignment only uses assignments of the same kind.
- [ ] To make the satisfaction relation unique.

  Uniqueness holds for tables with different bounds as well, by :ref{#lem-sat-tables}.
- [ ] Because the formulas below $p$ are infinitely many.

  There are at most $p$ of them.
:::

## Exercises

::::exercise{difficulty=1}
Show that the set of pairs $(z, e)$ of natural numbers such that $\nat \models \mathrm{Sat}_0(z, e)$ is computable.

:::solution
Since $\nat \models \mathrm I\Sigma_1$, :ref{#thm-sat0} gives a $\Sigma_1$ formula and a $\Pi_1$ formula that both define this set in $\nat$. So the set and its complement are $\Sigma_1$-definable, hence c.e. by :ref{#cor-sigma1-ce}, and a set that is c.e. with a c.e. complement is computable. Directly: given $z$ and $e$, compute the table for $p = z + 1$ and $r = 1 + \max_{i < p} e(i)$ by the recursion of the proof of :ref{#lem-sat-tables}, and read the entry.
:::
::::

## Notes and references

The construction follows Hájek and Pudlák, Chapter I, Section 1(d): the arithmetization of syntax (I.1.60–I.1.69) and satisfaction for bounded formulas with bounds by variables through partial satisfactions (Definition I.1.71, Lemma I.1.72, Theorem I.1.70, Lemma I.1.73). Truth definitions for bounded formulas in weaker theories, such as $\mathrm I\Delta_0 + \mathrm{exp}$, exist as well but are more delicate (Hájek and Pudlák, Chapter V, Section 5, and the bibliographical remarks to Chapter V); in $\mathrm I\Delta_0 + \neg \mathrm{exp}$ their existence is related to open problems on collection (Adamowicz, Kołodziejczyk and Paris, 2012).

- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(d).
- Z. Adamowicz, L. A. Kołodziejczyk and J. Paris, *Truth definitions without exponentiation and the Σ₁ collection scheme*, Journal of Symbolic Logic 77 (2012), 649–655.
