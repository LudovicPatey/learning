---
title: Types of bounded complexity
summary: Satisfaction for the formulas of a type through partial truth definitions; the Σₙ and Πₙ types of a tuple are coded in a non-standard model of IΣₙ; coded types of Σₙ₊₁ formulas, and of Πₙ₊₁ formulas with a bound, are realized by overspill; a model of IΣ₁ + BΣₙ₊₁ is Σₙ₊₁-recursively saturated exactly when the standard cut is not Σₙ₊₁-definable (Friedman).
duration: 25
prerequisites: [recursively-saturated-models, truth-and-provability/truth-definitions, truth-and-provability/provably-total, fragments-of-arithmetic/coded-sets]
---

Recursive saturation asks for the realization of types whose formulas have unbounded complexity. When all the formulas of a type have complexity at most $\Sigma_{n+1}$, a single formula, the partial truth definition $\mathrm{Sat}_{\Sigma_{n+1}}$ of :ref{#thm-sat-n}, evaluates all of them, and a type coded by an element $s$ becomes the single statement "some $v$ satisfies the first $k$ formulas coded in $s$". This statement holds for every standard $k$, so by **overspill** it holds for some non-standard $k$, and a witness realizes the type. The method needs only enough induction to forbid a definition of the standard cut. This lesson proves the resulting realization lemma and Friedman's characterization of $\Sigma_{n+1}$-recursive saturation; the next lesson uses the lemma, in place of recursive saturation, to prove Friedman's embedding theorem.

Models of $\mathrm I\Sigma_1$ satisfy $\mathrm{exp}$ (:ref{#prop-isigma1-exp}), so standard systems and coded types (:ref{#def-coded-type}) make sense in the non-standard ones.

## Satisfaction for the formulas of a type

The truth definition $\mathrm{Sat}_{\Sigma_n}$ applies to the codes of $\Sigma^*_n$ formulas. The translation $\varphi \mapsto \varphi^*$ of :ref{#lem-variable-bounds}, from $\Sigma_n$ to $\Sigma^*_n$ formulas, is primitive recursive (:ref{#rem-variable-bounds-pr}), and :ref{#thm-pr-provably-total} gives a function $t_n$, provably total in $\mathrm I\Sigma_1$ with a $\Delta_1$ graph, that represents it. For a standard $\Sigma_n$ formula $\varphi(v_0, \dots, v_k)$, the sentence $t_n(\ulcorner \varphi \urcorner) = \ulcorner \varphi^* \urcorner$ is a true $\Sigma_1$ sentence, provable in $\mathrm I\Sigma_1$, and :ref{#cor-snowing} gives
$$
\mathrm I\Sigma_1 \vdash \forall e\ \big( \varphi(e) \leftrightarrow \mathrm{Sat}_{\Sigma_n}(t_n(\ulcorner \varphi \urcorner), e) \big), \tag{1}
$$
and similarly for $\Pi_n$ formulas, with a translation $t'_n$ and $\mathrm{Sat}_{\Pi_n}$. A type $p(v, \bar c)$ is evaluated under the assignment $e = \langle v, \bar c \rangle$.

:::lemma{#lem-fe-types-coded}
Let $n \geq 1$, $M$ a non-standard model of $\mathrm I\Sigma_n$, and $\bar a \in M$. The sets of $\Sigma_n$ formulas and of $\Pi_n$ formulas $\theta(\bar u)$ with $M \models \theta(\bar a)$ belong to $\mathrm{SSy}(M)$. In particular, the $\Sigma_n$ theory $\mathrm{Th}_{\Sigma_n}(M)$ belongs to $\mathrm{SSy}(M)$.
:::

:::proof{of=lem-fe-types-coded}
This is the argument of :ref{#ex-ssy-truth}, with parameters. Let $b$ be non-standard. The set $\{ z < b : M \models \mathrm{Sat}_{\Sigma_n}(t_n(z), \langle \bar a \rangle) \}$ is defined by a $\Sigma_n$ formula, so it is coded by :ref{#thm-friedman-coded}. By (1), its trace on the computable set of codes of $\Sigma_n$ formulas is the first set, which therefore belongs to $\mathrm{SSy}(M)$ (:ref{#thm-ssy-turing-ideal}). A $\Pi_n$ formula $\theta$ holds of $\bar a$ if and only if the $\Sigma_n$ formula obtained from $\neg \theta$ by moving the negation through the quantifier prefix fails; this map is computable, and gives the second set by a computation from the first.
:::

## Coded types of bounded complexity

:::lemma{#lem-fe-realize}
Let $n \geq 0$, let $M$ be a non-standard model of $\mathrm I\Sigma_1 + \mathrm B\Sigma_{n+1}$, and $p(v, \bar c)$ a type over $M$ coded in $M$.

1. If every formula of $p$ is $\Sigma_{n+1}$ and $\nat$ is not $\Sigma_{n+1}$-definable in $M$, then $p$ is realized in $M$.
2. If every formula of $p$ is $\Pi_{n+1}$, $p$ contains a formula $v < a$ with $a \in M$, and $\nat$ is not $\Pi_{n+1}$-definable in $M$, then $p$ is realized in $M$.

Both definability conditions hold if $M \models \mathrm I\Sigma_{n+1}$.
:::

The proof turns the finite satisfiability of $p$ into a single formula of $k$, "some $v$ satisfies the first $k$ formulas coded in $s$", evaluated with the truth definition. It holds for every standard $k$, so it holds for some non-standard $k$; a witness $v$ then satisfies every standard formula of $p$.

:::proof{of=lem-fe-realize}
1. Let $s$ code $p$, and consider
$$
\varphi(k) \equiv \exists v\ \forall z < k\ \big( z \in s \rightarrow \mathrm{Sat}_{\Sigma_{n+1}}(t_{n+1}(z), \langle v, \bar c \rangle) \big).
$$
The matrix is a disjunction of a bounded formula and of a formula that is $\Sigma_{n+1}$ in $M$, by :ref{#thm-sat-n}; by :ref{#lem-fo-collection-closure}, since $M \models \mathrm B\Sigma_{n+1}$, the bounded quantifier keeps it $\Sigma_{n+1}$, and $\varphi$ is $\Sigma_{n+1}$ in $M$. For standard $k$, the elements $z < k$ of $s$ are the codes of finitely many formulas of $p$; some $v$ satisfies all of them, since $p$ is a type, and it satisfies the matrix by (1). The set $\{ k : M \models \varphi(k) \}$ is an initial segment of $M$, since $\varphi(k)$ implies $\varphi(k')$ for $k' < k$; it contains $\nat$ and is $\Sigma_{n+1}$-definable, so it is not $\nat$, and $M \models \varphi(k)$ for some non-standard $k$. Let $v$ be a witness. For every $\theta(v, \bar c) \in p$, the code $\ulcorner \theta \urcorner$ is standard, below $k$ and in $s$, so $\mathrm{Sat}_{\Sigma_{n+1}}(t_{n+1}(\ulcorner \theta \urcorner), \langle v, \bar c \rangle)$ holds, and $M \models \theta(v, \bar c)$ by (1).

2. The same argument applies to
$$
\psi(k) \equiv \exists v < a\ \forall z < k\ \big( z \in s \rightarrow \mathrm{Sat}_{\Pi_{n+1}}(t'_{n+1}(z), \langle v, \bar c \rangle) \big),
$$
which is $\Pi_{n+1}$ in $M$ by :ref{#lem-fo-collection-closure}: over $\mathrm B\Sigma_{n+1}$, $\Pi_{n+1}$ formulas are closed under both bounded quantifiers. For standard $k$, finitely many formulas of $p$ together with $v < a$ are satisfied by some $v$. The last statement is :ref{#prop-cuts-induction}.
:::

:::quiz[coded types of bounded complexity]
Why does item 2 of :ref{#lem-fe-realize} require the bound $v < a$?

- [x] Without it, $\psi(k)$ would begin with an unbounded $\exists v$ in front of a $\Pi_{n+1}$ formula, and would be $\Sigma_{n+2}$; overspill for it would need $\nat$ not to be $\Sigma_{n+2}$-definable.
- [ ] Because a $\Pi_{n+1}$ type might otherwise be realized only by non-standard elements.

  Realizers are non-standard in general; this is not a problem.
- [ ] Because the code $s$ must be below $a$.

  The code is a parameter of $\psi$; its size plays no role.
:::

The first item characterizes partial recursive saturation (:ref{#def-rec-sat}).

:::theorem[Friedman]{#thm-fe-friedman-rs}
Let $n \geq 0$ and $M$ a non-standard model of $\mathrm I\Sigma_1 + \mathrm B\Sigma_{n+1}$. Then $M$ is $\Sigma_{n+1}$-recursively saturated if and only if $\nat$ is not $\Sigma_{n+1}$-definable in $M$.
:::

:::proof{of=thm-fe-friedman-rs}
($\Leftarrow$) Recursive types are coded (:ref{#thm-ssy-turing-ideal}); apply item 1 of :ref{#lem-fe-realize}. ($\Rightarrow$) If $\theta(v, \bar c)$ is a $\Sigma_{n+1}$ formula defining $\nat$, the recursive $\Sigma_{n+1}$-type $\{ \theta(v, \bar c) \} \cup \{ \bar m < v : m \in \nat \}$ is finitely satisfiable, by any large enough standard number, and omitted.
:::

So every non-standard model of $\mathrm I\Sigma_{n+1}$ is $\Sigma_{n+1}$-recursively saturated, and every non-standard model of $\mathrm{PA}$ is $\Sigma_n$-recursively saturated for every $n$. It need not be recursively saturated (:ref{#prop-rs-definable}): the types of recursive saturation have formulas of unbounded complexity, and no single truth definition covers them.

::::exercise{#ex-bt-sigma1-bound difficulty=1 objective="Realize a coded type of bounded formulas to bound the witnesses of all true $\Sigma_1$ sentences."}
Let $M$ be a non-standard model of $\mathrm I\Sigma_1$. Show that some $d \in M$ bounds witnesses of all true $\Sigma_1$ sentences: if $M \models \exists \bar x\ \theta(\bar x)$ with $\theta$ bounded, then $M \models \exists \bar x < d\ \theta(\bar x)$.

:::solution
Let $q_0(v) = \{ \exists \bar x < v\ \theta(\bar x) : M \models \exists \bar x\ \theta(\bar x),\ \theta \text{ bounded} \}$. It is computable from $\mathrm{Th}_{\Sigma_1}(M)$, which belongs to $\mathrm{SSy}(M)$ by :ref{#lem-fe-types-coded}, so it is coded in $M$ (:ref{#thm-ssy-turing-ideal}). A finite part is satisfied by any $v$ above witnesses of the finitely many sentences involved. Its formulas are bounded, hence $\Sigma_1$, and $M \models \mathrm I\Sigma_1$; by :ref{#lem-fe-realize} (1) with $n = 0$, some $d$ realizes $q_0$.
:::
::::

## Notes and references

:ref{#thm-fe-friedman-rs} is Wong's Theorem 7.4, stated there over $\mathrm B\Sigma_{n+1} + \mathrm{exp}$ and attributed to H. Friedman (1973), where it is implicit; Wong's proof uses truth definitions in $\mathrm I\Delta_0 + \mathrm{exp}$, while this lesson uses those of :ref{#thm-sat-n}, built in $\mathrm I\Sigma_1$. :ref{#lem-fe-types-coded} is the argument of :ref{#ex-ssy-truth} with parameters. Item 2 of :ref{#lem-fe-realize}, for bounded $\Pi_{n+1}$ types, is what the back steps of the next lesson need.

- H. Friedman, *Countable models of set theories*, in Cambridge Summer School in Mathematical Logic, Lecture Notes in Mathematics 337, Springer, 1973, 539–573.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 7.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.

:::::exercises
::::exercise{#ex-bt-code-below difficulty=1 objective="Apply the realization lemma to find codes of a set of the standard system below any non-standard element."}
Let $M$ be a non-standard model of $\mathrm I\Sigma_1$, $X \in \mathrm{SSy}(M)$ and $a \in M$ non-standard. Show, with :ref{#lem-fe-realize}, that some $c < a$ satisfies $\mathrm{Ack}(c) \cap \nat = X$.

:::solution
Consider, with the parameter $a$, the type $p(v) = \{ v < a \} \cup \{ \bar n \in v : n \in X \} \cup \{ \neg\, \bar n \in v : n \notin X \}$. Its formulas are bounded, hence $\Sigma_1$, and its set of codes is computable from $X$, so it belongs to $\mathrm{SSy}(M)$ (:ref{#thm-ssy-turing-ideal}) and $p$ is coded. A finite part mentions numbers $n < m$ only; the standard number $\sum_{n \in X,\, n < m} 2^n$ is below $a$ and satisfies it, since bounded sentences with numerals have the same truth value in $M$ and in $\nat$ (:ref{#thm-sigma1-complete}). By :ref{#lem-fe-realize} (1) with $n = 0$, since $M \models \mathrm I\Sigma_1$, some $c$ realizes $p$.
:::
::::

::::exercise{#ex-bt-coding-needed difficulty=1 objective="See why the realization lemma needs coded types, with a type of bounded formulas omitted in a countable model."}
Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$. Show that some type over $M$ without parameters, all of whose formulas are bounded, is omitted in $M$.

:::solution
Every member of $\mathrm{SSy}(M)$ is $\mathrm{Ack}(c) \cap \nat$ for some $c \in M$, so $\mathrm{SSy}(M)$ is countable, and some $X \subseteq \nat$ is not in it. Let $p_X(v) = \{ \bar n \in v : n \in X \} \cup \{ \neg\, \bar n \in v : n \notin X \}$, as in :ref{#ex-rs-types} (2). A finite part mentions numbers $n < m$ only, and is satisfied by $\sum_{n \in X,\, n < m} 2^n$, by :ref{#thm-sigma1-complete} as in :ref{#ex-bt-code-below}; so $p_X$ is a type. An element realizing it would satisfy $\mathrm{Ack}(c) \cap \nat = X$, which is impossible. So :ref{#lem-fe-realize} fails for types that are not coded, even of bounded formulas.
:::
::::

::::exercise{#ex-bt-sigma-n-bound difficulty=2 objective="Adapt the bound for witnesses of $\Sigma_1$ sentences to $\Sigma_{n+1}$ sentences in models of $\mathrm I\Sigma_{n+1}$."}
Let $n \geq 0$ and $M$ a non-standard model of $\mathrm I\Sigma_{n+1}$. Show that some $d \in M$ satisfies: for every $\Pi_n$ formula $\theta(\bar x)$ without parameters, if $M \models \exists \bar x\ \theta(\bar x)$, then $M \models \exists \bar x\ (\bar x < d \wedge \theta(\bar x))$. For $n = 0$ this is :ref{#ex-bt-sigma1-bound}.

:::solution
For a $\Pi_n$ formula $\theta(\bar x)$, the formula $\bar x < v \wedge \theta(\bar x)$ is logically equivalent to the $\Pi_n$ formula obtained by putting the bounded conjunct $\bar x < v$ inside the quantifier prefix of $\theta$, and this rewriting is computable. Let $\theta^\sharp(v)$ be the $\Sigma_{n+1}$ formula $\exists \bar x$ followed by it, and
$$
q(v) = \{ \theta^\sharp(v) : \theta \in \Pi_n,\ M \models \exists \bar x\ \theta(\bar x) \}.
$$
The sentences $\exists \bar x\ \theta(\bar x)$ are $\Sigma_{n+1}$, so the set of codes of $q$ is computable from $\mathrm{Th}_{\Sigma_{n+1}}(M)$, which belongs to $\mathrm{SSy}(M)$ by :ref{#lem-fe-types-coded}, applied with $n + 1 \geq 1$; so $q$ is coded (:ref{#thm-ssy-turing-ideal}). A finite part concerns finitely many true sentences $\exists \bar x\ \theta_j(\bar x)$; any $v$ greater than all entries of chosen witnesses satisfies it. The model satisfies $\mathrm I\Sigma_1$ and $\mathrm B\Sigma_{n+1}$ (:ref{#thm-fo-parsons}), and $\nat$ is not $\Sigma_{n+1}$-definable in it, by the last statement of :ref{#lem-fe-realize}. By item 1 of that lemma, some $d$ realizes $q$.
:::
::::

::::exercise{#ex-bt-sigma-n-same-type difficulty=2 objective="Realize, by overspill on a truth definition, a second element with the same $\Sigma_n$ properties as a non-definable element."}
Let $M$ be a non-standard model of $\mathrm{PA}$, $n \in \nat$, and $a \in M$ an element not definable in $M$ without parameters. Show that some $b \neq a$ satisfies exactly the same $\Sigma_n$ formulas $\theta(x)$ without parameters as $a$.

:::solution
For a $\Sigma_n$ formula $\theta$, write $\theta^-$ for the $\Pi_n$ formula obtained from $\neg \theta$ by moving the negation through the quantifier prefix. Let
$$
q(v) = \{ v \neq a \} \cup \{ \theta(v) : \theta \in \Sigma_n,\ M \models \theta(a) \} \cup \{ \theta^-(v) : \theta \in \Sigma_n,\ M \models \neg \theta(a) \}.
$$
Its formulas are $\Sigma_n$ or $\Pi_n$, hence equivalent to $\Sigma_{n+1}$ formulas by adding dummy quantifiers, computably. If $n \geq 1$, the set of $\Sigma_n$ formulas true of $a$ belongs to $\mathrm{SSy}(M)$ by :ref{#lem-fe-types-coded}; if $n = 0$, it is computable from the set of $\Sigma_1$ formulas true of $a$, given by the same lemma. In both cases the set of codes of $q$ is computable from it, so $q$ is coded.

A finite part involves $v \neq a$ and finitely many formulas; let $\eta(x)$ be their conjunction, other than $v \neq a$. Then $M \models \eta(a)$. If $a$ were the only element satisfying $\eta$, it would be definable by $\eta$; so some $b \neq a$ satisfies $\eta$, and the finite part. Since $M \models \mathrm I\Sigma_{n+1}$, :ref{#lem-fe-realize} (1) gives $b$ realizing $q$. For a $\Sigma_n$ formula $\theta$, $M \models \theta(b)$ if $M \models \theta(a)$, and $M \models \theta^-(b)$, that is $\neg \theta(b)$, otherwise.

The same argument for all formulas at once needs a truth definition for formulas of unbounded complexity; for recursively saturated models it is a direct application of the definition.
:::
::::
:::::
