---
title: The reduction and separation properties
summary: The reduction property for Π¹₁ sets, proved by stage comparison; Kleene's separation theorem for Σ¹₁ sets; disjoint Π¹₁ sets without Δ¹₁ separation, and the failure of reduction for Σ¹₁ sets.
duration: 35
prerequisites: [norms]
---

Two c.e. sets $B$ and $C$ can be **reduced** to disjoint c.e. sets $B' \subseteq B$ and $C' \subseteq C$ with the same union: enumerate both sets simultaneously and put each element in the set where it appears first. Taking complements, two disjoint co-c.e. sets are separated by a computable set. On the other hand, there are disjoint c.e. sets that no computable set separates. This lesson proves the same three facts one level up, with $\Pi^1_1$ in place of c.e. and $\Delta^1_1$ in place of computable: the $\Pi^1_1$ sets have the reduction property, two disjoint $\Sigma^1_1$ sets are separated by a $\Delta^1_1$ set, and some disjoint $\Pi^1_1$ sets are not.

The first two results use stage comparison (:ref{#thm-stage-comparison}) in place of the simultaneous enumeration. The third is a diagonal argument against all $\Delta^1_1$ sets, each of them described by a pair of $\Pi^1_1$ indices, one for the set and one for its complement, as a computable set is described by a pair of c.e. indices.

## The reduction property

The stages of a single $\Pi^1_1$ set, combining $B$ on the even numbers and $C$ on the odd numbers, play the role of the common enumeration, and stage comparison decides which of $2n$ and $2n + 1$ comes first. Ties must be broken in favor of one side, here $B$, so that the two parts are disjoint.

:::figure[The reduction of :ref{#thm-pi11-reduction}. For each $n$, the stages of $2n$ (circle) and $2n + 1$ (square) are compared. The number $n$ goes to $B'$ if $2n$ enters no later than $2n + 1$, ties included, and to $C'$ if $2n + 1$ enters strictly first; if neither enters, $n \notin B \cup C$.]
<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="For each n, the stages of 2n and 2n+1 on an ordinal axis; n goes to B prime when 2n arrives no later than 2n+1, and to C prime when 2n+1 arrives strictly first"><line x1="70" y1="34" x2="400" y2="34" class="axis"/><line x1="400" y1="34" x2="418" y2="34" class="axis" stroke-dasharray="2 3"/><text x="22" y="39" class="math" font-size="15">n</text><text x="34" y="39" class="mrm" font-size="15">= 0</text><circle cx="136.0" cy="34" r="6" class="accent-fill"/><rect x="296.0" y="29" width="10" height="10" class="ink-fill"/><text x="476" y="39" class="label">ρ₀ ≤ ρ₁: 0 ∈ B′</text><line x1="70" y1="80" x2="400" y2="80" class="axis"/><line x1="400" y1="80" x2="418" y2="80" class="axis" stroke-dasharray="2 3"/><text x="22" y="85" class="math" font-size="15">n</text><text x="34" y="85" class="mrm" font-size="15">= 1</text><circle cx="450.0" cy="80" r="6" class="accent-fill"/><rect x="230.0" y="75" width="10" height="10" class="ink-fill"/><text x="476" y="85" class="label">ρ₂ = ∞ > ρ₃: 1 ∈ C′</text><line x1="70" y1="126" x2="400" y2="126" class="axis"/><line x1="400" y1="126" x2="418" y2="126" class="axis" stroke-dasharray="2 3"/><text x="22" y="131" class="math" font-size="15">n</text><text x="34" y="131" class="mrm" font-size="15">= 2</text><circle cx="356.0" cy="126" r="6" class="accent-fill"/><rect x="352.0" y="108" width="8" height="8" class="ink-fill"/><text x="476" y="131" class="label">ρ₄ = ρ₅: 2 ∈ B′</text><line x1="70" y1="172" x2="400" y2="172" class="axis"/><line x1="400" y1="172" x2="418" y2="172" class="axis" stroke-dasharray="2 3"/><text x="22" y="177" class="math" font-size="15">n</text><text x="34" y="177" class="mrm" font-size="15">= 3</text><circle cx="450.0" cy="172" r="6" class="accent-fill"/><rect x="446.0" y="154" width="8" height="8" class="ink-fill"/><text x="476" y="177" class="label">both ∞: 3 ∉ B ∪ C</text><text x="70" y="210" text-anchor="middle" class="mrm" font-size="13">0</text><text x="400" y="210" text-anchor="middle" class="mrm" font-size="13">ω<tspan font-size="9" dy="-6">CK</tspan><tspan font-size="9" dy="9" dx="-12">1</tspan></text><text x="450" y="210" text-anchor="middle" class="mrm" font-size="13">∞</text><circle cx="74" cy="228" r="5" class="accent-fill"/><text x="84" y="232" class="label">stage of 2n (finite iff n ∈ B)</text><rect x="290" y="223" width="10" height="10" class="ink-fill"/><text x="306" y="232" class="label">stage of 2n + 1 (finite iff n ∈ C)</text></svg>
:::

:::theorem[Reduction property]{#thm-pi11-reduction}
For all $\Pi^1_1$ sets $B$ and $C$, there are disjoint $\Pi^1_1$ sets $B' \subseteq B$ and $C' \subseteq C$ with $B' \cup C' = B \cup C$.
:::

:::proof{of=thm-pi11-reduction}
Let $A = \{ 2n : n \in B \} \cup \{ 2n + 1 : n \in C \}$, a $\Pi^1_1$ set, with stages given by a sequence of trees as in :ref{#def-pi11-stage}, and let
$$
B' = \{ n : 2n \leq^* 2n + 1 \}, \qquad C' = \{ n : 2n + 1 <^* 2n \}.
$$
Both are $\Pi^1_1$ by :ref{#thm-stage-comparison}. If $n \in B'$, then $2n \in A$, so $n \in B$; similarly $C' \subseteq C$. They are disjoint, since $\rho_{2n} \leq \rho_{2n+1}$ and $\rho_{2n+1} < \rho_{2n}$ are incompatible. If $n \in B \cup C$, then $\rho_{2n}$ and $\rho_{2n+1}$ are not both $\infty$: if $\rho_{2n} \leq \rho_{2n+1}$, then $\rho_{2n}$ is an ordinal and $n \in B'$; otherwise $\rho_{2n+1} < \rho_{2n}$ and $n \in C'$.
:::

:::quiz[the reduction property]
In the proof of :ref{#thm-pi11-reduction}, why is $B'$ defined with $\leq^*$ and $C'$ with $<^*$, rather than both with $\leq^*$?

- [x] With $\leq^*$ on both sides, a number $n$ such that $2n$ and $2n + 1$ enter $A$ at the same stage would belong to both $B'$ and $C'$; the strict comparison breaks ties in favor of $B'$.
- [ ] Because $\leq^*$ is $\Pi^1_1$ and $<^*$ is not, or conversely.

  Both relations are $\Pi^1_1$, by :ref{#thm-stage-comparison}.
- [ ] To obtain $C' \subseteq C$.

  Both $2n + 1 \leq^* 2n$ and $2n + 1 <^* 2n$ imply $2n + 1 \in A$, hence $n \in C$.

---

If $n \in B \setminus C$, why does $n$ belong to $B'$?

- [x] Because $\rho_{2n}$ is an ordinal and $\rho_{2n+1} = \infty$, so $2n \leq^* 2n + 1$.
- [ ] Because $B' = B \setminus C$.

  $B'$ may also contain elements of $B \cap C$, those with $\rho_{2n} \leq \rho_{2n+1}$.
- [ ] Because $\rho_{2n} = \rho_{2n+1}$.

  Here $\rho_{2n}$ is an ordinal and $\rho_{2n+1} = \infty$; the case of equal stages is the case of a tie, also resolved in favor of $B'$.
:::

## Separation

Separation follows from reduction by taking complements, as for c.e. sets: the reduction property of $\Sigma^0_1$ sets gives the separation of disjoint $\Pi^0_1$ sets by computable sets. Two disjoint $\Sigma^1_1$ sets have $\Pi^1_1$ complements that cover $\nat$; reducing them gives a partition of $\nat$ into two $\Pi^1_1$ sets, each the complement of the other.

:::corollary[Kleene's separation theorem]{#cor-sigma11-separation}
For all disjoint $\Sigma^1_1$ sets $D$ and $E$, there is a $\Delta^1_1$ set $F$ with $D \subseteq F$ and $F \cap E = \emptyset$.
:::

:::proof{of=cor-sigma11-separation}
The complements $\overline D$ and $\overline E$ are $\Pi^1_1$, and their union is $\nat$, since $D \cap E = \emptyset$. Let $B' \subseteq \overline D$ and $C' \subseteq \overline E$ be given by :ref{#thm-pi11-reduction}: they are disjoint $\Pi^1_1$ sets with union $\nat$, so each is the complement of the other, and both are $\Delta^1_1$. Let $F = C'$. Then $F \subseteq \overline E$, so $F \cap E = \emptyset$. If $n \in D$, then $n \notin \overline D \supseteq B'$, so $n \in C' = F$.
:::

By Kleene's theorem, the separating set is hyperarithmetic. Taking $E = \overline D$ for a $\Delta^1_1$ set $D$ shows that the corollary contains the statement "$\Sigma^1_1 \cap \Pi^1_1 = \Delta^1_1$" as a special case, and it is strictly more: the sets $D$ and $E$ need not be complements of each other.

In classical descriptive set theory, the corresponding theorem is Lusin's separation theorem: two disjoint analytic sets are separated by a Borel set.

## Inseparable Π¹₁ sets

The separation property fails for $\Pi^1_1$ sets, exactly as two disjoint c.e. sets need not be separated by a computable set. The proof diagonalizes against every candidate separating set $F$, using the universal $\Pi^1_1$ set $U$ of :ref{#prop-pi11-not-sigma11}, whose sections $U_e = \{ n : \langle e, n \rangle \in U \}$ include all the $\Pi^1_1$ sets. A $\Delta^1_1$ set $F$ is determined by a pair $\langle a, b \rangle$ with $U_a = \overline F$ and $U_b = F$, and the number $\langle a, b \rangle$ itself is the witness that $F$ fails.

:::proposition{#prop-pi11-inseparable}
There are disjoint $\Pi^1_1$ sets $Y_0$ and $Y_1$ such that no $\Delta^1_1$ set $F$ satisfies $Y_0 \subseteq F$ and $F \cap Y_1 = \emptyset$.
:::

:::proof{of=prop-pi11-inseparable}
For $e = \langle a, b \rangle$, let $e \in X_0$ if $e \in U_a$, and $e \in X_1$ if $e \in U_b$. Both sets are $\Pi^1_1$. Let $Y_0 \subseteq X_0$ and $Y_1 \subseteq X_1$ be given by :ref{#thm-pi11-reduction}. Suppose that a $\Delta^1_1$ set $F$ satisfies $Y_0 \subseteq F$ and $F \cap Y_1 = \emptyset$. Choose $a$ with $U_a = \overline F$ and $b$ with $U_b = F$, possible since both are $\Pi^1_1$, and let $e = \langle a, b \rangle$. If $e \in F$, then $e \in U_b$, so $e \in X_1$, and $e \notin U_a$, so $e \notin X_0 \supseteq Y_0$; since $Y_0 \cup Y_1 = X_0 \cup X_1$, $e \in Y_1$, contradicting $F \cap Y_1 = \emptyset$. If $e \notin F$, then $e \in X_0 \setminus X_1$, so $e \in Y_0 \subseteq F$: a contradiction. So no $\Delta^1_1$ set separates $Y_0$ from $Y_1$.
:::

:::quiz[inseparable Π¹₁ sets]
In the proof of :ref{#prop-pi11-inseparable}, why is the reduction property applied to $X_0$ and $X_1$, instead of separating $X_0$ and $X_1$ directly?

- [x] Because $X_0$ and $X_1$ need not be disjoint, and the separation question only makes sense for disjoint sets; reduction makes them disjoint while keeping their union, which the argument uses.
- [ ] Because $X_0$ and $X_1$ are not $\Pi^1_1$.

  They are $\Pi^1_1$, as preimages of $U$ under computable maps.
- [ ] Because reduction makes the sets $\Delta^1_1$.

  The sets $Y_0$ and $Y_1$ are $\Pi^1_1$; if they were $\Delta^1_1$, $Y_0$ itself would separate them.
:::

Reduction and separation thus sit on opposite sides: the $\Pi^1_1$ sets have the reduction property and not the separation property, and the $\Sigma^1_1$ sets have the separation property and, by the first exercise, not the reduction property. The same pattern holds for the c.e. and co-c.e. sets, and, classically, for the co-analytic and analytic sets.

## Exercises

::::exercise{difficulty=1}
Show that the reduction property fails for $\Sigma^1_1$ sets: there are $\Sigma^1_1$ sets $D$ and $E$ for which no disjoint $\Sigma^1_1$ sets $D' \subseteq D$ and $E' \subseteq E$ have union $D \cup E$.

:::solution
Let $Y_0$ and $Y_1$ be given by :ref{#prop-pi11-inseparable}, and let $D = \overline{Y_0}$ and $E = \overline{Y_1}$, which are $\Sigma^1_1$ with $D \cup E = \nat$. If $D' \subseteq D$ and $E' \subseteq E$ were disjoint $\Sigma^1_1$ sets with union $\nat$, each would be the complement of the other, hence $\Delta^1_1$. Then $E'$ would contain $Y_0$, since $Y_0 \cap D' \subseteq Y_0 \cap D = \emptyset$, and $E' \cap Y_1 \subseteq E \cap Y_1 = \emptyset$: a $\Delta^1_1$ separation.
:::
::::

::::exercise{difficulty=2}
Let $(B_k)$ be a sequence of sets such that $\{ \langle n, k \rangle : n \in B_k \}$ is $\Pi^1_1$. Show that there are pairwise disjoint sets $B'_k \subseteq B_k$ with $\bigcup_k B'_k = \bigcup_k B_k$ and $\{ \langle n, k \rangle : n \in B'_k \}$ $\Pi^1_1$.

:::solution
Apply :ref{#thm-stage-comparison} to $A = \{ \langle n, k \rangle : n \in B_k \}$, and let $n \in B'_k$ if $\langle n, k \rangle \leq^* \langle n, j \rangle$ for every $j$, and $\langle n, k \rangle <^* \langle n, j \rangle$ for every $j < k$. This is $\Pi^1_1$, since a universal number quantifier in front of a $\Pi^1_1$ formula gives a $\Pi^1_1$ formula. If $n \in B'_k$, then $\langle n, k \rangle \in A$, so $n \in B_k$. If $n \in B'_k \cap B'_j$ with $j < k$, the first condition for $j$ gives $\rho_{\langle n, j \rangle} \leq \rho_{\langle n, k \rangle}$ and the second condition for $k$ gives $\rho_{\langle n, k \rangle} < \rho_{\langle n, j \rangle}$, a contradiction. If $n \in \bigcup_k B_k$, the stages $\rho_{\langle n, k \rangle}$ are not all $\infty$; let $\alpha$ be the least of them and $k$ the least number with $\rho_{\langle n, k \rangle} = \alpha$. Then $n \in B'_k$. This is the selection of the next lesson, applied to the relation $n \in B_k$.
:::
::::

## Notes and references

The separation theorem for analytic sets is due to Lusin (1927), and the reduction principle was introduced by Kuratowski (1936) in the classical hierarchy. Kleene (1950) proved that disjoint c.e. sets need not be separated by a computable set, and Kleene (1955) that disjoint $\Sigma^1_1$ sets are separated by a hyperarithmetic set. Addison (1958) stated the effective reduction and separation results systematically, following the classical work and Kleene's, and stressed the analogy between the two hierarchies. Moschovakis derives reduction and separation from the prewellordering property in exercises 4B.10–4B.12, with these attributions in his historical remark 13 of Section 4G.

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- J. W. Addison, *Separation principles in the hierarchies of classical and effective descriptive set theory*, Fundamenta Mathematicae 46 (1958), 123–135.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Section 4B.
