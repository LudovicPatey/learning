---
title: Recursively saturated models
summary: Types over a structure, recursive types and recursively saturated structures; every countable structure for a recursive language has a countable recursively saturated elementary extension; a non-standard model of IΔ₀ + exp is recursively saturated exactly when it realizes every type coded in it, and its realized complete types are then exactly its coded complete types.
duration: 45
prerequisites: [cuts-and-extensions/standard-system, cuts-and-extensions/scott-tennenbaum]
---

A structure is **saturated** when it realizes every type consistent with its elementary diagram. No countable model of Peano arithmetic realizes all types with finitely many parameters. Recursive saturation, due to Barwise and Schlipf, asks only for the types that a computation can list. Later lessons show that countable recursively saturated models are determined by two invariants, have many automorphisms, and are the countable models carrying a full satisfaction class. This lesson defines them, proves their existence, and characterizes them through the standard system (:ref{#def-coded-subsets}): a non-standard model of $\mathrm I\Delta_0 + \mathrm{exp}$ is recursively saturated exactly when it realizes every type that it codes. Compactness, elementary diagrams and unions of elementary chains are used without comment.

## Types

A language $\mathcal L$ is **recursive** if its symbols are coded by numbers so that the syntactic notions are computable; $\mathcal L_A$, with the coding of :ref{#fact-syntax}, and its extensions by finitely many symbols are recursive. For an $\mathcal L$-structure $M$, $\mathcal L(M)$ is $\mathcal L$ with a new constant for each element of $M$, written as the element itself, and $\mathrm{ElemDiag}(M)$ is the set of $\mathcal L(M)$-sentences true in $M$.

:::definition{#def-rs-type}
Let $M$ be a structure for a recursive language $\mathcal L$.

1. A **type** over $M$ is a set $p(\bar v)$ of $\mathcal L(M)$-formulas whose free variables are among a fixed finite tuple $\bar v$, that is **finitely satisfiable** in $M$: for every finite $p_0 \subseteq p$, $M \models \exists \bar v \bigwedge p_0$. It is **realized** by $\bar a \in M$ if $M \models \theta(\bar a)$ for every $\theta \in p$, and **omitted** otherwise.
2. The type has **finitely many parameters** if the constants from $M$ occurring in its formulas form a finite tuple $\bar c$. We then write $p = p(\bar v, \bar c)$, and $p(\bar v, \bar z) = \{ \theta(\bar v, \bar z) \in \mathcal L : \theta(\bar v, \bar c) \in p \}$ for its set of $\mathcal L$-formulas, in new variables $\bar z$.
3. It is **recursive** if it has finitely many parameters and $\{ \ulcorner \theta(\bar v, \bar z) \urcorner : \theta(\bar v, \bar c) \in p \}$ is a computable set.
4. It is **complete** if for every $\mathcal L$-formula $\theta(\bar v, \bar z)$, either $\theta(\bar v, \bar c)$ or $\neg \theta(\bar v, \bar c)$ belongs to $p$. For $\bar a, \bar c \in M$, the **type of $\bar a$ over $\bar c$** is the complete type $\mathrm{tp}(\bar a / \bar c) = \{ \theta(\bar v, \bar c) : M \models \theta(\bar a, \bar c) \}$; $\mathrm{tp}(\bar a)$ is the type over the empty tuple.
:::

By compactness, a set of $\mathcal L(M)$-formulas is finitely satisfiable in $M$ if and only if it is consistent with $\mathrm{ElemDiag}(M)$, the variables read as new constants; so a type is realized in some elementary extension of $M$.

:::example{#ex-rs-types}
Let $M$ be a model of $\mathrm{PA}$.

1. $p(v) = \{ \bar n < v : n \in \nat \}$ is a recursive type without parameters: a finite part says $v > \bar n$ for a standard $n$. It is realized exactly by the non-standard elements. In $\nat$ it is finitely satisfiable and omitted.
2. Let $X \subseteq \nat$ and $p_X(v) = \{ \bar n \in v : n \in X \} \cup \{ \neg\, \bar n \in v : n \notin X \}$, with the bounded formula of :ref{#def-ack-membership}. A finite part mentions $n < m$ only and is satisfied by the standard number $\sum_{n \in X,\, n < m} 2^n$. If $M$ is non-standard, $p_X$ is realized in $M$ if and only if $X \in \mathrm{SSy}(M)$. It is recursive if and only if $X$ is computable.
3. Let $p(v) = \{ \exists! x\ \theta(x) \rightarrow \neg \theta(v) : \theta(x) \in \mathcal L_A \}$. A finite part excludes the finitely many elements defined without parameters by the formulas involved, and $M$ is infinite. This recursive type is realized exactly by the elements of $M$ that are not definable without parameters.
:::

:::definition{#def-rec-sat}
A structure $M$ for a recursive language is **recursively saturated** if every recursive type over $M$ is realized in $M$. For a class $\Gamma$ of formulas, $M$ is **$\Gamma$-recursively saturated** if every recursive type over $M$ consisting of $\Gamma$ formulas with parameters is realized.
:::

Both restrictions are needed. Over an infinite $M$, the set $\{ v \neq a : a \in M \}$ is a type with infinitely many parameters, omitted in $M$. By the second example, a non-standard model realizing all types with finitely many parameters has $\mathrm{SSy}(M) = \mathcal P(\nat)$, which is impossible for a countable model. By the first example, $\nat$ is not recursively saturated, and a recursively saturated model of $\mathrm{PA}$ is non-standard.

## Existence

:::theorem{#thm-rs-existence}
Let $M$ be a countable structure for a recursive language $\mathcal L$. There is a countable recursively saturated structure $N$ with $M \preccurlyeq N$.
:::

:::proof{of=thm-rs-existence}
*One step.* There are countably many computable sets and countably many finite tuples of elements of $M$, so countably many recursive types $p_0, p_1, \dots$ over $M$; say $p_i$ is in the variables $\bar v_i$. Take new constants $\bar d_i$ for each $i$, and let $\Sigma = \mathrm{ElemDiag}(M) \cup \bigcup_i p_i(\bar d_i)$. A finite part of $\Sigma$ holds in $M$ when each $\bar d_i$ is interpreted by a tuple satisfying the finitely many formulas of $p_i$ involved; distinct types have distinct constants. By compactness and the downward Löwenheim–Skolem theorem, $\Sigma$ has a countable model, whose reduct to $\mathcal L$ is, after identification, a countable elementary extension $M'$ of $M$ in which every recursive type over $M$ is realized.

*The chain.* Let $M_0 = M$ and $M_{k+1} = M_k'$. The union $N = \bigcup_k M_k$ is countable, and $M \preccurlyeq M_k \preccurlyeq N$. Let $p(\bar v, \bar c)$ be a recursive type over $N$. Its parameters lie in some $M_k$, and $p$ is a type over $M_k$: a finite part satisfied in $N$ is satisfied in $M_k$, by elementarity. So $p$ is realized in $M_{k+1}$ by some $\bar a$, and $N \models \theta(\bar a, \bar c)$ for every $\theta \in p$, again by elementarity.
:::

Recursiveness enters only through the number of types; the same chain gives every infinite structure a recursively saturated elementary extension of the same cardinality. So every completion of $\mathrm{PA}$ has countable recursively saturated models, which are non-standard. Not every non-standard model is recursively saturated.

:::proposition{#prop-rs-definable}
Let $M$ be a model of $\mathrm{PA}$ and $\bar c \in M$ such that every element of $M$ is definable in $M$ with the parameters $\bar c$. Then $M$ is not recursively saturated. In particular, for every completion $T$ of $\mathrm{PA}$ other than the theory of $\nat$, the elements of a model of $T$ that are definable without parameters form a non-standard model of $T$ that is not recursively saturated.
:::

:::proof{of=prop-rs-definable}
The type $\{ \exists! x\ \theta(x, \bar c) \rightarrow \neg \theta(v, \bar c) : \theta(x, \bar z) \in \mathcal L_A \}$ is recursive, with parameters $\bar c$, and finitely satisfiable as in :ref{#ex-rs-types} (3). It is omitted, since every element is defined by some $\theta(x, \bar c)$.

For the second statement, let $N \models T$ and $K$ the set of its elements definable without parameters. As in the proof of :ref{#thm-scott-converse}, least witnesses make $K \preccurlyeq N$, by the Tarski–Vaught test; every element of $K$ is definable in $K$ by the formula that defines it in $N$. If $K$ were standard, $T$ would be the theory of $\nat$.
:::

## Coded types

In a non-standard model of arithmetic, a set of formulas can be described by a single element, through the standard system.

:::definition{#def-coded-type}
Let $M$ be a non-standard model of $\mathrm I\Delta_0$. A type $p(\bar v, \bar c)$ over $M$ with finitely many parameters is **coded** in $M$ if $\{ \ulcorner \theta(\bar v, \bar z) \urcorner : \theta(\bar v, \bar c) \in p \} \in \mathrm{SSy}(M)$, that is, if some $s \in M$ satisfies, for every $\mathcal L_A$-formula $\theta(\bar v, \bar z)$, $\theta(\bar v, \bar c) \in p$ if and only if $M \models \ulcorner \theta \urcorner \in s$. We say that $s$ **codes** $p$.
:::

If $M \models \mathrm I\Delta_0 + \mathrm{exp}$ is non-standard, every computable set belongs to $\mathrm{SSy}(M)$ (:ref{#thm-ssy-turing-ideal}), so every recursive type over $M$ is coded. The converse fails: for $X \in \mathrm{SSy}(M)$ not computable, the type $p_X$ of :ref{#ex-rs-types} (2) is coded, its set of codes being computable from $X$, and it is not recursive.

:::theorem{#thm-rs-coded-types}
Let $M$ be a non-standard model of $\mathrm I\Delta_0 + \mathrm{exp}$. Then $M$ is recursively saturated if and only if every type over $M$ coded in $M$ is realized in $M$.
:::

A coded type is a recursive type in disguise: the code $s$ becomes one more parameter, and the type asks $\bar v$ to satisfy every formula whose code is in $s$.

:::proof{of=thm-rs-coded-types}
($\Leftarrow$) Recursive types are coded, by the remark above.

($\Rightarrow$) Let $p(\bar v, \bar c)$ be a type coded by $s$, and
$$
q(\bar v) = \{ \ulcorner \theta \urcorner \in s \rightarrow \theta(\bar v, \bar c) : \theta(\bar v, \bar z) \in \mathcal L_A \},
$$
where $\ulcorner \theta \urcorner$ is the numeral of the code of $\theta$. Its parameters are $\bar c$ and $s$, and the set of its formulas is computable, since the formula $\ulcorner \theta \urcorner \in w \rightarrow \theta(\bar v, \bar z)$, with a new variable $w$ for $s$, is computed from $\theta$, and $\theta$ from it. It is finitely satisfiable: given the formulas of $q$ for $\theta_1, \dots, \theta_k$, the $\theta_j$ with $M \models \ulcorner \theta_j \urcorner \in s$ are in $p$, so some $\bar a$ satisfies all of them, since $p$ is a type; this $\bar a$ satisfies the given formulas of $q$, the other implications being true because their premise is false. By recursive saturation, some $\bar a \in M$ realizes $q$. If $\theta(\bar v, \bar c) \in p$, then $M \models \ulcorner \theta \urcorner \in s$, so $M \models \theta(\bar a, \bar c)$. So $\bar a$ realizes $p$.
:::

:::quiz[coded types]
In the proof of :ref{#thm-rs-coded-types}, why does $q$ use the implication $\ulcorner \theta \urcorner \in s \rightarrow \theta(\bar v, \bar c)$ rather than the equivalence $\ulcorner \theta \urcorner \in s \leftrightarrow \theta(\bar v, \bar c)$?

- [x] With the equivalence, a finite part of $q$ would require $\bar v$ to fail the formulas not in $p$, which may be impossible when $p$ is not complete; the implication requires only the formulas of $p$.
- [ ] Because the equivalence is not a recursive set of formulas.

  The set of equivalences is computable as well; the problem is finite satisfiability.
- [ ] Because $s$ may code non-standard formulas.

  Only standard numerals occur in $q$; what $s$ contains above $\nat$ plays no role.
:::

In the other direction, a realized type need not be coded (see below); a realized complete type is coded if the model is recursively saturated.

:::proposition{#prop-rs-realized-coded}
Let $M$ be a recursively saturated model of $\mathrm I\Delta_0 + \mathrm{exp}$, and $\bar a, \bar c \in M$. Then $\mathrm{tp}(\bar a / \bar c)$ is coded in $M$. In particular, $\mathrm{Th}(M) \in \mathrm{SSy}(M)$.
:::

:::proof{of=prop-rs-realized-coded}
The model is non-standard, by :ref{#ex-rs-types} (1). Consider the recursive type, with parameters $\bar a$ and $\bar c$,
$$
r(w) = \{ \theta(\bar a, \bar c) \leftrightarrow \ulcorner \theta \urcorner \in w : \theta(\bar v, \bar z) \in \mathcal L_A \}.
$$
Given $\theta_1, \dots, \theta_k$, let $m = \sum 2^{\ulcorner \theta_j \urcorner}$, the sum over the $j$ with $M \models \theta_j(\bar a, \bar c)$, a standard number. Bounded sentences $\bar n \in \bar m$ have the same truth value in $M$ and in $\nat$ (:ref{#thm-sigma1-complete}), so $m$ satisfies the $k$ formulas. By recursive saturation, some $s \in M$ realizes $r$; for every formula $\theta$, $\theta(\bar v, \bar c) \in \mathrm{tp}(\bar a / \bar c)$ if and only if $M \models \ulcorner \theta \urcorner \in s$. The set of codes of formulas in $\mathrm{Ack}(s) \cap \nat$ is the intersection of a member of $\mathrm{SSy}(M)$ with a computable set, so it belongs to $\mathrm{SSy}(M)$ by :ref{#thm-ssy-turing-ideal}. For $\mathrm{Th}(M)$, take $\bar a$ and $\bar c$ empty.
:::

:::corollary{#cor-rs-complete-types}
Let $M$ be a recursively saturated model of $\mathrm I\Delta_0 + \mathrm{exp}$. A complete type over $M$ is realized in $M$ if and only if it is coded in $M$.
:::

:::proof{of=cor-rs-complete-types}
A realized complete type $p(\bar v, \bar c)$ is $\mathrm{tp}(\bar a / \bar c)$ for a realizer $\bar a$, and is coded by :ref{#prop-rs-realized-coded}. A coded type is realized by :ref{#thm-rs-coded-types}.
:::

The completeness hypothesis is needed for "realized implies coded": the type $\{ \neg\, \bar n \in v : n \notin X \}$ is realized by $0$, which codes the empty set, for every $X \subseteq \nat$, and it is coded only when $X \in \mathrm{SSy}(M)$, since its set of codes and $\nat \setminus X$ are computable from each other.

So the standard system of a recursively saturated model $M$ of $\mathrm{PA}$ is a Scott set (:ref{#cor-ssy-scott-set}) that contains $\mathrm{Th}(M)$. The next lesson shows that, for countable models, these two invariants determine $M$.

## Exercises

::::exercise{difficulty=1}
Show that the union of an elementary chain $M_0 \preccurlyeq M_1 \preccurlyeq \cdots$ of structures for a recursive language is recursively saturated if every $M_{k+1}$ realizes all recursive types over $M_k$, and that it is recursively saturated if every $M_k$ is.

:::solution
The first statement is the second step of the proof of :ref{#thm-rs-existence}. For the second, a recursive type over the union has its parameters in some $M_k$, is a type over $M_k$ by elementarity, and is realized in $M_k$, hence in the union.
:::
::::

## Notes and references

Recursively saturated structures were introduced by Barwise and Schlipf (1976), in connection with admissible sets; Schlipf (1978) developed their model theory. Wong's Lecture 7 gives the definitions and the existence argument. :ref{#thm-rs-coded-types}, :ref{#prop-rs-realized-coded} and :ref{#cor-rs-complete-types} correspond to Wong's Proposition 8.1, stated there for complete types, and his Proposition 8.13 gives a converse: a non-standard model of $\mathrm{PA}$ in which the coded complete types are exactly the realized ones is recursively saturated.

- J. Barwise and J. S. Schlipf, *An introduction to recursively saturated and resplendent models*, Journal of Symbolic Logic 41 (1976), 531–536.
- J. S. Schlipf, *Toward model theory through recursive saturation*, Journal of Symbolic Logic 43 (1978), 183–206.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 7 and 8.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
