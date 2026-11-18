---
title: Definability and automorphisms
summary: Robust minimal pairs are first-order definable in the partial order of the enumeration degrees; the jump (Kalimullin; Ganchev, Soskova) and the total degrees (Cai, Ganchev, Lempp, Miller, Soskova) are definable through them; consequences for automorphisms, which are determined by their action on the Turing degrees; the theory of the enumeration degrees and the open questions.
duration: 25
prerequisites: [kalimullin-pairs]
---

The Turing jump is first-order definable in the partial order of the Turing degrees, but the only known definition comes out of the analysis of the automorphisms of the Turing degrees by Slaman and Woodin, and of the method of Shore and Slaman: it is long and gives little insight. In the enumeration degrees, both the jump and the image of the Turing degrees have short, natural definitions, through the robust minimal pairs of the previous lesson. This lesson states these definitions, proves the parts that follow from what has been established, and derives their consequences for the automorphisms and the theory of $\mathcal D_e$.

## Robust minimal pairs as formulas

The language is that of partial orders, $\leq$. The join $\mathbf a \vee \mathbf b$ is definable, as the least upper bound, and so is the statement "the meet of $\mathbf a$ and $\mathbf b$ exists and equals $\mathbf x$": $\mathbf x \leq \mathbf a$, $\mathbf x \leq \mathbf b$, and every common lower bound is below $\mathbf x$. So the condition of :ref{#thm-kalimullin-pairs} is a first-order formula:
$$
\mathrm{RMP}(\mathbf a, \mathbf b, \mathbf u) \equiv \forall \mathbf x \geq \mathbf u\ \forall \mathbf z\ \big( (\mathbf z \leq \mathbf a \vee \mathbf u \vee \mathbf x \text{ and } \mathbf z \leq \mathbf b \vee \mathbf u \vee \mathbf x) \to \mathbf z \leq \mathbf x \big),
$$
where the joins are expanded by their definition, and $\mathbf a \vee \mathbf u \vee \mathbf x = \mathbf a \vee \mathbf x$ since $\mathbf u \leq \mathbf x$. By Kalimullin's theorem, $\mathrm{RMP}(\mathbf a, \mathbf b, \mathbf u)$ holds if and only if sets in $\mathbf a$ and $\mathbf b$ form a K-pair relative to a set in $\mathbf u$. Write $\mathrm{RMP}(\mathbf a, \mathbf b)$ for $\mathrm{RMP}(\mathbf a, \mathbf b, \mathbf 0_e)$; the least degree is definable, as the least element. A robust minimal pair $\{ \mathbf a, \mathbf b \}$ is **nontrivial** if neither degree is $\mathbf 0_e$.

## The jump

:::theorem[Kalimullin]{#thm-jump-definable}
The jump of an enumeration degree $\mathbf u$ is the greatest degree of the form $\mathbf a \vee \mathbf b \vee \mathbf c$, where the pairs $\{ \mathbf a, \mathbf b \}$, $\{ \mathbf b, \mathbf c \}$ and $\{ \mathbf a, \mathbf c \}$ are robust minimal pairs relative to $\mathbf u$. Hence the enumeration jump is first-order definable in $\mathcal D_e$.
:::

:::theorem[Ganchev, Soskova]{#thm-jump-definable-gs}
The jump of $\mathbf u$ is the greatest degree of the form $\mathbf a \vee \mathbf b$, where $\{ \mathbf a, \mathbf b \}$ is a nontrivial robust minimal pair with $\mathbf a \leq \mathbf u$.
:::

We admit both theorems. The second uses only unrelativized robust minimal pairs. Both definitions have low quantifier complexity, in contrast with the definition of the Turing jump in $\mathcal D_T$.

## Totality

A robust minimal pair $\{ \mathbf a, \mathbf b \}$ is **maximal** if, whenever $\{ \mathbf c, \mathbf d \}$ is a robust minimal pair with $\mathbf a \leq \mathbf c$ and $\mathbf b \leq \mathbf d$, then $\mathbf a = \mathbf c$ and $\mathbf b = \mathbf d$. This is a first-order condition.

:::theorem[Cai, Ganchev, Lempp, Miller, Soskova]{#thm-totality-definable}
A nonzero enumeration degree is total if and only if it is the join of a maximal robust minimal pair. Hence the total degrees are first-order definable in $\mathcal D_e$.
:::

The proof rests on a lemma: for every K-pair $A$, $B$, there is a semi-computable set $C$ with $A \leq_e C$ and $B \leq_e \overline C$. Ganchev and Soskova proved it for K-pairs bounded by $\mathbf 0'_e$, and Cai, Ganchev, Lempp, Miller and Soskova in general. We admit the lemma, and derive one half of the theorem from it.

:::proposition{#prop-maximal-pair-total}
Assume the lemma. If $\{ \mathbf a, \mathbf b \}$ is a maximal robust minimal pair, then $\mathbf a \vee \mathbf b$ is total.
:::

:::proof{of=prop-maximal-pair-total}
Let $A \in \mathbf a$ and $B \in \mathbf b$; they form a K-pair by Kalimullin's theorem. By the lemma, there is a semi-computable set $C$ with $A \leq_e C$ and $B \leq_e \overline C$. By :ref{#ex-k-pairs}, $C$ and $\overline C$ form a K-pair, so $\{ \deg_e(C), \deg_e(\overline C) \}$ is a robust minimal pair above $\{ \mathbf a, \mathbf b \}$ componentwise. By maximality, $\mathbf a = \deg_e(C)$ and $\mathbf b = \deg_e(\overline C)$, and $\mathbf a \vee \mathbf b = \deg_e(C \oplus \overline C)$ is total.
:::

The converse uses Jockusch's semi-computable sets and a further argument showing that the pair of a suitable semi-computable set and its complement is maximal. Once the total degrees are definable, so is much more: the relation "$\iota^{-1}(\mathbf a)$ is c.e. in $\iota^{-1}(\mathbf b)$" on total degrees (Cai, Ganchev, Lempp, Miller and Soskova), and the relation "PA above" (next lesson).

:::quiz[definability of totality]
In the proof of :ref{#prop-maximal-pair-total}, where is maximality used?

- [x] To conclude that the given pair equals the pair of degrees of $C$ and $\overline C$, which lies above it componentwise and is a robust minimal pair.
- [ ] To show that $A$ and $B$ form a K-pair.

  That holds for every robust minimal pair, by Kalimullin's theorem.
- [ ] To show that $C$ is semi-computable.

  The lemma provides a semi-computable $C$; maximality identifies the degrees.

---

Why does the definition of robust minimal pairs use the join with every $\mathbf x$, rather than only the meet of $\mathbf a$ and $\mathbf b$?

- [x] Minimal pairs are common in many degree structures and do not characterize anything; the robust version is the one equivalent, by Kalimullin's theorem, to the combinatorial K-pair condition.
- [ ] Because the meet of two degrees does not always exist.

  That is true but beside the point; the robust condition asserts that certain meets exist.
- [ ] To make the formula first-order.

  The plain minimal pair condition is also first-order; robustness is what gives it content.
:::

## Automorphisms and the theory

The total degrees are the image of the Turing degrees, and by :ref{#cor-selman-degrees}, a degree is determined by the total degrees above it.

:::proposition{#prop-automorphisms-restrict}
Every automorphism $\pi$ of $\mathcal D_e$ maps total degrees to total degrees, so it induces an automorphism $\pi^* = \iota^{-1} \circ \pi \circ \iota$ of the Turing degrees, and $\pi$ is determined by $\pi^*$: if $\pi^*$ is the identity, so is $\pi$.
:::

:::proof{of=prop-automorphisms-restrict}
An automorphism preserves every first-order definable class, in particular the total degrees (:ref{#thm-totality-definable}), so $\pi$ restricts to an automorphism of the total degrees, and $\pi^*$ is an automorphism of $\mathcal D_T$. Suppose $\pi^*$ is the identity, so $\pi$ fixes every total degree. For a degree $\mathbf a$, the total degrees above $\pi(\mathbf a)$ are the images of the total degrees above $\mathbf a$, that is, the same total degrees. By :ref{#cor-selman-degrees}, $\pi(\mathbf a) = \mathbf a$.
:::

Slaman and Woodin proved that $\mathcal D_T$ has at most countably many automorphisms, and that a single degree below $\mathbf 0^{(5)}$ is an automorphism base. By the proposition, the same holds for $\mathcal D_e$: it has at most countably many automorphisms, and a single total degree below $\mathbf 0_e^{(5)}$ is an automorphism base. Slaman and Soskova improved the last statement: finitely many $\Delta^0_2$ total degrees form an automorphism base for $\mathcal D_e$.

The theory of $\mathcal D_e$ is as complicated as possible: Slaman and Woodin proved that it is computably isomorphic to the theory of second-order arithmetic. Its existential theory is decidable, since every finite partial order embeds; its three-quantifier theory is undecidable (Lempp, Slaman and Soskova, through the Nies transfer lemma); the decidability of its two-quantifier theory is open. The central open question is whether $\mathcal D_e$ is **rigid**, that is, has no automorphism other than the identity. By the work of Slaman and Woodin and of Soskova, rigidity is equivalent to the biinterpretability of $\mathcal D_e$ with second-order arithmetic, and to the statement that the definable relations on $\mathcal D_e$ are exactly those induced by degree-invariant definable relations of second-order arithmetic. Other open questions listed in Soskova's survey: whether every automorphism of $\mathcal D_T$ extends to $\mathcal D_e$, whether the skip and the cototal degrees are definable, and whether there are strong minimal pairs.

::::exercise{#ex-rmp-formula difficulty=1 objective="Write the definability results as explicit first-order formulas."}
Write a first-order formula $\mathrm{Tot}(\mathbf x)$ in the language of partial orders that defines the total degrees, using :ref{#thm-totality-definable} and the formula $\mathrm{RMP}$. Do not forget the least degree.

:::solution
Let $\mathrm{Zero}(\mathbf z) \equiv \forall \mathbf y\, (\mathbf z \leq \mathbf y)$, and let $\mathrm{Join}(\mathbf a, \mathbf b, \mathbf x) \equiv \mathbf a \leq \mathbf x \wedge \mathbf b \leq \mathbf x \wedge \forall \mathbf y\, ((\mathbf a \leq \mathbf y \wedge \mathbf b \leq \mathbf y) \to \mathbf x \leq \mathbf y)$. Let $\mathrm{Max}(\mathbf a, \mathbf b) \equiv \mathrm{RMP}(\mathbf a, \mathbf b) \wedge \forall \mathbf c\, \forall \mathbf d\, ((\mathrm{RMP}(\mathbf c, \mathbf d) \wedge \mathbf a \leq \mathbf c \wedge \mathbf b \leq \mathbf d) \to (\mathbf c \leq \mathbf a \wedge \mathbf d \leq \mathbf b))$. Then
$$
\mathrm{Tot}(\mathbf x) \equiv \mathrm{Zero}(\mathbf x) \vee \exists \mathbf a\, \exists \mathbf b\, (\mathrm{Max}(\mathbf a, \mathbf b) \wedge \mathrm{Join}(\mathbf a, \mathbf b, \mathbf x)),
$$
where $\mathrm{RMP}(\mathbf a, \mathbf b)$ is the formula of the lesson with $\mathbf u$ replaced by the least degree, expressed through $\mathrm{Zero}$. By :ref{#thm-totality-definable}, it defines the total degrees, $\mathbf 0_e$ being total.
:::
::::

## Notes and references

:ref{#thm-jump-definable} is Kalimullin (2003); :ref{#thm-jump-definable-gs} and the local case of the lemma are Ganchev and Soskova (2015); :ref{#thm-totality-definable} is Cai, Ganchev, Lempp, Miller and Soskova (2016). The consequences for automorphisms and the open questions are from Soskova's survey, Sections 1, 2.4 and 4.

- I. Sh. Kalimullin, *Definability of the jump operator in the enumeration degrees*, Journal of Mathematical Logic 3 (2003), 257–267.
- H. A. Ganchev and M. I. Soskova, *Definability via Kalimullin pairs in the structure of the enumeration degrees*, Transactions of the American Mathematical Society 367 (2015), 4873–4893.
- M. Cai, H. A. Ganchev, S. Lempp, J. S. Miller and M. I. Soskova, *Defining totality in the enumeration degrees*, Journal of the American Mathematical Society 29 (2016), 1051–1067.
- T. A. Slaman and W. H. Woodin, *Definability in the enumeration degrees*, Archive for Mathematical Logic 36 (1997), 255–267.
- T. A. Slaman and M. I. Soskova, *The enumeration degrees: local and global structural interactions*, in *Foundations of Mathematics*, Contemporary Mathematics 690, American Mathematical Society, 2017, 31–67.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020.

:::::exercises
::::exercise{#ex-low-definable difficulty=1 objective="Combine the definability of the jump with that of the least degree."}
Using :ref{#thm-jump-definable}, show that the degree $\mathbf 0'_e$ and the class of degrees $\mathbf a$ with $\mathbf a' = \mathbf 0'_e$ are first-order definable in $\mathcal D_e$.

:::solution
The least degree is definable, and so is the jump, as a definable function: $\mathbf y = \mathbf u'$ if and only if $\mathbf y$ is the greatest degree of the form described in :ref{#thm-jump-definable}, a first-order condition on $\mathbf u$ and $\mathbf y$. So $\mathbf 0'_e$ is defined as the jump of the least degree, and the class of degrees whose jump is $\mathbf 0'_e$ by the formula $\exists \mathbf y\, (\mathbf y = \mathbf a' \wedge \mathbf y = \mathbf 0'_e)$, with both equalities written with the definitions.
:::
::::
:::::
