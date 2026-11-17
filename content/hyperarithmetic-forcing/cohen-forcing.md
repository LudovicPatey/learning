---
title: Cohen forcing over the hyperarithmetic sets
summary: Cohen forcing for the language of the ramified analytic hierarchy; forcing existential sentences is Π¹₁; forcing equals truth for generic sets; a generic set preserves ω₁ᶜᵏ (Feferman); every non-hyperarithmetic set has a hyperarithmetically incomparable set.
duration: 35
prerequisites: [ramified-hierarchy, effective-forcing/forcing-relation]
---

Cohen forcing with finite strings builds 1-generic sets, which meet every c.e. dense set of strings. Over the hyperarithmetic hierarchy, the same conditions are used, but the sentences to be decided are the sentences of the ramified analytic hierarchy, which talk about all the sets hyperarithmetic in the generic set. Feferman introduced this forcing in 1965. Its first theorem is that a generic set does not collapse $\omega_1^{\mathrm{CK}}$: the generic extension $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ satisfies $\Delta^1_1$ comprehension, which by Kreisel's theorem is equivalent. The proof is a boundedness argument: the ordinal ranks needed to witness the instances of comprehension are chosen by a hyperarithmetic function, hence bounded below $\omega_1^{\mathrm{CK}}$.

The key technical fact is that forcing an existential sentence is a $\Pi^1_1$ relation, like truth. It turns the forcing construction into a $\Pi^1_1$ object, to which Kreisel's uniformization and Spector's boundedness apply, and it lets one show that a set defined by forcing is hyperarithmetic. The lesson ends with an application: every non-hyperarithmetic set has a set of incomparable hyperdegree.

## The forcing relation

A **condition** is a finite binary string $p$; it **extends** $q$, written $p \leq q$, if $p \succeq q$. A set $T$ **meets** $p$ if $p \prec T$. Sentences are those of $\mathcal L(\omega_1^{\mathrm{CK}}, \mathcal T)$, with $\wedge$, $\neg$ and $\exists$ as primitive connectives and quantifiers.

:::definition[Feferman]{#def-cohen-forcing-hyp}
The relation $p \Vdash \varphi$ ($p$ **forces** $\varphi$) is defined by recursion on the full ordinal rank and the logical complexity of the sentence $\varphi$:

1. $p \Vdash t = s$ if $t$ and $s$ have the same value; $p \Vdash t \in \mathcal T$ if $p(v) = 1$, where $v$ is the value of $t$;
2. $p \Vdash (\exists x)\varphi(x)$ if $p \Vdash \varphi(n)$ for some $n$;
3. $p \Vdash (\exists X^\alpha)\varphi(X^\alpha)$ if $p \Vdash \varphi(x_\theta)$ for some ranked formula $\theta(x)$ of rank at most $\alpha$;
4. $p \Vdash (\exists X)\varphi(X)$ if $p \Vdash (\exists X^\alpha)\varphi(X^\alpha)$ for some $\alpha < \omega_1^{\mathrm{CK}}$;
5. $p \Vdash \varphi \wedge \psi$ if $p \Vdash \varphi$ and $p \Vdash \psi$;
6. $p \Vdash \neg\varphi$ if no $q \leq p$ forces $\varphi$.
:::

Here $\varphi(x_\theta)$ is the result of replacing each $t \in X^\alpha$ by $\theta(t)$, as in the previous lesson; the recursion terminates because this substitution decreases full ordinal rank. As in the effective forcing course, clause 6 makes forcing a statement about all extensions: $p$ forces $\neg\varphi$ when $\varphi$ can never be forced below $p$.

:::proposition{#prop-cohen-hyp-basic}
For every sentence $\varphi$ and conditions $p, q$:

1. $p$ does not force both $\varphi$ and $\neg\varphi$;
2. some $q \leq p$ forces $\varphi$ or forces $\neg\varphi$;
3. if $p \Vdash \varphi$ and $q \leq p$, then $q \Vdash \varphi$.
:::

:::proof{of=prop-cohen-hyp-basic}
1. If $p \Vdash \neg\varphi$, then no extension of $p$, in particular not $p$, forces $\varphi$.
2. If no $q \leq p$ forces $\varphi$, then $p \Vdash \neg\varphi$.
3. By induction on the definition: the clauses 1 to 5 are preserved by extension, since a longer string has the same values on the domain of the shorter one, and for clause 6, the extensions of $q$ are extensions of $p$.
:::

:::lemma{#lem-cohen-hyp-pi11}
The relation "$p \Vdash \varphi$", restricted to existential sentences $\varphi$, is $\Pi^1_1$. Restricted to ranked sentences of rank less than $|a|$, it is $\Delta^1_1$, uniformly in $a \in \mathcal O_1$.
:::

:::proof{of=lem-cohen-hyp-pi11}
As in the proof of :ref{#lem-ramified-truth}, with triples in place of pairs: $X$ is a set of triples $(p, \varphi, 1)$, recording that $p \Vdash \varphi$, and $(p, \varphi, 0)$, recording that $p \not\Vdash \varphi$, so that negation is handled monotonically. For instance, clause 6 becomes: if $(q, \varphi, 0) \in X$ for every $q \leq p$, then $(p, \neg\varphi, 1) \in X$; and if $(q, \varphi, 1) \in X$ for some $q \leq p$, then $(p, \neg\varphi, 0) \in X$. The quantifiers over the extensions $q$ of $p$ are number quantifiers. For ranked sentences, the clauses are $\Sigma^1_1$ closure conditions $A(X)$, the forcing relation and its complement form the least set satisfying them, and $p \Vdash \varphi$ if and only if $(\forall X)(A(X) \to (p, \varphi, 1) \in X)$. An existential sentence is forced if and only if a ranked instance is, as in clause 4. (Sacks, Lemma IV.3.2.)
:::

## Generic sets

A set $T$ is **generic** if for every sentence $\varphi$ there is a condition $p \prec T$ with $p \Vdash \varphi$ or $p \Vdash \neg\varphi$. Generic sets exist, and every condition is met by one: enumerate the countably many sentences, and extend the condition successively to decide each of them, by :ref{#prop-cohen-hyp-basic} (2); the sentences $n \in \mathcal T$ are among them, so the conditions determine a unique set.

:::lemma[Forcing equals truth]{#lem-cohen-hyp-truth}
Let $T$ be generic. For every sentence $\varphi$, $\mathcal M(\omega_1^{\mathrm{CK}}, T) \models \varphi$ if and only if $p \Vdash \varphi$ for some $p \prec T$.
:::

:::proof{of=lem-cohen-hyp-truth}
By induction on full ordinal rank and logical complexity. The atomic case holds since $p \prec T$. The existential clauses and conjunction follow from the induction hypothesis; for conjunction, the two conditions are prefixes of $T$, so the longer one forces both sentences by :ref{#prop-cohen-hyp-basic} (3). For a negation $\neg\varphi$: if $p \prec T$ forces $\neg\varphi$ and $\varphi$ were true, some $q \prec T$ would force $\varphi$ by induction, and the longer of $p$ and $q$ would force $\varphi$ and $\neg\varphi$, contradicting :ref{#prop-cohen-hyp-basic} (1). Conversely, if $\neg\varphi$ is true, no $q \prec T$ forces $\varphi$ by induction, and since $T$ is generic, some $p \prec T$ forces $\varphi$ or $\neg\varphi$; it forces $\neg\varphi$. (Sacks, Lemma IV.3.5.)
:::

## Generic sets preserve ω₁ᶜᵏ

:::theorem[Feferman]{#thm-feferman}
If $T$ is generic, then $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ satisfies $\Delta^1_1$ comprehension. Consequently $\omega_1^T = \omega_1^{\mathrm{CK}}$ and $\mathcal M(\omega_1^{\mathrm{CK}}, T) = \mathrm{HYP}(T)$.
:::

The difficulty is that $(\exists Y) A(x, Y)$ may need witnesses $Y$ of ranks unbounded below $\omega_1^{\mathrm{CK}}$ as $x$ varies, so that the set it defines is not in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$. Forcing reduces the choice of these ranks to a $\Pi^1_1$ relation between conditions, numbers and notations; Kreisel's uniformization turns it into a hyperarithmetic function, and Spector's boundedness theorem bounds its values.

:::proof{of=thm-feferman}
Suppose that $\mathcal M(\omega_1^{\mathrm{CK}}, T) \models (\forall x)((\exists Y) A(x, Y) \leftrightarrow (\forall Z) B(x, Z))$, with $A$ and $B$ arithmetic and parameters in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, given by ranked formulas. Write $C(x, Y)$ for $A(x, Y) \vee \neg B(x, Y)$. Then
$$
\mathcal M(\omega_1^{\mathrm{CK}}, T) \models (\forall x)(\exists Y) C(x, Y), \tag{1}
$$
since for each $x$ either $(\exists Y)A(x, Y)$ holds, or $(\forall Z)B(x, Z)$ fails. By :ref{#lem-cohen-hyp-truth}, some $p \prec T$ forces (1), that is $\neg(\exists x)\neg(\exists Y) C(x, Y)$. By clause 6, no $q \leq p$ forces $\neg(\exists Y) C(n, Y)$ for any $n$; by clause 6 again, for every $q \leq p$ and every $n$ there is $r \leq q$ forcing $(\exists Y) C(n, Y)$, hence, by clause 4, a notation $a \in \mathcal O_1$ with $r \Vdash (\exists Y^{|a|}) C(n, Y^{|a|})$.

The relation between $(q, n)$ and $(r, a)$ expressed by "$r \leq q$, $a \in \mathcal O_1$ and $r \Vdash (\exists Y^{|a|}) C(n, Y^{|a|})$" is $\Pi^1_1$ by :ref{#lem-cohen-hyp-pi11}. By Kreisel's uniformization theorem (:ref{#thm-kreisel-uniformization}), it is uniformized by a $\Pi^1_1$ partial function, which is total on the computable set of pairs $(q, n)$ with $q \leq p$, hence hyperarithmetic (:ref{#cor-total-pi11}). Its values $a$ form a hyperarithmetic, hence $\Sigma^1_1$, subset of $\mathcal O_1$, which is bounded below some $\gamma < \omega_1^{\mathrm{CK}}$ by Spector's boundedness theorem (:ref{#thm-boundedness}). A sentence $(\exists Y^{\beta}) C(n, Y^\beta)$ forced by $r$ remains forced with $\gamma \geq \beta$ in place of $\beta$, the same witness formulas being allowed. So every $q \leq p$ has an extension forcing $(\exists Y^\gamma) C(n, Y^\gamma)$, for every $n$, and therefore $p \Vdash \neg(\exists x)\neg(\exists Y^\gamma) C(x, Y^\gamma)$. By :ref{#lem-cohen-hyp-truth},
$$
\mathcal M(\omega_1^{\mathrm{CK}}, T) \models (\forall x)(\exists Y^\gamma)\big(A(x, Y^\gamma) \vee \neg B(x, Y^\gamma)\big).
$$
Let $X = \{ n : (\exists Y^\gamma) A(n, Y^\gamma) \text{ is true} \}$, a member of $\mathcal M(\gamma + 1, T)$. If $n \in X$, then $(\exists Y) A(n, Y)$. If $n \notin X$, some $Y$ satisfies $\neg B(n, Y)$, so $(\forall Z)B(n, Z)$ fails, and so does $(\exists Y) A(n, Y)$. So $X$ witnesses the instance of comprehension. The consequences follow from :ref{#thm-ramified-comprehension}.
:::

:::quiz[Feferman's theorem]
In the proof of :ref{#thm-feferman}, why is it important that forcing existential sentences is $\Pi^1_1$ rather than merely definable?

- [x] Kreisel's uniformization applies to $\Pi^1_1$ relations, and gives a hyperarithmetic choice of the notations $a$, whose range is then bounded below $\omega_1^{\mathrm{CK}}$ by Spector's theorem.
- [ ] To show that generic sets exist.

  Existence only uses that there are countably many sentences.
- [ ] To show that forcing equals truth.

  The truth lemma holds whatever the complexity of the forcing relation.

---

Why does the bound $\gamma$ give a set in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$?

- [x] Because the definition $(\exists Y^\gamma) A(n, Y^\gamma)$ only quantifies over sets of rank $\gamma$, so it is a ranked formula of rank $\gamma + 1$, defining a member of $\mathcal M(\gamma + 1, T)$.
- [ ] Because $A$ is arithmetic.

  With an unranked quantifier, $(\exists Y) A(n, Y)$ is not ranked, and need not define a member.
- [ ] Because $\gamma$ is a successor ordinal.

  Any $\gamma < \omega_1^{\mathrm{CK}}$ would do.
:::

## Incomparable hyperdegrees

:::theorem{#thm-incomparable-hyp}
For every non-hyperarithmetic set $Z$, there is a generic set $T$ with $T \not\leq_h Z$ and $Z \not\leq_h T$.
:::

:::proof{of=thm-incomparable-hyp}
Let $Z_0, Z_1, \dots$ list the sets hyperarithmetic in $Z$, a countable family, and $\varphi_0, \varphi_1, \dots$ the sentences, and $\theta_0(x, y), \theta_1(x, y), \dots$ the ranked formulas with two free number variables. Build conditions $p_0 \geq p_1 \geq \cdots$, starting from the empty string. At step $i$:

1. extend $p_i$ to $q$ with $q(j) \neq Z_i(j)$ for some $j$ (take $j = |p_i|$);
2. extend $q$ to $q'$ deciding $\varphi_i$ (:ref{#prop-cohen-hyp-basic} (2));
3. consider $\theta = \theta_i$. If some $n$ has no extension $r \leq q'$ forcing $\theta(n, k)$ for any $k$, let $p_{i+1} = q'$. If every $n$ has such an $r$ and $k$, and the value $k$ is unique (no two extensions of $q'$ force $\theta(n, k)$ and $\theta(n, k')$ with $k \neq k'$), let $p_{i+1} = q'$. Otherwise, there are $n$, $k \neq k'$ and extensions of $q'$ forcing $\theta(n, k)$ and $\theta(n, k')$; one of $k, k'$ differs from $Z(n)$, and let $p_{i+1}$ be the corresponding extension.

Let $T = \bigcup_i p_i$. It is generic, by step 2, and differs from every $Z_i$, by step 1, so $T \not\leq_h Z$. By :ref{#thm-feferman}, $\mathrm{HYP}(T) = \mathcal M(\omega_1^{\mathrm{CK}}, T)$. Suppose $Z \leq_h T$. Then $Z$ is a member of $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, so for some $i$, $Z(n) = k$ if and only if $\theta_i(n, k)$ is true in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, for all $n$ and $k$. Consider step $i$, with $q' = q'_i \prec T$. In the first case, some $n$ has no extension of $q'$ forcing any $\theta_i(n, k)$; but $\theta_i(n, Z(n))$ is true, so some $r \prec T$ forces it by :ref{#lem-cohen-hyp-truth}, and the longer of $r$ and $q'$ is an extension of $q'$ that forces it, a contradiction. In the third case, $p_{i+1} \prec T$ forces $\theta_i(n, k)$ with $k \neq Z(n)$, so $\theta_i(n, k)$ is true and $Z(n) = k$, a contradiction. In the second case, define $\hat Z(n) = k$ if some $r \leq q'$ forces $\theta_i(n, k)$; this is a total function, its graph is $\Pi^1_1$ by :ref{#lem-cohen-hyp-pi11}, so it is hyperarithmetic, and $\hat Z = Z$: the true value $Z(n)$ is forced by some $r \prec T$ extending $q'$, and the forced value is unique. Then $Z$ is hyperarithmetic, a contradiction. So $Z \not\leq_h T$.
:::

The theorem gives, for instance, a set $T$ hyperarithmetically incomparable with $\mathcal O$, and two sets $T$, $Z$ of incomparable hyperdegrees, both preserving $\omega_1^{\mathrm{CK}}$ when $Z$ is taken generic.

::::exercise[Generic sets are not hyperarithmetic]{#ex-generic-not-hyp difficulty=1 objective="Use the truth lemma and the Kleene definitions of the H-sets to show that generic sets avoid HYP."}
Show that no generic set is hyperarithmetic.

:::solution
Let $T$ be generic and suppose $T = H$ is hyperarithmetic. By :ref{#lem-h-ranked}, there is a ranked formula $\eta(x)$, without $\mathcal T$, defining $H$ in $\mathcal M(\omega_1^{\mathrm{CK}}, S)$ for every $S$. The sentence $(\forall x)(x \in \mathcal T \leftrightarrow \eta(x))$ is true in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, so some $p \prec T$ forces it. Let $n = |p|$ and let $q = p\, i$ with $i = 1 - H(n)$. A generic set $T^* \succ q$ exists, and by :ref{#lem-cohen-hyp-truth} the sentence is true in $\mathcal M(\omega_1^{\mathrm{CK}}, T^*)$, so $T^* = H$; but $T^*(n) = i \neq H(n)$, a contradiction.
:::
::::

## Notes and references

Feferman (1965) introduced forcing over the ramified analytic hierarchy and proved that generic sets satisfy $\Delta^1_1$ comprehension; the presentation follows Sacks (Section IV.3: subsection 3.1, Lemma 3.2, Proposition 3.4, Lemma 3.5, Theorem 3.6). The theorem on incomparable hyperdegrees follows the proof of Chong and Yu (Proposition 5.2.7); Sacks derives incomparability from the two halves of a generic set (Exercise IV.3.15).

- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Section IV.3.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Section 5.2.

:::::exercises
::::exercise{#ex-generic-comeager difficulty=1 objective="See that genericity for the ramified language is a countable intersection of dense open conditions."}
Show that the class of generic sets is comeager in $\cs$.

:::solution
For a sentence $\varphi$, let $\mathcal U_\varphi$ be the class of sets $T$ that meet a condition forcing $\varphi$ or $\neg\varphi$. It is open, a union of basic open sets $[p]$, and dense, since every $p$ has an extension deciding $\varphi$ (:ref{#prop-cohen-hyp-basic} (2)). The generic sets form the intersection of the classes $\mathcal U_\varphi$ over the countably many sentences, a comeager class.
:::
::::

::::exercise{#ex-generic-1-generic difficulty=2 objective="Compare genericity for the ramified language with 1-genericity."}
Show that every generic set $T$ is 1-generic: for every c.e. set $W$ of strings, some prefix of $T$ belongs to $W$ or has no extension in $W$.

:::solution
For a string $\sigma$, let $\sigma \prec \mathcal T$ be the conjunction of the atomic formulas $i \in \mathcal T$ for $\sigma(i) = 1$ and of their negations for $\sigma(i) = 0$. A condition $q \succeq \sigma$ forces $\sigma \prec \mathcal T$: it forces $i \in \mathcal T$ when $q(i) = 1$, and forces $\neg(i \in \mathcal T)$ when $q(i) = 0$, since no extension of $q$ forces $i \in \mathcal T$. Let $\varphi$ be the rank $0$ sentence $(\exists x)(x \text{ codes a string in } W \wedge x \prec \mathcal T)$, where "$x$ codes a string in $W$" is an arithmetic formula. By genericity, some $p \prec T$ forces $\varphi$ or $\neg\varphi$. If $p \Vdash \varphi$, then $\varphi$ is true by :ref{#lem-cohen-hyp-truth}: some prefix of $T$ belongs to $W$. If $p \Vdash \neg\varphi$, then no $q \leq p$ forces $\varphi$; if some $q \succeq p$ extended a string $\sigma \in W$, then $q$ would force $\varphi$ with the witness $\sigma$. So $p$ has no extension in $W$.
:::
::::

::::exercise{#ex-generic-below-o-cone difficulty=1 objective="Combine Feferman's theorem with Spector's theorem."}
Show that no generic set $T$ satisfies $\mathcal O \leq_h T$.

:::solution
By :ref{#thm-feferman}, $\omega_1^T = \omega_1^{\mathrm{CK}}$, and by :ref{#thm-spector-collapse}, $\mathcal O \leq_h T$ would imply $\omega_1^T > \omega_1^{\mathrm{CK}}$.
:::
::::

::::exercise{#ex-generic-hyp-below-o difficulty=2 objective="Bound the complexity of a generic set by the complexity of the forcing relation."}
Show that there is a generic set $T \leq_T \mathcal O^{(\omega)}$, and deduce that there is a generic set $T \leq_h \mathcal O$.

:::solution
For a ranked sentence, forcing is $\Pi^1_1$ uniformly (:ref{#lem-cohen-hyp-pi11}), hence computable in $\mathcal O$. A sentence with $k$ unranked quantifiers and negations is handled by the clauses 4 and 6: clause 4 replaces an unranked quantifier by a number quantifier over the notations of $\mathcal O_1$, and clause 6 adds a number quantifier over the extensions of a condition. So, by induction on the logical complexity, "$p \Vdash \varphi$" is arithmetic in $\mathcal O$, uniformly in $\varphi$, with a number of quantifiers bounded in terms of $\varphi$; the whole relation is computable in $\mathcal O^{(\omega)}$. The construction of a generic set, which extends the current condition to the first extension deciding the next sentence, is then computable in $\mathcal O^{(\omega)}$, and so is $T$. Since $\mathcal O^{(\omega)}$ is hyperarithmetic in $\mathcal O$, $T \leq_h \mathcal O$. (Sacks, Exercise IV.3.18, asks for a generic set strictly below $\mathcal O$.)
:::
::::
:::::
