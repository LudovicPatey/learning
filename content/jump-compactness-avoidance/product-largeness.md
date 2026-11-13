---
title: Product largeness
summary: Large classes of tuples of sets, where each coordinate chooses its own part of a cover; the decreasing intersection, intersection and cover lemmas; the complexity of largeness over a coded Scott ideal.
duration: 45
prerequisites: [merging-level-two, jump-cone-avoidance/largeness, big-five/wkl0]
---

The previous lesson showed that a single large class of reservoirs cannot carry two negative answers about $\Sigma^0_2$ sentences (:ref{#lem-no-two-sides}), and proposed to keep several reservoirs and a class of tuples of sets. This lesson develops the corresponding notion of largeness, due to Monin and Patey, which is the combinatorial tool of the rest of the course. The definitions follow :ref{to="jump-cone-avoidance/largeness"}, except that each coordinate of a tuple chooses its own part of a cover.

## Product largeness

An **index set** is a finite non-empty set $I$ of strings of natural numbers, all of the same length. An **$I$-tuple** is a family $\vec X = \langle X_\nu : \nu \in I \rangle$ of sets, coded by a single set, and we write $\bigcup \vec X$ for $\bigcup_{\nu \in I} X_\nu$. A class $\mathcal A$ of $I$-tuples is **upward closed** if $\vec X \in \mathcal A$ and $X_\nu \subseteq Y_\nu$ for every $\nu$ imply $\vec Y \in \mathcal A$. For a $k$-cover $Y_0, \dots, Y_{k-1}$ of $\nat$ and a function $j : I \to k$, write $\vec Y_j = \langle Y_{j(\nu)} : \nu \in I \rangle$.

:::definition{#def-product-large}
A class $\mathcal A$ of $I$-tuples is **large** if it is upward closed and for every $k$ and every $k$-cover $Y_0, \dots, Y_{k-1}$ of $\nat$, there is $j : I \to k$ with $\vec Y_j \in \mathcal A$. It is **non-trivial** if every coordinate of every member is infinite. For an $I$-tuple $\vec X$, let
$$
\mathcal L_{\vec X} = \{ \vec Y : Y_\nu \cap X_\nu \text{ is infinite for every } \nu \in I \}.
$$
:::

For $I$ a singleton this is :ref{#def-large}. The function $j$ chooses a part of the cover for each coordinate independently; this is the difference with largeness of the class of sets $\bigcup \vec Y$.

:::example{#ex-product-large}
1. If $\mathcal A_\nu$ is a large class of sets for each $\nu \in I$, the product $\{ \vec Y : Y_\nu \in \mathcal A_\nu \text{ for all } \nu \}$ is large: choose $j(\nu)$ for each $\nu$ separately. For instance $\mathcal L_{\vec X}$ is large and non-trivial if all $X_\nu$ are infinite.
2. Let $R$ be infinite and coinfinite and $I = \{0, 1\}$ (strings of length $1$). The class $\mathcal L_R \times \mathcal L_{\overline R}$ is large. It does not contain $(R, R)$, $(\overline R, \overline R)$ or $(\overline R, R)$: for the cover $Y_0 = R$, $Y_1 = \overline R$ of $\nat$, only the function $j$ with $j(0) = 0$ and $j(1) = 1$ works.
3. The class of pairs $(Y_0, Y_1)$ such that $Y_0 \cap Y_1$ is infinite is large: a finite cover of $\nat$ has an infinite part $Y_t$, and the constant function $t$ works. The class of pairs such that $Y_0 \cap R$ and $Y_0 \setminus R$ are infinite is upward closed and not large, by :ref{#lem-no-two-sides} applied to the first coordinate.
:::

:::figure[The class $\mathcal L_R \times \mathcal L_{\overline R}$ of :ref{#ex-product-large} and the $2$-cover $R, \overline R$ of $\nat$. Of the four functions $j : \{0, 1\} \to 2$, only the one choosing $R$ for coordinate $0$ and $\overline R$ for coordinate $1$ gives a pair in the class; the constant functions do not.]
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="The cover of the natural numbers by R and its complement, and the four ways to assign a part to each of the two coordinates; only the assignment of R to coordinate 0 and the complement of R to coordinate 1 gives a pair in the class L_R times L of the complement of R"><text x="30" y="34" text-anchor="middle" class="math">n</text><text x="75.0" y="34" text-anchor="middle" class="mrm muted">0</text><rect x="60" y="42" width="30" height="24" class="cell"/><text x="75.0" y="59" text-anchor="middle" class="label">·</text><text x="105.0" y="34" text-anchor="middle" class="mrm muted">1</text><rect x="90" y="42" width="30" height="24" class="cell head-cell"/><text x="105.0" y="59" text-anchor="middle" class="label">R</text><text x="135.0" y="34" text-anchor="middle" class="mrm muted">2</text><rect x="120" y="42" width="30" height="24" class="cell head-cell"/><text x="135.0" y="59" text-anchor="middle" class="label">R</text><text x="165.0" y="34" text-anchor="middle" class="mrm muted">3</text><rect x="150" y="42" width="30" height="24" class="cell"/><text x="165.0" y="59" text-anchor="middle" class="label">·</text><text x="195.0" y="34" text-anchor="middle" class="mrm muted">4</text><rect x="180" y="42" width="30" height="24" class="cell head-cell"/><text x="195.0" y="59" text-anchor="middle" class="label">R</text><text x="225.0" y="34" text-anchor="middle" class="mrm muted">5</text><rect x="210" y="42" width="30" height="24" class="cell"/><text x="225.0" y="59" text-anchor="middle" class="label">·</text><text x="255.0" y="34" text-anchor="middle" class="mrm muted">6</text><rect x="240" y="42" width="30" height="24" class="cell"/><text x="255.0" y="59" text-anchor="middle" class="label">·</text><text x="285.0" y="34" text-anchor="middle" class="mrm muted">7</text><rect x="270" y="42" width="30" height="24" class="cell head-cell"/><text x="285.0" y="59" text-anchor="middle" class="label">R</text><text x="315.0" y="34" text-anchor="middle" class="mrm muted">8</text><rect x="300" y="42" width="30" height="24" class="cell head-cell"/><text x="315.0" y="59" text-anchor="middle" class="label">R</text><text x="345.0" y="34" text-anchor="middle" class="mrm muted">9</text><rect x="330" y="42" width="30" height="24" class="cell"/><text x="345.0" y="59" text-anchor="middle" class="label">·</text><text x="375.0" y="34" text-anchor="middle" class="mrm muted">10</text><rect x="360" y="42" width="30" height="24" class="cell head-cell"/><text x="375.0" y="59" text-anchor="middle" class="label">R</text><text x="405.0" y="34" text-anchor="middle" class="mrm muted">11</text><rect x="390" y="42" width="30" height="24" class="cell"/><text x="405.0" y="59" text-anchor="middle" class="label">·</text><text x="435.0" y="34" text-anchor="middle" class="mrm muted">12</text><rect x="420" y="42" width="30" height="24" class="cell head-cell"/><text x="435.0" y="59" text-anchor="middle" class="label">R</text><text x="465.0" y="34" text-anchor="middle" class="mrm muted">13</text><rect x="450" y="42" width="30" height="24" class="cell head-cell"/><text x="465.0" y="59" text-anchor="middle" class="label">R</text><text x="495.0" y="34" text-anchor="middle" class="mrm muted">14</text><rect x="480" y="42" width="30" height="24" class="cell"/><text x="495.0" y="59" text-anchor="middle" class="label">·</text><text x="525.0" y="34" text-anchor="middle" class="mrm muted">15</text><rect x="510" y="42" width="30" height="24" class="cell"/><text x="525.0" y="59" text-anchor="middle" class="label">·</text><text x="554" y="59" text-anchor="middle" class="mrm muted">⋯</text><text x="300" y="90" text-anchor="middle" class="label">shaded: R; blank: the complement of R</text><text x="110" y="124" text-anchor="middle" class="label">j = (0, 0)</text><rect x="170" y="108" width="110" height="22" rx="6" class="state"/><text x="225.0" y="123.0" text-anchor="middle" class="label">(R, R)</text><text x="300" y="124" text-anchor="start" class="label">second coordinate misses the complement</text><text x="110" y="152" text-anchor="middle" class="label">j = (1, 1)</text><rect x="170" y="136" width="110" height="22" rx="6" class="state"/><text x="225.0" y="151.0" text-anchor="middle" class="label">(R̄, R̄)</text><text x="300" y="152" text-anchor="start" class="label">first coordinate misses R</text><text x="110" y="180" text-anchor="middle" class="label">j = (0, 1)</text><rect x="170" y="164" width="110" height="22" rx="6" class="node"/><text x="225.0" y="179.0" text-anchor="middle" class="label">(R, R̄)</text><text x="300" y="180" text-anchor="start" class="label">in the class</text><text x="110" y="208" text-anchor="middle" class="label">j = (1, 0)</text><rect x="170" y="192" width="110" height="22" rx="6" class="state"/><text x="225.0" y="207.0" text-anchor="middle" class="label">(R̄, R)</text><text x="300" y="208" text-anchor="start" class="label">misses both</text></svg>
:::

Item 2 is the situation of :ref{#lem-no-two-sides}: the class keeps both halves of a split, at the price that no single part of the cover serves all coordinates.

:::lemma{#lem-product-decreasing}
If $\mathcal A_0 \supseteq \mathcal A_1 \supseteq \cdots$ are large classes of $I$-tuples, then $\bigcap_n \mathcal A_n$ is large.
:::

:::proof{of=lem-product-decreasing}
The intersection is upward closed. Let $Y_0, \dots, Y_{k-1}$ cover $\nat$, and suppose that no $\vec Y_j$ is in the intersection: for each of the finitely many $j : I \to k$ there is $n_j$ with $\vec Y_j \notin \mathcal A_{n_j}$. For $n = \max_j n_j$, no $\vec Y_j$ is in $\mathcal A_n$, which contradicts its largeness.
:::

:::lemma{#lem-product-intersection}
Let $\mathcal A$ be an upward closed class of $I$-tuples and $\vec X$, $\vec W$ two $I$-tuples. If $\mathcal A \cap \mathcal L_{\vec X} \cap \mathcal L_{\vec W}$ is large, then $\mathcal A \cap \mathcal L_{\langle X_\nu \cap W_\nu : \nu \in I \rangle}$ is large. In particular, if $\mathcal A \cap \mathcal L_{\vec W}$ is large, then $\vec W \in \mathcal A$.
:::

:::proof{of=lem-product-intersection}
The class is upward closed. Let $Z_0, \dots, Z_{k-1}$ cover $\nat$. Refine it into the finite partition of $\nat$ whose parts are the non-empty sets of the form $Z_t \cap \bigcap_\nu X^{\pm}_\nu \cap \bigcap_\nu W^{\pm}_\nu$, where $t$ is the least index of a part containing the element and $X^{\pm}_\nu$ is $X_\nu$ or its complement, and similarly for $W^\pm_\nu$. Each part $Q$ is contained in some $Z_t$, and is contained in or disjoint from each $X_\nu$ and each $W_\nu$. By largeness, some function $r$ from $I$ to the parts gives a tuple $\langle Q_{r(\nu)} \rangle$ in $\mathcal A \cap \mathcal L_{\vec X} \cap \mathcal L_{\vec W}$. For each $\nu$, $Q_{r(\nu)}$ meets $X_\nu$ infinitely often, so it is contained in $X_\nu$; similarly in $W_\nu$; and it is infinite. Let $j(\nu)$ be such that $Q_{r(\nu)} \subseteq Z_{j(\nu)}$. By upward closure $\vec Z_j \in \mathcal A$, and $Z_{j(\nu)}$ contains the infinite subset $Q_{r(\nu)}$ of $X_\nu \cap W_\nu$. For the last statement, take $X_\nu = \nat$: the tuple $\langle Q_{r(\nu)} \rangle$ is in $\mathcal A$ and $Q_{r(\nu)} \subseteq W_\nu$, so $\vec W \in \mathcal A$.
:::

:::lemma{#lem-product-cover}
Let $\mathcal A$ be a non-trivial large class of $I$-tuples. For every finite cover $Y_0, \dots, Y_{k-1}$ of $\nat$, there is $j : I \to k$ such that $\mathcal A \cap \mathcal L_{\vec Y_j}$ is large.
:::

:::proof{of=lem-product-cover}
Suppose not. For each $j : I \to k$ there is a finite cover $\mathcal Z^j$ of $\nat$ with no function $r$ making the tuple of its parts a member of $\mathcal A \cap \mathcal L_{\vec Y_j}$. Let $Q_0, \dots, Q_{l-1}$ be a common refinement of all the covers $\mathcal Z^j$ and of $Y_0, \dots, Y_{k-1}$. By largeness, some $r : I \to l$ has $\vec Q_r \in \mathcal A$. Each $Q_{r(\nu)}$ is infinite, since $\mathcal A$ is non-trivial, and contained in some $Y_{j(\nu)}$; this defines $j : I \to k$. Each $Q_{r(\nu)}$ is also contained in a part $Z^j_{s(\nu)}$ of $\mathcal Z^j$. By upward closure the tuple $\langle Z^j_{s(\nu)} \rangle$ is in $\mathcal A$, and $Z^j_{s(\nu)}$ contains the infinite subset $Q_{r(\nu)}$ of $Y_{j(\nu)}$, so the tuple is in $\mathcal L_{\vec Y_j}$. This contradicts the choice of $\mathcal Z^j$.
:::

By the two lemmas, the class of tuples $\vec W$ such that $\mathcal A \cap \mathcal L_{\vec W}$ is large is a large subclass of $\mathcal A$; it is the largest partition regular subclass, as in :ref{#prop-largest-partition-regular} (last exercise). The cover lemma is how a condition will choose, for each reservoir, a part of a cover while keeping the class large.

:::quiz[product largeness]
In the proof of :ref{#lem-product-intersection}, why is the cover refined so that each part is contained in or disjoint from each $X_\nu$ and $W_\nu$?

- [x] So that a part meeting $X_\nu$ infinitely often is contained in $X_\nu$, and similarly for $W_\nu$; the chosen parts are then infinite subsets of $X_\nu \cap W_\nu$.
- [ ] So that the refined cover is finite.

  Any refinement by finitely many sets is finite; the point is homogeneity.
- [ ] So that $\mathcal A$ becomes partition regular.

  The class is only assumed upward closed.

---

Where is non-triviality used in :ref{#lem-product-cover}?

- [x] To know that the chosen parts $Q_{r(\nu)}$ are infinite, so that the coarser parts containing them meet $Y_{j(\nu)}$ infinitely often.
- [ ] To show that $\mathcal A$ is upward closed.

  This is part of largeness.
- [ ] To define the common refinement.

  The refinement exists for any finite family of finite covers.
:::

## Effective classes of tuples

As in :ref{to="jump-cone-avoidance/largeness"}, fix a Scott ideal $\mathcal M$ with a code $M = \bigoplus_i Z_i$. For a set $Y$, an index $e$ and an index set $I$, let $\mathcal U^{Y, I}_e$ be the class of $I$-tuples $\vec X$ such that some $I$-tuple of finite sets $\vec F$ enumerated in $W^Y_e$ satisfies $F_\nu \subseteq X_\nu$ for all $\nu$. These are exactly the upward closed $\Sigma^0_1(Y)$ classes of $I$-tuples. For $S \subseteq \nat^2$, let $\mathcal U^I_S = \bigcap_{(e, i) \in S} \mathcal U^{Z_i, I}_e$; the classes $\mathcal U^{Z_i, I}_e$, and their finite intersections, are the **$\Sigma^0_1(\mathcal M)$ classes** of $I$-tuples. For an $I$-tuple $\vec W$ of members of $\mathcal M$, $\mathcal L_{\vec W} = \bigcap_{\nu, n} \{ \vec Y : |Y_\nu \cap W_\nu| \geq n \}$ is $\mathcal U^I_E$ for a set $E$ computable from the $M$-indices of the $W_\nu$.

:::proposition{#prop-product-complexity}
1. For an upward closed $\Sigma^0_1(Y)$ class $\mathcal V$ of $I$-tuples, "$\mathcal V$ is large" is $\Pi^0_2(Y)$, uniformly in an index.
2. $\mathcal U^I_S$ is large if and only if $\mathcal U^I_F$ is large for every finite $F \subseteq S$. "$\mathcal U^I_S$ is large" is $\Pi^0_1(S \oplus M')$, uniformly in $S$ and $I$.
3. If a $\Sigma^0_1(\mathcal M)$ class $\mathcal V$ of $I$-tuples is not large, there are $k$ and a $k$-partition $Y_0, \dots, Y_{k-1}$ of $\nat$ with all $Y_t \in \mathcal M$ and $\vec Y_j \notin \mathcal V$ for every $j : I \to k$.
:::

:::proof{of=prop-product-complexity}
1. Since $\mathcal V$ is upward closed, it suffices to consider $k$-partitions. We show: $\mathcal V$ is large if and only if for every $k$ there is $l$ such that for every $k$-partition $P$ of $\{0, \dots, l - 1\}$ there are $j : I \to k$ and a tuple $\vec F$ enumerated in $W^Y_e$ by stage $l$ with each $F_\nu$ contained in the part $P_{j(\nu)}$. This is $\Pi^0_2(Y)$. If such $l$ exist, a $k$-partition of $\nat$ restricted to $\{0, \dots, l-1\}$ gives $j$ and $\vec F$, and $\vec Y_j \in \mathcal V$. Conversely, if for some $k$ no $l$ works, the failing $k$-partitions of initial segments form an infinite finitely branching tree under restriction; by König's lemma it has a path, a $k$-partition of $\nat$. By largeness some $\vec Y_j$ is in $\mathcal V$, witnessed by $\vec F$ enumerated at stage $s$; for $l > s$ larger than all elements of $\vec F$, the restriction to $\{0, \dots, l-1\}$ does not fail. This is a contradiction.
2. The first statement is :ref{#lem-product-decreasing}, applied to the intersections over an increasing sequence of finite sets with union $S$. For finite $F$, $\mathcal U^I_F$ is an upward closed $\Sigma^0_1(M)$ class with an index computable from $F$ and $I$, so its largeness is $\Pi^0_2(M)$ by 1, that is, $\Pi^0_1(M')$. Quantifying over the finite $F \subseteq S$ adds a universal quantifier and an $S$-computable condition.
3. Say $\mathcal V$ is $\Sigma^0_1(W)$ with $W \in \mathcal M$. For some $k$, the class of functions $P : \nat \to k$ such that no $j$ gives a member of $\mathcal V$ is non-empty; it is $\Pi^0_1(W)$, since "$\vec Y_j \in \mathcal V$" is $\Sigma^0_1(P \oplus W)$. Since $\mathcal M$ is a Scott ideal, it has a member in $\mathcal M$ (:ref{#prop-wkl-scott}), whose parts are in $\mathcal M$.
:::

If $M$ is low and $S$ is $\Delta^0_2$, the property "$\mathcal U^I_S$ is large" is $\Pi^0_1(\emptyset')$, that is, $\Pi^0_2$. This is the complexity that will make the forcing questions of the course $\Sigma^0_2$.

## Exercises

::::exercise{difficulty=1}
Let $R$ be infinite and coinfinite and $I = \{0, 1\}$. Decide whether the following classes of pairs $(Y_0, Y_1)$ are large: (a) $Y_0 \cup Y_1$ is infinite; (b) $Y_0 \cap Y_1 \cap R$ and $Y_0 \cap Y_1 \cap \overline R$ are infinite.

:::solution
(a) Large: a finite cover of $\nat$ has an infinite part $Y_t$, and the constant function $t$ works. (b) Not large: for the cover $R, \overline R$, each coordinate of $\vec Y_j$ is $R$ or $\overline R$, so $Y_0 \cap Y_1$ is $R$, $\overline R$ or empty, and in each case one of the two intersections is empty. Compare with the class of :ref{#ex-product-large}, item 2, which asks for $Y_0 \cap R$ and $Y_1 \setminus R$ to be infinite: there the two conditions are carried by different coordinates.
:::
::::

::::exercise{difficulty=2}
Call a class $\mathcal P$ of $I$-tuples **partition regular** if it is non-empty and upward closed, and for every $\vec X \in \mathcal P$ and every finite cover $Y_0, \dots, Y_{k-1}$ of $\nat$, there is $j : I \to k$ with $\langle X_\nu \cap Y_{j(\nu)} : \nu \in I \rangle \in \mathcal P$. Let $\mathcal A$ be a non-trivial large class of $I$-tuples and $\mathcal L(\mathcal A) = \{ \vec X : \mathcal A \cap \mathcal L_{\vec X} \text{ is large} \}$. Show that $\mathcal L(\mathcal A)$ is a partition regular subclass of $\mathcal A$, and that it contains every partition regular subclass of $\mathcal A$.

:::solution
$\mathcal L(\mathcal A) \subseteq \mathcal A$ by the last statement of :ref{#lem-product-intersection}, and it is upward closed since $\mathcal L_{\vec X} \subseteq \mathcal L_{\vec Y}$ when $X_\nu \subseteq Y_\nu$ for all $\nu$. It is non-empty, since it contains the tuple with all coordinates $\nat$. Let $\vec X \in \mathcal L(\mathcal A)$ and let $Y_0, \dots, Y_{k-1}$ cover $\nat$. The class $\mathcal A \cap \mathcal L_{\vec X}$ is large and non-trivial, so by :ref{#lem-product-cover} some $j$ makes $\mathcal A \cap \mathcal L_{\vec X} \cap \mathcal L_{\vec Y_j}$ large, and by :ref{#lem-product-intersection}, $\mathcal A \cap \mathcal L_{\langle X_\nu \cap Y_{j(\nu)} \rangle}$ is large: the tuple $\langle X_\nu \cap Y_{j(\nu)} \rangle$ is in $\mathcal L(\mathcal A)$.

Let $\mathcal P \subseteq \mathcal A$ be partition regular and $\vec X \in \mathcal P$. The class $\mathcal A \cap \mathcal L_{\vec X}$ is upward closed. For a cover $Y_0, \dots, Y_{k-1}$ of $\nat$, partition regularity gives $j$ with $\langle X_\nu \cap Y_{j(\nu)} \rangle \in \mathcal P \subseteq \mathcal A$. Its coordinates are infinite, since $\mathcal A$ is non-trivial, so $\vec Y_j$ is in $\mathcal A$ by upward closure and in $\mathcal L_{\vec X}$. So $\mathcal A \cap \mathcal L_{\vec X}$ is large, and $\vec X \in \mathcal L(\mathcal A)$. This is the product version of :ref{#prop-largest-partition-regular}.
:::
::::

## Notes and references

Product largeness and :ref{#lem-product-decreasing}, :ref{#lem-product-intersection} and :ref{#lem-product-cover} are due to Monin and Patey (*SRT²₂ does not imply RT²₂ in ω-models*); the presentation follows the section *Product largeness* of the chapter *Jump compactness avoidance* of Patey's monograph, where the cover lemma is proved in the form "$\mathcal L(\mathcal A)$ is large" and the last exercise is stated without proof. The complexity of largeness is the product version of :ref{#prop-largeness-complexity}, with the compactness argument of :ref{#lem-cover-class}.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Product largeness*.
