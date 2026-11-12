---
title: Preservation of hyperimmunities
summary: Moduli and the duality between computing a set and computing fast-growing functions; a problem preserves hyperimmunity if its solutions never compute a function dominating a given hyperimmune one; this implies cone avoidance, and is equivalent to it; compact forcing questions prove it for WKL, COH, the pigeonhole principle and Ramsey's theorem for pairs.
duration: 45
prerequisites: [non-sigma1-definitions, turing-degrees/limit-computability, immunity-growth/immune-sets]
---

There is a duality between computing sets and computing fast-growing functions. A set computes $\emptyset'$ if and only if it computes a function dominating the modulus of the standard enumeration of $\emptyset'$ (:ref{#cor-complete-domination}); more generally, a non-computable $\Delta^0_2$ set is computed by every function dominating its computation function (:ref{#thm-computation-function}). The lower bounds for Ramsey's theorem use this duality: the homogeneous sets of the coloring of triples of :ref{#prop-rt32-jump} compute $\emptyset'$ because they are sparse, so that their principal functions dominate a modulus. A problem that can force its solutions to compute fast-growing functions is a candidate for encoding sets. This lesson defines the corresponding avoidance property, the **preservation of hyperimmunity**, relates it to cone avoidance, and proves it for the problems of the course with a **compact** forcing question.

Recall that a function $f$ is **hyperimmune** if no computable function dominates it (:ref{#def-hyperimmune-fn}), where $g$ dominates $f$ if $g(x) \geq f(x)$ for every $x$. Relative to a set $W$, $f$ is **$W$-hyperimmune** if no $W$-computable function dominates it. Changing finitely many values of a dominating function does not change its degree, so "dominates" may equivalently be read as "dominates from some point on".

## Moduli

:::definition{#def-relative-modulus}
Let $Z$ be a set. A function $m$ is a **modulus of $C$ relative to $Z$** if $C \leq_T Z \oplus g$ for every function $g$ that dominates $m$.
:::

By :ref{#cor-complete-domination}, the modulus of the standard approximation of $\emptyset'$ is a modulus of $\emptyset'$ relative to $\emptyset$. A modulus of a set relative to $Z$ is a growth rate beyond which every function, together with $Z$, knows the set. Not every set has one: Solovay showed that the sets having a modulus relative to $\emptyset$ are exactly the hyperarithmetic sets. The $\Delta^0_2$ sets have moduli that are computable in them.

:::lemma{#lem-delta2-modulus}
Let $C \leq_T Z'$. There is a function $m \leq_T C \oplus Z$ that is a modulus of $C$ relative to $Z$.
:::

:::proof{of=lem-delta2-modulus}
By the limit lemma relativized to $Z$ (:ref{#thm-limit-lemma}), $C$ has a $Z$-computable approximation $(C_s)$. Let $m$ be its computation function (:ref{#def-modulus}): $m(x)$ is the least $s \geq x$ with $C_s \uh x = C \uh x$, which is found with oracle $C \oplus Z$. The proof of :ref{#thm-computation-function} relativized to $Z$ shows that for every $g$ dominating $m$, $C$ is computable in $g \oplus Z$: the function $M$ of that proof is computable in $g$ and the approximation.
:::

:::lemma{#lem-modulus-hyperimmune}
Let $m$ be a modulus of $C$ relative to $Z$, and $Y$ a set.

1. If $C \not\leq_T Z \oplus Y$, then $m$ is $(Z \oplus Y)$-hyperimmune.
2. If $m \leq_T C \oplus Z$ and $m$ is $(Z \oplus Y)$-hyperimmune, then $C \not\leq_T Z \oplus Y$.
:::

:::proof{of=lem-modulus-hyperimmune}
1. If a function $g \leq_T Z \oplus Y$ dominated $m$, then $C \leq_T Z \oplus g \leq_T Z \oplus Y$.
2. If $C \leq_T Z \oplus Y$, then $m \leq_T C \oplus Z \leq_T Z \oplus Y$, and $m$ dominates itself.
:::

For a set $C \leq_T Z'$ with $C \not\leq_T Z$ and the modulus $m$ of :ref{#lem-delta2-modulus}, the two items say that a set $Y$ avoids the cone above $C$ together with $Z$ if and only if $m$ remains hyperimmune relative to $Z \oplus Y$. For such sets, cone avoidance is a statement about the growth of the functions computed by the solutions.

## Preservation of hyperimmunity

:::definition{#def-preserve-hyperimmunity}
A problem $\mathsf P$ admits **preservation of hyperimmunity** if for every set $Z$, every $Z$-hyperimmune function $f$, and every instance $X \leq_T Z$ of $\mathsf P$, there is a solution $Y$ to $X$ such that $f$ is $(Z \oplus Y)$-hyperimmune. It admits **strong** preservation of hyperimmunity if the same holds for every instance $X$.
:::

For a fixed $f$, the class of sets $W$ such that $f$ is $W$-hyperimmune is closed downwards, so this is again the preservation of a family of weakness properties. The problem $\mathsf J$ does not admit it: the modulus of $\emptyset'$ is hyperimmune, by :ref{#lem-modulus-hyperimmune} with $Z = Y = \emptyset$, and it is computable in $\emptyset'$. Unlike preservation of non-$\Sigma^0_1$ definitions, preservation of hyperimmunity has no immediate relation with cone avoidance: a hyperimmune function need not be a modulus of any non-computable set relative to $\emptyset$; Downey, Greenberg, Harrison-Trainor, Patey and Turetsky observe that the principal function of a $\Delta^1_1$-random set is an example. The relation appears after relativizing, through the theorem that every set is $\Delta^0_2$ relative to a set avoiding a cone.

:::theorem[Downey, Greenberg, Harrison-Trainor, Patey, Turetsky]{#thm-hyperimmunity-cone}
If a problem admits preservation of hyperimmunity, it admits cone avoidance.
:::

:::proof{of=thm-hyperimmunity-cone}
Let $C \not\leq_T Z$, and $X \leq_T Z$ an instance. By :ref{#thm-delta2-cone-avoidance}, there is a set $W$ with $C \not\leq_T Z \oplus W$ and $C \leq_T W' \leq_T (Z \oplus W)'$. By :ref{#lem-delta2-modulus} relative to $Z \oplus W$, $C$ has a modulus $m$ relative to $Z \oplus W$ with $m \leq_T C \oplus Z \oplus W$. By :ref{#lem-modulus-hyperimmune} (1) with $Y = \emptyset$, $m$ is $(Z \oplus W)$-hyperimmune. The instance $X$ is computable in $Z \oplus W$, so preservation of hyperimmunity relative to $Z \oplus W$ gives a solution $Y$ such that $m$ is $(Z \oplus W \oplus Y)$-hyperimmune. By :ref{#lem-modulus-hyperimmune} (2), $C \not\leq_T Z \oplus W \oplus Y$, hence $C \not\leq_T Z \oplus Y$.
:::

The set $W$ is the price of relativization: $C$ itself need not have a modulus relative to $Z$, but it has one relative to $Z \oplus W$, and $W$ was chosen so as not to help computing $C$. The converse uses a construction in the opposite direction, which we admit.

:::theorem[Downey, Greenberg, Harrison-Trainor, Patey, Turetsky]{#thm-hyperimmune-modulus}
For every set $Z$ and every non-decreasing $Z$-hyperimmune function $f$, there are sets $W$ and $A$ such that $A \not\leq_T Z \oplus W$ and $f$ is a modulus of $A$ relative to $W$.
:::

:::corollary{#cor-hyperimmunity-equivalence}
A problem admits preservation of hyperimmunity if and only if it admits cone avoidance.
:::

:::proof{of=cor-hyperimmunity-equivalence}
One direction is :ref{#thm-hyperimmunity-cone}. Conversely, assume cone avoidance, and let $f$ be $Z$-hyperimmune and $X \leq_T Z$ an instance. By the first exercise, we may assume that $f$ is non-decreasing. Let $W$ and $A$ be given by :ref{#thm-hyperimmune-modulus}. Cone avoidance relative to $Z \oplus W$ gives a solution $Y$ with $A \not\leq_T Z \oplus W \oplus Y$. If some $g \leq_T Z \oplus Y$ dominated $f$, then $A \leq_T W \oplus g \leq_T Z \oplus W \oplus Y$. So $f$ is $(Z \oplus Y)$-hyperimmune.
:::

:::quiz[hyperimmunity and cone avoidance]
In the proof of :ref{#thm-hyperimmunity-cone}, why is the set $W$ needed?

- [x] Because $C$ is arbitrary, and only $\Delta^0_2$ sets are known to have moduli computable in them; $W$ makes $C$ a $\Delta^0_2$ set relative to $Z \oplus W$ without making it computable.
- [ ] Because the instance $X$ is not computable in $Z$.

  $X$ is computable in $Z$, hence in $Z \oplus W$.
- [ ] Because preservation of hyperimmunity only applies to computable instances.

  The definition is relativized to every $Z$; $W$ serves to produce a modulus.

---

Where is item 2 of :ref{#lem-modulus-hyperimmune} used, and why does it need $m \leq_T C \oplus Z$?

- [x] In the last step: if the solution computed $C$ together with $Z \oplus W$, it would compute $m$, which dominates itself; a modulus not computable from $C$ would give no contradiction.
- [ ] In the choice of $W$.

  $W$ comes from :ref{#thm-delta2-cone-avoidance}, independently of the modulus.
- [ ] To show that $m$ is hyperimmune relative to $Z \oplus W$.

  That is item 1.
:::

## Compact forcing questions

A positive answer to a question about a convergence must come with a bound on the value, so that the answers define a function that can be compared with $f$. This is the compactness of :ref{#def-question-compact}; the proof of :ref{#thm-question-hyperimmunity} applies to questions that are $\Sigma^0_1(\mathcal M)$-preserving, with the function $g$ of that proof computable in a member $X$ of $\mathcal M$.

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

1. The questions of Jockusch–Soare forcing and of computable Mathias forcing at level $1$ are compact and $\Sigma^0_1$-preserving (:ref{to="effective-forcing/forcing-question"}, :ref{#prop-mathias-question}); relativized to $Z$, they are $\Sigma^0_1(\{ Z \})$-preserving, and :ref{#thm-local-hyperimmunity} applies, with Jockusch–Soare forcing inside the paths of a $Z$-computable tree, and Mathias forcing for a $Z$-computable sequence of sets.
2. By item 1, $\mathsf{WKL}$ preserves $\mathcal W$, so :ref{#lem-scott-preservation} gives a Scott ideal $\mathcal M \subseteq \mathcal W$ containing $Z$. Let $g$ be a $Z$-computable coloring of pairs, and use the Seetapun forcing for $g$ (:ref{#def-seetapun-forcing}, with $g$ in place of $f$) with reservoirs in $\mathcal M$. If an infinite homogeneous set $H$ for $g$ belongs to $\mathcal M$, then $Z \oplus H \in \mathcal W$. Otherwise, both sides can always be extended (:ref{#lem-seetapun-infinity}). Given a condition $c$ and indices $e_0, e_1$, either the question about $\Phi^{Z \oplus G}_{e_0}(x)\converge$ on side $0$ or $\Phi^{Z \oplus G}_{e_1}(x)\converge$ on side $1$ is answered negatively for some $x$, and an extension forces the divergence at $x$ on some side; or it is answered positively for every $x$, and by :ref{#lem-seetapun-compact} the least bound $k$, found in an enumeration computable in some $X \in \mathcal M$, defines an $X$-computable function $h$. Then $h(x) < f(x)$ for some $x$, and an extension forces, on some side $i$, $\Phi^{Z \oplus G_i}_{e_i}(x)\converge < h(x) < f(x)$. As in :ref{#lem-disjunctive-construction}, one side $G_i$ of the resulting homogeneous sets satisfies: no $\Phi^{Z \oplus G_i}_e$ dominates $f$, that is, $f$ is $(Z \oplus G_i)$-hyperimmune.
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
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Relations between the avoidance properties of a problem: strong cone avoidance implies cone avoidance; cone avoidance is equivalent to preservation of one non-Sigma01 definition and to preservation of one hyperimmunity; forcing questions with the right properties give each preservation property"><defs><marker id="av-rel-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="225" y="14" width="150" height="40" rx="6" class="state"/><text x="300.0" y="38.0" text-anchor="middle" class="label">strong cone avoidance</text><rect x="225" y="112" width="150" height="40" rx="6" class="state"/><text x="300.0" y="136.0" text-anchor="middle" class="label">cone avoidance</text><rect x="10" y="104" width="170" height="56" rx="6" class="state"/><text x="95.0" y="128.0" text-anchor="middle" class="label">preservation of 1</text><text x="95.0" y="144.0" text-anchor="middle" class="label">non-Σ⁰₁ definition</text><rect x="420" y="104" width="170" height="56" rx="6" class="state"/><text x="505.0" y="128.0" text-anchor="middle" class="label">preservation of 1</text><text x="505.0" y="144.0" text-anchor="middle" class="label">hyperimmunity</text><rect x="10" y="222" width="170" height="56" rx="6" class="cell"/><text x="95.0" y="246.0" text-anchor="middle" class="label">Σ⁰₁-preserving</text><text x="95.0" y="262.0" text-anchor="middle" class="label">forcing question</text><rect x="420" y="222" width="170" height="56" rx="6" class="cell"/><text x="505.0" y="246.0" text-anchor="middle" class="label">Σ⁰₁-preserving compact</text><text x="505.0" y="262.0" text-anchor="middle" class="label">forcing question</text><line x1="300" y1="56" x2="300" y2="108" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="182" y1="124" x2="221" y2="124" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="223" y1="140" x2="184" y2="140" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#av-rel-arr)"/><line x1="418" y1="124" x2="379" y2="124" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="377" y1="140" x2="416" y2="140" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#av-rel-arr)"/><line x1="95" y1="220" x2="95" y2="164" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="505" y1="220" x2="505" y2="164" class="ink-stroke" stroke-width="1.3" marker-end="url(#av-rel-arr)"/><line x1="200" y1="262" x2="240" y2="262" class="ink-stroke" stroke-width="1.3"/><text x="248" y="266" class="label">proved in the course</text><line x1="200" y1="284" x2="240" y2="284" class="ink-stroke" stroke-width="1.3" stroke-dasharray="5 4"/><text x="248" y="288" class="label">admitted (Downey et al.)</text></svg>
:::

## Exercises

::::exercise{difficulty=1}
For a function $f$, let $F(n) = \max_{i \leq n} f(i)$. Show that for every set $W$, $f$ is $W$-hyperimmune if and only if $F$ is.

:::solution
Since $F \geq f$, a function dominating $F$ dominates $f$; so if $f$ is $W$-hyperimmune, so is $F$. Conversely, if $g \leq_T W$ dominates $f$, then $G(n) = \max_{i \leq n} g(i)$ is $W$-computable and $G(n) \geq g(i) \geq f(i)$ for every $i \leq n$, so $G$ dominates $F$.
:::
::::

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

::::exercise{difficulty=1}
Let $A$ be a non-computable computably dominated set (:ref{#def-computably-dominated}), and let $\mathsf P$ be the problem with the single instance $\emptyset$, whose single solution is $A$. Show that for every hyperimmune function $f$, $f$ is $A$-hyperimmune, but that $\mathsf P$ does not admit cone avoidance. Why does this not contradict :ref{#cor-hyperimmunity-equivalence}?

:::solution
Every $A$-computable function is dominated by a computable function, so a function dominating $f$ and computable in $A$ would give a computable function dominating $f$. The solution $A$ computes the non-computable set $A$, so cone avoidance fails with $Z = \emptyset$ and $C = A$. There is no contradiction: the property shown is the unrelativized version of preservation of hyperimmunity. Relative to $Z = A$ and with the instance $\emptyset \leq_T A$, the relativized version holds trivially, but relative to suitable other sets $Z$ it fails, as it must by :ref{#thm-hyperimmunity-cone}. This example is used by Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (Theorem 2.12) to separate the unrelativized versions.
:::
::::

## Notes and references

The duality between moduli and coding, and preservation of one hyperimmunity, follow the section *Preserving hyperimmunities* of the chapter *Cone avoidance* of Patey's monograph; the abstract theorem with a compact question is Lemma 2.6 of Monin and Patey (2019) according to the monograph. :ref{#thm-hyperimmunity-cone} is Corollary 2.10 of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022), whose proof goes through a variant of :ref{#thm-delta2-cone-avoidance} (their Lemma 2.8, attributed to Patey) and the modulus of a $\Delta^0_2$ set; :ref{#thm-hyperimmune-modulus} is their Lemma 2.6, and :ref{#cor-hyperimmunity-equivalence} their Corollary 2.7. Their Theorem 2.1 states the four equivalences, and Corollaries 3.4 and 3.6 the equivalence for $k$ hyperimmunities and $k$ definitions. The characterization of the sets with a modulus as the hyperarithmetic sets is due to Solovay (1978). Preservation of hyperimmunity for $\mathsf{WKL}$ is Theorem 2.4 of Jockusch and Soare (1972) (they build computably dominated paths); the results on $\mathsf{RT}^2_{k+1,k}$ and the Erdős–Moser theorem are in Patey (2017).

- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- R. M. Solovay, *Hyperarithmetically encodable sets*, Transactions of the American Mathematical Society 239 (1978), 99–122.
- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Preserving hyperimmunities*.
