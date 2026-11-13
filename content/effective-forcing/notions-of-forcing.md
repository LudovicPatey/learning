---
title: Notions of forcing
summary: Conditions, extensions and the classes of their members; Cohen, Jockusch–Soare, computable Sacks and computable Mathias forcing; filters, dense sets and the existence of generic filters; the set determined by a generic filter.
duration: 45
prerequisites: [cohen-genericity/baire-category, pi01-classes/basis-theorems, immunity-growth/computably-dominated]
---

Several constructions of the previous courses follow one pattern. A set is approximated by a decreasing sequence of objects, each describing a class of candidates: strings in the finite extension method (:ref{to="turing-degrees/finite-extensions"}), non-empty $\Pi^0_1$ classes in the basis theorems (:ref{to="pi01-classes/basis-theorems"}), computable function trees in the construction of computably dominated sets (:ref{to="immunity-growth/computably-dominated"}) and of minimal degrees. Each step passes to a smaller class whose candidates all satisfy one more requirement, and the set built is the last candidate left. Only the kind of approximation and the density arguments differ.

This lesson isolates the common part. A **notion of forcing** is a set of approximations, called conditions, ordered by refinement; a requirement corresponds to a **dense** set of conditions; and a **generic** set is a set built by meeting countably many dense sets. Once this is set up, a construction reduces to two tasks: choosing the conditions, and proving that the relevant sets of conditions are dense. The next lesson collects the dense sets met in earlier courses.

## Conditions and their members

:::definition{#def-forcing-notion}
A **notion of forcing** is a triple $(\mathbb P, \leq, [\cdot])$, where $\mathbb P$ is a set whose elements are called **conditions**, $\leq$ is a preorder on $\mathbb P$ (a reflexive and transitive relation), and $[\cdot]$ assigns to each condition $c$ a non-empty closed class $[c] \subseteq \cs$, whose elements are the **members** of $c$, such that:

1. if $d \leq c$, then $[d] \subseteq [c]$;
2. (**refinement**) for every condition $c$ and every string $\sigma$ with $[c] \cap [\sigma] \neq \emptyset$, there is $d \leq c$ with $[d] \subseteq [\sigma]$.

A condition $d$ **extends** $c$ if $d \leq c$. Two conditions are **compatible** if they have a common extension.
:::

The order is written as in set theory: an extension is *smaller*, since it carries more information and leaves fewer candidates. The members of $c$ are the sets that the construction may still produce once it has reached $c$. Refinement says that conditions can decide arbitrarily long prefixes of the set being built: if some member of $c$ extends $\sigma$, then $c$ can be extended so that every member extends $\sigma$. A preorder rather than a partial order is allowed because conditions are often given by indices, and two indices of the same object extend each other.

:::example{#ex-forcing-notions}
1. **Cohen forcing.** The conditions are the strings, $\tau \leq \sigma$ if $\tau \succeq \sigma$, and $[\sigma]$ is the cylinder of $\sigma$. If $[\sigma] \cap [\rho] \neq \emptyset$, the strings $\sigma$ and $\rho$ are comparable, and the longer one is an extension of $\sigma$ whose cylinder is contained in $[\rho]$.
2. **Jockusch–Soare forcing**, or forcing with $\Pi^0_1$ classes. The conditions are the non-empty $\Pi^0_1$ classes, ordered by inclusion, and $[\mathcal P] = \mathcal P$. If $\mathcal P \cap [\sigma] \neq \emptyset$, then $\mathcal P \cap [\sigma]$ is a non-empty $\Pi^0_1$ class contained in $\mathcal P$ and in $[\sigma]$.
3. **Computable Sacks forcing**, or forcing with computable perfect trees. The conditions are the computable f-trees $T$ of :ref{#def-function-tree}, $S \leq T$ if $S$ is a subtree of $T$ (every node of $S$ is a node of $T$), and $[T]$ is the class of paths of $T$. A set $X$ is a path if and only if for every $k$, some node $T(\rho)$ with $|\rho| = k$ is a prefix of $X$ (the nodes that are prefixes of $X$ are pairwise comparable, so their preimages form a chain, since $T$ preserves the prefix order in both directions); each of these conditions defines a finite union of cylinders, so $[T]$ is closed, and it is non-empty. If some path $X$ of $T$ extends $\sigma$, some node $T(\rho) \prec X$ has length at least $|\sigma|$, and the full subtree above $T(\rho)$ is an extension all of whose paths extend $\sigma$.
4. **Computable Mathias forcing.** The conditions are the Mathias conditions $(\sigma, X)$ of :ref{#def-mathias-condition} whose reservoir is computable: $\sigma$ is a string, the **stem**, and $X$ an infinite computable set, the **reservoir**, with $\min X \geq |\sigma|$. A string $\tau$ is **compatible** with $(\sigma, X)$ if $\sigma \preceq \tau$ and every $n$ with $|\sigma| \leq n < |\tau|$ and $\tau(n) = 1$ belongs to $X$, and $(\tau, Y) \leq (\sigma, X)$ if $\tau$ is compatible with $(\sigma, X)$ and $Y \subseteq X$. The members of $(\sigma, X)$ are the sets that satisfy it in the sense of :ref{#def-mathias-condition}: the sets $G$ with $\sigma \prec G$ and $G(n) = 0$ for every $n \geq |\sigma|$ outside $X$, that is, whose prefixes of length at least $|\sigma|$ are all compatible with $(\sigma, X)$. As in the course on Ramsey's theorem, a string $\sigma$ is identified with the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$, so that $G \setminus \sigma \subseteq X$ for every member $G$. This class is closed, and non-empty since it contains $\sigma 0 0 \cdots$. If a member $G$ extends $\rho$, let $\tau = G \uh \max(|\sigma|, |\rho|)$; then $(\tau, X \setminus \{0, \dots, |\tau| - 1\})$ is an extension all of whose members extend $\rho$.
:::

In the first three examples the conditions are closed classes and the members of a condition are the condition itself. In Mathias forcing the reservoir restricts all future elements of the set, and a condition is extended by adding elements of the reservoir to the stem and by shrinking the reservoir.

:::figure[A condition $c$ and an extension $d$ for each of the four notions of forcing. Each class is drawn through its strings of length $6$ that are prefixes of members, as intervals of Cantor space ordered from $0\cdots$ on the left to $1\cdots$ on the right. In every case $[d] \subseteq [c]$. The Cohen classes are intervals; the others are closed classes with empty interior.]
<svg class="fig" viewBox="0 0 600 330" width="600" role="img" aria-label="For four notions of forcing, a condition and an extension, each drawn as the set of strings of length six that are prefixes of its members"><text x="240" y="14" class="mrm muted" font-size="11">0</text><text x="580" y="14" text-anchor="end" class="mrm muted" font-size="11">1</text><text x="10" y="44" class="label">Cohen</text><line x1="240" y1="29" x2="580" y2="29" class="axis"/><rect x="325.0" y="22" width="85.0" height="14" class="cell"/><text x="232" y="34" text-anchor="end" class="mrm" font-size="12">[c]</text><line x1="240" y1="59" x2="580" y2="59" class="axis"/><rect x="367.5" y="52" width="21.2" height="14" class="cell head-cell"/><text x="232" y="64" text-anchor="end" class="mrm" font-size="12">[d]</text><text x="10" y="60" class="label" font-size="10">c: σ = 01</text><text x="10" y="74" class="label" font-size="10">d: τ = 0110</text><text x="10" y="120" class="label">Jockusch–Soare</text><line x1="240" y1="105" x2="580" y2="105" class="axis"/><rect x="240.0" y="98" width="15.9" height="14" class="cell"/><rect x="261.2" y="98" width="10.6" height="14" class="cell"/><rect x="282.5" y="98" width="15.9" height="14" class="cell"/><rect x="325.0" y="98" width="15.9" height="14" class="cell"/><rect x="346.2" y="98" width="10.6" height="14" class="cell"/><rect x="410.0" y="98" width="15.9" height="14" class="cell"/><rect x="431.2" y="98" width="10.6" height="14" class="cell"/><rect x="452.5" y="98" width="15.9" height="14" class="cell"/><text x="232" y="110" text-anchor="end" class="mrm" font-size="12">[c]</text><line x1="240" y1="135" x2="580" y2="135" class="axis"/><rect x="240.0" y="128" width="15.9" height="14" class="cell head-cell"/><rect x="261.2" y="128" width="10.6" height="14" class="cell head-cell"/><rect x="282.5" y="128" width="15.9" height="14" class="cell head-cell"/><rect x="410.0" y="128" width="15.9" height="14" class="cell head-cell"/><rect x="431.2" y="128" width="10.6" height="14" class="cell head-cell"/><rect x="452.5" y="128" width="15.9" height="14" class="cell head-cell"/><text x="232" y="140" text-anchor="end" class="mrm" font-size="12">[d]</text><text x="10" y="136" class="label" font-size="10">c: no two consecutive 1s</text><text x="10" y="150" class="label" font-size="10">d: and X(1) = 0</text><text x="10" y="196" class="label">computable Sacks</text><line x1="240" y1="181" x2="580" y2="181" class="axis"/><rect x="240.0" y="174" width="5.3" height="14" class="cell"/><rect x="255.9" y="174" width="5.3" height="14" class="cell"/><rect x="303.8" y="174" width="5.3" height="14" class="cell"/><rect x="319.7" y="174" width="5.3" height="14" class="cell"/><rect x="495.0" y="174" width="5.3" height="14" class="cell"/><rect x="510.9" y="174" width="5.3" height="14" class="cell"/><rect x="558.8" y="174" width="5.3" height="14" class="cell"/><rect x="574.7" y="174" width="5.3" height="14" class="cell"/><text x="232" y="186" text-anchor="end" class="mrm" font-size="12">[c]</text><line x1="240" y1="211" x2="580" y2="211" class="axis"/><rect x="240.0" y="204" width="5.3" height="14" class="cell head-cell"/><rect x="255.9" y="204" width="5.3" height="14" class="cell head-cell"/><rect x="303.8" y="204" width="5.3" height="14" class="cell head-cell"/><rect x="319.7" y="204" width="5.3" height="14" class="cell head-cell"/><text x="232" y="216" text-anchor="end" class="mrm" font-size="12">[d]</text><text x="10" y="212" class="label" font-size="10">c: T(ρ): bits of ρ doubled</text><text x="10" y="226" class="label" font-size="10">d: full subtree above T(0)</text><text x="10" y="272" class="label">computable Mathias</text><line x1="240" y1="257" x2="580" y2="257" class="axis"/><rect x="240.0" y="250" width="5.3" height="14" class="cell"/><rect x="250.6" y="250" width="5.3" height="14" class="cell"/><rect x="282.5" y="250" width="5.3" height="14" class="cell"/><rect x="293.1" y="250" width="5.3" height="14" class="cell"/><rect x="410.0" y="250" width="5.3" height="14" class="cell"/><rect x="420.6" y="250" width="5.3" height="14" class="cell"/><rect x="452.5" y="250" width="5.3" height="14" class="cell"/><rect x="463.1" y="250" width="5.3" height="14" class="cell"/><text x="232" y="262" text-anchor="end" class="mrm" font-size="12">[c]</text><line x1="240" y1="287" x2="580" y2="287" class="axis"/><rect x="410.0" y="280" width="5.3" height="14" class="cell head-cell"/><rect x="420.6" y="280" width="5.3" height="14" class="cell head-cell"/><text x="232" y="292" text-anchor="end" class="mrm" font-size="12">[d]</text><text x="10" y="288" class="label" font-size="10">c: (ε, even numbers)</text><text x="10" y="302" class="label" font-size="10">d: (1, multiples of 4 from 4)</text></svg>
:::

Many variants are used in the literature, obtained by restricting the conditions: Jockusch–Soare forcing inside a fixed class, for instance the class of $\{0, 1\}$-valued DNC functions; Mathias forcing with reservoirs computable in a fixed set $Z$, or not computing a fixed set, or belonging to a fixed Scott ideal, as in the proof of the Dzhafarov–Jockusch theorem (:ref{to="ramsey-theorem/cone-avoidance"}). The definition is designed to cover all of them. For a class $\mathcal M$ of sets, **Mathias forcing with reservoirs in $\mathcal M$** has the conditions $(\sigma, X)$ with $X \in \mathcal M$ infinite, ordered as in item 4; refinement holds, by the same argument, whenever $\mathcal M$ is closed under removing finitely many elements. The later courses of the track use these conventions.

:::remark{#rem-refinement-needed}
Refinement is a real restriction. Let the conditions be the closed classes of positive Lebesgue measure, ordered by inclusion, each being its own class of members. The class $\mathcal P = [0] \cup \{ 1 0 0 \cdots \}$ has measure $\tfrac12$ and meets $[1]$, but every closed subclass of $\mathcal P \cap [1] = \{ 1 0 0 \cdots \}$ has measure $0$; so no extension of $\mathcal P$ has all its members in $[1]$, and refinement fails for $\sigma = 1$: the member $1 0 0 \cdots$ of $\mathcal P$ is never singled out by a condition. Forcing with classes of positive measure is used in randomness, with a separate argument; it is not a notion of forcing in the sense of :ref{#def-forcing-notion}.
:::

:::quiz[notions of forcing]
In the refinement property of Jockusch–Soare forcing, why is the hypothesis $\mathcal P \cap [\sigma] \neq \emptyset$ needed for $\mathcal P \cap [\sigma]$ to be an extension of $\mathcal P$?

- [x] Because conditions must be non-empty classes, and $\mathcal P \cap [\sigma]$ is a $\Pi^0_1$ class in any case, but a condition only if it has a member.
- [ ] Because otherwise $\mathcal P \cap [\sigma]$ is not $\Pi^0_1$.

  The intersection of two $\Pi^0_1$ classes is always $\Pi^0_1$; the issue is emptiness.
- [ ] Because otherwise $\mathcal P \cap [\sigma]$ is not contained in $\mathcal P$.

  It is always contained in $\mathcal P$.

---

In computable Mathias forcing, why is the finite set $\sigma 0 0 \cdots$ a member of $(\sigma, X)$, although the sets built by the construction are infinite?

- [x] Because the members are all the sets compatible with the commitments made so far, and adding no further element breaks none of them; infinity is a requirement met later, by a dense set of conditions.
- [ ] Because $X$ may be finite.

  Reservoirs are infinite by definition.
- [ ] Because the members of a condition are its extensions.

  Members are sets, extensions are conditions; the class $[c]$ is closed, so it contains limits of finite sets.
:::

## Filters and generic sets

:::definition{#def-generic-filter}
Let $(\mathbb P, \leq, [\cdot])$ be a notion of forcing.

1. A **filter** is a non-empty set $F \subseteq \mathbb P$ that is closed upward ($c \in F$ and $c \leq d$ imply $d \in F$) and in which any two conditions have a common extension in $F$.
2. A set $D \subseteq \mathbb P$ is **dense** if every condition has an extension in $D$, and **dense below** a condition $c$ if every extension of $c$ has an extension in $D$.
3. A filter $F$ **meets** $D$ if $F \cap D \neq \emptyset$. If $\mathcal D$ is a family of dense sets, $F$ is **$\mathcal D$-generic** if it meets every member of $\mathcal D$.
:::

A decreasing sequence $c_0 \geq c_1 \geq \cdots$ **generates** the filter $\{ d : c_i \leq d \text{ for some } i \}$. This is the form in which filters appear in constructions; filters are convenient because statements about them do not depend on the choice of a generating sequence.

:::lemma[Rasiowa–Sikorski]{#lem-rasiowa-sikorski}
For every countable family $\mathcal D = \{ D_0, D_1, \dots \}$ of dense sets and every condition $c$, there is a $\mathcal D$-generic filter containing $c$, generated by a decreasing sequence.
:::

:::proof{of=lem-rasiowa-sikorski}
Let $c_0 = c$, and let $c_{i+1}$ be an extension of $c_i$ in $D_i$, which exists by density. The filter generated by $(c_i)$ is closed upward by definition; two of its elements lie above some $c_i$ and $c_j$, and $c_{\max(i, j)}$ is a common extension in the filter. It contains $c$ and meets every $D_i$.
:::

The set built is read off the filter. For $n \in \nat$, let $S_n$ be the set of conditions all of whose members have the same prefix of length $n$. By refinement, $S_n$ is dense: a condition $c$ has a member $X$, and an extension $d$ with $[d] \subseteq [X \uh n]$.

:::lemma{#lem-generic-set}
Let $F$ be a filter that meets every $S_n$. There is a unique set $G_F$ that is a member of every condition of $F$: $\bigcap_{c \in F} [c] = \{ G_F \}$.
:::

:::proof{of=lem-generic-set}
For $d \in F \cap S_n$, let $\sigma_d$ be the common prefix of length $n$ of the members of $d$. If $d, d' \in F \cap S_n$, a common extension $e \in F$ has a member, which extends both $\sigma_d$ and $\sigma_{d'}$; so $\sigma_d = \sigma_{d'}$, and we call this string $\sigma_n$. In the same way $\sigma_n \prec \sigma_{n+1}$. Let $G_F$ be the set with prefixes $\sigma_0 \prec \sigma_1 \prec \cdots$.

Let $c \in F$ and $n \in \nat$. Take $d \in F \cap S_n$ and a common extension $e \in F$ of $c$ and $d$. Then $\emptyset \neq [e] \subseteq [c] \cap [\sigma_n]$. So $[c]$ meets every cylinder $[G_F \uh n]$, and since $[c]$ is closed, $G_F \in [c]$. Any member of every condition of $F$ extends every $\sigma_n$, so it equals $G_F$.
:::

From now on, every family of dense sets is assumed to contain the sets $S_n$, so that every generic filter $F$ determines a set $G_F$, called the **generic set** of $F$. If $F$ is generated by $c_0 \geq c_1 \geq \cdots$, then $\{ G_F \} = \bigcap_i [c_i]$, since every condition of $F$ lies above some $c_i$. A set is **$\mathcal D$-generic** if it is $G_F$ for some $\mathcal D$-generic filter $F$.


:::quiz[generic filters]
In the proof of :ref{#lem-generic-set}, where is it used that the classes $[c]$ are closed?

- [x] To conclude from "$[c]$ meets every cylinder $[G_F \uh n]$" that $G_F \in [c]$.
- [ ] To show that the strings $\sigma_d$ for $d \in F \cap S_n$ coincide.

  This uses only that common extensions have members.
- [ ] To show that $S_n$ is dense.

  Density of $S_n$ comes from refinement and non-emptiness.
:::

## Notes and references

Forcing was invented by Cohen (1963) in set theory; Feferman (1965) adapted it to arithmetic, and Jockusch (1980) made Cohen genericity a standard tool of computability theory. The existence of generic filters is the lemma of Rasiowa and Sikorski (1950). Forcing with $\Pi^0_1$ classes comes from Jockusch and Soare (1972), forcing with perfect trees from Spector (1956) and, in set theory, Sacks (1971), and Mathias forcing from Mathias (1977). The definition of a notion of forcing used here, with a closed class of members for each condition and the refinement property, follows the chapter *Effective forcing* of Monin and Patey, where such notions are called Cantor forcings. Dzhafarov and Mummert (Section 7.2, Definition 7.2.1) use instead a valuation map giving the prefix decided by each condition; Hirschfeldt (Section 2.3, Propositions 2.6 and 2.7) presents generic filters and their effective existence. The conventions for Mathias conditions (stem, reservoir, compatible strings) are those of the course on Ramsey's theorem and of Patey's monograph *Lowness and avoidance*.

- H. Rasiowa and R. Sikorski, *A proof of the completeness theorem of Gödel*, Fundamenta Mathematicae 37 (1950), 193–200.
- P. J. Cohen, *The independence of the continuum hypothesis*, Proceedings of the National Academy of Sciences 50 (1963), 1143–1148.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- G. E. Sacks, *Forcing with perfect closed sets*, in *Axiomatic Set Theory*, Proceedings of Symposia in Pure Mathematics 13, Part I, American Mathematical Society, 1971, 331–355.
- A. R. D. Mathias, *Happy families*, Annals of Mathematical Logic 12 (1977), 59–111.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 2.3.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 7.2–7.3.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Fundamentals of forcing*.
