---
title: A fast-growing hierarchy
summary: The hierarchy of functions F_k, defined by iteration; its formalization in IΣ₁ by finite computations; IΣ₁ proves the totality of each F_k, and IΣ₂ proves the totality of all of them; growth of the hierarchy in the argument and in the index.
duration: 30
prerequisites: [truth-and-provability/provably-total, truth-and-provability/ackermann-isigma, fragments-of-arithmetic/coding]
---

The course on truth and provability proved that $\mathrm I\Sigma_1$ proves the totality of every primitive recursive function, and stated the converse (:ref{#thm-pmt}), which this course proves. This course proves such unprovability results by the method of Paris and Kirby: to show that a theory $T$ does not prove that a function $f$ is total, one finds, inside a model of $T$, a cut that is again a model of $T$ and is not closed under $f$. The cut is caught in an interval $[a, b]$ that is large in a combinatorial sense.

The first application concerns $\mathrm I\Sigma_1$, and the large intervals are those of the form $[a, F_\nu(a)]$ for a hierarchy of fast-growing functions $F_k$ and a non-standard index $\nu$. This lesson defines the hierarchy, formalizes it in $\mathrm I\Sigma_1$, and shows that $\mathrm I\Sigma_1$ proves the totality of each $F_k$ separately; the next lesson builds the cuts. The track assumes first-order logic; compactness provides the countable non-standard models used throughout.

## The hierarchy

:::definition{#def-fgh}
The functions $F_k : \nat \to \nat$, for $k \in \nat$, are defined by
$$
F_0(x) = x + 1, \qquad F_{k+1}(x) = F_k^{(x)}(x + 1),
$$
where $g^{(i)}$ is the $i$-th iterate of $g$: $g^{(0)}(y) = y$ and $g^{(i+1)}(y) = g(g^{(i)}(y))$.
:::

Each step iterates the previous function a number of times equal to the argument. This is the hierarchy of Hájek and Pudlák (a finite part of the Schwichtenberg–Wainer hierarchy, II.3.22); Wong's Lecture 5 uses the variant $F_{k+1}(x) = F_k^{(x+1)}(x)$, which grows at the same rate. Our choice is dictated by lesson 8, where $F_k(x)$ turns out to be exactly the least $y$ such that $[x, y)$ is $\omega^k$-large.

:::example{#ex-fgh-values}
1. $F_1(x) = F_0^{(x)}(x + 1) = 2x + 1$.
2. By induction on $i$, $F_1^{(i)}(y) = 2^i (y + 1) - 1$; hence $F_2(x) = F_1^{(x)}(x + 1) = 2^x (x + 2) - 1$. For instance $F_2(1) = 5$, $F_2(2) = 15$, $F_2(3) = 39$.
3. $F_3(1) = F_2(2) = 15$, and $F_3(2) = F_2(F_2(3)) = F_2(39) = 2^{39} \cdot 41 - 1$. The function $F_3$ grows like a tower of exponentials of height $x$.
4. $F_k(0) = F_{k-1}^{(0)}(1) = 1$ for every $k \geq 1$. The hierarchy does not separate its members at $0$.
:::

Each $F_k$ is primitive recursive: $F_{k+1}(x) = G(x, x + 1)$, where $G(0, y) = y$ and $G(i + 1, y) = F_k(G(i, y))$ is a primitive recursion.

## Formalization in IΣ₁

Inside a model, $F_k(x)$ must be defined for non-standard $k$ as well. We use finite computations, as for the Ackermann function in :ref{to="truth-and-provability/ackermann-isigma"}.

:::fact{#fact-fgh-formal}
There is a $\Sigma_1$ formula $\mathrm{It}(k, i, x, y)$, read "$F_k^{(i)}(x) = y$", such that $\mathrm I\Sigma_1$ proves:

1. (**functionality**) $\mathrm{It}(k, i, x, y) \wedge \mathrm{It}(k, i, x, y') \rightarrow y = y'$;
2. (**iteration**) $\mathrm{It}(k, 0, x, y) \leftrightarrow y = x$, and $\mathrm{It}(k, i + 1, x, z) \leftrightarrow \exists y\ \big(\mathrm{It}(k, i, x, y) \wedge \mathrm{It}(k, 1, y, z)\big)$;
3. (**the hierarchy**) $\mathrm{It}(0, 1, x, y) \leftrightarrow y = x + 1$, and $\mathrm{It}(k + 1, 1, x, y) \leftrightarrow \mathrm{It}(k, x, x + 1, y)$.

In $\nat$, $\mathrm{It}(k, i, x, y)$ holds if and only if $F_k^{(i)}(x) = y$.
:::

The formula says that some **computation** contains $\langle k, i, x, y \rangle$: a coded finite set of quadruples each justified by the clauses 2–3 from other elements. Justification is bounded, so the formula is $\Sigma_1$; the proofs are those for the Ackermann function (:ref{#prop-ack-computations}). We write $F_k(x) = y$ for $\mathrm{It}(k, 1, x, y)$, and $F_k(x){\downarrow}$ for $\exists y\ F_k(x) = y$.

:::lemma{#lem-fgh-isigma1}
$\mathrm I\Sigma_1$ proves:

1. if $F_k(y) = z$, then $z > y$; if $\mathrm{It}(k, i, x, y)$, then $y \geq x + i$;
2. if $\mathrm{It}(k, i, x, y)$, then there is a coded sequence $t$ of length $i + 1$ with $\mathrm{It}(k, j, x, (t)_j)$ for every $j \leq i$, and this sequence is strictly increasing.

Moreover, for every standard $k$, $\mathrm I\Sigma_1 \vdash \forall x\ F_k(x){\downarrow}$.
:::

:::proof{of=lem-fgh-isigma1}
1. Let $P(k) \equiv \forall y\ \forall z\ \big(F_k(y) = z \rightarrow z > y\big)$, a $\Pi_1$ formula. We prove $\forall k\ P(k)$ by $\Pi_1$ induction, available in $\mathrm I\Sigma_1$ by :ref{#thm-fo-isigma-ipi}. $P(0)$ holds by item 3 of :ref{#fact-fgh-formal}. Assume $P(k)$. By $\Pi_1$ induction on $i$, $\forall x\ \forall w\ (\mathrm{It}(k, i, x, w) \rightarrow w \geq x + i)$: the case $i = 0$ is item 2, and if $\mathrm{It}(k, i + 1, x, w)$, item 2 gives $v$ with $\mathrm{It}(k, i, x, v)$ and $F_k(v) = w$, so $w > v \geq x + i$ by $P(k)$. Now if $F_{k+1}(y) = z$, then $\mathrm{It}(k, y, y + 1, z)$, so $z \geq 2y + 1 > y$. This is $P(k + 1)$, and also proves the second claim.

2. Fix $k, i, x, y$ with $\mathrm{It}(k, i, x, y)$. First, every rank $j \leq i$ has an iterate: apply $\Sigma_1$ induction to $\rho(m) \equiv m \leq i \rightarrow \exists w\ \mathrm{It}(k, i - m, x, w)$. $\rho(0)$ is the hypothesis, and if $w$ witnesses $\rho(m)$ with $m + 1 \leq i$, the implication from left to right in item 2 of :ref{#fact-fgh-formal}, applied to the rank $i - m = (i - m - 1) + 1$, gives an iterate of rank $i - m - 1$. Then apply $\Sigma_1$ induction to
$$
\chi(j) \equiv j \leq i \rightarrow \exists t\ \big(\mathrm{Seq}(t, j + 1) \wedge \forall j' \leq j\ \mathrm{It}(k, j', x, (t)_{j'})\big),
$$
which is $\Sigma_1$ in $\mathrm I\Sigma_1$ by Parsons' lemma (:ref{#lem-fo-collection-closure}). For $j = 0$ take the sequence of length $1$ with entry $x$. For the step, the iterate of rank $j + 1 \leq i$ exists, and concatenation (:ref{#prop-seq-basic}) extends $t$. The sequence is strictly increasing by item 1, since consecutive entries satisfy $F_k((t)_j) = (t)_{j+1}$, by item 2 of :ref{#fact-fgh-formal} and functionality.

*Totality.* By induction on $k$ in the metatheory. $F_0$ is total by item 3. If $\mathrm I\Sigma_1 \vdash \forall y\ F_k(y){\downarrow}$, then, for fixed $x$, $\Sigma_1$ induction on $i$ for $\exists y\ \mathrm{It}(k, i, x, y)$, with item 2, gives $\forall i\ \forall x\ \exists y\ \mathrm{It}(k, i, x, y)$, and item 3 gives $\forall x\ F_{k+1}(x){\downarrow}$.
:::

The induction in the totality proof is in the metatheory, one proof for each $k$. A uniform proof would be an induction on $k$ for the $\Pi_2$ formula $\forall x\ F_k(x){\downarrow}$: $\mathrm I\Sigma_2$ can carry it out (exercise), and lesson 3 shows that $\mathrm I\Sigma_1$ cannot.

:::quiz[the formalization of the hierarchy]
In the proof of :ref{#lem-fgh-isigma1}, item 1, why is the induction carried out on the formula $P(k)$, which says that every *existing* value $F_k(y)$ is above $y$, rather than on the statement that $F_k$ is total and increasing?

- [x] $P(k)$ is $\Pi_1$, so $\mathrm I\Sigma_1$ can induct on it; the statement "$F_k$ is total" is $\Pi_2$, and $\Pi_2$ induction is not available in $\mathrm I\Sigma_1$.
- [ ] Because $F_k$ is not total in models of $\mathrm I\Sigma_1$ for standard $k$.

  For standard $k$ it is total, by the last part of the lemma; the issue is the uniformity in $k$.
- [ ] Because $\Pi_1$ formulas are preserved in cuts.

  This is true but irrelevant here: the induction takes place in a single model.
:::

## Growth in the standard model

In $\nat$, the functions $F_k$ increase in the argument and in the index. These facts are used in lessons 3 and 8; inside a model of $\mathrm I\Sigma_1$ we use only :ref{#lem-fgh-isigma1}.

:::lemma{#lem-fgh-monotone}
For all $k, x$ in $\nat$:

1. $F_k$ is strictly increasing, and $F_k^{(i)}(y) \geq y + i$;
2. $F_k(x) \leq F_{k+1}(x)$, and $F_{k+1}(x) \geq F_k(x) + x$ for $x \geq 1$.
:::

:::proof{of=lem-fgh-monotone}
1. By induction on $k$. For $F_0$ it is clear. If $F_k$ is strictly increasing with $F_k(y) > y$, its iterates are increasing in $y$ and $F_k^{(i)}(y) \geq y + i$. So $F_{k+1}(x + 1) = F_k^{(x)}(F_k(x + 2)) > F_k^{(x)}(x + 1) = F_{k+1}(x)$, since $F_k(x + 2) > x + 1$, and $F_{k+1}(x) \geq 2x + 1 > x$.
2. For $x = 0$, both sides equal $1$ (:ref{#ex-fgh-values}). For $x \geq 1$, $F_{k+1}(x) = F_k^{(x-1)}(F_k(x + 1)) \geq F_k(x + 1) + x - 1 \geq F_k(x) + x$, by item 1.
:::

## Exercises

::::exercise{difficulty=2}
Show that $\mathrm I\Sigma_2$ proves $\forall k\ \forall x\ F_k(x){\downarrow}$.

:::solution
Apply $\Pi_2$ induction, available in $\mathrm I\Sigma_2$ by :ref{#thm-fo-isigma-ipi}, to $\tau(k) \equiv \forall x\ F_k(x){\downarrow}$. $\tau(0)$ holds by item 3 of :ref{#fact-fgh-formal}. Assume $\tau(k)$. For fixed $x$, $\Sigma_1$ induction on $i$ for $\exists y\ \mathrm{It}(k, i, x, y)$, with the parameters $k, x$ and the hypothesis $\tau(k)$, gives $\forall i\ \exists y\ \mathrm{It}(k, i, x, y)$: the step uses item 2. With $i = x$ and the point $x + 1$, item 3 gives $F_{k+1}(x){\downarrow}$. So $\tau(k + 1)$.
:::
::::

## Notes and references

The hierarchy is the finite part of the hierarchy of Hájek and Pudlák (Chapter II, 3.22), a variant of the hierarchy of Schwichtenberg and Wainer; Wong's Lecture 5 uses the closely related functions $F_{k+1}(x) = F_k^{(x+1)}(x)$, after Grzegorczyk (1953). The formalization by finite computations is that of the Ackermann function in :ref{to="truth-and-provability/ackermann-isigma"}; Hájek and Pudlák define the whole hierarchy $f_\alpha$, $\alpha < \varepsilon_0$, by derivations (II.3.24–3.29). The unprovability in $\mathrm I\Sigma_1$ of the totality of all the $F_k$ is due to Kirby and Paris (1977); it is proved in lesson 3.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- A. Grzegorczyk, *Some classes of recursive functions*, Rozprawy Matematyczne 4 (1953), 1–46.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter II, Section 3(d).
