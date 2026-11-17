---
title: Minimal covers and minimal upper bounds
summary: Relativized splitting trees give a minimal cover of every degree and a minimal upper bound of every strictly increasing sequence of degrees; PA degrees, c.e. degrees and 1-generic degrees are not minimal, and the non-computability requirements of Spector's construction are redundant.
duration: 35
prerequisites: [minimal-degrees, pi01-classes/pa-degrees]
---

Spector's construction relativizes: replacing computable trees by trees computable in a set $A$ gives a degree immediately above $\deg_T(A)$. A second modification lets the oracle grow along the construction, and gives a minimal upper bound to every strictly increasing sequence of degrees. Together with the exact pair theorem, it describes what replaces least upper bounds in $\mathcal D$. The lesson ends with the limits of the method: several natural classes of degrees contain no minimal degree.

## Relativized splitting trees

The lemmas of the previous lesson relativize to any oracle $A$. An f-tree is **$A$-computable** if it is computable as a function with oracle $A$.

:::lemma{#lem-relativized-splitting}
Let $A$ be a set, $T$ an $A$-computable f-tree and $e \in \nat$.

1. There is an $A$-computable subtree $S$ of $T$ such that $\Phi^A_e \neq X$ for every $X \in [S]$.
2. There is an $A$-computable subtree $S$ of $T$ that is $e$-splitting or avoids $e$-splits.
3. If $S$ is an $A$-computable f-tree, $X \in [S]$ and $\Phi^X_e$ is total, then $\Phi^X_e \leq_T A$ if $S$ avoids $e$-splits, and $X \leq_T \Phi^X_e \oplus A$ if $S$ is $e$-splitting.
:::

:::proof{of=lem-relativized-splitting}
The proofs of :ref{#lem-ftree-noncomputable}, :ref{#lem-splitting-dichotomy} and :ref{#lem-splitting-consequences} apply with oracle $A$. In (1), the subtree is chosen according to $\Phi^A_e(i)$ instead of $\Phi_e(i)$. In (2) and (3), every search through the nodes of a tree uses the oracle $A$, which computes the tree; the decoding procedure of (3) also uses $\Phi^X_e$. The functional $\Phi_e$ is applied to strings, and is not relativized.
:::

The oracle $A$ appears in the conclusion of (3) only through the tree: a path of an $e$-splitting tree is recovered from its image by following the tree, and the tree is known only with $A$.

## Minimal covers

:::definition{#def-minimal-cover}
A degree $\bbf$ is a **minimal cover** of a degree $\abf$ if $\abf < \bbf$ and there is no degree $\cbf$ with $\abf < \cbf < \bbf$.
:::

A minimal degree is a minimal cover of $\obf$. The jump $\abf'$ is never a minimal cover of $\abf$: by the relativized Kleene–Post theorem (Soare, Theorem 6.1.2), there are degrees $\cbf$ with $\abf < \cbf < \abf'$.

:::theorem{#thm-minimal-cover}
For every set $A$ there is a set $B$ with $A <_T B$ such that no set $C$ satisfies $A <_T C <_T B$. So $\deg_T(B)$ is a minimal cover of $\deg_T(A)$.
:::

:::proof{of=thm-minimal-cover}
Relativize the construction to $A$, with $A$-computable f-trees, and start from the tree $T_0(\rho) = \rho \oplus (A \uh |\rho|)$ of :ref{#ex-ftree}, which interleaves the bits of $\rho$ with those of $A$; every path of every subtree computes $A$ from its odd bits. Alternate the two steps of :ref{#lem-relativized-splitting} (1) and (2) as in :ref{#thm-minimal-degree}, passing to full subtrees so that the roots increase. This gives $X \in [T_0]$ such that $X \neq \Phi^A_e$ for every $e$, and, by :ref{#lem-relativized-splitting} (3), such that every total $Y = \Phi^X_e$ satisfies $Y \leq_T A$ or $X \leq_T Y \oplus A$.

Let $B = X$. Then $A \leq_T B$, and $B \not\leq_T A$. If $A \leq_T C \leq_T B$ with $C = \Phi^B_e$, then $C \leq_T A$, or $B \leq_T C \oplus A \equiv_T C$. So there is no $C$ strictly between.
:::

:::quiz[minimal covers]
In the proof of :ref{#thm-minimal-cover}, why must every path of the initial tree compute $A$?

- [x] So that $B = X$ lies above $A$: then every $C$ with $A \leq_T C \leq_T B$ is of the form $\Phi^X_e$, and the relativized dichotomy gives $C \leq_T A$ or $X \leq_T C \oplus A \equiv_T C$.
- [ ] Because otherwise the trees would not be $A$-computable.

  The trees are $A$-computable by construction; the coding of $A$ ensures that $B$ lies above $A$.
- [ ] Because $A$ must be non-computable.

  $A$ is arbitrary; for computable $A$ the theorem gives a minimal degree.
:::

A minimal cover $\bbf$ of $\abf$ may still bound degrees incomparable with $\abf$: the construction only controls the sets that compute $A$. If every degree below $\bbf$ is below $\abf$, then $\bbf$ is a **strong minimal cover** of $\abf$. Not every degree has a strong minimal cover, and which degrees do is not known in general (Monin–Patey; see the survey of Lewis, 2009, on a related question of Yates).

## Minimal upper bounds

By :ref{#cor-not-lattice}, a strictly increasing sequence of degrees has no least upper bound. It has minimal ones.

:::definition{#def-minimal-upper-bound}
A degree $\mathbf m$ is a **minimal upper bound** of a set of degrees $\mathcal S$ if it is an upper bound of $\mathcal S$ and no upper bound of $\mathcal S$ is strictly below $\mathbf m$.
:::

For example, if $\mathcal S$ has a greatest element, it is the only minimal upper bound. The exact pair theorem does not give minimal upper bounds: it controls the common lower bounds of two upper bounds, not the upper bounds below each of them.

:::theorem[Sacks]{#thm-minimal-upper-bound}
Every strictly increasing sequence $\dbf_0 < \dbf_1 < \cdots$ of degrees has a minimal upper bound.
:::

*Idea of the proof.* A minimal cover of $\deg_T(A)$ is built with $A$-computable trees whose paths all compute $A$. Here the oracle must grow: at step $n$, the trees are computable in a set $B_n \in \dbf_n$, and the construction passes to a subtree whose paths all compute $B_{n+1}$. The splitting step relative to $B_n$ yields the dichotomy of :ref{#lem-relativized-splitting}: a set $Y$ computed by the final path $X$ either is computable in $B_n$, and then it is not an upper bound, since it does not compute $B_{n+1}$; or it computes $X$ with the help of $B_n$, and then it computes $X$ if it is an upper bound.

:::proof{of=thm-minimal-upper-bound}
Let $B_n \in \dbf_n$. Since $\dbf_n \leq \dbf_{n+1}$, every $B_n$-computable tree is $B_{n+1}$-computable. For an f-tree $S$ and a set $C$, the **coding subtree** $S_C$ is defined by $S_C(\rho) = S(c(\rho))$, where $c(\varepsilon) = \varepsilon$ and $c(\rho i) = c(\rho)\, C(|\rho|)\, i$. The map $c$ preserves the prefix relation and incompatibility, so $S_C$ is a subtree of $S$, computable in $S \oplus C$. Its paths **code** $C$ relative to $S$: if $X \in [S_C]$, then $C \leq_T X \oplus S$. Indeed, let $\mu_0 = \varepsilon$, so that $S(\mu_0) \prec X$. Given $\mu_k = c(\rho)$ with $|\rho| = k$ and $S(\mu_k) \prec X$, exactly one of the incompatible nodes $S(\mu_k 0)$ and $S(\mu_k 1)$ is a prefix of $X$, namely $S(\mu_k\, C(k))$, because $X$ extends a node $S_C(\rho j) = S(\mu_k\, C(k)\, j)$: a node of $S_C$ longer than $S_C(\rho)$ that is a prefix of $X$ is of the form $S_C(\rho')$ with $\rho' \succeq \rho j$ for some $j$. So comparing these nodes with $X$ gives $C(k)$; comparing $S(\mu_k\, C(k)\, 0)$ and $S(\mu_k\, C(k)\, 1)$ with $X$ gives the bit $j$, and $\mu_{k+1} = \mu_k\, C(k)\, j$.

Let $T_0$ be the coding subtree of the identity tree for $B_0$; it is $B_0$-computable. Given a $B_n$-computable f-tree $T_n$, let $S$ be given by :ref{#lem-relativized-splitting} (2) for the oracle $B_n$, the tree $T_n$ and $e = n$, and let $T_{n+1}$ be the full subtree of $S_{B_{n+1}}$ above $S_{B_{n+1}}(0)$. It is $B_{n+1}$-computable, and its root strictly extends that of $T_n$. As in the proof of :ref{#thm-minimal-degree}, the union $X$ of the roots belongs to $[T_n]$ for every $n$.

*$X$ computes every $B_n$.* By induction on $n$. The tree $T_0$ is the coding subtree of the identity, so $X \in [T_0]$ computes $B_0$. Suppose $B_n \leq_T X$. The tree $S$ of step $n$ is $B_n$-computable, hence $X$-computable, and $X \in [T_{n+1}] \subseteq [S_{B_{n+1}}]$, so $B_{n+1} \leq_T X \oplus S \leq_T X$.

*$\deg_T(X)$ is a minimal upper bound.* It is an upper bound by the previous paragraph. Let $Y \leq_T X$ compute every $B_n$, say $Y = \Phi^X_e$. Let $S$ be the tree of step $e$. It is $B_e$-computable and $X \in [S]$. If $S$ avoids $e$-splits, then $Y \leq_T B_e$ by :ref{#lem-relativized-splitting} (3); since $B_{e+1} \leq_T Y$, this gives $\dbf_{e+1} \leq \dbf_e$, a contradiction. So $S$ is $e$-splitting, and $X \leq_T Y \oplus B_e \equiv_T Y$. Hence no upper bound of the sequence is strictly below $\deg_T(X)$.
:::

The strictness of the sequence is used once, to exclude the case where $\Phi_e$ loses information. Since a countable ideal without greatest element contains a strictly increasing cofinal sequence, every such ideal has a minimal upper bound. Sacks showed that there are continuum many (:ref{#ex-mub-continuum}); two distinct ones $\mathbf m \neq \mathbf m'$ again exclude a least upper bound $\mathbf l$, which would satisfy $\mathbf l \leq \mathbf m$, hence $\mathbf l = \mathbf m$ by minimality, and likewise $\mathbf l = \mathbf m'$.

:::quiz[minimal upper bounds]
In the proof of :ref{#thm-minimal-upper-bound}, why is the dichotomy at step $e$ taken relative to $B_e$, and not relative to the final set $X$ or to a fixed oracle?

- [x] Because the tree $T_e$ is only $B_e$-computable: the splitting procedure and the decoding search through its nodes, so the conclusions of :ref{#lem-relativized-splitting} (3) hold relative to $B_e$, which every upper bound computes.
- [ ] Because $X$ is computable in $B_e$.

  $X$ computes $B_{e+1}$, which is not computable in $B_e$; so $X \not\leq_T B_e$.
- [ ] Because a computable tree cannot be $e$-splitting.

  Computable trees may well be $e$-splitting; but a computable tree cannot code the non-computable sets $B_n$, so the trees must use the oracles.
:::

## Degrees that are not minimal

Several natural classes contain no minimal degree: the non-zero c.e. degrees (:ref{#cor-no-minimal-ce}), the 1-generic degrees (:ref{#ex-generic-not-minimal}), and the PA degrees.

:::proposition{#prop-pa-not-minimal}
No PA degree is minimal.
:::

:::proof{of=prop-pa-not-minimal}
Let $\mathcal P$ be the class of sets $X \oplus Y$ such that $X(e) \neq \Phi_e(e)$ for every $e$ with $\Phi_e(e)\converge$, and $Y(e) \neq \Phi^X_e(e)$ for every $e$ with $\Phi^X_e(e)\converge$. A set fails to belong to $\mathcal P$ if and only if some computation $\Phi_e(e)$, or some computation $\Phi^{\sigma}_e(e)$ with $\sigma$ a prefix of $X$, converges to the corresponding bit; this is witnessed by a finite prefix of $X \oplus Y$, so $\mathcal P$ is a $\Pi^0_1$ class. It is non-empty: take $X$ in $\mathrm{DNC}_2$, which is non-empty (:ref{#thm-dnc2-no-computable}), and $Y(e) = 1$ if $\Phi^X_e(e)\converge = 0$, $Y(e) = 0$ otherwise.

Let $A$ be PA. By :ref{#thm-pa-characterization}, $A$ computes a member $X \oplus Y$ of $\mathcal P$. The set $X$ is not computable, by :ref{#thm-dnc2-no-computable}. The set $Y$ is not computable in $X$: if $Y = \Phi^X_e$, then $Y(e) = \Phi^X_e(e)$, which the definition of $\mathcal P$ excludes. So $X <_T X \oplus Y \leq_T A$, and $\obf < \deg_T(X) < \deg_T(A)$.
:::

Nevertheless, every PA degree bounds a minimal degree (Groszek and Slaman, 1997), and so does every non-zero c.e. degree (Yates, 1970; Cooper, 1972). On the other hand, the degrees that bound no minimal degree form a comeager class (Martin) and a class of measure one (Paris); see Shore (1997).

## Exercises

The two exercises below return to Spector's construction of the previous lesson.

::::exercise{#ex-continuum-minimal difficulty=2 objective="Branch Spector's construction according to a parameter to obtain continuum many minimal degrees."}
Show that there are continuum many minimal degrees.

:::hint
Modify the construction as in :ref{#ex-ftree-continuum}: at each step, choose between the two subtrees above $T(0)$ and $T(1)$ according to a bit of a parameter $Z \in \cs$.
:::

:::solution
Fix the subtrees given by the lemmas, choosing the least witness in Case 1, so that each step is determined by the current tree. For $Z \in \cs$, run the construction, but at each even step $2e+2$ pass to the full subtree of $S$ above $S(Z(e))$ instead of $S(0)$. Let $X_Z$ be the union of the roots. As before, $X_Z$ has minimal degree. If $Z$ and $Z'$ first differ at $e$, the constructions coincide up to step $2e + 1$ and produce the same $S$; then $X_Z$ and $X_{Z'}$ extend the incompatible nodes $S(0)$ and $S(1)$, so $X_Z \neq X_{Z'}$. Each degree contains countably many sets, so the continuum many sets $X_Z$ have continuum many degrees. This is Soare's Exercise 12.6.2.
:::
::::

::::exercise{#ex-posner-epstein difficulty=2 objective="Design a functional that defeats both cases of the splitting dichotomy on a computable path, to show that the non-computability steps are redundant."}
Let $X$ be a set such that, for every $e$, $X$ is a path of some computable f-tree that is $e$-splitting or avoids $e$-splits. Show that $X$ is not computable. Conclude that the odd steps of the proof of :ref{#thm-minimal-degree} can be omitted.

:::hint
If $X$ is computable, consider the functional with $\Phi^\sigma_e(x) = \sigma(x)$ for $x < |\sigma|$ when $\sigma$ is not a prefix of $X$, and $\Phi^\sigma_e(x)$ undefined for all $x$ when $\sigma$ is a prefix of $X$.
:::

:::solution
Suppose $X$ computable, and let $\Phi_e$ be the functional of the hint. It is a functional: the strings that are not prefixes of $X$ are closed under extension, and their outputs extend each other. Let $T$ be a computable f-tree with $X \in [T]$ that is $e$-splitting or avoids $e$-splits.

*$T$ is not $e$-splitting.* Some node $T(\rho)$ is a prefix of $X$, and so is one of its successors $T(\rho i)$, since a longer node $T(\rho') \prec X$ has $\rho' \succeq \rho i$ for some $i$. On the prefix $T(\rho i)$ of $X$, $\Phi_e$ is nowhere defined, so $T(\rho 0)$ and $T(\rho 1)$ do not form an $e$-split.

*$T$ does not avoid $e$-splits.* The successors $T(0)$ and $T(1)$ are incompatible, so one of them, say $\tau$, is not a prefix of $X$. The other one, $\tau'$, has two incompatible successors in $T$, and one of them, $\tau''$, is not a prefix of $X$. The strings $\tau$ and $\tau''$ are incompatible, and neither is a prefix of $X$; so $\Phi_e$ outputs their bits, which differ at some position below both lengths, and they form an $e$-split.

This contradicts the choice of $T$. In the proof of :ref{#thm-minimal-degree}, the even steps alone give such trees for every $e$, so the set built without the odd steps is still non-computable.
:::
::::

## Notes and references

Monin and Patey present minimal covers and strong minimal covers in their chapter on the structure of the degrees. Soare gives the minimal upper bound theorem, with a hint, as Exercise 12.6.1 of *Turing Computability*, crediting it to Sacks; Monin and Patey state that there are continuum many minimal upper bounds, after Sacks's monograph. The non-computability lemma of :ref{#ex-posner-epstein} is Lemma 12.2.1 in Soare, credited to Posner and Epstein. That no PA degree is minimal, with the class $\mathcal P$ used here, is an exercise in Monin and Patey; Groszek and Slaman (1997) proved that every PA degree bounds a minimal degree. Kumabe built a minimal degree that computes a DNC function; the proof was published by Kumabe and Lewis (2009), and recast as a forcing with **bushy trees** by Khan and Miller (2017). Jockusch and Posner (1978) showed that every minimal degree $\abf$ satisfies $\abf'' = (\abf \vee \obf')'$. Lachlan and Lebeuf (1976) showed, by elaborations of the tree method, that every countable upper semilattice with least element is isomorphic to an initial segment of $\mathcal D$; Lerman's monograph presents these constructions.

- G. E. Sacks, *Degrees of Unsolvability*, Annals of Mathematics Studies 55, Princeton University Press, 1963 (revised edition 1966).
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 12.2 and Exercise 12.6.1.
- M. J. Groszek and T. A. Slaman, *Π⁰₁ classes and minimal degrees*, Annals of Pure and Applied Logic 87 (1997), 117–144.
- M. Kumabe and A. E. M. Lewis, *A fixed-point-free minimal degree*, Journal of the London Mathematical Society 80 (2009), 785–797.
- M. Khan and J. S. Miller, *Forcing with bushy trees*, Bulletin of Symbolic Logic 23 (2017), 160–180.
- C. G. Jockusch, Jr. and D. Posner, *Double jumps of minimal degrees*, Journal of Symbolic Logic 43 (1978), 715–724.
- A. H. Lachlan and R. Lebeuf, *Countable initial segments of the degrees of unsolvability*, Journal of Symbolic Logic 41 (1976), 289–300.
- A. E. M. Lewis, *Strong minimal covers and a question of Yates: the story so far*, in *Logic Colloquium 2006*, Lecture Notes in Logic 32, 2009, 213–228.
- R. A. Shore, *Conjectures and questions from Gerald Sacks's Degrees of Unsolvability*, Archive for Mathematical Logic 36 (1997), 233–253.

:::::exercises
::::exercise{#ex-pi01-no-minimal difficulty=1 objective="Show that the leftmost path of a $\Pi^0_1$ class has c.e. degree, and deduce that no non-empty $\Pi^0_1$ class consists of minimal degrees."}
Show that there is no non-empty $\Pi^0_1$ class all of whose members have minimal degree.

:::solution
Let $\mathcal P = [T]$ be non-empty, with $T$ computable, and $X$ its leftmost path: for every $n$, $X \uh n$ is the lexicographically least string of length $n$ that is extendible in $T$. Let $L$ be the set of strings $\sigma$ that are lexicographically smaller than $X \uh |\sigma|$. Then $\sigma \in L$ if and only if every string $\tau$ of length $|\sigma|$ with $\tau \leq_{\mathrm{lex}} \sigma$ satisfies $[\tau] \cap \mathcal P = \emptyset$; this is a finite conjunction of $\Sigma^0_1$ conditions (:ref{#prop-pi01-emptiness}), so $L$ is c.e. The set $L$ computes $X$: $X \uh n$ is the least string of length $n$ not in $L$. Conversely $X$ computes $L$. So $X$ has c.e. degree. If $X$ is computable, it does not have minimal degree; otherwise its degree is c.e. and non-zero, hence not minimal by :ref{#cor-no-minimal-ce}. Adapted from an exercise of Monin and Patey, chapter on the structure of the degrees.
:::
::::

::::exercise{#ex-minimal-cover-join difficulty=1 objective="Characterize minimal covers through joins with the degrees below them."}
Let $\abf < \bbf$. Show that $\bbf$ is a minimal cover of $\abf$ if and only if every degree $\cbf \leq \bbf$ satisfies $\cbf \leq \abf$ or $\abf \vee \cbf = \bbf$.

:::solution
Suppose $\bbf$ is a minimal cover of $\abf$, and let $\cbf \leq \bbf$. Then $\abf \leq \abf \vee \cbf \leq \bbf$, so $\abf \vee \cbf$ is $\abf$ or $\bbf$. In the first case $\cbf \leq \abf$. Conversely, suppose the condition holds and $\abf < \cbf < \bbf$. Then $\cbf \not\leq \abf$, since $\abf \leq \cbf$ and $\cbf \neq \abf$; and $\abf \vee \cbf = \cbf \neq \bbf$. This contradicts the condition. For $\abf = \obf$, the condition says that every non-zero degree below $\bbf$ is $\bbf$ itself.
:::
::::

::::exercise{#ex-ideal-mub difficulty=1 objective="Extract a strictly increasing cofinal sequence from a countable ideal without greatest element." lessons="exact-pairs"}
Let $\mathcal I$ be a countable ideal without greatest element. Show that there is a strictly increasing sequence $\dbf_0 < \dbf_1 < \cdots$ of elements of $\mathcal I$ such that every element of $\mathcal I$ is below some $\dbf_n$. Deduce that every countable ideal has a minimal upper bound.

:::solution
List the elements of $\mathcal I$ as $\cbf_0, \cbf_1, \dots$. Let $\dbf_0 = \cbf_0$. Given $\dbf_n \in \mathcal I$, it is not the greatest element of $\mathcal I$, so some $\cbf_k$ satisfies $\cbf_k \not\leq \dbf_n$; take the least such $k$, and let $\dbf_{n+1} = \dbf_n \vee \cbf_k \vee \cbf_{n+1}$. It belongs to $\mathcal I$, by closure under $\vee$, and $\dbf_n < \dbf_{n+1}$, since $\dbf_n \leq \dbf_{n+1}$ and $\cbf_k \leq \dbf_{n+1}$, $\cbf_k \not\leq \dbf_n$. Every $\cbf_n$ is below $\dbf_n$, by construction for $n \geq 1$, and $\cbf_0 = \dbf_0$.

The upper bounds of $\mathcal I$ are then exactly the upper bounds of the sequence: an upper bound of the sequence is above every $\cbf_n$, and the $\dbf_n$ belong to $\mathcal I$. So a minimal upper bound of the sequence, given by :ref{#thm-minimal-upper-bound}, is a minimal upper bound of $\mathcal I$. If $\mathcal I$ has a greatest element, this element is its least upper bound, hence its only minimal upper bound. The two cases give a minimal upper bound for every countable ideal.
:::
::::

::::exercise{#ex-minimal-cover-bound difficulty=2 objective="Relativize the effectivity analysis of Spector's construction."}
Show that for every set $A$, the set $B$ of :ref{#thm-minimal-cover} can be chosen computable in $A''$.

:::solution
We follow the analysis of :ref{#thm-minimal-degree}, relative to $A$. An $A$-computable f-tree is given by an index $k$ with $T = \Phi^A_k$. The initial tree $T_0(\rho) = \rho \oplus (A \uh |\rho|)$ has an index computable outright. At a step of the first kind, for the index of $T$ and $e$, one asks whether $\Phi^A_e(i)\converge = T(0)(i)$, where $i$ is the first position where $T(0)$ and $T(1)$ differ, found with $A$; this is a $\Sigma^0_1$ question relative to $A$, answered by $A'$, hence by $A''$. The index of the full subtree chosen is computable from the answer. At a step of the second kind, the relation "$T(\rho)$ and $T(\rho')$ form an $e$-split" is $\Sigma^0_1$ relative to $A$, uniformly in the index of $T$; so "no two extensions above $T(\nu)$ form an $e$-split" is $\Pi^0_1$ relative to $A$, the existence of such a $\nu$ is $\Sigma^0_2$ relative to $A$, and $A''$ decides it and finds the least $\nu$. In Case 2, the splitting subtree has an index computable from the index of $T$ and $e$, and the passage to a full subtree is computable on indices. So the sequence of indices is computable in $A''$, and the roots, hence $X = B$, are computable from it with the oracle $A \leq_T A''$.
:::
::::

::::exercise{#ex-pa-relative-not-cover difficulty=2 objective="Relativize the proof that PA degrees are not minimal, to show that a degree PA relative to $\abf$ is not a minimal cover of $\abf$." lessons="pi01-classes/pa-degrees"}
A set $B$ is PA relative to a set $A$ if it computes a function $f : \nat \to \{0, 1\}$ with $f(e) \neq \Phi^A_e(e)$ whenever $\Phi^A_e(e)\converge$ (:ref{#ex-pa-relative}). Show that if $B$ is PA relative to $A$, then $\deg_T(B)$ is not a minimal cover of $\deg_T(A)$.

:::solution
Relativize :ref{#prop-pa-not-minimal}. Let $\mathcal P_A$ be the class of sets $X \oplus Y$ such that $X(e) \neq \Phi^A_e(e)$ whenever $\Phi^A_e(e)\converge$, and $Y(e) \neq \Phi^{A \oplus X}_e(e)$ whenever $\Phi^{A \oplus X}_e(e)\converge$. A set fails to belong to $\mathcal P_A$ if and only if a finite prefix of it witnesses a convergent computation with the forbidden value, which can be recognized with the oracle $A$; so $\mathcal P_A$ is the class of paths of an $A$-computable tree. It is non-empty: let $X(e) = 1$ if $\Phi^A_e(e)\converge = 0$ and $X(e) = 0$ otherwise, and define $Y$ from $A \oplus X$ in the same way.

By the relativized characterization of PA sets (the proof of :ref{#thm-pa-characterization} relativized, as in :ref{#ex-pa-relative}), $B$ computes a member $X \oplus Y$ of $\mathcal P_A$, and $A \leq_T B$ by :ref{#ex-pa-relative}. The set $X$ is not computable in $A$: if $X = \Phi^A_e$, then $\Phi^A_e(e)\converge = X(e)$, which is excluded. Similarly $Y$ is not computable in $A \oplus X$. So
$$
A <_T A \oplus X <_T A \oplus X \oplus Y \leq_T B,
$$
and $\deg_T(A \oplus X)$ lies strictly between $\deg_T(A)$ and $\deg_T(B)$. In particular, a minimal cover of $\abf$ is never PA relative to $\abf$; for $A = \emptyset$, this is :ref{#prop-pa-not-minimal}.
:::
::::

::::exercise{#ex-mub-continuum difficulty=2 objective="Branch the construction of a minimal upper bound to obtain continuum many of them."}
Let $\dbf_0 < \dbf_1 < \cdots$ be a strictly increasing sequence of degrees. Show that it has continuum many minimal upper bounds.

:::solution
In the proof of :ref{#thm-minimal-upper-bound}, fix the subtrees given by :ref{#lem-relativized-splitting} (2), choosing the least $\nu$ in Case 1, so that each step is determined by the current tree. For $Z \in \cs$, run the construction, but at step $n$ let $T_{n+1}$ be the full subtree of $S_{B_{n+1}}$ above $S_{B_{n+1}}(Z(n))$ instead of $S_{B_{n+1}}(0)$. Let $X_Z$ be the union of the roots.

The proof applies to $X_Z$ without change: $T_{n+1}$ is still a $B_{n+1}$-computable subtree of $S_{B_{n+1}}$, and its root $S_{B_{n+1}}(Z(n)) = S(B_{n+1}(0)\, Z(n))$ strictly extends the root $S(\varepsilon)$ of $S$, which extends the root of $T_n$. So $\deg_T(X_Z)$ is a minimal upper bound of the sequence.

If $Z$ and $Z'$ first differ at $n$, the two constructions coincide up to step $n$, which produces the same tree $S_{B_{n+1}}$ for both; then $X_Z$ and $X_{Z'}$ extend the incompatible nodes $S_{B_{n+1}}(0)$ and $S_{B_{n+1}}(1)$, so $X_Z \neq X_{Z'}$. Each degree contains countably many sets, so the continuum many sets $X_Z$ have continuum many degrees. The method is that of :ref{#ex-continuum-minimal}.
:::
::::

::::exercise{#ex-mub-arithmetic difficulty=2 objective="Analyze the effectivity of a tree construction whose oracle grows."}
Let $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$. Show that the arithmetic degrees have a minimal upper bound computable in $\emptyset^{(\omega)}$.

:::solution
The sequence $\obf^{(n)}$ is strictly increasing and cofinal in the arithmetic degrees, so a minimal upper bound of the sequence is a minimal upper bound of the arithmetic degrees. Apply the proof of :ref{#thm-minimal-upper-bound} with $B_n = \emptyset^{(n)}$. Every set $X$ is $X$-c.e. through a single index, that of the machine that halts on $x$ if and only if $x$ is in its oracle; so item 2 of :ref{#thm-jump} gives one computable function $f$ with $x \in X \iff f(x) \in X'$ for every $X$. Replacing each query "$y \in B_n$?" by "$f(y) \in B_{n+1}$?" turns a $B_n$-index of a tree into a $B_{n+1}$-index of the same tree, uniformly in $n$.

Step $n$ starts from a $B_n$-index of $T_n$. To find $S$ by :ref{#lem-relativized-splitting} (2), one must decide whether some node of $T_n$ has no two extensions forming an $n$-split, a $\Sigma^0_2$ question relative to $B_n$, and find the least such node if it exists, by $\Pi^0_1$ questions relative to $B_n$; the oracle $B_n'' = \emptyset^{(n+2)}$ answers them. Otherwise $S$ is the splitting subtree, with a $B_n$-index computable from that of $T_n$. The coding subtree $S_{B_{n+1}}$ and its full subtree above $S_{B_{n+1}}(0)$ then have a $B_{n+1}$-index computable from the index of $S$. Since $\emptyset^{(\omega)}$ computes $\emptyset^{(n+2)}$ uniformly in $n$, as its column $n + 2$, the sequence of indices is computable in $\emptyset^{(\omega)}$, and so is the sequence of roots, each root $T_n(\varepsilon)$ being computed with the oracle $B_n$ from its index. So $X \leq_T \emptyset^{(\omega)}$.
:::
::::
:::::
