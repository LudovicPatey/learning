---
title: Hyperarithmetic sets and constructibility
summary: Codes of ω-models of KP form a Δ¹₁ class; ω₁ᶜᵏ is the second admissible ordinal, so the level ω₁ᶜᵏ of the constructible hierarchy is admissible; the hyperarithmetic sets are exactly the subsets of ℕ in the level ω₁ᶜᵏ of the constructible hierarchy, and exactly the sets that belong to every ω-model of KP.
duration: 25
prerequisites: [constructible-hierarchy, sigma11-basis/kreisel-basis]
---

The hyperarithmetic sets were defined by iterating the Turing jump along the computable ordinals, and characterized as the $\Delta^1_1$ sets by Kleene. This lesson gives a third characterization, by definability in set theory: the hyperarithmetic sets are the subsets of $\nat$ that are constructed before stage $\omega_1^{\mathrm{CK}}$. Along the way, $\omega_1^{\mathrm{CK}}$ turns out to be the second admissible ordinal, after $\omega$, so that $L_{\omega_1^{\mathrm{CK}}}$ is an admissible set: the smallest universe of generalized computation beyond the hereditarily finite sets.

The proofs combine the two sides of the theory. ω-models of KP can be coded by sets of numbers, and the codes form a $\Delta^1_1$ class. The basis theorems of Gandy and Kreisel, applied to this class, produce ω-models that are computationally weak: they do not collapse $\omega_1^{\mathrm{CK}}$, or they do not compute a given non-hyperarithmetic set. Their standard parts are admissible and contain $L_{\omega_1^{\mathrm{CK}}}$, which bounds what this level of $L$ can contain.

## Codes of ω-models

A set $E \subseteq \nat^2$, read as a binary relation on $\nat$, **codes** the structure $(\nat, E)$. It is a **nice code of an ω-model of KP** if $(\nat, E)$ is a model of KP and the elements that $(\nat, E)$ regards as natural numbers are the even numbers, with $2n$ playing the role of $n$: the number $0$ codes $\emptyset$, and $2n + 2$ codes $(2n) \cup \{ 2n \}$ in the model.

:::proposition{#prop-omega-model-codes}
1. The class of nice codes of ω-models of KP is $\Delta^1_1$; in fact it is arithmetic in the $\omega$-th jump of $E$, uniformly.
2. If $E$ is a nice code, every subset of $\nat$ represented in $(\nat, E)$, that is of the form $\{ n : 2n \mathrel E c \}$ for some $c$, is computable in $E$.
3. Every ω-model of KP is isomorphic to a model with a nice code. Nice codes exist.
:::

:::proof{of=prop-omega-model-codes}
1. That $(\nat, E)$ satisfies a given axiom of KP is arithmetic in $E$, uniformly in the axiom; satisfying all of them is computable in $E^{(\omega)}$, uniformly. The conditions on the even numbers are arithmetic in $E$. So the class is computable in the $\omega$-th jump, uniformly in $E$, and is $\Delta^1_1$.
2. $n$ belongs to the represented set if and only if $2n \mathrel E c$.
3. Given an ω-model $(M, E')$, its natural numbers are isomorphic to $\nat$ by hypothesis; enumerate them as $0, 2, 4, \dots$ and the other elements as $1, 3, 5, \dots$ (if there are finitely many others, the model is hereditarily finite, which is impossible since it contains $\omega$). A countable admissible set containing $\omega$ exists: the transitive collapse of a countable elementary substructure of $L_{\omega_1}$, which is admissible (admitted; Chong–Yu, Exercise 3.3.1). Its natural numbers are standard, so it gives a nice code.
:::

## The second admissible ordinal

:::theorem{#thm-ck-second-admissible}
$\omega_1^{\mathrm{CK}}$ is the least admissible ordinal greater than $\omega$. Consequently, $L_{\omega_1^{\mathrm{CK}}}$ is an admissible set.
:::

:::proof{of=thm-ck-second-admissible}
By :ref{#prop-admissible-above-ck}, no admissible ordinal lies strictly between $\omega$ and $\omega_1^{\mathrm{CK}}$. By :ref{#prop-omega-model-codes} and the Gandy basis theorem (:ref{#thm-gandy-basis}), there is a nice code $E$ of an ω-model of KP with $\omega_1^E = \omega_1^{\mathrm{CK}}$. Let $N$ be the transitive collapse of the standard part of $(\nat, E)$; it is admissible (:ref{#lem-standard-kp}), and $o(N) \geq \omega_1^{\mathrm{CK}}$ by :ref{#cor-omega-model-contains-l}. Conversely, let $\beta \in N$ be an ordinal, represented by some $b \in \nat$. The elements of the model below $b$ are ordered by $E$ with type $\beta$, and this order is computable in $E$; so $\beta < \omega_1^E = \omega_1^{\mathrm{CK}}$. Hence $o(N) = \omega_1^{\mathrm{CK}}$, which is admissible. By :ref{#thm-l-admissible}, $L_{\omega_1^{\mathrm{CK}}}$ is admissible.
:::

:::quiz[the second admissible ordinal]
In the proof of :ref{#thm-ck-second-admissible}, why is the Gandy basis theorem needed?

- [x] To bound the ordinals of the standard part: they are types of $E$-computable well-orderings, so they are below $\omega_1^E$, which the Gandy basis theorem makes equal to $\omega_1^{\mathrm{CK}}$.
- [ ] To show that the standard part is admissible.

  This holds for every model of KP (:ref{#lem-standard-kp}).
- [ ] To show that nice codes exist.

  Existence comes from a countable admissible set; the basis theorem selects a weak code among them.
:::

## The hyperarithmetic sets are the constructible sets of level ω₁ᶜᵏ

:::theorem{#thm-hyp-l}
A set $X \subseteq \nat$ is hyperarithmetic if and only if $X \in L_{\omega_1^{\mathrm{CK}}}$.
:::

:::proof{of=thm-hyp-l}
*Hyperarithmetic sets are in $L_{\omega_1^{\mathrm{CK}}}$.* Write $A = L_{\omega_1^{\mathrm{CK}}}$, which is admissible. Let $T$ be a computable tree on $\nat$; it belongs to $L_{\omega+1} \subseteq A$. We claim that $T$ is well-founded if and only if $A \models (\exists g)(g$ is a function from $T$ to the ordinals with $g(\tau) < g(\sigma)$ whenever $\sigma \prec \tau)$. If such a $g$ exists, an infinite path would give a descending sequence of ordinals, so $T$ is well-founded. Conversely, if $T$ is well-founded, the relation "$\tau$ properly extends $\sigma$" on $T$ is well-founded and belongs to $A$; by :ref{#prop-wf-recursion}, the rank function $g(\sigma) = \sup \{ g(\tau) + 1 : \tau \text{ a child of } \sigma \}$ is $\Sigma$ over $A$, and by :ref{#ex-sigma-image} its restriction to $T$ is a set of $A$, since its values are ordinals of $A$, the ranks of computable well-founded trees being computable ordinals (:ref{#prop-rank-computable}).

Now let $X$ be hyperarithmetic. By Kleene's theorem, $X$ and its complement are $\Pi^1_1$, so by the normal form theorem there are computable sequences of trees $(T_n)$ and $(T'_n)$, elements of $A$, with $n \in X$ if and only if $T_n$ is well-founded, and $n \notin X$ if and only if $T'_n$ is well-founded. By the claim, $X$ is defined over $A$ by a $\Sigma$ formula, and its complement in $\nat$ by another; on $\nat$, the first is equivalent to the negation of the second, a $\Pi$ formula. By $\Delta$-separation (:ref{#cor-sigma-collection}), $X = \{ n \in \omega : \ldots \}$ is an element of $A$.

*Sets in $L_{\omega_1^{\mathrm{CK}}}$ are hyperarithmetic.* Let $X \in L_{\omega_1^{\mathrm{CK}}}$ be a subset of $\nat$, and suppose that $X$ is not hyperarithmetic. The class of nice codes of ω-models of KP is a non-empty $\Delta^1_1$ class (:ref{#prop-omega-model-codes}). By Kreisel's basis theorem (:ref{#thm-kreisel-basis}), it has a member $E$ with $X \not\leq_h E$. By :ref{#cor-omega-model-contains-l}, $X$ is represented in $(\nat, E)$, so $X \leq_T E$ by :ref{#prop-omega-model-codes} (2), a contradiction.
:::

:::corollary[Kreisel]{#cor-hyp-omega-models}
A set $X \subseteq \nat$ is hyperarithmetic if and only if it is represented in every ω-model of KP.
:::

:::proof{of=cor-hyp-omega-models}
If $X$ is hyperarithmetic, then $X \in L_{\omega_1^{\mathrm{CK}}}$ by :ref{#thm-hyp-l}, and $X$ is represented in every ω-model of KP by :ref{#cor-omega-model-contains-l}. If $X$ is not hyperarithmetic, Kreisel's basis theorem gives a nice code $E$ with $X \not\leq_h E$, so $X$ is not represented in $(\nat, E)$.
:::

So the hyperarithmetic sets are the sets of numbers that every ω-model of KP must contain, as the computable sets are, in a sense, the sets that every model of the arithmetic of finite sets must contain. Kreisel proved the corresponding statement for ω-models of $\Delta^1_1$ comprehension, an axiom of second-order arithmetic, which the course on forcing over the hyperarithmetic sets uses.

::::exercise[Notations and constructibility]{#ex-wf-sigma1 difficulty=1 objective="Recognize well-foundedness of computable trees as a Σ₁ property over $L_{\omega_1^{\mathrm{CK}}}$."}
Show that the set $\mathcal O$ of notations is $\Sigma_1$-definable over $L_{\omega_1^{\mathrm{CK}}}$, without parameters other than numbers.

:::solution
By the normal form theorem, there is a computable sequence of trees $(T_n)$ with $n \in \mathcal O$ if and only if $T_n$ is well-founded; the sequence is computable, so it is $\Delta_1$-definable over $L_\omega$ and belongs to $L_{\omega+1}$, and it is $\Sigma_1$-definable over $L_{\omega_1^{\mathrm{CK}}}$ without parameters, as the unique set satisfying a $\Delta_0$ property over $L_\omega$ (in fact over $\mathrm{HF}$, by :ref{#thm-hf-ce}). By the claim in the proof of :ref{#thm-hyp-l}, $n \in \mathcal O$ if and only if $L_{\omega_1^{\mathrm{CK}}} \models (\exists g)(g$ is an order-reversing map from $T_n$ to the ordinals$)$, a $\Sigma_1$ formula. (Chong–Yu, Exercise 3.7.1.)
:::
::::

## Notes and references

That $\omega_1^{\mathrm{CK}}$ is the second admissible ordinal, and that the hyperarithmetic sets are the subsets of $\nat$ in $L_{\omega_1^{\mathrm{CK}}}$, go back to Kripke and Platek; Kreisel characterized the hyperarithmetic sets by ω-models. The proofs follow Chong and Yu (Propositions 3.6.3 and 3.6.5, Lemma 3.6.6, Corollary 3.6.7, Theorem 3.6.8, Corollary 3.6.9), with a direct proof of the inclusion of $\mathrm{HYP}$ in $L_{\omega_1^{\mathrm{CK}}}$ by $\Delta$-separation instead of their use of $\Pi^0_1$ singletons; Sacks (Theorem III.4.10) proves Kreisel's characterization by ω-models of $\Delta^1_1$ comprehension.

- G. Kreisel, *The axiom of choice and the class of hyperarithmetic functions*, Indagationes Mathematicae 24 (1962), 307–319.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Section 3.6.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Section III.4.
- J. Barwise, *Admissible Sets and Structures*, Springer, 1975.

:::::exercises
::::exercise{#ex-hyp-delta1-l difficulty=2 objective="Show that hyperarithmetic sets are Δ₁-definable over $L_{\omega_1^{\mathrm{CK}}}$ and that the converse also holds."}
Show that a set $X \subseteq \nat$ is hyperarithmetic if and only if both $X$ and its complement are $\Sigma_1$-definable over $L_{\omega_1^{\mathrm{CK}}}$, with parameters.

:::solution
If $X$ is hyperarithmetic, then $X \in L_{\omega_1^{\mathrm{CK}}}$ by :ref{#thm-hyp-l}, so $X$ and its complement are $\Delta_0$-definable with the parameter $X$. Conversely, if both are $\Sigma_1$-definable over the admissible set $L_{\omega_1^{\mathrm{CK}}}$, then $\Delta$-separation (:ref{#cor-sigma-collection}) gives $X \in L_{\omega_1^{\mathrm{CK}}}$, and $X$ is hyperarithmetic by :ref{#thm-hyp-l}.
:::
::::
:::::
