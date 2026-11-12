---
title: Lower bounds and Ramsey's theorem for triples
summary: A computable coloring of pairs without Δ⁰₂ homogeneous set; a Δ⁰₂ coloring of n-tuples is the limit of a computable coloring of (n+1)-tuples; a computable coloring of triples codes the halting set into all its homogeneous sets; Ramsey's theorem for n-tuples, n ≥ 3, is equivalent to ACA₀; WKL₀ does not prove Ramsey's theorem for pairs.
duration: 50
prerequisites: [jockusch]
---

The previous lesson showed that homogeneous sets for computable colorings of $n$-tuples can be found computably in any degree PA over $\obf^{(n-1)}$. This lesson proves lower bounds of two kinds. The first concerns the **complexity** of homogeneous sets: some computable coloring of pairs has no $\Delta^0_2$ infinite homogeneous set. The second concerns their **coding power**: can a computable coloring force every infinite homogeneous set to compute a given non-computable set? A coloring with no $\Delta^0_2$ homogeneous set does not do this by itself, since a set can fail to be $\Delta^0_2$ without computing anything in particular. For triples, the answer is positive: the halting set can be coded. This lesson proves it, and deduces the equivalence of Ramsey's theorem for triples with $\mathsf{ACA}_0$.

## The lower bound

Specker (1971) built a computable coloring of pairs without computable infinite homogeneous set. Jockusch's theorem below improves this to $\Delta^0_2$ sets. The idea is a **diagonalization against the $\Delta^0_2$ sets through their approximations**. By the limit lemma, every $\Delta^0_2$ set $A$ is the limit of a computable sequence of finite approximations, and these approximations can be listed uniformly. The coloring is defined stage by stage: at stage $s$, it colors the pairs $\{ x, s \}$ with $x < s$. If $s$ belongs to an infinite $\Delta^0_2$ set $A$, the approximation at stage $s$ already knows a few elements of $A$ correctly, and the construction gives two of them different colors with $s$. Then $A$ contains three elements $a < b < s$ with $f(\{ a, s \}) \neq f(\{ b, s \})$, and $A$ is not homogeneous. All the requirements act at every stage, on disjoint pairs, so they never conflict.

:::theorem[Jockusch]{#thm-jockusch-no-delta2}
There is a computable coloring $f : [\nat]^2 \to 2$ with no infinite $\Delta^0_2$ homogeneous set, hence no infinite $\Sigma^0_2$ homogeneous set.
:::

:::proof{of=thm-jockusch-no-delta2}
For each $e$ and $s$, let $A_{e,s} = \{ x < s : \Phi^{\emptyset'_s}_e(x)[s]\converge = 1 \}$, where $\emptyset'_s$ is the stage $s$ approximation of $\emptyset'$. If $\Phi^{\emptyset'}_e$ is the characteristic function of a set $A$, then for every $x$, $x \in A_{e,s}$ for all large $s$ if $x \in A$, and $x \notin A_{e,s}$ for all large $s$ otherwise. Every $\Delta^0_2$ set is of this form, by the limit lemma.

Define $f(\{ x, s \})$ for $x < s$ at stage $s$: for $e = 0, 1, \dots, s - 1$ in turn, if $A_{e,s}$ has at least $2e + 2$ elements, choose the two least elements $a < b$ of $A_{e,s}$ for which $f(\{ a, s \})$ and $f(\{ b, s \})$ are not yet defined, and set $f(\{ a, s \}) = 0$ and $f(\{ b, s \}) = 1$. Before $e$ acts, at most $2e$ values $f(\{ x, s \})$ have been defined, so the two elements exist. All remaining values $f(\{ x, s \})$ are set to $0$. The coloring is computable.

Let $A = \Phi^{\emptyset'}_e$ be an infinite $\Delta^0_2$ set, and $n$ such that $A \cap \{0, \dots, n-1\}$ has exactly $2e + 2$ elements. For large enough $s \in A$, $A_{e,s} \cap \{0, \dots, n-1\} = A \cap \{0, \dots, n-1\}$. At stage $s$, the $2e + 2$ least elements of $A_{e,s}$ are those of $A$ below $n$, and $e$ chooses two of them, $a$ and $b$, with $f(\{ a, s \}) \neq f(\{ b, s \})$. Since $a, b, s \in A$, $A$ is not homogeneous.

Finally, every infinite $\Sigma^0_2$ set $B = \{ x : \exists y\, \forall z\, R(x, y, z) \}$, with $R$ computable, has an infinite $\Delta^0_2$ subset: with $\emptyset'$, search for pairs $(x, y)$ with $\forall z\, R(x, y, z)$, and keep an increasing sequence of the first coordinates found. A subset of a homogeneous set is homogeneous.
:::

In particular, the coloring has no computable infinite homogeneous set, so the ω-model of the computable sets does not satisfy $\mathsf{RT}^2_2$, and $\mathsf{RCA}_0$ does not prove $\mathsf{RT}^2_2$ (Specker's theorem).

The two bounds leave a gap at pairs: homogeneous sets for computable colorings can always be found below $\emptyset''$, and sometimes not below $\emptyset'$. Whether every homogeneous set must carry some specific computational power is a different question. The next sections show that for triples it must; for pairs, it is the question of the rest of the course.

:::quiz[the lower bound]
In the proof of :ref{#thm-jockusch-no-delta2}, why does the requirement for $e$ wait until $A_{e,s}$ has at least $2e + 2$ elements?

- [x] Because the requirements $e' < e$ may already have used up to $2e$ elements at stage $s$; with $2e + 2$ elements, two remain available for $e$.
- [ ] Because $A$ must have at least $2e + 2$ elements to be infinite.

  An infinite set has arbitrarily many elements; the bound is about sharing the stage $s$ among requirements.
- [ ] To ensure that $f$ is computable.

  $f$ is computable whatever the threshold; the threshold guarantees that two fresh elements exist.

---

In the same proof, why are the elements $a$ and $b$ taken among the least elements of $A_{e,s}$, rather than anywhere in $A_{e,s}$?

- [x] Because only finitely many elements of the approximation are guaranteed to be correct at a given stage: for large $s$, the elements of $A_{e,s}$ below $n$ are exactly those of $A$, while larger elements of $A_{e,s}$ may not belong to $A$.
- [ ] Because $f(\{ x, s \})$ is only defined for small $x$.

  It is defined for every $x < s$.
- [ ] Because $A$ is finite.

  $A$ is infinite by hypothesis; the issue is the correctness of the approximation.
:::

## Limits of colorings

One additional element in the tuples can play the role of a stage of an approximation.

:::lemma{#lem-limit-coloring}
For every $\emptyset'$-computable coloring $h : [\nat]^n \to k$, there is a computable coloring $f : [\nat]^{n+1} \to k$ such that every infinite homogeneous set for $f$ is homogeneous for $h$.
:::

:::proof{of=lem-limit-coloring}
By the limit lemma, $h(\{ x_1, \dots, x_n \}) = \lim_t f(\{ x_1, \dots, x_n, t \})$ for a computable function $f$ defined for $x_1 < \cdots < x_n < t$; replacing the values outside $k$ by $0$, which does not change the limit, $f$ is a coloring $[\nat]^{n+1} \to k$. Let $H$ be infinite and homogeneous for $f$ with color $i$. For $x_1 < \cdots < x_n$ in $H$, take $t \in H$ large enough that $f(\{ x_1, \dots, x_n, t \}) = h(\{ x_1, \dots, x_n \})$; this value is $i$.
:::

The infinity of $H$ is used to find a stage $t \in H$ at which the approximation has converged. The lemma trades one jump in the complexity of the coloring for one more element in the tuples. It relativizes: for every $Z$, a $Z'$-computable coloring of $[\nat]^n$ is the limit of a $Z$-computable coloring of $[\nat]^{n+1}$ with the same property.

:::quiz[limits of colorings]
In the proof of :ref{#lem-limit-coloring}, why does the argument fail for a finite homogeneous set $H$?

- [x] Because the element $t \in H$ must be large enough for the approximation of $h(\{ x_1, \dots, x_n \})$ to have converged, and a finite set may contain no such element.
- [ ] Because a finite set is not homogeneous for $h$.

  Finite sets with fewer than $n$ elements are homogeneous for every coloring; the question is whether the color of $f$ on $H$ is that of $h$.
- [ ] Because $f$ is only defined on infinite sets.

  $f$ is defined on all $(n+1)$-tuples.
:::

## Coding the jump into triples

To code $\emptyset'$, it suffices to force homogeneous sets to grow fast enough. Let $m(x)$ be the **settling time** of $\emptyset'$ below $x$: the least stage $s$ at which the approximation $\emptyset'_s$ agrees with $\emptyset'$ on $\{ 0, \dots, x - 1 \}$. A set containing, after each of its elements $x$, an element larger than $m(x)$ computes $\emptyset'$, by reading the approximation at that element. The function $m$ is $\emptyset'$-computable, so a coloring of pairs expressing "$y$ is larger than $m(x)$" is $\Delta^0_2$, and :ref{#lem-limit-coloring} turns it into a computable coloring of triples.

:::proposition[Jockusch]{#prop-rt32-jump}
There is a computable coloring of $[\nat]^3$ with two colors all of whose infinite homogeneous sets compute $\emptyset'$.
:::

:::proof{of=prop-rt32-jump}
Let $m(x)$ be the least $s$ with $\emptyset'_s \cap \{0, \dots, x - 1\} = \emptyset' \cap \{0, \dots, x - 1\}$, a $\emptyset'$-computable function. Let $h(\{ x, y \}) = 1$ if $m(x) < y$ and $0$ otherwise, for $x < y$. An infinite homogeneous set $H$ for $h$ has color $1$: color $0$ would give $m(x) \geq y$ for all $y > x$ in $H$. So for consecutive elements $x < y$ of $H$, $\emptyset' \cap \{0, \dots, x-1\} = \emptyset'_y \cap \{0, \dots, x-1\}$, and $H$ computes $\emptyset'$. Apply :ref{#lem-limit-coloring}.
:::

:::quiz[coding the jump]
In the proof of :ref{#prop-rt32-jump}, why can an infinite homogeneous set for $h$ not have color $0$?

- [x] Because color $0$ would bound every element $y > x$ of $H$ by $m(x)$, for a fixed $x \in H$, so $H$ would be finite.
- [ ] Because $h$ takes the value $0$ only finitely often.

  For each $x$, $h(\{ x, y \}) = 0$ for the finitely many $y \leq m(x)$, but there are infinitely many such pairs in total.
- [ ] Because $\emptyset'$ is not computable.

  The argument does not use this; it only uses that $m(x)$ is a number.
:::

The coloring $h$ has an unusual feature: for each $x$, $h(\{ x, y \}) = 1$ for all large $y$. Colorings of pairs in which each element has a limit color are called **stable**; they reappear in the lesson on stable colorings, where this example shows that a statement about computable colorings fails for $\Delta^0_2$ ones.

## Reverse mathematics

The equivalence formalizes the two previous results in second-order arithmetic.

:::theorem[Jockusch, Simpson]{#thm-rt3-aca}
For every standard $n \geq 3$, $\mathsf{RT}^n_2$ is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$. Moreover $\mathsf{ACA}_0$ proves $\mathsf{RT}^n_k$ for all standard $n$ and $k$.
:::

:::proof{of=thm-rt3-aca}
*$\mathsf{ACA}_0$ proves $\mathsf{RT}^n_k$*, by induction on $n$ in the metatheory. The case $n = 1$ is :ref{#prop-rt-basic}. Given $f : [\nat]^{n+1} \to k$, the Erdős–Radó tree exists by $\Delta^0_1$ comprehension, and $\mathsf{RCA}_0$ proves that it is infinite and finitely branching. By König's lemma (:ref{#thm-konig-aca}), it has a path, which is pre-homogeneous. The induction hypothesis, with :ref{#prop-rt-basic} (2), whose proof applies to any number of colors, gives a homogeneous set for the induced coloring.

*$\mathsf{RT}^3_2$ implies $\mathsf{ACA}_0$.* We prove that $X'$ exists, using :ref{#thm-aca-equivalents}. Define $f(\{ x, s, t \}) = 1$ for $x < s < t$ if every $e < x$ satisfies $\Phi^X_e(e)[s]\converge \leftrightarrow \Phi^X_e(e)[t]\converge$, and $0$ otherwise. Let $H$ be infinite and homogeneous. Its color is $1$: for $x \in H$, among $2^x + 1$ elements of $H$ above $x$, two have the same pattern of convergence for the indices $e < x$, by the finite pigeonhole principle, provable in $\mathsf{RCA}_0$. For each $e$, let $x_e$ be the least element of $H$ above $e$ and $s_e$ the least element of $H$ above $x_e$. If $\Phi^X_e(e)[t_0]\converge$ for some $t_0$, take $t \in H$ above $s_e$ and $t_0$, so that $\Phi^X_e(e)[t]\converge$; then $f(\{ x_e, s_e, t \}) = 1$ gives $\Phi^X_e(e)[s_e]\converge$. So $X' = \{ e : \Phi^X_e(e)[s_e]\converge \}$, which exists by $\Delta^0_1$ comprehension relative to $X \oplus H$.

For $n \geq 3$, $\mathsf{RT}^n_2$ implies $\mathsf{RT}^3_2$: a coloring $f$ of triples induces the coloring $\{ x_1, \dots, x_n \} \mapsto f(\{ x_1, x_2, x_3 \})$ of $n$-tuples, with the same infinite homogeneous sets.
:::

The coloring used for the reversal is a variant of the one of :ref{#prop-rt32-jump} that can be defined in $\mathsf{RCA}_0$: instead of the settling time, which requires $X'$, it compares the convergence patterns at two stages $s < t$, and homogeneity forces the stages of $H$ to be settling times.

The induction on $n$ in the first part is external: $\mathsf{ACA}_0$ proves each $\mathsf{RT}^n_k$ separately, but not the statement $\forall n\, \forall k\, \mathsf{RT}^n_k$, which is equivalent over $\mathsf{RCA}_0$ to the existence of all finite jumps $X^{(n)}$ of every set $X$ (McAloon; Dzhafarov–Mummert, Theorem 8.1.6; Hirschfeldt, §6.3).

:::corollary{#cor-wkl-not-rt22}
$\mathsf{WKL}_0$ does not prove $\mathsf{RT}^2_2$.
:::

:::proof{of=cor-wkl-not-rt22}
By :ref{#thm-low-scott}, there is an ω-model of $\mathsf{WKL}_0$ consisting of low sets, hence of $\Delta^0_2$ sets. The computable coloring of :ref{#thm-jockusch-no-delta2} belongs to it and has no homogeneous set in it.
:::

The coloring of :ref{#prop-rt32-jump} has no analogue for pairs: by Seetapun's theorem, proved in the last lesson, every computable coloring of pairs has an infinite homogeneous set that does not compute $\emptyset'$. So $\mathsf{RT}^2_2$ lies strictly between $\mathsf{RCA}_0$ and $\mathsf{ACA}_0$, and is not provable in $\mathsf{WKL}_0$.

:::quiz[RT³₂ and ACA₀]
In the proof of :ref{#thm-rt3-aca}, why must an infinite homogeneous set for $f$ have color $1$?

- [x] Because for each $x \in H$, the convergence patterns at stages in $H$ take at most $2^x$ values, so two stages $s < t$ in $H$ above $x$ share a pattern, and $f(\{ x, s, t \}) = 1$.
- [ ] Because $X'$ is infinite.

  The argument does not depend on $X'$; it is a counting argument on patterns.
- [ ] Because $f$ takes the value $1$ on infinitely many triples.

  Many colorings take both values infinitely often; homogeneity of $H$ together with the counting argument fixes the color.
:::

## Exercises

::::exercise{difficulty=1}
Show that for every $n \geq 2$ there is a computable coloring $f : [\nat]^n \to 2$ with no infinite $\Sigma^0_n$ homogeneous set.

:::solution
By induction on $n$, relativized to an arbitrary oracle $Z$: there is a $Z$-computable coloring of $[\nat]^n$ with no infinite $\Sigma^0_n(Z)$ homogeneous set. For $n = 2$, this is :ref{#thm-jockusch-no-delta2} relativized. Given the statement for $n$ and every oracle, apply it to $Z'$: there is a $Z'$-computable coloring $h$ of $[\nat]^n$ with no infinite $\Sigma^0_n(Z')$, that is $\Sigma^0_{n+1}(Z)$, homogeneous set. By :ref{#lem-limit-coloring} relativized to $Z$, there is a $Z$-computable coloring of $[\nat]^{n+1}$ whose infinite homogeneous sets are homogeneous for $h$.
:::
::::

::::exercise{difficulty=2}
Show that for every $n \geq 3$ there is a computable coloring of $[\nat]^n$ with finitely many colors all of whose infinite homogeneous sets compute $\emptyset^{(n-2)}$.

:::solution
We prove by induction on $n \geq 3$ that for every $Z$ there is a $Z$-computable coloring of $[\nat]^n$ with finitely many colors such that $Z^{(n-2)} \leq_T Z \oplus H$ for every infinite homogeneous set $H$. For $n = 3$, this is :ref{#prop-rt32-jump} relativized to $Z$: the set $H$ computes $Z'$ from the approximation $Z'_s$, which is $Z$-computable.

Assume the statement for $n$, and apply it to $Z'$: there is a $Z'$-computable coloring $h$ of $[\nat]^n$ with $Z^{(n-1)} \leq_T Z' \oplus H$ for every infinite homogeneous $H$. By :ref{#lem-limit-coloring} relativized to $Z$, there is a $Z$-computable coloring $f$ of $[\nat]^{n+1}$ whose infinite homogeneous sets are homogeneous for $h$. Let $c$ be the $Z$-computable coloring of triples given by the case $n = 3$, and $c'(\{ x_1, \dots, x_{n+1} \}) = c(\{ x_1, x_2, x_3 \})$. The coloring $e = (f, c')$, with pairs of colors as colors, is $Z$-computable. An infinite homogeneous set $H$ for $e$ is homogeneous for $c'$, hence for $c$, so $Z' \leq_T Z \oplus H$; and it is homogeneous for $f$, hence for $h$, so $Z^{(n-1)} \leq_T Z' \oplus H \leq_T Z \oplus H$.
:::
::::

## Notes and references

Specker (1971) built a computable coloring of pairs without computable infinite homogeneous set, and Jockusch (1972) improved it to :ref{#thm-jockusch-no-delta2} (Hirschfeldt, Theorem 6.11; Dzhafarov–Mummert, Theorem 8.2.2). Jockusch also proved :ref{#lem-limit-coloring} and :ref{#prop-rt32-jump}, as well as the generalization of the second exercise, in which the coloring has two colors; Hirschfeldt presents them as Theorem 6.13 and Exercise 6.15, Dzhafarov and Mummert as Lemma 8.2.1 and Theorem 8.2.4. Simpson formalized the equivalence with $\mathsf{ACA}_0$ (Simpson, Lemmas III.7.4 and III.7.5 and Theorem III.7.6; Hirschfeldt, Exercise 6.14; Dzhafarov–Mummert, Corollary 8.2.6). Hirschfeldt attributes :ref{#cor-wkl-not-rt22} to Hirst (Corollary 6.12). Hirschfeldt and Jockusch strengthened :ref{#prop-rt32-jump}: some computable coloring of triples has all its infinite pre-homogeneous sets, hence all its infinite homogeneous sets, of PA degree relative to $\emptyset'$ (Hirschfeldt, Theorems 6.16 and 6.17). By contrast, the exact coding power of $\mathsf{RT}^3_2$ is $\emptyset'$: a set $X \not\leq_T \emptyset'$ can be avoided by some homogeneous set of every computable coloring of triples (Cholak, Jockusch and Slaman; see the exercises of the lesson on Seetapun's theorem).

- E. Specker, *Ramsey's theorem does not hold in recursive set theory*, in *Logic Colloquium '69*, North-Holland, 1971, 439–442.
- C. G. Jockusch, Jr., *Ramsey's theorem and recursion theory*, Journal of Symbolic Logic 37 (1972), 268–280.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022.
