---
title: Σ¹₁ classes and their members
summary: Σ¹₁ classes as projections of closed sets of Baire space; a computable tree with paths but no hyperarithmetic path; the Kleene basis theorem; the Gandy basis theorem (admitted).
duration: 25
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
2. The class of sets that are not hyperarithmetic. By the second exercise of :ref{to="kleene-theorem"}, "$X$ is hyperarithmetic" is $\Pi^1_1$ in $X$, so its negation is $\Sigma^1_1$. This class is non-empty, since $\mathrm{HYP}$ is countable, and it has no hyperarithmetic member: the hyperarithmetic sets are not a **basis** for the $\Sigma^1_1$ classes, in the sense that some non-empty $\Sigma^1_1$ class has no hyperarithmetic member. The next theorem shows that the same holds for the much simpler classes of paths of computable trees.
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

## Exercises

::::exercise{difficulty=1}
Show that every non-empty $\Pi^0_1$ class of subsets of $\nat$ has a hyperarithmetic member, and explain why this does not contradict :ref{#thm-no-hyp-path}.

:::solution
The leftmost path of a computable binary tree with a path is computable in $\emptyset'$ (:ref{#prop-leftmost-path}), hence hyperarithmetic. :ref{#thm-no-hyp-path} concerns trees on $\nat$, whose paths form closed subsets of Baire space, which are not compact; their extendible nodes are not $\Pi^0_1$ in general.
:::
::::

## Notes and references

Kleene (1955) proved the existence of computable trees with paths but no hyperarithmetic paths, and the basis theorem for $\mathcal O$. Gandy (1960) proved the basis theorem that bears his name.

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- R. O. Gandy, *On a problem of Kleene's*, Bulletin of the American Mathematical Society 66 (1960), 501–502.
- B. Monin and L. Patey, *Computability theory*, chapter "$\Sigma^1_1$ and $\Pi^1_1$ classes".
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
