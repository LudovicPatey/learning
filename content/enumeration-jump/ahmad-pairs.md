---
title: Ahmad pairs and the two-quantifier theory
summary: The two-quantifier theory of the local structure and the extension of embeddings problem; Ahmad pairs, where everything below one degree is below another, obstruct extensions; the left half of an Ahmad pair is join-irreducible and the two halves are incomparable; no symmetric pairs, no cupping pairs, no triples; the characterization of the left halves as the low₃ join-irreducible degrees (Ravishankar, 2025).
duration: 15
prerequisites: [enumeration-jump]
---

The existential theory of the local structure $\mathcal D_e(\leq \mathbf 0'_e)$ is decidable, since every finite partial order embeds into it, and its three-quantifier theory is undecidable (Kent). In between, the decidability of the two-quantifier theory is open, and it is one of the main open problems on the enumeration degrees. A two-quantifier sentence asks whether every embedding of a finite partial order $P$ extends to an embedding of one of finitely many extensions $Q_1, \ldots, Q_k$ of $P$; the case $k = 1$, the extension of embeddings problem, was solved by Lempp, Slaman and Sorbi. The obstructions to extending embeddings are configurations in which the degrees below one element are controlled by another. The simplest of them was found by Ahmad.

## Ahmad pairs

:::definition[Ahmad]{#def-ahmad-pair}
Two $\Sigma^0_2$ enumeration degrees $\mathbf a$ and $\mathbf b$ form an **Ahmad pair** if $\mathbf a \not\leq \mathbf b$ and every degree $\mathbf x < \mathbf a$ satisfies $\mathbf x \leq \mathbf b$.
:::

If $\mathbf a$ and $\mathbf b$ form an Ahmad pair, the embedding of the two-element antichain $P = \{ u, v \}$ that sends $u$ to $\mathbf a$ and $v$ to $\mathbf b$ does not extend to an embedding of the order $Q$ obtained by adding an element below $u$ and not below $v$.

:::proposition{#prop-ahmad-basic}
Let $\mathbf a$ and $\mathbf b$ form an Ahmad pair. Then $\mathbf a$ is join-irreducible: it is not the join of two degrees strictly below it. Moreover $\mathbf b \not\leq \mathbf a$, so the two degrees are incomparable.
:::

:::proof{of=prop-ahmad-basic}
If $\mathbf a = \mathbf c \vee \mathbf d$ with $\mathbf c, \mathbf d < \mathbf a$, then $\mathbf c, \mathbf d \leq \mathbf b$ by definition, so $\mathbf a \leq \mathbf b$, which is excluded. Suppose $\mathbf b \leq \mathbf a$; then $\mathbf b < \mathbf a$, since $\mathbf a \not\leq \mathbf b$. By Cooper's density theorem for the local structure, there is $\mathbf x$ with $\mathbf b < \mathbf x < \mathbf a$; then $\mathbf x \leq \mathbf b$ by definition, a contradiction.
:::

Join-irreducibility is already a difference with the c.e. Turing degrees, which are all join-reducible by the Sacks splitting theorem.

:::quiz[Ahmad pairs]
Why does an Ahmad pair obstruct the extension of embeddings?

- [x] An extension would need a degree below $\mathbf a$ and not below $\mathbf b$, and the definition says there is none.
- [ ] Because $\mathbf a$ and $\mathbf b$ have no common lower bound.

  They have many: every degree below $\mathbf a$ is a common lower bound.
- [ ] Because $\mathbf a$ is join-irreducible.

  Join-irreducibility is a consequence; the obstruction is the definition itself.
:::

## What is known

The following results are admitted.
- **Existence and asymmetry** (Ahmad, 1989, with Lachlan). Ahmad pairs exist, and there is no symmetric Ahmad pair: if $\mathbf a$ and $\mathbf b$ form one, then $\mathbf b$ and $\mathbf a$ do not.
- **No cupping** (Kalimullin, Lempp, Ng, Yamaleev). If $\mathbf a$ and $\mathbf b$ form an Ahmad pair, then $\mathbf a \vee \mathbf b < \mathbf 0'_e$.
- **No triples** (Goh, Lempp, Ng, Soskova). There are no $\Sigma^0_2$ degrees $\mathbf a$, $\mathbf b$, $\mathbf c$ such that $\mathbf a, \mathbf b$ and $\mathbf b, \mathbf c$ are both Ahmad pairs; the proof is a priority argument relative to $\emptyset'''$.
- **Characterization** (Ravishankar, preprint, 2025). A $\Sigma^0_2$ degree is the left half of an Ahmad pair if and only if it is low₃ and join-irreducible, and every right half is high₂. The non-existence of triples follows, since a degree cannot be both low₃ and high₂. The characterization gives a $\Pi_3$ definition of the low₃ degrees in the local structure, much simpler than the general definitions of the jump classes by Ganchev and Soskova, and extends to a hierarchy of Ahmad $n$-pairs.

These results bear on the two-quantifier theory, whose decidability remains open; Goh, Lempp, Ng and Soskova are studying the extensions of embeddings of finite antichains by one point, a first step. For the global structure, Lempp, Slaman and Soskova proved that every finite distributive lattice embeds as an interval $[\mathbf a, \mathbf b]$ such that every degree below $\mathbf b$ lies in the interval or below $\mathbf a$; it follows that the extension of embeddings problem for $\mathcal D_e$ is decidable and that its three-quantifier theory is undecidable.

::::exercise{#ex-ahmad-not-zero difficulty=1 objective="Check the elementary properties of the halves of an Ahmad pair."}
Let $\mathbf a$ and $\mathbf b$ form an Ahmad pair. Show that $\mathbf a \neq \mathbf 0_e$ and $\mathbf b \neq \mathbf 0_e$.

:::solution
$\mathbf a \not\leq \mathbf b$, while $\mathbf 0_e \leq \mathbf b$, so $\mathbf a \neq \mathbf 0_e$. By density (or by Gutteridge's theorem, there are no minimal degrees), there is $\mathbf x$ with $\mathbf 0_e < \mathbf x < \mathbf a$; then $\mathbf x \leq \mathbf b$, so $\mathbf b \neq \mathbf 0_e$.
:::
::::

## Notes and references

Ahmad pairs were found by Ahmad in her thesis (Simon Fraser University, 1989), with Lachlan. The results above are from the papers below; Ravishankar's paper, which credits Soskova's 2025 notes on the enumeration degrees, is a recent preprint and has not yet been refereed.

- S. Ahmad and A. H. Lachlan, *Some special pairs of Σ₂ e-degrees*, Mathematical Logic Quarterly 44 (1998), 431–449.
- I. Sh. Kalimullin, S. Lempp, K. M. Ng and M. M. Yamaleev, *On cupping and Ahmad pairs*, Journal of Symbolic Logic.
- K. Ravishankar, *Contrasting the halves of an Ahmad pair*, arXiv:2511.22901, 2025.
- S. Lempp, T. A. Slaman and M. I. Soskova, *Fragments of the theory of the enumeration degrees*, preprint.
- S. Lempp, T. A. Slaman and A. Sorbi, *On extensions of embeddings into the enumeration degrees of the Σ⁰₂-sets*, Journal of Mathematical Logic 5 (2005), 247–298.

:::::exercises
::::exercise{#ex-ahmad-not-k-pair difficulty=1 objective="Contrast Ahmad pairs with Kalimullin pairs."}
Show that two $\Sigma^0_2$ degrees forming a K-pair do not form an Ahmad pair.

:::solution
Suppose $\mathbf a$ and $\mathbf b$ form a K-pair and an Ahmad pair. By :ref{#thm-kalimullin-pairs} with $\mathbf x = \mathbf 0_e$, their meet is $\mathbf 0_e$. Every $\mathbf x < \mathbf a$ is below $\mathbf b$, hence below the meet, so $\mathbf x = \mathbf 0_e$. Since $\mathbf a \neq \mathbf 0_e$, $\mathbf a$ would be a minimal degree, contradicting :ref{#thm-gutteridge}.
:::
::::

::::exercise{#ex-ahmad-upward difficulty=1 objective="See that the right half of an Ahmad pair can be raised."}
Let $\mathbf a$ and $\mathbf b$ form an Ahmad pair, and let $\mathbf c \leq \mathbf 0'_e$ with $\mathbf b \leq \mathbf c$ and $\mathbf a \not\leq \mathbf c$. Show that $\mathbf a$ and $\mathbf c$ form an Ahmad pair.

:::solution
$\mathbf a \not\leq \mathbf c$ by hypothesis, and every $\mathbf x < \mathbf a$ satisfies $\mathbf x \leq \mathbf b \leq \mathbf c$. Both degrees are $\Sigma^0_2$, being below $\mathbf 0'_e$.
:::
::::

:::::
