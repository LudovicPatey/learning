---
title: A high incomplete c.e. degree
summary: Sacks' theorem that some c.e. degree is high but incomplete; the columns of the set code which c.e. sets are infinite; a finite injury construction fails; the tree construction, in which the infinitary strategies enumerate infinitely many numbers, and the coding requirements.
duration: 55
prerequisites: [minimal-pair-verification, arithmetic-hierarchy/index-sets, turing-degrees/low-and-high]
---

A set $H$ is high if $H' \geq_T \emptyset''$. The course on oracles built a high set that does not compute $\emptyset'$, by a forcing construction whose conditions fix finitely many columns to their limit values (:ref{#thm-high-cone-avoidance}); that set is not c.e. Sacks proved in 1963 that there is a high **c.e.** set that is not complete. The strategies coding $\emptyset''$ into the jump of $H$ must enumerate infinitely many numbers into $H$ when they guess correctly that some $W_e$ is infinite, and the strategies keeping $H$ incomplete must survive these enumerations. In the minimal pair construction, the infinitary strategies enumerated nothing; here they act infinitely often, and the tree arranges that their actions avoid the computations protected below them.

This lesson states the theorem, explains why a finite injury construction cannot prove it, gives the construction on a tree, and verifies the coding requirements. The next lesson verifies the diagonalization requirements.

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

## The obstruction to a finite injury argument

When $W_e$ is infinite, the strategy for $\mathcal G_e$ acts at infinitely many stages, and may enumerate numbers below the restraint of a strategy for $\mathcal P_i$ of lower priority, which a finite injury argument would then initialize. The following proposition shows that this can happen infinitely often.

Consider the **finite injury version** of the construction. There is one strategy per requirement, with the priority order $\mathcal G_0, \mathcal P_0, \mathcal G_1, \mathcal P_1, \dots$, and at each stage $s \geq 1$ the strategies are run in this order, with the current approximation $\tilde H$ of $H$ defined as in the construction below. We only describe the first two strategies, with a c.e. set $V$, given by a computable enumeration $(V_s)$ with $V_0 = \emptyset$, in place of $W_0$, and a Turing functional $\Psi$ in place of $\Phi_0$.

- *$\mathcal G_0$:* if $|V_s| > |V_{s-1}|$, enumerate into $H$ every number $\langle 0, y \rangle$ with $y < s$ that is not yet in $H$.
- *$\mathcal P_0$:* if it has no follower, it receives a fresh follower. If it has a follower $x$, is not marked satisfied, and $\Psi^{\tilde H}(x)[s]\converge = 0$, it enumerates $x$ into $C$, sets its restraint to $s$, and is marked satisfied. It is **initialized**, losing its follower, its mark and its restraint, whenever $\mathcal G_0$ enumerates a number less than its restraint.

The verification of a finite injury argument uses nothing about $W_0$ and $\Phi_0$ beyond the facts that they are a c.e. set and a Turing functional, so it would apply to $V$ and $\Psi$ as well.

:::proposition{#prop-hi-finite-injury}
There are a c.e. set $V$ with a computable enumeration $(V_s)$, and a Turing functional $\Psi$ such that $\Psi^X$ is total for every oracle $X$, for which, in the finite injury version, $V$ is infinite and the strategy for $\mathcal P_0$ is initialized at infinitely many stages.
:::

:::proof{of=prop-hi-finite-injury}
Let $\Psi^X(x)$ query $X(\langle 0, y \rangle)$ for $y = 0, 1, \dots, x$, then output $0$. The steps of this computation do not depend on the answers of the oracle, so there is a least $n_x$ such that, for every oracle $X$, $\Psi^X(x)[s]$ converges, to $0$, if and only if $s \geq n_x$; the use is $\langle 0, x \rangle + 1$. Define $V$ together with the construction: $V_0 = \emptyset$, and $V_{s+1} = V_s \cup \{ s \}$ if $\mathcal P_0$ acts at stage $s$, $V_{s+1} = V_s$ otherwise. Stage $s + 1$ only uses $V_{s+1}$, which is known at the end of stage $s$, so the whole process is computable and $V$ is c.e.; since the construction is deterministic, running it with the enumeration $(V_s)$ given in advance produces the same stages.

Only $\mathcal G_0$ enumerates numbers of the column $0$ into $H$, and it respects no restraint, since it has the highest priority. We show the following, for a stage $g \geq 1$: if $\mathcal P_0$ receives a follower $x$ at stage $g$, and the column $0$ of $H$ at the end of stage $g$ contains only numbers $\langle 0, y \rangle$ with $y < g$, then $\mathcal P_0$ acts at some stage $s > g$, is initialized at stage $s + 1$, receives a new follower at stage $s + 1$, and the hypothesis holds again for $s + 1$ in place of $g$.

Since the follower is fresh, $x > g$. The set $V$ only grows at the stage after an action of $\mathcal P_0$, and $\mathcal P_0$ does not act at stage $g$. As long as $\mathcal P_0$ has not acted, $V$ does not grow, so $\mathcal G_0$ enumerates nothing and $\mathcal P_0$ keeps $x$. At stage $s = \max(g + 1, n_x)$, the computation $\Psi^{\tilde H}(x)[s]$ converges to $0$ for the first time after stage $g$, and $\mathcal P_0$ acts, with restraint $s$. The use of the computation is at most $s$, so $\langle 0, x \rangle < s$, and since $g < x$, also $\langle 0, g \rangle < s$. At the end of stage $s$, the column $0$ of $H$ still contains only numbers $\langle 0, y \rangle$ with $y < g$, so $\langle 0, g \rangle \notin H_{s+1}$. At stage $s + 1$, $V$ grows, and $\mathcal G_0$ enumerates every $\langle 0, y \rangle$ with $y < s + 1$, among them $\langle 0, g \rangle < s$: the strategy for $\mathcal P_0$ is initialized, then receives a fresh follower at stage $s + 1$, and the column $0$ of $H$ consists of the numbers $\langle 0, y \rangle$ with $y < s + 1$.

At stage $1$, $\mathcal P_0$ receives its first follower and the column $0$ of $H$ is empty, so the hypothesis holds for $g = 1$. By induction, $\mathcal P_0$ acts and is initialized infinitely often, and $V$ is infinite.
:::

The requirement $\mathcal P_0$ itself is met in this run, since the followers enter $C$ while $\Psi^H$ is the constant function $0$. What fails is the finite injury lemma: the strategy is never left undisturbed, and each initialization destroys the computation on which it acted, since that computation queried $\langle 0, g \rangle$ while this number was out of $H$. A verification by induction along the priority order, as in the Friedberg–Muchnik theorem, is impossible.

## The tree solution

A $\mathcal P_i$-strategy below $\mathcal G_e$ with outcome $\infty$ cannot respect the column $e$: it would have to wait for $\mathcal G_e$ to stop, which never happens. In the proof of :ref{#prop-hi-finite-injury}, $\mathcal P_0$ acts between two growths of $V$, while the numbers $\langle 0, y \rangle$ with $g \leq y < s$ are still missing from $H$. The tree solves the conflict by timing. The $\mathcal P_i$-strategy guessing $\infty$ only acts at stages at which $\mathcal G_e$ has just filled its column up to the current stage $s$. The uses of the computations it protects are at most $s$, and from then on, $\mathcal G_e$ only enumerates numbers $\langle e, y \rangle$ with $y \geq s$, which are at least $s$.

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

## The true path and the coding requirements

The true path $P$ is defined as in :ref{#def-true-path}, and the proof of :ref{#lem-true-path} applies, with a simpler first case since no stage ends early (:ref{#ex-hi-true-path}).

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

:::quiz[the coding requirements]
Why is the first visit of a $\mathcal G_e$-node after an initialization not expansionary, unlike the first visit of an $\mathcal N$-node in the minimal pair construction?

- [x] Because a $\mathcal G_e$-node may be initialized and visited again infinitely often; if each such first visit were expansionary, it could enumerate numbers into the column $e$ at infinitely many stages, and make the column infinite even when $W_e$ is finite. With records, a node whose record is set after $W_e$ has stopped growing is never expansionary.
- [ ] To make the construction computable.

  Both versions are computable.
- [ ] So that the column $e$ is cofinite when $W_e$ is infinite.

  Cofiniteness only uses the node on the true path, which has infinitely many expansionary stages in both versions.
:::

::::exercise{#ex-hi-true-path difficulty=1 objective="Adapt the proof of the properties of the true path to the high incomplete construction."}
Prove :ref{#lem-hi-true-path}, following the proof of :ref{#lem-true-path}. Where is it used that no stage ends early?

:::solution
A $\mathcal P$-node is marked satisfied when it acts, and only an initialization removes the mark, so it acts at most once between two initializations. The rest is the induction of :ref{#lem-true-path}, in which $\mathcal G$-nodes are treated as the $\mathcal N$-nodes of case 2, with the same proof. The only change is in case 1. In the minimal pair construction, an $\mathcal R$-node that acts ends the stage, so the proof first needs a stage after which the node no longer acts. Here the stage continues after an action, and the current path has length $s$, so at every $\alpha$-stage $s > n + 1$ of a $\mathcal P$-node $\alpha = P \uh n$, the node $\alpha^\frown \mathrm f$ is visited, whether or not $\alpha$ acts. Hence $P(n) = \mathrm f$, and a current path to the left of $\alpha^\frown \mathrm f$ is to the left of $\alpha$.
:::
::::

## Notes and references

Sacks (1963) proved that every degree c.e. in and above $\mathbf 0'$ is the jump of a c.e. degree, by an infinite injury argument; high incomplete c.e. degrees are the case of $\mathbf 0''$. Downey and Hirschfeldt (§2.14.3) prove the existence of a high incomplete c.e. degree in two steps: a c.e. set whose columns are either finite or full according to whether $\Phi_e$ is total, and a c.e. thick subset of it that avoids the cone above a given non-computable c.e. set (a weak form of Shoenfield's thickness lemma), proved on a tree with the same tree and outcomes as here. The construction of this lesson merges the two steps: the columns of $H$ code $\mathrm{Inf}$ directly. The finite injury version of :ref{#prop-hi-finite-injury} is the obstacle described informally by Downey and Hirschfeldt and by Nies.

- G. E. Sacks, *Recursive enumerability and the jump operator*, Transactions of the American Mathematical Society 108 (1963), 223–239.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.14.3 and §2.16.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter VIII (the thickness lemma is Theorem VIII.1.1, Sacks' jump theorem is Theorem VIII.3.1).

:::::exercises
::::exercise{#ex-hi-coding-forms difficulty=1 objective="See why the coding requirements ask for finite or cofinite columns, rather than empty or full ones, or merely infinite ones."}
1. Show that there is no c.e. set $H$ such that $H^{[e]} = \nat$ for every $e \in \mathrm{Inf}$ and $H^{[e]} = \emptyset$ for every $e \notin \mathrm{Inf}$.
2. Let $H = \{ \langle e, y \rangle : y \in W_e \}$. Show that $H$ is c.e., that $H^{[e]}$ is infinite if and only if $W_e$ is infinite, and that $\emptyset' \leq_T H$.

Explain what these two facts say about the form of the requirements $\mathcal G_e$.

:::solution
1. If $H$ were such a set, then $e \in \mathrm{Inf}$ if and only if $\langle e, 0 \rangle \in H$, so $\mathrm{Inf} \leq_T H$. Since $H$ is c.e., $H \leq_T \emptyset'$, and since $\mathrm{Inf}$ is $\Pi^0_2$-complete (:ref{#thm-fin-complete}), $\emptyset'' \leq_T \mathrm{Inf} \leq_T \emptyset'$, contradicting :ref{#thm-jump}.
2. $\langle e, y \rangle \in H$ if and only if $\exists s\ y \in W_{e,s}$, so $H$ is c.e. Its column $e$ is $W_e$. Finally $e \in \emptyset'$ if and only if $e \in W_e$, if and only if $\langle e, e \rangle \in H$, so $\emptyset' \leq_m H$.

The requirement that $H^{[e]}$ be full or empty according to $\mathrm{Inf}$ is too strong: it would make $\mathrm{Inf}$ computable in $H$, which no c.e. set allows. The requirement that $H^{[e]}$ be infinite exactly when $W_e$ is infinite is too weak: it is met by a complete set, and it only makes $\mathrm{Inf}$ a $\Pi^0_2(H)$ set, which gives $\mathrm{Inf} \leq_T H''$ and nothing about $H'$. The requirements $\mathcal G_e$ lie in between: $\mathrm{Inf}(e)$ is the limit of the column $e$, which places $\mathrm{Inf}$ below $H'$ by the limit lemma (:ref{#lem-hi-coding-suffices}), and :ref{#thm-high-incomplete} shows that they can be met by an incomplete c.e. set.
:::
::::

::::exercise{#ex-hi-restraints-finite difficulty=1 objective="Check that the bound $R_\alpha$ used by the coding nodes is computable."}
Show that, at each stage $s$ of the construction, only nodes of length less than $s$ have a non-zero restraint. Deduce that the value of $R_\alpha$ at any moment of stage $s$ is computable from $\alpha$, $s$ and that moment.

:::solution
A restraint is set to a non-zero value only when a $\mathcal P$-node acts, at a stage $t \geq 1$ at which it is visited, and is reset to $0$ by initialization. A node visited at stage $t$ is $\sigma_t \uh n$ for some $n < t$, so it has length less than $t$. Hence, during stage $s$, the nodes with a non-zero restraint have length less than $s$, and there are finitely many of them.

The construction up to a given moment of stage $s$ is a finite computation, which yields the current restraints of the finitely many nodes of length less than $s$. Whether such a node $\gamma$ has higher priority than $\alpha$ is decidable: check whether $\gamma \prec \alpha$ or $\gamma <_L \alpha$. So $R_\alpha$ is the maximum of a finite, computable list of numbers, or $0$ if the list is empty.
:::
::::

::::exercise{#ex-hi-tot-coding difficulty=2 objective="Adapt the coding requirements to the $\Pi^0_2$-complete set $\mathrm{Tot}$, and identify the properties of the coded approximation that the verification uses." lessons="arithmetic-hierarchy/index-sets"}
Let $c(e, s)$ be the largest $n \leq s$ such that $\Phi_e(y)[s]$ converges for every $y < n$. Modify the construction by replacing $|W_{e,s}|$ by $c(e, s)$ in the treatment of $\mathcal G_e$-nodes. Show that the column $e$ of the resulting set $H$ is cofinite if $\Phi_e$ is total and finite otherwise, and that $H$ is high. Which properties of the function $s \mapsto |W_{e,s}|$ does the proof of :ref{#lem-hi-coding} use?

:::solution
The proof of :ref{#lem-hi-coding} uses only three properties of $q(s) = |W_{e,s}|$: $q$ is computable, so that the construction is computable; $q$ is non-decreasing, and if it is bounded it is eventually constant, equal to its maximum $m$, from a stage $s_0$ on; if it is unbounded, it tends to infinity. In the finite case the proof uses that records never exceed $m$ and that a record defined at a stage $s \geq s_0$ equals $m$; in the infinite case, that $q(s) > \rho_\alpha$ at some later stage, whatever the record $\rho_\alpha$.

The function $s \mapsto c(e, s)$ is computable. It is non-decreasing, since a computation converging at stage $s$ also converges at stage $s + 1$, and the bound $n \leq s$ increases with $s$. If $\Phi_e$ is total, then for every $n$, all the computations $\Phi_e(y)$, $y < n$, converge by some stage $s_n$, and $c(e, s) \geq n$ for every $s \geq \max(s_n, n)$, so $c(e, s) \to \infty$. If $\Phi_e(y)$ diverges, then $c(e, s) \leq y$ for every $s$, so $c(e, s)$ is bounded and, being non-decreasing, eventually constant. The proof of :ref{#lem-hi-coding} therefore applies word for word, with "$\Phi_e$ total" in place of "$W_e$ infinite": $H^{[e]}$ is cofinite if $e \in \mathrm{Tot}$ and finite otherwise. The other parts of the verification, :ref{#lem-hi-true-path} and the diagonalization requirements, do not depend on what the coding nodes measure.

As in :ref{#lem-hi-coding-suffices}, $\mathrm{Tot}(e) = \lim_y H(\langle e, y \rangle)$, so $\mathrm{Tot} \leq_T H'$ by the relativized limit lemma (:ref{#thm-limit-lemma}). Since $\mathrm{Tot}$ is $\Pi^0_2$-complete (:ref{#thm-tot-complete}), $\emptyset'' \leq_T H'$.
:::
::::

::::exercise{#ex-hi-v-every-stage difficulty=2 objective="See on the finite injury version why the timing of the coding strategy is what protects the diagonalization strategy."}
In the finite injury version described before :ref{#prop-hi-finite-injury}, let $V = \nat$, with the enumeration $V_s = \{ 0, \dots, s - 1 \}$, and let $\Psi$ be any Turing functional. Show that the strategy for $\mathcal P_0$ is never initialized. Compare with the run of the proof of :ref{#prop-hi-finite-injury}.

:::solution
Since $|V_s| = s > |V_{s-1}|$, the strategy for $\mathcal G_0$ acts at every stage $s \geq 1$. By induction on $s \geq 1$, at the end of the action of $\mathcal G_0$ at stage $s$, the column $0$ of $H$ is $\{ \langle 0, y \rangle : y < s \}$: at stage $1$ it enumerates $\langle 0, 0 \rangle$, and at a stage $s \geq 2$ it finds the numbers $\langle 0, y \rangle$ with $y < s - 1$ already in $H$, and enumerates only $\langle 0, s - 1 \rangle$. No other strategy enumerates numbers of the column $0$.

The strategy for $\mathcal P_0$ is initialized only when $\mathcal G_0$ enumerates a number less than its restraint. Before $\mathcal P_0$ acts, its restraint is $0$, and no number is less than $0$. Suppose that it acts at stage $s_1$, with restraint $s_1$; this happens after the action of $\mathcal G_0$ at stage $s_1$. At every later stage $t > s_1$, $\mathcal G_0$ enumerates only $\langle 0, t - 1 \rangle \geq t - 1 \geq s_1$, which is not less than the restraint. So $\mathcal P_0$ is never initialized, and it acts at most once.

In the proof of :ref{#prop-hi-finite-injury}, $V$ grows only at the stage after an action of $\mathcal P_0$, so $\mathcal P_0$ always acts while the numbers $\langle 0, y \rangle$ with $g \leq y < s$ are missing from $H$, and the next growth of $V$ enumerates them below the restraint. Here, $\mathcal G_0$ fills its column up to the current stage at every stage, before $\mathcal P_0$ acts, and later enumerates only numbers at least as large as the stage. This is the timing that the tree imposes on the nodes below the outcome $\infty$ of a coding node: they act only at stages at which the coding node has just filled its column.
:::
::::
:::::
