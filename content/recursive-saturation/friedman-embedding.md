---
title: Friedman's embedding theorem
summary: A countable non-standard model of IΣ₁ is isomorphic to a proper initial segment of another one exactly when they have the same standard system and its Σ₁ theory is contained in the other's (Friedman); so every such model is isomorphic to a proper initial segment of itself.
duration: 25
prerequisites: [bounded-types, back-and-forth, cuts-and-extensions/scott-tennenbaum]
---

Every countable non-standard model of Peano arithmetic is isomorphic to a proper initial segment of itself (Friedman, 1973). The models need not be recursively saturated. The proof is a **back-and-forth** argument, as in the previous lessons, with two differences. The map is not required to be elementary: it only has to send every $\Sigma_1$ property of a tuple to the image tuple, with witnesses below a fixed element $d$, which keeps the image below $d$ and makes it an initial segment. And every type to be realized has bounded complexity, so that the realization lemma of the previous lesson (:ref{#lem-fe-realize}) replaces recursive saturation. The method gives a criterion for embedding one model as an initial segment of another, in terms of the standard systems and the $\Sigma_1$ theories.

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
- [ ] To show that $f$ preserves addition and multiplication.

  This follows from $(*)$ applied to bounded formulas without $\bar x$, such as $u_i + u_j = u_k$; no collection is involved.

:::

:::corollary{#cor-fe-self}
Every countable non-standard model of $\mathrm I\Sigma_1$ is isomorphic to a proper initial segment of itself. In particular, every countable non-standard model of $\mathrm{PA}$ has a proper cut that is a model of $\mathrm{PA}$.
:::

Such cuts are not definable, by :ref{#prop-cuts-induction}. Both conditions of the theorem are needed. A countable Scott set $\mathcal X$ contains completions $T_1 \ni \neg \mathrm{Con}(\mathrm{PA})$ and $T_2 \ni \mathrm{Con}(\mathrm{PA})$ of $\mathrm{PA}$ (first step of the proof of :ref{#thm-scott-converse}), and that theorem gives $M \models T_1$ and $N \models T_2$ with standard system $\mathcal X$; the $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathrm{PA})$ holds in $M$ and not in $N$. Models of one completion with different standard systems (:ref{#cor-bf-classification}) show that the first condition is needed.

::::exercise{#ex-fe-below difficulty=2 objective="Characterize the elements below which a model embeds into itself as an initial segment."}
Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$ and $a \in M$. Show that $M$ is isomorphic to a proper initial segment of itself lying below $a$ if and only if every $\Sigma_1$ sentence true in $M$ has witnesses below $a$.

:::solution
If the condition holds, $a$ realizes $q_0$ (with $N = M$); run the proof with $d = a$. Conversely, let $f : M \cong I$ with $I < a$. If $M \models \theta(\bar b)$ with $\theta$ bounded, then $I \models \theta(f(\bar b))$, so $M \models \theta(f(\bar b))$ by :ref{#lem-delta0-absolute}, and $f(\bar b) < a$.
:::
::::

## Notes and references

Friedman (1973) proved :ref{#thm-fe-friedman} for models of $\mathrm{PA}$; the extension to $\mathrm I\Sigma_1$ is due to Ressayre and, independently, to Dimitracopoulos and Paris, in the 1980s, and the proof given here follows the back-and-forth pattern of Wong's Theorem 8.5, with recursive saturation replaced by :ref{#lem-fe-realize}. Wong's Theorem 8.5, for recursively saturated models of $\mathrm B\Sigma_{n+1}$ and attributed there essentially to Solovay, and his Remark 8.7 give the refinement for elementarity: every countable non-standard model of $\mathrm I\Sigma_{n+1}$ is isomorphic to a proper $\Sigma_n$-elementary initial segment of itself. Ressayre also proved a converse: a model of $\mathrm I\Delta_0 + \mathrm{exp}$ such that, for every element $a$, some proper initial self-embedding fixes every element below $a$, is a model of $\mathrm I\Sigma_1$.

- H. Friedman, *Countable models of set theories*, in Cambridge Summer School in Mathematical Logic, Lecture Notes in Mathematics 337, Springer, 1973, 539–573.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 8.
- J.-P. Ressayre, *Nonstandard universes with strong embeddings, and their finite approximations*, in Logic and Combinatorics, Contemporary Mathematics 65, American Mathematical Society, 1987, 333–358.
- C. Dimitracopoulos and J. Paris, *A note on a theorem of H. Friedman*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 34 (1988), 13–17.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.

:::::exercises
::::exercise{#ex-fe-decreasing-chain difficulty=1 objective="Iterate an initial self-embedding to obtain a strictly decreasing sequence of initial segments isomorphic to the model."}
Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$. Show that there are proper initial segments $M = I_0 \supsetneq I_1 \supsetneq I_2 \supsetneq \cdots$ of $M$, each isomorphic to $M$.

:::solution
By :ref{#cor-fe-self}, there is an embedding $f : M \to M$ whose image $f[M]$ is a proper initial segment. Let $I_k = f^k[M]$, the image of the $k$-th iterate, which is isomorphic to $M$ through $f^k$.

First, $f$ maps every initial segment $J$ of $M$ onto an initial segment of $M$: if $y < f(x)$ with $x \in J$, then $y \in f[M]$, since $f[M]$ is an initial segment, so $y = f(x')$, and $x' < x$ since $f$ preserves the order and is injective; so $x' \in J$ and $y \in f[J]$. By induction on $k$, each $I_{k+1} = f[I_k]$ is an initial segment. Finally $I_1 \subsetneq I_0$, and applying the injective map $f^k$ gives $I_{k+1} = f^k[I_1] \subsetneq f^k[I_0] = I_k$.
:::
::::

::::exercise{#ex-fe-fix-element difficulty=2 objective="Start the back-and-forth of Friedman's theorem from a non-empty pair of tuples, to fix a given element."}
Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$ and $b \in M$. Show that there is an embedding $f : M \to M$ whose image is a proper initial segment of $M$ and such that $f(b) = b$. Deduce that this image contains every element $x \leq b$.

:::solution
We start the construction of the proof of :ref{#thm-fe-friedman}, with $N = M$, from the tuples $\bar r = \bar s = (b)$ instead of the empty tuples. Let
$$
q(v) = \{ \exists \bar x < v\ \theta(\bar x, b) : M \models \exists \bar x\ \theta(\bar x, b),\ \theta \text{ bounded} \}.
$$
Its set of codes is computable from the set of $\Sigma_1$ formulas true of $b$, which belongs to $\mathrm{SSy}(M)$ by :ref{#lem-fe-types-coded}; so $q$ is coded. A finite part is satisfied by any $v$ above chosen witnesses. Its formulas are bounded, with the parameter $b$, so :ref{#lem-fe-realize} (1) gives $d$ realizing $q$. Then $(b)$ and $(b)$ satisfy the inductive condition $(*)$ with $d$: this is the choice of $q$.

From there, the forth and back steps of the proof apply unchanged, and the embedding $f$ they produce maps the first entry $b$ of $\bar r$ to the first entry $b$ of $\bar s$. Its image is an initial segment below $d$, hence proper. It contains $f(b) = b$, so it contains every $x \leq b$.
:::
::::

::::exercise{#ex-fe-not-symmetric difficulty=2 objective="Use the criterion of Friedman's theorem to show that embeddability as an initial segment is not symmetric." lessons="recursively-saturated-models"}
Give countable non-standard models $M$ and $N$ of $\mathrm{PA}$ such that $M$ is isomorphic to a proper initial segment of $N$, while $N$ is isomorphic to no initial segment of $M$.

:::solution
By :ref{#thm-rs-existence}, the theory of $\nat$ has a countable recursively saturated model $M$; it is non-standard, and $\mathcal X = \mathrm{SSy}(M)$ is a countable Scott set (:ref{#cor-ssy-scott-set}) containing $\mathrm{Th}(M) = \mathrm{Th}(\nat)$ (:ref{#prop-rs-realized-coded}). The theory $\mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA})$ is consistent, by Gödel's second incompleteness theorem, and computable, so $\mathcal X$ contains a completion $T$ of it (first step of the proof of :ref{#thm-scott-converse}), and that theorem gives a countable $N \models T$ with $\mathrm{SSy}(N) = \mathcal X$; it is non-standard since $T \neq \mathrm{Th}(\nat)$.

Every $\Sigma_1$ sentence true in $M$ is true in $\nat$, since $M \equiv \nat$, hence true in $N$ (:ref{#thm-sigma1-complete}). By :ref{#thm-fe-friedman}, $M$ is isomorphic to a proper initial segment of $N$. The $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathrm{PA})$ is true in $N$ and false in $M$, so $\mathrm{Th}_{\Sigma_1}(N) \not\subseteq \mathrm{Th}_{\Sigma_1}(M)$, and by the same theorem $N$ is isomorphic to no proper initial segment of $M$. It is not isomorphic to $M$ itself either, since the theories differ.
:::
::::

::::exercise{#ex-fe-arbitrarily-small difficulty=2 objective="Characterize the models that embed into themselves as initial segments below every non-standard element."}
Let $M$ be a countable non-standard model of $\mathrm I\Sigma_1$. Show that $M$ is isomorphic to a proper initial segment of itself lying below $a$, for every non-standard $a \in M$, if and only if every $\Sigma_1$ sentence true in $M$ is true in $\nat$. Give an example of such a model.

:::solution
By :ref{#ex-fe-below}, the first condition says that for every non-standard $a$, every $\Sigma_1$ sentence true in $M$ has witnesses below $a$.

Suppose every $\Sigma_1$ sentence true in $M$ is true in $\nat$. If $M \models \exists \bar x\ \theta(\bar x)$ with $\theta$ bounded, some standard tuple $\bar n$ satisfies $\theta$ in $\nat$, hence in $M$ (:ref{#thm-sigma1-complete}), and $\bar n < a$ for every non-standard $a$.

Conversely, let $\exists \bar x\ \theta(\bar x)$ be true in $M$, with witnesses below every non-standard element. The bounded formula $\psi(y) \equiv \exists \bar x < y\ \theta(\bar x)$ holds of every non-standard $y$. By the least number principle for bounded formulas, there is a least $y_0$ with $M \models \psi(y_0)$. If $y_0$ were non-standard, $y_0 - 1$ would be non-standard and satisfy $\psi$, contradicting minimality. So $y_0$ is standard, $M \models \theta(\bar n)$ for some standard $\bar n < y_0$, and $\nat \models \theta(\bar n)$ by :ref{#lem-delta0-absolute}. So the sentence is true in $\nat$.

Every countable non-standard model of $\mathrm{Th}(\nat)$, for instance one given by :ref{#thm-rs-existence}, satisfies the condition.
:::
::::
:::::
