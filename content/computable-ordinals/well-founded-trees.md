---
title: Well-founded trees
summary: Trees on ℕ, well-foundedness and ranks, the tree of descending sequences of a well-ordering, the Kleene–Brouwer ordering, and the ranks of computable well-founded trees.
duration: 35
prerequisites: [computable-well-orderings]
---

Well-founded trees are the second representation of ordinals used in the track, next to well-orderings. A tree is well-founded when it has no infinite path; its **rank** measures how far it is from having one. Trees are the natural form of $\Pi^1_1$ conditions: the next lesson shows that every $\Pi^1_1$ set is of the form $\{ n : T_n \text{ is well-founded} \}$ for a computable sequence of trees. This lesson develops the two tools that connect trees with ordinals: ranks, which assign an ordinal to a well-founded tree, and the Kleene–Brouwer ordering, which turns a tree into a linear order that is a well-ordering exactly when the tree is well-founded.

## Trees on ℕ and their ranks

A **tree** $T \subseteq \nat^{<\nat}$ is a set of finite sequences of numbers closed under prefixes. For a sequence $\sigma$ and a number $n$, $\sigma n$ denotes the sequence $\sigma$ followed by $n$, and $\sigma\tau$ the concatenation of $\sigma$ and $\tau$. A **path** of $T$ is a function $f \in \nat^\nat$ all of whose prefixes $f \uh m$ belong to $T$. The tree is **well-founded** if it has no path, and **ill-founded** otherwise. For $\sigma \in \nat^{<\nat}$, write $T_\sigma = \{ \tau : \sigma\tau \in T \}$, the part of $T$ above $\sigma$, seen as a tree; it is empty if $\sigma \notin T$.

:::example{#ex-trees}
1. Every finite tree is well-founded. The full tree $\nat^{<\nat}$ is ill-founded, and so is the tree of sequences of zeros, whose only path is the constant function $0$.
2. The tree $T$ of strictly decreasing sequences $n_0 > n_1 > \cdots > n_k$ of numbers is well-founded, since a path would be an infinite decreasing sequence of numbers. It is infinite and has nodes of every length, but each branch is finite.
3. The tree of sequences $\sigma$ such that $\sigma(i) \neq 0$ for $i \geq 1$ and $|\sigma| \leq \sigma(0) + 1$ is well-founded: above the node $\langle n \rangle$ there are only sequences of length at most $n + 1$. König's lemma does not apply, since the root has infinitely many immediate successors.
:::

:::definition{#def-tree-rank}
The **rank** of a well-founded tree is defined by transfinite recursion: $\mathrm{rk}(T) = \sup \{ \mathrm{rk}(T_{\langle n \rangle}) + 1 : \langle n \rangle \in T \}$, and $\mathrm{rk}(\emptyset) = 0$.
:::

The recursion is legitimate because the relation "$\tau$ properly extends $\sigma$", restricted to a well-founded tree, has no infinite increasing chains. A tree with a path has no rank. The tree $\{ \langle \rangle \}$ with only the root, like the empty tree, has rank $0$; a node $\sigma$ of $T$ is a **leaf** when $\mathrm{rk}(T_\sigma) = 0$, and in general $\mathrm{rk}(T_\sigma)$ is the **rank of the node** $\sigma$. In :ref{#ex-trees} (2), the node $\langle n \rangle$ has rank $n$, by induction on $n$, and the tree has rank $\sup_n (n + 1) = \omega$: every branch is finite, but there are branches of every finite length. In (3), the node $\langle n \rangle$ has rank $n$ as well, and the tree has rank $\omega$.

Every countable ordinal is the rank of a well-founded tree, and the tree can be taken computable when the ordinal is computable.

:::proposition{#prop-descending-tree}
Let $L$ be a well-ordering of a subset of $\nat$, and let $D_L$ be the tree of finite sequences $x_0 >_L x_1 >_L \cdots >_L x_k$ of elements of its field that are strictly decreasing for $L$. Then $D_L$ is well-founded and $\mathrm{rk}(D_L) = |L|$. If $L$ is computable, so is $D_L$, uniformly in an index of $L$.
:::

:::proof{of=prop-descending-tree}
A path of $D_L$ would be an infinite descending sequence of $L$, so $D_L$ is well-founded. For $x$ in the field of $L$, the tree $(D_L)_{\langle x \rangle}$ is the tree of decreasing sequences of elements $<_L x$. We show by induction along $L$ that its rank is $|L_{<x}|$, the type of the initial segment below $x$. Its immediate successors are the sequences $\langle y \rangle$ with $y <_L x$, above which lies the tree of decreasing sequences below $y$, of rank $|L_{<y}|$ by the induction hypothesis. So the rank is $\sup_{y <_L x} (|L_{<y}| + 1) = |L_{<x}|$, since in a well-ordering the initial segment below $x$ is the union of the segments $L_{<y} \cup \{ y \}$ for $y <_L x$. The same computation at the root gives $\mathrm{rk}(D_L) = \sup_x (|L_{<x}| + 1) = |L|$. Membership in $D_L$ is decided by finitely many queries to $L$.
:::

## The Kleene–Brouwer ordering

A tree is a partial order, and its ranks are ordinals, but the tree is not itself a well-ordering. The Kleene–Brouwer ordering linearizes it: it lists the nodes from left to right, each node after all its extensions, as in a post-order traversal of a finite tree.

The **Kleene–Brouwer ordering** on $\nat^{<\nat}$ is defined by $\sigma <_{\mathrm{KB}} \tau$ if $\sigma$ properly extends $\tau$, or if $\sigma(i) < \tau(i)$ at the first position $i$ where they differ. It is a computable linear order: extensions come before their prefixes, and incomparable sequences are compared lexicographically. On the whole of $\nat^{<\nat}$ it is not a well-ordering: $\langle 0 \rangle >_{\mathrm{KB}} \langle 0, 0 \rangle >_{\mathrm{KB}} \langle 0, 0, 0 \rangle >_{\mathrm{KB}} \cdots$.

:::figure[A finite tree. The number inside each node is its position in the Kleene–Brouwer ordering, starting from $0$; next to it, the rank of the node. The ordering visits the leftmost branch first, from the top down, and each node comes after all the nodes above it and to its left. The order type, $8$, is larger than the rank, $3$.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="A finite tree; each node carries its rank and its position in the Kleene-Brouwer ordering"><line x1="300" y1="34" x2="150" y2="104" class="ink-stroke" stroke-width="1.3"/><line x1="150" y1="104" x2="100" y2="174" class="ink-stroke" stroke-width="1.3"/><line x1="100" y1="174" x2="100" y2="244" class="ink-stroke" stroke-width="1.3"/><line x1="150" y1="104" x2="200" y2="174" class="ink-stroke" stroke-width="1.3"/><line x1="300" y1="34" x2="300" y2="104" class="ink-stroke" stroke-width="1.3"/><line x1="300" y1="34" x2="450" y2="104" class="ink-stroke" stroke-width="1.3"/><line x1="450" y1="104" x2="450" y2="174" class="ink-stroke" stroke-width="1.3"/><circle cx="300" cy="34" r="13" class="node"/><text x="300.0" y="39.0" text-anchor="middle" class="mrm" font-size="14">7</text><text x="280.0" y="39.0" text-anchor="end" class="mrm" font-size="13">⟨⟩</text><text x="320.0" y="39.0" text-anchor="start" class="label" font-size="12">rk 3</text><circle cx="150" cy="104" r="13" class="node"/><text x="150.0" y="109.0" text-anchor="middle" class="mrm" font-size="14">3</text><text x="130.0" y="109.0" text-anchor="end" class="mrm" font-size="13">⟨0⟩</text><text x="170.0" y="109.0" text-anchor="start" class="label" font-size="12">rk 2</text><circle cx="100" cy="174" r="13" class="node"/><text x="100.0" y="179.0" text-anchor="middle" class="mrm" font-size="14">1</text><text x="80.0" y="179.0" text-anchor="end" class="mrm" font-size="13">⟨0,0⟩</text><text x="120.0" y="179.0" text-anchor="start" class="label" font-size="12">rk 1</text><circle cx="100" cy="244" r="13" class="node"/><text x="100.0" y="249.0" text-anchor="middle" class="mrm" font-size="14">0</text><text x="80.0" y="249.0" text-anchor="end" class="mrm" font-size="13">⟨0,0,0⟩</text><text x="120.0" y="249.0" text-anchor="start" class="label" font-size="12">rk 0</text><circle cx="200" cy="174" r="13" class="node"/><text x="200.0" y="179.0" text-anchor="middle" class="mrm" font-size="14">2</text><text x="180.0" y="179.0" text-anchor="end" class="mrm" font-size="13">⟨0,1⟩</text><text x="220.0" y="179.0" text-anchor="start" class="label" font-size="12">rk 0</text><circle cx="300" cy="104" r="13" class="node"/><text x="300.0" y="109.0" text-anchor="middle" class="mrm" font-size="14">4</text><text x="280.0" y="109.0" text-anchor="end" class="mrm" font-size="13">⟨1⟩</text><text x="320.0" y="109.0" text-anchor="start" class="label" font-size="12">rk 0</text><circle cx="450" cy="104" r="13" class="node"/><text x="450.0" y="109.0" text-anchor="middle" class="mrm" font-size="14">6</text><text x="430.0" y="109.0" text-anchor="end" class="mrm" font-size="13">⟨2⟩</text><text x="470.0" y="109.0" text-anchor="start" class="label" font-size="12">rk 1</text><circle cx="450" cy="174" r="13" class="node"/><text x="450.0" y="179.0" text-anchor="middle" class="mrm" font-size="14">5</text><text x="430.0" y="179.0" text-anchor="end" class="mrm" font-size="13">⟨2,0⟩</text><text x="470.0" y="179.0" text-anchor="start" class="label" font-size="12">rk 0</text><circle cx="340" cy="244" r="11" class="node"/><text x="358.0" y="248.0" text-anchor="start" class="label" font-size="12">position in the Kleene–Brouwer order</text><text x="340.0" y="276.0" text-anchor="start" class="label" font-size="12">rk: rank of the subtree above the node</text></svg>
:::

:::theorem{#thm-kleene-brouwer}
A tree $T$ is well-founded if and only if $<_{\mathrm{KB}}$ restricted to $T$ is a well-ordering. In that case, its order type is at least $\mathrm{rk}(T)$.
:::

:::proof{of=thm-kleene-brouwer}
If $T$ has a path $f$, then $f \uh 0 >_{\mathrm{KB}} f \uh 1 >_{\mathrm{KB}} \cdots$ is a descending sequence.

Suppose $T$ well-founded; we prove by induction on $\mathrm{rk}(T)$ that $(T, <_{\mathrm{KB}})$ is a well-ordering of type at least $\mathrm{rk}(T)$. If $T$ is empty, both are $0$. Otherwise, the nodes of $T$ other than the root are the sequences $\langle n \rangle \tau$ with $\tau \in T_{\langle n \rangle}$, and the ordering compares first the initial numbers $n$, then the sequences $\tau$ by the Kleene–Brouwer ordering; the root comes last. So $(T, <_{\mathrm{KB}})$ is the ordered sum of the orderings $(T_{\langle n \rangle}, <_{\mathrm{KB}})$ for $n = 0, 1, 2, \dots$ with $\langle n \rangle \in T$, followed by one element. Each summand is a well-ordering of type at least $\mathrm{rk}(T_{\langle n \rangle})$, by the induction hypothesis, and an ordered sum of well-orderings indexed by a well-ordering is a well-ordering. Its type is at least $\mathrm{rk}(T_{\langle n \rangle}) + 1$ for every $n$, hence at least $\mathrm{rk}(T)$.
:::

:::quiz[the Kleene–Brouwer ordering]
Why do extensions come **before** their prefixes in the Kleene–Brouwer ordering?

- [x] So that a path, which gives longer and longer prefixes, yields a descending sequence; with the opposite convention, a path would give an increasing sequence, compatible with well-ordering.
- [ ] So that the ordering is computable.

  Both conventions give computable orderings; the choice matters for well-foundedness.
- [ ] So that the root is the least element.

  With this convention the root is the largest element.
:::

The inequality between the order type and the rank can be strict, as in the figure. For an infinite example, the tree consisting of the root and the sequences $\langle n \rangle$, $n \in \nat$, has rank $1$, while its Kleene–Brouwer ordering is $\langle 0 \rangle < \langle 1 \rangle < \cdots < \langle \rangle$, of type $\omega + 1$.

## Ranks of computable trees

:::proposition{#prop-rank-computable}
The rank of a computable well-founded tree is a computable ordinal, and every computable ordinal is the rank of a computable well-founded tree. Hence $\omega_1^{\mathrm{CK}}$ is the supremum of the ranks of the computable well-founded trees, and it is not attained.
:::

:::proof{of=prop-rank-computable}
If $T$ is computable, then the restriction of $<_{\mathrm{KB}}$ to $T$ is a computable linear order, a well-ordering if $T$ is well-founded, of type at least $\mathrm{rk}(T)$ by :ref{#thm-kleene-brouwer}. Its type is computable, and so is $\mathrm{rk}(T)$, by :ref{#prop-computable-ordinals-basic} (1). Conversely, if $\alpha$ is computable, the tree $D_L$ of :ref{#prop-descending-tree}, for a computable well-ordering $L$ of type $\alpha$, is computable of rank $\alpha$. The ranks are therefore exactly the ordinals below $\omega_1^{\mathrm{CK}}$.
:::

The same argument relativizes: the ranks of the $X$-computable well-founded trees are the ordinals below $\omega_1^X$. The boundedness lesson shows that a $\Sigma^1_1$ set of computable well-founded trees has ranks bounded below $\omega_1^{\mathrm{CK}}$ (:ref{#ex-tree-boundedness}).

## Exercises

::::exercise{difficulty=1}
Let $T$ be the tree of strictly decreasing sequences of numbers (:ref{#ex-trees} (2)). Show that $\mathrm{rk}(T) = \omega$ and that $(T, <_{\mathrm{KB}})$ has type $\omega + 1$.

:::solution
The rank was computed after :ref{#def-tree-rank}. For the ordering, let $k_n$ be the type of $(T_{\langle n \rangle}, <_{\mathrm{KB}})$, the Kleene–Brouwer ordering of the decreasing sequences of numbers below $n$, a finite tree. By the decomposition in the proof of :ref{#thm-kleene-brouwer}, $k_n = k_0 + \cdots + k_{n-1} + 1$, so $k_n = 2^n$ by induction. The ordering of $T$ is the sum of the finite orders of types $k_0, k_1, \dots$, followed by the root: an infinite sum of non-empty finite orders has type $\omega$, so the type is $\omega + 1$.
:::
::::

::::exercise{difficulty=2}
Show that some computable tree has a path but no computable path.

:::solution
Let $T$ be the set of $\sigma \in 2^{<\nat}$ such that $\sigma(e) \neq \Phi_e(e)$ for every $e < |\sigma|$ with $\Phi_e(e)[|\sigma|]\converge$. It is a computable tree, and its paths are the $\{0,1\}$-valued functions $f$ with $f(e) \neq \Phi_e(e)$ whenever $\Phi_e(e)\converge$. It has a path, for instance $f(e) = 1$ if $\Phi_e(e)\converge = 0$ and $f(e) = 0$ otherwise. No path $f$ is computable: if $f = \Phi_e$, then $\Phi_e(e)\converge = f(e)$, a contradiction. This is a diagonal argument; the tree is the tree of :ref{#thm-dnc2-no-computable} in the course on $\Pi^0_1$ classes. So the ill-foundedness of a computable tree need not be witnessed by a computable path. The next lesson shows that well-foundedness of computable trees is not even a $\Sigma^1_1$ property.
:::
::::

## Notes and references

The use of well-founded trees and their ranks goes back to Lusin and Sierpiński in descriptive set theory; the ordering is named after Brouwer, who used well-founded trees in his analysis of bar induction, and Kleene, who used it in the effective theory (1955). Simpson defines the Kleene–Brouwer ordering in Definition V.1.2 and proves that it is a well-ordering exactly for well-founded trees in Lemma V.1.3; Dzhafarov and Mummert do the same in Definition 5.8.7 and Proposition 5.8.8, and compare ranks with the Kleene–Brouwer ordering in Section 12.1 (Lemma 12.1.6). Monin and Patey represent ordinals by trees in the section *Representation of ordinals by trees* of their chapter on transfinite numbers, with ranks and the Kleene–Brouwer ordering, and show there that the ordinals of c.e. well-founded trees are the computable ordinals.

- S. C. Kleene, *Arithmetical predicates and function quantifiers*, Transactions of the American Mathematical Society 79 (1955), 312–340.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section V.1.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.8 and 12.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Transfinite numbers*, section *Representation of ordinals by trees*.
