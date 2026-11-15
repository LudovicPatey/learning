---
title: Countable Σ¹₁ classes
summary: Σ¹₁ singletons are hyperarithmetic, while WF is a Π¹₁ singleton; the class of hyperarithmetic sets is Π¹₁; by the effective perfect set theorem, a Σ¹₁ class with a non-hyperarithmetic member contains a perfect closed subclass, so countable Σ¹₁ classes consist of hyperarithmetic sets; relativization gives the perfect set theorem for analytic sets.
duration: 45
prerequisites: [norms, hyperarithmetic/sigma11-classes]
---

Classical descriptive set theory proves that an analytic subset of the reals is either countable or contains a perfect closed subset, hence has the cardinality of the continuum: analytic sets satisfy the continuum hypothesis. The effective version, due to Harrison, identifies the countable $\Sigma^1_1$ classes: their members are all hyperarithmetic. A $\Sigma^1_1$ class with at least one non-hyperarithmetic member has continuum many members.

The proof follows the splitting construction of the course on $\Pi^0_1$ classes (:ref{#thm-perfect-continuum}), where a perfect class is shown to contain a copy of Cantor space by finding, above each node already chosen, two incompatible extensions that are still in the class. In a closed class, the splitting can only fail above an isolated member, and isolated members of $\Pi^0_1$ classes are computable. In a $\Sigma^1_1$ class, the corresponding obstacle is a $\Sigma^1_1$ subclass with a single member, and such a member is hyperarithmetic. So the construction succeeds as soon as the hyperarithmetic members have been removed, which keeps the class $\Sigma^1_1$ because the hyperarithmetic sets form a $\Pi^1_1$ class.

## Σ¹₁ singletons

Recall that a class $\mathcal A \subseteq \cs$ is $\Sigma^1_1$ if it is defined by a formula $\exists Y\, \varphi(X, Y)$ with $\varphi$ arithmetic, possibly with number parameters (:ref{#def-sigma11-class}), and that it is then the projection of the set of paths of a computable tree $S$ of pairs: $X \in \mathcal A$ if and only if $(X, f)$ is a path of $S$ for some $f \in \nat^\nat$.

:::proposition{#prop-sigma11-singleton}
1. If $\{ X \}$ is a $\Sigma^1_1$ class, then $X$ is hyperarithmetic.
2. The class $\mathrm{HYP}$ of hyperarithmetic sets is $\Pi^1_1$.
:::

:::proof{of=prop-sigma11-singleton}
1. Let $\{ X \} = \{ Z : \exists Y\, \varphi(Z, Y) \}$. Then $n \in X$ if and only if $\exists Z\, \exists Y\, (\varphi(Z, Y) \wedge n \in Z)$, a $\Sigma^1_1$ condition, and if and only if $\forall Z\, \forall Y\, (\varphi(Z, Y) \rightarrow n \in Z)$, a $\Pi^1_1$ condition, since $X$ is the only $Z$ with a witness $Y$. So $X$ is $\Delta^1_1$, hence hyperarithmetic by :ref{#thm-kleene-delta11}.
2. This is :ref{#ex-hyp-pi11-in-x}: $X$ is hyperarithmetic if and only if there are $a$ and $e$ with $a \in \mathcal O$ and, for every $Y$ that is an H-sequence along $a$, $X = \Phi^{Y^{[a]}}_e$. By :ref{#lem-h-sequence-unique}, this expresses $X \leq_T H_a$, and the formula is $\Pi^1_1$.
:::

Conversely, every hyperarithmetic singleton is $\Sigma^1_1$, as observed after :ref{#def-sigma11-class}: if $X = \Phi^{H_a}_e$, then $\{ X \}$ is the class of sets $Z$ such that $Z = \Phi^{Y^{[a]}}_e$ for some H-sequence $Y$ along $a$. So **the $\Sigma^1_1$ singletons are exactly the hyperarithmetic sets**. In particular, the class of non-hyperarithmetic sets is $\Sigma^1_1$, by item 2.

Item 1 fails for $\Pi^1_1$ singletons. The obstacle is visible in its proof: for a $\Pi^1_1$ singleton $\{ X \} = \mathcal A$, the two definitions become "$\exists Z\, (Z \in \mathcal A \wedge n \in Z)$" and "$\forall Z\, (Z \in \mathcal A \rightarrow n \in Z)$", and in both the condition $Z \in \mathcal A$ now has the wrong complexity: the first is an existential set quantifier in front of a $\Pi^1_1$ formula, the second a universal set quantifier in front of a $\Sigma^1_1$ formula. The set $\mathrm{WF}$ of indices of well-founded computable trees (:ref{#cor-pi11-complete}) gives an example. Its definition is an inductive one: $\mathrm{WF}$ is the least set closed under the rule "if all the subtrees above the immediate successors of the root are in the set, then so is the tree". Being the least set closed under an arithmetic rule makes a set a $\Pi^1_1$ singleton, since "being contained in $\mathrm{WF}$" is $\Pi^1_1$ and "being closed under the rule" is arithmetic.

:::proposition{#prop-wf-pi11-singleton}
The class $\{ \mathrm{WF} \}$ is $\Pi^1_1$. So there is a $\Pi^1_1$ singleton that is not hyperarithmetic.
:::

:::proof{of=prop-wf-pi11-singleton}
Let $\mathrm{Tr}$ be the set of indices $e$ such that $\Phi_e$ is total, $\{0, 1\}$-valued, and the characteristic function of a tree $T_e$; it is arithmetic. By the SMN theorem, there is a computable function $s$ such that, for $e \in \mathrm{Tr}$ and every $n$, $s(e, n) \in \mathrm{Tr}$ and $T_{s(e, n)} = (T_e)_{\langle n \rangle}$. Call a set $X$ **closed** if, for every $e \in \mathrm{Tr}$ such that $s(e, n) \in X$ for every $n$ with $\langle n \rangle \in T_e$, we have $e \in X$. This is an arithmetic property of $X$. We show that $X = \mathrm{WF}$ if and only if $X \subseteq \mathrm{WF}$ and $X$ is closed; the condition $X \subseteq \mathrm{WF}$, that is, $\forall e\, (e \in X \rightarrow e \in \mathrm{WF})$, is $\Pi^1_1$, so the class $\{ \mathrm{WF} \}$ is $\Pi^1_1$.

The set $\mathrm{WF}$ is closed: if $e \in \mathrm{Tr}$ and all the trees $(T_e)_{\langle n \rangle}$ with $\langle n \rangle \in T_e$ are well-founded, then $T_e$ is well-founded, since a path of $T_e$ passes through some $\langle n \rangle$ and gives a path of $(T_e)_{\langle n \rangle}$. Conversely, let $X \subseteq \mathrm{WF}$ be closed. We show by induction on $\alpha$ that every $e \in \mathrm{WF}$ with $\mathrm{rk}(T_e) = \alpha$ belongs to $X$. For $\langle n \rangle \in T_e$, the tree $(T_e)_{\langle n \rangle}$ is well-founded of rank less than $\alpha$, by :ref{#def-tree-rank}, so $s(e, n) \in X$ by the induction hypothesis; since $X$ is closed, $e \in X$. (For a tree of rank $0$, the condition on the successors is vacuous.) So $X = \mathrm{WF}$.

Finally, $\mathrm{WF}$ is not $\Sigma^1_1$ (:ref{#prop-pi11-not-sigma11}), hence not $\Delta^1_1$, hence not hyperarithmetic.
:::

:::quiz[a Π¹₁ singleton]
In the proof of :ref{#prop-wf-pi11-singleton}, what is the role of the condition $X \subseteq \mathrm{WF}$?

- [x] Closedness alone only gives $\mathrm{WF} \subseteq X$; for instance $\nat$ is closed. The condition $X \subseteq \mathrm{WF}$ gives the other inclusion.
- [ ] It makes the class $\Sigma^1_1$.

  It is a $\Pi^1_1$ condition; the class is $\Pi^1_1$, not $\Sigma^1_1$, and by :ref{#prop-sigma11-singleton} it cannot be $\Sigma^1_1$.
- [ ] It is used in the induction on the rank.

  The induction uses only that $X$ is closed; it proves $\mathrm{WF} \subseteq X$.
:::

The set $\mathcal O$ is also a $\Pi^1_1$ singleton, by the same argument applied to the inductive definition of the notations (:ref{#def-kleene-o}), with some care for the simultaneous definition of $<_{\mathcal O}$; we do not give the details (Monin–Patey, section *Π¹₁ singletons*).

## The effective perfect set theorem

Recall that a class $\mathcal P \subseteq \cs$ is **perfect** if it is non-empty, closed and has no isolated member (:ref{#def-isolated}). A perfect class has the cardinality of the continuum (:ref{#thm-perfect-continuum}); in the proof below, this is seen directly, since the perfect class is the image of an injective continuous map from $\cs$.

:::theorem[Harrison]{#thm-effective-perfect-set}
If a $\Sigma^1_1$ class $\mathcal A$ has a member that is not hyperarithmetic, then $\mathcal A$ contains a non-empty perfect closed class. In particular, $\mathcal A$ has the cardinality of the continuum.
:::

:::proof{of=thm-effective-perfect-set}
Let $\mathcal B = \mathcal A \setminus \mathrm{HYP}$. It is a non-empty $\Sigma^1_1$ class, by :ref{#prop-sigma11-singleton}, and the projection of the paths of a computable tree $S$ of pairs $u = (\sigma, \tau) \in 2^{<\nat} \times \nat^{<\nat}$ with $|\sigma| = |\tau|$. For such a pair, let $\mathcal B_u$ be the class of sets $X$ such that $(X, f)$ is a path of $S$ extending $u$ for some $f$; it is a $\Sigma^1_1$ class, with the finite object $u$ as a parameter, included in $\mathcal B$. Call $u$ **good** if $\mathcal B_u$ is non-empty. A good pair belongs to $S$, and the empty pair is good.

*Splitting.* Let $u$ be good. The class $\mathcal B_u$ is $\Sigma^1_1$ and contains only non-hyperarithmetic sets, so by :ref{#prop-sigma11-singleton} (1) it is not a singleton: it contains $X \neq X'$, with witnesses $f$ and $f'$. Let $k$ be such that $X(k) \neq X'(k)$, and $m > \max(k, |u|)$. Then $u_0 = (X \uh m, f \uh m)$ and $u_1 = (X' \uh m, f' \uh m)$ are good, extend $u$, and their first components are incompatible.

*Construction.* Define good pairs $u_s = (\sigma_s, \tau_s)$ for $s \in 2^{<\nat}$ by $u_\emptyset = (\emptyset, \emptyset)$, and, given $u_s$, let $u_{s0}$ and $u_{s1}$ be the two pairs given by the splitting step. For $Z \in \cs$, the pairs $u_{Z \uh n}$ are increasing, and their lengths increase strictly, so they converge to a pair $(X_Z, f_Z)$. Every prefix of $(X_Z, f_Z)$ is a prefix of a good pair, hence belongs to the tree $S$; so $(X_Z, f_Z)$ is a path of $S$, and $X_Z \in \mathcal B \subseteq \mathcal A$.

*The image is perfect.* If $Z \neq Z'$, let $s$ be their longest common prefix; then $X_Z$ and $X_{Z'}$ extend $\sigma_{s0}$ and $\sigma_{s1}$, which are incompatible, so $X_Z \neq X_{Z'}$. The map $Z \mapsto X_Z$ is continuous, since $X_Z \uh n$ only depends on $Z \uh n$, because $\sigma_{Z \uh n}$ has length at least $n$. Its image $\mathcal P$ is therefore compact, hence closed. It has no isolated point: for $Z \in \cs$ and $n \in \nat$, let $Z'$ differ from $Z$ only at position $n$; then $X_{Z'} \neq X_Z$, and both extend $\sigma_{Z \uh n}$, of length at least $n$. So $\mathcal P$ is a non-empty perfect closed subclass of $\mathcal A$, in bijection with $\cs$.
:::

:::figure[The construction of :ref{#thm-effective-perfect-set}. The first components $\sigma_s$ of the good pairs $u_s$ are drawn as cylinders of Cantor space: each splits into two disjoint cylinders, those of $u_{s0}$ and $u_{s1}$. A sequence $Z$ selects a nested sequence of cylinders, and the limit $X_Z$ belongs to the class.]
<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="The first components of the good pairs u_s drawn as cylinders of Cantor space: each cylinder contains two disjoint cylinders, one for each extension of s"><line x1="120" y1="32" x2="580" y2="32" class="axis"/><text x="20" y="37" class="label">|s| = 0</text><rect x="121.0" y="22" width="458.0" height="20" class="cell head-cell"/><text x="350.0" y="37" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">ε</tspan></text><line x1="120" y1="82" x2="580" y2="82" class="axis"/><text x="20" y="87" class="label">|s| = 1</text><rect x="121.0" y="72" width="113.0" height="20" class="cell head-cell"/><text x="177.5" y="87" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">0</tspan></text><rect x="351.0" y="72" width="113.0" height="20" class="cell head-cell"/><text x="407.5" y="87" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">1</tspan></text><line x1="120" y1="132" x2="580" y2="132" class="axis"/><text x="20" y="137" class="label">|s| = 2</text><rect x="149.8" y="122" width="26.8" height="20" class="cell head-cell"/><text x="163.1" y="137" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">00</tspan></text><rect x="207.2" y="122" width="26.8" height="20" class="cell head-cell"/><text x="220.6" y="137" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">01</tspan></text><rect x="351.0" y="122" width="26.8" height="20" class="cell head-cell"/><text x="364.4" y="137" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">10</tspan></text><rect x="437.2" y="122" width="26.8" height="20" class="cell head-cell"/><text x="450.6" y="137" text-anchor="middle" class="math" font-size="13">σ<tspan class="mrm" font-size="8" dy="4">11</tspan></text><line x1="120" y1="182" x2="580" y2="182" class="axis"/><text x="20" y="187" class="label">|s| = 3</text><rect x="149.8" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="171.3" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="207.2" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="221.6" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="351.0" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="372.6" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="437.2" y="172" width="5.2" height="20" class="cell head-cell"/><rect x="458.8" y="172" width="5.2" height="20" class="cell head-cell"/><text x="224.2" y="208" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><circle cx="224.2" cy="224" r="5" class="accent-fill"/><text x="234.2" y="229" text-anchor="start" class="math" font-size="15">X<tspan class="mrm" font-size="10" dy="4">Z</tspan></text><text x="20" y="229" class="label">Z = 011…</text></svg>
:::

:::quiz[the perfect set theorem]
In the splitting step of :ref{#thm-effective-perfect-set}, why does $\mathcal B_u$ have at least two members?

- [x] Because it is a non-empty $\Sigma^1_1$ class of non-hyperarithmetic sets, and a $\Sigma^1_1$ class with exactly one member has a hyperarithmetic member.
- [ ] Because $\mathcal B$ is uncountable.

  This is the conclusion of the theorem, not a hypothesis.
- [ ] Because $S$ is infinitely branching.

  Two different paths may project to the same set; the splitting must happen in the first component, which is ensured by the singleton argument.

---

Why is the class $\mathcal A \setminus \mathrm{HYP}$ used, rather than $\mathcal A$ itself?

- [x] So that every non-empty $\Sigma^1_1$ subclass built in the construction avoids hyperarithmetic sets, and therefore splits; $\mathcal A$ may have isolated hyperarithmetic members.
- [ ] Because $\mathcal A$ is not $\Sigma^1_1$.

  $\mathcal A$ is $\Sigma^1_1$ by hypothesis.
- [ ] To make the construction effective.

  The construction is not effective in either case.
:::

The hypothesis that $\mathcal A$ is $\Sigma^1_1$ cannot be weakened to $\Pi^1_1$: the class $\{ \mathrm{WF} \}$ of :ref{#prop-wf-pi11-singleton} is a $\Pi^1_1$ class with a single member, which is not hyperarithmetic. The proof uses the hypothesis twice: to make $\mathcal A \setminus \mathrm{HYP}$ a $\Sigma^1_1$ class, and to apply :ref{#prop-sigma11-singleton} (1) to its subclasses $\mathcal B_u$.

:::corollary{#cor-countable-sigma11}
1. Every member of a countable $\Sigma^1_1$ class is hyperarithmetic.
2. If a computable tree $T \subseteq \nat^{<\nat}$ has countably many paths, they are all hyperarithmetic. A computable tree with a path but no hyperarithmetic path, as in :ref{#thm-no-hyp-path}, has continuum many paths.
:::

:::proof{of=cor-countable-sigma11}
1. This is the contrapositive of :ref{#thm-effective-perfect-set}.
2. The class of graphs of the paths of $T$ is arithmetic, hence $\Sigma^1_1$, and in bijection with the set of paths; a path is hyperarithmetic if and only if its graph is. Item 1 gives the first statement. For the second, the class of graphs has a non-hyperarithmetic member, so it has the cardinality of the continuum by :ref{#thm-effective-perfect-set}.
:::

The construction is not effective: choosing good pairs requires deciding a $\Sigma^1_1$ property. It can be carried out with the oracle $\mathcal O$: the set of good pairs is $\Sigma^1_1$, so its complement is many-one reducible to $\mathcal O$, and choosing at each step the first suitable pairs $u_{s0}, u_{s1}$ in a fixed enumeration makes the map $Z \mapsto X_Z$ computable in $\mathcal O$. This is the method of the Kleene basis theorem (:ref{#thm-kleene-basis}), applied at every node of a binary tree instead of along a single path. Since $\Pi^0_1$ classes are $\Sigma^1_1$, the corollary applies to them: all members of a countable $\Pi^0_1$ class are hyperarithmetic. This complements :ref{#cor-countable-computable}, which only gives a computable member.

::::exercise{#ex-countable-pi11 difficulty=1 objective="Combine the effective perfect set theorem with the $\Pi^1_1$ definition of $\mathrm{HYP}$ to show that countability of $\Sigma^1_1$ classes is a $\Pi^1_1$ property of their indices."}
Show that a $\Sigma^1_1$ class is countable if and only if all its members are hyperarithmetic. Let $S_e$ be the computable tree of pairs with index $e$, and $\mathcal A_e$ the projection of its paths. Show that $\{ e : \mathcal A_e \text{ is countable} \}$ is $\Pi^1_1$.

:::solution
The class $\mathrm{HYP}$ is countable (:ref{#prop-hyp-ideal}), since every hyperarithmetic set is computable in some $H_a$ by some functional. With :ref{#cor-countable-sigma11}, a $\Sigma^1_1$ class is countable if and only if it is included in $\mathrm{HYP}$. So, for an index $e$ of a tree of pairs, $\mathcal A_e$ is countable if and only if $\forall X\, \forall f\, ((X, f) \text{ is a path of } S_e \rightarrow X \in \mathrm{HYP})$. Being an index of a computable tree of pairs and being a path are arithmetic, and $X \in \mathrm{HYP}$ is $\Pi^1_1$ by :ref{#prop-sigma11-singleton}, so the whole formula is $\Pi^1_1$.
:::
::::

## The perfect set theorem for analytic sets

Every notion and result of this lesson relativizes to an oracle $Z$: the $\Sigma^1_1(Z)$ classes are defined by formulas $\exists Y\, \varphi(X, Y, Z)$ with $\varphi$ arithmetic, a $\Sigma^1_1(Z)$ singleton is $\Delta^1_1(Z)$, hence hyperarithmetic in $Z$ by the relativized Kleene theorem, and the class of sets hyperarithmetic in $Z$ is $\Pi^1_1(Z)$ and countable. The proof of :ref{#thm-effective-perfect-set} goes through with $Z$ added everywhere. Since every closed subset of $\cs \times \nat^\nat$ is the set of paths of a tree, which is computable in itself, every projection of such a closed set is $\Sigma^1_1(Z)$ for some $Z$. These projections are the **analytic** subsets of Cantor space, and the relativized theorem gives the classical result.

:::corollary[Suslin]{#cor-analytic-perfect-set}
Every analytic subset of $\cs$ is either countable or contains a non-empty perfect closed subset.
:::

:::proof{of=cor-analytic-perfect-set}
Let $\mathcal A$ be analytic, the projection of the set of paths of a tree $S$, and let $Z$ be a set computing $S$. Then $\mathcal A$ is $\Sigma^1_1(Z)$. If $\mathcal A$ is uncountable, it has a member that is not hyperarithmetic in $Z$, since only countably many sets are; by :ref{#thm-effective-perfect-set} relativized to $Z$, $\mathcal A$ contains a non-empty perfect closed subset.
:::

The effective theorem says more than the classical one: it identifies which members of a countable $\Sigma^1_1$ class can occur, namely hyperarithmetic sets, and the perfect subclass it provides is the image of a map computable in $\mathcal O$. For co-analytic sets, the perfect set theorem is not provable in ZFC; Monin and Patey discuss the largest $\Pi^1_1$ class without a perfect closed subclass (section *Study of a very special Π¹₁ class*).

## Notes and references

The perfect set theorem for analytic sets is due to Suslin (1917). Its effective form, with the characterization of the countable $\Sigma^1_1$ classes, is due to Harrison (1967), in his thesis on recursive pseudo-well-orderings; Moschovakis proves it for $\Sigma^1_1$ subsets of arbitrary recursively presented Polish spaces (Theorem 4F.1). The splitting construction can be seen as forcing with non-empty $\Sigma^1_1$ classes, a method developed by Gandy and Harrington; Monin and Patey use the same conditions, together with the Gandy basis theorem, to build sets computable in $\mathcal O$ that are incomparable for hyperarithmetic reducibility. In second-order arithmetic, the perfect set theorem for analytic sets is equivalent to $\mathsf{ATR}_0$ over $\mathsf{ACA}_0$ (Simpson, Theorems V.4.3 and V.5.5), and its proof there uses pseudo-hierarchies, as in the previous course.

- J. Harrison, *Some applications of recursive pseudo-well-orderings*, PhD thesis, Stanford University, 1967.
- J. Harrison, *Recursive pseudo-well-orderings*, Transactions of the American Mathematical Society 131 (1968), 526–543.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Section 4F.
- B. Monin and L. Patey, *Computability theory*, chapter *Σ¹₁ and Π¹₁ classes*, sections *The continuum hypothesis for Σ¹₁ classes* and *Π¹₁ singletons*.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.4–V.5.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Section 29.

:::::exercises
::::exercise{#ex-non-hyp-perfect difficulty=2 objective="Apply the effective perfect set theorem to the class of non-hyperarithmetic sets."}
Show that the class of sets that are not hyperarithmetic contains a perfect closed class, and deduce that there are continuum many sets $X$ such that $X$ is not hyperarithmetic.

:::solution
By :ref{#prop-sigma11-singleton}, the class $\cs \setminus \mathrm{HYP}$ is $\Sigma^1_1$, and it is non-empty, since $\mathrm{HYP}$ is countable. By :ref{#thm-effective-perfect-set}, it contains a non-empty perfect closed class, which is in bijection with $\cs$ by the proof of the theorem.
:::
::::

::::exercise{#ex-finite-sigma11 difficulty=1 objective="Show without the perfect set theorem that isolated members of $\Sigma^1_1$ classes are hyperarithmetic, as isolated members of $\Pi^0_1$ classes are computable."}
Show that every isolated member of a $\Sigma^1_1$ class (:ref{#def-isolated}) is hyperarithmetic, without using :ref{#thm-effective-perfect-set}. Deduce that all members of a finite $\Sigma^1_1$ class are hyperarithmetic.

:::solution
Let $X$ be an isolated member of a $\Sigma^1_1$ class $\mathcal A = \{ Z : \exists Y\, \varphi(Z, Y) \}$, and $\sigma \prec X$ with $[\sigma] \cap \mathcal A = \{ X \}$. The class $[\sigma] \cap \mathcal A$ is defined by $\exists Y\, (\sigma \prec Z \wedge \varphi(Z, Y))$, where $\sigma$ is a fixed finite string, so "$\sigma \prec Z$" is an arithmetic formula; it is a $\Sigma^1_1$ class with the single member $X$, and $X$ is hyperarithmetic by :ref{#prop-sigma11-singleton} (1). If $\mathcal A = \{ X_1, \dots, X_k \}$ is finite with the $X_i$ distinct, choose $\ell$ such that the prefixes $X_i \uh \ell$ are pairwise distinct; then $[X_i \uh \ell] \cap \mathcal A = \{ X_i \}$, so every member is isolated, hence hyperarithmetic. This is the analogue of the fact that isolated members of $\Pi^0_1$ classes are computable; :ref{#thm-effective-perfect-set} is needed for countable classes, whose members need not be isolated.
:::
::::

::::exercise{#ex-o-computable-members difficulty=1 objective="Combine the splitting step with the Kleene basis theorem to find many non-hyperarithmetic members computable in $\mathcal O$."}
Show that every uncountable $\Sigma^1_1$ class $\mathcal A$ has infinitely many members that are computable in $\mathcal O$ and not hyperarithmetic.

:::solution
Since $\mathrm{HYP}$ is countable (:ref{#prop-hyp-ideal}), the class $\mathcal B = \mathcal A \setminus \mathrm{HYP}$ is non-empty, and it is $\Sigma^1_1$ by :ref{#prop-sigma11-singleton} (2). Write it as in the proof of :ref{#thm-effective-perfect-set}, with the classes $\mathcal B_u$ and good pairs $u$. Apply the splitting step repeatedly: starting from the empty pair $v_0$, given a good pair $v_i$, let $u_i$ and $v_{i+1}$ be the two good extensions of $v_i$ given by the splitting step, with incompatible first components. For $i < j$, the first component of $u_j$ extends that of $v_{i+1}$, which is incompatible with that of $u_i$; so the classes $\mathcal B_{u_i}$ are pairwise disjoint. Each of them is a non-empty $\Sigma^1_1$ class, so it has a member $X_i$ computable in $\mathcal O$ by the Kleene basis theorem (:ref{#thm-kleene-basis}). The sets $X_i$ are pairwise distinct, belong to $\mathcal B \subseteq \mathcal A$, and are not hyperarithmetic.
:::
::::

::::exercise{#ex-pi11-singletons-closure difficulty=2 objective="Show that the $\Pi^1_1$ singletons are closed under join and jump, and obtain more non-hyperarithmetic $\Pi^1_1$ singletons."}
Show that if $\{ X \}$ and $\{ Y \}$ are $\Pi^1_1$ classes, then so are $\{ X \oplus Y \}$ and $\{ X' \}$. Deduce that $\mathrm{WF}'$, $\mathrm{WF}''$, … are $\Pi^1_1$ singletons that are not hyperarithmetic.

:::solution
Let $\{ X \} = \{ W : \forall V\, \varphi(W, V) \}$ and $\{ Y \} = \{ W : \forall V\, \psi(W, V) \}$ with $\varphi$ and $\psi$ arithmetic. For a set $Z$, write $Z_0 = \{ n : 2n \in Z \}$ and $Z_1 = \{ n : 2n + 1 \in Z \}$. Then $Z = X \oplus Y$ if and only if $Z_0 = X$ and $Z_1 = Y$, that is, $\forall V\, \varphi(Z_0, V) \wedge \forall V\, \psi(Z_1, V)$. Replacing each atomic formula $n \in Z_0$ by $2n \in Z$ (and $n \in Z_1$ by $2n + 1 \in Z$) gives arithmetic formulas in $Z$ and $V$, so the class $\{ X \oplus Y \}$ is $\Pi^1_1$.

For the jump, let $h$ be a total computable function such that, for every oracle $W$ and every $n$, the program $h(n)$ with oracle $W$ halts on every input if $n \in W$ and on no input otherwise; it exists by the SMN theorem. Then $h(n) \in W'$ if and only if $n \in W$. For a set $Z$, let $W_Z = \{ n : h(n) \in Z \}$. We claim that $Z = X'$ if and only if $W_Z = X$ and $Z = (W_Z)'$. If $Z = X'$, then $W_Z = \{ n : h(n) \in X' \} = X$ and $Z = X' = (W_Z)'$. Conversely, the two conditions give $Z = (W_Z)' = X'$. The condition $Z = (W_Z)'$, that is, $\forall e\, (e \in Z \leftrightarrow \Phi^{W_Z}_e(e)\converge)$, is arithmetic in $Z$, since $W_Z$ is many-one reducible to $Z$; and $W_Z = X$ is $\forall V\, \varphi(W_Z, V)$, which is $\Pi^1_1$ in $Z$ after replacing $n \in W_Z$ by $h(n) \in Z$. So $\{ X' \}$ is $\Pi^1_1$.

By :ref{#prop-wf-pi11-singleton} and induction, $\{ \mathrm{WF}^{(k)} \}$ is $\Pi^1_1$ for every $k$. None of these sets is hyperarithmetic, since $\mathrm{WF} \leq_T \mathrm{WF}^{(k)}$ and $\mathrm{HYP}$ is closed downward under $\leq_T$ (:ref{#prop-hyp-ideal}).
:::
::::

::::exercise{#ex-countability-not-sigma11 difficulty=2 objective="Show that the $\Pi^1_1$ bound on the complexity of countability for $\Sigma^1_1$ classes cannot be improved."}
Let $\mathrm{Tr}$ be the set of numbers $e$ such that $\Phi_e$ is total, $\{0, 1\}$-valued, and the characteristic function of a tree $T_e \subseteq \nat^{<\nat}$ containing the empty sequence. For $e \in \mathrm{Tr}$, let $\mathcal C_e$ be the class of sets $X$ such that $\{ n : 2n \in X \}$ is the graph $\{ \langle i, f(i) \rangle : i \in \nat \}$ of a path $f$ of $T_e$. Show that $\mathcal C_e$ is $\Sigma^1_1$, that it is countable if and only if $T_e$ is well-founded, and that $\{ e \in \mathrm{Tr} : \mathcal C_e \text{ is countable} \}$ is $\Pi^1_1$ but not $\Sigma^1_1$.

:::solution
"$\{ n : 2n \in X \}$ is the graph of a function $f$" says that for every $i$ there is exactly one $k$ with $2 \langle i, k \rangle \in X$, and "$f$ is a path of $T_e$" says that for every $\ell$, the sequence of the values $f(0), \dots, f(\ell - 1)$, read off $X$, belongs to $T_e$. Both are arithmetic in $X$ and $e$, so $\mathcal C_e$ is arithmetic, hence $\Sigma^1_1$ (with a dummy existential set quantifier).

If $T_e$ is well-founded, $\mathcal C_e$ is empty. If $f$ is a path of $T_e$, with graph $G$, then for every set $Z$, the set $G \oplus Z$ belongs to $\mathcal C_e$, and $Z \mapsto G \oplus Z$ is injective; so $\mathcal C_e$ has the cardinality of the continuum.

So $\{ e \in \mathrm{Tr} : \mathcal C_e \text{ is countable} \}$ is the set $\mathrm{WF}^+$ of $e \in \mathrm{Tr}$ with $T_e$ well-founded, which is $\Pi^1_1$. It is not $\Sigma^1_1$: let $A$ be a $\Pi^1_1$ set that is not $\Sigma^1_1$ (:ref{#prop-pi11-not-sigma11}), and $(T'_n)$ uniformly computable trees containing the empty sequence with $n \in A$ if and only if $T'_n$ is well-founded (:ref{#thm-pi11-normal-form}); by the SMN theorem, there is a computable function $h$ with $h(n) \in \mathrm{Tr}$ and $T_{h(n)} = T'_n$, so $A = \{ n : h(n) \in \mathrm{WF}^+ \}$ would be $\Sigma^1_1$ if $\mathrm{WF}^+$ were. Thus the $\Pi^1_1$ definition of :ref{#ex-countable-pi11} is optimal.
:::
::::

::::exercise{#ex-countable-pi01-coding difficulty=2 objective="Code the paths of a computable tree of Baire space into a $\Pi^0_1$ class of Cantor space, at the cost of countably many computable members."}
For $f \in \nat^\nat$, let $c(f) = 1^{f(0)}\, 0\, 1^{f(1)}\, 0 \cdots \in \cs$, where $1^k$ is the string of $k$ ones, and for $\tau \in \nat^{<\nat}$, let $c(\tau) = 1^{\tau(0)}\, 0 \cdots 1^{\tau(|\tau| - 1)}\, 0$. Let $T \subseteq \nat^{<\nat}$ be a computable tree, and $S = \{ c(\tau)\, 1^j : \tau \in T,\ j \in \nat \}$.

1. Show that $S$ is a computable binary tree and that
$$
[S] = \{ c(f) : f \in [T] \} \cup \{ c(\tau)\, 1^\infty : \tau \in T \},
$$
where $1^\infty$ is the infinite sequence of ones.
2. Deduce that if $T$ has countably many paths, there is a countable $\Pi^0_1$ class $\mathcal P \subseteq \cs$ such that every path of $T$ is Turing equivalent to a member of $\mathcal P$, and every member of $\mathcal P$ is computable or Turing equivalent to a path of $T$.

:::solution
1. Every binary string $\sigma$ can be written in exactly one way as $c(\tau)\, 1^j$: $\tau$ lists the numbers of ones before each zero of $\sigma$, and $j$ is the number of ones after the last zero. So $\sigma \in S$ if and only if the sequence $\tau$ read off $\sigma$ belongs to $T$, which is decidable. A prefix of $c(\tau)\, 1^j$ is either $c(\tau)\, 1^{j'}$ with $j' \leq j$, or $c(\tau \uh i)\, 1^{j'}$ with $i < |\tau|$ and $j' \leq \tau(i)$; since $T$ is closed under prefixes, it belongs to $S$. So $S$ is a tree.

Let $X \in \cs$. If $X$ has infinitely many zeros, then $X = c(f)$ for a unique $f \in \nat^\nat$. If $f \in [T]$, every prefix of $X$ is a prefix of some $c(f \uh i)$, which is in $S$, so $X \in [S]$. Conversely, if $X \in [S]$, then $c(f \uh i) \prec X$ belongs to $S$ for every $i$, and by uniqueness of the decomposition (with $j = 0$), $f \uh i \in T$; so $f \in [T]$. If $X$ has finitely many zeros, then $X = c(\tau)\, 1^\infty$ for a unique $\tau$, and its prefixes are the prefixes of the strings $c(\tau)\, 1^j$. They all belong to $S$ if $\tau \in T$; and if $X \in [S]$, then $c(\tau) \in S$, so $\tau \in T$.

2. Let $\mathcal P = [S]$, a $\Pi^0_1$ class. If $T$ has countably many paths, $\mathcal P$ is countable, since $T$ is countable. The map $c$ is computable, and $f$ is computed from $c(f)$ by counting the ones between consecutive zeros, so $c(f) \equiv_T f$. The members $c(\tau)\, 1^\infty$ are computable. By :ref{#cor-countable-sigma11} (2), the paths of $T$ are hyperarithmetic; the coding shows that the members of countable $\Pi^0_1$ classes of Cantor space are as complicated as the paths of computable trees with countably many paths. Adapted from Monin–Patey, chapter *Σ¹₁ and Π¹₁ classes*, section *The continuum hypothesis for Σ¹₁ classes*; the coding $c$ is the one used in the course on $\Pi^0_1$ classes for finitely branching trees.
:::
::::

::::exercise{#ex-perfect-subclass-tree difficulty=2 objective="See that the perfect class given by the effective perfect set theorem cannot in general be a $\Pi^0_1$ class, or even the set of paths of a hyperarithmetic tree."}
Show that the class of non-hyperarithmetic sets contains no non-empty class of the form $[T]$ with $T \subseteq 2^{<\nat}$ a hyperarithmetic tree. Deduce that in :ref{#thm-effective-perfect-set}, the perfect closed class cannot in general be chosen to be a $\Pi^0_1$ class. Show that the tree of the perfect class built in the proof is computable in $\mathcal O$ when the construction is carried out with the oracle $\mathcal O$.

:::solution
Let $T \subseteq 2^{<\nat}$ be a hyperarithmetic tree with $[T] \neq \emptyset$. The class $[T]$ is a $\Pi^0_1$ class relative to $T$, so by :ref{#prop-leftmost-path} relativized to $T$, it has a member computable in $T'$. Since $\mathrm{HYP}$ is closed under the jump and downward under $\leq_T$ (:ref{#prop-hyp-ideal}), this member is hyperarithmetic. So $[T]$ is not included in the class of non-hyperarithmetic sets. Applied to $\mathcal A = \cs \setminus \mathrm{HYP}$, which is $\Sigma^1_1$ and has non-hyperarithmetic members (:ref{#ex-non-hyp-perfect}), this shows that no perfect closed subclass of $\mathcal A$ is a $\Pi^0_1$ class, or the set of paths of any hyperarithmetic tree.

For the last part, let $\mathcal P = \{ X_Z : Z \in \cs \}$ be built with the oracle $\mathcal O$, so that the map $s \mapsto \sigma_s$ is computable in $\mathcal O$. Every $X_Z$ extends $\sigma_{Z \uh n}$, which has length at least $n$. So a string $\tau$ of length $n$ is a prefix of a member of $\mathcal P$ if and only if $\tau \preceq \sigma_s$ for some $s \in 2^n$: if $\tau \prec X_Z$, take $s = Z \uh n$; conversely, if $\tau \preceq \sigma_s$ with $|s| = n$, then $\tau \prec X_Z$ for any $Z$ extending $s$. This is decided by $\mathcal O$, by computing the finitely many strings $\sigma_s$, $s \in 2^n$. So the tree $\{ \tau : [\tau] \cap \mathcal P \neq \emptyset \}$, whose set of paths is $\mathcal P$, is computable in $\mathcal O$.
:::
::::

::::exercise{#ex-turing-incomparable-o difficulty=3 objective="Adapt the splitting construction with $\Sigma^1_1$ classes to build Turing incomparable non-hyperarithmetic sets computable in $\mathcal O$."}
Show that there are sets $X$ and $Y$, both computable in $\mathcal O$ and not hyperarithmetic, such that $X \not\leq_T Y$ and $Y \not\leq_T X$.

:::solution
Let $\mathcal B = \cs \setminus \mathrm{HYP}$, a non-empty $\Sigma^1_1$ class (:ref{#prop-sigma11-singleton}, :ref{#prop-hyp-ideal}), written as the projection of the paths of a computable tree $S$ of pairs, with the classes $\mathcal B_u$ and the good pairs of the proof of :ref{#thm-effective-perfect-set}. For a pair $u = (\sigma, \tau)$, call $\sigma$ its first component. We use four facts.

(a) Questions of the form "is there a path $(Z, g)$ of $S$ extending $u$ such that $\theta$", with $\theta$ arithmetic and $u$ and other numbers as parameters, are $\Sigma^1_1$, so they are decided by $\mathcal O$: a $\Sigma^1_1$ set has a $\Pi^1_1$ complement, which is many-one reducible to $\mathcal O$ by :ref{#thm-o-complete}. In particular, $\mathcal O$ decides whether a pair is good.

(b) A good pair $u$ has good extensions of every length: if $(Z, g)$ is a path of $S$ extending $u$, its prefixes $(Z \uh m, g \uh m)$ are good.

(c) For a good pair $u$, the class $\mathcal B_u$ has two members, by the splitting step of the proof of :ref{#thm-effective-perfect-set}; so there are $k$ and good extensions $u^0$, $u^1$ of $u$ whose first components have length greater than $k$ and take the values $0$ and $1$ at $k$.

(d) Let $v$ be good, and $e, k \in \nat$, $i < 2$. If some $Y \in \mathcal B_v$ satisfies $\Phi^Y_e(k)\converge = i$, then there is a good extension $v'$ of $v$ whose first component $\sigma'$ satisfies $\Phi^{\sigma'}_e(k)\converge = i$, meaning that the computation halts in at most $|\sigma'|$ steps and only queries the oracle below $|\sigma'|$. Then $\Phi^{Y'}_e(k) = i$ for every $Y' \in \mathcal B_{v'}$. Indeed, take a witness $(Y, g)$ and $m$ large, and $v' = (Y \uh m, g \uh m)$.

*Construction.* We build good pairs $u_0, u_1, \dots$ and $v_0, v_1, \dots$, each extending the previous one, starting with empty pairs, and with $|u_{t+1}| > |u_t|$, $|v_{t+1}| > |v_t|$. At stage $t = 2e$, we make $X \neq \Phi^Y_e$. By (c), choose $k$ and good extensions $u^0$, $u^1$ of $u_t$ as there. Ask $\mathcal O$ whether some $Y \in \mathcal B_{v_t}$ satisfies $\Phi^Y_e(k)\converge = 0$, and then whether some satisfies $\Phi^Y_e(k)\converge = 1$. If one of these holds for some $i < 2$ (the first one found), let $v_{t+1}$ be a good extension of $v_t$ as in (d), and $u_{t+1}$ a good extension of $u^{1-i}$. Otherwise, let $u_{t+1}$ and $v_{t+1}$ be any good proper extensions of $u_t$ and $v_t$, given by (b). At stage $t = 2e + 1$, do the same with the roles of the two sequences exchanged, to make $Y \neq \Phi^X_e$. Each choice is a search among finitely many objects at a time for pairs that $\mathcal O$ declares good, or for computations that halt; the searches terminate by (b), (c) and (d). So the sequences $(u_t)$ and $(v_t)$ are computable in $\mathcal O$.

*Verification.* Let $X$ and $Y$ be the unions of the first components of the $u_t$ and of the $v_t$, and $f$, $g$ the unions of the second components. As in the proof of :ref{#thm-effective-perfect-set}, every prefix of $(X, f)$ is a prefix of a good pair, so $(X, f)$ is a path of $S$ and $X \in \mathcal B$; likewise $Y \in \mathcal B$. Both are computable in $\mathcal O$ and not hyperarithmetic. At stage $2e$, $(Y, g)$ is a path of $S$ extending $v_t$, so $Y \in \mathcal B_{v_t}$. In the first case, $Y \in \mathcal B_{v_{t+1}}$, so $\Phi^Y_e(k) = i$ by (d), while $X$ extends the first component of $u^{1-i}$ and $X(k) = 1 - i$. In the second case, $\Phi^Y_e(k)$ is undefined or not in $\{0, 1\}$, while $X(k) \in \{0, 1\}$. In both cases $X \neq \Phi^Y_e$. Symmetrically, $Y \neq \Phi^X_e$ for every $e$.

The splitting of (c), which relies on the absence of hyperarithmetic members, is what allows the value of $X$ at $k$ to be chosen. Monin and Patey give a variant for hyperarithmetic reducibility, with conditions that are $\Sigma^1_1$ classes (chapter *Σ¹₁ and Π¹₁ classes*, section *The continuum hypothesis for Σ¹₁ classes*).
:::
::::
:::::
