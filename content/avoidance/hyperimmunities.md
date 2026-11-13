---
title: Preservation of hyperimmunity by compact questions
summary: Compact forcing questions, simple and disjunctive, preserve hyperimmunity; WKL, COH and Ramsey's theorem for pairs admit preservation of hyperimmunity; the relations between the avoidance properties of the course.
duration: 30
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

::::exercise{difficulty=1}
Show that $\mathsf{WKL}$ preserves countably many hyperimmune functions at once, and that $\mathsf{RT}^3_2$ does not admit preservation of hyperimmunity.

:::solution
In the proof of :ref{#thm-local-hyperimmunity}, the dense sets for a function $f_j$ and an index $e$ form a countable family, indexed by $(j, e)$; a sufficiently generic set for Jockusch–Soare forcing inside the paths of the instance meets all of them. For $\mathsf{RT}^3_2$, if it admitted preservation of hyperimmunity, it would admit cone avoidance by :ref{#thm-hyperimmunity-cone}, contradicting :ref{#prop-rt32-jump}. Directly: the modulus $m$ of $\emptyset'$ is hyperimmune, and every infinite homogeneous set of the coloring of :ref{#prop-rt32-jump} computes $\emptyset'$, hence $m$.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{RT}^1_2$ admits strong preservation of hyperimmunity.

:::solution
Fix $Z$ and a $Z$-hyperimmune $f$, and let $\mathcal M$ be a Scott ideal of sets $X$ such that $f$ is $X$-hyperimmune, containing $Z$ (:ref{#lem-scott-preservation} and item 1 of :ref{#thm-hyperimmunity-examples}). Use the Dzhafarov–Jockusch forcing for the set $A$, with reservoirs in $\mathcal M$ and the question of the first exercise of :ref{to="avoidance/disjunctive-question"}. It is compact, by the proof of :ref{#lem-seetapun-compact} without the homogeneity clauses. If an infinite subset of $A$ or $\overline A$ belongs to $\mathcal M$, it is a solution. Otherwise both sides can be extended, and the argument of item 2 of :ref{#thm-hyperimmunity-examples} gives, for each pair $(e_0, e_1)$, an extension forcing on some side that $\Phi_{e_i}$ is partial or below $f$ at some point; Lachlan's disjunction gives one side preserving the hyperimmunity of $f$.
:::
::::

## Notes and references

The abstract theorem with a compact question follows the section *Preserving hyperimmunities* of the chapter *Cone avoidance* of Patey's monograph, where it is stated for $\Sigma^0_1$-preserving questions and attributed to Monin and Patey (2019, Lemma 2.6); the local and disjunctive versions are given here in the form needed for problems. Theorem 2.1 of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022) states the four equivalences of the figure, and their Corollaries 3.4 and 3.6 the equivalence of preservation of $k$ hyperimmunities and of $k$ non-$\Sigma^0_1$ definitions. Preservation of countably many hyperimmunities for $\mathsf{WKL}$ is Theorem 2.4 of Jockusch and Soare (1972), the hyperimmune-free basis theorem; the results on $\mathsf{RT}^2_{k+1,k}$ and the Erdős–Moser theorem are in Patey (2017).

- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Preserving hyperimmunities*.
