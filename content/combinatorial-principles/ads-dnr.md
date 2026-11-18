---
title: ADS does not imply DNR, and the zoo
summary: Forcing with finite ascending sequences in the ω-part of a stable linear order; SADS preserves the property of computing no DNC function (Hirschfeldt, Shore); with cohesiveness, ADS has an ω-model without DNC functions, so ADS implies neither DNR, WWKL₀, WKL₀, SRT²₂ nor EM; a map of the principles of the course.
duration: 30
prerequisites: [dnr-wwkl, stable-cohesive, reducibilities/preservation]
---

The previous lesson placed $\mathsf{DNR}$ below both $\mathsf{WKL}_0$ and $\mathsf{RT}^2_2$. This lesson shows that the order principles of the course do not reach it: there is an ω-model of $\mathsf{ADS}$ in which no function is DNC. The proof is a separation by preservation of a weakness property, the method of the course on reducibilities (:ref{#thm-preservation-separation}), with a notion of forcing adapted to stable orders. The lesson ends with a map of the principles met in the course.

## Forcing with ascending sequences

Let $\mathcal W$ be the class of sets that compute no DNC function. It is a weakness property: it is closed downwards under Turing reducibility (:ref{#def-weakness}). $\mathsf{DNR}$ does not preserve it: $\emptyset \in \mathcal W$, and every solution to the instance $\emptyset$ of $\mathsf{DNR}$ is a DNC function.

:::theorem[Hirschfeldt, Shore]{#thm-sads-preserves-dnc}
$\mathsf{SADS}$ preserves $\mathcal W$: for every set $Z$ that computes no DNC function and every $Z$-computable stable linear order $L$, there is an infinite ascending or descending sequence $G$ such that $Z \oplus G$ computes no DNC function.
:::

**Intuition.** If $L$ has a $Z$-computable solution, there is nothing to do. Otherwise, build an ascending sequence $G$ in the ω-part $A$ by finite approximations, and defeat each functional $\Gamma$: make $\Gamma^{Z \oplus G}$ partial, or make it agree with $\Phi_e(e)$ at some $e$. The approximations must stay in $A$, which $Z$ cannot decide, but the computations can be explored through all finite ascending sequences, inside $A$ or not. If neither goal can be reached inside $A$, the computations found outside $A$ give a $Z$-computable function that agrees with $\Phi_e(e)$ infinitely often only through sequences ending in $A^*$; this produces an infinite $Z$-c.e. subset of $A^*$, hence a $Z$-computable descending sequence.

:::proof{of=thm-sads-preserves-dnc}
Let $A$ and $A^*$ be the two parts of $L$. If $L$ has a $Z$-computable ascending or descending sequence $G$, then $Z \oplus G \equiv_T Z$ and we are done. Assume it has none. Then neither $A$ nor $A^*$ has an infinite $Z$-c.e. subset: such a subset would have an infinite $Z$-computable subset, which computes with $L$ a solution by :ref{#prop-stable-order-solutions}, relativized to $Z$.

A **precondition** is a finite sequence $\beta = (b_0, \ldots, b_{k-1})$ increasing in both orders: $b_0 < b_1 < \cdots$ and $b_0 <_L b_1 <_L \cdots$. The set of preconditions is $Z$-computable. A **condition** is a precondition whose last element is in $A$; then all its elements are in $A$, which is an initial segment of $L$. Extension is extension of sequences. We identify a sequence with its set of elements, and for a functional $\Gamma$ we write $\Gamma^{Z \oplus \beta}(e)\converge$ if the computation of $\Gamma$ on input $e < |\beta|$, with oracle $Z \oplus \beta$, halts in fewer than $|\beta|$ steps and queries the second oracle only on numbers at most $\max \beta$. If $\beta$ is an initial segment of an increasing enumeration of a set $G$, the second oracle agrees with $G$ on these numbers; so $\Gamma^{Z \oplus G}(e)\converge = v$ if and only if $\Gamma^{Z \oplus \beta}(e)\converge = v$ for some initial segment $\beta$ of $G$.

*Infinity.* Every condition $\alpha$ has a longer one extending it: its last element has finitely many $<_L$-predecessors, and $A$ is infinite (otherwise $A^*$ would be cofinite, hence computable and infinite), so some $x \in A$ is larger than the last element in both orders.

*Defeating a functional.* Let $\Gamma$ be a functional and $\alpha$ a condition. We claim that $\alpha$ has an extension $\alpha^*$ that is a condition and satisfies one of:

1. $\Gamma^{Z \oplus \alpha^*}(e)\converge = \Phi_e(e)$ for some $e$ with $\Phi_e(e)\converge$;
2. for some $e$, $\Gamma^{Z \oplus \beta}(e)\diverge$ for every precondition $\beta$ extending $\alpha^*$.

Suppose not. Taking $\alpha^* = \alpha$ in (2), for every $e$ some precondition $\beta \succeq \alpha$ has $\Gamma^{Z \oplus \beta}(e)\converge$. Let $\beta_e$ be the first one in a $Z$-computable search, and $f(e) = \Gamma^{Z \oplus \beta_e}(e)$. The function $f$ is total and $Z$-computable. If $f(e) = \Phi_e(e)$ held for only finitely many $e$, a finite modification of $f$ would be a $Z$-computable DNC function; so $f(e) = \Phi_e(e)\converge$ for infinitely many $e$. For each such $e$, $\beta_e$ is not a condition, since (1) fails with $\alpha^* = \beta_e$: its last element $b_e$ lies in $A^*$. Moreover $|\beta_e| > e$, so $b_e \geq |\beta_e| - 1 \geq e$. The set $\{ b_e : f(e) = \Phi_e(e)\converge \}$ is $Z$-c.e., infinite since $b_e \geq e$ for infinitely many $e$, and contained in $A^*$: a contradiction.

*The generic sequence.* List the functionals as $\Gamma_0, \Gamma_1, \ldots$. Build conditions $\alpha_0 \preceq \alpha_1 \preceq \cdots$, alternately lengthening the condition and applying the claim to the next functional. Let $G$ be the union. It is an infinite ascending sequence, contained in $A$. Let $\Gamma$ be a functional with $\Gamma^{Z \oplus G}$ total, and $\alpha^*$ the condition obtained for it. In case (2), $\Gamma^{Z \oplus G}(e)$ would diverge, since every initial segment of $G$ extending $\alpha^*$ is a precondition. So case (1) holds: $\Gamma^{Z \oplus G}(e) = \Phi_e(e)$ for some $e$ with $\Phi_e(e)\converge$, and $\Gamma^{Z \oplus G}$ is not DNC.
:::

The proof uses the two possible failures of an extension asymmetrically. A computation found through a precondition outside the conditions does not help the construction, but it reveals an element of $A^*$. Too many such revelations would give $Z$ a computable descending sequence. This is the same mechanism as in the low basis for $\mathsf{SADS}$ (:ref{to="lowness/stable-linear-orders"}), with the jump of $G$ replaced by its DNC power.

:::quiz[the proof that SADS preserves non-DNC degrees]
Why does the claim search through **preconditions** rather than through conditions?

- [x] Because whether a sequence ends in $A$ is not decidable by $Z$, while the preconditions form a $Z$-computable set: the function $f$ must be $Z$-computable.
- [ ] Because conditions might not extend $\alpha$.

  Conditions extending $\alpha$ exist, by the infinity step. The problem is computing them.
- [ ] Because preconditions are always in $A$.

  Preconditions may end in $A^*$; this is what the contradiction exploits.

---

Where is the stability of $L$ used?

- [x] To split $L$ into an initial segment $A$ of elements with finitely many predecessors and its complement $A^*$, so that a precondition ending in $A$ lies entirely in $A$, and to turn infinite subsets of $A^*$ into descending sequences.
- [ ] To make the set of preconditions computable.

  The preconditions are $Z$-computable for any $Z$-computable linear order.
- [ ] To guarantee that $f$ is total.

  Totality comes from the failure of (2) for $\alpha^* = \alpha$.
:::

## An ω-model of ADS without DNC functions

:::corollary[Hirschfeldt, Shore]{#cor-ads-not-dnr}
There is an ω-model of $\mathsf{ADS}$ that contains no DNC function. Consequently, over $\mathsf{RCA}_0$, $\mathsf{ADS}$ implies neither $\mathsf{DNR}$, nor $\mathsf{WWKL}_0$, $\mathsf{WKL}_0$, $\mathsf{SRT}^2_2$ or $\mathsf{EM}$.
:::

:::proof{of=cor-ads-not-dnr}
$\mathsf{COH}$ preserves $\mathcal W$: by the theorem on countably merging forcing questions with computable Mathias forcing relative to $Z$, it admits DNC avoidance (:ref{to="compactness-avoidance/dnc-avoidance"}; the unrelativized case is :ref{#thm-mathias-coh-preservation}), which for $D = \emptyset$ is exactly preservation of $\mathcal W$. By :ref{#thm-sads-preserves-dnc}, so does $\mathsf{SADS}$. Since both problems preserve $\mathcal W$ and $\emptyset \in \mathcal W$, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf{SADS}$ and $\mathsf{COH}$, by iterating and dovetailing as in :ref{#lem-preservation-ideal} (:ref{#ex-preserve-two-problems}).

In an ω-model, $\mathsf{COH}$ implies $\mathsf{CADS}$, and $\mathsf{SADS} + \mathsf{CADS}$ implies $\mathsf{ADS}$ (:ref{#prop-ads-decomposition}). So $\mathcal I \models \mathsf{ADS}$, and $\mathcal I$ contains no DNC function, since all its members are in $\mathcal W$: $\mathcal I \not\models \mathsf{DNR}$.

The other principles imply $\mathsf{DNR}$ over $\mathsf{RCA}_0$: $\mathsf{WKL}_0$ and $\mathsf{WWKL}_0$ by :ref{#thm-wwkl-dnr}, $\mathsf{SRT}^2_2$ by the theorem of Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (previous lesson). For $\mathsf{EM}$: if $\mathsf{ADS}$ implied $\mathsf{EM}$, it would imply $\mathsf{RT}^2_2$ by :ref{#thm-rt22-em-ads}, hence $\mathsf{DNR}$ (:ref{#cor-rt22-dnc} holds in every ω-model of $\mathsf{RT}^2_2$).
:::

The same argument works for $\mathsf{SCAC}$, with sequences that are chains of small elements (:ref{#ex-scac-preserves-dnc}), and then $\mathsf{CAC}$, which is $\mathsf{SCAC} + \mathsf{ADS}$ (:ref{#prop-cac-decomposition}), has an ω-model without DNC functions. So none of the order principles of the course carries any compactness. The next lesson explains this through a weakness property that detects compactness in general, constant-bound immunity, and adds a second measure, disjunction.

## A map of the course

:::figure[Implications over $\mathsf{RCA}_0$ between the principles of the course. Each solid arrow is strict. The dashed arrow from $\mathsf{COH}$ to $\mathsf{CADS}$ is not known to be strict over $\mathsf{RCA}_0$; the two principles are equivalent over $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$, hence in ω-models. The figure does not record which implications fail; the table below lists the main non-implications. $\mathsf{EM}$ implies $\mathsf{DNR}$ through the Ramsey-type weak König lemma, and $\mathsf{SRT}^2_2$ by Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman.]
<svg class="fig" viewBox="0 0 600 390" width="600" role="img" aria-label="A diagram of implications between principles: ACA0 implies RT22 and WKL0; RT22 implies CAC, SRT22 and EM; WKL0 implies WWKL0, which implies DNR; CAC implies ADS and SCAC; SRT22 implies SCAC and DNR; EM implies DNR; SCAC and ADS imply SADS; ADS implies COH, which implies CADS"><defs><marker id="zoo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker><marker id="zoo-arrow-m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><line x1="313.8" y1="47.0" x2="271.1" y2="81.2" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="358.0" y1="44.5" x2="461.8" y2="83.6" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="222.0" y1="109.9" x2="137.0" y2="146.2" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="250.0" y1="111.0" x2="250.0" y2="145.2" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="274.4" y1="111.0" x2="338.4" y2="145.2" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="500.0" y1="111.0" x2="500.0" y2="145.2" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="491.7" y1="175.0" x2="461.3" y2="222.3" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="92.1" y1="175.0" x2="70.3" y2="211.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="117.7" y1="175.0" x2="166.9" y2="211.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="238.2" y1="175.0" x2="205.4" y2="211.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="184.1" y1="241.0" x2="167.7" y2="277.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="79.7" y1="241.0" x2="134.3" y2="277.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="56.1" y1="241.0" x2="45.1" y2="277.0" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="278.0" y1="172.9" x2="410.0" y2="224.4" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="383.3" y1="175.0" x2="431.9" y2="222.3" class="ink-stroke" stroke-width="1.2" marker-end="url(#zoo-arrow)"/><line x1="40.0" y1="307.0" x2="40.0" y2="341.2" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#zoo-arrow-m)"/><rect x="302.0" y="21.0" width="56" height="26" rx="5" class="head-cell"/><text x="330" y="39" text-anchor="middle" class="mrm" font-size="14">ACA₀</text><rect x="222.0" y="85.0" width="56" height="26" rx="5" class="cell"/><text x="250" y="103" text-anchor="middle" class="mrm" font-size="14">RT²₂</text><rect x="472.0" y="85.0" width="56" height="26" rx="5" class="head-cell"/><text x="500" y="103" text-anchor="middle" class="mrm" font-size="14">WKL₀</text><rect x="72.0" y="149.0" width="56" height="26" rx="5" class="cell"/><text x="100" y="167" text-anchor="middle" class="mrm" font-size="14">CAC</text><rect x="222.0" y="149.0" width="56" height="26" rx="5" class="cell"/><text x="250" y="167" text-anchor="middle" class="mrm" font-size="14">SRT²₂</text><rect x="342.0" y="149.0" width="56" height="26" rx="5" class="cell"/><text x="370" y="167" text-anchor="middle" class="mrm" font-size="14">EM</text><rect x="472.0" y="149.0" width="56" height="26" rx="5" class="cell"/><text x="500" y="167" text-anchor="middle" class="mrm" font-size="14">WWKL₀</text><rect x="32.0" y="215.0" width="56" height="26" rx="5" class="cell"/><text x="60" y="233" text-anchor="middle" class="mrm" font-size="14">ADS</text><rect x="162.0" y="215.0" width="56" height="26" rx="5" class="cell"/><text x="190" y="233" text-anchor="middle" class="mrm" font-size="14">SCAC</text><rect x="422.0" y="227.0" width="56" height="26" rx="5" class="cell"/><text x="450" y="245" text-anchor="middle" class="mrm" font-size="14">DNR</text><rect x="12.0" y="281.0" width="56" height="26" rx="5" class="cell"/><text x="40" y="299" text-anchor="middle" class="mrm" font-size="14">COH</text><rect x="132.0" y="281.0" width="56" height="26" rx="5" class="cell"/><text x="160" y="299" text-anchor="middle" class="mrm" font-size="14">SADS</text><rect x="12.0" y="345.0" width="56" height="26" rx="5" class="cell"/><text x="40" y="363" text-anchor="middle" class="mrm" font-size="14">CADS</text><text x="590" y="320" text-anchor="end" class="label">arrow: implication over RCA₀</text><text x="590" y="338" text-anchor="end" class="label">solid arrows are strict</text><text x="590" y="356" text-anchor="end" class="label">dashed: strictness unknown</text></svg>
:::

The strictness of the arrows and the non-implications are proved, or admitted with references, in this course and in the courses it points to:

| Non-implication | Reason |
| --- | --- |
| $\mathsf{ADS}$, $\mathsf{CAC}$ do not imply $\mathsf{DNR}$ | :ref{#cor-ads-not-dnr}, :ref{#ex-scac-preserves-dnc} |
| $\mathsf{WKL}_0$ does not imply $\mathsf{SADS}$ | :ref{#ex-sads-hyperimmune} |
| $\mathsf{WWKL}_0$ does not imply $\mathsf{WKL}_0$; $\mathsf{DNR}$ does not imply $\mathsf{WWKL}_0$ | :ref{#cor-wwkl-not-wkl}; Ambos-Spies, Kjos-Hanssen, Lempp, Slaman |
| $\mathsf{RT}^2_2$ does not imply $\mathsf{WWKL}_0$ | Liu, :ref{#cor-rt22-not-wwkl} |
| $\mathsf{SADS}$ does not imply $\mathsf{COH}$; $\mathsf{SCAC}$ does not imply $\mathsf{SRT}^2_2$ | low bases; :ref{to="stable-cohesive"} |
| $\mathsf{COH}$ does not imply $\mathsf{SADS}$ | first-order strength; :ref{to="stable-cohesive"} |
| $\mathsf{ADS}$ does not imply $\mathsf{SCAC}$ | Lerman, Solomon, Towsner |
| $\mathsf{EM}$ does not imply $\mathsf{SRT}^2_2$ | Lerman, Solomon, Towsner; :ref{#cor-sd-em-not-srt22} |
| $\mathsf{SRT}^2_2$ does not imply $\mathsf{RT}^2_2$ | Chong, Slaman, Yang (over $\mathsf{RCA}_0$); Monin, Patey (in ω-models) |
| $\mathsf{RT}^2_2$ does not imply $\mathsf{ACA}_0$ | Seetapun, :ref{#cor-rt22-not-aca} |

Many more principles live in this region: the rainbow and polarized Ramsey theorems, the free set and thin set theorems, Hindman's theorem (which implies $\mathsf{ACA}_0$), the tree theorem, and principles from model theory such as the atomic model theorem (Hirschfeldt, Section 9.3). Dzhafarov and Mummert, Chapter 9, survey them, and the online Reverse Mathematics Zoo of Dzhafarov records the known relations.

## Notes and references

:ref{#thm-sads-preserves-dnc} and :ref{#cor-ads-not-dnr} are due to Hirschfeldt and Shore (2007), who proved them for $\mathsf{SCAC}$ and $\mathsf{CAC}$ (Hirschfeldt, Theorem 9.9 and Exercise 9.23; Dzhafarov–Mummert, Theorem 9.2.21, whose proof this lesson follows for linear orders). The separation of $\mathsf{SRT}^2_2$ from $\mathsf{RT}^2_2$ over $\mathsf{RCA}_0$ is due to Chong, Slaman and Yang (2014), with a non-standard model; Monin and Patey (2021) separated them in ω-models.

- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- C. T. Chong, T. A. Slaman and Y. Yang, *The metamathematics of stable Ramsey's theorem for pairs*, Journal of the American Mathematical Society 27 (2014), 863–892.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics 389 (2021), 107903.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 9.2 and 9.12.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Chapter 9.

:::::exercises
::::exercise{#ex-scac-preserves-dnc difficulty=2 objective="Adapt the forcing with ascending sequences to stable partial orders, with chains of small elements."}
Let $Z$ compute no DNC function, and $(P, \leq_P)$ a $Z$-computable stable partial order in which every element is small or isolated, with no infinite $Z$-computable chain or antichain. Show that there is an infinite chain $G$ such that $Z \oplus G$ computes no DNC function.

:::solution
Let $S$ be the set of small elements and $I$ the set of isolated ones. If $I$ had an infinite $Z$-c.e. subset, it would have an infinite $Z$-computable subset $J$, and the thinning $j_0 = \min J$, $j_{k+1}$ the least element of $J$ larger than $j_k$ and $\leq_P$-incomparable with $j_0, \ldots, j_k$, would be a $Z$-computable infinite antichain: the element $j_{k+1}$ exists since each isolated $j_i$ is incomparable with almost every element. So $I$ has no infinite $Z$-c.e. subset; in particular it is not cofinite, so $S$ is infinite.

A precondition is a finite sequence $\beta$ increasing in the order of $\nat$ and in $<_P$; a condition is a precondition whose last element is small, and then all its elements are small. As in :ref{#thm-sads-preserves-dnc}, a condition $\alpha$ has longer extensions: its last element is $\leq_P$-below almost every element, and infinitely many elements are small. Given a functional $\Gamma$ and a condition $\alpha$, if no condition $\alpha^* \succeq \alpha$ satisfies (1) or (2) of the proof of the theorem, the same $Z$-computable function $f$ agrees with $\Phi_e(e)$ infinitely often only through preconditions $\beta_e$ whose last element $b_e \geq e$ is not small, hence isolated, since $P$ is stable with every element small or isolated. These elements form an infinite $Z$-c.e. subset of $I$, a contradiction. The generic sequence $G$ is a $\leq_P$-chain, and $Z \oplus G$ computes no DNC function. (Hirschfeldt and Shore; Dzhafarov–Mummert, Theorem 9.2.21.)
:::
::::

::::exercise{#ex-ads-not-dnr-low difficulty=1 objective="Check which of the principles of the course hold in the ω-model of a single low random sequence."}
Let $\mathcal M$ be the ω-model of the proof of :ref{#cor-wwkl-not-wkl}, built from a low random sequence. Which of $\mathsf{WWKL}_0$, $\mathsf{DNR}$, $\mathsf{WKL}_0$, $\mathsf{COH}$ does it satisfy?

:::solution
It satisfies $\mathsf{WWKL}_0$ by :ref{#cor-wwkl-not-wkl}, hence $\mathsf{DNR}$ by :ref{#thm-wwkl-dnr}. It does not satisfy $\mathsf{WKL}_0$, by the same corollary. It does not satisfy $\mathsf{COH}$: all its members are low, and by :ref{#prop-coh-no-low} some computable sequence has no low cohesive set.
:::
::::

::::exercise{#ex-zoo-read difficulty=1 objective="Read implications and non-implications off the map of the course."}
Using the map and the table, decide, for each pair, whether the first principle implies the second over $\mathsf{RCA}_0$: ($\mathsf{CAC}$, $\mathsf{COH}$), ($\mathsf{EM}$, $\mathsf{ADS}$), ($\mathsf{SRT}^2_2$, $\mathsf{SADS}$), ($\mathsf{WKL}_0$, $\mathsf{CAC}$), ($\mathsf{SCAC}$, $\mathsf{DNR}$).

:::solution
- $\mathsf{CAC}$ implies $\mathsf{COH}$: $\mathsf{CAC} \to \mathsf{ADS} \to \mathsf{COH}$.
- $\mathsf{EM}$ does not imply $\mathsf{ADS}$: otherwise $\mathsf{EM}$ would imply $\mathsf{SADS}$, and with :ref{#thm-rt22-em-ads} (2) $\mathsf{SRT}^2_2$, which it does not.
- $\mathsf{SRT}^2_2$ implies $\mathsf{SADS}$: $\mathsf{SRT}^2_2 \to \mathsf{SCAC} \to \mathsf{SADS}$.
- $\mathsf{WKL}_0$ does not imply $\mathsf{CAC}$: it does not even imply $\mathsf{SADS}$ (:ref{#ex-sads-hyperimmune}).
- $\mathsf{SCAC}$ does not imply $\mathsf{DNR}$: it holds in the ω-model of $\mathsf{CAC}$ without DNC functions (:ref{#ex-scac-preserves-dnc}).
:::
::::
:::::
