---
title: Cohesiveness and stable colorings
summary: Cohesive sets; stable colorings of pairs and their limit sets; Ramsey's theorem for pairs decomposes into the cohesiveness principle and stable Ramsey's theorem; stable Ramsey's theorem is equivalent to the statement that every Δ⁰₂ set has an infinite subset in it or in its complement.
duration: 35
prerequisites: [jockusch]
---

The proof of Ramsey's theorem for pairs through pre-homogeneous sets mixes two different tasks. The first is to make the coloring **stable**, so that each element has a limit color; the second is to choose an infinite set of elements with the same limit color. Cholak, Jockusch and Slaman (2001) isolated the two tasks as separate principles. The first is the cohesiveness principle, whose instances are sequences of sets; the second is a statement about $\Delta^0_2$ sets. This decomposition reduces many questions about Ramsey's theorem for pairs to simpler ones, and it is the starting point of the proof of Seetapun's theorem in the next lesson.

## Cohesive sets

Write $X \subseteq^* Y$ if $X \setminus Y$ is finite.

:::definition{#def-cohesive}
Let $\vec R = (R_i)_{i \in \nat}$ be a sequence of sets. An infinite set $C$ is **$\vec R$-cohesive** if for every $i$, $C \subseteq^* R_i$ or $C \subseteq^* \overline{R_i}$. The **cohesiveness principle** $\mathsf{COH}$ states that every sequence of sets has a cohesive set.
:::

A cohesive set cannot be split by any of the sets $R_i$ into two infinite parts. Every infinite subset of an $\vec R$-cohesive set is $\vec R$-cohesive. Sets cohesive for the sequence of all computable sets are called **r-cohesive**; they are the computability-theoretic analogues of non-principal ultrafilters, restricted to countably many sets.

:::proposition{#prop-cohesive-exists}
Every sequence $\vec R$ has an $\vec R$-cohesive set computable in $\vec R''$.
:::

:::proof{of=prop-cohesive-exists}
Define sets $X_0 = \nat$ and $X_{i+1} = X_i \cap R_i$ if this set is infinite, and $X_{i+1} = X_i \cap \overline{R_i}$ otherwise. By induction, each $X_i$ is infinite, and an index of $X_i$ as an $\vec R$-computable set is obtained from the previous choices. Each choice asks whether an $\vec R$-computable set is infinite, a $\Pi^0_2(\vec R)$ question, answered by $\vec R''$. Let $c_i$ be the least element of $X_{i+1}$ larger than $c_{i-1}$, and $C = \{ c_0 < c_1 < \cdots \}$. For each $i$, all $c_j$ with $j \geq i$ belong to $X_{j+1} \subseteq X_{i+1}$, which is contained in $R_i$ or in $\overline{R_i}$. So $C$ is cohesive, and $\vec R''$-computable.
:::

Much better bounds hold. Jockusch and Stephan (1993) showed that a set computes a cohesive set for every computable sequence if and only if its jump is PA relative to $\emptyset'$, and Cholak, Jockusch and Slaman showed that every computable sequence has a cohesive set $C$ with $C' \leq_T P$ for any given $P$ PA relative to $\emptyset'$. In particular, cohesive sets for computable sequences can be **low₂**: $C'' \leq_T \emptyset''$. We admit these results.

## Stable colorings

:::definition{#def-stable-coloring}
A coloring $f : [\nat]^2 \to 2$ is **stable** if for every $x$, the limit $\lim_y f(\{ x, y \})$ exists. Its **limit set** is $A_f = \{ x : \lim_y f(\{ x, y \}) = 1 \}$. $\mathsf{SRT}^2_2$ is $\mathsf{RT}^2_2$ restricted to stable colorings.
:::

The limit set of a stable coloring is $\Delta^0_2(f)$, by the limit lemma; conversely, every $\Delta^0_2$ set is the limit set of a computable stable coloring: if $A(x) = \lim_s A_s(x)$, let $f(\{ x, y \}) = A_y(x)$ for $x < y$.

:::theorem[Cholak, Jockusch, Slaman]{#thm-rt22-decomposition}
For every coloring $f : [\nat]^2 \to 2$ and every set $C$ cohesive for the sequence $R_x = \{ y : f(\{ x, y \}) = 1 \}$, the restriction of $f$ to $[C]^2$ is stable. Consequently, over $\mathsf{RCA}_0$, $\mathsf{SRT}^2_2 + \mathsf{COH}$ implies $\mathsf{RT}^2_2$.
:::

:::proof{of=thm-rt22-decomposition}
Let $x \in C$. Since $C \subseteq^* R_x$ or $C \subseteq^* \overline{R_x}$, $f(\{ x, y \})$ is constant for all large $y \in C$: the limit along $C$ exists.

For the second statement, let $f$ be a coloring, and let $C$ be cohesive for the sequence $(R_x)$, which exists by $\Delta^0_1$ comprehension. Let $p$ be the increasing enumeration of $C$, and $g(\{ i, j \}) = f(\{ p(i), p(j) \})$; it is stable by the first part. By $\mathsf{SRT}^2_2$, $g$ has an infinite homogeneous set $H$, and $p[H] \subseteq C$ is homogeneous for $f$.
:::

The converse holds as well: $\mathsf{RT}^2_2$ implies $\mathsf{COH}$ over $\mathsf{RCA}_0$, by a theorem of Cholak, Jockusch and Slaman, with a correction by Mileti; we admit it (Hirschfeldt, *Slicing the Truth*, Chapter 6). So $\mathsf{RT}^2_2$ is equivalent to $\mathsf{SRT}^2_2 + \mathsf{COH}$. Chong, Slaman and Yang (2014) showed that $\mathsf{SRT}^2_2$ is strictly weaker than $\mathsf{RT}^2_2$, using non-standard models; on ω-models, the separation was obtained by Monin and Patey (2021).

:::quiz[the decomposition]
In the proof of :ref{#thm-rt22-decomposition}, why is the restriction of $f$ to a cohesive set stable?

- [x] Because cohesiveness for the set $R_x$ of $y$ with $f(\{ x, y \}) = 1$ means that the color of $\{ x, y \}$ is eventually constant for $y \in C$.
- [ ] Because $C$ is homogeneous for $f$.

  A cohesive set need not be homogeneous: different $x$ may have different limit colors.
- [ ] Because $C$ is computable in $f''$.

  The complexity of $C$ plays no role in stability.
:::

## Stable Ramsey's theorem and Δ⁰₂ sets

:::definition{#def-d22}
$\mathsf D^2_2$ is the statement: for every stable coloring $f$, there is an infinite set $H$ contained in $A_f$ or in $\overline{A_f}$. Equivalently, every $\Delta^0_2$ set, given by an approximation, has an infinite subset of itself or of its complement.
:::

:::proposition{#prop-srt-d22}
For every stable coloring $f$:

1. every infinite set homogeneous for $f$ is contained in $A_f$ or in $\overline{A_f}$;
2. every infinite set $H \subseteq A_f$, or $H \subseteq \overline{A_f}$, computes together with $f$ an infinite homogeneous set for $f$.
:::

:::proof{of=prop-srt-d22}
1. Let $H$ be homogeneous with color $i$. For $x \in H$, $f(\{ x, y \}) = i$ for all $y \in H$ above $x$, so the limit of $f(\{ x, y \})$, which exists, is $i$: $x \in A_f$ if $i = 1$ and $x \in \overline{A_f}$ if $i = 0$.
2. Suppose $H \subseteq A_f$, the other case being symmetric. Define $x_0 = \min H$ and $x_{j+1}$ the least $y \in H$ with $y > x_j$ and $f(\{ x_i, y \}) = 1$ for all $i \leq j$. It exists: each $x_i$ belongs to $A_f$, so $f(\{ x_i, y \}) = 1$ for all large $y$, and there are finitely many $i \leq j$. The sequence is computable in $f \oplus H$, and $\{ x_0 < x_1 < \cdots \}$ is homogeneous with color $1$.
:::

So, on ω-models, $\mathsf{SRT}^2_2$ and $\mathsf D^2_2$ are equivalent. The equivalence over $\mathsf{RCA}_0$ requires more care in item (2), where the existence of $x_{j+1}$ uses a bounding principle for $\Sigma^0_2$ formulas; Chong, Lempp and Yang (2010) showed that it nevertheless holds over $\mathsf{RCA}_0$.

The complexity of solutions to $\mathsf D^2_2$ is delicate. Every $\Delta^0_2$ set has an infinite subset of itself or of its complement that is low₂ (Cholak, Jockusch, Slaman, 2001), but some $\Delta^0_2$ sets have no such subset that is low (Downey, Hirschfeldt, Lempp, Solomon, 2001); both results are admitted.

:::quiz[stable colorings]
In :ref{#prop-srt-d22} (2), where is the stability of $f$ used?

- [x] To guarantee that each chosen $x_i \in A_f$ has $f(\{ x_i, y \}) = 1$ for all large $y$, so that a common later element $y \in H$ exists.
- [ ] To show that $H$ is infinite.

  $H$ is infinite by hypothesis.
- [ ] To compute $A_f$ from $f$.

  $A_f$ is not computable from $f$ in general; the construction only uses $f$ and $H$.
:::

## Exercises

::::exercise{difficulty=1}
Show that every infinite subset of an $\vec R$-cohesive set is $\vec R$-cohesive, and that a set is r-cohesive if and only if it is cohesive for the sequence of all computable sets $(\Phi_e)$, where $\Phi_e$ is replaced by $\emptyset$ when it is not the characteristic function of a set.

:::solution
If $C \subseteq^* R_i$ and $D \subseteq C$, then $D \setminus R_i \subseteq C \setminus R_i$ is finite. The second statement is the definition: the sequence lists every computable set, together with copies of $\emptyset$, for which cohesiveness is automatic since $C \subseteq \overline{\emptyset}$.
:::
::::

::::exercise{difficulty=2}
Show that for every computable coloring $f : [\nat]^2 \to 2$, there is an infinite homogeneous set computable in $\emptyset''$, using the decomposition: a cohesive set computable in $\emptyset''$ and a solution to the induced stable coloring.

:::solution
By :ref{#prop-cohesive-exists}, the computable sequence $R_x = \{ y : f(\{ x, y \}) = 1 \}$ has a cohesive set $C \leq_T \emptyset''$. Its construction also tells, computably in $\emptyset''$, for each $x$ whether $C \subseteq^* R_x$ or $C \subseteq^* \overline{R_x}$: this is the choice made at step $x + 1$. So the set $A$ of $x \in C$ such that $f(\{ x, y \}) = 1$ for almost all $y \in C$ is computable in $\emptyset''$, and so is $C \setminus A$. One of them is infinite; call it $H$. The restriction of $f$ to $C$ is stable (:ref{#thm-rt22-decomposition}), $H$ is contained in its limit set or in the complement, and :ref{#prop-srt-d22} (2), applied to the restriction of $f$ to $C$, gives an infinite homogeneous set computable in $f \oplus C \oplus H \leq_T \emptyset''$.
:::
::::

## Notes and references

Cohesive sets were studied by Jockusch and Stephan (1993). The decomposition of Ramsey's theorem for pairs is due to Cholak, Jockusch and Slaman (2001), whose paper initiated the modern reverse mathematics of Ramsey's theorem; the proof that $\mathsf{RT}^2_2$ implies $\mathsf{COH}$ was corrected by Mileti.

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- C. T. Chong, T. A. Slaman and Y. Yang, *The metamathematics of stable Ramsey's theorem for pairs*, Journal of the American Mathematical Society 27 (2014), 863–892.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics 389 (2021), 107903.
