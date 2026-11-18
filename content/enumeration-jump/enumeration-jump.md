---
title: The enumeration jump and the local structure
summary: Cooper's enumeration jump A′ = K_A ⊕ complement of K_A is strictly above A, monotone, total, and extends the Turing jump; its range is the set of total degrees above 0′ₑ; low quasi-minimal degrees; the degrees below 0′ₑ are those of the Σ⁰₂ sets, with Σ⁰₂ approximations; what is known about the local structure.
duration: 35
prerequisites: [enumeration-reducibility/quasi-minimal-degrees, turing-degrees/turing-jump, arithmetic-hierarchy/post-theorem]
---

The Turing jump of $A$ collects all the sets c.e. in $A$ into one complete set, and is not computable in $A$ because a diagonal argument uses its complement. The natural analogue for enumeration reducibility collects all the sets enumeration reducible to $A$, but this set is no stronger than $A$ itself: what $A$ cannot do is enumerate its complement. Cooper's enumeration jump adds the complement. This lesson proves that it behaves as a jump should, that it agrees with the Turing jump on the total degrees, and that its values are exactly the total degrees above $\mathbf 0'_e$.

## The jump

:::definition[Cooper]{#def-e-jump}
For a set $A$, let $K_A = \{ \langle e, n \rangle : n \in \Gamma_e(A) \}$. The **enumeration jump** of $A$ is $A' = K_A \oplus \overline{K_A}$.
:::

:::lemma{#lem-ka}
1. $K_A \equiv_e A$, uniformly in $A$.
2. Every set $B \leq_e A$ is 1-reducible to $K_A$, by a reduction computed from an index of $\Gamma$ with $B = \Gamma(A)$.
:::

:::proof{of=lem-ka}
The axioms $\langle \langle e, n \rangle, u \rangle$ for $\langle n, u \rangle \in W_e$ form a c.e. set and enumerate $K_A$ from $A$. If $B = \Gamma_e(A)$, then $n \in B$ if and only if $\langle e, n \rangle \in K_A$, and $n \mapsto \langle e, n \rangle$ is computable and injective. Taking for $\Gamma_e$ the identity gives $A \leq_1 K_A$, hence $A \leq_e K_A$.
:::

So $K_A$ adds nothing to $A$; the jump adds the complement of $K_A$, and this complement is out of reach of $A$.

:::theorem{#thm-e-jump}
For all sets $A$ and $B$:
1. $A <_e A'$;
2. if $A \leq_e B$, then $A' \leq_1 B'$; in particular the jump is well defined on degrees and monotone;
3. $A'$ is total;
4. $(B \oplus \overline B)' \equiv_e B'_T \oplus \overline{B'_T}$, where $B'_T$ is the Turing jump of $B$: on total degrees, $\iota(\mathbf b)' = \iota(\mathbf b')$.
:::

:::proof{of=thm-e-jump}
1. $A \leq_e K_A \leq_e A'$. Suppose $\overline{K_A} \leq_e A$, and let $D = \{ e : \langle e, e \rangle \notin K_A \} = \{ e : e \notin \Gamma_e(A) \}$. Then $D \leq_1 \overline{K_A}$, so $D \leq_e A$, and $D = \Gamma_m(A)$ for some $m$. Then $m \in D$ if and only if $m \notin \Gamma_m(A) = D$, a contradiction. So $\overline{K_A} \not\leq_e A$ and $A' \not\leq_e A$.
2. Let $A = \Gamma_c(B)$. By composition, there is a computable injective function $g$ with $\Gamma_{g(e)} = \Gamma_e \circ \Gamma_c$ for all $e$ (padding makes $g$ injective). Then $\langle e, n \rangle \in K_A$ if and only if $n \in \Gamma_{g(e)}(B)$, if and only if $\langle g(e), n \rangle \in K_B$. The same map reduces $\overline{K_A}$ to $\overline{K_B}$, and the two together give $A' \leq_1 B'$.
3. The complement of $A' = K_A \oplus \overline{K_A}$ is $\overline{K_A} \oplus K_A$, which is 1-reducible to $A'$ by exchanging even and odd numbers.
4. By :ref{#prop-ce-in-e}, the sets enumeration reducible to $B \oplus \overline B$ are the sets c.e. in $B$. So $K_{B \oplus \overline B}$ is c.e. in $B$, and every set c.e. in $B$ is 1-reducible to it, by :ref{#lem-ka}. The Turing jump $B'_T$ has the same two properties (:ref{#thm-jump}). Hence $K_{B \oplus \overline B} \leq_1 B'_T \leq_1 K_{B \oplus \overline B}$, and the jumps $K_{B \oplus \overline B} \oplus \overline{K_{B \oplus \overline B}}$ and $B'_T \oplus \overline{B'_T}$ are enumeration equivalent.
:::

The jump of $\emptyset$ is $K_\emptyset \oplus \overline{K_\emptyset}$, where $K_\emptyset$ is a 1-complete c.e. set; its degree is $\mathbf 0'_e = \deg_e(\overline K) = \iota(\mathbf 0')$, as in the lesson on enumeration operators. By item 2, every jump is above $\mathbf 0'_e$.

:::quiz[the enumeration jump]
Why is $K_A$ alone not a good candidate for the jump?

- [x] $K_A$ is enumeration equivalent to $A$: enumerating all the sets reducible to $A$ at once is no harder than enumerating $A$.
- [ ] Because $K_A$ is not total.

  Totality is a separate question; the point is that $K_A$ has the same degree as $A$.
- [ ] Because $K_A$ is not 1-complete for the sets reducible to $A$.

  It is, by the lemma; this completeness is why its complement makes a jump.

---

In item 2, why does the same map $h(\langle e, n \rangle) = \langle g(e), n \rangle$ reduce the complements?

- [x] A 1-reduction is an equivalence $x \in K_A \iff h(x) \in K_B$, which is the same statement as $x \notin K_A \iff h(x) \notin K_B$.
- [ ] Because the complements are c.e.

  They are not c.e. in general; the reduction is a property of the map.
- [ ] Because $g$ is injective.

  Injectivity makes $h$ a 1-reduction rather than an m-reduction; the transfer to complements holds for m-reductions as well.
:::

## The range of the jump

:::theorem{#thm-e-jump-range}
The jumps of enumeration degrees are exactly the total degrees above $\mathbf 0'_e$.
:::

:::proof{of=thm-e-jump-range}
Every jump is total and above $\mathbf 0'_e$, by :ref{#thm-e-jump}. Conversely, a total degree above $\mathbf 0'_e$ is $\iota(\mathbf z)$ for a Turing degree $\mathbf z \geq \mathbf 0'$, by :ref{#thm-myhill-embedding}. By Friedberg's jump inversion theorem (:ref{#cor-jump-inversion}), $\mathbf z = \mathbf g'$ for some Turing degree $\mathbf g$, and $\iota(\mathbf z) = \iota(\mathbf g)'$ by item 4 of :ref{#thm-e-jump}.
:::

McEvoy (1985) proved more: every total degree above $\mathbf 0'_e$ is the jump of a quasi-minimal degree. A degree $\mathbf a$ is **low** if $\mathbf a' = \mathbf 0'_e$.

:::proposition{#prop-low-quasi-minimal}
There is a low quasi-minimal enumeration degree below $\mathbf 0'_e$.
:::

:::proof{of=prop-low-quasi-minimal}
By :ref{#prop-1-generic}, there is a 1-generic set $G \leq_T \emptyset'$; it is low as a Turing degree, $G' \equiv_T \emptyset'$, by :ref{#thm-generic-low}. Its enumeration degree is quasi-minimal (:ref{#thm-generic-quasi-minimal}) and below $\iota(\deg_T G) \leq \iota(\mathbf 0') = \mathbf 0'_e$. Its jump is below $\iota(\deg_T G)' = \iota(\deg_T G') = \mathbf 0'_e$, by items 2 and 4 of :ref{#thm-e-jump}, and above $\mathbf 0'_e$; so $\deg_e(G)$ is low.
:::

::::exercise{#ex-e-jump-join difficulty=1 objective="Compare the jump of a join with the join of the jumps."}
Show that $A' \oplus B' \leq_e (A \oplus B)'$ for all sets $A$ and $B$. Then let $G \leq_T \emptyset'$ be 1-generic: show that $\deg_e(G)' = \deg_e(\overline G)' = (\deg_e(G) \vee \deg_e(\overline G))' = \mathbf 0'_e$, although $\deg_e(G) \vee \deg_e(\overline G)$ is strictly above $\deg_e(G)$ and $\deg_e(\overline G)$.

:::solution
$A \leq_e A \oplus B$ and $B \leq_e A \oplus B$, so $A', B' \leq_e (A \oplus B)'$ by monotonicity, and the join is below. For the example, $\overline G$ is 1-generic and computable in $\emptyset'$ (:ref{#ex-complement-generic}), so $G$ and $\overline G$ have low degrees, as in :ref{#prop-low-quasi-minimal}. The join $\deg_e(G \oplus \overline G) = \iota(\deg_T G)$ has jump $\iota(\deg_T G') = \iota(\mathbf 0') = \mathbf 0'_e$, since $G$ is low. The join is strictly above each of the two degrees by :ref{#ex-generic-total-cover}. So three distinct degrees have the same jump.
:::
::::

In the Turing degrees, the degrees below $\mathbf 0'$ are those of the $\Delta^0_2$ sets, which have computable approximations by the limit lemma. In the enumeration degrees, the corresponding interval, the **local structure** $\mathcal D_e(\leq \mathbf 0'_e)$, is larger: it consists of the degrees of the $\Sigma^0_2$ sets. This lesson proves this, gives the approximations that play the role of the limit lemma, and surveys what is known about the local structure, which is the setting of most priority constructions in the enumeration degrees.

## The local structure: Σ⁰₂ sets

:::proposition{#prop-below-zero-jump}
A set $A$ satisfies $A \leq_e \overline K$ if and only if $A$ is $\Sigma^0_2$. So the degrees below $\mathbf 0'_e$ are the degrees of the $\Sigma^0_2$ sets, and every set in such a degree is $\Sigma^0_2$.
:::

:::proof{of=prop-below-zero-jump}
Since $K$ is c.e., $\overline K \equiv_e K \oplus \overline K$. By :ref{#prop-ce-in-e}, $A \leq_e K \oplus \overline K$ if and only if $A$ is c.e. in $K$, which by Post's theorem (:ref{#thm-post}) means that $A$ is $\Sigma^0_2$.
:::

The total degrees below $\mathbf 0'_e$ are the images of the $\Delta^0_2$ Turing degrees, and the $\Delta^0_2$ sets are those whose complement is also $\Sigma^0_2$. A $\Sigma^0_2$ set has a computable approximation of a weaker kind than a $\Delta^0_2$ set.

:::proposition{#prop-sigma2-approximation}
A set $A$ is $\Sigma^0_2$ if and only if there is a computable sequence of finite sets $(A_s)$ such that, for every $n$: $n \in A$ if and only if $n \in A_s$ for all sufficiently large $s$.
:::

:::proof{of=prop-sigma2-approximation}
If such a sequence exists, $n \in A \iff \exists t\ \forall s \geq t\ n \in A_s$, a $\Sigma^0_2$ definition. Conversely, let $n \in A \iff \exists x\ \forall y\ R(n, x, y)$ with $R$ computable. For $s \geq 1$, let $x_s(n)$ be the least $x \leq s$ such that $R(n, x, y)$ holds for all $y \leq s$, if there is one, and let $n \in A_s$ if and only if $n \leq s$, $x_s(n)$ and $x_{s-1}(n)$ are defined, and $x_s(n) = x_{s-1}(n)$. If $n \in A$, let $x^*$ be its least witness: each $x < x^*$ fails at some $y$, so from some stage on $x_s(n) = x^*$, and $n \in A_s$ for all large $s$. If $n \notin A$ and $n \in A_s$ for all $s \geq t$, then $x_s(n)$ is defined and constant, equal to some $x$, for $s \geq t$, so $R(n, x, y)$ holds for all $y$, and $n \in A$: a contradiction.
:::

The approximation is "eventually always in" for elements and "infinitely often out" for non-elements. A $\Delta^0_2$ approximation, from the limit lemma, also requires the non-elements to be eventually always out.

:::quiz[Σ⁰₂ approximations]
In the proof of :ref{#prop-sigma2-approximation}, why does the definition of $A_s$ compare $x_s(n)$ with $x_{s-1}(n)$, rather than only ask that $x_s(n)$ be defined?

- [x] For $n \notin A$, $x_s(n)$ may be defined at every stage while changing infinitely often; requiring no change at the current stage makes $n$ leave $A_s$ at each change.
- [ ] To make the approximation computable.

  Both versions are computable; the comparison is what makes them correct.
- [ ] Because $x_s(n)$ is decreasing.

  It is not monotone: it increases when the current witness fails and may never settle.
:::

## Nontotal degrees below 0′ₑ

The local structure contains both total and nontotal degrees. By :ref{#prop-low-quasi-minimal}, the degree of a 1-generic set computable in $\emptyset'$ is a low quasi-minimal degree below $\mathbf 0'_e$, and so is the degree of its complement; the two are incomparable (:ref{#ex-generic-total-cover}) and join to a total degree. Every Turing degree below $\mathbf 0'$ is represented by a total degree. So the local structure contains a copy of the $\Delta^0_2$ Turing degrees, and degrees that are not in this copy.

## What is known about the local structure

The following results are admitted; they are described in Soskova's survey, Section 4.2.
- **Density** (Cooper, 1984). The local structure is dense: between two degrees $\mathbf a < \mathbf b \leq \mathbf 0'_e$ there is a third. The global structure is not dense (Cooper, 1990), and even the $\Pi^0_2$ enumeration degrees are not dense (Calhoun and Slaman, 1996).
- **Embeddings.** Every countable partial order embeds in every nonempty interval of the local structure (Bianchini, 2000), and every finite lattice embeds preserving least and greatest elements (Lempp and Sorbi, 2002). The extension of embeddings problem is decidable (Lempp, Slaman and Sorbi, 2005).
- **Theory.** The three-quantifier theory of the local structure is undecidable (Kent, 2006); whether its two-quantifier theory is decidable is open. The full theory is computably isomorphic to true first-order arithmetic (Ganchev and Soskova, 2012).
- **Definability.** The local structure defines its Kalimullin pairs, the low degrees, all levels of the high/low hierarchy, the $\Delta^0_2$ total degrees, and the degrees bounding no nonzero $\Delta^0_2$ degree (Ganchev and Soskova, 2012–2018).

Density marks the difference with the Turing degrees below $\mathbf 0'$, where there are minimal degrees. The proof of density is a priority construction using the approximations of :ref{#prop-sigma2-approximation}; it is beyond this course.

::::exercise{#ex-delta2-e-degree difficulty=1 objective="Recognize total degrees below 0′ₑ from the arithmetic complexity of their sets."}
Let $A$ be a set. Show that $\deg_e(A \oplus \overline A) \leq \mathbf 0'_e$ if and only if $A$ is $\Delta^0_2$, and that a $\Sigma^0_2$ set $A$ that is not $\Delta^0_2$ has a degree that is below $\mathbf 0'_e$ while $\deg_e(A \oplus \overline A)$ is not.

:::solution
By :ref{#prop-below-zero-jump}, $A \oplus \overline A \leq_e \overline K$ if and only if $A \oplus \overline A$ is $\Sigma^0_2$, that is, $A$ and $\overline A$ are $\Sigma^0_2$, that is, $A$ is $\Delta^0_2$. If $A$ is $\Sigma^0_2$ but not $\Delta^0_2$, then $\deg_e(A) \leq \mathbf 0'_e$, while $\deg_e(A \oplus \overline A) \not\leq \mathbf 0'_e$ by the first part.
:::
::::

## Notes and references

:ref{#def-e-jump} and :ref{#thm-e-jump} are due to Cooper (1984), and are recalled in Soskova's survey (Definition 3.1); McEvoy (1985) studied the jumps of quasi-minimal degrees. Soskova's survey, Section 3.3, compares the jump with the skip, the subject of the last lesson of this course.

:ref{#prop-below-zero-jump} and :ref{#prop-sigma2-approximation} are standard (Cooper 1984). The results of the last section are from the papers cited in Soskova's survey, Sections 2.1 and 4.2.

- S. B. Cooper, *Partial degrees and the density problem. Part 2: The enumeration degrees of the Σ₂ sets are dense*, Journal of Symbolic Logic 49 (1984), 503–513.
- K. McEvoy, *Jumps of quasi-minimal enumeration degrees*, Journal of Symbolic Logic 50 (1985), 839–848.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Section 3.1.
- W. C. Calhoun and T. A. Slaman, *The Π⁰₂ enumeration degrees are not dense*, Journal of Symbolic Logic 61 (1996), 1364–1379.
- S. Lempp, T. A. Slaman and A. Sorbi, *On extensions of embeddings into the enumeration degrees of the Σ⁰₂-sets*, Journal of Mathematical Logic 5 (2005), 247–298.
- H. A. Ganchev and M. I. Soskova, *Interpreting true arithmetic in the local structure of the enumeration degrees*, Journal of Symbolic Logic 77 (2012), 1184–1194.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Section 4.2.

:::::exercises
::::exercise{#ex-jump-zero difficulty=1 objective="Compute the jump of the least degree and of the degree of a c.e. set's complement."}
Show that $\mathbf 0_e' = \mathbf 0'_e$ and that $(\mathbf 0'_e)' = \iota(\mathbf 0'')$.

:::solution
$\mathbf 0_e = \iota(\mathbf 0)$, so by item 4 of :ref{#thm-e-jump}, $\mathbf 0_e' = \iota(\mathbf 0') = \mathbf 0'_e$. Applying item 4 again, $(\mathbf 0'_e)' = \iota(\mathbf 0')' = \iota(\mathbf 0'')$.
:::
::::

::::exercise{#ex-jump-not-injective difficulty=2 objective="See that the enumeration jump identifies a quasi-minimal degree with a total one."}
Show that the jump is not injective on enumeration degrees: there are degrees $\mathbf a < \mathbf b$ with $\mathbf a' = \mathbf b'$, one quasi-minimal and one total.

:::solution
Let $G \leq_T \emptyset'$ be 1-generic, $\mathbf a = \deg_e(G)$ and $\mathbf b = \iota(\deg_T G)$. By :ref{#ex-generic-total-cover}, $\mathbf a < \mathbf b$, and $\mathbf a$ is quasi-minimal while $\mathbf b$ is total. By the proof of :ref{#prop-low-quasi-minimal}, $\mathbf a' = \mathbf 0'_e$, and $\mathbf b' = \iota(\deg_T G') = \iota(\mathbf 0') = \mathbf 0'_e$.
:::
::::
::::exercise{#ex-sigma2-not-delta2-example difficulty=1 objective="Find a Σ⁰₂ set that is not Δ⁰₂ and compute its enumeration degree."}
Show that $\mathrm{Fin} = \{ e : W_e \text{ is finite} \}$ is $\Sigma^0_2$, and that its enumeration degree is below $\mathbf 0'_e$, while the degree of its complement is not.

:::solution
$e \in \mathrm{Fin}$ if and only if $\exists n\ \forall s\ \forall x \geq n\ x \notin W_{e,s}$, a $\Sigma^0_2$ definition, so $\deg_e(\mathrm{Fin}) \leq \mathbf 0'_e$ by :ref{#prop-below-zero-jump}. The complement $\mathrm{Inf}$ is $\Pi^0_2$-complete, hence not $\Sigma^0_2$ (otherwise it would be $\Delta^0_2$, and computable in $\emptyset'$, while it is Turing equivalent to $\emptyset''$); so its degree is not below $\mathbf 0'_e$.
:::
::::

::::exercise{#ex-sigma2-approx-ce difficulty=1 objective="Specialize Σ⁰₂ approximations to c.e. and co-c.e. sets."}
For a c.e. set $A$ and a co-c.e. set $B$, give approximations as in :ref{#prop-sigma2-approximation} that change their mind at most once on each element.

:::solution
For $A = \bigcup_s A_s$ c.e., the enumeration $(A_s)$ itself works: an element enters once and stays. For $B$ co-c.e., let $\overline B = \bigcup_s V_s$ with $(V_s)$ a computable enumeration, and $B_s = \{ n \leq s : n \notin V_s \}$: an element of $B$ is in $B_s$ for all $s \geq n$, and an element of $\overline B$ leaves once it is enumerated in $V_s$, and never returns.
:::
::::
:::::
