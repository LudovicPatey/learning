---
title: Forcing with a cohesive class
summary: Pairs of stems sharing a reservoir in the core of a cohesive class and in a Scott ideal avoiding the cone; validity; a question for Σ⁰₁ sentences about stems.
duration: 45
prerequisites: [cohesive-classes, ramsey-theorem/cone-avoidance, avoidance/seetapun-forcing]
---

This lesson and the next two prove the theorem of Monin and Patey.

:::theorem[Monin, Patey]{#thm-pigeons-non-high}
Let $Z$ be a set and $C$ a set with $C \not\leq_T Z'$. For every set $A$, there is an infinite set $H$ with $H \subseteq A$ or $H \subseteq \overline A$, and $C \not\leq_T (Z \oplus H)'$. In other words, $\mathsf{RT}^1_2$ admits strong jump cone avoidance.
:::

With $C = Z''$, it gives non-high solutions (:ref{#prop-jca-not-high}). The proof is a second-jump version of the Dzhafarov–Jockusch forcing of :ref{#thm-dj-cone-avoidance}, with pairs of stems $\sigma_0 \subseteq A$, $\sigma_1 \subseteq \overline A$ sharing a reservoir in a Scott ideal avoiding the cone. Two changes are needed. The reservoirs are taken in the core $\mathcal U$ of a cohesive class (:ref{#prop-cohesive-core}), a non-trivial partition regular class that maintains positive information, as forcing $\Pi^0_2$ sentences requires (:ref{to="jump-cone-avoidance/partition-regularity"}). And the Scott ideal of the reservoirs contains $\emptyset'$, since the questions about $\Sigma^0_2$ sentences have answers $\Sigma^0_1$ relative to its members. The price is the loss of first-jump control: the question for $\Sigma^0_1$ sentences has answers $\Pi^0_1$, not $\Sigma^0_1$, relative to a member of the ideal; this is no obstacle, since only the jump of the solution is controlled.

This lesson sets up the notion of forcing and the question for $\Sigma^0_1$ sentences; :ref{to="jump-cone-avoidance/pigeon-questions"} treats $\Sigma^0_2$ sentences, and :ref{to="jump-cone-avoidance/pigeons-non-high"} concludes. The proof is written for $Z = \emptyset$; the general case is explained at the end.

## The two ideals

:::lemma{#lem-pigeon-setting}
Let $C$ be a set with $C \not\leq_T \emptyset'$. There are:

1. a Scott ideal $\mathcal M$ with a low code $M = \bigoplus_i Z_i$;
2. a Scott ideal $\mathcal N$ containing $\emptyset'$ and not containing $C$;
3. a set $S \in \mathcal N$ of pairs such that $\mathcal U_S$, defined from $M$, is $\mathcal M$-cohesive and all its members are infinite.

Moreover $M \in \mathcal N$, $M' \in \mathcal N$ and $\mathcal M \subseteq \mathcal N$.
:::

:::proof{of=lem-pigeon-setting}
1 is :ref{#cor-scott-codes} with $X = \emptyset$. For 2, apply :ref{#lem-scott-cone} with $\emptyset'$ in place of $Z$. Since $M' \leq_T \emptyset'$, the sets $M$, $M'$ and the columns $Z_i$ are computable in $\emptyset' \in \mathcal N$, so they belong to $\mathcal N$. By :ref{#prop-wkl-scott}, $\mathcal N$ contains a set $P$ PA relative to $\emptyset'$, which is PA relative to $M'$. With $S_0$ the computable set of pairs defining the class of infinite sets (after :ref{#thm-cohesive-class}), $P$ is PA relative to $S_0 \oplus M'$, and :ref{#thm-cohesive-class} gives $S \leq_T P$, so $S \in \mathcal N$.
:::

From now on, $C$, $\mathcal M$, $\mathcal N$ and $S$ are fixed as in the lemma, $\mathcal U = \langle \mathcal U_S \rangle$ is the core of $\mathcal U_S$, and $A$ is the given set. Write $A_0 = A$ and $A_1 = \overline A$. By :ref{#prop-cohesive-core}, $\mathcal U$ is a non-trivial partition regular class, contained in $\mathcal U_S$; so it contains only infinite sets, and is closed under finite changes (:ref{#lem-partition-regular-basic}).

$\mathcal M$ is the ideal of the tests: the $\Sigma^0_1(\mathcal M)$ classes measure largeness, and its Scott property provides witnesses of non-largeness. Its code is low, so that largeness is $\Pi^0_1$ relative to $S \oplus M' \in \mathcal N$. $\mathcal N$ is the ideal of the reservoirs; it avoids the cone above $C$, which is where $C \not\leq_T \emptyset'$ is used.

## Conditions and validity

As in :ref{to="avoidance/seetapun-forcing"}, a string is identified with the finite set of its positions with value $1$. A string $\tau$ is **compatible** with a pair $(\sigma, X)$ if $\sigma \preceq \tau$ and every $x$ with $|\sigma| \leq x < |\tau|$ and $\tau(x) = 1$ is in $X$ (:ref{#def-mathias-condition}); this makes sense for any set $X$.

:::definition{#def-pigeon-condition}
A **condition** is a triple $(\sigma_0, \sigma_1, X)$ such that $\sigma_0 \subseteq A_0$ and $\sigma_1 \subseteq A_1$ as finite sets, $X \in \mathcal N \cap \mathcal U$, and $\min X \geq |\sigma_0|, |\sigma_1|$. A condition $(\tau_0, \tau_1, Y)$ **extends** $(\sigma_0, \sigma_1, X)$ if $Y \subseteq X$ and $\tau_i$ is compatible with $(\sigma_i, X)$ for each $i < 2$. The **members of side $i$** of $(\sigma_0, \sigma_1, X)$ are the sets $G$ with $\sigma_i \prec G$ whose elements larger than or equal to $|\sigma_i|$ belong to $X$.
:::

A condition $(\sigma_0, \sigma_1, X)$ is a pair of Mathias conditions $(\sigma_0, X)$ and $(\sigma_1, X)$ with a common reservoir. Since $\mathcal N$ and $\mathcal U$ are closed under finite changes, $X \setminus \{0, \dots, n\}$ is again an admissible reservoir. The triple $(\varepsilon, \varepsilon, \nat)$ is a condition, since $\nat \in \mathcal U$ by largeness and $\nat \in \mathcal N$. A condition **forces** a sentence of level $1$ **on side $i$** if all its members of side $i$ satisfy it.

The two sides may not both lead to infinite sets: if $A$ is finite, the stem on side $0$ never grows beyond $A$. Dzhafarov and Jockusch first assume that no reservoir has a finite intersection with $A_0$ or $A_1$; here the intersections are compared with the class $\mathcal U$.

:::definition{#def-valid-part}
Side $i$ of a condition $(\sigma_0, \sigma_1, X)$ is **valid** if $X \cap A_i \in \mathcal U$.
:::

:::lemma{#lem-valid-part}
1. Every condition has a valid side.
2. If $q$ extends $p$ and side $i$ of $q$ is valid, then side $i$ of $p$ is valid.
3. If $(\tau_0, \tau_1, Y)$ extends $(\sigma_0, \sigma_1, X)$ with $Y$ differing from $X$ on finitely many elements, the two conditions have the same valid sides.
4. If side $i$ of $(\sigma_0, \sigma_1, X)$ is valid, there is an extension with the same valid sides, whose stem on side $i$ has more elements than $\sigma_i$, the other stem being unchanged.
:::

:::proof{of=lem-valid-part}
1. The sets $X \cap A_0$ and $X \cap A_1$ cover $X \in \mathcal U$, and $\mathcal U$ is partition regular.
2. If $q = (\tau_0, \tau_1, Y)$, then $Y \cap A_i \subseteq X \cap A_i$, and $\mathcal U$ is upward closed.
3. $Y \cap A_i$ and $X \cap A_i$ differ on finitely many elements, and $\mathcal U$ is closed under finite changes.
4. $X \cap A_i$ belongs to $\mathcal U$, so it is infinite; let $x$ be one of its elements. Add $x$ to $\sigma_i$, giving a string $\tau_i$ of length $x + 1$ compatible with $(\sigma_i, X)$, and replace $X$ by $X \setminus \{0, \dots, x\}$. This is a condition, since $x \in A_i$, and item 3 applies.
:::

By item 2, validity can only be lost along a decreasing sequence of conditions: side $i$ stays valid forever, or is invalid from some point on; by item 1, at least one side stays valid.

:::figure[A condition $(\sigma_0, \sigma_1, X)$. The stems are finite subsets of $A$ and of $\overline A$; the reservoir $X$ belongs to the core $\mathcal U$ and to the ideal $\mathcal N$. Its elements are split by $A$ into $X \cap A_0$ and $X \cap A_1$, which cover $X$, so at least one of them belongs to $\mathcal U$: that side is valid. Elements of $X \cap A_i$ can be added to the stem on side $i$.]
<svg class="fig" viewBox="0 0 600 266" width="600" role="img" aria-label="A condition with two stems, a subset of A and a subset of its complement, and a common reservoir X; the reservoir is split by A into the parts X intersected with A0 and with A1"><text x="70.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="112.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="154.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="196.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="238.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="280.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="322.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="364.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="406.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="448.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">18</text><text x="490.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">20</text><text x="532.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">22</text><text x="50" y="48" text-anchor="end" class="math" font-size="14">A</text><rect x="60" y="34" width="21" height="20" class="cell head-cell"/><rect x="81" y="34" width="21" height="20" class="cell"/><rect x="102" y="34" width="21" height="20" class="cell head-cell"/><rect x="123" y="34" width="21" height="20" class="cell head-cell"/><rect x="144" y="34" width="21" height="20" class="cell"/><rect x="165" y="34" width="21" height="20" class="cell head-cell"/><rect x="186" y="34" width="21" height="20" class="cell"/><rect x="207" y="34" width="21" height="20" class="cell"/><rect x="228" y="34" width="21" height="20" class="cell head-cell"/><rect x="249" y="34" width="21" height="20" class="cell head-cell"/><rect x="270" y="34" width="21" height="20" class="cell"/><rect x="291" y="34" width="21" height="20" class="cell head-cell"/><rect x="312" y="34" width="21" height="20" class="cell head-cell"/><rect x="333" y="34" width="21" height="20" class="cell"/><rect x="354" y="34" width="21" height="20" class="cell head-cell"/><rect x="375" y="34" width="21" height="20" class="cell head-cell"/><rect x="396" y="34" width="21" height="20" class="cell"/><rect x="417" y="34" width="21" height="20" class="cell head-cell"/><rect x="438" y="34" width="21" height="20" class="cell head-cell"/><rect x="459" y="34" width="21" height="20" class="cell"/><rect x="480" y="34" width="21" height="20" class="cell head-cell"/><rect x="501" y="34" width="21" height="20" class="cell"/><rect x="522" y="34" width="21" height="20" class="cell head-cell"/><rect x="543" y="34" width="21" height="20" class="cell head-cell"/><text x="50" y="90" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">₀</tspan></text><rect x="60" y="76" width="21" height="20" class="cell"/><text x="70.5" y="90" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="81" y="76" width="21" height="20" class="cell"/><text x="91.5" y="90" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="102" y="76" width="21" height="20" class="cell"/><text x="112.5" y="90" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="123" y="76" width="21" height="20" class="cell"/><text x="133.5" y="90" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="144" y="76" width="21" height="20" class="cell"/><text x="154.5" y="90" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="165" y="76" width="21" height="20" class="cell"/><text x="175.5" y="90" text-anchor="middle" class="mrm" font-size="11">0</text><text x="50" y="120" text-anchor="end" class="math" font-size="14">σ<tspan class="mrm" font-size="10" dy="3">₁</tspan></text><rect x="60" y="106" width="21" height="20" class="cell"/><text x="70.5" y="120" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="81" y="106" width="21" height="20" class="cell"/><text x="91.5" y="120" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="102" y="106" width="21" height="20" class="cell"/><text x="112.5" y="120" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="123" y="106" width="21" height="20" class="cell"/><text x="133.5" y="120" text-anchor="middle" class="mrm" font-size="11">0</text><rect x="144" y="106" width="21" height="20" class="cell"/><text x="154.5" y="120" text-anchor="middle" class="mrm" font-size="11">1</text><rect x="165" y="106" width="21" height="20" class="cell"/><text x="175.5" y="120" text-anchor="middle" class="mrm" font-size="11">0</text><text x="50" y="164" text-anchor="end" class="label">X</text><line x1="186" y1="160" x2="564" y2="160" class="axis"/><circle cx="196.5" cy="160" r="4.5" class="ink-fill"/><circle cx="238.5" cy="160" r="4.5" class="ink-fill"/><circle cx="259.5" cy="160" r="4.5" class="ink-fill"/><circle cx="280.5" cy="160" r="4.5" class="ink-fill"/><circle cx="322.5" cy="160" r="4.5" class="ink-fill"/><circle cx="343.5" cy="160" r="4.5" class="ink-fill"/><circle cx="385.5" cy="160" r="4.5" class="ink-fill"/><circle cx="406.5" cy="160" r="4.5" class="ink-fill"/><circle cx="427.5" cy="160" r="4.5" class="ink-fill"/><circle cx="469.5" cy="160" r="4.5" class="ink-fill"/><circle cx="490.5" cy="160" r="4.5" class="ink-fill"/><circle cx="511.5" cy="160" r="4.5" class="ink-fill"/><circle cx="553.5" cy="160" r="4.5" class="ink-fill"/><text x="570" y="165" class="mrm muted" font-size="13">⋯</text><text x="50" y="190" text-anchor="end" class="label">X ∩ A₀</text><line x1="186" y1="186" x2="564" y2="186" class="axis"/><circle cx="238.5" cy="186" r="4.5" class="accent-fill"/><circle cx="259.5" cy="186" r="4.5" class="accent-fill"/><circle cx="322.5" cy="186" r="4.5" class="accent-fill"/><circle cx="385.5" cy="186" r="4.5" class="accent-fill"/><circle cx="427.5" cy="186" r="4.5" class="accent-fill"/><circle cx="490.5" cy="186" r="4.5" class="accent-fill"/><circle cx="553.5" cy="186" r="4.5" class="accent-fill"/><text x="570" y="191" class="mrm muted" font-size="13">⋯</text><text x="50" y="216" text-anchor="end" class="label">X ∩ A₁</text><line x1="186" y1="212" x2="564" y2="212" class="axis"/><circle cx="196.5" cy="212" r="4.5" class="ink-fill"/><circle cx="280.5" cy="212" r="4.5" class="ink-fill"/><circle cx="343.5" cy="212" r="4.5" class="ink-fill"/><circle cx="406.5" cy="212" r="4.5" class="ink-fill"/><circle cx="469.5" cy="212" r="4.5" class="ink-fill"/><circle cx="511.5" cy="212" r="4.5" class="ink-fill"/><text x="570" y="217" class="mrm muted" font-size="13">⋯</text><line x1="186" y1="70" x2="186" y2="220" class="ink-stroke" stroke-width="1" stroke-dasharray="4 3"/><text x="300" y="248" text-anchor="middle" class="label">shaded cells: elements of A; σ₀ ⊆ A₀ = A, σ₁ ⊆ A₁ = Aᶜ; side i is valid if X ∩ Aᵢ ∈ 𝒰</text></svg>
:::

:::quiz[validity]
Why does item 1 of :ref{#lem-valid-part} need the partition regularity of $\mathcal U$, and not only its largeness?

- [x] Because $X \cap A_0$ and $X \cap A_1$ cover $X$, not $\nat$; largeness concerns covers of $\nat$ only.
- [ ] Because $\mathcal U$ must contain only infinite sets.

  Non-triviality is used in item 4, to find a new element.
- [ ] Because $A$ is arbitrary.

  The argument works for every set $A$; what matters is the kind of cover.

---

In item 4, why does the new condition have the same valid sides?

- [x] Because its reservoir differs from $X$ on finitely many elements, and $\mathcal U$ is closed under finite changes, being non-trivial and partition regular.
- [ ] Because $x \in A_i$.

  This makes the new stem a subset of $A_i$; validity concerns the reservoir.
- [ ] Because the other stem is unchanged.

  Validity does not depend on the stems.
:::

## The question for Σ⁰₁ sentences

A $\Sigma^0_1$ sentence is $\varphi = \Phi^G_e(\vec m)\converge$, and a string $\tau$ **satisfies** it if $\Phi^\tau_e(\vec m)$ converges with all oracle queries below $|\tau|$. For a string $\sigma$ and a $\Sigma^0_1$ sentence $\varphi$, let
$$
\mathcal V_{\sigma, \varphi} = \{ Y : \text{some string compatible with } (\sigma, Y) \text{ satisfies } \varphi \}.
$$
It is an upward closed $\Sigma^0_1$ class, with an index computable from $\sigma$ and $\varphi$, hence a $\Sigma^0_1(\mathcal M)$ class.

:::definition{#def-pigeon-sigma1}
For a string $\sigma$ and a $\Sigma^0_1$ sentence $\varphi$, let $\sigma \mathrel{?{\vdash}} \varphi$ if $\mathcal U_S \cap \mathcal V_{\sigma, \varphi}$ is large.
:::

The question is asked about a stem alone, independently of the reservoir and of $A$, so it serves on both sides. By :ref{#prop-largeness-complexity}, the relation $\sigma \mathrel{?{\vdash}} \varphi$ is $\Pi^0_1(S \oplus M')$, uniformly in $\sigma$ and $\varphi$, and $S \oplus M' \in \mathcal N$.

:::lemma{#lem-pigeon-sigma1}
Let $p = (\sigma_0, \sigma_1, X)$ be a condition, $i < 2$, and $\varphi$ a $\Sigma^0_1$ sentence.

1. If side $i$ of $p$ is valid and $\sigma_i \mathrel{?{\vdash}} \varphi$, there is an extension of $p$, with the same valid sides, that forces $\varphi$ on side $i$, the stem on side $1 - i$ being unchanged.
2. If $\sigma_i \mathrel{?{\nvdash}} \varphi$, there is an extension $(\sigma_0, \sigma_1, Y)$ of $p$, with the same stems, such that no string compatible with $(\sigma_i, Y)$ satisfies $\varphi$; it forces $\neg\varphi$ on side $i$.
:::

:::proof{of=lem-pigeon-sigma1}
Write $\mathcal V = \mathcal V_{\sigma_i, \varphi}$.

1. Since $\mathcal U_S \cap \mathcal V$ is large, $\mathcal U \subseteq \mathcal V$ by item 2 of :ref{#prop-cohesive-core}. Side $i$ is valid, so $X \cap A_i \in \mathcal U \subseteq \mathcal V$: some string $\tau$ compatible with $(\sigma_i, X \cap A_i)$ satisfies $\varphi$. Its new elements are in $X \cap A_i$, so $\tau \subseteq A_i$. Let $\tau_i = \tau$, $\tau_{1-i} = \sigma_{1-i}$, and $Y = X \setminus \{0, \dots, |\tau| - 1\}$. Then $(\tau_0, \tau_1, Y)$ is a condition extending $p$, with the same valid sides by :ref{#lem-valid-part}. Every member of side $i$ extends $\tau$, so it satisfies $\varphi$ by the use principle.
2. The class $\mathcal U_S \cap \mathcal V$ is not large. By :ref{#prop-largeness-complexity}, there is a finite $F \subseteq S$ such that $\mathcal U_F \cap \mathcal V$ is not large. It is an upward closed $\Sigma^0_1(W)$ class for some $W \in \mathcal M$. As in the proof of :ref{#lem-cohesive-compatible}, the Scott property of $\mathcal M$ gives a partition $W_0, \dots, W_{k-1} \in \mathcal M$ of $\nat$ none of whose parts is in $\mathcal U_F \cap \mathcal V$. The sets $X \cap W_j$ cover $X \in \mathcal U$, so some $Y = X \cap W_j$ is in $\mathcal U$, by partition regularity. Then $W_j \in \mathcal U \subseteq \mathcal U_S \subseteq \mathcal U_F$, so $W_j \notin \mathcal V$. The set $Y$ is in $\mathcal N$, since $X \in \mathcal N$ and $W_j \in \mathcal M \subseteq \mathcal N$, and it is contained in $X$; so $(\sigma_0, \sigma_1, Y)$ is a condition extending $p$. A string compatible with $(\sigma_i, Y)$ is compatible with $(\sigma_i, W_j)$, so it does not satisfy $\varphi$, since $W_j \notin \mathcal V$. Finally, if a member $G$ of side $i$ satisfied $\varphi$, with use $u$, the prefix of $G$ of length $\max(u, |\sigma_i|)$ would be a string compatible with $(\sigma_i, Y)$ satisfying $\varphi$.
:::

The two cases are asymmetric. A positive answer is useful only on a valid side, which puts $X \cap A_i$ in $\mathcal U$. A negative answer is useful on every side, but it may lose validity, since the new reservoir is a part of $X$. So the question is not a forcing question in the sense of :ref{#def-forcing-question}, nor $\Sigma^0_1$-preserving: the reservoirs cannot be searched through, and the question replaces the search by the largeness of a class of possible reservoirs, a $\Pi^0_1(S \oplus M')$ property.

:::quiz[the question for Σ⁰₁ sentences]
In item 1 of :ref{#lem-pigeon-sigma1}, where is the cohesiveness of $\mathcal U_S$ used?

- [x] In the step $\mathcal U \subseteq \mathcal V$: the core of the cohesive class $\mathcal U_S$ is contained in every $\Sigma^0_1(\mathcal M)$ class meeting $\mathcal U_S$ largely, so $X \cap A_i \in \mathcal V$.
- [ ] In the step $\tau \subseteq A_i$.

  This only uses that the new elements of $\tau$ come from $X \cap A_i$.
- [ ] To show that the new reservoir is in $\mathcal N$.

  This uses closure of $\mathcal N$ under finite changes.

---

In item 2, why is the new reservoir $X \cap W_j$ rather than $W_j$?

- [x] Because an extension must have its reservoir contained in $X$; the partition regularity of $\mathcal U$, applied to the cover of $X$ by the sets $X \cap W_j$, gives a part in $\mathcal U$.
- [ ] Because $W_j$ is not in $\mathcal N$.

  It is, since $\mathcal M \subseteq \mathcal N$.
- [ ] Because $W_j$ is not in $\mathcal U$.

  If $X \cap W_j \in \mathcal U$, then $W_j \in \mathcal U$ by upward closure.

---

Why does item 2 not require side $i$ to be valid?

- [x] Because the extension forces $\neg\varphi$ on side $i$ through its reservoir: no string compatible with $(\sigma_i, Y)$ satisfies $\varphi$, whatever $A$ is.
- [ ] Because $\sigma_i \mathrel{?{\nvdash}} \varphi$ implies that side $i$ is valid.

  The question does not depend on the reservoir or on $A$, so it says nothing about validity.
- [ ] Because the new condition has both sides valid.

  Its valid sides may differ from those of $p$.
:::

## Notes and references

The two Scott ideals, the notion of forcing, validity and the question for $\Sigma^0_1$ sentences follow the section *Pigeonhole principle* of the chapter *Jump cone avoidance* of Patey's monograph. Its definition of validity is written with $\mathcal U_S$; the proofs use the core, as here. Monin and Patey (2019) introduced largeness and partition regularity to prove the theorem; the cohesive class fixed in advance comes from the later work of Monin and Patey on hyperarithmetical reductions and of Le Houérou, Levy Patey and Mimouni (2024). The underlying forcing is that of Dzhafarov and Jockusch (2009), presented in :ref{to="ramsey-theorem/cone-avoidance"} and, as a disjunctive notion of forcing, in :ref{to="avoidance/disjunctive-question"}.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Pigeonhole principle*.
