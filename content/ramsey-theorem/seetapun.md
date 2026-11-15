---
title: Seetapun's theorem
summary: Seetapun's theorem that every computable coloring of pairs has a homogeneous set not computing a given non-computable set; RT²₂ does not imply ACA₀; the separation of cohesiveness and stable Ramsey's theorem; further results on the weakness of Ramsey's theorem for pairs.
duration: 40
prerequisites: [cone-avoidance, triples]
---

By Jockusch's bounds, some computable colorings of pairs have no homogeneous set computable in $\emptyset'$, while some computable coloring of triples forces all its infinite homogeneous sets to compute $\emptyset'$. Seetapun (1995) showed that pairs behave differently: for every non-computable set $C$, every computable coloring of pairs has an infinite homogeneous set that does not compute $C$. In particular, Ramsey's theorem for pairs does not imply $\mathsf{ACA}_0$.

We follow the proof of Dzhafarov and Jockusch (2009), which goes through the decomposition of :ref{#cor-rt22-equivalence}. A computable coloring is first made stable by a cohesive set that avoids the cone above $C$ (:ref{#thm-coh-cone-avoidance}). The restricted coloring is then a stable coloring, computable in the cohesive set, and it remains to find an infinite subset of its limit set or of the complement, which is done by strong cone avoidance for the pigeonhole principle (:ref{#thm-dj-cone-avoidance}). The work was done in the previous lesson; this lesson assembles the pieces, builds the ω-model, and places Ramsey's theorem for pairs among the other principles.

:::figure[The structure of the proof of Seetapun's theorem. Each step preserves the property that $C$ is not computable in the sets built so far.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The proof of Seetapun theorem: a cohesive set makes the coloring stable, the pigeonhole principle on its limit set gives a subset, from which a homogeneous set is computed; each step keeps C out of the cone"><defs><marker id="rt-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="20" y="30" width="340" height="40" rx="6" class="cell"/><text x="190.0" y="55" text-anchor="middle" font-size="13" xml:space="preserve"><tspan class="math">f</tspan><tspan class="mrm">, computable in </tspan><tspan class="math">Z</tspan></text><rect x="20" y="100" width="340" height="40" rx="6" class="cell"/><text x="190.0" y="125" text-anchor="middle" font-size="13" xml:space="preserve"><tspan class="math">G</tspan><tspan class="mrm"> cohesive for (</tspan><tspan class="math">R</tspan><tspan class="math" font-size="9" dy="3">x</tspan><tspan dy="-3">​</tspan><tspan class="mrm">),  </tspan><tspan class="math">C</tspan><tspan class="mrm"> ≰ </tspan><tspan class="math">Z</tspan><tspan class="mrm"> ⊕ </tspan><tspan class="math">G</tspan></text><rect x="20" y="170" width="340" height="40" rx="6" class="cell"/><text x="190.0" y="195" text-anchor="middle" font-size="13" xml:space="preserve"><tspan class="math">K</tspan><tspan class="mrm"> ⊆ </tspan><tspan class="math">A</tspan><tspan class="math" font-size="9" dy="3">g</tspan><tspan dy="-3">​</tspan><tspan class="mrm"> or </tspan><tspan class="math">K</tspan><tspan class="mrm"> ∩ </tspan><tspan class="math">A</tspan><tspan class="math" font-size="9" dy="3">g</tspan><tspan dy="-3">​</tspan><tspan class="mrm"> = ∅,  </tspan><tspan class="math">C</tspan><tspan class="mrm"> ≰ </tspan><tspan class="math">Z</tspan><tspan class="mrm"> ⊕ </tspan><tspan class="math">G</tspan><tspan class="mrm"> ⊕ </tspan><tspan class="math">K</tspan></text><rect x="20" y="240" width="340" height="40" rx="6" class="cell"/><text x="190.0" y="265" text-anchor="middle" font-size="13" xml:space="preserve"><tspan class="math">H</tspan><tspan class="mrm"> homogeneous for </tspan><tspan class="math">f</tspan><tspan class="mrm">,  </tspan><tspan class="math">H</tspan><tspan class="mrm"> ≤</tspan><tspan class="mrm" font-size="9" dy="3">T</tspan><tspan dy="-3">​</tspan><tspan class="mrm"> </tspan><tspan class="math">Z</tspan><tspan class="mrm"> ⊕ </tspan><tspan class="math">G</tspan><tspan class="mrm"> ⊕ </tspan><tspan class="math">K</tspan></text><line x1="190.0" y1="70" x2="190.0" y2="98" class="ink-stroke" stroke-width="1.3" marker-end="url(#rt-arr)"/><text x="202.0" y="89.0" class="label">Mathias forcing: cone avoidance for COH; g = f on pairs of G is stable</text><line x1="190.0" y1="140" x2="190.0" y2="168" class="ink-stroke" stroke-width="1.3" marker-end="url(#rt-arr)"/><text x="202.0" y="159.0" class="label">strong cone avoidance for the pigeonhole principle, on the limit set of g</text><line x1="190.0" y1="210" x2="190.0" y2="238" class="ink-stroke" stroke-width="1.3" marker-end="url(#rt-arr)"/><text x="202.0" y="229.0" class="label">thin out K along the stable coloring g</text></svg>
:::

## Seetapun's theorem

:::theorem[Seetapun]{#thm-seetapun}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$.
:::

:::proof{of=thm-seetapun}
The sequence $R_x = \{ y : f(\{ x, y \}) = 1 \}$ is $Z$-computable. By :ref{#thm-coh-cone-avoidance}, it has a cohesive set $G$ with $C \not\leq_T Z \oplus G$. Let $p$ enumerate $G$ in increasing order, and $g(\{ i, j \}) = f(\{ p(i), p(j) \})$; it is a stable coloring (:ref{#thm-rt22-decomposition}), computable in $Z \oplus G$. By :ref{#thm-dj-cone-avoidance} with $Z \oplus G$ in place of $Z$, applied to the limit set $A_g$, there is an infinite set $K$ contained in $A_g$ or in its complement with $C \not\leq_T Z \oplus G \oplus K$. By :ref{#prop-srt-d22} (2), $g \oplus K$ computes an infinite homogeneous set $L$ for $g$, and $H = p[L]$ is homogeneous for $f$, computable in $Z \oplus G \oplus K$. So $C \not\leq_T Z \oplus H$.
:::

:::quiz[the proof of Seetapun's theorem]
In the proof of :ref{#thm-seetapun}, why is :ref{#thm-dj-cone-avoidance} applied with $Z \oplus G$ in place of $Z$, rather than with $Z$?

- [x] Because the homogeneous set is computed from $K$ together with $g$, which is computable in $Z \oplus G$; the cone must be avoided by $Z \oplus G \oplus K$, not only by $Z \oplus K$.
- [ ] Because the limit set $A_g$ is computable in $Z \oplus G$.

  It is only $\Delta^0_2(Z \oplus G)$; the theorem of Dzhafarov and Jockusch applies to sets of any complexity.
- [ ] Because $C \not\leq_T Z$ does not imply $C \not\leq_T Z \oplus G$.

  For this particular $G$ it does, by the choice of $G$; this is what makes the hypothesis of the theorem available with $Z \oplus G$.
:::

The last step thins $K$ along $g$, which is computable in $Z \oplus G$. This is why the pigeonhole step is applied to the limit set, with the stable coloring kept as a parameter, and not to the stable coloring itself: for stable colorings that are not computable in the sets already built, cone avoidance fails (:ref{#ex-stable-no-cone-avoidance}).

:::corollary[Seetapun]{#cor-rt22-not-aca}
There is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ not containing $\emptyset'$. Consequently $\mathsf{RT}^2_2$ does not imply $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
:::

:::proof{of=cor-rt22-not-aca}
Build sets $Z_0 = \emptyset \leq_T Z_1 \leq_T \cdots$ with $\emptyset' \not\leq_T Z_n$. Fix an enumeration of all pairs $(e, m)$ in which each pair appears infinitely often. At stage $n$, take the next pair $(e, m)$ with $m \leq n$. If $\Phi^{Z_m}_e$ is a coloring of $[\nat]^2$ with two colors, it is $Z_n$-computable, and :ref{#thm-seetapun} gives an infinite homogeneous set $H$ with $\emptyset' \not\leq_T Z_n \oplus H$; let $Z_{n+1} = Z_n \oplus H$. Otherwise $Z_{n+1} = Z_n$.

The class $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$ is a Turing ideal not containing $\emptyset'$. Every coloring in $\mathcal I$ is $\Phi^{Z_m}_e$ for some $e, m$, and is handled at some stage, so it has a homogeneous set in $\mathcal I$. By absoluteness, $\mathcal I$ satisfies $\mathsf{RT}^2_2$, and it is not a jump ideal.
:::

The construction of the ω-model is the standard method for separations in reverse mathematics: a class of sets (here, those not computing $\emptyset'$) that is closed under adding solutions to the instances of the weaker principle, and excludes the stronger one. The course on reducibilities develops it as the **preservation** of a weakness property.

::::exercise{#ex-stable-no-cone-avoidance difficulty=1 objective="See why the pigeonhole step of Seetapun's proof uses the limit set and not the stable coloring." lessons="triples"}
Show that the coloring $h$ in the proof of :ref{#prop-rt32-jump} is stable, and deduce that :ref{#thm-seetapun} fails for stable colorings that are not computable in $Z$: there is a stable coloring of pairs all of whose infinite homogeneous sets compute $\emptyset'$. Why does this not affect the proof of :ref{#thm-seetapun}?

:::solution
For each $x$, $h(\{ x, y \}) = 1$ for all $y > m(x)$, so $h$ is stable with limit set $\nat$. The proof of :ref{#prop-rt32-jump} shows that every infinite homogeneous set for $h$ computes $\emptyset'$. In the proof of :ref{#thm-seetapun}, the stable coloring $g$ is computable in $Z \oplus G$, and the pigeonhole principle is applied to its limit set. For $h$, the limit set $\nat$ is its own trivial solution $K = \nat$, and all the difficulty lies in thinning $K$ along $h$, which uses $h$ as an oracle. The decomposition separates the two: the arbitrary instance is only the limit set, while the coloring used for thinning stays in the cone-avoiding class.
:::
::::

::::exercise{#ex-rt32-coding-power difficulty=2 objective="Combine the cone avoidance basis theorem with Seetapun's theorem to determine the coding power of RT³₂." lessons="triples, jockusch"}
Let $C$ be a set with $C \not\leq_T \emptyset'$. Show that every computable coloring of $[\nat]^3$ with two colors has an infinite homogeneous set that does not compute $C$. Conclude that :ref{#prop-rt32-jump} is optimal: the sets computed by all infinite homogeneous sets of every computable coloring of triples are computable in $\emptyset'$.

:::solution
Let $f$ be the coloring. In the proof of :ref{#prop-erdos-rado-tree}, the paths of the Erdős–Radó tree of $f$ are computable, uniformly, from the members of a non-empty $\Pi^0_1(\emptyset')$ class together with $\emptyset'$. By the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $\emptyset'$, this class has a member $Q$ with $C \not\leq_T \emptyset' \oplus Q$. So there is an infinite pre-homogeneous set $A \leq_T \emptyset' \oplus Q$, and $C \not\leq_T A$. The induced coloring of $[A]^2$, transported to $[\nat]^2$ by the enumeration $p$ of $A$, is $A$-computable. By :ref{#thm-seetapun} with $Z = A$, it has an infinite homogeneous set $L$ with $C \not\leq_T A \oplus L$. The set $H = p[L]$ is homogeneous for $f$ and computable in $A \oplus L$, so $C \not\leq_T H$. For the conclusion, if every infinite homogeneous set of a computable coloring of triples computes $C$, then $C \leq_T \emptyset'$.
:::
::::

::::exercise{#ex-wkl-rt22-model difficulty=2 objective="Interleave PA degrees and homogeneous sets to build an ω-model of WKL₀ + RT²₂ without the halting set."}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{RT}^2_2$ not containing $\emptyset'$.

:::solution
Combine the constructions of :ref{#lem-scott-cone} and :ref{#cor-rt22-not-aca}: at even stages, add a set $P$ PA relative to $Z_n$ with $\emptyset' \not\leq_T Z_n \oplus P$, by the relativized cone avoidance basis theorem; at odd stages, handle the next coloring with :ref{#thm-seetapun}. The resulting Turing ideal is a Scott ideal, satisfies $\mathsf{RT}^2_2$, and does not contain $\emptyset'$.
:::
::::

## The place of Ramsey's theorem for pairs

Together with :ref{#cor-wkl-not-rt22}, Seetapun's theorem shows that $\mathsf{RT}^2_2$ escapes the Big Five: it lies strictly below $\mathsf{ACA}_0$ and is not provable in $\mathsf{WKL}_0$. The following results, admitted here, complete the picture.

- **Liu (2012)** proved that $\mathsf{RT}^2_2$ does not imply $\mathsf{WKL}_0$, by showing that the infinite pigeonhole principle avoids PA degrees in the sense of :ref{#thm-dj-cone-avoidance}: for every set $A$, there is an infinite subset of $A$ or of $\overline A$ that is not of PA degree. So $\mathsf{RT}^2_2$ and $\mathsf{WKL}_0$ are incomparable.
- **Cholak, Jockusch and Slaman (2001)** showed that every computable coloring of pairs has a low₂ infinite homogeneous set, and determined the coding power of $\mathsf{RT}^n_2$ for $n \geq 3$: some homogeneous set avoids any given set not computable in $\emptyset^{(n-2)}$ (:ref{#ex-rt32-coding-power} for $n = 3$, :ref{#ex-rtn-coding-power} in general).
- **Monin and Patey (2019)** extended strong cone avoidance up the arithmetic hierarchy: for every set $A$ and every set $C$ that is not $\Delta^0_n$, some infinite subset of $A$ or of $\overline A$ is a set $H$ such that $C$ is not $\Delta^0_n(H)$. In particular every set has an infinite subset, of itself or of its complement, that is not high.
- **Wang (2014)** and **Cholak and Patey (2020)** studied weakenings of Ramsey's theorem that allow a homogeneous set to use $\ell$ colors instead of one, the **thin set theorems**. For colorings of $n$-tuples with arbitrarily many colors, strong cone avoidance holds exactly when $\ell$ is at least the $n$-th Catalan number.

$\mathsf{RT}^2_2$ is the first and most studied of a large family of combinatorial principles, the **reverse mathematics zoo**, many of which lie strictly below $\mathsf{ACA}_0$ without being equivalent to any of the Big Five. The first-order strength of $\mathsf{RT}^2_2$, that is, which arithmetic statements it proves, is studied in the course on induction and conservation.

## Cohesiveness versus stability

The following table collects bounds on the solutions of **computable** instances. In the middle column, every computable instance has a solution of the given kind; in the last column, some computable instance has no solution of the given kind.

| Principle | Solutions always exist | Solutions may fail to exist |
| --- | --- | --- |
| $\mathsf{COH}$ | $\Delta^0_2$; low₂ (:ref{#cor-coh-bounds}) | low (:ref{#prop-coh-no-low}) |
| $\mathsf{SRT}^2_2$ | $\Delta^0_2$ (:ref{#ex-stable}); low₂ (Cholak, Jockusch, Slaman) | low (Downey, Hirschfeldt, Lempp, Solomon) |
| $\mathsf{RT}^2_2$ | low₂ (Cholak, Jockusch, Slaman) | $\Delta^0_2$ (:ref{#thm-jockusch-no-delta2}) |

The table does not separate $\mathsf{COH}$ from $\mathsf{SRT}^2_2$, and neither implies the other.

- $\mathsf{COH}$ does not imply $\mathsf{SRT}^2_2$ over $\mathsf{RCA}_0$. There is an ω-model of $\mathsf{COH}$ in which some computable stable coloring has no solution (Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman); a proof-theoretic argument also works, since $\mathsf{COH}$ proves no new first-order statement while $\mathsf{SRT}^2_2$ does (see the course on induction and conservation).
- $\mathsf{SRT}^2_2$ does not imply $\mathsf{COH}$, hence not $\mathsf{RT}^2_2$, over $\mathsf{RCA}_0$. This was a central open problem for over a decade. Chong, Slaman and Yang (2014) solved it with a non-standard model of $\mathsf{SRT}^2_2$ in which every set is low in the sense of the model, and Monin and Patey (2021) found an ω-model, in which no set has a jump PA relative to $\emptyset'$. By :ref{#prop-coh-no-low}, such a model does not satisfy $\mathsf{COH}$. The theorem of Downey, Hirschfeldt, Lempp and Solomon explains why an ω-model of low sets could not work.

So the decomposition is proper: $\mathsf{RT}^2_2$ is the conjunction of two strictly weaker, incomparable principles.

## Notes and references

The track on lowness and avoidance revisits this theorem with the forcing question (:ref{to="avoidance/seetapun-forcing"}), separates other Ramsey-type principles by custom preservation properties (:ref{to="separation-design/custom-properties"}), and proves the jump versions: solutions of non-high degree for the pigeonhole principle (:ref{to="jump-cone-avoidance/pigeons-non-high"}) and the theorem of Monin and Patey on Δ⁰₂ sets (:ref{to="jump-compactness-avoidance/delta2-jump-pa"}).

Seetapun's theorem appeared in Seetapun and Slaman (1995); the original proof is a direct forcing argument with finitely many Mathias conditions at once (Dzhafarov–Mummert, §8.3). The proof given here is due to Dzhafarov and Jockusch (2009), with the cohesiveness step of Cholak, Jockusch and Slaman (2001) (Hirschfeldt, §6.7, Corollary 6.64 and Theorem 6.61; Dzhafarov–Mummert, §8.5.1; Monin and Patey, section *Computational weakness of RT²₂*). The failure of strong cone avoidance for stable colorings is Proposition 8.5.5 of Dzhafarov–Mummert. :ref{#ex-rt32-coding-power} and :ref{#ex-rtn-coding-power} follow the proof of a theorem of Cholak, Jockusch and Slaman (Hirschfeldt, Theorem 6.65). Liu's theorem is proved in the appendix of Hirschfeldt's book and in Dzhafarov–Mummert, §8.6. The low₂ bounds are Theorems 6.52 and 6.53 of Hirschfeldt, the theorem of Downey, Hirschfeldt, Lempp and Solomon is Theorem 6.37. The history of the problem whether $\mathsf{SRT}^2_2$ implies $\mathsf{RT}^2_2$ is told in Dzhafarov–Mummert, §8.8 (Theorems 8.8.2, 8.8.5 and 8.8.7), which also records the questions that remain open for finer reducibilities, for instance whether $\mathsf{COH}$ is reducible to $\mathsf D^2_2$ by an omniscient computable reduction (Question 8.8.13). The surveys of Hirschfeldt (Chapter 9) and of Dzhafarov and Mummert (Chapter 9) describe the reverse mathematics zoo.

- D. Seetapun and T. A. Slaman, *On the strength of Ramsey's theorem*, Notre Dame Journal of Formal Logic 36 (1995), 570–582.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- R. Downey, D. R. Hirschfeldt, S. Lempp and R. Solomon, *A Δ⁰₂ set with no infinite low subset in either it or its complement*, Journal of Symbolic Logic 66 (2001), 1371–1381.
- C. T. Chong, T. A. Slaman and Y. Yang, *The metamathematics of stable Ramsey's theorem for pairs*, Journal of the American Mathematical Society 27 (2014), 863–892.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics 389 (2021), 107903.
- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095.
- W. Wang, *Some logically weak Ramseyan theorems*, Advances in Mathematics 261 (2014), 1–25.
- P. Cholak and L. Patey, *Thin set theorems and cone avoidance*, Transactions of the American Mathematical Society 373 (2020), 2743–2773.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.

:::::exercises
::::exercise{#ex-seetapun-k-colors difficulty=1 objective="Extend Seetapun's theorem to finitely many colors by merging colors and relativizing."}
Let $Z$ be a set, $C \not\leq_T Z$ and $k \geq 2$. Show that every $Z$-computable coloring $f : [\nat]^2 \to k$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$.

:::solution
By induction on $k$, for all $Z$ simultaneously; the case $k = 2$ is :ref{#thm-seetapun}. Let $f : [\nat]^2 \to k + 1$ be $Z$-computable, and $g$ the $Z$-computable coloring obtained by merging the colors $k - 1$ and $k$. By the induction hypothesis, $g$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$. If its color is less than $k - 1$, $H$ is homogeneous for $f$. Otherwise, let $p$ enumerate $H$ in increasing order; the coloring $h(\{ i, j \}) = f(\{ p(i), p(j) \}) - (k - 1)$ takes two values and is computable in $Z \oplus H$. By :ref{#thm-seetapun} with $Z \oplus H$ in place of $Z$, it has an infinite homogeneous set $L$ with $C \not\leq_T Z \oplus H \oplus L$, and $p[L]$, which is computable in $H \oplus L$, is homogeneous for $f$.
:::
::::

::::exercise{#ex-rt22-not-rt32 difficulty=1 objective="Separate Ramsey's theorem for pairs from Ramsey's theorem for triples." lessons="triples"}
Show that $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ does not prove $\mathsf{RT}^3_2$, in two ways: through :ref{#thm-rt3-aca}, and directly through the coloring of :ref{#prop-rt32-jump}.

:::solution
Let $\mathcal I$ be the ω-model of :ref{#cor-rt22-not-aca}: it satisfies $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ and does not contain $\emptyset'$. First way: if $\mathcal I$ satisfied $\mathsf{RT}^3_2$, it would satisfy $\mathsf{ACA}_0$ by :ref{#thm-rt3-aca}, and an ω-model of $\mathsf{ACA}_0$ contains the jump of each of its members, in particular $\emptyset'$. Second way: the computable coloring of triples of :ref{#prop-rt32-jump} belongs to $\mathcal I$, and all its infinite homogeneous sets compute $\emptyset'$, so none of them belongs to $\mathcal I$.
:::
::::

::::exercise{#ex-rt22-not-principal difficulty=1 objective="Show that no ω-model of RT²₂ consists of the sets computable in a single set." lessons="triples"}
Show that no Turing ideal of the form $\{ Y : Y \leq_T X \}$ is an ω-model of $\mathsf{RT}^2_2$.

:::solution
Relativize :ref{#thm-jockusch-no-delta2} to $X$: there is an $X$-computable coloring $f : [\nat]^2 \to 2$ with no infinite $\Delta^0_2(X)$ homogeneous set, in particular none computable in $X$. The coloring belongs to the ideal, and no infinite homogeneous set does.
:::
::::

::::exercise{#ex-rt22-intersection-models difficulty=1 objective="Determine the sets that belong to every ω-model of RT²₂."}
Show that for every non-computable set $C$ there is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ not containing $C$. Deduce that the sets belonging to every ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ are exactly the computable sets.

:::solution
Repeat the proof of :ref{#cor-rt22-not-aca} with $C$ in place of $\emptyset'$: start from $Z_0 = \emptyset$, which does not compute $C$, and apply :ref{#thm-seetapun} with the set $C$ at each stage. The resulting Turing ideal satisfies $\mathsf{RT}^2_2$ and does not contain $C$. Conversely, every ω-model of $\mathsf{RCA}_0$ is a non-empty Turing ideal, closed downwards under $\leq_T$, so it contains every computable set. Hence the sets common to all ω-models of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ are the computable sets.
:::
::::

::::exercise{#ex-rtn-coding-power difficulty=3 objective="Determine the coding power of Ramsey's theorem for $n$-tuples by controlling jumps with the low basis theorem." lessons="triples, jockusch"}
Let $n \geq 2$ and $k \geq 2$. Show that for every set $Z$ and every $C$ with $C \not\leq_T Z^{(n-2)}$, every $Z$-computable coloring $f : [\nat]^n \to k$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$. Deduce that, for $n \geq 3$, a set is computed by all infinite homogeneous sets of some computable coloring of $[\nat]^n$ with finitely many colors if and only if it is computable in $\emptyset^{(n-2)}$.

:::solution
By induction on $n$, for all $Z$, $C$ and $k$ simultaneously. For $n = 2$, this is :ref{#ex-seetapun-k-colors}. Assume the statement for some $n \geq 2$, and let $f$ be a $Z$-computable coloring of $[\nat]^{n+1}$ with $k$ colors and $C \not\leq_T Z^{(n-1)}$.

By the proof of :ref{#prop-erdos-rado-tree} relativized to $Z$, the paths of the Erdős–Radó tree of $f$ are computable, uniformly, from $Z' \oplus Q$ for the members $Q$ of a non-empty $\Pi^0_1(Z')$ class $\mathcal P$. Choose $Q \in \mathcal P$ such that $W = Z' \oplus Q$ satisfies $C \not\leq_T W^{(n-2)}$:

- if $n = 2$, by the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $Z'$, since $C \not\leq_T Z'$;
- if $n \geq 3$, by the low basis theorem relativized to $Z'$, with $W' \leq_T Z''$; then $W^{(n-2)} = (W')^{(n-3)} \leq_T Z^{(n-1)}$, so $C \not\leq_T W^{(n-2)}$.

Let $X \leq_T W$ be an infinite pre-homogeneous set given by a path, $p$ its increasing enumeration, and $g(\{ i_1, \dots, i_n \}) = f(\{ p(i_1), \dots, p(i_n), p(j) \})$ for any $j > i_n$, the induced coloring transported to $[\nat]^n$. It has $k$ colors and is computable in $Z \oplus X \leq_T W$. By the induction hypothesis with $W$ in place of $Z$, $g$ has an infinite homogeneous set $L$ with $C \not\leq_T W \oplus L$. The set $H = p[L]$ is homogeneous for the induced coloring, hence for $f$, and $Z \oplus H \leq_T W \oplus L$, so $C \not\leq_T Z \oplus H$.

For the last statement, let $n \geq 3$. If $C \not\leq_T \emptyset^{(n-2)}$, the statement with $Z = \emptyset$ gives, for every computable coloring of $[\nat]^n$ with finitely many colors, an infinite homogeneous set that does not compute $C$. Conversely, by :ref{#ex-coding-n-jumps}, some computable coloring of $[\nat]^n$ with finitely many colors has all its infinite homogeneous sets computing $\emptyset^{(n-2)}$, hence every set computable in $\emptyset^{(n-2)}$. Adapted from Hirschfeldt, *Slicing the Truth*, Theorem 6.65 (Cholak, Jockusch and Slaman).
:::
::::
:::::
