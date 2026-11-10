---
title: Minimal pairs and the preservation of agreement
summary: Minimal pairs of degrees; Posner's trick, which reduces the meet requirements to one functional; expansionary stages and the lemma that agreement is preserved when only one side changes between them; why the resulting strategy causes infinite injury.
duration: 35
prerequisites: [ce-degrees/sacks-splitting]
---

The Friedberg–Muchnik theorem gives two c.e. degrees that are incomparable. The **minimal pair theorem** of Lachlan and Yates gives two non-computable c.e. degrees whose only common lower bound is $\obf$. Each requirement of this construction asks that a set computed by both $A$ and $B$ be computable, and its natural strategy acts infinitely often when the hypothesis of the requirement holds. A requirement of lower priority may then be injured infinitely often: this is the **infinite injury** method. This lesson isolates the strategy for one requirement and proves its main lemma. The next lesson combines the strategies on a tree.

## Minimal pairs

:::definition{#def-minimal-pair}
Two degrees $\abf, \bbf > \obf$ form a **minimal pair** if every degree $\cbf$ with $\cbf \leq \abf$ and $\cbf \leq \bbf$ is $\obf$. Equivalently, every set computable both in a set of degree $\abf$ and in a set of degree $\bbf$ is computable.
:::

By Spector's theorem on exact pairs, the Turing degrees do not form a lattice, but the two degrees of a minimal pair have a meet, namely $\obf$. The difficulty of the theorem below is that both degrees must be c.e.

:::theorem[Lachlan, Yates]{#thm-minimal-pair}
There are c.e. sets $A$ and $B$ whose degrees form a minimal pair.
:::

The proof occupies this lesson and the next. The requirements are
$$
\mathcal R_e : W_e \neq \overline A, \qquad \mathcal S_e : W_e \neq \overline B, \qquad \mathcal N_e : \Phi^A_e = \Phi^B_e \text{ total} \implies \Phi^A_e \text{ computable}.
$$
The requirements $\mathcal R_e$ and $\mathcal S_e$ make $A$ and $B$ non-computable, as in the construction of a simple set: $\overline A$ is not c.e. The requirements $\mathcal N_e$ concern a single index $e$ for both oracles. The reason this suffices is the following observation.

:::lemma[Posner]{#lem-posner}
Let $A$ and $B$ be sets with $A \neq B$. Suppose that every requirement $\mathcal N_e$ holds. Then every set $C$ with $C \leq_T A$ and $C \leq_T B$ is computable.
:::

:::proof{of=lem-posner}
Let $C = \Phi^A_i = \Phi^B_j$, and fix $n$ with $A(n) \neq B(n)$. There is an index $e$ such that, for every oracle $X$ and every $y$, the machine $\Phi^X_e$ on input $y$ reads $X(n)$, then simulates $\Phi^X_i(y)$ if $X(n) = A(n)$, and $\Phi^X_j(y)$ otherwise. Since $B(n) \neq A(n)$, we have $\Phi^A_e = \Phi^A_i = C$ and $\Phi^B_e = \Phi^B_j = C$. So $\Phi^A_e = \Phi^B_e$ is total, and $\mathcal N_e$ shows that $C$ is computable.
:::

The index $e$ depends on $n$, $A(n)$, $i$ and $j$, and is not computed by the construction; it only serves in the verification. In the construction of :ref{#thm-minimal-pair}, $A$ and $B$ will be disjoint and $A$ non-empty, so $A \neq B$.

## Length of agreement and expansionary stages

Fix c.e. approximations $(A_s)$ and $(B_s)$. Recall that $\Phi^{A_s}_e(y)[s]\converge$ implies that the use of the computation is at most $s$, so that the computation depends only on $A_s \uh s$.

:::definition{#def-expansionary}
1. The **length of agreement** at stage $s$ is the largest $l(e, s) \leq s$ such that, for every $y < l(e, s)$, both $\Phi^{A_s}_e(y)[s]$ and $\Phi^{B_s}_e(y)[s]$ converge, with the same value.
2. Given a set $Q$ of stages, a stage $s \in Q$ is **expansionary** for $Q$ if $l(e, s) > l(e, t)$ for every expansionary stage $t \in Q$ with $t < s$.
:::

The set $Q$ is the set of stages at which the strategy for $\mathcal N_e$ is run; in the tree construction, it is the set of stages at which a node is visited. The first stage of $Q$ is expansionary.

:::proposition{#prop-agreement-unbounded}
If $\Phi^A_e = \Phi^B_e$ is total, then $\lim_s l(e, s) = \infty$. In particular, every infinite set of stages $Q$ has infinitely many expansionary stages.
:::

:::proof{of=prop-agreement-unbounded}
Let $n \in \nat$. For $y < n$, the computations $\Phi^A_e(y)$ and $\Phi^B_e(y)$ converge, with the same value, with uses $u_y$ and $v_y$. Let $s_0 \geq n$ be a stage at which all these computations converge, and after which $A$ and $B$ no longer change below $\max_{y < n} \max(u_y, v_y)$. For $s \geq s_0$, by :ref{#prop-oracle-stages} and the use principle, $\Phi^{A_s}_e(y)[s]$ and $\Phi^{B_s}_e(y)[s]$ converge to the true values for $y < n$, so $l(e, s) \geq n$. Now let $Q$ be infinite. The lengths of agreement at the expansionary stages increase. If $t$ is the last expansionary stage found so far, the least $s \in Q$ with $s > t$ and $l(e, s) > l(e, t)$ exists, and it is expansionary, since every expansionary stage before $s$ is at most $t$ and has a length of agreement at most $l(e, t)$. So there is always a next expansionary stage.
:::

The converse fails: $l(e, s)$ may be unbounded while $\Phi^A_e$ is partial, because agreements found at some stages can be destroyed later. The strategy will not try to decide which case holds.

## The preservation lemma

The natural strategy for $\mathcal N_e$ would restrain both $A$ and $B$ below the uses of the agreeing computations at expansionary stages. If $\Phi^A_e = \Phi^B_e$ is total, this restraint goes to infinity, and no element could ever enter $A$ or $B$ below it: the requirements $\mathcal R_d$ and $\mathcal S_d$ of lower priority would fail. The key observation is that it suffices to forbid simultaneous changes on both sides.

:::lemma[Preservation of agreement]{#lem-pair-module}
Let $s_0 < s_1 < s_2 < \cdots$ be an infinite computable sequence of stages such that, for every $k$:

1. $l(e, s_{k+1}) > l(e, s_k)$;
2. $A_{s_{k+1}} \uh s_k = A_{s_k} \uh s_k$ or $B_{s_{k+1}} \uh s_k = B_{s_k} \uh s_k$.

Define $\Delta(y) = \Phi^{A_{s_k}}_e(y)[s_k]$, where $k$ is least with $l(e, s_k) > y$. Then $\Delta$ is a total computable function, and for every $y$:

- $\Phi^{A_{s_j}}_e(y)[s_j] = \Phi^{B_{s_j}}_e(y)[s_j] = \Delta(y)$ for every $j \geq k$;
- if $\Phi^A_e(y)$ converges, then $\Phi^A_e(y) = \Delta(y)$; if $\Phi^B_e(y)$ converges, then $\Phi^B_e(y) = \Delta(y)$.
:::

:::proof{of=lem-pair-module}
By condition 1, $l(e, s_k) \geq k$, so $k$ exists for every $y$. The sequence is computable and the computations are decidable, so $\Delta$ is total and computable.

We show by induction on $j$ that $\Phi^{A_{s_j}}_e(y)[s_j] = \Phi^{B_{s_j}}_e(y)[s_j] = \Delta(y)$ for every $y < l(e, s_j)$. Fix $y < l(e, s_j)$, and let $k \leq j$ be least with $l(e, s_k) > y$. If $k = j$, the value at $s_j$ on the $A$ side is $\Delta(y)$ by definition, and equals the value on the $B$ side since $y < l(e, s_j)$. If $k < j$, then $y < l(e, s_{j-1})$, so by the induction hypothesis both computations at stage $s_{j-1}$ converge with value $\Delta(y)$. By condition 2, one of the two sides, say $X \in \{ A, B \}$, satisfies $X_{s_j} \uh s_{j-1} = X_{s_{j-1}} \uh s_{j-1}$. The computation $\Phi^{X_{s_{j-1}}}_e(y)[s_{j-1}]$ has use at most $s_{j-1}$, so by monotonicity (:ref{#prop-oracle-stages}) the computation $\Phi^{X_{s_j}}_e(y)[s_j]$ converges with the same value $\Delta(y)$. Since $y < l(e, s_{j-1}) < l(e, s_j)$, the computation on the other side at stage $s_j$ converges with the same value. This proves the first item, since $y < l(e, s_j)$ for all $j \geq k$.

For the second item, suppose that $\Phi^A_e(y)$ converges, with use $u$. Take $j \geq k$ large enough that the computation has converged by stage $s_j$, that $s_j \geq u$, and that $A_{s_j} \uh u = A \uh u$. Then $\Phi^{A_{s_j}}_e(y)[s_j]$ is the true computation, with value $\Phi^A_e(y)$, and by the first item this value is $\Delta(y)$. The same argument applies to $B$.
:::

The proof is the following chain of equalities, for $y < l(e, s_{j-1})$ and $A$ the side that does not change:
$$
\Phi^{B_{s_{j-1}}}_e(y)[s_{j-1}] = \Phi^{A_{s_{j-1}}}_e(y)[s_{j-1}] = \Phi^{A_{s_j}}_e(y)[s_j] = \Phi^{B_{s_j}}_e(y)[s_j].
$$
The computation on the $B$ side may have been destroyed between $s_{j-1}$ and $s_j$, and replaced by a different computation with a different use, but its value is forced by the agreement at stage $s_j$, which is new information obtained because $s_j$ is expansionary. This is why condition 1 cannot be dropped.

:::corollary{#cor-pair-module}
If, in addition, $\Phi^A_e = \Phi^B_e$ is total, then it is computable: it equals $\Delta$.
:::

:::quiz[the preservation lemma]
In the proof of :ref{#lem-pair-module}, why does the value on the side that changed remain $\Delta(y)$?

- [x] Because $s_j$ is a stage with a larger length of agreement, so the computation on the changed side at $s_j$ agrees with the preserved computation on the other side.
- [ ] Because its use is preserved by a restraint.

  No restraint is imposed on that side; its computation may be replaced by another one.
- [ ] Because $A$ and $B$ are c.e.

  Enumeration of new elements is what can destroy the computation; it does not preserve it.

---

Why is condition 2 required at every pair of consecutive stages, and not only for the side that is restrained at the start?

- [x] Because the chain of equalities passes from one side to the other at each step: if both sides changed below $s_{j-1}$ between $s_{j-1}$ and $s_j$, both computations could change their values while still agreeing with each other.

  The new common value would then differ from $\Delta(y)$.
- [ ] Because otherwise $\Delta$ would not be computable.

  $\Delta$ is computable from the sequence alone; condition 2 ensures that it is the correct function.
- [ ] Because the length of agreement would decrease.

  Condition 1 is about the length of agreement; condition 2 is about the oracles.
:::

## The strategy and its two outcomes

The strategy for $\mathcal N_e$ is now the following: it is run at a set $Q$ of stages and computes the expansionary stages for $Q$. It enumerates nothing and imposes no explicit restraint. Instead, it constrains how the requirements below it act, so that condition 2 of :ref{#lem-pair-module} holds between consecutive expansionary stages. It has two possible **outcomes**:

- **$\infty$**: there are infinitely many expansionary stages;
- **$\mathrm f$**: there are finitely many expansionary stages. By :ref{#prop-agreement-unbounded}, $\Phi^A_e = \Phi^B_e$ is then not total, and $\mathcal N_e$ holds trivially, provided $Q$ is infinite.

Consider a requirement $\mathcal R_d$ of lower priority. It acts by enumerating a follower $x$ into $A$ once $x$ appears in $W_d$. Two strategies are possible.

1. *If the outcome of $\mathcal N_e$ is $\infty$:* act only at expansionary stages, immediately after $\mathcal N_e$ has found the new expansionary stage. Then an action changes $A$ at stage $s_k$, after the computations of stage $s_k$ have been examined; if at most one element enters $A \cup B$ below $s_k$ between $s_k$ and $s_{k+1}$, condition 2 holds. Since there are infinitely many expansionary stages, $\mathcal R_d$ gets infinitely many opportunities to act.
2. *If the outcome is $\mathrm f$:* act at any stage, after the last expansionary stage. The strategy of $\mathcal N_e$ imposes nothing after that stage. With strategy 1, $\mathcal R_d$ would wait forever.

The construction cannot know which outcome holds: the outcome $\infty$ is a $\Pi^0_2$ property. It runs both versions of $\mathcal R_d$, one guessing each outcome. The version guessing $\mathrm f$ is **initialized** at every expansionary stage, and chooses its followers larger than the last expansionary stage, so that its actions never destroy computations examined by $\mathcal N_e$ at that stage. If the outcome is $\infty$, this version is initialized infinitely often and may act infinitely often: it is injured infinitely often, which is harmless, since the other version meets $\mathcal R_d$.

The same splitting is needed for the requirements $\mathcal N_{e'}$ of lower priority, since the stages at which they are run, and thus their own expansionary stages, depend on the outcome of $\mathcal N_e$. Iterating the case distinction gives a **tree of strategies**, one level per requirement, and one branch for each guess about the outcomes of the requirements above. The next lesson defines it precisely.

:::quiz[guessing outcomes]
Why must the version of $\mathcal R_d$ guessing the outcome $\mathrm f$ choose followers larger than the last expansionary stage?

- [x] So that its enumerations between two expansionary stages are above the uses of the computations examined at the earlier one, and do not count against condition 2 of :ref{#lem-pair-module}.
- [ ] So that $\mathcal R_d$ is met.

  Any follower outside $A$ would meet $\mathcal R_d$ once enumerated or once it fails to appear in $W_d$; the size matters for $\mathcal N_e$.
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

## Exercises

::::exercise{difficulty=1}
Let $\abf$ and $\bbf$ be c.e. degrees forming a minimal pair. Show that $\abf$ and $\bbf$ are incomparable and that neither is $\mathbf 0'$. Deduce that the four-element Boolean algebra embeds into the c.e. degrees, preserving the least element, joins and meets.

:::solution
If $\abf \leq \bbf$, then $\abf$ is a common lower bound of $\abf$ and $\bbf$, so $\abf = \obf$, contradicting the definition. If $\abf = \mathbf 0'$, then $\bbf \leq \mathbf 0' = \abf$, since $\bbf$ is c.e., which was just excluded. The map sending the four elements to $\obf$, $\abf$, $\bbf$ and $\abf \vee \bbf$ is injective, since $\abf$ and $\bbf$ are incomparable and non-zero, and $\abf \vee \bbf$ is the degree of the c.e. set $A \oplus B$. It preserves the order and joins, and the meet of $\abf$ and $\bbf$ is $\obf$; the other meets are between comparable elements.
:::
::::

::::exercise{difficulty=2}
Replace condition 2 of :ref{#lem-pair-module} by the stronger condition $B_t \uh s_k = B_{s_k} \uh s_k$ for every $t \geq s_k$ and every $k$, which corresponds to a permanent restraint on $B$ at expansionary stages. Show that the conclusion of the lemma still holds, and that $B$ is then computable. Explain why this rules out a strategy for $\mathcal N_e$ that always restrains the same side.

:::solution
The stronger condition implies condition 2 with $X = B$, so the lemma applies. Since $l(e, s_k) \geq k$ and $l(e, s_k) \leq s_k$, the stages $s_k$ tend to infinity. For every $x$, choose $k$ with $s_k > x$; then $B(x) = B_{s_k}(x)$, since $B$ does not change below $s_k$ after stage $s_k$. The sequence $(s_k)$ is computable, so $B$ is computable. In the construction, if $\mathcal N_e$ has outcome $\infty$ and always restrains $B$, the requirements $\mathcal S_d$ of lower priority can only enumerate finitely many elements below each $s_k$, and in fact none after $s_k$; $B$ would be computable, so some $\mathcal S_d$ would fail. The outcome $\infty$ does occur, for instance for an index $e$ such that $\Phi^X_e$ is the constant function $0$ for every oracle $X$.
:::
::::

## Notes and references

Lachlan (1966) and Yates (1966) proved the minimal pair theorem independently. Posner's observation that one index suffices is reported by Soare. The formulation of the strategy by expansionary stages, and the preservation lemma :ref{#lem-pair-module}, in which only one side needs to be preserved at a time, follow Soare's book; Monin and Patey present an equivalent version in which the strategy restrains $A$ and $B$ alternately.

- A. H. Lachlan, *Lower bounds for pairs of recursively enumerable degrees*, Proceedings of the London Mathematical Society (3) 16 (1966), 537–569.
- C. E. M. Yates, *A minimal pair of recursively enumerable degrees*, Journal of Symbolic Logic 31 (1966), 159–168.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter IX.
