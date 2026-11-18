---
title: The skip and the cototal degrees
summary: The skip of A is the complement of K_A; A ≤ₑ B if and only if the skip of A is 1-reducible to that of B; the skip is never below a degree and is often incomparable with it; cototal sets, enumeration reducible to their complement, are those on which skip and jump agree; complements of maximal independent sets and languages of minimal subshifts are cototal.
duration: 25
prerequisites: [enumeration-jump]
---

The enumeration jump of $A$ joins two sets, $K_A$, which is equivalent to $A$, and its complement $\overline{K_A}$, which carries the new information. Andrews, Ganchev, Kuyper, Lempp, Miller, A. Soskova and M. Soskova proposed to study this second half on its own: the **skip** of $A$. It turns out to be a more faithful analogue of the Turing jump in some respects, and less in others: it determines enumeration reducibility exactly, but it may lie to the side of the degree it comes from. The degrees on which it behaves like the jump, the cototal degrees, appear in unexpected places: maximal independent sets in graphs, and minimal subshifts in symbolic dynamics.

## The skip

:::definition[Andrews et al.]{#def-skip}
The **skip** of a set $A$ is $A^\diamond = \overline{K_A}$.
:::

:::proposition{#prop-skip-basic}
For all sets $A$ and $B$:
1. $A \leq_e B$ if and only if $A^\diamond \leq_1 B^\diamond$; so the skip is well defined and injective on enumeration degrees;
2. $A' \equiv_e A \oplus A^\diamond$;
3. $A^\diamond \not\leq_e A$;
4. $\emptyset^\diamond$ has degree $\mathbf 0'_e$.
:::

:::proof{of=prop-skip-basic}
1. If $A \leq_e B$, the proof of item 2 of :ref{#thm-e-jump} gives a computable injective $h$ with $x \in K_A \iff h(x) \in K_B$, which also reduces $A^\diamond$ to $B^\diamond$. Conversely, a 1-reduction $h$ of $A^\diamond$ to $B^\diamond$ satisfies $x \in K_A \iff h(x) \in K_B$, so $K_A \leq_1 K_B$, and $A \leq_e K_A \leq_e K_B \leq_e B$ by :ref{#lem-ka}.
2. $A' = K_A \oplus A^\diamond$ and $K_A \equiv_e A$.
3. If $A^\diamond \leq_e A$, then $A' \equiv_e A \oplus A^\diamond \leq_e A$, contradicting item 1 of :ref{#thm-e-jump}.
4. $K_\emptyset$ is a 1-complete c.e. set, so $\emptyset^\diamond \equiv_1 \overline K$.
:::

The first item says that the skip loses no information: unlike the jump, it is injective on degrees. The third says that the skip of a degree is never below it. But it need not be above it. When $A^\diamond \geq_e A$, the skip is the jump, by item 2; otherwise the two are incomparable, and the jump is their join. Andrews et al. showed that the skip can behave very differently from a jump: there are degrees $\mathbf a$ and $\mathbf b$ with $\mathbf a^\diamond = \mathbf b$ and $\mathbf b^\diamond = \mathbf a$, a skip 2-cycle, and such degrees must be above every hyperarithmetic degree.

## Cototal sets

:::definition{#def-cototal}
A set $A$ is **cototal** if $A \leq_e \overline A$. An enumeration degree is **cototal** if it contains a cototal set.
:::

Compare with totality: a set is total if its complement is enumeration reducible to it, and cototal if it is enumeration reducible to its complement. A total degree is cototal: $B \oplus \overline B$ is reducible to its complement $\overline B \oplus B$ by exchanging even and odd numbers.

:::proposition{#prop-cototal-skip}
If $A$ is cototal, then $A \leq_e A^\diamond$, and $\deg_e(A)^\diamond = \deg_e(A)'$.
:::

:::proof{of=prop-cototal-skip}
Let $\Gamma_i$ be the identity operator. Then $n \in \overline A$ if and only if $\langle i, n \rangle \in \overline{K_A} = A^\diamond$, so $\overline A \leq_1 A^\diamond$. If $A$ is cototal, $A \leq_e \overline A \leq_e A^\diamond$, and $A' \equiv_e A \oplus A^\diamond \equiv_e A^\diamond$ by :ref{#prop-skip-basic}.
:::

Andrews et al. proved the converse: a degree on which skip and jump agree is cototal. They also showed that every $\Sigma^0_2$ enumeration degree is cototal, while sufficiently generic degrees are not. So the cototal degrees form a proper class strictly between the total degrees and all degrees, containing the whole local structure.

:::quiz[the skip and cototality]
Why is the skip injective on degrees, while the jump is not?

- [x] The skip $\overline{K_A}$ determines $K_A$, which is equivalent to $A$; the jump $K_A \oplus \overline{K_A}$ adds information that can hide the difference between two degrees with the same jump.
- [ ] Because the skip is total.

  The skip is in general not total; injectivity comes from the 1-reduction between the sets $K_A$.
- [ ] Because the skip is above the degree.

  The skip need not be above the degree; that is the point of the cototal degrees.

---

For a cototal set $A$, why is $A$ below its skip?

- [x] The complement of $A$ is 1-reducible to $\overline{K_A}$, through the identity operator, and $A$ is enumeration reducible to its complement by cototality.
- [ ] Because every set is below its skip.

  The skip may be incomparable with the set; this is what cototality prevents.
- [ ] Because $A$ is total.

  Cototal sets need not be total; the argument uses only $A \leq_e \overline A$.
:::

## Cototal sets in combinatorics

Two natural sources of cototal sets show why the notion arises. A set $M$ of vertices of a graph is **independent** if no two of its elements are adjacent, and **maximal** independent if moreover every vertex outside $M$ is adjacent to some element of $M$.

:::proposition{#prop-independent-cototal}
Let $M$ be a maximal independent set in a computable graph on $\nat$. Then $\overline M$ is cototal.
:::

:::proof{of=prop-independent-cototal}
A vertex $v$ is outside $M$ if and only if it is adjacent to some $u \in M$: if $v \notin M$, maximality gives such a $u$; if $v \in M$, no neighbor of $v$ is in $M$, by independence. So $\overline M = \{ v : \exists u\, (u E v \wedge u \in M) \}$, which is enumeration reducible to $M$, the complement of $\overline M$, since the edge relation is computable.
:::

Andrews et al. proved the converse: every cototal degree contains the complement of a maximal independent set of a computable graph.

A **subshift** is a closed set $S \subseteq 2^\nat$ closed under the shift $x_0 x_1 x_2 \ldots \mapsto x_1 x_2 \ldots$; it is **minimal** if it is non-empty and has no non-empty proper closed subset closed under the shift. Its **language** $L_S$ is the set of finite words occurring in elements of $S$. We use a classical fact of topological dynamics (Birkhoff): in a minimal subshift, every word $w \in L_S$ occurs in every element of $S$ with bounded gaps, that is, there is $\ell$ such that every factor of length $\ell$ of every element of $S$ contains $w$.

:::proposition[Jeandel]{#prop-subshift-cototal}
The language of a minimal subshift is cototal.
:::

:::proof{of=prop-subshift-cototal}
We show that $w \in L_S$ if and only if there is $\ell$ such that every word of length $\ell$ not containing $w$ is outside $L_S$; this is enumeration reducible to $\overline{L_S}$, since for each $\ell$ there are finitely many such words. If $w \in L_S$, take $\ell$ given by Birkhoff's fact: a word of length $\ell$ without $w$ occurs in no element of $S$. Conversely, if $\ell$ is as stated, take any $x \in S$ (the subshift is non-empty): its prefix of length $\ell$ belongs to $L_S$, so it contains $w$, and $w \in L_S$.
:::

Jeandel observed that the Turing degrees computing an element of a minimal subshift $S$ are exactly those in which $L_S$ is c.e.: the enumeration degree of $L_S$ captures the computational content of the subshift, through :ref{#thm-selman}. McCarthy proved that every cototal degree is the degree of the language of a minimal subshift. The cototal degrees have several other characterizations, listed in Soskova's survey (Section 3.3): the degrees of complements of maximal antichains in $\nat^{<\nat}$ (McCarthy), the degrees of sets with good approximations (Miller and Soskova, who used it to prove that the cototal degrees are dense), and the degrees of points of computable $G_\delta$ topological spaces (Kihara, Ng and Pauly). Whether the cototal degrees, or the skip, are first-order definable in $\mathcal D_e$ is open.

::::exercise{#ex-cototal-total-not-converse difficulty=1 objective="Separate totality from cototality on a simple example."}
Show that the complement $\overline K$ of the halting set is total, and that $K$ is cototal but not total.

:::solution
$\overline K \equiv_e K \oplus \overline K$, and the complement of $\overline K$, which is $K$, is c.e., hence enumeration reducible to $\overline K$: so $\overline K$ is total. $K$ is c.e., so $K \leq_e \overline K$, and $K$ is cototal. If $K$ were total, $\overline K \leq_e K$ would make $\overline K$ c.e. by :ref{#prop-e-degrees-basic}, which it is not. (The degree of $K$ is $\mathbf 0_e$, which is total; the set $K$ itself is not.)
:::
::::

## Notes and references

The skip and the cototal degrees were introduced by Andrews, Ganchev, Kuyper, Lempp, Miller, A. Soskova and M. Soskova (2019), who proved :ref{#prop-skip-basic}, the converse of :ref{#prop-cototal-skip}, the cototality of the $\Sigma^0_2$ degrees and the characterization by maximal independent sets. :ref{#prop-subshift-cototal} is due to Jeandel (2015); McCarthy (2018) proved the converse. Birkhoff's fact is the characterization of minimal subshifts as those whose elements are uniformly recurrent.

- U. Andrews, H. A. Ganchev, R. Kuyper, S. Lempp, J. S. Miller, A. A. Soskova and M. I. Soskova, *On cototality and the skip operator in the enumeration degrees*, Transactions of the American Mathematical Society 372 (2019), 1631–1670.
- E. McCarthy, *Cototal enumeration degrees and their applications to effective mathematics*, Proceedings of the American Mathematical Society 146 (2018), 3541–3552.
- J. S. Miller and M. I. Soskova, *Density of the cototal enumeration degrees*, Annals of Pure and Applied Logic 169 (2018), 450–462.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Section 3.3.

:::::exercises
::::exercise{#ex-antichain-cototal difficulty=2 objective="Adapt the argument for independent sets to maximal antichains of strings."}
An antichain in $\nat^{<\nat}$ is a set of strings no two of which are comparable for the prefix order; it is maximal if every string is comparable with one of its elements. Show that the complement of a maximal antichain $M$ is cototal.

:::solution
A string $\sigma$ is outside $M$ if and only if it is comparable with, and different from, some element of $M$: if $\sigma \notin M$, maximality gives $\tau \in M$ comparable with $\sigma$, and $\tau \neq \sigma$; if $\sigma \in M$, no other element of $M$ is comparable with it. Comparability of strings is computable, so $\overline M = \{ \sigma : \exists \tau \in M\, (\tau \neq \sigma \text{ and } \tau, \sigma \text{ comparable}) \}$ is enumeration reducible to $M$, the complement of $\overline M$.
:::
::::

::::exercise{#ex-skip-low difficulty=1 objective="Compute the skip of the degree of a c.e. set and of a total degree."}
Compute $\mathbf 0_e^\diamond$, and show that for a total degree $\mathbf a = \iota(\mathbf x)$, $\mathbf a^\diamond = \mathbf a' = \iota(\mathbf x')$.

:::solution
$\mathbf 0_e^\diamond = \mathbf 0'_e$ by :ref{#prop-skip-basic}, item 4. A total degree is cototal, so $\mathbf a^\diamond = \mathbf a'$ by :ref{#prop-cototal-skip}, and $\mathbf a' = \iota(\mathbf x')$ by :ref{#thm-e-jump}, item 4.
:::
::::
:::::
