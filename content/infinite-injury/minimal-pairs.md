---
title: Minimal pairs and the preservation of agreement
summary: Minimal pairs of degrees; Posner's trick, which reduces the meet requirements to one functional; length of agreement and expansionary stages; the lemma that agreement is preserved when only one side changes between consecutive expansionary stages.
duration: 45
prerequisites: [ce-degrees/sacks-splitting]
---

The Friedberg–Muchnik theorem gives two c.e. degrees that are incomparable. The **minimal pair theorem** of Lachlan and Yates gives two non-computable c.e. degrees whose only common lower bound is $\obf$. Each requirement of this construction asks that a set computed by both $A$ and $B$ be computable, and its natural strategy acts infinitely often when the hypothesis of the requirement holds. A requirement of lower priority may then be injured infinitely often: this is the **infinite injury** method. This lesson proves the main lemma on which the strategy for one requirement rests. The next lesson describes the strategy, explains why the strategies of lower priority must guess its outcome, and organizes these guesses on a tree of strategies; the third one defines the true path and verifies the construction.

The construction reuses the tools of finite injury arguments: requirements ordered by priority, fresh followers and initialization, as in the Friedberg–Muchnik theorem (:ref{#thm-friedberg-muchnik}), and the length of agreement of Sacks' preservation strategy (:ref{#def-length-agreement}). What changes is that a strategy may act, or constrain the others, at infinitely many stages.

## Minimal pairs

:::definition{#def-minimal-pair}
Two degrees $\abf, \bbf > \obf$ form a **minimal pair** if every degree $\cbf$ with $\cbf \leq \abf$ and $\cbf \leq \bbf$ is $\obf$. Equivalently, every set computable both in a set of degree $\abf$ and in a set of degree $\bbf$ is computable.
:::

The Turing degrees do not form a lattice, as the course on the structure of the Turing degrees shows (:ref{#cor-not-lattice}), but the two degrees of a minimal pair have a meet, namely $\obf$. The difficulty of the theorem below is that both degrees must be c.e.

:::theorem[Lachlan, Yates]{#thm-minimal-pair}
There are c.e. sets $A$ and $B$ whose degrees form a minimal pair.
:::

The proof occupies this lesson and the next. The requirements are
$$
\begin{gathered}
\mathcal R_e : W_e \neq \overline A, \qquad \mathcal S_e : W_e \neq \overline B, \\
\mathcal N_e : \Phi^A_e = \Phi^B_e \text{ total} \implies \Phi^A_e \text{ computable}.
\end{gathered}
$$
The requirements $\mathcal R_e$ and $\mathcal S_e$ make $A$ and $B$ non-computable, as in the construction of a simple set: $\overline A$ is not c.e. The requirements $\mathcal N_e$ concern a single index $e$ for both oracles. The reason this suffices is the following observation.

:::lemma[Posner]{#lem-posner}
Let $A$ and $B$ be sets with $A \neq B$. Suppose that every requirement $\mathcal N_e$ holds. Then every set $C$ with $C \leq_T A$ and $C \leq_T B$ is computable.
:::

:::proof{of=lem-posner}
Let $C = \Phi^A_i = \Phi^B_j$, and fix $n$ with $A(n) \neq B(n)$. There is an index $e$ such that, for every oracle $X$ and every $y$, the machine $\Phi^X_e$ on input $y$ reads $X(n)$, then simulates $\Phi^X_i(y)$ if $X(n) = A(n)$, and $\Phi^X_j(y)$ otherwise. Since $B(n) \neq A(n)$, we have $\Phi^A_e = \Phi^A_i = C$ and $\Phi^B_e = \Phi^B_j = C$. So $\Phi^A_e = \Phi^B_e$ is total, and $\mathcal N_e$ shows that $C$ is computable.
:::

The index $e$ depends on $n$, $A(n)$, $i$ and $j$, and is not computed by the construction; it only serves in the verification. In the construction of :ref{#thm-minimal-pair}, $A$ and $B$ will be disjoint and $A$ non-empty, so $A \neq B$.

The hypothesis $A \neq B$ is used to find $n$, but the conclusion of the lemma also holds when $A = B$: every set $C \leq_T A$ is then of the form $\Phi^A_e = \Phi^B_e$ with both sides total, and $\mathcal N_e$ shows that $C$ is computable. What the trick provides is a single index that works for both oracles at once, so that the construction only has to consider one functional per requirement.

## Length of agreement and expansionary stages

Fix c.e. approximations $(A_s)$ and $(B_s)$. Recall that $\Phi^{A_s}_e(y)[s]\converge$ implies that the use of the computation is at most $s$, so that the computation depends only on $A_s \uh s$.

:::definition{#def-expansionary}
1. The **length of agreement** at stage $s$ is the largest $l(e, s) \leq s$ such that, for every $y < l(e, s)$, both $\Phi^{A_s}_e(y)[s]$ and $\Phi^{B_s}_e(y)[s]$ converge, with the same value.
2. Given a set $Q$ of stages, a stage $s \in Q$ is **expansionary** for $Q$ if $l(e, s) > l(e, t)$ for every expansionary stage $t \in Q$ with $t < s$.
:::

The set $Q$ is the set of stages at which the strategy for $\mathcal N_e$ is run; in the tree construction, it is the set of stages at which a node is visited. The first stage of $Q$ is expansionary.

:::example{#ex-expansionary}
Suppose that $A$ and $B$ are disjoint and that some number $a$ belongs to $A$, as in the construction below.

1. Let $e$ be an index such that $\Phi^X_e(y) = X(y)$ for every oracle $X$ and every $y$. From the stage at which $a$ enters $A$ on, $A_s(a) = 1 \neq 0 = B_s(a)$, so $l(e, s) \leq a$. The expansionary stages after that stage have strictly increasing lengths of agreement, all at most $a$, so there are at most $a + 1$ of them. Whatever $Q$ is, there are finitely many expansionary stages.
2. Let $e$ be an index such that $\Phi^X_e(y) = 0$ for every $X$ and $y$, by a computation that does not query the oracle. Then $\Phi^A_e = \Phi^B_e$ is total, and by :ref{#prop-agreement-unbounded} below, every infinite $Q$ has infinitely many expansionary stages, whatever $A$ and $B$ are.

In the first case $\mathcal N_e$ holds because the hypothesis fails; in the second, it holds because the common function is computable, and the strategy must nevertheless deal with infinitely many expansionary stages.
:::

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

:::figure[The proof of :ref{#lem-pair-module}. At each stage $s_k$ of the sequence, the computations on the two sides agree below the length of agreement. Between $s_k$ and $s_{k+1}$, one side is unchanged below $s_k$, so its computations at $s_k$ survive until $s_{k+1}$, where the agreement transfers their values to the other side. The value $\Delta(y)$ follows the highlighted zigzag path. Which side is preserved may change from one interval to the next.]
<svg class="fig" viewBox="0 0 590 230" width="590" role="img" aria-label="Four expansionary stages; at each of them the computations on the A side and on the B side agree; between two consecutive stages one side is unchanged below the earlier stage, and the common value is carried along a zigzag path"><defs><marker id="ii-agr-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><text x="30" y="55" class="label">A side</text><text x="30" y="130" class="label">B side</text><line x1="119" y1="50" x2="221" y2="50" class="accent-stroke" stroke-width="2.4" marker-end="url(#ii-agr-arrow)"/><line x1="119" y1="125" x2="221" y2="125" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 4"/><line x1="239" y1="50" x2="341" y2="50" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 4"/><line x1="239" y1="125" x2="341" y2="125" class="accent-stroke" stroke-width="2.4" marker-end="url(#ii-agr-arrow)"/><line x1="359" y1="50" x2="461" y2="50" class="accent-stroke" stroke-width="2.4" marker-end="url(#ii-agr-arrow)"/><line x1="359" y1="125" x2="461" y2="125" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 4"/><line x1="108" y1="59" x2="108" y2="116" class="accent-stroke" stroke-width="1.6"/><line x1="112" y1="59" x2="112" y2="116" class="accent-stroke" stroke-width="1.6"/><circle cx="110" cy="50" r="6" class="node"/><circle cx="110" cy="125" r="6" class="node"/><text x="110" y="159" text-anchor="middle" class="math" font-size="15">s<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="110" y1="137" x2="110" y2="143" class="axis"/><line x1="228" y1="59" x2="228" y2="116" class="accent-stroke" stroke-width="1.6"/><line x1="232" y1="59" x2="232" y2="116" class="accent-stroke" stroke-width="1.6"/><circle cx="230" cy="50" r="6" class="node"/><circle cx="230" cy="125" r="6" class="node"/><text x="230" y="159" text-anchor="middle" class="math" font-size="15">s<tspan class="mrm" font-size="10" dy="4">1</tspan></text><line x1="230" y1="137" x2="230" y2="143" class="axis"/><line x1="348" y1="59" x2="348" y2="116" class="accent-stroke" stroke-width="1.6"/><line x1="352" y1="59" x2="352" y2="116" class="accent-stroke" stroke-width="1.6"/><circle cx="350" cy="50" r="6" class="node"/><circle cx="350" cy="125" r="6" class="node"/><text x="350" y="159" text-anchor="middle" class="math" font-size="15">s<tspan class="mrm" font-size="10" dy="4">2</tspan></text><line x1="350" y1="137" x2="350" y2="143" class="axis"/><line x1="468" y1="59" x2="468" y2="116" class="accent-stroke" stroke-width="1.6"/><line x1="472" y1="59" x2="472" y2="116" class="accent-stroke" stroke-width="1.6"/><circle cx="470" cy="50" r="6" class="node"/><circle cx="470" cy="125" r="6" class="node"/><text x="470" y="159" text-anchor="middle" class="math" font-size="15">s<tspan class="mrm" font-size="10" dy="4">3</tspan></text><line x1="470" y1="137" x2="470" y2="143" class="axis"/><line x1="80" y1="140" x2="510" y2="140" class="axis"/><text x="516" y="144" class="label">stages</text><line x1="40" y1="191" x2="80" y2="191" class="accent-stroke" stroke-width="2.4"/><text x="88" y="195" class="label">unchanged below the earlier stage</text><line x1="310" y1="191" x2="350" y2="191" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 4"/><text x="358" y="195" class="label">may change</text><line x1="38" y1="213" x2="38" y2="227" class="accent-stroke" stroke-width="1.6"/><line x1="42" y1="213" x2="42" y2="227" class="accent-stroke" stroke-width="1.6"/><text x="52" y="224" class="label">agreement at an expansionary stage</text></svg>
:::

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

Why must condition 2 hold between every two consecutive stages of the sequence, and not only between some of them?

- [x] Because the chain of equalities passes from one side to the other at each step: if both sides changed below $s_{j-1}$ between $s_{j-1}$ and $s_j$, both computations could change their values while still agreeing with each other.

  The new common value would then differ from $\Delta(y)$.
- [ ] Because otherwise $\Delta$ would not be computable.

  $\Delta$ is computable from the sequence alone; condition 2 ensures that it is the correct function.
- [ ] Because the length of agreement would decrease.

  Condition 1 is about the length of agreement; condition 2 is about the oracles.
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
The stronger condition implies condition 2 with $X = B$, so the lemma applies. Since $l(e, s_k) \geq k$ and $l(e, s_k) \leq s_k$, the stages $s_k$ tend to infinity. For every $x$, choose $k$ with $s_k > x$; then $B(x) = B_{s_k}(x)$, since $B$ does not change below $s_k$ after stage $s_k$. The sequence $(s_k)$ is computable, so $B$ is computable. In the construction, if $\mathcal N_e$ has infinitely many expansionary stages and always restrains $B$, no requirement $\mathcal S_d$ of lower priority could enumerate a number below $s_k$ after stage $s_k$; $B$ would be computable, so some $\mathcal S_d$ would fail. This case does occur, for instance for an index $e$ such that $\Phi^X_e$ is the constant function $0$ for every oracle $X$.
:::
::::

## Notes and references

Lachlan (1966) and Yates (1966) proved the minimal pair theorem independently. The observation that one index suffices is known as Posner's trick (Downey–Hirschfeldt, §2.14.2). Monin and Patey, and the informal description of Downey and Hirschfeldt, present the strategy with explicit restraints placed alternately on $A$ and on $B$ at consecutive expansionary stages. The formulation adopted here, in which no restraint is imposed and the tree only ensures that one side changes between consecutive expansionary stages, is the one used in the verification of Downey and Hirschfeldt (proof of their Lemma 2.14.5); the preservation lemma :ref{#lem-pair-module} isolates it as a statement about a sequence of stages.

- A. H. Lachlan, *Lower bounds for pairs of recursively enumerable degrees*, Proceedings of the London Mathematical Society (3) 16 (1966), 537–569.
- C. E. M. Yates, *A minimal pair of recursively enumerable degrees*, Journal of Symbolic Logic 31 (1966), 159–168.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987, Chapter IX (the minimal pair theorem is Theorem IX.1.2).
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.14.2.
- B. Monin and L. Patey, *Computability theory*, chapter *Priority method and c.e. degrees*, section *$\Pi^0_2$ priority method (infinite injury)*.
