---
title: Π¹₁-randomness
summary: Randomness with respect to all null Π¹₁ classes; the Sacks–Tanaka theorem that almost no sequence computes a non-computable ordinal; the characterization of Π¹₁-randomness by Chong, Nies and Yu; Σ¹₁-randomness coincides with Δ¹₁-randomness; the largest null Π¹₁ class.
duration: 40
prerequisites: [higher-tests, descriptive-set-theory/uniformization]
---

Taking all null $\Pi^1_1$ classes as tests gives a randomness notion without classical analogue: there is no reason, in the arithmetic world, to consider null classes that are not Borel. The $\Pi^1_1$ classes are measurable by Lusin's theorem, and the null ones capture a phenomenon of a new kind: computing a non-computable ordinal is atypical. This lesson shows that $\Pi^1_1$-randomness is exactly $\Delta^1_1$-randomness combined with this ordinal condition.

## Definitions and the Sacks–Tanaka theorem

:::definition{#def-pi11-random}
A sequence is **$\Pi^1_1$-random** if it belongs to no null $\Pi^1_1$ class, and **$\Sigma^1_1$-random** if it belongs to no null $\Sigma^1_1$ class.
:::

The definition makes sense by :ref{#fact-higher-borel} (4). Every null $\Delta^1_1$ class is $\Pi^1_1$ and $\Sigma^1_1$, and the class captured by the universal higher test is a null $\Pi^1_1$ class (:ref{#cor-higher-mlr-class}). So
$$
\Pi^1_1\text{-random} \;\Rightarrow\; \Pi^1_1\text{-Martin-Löf random} \;\Rightarrow\; \Delta^1_1\text{-random}, \qquad \Sigma^1_1\text{-random} \;\Rightarrow\; \Delta^1_1\text{-random}.
$$

The analysis of $\Pi^1_1$ classes uses their decomposition along the ordinals. We admit the following form of it, which is the relativization to the members $Y$ of the class of the stages of the previous course, combined with :ref{#fact-higher-borel} (Sacks, *Higher Recursion Theory*, Section I.5 and Chapter IV).

:::fact{#fact-pi11-stages}
For every $\Pi^1_1$ class $\mathcal A$, there is an index $h$ such that, writing $\mathcal A_a = \mathcal D_{a, h}$ for $a \in \mathcal O$:

1. $\mathcal A_a \subseteq \mathcal A$, and $\mathcal A_a$ only depends on $|a|$; we write $\mathcal A_{|a|}$. These classes increase with $|a|$.
2. If $Y \in \mathcal A$ and $\omega_1^Y = \omega_1^{\mathrm{CK}}$, then $Y \in \mathcal A_\alpha$ for some $\alpha < \omega_1^{\mathrm{CK}}$.
:::

In words: a member $Y$ of a $\Pi^1_1$ class enters it at a stage below $\omega_1^Y$, and the members entering before a computable stage form a $\Delta^1_1$ class. The following theorem is the higher analogue of Sacks' theorem that almost no sequence computes a given non-computable set.

:::theorem[Sacks, Tanaka]{#thm-sacks-tanaka}
The class $\mathcal C = \{ Y : \omega_1^Y > \omega_1^{\mathrm{CK}} \}$ is $\Pi^1_1$ and null.
:::

We admit this theorem (Sacks 1969, Tanaka 1967; Sacks, *Higher Recursion Theory*, Section IV.1). The idea of the proof is as follows. A sequence $Y$ with $\omega_1^Y > \omega_1^{\mathrm{CK}}$ computes a sequence of notations, relative to $Y$, whose ordinals are cofinal in $\omega_1^{\mathrm{CK}}$. If a positive measure of sequences did so with a fixed functional, the stage at which a measure close to the total is reached would define a total $\Pi^1_1$ function from numbers to computable ordinals, hence a hyperarithmetic one by :ref{#cor-total-pi11}; its values would be bounded below $\omega_1^{\mathrm{CK}}$ by the boundedness theorem, a contradiction.

## The characterization of Chong, Nies and Yu

:::theorem[Chong, Nies, Yu]{#thm-chong-nies-yu}
A sequence $X$ is $\Pi^1_1$-random if and only if it is $\Delta^1_1$-random and $\omega_1^X = \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=thm-chong-nies-yu}
($\Rightarrow$) A $\Pi^1_1$-random sequence avoids the null $\Delta^1_1$ classes, and the null $\Pi^1_1$ class $\mathcal C$ of :ref{#thm-sacks-tanaka}.

($\Leftarrow$) Let $X$ be $\Delta^1_1$-random with $\omega_1^X = \omega_1^{\mathrm{CK}}$, and let $\mathcal A$ be a null $\Pi^1_1$ class. Suppose $X \in \mathcal A$. By :ref{#fact-pi11-stages} (2), $X \in \mathcal A_\alpha$ for some $\alpha < \omega_1^{\mathrm{CK}}$. The class $\mathcal A_\alpha$ is $\Delta^1_1$, and null since it is included in $\mathcal A$. This contradicts the $\Delta^1_1$-randomness of $X$.
:::

So the only new obstacle to randomness, beyond the hyperarithmetic null classes, is the ability to compute a non-computable ordinal. For instance, $\mathcal O$ computes all computable ordinals, and $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$; by the corollary below, a $\Pi^1_1$-random sequence is not even hyperarithmetically above $\mathcal O$.

:::corollary{#cor-pi11-random-class}
1. The union of all null $\Pi^1_1$ classes is null: almost every sequence is $\Pi^1_1$-random.
2. There is a $\Pi^1_1$-random sequence $X$, and no such sequence computes $\mathcal O$.
:::

:::proof{of=cor-pi11-random-class}
1. By :ref{#thm-chong-nies-yu}, the union is the union of the countably many null $\Delta^1_1$ classes and of $\mathcal C$, which are null.
2. By item 1, the class of $\Pi^1_1$-random sequences has measure $1$, hence is non-empty. Suppose $X$ computes $\mathcal O$. The set $\mathrm{WO}$ of indices of computable well-orderings is many-one reducible to $\mathcal O$, which is $\Pi^1_1$-complete (:ref{to="computable-ordinals/trees-and-pi11"}), so $X$ computes $\mathrm{WO}$. Then $X$ computes the ordered sum of the orderings $L_e$ for $e \in \mathrm{WO}$, taken in the order of the indices: a well-ordering whose type is at least every computable ordinal, hence at least $\omega_1^{\mathrm{CK}}$. So $\omega_1^X > \omega_1^{\mathrm{CK}}$, and $X$ is not $\Pi^1_1$-random by :ref{#thm-chong-nies-yu}.
:::

The union of the null $\Pi^1_1$ classes is itself $\Pi^1_1$: there is a **largest null $\Pi^1_1$ class**, a result of Kechris (1975) and of Hjorth and Nies. This uses a uniform enumeration of the null $\Delta^1_1$ classes, and is admitted. It contrasts with Martin-Löf randomness, where the universal test plays this role, and with $\Delta^1_1$-randomness, for which the union of the null $\Delta^1_1$ classes is not $\Delta^1_1$.

:::quiz[the characterization]
In the proof of :ref{#thm-chong-nies-yu}, where is the hypothesis $\omega_1^X = \omega_1^{\mathrm{CK}}$ used?

- [x] To know that $X$ enters the $\Pi^1_1$ class at a computable stage, so that it belongs to a $\Delta^1_1$ part of the class, which is null.
- [ ] To show that $\mathcal A$ is null.

  $\mathcal A$ is null by hypothesis.
- [ ] To show that $X$ is $\Delta^1_1$-random.

  This is the other hypothesis.

---

Why does the class $\mathcal C$ have to be excluded separately?

- [x] Because a sequence with $\omega_1^Y > \omega_1^{\mathrm{CK}}$ may enter a null $\Pi^1_1$ class only at a stage $\geq \omega_1^{\mathrm{CK}}$, where the parts of the class are no longer $\Delta^1_1$; $\Delta^1_1$-randomness does not exclude this.
- [ ] Because $\mathcal C$ is not $\Pi^1_1$.

  It is $\Pi^1_1$ and null, by :ref{#thm-sacks-tanaka}.
- [ ] Because $\mathcal C$ contains every hyperarithmetic sequence.

  Hyperarithmetic sequences $Y$ have $\omega_1^Y = \omega_1^{\mathrm{CK}}$.
:::

## Σ¹₁-randomness

:::theorem[Sacks]{#thm-sigma11-random}
Every null $\Sigma^1_1$ class is contained in a null $\Delta^1_1$ class. Hence $\Sigma^1_1$-randomness coincides with $\Delta^1_1$-randomness.
:::

:::proof{of=thm-sigma11-random}
Let $\mathcal S$ be a null $\Sigma^1_1$ class, and $\mathcal A = \cs \setminus \mathcal S$, a $\Pi^1_1$ class of measure $1$, with parts $\mathcal A_\alpha$ given by :ref{#fact-pi11-stages}. For $\alpha < \omega_1^{\mathrm{CK}}$, let $\mathcal E_\alpha = \cs \setminus \mathcal A_\alpha$, a $\Delta^1_1$ class containing $\mathcal S$, decreasing in $\alpha$.

*The measures tend to $0$.* If $Y$ belongs to $\mathcal E_\alpha$ for every $\alpha < \omega_1^{\mathrm{CK}}$, then either $Y \in \mathcal S$, or $Y \in \mathcal A$ and, by :ref{#fact-pi11-stages} (2), $\omega_1^Y > \omega_1^{\mathrm{CK}}$. So $\bigcap_{\alpha < \omega_1^{\mathrm{CK}}} \mathcal E_\alpha \subseteq \mathcal S \cup \mathcal C$, which is null by :ref{#thm-sacks-tanaka}. Since $\omega_1^{\mathrm{CK}}$ is a countable limit ordinal, it is the limit of an increasing sequence $(\alpha_k)$, and the intersection is $\bigcap_k \mathcal E_{\alpha_k}$; by countable additivity, $\lambda(\mathcal E_{\alpha_k}) \to 0$.

*A hyperarithmetic bound.* Let $R(n, a)$ be the relation "$a \in \mathcal O$ and $\lambda(\mathcal A_a) > 1 - 2^{-n}$". It is $\Pi^1_1$ by :ref{#fact-higher-borel} (2), and every $n$ has some $a$ with $R(n, a)$, by the previous paragraph. By :ref{#cor-total-pi11}, there is a hyperarithmetic function $f$ with $R(n, f(n))$ for every $n$. Its range is a hyperarithmetic, hence $\Sigma^1_1$, subset of $\mathcal O$, so the ordinals $|f(n)|$ are bounded by some computable ordinal $\beta$, by the first exercise of :ref{to="hyperarithmetic/kleene-theorem"}. Then $\mathcal E_\beta \subseteq \mathcal E_{|f(n)|}$ has measure less than $2^{-n}$ for every $n$, so it is a null $\Delta^1_1$ class, and it contains $\mathcal S$.
:::

The proof mirrors the argument for $\Pi^1_1$ sets of numbers, where a $\Delta^1_1$ set is enumerated before a computable stage (:ref{#thm-pi11-stages}). For $\Pi^1_1$ classes of measure $1$, almost all the measure is enumerated before a computable stage; the remaining part has measure $0$ by the Sacks–Tanaka theorem.

## Exercises

::::exercise{difficulty=1}
Show that a $\Pi^1_1$-random sequence is not hyperarithmetic, and that $\mathcal O$ is not $\Pi^1_1$-random.

:::solution
A $\Pi^1_1$-random sequence is $\Delta^1_1$-random, hence not hyperarithmetic by :ref{#prop-delta11-arith}. The sequence $\mathcal O$ computes itself, so $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ by the proof of :ref{#cor-pi11-random-class}, and it is not $\Pi^1_1$-random by :ref{#thm-chong-nies-yu}.
:::
::::

::::exercise{difficulty=2}
Show that if $X$ is $\Pi^1_1$-random, then so is every $Y$ that differs from $X$ at finitely many positions, and so are the halves $X_0 = \{ n : 2n \in X \}$ and $X_1 = \{ n : 2n + 1 \in X \}$.

:::solution
Let $\mathcal A$ be a null $\Pi^1_1$ class. For a finite set $F$, the map $Y \mapsto Y \triangle F$ is a computable bijection of $\cs$ that preserves the measure, so $\{ Y : Y \triangle F \in \mathcal A \}$ is a null $\Pi^1_1$ class; the union over all finite $F$, coded by numbers, is a null $\Pi^1_1$ class, since a number quantifier preserves $\Pi^1_1$. If $Y \triangle F \in \mathcal A$ for some $Y$ differing from $X$ by $F$, then $X$ belongs to this union. For the halves, $\{ Z : Z_0 \in \mathcal A \}$ is $\Pi^1_1$, and null since $Z \mapsto Z_0$ maps the uniform measure to the uniform measure; the same holds for $Z_1$.
:::
::::

## Notes and references

Sacks (1969) and Tanaka (1967) proved that the class of sequences collapsing $\omega_1^{\mathrm{CK}}$ is null; Sacks also proved that $\Sigma^1_1$-randomness coincides with $\Delta^1_1$-randomness. Kechris (1975) showed that there is a largest null $\Pi^1_1$ class, and Chong, Nies and Yu (2008) characterized $\Pi^1_1$-randomness.

- G. E. Sacks, *Measure-theoretic uniformity in recursion theory and set theory*, Transactions of the American Mathematical Society 142 (1969), 381–420.
- H. Tanaka, *A basis result for Π¹₁-sets of positive measure*, Commentarii Mathematici Universitatis Sancti Pauli 16 (1967), 115–127.
- A. S. Kechris, *The theory of countable analytical sets*, Transactions of the American Mathematical Society 202 (1975), 259–297.
- C. T. Chong, A. Nies and L. Yu, *Lowness of higher randomness notions*, Israel Journal of Mathematics 166 (2008), 39–60.
