---
title: Forcing with Π⁰₁ classes and perfect trees
summary: The complexity of the conditions and of the forcing of Σ⁰₁ and Π⁰₁ sentences for Jockusch–Soare and computable Sacks forcing; tree forcings decide Σ⁰₂ sentences for all members by a Σ⁰₂ question; their generic sets satisfy G″ ≤ G′ ⊕ ∅″.
duration: 40
prerequisites: [cohen-forcing]
---

Cohen forcing decides $\Sigma^0_1$ sentences well, and $\Sigma^0_2$ sentences badly: a string decides the convergence of a computation for all its members, but it can never make a set finite or infinite. Forcing with trees has the opposite profile. A non-empty $\Pi^0_1$ class or a computable perfect tree can be shrunk so that a computation diverges on all its members, or so that a functional is total on all of them; this is what the computably dominated basis theorem and the Miller–Martin construction do. The price is paid at level $1$: deciding which case holds needs more oracle, because the conditions themselves are complex objects.

This lesson measures both effects for **Jockusch–Soare forcing** and **computable Sacks forcing** (:ref{#ex-forcing-notions}). It shows that the generic sets of both notions have their double jump computed by their jump and $\emptyset''$. The next lesson turns to properties of Sacks generic sets that distinguish them from Cohen generic sets.

## The complexity of the conditions

A Jockusch–Soare condition is given by an index of a computable tree $T$ with $[T] \neq \emptyset$ (:ref{#prop-pi01-equivalent}), and a computable Sacks condition by an index of a total computable f-tree.

:::proposition{#prop-js-complexity}
For Jockusch–Soare forcing, with conditions given by indices:

1. the set of indices of conditions is $\Pi^0_1$;
2. the relation $\mathcal P \subseteq \mathcal Q$ is $\Pi^0_2$;
3. "$\mathcal P \Vdash \Phi^G_e(\vec m)\converge$" is $\Sigma^0_1$, and "$\mathcal P \Vdash \Phi^G_e(\vec m)\diverge$" is $\Pi^0_2$;
4. the set of indices of conditions forcing the $\Pi^0_1$ sentence "$G$ has no element" is $\Pi^0_2$-complete, hence not $\Sigma^0_2$.
:::

:::proof{of=prop-js-complexity}
1. Emptiness of a $\Pi^0_1$ class is $\Sigma^0_1$, uniformly in an index (:ref{#prop-pi01-emptiness}).
2. Let $T_{\mathcal Q}$ be the tree of $\mathcal Q$. Then $\mathcal P \subseteq \mathcal Q$ if and only if $\mathcal P \cap [\sigma] = \emptyset$ for every $\sigma \notin T_{\mathcal Q}$: a member of $\mathcal P$ outside $\mathcal Q$ has a prefix outside $T_{\mathcal Q}$. Each condition $\mathcal P \cap [\sigma] = \emptyset$ is $\Sigma^0_1$, so the whole is $\Pi^0_2$.
3. $\mathcal P$ forces the convergence if and only if the $\Pi^0_1$ class $\mathcal P \cap \{ X : \Phi^X_e(\vec m)\diverge \}$ is empty, a $\Sigma^0_1$ property. It forces the divergence if and only if $\mathcal P \subseteq \{ X : \Phi^X_e(\vec m)\diverge \}$, a $\Pi^0_2$ property by item 2, since the second class is $\Pi^0_1$ with an index computable from $e$ and $\vec m$.
4. The sentence holds only for $\emptyset$, so a condition forces it if and only if it equals $\{ \emptyset \}$; by item 3 this is $\Pi^0_2$. Let $S = \{ a : \forall x\ \exists y\ R(a, x, y) \}$ be any $\Pi^0_2$ set, with $R$ computable. Let $T_a$ be the computable tree of the strings $0^k$ and of the strings $0^x 1^j$, $j \geq 1$, such that $R(a, x, y)$ fails for all $y < j$. Its paths are $0 0 \cdots$ and the sets $0^x 1 1 \cdots$ for the $x$ such that $R(a, x, y)$ fails for every $y$. So $[T_a] = \{ \emptyset \}$ if and only if $a \in S$, and $a \mapsto T_a$ is a many-one reduction of $S$ to the set of item 4.
:::

:::proposition{#prop-sacks-complexity}
For computable Sacks forcing, with conditions given by indices:

1. the set of indices of conditions is $\Pi^0_2$;
2. the relation $S \leq T$, between indices of conditions, is $\Pi^0_1$;
3. "$T \Vdash \Phi^G_e(\vec m)\converge$" is $\Sigma^0_1$, and "$T \Vdash \Phi^G_e(\vec m)\diverge$" is $\Pi^0_1$, for indices of conditions.
:::

:::proof{of=prop-sacks-complexity}
1. An index defines a condition if the function is total, a $\Pi^0_2$ property, and preserves comparability and incomparability, a $\Pi^0_1$ property once totality is known.
2. Along a string $\mu$ the nodes $T(\mu \uh k)$ strictly increase, so $|T(\mu)| \geq |\mu|$. Hence $S \leq T$ if and only if for every $\rho$ there is $\mu$ with $|\mu| \leq |S(\rho)|$ and $S(\rho) = T(\mu)$, a $\Pi^0_1$ condition with a bounded inner search.
3. We show that $T$ forces the convergence if and only if there is $k$ such that $\Phi^{T(\rho)}_e(\vec m)[k]\converge$ for every $\rho$ of length $k$. If such a $k$ exists, every path extends some $T(\rho)$ with $|\rho| = k$, and the computation converges on it. Conversely, let $B$ be the set of strings $\rho$ with $\Phi^{T(\rho)}_e(\vec m)[|\rho|]\diverge$; it is closed under prefixes by monotonicity. If it were infinite, it would have a path $Z$ by weak König's lemma, and $X = \bigcup_k T(Z \uh k)$ would be a path of $T$; the computation $\Phi^X_e(\vec m)$ would converge with some use $u$ at some stage $s$, and then $\Phi^{T(Z \uh k)}_e(\vec m)[k]\converge$ for $k \geq \max(u, s)$, since $|T(Z \uh k)| \geq k$. So $B$ is finite, and $k$ exists. For the divergence, $T$ forces $\Phi^G_e(\vec m)\diverge$ if and only if $\Phi^{T(\rho)}_e(\vec m)[s]\diverge$ for every $\rho$ and $s$: a node with a convergent computation is a prefix of a path, and a path with a convergent computation has a node as long as the use as a prefix.
:::

The two notions are complex in different places. For Jockusch–Soare forcing the conditions are simple, but forcing divergence is as hard as comparing two classes. For Sacks forcing, forcing at level $1$ is as simple as for Cohen forcing, but being a condition is $\Pi^0_2$. In both cases the extension relation is not computable, and the universal clause of :ref{#def-forcing-relation}, which quantifies over extensions, makes the complexity of forcing grow faster than the level of the sentence. The next sections show how to avoid the forcing relation at level $2$.

## Deciding Σ⁰₂ sentences on all members

A $\Sigma^0_2$ sentence has the form $\exists y\ \Phi^G_e(\vec m, y)\diverge$; we absorb the parameters $\vec m$ into the index and write $\exists y\ \Phi^G_e(y)\diverge$.

:::proposition{#prop-tree-sigma2}
Let $\mathbb P$ be Jockusch–Soare or computable Sacks forcing, $c$ a condition, and $\varphi = \exists y\ \Phi^G_e(y)\diverge$. Say that $c$ **answers yes** for $\varphi$ if:

- for Jockusch–Soare forcing, $c \cap \{ X : \Phi^X_e(y)\diverge \} \neq \emptyset$ for some $y$;
- for Sacks forcing, the full subtree of $c$ above some node $c(\rho)$ forces $\Phi^G_e(y)\diverge$, for some $y$.

Then:

1. if $c$ answers yes, some $d \leq c$ forces $\varphi$, and every member of $d$ satisfies $\varphi$;
2. otherwise, some $d \leq c$ forces $\neg \varphi$, and every member of $d$ satisfies $\neg \varphi$; for Jockusch–Soare forcing $d = c$, and for Sacks forcing an index of $d$ is computed from indices of $c$ and $\Phi_e$;
3. "$c$ answers yes for $\varphi$" is a $\Sigma^0_2$ relation of an index of $c$ and the code of $\varphi$.
:::

:::proof{of=prop-tree-sigma2}
1. For Jockusch–Soare forcing, $d = c \cap \{ X : \Phi^X_e(y)\diverge \}$; for Sacks forcing, $d$ is the full subtree given by the definition. In both cases $d \Vdash \Phi^G_e(y)\diverge$, so $d \Vdash \varphi$, and every member satisfies $\Phi^G_e(y)\diverge$.
2. For Jockusch–Soare forcing, if $c$ does not answer yes, then $\Phi^X_e(y)\converge$ for every $X \in c$ and every $y$. For Sacks forcing, if $c$ does not answer yes, then for every node $c(\rho)$ and every $y$ some node above $c(\rho)$ makes $\Phi_e(y)$ converge, by :ref{#prop-sacks-complexity}. This is Case 2 of :ref{#lem-ftree-domination}, whose construction computes, uniformly, a subtree $d$ on all paths of which $\Phi_e$ is total. In both cases every member of $d$ satisfies $\neg \varphi = \forall y\ \Phi^G_e(y)\converge$. Moreover $d \Vdash \neg \varphi$: an extension of $d$ forcing $\Phi^G_e(y)\diverge$ would have a member, which is a member of $d$ on which $\Phi_e(y)$ converges.
3. For Jockusch–Soare forcing, non-emptiness of a $\Pi^0_1$ class is $\Pi^0_1$, so the relation is $\exists y\ \Pi^0_1$. For Sacks forcing, forcing divergence is $\Pi^0_1$ by :ref{#prop-sacks-complexity}, so the relation is $\exists y\ \exists \rho\ \Pi^0_1$.
:::

The proposition says that a tree forcing **decides $\Sigma^0_2$ sentences for all members**, and that the decision is made by a $\Sigma^0_2$ question. For Cohen forcing the first half fails: no string has only finite sets, or only infinite sets, as members. This is the main use of tree forcings: controlling the double jump. By :ref{#thm-post} relativized, "$m \in G''$" is a $\Sigma^0_2$ sentence.

:::theorem{#thm-tree-gl2}
Let $G$ be sufficiently generic for Jockusch–Soare forcing or for computable Sacks forcing. Then $G'' \leq_T G' \oplus \emptyset''$.
:::

:::proof{of=thm-tree-gl2}
For each $m$, let $\varphi_m$ be a $\Sigma^0_2$ sentence of the form $\exists y\ \Phi^G_{e(m)}(y)\diverge$, with $e$ computable, such that $X \models \varphi_m$ if and only if $m \in X''$ for every set $X$. For a code $c$ of a condition, let $d_m(c)$ be the extension given by :ref{#prop-tree-sigma2} for $\varphi_m$, and $i_m(c) = 1$ if $c$ answers yes for $\varphi_m$, $0$ otherwise. With the oracle $\emptyset''$, given $c$ and $m$, one decides $i_m(c)$ by item 3, and computes a code of $d_m(c)$: in the first case by searching for a witness $y$ (and $\rho$) of the $\Sigma^0_2$ relation, checking candidates with $\emptyset'$; in the second case directly. Every member $X$ of $d_m(c)$ satisfies $m \in X''$ if $i_m(c) = 1$, and $m \notin X''$ if $i_m(c) = 0$.

The set $C_m = \{ d_m(c) : c \text{ a code of a condition} \}$ is dense, since $d_m(c) \leq c$. Let $G$ be generic for a family containing every $C_m$. To compute $G''(m)$ with $G' \oplus \emptyset''$, enumerate the codes $c$ of conditions, which $\emptyset''$ recognizes by :ref{#prop-js-complexity} and :ref{#prop-sacks-complexity}; for each, compute $d_m(c)$ and $i_m(c)$ with $\emptyset''$, and ask $G'$ whether $G$ is a member of $d_m(c)$. Membership in a $\Pi^0_1$ class, or in the set of paths of a total computable f-tree, is a $\Pi^0_1(G)$ property (for f-trees: for every $k$, some node $T(\rho)$ with $|\rho| = k$ is a prefix of $G$). The search terminates, since the generic filter contains some $d_m(c)$, of which $G$ is a member; output $i_m(c)$ for the first $c$ found. The output is correct for any $c$ such that $G$ is a member of $d_m(c)$.
:::

Since $G' \oplus \emptyset'' \leq_T (G \oplus \emptyset')'$, every sufficiently generic set for these notions is **generalized low₂**: $G'' \equiv_T (G \oplus \emptyset')'$. Note where genericity enters: only to ensure that the search terminates. The decisions themselves are correct for every member of the conditions $d_m(c)$.

:::quiz[the double jump of tree generic sets]
In the proof of :ref{#thm-tree-gl2}, why is the oracle $G'$ needed, rather than $G$?

- [x] To decide whether $G$ is a member of the condition $d_m(c)$, which is a $\Pi^0_1(G)$ question.
- [ ] To decide whether $c$ answers yes for $\varphi_m$.

  That is a $\Sigma^0_2$ question about the condition, decided by $\emptyset''$.
- [ ] To enumerate the codes of conditions.

  This uses $\emptyset''$, since being a code of a condition is $\Pi^0_1$ or $\Pi^0_2$.

---

Why can the same argument not be carried out for Cohen forcing at level $2$?

- [x] Because no string decides "$G$ is finite" for all its members, so there is no dense set of strings whose members all agree on a given $\Sigma^0_2$ sentence.
- [ ] Because Cohen generic sets do not have a double jump.

  Every set has a double jump; for 2-generic sets it is even computable from $G \oplus \emptyset''$.
- [ ] Because the Cohen forcing relation is not definable.

  It is definable, by :ref{#thm-cohen-forcing-definable}.
:::

## Exercises

::::exercise{difficulty=1}
Show that for Jockusch–Soare forcing the relation "$\mathcal P \Vdash \forall y\ \Phi^G_e(y)\converge$" is $\Pi^0_2$, and that for computable Sacks forcing the relation "$T \Vdash \forall y\ \Phi^G_e(y)\converge$" is $\Pi^0_3$, on indices of conditions.

:::solution
For Jockusch–Soare forcing, by :ref{#ex-forcing-relation} the class forces totality if and only if $\mathcal P \cap \{ X : \Phi^X_e(y)\diverge \} = \emptyset$ for every $y$, which is $\forall y$ applied to a $\Sigma^0_1$ relation. For Sacks forcing, by the universal clause, $T$ forces totality if and only if for every $S$ and every $y$, if $S$ is a condition and $S \leq T$, then $S$ does not force $\Phi^G_e(y)\diverge$. Being a condition is $\Pi^0_2$, extension is $\Pi^0_1$, and forcing divergence is $\Pi^0_1$ (:ref{#prop-sacks-complexity}), so the matrix is a disjunction of a $\Sigma^0_2$, a $\Sigma^0_1$ and a $\Sigma^0_1$ relation, and the whole is $\Pi^0_3$. The complexity of the set of conditions is what raises the level.
:::
::::

::::exercise{#exr-low2-dominated difficulty=2}
Show that every non-empty $\Pi^0_1$ class $\mathcal P$ has a computably dominated member $G$ with $G'' \leq_T \emptyset''$.

:::solution
Use Jockusch–Soare forcing below $\mathcal P$. The dense sets $S_k$ of :ref{#lem-generic-set}, the sets $C_m$ of the proof of :ref{#thm-tree-gl2}, and the sets of :ref{#ex-generic-notions} ensuring computable domination are uniformly $\emptyset''$-effectively dense: for the last ones, $\emptyset''$ decides whether some $\mathcal Q \cap \{ X : \Phi^X_e(y)\diverge \}$ is non-empty, a $\Sigma^0_2$ question, and finds $y$. By :ref{#thm-effective-generic} there is a $\emptyset''$-computable sequence of conditions, starting from $\mathcal P$, meeting all of them; along it, $\emptyset''$ also computes the bits $i_m$ attached to the conditions $d_m(c)$ met. The set $G$ determined by the filter is a member of each of them, so $G''(m) = i_m$, and $G'' \leq_T \emptyset''$. It is computably dominated, and a member of $\mathcal P$.
:::
::::

## Notes and references

Forcing with $\Pi^0_1$ classes is the method of Jockusch and Soare (1972); forcing with perfect trees goes back to Spector (1956) and is the computable version of Sacks forcing (Sacks 1971). The complexity of the conditions and of the forcing relation for both notions, the decision of $\Sigma^0_2$ sentences by a $\Sigma^0_2$ question, and the generalized low₂ property of the generic sets are from the chapter *Effective forcing* of Monin and Patey, section *Computational complexity and forcing question*; the hardness result of :ref{#prop-js-complexity} is added here. Dzhafarov and Mummert (Proposition 7.5.8, Corollary 7.5.9) prove that every infinite computable tree has a low₂ path of hyperimmune-free degree, which is the first exercise.

- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- G. E. Sacks, *Forcing with perfect closed sets*, in *Axiomatic Set Theory*, Proceedings of Symposia in Pure Mathematics 13, Part I, American Mathematical Society, 1971, 331–355.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 7.5.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, sections *Forcing with trees* and *Computational complexity and forcing question*.
