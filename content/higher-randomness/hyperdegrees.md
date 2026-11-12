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

Combining the lessons of this course, and the characterization of $\Delta^1_1$-randomness in the exercise of :ref{to="higher-tests"}:

:::figure[The notions of randomness of the course, from the strongest to the weakest. Each implies the next; the labels on the arrows give the examples that separate them, and the labels on the right give characterizations.]{#fig-randomness-hierarchy}
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Five randomness notions in a column, from Pi11-randomness at the top to Martin-Loef randomness at the bottom, each implying the next; no implication reverses"><defs><marker id="hr-hier-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="30" y="14" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="34" text-anchor="middle" font-size="14">Π¹₁-random</text><text x="274" y="33" class="label">= Δ¹₁-random and <tspan class="math" font-size="14">ω</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="math" font-size="9" dy="-9">X</tspan><tspan class="mrm" font-size="14" dy="6"> = </tspan><tspan class="math" font-size="14">ω</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="mrm" font-size="9" dy="-9">CK</tspan></text><line x1="145.0" y1="46" x2="145.0" y2="68" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="61.0" text-anchor="start" class="label">strict: a Π¹₁-Martin-Löf random Z with O ≤h Z</text><rect x="30" y="70" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="90" text-anchor="middle" font-size="14">Π¹₁-Martin-Löf random</text><line x1="145.0" y1="102" x2="145.0" y2="124" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="117.0" text-anchor="start" class="label">strict: Hjorth and Nies</text><rect x="30" y="126" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="146" text-anchor="middle" font-size="14">Δ¹₁-random  =  Σ¹₁-random</text><text x="274.0" y="145.0" text-anchor="start" class="label">= Martin-Löf random relative to every hyperarithmetic set</text><line x1="145.0" y1="158" x2="145.0" y2="180" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="173.0" text-anchor="start" class="label">strict: Ω relative to ∅⁽ω⁾</text><rect x="30" y="182" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="202" text-anchor="middle" font-size="14">n-random for every n</text><line x1="145.0" y1="214" x2="145.0" y2="236" class="ink-stroke" stroke-width="1.3" marker-end="url(#hr-hier-arrow)"/><text x="157.0" y="229.0" text-anchor="start" class="label">strict: Ω</text><rect x="30" y="238" width="230" height="30" rx="4" class="cell"/><text x="145.0" y="258" text-anchor="middle" font-size="14">Martin-Löf random</text></svg>
:::

None of the implications reverses.

- The sequence $\Omega^{\emptyset^{(\omega)}}$ is $n$-random for every $n$ but not $\Delta^1_1$-random (first exercise).
- Some $\Delta^1_1$-random sequence is not $\Pi^1_1$-Martin-Löf random (Hjorth and Nies; admitted in :ref{to="higher-tests"}).
- Some $\Pi^1_1$-Martin-Löf random sequence $Z$ satisfies $\mathcal O \leq_h Z$, so it collapses $\omega_1^{\mathrm{CK}}$ and is not $\Pi^1_1$-random. This follows from the higher analogue of the Kučera–Gács theorem (Nies, Theorem 9.2.9): every set is computed, by a reduction with a $\Pi^1_1$ graph using finitely many bits of the oracle, by a member of a $\Sigma^1_1$ class of $\Pi^1_1$-Martin-Löf random sequences. The higher analogue of Chaitin's $\Omega$ is an explicit example (Nies, Exercise 9.2.10). We admit these results.

The notions differ in their lowness properties as well. A set $A$ is **low** for a randomness notion if every random sequence is random relative to $A$. Hjorth and Nies showed that the sets low for $\Pi^1_1$-Martin-Löf randomness are exactly the hyperarithmetic sets (Nies, Corollary 9.2.16). For $\Pi^1_1$-randomness, the question was asked by Hjorth and Nies and listed as open by Nies (Question 9.4.11); Greenberg and Monin (2017) answered it: if $A$ is not hyperarithmetic, some $\Pi^1_1$-random sequence is not $\Pi^1_1$-Martin-Löf random relative to $A$, so the sets low for $\Pi^1_1$-randomness are again exactly the hyperarithmetic sets. They also showed that for every non-hyperarithmetic $A$ and every $Y$, there is a $\Pi^1_1$-random $Z$ with $Y \leq_h A \oplus Z$. We admit these results.

## Exercises

::::exercise{difficulty=1}
Let $\Omega^Z$ denote Chaitin's halting probability relative to an oracle $Z$. Show that $\Omega^{\emptyset^{(\omega)}}$ is $n$-random for every $n$ but not $\Delta^1_1$-random, where $\emptyset^{(\omega)} = \bigoplus_n \emptyset^{(n)}$.

:::solution
By :ref{#cor-omega-random} relativized to $Z = \emptyset^{(\omega)}$, the sequence $\Omega^Z$ is Martin-Löf random relative to $Z$, hence relative to each $\emptyset^{(n)} \leq_T Z$, so it is $(n+1)$-random for every $n$. It is computable in $Z'$, which is hyperarithmetic, so it is hyperarithmetic, and not $\Delta^1_1$-random by :ref{#prop-delta11-arith}.
:::
::::

::::exercise{difficulty=2}
Let $Z$ be any set. Show that there is a $\Pi^1_1$-random sequence $Y$ such that every set $X$ with $X \leq_h Z$ and $X \leq_h Y$ is hyperarithmetic.

:::solution
The sets $X \leq_h Z$ are countably many: each is computable in some $H^Z_b$ with $b \in \mathcal O^Z$, and there are countably many notations and functionals. Apply :ref{#cor-higher-null-cone} to the non-hyperarithmetic ones: almost every $Y$ is $\Pi^1_1$-random and hyperarithmetically computes none of them. Any such $Y$ works.
:::
::::

::::exercise{difficulty=2}
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
