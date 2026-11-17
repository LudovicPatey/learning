---
title: Partition regularity and largeness
summary: Partition regular classes generalize the class of infinite sets; a class is large if every finite cover of the integers has a part in it; large classes contain a largest partition regular subclass; decreasing intersections of large classes are large.
duration: 30
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

::::exercise{#ex-pr-large-trace difficulty=2 objective="Restrict a partition regular class to the sets meeting one of its members infinitely, and see that largeness survives."}
Let $\mathcal P$ be a non-trivial partition regular class and $X \in \mathcal P$. Show that $\mathcal P \cap \mathcal L_X$ is large.

:::solution
It is upward closed. Let $Y_0, \dots, Y_{k-1}$ cover $\nat$. The sets $Y_i \cap X$ cover $X$, so some $Y_i \cap X$ is in $\mathcal P$. It is infinite, since $\mathcal P$ is non-trivial, so $Y_i \in \mathcal L_X$, and $Y_i \in \mathcal P$ by upward closure. So $Y_i \in \mathcal P \cap \mathcal L_X$.
:::
::::

::::exercise{#ex-pr-largest-subclass difficulty=2 objective="Characterize the largest partition regular subclass of a large class through the largeness of its traces."}
Let $\mathcal A$ be a large class all of whose members are infinite. Show that $\mathcal L(\mathcal A) = \{ X : \mathcal A \cap \mathcal L_X \text{ is large} \}$.

:::solution
If $X \in \mathcal L(\mathcal A)$, then $\mathcal L(\mathcal A)$ is non-trivial, being contained in $\mathcal A$, and :ref{#ex-pr-large-trace} applied to $\mathcal L(\mathcal A)$ shows that $\mathcal L(\mathcal A) \cap \mathcal L_X$ is large; so is the larger class $\mathcal A \cap \mathcal L_X$. Conversely, suppose $\mathcal A \cap \mathcal L_X$ is large, and let $Y_0, \dots, Y_{k-1}$ cover $X$. The sets $Y_0, \dots, Y_{k-1}, \overline X$ cover $\nat$, so one of them is in $\mathcal A \cap \mathcal L_X$. It is not $\overline X$, which is disjoint from $X$. So some $Y_i$ is in $\mathcal A$, and $X \in \mathcal L(\mathcal A)$.
:::
::::

## Notes and references

Partition regularity is a classical notion of Ramsey theory. Its use in computability theory, the notions of large class and of the largest partition regular subclass $\mathcal L(\mathcal A)$, and :ref{#lem-decreasing-large} are due to Monin and Patey (*Pigeons do not jump high*, 2019). :ref{#ex-pr-large-trace}, :ref{#ex-pr-largest-subclass}, :ref{#ex-pr-union-intersection} and :ref{#ex-pr-trace-not-regular} are adapted from exercises of the monograph, after Monin and Patey (2024) and Mimouni; Monin and Patey (2024) who also prove that measurable partition regular classes have measure $1$, and that partition regular classes with the Baire property are comeager. The presentation follows the subsection *Largeness* of the section *Partition regularity* of the chapter *Jump cone avoidance* of Patey's monograph.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095.
- B. Monin and L. Patey, *Partition genericity and pigeonhole basis theorems*, Journal of Symbolic Logic 89 (2024), 829–857.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Partition regularity*.

:::::exercises
::::exercise[Unions and intersections]{#ex-pr-union-intersection difficulty=1 objective="Check that partition regularity is preserved by unions and not by intersections."}
Show that the union of any family of partition regular classes is partition regular, and that the intersection of two partition regular classes need not be partition regular, nor even large.

:::solution
The union is non-empty and upward closed; if $X$ belongs to a member $\mathcal P$ of the family, every $2$-cover of $X$ has a part in $\mathcal P$, hence in the union. For the intersection, let $Z$ be infinite and coinfinite: $\mathcal L_Z$ and $\mathcal L_{\overline Z}$ are partition regular, but their intersection does not contain $Z$ or $\overline Z$, which cover $\nat$, so it is not large.
:::
::::

::::exercise[A trace that is not partition regular]{#ex-pr-trace-not-regular difficulty=1 objective="Show by an example that the trace of a partition regular class on one of its members is large but need not be partition regular."}
Let $Z$ be the set of even numbers and $X$ the set of multiples of $3$. Show that $X \in \mathcal L_Z$ and that $\mathcal L_Z \cap \mathcal L_X$ is large but not partition regular.

:::solution
$X \cap Z$ is the set of multiples of $6$, which is infinite, so $X \in \mathcal L_Z$, and $\mathcal L_Z \cap \mathcal L_X$ is large by :ref{#ex-pr-large-trace}. Let $Y = (Z \setminus X) \cup (X \setminus Z)$. Then $Y \cap Z = Z \setminus X$, the even numbers not divisible by $3$, and $Y \cap X = X \setminus Z$, the odd multiples of $3$; both are infinite, so $Y \in \mathcal L_Z \cap \mathcal L_X$. The sets $Y_0 = Z \setminus X$ and $Y_1 = X \setminus Z$ cover $Y$. But $Y_0 \cap X = \emptyset$ and $Y_1 \cap Z = \emptyset$, so neither part belongs to $\mathcal L_Z \cap \mathcal L_X$.
:::
::::

::::exercise[Ultrafilters]{#ex-pr-ultrafilter difficulty=2 objective="Identify the minimal partition regular classes with the ultrafilters, and see why a definable substitute for minimality is needed."}
An **ultrafilter** is a class $\mathcal F$ of sets, non-empty, upward closed and closed under finite intersections, with $\emptyset \notin \mathcal F$, such that $Y \in \mathcal F$ or $\overline Y \in \mathcal F$ for every set $Y$. It is **principal** if it is $\{ X : n \in X \}$ for some $n$.

1. Show that every ultrafilter is partition regular, and that it is non-trivial if and only if it is not principal.
2. Show that a partition regular class $\mathcal P$ is minimal for inclusion among partition regular classes if and only if it is an ultrafilter.

:::solution
1. Let $\mathcal F$ be an ultrafilter, $X \in \mathcal F$ and $X \subseteq Y_0 \cup Y_1$. If neither $Y_i$ is in $\mathcal F$, then $\overline{Y_0}, \overline{Y_1} \in \mathcal F$, so $X \cap \overline{Y_0} \cap \overline{Y_1} = \emptyset$ is in $\mathcal F$, which is excluded. So $\mathcal F$ is partition regular. A principal ultrafilter contains $\{ n \}$, so it is trivial. Conversely, if $\mathcal F$ contains a finite set $F$, then $F \neq \emptyset$, and by partition regularity applied to its cover by singletons, some $\{ n \}$ is in $\mathcal F$. Then $\mathcal F \supseteq \{ X : n \in X \}$ by upward closure, and a set $X$ with $n \notin X$ is not in $\mathcal F$, since $X \cap \{ n \} = \emptyset$. So $\mathcal F$ is principal.
2. Let $\mathcal F$ be an ultrafilter and $\mathcal Q \subseteq \mathcal F$ partition regular. Let $X \in \mathcal F$ and $Y \in \mathcal Q$. The sets $Y \cap X$ and $Y \setminus X$ cover $Y$, so one of them is in $\mathcal Q \subseteq \mathcal F$; it is not $Y \setminus X$, which is disjoint from $X \in \mathcal F$. So $Y \cap X \in \mathcal Q$, and $X \in \mathcal Q$ by upward closure. Hence $\mathcal Q = \mathcal F$, and $\mathcal F$ is minimal.

Conversely, let $\mathcal P$ be minimal. For $X \in \mathcal P$, let $\mathcal P_X = \{ Y : Y \cap X \in \mathcal P \}$. It contains $X$, is upward closed, and is partition regular: if $Y \cap X \in \mathcal P$ and $Y \subseteq Y_0 \cup Y_1$, the sets $Y_0 \cap X$ and $Y_1 \cap X$ cover $Y \cap X$, so one of them is in $\mathcal P$. Moreover $\mathcal P_X \subseteq \mathcal P$ by upward closure. By minimality $\mathcal P_X = \mathcal P$: for $X, Y \in \mathcal P$, $Y \in \mathcal P_X$ gives $X \cap Y \in \mathcal P$. If $\emptyset \in \mathcal P$, then $\mathcal P$ is the class of all sets, which strictly contains the partition regular class $\{ X : 0 \in X \}$; so $\emptyset \notin \mathcal P$. Finally $\nat \in \mathcal P$, and $Y, \overline Y$ cover $\nat$, so one of them is in $\mathcal P$. So $\mathcal P$ is an ultrafilter.

Non-principal ultrafilters exist by Zorn's lemma, but none of them has the Baire property (a classical fact, admitted here), so minimal non-trivial partition regular classes are of no use in an effective construction. The course replaces minimality by a minimality with respect to the $\Sigma^0_1(\mathcal M)$ classes of a countable ideal (:ref{to="jump-cone-avoidance/cohesive-classes"}).
:::
::::

::::exercise[Many elements in exponential intervals]{#ex-pr-towers difficulty=2 objective="Prove the partition regularity of a $\Pi^0_2$ class by a pigeonhole argument on the parameter, and separate it from the class of infinite sets."}
Let $\mathcal Q$ be the class of sets $X$ such that for every $n$ there is $x$ with $|X \cap [x, 2^x)| \geq n$. Show that $\mathcal Q$ is a non-trivial partition regular class. Let $t_0 = 1$ and $t_{k+1} = 2^{t_k}$; show that the infinite set $\{ t_k : k \in \nat \}$ is not in $\mathcal Q$.

:::solution
$\mathcal Q$ is upward closed, and $\nat \in \mathcal Q$, since $|[x, 2^x)| = 2^x - x$ is unbounded. A finite set $X$ satisfies $|X \cap [x, 2^x)| \leq |X|$ for every $x$, so it is not in $\mathcal Q$. Let $X \in \mathcal Q$ and $X \subseteq Y_0 \cup Y_1$. For each $n$, choose $x_n$ with $|X \cap [x_n, 2^{x_n})| \geq 2n$; one of $Y_0$, $Y_1$, call it $Y_{i_n}$, has at least $n$ elements in $[x_n, 2^{x_n})$. Some $i$ equals $i_n$ for infinitely many $n$. For every $n$ there is $n' \geq n$ with $i_{n'} = i$, and $Y_i$ has at least $n' \geq n$ elements in $[x_{n'}, 2^{x_{n'}})$. So $Y_i \in \mathcal Q$.

Let $T = \{ t_k : k \in \nat \}$, an increasing sequence. For $x = 0$ the interval is empty. For $x \geq 1$, let $k$ be least with $x \leq t_k$; then $t_{k-1} < x$ if $k \geq 1$, and $2^x \leq 2^{t_k} = t_{k+1}$. So $T \cap [x, 2^x) \subseteq \{ t_k \}$ has at most one element, and $T \notin \mathcal Q$.
:::
::::

::::exercise[Density classes]{#ex-pr-density difficulty=1 objective="Complete the verification of item 4 of the examples of partition regular classes."}
Prove item 4 of :ref{#ex-partition-regular}: the class of sets of positive upper density and the class of sets $X$ with $\sum_{n \in X} 1/(n + 1) = \infty$ are non-trivial partition regular classes. Show that the second class contains the first, and that the set of squares is in neither.

:::solution
Write $d_n(X) = |X \cap \{0, \dots, n-1\}| / n$ and $\bar d(X) = \limsup_n d_n(X)$. If $X \subseteq Y$, then $d_n(X) \leq d_n(Y)$, so $\bar d(X) \leq \bar d(Y)$: the class is upward closed, and it contains $\nat$. If $X \subseteq Y_0 \cup Y_1$, then $d_n(X) \leq d_n(Y_0) + d_n(Y_1)$, and $\limsup (a_n + b_n) \leq \limsup a_n + \limsup b_n$; so $\bar d(X) > 0$ gives $\bar d(Y_i) > 0$ for some $i$. A finite set has upper density $0$. For the second class, $\sum_{n \in X} 1/(n+1) \leq \sum_{n \in Y_0} 1/(n+1) + \sum_{n \in Y_1} 1/(n+1)$, the class is upward closed, contains $\nat$ (harmonic series), and finite sets have finite sums.

If $\bar d(X) > \varepsilon > 0$, there are infinitely many $n$ with $|X \cap [0, n)| \geq \varepsilon n$. For such $n$, at most $\varepsilon n / 2$ of these elements are below $\varepsilon n / 2$, so at least $\varepsilon n / 2$ of them lie in $[\varepsilon n / 2, n)$, and each contributes $1/(k+1) \geq 1/n$; the block $[\varepsilon n / 2, n)$ contributes at least $\varepsilon / 2$ to the sum. Choose such numbers $n_0 < n_1 < \cdots$ with $\varepsilon n_{j+1} / 2 \geq n_j$: the blocks are disjoint, and the sum diverges. The squares satisfy $d_n \leq (\sqrt n + 1)/n \to 0$ and $\sum_k 1/(k^2 + 1) < \infty$.
:::
::::

::::exercise[Computing a largest partition regular subclass]{#ex-pr-largest-example difficulty=1 objective="Compute the largest partition regular subclass of the large class of the lesson that is not partition regular."}
Let $Z$ be infinite and coinfinite, and $\mathcal A = \mathcal L_Z \cup \{ X : X \supseteq \overline Z \}$. Show that $\mathcal L(\mathcal A) = \mathcal L_Z$.

:::solution
$\mathcal L_Z$ is a partition regular subclass of $\mathcal A$, so $\mathcal L_Z \subseteq \mathcal L(\mathcal A)$ by :ref{#prop-largest-partition-regular}. Conversely, let $X \notin \mathcal L_Z$, so that $X \cap Z$ is finite. Split $X \cap \overline Z$ into two sets $W_0, W_1$, each different from $\overline Z$: if $X \cap \overline Z$ has at most one element, take it and $\emptyset$, which differ from the infinite set $\overline Z$; otherwise put one element in $W_0$ and the rest in $W_1$. The sets $X \cap Z$, $W_0$, $W_1$ cover $X$. None is in $\mathcal L_Z$: the first is finite, the others are disjoint from $Z$. None contains $\overline Z$: the first is disjoint from the non-empty set $\overline Z$, and $W_0, W_1$ are subsets of $\overline Z$ different from it. So this cover has no part in $\mathcal A$, and $X \notin \mathcal L(\mathcal A)$.
:::
::::
:::::
