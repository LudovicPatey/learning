---
title: Countable Σ¹₁ classes
summary: Σ¹₁ singletons are hyperarithmetic, while WF is a Π¹₁ singleton; the class of hyperarithmetic sets is Π¹₁; by the effective perfect set theorem, a Σ¹₁ class with a non-hyperarithmetic member contains a perfect closed subclass, so countable Σ¹₁ classes consist of hyperarithmetic sets; relativization gives the perfect set theorem for analytic sets.
duration: 50
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
2. This is the second exercise of :ref{to="hyperarithmetic/kleene-theorem"}: $X$ is hyperarithmetic if and only if there are $a$ and $e$ with $a \in \mathcal O$ and, for every $Y$ that is an H-sequence along $a$, $X = \Phi^{Y^{[a]}}_e$. By :ref{#lem-h-sequence-unique}, this expresses $X \leq_T H_a$, and the formula is $\Pi^1_1$.
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

## The perfect set theorem for analytic sets

Every notion and result of this lesson relativizes to an oracle $Z$: the $\Sigma^1_1(Z)$ classes are defined by formulas $\exists Y\, \varphi(X, Y, Z)$ with $\varphi$ arithmetic, a $\Sigma^1_1(Z)$ singleton is $\Delta^1_1(Z)$, hence hyperarithmetic in $Z$ by the relativized Kleene theorem, and the class of sets hyperarithmetic in $Z$ is $\Pi^1_1(Z)$ and countable. The proof of :ref{#thm-effective-perfect-set} goes through with $Z$ added everywhere. Since every closed subset of $\cs \times \nat^\nat$ is the set of paths of a tree, which is computable in itself, every projection of such a closed set is $\Sigma^1_1(Z)$ for some $Z$. These projections are the **analytic** subsets of Cantor space, and the relativized theorem gives the classical result.

:::corollary[Suslin]{#cor-analytic-perfect-set}
Every analytic subset of $\cs$ is either countable or contains a non-empty perfect closed subset.
:::

:::proof{of=cor-analytic-perfect-set}
Let $\mathcal A$ be analytic, the projection of the set of paths of a tree $S$, and let $Z$ be a set computing $S$. Then $\mathcal A$ is $\Sigma^1_1(Z)$. If $\mathcal A$ is uncountable, it has a member that is not hyperarithmetic in $Z$, since only countably many sets are; by :ref{#thm-effective-perfect-set} relativized to $Z$, $\mathcal A$ contains a non-empty perfect closed subset.
:::

The effective theorem says more than the classical one: it identifies which members of a countable $\Sigma^1_1$ class can occur, namely hyperarithmetic sets, and the perfect subclass it provides is the image of a map computable in $\mathcal O$. For co-analytic sets, the perfect set theorem is not provable in ZFC; Monin and Patey discuss the largest $\Pi^1_1$ class without a perfect closed subclass (section *Study of a very special Π¹₁ class*).

## Exercises

::::exercise{difficulty=1}
Show that a $\Sigma^1_1$ class is countable if and only if all its members are hyperarithmetic. Let $S_e$ be the computable tree of pairs with index $e$, and $\mathcal A_e$ the projection of its paths. Show that $\{ e : \mathcal A_e \text{ is countable} \}$ is $\Pi^1_1$.

:::solution
The class $\mathrm{HYP}$ is countable (:ref{#prop-hyp-ideal}), since every hyperarithmetic set is computable in some $H_a$ by some functional. With :ref{#cor-countable-sigma11}, a $\Sigma^1_1$ class is countable if and only if it is included in $\mathrm{HYP}$. So, for an index $e$ of a tree of pairs, $\mathcal A_e$ is countable if and only if $\forall X\, \forall f\, ((X, f) \text{ is a path of } S_e \rightarrow X \in \mathrm{HYP})$. Being an index of a computable tree of pairs and being a path are arithmetic, and $X \in \mathrm{HYP}$ is $\Pi^1_1$ by :ref{#prop-sigma11-singleton}, so the whole formula is $\Pi^1_1$.
:::
::::

::::exercise{difficulty=2}
Show that the class of sets that are not hyperarithmetic contains a perfect closed class, and deduce that there are continuum many sets $X$ such that $X$ is not hyperarithmetic.

:::solution
By :ref{#prop-sigma11-singleton}, the class $\cs \setminus \mathrm{HYP}$ is $\Sigma^1_1$, and it is non-empty, since $\mathrm{HYP}$ is countable. By :ref{#thm-effective-perfect-set}, it contains a non-empty perfect closed class, which is in bijection with $\cs$ by the proof of the theorem.
:::
::::

## Notes and references

The perfect set theorem for analytic sets is due to Suslin (1917). Its effective form, with the characterization of the countable $\Sigma^1_1$ classes, is due to Harrison (1967), in his thesis on recursive pseudo-well-orderings; Moschovakis proves it for $\Sigma^1_1$ subsets of arbitrary recursively presented Polish spaces (Theorem 4F.1). The splitting construction can be seen as forcing with non-empty $\Sigma^1_1$ classes, a method developed by Gandy and Harrington; Monin and Patey use the same conditions, together with the Gandy basis theorem, to build sets computable in $\mathcal O$ that are incomparable for hyperarithmetic reducibility. In second-order arithmetic, the perfect set theorem for analytic sets is equivalent to $\mathsf{ATR}_0$ over $\mathsf{ACA}_0$ (Simpson, Theorems V.4.3 and V.5.5), and its proof there uses pseudo-hierarchies, as in the previous course.

- J. Harrison, *Some applications of recursive pseudo-well-orderings*, PhD thesis, Stanford University, 1967.
- J. Harrison, *Recursive pseudo-well-orderings*, Transactions of the American Mathematical Society 131 (1968), 526–543.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Section 4F.
- B. Monin and L. Patey, *Computability theory*, chapter *Σ¹₁ and Π¹₁ classes*, sections *The continuum hypothesis for Σ¹₁ classes* and *Π¹₁ singletons*.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.4–V.5.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Section 29.
