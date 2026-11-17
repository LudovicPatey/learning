---
title: Minimal pairs and the preservation of agreement
summary: Minimal pairs of degrees; Posner's trick, which reduces the meet requirements to one functional; length of agreement and expansionary stages; the lemma that agreement is preserved when only one side changes between consecutive expansionary stages.
duration: 35
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

::::exercise{#ex-mp-one-side-restraint difficulty=2 objective="See why a strategy for $\mathcal N_e$ that always restrains the same side makes that side computable."}
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

:::::exercises
::::exercise{#ex-mp-boolean-algebra difficulty=1 objective="Derive from the definition of a minimal pair that the four-element Boolean algebra embeds into the c.e. degrees."}
Let $\abf$ and $\bbf$ be c.e. degrees forming a minimal pair. Show that $\abf$ and $\bbf$ are incomparable and that neither is $\mathbf 0'$. Deduce that the four-element Boolean algebra embeds into the c.e. degrees, preserving the least element, joins and meets.

:::solution
If $\abf \leq \bbf$, then $\abf$ is a common lower bound of $\abf$ and $\bbf$, so $\abf = \obf$, contradicting the definition. If $\abf = \mathbf 0'$, then $\bbf \leq \mathbf 0' = \abf$, since $\bbf$ is c.e., which was just excluded. The map sending the four elements to $\obf$, $\abf$, $\bbf$ and $\abf \vee \bbf$ is injective, since $\abf$ and $\bbf$ are incomparable and non-zero, and $\abf \vee \bbf$ is the degree of the c.e. set $A \oplus B$. It preserves the order and joins, and the meet of $\abf$ and $\bbf$ is $\obf$; the other meets are between comparable elements.
:::
::::

::::exercise{#ex-mp-expansionary-record difficulty=1 objective="Characterize the expansionary stages for a set $Q$ by a record condition, and compare the expansionary stages for two sets of stages."}
Fix $e$ and a set of stages $Q$, with the notation of :ref{#def-expansionary}.

1. Show that a stage $s \in Q$ is expansionary for $Q$ if and only if $l(e, s) > l(e, t)$ for every $t \in Q$ with $t < s$.
2. Deduce that if $Q \subseteq Q'$, every stage of $Q$ that is expansionary for $Q'$ is expansionary for $Q$.
3. Let $E$ be the set of expansionary stages for $Q$. Show that the expansionary stages for $E$ are exactly the elements of $E$, and that $E$ is computable if $Q$ is computable.

:::solution
1. If $l(e, s) > l(e, t)$ for every $t \in Q$ with $t < s$, this holds in particular for the expansionary stages $t < s$, so $s$ is expansionary. Conversely, let $s$ be expansionary, and $t \in Q$ with $t < s$. The least element of $Q$ is expansionary and at most $t$, so there is a largest expansionary stage $t' \leq t$. The lengths of agreement at the expansionary stages are strictly increasing, since each one exceeds those of the earlier ones. If $t = t'$, then $l(e, t) < l(e, s)$. Otherwise $t$ is not expansionary, so $l(e, t) \leq l(e, t'')$ for some expansionary stage $t'' < t$; then $t'' \leq t'$, and $l(e, t) \leq l(e, t'') \leq l(e, t') < l(e, s)$.
2. Let $s \in Q$ be expansionary for $Q'$. By item 1 applied to $Q'$, $l(e, s) > l(e, t)$ for every $t \in Q'$ with $t < s$, in particular for every $t \in Q$ with $t < s$. By item 1 applied to $Q$, $s$ is expansionary for $Q$.
3. An expansionary stage for $E$ belongs to $E$ by definition. Conversely, let $s \in E$. By item 1, $l(e, s) > l(e, t)$ for every $t \in Q$ with $t < s$, hence for every $t \in E$ with $t < s$, and by item 1 applied to $E$, $s$ is expansionary for $E$. If $Q$ is computable, item 1 decides whether $s \in E$: check whether $s \in Q$, and compare $l(e, s)$ with the finitely many values $l(e, t)$, $t \in Q$, $t < s$; the function $l$ is computable, since the computations $\Phi^{A_s}_e(y)[s]$ are decidable.
:::
::::

::::exercise{#ex-mp-agreement-converse difficulty=2 objective="Build an example in which the length of agreement is unbounded while the common function is partial."}
Let $\Psi = \Phi_e$ be the Turing functional such that $\Psi^X(0)$ queries $X(0), X(2), X(4), \dots$ in turn and outputs $0$ as soon as it finds some $k$ with $2k \notin X$, and $\Psi^X(y) = 0$ for $y \geq 1$, by a computation that does not query the oracle. Let $A = B = D$, where $D$ is enumerated as follows: $D_0 = \emptyset$, and if $D_s = \{ 0, 2, \dots, 2k - 2 \}$ and $l(e, s) > k$, then $D_{s+1} = D_s \cup \{ 2k \}$; otherwise $D_{s+1} = D_s$. Show that $D$ is the set of even numbers, that $\Psi^A = \Psi^B$ is not total, and that $l(e, s) > k$ for infinitely many $s$ and every $k$. Which statement of the lesson does this example illustrate?

:::solution
The enumeration is computable, since $l(e, s)$ is computed from $D_s$ and $s$, so $D$ is c.e., and $D_s$ is always of the form $\{ 0, 2, \dots, 2k - 2 \}$ with $k = |D_s|$.

We show that $D$ receives the number $2k$ for every $k$. Suppose that $D_s = \{ 0, 2, \dots, 2k - 2 \}$ from some stage $s_0$ on, for all $s \geq s_0$. With this oracle, $\Psi(0)$ finds $2k \notin D_{s_0}$ and halts; the computation queries only $X(0), X(2), \dots, X(2k)$, and the oracle does not change after $s_0$, so $\Psi^{D_s}(0)[s]$ converges for every large $s$. The computations $\Psi(y)$, $1 \leq y \leq k$, do not query the oracle and converge at every large stage. Since $A_s = B_s = D_s$, the two sides agree wherever they converge, so $l(e, s) > k$ for every large $s$ (recall that $l(e, s) \leq s$). Then $2k$ enters $D$ at the next stage, a contradiction. Hence $|D_s| \to \infty$, $D$ is the set of even numbers, and each $2k$ enters at the end of a stage $s$ with $l(e, s) > k$; these stages are distinct for distinct $k$, so for every $k$, infinitely many stages have $l(e, s) > k$.

With oracle $D$, the search of $\Psi^D(0)$ never ends, since every even number is in $D$. So $\Psi^A = \Psi^B$ is not total, while $\limsup_s l(e, s) = \infty$. This is the remark after :ref{#prop-agreement-unbounded}: the converse of the proposition fails, because agreements found at some stages can be destroyed later; here each new even number destroys the computation of $\Psi(0)$.
:::
::::

::::exercise{#ex-mp-pair-module-hypotheses difficulty=2 objective="Show by counterexamples that neither condition of the preservation lemma can be dropped."}
Let $A$ and $B$ be finite sets given with enumerations $(A_s)$ and $(B_s)$, which the exercise chooses. Show that the conclusion of :ref{#lem-pair-module} may fail in each of the following cases.

1. The sequence satisfies condition 1, but not condition 2.
2. The sequence satisfies condition 2, and the lengths $l(e, s_k)$ are unbounded but not increasing.

:::solution
In both cases we use a functional $\Phi_e$ whose computations on input $y$ query fixed oracle bits and take a number of steps that does not depend on the answers. There is then a least $n_y$ such that, for every oracle $X$, $\Phi^X_e(y)[s]$ converges if and only if $s \geq n_y$; by the convention on uses, $n_y$ is at least the use, which is at least $1$ when the computation queries the oracle. Let $s^* = n_0$.

1. Let $\Phi^X_e(y) = X(0)$ for every $y$, and let $A_s = B_s = \emptyset$ for $s \leq s^*$ and $A_s = B_s = \{ 0 \}$ for $s > s^*$. The two sides always agree when they converge, so $l(e, s)$ is the largest $l \leq s$ with $n_y \leq s$ for all $y < l$, which tends to infinity. Let $s_0 = s^*$, and $s_{k+1}$ the least $s > s_k$ with $l(e, s) > l(e, s_k)$. The sequence is computable and satisfies condition 1, and $l(e, s_0) \geq 1$. Condition 2 fails for $k = 0$: $0 < s_0$, and $0$ enters both $A$ and $B$ between $s_0$ and $s_1$. Now $\Delta(0) = \Phi^{A_{s_0}}_e(0)[s_0] = A_{s_0}(0) = 0$, whereas $\Phi^A_e(0) = A(0) = 1$. So the second item of the conclusion fails, and so does :ref{#cor-pair-module}: $\Phi^A_e = \Phi^B_e$ is the constant function $1$, while $\Delta(0) = 0$.

2. Let $\Phi^X_e(y) = \max(X(0), X(1))$ for every $y$, and $s^* = n_0$ as above. Let $B_s = \emptyset$ for $s \leq s^*$ and $B_s = \{ 1 \}$ after; $A_s = \emptyset$ for $s \leq s^* + 1$ and $A_s = \{ 0 \}$ after. Let $s_0 = s^*$, $s_1 = s^* + 1$, $s_2 = s^* + 2$, and for $k \geq 2$, $s_{k+1}$ the least $s > s_k$ with $l(e, s) > l(e, s_k)$. Between $s_0$ and $s_1$, $A$ does not change; between $s_1$ and $s_2$, $B$ does not change; after $s_2$, neither changes. So condition 2 holds. At $s_0$ both sides compute $0$ at input $0$, so $l(e, s_0) \geq 1$; at $s_1$, $\Phi^{A_{s_1}}_e(0)[s_1] = 0 \neq 1 = \Phi^{B_{s_1}}_e(0)[s_1]$, so $l(e, s_1) = 0$; from $s_2$ on, both sides compute the constant function $1$, so the lengths are unbounded. The least $k$ with $l(e, s_k) > 0$ is $k = 0$, so $\Delta(0) = 0$, whereas $\Phi^A_e(0) = \Phi^B_e(0) = 1$. The value has passed from one side to the other at a stage where the agreement was lost: the side that changed between $s_0$ and $s_1$ was not checked against the other at $s_1$.

In the tree construction, the first case is excluded because at most one number enters $A \cup B$ at each stage, and the second because the sequence used is that of the expansionary stages, whose lengths increase.
:::
::::

::::exercise{#ex-mp-posner-pairs difficulty=1 objective="Compare the requirements with one index for both oracles and the requirements with two indices."}
For indices $i$ and $j$, consider the requirement
$$
\mathcal N_{i,j} : \Phi^A_i = \Phi^B_j \text{ total} \implies \Phi^A_i \text{ computable}.
$$
Show that, for all sets $A$ and $B$, every requirement $\mathcal N_e$ holds if and only if every requirement $\mathcal N_{i,j}$ holds. Show that :ref{#lem-pair-module} remains true with $\Phi^A_i$ and $\Phi^B_j$ in place of $\Phi^A_e$ and $\Phi^B_e$, the length of agreement being defined accordingly. What does Posner's trick bring to the construction?

:::solution
$\mathcal N_e$ is $\mathcal N_{e,e}$, so if all $\mathcal N_{i,j}$ hold, all $\mathcal N_e$ hold. Conversely, suppose that all $\mathcal N_e$ hold, and that $C = \Phi^A_i = \Phi^B_j$ is total. Then $C \leq_T A$ and $C \leq_T B$. If $A \neq B$, :ref{#lem-posner} shows that $C$ is computable. If $A = B$, then $\Phi^A_i = \Phi^B_i = C$ is total, and $\mathcal N_i$ shows that $C$ is computable.

The proof of :ref{#lem-pair-module} never uses that the two functionals are the same: it compares a computation on the $A$ side with a computation on the $B$ side through the agreement at the stages $s_k$, and uses monotonicity on the side that does not change. It goes through word for word with $\Phi_i$ on the $A$ side and $\Phi_j$ on the $B$ side.

So the minimal pair construction could be run with the requirements $\mathcal N_{i,j}$ and without :ref{#lem-posner}. Posner's trick only simplifies the bookkeeping: one index per requirement instead of two.
:::
::::
:::::
