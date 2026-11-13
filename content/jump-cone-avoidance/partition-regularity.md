---
title: Partition regularity and largeness
summary: Partition regular classes generalize the class of infinite sets; a class is large if every finite cover of the integers has a part in it; large classes contain a largest partition regular subclass; decreasing intersections of large classes are large.
duration: 40
prerequisites: [cohesiveness-second-jump, ramsey-theorem/cone-avoidance]
---

The Mathias-type forcing for the pigeonhole principle (:ref{#thm-dj-cone-avoidance}) splits the reservoir along a partition and keeps a part that is infinite. For second-jump control, :ref{to="jump-cone-avoidance/cohesiveness-second-jump"} suggests restricting the reservoirs further, so that they keep enough structure for the questions about $\Pi^0_2$ sentences. For cohesiveness the restriction was a fixed sequence of Boolean combinations. For the pigeonhole principle, the instance is arbitrary, and the restriction is given instead by a class of sets, the **reservoir of reservoirs**: every reservoir of the construction must belong to it, and the class must allow splitting, as the class of infinite sets does.

There is a useful reading in terms of information. A Mathias condition $(\sigma, X)$ gives positive and negative information about the set $G$ under construction through its stem, but only negative information through its reservoir: elements outside $X$ are excluded, and no element of $X$ is guaranteed to enter $G$. $\Sigma^0_1$ properties are positive information and are forced by extending the stem; $\Pi^0_1$ properties are negative information and are forced by shrinking the reservoir. A $\Pi^0_2$ property, $\forall x\ \theta(x)$ with $\theta$ a $\Sigma^0_1$ formula, requires positive information in every future condition, and the only way to guarantee it is to restrict the possible future reservoirs. A class of allowed reservoirs does exactly this. This lesson studies such classes combinatorially; the next two lessons study their effective versions and choose the class used by the forcing.

## Partition regular classes

Classes are classes of subsets of $\nat$. A class $\mathcal A$ is **upward closed** if $X \in \mathcal A$ and $X \subseteq Y$ imply $Y \in \mathcal A$. A **$k$-cover** of a set $X$ is a sequence $Y_0, \dots, Y_{k-1}$ of sets with $X \subseteq Y_0 \cup \dots \cup Y_{k-1}$; it is a **$k$-partition** of $X$ if the sets are pairwise disjoint with union $X$.

:::definition{#def-partition-regular}
A class $\mathcal P$ is **partition regular** if it is non-empty, upward closed, and for every $X \in \mathcal P$ and every $2$-cover $Y_0, Y_1$ of $X$, some $Y_i$ belongs to $\mathcal P$. It is **non-trivial** if all its members are infinite.
:::

By induction on $k$, every $k$-cover of a member of a partition regular class has a part in the class: if $X \subseteq Y_0 \cup \dots \cup Y_k$, then $Y_0$ or $Y_1 \cup \dots \cup Y_k$ belongs to $\mathcal P$. Since $\mathcal P$ is non-empty and upward closed, $\nat \in \mathcal P$.

:::example{#ex-partition-regular}
1. The class of infinite sets is partition regular: this is the infinite pigeonhole principle. It is non-trivial.
2. For a fixed $n$, the class $\{ X : n \in X \}$ is partition regular, and trivial.
3. For an infinite set $Z$, the class $\mathcal L_Z = \{ X : X \cap Z \text{ is infinite} \}$ is partition regular and non-trivial: if $X \cap Z$ is infinite and $X \subseteq Y_0 \cup Y_1$, one of $Y_0 \cap Z$ and $Y_1 \cap Z$ is infinite. The class of infinite sets is $\mathcal L_\nat$.
4. The class of sets of positive upper density, $\limsup_n |X \cap \{0, \dots, n - 1\}| / n > 0$, is partition regular, since the upper density of $Y_0 \cup Y_1$ is at most the sum of the upper densities. So is the class of sets $X$ with $\sum_{n \in X} 1/(n+1) = \infty$.
5. Let $Z$ be a set and $C \not\leq_T Z$. The class $\mathcal P_C$ of sets $X$ having an infinite subset $H$ with $C \not\leq_T Z \oplus H$ is partition regular. Let $X \in \mathcal P_C$ with witness $H$, enumerated in increasing order by $p_H$, and let $Y_0, Y_1$ cover $X$. By :ref{#thm-dj-cone-avoidance} relative to $Z \oplus H$, the set $\{ k : p_H(k) \in Y_0 \}$ has an infinite subset $K$, of itself or of its complement, with $C \not\leq_T Z \oplus H \oplus K$. The set $p_H[K]$ is infinite, contained in $Y_0$ or in $Y_1$, and computable in $H \oplus K$.
:::

The last example shows that strong cone avoidance of the pigeonhole principle is a statement of partition regularity. Non-trivial partition regular classes are generalizations of the class of infinite sets. They share its closure properties.

:::lemma{#lem-partition-regular-basic}
Let $\mathcal P$ be a partition regular class.

1. $\mathcal P$ is non-trivial if and only if it contains no finite set.
2. If $\mathcal P$ is non-trivial, it is closed under finite changes: if $X \in \mathcal P$ and $Y$ differs from $X$ on finitely many elements, then $Y \in \mathcal P$.
:::

:::proof{of=lem-partition-regular-basic}
1. This is the definition.
2. The sets $X \cap Y$ and $X \setminus Y$ cover $X$, and $X \setminus Y$ is finite, so it is not in $\mathcal P$. So $X \cap Y \in \mathcal P$, and $Y \in \mathcal P$ by upward closure.
:::

:::quiz[partition regularity]
In item 5 of :ref{#ex-partition-regular}, why is strong cone avoidance of the pigeonhole principle needed, and not only cone avoidance?

- [x] Because the set $\{ k : p_H(k) \in Y_0 \}$ is determined by the arbitrary cover $Y_0, Y_1$, and need not be computable in $Z \oplus H$.
- [ ] Because $p_H[K]$ must be infinite.

  This holds since $K$ is infinite and $p_H$ is injective.
- [ ] Because $\mathcal P_C$ must be upward closed.

  Upward closure is immediate: a superset of $X$ has the same infinite subset $H$.
:::

:::figure[A $2$-cover of a member $X$ of a partition regular class $\mathcal P$. The elements of $X$ are split between $Y_0$ and $Y_1$; whatever the split, at least one part belongs to $\mathcal P$. For the class of infinite sets this is the pigeonhole principle; for $\mathcal L_Z$, the part that meets $Z$ infinitely often.]
<svg class="fig" viewBox="0 0 600 196" width="600" role="img" aria-label="A set X in a partition regular class P, split into two parts Y0 and Y1; at least one of the parts belongs to P"><text x="60.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="102.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">2</text><text x="144.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="186.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">6</text><text x="228.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="270.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">10</text><text x="312.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="354.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">14</text><text x="396.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="438.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">18</text><text x="480.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">20</text><text x="522.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">22</text><text x="564.5" y="16" text-anchor="middle" class="mrm muted" font-size="10">24</text><text x="38" y="45" text-anchor="end" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3"></tspan></text><line x1="50" y1="40" x2="596" y2="40" class="axis"/><circle cx="81.5" cy="40" r="5" class="ink-fill"/><circle cx="123.5" cy="40" r="5" class="ink-fill"/><circle cx="144.5" cy="40" r="5" class="ink-fill"/><circle cx="186.5" cy="40" r="5" class="ink-fill"/><circle cx="207.5" cy="40" r="5" class="ink-fill"/><circle cx="249.5" cy="40" r="5" class="ink-fill"/><circle cx="270.5" cy="40" r="5" class="ink-fill"/><circle cx="312.5" cy="40" r="5" class="ink-fill"/><circle cx="333.5" cy="40" r="5" class="ink-fill"/><circle cx="375.5" cy="40" r="5" class="ink-fill"/><circle cx="396.5" cy="40" r="5" class="ink-fill"/><circle cx="438.5" cy="40" r="5" class="ink-fill"/><circle cx="459.5" cy="40" r="5" class="ink-fill"/><circle cx="501.5" cy="40" r="5" class="ink-fill"/><circle cx="522.5" cy="40" r="5" class="ink-fill"/><circle cx="564.5" cy="40" r="5" class="ink-fill"/><text x="602" y="45" class="mrm muted" font-size="13">⋯</text><text x="38" y="85" text-anchor="end" class="math" font-size="14">Y<tspan class="mrm" font-size="10" dy="3">₀</tspan></text><line x1="50" y1="80" x2="596" y2="80" class="axis"/><circle cx="81.5" cy="80" r="5" class="accent-fill"/><circle cx="144.5" cy="80" r="5" class="accent-fill"/><circle cx="207.5" cy="80" r="5" class="accent-fill"/><circle cx="249.5" cy="80" r="5" class="accent-fill"/><circle cx="333.5" cy="80" r="5" class="accent-fill"/><circle cx="396.5" cy="80" r="5" class="accent-fill"/><circle cx="501.5" cy="80" r="5" class="accent-fill"/><circle cx="564.5" cy="80" r="5" class="accent-fill"/><text x="602" y="85" class="mrm muted" font-size="13">⋯</text><text x="38" y="125" text-anchor="end" class="math" font-size="14">Y<tspan class="mrm" font-size="10" dy="3">₁</tspan></text><line x1="50" y1="120" x2="596" y2="120" class="axis"/><circle cx="123.5" cy="120" r="5" class="ink-fill"/><circle cx="186.5" cy="120" r="5" class="ink-fill"/><circle cx="270.5" cy="120" r="5" class="ink-fill"/><circle cx="312.5" cy="120" r="5" class="ink-fill"/><circle cx="375.5" cy="120" r="5" class="ink-fill"/><circle cx="438.5" cy="120" r="5" class="ink-fill"/><circle cx="459.5" cy="120" r="5" class="ink-fill"/><circle cx="522.5" cy="120" r="5" class="ink-fill"/><text x="602" y="125" class="mrm muted" font-size="13">⋯</text><text x="300" y="168" text-anchor="middle" class="label">X ∈ 𝒫 and X ⊆ Y₀ ∪ Y₁: then Y₀ ∈ 𝒫 or Y₁ ∈ 𝒫</text><text x="300" y="186" text-anchor="middle" class="label">for the infinite sets: one part is infinite; for 𝓛<tspan font-size="9" dy="3">Z</tspan><tspan dy="-3">: one part meets Z infinitely often</tspan></text></svg>
:::

## Large classes

An upward closed class containing a partition regular class need not be partition regular. Let $Z$ be infinite and coinfinite. The class $\mathcal L_Z \cup \{ X : X \supseteq \overline Z \}$ contains $\mathcal L_Z$ and the set $\overline Z$, but if $\overline Z$ is split into two infinite parts, neither part meets $Z$ or contains $\overline Z$, so neither belongs to the class. The following notion is preserved by passing to larger upward closed classes.

:::definition{#def-large}
A class $\mathcal A$ is **large** if it is upward closed and for every $k$ and every $k$-cover $Y_0, \dots, Y_{k-1}$ of $\nat$, some $Y_i$ belongs to $\mathcal A$.
:::

A large class contains $\nat$, using the $1$-cover. A partition regular class is large, and a large class need not be partition regular, as the class $\mathcal L_Z \cup \{ X : X \supseteq \overline Z \}$ shows. For an upward closed class $\mathcal A$, let
$$
\mathcal L(\mathcal A) = \{ X : \text{every finite cover of } X \text{ has a part in } \mathcal A \}.
$$

:::proposition{#prop-largest-partition-regular}
Let $\mathcal A$ be a large class. Then $\mathcal L(\mathcal A)$ is a partition regular subclass of $\mathcal A$, and it contains every partition regular subclass of $\mathcal A$. In particular, an upward closed class is large if and only if it contains a partition regular class.
:::

:::proof{of=prop-largest-partition-regular}
The class $\mathcal L(\mathcal A)$ is upward closed, since a cover of a superset of $X$ is a cover of $X$. It contains $\nat$, since $\mathcal A$ is large. It is contained in $\mathcal A$, using the $1$-cover of $X$ by itself. Let $X \in \mathcal L(\mathcal A)$ and let $Y_0, Y_1$ cover $X$. Suppose neither $Y_i$ is in $\mathcal L(\mathcal A)$: there are finite covers $(W^i_j)_{j < k_i}$ of $Y_i$ with no part in $\mathcal A$. The sets $W^i_j$, for $i < 2$ and $j < k_i$, form a finite cover of $X$ with no part in $\mathcal A$, which contradicts $X \in \mathcal L(\mathcal A)$. So $\mathcal L(\mathcal A)$ is partition regular.

If $\mathcal P \subseteq \mathcal A$ is partition regular and $X \in \mathcal P$, every finite cover of $X$ has a part in $\mathcal P \subseteq \mathcal A$, so $X \in \mathcal L(\mathcal A)$. Finally, if an upward closed class $\mathcal A$ contains a partition regular class $\mathcal P$, every finite cover of $\nat$ has a part in $\mathcal P$, since $\nat \in \mathcal P$; so $\mathcal A$ is large.
:::

:::lemma{#lem-decreasing-large}
If $\mathcal A_0 \supseteq \mathcal A_1 \supseteq \cdots$ are large classes, then $\bigcap_n \mathcal A_n$ is large.
:::

:::proof{of=lem-decreasing-large}
The intersection is upward closed. Let $Y_0, \dots, Y_{k-1}$ cover $\nat$, and suppose that no $Y_i$ is in the intersection: for each $i$ there is $n_i$ with $Y_i \notin \mathcal A_{n_i}$. Let $n = \max_i n_i$. Since the sequence decreases, no $Y_i$ belongs to $\mathcal A_n$, which contradicts the largeness of $\mathcal A_n$.
:::

The lemma is a form of compactness: if an intersection of large classes, taken along an increasing sequence of finite sets of classes, is not large, then one of the finite intersections is not large. It fails for arbitrary intersections of two large classes: $\mathcal L_Z \cap \mathcal L_{\overline Z}$ does not contain $Z$ or $\overline Z$, so it is not large when $Z$ and $\overline Z$ are infinite. Choosing, among several large classes, some whose intersection remains large is the subject of the next two lessons.

:::quiz[large classes]
In the proof of :ref{#prop-largest-partition-regular}, why can the two failing covers be merged into one cover of $X$?

- [x] Because $Y_0 \cup Y_1 \supseteq X$, so the union of a cover of $Y_0$ and a cover of $Y_1$ is a finite cover of $X$; none of its parts is in $\mathcal A$.
- [ ] Because $\mathcal A$ is partition regular.

  It is only large; the merging shows that $\mathcal L(\mathcal A)$ is partition regular.
- [ ] Because $Y_0$ and $Y_1$ are disjoint.

  Disjointness is not needed for covers.

---

Where is the decreasing hypothesis used in :ref{#lem-decreasing-large}?

- [x] To pass from "$Y_i \notin \mathcal A_{n_i}$ for each $i$" to "$Y_i \notin \mathcal A_n$ for all $i$" with a single $n$, the largest of the $n_i$.
- [ ] To show that the intersection is upward closed.

  Any intersection of upward closed classes is upward closed.
- [ ] To show that the intersection contains $\nat$.

  Every large class contains $\nat$; the intersection does too, for any family.
:::

## Exercises

::::exercise{difficulty=1}
Show that the union of any family of partition regular classes is partition regular, and that the intersection of two partition regular classes need not be partition regular, nor even large.

:::solution
The union is non-empty and upward closed; if $X$ belongs to a member $\mathcal P$ of the family, every $2$-cover of $X$ has a part in $\mathcal P$, hence in the union. For the intersection, let $Z$ be infinite and coinfinite: $\mathcal L_Z$ and $\mathcal L_{\overline Z}$ are partition regular, but their intersection does not contain $Z$ or $\overline Z$, which cover $\nat$, so it is not large.
:::
::::

::::exercise{difficulty=2}
Let $\mathcal P$ be a non-trivial partition regular class and $X \in \mathcal P$. Show that $\mathcal P \cap \mathcal L_X$ is large.

:::solution
It is upward closed. Let $Y_0, \dots, Y_{k-1}$ cover $\nat$. The sets $Y_i \cap X$ cover $X$, so some $Y_i \cap X$ is in $\mathcal P$. It is infinite, since $\mathcal P$ is non-trivial, so $Y_i \in \mathcal L_X$, and $Y_i \in \mathcal P$ by upward closure. So $Y_i \in \mathcal P \cap \mathcal L_X$.
:::
::::

::::exercise{difficulty=2}
Let $\mathcal A$ be a large class all of whose members are infinite. Show that $\mathcal L(\mathcal A) = \{ X : \mathcal A \cap \mathcal L_X \text{ is large} \}$.

:::solution
If $X \in \mathcal L(\mathcal A)$, then $\mathcal L(\mathcal A)$ is non-trivial, being contained in $\mathcal A$, and the previous exercise applied to $\mathcal L(\mathcal A)$ shows that $\mathcal L(\mathcal A) \cap \mathcal L_X$ is large; so is the larger class $\mathcal A \cap \mathcal L_X$. Conversely, suppose $\mathcal A \cap \mathcal L_X$ is large, and let $Y_0, \dots, Y_{k-1}$ cover $X$. The sets $Y_0, \dots, Y_{k-1}, \overline X$ cover $\nat$, so one of them is in $\mathcal A \cap \mathcal L_X$. It is not $\overline X$, which is disjoint from $X$. So some $Y_i$ is in $\mathcal A$, and $X \in \mathcal L(\mathcal A)$.
:::
::::

## Notes and references

Partition regularity is a classical notion of Ramsey theory. Its use in computability theory, the notions of large class and of the largest partition regular subclass $\mathcal L(\mathcal A)$, and :ref{#lem-decreasing-large} are due to Monin and Patey (*Pigeons do not jump high*, 2019). The exercises are from Monin and Patey (2024), who also prove that measurable partition regular classes have measure $1$, and that partition regular classes with the Baire property are comeager. The presentation follows the subsection *Largeness* of the section *Partition regularity* of the chapter *Jump cone avoidance* of Patey's monograph.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095.
- B. Monin and L. Patey, *Partition genericity and pigeonhole basis theorems*, Journal of Symbolic Logic 89 (2024), 829–857.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Partition regularity*.
