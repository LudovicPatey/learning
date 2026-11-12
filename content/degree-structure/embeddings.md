---
title: Embedding partial orders
summary: The columns of a 1-generic set are computably independent; a computable partial order contains a copy of every countable partial order; hence every countable partial order embeds into the Turing degrees below 0′; there is an antichain of continuum many degrees.
duration: 50
prerequisites: [exact-pairs, turing-degrees/finite-extensions]
---

The previous lesson showed what $\mathcal D$ lacks: least upper bounds of increasing sequences, and greatest lower bounds. This lesson shows what it contains: a copy of every countable partial order, already below $\obf'$. Each element of the order is coded by the join of some members of a sequence of sets none of which is computable from the others. The proof has two ingredients of independent interest: such an independent sequence, obtained from the columns of a 1-generic set, and a computable partial order that contains a copy of every countable partial order, since the coding needs to decide the order relation. The lesson ends with an antichain of continuum many degrees, built by a perfect tree of finite extensions.

An **embedding** of a partial order $(P, \leq_P)$ into $\mathcal D$ is an injective map $f : P \to \mathcal D$ with $p \leq_P q$ if and only if $f(p) \leq f(q)$. A map that only preserves the order is not enough: the constant map with value $\obf$ preserves every order. The difficulty is in the converse direction, which requires many non-reductions.

## Independent sets

:::definition{#def-independent}
A sequence of sets $(X_n)_{n \in \nat}$ is **computably independent** if $X_i \not\leq_T \bigoplus_{k \neq i} X_k$ for every $i$, where $\bigoplus_{k \neq i} X_k$ is the set whose column $k$ is $X_k$ for $k \neq i$ and whose column $i$ is empty.
:::

For example, a sequence containing a computable set, or the same set twice, is not independent; nor is $\emptyset, \emptyset', \emptyset'', \dots$, since each term computes the previous ones. Finite extensions give independent sequences directly (Soare, Exercise 6.1.4); here they come from genericity. The idea is that a 1-generic set chooses the bits of column $i$ freely, so a reduction that reads only the other columns cannot predict them: at any stage, the bit it predicts at a new position of column $i$ can be flipped.

For a set or string $\sigma$, write $\sigma^{\neq i}$ for the set or string obtained by replacing every bit at a position $\langle i, y \rangle$ with $0$. For a set $G$, $G^{\neq i} = \bigoplus_{k \neq i} G^{[k]}$.

:::theorem{#thm-generic-independent}
If $G$ is 1-generic, its columns $G^{[0]}, G^{[1]}, \dots$ are computably independent.
:::

:::proof{of=thm-generic-independent}
Suppose that $\Phi^{G^{\neq i}}_e = G^{[i]}$ for some $i$ and $e$. Let $W$ be the c.e. set of strings $\sigma$ for which some position $\langle i, y \rangle < |\sigma|$ satisfies $\Phi^{\sigma^{\neq i}}_e(y)\converge \neq \sigma(\langle i, y \rangle)$. Since $G$ is 1-generic (:ref{#def-1-generic}), some prefix $\sigma$ of $G$ belongs to $W$ or has no extension in $W$.

If $\sigma \prec G$ belongs to $W$, then $\sigma^{\neq i} \prec G^{\neq i}$, so $\Phi^{G^{\neq i}}_e(y) = \Phi^{\sigma^{\neq i}}_e(y) \neq \sigma(\langle i, y \rangle) = G^{[i]}(y)$ for some $y$, a contradiction.

Suppose that $\sigma \prec G$ has no extension in $W$. Choose $y$ with $\langle i, y \rangle \geq |\sigma|$. Since $\Phi^{G^{\neq i}}_e(y)$ converges, there is $m > \langle i, y \rangle$ with $\Phi^{G^{\neq i} \uh m}_e(y)\converge = v$. Let $\tau$ be $G \uh m$ with the bit at position $\langle i, y \rangle$ replaced by $1 - v$. Then $\tau$ extends $\sigma$, because $\langle i, y \rangle \geq |\sigma|$, and $\tau^{\neq i} = G^{\neq i} \uh m$, because the modified position is in column $i$. So $\Phi^{\tau^{\neq i}}_e(y)\converge = v \neq \tau(\langle i, y \rangle)$, and $\tau \in W$, a contradiction.
:::

:::quiz[independent columns]
In the proof of :ref{#thm-generic-independent}, why does the modified string $\tau$ satisfy $\tau^{\neq i} = G^{\neq i} \uh m$?

- [x] Because $\tau$ differs from $G \uh m$ only at a position of column $i$, and the operation $\sigma \mapsto \sigma^{\neq i}$ erases column $i$.
- [ ] Because $\tau$ extends $\sigma$.

  Extending $\sigma$ is needed to contradict the choice of $\sigma$; the equality comes from the position of the modification.
- [ ] Because $G$ is 1-generic.

  The equality is a property of strings, independent of genericity.

---

Why is $y$ chosen with $\langle i, y \rangle \geq |\sigma|$?

- [x] So that the bit that is flipped lies beyond $\sigma$, and the modified string still extends $\sigma$.
- [ ] So that $\Phi^{G^{\neq i}}_e(y)$ converges.

  It converges for every $y$, by hypothesis.
- [ ] So that $y$ belongs to $G^{[i]}$.

  The value of $G^{[i]}(y)$ plays no role; the flipped bit is chosen opposite to the computed value.
:::

## A universal countable partial order

The coding into columns needs to decide the order relation, so we first embed every countable partial order into a single computable one. A greedy construction suffices if the target order can always realize a new point with prescribed relations to finitely many given points.

A partial order $(Q, \leq)$ has the **extension property** if for every finite $F \subseteq Q$ and every partial order on $F \cup \{ p \}$, with $p$ a new element, that extends the order of $F$, there is $q \in Q \setminus F$ with $a \leq q \iff a \leq p$ and $q \leq a \iff p \leq a$ for every $a \in F$.

:::lemma{#lem-extension-universal}
If $(Q, \leq)$ has the extension property, every countable partial order embeds into it.
:::

For instance, $(\mathbb Q, <)$ lacks the extension property: no rational is incomparable with $0$. An infinite antichain lacks it as well: no element lies above a given one. The lemma fails for both, since neither contains a two-element chain together with an incomparable element.

:::proof{of=lem-extension-universal}
Let $P = \{ p_0, p_1, \dots \}$. Define $f(p_n)$ by induction. Given $f(p_0), \dots, f(p_{n-1})$, preserving the order and its negation on $\{ p_0, \dots, p_{n-1} \}$, let $F$ be the image, and transport the order of $\{ p_0, \dots, p_n \}$ to $F \cup \{ p \}$ through $f$ and $p_n \mapsto p$. By the extension property, there is $q \in Q \setminus F$ realizing the same relations with $F$; let $f(p_n) = q$. The map $f$ is injective, since $q \notin F$, and preserves the order in both directions.
:::

:::lemma{#lem-computable-universal}
There is a computable partial order on $\nat$ with the extension property.
:::

:::proof{of=lem-computable-universal}
A one-point extension of a finite part $F$ of a partial order is determined by the sets $L = \{ a \in F : a < p \}$ and $V = \{ a \in F : p < a \}$. These sets define a partial order on $F \cup \{ p \}$ extending that of $F$ if and only if $L$ is closed downward in $F$, $V$ is closed upward in $F$, $L \cap V = \emptyset$, and $a \leq b$ for all $a \in L$ and $b \in V$. Call such a triple $(F, L, V)$ **consistent** with the order of $F$.

Fix a computable list of all triples of finite subsets of $\nat$ in which each triple appears infinitely often. We build the order $\preceq$ on $\nat$ by adding the element $s$ at stage $s$, deciding its relations with $0, \dots, s - 1$ once and for all. At stage $s$, let $(F, L, V)$ be the $s$-th triple of the list. If $F \subseteq \{ 0, \dots, s-1 \}$ and the triple is consistent with the current order on $F$, let
$$
y \prec s \iff y \preceq a \text{ for some } a \in L, \qquad s \prec y \iff b \preceq y \text{ for some } b \in V,
$$
for $y < s$, and $s$ is incomparable with the other elements. Otherwise $s$ is incomparable with all $y < s$.

*The order remains a partial order.* Let $D$ and $E$ be the sets of elements below and above $s$. $D$ is closed downward and $E$ upward. They are disjoint: $b \preceq y \preceq a$ with $a \in L$, $b \in V$ would give $b \preceq a$, while $a \preceq b$ by consistency, so $a = b \in L \cap V$. Transitivity through $s$ holds: if $y \prec s \prec z$, then $y \preceq a \preceq b \preceq z$ for some $a \in L$, $b \in V$, so $y \preceq z$, and $y \neq z$ since $D \cap E = \emptyset$.

*The new element realizes the triple.* For $a \in F$, $a \prec s$ if and only if $a \preceq a'$ for some $a' \in L$, if and only if $a \in L$, since $L$ is closed downward in $F$. Similarly $s \prec a$ if and only if $a \in V$.

The relation $\preceq$ is computable, since the relations of $s$ with smaller elements are decided at stage $s$ by a finite computation. A consistent triple $(F, L, V)$ appears at some stage $s$ with $F \subseteq \{ 0, \dots, s-1 \}$, and $s \notin F$ realizes it.
:::

## The embedding theorem

:::theorem[Kleene, Post; Sacks]{#thm-embedding}
Every countable partial order embeds into the Turing degrees below $\obf'$.
:::

:::proof{of=thm-embedding}
By :ref{#lem-extension-universal} and :ref{#lem-computable-universal}, it suffices to embed the computable partial order $(\nat, \preceq)$. Let $G$ be a 1-generic set computable in $\emptyset'$ (:ref{#prop-1-generic}), and $G_m = G^{[m]}$. For each $n$, let
$$
D_n = \{ \langle m, y \rangle : m \preceq n,\ y \in G_m \},
$$
the set whose column $m$ is $G_m$ if $m \preceq n$, and empty otherwise. Each $D_n$ is computable in $G$, hence in $\emptyset'$.

If $m \preceq n$, then $D_m \leq_T D_n$: the column $k$ of $D_m$ is the column $k$ of $D_n$ if $k \preceq m$, since then $k \preceq n$, and is empty otherwise, and $\preceq$ is computable.

If $m \not\preceq n$, then $G_m \leq_T D_m$, since $m \preceq m$, and $D_n \leq_T G^{\neq m}$, since column $m$ is empty in $D_n$ and $\preceq$ is computable. So $D_m \leq_T D_n$ would give $G_m \leq_T G^{\neq m}$, contradicting :ref{#thm-generic-independent}.

So $n \mapsto \deg_T(D_n)$ preserves the order in both directions, and is injective since $\preceq$ is antisymmetric.
:::

:::figure[The coding of the proof of :ref{#thm-embedding} on the four-element order $0 \preceq 1, 2 \preceq 3$. The set $D_n$ keeps the columns $G_m$ with $m \preceq n$ and empties the others. For instance $D_1 \not\leq_T D_2$: $D_1$ computes $G_1$, while $D_2$ is computable from the columns other than $1$.]
<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="Left: the diamond order with 0 below 1 and 2, and 1 and 2 below 3. Right: the sets D_0 to D_3; the column m of D_n is the column G_m of a 1-generic set if m precedes n, and is empty otherwise"><line x1="110" y1="190" x2="60" y2="115" class="ink-stroke" stroke-width="1.3"/><line x1="110" y1="190" x2="160" y2="115" class="ink-stroke" stroke-width="1.3"/><line x1="60" y1="115" x2="110" y2="40" class="ink-stroke" stroke-width="1.3"/><line x1="160" y1="115" x2="110" y2="40" class="ink-stroke" stroke-width="1.3"/><circle cx="110" cy="190" r="13" class="node"/><text x="110" y="195" text-anchor="middle" class="mrm" font-size="14">0</text><circle cx="60" cy="115" r="13" class="node"/><text x="60" y="120" text-anchor="middle" class="mrm" font-size="14">1</text><circle cx="160" cy="115" r="13" class="node"/><text x="160" y="120" text-anchor="middle" class="mrm" font-size="14">2</text><circle cx="110" cy="40" r="13" class="node"/><text x="110" y="45" text-anchor="middle" class="mrm" font-size="14">3</text><text x="110" y="214" text-anchor="middle" class="label">the order ⪯</text><text x="363.0" y="22" text-anchor="middle" class="label">column 0</text><text x="429.0" y="22" text-anchor="middle" class="label">column 1</text><text x="495.0" y="22" text-anchor="middle" class="label">column 2</text><text x="561.0" y="22" text-anchor="middle" class="label">column 3</text><text x="308" y="174.0" text-anchor="middle" class="math" font-size="15">D<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="330" y="156" width="62" height="30" class="cell head-cell"/><text x="361.0" y="174.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">0</tspan></text><rect x="396" y="156" width="62" height="30" class="cell"/><text x="427.0" y="176.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><rect x="462" y="156" width="62" height="30" class="cell"/><text x="493.0" y="176.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><rect x="528" y="156" width="62" height="30" class="cell"/><text x="559.0" y="176.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><text x="308" y="132.0" text-anchor="middle" class="math" font-size="15">D<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="330" y="114" width="62" height="30" class="cell head-cell"/><text x="361.0" y="132.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">0</tspan></text><rect x="396" y="114" width="62" height="30" class="cell head-cell"/><text x="427.0" y="132.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">1</tspan></text><rect x="462" y="114" width="62" height="30" class="cell"/><text x="493.0" y="134.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><rect x="528" y="114" width="62" height="30" class="cell"/><text x="559.0" y="134.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><text x="308" y="90.0" text-anchor="middle" class="math" font-size="15">D<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="330" y="72" width="62" height="30" class="cell head-cell"/><text x="361.0" y="90.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">0</tspan></text><rect x="396" y="72" width="62" height="30" class="cell"/><text x="427.0" y="92.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><rect x="462" y="72" width="62" height="30" class="cell head-cell"/><text x="493.0" y="90.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">2</tspan></text><rect x="528" y="72" width="62" height="30" class="cell"/><text x="559.0" y="92.0" text-anchor="middle" class="mrm muted" font-size="14">∅</text><text x="308" y="48.0" text-anchor="middle" class="math" font-size="15">D<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="330" y="30" width="62" height="30" class="cell head-cell"/><text x="361.0" y="48.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">0</tspan></text><rect x="396" y="30" width="62" height="30" class="cell head-cell"/><text x="427.0" y="48.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">1</tspan></text><rect x="462" y="30" width="62" height="30" class="cell head-cell"/><text x="493.0" y="48.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">2</tspan></text><rect x="528" y="30" width="62" height="30" class="cell head-cell"/><text x="559.0" y="48.0" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">3</tspan></text></svg>
:::

The computability of $\preceq$ is used in both directions: to extract the columns of $D_m$ from $D_n$, and to see that $D_n$ is computable from the columns other than $m$. An arbitrary countable partial order may be far from computable, and the universal computable order removes this difficulty.

:::quiz[the embedding theorem]
In the proof of :ref{#thm-embedding}, why is the computable order $(\nat, \preceq)$ embedded, rather than the given partial order directly?

- [x] Because the reductions $D_m \leq_T D_n$ and $D_n \leq_T G^{\neq m}$ need to decide the order relation, which may not be computable for an arbitrary countable order.
- [ ] Because a countable partial order may be uncountable.

  Countable orders are countable; the issue is the complexity of their order relation.
- [ ] Because 1-generic sets have only computably many columns.

  A 1-generic set has infinitely many columns, all independent.

---

Where is the independence of the columns used?

- [x] To show that $D_m \not\leq_T D_n$ when $m \not\preceq n$: $D_m$ computes $G_m$, while $D_n$ is computable from the other columns.
- [ ] To show that $D_m \leq_T D_n$ when $m \preceq n$.

  This direction only uses the definition of $D_n$ and the computability of $\preceq$.
- [ ] To show that $D_n \leq_T \emptyset'$.

  This follows from $G \leq_T \emptyset'$.
:::

## An antichain of size continuum

The degrees also contain antichains of the largest possible size. The proof replaces the sequence of strings of the Kleene–Post construction (:ref{#thm-kleene-post}) by a binary tree of strings, so that every path of the tree defines a set; the requirements diagonalize between any two nodes of the same level, hence between any two paths. This method of **perfect trees of finite extensions** is used again for continuum many minimal degrees in the last lesson.

:::theorem[Lacombe, Sacks]{#thm-continuum-antichain}
There is a family $(X_Z)_{Z \in \cs}$ of sets such that $X_Z$ and $X_{Z'}$ are Turing incomparable whenever $Z \neq Z'$.
:::

:::proof{of=thm-continuum-antichain}
We define strings $\sigma_\rho$, for $\rho \in \bstr$, with $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ incomparable extensions of $\sigma_\rho$, and set $X_Z = \bigcup_n \sigma_{Z \uh n}$.

Let $\sigma_\varepsilon = \varepsilon$. Suppose that $\sigma_\rho$ is defined for all $\rho$ of length $n$. We modify these finitely many strings by finitely many extension steps, one for each $e < n$ and each ordered pair $(\rho, \rho')$ of distinct strings of length $n$. In the step for $(e, \rho, \rho')$, let $x = |\sigma_{\rho'}|$. If some $\tau \succeq \sigma_\rho$ has $\Phi^\tau_e(x)\converge = v$, replace $\sigma_\rho$ by $\tau$ and $\sigma_{\rho'}$ by $\sigma_{\rho'} b$, where $b \in \{0, 1\}$ is a bit different from $v$. Otherwise leave the strings unchanged; then $\Phi^Y_e(x)\diverge$ for every $Y \succeq \sigma_\rho$, by the use principle. In both cases, $\Phi^Y_e \neq X$ for all $Y \succeq \sigma_\rho$ and $X \succeq \sigma_{\rho'}$, and this remains true after further extensions. After all steps, let $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ be the final strings for $\rho$ followed by $0$ and by $1$.

Let $Z \neq Z'$, and $e \in \nat$. For $n > e$ larger than the first position where $Z$ and $Z'$ differ, $\rho = Z \uh n$ and $\rho' = Z' \uh n$ are distinct, and the step for $(e, \rho, \rho')$ ensures $\Phi^{X_Z}_e \neq X_{Z'}$. So $X_{Z'} \not\leq_T X_Z$, and symmetrically.
:::

The degrees $\deg_T(X_Z)$ are pairwise distinct, so the antichain has continuum many elements. It is a perfect version of the Kleene–Post construction of two incomparable degrees.

:::figure[The strings $\sigma_\rho$ for $|\rho| \leq 2$. When the level $n = 1$ is processed, the step for $e$ and the ordered pair $(0, 1)$ makes $\Phi^Y_e$ differ from every $X \succeq \sigma_1$ at the position $x = |\sigma_1|$, for every $Y \succeq \sigma_0$. The sets $X_Z$ are the unions of the strings along the paths $Z$.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The strings sigma_rho for rho of length at most 2, arranged as a binary tree. At level 1, the step for e and the pair (0, 1) extends sigma_0 to a string tau on which Phi_e converges at x, and extends sigma_1 at position x by a bit different from the value"><defs><marker id="ds-anti-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="300" y1="30" x2="160" y2="95" class="accent-stroke" stroke-width="1.8"/><line x1="300" y1="30" x2="440" y2="95" class="accent-stroke" stroke-width="1.8"/><line x1="160" y1="95" x2="90" y2="190" class="accent-stroke" stroke-width="1.8"/><line x1="160" y1="95" x2="230" y2="190" class="accent-stroke" stroke-width="1.8"/><line x1="440" y1="95" x2="370" y2="190" class="accent-stroke" stroke-width="1.8"/><line x1="440" y1="95" x2="510" y2="190" class="accent-stroke" stroke-width="1.8"/><circle cx="300" cy="30" r="5" class="node"/><text x="322" y="34" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">ε</tspan></text><circle cx="160" cy="95" r="5" class="node"/><text x="184" y="99" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><circle cx="440" cy="95" r="5" class="node"/><text x="464" y="99" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><circle cx="90" cy="190" r="5" class="node"/><text x="114" y="194" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">00</tspan></text><circle cx="230" cy="190" r="5" class="node"/><text x="254" y="194" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">01</tspan></text><circle cx="370" cy="190" r="5" class="node"/><text x="394" y="194" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">10</tspan></text><circle cx="510" cy="190" r="5" class="node"/><text x="534" y="194" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">11</tspan></text><line x1="182" y1="118" x2="415" y2="118" class="ink-stroke" stroke-width="1.1" stroke-dasharray="4 3" marker-end="url(#ds-anti-arrow)"/><text x="300" y="222" text-anchor="middle" class="label">step for e and the pair (0, 1): σ<tspan font-size="9" dy="3">0</tspan><tspan dy="-3"> is extended so that the computation at x converges to v,</tspan></text><text x="300" y="238" text-anchor="middle" class="label">and σ<tspan font-size="9" dy="3">1</tspan><tspan dy="-3"> receives the bit 1 − v at the position x = |σ</tspan><tspan font-size="9" dy="3">1</tspan><tspan dy="-3">| (dashed arrow)</tspan></text></svg>
:::

Each step asks whether some extension of a string makes a computation converge, a $\Sigma^0_1$ question; so, choosing the first witness in a fixed enumeration, the map $\rho \mapsto \sigma_\rho$ is computable in $\emptyset'$, and the construction uses no form of the axiom of choice.

## Exercises

::::exercise{difficulty=1}
Let $G$ be 1-generic. For a computable set $S$, let $G_S$ be the set whose column $m$ is $G^{[m]}$ for $m \in S$ and empty otherwise. Show that $S \subseteq S'$ if and only if $G_S \leq_T G_{S'}$, for computable sets $S, S'$.

:::solution
If $S \subseteq S'$, then $G_S$ is obtained from $G_{S'}$ by erasing the columns $m \notin S$, a computable operation since $S$ is computable. If $m \in S \setminus S'$, then $G^{[m]} \leq_T G_S$ and $G_{S'} \leq_T G^{\neq m}$, so $G_S \leq_T G_{S'}$ would contradict :ref{#thm-generic-independent}.
:::
::::

::::exercise{difficulty=1 #ex-generic-not-minimal}
Show that no 1-generic set has minimal degree: if $G$ is 1-generic, there is a set $Y$ with $\obf < \deg_T(Y) < \deg_T(G)$.

:::solution
Let $Y = G^{[0]}$. It is computable from $G$. It is not computable: otherwise $G^{[0]} \leq_T G^{\neq 0}$, contradicting :ref{#thm-generic-independent}. If $G \leq_T Y$, then $G^{[1]} \leq_T G^{[0]} \leq_T G^{\neq 1}$, again a contradiction. So $\obf < \deg_T(Y) < \deg_T(G)$.
:::
::::

## Notes and references

Kleene and Post (1954) introduced the finite extension method, from which the embedding of countable partial orders follows, since it builds independent sequences below $\obf'$ (Shore, 1997). Soare presents the countable case as Exercises 6.1.4–6.1.6 of *Turing Computability*. Monin and Patey attribute the embedding theorem to Sacks, and obtain independent sets from a 1-generic set, as here. The computable universal partial order is a computable presentation of the Fraïssé limit of the finite partial orders.

Sacks (1961, 1963) embedded every partial order of size $\aleph_1$ with the **countable predecessor property**, every element having countably many predecessors, a necessary condition by :ref{#prop-degrees-elementary}. Without the continuum hypothesis, whether every such order of size continuum embeds is an open problem posed by Sacks (Shore, 1997; Monin–Patey).

Shoenfield (1960) proved, using Zorn's lemma, that there is an uncountable antichain of degrees. Sacks (1963) constructed one of size continuum without the axiom of choice, crediting the result to an unpublished paper of Lacombe; Soare gives the construction as Exercise 6.1.7. Lerman's monograph studies embeddings preserving joins, and initial segments.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- J. R. Shoenfield, *An uncountable set of incomparable degrees*, Proceedings of the American Mathematical Society 11 (1960), 61–62.
- G. E. Sacks, *On suborderings of degrees of recursive unsolvability*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 7 (1961), 46–56.
- G. E. Sacks, *Degrees of Unsolvability*, Annals of Mathematics Studies 55, Princeton University Press, 1963.
- R. A. Shore, *Conjectures and questions from Gerald Sacks's Degrees of Unsolvability*, Archive for Mathematical Logic 36 (1997), 233–253.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 6.1.
- M. Lerman, *Degrees of Unsolvability: Local and Global Theory*, Springer, 1983.
