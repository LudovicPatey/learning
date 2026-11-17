---
title: The Spector–Gandy theorem
summary: A set of numbers is Π¹₁ if and only if it is Σ₁-definable over the level ω₁ᶜᵏ of the constructible hierarchy (Spector, Gandy); Π¹₁ sets are the c.e. sets of the level ω₁ᶜᵏ of the constructible hierarchy; relativization, ω₁ˣ is admissible for every x, and Sacks's theorem that every countable admissible ordinal greater than ω is of this form.
duration: 20
prerequisites: [hyp-in-l, descriptive-set-theory/uniformization]
---

Over the hereditarily finite sets, the $\Sigma_1$ relations on numbers are the c.e. relations (:ref{#thm-hf-ce}). One level up, over $L_{\omega_1^{\mathrm{CK}}}$, the $\Sigma_1$ relations on numbers are the $\Pi^1_1$ relations: this is the theorem of Spector and Gandy, which makes precise the analogy between $\Pi^1_1$ and c.e. that runs through higher computability. A $\Pi^1_1$ set is enumerated along the ordinals of $L_{\omega_1^{\mathrm{CK}}}$, an element entering at the first level of $L$ that contains a witness, and the hyperarithmetic sets, which are the elements of $L_{\omega_1^{\mathrm{CK}}}$, play the role of the finite sets.

The theorem relativizes, and its relativization shows that $\omega_1^x$ is an admissible ordinal for every $x$. Sacks proved the converse, which closes the circle between the ordinals of computability and the ordinals of set theory: every countable admissible ordinal greater than $\omega$ is $\omega_1^x$ for some $x$.

## The theorem

:::theorem[Spector, Gandy]{#thm-spector-gandy}
A set $X \subseteq \nat$ is $\Pi^1_1$ if and only if there is a $\Sigma_1$ formula $\varphi(u)$ such that $n \in X$ if and only if $L_{\omega_1^{\mathrm{CK}}} \models \varphi(n)$.
:::

:::proof{of=thm-spector-gandy}
*From $\Pi^1_1$ to $\Sigma_1$.* By the normal form theorem, there is a computable sequence of trees $(T_n)$ with $n \in X$ if and only if $T_n$ is well-founded. By the claim in the proof of :ref{#thm-hyp-l}, $T_n$ is well-founded if and only if $L_{\omega_1^{\mathrm{CK}}}$ satisfies "there is an order-reversing map from $T_n$ to the ordinals", a $\Sigma_1$ formula in which the sequence $(T_n)$, an element of $L_{\omega+1}$ definable without parameters, can be replaced by its definition.

*From $\Sigma_1$ to $\Pi^1_1$.* Let $\varphi$ be $\Sigma_1$. We claim that $L_{\omega_1^{\mathrm{CK}}} \models \varphi(n)$ if and only if every ω-model of KP satisfies $\varphi(n)$, where $n$ denotes the natural number $n$ of the model. If $L_{\omega_1^{\mathrm{CK}}} \models \varphi(n)$ and $(M, E)$ is an ω-model of KP, the transitive collapse $N$ of the standard part of $M$ contains $L_{\omega_1^{\mathrm{CK}}}$ (:ref{#cor-omega-model-contains-l}), so $N \models \varphi(n)$ by upward absoluteness of $\Sigma_1$ formulas between transitive sets; the witness lies in the standard part, which is $E$-closed, so the $\Delta_0$ matrix holds in $M$ too, and $M \models \varphi(n)$. Conversely, $L_{\omega_1^{\mathrm{CK}}}$ is a countable admissible set (:ref{#thm-ck-second-admissible}), hence an ω-model of KP, so if every ω-model of KP satisfies $\varphi(n)$, so does $L_{\omega_1^{\mathrm{CK}}}$.

By :ref{#prop-omega-model-codes}, every ω-model of KP is isomorphic to one with a nice code, and the nice codes form a $\Delta^1_1$ class. So
$$
n \in X \iff (\forall E)\big(E \text{ is a nice code of an } \omega\text{-model of KP} \to (\nat, E) \models \varphi(2n)\big).
$$
Satisfaction of a fixed formula in $(\nat, E)$ is arithmetic in $E$, so the right-hand side is $\Pi^1_1$.
:::

:::quiz[the Spector–Gandy theorem]
In the second part of the proof of :ref{#thm-spector-gandy}, why is it necessary that $\varphi$ be $\Sigma_1$?

- [x] Because $\Sigma_1$ formulas are upward absolute: a witness in $L_{\omega_1^{\mathrm{CK}}}$, which is included in the well-founded part of every ω-model, remains a witness in the whole model. A universal formula true in $L_{\omega_1^{\mathrm{CK}}}$ could fail in a larger model.
- [ ] To make the class of codes $\Delta^1_1$.

  The class of codes does not depend on $\varphi$.
- [ ] To make satisfaction arithmetic in $E$.

  Satisfaction of any fixed formula is arithmetic in $E$.
:::

:::corollary{#cor-pi11-stages-l}
Let $X$ be $\Pi^1_1$, defined by the $\Sigma_1$ formula $(\exists v)\psi(u, v)$ with $\psi$ in $\Delta_0$, and let $X_\beta = \{ n : (\exists v \in L_\beta)\psi(n, v) \}$ for $\beta < \omega_1^{\mathrm{CK}}$. Then each $X_\beta$ is hyperarithmetic, $X_\beta \subseteq X_\gamma$ for $\beta \leq \gamma$, and $X = \bigcup_{\beta < \omega_1^{\mathrm{CK}}} X_\beta$. Moreover $X$ is hyperarithmetic if and only if $X = X_\beta$ for some $\beta < \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=cor-pi11-stages-l}
$X_\beta$ is definable over $L_\beta$, hence in $L_{\beta+1} \subseteq L_{\omega_1^{\mathrm{CK}}}$, and hyperarithmetic by :ref{#thm-hyp-l}. Monotonicity and the union are clear, since $\Delta_0$ formulas are absolute. If $X$ is hyperarithmetic, then $X \in L_{\omega_1^{\mathrm{CK}}}$, and every $n \in X$ has a witness in some $L_\beta$; the map $n \mapsto$ (least such $\beta$), restricted to $X$, is $\Sigma$-definable over the admissible set $L_{\omega_1^{\mathrm{CK}}}$, so its range is a set of ordinals of $L_{\omega_1^{\mathrm{CK}}}$ (:ref{#ex-sigma-image}), bounded by some $\beta < \omega_1^{\mathrm{CK}}$, and $X = X_\beta$. The converse is the first statement.
:::

This is the set-theoretic form of :ref{#thm-pi11-stages}: a $\Pi^1_1$ set is enumerated in $\omega_1^{\mathrm{CK}}$ stages, each stage hyperarithmetic, as a c.e. set is enumerated in $\omega$ stages, each finite.

## Relativization and admissible ordinals

For a set $x \subseteq \nat$, the constructible hierarchy relative to $x$ is defined as $L_\beta$, but with $x$ available as a predicate in the definitions: $L_0[x] = \emptyset$, $L_{\beta+1}[x] = \mathrm{Def}_x(L_\beta[x])$, the subsets of $L_\beta[x]$ definable over $(L_\beta[x], \in, x \cap L_\beta[x])$, and unions at limits. The results of this course relativize: KP is extended by allowing the predicate $x$ in $\Delta_0$ formulas, and the proofs are unchanged (Chong–Yu, Corollary 3.7.2 and the exercises of Section 3.6).

:::theorem{#thm-omega1x-admissible}
For every $x \subseteq \nat$:

1. $\omega_1^x$ is the least ordinal $\alpha > \omega$ such that $L_\alpha[x]$ is admissible; in particular $\omega_1^x$ is admissible;
2. the subsets of $\nat$ in $L_{\omega_1^x}[x]$ are the sets hyperarithmetic in $x$;
3. a set of numbers is $\Pi^1_1(x)$ if and only if it is $\Sigma_1$-definable over $L_{\omega_1^x}[x]$.
:::

:::proof{of=thm-omega1x-admissible}
Relativize :ref{#thm-ck-second-admissible}, :ref{#thm-hyp-l} and :ref{#thm-spector-gandy} to $x$: the computable ordinals become the $x$-computable ordinals, the Gandy and Kreisel basis theorems are applied relative to $x$, and the ω-models of KP become the ω-models of KP with the predicate $x$, which contain $L_{\omega_1^x}[x]$. An ordinal $\alpha$ with $L_\alpha[x]$ admissible is admissible, since $L_\alpha[x]$ is in particular a model of KP in the language of set theory.
:::

So $\omega_1^x$ is always admissible. The converse is a deep theorem of Sacks, which we admit.

:::theorem[Sacks]{#thm-sacks-admissible}
Every countable admissible ordinal $\alpha > \omega$ is $\omega_1^x$ for some $x \subseteq \nat$.
:::

Sacks's proof uses forcing with perfect sets over $L_\alpha$, and gives $x$ of minimal hyperdegree among the sets with $\omega_1^x = \alpha$. Chong and Yu (Section 5.4) prove the weaker statement with a notion of forcing due to Steel: the conditions are finite trees $p$ on $\nat$ labeled by ordinals below $\alpha$, the labels decreasing along branches; a generic tree $T$ is well-founded below the nodes labeled by ordinals, with ranks at least the labels, so $\omega_1^T \geq \alpha$; and the main difficulty, the proof that the generic does not compute a well-ordering of type $\alpha$, uses **retagging**, the replacement of large labels by others without changing what is forced. Friedman and Jensen gave another proof with Barwise's compactness theorem for admissible sets.

:::quiz[admissible ordinals]
Why does :ref{#thm-omega1x-admissible} give an admissible ordinal for every $x$, while :ref{#thm-sacks-admissible} needs a separate proof?

- [x] The first says that the ordinal $\omega_1^x$ attached to a given $x$ is admissible; the second asks, for a given admissible ordinal, for an $x$ that produces it, which requires building $x$, here by forcing.
- [ ] Because the admissible ordinals are not countable.

  The theorem concerns countable admissible ordinals; there are uncountably many countable ordinals but only countably many below each one.
- [ ] Because $\omega_1^x$ may be equal to $\omega$.

  $\omega_1^x$ is always greater than $\omega$, since $\omega$ is computable.
:::

::::exercise[Hyperarithmetic reducibility and constructibility]{#ex-hyp-reducible-l difficulty=2 objective="Use the relativized characterization to express hyperarithmetic reducibility and Spector's collapse theorem in set-theoretic terms."}
Show that $y \leq_h x$ if and only if $y \in L_{\omega_1^x}[x]$. Deduce that $\mathcal O \leq_h x$ if and only if $\omega_1^x > \omega_1^{\mathrm{CK}}$, using :ref{#ex-wf-sigma1}.

:::solution
The first statement is :ref{#thm-omega1x-admissible} (2). For the second: if $\omega_1^x > \omega_1^{\mathrm{CK}}$, then $L_{\omega_1^{\mathrm{CK}}} \in L_{\omega_1^{\mathrm{CK}}+1} \subseteq L_{\omega_1^x}[x]$, and $\mathcal O$, which is $\Sigma_1$-definable over $L_{\omega_1^{\mathrm{CK}}}$ by :ref{#ex-wf-sigma1}, is definable over the set $L_{\omega_1^{\mathrm{CK}}}$, hence belongs to $L_{\omega_1^{\mathrm{CK}}+1} \subseteq L_{\omega_1^x}[x]$; so $\mathcal O \leq_h x$. Conversely, if $\mathcal O \leq_h x$, then $\omega_1^x \geq \omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ by :ref{#cor-h-omega1} and :ref{#prop-omega1-relative}. This is Spector's theorem (:ref{#thm-spector-collapse}), obtained here through constructibility. (Chong–Yu, Exercise 3.7.1.)
:::
::::

## Notes and references

The theorem of Spector (1959) and Gandy (1960), in the form "a set is $\Pi^1_1$ if and only if it is $\Sigma_1$ over $L_{\omega_1^{\mathrm{CK}}}$", follows Chong and Yu (Theorem 3.7.1); they also prove a second form, "$X$ is $\Pi^1_1$ if and only if $n \in X \iff (\exists z \in \mathrm{HYP})\, B(n, z)$ for an arithmetic $B$" (Theorem 3.7.3), which we do not use. Sacks's theorem on countable admissible ordinals is from his 1976 paper; Sacks presents the perfect set forcing proof in *Higher Recursion Theory* and Chong and Yu the proof with Steel forcing (Theorem 5.4.12 and Remark 5.4.13).

- C. Spector, *Hyperarithmetical quantifiers*, Fundamenta Mathematicae 48 (1959), 313–320.
- R. O. Gandy, *Proof of Mostowski's conjecture*, Bulletin de l'Académie Polonaise des Sciences 8 (1960), 571–575.
- G. E. Sacks, *Countable admissible ordinals and hyperdegrees*, Advances in Mathematics 19 (1976), 213–262.
- J. Steel, *Forcing with tagged trees*, Annals of Mathematical Logic 15 (1978), 55–74.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Sections 3.7 and 5.4.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.

:::::exercises
::::exercise{#ex-pi11-c-e-l difficulty=1 objective="See the Π¹₁ sets as the c.e. sets of $L_{\omega_1^{\mathrm{CK}}}$ on an example."}
Describe the stages $X_\beta$ of :ref{#cor-pi11-stages-l} for $X = \mathcal O$ with the formula of :ref{#ex-wf-sigma1}, and show that $X_\beta \neq \mathcal O$ for every $\beta < \omega_1^{\mathrm{CK}}$.

:::solution
With the formula "there is an order-reversing map from $T_n$ to the ordinals", $X_\beta$ is the set of $n$ such that $L_\beta$ contains such a map; this requires $T_n$ to be well-founded, and holds once $\beta$ is large enough to contain a map into its ordinals, so roughly the notations whose trees have rank below $\beta$. If $X_\beta = \mathcal O$ for some $\beta < \omega_1^{\mathrm{CK}}$, then $\mathcal O$ would be hyperarithmetic by :ref{#cor-pi11-stages-l}, which it is not, since it is not $\Sigma^1_1$. So the stages never stabilize below $\omega_1^{\mathrm{CK}}$.
:::
::::
:::::
