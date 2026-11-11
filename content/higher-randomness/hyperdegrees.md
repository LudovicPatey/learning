---
title: Randomness and hyperarithmetic reducibility
summary: Hyperarithmetic reducibility; the higher analogue of Sacks' theorem, that the upper hyperarithmetic cone of a non-hyperarithmetic set is null; the hierarchy of higher randomness notions and its relation with arithmetic randomness.
duration: 30
prerequisites: [pi11-randomness, martin-lof-randomness/measure]
---

Sacks' theorem (:ref{#thm-sacks}) says that a non-computable set is computed by almost no sequence. Its proof decides each bit of the set by a majority vote over a cone of positive measure, which is a computable process when the measures can be approximated. In the higher setting, the measures of $\Delta^1_1$ classes are hyperarithmetic, and the same vote, combined with the Sacks–Tanaka theorem, shows that a non-hyperarithmetic set is hyperarithmetically computed by almost no sequence. The lesson ends with the hierarchy of the notions of the course.

## Hyperarithmetic reducibility

:::definition{#def-hyp-reducible}
A set $X$ is **hyperarithmetic in** $Y$, written $X \leq_h Y$, if $X$ is $\Delta^1_1(Y)$: both $X$ and its complement are defined by $\Pi^1_1$ formulas with the set parameter $Y$.
:::

The relation $\leq_h$ is a preorder, and the hyperarithmetic sets are the sets $X$ with $X \leq_h \emptyset$. Kleene's theorem relativizes: $X \leq_h Y$ if and only if $X$ is computable in some set $H^Y_b$ with $b$ a notation relative to $Y$, that is, $b \in \mathcal O^Y$. When $Y$ does not compute new ordinals, notations in $\mathcal O$ suffice. We admit this refinement, due to Spector (Sacks, *Higher Recursion Theory*, Section II.7).

:::fact{#fact-hyp-reducible}
If $\omega_1^Y = \omega_1^{\mathrm{CK}}$ and $X \leq_h Y$, then $X \leq_T H^Y_a$ for some $a \in \mathcal O$.
:::

## The upper cone of a non-hyperarithmetic set

:::theorem[Sacks]{#thm-higher-null-cone}
If $X$ is not hyperarithmetic, then the class $\{ Y : X \leq_h Y \}$ is null.
:::

:::proof{of=thm-higher-null-cone}
For $a \in \mathcal O$ and an index $e$, let $\mathcal K_{a, e} = \{ Y : \Phi^{H^Y_a}_e = X \}$, where the equality means that the functional is total and equal to the characteristic function of $X$. By :ref{#fact-hyp-reducible},
$$
\{ Y : X \leq_h Y \} \subseteq \mathcal C \cup \bigcup_{a \in \mathcal O,\, e \in \nat} \mathcal K_{a, e},
$$
where $\mathcal C$ is the null class of :ref{#thm-sacks-tanaka}. The union is countable, so it suffices to show that every $\mathcal K_{a, e}$ is null.

For a string $\sigma$, a number $n$ and $i \in \{ 0, 1 \}$, let $\mathcal P^\sigma_{n, i} = \{ Y \in [\sigma] : \Phi^{H^Y_a}_e(n)\converge = i \}$. By the parameter theorem, it is of the form $\mathcal D_{a, e'}$ with $e'$ computable from $e$, $\sigma$, $n$ and $i$; so it is Borel, and by :ref{#fact-higher-borel} (2) the relation $\lambda(\mathcal P^\sigma_{n, i}) > q$ is $\Pi^1_1$ in $(\sigma, n, i, q)$, for our fixed $a \in \mathcal O$. The class $\mathcal K_{a, e} = \bigcap_n \mathcal P^{\emptyset}_{n, X(n)}$ is Borel.

Suppose $\lambda(\mathcal K_{a, e}) > 0$. By the Lebesgue density lemma (:ref{#lem-density}), there is a string $\sigma$ with $\lambda(\mathcal K_{a, e} \cap [\sigma]) > \frac12 \cdot 2^{-|\sigma|}$. For every $n$, $\mathcal K_{a, e} \cap [\sigma] \subseteq \mathcal P^\sigma_{n, X(n)}$, so this class has measure greater than $q = 2^{-|\sigma| - 1}$. The classes $\mathcal P^\sigma_{n, 0}$ and $\mathcal P^\sigma_{n, 1}$ are disjoint subclasses of $[\sigma]$, so $\mathcal P^\sigma_{n, 1 - X(n)}$ has measure less than $q$. Hence
$$
n \in X \iff \lambda(\mathcal P^\sigma_{n, 1}) > q, \qquad n \notin X \iff \lambda(\mathcal P^\sigma_{n, 0}) > q.
$$
Both conditions are $\Pi^1_1$ in $n$, so $X$ is $\Delta^1_1$, hence hyperarithmetic by Kleene's theorem: a contradiction.
:::

:::corollary{#cor-higher-null-cone}
For every countable family of non-hyperarithmetic sets $X_0, X_1, \dots$, almost every sequence $Y$ is $\Pi^1_1$-random and satisfies $X_k \not\leq_h Y$ for every $k$.
:::

:::proof{of=cor-higher-null-cone}
The non-$\Pi^1_1$-random sequences form a null class (:ref{#cor-pi11-random-class}), and so does each cone $\{ Y : X_k \leq_h Y \}$; a countable union of null classes is null.
:::

:::quiz[the null cone]
In the proof of :ref{#thm-higher-null-cone}, why is :ref{#thm-sacks-tanaka} needed?

- [x] Because a sequence $Y$ with $\omega_1^Y > \omega_1^{\mathrm{CK}}$ may compute $X$ hyperarithmetically through a notation outside $\mathcal O$, which gives no class $\mathcal K_{a, e}$ with $a \in \mathcal O$; such sequences form a null class.
- [ ] To show that $\mathcal K_{a, e}$ is Borel.

  This follows from :ref{#fact-higher-borel}.
- [ ] To find the string $\sigma$.

  The string comes from the density lemma.

---

Why does the majority vote give a $\Delta^1_1$ definition of $X$, and not only a $\Pi^1_1$ one?

- [x] Because exactly one of the two classes $\mathcal P^\sigma_{n, 0}$, $\mathcal P^\sigma_{n, 1}$ has measure greater than $q$, so both $n \in X$ and $n \notin X$ are expressed by a $\Pi^1_1$ condition.
- [ ] Because the measures are rational.

  The measures are hyperarithmetic reals; only the comparisons with $q$ are used.
- [ ] Because $\mathcal K_{a, e}$ is $\Delta^1_1$.

  Its definition uses $X$, which is the unknown set.
:::

## The hierarchy of higher randomness

Combining the lessons of this course:
$$
\Pi^1_1\text{-random} \;\Rightarrow\; \Pi^1_1\text{-Martin-Löf random} \;\Rightarrow\; \Delta^1_1\text{-random} \;\Leftrightarrow\; \Sigma^1_1\text{-random} \;\Rightarrow\; n\text{-random for every } n.
$$
None of the implications reverses. For the last one, see the first exercise. The separation of $\Delta^1_1$-randomness from $\Pi^1_1$-Martin-Löf randomness is due to Hjorth and Nies, and the separation of $\Pi^1_1$-Martin-Löf randomness from $\Pi^1_1$-randomness to Hjorth and Nies and to Chong, Nies and Yu; both are admitted. The lowness properties of these notions were studied by Chong, Nies and Yu, Hjorth and Nies, Bienvenu, Greenberg and Monin, and Greenberg and Monin. For instance, Hjorth and Nies showed that the sets that are low for $\Pi^1_1$-Martin-Löf randomness are exactly the hyperarithmetic sets, and Greenberg and Monin that if $A$ is not hyperarithmetic, some $\Pi^1_1$-random sequence is not $\Pi^1_1$-Martin-Löf random relative to $A$; we admit these results.

## Exercises

::::exercise{difficulty=1}
Let $\Omega^Z$ denote Chaitin's halting probability relative to an oracle $Z$. Show that $\Omega^{\emptyset^{(\omega)}}$ is $n$-random for every $n$ but not $\Delta^1_1$-random, where $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$.

:::solution
By :ref{#cor-omega-random} relativized to $Z = \emptyset^{(\omega)}$, the sequence $\Omega^Z$ is Martin-Löf random relative to $Z$, hence relative to each $\emptyset^{(n)} \leq_T Z$, so it is $(n+1)$-random for every $n$. It is computable in $Z'$, which is hyperarithmetic, so it is hyperarithmetic, and not $\Delta^1_1$-random by :ref{#prop-delta11-arith}.
:::
::::

::::exercise{difficulty=2}
Let $Z$ be any set. Show that there is a $\Pi^1_1$-random sequence $Y$ such that no set $X$ with $X \leq_h Z$ and $X \leq_h Y$ is non-hyperarithmetic.

:::solution
The sets $X \leq_h Z$ are countably many: each is computable in some $H^Z_b$ with $b \in \mathcal O^Z$, and there are countably many notations and functionals. Apply :ref{#cor-higher-null-cone} to the non-hyperarithmetic ones: almost every $Y$ is $\Pi^1_1$-random and hyperarithmetically computes none of them. Any such $Y$ works.
:::
::::

## Notes and references

Sacks proved the measure-theoretic results of this lesson in his work on measure-theoretic uniformity. Recent surveys of higher randomness are the monograph of Chong and Yu and the chapter of Monin and Patey's book.

- G. E. Sacks, *Measure-theoretic uniformity in recursion theory and set theory*, Transactions of the American Mathematical Society 142 (1969), 381–420.
- L. Bienvenu, N. Greenberg and B. Monin, *Continuous higher randomness*, Journal of Mathematical Logic 17 (2017), 1750004.
- N. Greenberg and B. Monin, *Higher randomness and genericity*, Forum of Mathematics, Sigma 5 (2017), e31.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015.
