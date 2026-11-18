---
title: Variants of cototality
summary: Graph-cototal and weakly cototal degrees; total degrees are graph-cototal; every Σ⁰₂ degree is graph-cototal, through a Σ⁰₂ approximation; every cototal degree contains the complement of a maximal independent set of ω^{<ω}; non-identity words in a finitely generated simple group; the separations between the variants.
duration: 25
prerequisites: [enumeration-jump/skip-and-cototality]
---

The first examples of cototal sets were complements of graphs of total functions: if $G_f$ is the graph of a total function $f$, its complement is enumeration reducible to $G_f$, so $\overline{G_f}$ is cototal. Degrees containing such a set were studied by Solon before cototality had a name, and Case asked as early as 1969 whether a set can have total degree while its complement does not. This lesson separates three variants of cototality, shows that the whole local structure consists of graph-cototal degrees, and proves that complements of maximal independent sets in one fixed computable graph realize every cototal degree.

## Three notions

:::definition{#def-graph-cototal}
An enumeration degree is **graph-cototal** if it contains the complement $\overline{G_f}$ of the graph of a total function $f$. It is **weakly cototal** if it contains a set $A$ such that $\overline A$ has total degree.
:::

A graph-cototal degree is cototal, since $\overline{G_f} \leq_e G_f$ (:ref{#ex-enumeration-reductions}), and a cototal degree is weakly cototal: if $A \leq_e \overline A$, then $\overline A$ is total. Every total degree is graph-cototal: a total degree contains the graph of the characteristic function $\chi_X$ of a set $X$, and $\langle n, m \rangle \in \overline{G_{\chi_X}}$ if and only if $m \notin \{ 0, 1 \}$ or $\langle n, 1 - m \rangle \in G_{\chi_X}$, so the complement of this graph is enumeration equivalent to the graph.

:::theorem[Andrews et al.]{#thm-sigma2-graph-cototal}
Every enumeration degree below $\mathbf 0'_e$ is graph-cototal.
:::

**Intuition.** A $\Sigma^0_2$ set $A$ has an approximation in which each element of $A$ is eventually always present, from a first stage $s_a$ on (:ref{#prop-sigma2-approximation}). The table of pairs $\langle a, s \rangle$ with $s \neq s_a$ is c.e.: one sees that $s$ is not the right stage either because $a$ was already present at $s - 1$ or because $a$ leaves again later. A function $g$ that marks, in column $a$, the stage $s_a$ if $a \in A$, and $0$ otherwise, has a graph whose complement is built from this c.e. table and from $A$ itself.

:::proof{of=thm-sigma2-graph-cototal}
Let $A$ be $\Sigma^0_2$, by :ref{#prop-below-zero-jump}, with an approximation $(A_s)$ as in :ref{#prop-sigma2-approximation}, and $A_0 = \emptyset$. For $a \in A$, let $s_a \geq 1$ be the least stage such that $a \in A_s$ for all $s \geq s_a$. Let
$$
U = \{ \langle a, s \rangle : s \geq 1 \text{ and } a \in A_{s-1} \} \cup \{ \langle a, s \rangle : \exists t \geq s\ a \notin A_t \},
$$
a c.e. set. We claim that $\langle a, s \rangle \in U$ if and only if $a \notin A$ or $s \neq s_a$. If $a \notin A$, then $a \notin A_t$ for infinitely many $t$, so $\langle a, s \rangle \in U$. Let $a \in A$. If $s < s_a$, then $a \notin A_{s_a - 1}$ with $s_a - 1 \geq s$, by minimality of $s_a$. If $s > s_a$, then $a \in A_{s-1}$. If $s = s_a$, then $a \notin A_{s-1}$, by minimality, and $a \in A_t$ for all $t \geq s$; so $\langle a, s_a \rangle \notin U$.

Define $g(a) = s_a + 1$ if $a \in A$ and $g(a) = 0$ otherwise, and
$$
H = \{ \langle a, 0 \rangle : a \in A \} \cup \{ \langle a, m \rangle : m \geq 1,\ \langle a, m - 1 \rangle \in U \}.
$$
In column $a$, $H$ contains $0$ exactly when $a \in A$, and $m \geq 1$ exactly when $a \notin A$ or $m - 1 \neq s_a$. So column $a$ misses exactly one number, $g(a)$: $H = \overline{G_g}$. Moreover $H \leq_e A$, as $U$ is c.e., and $A \leq_e H$, by $a \in A \iff \langle a, 0 \rangle \in H$. So $\deg_e(A)$ contains $\overline{G_g}$.
:::

The proof does not extend further: Andrews et al. show that some $\Pi^0_2$ sets do not have cototal degree, although every $\Pi^0_2$ degree is weakly cototal (:ref{#ex-pi2-weakly-cototal}).

:::quiz[Σ⁰₂ degrees are graph-cototal]
Why is the set $U$ c.e., although $s_a$ is not computable?

- [x] Each of the two conditions defining $U$ is witnessed by finitely many stages of the approximation, and together they say exactly that $s$ is not the stage from which $a$ stays in $A$.
- [ ] Because $A$ is c.e.

  $A$ is only $\Sigma^0_2$; the trick is that the wrong stages, not the right one, are recognized.
- [ ] Because $s_a$ is computable in $A$.

  It need not be; $U$ is c.e. outright.
:::

## Maximal independent sets

A set $S$ of vertices of a graph is independent if no two of its elements are adjacent, and maximal if every other vertex is adjacent to one of its elements. The complement of a maximal independent set of a computable graph is cototal (:ref{#prop-independent-cototal}). Consider the graph on $\nat^{<\nat}$ in which each nonempty string is adjacent to its immediate predecessor; it is computable, after coding strings by numbers.

:::theorem[Andrews et al.]{#thm-independent-universal}
Every cototal degree contains the complement of a maximal independent set of the graph $\nat^{<\nat}$.
:::

:::proof{of=thm-independent-universal}
Let $A$ be cototal with $A = \Gamma(\overline A)$. If $A$ is c.e., the set of strings of odd length is a computable maximal independent set, whose complement is computable, of degree $\mathbf 0_e = \deg_e(A)$. Otherwise $A$ and $\overline A$ are nonempty (if $\overline A$ were empty, $A = \nat$ would be c.e.); fix $a_0 \in A$ and $b_0 \in \overline A$. Replacing each axiom $\langle a, \emptyset \rangle$ of $\Gamma$ by $\langle a, \{ b_0 \} \rangle$, which is still valid on $\overline A$, we may assume that no axiom has an empty set of hypotheses. Then $\Gamma$ is infinite, since $A$ is not c.e.; fix a computable listing $\gamma(0), \gamma(1), \ldots$ of its axioms without repetitions.

To each nonempty string $\sigma$ we assign a finite set $D_\sigma$, computably, by induction on the length: for a string $\langle n \rangle$ of length $1$, $D_{\langle n \rangle} = \{ n \}$; for $\sigma = \tau n$, if $\gamma(n) = \langle a, D \rangle$ with $a \in D_\tau$, then $D_\sigma = D$, and otherwise $D_\sigma = \{ a_0 \}$. Let
$$
G = \{ \sigma : D_\sigma \cap A \neq \emptyset \} \cup \{ \langle \rangle \}.
$$
Then $G \leq_e A$, and $A \leq_e G$, since $n \in A$ if and only if $\langle n \rangle \in G$. We show that $\overline G$ is a maximal independent set.

*Independence.* Let $\sigma = \tau n$; we show that $\sigma \in G$ or $\tau \in G$. Suppose $\tau \notin G$: then $\tau$ is nonempty and $D_\tau \subseteq \overline A$. If $\gamma(n)$ is not an axiom for an element of $D_\tau$, then $D_\sigma = \{ a_0 \}$ meets $A$, and $\sigma \in G$. If $\gamma(n) = \langle a, D \rangle$ with $a \in D_\tau \subseteq \overline A$, then $a \notin A = \Gamma(\overline A)$, so the axiom is not valid: $D \not\subseteq \overline A$, that is, $D_\sigma = D$ meets $A$, and $\sigma \in G$.

*Maximality.* Let $\tau \in G$; we find a neighbor outside $G$. If $\tau$ is the root, take $\langle b_0 \rangle$, which is not in $G$ since $b_0 \notin A$. Otherwise let $a \in D_\tau \cap A$. Since $a \in \Gamma(\overline A)$, some axiom $\gamma(n) = \langle a, D \rangle$ has $D \subseteq \overline A$; then $D_{\tau n} = D$ and $\tau n \notin G$.
:::

The proof uses two fixed elements: $a_0 \in A$, assigned to the strings whose last entry is not a relevant axiom, so that they belong to $G$, and $b_0 \in \overline A$, used to normalize the axioms. McCarthy proved the same universality for complements of maximal antichains in $\nat^{<\nat}$, and for languages of minimal subshifts (lesson on the skip).

## Separations

Andrews et al. proved that the three notions are distinct: there is a cototal degree that is not graph-cototal, by an infinite injury argument relative to $\mathbf 0'$, a weakly cototal degree that is not cototal, and a degree that is not weakly cototal (a $\Delta^0_3$ set suffices). Graph-cototality has a combinatorial characterization: a degree is graph-cototal if and only if it contains a cototal set $A$ with a reduction $A \leq_e \overline A$ in which every element of $A$ has a unique valid axiom.

::::exercise{#ex-simple-group-cototal difficulty=2 objective="Recognize cototality in combinatorial group theory, following Jeandel."}
Let $G$ be a nontrivial finitely generated simple group, with a finite set $F$ of generators closed under inverses, and let $W$ be the set of words over $F$ that represent the identity. Show that the set of words that do not represent the identity is enumeration reducible to $W$, so that it is cototal.

:::solution
Let $w$ be a word. If $w$ does not represent the identity, the normal subgroup generated by $w$ is nontrivial, hence equal to $G$ by simplicity, so every generator $x \in F$ is a product of conjugates of $w$ and $w^{-1}$: there are words $c_1, \ldots, c_k$ and signs $\varepsilon_i$ such that the word $x^{-1} c_1 w^{\varepsilon_1} c_1^{-1} \cdots c_k w^{\varepsilon_k} c_k^{-1}$ belongs to $W$. If $w$ represents the identity, every product of conjugates of $w^{\pm 1}$ represents the identity, so such words would show that $x$ is the identity for every generator, and $G$ would be trivial. So $w \notin W$ if and only if, for each of the finitely many $x \in F$, some word of this form is in $W$: a positive condition on $W$, which gives $\overline W \leq_e W$.
:::
::::

## Notes and references

The variants of cototality, :ref{#thm-sigma2-graph-cototal}, :ref{#thm-independent-universal} and the separations are due to Andrews, Ganchev, Kuyper, Lempp, Miller, A. Soskova and M. Soskova (2019), who also trace the history (Case, Gutteridge, Sanchis, Sorbi, Solon, Pankratov). The example of simple groups is due to Jeandel, and independently Thomas and Williams.

- U. Andrews, H. A. Ganchev, R. Kuyper, S. Lempp, J. S. Miller, A. A. Soskova and M. I. Soskova, *On cototality and the skip operator in the enumeration degrees*, Transactions of the American Mathematical Society 372 (2019), 1631–1670, Section 2.
- E. McCarthy, *Cototal enumeration degrees and their applications to effective mathematics*, Proceedings of the American Mathematical Society 146 (2018), 3541–3552.
- E. Jeandel, *Enumeration in closure spaces with applications to algebra*, arXiv:1505.07578, 2015.

:::::exercises
::::exercise{#ex-pi2-weakly-cototal difficulty=1 objective="Show that Π⁰₂ sets have weakly cototal degree by joining with the halting set."}
Let $A$ be a $\Pi^0_2$ set and $K$ the halting set. Show that $A \equiv_e A \oplus K$ and that the complement of $A \oplus K$ has total degree; deduce that $\deg_e(A)$ is weakly cototal.

:::solution
$K$ is c.e., so $A \oplus K \equiv_e A$. The complement of $A \oplus K$ is $\overline A \oplus \overline K$. Since $\overline A$ is $\Sigma^0_2$, $\overline A \leq_e \overline K$ by :ref{#prop-below-zero-jump}, so $\overline A \oplus \overline K \equiv_e \overline K$, which has the total degree $\mathbf 0'_e$. So $\deg_e(A)$ contains $A \oplus K$, whose complement has total degree.
:::
::::

::::exercise{#ex-independent-total difficulty=1 objective="Realize a total degree by a maximal independent set in a simple graph."}
In the computable graph on $\nat$ whose edges are the pairs $\{ 2n, 2n + 1 \}$, let $S = \{ 2n : n \in A \} \cup \{ 2n + 1 : n \notin A \}$. Show that $S$ is a maximal independent set and that its complement has the total degree of $A \oplus \overline A$.

:::solution
Each edge $\{ 2n, 2n + 1 \}$ has exactly one endpoint in $S$, so $S$ is independent and every vertex outside $S$ is adjacent to one in $S$. The complement is $\{ 2n : n \notin A \} \cup \{ 2n + 1 : n \in A \}$, which is a computable permutation of $\overline A \oplus A$, enumeration equivalent to $A \oplus \overline A$.
:::
::::

::::exercise{#ex-cototal-weakly difficulty=1 objective="Order the variants of cototality."}
Show directly that every cototal set $A$ has a complement of total degree, so that cototal degrees are weakly cototal.

:::solution
If $A \leq_e \overline A$, the set $\overline A$ is total: its complement $A$ is enumeration reducible to it. So $\deg_e(\overline A)$ is total, and $\deg_e(A)$ is weakly cototal.
:::
::::

:::::
