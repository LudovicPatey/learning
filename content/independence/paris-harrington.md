---
title: The Paris–Harrington principle
summary: Relatively large homogeneous sets and the Paris–Harrington principle; its truth, from the infinite Ramsey theorem and König's lemma; each instance of fixed arity is provable in ACA₀, hence in Peano arithmetic.
duration: 35
prerequisites: [indicators, ramsey-theorem/triples, big-five/aca0-reversals, induction-conservation/first-order-parts]
---

The independence results of the previous lessons concern the totality of functions defined for the purpose. Paris and Harrington (1977) found a statement of finite combinatorics, a slight strengthening of the finite Ramsey theorem, that is true and not provable in Peano arithmetic. The strengthening asks for a homogeneous set that is **relatively large**: it has more elements than its least element. This lesson states the principle, proves it from the infinite Ramsey theorem, shows that each instance of fixed arity is provable in $\mathrm{PA}$, and makes it a $\Pi_2$ sentence of arithmetic; the next three lessons prove that $\mathrm{PA}$ does not prove it.

## Relatively large homogeneous sets

For a set $X$ of natural numbers, $[X]^n$ is the set of its $n$-element subsets, identified with increasing $n$-tuples; $[a, b]$ is the interval $\{ a, \dots, b \}$, and $c = \{ 0, \dots, c - 1 \}$. A **coloring** is a function $f : [X]^n \to c$, and $H \subseteq X$ is **homogeneous** for $f$ if $f$ is constant on $[H]^n$.

:::definition{#def-relatively-large}
A finite set $H$ is **relatively large** if $|H| > \min H$. For numbers $a \leq b$ and $k, n, c$, the relation $[a, b] \to_* (k)^n_c$ means: every coloring $f : [[a, b]]^n \to c$ has a homogeneous set $H$ that is relatively large and has at least $k$ elements.

The **Paris–Harrington principle** $\mathrm{PH}$ is $\forall n\ \forall c\ \forall k\ \forall a\ \exists b\ [a, b] \to_* (k)^n_c$. For a fixed $n$, $\mathrm{PH}_n$ is $\forall c\ \forall k\ \forall a\ \exists b\ [a, b] \to_* (k)^n_c$.
:::

Without the condition "relatively large", this is the **finite Ramsey theorem**, which follows from the infinite one by compactness and is provable in $\mathrm I\Sigma_1$ (Hájek and Pudlák, Theorem II.1.10). The condition is a lower bound on the size of $H$ that depends on where $H$ lies: a homogeneous set far out must be large. Relative largeness is the first instance of the $\alpha$-large sets of lesson 8, for $\alpha = \omega$.

:::example{#ex-relatively-large}
1. $\{ 3, 5, 8, 13 \}$ is relatively large; $\{ 4, 5, 8, 13 \}$ is not. A set containing $0$ is relatively large as soon as it is nonempty.
2. *Colorings of points.* Let $a \geq 1$ and $f : [a, 2^c a - 1] \to c$, $f(x) = i$ for $2^i a \leq x < 2^{i+1} a$. A homogeneous set $H$ of color $i$ with minimum $m \geq 2^i a$ has at most $2^{i+1} a - m \leq m$ elements, so it is not relatively large. Hence $[a, 2^c a - 1] \not\to_* (1)^1_c$. For the plain pigeonhole principle, an interval of $c (k - 1) + 1$ points suffices for a homogeneous set of size $k$: relative largeness already forces an exponential interval for colorings of points.
3. The relation is monotone: if $[a, b] \to_* (k)^n_c$, then $[a', b'] \to_* (k')^n_{c'}$ for $a' \leq a$, $b \leq b'$, $k' \leq k$ and $c' \leq c$, by restricting a coloring of $[[a', b']]^n$ to $[[a, b]]^n$ and viewing $c'$ colors among $c$.
:::

The relation $[a, b] \to_* (k)^n_c$ quantifies over the colorings of $[[a, b]]^n$ and over the subsets of $[a, b]$. In $\mathrm I\Delta_0 + \mathrm{exp}$ these are coded by numbers below a bound $E$ computable from $a, b, n, c$ by a term in exponentiation, and the relation becomes a bounded formula in $a, b, k, n, c$ and $E$. Since the graph of exponentiation is bounded (:ref{#fact-exp}), the relation is $\Delta_1$ in $\mathrm I\Sigma_1$, and $\mathrm{PH}$ and $\mathrm{PH}_n$ are $\Pi_2$ sentences.

## Truth of the principle

:::theorem[Paris, Harrington]{#thm-ph-true}
$\mathrm{PH}$ is true. More precisely, for each standard $n$, $\mathsf{ACA}_0$ proves $\mathrm{PH}_n$, and therefore $\mathrm{PA} \vdash \mathrm{PH}_n$.
:::

The proof is a **compactness argument**: if the conclusion failed for every $b$, the counterexamples would assemble, by König's lemma, into a coloring of an infinite set; the infinite Ramsey theorem gives an infinite homogeneous set, and an initial part of it, long enough to be relatively large, contradicts one of the finite counterexamples.

:::proof{of=thm-ph-true}
We argue in $\mathsf{ACA}_0$, for a fixed standard $n$. Suppose that $c, k, a$ are such that $[a, b] \not\to_* (k)^n_c$ for every $b \geq a$. Call a coloring of $[[a, b]]^n$ **bad** if it has no relatively large homogeneous set with at least $k$ elements. The restriction of a bad coloring of $[[a, b']]^n$ to $[[a, b]]^n$, for $b \leq b'$, is bad, since a homogeneous set for the restriction is homogeneous for the original coloring. Let $T$ be the tree whose nodes at level $\ell$ are the bad colorings of $[[a, a + \ell]]^n$, ordered by extension. It exists by $\Delta^0_1$ comprehension, since badness is a bounded condition. Each level is finite and nonempty by hypothesis, so $T$ is an infinite, finitely branching tree. By König's lemma, which $\mathsf{ACA}_0$ proves (:ref{#thm-konig-aca}), $T$ has a path, that is a coloring $F$ of $[[a, \infty)]^n$ into $c$ colors all of whose restrictions to $[[a, b]]^n$ are bad.

$\mathsf{ACA}_0$ proves Ramsey's theorem for $n$-tuples and any number of colors (:ref{#thm-rt3-aca}; for an arbitrary number of colors, Simpson, Lemma III.7.4), in the form of :ref{#prop-rt-basic} for colorings of an infinite set. So $F$ has an infinite homogeneous set $Y$. Let $H$ consist of the first $\max(k, \min Y + 1)$ elements of $Y$ and $b = \max H$. Then $H$ is homogeneous for the restriction of $F$ to $[[a, b]]^n$, has at least $k$ elements, and $|H| \geq \min Y + 1 > \min H$. This contradicts the badness of the restriction.

$\mathrm{PH}_n$ is a sentence of first-order arithmetic, and $\mathsf{ACA}_0$ is a conservative extension of $\mathrm{PA}$ (:ref{#thm-aca0-pa}); so $\mathrm{PA} \vdash \mathrm{PH}_n$. The truth of $\mathrm{PH}$ follows, since $\nat$ with all its subsets is a model of $\mathsf{ACA}_0$ in which $n$ ranges over all natural numbers.
:::

$\mathsf{ACA}_0$ proves each $\mathsf{RT}^n$, not $\forall n\ \mathsf{RT}^n$ (:ref{#thm-rt3-aca}), so the proof says nothing about $\mathrm{PH}$ itself in $\mathrm{PA}$; lesson 7 shows that $\mathrm{PA} \nvdash \mathrm{PH}$. The same proof in $\mathsf{ACA}_0 + \forall n\ \mathsf{RT}^n$, which is equivalent to $\mathsf{ACA}'_0$ (McAloon), proves $\mathrm{PH}$.

:::quiz[the truth of the Paris–Harrington principle]
In the proof of :ref{#thm-ph-true}, where is the infinite homogeneous set $Y$ used to obtain *relative* largeness, and not only size?

- [x] An infinite set has initial segments of every finite size, in particular of size $\min Y + 1$, which is more than the minimum of the segment.
- [ ] König's lemma provides a relatively large set.

  König's lemma only provides the infinite coloring $F$; it says nothing about homogeneity.
- [ ] Every infinite set is relatively large.

  Relative largeness is a property of finite sets; it is obtained by choosing a long enough finite part of $Y$.

:::

## Exercises

::::exercise{difficulty=1}
Show that $[a, b] \to_* (1)^1_1$ if and only if $b \geq 2a$, and that $[a, 2a] \to_* (1)^1_1$ while $[a + 1, 2a] \not\to_* (1)^1_1$ for $a \geq 1$. Explain why item 3 of :ref{#ex-relatively-large} allows the left endpoint to decrease but not to increase.

:::solution
With one color, every subset of $[a, b]$ is homogeneous, and the best candidate is $[a, b]$ itself, whose minimum is smallest and size largest; it is relatively large if and only if $b - a + 1 > a$, that is $b \geq 2a$. The interval $[a + 1, 2a]$ has $a$ elements and minimum $a + 1$, and no subset of it is relatively large. Decreasing the left endpoint enlarges the interval, so a relatively large homogeneous set of the smaller interval remains one; increasing it removes the small elements, and relative largeness depends on the minimum.
:::
::::

## Notes and references

The principle and :ref{#thm-ph-true} are due to Paris and Harrington (1977); Hájek and Pudlák state it in Chapter II, 1.2–1.3, and prove its finite instances in fragments in Theorem II.1.9 (from the low basis theorem in fragments, a proof finer than the one above, which gives $\mathrm I\Sigma_n \vdash \mathrm{PH}_n$ for the colorings of $n$-sets, and $\mathrm I\Sigma_n \vdash \mathrm{PH}_{n+1}$ for each standard number of colors). Ramsey's theorem in $\mathsf{ACA}_0$ is Simpson, Lemma III.7.4 and Theorem III.7.6. The equivalence of $\forall n\ \mathsf{RT}^n$ with $\mathsf{ACA}'_0$ is due to McAloon (1985); see Dzhafarov and Mummert, Theorem 8.1.6.

*Recent work.* The first-order strength of Ramsey's theorem for pairs is measured by the methods of this course. The $\alpha$-large sets of lesson 8, which generalize relative largeness, are now a standard tool for measuring the first-order strength of Ramsey-type principles. Patey and Yokoyama (2018) proved that $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ is $\forall\Pi^0_3$-conservative over $\mathsf{RCA}_0$, through bounds on $\alpha$-large homogeneous sets for colorings of pairs; Kołodziejczyk and Yokoyama (2020) gave explicit bounds (every $2$-coloring of pairs of an $\omega^{300n}$-large set has an $\omega^n$-large homogeneous set) and a more direct proof; Kołodziejczyk, Wong and Yokoyama showed that the conservation costs only a polynomial increase in the size of proofs. Le Houérou, Levy Patey and Yokoyama extended the conservation to $\forall\Pi^0_4$ sentences over $\mathsf{RCA}_0 + \mathrm B\Sigma^0_2$, and Le Houérou and Patey obtained bounds of the form $\omega^{nk + 3}$ for $k$-colorings of pairs, optimal up to an additive constant. Whether $\mathsf{RT}^2_2$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathrm B\Sigma^0_2$, that is whether its first-order part is that of $\mathrm B\Sigma_2$, remains open. Bovykin and Weiermann (2017) measure infinitary Ramsey principles by their "densities", a notion of largeness obtained by iterating relative largeness, introduced by Paris. The works of Kołodziejczyk, Wong and Yokoyama, of Le Houérou, Levy Patey and Yokoyama, and of Le Houérou and Patey are cited from arXiv (2020–2026).

- J. Paris and L. Harrington, *A mathematical incompleteness in Peano arithmetic*, in J. Barwise (ed.), Handbook of Mathematical Logic, North-Holland, 1977, 1133–1142.
- K. McAloon, *Paris–Harrington incompleteness and progressions of theories*, in Recursion Theory, Proceedings of Symposia in Pure Mathematics 42, American Mathematical Society, 1985, 447–460.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.1.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter II, Section 1.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009, Section III.7.
- L. A. Kołodziejczyk and K. Yokoyama, *Some upper bounds on ordinal-valued Ramsey numbers for colourings of pairs*, Selecta Mathematica (New Series) 26 (2020), article 56.
- L. A. Kołodziejczyk, T. L. Wong and K. Yokoyama, *Ramsey's theorem for pairs, collection, and proof size*, arXiv:2005.06854.
- L. Patey and K. Yokoyama, *The proof-theoretic strength of Ramsey's theorem for pairs and two colors*, Advances in Mathematics 330 (2018), 1034–1070.
- Q. Le Houérou, L. Levy Patey and K. Yokoyama, *$\Pi^0_4$ conservation of Ramsey's theorem for pairs*, arXiv:2404.18974; and *Conservation of Ramsey's theorem for pairs and well-foundedness*, arXiv:2402.11616.
- Q. Le Houérou and L. Patey, *Partition theorems for Ketonen–Solovay largeness: Hardy-like version*, arXiv:2602.08778.
- A. Bovykin and A. Weiermann, *The strength of infinitary Ramseyan principles can be accessed by their densities*, Annals of Pure and Applied Logic 168 (2017), 1700–1709.
