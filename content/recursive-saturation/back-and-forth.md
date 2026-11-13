---
title: Back-and-forth and the classification of countable models
summary: Two countable recursively saturated models of IΔ₀ + exp are isomorphic if and only if they have the same theory and the same standard system; countable recursively saturated models are homogeneous; every countable Scott set containing a completion T of PA is the standard system of a countable recursively saturated model of T, so that these models are classified by their standard systems.
duration: 40
prerequisites: [recursively-saturated-models]
---

A countable structure is determined up to isomorphism by very little when it realizes many types: Cantor's theorem that countable dense linear orders without endpoints are isomorphic is the first example. The proof, by **back-and-forth**, builds the isomorphism one element at a time, alternately in the domain and in the range, while keeping the finite partial maps elementary. This lesson applies the method to recursively saturated models of arithmetic. What makes it work is the previous lesson: in such a model, the complete types realized are exactly the complete types coded (:ref{#cor-rs-complete-types}), so two models with the same standard system realize the same types. The theory and the standard system are then a complete set of invariants for countable recursively saturated models, and Scott's theorem (:ref{#thm-scott-converse}) shows which pairs of invariants occur.

## The back-and-forth lemma

For tuples $\bar r$ in $M$ and $\bar s$ in $N$ of the same length, we write $\mathrm{tp}^M(\bar r) = \mathrm{tp}^N(\bar s)$ if the same $\mathcal L_A$-formulas $\theta(\bar u)$ hold of $\bar r$ in $M$ and of $\bar s$ in $N$. For the empty tuples, this says $\mathrm{Th}(M) = \mathrm{Th}(N)$.

:::lemma{#lem-bf-step}
Let $M$ and $N$ be recursively saturated models of $\mathrm I\Delta_0 + \mathrm{exp}$ with $\mathrm{SSy}(M) \subseteq \mathrm{SSy}(N)$, and let $\bar r \in M$, $\bar s \in N$ with $\mathrm{tp}^M(\bar r) = \mathrm{tp}^N(\bar s)$. For every $r \in M$ there is $s \in N$ with $\mathrm{tp}^M(\bar r, r) = \mathrm{tp}^N(\bar s, s)$.
:::

:::proof{of=lem-bf-step}
Let $Y$ be the set of codes of the formulas $\theta(v, \bar u)$ with $M \models \theta(r, \bar r)$. It is the type $\mathrm{tp}(r / \bar r)$, read as a set of formulas in $v, \bar u$, so $Y \in \mathrm{SSy}(M)$ by :ref{#prop-rs-realized-coded}, and $Y \in \mathrm{SSy}(N)$. Let $q(v) = \{ \theta(v, \bar s) : \ulcorner \theta \urcorner \in Y \}$. It is closed under conjunction, and finitely satisfiable in $N$: if $\ulcorner \theta \urcorner \in Y$, then $M \models \exists v\ \theta(v, \bar r)$, witnessed by $r$; the formula $\exists v\ \theta(v, \bar u)$ belongs to $\mathrm{tp}^M(\bar r) = \mathrm{tp}^N(\bar s)$, so $N \models \exists v\ \theta(v, \bar s)$. So $q$ is a type over $N$, coded in $N$ by $Y$, and :ref{#thm-rs-coded-types} gives $s \in N$ realizing it. For every formula $\theta(v, \bar u)$: if $M \models \theta(r, \bar r)$, then $\ulcorner \theta \urcorner \in Y$ and $N \models \theta(s, \bar s)$; if not, $\ulcorner \neg \theta \urcorner \in Y$ and $N \models \neg \theta(s, \bar s)$.
:::

The lemma is the whole content of the method: a complete type over finitely many elements is coded, and a code passes from one model to the other through the standard system.

## The isomorphism theorem

:::theorem{#thm-bf-isomorphism}
Let $M$ and $N$ be countable recursively saturated models of $\mathrm I\Delta_0 + \mathrm{exp}$. Then $M \cong N$ if and only if $\mathrm{Th}(M) = \mathrm{Th}(N)$ and $\mathrm{SSy}(M) = \mathrm{SSy}(N)$. More precisely, if these conditions hold and $\bar a \in M$, $\bar b \in N$ satisfy $\mathrm{tp}^M(\bar a) = \mathrm{tp}^N(\bar b)$, there is an isomorphism $f : M \to N$ with $f(\bar a) = \bar b$.
:::

:::proof{of=thm-bf-isomorphism}
An isomorphism preserves the theory, and it maps $\mathrm{Ack}(c) \cap \nat$ to $\mathrm{Ack}(f(c)) \cap \nat$, since it fixes the numerals and preserves the bounded formula $x \in y$; so it preserves the standard system.

Conversely, enumerate $M = \{ m_0, m_1, \dots \}$ and $N = \{ n_0, n_1, \dots \}$. We build tuples $\bar r_k \in M$ and $\bar s_k \in N$ of the same length, each extending the previous one, with $\mathrm{tp}^M(\bar r_k) = \mathrm{tp}^N(\bar s_k)$ (the **inductive condition**). Start with $\bar r_0 = \bar a$ and $\bar s_0 = \bar b$, or with the empty tuples, for which the condition is $\mathrm{Th}(M) = \mathrm{Th}(N)$.

- *Forth*, at step $2k + 1$: apply :ref{#lem-bf-step} to $r = m_k$, and append $m_k$ to $\bar r$ and the element $s$ obtained to $\bar s$.
- *Back*, at step $2k + 2$: apply :ref{#lem-bf-step} with the roles of $M$ and $N$ exchanged, which is allowed since $\mathrm{SSy}(N) \subseteq \mathrm{SSy}(M)$, to $n_k$, and append it to $\bar s$ and the element obtained to $\bar r$.

Let $f$ map the $i$-th entry of $\bar r_k$ to the $i$-th entry of $\bar s_k$. It is well defined and injective: the formula $u_i = u_j$ holds of $\bar r_k$ if and only if it holds of $\bar s_k$. It preserves every atomic formula, by the inductive condition, so it is an embedding. It is total by the forth steps and surjective by the back steps.
:::

:::figure[The back-and-forth construction. Forth steps (solid) put the next element of $M$ in the domain, back steps (dashed) put the next element of $N$ in the range; at each stage the two finite tuples have the same complete type.]
<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="Back-and-forth between M and N: forth steps send the next element of M to an element of N with the same type over the previous ones, back steps find a preimage in M for the next element of N"><defs><marker id="rs-zz" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="40.0" y1="50.0" x2="570.0" y2="50.0" class="ink-stroke" stroke-width="1.2"/><line x1="40.0" y1="150.0" x2="570.0" y2="150.0" class="ink-stroke" stroke-width="1.2"/><text x="22.0" y="55.0" text-anchor="middle" class="math" font-size="15">M</text><text x="22.0" y="155.0" text-anchor="middle" class="math" font-size="15">N</text><circle cx="90.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="300.0" cy="150.0" r="3.5" class="accent-fill"/><line x1="90.0" y1="56.0" x2="300.0" y2="143.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#rs-zz)"/><text x="90.0" y="38.0" text-anchor="middle" class="math" font-size="13">r<tspan class="mrm" font-size="9" dy="3">0</tspan></text><text x="300.0" y="172.0" text-anchor="middle" class="math" font-size="13">s<tspan class="mrm" font-size="9" dy="3">0</tspan></text><circle cx="450.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="140.0" cy="150.0" r="3.5" class="accent-fill"/><line x1="140.0" y1="144.0" x2="450.0" y2="57.0" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 3" marker-end="url(#rs-zz)"/><text x="450.0" y="38.0" text-anchor="middle" class="math" font-size="13">r<tspan class="mrm" font-size="9" dy="3">1</tspan></text><text x="140.0" y="172.0" text-anchor="middle" class="math" font-size="13">s<tspan class="mrm" font-size="9" dy="3">1</tspan></text><circle cx="230.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="490.0" cy="150.0" r="3.5" class="accent-fill"/><line x1="230.0" y1="56.0" x2="490.0" y2="143.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#rs-zz)"/><text x="230.0" y="38.0" text-anchor="middle" class="math" font-size="13">r<tspan class="mrm" font-size="9" dy="3">2</tspan></text><text x="490.0" y="172.0" text-anchor="middle" class="math" font-size="13">s<tspan class="mrm" font-size="9" dy="3">2</tspan></text><circle cx="360.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="220.0" cy="150.0" r="3.5" class="accent-fill"/><line x1="220.0" y1="144.0" x2="360.0" y2="57.0" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 3" marker-end="url(#rs-zz)"/><text x="360.0" y="38.0" text-anchor="middle" class="math" font-size="13">r<tspan class="mrm" font-size="9" dy="3">3</tspan></text><text x="220.0" y="172.0" text-anchor="middle" class="math" font-size="13">s<tspan class="mrm" font-size="9" dy="3">3</tspan></text><circle cx="520.0" cy="50.0" r="3.5" class="accent-fill"/><circle cx="400.0" cy="150.0" r="3.5" class="accent-fill"/><line x1="520.0" y1="56.0" x2="400.0" y2="143.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#rs-zz)"/><text x="520.0" y="38.0" text-anchor="middle" class="math" font-size="13">r<tspan class="mrm" font-size="9" dy="3">4</tspan></text><text x="400.0" y="172.0" text-anchor="middle" class="math" font-size="13">s<tspan class="mrm" font-size="9" dy="3">4</tspan></text><text x="300.0" y="185.0" text-anchor="middle" class="label">solid: forth (next element of M); dashed: back (next element of N)</text></svg>
:::

:::quiz[the isomorphism theorem]
Which hypothesis of :ref{#thm-bf-isomorphism} does each back step use that the forth steps do not?

- [x] The inclusion $\mathrm{SSy}(N) \subseteq \mathrm{SSy}(M)$, so that the type of $n_k$ over $\bar s$, coded in $N$, is coded in $M$, and the recursive saturation of $M$, so that it is realized there.
- [ ] The equality of the theories.

  It is used once, to start the construction with the empty tuples; afterwards the inductive condition carries it.
- [ ] The countability of $N$.

  Countability is used by both kinds of steps, through the enumerations.
:::

The same proof with $N = M$ gives the **homogeneity** of countable recursively saturated models.

:::corollary{#cor-bf-homogeneous}
Let $M$ be a countable recursively saturated model of $\mathrm I\Delta_0 + \mathrm{exp}$, and $\bar a, \bar b \in M$ with $\mathrm{tp}(\bar a) = \mathrm{tp}(\bar b)$. There is an automorphism of $M$ mapping $\bar a$ to $\bar b$.
:::

Each hypothesis of the theorem is needed. Two models with different theories are not isomorphic, and neither are two models with different standard systems; the existence theorem below gives countable recursively saturated models of the same completion of $\mathrm{PA}$ with different standard systems. Recursive saturation cannot be dropped either: by :ref{#prop-rs-definable}, the elements of a recursively saturated model $M \models \mathrm{PA}$ that are definable without parameters form an elementary substructure that is not recursively saturated, and so it is not isomorphic to $M$, although the two models have the same theory.

## Models with prescribed invariants

A recursively saturated model $M$ of a completion $T$ of $\mathrm{PA}$ has a standard system that is a Scott set (:ref{#cor-ssy-scott-set}) containing $T$ (:ref{#prop-rs-realized-coded}). The converse adds to Scott's construction steps that realize types. We use one-variable types: in $\mathrm{PA}$, a type in $v_1, \dots, v_k$ is realized if and only if the type in one variable $w$ obtained by writing each $v_i$ as the $i$-th component of $w$, with the pairing of :ref{#fact-pairing}, is realized; and the second type is computable from the first.

:::theorem{#thm-bf-existence}
Let $\mathcal X$ be a countable Scott set and $T \in \mathcal X$ a complete consistent extension of $\mathrm{PA}$. There is a countable recursively saturated model $M$ of $T$ with $\mathrm{SSy}(M) = \mathcal X$.
:::

:::proof{of=thm-bf-existence}
We follow the proof of :ref{#thm-scott-converse}, with its constants $c_0, c_1, \dots$ and languages $\mathcal L_i$, and its fact that a consistent theory computable in a member of $\mathcal X$ has a complete consistent extension in $\mathcal X$. Enumerate $\mathcal X = \{ X_0, X_1, \dots \}$, and list all pairs $(m, \bar j)$, with $m \in \nat$ and $\bar j$ a finite tuple of indices, as $(m_0, \bar j_0), (m_1, \bar j_1), \dots$, each pair occurring infinitely often. We build complete consistent $\mathcal L_l$-theories $T = T_0 \subseteq T_1 \subseteq \cdots$ in $\mathcal X$.

- *Coding steps*, $l = 2i$: as in Scott's proof, $T_{l+1}$ is a complete extension in $\mathcal X$ of $T_l \cup \{ \bar k \in c_l : k \in X_i \} \cup \{ \neg\, \bar k \in c_l : k \notin X_i \}$.
- *Realizing steps*, $l = 2i + 1$: write $\bar c$ for the constants $c_j$, $j \in \bar j_i$, and read $X_{m_i}$ as a set of codes of formulas $\theta(v, \bar z)$. If every index in $\bar j_i$ is below $l$ and $S = T_l \cup \{ \theta(c_l, \bar c) : \ulcorner \theta \urcorner \in X_{m_i} \}$ is consistent, let $T_{l+1}$ be a complete extension of $S$ in $\mathcal X$, which exists since $S$ is computable in $T_l \oplus X_{m_i}$; otherwise, of $T_l$.

Let $N \models T_\omega = \bigcup_l T_l$, and $M$ the set of elements of $N$ definable in $\mathcal L_\omega$ without parameters. Exactly as in Scott's proof, $M \preccurlyeq N$, the reduct of $M$ to $\mathcal L_A$ is a model of $T$, and $\mathrm{SSy}(M) = \mathcal X$, by the coding steps; the realizing steps add only constants, which do not affect that argument.

By :ref{#thm-rs-coded-types}, it remains to realize every type $p(v, \bar d)$ over $M$ coded in $M$. Each $d_t$ is the only element of $N$ satisfying a formula $\psi_t(x, \bar c)$, with $\bar c$ finitely many constants. Let
$$
Y = \big\{ \ulcorner \exists \bar y\, \big( \textstyle\bigwedge_t \psi_t(y_t, \bar z) \wedge \theta(v, \bar y) \big) \urcorner : \theta(v, \bar d) \in p \big\}.
$$
It is computable from the set of codes of $p$, which belongs to $\mathrm{SSy}(M) = \mathcal X$, since $\theta$ can be read off the code; so $Y = X_m$ for some $m$. For each $\theta(v, \bar d) \in p$, the formula of $Y$ obtained from it holds of $v$ in $N$ if and only if $\theta(v, \bar d)$ does. Let $l$ be a realizing step handling the pair $(m, \bar j)$, where $\bar j$ lists the indices of $\bar c$, with $l$ above these indices. Every finite part of $S$ is consistent: for finitely many formulas $\theta_1, \dots, \theta_k$ of $p$, $M \models \exists v \bigwedge_q \theta_q(v, \bar d)$, so the corresponding $\mathcal L_l$-sentence $\exists v \bigwedge_q \theta'_q(v, \bar c)$ holds in $N$, hence belongs to the complete theory $T_l$; and $c_l$ does not occur in $T_l$. So $T_{l+1} \supseteq S$, and $c_l^N \in M$ satisfies $\theta(v, \bar d)$ in $N$, hence in $M$, for every $\theta(v, \bar d) \in p$.
:::

:::quiz[models with prescribed invariants]
In the proof of :ref{#thm-bf-existence}, why does each pair $(m, \bar j)$ have to occur infinitely often in the list?

- [x] A pair can be handled only at a step $l$ above the indices in $\bar j$, since the constants $\bar c$ must already be in $\mathcal L_l$; a pair occurring infinitely often occurs at such a step.
- [ ] Because a type must be realized infinitely often.

  One realizer suffices for each type.
- [ ] Because the consistency of $S$ may fail the first time and succeed later.

  For the types used in the proof, $S$ is consistent at every step above the indices of $\bar c$, as the last paragraph shows.
:::

## Classification

:::corollary{#cor-bf-classification}
Let $T$ be a complete consistent extension of $\mathrm{PA}$. The map $M \mapsto \mathrm{SSy}(M)$ induces a bijection between the isomorphism classes of countable recursively saturated models of $T$ and the countable Scott sets that contain $T$.
:::

:::proof{of=cor-bf-classification}
The standard system of such a model is a countable Scott set containing $T$, by :ref{#cor-ssy-scott-set} and :ref{#prop-rs-realized-coded}, and isomorphic models have the same standard system. The map is injective by :ref{#thm-bf-isomorphism}, all models having the theory $T$, and surjective by :ref{#thm-bf-existence}.
:::

For example, every set $Z \subseteq \nat$ belongs to a countable Scott set containing $T$: a countable ω-model of $\mathsf{WKL}_0$ containing $T \oplus Z$, as in :ref{to="big-five/wkl0"}. Each countable Scott set contains countably many sets, so there are $2^{\aleph_0}$ countable Scott sets containing $T$, and $2^{\aleph_0}$ countable recursively saturated models of $T$ up to isomorphism. For the theory of $\nat$, the Scott sets concerned are those containing $\mathrm{Th}(\nat)$, hence every arithmetic set, as in :ref{#ex-ssy-truth}.

## Exercises

::::exercise{difficulty=1}
Let $M \preccurlyeq N$ be countable recursively saturated models of $\mathrm{PA}$ with $M \subseteq_e N$. Show that $M \cong N$.

:::solution
The theories are equal since $M \preccurlyeq N$, and $\mathrm{SSy}(M) = \mathrm{SSy}(N)$ by :ref{#ex-ssy-end-extension}. Apply :ref{#thm-bf-isomorphism}.
:::
::::

::::exercise{#ex-bf-elementary-embedding difficulty=2}
Let $M$ and $N$ be countable recursively saturated models of $\mathrm{PA}$ with $\mathrm{Th}(M) = \mathrm{Th}(N)$ and $\mathrm{SSy}(M) \subseteq \mathrm{SSy}(N)$. Show that there is an elementary embedding of $M$ into $N$. Show that it cannot be surjective if the inclusion is strict.

:::solution
Run the construction of :ref{#thm-bf-isomorphism} with forth steps only; :ref{#lem-bf-step} applies with the inclusion $\mathrm{SSy}(M) \subseteq \mathrm{SSy}(N)$. The map $f$ is total, and it preserves every formula: if $M \models \theta(\bar r)$ for a tuple $\bar r$ of the domain, then $N \models \theta(f(\bar r))$ by the inductive condition. An elementary embedding that is surjective is an isomorphism, and isomorphic models have the same standard system.
:::
::::

## Notes and references

:ref{#thm-bf-isomorphism} and :ref{#cor-bf-homogeneous} are Wong's Theorem 8.3 and Remark 8.4, with the same back-and-forth proof; the classification by standard systems, which combines this theorem with Scott's theorem (1962), is treated in Kaye's book and in Kossak and Schmerl's. The proof of :ref{#thm-bf-existence} given here adds realizing steps to the construction of :ref{#thm-scott-converse}.

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 8.
- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in Recursive Function Theory, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
- R. Kossak and J. H. Schmerl, *The Structure of Models of Peano Arithmetic*, Oxford University Press, 2006.
