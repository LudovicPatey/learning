---
title: The Sacks–Tanaka theorem
summary: Almost no sequence computes a non-computable ordinal; the class of sequences collapsing ω₁ᶜᵏ is Π¹₁ and null; the proof by selection and boundedness; the measure of a Π¹₁ class is reached at its Δ¹₁ stages.
duration: 30
prerequisites: [pi11-measure, martin-lof-randomness/upper-cones]
---

A member $Y$ of a $\Pi^1_1$ class enters it at a stage below $\omega_1^Y$ (:ref{#fact-pi11-stages}). For most sequences $\omega_1^Y = \omega_1^{\mathrm{CK}}$, and they enter at a computable stage, that is, in a $\Delta^1_1$ stage of the class. This lesson proves the theorem that makes "most" precise: the sequences $Y$ with $\omega_1^Y > \omega_1^{\mathrm{CK}}$ form a null class. It is the key to $\Pi^1_1$-randomness in the next lesson, and to the results on $\Sigma^1_1$ null classes and hyperarithmetic reducibility in the last one. Its proof introduces the technique that all these results share: a hyperarithmetic selection of computable stages, followed by the boundedness theorem.

## Collapsing ω₁ᶜᵏ

A sequence $Y$ **collapses** $\omega_1^{\mathrm{CK}}$ if $\omega_1^Y > \omega_1^{\mathrm{CK}}$, that is, if some $Y$-computable well-ordering has type $\omega_1^{\mathrm{CK}}$. Kleene's $\mathcal O$ collapses $\omega_1^{\mathrm{CK}}$ (:ref{#prop-omega1-relative}), and so does every sequence coding a well-ordering of type at least $\omega_1^{\mathrm{CK}}$. The following theorem is the higher analogue of the fact that almost no sequence computes a given non-computable set (:ref{#thm-sacks}).

:::theorem[Sacks, Tanaka]{#thm-sacks-tanaka}
The class $\mathcal C = \{ Y : \omega_1^Y > \omega_1^{\mathrm{CK}} \}$ is $\Pi^1_1$ and null.
:::

The idea of the proof is as follows. A sequence in $\mathcal C$ computes a sequence of trees whose ranks are computable ordinals, cofinal in $\omega_1^{\mathrm{CK}}$. Fix the functional producing the trees. Up to a small measure $\varepsilon$, the sequences for which the first $n$ trees have computable ranks have these ranks bounded by a single computable ordinal $\alpha_n$. If the ordinals $\alpha_n$ are chosen in a hyperarithmetic way, they are bounded by a single computable ordinal $\beta$, by the boundedness theorem. Up to $\varepsilon$, all the ranks are then below $\beta$, so the sequences for which the ranks are cofinal in $\omega_1^{\mathrm{CK}}$ form a null class. The technique, **selection and boundedness**, is the one that proves that a $\Delta^1_1$ set of numbers is enumerated before a computable stage (:ref{#thm-pi11-stages}): Kreisel's selection theorem (:ref{#cor-total-pi11}) chooses notations in a hyperarithmetic way, and the boundedness theorem bounds them.

:::proof{of=thm-sacks-tanaka}
For an index $e$ and a sequence $Y$, write $L^Y_e$ for the relation whose characteristic function is $\Phi^Y_e$, when $\Phi^Y_e$ is total and $\{0,1\}$-valued.

*$\mathcal C$ is $\Pi^1_1$.* We show that
$$
Y \in \mathcal C \iff \exists e\, \big( L^Y_e \text{ is a well-ordering} \wedge \forall i\, ( i \text{ is an index of a computable linear order} \rightarrow L_i \not\cong L^Y_e ) \big).
$$
If $\omega_1^Y > \omega_1^{\mathrm{CK}}$, some $L^Y_e$ is a well-ordering of type $\omega_1^{\mathrm{CK}}$, and no computable linear order is isomorphic to it. Conversely, if the well-ordering $L^Y_e$ is isomorphic to no computable linear order, its type $\gamma$ is not a computable ordinal, so $\gamma \geq \omega_1^{\mathrm{CK}}$; then $\omega_1^{\mathrm{CK}}$ is the type of $L^Y_e$ or of a proper initial segment of it, which is $Y$-computable, and $\omega_1^Y > \omega_1^{\mathrm{CK}}$. "$L^Y_e$ is a well-ordering" is $\Pi^1_1$, and "$L_i \not\cong L^Y_e$" is the negation of an existential function quantifier in front of an arithmetic condition, hence $\Pi^1_1$. The number quantifiers preserve $\Pi^1_1$.

*The classes involved.* Fix $e$. For each $m$, let $p(e, m)$ be an index, computable from $e$ and $m$, with $\Phi^Y_{p(e, m)}(\sigma) = \Phi^Y_e(\langle m, \sigma \rangle)$, and write $T^Y_{e, m}$ for the tree $T^Y_{p(e, m)}$ when it is defined: the $m$-th tree produced by $e$ from $Y$. For an ordinal $\alpha$ and a number $n$, let
$$
\mathcal B_{n, \alpha} = \bigcap_{m \leq n} \mathcal A^{p(e, m)}_\alpha, \qquad \mathcal B_\alpha = \bigcap_m \mathcal A^{p(e, m)}_\alpha:
$$
the classes of $Y$ for which the first $n + 1$ trees, respectively all the trees, are defined and well-founded of rank less than $\alpha$. Let $\mathcal B$ be the class of $Y$ for which every tree $T^Y_{e, m}$ is defined and well-founded of computable rank, and
$$
\mathcal U = \mathcal B \setminus \bigcup_{\alpha < \omega_1^{\mathrm{CK}}} \mathcal B_\alpha,
$$
the class of $Y$ for which these ranks are computable but not bounded by a computable ordinal. All these classes are Borel, by :ref{#lem-stages-borel}, since the unions and intersections are countable.

*$\mathcal U$ is null.* We may assume $\lambda(\mathcal B) > 0$. Let $r < \lambda(\mathcal B)$ be rational. For $a \in \mathcal O$, the class $\mathcal B_{n, |a|}$ and its complement are defined by the $\Pi^1_1$ relations $\bigwedge_{m \leq n} P_<(p(e, m), a, Y)$ and $\bigvee_{m \leq n} P_\geq(p(e, m), a, Y)$ of :ref{#fact-pi11-stages} (1), in which the bounded quantifier over $m$ is a number quantifier. By :ref{#fact-higher-borel} (1), the relation
$$
R(n, a) \iff a \in \mathcal O \wedge \lambda(\mathcal B_{n, |a|}) > r
$$
is $\Pi^1_1$. Every $n$ has some $a$ with $R(n, a)$. Indeed, the stages increase, so $\mathcal B \subseteq \bigcup_{\alpha < \omega_1^{\mathrm{CK}}} \mathcal B_{n, \alpha}$: the first $n + 1$ ranks of a member of $\mathcal B$ are computable, and so is their maximum. The ordinal $\omega_1^{\mathrm{CK}}$ is a countable limit, the limit of an increasing sequence $(\alpha_k)$ of computable ordinals, and by countable additivity $\lambda(\mathcal B_{n, \alpha_k})$ tends to the measure of the union, which is at least $\lambda(\mathcal B) > r$. So $\lambda(\mathcal B_{n, \alpha_k}) > r$ for some $k$, and any notation $a$ of $\alpha_k$ satisfies $R(n, a)$.

By Kreisel's selection theorem (:ref{#cor-total-pi11}), there is a hyperarithmetic function $f$ with $R(n, f(n))$ for every $n$. Its range $\{ a : \exists n\, f(n) = a \}$ is a $\Delta^1_1$, hence $\Sigma^1_1$, subset of $\mathcal O$, so by boundedness there is $b \in \mathcal O$ with $|f(n)| < |b|$ for every $n$ (:ref{#ex-o-bounded}). Then $\mathcal B_{n, |b|} \supseteq \mathcal B_{n, |f(n)|}$ has measure greater than $r$ for every $n$. The classes $\mathcal B_{n, |b|}$ decrease with $n$, and their intersection is $\mathcal B_{|b|}$, so $\lambda(\mathcal B_{|b|}) \geq r$. Every member of $\mathcal B_{|b|}$ belongs to $\mathcal B$ and not to $\mathcal U$, so $\lambda(\mathcal U) \leq \lambda(\mathcal B) - r$. Since $r$ is any rational below $\lambda(\mathcal B)$, $\lambda(\mathcal U) = 0$.

*$\mathcal C$ is covered.* Write $\mathcal U^e$ for the class $\mathcal U$ built from the index $e$. Let $Y \in \mathcal C$, and let $W$ be a $Y$-computable well-ordering of type $\omega_1^{\mathrm{CK}}$. Its field is infinite and $Y$-c.e.; let $x_0, x_1, \dots$ be a $Y$-computable enumeration of it. The trees $D_{W_{< x_m}}$ of the descending sequences of the initial segments below $x_m$ (:ref{#prop-descending-tree}) are $Y$-computable, uniformly in $m$, so they are the trees $T^Y_{e, m}$ for some $e$. Their ranks $|W_{< x_m}|$ are less than $\omega_1^{\mathrm{CK}}$, hence computable, and they are cofinal in $\omega_1^{\mathrm{CK}}$, since $\omega_1^{\mathrm{CK}}$ is a limit ordinal. So $Y \in \mathcal U^e$. Hence $\mathcal C \subseteq \bigcup_e \mathcal U^e$, a countable union of null classes, and $\mathcal C$ is null.
:::

:::quiz[the Sacks–Tanaka theorem]
In the proof of :ref{#thm-sacks-tanaka}, why does the proof not simply choose, for each $n$, some computable $\alpha_n$ with $\lambda(\mathcal B_{n, \alpha_n}) > r$, and take the supremum of the $\alpha_n$?

- [x] Because the supremum of countably many computable ordinals may be $\omega_1^{\mathrm{CK}}$ itself; only a hyperarithmetic choice of notations gives a $\Sigma^1_1$ set of notations, to which the boundedness theorem applies.
- [ ] Because the ordinals $\alpha_n$ may not exist.

  They exist by countable additivity, as shown in the proof; the issue is to bound them.
- [ ] Because $\lambda(\mathcal B_{n, \alpha})$ is not monotone in $\alpha$.

  It is nondecreasing in $\alpha$, since the stages increase.

---

Where is the hypothesis $r < \lambda(\mathcal B)$ used?

- [x] To show that every $n$ has some $a$ with $R(n, a)$, so that Kreisel's selection theorem applies to a relation that is total in $n$.
- [ ] To show that $R$ is $\Pi^1_1$.

  $R$ is $\Pi^1_1$ for every rational $r$, by the measure fact.
- [ ] To show that $\mathcal B_{|b|} \subseteq \mathcal B$.

  This inclusion holds since $|b|$ is a computable ordinal, whatever $r$.
:::

Combined with Lusin's theorem, the Sacks–Tanaka theorem refines the picture of :ref{#fig-stage-measure}: the members of a $\Pi^1_1$ class that enter at a stage at least $\omega_1^{\mathrm{CK}}$ collapse $\omega_1^{\mathrm{CK}}$ (:ref{#fact-pi11-stages} (2)), so they form a null class, and the measure of the class is the supremum of the measures of its $\Delta^1_1$ stages (exercise).

## Exercises

::::exercise{difficulty=2}
Show that for every $\Pi^1_1$ class $\mathcal A = \mathcal A^p$, $\lambda(\mathcal A) = \sup_{\alpha < \omega_1^{\mathrm{CK}}} \lambda(\mathcal A_\alpha)$. Deduce that the relation $\lambda(\mathcal A^p) > q$ is $\Pi^1_1$ in $p$ and $q$.

:::solution
By :ref{#fact-pi11-stages} (2), $\mathcal A \subseteq \mathcal C \cup \bigcup_{\alpha < \omega_1^{\mathrm{CK}}} \mathcal A_\alpha$, and $\mathcal C$ is null by :ref{#thm-sacks-tanaka}. The stages increase, so by countable additivity along an increasing sequence of computable ordinals cofinal in $\omega_1^{\mathrm{CK}}$, the measure of the union is the supremum of the measures of the stages; and it is at most $\lambda(\mathcal A)$. Hence $\lambda(\mathcal A^p) > q$ if and only if $\exists a\, (a \in \mathcal O \wedge M(p, a, q))$, where $M$ expresses $\lambda(\mathcal A^p_{|a|}) > q$ for $a \in \mathcal O$ (:ref{#fact-higher-borel} (1)). This is $\Pi^1_1$: it is the measure lemma for $\Pi^1_1$ classes, Nies's Measure Lemma 9.1.10, obtained here from its $\Delta^1_1$ case.
:::
::::

## Notes and references

Sacks (1969) and Tanaka (1967) proved that the class of sequences collapsing $\omega_1^{\mathrm{CK}}$ is null. Nies obtains it (Corollary 9.1.15) from Sacks's theorem on hyperarithmetic upper cones (his Theorem 9.1.13, referred to Sacks's book) and Spector's theorem that $\omega_1^Y > \omega_1^{\mathrm{CK}}$ exactly when $\mathcal O \leq_h Y$ (Theorem 9.1.14). The proof given here, by selection and boundedness, follows Monin and Patey (chapter *Higher randomness*), written with trees and the stages of :ref{to="pi11-classes"}. Nies also states the companion basis theorem of Sacks and Tanaka: a $\Pi^1_1$ class of positive measure has a hyperarithmetic member (Theorem 9.1.11).

- G. E. Sacks, *Measure-theoretic uniformity in recursion theory and set theory*, Transactions of the American Mathematical Society 142 (1969), 381–420.
- H. Tanaka, *A basis result for Π¹₁-sets of positive measure*, Commentarii Mathematici Universitatis Sancti Pauli 16 (1967), 115–127.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.1.
