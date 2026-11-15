---
title: Σ¹₁ null classes and hyperarithmetic reducibility
summary: Every null Σ¹₁ class is included in a null Δ¹₁ class, so Σ¹₁-randomness is Δ¹₁-randomness; hyperarithmetic reducibility; the upper hyperarithmetic cone of a non-hyperarithmetic set is null; the hierarchy of higher randomness notions.
duration: 45
prerequisites: [pi11-randomness, martin-lof-randomness/upper-cones]
---

The Sacks–Tanaka theorem says that the sequences entering a $\Pi^1_1$ class beyond its $\Delta^1_1$ stages form a null class. This lesson draws two further consequences, both of them higher analogues of classical facts. The first concerns $\Sigma^1_1$ null classes: they add nothing to the $\Delta^1_1$ ones, because the complement of such a class receives almost all its measure before a computable stage, and selection and boundedness turn "almost all" into a single computable stage. The second is the higher analogue of Sacks's theorem (:ref{#thm-sacks}) that a non-computable set is computed by almost no sequence. Its proof decides each bit of the set by a majority vote over a cylinder, which is a computable process when the measures can be approximated; in the higher setting the measures of $\Delta^1_1$ classes are hyperarithmetic, and the same vote, combined with the Sacks–Tanaka theorem, shows that a non-hyperarithmetic set is hyperarithmetically computed by almost no sequence. The lesson ends with the hierarchy of the notions of the course.

## Σ¹₁-randomness

:::theorem[Sacks]{#thm-sigma11-random}
Every null $\Sigma^1_1$ class is contained in a null $\Delta^1_1$ class. Hence $\Sigma^1_1$-randomness coincides with $\Delta^1_1$-randomness.
:::

:::proof{of=thm-sigma11-random}
Let $\mathcal S$ be a null $\Sigma^1_1$ class, and let $\mathcal A^p = \cs \setminus \mathcal S$, a $\Pi^1_1$ class of measure $1$, with stages $\mathcal A^p_\alpha$.

*Almost all the measure is reached before $\omega_1^{\mathrm{CK}}$.* By :ref{#fact-pi11-stages} (2), $\mathcal A^p \subseteq \mathcal C \cup \bigcup_{\alpha < \omega_1^{\mathrm{CK}}} \mathcal A^p_\alpha$, where $\mathcal C$ is the null class of :ref{#thm-sacks-tanaka}. So the union of the stages $\mathcal A^p_\alpha$, $\alpha < \omega_1^{\mathrm{CK}}$, has measure $1$. Since $\omega_1^{\mathrm{CK}}$ is the limit of an increasing sequence $(\alpha_k)$ of computable ordinals, countable additivity gives $\lambda(\mathcal A^p_{\alpha_k}) \to 1$.

*Selection and boundedness.* Let $R(n, a)$ be the relation "$a \in \mathcal O$ and $\lambda(\mathcal A^p_{|a|}) > 1 - 2^{-n}$". It is $\Pi^1_1$ by :ref{#fact-pi11-stages} (1) and :ref{#fact-higher-borel} (1). Every $n$ has some $a$ with $R(n, a)$, by the previous paragraph: take a notation of a suitable $\alpha_k$. By Kreisel's selection theorem (:ref{#cor-total-pi11}), there is a hyperarithmetic function $f$ with $R(n, f(n))$ for every $n$. Its range is a $\Delta^1_1$, hence $\Sigma^1_1$, subset of $\mathcal O$, so there is $b \in \mathcal O$ with $|f(n)| < |b|$ for every $n$ (:ref{#ex-o-bounded}). Then $\lambda(\mathcal A^p_{|b|}) > 1 - 2^{-n}$ for every $n$, so the complement $\mathcal E = \cs \setminus \mathcal A^p_{|b|}$ is null. It is $\Delta^1_1$ by :ref{#fact-pi11-stages} (1), and it contains $\mathcal S$, since $\mathcal A^p_{|b|} \subseteq \mathcal A^p$.
:::

The proof is the measure-theoretic version of :ref{#thm-pi11-stages} (3), by which a $\Delta^1_1$ set of numbers is enumerated before a computable stage. A $\Pi^1_1$ class of measure $1$ is not enumerated before a computable stage in general, but almost all its measure is, and the remaining part is null by the Sacks–Tanaka theorem.

:::quiz[Σ¹₁ null classes]
In the proof of :ref{#thm-sigma11-random}, where is the Sacks–Tanaka theorem used?

- [x] To show that the stages below $\omega_1^{\mathrm{CK}}$ already carry measure $1$: the members of $\mathcal A^p$ entering later collapse $\omega_1^{\mathrm{CK}}$, and they form a null class.
- [ ] To show that $R$ is $\Pi^1_1$.

  This uses the description of the stages and the measure fact, not the Sacks–Tanaka theorem.
- [ ] To bound the ordinals $|f(n)|$.

  This is the boundedness theorem, applied to the range of the hyperarithmetic function $f$.

---

Why does the same argument not show that every null $\Pi^1_1$ class is included in a null $\Delta^1_1$ class?

- [x] Because for a null $\Pi^1_1$ class, the complement is $\Sigma^1_1$ and has no stages; the stages describe a $\Pi^1_1$ class from inside, and only for the class $\mathcal A^p$ of measure $1$ do they give $\Delta^1_1$ classes whose complements cover a null class.
- [ ] Because null $\Pi^1_1$ classes are not measurable.

  They are measurable by Lusin's theorem.
- [ ] Because the relation $R$ would then be $\Sigma^1_1$.

  The obstacle is earlier: there is no stage decomposition of a $\Sigma^1_1$ class to which the measure fact applies. And the statement is false, since the null $\Pi^1_1$ class $\mathcal C$ is not included in a null $\Delta^1_1$ class.
:::

## Hyperarithmetic reducibility

:::definition{#def-hyp-reducible}
A set $X$ is **hyperarithmetic in** $Y$, written $X \leq_h Y$, if $X$ is $\Delta^1_1(Y)$: both $X$ and its complement are defined by $\Pi^1_1$ formulas with the set parameter $Y$.
:::

The relation $\leq_h$ is a preorder, and the hyperarithmetic sets are the sets $X$ with $X \leq_h \emptyset$. For example, every set computable in $Y^{(\omega)}$ is hyperarithmetic in $Y$, and Spector proved that $\mathcal O \leq_h Y$ if and only if $Y$ collapses $\omega_1^{\mathrm{CK}}$ (Nies, Theorem 9.1.14). Kleene's theorem relativizes (remark after :ref{#thm-kleene-delta11}): $X \leq_h Y$ if and only if $X$ is computable in some set $H^Y_b$ with $b$ a notation relative to $Y$, that is, $b \in \mathcal O^Y$. Here the H-sets relative to $Y$ are defined as the sets $H_a$ (:ref{#def-h-sets}), starting from $H^Y_1 = Y$. When $Y$ does not collapse $\omega_1^{\mathrm{CK}}$, the notations of $\mathcal O$ suffice.

:::proposition{#fact-hyp-reducible}
If $\omega_1^Y = \omega_1^{\mathrm{CK}}$ and $X \leq_h Y$, then $X \leq_T H^Y_a$ for some $a \in \mathcal O$.
:::

:::proof{of=fact-hyp-reducible}
By Kleene's theorem relativized, $X \leq_T H^Y_b$ for some $b \in \mathcal O^Y$. The ordinal $|b|$ is $Y$-computable, by :ref{#prop-constructive-computable} relativized, so $|b| < \omega_1^Y = \omega_1^{\mathrm{CK}}$, and $|b|$ has a notation $a \in \mathcal O$ (:ref{#cor-constructive-computable}). A notation in $\mathcal O$ can be read as a notation in $\mathcal O^Y$, by replacing each index of a computable fundamental sequence by an index of the same sequence computed with an oracle that is not consulted; this does not change the H-sets relative to $Y$. Spector's theorem relativized to $Y$ (:ref{#thm-spector-uniqueness}) then gives $H^Y_a \equiv_T H^Y_b$, so $X \leq_T H^Y_a$.
:::

## The upper cone of a non-hyperarithmetic set

:::theorem[Sacks]{#thm-higher-null-cone}
If $X$ is not hyperarithmetic, then the class $\{ Y : X \leq_h Y \}$ is null.
:::

The proof is the majority vote of :ref{#thm-sacks}, in which the computable approximations of measures are replaced by the $\Pi^1_1$ comparisons of :ref{#fact-higher-borel}; the sequences collapsing $\omega_1^{\mathrm{CK}}$, for which :ref{#fact-hyp-reducible} fails, are set aside by the Sacks–Tanaka theorem.

:::proof{of=thm-higher-null-cone}
For $a \in \mathcal O$ and an index $e$, let $\mathcal K_{a, e} = \{ Y : \Phi^{H^Y_a}_e = X \}$, where the equality means that the functional is total and equal to the characteristic function of $X$. By :ref{#fact-hyp-reducible},
$$
\{ Y : X \leq_h Y \} \subseteq \mathcal C \cup \bigcup_{a \in \mathcal O,\, e \in \nat} \mathcal K_{a, e},
$$
where $\mathcal C$ is the null class of :ref{#thm-sacks-tanaka}. The union is countable, so it suffices to show that every $\mathcal K_{a, e}$ is null. Fix $a \in \mathcal O$ and $e$.

For a string $\sigma$, a number $n$ and $i \in \{ 0, 1 \}$, let $\mathcal P^\sigma_{n, i} = \{ Y \in [\sigma] : \Phi^{H^Y_a}_e(n)\converge = i \}$. Relativizing :ref{#lem-h-sequence-unique}, for every $Y$ there is exactly one H-sequence along $a$ starting from $Y$, and its column $a$ is $H^Y_a$. So, as in the proof of :ref{#prop-h-delta11},
$$
Y \in \mathcal P^\sigma_{n, i} \iff \sigma \prec Y \wedge \forall Z\, \big( Z \text{ is an H-sequence along } a \text{ starting from } Y \rightarrow \Phi^{Z^{[a]}}_e(n)\converge = i \big),
$$
and the complement is defined in the same way with $\neg(\sigma \prec Y) \vee \forall Z\, (\cdots \rightarrow \neg\, \Phi^{Z^{[a]}}_e(n)\converge = i)$. Both are $\Pi^1_1$ in $(\sigma, n, i, Y)$. So the classes $\mathcal P^\sigma_{n, i}$ are $\Delta^1_1$, hence Borel, and by :ref{#fact-higher-borel} (1) the relation $\lambda(\mathcal P^\sigma_{n, i}) > q$ is $\Pi^1_1$ in $(\sigma, n, i, q)$. The class $\mathcal K_{a, e} = \bigcap_n \mathcal P^{\langle\rangle}_{n, X(n)}$ is Borel.

Suppose $\lambda(\mathcal K_{a, e}) > 0$. By the Lebesgue density lemma (:ref{#lem-density}), there is a string $\sigma$ with $\lambda(\mathcal K_{a, e} \mid \sigma) > \frac12$, that is, $\lambda(\mathcal K_{a, e} \cap [\sigma]) > q$ with $q = 2^{-|\sigma| - 1}$. For every $n$, $\mathcal K_{a, e} \cap [\sigma] \subseteq \mathcal P^\sigma_{n, X(n)}$, so this class has measure greater than $q$. The classes $\mathcal P^\sigma_{n, 0}$ and $\mathcal P^\sigma_{n, 1}$ are disjoint subclasses of $[\sigma]$, so $\mathcal P^\sigma_{n, 1 - X(n)}$ has measure less than $q$ (:ref{#fig-majority-vote}). Hence
$$
n \in X \iff \lambda(\mathcal P^\sigma_{n, 1}) > q, \qquad n \notin X \iff \lambda(\mathcal P^\sigma_{n, 0}) > q.
$$
Both conditions are $\Pi^1_1$ in $n$, so $X$ is $\Delta^1_1$, hence hyperarithmetic by Kleene's theorem: a contradiction.
:::

:::figure[The majority vote in the proof of :ref{#thm-higher-null-cone}, in a cylinder $[\sigma]$ where the class $\mathcal K = \mathcal K_{a, e}$ has relative measure greater than $\frac12$ (the cone class). The class $\mathcal P^\sigma_{n, X(n)}$ of oracles giving the right bit contains $\mathcal K \cap [\sigma]$, so it has relative measure greater than $\frac12$; the class $\mathcal P^\sigma_{n, 1 - X(n)}$ of oracles giving the wrong bit is disjoint from it, so it has relative measure less than $\frac12$. Oracles on which the functional diverges belong to neither.]{#fig-majority-vote}
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="A cylinder; the part of the cone class in it occupies more than half; the class of oracles giving the right bit contains it and has relative measure above one half; the class giving the wrong bit is disjoint from it and has relative measure below one half"><rect x="90" y="35" width="330" height="18" class="cell"/><rect x="90" y="85" width="330" height="18" class="cell"/><rect x="90.0" y="85" width="99.0" height="18" class="soft-fill"/><rect x="208.8" y="85" width="79.2" height="18" class="soft-fill"/><rect x="314.4" y="85" width="59.4" height="18" class="soft-fill"/><rect x="90" y="135" width="330" height="18" class="cell"/><rect x="90.0" y="135" width="108.9" height="18" class="accent-fill"/><rect x="208.8" y="135" width="92.4" height="18" class="accent-fill"/><rect x="314.4" y="135" width="72.6" height="18" class="accent-fill"/><rect x="403.5" y="135" width="6.6" height="18" class="accent-fill"/><rect x="90" y="185" width="330" height="18" class="cell"/><rect x="198.9" y="185" width="9.9" height="18" class="muted-fill"/><rect x="301.2" y="185" width="13.2" height="18" class="muted-fill"/><rect x="387.0" y="185" width="16.5" height="18" class="muted-fill"/><text x="80" y="49" text-anchor="end" class="math" font-size="15"><tspan class="mrm">[</tspan>σ<tspan class="mrm">]</tspan></text><text x="80.0" y="98.0" text-anchor="end" class="label">cone class</text><text x="80.0" y="148.0" text-anchor="end" class="label">right bit</text><text x="80.0" y="198.0" text-anchor="end" class="label">wrong bit</text><text x="432.0" y="98.0" text-anchor="start" class="label">relative measure &gt; 1/2</text><text x="432.0" y="148.0" text-anchor="start" class="label">contains it: &gt; 1/2</text><text x="432.0" y="198.0" text-anchor="start" class="label">disjoint from it: &lt; 1/2</text></svg>
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

  This follows from the $\Delta^1_1$ definitions of the classes $\mathcal P^\sigma_{n, i}$.
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

Combining the lessons of this course, and the characterization of $\Delta^1_1$-randomness of :ref{#ex-delta11-ml-hyp}:

:::figure[The notions of randomness of the course, from the strongest to the weakest. Each implies the next; the labels on the arrows give the examples that separate them, and the labels on the right give characterizations.]{#fig-randomness-hierarchy}
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Five randomness notions in a column, from Pi11-randomness at the top to Martin-Loef randomness at the bottom, each implying the next; no implication reverses"><defs><marker id="hr-hier-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="30" y="14" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="34" text-anchor="middle" font-size="14">Π¹₁-random</text><text x="274" y="33" class="label">= Δ¹₁-random and <tspan class="math" font-size="14">ω</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="math" font-size="9" dy="-9">X</tspan><tspan class="mrm" font-size="14" dy="6"> = </tspan><tspan class="math" font-size="14">ω</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="mrm" font-size="9" dy="-9">CK</tspan></text><line x1="145.0" y1="46" x2="145.0" y2="68" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="61.0" text-anchor="start" class="label">strict: a Π¹₁-Martin-Löf random Z with O ≤h Z</text><rect x="30" y="70" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="90" text-anchor="middle" font-size="14">Π¹₁-Martin-Löf random</text><line x1="145.0" y1="102" x2="145.0" y2="124" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="117.0" text-anchor="start" class="label">strict: Hjorth and Nies</text><rect x="30" y="126" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="146" text-anchor="middle" font-size="14">Δ¹₁-random  =  Σ¹₁-random</text><text x="274.0" y="145.0" text-anchor="start" class="label">= Martin-Löf random relative to every hyperarithmetic set</text><line x1="145.0" y1="158" x2="145.0" y2="180" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="173.0" text-anchor="start" class="label">strict: Ω relative to ∅⁽ω⁾</text><rect x="30" y="182" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="202" text-anchor="middle" font-size="14">n-random for every n</text><line x1="145.0" y1="214" x2="145.0" y2="236" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="229.0" text-anchor="start" class="label">strict: Ω</text><rect x="30" y="238" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="258" text-anchor="middle" font-size="14">Martin-Löf random</text></svg>
:::

None of the implications reverses.

- The sequence $\Omega^{\emptyset^{(\omega)}}$ is $n$-random for every $n$ but not $\Delta^1_1$-random (:ref{#ex-omega-hyp-not-delta11}).
- Some $\Delta^1_1$-random sequence is not $\Pi^1_1$-Martin-Löf random (Hjorth and Nies; admitted in :ref{to="higher-tests"}).
- Some $\Pi^1_1$-Martin-Löf random sequence $Z$ satisfies $\mathcal O \leq_h Z$, so it collapses $\omega_1^{\mathrm{CK}}$ and is not $\Pi^1_1$-random. This follows from the higher analogue of the Kučera–Gács theorem (Nies, Theorem 9.2.9): every set is computed, by a reduction with a $\Pi^1_1$ graph using finitely many bits of the oracle, by a member of a $\Sigma^1_1$ class of $\Pi^1_1$-Martin-Löf random sequences. The higher analogue of Chaitin's $\Omega$ is an explicit example (Nies, Exercise 9.2.10). We admit these results.

The notions differ in their lowness properties as well. A set $A$ is **low** for a randomness notion if every random sequence is random relative to $A$. Hjorth and Nies showed that the sets low for $\Pi^1_1$-Martin-Löf randomness are exactly the hyperarithmetic sets (Nies, Corollary 9.2.16). For $\Pi^1_1$-randomness, the question was asked by Hjorth and Nies and listed as open by Nies (Question 9.4.11); Greenberg and Monin (2017) answered it: if $A$ is not hyperarithmetic, some $\Pi^1_1$-random sequence is not $\Pi^1_1$-Martin-Löf random relative to $A$, so the sets low for $\Pi^1_1$-randomness are again exactly the hyperarithmetic sets. They also showed that for every non-hyperarithmetic $A$ and every $Y$, there is a $\Pi^1_1$-random $Z$ with $Y \leq_h A \oplus Z$. We admit these results.

## Exercises

::::exercise{#ex-omega-hyp-not-delta11 difficulty=1 objective="Separate $\Delta^1_1$-randomness from $n$-randomness for every $n$ with a relativized halting probability."}
Let $\Omega^Z$ denote Chaitin's halting probability relative to an oracle $Z$. Show that $\Omega^{\emptyset^{(\omega)}}$ is $n$-random for every $n$ but not $\Delta^1_1$-random, where $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$.

:::solution
By :ref{#cor-omega-random} relativized to $Z = \emptyset^{(\omega)}$, the sequence $\Omega^Z$ is Martin-Löf random relative to $Z$, hence relative to each $\emptyset^{(n)} \leq_T Z$, so it is $(n+1)$-random for every $n$. It is computable in $Z'$, which is hyperarithmetic, so it is hyperarithmetic, and not $\Delta^1_1$-random by :ref{#prop-delta11-arith}.
:::
::::

::::exercise{#ex-delta11-random-hyp-cone difficulty=2 objective="Combine Sacks's theorem with the $\Delta^1_1$ definition of a Turing cone above a hyperarithmetic set."}
Show that a $\Delta^1_1$-random sequence computes no non-computable hyperarithmetic set.

:::solution
Let $A$ be hyperarithmetic and not computable. The class $\{ Y : A \leq_T Y \}$ is defined by "$\exists e\, \forall n\, \Phi^Y_e(n)\converge = A(n)$", an arithmetic formula with the hyperarithmetic parameter $A$, so it is $\Delta^1_1$ (:ref{#ex-delta11-classes} (2)). It is null by Sacks's theorem (:ref{#thm-sacks}). A $\Delta^1_1$-random sequence avoids it. In contrast, by the Kučera–Gács theorem, every set, in particular every hyperarithmetic set, is computed by some Martin-Löf random sequence.
:::
::::

## Notes and references

Sacks proved the measure-theoretic results of this lesson in his work on measure-theoretic uniformity. Monin and Patey attribute :ref{#thm-sigma11-random} to Sacks (Section IV.2 of his book); Nies attributes it to Chong, Nies and Yu (2008). The proof of :ref{#thm-higher-null-cone} follows Monin and Patey; Nies refers it to Sacks's book (Theorem 9.1.13). Nies's Chapter 9 and the monograph of Chong and Yu survey higher randomness, including lowness and the higher analogue of $K$-triviality.

- G. E. Sacks, *Measure-theoretic uniformity in recursion theory and set theory*, Transactions of the American Mathematical Society 142 (1969), 381–420.
- G. Hjorth and A. Nies, *Randomness via effective descriptive set theory*, Journal of the London Mathematical Society 75 (2007), 495–508.
- C. T. Chong, A. Nies and L. Yu, *Lowness of higher randomness notions*, Israel Journal of Mathematics 166 (2008), 39–60.
- L. Bienvenu, N. Greenberg and B. Monin, *Continuous higher randomness*, Journal of Mathematical Logic 17 (2017), 1750004.
- N. Greenberg and B. Monin, *Higher randomness and genericity*, Forum of Mathematics, Sigma 5 (2017), e31.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Chapter 9.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015.

:::::exercises
::::exercise{#ex-hyp-random-minimal-pair difficulty=2 objective="Apply the null cone theorem to countably many sets at once."}
Let $Z$ be any set. Show that there is a $\Pi^1_1$-random sequence $Y$ such that every set $X$ with $X \leq_h Z$ and $X \leq_h Y$ is hyperarithmetic.

:::solution
The sets $X \leq_h Z$ are countably many: each is computable in some $H^Z_b$ with $b \in \mathcal O^Z$, and there are countably many notations and functionals. Apply :ref{#cor-higher-null-cone} to the non-hyperarithmetic ones: almost every $Y$ is $\Pi^1_1$-random and hyperarithmetically computes none of them. Any such $Y$ works.
:::
::::

::::exercise{#ex-hyp-low-pi11 difficulty=1 objective="Show that hyperarithmetic sets are low for $\Pi^1_1$-randomness, by eliminating a hyperarithmetic parameter."}
A class is **$\Pi^1_1(A)$** if it is defined by a formula $\forall Z\, \varphi(Y, Z, A)$ with $\varphi$ arithmetic, and a sequence is **$\Pi^1_1$-random relative to $A$** if it belongs to no null $\Pi^1_1(A)$ class. Show that if $A$ is hyperarithmetic, every $\Pi^1_1(A)$ class is $\Pi^1_1$, so that $\Pi^1_1$-randomness relative to $A$ is $\Pi^1_1$-randomness.

:::solution
Let $\psi(n)$ and $\chi(n)$ be a $\Pi^1_1$ and a $\Sigma^1_1$ definition of $A$ (:ref{#prop-h-delta11}). Write $\varphi$ in prenex form, with its matrix in negation normal form, so that the parameter $A$ occurs only in atomic formulas $x \in A$ and negated atomic formulas $x \notin A$. Replace each $x \in A$ by $\psi(x)$ and each $x \notin A$ by $\neg \chi(x)$, both $\Pi^1_1$. The result is built from $\Pi^1_1$ and arithmetic formulas by conjunctions, disjunctions and number quantifiers, so it is $\Pi^1_1$, and it is equivalent to $\varphi(Y, Z, A)$ for all $Y$ and $Z$. A universal set quantifier in front of a $\Pi^1_1$ formula gives a $\Pi^1_1$ formula, by contracting the two set quantifiers $\forall Z\, \forall Z'$ into one. So the class is $\Pi^1_1$, and the null $\Pi^1_1(A)$ classes are null $\Pi^1_1$ classes. Conversely, a $\Pi^1_1$ class is $\Pi^1_1(A)$. The argument is that of :ref{#ex-delta11-classes} (2). This is the easy half of the theorem of Greenberg and Monin stated in the lesson: the sets low for $\Pi^1_1$-randomness are exactly the hyperarithmetic sets.
:::
::::

::::exercise{#ex-sigma11-measure-not-attained difficulty=2 objective="See that the theorem on null $\Sigma^1_1$ classes does not extend to $\Sigma^1_1$ classes of positive measure."}
Give a $\Sigma^1_1$ class $\mathcal S$ such that no $\Delta^1_1$ class $\mathcal D \supseteq \mathcal S$ has $\lambda(\mathcal D) = \lambda(\mathcal S)$. (By :ref{#ex-delta11-approx-pi11}, such classes $\mathcal D$ exist with $\lambda(\mathcal D) < \lambda(\mathcal S) + \varepsilon$ for every $\varepsilon > 0$.)

:::solution
Let $\mathcal S = \cs \setminus [W]$, with $W = \{ 0^n 1 : n \in \mathcal O \}$ as in :ref{#ex-open-measure-not-hyp}; it is $\Sigma^1_1$, of measure $1 - r$, where $r = \lambda([W])$ is not a hyperarithmetic real. If $\mathcal D \supseteq \mathcal S$ is $\Delta^1_1$ with $\lambda(\mathcal D) = 1 - r$, then by :ref{#fact-higher-borel} (1) and the discussion after it, the left and right cuts of $1 - r$ are $\Delta^1_1$, and so are those of $r$: $q < r$ if and only if $1 - q > 1 - r$. This contradicts :ref{#ex-open-measure-not-hyp}.

In the proof of :ref{#thm-sigma11-random}, the selection uses the relation $\lambda(\mathcal A^p_{|a|}) > 1 - 2^{-n}$, whose bound is a rational. For a class of positive measure, the corresponding bound $\lambda(\mathcal A^p) - 2^{-n}$ need not be a hyperarithmetic real, as the example shows, and :ref{#fact-higher-borel} (1) no longer makes the relation $\Pi^1_1$.
:::
::::

::::exercise{#ex-random-hyp-incomparable difficulty=1 objective="Apply the null cone theorem to find $\Pi^1_1$-random sequences that are hyperarithmetically incomparable."}
Let $X$ be $\Pi^1_1$-random. Show that almost every $Y$ is $\Pi^1_1$-random and hyperarithmetically incomparable with $X$: $X \not\leq_h Y$ and $Y \not\leq_h X$.

:::solution
The sequence $X$ is not hyperarithmetic (:ref{#ex-pi11-random-not-hyp}), so by :ref{#cor-higher-null-cone} almost every $Y$ is $\Pi^1_1$-random with $X \not\leq_h Y$. The class $\{ Y : Y \leq_h X \}$ is countable, since by Kleene's theorem relativized every such $Y$ is $\Phi^{H^X_b}_e$ for some $b \in \mathcal O^X$ and some $e$; so it is null. The union of these two null classes is null, and every $Y$ outside it works.
:::
::::

::::exercise[One direction of Spector's theorem]{#ex-spector-easy-direction difficulty=2 objective="Prove without Spector's theorem that a sequence hyperarithmetically above $\mathcal O$ collapses $\omega_1^{\mathrm{CK}}$."}
Show that if $\mathcal O \leq_h Y$, then $\omega_1^Y > \omega_1^{\mathrm{CK}}$. Deduce that no $\Pi^1_1$-random sequence $X$ satisfies $\mathcal O \leq_h X$.

:::solution
Suppose $\mathcal O \leq_h Y$ and $\omega_1^Y = \omega_1^{\mathrm{CK}}$. By :ref{#fact-hyp-reducible}, $\mathcal O \leq_T H^Y_a$ for some $a \in \mathcal O$. We show that $\omega_1^{H^Y_a} = \omega_1^Y$; then every $\mathcal O$-computable well-ordering is $H^Y_a$-computable, and $\omega_1^{\mathcal O} \leq \omega_1^Y = \omega_1^{\mathrm{CK}}$, contradicting :ref{#prop-omega1-relative} (2).

Clearly $\omega_1^{H^Y_a} \geq \omega_1^Y$, since $Y \leq_T H^Y_a$. Suppose that some $H^Y_a$-computable well-ordering $W = \Phi^{H^Y_a}_k$ has type $\omega_1^Y$; such a $W$ exists if $\omega_1^{H^Y_a} > \omega_1^Y$, since the $H^Y_a$-computable ordinals are closed downward. For an index $e$, let $L^Y_e$ be the relation computed by $\Phi^Y_e$. Then $L^Y_e$ is a well-ordering if and only if it is a linear order and there are sets $Z$ and $h$ such that $Z$ is an H-sequence along $a$ starting from $Y$, $\Phi^{Z^{[a]}}_k$ is the characteristic function of a linear order $W_Z$, and $h$ embeds $L^Y_e$ into $W_Z$. Indeed, there is exactly one such $Z$, with column $a$ equal to $H^Y_a$ (:ref{#lem-h-sequence-unique} relativized to $Y$, as in the proof of :ref{#thm-higher-null-cone}), so $W_Z = W$; a well-ordering $L^Y_e$ has type less than $\omega_1^Y$ and embeds into $W$ by :ref{#thm-wo-comparison}, and a linear order that embeds into a well-ordering is a well-ordering. The conditions are arithmetic in $Y$, $Z$ and $h$. This is a $\Sigma^1_1(Y)$ definition of the set of indices of $Y$-computable well-orderings, which contradicts :ref{#prop-pi11-not-sigma11} relativized to $Y$. This is the argument of :ref{#ex-hyp-omega1-ck}, relativized to $Y$.

If $X$ is $\Pi^1_1$-random, then $\omega_1^X = \omega_1^{\mathrm{CK}}$ by :ref{#thm-chong-nies-yu}, so $\mathcal O \not\leq_h X$. The converse of the first statement, that $\omega_1^Y > \omega_1^{\mathrm{CK}}$ implies $\mathcal O \leq_h Y$, is the harder direction of Spector's theorem, admitted in the lesson.
:::
::::

::::exercise[Π¹₁-random sequences are hyp-dominated]{#ex-pi11-random-hyp-dominated difficulty=3 objective="Combine the $\Delta^1_1$ classes of the null cone proof with Kreisel's selection to show that functions hyperarithmetic in a $\Pi^1_1$-random sequence are dominated by hyperarithmetic functions."}
A function $g$ **dominates** $f$ if $f(n) \leq g(n)$ for almost every $n$. Show that if $X$ is $\Pi^1_1$-random, then every function $f \leq_h X$ is dominated by a hyperarithmetic function.

:::solution
By :ref{#thm-chong-nies-yu}, $X$ is $\Delta^1_1$-random and $\omega_1^X = \omega_1^{\mathrm{CK}}$. By :ref{#fact-hyp-reducible}, applied to the graph of $f$, there are $a \in \mathcal O$ and $e$ with $f = \Phi^{H^X_a}_e$. For numbers $n$ and $k$, let
$$
\mathcal E_{n, k} = \{ Y : \Phi^{H^Y_a}_e(n)\converge \geq k \}.
$$
*The classes $\mathcal E_{n, k}$ are $\Delta^1_1$, uniformly.* As for the classes $\mathcal P^\sigma_{n, i}$ in the proof of :ref{#thm-higher-null-cone}, $Y \in \mathcal E_{n, k}$ if and only if every H-sequence $Z$ along $a$ starting from $Y$ satisfies $\Phi^{Z^{[a]}}_e(n)\converge \geq k$, and $Y \notin \mathcal E_{n, k}$ if and only if every such $Z$ fails it; both are $\Pi^1_1$ in $(n, k, Y)$. By :ref{#fact-higher-borel} (1), and the discussion after it, the relations $\lambda(\mathcal E_{n, k}) > q$ and $\lambda(\mathcal E_{n, k}) < q$ are $\Pi^1_1$ in $(n, k, q)$; so is $\lambda(\mathcal E_{n, k}) \leq q$, which holds if and only if $\lambda(\mathcal E_{n, k}) < q'$ for every rational $q' > q$.

*A hyperarithmetic bound.* For fixed $n$, the classes $\mathcal E_{n, k}$ decrease with $k$, and their intersection is empty, since a convergent computation has a single value. By countable additivity, $\lambda(\mathcal E_{n, k}) \to 0$ as $k \to \infty$. Let $r(n)$ be the least $k$ with $\lambda(\mathcal E_{n, k}) \leq 2^{-n}$. Then $r(n) = k$ if and only if $\lambda(\mathcal E_{n, k}) \leq 2^{-n}$ and $\lambda(\mathcal E_{n, j}) > 2^{-n}$ for every $j < k$, a $\Pi^1_1$ relation. So $r$ is a total function with $\Pi^1_1$ graph, hyperarithmetic by :ref{#cor-total-pi11}.

*A null $\Delta^1_1$ class.* Let $\mathcal D$ be the class of $Y$ that belong to $\mathcal E_{n, r(n)}$ for infinitely many $n$. Since the graph of $r$ is $\Delta^1_1$, the relation $Y \in \mathcal E_{n, r(n)}$, that is $\exists k\, (r(n) = k \wedge Y \in \mathcal E_{n, k})$, and its negation, $\exists k\, (r(n) = k \wedge Y \notin \mathcal E_{n, k})$, are $\Pi^1_1$; so $\mathcal D = \{ Y : \forall m\, \exists n \geq m\ Y \in \mathcal E_{n, r(n)} \}$ and its complement are $\Pi^1_1$, and $\mathcal D$ is $\Delta^1_1$. For every $m$, $\mathcal D \subseteq \bigcup_{n \geq m} \mathcal E_{n, r(n)}$, of measure at most $\sum_{n \geq m} 2^{-n} = 2^{1 - m}$; so $\mathcal D$ is null.

*Domination.* $X$ is $\Delta^1_1$-random, so $X \notin \mathcal D$: for almost every $n$, $X \notin \mathcal E_{n, r(n)}$. Since $\Phi^{H^X_a}_e(n)$ converges to $f(n)$, this means $f(n) < r(n)$. So $r$ dominates $f$.

This is a theorem of Chong, Nies and Yu (Nies, Theorem 9.4.3, where the proof uses the bounding principle instead of :ref{#fact-hyp-reducible}); sequences with this property are called **hyp-dominated**.
:::
::::
:::::
