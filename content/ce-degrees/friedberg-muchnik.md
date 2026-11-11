---
title: The Friedberg–Muchnik theorem
summary: Two Turing incomparable c.e. sets, by the finite injury priority method; requirements, witnesses, priority and initialization.
duration: 45
prerequisites: [simple-sets, turing-degrees/finite-extensions]
---

The Kleene–Post theorem builds two incomparable sets by finite extensions, with the oracle $\emptyset'$ answering questions such as "is there an extension making this computation converge?". To make the sets c.e., the construction must be computable, and elements may be added but never removed. It can no longer ask whether a computation will converge; it can only watch computations converge with the current approximations, and act on what it sees. A later action may then destroy what an earlier one relied on. The **priority method**, found independently by Friedberg and Muchnik, organizes these conflicts: requirements are ordered by priority, a requirement may only be disturbed by requirements of higher priority, and each requirement is disturbed only finitely often.

:::theorem[Friedberg, Muchnik]{#thm-friedberg-muchnik}
There are c.e. sets $A$ and $B$ such that $A \not\leq_T B$ and $B \not\leq_T A$.
:::

:::corollary{#cor-post-problem}
There is a c.e. set $A$ with $\emptyset <_T A <_T \emptyset'$. This solves Post's problem.
:::

:::proof{of=cor-post-problem}
Let $A$ and $B$ be as in the theorem. If $A$ were computable, it would be computable from $B$, contradicting $A \not\leq_T B$. If $\emptyset' \leq_T A$, then $B \leq_T \emptyset' \leq_T A$, since every c.e. set is computable in $\emptyset'$, contradicting $B \not\leq_T A$. And $A \leq_T \emptyset'$ since $A$ is c.e.
:::

## The requirements

We enumerate $A$ and $B$ by stages, $A = \bigcup_s A_s$ and $B = \bigcup_s B_s$, with finite sets $A_s \subseteq A_{s+1}$ and $B_s \subseteq B_{s+1}$ computable from $s$. The requirements are, for every $e$:
$$
\mathcal R_{2e} : \Phi^A_e \neq B, \qquad \mathcal R_{2e+1} : \Phi^B_e \neq A.
$$
They are ordered by **priority**: $\mathcal R_i$ has higher priority than $\mathcal R_j$ if $i < j$.

*The strategy for one requirement.* Consider $\mathcal R_{2e}$. It is assigned a **witness** $x$, a number not yet in $B$. It waits for a stage $s$ at which $\Phi^{A_s}_e(x)[s]\converge = 0$. If this never happens, then either $\Phi^A_e(x)$ diverges or is different from $0$, while $x \notin B$, so $\Phi^A_e(x) \neq B(x)$: the requirement is satisfied without action. If it happens, the strategy enumerates $x$ into $B$, so that $B(x) = 1 \neq 0 = \Phi^{A_s}_e(x)$, and must then ensure that $A$ does not change below the use $u$ of this computation, so that $\Phi^A_e(x) = 0$ as well. This last condition is a **restraint** on $A$: the numbers below $u$ must not be enumerated into $A$ later. The strategy for $\mathcal R_{2e+1}$ is the same with $A$ and $B$ exchanged.

*Conflicts.* The requirements $\mathcal R_{2e'+1}$ enumerate their witnesses into $A$, and may thus violate the restraint of $\mathcal R_{2e}$. Priority resolves the conflict: a requirement of lower priority must respect the restraints of higher priority, and a requirement of higher priority may **injure** one of lower priority, by enumerating a number below its restraint. The injured requirement is then **initialized**: it loses its witness, and starts again with a new one.

Respecting restraints is obtained without bookkeeping: when a requirement acts, all requirements of lower priority are initialized, and the witnesses chosen afterwards are **fresh**, larger than every number seen so far in the construction, in particular larger than the use of the computation being preserved.

## The construction

A requirement $\mathcal R_i$ may have a witness, written $x_i$, and may be marked as **satisfied**. To **initialize** $\mathcal R_i$ is to cancel its witness and remove its mark. A number is **fresh** at a stage if it is larger than every number mentioned so far in the construction: every witness, every element of $A_s$ or $B_s$, and the stage itself.

*Stage $0$.* $A_0 = B_0 = \emptyset$, no requirement has a witness.

*Stage $s + 1$.* Say that $\mathcal R_{2e}$ **requires attention** if it has a witness $x$, it is not marked as satisfied, and $\Phi^{A_s}_e(x)[s]\converge = 0$; and similarly that $\mathcal R_{2e+1}$ requires attention if it has a witness $x$, it is not marked, and $\Phi^{B_s}_e(x)[s]\converge = 0$.

1. If some $\mathcal R_i$ with $i \leq s$ requires attention, take the least such $i$. If $i = 2e$, enumerate $x_i$ into $B$; if $i = 2e + 1$, enumerate $x_i$ into $A$. Mark $\mathcal R_i$ as satisfied, and initialize every $\mathcal R_j$ with $j > i$. We say that $\mathcal R_i$ **acts** at stage $s + 1$.
2. Every $\mathcal R_j$ with $j \leq s$ that has no witness receives a fresh witness, the witnesses being chosen in increasing order of $j$.

The construction is computable: at each stage, finitely many requirements are considered, and the condition "$\Phi^{A_s}_e(x)[s]\converge = 0$" is decidable. So $A$ and $B$ are c.e.

:::figure[A schematic run of the construction for the first four requirements. Each action initializes the requirements of lower priority, which then receive new, fresh witnesses (in the construction, during the same stage; they are drawn one stage later for readability). A requirement of priority $i$ is initialized at most $2^i - 1$ times.]
<svg class="fig" viewBox="0 0 590 250" width="590" role="img" aria-label="A run of a finite injury construction: each action initializes all requirements of lower priority, which then choose new witnesses"><text x="70" y="22" text-anchor="middle" class="mrm muted" font-size="11">0</text><line x1="70" y1="32" x2="70" y2="170" class="axis" stroke-dasharray="2 4"/><text x="108" y="22" text-anchor="middle" class="mrm muted" font-size="11">1</text><line x1="108" y1="32" x2="108" y2="170" class="axis" stroke-dasharray="2 4"/><text x="146" y="22" text-anchor="middle" class="mrm muted" font-size="11">2</text><line x1="146" y1="32" x2="146" y2="170" class="axis" stroke-dasharray="2 4"/><text x="184" y="22" text-anchor="middle" class="mrm muted" font-size="11">3</text><line x1="184" y1="32" x2="184" y2="170" class="axis" stroke-dasharray="2 4"/><text x="222" y="22" text-anchor="middle" class="mrm muted" font-size="11">4</text><line x1="222" y1="32" x2="222" y2="170" class="axis" stroke-dasharray="2 4"/><text x="260" y="22" text-anchor="middle" class="mrm muted" font-size="11">5</text><line x1="260" y1="32" x2="260" y2="170" class="axis" stroke-dasharray="2 4"/><text x="298" y="22" text-anchor="middle" class="mrm muted" font-size="11">6</text><line x1="298" y1="32" x2="298" y2="170" class="axis" stroke-dasharray="2 4"/><text x="336" y="22" text-anchor="middle" class="mrm muted" font-size="11">7</text><line x1="336" y1="32" x2="336" y2="170" class="axis" stroke-dasharray="2 4"/><text x="374" y="22" text-anchor="middle" class="mrm muted" font-size="11">8</text><line x1="374" y1="32" x2="374" y2="170" class="axis" stroke-dasharray="2 4"/><text x="412" y="22" text-anchor="middle" class="mrm muted" font-size="11">9</text><line x1="412" y1="32" x2="412" y2="170" class="axis" stroke-dasharray="2 4"/><text x="450" y="22" text-anchor="middle" class="mrm muted" font-size="11">10</text><line x1="450" y1="32" x2="450" y2="170" class="axis" stroke-dasharray="2 4"/><text x="488" y="22" text-anchor="middle" class="mrm muted" font-size="11">11</text><line x1="488" y1="32" x2="488" y2="170" class="axis" stroke-dasharray="2 4"/><text x="526" y="22" text-anchor="middle" class="mrm muted" font-size="11">12</text><line x1="526" y1="32" x2="526" y2="170" class="axis" stroke-dasharray="2 4"/><text x="540" y="22" class="label">stage</text><text x="48" y="45" text-anchor="end" class="math" font-size="16">R<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="108" y1="40" x2="184" y2="40" class="accent-stroke" stroke-width="2"/><line x1="184" y1="40" x2="545.0" y2="40" class="ink-stroke" stroke-width="3"/><circle cx="108" cy="40" r="5" class="node"/><rect x="178" y="34" width="12" height="12" class="accent-fill"/><text x="48" y="85" text-anchor="end" class="math" font-size="16">R<tspan class="mrm" font-size="10" dy="4">1</tspan></text><line x1="108" y1="80" x2="184" y2="80" class="accent-stroke" stroke-width="2"/><line x1="222" y1="80" x2="336" y2="80" class="accent-stroke" stroke-width="2"/><line x1="336" y1="80" x2="545.0" y2="80" class="ink-stroke" stroke-width="3"/><circle cx="108" cy="80" r="5" class="node"/><path d="M179,75 L189,85 M179,85 L189,75" class="ink-stroke" stroke-width="1.8"/><circle cx="222" cy="80" r="5" class="node"/><rect x="330" y="74" width="12" height="12" class="accent-fill"/><text x="48" y="125" text-anchor="end" class="math" font-size="16">R<tspan class="mrm" font-size="10" dy="4">2</tspan></text><line x1="108" y1="120" x2="184" y2="120" class="accent-stroke" stroke-width="2"/><line x1="222" y1="120" x2="336" y2="120" class="accent-stroke" stroke-width="2"/><line x1="374" y1="120" x2="450" y2="120" class="accent-stroke" stroke-width="2"/><line x1="450" y1="120" x2="545.0" y2="120" class="ink-stroke" stroke-width="3"/><circle cx="108" cy="120" r="5" class="node"/><path d="M179,115 L189,125 M179,125 L189,115" class="ink-stroke" stroke-width="1.8"/><circle cx="222" cy="120" r="5" class="node"/><path d="M331,115 L341,125 M331,125 L341,115" class="ink-stroke" stroke-width="1.8"/><circle cx="374" cy="120" r="5" class="node"/><rect x="444" y="114" width="12" height="12" class="accent-fill"/><text x="48" y="165" text-anchor="end" class="math" font-size="16">R<tspan class="mrm" font-size="10" dy="4">3</tspan></text><line x1="108" y1="160" x2="184" y2="160" class="accent-stroke" stroke-width="2"/><line x1="222" y1="160" x2="336" y2="160" class="accent-stroke" stroke-width="2"/><line x1="374" y1="160" x2="450" y2="160" class="accent-stroke" stroke-width="2"/><line x1="488" y1="160" x2="545.0" y2="160" class="accent-stroke" stroke-width="2"/><circle cx="108" cy="160" r="5" class="node"/><path d="M179,155 L189,165 M179,165 L189,155" class="ink-stroke" stroke-width="1.8"/><circle cx="222" cy="160" r="5" class="node"/><path d="M331,155 L341,165 M331,165 L341,155" class="ink-stroke" stroke-width="1.8"/><circle cx="374" cy="160" r="5" class="node"/><path d="M445,155 L455,165 M445,165 L455,155" class="ink-stroke" stroke-width="1.8"/><circle cx="488" cy="160" r="5" class="node"/><circle cx="70" cy="206" r="5" class="node"/><text x="82" y="210" class="label">new witness</text><rect x="182" y="200" width="12" height="12" class="accent-fill"/><text x="200" y="210" class="label">action (enumeration and restraint)</text><path d="M415,201 L425,211 M415,211 L425,201" class="ink-stroke" stroke-width="1.8"/><text x="432" y="210" class="label">initialization</text></svg>
:::

## Verification

Witnesses are fresh when chosen, so distinct requirements, and distinct witnesses of the same requirement, never share a number; and a witness $x_i$ is enumerated only by $\mathcal R_i$.

:::lemma{#lem-fm-preservation}
Suppose $\mathcal R_{2e}$ acts at stage $s + 1$ with witness $x$, through a computation $\Phi^{A_s}_e(x)[s]\converge = 0$ with use $u$, and is never initialized afterwards. Then $A \uh u = A_s \uh u$, so that $\Phi^A_e(x) = 0 \neq 1 = B(x)$. The same holds for $\mathcal R_{2e+1}$, with $A$ and $B$ exchanged.
:::

:::proof{of=lem-fm-preservation}
The numbers enumerated into $A$ after stage $s$ are witnesses of requirements $\mathcal R_j$ with $j$ odd, at the stages where they act. No $\mathcal R_j$ with $j < 2e$ acts after stage $s + 1$, since it would initialize $\mathcal R_{2e}$. Every $\mathcal R_j$ with $j > 2e$ is initialized at stage $s + 1$, so any witness it uses afterwards was chosen fresh at stage $s + 1$ or later, and is greater than $s$. The use satisfies $u \leq s$, since the computation converges at stage $s$ (its code is smaller than $s$, and it reads only cells below its number of steps). So no number below $u$ enters $A$ after stage $s$, and by the use principle $\Phi^A_e(x) = \Phi^{A_s}_e(x) = 0$, while $x \in B$.
:::

:::lemma{#lem-fm-finite-injury}
Every requirement acts only finitely often, is initialized only finitely often, and is satisfied.
:::

:::proof{of=lem-fm-finite-injury}
By induction on $i$. Suppose every $\mathcal R_j$ with $j < i$ acts only finitely often, and let $s_0 \geq i$ be a stage after which none of them acts. A requirement is only initialized by the action of a requirement of higher priority, so $\mathcal R_i$ is not initialized after stage $s_0$, and it is initialized only finitely often. Let $t \leq s_0$ be the last stage at which $\mathcal R_i$ is initialized, or $t = 0$ if it never is. From the end of stage $s_0 + 1$ on, $\mathcal R_i$ has a witness $x$ (it receives one at the latest at stage $s_0 + 1$, since $i \leq s_0$), which never changes. After stage $t$, $\mathcal R_i$ acts at most once, since acting marks it as satisfied and the mark can only be removed by an initialization. So $\mathcal R_i$ acts finitely often. Say $i = 2e$; the odd case is symmetric.

If $\mathcal R_i$ acts after stage $t$, it acts with the witness $x$ and is never initialized afterwards, so it is satisfied by :ref{#lem-fm-preservation}.

If $\mathcal R_i$ does not act after stage $t$, then $x \notin B$, since only $\mathcal R_i$ enumerates $x$, and $\mathcal R_i$ is never marked as satisfied after stage $t$ (the mark is removed at an initialization, and is absent at the start). Suppose $\Phi^A_e(x)\converge = 0$, with use $u$. For all sufficiently large $s$, $A_s \uh u = A \uh u$ and the computation converges at stage $s$, so $\Phi^{A_s}_e(x)[s]\converge = 0$ by the use principle, and, for $s \geq s_0$, $\mathcal R_i$ requires attention at stage $s + 1$. No $\mathcal R_j$ with $j < i$ requires attention at a stage after $s_0$, since the least requirement requiring attention acts, and they do not act. So $\mathcal R_i$ would act, a contradiction. Hence $\Phi^A_e(x) \neq 0 = B(x)$, and $\mathcal R_i$ is satisfied.
:::

:::proof{of=thm-friedberg-muchnik}
The sets $A$ and $B$ are c.e., and by :ref{#lem-fm-finite-injury} every requirement is satisfied: $\Phi^A_e \neq B$ and $\Phi^B_e \neq A$ for every $e$. So $B \not\leq_T A$ and $A \not\leq_T B$.
:::

The method is called **finite injury** because each requirement is injured only finitely often; here the number of injuries of $\mathcal R_i$ is even bounded by a computable function of $i$ (see the exercises). In later constructions, a requirement may be injured infinitely often while still being satisfied; these are **infinite injury** arguments.

:::quiz[the priority construction]
Why are witnesses chosen fresh, larger than every number mentioned so far?

- [x] So that a requirement of lower priority, initialized when a higher one acts, can never enumerate a number below the use the higher one wants to preserve.

  Freshness implements the restraints without recording them: the uses are smaller than the stage at which they are found.
- [ ] To make $A$ and $B$ infinite.

  Freshness plays no role in the size of $A$ and $B$; what it ensures is that the restraints are respected.
- [ ] To make the construction computable.

  Any computable choice of witnesses keeps the construction computable.

---

In :ref{#lem-fm-finite-injury}, where is it used that the **least** requirement requiring attention acts?

- [x] To conclude that, after stage $s_0$, the requirement $\mathcal R_i$ acts whenever it requires attention, since no requirement of higher priority requires attention then.

  If any requirement requiring attention could act, $\mathcal R_i$ might be postponed forever by requirements of lower priority.
- [ ] To show that $\mathcal R_i$ is initialized finitely often.

  This only uses that initializations come from actions of higher priority requirements, which act finitely often by induction.
- [ ] To show that the witnesses are distinct.

  Distinctness comes from freshness.

---

A requirement $\mathcal R_{2e}$ never acts after its last initialization, and $\Phi^A_e(x)$ converges to $1$. Is it satisfied?

- [x] Yes: $x \notin B$, so $B(x) = 0 \neq 1 = \Phi^A_e(x)$.

  The strategy only acts when the computation converges to $0$; any other outcome already gives a disagreement, since $x$ stays out of $B$.
- [ ] No: it should have enumerated $x$ into $B$.

  Enumerating $x$ would create an agreement, $B(x) = 1 = \Phi^A_e(x)$.
- [ ] Only if $\Phi^B_e \neq A$.

  This is the requirement $\mathcal R_{2e+1}$, which is independent.
:::

## Exercises

::::exercise{difficulty=1}
Show that the requirement $\mathcal R_i$ acts at most $2^i$ times and is initialized at most $2^i - 1$ times.

:::solution
Let $a_i$ and $n_i$ be the numbers of actions and initializations of $\mathcal R_i$. Initializations of $\mathcal R_i$ are caused by actions of $\mathcal R_j$, $j < i$, so $n_i \leq \sum_{j < i} a_j$. Between two initializations, and after the last one, $\mathcal R_i$ acts at most once, so $a_i \leq n_i + 1$. By induction, if $a_j \leq 2^j$ for $j < i$, then $n_i \leq 2^i - 1$ and $a_i \leq 2^i$.
:::
::::

::::exercise{difficulty=2}
Show that there is a uniformly c.e. sequence of sets $(A_n)_{n \in \nat}$ such that $A_n \not\leq_T A_m$ for all $n \neq m$.

:::solution
Use the requirements $\mathcal R_{\langle e, n, m \rangle} : \Phi^{A_m}_e \neq A_n$, for $n \neq m$, ordered by their index. The strategy for $\mathcal R_{\langle e, n, m \rangle}$ has a witness $x$ for $A_n$, waits for $\Phi^{A_{m,s}}_e(x)[s]\converge = 0$, and then enumerates $x$ into $A_n$, initializing all requirements of lower priority. The verification is the same as for :ref{#thm-friedberg-muchnik}: after an action, the numbers entering $A_m$ are witnesses of requirements that are either of higher priority, and then act only finitely often, or of lower priority, and then are fresh. The construction builds all the sets $A_n$ simultaneously and is computable, so the relation $x \in A_n$ is c.e. in $(n, x)$: the sequence is uniformly c.e.
:::
::::

## Notes and references

Muchnik announced the solution of Post's problem in 1956 and Friedberg published his independently in 1957. The presentation with witnesses and initialization follows Soare's textbooks, where the finite injury method is developed with many further applications.

- A. A. Muchnik, *On the unsolvability of the problem of reducibility in the theory of algorithms*, Doklady Akademii Nauk SSSR 108 (1956), 194–197.
- R. M. Friedberg, *Two recursively enumerable sets of incomparable degrees of unsolvability*, Proceedings of the National Academy of Sciences 43 (1957), 236–238.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
