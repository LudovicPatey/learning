---
title: Genericity and Baire category
summary: Dense sets of strings and generic sets; meager and co-meager classes of Cantor space; the Baire category theorem; properties of sufficiently generic sets.
duration: 50
prerequisites: [turing-degrees/finite-extensions]
---

The finite extension method builds a set by meeting, one after the other, countably many dense sets of strings. Cohen's **forcing** turns this method into a theory: instead of building one set for one list of requirements, it studies the sets that meet *every* dense set from a given countable family — the **generic** sets — and the properties that all sufficiently generic sets share. In topological terms, these are the properties that hold on a **co-meager** class, a notion introduced by Baire long before Cohen. This lesson sets up the two points of view and the Baire category theorem, which guarantees that co-meager classes are large. The following lessons make genericity effective.

The technique throughout the course is the finite extension method of the course on Turing degrees (:ref{#lem-meet-dense}). What changes is the point of view: a construction by finite extensions is now read as a list of dense sets, and a theorem of the form "there is a set with property $P$" becomes "every sufficiently generic set has property $P$".

## Generic sets

Recall from :ref{#def-dense} that a set of strings $D \subseteq \bstr$ is **dense** if every string has an extension in $D$, and that a set $G$ **meets** $D$ if some prefix of $G$ belongs to $D$.

:::definition{#def-d-generic}
Let $\mathcal D = (D_n)_{n \in \nat}$ be a sequence of dense sets of strings. A set $G$ is **$\mathcal D$-generic** if it meets every $D_n$.
:::

By :ref{#lem-meet-dense}, $\mathcal D$-generic sets exist, and one extends any given string $\sigma$: start the construction from $\sigma$. A single set cannot be generic for all dense sets: the set $\{ \sigma : \sigma \not\prec G \}$ is dense and $G$ does not meet it. Genericity is therefore always relative to a countable family of dense sets, and statements are made about **sufficiently generic** sets.

:::definition{#def-sufficiently-generic}
A property of sets **holds for all sufficiently generic sets** if there is a sequence $\mathcal D$ of dense sets of strings such that every $\mathcal D$-generic set has the property.
:::

If two properties hold for all sufficiently generic sets, witnessed by $\mathcal D$ and $\mathcal E$, then both hold for all sets generic for the merged sequence $D_0, E_0, D_1, E_1, \dots$. The same holds for countably many properties, by merging countably many sequences into one through a pairing function. This closure under countable conjunctions is what makes the notion useful: a single sufficiently generic set has all the countably many properties one wishes to consider at once.

:::example{#ex-generic-properties}
1. Every sufficiently generic set is infinite and coinfinite: the sets $\{ \sigma : \exists n \geq m\ \sigma(n) = 1 \}$ and $\{ \sigma : \exists n \geq m\ \sigma(n) = 0 \}$ are dense for each $m$.
2. Every sufficiently generic set is different from any given countable family of sets $(X_k)$: the sets $\{ \sigma : \sigma \not\prec X_k \}$ are dense. In particular, sufficiently generic sets are not computable.
3. For every non-computable set $C$, every sufficiently generic set fails to compute $C$: the sets $D_e$ of :ref{#thm-cone-avoidance} are dense.
4. A sufficiently generic set contains, for every $k$, a block of $k$ consecutive elements, and also a block of $k$ consecutive non-elements: the sets of strings containing $1^k$, or $0^k$, are dense. So the set of even numbers, or any set whose elements are spread out at regular distance, has a property that sufficiently generic sets do not have.
:::

In each item, the property is a conjunction of countably many requirements, and each requirement can be secured by a finite extension, whatever finite part of the set has been fixed. A requirement that cannot be secured in this way is not satisfied by generic sets: for instance "$0 \in G$" holds for some generic sets and fails for others, since both $\{ \sigma : \sigma(0) = 1 \}$ and $\{ \sigma : \sigma(0) = 0 \}$ fail to be dense.

:::quiz[sufficiently generic sets]
Why can no set $G$ be generic for **all** dense sets of strings?

- [x] Because $\{ \sigma : \sigma \not\prec G \}$ is dense, and $G$ does not meet it by definition.
- [ ] Because there are uncountably many dense sets, and a construction can only meet countably many.

  The construction argument shows that a countable family can be met; the impossibility for all dense sets comes from the particular dense set built from $G$.
- [ ] Because a dense set may be empty.

  A dense set is never empty: the empty string has an extension in it.

---

Which properties hold for all sufficiently generic sets?

- [x] Being different from every computable set.

  The countably many sets $\{ \sigma : \sigma \not\prec X \}$, for $X$ computable, are dense.
- [x] Having infinitely many elements of the form $2n$.

  For each $m$, the set of strings with a $1$ at some even position at least $m$ is dense.
- [ ] Being equal to the set of even numbers.

  The set $\{ \sigma : \sigma \text{ has a } 1 \text{ at some odd position} \}$ is dense, so sufficiently generic sets contain odd numbers.
:::

## Meager and co-meager classes

Dense sets of strings correspond to dense open classes. Recall that a class $\mathcal U \subseteq \cs$ is **open** if it is a union of cylinders, and **closed** if its complement is open; for a set of strings $D$, write $[D]^{\prec} = \bigcup_{\sigma \in D} [\sigma]$ (:ref{#def-open-closed}). A class $\mathcal B \subseteq \cs$ is **dense** if it meets every cylinder.

:::lemma{#lem-dense-open}
1. If $D$ is a dense set of strings, then $[D]^{\prec}$ is a dense open class, and a set meets $D$ if and only if it belongs to $[D]^{\prec}$.
2. If $\mathcal U$ is a dense open class, the set $D = \{ \sigma : [\sigma] \subseteq \mathcal U \}$ is a dense set of strings with $[D]^{\prec} = \mathcal U$.
:::

:::proof{of=lem-dense-open}
1. A set belongs to $[D]^{\prec}$ exactly when one of its prefixes is in $D$. For a cylinder $[\sigma]$, an extension $\tau \in D$ of $\sigma$ gives $[\tau] \subseteq [\sigma] \cap [D]^{\prec}$.
2. An open class is the union of the cylinders it contains, so $[D]^{\prec} = \mathcal U$. Given $\sigma$, the class $\mathcal U \cap [\sigma]$ is non-empty, since $\mathcal U$ is dense, and open, so it contains a cylinder $[\tau]$. Then $[\tau] \subseteq [\sigma]$ gives $\tau \succeq \sigma$, and $[\tau] \subseteq \mathcal U$ gives $\tau \in D$.
:::

The second half of the dictionary concerns the classes that genericity avoids. A dense open class is large in the sense that it leaves no room: every cylinder contains a cylinder inside it. Its complement is small in the dual sense.

:::definition{#def-meager}
A class is **nowhere dense** if its closure has empty interior, that is, if every cylinder $[\sigma]$ contains a cylinder $[\tau]$ disjoint from the class. A class is **meager** if it is contained in a countable union of nowhere dense classes, and **co-meager** if its complement is meager.
:::

:::example{#ex-nowhere-dense}
1. A singleton $\{ X \}$ is nowhere dense: the cylinder $[\sigma]$ contains $[\sigma\, (1 - X(|\sigma|))]$, which avoids $X$ whenever $\sigma \prec X$, and $[\sigma]$ itself avoids $X$ otherwise. Hence every countable class is meager.
2. A closed class is nowhere dense if and only if it contains no cylinder. For instance $\{ X : X(2n) = 0 \text{ for every } n \}$ is closed and contains no cylinder, so it is nowhere dense, although it has the cardinality of the continuum.
3. The class $\mathcal F$ of finite sets is dense, since every cylinder $[\sigma]$ contains the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$, and it is meager, since it is countable. So a dense class can be meager. The class of cofinite sets is also dense and meager, and disjoint from $\mathcal F$: the intersection of two dense classes may be empty. This is why genericity is defined with dense *open* classes, that is, with dense sets of strings.
:::

Equivalently, a class is co-meager if and only if it contains a countable intersection of dense open classes: the complement of a nowhere dense class contains a dense open class, namely the union of the cylinders disjoint from it; conversely, the complement of a dense open class is nowhere dense, since every cylinder contains a cylinder included in the dense open class. By :ref{#lem-dense-open}, this gives the link with genericity.

:::proposition{#prop-generic-comeager}
A property holds for all sufficiently generic sets if and only if the class of sets with the property is co-meager.
:::

:::proof{of=prop-generic-comeager}
If every $\mathcal D$-generic set has the property, the class contains $\bigcap_n [D_n]^{\prec}$, a countable intersection of dense open classes, by :ref{#lem-dense-open}. Conversely, if the class contains $\bigcap_n \mathcal U_n$ with $\mathcal U_n$ dense open, the sets $D_n = \{ \sigma : [\sigma] \subseteq \mathcal U_n \}$ are dense, and every set meeting all of them lies in $\bigcap_n \mathcal U_n$.
:::

Countable unions of meager classes are meager, and countable intersections of co-meager classes are co-meager; on the side of genericity, this is the merging of countably many sequences of dense sets.

## The Baire category theorem

Two questions arise: whether a co-meager class is non-empty, and how large it is. The finite extension method answers the first one: some set meets every dense set of a countable family. To show that there are many such sets, the construction is made to branch. At each step, instead of one extension, it builds two incompatible ones, by first adding a bit $0$ or a bit $1$ and then extending into the next dense set. The result is a perfect tree of strings whose paths are all generic, and distinct paths of the binary tree give distinct generic sets.

:::theorem[Baire category theorem]{#thm-baire-category}
Every co-meager class $\mathcal B \subseteq \cs$ meets every cylinder. More precisely, for every string $\sigma$, there is an injective map $X \mapsto G_X$ from $\cs$ into $\mathcal B \cap [\sigma]$. In particular, no cylinder is meager, and every co-meager class has the cardinality of the continuum.
:::

:::proof{of=thm-baire-category}
Let $\bigcap_n \mathcal U_n \subseteq \mathcal B$ with $\mathcal U_n$ dense open, and let $D_n = \{ \tau : [\tau] \subseteq \mathcal U_n \}$, dense by :ref{#lem-dense-open}. Fix an enumeration of $\bstr$. Define strings $\sigma_\rho$ for $\rho \in \bstr$: let $\sigma_\varepsilon = \sigma$, and for $i \in \{0, 1\}$, let $\sigma_{\rho i}$ be the first extension of $\sigma_\rho\, i$ in $D_{|\rho|}$. The strings $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ are incompatible, since they extend $\sigma_\rho 0$ and $\sigma_\rho 1$. For $X \in \cs$, let $G_X$ be the sequence extending every $\sigma_{X \uh n}$; it meets every $D_n$, through $\sigma_{X \uh (n+1)}$, so $G_X \in \bigcap_n \mathcal U_n$, and it extends $\sigma$. Different $X$ give different $G_X$, by the incompatibility of the splitting strings.
:::

:::figure[The construction of :ref{#thm-baire-category}, drawn with cylinders as intervals. Inside each cylinder $[\sigma_\rho]$, the dashed halves are $[\sigma_\rho 0]$ and $[\sigma_\rho 1]$; inside each half, the construction chooses the cylinder of an extension in the next dense set. Distinct branches give disjoint cylinders, and the branch $X$ determines a single point $G_X$.]
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Nested cylinders in the proof of the Baire category theorem: each cylinder of the construction splits into two halves, and inside each half the construction chooses a smaller cylinder belonging to the next dense set"><line x1="40.0" y1="36" x2="520.0" y2="36" class="accent-stroke" stroke-width="3"/><line x1="40.0" y1="31" x2="40.0" y2="41" class="accent-stroke" stroke-width="1.2"/><line x1="520.0" y1="31" x2="520.0" y2="41" class="accent-stroke" stroke-width="1.2"/><text x="280.0" y="60" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">ε</tspan></text><line x1="41.0" y1="95" x2="279.0" y2="95" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="41.0" y1="91" x2="41.0" y2="99" class="muted-stroke" stroke-width="1"/><line x1="279.0" y1="91" x2="279.0" y2="99" class="muted-stroke" stroke-width="1"/><line x1="64.0" y1="104" x2="220.0" y2="104" class="accent-stroke" stroke-width="3"/><line x1="64.0" y1="99" x2="64.0" y2="109" class="accent-stroke" stroke-width="1.2"/><line x1="220.0" y1="99" x2="220.0" y2="109" class="accent-stroke" stroke-width="1.2"/><text x="142.0" y="128" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="281.0" y1="95" x2="519.0" y2="95" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="281.0" y1="91" x2="281.0" y2="99" class="muted-stroke" stroke-width="1"/><line x1="519.0" y1="91" x2="519.0" y2="99" class="muted-stroke" stroke-width="1"/><line x1="352.0" y1="104" x2="496.0" y2="104" class="ink-stroke" stroke-width="2"/><line x1="352.0" y1="99" x2="352.0" y2="109" class="ink-stroke" stroke-width="1.2"/><line x1="496.0" y1="99" x2="496.0" y2="109" class="ink-stroke" stroke-width="1.2"/><text x="424.0" y="128" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><line x1="65.0" y1="163" x2="141.0" y2="163" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="65.0" y1="159" x2="65.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="141.0" y1="159" x2="141.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="79.6" y1="172" x2="130.3" y2="172" class="ink-stroke" stroke-width="2"/><line x1="79.6" y1="167" x2="79.6" y2="177" class="ink-stroke" stroke-width="1.2"/><line x1="130.3" y1="167" x2="130.3" y2="177" class="ink-stroke" stroke-width="1.2"/><text x="104.95" y="196" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">00</tspan></text><line x1="143.0" y1="163" x2="219.0" y2="163" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="143.0" y1="159" x2="143.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="219.0" y1="159" x2="219.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="145.9" y1="172" x2="188.8" y2="172" class="accent-stroke" stroke-width="3"/><line x1="145.9" y1="167" x2="145.9" y2="177" class="accent-stroke" stroke-width="1.2"/><line x1="188.8" y1="167" x2="188.8" y2="177" class="accent-stroke" stroke-width="1.2"/><text x="167.35000000000002" y="196" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">01</tspan></text><line x1="353.0" y1="163" x2="423.0" y2="163" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="353.0" y1="159" x2="353.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="423.0" y1="159" x2="423.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="377.2" y1="172" x2="420.4" y2="172" class="ink-stroke" stroke-width="2"/><line x1="377.2" y1="167" x2="377.2" y2="177" class="ink-stroke" stroke-width="1.2"/><line x1="420.4" y1="167" x2="420.4" y2="177" class="ink-stroke" stroke-width="1.2"/><text x="398.79999999999995" y="196" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">10</tspan></text><line x1="425.0" y1="163" x2="495.0" y2="163" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="425.0" y1="159" x2="425.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="495.0" y1="159" x2="495.0" y2="167" class="muted-stroke" stroke-width="1"/><line x1="431.2" y1="172" x2="474.4" y2="172" class="ink-stroke" stroke-width="2"/><line x1="431.2" y1="167" x2="431.2" y2="177" class="ink-stroke" stroke-width="1.2"/><line x1="474.4" y1="167" x2="474.4" y2="177" class="ink-stroke" stroke-width="1.2"/><text x="452.79999999999995" y="196" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">11</tspan></text><line x1="80.6" y1="231" x2="104.0" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="80.6" y1="227" x2="80.6" y2="235" class="muted-stroke" stroke-width="1"/><line x1="104.0" y1="227" x2="104.0" y2="235" class="muted-stroke" stroke-width="1"/><line x1="84.7" y1="240" x2="99.9" y2="240" class="ink-stroke" stroke-width="2"/><line x1="84.7" y1="235" x2="84.7" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="99.9" y1="235" x2="99.9" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="106.0" y1="231" x2="129.3" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="106.0" y1="227" x2="106.0" y2="235" class="muted-stroke" stroke-width="1"/><line x1="129.3" y1="227" x2="129.3" y2="235" class="muted-stroke" stroke-width="1"/><line x1="107.5" y1="240" x2="122.7" y2="240" class="ink-stroke" stroke-width="2"/><line x1="107.5" y1="235" x2="107.5" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="122.7" y1="235" x2="122.7" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="146.9" y1="231" x2="166.4" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="146.9" y1="227" x2="146.9" y2="235" class="muted-stroke" stroke-width="1"/><line x1="166.4" y1="227" x2="166.4" y2="235" class="muted-stroke" stroke-width="1"/><line x1="152.3" y1="240" x2="165.2" y2="240" class="ink-stroke" stroke-width="2"/><line x1="152.3" y1="235" x2="152.3" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="165.2" y1="235" x2="165.2" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="168.4" y1="231" x2="187.8" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="168.4" y1="227" x2="168.4" y2="235" class="muted-stroke" stroke-width="1"/><line x1="187.8" y1="227" x2="187.8" y2="235" class="muted-stroke" stroke-width="1"/><line x1="171.6" y1="240" x2="183.4" y2="240" class="ink-stroke" stroke-width="2"/><line x1="171.6" y1="235" x2="171.6" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="183.4" y1="235" x2="183.4" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="378.2" y1="231" x2="397.8" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="378.2" y1="227" x2="378.2" y2="235" class="muted-stroke" stroke-width="1"/><line x1="397.8" y1="227" x2="397.8" y2="235" class="muted-stroke" stroke-width="1"/><line x1="379.4" y1="240" x2="391.2" y2="240" class="ink-stroke" stroke-width="2"/><line x1="379.4" y1="235" x2="379.4" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="391.2" y1="235" x2="391.2" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="399.8" y1="231" x2="419.4" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="399.8" y1="227" x2="399.8" y2="235" class="muted-stroke" stroke-width="1"/><line x1="419.4" y1="227" x2="419.4" y2="235" class="muted-stroke" stroke-width="1"/><line x1="404.2" y1="240" x2="417.2" y2="240" class="ink-stroke" stroke-width="2"/><line x1="404.2" y1="235" x2="404.2" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="417.2" y1="235" x2="417.2" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="432.2" y1="231" x2="451.8" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="432.2" y1="227" x2="432.2" y2="235" class="muted-stroke" stroke-width="1"/><line x1="451.8" y1="227" x2="451.8" y2="235" class="muted-stroke" stroke-width="1"/><line x1="437.7" y1="240" x2="450.6" y2="240" class="ink-stroke" stroke-width="2"/><line x1="437.7" y1="235" x2="437.7" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="450.6" y1="235" x2="450.6" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="453.8" y1="231" x2="473.4" y2="231" class="muted-stroke" stroke-width="1" stroke-dasharray="3 3"/><line x1="453.8" y1="227" x2="453.8" y2="235" class="muted-stroke" stroke-width="1"/><line x1="473.4" y1="227" x2="473.4" y2="235" class="muted-stroke" stroke-width="1"/><line x1="455.0" y1="240" x2="465.8" y2="240" class="ink-stroke" stroke-width="2"/><line x1="455.0" y1="235" x2="455.0" y2="245" class="ink-stroke" stroke-width="1.2"/><line x1="465.8" y1="235" x2="465.8" y2="245" class="ink-stroke" stroke-width="1.2"/><text x="538" y="40" class="label">[σ]</text><text x="538" y="108" class="label">in D<tspan font-size="9" dy="3">0</tspan></text><text x="538" y="176" class="label">in D<tspan font-size="9" dy="3">1</tspan></text><text x="538" y="244" class="label">in D<tspan font-size="9" dy="3">2</tspan></text><circle cx="158.8" cy="266" r="3.5" class="accent-fill"/><text x="158.77" y="286" text-anchor="middle" class="math" font-size="14">G<tspan class="mrm" font-size="9" dy="4">X</tspan></text><text x="176.8" y="286" class="label">for X = 01…</text></svg>
:::

The theorem expresses that co-meager classes are large, and meager classes small, in a topological sense. This notion of size is independent of measure: by the strong law of large numbers (admitted here), the class of sets of asymptotic density $\tfrac12$ has measure $1$, and it is meager by :ref{#exr-density-meager}; its complement is a co-meager class of measure $0$. In the rest of this course, "typical" means "sufficiently generic", that is, belonging to a co-meager class.

:::quiz[the Baire category theorem]
In the proof of :ref{#thm-baire-category}, why does $\sigma_{\rho i}$ extend $\sigma_\rho\, i$, and not only $\sigma_\rho$?

- [x] To make $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ incompatible, so that different branches give different sets.
- [ ] To make $\sigma_{\rho i}$ belong to $D_{|\rho|}$.

  Membership in $D_{|\rho|}$ comes from the choice of an extension in it, which exists by density.
- [ ] Because $D_{|\rho|}$ only contains strings ending with $i$.

  Nothing is assumed about the last bits of the strings in $D_n$.

---

Is the class $\{ X : X(2n) = 0 \text{ for every } n \}$ meager?

- [x] Yes: it is closed and contains no cylinder, so it is nowhere dense.

  Every cylinder $[\sigma]$ contains the cylinder $[\sigma\, 1\, 1]$, whose sets have a $1$ at an even position.
- [ ] No: it is uncountable.

  Meager classes can be uncountable; this one has the cardinality of the continuum.
- [ ] No: it is closed.

  Closed classes with empty interior are meager; cylinders are closed and not meager.
:::

:::aside[Banach–Mazur games]
Genericity has a description in terms of games. Given a class $\mathcal B$, two players alternately extend a string: player I chooses $\tau_0$, player II chooses $\tau_1 \succ \tau_0$, player I chooses $\tau_2 \succ \tau_1$, and so on; player II wins if the set extending all the $\tau_k$ belongs to $\mathcal B$. If $\mathcal B$ contains $\bigcap_n [D_n]^{\prec}$ with each $D_n$ dense, player II wins by answering, at her $n$-th move, with a proper extension in $D_n$ of the current string. Conversely, Banach showed that if player II has a winning strategy, then $\mathcal B$ is co-meager. A finite extension construction is thus a strategy for player II in which the opponent's moves are the finite parts fixed so far. This converse is admitted here; see Soare (2016, Theorem 14.1.3, stated there with the roles of the players exchanged).
:::

## Exercises

::::exercise{difficulty=1}
Show that the class of computable sets is meager, and that the class of sets computing $\emptyset'$ is meager.

:::solution
The class of computable sets is countable, hence meager. By :ref{#thm-cone-avoidance}, the sets $D_e = \{ \tau : \exists x\ \Phi^\tau_e(x)\converge \neq \emptyset'(x) \} \cup \{ \tau : \exists x\ \forall \rho \succeq \tau\ \Phi^\rho_e(x)\diverge \}$ are dense, and a set meeting all of them does not compute $\emptyset'$. By :ref{#prop-generic-comeager}, the class of sets not computing $\emptyset'$ is co-meager.
:::
::::

::::exercise{difficulty=1}
Show that a closed class is meager if and only if it is nowhere dense, if and only if it contains no cylinder.

:::solution
Nowhere dense classes are meager. A meager class contains no cylinder, since by :ref{#thm-baire-category} no cylinder is meager and a subclass of a meager class is meager. It remains to show that a closed class $\mathcal C$ containing no cylinder is nowhere dense. Given $\sigma$, the cylinder $[\sigma]$ is not included in $\mathcal C$; pick $X \in [\sigma] \setminus \mathcal C$. Since the complement of $\mathcal C$ is open, there is $\tau \prec X$ with $[\tau] \cap \mathcal C = \emptyset$. For $n = \max(|\sigma|, |\tau|)$, the cylinder $[X \uh n]$ is included in $[\sigma] \cap [\tau]$, hence disjoint from $\mathcal C$.
:::
::::

::::exercise{#exr-density-meager difficulty=2}
For a set $X$ and $n \geq 1$, let $\delta_n(X) = |X \cap \{0, \dots, n-1\}| / n$. Show that for every sufficiently generic set $G$, $\limsup_n \delta_n(G) = 1$ and $\liminf_n \delta_n(G) = 0$. Deduce that the class of sets with asymptotic density $\tfrac12$ is meager.

:::solution
For $k \geq 1$, let $D_k$ be the set of strings $\sigma$ having a prefix $\tau$ of length $n \geq k$ with $|\{ i < n : \tau(i) = 1 \}| \geq (1 - 1/k)\, n$. It is dense: any string $\sigma$ extended by $k |\sigma| + k$ ones has a prefix, itself, of the required kind. Similarly the sets $E_k$, with zeros in place of ones, are dense. A set meeting every $D_k$ has $\delta_n(G) \geq 1 - 1/k$ for some $n \geq k$, for every $k$, so $\limsup_n \delta_n(G) = 1$; symmetrically $\liminf_n \delta_n(G) = 0$. Such a set has no asymptotic density, so the class of sets of density $\tfrac12$ is contained in a meager class.
:::
::::

## Notes and references

Baire introduced meager classes, under the name of sets of first category, in his thesis (1899), to study the limits of continuous functions. Cohen invented forcing in 1963 to prove the independence of the continuum hypothesis, and Feferman (1965) adapted it to arithmetic. The systematic use of genericity in computability theory is due to Jockusch (1980). Mazur introduced his game in 1928, and Banach proved the characterization of co-meager classes by winning strategies (Soare 2016, §14.1). Oxtoby's book compares measure and category. The correspondence between dense sets of strings and dense open classes is presented in the same way in Monin and Patey (chapter *Cohen forcing*, section on $\Sigma^0_1$ forcing, the topological approach) and in Soare (2016, §14.1).

- R. Baire, *Sur les fonctions de variables réelles*, Annali di Matematica Pura ed Applicata (3) 3 (1899), 1–123.
- P. J. Cohen, *The independence of the continuum hypothesis*, Proceedings of the National Academy of Sciences 50 (1963), 1143–1148.
- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- J. C. Oxtoby, *Measure and Category*, 2nd edition, Graduate Texts in Mathematics 2, Springer, 1980.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §14.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Cohen forcing*.
