---
title: The Paris–Harrington principle
summary: Relatively large homogeneous sets and the Paris–Harrington principle; its truth, from the infinite Ramsey theorem and König's lemma; each instance of fixed arity is provable in ACA₀, hence in Peano arithmetic; relatively large homogeneous sets give min-homogeneous sets for regressive colorings.
duration: 45
prerequisites: [indicators, ramsey-theorem/triples, big-five/aca0-reversals, induction-conservation/first-order-parts]
---

The independence results of the previous lessons concern the totality of functions defined for the purpose. Paris and Harrington (1977) found a statement of finite combinatorics, a slight strengthening of the finite Ramsey theorem, that is true and not provable in Peano arithmetic. The strengthening asks for a homogeneous set that is **relatively large**: it has more elements than its least element. This lesson states the principle, proves it from the infinite Ramsey theorem, shows that each instance of fixed arity is provable in $\mathrm{PA}$, and proves a combinatorial lemma that turns relatively large homogeneous sets into the indiscernibles of the next lesson.

## Relatively large homogeneous sets

For a set $X$ of natural numbers, $[X]^n$ is the set of its $n$-element subsets, identified with increasing $n$-tuples; $[a, b]$ is the interval $\{ a, \dots, b \}$, and $c = \{ 0, \dots, c - 1 \}$. A **coloring** is a function $f : [X]^n \to c$, and $H \subseteq X$ is **homogeneous** for $f$ if $f$ is constant on $[H]^n$.

:::definition{#def-relatively-large}
A finite set $H$ is **relatively large** if $|H| > \min H$. For numbers $a \leq b$ and $k, n, c$, the relation $[a, b] \to_* (k)^n_c$ means: every coloring $f : [[a, b]]^n \to c$ has a homogeneous set $H$ that is relatively large and has at least $k$ elements.

The **Paris–Harrington principle** $\mathrm{PH}$ is $\forall n\ \forall c\ \forall k\ \forall a\ \exists b\ [a, b] \to_* (k)^n_c$. For a fixed $n$, $\mathrm{PH}_n$ is $\forall c\ \forall k\ \forall a\ \exists b\ [a, b] \to_* (k)^n_c$.
:::

Without the condition "relatively large", this is the **finite Ramsey theorem**, which follows from the infinite one by compactness and is provable in $\mathrm I\Sigma_1$ (Hájek and Pudlák, Theorem II.1.10). The condition is a lower bound on the size of $H$ that depends on where $H$ lies: a homogeneous set far out must be large. Relative largeness is the first instance of the $\alpha$-large sets of lesson 6, for $\alpha = \omega$.

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

$\mathsf{ACA}_0$ proves each $\mathsf{RT}^n$, not $\forall n\ \mathsf{RT}^n$ (:ref{#thm-rt3-aca}), so the proof says nothing about $\mathrm{PH}$ itself in $\mathrm{PA}$; lesson 5 shows that $\mathrm{PA} \nvdash \mathrm{PH}$. The same proof in $\mathsf{ACA}_0 + \forall n\ \mathsf{RT}^n$, which is equivalent to $\mathsf{ACA}'_0$ (McAloon), proves $\mathrm{PH}$.

:::quiz[the truth of the Paris–Harrington principle]
In the proof of :ref{#thm-ph-true}, where is the infinite homogeneous set $Y$ used to obtain *relative* largeness, and not only size?

- [x] An infinite set has initial segments of every finite size, in particular of size $\min Y + 1$, which is more than the minimum of the segment.
- [ ] König's lemma provides a relatively large set.

  König's lemma only provides the infinite coloring $F$; it says nothing about homogeneity.
- [ ] Every infinite set is relatively large.

  Relative largeness is a property of finite sets; it is obtained by choosing a long enough finite part of $Y$.

:::

## Regressive colorings

Relative largeness is used through a consequence due to Kanamori and McAloon: colorings with unboundedly many colors, provided each value is below the least element of its argument, have large sets on which the value depends only on the least element.

:::definition[Kanamori, McAloon]{#def-regressive}
A function $f : [X]^n \to \nat$ is **regressive** if $f(s) < \min s$ for every $s \in [X]^n$. A set $H \subseteq X$ is **min-homogeneous** for $f$ if $f(s) = f(t)$ for all $s, t \in [H]^n$ with $\min s = \min t$.
:::

For instance, $f(\{ x, y \}) = $ the remainder of $y$ modulo $x$, on $[1, \infty)$, is regressive; a set $\{ x_0 < x_1 < \cdots \}$ is min-homogeneous when, for each $i$, all $x_j$ with $j > i$ have the same remainder modulo $x_i$. Homogeneity cannot be asked for (last exercise).

:::lemma{#lem-ph-regressive}
Let $n \geq 2$, $k \geq 1$ and $1 \leq a \leq b$. If $[a + n, b + n] \to_* (k + n - 1)^{n+1}_{2^{n-1}}$, then every regressive $f : [[a, b]]^n \to \nat$ has a min-homogeneous set with at least $k$ elements.
:::

The idea is to color an $(n+1)$-set $t = \{ t_0 < \cdots < t_n \}$ by recording, for each $j$ between $1$ and $n - 1$, whether the two $n$-sets obtained by removing $t_j$ or $t_{j+1}$ have the same value. On a homogeneous set, a coordinate other than the least can then be moved without changing the value, and the moves connect any two $n$-sets with the same minimum. The homogeneous color must say "same value" everywhere: otherwise, many $n$-sets with the same minimum would have pairwise distinct values, all below that minimum, and relative largeness gives more such sets than there are possible values.

:::proof{of=lem-ph-regressive}
For $t = \{ t_0 < \cdots < t_n \} \subseteq [a, b]$, let $C(t)$ be the set of $j \in \{ 1, \dots, n - 1 \}$ such that $f(t \setminus \{ t_j \}) = f(t \setminus \{ t_{j+1} \})$, coded as a number below $2^{n-1}$. The coloring $C'(t) = C(t - n)$ of $[[a + n, b + n]]^{n+1}$, where $t - n$ is the translate of $t$, has a relatively large homogeneous set $H'$ with at least $k + n - 1$ elements. Its translate $H = H' - n \subseteq [a, b]$ is homogeneous for $C$, has $N \geq k + n - 1$ elements, and $N > \min H' = \min H + n$. Write $H = \{ x_0 < \cdots < x_{N-1} \}$.

*The color is $\{ 1, \dots, n - 1 \}$.* Suppose $j \notin C$ on $[H]^{n+1}$. For $y \in H$ with $x_{j-1} < y < x_{N-n+j+1}$, with the convention $x_N = \infty$, let
$$
s_y = \{ x_0, \dots, x_{j-1} \} \cup \{ y \} \cup \{ x_{N-n+j+1}, \dots, x_{N-1} \},
$$
an $n$-set in which $y$ has position $j$. For $y < y'$ of this kind, $t = s_y \cup \{ y' \}$ is an $(n+1)$-set with $t_j = y$ and $t_{j+1} = y'$; removing $t_{j+1}$ gives $s_y$, removing $t_j$ gives $s_{y'}$, and $j \notin C(t)$ gives $f(s_y) \neq f(s_{y'})$. There are $N - n + 1$ such $y$, namely $x_j, \dots, x_{N-n+j}$, and the values $f(s_y)$ are pairwise distinct and below $\min s_y = x_0$, since $f$ is regressive. So $N - n + 1 \leq x_0$, contradicting $N > x_0 + n$.

*Moving coordinates.* So $C = \{ 1, \dots, n - 1 \}$ on $[H]^{n+1}$. Let $u = \{ u_0 < \cdots < u_{n-1} \} \subseteq H$, $1 \leq j \leq n - 1$, and $y \in H \setminus u$ with $u_{j-1} < y < u_{j+1}$ (where $u_n = \infty$); let $u'$ be $u$ with $u_j$ replaced by $y$. Then $t = u \cup \{ y \}$ is an $(n+1)$-set in which $u_j$ and $y$ are adjacent, at positions $j$ and $j + 1$ in some order, and removing one or the other gives $u$ and $u'$; as $j \in C(t)$, $f(u) = f(u')$.

*Min-homogeneity.* Let $H_0$ be $H$ without its $n - 1$ largest elements $w_1 < \cdots < w_{n-1}$; $|H_0| \geq k$. Let $u \in [H_0]^n$. Move $u_{n-1}$ to $w_{n-1}$, then $u_{n-2}$ to $w_{n-2}$, and so on down to $u_1$ to $w_1$: at each step the new value lies strictly between the coordinate below and the one above, so the move is allowed. Hence $f(u) = f(\{ u_0, w_1, \dots, w_{n-1} \})$, which depends only on $\min u = u_0$. So $H_0$ is min-homogeneous.
:::

The translation by $n$ trades the relative largeness of $H'$ for the stronger condition $|H| > \min H + n$, which the counting argument requires; this is why the hypothesis concerns $[a + n, b + n]$.

:::quiz[regressive colorings]
In the proof of :ref{#lem-ph-regressive}, where is it used that $f$ is regressive?

- [x] To bound the number of possible values of $f(s_y)$ by $x_0 = \min s_y$, which the pairwise distinct values exceed.
- [ ] To show that the moves of coordinates preserve the value of $f$.

  The moves only use the homogeneous color $C = \{ 1, \dots, n - 1 \}$.
- [ ] To make $C$ a coloring with finitely many colors.

  $C$ takes values below $2^{n-1}$ whatever $f$ is.

---

Why is the least coordinate $u_0$ never moved?

- [x] Every comparison made by $C$ keeps $t_0$ in both $n$-sets, so the colors give no information on what happens when the minimum changes; and min-homogeneity does not require it.
- [ ] Because $u_0$ is in $H_0$.

  All coordinates of $u$ are in $H_0$.
- [ ] Because moving it would break regressiveness.

  Regressiveness is a property of $f$, not of the moves.
:::

## Formalization

The arguments of this lesson other than :ref{#thm-ph-true} are finite combinatorics with coded objects: colorings, homogeneous sets and translates are coded in $\mathrm I\Delta_0 + \mathrm{exp}$ by bounded definitions, and the only principle used beyond bounded induction is the pigeonhole principle for coded functions (exercise of :ref{to="fragments-of-arithmetic/coding"}). So they hold in every model of $\mathrm I\Sigma_1$, for non-standard parameters and colorings coded in the model. This is how :ref{#lem-ph-regressive} is used in the next lesson.

## Exercises

::::exercise{difficulty=2}
Let $f : [X]^2 \to \nat$, $f(\{ x, y \}) = x - 1$, on $X = [1, b]$. Show that $f$ is regressive, that every set is min-homogeneous for $f$, and that a homogeneous set for $f$ has at most two elements. Deduce that "min-homogeneous" cannot be replaced by "homogeneous" in :ref{#lem-ph-regressive}.

:::solution
$f(\{ x, y \}) = x - 1 < x = \min \{ x, y \}$. The value depends only on the minimum, so every set is min-homogeneous. If $x < y < z$ are in a homogeneous set, $f(\{ x, y \}) = x - 1 \neq y - 1 = f(\{ y, z \})$. So no homogeneous set has three elements, while the lemma, for $k \geq 3$, provides min-homogeneous sets of size $k$ when $b$ is large enough.
:::
::::

## Notes and references

The principle and :ref{#thm-ph-true} are due to Paris and Harrington (1977); Hájek and Pudlák state it in Chapter II, 1.2–1.3, and prove its finite instances in fragments in Theorem II.1.9 (from the low basis theorem in fragments, a proof finer than the one above, which gives $\mathrm I\Sigma_n \vdash \mathrm{PH}_n$ for the colorings of $n$-sets, and $\mathrm I\Sigma_n \vdash \mathrm{PH}_{n+1}$ for each standard number of colors). Ramsey's theorem in $\mathsf{ACA}_0$ is Simpson, Lemma III.7.4 and Theorem III.7.6. Regressive colorings and min-homogeneous sets are due to Kanamori and McAloon (1987), who showed that the corresponding principle is equivalent to $\mathrm{PH}$; :ref{#lem-ph-regressive} is one direction of this equivalence, with a proof written for this course.

- J. Paris and L. Harrington, *A mathematical incompleteness in Peano arithmetic*, in J. Barwise (ed.), Handbook of Mathematical Logic, North-Holland, 1977, 1133–1142.
- A. Kanamori and K. McAloon, *On Gödel incompleteness and finite combinatorics*, Annals of Pure and Applied Logic 33 (1987), 23–41.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter II, Section 1.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009, Section III.7.
