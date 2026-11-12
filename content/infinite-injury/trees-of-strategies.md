---
title: Guessing on a tree of strategies
summary: The strategy for a minimal pair requirement and its two outcomes; why the strategies of lower priority must guess the outcome; the tree of strategies, its priority order, and the construction along the current path, with initialization to the right of the current path.
duration: 45
prerequisites: [minimal-pairs]
---

The previous lesson reduced the minimal pair theorem to requirements $\mathcal N_e$, $\mathcal R_e$ and $\mathcal S_e$, and proved that a computation agreed on by both sides keeps its value as long as only one side changes between consecutive expansionary stages (:ref{#lem-pair-module}). This lesson turns the lemma into a strategy for $\mathcal N_e$, shows that the strategies of lower priority must behave differently according to the outcome of this strategy, which the construction cannot compute, and organizes the resulting guesses on a tree. The next lesson verifies the construction.

## The strategy and its two outcomes

The strategy for $\mathcal N_e$ is now the following: it is run at a set $Q$ of stages and computes the expansionary stages for $Q$. It enumerates nothing and imposes no explicit restraint. Instead, it constrains how the requirements below it act, so that condition 2 of :ref{#lem-pair-module} holds between consecutive expansionary stages. It has two possible **outcomes**:

- **$\infty$**: there are infinitely many expansionary stages;
- **$\mathrm f$**: there are finitely many expansionary stages. By :ref{#prop-agreement-unbounded}, $\Phi^A_e = \Phi^B_e$ is then not total, and $\mathcal N_e$ holds trivially, provided $Q$ is infinite.

Consider a requirement $\mathcal R_d$ of lower priority. It acts by enumerating a follower $x$ into $A$ once $x$ appears in $W_d$. Two strategies are possible.

1. *If the outcome of $\mathcal N_e$ is $\infty$:* act only at expansionary stages, immediately after $\mathcal N_e$ has found the new expansionary stage. Then an action changes $A$ at stage $s_k$, after the computations of stage $s_k$ have been examined; if at most one element enters $A \cup B$ below $s_k$ between $s_k$ and $s_{k+1}$, condition 2 holds. Since there are infinitely many expansionary stages, $\mathcal R_d$ gets infinitely many opportunities to act.
2. *If the outcome is $\mathrm f$:* act at any stage, after the last expansionary stage. The strategy of $\mathcal N_e$ imposes nothing after that stage. With strategy 1, $\mathcal R_d$ would wait forever.

The construction cannot know which outcome holds: the outcome $\infty$ is a $\Pi^0_2$ property. It runs both versions of $\mathcal R_d$, one guessing each outcome. The version guessing $\mathrm f$ is **initialized** at every expansionary stage, and chooses its followers larger than the last expansionary stage, so that its actions never destroy computations examined by $\mathcal N_e$ at that stage. If the outcome is $\infty$, this version is initialized infinitely often and may act infinitely often: it is injured infinitely often, which is harmless, since the other version meets $\mathcal R_d$.

The same splitting is needed for the requirements $\mathcal N_{e'}$ of lower priority, for a reason of coherence. Suppose that $\mathcal N_{e'}$ computed its expansionary stages among all stages, and that $\mathcal N_e$ and $\mathcal N_{e'}$ both have infinitely many expansionary stages. A requirement $\mathcal R_d$ of lower priority than both, using strategy 1 for both, may only act at stages that are expansionary for both, and the two infinite sets of expansionary stages may be disjoint: $\mathcal R_d$ would never act. So the version of $\mathcal N_{e'}$ that guesses the outcome $\infty$ for $\mathcal N_e$ is run only at the expansionary stages of $\mathcal N_e$. This is why :ref{#def-expansionary} defines the expansionary stages relative to a set $Q$: with $Q$ the set of expansionary stages of $\mathcal N_e$, every expansionary stage of $\mathcal N_{e'}$ is also expansionary for $\mathcal N_e$. Iterating the case distinction gives a **tree of strategies**, one level per requirement, and one branch for each guess about the outcomes of the requirements above. The rest of this lesson defines it precisely.

:::quiz[guessing outcomes]
Why must the version of $\mathcal R_d$ guessing the outcome $\mathrm f$ choose followers larger than the last expansionary stage?

- [x] So that its enumerations between two expansionary stages are above the uses of the computations examined at the earlier one, and do not count against condition 2 of :ref{#lem-pair-module}.
- [ ] So that $\mathcal R_d$ is met.

  Any follower serves $\mathcal R_d$: either it appears in $W_d$ and is enumerated into $A$, or it never appears in $W_d$ and stays outside $A$. The size matters for $\mathcal N_e$.
- [ ] Because followers must be fresh in every priority argument.

  Freshness is a tool; here its purpose is precisely to protect the computations seen by $\mathcal N_e$.

---

Why can the construction not simply determine the outcome of $\mathcal N_e$ and use the corresponding strategy for $\mathcal R_d$?

- [x] Because the outcome $\infty$, "there are infinitely many expansionary stages", is a $\Pi^0_2$ property, not decidable during a computable construction.
- [ ] Because the outcome changes during the construction.

  The outcome is a property of the whole construction; what changes is the current guess about it.
- [ ] Because $\mathcal N_e$ has more than two outcomes.

  It has exactly two.
:::

## The tree method

The **tree method** assigns to each requirement one strategy for each possible guess about the outcomes of the strategies above it. At every stage, the construction computes a current guess, a finite path through the tree, and only runs the strategies along it. The **true path**, the leftmost path visited infinitely often, will consist of the strategies whose guesses are correct; it is defined and studied in the next lesson.

The same organization applies to finite injury arguments: Downey and Hirschfeldt present the Friedberg–Muchnik construction on a binary tree, whose outcomes record whether a strategy has enumerated its follower. There the current guess about each strategy can only move to the left, once, and the true path is computable in $\emptyset'$. In an infinite injury argument the guess about an $\mathcal N$-node moves to the left at each expansionary stage and back to the right in between, and the true path is only computable in $\emptyset''$, as an exercise of the next lesson shows (:ref{#ex-true-path-double-jump}).

## The tree and the priority order

Let $\Lambda = \{ \infty, \mathrm f \}$, ordered by $\infty < \mathrm f$. We list the requirements as $\mathcal N_0, \mathcal R_0, \mathcal S_0, \mathcal N_1, \mathcal R_1, \mathcal S_1, \dots$, so that the requirement of index $3e$ is $\mathcal N_e$, that of index $3e + 1$ is $\mathcal R_e$, and that of index $3e + 2$ is $\mathcal S_e$.

:::definition{#def-strategy-tree}
1. The **tree of strategies** is the set $\mathbb T$ of finite strings $\alpha \in \Lambda^{<\nat}$ such that $\alpha(n) = \mathrm f$ whenever $n$ is not a multiple of $3$. A string $\alpha \in \mathbb T$ is a **node**, and the node $\alpha$ works for the requirement of index $|\alpha|$: it is an $\mathcal N_e$-node if $|\alpha| = 3e$, and so on.
2. For nodes $\alpha$ and $\beta$, $\alpha$ is **to the left** of $\beta$, written $\alpha <_L \beta$, if there is $n$ with $\alpha \uh n = \beta \uh n$, $\alpha(n) = \infty$ and $\beta(n) = \mathrm f$.
3. $\alpha$ has **higher priority** than $\beta$ if $\alpha \prec \beta$ or $\alpha <_L \beta$.
:::

The $\mathcal N$-nodes have two outcomes, the other nodes only the outcome $\mathrm f$. A node $\beta$ with $\alpha^\frown \infty \preceq \beta$ guesses that the $\mathcal N$-node $\alpha$ has infinitely many expansionary stages, and a node with $\alpha^\frown \mathrm f \preceq \beta$ that it has finitely many. For any two distinct nodes, either one is a prefix of the other, or one is to the left of the other; the priority order is a linear order on $\mathbb T$. Unlike the priority orders of finite injury arguments, it gives most nodes infinitely many nodes of higher priority: a node with the value $\mathrm f$ at some $\mathcal N$-level $n$ has to its left every extension of $(\alpha \uh n)^\frown \infty$.

:::figure[The first levels of the tree of strategies. The column on the right gives the requirement of each level. The highlighted path is the true path of a construction in which $\mathcal N_0$ has infinitely many expansionary stages and $\mathcal N_1$, on that branch, has infinitely many as well. All the nodes on the right half have lower priority than all the nodes of the highlighted path.]
<svg class="fig" viewBox="0 0 590 250" width="590" role="img" aria-label="The first levels of the tree of strategies of the minimal pair construction: each N node has two outcomes, infinite on the left and finite on the right; the other nodes have one outcome"><line x1="250" y1="41" x2="130" y2="73" class="accent-stroke" stroke-width="2.4"/><text x="178" y="59" class="mrm" font-size="14">∞</text><line x1="250" y1="41" x2="370" y2="73" class="muted-stroke" stroke-width="1.3"/><text x="318" y="59" class="math" font-size="14">f</text><line x1="130" y1="87" x2="130" y2="119" class="accent-stroke" stroke-width="2.4"/><line x1="370" y1="87" x2="370" y2="119" class="muted-stroke" stroke-width="1.3"/><line x1="130" y1="133" x2="130" y2="165" class="accent-stroke" stroke-width="2.4"/><line x1="370" y1="133" x2="370" y2="165" class="muted-stroke" stroke-width="1.3"/><line x1="130" y1="179" x2="70" y2="211" class="accent-stroke" stroke-width="2.4"/><text x="88" y="197" class="mrm" font-size="14">∞</text><line x1="130" y1="179" x2="190" y2="211" class="muted-stroke" stroke-width="1.3"/><text x="168" y="197" class="math" font-size="14">f</text><line x1="370" y1="179" x2="310" y2="211" class="muted-stroke" stroke-width="1.3"/><text x="328" y="197" class="mrm" font-size="14">∞</text><line x1="370" y1="179" x2="430" y2="211" class="muted-stroke" stroke-width="1.3"/><text x="408" y="197" class="math" font-size="14">f</text><circle cx="250" cy="34" r="6" class="accent-fill"/><circle cx="130" cy="80" r="6" class="accent-fill"/><circle cx="370" cy="80" r="6" class="node"/><circle cx="130" cy="126" r="6" class="accent-fill"/><circle cx="370" cy="126" r="6" class="node"/><circle cx="130" cy="172" r="6" class="accent-fill"/><circle cx="370" cy="172" r="6" class="node"/><circle cx="70" cy="218" r="6" class="accent-fill"/><circle cx="190" cy="218" r="6" class="node"/><circle cx="310" cy="218" r="6" class="node"/><circle cx="430" cy="218" r="6" class="node"/><line x1="70" y1="226" x2="70" y2="244" class="muted-stroke" stroke-width="1.3" stroke-dasharray="2 3"/><line x1="190" y1="226" x2="190" y2="244" class="muted-stroke" stroke-width="1.3" stroke-dasharray="2 3"/><line x1="310" y1="226" x2="310" y2="244" class="muted-stroke" stroke-width="1.3" stroke-dasharray="2 3"/><line x1="430" y1="226" x2="430" y2="244" class="muted-stroke" stroke-width="1.3" stroke-dasharray="2 3"/><text x="520" y="39" class="math" font-size="16">N<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="470" y1="34" x2="505" y2="34" class="axis" stroke-dasharray="2 4"/><text x="520" y="85" class="math" font-size="16">R<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="470" y1="80" x2="505" y2="80" class="axis" stroke-dasharray="2 4"/><text x="520" y="131" class="math" font-size="16">S<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="470" y1="126" x2="505" y2="126" class="axis" stroke-dasharray="2 4"/><text x="520" y="177" class="math" font-size="16">N<tspan class="mrm" font-size="10" dy="4">1</tspan></text><line x1="470" y1="172" x2="505" y2="172" class="axis" stroke-dasharray="2 4"/><text x="520" y="223" class="math" font-size="16">R<tspan class="mrm" font-size="10" dy="4">1</tspan></text><line x1="470" y1="218" x2="505" y2="218" class="axis" stroke-dasharray="2 4"/></svg>
:::

## The construction

Each node carries some data, which **initializing** the node resets.

- An $\mathcal N_e$-node $\alpha$ has a **record** $m_\alpha$, a number or undefined. Initialization makes it undefined.
- An $\mathcal R_e$-node or $\mathcal S_e$-node $\beta$ may have a **follower** $x_\beta$, and may be marked **satisfied**. Initialization cancels the follower and the mark.

A number is **fresh** at a stage if it is larger than the stage and than every number mentioned so far in the construction. Initially every node is initialized, and $A_0 = B_0 = \emptyset$.

*Stage $s$.* We define the **current path** $\sigma_s \in \mathbb T$, of length at most $s$, by visiting nodes one after the other, starting with the root; when a node $\alpha$ is visited with outcome $o$, the next node to visit is $\alpha^\frown o$. A node of length $s$ is not visited, and the stage also ends when a node acts. Let $\alpha$ be the node visited.

1. If $\alpha$ is an $\mathcal N_e$-node, compute the length of agreement $l(e, s)$ of $\Phi^{A_s}_e$ and $\Phi^{B_s}_e$ (:ref{#def-expansionary}). The stage $s$ is **$\alpha$-expansionary** if $m_\alpha$ is undefined or $l(e, s) > m_\alpha$. In that case, set $m_\alpha = l(e, s)$, and the outcome is $\infty$; otherwise the outcome is $\mathrm f$.
2. If $\alpha$ is an $\mathcal R_e$-node without a follower, it receives a fresh follower; the outcome is $\mathrm f$. If it has a follower $x$, is not marked satisfied, and $x \in W_{e,s}$, then $\alpha$ **acts**: $x$ is enumerated into $A$, $\alpha$ is marked satisfied, the stage ends, and $\sigma_s = \alpha^\frown \mathrm f$. Otherwise the outcome is $\mathrm f$.
3. $\mathcal S_e$-nodes are treated in the same way, with $B$ in place of $A$.

At the end of the stage, initialize every node $\beta$ with $\sigma_s <_L \beta$. Then $A_{s+1}$ and $B_{s+1}$ are $A_s$ and $B_s$ with the element enumerated at stage $s$, if any.

A node $\alpha$ is **visited at stage $s$**, and $s$ is an **$\alpha$-stage**, if $\alpha \prec \sigma_s$, strictly. At each stage, at most one number is enumerated, at the very end, after all the computations of the stage have been examined. The construction is computable, so $A$ and $B$ are c.e. Followers are fresh, so distinct followers are distinct numbers, and a follower enters $A$ or $B$ only through the action of its own node. In particular $A \cap B = \emptyset$.

In the Friedberg–Muchnik construction, an action initializes every requirement of lower priority. Here, initialization is triggered by the current path, not by actions: a node is initialized when the construction moves to its left. The initialization rule replaces the explicit restraints of finite injury arguments. A node to the right of the current path has made a guess that the current stage refutes, at least for now: it loses its follower, and the next follower it receives is fresh, hence larger than every use of a computation examined so far.

## Exercises

::::exercise{difficulty=1}
Show that the priority order of :ref{#def-strategy-tree} is a strict linear order on $\mathbb T$. Show that a node $\beta$ has infinitely many nodes of higher priority if $\beta(n) = \mathrm f$ for some multiple $n$ of $3$ with $n < |\beta|$, and only its proper prefixes otherwise.

:::solution
Write $\alpha \lhd \beta$ when $\alpha$ has higher priority than $\beta$. No node is a proper prefix of itself or to the left of itself, so $\lhd$ is irreflexive. If $\alpha \neq \beta$ and neither is a prefix of the other, let $n$ be the first position where they differ; since $\Lambda$ has two elements, one of them has the value $\infty$ at $n$ and is to the left of the other. So any two distinct nodes are comparable.

Transitivity: let $\alpha \lhd \beta \lhd \gamma$.
- If $\alpha \prec \beta \prec \gamma$, then $\alpha \prec \gamma$.
- If $\alpha \prec \beta$ and $\beta <_L \gamma$, with first difference at $n$: if $|\alpha| \leq n$, then $\alpha \preceq \beta \uh n = \gamma \uh n$, and $\alpha \prec \gamma$ since $|\alpha| \leq n < |\gamma|$; otherwise $\alpha \uh n = \gamma \uh n$ and $\alpha(n) = \beta(n) = \infty \neq \gamma(n)$, so $\alpha <_L \gamma$.
- If $\alpha <_L \beta$, with first difference at $n$, and $\beta \prec \gamma$, then $\gamma \uh (n + 1) = \beta \uh (n + 1)$, so $\alpha <_L \gamma$.
- If $\alpha <_L \beta$ at $n$ and $\beta <_L \gamma$ at $m$, then $n \neq m$, since $\beta(n) = \mathrm f$ and $\beta(m) = \infty$. If $n < m$, then $\alpha \uh n = \gamma \uh n$, $\alpha(n) = \infty$ and $\gamma(n) = \beta(n) = \mathrm f$. If $m < n$, then $\alpha \uh m = \gamma \uh m$, $\alpha(m) = \beta(m) = \infty$ and $\gamma(m) = \mathrm f$. In both cases $\alpha <_L \gamma$.

If $\beta(n) = \mathrm f$ with $n$ a multiple of $3$, every node extending $(\beta \uh n)^\frown \infty$ is to the left of $\beta$, and there are infinitely many. Otherwise, a node $\alpha <_L \beta$ would need a position $n$ with $\alpha(n) = \infty$ and $\beta(n) = \mathrm f$; such an $n$ is a multiple of $3$, since the other positions have the value $\mathrm f$ in every node, and there is none. So the nodes of higher priority are the proper prefixes of $\beta$.
:::
::::

## Notes and references

Infinite injury arguments were introduced in the 1960s by Sacks, Shoenfield and Yates, without trees. According to Lempp and Lerman, the tree of strategies was introduced by Lachlan (1975), in a $\mathbf 0'''$-argument, developed by Harrington, and popularized by Soare's book. Lempp and Lerman also describe Harrington's classification of priority arguments by the oracle needed to determine how each requirement is satisfied: finite injury arguments are $\mathbf 0'$-arguments, the infinite injury arguments of this course are $\mathbf 0''$-arguments, since the true path is computable in $\emptyset''$, and so on. Downey and Hirschfeldt (§2.14.1) present trees of strategies first on the Friedberg–Muchnik construction, as in the remark of the section on the tree method, and discuss the coherence problem between two $\mathcal N$-requirements in §2.14.2.

Other presentations exist. Montalbán's true stages replace the guesses along a tree by approximations to the iterated jumps of $\emptyset$, and a stage is $\xi$-true when its approximation to the $\xi$-th jump is correct; the method is designed for iterated priority arguments, in the tradition of Ash's metatheorem, and has been applied in descriptive set theory by Day, Greenberg, Harrison-Trainor and Turetsky. For the $\mathbf 0''$-arguments of this course, trees remain the standard presentation of the textbooks, and we use them.

- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter IX (minimal pairs) and Chapter XIV (the tree method for $\mathbf 0'''$-arguments).
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.14.1–2.14.2.
- A. H. Lachlan, *A recursively enumerable degree which will not split over all lesser ones*, Annals of Mathematical Logic 9 (1975), 307–365.
- S. Lempp and M. Lerman, *A general framework for priority arguments*, Bulletin of Symbolic Logic 1 (1995), 189–201.
- A. Montalbán, *Priority arguments via true stages*, Journal of Symbolic Logic 79 (2014), 1315–1335.
- A. Day, N. Greenberg, M. Harrison-Trainor and D. Turetsky, *Iterated priority arguments in descriptive set theory*, Bulletin of Symbolic Logic 30 (2024), 199–226.
