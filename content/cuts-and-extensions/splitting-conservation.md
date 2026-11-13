---
title: The splitting theorem and conservation
summary: Every Σₙ₊₁-elementary extension of a model of IΣₙ splits into a Σₙ₊₁-elementary cofinal extension followed by a Σₙ-elementary end extension; every model of IΣₙ has a Σₙ₊₁-elementary cofinal extension satisfying BΣₙ₊₁; BΣₙ₊₁ is Πₙ₊₂-conservative over IΣₙ (Friedman, Paris).
duration: 35
prerequisites: [collection-end-extensions]
---

This lesson shows that, for a $\Sigma_{n+1}$-elementary extension of a model of $\mathrm I\Sigma_n$, both parts of its decomposition at the supremum of the small model keep some elementarity: this is the splitting theorem, whose end part is proved with strong collection (:ref{#thm-strong-collection}). Combined with the theorem of Paris and Kirby (:ref{#thm-end-ext-collection}), it gives a conservation theorem: $\mathrm B\Sigma_{n+1}$ proves no more $\Pi_{n+2}$ sentences than $\mathrm I\Sigma_n$. The proof builds, for a model of $\mathrm I\Sigma_n$, an elementary extension, splits it at the supremum of the model, and recognizes the middle model as a model of collection.

## The splitting theorem

Every extension $M \subseteq K$ factors as $M \subseteq_{cf} \sup_K M \subseteq_e K$ (:ref{#def-cofinal-ext}). When the extension is elementary enough and $M$ satisfies enough induction, each part keeps some elementarity.

:::theorem[Splitting]{#thm-splitting}
Let $n \geq 0$, let $M$ be a model of $\mathrm I\Sigma_n$, and $K$ a structure with $M \preccurlyeq_{n+1} K$. Let $\bar M = \sup_K M$. Then
$$
M \preccurlyeq_{n+1} \bar M, \qquad M \subseteq_{cf} \bar M, \qquad \bar M \preccurlyeq_n K, \qquad \bar M \subseteq_e K.
$$
:::

The end part is handled by the Tarski–Vaught test. A $\Pi_{n-1}$ property with a witness in $K$ and a parameter $c \in \bar M$ must have a witness in $\bar M$: take $a \in M$ above $c$; strong collection in $M$ gives one bound $b \in M$ for the witnesses of all $x < a$ that have one; this statement transfers to $K$, and then the witness for $c$ in $K$ can be taken below $b$, hence in $\bar M$. Strong collection is needed because some $x < a$ may have no witness.

:::proof{of=thm-splitting}
As noted after :ref{#def-cofinal-ext}, $\bar M$ is a substructure of $K$, $M \subseteq_{cf} \bar M$ and $\bar M \subseteq_e K$; so $\bar M \preccurlyeq_0 K$ by :ref{#lem-delta0-absolute}.

*$\bar M \preccurlyeq_n K$.* For $n = 0$ this is the previous sentence. Let $n = m + 1$. We apply :ref{#lem-tarski-vaught-n}. Let $\eta(x, \bar y)$ be a $\Pi_m$ formula without parameters, $c \in \bar M$, and suppose $K \models \exists \bar y\ \eta(c, \bar y)$; parameters from $\bar M$ can be gathered into $c$ by pairing, since $\bar M$ is closed under the operations. Take $a \in M$ with $c < a$. By :ref{#thm-strong-collection}, applied in $M \models \mathrm I\Sigma_{m+1}$ after contracting $\bar y$ to one variable, there is $b \in M$ with
$$
M \models \forall x < a\ \big( \exists \bar y\ \eta(x, \bar y) \rightarrow \exists \bar y < b\ \eta(x, \bar y) \big).
$$
The formula after $\forall x < a$ is the disjunction of a $\Pi_{m+1}$ and a $\Sigma_{m+1}$ formula, so the whole formula is logically $\Pi_{m+2} = \Pi_{n+1}$, with parameters $a, b \in M$. It holds in $K$, by $M \preccurlyeq_{n+1} K$. Since $c < a$ and $K \models \exists \bar y\ \eta(c, \bar y)$, some $\bar y < b$ satisfies $\eta(c, \bar y)$ in $K$, and these elements are in $\bar M$.

*$M \preccurlyeq_{n+1} \bar M$.* For $\Sigma_n$ formulas with parameters in $M$, truth in $M$, in $K$ and in $\bar M$ agree, by $M \preccurlyeq_{n+1} K$ and $\bar M \preccurlyeq_n K$. Let $\eta$ be $\Pi_n$ with parameters in $M$. If $M \models \exists \bar y\ \eta(\bar y)$, a witness in $M$ satisfies $\eta$ in $\bar M$. If $\bar M \models \eta(\bar d)$ with $\bar d \in \bar M$, then $K \models \eta(\bar d)$ by $\bar M \preccurlyeq_n K$, so $K \models \exists \bar y\ \eta(\bar y)$, and $M \models \exists \bar y\ \eta(\bar y)$ by $M \preccurlyeq_{n+1} K$.
:::

:::figure[The splitting theorem. The supremum $\bar M$ of $M$ in $K$ consists of the elements of $K$ below some element of $M$. $M$ is cofinal in $\bar M$, and $\bar M$ is an initial segment of $K$.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="The splitting theorem: M is cofinal in its supremum in K, which is an initial segment of K"><line x1="20.0" y1="70.0" x2="580.0" y2="70.0" class="ink-stroke" stroke-width="1.2"/><circle cx="40.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="100.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="170.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="240.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="300.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="346.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="70.0" cy="70.0" r="3" class="node"/><circle cx="135.0" cy="70.0" r="3" class="node"/><circle cx="205.0" cy="70.0" r="3" class="node"/><circle cx="270.0" cy="70.0" r="3" class="node"/><circle cx="325.0" cy="70.0" r="3" class="node"/><line x1="360.0" y1="48.0" x2="360.0" y2="92.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><circle cx="420.0" cy="70.0" r="3" class="node"/><circle cx="480.0" cy="70.0" r="3" class="node"/><circle cx="540.0" cy="70.0" r="3" class="node"/><path d="M22,86 L22,92 L354,92 L354,86" class="muted-stroke" stroke-width="1.2"/><text x="188.0" y="110" text-anchor="middle" class="label">M̄ = sup_K M: below some element of M</text><path d="M22,122 L22,128 L578,128 L578,122" class="muted-stroke" stroke-width="1.2"/><text x="300.0" y="146" text-anchor="middle" class="label">K</text><path d="M366,50 L366,44 L578,44 L578,50" class="muted-stroke" stroke-width="1.2"/><text x="472.0" y="34" text-anchor="middle" class="label">K ∖ M̄: above all of M</text><path d="M22,50 L22,44 L354,44 L354,50" class="muted-stroke" stroke-width="1.2"/><text x="188.0" y="34" text-anchor="middle" class="label">M (discs) is cofinal in M̄</text></svg>
:::

:::quiz[the splitting theorem]
In the proof that $\bar M \preccurlyeq_n K$, why is strong collection used instead of collection?

- [x] Some $x < a$ may have no witness for $\eta$; ordinary collection applies only when every $x < a$ has one, while strong collection bounds the witnesses of those $x$ that have one.
- [ ] Because $M$ does not satisfy $\mathrm B\Sigma_n$.

  $M \models \mathrm I\Sigma_n$, which proves $\mathrm B\Sigma_n$; ordinary collection is available but does not apply to a partial function.
- [ ] To make the transferred formula $\Pi_{n+1}$.

  The complexity comes from the shape of the implication; strong collection is what makes the implication true in $M$ for a single $b$.
:::

## Cofinal extensions satisfying collection, and conservation

:::theorem[Friedman, Paris]{#thm-cofinal-bsigma}
Let $n \geq 0$ and $M$ a model of $\mathrm I\Sigma_n$. There is a model $\bar M$ of $\mathrm B\Sigma_{n+1}$ with $M \subseteq_{cf} \bar M$ and $M \preccurlyeq_{n+1} \bar M$.
:::

:::proof{of=thm-cofinal-bsigma}
Let $d$ be a new constant. Every finite part of the elementary diagram of $M$ together with the sentences $d > m$, $m \in M$, is satisfied in $M$ by a large enough element; by compactness there is $K$ with $M \preccurlyeq K$ and an element $d \in K$ above every element of $M$. Then $K \models \mathrm I\Sigma_n$. Let $\bar M = \sup_K M$. By :ref{#thm-splitting}, $M \preccurlyeq_{n+1} \bar M$, $M \subseteq_{cf} \bar M$, $\bar M \preccurlyeq_n K$ and $\bar M \subseteq_e K$, and $\bar M \neq K$ since $d \notin \bar M$. The structure $\bar M$ is a model of $\mathrm{PA}^-$, being a cut of $K$ closed under the operations (:ref{#lem-cut-model}). By :ref{#thm-end-ext-collection}, $\bar M \models \mathrm B\Sigma_{n+1}$.
:::

The proof shows more: if $M \models \mathrm I\Sigma_n$, $M \preccurlyeq_{n+1} K$, $K \models \mathrm I\Sigma_n$ and $M$ is not cofinal in $K$, then $\sup_K M$ satisfies $\mathrm B\Sigma_{n+1}$. The hypothesis $K \models \mathrm I\Sigma_n$ is automatic when $K$ is an elementary extension, as here. It can in fact be dropped: a $\Sigma_{n+1}$ sentence true in $M$ is true in $K$, so $\Pi_{n+1}$ sentences true in $M$ hold in $K$; for $n = 0$ this gives $K \models \mathrm I\Delta_0$, which suffices in :ref{#thm-end-ext-collection}, and for $n \geq 1$ it gives $K \models \mathrm I\Sigma_{n-1}$, which is axiomatized by $\Pi_{n+1}$ sentences and suffices by the theorem of Adamowicz, Clote and Wilkie recalled after :ref{#fact-end-ext-converse}.

:::theorem[Friedman, Paris]{#thm-friedman-paris-conservation}
Let $n \geq 0$. Every $\Pi_{n+2}$ sentence provable in $\mathrm B\Sigma_{n+1}$ is provable in $\mathrm I\Sigma_n$.
:::

:::proof{of=thm-friedman-paris-conservation}
Let $\sigma$ be a $\Pi_{n+2}$ sentence not provable in $\mathrm I\Sigma_n$, and $M \models \mathrm I\Sigma_n + \neg \sigma$. The sentence $\neg \sigma$ is $\exists \bar x\ \pi(\bar x)$ with $\pi \in \Pi_{n+1}$; let $\bar c \in M$ with $M \models \pi(\bar c)$. Let $\bar M$ be given by :ref{#thm-cofinal-bsigma}. Then $\bar M \models \pi(\bar c)$, by $M \preccurlyeq_{n+1} \bar M$, so $\bar M$ is a model of $\mathrm B\Sigma_{n+1} + \neg \sigma$, and $\mathrm B\Sigma_{n+1}$ does not prove $\sigma$.
:::

:::quiz[conservation]
Why does the proof give conservation for $\Pi_{n+2}$ sentences and not for $\Pi_{n+3}$ sentences?

- [x] The extension $\bar M$ is only $\Sigma_{n+1}$-elementary: it preserves the $\Sigma_{n+2}$ sentence $\neg \sigma$, whose witness is in $M$ and whose matrix is $\Pi_{n+1}$, but not $\Sigma_{n+3}$ sentences in general.
- [ ] Because the compactness argument only gives a $\Sigma_{n+1}$-elementary extension $K$.

  $K$ is a fully elementary extension of $M$; elementarity is lost when passing to $\bar M$.
- [ ] Because $\mathrm I\Sigma_n$ is axiomatized by $\Pi_{n+2}$ sentences.

  This is true but plays no role in the argument.
:::

The conservation theorem is sharp, as the second exercise shows. For $n = 0$ it says that $\mathrm B\Sigma_1$ is $\Pi_2$-conservative over $\mathrm I\Delta_0$; with :ref{#thm-fo-paris-kirby}, $\mathrm B\Sigma_{n+1}$ and $\mathrm I\Sigma_n$ are equiconsistent, since $0 = 1$ is a $\Pi_{n+2}$ sentence. Many proofs are known: Paris's original proof used a hierarchy of cuts, and others use definable ultrapowers, Skolem hulls, or proof theory (Wong, Further comments to Lecture 6).

## Exercises

::::exercise{#ex-sup-elementary difficulty=1}
Let $M \preccurlyeq K$ be models of $\mathrm{PA}$. Show that $M \preccurlyeq \sup_K M \preccurlyeq K$.

:::solution
For every $n$, $M \models \mathrm I\Sigma_n$ and $M \preccurlyeq_{n+1} K$, so :ref{#thm-splitting} gives $M \preccurlyeq_{n+1} \sup_K M$ and $\sup_K M \preccurlyeq_n K$. Since $n$ is arbitrary, both extensions are elementary.
:::
::::

::::exercise{#ex-conservation-sharp difficulty=2}
Using the strictness of the hierarchy of induction and collection (the lesson :ref{to="fragments-of-arithmetic/induction-collection"}), show that $\mathrm B\Sigma_{n+1}$ is not $\Pi_{n+3}$-conservative over $\mathrm I\Sigma_n$.

:::solution
By :ref{#ex-fo-bsigma-bpi} for $n \geq 1$, and by contraction of quantifiers for $n = 0$, $\mathrm B\Sigma_{n+1}$ is equivalent over $\mathrm I\Delta_0$ to the collection scheme for $\Pi_n$ formulas. An instance of the latter is the universal closure of
$$
\exists x < a\ \forall y\ \neg \varphi(x, y) \;\vee\; \exists b\ \forall x < a\ \exists y < b\ \varphi(x, y), \qquad \varphi \in \Pi_n.
$$
The first disjunct is logically $\Sigma_{n+2}$. In the second, $\forall x < a\ \exists y < b\ \varphi$ is bounded if $n = 0$, and equivalent to a $\Pi_n$ formula in $\mathrm B\Sigma_n$, hence in $\mathrm I\Sigma_n$, if $n \geq 1$ (:ref{#lem-fo-collection-closure}); so the second disjunct is $\Sigma_{n+1}$ in $\mathrm I\Sigma_n$. Hence $\mathrm I\Sigma_n$ proves each instance equivalent to a $\Pi_{n+3}$ sentence $\sigma$, which $\mathrm B\Sigma_{n+1}$ proves. If $\mathrm B\Sigma_{n+1}$ were $\Pi_{n+3}$-conservative over $\mathrm I\Sigma_n$, then $\mathrm I\Sigma_n$ would prove every such $\sigma$, hence every instance, and $\mathrm I\Sigma_n$ would prove $\mathrm B\Sigma_{n+1}$. This contradicts the existence of a model of $\mathrm I\Sigma_n$ in which $\mathrm B\Sigma_{n+1}$ fails.
:::
::::

## Notes and references

The splitting theorem is Wong's, "essentially Kaye", with the proof of Enayat and Mohsenipour that uses :ref{#thm-strong-collection}; for models of $\mathrm{PA}$ without any initial elementarity, Gaifman's splitting theorem gives $M \preccurlyeq \sup_K M$ (Hájek and Pudlák, Remark IV.1.25; Wong, Further exercises to Lecture 6). :ref{#thm-cofinal-bsigma} is Wong's Theorem 6.6 and Theorem IV.1.61 of Hájek and Pudlák, who prove it by a definable ultrapower; Wong notes that its countable version first appeared in Paris (1980), who reports that Friedman found it independently. :ref{#thm-friedman-paris-conservation} is Wong's Theorem 6.1 and Theorem IV.1.59 of Hájek and Pudlák; Friedman never published his proof (Hájek and Pudlák, bibliographical remarks to Chapter IV).

- J. B. Paris, *A hierarchy of cuts in models of arithmetic*, in Model Theory of Algebra and Arithmetic, Lecture Notes in Mathematics 834, Springer, 1980, 312–337.
- R. Kaye, *Model-theoretic properties characterizing Peano arithmetic*, Journal of Symbolic Logic 56 (1991), 949–963.
- A. Enayat and S. Mohsenipour, *Model theory of the regularity and reflection schemes*, Archive for Mathematical Logic 47 (2008), 447–464.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 6.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Sections 1(c) and 1(f).
