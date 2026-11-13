---
title: Low₂ solutions of Ramsey's theorem for pairs
summary: Combining cohesiveness and the pigeonhole principle for Δ⁰₂ sets, every computable coloring of pairs has an infinite homogeneous set whose jump is computed by any given set PA relative to ∅′, hence a low₂ one (Cholak–Jockusch–Slaman); ω-models of low₂ sets; no low basis exists (Downey–Hirschfeldt–Lempp–Solomon).
duration: 30
prerequisites: [cjs-theorem, ramsey-theorem/seetapun, ramsey-theorem/triples, weak-preservation]
---

The two halves of the decomposition of Ramsey's theorem for pairs (:ref{#thm-rt22-decomposition}) admit weakly low bases: cohesiveness by :ref{#thm-coh-weakly-low}, and the pigeonhole principle for $\Delta^0_2$ sets by :ref{#thm-d22-weakly-low}. This lesson combines them. The combination is not automatic: the second step is applied relative to the cohesive set built in the first, and it needs a set PA relative to the jump of that cohesive set. The density of PA degrees (:ref{#lem-pa-between}) provides the room. The lesson ends with the limits of the method: no low basis exists, and the reason is a theorem of Downey, Hirschfeldt, Lempp and Solomon, admitted here.

## Combining the two halves

:::theorem[Cholak, Jockusch, Slaman]{#thm-rt22-weakly-low}
Let $Z$ be a set, $f : [\nat]^2 \to 2$ a $Z$-computable coloring, and $P$ a set PA relative to $Z'$. There is an infinite homogeneous set $H$ for $f$ with $(Z \oplus H)' \leq_T P$. So $\mathsf{RT}^2_2$ admits a weakly low basis.
:::

:::proof{of=thm-rt22-weakly-low}
We write the proof for $Z = \emptyset$; it relativizes. By :ref{#lem-pa-between}, there is $Q$ PA relative to $\emptyset'$ such that $P$ is PA relative to $Q$. Let $R_x = \{ y : f(\{ x, y \}) = 1 \}$, a computable sequence. By :ref{#thm-coh-weakly-low}, there is an $\vec R$-cohesive set $C$ with $C' \leq_T Q$. Since $P$ is PA relative to $Q$, it is PA relative to $C'$.

Let $p$ be the increasing enumeration of $C$, and $g(\{ i, j \}) = f(\{ p(i), p(j) \})$. By :ref{#thm-rt22-decomposition}, $g$ is stable; it is computable in $C$. Its limit set $A_g$ is $\Delta^0_2(C)$ by the limit lemma relativized (:ref{#thm-limit-lemma}). By :ref{#thm-d22-weakly-low} relativized to $C$, with the oracle $P$, there is an infinite set $H_0$ contained in $A_g$ or in its complement with $(C \oplus H_0)' \leq_T P$. By :ref{#prop-srt-d22}, $g \oplus H_0$ computes an infinite homogeneous set $H_1$ for $g$, and $H_1 \leq_T C \oplus H_0$. The set $H = p[H_1]$ is homogeneous for $f$, and computable in $C \oplus H_0$, so $H' \leq_T (C \oplus H_0)' \leq_T P$.
:::

:::corollary[Cholak, Jockusch, Slaman]{#cor-rt22-low2}
Every computable coloring of pairs has a low₂ infinite homogeneous set. There is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ consisting of low₂ sets.
:::

:::proof{of=cor-rt22-low2}
By :ref{#thm-rt22-weakly-low} and item 2 of :ref{#prop-weakly-low-properties}, every computable coloring has an infinite homogeneous set $H$ with $H'' \leq_T \emptyset''$. The ω-model is given by :ref{#thm-weakly-low-model}, with $P$ PA relative to $\emptyset'$ and $P' \leq_T \emptyset''$.
:::

The model contains no set computing $\emptyset'$, which gives a second proof of :ref{#cor-rt22-not-aca}. The two proofs illustrate the two kinds of properties of the first lesson: Seetapun's theorem is a genericity property, cone avoidance, while the low₂ bound is an effectiveness property, obtained from an effective construction relative to $P$.

:::quiz[Ramsey's theorem for pairs]
In the proof of :ref{#thm-rt22-weakly-low}, why is the cohesive set built with the oracle $Q$ rather than $P$?

- [x] Because the second step needs a set PA relative to $C'$ and computing the jump of the final solution; if $C'$ were only computable in $P$, $P$ need not be PA relative to $C'$.
- [ ] Because $P$ does not compute a cohesive set.

  It does; the issue is what remains available for the second step.
- [ ] Because $Q$ is low relative to $\emptyset'$.

  Nothing is assumed about the jump of $Q$.

---

Why is the theorem for $\Delta^0_2$ sets applied relative to $C$ rather than unrelativized?

- [x] Because the limit set $A_g$ is $\Delta^0_2$ relative to $C$, not necessarily $\Delta^0_2$, and the stable coloring $g$ is only computable in $C$.
- [ ] Because $C$ is low.

  It need not be: by :ref{#prop-coh-no-low}, cohesive sets are not always low.
- [ ] Because the homogeneous set must be a subset of $C$.

  The homogeneous set is $p[H_1] \subseteq C$, but this is not why the relativization is needed.
:::

## No low basis

The weakly low basis cannot be improved to a low basis, even for the pigeonhole principle for $\Delta^0_2$ sets, although every computable instance of $\mathsf D^2_2$ has a $\Delta^0_2$ solution. The proof uses an infinite injury priority argument, outside the scope of this course.

:::theorem[Downey, Hirschfeldt, Lempp, Solomon]{#thm-dhls}
There is a $\Delta^0_2$ set $A$ such that neither $A$ nor $\overline A$ has an infinite low subset.
:::

By the last exercise of :ref{to="lowness/weak-preservation"}, such a set is neither hyperimmune nor co-hyperimmune. The construction is intrinsically complex: Chong, Slaman and Yang built a non-standard model of $\mathsf{RCA}_0 + \mathsf{SRT}^2_2$ in which every set is low in the sense of the model, exploiting a failure of $\Sigma^0_2$ induction (see :ref{to="ramsey-theorem/seetapun"}); so the existence of a set as in :ref{#thm-dhls} is not provable in $\mathsf{RCA}_0 + \mathsf{SRT}^2_2$, and its proof uses induction in an essential way. For cohesiveness, the gap between low and weakly low bases is explained by :ref{#prop-coh-no-low}: some instance forces the jump of every solution to be PA relative to $\emptyset'$. For $\mathsf D^2_2$ this is not the case: Monin and Patey showed that every $\Delta^0_2$ set has an infinite subset, of itself or of its complement, whose jump is not PA relative to $\emptyset'$.

## Exercises

::::exercise{difficulty=1}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{RT}^2_2$ consisting of low₂ sets.

:::solution
$\mathsf{WKL}$ admits a low basis, hence a weakly low basis, and so does $\mathsf{RT}^2_2$ by :ref{#thm-rt22-weakly-low}. By the last exercise of :ref{to="lowness/weakly-low-bases"}, the product problem, whose instances are pairs of an infinite binary tree and a coloring of pairs, admits a weakly low basis. Apply :ref{#thm-weakly-low-model} to it, with $P$ PA relative to $\emptyset'$ and $P' \leq_T \emptyset''$: the resulting Turing ideal satisfies both problems, since a tree $T$ in the ideal is the first component of the instance $T \oplus c$ of the product, with $c$ a fixed computable coloring, and a coloring $c'$ in the ideal is the second component of $T_0 \oplus c'$, with $T_0$ a fixed computable infinite tree. Its members are low₂.
:::
::::

::::exercise{difficulty=2}
Show by induction on $k \geq 2$ that $\mathsf{RT}^2_k$ admits a weakly low basis.

:::solution
The case $k = 2$ is :ref{#thm-rt22-weakly-low}. Let $k \geq 3$, $f$ a $Z$-computable coloring of pairs with $k$ colors, and $P$ PA relative to $Z'$. By :ref{#lem-pa-between} relativized, let $Q$ be PA relative to $Z'$ with $P$ PA relative to $Q$. Let $f_0$ be the coloring with $k - 1$ colors obtained by merging the colors $k - 2$ and $k - 1$. By the induction hypothesis with $Q$, there is an infinite set $H_0$ homogeneous for $f_0$ with $(Z \oplus H_0)' \leq_T Q$. If its color is less than $k - 2$, $H_0$ is homogeneous for $f$ and $(Z \oplus H_0)' \leq_T P$. Otherwise $f$ takes two values on $[H_0]^2$; transported to $[\nat]^2$ by the enumeration of $H_0$, it is a coloring with two colors computable in $Z \oplus H_0$. Since $P$ is PA relative to $Q$, which computes $(Z \oplus H_0)'$, :ref{#thm-rt22-weakly-low} relativized to $Z \oplus H_0$ gives an infinite homogeneous set, whose image $H \subseteq H_0$ is homogeneous for $f$, with $(Z \oplus H)' \leq_T P$.
:::
::::

## Notes and references

:ref{#thm-rt22-weakly-low} and :ref{#cor-rt22-low2} are due to Cholak, Jockusch and Slaman (2001); Hirschfeldt presents them as Theorem 6.53 and Corollary 6.58, Dzhafarov and Mummert as Theorem 8.5.8 and Corollary 8.5.9, with the induction on the number of colors of the second exercise. The proof given here follows the section *Ramsey's theorem for pairs* of the chapter *Lowness* of Patey's monograph. :ref{#thm-dhls} is due to Downey, Hirschfeldt, Lempp and Solomon (2001), Theorem 6.37 of Hirschfeldt. Monin and Patey (2021) proved that every $\Delta^0_2$ set has an infinite subset in it or its complement whose jump is not PA relative to $\emptyset'$, a result that belongs to the later course on jump compactness avoidance. Dzhafarov and Jockusch (2009) combined the low₂ bound with cone avoidance (Dzhafarov–Mummert, Theorem 8.5.10).

- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- R. Downey, D. R. Hirschfeldt, S. Lempp and R. Solomon, *A Δ⁰₂ set with no infinite low subset in either it or its complement*, Journal of Symbolic Logic 66 (2001), 1371–1381.
- C. T. Chong, T. A. Slaman and Y. Yang, *The metamathematics of stable Ramsey's theorem for pairs*, Journal of the American Mathematical Society 27 (2014), 863–892.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics 389 (2021), 107903.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 6.4 and 6.6.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.5.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, section *Ramsey's theorem for pairs*.
