---
title: Computable reducibility
summary: Reductions that use a single instance of the stronger problem; computable and strong computable reducibility; problems that admit computable solutions; König's lemma is ω-reducible but not computably reducible to the jump; computable reducibility and provability over RCA₀ are incomparable.
duration: 30
prerequisites: [preservation]
---

An ω-reduction may use any number of instances of $\mathsf Q$, each built from the solutions of the previous ones. Dzhafarov proposed to count: a **computable reduction** solves an instance of $\mathsf P$ with a single instance of $\mathsf Q$. It is the analogue for problems of the reductions of complexity theory, where one instance of a problem is transformed into one instance of another. This finer notion separates problems that are equivalent in ω-models, such as König's lemma and the jump.

## Computable and strong computable reducibility

A computable reduction of $\mathsf P$ to $\mathsf Q$ has two steps. In the forward step, an instance $X$ of $\mathsf P$ is transformed into an instance $\widetilde X$ of $\mathsf Q$. In the backward step, an arbitrary solution $\widetilde Y$ to $\widetilde X$ is transformed back into a solution to $X$, with the help of $X$ itself.

:::definition{#def-computable-reducible}
Let $\mathsf P$ and $\mathsf Q$ be problems.

1. $\mathsf P$ is **computably reducible** to $\mathsf Q$, written $\mathsf P \leq_c \mathsf Q$, if every instance $X$ of $\mathsf P$ computes an instance $\widetilde X$ of $\mathsf Q$ such that, for every solution $\widetilde Y$ to $\widetilde X$, the set $X \oplus \widetilde Y$ computes a solution to $X$.
2. $\mathsf P$ is **strongly computably reducible** to $\mathsf Q$, written $\mathsf P \leq_{sc} \mathsf Q$, if moreover $\widetilde Y$ alone computes a solution to $X$.
3. $\mathsf P$ **admits computable solutions** if every instance computes a solution to itself.
:::

:::figure[Computable and strong computable reductions of $\mathsf P$ to $\mathsf Q$. The instance $\widetilde X$ depends on $X$, and the backward computation must succeed for every solution $\widetilde Y$ to $\widetilde X$. In a strong reduction, the backward step has no access to $X$.]
<svg class="fig" viewBox="0 0 660 262" width="660" role="img" aria-label="Diagrams of a computable reduction and of a strong computable reduction of P to Q"><defs><marker id="ah-cred" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker><marker id="ah-creda" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><text x="90" y="34" text-anchor="middle" class="math" font-size="18">P</text><text x="250" y="34" text-anchor="middle" class="math" font-size="18">Q</text><text x="170.0" y="250" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" dx="5">≤</tspan><tspan class="mrm" font-size="11" dy="4">c</tspan><tspan dx="5" dy="-4">Q</tspan></text><rect x="68" y="50" width="44" height="30" rx="6" class="cell"/><text x="90" y="71" text-anchor="middle" class="math" font-size="17">X</text><rect x="228" y="50" width="44" height="30" rx="6" class="cell"/><text x="250" y="71" text-anchor="middle" class="math" font-size="17">X̃</text><rect x="228" y="180" width="44" height="30" rx="6" class="cell"/><text x="250" y="201" text-anchor="middle" class="math" font-size="17">Ỹ</text><rect x="68" y="180" width="44" height="30" rx="6" class="head-cell"/><text x="90" y="201" text-anchor="middle" class="math" font-size="17">Y</text><line x1="114" y1="65" x2="224" y2="65" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cred)"/><text x="170.0" y="57" text-anchor="middle" class="label">X computes</text><line x1="250" y1="82" x2="250" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-cred)"/><line x1="90" y1="82" x2="90" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-cred)"/><text x="258" y="133.0" text-anchor="start" class="label">any solution</text><text x="82" y="133.0" text-anchor="end" class="label">a solution</text><line x1="226" y1="195" x2="116" y2="195" class="accent-stroke" stroke-width="1.6" marker-end="url(#ah-cred)"/><text x="170.0" y="224" text-anchor="middle" class="label">X ⊕ Ỹ computes</text><path d="M108,82 C160,120 170,160 150,191" class="accent-stroke" stroke-width="1.2" stroke-dasharray="2 3" marker-end="url(#ah-creda)"/><text x="170" y="132" text-anchor="start" class="label">X is used</text><text x="410" y="34" text-anchor="middle" class="math" font-size="18">P</text><text x="570" y="34" text-anchor="middle" class="math" font-size="18">Q</text><text x="490.0" y="250" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" dx="5">≤</tspan><tspan class="mrm" font-size="11" dy="4">sc</tspan><tspan dx="5" dy="-4">Q</tspan></text><rect x="388" y="50" width="44" height="30" rx="6" class="cell"/><text x="410" y="71" text-anchor="middle" class="math" font-size="17">X</text><rect x="548" y="50" width="44" height="30" rx="6" class="cell"/><text x="570" y="71" text-anchor="middle" class="math" font-size="17">X̃</text><rect x="548" y="180" width="44" height="30" rx="6" class="cell"/><text x="570" y="201" text-anchor="middle" class="math" font-size="17">Ỹ</text><rect x="388" y="180" width="44" height="30" rx="6" class="head-cell"/><text x="410" y="201" text-anchor="middle" class="math" font-size="17">Y</text><line x1="434" y1="65" x2="544" y2="65" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cred)"/><text x="490.0" y="57" text-anchor="middle" class="label">X computes</text><line x1="570" y1="82" x2="570" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-cred)"/><line x1="410" y1="82" x2="410" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-cred)"/><text x="578" y="133.0" text-anchor="start" class="label">any solution</text><text x="402" y="133.0" text-anchor="end" class="label">a solution</text><line x1="546" y1="195" x2="436" y2="195" class="accent-stroke" stroke-width="1.6" marker-end="url(#ah-cred)"/><text x="490.0" y="224" text-anchor="middle" class="label">Ỹ computes</text></svg>
:::

Strong reducibility forbids the use of the original instance in the backward step: all the information needed must be coded in the solutions of $\mathsf Q$. Both relations are preorders (for $\leq_c$, see the first exercise), and $\mathsf P \leq_{sc} \mathsf Q$ implies $\mathsf P \leq_c \mathsf Q$. The terminology of item 3 is that of Dzhafarov and Mummert; they reserve the term "computably true" for the weaker property that every computable instance has a computable solution.

Some examples:

- $\mathsf{WKL} \leq_{sc} \mathsf{KL}$: an infinite binary tree is an infinite finitely branching tree with the same paths. Take $\widetilde X = X$, and the solution itself.
- $\mathsf{RT}^1_2$ and $\mathsf{RT}^1_{<\infty}$ admit computable solutions: an instance computes its finitely many color classes, one of which is infinite.
- $\mathsf{Id} \leq_c \mathsf Q$ for every problem $\mathsf Q$ with a computable instance $V$: take $\widetilde X = V$, and $X$ itself as the solution, computed by $X \oplus \widetilde Y$. The reduction uses $X$ in the backward step, and need not be strong; the next lesson studies when it can be.

:::proposition{#prop-c-omega}
If $\mathsf P \leq_c \mathsf Q$, then $\mathsf P \leq_\omega \mathsf Q$. A problem $\mathsf P$ admits computable solutions if and only if $\mathsf P \leq_c \mathsf{Id}$, if and only if every Turing ideal satisfies it.
:::

:::proof{of=prop-c-omega}
Let $\mathcal I \models \mathsf Q$ and $X \in \mathcal I$ an instance of $\mathsf P$. The instance $\widetilde X \leq_T X$ belongs to $\mathcal I$, so it has a solution $\widetilde Y \in \mathcal I$; then $X \oplus \widetilde Y \in \mathcal I$ computes a solution to $X$, which belongs to $\mathcal I$.

If $\mathsf P$ admits computable solutions, take $\widetilde X = X$ as an instance of $\mathsf{Id}$. Conversely, if $\mathsf P \leq_c \mathsf{Id}$, the only solution to $\widetilde X$ is $\widetilde X \leq_T X$, so $X$ computes a solution. If every Turing ideal satisfies $\mathsf P$, so does $\{ Y : Y \leq_T X \}$, so $X$ computes a solution. Conversely, if $\mathsf P$ admits computable solutions, every instance in a Turing ideal computes a solution, which belongs to the ideal.
:::

The game of the previous lesson refines into a hierarchy: write $\mathsf P \leq^n_\omega \mathsf Q$ if Player 2 has a strategy in $G(\mathsf Q \rightarrow \mathsf P)$ that wins within $n + 1$ rounds, that is, after at most $n$ instances of $\mathsf Q$. Then $\mathsf P \leq^0_\omega \mathsf Q$ means that $\mathsf P$ admits computable solutions, and $\mathsf P \leq_c \mathsf Q$ implies $\mathsf P \leq^1_\omega \mathsf Q$, with equivalence when $\mathsf Q$ has a computable instance. Dzhafarov and Mummert call $\mathsf P \leq^n_\omega \mathsf Q$, for $n \geq 1$, computable reducibility to $n$ applications of $\mathsf Q$, up to the same proviso on instances.

## König's lemma and the jump

:::proposition{#prop-kl-not-c-j}
$\mathsf{KL} \leq^2_\omega \mathsf J$, but $\mathsf{KL} \not\leq_c \mathsf J$.
:::

:::proof{of=prop-kl-not-c-j}
Player 2 plays $T$, then $T'$, and receives $T''$, which computes a path through $T$, as in :ref{#prop-kl-j}.

No set is PA relative to itself, since it would compute a function that differs from every function it computes; so by :ref{#thm-konig-strength} there is an infinite computable finitely branching tree $T$ without $\emptyset'$-computable path. Every instance $\widetilde X \leq_T T$ of $\mathsf J$ is computable, so its solution $\widetilde X'$ is computable in $\emptyset'$, and $T \oplus \widetilde X' \leq_T \emptyset'$ computes no path through $T$.
:::

The proof is a counting argument on the resources of a single application: a computable instance of $\mathsf J$ yields at most $\emptyset'$, while some computable instance of $\mathsf{KL}$ needs more. It depends on how instances of $\mathsf{KL}$ are presented. If an instance is a pair $(T, h)$ of a finitely branching tree and a function $h$ bounding its successors, then extendibility in $T$ is $\Pi^0_1(T \oplus h)$, and $(T \oplus h)'$ computes the leftmost path; this bounded version of $\mathsf{KL}$ is computably reducible to $\mathsf J$. Without the bound, the first jump is spent computing it.

:::quiz[computable reducibility]
In the proof of :ref{#prop-kl-not-c-j}, why does a single instance of $\mathsf J$ not suffice?

- [x] Because the instance must be computable from the computable tree $T$, so it is computable, and its jump is computable in $\emptyset'$, which computes no path through $T$.
- [ ] Because $\mathsf J$ has a unique solution.

  Uniqueness is not the issue: the unique solution $\widetilde X'$ is computable in $\emptyset'$, which is not enough.
- [ ] Because $T$ has no computable path.

  Many trees without computable paths have paths computable in $\emptyset'$; $T$ was chosen to have none.
:::

So computable reducibility is strictly finer than ω-reducibility. It is also incomparable with provability over $\mathsf{RCA}_0$, in both directions:

- $\mathsf{RCA}_0$ proves that if every set has a Turing jump, then König's lemma holds (:ref{#thm-aca-equivalents} and :ref{#thm-konig-aca}); yet $\mathsf{KL} \not\leq_c \mathsf J$. A proof may use its hypothesis several times.
- $\mathsf{RT}^1_{<\infty}$ admits computable solutions, so $\mathsf{RT}^1_{<\infty} \leq_c \mathsf{Id}$; yet $\mathsf{RCA}_0$ does not prove it, since it is equivalent to $\Sigma^0_2$ collection (:ref{#thm-hirst}). A computable reduction may rely on properties of the standard natural numbers, here an induction on the number of colors, that $\mathsf{RCA}_0$ does not prove.

In practice, many implications over $\mathsf{RCA}_0$ are proved by computable reductions that formalize in $\mathsf{RCA}_0$, and the two kinds of information complement each other.

## Exercises

::::exercise{difficulty=1}
Show that $\leq_c$ is transitive.

:::solution
Let $\mathsf P \leq_c \mathsf Q \leq_c \mathsf R$, and $X$ an instance of $\mathsf P$. Let $\widetilde X \leq_T X$ be the instance of $\mathsf Q$, and $\widehat X \leq_T \widetilde X$ the instance of $\mathsf R$ given by the second reduction for $\widetilde X$. Then $\widehat X \leq_T X$. For every solution $\widehat Y$ to $\widehat X$, $\widetilde X \oplus \widehat Y$ computes a solution $\widetilde Y$ to $\widetilde X$, and $X \oplus \widetilde Y$ computes a solution to $X$. Since $\widetilde X \leq_T X$, the set $X \oplus \widehat Y$ computes $X \oplus \widetilde Y$, hence a solution to $X$.
:::
::::

::::exercise{difficulty=2}
Let $\mathsf{KL}_b$ be the problem whose instances are the pairs $(T, h)$ of an infinite finitely branching tree $T$ and a function $h$ such that $\sigma^\frown n \in T$ implies $n \leq h(\sigma)$, with the paths through $T$ as solutions. Show that $\mathsf{KL}_b \leq_c \mathsf J$, and that $\mathsf{KL} \leq_c \mathsf J \times \mathsf{KL}_b$ fails.

:::solution
Let $Z = T \oplus h$. A node $\sigma$ is extendible if and only if, for every $n$, some extension of $\sigma$ of length $|\sigma| + n$ lies in $T$; since the values of such extensions are bounded by $h$, there are finitely many candidates, listed computably in $h$, and extendibility is $\Pi^0_1(Z)$. So $Z'$ computes the set of extendible nodes, and the path that always takes the least extendible successor. Take $\widetilde X = Z$ as an instance of $\mathsf J$. For the second statement, let $T$ be the computable tree of :ref{#prop-kl-not-c-j}, with no $\emptyset'$-computable path. An instance of $\mathsf J \times \mathsf{KL}_b$ computable in $T$ is a pair of a computable set $V$ and a computable bounded instance $(S, h)$. The jump $V'$ is computable in $\emptyset'$, and $(S, h)$ has a path computable in $(S \oplus h)' \leq_T \emptyset'$, by the first part. So some solution to the instance is computable in $\emptyset'$, and together with $T$ computes no path through $T$.
:::
::::

## Notes and references

Computable reducibility was introduced by Dzhafarov (2015) in his study of cohesiveness, together with strong computable reducibility; Hirschfeldt, *Slicing the Truth*, Section 2.2, and Dzhafarov and Mummert, Sections 4.2 and 4.4, present both. The comparison with provability over $\mathsf{RCA}_0$ is Section 5.11 of Dzhafarov and Mummert, and the reductions to several applications are their Section 4.5.

Dzhafarov and Mummert (Proposition 4.2.9) state that $\mathsf{KL}$ is computably equivalent to $\mathsf J$. Their proof computes the extendible nodes of a finitely branching tree $T$ from $T'$, which is correct when $T$ comes with a bound on its successors (their Proposition 2.8.5) but not in general, as :ref{#prop-kl-not-c-j} shows; the correct statement is the one for $\mathsf{KL}_b$ in the last exercise.

- D. D. Dzhafarov, *Cohesive avoidance and strong reductions*, Proceedings of the American Mathematical Society 143 (2015), 869–876.
- D. R. Hirschfeldt and C. G. Jockusch, *On notions of computability-theoretic reduction between Π¹₂ principles*, Journal of Mathematical Logic 16 (2016), 1650002.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 4.2, 4.4, 4.5 and 5.11.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Section 2.2.
