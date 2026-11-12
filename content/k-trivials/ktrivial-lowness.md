---
title: K-triviality and lowness
summary: Every K-trivial set is low for K, by a theorem of Nies and Hirschfeldt; the amplification argument, which proves the weak truth-table case of its consequence that no K-trivial set is complete; the decanter and golden run methods; the equivalence of K-triviality with the lowness notions, and the ideal of K-trivial sets.
duration: 50
prerequisites: [hungry-sets, cost-functions, solovay-functions, fundamentals/fixed-point]
---

The lesson on lowness showed that a set that is low for K is K-trivial (:ref{#prop-lowness-implications}), and the hungry sets theorem that the three lowness notions coincide. The converse is the central theorem of the subject: every K-trivial set is low for K. It identifies a property of initial segments, being as simple as possible, with a property of the set as an oracle, being useless for compression. Its proof, the **golden run** construction of Nies, is a priority argument of considerable length, and is admitted here. This lesson presents its basic technique, the **amplification** of the cost of changes, in the simplest case where it gives a complete proof: a K-trivial set does not compute $\emptyset'$ by a weak truth-table reduction. It then explains how the decanter and golden run methods overcome the obstacles met by Turing reductions, states the main theorem, and derives its consequences.

## Amplification

Suppose that $A$ is K-trivial with constant $b$, and that we build a prefix-free machine $M$ by the KC theorem. If we give a number $n$ a description of length $\ell$, then $K(n) \leq \ell + d$, where $d$ is the coding constant of $M$, and so $U$ must eventually describe the current prefix $A \uh n$ with at most $\ell + d + b$ bits. If we can then force the approximation of $A \uh n$ to change, $U$ must describe the new version as well, and so on. We pay $2^{-\ell}$ once, and $U$ pays at least $2^{-\ell - d - b}$ for each version. With more than $2^{\ell + d + b}$ versions, the domain of $U$ would have measure larger than $1$. The constants $b$ and $d$ are not known in advance, so the argument is run for every possible value of $\ell$, with budget $2^{-\ell}$.

To force changes of $A$, assume that $A$ computes a c.e. set $B$ that we build: enumerating an element $y$ into $B$ forces $A$ to change below the use of the computation of $B(y)$. For a weak truth-table reduction, the use is bounded in advance by a computable function, and $n$ can be chosen above it. This proves again :ref{#cor-k-trivial-wtt-incomplete}, without $\Omega$.

:::theorem[Downey, Hirschfeldt, Nies, Stephan]{#thm-wtt-amplification}
If $A$ is K-trivial, then $\emptyset' \not\leq_{wtt} A$.
:::

:::proof{of=thm-wtt-amplification}
Suppose that $A$ is K-trivial with constant $b$ and that $\emptyset' = \Theta^A$, where the computation $\Theta^A(z)$ only queries the oracle below $\theta(z)$, for a computable function $\theta$. By :ref{#cor-k-trivial-delta2}, $A$ has a computable approximation $(A_s)$. By :ref{#cor-smn-parameters}, there is a computable function $q$ such that $x \in W_e$ if and only if $q(e, x) \in \emptyset'$, for all $e$ and $x$. For each $e$, let $\Gamma_e^X(x) = \Theta^X(q(e, x))$ and $\gamma_e(x) = \theta(q(e, x))$. If $W_e$ is the set $B$ we build, then $\Gamma^A_e = B$, with use bounded by $\gamma_e$; we obtain such an $e$ by the fixed point theorem. For a string $\sigma$, $K_s(\sigma)$ is defined as for numbers.

*The construction with parameter $e$.* We build a c.e. set $B$ and a request set $L$, by strategies $S_j$, $j \geq 1$, run in parallel. Let $k_j = 2^{2j} + 1$. The strategy $S_j$ uses the followers $y_{j, i} = \langle j, i \rangle$ for $i < k_j$, and the number $n_j = 1 + \max \{ \gamma_e(y_{j,i}) : i < k_j \}$. It first enumerates the request $(n_j, j)$ into $L$. Then, for $i = 0, 1, \dots, k_j - 1$, it waits for a stage $s$, larger than the stages found before, such that

1. $\Gamma^{A_s}_e(y_{j, l})[s]\converge = B_s(y_{j, l})$ for every $l < k_j$, with use at most $\gamma_e(y_{j,l})$, and
2. $K_s(A_s \uh n_j) \leq 2j$.

When such a stage $s_{j,i}$ is found, and $i < k_j - 1$, the strategy enumerates $y_{j, i}$ into $B$ at stage $s_{j,i} + 1$, and passes to $i + 1$. The weight of $L$ is $\sum_{j \geq 1} 2^{-j} = 1$, for every $e$. The construction is uniform in $e$: there is a computable $h$ such that $B = W_{h(e)}$.

*The fixed point.* By :ref{#thm-fixed-point}, there is $e$ with $\Phi_e = \Phi_{h(e)}$, hence $W_e = W_{h(e)}$. Fix this $e$; then the set $B$ built with parameter $e$ is $W_e$, and $\Gamma^A_e = B$. By the KC theorem (:ref{#thm-kc}) applied to $L$, there is $d$ with $K(n_j) \leq j + d$ for every $j$. Let $j \geq b + d$, with $j \geq 1$.

*Every wait of $S_j$ ends.* Suppose that $S_j$ waits forever for the stage $s_{j,i}$. Then $S_j$ enumerates no further follower, so $B_s(y_{j,l}) = B(y_{j,l})$ for all $l < k_j$ and all large $s$. Since $\Gamma^A_e = B$ with uses below $n_j$, and $A_s \uh n_j = A \uh n_j$ for all large $s$, condition 1 holds at all large stages. And $K(A \uh n_j) \leq K(n_j) + b \leq j + d + b \leq 2j$, so $K_s(A_s \uh n_j) \leq 2j$ for all large $s$, which is condition 2. So the stage $s_{j,i}$ exists.

*The versions are distinct.* Let $\sigma_i = A_{s_{j,i}} \uh n_j$ for $i < k_j$. At the stage $s_{j,i}$, the followers $y_{j,l}$ with $l < i$ are in $B$, and those with $l \geq i$ are not. By condition 1, the computations $\Gamma^{\sigma_i}_e(y_{j,l})$ converge, since their uses are below $n_j$, and $\Gamma^{\sigma_i}_e(y_{j,l}) = 1$ if and only if $l < i$. So for $i < i'$, the strings $\sigma_i$ and $\sigma_{i'}$ give different values at $y_{j,i}$, and are distinct.

*Conclusion.* The $k_j$ distinct strings $\sigma_i$ satisfy $K(\sigma_i) \leq K_{s_{j,i}}(\sigma_i) \leq 2j$, so $\sum_\sigma 2^{-K(\sigma)} \geq k_j\, 2^{-2j} > 1$, contradicting :ref{#prop-k-basic} (4).
:::

:::figure[The versions forced by the strategy $S_j$, for $k_j = 4$. At the stage $s_{j,i}$, the prefix of length $n_j$ of the approximation computes $B$ correctly on the followers, $i$ of which are in $B$. The highlighted positions, below the use bound $\gamma = \max_i \gamma_e(y_{j,i})$, determine these values, so the versions are pairwise distinct strings, and $U$ must describe each of them with at most $2j$ bits.]
<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="Four versions of the prefix of length n of the approximation of A, one per stage s_i; they differ in the first gamma positions, since they compute different values of B on the followers; each has a description of length at most 2j"><text x="278" y="10" text-anchor="middle" class="label">positions below the use bound</text><text x="10.0" y="33.0" text-anchor="start" class="math" font-size="14">A<tspan class="mrm" font-size="9" dy="4">s₀</tspan></text><text x="40.0" y="33.0" text-anchor="start" class="mrm" font-size="14">↾ n</text><text x="78" y="33" class="label">0 followers in B</text><rect x="200" y="16" width="26" height="24" class="head-cell"/><text x="213.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="226" y="16" width="26" height="24" class="head-cell"/><text x="239.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="252" y="16" width="26" height="24" class="head-cell"/><text x="265.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="278" y="16" width="26" height="24" class="head-cell"/><text x="291.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="304" y="16" width="26" height="24" class="head-cell"/><text x="317.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="330" y="16" width="26" height="24" class="head-cell"/><text x="343.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="356" y="16" width="26" height="24" class="cell"/><text x="369.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="382" y="16" width="26" height="24" class="cell"/><text x="395.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="408" y="16" width="26" height="24" class="cell"/><text x="421.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="434" y="16" width="26" height="24" class="cell"/><text x="447.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="460" y="16" width="26" height="24" class="cell"/><text x="473.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="486" y="16" width="26" height="24" class="cell"/><text x="499.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="512" y="16" width="26" height="24" class="cell"/><text x="525.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="538" y="16" width="26" height="24" class="cell"/><text x="551.0" y="33.0" text-anchor="middle" class="mrm" font-size="13">1</text><text x="10.0" y="67.0" text-anchor="start" class="math" font-size="14">A<tspan class="mrm" font-size="9" dy="4">s₁</tspan></text><text x="40.0" y="67.0" text-anchor="start" class="mrm" font-size="14">↾ n</text><text x="78" y="67" class="label">1 follower in B</text><rect x="200" y="50" width="26" height="24" class="head-cell"/><text x="213.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="226" y="50" width="26" height="24" class="head-cell"/><text x="239.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="252" y="50" width="26" height="24" class="head-cell"/><text x="265.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="278" y="50" width="26" height="24" class="head-cell"/><text x="291.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="304" y="50" width="26" height="24" class="head-cell"/><text x="317.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="330" y="50" width="26" height="24" class="head-cell"/><text x="343.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="356" y="50" width="26" height="24" class="cell"/><text x="369.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="382" y="50" width="26" height="24" class="cell"/><text x="395.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="408" y="50" width="26" height="24" class="cell"/><text x="421.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="434" y="50" width="26" height="24" class="cell"/><text x="447.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="460" y="50" width="26" height="24" class="cell"/><text x="473.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="486" y="50" width="26" height="24" class="cell"/><text x="499.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="512" y="50" width="26" height="24" class="cell"/><text x="525.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="538" y="50" width="26" height="24" class="cell"/><text x="551.0" y="67.0" text-anchor="middle" class="mrm" font-size="13">1</text><text x="10.0" y="101.0" text-anchor="start" class="math" font-size="14">A<tspan class="mrm" font-size="9" dy="4">s₂</tspan></text><text x="40.0" y="101.0" text-anchor="start" class="mrm" font-size="14">↾ n</text><text x="78" y="101" class="label">2 followers in B</text><rect x="200" y="84" width="26" height="24" class="head-cell"/><text x="213.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="226" y="84" width="26" height="24" class="head-cell"/><text x="239.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="252" y="84" width="26" height="24" class="head-cell"/><text x="265.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="278" y="84" width="26" height="24" class="head-cell"/><text x="291.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="304" y="84" width="26" height="24" class="head-cell"/><text x="317.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="330" y="84" width="26" height="24" class="head-cell"/><text x="343.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="356" y="84" width="26" height="24" class="cell"/><text x="369.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="382" y="84" width="26" height="24" class="cell"/><text x="395.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="408" y="84" width="26" height="24" class="cell"/><text x="421.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="434" y="84" width="26" height="24" class="cell"/><text x="447.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="460" y="84" width="26" height="24" class="cell"/><text x="473.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="486" y="84" width="26" height="24" class="cell"/><text x="499.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="512" y="84" width="26" height="24" class="cell"/><text x="525.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="538" y="84" width="26" height="24" class="cell"/><text x="551.0" y="101.0" text-anchor="middle" class="mrm" font-size="13">1</text><text x="10.0" y="135.0" text-anchor="start" class="math" font-size="14">A<tspan class="mrm" font-size="9" dy="4">s₃</tspan></text><text x="40.0" y="135.0" text-anchor="start" class="mrm" font-size="14">↾ n</text><text x="78" y="135" class="label">3 followers in B</text><rect x="200" y="118" width="26" height="24" class="head-cell"/><text x="213.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="226" y="118" width="26" height="24" class="head-cell"/><text x="239.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="252" y="118" width="26" height="24" class="head-cell"/><text x="265.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="278" y="118" width="26" height="24" class="head-cell"/><text x="291.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="304" y="118" width="26" height="24" class="head-cell"/><text x="317.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="330" y="118" width="26" height="24" class="head-cell"/><text x="343.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="356" y="118" width="26" height="24" class="cell"/><text x="369.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="382" y="118" width="26" height="24" class="cell"/><text x="395.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="408" y="118" width="26" height="24" class="cell"/><text x="421.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="434" y="118" width="26" height="24" class="cell"/><text x="447.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="460" y="118" width="26" height="24" class="cell"/><text x="473.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="486" y="118" width="26" height="24" class="cell"/><text x="499.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="512" y="118" width="26" height="24" class="cell"/><text x="525.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="538" y="118" width="26" height="24" class="cell"/><text x="551.0" y="135.0" text-anchor="middle" class="mrm" font-size="13">0</text><text x="200" y="166" class="label">0</text><text x="356" y="166" text-anchor="middle" class="label">γ</text><text x="564" y="166" text-anchor="middle" class="label">n</text><text x="200" y="192" class="label">pairwise distinct strings of length n, each of complexity at most 2j:</text><text x="200" y="208" class="label">together they use at least k · 2⁻²ʲ of the domain of U</text></svg>
:::

The fixed point theorem gives the construction access to a reduction of the set it builds, and the strategies for all $j$ take care of the unknown constants $b$ and $d$.

:::quiz[amplification]
In the proof of :ref{#thm-wtt-amplification}, where is it used that the reduction is a weak truth-table reduction?

- [x] In the choice of $n_j$ above the uses $\gamma_e(y_{j,i})$ before any computation is seen: a change of $B$ on a follower then forces a change of $A$ below $n_j$.
- [ ] To make the request set $L$ bounded.

  The weight of $L$ is $\sum_j 2^{-j}$, whatever the reduction.
- [ ] To show that $B$ is c.e.

  $B$ is enumerated by the construction, whatever the reduction.

---

Why does the strategy $S_j$ need $2^{2j} + 1$ followers?

- [x] Each version of $A_s \uh n_j$ has a description of length at most $2j$, hence weight at least $2^{-2j}$, and more than $2^{2j}$ distinct versions exceed the total weight $1$.
- [ ] Because $K(n_j) \leq 2j$.

  The request gives $K(n_j) \leq j + d$; the bound $2j$ concerns the versions of $A \uh n_j$.
- [ ] To make the followers larger than $2j$.

  The size of the followers plays no role; their number does.
:::

## Turing reductions: the decanter method

For a Turing reduction, the use of the computation of $B(y)$ is not bounded in advance, and the argument above fails. Suppose that we describe $n$ above the current use. The opponent, who controls the approximation of $A$, can first change $A$ below the use, so that the new computation of $B(y)$ has a use larger than $n$, and only then let $U$ describe the new prefix $A \uh n$. When we enumerate $y$ into $B$, the approximation of $A$ must change below the new use, but possibly above $n$, so that $A \uh n$ need not change again. Our description of $n$ has forced a single description by $U$, and the weight we spent is lost.

The **decanter method** of Downey, Hirschfeldt, Nies and Stephan avoids this loss by loading weight gradually. Instead of one description of weight $2^{-j}$, the strategy gives descriptions of small weight to many numbers beyond the current use, waiting each time for $U$ to describe the current prefix. If the use moves, only the last small piece is wasted: the numbers already described by $U$ remain useful, since the change of $A$ below the use forces a second version of their prefixes. Such a set of numbers, whose prefixes are described at least twice, is called a 2-set. A strategy is given a goal and a garbage quota; each time the use moves, the size of the pieces is halved, so the total garbage is bounded by the quota.

To obtain more versions, the procedures are nested, as the followers are in the proof above. A procedure that builds a $j$-set chooses a follower, calls procedures that build $(j-1)$-sets beyond its use, and enumerates its follower when they have reached their goal, turning their union into a $j$-set; if its use moves first, the change does the same at no cost. The weights flow down from the innermost procedure to the outermost, like wine poured through a stack of decanters, which gives the method its name. With $j$ large enough, a $j$-set of weight $\tfrac12$ is impossible, and the method proves that **no K-trivial set is Turing complete** (Downey, Hirschfeldt, Nies and Stephan; Downey and Hirschfeldt, Theorem 11.3.1).

To prove lowness, there is no set $B$ to enumerate. Nies's **golden run** method replaces the followers by computations with oracle $A$: a procedure believes a computation $U^{A_s}(\sigma)$, or $\Phi^{A_s}_e(e)$, only after it has loaded weight beyond its use, so that a later change of $A$ below the use costs the opponent a definite amount of weight. The procedures form a tree of nested runs. A counting argument, the same as in the decanter method, shows that some run, the golden run, is never cancelled, never reaches its goal, and has all the subprocedures it calls return; the computations certified within this run yield a bounded request set that proves lowness. The golden run exists, but it cannot be found effectively, and the theorem is not uniform: a constant witnessing lowness for K cannot be computed from a c.e. index of a K-trivial set and its constant of K-triviality (Nies, Corollary 5.5.6).

## The main theorem

:::theorem[Nies; Hirschfeldt, Nies]{#thm-ktrivial-lowk}
Every K-trivial set is low for K.
:::

The proof, by the golden run method, is admitted here; see Nies (2005), Nies, *Computability and Randomness*, Section 5.4 (Theorem 5.4.1), and Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Section 11.4 (Theorems 11.4.1 and 11.4.9). Bienvenu and Shen (2015) present the proof as a game between two players who increase weights, which separates the combinatorics from the computability. Granting the theorem, the following consequences are immediate.

:::corollary{#cor-ktrivial-equivalent}
For a set $A$, the following are equivalent:

1. $A$ is K-trivial;
2. $A$ is low for K;
3. $A$ is low for Martin-Löf randomness;
4. $A$ is a base for randomness.

The K-trivial sets form an ideal of the Turing degrees: they are closed downward under $\leq_T$, and under $\oplus$.
:::

:::proof{of=cor-ktrivial-equivalent}
(1 ⇔ 2) by :ref{#thm-ktrivial-lowk} and :ref{#prop-lowness-implications} (1); the other equivalences by :ref{#cor-lowness-equivalent}. Closure downward holds for low for K sets by :ref{#prop-lowness-implications} (4), and closure under join for K-trivial sets by :ref{#prop-k-trivial-join}.
:::

Downward closure is not apparent from the definition of K-triviality, and closure under join is not apparent from the definition of lowness for K; the equivalence yields both. The equivalence also transfers results proved for one notion to the others: K-trivial sets are low in the sense of the jump, by the exercise of the lesson on lowness. In the other direction, the hungry sets theorem alone shows that sets that are low for randomness are K-trivial, hence $\Delta^0_2$ by :ref{#cor-k-trivial-delta2}, which answers a question of Kučera and Terwijn.

## Further results

The golden run method gives more information on K-trivial sets. The following results are admitted, with references.

- **Superlowness.** Every K-trivial set $A$ is superlow: $A' \leq_{tt} \emptyset'$ (Nies; Nies, Corollary 5.5.4; Downey and Hirschfeldt, Theorem 11.4.1).
- **Cost functions.** A set is K-trivial if and only if it has a computable approximation that obeys $c_K$ (Nies; Nies, Theorem 5.5.2; Downey and Hirschfeldt, Theorem 11.5.3). This is the converse of :ref{#thm-obey-ktrivial}.
- **C.e. covers.** Every K-trivial set is truth-table reducible to a c.e. K-trivial set (Nies, Corollary 5.5.3). The ideal of K-trivial degrees is generated by its c.e. members, and its c.e. part has a $\Sigma^0_3$ index set (Downey and Hirschfeldt, Theorem 11.6.1).
- **Covering by random sets.** Hirschfeldt, Nies and Stephan proved that a c.e. set computed by an incomplete Martin-Löf random set is K-trivial, and Stephan asked whether the converse holds. The answer is positive: every K-trivial set is computed by an incomplete Martin-Löf random set, and in fact a single incomplete random set computes all of them. This follows from the theorem of Bienvenu, Greenberg, Kučera, Nies and Turetsky (2016) that the c.e. K-trivial sets are computed by every random set that is not "Oberwolfach random", and the theorem of Day and Miller that some incomplete random set is not Oberwolfach random; see Bienvenu, Day, Greenberg, Kučera, Miller, Nies and Turetsky (2014).

The last result gives another route to :ref{#thm-ktrivial-lowk}, as Bienvenu, Day, Greenberg, Kučera, Miller, Nies and Turetsky observe. Let $A$ be K-trivial. By the result on c.e. covers in its Turing form, which Bienvenu, Downey, Merkle and Nies prove with Solovay functions (see the lesson on Solovay functions), $A \leq_T C$ for a c.e. K-trivial set $C$. By the covering theorem, $C \leq_T Z$ for an incomplete random set $Z$, and by a theorem of Hirschfeldt, Nies and Stephan, $Z$ is then random relative to the c.e. set $C$, hence relative to $A$. So $A$ is a base for randomness, and it is low for K by :ref{#thm-hungry-sets}.

## Exercises

::::exercise{difficulty=1}
Show that no K-trivial set is Turing complete.

:::solution
By :ref{#thm-ktrivial-lowk}, a K-trivial set $A$ is low for K, and by the exercise of the lesson on lowness, $A' \leq_T \emptyset'$. A complete set $A$ has $A' \equiv_T \emptyset''$, which is not computable in $\emptyset'$. So $A$ is not complete. With :ref{#thm-solovay-ktrivial}, this gives a non-computable c.e. set that is not complete: a solution to Post's problem by a construction without injury.
:::
::::

::::exercise{difficulty=1}
Let $A$ be K-trivial, and let $B$ be K-trivial relative to $A$, that is, $K^A(B \uh n) \leq^+ K^A(n)$. Show that $B$ is K-trivial.

:::solution
By :ref{#thm-ktrivial-lowk}, $K \leq^+ K^A$, and $K^A \leq^+ K$ holds for every oracle. So $K(B \uh n) \leq^+ K^A(B \uh n) \leq^+ K^A(n) \leq^+ K(n)$.
:::
::::

## Notes and references

The amplification argument and the decanter method are due to Downey, Hirschfeldt, Nies and Stephan (2003), who proved that K-trivial sets are Turing incomplete; the weak truth-table case is Proposition 11.3.2 of Downey and Hirschfeldt. Nies (2005) introduced the golden run method and proved that K-trivial sets are low for K, with Hirschfeldt, and superlow. Nies, *Computability and Randomness*, Sections 5.4 and 5.5, and Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Sections 11.3–11.6, give the proofs. The covering problem was Problem 4.6 of Miller and Nies (2006).

- R. G. Downey, D. R. Hirschfeldt, A. Nies and F. Stephan, *Trivial reals*, in: Proceedings of the 7th and 8th Asian Logic Conferences, 2003, 103–131.
- A. Nies, *Lowness properties and randomness*, Advances in Mathematics 197 (2005), 274–305.
- D. R. Hirschfeldt, A. Nies and F. Stephan, *Using random sets as oracles*, Journal of the London Mathematical Society 75 (2007), 610–622.
- J. S. Miller and A. Nies, *Randomness and computability: open questions*, Bulletin of Symbolic Logic 12 (2006), 390–410.
- L. Bienvenu, A. R. Day, N. Greenberg, A. Kučera, J. S. Miller, A. Nies and D. Turetsky, *Computing K-trivial sets by incomplete random sets*, Bulletin of Symbolic Logic 20 (2014), 80–90.
- A. R. Day and J. S. Miller, *Density, forcing, and the covering problem*, preprint, arXiv:1304.2789, 2013.
- L. Bienvenu and A. Shen, *K-trivial, K-low and MLR-low sequences: a tutorial*, in: Fields of Logic and Computation II, Lecture Notes in Computer Science 9300, Springer, 2015.
- L. Bienvenu, R. Downey, A. Nies and W. Merkle, *Solovay functions and their applications in algorithmic randomness*, Journal of Computer and System Sciences 81 (2015), 1575–1591.
- L. Bienvenu, N. Greenberg, A. Kučera, A. Nies and D. Turetsky, *Coherent randomness tests and computing the K-trivial sets*, Journal of the European Mathematical Society 18 (2016), 773–812.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 5.4 and 5.5.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 11.3–11.6.
