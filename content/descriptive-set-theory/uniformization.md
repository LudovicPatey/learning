---
title: Uniformization and stages
summary: Kreisel's uniformization theorem for Π¹₁ relations on numbers; total Π¹₁ functions are hyperarithmetic; a Π¹₁ set is the increasing union of hyperarithmetic stages along ω₁ᶜᵏ, and it is Δ¹₁ exactly when its stages are bounded.
duration: 40
prerequisites: [reduction]
---

If $R \subseteq \nat^2$ is c.e. and every $n$ has some $m$ with $R(n, m)$, a computable function selects such an $m$: the first one enumerated. The same selection works for $\Pi^1_1$ relations, with the stages of :ref{#def-pi11-stage} in place of the steps of an enumeration. The resulting function has a $\Pi^1_1$ graph, and when it is total, it is hyperarithmetic. The obvious alternative, choosing the least $m$ with $R(n, m)$, does not work: it requires knowing that $R(n, k)$ fails for the smaller $k$, a $\Sigma^1_1$ condition. Stage comparison avoids negative information, as the "first enumerated" selection does for c.e. relations.

The second part of the lesson describes the stages of a $\Pi^1_1$ set from below: the elements that enter before a computable stage form a hyperarithmetic set, and these sets exhaust the $\Pi^1_1$ set at $\omega_1^{\mathrm{CK}}$. A $\Pi^1_1$ set is hyperarithmetic exactly when its stages are bounded below $\omega_1^{\mathrm{CK}}$; the proof is an application of Spector's boundedness theorem (:ref{#thm-boundedness}), the technique of the proof of Kleene's theorem.

## Uniformization

:::theorem[Kreisel]{#thm-kreisel-uniformization}
Let $R \subseteq \nat^2$ be $\Pi^1_1$. There is a partial function $f$ with $\Pi^1_1$ graph such that, for every $n$, if $R(n, m)$ holds for some $m$, then $f(n)$ is defined and $R(n, f(n))$ holds.
:::

:::proof{of=thm-kreisel-uniformization}
This is stage comparison. Apply :ref{#def-pi11-stage} to the $\Pi^1_1$ set $\{ \langle n, m \rangle : R(n, m) \}$, and write $\leq^*$, $<^*$ for its stage comparison relations, which are $\Pi^1_1$ by :ref{#thm-stage-comparison}. Let
$$
f(n) = m \iff \forall k\ \big(\langle n, m \rangle \leq^* \langle n, k \rangle\big) \wedge \forall k < m\ \big(\langle n, m \rangle <^* \langle n, k \rangle\big).
$$
In words: $\langle n, m \rangle$ enters the set at the least stage among the pairs $\langle n, k \rangle$, and $m$ is the least number with this stage. A number quantifier in front of a $\Pi^1_1$ formula gives a $\Pi^1_1$ formula, so the graph is $\Pi^1_1$. The first condition implies $R(n, m)$. If $R(n, m) \wedge R(n, m')$ with both $m$ and $m'$ satisfying the definition, then their stages are equal, and the second condition gives $m \leq m'$ and $m' \leq m$; so $f$ is a function. If $R(n, k)$ holds for some $k$, the ordinals $\rho_{\langle n, k \rangle}$ with $R(n, k)$ have a least element $\alpha$, and the least $m$ with $\rho_{\langle n, m \rangle} = \alpha$ satisfies the definition.
:::

:::figure[The selection of :ref{#thm-kreisel-uniformization} for a fixed $n$. Among the pairs $\langle n, m \rangle$ that enter the set, take those entering at the least stage $\alpha$, then the least $m$ among them. Choosing the least $m$ with $R(n, m)$ directly would require knowing that the smaller values fail, a $\Sigma^1_1$ condition.]
<svg class="fig" viewBox="0 0 600 306" width="600" role="img" aria-label="For a fixed n, the stage of each pair (n, m) plotted above m; the selected value is the least m among those whose pair enters at the least stage"><line x1="70" y1="210" x2="506" y2="210" class="axis"/><line x1="70" y1="210" x2="70" y2="60" class="axis"/><line x1="70" y1="30" x2="506" y2="30" class="axis" stroke-dasharray="2 3"/><text x="62" y="214" text-anchor="end" class="mrm" font-size="13">0</text><text x="62" y="64" text-anchor="end" class="mrm" font-size="13">ω<tspan font-size="9" dy="-6">CK</tspan><tspan font-size="9" dy="9" dx="-12">1</tspan></text><text x="62" y="34" text-anchor="end" class="mrm" font-size="13">∞</text><line x1="70" y1="162.3" x2="506" y2="162.3" class="muted-stroke" stroke-dasharray="4 3"/><text x="62" y="166.3" text-anchor="end" class="math" font-size="14">α</text><text x="106.0" y="230" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="106.0" cy="30.0" r="5" class="node"/><text x="158.0" y="230" text-anchor="middle" class="mrm" font-size="13">1</text><line x1="158.0" y1="210" x2="158.0" y2="107.7" class="muted-stroke" stroke-width="1"/><circle cx="158.0" cy="107.7" r="5" class="ink-fill"/><text x="210.0" y="230" text-anchor="middle" class="mrm" font-size="13">2</text><line x1="210.0" y1="210" x2="210.0" y2="162.3" class="muted-stroke" stroke-width="1"/><circle cx="210.0" cy="162.3" r="7" class="accent-fill"/><text x="262.0" y="230" text-anchor="middle" class="mrm" font-size="13">3</text><circle cx="262.0" cy="30.0" r="5" class="node"/><text x="314.0" y="230" text-anchor="middle" class="mrm" font-size="13">4</text><line x1="314.0" y1="210" x2="314.0" y2="162.3" class="muted-stroke" stroke-width="1"/><circle cx="314.0" cy="162.3" r="5" class="ink-fill"/><text x="366.0" y="230" text-anchor="middle" class="mrm" font-size="13">5</text><line x1="366.0" y1="210" x2="366.0" y2="135.0" class="muted-stroke" stroke-width="1"/><circle cx="366.0" cy="135.0" r="5" class="ink-fill"/><text x="418.0" y="230" text-anchor="middle" class="mrm" font-size="13">6</text><circle cx="418.0" cy="30.0" r="5" class="node"/><text x="470.0" y="230" text-anchor="middle" class="mrm" font-size="13">7</text><line x1="470.0" y1="210" x2="470.0" y2="73.6" class="muted-stroke" stroke-width="1"/><circle cx="470.0" cy="73.6" r="5" class="ink-fill"/><text x="298.0" y="252" text-anchor="middle" class="math" font-size="15">m</text><text x="70" y="280" class="label">dots: the stage of ⟨n, m⟩; hollow dots at ∞: R(n, m) fails. Two pairs enter at the least stage α;</text><text x="70" y="296" class="label">f(n) = 2, the least of them. The value 1, which enters later, is not chosen.</text></svg>
:::

:::example{#ex-ce-uniformization}
Let $R \subseteq \nat^2$ be c.e., with a computable enumeration $(R_s)$ of the set of pairs $\langle n, m \rangle$ with $R(n, m)$, and take the trees of :ref{#ex-ce-stages}, so that the stage of $\langle n, m \rangle$ is its stage of enumeration minus one. The function of :ref{#thm-kreisel-uniformization} is then: find the least $s$ such that some $\langle n, m \rangle$ belongs to $R_s$, and return the least such $m$. It is partial computable, and its domain is $\{ n : \exists m\ R(n, m) \}$. Kreisel's theorem extends this selection along the computable ordinals.
:::

:::corollary{#cor-total-pi11}
Every total function $f : \nat \to \nat$ whose graph is $\Pi^1_1$ is hyperarithmetic. Consequently, if $R \subseteq \nat^2$ is $\Pi^1_1$ and every $n$ has some $m$ with $R(n, m)$, there is a hyperarithmetic function $f$ with $R(n, f(n))$ for every $n$.
:::

:::proof{of=cor-total-pi11}
If $f$ is total, then $f(n) \neq m$ if and only if $\exists k\ (k \neq m \wedge f(n) = k)$, which is $\Pi^1_1$. So the graph is $\Delta^1_1$, hence hyperarithmetic by Kleene's theorem (:ref{#thm-kleene-delta11}), and so is $f$, computable from its graph. The second statement follows from :ref{#thm-kreisel-uniformization}.
:::

The same argument for c.e. sets shows that a total function with a c.e. graph is computable. The selection principle fails for $\Sigma^1_1$ relations. Let $Y_0$ and $Y_1$ be disjoint $\Pi^1_1$ sets without $\Delta^1_1$ separation (:ref{#prop-pi11-inseparable}), and let $R(n, 0)$ hold if $n \notin Y_0$ and $R(n, 1)$ hold if $n \notin Y_1$. This relation is $\Sigma^1_1$, and every $n$ has a value. If $f$ were a hyperarithmetic function with $R(n, f(n))$ for every $n$, then $f$ would take only the values $0$ and $1$, and the set $\{ n : f(n) = 1 \}$ would be $\Delta^1_1$, would contain $Y_0$ (where $R(n, 0)$ fails) and be disjoint from $Y_1$ (where $R(n, 1)$ fails): a $\Delta^1_1$ separation, which does not exist.

:::quiz[uniformization]
In the proof of :ref{#thm-kreisel-uniformization}, why is the least stage used before the least number $m$?

- [x] Because "$m$ is the least number with $R(n, m)$" requires $\neg R(n, k)$ for $k < m$, a $\Sigma^1_1$ condition, while the comparison of stages only uses the $\Pi^1_1$ relations $\leq^*$ and $<^*$.
- [ ] Because the least $m$ might not exist.

  If $R(n, m)$ holds for some $m$, the least one exists; the problem is the complexity of its definition.
- [ ] Because stages are numbers.

  Stages are ordinals, which is why their least element exists by well-ordering.

---

In :ref{#cor-total-pi11}, where is the totality of $f$ used?

- [x] To express $f(n) \neq m$ as "$f(n)$ is some other value", which is $\Pi^1_1$; for a partial function, $f(n) \neq m$ also holds when $f(n)$ is undefined, a condition with no $\Pi^1_1$ definition in general.
- [ ] To make the graph of $f$ a $\Pi^1_1$ set.

  The graph is $\Pi^1_1$ by hypothesis.
- [ ] To apply :ref{#thm-kreisel-uniformization}.

  The first statement does not use the uniformization theorem.
:::

::::exercise{#ex-delta11-domain difficulty=1 objective="Extend a partial function with $\Pi^1_1$ graph and $\Delta^1_1$ domain to a total hyperarithmetic function."}
Let $f$ be a partial function with $\Pi^1_1$ graph whose domain $D$ is $\Delta^1_1$. Show that $f$ is the restriction to $D$ of a hyperarithmetic function. Deduce that the function of :ref{#thm-kreisel-uniformization} is the restriction of a hyperarithmetic function whenever $\{ n : \exists m\ R(n, m) \}$ is $\Delta^1_1$.

:::solution
Let $g(n) = f(n)$ for $n \in D$, and $g(n) = 0$ otherwise. Then $g(n) = m$ if and only if $(n \in D \wedge f(n) = m) \vee (n \notin D \wedge m = 0)$, which is $\Pi^1_1$, since $D$ and its complement are $\Pi^1_1$. So $g$ is a total function with $\Pi^1_1$ graph, hyperarithmetic by :ref{#cor-total-pi11}. For the second statement, the domain of the function of :ref{#thm-kreisel-uniformization} is exactly $\{ n : \exists m\ R(n, m) \}$.
:::
::::

The proof relativizes uniformly to an oracle. If $R \subseteq \cs \times \nat \times \nat$ is a $\Pi^1_1$ relation, defined by a formula with a set variable $X$, the normal form theorem applied with $X$ as a parameter gives trees $T_{X, k}$ computable in $X$, uniformly in $k$, and :ref{#lem-rank-comparison} holds for arbitrary trees. The formulas of :ref{#thm-stage-comparison} and of the proof above, with $X$ as a parameter, define a $\Pi^1_1$ relation $F \subseteq \cs \times \nat \times \nat$ such that, for every $X$, the section $F(X, \cdot, \cdot)$ is the graph of a partial function uniformizing $R(X, \cdot, \cdot)$. Selecting a set rather than a number is much harder. For a $\Pi^1_1$ relation $R \subseteq \cs \times \cs$, there is still a partial function with $\Pi^1_1$ graph selecting some $Y$ with $R(X, Y)$ whenever there is one: this is the Novikov–Kondo–Addison uniformization theorem, whose proof needs a finer analysis of $\Pi^1_1$ classes (scales, in Moschovakis's treatment), and which is beyond this course.

## Stages from below

Stage comparison compares stages with each other. This section looks at the sets of elements that enter before a fixed stage, the analogues of the finite sets $A_s$ enumerated by stage $s$ of a c.e. set.

Let $A$ be a $\Pi^1_1$ set with stages $\rho_n = \rho(T_n)$ as in :ref{#def-pi11-stage}. For $\alpha \leq \omega_1^{\mathrm{CK}}$, let $A_{< \alpha} = \{ n : \rho_n < \alpha \}$ be the set of elements of $A$ that enter before stage $\alpha$.

:::example{#ex-ce-stages-below}
For the trees of :ref{#ex-ce-stages}, the stage of $n$ is less than $k$ exactly when $n$ is enumerated by step $k$ of the enumeration, so $A_{< k} = A_k$ for every $k \in \nat$, and $A = A_{< \omega}$.
:::

:::theorem{#thm-pi11-stages}
Let $A$ be a $\Pi^1_1$ set, with stages given by uniformly computable trees $(T_n)$.

1. $A = A_{< \omega_1^{\mathrm{CK}}}$: every element of $A$ enters at a computable stage.
2. For every computable ordinal $\alpha$, the set $A_{< \alpha}$ is hyperarithmetic.
3. $A$ is $\Delta^1_1$ if and only if $A = A_{< \alpha}$ for some computable ordinal $\alpha$.
:::

:::proof{of=thm-pi11-stages}
1. A computable well-founded tree has a computable Kleene–Brouwer ordering, which is a well-ordering of type at least its rank (:ref{#thm-kleene-brouwer}); so its rank is less than $\omega_1^{\mathrm{CK}}$.
2. Let $t(n)$ be an index of $T_n$, computable from $n$. Then $n \in A_{< \alpha}$ if and only if $t(n) \in \mathrm{WF}_{< \alpha}$, which is hyperarithmetic by :ref{#lem-wf-rank-hyp}.
3. If $A = A_{< \alpha}$, it is hyperarithmetic by item 2, hence $\Delta^1_1$. Conversely, if $A$ is $\Delta^1_1$, then $\{ t(n) : n \in A \}$ is a $\Sigma^1_1$ set of indices of computable well-founded trees. By the boundedness theorem, in the form used in the proof of :ref{#thm-kleene-delta11}, their ranks have a supremum $\gamma < \omega_1^{\mathrm{CK}}$. With $\alpha = \gamma + 1$, a computable ordinal, every $n \in A$ has $\rho_n < \alpha$, and $A = A_{< \alpha}$.
:::

A $\Pi^1_1$ set that is not hyperarithmetic, such as $\mathcal O$ or $\mathrm{WF}$, thus receives new elements at cofinally many stages below $\omega_1^{\mathrm{CK}}$, while each initial part of its enumeration is hyperarithmetic. This is the analogue of the fact that a c.e. set is the union of the finite sets $A_s$. There is one difference. A c.e. set is computable when the stage at which each $n$ is enumerated, if at all, is bounded by a computable function of $n$, and these bounds need not be uniform. For a $\Pi^1_1$ set, a single computable ordinal bounds all stages: by the boundedness theorem, a set of notations that is $\Sigma^1_1$, such as the range of a hyperarithmetic function with values in $\mathcal O$, is bounded below $\omega_1^{\mathrm{CK}}$ (:ref{#ex-sigma11-notations-bounded}), so bounds that depend on $n$ can be replaced by their supremum.

The analogy with c.e. sets has a precise form: the $\Pi^1_1$ sets are exactly the sets that are $\Sigma_1$-definable over the level $L_{\omega_1^{\mathrm{CK}}}$ of Gödel's constructible hierarchy, and the hyperarithmetic sets are the subsets of $\nat$ that belong to it. Another precise form is the **Spector–Gandy theorem**: a set $A \subseteq \nat$ is $\Pi^1_1$ if and only if $A = \{ n : \exists X \in \mathrm{HYP}\ \psi(n, X) \}$ for some arithmetic formula $\psi$, so that $\Pi^1_1$ means "$\Sigma_1$ over the hyperarithmetic sets", as c.e. means $\Sigma_1$ over the finite sets. The direction from right to left is :ref{#cor-hyp-quantifier}. We admit the other direction (Moschovakis, Theorem 4F.3) and the characterization by $L_{\omega_1^{\mathrm{CK}}}$. They are the starting point of metarecursion theory, in which $\omega_1^{\mathrm{CK}}$ plays the role of $\omega$, and of $\alpha$-recursion theory, in which it is replaced by other admissible ordinals (Sacks, *Higher Recursion Theory*, Parts B and C).

:::quiz[stages]
In item 3 of :ref{#thm-pi11-stages}, where is the hypothesis that $A$ is $\Sigma^1_1$ used?

- [x] To make $\{ t(n) : n \in A \}$ a $\Sigma^1_1$ set of well-founded trees, to which the boundedness theorem applies.
- [ ] To make $A_{< \alpha}$ hyperarithmetic.

  This holds for every $\Pi^1_1$ set, by item 2.
- [ ] To show that every element of $A$ has a computable stage.

  This is item 1, which holds for every $\Pi^1_1$ set.
:::

## Notes and references

Kreisel (1962) proved the uniformization theorem for $\Pi^1_1$ relations on numbers, and deduced the selection of hyperarithmetic functions. In Moschovakis's book, the theorem is the Easy Uniformization Theorem 4B.4, a consequence of the prewellordering property, and the selection of hyperarithmetic functions is the $\Delta$-Selection Principle 4B.5. The uniformization theorem for co-analytic relations on the reals is due to Kondo (1938), building on an idea of Novikov; Addison worked out the effective version (Moschovakis, Theorem 4E.4 and historical remark 21 of Section 4G). In second-order arithmetic, Kondo's theorem is equivalent to $\Pi^1_1$ comprehension over $\mathsf{ATR}_0$ (Simpson, Theorem VI.2.6). The characterization of the $\Pi^1_1$ sets by $\Sigma_1$ definability over $L_{\omega_1^{\mathrm{CK}}}$ belongs to the theory of admissible ordinals of Kripke and Platek, and underlies the metarecursion theory of Kreisel and Sacks (Sacks, Parts B and C). The Spector–Gandy theorem is due to Spector (1960) and Gandy (1960).

- G. Kreisel, *The axiom of choice and the class of hyperarithmetic functions*, Indagationes Mathematicae 24 (1962), 307–319.
- M. Kondo, *Sur l'uniformisation des complémentaires analytiques et les ensembles projectifs de la seconde classe*, Japanese Journal of Mathematics 15 (1938), 197–230.
- B. Monin and L. Patey, *Computability theory*, chapter *Beyond hyperarithmetic*, section *Analogies between Π¹₁ sets and c.e. sets* (Kreisel's uniformization and total Π¹₁ functions), and chapter *Σ¹₁ and Π¹₁ classes*, section *Study of a very special Π¹₁ class* (uniformization of Π¹₁ classes).
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section VI.2.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Sections 4B, 4E and 4F.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Section 36.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Parts B and C.

:::::exercises
::::exercise{#ex-unbounded-stages difficulty=2 objective="See that a $\Pi^1_1$ set that is not $\Delta^1_1$ receives new elements above every computable stage."}
Let $A$ be a $\Pi^1_1$ set that is not $\Delta^1_1$. Show that for every computable ordinal $\alpha$, there is $n \in A$ with $\rho_n \geq \alpha$, and that the function $\alpha \mapsto$ "the least stage $\beta \geq \alpha$ at which some element enters $A$" is defined on all computable ordinals.

:::solution
If every $n \in A$ had $\rho_n < \alpha$, then $A = A_{< \alpha}$ would be $\Delta^1_1$ by :ref{#thm-pi11-stages}. So the set $\{ \rho_n : n \in A, \rho_n \geq \alpha \}$ is a non-empty set of ordinals, and has a least element $\beta$; it is a computable ordinal by item 1.
:::
::::

::::exercise{#ex-uniformization-reduction difficulty=1 objective="Derive the reduction property from Kreisel's uniformization theorem." lessons="reduction"}
Deduce the reduction property (:ref{#thm-pi11-reduction}) from :ref{#thm-kreisel-uniformization}.

:::solution
Let $B$ and $C$ be $\Pi^1_1$ sets, and let $R(n, i)$ hold if $i = 0$ and $n \in B$, or $i = 1$ and $n \in C$. This relation is $\Pi^1_1$. Let $f$ be a partial function with $\Pi^1_1$ graph given by :ref{#thm-kreisel-uniformization}, and let
$$
B' = \{ n : f(n) = 0 \} \cap B, \qquad C' = \{ n : f(n) = 1 \} \cap C.
$$
Both are $\Pi^1_1$, as intersections of $\Pi^1_1$ sets. They are disjoint since $f$ is a function, and $B' \subseteq B$, $C' \subseteq C$. If $n \in B \cup C$, then $R(n, i)$ holds for some $i$, so $f(n)$ is defined and $R(n, f(n))$ holds: either $f(n) = 0$ and $n \in B$, so $n \in B'$, or $f(n) = 1$ and $n \in C$, so $n \in C'$. Hence $B' \cup C' = B \cup C$. (The intersections with $B$ and $C$ are there because the statement of the theorem says nothing about $f(n)$ when no $m$ satisfies $R(n, m)$.)
:::
::::

::::exercise{#ex-pi11-range difficulty=1 objective="See where the analogy between $\Pi^1_1$ and c.e. sets breaks down for ranges of total functions."}
Show that the range of a total function $f : \nat \to \nat$ with $\Pi^1_1$ graph is $\Delta^1_1$, and that every non-empty $\Delta^1_1$ set is the range of such a function. Deduce that $\mathcal O$ is not the range of a total function with $\Pi^1_1$ graph, although every non-empty c.e. set is the range of a total computable function.

:::solution
Let $f$ be total with $\Pi^1_1$ graph. As in the proof of :ref{#cor-total-pi11}, the graph is $\Delta^1_1$: $f(n) \neq m$ if and only if $\exists k\ (k \neq m \wedge f(n) = k)$. Then $m$ belongs to the range if and only if $\exists n\ f(n) = m$, a number quantifier in front of a $\Delta^1_1$ relation; the result is both $\Pi^1_1$ and $\Sigma^1_1$, since both classes are closed under number quantifiers. Conversely, let $D$ be $\Delta^1_1$ and $d \in D$. Let $f(n) = n$ if $n \in D$ and $f(n) = d$ otherwise. Then $f(n) = m$ if and only if $(n \in D \wedge m = n) \vee (n \notin D \wedge m = d)$, a $\Pi^1_1$ condition since $D$ and its complement are $\Pi^1_1$; and the range of $f$ is $D$.

The set $\mathcal O$ is not $\Sigma^1_1$: every $\Pi^1_1$ set is many-one reducible to it (:ref{#thm-o-complete}), so if $\mathcal O$ were $\Sigma^1_1$, every $\Pi^1_1$ set would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}. So $\mathcal O$ is not $\Delta^1_1$, and not the range of a total function with $\Pi^1_1$ graph. The c.e. analogy holds with ordinal time instead: Monin and Patey show that a non-empty $\Pi^1_1$ set is the range of a total $\Pi^1_1$ function defined on $\mathcal O$, which enumerates it along the notations (chapter *Beyond hyperarithmetic*, section *Analogies between Π¹₁ sets and c.e. sets*).
:::
::::

::::exercise{#ex-domain-hypothesis difficulty=1 objective="See with a counterexample that the hypothesis of a $\Delta^1_1$ domain cannot be dropped when extending partial $\Pi^1_1$ functions." lessons="reduction"}
Show that there is a partial function $f$ with $\Pi^1_1$ graph and values in $\{0, 1\}$ that is not the restriction of any hyperarithmetic function. Compare with :ref{#ex-delta11-domain}.

:::solution
Let $Y_0$ and $Y_1$ be disjoint $\Pi^1_1$ sets without $\Delta^1_1$ separation (:ref{#prop-pi11-inseparable}), and let $f(n) = 0$ for $n \in Y_0$ and $f(n) = 1$ for $n \in Y_1$, undefined elsewhere. It is a function since $Y_0 \cap Y_1 = \emptyset$, and $f(n) = m$ if and only if $(m = 0 \wedge n \in Y_0) \vee (m = 1 \wedge n \in Y_1)$, which is $\Pi^1_1$. Suppose that a hyperarithmetic function $g$ extends $f$. Then $F = \{ n : g(n) = 0 \}$ is hyperarithmetic, hence $\Delta^1_1$; it contains $Y_0$, and it is disjoint from $Y_1$, on which $g = f = 1$. This contradicts the choice of $Y_0$ and $Y_1$. By :ref{#ex-delta11-domain}, the domain $Y_0 \cup Y_1$ of $f$, a $\Pi^1_1$ set, is therefore not $\Delta^1_1$.
:::
::::

::::exercise{#ex-total-relation-bound difficulty=2 objective="Apply boundedness to find a single computable stage by which a total $\Pi^1_1$ relation has a witness for every argument."}
Let $R \subseteq \nat^2$ be $\Pi^1_1$ with $\forall n\, \exists m\ R(n, m)$, and let the stages $\rho_k$ of $A = \{ \langle n, m \rangle : R(n, m) \}$ be given by uniformly computable trees $(T_k)$. Show that there is a computable ordinal $\alpha$ such that for every $n$, some $m$ satisfies $\rho_{\langle n, m \rangle} < \alpha$. Deduce that $R$ contains a $\Delta^1_1$ relation $R'$ with $\forall n\, \exists m\ R'(n, m)$.

:::solution
By :ref{#cor-total-pi11}, there is a hyperarithmetic function $f$ with $R(n, f(n))$ for every $n$. Its graph $G = \{ \langle n, f(n) \rangle : n \in \nat \}$ is hyperarithmetic, hence $\Delta^1_1$, and included in $A$. Let $t(k)$ be an index of $T_k$, computable from $k$. The set $\{ t(k) : k \in G \}$ is $\Sigma^1_1$, since $i$ belongs to it if and only if $\exists k\ (k \in G \wedge t(k) = i)$, and it consists of indices of well-founded computable trees. By the boundedness theorem in the form used in item 3 of :ref{#thm-pi11-stages}, their ranks have a supremum $\gamma < \omega_1^{\mathrm{CK}}$. With $\alpha = \gamma + 1$, every $n$ satisfies $\rho_{\langle n, f(n) \rangle} < \alpha$.

Let $R'(n, m)$ hold if $\langle n, m \rangle \in A_{< \alpha}$. Then $R' \subseteq R$, $R'$ is hyperarithmetic by item 2 of :ref{#thm-pi11-stages}, hence $\Delta^1_1$, and $R'(n, f(n))$ holds for every $n$. The bound $\alpha$ is uniform in $n$, as in the discussion after :ref{#thm-pi11-stages}.
:::
::::

::::exercise{#ex-stages-below-comparison difficulty=2 objective="Compare stages with the order types of computable well-orderings, and obtain a second proof that the sets $A_{< \alpha}$ are $\Delta^1_1$." lessons="norms"}
For an index $e$ of a computable linear order, let $S_e$ be the tree of finite sequences $\langle x_0, \dots, x_k \rangle$ of elements of the field of $L_e$ that are strictly decreasing for $L_e$, including the empty sequence.

1. Show that $\rho(S_e) = |L_e|$ if $e \in \mathrm{WO}$, and that $S_e$ is ill-founded otherwise.
2. Let $A$ be a $\Pi^1_1$ set with stages $\rho_n = \rho(T_n)$. Show that there are $\Pi^1_1$ relations $P, Q \subseteq \nat^2$ such that, for every $e \in \mathrm{WO}$, $\{ n : P(e, n) \} = A_{< |L_e|}$ and $\{ n : Q(e, n) \} = \nat \setminus A_{< |L_e|}$.
3. Deduce a second proof of item 2 of :ref{#thm-pi11-stages}, which uses rank comparison and Kleene's theorem in place of :ref{#lem-wf-rank-hyp}.

:::solution
1. For $\sigma \in S_e$ ending with $x$, the subtree $(S_e)_\sigma$ is the tree of strictly decreasing sequences of elements below $x$, that is, the tree built in the same way from the initial segment $L_{<x} = \{ y : y <_{L_e} x \}$. We show $\rho(S_W) = |W|$ for every well-ordering $W$, by induction on $|W|$, where $S_W$ is the tree of strictly decreasing sequences of $W$. By :ref{#def-tree-rank}, $\rho(S_W) = \sup \{ \rho(S_{W_{<x}}) + 1 : x \in W \} = \sup \{ |W_{<x}| + 1 : x \in W \}$, by the induction hypothesis applied to the proper initial segments $W_{<x}$, of smaller type. The types $|W_{<x}|$ are exactly the ordinals $\gamma < |W|$, so the supremum is $|W|$ (for $W$ empty, both sides are $0$). If $L_e$ is not a well-ordering, an infinite strictly descending sequence is a path of $S_e$.

2. The tree $S_e$ contains the empty sequence, and "$\sigma \in S_e$" is an arithmetic relation of $\sigma$ and $e$, which makes sense for every $e$. Let
$$
\begin{aligned}
P(e, n) &\iff n \in A \wedge \neg \big(\rho(S_e) \leq \rho(T_n)\big), \\
Q(e, n) &\iff \neg \exists k\ \big(\langle k \rangle \in S_e \wedge \rho(T_n) \leq \rho((S_e)_{\langle k \rangle})\big).
\end{aligned}
$$
By :ref{#lem-rank-comparison}, each comparison $\rho(\cdot) \leq \rho(\cdot)$ is the existence of a strictly monotone map, an existential function quantifier in front of an arithmetic formula, so $P$ and $Q$ are $\Pi^1_1$. Let $e \in \mathrm{WO}$, so that $S_e$ is well-founded of rank $|L_e|$. If $n \in A$, then $\rho_n$ is an ordinal, and $\rho_n < |L_e|$ if and only if $\rho(S_e) \leq \rho(T_n)$ fails; if $n \notin A$, both $P(e, n)$ and $\rho_n < |L_e|$ fail. So $P(e, \cdot)$ is $A_{< |L_e|}$. Since $S_e$ is well-founded, the display after :ref{#lem-rank-comparison} gives $\rho(T_n) < \rho(S_e)$ if and only if $\exists k\ (\langle k \rangle \in S_e \wedge \rho(T_n) \leq \rho((S_e)_{\langle k \rangle}))$; so $Q(e, n)$ holds if and only if $\rho_n \geq |L_e|$, that is, $n \notin A_{< |L_e|}$.

3. Let $\alpha$ be a computable ordinal and $e \in \mathrm{WO}$ with $|L_e| = \alpha$. Then $A_{< \alpha} = \{ n : P(e, n) \}$ and its complement $\{ n : Q(e, n) \}$ are $\Pi^1_1$, so $A_{< \alpha}$ is $\Delta^1_1$, hence hyperarithmetic by :ref{#thm-kleene-delta11}. This is stage comparison between the trees $T_n$ and a tree of known rank, the same technique as in :ref{#cor-initial-segments}, where the tree of known rank was some $T_n$ with $n \in A$.
:::
::::
:::::
