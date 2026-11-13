---
title: Minimal types and minimal end extensions
summary: Rare types, realized at most once in each gap; every model of PA has an unbounded strongly definable rare type, and the extension it generates is a minimal elementary end extension; minimal types are indiscernible, and iterating them along a linear order gives models whose automorphism group is that of the order.
duration: 45
prerequisites: [gaps]
---

By the previous lesson, an extension $M(p / d)$ by an unbounded strongly definable type consists of $M$ and of the gap of $d$. An elementary substructure strictly between $M$ and $M(p)$ could still exist, made of $M$ and a thinner part of the gap. Gaifman's idea is to choose $p$ so that it is realized at most once in each gap. Then every element $c$ of the gap of $d$ determines $d$ as the nearest realization of $p$, and a compactness argument turns "nearest" into "definable from $c$": any elementary substructure that meets the gap contains $d$. The types obtained are **minimal**: they give minimal elementary end extensions, and they are indiscernible, so that they can be realized along any linear order.

Throughout, $M$ is a model of $\mathrm{PA}$. Skolem functions and gaps are as in :ref{#def-ee-skolem} and :ref{#def-ee-gap}; for $K \models \mathrm{PA}$ and $A \subseteq K$, $\mathrm{cl}_K(A)$ denotes the set of values $t(\bar a)$ of Skolem functions at tuples of $A$, the definable closure of $A$, which is an elementary substructure of $K$ (:ref{#lem-ee-mp}).

## Rare types

:::definition[Kossak, Kotlarski, Schmerl]{#def-ee-rare}
A complete $M$-type $p(v)$ is **rare** if, for every $K \succcurlyeq M$ and all distinct $c, d \in K$ realizing $p$, $c \notin \mathrm{gap}(d)$.
:::

:::lemma{#lem-ee-rare-syntactic}
A complete $M$-type $p(v)$ is rare if and only if for every Skolem function $t(v)$ there is $\theta \in p$ with
$$
M \models \forall u\ \forall v\ \big( \theta(u) \wedge \theta(v) \wedge u < v \rightarrow t(u) < v \big).
$$
:::

:::proof{of=lem-ee-rare-syntactic}
($\Leftarrow$) Let $c \neq d$ realize $p$ in $K \succcurlyeq M$, with $c \in \mathrm{gap}(d)$; by symmetry of the criterion :ref{#lem-ee-gap-criterion}, assume $c < d$. Some Skolem $t$ satisfies $t(c) \geq d$. The sentence given for $t$ holds in $K$, and $\theta(c) \wedge \theta(d) \wedge c < d$, so $t(c) < d$, a contradiction.

($\Rightarrow$) Suppose that some $t$ has no such $\theta$. Then for every $\theta \in p$, $M \models \exists u\ \exists v\ (\theta(u) \wedge \theta(v) \wedge u < v \leq t(u))$. Since $p$ is closed under conjunction, the set $p(c) \cup p(d) \cup \{ c < d \leq t(c) \}$, together with the elementary diagram of $M$, is finitely satisfiable, and some $K \succcurlyeq M$ contains realizations $c < d$ of $p$ with $t(c) \geq d$. The identity gives $d \geq c$, so $c \in \mathrm{gap}(d)$ by :ref{#lem-ee-gap-criterion}, and $p$ is not rare.
:::

The sentence of the lemma is preserved by elementary extensions, so every extension of a rare type to an elementary extension of $M$ is rare.

:::lemma{#lem-ee-far}
Let $S \subseteq M$ be unbounded and $F : M \to M$ a function, both definable. There is an unbounded definable $H \subseteq S$ such that $F(u) < v$ for all $u < v$ in $H$.
:::

:::proof{of=lem-ee-far}
Define by recursion in $M$: $h_0 = \min S$ and $h_{i+1} = \min \{ v \in S : v > h_i \wedge v > F(h_i) \}$, which exists since $S$ is unbounded. Let $H = \{ h_i : i \in M \}$. The sequence is strictly increasing, so $H$ is unbounded, and if $u = h_i < v = h_j$, then $j \geq i + 1$ and $v \geq h_{i+1} > F(h_i)$.
:::

:::theorem[Gaifman]{#thm-ee-minimal-exists}
Every model $M$ of $\mathrm{PA}$ has an unbounded complete $M$-type that is strongly definable and rare.
:::

:::proof{of=thm-ee-minimal-exists}
Follow the proof of :ref{#thm-ee-gaifman-sd}, with a chain $M = S_0 \supseteq S_1 \supseteq \cdots$ of unbounded definable sets, and also enumerate the Skolem functions of one variable as $t_0, t_1, \dots$. At step $2i$, obtain $S_{2i+1} \subseteq S_{2i}$ cohesive for the family defined by $\varphi_i$, by :ref{#lem-ee-cohesive}; at step $2i+1$, obtain $S_{2i+2} \subseteq S_{2i+1}$ by :ref{#lem-ee-far} with $F = t_i$. Let $p$ consist of the formulas $\psi$ with $S_j \subseteq^* \psi(M)$ for some $j$. As before, $p$ is an unbounded complete type. A subset of a cohesive set is cohesive, so the formula defining $S_{2i+1}$, and also every later $S_j$, witnesses strong definability for $\varphi_i$. The formula $\theta$ defining $S_{2i+2}$ is in $p$ and satisfies the condition of :ref{#lem-ee-rare-syntactic} for $t_i$; so $p$ is rare.
:::

:::definition{#def-ee-minimal-type}
A complete $M$-type is **minimal** if it is unbounded, strongly definable and rare.
:::

## Minimal end extensions

:::lemma{#lem-ee-rare-definable}
Let $p$ be a rare complete $M$-type, $K \succcurlyeq M$, $d \in K$ realizing $p$, and $c \in \mathrm{gap}(d)$. Then $d \in \mathrm{cl}_K(M \cup \{c\})$.
:::

:::proof{of=lem-ee-rare-definable}
*Case $c \leq d$.* By :ref{#lem-ee-gap-criterion}, $t(c) \geq d$ for some Skolem $t$; let $t^*$ be its increasing majorant. By :ref{#lem-ee-rare-syntactic}, some $\theta(v, \bar m) \in p$, with $\bar m \in M$, satisfies the condition for $t^*$, which holds in $K$. If $c \leq v' < d$ and $\theta(v', \bar m)$, then $t^*(v') \geq t^*(c) > t(c) \geq d$, contradicting $t^*(v') < d$. So $d$ is the least $v \geq c$ with $\theta(v, \bar m)$, a Skolem function of $c$ and $\bar m$.

*Case $d < c$.* Some Skolem $t$ satisfies $t(d) \geq c$; take $\theta$ for $t^*$ as before. If $d < v' < c$ and $\theta(v', \bar m)$, then $t^*(d) < v' < c \leq t(d)$, a contradiction. So $d$ is the largest $v < c$ with $\theta(v, \bar m)$.
:::

:::figure[The proof of :ref{#lem-ee-rare-definable}. Rarity makes consecutive solutions of $\theta$ far apart, beyond the reach of $t^*$. If $c$ is in the gap of $d$, no solution of $\theta$ lies between them, and $d$ is the nearest solution of $\theta$ on the appropriate side of $c$.]
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="Consecutive solutions of theta are far apart; if c lies in the gap of d, no solution of theta lies between c and d, so d is the least solution of theta above c"><line x1="20.0" y1="80.0" x2="580.0" y2="80.0" class="ink-stroke" stroke-width="1.2"/><circle cx="60.0" cy="80.0" r="4" class="node"/><circle cx="330.0" cy="80.0" r="4" class="node"/><text x="60.0" y="66.0" text-anchor="middle" class="math" font-size="13">v′</text><path d="M60,88 C120,130 240,130 300,88" class="accent-stroke" fill="none" stroke-width="1.4"/><text x="180.0" y="138.0" text-anchor="middle" class="label">t*(v′) &lt; next solution</text><circle cx="250.0" cy="80.0" r="4" class="ink-fill"/><text x="250.0" y="66.0" text-anchor="middle" class="math" font-size="14">c</text><circle cx="330.0" cy="80.0" r="5" class="accent-fill"/><text x="330.0" y="66.0" text-anchor="middle" class="math" font-size="14">d</text><circle cx="540.0" cy="80.0" r="4" class="node"/><path d="M240.0,52.0 L240.0,46.0 L470.0,46.0 L470.0,52.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="355.0" y="36.0" text-anchor="middle" class="label">gap(d)</text><text x="410.0" y="110.0" text-anchor="middle" class="label">no solution of θ in [c, d)</text><text x="300.0" y="150.0" text-anchor="middle" class="label">discs: solutions of θ; d = (min v ≥ c) θ(v)</text></svg>
:::

:::definition{#def-ee-minimal-extension}
An elementary extension $M \preccurlyeq N$ is **minimal** if $M \neq N$ and there is no $K$ with $M \preccurlyeq K \preccurlyeq N$, $M \neq K \neq N$.
:::

:::theorem[Gaifman]{#thm-ee-minimal-extension}
If $p$ is a minimal $M$-type, then $M(p)$ is a minimal elementary end extension of $M$. Every model of $\mathrm{PA}$ has a minimal elementary end extension.
:::

:::proof{of=thm-ee-minimal-extension}
$M(p) = M(p / d)$ is a proper elementary end extension by :ref{#cor-ee-definable-end} and :ref{#lem-ee-strongly-definable-definable}. Let $M \preccurlyeq K \preccurlyeq M(p)$. By :ref{#prop-ee-one-gap}, $M(p) = M \cup \mathrm{gap}(d)$. If $K$ does not meet $\mathrm{gap}(d)$, then $K = M$. If $c \in K \cap \mathrm{gap}(d)$, then $d = t(c, \bar m)$ for a Skolem function $t$ and $\bar m \in M$, by :ref{#lem-ee-rare-definable}; since $K \preccurlyeq M(p)$ contains $c$ and $\bar m$, it contains $d$, and then every element $t'(d, \bar m')$ of $M(p)$. So $K = M(p)$. The second statement follows from :ref{#thm-ee-minimal-exists}.
:::

:::quiz[minimal end extensions]
Which property of $p$ is used for each half of the proof?

- [x] Strong definability, through :ref{#prop-ee-one-gap}, shows that an elementary substructure that misses the gap of $d$ is $M$; rarity, through :ref{#lem-ee-rare-definable}, shows that one that meets it contains $d$.
- [ ] Rarity shows that $M(p)$ is an end extension.

  The end extension property comes from definability (:ref{#cor-ee-definable-end}).
- [ ] Strong definability shows that $d$ is definable from every element of its gap.

  This is rarity: with only strong definability, the gap may contain other realizations of $p$, and an elementary substructure generated by one of them need not contain $d$.
:::

Every minimal elementary extension $N$ of a model of $\mathrm{PA}$ is an end extension or a cofinal extension, since $\sup_N M$ lies elementarily between $M$ and $N$ (:ref{#ex-sup-elementary}). Blass (1974) showed that every countable non-standard model of $\mathrm{PA}$ has a minimal elementary cofinal extension; whether every model of $\mathrm{PA}$ has one is open (Kossak and Schmerl, Chapter 12, Question 2, as reported by Wong). Conversely, minimality of all extensions by unbounded extensions of $p$ forces $p$ to be strongly definable and rare (Wong, Proposition 11.12, citing Kossak and Schmerl).

## Indiscernibility and iterated extensions

:::proposition{#prop-ee-indiscernible}
Let $p$ be a minimal $M$-type, $K \succcurlyeq M$, and $c_0 < \cdots < c_n$, $d_0 < \cdots < d_n$ elements of $K$ realizing $p$. Then $(c_0, \dots, c_n)$ and $(d_0, \dots, d_n)$ have the same type over $M$.
:::

:::proof{of=prop-ee-indiscernible}
By induction on $n$. For $n = 0$, both types are $p$. Assume the statement for $n$, and let $c_0 < \cdots < c_{n+1}$ and $d_0 < \cdots < d_{n+1}$ realize $p$; write $\bar c = (c_0, \dots, c_n)$ and $\bar d = (d_0, \dots, d_n)$. Let $\varphi(\bar v, v_{n+1}, w)$ be a formula and $a \in M$. By strong definability, applied to $\varphi$ as a formula in $v_{n+1}$ with parameters $(\bar v, w)$, there is $\theta(v, b) \in p$, with $b \in M$, such that $M$ satisfies, for all $\bar v, w$,
$$
\exists u\ \Big( \forall v' \geq u\ \big(\theta(v', b) \rightarrow \varphi(\bar v, v', w)\big) \vee \forall v' \geq u\ \big(\theta(v', b) \rightarrow \neg \varphi(\bar v, v', w)\big) \Big).
$$
Let $t(\bar v, w, z)$ be the least such $u$ with $b$ replaced by $z$ ($0$ if none), and $t'(\bar v) = \max_{w, z \leq v_0} t(\bar v, w, z)$, a Skolem function. The property inside $\exists u$ is preserved when $u$ increases, and $a, b \in M$ are below $c_0$ and $d_0$; so, in $K$, it holds at $u = t'(\bar c)$ for $\bar v = \bar c$, $w = a$, $z = b$, and at $u = t'(\bar d)$ for $\bar d$.

By rarity, $t'(\bar c) < c_{n+1}$: with the one-variable Skolem function $T(x) = \max_{\bar y \leq x} t'(\bar y)$, $t'(\bar c) \leq T(c_n)$, and :ref{#lem-ee-rare-syntactic} for $T$ gives $T(c_n) < c_{n+1}$. Similarly $t'(\bar d) < d_{n+1}$.

Suppose $K \models \varphi(\bar c, c_{n+1}, a)$. Since $c_{n+1} \geq t'(\bar c)$ and $K \models \theta(c_{n+1}, b)$, the second disjunct fails at $\bar c$, so $K \models \psi(\bar c)$, where $\psi(\bar v)$ is $\forall v' \geq t'(\bar v)\ (\theta(v', b) \rightarrow \varphi(\bar v, v', a))$, a formula with parameters $a, b \in M$. By the induction hypothesis, $K \models \psi(\bar d)$, and with $d_{n+1} \geq t'(\bar d)$ and $\theta(d_{n+1}, b)$, $K \models \varphi(\bar d, d_{n+1}, a)$. The converse is symmetric.
:::

:::theorem[Gaifman]{#thm-ee-linear-order}
Let $p$ be a minimal $M$-type and $(I, <)$ a linear order. There are $K \succcurlyeq M$ and elements $d_i \in K$, $i \in I$, such that, with $D = \{ d_i : i \in I \}$:

1. $K = \mathrm{cl}_K(M \cup D)$;
2. $d_i < d_j$ if and only if $i < j$;
3. $K = M \cup \bigcup_{i \in I} \mathrm{gap}(d_i)$;
4. the elements of $K$ that realize $p$ are exactly the $d_i$.
:::

:::proof{of=thm-ee-linear-order}
The elementary diagram of $M$, the sets $p(d_i)$ and the sentences $d_i < d_j$ for $i < j$ are finitely satisfiable: a finite part involves finitely many formulas of $p$, whose conjunction $\theta$ defines an unbounded set, and finitely many indices, to which increasing solutions of $\theta$ in $M$ can be assigned. Let $K' \succcurlyeq M$ satisfy them, and $K = \mathrm{cl}_{K'}(M \cup D) \preccurlyeq K'$. Items 1 and 2 hold.

For 3, let $c \in K$; then $c \in K_0 = \mathrm{cl}_K(M \cup \{ d_{i_0}, \dots, d_{i_n} \})$ for some $i_0 < \cdots < i_n$. Let $N_0 = M$ and $N_{k+1} = \mathrm{cl}_K(N_k \cup \{ d_{i_k} \})$. Every element of $N_k$, $k \geq 1$, is $t(\bar m, d_{i_0}, \dots, d_{i_{k-1}})$ with $\bar m \in M$, so it is at most $T(d_{i_{k-1}})$ for the one-variable Skolem function $T(x) = \max_{\bar y \leq x} t(\bar y)$, since $\bar m < d_{i_0}$; and $T(d_{i_{k-1}}) < d_{i_k}$ by rarity. So $d_{i_k} > N_k$, and its type over $N_k$ is an unbounded extension of $p$, strongly definable by :ref{#ex-ee-sd-preserved}. By :ref{#prop-ee-one-gap}, $N_{k+1} = N_k \cup \mathrm{gap}^{N_{k+1}}(d_{i_k})$. Hence $K_0 = N_{n+1} = M \cup \bigcup_{k \leq n} \mathrm{gap}^{K_0}(d_{i_k})$, and gaps are the same in $K_0$ and in $K$ (remark after :ref{#lem-ee-gap-criterion}). So $c \in M$ or $c \in \mathrm{gap}^K(d_{i_k})$ for some $k$.

For 4, let $c \in K$ realize $p$. Then $c \notin M$, as $p$ is unbounded, so $c \in \mathrm{gap}(d_i)$ for some $i$ by 3, and $c = d_i$ by rarity.
:::

:::corollary[Gaifman]{#cor-ee-automorphisms}
For every complete extension $T$ of $\mathrm{PA}$ and every linear order $(I, <)$, there is a model $K$ of $T$ whose automorphism group is isomorphic to the automorphism group of $(I, <)$.
:::

:::proof{of=cor-ee-automorphisms}
Let $N \models T$, and let $M$ be the set of elements of $N$ definable without parameters; $M \preccurlyeq N$ by :ref{#lem-ee-mp}, and every element of $M$ is definable without parameters in $M$. Let $p$ be a minimal $M$-type and $K$ given by :ref{#thm-ee-linear-order}. Then $K \models T$, and $K = \mathrm{cl}_K(D)$, since $M = \mathrm{cl}_K(\emptyset)$.

An automorphism $g$ of $K$ fixes the elements of $M$, which are definable without parameters in $K$; so it preserves the formulas of $p$, maps $D$ onto $D$ by item 4, and preserves the order. Let $\hat g(i) = j$ when $g(d_i) = d_j$; $\hat g$ is an automorphism of $(I, <)$, and $g \mapsto \hat g$ is a group homomorphism. It is injective: an automorphism that fixes $D$ fixes $\mathrm{cl}_K(D) = K$. It is onto: given an automorphism $f$ of $(I, <)$, set $g(t(d_{i_0}, \dots, d_{i_n})) = t(d_{f(i_0)}, \dots, d_{f(i_n)})$ for $i_0 < \cdots < i_n$. Two descriptions of elements, and any formula about them, involve finitely many indices, which can be listed in increasing order; $f$ maps this list to an increasing list, and by :ref{#prop-ee-indiscernible} the two tuples have the same type. So $g$ is well defined and elementary, and it is a bijection, with inverse given by $f^{-1}$.
:::

With $(I, <)$ an infinite cardinal, which has no non-trivial automorphism, every completion of $\mathrm{PA}$ has rigid models of every infinite cardinality: $K = \mathrm{cl}_K(D)$ has the cardinality of $I$. Gaifman also obtained, from the same models, that for every set $I$ the lattice of elementary substructures of a suitable model of $T$ is isomorphic to the Boolean algebra of subsets of $I$; we state this without proof (Wong, Corollary 11.13). Schmerl (2002) extended the corollary to a much larger class of groups (Wong, Further comments to Lecture 11).

## Exercises

::::exercise{#ex-ee-rare-extension difficulty=1}
Show that every extension of a minimal $M$-type to an elementary extension of $M$ that is unbounded is minimal.

:::solution
Strong definability is preserved by :ref{#ex-ee-sd-preserved}, and rarity because the sentences of :ref{#lem-ee-rare-syntactic} hold in every elementary extension.
:::
::::

## Notes and references

Rare types are named by Kossak, Kotlarski and Schmerl (1993); Wong's Lecture 11 gives :ref{#lem-ee-rare-syntactic} (Lemma 11.1), the principle of :ref{#lem-ee-far} (Lemma 11.2, $\mathrm{FAR}$), :ref{#thm-ee-minimal-exists} (Theorem 11.4), :ref{#lem-ee-rare-definable} (Lemma 11.5), :ref{#thm-ee-minimal-extension} (Theorem 11.6), :ref{#prop-ee-indiscernible} (Proposition 11.7, following Kossak and Schmerl, Lemma 3.1.19), :ref{#thm-ee-linear-order} (Theorem 11.10) and :ref{#cor-ee-automorphisms} (Corollary 11.14); the results are due to Gaifman (1976). In :ref{#lem-ee-rare-definable} we use the increasing majorant $t^*$ of a single Skolem function instead of Wong's majorizing sequence of all Skolem functions.

- H. Gaifman, *Models and types of Peano's arithmetic*, Annals of Mathematical Logic 9 (1976), 223–306.
- R. Kossak, H. Kotlarski and J. H. Schmerl, *On maximal subgroups of the automorphism group of a countable recursively saturated model of PA*, Annals of Pure and Applied Logic 65 (1993), 125–148.
- A. Blass, *On certain types and models for arithmetic*, Journal of Symbolic Logic 39 (1974), 151–162.
- J. H. Schmerl, *Automorphism groups of models of Peano arithmetic*, Journal of Symbolic Logic 67 (2002), 1249–1264.
- R. Kossak and J. H. Schmerl, *The Structure of Models of Peano Arithmetic*, Oxford Logic Guides 50, Clarendon Press, 2006.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 11.
