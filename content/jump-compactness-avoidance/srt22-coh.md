---
title: Stable Ramsey's theorem without cohesiveness
summary: An ω-model of stable Ramsey's theorem for pairs in which no set has a jump PA relative to ∅′; it satisfies neither cohesiveness nor Ramsey's theorem for pairs; the second-jump picture of COH, SRT²₂ and RT²₂; jump DNC avoidance, a Δ⁰₃ set all of whose homogeneous sets have a jump DNC relative to ∅′, and an open question.
duration: 35
prerequisites: [delta2-jump-pa, immunity-growth/dnc-functions, compactness-avoidance/liu-theorem]
---

This lesson draws the consequences of :ref{#thm-d22-jump-pa} for the reverse mathematics of Ramsey's theorem for pairs, and discusses the DNC analogue of jump PA avoidance, where the corresponding question for the pigeonhole principle is open.

## The separation

:::corollary{#cor-srt22-jump-pa}
$\mathsf{SRT}^2_2$ admits jump PA avoidance.
:::

:::proof{of=cor-srt22-jump-pa}
Let $D \leq_T Z$ with $Z'$ not PA relative to $D'$, and $f \leq_T Z$ a stable coloring. Its limit set $A_f$ is $\Delta^0_2(Z)$ by the limit lemma relativized. By :ref{#thm-d22-jump-pa}, there is an infinite $H$, contained in $A_f$ or in its complement, with $(Z \oplus H)'$ not PA relative to $D'$. By item 2 of :ref{#prop-srt-d22}, $f \oplus H$ computes an infinite homogeneous set $L$ for $f$, and $(Z \oplus L)' \leq_T (Z \oplus H)'$.
:::

:::theorem[Monin, Patey]{#thm-srt22-not-coh}
There is a Turing ideal satisfying $\mathsf{SRT}^2_2$ in which no member has a jump PA relative to $\emptyset'$. It satisfies neither $\mathsf{COH}$ nor $\mathsf{RT}^2_2$. Consequently $\mathsf{COH} \not\leq_\omega \mathsf{SRT}^2_2$, $\mathsf{RT}^2_2 \not\leq_\omega \mathsf{SRT}^2_2$, and some ω-model of $\mathsf{RCA}_0 + \mathsf{SRT}^2_2$ is not a model of $\mathsf{RT}^2_2$.
:::

:::proof{of=thm-srt22-not-coh}
By :ref{#cor-srt22-jump-pa} and :ref{#prop-jump-pa-model}, there is a Turing ideal $\mathcal I$ satisfying $\mathsf{SRT}^2_2$ whose members have jumps that are not PA relative to $\emptyset'$, and it does not satisfy $\mathsf{COH}$. It does not satisfy $\mathsf{RT}^2_2$ either: by item 3 of :ref{#ex-jump-pa-problems}, the sequence of :ref{#prop-coh-no-low} gives a computable coloring of pairs all of whose infinite homogeneous sets are cohesive for it, and none of them is in $\mathcal I$. A Turing ideal is an ω-model of $\mathsf{RCA}_0$, and it satisfies the $\Pi^1_2$ statement $\mathsf{SRT}^2_2$ in the sense of ω-models since every stable coloring in $\mathcal I$ has a homogeneous set in $\mathcal I$.
:::

The separation completes the picture of the decomposition :ref{#thm-rt22-decomposition}: $\mathsf{RT}^2_2$ is the conjunction of two principles neither of which implies the other, on ω-models as well as over $\mathsf{RCA}_0$. The converse non-implication, $\mathsf{SRT}^2_2 \not\leq_\omega \mathsf{COH}$, is the theorem of Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman quoted in :ref{to="ramsey-theorem/seetapun"}. Before Monin and Patey, Chong, Slaman and Yang (2014) had shown that $\mathsf{SRT}^2_2$ does not imply $\mathsf{COH}$ over $\mathsf{RCA}_0$, with a non-standard model in which every set is low in the sense of the model. By :ref{#thm-dhls}, no ω-model of $\mathsf{SRT}^2_2$ consists of low sets, so the standard version needs a weakness property that is preserved by $\mathsf D^2_2$ and fails for cohesive sets. Jump PA avoidance is such a property; lowness, and even the weaker property "the jump is computed by a fixed set PA relative to $\emptyset'$" of :ref{#def-weakly-low-basis}, are not, the first because of :ref{#thm-dhls}, the second because it is satisfied by $\mathsf{COH}$.

:::quiz[the separation]
Why does the proof of :ref{#cor-srt22-jump-pa} not need jump PA avoidance for arbitrary instances of the pigeonhole principle?

- [x] Because the limit set of a $Z$-computable stable coloring is $\Delta^0_2(Z)$, which is the case covered by :ref{#thm-d22-jump-pa}; the passage from the limit set back to a homogeneous set is computable in $f \oplus H$.
- [ ] Because stable colorings have computable limit sets.

  Their limit sets are only $\Delta^0_2(Z)$ in general.
- [ ] Because every homogeneous set for $f$ is contained in $A_f$.

  It is contained in $A_f$ or in its complement (:ref{#prop-srt-d22}); this is the direction not used here.

---

Which property of the ideal $\mathcal I$ of :ref{#thm-srt22-not-coh} excludes $\mathsf{RT}^2_2$?

- [x] Ramsey's theorem for pairs has a computable instance all of whose solutions are cohesive for the sequence of :ref{#prop-coh-no-low}, hence have a jump PA relative to $\emptyset'$, and $\mathcal I$ contains no such set.
- [ ] $\mathcal I$ contains no set computing $\emptyset'$.

  $\mathsf{RT}^2_2$ does not require such sets: by Seetapun's theorem it admits cone avoidance.
- [ ] $\mathcal I$ is not a Scott ideal.

  The ideal can be taken to be a Scott ideal (first exercise below), and a Scott ideal can omit $\mathsf{RT}^2_2$; here $\mathsf{RT}^2_2$ is excluded by cohesiveness.
:::

The following table collects the avoidance properties of the track for four problems, for computable instances relative to $Z$.

| problem | PA avoidance | jump cone avoidance | jump PA avoidance |
| --- | --- | --- | --- |
| $\mathsf{WKL}$ | no | yes (low basis) | yes (low basis) |
| $\mathsf{COH}$ | yes (:ref{#thm-coh-pa-avoidance}) | yes (:ref{#thm-coh-weakly-low}) | no (:ref{#prop-coh-no-low}) |
| $\mathsf{D}^2_2$, $\mathsf{SRT}^2_2$ | yes (:ref{#thm-rt12-strong-pa}) | yes (:ref{#thm-d22-weakly-low}) | yes (:ref{#cor-srt22-jump-pa}) |
| $\mathsf{RT}^2_2$ | yes (:ref{#thm-liu-rt22}) | yes (:ref{#thm-rt22-weakly-low}) | no |

Jump PA avoidance is the only property in the table that separates $\mathsf{SRT}^2_2$ from $\mathsf{RT}^2_2$. At the first level, $\mathsf{COH}$ and $\mathsf{SRT}^2_2$ behave alike; one jump up, cohesiveness behaves like weak König's lemma relative to $\emptyset'$ (:ref{#cor-coh-bounds}), and jump PA avoidance detects it as PA avoidance detects $\mathsf{WKL}$.

## Jump DNC avoidance

Replacing PA by DNC gives a weaker property, as in :ref{to="compactness-avoidance/dnc-avoidance"}. A function $g$ is **DNC relative to** a set $D$ if $g(x) \neq \Phi^D_x(x)$ whenever $\Phi^D_x(x)$ converges.

:::definition{#def-jump-dnc-avoidance}
A problem $\mathsf P$ admits **jump DNC avoidance** if for all $D \leq_T Z$ such that $Z'$ computes no function DNC relative to $D'$, every instance $X \leq_T Z$ has a solution $Y$ such that $(Z \oplus Y)'$ computes no function DNC relative to $D'$. It admits **strong jump DNC avoidance** if this holds for every instance.
:::

A set PA relative to $D'$ computes a function DNC relative to $D'$, so the conclusion of jump DNC avoidance is stronger than that of jump PA avoidance; so is its hypothesis, and neither property implies the other formally. For ω-models the comparison is clear: with $D = Z = \emptyset$, jump DNC avoidance gives, by :ref{#lem-preservation-ideal}, a Turing ideal satisfying the problem in which no jump computes a function DNC relative to $\emptyset'$, and in particular no jump is PA relative to $\emptyset'$. The pigeonhole principle does not admit strong jump DNC avoidance, by a construction of Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman.

:::proposition{#prop-bi-immune-dnc}
For every set $X$ there is a set $A \leq_T X'$ such that for every infinite set $H$ contained in $A$ or in $\overline A$, $H \oplus X$ computes a function DNC relative to $X$.
:::

:::proof{of=prop-bi-immune-dnc}
We build $A$ by stages with the oracle $X'$, so that for every $e$: if $W^X_e \subseteq A$ or $W^X_e \subseteq \overline A$, then $|W^X_e| \leq 3e + 1$. Before stage $e$, the values $A(0), \dots, A(e - 1)$ are defined, and at most $2e$ other values. At stage $e$, ask $X'$ whether $W^X_e$ has at least $3e + 2$ elements. If so, enumerate $3e + 2$ of them; at most $3e$ have a defined value, so two of them, $x_0$ and $x_1$, have none; let $A(x_0) = 0$ and $A(x_1) = 1$. Then define $A(e)$, if it is not defined, as $0$. After stage $e$, $A(0), \dots, A(e)$ are defined and at most $2e + 2$ other values. The construction is $X'$-computable, and every number is eventually decided. If $|W^X_e| \geq 3e + 2$, then $W^X_e$ meets $A$ and $\overline A$, so the property holds.

Let $H \subseteq A$ be infinite, the other case being symmetric. If $W^X_e \subseteq H$, then $W^X_e \subseteq A$ and $|W^X_e| \leq 3e + 1$: $H$ is effectively immune relative to $X$, with the bound $e \mapsto 3e + 1$. By :ref{#thm-dnc-effectively-immune} relativized to $X$, $H \oplus X$ computes a function DNC relative to $X$.
:::

With $X = \emptyset'$, the set $A$ is $\Delta^0_3$, and every infinite subset $H$ of $A$ or of $\overline A$ has $H' \geq_T H \oplus \emptyset'$, which computes a function DNC relative to $\emptyset'$. So $\mathsf{RT}^1_2$ does not admit strong jump DNC avoidance. With $X = \emptyset$ the set $A$ is $\Delta^0_2$, and $\mathsf D^2_2$ does not admit DNC avoidance at the first level. For $\Delta^0_2$ instances at the second level, the problem is open.

:::question{#qu-d22-jump-dnc}
Is there a $\Delta^0_2$ set $A$ such that for every infinite set $H$ contained in $A$ or in $\overline A$, $H'$ computes a function DNC relative to $\emptyset'$?
:::

The question is stated in Patey's monograph, where it is observed that the natural approach, a countable version of the product classes of this course with countably many slices, fails because largeness for infinite products does not behave as for finite ones. If $\mathsf D^2_2$ admitted jump DNC avoidance, which would in particular answer the question negatively, some ω-model of $\mathsf{SRT}^2_2$ would not satisfy the rainbow Ramsey theorem for pairs: by a theorem of J. Miller, quoted in the monograph and admitted here, some computable coloring of pairs in which each color is used at most twice has only infinite rainbows (sets on which the coloring is injective) that compute a function DNC relative to $\emptyset'$.

:::quiz[jump DNC avoidance]
In the proof of :ref{#prop-bi-immune-dnc}, why are $3e + 2$ elements of $W^X_e$ required?

- [x] Because before stage $e$ at most $e + 2e = 3e$ values of $A$ are defined, so among $3e + 2$ elements two are still free, and they can be put on different sides.
- [ ] Because $H$ must have more than $3e$ elements.

  $H$ is infinite; the bound concerns $W^X_e$.
- [ ] Because the oracle $X'$ can only test sizes of the form $3e + 2$.

  $X'$ decides "$|W^X_e| \geq k$" for every $k$.
:::

## Exercises

::::exercise{difficulty=2}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{SRT}^2_2$ that is not a model of $\mathsf{COH}$.

:::solution
$\mathsf{WKL}$ admits jump PA avoidance by the low basis theorem relativized (item 1 of :ref{#ex-jump-pa-problems}), and $\mathsf{SRT}^2_2$ by :ref{#cor-srt22-jump-pa}. By the first exercise of :ref{to="jump-compactness-avoidance/jump-pa-avoidance"}, the problem whose instances are pairs of an instance of $\mathsf{WKL}$ and an instance of $\mathsf{SRT}^2_2$ admits jump PA avoidance. By :ref{#prop-jump-pa-model}, there is a Turing ideal satisfying it, hence both problems, in which no jump is PA relative to $\emptyset'$; it does not satisfy $\mathsf{COH}$.
:::
::::

::::exercise{difficulty=1}
Deduce from :ref{#prop-bi-immune-dnc} that some computable stable coloring of pairs has only infinite homogeneous sets that compute a DNC function.

:::solution
With $X = \emptyset$, $A$ is $\Delta^0_2$, so it is the limit set of a computable stable coloring $f$, with $f(\{x, y\}) = A_y(x)$ for an approximation $A_s$ (:ref{to="ramsey-theorem/stable-colorings"}). An infinite homogeneous set is contained in $A$ or in $\overline A$ by item 1 of :ref{#prop-srt-d22}, so it computes a DNC function.
:::
::::

## Notes and references

:ref{#thm-srt22-not-coh} is due to Monin and Patey; the first version of their paper (arXiv 2019) was entitled *SRT²₂ does not imply COH in ω-models*, and the published version *SRT²₂ does not imply RT²₂ in ω-models*. The non-standard model of $\mathsf{SRT}^2_2$ without $\mathsf{COH}$ is due to Chong, Slaman and Yang (2014). :ref{#prop-bi-immune-dnc} is due to Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008), in the form given in the section *Jump DNC avoidance* of the chapter *Jump compactness avoidance* of Patey's monograph, where :ref{#qu-d22-jump-dnc} is stated as open. Dzhafarov and Mummert tell the history of the problem whether $\mathsf{SRT}^2_2$ implies $\mathsf{RT}^2_2$ in §8.8.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- C. T. Chong, T. A. Slaman and Y. Yang, *The metamathematics of stable Ramsey's theorem for pairs*, Journal of the American Mathematical Society 27 (2014), 863–892.
- D. R. Hirschfeldt, C. G. Jockusch, Jr., B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, §8.8.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, sections *Pigeonhole principle* and *Jump DNC avoidance*.
