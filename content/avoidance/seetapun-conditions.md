---
title: Seetapun conditions
summary: "The notion of forcing of Seetapun's original proof, with two stems homogeneous for the two colors and a common reservoir from which either stem can be extended; why both stems can always be extended when no homogeneous set lies in the Scott ideal of reservoirs."
duration: 30
prerequisites: [disjunctive-question, big-five/wkl0]
---

The proof of :ref{#thm-seetapun} goes through the decomposition of a coloring of pairs into a cohesive set and an instance of the pigeonhole principle. This lesson and the next prove Seetapun's theorem directly, with a disjunctive notion of forcing (:ref{#def-disjunctive-notion}) that builds one homogeneous set of each color. The argument is close to Seetapun's original proof, and it shows on a central example how a notion of forcing for a Ramsey-type problem is set up. This lesson defines the conditions and explains the **invariant** they maintain: every element of the reservoir can be added to either stem. It then proves that both stems can always be extended. The next lesson defines the disjunctive forcing question, about all partitions of the reservoir, and proves the theorem.

## Seetapun conditions

Fix a set $Z$, a set $C \not\leq_T Z$, and a coloring $f : [\nat]^2 \to 2$ computable in $Z$. For a finite set $F$ and a color $i$, $F$ is **homogeneous for color $i$** if $f(\{ a, b \}) = i$ for all $a \neq b$ in $F$; sets with at most one element are homogeneous for both colors. As in the previous lesson, the sentences are built with functionals of the oracle $Z \oplus G$. As in the course on Ramsey's theorem, a string $\sigma$ is identified with the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$.

Let $\mathcal M$ be a Scott ideal containing $Z$ and not containing $C$ (:ref{#lem-scott-cone}). If some infinite homogeneous set $H$ for $f$ belongs to $\mathcal M$, then $Z \oplus H \in \mathcal M$, so $C \not\leq_T Z \oplus H$, and the theorem holds. We assume from now on:

(H) no infinite homogeneous set for $f$ belongs to $\mathcal M$.

:::definition{#def-seetapun-forcing}
A **Seetapun condition** is a triple $(\sigma_0, \sigma_1, X)$ such that:

1. $X \in \mathcal M$ is infinite, and $\min X \geq |\sigma_0|, |\sigma_1|$;
2. for each $i < 2$, $\sigma_i$ is homogeneous for color $i$;
3. for each $i < 2$, every $a \in \sigma_i$ and every $y \in X$, $f(\{ a, y \}) = i$.

A condition $(\tau_0, \tau_1, Y)$ **extends** $(\sigma_0, \sigma_1, X)$ if $Y \subseteq X$ and, for each $i$, $\tau_i$ is compatible with the Mathias condition $(\sigma_i, X)$: $\sigma_i \preceq \tau_i$ and the new elements of $\tau_i$ belong to $X$. The **members of side $i$** of $(\sigma_0, \sigma_1, X)$ are the sets $G$ that are homogeneous for color $i$, with $\sigma_i \prec G$ and every element of $G$ beyond $|\sigma_i|$ in $X$.
:::

Conditions 2 and 3 say that for every $y \in X$, the set $\sigma_i \cup \{ y \}$ is homogeneous for color $i$: each element of the reservoir can be added to either stem. The class of members of side $i$ is closed, since homogeneity and the other clauses are properties of the finite initial segments of $G$, and it contains $\sigma_i$ itself. If $d \leq c$, the members of side $i$ of $d$ are members of side $i$ of $c$, since the new elements of the stem of $d$ and its reservoir lie in the reservoir of $c$.

:::example{#ex-seetapun-condition}
Let $f(\{ a, b \}) = 1$ if $a$ and $b$ are both even, and $f(\{ a, b \}) = 0$ otherwise. Let $\sigma_0 = \{ 1 \}$, $\sigma_1 = \{ 2 \}$, and let $X$ be the set of even numbers at least $4$, a computable set, hence in $\mathcal M$. Clause 2 holds trivially. For clause 3, $f(\{ 1, y \}) = 0$ and $f(\{ 2, y \}) = 1$ for every even $y$. So $(\sigma_0, \sigma_1, X)$ is a condition.

1. Adding $4$ to the stem of side $1$ gives $\{ 2, 4 \}$, homogeneous for color $1$; with the reservoir $X \setminus \{ 4 \}$, clause 3 still holds, and the result is an extension.
2. Adding $4$ to the stem of side $0$ gives $\{ 1, 4 \}$, homogeneous for color $0$. But $f(\{ 4, y \}) = 1$ for every $y \in X$, so no infinite reservoir inside $X$ satisfies clause 3 for the new stem: the move is not allowed. The same holds for every element of $X$, so side $0$ cannot be extended at all.

Here $X$ itself is an infinite homogeneous set for color $1$ in $\mathcal M$, so this coloring does not satisfy (H), and the theorem holds trivially for it. The next lemma shows that this is the only obstruction.
:::

Without clause 3, the triple $(\{ 1, 4 \}, \{ 2 \}, X)$ of the example would satisfy all the other requirements, and its stem of side $0$ could never be extended by an element of the reservoir. Clause 3 is the invariant that keeps both stems extendible; the price is that each extension of a stem must thin the reservoir to the elements that have the right color with the new elements.

:::lemma{#lem-seetapun-infinity}
Assume (H). For every condition $c = (\sigma_0, \sigma_1, X)$ and every $i < 2$, there is an extension of $c$ whose stem on side $i$ has an element that is not in $\sigma_i$, the other stem being unchanged.
:::

:::proof{of=lem-seetapun-infinity}
Suppose first that some $x \in X$ has $f(\{ x, y \}) = i$ for infinitely many $y \in X$. Let $\tau_i$ be the string of length $x + 1$ with the elements of $\sigma_i$ and $x$, and $Y = \{ y \in X : y > x,\ f(\{ x, y \}) = i \}$, an infinite set computable in $X \oplus Z$, hence in $\mathcal M$. Then $\tau_i$ is homogeneous for color $i$, since $x \in X$ has color $i$ with the elements of $\sigma_i$; every $y \in Y$ has color $i$ with $x$ by the choice of $Y$, and with the elements of $\sigma_i$ since $y \in X$. Replacing $\sigma_i$ by $\tau_i$ and $X$ by $Y$ gives the extension.

Otherwise, every $x \in X$ has color $1 - i$ with almost every $y \in X$. Define $x_0 = \min X$, and $x_{k+1}$ as the least $y \in X$ larger than $x_k$ such that $f(\{ x_j, y \}) = 1 - i$ for every $j \leq k$; it exists, since each of the finitely many $x_j$ excludes only finitely many $y$. The set $\{ x_k : k \in \nat \}$ is infinite, homogeneous for color $1 - i$, and computable in $X \oplus Z$, so it belongs to $\mathcal M$, contradicting (H).
:::

The dichotomy in the proof is the standard one for Ramsey-type constructions: either some element of the reservoir can be added to the stem of side $i$ while keeping infinitely many compatible elements, or the reservoir computes a homogeneous set for the other color. In the second case, the construction would be finished at once, which is why (H) is assumed.

:::quiz[extending the stems]
In the proof of :ref{#lem-seetapun-infinity}, where is assumption (H) used?

- [x] In the second case, where the elements $x_k$ form an infinite homogeneous set for color $1 - i$ computable in $X \oplus Z$, hence in $\mathcal M$; without (H), side $i$ may never be extendable, as in :ref{#ex-seetapun-condition}.
- [ ] In the first case, to show that the new reservoir $Y$ is infinite.

  $Y$ is infinite by the choice of $x$, which has color $i$ with infinitely many $y \in X$; (H) is not used there.
- [ ] In the first case, to show that $\tau_i$ is homogeneous for color $i$.

  Homogeneity of $\tau_i$ follows from clause 3 for $c$, since $x \in X$ has color $i$ with every element of $\sigma_i$.
:::

## Exercises

::::exercise{difficulty=1}
Assume (H), and let $(\sigma_0, \sigma_1, X)$ be a condition and $i < 2$. Show that infinitely many $x \in X$ have color $i$ with infinitely many $y \in X$.

:::solution
Otherwise, let $X'$ be $X$ without the finitely many such $x$. It is infinite and computable in $X$, hence in $\mathcal M$. Every $x \in X'$ has color $1 - i$ with almost every $y \in X$, hence with almost every $y \in X'$. The construction of the second case of :ref{#lem-seetapun-infinity}, applied to $X'$, gives an infinite homogeneous set for color $1 - i$ computable in $X' \oplus Z$, which belongs to $\mathcal M$ and contradicts (H).
:::
::::

## Notes and references

Seetapun's theorem appeared in Seetapun and Slaman (1995). The notion of forcing with two stems homogeneous for the two colors and a common reservoir is that of Seetapun's original proof, presented by Dzhafarov and Mummert (Section 8.3: 2-fold Mathias forcing is their Definition 8.3.5, the homogeneity clauses are their Remark 8.3.6, and the argument of :ref{#lem-seetapun-infinity} is the beginning of their proof of Theorem 8.3.1, with cone-avoiding reservoirs). The version with reservoirs in a Scott ideal follows an exercise of the chapter *Cone avoidance* of Patey's monograph (section *Seetapun's theorem*).

- D. Seetapun and T. A. Slaman, *On the strength of Ramsey's theorem*, Notre Dame Journal of Formal Logic 36 (1995), 570–582.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.3.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Seetapun's theorem*.
