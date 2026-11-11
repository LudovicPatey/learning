---
title: The pigeonhole principle and Σ⁰₂ collection
summary: The infinite pigeonhole principle for arbitrarily many colors is equivalent to Σ⁰₂ collection over RCA₀ (Hirst); Ramsey's theorem for pairs implies it; first-order consequences of combinatorial principles.
duration: 30
prerequisites: [induction-collection, ramsey-theorem/jockusch]
---

$\mathsf{RCA}_0$ proves the infinite pigeonhole principle $\mathsf{RT}^1_k$ for every standard number $k$ of colors (:ref{#prop-rt-basic}): the proof is a case analysis on finitely many colors. The statement $\mathsf{RT}^1_{<\infty}$, "for every $k$, every coloring $f : \nat \to k$ has an infinite homogeneous set", quantifies over $k$ inside the theory. In a non-standard model, $k$ may be non-standard, and the case analysis is no longer available. Hirst showed that $\mathsf{RT}^1_{<\infty}$ is exactly $\Sigma^0_2$ collection. A combinatorial principle about sets thus has a purely arithmetic content, and so does every principle that implies it, such as Ramsey's theorem for pairs.

## Hirst's theorem

By the first exercise of the previous lesson, $\mathsf B\Sigma^0_2$ is equivalent to $\mathsf B\Pi^0_1$ over $\mathsf I\Delta^0_0$. We use the second form.

:::theorem[Hirst]{#thm-hirst}
Over $\mathsf{RCA}_0$, $\mathsf{RT}^1_{<\infty}$ is equivalent to $\mathsf B\Pi^0_1$, hence to $\mathsf B\Sigma^0_2$.
:::

:::proof{of=thm-hirst}
Recall that $\mathsf{RCA}_0$ proves $\mathsf I\Sigma^0_1$, hence $\mathsf B\Sigma^0_1$ by :ref{#thm-induction-collection}.

($\mathsf B\Pi^0_1 \Rightarrow \mathsf{RT}^1_{<\infty}$) Let $f : \nat \to k$. If there is $x < k$ such that $\forall y\ \exists z > y\ f(z) = x$, the set $\{ z : f(z) = x \}$ exists by $\Delta^0_1$ comprehension, is infinite, and is homogeneous. Otherwise, every $x < k$ satisfies $\exists y\ \forall z > y\ f(z) \neq x$, a $\Pi^0_1$ formula of $x$ and $y$. By $\mathsf B\Pi^0_1$, there is $p$ such that every $x < k$ has some $y < p$ with $\forall z > y\ f(z) \neq x$. Let $x = f(p)$; then $p > y$ for the corresponding $y$, and $f(p) \neq x$: a contradiction.

($\mathsf{RT}^1_{<\infty} \Rightarrow \mathsf B\Pi^0_1$) Let $\varphi(x, y) \equiv \forall z\ \theta(x, y, z)$ with $\theta$ bounded, and suppose $\forall x < k\ \exists y\ \varphi(x, y)$; we may assume $k \geq 1$. For every $t$, let $f(t)$ be the least $n$ such that
$$
\forall x < k\ \exists y < n\ \forall z < t\ \theta(x, y, z).
$$
It exists: every $x < k$ has some $y$ with $\forall z < t\ \theta(x, y, z)$, a bounded condition, so $\mathsf B\Sigma^0_1$ gives a common bound, and the least one exists by the least number principle for bounded formulas. The graph of $f$ is defined by a bounded formula, so $f$ exists by $\Delta^0_1$ comprehension. The condition becomes stronger as $t$ increases, so $f$ is non-decreasing, and $f(t) \geq 1$ since $k \geq 1$.

*Case 1: $f$ is bounded*, say by $\ell$. By $\mathsf{RT}^1_\ell$, there are an infinite set $H$ and $c < \ell$ with $f(t) = c$ for every $t \in H$. We claim $\forall x < k\ \exists y < c\ \varphi(x, y)$, which is the conclusion of $\mathsf B\Pi^0_1$. Otherwise, some $x_0 < k$ satisfies $\forall y < c\ \exists z\ \neg \theta(x_0, y, z)$, and $\mathsf B\Sigma^0_1$ gives $z_0$ with $\forall y < c\ \exists z < z_0\ \neg \theta(x_0, y, z)$. Taking $t \in H$ with $t > z_0$, the definition of $f(t) = c$ gives $y < c$ with $\forall z < t\ \theta(x_0, y, z)$: a contradiction.

*Case 2: $f$ is unbounded.* Since $f(t) - 1$ does not satisfy the condition defining $f(t)$, there is $x < k$ such that $\forall y < f(t) - 1\ \exists z < t\ \neg \theta(x, y, z)$. Let $g(t)$ be the least such $x$; $g : \nat \to k$ exists by $\Delta^0_1$ comprehension. By $\mathsf{RT}^1_k$, there are an infinite set $S$ and $x_0 < k$ with $g(t) = x_0$ for $t \in S$. Let $y$ be any number. Since $f$ is unbounded and non-decreasing, and $S$ is infinite, there is $t \in S$ with $f(t) - 1 > y$, so $\exists z < t\ \neg \theta(x_0, y, z)$. Hence $\forall y\ \neg \varphi(x_0, y)$, contradicting the hypothesis. So case 2 does not occur.
:::

The function $f$ measures, at stage $t$, how far one must search to find witnesses that look correct up to $t$. Collection says that this search stays bounded; the pigeonhole principle, applied twice, turns an unbounded search into a single color $x_0$ whose witnesses are all eventually refuted.

:::quiz[Hirst's theorem]
In the direction $\mathsf{RT}^1_{<\infty} \Rightarrow \mathsf B\Pi^0_1$, where is the pigeonhole principle used for a non-standard number of colors?

- [x] Twice: in case 1 with $\ell$ colors, where $\ell$ bounds $f$, and in case 2 with $k$ colors, where $k$ is the bound in the instance of collection; both may be non-standard.
- [ ] Only in case 2.

  Case 1 also applies the principle, to $f$ with $\ell$ colors.
- [ ] Nowhere: the colors are bounded by $k$.

  $k$ is an arbitrary number of the model, possibly non-standard; this is the whole point.

---

Why can the theorem not be proved by induction on $k$, using the proofs of $\mathsf{RT}^1_k$ for each standard $k$?

- [x] Because "every coloring $f : \nat \to k$ has an infinite homogeneous set" quantifies over sets; it is not a $\Sigma^0_1$ formula of $k$, and $\mathsf{RCA}_0$ does not provide induction for it.
- [ ] Because $\mathsf{RT}^1_{k+1}$ does not follow from $\mathsf{RT}^1_k$.

  It does, over $\mathsf{RCA}_0$, as an exercise below shows.
- [ ] Because $\mathsf{RCA}_0$ has no induction.

  It has $\Sigma^0_1$ induction, which does not apply to this formula.
:::

## Ramsey's theorem for pairs

:::proposition{#prop-rt22-bsigma2}
$\mathsf{RCA}_0 + \mathsf{RT}^2_2$ proves $\mathsf{RT}^1_{<\infty}$, hence $\mathsf B\Sigma^0_2$.
:::

:::proof{of=prop-rt22-bsigma2}
Let $f : \nat \to k$. Define $g : [\nat]^2 \to 2$ by $g(\{ x, y \}) = 1$ if $f(x) = f(y)$, and $0$ otherwise; it exists by $\Delta^0_1$ comprehension. Let $H$ be an infinite homogeneous set for $g$. If its color is $1$, then $f$ is constant on $H$, and $H$ is homogeneous for $f$. If its color is $0$, then $f$ is injective on $H$; the first $k + 1$ elements of $H$ form a finite set, which exists in $\mathsf{RCA}_0$, on which $f$ is an injection into $k$. This contradicts the finite pigeonhole principle, which $\mathsf{RCA}_0$ proves by $\Pi^0_1$ induction on $k$. By :ref{#thm-hirst}, $\mathsf B\Sigma^0_2$ follows.
:::

Every ω-model satisfies $\mathsf B\Sigma^0_2$, since its first-order part is $\nat$. The proposition is therefore invisible in ω-models: it says something about the non-standard models of $\mathsf{RT}^2_2$. By :ref{#thm-collection-induction}, $\mathsf B\Sigma^0_2$ implies $\mathsf I\Sigma^0_1$, which $\mathsf{RCA}_0$ already has; but $\mathsf{RCA}_0$ does not prove $\mathsf B\Sigma^0_2$. Indeed, Paris and Kirby built a model of $\mathrm I\Sigma_1$ in which $\Sigma_2$ collection fails, and the next lesson shows that every countable model of $\mathrm I\Sigma_1$ is the first-order part of a model of $\mathsf{RCA}_0$. Hence $\mathsf{RCA}_0$ does not prove $\mathsf{RT}^1_{<\infty}$.

The first-order strength of $\mathsf{RT}^2_2$ has been studied intensively. We state the main results without proof.

- Cholak, Jockusch and Slaman (2001): $\mathsf{RCA}_0 + \mathsf I\Sigma^0_2 + \mathsf{RT}^2_2$ proves the same $\Pi^1_1$ sentences as $\mathsf{RCA}_0 + \mathsf I\Sigma^0_2$.
- Chong, Slaman and Yang (2017): $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ does not prove $\mathsf I\Sigma^0_2$.
- Patey and Yokoyama (2018): $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ proves the same $\Pi^0_3$ sentences as $\mathsf{RCA}_0$. This does not contradict the proposition: $\mathsf B\Sigma^0_2$ is not equivalent to a $\Pi^0_3$ sentence.

Whether $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ proves any arithmetic sentence not provable in $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$ is a central question of the area.

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{RCA}_0$ proves $\mathsf{RT}^1_1$ and $\forall k\, (\mathsf{RT}^1_k \rightarrow \mathsf{RT}^1_{k+1})$. Explain why $\mathsf{RT}^1_{<\infty}$ does not follow.

:::solution
A coloring with one color is constant, and $\nat$ is homogeneous. Assume $\mathsf{RT}^1_k$, and let $f : \nat \to k + 1$. If $\{ z : f(z) = k \}$ is infinite, it is homogeneous. Otherwise, it is bounded by some $m$, and $f'(z) = f(z + m)$ is a coloring with $k$ colors, which exists by $\Delta^0_1$ comprehension. An infinite homogeneous set $H'$ for $f'$ gives the infinite homogeneous set $\{ z + m : z \in H' \}$ for $f$. To conclude $\forall k\ \mathsf{RT}^1_k$, one would need induction on $k$ for the formula $\mathsf{RT}^1_k$, which begins with a universal set quantifier; $\mathsf{RCA}_0$ only provides induction for $\Sigma^0_1$ formulas. By the discussion after :ref{#prop-rt22-bsigma2}, the conclusion is indeed not provable.
:::
::::

::::exercise{difficulty=2}
Let $\mathcal M$ be a model of $\mathsf{RCA}_0$ in which $\mathsf B\Pi^0_1$ fails. Show that there are $k \in M$ and a coloring $f : M \to k$ in $\mathcal M$ such that every color class $\{ z : f(z) = x \}$, for $x < k$, is bounded in $M$, and that $k$ is non-standard.

:::solution
By :ref{#thm-hirst}, $\mathsf{RT}^1_{<\infty}$ fails in $\mathcal M$: there are $k$ and $f : M \to k$ in $\mathcal M$ without infinite homogeneous set in $\mathcal M$. If some color class were unbounded, it would exist by $\Delta^0_1$ comprehension and be an infinite homogeneous set. So every color class is bounded. If $k$ were standard, $\mathsf{RT}^1_k$ would hold in $\mathcal M$ by :ref{#prop-rt-basic}. So $k$ is non-standard: $M$ is the union of $k$ bounded sets, but no single bound works for all of them.
:::
::::

## Notes and references

Hirst proved the equivalence in his thesis (1987). The relation between Ramsey's theorem for pairs and induction was initiated by Cholak, Jockusch and Slaman, and remains an active topic.

- J. L. Hirst, *Combinatorics in Subsystems of Second Order Arithmetic*, PhD thesis, Pennsylvania State University, 1987.
- P. A. Cholak, C. G. Jockusch and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- C. T. Chong, T. A. Slaman and Y. Yang, *The inductive strength of Ramsey's theorem for pairs*, Advances in Mathematics 308 (2017), 121–141.
- L. Patey and K. Yokoyama, *The proof-theoretic strength of Ramsey's theorem for pairs and two colors*, Advances in Mathematics 330 (2018), 1034–1070.
