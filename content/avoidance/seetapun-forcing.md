---
title: Seetapun's theorem by a disjunctive forcing question
summary: A direct proof of Seetapun's theorem by forcing with two homogeneous sets and a question about all partitions of the reservoir.
duration: 45
prerequisites: [disjunctive-question, big-five/wkl0]
---

The proof of :ref{#thm-seetapun} goes through the decomposition of a coloring of pairs into a cohesive set and an instance of the pigeonhole principle. This lesson proves Seetapun's theorem directly, with a disjunctive notion of forcing (:ref{#def-disjunctive-notion}) that builds one homogeneous set of each color, and a disjunctive forcing question about all partitions of the reservoir. The argument is close to Seetapun's original proof. It shows on a central example how a notion of forcing for a Ramsey-type problem is set up: which invariant the conditions maintain, how blocks of elements are added, and how compactness brings the question down to the right complexity.

## A direct proof of Seetapun's theorem

We now build homogeneous sets for a coloring of pairs directly, with one homogeneous set of each color. Fix a set $Z$, a set $C \not\leq_T Z$, and a coloring $f : [\nat]^2 \to 2$ computable in $Z$. For a finite set $F$ and a color $i$, $F$ is **homogeneous for color $i$** if $f(\{ a, b \}) = i$ for all $a \neq b$ in $F$; sets with at most one element are homogeneous for both colors. As in the previous lesson, the sentences are built with functionals of the oracle $Z \oplus G$. As in the course on Ramsey's theorem, a string $\sigma$ is identified with the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$.

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

:::figure[A Seetapun condition, with $\sigma_0 = \{ 1, 4 \}$ homogeneous for color $0$, $\sigma_1 = \{ 2 \}$, and a reservoir $X$ whose elements have color $i$ with every element of $\sigma_i$. In the proof of property 1 of :ref{#lem-seetapun-question}, the elements of $X$ below the bound $\ell$ are split according to their color with the elements of a thinned reservoir $Y$ above $\ell$; the answer to the question then provides a block of new elements, homogeneous of some color $i$, taken among the elements labeled $i$.]
<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="A condition of the Seetapun forcing: two stems, homogeneous for colors 0 and 1, and a reservoir; for a positive answer, the finite part of the reservoir below l is split according to the colors towards a thinned reservoir Y above l"><text x="70.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="112.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="154.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="196.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="238.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="280.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="322.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="364.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="406.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="448.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">18</text><text x="490.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">20</text><text x="532.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">22</text><text x="50" y="52" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">₀</tspan></text><rect x="60" y="38" width="21" height="20" class="cell"/><text x="70.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="81" y="38" width="21" height="20" class="cell head-cell"/><text x="91.5" y="52" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="102" y="38" width="21" height="20" class="cell"/><text x="112.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="123" y="38" width="21" height="20" class="cell"/><text x="133.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="144" y="38" width="21" height="20" class="cell head-cell"/><text x="154.5" y="52" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="165" y="38" width="21" height="20" class="cell"/><text x="175.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><text x="50" y="86" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">₁</tspan></text><rect x="60" y="72" width="21" height="20" class="cell"/><text x="70.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="81" y="72" width="21" height="20" class="cell"/><text x="91.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="102" y="72" width="21" height="20" class="cell head-cell"/><text x="112.5" y="86" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="123" y="72" width="21" height="20" class="cell"/><text x="133.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="144" y="72" width="21" height="20" class="cell"/><text x="154.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="165" y="72" width="21" height="20" class="cell"/><text x="175.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><text x="50" y="120" text-anchor="end" class="math" font-size="14">X</text><circle cx="196.5" cy="116" r="2" class="muted-fill"/><circle cx="217.5" cy="116" r="5" class="accent-fill"/><circle cx="238.5" cy="116" r="5" class="accent-fill"/><circle cx="259.5" cy="116" r="2" class="muted-fill"/><circle cx="280.5" cy="116" r="5" class="accent-fill"/><circle cx="301.5" cy="116" r="5" class="accent-fill"/><circle cx="322.5" cy="116" r="2" class="muted-fill"/><circle cx="343.5" cy="116" r="5" class="accent-fill"/><circle cx="364.5" cy="116" r="2" class="muted-fill"/><circle cx="385.5" cy="116" r="5" class="accent-fill"/><circle cx="406.5" cy="116" r="5" class="accent-fill"/><circle cx="427.5" cy="116" r="2" class="muted-fill"/><circle cx="448.5" cy="116" r="5" class="accent-fill"/><circle cx="469.5" cy="116" r="5" class="accent-fill"/><circle cx="490.5" cy="116" r="2" class="muted-fill"/><circle cx="511.5" cy="116" r="5" class="accent-fill"/><circle cx="532.5" cy="116" r="5" class="accent-fill"/><circle cx="553.5" cy="116" r="2" class="muted-fill"/><text x="570" y="120" class="mrm muted" font-size="13">⋯</text><text x="50" y="180" text-anchor="end" class="label">split</text><circle cx="196.5" cy="176" r="2" class="muted-fill"/><rect x="208" y="166" width="19" height="20" class="cell"/><text x="217.5" y="180" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="229" y="166" width="19" height="20" class="cell"/><text x="238.5" y="180" text-anchor="middle" class="mrm" font-size="11">1</text><circle cx="259.5" cy="176" r="2" class="muted-fill"/><rect x="271" y="166" width="19" height="20" class="cell"/><text x="280.5" y="180" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="292" y="166" width="19" height="20" class="cell"/><text x="301.5" y="180" text-anchor="middle" class="mrm" font-size="11">1</text><circle cx="322.5" cy="176" r="2" class="muted-fill"/><rect x="334" y="166" width="19" height="20" class="cell"/><text x="343.5" y="180" text-anchor="middle" class="mrm" font-size="11">0</text><circle cx="364.5" cy="176" r="2" class="muted-fill"/><circle cx="385.5" cy="176" r="5" class="muted-stroke" fill="none"/><circle cx="406.5" cy="176" r="5" class="accent-fill"/><circle cx="427.5" cy="176" r="2" class="muted-fill"/><circle cx="448.5" cy="176" r="5" class="muted-stroke" fill="none"/><circle cx="469.5" cy="176" r="5" class="accent-fill"/><circle cx="490.5" cy="176" r="2" class="muted-fill"/><circle cx="511.5" cy="176" r="5" class="muted-stroke" fill="none"/><circle cx="532.5" cy="176" r="5" class="accent-fill"/><circle cx="553.5" cy="176" r="2" class="muted-fill"/><text x="570" y="180" class="mrm muted" font-size="13">⋯</text><line x1="354" y1="100" x2="354" y2="196" class="ink-stroke" stroke-width="1.2" stroke-dasharray="4 3"/><text x="358" y="104" class="math" font-size="13">ℓ</text><text x="60" y="222" class="label">σ₀ is homogeneous for color 0, σ₁ for color 1; every y ∈ X has color i with all of σᵢ</text><text x="60" y="242" class="label">split: each a ∈ X below ℓ has the shown color with every y ∈ Y (filled); open circles leave the reservoir</text></svg>
:::

:::lemma{#lem-seetapun-infinity}
Assume (H). For every condition $c = (\sigma_0, \sigma_1, X)$ and every $i < 2$, there is an extension of $c$ whose stem on side $i$ has an element larger than $|\sigma_i|$, the other stem being unchanged.
:::

:::proof{of=lem-seetapun-infinity}
Suppose first that some $x \in X$ has $f(\{ x, y \}) = i$ for infinitely many $y \in X$. Let $\tau_i$ be the string of length $x + 1$ with the elements of $\sigma_i$ and $x$, and $Y = \{ y \in X : y > x,\ f(\{ x, y \}) = i \}$, an infinite set computable in $X \oplus Z$, hence in $\mathcal M$. Then $\tau_i$ is homogeneous for color $i$, since $x \in X$ has color $i$ with the elements of $\sigma_i$; every $y \in Y$ has color $i$ with $x$ by the choice of $Y$, and with the elements of $\sigma_i$ since $y \in X$. Replacing $\sigma_i$ by $\tau_i$ and $X$ by $Y$ gives the extension.

Otherwise, every $x \in X$ has color $1 - i$ with almost every $y \in X$. Define $x_0 = \min X$, and $x_{k+1}$ as the least $y \in X$ larger than $x_k$ such that $f(\{ x_j, y \}) = 1 - i$ for every $j \leq k$; it exists, since each of the finitely many $x_j$ excludes only finitely many $y$. The set $\{ x_k : k \in \nat \}$ is infinite, homogeneous for color $1 - i$, and computable in $X \oplus Z$, so it belongs to $\mathcal M$, contradicting (H).
:::

The forcing question asks for a block of new elements on one side. The block must be homogeneous for the color of its side and taken from the reservoir. To decide whether such a block exists with an answer of low complexity, the question does not ask it for the actual coloring of the reservoir elements towards the future, which is not even defined, but for every possible partition of the reservoir: this is the over-approximation of the previous lesson.

:::lemma{#lem-seetapun-question}
For a condition $c = (\sigma_0, \sigma_1, X)$ and $\Sigma^0_1$ sentences $\varphi_0, \varphi_1$, let $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ hold if for every set $B$, writing $B^0 = B$ and $B^1 = \nat \setminus B$, there are $i < 2$ and a string $\tau$ compatible with $(\sigma_i, X \cap B^i)$, whose new elements form a set homogeneous for color $i$, such that $\tau$ satisfies $\varphi_i$. This is a disjunctive forcing question, and it is $\Sigma^0_1(\mathcal M)$-preserving.
:::

:::proof{of=lem-seetapun-question}
Write $\varphi_i = \Phi^{Z \oplus G}_{a_i}\converge$, and say that $\tau$ **satisfies** $\varphi_i$ if $\Phi^{Z \oplus \tau}_{a_i}\converge$. For a string $\beta$, write $\beta^0 = \{ n < |\beta| : \beta(n) = 1 \}$ and $\beta^1 = \{ n < |\beta| : \beta(n) = 0 \}$. Let $T$ be the set of strings $\beta$ for which there are no $i < 2$ and $\tau$ with $|\tau| \leq |\beta|$, compatible with $(\sigma_i, X \cap \beta^i)$, with new elements homogeneous for color $i$, and $\Phi^{Z \oplus \tau}_{a_i}[|\beta|]\converge$. Compatibility only involves the positions below $|\tau| \leq |\beta|$, so $T$ is a tree, computable in $X \oplus Z$. A set $B$ is a path of $T$ if and only if no witness $(i, \tau)$ exists for $B$, since a witness, with its convergence time $s$, is seen by the prefix of $B$ of length $\max(|\tau|, s)$. So $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ holds if and only if $T$ has no path.

*Preservation.* $T$ has no path if and only if it is finite (:ref{#lem-weak-konig}), if and only if no string of some length $\ell$ belongs to $T$. This is $\Sigma^0_1(X \oplus Z)$, uniformly in the parameters of $\varphi_0$ and $\varphi_1$, and $X \oplus Z \in \mathcal M$.

*Property 2.* Suppose $T$ has a path. Since $T \leq_T X \oplus Z \in \mathcal M$ and $\mathcal M$ is a Scott ideal, $T$ has a path $B \in \mathcal M$. As $X$ is infinite, $X \cap B^i$ is infinite for some $i$; let $Y = X \cap B^i \in \mathcal M$. Then $d = (\sigma_0, \sigma_1, Y)$ is a condition extending $c$. We show that $d \Vdash \neg \varphi_i(G_i)$. Let $G$ be a member of side $i$ of $d$ with $\Phi^{Z \oplus G}_{a_i}\converge$, with use $u$, and let $\tau = G \uh \max(u, |\sigma_i|)$. Then $\tau$ is compatible with $(\sigma_i, Y)$, hence with $(\sigma_i, X \cap B^i)$, its new elements are elements of $G$, hence form a set homogeneous for color $i$, and $\Phi^{Z \oplus \tau}_{a_i}\converge$. This witness for $B$ contradicts $B \in [T]$.

*Property 1.* Suppose $T$ is finite, and let $\ell$ be such that no string of length $\ell$ belongs to $T$; we may take $\ell \geq |\sigma_0|, |\sigma_1|$. Let $F = X \cap [0, \ell)$. Thin out the reservoir: let $Y_0 = X \setminus [0, \ell)$ and, for each element $a$ of $F$ in turn, let $Y_{k+1}$ be the set of $y \in Y_k$ with $f(\{ a, y \}) = 0$ if it is infinite, and the set of $y \in Y_k$ with $f(\{ a, y \}) = 1$ otherwise. The last set $Y$ is infinite, computable in $X \oplus Z$, hence in $\mathcal M$, and each $a \in F$ has a color $\gamma(a)$ with $f(\{ a, y \}) = \gamma(a)$ for all $y \in Y$. Let $\beta$ be the string of length $\ell$ with $\beta(n) = 1$ if $n \in F$ and $\gamma(n) = 0$, and $\beta(n) = 0$ otherwise, so that $X \cap \beta^i = \{ a \in F : \gamma(a) = i \}$. Since $\beta \notin T$, there are $i$ and $\tau$ with $|\tau| \leq \ell$, compatible with $(\sigma_i, X \cap \beta^i)$, with new elements homogeneous for color $i$, and $\Phi^{Z \oplus \tau}_{a_i}\converge$.

Let $d$ be the triple with stem $\tau$ on side $i$, stem $\sigma_{1-i}$ on side $1 - i$, and reservoir $Y$. It is a condition. The reservoir $Y \in \mathcal M$ is infinite with $\min Y \geq \ell \geq |\tau|$. The stem $\tau$ is homogeneous for color $i$: pairs inside $\sigma_i$ and pairs of new elements have color $i$ by hypothesis, and a pair of an element of $\sigma_i$ and a new element, which lies in $X$, has color $i$ by clause 3 for $c$. For $y \in Y$, an element of $\sigma_i$ has color $i$ with $y$ since $y \in X$, and a new element $a$ satisfies $\gamma(a) = i$, so $f(\{ a, y \}) = i$. Side $1 - i$ keeps its properties since $Y \subseteq X$. So $d \leq c$, and every member of side $i$ of $d$ extends $\tau$, hence satisfies $\varphi_i$ by the use principle.
:::

:::theorem[Seetapun]{#thm-seetapun-direct}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$.
:::

:::proof{of=thm-seetapun-direct}
Let $\mathcal M$ be as above; we may assume (H). Start from $c_0 = (\varepsilon, \varepsilon, \nat)$, which is a condition since $\nat \in \mathcal M$. Build $c_0 \geq c_1 \geq \cdots$, handling in turn, infinitely often each, the following tasks: for $i < 2$, extend the stem of side $i$ by :ref{#lem-seetapun-infinity}; for a pair $(e_0, e_1)$, pass to an extension given by :ref{#lem-disjunctive-cone}, which applies by :ref{#lem-seetapun-question} since $C$ is computable in no member of $\mathcal M$. Let $G_i$ be the union of the stems of side $i$.

Each $G_i$ is infinite, by the first task. It is homogeneous for color $i$, since every finite subset is contained in some stem. It is a member of side $i$ of every $c_s$: it extends the stem $\sigma_{s,i}$, and every element beyond $|\sigma_{s,i}|$ was added at a later step from a reservoir contained in the reservoir of $c_s$. By the second task and :ref{#lem-disjunctive-construction}, $C \not\leq_T Z \oplus G_0$ or $C \not\leq_T Z \oplus G_1$. The corresponding $G_i$ is the set $H$.
:::

:::quiz[the Seetapun forcing]
In the proof of property 1 of :ref{#lem-seetapun-question}, why is the reservoir thinned before the string $\beta$ is chosen?

- [x] So that each element of $F$ has a single color with all the remaining reservoir; the partition $\beta$ records these colors, and a block taken from the elements of color $i$ can then be added to the stem of side $i$ without breaking clause 3.
- [ ] To make the reservoir computable.

  The reservoir was already in $\mathcal M$; thinning keeps it there but is not done for this reason.
- [ ] To make the new elements homogeneous for color $i$.

  Homogeneity of the new block is part of the answer to the question, not a consequence of the thinning.

---

Where is it used that $\mathcal M$ is a Scott ideal, and not only a Turing ideal avoiding $C$?

- [x] In property 2, to find a partition $B$ witnessing the negative answer inside $\mathcal M$, so that the new reservoir $X \cap B^i$ stays in $\mathcal M$.
- [ ] In :ref{#lem-seetapun-infinity}.

  The homogeneous set built there is computable in $X \oplus Z$; a Turing ideal suffices.
- [ ] In property 1.

  The thinned reservoir is computable in $X \oplus Z$.

---

Why can the proof not ensure that one fixed side, say side $0$, avoids the cone?

- [x] Because the extensions given by the question act on a side that the construction does not choose; only the disjunction over the two sides is forced, and Lachlan's disjunction recovers one side at the end.
- [ ] Because side $0$ may be finite.

  Under (H), both sides are infinite by :ref{#lem-seetapun-infinity}.
- [ ] Because $C$ may be computable in $G_0$.

  This is exactly what cannot be excluded in advance for a fixed side, and the reason is the one of the first option.
:::

## Comparison with the proof through cohesiveness

The proof of :ref{#thm-seetapun} first makes the coloring stable on a cohesive set, and then applies the pigeonhole principle to the limit set: there, the question about all partitions of the reservoir replaces the unknown limit set. In the direct proof, the coloring has no limit behavior. Its role is taken by the thinning of property 1: a positive answer is witnessed below a finite bound $\ell$, so only the finitely many elements of $F$ need a limit color, and finitely many applications of the pigeonhole principle to computable colorings provide one. Compactness is used twice, in opposite directions: to bring the question down to $\Sigma^0_1(X \oplus Z)$, and, through the Scott ideal, to find in $\mathcal M$ a partition witnessing a negative answer.

The forcing is a variant of Mathias forcing with two stems and a common reservoir, with clauses 2 and 3 added so that the stems stay homogeneous and every reservoir element can be added to either stem. The general method of designing such notions, by identifying the invariant that keeps the stems extendible and the blocks that can be added at once, is the subject of the course on forcing design of the track.

## Exercises

::::exercise{difficulty=2}
Replace, in the proof of :ref{#thm-seetapun-direct}, the condition $X \in \mathcal M$ by $C \not\leq_T X \oplus Z$, and the Scott ideal by the cone avoidance basis theorem. Check each lemma, and identify the class $\mathcal M$ for which the question is $\Sigma^0_1(\mathcal M)$-preserving.

:::solution
Let $\mathcal M = \{ X \oplus Z : C \not\leq_T X \oplus Z \}$. Assumption (H) becomes: no infinite homogeneous set $H$ has $C \not\leq_T H \oplus Z$. In :ref{#lem-seetapun-infinity} and in property 1, the new reservoirs are computable in $X \oplus Z$, so they avoid the cone together with $Z$. Preservation is unchanged: the question is $\Sigma^0_1(X \oplus Z)$. In property 2, the tree $T$ is computable in $X \oplus Z$, and the cone avoidance basis theorem relativized to $X \oplus Z$ (:ref{#thm-cone-avoidance-basis}) gives a path $B$ with $C \not\leq_T X \oplus Z \oplus B$; the reservoir $X \cap B^i$ is computable in $X \oplus B$, so $C \not\leq_T (X \cap B^i) \oplus Z$. This is the setting of Seetapun's original proof, presented by Dzhafarov and Mummert.
:::
::::

::::exercise{difficulty=2}
Suppose that $f$ is stable (:ref{#def-stable-coloring}), with limit set $A_f$. Show that property 1 of :ref{#lem-seetapun-question} can then be proved without thinning the reservoir, by applying the definition of the question to $B = A_f$. Where is stability used?

:::solution
Apply the definition with $B = A_f$: there are $i$ and $\tau$ compatible with $(\sigma_i, X \cap B^i)$, with new elements homogeneous for color $i$, satisfying $\varphi_i$. Each new element $a$ lies in $B^i$, so $\lim_y f(\{ a, y \}) = i$: only finitely many $y$ have $f(\{ a, y \}) \neq i$. Let $Y$ be the set of $y \in X$ with $y \geq |\tau|$ and $f(\{ a, y \}) = i$ for every new element $a$. It is cofinite in $X$, hence infinite, and computable in $X \oplus Z$. The triple with stem $\tau$ on side $i$ and reservoir $Y$ is a condition, by the verification of property 1, and it forces $\varphi_i(G_i)$. Stability is used to know that the limits exist, so that $A_f$ is a partition whose sides describe the color of each element with almost all later ones. For an unstable coloring no such partition exists, and the proof uses instead the bound $\ell$ and the thinning, which give limit colors to the finitely many elements below $\ell$.
:::
::::

## Notes and references

Seetapun's theorem appeared in Seetapun and Slaman (1995). Seetapun's original proof is a forcing argument with two stems homogeneous for the two colors and cone-avoiding reservoirs, presented by Dzhafarov and Mummert (Section 8.3, Definition 8.3.5 and Remark 8.3.6 for the notion of forcing, Lemma 8.3.7 for Lachlan's disjunction); the dichotomy there is formulated with finite blocks and a finitely branching tree rather than with a question about partitions. The formulation with a disjunctive forcing question over all partitions of the reservoir follows an exercise of the chapter *Cone avoidance* of Patey's monograph (section *Seetapun's theorem*), where disjunctive forcing questions are defined. The proof through cohesiveness is due to Dzhafarov and Jockusch (2009), after Cholak, Jockusch and Slaman (2001).

- D. Seetapun and T. A. Slaman, *On the strength of Ramsey's theorem*, Notre Dame Journal of Formal Logic 36 (1995), 570–582.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.3.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Seetapun's theorem*.
