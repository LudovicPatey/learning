---
title: The pigeonhole principle and Σ⁰₂ collection
summary: The infinite pigeonhole principle for arbitrarily many colors is equivalent to Σ⁰₂ collection over RCA₀ (Hirst); Ramsey's theorem for pairs implies it; what is known of the first-order part of Ramsey's theorem for pairs.
duration: 35
prerequisites: [separations, ramsey-theorem/jockusch]
---

$\mathsf{RCA}_0$ proves the infinite pigeonhole principle $\mathsf{RT}^1_k$ for every standard number $k$ of colors (:ref{#prop-rt-basic}): the proof is a case analysis on finitely many colors. The statement $\mathsf{RT}^1_{<\infty}$, "for every $k$, every coloring $f : \nat \to k$ has an infinite homogeneous set", quantifies over $k$ inside the theory. In a non-standard model, $k$ may be non-standard, and the case analysis is no longer available. Hirst showed that $\mathsf{RT}^1_{<\infty}$ is exactly $\Sigma^0_2$ collection. A combinatorial principle about sets thus has a purely arithmetic content, and so does every principle that implies it, such as Ramsey's theorem for pairs.

## Hirst's theorem

By :ref{#ex-bsigma-bpi}, $\mathsf B\Sigma^0_2$ is equivalent to $\mathsf B\Pi^0_1$ over $\mathsf I\Delta^0_0$. We use the second form.

:::theorem[Hirst]{#thm-hirst}
Over $\mathsf{RCA}_0$, $\mathsf{RT}^1_{<\infty}$ is equivalent to $\mathsf B\Pi^0_1$, hence to $\mathsf B\Sigma^0_2$.
:::

Both directions translate between colorings and families of witnesses. A coloring $f : \nat \to k$ without infinite color class gives, for each color $x < k$, a $\Pi^0_1$ property "$x$ does not occur after $y$", whose witnesses $y$ collection bounds uniformly, which is absurd. Conversely, given an instance $\forall x < k\ \exists y\ \varphi(x, y)$ of $\mathsf B\Pi^0_1$, a computable approximation $f(t)$ measures, at stage $t$, how far one must search to find witnesses that look correct up to $t$. If $f$ is bounded, the pigeonhole principle gives a value $c$ taken infinitely often, and $c$ is a common bound. If $f$ is unbounded, the pigeonhole principle applied to the color responsible for each increase of $f$ gives a single $x_0$ whose candidate witnesses are all eventually refuted, which contradicts the hypothesis.

:::proof{of=thm-hirst}
Recall that $\mathsf{RCA}_0$ proves $\mathsf I\Sigma^0_1$, hence $\mathsf B\Sigma^0_1$ by :ref{#thm-induction-collection}.

($\mathsf B\Pi^0_1 \Rightarrow \mathsf{RT}^1_{<\infty}$) Let $f : \nat \to k$. If there is $x < k$ such that $\forall y\ \exists z > y\ f(z) = x$, the set $\{ z : f(z) = x \}$ exists by $\Delta^0_1$ comprehension, is infinite, and is homogeneous. Otherwise, every $x < k$ satisfies $\exists y\ \forall z > y\ f(z) \neq x$, a $\Pi^0_1$ formula of $x$ and $y$. By $\mathsf B\Pi^0_1$, there is $p$ such that every $x < k$ has some $y < p$ with $\forall z > y\ f(z) \neq x$. Let $x = f(p)$; then $p > y$ for the corresponding $y$, and $f(p) \neq x$: a contradiction.

($\mathsf{RT}^1_{<\infty} \Rightarrow \mathsf B\Pi^0_1$) Let $\varphi(x, y) \equiv \forall z\ \theta(x, y, z)$ with $\theta$ bounded, and suppose $\forall x < k\ \exists y\ \varphi(x, y)$; we may assume $k \geq 1$. For every $t$, let $f(t)$ be the least $n$ such that
$$
\forall x < k\ \exists y < n\ \forall z < t\ \theta(x, y, z).
$$
It exists: every $x < k$ has some $y$ with $\forall z < t\ \theta(x, y, z)$, a bounded condition, so $\mathsf B\Sigma^0_1$ gives a common bound, and the least one exists by $\mathsf L\Sigma^0_1$ (:ref{#prop-least-number}), since a bounded formula is $\Sigma^0_1$. The graph of $f$ is defined by a bounded formula, so $f$ exists by $\Delta^0_1$ comprehension. The condition becomes stronger as $t$ increases, so $f$ is non-decreasing, and $f(t) \geq 1$ since $k \geq 1$.

*Case 1: $f$ is bounded*: there is $\ell$ with $f(t) < \ell$ for every $t$. By $\mathsf{RT}^1_\ell$, there are an infinite set $H$ and $c < \ell$ with $f(t) = c$ for every $t \in H$. We claim $\forall x < k\ \exists y < c\ \varphi(x, y)$, which is the conclusion of $\mathsf B\Pi^0_1$. Otherwise, some $x_0 < k$ satisfies $\forall y < c\ \exists z\ \neg \theta(x_0, y, z)$, and $\mathsf B\Sigma^0_1$ gives $z_0$ with $\forall y < c\ \exists z < z_0\ \neg \theta(x_0, y, z)$. Taking $t \in H$ with $t > z_0$, the definition of $f(t) = c$ gives $y < c$ with $\forall z < t\ \theta(x_0, y, z)$: a contradiction.

*Case 2: $f$ is unbounded.* Since $f(t) - 1$ does not satisfy the condition defining $f(t)$, there is $x < k$ such that $\forall y < f(t) - 1\ \exists z < t\ \neg \theta(x, y, z)$. Let $g(t)$ be the least such $x$; $g : \nat \to k$ exists by $\Delta^0_1$ comprehension. By $\mathsf{RT}^1_k$, there are an infinite set $S$ and $x_0 < k$ with $g(t) = x_0$ for $t \in S$. Let $y$ be any number. Since $f$ is unbounded and non-decreasing, and $S$ is infinite, there is $t \in S$ with $f(t) - 1 > y$, so $\exists z < t\ \neg \theta(x_0, y, z)$. Hence $\forall y\ \neg \varphi(x_0, y)$, contradicting the hypothesis. So case 2 does not occur.
:::

:::quiz[Hirst's theorem]
In the direction $\mathsf{RT}^1_{<\infty} \Rightarrow \mathsf B\Pi^0_1$, where is the pigeonhole principle used for a non-standard number of colors?

- [x] Twice: in case 1 with $\ell$ colors, where $\ell$ bounds $f$, and in case 2 with $k$ colors, where $k$ is the bound in the instance of collection; both may be non-standard.
- [ ] Only in case 2.

  Case 1 also applies the principle, to $f$ with $\ell$ colors.
- [ ] Nowhere: the colors are bounded by $k$.

  $k$ is an arbitrary number of the model, possibly non-standard; this is the whole point.

---

Why can $\mathsf{RCA}_0$ not prove $\mathsf{RT}^1_{<\infty}$ by induction on $k$, from $\mathsf{RT}^1_1$ and $\forall k\, (\mathsf{RT}^1_k \rightarrow \mathsf{RT}^1_{k+1})$?

- [x] Because "every coloring $f : \nat \to k$ has an infinite homogeneous set" quantifies over sets; it is not a $\Sigma^0_1$ formula of $k$, and $\mathsf{RCA}_0$ does not provide induction for it.
- [ ] Because $\mathsf{RT}^1_{k+1}$ does not follow from $\mathsf{RT}^1_k$.

  It does, over $\mathsf{RCA}_0$, as an exercise below shows.
- [ ] Because $\mathsf{RCA}_0$ has no induction.

  It has $\Sigma^0_1$ induction, which does not apply to this formula.
:::

## Ramsey's theorem for pairs

:::proposition[Hirst]{#prop-rt22-bsigma2}
$\mathsf{RCA}_0 + \mathsf{RT}^2_2$ proves $\mathsf{RT}^1_{<\infty}$, hence $\mathsf B\Sigma^0_2$.
:::

:::proof{of=prop-rt22-bsigma2}
Let $f : \nat \to k$. Define $g : [\nat]^2 \to 2$ by $g(\{ x, y \}) = 1$ if $f(x) = f(y)$, and $0$ otherwise; it exists by $\Delta^0_1$ comprehension. Let $H$ be an infinite homogeneous set for $g$. If its color is $1$, then $f$ is constant on $H$, and $H$ is homogeneous for $f$. If its color is $0$, then $f$ is injective on $H$; the first $k + 1$ elements of $H$ form a finite set, which exists in $\mathsf{RCA}_0$, on which $f$ is an injection into $k$. This contradicts the finite pigeonhole principle, which $\mathsf{RCA}_0$ proves by $\Pi^0_1$ induction on $k$. By :ref{#thm-hirst}, $\mathsf B\Sigma^0_2$ follows.
:::

Every ω-model satisfies $\mathsf B\Sigma^0_2$, since its first-order part is $\nat$. The proposition is therefore invisible in ω-models: it says something about the non-standard models of $\mathsf{RT}^2_2$. By :ref{#thm-collection-induction}, $\mathsf B\Sigma^0_2$ implies $\mathsf I\Sigma^0_1$, which $\mathsf{RCA}_0$ already has; but $\mathsf{RCA}_0$ does not prove $\mathsf B\Sigma^0_2$. Indeed, :ref{#thm-isigma-not-bsigma} gives a countable model of $\mathrm I\Sigma_1$ in which $\Sigma_2$ collection fails, and the next lesson shows that every countable model of $\mathrm I\Sigma_1$ is the first-order part of a model of $\mathsf{RCA}_0$. Hence $\mathsf{RCA}_0$ does not prove $\mathsf{RT}^1_{<\infty}$.

The first-order strength of $\mathsf{RT}^2_2$ has been studied intensively. We state the main results without proof.

- Cholak, Jockusch and Slaman (2001): $\mathsf{RCA}_0 + \mathsf I\Sigma^0_2 + \mathsf{RT}^2_2$ proves the same $\Pi^1_1$ sentences as $\mathsf{RCA}_0 + \mathsf I\Sigma^0_2$.
- Chong, Slaman and Yang (2017): $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ does not prove $\mathsf I\Sigma^0_2$. So the first-order part of $\mathsf{RT}^2_2$ lies between $\mathsf B\Sigma^0_2$ and $\mathsf I\Sigma^0_2$ in the hierarchy.
- Patey and Yokoyama (2018): $\mathsf{WKL}_0 + \mathsf{RT}^2_2$ is conservative over $\mathsf{RCA}_0$ for sentences $\forall X\, \varphi(X)$ with $\varphi \in \Pi^0_3$; in particular it proves the same $\Pi_3$ sentences of $\mathcal L_1$ as $\mathrm I\Sigma_1$. This does not contradict the proposition: since $\mathsf{RCA}_0$ does not prove $\mathsf B\Sigma^0_2$, whose instances are $\Pi_4$ sentences, $\mathsf B\Sigma^0_2$ is not equivalent over $\mathsf{RCA}_0$ to any set of $\Pi^0_3$ sentences.
- Le Houérou, Levy Patey and Yokoyama (preprint, 2024): $\mathsf{WKL}_0 + \mathsf{RT}^2_2$ is conservative over $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$ for sentences $\forall X\, \varphi(X)$ with $\varphi \in \Pi^0_4$. In a companion preprint, the same authors show that $\mathsf{RT}^2_2$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$ extended by the well-foundedness of the ordinal $\varepsilon_0$, improving earlier results of Chong, Slaman and Yang and of Kołodziejczyk and Yokoyama.

So $\mathsf{RT}^2_2$ proves no $\Pi_4$ sentence of $\mathcal L_1$ beyond $\mathrm I\Sigma_1 + \mathrm B\Sigma_2$. Whether it is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$, which would make its first-order part exactly $\mathrm I\Sigma_1 + \mathrm B\Sigma_2$, remains open; it is regarded as the main open question on the first-order part of Ramsey's theorem for pairs. Le Houérou, Levy Patey and Yokoyama recall that, by work of Fiori-Carones, Kołodziejczyk, Wong and Yokoyama, this $\Pi^1_1$-conservation is equivalent to conservation for sentences $\forall X\, \varphi(X)$ with $\varphi \in \Pi^0_5$, so the 2024 result leaves one level of the arithmetic hierarchy to be settled.

::::exercise{#ex-rt1-successor difficulty=1 objective="See why the induction on the number of colors that proves each $\mathsf{RT}^1_k$ cannot be carried out inside $\mathsf{RCA}_0$."}
Show that $\mathsf{RCA}_0$ proves $\mathsf{RT}^1_1$ and $\forall k\, (\mathsf{RT}^1_k \rightarrow \mathsf{RT}^1_{k+1})$. Explain why $\mathsf{RT}^1_{<\infty}$ does not follow.

:::solution
A coloring with one color is constant, and $\nat$ is homogeneous. Assume $\mathsf{RT}^1_k$, and let $f : \nat \to k + 1$. If $\{ z : f(z) = k \}$ is infinite, it is homogeneous. Otherwise, all its elements are less than some $m$, and $f'(z) = f(z + m)$ is a coloring with $k$ colors, which exists by $\Delta^0_1$ comprehension. An infinite homogeneous set $H'$ for $f'$ gives the infinite homogeneous set $\{ z + m : z \in H' \}$ for $f$. To conclude $\forall k\ \mathsf{RT}^1_k$, one would need induction on $k$ for the formula $\mathsf{RT}^1_k$, which begins with a universal set quantifier; $\mathsf{RCA}_0$ only provides induction for $\Sigma^0_1$ formulas. By the discussion after :ref{#prop-rt22-bsigma2}, the conclusion is indeed not provable.
:::
::::

::::exercise{#ex-bounded-color-classes difficulty=2 objective="Translate a failure of $\Sigma^0_2$ collection into a coloring whose color classes are all bounded."}
Let $\mathcal M$ be a model of $\mathsf{RCA}_0$ in which $\mathsf B\Pi^0_1$ fails. Show that there are $k \in M$ and a coloring $f : M \to k$ in $\mathcal M$ such that every color class $\{ z : f(z) = x \}$, for $x < k$, is bounded in $M$, and that $k$ is non-standard.

:::solution
By :ref{#thm-hirst}, $\mathsf{RT}^1_{<\infty}$ fails in $\mathcal M$: there are $k$ and $f : M \to k$ in $\mathcal M$ without infinite homogeneous set in $\mathcal M$. If some color class were unbounded, it would exist by $\Delta^0_1$ comprehension and be an infinite homogeneous set. So every color class is bounded. If $k$ were standard, $\mathsf{RT}^1_k$ would hold in $\mathcal M$ by :ref{#prop-rt-basic}. So $k$ is non-standard: $M$ is the union of $k$ bounded sets, but no single bound works for all of them.
:::
::::

## Notes and references

Combinatorial principles that are true but unprovable in PA, such as the Paris–Harrington principle, are studied in the track on models of arithmetic (:ref{to="independence/paris-harrington"}).

Hirst proved the equivalence of :ref{#thm-hirst} and :ref{#prop-rt22-bsigma2} in his thesis (1987). The proof of :ref{#thm-hirst} given here is close to Hirschfeldt's (*Slicing the Truth*, Theorem 6.81, Section 6.8); Dzhafarov and Mummert treat the theorem in Section 6.5, and Cholak, Jockusch and Slaman strengthened :ref{#prop-rt22-bsigma2} to stable colorings (Hirschfeldt, Theorem 6.82). The relation between Ramsey's theorem for pairs and induction was initiated by Cholak, Jockusch and Slaman, and remains an active topic.

- J. L. Hirst, *Combinatorics in Subsystems of Second Order Arithmetic*, PhD thesis, Pennsylvania State University, 1987.
- P. A. Cholak, C. G. Jockusch and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- C. T. Chong, T. A. Slaman and Y. Yang, *The inductive strength of Ramsey's theorem for pairs*, Advances in Mathematics 308 (2017), 121–141.
- L. Patey and K. Yokoyama, *The proof-theoretic strength of Ramsey's theorem for pairs and two colors*, Advances in Mathematics 330 (2018), 1034–1070.
- Q. Le Houérou, L. Levy Patey and K. Yokoyama, *Π⁰₄ conservation of Ramsey's theorem for pairs*, preprint, arXiv:2404.18974, 2024.
- Q. Le Houérou, L. Levy Patey and K. Yokoyama, *Conservation of Ramsey's theorem for pairs and well-foundedness*, preprint, arXiv:2402.11616, 2024.
- M. Fiori-Carones, L. A. Kołodziejczyk, T. L. Wong and K. Yokoyama, *An isomorphism theorem for models of weak König's lemma without primitive recursion*, Journal of the European Mathematical Society, published online 2024, arXiv:2112.10876.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 6.8.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 6.5.

:::::exercises
::::exercise{#ex-rt1-cut difficulty=1 objective="See the numbers of colors for which the pigeonhole principle holds as a cut, and deduce that this property is not $\Sigma^0_1$-definable."}
Let $\mathcal M = (M, \mathcal S)$ be a model of $\mathsf{RCA}_0$, and $I$ the set of $k \in M$ such that $\mathcal M \models \mathsf{RT}^1_k$. Show that $I$ contains $0$, is closed under successor, and is an initial segment of $M$. Show that $I = M$ if and only if $\mathcal M \models \mathsf B\Sigma^0_2$. Deduce that if $\mathcal M \not\models \mathsf B\Sigma^0_2$, the property "$\mathsf{RT}^1_k$" of $k$ is not equivalent in $\mathcal M$ to any $\Sigma^0_1$ or $\Pi^0_1$ formula with parameters.

:::solution
There is no function from $M$ to $0$, so $\mathsf{RT}^1_0$ holds vacuously and $0 \in I$. If $k \in I$, then $k + 1 \in I$ by :ref{#ex-rt1-successor}, whose proof takes place in $\mathsf{RCA}_0$, hence in $\mathcal M$. If $k' \leq k \in I$, a coloring $f : M \to k'$ in $\mathcal M$ is also a coloring with $k$ colors, so it has an infinite homogeneous set in $\mathcal M$: $k' \in I$. By definition, $I = M$ if and only if $\mathcal M \models \mathsf{RT}^1_{<\infty}$, that is, by :ref{#thm-hirst}, if and only if $\mathcal M \models \mathsf B\Sigma^0_2$.

If $\mathcal M \not\models \mathsf B\Sigma^0_2$, then $I$ contains $0$, is closed under successor, and is not all of $M$. A $\Sigma^0_1$ formula $\psi(k)$ defining $I$ in $\mathcal M$ would violate $\mathsf I\Sigma^0_1$; a $\Pi^0_1$ formula would violate $\mathsf I\Pi^0_1$, which holds in $\mathcal M$ by :ref{#thm-isigma-ipi}. The formula $\mathsf{RT}^1_k$ begins with a universal set quantifier, to which the induction of $\mathsf{RCA}_0$ does not apply.
:::
::::

::::exercise{#ex-uniform-limits difficulty=2 objective="Prove that $\Sigma^0_2$ collection is equivalent to the uniform stabilization of finitely many convergent sequences." lessons="collection-induction"}
Consider the following statement: for every $a$ and every function $f : \nat \times \nat \to \nat$ such that $\lim_s f(x, s)$ exists for every $x < a$ (that is, $\exists t\ \forall s \geq t\ f(x, s) = f(x, t)$), there is $s_0$ such that $f(x, s) = f(x, s_0)$ for all $x < a$ and $s \geq s_0$. Show that it is equivalent to $\mathsf B\Sigma^0_2$ over $\mathsf{RCA}_0$.

:::solution
By :ref{#ex-bsigma-bpi}, we may work with $\mathsf B\Pi^0_1$. Since $f$ is total, $f(x, s) = f(x, t)$ is equivalent to a $\Pi^0_1$ formula, as in :ref{#ex-overspill-limits}.

*$\mathsf B\Pi^0_1$ implies the statement.* The formula $\forall s\ (s < t \vee f(x, s) = f(x, t))$ is $\Pi^0_1$, and every $x < a$ has some $t$ satisfying it. By $\mathsf B\Pi^0_1$ there is $b$ such that every $x < a$ has such a $t < b$. Let $s_0 = b$. For $x < a$ and $s \geq s_0$, both $s$ and $s_0$ are at least $t$, so $f(x, s) = f(x, t) = f(x, s_0)$.

*The statement implies $\mathsf B\Pi^0_1$.* Let $\varphi(x, y) \equiv \forall z\ \theta(x, y, z)$ with $\theta$ bounded, and suppose $\forall x < a\ \exists y\ \varphi(x, y)$. Let $f(x, s)$ be the least $y < s$ such that $\forall z < s\ \theta(x, y, z)$, and $s$ if there is none. Its graph is defined by a bounded formula, so $f$ exists by $\Delta^0_1$ comprehension. Fix $x < a$. By $\mathsf L\Pi^0_1$ (:ref{#prop-least-number}), there is a least $y_0$ with $\varphi(x, y_0)$. Every $y < y_0$ has some $z$ with $\neg \theta(x, y, z)$, and by $\mathsf B\Sigma^0_1$ there is $z_0$ such that every $y < y_0$ has such a $z < z_0$. For $s > \max(y_0, z_0)$, $y_0 < s$ satisfies $\forall z < s\ \theta(x, y_0, z)$, and no $y < y_0$ does, so $f(x, s) = y_0$. Hence $\lim_s f(x, s)$ exists and equals $y_0$. The statement gives $s_0$ with $f(x, s) = f(x, s_0)$ for all $x < a$ and $s \geq s_0$; so $f(x, s_0)$ is the limit $y_0$ for each $x < a$. Since $f(x, s_0) \leq s_0$ by definition, $\forall x < a\ \exists y < s_0 + 1\ \varphi(x, y)$.
:::
::::

::::exercise{#ex-fuf difficulty=2 objective="Prove that $\Sigma^0_2$ collection is equivalent to the statement that a finite union of finite sets is finite."}
A **sequence of finite sets** is a set $F$ whose columns $F_i = \{ x : \langle i, x \rangle \in F \}$ are all bounded. The principle $\mathsf{FUF}$ states: if $F$ is a sequence of finite sets and $F_i = \emptyset$ for every $i \geq m$, for some $m$, then $\bigcup_i F_i = \{ x : \exists i\ \langle i, x \rangle \in F \}$ is bounded. Show that $\mathsf{FUF}$ is equivalent to $\mathsf B\Sigma^0_2$ over $\mathsf{RCA}_0$.

:::solution
($\mathsf B\Sigma^0_2 \Rightarrow \mathsf{FUF}$) We use $\mathsf B\Pi^0_1$ (:ref{#ex-bsigma-bpi}). Every $i < m$ satisfies $\exists b\ \forall x\ (\langle i, x \rangle \in F \rightarrow x < b)$, and the formula after $\exists b$ is $\Pi^0_1$. By $\mathsf B\Pi^0_1$, there is $c$ such that every $i < m$ has such a $b < c$; then every element of $F_i$, $i < m$, is less than $c$. Since $F_i$ is empty for $i \geq m$, $\bigcup_i F_i$ is bounded by $c$.

($\mathsf{FUF} \Rightarrow \mathsf B\Sigma^0_2$) We prove $\mathsf{RT}^1_{<\infty}$ and apply :ref{#thm-hirst}. Let $f : \nat \to k$, and suppose that it has no infinite homogeneous set. Then every color class $\{ z : f(z) = i \}$ is bounded: otherwise it would exist by $\Delta^0_1$ comprehension and be an infinite homogeneous set. Let $F = \{ \langle i, z \rangle : i < k \wedge f(z) = i \}$, which exists by $\Delta^0_1$ comprehension. Its columns are the color classes for $i < k$ and are empty for $i \geq k$, so $\mathsf{FUF}$ gives a bound $b$ on $\bigcup_i F_i$. But $f(b) = i$ for some $i < k$, so $b \in F_i$: a contradiction.

Adapted from Dzhafarov and Mummert, Proposition 6.5.4.
:::
::::

::::exercise{#ex-stcoh difficulty=2 objective="Show that requiring a uniform threshold in the definition of cohesiveness forces $\Sigma^0_2$ collection."}
A sequence of sets $\vec R = (R_i)$ is coded by a set whose $i$-th column is $R_i$. The **strong cohesiveness principle** $\mathsf{StCOH}$ states: for every sequence $\vec R$ there is an infinite set $S$ such that, for every $z$, there is $w$ with
$$
\forall i < z\ \bigl(\forall x > w\ (x \in S \rightarrow x \in R_i) \vee \forall x > w\ (x \in S \rightarrow x \notin R_i)\bigr).
$$
It differs from cohesiveness in that one threshold $w$ works for all $i < z$. Show that $\mathsf{RCA}_0 + \mathsf{StCOH}$ proves $\mathsf B\Sigma^0_2$.

:::solution
We prove $\mathsf{RT}^1_{<\infty}$ and apply :ref{#thm-hirst}. Let $f : \nat \to z$, and let $R_i = \{ x : f(x) = i \}$; the sequence exists by $\Delta^0_1$ comprehension. Let $S$ be given by $\mathsf{StCOH}$, and $w$ the threshold for this $z$. Since $S$ is infinite, it has an element $x_0 > w$; let $i = f(x_0) < z$. Then $x_0 \in S \cap R_i$ and $x_0 > w$, so the second alternative fails for $i$, and the first holds: every $x \in S$ with $x > w$ belongs to $R_i$. The set $\{ x \in S : x > w \}$ exists by $\Delta^0_1$ comprehension, is infinite, and $f$ takes the value $i$ on it: it is homogeneous.

The non-uniform principle $\mathsf{COH}$, where $w$ may depend on $i$, does not imply $\mathsf B\Sigma^0_2$ over $\mathsf{RCA}_0$: it is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$ (Cholak, Jockusch and Slaman; an exercise of the lesson on Harrington's theorem). Adapted from Dzhafarov and Mummert, Proposition 6.5.6, due to Hirschfeldt and Shore.
:::
::::
:::::
