---
title: The constructible hierarchy and ω-models
summary: Gödel's constructible hierarchy L_α; an ordinal is admissible exactly when L_α is admissible; every admissible ordinal above ω is at least ω₁ᶜᵏ; recursion along well-founded relations in an admissible set; ω-models of KP and their standard parts.
duration: 30
prerequisites: [kripke-platek, computable-ordinals/kleene-o]
---

The admissible sets of interest for higher computability are built by Gödel's **constructible hierarchy**: start from the empty set, and at each step add the subsets of the current level that are definable over it, taking unions at limits. The levels $L_\alpha$ form a hierarchy of definability indexed by ordinals, as the H-sets form a hierarchy of computability indexed by notations. This lesson proves two facts that connect the two: $L_\alpha$ is admissible exactly when $\alpha$ is, and no ordinal strictly between $\omega$ and $\omega_1^{\mathrm{CK}}$ is admissible. It also studies **ω-models** of KP, possibly non-standard models whose natural numbers are the true ones; their well-founded part is admissible, which is the tool of the next lesson.

## The constructible hierarchy

For a set $X$, let $\mathrm{Def}(X)$ be the set of subsets of $X$ of the form $\{ y \in X : (X, \in) \models \varphi(y, \vec a) \}$, for a formula $\varphi$ and parameters $\vec a \in X$.

:::definition[Gödel]{#def-constructible}
The **constructible hierarchy** is defined by recursion on ordinals: $L_0 = \emptyset$, $L_{\beta+1} = \mathrm{Def}(L_\beta)$, and $L_\lambda = \bigcup_{\beta < \lambda} L_\beta$ for limit $\lambda$. The **constructible universe** is $L = \bigcup_\beta L_\beta$.
:::

Each $L_\beta$ is transitive, $L_\beta \subseteq L_\gamma$ for $\beta \leq \gamma$, and $L_\beta \cap \mathrm{Ord} = \beta$. The finite levels are the sets $V_n$, so $L_\omega = \mathrm{HF}$. The next level $L_{\omega+1}$ contains the subsets of $\nat$ definable over $\mathrm{HF}$, in particular every c.e. set and every computable set, by :ref{#thm-hf-ce}. The subsets of $\nat$ in $L$ are studied in Chong and Yu (Section 3.3); here only the levels below $\omega_1^{\mathrm{CK}}$ and a little beyond matter.

The construction can be carried out inside every admissible set, and gives the true levels. This is the basic fact of the theory, and we admit it.

:::fact[Gödel; Barwise]{#fact-l-absolute}
There is a $\Sigma_1$ formula $\Lambda(\beta, x)$ such that for every admissible set $A$ and every ordinal $\beta \in A$, $A \models \Lambda(\beta, x)$ if and only if $x = L_\beta$. In particular $L_\beta \in A$ for every $\beta < o(A)$.
:::

The formula expresses "there is a sequence $(L_\gamma)_{\gamma \leq \beta}$ built by the recursive clauses", where the satisfaction relation of a set is defined by $\Sigma$-recursion; the details are a long formalization (Chong–Yu, Theorem 3.3.2 and Proposition 3.3.3, with a reference to Devlin's *Constructibility*). Since $L_\beta$ is the unique solution, the formula is also equivalent over $A$ to a $\Pi_1$ formula, "every solution equals $x$", so the relation $x = L_\beta$ is $\Delta_1$ over $A$.

:::theorem{#thm-l-admissible}
An ordinal $\alpha$ is admissible if and only if $L_\alpha$ is admissible.
:::

:::proof{of=thm-l-admissible}
If $L_\alpha$ is admissible, then $\alpha = o(L_\alpha)$ is admissible. Conversely, let $\alpha = o(A)$ with $A$ admissible. By :ref{#fact-l-absolute}, $L_\beta \in A$ for every $\beta < \alpha$, so $L_\alpha \subseteq A$. If $\alpha = \omega$, then $L_\alpha = \mathrm{HF}$ is admissible (:ref{#ex-hf-smallest}). Otherwise $\alpha$ is a limit ordinal greater than $\omega$, since $A$ is closed under $\beta \mapsto \beta \cup \{ \beta \}$. Extensionality and foundation hold in the transitive set $L_\alpha$; pair, union and $\Delta_0$-separation hold because a set definable over $L_\beta$ with parameters belongs to $L_{\beta+1}$. We check $\Delta_0$-collection. Suppose $L_\alpha \models (\forall x \in a)(\exists y)\varphi(x, y)$ with $\varphi$ in $\Delta_0$ and $a \in L_\alpha$. By absoluteness, for each $x \in a$ there is $\beta < \alpha$ with $(\exists y \in L_\beta)\varphi(x, y)$. In $A$, the formula $(\exists \beta)(\exists \ell)(\Lambda(\beta, \ell) \wedge (\exists y \in \ell)\varphi(x, y))$ is $\Sigma$, so $\Sigma$-collection in $A$ gives $\alpha_0 < \alpha$, which may be taken with $a \in L_{\alpha_0}$, such that every $x \in a$ has a witness $y \in L_{\alpha_0}$. Then the set $\{ y \in L_{\alpha_0} : (\exists x \in a)\varphi(x, y) \}$ is definable over $L_{\alpha_0}$, hence in $L_{\alpha_0 + 1} \subseteq L_\alpha$, and collects witnesses for all $x \in a$.
:::

:::proposition{#prop-admissible-above-ck}
If $\alpha > \omega$ is admissible, then $\alpha \geq \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=prop-admissible-above-ck}
Suppose that $\omega < \alpha < \omega_1^{\mathrm{CK}}$ is admissible. By :ref{#thm-l-admissible}, $L_\alpha$ is admissible. Since $\alpha$ is a computable ordinal, there is a computable well-ordering $W$ of a subset of $\nat$ of type $\alpha$ (:ref{#def-computable-ordinal}). It belongs to $L_{\omega+1} \subseteq L_\alpha$, being computable. By $\Sigma$-recursion along $W$ (:ref{#prop-wf-recursion} below), the map sending each element of the field of $W$ to the type of its initial segment is a $\Sigma$ function on the field of $W$, whose values are ordinals of $L_\alpha$; by :ref{#ex-sigma-image}, its range is a set of $L_\alpha$. Its range is the ordinal $\alpha$, so $\alpha \in L_\alpha$, a contradiction.
:::

The proof used recursion along a well-ordering that is an element of the admissible set, not along $\in$. This is always possible.

:::proposition{#prop-wf-recursion}
Let $A$ be an admissible set, $R \in A$ a well-founded relation, and $G$ a function $\Sigma$-definable over $A$. There is a function $F$, $\Sigma$-definable over $A$, defined on the field of $R$, with $F(y) = G(y, \{ (z, F(z)) : z \mathrel R y \})$ for every $y$ in the field.
:::

:::proof{of=prop-wf-recursion}
Repeat the proof of :ref{#thm-sigma-recursion}, with attempts defined on subsets of the field of $R$ closed downward under $R$, and with minimal elements taken for $R$ instead of $\in$. The minimal elements exist because $R$ is well-founded in the universe, and the sets of the proof are subsets of the field of $R$; the rest of the proof takes place in $A$, with $\Sigma$-collection and $\Delta$-separation, the sets $\{ z : z \mathrel R y \}$ belonging to $A$ by $\Delta_0$-separation.
:::

:::quiz[the constructible hierarchy]
In the proof of :ref{#prop-admissible-above-ck}, where is it used that $\alpha$ is a computable ordinal?

- [x] To have a well-ordering of type $\alpha$ that is computable, hence an element of $L_{\omega+1} \subseteq L_\alpha$; recursion along it inside $L_\alpha$ then produces $\alpha$ as a set of $L_\alpha$.
- [ ] To show that $L_\alpha$ is admissible.

  This is :ref{#thm-l-admissible}, valid for every admissible ordinal.
- [ ] Because admissible ordinals are limit ordinals.

  Being a limit ordinal does not lead to a contradiction; the computable presentation does.
:::

## ω-models of KP

KP can also be studied in models that are not transitive, given by a binary relation $E$ on a set $M$ that interprets $\in$. Such a model is an **ω-model** if its natural numbers are standard: the elements that the model regards as natural numbers are, under $E$, isomorphic to $\nat$.

:::definition{#def-standard-part}
Let $(M, E)$ be a model of KP. A subset $M_1 \subseteq M$ is **$E$-closed** if $y \mathrel E x$ and $x \in M_1$ imply $y \in M_1$. The **standard part** of $M$ is the largest $E$-closed subset of $M$ on which $E$ is well-founded.
:::

The union of all $E$-closed well-founded subsets is $E$-closed and well-founded, so the standard part exists. By Mostowski's collapsing lemma, $(M_1, E)$ is isomorphic to a transitive set; we identify it with this set when convenient.

:::lemma{#lem-standard-rank}
Let $(M, E)$ be a model of KP. An element $x$ belongs to the standard part of $M$ if and only if its rank, computed in $M$, does.
:::

:::proof{of=lem-standard-rank}
The rank function is $\Sigma$-definable in KP (:ref{#thm-sigma-recursion}), so $M$ computes $\mathrm{rk}(x)$ for every $x$. If $x$ is in the standard part, an induction along the well-founded relation $E$ on the standard part shows that $\mathrm{rk}(x)$ is too. If $x$ is not, there is a descending sequence $x_0 \mathrel E x$, $x_{n+1} \mathrel E x_n$ in $M$, and then $\mathrm{rk}(x_{n+1}) \mathrel E \mathrm{rk}(x_n)$ and $\mathrm{rk}(x_0) \mathrel E \mathrm{rk}(x)$, by the defining property of the rank in $M$; so $\mathrm{rk}(x)$ is not in the standard part.
:::

:::lemma{#lem-standard-kp}
The standard part of a model of KP is a model of KP. So its transitive collapse is an admissible set.
:::

:::proof{of=lem-standard-kp}
Let $M_1$ be the standard part of $(M, E) \models \mathrm{KP}$. Since $M_1$ is $E$-closed, $\Delta_0$ formulas with parameters in $M_1$ have the same truth value in $M_1$ and in $M$. Extensionality, pair, union and $\Delta_0$-separation pass from $M$ to $M_1$: the sets they provide in $M$ have their $E$-elements in $M_1$, hence a well-founded $E$-closure, hence belong to $M_1$. Foundation holds since $E$ is well-founded on $M_1$.

For $\Delta_0$-collection, suppose $M_1 \models (\forall x \mathrel E a)(\exists y)\varphi(x, y)$, with $\varphi$ in $\Delta_0$ and parameters in $M_1$. Then the same holds in $M$, with witnesses in $M_1$. Let $\alpha_0$ be the least ordinal of $M$ such that some $b$ of rank $\alpha_0$ in $M$ collects witnesses; it exists by collection in $M$ and foundation in $M$. If $\alpha_0$ is standard, then $b$ is in $M_1$ by :ref{#lem-standard-rank}. Otherwise, there is a non-standard ordinal $\alpha_1 \mathrel E \alpha_0$ of $M$: if every ordinal $E$-below $\alpha_0$ were standard, the $E$-closure of $\{ \alpha_0 \}$ would be well-founded, and $\alpha_0$ would be standard. The ordinals of $M$ are linearly ordered by $E$, as KP proves, and the standard ones form an initial segment, so all the witnesses in $M_1$ have ranks $E$-below $\alpha_1$. So $M \models (\forall x \mathrel E a)(\exists y)(\varphi(x, y) \wedge \mathrm{rk}(y) \mathrel E \alpha_1)$, a $\Sigma$ statement; by $\Sigma$-collection in $M$ and $\Delta_0$-separation, there is $c$ in $M$ collecting witnesses of rank below $\alpha_1$, so $\mathrm{rk}(c) \leq \alpha_1 < \alpha_0$, contradicting the choice of $\alpha_0$.
:::

:::corollary{#cor-omega-model-contains-l}
Let $(M, E)$ be an ω-model of KP. The ordinal of the transitive collapse of its standard part is at least $\omega_1^{\mathrm{CK}}$, and every subset of $\nat$ in $L_{\omega_1^{\mathrm{CK}}}$ is represented in $M$: it is the set of numbers $E$-below some element of $M$.
:::

:::proof{of=cor-omega-model-contains-l}
By :ref{#lem-standard-kp}, the collapse $N$ of the standard part is admissible. Since $M$ is an ω-model, the natural numbers and the set $\omega$ of $M$ are in the standard part, so $\omega \in N$ and $o(N) > \omega$. By :ref{#prop-admissible-above-ck}, $o(N) \geq \omega_1^{\mathrm{CK}}$. By :ref{#fact-l-absolute}, $L_\beta \in N$ for every $\beta < \omega_1^{\mathrm{CK}}$, so every subset of $\nat$ in $L_{\omega_1^{\mathrm{CK}}}$ is an element of $N$. The collapse fixes the natural numbers, so such a set corresponds to an element of the standard part of $M$ whose $E$-elements are exactly its members.
:::

::::exercise[Non-standard ordinals]{#ex-nonstandard-ordinals difficulty=1 objective="Relate the well-foundedness of an ω-model of KP to its ordinals."}
Let $(M, E)$ be an ω-model of KP. Show that $M$ is well-founded if and only if every ordinal of $M$ is in its standard part.

:::solution
If $M$ is well-founded, $M$ itself is $E$-closed and well-founded, so it is its own standard part. Conversely, if every ordinal of $M$ is standard, then every element of $M$ has a standard rank, so it is standard by :ref{#lem-standard-rank}; the standard part is $M$, which is therefore well-founded.
:::
::::

## Notes and references

Gödel introduced the constructible universe in 1938 to prove the consistency of the axiom of choice and the generalized continuum hypothesis. The characterization of admissible ordinals through $L_\alpha$ and the analysis of ω-models are in Chong and Yu (Theorems 3.3.4 and 3.3.6, Proposition 3.3.12, Lemmas 3.5.3 and 3.5.4, Proposition 3.5.5); the proof of :ref{#cor-omega-model-contains-l} given here uses :ref{#prop-admissible-above-ck} instead of their induction along the levels $J_\beta$. Barwise (*Admissible Sets and Structures*, Chapter II) proves recursion along well-founded relations in admissible sets.

- K. Gödel, *The consistency of the axiom of choice and of the generalized continuum-hypothesis*, Proceedings of the National Academy of Sciences 24 (1938), 556–557.
- K. J. Devlin, *Constructibility*, Springer, 1984.
- J. Barwise, *Admissible Sets and Structures*, Springer, 1975.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Sections 3.3 and 3.5.

:::::exercises
::::exercise{#ex-computable-in-l-omega-plus-one difficulty=1 objective="Locate the computable and the arithmetic sets in the constructible hierarchy."}
Show that every computable set and every c.e. set belongs to $L_{\omega+1}$, and every arithmetic set to $L_{\omega+1}$ as well.

:::solution
By :ref{#thm-hf-ce}, a c.e. set is $\Sigma_1$-definable over $\mathrm{HF} = L_\omega$, so it belongs to $\mathrm{Def}(L_\omega) = L_{\omega+1}$. An arithmetic set is defined by a first-order formula of arithmetic, which translates, through the definitions of addition and multiplication over $\mathrm{HF}$ in the proof of :ref{#thm-hf-ce}, into a formula of set theory over $L_\omega$; so it also belongs to $L_{\omega+1}$. In particular every computable set is in $L_{\omega+1}$.
:::
::::
:::::
