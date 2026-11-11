---
title: Uniformization and stages
summary: Kreisel's uniformization theorem for Π¹₁ relations on numbers; total Π¹₁ functions are hyperarithmetic; a Π¹₁ set is the increasing union of hyperarithmetic stages along ω₁ᶜᵏ, and it is Δ¹₁ exactly when its stages are bounded.
duration: 30
prerequisites: [norms]
---

If $R \subseteq \nat^2$ is c.e. and every $n$ has some $m$ with $R(n, m)$, a computable function selects such an $m$: the first one enumerated. The same selection works for $\Pi^1_1$ relations, with the stages of the previous lesson in place of the steps of an enumeration. The resulting function has a $\Pi^1_1$ graph, and when it is total, it is hyperarithmetic. This lesson also describes the stages of a $\Pi^1_1$ set from below: they are hyperarithmetic, and they exhaust the set at $\omega_1^{\mathrm{CK}}$.

## Uniformization

:::theorem[Kreisel]{#thm-kreisel-uniformization}
Let $R \subseteq \nat^2$ be $\Pi^1_1$. There is a partial function $f$ with $\Pi^1_1$ graph such that, for every $n$, if $R(n, m)$ holds for some $m$, then $f(n)$ is defined and $R(n, f(n))$ holds.
:::

:::proof{of=thm-kreisel-uniformization}
Apply the previous lesson to the $\Pi^1_1$ set $\{ \langle n, m \rangle : R(n, m) \}$, and write $\leq^*$, $<^*$ for its stage comparison relations, which are $\Pi^1_1$ by :ref{#thm-stage-comparison}. Let
$$
f(n) = m \iff \forall k\ \big(\langle n, m \rangle \leq^* \langle n, k \rangle\big) \wedge \forall k < m\ \big(\langle n, m \rangle <^* \langle n, k \rangle\big).
$$
In words: $\langle n, m \rangle$ enters the set at the least stage among the pairs $\langle n, k \rangle$, and $m$ is the least number with this stage. A number quantifier in front of a $\Pi^1_1$ formula gives a $\Pi^1_1$ formula, so the graph is $\Pi^1_1$. The first condition implies $R(n, m)$. If $R(n, m) \wedge R(n, m')$ with both $m$ and $m'$ satisfying the definition, then their stages are equal, and the second condition gives $m \leq m'$ and $m' \leq m$; so $f$ is a function. If $R(n, k)$ holds for some $k$, the ordinals $\rho_{\langle n, k \rangle}$ with $R(n, k)$ have a least element $\alpha$, and the least $m$ with $\rho_{\langle n, m \rangle} = \alpha$ satisfies the definition.
:::

:::corollary{#cor-total-pi11}
Every total function $f : \nat \to \nat$ whose graph is $\Pi^1_1$ is hyperarithmetic. Consequently, if $R \subseteq \nat^2$ is $\Pi^1_1$ and every $n$ has some $m$ with $R(n, m)$, there is a hyperarithmetic function $f$ with $R(n, f(n))$ for every $n$.
:::

:::proof{of=cor-total-pi11}
If $f$ is total, then $f(n) \neq m$ if and only if $\exists k\ (k \neq m \wedge f(n) = k)$, which is $\Pi^1_1$. So the graph is $\Delta^1_1$, hence hyperarithmetic by Kleene's theorem (:ref{#thm-kleene-delta11}), and so is $f$, computable from its graph. The second statement follows from :ref{#thm-kreisel-uniformization}.
:::

The same argument for c.e. sets shows that a total function with a c.e. graph is computable. The selection principle fails for $\Sigma^1_1$ relations. Let $Y_0$ and $Y_1$ be disjoint $\Pi^1_1$ sets without $\Delta^1_1$ separation (second exercise of the previous lesson), and let $R(n, 0)$ hold if $n \notin Y_0$ and $R(n, 1)$ hold if $n \notin Y_1$. This relation is $\Sigma^1_1$, and every $n$ has a value. If $f$ were a hyperarithmetic function with $R(n, f(n))$ for every $n$, the set $\{ n : f(n) = 1 \}$ would be $\Delta^1_1$, would contain $Y_0$ and be disjoint from $Y_1$.

:::quiz[uniformization]
In the proof of :ref{#thm-kreisel-uniformization}, why is the least stage used before the least number $m$?

- [x] Because "$m$ is the least number with $R(n, m)$" requires $\neg R(n, k)$ for $k < m$, a $\Sigma^1_1$ condition, while the comparison of stages only uses the $\Pi^1_1$ relations $\leq^*$ and $<^*$.
- [ ] Because the least $m$ might not exist.

  If $R(n, m)$ holds for some $m$, the least one exists; the problem is the complexity of its definition.
- [ ] Because stages are numbers.

  Stages are ordinals, which is why their least element exists by well-ordering.

---

In :ref{#cor-total-pi11}, where is the totality of $f$ used?

- [x] To express $f(n) \neq m$ as "$f(n)$ is some other value", which is $\Pi^1_1$; for a partial function, $f(n) \neq m$ also holds when $f(n)$ is undefined, a condition with no $\Pi^1_1$ definition in general.
- [ ] To make the graph of $f$ a $\Pi^1_1$ set.

  The graph is $\Pi^1_1$ by hypothesis.
- [ ] To apply :ref{#thm-kreisel-uniformization}.

  The first statement does not use the uniformization theorem.
:::

## Stages from below

For $\alpha \leq \omega_1^{\mathrm{CK}}$, let $A_{< \alpha} = \{ n : \rho_n < \alpha \}$ be the set of elements of $A$ that enter before stage $\alpha$.

:::theorem{#thm-pi11-stages}
Let $A$ be a $\Pi^1_1$ set, with stages given by uniformly computable trees $(T_n)$.

1. $A = A_{< \omega_1^{\mathrm{CK}}}$: every element of $A$ enters at a computable stage.
2. For every computable ordinal $\alpha$, the set $A_{< \alpha}$ is hyperarithmetic.
3. $A$ is $\Delta^1_1$ if and only if $A = A_{< \alpha}$ for some computable ordinal $\alpha$.
:::

:::proof{of=thm-pi11-stages}
1. A computable well-founded tree has a computable Kleene–Brouwer ordering, which is a well-ordering of type at least its rank (:ref{#thm-kleene-brouwer}); so its rank is less than $\omega_1^{\mathrm{CK}}$.
2. Let $t(n)$ be an index of $T_n$, computable from $n$. Then $n \in A_{< \alpha}$ if and only if $t(n) \in \mathrm{WF}_{< \alpha}$, which is hyperarithmetic by :ref{#lem-wf-rank-hyp}.
3. If $A = A_{< \alpha}$, it is hyperarithmetic by item 2, hence $\Delta^1_1$. Conversely, if $A$ is $\Delta^1_1$, then $\{ t(n) : n \in A \}$ is a $\Sigma^1_1$ set of indices of computable well-founded trees. By the boundedness theorem, in the form used in the proof of :ref{#thm-kleene-delta11}, their ranks are bounded by some computable ordinal $\alpha$, and $A = A_{< \alpha}$.
:::

A $\Pi^1_1$ set that is not hyperarithmetic, such as $\mathcal O$ or $\mathrm{WF}$, thus receives new elements at cofinally many stages below $\omega_1^{\mathrm{CK}}$, while each initial part of its enumeration is hyperarithmetic. This is the analogue of the fact that a c.e. set is the union of the finite sets $A_s$, and is computable when the enumeration can be bounded. The analogy has a precise form: the $\Pi^1_1$ sets are exactly the sets that are $\Sigma_1$-definable over the structure $L_{\omega_1^{\mathrm{CK}}}$ of constructible sets of rank less than $\omega_1^{\mathrm{CK}}$, and the hyperarithmetic sets are the subsets of $\nat$ that belong to it. We admit these characterizations, which are the starting point of $\alpha$-recursion theory (Sacks, *Higher Recursion Theory*, Chapter VII).

:::quiz[stages]
In item 3 of :ref{#thm-pi11-stages}, where is the hypothesis that $A$ is $\Sigma^1_1$ used?

- [x] To make $\{ t(n) : n \in A \}$ a $\Sigma^1_1$ set of well-founded trees, to which the boundedness theorem applies.
- [ ] To make $A_{< \alpha}$ hyperarithmetic.

  This holds for every $\Pi^1_1$ set, by item 2.
- [ ] To show that every element of $A$ has a computable stage.

  This is item 1, which holds for every $\Pi^1_1$ set.
:::

## Exercises

::::exercise{difficulty=1}
Show that the reduction property fails for $\Sigma^1_1$ sets: there are $\Sigma^1_1$ sets $D$ and $E$ for which no disjoint $\Sigma^1_1$ sets $D' \subseteq D$ and $E' \subseteq E$ have union $D \cup E$.

:::solution
By the second exercise of the previous lesson, there are disjoint $\Pi^1_1$ sets $Y_0$ and $Y_1$ without $\Delta^1_1$ separation. Let $D = \overline{Y_0}$ and $E = \overline{Y_1}$, which are $\Sigma^1_1$ with $D \cup E = \nat$. If $D' \subseteq D$ and $E' \subseteq E$ were disjoint $\Sigma^1_1$ sets with union $\nat$, each would be the complement of the other, hence $\Delta^1_1$. Then $E'$ would contain $Y_0$, since $Y_0 \cap D' \subseteq Y_0 \cap D = \emptyset$, and $E' \cap Y_1 \subseteq E \cap Y_1 = \emptyset$: a $\Delta^1_1$ separation.
:::
::::

::::exercise{difficulty=2}
Let $A$ be a $\Pi^1_1$ set that is not $\Delta^1_1$. Show that for every computable ordinal $\alpha$, there is $n \in A$ with $\rho_n \geq \alpha$, and that the function $\alpha \mapsto$ "the least stage $\beta \geq \alpha$ at which some element enters $A$" is defined on all computable ordinals.

:::solution
If every $n \in A$ had $\rho_n < \alpha$, then $A = A_{< \alpha}$ would be $\Delta^1_1$ by :ref{#thm-pi11-stages}. So the set $\{ \rho_n : n \in A, \rho_n \geq \alpha \}$ is a non-empty set of ordinals, and has a least element $\beta$; it is a computable ordinal by item 1.
:::
::::

## Notes and references

Kreisel (1962) proved the uniformization theorem for $\Pi^1_1$ relations on numbers; Kondo and Addison proved the much harder uniformization theorem for $\Pi^1_1$ relations on reals. The characterization of $\Pi^1_1$ sets by $\Sigma_1$ definability over $L_{\omega_1^{\mathrm{CK}}}$ is due to Kripke and Platek.

- G. Kreisel, *The axiom of choice and the class of hyperarithmetic functions*, Indagationes Mathematicae 24 (1962), 307–319.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Chapters I, II and VII.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Chapter 4.
