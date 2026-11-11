---
title: Genericity and Baire category
summary: Dense sets of strings and generic sets; meager and co-meager classes of Cantor space; the Baire category theorem; properties of sufficiently generic sets.
duration: 40
prerequisites: [turing-degrees/finite-extensions]
---

The finite extension method builds a set by meeting, one after the other, countably many dense sets of strings. Cohen's **forcing** turns this method into a theory: instead of building one set for one list of requirements, it studies the sets that meet *every* dense set from a given countable family — the **generic** sets — and the properties that all sufficiently generic sets share. In topological terms, these are the properties that hold on a **co-meager** class, a notion introduced by Baire long before Cohen. This lesson sets up the two points of view and the Baire category theorem, which guarantees that co-meager classes are large. The following lessons make genericity effective.

## Generic sets

Recall from :ref{#def-dense} that a set of strings $D \subseteq \bstr$ is **dense** if every string has an extension in $D$, and that a set $G$ **meets** $D$ if some prefix of $G$ belongs to $D$.

:::definition{#def-d-generic}
Let $\mathcal D = (D_n)_{n \in \nat}$ be a sequence of dense sets of strings. A set $G$ is **$\mathcal D$-generic** if it meets every $D_n$.
:::

By :ref{#lem-meet-dense}, $\mathcal D$-generic sets exist, and one extends any given string $\sigma$: start the construction from $\sigma$. A single set cannot be generic for all dense sets: the set $\{ \sigma : \sigma \not\prec G \}$ is dense and $G$ does not meet it. Genericity is therefore always relative to a countable family of dense sets, and statements are made about **sufficiently generic** sets.

:::definition{#def-sufficiently-generic}
A property of sets **holds for all sufficiently generic sets** if there is a sequence $\mathcal D$ of dense sets of strings such that every $\mathcal D$-generic set has the property.
:::

If two properties hold for all sufficiently generic sets, witnessed by $\mathcal D$ and $\mathcal E$, then both hold for all sets generic for the merged sequence. The same holds for countably many properties, by merging countably many sequences into one.

:::example{#ex-generic-properties}
1. Every sufficiently generic set is infinite and coinfinite: the sets $\{ \sigma : \exists n \geq m\ \sigma(n) = 1 \}$ and $\{ \sigma : \exists n \geq m\ \sigma(n) = 0 \}$ are dense for each $m$.
2. Every sufficiently generic set is different from any given countable family of sets $(X_k)$: the sets $\{ \sigma : \sigma \not\prec X_k \}$ are dense. In particular, sufficiently generic sets are not computable.
3. For every non-computable set $C$, every sufficiently generic set fails to compute $C$: the sets $D_e$ of :ref{#thm-cone-avoidance} are dense.
:::

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

:::definition{#def-meager}
A class is **nowhere dense** if its closure has empty interior, that is, if every cylinder $[\sigma]$ contains a cylinder $[\tau]$ disjoint from the class. A class is **meager** if it is contained in a countable union of nowhere dense classes, and **co-meager** if its complement is meager.
:::

Equivalently, a class is co-meager if and only if it contains a countable intersection of dense open classes: the complement of a nowhere dense class contains a dense open class, namely the union of the cylinders disjoint from it; conversely, the complement of a dense open class is nowhere dense, since every cylinder contains a cylinder included in the dense open class. By :ref{#lem-dense-open}, this gives the link with genericity.

:::proposition{#prop-generic-comeager}
A property holds for all sufficiently generic sets if and only if the class of sets with the property is co-meager.
:::

:::proof{of=prop-generic-comeager}
If every $\mathcal D$-generic set has the property, the class contains $\bigcap_n [D_n]^{\prec}$, a countable intersection of dense open classes, by :ref{#lem-dense-open}. Conversely, if the class contains $\bigcap_n \mathcal U_n$ with $\mathcal U_n$ dense open, the sets $D_n = \{ \sigma : [\sigma] \subseteq \mathcal U_n \}$ are dense, and every set meeting all of them lies in $\bigcap_n \mathcal U_n$.
:::

Countable unions of meager classes are meager, and countable intersections of co-meager classes are co-meager. Every countable class is meager, since a singleton is nowhere dense: any cylinder $[\sigma]$ contains a cylinder $[\sigma i]$ avoiding a given point.

## The Baire category theorem

:::theorem[Baire category theorem]{#thm-baire-category}
Every co-meager class $\mathcal B \subseteq \cs$ meets every cylinder. More precisely, for every string $\sigma$, there is an injective map $X \mapsto G_X$ from $\cs$ into $\mathcal B \cap [\sigma]$. In particular, no cylinder is meager, and every co-meager class has the cardinality of the continuum.
:::

:::proof{of=thm-baire-category}
Let $\bigcap_n \mathcal U_n \subseteq \mathcal B$ with $\mathcal U_n$ dense open, and let $D_n = \{ \tau : [\tau] \subseteq \mathcal U_n \}$, dense by :ref{#lem-dense-open}. Fix an enumeration of $\bstr$. Define strings $\sigma_\rho$ for $\rho \in \bstr$: let $\sigma_\varepsilon = \sigma$, and for $i \in \{0, 1\}$, let $\sigma_{\rho i}$ be the first extension of $\sigma_\rho\, i$ in $D_{|\rho|}$. The strings $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ are incompatible, since they extend $\sigma_\rho 0$ and $\sigma_\rho 1$. For $X \in \cs$, let $G_X$ be the sequence extending every $\sigma_{X \uh n}$; it meets every $D_n$, through $\sigma_{X \uh (n+1)}$, so $G_X \in \bigcap_n \mathcal U_n$, and it extends $\sigma$. Different $X$ give different $G_X$, by the incompatibility of the splitting strings.
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

## Exercises

::::exercise{difficulty=1}
Show that the class of computable sets is meager, and that the class of sets computing $\emptyset'$ is meager.

:::solution
The class of computable sets is countable, hence meager. By :ref{#thm-cone-avoidance}, the sets $D_e = \{ \tau : \exists x\ \Phi^\tau_e(x)\converge \neq \emptyset'(x) \} \cup \{ \tau : \exists x\ \forall \rho \succeq \tau\ \Phi^\rho_e(x)\diverge \}$ are dense, and a set meeting all of them does not compute $\emptyset'$. By :ref{#prop-generic-comeager}, the class of sets not computing $\emptyset'$ is co-meager.
:::
::::

::::exercise{#exr-density-meager difficulty=2}
For a set $X$ and $n \geq 1$, let $\delta_n(X) = |X \cap \{0, \dots, n-1\}| / n$. Show that for every sufficiently generic set $G$, $\limsup_n \delta_n(G) = 1$ and $\liminf_n \delta_n(G) = 0$. Deduce that the class of sets with asymptotic density $\tfrac12$ is meager.

:::solution
For $k \geq 1$, let $D_k$ be the set of strings $\sigma$ having a prefix $\tau$ of length $n \geq k$ with $|\{ i < n : \tau(i) = 1 \}| \geq (1 - 1/k)\, n$. It is dense: any string $\sigma$ extended by $k |\sigma| + k$ ones has a prefix, itself, of the required kind. Similarly the sets $E_k$, with zeros in place of ones, are dense. A set meeting every $D_k$ has $\delta_n(G) \geq 1 - 1/k$ for some $n \geq k$, for every $k$, so $\limsup_n \delta_n(G) = 1$; symmetrically $\liminf_n \delta_n(G) = 0$. Such a set has no asymptotic density, so the class of sets of density $\tfrac12$ is contained in a meager class.
:::
::::

## Notes and references

Baire introduced meager classes in his thesis (1899), to study the limits of continuous functions. Cohen invented forcing in 1963 to prove the independence of the continuum hypothesis, and Feferman (1965) adapted it to arithmetic. The systematic use of genericity in computability theory is due to Jockusch (1980). Oxtoby's book compares measure and category.

- R. Baire, *Sur les fonctions de variables réelles*, Annali di Matematica Pura ed Applicata (3) 3 (1899), 1–123.
- P. J. Cohen, *The independence of the continuum hypothesis*, Proceedings of the National Academy of Sciences 50 (1963), 1143–1148.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- J. C. Oxtoby, *Measure and Category*, 2nd edition, Graduate Texts in Mathematics 2, Springer, 1980.
