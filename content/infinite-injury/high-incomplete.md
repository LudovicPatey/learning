---
title: A high incomplete c.e. degree
summary: Sacks' theorem that some c.e. degree is high but incomplete, by a tree construction in which the infinitary strategies enumerate infinitely many numbers; the columns of the set code which c.e. sets are infinite; further results on the c.e. degrees.
duration: 40
prerequisites: [trees-of-strategies, arithmetic-hierarchy/index-sets, turing-degrees/low-and-high]
---

A set $H$ is high if $H' \geq_T \emptyset''$. The course on oracles built a high set that does not compute $\emptyset'$, by a forcing construction whose conditions fix finitely many columns to their limit values (:ref{#thm-high-cone-avoidance}); that set is not c.e. Sacks proved in 1963 that there is a high **c.e.** set that is not complete. The strategies coding $\emptyset''$ into the jump of $H$ must enumerate infinitely many numbers into $H$ when they guess correctly that some $W_e$ is infinite, and the strategies keeping $H$ incomplete must survive these enumerations. In the minimal pair construction, the infinitary strategies enumerated nothing; here they act infinitely often, and the tree arranges that their actions avoid the computations protected below them.

:::theorem[Sacks]{#thm-high-incomplete}
There are c.e. sets $H$ and $C$ such that $H$ is high and $C \not\leq_T H$.
:::

:::corollary{#cor-high-incomplete-ce}
There is a c.e. degree $\mathbf h$ with $\mathbf h' = \mathbf 0''$ and $\obf < \mathbf h < \mathbf 0'$.
:::

:::proof{of=cor-high-incomplete-ce}
Let $H$ and $C$ be as in the theorem. Since $H$ is c.e., $H \leq_T \emptyset'$, so $H' \leq_T \emptyset''$, and $H' \equiv_T \emptyset''$. If $\emptyset' \leq_T H$, then $C \leq_T \emptyset' \leq_T H$, which is excluded. If $H$ were computable, $H'$ would be $\emptyset'$, and $\emptyset'' \leq_T \emptyset'$ would contradict :ref{#thm-jump}.
:::

## The requirements

Write $H^{[e]} = \{ y : \langle e, y \rangle \in H \}$ for the column $e$ of $H$. The requirements are
$$
\begin{gathered}
\mathcal G_e : H^{[e]} \text{ is cofinite if } W_e \text{ is infinite, and finite if } W_e \text{ is finite}; \\
\mathcal P_i : \Phi^H_i \neq C.
\end{gathered}
$$

:::lemma{#lem-hi-coding-suffices}
If every requirement $\mathcal G_e$ holds, then $H$ is high.
:::

:::proof{of=lem-hi-coding-suffices}
For every $e$, the sequence $y \mapsto H(\langle e, y \rangle)$ is eventually constant, equal to $1$ if $e \in \mathrm{Inf}$ and to $0$ otherwise. So $\mathrm{Inf}(e) = \lim_y H(\langle e, y \rangle)$, with an $H$-computable approximation, and $\mathrm{Inf} \leq_T H'$ by the limit lemma relativized to $H$ (:ref{#thm-limit-lemma}). Since $\mathrm{Inf}$ is $\Pi^0_2$-complete (:ref{#thm-fin-complete}), $\emptyset'' \equiv_T \mathrm{Inf} \leq_T H'$.
:::

The strategy for $\mathcal P_i$ is the Friedberg–Muchnik strategy: choose a fresh follower $x$, wait for $\Phi^H_i(x) = 0$ at some stage, enumerate $x$ into $C$ and restrain $H$ below the use. The strategy for $\mathcal G_e$, when $W_e$ grows, enumerates into $H$ all the numbers of the column $e$ below the current stage, except those restrained by strategies of higher priority. It has two outcomes, $\infty$ if $W_e$ grows infinitely often and $\mathrm f$ otherwise.

A $\mathcal P_i$-strategy below $\mathcal G_e$ with outcome $\infty$ cannot respect the column $e$: it would have to wait for $\mathcal G_e$ to stop, which never happens. The tree solves the conflict by timing. The $\mathcal P_i$-strategy guessing $\infty$ only acts at stages at which $\mathcal G_e$ has just filled its column up to the current stage $s$. The uses of the computations it protects are at most $s$, and from then on, $\mathcal G_e$ only enumerates numbers $\langle e, y \rangle$ with $y \geq s$, which are at least $s$.

## The construction

The tree $\mathbb T$ is the set of strings $\alpha \in \{ \infty, \mathrm f \}^{<\nat}$ with $\alpha(n) = \mathrm f$ for every odd $n$. A node of length $2e$ is a $\mathcal G_e$-node, and a node of length $2i + 1$ is a $\mathcal P_i$-node. The relations "to the left" and "higher priority" are those of :ref{#def-strategy-tree}.

- A $\mathcal G_e$-node $\alpha$ has a **record** $\rho_\alpha$, a number or undefined.
- A $\mathcal P_i$-node $\beta$ may have a follower $x_\beta$ and a mark **satisfied**, and has a **restraint** $r_\beta \in \nat$.
- **Initializing** a node makes its record undefined, or cancels its follower and its mark and sets its restraint to $0$.

Initially every node is initialized, and $H_0 = C_0 = \emptyset$. During a stage, the **current approximation** of $H$ is $H_s$ together with the numbers enumerated so far during the stage. For a $\mathcal G_e$-node $\alpha$, let $R_\alpha$ be the largest restraint $r_\gamma$ of a $\mathcal P$-node $\gamma$ of higher priority than $\alpha$; only finitely many nodes have a non-zero restraint at a given stage, so $R_\alpha$ is computable.

*Stage $s$.* Visit the nodes $\sigma_s \uh n$ for $n < s$ in order, where $\sigma_s \uh (n + 1) = (\sigma_s \uh n)^\frown o$ with $o$ the outcome of the node $\sigma_s \uh n$; so $\sigma_s$ has length $s$. Let $\alpha$ be the node visited.

1. If $\alpha$ is a $\mathcal G_e$-node with undefined record, set $\rho_\alpha = |W_{e,s}|$; the outcome is $\mathrm f$. If $\rho_\alpha$ is defined and $|W_{e,s}| > \rho_\alpha$, the stage is **$\alpha$-expansionary**: set $\rho_\alpha = |W_{e,s}|$, and enumerate into $H$ every number $\langle e, y \rangle$ with $y < s$, $\langle e, y \rangle \geq R_\alpha$, and $\langle e, y \rangle$ not yet in $H$; the outcome is $\infty$. Otherwise the outcome is $\mathrm f$.
2. If $\alpha$ is a $\mathcal P_i$-node without a follower, it receives a fresh follower. If it has a follower $x$, is not marked satisfied, and $\Phi^{\tilde H}_i(x)[s]\converge = 0$, where $\tilde H$ is the current approximation of $H$, then $\alpha$ **acts**: enumerate $x$ into $C$, set $r_\alpha = s$, and mark $\alpha$ satisfied. In all cases the outcome is $\mathrm f$.

At the end of the stage, initialize every node $\beta$ with $\sigma_s <_L \beta$.

The construction is computable, so $H$ and $C$ are c.e. Only $\mathcal G_e$-nodes enumerate into the column $e$ of $H$, and a follower enters $C$ only through the action of its own node. The node visited at stage $s$ after a $\mathcal P$-node that acts at stage $s$ already sees its restraint.

## Verification

The true path $P$ is defined as in :ref{#def-true-path}, and the proof of :ref{#lem-true-path} applies, with a simpler first case since no stage ends early.

:::lemma{#lem-hi-true-path}
For every $n$, the node $P \uh n$ is visited at infinitely many stages, and $\sigma_s <_L P \uh n$ holds for only finitely many $s$; so $P \uh n$ is initialized finitely often. A $\mathcal P$-node acts at most once between two initializations.
:::

:::lemma{#lem-hi-coding}
Every requirement $\mathcal G_e$ holds.
:::

:::proof{of=lem-hi-coding}
*$W_e$ finite.* Let $m = |W_e|$, and $s_0$ a stage with $|W_{e,s_0}| = m$. Records never exceed $m$. A $\mathcal G_e$-node is expansionary at a stage $s \geq s_0$ only when its record is less than $m$, and its record then becomes $m$. A record defined at a stage $s \geq s_0$ is equal to $m$. So after $s_0$, the only $\mathcal G_e$-nodes that can be expansionary are those visited before $s_0$ with a record defined before $s_0$ and kept since, and each of them is expansionary at most once after $s_0$. Finitely many nodes are visited before $s_0$, so there are finitely many expansionary stages of $\mathcal G_e$-nodes in total. Each of them enumerates finitely many numbers, and only these stages enumerate into the column $e$, which is therefore finite.

*$W_e$ infinite.* Let $\alpha = P \uh 2e$. By :ref{#lem-hi-true-path}, let $s_1$ be a stage after which $\alpha$ is never initialized and no stage satisfies $\sigma_s <_L \alpha$. After $s_1$, the record of $\alpha$ is defined at the first visit, and since $|W_{e,s}| \to \infty$ and $\alpha$ is visited infinitely often, there are infinitely many $\alpha$-expansionary stages.

We show that $R_\alpha$ is eventually constant. The $\mathcal P$-nodes of higher priority than $\alpha$ are its prefixes and the nodes to its left. A prefix $\gamma$ of $\alpha$ lies on the true path, so it is initialized finitely often and acts at most once between initializations; its restraint changes finitely often. A node $\gamma <_L \alpha$ is never visited after $s_1$, since it would give $\sigma_s <_L \alpha$; so after $s_1$ its restraint can only be reset to $0$ by an initialization. Only finitely many nodes have a non-zero restraint at stage $s_1$. Hence $R_\alpha$ changes finitely often, and is equal to some $R$ from a stage $s_2$ on.

Let $y$ be such that $\langle e, y \rangle \geq R$. At an $\alpha$-expansionary stage $s > \max(s_2, y)$, the number $\langle e, y \rangle$ is enumerated into $H$ if it is not already there. The numbers $\langle e, y \rangle < R$ are finitely many, so $H^{[e]}$ is cofinite.
:::

:::lemma{#lem-hi-preservation}
Suppose that a $\mathcal P_i$-node $\beta$ acts at stage $s_0$, through a computation $\Phi^{\tilde H}_i(x)[s_0]\converge = 0$, and is never initialized afterwards. Then no number less than $s_0$ enters $H$ after the action of $\beta$. Consequently $\Phi^H_i(x) = 0$.
:::

:::proof{of=lem-hi-preservation}
Let a $\mathcal G_e$-node $\alpha$ enumerate a number $z = \langle e, y \rangle$ into $H$ at an $\alpha$-expansionary stage $t \geq s_0$, after the action of $\beta$. We show that $z \geq s_0$. Throughout, $r_\beta = s_0$, since $\beta$ is not initialized.

1. *$\alpha$ has lower priority than $\beta$.* Then $R_\alpha \geq r_\beta = s_0$ at stage $t$, and $z \geq R_\alpha$.
2. *$\alpha <_L \beta$.* Then $\alpha$ is visited at $t$, so $\sigma_t <_L \beta$ and $\beta$ is initialized at the end of stage $t$: excluded.
3. *$\alpha^\frown \mathrm f \preceq \beta$.* Since $t$ is $\alpha$-expansionary, $\alpha^\frown \infty \preceq \sigma_t$, so again $\sigma_t <_L \beta$: excluded.
4. *$\alpha^\frown \infty \preceq \beta$.* Since $\beta$ is visited at $s_0$, so is $\alpha$, with outcome $\infty$: the stage $s_0$ is $\alpha$-expansionary, and $\alpha$ acted before $\beta$, so that $t > s_0$. If $y \geq s_0$, then $z \geq y \geq s_0$. Suppose $y < s_0$. At stage $s_0$, $\alpha$ did not enumerate $z$, and $z$ was not in $H$, so $z < R_\alpha$ at stage $s_0$: some $\mathcal P$-node $\gamma$ of higher priority than $\alpha$ had $z < r_\gamma$. At stage $t$, $z \geq R_\alpha$, so the restraint of $\gamma$ has decreased. A restraint only decreases by initialization, so $\gamma$ was initialized at the end of a stage $v$ with $s_0 \leq v < t$, and $\sigma_v <_L \gamma$. If $\gamma \prec \alpha$, then $\gamma \prec \beta$; if $\gamma <_L \alpha$, then $\gamma <_L \beta$. In both cases $\sigma_v <_L \beta$, and $\beta$ is initialized at the end of stage $v$: excluded.

So no number less than $s_0$ enters $H$ after the action. The computation $\Phi^{\tilde H}_i(x)[s_0]$ has use at most $s_0$, and $H \uh s_0 = \tilde H \uh s_0$, so $\Phi^H_i(x) = 0$ by the use principle.
:::

Case 4 is where the tree matters. A $\mathcal G_e$-node with outcome $\infty$ on the true path enumerates infinitely many numbers, and injures infinitely often every node to its right; but at the stages at which the nodes below its outcome $\infty$ act, it has just filled its column up to the current stage, and it never comes back below. The only way it could come back is the release of a restraint of higher priority, which also initializes $\beta$.

:::lemma{#lem-hi-diagonal}
Every requirement $\mathcal P_i$ is met.
:::

:::proof{of=lem-hi-diagonal}
Let $\beta = P \uh (2i + 1)$. By :ref{#lem-hi-true-path}, $\beta$ is initialized finitely often and visited infinitely often; after its last initialization, it receives a follower $x$ and keeps it. If $\beta$ acts, then $x \in C$ and $\Phi^H_i(x) = 0$ by :ref{#lem-hi-preservation}. If $\beta$ never acts, then $x \notin C$. Suppose that $\Phi^H_i(x) = 0$, with use $u$. At every large stage $s$, the computation has converged, $s \geq u$, and the current approximation of $H$ agrees with $H$ below $u$, so $\Phi^{\tilde H}_i(x)[s]\converge = 0$ at every large $\beta$-stage, and $\beta$ acts: a contradiction. So $\Phi^H_i(x) \neq 0 = C(x)$. In both cases $\Phi^H_i \neq C$.
:::

:::proof{of=thm-high-incomplete}
By :ref{#lem-hi-coding} and :ref{#lem-hi-coding-suffices}, $H$ is high. By :ref{#lem-hi-diagonal}, $C \not\leq_T H$.
:::

:::quiz[the high incomplete construction]
In case 4 of the proof of :ref{#lem-hi-preservation}, why does $\alpha$ not enumerate the number $\langle e, y \rangle$ with $y < s_0$ at a later stage?

- [x] Because at stage $s_0$, just before $\beta$ acted, $\alpha$ enumerated every number of its column below $s_0$ that was not restrained; a number left out then can only enter after the release of a restraint of higher priority, which initializes $\beta$.
- [ ] Because $\alpha$ respects the restraint of $\beta$.

  $\alpha$ has higher priority than $\beta$, and does not respect its restraint.
- [ ] Because $\alpha$ has finitely many expansionary stages.

  In this case, $\alpha$ may have infinitely many expansionary stages: this is the infinite injury situation.

---

Why is the first visit of a $\mathcal G_e$-node after an initialization not expansionary, unlike the first visit of an $\mathcal N$-node in the minimal pair construction?

- [x] Because a $\mathcal G_e$-node may be initialized and visited again infinitely often; if each such first visit were expansionary, it could enumerate numbers into the column $e$ at infinitely many stages, and make the column infinite even when $W_e$ is finite. With records, a node whose record is set after $W_e$ has stopped growing is never expansionary.
- [ ] To make the construction computable.

  Both versions are computable.
- [ ] So that the column $e$ is cofinite when $W_e$ is infinite.

  Cofiniteness only uses the node on the true path, which has infinitely many expansionary stages in both versions.

---

In :ref{#lem-hi-diagonal}, why is the true path used, rather than an arbitrary $\mathcal P_i$-node?

- [x] Because a node on the true path is initialized finitely often and visited infinitely often, so it keeps a follower and gets to act if the computation converges to $0$.
- [ ] Because only nodes on the true path act.

  Nodes to the right of the true path may act infinitely often.
- [ ] Because the true path is computable.

  The true path computes $\emptyset''$.
:::

## Further results

The c.e. degrees have been studied intensively with these methods and their elaborations. We state some of the main results without proof; see Soare's book for all of them.

- **Density** (Sacks, 1964). Between any two c.e. degrees $\abf < \bbf$ there is a c.e. degree $\cbf$ with $\abf < \cbf < \bbf$. The proof combines the Sacks preservation strategy with coding, in an infinite injury argument.
- **No diamond with top $\mathbf 0'$** (Lachlan, 1966). There are no c.e. degrees $\abf$ and $\bbf$ forming a minimal pair with $\abf \vee \bbf = \mathbf 0'$.
- **Cappable degrees** (Ambos-Spies, Jockusch, Shore, Soare, 1984). A non-zero c.e. degree is **cappable** if it belongs to a minimal pair of c.e. degrees. A co-infinite c.e. set $A$ is **promptly simple** if there are a c.e. approximation $(A_s)$ and a computable function $p$ such that, for every $e$ with $W_e$ infinite, some $x$ enters $W_e$ at a stage $s$ and belongs to $A_{p(s)}$. A non-zero c.e. degree is non-cappable if and only if it contains a promptly simple set. The non-cappable degrees form a filter of the c.e. degrees, and the cappable degrees, together with $\obf$, form an ideal.

## Exercises

::::exercise{difficulty=1}
Show that the outcome of the $\mathcal G_e$-node on the true path is $\infty$ if and only if $W_e$ is infinite, and deduce that the true path is Turing equivalent to $\emptyset''$.

:::solution
Let $\alpha = P \uh 2e$. After its last initialization, $\alpha$ keeps its record. If $W_e$ is infinite, there are infinitely many $\alpha$-expansionary stages (proof of :ref{#lem-hi-coding}), and $P(2e) = \infty$. If $W_e$ is finite, the record eventually equals $|W_e|$ and $\alpha$ is no longer expansionary, so $\alpha^\frown \infty$ is visited finitely often and $P(2e) = \mathrm f$. Hence $\mathrm{Inf}(e) = 1$ if and only if $P(2e) = \infty$, and $\emptyset'' \equiv_T \mathrm{Inf} \leq_T P$. As in the previous lesson, $P \leq_T \emptyset''$.
:::
::::

::::exercise{difficulty=2}
Consider the finite injury version of the construction: one strategy per requirement, ordered $\mathcal G_0, \mathcal P_0, \mathcal G_1, \mathcal P_1, \dots$, in which the strategy for $\mathcal G_e$ fills its column below the current stage whenever $W_e$ grows, respecting the restraints of the strategies of higher priority, and a strategy for $\mathcal P_i$ acts at any stage and is initialized whenever a strategy of higher priority enumerates a number below its restraint. Show that the strategy for $\mathcal P_0$ may be injured infinitely often, and identify the case of :ref{#lem-hi-preservation} that has no counterpart.

:::solution
Suppose that $\Phi^X_0(x)$ converges to $0$ for every oracle $X$ and every $x$, after querying $X$ at $\langle 0, y \rangle$ for every $y < x$, and that $W_0$ is infinite and grows only at stages $t_0 < t_1 < \cdots$ that are far apart. After $t_k$, the strategy for $\mathcal P_0$ has a follower $x > t_k$, since followers are fresh after its last initialization, which happened at or before $t_k$. If $t_{k+1}$ is large enough, the computation $\Phi^H_0(x)$ converges at some stage $s$ with $t_k < s < t_{k+1}$, and $\mathcal P_0$ acts, with a restraint larger than $\langle 0, t_k \rangle$, a number queried by the computation. This number is not in $H$, since $\mathcal G_0$ last filled its column below $t_k$. At stage $t_{k+1}$, $\mathcal G_0$, which has higher priority, enumerates $\langle 0, t_k \rangle$ and injures $\mathcal P_0$. This repeats for every $k$.

Case 4 of :ref{#lem-hi-preservation} fails. On the tree, the node below the outcome $\infty$ of $\alpha$ only acts at $\alpha$-expansionary stages, just after $\alpha$ has filled its column below the current stage; here $\mathcal P_0$ acts between two growths of $W_0$, while the numbers $\langle 0, y \rangle$ with $t_k \leq y < s$ are still missing from $H$.
:::
::::

## Notes and references

Sacks (1963) proved that every degree c.e. in and above $\mathbf 0'$ is the jump of a c.e. degree, by an infinite injury argument; high incomplete c.e. degrees are the case of $\mathbf 0''$. The construction of this lesson is a tree version of the classical proof, in which the columns of $H$ code $\mathrm{Inf}$; Soare's book gives another proof through the thickness lemma, and observes that the result can also be obtained by two successive finite injury arguments. The characterization of the cappable degrees is due to Ambos-Spies, Jockusch, Shore and Soare (1984).

- G. E. Sacks, *Recursive enumerability and the jump operator*, Transactions of the American Mathematical Society 108 (1963), 223–239.
- G. E. Sacks, *The recursively enumerable degrees are dense*, Annals of Mathematics 80 (1964), 300–312.
- K. Ambos-Spies, C. G. Jockusch, R. A. Shore and R. I. Soare, *An algebraic decomposition of the recursively enumerable degrees and the coincidence of several degree classes with the promptly simple degrees*, Transactions of the American Mathematical Society 281 (1984), 109–128.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapters VIII–XIII.
- S. Lempp, *Priority arguments in computability theory, model theory, and complexity theory*, lecture notes, University of Wisconsin, 2012.
