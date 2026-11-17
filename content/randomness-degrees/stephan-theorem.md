---
title: Random sequences of PA degree
summary: A Martin-Löf random sequence of PA degree computes ∅′ (Stephan); so incomplete random sequences compute no {0,1}-valued DNC function, there are PA degrees that are not random, and the random degrees are not closed upward.
duration: 25
prerequisites: [ce-sets, pi01-classes/pa-degrees, martin-lof-randomness/solovay-tests]
---

Random sequences compute diagonally non-computable functions (:ref{#cor-random-dnc}), and every PA set computes a random sequence, since a non-empty $\Pi^0_1$ class of random sequences exists (:ref{#cor-mlr-structure}) and a PA set computes a member of every non-empty $\Pi^0_1$ class (:ref{#thm-pa-characterization}). It is natural to ask whether random sequences compute $\{0, 1\}$-valued DNC functions, that is, whether they are of PA degree. Stephan's theorem answers that they never do, unless they compute $\emptyset'$.

So the random sequences come in two kinds. Those above $\emptyset'$, such as $\Omega$, are computationally powerful: they compute everything below $\emptyset'$ and, by the Kučera–Gács theorem, every set is computable from one of them. The others are computationally weak: they are not PA, and many results of the theory (in the course on K-trivial sets, for instance) show that they behave like weak oracles. A sequence that is neither of the two kinds, that is, an incomplete PA sequence, is never random.

The proof builds a partial computable $\{0, 1\}$-valued function $f$ that is hard to extend for most oracles: for each functional $\Phi_e$, the class of oracles $B$ such that $\Phi^B_e$ extends $f$ on a certain finite interval has measure at most $2^{-e-1}$. A PA set $A$ computes a total extension $g$ of $f$, through infinitely many functionals. If $A$ does not compute $\emptyset'$, then infinitely often the computation of $g$ on an interval converges before the enumeration of $\emptyset'$ reveals a number; a Solovay test catches $A$ at these moments.

## Stephan's theorem

:::theorem[Stephan]{#thm-stephan}
If $A$ is Martin-Löf random and of PA degree, then $\emptyset' \leq_T A$.
:::

:::proof{of=thm-stephan}
Let $A$ be of PA degree with $\emptyset' \not\leq_T A$; we show that $A$ is not random.

*A partial function that is hard to extend.* For each $e$, let $I_e = \{ 2^{e+2}, \dots, 2^{e+3} - 1 \}$, an interval of $2^{e+2}$ numbers; the intervals are pairwise disjoint. We define a partial computable $f : \nat \to \{0, 1\}$, working on each interval $I_e$ separately. At stage $s$, let $a_s$ be the least element of $I_e$ at which $f$ is not yet defined. For $i < 2$, let $\mathcal P_{e, s, i}$ be the class of sequences $B$ such that:

1. $\Phi^B_e(n)[s]$ converges for every $n \in I_e$;
2. $\Phi^B_e(n) = f(n)$ for every $n \in I_e$ with $n < a_s$;
3. $\Phi^B_e(a_s) = i$.

Membership in $\mathcal P_{e, s, i}$ depends only on $B \uh s$, so $\mathcal P_{e, s, i}$ is clopen, and its measure $d_{e, s, i}$ is a rational computable from $(e, s, i)$. If $d_{e, s, 0} + d_{e, s, 1} > 2^{-e-1}$, choose $i < 2$ with $d_{e, s, i} \leq d_{e, s, 1-i}$ and define $f(a_s) = i$. Otherwise, do nothing on $I_e$ at stage $s$.

*Each interval is defined only finitely often.* When $f(a_s) = i$ is defined at stage $s$, the class $\mathcal K_s = \mathcal P_{e, s, 1-i}$ has measure at least $2^{-e-2}$, and every $B \in \mathcal K_s$ satisfies $\Phi^B_e(a_s) = 1 - i \neq f(a_s)$. For two such stages $s < t$ of the interval $I_e$, $a_s < a_t$, so every $B \in \mathcal K_t$ satisfies $\Phi^B_e(a_s) = f(a_s)$, by condition 2; hence $\mathcal K_s \cap \mathcal K_t = \emptyset$. So there are fewer than $2^{e+2}$ such stages, and $a_s$ always exists. Let $t_e$ be the last one; for every $s > t_e$, $d_{e, s, 0} + d_{e, s, 1} \leq 2^{-e-1}$.

*A Solovay test.* Since $A$ is PA, it computes a total $\{0, 1\}$-valued function $g$ extending $f$ (:ref{#ex-pa-extension}). Let $\Phi_{e^*}$ be a functional with $\Phi^A_{e^*} = g$; by the padding lemma, there is a computable strictly increasing sequence $e_0 < e_1 < \cdots$ of indices of the same functional, so $\Phi^A_{e_j} = g$ for every $j$. Let $k_0, k_1, \dots$ be a computable enumeration of $\emptyset'$ without repetitions, where $k_s$ is enumerated at stage $s$. For each $s$, let $e(s) = e_{k_s}$, let $r(s)$ be the least stage $r > s$ with $d_{e(s), r, 0} + d_{e(s), r, 1} \leq 2^{-e(s)-1}$, which exists since every $r > t_{e(s)}$ qualifies, and let
$$
\mathcal S_s = \mathcal P_{e(s), r(s), 0} \cup \mathcal P_{e(s), r(s), 1}.
$$
These classes are clopen and uniformly computable, and $\sum_s \lambda(\mathcal S_s) \leq \sum_s 2^{-e(s)-1} \leq \sum_e 2^{-e-1} = 1$, since the indices $e(s)$ are pairwise distinct. So $(\mathcal S_s)$ is a Solovay test.

*$A$ fails the test.* Let $h(j)$ be the least stage $h$ such that $\Phi^A_{e_j}(n)[h]$ converges for every $n \in I_{e_j}$; then $h \leq_T A$. There are infinitely many $s$ with $h(k_s) < s$. Otherwise, for almost every $s$, $s \leq h(k_s)$: the number $k_s$ enters $\emptyset'$ at a stage bounded by $h(k_s)$. Then for almost every $n$, $n \in \emptyset'$ if and only if $n = k_s$ for some $s \leq h(n)$, which $A$ can decide, and $\emptyset' \leq_T A$, contrary to the hypothesis. For each $s$ with $h(k_s) < s$, the computations $\Phi^A_{e(s)}(n)$, $n \in I_{e(s)}$, converge by stage $s < r(s)$, with values $g(n)$, which agree with $f(n)$ where $f$ is defined. So $A \in \mathcal P_{e(s), r(s), g(a)}$, where $a = a_{r(s)}$ for the interval $I_{e(s)}$, and $A \in \mathcal S_s$. So $A$ belongs to infinitely many $\mathcal S_s$, and by :ref{#thm-solovay}, $A$ is not random.
:::

:::figure[The construction on an interval $I_e$ in the proof of :ref{#thm-stephan}. Each time the oracles that make $\Phi_e$ total on $I_e$ and consistent with $f$ so far have measure more than $2^{-e-1}$, the value of $f$ at the next point $a_s$ is chosen against the larger half, which is discarded for good. The discarded classes are disjoint and have measure at least $2^{-e-2}$, so this happens fewer than $2^{e+2}$ times.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="A row of cells for the numbers of the interval I e, with f defined on the first three; below, a bar of measure divided into discarded classes for each defined value and a remaining class of measure at most 2 to the minus e minus 1"><text x="20" y="40" class="label">I_e</text><rect x="70" y="24" width="40" height="26" class="cell head-cell"/><rect x="110" y="24" width="40" height="26" class="cell head-cell"/><rect x="150" y="24" width="40" height="26" class="cell head-cell"/><rect x="190" y="24" width="40" height="26" class="cell"/><rect x="230" y="24" width="40" height="26" class="cell"/><rect x="270" y="24" width="40" height="26" class="cell"/><rect x="310" y="24" width="40" height="26" class="cell"/><rect x="350" y="24" width="40" height="26" class="cell"/><text x="90" y="42" text-anchor="middle" class="mrm" font-size="13">0</text><text x="130" y="42" text-anchor="middle" class="mrm" font-size="13">1</text><text x="170" y="42" text-anchor="middle" class="mrm" font-size="13">1</text><text x="210" y="42" text-anchor="middle" class="math" font-size="13">?</text><text x="210" y="66" text-anchor="middle" class="label">a_s</text><text x="420" y="42" class="label">values of f defined so far</text><text x="20" y="116" class="label">measure</text><rect x="70" y="100" width="90" height="26" class="soft-fill"/><rect x="160" y="100" width="70" height="26" class="soft-fill"/><rect x="230" y="100" width="80" height="26" class="soft-fill"/><rect x="310" y="100" width="60" height="26" class="accent-fill"/><rect x="370" y="100" width="180" height="26" class="cell"/><text x="115" y="118" text-anchor="middle" class="label">K₁</text><text x="195" y="118" text-anchor="middle" class="label">K₂</text><text x="270" y="118" text-anchor="middle" class="label">K₃</text><text x="340" y="118" text-anchor="middle" class="label">≤ 2⁻ᵉ⁻¹</text><text x="460" y="118" text-anchor="middle" class="label">Φ_e not total on I_e</text><text x="70" y="150" class="label">shaded: discarded classes, each of measure ≥ 2⁻ᵉ⁻², pairwise disjoint;</text><text x="70" y="168" class="label">accent: oracles still consistent with f, of measure ≤ 2⁻ᵉ⁻¹ once the interval is settled</text></svg>
:::

:::quiz[Stephan's theorem]
In the proof of :ref{#thm-stephan}, why does the interval $I_e$ have $2^{e+2}$ elements?

- [x] Each value of $f$ defined on $I_e$ discards a class of measure at least $2^{-e-2}$, the classes are disjoint, so fewer than $2^{e+2}$ values are defined; the interval never runs out of points, and the construction on it eventually stops.
- [ ] To make the test have total measure at most $1$.

  The bound on the test comes from the threshold $2^{-e-1}$, not from the size of the interval.
- [ ] Because $\Phi_e$ is defined on $2^{e+2}$ arguments.

  $\Phi^B_e$ may be defined anywhere; only its values on $I_e$ matter.

---

Where is the hypothesis $\emptyset' \not\leq_T A$ used?

- [x] To find infinitely many $s$ at which the $A$-computable stage $h(k_s)$ is smaller than the stage $s$ at which $k_s$ enters $\emptyset'$; at those $s$, $A$ is already in the clopen class $\mathcal S_s$.
- [ ] To show that $A$ computes a total extension of $f$.

  This uses only that $A$ is PA.
- [ ] To bound the measure of the classes $\mathcal S_s$.

  The bound holds for every oracle; it is a property of the construction of $f$.
:::

## Consequences

:::corollary[Kučera; Stephan]{#cor-stephan}
1. A random sequence $A$ with $\emptyset' \not\leq_T A$ computes no $\{0, 1\}$-valued DNC function, although it computes a DNC function.
2. There are PA degrees that are not random: every low PA set is an example.
3. The class of random degrees is not closed upward: a low PA set computes a random sequence but is not of random degree.
:::

:::proof{of=cor-stephan}
1. By :ref{#thm-stephan} and :ref{#cor-random-dnc}.
2. A low PA set exists by the low basis theorem applied to the $\Pi^0_1$ class $\mathrm{DNC}_2$ (:ref{#cor-pa-basis}). A low set does not compute $\emptyset'$, so by :ref{#thm-stephan}, no PA set Turing equivalent to it is random.
3. A PA set computes a member of the non-empty $\Pi^0_1$ class of :ref{#cor-mlr-structure}, which consists of random sequences. By (2), a low PA set is not Turing equivalent to a random sequence.
:::

Part 1 shows that the DNC degrees are not all PA: a low random sequence computes a DNC function but no $\{0, 1\}$-valued one. The two notions differ in the size of the values allowed, and the incomplete random sequences lie between them: DNC, but not PA.

::::exercise[Above every incomplete degree]{#ex-stephan-above-incomplete difficulty=2 objective="Combine Stephan's theorem with the relativized computably dominated basis theorem."}
Let $X$ be a set with $\emptyset' \not\leq_T X$. Show that some set $Y \geq_T X$ is not of random degree. (Stephan.)

:::hint
Find a PA set $Y \geq_T X$ such that every $Y$-computable function is dominated by an $X$-computable function, and use the settling-time function of $\emptyset'$.
:::

:::solution
The class of sets $X \oplus D$ with $D \in \mathrm{DNC}_2$ is a non-empty $\Pi^0_1(X)$ class. By the computably dominated basis theorem relativized to $X$ (:ref{#thm-dominated-basis}), it has a member $Y = X \oplus D$ such that every $Y$-computable function is dominated by an $X$-computable function. The set $Y$ computes $X$, and it is PA since it computes $D$.

Suppose that $\emptyset' \leq_T Y$. The settling-time function $m(n)$, the least $s$ with $\emptyset'_s \uh n = \emptyset' \uh n$, is then $Y$-computable, so it is dominated by an $X$-computable function $g$: $m(n) \leq g(n)$ for almost every $n$. Then $\emptyset' \uh n = \emptyset'_{g(n)} \uh n$ for almost every $n$, and $\emptyset' \leq_T X$, a contradiction. So $\emptyset' \not\leq_T Y$, and by :ref{#thm-stephan}, no set Turing equivalent to $Y$ is random, since such a set would be PA and random. (Downey–Hirschfeldt, Corollary 8.8.7.)
:::
::::

## Notes and references

Stephan's theorem is from his 2006 paper; Kučera (1985) had shown that the PA degrees have measure $0$ and that some PA degrees are not random, which follow. The proof is that of Downey and Hirschfeldt (Theorem 8.8.4). Stephan describes the dichotomy as two types of random sets, the powerful ones that solve the halting problem and the weak ones that are not PA. Barmpalias, Lewis and Ng (2010) proved that every PA degree is the join of two random degrees (admitted; Downey–Hirschfeldt, Theorem 8.8.8), so a join of two random degrees need not be random. The incomplete random sequences are also characterized as the difference random sequences of Franklin and Ng (Downey–Hirschfeldt, Section 7.7).

- F. Stephan, *Martin-Löf random and PA-complete sets*, in: Logic Colloquium '02, Lecture Notes in Logic 27, Association for Symbolic Logic, 2006, 342–348.
- A. Kučera, *Measure, $\Pi^0_1$-classes and complete extensions of PA*, in: Recursion Theory Week, Lecture Notes in Mathematics 1141, Springer, 1985, 245–259.
- G. Barmpalias, A. E. M. Lewis and K. M. Ng, *The importance of $\Pi^0_1$ classes in effective randomness*, Journal of Symbolic Logic 75 (2010), 387–400.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 8.8.

:::::exercises
::::exercise{#ex-pa-measure-zero difficulty=1 objective="Derive from Stephan's theorem that the PA sets form a null class."}
Show that the class of PA sets has measure $0$. (Kučera.)

:::solution
The class of sets that compute $\emptyset'$ has measure $0$, by Sacks's theorem (:ref{#thm-sacks}), and the class of non-random sets has measure $0$ (:ref{#cor-mlr-structure}). By :ref{#thm-stephan}, every PA set is non-random or computes $\emptyset'$, so the PA sets are contained in a union of two null classes.
:::
::::

::::exercise{#ex-stephan-delta2 difficulty=1 objective="Apply Stephan's theorem to Δ⁰₂ random sequences."}
Let $A \leq_T \emptyset'$ be random. Show that $A$ is PA if and only if $A \equiv_T \emptyset'$.

:::solution
If $A \equiv_T \emptyset'$, then $A$ computes $\emptyset'$, which is PA, so $A$ is PA. Conversely, if $A$ is PA, then $\emptyset' \leq_T A$ by :ref{#thm-stephan}, and $A \leq_T \emptyset'$ by hypothesis.
:::
::::

::::exercise{#ex-pa-computes-nonpa-random difficulty=1 objective="Combine the two kinds of random sequences to find, below every PA set, a random sequence that is not PA."}
Show that every PA set computes a random sequence that is not PA.

:::solution
Let $Y$ be PA. If $\emptyset' \not\leq_T Y$, then $Y$ computes a random sequence $A$, a member of the $\Pi^0_1$ class of :ref{#cor-mlr-structure}, and $\emptyset' \not\leq_T A$, so $A$ is not PA by :ref{#thm-stephan}. If $\emptyset' \leq_T Y$, then $Y$ computes a low random sequence $A$, which exists by the low basis theorem and is computable in $\emptyset'$ (:ref{#thm-low-basis}); a low set does not compute $\emptyset'$, so $A$ is not PA by :ref{#thm-stephan}.
:::
::::
:::::
