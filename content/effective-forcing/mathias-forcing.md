---
title: Mathias forcing and preservation
summary: The forcing question of computable Mathias forcing at level 1; cohesive sets that avoid a cone, preserve a hyperimmune function and are not PA; sufficiently generic sets are high, so there is no Σ⁰₂-preserving forcing question; the disjunctive question of Dzhafarov and Jockusch.
duration: 35
prerequisites: [forcing-question, immunity-growth/domination]
---

Mathias forcing is the main tool for building solutions to combinatorial principles, such as cohesive sets and homogeneous sets for colorings. The course on Ramsey's theorem proved cone avoidance for cohesiveness by a direct argument (:ref{to="ramsey-theorem/cone-avoidance"}). This lesson places that argument in the framework of the forcing question. At level $1$, computable Mathias forcing has a forcing question with all the properties of the previous lesson, which gives at once cohesive sets that avoid a cone, preserve a hyperimmune function and are not PA. At level $2$ the picture changes: sufficiently generic sets are high, and no forcing question can be $\Sigma^0_2$-preserving. The reason is that a reservoir is an infinite set, and questions about infinite sets, such as "is $X \cap R$ infinite?", are $\Pi^0_2$.

Recall the notion of forcing of :ref{#ex-forcing-notions}: conditions $(\sigma, X)$ with $X$ an infinite computable set and $\min X \geq |\sigma|$, given by $\sigma$ and an index of $X$. A string $\tau$ is **compatible** with $(\sigma, X)$ if $\sigma \preceq \tau$ and every $n$ with $|\sigma| \leq n < |\tau|$ and $\tau(n) = 1$ belongs to $X$. The members of $(\sigma, X)$ are the sets all of whose prefixes of length at least $|\sigma|$ are compatible with it.

## The forcing question at level 1

:::proposition{#prop-mathias-question}
For computable Mathias forcing, let $(\sigma, X) \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if $\Phi^\tau_e(\vec m)\converge$ for some string $\tau$ compatible with $(\sigma, X)$. This defines a forcing question for $\Sigma^0_1$ sentences, which is $\Sigma^0_1$-preserving, compact and merging, and even $\omega$-merging in the sense of :ref{#exr-sacks-dnc}.
:::

:::proof{of=prop-mathias-question}
*Property 1.* If $\tau$ is compatible and $\Phi^\tau_e(\vec m)\converge$, then $(\tau, X \setminus \{0, \dots, |\tau| - 1\})$ is a condition extending $(\sigma, X)$, whose reservoir is infinite and computable. All its members extend $\tau$, so they satisfy $\Phi^G_e(\vec m)\converge$.

*Property 2.* Suppose no compatible string makes the computation converge. If a member $G$ of $(\sigma, X)$ had $\Phi^G_e(\vec m)\converge$ with use $u$, the prefix $G \uh \max(u, |\sigma|)$ would be compatible, with a convergent computation. So $(\sigma, X)$ forces $\Phi^G_e(\vec m)\diverge$.

*Preservation.* Compatibility with $(\sigma, X)$ is decidable, since $X$ is computable; so the question is $\Sigma^0_1$ in $\vec m$.

*Compactness.* A compatible $\tau$ with $\Phi^\tau_e(m)\converge = v$ witnesses $(\sigma, X) \mathrel{?{\vdash}} \Phi^G_e(m)\converge < v + 1$.

*Merging.* If the answer is negative for each sentence of a family of $\Sigma^0_1$ sentences, finite or infinite, the proof of property 2 shows that $(\sigma, X)$ itself forces all their negations.
:::

The proof of property 1 shows why the reservoirs are required to be computable: the question searches through the strings compatible with the condition, a search that is effective only if membership in the reservoir is.

:::theorem{#thm-mathias-coh-preservation}
Let $\vec R = (R_i)$ be a computable sequence of sets, $C$ a non-computable set, and $f$ a hyperimmune function. There is an $\vec R$-cohesive set $G$ such that $C \not\leq_T G$, $f$ is hyperimmune relative to $G$, and $G$ computes no DNC function; in particular $G$ is not PA.
:::

:::proof{of=thm-mathias-coh-preservation}
Let $G$ be sufficiently generic for computable Mathias forcing. It is infinite and $\vec R$-cohesive by :ref{#ex-generic-notions}. By :ref{#prop-mathias-question}, the forcing question at level $1$ is $\Sigma^0_1$-preserving, compact and $\omega$-merging. So $C \not\leq_T G$ by :ref{#cor-question-jump-cone} with $n = 0$, $f$ is hyperimmune relative to $G$ by :ref{#thm-question-hyperimmunity}, and $G$ computes no DNC function by :ref{#exr-sacks-dnc}. A countable union of countable families of dense sets is countable, so a single sufficiently generic set has all these properties.
:::

Everything relativizes. For a set $Z$, take reservoirs computable in $Z$ and formulas built from functionals with oracle $G \oplus Z$. For every $Z$-computable sequence $\vec R$, every $C \not\leq_T Z$ and every $f$ hyperimmune relative to $Z$, this gives an $\vec R$-cohesive $G$ with $C \not\leq_T G \oplus Z$, $f$ hyperimmune relative to $G \oplus Z$, and $G \oplus Z$ not PA relative to $Z$. The first property is :ref{#thm-coh-cone-avoidance}, whose three cases are exactly the two answers of the forcing question and the contradiction with $C \not\leq_T Z$.

:::quiz[the Mathias forcing question]
In :ref{#prop-mathias-question}, why does a negative answer give a condition forcing divergence without any extension?

- [x] Because every member of $(\sigma, X)$ has its long prefixes compatible with the condition, so a convergent computation on a member would produce a compatible string with a convergent computation.
- [ ] Because the reservoir $X$ is infinite.

  Infinity of the reservoir is not used in property 2.
- [ ] Because $X$ is computable.

  Computability of $X$ is used for the definability of the question, not for property 2.

---

Why does the same question make the generic set avoid PA degrees, while it fails for Jockusch–Soare forcing?

- [x] Because a negative answer for two sentences is witnessed by the condition itself, which forces both negations; in Jockusch–Soare forcing the two divergence classes may be disjoint.
- [ ] Because Mathias conditions are not closed classes.

  The classes of members of Mathias conditions are closed.
- [ ] Because Mathias generic sets are infinite.

  Infinity plays no role in avoiding PA degrees.
:::

## Generic sets are high

:::proposition{#prop-mathias-dominant}
Let $G$ be sufficiently generic for computable Mathias forcing, and let $p_G$ be its principal function, which maps $n$ to the $n$-th element of $G$ in increasing order. Then $p_G$ eventually dominates every computable function. In particular $G$ is high.
:::

:::proof{of=prop-mathias-dominant}
Let $h$ be a total computable function, and $(\sigma, X)$ a condition. Let $k$ be the number of elements of $\sigma$, that is, of $n < |\sigma|$ with $\sigma(n) = 1$. Define $y_0 < y_1 < \cdots$ by letting $y_j$ be the least element of $X$ that is larger than $y_{j-1}$ and than $h(j + k)$. The set $Y = \{ y_j : j \in \nat \}$ is computable, infinite and contained in $X$, so $(\sigma, Y)$ extends $(\sigma, X)$. Let $G$ be a member of $(\sigma, Y)$ that is infinite. For $n \geq k$, the $n$-th element of $G$ is the $(n - k)$-th element of $G \setminus \{0, \dots, |\sigma| - 1\} \subseteq Y$, so it is at least $y_{n - k} \geq h(n)$. Hence $p_G(n) \geq h(n)$ for every $n \geq k$.

So for each computable $h$, the set of conditions whose infinite members have principal functions eventually dominating $h$ is dense. A sufficiently generic set is infinite and meets these sets, so $p_G$ is dominant (:ref{#def-dominant}), and $G$, which computes $p_G$, is high by Martin's theorem (:ref{#thm-martin-domination}).
:::

:::corollary{#cor-mathias-no-sigma2}
Computable Mathias forcing has no $\Sigma^0_2$-preserving forcing question.
:::

:::proof{of=cor-mathias-no-sigma2}
The complement $A$ of $\emptyset''$ is not $\Sigma^0_2$: otherwise $\emptyset''$ would be $\Delta^0_2$, hence computable in $\emptyset'$ by Post's theorem, contradicting :ref{#cor-hierarchy-strict}. If there were a $\Sigma^0_2$-preserving forcing question, :ref{#thm-question-preservation} would give, for every sufficiently generic $G$, that $A$ is not $\Sigma^0_2(G)$. But $G$ is high, so $A \leq_T \emptyset'' \leq_T G'$, and $A$ is $\Delta^0_2(G)$ by Post's theorem relativized.
:::

The obstruction is visible in the proof of cohesiveness. To make $G$ cohesive for a set $R$, the reservoir is replaced by $X \cap R$ or $X \setminus R$, whichever is infinite, and deciding which one is infinite is a $\Pi^0_2$ question. More generally, a negative answer to a question about $\Sigma^0_2$ sentences should produce a reservoir on which some computation is total, and the existence of an infinite computable subset with this property has no $\Sigma^0_2$ description. Constructions of cohesive sets of low₂ degree (:ref{to="ramsey-theorem/cohesiveness"}) avoid the problem by not working with sufficiently generic sets: they build one sequence of conditions effectively in $\emptyset''$.

:::quiz[highness of Mathias generic sets]
In the proof of :ref{#prop-mathias-dominant}, why is the new reservoir chosen inside $X$ with its $j$-th element above $h(j + k)$, rather than simply above $h(j)$?

- [x] Because the $n$-th element of $G$ is the $(n - k)$-th element taken from the reservoir, the first $k$ elements coming from $\sigma$; the shift makes the bound $h(n)$ apply at position $n$.
- [ ] Because $h$ is increasing.

  Nothing is assumed about $h$ besides computability and totality.
- [ ] Because $G$ must contain all the elements of $Y$.

  $G$ may omit elements of $Y$; omitting them only makes the later elements of $G$ larger.
:::

## The disjunctive question of Dzhafarov and Jockusch

The proof of strong cone avoidance for the pigeonhole principle (:ref{#thm-dj-cone-avoidance}) uses a variant of Mathias forcing whose conditions $(\sigma_0, \sigma_1, X)$ build two sets $G^0 \subseteq A$ and $G^1 \subseteq \overline A$ at once, with reservoirs in a Scott ideal $\mathcal I$, and requirements that are disjunctions: "$\Phi^{G^0}_{e_0} \neq C$ or $\Phi^{G^1}_{e_1} \neq C$". The relation "$c$ answers $(x, v)$" of that proof is a forcing question for these disjunctions: a positive answer, applied to the partition $(A, \overline A)$, gives an extension forcing $\Phi^{G^i}_{e_i}(x)\converge = v$ on one side $i$; a negative answer, witnessed by a partition in $\mathcal I$, gives an extension forcing that $\Phi^{G^i}_{e_i}(x)$ does not converge to $v$, on one side. The question does not mention $A$, and it is $\Sigma^0_1$ relative to $Z \oplus X$, a member of $\mathcal I$. The three cases of that proof are then the argument of :ref{#thm-question-preservation} at level $1$, relative to a member of $\mathcal I$: the set $W$ of answered pairs plays the role of $U$, and it cannot coincide with the graph of $C$, since $C \notin \mathcal I$.

This is the general shape of the forcing questions used for Ramsey-type theorems: the question is asked about all instances of a problem at once, so that its complexity does not depend on the particular instance, and a negative answer is witnessed inside a class of simple sets closed under the operations of the construction.

## Exercises

::::exercise{difficulty=1}
Show that every sufficiently generic set for computable Mathias forcing is **r-cohesive**, that is, cohesive for the sequence of all computable sets, and is not computably dominated.

:::solution
The computable sets form a countable family, so the dense sets of :ref{#ex-generic-notions} for each of them can be met at once: every sufficiently generic set $G$ satisfies $G \subseteq^* R$ or $G \subseteq^* \overline R$ for every computable $R$. By :ref{#prop-mathias-dominant}, $G$ computes $p_G$, which eventually dominates every computable function; a computable function $g$ dominating $p_G$ would be eventually dominated by $p_G$, and so would $g + 1$, which is impossible. So $p_G$ is not dominated by any computable function, and $G$ is not computably dominated.
:::
::::

::::exercise{difficulty=2}
Let $Z$ be a set, $\vec R$ a $Z$-computable sequence and $C \not\leq_T Z$. Using Mathias forcing with $Z$-computable reservoirs, show that there is an $\vec R$-cohesive set $G$ with $C \not\leq_T G \oplus Z$ such that $G$ is high relative to $Z$, that is, $(G \oplus Z)' \geq_T Z''$.

:::solution
Conditions are pairs $(\sigma, X)$ with $X$ infinite and $Z$-computable. The question of :ref{#prop-mathias-question}, with functionals of the oracle $G \oplus Z$, is a forcing question; it is $\Sigma^0_1(Z)$-preserving, since compatibility is $Z$-computable. The proofs of :ref{#thm-question-preservation} and :ref{#cor-question-jump-cone} with $n = 0$, relativized to $Z$, give $C \not\leq_T G \oplus Z$ for every sufficiently generic $G$: one of $C$ and $\overline C$ is not $\Sigma^0_1(Z)$, hence not $\Sigma^0_1(G \oplus Z)$. Cohesiveness follows as before, since $X \cap R_i$ and $X \setminus R_i$ are $Z$-computable. The proof of :ref{#prop-mathias-dominant}, for $Z$-computable functions $h$, shows that $p_G$ eventually dominates every $Z$-computable function, and Martin's theorem relativized to $Z$ gives $(G \oplus Z)' \geq_T Z''$.
:::
::::

## Notes and references

Mathias forcing with computable reservoirs is presented by Hirschfeldt (Section 6.5, Definition 6.40) and by Dzhafarov and Mummert (Examples 7.2.5 and 7.2.10, Example 7.3.6 for highness, Example 7.3.9 for cohesiveness). Cone avoidance for cohesiveness is attributed to Cholak, Jockusch and Slaman (2001) by Dzhafarov and Mummert, and to Jockusch and Stephan (1993) by Hirschfeldt; preservation of hyperimmunity for Ramsey-type principles was studied systematically by Patey (2017). The interpretation of the Dzhafarov–Jockusch argument as a forcing question follows Monin and Patey, whose chapter *Effective forcing* presents the forcing question and its preservation properties in general, and whose paper *Pigeons do not jump high* (2019) designs forcing questions for the pigeonhole principle at level $2$.

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), doi:10.3233/COM-160062; arXiv:1501.07709.
- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics (2019), doi:10.1016/j.aim.2019.06.026.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 6.5.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 7.2–7.3.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*.
