---
title: End extensions and Σ₁-completeness
summary: End extensions; bounded formulas are absolute between a model and its end extensions, Σ₁ formulas persist upwards and Π₁ formulas downwards; PA⁻ proves every Σ₁ sentence true in ℕ; non-standard models of PA with false Σ₁ sentences.
duration: 25
prerequisites: [pa-minus]
---

The standard part of a model of $\mathrm{PA}^-$ is an initial segment (:ref{#prop-standard-part}): a model of $\mathrm{PA}^-$ extends $\nat$ only at the top. This lesson isolates this situation, an **end extension**, and proves that it does not change the truth of bounded formulas. The reason is simple: a bounded quantifier with parameters in the smaller model only inspects elements below a value of a term, and these elements are the same in both models. Two consequences are used throughout the course: $\Sigma_1$ formulas persist from a model to its end extensions, and $\Pi_1$ formulas from a model to its initial segments. Applied to $\nat$, the first gives the $\Sigma_1$-completeness of $\mathrm{PA}^-$.

## End extensions and bounded formulas

:::definition{#def-end-extension}
Let $M$ and $N$ be $\mathcal L_A$-structures. $N$ is an **end extension** of $M$, written $M \subseteq_e N$, if $M$ is a substructure of $N$ and an initial segment of it: if $a \in M$, $b \in N$ and $N \models b < a$, then $b \in M$.
:::

By :ref{#prop-standard-part}, every model of $\mathrm{PA}^-$ is an end extension of $\nat$. End extensions do not change the truth of bounded formulas: for a bounded quantifier $\exists y < t(\bar a)$ with $\bar a$ in $M$, the value $t(\bar a)$ and all the candidates below it lie in $M$.

:::figure[A bounded quantifier in an end extension. The value $t(\bar a)$ of a term at parameters $\bar a$ in $M$ lies in $M$, and so do all the elements below it. The new elements of $N$ lie above $M$ and are never inspected by $\exists y < t(\bar a)$ or $\forall y < t(\bar a)$.]
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="An end extension: the model M is an initial segment of N; the candidates y below t(a) for a bounded quantifier with parameters a in M all lie in M"><line x1="20" y1="70" x2="580" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="24" cy="70" r="3.5" class="accent-fill"/><text x="24" y="58" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="110" cy="70" r="3.5" class="accent-fill"/><text x="110.0" y="58.0" text-anchor="middle" class="math" font-size="14">a</text><circle cx="270" cy="70" r="3.5" class="accent-fill"/><text x="270.0" y="58.0" text-anchor="middle" class="math" font-size="14">t(a)</text><circle cx="140" cy="70" r="2.5" class="node"/><circle cx="170" cy="70" r="2.5" class="node"/><circle cx="200" cy="70" r="2.5" class="node"/><circle cx="230" cy="70" r="2.5" class="node"/><circle cx="255" cy="70" r="2.5" class="node"/><path d="M130,46 L130,40 L262,40 L262,46" class="muted-stroke" stroke-width="1.2"/><text x="196.0" y="30" text-anchor="middle" class="label">candidates y &lt; t(a): all in M</text><line x1="340" y1="48" x2="340" y2="92" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><circle cx="420" cy="70" r="3.5" class="node"/><circle cx="470" cy="70" r="3.5" class="node"/><circle cx="520" cy="70" r="3.5" class="node"/><path d="M380,46 L380,40 L560,40 L560,46" class="muted-stroke" stroke-width="1.2"/><text x="470.0" y="30" text-anchor="middle" class="label">new elements of N</text><path d="M22,86 L22,92 L334,92 L334,86" class="muted-stroke" stroke-width="1.2"/><text x="178.0" y="110" text-anchor="middle" class="label">M: an initial segment of N</text><path d="M22,120 L22,126 L578,126 L578,120" class="muted-stroke" stroke-width="1.2"/><text x="300.0" y="144" text-anchor="middle" class="label">N</text></svg>
:::

:::lemma[Absoluteness of bounded formulas]{#lem-delta0-absolute}
Let $M \subseteq_e N$. For every $\Delta_0$ formula $\delta(\bar x)$ and every tuple $\bar a$ of elements of $M$, $M \models \delta(\bar a)$ if and only if $N \models \delta(\bar a)$.
:::

:::proof{of=lem-delta0-absolute}
By induction on $\delta$. Since $M$ is a substructure of $N$, every term has the same value at $\bar a$ in $M$ and in $N$, and atomic formulas have the same truth value. The induction steps for $\neg$, $\wedge$ and $\vee$ are immediate. Let $\delta = \exists y < t(\bar x)\ \psi(y, \bar x)$, and let $c = t(\bar a)$, an element of $M$. If $M \models \delta(\bar a)$, some $b \in M$ with $b < c$ satisfies $M \models \psi(b, \bar a)$, hence $N \models \psi(b, \bar a)$ by the induction hypothesis, and $N \models \delta(\bar a)$. Conversely, if $N \models \psi(b, \bar a)$ for some $b \in N$ with $b < c$, then $b \in M$ since $M$ is an initial segment of $N$, and $M \models \psi(b, \bar a)$ by the induction hypothesis. The bounded universal quantifier is the negation of a bounded existential one.
:::

:::quiz[absoluteness of bounded formulas]
In the proof of :ref{#lem-delta0-absolute}, where is it used that $M$ is an initial segment of $N$, and not only a substructure?

- [x] In the case $\exists y < t$, to know that a witness $b \in N$ below $t(\bar a)$ belongs to $M$.
- [ ] To know that $t(\bar a)$ has the same value in $M$ and in $N$.

  This only uses that $M$ is a substructure: the operations of $M$ are those of $N$ restricted.
- [ ] In the case of atomic formulas $s < t$.

  The order of $M$ is the restriction of the order of $N$; no initial segment condition is needed.
:::

The hypothesis that $M$ is an initial segment cannot be dropped.

:::example[A substructure that is not an initial segment]{#ex-not-end-extension}
In $\mathbb Z[X]^+$ (:ref{#ex-zx-plus}), let $M$ be the set of non-negative polynomials in $X^2$, that is, of the form $p(X^2)$. It contains $0$ and $1$ and is closed under addition and multiplication, so it is a substructure of $\mathbb Z[X]^+$; it is not an initial segment, since $X < X^2$ and $X \notin M$. The bounded formula $\exists y < x\ (y \cdot y = x)$ holds at $x = X^2$ in $\mathbb Z[X]^+$, with $y = X$. It fails at $X^2$ in $M$: if $p(X^2)^2 = X^2$, then $p(X^2)$ has degree $1$ in $X$, while every non-zero element of $M$ has even degree.
:::

:::corollary{#cor-sigma1-upward}
Let $M \subseteq_e N$ and $\bar a \in M$. If $\sigma(\bar x)$ is $\Sigma_1$ and $M \models \sigma(\bar a)$, then $N \models \sigma(\bar a)$. If $\pi(\bar x)$ is $\Pi_1$ and $N \models \pi(\bar a)$, then $M \models \pi(\bar a)$.
:::

:::proof{of=cor-sigma1-upward}
Write $\sigma = \exists \bar y\ \delta(\bar x, \bar y)$ with $\delta$ bounded. Witnesses $\bar b \in M$ with $M \models \delta(\bar a, \bar b)$ satisfy $N \models \delta(\bar a, \bar b)$ by :ref{#lem-delta0-absolute}. The statement for $\Pi_1$ formulas is the contrapositive, applied to the negation.
:::

The converse implications fail: a $\Sigma_1$ formula true in $N$ may have all its witnesses in $N \setminus M$. The exercise at the end of the lesson gives an example with $M = \nat$.

## Σ₁-completeness

Applied to $\nat \subseteq_e M$, the corollary gives the first theorem of the subject.

:::theorem[Σ₁-completeness]{#thm-sigma1-complete}
Every $\Sigma_1$ sentence true in $\nat$ holds in every model of $\mathrm{PA}^-$, and is therefore provable in $\mathrm{PA}^-$. Every $\Pi_1$ sentence true in some model of $\mathrm{PA}^-$ is true in $\nat$.
:::

:::proof{of=thm-sigma1-complete}
Let $M \models \mathrm{PA}^-$. By :ref{#prop-standard-part}, $\nat$ is isomorphic to an initial segment of $M$ that is a substructure, so we may assume $\nat \subseteq_e M$. A $\Sigma_1$ sentence true in $\nat$ is true in $M$ by :ref{#cor-sigma1-upward}; by the completeness theorem, it is provable in $\mathrm{PA}^-$. The second statement is the contrapositive of the first, applied to the negation of the $\Pi_1$ sentence.
:::

The theorem does not extend to $\Pi_1$ sentences. By Gödel's second incompleteness theorem, the consistency of Peano arithmetic, a $\Pi_1$ sentence true in $\nat$, is not provable even in Peano arithmetic. The model $\mathbb Z[X]^+$ of :ref{#ex-zx-plus} even fails the simple $\Pi_1$ sentence "every number is even or odd".

The theorem also produces non-standard models of Peano arithmetic in which false sentences hold. By Gödel's second incompleteness theorem, $\mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA})$ is consistent, and in any of its models the $\Sigma_1$ sentence $\neg \mathrm{Con}(\mathrm{PA})$, false in $\nat$, holds. Write $\neg \mathrm{Con}(\mathrm{PA})$ as $\exists p\ \delta(p)$ with $\delta$ bounded. A witness $p$ in such a model $M$, a code of a proof of a contradiction, is non-standard: if $p = \bar k^M$, then $\nat \models \delta(k)$ by :ref{#lem-delta0-absolute}, and $\neg \mathrm{Con}(\mathrm{PA})$ would be true. Equivalently, by the second part of :ref{#thm-sigma1-complete}, the $\Pi_1$ sentence $\mathrm{Con}(\mathrm{PA})$ fails in $M$ because a non-standard element witnesses its negation.

## Exercises

::::exercise{#ex-sigma1-not-down difficulty=1}
Give a $\Sigma_1$ sentence that is true in $\mathbb Z[X]^+$ and false in $\nat$. Deduce that the converse of the first statement of :ref{#cor-sigma1-upward} fails for the end extension $\nat \subseteq_e \mathbb Z[X]^+$.

:::solution
Let $\sigma \equiv \exists x\ \forall y < x + 1\ (x \neq y + y \wedge x \neq y + y + 1)$, the negation of "every number is even or odd". It is $\Sigma_1$, since its matrix is bounded. It holds in $\mathbb Z[X]^+$ with $x = X$ (:ref{#ex-zx-plus}), and it is false in $\nat$. Since $\nat \subseteq_e \mathbb Z[X]^+$ by :ref{#prop-standard-part}, $\sigma$ is a $\Sigma_1$ sentence true in an end extension of $\nat$ and false in $\nat$: its only witnesses are non-standard.
:::
::::

## Notes and references

Wong (Lecture 2) notes that $\mathrm{PA}^-$ proves all true $\Sigma_1$ sentences, with a reference to Kaye's book (Chapter 2). Hájek and Pudlák prove the $\Sigma_1$-completeness of Robinson's arithmetic $\mathsf Q$ (Theorem I.1.8).

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 2.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(a).
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991, Chapter 2.
