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

A $\Pi^1_1$ set that is not hyperarithmetic, such as $\mathcal O$ or $\mathrm{WF}$, thus receives new elements at cofinally many stages below $\omega_1^{\mathrm{CK}}$, while each initial part of its enumeration is hyperarithmetic. This is the analogue of the fact that a c.e. set is the union of the finite sets $A_s$. There is one difference. A c.e. set is computable when the stage at which each $n$ is enumerated, if at all, is bounded by a computable function of $n$, and these bounds need not be uniform. For a $\Pi^1_1$ set, a single computable ordinal bounds all stages: by the boundedness theorem, a set of notations that is $\Sigma^1_1$, such as the range of a hyperarithmetic function with values in $\mathcal O$, is bounded below $\omega_1^{\mathrm{CK}}$ (first exercise of :ref{to="hyperarithmetic/kleene-theorem"}), so bounds that depend on $n$ can be replaced by their supremum.

The analogy with c.e. sets has a precise form: the $\Pi^1_1$ sets are exactly the sets that are $\Sigma_1$-definable over the level $L_{\omega_1^{\mathrm{CK}}}$ of Gödel's constructible hierarchy, and the hyperarithmetic sets are the subsets of $\nat$ that belong to it. Another precise form is the **Spector–Gandy theorem**: a set $A \subseteq \nat$ is $\Pi^1_1$ if and only if $A = \{ n : \exists X \in \mathrm{HYP}\ \psi(n, X) \}$ for some arithmetic formula $\psi$, so that $\Pi^1_1$ means "$\Sigma_1$ over the hyperarithmetic sets", as c.e. means $\Sigma_1$ over the finite sets. The direction from right to left is :ref{#cor-hyp-quantifier}. We admit the other direction (Moschovakis, Theorem 4F.3) and the characterization by $L_{\omega_1^{\mathrm{CK}}}$. They are the starting point of metarecursion theory, in which $\omega_1^{\mathrm{CK}}$ plays the role of $\omega$, and of $\alpha$-recursion theory, in which it is replaced by other admissible ordinals (Sacks, *Higher Recursion Theory*, Parts B and C).

:::quiz[stages]
In item 3 of :ref{#thm-pi11-stages}, where is the hypothesis that $A$ is $\Sigma^1_1$ used?

- [x] To make $\{ t(n) : n \in A \}$ a $\Sigma^1_1$ set of well-founded trees, to which the boundedness theorem applies.
- [ ] To make $A_{< \alpha}$ hyperarithmetic.

  This holds for every $\Pi^1_1$ set, by item 2.
- [ ] To show that every element of $A$ has a computable stage.

  This is item 1, which holds for every $\Pi^1_1$ set.
:::

## Exercises

::::exercise{difficulty=1}
Let $f$ be a partial function with $\Pi^1_1$ graph whose domain $D$ is $\Delta^1_1$. Show that $f$ is the restriction to $D$ of a hyperarithmetic function. Deduce that the function of :ref{#thm-kreisel-uniformization} is the restriction of a hyperarithmetic function whenever $\{ n : \exists m\ R(n, m) \}$ is $\Delta^1_1$.

:::solution
Let $g(n) = f(n)$ for $n \in D$, and $g(n) = 0$ otherwise. Then $g(n) = m$ if and only if $(n \in D \wedge f(n) = m) \vee (n \notin D \wedge m = 0)$, which is $\Pi^1_1$, since $D$ and its complement are $\Pi^1_1$. So $g$ is a total function with $\Pi^1_1$ graph, hyperarithmetic by :ref{#cor-total-pi11}. For the second statement, the domain of the function of :ref{#thm-kreisel-uniformization} is exactly $\{ n : \exists m\ R(n, m) \}$.
:::
::::

::::exercise{difficulty=2}
Let $A$ be a $\Pi^1_1$ set that is not $\Delta^1_1$. Show that for every computable ordinal $\alpha$, there is $n \in A$ with $\rho_n \geq \alpha$, and that the function $\alpha \mapsto$ "the least stage $\beta \geq \alpha$ at which some element enters $A$" is defined on all computable ordinals.

:::solution
If every $n \in A$ had $\rho_n < \alpha$, then $A = A_{< \alpha}$ would be $\Delta^1_1$ by :ref{#thm-pi11-stages}. So the set $\{ \rho_n : n \in A, \rho_n \geq \alpha \}$ is a non-empty set of ordinals, and has a least element $\beta$; it is a computable ordinal by item 1.
:::
::::

## Notes and references

Kreisel (1962) proved the uniformization theorem for $\Pi^1_1$ relations on numbers, and deduced the selection of hyperarithmetic functions. In Moschovakis's book, the theorem is the Easy Uniformization Theorem 4B.4, a consequence of the prewellordering property, and the selection of hyperarithmetic functions is the $\Delta$-Selection Principle 4B.5. The uniformization theorem for co-analytic relations on the reals is due to Kondo (1938), building on an idea of Novikov; Addison worked out the effective version (Moschovakis, Theorem 4E.4 and historical remark 21 of Section 4G). In second-order arithmetic, Kondo's theorem is equivalent to $\Pi^1_1$ comprehension over $\mathsf{ATR}_0$ (Simpson, Theorem VI.2.6). The characterization of the $\Pi^1_1$ sets by $\Sigma_1$ definability over $L_{\omega_1^{\mathrm{CK}}}$ belongs to the theory of admissible ordinals of Kripke and Platek, and underlies the metarecursion theory of Kreisel and Sacks (Sacks, Parts B and C). The Spector–Gandy theorem is due to Spector (1960) and Gandy (1960).

- G. Kreisel, *The axiom of choice and the class of hyperarithmetic functions*, Indagationes Mathematicae 24 (1962), 307–319.
- M. Kondo, *Sur l'uniformisation des complémentaires analytiques et les ensembles projectifs de la seconde classe*, Japanese Journal of Mathematics 15 (1938), 197–230.
- B. Monin and L. Patey, *Computability theory*, chapter *Beyond hyperarithmetic*, section *Analogies between Π¹₁ sets and c.e. sets* (Kreisel's uniformization and total Π¹₁ functions), and chapter *Σ¹₁ and Π¹₁ classes*, section *Study of a very special Π¹₁ class* (uniformization of Π¹₁ classes).
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section VI.2.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Sections 4B, 4E and 4F.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Section 36.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Parts B and C.
