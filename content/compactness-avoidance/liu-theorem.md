---
title: Liu's theorem
summary: The pigeonhole principle admits strong PA avoidance, by a disjunctive forcing question whose negative answers are realized with the Ramsey-type weak König lemma instead of a Scott ideal; Ramsey's theorem for pairs admits PA avoidance, and does not imply weak König's lemma.
duration: 45
prerequisites: [rwkl-pa-avoidance, pa-avoidance-examples, ramsey-theorem/seetapun]
---

Seetapun's theorem decomposes a coloring of pairs into a cohesive set and an instance of the pigeonhole principle (:ref{#thm-seetapun}). Liu's theorem follows the same plan for PA degrees. Cohesiveness admits PA avoidance (:ref{#thm-coh-pa-avoidance}); what remains is the strong PA avoidance of the pigeonhole principle, where the previous lessons are used: a disjunctive forcing question that is weakly merging (:ref{#lem-disjunctive-pa}), whose negative answers are realized, not by choosing a partition in a Scott ideal, but by the Ramsey-type weak König lemma (:ref{#thm-rwkl-pa-avoidance}).

:::figure[The structure of the proof of :ref{#thm-liu-rt22}. The upper row is the decomposition of the proof of Seetapun's theorem; the lower row shows the ingredients of the strong PA avoidance of the pigeonhole principle.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Structure of the proof of Liu theorem: a computable coloring of pairs, a cohesive set by PA avoidance of COH, a stable coloring and its limit set, an infinite subset of the limit set or its complement by strong PA avoidance of the pigeonhole principle, which uses the Ramsey-type weak Konig lemma and Liu lemma, and finally a homogeneous set"><defs><marker id="ca-st-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="20" y="20" width="170" height="46" rx="6" class="state"/><text x="105.0" y="39.0" text-anchor="middle" class="label">f : [ℕ]² → 2</text><text x="105.0" y="55.0" text-anchor="middle" class="label">computable in Z</text><rect x="215" y="20" width="170" height="46" rx="6" class="state"/><text x="300.0" y="39.0" text-anchor="middle" class="label">cohesive set G</text><text x="300.0" y="55.0" text-anchor="middle" class="label">COH, PA avoidance</text><rect x="410" y="20" width="170" height="46" rx="6" class="state"/><text x="495.0" y="39.0" text-anchor="middle" class="label">limit set of the</text><text x="495.0" y="55.0" text-anchor="middle" class="label">stable coloring on G</text><rect x="410" y="126" width="170" height="46" rx="6" class="state"/><text x="495.0" y="145.0" text-anchor="middle" class="label">K ⊆ limit set or its</text><text x="495.0" y="161.0" text-anchor="middle" class="label">complement: RT¹₂ strong</text><rect x="410" y="232" width="170" height="46" rx="6" class="state"/><text x="495.0" y="251.0" text-anchor="middle" class="label">homogeneous set H</text><text x="495.0" y="267.0" text-anchor="middle" class="label">Z ⊕ H not PA over D</text><rect x="150" y="126" width="200" height="46" rx="6" class="cell"/><text x="250.0" y="145.0" text-anchor="middle" class="label">weakly merging question</text><text x="250.0" y="161.0" text-anchor="middle" class="label">for RT¹₂ (Liu forcing)</text><rect x="20" y="232" width="170" height="46" rx="6" class="cell"/><text x="105.0" y="251.0" text-anchor="middle" class="label">RWKL avoids PA</text><text x="105.0" y="267.0" text-anchor="middle" class="label">(partition forcing)</text><rect x="215" y="232" width="170" height="46" rx="6" class="cell"/><text x="300.0" y="251.0" text-anchor="middle" class="label">Liu's lemma</text><text x="300.0" y="267.0" text-anchor="middle" class="label">on valuations</text><line x1="192" y1="43" x2="211" y2="43" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="387" y1="43" x2="406" y2="43" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="495" y1="68" x2="495" y2="122" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="495" y1="174" x2="495" y2="228" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="352" y1="149" x2="406" y2="149" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="105" y1="230" x2="200" y2="176" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="300" y1="230" x2="270" y2="176" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-st-arr)"/><line x1="213" y1="255" x2="194" y2="255" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ca-st-arr)"/><text x="300" y="104" text-anchor="middle" class="label">each step keeps Z ⊕ (sets built) not PA relative to D</text><text x="202" y="292" text-anchor="middle" class="label muted">dashed: RWKL avoidance uses Liu's lemma too</text></svg>
:::

Throughout the lesson, $D \leq_T Z$ are sets such that $Z$ is not PA relative to $D$, and $\mathcal M$ is the class of the sets $Z \oplus X$ that are not PA relative to $D$. Every member of $\mathcal M$ computes $D$.

## The pigeonhole principle

Fix a set $A$, with $A^0 = A$ and $A^1 = \overline A$. A function $B : \nat \to 2$ is a partition with parts $B^{-1}(i)$.

:::definition{#def-liu-forcing}
A **Liu condition** is a triple $(\sigma_0, \sigma_1, X)$ where $X$ is an infinite set with $\min X \geq |\sigma_0|, |\sigma_1|$ and $Z \oplus X \in \mathcal M$, and $\sigma_i \subseteq A^i$ for each $i < 2$. Extension is as for the Dzhafarov–Jockusch conditions: $(\tau_0, \tau_1, Y) \leq (\sigma_0, \sigma_1, X)$ if $(\tau_i, Y)$ extends $(\sigma_i, X)$ as a Mathias condition for each $i$. The members of side $i$ are the members of the Mathias condition $(\sigma_i, X)$. For $\Sigma^0_1$ sentences $\varphi_0, \varphi_1$, let $(\sigma_0, \sigma_1, X) \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if for every $B : \nat \to 2$ there are $i < 2$ and a string $\tau$ compatible with $(\sigma_i, X \cap B^{-1}(i))$ satisfying $\varphi_i$.
:::

The only difference with the Dzhafarov–Jockusch forcing (:ref{#ex-dj-weakly-merging}) is the class of the reservoirs: sets $X$ with $Z \oplus X$ not PA relative to $D$, instead of the members of a Scott ideal. Removing finitely many elements from a reservoir does not change its degree, so this is a disjunctive notion of forcing (:ref{#def-disjunctive-notion}).

:::lemma{#lem-liu-question}
The relation of :ref{#def-liu-forcing} is a $\Sigma^0_1(\mathcal M)$-preserving disjunctive forcing question, and it is weakly merging with $k = 3$ for every condition.
:::

:::proof{of=lem-liu-question}
Let $c = (\sigma_0, \sigma_1, X)$.

*Preservation.* The functions $B$ for which the definition fails form a $\Pi^0_1(Z \oplus X)$ class. By compactness, $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if and only if this class is empty, a $\Sigma^0_1(Z \oplus X)$ property, uniformly in the formulas (first exercise of :ref{to="avoidance/disjunctive-question"}); and $Z \oplus X \in \mathcal M$.

*Property 1.* Apply the definition to the function $B$ with $B^{-1}(i) = A^i$. There are $i$ and $\tau$ compatible with $(\sigma_i, X \cap A^i)$ satisfying $\varphi_i$. The new elements of $\tau$ lie in $A^i$, so $(\sigma_0, \sigma_1, X)$ with $\sigma_i$ replaced by $\tau$ and $X$ by $X \setminus [0, |\tau|)$ is a condition; all its members of side $i$ extend $\tau$, hence satisfy $\varphi_i$.

*Weak merging.* Suppose that the answer is negative for three pairs $(\varphi^s_0, \varphi^s_1)$, $s < 3$. For each $s$, the class $\mathcal P_s$ of the functions $B$ such that, for both $i < 2$, no string compatible with $(\sigma_i, X \cap B^{-1}(i))$ satisfies $\varphi^s_i$, is a non-empty $\Pi^0_1(Z \oplus X)$ class. Apply :ref{#exr-rwkl-subset} three times. With the oracle $W_0 = Z \oplus X$, which computes $D$ and is not PA relative to $D$, and the set $X \leq_T W_0$, there are $B_0 \in \mathcal P_0$, a color $i_0$ and an infinite $H_0 \subseteq X \cap B_0^{-1}(i_0)$ such that $W_1 = W_0 \oplus H_0$ is not PA relative to $D$. With $W_1$, the class $\mathcal P_1$ and the set $H_0$, there are $B_1$, $i_1$ and an infinite $H_1 \subseteq H_0 \cap B_1^{-1}(i_1)$ with $W_2 = W_1 \oplus H_1$ not PA relative to $D$; and similarly $H_2 \subseteq H_1 \cap B_2^{-1}(i_2)$ with $W_2 \oplus H_2$ not PA relative to $D$. Since $Z \oplus H_2 \leq_T W_2 \oplus H_2$, the triple $d = (\sigma_0, \sigma_1, H_2)$ is a condition, and it extends $c$.

Two of the colors $i_0, i_1, i_2$ coincide: $i_s = i_t = i$ with $s < t$. Let $G$ be a member of side $i$ of $d$. If $G$ satisfied $\varphi^s_i$, some prefix $\tau$ of $G$ would satisfy it, by the use principle, and $\tau$ would be compatible with $(\sigma_i, H_2)$, hence with $(\sigma_i, X \cap B_s^{-1}(i))$, since $H_2 \subseteq H_s \subseteq X \cap B_s^{-1}(i)$. This contradicts $B_s \in \mathcal P_s$. The same holds for $t$. So $d \Vdash \neg \varphi^s_i(G_i) \wedge \neg \varphi^t_i(G_i)$.

*Property 2.* The same argument with a single negative answer gives $d \leq c$ and $i$ with $d \Vdash \neg \varphi_i(G_i)$.
:::

Compared with :ref{#ex-dj-weakly-merging}, no partition is chosen: for each $s$, the new reservoir is only known to lie on one side of some member of $\mathcal P_s$, which is what $\mathsf{RWKL}$ provides while avoiding PA degrees.

:::quiz[the Liu question]
In the proof of :ref{#lem-liu-question}, why is the homogeneous set $H_1$ taken inside $H_0$, rather than inside $X$?

- [x] Because the final reservoir must lie on side $i_s$ of a member of $\mathcal P_s$ for each of the three values of $s$ at once; nesting the sets keeps the earlier properties.
- [ ] Because $H_0$ is computable in $Z$.

  $H_0$ is not computable in $Z$ in general; it is added to the oracle.
- [ ] Because $\mathcal P_1 \subseteq \mathcal P_0$.

  The classes come from different pairs of sentences.

---

Why is the oracle increased at each step, from $W_0$ to $W_1$ and $W_2$?

- [x] Because the next application of :ref{#thm-rwkl-pa-avoidance} must produce a set $H_{s+1}$ such that $W_{s+1} \oplus H_{s+1}$, and not only $Z \oplus H_{s+1}$, is not PA relative to $D$, and it needs $H_s$ to be computable in the oracle.
- [ ] Because the classes $\mathcal P_s$ are only $\Pi^0_1(W_s)$.

  All three classes are $\Pi^0_1(Z \oplus X)$; the oracle grows for the sets $H_s$.
- [ ] Because $D$ changes.

  $D$ is fixed throughout.
:::

:::theorem[Liu]{#thm-rt12-strong-pa}
For every set $A$, there is an infinite set $H$, contained in $A$ or in $\overline A$, such that $Z \oplus H$ is not PA relative to $D$. So $\mathsf{RT}^1_2$ admits strong PA avoidance.
:::

:::proof{of=thm-rt12-strong-pa}
If some infinite subset $H$ of $A^0$ or of $A^1$ has $Z \oplus H$ not PA relative to $D$, we are done. Assume from now on:

(H) for every infinite $H \subseteq A^0$ and every infinite $H \subseteq A^1$, $Z \oplus H$ is PA relative to $D$.

*Infinity.* Let $(\sigma_0, \sigma_1, X)$ be a condition and $i < 2$. The set $X \cap A^i$ is infinite: otherwise $X$ minus finitely many elements would be an infinite subset $H$ of $A^{1-i}$ with $Z \oplus H \equiv_T Z \oplus X$ not PA relative to $D$, contradicting (H). Adding to $\sigma_i$ an element $n \in X \cap A^i$ above a given bound, and removing from $X$ the numbers up to $n$, gives an extension.

*Requirements.* By :ref{#lem-liu-question}, :ref{#lem-disjunctive-pa} (1) applies: for every condition and every pair $(e_0, e_1)$, there are an extension $d$ and a side $i$ such that $\Phi^{Z \oplus G}_{e_i}$ is not $\mathrm{DNC}_2$ relative to $D$ for every member $G$ of side $i$ of $d$.

*Construction.* Starting from the condition $(\varepsilon, \varepsilon, \nat)$, build a sequence of conditions $c_0 \geq c_1 \geq \cdots$ that handles, in turn, the infinity of both sides above every bound and every pair $(e_0, e_1)$. The union $G_i$ of the stems of side $i$ is an infinite subset of $A^i$ and a member of side $i$ of every $c_s$. By :ref{#lem-disjunctive-pa} (2), $Z \oplus G_0$ or $Z \oplus G_1$ is not PA relative to $D$, contradicting (H). So the second case never happens, and the first case gives the theorem.
:::

The assumption (H) keeps both sides extendible, as in the proof of :ref{#thm-dj-cone-avoidance}. The disjunction "$G_0$ or $G_1$" cannot be avoided: for some sets $A$, only one of $A$ and $\overline A$ contains a non-PA solution.

:::quiz[strong PA avoidance of the pigeonhole principle]
In the proof of :ref{#thm-rt12-strong-pa}, where is the hypothesis that the reservoirs are not PA relative to $D$ used?

- [x] In :ref{#lem-disjunctive-pa}, through the third case of the density argument, which needs the oracle of the question to be a set not PA relative to $D$; and in the infinity step, through (H).
- [ ] In property 1 of the question.

  Property 1 uses the partition given by $A$, whatever the reservoir.
- [ ] To show that $G_i \subseteq A^i$.

  This comes from the definition of the conditions.
:::

## Ramsey's theorem for pairs

:::theorem[Liu]{#thm-liu-rt22}
$\mathsf{RT}^2_2$ admits PA avoidance: for all $D \leq_T Z$ with $Z$ not PA relative to $D$, every $Z$-computable coloring $f : [\nat]^2 \to 2$ has an infinite homogeneous set $H$ such that $Z \oplus H$ is not PA relative to $D$.
:::

:::proof{of=thm-liu-rt22}
The proof is that of :ref{#thm-seetapun}, with PA avoidance in place of cone avoidance. The sequence $R_x = \{ y : f(\{ x, y \}) = 1 \}$ is $Z$-computable. By :ref{#thm-coh-pa-avoidance}, it has a cohesive set $G$ with $Z \oplus G$ not PA relative to $D$. Let $p$ enumerate $G$ in increasing order, and $g(\{ i, j \}) = f(\{ p(i), p(j) \})$; it is a stable coloring (:ref{#thm-rt22-decomposition}), computable in $Z \oplus G$. By :ref{#thm-rt12-strong-pa} relative to $Z \oplus G$, which computes $D$ and is not PA relative to $D$, applied to the limit set $A_g$, there is an infinite set $K$ contained in $A_g$ or in its complement such that $Z \oplus G \oplus K$ is not PA relative to $D$. By :ref{#prop-srt-d22} (2), $g \oplus K$ computes an infinite homogeneous set $L$ for $g$, and $H = p[L]$ is homogeneous for $f$ and computable in $Z \oplus G \oplus K$. So $Z \oplus H$ is not PA relative to $D$.
:::

:::corollary[Liu]{#cor-rt22-not-wkl}
There is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ that is not a model of $\mathsf{WKL}_0$. In particular, $\mathsf{RT}^2_2$ does not imply $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$, and $\mathsf{WKL} \not\leq_\omega \mathsf{RT}^2_2$.
:::

:::proof{of=cor-rt22-not-wkl}
By :ref{#prop-pa-avoidance-model}, there is a Turing ideal satisfying $\mathsf{RT}^2_2$ and containing no PA set. The ω-model with this second-order part satisfies $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ but not $\mathsf{WKL}_0$, since it is not a Scott ideal (:ref{#prop-wkl-scott}). The last statement is :ref{#prop-pa-avoidance-model} (3).
:::

By :ref{#thm-pa-implies-cone}, the theorem gives Seetapun's theorem again. It answers the question, open since Seetapun's theorem, whether Ramsey's theorem for pairs implies weak König's lemma, as Ramsey's theorem for triples does; with :ref{#cor-wkl-not-rt22}, the two principles are incomparable over $\mathsf{RCA}_0$. Since $\mathsf{RT}^2_2$ implies $\mathsf{RWKL}$ (:ref{#prop-rwkl-reductions}), Ramsey's theorem for pairs contains a weak form of compactness, but not compactness itself. The remaining lessons ask whether it implies the existence of random sequences (:ref{to="compactness-avoidance/closed-classes"}) or of DNC functions (:ref{to="compactness-avoidance/rwwkl-dnc"}).

The theorem does not extend to strong PA avoidance: the coloring $h$ of the proof of :ref{#prop-rt32-jump} is a coloring of pairs, computable in $\emptyset'$, all of whose infinite homogeneous sets compute $\emptyset'$, which is PA (:ref{#ex-cone-avoidance-problems}).

:::quiz[Liu's theorem]
In the proof of :ref{#thm-liu-rt22}, why does the pigeonhole principle need to be applied in its strong form?

- [x] Because the limit set $A_g$ is $\Delta^0_2$ relative to $Z \oplus G$, not computable in it, so PA avoidance for $Z \oplus G$-computable instances would not apply.
- [ ] Because $g$ is not computable in $Z \oplus G$.

  $g$ is computable in $Z \oplus G$; its limit set is not.
- [ ] Because $G$ is PA relative to $D$.

  $Z \oplus G$ is not PA relative to $D$, by the choice of $G$.
:::

## Exercises

::::exercise{difficulty=2}
Show that $\mathsf{COH}$ admits strong PA avoidance, following the proof of :ref{#thm-coh-strong-cone}.

:::solution
Let $\vec R$ be an arbitrary sequence of sets. Use Mathias conditions $(\sigma, X)$ with $Z \oplus X$ not PA relative to $D$, and the question "some string compatible with $(\sigma, X)$ satisfies $\varphi$". It is $\Sigma^0_1(\mathcal M)$-preserving and merging, as in :ref{#thm-coh-pa-avoidance}. By :ref{#thm-local-pa-avoidance}, a sufficiently generic $G$ has $Z \oplus G$ not PA relative to $D$. For cohesiveness, given $(\sigma, X)$ and $n$, let $p$ enumerate $X$, and $A = \{ k : p(k) \in R_n \}$. By :ref{#thm-rt12-strong-pa} relative to $Z \oplus X$, there is an infinite $H$ contained in $A$ or $\overline A$ with $Z \oplus X \oplus H$ not PA relative to $D$; then $(\sigma, p[H])$ is a condition extending $(\sigma, X)$, all of whose members are almost contained in $R_n$ or in $\overline{R_n}$. Infinity is handled as usual.
:::
::::

::::exercise{difficulty=2}
Show that for every $\ell \geq 2$, $\mathsf{RT}^1_\ell$ admits strong PA avoidance, and $\mathsf{RT}^2_\ell$ admits PA avoidance.

:::solution
For $\mathsf{RT}^1_\ell$, by induction on $\ell$. Let $c : \nat \to \ell$ and $D \leq_T Z$ with $Z$ not PA relative to $D$. By :ref{#thm-rt12-strong-pa}, there is an infinite $H$ contained in $c^{-1}(\ell - 1)$ or in its complement, with $Z \oplus H$ not PA relative to $D$. In the first case we are done. In the second, let $p$ enumerate $H$; the coloring $c \circ p$ takes values in $\ell - 1$ colors, and the induction hypothesis relative to $Z \oplus H$ gives an infinite $K$ homogeneous for $c \circ p$ with $Z \oplus H \oplus K$ not PA relative to $D$; then $p[K]$ is homogeneous for $c$. For $\mathsf{RT}^2_\ell$, repeat the proof of :ref{#thm-liu-rt22} with a cohesive set for the sets $\{ y : f(\{ x, y \}) = j \}$, $x \in \nat$, $j < \ell$; on it the coloring is stable, and strong PA avoidance of $\mathsf{RT}^1_\ell$ applies to its limit coloring, followed by the thinning of :ref{#prop-srt-d22} (2).
:::
::::

## Notes and references

Liu (2012) proved that every computable coloring of pairs has an infinite homogeneous set of non-PA degree, solving what Hirschfeldt calls one of the major open questions of reverse mathematics (*Slicing the Truth*, Theorem 6.71, proved in the appendix of the book); Dzhafarov and Mummert state it as Theorem 8.6.1. Liu's original proof also goes through cohesiveness, and proves the strong PA avoidance of the pigeonhole principle with one notion of forcing that combines compactness and disjunction. The proof given here separates the two, as in the chapter *Compactness avoidance* of Patey's monograph, section *Liu's theorem*: the compactness is handled by $\mathsf{RWKL}$, and the disjunction by a weakly merging disjunctive question. The incomparability of $\mathsf{RT}^2_2$ and $\mathsf{WKL}_0$ combines Liu's theorem with :ref{#cor-wkl-not-rt22}, attributed to Hirst by Hirschfeldt (Corollary 6.12).

- J. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Chapter 6.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Chapter 8.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *Liu's theorem*.
