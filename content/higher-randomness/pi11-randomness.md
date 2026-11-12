---
title: Π¹₁-randomness
summary: Randomness with respect to all null Π¹₁ classes; Π¹₁-randomness is Δ¹₁-randomness together with ω₁ˣ = ω₁ᶜᵏ (Stern; Chong, Nies, Yu); there is a largest null Π¹₁ class.
duration: 35
prerequisites: [sacks-tanaka, higher-tests]
---

Taking all null $\Pi^1_1$ classes as tests gives a randomness notion with no classical analogue: in the arithmetic world, there is no reason to consider null classes that are not Borel. By Lusin's theorem (:ref{#thm-lusin}), $\Pi^1_1$ classes are measurable, so the notion makes sense. A $\Pi^1_1$ class is the union of its stages, which are $\Delta^1_1$ below $\omega_1^{\mathrm{CK}}$ (:ref{#fact-pi11-stages}); the only members it can have beyond the $\Delta^1_1$ stages are sequences that compute non-computable ordinals. By the Sacks–Tanaka theorem (:ref{#thm-sacks-tanaka}), such sequences are rare, and this lesson deduces that $\Pi^1_1$-randomness is exactly $\Delta^1_1$-randomness combined with this ordinal condition. As a consequence, the union of all null $\Pi^1_1$ classes is itself a null $\Pi^1_1$ class, a universal test for the notion.

## Π¹₁-randomness

:::definition{#def-pi11-random}
A sequence is **$\Pi^1_1$-random** if it belongs to no null $\Pi^1_1$ class, and **$\Sigma^1_1$-random** if it belongs to no null $\Sigma^1_1$ class.
:::

The definition makes sense by Lusin's theorem (:ref{#thm-lusin}). Every null $\Delta^1_1$ class is $\Pi^1_1$ and $\Sigma^1_1$, and the class captured by the universal higher test is a null $\Pi^1_1$ class (:ref{#cor-higher-mlr-class}). So
$$
\Pi^1_1\text{-random} \;\Rightarrow\; \Pi^1_1\text{-Martin-Löf random} \;\Rightarrow\; \Delta^1_1\text{-random}, \qquad \Sigma^1_1\text{-random} \;\Rightarrow\; \Delta^1_1\text{-random}.
$$
The last lesson shows that $\Sigma^1_1$-randomness coincides with $\Delta^1_1$-randomness; the new notion is $\Pi^1_1$-randomness. By the Sacks–Tanaka theorem, a $\Pi^1_1$-random sequence does not collapse $\omega_1^{\mathrm{CK}}$: Kleene's $\mathcal O$, and every sequence computing it, is not $\Pi^1_1$-random. The class of well-founded relations (:ref{#ex-measure-pi11}) is another null $\Pi^1_1$ class; it is not $\Delta^1_1$, but it adds nothing new, since it is included in a null $\Delta^1_1$ class, the class of $Y$ containing no pair $\langle x, x \rangle$. The next theorem says that this is the general situation, once the sequences collapsing $\omega_1^{\mathrm{CK}}$ are set aside.

## The characterization

:::theorem[Stern; Chong, Nies, Yu]{#thm-chong-nies-yu}
A sequence $X$ is $\Pi^1_1$-random if and only if it is $\Delta^1_1$-random and $\omega_1^X = \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=thm-chong-nies-yu}
($\Rightarrow$) A $\Pi^1_1$-random sequence avoids the null $\Delta^1_1$ classes, and the null $\Pi^1_1$ class $\mathcal C$ of :ref{#thm-sacks-tanaka}.

($\Leftarrow$) Let $X$ be $\Delta^1_1$-random with $\omega_1^X = \omega_1^{\mathrm{CK}}$, and let $\mathcal A$ be a null $\Pi^1_1$ class; write $\mathcal A = \mathcal A^p$. Suppose $X \in \mathcal A$. By :ref{#fact-pi11-stages} (2), $X \in \mathcal A^p_\alpha$ for some $\alpha < \omega_1^{\mathrm{CK}}$. The stage $\mathcal A^p_\alpha$ is $\Delta^1_1$ by :ref{#fact-pi11-stages} (1), and null since it is included in $\mathcal A$. This contradicts the $\Delta^1_1$-randomness of $X$.
:::

So the only new obstacle to randomness, beyond the hyperarithmetic null classes, is the ability to compute a non-computable ordinal. Since some $\Delta^1_1$-random sequences collapse $\omega_1^{\mathrm{CK}}$ (see the last lesson), the class $\mathcal C$ is not included in any null $\Delta^1_1$ class.

:::quiz[the characterization]
In the proof of :ref{#thm-chong-nies-yu}, where is the hypothesis $\omega_1^X = \omega_1^{\mathrm{CK}}$ used?

- [x] To know that $X$ enters the $\Pi^1_1$ class at a computable stage, so that it belongs to a $\Delta^1_1$ part of the class, which is null.
- [ ] To show that $\mathcal A$ is null.

  $\mathcal A$ is null by hypothesis.
- [ ] To show that $X$ is $\Delta^1_1$-random.

  This is the other hypothesis.

---

Why does the class $\mathcal C$ have to be excluded separately?

- [x] Because a sequence with $\omega_1^Y > \omega_1^{\mathrm{CK}}$ may enter a null $\Pi^1_1$ class only at a stage $\geq \omega_1^{\mathrm{CK}}$, where the stages of the class are no longer $\Delta^1_1$; $\Delta^1_1$-randomness does not exclude this.
- [ ] Because $\mathcal C$ is not $\Pi^1_1$.

  It is $\Pi^1_1$ and null, by :ref{#thm-sacks-tanaka}.
- [ ] Because $\mathcal C$ contains every hyperarithmetic sequence.

  Hyperarithmetic sequences $Y$ have $\omega_1^Y = \omega_1^{\mathrm{CK}}$.
:::

:::corollary{#cor-pi11-random-class}
1. The union of all null $\Pi^1_1$ classes is null: almost every sequence is $\Pi^1_1$-random.
2. There is a $\Pi^1_1$-random sequence $X$, and no such sequence computes $\mathcal O$.
:::

:::proof{of=cor-pi11-random-class}
1. By :ref{#thm-chong-nies-yu}, the union is the union of the countably many null $\Delta^1_1$ classes and of $\mathcal C$, which are null.
2. By item 1, the class of $\Pi^1_1$-random sequences has measure $1$, hence is non-empty. If $X$ computes $\mathcal O$, every $\mathcal O$-computable well-ordering is $X$-computable, so $\omega_1^X \geq \omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ by :ref{#prop-omega1-relative} (2), and $X$ is not $\Pi^1_1$-random by :ref{#thm-chong-nies-yu}.
:::

## The largest null Π¹₁ class

Item 1 of the corollary can be made effective: the union of all null $\Pi^1_1$ classes is not only null but $\Pi^1_1$. This is the counterpart of the universal Martin-Löf test, and it comes without the condition on the speed of convergence of the measures that tests require.

:::theorem[Kechris; Stern; Hjorth, Nies]{#thm-largest-null}
There is a null $\Pi^1_1$ class $\mathcal Q$ that contains every null $\Pi^1_1$ class. A sequence is $\Pi^1_1$-random if and only if it does not belong to $\mathcal Q$.
:::

:::proof{of=thm-largest-null}
Let
$$
\mathcal Q = \mathcal C \cup \bigcup \big\{ \mathcal A^p_{|a|} : p \in \nat,\ a \in \mathcal O,\ \lambda(\mathcal A^p_{|a|}) = 0 \big\}.
$$
It is null: $\mathcal C$ is null by :ref{#thm-sacks-tanaka}, and the other members of the union are countably many null classes. It contains every null $\Pi^1_1$ class $\mathcal A^p$: a member $Y$ of $\mathcal A^p$ not in $\mathcal C$ belongs to a stage $\mathcal A^p_{|a|}$ with $a \in \mathcal O$, by :ref{#fact-pi11-stages} (2), and this stage is null since it is included in $\mathcal A^p$.

It is $\Pi^1_1$. By :ref{#fact-pi11-stages} (1) and :ref{#fact-higher-borel} (1), applied to the relations $P_<$ and $P_\geq$, there is a $\Pi^1_1$ relation $M'(p, a, q)$ that expresses $\lambda(\mathcal A^p_{|a|}) < q$ for $a \in \mathcal O$, as explained after :ref{#fact-higher-borel}. Then
$$
Y \in \mathcal Q \iff Y \in \mathcal C \vee \exists p\, \exists a\, \big( a \in \mathcal O \wedge P_<(p, a, Y) \wedge \forall q > 0\ M'(p, a, q) \big),
$$
where $q$ ranges over rationals. Each component is $\Pi^1_1$, and number quantifiers preserve $\Pi^1_1$. The second statement is the definition of $\Pi^1_1$-randomness.
:::

The proof shows that $\mathcal Q$ is the union of $\mathcal C$ and of the null $\Delta^1_1$ classes, by :ref{#cor-delta11-stage}: this is :ref{#thm-chong-nies-yu} again. The contrast with the other notions is instructive. For Martin-Löf randomness, the classes captured by tests are covered by a single one, but only because the tests are a restricted family of null $\Pi^0_2$ classes, with a computable bound on the measures of the components. For $\Delta^1_1$-randomness, the union of the null $\Delta^1_1$ classes is $\Pi^1_1$ but not $\Delta^1_1$ (first exercise), so there is no largest null $\Delta^1_1$ class. For $\Pi^1_1$-randomness, the union of the tests is again a test.

The class of $\Pi^1_1$-random sequences, the complement of $\mathcal Q$, is $\Sigma^1_1$ and non-empty, so it has a member computable in $\mathcal O$ by the Kleene basis theorem (:ref{#thm-kleene-basis}). Such a member does not compute $\mathcal O$, by :ref{#cor-pi11-random-class}; it is strictly below $\mathcal O$ in the Turing degrees.

## Exercises

::::exercise{difficulty=1}
Show that the union $\mathcal G$ of all null $\Delta^1_1$ classes is $\Pi^1_1$, so that the class of $\Delta^1_1$-random sequences is $\Sigma^1_1$, and that $\mathcal G$ is not $\Delta^1_1$.

:::hint
For the second part, suppose that $\mathcal G$ is $\Delta^1_1$, cover it by an open class of measure at most $\frac12$ generated by a set c.e. in a hyperarithmetic set, and look for a hyperarithmetic member of the complement.
:::

:::solution
By :ref{#cor-delta11-stage}, the null $\Delta^1_1$ classes are the null stages $\mathcal A^p_{|a|}$ with $a \in \mathcal O$. As in the proof of :ref{#thm-largest-null}, $Y \in \mathcal G$ if and only if $\exists p\, \exists a\, \big( a \in \mathcal O \wedge P_<(p, a, Y) \wedge \forall q > 0\ M'(p, a, q) \big)$, a $\Pi^1_1$ condition. This is due to Martin-Löf (Nies, Exercise 9.3.11).

Suppose that $\mathcal G$ is $\Delta^1_1$. It is null, being a countable union of null classes. By :ref{#fact-higher-borel} (2), there are a hyperarithmetic set $A$ and a set of strings $W$ c.e. in $A$ with $\mathcal G \subseteq [W]$ and $\lambda([W]) \leq \frac12$. The complement of $[W]$ is a non-empty $\Pi^0_1(A)$ class, so its leftmost member is computable in $A'$, by :ref{#prop-leftmost-path} relativized to $A$; this member is hyperarithmetic. It lies outside $\mathcal G$, so it is $\Delta^1_1$-random, which contradicts :ref{#prop-delta11-arith}.
:::
::::

::::exercise{difficulty=1}
Show that a $\Pi^1_1$-random sequence is not hyperarithmetic and does not compute $\mathcal O$, and that a sequence computing $\mathcal O$ is not $\Pi^1_1$-random.

:::solution
A $\Pi^1_1$-random sequence is $\Delta^1_1$-random, hence not hyperarithmetic by :ref{#prop-delta11-arith}. It does not compute $\mathcal O$ by :ref{#cor-pi11-random-class}, which is equivalent to the last statement.
:::
::::

::::exercise{difficulty=2}
Show that if $X$ is $\Pi^1_1$-random, then so is every $Y$ that differs from $X$ at finitely many positions, and so are the halves $X_0 = \{ n : 2n \in X \}$ and $X_1 = \{ n : 2n + 1 \in X \}$.

:::solution
Let $\mathcal A$ be a null $\Pi^1_1$ class. For a finite set $F$, the map $Y \mapsto Y \triangle F$ is a computable bijection of $\cs$ that preserves the measure, so $\{ Z : Z \triangle F \in \mathcal A \}$ is a null $\Pi^1_1$ class. If $Y = X \triangle F$ belongs to $\mathcal A$, then $X$ belongs to this class, which is impossible when $X$ is $\Pi^1_1$-random. For the halves, $\{ Z : Z_0 \in \mathcal A \}$ is $\Pi^1_1$, and null since $Z \mapsto Z_0$ maps the uniform measure to the uniform measure: the preimage of a null Borel class containing $\mathcal A$ is a null Borel class. If $X_0 \in \mathcal A$, then $X$ belongs to this class; the same holds for $X_1$.
:::
::::

## Notes and references

Sacks introduced $\Pi^1_1$-randomness and showed that it differs from $\Delta^1_1$-randomness (Sacks, Section IV.2, as cited by Greenberg and Monin); Hjorth and Nies, who call it strong randomness, note that Sacks's book calls it $\Sigma^1_1$-randomness. The characterization :ref{#thm-chong-nies-yu} was first proved by Stern (1973, 1975) and rediscovered by Chong, Nies and Yu (2008); the largest null $\Pi^1_1$ class was found by Stern and by Kechris (1975), independently, and again by Hjorth and Nies (2007). These attributions follow the introduction of Greenberg and Monin (2017). The proof of :ref{#thm-largest-null} follows Nies (Theorem 9.3.6 and Fact 9.3.8). Monin (2014) showed that the class of $\Pi^1_1$-random sequences is $\Pi^0_3$, a much lower Borel rank than its definition suggests.

- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Chapter IV.
- J. Stern, *Some measure theoretic results in effective descriptive set theory*, Israel Journal of Mathematics 20 (1975), 97–110.
- A. S. Kechris, *The theory of countable analytical sets*, Transactions of the American Mathematical Society 202 (1975), 259–297.
- C. T. Chong, A. Nies and L. Yu, *Lowness of higher randomness notions*, Israel Journal of Mathematics 166 (2008), 39–60.
- N. Greenberg and B. Monin, *Higher randomness and genericity*, Forum of Mathematics, Sigma 5 (2017), e31.
- B. Monin, *Higher randomness and forcing with closed sets*, 31st Symposium on Theoretical Aspects of Computer Science (STACS 2014), LIPIcs 25 (2014).
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.3.
