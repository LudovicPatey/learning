---
title: The ramified analytic hierarchy
summary: The structure M(ω₁ᶜᵏ, T) of the sets ramified analytic in T; truth for existential sentences is Π¹₁; the ramified analytic hierarchy is HYP (Kleene); M(ω₁ᶜᵏ, T) satisfies Δ¹₁ comprehension exactly when ω₁ᵀ = ω₁ᶜᵏ (Kreisel).
duration: 40
prerequisites: [sigma11-basis/hyperjump, descriptive-set-theory/uniformization, hyperarithmetic/kleene-theorem]
---

Forcing builds sets with prescribed properties by deciding, step by step, the truth of statements about the set under construction. To force properties of hyperdegrees, such as preserving $\omega_1^{\mathrm{CK}}$ or being of minimal hyperdegree, the statements must speak about the sets hyperarithmetic in the generic set $T$. Kleene's **ramified analytic hierarchy** provides the language. It builds the sets hyperarithmetic in $T$ by stages indexed by the computable ordinals: at each stage, it adds the sets of numbers definable, in the language of second-order arithmetic, over the sets built at earlier stages. A formula whose set variables carry ordinal superscripts, telling at which stage they are bounded, is **ranked**, and its truth is defined by recursion on the ordinals.

This lesson, which follows Sacks (Section III.4), sets up the language and the structure $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, proves that truth for existential sentences is $\Pi^1_1$, and characterizes the sets $T$ for which $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ is exactly the class of sets hyperarithmetic in $T$: those that do not collapse $\omega_1^{\mathrm{CK}}$, or equivalently those for which $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ satisfies the $\Delta^1_1$ comprehension axiom. The next lessons force this axiom to hold.

## The language

The language $\mathcal L(\omega_1^{\mathrm{CK}}, \mathcal T)$ has: number variables $x, y, \dots$; numerals $0, 1, 2, \dots$; a set constant $\mathcal T$; **ranked** set variables $X^\beta, Y^\beta, \dots$ for each $\beta < \omega_1^{\mathrm{CK}}$; **unranked** set variables $X, Y, \dots$; the symbols $+$, $\cdot$, successor, $=$ and $\in$. Atomic formulas are $t = s$ and $t \in U$, with $t, s$ number terms and $U$ the constant $\mathcal T$ or a set variable. A formula is **ranked** if all its set variables are ranked; a ranked formula has **rank at most $\beta$** if its free ranked variables $X^\gamma$ have $\gamma \leq \beta$ and its bound ranked variables have $\gamma < \beta$.

Formulas are coded by numbers. A ranked variable $X^\beta$ is coded with a notation for $\beta$ taken from a fixed $\Pi^1_1$ set $\mathcal O_1 \subseteq \mathcal O$ that contains exactly one notation for each computable ordinal and on which $<_{\mathcal O}$ is linear (admitted; Sacks, Theorem III.2.4). With this coding, the set of codes of formulas is $\Pi^1_1$, and the set of codes of ranked formulas of rank less than $|a|$ is c.e. uniformly in the notation $a \in \mathcal O_1$.

## The structure

Fix $T \subseteq \nat$. By recursion on $\beta < \omega_1^{\mathrm{CK}}$, define a set $\mathcal M(\beta, T)$ of subsets of $\nat$, and truth of ranked sentences of rank at most $\beta$ in the universe $\bigcup_{\alpha < \beta} \mathcal M(\alpha, T)$:

1. A ranked sentence of rank at most $\beta$ is **true** if it holds when $\mathcal T$ is interpreted as $T$, the variables $X^\alpha$ range over $\mathcal M(\alpha, T)$, number variables range over $\nat$, and the symbols have their usual meaning.
2. $\mathcal M(\beta, T)$ consists of the sets $\{ n : \varphi(n) \text{ is true} \}$, for the ranked formulas $\varphi(x)$ of rank at most $\beta$ with $x$ as only free variable.

Let $\mathcal M(\omega_1^{\mathrm{CK}}, T) = \bigcup_{\beta < \omega_1^{\mathrm{CK}}} \mathcal M(\beta, T)$. Truth in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ of an arbitrary sentence is defined by letting the unranked variables range over $\mathcal M(\omega_1^{\mathrm{CK}}, T)$; for ranked sentences, it agrees with the truth just defined. $\mathcal M(0, T)$ is the set of sets arithmetic in $T$, since a formula of rank $0$ has no bound set variables. A sentence is **existential**, or $\Sigma^1_1$, if it is ranked or of the form $(\exists X_1) \cdots (\exists X_k)\, \psi$ with $\psi$ without bound unranked variables.

Inductions on ranked sentences use their **full ordinal rank**: the function $r$ on $\{ -1 \} \cup \omega_1^{\mathrm{CK}}$ such that $r(\beta)$ is the number of quantifiers over variables of rank $\beta$, and $r(-1)$ the number of number quantifiers. Full ranks are compared lexicographically from the top: $r_0 < r_1$ if $r_0(\beta) < r_1(\beta)$ for the largest $\beta$ where they differ. This is a well-ordering, and the substitution of a formula of rank at most $\alpha$ for the variable of $(\exists X^\alpha)\varphi(X^\alpha)$ decreases full rank, since the quantifier over $X^\alpha$ disappears and only quantifiers of rank less than $\alpha$ are added.

## Truth is Π¹₁

:::lemma[Kleene]{#lem-ramified-truth}
The relation "$\varphi$ is an existential sentence true in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$", between the code of $\varphi$ and $T$, is $\Pi^1_1$. For each $a \in \mathcal O_1$, the restriction of truth to ranked sentences of rank less than $|a|$ is $\Delta^1_1$, uniformly in $a$.
:::

:::proof{of=lem-ramified-truth}
It suffices to treat ranked sentences: an existential sentence $(\exists X_1)\cdots(\exists X_k)\psi$ is true if and only if there are notations $a_1, \dots, a_k \in \mathcal O_1$ such that the ranked sentence obtained by giving the variables the ranks $|a_i|$ is true, a number quantifier over a $\Pi^1_1$ set.

The truth set for ranked sentences, the set of pairs $(\varphi, 1)$ for true and $(\varphi, 0)$ for false ranked sentences, is the least set $X$ satisfying a list of closure conditions $A(X, T)$, one for each clause of the definition of truth. For instance:

- if $(\varphi, 1) \in X$ and $(\psi, 1) \in X$, then $(\varphi \wedge \psi, 1) \in X$; if $(\varphi, 0) \in X$ or $(\psi, 0) \in X$, then $(\varphi \wedge \psi, 0) \in X$;
- if $(\varphi, 0) \in X$ then $(\neg\varphi, 1) \in X$, and if $(\varphi, 1) \in X$ then $(\neg\varphi, 0) \in X$;
- if $a \in \mathcal O_1$ and $(\varphi(x_\theta), 1) \in X$ for some ranked $\theta(x)$ of rank at most $|a|$, then $((\exists X^{|a|})\varphi(X^{|a|}), 1) \in X$; if $(\varphi(x_\theta), 0) \in X$ for all such $\theta$, then $((\exists X^{|a|})\varphi, 0) \in X$;
- the analogous conditions for number quantifiers, and the atomic conditions, for instance $(t \in \mathcal T, 1) \in X$ if the value of $t$ is in $T$.

Here $\varphi(x_\theta)$ denotes the result of replacing each atomic formula $t \in X^{|a|}$ by $\theta(t)$. Each condition is $\Sigma^1_1$ in $X$ and $T$: the hypotheses "$a \in \mathcal O_1$" and "$\varphi$ is a code of a ranked sentence" are $\Pi^1_1$ and appear negatively, and the quantification over the formulas $\theta$ of rank at most $|a|$ is a number quantifier over a c.e. set. So $A(X, T)$ is $\Sigma^1_1$. By induction on full ordinal rank and logical complexity, every set $X$ satisfying $A(X, T)$ contains the truth set, and the truth set satisfies $A(X, T)$. Hence
$$
\varphi \text{ is a true ranked sentence} \iff (\forall X)\big(A(X, T) \to (\varphi, 1) \in X\big),
$$
which is $\Pi^1_1$. For sentences of rank less than $|a|$, which form a c.e. set uniformly in $a$, the falsity of $\varphi$ is the truth of $\neg\varphi$, also $\Pi^1_1$; so truth restricted to them is $\Delta^1_1$.
:::

:::quiz[truth in the ramified hierarchy]
In the proof of :ref{#lem-ramified-truth}, why are the closure conditions $\Sigma^1_1$ although "$a \in \mathcal O_1$" is $\Pi^1_1$?

- [x] Because "$a \in \mathcal O_1$" appears as a hypothesis of an implication, hence negatively; the negation of a $\Pi^1_1$ condition is $\Sigma^1_1$.
- [ ] Because $\mathcal O_1$ is computable.

  $\mathcal O_1$ is $\Pi^1_1$ and not hyperarithmetic, since it contains a notation for every computable ordinal.
- [ ] Because the conditions do not mention $T$.

  They mention $T$ in the atomic conditions; this does not affect their complexity.
:::

## The ramified hierarchy is HYP

:::lemma[Kleene]{#lem-h-ranked}
For each $b \in \mathcal O_1$ there is a ranked formula $\eta_b(x)$, in which $\mathcal T$ does not occur, of rank $|b| + 1$, such that $H_b = \{ n : \eta_b(n) \text{ is true in } \mathcal M(\omega_1^{\mathrm{CK}}, T) \}$ for every $T$. More generally, if $\mathcal T$ is allowed in $\eta_b$, the formula $\eta_b^{\mathcal T}(x)$ defines $H^T_b$ in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ for every $T$ with $b \in \mathcal O^T$ and $|b|_T = |b|$.
:::

:::proof{of=lem-h-ranked}
"$Y$ is an H-sequence along $b$" is an arithmetic property of $Y$ (:ref{#def-h-sequence}), and the H-sequence along $b$ is unique. Let $\eta_b(x)$ be $(\exists Y^{|b|})(Y \text{ is an H-sequence along } b \wedge \langle b, x \rangle \in Y)$. By induction along $b$, the H-sequence along $b$ is arithmetic in the H-sequences along the notations below $b$, hence belongs to $\mathcal M(|b|, T)$, and then $\eta_b$ defines $H_b$. The relativized statement is proved in the same way with H-sequences relative to $T$. (Sacks, Lemma III.4.7 and Exercise III.4.21.)
:::

:::theorem[Kleene]{#thm-ramified-hyp}
$\mathcal M(\omega_1^{\mathrm{CK}}, \emptyset) = \mathrm{HYP}$. More generally, $\mathrm{HYP} \subseteq \mathcal M(\omega_1^{\mathrm{CK}}, T) \subseteq \mathrm{HYP}(T)$ for every $T$.
:::

:::proof{of=thm-ramified-hyp}
Every hyperarithmetic set is computable in some $H_b$, $b \in \mathcal O_1$, hence arithmetic in a member of $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ by :ref{#lem-h-ranked}, hence in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$. Conversely, a member $\{ n : \varphi(n) \}$ of $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, with $\varphi$ ranked of rank less than some $|a|$, is $\Delta^1_1$ in $T$ by :ref{#lem-ramified-truth} relativized, hence hyperarithmetic in $T$. For $T = \emptyset$, both bounds are $\mathrm{HYP}$.
:::

## Δ¹₁ comprehension

The **$\Delta^1_1$ comprehension** scheme consists of the sentences
$$
(\forall x)\big((\exists Y) A(x, Y) \leftrightarrow (\forall Z) B(x, Z)\big) \to (\exists X)(\forall x)\big(x \in X \leftrightarrow (\exists Y) A(x, Y)\big),
$$
for arithmetic $A$ and $B$, possibly with set parameters. A family of sets $\mathcal N$ satisfies it if it holds when the set variables range over $\mathcal N$.

:::fact[Kleene; Kreisel]{#fact-hyp-uniform}
1. A relation $P(n, Y)$ between numbers and sets is $\Delta^1_1$ if and only if there are $b \in \mathcal O$ and $e$ such that $P(n, Y) \iff \Phi^{H^Y_b}_e(n) = 1$ for all $n$ and $Y$, with $\Phi^{H^Y_b}_e$ total.
2. Every family of sets that contains $T$, is closed under Turing reducibility and join, and satisfies $\Delta^1_1$ comprehension, contains $\mathrm{HYP}(T)$.
:::

These are admitted: (1) is Kleene's theorem made uniform in a set parameter (Sacks, Section II.5.6), and (2) is Kreisel's theorem that $\mathrm{HYP}(T)$ is the least ω-model of $\Delta^1_1$ comprehension containing $T$ (Sacks, Theorem III.4.10); its proof shows that $H^T_b$ belongs to the family by induction along $b \in \mathcal O^T$, the set being $\Delta^1_1$-definable from the earlier ones.

:::theorem[Kreisel]{#thm-ramified-comprehension}
For every set $T$, the following are equivalent:

1. $\omega_1^T = \omega_1^{\mathrm{CK}}$;
2. $\mathcal M(\omega_1^{\mathrm{CK}}, T) = \mathrm{HYP}(T)$;
3. $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ satisfies $\Delta^1_1$ comprehension.
:::

:::proof{of=thm-ramified-comprehension}
First, every member of $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ is computable in $H^T_b$ for some $b \in \mathcal O$: it is $\{ n : \varphi(n) \}$ for a ranked $\varphi$ of rank less than some $|a|$, the relation "$\varphi(n)$ is true in $\mathcal M(\omega_1^{\mathrm{CK}}, Y)$" is $\Delta^1_1$ in $(n, Y)$ by :ref{#lem-ramified-truth}, and :ref{#fact-hyp-uniform} (1) applies.

(1 ⇒ 2) $\mathcal M(\omega_1^{\mathrm{CK}}, T) \subseteq \mathrm{HYP}(T)$ by :ref{#thm-ramified-hyp}. If $B \leq_h T$, then $B \leq_T H^T_c$ for some $c \in \mathcal O^T$ with $|c|_T < \omega_1^T = \omega_1^{\mathrm{CK}}$; with $b \in \mathcal O_1$ of the same ordinal, $H^T_b \equiv_T H^T_c$, and $H^T_b \in \mathcal M(\omega_1^{\mathrm{CK}}, T)$ by :ref{#lem-h-ranked}. Sets computable in a member are arithmetic in it, hence members.

(2 ⇒ 3) Suppose the hypothesis of an instance of comprehension holds in $\mathrm{HYP}(T)$, with parameters in $\mathrm{HYP}(T)$. The set $\{ x : (\exists Y \in \mathrm{HYP}(T)) A(x, Y) \}$ is $\Pi^1_1(T)$ by :ref{#cor-hyp-quantifier} relativized, and its complement, $\{ x : (\exists Z \in \mathrm{HYP}(T)) \neg B(x, Z) \}$ by the hypothesis, is $\Pi^1_1(T)$ as well. So it is $\Delta^1_1(T)$, a member of $\mathrm{HYP}(T)$.

(3 ⇒ 1) The family $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ contains $T$ and is closed under Turing reducibility and join, since it is closed under arithmetic definability. By :ref{#fact-hyp-uniform} (2), it contains $\mathrm{HYP}(T)$. If $\omega_1^T > \omega_1^{\mathrm{CK}}$, take $c \in \mathcal O^T$ with $|c|_T = \omega_1^{\mathrm{CK}}$; then $H^T_c \in \mathcal M(\omega_1^{\mathrm{CK}}, T)$, so $H^T_c \leq_T H^T_b$ for some $b \in \mathcal O$ by the first paragraph, with $|b| < \omega_1^{\mathrm{CK}} = |c|_T$. But $H^T_{2^b}$ is computable in $H^T_c$ and computes the jump of $H^T_b$, by Spector's uniqueness theorem relativized, which gives $(H^T_b)' \leq_T H^T_b$, a contradiction.
:::

The theorem gives a criterion for preserving $\omega_1^{\mathrm{CK}}$ that can be forced: a generic set $T$ for which the generic extension $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ satisfies $\Delta^1_1$ comprehension does not collapse $\omega_1^{\mathrm{CK}}$, and then $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ consists exactly of the sets hyperarithmetic in $T$, each defined by a ranked formula. Statements about $\mathrm{HYP}(T)$ become statements about $\mathcal M(\omega_1^{\mathrm{CK}}, T)$, which forcing can decide.

:::quiz[Δ¹₁ comprehension]
In the proof of (3 ⇒ 1) in :ref{#thm-ramified-comprehension}, why does $H^T_c$ with $|c|_T = \omega_1^{\mathrm{CK}}$ lead to a contradiction?

- [x] Every member of $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ is computable in some $H^T_b$ with $b \in \mathcal O$, below $\omega_1^{\mathrm{CK}}$; but $H^T_c$ computes the jump of every such $H^T_b$, so it cannot be computable in one of them.
- [ ] Because $H^T_c$ is not hyperarithmetic in $T$.

  It is hyperarithmetic in $T$, since $c \in \mathcal O^T$; the problem is that it climbs above all the levels of the ramified hierarchy.
- [ ] Because $\mathcal O^T$ is not $\Pi^1_1$.

  $\mathcal O^T$ is $\Pi^1_1(T)$; its complexity plays no role here.
:::

::::exercise[Collapsing sets]{#ex-ramified-collapse difficulty=1 objective="Apply Kreisel's characterization to Kleene's O."}
Show that $\mathcal M(\omega_1^{\mathrm{CK}}, \mathcal O)$ does not satisfy $\Delta^1_1$ comprehension, and that it is strictly smaller than $\mathrm{HYP}(\mathcal O)$.

:::solution
$\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ (:ref{#prop-omega1-relative}), so by :ref{#thm-ramified-comprehension}, $\mathcal M(\omega_1^{\mathrm{CK}}, \mathcal O)$ does not satisfy $\Delta^1_1$ comprehension and is not equal to $\mathrm{HYP}(\mathcal O)$; it is included in it by :ref{#thm-ramified-hyp}. Concretely, $H^{\mathcal O}_c$ with $|c|_{\mathcal O} = \omega_1^{\mathrm{CK}}$ is hyperarithmetic in $\mathcal O$ but not in $\mathcal M(\omega_1^{\mathrm{CK}}, \mathcal O)$.
:::
::::

## Notes and references

The ramified analytic hierarchy is due to Kleene (1959), who proved that it equals the hyperarithmetic hierarchy; Kreisel (1962) characterized $\mathrm{HYP}$ as the least ω-model of $\Delta^1_1$ comprehension. Feferman (1965) introduced the language $\mathcal L(\omega_1^{\mathrm{CK}}, \mathcal T)$ to study forcing over the hyperarithmetic hierarchy. The presentation follows Sacks (Section III.4: subsections 4.1–4.4, Lemmas 4.5–4.7, Theorem 4.8, Theorem 4.10, Lemmas 4.15 and 4.16); Chong and Yu (Section 5.1) give a variant with the structure $\mathcal A(\omega_1^{\mathrm{CK}}, x)$.

- S. C. Kleene, *Quantification of number-theoretic functions*, Compositio Mathematica 14 (1959), 23–40.
- G. Kreisel, *The axiom of choice and the class of hyperarithmetic functions*, Indagationes Mathematicae 24 (1962), 307–319.
- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Section III.4.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Section 5.1.

:::::exercises
::::exercise{#ex-ramified-levels difficulty=1 objective="Locate the first levels of the ramified hierarchy."}
Show that $\mathcal M(0, T)$ is the set of sets arithmetic in $T$, and that $\mathcal M(1, T)$ contains the $\omega$-th jump of $T$.

:::solution
A ranked formula of rank at most $0$ has no bound set variables, so it is a formula of first-order arithmetic with the parameter $T$, and the sets it defines are the sets arithmetic in $T$. A formula of rank at most $1$ may quantify over $\mathcal M(0, T)$. The set $T^{(\omega)} = \{ \langle n, x \rangle : x \in T^{(n)} \}$ is defined by "there is $Y^0$ such that $Y^0$ is the sequence of the first $n + 1$ jumps of $T$, coded as columns, and $x$ is in its last column": the finite sequence of jumps is arithmetic in $T$, so it belongs to $\mathcal M(0, T)$, and "$Y$ is the sequence of the first $n + 1$ jumps" is arithmetic in $Y$, $n$ and $T$.
:::
::::
:::::
