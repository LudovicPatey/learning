---
title: Hyperarithmetic reducibility and the hyperjump
summary: Hyperarithmetic reducibility and the hyperjump; a well-founded tree that is Σ¹₁ relative to a set has rank below the Church–Kleene ordinal of that set; hyperarithmetic reducibility preserves the Church–Kleene ordinal; Spector's theorem that a set computes O hyperarithmetically exactly when it collapses ω₁ᶜᵏ.
duration: 30
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

:::example{#ex-h-examples}
1. For every $a \in \mathcal O$, $H_a \leq_h \emptyset$; in particular $\emptyset^{(\omega)} \leq_h \emptyset$, although $\emptyset^{(\omega)}$ is computable in no finite jump $\emptyset^{(n)}$. Hyperarithmetic reducibility ignores all the jumps along computable ordinals.
2. Relativizing, $Y^{(n)}$, $Y^{(\omega)}$ and every $H^Y_a$ with $a \in \mathcal O^Y$ are hyperarithmetic in $Y$.
3. $\mathcal O \not\leq_h \emptyset$, since $\mathcal O$ is not $\Sigma^1_1$, but $\mathcal O \leq_T \mathcal O$; so the hyperdegree of $\mathcal O$ is not the least one. The set $\mathcal O$ is the hyperjump of $\emptyset$.
:::

:::proposition{#prop-hyperjump}
1. $Y \leq_m \mathcal O^Y$ and $Y <_h \mathcal O^Y$.
2. $X \leq_h Y$ if and only if $\mathcal O^X \leq_m \mathcal O^Y$.
:::

:::proof{of=prop-hyperjump}
1. The set $Y$ is $\Pi^1_1(Y)$, so it is many-one reducible to the $\Pi^1_1(Y)$-complete set $\mathcal O^Y$. If $\mathcal O^Y \leq_h Y$, then $\mathcal O^Y$ would be $\Sigma^1_1(Y)$, which it is not.
2. If $X$ is $\Delta^1_1(Y)$, the set $\mathcal O^X$, which is $\Pi^1_1(X)$, is $\Pi^1_1(Y)$ by substitution of the definitions of $X$; so $\mathcal O^X \leq_m \mathcal O^Y$ by completeness. Conversely, suppose that $\mathcal O^X \leq_m \mathcal O^Y$. The set $X$ and its complement are $\Pi^1_1(X)$, so they are many-one reducible to the $\Pi^1_1(X)$-complete set $\mathcal O^X$, hence to $\mathcal O^Y$. A set many-one reducible to $\mathcal O^Y$ is $\Pi^1_1(Y)$, so $X$ and its complement are $\Pi^1_1(Y)$, and $X$ is $\Delta^1_1(Y)$.
:::

The analogy with the Turing jump is close: $Y <_T Y'$ and $X \leq_T Y$ implies $X' \leq_m Y'$. But the hyperjump is much stronger than any iterate of the jump: $Y^{(\alpha)} \leq_T H^Y_a$ for every $\alpha = |a|$ with $a \in \mathcal O^Y$, and all these sets are hyperarithmetic in $Y$, hence below $\mathcal O^Y$.

## Boundedness for trees

For trees $S$ and $T$ on $\nat$, a **morphism** from $S$ to $T$ is a map $f : S \to T$ that preserves lengths and the prefix order: $|f(\sigma)| = |\sigma|$, and $f(\sigma) \preceq f(\tau)$ whenever $\sigma \preceq \tau$. A morphism maps every path of $S$ to a path of $T$, so if $T$ is well-founded and there is a morphism from $S$ to $T$, then $S$ is well-founded. For well-founded trees, morphisms compare ranks: a morphism exists as soon as the rank of $S$ is at most the rank of $T$, and the converse holds as well (:ref{to="pi11-singletons"}). A morphism need not be injective: two branches of $S$ may follow the same branch of $T$, as in the figure below.

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

:::figure[A morphism from $S$ to $T$, built as in the proof of :ref{#lem-tree-morphism}. Each node of $S$ goes to the leftmost child of the image of its parent whose rank is at least its own: both children of the root of $S$ go to the child of rank $1$ of the root of $T$.]
<svg class="fig" viewBox="0 0 600 240" width="600" role="img" aria-label="Two trees S and T with their ranks; dashed arrows map each node of S to a node of T of the same length and of rank at least as large; both children of the root of S are mapped to the same child of the root of T"><defs><marker id="tm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><text x="40" y="30" text-anchor="middle" class="math">S</text><line x1="140" y1="50" x2="100" y2="120" class="ink-stroke" stroke-width="1.2"/><line x1="140" y1="50" x2="180" y2="120" class="ink-stroke" stroke-width="1.2"/><line x1="100" y1="120" x2="100" y2="190" class="ink-stroke" stroke-width="1.2"/><circle cx="140" cy="50" r="9" class="node"/><text x="140" y="54" text-anchor="middle" class="mrm" font-size="11">2</text><circle cx="100" cy="120" r="9" class="node"/><text x="100" y="124" text-anchor="middle" class="mrm" font-size="11">1</text><circle cx="180" cy="120" r="9" class="node"/><text x="180" y="124" text-anchor="middle" class="mrm" font-size="11">0</text><circle cx="100" cy="190" r="9" class="node"/><text x="100" y="194" text-anchor="middle" class="mrm" font-size="11">0</text><text x="580" y="30" text-anchor="middle" class="math">T</text><line x1="450" y1="50" x2="400" y2="120" class="ink-stroke" stroke-width="1.2"/><line x1="450" y1="50" x2="460" y2="120" class="ink-stroke" stroke-width="1.2"/><line x1="450" y1="50" x2="520" y2="120" class="ink-stroke" stroke-width="1.2"/><line x1="400" y1="120" x2="370" y2="190" class="ink-stroke" stroke-width="1.2"/><line x1="400" y1="120" x2="430" y2="190" class="ink-stroke" stroke-width="1.2"/><circle cx="450" cy="50" r="9" class="node"/><text x="450" y="54" text-anchor="middle" class="mrm" font-size="11">2</text><circle cx="400" cy="120" r="9" class="node"/><text x="400" y="124" text-anchor="middle" class="mrm" font-size="11">1</text><circle cx="460" cy="120" r="9" class="node"/><text x="460" y="124" text-anchor="middle" class="mrm" font-size="11">0</text><circle cx="520" cy="120" r="9" class="node"/><text x="520" y="124" text-anchor="middle" class="mrm" font-size="11">0</text><circle cx="370" cy="190" r="9" class="node"/><text x="370" y="194" text-anchor="middle" class="mrm" font-size="11">0</text><circle cx="430" cy="190" r="9" class="node"/><text x="430" y="194" text-anchor="middle" class="mrm" font-size="11">0</text><path d="M151,50 Q295,50 438,50" class="accent-stroke" fill="none" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#tm-arrow)"/><path d="M111,120 Q250,75 388,120" class="accent-stroke" fill="none" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#tm-arrow)"/><path d="M191,120 Q290,150 388,120" class="accent-stroke" fill="none" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#tm-arrow)"/><path d="M111,190 Q235,190 358,190" class="accent-stroke" fill="none" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#tm-arrow)"/><text x="300" y="232" text-anchor="middle" class="label">numbers in the nodes: ranks; dashed arrows: the morphism f</text></svg>
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

The proof gives more than the equivalence: when $\omega_1^Y > \omega_1^{\mathrm{CK}}$, the definition of $\mathcal O$ as a $\Sigma^1_1(Y)$ set is obtained from any $Y$-computable well-ordering of type at least $\omega_1^{\mathrm{CK}}$. The ordinal $\omega_1^{\mathrm{CK}}$ itself is used as a bound: all computable well-founded trees fit below a single $Y$-computable tree.

:::quiz[Spector's theorem]
In the proof of :ref{#thm-spector-collapse}, why can the tree $T = D_L$ be used in place of an arbitrary $\Sigma^1_1(Y)$ tree?

- [x] It only needs to be $\Sigma^1_1(Y)$ and well-founded of rank at least every computable ordinal; a $Y$-computable tree is $\Sigma^1_1(Y)$, and its rank $\omega_1^{\mathrm{CK}}$ bounds the ranks of the computable well-founded trees.
- [ ] Because $D_L$ has rank exactly $\omega_1^{\mathrm{CK}}$, and a larger rank would not work.

  Any $Y$-computable well-founded tree of rank at least $\omega_1^{\mathrm{CK}}$ works: the morphisms only need enough room.
- [ ] Because $D_L$ is computable.

  It is $Y$-computable, not computable; a computable well-founded tree has computable rank, which would be too small.
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
::::exercise{#ex-h-kleene-relativized difficulty=1 objective="Restate hyperarithmetic reducibility through the relativized hierarchy."}
Show that $X \leq_h Y$ if and only if $X \leq_T H^Y_a$ for some $a \in \mathcal O^Y$, and that $X \leq_h Y$ if and only if $X \leq_T Y^{(\alpha)}$ for some $Y$-computable ordinal $\alpha$, where $Y^{(\alpha)}$ denotes $H^Y_a$ for any notation $a \in \mathcal O^Y$ of $\alpha$.

:::solution
The first equivalence is Kleene's theorem relativized to $Y$: a set is $\Delta^1_1(Y)$ if and only if it is computable in some $H^Y_a$ with $a \in \mathcal O^Y$. For the second, the ordinals $|a|$ with $a \in \mathcal O^Y$ are exactly the $Y$-computable ordinals (Markwald–Kleene relativized), and by Spector's uniqueness theorem relativized, $H^Y_a \equiv_T H^Y_b$ when $|a| = |b|$, so $Y^{(\alpha)}$ is well defined up to Turing equivalence.
:::
::::

::::exercise{#ex-h-join difficulty=1 objective="Check that the hyperdegrees form an upper semilattice."}
Show that $X \oplus Y$ is a least upper bound of $X$ and $Y$ for $\leq_h$: $X, Y \leq_h X \oplus Y$, and $X \oplus Y \leq_h Z$ whenever $X \leq_h Z$ and $Y \leq_h Z$.

:::solution
$X$ and $Y$ are computable in $X \oplus Y$, hence hyperarithmetic in it. If $X$ and $Y$ are $\Delta^1_1(Z)$, then $n \in X \oplus Y$ if and only if ($n = 2k$ and $k \in X$) or ($n = 2k + 1$ and $k \in Y$), a Boolean combination of $\Delta^1_1(Z)$ statements with a computable case distinction, so $X \oplus Y$ is $\Sigma^1_1(Z)$ and $\Pi^1_1(Z)$.
:::
::::

::::exercise{#ex-pi11-tree-unbounded difficulty=2 objective="See why the hypothesis Σ¹₁ is needed in the boundedness theorem for trees."}
Let $\mathrm{WF}$ be the set of indices $e$ such that $\Phi_e$ is the characteristic function of a well-founded tree $T_e$ containing the empty string. Let $T$ be the set of the strings $e \sigma$ (the string $\sigma$ preceded by the number $e$) with $e \in \mathrm{WF}$ and $\sigma \in T_e$, together with the empty string. Show that $T$ is a well-founded $\Pi^1_1$ tree of rank $\omega_1^{\mathrm{CK}}$. Which step of the proof of :ref{#thm-sigma11-tree-bound} fails for $T$?

:::solution
$T$ is closed under prefixes, since each $T_e$ is and contains the empty string, and a path of $T$ would be $e$ followed by a path of $T_e$ with $e \in \mathrm{WF}$, which does not exist: $T$ is well-founded. Membership is $\Pi^1_1$: $\tau \in T$ if and only if $\tau$ is empty or $\tau = e \sigma$ with $e \in \mathrm{WF}$ and $\sigma \in T_e$, and $\mathrm{WF}$ is $\Pi^1_1$. The subtree of $T$ above the node $e$ is $T_e$, so $\mathrm{rk}(T) = \sup \{ \mathrm{rk}(T_e) + 1 : e \in \mathrm{WF} \}$. The ranks of computable well-founded trees are exactly the computable ordinals (:ref{#prop-rank-computable}), and every computable tree has an index; so the supremum is $\omega_1^{\mathrm{CK}}$. In the proof of :ref{#thm-sigma11-tree-bound}, the statements $f(\sigma) \in T$ occur positively, and they are now $\Pi^1_1$: the formula $\exists f\, (f \text{ is a morphism from } T_e \text{ to } T)$ is $\Sigma^1_2$, not $\Sigma^1_1$, and no contradiction follows.
:::
::::

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
