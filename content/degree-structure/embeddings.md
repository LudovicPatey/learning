---
title: Embedding partial orders
summary: The columns of a 1-generic set are computably independent; a computable partial order contains a copy of every countable partial order; hence every countable partial order embeds into the Turing degrees below 0′; there is an antichain of continuum many degrees.
duration: 35
prerequisites: [exact-pairs, turing-degrees/low-and-high]
---

Kleene and Post showed that every finite partial order embeds into the Turing degrees. The method extends to every countable partial order: the degrees contain a copy of each of them, already below $\obf'$. The proof combines two ingredients of independent interest. The first is a sequence of sets none of which is computable from the others, obtained from the columns of a 1-generic set. The second is a computable partial order that contains a copy of every countable partial order. The lesson ends with an antichain of continuum many degrees.

An **embedding** of a partial order $(P, \leq_P)$ into $\mathcal D$ is an injective map $f : P \to \mathcal D$ with $p \leq_P q$ if and only if $f(p) \leq f(q)$.

## Independent sets

:::definition{#def-independent}
A sequence of sets $(X_n)_{n \in \nat}$ is **computably independent** if $X_i \not\leq_T \bigoplus_{k \neq i} X_k$ for every $i$, where $\bigoplus_{k \neq i} X_k$ is the set whose column $k$ is $X_k$ for $k \neq i$ and whose column $i$ is empty.
:::

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

A partial order $(Q, \leq)$ has the **extension property** if for every finite $F \subseteq Q$ and every partial order on $F \cup \{ p \}$, with $p$ a new element, that extends the order of $F$, there is $q \in Q \setminus F$ with $a \leq q \iff a \leq p$ and $q \leq a \iff p \leq a$ for every $a \in F$.

:::lemma{#lem-extension-universal}
If $(Q, \leq)$ has the extension property, every countable partial order embeds into it.
:::

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

*The order remains a partial order.* Let $D$ and $E$ be the sets of elements below and above $s$. $D$ is closed downward and $E$ upward. They are disjoint: $b \preceq y \preceq a$ with $a \in L$, $b \in V$ would give $b \preceq a \preceq b$, so $a = b \in L \cap V$. Transitivity through $s$ holds: if $y \prec s \prec z$, then $y \preceq a \preceq b \preceq z$ for some $a \in L$, $b \in V$, so $y \preceq z$, and $y \neq z$ since $D \cap E = \emptyset$.

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

Countable antichains are particular countable partial orders. The degrees also contain antichains of the largest possible size.

:::theorem[Sacks]{#thm-continuum-antichain}
There is a family $(X_Z)_{Z \in \cs}$ of sets such that $X_Z$ and $X_{Z'}$ are Turing incomparable whenever $Z \neq Z'$.
:::

:::proof{of=thm-continuum-antichain}
We define strings $\sigma_\rho$, for $\rho \in \bstr$, with $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ incomparable extensions of $\sigma_\rho$, and set $X_Z = \bigcup_n \sigma_{Z \uh n}$.

Let $\sigma_\varepsilon = \varepsilon$. Suppose that $\sigma_\rho$ is defined for all $\rho$ of length $n$. We modify these finitely many strings by finitely many extension steps, one for each $e < n$ and each ordered pair $(\rho, \rho')$ of distinct strings of length $n$. In the step for $(e, \rho, \rho')$, let $x = |\sigma_{\rho'}|$. If some $\tau \succeq \sigma_\rho$ has $\Phi^\tau_e(x)\converge = v$, replace $\sigma_\rho$ by $\tau$ and $\sigma_{\rho'}$ by $\sigma_{\rho'} (1 - v)$. Otherwise leave the strings unchanged; then $\Phi^Y_e(x)\diverge$ for every $Y \succeq \sigma_\rho$, by the use principle. In both cases, $\Phi^Y_e \neq X$ for all $Y \succeq \sigma_\rho$ and $X \succeq \sigma_{\rho'}$, and this remains true after further extensions. After all steps, let $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ be the final strings for $\rho$ followed by $0$ and by $1$.

Let $Z \neq Z'$, and $e \in \nat$. For $n > e$ larger than the first position where $Z$ and $Z'$ differ, $\rho = Z \uh n$ and $\rho' = Z' \uh n$ are distinct, and the step for $(e, \rho, \rho')$ ensures $\Phi^{X_Z}_e \neq X_{Z'}$. So $X_{Z'} \not\leq_T X_Z$, and symmetrically.
:::

The degrees $\deg_T(X_Z)$ are pairwise distinct, so the antichain has continuum many elements. It is a perfect version of the Kleene–Post construction of two incomparable degrees.

## Exercises

::::exercise{difficulty=1}
Let $G$ be 1-generic. For a computable set $S$, let $G_S$ be the set whose column $m$ is $G^{[m]}$ for $m \in S$ and empty otherwise. Show that $S \subseteq S'$ if and only if $G_S \leq_T G_{S'}$, for computable sets $S, S'$.

:::solution
If $S \subseteq S'$, then $G_S$ is obtained from $G_{S'}$ by erasing the columns $m \notin S$, a computable operation since $S$ is computable. If $m \in S \setminus S'$, then $G^{[m]} \leq_T G_S$ and $G_{S'} \leq_T G^{\neq m}$, so $G_S \leq_T G_{S'}$ would contradict :ref{#thm-generic-independent}.
:::
::::

::::exercise{difficulty=1}
Show that no 1-generic set has minimal degree: if $G$ is 1-generic, there is a set $Y$ with $\obf < \deg_T(Y) < \deg_T(G)$.

:::solution
Let $Y = G^{[0]}$. It is computable from $G$. It is not computable: otherwise $G^{[0]} \leq_T G^{\neq 0}$, contradicting :ref{#thm-generic-independent}. If $G \leq_T Y$, then $G^{[1]} \leq_T G^{[0]} \leq_T G^{\neq 1}$, again a contradiction. So $\obf < \deg_T(Y) < \deg_T(G)$.
:::
::::

## Notes and references

Kleene and Post (1954) embedded every finite partial order, and Sacks (1963) every partial order of size $\aleph_1$ in which every element has countably many predecessors; the countable case follows from the methods of Kleene and Post. The computable universal partial order is a computable presentation of the Fraïssé limit of the finite partial orders. Sacks (1963) also constructed antichains of size continuum. Embeddings preserving least upper bounds, and initial segments of $\mathcal D$, are studied in Lerman's monograph.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- G. E. Sacks, *Degrees of Unsolvability*, Annals of Mathematics Studies 55, Princeton University Press, 1963.
- M. Lerman, *Degrees of Unsolvability*, Springer, 1983.
