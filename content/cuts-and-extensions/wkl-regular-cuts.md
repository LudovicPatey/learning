---
title: The Kirby–Paris characterization and regular cuts
summary: A proper cut is semiregular if and only if it is closed under multiplication and its coded subsets form a model of WKL₀ (Kirby and Paris); regular cuts and the pigeonhole principle; every regular cut is semiregular.
duration: 25
prerequisites: [semiregular-cuts]
---

The previous lesson showed that a semiregular cut, with its coded subsets, satisfies $\Sigma^0_1$ induction (:ref{#thm-semireg-isigma1}). Together with the results of the first two lessons, this makes $(I, \mathrm{Cod}(M/I))$ a model of $\mathsf{WKL}_0$. This lesson proves the converse, due to Kirby and Paris: semiregularity is exactly what a cut closed under multiplication needs for its coded subsets to form a model of $\mathsf{WKL}_0$. The proof of the converse is by contradiction: a coded function with values cofinal in the cut gives an increasing sequence of codes, indexed by a $\Sigma^0_1$ formula, that would exceed a fixed bound. The lesson ends with the stronger notion of a regular cut, a pigeonhole principle for coded colorings of the cut, and proves that regular cuts are semiregular.

Throughout, $M$ is a model of $\mathrm I\Delta_0 + \mathrm{exp}$.

## The Kirby–Paris characterization

The structure $(I, \mathrm{Cod}(M/I))$ is a natural candidate for a model of $\mathsf{WKL}_0$, the system $\mathsf{RCA}_0$ of :ref{#def-rca0} together with weak König's lemma, stated as: every unbounded binary tree has an unbounded branch. Comprehension comes from :ref{#cor-cod-delta1-ca}, and weak König's lemma from :ref{#thm-scott-wkl-cut} if $I$ is exponential. Semiregularity is exactly what is missing.

:::theorem[Kirby, Paris]{#thm-kirby-paris-wkl}
Let $I$ be a proper cut of $M$. Then $I$ is semiregular if and only if $I$ is closed under multiplication and $(I, \mathrm{Cod}(M/I)) \models \mathsf{WKL}_0$.
:::

:::proof{of=thm-kirby-paris-wkl}
($\Rightarrow$) By :ref{#lem-semireg-closed}, $I$ is closed under addition and multiplication; it satisfies the basic axioms of arithmetic, since it is a model of $\mathrm I\Delta_0$ (:ref{#lem-cut-model}). $\Sigma^0_1$ induction is :ref{#thm-semireg-isigma1}, $\Delta^0_1$ comprehension is :ref{#cor-cod-delta1-ca}, and since $I$ is exponential by :ref{#thm-semireg-isigma1}, weak König's lemma is :ref{#thm-scott-wkl-cut}.

($\Leftarrow$) The first-order part $I$ satisfies $\mathrm I\Sigma_1$, hence $\mathrm{exp}$, and is an exponential cut, as at the end of the proof of :ref{#thm-semireg-isigma1}. Let $f$ be a coded function with domain $a \in I$, given by $s \in M$, and suppose that its values in $I$ are cofinal in $I$. For $y \in M$, let $d_y < 2^a$ code the set $\{ i < a : f(i) < y \}$ (:ref{#thm-delta0-comprehension}); if $y \in I$, then $d_y < 2^a \in I$. The relation $z = d_y$ is defined in $M$ by a bounded formula with the parameters $s$ and $a$, so the set $R$ of pairs $\langle y, z \rangle \in I$ with $z = d_y$ belongs to $\mathrm{Cod}(M/I)$, by :ref{#ex-coded-subsets}. Consider the $\Sigma^0_1$ formula with parameter $R$
$$
\varphi(m) \equiv \exists y\ \exists z\ (\langle y, z \rangle \in R \wedge z \geq m).
$$
It holds at $m = 0$. Suppose $\varphi(m)$ in $I$, with $z = d_y \geq m$ and $y \in I$. Since the values of $f$ in $I$ are cofinal, some $i < a$ has $y \leq f(i) \in I$; let $y' = f(i) + 1 \in I$. Then $\mathrm{Ack}(d_{y'})$ contains $\mathrm{Ack}(d_y)$ and the element $i \notin \mathrm{Ack}(d_y)$. By :ref{#ex-subset-sum}, $d_{y'} \geq d_y + 1 > m$. As $y' \in I$ and $d_{y'} < 2^a \in I$, the pair $\langle y', d_{y'} \rangle$ belongs to $R$. Thus $\varphi(m + 1)$. By $\Sigma^0_1$ induction, $\varphi(2^a)$ holds: some $d_y \geq 2^a$, a contradiction.
:::

:::quiz[the Kirby–Paris characterization]
In the proof of ($\Leftarrow$), where is it used that $I$ is an exponential cut?

- [x] To have $d_{y'} < 2^a \in I$, so that the pair $\langle y', d_{y'} \rangle$ lies in $I$ and belongs to $R$, and so that the induction can be run up to $m = 2^a$ inside $I$.
- [ ] To define the codes $d_y$.

  The codes exist in $M$ by bounded comprehension, since $M \models \mathrm{exp}$; no property of $I$ is used.
- [ ] To show that $R$ belongs to $\mathrm{Cod}(M/I)$.

  $R$ is the trace on $I$ of a set defined in $M$ by a bounded formula, which is coded by :ref{#ex-coded-subsets} for every proper cut.
:::

The second direction uses only $\Sigma^0_1$ induction with set parameters, so the proof shows that a proper cut closed under multiplication is semiregular if and only if $(I, \mathrm{Cod}(M/I))$ satisfies $\Sigma^0_1$ induction. Kirby and Paris used semiregular cuts to construct models of $\mathrm I\Sigma_1$ inside models of stronger theories; the method of indicators, in the last course of the track, refines this to show that $\mathrm I\Sigma_1$ does not prove the totality of fast-growing functions such as the Ackermann function.

## Regular cuts

Semiregularity is a bounding property for coded functions on bounded domains. A stronger property concerns coded colorings of the whole cut with a bounded number of colors.

:::definition[Kirby, Paris]{#def-regular-cut}
A proper cut $I$ of $M$ closed under addition and multiplication is **regular** if for every $a \in I$ and every function $F : I \to [0, a)$ whose graph $\{ \langle x, F(x) \rangle : x \in I \}$ belongs to $\mathrm{Cod}(M/I)$, there is $j < a$ such that $F^{-1}(j)$ is unbounded in $I$.
:::

In words: $(I, \mathrm{Cod}(M/I))$ satisfies the infinite pigeonhole principle for a bounded number of colors. The standard cut is regular in every non-standard $M$, by the infinite pigeonhole principle: a coloring of $\nat$ with finitely many colors has an infinite color class.

:::proposition{#prop-regular-semireg}
Every regular cut is semiregular.
:::

:::proof{of=prop-regular-semireg}
Suppose that $I$ is closed under addition and multiplication, as in the definition of regular cuts, and not semiregular: some coded function $f$ with domain $a \in I$ has values cofinal in $I$. For $x \in I$, if some value of $f$ is at most $x$, let $F(x)$ be the least $i < a$ such that $f(i)$ is the largest value of $f$ that is at most $x$; otherwise let $F(x) = 0$. The largest such value exists in $M$, since the set of values of $f$ that are at most $x$ is defined by a bounded formula with the parameter coding $f$. So the graph of $F$ is defined by a bounded formula with parameters, and its restriction to $I$ belongs to $\mathrm{Cod}(M/I)$ by :ref{#ex-coded-subsets}; $F$ maps $I$ into $[0, a)$. Let $j < a$. If $F(x) = j$ for some $x$ in the first case, then $f(j) \leq x$ is in $I$, and by cofinality some $i$ has $f(j) < f(i) \in I$; for every $x \geq f(i)$, the largest value at most $x$ is at least $f(i) > f(j)$, so $F(x) \neq j$. The elements $x$ of the second case are below every value of $f$ in $I$. In both cases $F^{-1}(j)$ is bounded in $I$, and $I$ is not regular.
:::

The converse fails: Kirby and Paris (1977) built semiregular cuts that are not regular. With their coded subsets, regular cuts are characterized by a collection scheme: by a theorem of Hirst, the infinite pigeonhole principle for arbitrarily many colors is equivalent over $\mathsf{RCA}_0$ to $\Sigma^0_2$ collection (:ref{to="induction-conservation/pigeonhole"}), and accordingly a semiregular cut $I$ is regular if and only if $(I, \mathrm{Cod}(M/I))$ satisfies $\Sigma^0_2$ collection with set parameters (Hájek and Pudlák, Theorem IV.2.21, for short cuts). We admit this characterization.

## Notes and references

:ref{#thm-kirby-paris-wkl} is Wong's Theorem 5.9 (Kirby and Paris), of which Wong proves one direction; the proof of the other direction given here, by $\Sigma^0_1$ induction on the codes $d_y$, is added. Hájek and Pudlák treat regular cuts in models of arithmetic with a top, as $1$-Ramsey cuts (Definition IV.2.19 and the remark after it); :ref{#prop-regular-semireg} is their Theorem IV.2.20, and the characterization by collection is the case $k = 1$ of their Theorem IV.2.21. Hirst's theorem is proved in the course on induction and conservation.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 2(c).
