---
title: Branches and meta-conditions
summary: The pigeonhole principle for Δ⁰₂ sets with product Mathias forcing; a condition with several reservoirs may have no valid side; index sets built by triplication, whose branches satisfy a Ramsey property; meta-conditions carry one pair of stems per branch, and some branch always has a valid side.
duration: 45
prerequisites: [product-mathias]
---

This lesson and the next two prove the theorem of Monin and Patey.

:::theorem[Monin, Patey]{#thm-d22-jump-pa}
Let $D \leq_T Z$ be sets such that $Z'$ is not PA relative to $D'$, and let $A$ be a $\Delta^0_2(Z)$ set. There is an infinite set $H$, contained in $A$ or in $\overline A$, such that $(Z \oplus H)'$ is not PA relative to $D'$. So $\mathsf D^2_2$ admits jump PA avoidance.
:::

We write the proof for $Z = D = \emptyset$, so that $A$ is $\Delta^0_2$ and the conclusion is that $H'$ is not PA relative to $\emptyset'$; the general case is explained at the end of :ref{to="jump-compactness-avoidance/delta2-jump-pa"}. Write $A_0 = A$ and $A_1 = \overline A$. The plan follows the proof of :ref{#thm-d22-weakly-low} by Cholak, Jockusch and Slaman, and the forcing of Dzhafarov and Jockusch (:ref{#thm-dj-cone-avoidance}): conditions with two stems, $\sigma_0 \subseteq A_0$ and $\sigma_1 \subseteq A_1$, sharing their reservoirs. Here the reservoirs are those of product Mathias forcing. This lesson explains why a pair of stems does not suffice and introduces the structure that replaces it.

## Valid sides and products

Consider for a moment quadruples $(\sigma_0, \sigma_1, \vec X, S)$ such that $(\sigma_i, \vec X, S)$ is a condition of product Mathias forcing (:ref{#def-product-condition}) with $\sigma_i \subseteq A_i$, for $i < 2$. The reservoirs contain elements of both $A_0$ and $A_1$, and side $i$ is useful only if the class $\mathcal U^I_S$ allows reservoirs inside $A_i$. As in :ref{#def-valid-part}, call side $i$ **valid** if $\mathcal U^I_S \cap \mathcal L_{\langle X_\nu \cap A_i : \nu \in I \rangle}$ is large.

If $I$ is a singleton, some side is valid. By :ref{#lem-product-cover} applied to the cover $A_0, A_1$ of $\nat$, some $i$ makes $\mathcal U^I_S \cap \mathcal L_{\langle A_i \rangle}$ large, and since $\mathcal U^I_S \subseteq \mathcal L_{\vec X}$, :ref{#lem-product-intersection} makes $\mathcal U^I_S \cap \mathcal L_{\langle X \cap A_i \rangle}$ large. For two coordinates this fails. Suppose $A$ and $\overline A$ are infinite and the class is $\mathcal L_A \times \mathcal L_{\overline A}$, with reservoirs $(\nat, \nat)$. Side $0$ is valid only if $(\mathcal L_A \times \mathcal L_{\overline A}) \cap \mathcal L_{(A, A)}$ is large; for the cover $A_0, A_1$, the second coordinate of a pair of parts in this class would meet both $A$ and $\overline A$ infinitely often, which neither part does. So side $0$ is not valid, and symmetrically side $1$ is not valid. Such classes are exactly what the merging lemma :ref{#lem-product-merging} produces.

The cover lemma still says something for two coordinates: it gives $j : I \to 2$ such that $\mathcal U^I_S \cap \mathcal L_{\langle X_\nu \cap A_{j(\nu)} \rangle}$ is large. The function $j$ colors the coordinates. If two coordinates out of three have the same color $i$, the pair of these two coordinates has a valid side $i$. This suggests keeping, instead of one pair of stems for the whole tuple, one pair of stems for each sub-tuple in a family with a Ramsey property: every $2$-coloring of the coordinates makes some member of the family monochromatic. Weak merging, with three negative answers instead of two, provides such families.

## Branches

Let $u_0 = 1$ and $u_{n+1} = \binom{2u_n + 1}{2} u_n$.

:::definition{#def-meta-index}
The index sets $\mathbb I_n$ are defined by $\mathbb I_0 = \{ \varepsilon \}$ and $\mathbb I_{n+1} = \mathbb I_n \cdot \{ 0, 1, \dots, 2u_n \}$, where the numbers are strings of length $1$. The **branches** of $\mathbb I_n$ are defined by induction: $\{ \varepsilon \}$ is the only branch of $\mathbb I_0$, and the branches of $\mathbb I_{n+1}$ are the sets $I \cdot \{a, b\}$ for a branch $I$ of $\mathbb I_n$ and $a < b \leq 2u_n$.
:::

So $\mathbb I_n$ is a set of strings of length $n$, and its branches are subsets of size $2^n$. For $m \geq n$ and a branch $J$ of $\mathbb I_m$, the set $J \upharpoonright n = \{ \mu \upharpoonright n : \mu \in J \}$ of the prefixes of length $n$ of its elements is a branch of $\mathbb I_n$, and $J = (J \upharpoonright n) \cdot K$ for some set $K$ of strings of length $m - n$; this follows from the definition by induction on $m - n$. We call $J \upharpoonright n$ the **ancestor** of $J$ at level $n$. Finally $\mathbb I_m = \mathbb I_n \cdot K_{m, n}$, where $K_{m, n}$ is the set of strings $\kappa$ of length $m - n$ with $\kappa(t) \leq 2u_{n+t}$ for each $t$.

:::lemma{#lem-branch-ramsey}
1. $\mathbb I_n$ has exactly $u_n$ branches.
2. For every $n$ and every function $j : \mathbb I_n \to 2$, there are a branch $I$ of $\mathbb I_n$ and $i < 2$ with $j(\nu) = i$ for every $\nu \in I$.
:::

:::proof{of=lem-branch-ramsey}
Both by induction on $n$; the case $n = 0$ is clear.

1. A branch of $\mathbb I_{n+1}$ is determined by a branch $I$ of $\mathbb I_n$ and a pair $a < b \leq 2u_n$, and distinct choices give distinct sets. There are $\binom{2u_n + 1}{2} u_n = u_{n+1}$ of them.
2. Let $j : \mathbb I_{n+1} \to 2$. For each $a \leq 2u_n$, the function $\nu \mapsto j(\nu a)$ on $\mathbb I_n$ has, by induction, a monochromatic branch $I_a$ with color $i_a$. There are $2u_n + 1$ numbers $a$ and $2u_n$ possible pairs $(I_a, i_a)$, by item 1; so $(I_a, i_a) = (I_b, i_b)$ for some $a < b$. The branch $I_a \cdot \{a, b\}$ of $\mathbb I_{n+1}$ is monochromatic with color $i_a$.
:::

:::figure[The index sets $\mathbb I_0 = \{\varepsilon\}$ and $\mathbb I_1 = \{0, 1, 2\}$, and the three branches of $\mathbb I_1$. A coloring of $\mathbb I_1$ in two colors, here $0 \mapsto 0$, $1 \mapsto 1$, $2 \mapsto 0$, makes the branch $\{0, 2\}$ monochromatic. Each element of $\mathbb I_1$ is later replaced by $2u_1 + 1 = 7$ copies, and the branches of $\mathbb I_2$ are the copies of a branch of $\mathbb I_1$ indexed by two of them.]
<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="The index set I_0 with the single element epsilon, the index set I_1 with elements 0, 1, 2, and its three branches; with the coloring 0 to 0, 1 to 1, 2 to 0, the branch 0, 2 is monochromatic"><text x="60" y="30" text-anchor="middle" class="label">𝕀₀</text><circle cx="300" cy="26" r="13" class="state"/><text x="300" y="31" text-anchor="middle" class="math">ε</text><text x="60" y="100" text-anchor="middle" class="label">𝕀₁</text><line x1="300" y1="39" x2="200" y2="83" class="muted-stroke" stroke-width="1"/><circle cx="200" cy="96" r="13" class="node"/><text x="200" y="101" text-anchor="middle" class="mrm">0</text><text x="200" y="128" text-anchor="middle" class="label">color 0</text><line x1="300" y1="39" x2="300" y2="83" class="muted-stroke" stroke-width="1"/><circle cx="300" cy="96" r="13" class="state"/><text x="300" y="101" text-anchor="middle" class="mrm">1</text><text x="300" y="128" text-anchor="middle" class="label">color 1</text><line x1="300" y1="39" x2="400" y2="83" class="muted-stroke" stroke-width="1"/><circle cx="400" cy="96" r="13" class="node"/><text x="400" y="101" text-anchor="middle" class="mrm">2</text><text x="400" y="128" text-anchor="middle" class="label">color 0</text><rect x="120" y="150" width="120" height="44" rx="6" class="state"/><text x="180.0" y="168.0" text-anchor="middle" class="label">branch {0, 1}</text><text x="180.0" y="184.0" text-anchor="middle" class="label">two colors</text><rect x="270" y="150" width="120" height="44" rx="6" class="node"/><text x="330.0" y="168.0" text-anchor="middle" class="label">branch {0, 2}</text><text x="330.0" y="184.0" text-anchor="middle" class="label">monochromatic</text><rect x="420" y="150" width="120" height="44" rx="6" class="state"/><text x="480.0" y="168.0" text-anchor="middle" class="label">branch {1, 2}</text><text x="480.0" y="184.0" text-anchor="middle" class="label">two colors</text></svg>
:::

:::quiz[branches]
In item 2 of :ref{#lem-branch-ramsey}, why are $2u_n + 1$ copies needed?

- [x] Because each copy $a$ yields a pair $(I_a, i_a)$ among $u_n \cdot 2$ possibilities, and two copies with the same pair are needed to form a branch $I_a \cdot \{a, b\}$; $2u_n + 1$ copies guarantee this by the pigeonhole principle.
- [ ] Because a branch of $\mathbb I_{n+1}$ has $2u_n + 1$ elements.

  It has $2^{n+1}$ elements.
- [ ] Because $\mathbb I_n$ has $2u_n + 1$ elements.

  The size of $\mathbb I_n$ is a product of the numbers $2u_t + 1$.
:::

## Meta-conditions

:::definition{#def-meta-condition}
A **meta-condition** of level $n$ is a triple $c = (\vec \sigma, \vec X, S)$ where:

1. $\vec \sigma = \langle \sigma^I_i : I \text{ a branch of } \mathbb I_n,\ i < 2 \rangle$ is a family of strings with $\sigma^I_i \subseteq A_i$;
2. $\vec X$ is an $\mathbb I_n$-tuple of members of $\mathcal M$ with $\min X_\nu \geq |\sigma^I_i|$ for all $\nu$, $I$ and $i$;
3. $S$ is $\Delta^0_2$, and $\mathcal U^{\mathbb I_n}_S$ is a large subclass of $\mathcal L_{\vec X}$.

The pair $(I, i)$ is a **part** of $c$. A **member** of the part $(I, i)$ is a set $G$ with $\sigma^I_i \prec G$ whose elements larger than or equal to $|\sigma^I_i|$ are in $\bigcup_{\nu \in I} X_\nu$.
:::

A meta-condition is a family of $2u_n$ parallel attempts, one for each part, which share the reservoirs and the class of tuples. The part $(I, i)$ uses the reservoirs indexed by $I$ only, and builds a subset of $A_i$. The meta-condition $(\langle \varepsilon, \varepsilon \rangle, \langle \nat \rangle, S_\infty)$ of level $0$ is the starting point, with $\mathcal U_{S_\infty}$ the class of infinite sets.

:::definition{#def-meta-extension}
A meta-condition $d = (\vec \tau, \vec Y, T)$ of level $m$ **extends** a meta-condition $c = (\vec \sigma, \vec X, S)$ of level $n$ if $m \geq n$ and:

1. $Y_\mu \subseteq X_{\mu \upharpoonright n}$ for every $\mu \in \mathbb I_m$;
2. for every branch $J$ of $\mathbb I_m$ and $i < 2$, $\tau^J_i$ is compatible with $(\sigma^{J \upharpoonright n}_i, \bigcup_{\nu \in J \upharpoonright n} X_\nu)$;
3. $\vec Z^{(\kappa)} \in \mathcal U^{\mathbb I_n}_S$ for every $\vec Z \in \mathcal U^{\mathbb I_m}_T$ and every $\kappa \in K_{m, n}$.
:::

This is the extension of :ref{#def-product-condition}, for every branch and its ancestor at once. If $d$ extends $c$ and $J \upharpoonright n = I$, every member of the part $(J, i)$ of $d$ is a member of the part $(I, i)$ of $c$: it extends $\tau^J_i$, which is compatible with $(\sigma^I_i, \bigcup_{\nu \in I} X_\nu)$, and its later elements are in $\bigcup_{\mu \in J} Y_\mu \subseteq \bigcup_{\nu \in I} X_\nu$. The relation is transitive, since $K_{m', n} = K_{m, n} \cdot K_{m', m}$, slices of slices are slices, and compatibility composes.

## Valid parts

For a meta-condition $c = (\vec \sigma, \vec X, S)$ of level $n$ and a part $(I, i)$, let $\vec X^{I, i}$ be the $\mathbb I_n$-tuple with coordinate $X_\nu \cap A_i$ for $\nu \in I$ and $\nat$ for $\nu \notin I$.

:::definition{#def-meta-valid}
The part $(I, i)$ of $c$ is **valid** if $\mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\vec X^{I, i}}$ is large.
:::

Since $\mathcal U^{\mathbb I_n}_S \subseteq \mathcal L_{\vec X}$, validity says that the class keeps enough tuples whose coordinates in $I$ meet $X_\nu \cap A_i$ infinitely often. By :ref{#lem-product-intersection}, a valid part has $\vec X^{I, i} \in \mathcal U^{\mathbb I_n}_S$; in particular $X_\nu \cap A_i$ is infinite for $\nu \in I$.

:::lemma{#lem-meta-valid}
Let $c = (\vec \sigma, \vec X, S)$ be a meta-condition of level $n$.

1. Some part of $c$ is valid.
2. If $d$ of level $m$ extends $c$ and the part $(J, i)$ of $d$ is valid, the part $(J \upharpoonright n, i)$ of $c$ is valid.
3. If $d = (\vec \tau, \vec Y, S)$ is a meta-condition of level $n$ extending $c$, with the same $S$ and each $Y_\nu$ differing from $X_\nu$ on finitely many elements, then $c$ and $d$ have the same valid parts.
4. If $(I, i)$ is valid, there is an extension of $c$ as in item 3 in which $\tau^I_i$ has more elements than $\sigma^I_i$ and the other stems are unchanged.
:::

:::proof{of=lem-meta-valid}
1. By :ref{#lem-product-cover} applied to the non-trivial class $\mathcal U^{\mathbb I_n}_S$ and the cover $A_0, A_1$, there is $j : \mathbb I_n \to 2$ such that $\mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\langle A_{j(\nu)} \rangle}$ is large, and by :ref{#lem-product-intersection}, $\mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\langle X_\nu \cap A_{j(\nu)} \rangle}$ is large. By :ref{#lem-branch-ramsey}, some branch $I$ is monochromatic with a color $i$. Then $\mathcal L_{\langle X_\nu \cap A_{j(\nu)} \rangle} \subseteq \mathcal L_{\vec X^{I, i}}$, so $(I, i)$ is valid.
2. Let $d = (\vec \tau, \vec Y, T)$, $I = J \upharpoonright n$, and $J = I \cdot K$ with $K \subseteq K_{m, n}$; fix $\kappa \in K$. Let $\mathcal B = \mathcal U^{\mathbb I_m}_T \cap \mathcal L_{\vec Y^{J, i}}$, which is large. For $\vec Z \in \mathcal B$, the slice $\vec Z^{(\kappa)}$ is in $\mathcal U^{\mathbb I_n}_S$, and for $\nu \in I$, $Z_{\nu\kappa}$ meets $Y_{\nu\kappa} \cap A_i \subseteq X_\nu \cap A_i$ infinitely often; so $\vec Z^{(\kappa)} \in \mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\vec X^{I, i}}$. This class is upward closed, and for a cover of $\nat$ with $\vec Y_j \in \mathcal B$, the slice $\kappa$ of $\vec Y_j$ is a tuple of parts of the same cover. So it is large.
3. The classes $\mathcal L_{\vec X^{I, i}}$ and $\mathcal L_{\vec Y^{I, i}}$ are equal, since finite changes do not affect infinite intersections.
4. Let $x \in X_\nu \cap A_i$ for some $\nu \in I$, larger than all stems of $c$. Let $\tau^I_i = \sigma^I_i \cup \{ x \}$, the string of length $x + 1$, keep the other stems, and replace each $X_\mu$ by $X_\mu \setminus \{0, \dots, x\}$. Since $x \in A_i$, this is a meta-condition, it extends $c$ with $K_{n, n} = \{ \varepsilon \}$, and item 3 applies.
:::

Item 2 says that validity can only be lost along a sequence of extensions, as in :ref{#lem-valid-part}.

:::quiz[valid parts]
In item 1 of :ref{#lem-meta-valid}, why is the cover lemma applied to the cover $A_0, A_1$ although $A$ need not belong to $\mathcal M$?

- [x] Because :ref{#lem-product-cover} holds for every finite cover of $\nat$; only witnesses of non-largeness need to be in $\mathcal M$, and none is needed here.
- [ ] Because $A$ is $\Delta^0_2$ and $M$ is low.

  These hypotheses are used for the complexity of the questions, not here.
- [ ] Because the class $\mathcal U^{\mathbb I_n}_S$ is $\mathcal M$-cohesive.

  No cohesiveness is assumed in this course.

---

In item 2, why is a single slice $\kappa$ enough?

- [x] Because validity of $(J, i)$ only concerns the coordinates $\nu\kappa$ for $\nu \in I$ and $\kappa \in K$, and one slice already gives tuples in $\mathcal U^{\mathbb I_n}_S$ meeting $X_\nu \cap A_i$ infinitely often on $I$.
- [ ] Because $K$ is a singleton.

  $K$ has $2^{m-n}$ elements in general.
- [ ] Because all slices are equal.

  Different slices of a tuple can be different.
:::

## Exercises

::::exercise{difficulty=1}
Compute $u_1$, $u_2$ and the sizes of $\mathbb I_1$ and $\mathbb I_2$, and list the branches of $\mathbb I_1$.

:::solution
$u_1 = \binom{3}{2} \cdot 1 = 3$ and $u_2 = \binom{7}{2} \cdot 3 = 63$. $\mathbb I_1 = \{0, 1, 2\}$ has $3$ elements and $\mathbb I_2 = \mathbb I_1 \cdot \{0, \dots, 6\}$ has $21$. The branches of $\mathbb I_1$ are $\{0, 1\}$, $\{0, 2\}$ and $\{1, 2\}$.
:::
::::

::::exercise{difficulty=2}
Show that if $A$ is finite, then for every meta-condition only parts of the form $(I, 1)$ are valid, and at least one of them is.

:::solution
If $A$ is finite, $X_\nu \cap A_0$ is finite, so $\mathcal L_{\vec X^{I, 0}}$ is empty and no part $(I, 0)$ is valid. By item 1 of :ref{#lem-meta-valid}, some part is valid; it has the form $(I, 1)$.
:::
::::

## Notes and references

The pigeonhole forcing with meta-conditions, the index sets $\mathbb I_n$ with their branches, :ref{#lem-branch-ramsey} and the validity lemma are due to Monin and Patey (2021). The presentation follows the section *Pigeonhole principle* of the chapter *Jump compactness avoidance* of Patey's monograph, with two changes: branches are not equipped with projected classes, and validity is defined by the largeness of $\mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\vec X^{I, i}}$ (the stronger form mentioned in a note of the monograph), which is invariant under finite changes and is what the proofs use.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Pigeonhole principle*.
