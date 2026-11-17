---
title: Semiregular cuts
summary: Semiregular cuts, in which no coded function on a bounded domain has values cofinal in the cut; they are closed under addition and multiplication, and with their coded subsets they satisfy Σ⁰₁ induction (Kirby and Paris).
duration: 30
prerequisites: [weak-konig-cuts]
---

The previous lessons studied the coded subsets of an arbitrary cut. This lesson asks when a cut, with its coded subsets, is itself a model of a reasonable theory. Coded subsets always satisfy $\Delta^0_1$ comprehension, and those of exponential cuts satisfy weak König's lemma; what may fail is induction. Kirby and Paris found the condition that restores it, by analogy with regular cardinals: no coded function with domain bounded in the cut should have values cofinal in the cut. Such cuts are called **semiregular**. This lesson proves that they satisfy $\Sigma^0_1$ induction, which makes them a source of models of $\mathrm I\Sigma_1$; the next lesson shows that they are exactly the cuts whose coded subsets form a model of $\mathsf{WKL}_0$, and compares them with the regular cuts.

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

*Multiplication.* We may assume $a \geq 1$ and $b \geq 1$. The function $g(i) = a \cdot i$, for $i < b$, is coded; let $d \in I$ bound its values in $I$. The set of $i < b$ with $a \cdot i < d$ is defined by a bounded formula and contains $0$, since $g(0) = 0$ is a value in $I$, so it has a largest element $i_0$. If $i_0 + 1 < b$, then $a (i_0 + 1) = a \cdot i_0 + a$ is in $I$, by closure under addition, since $a \cdot i_0 < d$; it is a value of $g$ in $I$, so it is below $d$, contradicting the maximality of $i_0$. So $i_0 = b - 1$, and $a \cdot b = a \cdot i_0 + a \in I$.
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

## Exercises

::::exercise{#ex-semireg-preimage difficulty=1 objective="Use the bound given by semiregularity to code the set of arguments at which a coded function takes values in the cut."}
Let $I$ be a semiregular cut of $M$, $a \in I$, and $f$ a coded function with domain $a$. Show that $\{ i < a : f(i) \in I \}$ belongs to $\mathrm{Cod}(M/I)$.

:::solution
Let $d \in I$ bound the values of $f$ that lie in $I$. For $i < a$, $f(i) \in I$ if and only if $f(i) < d$: one direction is the choice of $d$, the other holds because $I$ is an initial segment. The set $\{ i < a : f(i) < d \}$ is defined in $M$ by a bounded formula with parameters, so its trace on $I$, which is the set itself since $a \in I$, belongs to $\mathrm{Cod}(M/I)$ by :ref{#ex-coded-subsets}.
:::
::::

## Notes and references

Semiregular and regular cuts were introduced by Kirby and Paris (1977), by analogy with regular cardinals. The definition, :ref{#ex-not-semiregular} and :ref{#lem-semireg-closed} follow Wong's Lecture 5 (definition of semiregularity, Example 5.7, Lemma 5.8); :ref{#thm-semireg-isigma1} is the part of Wong's Theorem 5.9 proved there, here with set parameters. Hájek and Pudlák define semiregular cuts in models of arithmetic with a top by strong collection for coded functions, and prove that they are exactly the cuts satisfying $\mathrm I\Sigma^*_1$, induction for $\Sigma_1$ formulas with coded set parameters (Definition IV.2.15, Theorem IV.2.16). Wong's Lecture 5 applies semiregular cuts to the unprovability in $\mathrm I\Sigma_1$ of the totality of fast-growing functions.

- L. A. S. Kirby and J. B. Paris, *Initial segments of models of Peano's axioms*, in Set Theory and Hierarchy Theory V, Lecture Notes in Mathematics 619, Springer, 1977, 211–226.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 5.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 2(b).

:::::exercises
::::exercise{#ex-semireg-exp difficulty=1 objective="Prove directly, with the coded function $i \mapsto 2^i$, that a semiregular cut is exponential."}
Let $I$ be a semiregular cut of $M$. Without using :ref{#thm-semireg-isigma1}, show that $I$ is exponential, by applying the definition to the coded function $i \mapsto 2^i$ on a suitable domain.

:::solution
Let $a \in I$ and suppose $2^a \notin I$. The function $f(i) = 2^i$, for $i < a + 1$, is coded, by :ref{#prop-seq-basic} with the bounded formula $\varepsilon(i, v)$ and the bound $2^a + 1$. Its domain $a + 1$ is in $I$. Let $y \in I$ with $y \geq 1$, and $\ell = \mathrm{len}(y)$, so that $2^\ell \leq y < 2^{\ell + 1}$ (:ref{#lem-strings-model}). Since $2^a \notin I$ and $y \in I$, $y < 2^a$, so $\ell < a$ and $\ell + 1$ is in the domain of $f$. Moreover $2^{\ell + 1} = 2^\ell + 2^\ell \leq y + y$, which is in $I$ by :ref{#lem-semireg-closed}. So $f(\ell + 1) \in I$ and $f(\ell + 1) > y$: the values of $f$ in $I$ are cofinal in $I$, which contradicts semiregularity. Hence $2^a \in I$.
:::
::::

::::exercise{#ex-not-semireg-mult difficulty=1 objective="Find a cut closed under addition and multiplication that is not semiregular, and check that it is not exponential."}
Let $a \in M$ be non-standard and $I = \{ x \in M : x < 2^{a \cdot n} \text{ for some } n \in \nat \}$. Show that $I$ is a proper cut closed under addition and multiplication, that it is not semiregular, and that it is not exponential.

:::solution
We use the laws $2^u \cdot 2^v = 2^{u + v}$ and $u < v \rightarrow 2^u < 2^v$, provable in $\mathrm I\Delta_0 + \mathrm{exp}$ by bounded induction from :ref{#fact-exp}. *A cut.* $I$ is an initial segment containing $0$; if $x < 2^{a n}$, then $x + 1 \leq 2^{a n} < 2^{a (n + 1)}$. *Operations.* If $x < 2^{a n}$ and $y < 2^{a m}$ with $m \leq n$, then $x + y < 2 \cdot 2^{a n} = 2^{a n + 1} \leq 2^{a (n + 1)}$, since $a \geq 1$, and $x \cdot y < 2^{a n} \cdot 2^{a m} = 2^{a (n + m)}$. *Proper.* $2^{a \cdot a}$ exists, and $a \cdot a > a \cdot n$ for every $n \in \nat$, so $2^{a \cdot a} \notin I$.

*Not semiregular.* The function $f(i) = 2^{a \cdot i}$, for $i < a$, is coded, by :ref{#prop-seq-basic} with the bounded formula $\varepsilon(a \cdot i, v)$ and the bound $2^{a \cdot a}$. Its domain $a$ is in $I$, since $a < 2^a$. For $n \in \nat$, the value $f(n) = 2^{a n}$ lies in $I$, and these values are cofinal in $I$ by definition. *Not exponential.* $a \cdot a < 2^a \cdot 2^a = 2^{2a}$, so $a \cdot a \in I$, but $2^{a \cdot a} \notin I$. This agrees with :ref{#ex-semireg-exp}; the cut of :ref{#ex-not-semiregular} fails semiregularity for a cruder reason, not being closed under multiplication.
:::
::::

::::exercise{#ex-semireg-bounded-sigma1 difficulty=2 objective="Adapt the least witness argument of the Kirby–Paris theorem to prove bounded $\Sigma^0_1$ comprehension in a semiregular cut."}
Let $I$ be a semiregular cut of $M$, $a \in I$, and $\varphi(x)$ a $\Sigma^0_1$ formula of $\mathcal L_2$ with set parameters in $\mathrm{Cod}(M/I)$ and number parameters in $I$. Show that $\{ x < a : (I, \mathrm{Cod}(M/I)) \models \varphi(x) \}$ belongs to $\mathrm{Cod}(M/I)$.

:::solution
Write $\varphi(x) \equiv \exists y\ \eta(x, y)$ with $\eta$ bounded, contracting a block of quantifiers by pairing, and let $\bar c$ be codes of the set parameters, $\eta' = \eta[\bar c]$ and $e \in M \setminus I$. As in the proof of :ref{#thm-semireg-isigma1}, let $f$ be the coded function with domain $a$ such that $f(x)$ is the least $y < e$ with $M \models \eta'(x, y)$ if there is one, and $f(x) = e$ otherwise, and let $d \in I$ bound the values of $f$ in $I$. The claim of that proof, applied with $b + 1 = a$, gives, for $x < a$,
$$
(I, \mathrm{Cod}(M/I)) \models \varphi(x) \iff M \models \exists y < d\ \eta'(x, y).
$$
The right-hand side is a bounded formula with parameters, so by :ref{#thm-delta0-comprehension} some $c$ codes $\{ x < a : M \models \exists y < d\ \eta'(x, y) \}$. This set is contained in $[0, a) \subseteq I$, so it equals its trace $\mathrm{Ack}(c) \cap I$, and it is the required set.
:::
::::

::::exercise{#ex-semireg-preimage-converse difficulty=2 objective="Prove the converse of the featured exercise, so that semiregularity is characterized by coding the arguments with values in the cut."}
Let $I$ be a proper cut of $M$ such that for every $a \in I$ and every coded function $f$ with domain $a$, the set $\{ i < a : f(i) \in I \}$ belongs to $\mathrm{Cod}(M/I)$. Show that $I$ is semiregular. With :ref{#ex-semireg-preimage}, this characterizes semiregular cuts.

:::solution
Let $f$ be coded by $s$, with domain $a \in I$, and let $c$ satisfy $\mathrm{Ack}(c) \cap I = \{ i < a : f(i) \in I \}$. Since $a \in I$, for $i < a$ we have $i \in c$ if and only if $f(i) \in I$. If $a = 0$ there is nothing to prove; let $a \geq 1$. Let $g$ be the coded function with domain $a$ given by $g(i) = f(i)$ if $i \in c$ and $g(i) = 0$ otherwise (:ref{#prop-seq-basic}, with a bounded formula and the bound $s + 1$). All values of $g$ lie in $I$.

The set of $m \leq s$ such that $g(i) \leq m$ for every $i < a$ is defined by a bounded formula and contains $s$; let $m_0$ be its least element. If $m_0 = 0$, then $m_0 = g(0)$. If $m_0 > 0$, then $m_0 - 1$ is not an upper bound, so $g(i) \geq m_0$ for some $i < a$, and $g(i) = m_0$. In both cases $m_0$ is a value of $g$, hence $m_0 \in I$. Every value of $f$ in $I$ is $f(i)$ with $i \in c$, hence equal to $g(i) \leq m_0$; so $d = m_0 + 1 \in I$ bounds the values of $f$ in $I$.
:::
::::

::::exercise{#ex-semireg-local difficulty=2 objective="Show that semiregularity and the coded subsets of a cut only depend on an exponential cut above it, by truncating coded functions."}
Let $I \subsetneq J$ be cuts of $M$, with $J$ exponential. Show that $J$ is a model of $\mathrm I\Delta_0 + \mathrm{exp}$ in which $I$ is a proper cut, that $\mathrm{Cod}(J/I) = \mathrm{Cod}(M/I)$, and that $I$ is semiregular in $J$ if and only if it is semiregular in $M$.

:::solution
$J$ is closed under addition and multiplication (:ref{#ex-exp-cut-closed}), so $J \models \mathrm I\Delta_0$ and $J \subseteq_e M$ (:ref{#lem-cut-model}). For $x \in J$, $2^x \in J$ and $J \models \varepsilon(x, 2^x)$ by :ref{#lem-delta0-absolute}, so $J \models \mathrm{exp}$, and powers in $J$ are those of $M$. Bounded formulas with parameters in $J$ have the same meaning in $J$ and in $M$; in particular $\mathrm{Ack}^J(c) = \mathrm{Ack}(c) \cap J$ for $c \in J$, and an element of $J$ codes in $J$ the same sequence as in $M$, since $\mathrm{Seq}$ and $(s)_i$ are bounded.

*Coded sets.* $\mathrm{Cod}(J/I) \subseteq \mathrm{Cod}(M/I)$ by the previous remark. Conversely, let $c \in M$ and $b \in J \setminus I$. By :ref{#thm-delta0-comprehension}, some $c' < 2^b$ codes $\{ x < b : x \in c \}$; then $c' \in J$, and $\mathrm{Ack}(c') \cap I = \mathrm{Ack}(c) \cap I$, since $I \subseteq [0, b)$.

*Semiregularity.* If $I$ is semiregular in $M$, it is semiregular in $J$, because a coded function of $J$ is a coded function of $M$ with the same values. Conversely, suppose that $I$ is semiregular in $J$, and let $f$ be a coded function of $M$ with domain $a \in I$. Fix $b \in J \setminus I$, and let $g(i) = f(i)$ if $f(i) < b$ and $g(i) = b$ otherwise, for $i < a$. By :ref{#prop-seq-basic}, $g$ is coded in $M$ by some $s' < 2^{\langle a, b + 1 \rangle}$; since $J$ is closed under addition, multiplication and pairing (:ref{#fact-pairing}) and is exponential, $s' \in J$, and $s'$ codes $g$ in $J$. If $f(i) \in I$, then $f(i) < b$ and $g(i) = f(i)$; if $g(i) \in I$, then $g(i) \neq b$, so $g(i) = f(i)$. So $f$ and $g$ have the same values in $I$, which are bounded in $I$ by semiregularity in $J$.
:::
::::
:::::
