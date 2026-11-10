---
title: Trees of strategies
summary: The tree of strategies of the minimal pair construction; the priority order, initialization to the right of the current path, and the true path; the verification of the minimal pair theorem.
duration: 45
prerequisites: [minimal-pairs]
---

The previous lesson reduced the minimal pair theorem to requirements $\mathcal N_e$, $\mathcal R_e$ and $\mathcal S_e$, and showed that the strategy for $\mathcal R_d$ below $\mathcal N_e$ depends on the outcome of $\mathcal N_e$, which the construction cannot compute. The **tree method** assigns to each requirement one strategy for each possible guess about the outcomes of the strategies above it. At every stage, the construction computes a current guess, a finite path through the tree, and only runs the strategies along it. The **true path**, the leftmost path visited infinitely often, consists of the strategies whose guesses are correct; the verification shows that they meet their requirements.

## The tree and the priority order

Let $\Lambda = \{ \infty, \mathrm f \}$, ordered by $\infty < \mathrm f$. We list the requirements as $\mathcal N_0, \mathcal R_0, \mathcal S_0, \mathcal N_1, \mathcal R_1, \mathcal S_1, \dots$, so that the requirement of index $3e$ is $\mathcal N_e$, that of index $3e + 1$ is $\mathcal R_e$, and that of index $3e + 2$ is $\mathcal S_e$.

:::definition{#def-strategy-tree}
1. The **tree of strategies** is the set $\mathbb T$ of finite strings $\alpha \in \Lambda^{<\nat}$ such that $\alpha(n) = \mathrm f$ whenever $n$ is not a multiple of $3$. A string $\alpha \in \mathbb T$ is a **node**, and the node $\alpha$ works for the requirement of index $|\alpha|$: it is an $\mathcal N_e$-node if $|\alpha| = 3e$, and so on.
2. For nodes $\alpha$ and $\beta$, $\alpha$ is **to the left** of $\beta$, written $\alpha <_L \beta$, if there is $n$ with $\alpha \uh n = \beta \uh n$, $\alpha(n) = \infty$ and $\beta(n) = \mathrm f$.
3. $\alpha$ has **higher priority** than $\beta$ if $\alpha \prec \beta$ or $\alpha <_L \beta$.
:::

The $\mathcal N$-nodes have two outcomes, the other nodes only the outcome $\mathrm f$. A node $\beta$ with $\alpha^\frown \infty \preceq \beta$ guesses that the $\mathcal N$-node $\alpha$ has infinitely many expansionary stages, and a node with $\alpha^\frown \mathrm f \preceq \beta$ that it has finitely many. For any two distinct nodes, either one is a prefix of the other, or one is to the left of the other; the priority order is a linear order on $\mathbb T$, but a node has infinitely many nodes of higher priority, all those to its left.

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

The initialization rule replaces the explicit restraints of finite injury arguments. A node to the right of the current path has made a guess that the current stage refutes, at least for now: it loses its follower, and the next follower it receives is fresh, hence larger than every use of a computation examined so far.

## The true path

:::definition{#def-true-path}
The **true path** is the infinite sequence $P \in \Lambda^\nat$ defined by induction: $P(n)$ is the least $o \in \Lambda$ such that $(P \uh n)^\frown o$ is visited at infinitely many stages.
:::

:::lemma{#lem-true-path}
For every $n$, the true path is defined at $n$, and the node $\alpha = P \uh n$ satisfies:

1. $\alpha$ is visited at infinitely many stages;
2. $\sigma_s <_L \alpha$ holds for only finitely many $s$; in particular $\alpha$ is initialized only finitely often;
3. if $\alpha$ is an $\mathcal R$- or $\mathcal S$-node, it acts only finitely often.
:::

:::proof{of=lem-true-path}
By induction on $n$. The root is visited at every stage $s \geq 1$, and no path is to its left.

Suppose that $\alpha = P \uh n$ satisfies items 1 and 2. A node is initialized only at the end of a stage $s$ with $\sigma_s <_L \alpha$, so it is initialized finitely often. If $\alpha$ is an $\mathcal R$- or $\mathcal S$-node, then between two initializations it acts at most once, since it is then marked satisfied; this gives item 3. Let $s_0$ be a stage after which $\alpha$ never acts, nor is initialized, nor satisfies $\sigma_s <_L \alpha$.

*Case 1: $\alpha$ is an $\mathcal R$- or $\mathcal S$-node.* At every $\alpha$-stage $s > \max(s_0, n + 1)$, $\alpha$ does not act and $\alpha^\frown \mathrm f$ has length less than $s$, so $\alpha^\frown \mathrm f$ is visited. So $P(n) = \mathrm f$, and $\alpha^\frown \mathrm f$ satisfies item 1. A node to the left of $\alpha^\frown \mathrm f$ is to the left of $\alpha$, since no node has the value $\infty$ at position $n$; this gives item 2.

*Case 2: $\alpha$ is an $\mathcal N$-node.* At every $\alpha$-stage $s > n + 1$, $\alpha^\frown o$ is visited, where $o$ is the outcome of $\alpha$ at $s$. If the outcome $\infty$ occurs at infinitely many stages, $P(n) = \infty$, and a path to the left of $\alpha^\frown \infty$ is to the left of $\alpha$. Otherwise, $P(n) = \mathrm f$, the node $\alpha^\frown \mathrm f$ is visited at all $\alpha$-stages after the last $\alpha$-expansionary stage, and a path to the left of $\alpha^\frown \mathrm f$ is either to the left of $\alpha$ or extends $\alpha^\frown \infty$; both happen only finitely often.
:::

Item 2 is the reason why the priority order puts every node to the left of $\alpha$ above it. A node $\beta$ to the right of the true path may be initialized infinitely often, and act infinitely often, each time with a new follower: if $\beta$ extends $\alpha^\frown \mathrm f$ while the true outcome of $\alpha$ is $\infty$, $\beta$ is initialized at every $\alpha$-expansionary stage. This is the infinite injury. It is harmless, because the requirement of $\beta$ is met by the node of the same level on the true path, and because the actions of $\beta$ only enumerate fresh numbers.

:::quiz[the true path]
Why is the true path defined with the leftmost outcome visited infinitely often, rather than any outcome visited infinitely often?

- [x] Because the leftmost one is the correct guess: if $\alpha^\frown \infty$ is visited infinitely often, $\alpha$ has infinitely many expansionary stages, while $\alpha^\frown \mathrm f$ may also be visited infinitely often, at the stages between them.
- [ ] Because only one outcome is visited infinitely often.

  Both outcomes of an $\mathcal N$-node may be visited infinitely often.
- [ ] Because the leftmost outcome is computable.

  The true path is computable in $\emptyset''$, not computable in general.

---

Why must a node to the left of $\alpha$ have higher priority than $\alpha$, rather than lower?

- [x] Because a node to the right of the true path may act infinitely often; if it had higher priority than the nodes of the true path, these could be injured infinitely often.
- [ ] Because nodes to the left are visited more often.

  Nodes to the left of the true path are visited only finitely often.
- [ ] Because the tree order must be well-founded.

  The priority order is not a well-ordering: a node has infinitely many nodes of higher priority.
:::

## Verification

:::lemma{#lem-mp-positive}
Every requirement $\mathcal R_e$ and $\mathcal S_e$ is met.
:::

:::proof{of=lem-mp-positive}
Let $\beta = P \uh (3e + 1)$, the $\mathcal R_e$-node on the true path. By :ref{#lem-true-path}, $\beta$ is initialized finitely often and visited infinitely often. At its first visit after its last initialization, it receives a follower $x$, which it keeps forever. If $x \in W_e$, at the first $\beta$-stage $s$ with $x \in W_{e,s}$, $\beta$ is not yet marked satisfied, so it acts, and $x \in A \cap W_e$. If $x \notin W_e$, then $\beta$ never enumerates $x$, no other node does, and $x \in \overline A \setminus W_e$. In both cases $W_e \neq \overline A$. The argument for $\mathcal S_e$ is the same.
:::

The main lemma checks condition 2 of :ref{#lem-pair-module} for the $\mathcal N$-nodes of the true path.

:::lemma{#lem-mp-one-side}
Let $\alpha = P \uh 3e$, and let $s^*$ be a stage larger than $|\alpha| + 1$ such that, for $s \geq s^*$, $\sigma_s \not<_L \alpha$ and no proper prefix of $\alpha$ acts at stage $s$. If $s^* \leq s < t$ are consecutive $\alpha$-expansionary stages, then $A_t \uh s = A_s \uh s$ or $B_t \uh s = B_s \uh s$.
:::

:::proof{of=lem-mp-one-side}
Let $u$ be a stage with $s \leq u < t$ at which some node $\gamma$ acts, so that $\sigma_u = \gamma^\frown \mathrm f$. We consider the position of $\gamma$ relative to $\alpha$.

- $\gamma$ is a proper prefix of $\alpha$, or $\gamma <_L \alpha$: excluded by the choice of $s^*$, since then $\sigma_u <_L \alpha$ in the second case.
- $\gamma = \alpha$: impossible, since $\mathcal N$-nodes do not act.
- $\alpha^\frown \infty \preceq \gamma$: then $\alpha$ is visited at $u$ with outcome $\infty$, so $u$ is $\alpha$-expansionary, and $u = s$.
- $\alpha^\frown \mathrm f \preceq \gamma$ or $\alpha <_L \gamma$: since $s$ is $\alpha$-expansionary, $\alpha^\frown \infty \preceq \sigma_s$, so $\sigma_s <_L \gamma$, and $\gamma$ is initialized at the end of stage $s$. In particular $u > s$, and the follower enumerated by $\gamma$ was received after stage $s$; it is fresh, hence larger than $s$.

So the only number below $s$ that may be enumerated during the stages $s, \dots, t - 1$ is the follower of the node acting at stage $s$, if any. It enters $A$ or $B$, not both, and the other side does not change below $s$.
:::

:::lemma{#lem-mp-negative}
Every requirement $\mathcal N_e$ is met.
:::

:::proof{of=lem-mp-negative}
Let $\alpha = P \uh 3e$. By :ref{#lem-true-path}, the prefixes of $\alpha$ act finitely often, and $\sigma_s <_L \alpha$ for finitely many $s$; so a stage $s^*$ as in :ref{#lem-mp-one-side} exists, and $\alpha$ is not initialized after $s^*$. Suppose that $\Phi^A_e = \Phi^B_e$ is total. By :ref{#prop-agreement-unbounded}, applied to the infinite set of $\alpha$-stages after the last initialization of $\alpha$, there are infinitely many $\alpha$-expansionary stages. List those larger than $s^*$ as $s_0 < s_1 < \cdots$. The sequence is computable from $s^*$ and the record $m_\alpha$ at stage $s^*$, by running the construction. Condition 1 of :ref{#lem-pair-module} holds since the record increases, and condition 2 by :ref{#lem-mp-one-side}. By :ref{#cor-pair-module}, $\Phi^A_e$ is computable.
:::

:::proof{of=thm-minimal-pair}
The sets $A$ and $B$ are c.e. By :ref{#lem-mp-positive}, they are not computable, and $A$ is non-empty: for an index $e$ with $W_e = \nat$, the requirement $\mathcal R_e$ puts a number into $A$. Since $A \cap B = \emptyset$, we have $A \neq B$. By :ref{#lem-mp-negative} and :ref{#lem-posner}, every set computable in both $A$ and $B$ is computable.
:::

:::quiz[the main lemma]
In the proof of :ref{#lem-mp-one-side}, why can a node $\gamma$ extending $\alpha^\frown \mathrm f$ not enumerate a small number between two consecutive $\alpha$-expansionary stages?

- [x] Because it is initialized at the end of the first of them, which has outcome $\infty$, so its next follower is fresh, larger than that stage.
- [ ] Because it has lower priority than $\alpha$.

  Priority alone imposes nothing: $\mathcal N$-nodes impose no restraint. Initialization does the work.
- [ ] Because it is never visited.

  It is visited at the $\alpha$-stages with outcome $\mathrm f$, which may occur between expansionary stages.

---

Why does the stage end when a node acts?

- [x] So that at most one number enters $A \cup B$ at an $\alpha$-expansionary stage; two actions below $\alpha^\frown \infty$ at the same stage could change $A$ and $B$ simultaneously below $s$.
- [ ] To make the construction computable.

  The construction would be computable in any case.
- [ ] Because a node that acts initializes all the nodes below it.

  In this construction, initialization only concerns nodes to the right of the current path.
:::

## Exercises

::::exercise{difficulty=1}
Show that the true path is computable in $\emptyset''$.

:::solution
Given $P \uh n$, if it is an $\mathcal N$-node, then $P(n) = \infty$ if and only if $(P \uh n)^\frown \infty$ is visited at infinitely many stages. The set of stages at which a node $\beta$ is visited is computable, uniformly in $\beta$, so it is $W_{g(\beta)}$ for a computable function $g$. Hence $\beta$ is visited at infinitely many stages if and only if $g(\beta) \in \mathrm{Inf}$, which $\emptyset''$ decides (:ref{#prop-tot-double-jump}). If $P \uh n$ is another node, $P(n) = \mathrm f$. By induction on $n$, $\emptyset''$ computes $P$.
:::
::::

::::exercise{difficulty=2}
Modify the construction so that $A$ and $B$ are, in addition, simple sets.

:::solution
Put $0$ into $A$ at stage $0$, and replace $\mathcal R_e$ by the requirement "if $W_e$ is infinite, then $W_e \cap A \neq \emptyset$". An $\mathcal R_e$-node $\beta$, visited at stage $s$, acts if $W_{e,s} \cap A_s = \emptyset$ and there is $x \in W_{e,s}$ with $x > 2e$ and $x$ larger than the last stage at which $\beta$ was initialized: it enumerates the least such $x$ into $A$, and the stage ends. Treat $\mathcal S_e$ in the same way for $B$, with numbers $x > 2e$ and $x > 0$, so that $0 \in A \setminus B$ and $A \neq B$.

The numbers enumerated by a node $\gamma$ to the right of the current path at the end of stage $s$ are larger than $s$ at any later action, so :ref{#lem-mp-one-side} still holds, with the same proof; :ref{#lem-mp-negative} and :ref{#lem-posner} then give the minimal pair property. If $W_e$ is infinite, the $\mathcal R_e$-node $\beta$ on the true path, after its last initialization at stage $s_0$, eventually sees an element of $W_e$ larger than $2e$ and $s_0$, and acts at the next $\beta$-stage unless $W_e \cap A \neq \emptyset$ already. Finally, once some element of $W_e$ is in $A$, no $\mathcal R_e$-node acts again, so each $e$ contributes at most one element to $A$, and that element is larger than $2e$. Hence $A \cap \{0, \dots, 2n\}$ has at most $n + 1$ elements, and $\overline A$ is infinite. The same holds for $B$.
:::
::::

## Notes and references

The tree method was made explicit by Lachlan in the 1970s, and became the standard presentation of infinite injury arguments with Soare's book; earlier proofs organized the same guesses implicitly, through the stages at which restraints are recomputed. Lempp's lecture notes describe the hierarchy of priority arguments: finite injury arguments are $\mathbf 0'$-arguments, since $\emptyset'$ can follow them, the tree arguments of this course are $\mathbf 0''$-arguments, since the true path is computable in $\emptyset''$, and $\mathbf 0'''$-arguments use trees of strategies with more complex interactions.

- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapters IX and XIV.
- S. Lempp, *Priority arguments in computability theory, model theory, and complexity theory*, lecture notes, University of Wisconsin, 2012.
