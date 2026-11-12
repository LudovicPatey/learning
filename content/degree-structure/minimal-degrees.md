---
title: Minimal degrees
summary: Splitting trees give a set of minimal Turing degree computable in 0″ (Spector); the construction is a forcing with computable perfect trees, whose conditions decide for all their paths whether a functional loses information.
duration: 50
prerequisites: [embeddings, immunity-growth/computably-dominated, ce-degrees/sacks-splitting]
---

By the embedding theorem, the degrees contain every countable partial order, and the interval below a 1-generic degree is already rich. One may ask whether below every non-zero degree there is a degree strictly between it and $\obf$. Spector showed that this fails: there are **minimal** degrees, immediately above $\obf$. This lesson proves his theorem. The next one relativizes the construction, and describes which degrees are not minimal.

The finite extension method cannot produce a minimal degree. A string decides only finitely many bits, and a sufficiently generic set has independent columns, each strictly below the whole set (:ref{#ex-generic-not-minimal}). The proof uses a different kind of condition: a computable **perfect tree**, which keeps a perfect class of candidates and decides a property for all of them at once. The method is called **Sacks forcing**, or **forcing with perfect trees**. It was used in the course on immunity to build a computably dominated set (:ref{#thm-martin-miller-ftrees}); here the property to decide is whether a functional $\Phi_e$ loses information on the paths of the tree, or preserves all of it.

We use the function trees of :ref{#def-function-tree}: total functions $T : \bstr \to \bstr$ with $\rho \preceq \mu \iff T(\rho) \preceq T(\mu)$, with paths $[T]$, subtrees, and full subtrees above a node. If $X \in [T]$, then for every $n$ some $\rho$ of length $n$ has $T(\rho) \prec X$.

:::definition{#def-minimal-degree}
A degree $\dbf$ is **minimal** if $\dbf > \obf$ and there is no degree $\cbf$ with $\obf < \cbf < \dbf$. Equivalently, a set $X$ has minimal degree if it is not computable and every set computable from $X$ is computable or computes $X$.
:::

The degrees met so far are not minimal. The degree $\obf'$, and more generally every non-zero c.e. degree, bounds a strictly smaller non-zero c.e. degree, by the Sacks splitting theorem (:ref{#cor-no-minimal-ce}). A 1-generic degree bounds the degrees of its columns (:ref{#ex-generic-not-minimal}). For a set $X$ of minimal degree, every reduction $\Phi^X_e$ that is total must either lose all the information of $X$, and be computable, or lose none of it, and compute $X$ back. The construction meets these requirements one at a time, each for all the paths of a tree.

## Splitting trees

:::definition{#def-e-splitting}
Two strings $\sigma, \tau$ form an **$e$-split** if $\Phi^\sigma_e(x)\converge \neq \Phi^\tau_e(x)\converge$ for some $x$. An f-tree $T$ is **$e$-splitting** if $T(\rho 0)$ and $T(\rho 1)$ form an $e$-split for every $\rho$. It **avoids $e$-splits** if no two of its nodes form an $e$-split.
:::

Two strings that form an $e$-split are incomparable, since a computation with an oracle string is preserved by extending the string. For instance, if $\Phi_e$ is the identity functional, $\Phi^\sigma_e(x) = \sigma(x)$ for $x < |\sigma|$, any two incomparable strings form an $e$-split, and every f-tree is $e$-splitting. If $\Phi^X_e$ ignores its oracle, no two strings form an $e$-split, and every f-tree avoids $e$-splits. A general functional behaves differently on different parts of the tree, and the next lemma finds a subtree on which it behaves uniformly.

:::lemma{#lem-splitting-dichotomy}
Let $T$ be a computable f-tree and $e \in \nat$. There is a computable subtree $S$ of $T$ that is $e$-splitting or avoids $e$-splits.
:::

:::proof{of=lem-splitting-dichotomy}
*Case 1: some node $T(\nu)$ has no two extensions $T(\rho), T(\rho')$, with $\rho, \rho' \succeq \nu$, that form an $e$-split.* Let $S$ be the full subtree above $T(\nu)$. It avoids $e$-splits.

*Case 2: for every $\nu$, there are $\rho, \rho' \succeq \nu$ such that $T(\rho)$ and $T(\rho')$ form an $e$-split.* Define $S(\mu) = T(\nu_\mu)$ by induction. Let $\nu_\varepsilon = \varepsilon$. Given $\nu_\mu$, search for the first pair $\rho, \rho' \succeq \nu_\mu$ such that $T(\rho)$ and $T(\rho')$ form an $e$-split, and let $\nu_{\mu 0} = \rho$ and $\nu_{\mu 1} = \rho'$. The search terminates by the hypothesis of Case 2, so $S$ is computable. The nodes $T(\rho)$ and $T(\rho')$ are incomparable, so $\rho$ and $\rho'$ are incomparable, and both strictly extend $\nu_\mu$. Hence $\mu \mapsto \nu_\mu$ preserves the prefix relation and incomparability, $S$ is an f-tree, a subtree of $T$, and it is $e$-splitting by construction.
:::

:::lemma{#lem-splitting-consequences}
Let $T$ be a computable f-tree, $e \in \nat$, and $X \in [T]$ such that $\Phi^X_e$ is total.

1. If $T$ avoids $e$-splits, then $\Phi^X_e$ is computable.
2. If $T$ is $e$-splitting, then $X \leq_T \Phi^X_e$.
:::

:::proof{of=lem-splitting-consequences}
1. To compute $\Phi^X_e(x)$, search for a node $\sigma$ of $T$ with $\Phi^\sigma_e(x)\converge$ and output its value. A long enough prefix of $X$ that is a node of $T$ has a convergent computation, so the search terminates. Two nodes of $T$ do not form an $e$-split, so the value found is the value given by the prefixes of $X$, which is $\Phi^X_e(x)$.
2. Let $Y = \Phi^X_e$. We compute, with oracle $Y$, strings $\mu_0 \prec \mu_1 \prec \cdots$ with $|\mu_n| = n$ and $T(\mu_n) \prec X$. Let $\mu_0 = \varepsilon$. Given $\mu_n$, the nodes $T(\mu_n 0)$ and $T(\mu_n 1)$ form an $e$-split; find, by a search, an $x$ with $\Phi^{T(\mu_n 0)}_e(x)\converge \neq \Phi^{T(\mu_n 1)}_e(x)\converge$. One of the two nodes is a prefix of $X$: since $X$ is a path, some node $T(\rho) \prec X$ is longer than $T(\mu_n)$; then $T(\mu_n) \prec T(\rho)$, so $\mu_n \prec \rho$, and $\rho \succeq \mu_n i$ for some $i$, which gives $T(\mu_n i) \preceq T(\rho) \prec X$. The computation of this node gives $Y(x)$, by the use principle; so exactly one of the two values equals $Y(x)$, and we let $\mu_{n+1} = \mu_n i$ for the corresponding $i$. Then $T(\mu_{n+1}) \prec X$. The nodes $T(\mu_n)$ have increasing lengths, so $X$ is computed from $Y$.
:::

On an $e$-splitting tree, the functional $\Phi_e$ distinguishes the two branches at every node, so its output tells which branch a path follows. On a tree avoiding $e$-splits, all paths give compatible outputs, which can be found by searching the tree. The search is effective because the tree is computable: this is why the conditions are computable trees, and not arbitrary perfect trees.

:::figure[Left: an $e$-splitting tree. At each node, the two successors give different values of $\Phi_e$ at some input $x$, written next to the edges; knowing $Y = \Phi^X_e$, one follows the edge whose value agrees with $Y$, and recovers the path $X$. Right: a tree avoiding $e$-splits. The outputs of $\Phi_e$ at the nodes, written as strings, are pairwise compatible, so they are all prefixes of a single sequence, which a search through the computable tree computes.]
<svg class="fig" viewBox="0 0 600 272" width="600" role="img" aria-label="Left: an e-splitting tree; at each node, the two successors give different values of Phi_e at some input, and the values of Y select the branch followed by X. Right: a tree avoiding e-splits; all its nodes give compatible outputs"><line x1="150.0" y1="40" x2="80.0" y2="98" class="accent-stroke" stroke-width="2.2"/><line x1="150.0" y1="40" x2="220.0" y2="98" class="muted-stroke" stroke-width="1.1"/><line x1="80.0" y1="98" x2="45.0" y2="156" class="muted-stroke" stroke-width="1.1"/><line x1="80.0" y1="98" x2="115.0" y2="156" class="accent-stroke" stroke-width="2.2"/><line x1="220.0" y1="98" x2="185.0" y2="156" class="muted-stroke" stroke-width="1.1"/><line x1="220.0" y1="98" x2="255.0" y2="156" class="muted-stroke" stroke-width="1.1"/><line x1="115.0" y1="156" x2="97.5" y2="214" class="muted-stroke" stroke-width="1.1"/><line x1="115.0" y1="156" x2="132.5" y2="214" class="accent-stroke" stroke-width="2.2"/><circle cx="150.0" cy="40" r="4.5" class="node"/><circle cx="80.0" cy="98" r="4.5" class="node"/><circle cx="220.0" cy="98" r="4.5" class="node"/><circle cx="45.0" cy="156" r="4.5" class="node"/><circle cx="115.0" cy="156" r="4.5" class="node"/><circle cx="185.0" cy="156" r="4.5" class="node"/><circle cx="255.0" cy="156" r="4.5" class="node"/><circle cx="97.5" cy="214" r="4.5" class="node"/><circle cx="132.5" cy="214" r="4.5" class="node"/><text x="107.0" y="71.0" text-anchor="end" class="mrm" font-size="11">0</text><text x="193.0" y="71.0" text-anchor="start" class="mrm" font-size="11">1</text><text x="150.0" y="30" text-anchor="middle" class="math" font-size="12">x<tspan class="mrm" font-size="8" dy="4">0</tspan></text><text x="54.5" y="129.0" text-anchor="end" class="mrm" font-size="11">1</text><text x="105.5" y="129.0" text-anchor="start" class="mrm" font-size="11">0</text><text x="80.0" y="88" text-anchor="middle" class="math" font-size="12">x<tspan class="mrm" font-size="8" dy="4">1</tspan></text><text x="98.2" y="187.0" text-anchor="end" class="mrm" font-size="11">0</text><text x="131.8" y="187.0" text-anchor="start" class="mrm" font-size="11">1</text><text x="115.0" y="146" text-anchor="middle" class="math" font-size="12">x<tspan class="mrm" font-size="8" dy="4">2</tspan></text><text x="132.5" y="236" text-anchor="middle" class="math" font-size="13">X</text><text x="150.0" y="16" text-anchor="middle" class="label">e-splitting, with Y = 0, 0, 1 at the three inputs</text><text x="150.0" y="262" text-anchor="middle" class="label">the values of Y choose the branch followed by X</text><line x1="450.0" y1="40" x2="380.0" y2="98" class="ink-stroke" stroke-width="1.1"/><line x1="450.0" y1="40" x2="520.0" y2="98" class="ink-stroke" stroke-width="1.1"/><line x1="380.0" y1="98" x2="345.0" y2="156" class="ink-stroke" stroke-width="1.1"/><line x1="380.0" y1="98" x2="415.0" y2="156" class="ink-stroke" stroke-width="1.1"/><line x1="520.0" y1="98" x2="485.0" y2="156" class="ink-stroke" stroke-width="1.1"/><line x1="520.0" y1="98" x2="555.0" y2="156" class="ink-stroke" stroke-width="1.1"/><line x1="345.0" y1="156" x2="327.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="345.0" y1="156" x2="362.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="415.0" y1="156" x2="397.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="415.0" y1="156" x2="432.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="485.0" y1="156" x2="467.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="485.0" y1="156" x2="502.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="555.0" y1="156" x2="537.5" y2="214" class="ink-stroke" stroke-width="1.1"/><line x1="555.0" y1="156" x2="572.5" y2="214" class="ink-stroke" stroke-width="1.1"/><circle cx="450.0" cy="40" r="4.5" class="node"/><text x="458.0" y="44" class="mrm" font-size="11">0</text><circle cx="380.0" cy="98" r="4.5" class="node"/><text x="388.0" y="102" class="mrm" font-size="11">01</text><circle cx="520.0" cy="98" r="4.5" class="node"/><text x="528.0" y="102" class="mrm" font-size="11">0</text><circle cx="345.0" cy="156" r="4.5" class="node"/><text x="353.0" y="160" class="mrm" font-size="11">011</text><circle cx="415.0" cy="156" r="4.5" class="node"/><text x="423.0" y="160" class="mrm" font-size="11">01</text><circle cx="485.0" cy="156" r="4.5" class="node"/><text x="493.0" y="160" class="mrm" font-size="11">01</text><circle cx="555.0" cy="156" r="4.5" class="node"/><text x="563.0" y="160" class="mrm" font-size="11">011</text><circle cx="327.5" cy="214" r="4.5" class="node"/><text x="327.5" y="232" text-anchor="middle" class="mrm" font-size="10">0110</text><circle cx="362.5" cy="214" r="4.5" class="node"/><text x="362.5" y="232" text-anchor="middle" class="mrm" font-size="10">011</text><circle cx="397.5" cy="214" r="4.5" class="node"/><text x="397.5" y="232" text-anchor="middle" class="mrm" font-size="10">011</text><circle cx="432.5" cy="214" r="4.5" class="node"/><text x="432.5" y="232" text-anchor="middle" class="mrm" font-size="10">0110</text><circle cx="467.5" cy="214" r="4.5" class="node"/><text x="467.5" y="232" text-anchor="middle" class="mrm" font-size="10">011</text><circle cx="502.5" cy="214" r="4.5" class="node"/><text x="502.5" y="232" text-anchor="middle" class="mrm" font-size="10">01</text><circle cx="537.5" cy="214" r="4.5" class="node"/><text x="537.5" y="232" text-anchor="middle" class="mrm" font-size="10">0110</text><circle cx="572.5" cy="214" r="4.5" class="node"/><text x="572.5" y="232" text-anchor="middle" class="mrm" font-size="10">011</text><text x="450.0" y="16" text-anchor="middle" class="label">avoiding e-splits: all outputs are compatible</text><text x="450.0" y="262" text-anchor="middle" class="label">they are prefixes of one computable sequence</text></svg>
:::

:::quiz[splitting trees]
In :ref{#lem-splitting-consequences} (2), why does the procedure choose the branch whose computation agrees with $Y(x)$?

- [x] Because one of the two nodes is a prefix of $X$ and its computation gives $\Phi^X_e(x) = Y(x)$, while the other node gives a different value; the node agreeing with $Y$ is the prefix of $X$.
- [ ] Because $X$ always follows the left branch.

  $X$ may follow either branch; the computation of $\Phi_e$ tells which one.
- [ ] Because the tree avoids $e$-splits.

  On a tree avoiding $e$-splits, both branches would agree, and the procedure could not choose.

---

In Case 1 of :ref{#lem-splitting-dichotomy}, why does the full subtree above $T(\nu)$ avoid $e$-splits?

- [x] Because its nodes are the nodes $T(\rho)$ with $\rho \succeq \nu$, and by the case hypothesis no two of them form an $e$-split.
- [ ] Because $\Phi_e$ is partial on its paths.

  $\Phi_e$ may be total on its paths; the subtree avoids splits, so the values are computable.
- [ ] Because it has a single path.

  A full subtree is perfect: it has continuum many paths.
:::

## Spector's theorem

:::theorem[Spector]{#thm-minimal-degree}
There is a set of minimal degree, computable in $\emptyset''$.
:::

:::proof{of=thm-minimal-degree}
Build computable f-trees $T_0, T_1, \dots$, each a subtree of the previous one, as follows. Let $T_0$ be the identity. Given $T_{2e}$, let $T_{2e+1}$ be given by :ref{#lem-ftree-noncomputable} for $T_{2e}$ and $e$. Given $T_{2e+1}$, let $S$ be given by :ref{#lem-splitting-dichotomy} for $T_{2e+1}$ and $e$, and let $T_{2e+2}$ be the full subtree of $S$ above $S(0)$. Each step passes to a subtree whose root strictly extends the previous root: this holds at the odd steps, where full subtrees above $T(0)$ or $T(1)$ are taken, and at the even steps by the passage to $S(0)$. A full subtree of an $e$-splitting tree is $e$-splitting, and a subtree of a tree avoiding $e$-splits avoids them.

Let $X$ be the union of the roots $T_k(\varepsilon)$. As in the proof of :ref{#thm-martin-miller-ftrees}, $X \in [T_k]$ for every $k$.

*$X$ is not computable*, since $X \in [T_{2e+1}]$ gives $X \neq \Phi_e$ for every $e$.

*$X$ has minimal degree.* Let $Y \leq_T X$, say $Y = \Phi^X_e$. Since $X \in [T_{2e+2}]$, by :ref{#lem-splitting-consequences}, $Y$ is computable if $T_{2e+2}$ avoids $e$-splits, and $X \leq_T Y$ if it is $e$-splitting.

*$X \leq_T \emptyset''$.* Indices of the trees can be computed with $\emptyset''$. At the odd steps, one must decide whether $\Phi_e(i)\converge = T(0)(i)$, a $\Sigma^0_1$ question. At the even steps, one must decide which case of :ref{#lem-splitting-dichotomy} holds and find $\nu$ in Case 1. The relation "$T(\rho)$ and $T(\rho')$ form an $e$-split" is $\Sigma^0_1$, uniformly in an index of the computable tree $T$, so "no two extensions above $T(\nu)$ form an $e$-split" is $\Pi^0_1$, and the existence of such a $\nu$ is $\Sigma^0_2$; $\emptyset''$ decides it and finds the least $\nu$. The roots, hence $X$, are computable from the sequence of indices.
:::

The two lemmas on f-trees, for non-computability and for splitting, play the role of the dense sets of the finite extension method. The essential difference is that a tree decides, for all its paths at once, whether $\Phi_e$ loses information or not. With strings as conditions, genericity has the opposite effect: by :ref{#thm-generic-independent} and :ref{#ex-generic-not-minimal}, a 1-generic set never has minimal degree.

In the language of forcing, the **conditions** are the computable f-trees, a condition $S$ **extends** $T$ if $S$ is a subtree of $T$, and a set $X$ satisfies a condition if $X \in [T]$. For each $e$, the conditions that are $e$-splitting or avoid $e$-splits form a **dense** family, by :ref{#lem-splitting-dichotomy}: every condition has an extension in it. So do the conditions all of whose paths differ from $\Phi_e$, by :ref{#lem-ftree-noncomputable}. The proof above builds a decreasing sequence of conditions that meets every one of these dense families, and a path of all these conditions has minimal degree. The same scheme, with other dense families, gives the computably dominated sets of :ref{#thm-martin-miller-ftrees}, and both can be met at once (see the exercises).

:::quiz[Spector's theorem]
In the proof of :ref{#thm-minimal-degree}, why is $\emptyset''$ needed rather than $\emptyset'$?

- [x] Because deciding whether a node of the tree has no pair of extensions forming an $e$-split is a $\Pi^0_1$ property, and the existence of such a node is $\Sigma^0_2$.
- [ ] Because the trees $T_k$ are not computable.

  Each tree is computable; what requires $\emptyset''$ is the choice between the cases.
- [ ] Because $X$ must be non-computable.

  Non-computability is obtained at the odd steps with $\emptyset'$.

---

Unlike the construction of a computably dominated set in :ref{#thm-martin-miller-ftrees}, the proof of :ref{#thm-minimal-degree} never forces $\Phi^X_e$ to be partial. Why is this not needed?

- [x] Because it does not need to: the dichotomy applies whatever $\Phi_e$ does, and the conclusions of :ref{#lem-splitting-consequences} concern only the paths on which $\Phi_e$ is total.
- [ ] Because $\Phi^X_e$ is always total.

  It may be partial, in which case it defines no set and nothing is required.
- [ ] Because partiality cannot be forced with trees.

  It can, as in :ref{#lem-ftree-domination}, but it is not needed here.
::

## Below the halting problem

Spector's construction needs $\emptyset''$ to decide which case of :ref{#lem-splitting-dichotomy} holds. Sacks (1961) improved the bound: there is a minimal degree below $\obf'$. The construction uses partial computable trees: the splitting procedure of Case 2 is run without knowing whether it will stall, and a node on which it stalls avoids $e$-splits. With the oracle $\emptyset'$, the construction guesses the case and corrects its guesses finitely often, in the manner of a finite injury argument (Soare, Chapter 13). We admit this result. By contrast, no c.e. degree is minimal (:ref{#cor-no-minimal-ce}), although Yates (1970) and Cooper (1972) showed that every non-zero c.e. degree bounds a minimal degree. Every minimal degree below $\obf'$ is hyperimmune, since no non-computable $\Delta^0_2$ set is computably dominated (:ref{#thm-computation-function}); so minimality does not imply computable domination, although the first exercise below combines the two.

## Exercises

::::exercise{difficulty=1}
Show that there is a set of minimal degree that is computably dominated, computable in $\emptyset''$.

:::solution
Interleave the steps of :ref{#thm-minimal-degree} with those of :ref{#thm-martin-miller-ftrees}: at step $3e + 1$, apply :ref{#lem-ftree-noncomputable}; at step $3e + 2$, apply :ref{#lem-splitting-dichotomy} for $e$; at step $3e + 3$, apply :ref{#lem-ftree-domination} for $e$; after the last two, pass to the full subtree above the node of the new tree indexed by $0$, so that the roots increase. Each step yields a computable subtree of the previous tree, so the union $X$ of the roots lies on all the trees. The verification of each property only uses the tree of the corresponding step, so $X$ is non-computable, of minimal degree, and computably dominated. Each step is decided by $\emptyset''$, as in the two proofs.
:::
::::

::::exercise{difficulty=2}
Let $T$ be a computable f-tree that avoids $e$-splits, and let $\Phi^X_e$ be total for some $X \in [T]$. Show that the computable set $\Phi^X_e$ does not depend on $X$ among the paths $X$ of $T$ on which $\Phi_e$ is total.

:::solution
Let $X, X' \in [T]$ with $\Phi^X_e$ and $\Phi^{X'}_e$ total, and $x \in \nat$. Long enough prefixes of $X$ and $X'$ that are nodes of $T$ give convergent computations at $x$, with the values $\Phi^X_e(x)$ and $\Phi^{X'}_e(x)$ by the use principle. Two nodes of $T$ do not form an $e$-split, so these values are equal.
:::
::::

## Notes and references

Spector's construction is forcing with perfect trees. The course on effective forcing studies its generic sets: they are computably dominated, of minimal degree (:ref{#prop-sacks-generic}), and not generalized low (:ref{#thm-sacks-not-gl1}).

Spector (1956) proved the existence of minimal degrees, with a forcing over a restricted class of computable trees, in which all the nodes of a level are extended by the same strings; Shoenfield (1966) observed that arbitrary computable f-trees suffice for minimality, which gives the presentation used here (Downey and Hirschfeldt, Section 2.18, attribute the influential use of trees to Shoenfield's book of 1971). Soare's *Turing Computability* (2016) gives the construction in Chapter 12: e-splitting f-trees in Section 12.1, the two consequences of :ref{#lem-splitting-consequences} as the e-black and e-white Lemmas 12.2.2 and 12.2.3, the splitting procedure in Section 12.3, and the theorem as Theorem 12.5.1; Chapter 13 presents Sacks's minimal degree below $\obf'$. Downey and Hirschfeldt prove Spector's theorem as Theorem 2.18.2, after their construction of a computably dominated set, as in this course. Monin and Patey present it as a theorem on sufficiently generic sets for computable Sacks forcing, in their chapter on the structure of the degrees. Lerman's monograph develops the method for initial segments of $\mathcal D$.

- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- J. R. Shoenfield, *A theorem on minimal degrees*, Journal of Symbolic Logic 31 (1966), 539–544.
- G. E. Sacks, *A minimal degree less than 0′*, Bulletin of the American Mathematical Society 67 (1961), 416–419.
- C. E. M. Yates, *Initial segments of the degrees of unsolvability, Part II: minimal degrees*, Journal of Symbolic Logic 35 (1970), 243–266.
- S. B. Cooper, *Degrees of unsolvability complementary between recursively enumerable degrees*, Annals of Mathematical Logic 4 (1972), 31–73.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Chapters 12 and 13.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.18.
- M. Lerman, *Degrees of Unsolvability: Local and Global Theory*, Springer, 1983.
