---
title: Π¹₁ norms and the reduction property
summary: The rank of the normal-form tree as a stage at which an element enters a Π¹₁ set; comparison of ranks by strictly monotone maps; the stage comparison relations are Π¹₁; the reduction property for Π¹₁ sets and Kleene's separation theorem for Σ¹₁ sets.
duration: 35
prerequisites: [hyperarithmetic/kleene-theorem]
---

A c.e. set is enumerated in stages $0, 1, 2, \dots$, and two elements can be compared by the stage at which they appear. Many properties of c.e. sets follow from this: for instance, two c.e. sets $A$ and $B$ can be **reduced** to disjoint c.e. sets $A' \subseteq A$, $B' \subseteq B$ with the same union, by keeping each element in the set where it appears first. The $\Pi^1_1$ sets are enumerated in the same way, along the computable ordinals: the stage of an element is the rank of a well-founded tree. This lesson shows that stages can be compared in a $\Pi^1_1$ way, and deduces the reduction property.

## Ranks and strictly monotone maps

Throughout, trees are subsets of $\nat^{<\nat}$ closed under prefixes, and we only consider trees containing the empty sequence. Adding the empty sequence to a tree does not change whether it is well-founded, so the trees $T_n$ of the normal form theorem (:ref{#thm-pi11-normal-form}) may be assumed to contain it. For a tree $T$, let $\rho(T) = \mathrm{rk}(T)$ if $T$ is well-founded (:ref{#def-tree-rank}), and $\rho(T) = \infty$ otherwise, with $\alpha < \infty$ for every ordinal $\alpha$. For $\sigma \in T$, write $T_\sigma = \{ \tau : \sigma \tau \in T \}$ for the subtree above $\sigma$, and $\mathrm{rk}_T(\sigma) = \mathrm{rk}(T_\sigma)$ when it is well-founded. If $\sigma \subsetneq \tau$ are in a well-founded tree $T$, then $\mathrm{rk}_T(\tau) < \mathrm{rk}_T(\sigma)$, by induction on the length of $\tau$ from the definition of the rank.

A map $g : S \to T$ between trees is **strictly monotone** if $\sigma \subsetneq \tau$ implies $g(\sigma) \subsetneq g(\tau)$.

:::lemma{#lem-rank-comparison}
For trees $S$ and $T$, $\rho(S) \leq \rho(T)$ if and only if there is a strictly monotone map $g : S \to T$.
:::

:::proof{of=lem-rank-comparison}
($\Leftarrow$) Let $g$ be strictly monotone. If $T$ is ill-founded, $\rho(T) = \infty$ and there is nothing to prove. Suppose $T$ well-founded. Then $S$ is well-founded: a path $f$ through $S$ would give a strictly increasing sequence $g(f \uh 0) \subsetneq g(f \uh 1) \subsetneq \cdots$ in $T$, hence a path. We show $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma))$ for every $\sigma \in S$, by induction along the well-founded relation "$\tau$ properly extends $\sigma$" on $S$. For every $n$ with $\sigma n \in S$, the induction hypothesis and $g(\sigma) \subsetneq g(\sigma n)$ give $\mathrm{rk}_S(\sigma n) \leq \mathrm{rk}_T(g(\sigma n)) < \mathrm{rk}_T(g(\sigma))$. Taking the supremum of $\mathrm{rk}_S(\sigma n) + 1$ gives $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma))$. For $\sigma$ empty, $\rho(S) \leq \mathrm{rk}_T(g(\emptyset)) \leq \rho(T)$.

($\Rightarrow$) If $T$ has a path $h$, let $g(\sigma) = h \uh |\sigma|$. Otherwise $T$ is well-founded, and so is $S$, since $\rho(S) \leq \rho(T) < \infty$. Define $g(\sigma)$ by induction on $|\sigma|$, maintaining $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma))$. Let $g(\emptyset) = \emptyset$. If $g(\sigma)$ is defined and $\sigma n \in S$, then
$$
\mathrm{rk}_S(\sigma n) < \mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma)) = \sup \{ \mathrm{rk}_T(g(\sigma) m) + 1 : g(\sigma) m \in T \},
$$
so there is $m$ with $g(\sigma) m \in T$ and $\mathrm{rk}_S(\sigma n) \leq \mathrm{rk}_T(g(\sigma) m)$; let $g(\sigma n) = g(\sigma) m$ for the least such $m$. The map is strictly monotone, since each step extends the image by one element.
:::

The existence of a strictly monotone map is expressed by an existential function quantifier followed by an arithmetic condition. So the relation $\rho(S) \leq \rho(T)$ between indices of computable trees is $\Sigma^1_1$. Strict comparison reduces to it, when the larger tree is well-founded:
$$
\text{if } T \text{ is well-founded:} \quad \rho(S) < \rho(T) \iff \exists n\ (\langle n \rangle \in T \wedge \rho(S) \leq \rho(T_{\langle n \rangle})),
$$
since $\rho(T)$ is the supremum of the ordinals $\rho(T_{\langle n \rangle}) + 1$.

## Stage comparison

Fix a $\Pi^1_1$ set $A$ and a uniformly computable sequence of trees $(T_n)$, containing the empty sequence, with $n \in A$ if and only if $T_n$ is well-founded. Let $\rho_n = \rho(T_n)$: for $n \in A$, it is a computable ordinal, the **stage** at which $n$ enters $A$, and $\rho_n = \infty$ for $n \notin A$. The map $n \mapsto \rho_n$ on $A$ is a **$\Pi^1_1$ norm** on $A$.

:::theorem{#thm-stage-comparison}
The relations
$$
n \leq^* m \iff n \in A \wedge \rho_n \leq \rho_m, \qquad n <^* m \iff n \in A \wedge \rho_n < \rho_m
$$
are $\Pi^1_1$.
:::

:::proof{of=thm-stage-comparison}
If $n \in A$, then $T_n$ is well-founded, and $\rho_n \leq \rho_m$ holds if and only if $\rho_m < \rho_n$ fails, that is, by the display above, if and only if there is no $k$ with $\langle k \rangle \in T_n$ and $\rho_m \leq \rho((T_n)_{\langle k \rangle})$. So
$$
n \leq^* m \iff n \in A \wedge \neg \exists k\ \big(\langle k \rangle \in T_n \wedge \rho(T_m) \leq \rho((T_n)_{\langle k \rangle})\big),
$$
the conjunction of a $\Pi^1_1$ formula and the negation of a $\Sigma^1_1$ formula, by :ref{#lem-rank-comparison}. Similarly, $n <^* m$ if and only if $n \in A$ and $\rho(T_m) \leq \rho(T_n)$ fails.
:::

The definitions of $\leq^*$ and $<^*$ do not require $m \in A$: if $m \notin A$, then $\rho_m = \infty$, and every $n \in A$ satisfies $n <^* m$. This is the analogue of the fact that an element enumerated into a c.e. set comes before every element that is never enumerated.

:::corollary{#cor-initial-segments}
For every $n \in A$, the set $\{ m : \rho_m \leq \rho_n \}$ is $\Delta^1_1$, hence hyperarithmetic, and included in $A$.
:::

:::proof{of=cor-initial-segments}
It is $\{ m : m \leq^* n \}$, which is $\Pi^1_1$ by :ref{#thm-stage-comparison}; and it is $\{ m : \rho(T_m) \leq \rho(T_n) \}$, which is $\Sigma^1_1$ by :ref{#lem-rank-comparison}. Its members have $\rho_m \leq \rho_n < \infty$, so they belong to $A$. By Kleene's theorem (:ref{#thm-kleene-delta11}), it is hyperarithmetic.
:::

:::quiz[stage comparison]
In the proof of :ref{#thm-stage-comparison}, why is $n \leq^* m$ written as the negation of $\rho_m < \rho_n$, rather than directly as "there is a strictly monotone map from $T_n$ to $T_m$"?

- [x] Because the existence of a map is $\Sigma^1_1$, while $n \leq^* m$ must be $\Pi^1_1$; the negation of the $\Sigma^1_1$ relation $\rho_m < \rho_n$, available since $T_n$ is well-founded, has the right complexity.
- [ ] Because the map does not exist when $T_m$ is ill-founded.

  It does: every tree maps strictly monotonically into an ill-founded tree.
- [ ] Because ranks cannot be compared by maps.

  :ref{#lem-rank-comparison} shows that they can.

---

Why is the hypothesis $n \in A$ part of the definition of $n \leq^* m$?

- [x] Because the formula for $\rho_m < \rho_n$ by the subtrees $(T_n)_{\langle k \rangle}$ is only correct when $T_n$ is well-founded; when both trees are ill-founded, it would wrongly assert $\infty < \infty$.
- [ ] Because $\rho_n$ is not defined for $n \notin A$.

  It is defined, and equal to $\infty$.
- [ ] To make the relation $\Sigma^1_1$.

  Membership in $A$ is $\Pi^1_1$; it keeps the relation $\Pi^1_1$.
:::

## Reduction and separation

:::theorem[Reduction property]{#thm-pi11-reduction}
For all $\Pi^1_1$ sets $B$ and $C$, there are disjoint $\Pi^1_1$ sets $B' \subseteq B$ and $C' \subseteq C$ with $B' \cup C' = B \cup C$.
:::

:::proof{of=thm-pi11-reduction}
Let $A = \{ 2n : n \in B \} \cup \{ 2n + 1 : n \in C \}$, a $\Pi^1_1$ set, with a norm as above, and let
$$
B' = \{ n : 2n \leq^* 2n + 1 \}, \qquad C' = \{ n : 2n + 1 <^* 2n \}.
$$
Both are $\Pi^1_1$ by :ref{#thm-stage-comparison}. If $n \in B'$, then $2n \in A$, so $n \in B$; similarly $C' \subseteq C$. They are disjoint, since $\rho_{2n} \leq \rho_{2n+1}$ and $\rho_{2n+1} < \rho_{2n}$ are incompatible. If $n \in B \cup C$, then $\rho_{2n}$ and $\rho_{2n+1}$ are not both $\infty$: if $\rho_{2n} \leq \rho_{2n+1}$, then $\rho_{2n}$ is an ordinal and $n \in B'$; otherwise $\rho_{2n+1} < \rho_{2n}$ and $n \in C'$.
:::

:::corollary[Kleene's separation theorem]{#cor-sigma11-separation}
For all disjoint $\Sigma^1_1$ sets $D$ and $E$, there is a $\Delta^1_1$ set $F$ with $D \subseteq F$ and $F \cap E = \emptyset$.
:::

:::proof{of=cor-sigma11-separation}
The complements $\overline D$ and $\overline E$ are $\Pi^1_1$, and their union is $\nat$, since $D \cap E = \emptyset$. Let $B' \subseteq \overline D$ and $C' \subseteq \overline E$ be given by :ref{#thm-pi11-reduction}: they are disjoint $\Pi^1_1$ sets with union $\nat$, so each is the complement of the other, and both are $\Delta^1_1$. Let $F = C'$. Then $F \subseteq \overline E$, so $F \cap E = \emptyset$. If $n \in D$, then $n \notin \overline D \supseteq B'$, so $n \in C' = F$.
:::

The corresponding statement for $\Pi^1_1$ sets fails, exactly as two disjoint c.e. sets need not be separated by a computable set; see the exercises. By Kleene's theorem, the separating set is hyperarithmetic. In classical descriptive set theory, the corresponding theorem is Lusin's separation theorem: two disjoint analytic sets are separated by a Borel set.

## Exercises

::::exercise{difficulty=1}
Show that for $n \in A$, the set $\{ m : \rho_m < \rho_n \}$ is $\Delta^1_1$, and that the relation $n \leq^* m \wedge m \leq^* n$ is $\Pi^1_1$ and an equivalence relation on $A$ whose classes are the sets of elements entering $A$ at the same stage.

:::solution
The set is $\{ m : m <^* n \}$, which is $\Pi^1_1$, and $\{ m : \exists k\ (\langle k \rangle \in T_n \wedge \rho(T_m) \leq \rho((T_n)_{\langle k \rangle})) \}$, which is $\Sigma^1_1$, by the display after :ref{#lem-rank-comparison}, since $T_n$ is well-founded. The relation is a conjunction of $\Pi^1_1$ relations. It holds exactly when $n, m \in A$ and $\rho_n = \rho_m$, which is an equivalence relation on $A$ with the stated classes.
:::
::::

::::exercise{difficulty=2}
Show that there are disjoint $\Pi^1_1$ sets that cannot be separated by a $\Delta^1_1$ set. Use the $\Pi^1_1$ set $U$ of :ref{#prop-pi11-not-sigma11}, whose sections $U_e = \{ n : \langle e, n \rangle \in U \}$ include all the $\Pi^1_1$ sets.

:::solution
For $e = \langle a, b \rangle$, let $e \in X_0$ if $e \in U_a$, and $e \in X_1$ if $e \in U_b$. Both sets are $\Pi^1_1$. Let $Y_0 \subseteq X_0$ and $Y_1 \subseteq X_1$ be given by :ref{#thm-pi11-reduction}. Suppose that a $\Delta^1_1$ set $F$ satisfies $Y_0 \subseteq F$ and $F \cap Y_1 = \emptyset$. Choose $a$ with $U_a = \overline F$ and $b$ with $U_b = F$, possible since both are $\Pi^1_1$, and let $e = \langle a, b \rangle$. If $e \in F$, then $e \in U_b$, so $e \in X_1$, and $e \notin U_a$, so $e \notin X_0 \supseteq Y_0$; since $Y_0 \cup Y_1 = X_0 \cup X_1$, $e \in Y_1$, contradicting $F \cap Y_1 = \emptyset$. If $e \notin F$, then $e \in X_0 \setminus X_1$, so $e \in Y_0 \subseteq F$: a contradiction. So $Y_0$ and $Y_1$ are disjoint $\Pi^1_1$ sets without $\Delta^1_1$ separation.
:::
::::

## Notes and references

Norms and the prewellordering property were isolated by Moschovakis, following Kleene and Spector, who used ordinal notations and the H-sets. The reduction property for $\Pi^1_1$ sets is due to Kuratowski in the classical setting, and to Addison and Kleene in the effective setting.

- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Chapter 4.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Chapter I.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Section 34.
