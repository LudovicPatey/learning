---
title: The Friedberg–Muchnik theorem
summary: Two Turing incomparable c.e. sets, by the finite injury priority method; requirements, witnesses, priority and initialization.
duration: 35
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

:::figure[The strategy of $\mathcal R_{2e}$ when it acts at stage $s + 1$ (here $s = 13$). Its witness $x$ enters $B$, which makes $B(x) = 1$, and the part of $A$ below the use $u$ of the computation $\Phi^{A_s}_e(x) = 0$ must be kept fixed. Requirements of lower priority are initialized and later use only numbers greater than $s$, which lie above $u$. A witness of higher priority chosen earlier may still enter below $u$: this is an injury.]
<svg class="fig" viewBox="0 0 590 230" width="590" role="img" aria-label="The action of R_2e: its witness x enters B, the oracle A is frozen below the use u, and the requirements of lower priority later use only fresh numbers, greater than the stage"><defs><marker id="ce-fm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="34" y="68" text-anchor="middle" class="math" font-size="17">A</text><rect x="60" y="52" width="23" height="23" class="cell"/><rect x="83" y="52" width="23" height="23" class="cell"/><rect x="106" y="52" width="23" height="23" class="cell"/><rect x="129" y="52" width="23" height="23" class="cell"/><rect x="152" y="52" width="23" height="23" class="cell"/><rect x="175" y="52" width="23" height="23" class="cell"/><rect x="198" y="52" width="23" height="23" class="cell"/><rect x="221" y="52" width="23" height="23" class="cell"/><rect x="244" y="52" width="23" height="23" class="cell"/><rect x="267" y="52" width="23" height="23" class="cell"/><rect x="290" y="52" width="23" height="23" class="cell"/><rect x="313" y="52" width="23" height="23" class="cell"/><rect x="336" y="52" width="23" height="23" class="cell"/><rect x="359" y="52" width="23" height="23" class="cell"/><rect x="382" y="52" width="23" height="23" class="cell"/><rect x="405" y="52" width="23" height="23" class="cell"/><rect x="428" y="52" width="23" height="23" class="cell"/><rect x="451" y="52" width="23" height="23" class="cell"/><rect x="474" y="52" width="23" height="23" class="cell"/><rect x="497" y="52" width="23" height="23" class="cell"/><rect x="385" y="55" width="17" height="17" class="soft-fill"/><rect x="408" y="55" width="17" height="17" class="soft-fill"/><rect x="431" y="55" width="17" height="17" class="soft-fill"/><rect x="454" y="55" width="17" height="17" class="soft-fill"/><rect x="477" y="55" width="17" height="17" class="soft-fill"/><rect x="500" y="55" width="17" height="17" class="soft-fill"/><text x="528" y="68" class="mrm muted" font-size="15">⋯</text><text x="34" y="166" text-anchor="middle" class="math" font-size="17">B</text><rect x="60" y="150" width="23" height="23" class="cell"/><rect x="83" y="150" width="23" height="23" class="cell"/><rect x="106" y="150" width="23" height="23" class="cell"/><rect x="129" y="150" width="23" height="23" class="cell"/><rect x="152" y="150" width="23" height="23" class="cell"/><rect x="175" y="150" width="23" height="23" class="cell"/><rect x="198" y="150" width="23" height="23" class="cell"/><rect x="221" y="150" width="23" height="23" class="cell"/><rect x="244" y="150" width="23" height="23" class="cell"/><rect x="267" y="150" width="23" height="23" class="cell"/><rect x="290" y="150" width="23" height="23" class="cell"/><rect x="313" y="150" width="23" height="23" class="cell"/><rect x="336" y="150" width="23" height="23" class="cell"/><rect x="359" y="150" width="23" height="23" class="cell"/><rect x="382" y="150" width="23" height="23" class="cell"/><rect x="405" y="150" width="23" height="23" class="cell"/><rect x="428" y="150" width="23" height="23" class="cell"/><rect x="451" y="150" width="23" height="23" class="cell"/><rect x="474" y="150" width="23" height="23" class="cell"/><rect x="497" y="150" width="23" height="23" class="cell"/><rect x="385" y="153" width="17" height="17" class="soft-fill"/><rect x="408" y="153" width="17" height="17" class="soft-fill"/><rect x="431" y="153" width="17" height="17" class="soft-fill"/><rect x="454" y="153" width="17" height="17" class="soft-fill"/><rect x="477" y="153" width="17" height="17" class="soft-fill"/><rect x="500" y="153" width="17" height="17" class="soft-fill"/><text x="528" y="166" class="mrm muted" font-size="15">⋯</text><text x="71.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="94.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">1</text><text x="117.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="140.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">3</text><text x="163.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="186.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">5</text><text x="209.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="232.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">7</text><text x="255.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="278.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">9</text><text x="301.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="324.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">11</text><text x="347.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="370.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">13</text><text x="393.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="416.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">15</text><text x="439.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="462.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">17</text><text x="485.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">18</text><text x="508.5" y="44" text-anchor="middle" class="mrm muted" font-size="10">19</text><path d="M62,81 L62,87 L265,87 L265,81" class="accent-stroke" stroke-width="1.6"/><text x="163.5" y="103" text-anchor="middle" class="label">below the use <tspan class="math" font-size="13">u</tspan>: kept fixed (restraint)</text><rect x="198" y="150" width="23" height="23" class="cell head-cell"/><text x="209.5" y="166" text-anchor="middle" class="mrm" font-size="13">1</text><text x="209.5" y="189" text-anchor="middle" class="math" font-size="14">x</text><line x1="209.5" y1="109" x2="209.5" y2="146" class="ink-stroke" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#ce-fm-arrow)"/><text x="217.5" y="136" class="label"><tspan class="mrm" font-size="13">Φ</tspan><tspan class="math" dy="-6" font-size="10">A</tspan><tspan class="mrm" font-size="8" dy="3">s</tspan><tspan class="mrm" font-size="13" dy="3">(</tspan><tspan class="math" font-size="13">x</tspan><tspan class="mrm" font-size="13">) = 0</tspan> at stage <tspan class="math" font-size="13">s</tspan>: enumerate <tspan class="math" font-size="13">x</tspan> into <tspan class="math" font-size="13">B</tspan></text><text x="382" y="189" class="label">numbers &gt; s: fresh witnesses</text><text x="382" y="204" class="label">of lower priority</text><path d="M135,58 L146,69 M135,69 L146,58" class="ink-stroke" stroke-width="1.6"/><text x="60" y="223" class="label">× a witness of higher priority, chosen before stage s, may still enter below <tspan class="math" font-size="13">u</tspan>: an injury</text></svg>
:::

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

The method is called **finite injury** because each requirement is injured only finitely often; here the number of injuries of $\mathcal R_i$ is even bounded by a computable function of $i$ (:ref{#ex-fm-injury-bound}). In later constructions, a requirement may be injured infinitely often while still being satisfied; these are **infinite injury** arguments.

The proof has the structure shared by all finite injury arguments, which the next two lessons follow:

1. the goal is split into countably many **requirements**, ordered by priority;
2. each requirement has a **strategy** that works in isolation, and has finitely many possible **outcomes**; here, $\mathcal R_{2e}$ either waits forever with its final witness outside $B$ (it is satisfied because $\Phi^A_e(x)$ never equals $0$), or acts once more and is satisfied by a preserved computation;
3. a strategy may be **injured** only by strategies of higher priority, and is then **initialized**;
4. the verification shows, by induction along the priority order, that each strategy acts finitely often, so that each one is injured finitely often and eventually runs undisturbed.

The induction of item 4 is exactly the proof of :ref{#lem-fm-finite-injury}: the hypothesis on the requirements of higher priority provides the stage $s_0$ after which $\mathcal R_i$ runs undisturbed.

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

::::exercise{#ex-fm-injury-bound difficulty=1 objective="Bound the number of injuries of a requirement in the Friedberg–Muchnik construction by a computable function."}
Show that the requirement $\mathcal R_i$ acts at most $2^i$ times and is initialized at most $2^i - 1$ times.

:::solution
Let $a_i$ and $n_i$ be the numbers of actions and initializations of $\mathcal R_i$. Initializations of $\mathcal R_i$ are caused by actions of $\mathcal R_j$, $j < i$, so $n_i \leq \sum_{j < i} a_j$. Between two initializations, and after the last one, $\mathcal R_i$ acts at most once, so $a_i \leq n_i + 1$. By induction, if $a_j \leq 2^j$ for $j < i$, then $n_i \leq 2^i - 1$ and $a_i \leq 2^i$.
:::
::::

::::exercise{#ex-fm-independent difficulty=2 objective="Extend the Friedberg–Muchnik construction to infinitely many pairwise incomparable c.e. sets."}
Show that there is a uniformly c.e. sequence of sets $(A_n)_{n \in \nat}$ such that $A_n \not\leq_T A_m$ for all $n \neq m$.

:::solution
Use the requirements $\mathcal R_{\langle e, n, m \rangle} : \Phi^{A_m}_e \neq A_n$, for $n \neq m$, ordered by their index. The strategy for $\mathcal R_{\langle e, n, m \rangle}$ has a witness $x$ for $A_n$, waits for $\Phi^{A_{m,s}}_e(x)[s]\converge = 0$, and then enumerates $x$ into $A_n$, initializing all requirements of lower priority. The verification is the same as for :ref{#thm-friedberg-muchnik}: after an action, the numbers entering $A_m$ are witnesses of requirements that are either of higher priority, and then act only finitely often, or of lower priority, and then are fresh. The construction builds all the sets $A_n$ simultaneously and is computable, so the relation $x \in A_n$ is c.e. in $(n, x)$: the sequence is uniformly c.e.
:::
::::

## Notes and references

Muchnik announced the solution of Post's problem in 1956 and Friedberg published his independently in 1957. The presentation with witnesses and initialization is the standard one: see Soare's book of 2016, Section 7.3 (Theorem 7.3.1, and Proposition 7.3.5 for the bound $2^e - 1$ on the injuries), Downey and Hirschfeldt, Section 2.11 (Theorem 2.11.1), and Nies, Section 1.6 (Theorem 1.6.8). Monin and Patey present the same construction with strategies described by states and outcomes, in their chapter on the priority method and c.e. degrees. The finite injury method requires only a weak form of induction: Mytilinaios showed that the Friedberg–Muchnik and Sacks splitting constructions can be carried out in models of arithmetic with $\Sigma_1$ induction; Chong, Li and Yang survey this line of work.

- C. T. Chong, W. Li and Y. Yang, *Nonstandard models in recursion theory and reverse mathematics*, Bulletin of Symbolic Logic 20 (2014), 170–200.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010.
- R. M. Friedberg, *Two recursively enumerable sets of incomparable degrees of unsolvability*, Proceedings of the National Academy of Sciences 43 (1957), 236–238.
- B. Monin and L. Patey, *Computability theory*, chapter *Priority method and c.e. degrees*.
- A. A. Muchnik, *On the unsolvability of the problem of reducibility in the theory of algorithms*, Doklady Akademii Nauk SSSR 108 (1956), 194–197.
- M. Mytilinaios, *Finite injury and $\Sigma_1$-induction*, Journal of Symbolic Logic 54 (1989), 38–49.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.

:::::exercises
::::exercise{#ex-fm-fresh-needed difficulty=1 objective="See why the witnesses of the Friedberg–Muchnik construction must be fresh."}
Change the construction so that a requirement without witness receives as witness the least number that is not in $A_s \cup B_s$ and is not the witness of another requirement, instead of a fresh number. Identify the step of the proof of :ref{#lem-fm-preservation} that no longer holds, and describe how $\mathcal R_0$ could then fail to be satisfied.

:::solution
The proof of :ref{#lem-fm-preservation} uses that every requirement $\mathcal R_j$ with $j > 2e$, initialized at stage $s + 1$, afterwards uses only witnesses greater than $s$, hence greater than the use $u \leq s$ of the computation preserved by $\mathcal R_{2e}$. With the new rule, this fails: the new witness of $\mathcal R_j$ may be smaller than $u$.

A possible run: $\mathcal R_0$ acts at stage $s + 1$ with witness $x$, through a computation $\Phi^{A_s}_0(x)[s] = 0$ whose use $u$ exceeds some number $y \notin A_s$ read by the computation. At the same stage, $\mathcal R_1 : \Phi^B_0 \neq A$ is initialized and may receive $y$ as its new witness, if $y$ is the least number outside $A_s \cup B_s$ that is not a witness. If later $\Phi^{B_t}_0(y)[t]\converge = 0$, then $\mathcal R_1$ requires attention; $\mathcal R_0$ is marked and does not, so $\mathcal R_1$ acts and enumerates $y$ into $A$. Then $A \uh u \neq A_s \uh u$, and the computation $\Phi^A_0(x)$ may diverge or converge to $1$. Since $\mathcal R_1$ has lower priority, $\mathcal R_0$ is not initialized: it stays marked as satisfied and never acts again, although $\Phi^A_0(x) = 1 = B(x)$ is possible. Freshness is what prevents a requirement of lower priority from acting below a use that a requirement of higher priority preserves.
:::
::::

::::exercise{#ex-fm-relativized difficulty=1 objective="Relativize the Friedberg–Muchnik theorem and derive incomparable degrees between a degree and its jump." lessons="turing-degrees/turing-jump"}
Show that for every set $X$ there are sets $A$ and $B$, c.e. in $X$, such that $A \oplus X$ and $B \oplus X$ are Turing incomparable. Deduce that for every degree $\mathbf{x}$ there are incomparable degrees $\abf$ and $\bbf$ with $\mathbf{x} < \abf < \mathbf{x}'$ and $\mathbf{x} < \bbf < \mathbf{x}'$.

:::solution
Run the construction with the requirements $\Phi^{A \oplus X}_e \neq B$ and $\Phi^{B \oplus X}_e \neq A$, using at stage $s$ the computations $\Phi^{A_s \oplus X}_e(x)[s]$ and $\Phi^{B_s \oplus X}_e(x)[s]$. Their convergence is decidable with oracle $X$, so the construction is $X$-computable and $A$, $B$ are c.e. in $X$. The verification is unchanged. In :ref{#lem-fm-preservation}, a computation converging at stage $s$ reads only cells below $u \leq s$ of $A_s \oplus X$; its $X$-part never changes, and a number $y$ entering $A$ after stage $s$ is fresh, so $y > s$ and the cell $2y$ that codes it lies above $u$. The use principle, which holds for every oracle, gives the preservation, and :ref{#lem-fm-finite-injury} is proved as before. So $B \not\leq_T A \oplus X$ and $A \not\leq_T B \oplus X$; since $B \leq_T B \oplus X$ and $X \leq_T A \oplus X$, this gives $B \oplus X \not\leq_T A \oplus X$, and symmetrically.

Let $X \in \mathbf{x}$, $\abf = \deg_T(A \oplus X)$ and $\bbf = \deg_T(B \oplus X)$, which are incomparable. Both are above $\mathbf{x}$. If $\abf = \mathbf{x}$, then $A \oplus X \leq_T B \oplus X$, which is false; so $\mathbf{x} < \abf$. Every set c.e. in $X$ is computable in $X'$, so $A \oplus X \leq_T X'$. If $X' \leq_T A \oplus X$, then $B \leq_T X' \leq_T A \oplus X$, which is false; so $\abf < \mathbf{x}'$. The same holds for $\bbf$.
:::
::::

::::exercise{#ex-fm-simple difficulty=2 objective="Combine the Friedberg–Muchnik requirements with Post's requirements to make both sets simple." lessons="simple-sets"}
Modify the construction so that, in addition, $A$ and $B$ are simple.

:::solution
Add, for every $e$, the requirements $\mathcal P^A_e : W_e \text{ infinite} \Rightarrow W_e \cap A \neq \emptyset$ and $\mathcal P^B_e : W_e \text{ infinite} \Rightarrow W_e \cap B \neq \emptyset$, and arrange all requirements in one priority list $\mathcal Q_0, \mathcal Q_1, \dots$, for instance $\mathcal Q_{4e} = \mathcal R_{2e}$, $\mathcal Q_{4e+1} = \mathcal R_{2e+1}$, $\mathcal Q_{4e+2} = \mathcal P^A_e$, $\mathcal Q_{4e+3} = \mathcal P^B_e$. When $\mathcal R_{2e}$ is marked as satisfied, call the use of the computation through which it acted its **restraint on $A$**; similarly, a marked $\mathcal R_{2e+1}$ has a restraint on $B$.

*Construction.* The requirements $\mathcal R_i$ require attention as before. The requirement $\mathcal P^A_e = \mathcal Q_k$ requires attention at stage $s + 1$ if $k \leq s$, $W_e[s] \cap A_s = \emptyset$, and some $x \in W_e[s]$ is greater than the restraint on $A$ of every marked $\mathcal R_j$ of higher priority, and is not the witness of a requirement of higher priority. At stage $s + 1$, the requirement $\mathcal Q_k$ of least index $k \leq s$ that requires attention acts: an $\mathcal R_i$ as before, and $\mathcal P^A_e$ by enumerating the least such $x$ into $A$; in both cases, all requirements of lower priority are initialized. Then fresh witnesses are assigned as before. $\mathcal P^B_e$ is treated symmetrically.

*Preservation.* Suppose $\mathcal R_{2e}$ acts at stage $s + 1$ with use $u \leq s$ and is never initialized afterwards; it stays marked. A number entering $A$ after stage $s$ is either the witness of some $\mathcal R_j$ with $j$ odd, or an element enumerated by some $\mathcal P^A_{e'}$. Requirements of higher priority do not act after stage $s + 1$, since they would initialize $\mathcal R_{2e}$. Requirements $\mathcal R_j$ of lower priority use witnesses chosen fresh after stage $s$, greater than $u$. Requirements $\mathcal P^A_{e'}$ of lower priority enumerate only numbers greater than the restraint $u$ of the marked $\mathcal R_{2e}$. So $A \uh u = A_s \uh u$, and :ref{#lem-fm-preservation} holds.

*Each requirement acts finitely often and is satisfied*, by induction on $k$. Let $s_0 \geq k$ be a stage after which no requirement of higher priority than $\mathcal Q_k$ acts. Then $\mathcal Q_k$ is not initialized after $s_0$.

- A requirement $\mathcal P^A_e$ acts at most once: afterwards $W_e \cap A \neq \emptyset$, and it never requires attention again.
- If $\mathcal Q_k = \mathcal R_{2e}$, the proof of :ref{#lem-fm-finite-injury} applies, with one more remark: its final witness $x$ could only enter $B$ through $\mathcal R_{2e}$ itself or through some $\mathcal P^B_{e'}$; one of higher priority does not act after $s_0$, and one of lower priority may not enumerate the witness of a requirement of higher priority. So $x \notin B$ as long as $\mathcal R_{2e}$ does not act.
- If $\mathcal Q_k = \mathcal P^A_e$ and $W_e$ is infinite: after $s_0$, the witnesses of the requirements of higher priority, and the marks and restraints of the $\mathcal R_j$ of higher priority, no longer change, since these change only when a requirement acts or is initialized. Let $M$ bound these restraints and witnesses. Some $x > M$ belongs to $W_e[s]$ for some $s \geq s_0$. If $W_e[s] \cap A_s = \emptyset$, then $\mathcal P^A_e$ requires attention at stage $s + 1$, while no requirement of higher priority does, since it would act; so $\mathcal P^A_e$ acts. In all cases $W_e \cap A \neq \emptyset$.

*Conclusion.* As before, $A \not\leq_T B$ and $B \not\leq_T A$. In particular $A$ is not computable, hence not cofinite, so its complement is infinite; together with the requirements $\mathcal P^A_e$, $A$ is simple. The same holds for $B$. No counting argument is needed here: the coinfiniteness of $A$ follows from its non-computability.
:::
::::

::::exercise{#ex-fm-independent-join difficulty=2 objective="Strengthen the independence of a uniformly c.e. sequence: no set is computable in the join of the others."}
For a sequence $(A_n)$ and a set $F \subseteq \nat$, write $\bigoplus_{m \in F} A_m = \{ \langle m, x \rangle : m \in F, x \in A_m \}$. Show that there is a uniformly c.e. sequence $(A_n)$ such that $A_n \not\leq_T \bigoplus_{m \neq n} A_m$ for every $n$. Deduce that for finite sets $F, G \subseteq \nat$ with $G \not\subseteq F$, we have $\bigoplus_{m \in G} A_m \not\leq_T \bigoplus_{m \in F} A_m$.

:::solution
Write $\widehat A_n = \bigoplus_{m \neq n} A_m$, with the approximations $\widehat A_{n,s} = \{ \langle m, x \rangle : m \neq n, x \in A_{m,s} \}$. The requirements are $\mathcal R_{\langle e, n \rangle} : \Phi^{\widehat A_n}_e \neq A_n$, ordered by their index. The strategy of $\mathcal R_{\langle e, n \rangle}$ has a witness $x$, fresh when chosen, waits for a stage $s$ with $\Phi^{\widehat A_{n,s}}_e(x)[s]\converge = 0$, then enumerates $x$ into $A_n$, is marked as satisfied, and initializes all requirements of lower priority. The construction is that of the lesson, with these requirements; it is computable, so the relation $x \in A_n$ is c.e. in $(n, x)$.

*Preservation.* Suppose $\mathcal R_{\langle e, n \rangle}$ acts at stage $s + 1$ through a computation with use $u \leq s$, and is never initialized afterwards. A number entering $\widehat A_n$ after stage $s$ has the form $\langle m, y \rangle$, where $m \neq n$ and $y$ is the witness of a requirement $\mathcal R_{\langle e', m \rangle}$ acting after stage $s + 1$. Such a requirement has lower priority, since one of higher priority would initialize $\mathcal R_{\langle e, n \rangle}$; it was initialized at stage $s + 1$, so $y$ was chosen fresh afterwards and $y > s$. Then $\langle m, y \rangle \geq y > s \geq u$, by the properties of the pairing function. So $\widehat A_n \uh u = \widehat A_{n,s} \uh u$, and $\Phi^{\widehat A_n}_e(x) = 0 \neq 1 = A_n(x)$.

*Finite injury.* The proof of :ref{#lem-fm-finite-injury} applies without change: by induction on the index, each requirement is initialized finitely often, has a final witness, acts at most once after its last initialization, and is satisfied either by the preservation above or because its final witness stays out of $A_n$ while $\Phi^{\widehat A_n}_e(x) \neq 0$.

*Deduction.* Let $n \in G \setminus F$. Then $A_n \leq_T \bigoplus_{m \in G} A_m$, through $x \in A_n \iff \langle n, x \rangle \in \bigoplus_{m \in G} A_m$. And $\bigoplus_{m \in F} A_m \leq_T \widehat A_n$, since $n \notin F$: a number belongs to the first set if and only if it has the form $\langle m, x \rangle$ with $m \in F$ and it belongs to $\widehat A_n$, and $F$ is finite. If $\bigoplus_{m \in G} A_m \leq_T \bigoplus_{m \in F} A_m$, then $A_n \leq_T \widehat A_n$, a contradiction.

Adapted from Soare 2016, Exercise 7.3.6 (i). The sets $\bigoplus_{m \in F} A_m$, for finite $F$, thus have pairwise distinct degrees, ordered as the finite sets $F$ under inclusion; this is the starting point of embeddings of partial orders into the c.e. degrees.
:::
::::
:::::
