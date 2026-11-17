---
title: Seetapun's theorem by a disjunctive forcing question
summary: The disjunctive forcing question of the Seetapun forcing, about all partitions of the reservoir, and the direct proof of Seetapun's theorem; comparison with the proof through cohesiveness.
duration: 35
prerequisites: [seetapun-conditions]
---

The previous lesson defined the Seetapun conditions (:ref{#def-seetapun-forcing}) and showed that both stems can always be extended (:ref{#lem-seetapun-infinity}). This lesson defines the disjunctive forcing question and proves Seetapun's theorem. The question asks for a block of new elements on one side, and it has two difficulties: the block must keep the invariant of the conditions, which depends on the colors of its elements towards the rest of the reservoir, and the answer must be $\Sigma^0_1$ relative to the reservoir. Both are handled by quantifying over all partitions of the reservoir: compactness brings the answer down to $\Sigma^0_1$, and a thinning of the reservoir restores the invariant.

As in the previous lesson, $Z$ is a set, $C \not\leq_T Z$, $f : [\nat]^2 \to 2$ is a coloring computable in $Z$, $\mathcal M$ is a Scott ideal containing $Z$ and not containing $C$, and we assume (H): no infinite homogeneous set for $f$ belongs to $\mathcal M$. A string is identified with the finite set of the positions where it takes the value $1$, and sentences are built with functionals of the oracle $Z \oplus G$.

## The question

The block asked for must be homogeneous for the color of its side and taken from the reservoir. To decide whether such a block exists with an answer of low complexity, the question does not ask it for the limit colors of the reservoir elements, which are not defined when $f$ is not stable, but for every possible partition of the reservoir into two sides: this is the over-approximation of :ref{to="avoidance/forcing-question-method"}, in the form of the Dzhafarov–Jockusch question (:ref{to="avoidance/disjunctive-question"}), with the homogeneity of the block added.

:::figure[A Seetapun condition, with $\sigma_0 = \{ 1, 4 \}$ homogeneous for color $0$, $\sigma_1 = \{ 2 \}$, and a reservoir $X$ whose elements have color $i$ with every element of $\sigma_i$. In the proof of property 1 of :ref{#lem-seetapun-question}, the elements of $X$ below the bound $\ell$ are split according to their color with the elements of a thinned reservoir $Y$ above $\ell$; the answer to the question then provides a block of new elements, homogeneous of some color $i$, taken among the elements labeled $i$.]
<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="A condition of the Seetapun forcing: two stems, homogeneous for colors 0 and 1, and a reservoir; for a positive answer, the finite part of the reservoir below l is split according to the colors towards a thinned reservoir Y above l"><text x="70.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="112.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="154.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="196.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="238.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="280.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="322.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="364.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="406.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="448.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">18</text><text x="490.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">20</text><text x="532.5" y="18" text-anchor="middle" class="mrm muted" font-size="10">22</text><text x="50" y="52" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">₀</tspan></text><rect x="60" y="38" width="21" height="20" class="cell"/><text x="70.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="81" y="38" width="21" height="20" class="cell head-cell"/><text x="91.5" y="52" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="102" y="38" width="21" height="20" class="cell"/><text x="112.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="123" y="38" width="21" height="20" class="cell"/><text x="133.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="144" y="38" width="21" height="20" class="cell head-cell"/><text x="154.5" y="52" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="165" y="38" width="21" height="20" class="cell"/><text x="175.5" y="52" text-anchor="middle" class="mrm" font-size="11">0</text><text x="50" y="86" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">₁</tspan></text><rect x="60" y="72" width="21" height="20" class="cell"/><text x="70.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="81" y="72" width="21" height="20" class="cell"/><text x="91.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="102" y="72" width="21" height="20" class="cell head-cell"/><text x="112.5" y="86" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="123" y="72" width="21" height="20" class="cell"/><text x="133.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="144" y="72" width="21" height="20" class="cell"/><text x="154.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="165" y="72" width="21" height="20" class="cell"/><text x="175.5" y="86" text-anchor="middle" class="mrm" font-size="11">0</text><text x="50" y="120" text-anchor="end" class="math" font-size="14">X</text><circle cx="196.5" cy="116" r="2" class="muted-fill"/><circle cx="217.5" cy="116" r="5" class="accent-fill"/><circle cx="238.5" cy="116" r="5" class="accent-fill"/><circle cx="259.5" cy="116" r="2" class="muted-fill"/><circle cx="280.5" cy="116" r="5" class="accent-fill"/><circle cx="301.5" cy="116" r="5" class="accent-fill"/><circle cx="322.5" cy="116" r="2" class="muted-fill"/><circle cx="343.5" cy="116" r="5" class="accent-fill"/><circle cx="364.5" cy="116" r="2" class="muted-fill"/><circle cx="385.5" cy="116" r="5" class="accent-fill"/><circle cx="406.5" cy="116" r="5" class="accent-fill"/><circle cx="427.5" cy="116" r="2" class="muted-fill"/><circle cx="448.5" cy="116" r="5" class="accent-fill"/><circle cx="469.5" cy="116" r="5" class="accent-fill"/><circle cx="490.5" cy="116" r="2" class="muted-fill"/><circle cx="511.5" cy="116" r="5" class="accent-fill"/><circle cx="532.5" cy="116" r="5" class="accent-fill"/><circle cx="553.5" cy="116" r="2" class="muted-fill"/><text x="570" y="120" class="mrm muted" font-size="13">⋯</text><text x="50" y="180" text-anchor="end" class="label">split</text><circle cx="196.5" cy="176" r="2" class="muted-fill"/><rect x="208" y="166" width="19" height="20" class="cell"/><text x="217.5" y="180" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="229" y="166" width="19" height="20" class="cell"/><text x="238.5" y="180" text-anchor="middle" class="mrm" font-size="11">1</text><circle cx="259.5" cy="176" r="2" class="muted-fill"/><rect x="271" y="166" width="19" height="20" class="cell"/><text x="280.5" y="180" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="292" y="166" width="19" height="20" class="cell"/><text x="301.5" y="180" text-anchor="middle" class="mrm" font-size="11">1</text><circle cx="322.5" cy="176" r="2" class="muted-fill"/><rect x="334" y="166" width="19" height="20" class="cell"/><text x="343.5" y="180" text-anchor="middle" class="mrm" font-size="11">0</text><circle cx="364.5" cy="176" r="2" class="muted-fill"/><circle cx="385.5" cy="176" r="5" class="muted-stroke" fill="none"/><circle cx="406.5" cy="176" r="5" class="accent-fill"/><circle cx="427.5" cy="176" r="2" class="muted-fill"/><circle cx="448.5" cy="176" r="5" class="muted-stroke" fill="none"/><circle cx="469.5" cy="176" r="5" class="accent-fill"/><circle cx="490.5" cy="176" r="2" class="muted-fill"/><circle cx="511.5" cy="176" r="5" class="muted-stroke" fill="none"/><circle cx="532.5" cy="176" r="5" class="accent-fill"/><circle cx="553.5" cy="176" r="2" class="muted-fill"/><text x="570" y="180" class="mrm muted" font-size="13">⋯</text><line x1="354" y1="100" x2="354" y2="196" class="ink-stroke" stroke-width="1.2" stroke-dasharray="4 3"/><text x="358" y="104" class="math" font-size="13">ℓ</text><text x="60" y="222" class="label">σ₀ is homogeneous for color 0, σ₁ for color 1; every y ∈ X has color i with all of σᵢ</text><text x="60" y="242" class="label">split: each a ∈ X below ℓ has the shown color with every y ∈ Y (filled); open circles leave the reservoir</text></svg>
:::

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
:::

## The theorem

:::theorem[Seetapun]{#thm-seetapun-direct}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$.
:::

:::proof{of=thm-seetapun-direct}
Let $\mathcal M$ be as above. If some infinite homogeneous set for $f$ belongs to $\mathcal M$, it is the set $H$; so we may assume (H). Start from $c_0 = (\varepsilon, \varepsilon, \nat)$, which is a condition since $\nat \in \mathcal M$. Build $c_0 \geq c_1 \geq \cdots$, handling in turn, infinitely often each, the following tasks: for $i < 2$, extend the stem of side $i$ by :ref{#lem-seetapun-infinity}; for a pair $(e_0, e_1)$, pass to an extension given by :ref{#lem-disjunctive-cone}, which applies by :ref{#lem-seetapun-question} since $C$ is computable in no member of $\mathcal M$. Let $G_i$ be the union of the stems of side $i$.

Each $G_i$ is infinite, by the first task. It is homogeneous for color $i$, since every finite subset is contained in some stem. It is a member of side $i$ of every $c_s$: it extends the stem $\sigma_{s,i}$, and every element beyond $|\sigma_{s,i}|$ was added at a later step from a reservoir contained in the reservoir of $c_s$. By the second task and :ref{#lem-disjunctive-construction}, $C \not\leq_T Z \oplus G_0$ or $C \not\leq_T Z \oplus G_1$. The corresponding $G_i$ is the set $H$.
:::

:::quiz[the direct proof of Seetapun's theorem]
Why can the proof not ensure that one fixed side, say side $0$, avoids the cone?

- [x] Because the extensions given by the question act on a side that the construction does not choose; only the disjunction over the two sides is forced, and Lachlan's disjunction recovers one side at the end.
- [ ] Because side $0$ may be finite.

  Under (H), both sides are infinite by :ref{#lem-seetapun-infinity}.
- [ ] Because the members of side $0$ do not form a closed class.

  They do: homogeneity and the other clauses are properties of the finite initial segments of a set, so the definition of a disjunctive notion of forcing applies.
:::

## Comparison with the proof through cohesiveness

The proof of :ref{#thm-seetapun} first makes the coloring stable on a cohesive set, and then applies the pigeonhole principle to the limit set: there, the question about all partitions of the reservoir replaces the unknown limit set. In the direct proof, the coloring has no limit behavior. Its role is taken by the thinning of property 1: a positive answer is witnessed below a finite bound $\ell$, so only the finitely many elements of $F$ need a limit color, and finitely many applications of the pigeonhole principle to computable colorings provide one. Compactness is used twice, in opposite directions: to bring the question down to $\Sigma^0_1(X \oplus Z)$, and, through the Scott ideal, to find in $\mathcal M$ a partition witnessing a negative answer.

The general method of designing notions of forcing for Ramsey-type problems, by identifying the invariant that keeps the stems extendible (clause 3 here) and the blocks that can be added at once, is the subject of the course on forcing design of the track.

## Exercises

::::exercise{#ex-seetapun-cone-reservoirs difficulty=2 objective="Replace the Scott ideal by the cone avoidance basis theorem, and recover the setting of Seetapun's original proof."}
Replace, in the proof of :ref{#thm-seetapun-direct}, the condition $X \in \mathcal M$ by $C \not\leq_T X \oplus Z$, and the Scott ideal by the cone avoidance basis theorem. Check each lemma, and identify the class $\mathcal M$ for which the question is $\Sigma^0_1(\mathcal M)$-preserving.

:::solution
Let $\mathcal M = \{ X \oplus Z : C \not\leq_T X \oplus Z \}$. Assumption (H) becomes: no infinite homogeneous set $H$ has $C \not\leq_T H \oplus Z$. In :ref{#lem-seetapun-infinity} and in property 1, the new reservoirs are computable in $X \oplus Z$, so they avoid the cone together with $Z$. Preservation is unchanged: the question is $\Sigma^0_1(X \oplus Z)$. In property 2, the tree $T$ is computable in $X \oplus Z$, and the cone avoidance basis theorem relativized to $X \oplus Z$ (:ref{#thm-cone-avoidance-basis}) gives a path $B$ with $C \not\leq_T X \oplus Z \oplus B$; the reservoir $X \cap B^i$ is computable in $X \oplus B$, so $C \not\leq_T (X \cap B^i) \oplus Z$. This is the setting of Seetapun's original proof, presented by Dzhafarov and Mummert.
:::
::::

::::exercise{#ex-seetapun-stable-question difficulty=2 objective="See how stability replaces the thinning step of the Seetapun question by the limit partition."}
Suppose that $f$ is stable (:ref{#def-stable-coloring}), with limit set $A_f$. Show that property 1 of :ref{#lem-seetapun-question} can then be proved without thinning the reservoir, by applying the definition of the question to $B = \overline{A_f}$. Where is stability used?

:::solution
With $B = \overline{A_f}$, the side $B^0 = \overline{A_f}$ is the set of $x$ with $\lim_y f(\{ x, y \}) = 0$, and $B^1 = A_f$ the set of $x$ with limit $1$. Apply the definition with this $B$: there are $i$ and $\tau$ compatible with $(\sigma_i, X \cap B^i)$, with new elements homogeneous for color $i$, satisfying $\varphi_i$. Each new element $a$ lies in $B^i$, so $\lim_y f(\{ a, y \}) = i$: only finitely many $y$ have $f(\{ a, y \}) \neq i$. Let $Y$ be the set of $y \in X$ with $y \geq |\tau|$ and $f(\{ a, y \}) = i$ for every new element $a$. It is cofinite in $X$, hence infinite, and computable in $X \oplus Z$. The triple with stem $\tau$ on side $i$ and reservoir $Y$ is a condition, by the verification of property 1, and it forces $\varphi_i(G_i)$. Stability is used to know that the limits exist, so that $A_f$ is a partition whose sides describe the color of each element with almost all later ones. For an unstable coloring no such partition exists, and the proof uses instead the bound $\ell$ and the thinning, which give limit colors to the finitely many elements below $\ell$.
:::
::::

## Notes and references

The notion of forcing is that of Seetapun's original proof (Seetapun and Slaman, 1995), presented by Dzhafarov and Mummert (Section 8.3), where the dichotomy is formulated with finite blocks and a finitely branching tree rather than with a question about partitions. The formulation with a disjunctive forcing question follows an exercise of the chapter *Cone avoidance* of Patey's monograph (section *Seetapun's theorem*). The proof through cohesiveness is due to Cholak, Jockusch and Slaman (2001), with the simplification of Dzhafarov and Jockusch (2009).

- D. Seetapun and T. A. Slaman, *On the strength of Ramsey's theorem*, Notre Dame Journal of Formal Logic 36 (1995), 570–582.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.3.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Seetapun's theorem*.

:::::exercises
::::exercise[Progress on an uncontrolled side]{#ex-seetapun-infinity-question difficulty=1 objective="See that the disjunctive question gives progress on a side that the construction does not choose, which is why both stems are extended separately."}
For $n \in \nat$, let $\varphi_n$ be the $\Sigma^0_1$ sentence "$G$ has an element at least $n$". Show that $c \mathrel{?{\vdash}} \varphi_n(G_0) \vee \varphi_n(G_1)$ for every Seetapun condition $c$. What does property 1 of :ref{#lem-seetapun-question} give, and why can it not replace :ref{#lem-seetapun-infinity} in the proof of :ref{#thm-seetapun-direct}?

:::solution
Let $c = (\sigma_0, \sigma_1, X)$ and let $B$ be a set. Since $X$ is infinite, for some $i < 2$ the set $X \cap B^i$ has an element $x \geq n$. Let $\tau$ be the string of length $x + 1$ whose elements are those of $\sigma_i$ and $x$. Since $x \geq \min X \geq |\sigma_i|$, $\tau$ extends $\sigma_i$, and its only new element $x$ lies in $X \cap B^i$; a set with one element is homogeneous for color $i$; and $\tau$ satisfies $\varphi_n$. So every $B$ has a witness, and the answer is positive.

Property 1 then gives an extension of $c$ whose stem on some side $i$ contains an element at least $n$; its proof does not use (H). But the side is not chosen: a construction using only these extensions might always extend the same side, and leave the other stem finite. Lachlan's disjunction (:ref{#lem-disjunctive-construction}) may then select the finite side, which avoids the cone trivially and is not a solution. :ref{#lem-seetapun-infinity} extends a prescribed side, and this is where (H) is needed.
:::
::::

::::exercise[A one-sided question]{#ex-seetapun-single-side-question difficulty=2 objective="See why a one-sided question for the Seetapun forcing is not a forcing question: a homogeneous block may exist without being extendible."}
For a Seetapun condition $c = (\sigma_0, \sigma_1, X)$, a side $i < 2$ and a $\Sigma^0_1$ sentence $\varphi$, let $c \mathrel{?{\vdash}_i} \varphi$ if some string $\tau$ compatible with $(\sigma_i, X)$, whose new elements form a set homogeneous for color $i$, satisfies $\varphi$. Show that this relation is $\Sigma^0_1(X \oplus Z)$, uniformly in the parameters of $\varphi$, and that if $c \mathrel{?{\nvdash}_i} \varphi$ then $c \Vdash \neg \varphi(G_i)$. With the coloring and the condition of :ref{#ex-seetapun-condition}, and $\varphi$ the sentence "$G$ has an element at least $4$", show that $c \mathrel{?{\vdash}_0} \varphi$ but that no extension of $c$ forces $\varphi(G_0)$.

:::solution
*Complexity.* The relation searches for a string $\tau$ and a convergent computation; compatibility with $(\sigma_i, X)$ is decidable in $X$, and homogeneity of the finite set of new elements is decidable in $Z$, which computes $f$. So it is $\Sigma^0_1(X \oplus Z)$, uniformly.

*Negative answers.* Suppose that a member $G$ of side $i$ of $c$ satisfies $\varphi$, with use $u$. Then $\tau = G \uh \max(u, |\sigma_i|)$ is compatible with $(\sigma_i, X)$, its new elements are elements of $G$, hence homogeneous for color $i$, and $\tau$ satisfies $\varphi$, so $c \mathrel{?{\vdash}_i} \varphi$. Contrapositively, a negative answer means that $c$ forces $\neg \varphi(G_i)$.

*Positive answers.* In :ref{#ex-seetapun-condition}, $\sigma_0 = \{ 1 \}$, $\sigma_1 = \{ 2 \}$ and $X$ is the set of even numbers at least $4$. The string $\tau$ of length $5$ with elements $1$ and $4$ is compatible with $(\sigma_0, X)$, its only new element $4$ forms a homogeneous set, and $\tau$ satisfies $\varphi$; so $c \mathrel{?{\vdash}_0} \varphi$. Let $d = (\tau_0, \tau_1, Y)$ be an extension of $c$ forcing $\varphi(G_0)$. Its stem $\tau_0$ is itself a member of side $0$ of $d$, so it has an element at least $4$, which is a new element, hence an even number $a \in X$. By clause 3 for $d$, $f(\{ a, y \}) = 0$ for every $y \in Y$; but $Y \subseteq X$ consists of even numbers, so $f(\{ a, y \}) = 1$. This contradicts the fact that $Y$ is non-empty. So property 1 of a forcing question fails.

A block that is homogeneous for color $i$ may have color $1 - i$ with almost every element of the reservoir. The disjunctive question of :ref{#lem-seetapun-question} avoids this by the thinning step, which gives each element below $\ell$ a color with the remaining reservoir, and by asking for a block on the side matching that color.
:::
::::

::::exercise[Where the coloring must be computable]{#ex-seetapun-uses-computability difficulty=1 objective="Locate the uses of the computability of the coloring in the direct proof of Seetapun's theorem, and see why they cannot be removed."}
List the steps of the proofs of :ref{#lem-seetapun-infinity}, :ref{#lem-seetapun-question} and :ref{#thm-seetapun-direct} that use the hypothesis that $f$ is computable in $Z$. Explain why the proof does not apply to the coloring $h$ of the proof of :ref{#prop-rt32-jump}, which is computable in $\emptyset'$, with $C = \emptyset'$.

:::solution
The hypothesis is used each time a set must belong to $\mathcal M$ or a relation must have low complexity:

1. in :ref{#lem-seetapun-infinity}, the new reservoir $Y$ of the first case and the homogeneous set of the second case are computable in $X \oplus Z$, which needs $f \leq_T Z$; the second case uses this for (H);
2. in :ref{#lem-seetapun-question}, the tree $T$ is computable in $X \oplus Z$, since the homogeneity of the blocks is decided with $f$; this gives the preservation and, through the Scott ideal, a path in $\mathcal M$;
3. in property 1, the thinned reservoir is computable in $X \oplus Z$;
4. in :ref{#thm-seetapun-direct}, (H) is applied to the homogeneous sets just mentioned.

For a coloring $f$ that is not computable in $Z$, one could replace $Z$ by $Z \oplus f$, but the hypothesis $C \not\leq_T Z \oplus f$ must then hold. For $h$, every set computing $h$ computes the function $m$ of the proof of :ref{#prop-rt32-jump}, hence $\emptyset'$; so no Scott ideal contains $h$ and avoids $\emptyset'$. This is consistent with the fact that every infinite homogeneous set for $h$ computes $\emptyset'$.
:::
::::

::::exercise[Cohesive homogeneous sets]{#ex-seetapun-cohesive difficulty=1 objective="Add a density requirement to the Seetapun forcing so that the homogeneous sets are cohesive." lessons="seetapun-conditions"}
Let $\vec R$ be a sequence of sets with $\bigoplus_n R_n \leq_T Z$. Add a task to the construction of :ref{#thm-seetapun-direct} so that $G_0$ and $G_1$ are $\vec R$-cohesive. Deduce that every $Z$-computable coloring of pairs has an infinite homogeneous set $H$ that is $\vec R$-cohesive and satisfies $C \not\leq_T Z \oplus H$.

:::solution
Given a condition $(\sigma_0, \sigma_1, X)$ and $n$, one of the sets $X \cap R_n$ and $X \setminus R_n$ is infinite; call it $Y$. It is computable in $X \oplus Z$, so $Y \in \mathcal M$. Shrinking the reservoir preserves clauses 1–3, so $(\sigma_0, \sigma_1, Y)$ is a condition extending $(\sigma_0, \sigma_1, X)$. Add the task of passing to such an extension for each $n$. At a later stage, every element of $G_i$ beyond the stem of side $i$ of this condition was added from a reservoir contained in $Y$, so $G_i \subseteq^* R_n$ or $G_i \subseteq^* \overline{R_n}$. With the other tasks, $G_0$ and $G_1$ are infinite, homogeneous and $\vec R$-cohesive, and one of them, $H$, satisfies $C \not\leq_T Z \oplus H$. If (H) fails, some infinite homogeneous set $H$ belongs to $\mathcal M$, so $C \not\leq_T Z \oplus H$, but $H$ need not be cohesive. Let $p$ enumerate $H$ in increasing order and $R'_n = \{ k : p(k) \in R_n \}$, a sequence computable in $Z \oplus H$. By :ref{#thm-coh-cone-avoidance} relative to $Z \oplus H$, there is an $\vec R'$-cohesive set $G'$ with $C \not\leq_T Z \oplus H \oplus G'$; as in :ref{#ex-coh-rt12-combined}, $p[G'] \subseteq H$ is $\vec R$-cohesive, homogeneous, and does not compute $C$ together with $Z$.
:::
::::
:::::
