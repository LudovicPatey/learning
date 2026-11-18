---
title: Well-orderings, comparison maps and ATR₀
summary: Countable well-orderings in second-order arithmetic; the Kleene–Brouwer ordering, and in ACA₀ a tree is well-founded if and only if its Kleene–Brouwer ordering is a well-ordering; arithmetic transfinite induction, uniqueness of hierarchies and of comparison maps; ATR₀ proves that any two countable well-orderings are comparable.
duration: 30
prerequisites: [big-five/atr0-pi11ca0, big-five/aca0-reversals, computable-ordinals/well-founded-trees]
---

The course on the Big Five introduced $\mathsf{ATR}_0$ and surveyed its equivalents without proofs. This course proves the main ones: the comparability of well-orderings, $\Sigma^1_1$ separation, the perfect set theorem and open determinacy. They all rest on a small theory of countable well-orderings that can be developed in $\mathsf{ACA}_0$, and on one construction that needs $\mathsf{ATR}_0$: the comparison map between two well-orderings. This lesson develops both. Its main technique is **arithmetic transfinite induction**, the form of induction along a well-ordering that is available for arithmetic properties.

## Well-orderings and the Kleene–Brouwer ordering

We keep the conventions of the course on the Big Five (:ref{#def-atr0}): a countable linear order is a set $W$ of pairs with field $F_W$, written $\leq_W$; it is a **well-ordering**, $\mathrm{WO}(W)$, if every non-empty subset of $F_W$ has a $\leq_W$-least element. Over $\mathsf{ACA}_0$, this is equivalent to the absence of descending sequences (:ref{#ex-wo-descending}), and we use both forms. For $j \in F_W$, the **initial segment** $W \uh j$ is the restriction of $W$ to $\{ i : i <_W j \}$.

Trees are related to linear orders by an ordering already met in the course on computable ordinals (:ref{#thm-kleene-brouwer}).

:::definition{#def-kb-order}
The **Kleene–Brouwer ordering** of $\nat^{<\nat}$ is defined by $\sigma \leq_{\mathrm{KB}} \tau$ if $\sigma$ extends $\tau$, or $\sigma(i) < \tau(i)$ at the first position $i$ where they differ. For a tree $T$, $\mathrm{KB}(T)$ is its restriction to $T$, a linear order that exists by $\Delta^0_1$ comprehension.
:::

On a finite tree, the Kleene–Brouwer ordering lists the nodes in post-order: the subtrees of the children from left to right, then the node itself. Going down a path of the tree means going down in the ordering.

:::figure[The Kleene–Brouwer ordering of the tree with nodes $\langle\rangle$, $\langle 0 \rangle$, $\langle 1 \rangle$, $\langle 0, 0 \rangle$, $\langle 0, 1 \rangle$, $\langle 1, 0 \rangle$ and $\langle 0, 0, 0 \rangle$. Each node is labeled by its position in the ordering, $1$ for the least. A node comes after its extensions, and after the nodes to its left.]
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="A finite tree with root, nodes 0 and 1, nodes 00, 01 and 10, and node 000. Each node carries its position in the Kleene-Brouwer order: 000 is first, then 00, 01, 0, 10, 1, and the root is last; the order lists the children from left to right before the node itself"><line x1="300" y1="54" x2="190" y2="96" class="muted-stroke" stroke-width="1.3"/><line x1="300" y1="54" x2="420" y2="96" class="muted-stroke" stroke-width="1.3"/><line x1="190" y1="124" x2="130" y2="166" class="muted-stroke" stroke-width="1.3"/><line x1="190" y1="124" x2="250" y2="166" class="muted-stroke" stroke-width="1.3"/><line x1="420" y1="124" x2="420" y2="166" class="muted-stroke" stroke-width="1.3"/><line x1="130" y1="194" x2="130" y2="236" class="muted-stroke" stroke-width="1.3"/><circle cx="300" cy="40" r="14" class="node"/><text x="300" y="45" text-anchor="middle" class="mrm" font-size="13">7</text><text x="320" y="32" class="label">⟨⟩</text><circle cx="190" cy="110" r="14" class="node"/><text x="190" y="115" text-anchor="middle" class="mrm" font-size="13">4</text><text x="210" y="102" class="label">⟨0⟩</text><circle cx="420" cy="110" r="14" class="node"/><text x="420" y="115" text-anchor="middle" class="mrm" font-size="13">6</text><text x="440" y="102" class="label">⟨1⟩</text><circle cx="130" cy="180" r="14" class="node"/><text x="130" y="185" text-anchor="middle" class="mrm" font-size="13">2</text><text x="150" y="172" class="label">⟨0,0⟩</text><circle cx="250" cy="180" r="14" class="node"/><text x="250" y="185" text-anchor="middle" class="mrm" font-size="13">3</text><text x="270" y="172" class="label">⟨0,1⟩</text><circle cx="420" cy="180" r="14" class="node"/><text x="420" y="185" text-anchor="middle" class="mrm" font-size="13">5</text><text x="440" y="172" class="label">⟨1,0⟩</text><circle cx="130" cy="250" r="14" class="node"/><text x="130" y="255" text-anchor="middle" class="mrm" font-size="13">1</text><text x="150" y="242" class="label">⟨0,0,0⟩</text><text x="300" y="284" text-anchor="middle" class="label">numbers: positions in the Kleene–Brouwer order, from the least (1) to the greatest (7)</text></svg>
:::

:::proposition{#prop-kb-aca}
The following is provable in $\mathsf{ACA}_0$. A tree $T \subseteq \nat^{<\nat}$ has no path if and only if $\mathrm{KB}(T)$ is a well-ordering.
:::

:::proof{of=prop-kb-aca}
If $f$ is a path of $T$, then $f \uh (n + 1)$ extends $f \uh n$, so $f \uh (n+1) <_{\mathrm{KB}} f \uh n$, and $n \mapsto f \uh n$ is a descending sequence: $\mathrm{KB}(T)$ is not a well-ordering. This direction holds in $\mathsf{RCA}_0$.

Conversely, let $(\sigma_m)$ be a descending sequence of $\mathrm{KB}(T)$. By arithmetic comprehension, the set $S = \{ \sigma \in T : \exists m\ \sigma \preceq \sigma_m \}$ exists; it is a subtree of $T$, and infinite, since the $\sigma_m$ are pairwise distinct. It is finitely branching. Otherwise some $\sigma \in S$ has $\sigma \langle i \rangle \in S$ for infinitely many $i$; let $m(i)$ be the least $m$ with $\sigma \langle i \rangle \preceq \sigma_m$. For $i < j$ among these, $\sigma_{m(i)}$ and $\sigma_{m(j)}$ first differ at position $|\sigma|$, with values $i < j$, so $\sigma_{m(i)} <_{\mathrm{KB}} \sigma_{m(j)}$, and therefore $m(i) > m(j)$ since the sequence is descending. So $i \mapsto m(i)$ would be strictly decreasing on an infinite set, which is impossible. By König's lemma, which $\mathsf{ACA}_0$ proves (:ref{#thm-konig-aca}), $S$ has a path, which is a path of $T$.
:::

In particular, the formula $\mathrm{WO}$ is as complicated as the property of having no path, which is the typical $\Pi^1_1$ property (:ref{#fact-kleene-normal-form}).

## Arithmetic transfinite induction

:::lemma{#lem-ati}
For every arithmetic formula $\varphi(j)$, possibly with parameters, $\mathsf{ACA}_0$ proves: if $\mathrm{WO}(W)$ and $\varphi(j)$ holds for every $j \in F_W$ such that $\varphi(i)$ holds for all $i <_W j$, then $\varphi(j)$ holds for every $j \in F_W$.
:::

:::proof{of=lem-ati}
By arithmetic comprehension, the set $Y = \{ j \in F_W : \neg \varphi(j) \}$ exists. If it is non-empty, it has a $\leq_W$-least element $j$; then $\varphi(i)$ holds for all $i <_W j$, hence $\varphi(j)$ holds, a contradiction.
:::

The restriction to arithmetic formulas is the point: the set $Y$ must exist. For a $\Pi^1_1$ formula, the same argument would need $\Pi^1_1$ comprehension. The first application is the uniqueness of hierarchies, already used in the course on the Big Five.

:::proposition{#prop-hierarchy-unique}
Let $\theta(n, j, Y)$ be arithmetic. $\mathsf{ACA}_0$ proves: if $\mathrm{WO}(W)$, then there is at most one $\theta$-hierarchy along $W$. Moreover, for $k \in F_W$, any two $\theta$-hierarchies along $W \uh k$ are equal.
:::

:::proof{of=prop-hierarchy-unique}
Let $H$ and $H'$ be $\theta$-hierarchies along $W$. By :ref{#lem-ati}, applied to the arithmetic formula $H^{[j]} = H'^{[j]}$: if the columns agree below $j$, then $H^{[<j]} = H'^{[<j]}$, and $H^{[j]} = \{ n : \theta(n, j, H^{[<j]}) \} = H'^{[j]}$. So all columns agree, and $H = H'$, since neither has elements outside the columns of $F_W$. The same argument applies to $W \uh k$, which is a well-ordering.
:::

## Comparison maps

:::definition{#def-comparison-maps}
Let $V$ and $W$ be countable linear orders. An **embedding** of $V$ into $W$ is a function $f : F_V \to F_W$ such that $i \leq_V j \iff f(i) \leq_W f(j)$. It is an **isomorphism onto an initial segment** if moreover its range is all of $F_W$, or is $\{ x : x <_W k \}$ for some $k \in F_W$. We write $|V| \leq |W|$ if there is such an isomorphism, $|V| = |W|$ if there is one onto $F_W$, and $|V| < |W|$ if there is one onto a proper initial segment. $V$ and $W$ are **comparable** if $|V| \leq |W|$ or $|W| \leq |V|$.
:::

All these notions are arithmetic in $V$, $W$ and the function. An isomorphism onto an initial segment is the formal version of a comparison of order types: for well-orderings, $|V|$ is the ordinal of $V$, and $|V| \leq |W|$ says that the first is at most the second.

:::lemma{#lem-comparison-unique}
The following is provable in $\mathsf{RCA}_0$. If $\mathrm{WO}(V)$, then any two isomorphisms of $V$ onto initial segments of $W$ are equal.
:::

:::proof{of=lem-comparison-unique}
Let $f$ be such an isomorphism and $m \in F_V$. Every $y <_W f(m)$ is in the range of $f$, which is an initial segment, so $y = f(i)$ for some $i$, and $i <_V m$. Hence $f(m)$ is the $\leq_W$-least element of $F_W$ outside $\{ f(i) : i <_V m \}$: it is determined by the values of $f$ below $m$. Let $g$ be another isomorphism, and $Z = \{ m \in F_V : f(m) \neq g(m) \}$, which exists by $\Delta^0_1$ comprehension. If $Z$ were non-empty, its least element $m$ would satisfy $f(i) = g(i)$ for all $i <_V m$, hence $f(m) = g(m)$: a contradiction.
:::

:::theorem{#thm-atr-comparability}
$\mathsf{ATR}_0$ proves that any two countable well-orderings are comparable.
:::

**Intuition.** Map the elements of $V$ one after the other, in the order of $V$, to the least element of $W$ not yet used. This is a transfinite recursion along $V$, with an arithmetic step. Either the recursion runs through all of $V$, and $V$ is mapped onto an initial segment of $W$, or $W$ is exhausted at some point $j$, and then $V \uh j$ is mapped onto $W$.

:::proof{of=thm-atr-comparability}
We argue in $\mathsf{ATR}_0$. Let $V$ and $W$ be well-orderings. Let $\theta(x, j, Y)$ say: $x \in F_W$, and $x$ is the $\leq_W$-least element of $F_W$ that is not in any column $Y^{[i]}$. By arithmetic transfinite recursion, let $H$ be a $\theta$-hierarchy along $V$. Each column $H^{[j]}$ has at most one element; let $D$ be the set of $j \in F_V$ with $H^{[j]} \neq \emptyset$, let $f(j)$ be the element of $H^{[j]}$ for $j \in D$, and let $R_j = \{ f(i) : i \in D, i <_V j \}$. Then $H^{[j]}$ consists of the least element of $F_W \setminus R_j$, if this set is non-empty, and is empty otherwise; $D$, $f$ and the sets $R_j$ exist by arithmetic comprehension.

1. *Each $R_j$ is an initial segment of $W$.* Let $f(i) \in R_j$ and $y <_W f(i)$. Since $f(i)$ is the least element outside $R_i$, $y \in R_i \subseteq R_j$.
2. *$f$ is an embedding.* Let $i <_V i'$ in $D$. Then $f(i) \in R_{i'}$ and $f(i') \notin R_{i'}$, and $R_{i'}$ is an initial segment by 1, so $f(i) <_W f(i')$.
3. *$D$ is an initial segment of $V$.* If $j \notin D$, then $R_j = F_W$, and $R_{j'} \supseteq R_j$ for $j' >_V j$, so $j' \notin D$.

The range of $f$ is the union of the sets $R_j$ and the values $f(j)$, an initial segment of $W$ by 1. If $D = F_V$, $f$ is an isomorphism of $V$ onto an initial segment of $W$, and $|V| \leq |W|$. Otherwise, let $j$ be the $\leq_V$-least element of $F_V \setminus D$. By 3, $D = \{ i : i <_V j \}$, and $R_j = F_W$: $f$ is an isomorphism of $V \uh j$ onto $W$, and its inverse is an isomorphism of $W$ onto the initial segment $V \uh j$ of $V$. So $|W| \leq |V|$.
:::

:::quiz[the comparison of two well-orderings]
In the proof of :ref{#thm-atr-comparability}, where is arithmetic transfinite recursion needed, rather than arithmetic comprehension?

- [x] To build the whole family of columns at once: the value at $j$ depends on all values below $j$, and along a well-ordering of type beyond $\omega$ this cannot be done by finitely many applications of arithmetic comprehension.
- [ ] To show that $f$ is an embedding.

  This is a direct argument from the definition of the columns, once the hierarchy exists.
- [ ] To find the least element of $F_V \setminus D$.

  The set exists by arithmetic comprehension, and has a least element since $V$ is a well-ordering.

---

Where is the well-foundedness of $W$ used?

- [x] In the step: the least element of $F_W \setminus R_j$ must exist whenever this set is non-empty, otherwise the recursion would stop without exhausting $W$.
- [ ] Nowhere: only $V$ needs to be a well-ordering.

  If $W$ is not a well-ordering, the set of unused elements may have no least element, and the map stops early, without $R_j = F_W$.
- [ ] To show that $D$ is an initial segment.

  This uses only the definition of $R_j$.
:::

So in $\mathsf{ATR}_0$, the **countable ordinals**, the well-orderings up to isomorphism, are linearly ordered by $\leq$. By :ref{#ex-wo-not-initial}, exactly one of $|V| < |W|$, $|V| = |W|$, $|W| < |V|$ holds, and the comparison map is unique by :ref{#lem-comparison-unique}. In the lesson on comparability, we prove the converse of :ref{#thm-atr-comparability}: the comparability of well-orderings implies arithmetic transfinite recursion, so $\mathsf{ATR}_0$ is the weakest system in which the ordinals form a linear order.

::::exercise{#ex-wo-not-initial difficulty=2 objective="Prove by arithmetic transfinite induction that a well-ordering is not isomorphic to a proper initial segment of itself, and deduce the trichotomy of comparisons."}
1. Show in $\mathsf{ACA}_0$: if $\mathrm{WO}(W)$ and $h$ is an embedding of $W$ into itself, then $m \leq_W h(m)$ for every $m \in F_W$. Deduce that $W$ is not isomorphic to $W \uh k$ for any $k \in F_W$.
2. Deduce in $\mathsf{ATR}_0$ that for well-orderings $V$ and $W$, exactly one of $|V| < |W|$, $|V| = |W|$ and $|W| < |V|$ holds.

:::solution
1. Apply :ref{#lem-ati} to the arithmetic formula $m \leq_W h(m)$. Suppose that $i \leq_W h(i)$ for all $i <_W m$, and that $h(m) <_W m$. Then $i = h(m)$ satisfies $h(m) \leq_W h(h(m))$; but $h$ is an embedding and $h(m) <_W m$, so $h(h(m)) <_W h(m)$, a contradiction. So $m \leq_W h(m)$ for all $m$. If $h$ were an isomorphism of $W$ onto $W \uh k$, then $h(k) <_W k$, since $h(k)$ is in the range, contradicting $k \leq_W h(k)$.
2. By :ref{#thm-atr-comparability}, at least one of $|V| \leq |W|$ and $|W| \leq |V|$ holds, so one of the three cases occurs. If two occurred, composing the isomorphisms would give an isomorphism of $V$ or $W$ onto a proper initial segment of itself: for instance, $f : V \to W \uh k$ and $g : W \to V$ onto $F_V$ give $f \circ g : W \to W \uh k$, an isomorphism onto a proper initial segment, which part 1 excludes. The other combinations are similar: the composition of an isomorphism onto an initial segment with an isomorphism onto a proper initial segment is an isomorphism onto a proper initial segment.
:::
::::

## Notes and references

The development follows Simpson, Sections V.1 and V.2: :ref{#prop-kb-aca} is his Lemma V.1.3, :ref{#lem-ati} Lemma V.2.1, :ref{#prop-hierarchy-unique} Lemma V.2.3, :ref{#lem-comparison-unique} Lemma V.2.8, and :ref{#thm-atr-comparability} Lemma V.2.9, whose proof is given here in detail through the least unused element. Dzhafarov and Mummert, Section 12.1, prove the same comparison by a recursion along $V$ that separates successor and limit stages. $\mathsf{ATR}_0$ was introduced by Friedman (1975, 1976) and by Steel in his thesis (1976).

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.1–V.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.8 and 12.1.
- J. R. Steel, *Determinateness and Subsystems of Analysis*, PhD thesis, University of California, Berkeley, 1976.

:::::exercises
::::exercise{#ex-kb-binary difficulty=1 objective="Compute Kleene–Brouwer orderings on small trees, and see that the ordering of a tree with a path has no least element."}
1. List the strings of length at most $2$ over $\{ 0, 1 \}$ in the Kleene–Brouwer ordering.
2. Show that $\mathrm{KB}(\bstr)$ has no least element, and give a descending sequence.

:::solution
1. In post-order: $\langle 0, 0 \rangle <_{\mathrm{KB}} \langle 0, 1 \rangle <_{\mathrm{KB}} \langle 0 \rangle <_{\mathrm{KB}} \langle 1, 0 \rangle <_{\mathrm{KB}} \langle 1, 1 \rangle <_{\mathrm{KB}} \langle 1 \rangle <_{\mathrm{KB}} \langle\rangle$.
2. Every $\sigma \in \bstr$ has the extension $\sigma \langle 0 \rangle <_{\mathrm{KB}} \sigma$, so there is no least element. The sequence $\langle\rangle, \langle 0 \rangle, \langle 0, 0 \rangle, \ldots$ is descending; it is the image of the path $0, 0, 0, \ldots$, as in the proof of :ref{#prop-kb-aca}.
:::
::::

::::exercise{#ex-comparison-examples difficulty=1 objective="Check the definition of comparison maps on the orders ω + 1 and 1 + ω."}
Let $V$ be $\omega + 1$, coded by $\nat$ with $0$ moved to the end ($0$ above all other numbers, which are in their usual order), and $W$ be $1 + \omega$, coded by $\nat$ in its usual order with an extra first element. Give the comparison map between $V$ and $W$, and say which of $|V| < |W|$, $|V| = |W|$, $|W| < |V|$ holds.

:::solution
$W$ has type $\omega$: its elements are a first element followed by an $\omega$-sequence, and each has finitely many predecessors. Map the $n$-th element of $W$ (counting from $0$) to $n + 1 \in F_V$. This is an isomorphism of $W$ onto the initial segment $V \uh 0 = \{ 1, 2, \ldots \}$ of $V$, which is proper. So $|W| < |V|$: $1 + \omega = \omega < \omega + 1$. By :ref{#lem-comparison-unique}, this is the only comparison map.
:::
::::

::::exercise{#ex-sum-comparison difficulty=1 objective="Check which operations on well-orderings preserve comparisons, and see the failure on one side."}
Using the sum $V + W$ of :ref{#ex-wo-sum}, show in $\mathsf{RCA}_0$: if $|V| \leq |W|$, then $|U + V| \leq |U + W|$ for every linear order $U$. Give well-orderings with $|V| < |W|$ and $|V + U| = |W + U|$.

:::solution
Let $f$ be an isomorphism of $V$ onto an initial segment of $W$. Define $g(2i) = 2i$ for $i \in F_U$ and $g(2j + 1) = 2 f(j) + 1$ for $j \in F_V$. It is an embedding, since it is the identity on the $U$-part, sends the $V$-part into the $W$-part, and preserves the order inside it. Its range is $U$ followed by the range of $f$, an initial segment of $U + W$. So $|U + V| \leq |U + W|$.

For the second part, take $V = 1$ (one element), $W = 2$ and $U = \omega$: then $1 + \omega$ and $2 + \omega$ both have type $\omega$, while $1 < 2$.
:::
::::
:::::
