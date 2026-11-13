---
title: Largeness over a Scott ideal
summary: Upward closed Σ⁰₁ classes over the members of a coded Scott ideal and their intersections; the largeness of such an intersection is Π⁰₁ relative to the jump of the code; cohesive classes choose a side of every member of the ideal, and are compatible with every Σ⁰₁ class they meet largely.
duration: 45
prerequisites: [partition-regularity, lowness/coded-ideals, big-five/wkl0]
---

The reservoirs of the forcing for the pigeonhole principle will be taken in a partition regular class that is not given by an explicit combinatorial property, but as an intersection of simple classes: upward closed $\Sigma^0_1$ classes relative to the members of a Scott ideal. This lesson studies such intersections. Their largeness is decided one jump above the code of the ideal (:ref{#prop-largeness-complexity}), and an intersection that chooses a side of every member of the ideal, a **cohesive class**, behaves well with respect to further intersections (:ref{#lem-cohesive-compatible}). The next lesson extracts from a cohesive class the partition regular class used by the forcing.

## Effective classes

The classes used in the forcing are intersections of upward closed $\Sigma^0_1$ classes relative to members of a Scott ideal. Identify a finite set $F$ with its canonical code. For a set $Y$ and an index $e$, let
$$
\mathcal U^Y_e = \{ X : F \subseteq X \text{ for some finite } F \in W^Y_e \}.
$$
It is upward closed and $\Sigma^0_1(Y)$. Conversely, every upward closed $\Sigma^0_1(Y)$ class $\mathcal V$ has this form: if $\mathcal V = \{ X : \sigma \prec X \text{ for some } \sigma \in W \}$ with $W$ a $Y$-c.e. set of strings, let $W'$ be the set of finite sets $\{ n < |\sigma| : \sigma(n) = 1 \}$ for $\sigma \in W$. A finite set $F$ obtained from $\sigma \in W$ belongs to $\mathcal V$, since it has the prefix $\sigma$, so every superset of $F$ belongs to $\mathcal V$; and every member $X$ of $\mathcal V$ contains such an $F$.

:::lemma{#lem-cover-class}
Let $\mathcal V$ be an upward closed $\Sigma^0_1(Y)$ class and $k \geq 1$. The class $\mathcal L_k(\mathcal V)$ of sets $X$ all of whose $k$-covers have a part in $\mathcal V$ is upward closed and $\Sigma^0_1(Y)$, with an index computable from $k$ and an index of $\mathcal V$. Moreover $\mathcal L(\mathcal V) = \bigcap_k \mathcal L_k(\mathcal V)$, and "$\mathcal V$ is large" is a $\Pi^0_2(Y)$ property of an index of $\mathcal V$.
:::

:::proof{of=lem-cover-class}
Write $\mathcal V = \mathcal U^Y_e$. Since $\mathcal V$ is upward closed, a $k$-cover of $X$ has a part in $\mathcal V$ for every cover as soon as this holds for the $k$-partitions of $X$, obtained by shrinking the parts. We show that $X \in \mathcal L_k(\mathcal V)$ if and only if there are a finite set $F \subseteq X$ and a stage $s$ such that for every $k$-partition $F_0, \dots, F_{k-1}$ of $F$, some $F_i$ contains a finite set enumerated in $W^Y_e$ by stage $s$. This is a $\Sigma^0_1(Y)$ condition, as there are finitely many partitions of $F$, and the class it defines is upward closed.

If $F$ and $s$ exist, a $k$-partition of $X$ induces a $k$-partition of $F$, one of whose parts contains a set of $W^Y_e$; the corresponding part of $X$ contains it too, so it is in $\mathcal V$. Conversely, suppose that no $F$ and $s$ exist. For each $n$, consider the $k$-partitions of $X \cap \{0, \dots, n-1\}$ none of whose parts contains a set enumerated by stage $n$. They form a finitely branching tree under restriction, which is infinite by hypothesis, applied to $F = X \cap \{0, \dots, n-1\}$ and $s = n$. By König's lemma it has an infinite path, a $k$-partition of $X$. A part of it in $\mathcal V$ would contain a finite set $F' \in W^Y_e$, enumerated at some stage $t$; then for $n > \max(\max F', t)$, the restriction of the partition to $X \cap \{0, \dots, n-1\}$ would have a part containing $F'$, enumerated by stage $n$, which is excluded. So $X \notin \mathcal L_k(\mathcal V)$.

The equality $\mathcal L(\mathcal V) = \bigcap_k \mathcal L_k(\mathcal V)$ is the definition, and $\mathcal V$ is large if and only if $\nat \in \mathcal L_k(\mathcal V)$ for every $k$: $\forall k$ followed by a $\Sigma^0_1(Y)$ condition.
:::

Fix a Scott ideal $\mathcal M$ coded by a set $M = \bigoplus_i Z_i$ (:ref{#def-coded-family}). For a set $S \subseteq \nat^2$ of pairs, let
$$
\mathcal U_S = \bigcap_{(e, i) \in S} \mathcal U^{Z_i}_e,
$$
with $\mathcal U_\emptyset$ the class of all sets. Every upward closed $\Sigma^0_1(Y)$ class with $Y \in \mathcal M$ is a class $\mathcal U^{Z_i}_e$, and a finite intersection of them is an upward closed $\Sigma^0_1(Z_{i_0} \oplus \dots \oplus Z_{i_r})$ class, hence again of this form, since $\mathcal M$ is closed under joins. We call these classes the **$\Sigma^0_1(\mathcal M)$ classes**, and write $\mathcal V$, $\mathcal W$ for them.

:::proposition{#prop-largeness-complexity}
Let $S \subseteq \nat^2$. The class $\mathcal U_S$ is large if and only if $\mathcal U_F$ is large for every finite $F \subseteq S$. The property "$\mathcal U_S$ is large" is $\Pi^0_1(S \oplus M')$, uniformly in $S$.
:::

:::proof{of=prop-largeness-complexity}
If $\mathcal U_S$ is large, so are the larger classes $\mathcal U_F$. Conversely, let $F_0 \subseteq F_1 \subseteq \cdots$ be finite sets with union $S$; the classes $\mathcal U_{F_n}$ decrease and their intersection is $\mathcal U_S$, so :ref{#lem-decreasing-large} applies. For a finite $F$, $\mathcal U_F$ is an upward closed $\Sigma^0_1(M)$ class, with an index computable from $F$, since the columns $Z_i$ are uniformly computable in $M$. Its largeness is $\Pi^0_2(M)$ by :ref{#lem-cover-class}, that is, $\Pi^0_1(M')$, uniformly. The quantification over the finite subsets $F$ of $S$ adds a universal quantifier and the $S$-computable condition $F \subseteq S$.
:::

The proposition is the main computational feature of largeness. A large class all of whose members are infinite is never $\Sigma^0_1$, since a $\Sigma^0_1$ class containing a set $X$ contains every set with a long enough common prefix with $X$, among which finite sets; the class of infinite sets is $\Pi^0_2$, an intersection of the classes $\{ X : |X| \geq n \}$. Monin and Patey proved that no non-trivial partition regular class is $\mathbf\Sigma^0_2$. The intersections $\mathcal U_S$ are therefore the natural level, and the proposition says that their largeness, a property of the whole class, is decided one jump above the code of the ideal, uniformly in the index set $S$.

:::quiz[the complexity of largeness]
In the proof of :ref{#lem-cover-class}, why are the partitions of $X \cap \{0, \dots, n-1\}$ tested against the sets enumerated by stage $n$ only?

- [x] So that the failing partial partitions form a tree, closed under restriction, with a node at every level $n$ by the hypothesis applied to $F = X \cap \{0, \dots, n-1\}$ and $s = n$; a set enumerated at stage $t$ is taken into account at every level $n > t$.
- [ ] Because $W^Y_e$ is finite.

  It is a $Y$-c.e. set, usually infinite.
- [ ] Because the class $\mathcal V$ is closed under finite changes.

  It need not be; the argument uses only upward closure.

---

In :ref{#prop-largeness-complexity}, why does largeness of $\mathcal U_S$ reduce to largeness of its finite sub-intersections?

- [x] By :ref{#lem-decreasing-large}: $\mathcal U_S$ is the intersection of the decreasing sequence $\mathcal U_{F_n}$, so it is large if all the $\mathcal U_{F_n}$ are.
- [ ] Because $S$ is finite.

  $S$ is an arbitrary set of pairs.
- [ ] Because the classes $\mathcal U^{Z_i}_e$ are partition regular.

  They are only upward closed in general.
:::

## Cohesive classes

The forcing for the pigeonhole principle will use reservoirs in a fixed partition regular class $\mathcal U$. The class should carry as much positive information as possible: the smaller $\mathcal U$, the fewer the possible reservoirs, and the more the condition says about the future. The natural candidate is a class that is minimal for the effective classes of the previous section: for every $\Sigma^0_1(\mathcal M)$ class $\mathcal V$, either $\mathcal U \subseteq \mathcal V$, or $\mathcal U \cap \mathcal V$ is not large. Such a class can be built greedily, deciding for each $\mathcal V$ in turn whether it can be added to the intersection. Each decision is a $\Pi^0_1$ question relative to the jump of the code, so the greedy construction needs the double jump of the code, which is too much. The difficulty is that two large classes may have a non-large intersection, as $\mathcal L_Z$ and $\mathcal L_{\overline Z}$ do, so the order of the decisions matters.

The remedy is to make first, for every member $Z$ of the ideal, the choice between $\mathcal L_Z$ and $\mathcal L_{\overline Z}$. Once these choices are made, the order of all other decisions no longer matters (:ref{#lem-cohesive-compatible}), and a minimal class is determined. The choices can be made by a set PA relative to the jump of the code, one jump below the greedy construction; both facts are proved in :ref{to="jump-cone-avoidance/cohesive-classes"}.

:::definition{#def-cohesive-class}
A large class $\mathcal A$ is **$\mathcal M$-cohesive** if for every $X \in \mathcal M$, $\mathcal A \subseteq \mathcal L_X$ or $\mathcal A \subseteq \mathcal L_{\overline X}$.
:::

The name comes from cohesive sets. Let $H$ be an infinite set cohesive for the sequence of the members of $\mathcal M$: $H \subseteq^* X$ or $H \subseteq^* \overline X$ for every $X \in \mathcal M$. The class $\mathcal L_H$ is partition regular (:ref{#ex-partition-regular}), hence large. If $H \subseteq^* X$ and $Y \cap H$ is infinite, then $Y \cap X$ is infinite; so $\mathcal L_H \subseteq \mathcal L_X$, and similarly $\mathcal L_H \subseteq \mathcal L_{\overline X}$ if $H \subseteq^* \overline X$. So $\mathcal L_H$ is $\mathcal M$-cohesive. A cohesive class chooses, like a cohesive set, a side of every set of the ideal, but it remains a class of sets, which can contain sets with no such property.

For a member $X$ of $\mathcal M$, the two cases are exclusive: if $\mathcal A \subseteq \mathcal L_X \cap \mathcal L_{\overline X}$, then neither $X$ nor $\overline X$ is in $\mathcal A$, which contradicts the largeness of $\mathcal A$. So an $\mathcal M$-cohesive class determines a side of every set of $\mathcal M$, namely the side it contains.

:::lemma{#lem-cohesive-compatible}
Let $\mathcal U_S$ be $\mathcal M$-cohesive, and let $\mathcal V$, $\mathcal W$ be $\Sigma^0_1(\mathcal M)$ classes such that $\mathcal U_S \cap \mathcal V$ and $\mathcal U_S \cap \mathcal W$ are large. Then $\mathcal U_S \cap \mathcal V \cap \mathcal W$ is large.
:::

:::proof{of=lem-cohesive-compatible}
Suppose not. By :ref{#prop-largeness-complexity}, applied to the set of pairs $S$ together with indices of $\mathcal V$ and $\mathcal W$, there is a finite $F \subseteq S$ such that $\mathcal U_F \cap \mathcal V \cap \mathcal W$ is not large. This class is an upward closed $\Sigma^0_1(Y)$ class for some $Y \in \mathcal M$. Since it is not large, there are $k$ and a $k$-partition of $\nat$ with no part in it. The $k$-partitions of $\nat$ with this property, coded as functions from $\nat$ to $\{0, \dots, k-1\}$, form a non-empty $\Pi^0_1(Y)$ class, and since $\mathcal M$ is a Scott ideal, it has a member in $\mathcal M$ (:ref{#prop-wkl-scott}). Let $Y_0, \dots, Y_{k-1} \in \mathcal M$ be its parts.

Since $\mathcal U_S$ is large, some $Y_j$ is in $\mathcal U_S$. Then $\mathcal U_S \not\subseteq \mathcal L_{\overline{Y_j}}$, since $Y_j \cap \overline{Y_j} = \emptyset$; by cohesiveness, $\mathcal U_S \subseteq \mathcal L_{Y_j}$. Now $Y_j \in \mathcal U_S \subseteq \mathcal U_F$ and $Y_j \notin \mathcal U_F \cap \mathcal V \cap \mathcal W$, so $Y_j \notin \mathcal V$ or $Y_j \notin \mathcal W$; say $Y_j \notin \mathcal V$. For $l \neq j$, the set $Y_l$ is disjoint from $Y_j$, so $Y_l \notin \mathcal L_{Y_j} \supseteq \mathcal U_S$. So no part of the partition is in $\mathcal U_S \cap \mathcal V$, which contradicts its largeness.
:::

The proof uses the Scott property of $\mathcal M$ to replace an arbitrary witness of non-largeness by one in $\mathcal M$, and cohesiveness to know that the class concentrates on one part of it. Without cohesiveness, the lemma fails. Let $Z \in \mathcal M$ be infinite and coinfinite, $\mathcal V = \{ X : X \cap Z \neq \emptyset \}$ and $\mathcal W = \{ X : X \cap \overline Z \neq \emptyset \}$, two $\Sigma^0_1(Z)$ classes. The class $\mathcal L_\nat$ of infinite sets, an intersection of the $\Sigma^0_1$ classes $\{ X : |X| \geq n \}$, is not $\mathcal M$-cohesive. The classes $\mathcal L_\nat \cap \mathcal V$ and $\mathcal L_\nat \cap \mathcal W$ are large, since they contain the partition regular classes $\mathcal L_Z$ and $\mathcal L_{\overline Z}$, but $\mathcal L_\nat \cap \mathcal V \cap \mathcal W$ contains neither $Z$ nor $\overline Z$, so it is not large.

:::quiz[compatibility]
In the proof of :ref{#lem-cohesive-compatible}, why is the partition taken in $\mathcal M$?

- [x] Because cohesiveness of $\mathcal U_S$ only gives information about members of $\mathcal M$: it says $\mathcal U_S \subseteq \mathcal L_{Y_j}$ for a part $Y_j \in \mathcal M$, which excludes the other parts from $\mathcal U_S$.
- [ ] Because the classes $\mathcal V$ and $\mathcal W$ are $\Sigma^0_1(\mathcal M)$.

  This is used to make the class of failing partitions $\Pi^0_1(Y)$ with $Y \in \mathcal M$; the reason for wanting a member in $\mathcal M$ is cohesiveness.
- [ ] Because $\mathcal M$ is closed under joins.

  Joins are used to see $\mathcal U_F \cap \mathcal V \cap \mathcal W$ as a $\Sigma^0_1(Y)$ class; the choice of the partition uses the Scott property.

---

Why does $Y_j \in \mathcal U_S$ force $\mathcal U_S \subseteq \mathcal L_{Y_j}$, and not $\mathcal L_{\overline{Y_j}}$?

- [x] Because $Y_j \notin \mathcal L_{\overline{Y_j}}$, its intersection with $\overline{Y_j}$ being empty; so $\mathcal U_S \not\subseteq \mathcal L_{\overline{Y_j}}$, and cohesiveness leaves the other case.
- [ ] Because $Y_j$ is infinite.

  Infinity of $Y_j$ follows, but is not the reason.
- [ ] Because $\mathcal U_S$ is partition regular.

  The argument uses only largeness and cohesiveness.
:::

## Notes and references

The classes $\mathcal U_S$ over a coded Scott ideal, :ref{#prop-largeness-complexity} and the compatibility lemma are from Monin and Patey's work on hyperarithmetical reductions (arXiv 2019); the notion of $\mathcal M$-cohesive class is due to Le Houérou, Levy Patey and Mimouni (2024). Monin and Patey (2024) prove that no non-trivial partition regular class is $\mathbf\Sigma^0_2$. The presentation follows the subsections *Effective classes*, *$\mathcal M$-minimal classes* and *$\mathcal M$-cohesive classes* of the chapter *Jump cone avoidance* of Patey's monograph; :ref{#lem-cover-class} makes explicit the compactness argument used there.

- B. Monin and L. Patey, *The weakness of the pigeonhole principle under hyperarithmetical reductions*, arXiv:1905.08425 (2019).
- B. Monin and L. Patey, *Partition genericity and pigeonhole basis theorems*, Journal of Symbolic Logic 89 (2024), 829–857.
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Partition regularity*.
