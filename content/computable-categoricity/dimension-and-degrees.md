---
title: Computable dimension and degrees of categoricity
summary: Two measures of the failure of computable categoricity; the computable dimension, the number of computable copies up to computable isomorphism, is infinite for ω and can be any finite number (Goncharov); the degree of categoricity, the least degree computing isomorphisms between computable copies, is 0′ for ω; known degrees of categoricity, non-examples, and the open question whether every degree of categoricity is strong.
duration: 30
prerequisites: [nurtazin-theorem]
---

A structure that is not computably categorical can fail in two ways, which this lesson measures. The first measure counts: how many computable copies are there, up to computable isomorphism? The second measures strength: how much computational power is needed to build isomorphisms between computable copies? For the order $\omega$, both answers are found by the same family of copies, in which the successor relation codes a c.e. set: there are infinitely many classes, and the jump is necessary and sufficient. For general structures, the first measure can take any finite value, as Goncharov showed, and the second has been determined for many degrees, with an open question at its center.

## Computable dimension

:::definition{#def-computable-dimension}
The **computable dimension** of a computable structure $\mathcal A$ is the number of equivalence classes of computable copies of $\mathcal A$ under computable isomorphism, a number in $\{1, 2, \ldots\} \cup \{\omega\}$.
:::

A structure is computably categorical if and only if its computable dimension is $1$. To compute the dimension of $\omega$, we build a copy in which a given c.e. set is coded into adjacencies, as in :ref{#prop-successor-not-ice}.

:::lemma{#lem-omega-x}
For every c.e. set $X$, there is a computable copy $\omega_X$ of $(\nat; \leq)$ whose successor relation is Turing equivalent to $X$, uniformly in a c.e. index of $X$.
:::

:::figure[The copy $\omega_X$ of :ref{#lem-omega-x}. Each $n$ has a pair $a_n < b_n$, placed at the end of the order at stage $n$; when $n$ enters $X$, an element is inserted between $a_n$ and $b_n$. The successor relation tells whether $a_n$ and $b_n$ are adjacent, hence whether $n \in X$.]
<svg class="fig" viewBox="0 0 680 150" width="680" role="img" aria-label="The copy of omega built from a c.e. set X, drawn as a line of elements from left to right. For n from 0 to 4 there is a pair a_n, b_n. For n = 1 and n = 3, which belong to X, an extra element is inserted between a_n and b_n; for the other values of n, a_n and b_n stay adjacent. The line continues to the right"><line x1="40" y1="70" x2="100" y2="70" class="muted-stroke" stroke-width="1.2"/><path d="M40,60 Q70.0,40 100,60" fill="none" class="accent-stroke" stroke-width="1.6"/><circle cx="40" cy="70" r="6" class="node"/><text x="40" y="98" text-anchor="middle" class="math">a₀</text><circle cx="100" cy="70" r="6" class="node"/><text x="100" y="98" text-anchor="middle" class="math">b₀</text><line x1="100" y1="70" x2="140" y2="70" class="muted-stroke" stroke-width="1.2"/><line x1="140" y1="70" x2="230" y2="70" class="muted-stroke" stroke-width="1.2"/><circle cx="140" cy="70" r="6" class="node"/><text x="140" y="98" text-anchor="middle" class="math">a₁</text><circle cx="230" cy="70" r="6" class="node"/><text x="230" y="98" text-anchor="middle" class="math">b₁</text><circle cx="185.0" cy="70" r="6" class="head-cell"/><line x1="230" y1="70" x2="270" y2="70" class="muted-stroke" stroke-width="1.2"/><line x1="270" y1="70" x2="330" y2="70" class="muted-stroke" stroke-width="1.2"/><path d="M270,60 Q300.0,40 330,60" fill="none" class="accent-stroke" stroke-width="1.6"/><circle cx="270" cy="70" r="6" class="node"/><text x="270" y="98" text-anchor="middle" class="math">a₂</text><circle cx="330" cy="70" r="6" class="node"/><text x="330" y="98" text-anchor="middle" class="math">b₂</text><line x1="330" y1="70" x2="370" y2="70" class="muted-stroke" stroke-width="1.2"/><line x1="370" y1="70" x2="460" y2="70" class="muted-stroke" stroke-width="1.2"/><circle cx="370" cy="70" r="6" class="node"/><text x="370" y="98" text-anchor="middle" class="math">a₃</text><circle cx="460" cy="70" r="6" class="node"/><text x="460" y="98" text-anchor="middle" class="math">b₃</text><circle cx="415.0" cy="70" r="6" class="head-cell"/><line x1="460" y1="70" x2="500" y2="70" class="muted-stroke" stroke-width="1.2"/><line x1="500" y1="70" x2="560" y2="70" class="muted-stroke" stroke-width="1.2"/><path d="M500,60 Q530.0,40 560,60" fill="none" class="accent-stroke" stroke-width="1.6"/><circle cx="500" cy="70" r="6" class="node"/><text x="500" y="98" text-anchor="middle" class="math">a₄</text><circle cx="560" cy="70" r="6" class="node"/><text x="560" y="98" text-anchor="middle" class="math">b₄</text><line x1="560" y1="70" x2="600" y2="70" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 4"/><text x="8" y="140" class="label">arcs: pairs that stay adjacent (n not in X)</text><text x="672" y="140" text-anchor="end" class="label">highlighted: element inserted when n enters X</text></svg>
:::

:::proof{of=lem-omega-x}
Let $(X_s)$ be a computable enumeration of $X$. Build an order on $\nat$ by stages, never changing the relative order of elements already placed. At stage $s$, place two new elements $a_s < b_s$ at the end of the order, above everything placed so far; then, for each $n \leq s$ such that $n \in X_s$ and no element has yet been placed between $a_n$ and $b_n$, place one new element between them. The order is computable, since the position of each element relative to the previous ones is decided when it is placed. Each element has finitely many predecessors: an element placed at stage $s$ is preceded by elements placed before stage $s$ and by at most one element inserted between each of the finitely many pairs placed before it; so the order is a copy of $\omega$.

Two elements $x < y$ are adjacent if and only if no element lies between them at the stage when both are placed and they are not a pair $a_n, b_n$ with $n \in X$: insertions only happen inside the pairs $a_n, b_n$, once. So the successor relation is computable in $X$. Conversely, $n \in X$ if and only if $a_n$ and $b_n$ are not adjacent, and $n \mapsto (a_n, b_n)$ is computable; so $X$ is computable in the successor relation.
:::

:::proposition{#prop-omega-dimension}
The order $\omega$ has computable dimension $\omega$.
:::

:::proof{of=prop-omega-dimension}
Two copies of $\omega$ have a unique isomorphism between them, which preserves the successor relation. If $f : \omega_X \to \omega_Y$ is a computable isomorphism, then two elements are adjacent in $\omega_X$ if and only if their images are adjacent in $\omega_Y$, so the successor relation of $\omega_X$ is computable in that of $\omega_Y$, and $X \leq_T Y$ by :ref{#lem-omega-x}. There are infinitely many c.e. sets that are pairwise Turing incomparable, by the extension of the Friedberg–Muchnik construction in :ref{#ex-fm-independent}. The corresponding copies $\omega_X$ are pairwise not computably isomorphic.
:::

For structures in which effectiveness conditions hold, this is the typical behavior: Goncharov proved that a $\forall\exists$-decidable structure that is not computably categorical has computable dimension $\omega$, by the construction of :ref{#thm-nurtazin} run against infinitely many copies at once (Ash–Knight, Theorem 12.4). Linear orders and Boolean algebras have computable dimension $1$ or $\omega$ (Dzgoev and Goncharov; Goncharov; Ash–Knight, Theorems 12.11 and 12.13). For the relative notion, where isomorphisms computable in the diagrams are counted, the dimension is always $1$ or infinite (McCoy; Ash–Knight, Theorem 10.15). Finite dimensions greater than $1$ nevertheless exist.

:::theorem[Goncharov]{#thm-finite-dimension}
For every $n \geq 1$, there is a computable structure of computable dimension $n$.
:::

We admit the theorem. Goncharov's proof builds a family of c.e. sets with exactly $n$ computable enumerations without repetitions, up to computable equivalence, and codes it into a graph with one component for each set, so that computable copies of the graph correspond to such enumerations (Ash–Knight, Section 12.6). Hirschfeldt, Khoussainov, Shore and Slinko showed that the same values are realized in many classes of algebraic structures, among them graphs, partial orders, lattices and nilpotent groups. As Ash and Knight remark, finite dimensions greater than $1$ are not explained by definability: no structural condition accounts for them, and they disappear on a cone.

## Degrees of categoricity

:::definition{#def-degree-categoricity}
Let $\mathcal A$ be a computable structure. A Turing degree $\mathbf d$ is the **degree of categoricity** of $\mathcal A$ if $\mathbf d$ computes an isomorphism between any two computable copies of $\mathcal A$, and every degree with this property is above $\mathbf d$. It is a **strong degree of categoricity** if moreover there are two computable copies $\mathcal B$ and $\mathcal C$ such that every isomorphism between them computes $\mathbf d$. A degree is a (strong) degree of categoricity if it is the (strong) degree of categoricity of some computable structure.
:::

A structure need not have a degree of categoricity: the degrees computing isomorphisms between all pairs of computable copies may have no least element. The strong version is the easiest to establish, by the following remark: if $\mathbf d$ computes isomorphisms between all pairs of computable copies, and some pair $\mathcal B$, $\mathcal C$ has only isomorphisms above $\mathbf d$, then any degree computing isomorphisms between all pairs computes one between $\mathcal B$ and $\mathcal C$, hence is above $\mathbf d$; so $\mathbf d$ is the strong degree of categoricity. A computably categorical structure has the strong degree of categoricity $\mathbf 0$.

:::proposition{#prop-omega-degree}
The order $\omega$ has strong degree of categoricity $\mathbf 0'$.
:::

:::proof{of=prop-omega-degree}
By :ref{#prop-omega-delta2}, $\mathbf 0'$ computes an isomorphism between any two computable copies. Let $K$ be the halting set, and compare the standard copy $(\nat; \leq)$ with $\omega_K$ of :ref{#lem-omega-x}. The only isomorphism $f : \omega_K \to (\nat; \leq)$ satisfies: $x$ and $y$ are adjacent in $\omega_K$ if and only if $f(y) = f(x) + 1$. So the successor relation of $\omega_K$ is computable in $f$, and $K \leq_T f$ by :ref{#lem-omega-x}. By the remark above, $\mathbf 0'$ is the strong degree of categoricity of $\omega$.
:::

:::quiz[the degree of categoricity of ω]
In the proof of :ref{#prop-omega-degree}, why does every isomorphism between $\omega_K$ and the standard copy compute $K$?

- [x] There is only one isomorphism, it preserves adjacency, and adjacency in the standard copy is computable; so the successor relation of $\omega_K$, which computes $K$, is computable from it.
- [ ] Because $\omega_K$ is not computable.

  $\omega_K$ is a computable copy; the complexity lies in its successor relation.
- [ ] Because $\mathbf 0'$ computes the isomorphism.

  That gives the upper bound; the lower bound is that every isomorphism computes $K$.

---

In :ref{#lem-omega-x}, why is the successor relation of $\omega_X$ computable in $X$?

- [x] Elements are inserted only between the designated pairs $a_n$, $b_n$, at most once each, so two elements adjacent when both are placed stay adjacent unless they form a pair $a_n, b_n$ with $n \in X$.
- [ ] Because $\omega_X$ is computable.

  The order is computable, but adjacency is in general not; the lemma shows it is computable in $X$.
- [ ] Because $X$ is c.e.

  That makes the construction computable; computing adjacency needs the answers of $X$ for the pairs.
:::


::::exercise{#ex-integers-degree difficulty=1 objective="Adapt the coding of the halting set into adjacencies to a structure with many automorphisms." lessons="computable-structures/back-and-forth"}
Show that the order $\zeta = (\mathbb Z; \leq)$ of the integers has strong degree of categoricity $\mathbf 0'$. Unlike $\omega$, it has infinitely many automorphisms.

:::solution
By :ref{#ex-integers-delta2}, $\mathbf 0'$ computes an isomorphism between any two computable copies. Let $\mathcal C$ be the computable copy of $\zeta$ obtained by placing a copy of the negative integers below $\omega_K$: on $\nat$, put the even numbers in decreasing order, below the odd numbers ordered as $\omega_K$, transported to the odd numbers. Its order type is $\omega^* + \omega = \zeta$. Let $f : \mathcal C \to (\mathbb Z; \leq)$ be any isomorphism. Every isomorphism preserves adjacency, so two odd numbers are adjacent in $\mathcal C$ if and only if their images differ by $1$; this is computable in $f$. Two odd numbers are adjacent in $\mathcal C$ if and only if the corresponding elements are adjacent in $\omega_K$, so the successor relation of $\omega_K$, hence $K$, is computable in $f$. So every isomorphism between $\mathcal C$ and the standard copy computes $\mathbf 0'$, and $\mathbf 0'$ is the strong degree of categoricity.
:::
::::

The study of which degrees are degrees of categoricity was started by Fokina, Kalimullin and Miller (2010). The main results are the following.
- **Positive results.** Every degree that is d.c.e. in and above $\mathbf 0^{(n)}$, for some $n$, is a strong degree of categoricity (Fokina, Kalimullin, Miller), and so is $\mathbf 0^{(\alpha)}$ for every computable ordinal $\alpha$ (Csima, Franklin, Shore). Csima and Ng proved that every $\Delta^0_2$ degree is a strong degree of categoricity.
- **Upper bound.** Every degree of categoricity is hyperarithmetic (Csima, Franklin, Shore).
- **Non-examples.** No non-computable hyperimmune-free degree, and no degree of a 2-generic set, is a degree of categoricity; there is a $\Sigma^0_2$ degree that is not one (Anderson, Csima).
- **On a cone.** Relative to all oracles above a fixed one, every structure has a strong degree of categoricity, of the form $\mathbf 0^{(\alpha)}$ (Csima, Harrison-Trainor), in agreement with the general principle that natural structures have jumps as their complexity.

Fokina, Kalimullin and Miller asked whether every degree of categoricity is a strong degree of categoricity. The question is open: in all known examples, the degree of categoricity is witnessed by a single pair of copies.

## Notes and references

Computable dimension was introduced by Goncharov; :ref{#thm-finite-dimension} is from Goncharov (1980), with the family of sets of Goncharov's lemma (Ash–Knight, Lemma 12.9 and Theorem 12.10). :ref{#lem-omega-x} and :ref{#prop-omega-dimension} are standard; Ash–Knight prove the infinite dimension of linear orders with infinitely many adjacencies in Theorem 12.11. :ref{#prop-omega-degree} is an example of Fokina, Kalimullin and Miller. The results on degrees of categoricity listed above are from the papers below; the status of the question on strong degrees was checked in 2026 against the recent literature, where it is still stated as open.

- S. S. Goncharov, *The problem of the number of non-autoequivalent constructivizations*, Algebra and Logic 19 (1980), 401–414.
- D. R. Hirschfeldt, B. Khoussainov, R. A. Shore and A. M. Slinko, *Degree spectra and computable dimensions in algebraic structures*, Annals of Pure and Applied Logic 115 (2002), 71–113.
- E. B. Fokina, I. Kalimullin and R. Miller, *Degrees of categoricity of computable structures*, Archive for Mathematical Logic 49 (2010), 51–67.
- B. F. Csima, J. N. Y. Franklin and R. A. Shore, *Degrees of categoricity and the hyperarithmetic hierarchy*, Notre Dame Journal of Formal Logic 54 (2013), 215–231.
- B. A. Anderson and B. F. Csima, *Degrees that are not degrees of categoricity*, Notre Dame Journal of Formal Logic 57 (2016), 389–398.
- B. F. Csima and M. Harrison-Trainor, *Degrees of categoricity on a cone via η-systems*, Journal of Symbolic Logic 82 (2017), 325–346.
- B. F. Csima and K. M. Ng, *Every $\Delta^0_2$ degree is a strong degree of categoricity*, 2022.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Sections 12.6–12.7.

:::::exercises
::::exercise{#ex-degree-zero difficulty=1 objective="Check the definition of degrees of categoricity on the extreme case."}
Show that a computable structure has degree of categoricity $\mathbf 0$ if and only if it is computably categorical, and that in this case $\mathbf 0$ is a strong degree of categoricity.

:::solution
If the structure is computably categorical, $\mathbf 0$ computes an isomorphism between any two computable copies, and every degree is above $\mathbf 0$; so $\mathbf 0$ is its degree of categoricity. For strength, take $\mathcal B = \mathcal C$ any computable copy: every isomorphism between them computes $\mathbf 0$, trivially. Conversely, if $\mathbf 0$ is the degree of categoricity, it computes an isomorphism between any two computable copies, which is computable: the structure is computably categorical.
:::
::::

::::exercise{#ex-omega-x-degrees difficulty=2 objective="Use the copies ω_X to realize every c.e. degree as the degree of an isomorphism." lessons="relative-categoricity"}
Let $X$ be a c.e. set. Show that the isomorphism between the standard copy of $\omega$ and $\omega_X$ has the Turing degree of $X$. Deduce that every c.e. degree is the degree of an isomorphism between two computable copies of $\omega$.

:::solution
Let $f : (\nat; \leq) \to \omega_X$ be the isomorphism, and $S_X$ the successor relation of $\omega_X$. From $S_X$ and the least element of $\omega_X$, compute $f$: $f(0)$ is the least element, and $f(n + 1)$ is the unique $y$ with $S_X(f(n), y)$, found by search. So $f \leq_T S_X \equiv_T X$. Conversely, $x$ and $y$ are adjacent in $\omega_X$ if and only if $f^{-1}(y) = f^{-1}(x) + 1$, and $f^{-1}$ is computable in $f$; so $X \equiv_T S_X \leq_T f$. Hence $f \equiv_T X$, and every c.e. degree is the degree of such an isomorphism.
:::
::::
:::::
