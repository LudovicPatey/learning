---
title: The true path and the verification
summary: The true path of a tree construction, whose nodes are visited infinitely often and initialized finitely often; the nodes on the true path meet their requirements; between two consecutive expansionary stages of an N-node on the true path, only one of the two sets changes below the first of them; end of the proof of the minimal pair theorem.
duration: 50
prerequisites: [trees-of-strategies]
---

The previous lesson built the c.e. sets $A$ and $B$ along a tree of strategies. This lesson defines the true path, the leftmost path visited infinitely often, and shows that its nodes are visited infinitely often and initialized finitely often. It then shows that the nodes on the true path meet their requirements.

For the positive requirements, this is a finite injury argument: after its last initialization, the $\mathcal R_e$-node on the true path behaves like a Friedberg–Muchnik strategy with a permanent follower. For the negative requirements, the infinite injury appears. Let $\alpha$ be the $\mathcal N_e$-node on the true path, and suppose that its outcome is $\infty$. Infinitely many nodes act between consecutive $\alpha$-expansionary stages, but the tree sorts them into three groups, shown in the figure of the main lemma. The nodes above $\alpha$ or to its left stop acting after some stage. The nodes to the right of $\alpha^\frown \infty$ are initialized at every $\alpha$-expansionary stage, so their later followers are larger than that stage. The nodes below $\alpha^\frown \infty$ act only at $\alpha$-expansionary stages, after $\alpha$ has examined its computations, and a stage ends as soon as one node acts. Hence at most one number below an $\alpha$-expansionary stage $s$ enters $A \cup B$ before the next one: this is condition 2 of the preservation lemma (:ref{#lem-pair-module}).

## The true path

:::definition{#def-true-path}
The **true path** is the infinite sequence $P \in \Lambda^\nat$ defined by induction: $P(n)$ is the least $o \in \Lambda$ such that $(P \uh n)^\frown o$ is visited at infinitely many stages.
:::

:::example{#ex-true-path}
Suppose that the root has infinitely many expansionary stages, and infinitely many stages that are not expansionary. This happens, for instance, if $\Phi^X_0(y) = 0$ for every $X$ and $y$, by a computation that does not query the oracle and takes more than $2^y$ steps: then $l(0, s)$ is non-decreasing and unbounded, but increases only at sparse stages (compare :ref{#ex-expansionary}). The current path begins with $\infty$ at the expansionary stages and with $\mathrm f$ at the others. Both nodes of length $1$, the $\mathcal R_0$-nodes $\langle \infty \rangle$ and $\langle \mathrm f \rangle$, are visited infinitely often, and $P(0) = \infty$.

- No node is to the left of $\langle \infty \rangle$, so it is never initialized. It receives a follower at its first visit, keeps it, and acts at most once.
- At the end of every expansionary stage, $\sigma_s <_L \langle \mathrm f \rangle$, so $\langle \mathrm f \rangle$ and all its extensions are initialized. Between two expansionary stages, $\langle \mathrm f \rangle$ receives a new follower and may enumerate it, for instance if $W_0 = \nat$: this node can act infinitely often, each time with a fresh follower.

The guess of $\langle \mathrm f \rangle$ is wrong, and its infinitely many actions do not matter, since $\mathcal R_0$ is met by $\langle \infty \rangle$. The lemma below shows that this is the general situation.
:::

:::lemma{#lem-true-path}
For every $n$, the true path is defined at $n$, and the node $\alpha = P \uh n$ satisfies:

1. $\alpha$ is visited at infinitely many stages;
2. $\sigma_s <_L \alpha$ holds for only finitely many $s$; in particular $\alpha$ is initialized only finitely often;
3. if $\alpha$ is an $\mathcal R$- or $\mathcal S$-node, it acts only finitely often.
:::

:::proof{of=lem-true-path}
By induction on $n$. The root is visited at every stage $s \geq 1$, and no path is to its left.

Suppose that $\alpha = P \uh n$ satisfies items 1 and 2. The node $\alpha$ is initialized only at the end of a stage $s$ with $\sigma_s <_L \alpha$, so it is initialized finitely often. If $\alpha$ is an $\mathcal R$- or $\mathcal S$-node, then between two initializations it acts at most once, since it is then marked satisfied; this gives item 3. Let $s_0$ be a stage after which $\alpha$ never acts, nor is initialized, nor satisfies $\sigma_s <_L \alpha$.

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

  The priority order is not well-founded: each of the nodes $\mathrm f$, $\infty\mathrm{fff}$, $\infty\mathrm{ff}\infty\mathrm{fff}$, … has lower priority than the next one.
:::

## The positive requirements

:::lemma{#lem-mp-positive}
Every requirement $\mathcal R_e$ and $\mathcal S_e$ is met.
:::

:::proof{of=lem-mp-positive}
Let $\beta = P \uh (3e + 1)$, the $\mathcal R_e$-node on the true path. By :ref{#lem-true-path}, $\beta$ is initialized finitely often and visited infinitely often. At its first visit after its last initialization, it receives a follower $x$, which it keeps forever. If $x \in W_e$, at the first $\beta$-stage $s$ with $x \in W_{e,s}$, $\beta$ is not yet marked satisfied, so it acts, and $x \in A \cap W_e$. If $x \notin W_e$, then $\beta$ never enumerates $x$, no other node does, and $x \in \overline A \setminus W_e$. In both cases $W_e \neq \overline A$. The argument for $\mathcal S_e$ is the same.
:::


## The main lemma

The main lemma checks condition 2 of :ref{#lem-pair-module} for the $\mathcal N$-nodes of the true path. Its proof is a case analysis on the position of the acting node relative to $\alpha$, along the three groups described above.

:::figure[The nodes of the tree seen from an $\mathcal N$-node $\alpha$ on the true path, between two consecutive $\alpha$-expansionary stages after the stage $s^*$ of :ref{#lem-mp-one-side}. Only a node below $\alpha^\frown \infty$ can enumerate a number below the first of the two stages, and only at that stage.]
<svg class="fig" viewBox="0 0 600 315" width="600" role="img" aria-label="The node alpha on the true path, its prefixes, the subtrees below its two outcomes, and the nodes to its left and to its right, with what each group can do between two consecutive alpha-expansionary stages"><polygon points="288,36 286,116 182,252 30,252" class="cell" stroke-dasharray="3 3"/><polygon points="312,36 314,116 418,252 570,252" class="cell" stroke-dasharray="3 3"/><polygon points="240,168 188,252 292,252" class="soft-fill"/><polygon points="360,168 308,252 412,252" class="cell"/><line x1="300" y1="36" x2="300" y2="112" class="accent-stroke" stroke-width="2.4"/><circle cx="300" cy="36" r="5" class="accent-fill"/><circle cx="300" cy="74" r="5" class="accent-fill"/><line x1="300" y1="118" x2="240" y2="154" class="ink-stroke" stroke-width="1.4"/><text x="254" y="136" class="mrm" font-size="14">∞</text><circle cx="240" cy="160" r="6" class="node"/><line x1="300" y1="118" x2="360" y2="154" class="ink-stroke" stroke-width="1.4"/><text x="338" y="136" class="math" font-size="14">f</text><circle cx="360" cy="160" r="6" class="node"/><circle cx="300" cy="112" r="7" class="accent-fill"/><text x="314" y="114" class="math" font-size="16">α</text><text x="300" y="16" text-anchor="middle" class="label">prefixes of α: no action after s*</text><text x="110" y="212" text-anchor="middle" class="label">left of α: not</text><text x="110" y="227" text-anchor="middle" class="label">visited after s*</text><text x="490" y="212" text-anchor="middle" class="label">right of α: initialized</text><text x="490" y="227" text-anchor="middle" class="label">at each α-exp. stage</text><text x="240" y="274" text-anchor="middle" class="label">below α⁀∞: act only</text><text x="240" y="289" text-anchor="middle" class="label">at α-exp. stages</text><text x="360" y="274" text-anchor="middle" class="label">below α⁀f: initialized</text><text x="360" y="289" text-anchor="middle" class="label">at each α-exp. stage</text></svg>
:::

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

## The negative requirements

:::lemma{#lem-mp-negative}
Every requirement $\mathcal N_e$ is met.
:::

:::proof{of=lem-mp-negative}
Let $\alpha = P \uh 3e$. By :ref{#lem-true-path}, the prefixes of $\alpha$ act finitely often, and $\sigma_s <_L \alpha$ for finitely many $s$; so a stage $s^*$ as in :ref{#lem-mp-one-side} exists, and $\alpha$ is not initialized after $s^*$. Suppose that $\Phi^A_e = \Phi^B_e$ is total. By :ref{#prop-agreement-unbounded}, applied to the infinite set of $\alpha$-stages after the last initialization of $\alpha$, there are infinitely many $\alpha$-expansionary stages. List those larger than $s^*$ as $s_0 < s_1 < \cdots$. The sequence is computable: run the construction and list the $\alpha$-expansionary stages after $s^*$. Condition 1 of :ref{#lem-pair-module} holds since the record increases, and condition 2 by :ref{#lem-mp-one-side}. By :ref{#cor-pair-module}, $\Phi^A_e$ is computable.
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

---

In the proof of :ref{#lem-mp-negative}, why is the $\mathcal N_e$-node on the true path used, and not an arbitrary $\mathcal N_e$-node visited infinitely often?

- [x] Because a node to the right of the true path may be initialized infinitely often, and nodes to its left, among them nodes of the true path, may act between its expansionary stages with small followers: no stage $s^*$ as in :ref{#lem-mp-one-side} exists for it.
- [ ] Because the other $\mathcal N_e$-nodes compute a different length of agreement.

  All $\mathcal N_e$-nodes compute the same $l(e, s)$; they differ in the stages at which they are visited and in their records.
- [ ] Because only the node on the true path has infinitely many expansionary stages.

  A node initialized infinitely often and visited infinitely often has infinitely many expansionary stages, since its first visit after each initialization is expansionary.
:::

## Exercises

::::exercise{difficulty=1 #ex-true-path-double-jump}
Show that the true path is computable in $\emptyset''$.

:::solution
Given $P \uh n$, if it is an $\mathcal N$-node, then $P(n) = \infty$ if and only if $(P \uh n)^\frown \infty$ is visited at infinitely many stages. The set of stages at which a node $\beta$ is visited is computable, uniformly in $\beta$, so it is $W_{g(\beta)}$ for a computable function $g$. Hence $\beta$ is visited at infinitely many stages if and only if $g(\beta) \in \mathrm{Inf}$, which $\emptyset''$ decides (:ref{#prop-tot-double-jump}). If $P \uh n$ is another node, $P(n) = \mathrm f$. By induction on $n$, $\emptyset''$ computes $P$.
:::
::::

::::exercise{difficulty=2}
Modify the construction so that $A$ and $B$ are, in addition, simple sets.

:::solution
Put $0$ into $A$ at stage $0$, and replace $\mathcal R_e$ by the requirement "if $W_e$ is infinite, then $W_e \cap A \neq \emptyset$". An $\mathcal R_e$-node $\beta$, visited at stage $s$, acts if $W_{e,s} \cap A_s = \emptyset$ and there is $x \in W_{e,s}$ with $x > 2e$ and $x$ larger than the last stage at which $\beta$ was initialized: it enumerates the least such $x$ into $A$, and the stage ends. Treat $\mathcal S_e$ in the same way for $B$, with numbers $x > 2e$ and $x > 0$, so that $0 \in A \setminus B$ and $A \neq B$.

A node $\gamma$ initialized at the end of stage $s$ only enumerates numbers larger than $s$ at its later actions, so :ref{#lem-mp-one-side} still holds, with the same proof; :ref{#lem-mp-negative} and :ref{#lem-posner} then give the minimal pair property. If $W_e$ is infinite, the $\mathcal R_e$-node $\beta$ on the true path, after its last initialization at stage $s_0$, eventually sees an element of $W_e$ larger than $2e$ and $s_0$, and acts at the next $\beta$-stage unless $W_e \cap A \neq \emptyset$ already. Finally, once some element of $W_e$ is in $A$, no $\mathcal R_e$-node acts again, so each $e$ contributes at most one element to $A$, and that element is larger than $2e$. Hence $A \cap \{0, \dots, 2n\}$ has at most $n + 1$ elements, and $\overline A$ is infinite. The same holds for $B$.
:::
::::

## Notes and references

The verification follows the proof of the minimal pair theorem of Downey and Hirschfeldt (their Lemmas 2.14.4 and 2.14.5), with the preservation lemma :ref{#lem-pair-module} isolated as a statement about a sequence of stages. A case analysis on the position of the acting node with respect to the node under consideration, as in the proof of :ref{#lem-mp-one-side}, is the typical verification step of tree arguments; the verification of the high incomplete construction uses it again (:ref{#lem-hi-preservation}).

- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.14.2.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter IX.
