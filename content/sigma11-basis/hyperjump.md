---
title: Hyperarithmetic reducibility and the hyperjump
summary: Hyperarithmetic reducibility and the hyperjump O^X; a Σ¹₁(Y) well-founded tree has rank below ω₁^Y; hyperarithmetic reducibility preserves the Church–Kleene ordinal; Spector's theorem that a set computes O hyperarithmetically exactly when it collapses ω₁ᶜᵏ.
duration: 25
prerequisites: [hyperarithmetic/kleene-theorem, computable-ordinals/boundedness]
---

Turing reducibility measures computation with finitely many steps. In higher computability, the natural notion of computation is hyperarithmetic: computation along the computable ordinals. Relativizing the hyperarithmetic sets gives a reducibility, $X \leq_h Y$ if $X$ is hyperarithmetic relative to $Y$, and relativizing Kleene's $\mathcal O$ gives the **hyperjump** $\mathcal O^X$, which plays for $\leq_h$ the role that the Turing jump plays for $\leq_T$. This course studies these notions, and the $\Sigma^1_1$ classes, which play the role of the $\Pi^0_1$ classes.

A new phenomenon appears with relativization. The Turing jump of every oracle is computed by finite iteration; the hyperarithmetic sets relative to $Y$ are obtained by iterating the jump along the ordinals computable in $Y$, and there are more of them when $\omega_1^Y > \omega_1^{\mathrm{CK}}$. Spector's theorem identifies exactly when this happens: $Y$ computes a well-ordering of type $\omega_1^{\mathrm{CK}}$ if and only if $\mathcal O$ is hyperarithmetic in $Y$. The tool is a boundedness principle for trees: a well-founded tree definable by a $\Sigma^1_1(Y)$ formula has rank below $\omega_1^Y$.

## Hyperarithmetic reducibility

All the notions of the courses on computable ordinals and hyperarithmetic sets relativize to an oracle $Y$: the notations $\mathcal O^Y$, defined as $\mathcal O$ with $Y$-computable fundamental sequences, the ordinal $\omega_1^Y$, the supremum of the $Y$-computable ordinals, the sets $H^Y_a$ for $a \in \mathcal O^Y$, and the $\Pi^1_1(Y)$ and $\Sigma^1_1(Y)$ sets, defined with $Y$ as a parameter. The proofs relativize, uniformly in $Y$. In particular, $\mathcal O^Y$ is $\Pi^1_1(Y)$-complete, $\mathcal O^Y$ is not $\Sigma^1_1(Y)$, and Kleene's theorem relativizes: a set is $\Delta^1_1(Y)$ if and only if it is computable in $H^Y_a$ for some $a \in \mathcal O^Y$.

:::definition{#def-hyperarithmetic-in}
A set $X$ is **hyperarithmetic in** $Y$, written $X \leq_h Y$, if $X$ is $\Delta^1_1(Y)$. The **hyperjump** of $Y$ is $\mathcal O^Y$. We write $X \equiv_h Y$ if $X \leq_h Y$ and $Y \leq_h X$, and $X <_h Y$ if $X \leq_h Y$ and $Y \not\leq_h X$; the equivalence classes of $\equiv_h$ are the **hyperdegrees**.
:::

The relation $\leq_h$ is a preorder: if $X$ is $\Delta^1_1(Y)$ and $Y$ is $\Delta^1_1(Z)$, replacing in the definitions of $X$ the atomic formulas $n \in Y$ by their $\Pi^1_1(Z)$ or $\Sigma^1_1(Z)$ definitions, according to their polarity in prenex form, shows that $X$ is $\Delta^1_1(Z)$, as in :ref{#prop-h-delta11}. If $X \leq_T Y$, then $X \leq_h Y$, and the hyperarithmetic sets form the least hyperdegree.

:::proposition{#prop-hyperjump}
1. $Y \leq_m \mathcal O^Y$ and $Y <_h \mathcal O^Y$.
2. $X \leq_h Y$ if and only if $\mathcal O^X \leq_m \mathcal O^Y$.
:::

:::proof{of=prop-hyperjump}
1. The set $Y$ is $\Pi^1_1(Y)$, so it is many-one reducible to the $\Pi^1_1(Y)$-complete set $\mathcal O^Y$. If $\mathcal O^Y \leq_h Y$, then $\mathcal O^Y$ would be $\Sigma^1_1(Y)$, which it is not.
2. If $X$ is $\Delta^1_1(Y)$, the set $\mathcal O^X$, which is $\Pi^1_1(X)$, is $\Pi^1_1(Y)$ by substitution of the definitions of $X$; so $\mathcal O^X \leq_m \mathcal O^Y$ by completeness. Conversely, if $\mathcal O^X \leq_m \mathcal O^Y$, then $X$ and its complement, which are many-one reducible to $\mathcal O^X$ by 1 applied to $X$ and to its complement, are $\Pi^1_1(Y)$; so $X$ is $\Delta^1_1(Y)$.
:::

The analogy with the Turing jump is close: $Y <_T Y'$ and $X \leq_T Y$ implies $X' \leq_m Y'$. But the hyperjump is much stronger than any iterate of the jump: $Y^{(\alpha)} \leq_T H^Y_a$ for every $\alpha = |a|$ with $a \in \mathcal O^Y$, and all these sets are hyperarithmetic in $Y$, hence below $\mathcal O^Y$.

## Boundedness for trees

For trees $S$ and $T$ on $\nat$, a **morphism** from $S$ to $T$ is a map $f : S \to T$ that preserves lengths and the prefix order: $|f(\sigma)| = |\sigma|$, and $f(\sigma) \preceq f(\tau)$ whenever $\sigma \preceq \tau$. A morphism maps every path of $S$ to a path of $T$, so if $T$ is well-founded and there is a morphism from $S$ to $T$, then $S$ is well-founded. For well-founded trees, morphisms compare ranks.

:::lemma{#lem-tree-morphism}
Let $S$ and $T$ be non-empty well-founded trees with $\mathrm{rk}(S) \leq \mathrm{rk}(T)$. Then there is a morphism from $S$ to $T$.
:::

:::proof{of=lem-tree-morphism}
For a node $\sigma$ of a tree $R$, write $\mathrm{rk}_R(\sigma)$ for the rank of the subtree of the nodes of $R$ extending $\sigma$, translated to begin at the root; so $\mathrm{rk}_R(\sigma) = \sup \{ \mathrm{rk}_R(\sigma n) + 1 : \sigma n \in R \}$. Define $f(\sigma)$ by induction on the length of $\sigma$, keeping the invariant $\mathrm{rk}_T(f(\sigma)) \geq \mathrm{rk}_S(\sigma)$. Let $f(\varepsilon) = \varepsilon$; the invariant is the hypothesis. If $f(\sigma)$ is defined and $\sigma n \in S$, then
$$
\mathrm{rk}_S(\sigma n) < \mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(f(\sigma)) = \sup \{ \mathrm{rk}_T(f(\sigma) m) + 1 : f(\sigma) m \in T \},
$$
so there is $m$ with $f(\sigma) m \in T$ and $\mathrm{rk}_T(f(\sigma) m) \geq \mathrm{rk}_S(\sigma n)$; let $f(\sigma n) = f(\sigma) m$ for the least such $m$.
:::

:::theorem{#thm-sigma11-tree-bound}
Let $T$ be a well-founded tree that is $\Sigma^1_1(Y)$, as a set of codes of strings. Then $\mathrm{rk}(T) < \omega_1^Y$.
:::

If the rank of $T$ were at least $\omega_1^Y$, every $Y$-computable well-founded tree would map into $T$ by a morphism. Since a morphism into a well-founded tree only exists from well-founded trees, the existence of a morphism into $T$ would characterize well-foundedness among $Y$-computable trees, and this existence is a $\Sigma^1_1(Y)$ property, because $T$ only appears positively. This would make a $\Pi^1_1(Y)$-complete set $\Sigma^1_1(Y)$.

:::proof{of=thm-sigma11-tree-bound}
By the normal form theorem relativized to $Y$ (:ref{#thm-pi11-normal-form}), there is a uniformly $Y$-computable sequence of trees $(T_e)$ with $e \in \mathcal O^Y$ if and only if $T_e$ is well-founded. Suppose that $\mathrm{rk}(T) \geq \omega_1^Y$. For $e \in \mathcal O^Y$, $T_e$ is a $Y$-computable well-founded tree, so its rank is a $Y$-computable ordinal, by :ref{#prop-rank-computable} relativized, hence less than $\omega_1^Y \leq \mathrm{rk}(T)$; by :ref{#lem-tree-morphism}, there is a morphism from $T_e$ to $T$ (if $T_e$ is empty, so is the empty map). For $e \notin \mathcal O^Y$, $T_e$ has a path, which a morphism would map to a path of $T$; so there is none. Hence
$$
e \in \mathcal O^Y \iff \exists f\ (f \text{ is a morphism from } T_e \text{ to } T),
$$
where $f$ ranges over functions from codes of strings to codes of strings. The condition "$f$ is a morphism" is arithmetic in $Y$ and $f$, except for the statements $f(\sigma) \in T$, which occur positively and are $\Sigma^1_1(Y)$. So the right-hand side is $\Sigma^1_1(Y)$, and $\mathcal O^Y$ would be $\Sigma^1_1(Y)$, a contradiction.
:::

:::quiz[boundedness for trees]
In the proof of :ref{#thm-sigma11-tree-bound}, why does it matter that the statements $f(\sigma) \in T$ occur positively?

- [x] A $\Sigma^1_1(Y)$ statement occurring positively inside an existential set quantifier and number quantifiers gives a $\Sigma^1_1(Y)$ formula; a negative occurrence would be $\Pi^1_1(Y)$ and would spoil the complexity.
- [ ] Because $T$ is well-founded.

  Well-foundedness is used to exclude morphisms from ill-founded trees, not to compute the complexity.
- [ ] Because morphisms preserve lengths.

  Length preservation is a computable condition on $f$, irrelevant to the complexity of $T$.

---

Where is it used that $\mathrm{rk}(T) \geq \omega_1^Y$?

- [x] To have a morphism from every $Y$-computable well-founded tree to $T$, by :ref{#lem-tree-morphism}, since these trees have ranks below $\omega_1^Y$.
- [ ] To show that ill-founded trees have no morphism to $T$.

  This only uses that $T$ is well-founded.
- [ ] To show that $T$ is $\Sigma^1_1(Y)$.

  This is a hypothesis.
:::

## Spector's theorem

:::corollary{#cor-h-omega1}
If $X \leq_h Y$, then $\omega_1^X \leq \omega_1^Y$.
:::

:::proof{of=cor-h-omega1}
Let $L$ be an $X$-computable well-ordering. The tree $D_L$ of its descending sequences is $X$-computable, hence $\Delta^1_1(Y)$, well-founded, of rank $|L|$ (:ref{#prop-descending-tree}). By :ref{#thm-sigma11-tree-bound}, $|L| < \omega_1^Y$. So $\omega_1^X \leq \omega_1^Y$.
:::

:::theorem[Spector]{#thm-spector-collapse}
For every set $Y$, $\omega_1^Y > \omega_1^{\mathrm{CK}}$ if and only if $\mathcal O \leq_h Y$.
:::

:::proof{of=thm-spector-collapse}
If $\mathcal O \leq_h Y$, then $\omega_1^Y \geq \omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$, by :ref{#cor-h-omega1} and :ref{#prop-omega1-relative}.

Conversely, suppose that $\omega_1^Y > \omega_1^{\mathrm{CK}}$. Then $\omega_1^{\mathrm{CK}}$ is the type of a $Y$-computable well-ordering $L$: some $Y$-computable well-ordering has a type $\beta \geq \omega_1^{\mathrm{CK}}$, and its initial segment of type $\omega_1^{\mathrm{CK}}$ is $Y$-computable. The tree $T = D_L$ is $Y$-computable, well-founded, of rank $\omega_1^{\mathrm{CK}}$. As in the proof of :ref{#thm-sigma11-tree-bound}, with $(T_e)$ the computable trees with $e \in \mathcal O$ if and only if $T_e$ is well-founded,
$$
e \in \mathcal O \iff \exists f\ (f \text{ is a morphism from } T_e \text{ to } T),
$$
since computable well-founded trees have ranks below $\omega_1^{\mathrm{CK}}$. The right-hand side is $\Sigma^1_1(Y)$. Since $\mathcal O$ is also $\Pi^1_1$, it is $\Delta^1_1(Y)$, that is, $\mathcal O \leq_h Y$.
:::

So the hyperdegrees split in two kinds. Those above the hyperdegree of $\mathcal O$ collapse $\omega_1^{\mathrm{CK}}$: they compute well-orderings of type $\omega_1^{\mathrm{CK}}$. The others preserve it, $\omega_1^Y = \omega_1^{\mathrm{CK}}$, and for them the hyperarithmetic sets relative to $Y$ are obtained by iterating the jump along the computable ordinals only: a notation $b \in \mathcal O^Y$ denotes a $Y$-computable ordinal, which is below $\omega_1^Y = \omega_1^{\mathrm{CK}}$ and so has a notation in $\mathcal O$. The next lesson shows that there are non-hyperarithmetic sets of the second kind.

::::exercise[Hyperarithmetic in a collapsing set]{#ex-hyp-collapse difficulty=1 objective="Use Spector's theorem to compare hyperdegrees through the ordinals they compute."}
Let $Y$ be such that $\omega_1^Y > \omega_1^{\mathrm{CK}}$. Show that every set hyperarithmetic in $\mathcal O$ is hyperarithmetic in $Y$. Show that $\mathcal O^{\mathcal O} \not\leq_h \mathcal O$, although $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$.

:::solution
By :ref{#thm-spector-collapse}, $\mathcal O \leq_h Y$, and $\leq_h$ is transitive, so every $X \leq_h \mathcal O$ satisfies $X \leq_h Y$. By :ref{#prop-hyperjump} (1) applied to $\mathcal O$, $\mathcal O <_h \mathcal O^{\mathcal O}$, so $\mathcal O^{\mathcal O} \not\leq_h \mathcal O$; and $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ by :ref{#prop-omega1-relative}. So collapsing $\omega_1^{\mathrm{CK}}$ gives $\mathcal O$, but not the next hyperjump.
:::
::::

## Notes and references

Spector (1955) proved that $\mathcal O \leq_h Y$ if and only if $\omega_1^Y > \omega_1^{\mathrm{CK}}$, and the boundedness theorem for $\Sigma^1_1$ sets of well-orderings; the version for trees with morphisms follows Monin and Patey. The hyperjump and hyperdegrees were studied by Spector, Kleene and Gandy in the 1950s and 1960s.

- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- B. Monin and L. Patey, *Computability theory*, chapters "Beyond hyperarithmetic" (sections "Other boundedness theorems" and "Hyperarithmetic reducibility").
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Part A.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015.

:::::exercises
::::exercise{#ex-hyp-wo-bound difficulty=1 objective="Apply the boundedness theorem for trees to hyperarithmetic well-orderings."}
Show that every hyperarithmetic well-ordering of a subset of $\nat$ has a computable type.

:::solution
Let $L$ be a hyperarithmetic well-ordering. The tree $D_L$ of its descending sequences is hyperarithmetic, being computable in $L$, and well-founded, of rank $|L|$ (:ref{#prop-descending-tree}). It is $\Delta^1_1$, in particular $\Sigma^1_1$, so $|L| = \mathrm{rk}(D_L) < \omega_1^{\mathrm{CK}}$ by :ref{#thm-sigma11-tree-bound}. Every ordinal below $\omega_1^{\mathrm{CK}}$ is computable. So the least non-computable ordinal is also the least ordinal that is not the type of a hyperarithmetic well-ordering.
:::
::::

::::exercise{#ex-hyperjump-monotone difficulty=1 objective="Check that the hyperjump is invariant on hyperdegrees."}
Show that if $X \equiv_h Y$, then $\mathcal O^X \equiv_m \mathcal O^Y$, and that $\omega_1^X = \omega_1^Y$.

:::solution
By :ref{#prop-hyperjump} (2) in both directions, $\mathcal O^X \leq_m \mathcal O^Y$ and $\mathcal O^Y \leq_m \mathcal O^X$. By :ref{#cor-h-omega1} in both directions, $\omega_1^X = \omega_1^Y$.
:::
::::
:::::
