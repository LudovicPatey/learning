---
title: Σ¹₁ classes and their members
summary: Σ¹₁ classes as projections of closed sets of Baire space; a computable tree with paths but no hyperarithmetic path; the Kleene basis theorem; the Gandy basis theorem (admitted).
duration: 30
prerequisites: [kleene-theorem, pi01-classes/computable-members, computable-ordinals/boundedness]
---

In Cantor space, every non-empty $\Pi^0_1$ class has a low member. In Baire space, the situation changes completely: a computable tree on $\nat$ may have paths, none of them hyperarithmetic. The classes of sets definable by an existential set quantifier, the $\Sigma^1_1$ classes, are the projections of the sets of paths of such trees, and their members can be very complex. This lesson proves the existence of computable trees without hyperarithmetic paths and the Kleene basis theorem, which bounds the complexity of some member of every non-empty $\Sigma^1_1$ class by $\mathcal O$.

The first result uses a **definability argument**, which reappears in the next lesson: if the hyperarithmetic sets sufficed, quantifying over them, which is a $\Pi^1_1$ operation (:ref{#cor-hyp-quantifier}), would turn a $\Sigma^1_1$ property into a $\Pi^1_1$ one, and a complete $\Pi^1_1$ set would become $\Delta^1_1$ (:ref{#prop-pi11-not-sigma11}). The second uses the method of the leftmost path, as for $\Pi^0_1$ classes.

## Σ¹₁ classes

:::definition{#def-sigma11-class}
A class $\mathcal A \subseteq \cs$ is **$\Sigma^1_1$** if there is an arithmetic formula $\varphi(X, Y)$ with $X \in \mathcal A \iff \exists Y\, \varphi(X, Y)$.
:::

By the normal form theorem (:ref{#thm-pi11-normal-form}), applied with the set variable $X$ as a parameter, every $\Sigma^1_1$ class is the projection of the set of paths of a computable tree: there is a computable tree $S$ of pairs $(\sigma, \tau) \in 2^{<\nat} \times \nat^{<\nat}$ of the same length such that $X \in \mathcal A$ if and only if $(X, f)$ is a path of $S$ for some $f \in \nat^\nat$. Every $\Pi^0_1$ class, and every hyperarithmetic singleton, is $\Sigma^1_1$.

:::example{#ex-sigma11-classes}
1. The class of sets $X$ that compute a path of a fixed computable tree $T \subseteq \nat^{<\nat}$: $X \in \mathcal A$ if and only if $\exists f\, \exists e\, (f \text{ is a path of } T \wedge \Phi^X_e = f)$, where the existential quantifier over $e$ is absorbed into the quantifier over $f$.
2. The class of sets that are not hyperarithmetic. By :ref{#ex-hyp-pi11-in-x}, "$X$ is hyperarithmetic" is $\Pi^1_1$ in $X$, so its negation is $\Sigma^1_1$. This class is non-empty, since $\mathrm{HYP}$ is countable, and it has no hyperarithmetic member: the hyperarithmetic sets are not a **basis** for the $\Sigma^1_1$ classes, in the sense that some non-empty $\Sigma^1_1$ class has no hyperarithmetic member. The next theorem shows that the same holds for the much simpler classes of paths of computable trees.
:::

## Trees without hyperarithmetic paths

:::theorem[Kleene]{#thm-no-hyp-path}
There is a computable tree $T \subseteq \nat^{<\nat}$ that has a path but no hyperarithmetic path.
:::

:::proof{of=thm-no-hyp-path}
Suppose that every computable tree with a path has a hyperarithmetic path, a function $f$ being identified with its graph, which is hyperarithmetic if and only if $f$ is. Then for every index $i$ of a computable tree $T_i$,
$$
i \notin \mathrm{WF} \iff \exists X \in \mathrm{HYP}\ (X \text{ is the graph of a path of } T_i),
$$
and the right-hand side is $\Pi^1_1$ by :ref{#cor-hyp-quantifier}, the formula in parentheses being arithmetic. Being an index of a computable tree is an arithmetic property of $i$, so the complement of $\mathrm{WF}$, which consists of the other numbers and of the indices of trees with a path, would be $\Pi^1_1$. Then $\mathrm{WF}$ would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}.
:::

Hence the hyperarithmetic sets are not a basis for the $\Sigma^1_1$ classes, nor even for the sets of paths of computable trees on $\nat$, the $\Pi^0_1$ classes of Baire space. The difference with Cantor space comes from compactness: a computable binary tree with a path has a leftmost path computable in $\emptyset'$ (:ref{#prop-leftmost-path}), because the extendible nodes form a $\Pi^0_1$ set; for a tree on $\nat$, extendibility is $\Sigma^1_1$.

::::exercise{#ex-unique-path-hyp difficulty=2 objective="Use Kleene's theorem to show that isolated paths of computable trees are hyperarithmetic, so that a tree without hyperarithmetic paths has continuum many paths."}
Let $T \subseteq \nat^{<\nat}$ be a computable tree.

1. Show that if $T$ has exactly one path, then this path is hyperarithmetic.
2. Deduce that if $T$ has a path but no hyperarithmetic path, then $T$ has $2^{\aleph_0}$ paths.

:::solution
1. Let $f$ be the unique path, identified with its graph. For all $n$ and $m$,
   $$
   f(n) = m \iff \exists g\, (g \text{ is a path of } T \wedge g(n) = m) \iff \forall g\, (g \text{ is a path of } T \rightarrow g(n) = m).
   $$
   Both equivalences use that $f$ is a path and the only one. "$g$ is a path of $T$" is arithmetic in $g$, since $T$ is computable; a quantifier over functions is a quantifier over their graphs. So the graph of $f$ is $\Sigma^1_1$ and $\Pi^1_1$, hence hyperarithmetic by :ref{#thm-kleene-delta11}, and so is $f$.
2. Let $\sigma \in T$ be a node through which some path of $T$ passes. The set $T_{(\sigma)} = \{ \tau \in T : \tau \preceq \sigma \text{ or } \sigma \preceq \tau \}$ is a computable tree, whose paths are the paths of $T$ through $\sigma$. They are not hyperarithmetic, so by (1) there are at least two of them, $g \neq g'$. Let $k$ be such that $g \uh k \neq g' \uh k$; then $\sigma_0 = g \uh \max(k, |\sigma|)$ and $\sigma_1 = g' \uh \max(k, |\sigma|)$ are incompatible nodes of $T$, both extending $\sigma$, hence properly, and both with a path through them.

   Starting from the root, which has a path through it, this gives by induction on $|s|$ nodes $\sigma_s \in T$ for $s \in 2^{<\nat}$, each with a path through it, such that $\sigma_{s0}$ and $\sigma_{s1}$ are incompatible proper extensions of $\sigma_s$. For $X \in \cs$, the nodes $\sigma_{X \uh n}$ form a chain whose lengths increase strictly; their union is a function whose initial segments are in $T$, a path $p_X$ of $T$. If $X \neq X'$, they first differ at some $n$, and $p_X$, $p_{X'}$ extend the incompatible nodes $\sigma_{(X \uh n) 0}$ and $\sigma_{(X \uh n) 1}$ in some order, so $p_X \neq p_{X'}$. Hence $T$ has at least $2^{\aleph_0}$ paths, and at most $2^{\aleph_0}$ since $\nat^\nat$ has this cardinality.

So the tree of :ref{#thm-no-hyp-path} has no isolated path: its set of paths is perfect.
:::
::::

:::theorem[Kleene basis theorem]{#thm-kleene-basis}
Every non-empty $\Sigma^1_1$ class has a member computable in $\mathcal O$.
:::

:::proof{of=thm-kleene-basis}
Let $S$ be a computable tree of pairs whose projection is the class. Let $E$ be the set of nodes $(\sigma, \tau) \in S$ above which $S$ has a path; it is $\Sigma^1_1$, so its complement is $\Pi^1_1$ and many-one reducible to $\mathcal O$, which is $\Pi^1_1$-complete (:ref{#thm-o-complete}). So $E \leq_T \mathcal O$. The root belongs to $E$. Define a path by choosing at each step the first immediate successor, in the order of codes, that belongs to $E$; one exists, since a path through the current node passes through one of its successors. The resulting path $(X, f)$ is computable in $E$, hence in $\mathcal O$, and $X$ belongs to the class.
:::

The proof is the method of the leftmost path, used for the $\emptyset'$ bound on binary trees (:ref{#prop-leftmost-path}); the only change is the cost of deciding extendibility, $\Sigma^1_1$ instead of $\Pi^0_1$.

By :ref{#thm-no-hyp-path}, $\mathcal O$ cannot be replaced by a hyperarithmetic set. Gandy (1960) refined the theorem: every non-empty $\Sigma^1_1$ class has a member $X$ with $\omega_1^X = \omega_1^{\mathrm{CK}}$. Such an $X$ does not compute $\mathcal O$, since $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ (:ref{#prop-omega1-relative}). This **Gandy basis theorem** is the analogue of the low basis theorem (:ref{to="pi01-classes/basis-theorems"}), with $\omega_1^X = \omega_1^{\mathrm{CK}}$ playing the role of lowness. Its proof is a forcing argument with $\Sigma^1_1$ classes, parallel to the proof of the low basis theorem with $\Pi^0_1$ classes; the new difficulty is that a decreasing sequence of non-empty $\Sigma^1_1$ classes may have an empty intersection, so the construction must build the witnesses $f$ together with $X$. It gives a member $X$ that is **hyperlow**, $\mathcal O^X \leq_T \mathcal O$. We admit it (Monin and Patey, chapter "$\Sigma^1_1$ and $\Pi^1_1$ classes").

:::quiz[trees without hyperarithmetic paths]
In the proof of :ref{#thm-no-hyp-path}, why would the hypothesis make $\mathrm{WF}$ a $\Sigma^1_1$ set?

- [x] Because ill-foundedness, a $\Sigma^1_1$ property, would be equivalent to the existence of a hyperarithmetic path, a $\Pi^1_1$ property; so the complement of $\mathrm{WF}$ would be $\Pi^1_1$.
- [ ] Because every hyperarithmetic set is $\Sigma^1_1$.

  The relevant fact is the complexity of quantifying over hyperarithmetic sets, not the complexity of each of them.
- [ ] Because $\mathrm{WF}$ is $\Pi^1_1$.

  This is true but gives no contradiction by itself.

---

Why is the analogous statement false for binary trees?

- [x] Because a computable binary tree with a path has a path computable in $\emptyset'$, the leftmost one, since the extendible nodes of a binary tree form a $\Pi^0_1$ set by compactness.
- [ ] Because binary trees are finite.

  Infinite binary trees exist; compactness makes them tame.
- [ ] Because binary trees have no paths.

  By weak König's lemma, infinite binary trees have paths.
:::

## Notes and references

Kleene (1955) proved the existence of computable trees with paths but no hyperarithmetic paths, and the basis theorem for $\mathcal O$. Gandy (1960) proved the basis theorem that bears his name.

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- R. O. Gandy, *On a problem of Kleene's*, Bulletin of the American Mathematical Society 66 (1960), 501–502.
- B. Monin and L. Patey, *Computability theory*, chapter "$\Sigma^1_1$ and $\Pi^1_1$ classes".
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.

:::::exercises
::::exercise{#ex-pi01-hyp-member difficulty=1 objective="Contrast Cantor space with Baire space: non-empty $\Pi^0_1$ classes of sets have hyperarithmetic members." lessons="pi01-classes/computable-members"}
Show that every non-empty $\Pi^0_1$ class of subsets of $\nat$ has a hyperarithmetic member, and explain why this does not contradict :ref{#thm-no-hyp-path}.

:::solution
The leftmost path of a computable binary tree with a path is computable in $\emptyset'$ (:ref{#prop-leftmost-path}), hence hyperarithmetic. :ref{#thm-no-hyp-path} concerns trees on $\nat$, whose paths form closed subsets of Baire space, which are not compact; their extendible nodes are not $\Pi^0_1$ in general.
:::
::::

::::exercise{#ex-sigma11-closure difficulty=1 objective="Check the closure properties of $\Sigma^1_1$ classes by merging set quantifiers."}
Let $\mathcal A$ and $\mathcal B$ be $\Sigma^1_1$ classes.

1. Show that $\mathcal A \cap \mathcal B$ and $\mathcal A \cup \mathcal B$ are $\Sigma^1_1$.
2. Let $e$ be an index of a Turing functional. Show that the class $\{ Z : \exists X \in \mathcal A\ (\Phi^X_e \text{ is total and } \Phi^X_e = Z) \}$ is $\Sigma^1_1$.
3. Let $\varphi(n, X, Y)$ be arithmetic, and $\mathcal A_n = \{ X : \exists Y\, \varphi(n, X, Y) \}$. Show that $\bigcup_n \mathcal A_n$ and $\bigcap_n \mathcal A_n$ are $\Sigma^1_1$.

:::solution
Let $X \in \mathcal A \iff \exists Y\, \varphi(X, Y)$ and $X \in \mathcal B \iff \exists Y\, \psi(X, Y)$, with $\varphi$ and $\psi$ arithmetic. Two set quantifiers $\exists Y_0\, \exists Y_1$ are merged into one, $\exists W$ with $Y_i = W^{[i]}$, and "$n \in W^{[i]}$" is the arithmetic formula $\langle i, n \rangle \in W$.

1. $X \in \mathcal A \cap \mathcal B \iff \exists W\, (\varphi(X, W^{[0]}) \wedge \psi(X, W^{[1]}))$, and $X \in \mathcal A \cup \mathcal B \iff \exists Y\, (\varphi(X, Y) \vee \psi(X, Y))$.
2. $Z$ is in the class if and only if $\exists W\, (\varphi(W^{[0]}, W^{[1]}) \wedge \forall n\, (\Phi^{W^{[0]}}_e(n)\converge = Z(n)))$, where $W^{[0]}$ plays the role of $X$ and $W^{[1]}$ of its witness; the formula after $\exists W$ is arithmetic.
3. $X \in \bigcup_n \mathcal A_n \iff \exists Y\, \exists n\, \varphi(n, X, Y)$, and $\exists n\, \varphi$ is arithmetic. For the intersection, $\forall n\, \exists Y\, \varphi(n, X, Y) \iff \exists W\, \forall n\, \varphi(n, X, W^{[n]})$: from right to left, take $Y = W^{[n]}$; from left to right, choose for each $n$ a witness $Y_n$ (countable choice) and let $W = \{ \langle n, m \rangle : m \in Y_n \}$.
:::
::::

::::exercise{#ex-extendible-not-hyp difficulty=1 objective="See where the Kleene basis theorem needs more than a hyperarithmetic oracle: the extendible nodes of a computable tree need not be hyperarithmetic."}
Let $T$ be the tree of :ref{#thm-no-hyp-path}, and $E$ the set of nodes of $T$ through which $T$ has a path. Show that $E$ is $\Sigma^1_1$ and computable in $\mathcal O$, but not hyperarithmetic.

:::solution
"$\sigma \in E$" is "$\exists f\, (f \text{ is a path of } T \text{ and } \sigma \prec f)$", a $\Sigma^1_1$ condition. Its complement is $\Pi^1_1$, hence many-one reducible to $\mathcal O$ (:ref{#thm-o-complete}), so $E \leq_T \mathcal O$. The root is in $E$, since $T$ has a path. Suppose $E$ hyperarithmetic. As in the proof of :ref{#thm-kleene-basis}, define $p$ by letting $p(k)$ be the least $m$ such that $(p \uh k) m \in E$; such an $m$ exists when $p \uh k \in E$, since a path through $p \uh k$ goes through one of its immediate successors. By induction, $p \uh k \in E \subseteq T$ for every $k$, so $p$ is a path of $T$, and $p \leq_T E$ is hyperarithmetic. This contradicts the choice of $T$.
:::
::::

::::exercise{#ex-no-hyp-path-index-set difficulty=2 objective="Use a definability argument to classify the set of computable trees that have paths but no hyperarithmetic path."}
Let $N$ be the set of indices of computable trees $T \subseteq \nat^{<\nat}$ that have a path but no hyperarithmetic path. Show that $N$ is $\Sigma^1_1$, non-empty, and not $\Pi^1_1$.

:::solution
Let $\mathrm{Tr}$ be the set of indices of computable trees, an arithmetic set. "$T_i$ has a path" is $\Sigma^1_1$, and "$T_i$ has a hyperarithmetic path" is $\Pi^1_1$ by :ref{#cor-hyp-quantifier}, so its negation is $\Sigma^1_1$; hence $N$ is $\Sigma^1_1$. It is non-empty by :ref{#thm-no-hyp-path}.

Let $P$ be the set of $i \in \mathrm{Tr}$ such that $T_i$ has a hyperarithmetic path, a $\Pi^1_1$ set. The indices of computable trees with a path form the set $N \cup P$. If $N$ were $\Pi^1_1$, then $N \cup P$, and $(\nat \setminus \mathrm{Tr}) \cup N \cup P$, the complement of $\mathrm{WF}$, would be $\Pi^1_1$, and $\mathrm{WF}$ would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}.
:::
::::
:::::
