---
title: The core of a cohesive class
summary: The core of a cohesive class is partition regular and minimal; a set PA relative to the jump of the code computes a cohesive class.
duration: 45
prerequisites: [largeness, lowness/beyond-zero-jump]
---

The forcing for the pigeonhole principle uses reservoirs in a fixed partition regular class $\mathcal U$, the **core** of a cohesive class $\mathcal U_S$ (:ref{#def-cohesive-class}), the intersection of the $\Sigma^0_1(\mathcal M)$ classes that meet $\mathcal U_S$ largely. The second section shows that a set PA relative to the jump of the code computes such a set of indices $S$. Throughout, $\mathcal M$ is a Scott ideal coded by $M = \bigoplus_i Z_i$, and $\mathcal U_S$ and the $\Sigma^0_1(\mathcal M)$ classes are as in :ref{to="jump-cone-avoidance/largeness"}.

## The core of a cohesive class

:::definition{#def-cohesive-core}
Let $\mathcal U_S$ be $\mathcal M$-cohesive. Its **core** is the class
$$
\langle \mathcal U_S \rangle = \bigcap \{ \mathcal V : \mathcal V \text{ a } \Sigma^0_1(\mathcal M) \text{ class with } \mathcal U_S \cap \mathcal V \text{ large} \}.
$$
:::

:::proposition{#prop-cohesive-core}
Let $\mathcal U_S$ be $\mathcal M$-cohesive, and $\mathcal U = \langle \mathcal U_S \rangle$.

1. $\mathcal U \subseteq \mathcal U_S$, and $\mathcal U$ is large.
2. For every $\Sigma^0_1(\mathcal M)$ class $\mathcal V$: if $\mathcal U_S \cap \mathcal V$ is large, then $\mathcal U \subseteq \mathcal V$; otherwise $\mathcal U \cap \mathcal V$ is not large.
3. If $X \notin \mathcal U$, there is a $\Sigma^0_1(\mathcal M)$ class $\mathcal V \supseteq \mathcal U$ with $X \notin \mathcal V$.
4. $\mathcal U$ is partition regular. If all members of $\mathcal U_S$ are infinite, $\mathcal U$ is non-trivial.
:::

:::proof{of=prop-cohesive-core}
1. For $(e, i) \in S$, the class $\mathcal V = \mathcal U^{Z_i}_e$ satisfies $\mathcal U_S \cap \mathcal V = \mathcal U_S$, which is large; so $\mathcal U \subseteq \mathcal U_S$. Let $\mathcal V_0, \mathcal V_1, \dots$ enumerate the $\Sigma^0_1(\mathcal M)$ classes with $\mathcal U_S \cap \mathcal V_n$ large; there are countably many, given by pairs $(e, i)$. By induction on $n$, $\mathcal U_S \cap \mathcal V_0 \cap \dots \cap \mathcal V_n$ is large: the class $\mathcal V_0 \cap \dots \cap \mathcal V_{n-1}$ is a $\Sigma^0_1(\mathcal M)$ class, and :ref{#lem-cohesive-compatible} applies to it and $\mathcal V_n$. These classes decrease, and their intersection is $\mathcal U_S \cap \mathcal U = \mathcal U$, which is large by :ref{#lem-decreasing-large}.
2. The first case is the definition. In the second case, $\mathcal U \cap \mathcal V \subseteq \mathcal U_S \cap \mathcal V$, and a subclass of a non-large class is not large.
3. By definition of the intersection, some $\mathcal V$ of the family does not contain $X$, and $\mathcal U \subseteq \mathcal V$.
4. $\mathcal U$ is non-empty and upward closed. Let $X \in \mathcal U$ and let $Y_0, Y_1$ cover $X$. Suppose $Y_0, Y_1 \notin \mathcal U$. By item 3, there are $\Sigma^0_1(\mathcal M)$ classes $\mathcal V_0, \mathcal V_1 \supseteq \mathcal U$ with $Y_0 \notin \mathcal V_0$ and $Y_1 \notin \mathcal V_1$; by item 2, $\mathcal U_S \cap \mathcal V_0$ and $\mathcal U_S \cap \mathcal V_1$ are large, since they contain the large class $\mathcal U$. By :ref{#lem-cohesive-compatible}, the class $\mathcal A = \mathcal U_S \cap \mathcal V_0 \cap \mathcal V_1$ is large. By :ref{#prop-largest-partition-regular}, $\mathcal L(\mathcal A)$ is partition regular and contained in $\mathcal A$; it is contained in $\mathcal L_2(\mathcal V_0 \cap \mathcal V_1)$, since every $2$-cover of a member of $\mathcal L(\mathcal A)$ has a part in $\mathcal A \subseteq \mathcal V_0 \cap \mathcal V_1$. So $\mathcal U_S \cap \mathcal L_2(\mathcal V_0 \cap \mathcal V_1)$ contains the large class $\mathcal L(\mathcal A)$, and is large. The class $\mathcal L_2(\mathcal V_0 \cap \mathcal V_1)$ is $\Sigma^0_1(\mathcal M)$ by :ref{#lem-cover-class}, so $\mathcal U \subseteq \mathcal L_2(\mathcal V_0 \cap \mathcal V_1)$ by item 2. As $X \in \mathcal U$, one of $Y_0, Y_1$ is in $\mathcal V_0 \cap \mathcal V_1$, which contradicts the choice of $\mathcal V_0$ and $\mathcal V_1$. The last statement holds since $\mathcal U \subseteq \mathcal U_S$.
:::

Item 2 says that $\mathcal U$ is **$\mathcal M$-minimal**. It is the only large subclass of $\mathcal U_S$ with this property that is an intersection of $\Sigma^0_1(\mathcal M)$ classes. Let $\mathcal U' = \bigcap_j \mathcal V'_j$ be another one. Each $\mathcal U_S \cap \mathcal V'_j$ contains $\mathcal U'$ and is large, so $\mathcal U \subseteq \mathcal U'$. If $\mathcal U_S \cap \mathcal V$ is large, the compatibility lemma and :ref{#lem-decreasing-large} show, as in item 1, that $\mathcal U_S \cap \mathcal U' \cap \mathcal V = \mathcal U' \cap \mathcal V$ is large, so $\mathcal U' \subseteq \mathcal V$ by minimality of $\mathcal U'$; hence $\mathcal U' \subseteq \mathcal U$. This uniqueness is not used below. The constructions never compute indices of the core, only $S$: the questions of the forcing are asked about $\mathcal U_S$, whose largeness properties are $\Pi^0_1(S \oplus M')$, and the core appears only in the proofs.

:::quiz[the core]
In item 4 of the proof of :ref{#prop-cohesive-core}, why is the class $\mathcal L_2(\mathcal V_0 \cap \mathcal V_1)$ introduced?

- [x] Because it is a $\Sigma^0_1(\mathcal M)$ class, so item 2 applies to it, and its members are exactly the sets every $2$-cover of which has a part in $\mathcal V_0 \cap \mathcal V_1$; so $X \in \mathcal U$ yields a part of the cover in both classes.
- [ ] Because $\mathcal L(\mathcal A)$ is not large.

  It is large, being partition regular.
- [ ] Because $\mathcal V_0 \cap \mathcal V_1$ is not $\Sigma^0_1(\mathcal M)$.

  It is; but membership of $X$ in it says nothing about the parts of a cover of $X$.

---

Why is item 1 not a consequence of :ref{#lem-decreasing-large} alone?

- [x] Because the classes $\mathcal U_S \cap \mathcal V_0 \cap \dots \cap \mathcal V_n$ must first be shown to be large, which uses the compatibility lemma, hence cohesiveness; the lemma on decreasing sequences then passes to the intersection.
- [ ] Because the family of classes $\mathcal V$ is uncountable.

  It is countable.
- [ ] Because $\mathcal U_S$ is not large.

  It is large by definition of an $\mathcal M$-cohesive class.
:::

## Computing a cohesive class

:::lemma{#lem-large-split}
Let $\mathcal A$ be a large class all of whose members are infinite, and $X$ a set. Then $\mathcal A \cap \mathcal L_X$ or $\mathcal A \cap \mathcal L_{\overline X}$ is large.
:::

:::proof{of=lem-large-split}
Both classes are upward closed. Suppose neither is large: there are a finite cover $(Y_j)_{j < k}$ of $\nat$ with no part in $\mathcal A \cap \mathcal L_X$, and a finite cover $(W_l)_{l < m}$ with no part in $\mathcal A \cap \mathcal L_{\overline X}$. The sets $Y_j \cap X$ and $W_l \cap \overline X$ cover $\nat$, so one of them is in $\mathcal A$. If $Y_j \cap X \in \mathcal A$, then $Y_j \in \mathcal A$, so $Y_j \notin \mathcal L_X$: the set $Y_j \cap X$ is finite, and a finite set belongs to $\mathcal A$, which is excluded. The case $W_l \cap \overline X \in \mathcal A$ is symmetric.
:::

A set PA relative to $W$ uniformly chooses a true sentence among two $\Pi^0_1(W)$ sentences, not both false: this is :ref{#lem-pa-choice} one level down and relativized to $W$.

:::theorem{#thm-cohesive-class}
Let $S_0 \subseteq \nat^2$ be such that $\mathcal U_{S_0}$ is large and all its members are infinite, and let $P$ be PA relative to $S_0 \oplus M'$. There is a $P$-computable set $S \supseteq S_0$ such that $\mathcal U_S$ is $\mathcal M$-cohesive and all its members are infinite.
:::

:::proof{of=thm-cohesive-class}
For each $i$, $\mathcal L_{Z_i} = \bigcap_n \{ X : |X \cap Z_i| \geq n \}$ is an intersection of upward closed $\Sigma^0_1(Z_i)$ classes, with indices computable from $n$. So there are computable sets $E_i$ and $F_i$ of pairs, uniformly in $i$, with $\mathcal U_{E_i} = \mathcal L_{Z_i}$ and $\mathcal U_{F_i} = \mathcal L_{\overline{Z_i}}$; by padding the indices, we may assume that all elements of $E_i$ and $F_i$, coded as numbers, are at least $i$.

Define $S_0 \subseteq S_1 \subseteq \cdots$ with $\mathcal U_{S_k}$ large, as follows. Given $S_k$, at least one of the classes $\mathcal U_{S_k} \cap \mathcal L_{Z_k}$ and $\mathcal U_{S_k} \cap \mathcal L_{\overline{Z_k}}$ is large by :ref{#lem-large-split}, since the members of $\mathcal U_{S_k} \subseteq \mathcal U_{S_0}$ are infinite. These classes are $\mathcal U_{S_k \cup E_k}$ and $\mathcal U_{S_k \cup F_k}$, and their largeness is $\Pi^0_1(S_0 \oplus M')$ by :ref{#prop-largeness-complexity}, uniformly in $k$, since $S_k$ is $S_0$ together with finitely many sets $E_j$ and $F_j$. Let $S_{k+1} = S_k \cup E_k$ or $S_{k+1} = S_k \cup F_k$, according to the choice made by $P$ between the two sentences.

Let $S = \bigcup_k S_k$. The sequence of choices is $P$-computable. A number $a$ belongs to $S$ if and only if it belongs to $S_{a+1}$, since the sets added after step $a$ only contain numbers larger than $a$; and $S_{a+1}$ is computable from $S_0$, which $P$ computes, and the first $a + 1$ choices. So $S \leq_T P$. The classes $\mathcal U_{S_k}$ are large and decrease, with intersection $\mathcal U_S$, so $\mathcal U_S$ is large by :ref{#lem-decreasing-large}, and its members are infinite. For every $k$, $\mathcal U_S \subseteq \mathcal U_{S_{k+1}}$, which is contained in $\mathcal L_{Z_k}$ or in $\mathcal L_{\overline{Z_k}}$. So $\mathcal U_S$ is $\mathcal M$-cohesive.
:::

A starting set $S_0$ is given by the pairs $(a_n, 0)$, $n \in \nat$, where $a_n$ is an index with $\mathcal U^Y_{a_n} = \{ X : |X| \geq n \}$ for every oracle $Y$; then $\mathcal U_{S_0}$ is the class of infinite sets, and $S_0$ is computable. If $M$ is low, a set PA relative to $\emptyset'$ is PA relative to $M'$, and computes such a class.

:::figure[The construction of :ref{#thm-cohesive-class}. At step $k$, the class $\mathcal U_{S_k}$ is intersected with $\mathcal L_{Z_k}$ or with $\mathcal L_{\overline{Z_k}}$; at least one intersection is large, and the set $P$ chooses one of them. The resulting decreasing sequence determines an $\mathcal M$-cohesive class $\mathcal U_S$, and its core $\langle \mathcal U_S \rangle$, which is partition regular.]
<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="A decreasing sequence of classes U_S0, U_S1, and so on; at step k the class is intersected with L of Z_k or L of the complement of Z_k, the set P choosing a large intersection"><defs><marker id="jc-cc-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><rect x="14" y="70" width="64" height="40" rx="6" class="cell"/><text x="46.0" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S₀</tspan></text><line x1="80" y1="90" x2="110" y2="90" class="muted-stroke" stroke-width="1.2" marker-end="url(#jc-cc-arr)"/><text x="95.0" y="40" text-anchor="middle" class="label">𝓛<tspan font-size="9" dy="3">Z₀</tspan></text><text x="95.0" y="146" text-anchor="middle" class="label muted">𝓛<tspan font-size="9" dy="3">Z₀ᶜ</tspan></text><circle cx="95.0" cy="52" r="4" class="accent-fill"/><rect x="112" y="70" width="64" height="40" rx="6" class="cell"/><text x="144.0" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S₁</tspan></text><line x1="178" y1="90" x2="208" y2="90" class="muted-stroke" stroke-width="1.2" marker-end="url(#jc-cc-arr)"/><text x="193.0" y="40" text-anchor="middle" class="label muted">𝓛<tspan font-size="9" dy="3">Z₁</tspan></text><text x="193.0" y="146" text-anchor="middle" class="label">𝓛<tspan font-size="9" dy="3">Z₁ᶜ</tspan></text><circle cx="193.0" cy="128" r="4" class="accent-fill"/><rect x="210" y="70" width="64" height="40" rx="6" class="cell"/><text x="242.0" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S₂</tspan></text><line x1="276" y1="90" x2="306" y2="90" class="muted-stroke" stroke-width="1.2" marker-end="url(#jc-cc-arr)"/><text x="291.0" y="40" text-anchor="middle" class="label">𝓛<tspan font-size="9" dy="3">Z₂</tspan></text><text x="291.0" y="146" text-anchor="middle" class="label muted">𝓛<tspan font-size="9" dy="3">Z₂ᶜ</tspan></text><circle cx="291.0" cy="52" r="4" class="accent-fill"/><rect x="308" y="70" width="64" height="40" rx="6" class="cell"/><text x="340.0" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S₃</tspan></text><line x1="374" y1="90" x2="404" y2="90" class="muted-stroke" stroke-width="1.2" marker-end="url(#jc-cc-arr)"/><text x="389.0" y="40" text-anchor="middle" class="label">𝓛<tspan font-size="9" dy="3">Z₃</tspan></text><text x="389.0" y="146" text-anchor="middle" class="label muted">𝓛<tspan font-size="9" dy="3">Z₃ᶜ</tspan></text><circle cx="389.0" cy="52" r="4" class="accent-fill"/><rect x="406" y="70" width="64" height="40" rx="6" class="cell"/><text x="438.0" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S₄</tspan></text><line x1="472" y1="90" x2="502" y2="90" class="muted-stroke" stroke-width="1.2" marker-end="url(#jc-cc-arr)"/><text x="487.0" y="40" text-anchor="middle" class="label muted">𝓛<tspan font-size="9" dy="3">Z₄</tspan></text><text x="487.0" y="146" text-anchor="middle" class="label">𝓛<tspan font-size="9" dy="3">Z₄ᶜ</tspan></text><circle cx="487.0" cy="128" r="4" class="accent-fill"/><rect x="504" y="70" width="64" height="40" rx="6" class="head-cell"/><text x="536.0" y="95" text-anchor="middle" class="math" font-size="14">𝒰<tspan class="mrm" font-size="10" dy="3">S₅</tspan></text><text x="300" y="180" text-anchor="middle" class="label">at each step, P chooses a class whose intersection with the current one is large (dot)</text><text x="300" y="200" text-anchor="middle" class="label">Zᶜ is the complement of Z; the intersection of the sequence is 𝓜-cohesive</text></svg>
:::

:::quiz[computing a cohesive class]
In the proof of :ref{#thm-cohesive-class}, why is a set PA relative to $S_0 \oplus M'$ enough, while deciding the largeness of the classes would need $(S_0 \oplus M')'$?

- [x] Because the construction never needs to know whether a class is large: it only needs to name one of two classes that is large, when one of them is known to be, and choosing a true sentence among two $\Pi^0_1(S_0 \oplus M')$ sentences is what a PA set relative to $S_0 \oplus M'$ does.
- [ ] Because the classes $\mathcal L_{Z_k}$ are partition regular.

  This is not used; :ref{#lem-large-split} only uses that the members of $\mathcal U_{S_k}$ are infinite.
- [ ] Because $P$ computes $M''$.

  A set PA relative to $M'$ need not compute $M''$; it can even be low relative to $M'$.

---

Why are the elements of $E_i$ and $F_i$ taken at least $i$?

- [x] So that whether a number $a$ is in $S$ is settled by $S_{a+1}$; then $S$ is computable in $P$, and not only the limit of a $P$-computable sequence.
- [ ] So that the classes $\mathcal U_{S_k}$ are large.

  Largeness comes from the choices made by $P$.
- [ ] So that $\mathcal U_S$ is cohesive.

  Cohesiveness comes from the choice at each step; padding concerns the computation of $S$.
:::

## Exercises

::::exercise{difficulty=1}
Let $\mathcal A$ be $\mathcal M$-cohesive. Show that for $X \in \mathcal M$, $X \in \mathcal A$ if and only if $\mathcal A \subseteq \mathcal L_X$, and deduce that $\{ X \in \mathcal M : X \in \mathcal A \}$ is an ultrafilter on the Boolean algebra $\mathcal M$ containing no finite set, provided all members of $\mathcal A$ are infinite.

:::solution
If $\mathcal A \subseteq \mathcal L_X$, then $\overline X \notin \mathcal A$, since $\overline X \cap X = \emptyset$; as $\mathcal A$ is large, $X$ or $\overline X$ is in $\mathcal A$, so $X \in \mathcal A$. If $X \in \mathcal A$, then $\mathcal A \not\subseteq \mathcal L_{\overline X}$, so $\mathcal A \subseteq \mathcal L_X$ by cohesiveness.

Let $\mathcal F = \mathcal A \cap \mathcal M$. It is closed under supersets in $\mathcal M$, and for every $X \in \mathcal M$ exactly one of $X$ and $\overline X$ is in $\mathcal F$: at least one by largeness, and not both by the first part. If $X, Y \in \mathcal F$, the sets $X \cap Y$, $\overline X$ and $\overline Y$ cover $\nat$, so one of them is in $\mathcal A$; it is not $\overline X$ or $\overline Y$, so $X \cap Y \in \mathcal F$. So $\mathcal F$ is an ultrafilter on $\mathcal M$, and it contains no finite set if all members of $\mathcal A$ are infinite.
:::
::::

::::exercise{difficulty=2}
Let $S_0$ be such that $\mathcal U_{S_0}$ is large. Show that $(S_0 \oplus M')'$ computes a set $S \supseteq S_0$ such that $\mathcal U_S$ is $\mathcal M$-minimal in the sense of item 2 of :ref{#prop-cohesive-core}: for every $\Sigma^0_1(\mathcal M)$ class $\mathcal V$, $\mathcal U_S \subseteq \mathcal V$ or $\mathcal U_S \cap \mathcal V$ is not large.

:::solution
Enumerate the $\Sigma^0_1(\mathcal M)$ classes as $\mathcal V_0, \mathcal V_1, \dots$, by pairs $(e, i)$, with padded indices $(e_k, i_k)$ for $\mathcal V_k$ whose code is at least $k$. Let $S_{k+1} = S_k \cup \{ (e_k, i_k) \}$ if $\mathcal U_{S_k} \cap \mathcal V_k$ is large, and $S_{k+1} = S_k$ otherwise. The test is $\Pi^0_1(S_0 \oplus M')$ by :ref{#prop-largeness-complexity}, hence decided by $(S_0 \oplus M')'$, and $S = \bigcup_k S_k$ is computable in $(S_0 \oplus M')'$ by the padding. The classes $\mathcal U_{S_k}$ are large, so $\mathcal U_S$ is large. For each $k$: if $\mathcal U_{S_k} \cap \mathcal V_k$ is large, then $\mathcal U_S \subseteq \mathcal V_k$; otherwise $\mathcal U_S \cap \mathcal V_k \subseteq \mathcal U_{S_k} \cap \mathcal V_k$ is not large.
:::
::::

## Notes and references

$\mathcal M$-minimal classes and the core are due to Monin and Patey (*The weakness of the pigeonhole principle under hyperarithmetical reductions*, arXiv 2019); :ref{#thm-cohesive-class} and the greedy construction of the second exercise are due, according to the monograph, to Le Houérou, Levy Patey and Mimouni (2024), who also show that some $\mathcal M$-cohesive class of the form $\mathcal U_S$ is not $\mathcal M$-minimal. The presentation follows the chapter *Jump cone avoidance* of Patey's monograph. The partition regularity of the core (item 4 of :ref{#prop-cohesive-core}) is proved here directly with :ref{#lem-cover-class}; the monograph obtains it from the fact that the largest partition regular subclass of a class $\mathcal U_S$ is again of the form $\mathcal U_{S'}$, with $S'$ computable in $S$.

- B. Monin and L. Patey, *The weakness of the pigeonhole principle under hyperarithmetical reductions*, arXiv:1905.08425 (2019).
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Partition regularity*.
