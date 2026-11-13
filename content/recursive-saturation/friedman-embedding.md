---
title: Friedman's embedding theorem
summary: Coded types of bounded complexity are realized by overspill on partial truth definitions; a model of IΣ₁ + BΣₙ₊₁ is Σₙ₊₁-recursively saturated exactly when the standard cut is not Σₙ₊₁-definable; a countable non-standard model of IΣ₁ is isomorphic to a proper initial segment of another one exactly when they have the same standard system and its Σ₁ theory is contained in the other's (Friedman), so every such model is isomorphic to a proper initial segment of itself.
duration: 45
prerequisites: [recursively-saturated-models, truth-and-provability/truth-definitions, fragments-of-arithmetic/coded-sets]
---

Every countable non-standard model of Peano arithmetic is isomorphic to a proper initial segment of itself (Friedman, 1973). The models need not be recursively saturated: the proof is a back-and-forth argument in which every type to be realized has bounded complexity, and such types are realized in every non-standard model of $\mathrm I\Sigma_1$ that codes them, by overspill applied to the partial truth definitions of :ref{#thm-sat-n}.

Models of $\mathrm I\Sigma_1$ satisfy $\mathrm{exp}$ (:ref{#prop-isigma1-exp}), so standard systems and coded types (:ref{#def-coded-type}) make sense in the non-standard ones.

## Satisfaction for the formulas of a type

The truth definition $\mathrm{Sat}_{\Sigma_n}$ applies to the codes of $\Sigma^*_n$ formulas. The translation $\varphi \mapsto \varphi^*$ of :ref{#lem-variable-bounds}, from $\Sigma_n$ to $\Sigma^*_n$ formulas, is given by an explicit syntactic procedure; it is computable, indeed primitive recursive, and :ref{#thm-pr-provably-total} gives a function $t_n$, provably total in $\mathrm I\Sigma_1$ with a $\Delta_1$ graph, that represents it. For a standard $\Sigma_n$ formula $\varphi(v_0, \dots, v_k)$, the sentence $t_n(\ulcorner \varphi \urcorner) = \ulcorner \varphi^* \urcorner$ is a true $\Sigma_1$ sentence, provable in $\mathrm I\Sigma_1$, and :ref{#cor-snowing} gives
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

## Friedman's embedding theorem

:::theorem[Friedman]{#thm-fe-friedman}
Let $M$ and $N$ be countable non-standard models of $\mathrm I\Sigma_1$. The following are equivalent:

1. there is an embedding of $M$ into $N$ whose image is a proper initial segment of $N$;
2. $\mathrm{SSy}(M) = \mathrm{SSy}(N)$ and $\mathrm{Th}_{\Sigma_1}(M) \subseteq \mathrm{Th}_{\Sigma_1}(N)$.
:::

The embedding is built by back-and-forth, with back steps only for elements below the current image, and with the whole image below a fixed $d \in N$. The inductive condition does not compare complete types: every $\Sigma_1$ property of the tuple in $M$ must hold of the tuple in $N$, with witnesses below $d$.

:::proof{of=thm-fe-friedman}
(1 ⇒ 2) Let $I = f[M]$. It is a non-standard model of $\mathrm I\Delta_0 + \mathrm{exp}$ with $I \subseteq_e N$, so $\mathrm{SSy}(M) = \mathrm{SSy}(I) = \mathrm{SSy}(N)$ by :ref{#ex-ssy-end-extension}, and $\Sigma_1$ sentences true in $I$ are true in $N$ by :ref{#cor-sigma1-upward}.

(2 ⇒ 1) Write $\exists \bar x < d$ for a block of existential quantifiers bounded by $d$. For tuples $\bar r \in M$ and $\bar s \in N$ of the same length, and $d \in N$, the **inductive condition** is: for every bounded formula $\theta(\bar x, \bar u)$,
$$
M \models \exists \bar x\ \theta(\bar x, \bar r) \implies N \models \exists \bar x < d\ \theta(\bar x, \bar s). \tag{$*$}
$$
Applied to a bounded $\theta$ without $\bar x$, it says that $\bar r$ and $\bar s$ satisfy the same bounded formulas (apply it to $\theta$ and to $\neg \theta$). Applied to $x = u_i$, it gives $s_i < d$.

*The element $d$.* Let $q_0(v) = \{ \exists \bar x < v\ \theta(\bar x) : M \models \exists \bar x\ \theta(\bar x),\ \theta \text{ bounded} \}$. It is computable from $\mathrm{Th}_{\Sigma_1}(M) \in \mathrm{SSy}(M) = \mathrm{SSy}(N)$ (:ref{#lem-fe-types-coded}), so it is coded in $N$. It is finitely satisfiable in $N$: finitely many of its sentences $\exists \bar x\ \theta_i$ are true in $M$, hence in $N$, and any $v$ above witnesses for all of them satisfies the corresponding formulas. By :ref{#lem-fe-realize} (1), with $n = 0$, some $d \in N$ realizes $q_0$; then $(*)$ holds for the empty tuples.

*Forth.* Let $\bar r, \bar s$ satisfy $(*)$, and $r \in M$. Let
$$
q(v) = \{ v < d \} \cup \{ \exists \bar x < d\ \theta(\bar x, \bar s, v) : M \models \exists \bar x\ \theta(\bar x, \bar r, r),\ \theta \text{ bounded} \}.
$$
It is computable from the set of $\Sigma_1$ formulas true of $(\bar r, r)$, so coded in $N$. For finitely many of its formulas, $M \models \exists v\, \exists \bar x_1 \cdots \bar x_k\, \bigwedge_i \theta_i(\bar x_i, \bar r, v)$, witnessed by $r$; by $(*)$, $N \models \exists v < d\ \exists \bar x_1 \cdots \bar x_k < d\ \bigwedge_i \theta_i(\bar x_i, \bar s, v)$. So $q$ is a type of bounded formulas, realized in $N$ by some $s$ by :ref{#lem-fe-realize} (1). Then $(\bar r, r)$ and $(\bar s, s)$ satisfy $(*)$, by the choice of $q$.

*Back.* Let $\bar r, \bar s$ satisfy $(*)$, and $y \in N$ with $y < s_j$ for some $j$. Let
$$
q'(v) = \{ v < r_j \} \cup \{ \forall \bar x\ \neg \theta(\bar x, \bar r, v) : N \models \forall \bar x < d\ \neg \theta(\bar x, \bar s, y),\ \theta \text{ bounded} \}.
$$
It is computable from the set of bounded formulas true of $(\bar s, y, d)$ in $N$, so coded in $M$. A finite part reduces to one formula $\forall \bar x\, \neg \theta$, with $\theta$ the disjunction of the formulas involved (after renaming their variables $\bar x$ apart). Suppose that $M \models \forall v < r_j\ \exists \bar x\ \theta(\bar x, \bar r, v)$. By $\mathrm B\Sigma_1$ (:ref{#thm-fo-parsons}), $M \models \exists b\ \forall v < r_j\ \exists \bar x < b\ \theta(\bar x, \bar r, v)$, a $\Sigma_1$ property of $\bar r$ with a bounded matrix. By $(*)$, some $b < d$ satisfies $N \models \forall v < s_j\ \exists \bar x < b\ \theta(\bar x, \bar s, v)$; with $v = y$, this contradicts $N \models \forall \bar x < d\ \neg \theta(\bar x, \bar s, y)$. So the finite part is satisfied by some $v < r_j$, and $q'$ is a type of $\Pi_1$ formulas containing $v < r_j$, realized in $M$ by some $r$ by :ref{#lem-fe-realize} (2). If $M \models \exists \bar x\ \theta(\bar x, \bar r, r)$, then $\forall \bar x\, \neg \theta(\bar x, \bar r, v)$ is not in $q'$, that is, $N \models \exists \bar x < d\ \theta(\bar x, \bar s, y)$; so $(\bar r, r)$ and $(\bar s, y)$ satisfy $(*)$.

*The embedding.* Enumerate $M = \{ m_0, m_1, \dots \}$, and $N$ as $n_0, n_1, \dots$ with each element listed infinitely often. Starting from the empty tuples and $d$, alternate forth steps for $m_k$ and back steps for $n_k$, the latter only when $n_k$ is below some entry of the current $\bar s$. Let $f$ map the entries of $\bar r$ to the corresponding entries of $\bar s$. Since corresponding tuples satisfy the same bounded formulas, $f$ is a well-defined embedding, total by the forth steps. If $y < f(x)$, then $x$ is an entry $r_j$ from some stage on, and $y$ is handled at a later back step; so $f[M]$ is an initial segment. It lies below $d$, so it is proper.
:::

:::figure[Friedman's embedding theorem. The image of $M$ is built inside the initial segment of $N$ below $d$: forth steps send elements of $M$ below $d$, keeping witnesses of their $\Sigma_1$ properties below $d$; back steps give preimages to the elements of $N$ below the current image.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Friedman embedding: M is mapped onto a proper initial segment of N lying below an element d; forth steps send elements of M below d, back steps give preimages to elements of N below the image"><defs><marker id="rs-fe" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="40.0" y1="50.0" x2="570.0" y2="50.0" class="ink-stroke" stroke-width="1.2"/><line x1="40.0" y1="140.0" x2="570.0" y2="140.0" class="ink-stroke" stroke-width="1.2"/><text x="22.0" y="55.0" text-anchor="middle" class="math" font-size="15">M</text><text x="22.0" y="145.0" text-anchor="middle" class="math" font-size="15">N</text><circle cx="44.0" cy="50.0" r="3" class="ink-fill"/><circle cx="44.0" cy="140.0" r="3" class="ink-fill"/><circle cx="120.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="90.0" cy="140.0" r="3.5" class="accent-fill"/><line x1="120.0" y1="56.0" x2="90.0" y2="133.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#rs-fe)"/><circle cx="250.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="160.0" cy="140.0" r="3.5" class="accent-fill"/><line x1="250.0" y1="56.0" x2="160.0" y2="133.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#rs-fe)"/><circle cx="400.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="230.0" cy="140.0" r="3.5" class="accent-fill"/><line x1="400.0" y1="56.0" x2="230.0" y2="133.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#rs-fe)"/><circle cx="530.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="290.0" cy="140.0" r="3.5" class="accent-fill"/><line x1="530.0" y1="56.0" x2="290.0" y2="133.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#rs-fe)"/><line x1="330.0" y1="124.0" x2="330.0" y2="156.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><path d="M44,162 L44,168 L326,168 L326,162" class="muted-stroke" stroke-width="1.2"/><text x="185.0" y="186.0" text-anchor="middle" class="label">the image f[M]: a proper initial segment</text><circle cx="450.0" cy="140.0" r="4" class="ink-fill"/><text x="450.0" y="128.0" text-anchor="middle" class="math" font-size="14">d</text><text x="450.0" y="186.0" text-anchor="middle" class="label">all of f[M] and its Σ₁ witnesses lie below d</text></svg>
:::

:::quiz[Friedman's embedding theorem]
In the back step, where is $\Sigma_1$ collection in $M$ used?

- [x] To turn $\forall v < r_j\ \exists \bar x\ \theta$ into the $\Sigma_1$ formula $\exists b\ \forall v < r_j\ \exists \bar x < b\ \theta$, to which the inductive condition applies.
- [ ] To show that $q'$ is coded in $M$.

  Codedness comes from the equality of the standard systems and :ref{#lem-fe-types-coded} in $N$.
- [ ] To realize $q'$.

  Realizing $q'$ uses :ref{#lem-fe-realize}, whose hypotheses include $\mathrm B\Sigma_1$, but the step that needs collection explicitly is the reduction of a finite part to the inductive condition.

:::

:::corollary{#cor-fe-self}
Every countable non-standard model of $\mathrm I\Sigma_1$ is isomorphic to a proper initial segment of itself. In particular, every countable non-standard model of $\mathrm{PA}$ has a proper cut that is a model of $\mathrm{PA}$.
:::

Such cuts are not definable, by :ref{#prop-cuts-induction}. Both conditions of the theorem are needed. A countable Scott set $\mathcal X$ contains completions $T_1 \ni \neg \mathrm{Con}(\mathrm{PA})$ and $T_2 \ni \mathrm{Con}(\mathrm{PA})$ of $\mathrm{PA}$ (first step of the proof of :ref{#thm-scott-converse}), and that theorem gives $M \models T_1$ and $N \models T_2$ with standard system $\mathcal X$; the $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathrm{PA})$ holds in $M$ and not in $N$. Models of one completion with different standard systems (:ref{#cor-bf-classification}) show that the first condition is needed.

## Exercises

::::exercise{difficulty=2}
Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$ and $a \in M$. Show that $M$ is isomorphic to a proper initial segment of itself lying below $a$ if and only if every $\Sigma_1$ sentence true in $M$ has witnesses below $a$.

:::solution
If the condition holds, $a$ realizes $q_0$ (with $N = M$); run the proof with $d = a$. Conversely, let $f : M \cong I$ with $I < a$. If $M \models \theta(\bar b)$ with $\theta$ bounded, then $I \models \theta(f(\bar b))$, so $M \models \theta(f(\bar b))$ by :ref{#lem-delta0-absolute}, and $f(\bar b) < a$.
:::
::::

## Notes and references

:ref{#thm-fe-friedman-rs} is Wong's Theorem 7.4, attributed there to H. Friedman (1973), implicitly. Friedman (1973) proved :ref{#thm-fe-friedman} for models of $\mathrm{PA}$; the extension to $\mathrm I\Sigma_1$ is due to Ressayre and, independently, to Dimitracopoulos and Paris, in the 1980s, and the proof given here follows the back-and-forth pattern of Wong's Theorem 8.5, with recursive saturation replaced by :ref{#lem-fe-realize}. Wong's Theorem 8.5 and Remark 8.7 give the refinement for elementarity: every countable non-standard model of $\mathrm I\Sigma_{n+1}$ is isomorphic to a proper $\Sigma_n$-elementary initial segment of itself. Ressayre also proved a converse: a model of $\mathrm I\Delta_0 + \mathrm{exp}$ such that, for every element $a$, some proper initial self-embedding fixes every element below $a$, is a model of $\mathrm I\Sigma_1$.

- H. Friedman, *Countable models of set theories*, in Cambridge Summer School in Mathematical Logic, Lecture Notes in Mathematics 337, Springer, 1973, 539–573.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 7 and 8.
- J.-P. Ressayre, *Nonstandard universes with strong embeddings, and their finite approximations*, in Logic and Combinatorics, Contemporary Mathematics 65, American Mathematical Society, 1987, 333–358.
- C. Dimitracopoulos and J. Paris, *A note on a theorem of H. Friedman*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 34 (1988), 13–17.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
