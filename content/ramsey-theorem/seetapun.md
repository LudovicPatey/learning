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

The last step thins $K$ along $g$, which is computable in $Z \oplus G$. This is why the pigeonhole step is applied to the limit set, with the stable coloring kept as a parameter, and not to the stable coloring itself: for stable colorings that are not computable in the sets already built, cone avoidance fails (see the exercises).

:::corollary[Seetapun]{#cor-rt22-not-aca}
There is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ not containing $\emptyset'$. Consequently $\mathsf{RT}^2_2$ does not imply $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
:::

:::proof{of=cor-rt22-not-aca}
Build sets $Z_0 = \emptyset \leq_T Z_1 \leq_T \cdots$ with $\emptyset' \not\leq_T Z_n$. Fix an enumeration of all pairs $(e, m)$ in which each pair appears infinitely often. At stage $n$, take the next pair $(e, m)$ with $m \leq n$. If $\Phi^{Z_m}_e$ is a coloring of $[\nat]^2$ with two colors, it is $Z_n$-computable, and :ref{#thm-seetapun} gives an infinite homogeneous set $H$ with $\emptyset' \not\leq_T Z_n \oplus H$; let $Z_{n+1} = Z_n \oplus H$. Otherwise $Z_{n+1} = Z_n$.

The class $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$ is a Turing ideal not containing $\emptyset'$. Every coloring in $\mathcal I$ is $\Phi^{Z_m}_e$ for some $e, m$, and is handled at some stage, so it has a homogeneous set in $\mathcal I$. By absoluteness, $\mathcal I$ satisfies $\mathsf{RT}^2_2$, and it is not a jump ideal.
:::

The construction of the ω-model is the standard method for separations in reverse mathematics: a class of sets (here, those not computing $\emptyset'$) that is closed under adding solutions to the instances of the weaker principle, and excludes the stronger one. The course on reducibilities develops it as the **preservation** of a weakness property.

## The place of Ramsey's theorem for pairs

Together with :ref{#cor-wkl-not-rt22}, Seetapun's theorem shows that $\mathsf{RT}^2_2$ escapes the Big Five: it lies strictly below $\mathsf{ACA}_0$ and is not provable in $\mathsf{WKL}_0$. The following results, admitted here, complete the picture.

- **Liu (2012)** proved that $\mathsf{RT}^2_2$ does not imply $\mathsf{WKL}_0$, by showing that the infinite pigeonhole principle avoids PA degrees in the sense of :ref{#thm-dj-cone-avoidance}: for every set $A$, there is an infinite subset of $A$ or of $\overline A$ that is not of PA degree. So $\mathsf{RT}^2_2$ and $\mathsf{WKL}_0$ are incomparable.
- **Cholak, Jockusch and Slaman (2001)** showed that every computable coloring of pairs has a low₂ infinite homogeneous set, and determined the coding power of $\mathsf{RT}^n_2$ for $n \geq 3$: some homogeneous set avoids any given set not computable in $\emptyset^{(n-2)}$ (see the exercises for $n = 3$).
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

## Exercises

::::exercise{difficulty=1}
Show that there is an infinite set $A$ all of whose infinite subsets compute a given set $C$, and explain why this does not contradict :ref{#thm-dj-cone-avoidance}.

:::solution
Let $A = \{ \langle C \uh n \rangle : n \in \nat \}$, the set of codes of the prefixes of $C$, with a coding in which longer strings have larger codes. An infinite subset of $A$ contains codes of arbitrarily long prefixes of $C$, so it computes $C$: to find $C(x)$, search for an element coding a string of length larger than $x$. If $C$ is not computable, :ref{#thm-dj-cone-avoidance} with $Z = \emptyset$ gives an infinite subset of $A$ or of $\overline{A}$ that does not compute $C$; it cannot be a subset of $A$, so it is a subset of $\overline{A}$. There is no contradiction: the theorem only guarantees a solution on one of the two sides, without saying which.
:::
::::

::::exercise{difficulty=1}
Show that the coloring $h$ in the proof of :ref{#prop-rt32-jump} is stable, and deduce that :ref{#thm-seetapun} fails for stable colorings that are not computable in $Z$: there is a stable coloring of pairs all of whose infinite homogeneous sets compute $\emptyset'$. Why does this not affect the proof of :ref{#thm-seetapun}?

:::solution
For each $x$, $h(\{ x, y \}) = 1$ for all $y > m(x)$, so $h$ is stable with limit set $\nat$. The proof of :ref{#prop-rt32-jump} shows that every infinite homogeneous set for $h$ computes $\emptyset'$. In the proof of :ref{#thm-seetapun}, the stable coloring $g$ is computable in $Z \oplus G$, and the pigeonhole principle is applied to its limit set. For $h$, the limit set $\nat$ is its own trivial solution $K = \nat$, and all the difficulty lies in thinning $K$ along $h$, which uses $h$ as an oracle. The decomposition separates the two: the arbitrary instance is only the limit set, while the coloring used for thinning stays in the cone-avoiding class.
:::
::::

::::exercise{difficulty=2}
Let $C$ be a set with $C \not\leq_T \emptyset'$. Show that every computable coloring of $[\nat]^3$ with two colors has an infinite homogeneous set that does not compute $C$. Conclude that :ref{#prop-rt32-jump} is optimal: the sets computed by all infinite homogeneous sets of every computable coloring of triples are computable in $\emptyset'$.

:::solution
Let $f$ be the coloring. In the proof of :ref{#prop-erdos-rado-tree}, the paths of the Erdős–Radó tree of $f$ are computable, uniformly, from the members of a non-empty $\Pi^0_1(\emptyset')$ class together with $\emptyset'$. By the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $\emptyset'$, this class has a member $Q$ with $C \not\leq_T \emptyset' \oplus Q$. So there is an infinite pre-homogeneous set $A \leq_T \emptyset' \oplus Q$, and $C \not\leq_T A$. The induced coloring of $[A]^2$, transported to $[\nat]^2$ by the enumeration $p$ of $A$, is $A$-computable. By :ref{#thm-seetapun} with $Z = A$, it has an infinite homogeneous set $L$ with $C \not\leq_T A \oplus L$. The set $H = p[L]$ is homogeneous for $f$ and computable in $A \oplus L$, so $C \not\leq_T H$. For the conclusion, if every infinite homogeneous set of a computable coloring of triples computes $C$, then $C \leq_T \emptyset'$.
:::
::::

::::exercise{difficulty=2}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{RT}^2_2$ not containing $\emptyset'$.

:::solution
Combine the constructions of :ref{#lem-scott-cone} and :ref{#cor-rt22-not-aca}: at even stages, add a set $P$ PA relative to $Z_n$ with $\emptyset' \not\leq_T Z_n \oplus P$, by the relativized cone avoidance basis theorem; at odd stages, handle the next coloring with :ref{#thm-seetapun}. The resulting Turing ideal is a Scott ideal, satisfies $\mathsf{RT}^2_2$, and does not contain $\emptyset'$.
:::
::::

## Notes and references

The track on lowness and avoidance revisits this theorem with the forcing question (:ref{to="avoidance/seetapun-forcing"}), separates other Ramsey-type principles by custom preservation properties (:ref{to="separation-design/custom-properties"}), and proves the jump versions: solutions of non-high degree for the pigeonhole principle (:ref{to="jump-cone-avoidance/pigeons-non-high"}) and the theorem of Monin and Patey on Δ⁰₂ sets (:ref{to="jump-compactness-avoidance/delta2-jump-pa"}).

Seetapun's theorem appeared in Seetapun and Slaman (1995); the original proof is a direct forcing argument with finitely many Mathias conditions at once (Dzhafarov–Mummert, §8.3). The proof given here is due to Dzhafarov and Jockusch (2009), with the cohesiveness step of Cholak, Jockusch and Slaman (2001) (Hirschfeldt, §6.7, Corollary 6.64 and Theorem 6.61; Dzhafarov–Mummert, §8.5.1; Monin and Patey, section *Computational weakness of RT²₂*). The failure of strong cone avoidance for stable colorings is Proposition 8.5.5 of Dzhafarov–Mummert. The third exercise is the case $n = 3$ of a theorem of Cholak, Jockusch and Slaman (Hirschfeldt, Theorem 6.65). Liu's theorem is proved in the appendix of Hirschfeldt's book and in Dzhafarov–Mummert, §8.6. The low₂ bounds are Theorems 6.52 and 6.53 of Hirschfeldt, the theorem of Downey, Hirschfeldt, Lempp and Solomon is Theorem 6.37. The history of the problem whether $\mathsf{SRT}^2_2$ implies $\mathsf{RT}^2_2$ is told in Dzhafarov–Mummert, §8.8 (Theorems 8.8.2, 8.8.5 and 8.8.7), which also records the questions that remain open for finer reducibilities, for instance whether $\mathsf{COH}$ is reducible to $\mathsf D^2_2$ by an omniscient computable reduction (Question 8.8.13). The surveys of Hirschfeldt (Chapter 9) and of Dzhafarov and Mummert (Chapter 9) describe the reverse mathematics zoo.

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
