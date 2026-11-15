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

  The ideal can be taken to be a Scott ideal (:ref{#ex-wkl-srt22-no-coh}), and a Scott ideal can omit $\mathsf{RT}^2_2$; here $\mathsf{RT}^2_2$ is excluded by cohesiveness.
:::

::::exercise{#ex-wkl-srt22-no-coh difficulty=2 objective="Combine jump PA avoidance for weak König's lemma and for stable Ramsey's theorem into one ω-model without cohesiveness." lessons="jump-pa-avoidance"}
Show that there is an ω-model of $\mathsf{WKL}_0 + \mathsf{SRT}^2_2$ that is not a model of $\mathsf{COH}$.

:::solution
$\mathsf{WKL}$ admits jump PA avoidance by the low basis theorem relativized (item 1 of :ref{#ex-jump-pa-problems}), and $\mathsf{SRT}^2_2$ by :ref{#cor-srt22-jump-pa}. By :ref{#ex-jump-pa-product}, the problem whose instances are pairs of an instance of $\mathsf{WKL}$ and an instance of $\mathsf{SRT}^2_2$ admits jump PA avoidance. By :ref{#prop-jump-pa-model}, there is a Turing ideal satisfying it, hence both problems, in which no jump is PA relative to $\emptyset'$; it does not satisfy $\mathsf{COH}$.
:::
::::

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

The question is stated in Patey's monograph, where it is observed that the natural approach, a countable version of the product classes of this course with countably many slices, fails because largeness for infinite products does not behave as for finite ones. If $\mathsf D^2_2$ admitted jump DNC avoidance, which would in particular answer the question negatively, some ω-model of $\mathsf{SRT}^2_2$ would not satisfy the rainbow Ramsey theorem for pairs: by a theorem of J. Miller (:ref{#ex-miller-rainbow}), some computable coloring of pairs in which each color is used at most twice has only infinite rainbows (sets on which the coloring is injective) that compute a function DNC relative to $\emptyset'$.

:::quiz[jump DNC avoidance]
In the proof of :ref{#prop-bi-immune-dnc}, why are $3e + 2$ elements of $W^X_e$ required?

- [x] Because before stage $e$ at most $e + 2e = 3e$ values of $A$ are defined, so among $3e + 2$ elements two are still free, and they can be put on different sides.
- [ ] Because $H$ must have more than $3e$ elements.

  $H$ is infinite; the bound concerns $W^X_e$.
- [ ] Because the oracle $X'$ can only test sizes of the form $3e + 2$.

  $X'$ decides "$|W^X_e| \geq k$" for every $k$.
:::

## Notes and references

:ref{#thm-srt22-not-coh} is due to Monin and Patey; the first version of their paper (arXiv 2019) was entitled *SRT²₂ does not imply COH in ω-models*, and the published version *SRT²₂ does not imply RT²₂ in ω-models*. The non-standard model of $\mathsf{SRT}^2_2$ without $\mathsf{COH}$ is due to Chong, Slaman and Yang (2014). :ref{#prop-bi-immune-dnc} is due to Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008), in the form given in the section *Jump DNC avoidance* of the chapter *Jump compactness avoidance* of Patey's monograph, where :ref{#qu-d22-jump-dnc} is stated as open. Dzhafarov and Mummert tell the history of the problem whether $\mathsf{SRT}^2_2$ implies $\mathsf{RT}^2_2$ in §8.8.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- C. T. Chong, T. A. Slaman and Y. Yang, *The metamathematics of stable Ramsey's theorem for pairs*, Journal of the American Mathematical Society 27 (2014), 863–892.
- D. R. Hirschfeldt, C. G. Jockusch, Jr., B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, §8.8.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, sections *Pigeonhole principle* and *Jump DNC avoidance*.

:::::exercises
::::exercise{#ex-stable-dnc difficulty=1 objective="Translate the bi-immune construction into a computable stable coloring whose homogeneous sets compute DNC functions."}
Deduce from :ref{#prop-bi-immune-dnc} that some computable stable coloring of pairs has only infinite homogeneous sets that compute a DNC function.

:::solution
With $X = \emptyset$, $A$ is $\Delta^0_2$, so it is the limit set of a computable stable coloring $f$, with $f(\{x, y\}) = A_y(x)$ for an approximation $A_s$ (:ref{to="ramsey-theorem/stable-colorings"}). An infinite homogeneous set is contained in $A$ or in $\overline A$ by item 1 of :ref{#prop-srt-d22}, so it computes a DNC function.
:::
::::

::::exercise{#ex-dnc-basic-facts difficulty=1 objective="Check the basic facts on DNC functions relative to a jump, and place cohesiveness and weak König's lemma with respect to jump DNC avoidance."}
1. Show that a $\{0, 1\}$-valued function $g$ with $g(x) \neq J^{D'}(x)$ whenever $J^{D'}(x)$ is defined is DNC relative to $D'$.
2. Show that no set $D'$ computes a function DNC relative to $D'$; in particular the hypothesis of jump DNC avoidance holds for $Z = D$.
3. Show that $\mathsf{COH}$ does not admit jump DNC avoidance.
4. Show that $\mathsf{WKL}$ admits jump DNC avoidance.

:::solution
1. Let $x$ be such that $\Phi^{D'}_x(x)$ converges. If its value is $0$ or $1$, it is $J^{D'}(x)$, and $g(x)$ differs from it. Otherwise $g(x) \in \{0, 1\}$ differs from it as well.
2. If $\Phi^{D'}_e$ were a total function DNC relative to $D'$, then $\Phi^{D'}_e(e)$ would converge and differ from itself.
3. Take $D = Z = \emptyset$; the hypothesis holds by item 2. For the computable sequence $\vec R$ of :ref{#prop-coh-no-low}, the jump of every $\vec R$-cohesive set is PA relative to $\emptyset'$, hence computes a function DNC relative to $\emptyset'$ by item 1.
4. Let $D \leq_T Z$ with $Z'$ computing no function DNC relative to $D'$, and $T \leq_T Z$ an infinite binary tree. By the low basis theorem relativized to $Z$, $T$ has a path $Y$ with $(Z \oplus Y)' \leq_T Z'$, and a function computable in $(Z \oplus Y)'$ is computable in $Z'$.
:::
::::

::::exercise{#ex-srt2k-jump-pa difficulty=2 objective="Extend jump PA avoidance from stable Ramsey's theorem for two colors to finitely many colors." lessons="delta2-jump-pa, ramsey-theorem/stable-colorings"}
A coloring $f : [\nat]^2 \to k$ is **stable** if $\lim_y f(\{x, y\})$ exists for every $x$. Show that the problem $\mathsf{SRT}^2_k$, whose instances are the stable colorings $f : [\nat]^2 \to k$ and whose solutions are the infinite homogeneous sets, admits jump PA avoidance. Use :ref{#ex-d2k-jump-pa}.

:::solution
Let $D \leq_T Z$ with $Z'$ not PA relative to $D'$, and $f \leq_T Z$ a stable coloring with $k$ colors. For $c < k$, let $A_c = \{ x : \lim_y f(\{x, y\}) = c \}$. The sets $A_c$ partition $\nat$. Each is $\Sigma^0_2(Z)$, as "$\exists s\ \forall y > s\ f(\{x, y\}) = c$", and its complement is the union of the other $A_{c'}$, also $\Sigma^0_2(Z)$; so each is $\Delta^0_2(Z)$. By :ref{#ex-d2k-jump-pa}, there are $c$ and an infinite $H \subseteq A_c$ with $(Z \oplus H)'$ not PA relative to $D'$.

The set $f \oplus H$ computes an infinite homogeneous set $L = \{ x_0 < x_1 < \cdots \}$: let $x_0 = \min H$, and let $x_{n+1}$ be the least element of $H$ larger than $x_n$ with $f(\{x_i, x_{n+1}\}) = c$ for every $i \leq n$. It exists, since each $x_i \in A_c$ satisfies $f(\{x_i, y\}) = c$ for almost all $y$, and $H$ is infinite. Every pair $x_i < x_{n+1}$ has color $c$, so $L$ is homogeneous. Since $f \leq_T Z$, $Z \oplus L \leq_T Z \oplus H$ and $(Z \oplus L)'$ is not PA relative to $D'$.
:::
::::

::::exercise[Miller]{#ex-miller-rainbow difficulty=3 objective="Build a computable $2$-bounded coloring of pairs all of whose infinite rainbows compute a function DNC relative to $\emptyset'$, by approximating the $\emptyset'$-c.e. sets." lessons="immunity-growth/dnc-functions"}
A coloring $f : [\nat]^2 \to \nat$ is **$2$-bounded** if each color is used at most twice, and a set $R$ is an **$f$-rainbow** if $f$ is injective on $[R]^2$. Build a computable $2$-bounded coloring $f$ such that for every $e$, if $W^{\emptyset'}_e$ has at least $2e + 2$ elements, then $W^{\emptyset'}_e$ is contained in no infinite $f$-rainbow. Deduce that every infinite $f$-rainbow computes a function DNC relative to $\emptyset'$.

:::solution
*Approximations.* Let $\emptyset'_s$ be the finite set of numbers enumerated in $\emptyset'$ by stage $s$, and write $W^{\emptyset'}_e$ for the domain of $\Phi^{\emptyset'}_e$. We use the convention that a computation of at most $t$ steps queries its oracle only below $t$. For $x \in W^{\emptyset'}_e$, let $t_x$ be the least $t$ such that $\Phi^{\emptyset'}_{e, t}(x)$ converges in $t$ steps, and order $W^{\emptyset'}_e$ by the pairs $(t_x, x)$ lexicographically. If $|W^{\emptyset'}_e| \geq 2e + 2$, let $F_e$ be the set of its first $2e + 2$ elements in this order. At stage $s$, compute in the same way, with the oracle $\emptyset'_s$ and only for $x < s$ and $t < s$, the pairs $(t, x)$ with $t$ least such that $\Phi^{\emptyset'_s}_{e, t}(x)$ converges; if there are at least $2e + 2$ of them, let $F_{e, s}$ be the set of the first $2e + 2$ numbers $x$ in this order, and otherwise leave $F_{e, s}$ undefined. This is computable in $e$ and $s$.

If $|W^{\emptyset'}_e| \geq 2e + 2$, then $F_{e, s} = F_e$ for all large $s$. Let $t^*$ be the largest $t_x$ for $x \in F_e$, and take $s_0 > \max(t^*, \max F_e)$ such that $\emptyset'_s$ and $\emptyset'$ agree below $t^*$ for $s \geq s_0$. For such $s$, every computation of at most $t^*$ steps gives the same result with the two oracles, so the pairs $(t, x)$ with $t \leq t^*$ and $x < s$ are the same at stage $s$ and in the true order. The first $2e + 2$ true pairs have $t \leq t^*$ and $x < s$; a pair of stage $s$ preceding the last of them has $t \leq t^*$, so it is a true pair and precedes it in the true order. So the first $2e + 2$ pairs are the same.

*Construction.* At stage $s \geq 1$, define $f(\{x, s\})$ for all $x < s$. For $e = 0, 1, \dots, s - 1$ in turn, if $F_{e, s}$ is defined, let $x^e_0 < x^e_1$ be the two least elements of $F_{e, s}$ not chosen for some $e' < e$ at this stage; they exist, since $F_{e, s}$ has $2e + 2$ elements and at most $2e$ have been chosen. Give $\{x^e_0, s\}$ and $\{x^e_1, s\}$ the same new color, not used before. Then give every other pair $\{x, s\}$ with $x < s$ its own new color. The coloring is computable, and each color is used at stage $s$ only, on at most two pairs: $f$ is $2$-bounded.

*Verification.* Let $R$ be an infinite $f$-rainbow and suppose $W^{\emptyset'}_e \subseteq R$ with $|W^{\emptyset'}_e| \geq 2e + 2$. Then $F_e \subseteq R$. Take $s \in R$ with $s \geq s_0$ and $s > e$. At stage $s$, $F_{e, s} = F_e$, so two elements $x^e_0 \neq x^e_1$ of $F_e$, both smaller than $s$, satisfy $f(\{x^e_0, s\}) = f(\{x^e_1, s\})$. The two pairs are distinct subsets of $R$, which contradicts injectivity. So $|W^{\emptyset'}_e| \leq 2e + 1$ whenever $W^{\emptyset'}_e \subseteq R$.

*DNC.* For a number $v$, let $D_v$ be the finite set with canonical index $v$. Let $g$ be a computable function such that $W^{\emptyset'}_{g(e)} = D_{\Phi^{\emptyset'}_e(e)}$ if $\Phi^{\emptyset'}_e(e)$ converges, and $W^{\emptyset'}_{g(e)} = \emptyset$ otherwise. Let $h(e)$ be the canonical index of the set of the first $2g(e) + 2$ elements of $R$; $h$ is computable in $R$. If $\Phi^{\emptyset'}_e(e)$ converged to $h(e)$, then $W^{\emptyset'}_{g(e)} = D_{h(e)}$ would be a subset of $R$ with $2g(e) + 2$ elements, which is excluded. So $h$ is DNC relative to $\emptyset'$. This is the argument of :ref{#thm-dnc-effectively-immune}, relativized to $\emptyset'$.

Adapted from an exercise of the section *Jump DNC avoidance* of the chapter *Jump compactness avoidance* of Patey's monograph, attributed there to J. Miller.
:::
::::

::::exercise{#ex-rrt22-jump-dnc difficulty=1 objective="Deduce from Miller's coloring that a problem with jump DNC avoidance does not imply the rainbow Ramsey theorem for pairs on ω-models." lessons="reducibilities/preservation"}
Let $\mathsf{RRT}^2_2$ be the problem whose instances are the $2$-bounded colorings $f : [\nat]^2 \to \nat$ and whose solutions are the infinite $f$-rainbows. Let $\mathsf P$ admit jump DNC avoidance. Using :ref{#ex-miller-rainbow}, show that some Turing ideal satisfies $\mathsf P$ but not $\mathsf{RRT}^2_2$.

:::solution
Let $\mathcal W$ be the class of sets $Y$ such that $Y'$ computes no function DNC relative to $\emptyset'$. It is closed downward, since $W \leq_T Y$ implies $W' \leq_T Y'$, and it contains $\emptyset$, since $\emptyset'$ computes no function DNC relative to $\emptyset'$ (item 2 of :ref{#ex-dnc-basic-facts}). With $D = \emptyset$, jump DNC avoidance says that $\mathsf P$ preserves $\mathcal W$: for $Z \in \mathcal W$ and an instance $X \leq_T Z$, there is a solution $Y$ with $Z \oplus Y \in \mathcal W$. By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf P$. The coloring $f$ of :ref{#ex-miller-rainbow} is computable, hence in $\mathcal I$. An infinite $f$-rainbow $R$ computes a function DNC relative to $\emptyset'$, and so does $R' \geq_T R$; so $R \notin \mathcal W$, and $\mathcal I$ contains no solution to $f$.
:::
::::
:::::
