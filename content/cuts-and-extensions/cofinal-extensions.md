---
title: Elementarity, cofinal extensions and strong collection
summary: Σₙ-elementary substructures and the Tarski–Vaught test level by level; end and cofinal extensions; a cofinal Σₙ-elementary extension of a model of BΣₙ₊₁ is Σₙ₊₂-elementary, and a cofinal Δ₀-elementary extension of a model of PA is elementary; Σₙ₊₁ induction is equivalent to collection for partial functions (Friedman).
duration: 50
prerequisites: [fragments-of-arithmetic/coded-sets]
---

Every extension of models of arithmetic $M \subseteq K$ can be cut in two at the set of elements of $K$ that lie below some element of $M$. Below this set, $K$ is a **cofinal** extension of $M$: it adds new elements, but none above all of $M$. Above it, $K$ is an **end** extension. The two kinds behave in opposite ways. In an end extension, bounded formulas keep their meaning, so $\Sigma_1$ formulas go up and $\Pi_1$ formulas go down (:ref{#cor-sigma1-upward}). In a cofinal extension, every new element is below an old one, so universal statements of the small model can be checked on bounded pieces; collection in the small model then turns bounded pieces into statements that transfer. This lesson proves this preservation theorem for cofinal extensions, and a form of collection for partial functions that will be needed to split extensions in the next lesson.

## Elementarity, level by level

:::definition{#def-n-elementary}
Let $M \subseteq K$ be $\mathcal L_A$-structures, $M$ a substructure of $K$, and $n \geq 0$. $M$ is a **$\Sigma_n$-elementary substructure** of $K$, written $M \preccurlyeq_n K$, if for every $\Sigma_n$ formula $\varphi(\bar x)$ and every tuple $\bar a$ of elements of $M$, $M \models \varphi(\bar a)$ if and only if $K \models \varphi(\bar a)$. We write $M \preccurlyeq K$ if $M \preccurlyeq_n K$ for every $n$.
:::

Since $\Pi_n$ formulas are negations of $\Sigma_n$ formulas, they transfer as well, and $M \preccurlyeq_{n+1} K$ implies $M \preccurlyeq_n K$. A sentence $\forall \bar x\ \varphi(\bar x)$ with $\varphi \in \Sigma_n$ that holds in $K$ holds in $M$ if $M \preccurlyeq_n K$: every instance at a tuple of $M$ transfers down. So **$\Pi_{n+1}$ sentences go down** to $\Sigma_n$-elementary substructures, and theories axiomatized by $\Pi_{n+1}$ sentences are preserved downward. For instance $\mathrm I\Delta_0$, which has a $\Pi_1$ axiomatization (:ref{#lem-idelta0-pi1}), holds in every $\Sigma_0$-elementary substructure of a model of $\mathrm I\Delta_0$.

:::example{#ex-n-elementary}
1. If $M \subseteq_e K$, then $M \preccurlyeq_0 K$, by :ref{#lem-delta0-absolute}.
2. By :ref{#prop-standard-part}, $\nat \preccurlyeq_0 M$ for every model $M$ of $\mathrm{PA}^-$. If $M \models \mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA})$, then $\nat \not\preccurlyeq_1 M$: the $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathrm{PA})$ holds in $M$ and fails in $\nat$.
:::

The **Tarski–Vaught test** of first-order logic says that $M \preccurlyeq K$ as soon as every formula with parameters in $M$ that has a witness in $K$ has one in $M$. It has a version for each level, which lets one prove elementarity without knowing in advance which formulas hold in $M$.

:::lemma[Tarski–Vaught test]{#lem-tarski-vaught-n}
Let $M \preccurlyeq_0 K$ and $n \geq 0$. Then $M \preccurlyeq_{n+1} K$ if and only if for every $\Pi_n$ formula $\eta(\bar y)$ with parameters in $M$, if $K \models \exists \bar y\ \eta(\bar y)$, then $K \models \eta(\bar c)$ for some tuple $\bar c$ of elements of $M$.
:::

:::proof{of=lem-tarski-vaught-n}
If $M \preccurlyeq_{n+1} K$ and $K \models \exists \bar y\ \eta(\bar y)$, then $M \models \exists \bar y\ \eta(\bar y)$, and a witness $\bar c \in M$ satisfies $\eta$ in $K$, since $\Pi_n$ formulas transfer.

Conversely, by induction on $n$, assume the condition for $n$; then $M \preccurlyeq_n K$, by hypothesis if $n = 0$, and by the induction hypothesis otherwise, since the condition for $n$ implies the condition for $n - 1$. Let $\exists \bar y\ \eta(\bar y)$ be a $\Sigma_{n+1}$ formula with parameters in $M$, $\eta \in \Pi_n$. If it holds in $M$, a witness $\bar c \in M$ satisfies $\eta$ in $K$ by $M \preccurlyeq_n K$. If it holds in $K$, the condition gives $\bar c \in M$ with $K \models \eta(\bar c)$, hence $M \models \eta(\bar c)$.
:::

:::definition{#def-cofinal-ext}
Let $M \subseteq K$ be models of $\mathrm{PA}^-$. $K$ is a **cofinal extension** of $M$, written $M \subseteq_{cf} K$, if every element of $K$ is below some element of $M$. The **supremum** of $M$ in $K$ is $\sup_K M = \{ x \in K : x \leq m \text{ for some } m \in M \}$.
:::

An extension may be neither end nor cofinal. The set $\sup_K M$ is closed under addition and multiplication, since $m + m'$ and $m \cdot m'$ are in $M$; it is an initial segment of $K$ containing $M$, and $M \subseteq_{cf} \sup_K M \subseteq_e K$. The next lesson shows that, under induction hypotheses on $M$, some elementarity survives on both sides of this decomposition.

## Preservation in cofinal extensions

In a cofinal extension, a $\Pi_{n+2}$ sentence $\forall x\ \exists y\ \theta(x, y)$ needs only to be checked on the intervals $[0, a)$ with $a \in M$. On such an interval, $M$ can choose the witnesses once and for all, by collection and coding: a single code $s \in M$ lists a witness for each $x < a$. Then "$(s)_x$ is a witness for every $x < a$" is a $\Pi_n$ statement about $s$ and $a$, which transfers to $K$, including the new elements below $a$.

:::theorem{#thm-cofinal-preservation}
Let $n \geq 0$, let $M$ be a model of $\mathrm B\Sigma_{n+1}$, and $K$ an $\mathcal L_A$-structure with $M \subseteq_{cf} K$ and $M \preccurlyeq_n K$. Then $M \preccurlyeq_{n+2} K$.
:::

:::proof{of=thm-cofinal-preservation}
*Step 1: $\Pi_{n+2}$ formulas go up.* Let $\forall \bar x\ \exists \bar y\ \theta(\bar x, \bar y)$ be a $\Pi_{n+2}$ formula with parameters in $M$, $\theta \in \Pi_n$, true in $M$. Let $\bar x \in K$, and $a \in M$ above all its components, by cofinality. Writing $\bar x < a$ for the conjunction of $x_i < a$, it suffices to show $K \models \forall \bar x < a\ \exists \bar y\ \theta(\bar x, \bar y)$. No axiom is available in $K$, so the formulas transferred to $K$ must have the required complexity logically.

If $n = 0$, $\theta$ is bounded, and $\mathrm B\Sigma_1$ in $M$, applied after contracting the tuples by pairing, gives $b \in M$ with $M \models \forall \bar x < a\ \exists \bar y < b\ \theta(\bar x, \bar y)$. This is a bounded formula with parameters in $M$, so it holds in $K$.

If $n \geq 1$, then $M \models \mathrm I\Sigma_1$ (:ref{#thm-fo-paris-kirby}), hence $M \models \mathrm{exp}$, and $M \models \mathrm L\Pi_n$ and $\mathrm B\Sigma_n$. Coding tuples by pairing in $M$, let $g(\bar x)$ be, for $\bar x < a$, the least code of a tuple $\bar y$ with $M \models \theta(\bar x, \bar y)$. Its graph is $\Delta_{n+1}$ in $M$: it is the conjunction of a $\Pi_n$ formula and of a bounded universal quantifier in front of a $\Sigma_n$ formula, which is $\Sigma_n$ in $M$ by :ref{#lem-fo-collection-closure}. Collection gives a bound $b$ on the values of $g$, and the set of pairs $\langle \bar x, \bar y \rangle$ with $\bar x < a$ and $\langle \bar y \rangle = g(\bar x)$ is bounded and $\Delta_{n+1}$-definable in $M$, by Parsons' lemma in $\mathrm B\Sigma_{n+1}$, so it is coded by some $s \in M$ (:ref{#thm-collection-coded}). Then $M$ satisfies
$$
\begin{gathered}
\forall \bar x < a\ \exists \bar y < s\ \exists z < s\ \big(z = \langle \bar x, \bar y \rangle \wedge z \in s\big), \\
\forall \bar x < a\ \forall \bar y < s\ \forall z < s\ \big(z = \langle \bar x, \bar y \rangle \wedge z \in s \rightarrow \theta(\bar x, \bar y)\big),
\end{gathered}
$$
where $z = \langle \bar x, \bar y \rangle$ is the bounded formula of :ref{#fact-pairing}. The first formula is bounded, and the second is $\Pi_n$ *logically*: the bounded universal quantifiers merge with the first universal block of $\theta$. Both have parameters in $M$, so they hold in $K$, by $M \preccurlyeq_n K$. Together they give $K \models \forall \bar x < a\ \exists \bar y\ \theta(\bar x, \bar y)$.

*Step 2: $M \preccurlyeq_{n+1} K$.* $\Sigma_{n+1}$ formulas go up: a witness in $M$ of the $\Pi_n$ part transfers by $M \preccurlyeq_n K$. They go down: if $M \models \neg \exists \bar y\ \eta(\bar y)$, with $\eta \in \Pi_n$, then $M \models \forall \bar y\ \neg \eta(\bar y)$, a $\Pi_{n+1}$ formula, which is in particular $\Pi_{n+2}$ and holds in $K$ by step 1.

*Step 3: $M \preccurlyeq_{n+2} K$.* A $\Sigma_{n+2}$ formula true in $M$ has a witness in $M$ for its $\Pi_{n+1}$ part, which transfers by step 2. If a $\Sigma_{n+2}$ formula fails in $M$, its negation, a $\Pi_{n+2}$ formula, holds in $M$ and hence in $K$ by step 1.
:::

:::figure[A cofinal extension $K$ of $M$. Every new element of $K$ lies below an element $a$ of $M$. A single code $s \in M$ lists witnesses $(s)_x$ for all $x < a$; the statement that it does is $\Pi_n$ about $s$ and $a$, and transfers to $K$, where it covers the new elements below $a$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="A cofinal extension K of M: every element of K lies below an element a of M; a code s in M lists witnesses for all x below a, including the new elements of K below a"><line x1="20.0" y1="70.0" x2="580.0" y2="70.0" class="ink-stroke" stroke-width="1.2"/><circle cx="40.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="90.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="150.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="220.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="300.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="380.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="460.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="540.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="120.0" cy="70.0" r="3" class="node"/><circle cx="185.0" cy="70.0" r="3" class="node"/><circle cx="260.0" cy="70.0" r="3" class="node"/><circle cx="340.0" cy="70.0" r="3" class="node"/><circle cx="420.0" cy="70.0" r="3" class="node"/><circle cx="500.0" cy="70.0" r="3" class="node"/><circle cx="380.0" cy="70.0" r="4" class="ink-fill"/><text x="380.0" y="56.0" text-anchor="middle" class="math" font-size="14">a</text><path d="M22,86 L22,92 L378,92 L378,86" class="muted-stroke" stroke-width="1.2"/><text x="200.0" y="110" text-anchor="middle" class="label">x &lt; a in K: the code s in M gives witnesses (s)ₓ</text><text x="300" y="142" text-anchor="middle" class="label">discs: elements of M; circles: new elements of K, each below some element of M</text></svg>
:::

:::quiz[preservation in cofinal extensions]
In step 1 of the proof of :ref{#thm-cofinal-preservation}, for $n \geq 1$, why is the code $s$ used, rather than transferring the formula $\forall x' < a\ \exists y < b\ \theta(x', y)$ given by collection?

- [x] The formula $\forall x' < a\ \exists y < b\ \theta(x', y)$ is $\Pi_n$ only modulo $\mathrm B\Sigma_n$, which holds in $M$ but is not known in $K$; its logical form, with $\exists y < b$ in front of a $\Pi_n$ formula, is not $\Pi_n$. With the code, the witness is named by $\langle x', y \rangle \in s$ under a bounded universal quantifier, and the formula is logically $\Pi_n$.
- [ ] Because collection does not hold in $M$.

  $M \models \mathrm B\Sigma_{n+1}$ by hypothesis; collection is used to bound the witnesses before coding them.
- [ ] Because $K$ is not a model of $\mathrm{PA}^-$.

  The argument does not use any axiom in $K$; that is the point of making the transferred formulas logically $\Pi_n$.
:::

Applying the theorem at each level gives a statement that starts from $\Sigma_0$-elementarity.

:::corollary{#cor-cofinal-preservation}
Let $M \subseteq_{cf} K$ with $M \preccurlyeq_0 K$.

1. If $k \geq 1$ and $M \models \mathrm B\Sigma_k$, then $M \preccurlyeq_{k+1} K$.
2. If $M \models \mathrm{PA}$, then $M \preccurlyeq K$; in particular $K \models \mathrm{PA}$.
:::

:::proof{of=cor-cofinal-preservation}
1. By induction on $j \leq k$, we show $M \preccurlyeq_{j+1} K$. For $j = 1$, apply :ref{#thm-cofinal-preservation} with $n = 0$, since $M \models \mathrm B\Sigma_1$. If $M \preccurlyeq_j K$ with $2 \leq j \leq k$, apply it with $n = j - 1$, since $M \models \mathrm B\Sigma_j$; this gives $M \preccurlyeq_{j+1} K$.

2. $\mathrm{PA}$ proves $\mathrm B\Sigma_k$ for every $k$ (:ref{#thm-fo-parsons}), so $M \preccurlyeq_{k+1} K$ for every $k$ by item 1.
:::

The bound of item 1 is optimal: Hájek and Pudlák (Remark IV.1.25) show that for every $k \geq 1$ there are $M \models \mathrm B\Sigma_k$ and $K \models \mathrm I\Sigma_1$ with $M \subseteq K$ such that $M$ is not a $\Sigma_{k+2}$-elementary substructure of $\sup_K M$.

## Collection for partial functions

Collection bounds the values of a definable function on $[0, a)$ that is *total* on $[0, a)$. **Strong collection** asks the same for partial functions: whatever subset of $[0, a)$ has witnesses, a single bound $b$ catches a witness for each of its elements. This is stronger, because the set of elements that have a witness may be more complex than its witnesses, and its strength is that of induction one level up.

:::theorem[Friedman]{#thm-strong-collection}
Let $n \geq 0$. Over $\mathrm I\Delta_0$, $\mathrm I\Sigma_{n+1}$ is equivalent to the **strong $\Pi_n$ collection** scheme: the universal closures of
$$
\exists b\ \forall x < a\ \big( \exists y\ \eta(x, y) \rightarrow \exists y < b\ \eta(x, y) \big)
$$
for $\eta \in \Pi_n$, with parameters.
:::

:::proof{of=thm-strong-collection}
*Induction gives strong collection.* Assume $\mathrm I\Sigma_{n+1}$; it contains $\mathrm I\Sigma_1$, hence $\mathrm{exp}$ (:ref{#prop-isigma1-exp}). By :ref{#thm-friedman-coded}, some $c$ codes $\{ x < a : \exists y\ \eta(x, y) \}$ below $a$. Then $\forall x < a\ \exists y\ (x \notin c \vee \eta(x, y))$: for $x \in c$ a witness exists, and otherwise any $y$ will do. The formula in parentheses is $\Pi_n$, hence $\Sigma_{n+1}$, and $\mathrm B\Sigma_{n+1}$, which $\mathrm I\Sigma_{n+1}$ proves (:ref{#thm-fo-parsons}), gives $b$ with $\forall x < a\ \exists y < b\ (x \notin c \vee \eta(x, y))$. If $x < a$ has a witness, then $x \in c$, and some $y < b$ satisfies $\eta(x, y)$.

*Strong collection gives induction*, by induction on $n$. Strong $\Pi_n$ collection contains strong $\Pi_{n-1}$ collection for $n \geq 1$, so the induction hypothesis gives $\mathrm I\Sigma_n$, hence $\mathrm B\Sigma_n$ if $n \geq 1$; for $n = 0$ we have $\mathrm I\Delta_0$. Let $\varphi(x) \equiv \exists y\ \eta(x, y)$ with $\eta \in \Pi_n$ (after contraction), and assume $\varphi(0)$, $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$ and $\neg \varphi(a)$. Strong collection gives $b$ with $\forall x < a + 1\ (\varphi(x) \rightarrow \exists y < b\ \eta(x, y))$. Let $\psi(x) \equiv \exists y < b\ \eta(x, y)$, which is bounded if $n = 0$ and $\Pi_n$ by :ref{#lem-fo-collection-closure} if $n \geq 1$. For $x \leq a$, $\varphi(x) \leftrightarrow \psi(x)$. Apply $\Pi_n$ induction (:ref{#thm-fo-isigma-ipi}), or bounded induction if $n = 0$, to $x \leq a \rightarrow \psi(x)$: it holds at $0$, and if $x + 1 \leq a$ and $\psi(x)$, then $\varphi(x)$, $\varphi(x + 1)$ and $\psi(x + 1)$. So $\psi(a)$, hence $\varphi(a)$, a contradiction.
:::

:::quiz[strong collection]
In the proof that induction gives strong collection, why is the set $\{ x < a : \exists y\ \eta(x, y) \}$ coded first, rather than applying collection directly?

- [x] Collection needs a witness for every $x < a$. The formula $\exists y\ \eta(x, y) \rightarrow \eta(x, y)$ would provide one, but it is $\Sigma_{n+1} \rightarrow \Pi_n$, that is, of complexity $\Pi_{n+1} \vee \Pi_n$, too high for $\mathrm B\Sigma_{n+1}$; replacing the hypothesis by the bounded formula $x \in c$ keeps the formula $\Pi_n$.
- [ ] Because $\mathrm I\Sigma_{n+1}$ does not prove $\mathrm B\Sigma_{n+1}$.

  It does, by Parsons' theorem; the issue is the complexity of the formula to which collection is applied.
- [ ] To make the bound $b$ smaller than $a$.

  No relation between $b$ and $a$ is claimed.
:::

The same theorem holds for strong $\Sigma_{n+1}$ collection, by contraction of quantifiers (Wong, Remark 6.5).

## Exercises

::::exercise{difficulty=2}
Let $M \models \mathrm B\Sigma_{n+1}$, $n \geq 0$, and let $K$ be a cofinal extension of $M$ with $M \preccurlyeq_n K$. Show that $K \models \mathrm I\Delta_0$ and that every $\Pi_{n+2}$ sentence true in $M$ is true in $K$. Why does this not show that $K \models \mathrm B\Sigma_{n+1}$?

:::solution
By :ref{#thm-cofinal-preservation}, $M \preccurlyeq_{n+2} K$. If a $\Pi_{n+2}$ sentence is true in $M$, its negation, a $\Sigma_{n+2}$ sentence, is false in $M$, hence false in $K$. $\mathrm I\Delta_0$ is equivalent to a set of $\Pi_1$ sentences (:ref{#lem-idelta0-pi1}), which are true in $M$ and therefore in $K$. An instance of $\Sigma_{n+1}$ collection, $\forall \bar p\ \forall a\ (\forall x < a\ \exists y\ \varphi \rightarrow \exists b\ \forall x < a\ \exists y < b\ \varphi)$ with $\varphi \in \Sigma_{n+1}$, is in general only a $\Pi_{n+3}$ sentence, beyond the reach of $\Sigma_{n+2}$-elementarity.
:::
::::

## Notes and references

The hierarchical Tarski–Vaught test is in Wong's Lecture 6 and in Hájek and Pudlák (Lemma IV.1.19). :ref{#thm-cofinal-preservation} combines Wong's Further exercises (b)–(d) to Lecture 6, where the case $n \geq 1$ is reduced to coding a witness function, and Hájek and Pudlák's Theorem IV.1.24, which proves the form of item 1 of :ref{#cor-cofinal-preservation} for the supremum of a model of $\mathrm B\Sigma_k$ in a model $K \supseteq M$ of $\mathrm I\Sigma_1$, obtaining $\Sigma_0$-elementarity from the MRDP theorem; for $\mathrm{PA}$ (their Remark IV.1.25) this is part of Gaifman's splitting theorem. :ref{#thm-strong-collection} is Wong's Theorem 6.4, attributed there to H. Friedman.

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 6.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 1(c).
- H. Gaifman, *A note on models and submodels of arithmetic*, in Conference in Mathematical Logic — London '70, Lecture Notes in Mathematics 255, Springer, 1972, 128–144.
