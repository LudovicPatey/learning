---
title: Pigeons do not jump high
summary: The requirements of second-jump control for the pigeonhole principle follow from the three-case argument with the questions on two sides; a case distinction on validity and Lachlan's disjunction give an infinite subset, of the set or of its complement, whose jump avoids a given cone, and which is not high.
duration: 45
prerequisites: [pigeon-questions]
---

This lesson completes the proof of :ref{#thm-pigeons-non-high}, with the setting of :ref{to="jump-cone-avoidance/pigeonhole-forcing"} and the questions of :ref{to="jump-cone-avoidance/pigeon-questions"}. The construction is a decreasing sequence of conditions with tasks, as in :ref{#thm-seetapun-direct}. It distinguishes two cases: if some condition has an invalid side, the construction works on the other side alone; otherwise both sides stay valid, and Lachlan's disjunction chooses a side at the end.

## The proof of the theorem

We first show how the questions give the requirements. Let $h$ be the computable function such that "$\Phi^{G'}_e(x)\converge = v$" is equivalent to the $\Sigma^0_2$ sentence $\chi_{e,x,v} = \exists y\ \Phi^G_{h(e,x,v)}(y)\diverge$, for every set $G$ (:ref{to="jump-cone-avoidance/sigma2-questions"}). Its negation is the $\Pi^0_2$ sentence $\forall y\ \Phi^G_{h(e,x,v)}(y)\converge$.

:::lemma{#lem-pigeon-requirements}
Let $p$ be a condition.

1. For all $e_0, e_1$, there are an extension $q$ of $p$, a side $i$ and a number $x$ such that every member of side $i$ of $q$ satisfies $\chi_{e_i, x, 1 - C(x)}$, or $q$ promises $\neg\chi_{e_i, x, C(x)}$ on side $i$.
2. If side $1 - i$ of $p$ is invalid, then for every $e$ there are an extension $q$ of $p$ and a number $x$ such that every member of side $i$ of $q$ satisfies $\chi_{e, x, 1 - C(x)}$, or $q$ promises $\neg\chi_{e, x, C(x)}$ on side $i$.
:::

:::proof{of=lem-pigeon-requirements}
1. By item 3 of :ref{#lem-pigeon-disjunctive}, the set $U$ of pairs $(x, v) \in \nat \times \{0, 1\}$ with $p \mathrel{?{\vdash}} \chi_{e_0, x, v}(G_0) \vee \chi_{e_1, x, v}(G_1)$ is $\Sigma^0_1(Y)$ for some $Y \in \mathcal N$. If $(x, 1 - C(x)) \in U$ for some $x$, item 1 of :ref{#lem-pigeon-disjunctive} gives the first alternative. If $(x, C(x)) \notin U$ for some $x$, item 2 gives the second. Otherwise $U$ is the graph of $C$, and $C \leq_T Y \in \mathcal N$, which contradicts $C \notin \mathcal N$.
2. The same, with a witness $\mathcal V$ of invalidity of side $1 - i$ and :ref{#lem-pigeon-one-side}.
:::

This is the three-case argument of :ref{#thm-local-jump-cone}, with the sides of :ref{#lem-disjunctive-cone}. We now build the sets.

:::proof{of=thm-pigeons-non-high}
We first treat $Z = \emptyset$, with the setting of :ref{#lem-pigeon-setting}. There are two cases.

*Case A: some condition $p_0$ has an invalid side, say side $1 - i$.* By item 2 of :ref{#lem-valid-part}, side $1 - i$ is invalid in every extension of $p_0$, and so side $i$ is valid in every extension, by item 1. Build a sequence $p_0 \geq p_1 \geq \cdots$ of conditions, handling in turn, infinitely often each, the following tasks:

- extend the stem on side $i$, by item 4 of :ref{#lem-valid-part};
- for an index $e$, pass to an extension given by item 2 of :ref{#lem-pigeon-requirements};
- for a $\Pi^0_2$ sentence $\forall y\ \theta(y)$ and a number $m$: if the current condition promises $\forall y\ \theta(y)$ on side $i$, pass to an extension forcing $\theta(m)$ on side $i$, by :ref{#lem-pigeon-promise}; otherwise do nothing.

Let $G_i$ be the union of the stems on side $i$. It is infinite by the first task, contained in $A_i$, and a member of side $i$ of every $p_s$, as in the proof of :ref{#thm-seetapun-direct}. If $p_s$ promises $\forall y\ \theta(y)$ on side $i$, so does every later condition, and the third task, handled at a later step for each $m$, gives a condition forcing $\theta(m)$ on side $i$; so $G_i$ satisfies $\forall y\ \theta(y)$. For each $e$, the second task gives $s$ and $x$ such that $G_i$ satisfies $\chi_{e, x, 1 - C(x)}$, or $p_s$ promises $\neg\chi_{e, x, C(x)}$, and then $G_i$ satisfies $\neg\chi_{e, x, C(x)}$. In both cases $\Phi^{G_i'}_e(x) \neq C(x)$, as a divergence or as a wrong value. So $C \not\leq_T G_i'$, and $H = G_i$ works.

*Case B: every condition has both sides valid.* Start with $p_0 = (\varepsilon, \varepsilon, \nat)$, and handle in turn, infinitely often each: extending the stem on side $0$, and on side $1$; for a pair $(e_0, e_1)$, passing to an extension given by item 1 of :ref{#lem-pigeon-requirements}; for a side $j$, a $\Pi^0_2$ sentence and a number $m$, keeping promises on side $j$ as in case A. Both sides are valid throughout, so all tasks can be carried out. Let $G_0$ and $G_1$ be the unions of the stems. Both are infinite, $G_j \subseteq A_j$, and promises on either side are kept, as in case A. For every pair $(e_0, e_1)$, there is $j$ with $\Phi^{G_j'}_{e_j} \neq C$. This is Lachlan's disjunction, as in :ref{#lem-disjunctive-construction}: if $\Phi^{G_0'}_{e_0} = C$ for some $e_0$, then $\Phi^{G_1'}_{e_1} \neq C$ for every $e_1$, and $C \not\leq_T G_1'$; otherwise $C \not\leq_T G_0'$. Let $H$ be the corresponding $G_j$.

*The general case.* For a set $Z$ and $C \not\leq_T Z'$, take a Scott ideal $\mathcal M$ containing $Z$ with a code $M$ satisfying $M' \leq_T Z'$ (:ref{#cor-scott-codes}), and a Scott ideal $\mathcal N$ containing $Z'$ and not $C$ (:ref{#lem-scott-cone}). Then $M, M' \in \mathcal N$, and $\mathcal N$ contains a set PA relative to $Z' \geq_T M'$, which computes $S$. Use sentences about $Z \oplus G$ instead of $G$: the classes $\mathcal V_{\sigma, \varphi}$ become $\Sigma^0_1(Z)$ classes, and $Z \in \mathcal M$, so they are $\Sigma^0_1(\mathcal M)$ classes, and all the lemmas hold with the same proofs. The result is an infinite $H \subseteq A_0$ or $H \subseteq A_1$ with $C \not\leq_T (Z \oplus H)'$.
:::

:::figure[The structure of the proof of :ref{#thm-pigeons-non-high}. If some condition has an invalid side, every extension has the same invalid side, and the construction below it works on the other side alone, with the question of :ref{#def-pigeon-one-side}. Otherwise both sides stay valid, and the disjunctive question of :ref{#def-pigeon-disjunctive} satisfies the requirements on one side or the other; Lachlan's disjunction gives a side on which all of them hold.]
<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="The case split of the proof: if some condition has an invalid side, work on the other side with the question on one side; otherwise use the disjunctive question and Lachlan disjunction"><defs><marker id="jc-cs-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="170" y="8" width="260" height="40" rx="6" class="state"/><text x="300.0" y="24.0" text-anchor="middle" class="label">does some condition p₀</text><text x="300.0" y="40.0" text-anchor="middle" class="label">have an invalid side 1 − i?</text><rect x="20" y="92" width="260" height="54" rx="6" class="node"/><text x="150.0" y="107.0" text-anchor="middle" class="label">case A: work below p₀</text><text x="150.0" y="123.0" text-anchor="middle" class="label">side i valid in every extension</text><text x="150.0" y="139.0" text-anchor="middle" class="label">question on side i with a witness 𝒱</text><rect x="320" y="92" width="260" height="54" rx="6" class="node"/><text x="450.0" y="107.0" text-anchor="middle" class="label">case B: both sides always valid</text><text x="450.0" y="123.0" text-anchor="middle" class="label">disjunctive question</text><text x="450.0" y="139.0" text-anchor="middle" class="label">requirements on side 0 or side 1</text><rect x="20" y="196" width="260" height="48" rx="6" class="state"/><text x="150.0" y="216.0" text-anchor="middle" class="label">the stems on side i give an infinite</text><text x="150.0" y="232.0" text-anchor="middle" class="label">subset G of Aᵢ with C ≰ G′</text><rect x="320" y="196" width="260" height="48" rx="6" class="state"/><text x="450.0" y="216.0" text-anchor="middle" class="label">Lachlan’s disjunction: G₀ ⊆ A₀ with C ≰ G₀′</text><text x="450.0" y="232.0" text-anchor="middle" class="label">or G₁ ⊆ A₁ with C ≰ G₁′</text><line x1="260" y1="50" x2="160" y2="88" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><line x1="340" y1="50" x2="440" y2="88" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><line x1="150" y1="148" x2="150" y2="192" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><line x1="450" y1="148" x2="450" y2="192" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><text x="200" y="74" text-anchor="end" class="label">yes</text><text x="400" y="74" class="label">no</text></svg>
:::

:::quiz[the construction]
In case A, why is it essential that side $i$ is valid in every extension of $p_0$?

- [x] Because promises turn into truth only through :ref{#lem-pigeon-promise}, which requires the side to be valid when the instance is handled; validity throughout makes every promise on side $i$ kept.
- [ ] Because the question of :ref{#def-pigeon-one-side} requires side $i$ to be valid.

  It requires a witness of invalidity of side $1 - i$; validity of side $i$ follows.
- [ ] Because otherwise $G_i$ would not be contained in $A_i$.

  The stems on side $i$ are always subsets of $A_i$.

---

Why can case B not use :ref{#lem-pigeon-one-side}?

- [x] Because in case B no side of any condition is invalid, so there is no witness of invalidity; the requirements must be disjunctive, and the side is chosen by the disjunctive question.
- [ ] Because :ref{#lem-pigeon-one-side} only applies to side $0$.

  It applies to either side, given a witness for the other.
- [ ] Because in case B the sets $G_0$ and $G_1$ are finite.

  Both are infinite in case B.

---

Where is the hypothesis $C \not\leq_T \emptyset'$ used?

- [x] Only in the choice of $\mathcal N$, a Scott ideal containing $\emptyset'$ and not $C$; the third case of :ref{#lem-pigeon-requirements} contradicts $C \notin \mathcal N$.
- [ ] In the choice of the low code $M$.

  $M$ exists for every $C$.
- [ ] In the construction of $S$.

  $S$ is computed by a set PA relative to $\emptyset'$, whatever $C$ is.
:::

:::corollary{#cor-pigeons-non-high}
Every set $A$ has an infinite subset $H$, of $A$ or of $\overline A$, that is not high. More generally, for every $Z$, $H$ can be chosen not high relative to $Z$.
:::

:::proof{of=cor-pigeons-non-high}
Apply :ref{#thm-pigeons-non-high} with $C = Z''$, which is not computable in $Z'$.
:::

By :ref{#ex-no-low2-subset}, "not high" cannot be improved to "low₂" for arbitrary sets $A$, and by :ref{#thm-dhls} not to "low" for $\Delta^0_2$ sets. For $\Delta^0_3$ sets, Monin and Patey proved that low₃ solutions exist, the analogue one level up of the theorem of Cholak, Jockusch and Slaman for $\Delta^0_2$ sets; the proof is beyond this course.

## Exercises

::::exercise{difficulty=1}
Show that if $A$ is finite, side $0$ of every condition is invalid, and side $1$ of every condition is valid.

:::solution
If $A$ is finite, $X \cap A_0$ is finite, so it is not in $\mathcal U$, whose members are infinite. By item 1 of :ref{#lem-valid-part}, side $1$ is valid.
:::
::::

::::exercise{difficulty=2}
Suppose that $A \in \mathcal M$, for instance $A$ computable. Show that there is $i < 2$ such that side $i$ of every condition is valid and side $1 - i$ of every condition is invalid.

:::solution
Since $\mathcal U_S$ is $\mathcal M$-cohesive and $A \in \mathcal M$, $\mathcal U_S \subseteq \mathcal L_{A_0}$ or $\mathcal U_S \subseteq \mathcal L_{A_1}$; let $i$ be such that $\mathcal U_S \subseteq \mathcal L_{A_i}$. For every condition with reservoir $X$, the set $X \cap A_{1-i}$ has an empty intersection with $A_i$, so it is not in $\mathcal L_{A_i} \supseteq \mathcal U$: side $1 - i$ is invalid. By item 1 of :ref{#lem-valid-part}, side $i$ is valid. So for simple instances the construction is degenerate: everything happens on one side, as it should, since $A_i$ is then an infinite subset of $A_i$ in $\mathcal M$.
:::
::::

::::exercise{difficulty=2}
Deduce from :ref{#thm-pigeons-non-high} and :ref{#thm-coh-weakly-low} that $\mathsf{RT}^2_2$ admits jump cone avoidance, without using :ref{#thm-rt22-weakly-low}.

:::solution
Let $Z$ be a set, $C \not\leq_T Z'$, and $f$ a $Z$-computable coloring of pairs. The sequence $R_x = \{ y : f(\{x, y\}) = 1 \}$ is $Z$-computable. By :ref{#thm-coh-weakly-low} and item 3 of :ref{#prop-weakly-low-properties}, it has a cohesive set $G$ with $C \not\leq_T (Z \oplus G)'$. Let $p$ enumerate $G$ in increasing order, and $g(\{a, b\}) = f(\{p(a), p(b)\})$; it is stable by :ref{#thm-rt22-decomposition}, and computable in $Z \oplus G$. By :ref{#thm-pigeons-non-high} with $Z \oplus G$ in place of $Z$, applied to the limit set $A_g$, there is an infinite $K$ contained in $A_g$ or in its complement with $C \not\leq_T (Z \oplus G \oplus K)'$. By item 2 of :ref{#prop-srt-d22}, $g \oplus K$ computes an infinite homogeneous set $L$ for $g$, and $H = p[L]$ is homogeneous for $f$ and computable in $Z \oplus G \oplus K$. So $(Z \oplus H)' \leq_T (Z \oplus G \oplus K)'$, and $C \not\leq_T (Z \oplus H)'$.
:::
::::

::::exercise{difficulty=3}
Let $f$ be a function hyperimmune relative to $\emptyset'$. Show that every set $A$ has an infinite subset $H$, of $A$ or of $\overline A$, such that $f$ is hyperimmune relative to $H'$.

:::solution
Follow the proof of :ref{#thm-pigeons-non-high}, with the requirement "$\Phi^{G'}_e$ is partial, or $\Phi^{G'}_e(m) < f(m)$ for some $m$" in place of "$\Phi^{G'}_e \neq C$", and the sentences "$\Phi^{G'}_e(m)\converge$" and "$\Phi^{G'}_e(m)\converge < b$" written as in the exercise of :ref{to="jump-cone-avoidance/sigma2-questions"}.

*Compactness.* The question $\tau \mathrel{?{\vdash}} \varphi$ depends only on the strings satisfying $\varphi$, so for $k < b$ the formulas $\psi^b_m(k, y)$ and $\psi_m(k, y)$ give the same answers. If the question on one side holds for "$\Phi^{G'}_e(m)\converge$", the class $\mathcal C$ of the proof of :ref{#lem-pigeon-one-side} is empty; its complement is covered by open sets, each given by a finite part of $B$ together with a witness $\tau$, $\langle k, y \rangle$, or with a finite part of $B^{1-i}$ in $\mathcal V$. By compactness of Cantor space, finitely many of them suffice, and for $b$ larger than the numbers $k$ involved, the question holds for "$\Phi^{G'}_e(m)\converge < b$". The same holds for the disjunctive question.

*Choice of $\mathcal N$.* Let $Z_0 = \emptyset'$ and $Z_{n+1} = Z_n \oplus P_n$, where $P_n$ is PA relative to $Z_n$ and every $(Z_n \oplus P_n)$-computable function is dominated by a $Z_n$-computable one: apply :ref{#thm-dominated-basis}, relativized to $Z_n$, to the class of $\{0,1\}$-valued functions DNC relative to $Z_n$. The sets computable in some $Z_n$ form a Scott ideal $\mathcal N$ containing $\emptyset'$ (:ref{#prop-wkl-scott}), and by induction every function computable in a member of $\mathcal N$ is dominated by a $\emptyset'$-computable function, so it does not dominate $f$. The rest of :ref{#lem-pigeon-setting} is unchanged, with $S$ computed by $P_0$.

*Requirements.* In case A, given a condition and $e$, let $g(m)$ be the first $b$ found with a positive answer of the question on side $i$ for "$\Phi^{G'}_e(m)\converge < b$"; it is partial computable in a member of $\mathcal N$, by item 3 of :ref{#lem-pigeon-one-side}. If $g(m)$ is undefined, the question for "$\Phi^{G'}_e(m)\converge$" is negative by compactness, and an extension promises $\Phi^{G'}_e(m)\diverge$ on side $i$. If $g$ is total, then $f(m) > g(m)$ for some $m$, and an extension has all its members of side $i$ satisfying $\Phi^{G'}_e(m)\converge < g(m)$. In case B, use pairs $(e_0, e_1)$, the disjunctive question for "$\Phi^{G_0'}_{e_0}(m)\converge < b$" and "$\Phi^{G_1'}_{e_1}(m)\converge < b$", and Lachlan's disjunction. Promises are kept as in the proof, so for the resulting set $H$, no $H'$-computable function dominates $f$.
:::
::::

## Notes and references

:ref{#thm-pigeons-non-high} and :ref{#cor-pigeons-non-high} are due to Monin and Patey (2019); the same paper proves low₃ solutions for $\Delta^0_3$ sets and gives a simpler proof of Liu's theorem that every set has an infinite subset, of itself or of its complement, of non-PA degree. The proof given here follows the section *Pigeonhole principle* of the chapter *Jump cone avoidance* of Patey's monograph, with the cohesive classes of Le Houérou, Levy Patey and Mimouni (2024), including the case distinction on validity. The construction by sequences of conditions with tasks, instead of sufficiently generic filters, is written here, so that promises are turned into truth explicitly. The exercise on hyperimmunity is stated in the monograph, after Monin and Patey (2019).

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- B. Monin and L. Patey, *The weakness of the pigeonhole principle under hyperarithmetical reductions*, arXiv:1905.08425 (2019).
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Pigeonhole principle*.