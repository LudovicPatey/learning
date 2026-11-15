---
title: The Kirby–Paris characterization and regular cuts
summary: A proper cut is semiregular if and only if it is closed under multiplication and its coded subsets form a model of WKL₀ (Kirby and Paris); regular cuts and the pigeonhole principle; every regular cut is semiregular.
duration: 30
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

## Exercises

::::exercise{#ex-exp-not-semireg difficulty=2 objective="Build an exponential cut that is not semiregular, and deduce from the Kirby–Paris characterization that its coded subsets satisfy weak König's lemma but not $\Sigma^0_1$ induction."}
Let $M$ be a non-standard model of $\mathrm I\Sigma_1$ and $a \in M$ non-standard. Show that $M$ has a sequence $s$ of length $a$ with $(s)_0 = a$ and $(s)_{i+1} = 2^{(s)_i}$ for $i + 1 < a$. Let $I = \{ x \in M : x < (s)_n \text{ for some } n \in \nat \}$. Show that $I$ is a proper exponential cut that is not semiregular. Deduce that $(I, \mathrm{Cod}(M/I))$ satisfies $\Delta^0_1$ comprehension and weak König's lemma, but not the $\Sigma^0_1$ induction scheme.

:::solution
*The sequence.* $M \models \mathrm{exp}$ (:ref{#prop-isigma1-exp}). Let $\theta(\ell)$ say that some $s$ codes a sequence of length $\ell + 1$ with $(s)_0 = a$ and $\varepsilon((s)_i, (s)_{i+1})$ for every $i < \ell$; it is a $\Sigma_1$ formula, the rest being bounded. $\theta(0)$ holds, and if $s$ witnesses $\theta(\ell)$, the concatenation $s^\frown 2^{(s)_\ell}$ (:ref{#prop-seq-basic}) witnesses $\theta(\ell + 1)$. By $\Sigma_1$ induction, $\theta(a - 1)$ holds. By bounded induction on $j$, $(s)_i < (s)_j$ for $i < j < a$, since $x < 2^x$.

*The cut.* $I$ is an initial segment containing $0$. If $x < (s)_n$, then $2^x < 2^{(s)_n} = (s)_{n + 1}$, so $I$ is exponential, hence closed under successor, addition and multiplication (:ref{#ex-exp-cut-closed}). The element $(s)_{a - 1}$ is above every $(s)_n$, $n \in \nat$, since $n < a - 1$; so it is not in $I$, and $I$ is proper.

*Not semiregular.* The domain $a$ of $s$ is in $I$, since $a = (s)_0 < (s)_1$. For $n \in \nat$, $(s)_n < (s)_{n+1}$, so $(s)_n \in I$; these values are cofinal in $I$. So $I$ is not semiregular.

*Consequences.* $\Delta^0_1$ comprehension holds by :ref{#cor-cod-delta1-ca}, and weak König's lemma by :ref{#thm-scott-wkl-cut}, since $I$ is a proper exponential cut. The basic axioms hold, since $I$ is a model of $\mathrm I\Delta_0$ (:ref{#lem-cut-model}). If $\Sigma^0_1$ induction held as well, $(I, \mathrm{Cod}(M/I))$ would be a model of $\mathsf{WKL}_0$, and $I$, being closed under multiplication, would be semiregular by :ref{#thm-kirby-paris-wkl}. So $\Sigma^0_1$ induction fails in $(I, \mathrm{Cod}(M/I))$.
:::
::::

## Notes and references

:ref{#thm-kirby-paris-wkl} is Wong's Theorem 5.9 (Kirby and Paris), of which Wong proves one direction; the proof of the other direction given here, by $\Sigma^0_1$ induction on the codes $d_y$, is added. Hájek and Pudlák treat regular cuts in models of arithmetic with a top, as $1$-Ramsey cuts (Definition IV.2.19 and the remark after it); :ref{#prop-regular-semireg} is their Theorem IV.2.20, and the characterization by collection is the case $k = 1$ of their Theorem IV.2.21. Hirst's theorem is proved in the course on induction and conservation.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 2(c).

:::::exercises
::::exercise{#ex-regular-standard-colors difficulty=1 objective="See that the pigeonhole principle for a standard number of colors holds in every cut, so that regularity is about non-standard numbers of colors."}
Let $I$ be a proper cut of $M$ closed under addition and multiplication, $k \in \nat$, and $F : I \to [0, k)$ a function whose graph belongs to $\mathrm{Cod}(M/I)$. Show that $F^{-1}(j)$ is unbounded in $I$ for some $j < k$. Where does the argument fail when $k$ is replaced by a non-standard $a \in I$?

:::solution
Suppose that each $F^{-1}(j)$, $j < k$, is bounded in $I$, by $b_j \in I$: every element of $F^{-1}(j)$ is below $b_j$. Let $b = \max(b_0, \dots, b_{k-1}) \in I$, a maximum of finitely many elements. Then $F(b) = j$ for some $j < k$, so $b \in F^{-1}(j)$ and $b < b_j \leq b$, a contradiction. The graph of $F$ is not used. For a non-standard number $a$ of colors, the bounds $b_j$ exist one by one, but they form a family indexed by $[0, a)$ that need not be coded, and the family of bounds may have no upper bound in $I$; bounding it is an instance of collection, as in the characterization of regular cuts by $\Sigma^0_2$ collection.
:::
::::

::::exercise{#ex-regular-coded-functions difficulty=1 objective="Reformulate regularity with coded functions of the model defined on an interval above the cut."}
Let $I$ be a proper cut of $M$ closed under addition and multiplication. Show that $I$ is regular if and only if for every $a \in I$, every $b \in M \setminus I$ and every coded function $f : [0, b) \to [0, a)$, there is $j < a$ such that $\{ x \in I : f(x) = j \}$ is unbounded in $I$.

:::solution
($\Rightarrow$) Let $f$ be coded by $s$. Its restriction $F$ to $I$ maps $I$ into $[0, a)$, since $I \subseteq [0, b)$, and its graph is the trace on $I$ of the set of $z < \langle b, a \rangle$ such that $z = \langle x, v \rangle$ with $x < b$ and $v = (s)_x$, which is defined by a bounded formula; it is coded by :ref{#ex-coded-subsets}. Regularity gives $j$ with $F^{-1}(j) = \{ x \in I : f(x) = j \}$ unbounded.

($\Leftarrow$) Let $F : I \to [0, a)$ have graph $G = \mathrm{Ack}(c) \cap I$, and take $b \in M \setminus I$. Let $f(x)$, for $x < b$, be the least $j < a$ with $\langle x, j \rangle \in c$, or $0$ if there is none; it is coded, by :ref{#prop-seq-basic} with a bounded formula and the bound $a$. For $x \in I$ and $j < a$, $\langle x, j \rangle \in I$, since $I$ is closed under addition and multiplication, so $\langle x, j \rangle \in c$ if and only if $\langle x, j \rangle \in G$, if and only if $j = F(x)$. So $f(x) = F(x)$ for $x \in I$, and the hypothesis gives $j$ with $F^{-1}(j)$ unbounded.
:::
::::

::::exercise{#ex-regular-cover difficulty=1 objective="Derive from regularity that a coded cover of the cut by a bounded number of sets has an unbounded member."}
Let $I$ be a regular cut of $M$, $a \in I$, and $R \in \mathrm{Cod}(M/I)$ such that the sets $X_j = \{ x \in I : \langle x, j \rangle \in R \}$, for $j < a$, cover $I$. Show that some $X_j$ is unbounded in $I$.

:::solution
Let $F(x)$ be the least $j < a$ with $x \in X_j$, which exists since the sets cover $I$. The graph of $F$ is the set of $z \in I$ such that $z = \langle x, y \rangle$ for some $x, y \leq z$ with $y < a$, $\langle x, y \rangle \in R$ and $\langle x, j \rangle \notin R$ for every $j < y$; this is a bounded $\mathcal L_2$ formula with parameters $a$ and $R$, using the bounded definition of pairing (:ref{#fact-pairing}), so the graph belongs to $\mathrm{Cod}(M/I)$ by :ref{#cor-cod-delta1-ca}. By regularity, some $F^{-1}(j)$ is unbounded in $I$, and $F^{-1}(j) \subseteq X_j$.
:::
::::

::::exercise{#ex-semireg-bounded-comprehension difficulty=2 objective="Characterize semiregular cuts by bounded $\Sigma^0_1$ comprehension, combining two exercises of the previous lesson." lessons="semiregular-cuts"}
Let $I$ be a proper cut of $M$ closed under addition and multiplication. Show that $I$ is semiregular if and only if, for every $a \in I$ and every $\Sigma^0_1$ formula $\varphi(x)$ with parameters, $\{ x < a : (I, \mathrm{Cod}(M/I)) \models \varphi(x) \}$ belongs to $\mathrm{Cod}(M/I)$.

:::solution
($\Rightarrow$) This is :ref{#ex-semireg-bounded-sigma1}.

($\Leftarrow$) By :ref{#ex-semireg-preimage-converse}, it suffices to show that for every coded function $f$ with domain $a \in I$, given by $s$, the set $\{ i < a : f(i) \in I \}$ is coded. Let $G = \{ z \in I : \exists i < a\ \exists v < z + 1\ (z = \langle i, v \rangle \wedge v = (s)_i) \}$, the trace on $I$ of a set defined by a bounded formula; $G \in \mathrm{Cod}(M/I)$ by :ref{#ex-coded-subsets}. For $i < a$: if $f(i) \in I$, then $\langle i, f(i) \rangle \in I$, since $I$ is closed under the operations, so $\langle i, f(i) \rangle \in G$; conversely, if $\langle i, v \rangle \in G$ for some $v \in I$, then $v = f(i) \in I$. So $f(i) \in I$ if and only if $(I, G) \models \exists v\ \exists z\ (z = \langle i, v \rangle \wedge z \in G)$, a $\Sigma^0_1$ formula with the parameter $G$. By hypothesis, $\{ i < a : f(i) \in I \}$ is coded.
:::
::::
:::::
