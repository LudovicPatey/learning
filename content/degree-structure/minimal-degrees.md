---
title: Minimal degrees
summary: Splitting trees; Spector's theorem that there is a minimal Turing degree, computable in 0″; minimal covers; minimal degrees are neither c.e., 1-generic nor PA.
duration: 40
prerequisites: [embeddings, immunity-growth/computably-dominated]
---

By the embedding theorem, the degrees contain every countable partial order, and the interval below a 1-generic degree is already rich. One may ask whether every non-zero degree bounds another non-zero degree. Spector showed that it does not: there are **minimal** degrees, immediately above $\obf$. The proof is a construction by computable function trees, a method called **Sacks forcing** or **forcing with perfect trees**, which differs from the finite extension method: the conditions are trees rather than strings, so that a single condition can decide whether a functional computes the generic set back.

We use the function trees of :ref{#def-function-tree}: total functions $T : \bstr \to \bstr$ with $\rho \preceq \mu \iff T(\rho) \preceq T(\mu)$, with paths $[T]$, subtrees, and full subtrees above a node. If $X \in [T]$, then for every $n$ some $\rho$ of length $n$ has $T(\rho) \prec X$.

:::definition{#def-minimal-degree}
A degree $\dbf$ is **minimal** if $\dbf > \obf$ and there is no degree $\cbf$ with $\obf < \cbf < \dbf$. Equivalently, a set $X$ has minimal degree if it is not computable and every set computable from $X$ is computable or computes $X$.
:::

## Splitting trees

:::definition{#def-e-splitting}
Two strings $\sigma, \tau$ form an **$e$-split** if $\Phi^\sigma_e(x)\converge \neq \Phi^\tau_e(x)\converge$ for some $x$. An f-tree $T$ is **$e$-splitting** if $T(\rho 0)$ and $T(\rho 1)$ form an $e$-split for every $\rho$. It **avoids $e$-splits** if no two of its nodes form an $e$-split.
:::

Two strings that form an $e$-split are incomparable, since a computation with an oracle string is preserved by extending the string.

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
2. Let $Y = \Phi^X_e$. We compute, with oracle $Y$, strings $\mu_0 \prec \mu_1 \prec \cdots$ with $|\mu_n| = n$ and $T(\mu_n) \prec X$. Let $\mu_0 = \varepsilon$. Given $\mu_n$, the nodes $T(\mu_n 0)$ and $T(\mu_n 1)$ form an $e$-split; find, by a search, an $x$ with $\Phi^{T(\mu_n 0)}_e(x)\converge \neq \Phi^{T(\mu_n 1)}_e(x)\converge$. One of the two nodes is a prefix of $X$, and its computation gives $Y(x)$ by the use principle; so exactly one of the two values equals $Y(x)$, and we let $\mu_{n+1} = \mu_n i$ for the corresponding $i$. Then $T(\mu_{n+1}) \prec X$. The nodes $T(\mu_n)$ have increasing lengths, so $X$ is computed from $Y$.
:::

On an $e$-splitting tree, the functional $\Phi_e$ distinguishes the two branches at every node, so its output tells which branch a path follows. On a tree avoiding $e$-splits, all paths give compatible outputs, which can be found by searching the tree.

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

The two lemmas on f-trees, for non-computability and for splitting, play the role of the dense sets of the finite extension method. The essential difference is that a tree decides, for all its paths at once, whether $\Phi_e$ loses information or not. With strings as conditions, this is impossible: by :ref{#thm-generic-independent} and the exercise of the previous lesson, a 1-generic set never has minimal degree.

:::quiz[Spector's theorem]
In the proof of :ref{#thm-minimal-degree}, why is $\emptyset''$ needed rather than $\emptyset'$?

- [x] Because deciding whether a node of the tree has no pair of extensions forming an $e$-split is a $\Pi^0_1$ property, and the existence of such a node is $\Sigma^0_2$.
- [ ] Because the trees $T_k$ are not computable.

  Each tree is computable; what requires $\emptyset''$ is the choice between the cases.
- [ ] Because $X$ must be non-computable.

  Non-computability is obtained at the odd steps with $\emptyset'$.

---

Why does the construction not make $\Phi^X_e$ partial when neither case is convenient?

- [x] Because it does not need to: the dichotomy applies whatever $\Phi_e$ does, and the conclusions of :ref{#lem-splitting-consequences} concern only the paths on which $\Phi_e$ is total.
- [ ] Because $\Phi^X_e$ is always total.

  It may be partial, in which case it defines no set and nothing is required.
- [ ] Because partiality cannot be forced with trees.

  It can, as in :ref{#lem-ftree-domination}; it is simply not needed here.
:::

Sacks (1961) improved the bound: there is a minimal degree below $\obf'$. The construction uses partial computable trees and a full approximation argument, and is admitted here; see Lerman's monograph. By contrast, no c.e. degree is minimal (:ref{#cor-no-minimal-ce}), and Yates (1970) showed that every non-zero c.e. degree bounds a minimal degree.

## Minimal covers

Relativizing Spector's construction gives degrees immediately above any given degree.

:::theorem{#thm-minimal-cover}
For every set $A$ there is a set $B$ with $A <_T B$ such that no set $C$ satisfies $A <_T C <_T B$. The degree of $B$ is a **minimal cover** of $\deg_T(A)$.
:::

:::proof{of=thm-minimal-cover}
Relativize the construction to $A$, with $A$-computable f-trees, and start from the tree $T_0(\rho) = \rho \oplus (A \uh |\rho|)$, which interleaves the bits of $\rho$ with those of $A$; every path of every subtree computes $A$ from its odd bits. The relativized lemmas give $X \in [T_0]$ such that $X \neq \Phi^A_e$ for every $e$, and such that every $Y = \Phi^X_e$ satisfies $Y \leq_T A$ or $X \leq_T Y \oplus A$; in the splitting case, the decoding procedure needs the $A$-computable tree.

Let $B = X$. Then $A \leq_T B$, and $B \not\leq_T A$. If $A \leq_T C \leq_T B$ with $C = \Phi^B_e$, then $C \leq_T A$, or $B \leq_T C \oplus A \equiv_T C$. So there is no $C$ strictly between.
:::

:::quiz[minimal covers]
In the proof of :ref{#thm-minimal-cover}, why must every path of the initial tree compute $A$?

- [x] Because the splitting case only gives $X \leq_T Y \oplus A$; to conclude $X \leq_T Y$ for $Y \geq_T A$, one needs $A \leq_T X$, and to have a cover, $B$ must be above $A$.
- [ ] Because otherwise the trees would not be $A$-computable.

  The trees are $A$-computable by construction; the coding of $A$ ensures that $B$ lies above $A$.
- [ ] Because $A$ must be non-computable.

  $A$ is arbitrary; for computable $A$ the theorem gives a minimal degree.
:::

## Exercises

::::exercise{difficulty=1}
Show that there is no non-empty $\Pi^0_1$ class all of whose members have minimal degree.

:::solution
Let $\mathcal P = [T]$ be non-empty, with $T$ computable, and $X$ its leftmost path: for every $n$, $X \uh n$ is the lexicographically least string of length $n$ that is extendible in $T$. Let $L$ be the set of strings $\sigma$ that are lexicographically smaller than $X \uh |\sigma|$. Then $\sigma \in L$ if and only if every string $\tau$ of length $|\sigma|$ with $\tau \leq_{\mathrm{lex}} \sigma$ satisfies $[\tau] \cap \mathcal P = \emptyset$; this is a finite conjunction of $\Sigma^0_1$ conditions (:ref{#prop-pi01-emptiness}), so $L$ is c.e. The set $L$ computes $X$: $X \uh n$ is the least string of length $n$ not in $L$. Conversely $X$ computes $L$. So $X$ has c.e. degree. If $X$ is computable, it does not have minimal degree; otherwise its degree is c.e. and non-zero, hence not minimal by :ref{#cor-no-minimal-ce}.
:::
::::

::::exercise{difficulty=2}
Show that there are continuum many minimal degrees.

:::hint
Modify the construction as in the last exercise of the lesson on computably dominated sets: at each step, choose between the two subtrees above $T(0)$ and $T(1)$ according to a bit of a parameter $Z \in \cs$.
:::

:::solution
Fix the subtrees given by the lemmas, choosing the least witness in Case 1, so that each step is determined by the current tree. For $Z \in \cs$, run the construction, but at each even step $2e+2$ pass to the full subtree of $S$ above $S(Z(e))$ instead of $S(0)$. Let $X_Z$ be the union of the roots. As before, $X_Z$ has minimal degree. If $Z$ and $Z'$ first differ at $e$, the constructions coincide up to step $2e + 1$ and produce the same $S$; then $X_Z$ and $X_{Z'}$ extend the incompatible nodes $S(0)$ and $S(1)$, so $X_Z \neq X_{Z'}$. Each degree contains countably many sets, so the continuum many sets $X_Z$ have continuum many degrees.
:::
::::

## Notes and references

Spector (1956) proved the existence of minimal degrees with uniform trees; Shoenfield observed that arbitrary computable f-trees suffice. Sacks (1961) built a minimal degree below $\obf'$, and Yates (1970) and Cooper (1972) below every non-zero c.e. degree. Lachlan and Lebeuf (1976) showed that every countable upper semilattice with least element is isomorphic to an initial segment of $\mathcal D$, so that the theory of initial segments is very rich. No PA degree is minimal, and Kumabe and Lewis (2009) built a minimal degree that computes a DNC function.

- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- G. E. Sacks, *A minimal degree less than 0′*, Bulletin of the American Mathematical Society 67 (1961), 416–419.
- M. Lerman, *Degrees of Unsolvability*, Springer, 1983.
- M. Kumabe and A. E. M. Lewis, *A fixed-point-free minimal degree*, Journal of the London Mathematical Society 80 (2009), 785–797.
