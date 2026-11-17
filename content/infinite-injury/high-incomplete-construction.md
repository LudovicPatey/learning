---
title: The high incomplete construction
summary: The tree construction of a high incomplete c.e. set, in which the coding strategies with infinite outcome enumerate infinitely many numbers and the strategies below them act only after the column has been filled; the true path; the coding requirements hold.
duration: 20
prerequisites: [high-incomplete]
---

The previous lesson reduced Sacks' theorem to the requirements $\mathcal G_e$, which make the columns of $H$ code which c.e. sets are infinite, and $\mathcal P_i$, which keep $C$ out of the degree of $H$. It showed that the coding strategies, which enumerate infinitely many numbers when $W_e$ is infinite, can injure a diagonalization strategy of lower priority infinitely often. This lesson gives the solution, a construction on a tree in which the diagonalization strategies guessing that $W_e$ is infinite act only at the right moments, and verifies the coding requirements. The technique is the one of the minimal pair theorem, a tree of strategies with an infinitary outcome, with one new feature: the infinitary strategies now enumerate numbers.

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

The construction follows the tree method of the minimal pair theorem; for the sources and the comparison with the two-step proof of Downey and Hirschfeldt, see the notes of the previous lesson.

- G. E. Sacks, *Recursive enumerability and the jump operator*, Transactions of the American Mathematical Society 108 (1963), 223–239.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.14.3.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter VIII.

:::::exercises
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
:::::
