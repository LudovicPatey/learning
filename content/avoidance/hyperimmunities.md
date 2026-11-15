---
title: Preservation of hyperimmunity by compact questions
summary: Compact forcing questions, simple and disjunctive, preserve hyperimmunity; WKL, COH and Ramsey's theorem for pairs admit preservation of hyperimmunity; the relations between the avoidance properties of the course.
duration: 25
prerequisites: [moduli]
---

The previous lesson showed that preservation of hyperimmunity (:ref{#def-preserve-hyperimmunity}) is equivalent to cone avoidance, through moduli and a theorem admitted without proof. This lesson proves it directly for the problems of the course. The forcing question needs one more property: a positive answer about a convergence must come with a bound on the value, so that the answers define a function to be compared with the hyperimmune function. This is **compactness**. With it, the three-case argument becomes a two-case argument with bounds, and the scheme of :ref{to="avoidance/non-sigma1-definitions"} applies without change: one first preserves the property along weak König's lemma to obtain a Scott ideal of reservoirs, then uses the Seetapun forcing with its question.

As in the previous lessons, a set $Z$ is fixed, the sentences are built with functionals of the oracle $Z \oplus G$, and $f$ is **$W$-hyperimmune** if no $W$-computable function dominates it.

## Compact forcing questions

For simple questions, compactness at level $1$ is :ref{#def-question-compact}; the proof of :ref{#thm-question-hyperimmunity} applies to questions that are $\Sigma^0_1(\mathcal M)$-preserving, with the function $g$ of that proof computable in a member $X$ of $\mathcal M$.

:::theorem{#thm-local-hyperimmunity}
Let $\mathbb P$ be a notion of forcing with a compact $\Sigma^0_1(\mathcal M)$-preserving forcing question, and let $f$ be $X$-hyperimmune for every $X \in \mathcal M$. For every sufficiently generic set $G$, $f$ is $(Z \oplus G)$-hyperimmune.
:::

:::proof{of=thm-local-hyperimmunity}
Fix $e$ and a condition $c$, with $X \in \mathcal M$ as in :ref{#def-question-local}. If $c \mathrel{?{\nvdash}} \Phi^{Z \oplus G}_e(x)\converge$ for some $x$, an extension forces divergence at $x$. Otherwise, by compactness, for every $x$ there is $k$ with $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge < k$, and the function $h(x)$, the first such $k$ found in an $X$-computable enumeration, is total and $X$-computable. Since $f$ is $X$-hyperimmune, $h(x) < f(x)$ for some $x$, and an extension forces $\Phi^{Z \oplus G}_e(x)\converge < h(x)$. In both cases every member $G$ of the extension has $\Phi^{Z \oplus G}_e$ partial or below $f$ at some point. A set generic for these dense sets satisfies this for every $e$.
:::

:::definition{#def-disjunctive-compact}
A disjunctive forcing question is **compact** if whenever $c \mathrel{?{\vdash}} (\Phi^{Z \oplus G}_{e_0}(x)\converge)(G_0) \vee (\Phi^{Z \oplus G}_{e_1}(x)\converge)(G_1)$, there is $k$ such that $c \mathrel{?{\vdash}} (\Phi^{Z \oplus G}_{e_0}(x)\converge < k)(G_0) \vee (\Phi^{Z \oplus G}_{e_1}(x)\converge < k)(G_1)$.
:::

:::lemma{#lem-seetapun-compact}
The disjunctive question of the Seetapun forcing (:ref{#lem-seetapun-question}) is compact.
:::

:::proof{of=lem-seetapun-compact}
Suppose the answer is positive. As in the proof of :ref{#lem-seetapun-question}, there is $\ell$ such that for every string $\beta$ of length $\ell$, there are $i < 2$ and $\tau$ with $|\tau| \leq \ell$, compatible with $(\sigma_i, X \cap \beta^i)$, with new elements homogeneous for color $i$, and $\Phi^{Z \oplus \tau}_{e_i}(x)[\ell]\converge$. There are finitely many such pairs $(i, \tau)$; let $k$ exceed all the values $\Phi^{Z \oplus \tau}_{e_i}(x)[\ell]$. For every set $B$, the witness obtained for $\beta = B \uh \ell$ is a witness for the sentences "$\Phi^{Z \oplus G}_{e_i}(x)\converge < k$", which gives the positive answer for them.
:::

The same proof applies to the question of the Dzhafarov–Jockusch forcing.

:::theorem{#thm-hyperimmunity-examples}
1. $\mathsf{WKL}$ and $\mathsf{COH}$ admit preservation of hyperimmunity.
2. $\mathsf{RT}^2_2$ admits preservation of hyperimmunity.
:::

:::proof{of=thm-hyperimmunity-examples}
Fix $Z$ and a $Z$-hyperimmune function $f$, and let $\mathcal W$ be the class of sets $X$ such that $f$ is $X$-hyperimmune.

1. The questions of Jockusch–Soare forcing and of computable Mathias forcing at level $1$ are compact and $\Sigma^0_1$-preserving (:ref{to="effective-forcing/compactness-merging"}, :ref{#prop-mathias-question}); relativized to $Z$, they are $\Sigma^0_1(\{ Z \})$-preserving, and :ref{#thm-local-hyperimmunity} applies, with Jockusch–Soare forcing inside the paths of a $Z$-computable tree, and Mathias forcing for a $Z$-computable sequence of sets.
2. By item 1, $\mathsf{WKL}$ preserves $\mathcal W$, so :ref{#lem-scott-preservation} gives a Scott ideal $\mathcal M \subseteq \mathcal W$ containing $Z$. Let $g$ be a $Z$-computable coloring of pairs, and use the Seetapun forcing for $g$ (:ref{#def-seetapun-forcing}, with $g$ in place of $f$) with reservoirs in $\mathcal M$. If an infinite homogeneous set $H$ for $g$ belongs to $\mathcal M$, then $Z \oplus H \in \mathcal W$. Otherwise, both sides can always be extended (:ref{#lem-seetapun-infinity}). Given a condition $c$ and indices $e_0, e_1$, either the question about $\Phi^{Z \oplus G}_{e_0}(x)\converge$ on side $0$ or $\Phi^{Z \oplus G}_{e_1}(x)\converge$ on side $1$ is answered negatively for some $x$, and an extension forces the divergence at $x$ on some side; or it is answered positively for every $x$, and by :ref{#lem-seetapun-compact} the first bound $k$ found in an enumeration computable in some $X \in \mathcal M$ defines an $X$-computable function $h$. Then $h(x) < f(x)$ for some $x$, and an extension forces, on some side $i$, $\Phi^{Z \oplus G_i}_{e_i}(x)\converge < h(x) < f(x)$. As in :ref{#lem-disjunctive-construction}, one side $G_i$ of the resulting homogeneous sets satisfies: no $\Phi^{Z \oplus G_i}_e$ dominates $f$, that is, $f$ is $(Z \oplus G_i)$-hyperimmune.
:::

Item 2 also follows from Seetapun's theorem and :ref{#cor-hyperimmunity-equivalence}; the direct proof avoids the admitted theorem, and shows the role of compactness.

:::quiz[compact questions]
In the proof of :ref{#thm-local-hyperimmunity}, why is compactness needed?

- [x] To turn the positive answers about convergence into a function $h$ that bounds the forced values; without bounds, a positive answer gives no comparison with $f$.
- [ ] To make $h$ total.

  Totality comes from the positive answers for every $x$; compactness provides the bounds that $h$ outputs.
- [ ] To find an extension forcing divergence.

  That is property 2 of the question, in the first case.
:::

## The picture

The relations between the avoidance properties of this course are summarized in the figure. Downey, Greenberg, Harrison-Trainor, Patey and Turetsky showed that cone avoidance, avoidance of countably many cones, preservation of one non-$\Sigma^0_1$ definition and preservation of one hyperimmunity are all equivalent, while none of these equivalences holds for the unrelativized versions. The equivalences do not extend to several definitions or functions in the same way: preservation of $k$ hyperimmunities and preservation of $k$ non-$\Sigma^0_1$ definitions are equivalent for each $k \leq \omega$, but $\mathsf{RT}^2_2$ admits preservation of one hyperimmunity and not of two (Patey), whereas $\mathsf{WKL}$ (Jockusch and Soare) and the Erdős–Moser theorem (Patey) admit preservation of countably many. These finer properties are the custom properties used to separate Ramsey-type theorems from each other.

:::figure[Avoidance properties of problems and how they are proved. Solid arrows are proved in this course: strong cone avoidance implies cone avoidance by definition, the left arrow is :ref{#prop-non-sigma1-cone}, the right one :ref{#thm-hyperimmunity-cone}, and the lower arrows are :ref{#thm-local-non-sigma1} and :ref{#thm-local-hyperimmunity}, with their disjunctive versions. Dashed arrows are :ref{#thm-non-sigma1-equivalence} and :ref{#cor-hyperimmunity-equivalence}.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Relations between the avoidance properties of a problem: strong cone avoidance implies cone avoidance; cone avoidance is equivalent to preservation of one non-Sigma01 definition and to preservation of one hyperimmunity; forcing questions with the right properties give each preservation property"><defs><marker id="av-rel-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="225" y="14" width="150" height="40" rx="6" class="state"/><text x="300.0" y="38.0" text-anchor="middle" class="label">strong cone avoidance</text><rect x="225" y="112" width="150" height="40" rx="6" class="state"/><text x="300.0" y="136.0" text-anchor="middle" class="label">cone avoidance</text><rect x="10" y="104" width="170" height="56" rx="6" class="state"/><text x="95.0" y="128.0" text-anchor="middle" class="label">preservation of 1</text><text x="95.0" y="144.0" text-anchor="middle" class="label">non-Σ⁰₁ definition</text><rect x="420" y="104" width="170" height="56" rx="6" class="state"/><text x="505.0" y="128.0" text-anchor="middle" class="label">preservation of 1</text><text x="505.0" y="144.0" text-anchor="middle" class="label">hyperimmunity</text><rect x="10" y="222" width="170" height="56" rx="6" class="cell"/><text x="95.0" y="246.0" text-anchor="middle" class="label">Σ⁰₁(ℳ)-preserving</text><text x="95.0" y="262.0" text-anchor="middle" class="label">forcing question</text><rect x="420" y="222" width="170" height="56" rx="6" class="cell"/><text x="505.0" y="246.0" text-anchor="middle" class="label">Σ⁰₁(ℳ)-preserving compact</text><text x="505.0" y="262.0" text-anchor="middle" class="label">forcing question</text><line x1="300" y1="56" x2="300" y2="108" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="182" y1="124" x2="221" y2="124" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="223" y1="140" x2="184" y2="140" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#av-rel-arr)"/><line x1="418" y1="124" x2="379" y2="124" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="377" y1="140" x2="416" y2="140" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#av-rel-arr)"/><line x1="95" y1="220" x2="95" y2="164" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="505" y1="220" x2="505" y2="164" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="200" y1="262" x2="240" y2="262" class="ink-stroke" stroke-width="1.3"/><text x="248" y="266" class="label">proved in the course</text><line x1="200" y1="284" x2="240" y2="284" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4"/><text x="248" y="288" class="label">admitted (Downey et al.)</text></svg>
:::

## Exercises

::::exercise{#ex-rt12-strong-hyperimmunity difficulty=2 objective="Adapt the disjunctive argument to show that the pigeonhole principle preserves hyperimmunity on arbitrary instances." lessons="disjunctive-question"}
Show that $\mathsf{RT}^1_2$ admits strong preservation of hyperimmunity.

:::solution
Fix $Z$ and a $Z$-hyperimmune $f$, and let $\mathcal M$ be a Scott ideal of sets $X$ such that $f$ is $X$-hyperimmune, containing $Z$ (:ref{#lem-scott-preservation} and item 1 of :ref{#thm-hyperimmunity-examples}). Use the Dzhafarov–Jockusch forcing for the set $A$, with reservoirs in $\mathcal M$ and the question of :ref{#ex-dj-disjunctive}. It is compact, by the proof of :ref{#lem-seetapun-compact} without the homogeneity clauses. If an infinite subset of $A$ or $\overline A$ belongs to $\mathcal M$, it is a solution. Otherwise both sides can be extended, and the argument of item 2 of :ref{#thm-hyperimmunity-examples} gives, for each pair $(e_0, e_1)$, an extension forcing on some side that $\Phi_{e_i}$ is partial or below $f$ at some point; Lachlan's disjunction gives one side preserving the hyperimmunity of $f$.
:::
::::

## Notes and references

The abstract theorem with a compact question follows the section *Preserving hyperimmunities* of the chapter *Cone avoidance* of Patey's monograph, where it is stated for $\Sigma^0_1$-preserving questions and attributed to Monin and Patey (2019, Lemma 2.6); the local and disjunctive versions are given here in the form needed for problems. Theorem 2.1 of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022) states the four equivalences of the figure, and their Corollaries 3.4 and 3.6 the equivalence of preservation of $k$ hyperimmunities and of $k$ non-$\Sigma^0_1$ definitions. Preservation of countably many hyperimmunities for $\mathsf{WKL}$ is Theorem 2.4 of Jockusch and Soare (1972), the hyperimmune-free basis theorem; the results on $\mathsf{RT}^2_{k+1,k}$ and the Erdős–Moser theorem are in Patey (2017).

- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Preserving hyperimmunities*.

:::::exercises
::::exercise{#ex-wkl-countable-hyperimmune difficulty=1 objective="Preserve countably many hyperimmune functions with Jockusch–Soare forcing, and see why Ramsey's theorem for triples preserves none."}
Show that $\mathsf{WKL}$ preserves countably many hyperimmune functions at once, and that $\mathsf{RT}^3_2$ does not admit preservation of hyperimmunity.

:::solution
In the proof of :ref{#thm-local-hyperimmunity}, the dense sets for a function $f_j$ and an index $e$ form a countable family, indexed by $(j, e)$; a sufficiently generic set for Jockusch–Soare forcing inside the paths of the instance meets all of them. For $\mathsf{RT}^3_2$, if it admitted preservation of hyperimmunity, it would admit cone avoidance by :ref{#thm-hyperimmunity-cone}, contradicting :ref{#prop-rt32-jump}. Directly: the modulus $m$ of $\emptyset'$ is hyperimmune, and every infinite homogeneous set of the coloring of :ref{#prop-rt32-jump} computes $\emptyset'$, hence $m$.
:::
::::

::::exercise[A sparse reservoir]{#ex-hyperimmunity-sparse-reservoir difficulty=1 objective="See with a sparse reservoir why the hyperimmune function must remain hyperimmune relative to every member of the class ℳ."}
Consider Mathias forcing with arbitrary infinite reservoirs, and the question of :ref{#prop-mathias-question}, which is a compact forcing question whose answers at $(\sigma, X)$ are $\Sigma^0_1(X)$. Let $f$ be a hyperimmune function. Find a condition all of whose infinite members $G$ compute a function dominating $f$. Which hypothesis of :ref{#thm-local-hyperimmunity} fails?

:::solution
Let $F(n) = n + \max_{i \leq n} f(i)$. It is strictly increasing, so it is the principal function of its range $X$, an infinite set. Consider the condition $(\varepsilon, X)$. Its infinite members are the infinite subsets $G$ of $X$, and the $n$-th element of such a $G$ is at least the $n$-th element of $X$: $p_G(n) \geq F(n) \geq f(n)$ for every $n$. Since $p_G \leq_T G$, $f$ is not $G$-hyperimmune.

The question is compact and $\Sigma^0_1(\mathcal M)$-preserving for the class $\mathcal M$ of all sets, but $f$ is not $X$-hyperimmune: $X$ computes $F$, which dominates $f$. This is the hypothesis that fails. The example plays for hyperimmunity the role of :ref{#ex-coding-reservoir} for cones: a reservoir can transmit its growth to all the members of a condition.
:::
::::

::::exercise[Strong preservation for cohesiveness]{#ex-coh-strong-hyperimmunity difficulty=2 objective="Combine the strong preservation of hyperimmunity for the pigeonhole principle with Mathias forcing to obtain it for cohesiveness." lessons="strong-cone-avoidance"}
Show that $\mathsf{COH}$ admits strong preservation of hyperimmunity.

:::solution
Fix $Z$, a $Z$-hyperimmune function $f$ and an arbitrary sequence of sets $\vec R$. Use Mathias conditions $(\sigma, X)$ such that $f$ is $(Z \oplus X)$-hyperimmune, and let $\mathcal M$ be the class of these sets $Z \oplus X$. Refinement holds, since removing finitely many elements from $X$ does not change its degree.

*Hyperimmunity.* The question of :ref{#prop-mathias-question}, with functionals of the oracle $Z \oplus G$, is a forcing question whatever the reservoir. It is compact: a compatible string $\tau$ with $\Phi^{Z \oplus \tau}_e(x)\converge = v$ witnesses the positive answer for "$\Phi^{Z \oplus G}_e(x)\converge < v + 1$". Its answers at $(\sigma, X)$ are $\Sigma^0_1(Z \oplus X)$, and $f$ is $(Z \oplus X)$-hyperimmune. By :ref{#thm-local-hyperimmunity}, $f$ is $(Z \oplus G)$-hyperimmune for every sufficiently generic $G$.

*Cohesiveness.* Fix $n$ and a condition $(\sigma, X)$. Let $p$ enumerate $X$ in increasing order, and $A = \{ k : p(k) \in R_n \}$. By :ref{#ex-rt12-strong-hyperimmunity} relative to $Z \oplus X$, there is an infinite set $H$, contained in $A$ or in $\overline A$, such that $f$ is $(Z \oplus X \oplus H)$-hyperimmune. The set $Y = p[H]$ is an infinite subset of $X$, contained in $R_n$ or in $\overline{R_n}$, and computable in $X \oplus H$, so $f$ is $(Z \oplus Y)$-hyperimmune and $(\sigma, Y)$ is a condition extending $(\sigma, X)$. *Infinity* is handled as usual.

A sufficiently generic set is infinite, $\vec R$-cohesive, and preserves the hyperimmunity of $f$. The proof is that of :ref{#thm-coh-strong-cone}, with the weakness property of hyperimmunity in place of the cone.
:::
::::

::::exercise[Through computable domination]{#ex-wkl-hyperimmunity-dominated difficulty=1 objective="Derive the preservation of hyperimmunity for weak König's lemma from the computably dominated basis theorem."}
Using the computably dominated basis theorem (:ref{#thm-dominated-basis}) relativized to a set $Z$, give a second proof that $\mathsf{WKL}$ admits preservation of hyperimmunity, which preserves all $Z$-hyperimmune functions with a single path.

:::solution
Relativized to $Z$, the computably dominated basis theorem gives, for every infinite $Z$-computable binary tree, a path $Y$ such that every total $(Z \oplus Y)$-computable function is dominated by a $Z$-computable function. Let $f$ be $Z$-hyperimmune. If a function $g \leq_T Z \oplus Y$ dominated $f$, a $Z$-computable function $h$ dominating $g$ would dominate $f$, which is impossible. So $f$ is $(Z \oplus Y)$-hyperimmune. The path $Y$ does not depend on $f$, so it preserves every $Z$-hyperimmune function at once. This is the form in which Jockusch and Soare proved the preservation of countably many hyperimmunities.
:::
::::

::::exercise[Each function, or all of them]{#ex-preserve-every-hyperimmune difficulty=1 objective="Distinguish the preservation of each hyperimmune function from the preservation of all of them at once, which is computable domination."}
Show that a set $G$ has the property that every hyperimmune function is $G$-hyperimmune if and only if $G$ is computably dominated (:ref{#def-computably-dominated}). Deduce that for every hyperimmune function $f$, every sufficiently generic set $G$ for computable Mathias forcing keeps $f$ hyperimmune, while no such $G$ keeps all hyperimmune functions hyperimmune.

:::solution
Suppose that $G$ is computably dominated, and let $f$ be hyperimmune. If $g \leq_T G$ dominated $f$, a computable function dominating $g$ would dominate $f$. So $f$ is $G$-hyperimmune. Conversely, suppose that $G$ is not computably dominated: some total $G$-computable function $g$ is dominated by no computable function, that is, $g$ is hyperimmune. Since $g$ dominates itself, $g$ is not $G$-hyperimmune.

The question of :ref{#prop-mathias-question} is compact and $\Sigma^0_1$-preserving, so by :ref{#thm-local-hyperimmunity} with $Z = \emptyset$ and $\mathcal M = \{ \emptyset \}$, for each hyperimmune $f$ every sufficiently generic $G$ keeps $f$ hyperimmune; the dense sets used depend on $f$. But a sufficiently generic $G$ has a principal function $p_G$ that eventually dominates every computable function (:ref{#prop-mathias-dominant}). Then no computable function $h$ dominates $p_G$, since $p_G(n) \geq h(n) + 1$ for almost every $n$; so $p_G$ is hyperimmune and $G$-computable, and $G$ is not computably dominated. The order of the quantifiers matters: preservation of hyperimmunity is about one function at a time.
:::
::::
:::::
