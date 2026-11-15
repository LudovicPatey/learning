---
title: Verification of the high incomplete construction
summary: The diagonalization requirements of the high incomplete construction; a coding node with infinite outcome never enumerates a number below the restraint of a node acting below that outcome; end of the proof of Sacks' theorem; further results on the c.e. degrees.
duration: 35
prerequisites: [high-incomplete, minimal-pair-verification]
---

The previous lesson built the c.e. sets $H$ and $C$ on a tree of strategies and showed that $H$ is high. It remains to show that $C \not\leq_T H$: for every $i$, the $\mathcal P_i$-node $\beta$ on the true path meets $\mathcal P_i$. Once $\beta$ has acted at a stage $s_0$, it suffices that no number below $s_0$ enters $H$ afterwards. As in the verification of the minimal pair theorem (:ref{#lem-mp-one-side}), this is proved by a case analysis on the position, relative to $\beta$, of a node that could enumerate such a number.

The new case is a $\mathcal G_e$-node $\alpha$ with $\alpha^\frown \infty \preceq \beta$. Such a node, if it is on the true path, enumerates infinitely many numbers into $H$ after $\beta$ has acted, and $\beta$ cannot restrain it, since $\alpha$ has higher priority. But $\beta$ is only visited at $\alpha$-expansionary stages, after $\alpha$ has filled its column up to the current stage, and the later numbers of the column are large. The figure shows the column at the stage at which $\beta$ acts.

:::figure[The column $1$ of $H$ on the number line, just after the visit of a $\mathcal G_1$-node $\alpha$ at an $\alpha$-expansionary stage $s_0 = 10$, at which a $\mathcal P$-node $\beta$ below $\alpha^\frown \infty$ then acts. The numbers $\langle 1, y \rangle$ with $y < 10$ that are at least the bound $R_\alpha = 3$ are in $H$; the number $\langle 1, 0 \rangle = 1$ is kept out by a restraint of higher priority. Later visits of $\alpha$ only enumerate numbers $\langle 1, y \rangle$ with $y \geq 10$, which are at least $s_0$, and the number $1$, which can only enter after the release of that restraint, an event that also initializes $\beta$.]
<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="The numbers of column 1 on the number line; at stage s_0 all of them with second coordinate below s_0 are in H except those below the restraint R; the restraint of beta is s_0"><rect x="40" y="64" width="170" height="52" class="soft-fill"/><line x1="40" y1="90" x2="560" y2="90" class="axis"/><line x1="40" y1="86" x2="40" y2="94" class="axis"/><text x="40" y="112" text-anchor="middle" class="mrm muted" font-size="12">0</text><line x1="125" y1="86" x2="125" y2="94" class="axis"/><text x="125" y="112" text-anchor="middle" class="mrm muted" font-size="12">5</text><line x1="210" y1="86" x2="210" y2="94" class="axis"/><text x="210" y="112" text-anchor="middle" class="mrm muted" font-size="12">10</text><line x1="295" y1="86" x2="295" y2="94" class="axis"/><text x="295" y="112" text-anchor="middle" class="mrm muted" font-size="12">15</text><line x1="380" y1="86" x2="380" y2="94" class="axis"/><text x="380" y="112" text-anchor="middle" class="mrm muted" font-size="12">20</text><line x1="465" y1="86" x2="465" y2="94" class="axis"/><text x="465" y="112" text-anchor="middle" class="mrm muted" font-size="12">25</text><line x1="550" y1="86" x2="550" y2="94" class="axis"/><text x="550" y="112" text-anchor="middle" class="mrm muted" font-size="12">30</text><line x1="91" y1="62" x2="91" y2="118" class="ink-stroke" stroke-width="1.4" stroke-dasharray="3 3"/><line x1="210" y1="62" x2="210" y2="118" class="ink-stroke" stroke-width="1.4" stroke-dasharray="3 3"/><text x="91" y="56" text-anchor="middle" class="math" font-size="15">R<tspan class="mrm" font-size="10" dy="4">α</tspan></text><text x="210" y="56" text-anchor="middle" class="math" font-size="15">s<tspan class="mrm" font-size="10" dy="4">0</tspan><tspan class="mrm" font-size="15" dy="-4">&#160;=&#160;</tspan>r<tspan class="mrm" font-size="10" dy="4">β</tspan></text><circle cx="57" cy="90" r="6" class="node"/><circle cx="108" cy="90" r="6" class="accent-fill"/><circle cx="176" cy="90" r="6" class="accent-fill"/><circle cx="261" cy="90" r="6" class="accent-fill"/><circle cx="363" cy="90" r="6" class="accent-fill"/><circle cx="482" cy="90" r="6" class="accent-fill"/><circle cx="46" cy="150" r="6" class="accent-fill"/><text x="58" y="154" class="label">in H after the visit of α at stage <tspan class="math">s</tspan><tspan font-size="9" dy="3">0</tspan></text><circle cx="286" cy="150" r="6" class="node"/><text x="298" y="154" class="label">kept out by a restraint of higher priority</text><rect x="40" y="166" width="12" height="12" class="soft-fill"/><text x="58" y="176" class="label">protected by β: contains the use of its computation</text></svg>
:::

## Preservation

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

Case 4 is where the tree matters. A $\mathcal G_e$-node with outcome $\infty$ on the true path enumerates infinitely many numbers, and injures infinitely often every node to its right; but at the stages at which the nodes below its outcome $\infty$ act, it has just filled its column up to the current stage, and it never comes back below. The only way it could come back is the release of a restraint of higher priority, which also initializes $\beta$. This is the case that has no counterpart in the finite injury version: in the proof of :ref{#prop-hi-finite-injury}, the strategy for $\mathcal P_0$ acts between two growths of $V$, before $\mathcal G_0$ has filled its column up to the current stage, and the next growth enumerates numbers below its restraint.

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

In :ref{#lem-hi-diagonal}, why is the true path used, rather than an arbitrary $\mathcal P_i$-node?

- [x] Because a node on the true path is initialized finitely often and visited infinitely often, so it keeps a follower and gets to act if the computation converges to $0$.
- [ ] Because only nodes on the true path act.

  Nodes to the right of the true path may act infinitely often.
- [ ] Because the true path is computable.

  The true path computes $\emptyset''$.
:::


::::exercise{#ex-hi-true-path-jump difficulty=1 objective="Show that the true path of the high incomplete construction has the degree of $\emptyset''$."}
Show that the outcome of the $\mathcal G_e$-node on the true path is $\infty$ if and only if $W_e$ is infinite, and deduce that the true path is Turing equivalent to $\emptyset''$.

:::solution
Let $\alpha = P \uh 2e$. After its last initialization, $\alpha$ keeps its record. If $W_e$ is infinite, there are infinitely many $\alpha$-expansionary stages (proof of :ref{#lem-hi-coding}), and $P(2e) = \infty$. If $W_e$ is finite, the record eventually equals $|W_e|$ and $\alpha$ is no longer expansionary, so $\alpha^\frown \infty$ is visited finitely often and $P(2e) = \mathrm f$. Hence $\mathrm{Inf}(e) = 1$ if and only if $P(2e) = \infty$, and $\emptyset'' \equiv_T \mathrm{Inf} \leq_T P$. As for the minimal pair construction (:ref{#ex-true-path-double-jump}), $P \leq_T \emptyset''$.
:::
::::

## Further results

The c.e. degrees have been studied intensively with these methods and their elaborations. We state some of the main results without proof; references are given at the end of the lesson.

- **Jump inversion** (Sacks, 1963). Every degree c.e. in and above $\mathbf 0'$ is the jump of a c.e. degree. :ref{#thm-high-incomplete} gives a c.e. degree whose jump is $\mathbf 0''$, the case of the degree $\mathbf 0''$, with the additional property that it is incomplete; the general theorem is proved by a tree construction with coding nodes of the same kind, which code a $\Sigma^0_2$ set into the columns, combined with requirements that keep the jump of the set low enough.
- **Density** (Sacks, 1964). Between any two c.e. degrees $\abf < \bbf$ there is a c.e. degree $\cbf$ with $\abf < \cbf < \bbf$. The proof combines the Sacks preservation strategy with coding, in an infinite injury argument.
- **No diamond with top $\mathbf 0'$** (Lachlan, 1966). There are no c.e. degrees $\abf$ and $\bbf$ forming a minimal pair with $\abf \vee \bbf = \mathbf 0'$.
- **Cappable degrees** (Ambos-Spies, Jockusch, Shore, Soare, 1984). A non-zero c.e. degree is **cappable** if it belongs to a minimal pair of c.e. degrees. A co-infinite c.e. set $A$ is **promptly simple** if there are a c.e. approximation $(A_s)$ and a computable function $p$ such that, for every $e$ with $W_e$ infinite, some $x$ enters $W_e$ at a stage $s$ and belongs to $A_{p(s)}$. A non-zero c.e. degree is non-cappable if and only if it contains a promptly simple set. The non-cappable degrees form a filter of the c.e. degrees, and the cappable degrees, together with $\obf$, form an ideal.
- **Minimal pairs of high degrees.** There are c.e. degrees that form a minimal pair and are both high. The proof combines the two constructions of this course on one tree; Downey and Hirschfeldt propose it as an exercise at the end of their §2.14.3.

## Notes and references

The case analysis of :ref{#lem-hi-preservation} plays the role of the main lemma of the minimal pair construction. Downey and Hirschfeldt (§2.14.3) implement the same timing idea differently: a node below the outcome $\infty$ of a coding node only *believes* a computation once all the numbers of the coded column between the restraint of higher priority and the use of the computation are in the set.

Other routes lead to high incomplete c.e. degrees. Jockusch and Shore's pseudojump inversion theorem, applied to the construction of a low simple set relative to an oracle, gives a high incomplete c.e. set through two finite injury arguments (Nies, Corollary 6.3.4). Sacks (1964) built a maximal set that is not complete, and Martin (1966) proved that a c.e. set is high if and only if it is Turing equivalent to a maximal set (Nies, p. 28; Soare, Theorem XI.2.3).

Jump inversion is proved in Soare's book (Theorem VIII.3.1) and sketched in Downey and Hirschfeldt (Theorem 2.16.4). Density is due to Sacks (1964) and is proved in Downey and Hirschfeldt, §2.15. The non-diamond theorem is due to Lachlan (1966). The characterization of the cappable degrees is due to Ambos-Spies, Jockusch, Shore and Soare (1984); the proof that a promptly simple set is not half of a minimal pair is in Nies, §1.7.

- G. E. Sacks, *Recursive enumerability and the jump operator*, Transactions of the American Mathematical Society 108 (1963), 223–239.
- G. E. Sacks, *The recursively enumerable degrees are dense*, Annals of Mathematics 80 (1964), 300–312.
- G. E. Sacks, *A maximal set which is not complete*, Michigan Mathematical Journal 11 (1964), 193–205.
- D. A. Martin, *Classes of recursively enumerable sets and degrees of unsolvability*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 12 (1966), 295–310.
- A. H. Lachlan, *Lower bounds for pairs of recursively enumerable degrees*, Proceedings of the London Mathematical Society (3) 16 (1966), 537–569.
- C. G. Jockusch and R. A. Shore, *Pseudo jump operators. I. The r.e. case*, Transactions of the American Mathematical Society 275 (1983), 599–609.
- K. Ambos-Spies, C. G. Jockusch, R. A. Shore and R. I. Soare, *An algebraic decomposition of the recursively enumerable degrees and the coincidence of several degree classes with the promptly simple degrees*, Transactions of the American Mathematical Society 281 (1984), 109–128.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.14.3, §2.15 and §2.16.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, §1.7 and §6.3.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter VIII.

:::::exercises
::::exercise{#ex-cappable-downward difficulty=1 objective="Derive from the definitions that the cappable degrees are closed downward and the non-cappable degrees upward."}
Let $\abf$ be a cappable c.e. degree, and $\cbf$ a c.e. degree with $\obf < \cbf \leq \abf$. Show that $\cbf$ is cappable. Deduce that every c.e. degree above a non-cappable c.e. degree is non-cappable.

:::solution
Let $\bbf$ be a c.e. degree such that $\abf$ and $\bbf$ form a minimal pair. If $\mathbf d \leq \cbf$ and $\mathbf d \leq \bbf$, then $\mathbf d \leq \abf$ and $\mathbf d \leq \bbf$, so $\mathbf d = \obf$. Since $\cbf > \obf$ and $\bbf > \obf$, the degrees $\cbf$ and $\bbf$ form a minimal pair, and $\cbf$ is cappable. If $\abf$ is non-cappable and $\mathbf d \geq \abf$ is c.e., then $\mathbf d \geq \abf > \obf$, and if $\mathbf d$ were cappable, $\abf$ would be cappable by the first part, applied to $\mathbf d$ and $\abf$.
:::
::::

::::exercise{#ex-hi-column-numbers difficulty=1 objective="Compute the numbers of a column of $H$ in the situation of case 4 of the preservation lemma."}
Recall that $\langle x, y \rangle = (x + y)(x + y + 1)/2 + y$. Let $\alpha$ be a $\mathcal G_1$-node and $\beta$ a $\mathcal P$-node with $\alpha^\frown \infty \preceq \beta$, and suppose that $s_0 = 10$ is $\alpha$-expansionary, that $R_\alpha = 3$ when $\alpha$ is visited at stage $s_0$, that no number of the column $1$ was in $H$ before, and that $\beta$ acts at stage $s_0$ and is never initialized afterwards. Which numbers less than $10$ belong to the column $1$, and which of them are in $H$ at the end of stage $10$? Show that every number that $\alpha$ enumerates after stage $10$ is at least $76$.

:::solution
The numbers $\langle 1, y \rangle = (y + 1)(y + 2)/2 + y$ are $1, 4, 8, 13, 19, \dots$ for $y = 0, 1, 2, 3, 4, \dots$, and they increase with $y$. Those less than $10$ are $1$, $4$ and $8$. At stage $10$, $\alpha$ enumerates every $\langle 1, y \rangle$ with $y < 10$ and $\langle 1, y \rangle \geq 3$, that is, all of them except $\langle 1, 0 \rangle = 1$. So $4$ and $8$ are in $H$, and $1$ is not.

Let $t > 10$ be an $\alpha$-expansionary stage. The numbers $\langle 1, y \rangle$ with $1 \leq y < 10$ are already in $H$. By the proof of :ref{#lem-hi-preservation} (case 4), $\alpha$ does not enumerate $\langle 1, 0 \rangle$ at stage $t$: this would require the restraint that kept it out to be released, which would initialize $\beta$. So $\alpha$ only enumerates numbers $\langle 1, y \rangle$ with $y \geq 10$, and $\langle 1, y \rangle \geq \langle 1, 10 \rangle = 11 \cdot 12 / 2 + 10 = 76$.
:::
::::

::::exercise{#ex-hi-same-stage difficulty=1 objective="Check the step of the preservation lemma at the stage at which the diagonalization node acts."}
Let a $\mathcal P$-node $\beta$ act at stage $s_0$. Show that every node visited after $\beta$ at stage $s_0$ extends $\beta^\frown \mathrm f$, and that a $\mathcal G_e$-node visited after $\beta$ at stage $s_0$ enumerates no number less than $s_0$ at that stage. Which case of the proof of :ref{#lem-hi-preservation} does this settle when $t = s_0$, and which rule of the construction does it use?

:::solution
A $\mathcal P$-node has outcome $\mathrm f$ at every visit, so the node visited after $\beta$ is $\beta^\frown \mathrm f$, and every later node visited at stage $s_0$ extends it. Let $\alpha$ be such a $\mathcal G_e$-node. Then $\beta \prec \alpha$, so $\beta$ has higher priority than $\alpha$, and when $\alpha$ is visited, $r_\beta = s_0$ has already been set. Hence $R_\alpha \geq s_0$, and $\alpha$ only enumerates numbers $\langle e, y \rangle \geq R_\alpha \geq s_0$.

This is case 1 of the proof of :ref{#lem-hi-preservation} (a node of lower priority than $\beta$) at the stage $t = s_0$. It uses the rule that the bound $R_\alpha$ is computed from the current restraints during the stage, so that the node visited after a $\mathcal P$-node that acts already sees its restraint. The nodes of higher priority than $\beta$ visited at stage $s_0$ are its prefixes, visited before $\beta$, whose enumerations at stage $s_0$ precede the action of $\beta$ and are part of the approximation $\tilde H$ used by $\beta$.
:::
::::

::::exercise{#ex-prompt-simple-simple difficulty=2 objective="Relate prompt simplicity to simplicity, and see that the computability of the delay function is the point of the definition."}
Use the definition of promptly simple sets stated in the lesson, and say that $x$ enters $W_e$ at stage $s$ if $x \in W_{e,s} \setminus W_{e,s-1}$, where each $W_{e,s}$ is finite.

1. Show that every promptly simple set is simple.
2. Let $A$ be a simple set with a c.e. approximation $(A_s)$. Show that there is a function $p \leq_T \emptyset'$ such that, for every $e$ with $W_e$ infinite, some $x$ enters $W_e$ at a stage $s$ and belongs to $A_{p(s)}$.

:::solution
1. Let $A$ be promptly simple, via $(A_s)$ and $p$. It is c.e. and co-infinite by definition. If $W_e$ is infinite, some $x$ enters $W_e$ at a stage $s$ and belongs to $A_{p(s)} \subseteq A$, so $W_e \cap A \neq \emptyset$. Hence $A$ is simple.

2. Let $p(s)$ be the least $t$ such that $A_t \cap F_s = A \cap F_s$, where $F_s = \bigcup_{e \leq s} W_{e,s}$ is a finite set computable from $s$. Since $(A_s)$ is increasing with union $A$, such a $t$ exists, and $\emptyset'$ finds it: $A$ is computable in $\emptyset'$, so $\emptyset'$ computes $A \cap F_s$, and then searches for $t$. Let $W_e$ be infinite. For every finite set $F$, $W_e \setminus F$ is an infinite c.e. set, so it meets $A$; hence $W_e \cap A$ is infinite. Only finitely many elements of $W_e$ enter it at a stage $s < e$, since $W_{e,e-1}$ is finite, so some $x \in W_e \cap A$ enters $W_e$ at a stage $s \geq e$. Then $x \in W_{e,s} \subseteq F_s$ and $x \in A$, so $x \in A_{p(s)}$.

So every simple set satisfies the condition of prompt simplicity with a delay function computable in $\emptyset'$; what the definition adds is that the delay is computable. This is a real restriction: the sets $A$ and $B$ of :ref{#ex-mp-simple} are simple and form a minimal pair, so their degrees are cappable, while the degree of a promptly simple set is non-cappable (:ref{#ex-prompt-noncappable}).
:::
::::

::::exercise{#ex-prompt-noncappable difficulty=3 objective="Prove that a promptly simple set is not half of a minimal pair, by permitting and the fixed point theorem."}
Let $E$ be promptly simple, via the approximation $(E_s)$ and the computable function $p$, and let $C$ be a non-computable c.e. set with an approximation $(C_s)$. Build a simple set $A$ with $A \leq_T C$ and $A \leq_T E$. Deduce that the degree of $E$ is non-cappable.

:::solution
*Idea.* $A$ meets the simplicity requirements $\mathcal S_i$: if $W_i$ is infinite, then $W_i \cap A \neq \emptyset$. A number $x$ may enter $A$ at stage $s$ only if $C$ changes below $x$ at stage $s$ (permitting by $C$), and only if $E$ changes below $x$ at stage $s$ or later (delayed permitting by $E$). To obtain the change of $E$, the requirement $\mathcal S_i$ enumerates a number $y < x$ into an auxiliary c.e. set $G_i$; when $y$ appears in the enumeration of $G_i$, prompt simplicity forces some such $y$ to enter $E$ within the delay $p$. For this the construction must know indices of the sets $G_i$ in advance, which the fixed point theorem provides.

*Indices.* For a number $r$, let $g_r(i)$ be an index, computable from $r$ and $i$, with $W_{g_r(i)} = \{ y : \langle i, y \rangle \in W_r \}$. The construction below, with $g = g_r$, enumerates sets $G^r_i$ uniformly in $r$ and $i$ (a stage may never end; the sets are then finite). There is a computable $f$ with $W_{f(r)} = \{ \langle i, y \rangle : y \in G^r_i \}$. By :ref{#thm-fixed-point}, there is $r$ with $\Phi_{f(r)} = \Phi_r$, so $W_{f(r)} = W_r$ and $W_{g_r(i)} = G^r_i$ for every $i$. We fix this $r$, write $g = g_r$ and $G_i = G^r_i$.

*Construction.* $A_0 = \emptyset$ and $G_{i,0} = \emptyset$. At stage $s \geq 1$, call $i < s$ *eligible* if $\mathcal S_i$ is not declared satisfied, $W_{g(i),s-1} = G_{i,s-1}$, and there are $x$ and $y$ with $x \geq 2i$, $x \in W_{i,s}$, $C_s \uh x \neq C_{s-1} \uh x$, $y < x$ and $y \notin E_{s-1} \cup G_{i,s-1}$. If some $i$ is eligible, take the least one, and the least such $x$ and then $y$; $\mathcal S_i$ *attempts*: put $y$ into $G_i$, and search for the least $t$ with $y \in W_{g(i),t}$. If $y \in E_{p(t)}$, put $x$ into $A$ and declare $\mathcal S_i$ satisfied. Then go to the next stage.

The search ends, since $y \in G_i = W_{g(i)}$. Since $W_{g(i),s-1} = G_{i,s-1}$ and $y \notin G_{i,s-1}$, we have $y \notin W_{g(i),s-1}$, so $y$ enters $W_{g(i)}$ at the stage $t \geq s$ found by the search.

*Reductions.* If $x$ enters $A$ at stage $s$, then $C_s \uh x \neq C_{s-1} \uh x$. Given $x$, the oracle $C$ finds a stage $s_x$ with $C_{s_x} \uh x = C \uh x$; then $C$ does not change below $x$ after $s_x$, so $x \in A$ if and only if $x \in A_{s_x}$. Hence $A \leq_T C$. If $x$ enters $A$ at stage $s$, the number $y < x$ attached to it satisfies $y \notin E_{s-1}$ and $y \in E_{p(t)} \subseteq E$, so $E_{s-1} \uh x \neq E \uh x$. Given $x$, the oracle $E$ finds a stage $u_x$ with $E_{u_x} \uh x = E \uh x$; $x$ cannot enter $A$ at a stage $s > u_x$, so $x \in A$ if and only if $x \in A_{u_x}$. Hence $A \leq_T E$.

*Each requirement attempts finitely often and is met.* Suppose, by induction, that every $\mathcal S_j$ with $j < i$ attempts only finitely often, and let $s_0$ be a stage after which none of them attempts; after $s_0$, none of them is eligible, since an eligible requirement of least index attempts.

Suppose first that $\mathcal S_i$ attempts infinitely often. Then $G_i = W_{g(i)}$ is infinite, so by prompt simplicity some $y$ enters $W_{g(i)}$ at a stage $t$ with $y \in E_{p(t)}$. This $y$ was put into $G_i$ by an attempt at a stage $s$, whose search found this $t$; the attempt then put its $x$ into $A$, and $\mathcal S_i$ was declared satisfied and never attempted again. This is a contradiction, so $\mathcal S_i$ attempts finitely often, and $G_i$ is finite.

Suppose now that $W_i$ is infinite and that $\mathcal S_i$ is never satisfied. Since $G_i$ is finite and $E$ is co-infinite, there is a bound $b$ such that every $x \geq b$ has some $y < x$ with $y \notin E \cup G_i$; and there is a stage $s_1 \geq s_0$ after which $\mathcal S_i$ does not attempt, $G_{i,s} = G_i$, and $W_{g(i),s} = G_i$. For $x \in W_i$ with $x \geq \max(2i, b)$, let $s_x$ be the stage at which $x$ enters $W_i$, and suppose $s_x > s_1$. If $C_s \uh x \neq C_{s-1} \uh x$ for some $s \geq s_x$, then $\mathcal S_i$ is eligible at stage $s$, with this $x$ and a $y < x$ outside $E \supseteq E_{s-1}$ and outside $G_i$, and it attempts: impossible. So $C \uh x = C_{s_x} \uh x$ for infinitely many $x$, all those of $W_i$ larger than $\max(2i, b)$ entering after $s_1$, and these $x$ and $s_x$ are found by enumerating $W_i$. This makes $C$ computable: a contradiction. Hence $\mathcal S_i$ is met.

*Conclusion.* Each $\mathcal S_i$ puts at most one number into $A$, and it is at least $2i$, so $A$ has at most $n$ elements below $2n$, and $\overline A$ is infinite. With the requirements $\mathcal S_i$, $A$ is simple, hence not computable. So $A$ is a non-computable set below both $C$ and $E$. Now $E$ is simple by :ref{#ex-prompt-simple-simple}, so its degree is not $\obf$; and for every non-zero c.e. degree $\bbf$, applying the construction to a set $C \in \bbf$ gives a non-zero degree below both, so the degree of $E$ and $\bbf$ never form a minimal pair. The degree of $E$ is non-cappable.

Adapted from Nies 2009, Theorem 1.7.14, where the set $A$ is moreover obtained effectively from $C$ and the reductions are weak truth-table reductions.
:::
::::
:::::
