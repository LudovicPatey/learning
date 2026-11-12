---
title: Semiregular and regular cuts
summary: Semiregular cuts, in which no coded function on a bounded domain has values cofinal in the cut; they are closed under addition and multiplication, and with their coded subsets they satisfy Σ⁰₁ induction (Kirby and Paris); a proper cut is semiregular if and only if it is closed under multiplication and its coded subsets form a model of WKL₀; regular cuts and the pigeonhole principle; every regular cut is semiregular.
duration: 50
prerequisites: [weak-konig-cuts]
---

The previous lessons studied the coded subsets of an arbitrary cut. This lesson asks when a cut, with its coded subsets, is itself a model of a reasonable theory. Coded subsets always satisfy $\Delta^0_1$ comprehension, and those of exponential cuts satisfy weak König's lemma; what may fail is induction. Kirby and Paris found the condition that restores it, by analogy with regular cardinals: no coded function with domain bounded in the cut should have values cofinal in the cut. Such cuts are called **semiregular**. They satisfy $\Sigma^0_1$ induction, which makes them a source of models of $\mathrm I\Sigma_1$, and they are exactly the cuts whose coded subsets form a model of $\mathsf{WKL}_0$.

Throughout, $M$ is a model of $\mathrm I\Delta_0 + \mathrm{exp}$, so that finite sequences are coded (:ref{#def-coded-sequence}).

## Semiregular cuts

A **coded function with domain $a$** is a function $f : [0, a) \to M$, $f(i) = (s)_i$, for some $s \in M$ coding a sequence of length $a$. By :ref{#prop-seq-basic}, if $\delta(i, v, \bar p)$ is a bounded formula, with parameters in $M$, such that every $i < a$ has exactly one $v < e$ with $\delta(i, v, \bar p)$, then the function $i \mapsto v$ is a coded function with domain $a$.

:::definition[Kirby, Paris]{#def-semiregular}
A proper cut $I$ of $M$ is **semiregular** if for every $a \in I$ and every coded function $f$ with domain $a$, the set $\{ f(i) : i < a \} \cap I$ is bounded in $I$: there is $d \in I$ such that $f(i) < d$ for every $i < a$ with $f(i) \in I$.
:::

A coded function on a domain bounded in $I$ is "small" from the point of view of the cut; semiregularity says that small sets of values cannot reach the top of the cut. The values that lie above $I$ do not matter.

:::figure[A coded function $f$ with domain $a \in I$. In a semiregular cut, the values of $f$ that lie in $I$ are bounded by some $d \in I$; the other values lie above $I$, and play no role.]
<svg class="fig" viewBox="0 0 600 220" width="600" role="img" aria-label="A coded function f with domain a in the cut I; the values of f that lie in I are bounded by some d in I, the other values lie above I"><line x1="30.0" y1="180.0" x2="570.0" y2="180.0" class="ink-stroke" stroke-width="1.2"/><line x1="30.0" y1="40.0" x2="570.0" y2="40.0" class="ink-stroke" stroke-width="1.2"/><text x="30" y="210" class="label">domain of f</text><text x="570" y="24" text-anchor="end" class="label">values of f</text><circle cx="34.0" cy="180.0" r="3.5" class="accent-fill"/><circle cx="170.0" cy="180.0" r="3.5" class="ink-fill"/><text x="170.0" y="198.0" text-anchor="middle" class="math" font-size="14">a</text><line x1="330.0" y1="166.0" x2="330.0" y2="194.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><line x1="330.0" y1="26.0" x2="330.0" y2="54.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="345.0" y="198.0" text-anchor="middle" class="math" font-size="13">I</text><text x="345.0" y="32.0" text-anchor="middle" class="math" font-size="13">I</text><circle cx="240.0" cy="40.0" r="3.5" class="ink-fill"/><text x="240.0" y="28.0" text-anchor="middle" class="math" font-size="14">d</text><line x1="50.0" y1="176.0" x2="120.0" y2="44.0" class="accent-stroke" stroke-width="1.2"/><circle cx="50.0" cy="180.0" r="2.5" class="node"/><circle cx="120.0" cy="40.0" r="3" class="accent-fill"/><line x1="66.0" y1="176.0" x2="520.0" y2="44.0" class="muted-stroke" stroke-width="1.2"/><circle cx="66.0" cy="180.0" r="2.5" class="node"/><circle cx="520.0" cy="40.0" r="3" class="node"/><line x1="82.0" y1="176.0" x2="60.0" y2="44.0" class="accent-stroke" stroke-width="1.2"/><circle cx="82.0" cy="180.0" r="2.5" class="node"/><circle cx="60.0" cy="40.0" r="3" class="accent-fill"/><line x1="98.0" y1="176.0" x2="455.0" y2="44.0" class="muted-stroke" stroke-width="1.2"/><circle cx="98.0" cy="180.0" r="2.5" class="node"/><circle cx="455.0" cy="40.0" r="3" class="node"/><line x1="114.0" y1="176.0" x2="200.0" y2="44.0" class="accent-stroke" stroke-width="1.2"/><circle cx="114.0" cy="180.0" r="2.5" class="node"/><circle cx="200.0" cy="40.0" r="3" class="accent-fill"/><line x1="130.0" y1="176.0" x2="560.0" y2="44.0" class="muted-stroke" stroke-width="1.2"/><circle cx="130.0" cy="180.0" r="2.5" class="node"/><circle cx="560.0" cy="40.0" r="3" class="node"/><line x1="146.0" y1="176.0" x2="160.0" y2="44.0" class="accent-stroke" stroke-width="1.2"/><circle cx="146.0" cy="180.0" r="2.5" class="node"/><circle cx="160.0" cy="40.0" r="3" class="accent-fill"/><line x1="160.0" y1="176.0" x2="390.0" y2="44.0" class="muted-stroke" stroke-width="1.2"/><circle cx="160.0" cy="180.0" r="2.5" class="node"/><circle cx="390.0" cy="40.0" r="3" class="node"/><path d="M36,56 L36,62 L236,62 L236,56" class="muted-stroke" stroke-width="1.2"/><text x="136.0" y="80" text-anchor="middle" class="label">values in I: all below d</text><path d="M340,56 L340,62 L568,62 L568,56" class="muted-stroke" stroke-width="1.2"/><text x="454.0" y="80" text-anchor="middle" class="label">values above I</text></svg>
:::

:::example{#ex-not-semiregular}
1. The standard cut $\nat$ is semiregular in every non-standard $M$: if $a \in \nat$, a function with domain $a$ has finitely many values.
2. Let $c \in M$ be non-standard, and $I = \{ x \in M : x < n \cdot c \text{ for some } n \in \nat \}$, a proper cut, since $c \cdot c \notin I$. The function $f(i) = i \cdot c$, for $i < c$, is coded, by :ref{#prop-seq-basic} with the bounded formula $v = i \cdot c$ and the bound $c \cdot c$. Its domain $c$ is in $I$, and its values $n \cdot c$, for $n \in \nat$, are cofinal in $I$. So $I$ is not semiregular. Note that $I$ is closed under addition but not under multiplication.
:::

The second example is typical: a cut that is the supremum of the values of a coded function with domain in the cut is not semiregular. In particular, semiregular cuts are closed under the operations.

:::lemma{#lem-semireg-closed}
Every semiregular cut $I$ of $M$ is closed under addition and multiplication.
:::

:::proof{of=lem-semireg-closed}
Let $a, b \in I$. *Addition.* The function $f(i) = a + i$, for $i < b$, is coded. If $a + b \notin I$, every $y \in I$ with $y \geq a$ is below $a + b$, hence equal to $f(i)$ for some $i < b$; so the values of $f$ in $I$ are cofinal in $I$, contradicting semiregularity.

*Multiplication.* We may assume $a \geq 1$. The function $g(i) = a \cdot i$, for $i < b$, is coded; let $d \in I$ bound its values in $I$. The set of $i < b$ with $a \cdot i < d$ is defined by a bounded formula and contains $0$, so it has a largest element $i_0$. If $i_0 + 1 < b$, then $a (i_0 + 1) = a \cdot i_0 + a$ is in $I$, by closure under addition, since $a \cdot i_0 < d$; it is a value of $g$ in $I$, so it is below $d$, contradicting the maximality of $i_0$. So $i_0 = b - 1$, and $a \cdot b = a \cdot i_0 + a \in I$.
:::

## Semiregular cuts satisfy Σ⁰₁ induction

By :ref{#lem-semireg-closed}, a semiregular cut $I$ is a substructure of $M$, and $(I, \mathrm{Cod}(M/I))$ is an $\mathcal L_2$-structure. The idea of the next theorem is to make a $\Sigma^0_1$ formula bounded on a bounded part of the cut. Given $\exists y\ \eta(x, y)$ and $a \in I$, let $f(x)$ be the least witness $y$ for $x$, computed in $M$ below some element $e$ above $I$. Semiregularity bounds those values of $f$ that lie in $I$ by a single $d \in I$; then for $x \leq a$, "$\exists y\ \eta(x, y)$ in $I$" is equivalent to "$\exists y < d\ \eta(x, y)$", a bounded formula, to which induction in $M$ applies. This is the device of collection, obtained here from the cut rather than from an axiom.

:::theorem[Kirby, Paris]{#thm-semireg-isigma1}
Let $I$ be a semiregular cut of $M$. Then $(I, \mathrm{Cod}(M/I))$ satisfies the induction scheme for $\Sigma^0_1$ formulas with set and number parameters. In particular $I \models \mathrm I\Sigma_1$, and $I$ is an exponential cut.
:::

:::proof{of=thm-semireg-isigma1}
*Bounded induction.* Let $\delta$ be a bounded $\mathcal L_2$ formula with parameters $\bar X = \mathrm{Ack}(\bar c) \cap I$ and number parameters in $I$, and suppose $(I, \bar X) \models \delta(0) \wedge \forall x\, (\delta(x) \rightarrow \delta(x + 1))$ and $(I, \bar X) \models \neg \delta(b)$. By :ref{#lem-delta00-absolute-cut}, the bounded formula $\neg \delta[\bar c](x)$ holds at $b$ in $M$, so it has a least solution $x_0 \leq b$ in $M$; $x_0 \in I$, $x_0 \neq 0$, and $x_0 - 1$ satisfies $\delta$, so $x_0$ does too: a contradiction.

*$\Sigma^0_1$ induction.* Let $\varphi(x) \equiv \exists y\ \eta(x, y)$, with $\eta$ bounded and parameters as above (a block of quantifiers $\exists \bar y$ is contracted to one by pairing, :ref{#fact-pairing}). Suppose $(I, \bar X) \models \varphi(0) \wedge \forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$, and let $b \in I$. Write $\eta' = \eta[\bar c]$, fix $e \in M \setminus I$, and let $f$ be the coded function with domain $b + 1$ such that $f(x)$ is the least $y < e$ with $M \models \eta'(x, y)$ if there is one, and $f(x) = e$ otherwise; it is coded by :ref{#prop-seq-basic}, with a bounded formula and the bound $e + 1$. Let $d \in I$ bound the values of $f$ in $I$. For $x \leq b$, we claim
$$
(I, \bar X) \models \varphi(x) \iff M \models \exists y < d\ \eta'(x, y).
$$
If $(I, \bar X) \models \eta(x, y)$ with $y \in I$, then $M \models \eta'(x, y)$ by :ref{#lem-delta00-absolute-cut}, and $y < e$; so $f(x) \leq y$ is a witness in $I$, and $f(x) < d$. Conversely, a witness $y < d$ is in $I$, and satisfies $\eta$ in $(I, \bar X)$ by the same lemma. The right-hand side is $\psi[\bar c](x)$ for the bounded $\mathcal L_2$ formula $\psi(x) \equiv \exists y < d\ \eta(x, y)$, with the parameter $d \in I$. By the claim and the hypothesis, $\psi(0)$ holds in $(I, \bar X)$, and $\psi(x) \rightarrow \psi(x + 1)$ for $x < b$. Bounded induction, applied to $x \leq b \rightarrow \psi(x)$, gives $\psi(b)$, hence $\varphi(b)$.

*Consequences.* Taking no set parameters, $I \models \mathrm I\Sigma_1$, so $I \models \mathrm{exp}$ by :ref{#prop-isigma1-exp}. For $a \in I$, the element $y \in I$ with $I \models \varepsilon(a, y)$ satisfies $M \models \varepsilon(a, y)$ by :ref{#lem-delta0-absolute}, so the power $2^a$ of $M$ is $y \in I$.
:::

:::quiz[semiregular cuts and induction]
In the proof of :ref{#thm-semireg-isigma1}, why is $f(x)$ defined as the *least* witness below $e$, rather than as any witness below $e$?

- [x] A witness below $e$ may lie above $I$ even when $x$ has a witness in $I$. The least witness lies in $I$ whenever some witness does, so the bound $d$ on the values of $f$ in $I$ bounds a witness for every $x$ that has one in $I$.
- [ ] To make $f$ a coded function.

  Any choice given by a bounded formula with a unique value gives a coded function; minimality is not needed for coding.
- [ ] Because $\eta'$ has no witness above $e$.

  Witnesses above $e$ play no role; all witnesses that matter are in $I$, below $e$.

:::

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

::::exercise{difficulty=1}
Let $I$ be a semiregular cut of $M$, $a \in I$, and $f$ a coded function with domain $a$. Show that $\{ i < a : f(i) \in I \}$ belongs to $\mathrm{Cod}(M/I)$.

:::solution
Let $d \in I$ bound the values of $f$ that lie in $I$. For $i < a$, $f(i) \in I$ if and only if $f(i) < d$: one direction is the choice of $d$, the other holds because $I$ is an initial segment. The set $\{ i < a : f(i) < d \}$ is defined in $M$ by a bounded formula with parameters, so its trace on $I$, which is the set itself since $a \in I$, belongs to $\mathrm{Cod}(M/I)$ by :ref{#ex-coded-subsets}.
:::
::::

## Notes and references

Semiregular and regular cuts were introduced by Kirby and Paris (1977), by analogy with regular cardinals. The definition and :ref{#lem-semireg-closed} follow Wong's Lecture 5 (definition of semiregularity, Lemma 5.8, Example 5.7); :ref{#thm-semireg-isigma1} is the part of Wong's Theorem 5.9 proved there, here with set parameters, and :ref{#thm-kirby-paris-wkl} is Wong's Theorem 5.9 (Kirby and Paris). Hájek and Pudlák treat these cuts in models of arithmetic with a top: semiregular cuts and $\mathrm I\Sigma^*_1$ (Definition IV.2.15, Theorem IV.2.16), regular cuts as $1$-Ramsey cuts (Definition IV.2.19 and the remark after it), :ref{#prop-regular-semireg} (Theorem IV.2.20), and the characterization by collection (Theorem IV.2.21). Wong's Lecture 5 applies semiregular cuts to the unprovability in $\mathrm I\Sigma_1$ of the totality of fast-growing functions.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 2(b)–(c).
