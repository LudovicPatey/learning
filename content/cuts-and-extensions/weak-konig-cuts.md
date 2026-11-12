---
title: Weak König's lemma in cuts
summary: Binary strings coded by numbers in IΔ₀ + exp; every unbounded binary tree coded in a proper exponential cut has an unbounded coded branch (Scott); the standard system of a non-standard model of IΔ₀ + exp is a Scott set.
duration: 40
prerequisites: [standard-system]
---

The previous lesson showed that the standard system of a non-standard model is closed under computations. This lesson adds the compactness principle of weak König's lemma: an infinite binary tree in the standard system has an infinite path in the standard system. The proof is an instance of the non-standard method. The tree, restricted to the cut, has nodes of every length in the cut; by overspill it has a node $\tau_0$ of a length above the cut; and the prefixes of $\tau_0$ that lie in the cut form a branch. We prove this for every proper exponential cut; for the standard cut, it makes the standard system a Scott set.

Throughout, $M$ is a model of $\mathrm I\Delta_0 + \mathrm{exp}$.

## Binary strings inside a model

A binary string $\sigma$ of length $\ell$ is coded by the number with binary digits $\sigma(0), \dots, \sigma(\ell - 1)$ followed by a leading digit $1$ at position $\ell$; the leading digit records the length.

:::definition{#def-strings-model}
In $M$, a **string** is an element $s \geq 1$. Its **length** $\mathrm{len}(s)$ is the $\ell$ with $2^\ell \leq s < 2^{\ell + 1}$, and its digit at $i < \ell$ is $1$ if $i \in s$ and $0$ otherwise. For strings $\sigma, \tau$, the relation $\sigma \sqsubseteq \tau$, "$\sigma$ is a prefix of $\tau$", is
$$
\mathrm{len}(\sigma) \leq \mathrm{len}(\tau) \wedge \forall i < \mathrm{len}(\sigma)\ (i \in \sigma \leftrightarrow i \in \tau).
$$
For $\ell \leq \mathrm{len}(\tau)$, the **restriction** $\tau \restriction \ell$ is $2^\ell + q$, where $q$ is the remainder of $\tau$ in the division by $2^\ell$.
:::

In $\nat$, the map sending a string $\sigma \in 2^{<\nat}$ of length $\ell$ to $2^\ell + \sum_{i < \ell} \sigma(i) 2^i$ is a computable bijection between $2^{<\nat}$ and the positive integers; for instance the empty string is coded by $1$, and the string $011$ by $8 + 2 + 4 = 14$. The relation $y = 2^x$ is bounded (:ref{#fact-exp}), so "$\ell = \mathrm{len}(s)$", "$\sigma \sqsubseteq \tau$" and "$\sigma = \tau \restriction \ell$" are expressed by bounded formulas.

:::lemma{#lem-strings-model}
$\mathrm I\Delta_0 + \mathrm{exp}$ proves:

1. every $s \geq 1$ has a unique length, and $\mathrm{len}(s) < s$;
2. if $\ell \leq \mathrm{len}(\tau)$, then $\tau \restriction \ell$ is a string of length $\ell$, $\tau \restriction \ell \sqsubseteq \tau$, and $\tau \restriction \ell \leq \tau$;
3. if $\sigma \sqsubseteq \tau$, then $\sigma = \tau \restriction \mathrm{len}(\sigma)$; in particular $\sigma \leq \tau$;
4. if $\sigma \sqsubseteq \tau$ and $\sigma' \sqsubseteq \tau$, then $\sigma \sqsubseteq \sigma'$ or $\sigma' \sqsubseteq \sigma$; and $\sqsubseteq$ is transitive.
:::

:::proof{of=lem-strings-model}
1. The set of $\ell \leq s$ with $2^\ell \leq s$ is defined by a bounded formula and contains $0$; by the least number principle for bounded formulas (:ref{#prop-idelta0-basic}), applied to its upper bounds, it has a largest element $\ell$. Then $2^{\ell + 1} > s$, since otherwise $\ell + 1 \leq 2^{\ell + 1} \leq s$ would belong to the set. Uniqueness follows from the monotonicity of $x \mapsto 2^x$, and $\ell < 2^\ell \leq s$.

2. Write $\tau = 2^\ell u + q$ with $q < 2^\ell$, and $\sigma = 2^\ell + q$. Then $2^\ell \leq \sigma < 2^{\ell + 1}$, so $\mathrm{len}(\sigma) = \ell$. For $i < \ell$, the splitting property of :ref{#lem-ack-basic}, applied to $\sigma = 2^\ell \cdot 1 + q$ and to $\tau = 2^\ell u + q$, gives $i \in \sigma \leftrightarrow i \in q \leftrightarrow i \in \tau$. If $\ell < \mathrm{len}(\tau)$, then $\tau \geq 2^{\ell + 1} > \sigma$; if $\ell = \mathrm{len}(\tau)$, then $u = 1$ and $\sigma = \tau$.

3. Let $\ell = \mathrm{len}(\sigma)$, and write $\sigma = 2^\ell + q'$ and $\tau \restriction \ell = 2^\ell + q$, with $q, q' < 2^\ell$. For $i < \ell$, $i \in q' \leftrightarrow i \in \sigma \leftrightarrow i \in \tau \leftrightarrow i \in q$, by splitting and the hypothesis. By extensionality (:ref{#lem-ack-basic}), $q = q'$. With item 2, $\sigma \leq \tau$.

4. If $\mathrm{len}(\sigma) \leq \mathrm{len}(\sigma')$, both agree with $\tau$ below $\mathrm{len}(\sigma)$, so $\sigma \sqsubseteq \sigma'$. Transitivity is immediate from the definition.
:::

## Trees in a cut

:::definition{#def-tree-cut}
Let $I$ be a cut of $M$. A **binary tree** in $I$ is a set $T \subseteq I$ of strings such that every string $\sigma \sqsubseteq \tau$ with $\tau \in T$ belongs to $T$. It is **unbounded** if for every $\ell \in I$ some $\tau \in T$ has length $\ell$. A **branch** of $T$ is a binary tree $B \subseteq T$ whose elements are pairwise comparable for $\sqsubseteq$.
:::

The prefixes of an element of $I$ are below it, by :ref{#lem-strings-model}, hence in $I$. The cut is used with its **exponential** closure (:ref{#def-exp}): if $I$ is closed under $x \mapsto 2^x$, every string of length $\ell \in I$ is below $2^{\ell + 1} \in I$, so the strings of the cut are exactly the strings whose length is in the cut. For $I = \nat$, a binary tree in $\nat$ is a tree $T \subseteq 2^{<\nat}$ in the usual sense, read through the coding of strings; it is unbounded if and only if it is infinite, since it has finitely many nodes of each length and is closed under prefixes; and an unbounded branch is the set of initial segments of an infinite path.

:::theorem[Scott]{#thm-scott-wkl-cut}
Let $I$ be a proper exponential cut of $M$. Every unbounded binary tree $T \in \mathrm{Cod}(M/I)$ has an unbounded branch $B \in \mathrm{Cod}(M/I)$.
:::

The proof passes from the cut to the model and back. Inside $M$, the statement "the tree coded by $t$ has a node of length $\ell$ all of whose prefixes are in the tree" is bounded and holds for every $\ell \in I$. By overspill it holds for some $\ell_0$ above $I$, which gives a node $\tau_0$ of non-standard length relative to the cut. Its prefixes form a branch, coded in $M$ by bounded comprehension; restricted to $I$, this branch is unbounded, because the prefix of $\tau_0$ of each length $\ell \in I$ is below $2^{\ell + 1}$, which is in $I$.

:::proof{of=thm-scott-wkl-cut}
Let $t \in M$ with $T = \mathrm{Ack}(t) \cap I$, and consider the bounded formula
$$
\theta(\ell) \equiv \exists \tau < t + 1\ \big( \tau \in t \wedge \tau \geq 1 \wedge \mathrm{len}(\tau) = \ell \wedge \forall \sigma < \tau + 1\ (\sigma \geq 1 \wedge \sigma \sqsubseteq \tau \rightarrow \sigma \in t) \big).
$$
*$\theta$ holds on $I$.* For $\ell \in I$, $T$ has a node $\tau$ of length $\ell$. It belongs to $\mathrm{Ack}(t)$, so $\tau < t$ (:ref{#lem-ack-basic}). Its prefixes are in $T$, since $T$ is a tree, and so in $\mathrm{Ack}(t)$.

*Overspill.* By :ref{#cor-overspill}, with $n = 0$, there is $\ell_0 \in M \setminus I$ with $M \models \theta(\ell_0)$; let $\tau_0$ be a witness, a node of length $\ell_0$ whose prefixes all belong to $\mathrm{Ack}(t)$.

*The branch.* By :ref{#thm-delta0-comprehension}, some $b \in M$ codes $\{ \sigma < \tau_0 + 1 : \sigma \geq 1 \wedge \sigma \sqsubseteq \tau_0 \}$; let $B = \mathrm{Ack}(b) \cap I$. Every $\sigma \in B$ is a prefix of $\tau_0$, so it belongs to $\mathrm{Ack}(t) \cap I = T$. If $\sigma' \sqsubseteq \sigma \in B$, then $\sigma' \sqsubseteq \tau_0$ by transitivity and $\sigma' \leq \sigma$, so $\sigma' \in B$; and two elements of $B$ are comparable by item 4 of :ref{#lem-strings-model}. So $B$ is a branch of $T$.

*Unboundedness.* Let $\ell \in I$. Then $\ell < \ell_0$, since $\ell_0 \notin I$, and $\sigma = \tau_0 \restriction \ell$ is a prefix of $\tau_0$ of length $\ell$, with $\sigma \leq \tau_0$ (:ref{#lem-strings-model}). As $\sigma < 2^{\ell + 1}$ and $I$ is exponential, $\sigma \in I$. So $\sigma \in B$.
:::

:::figure[The proof of :ref{#thm-scott-wkl-cut}. The tree has nodes of all lengths in $I$; by overspill it has a node $\tau_0$ of a length above $I$, whose prefixes all belong to the tree. The prefixes of $\tau_0$ that lie in $I$ form an unbounded branch.]
<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="A binary tree drawn upwards; by overspill the tree has a node tau0 of a length above the cut I; its prefixes of lengths in I form an unbounded branch"><line x1="300.0" y1="230.0" x2="150.0" y2="196.0" class="accent-stroke" stroke-width="2.2"/><line x1="300.0" y1="230.0" x2="450.0" y2="196.0" class="muted-stroke" stroke-width="1.2"/><line x1="150.0" y1="196.0" x2="61.8" y2="162.0" class="muted-stroke" stroke-width="1.2"/><line x1="150.0" y1="196.0" x2="238.2" y2="162.0" class="accent-stroke" stroke-width="2.2"/><line x1="450.0" y1="196.0" x2="538.2" y2="162.0" class="muted-stroke" stroke-width="1.2"/><line x1="238.2" y1="162.0" x2="186.3" y2="128.0" class="muted-stroke" stroke-width="1.2"/><line x1="238.2" y1="162.0" x2="290.1" y2="128.0" class="accent-stroke" stroke-width="2.2"/><line x1="538.2" y1="162.0" x2="486.3" y2="128.0" class="muted-stroke" stroke-width="1.2"/><line x1="290.1" y1="128.0" x2="259.6" y2="94.0" class="accent-stroke" stroke-width="2.2"/><line x1="290.1" y1="128.0" x2="320.7" y2="94.0" class="muted-stroke" stroke-width="1.2"/><line x1="486.3" y1="128.0" x2="516.9" y2="94.0" class="muted-stroke" stroke-width="1.2"/><line x1="259.6" y1="94.0" x2="277.6" y2="60.0" class="accent-stroke" stroke-width="2.2"/><line x1="259.6" y1="94.0" x2="241.6" y2="60.0" class="muted-stroke" stroke-width="1.2"/><line x1="516.9" y1="94.0" x2="534.8" y2="60.0" class="muted-stroke" stroke-width="1.2"/><line x1="277.6" y1="60.0" x2="267.0" y2="26.0" class="accent-stroke" stroke-width="2.2"/><line x1="241.6" y1="60.0" x2="252.2" y2="26.0" class="muted-stroke" stroke-width="1.2"/><circle cx="300.0" cy="230.0" r="3.5" class="accent-fill"/><circle cx="150.0" cy="196.0" r="3.5" class="accent-fill"/><circle cx="450.0" cy="196.0" r="3.5" class="node"/><circle cx="61.8" cy="162.0" r="3.5" class="node"/><circle cx="238.2" cy="162.0" r="3.5" class="accent-fill"/><circle cx="538.2" cy="162.0" r="3.5" class="node"/><circle cx="186.3" cy="128.0" r="3.5" class="node"/><circle cx="290.1" cy="128.0" r="3.5" class="accent-fill"/><circle cx="486.3" cy="128.0" r="3.5" class="node"/><circle cx="259.6" cy="94.0" r="3.5" class="accent-fill"/><circle cx="320.7" cy="94.0" r="3.5" class="node"/><circle cx="516.9" cy="94.0" r="3.5" class="node"/><circle cx="277.6" cy="60.0" r="3.5" class="accent-fill"/><circle cx="241.6" cy="60.0" r="3.5" class="node"/><circle cx="534.8" cy="60.0" r="3.5" class="node"/><circle cx="267.0" cy="26.0" r="3.5" class="accent-fill"/><circle cx="252.2" cy="26.0" r="3.5" class="node"/><line x1="60.0" y1="111.0" x2="560.0" y2="111.0" class="accent-stroke" stroke-width="1.4" stroke-dasharray="5 4"/><text x="40" y="103.0" class="label">lengths above I</text><text x="40" y="129.0" class="label">lengths in I</text><text x="285.0" y="30.0" text-anchor="middle" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="3">0</tspan></text><text x="470" y="220" text-anchor="middle" class="label">the branch B: prefixes of τ₀</text></svg>
:::

:::quiz[weak König's lemma in cuts]
Where is it used that the cut $I$ is exponential?

- [x] To show that the prefix $\tau_0 \restriction \ell$ of length $\ell \in I$ lies in $I$: it is below $2^{\ell + 1}$, which is in $I$ only because $I$ is closed under exponentiation.
- [ ] To apply overspill to $\theta$.

  Overspill for bounded formulas holds for every proper cut of a model of $\mathrm I\Delta_0$.
- [ ] To find the code $b$ of the prefixes of $\tau_0$.

  This uses bounded comprehension in $M$, which needs $\mathrm{exp}$ in $M$, not a property of $I$.

---

Why does the formula $\theta$ require all prefixes of $\tau$ to belong to $\mathrm{Ack}(t)$, rather than only $\tau \in t$?

- [x] Above $I$, the set $\mathrm{Ack}(t)$ need not be a tree: a node $\tau_0$ of length $\ell_0$ in $\mathrm{Ack}(t)$ could have prefixes of length in $I$ outside $T$, and then $B$ would not be contained in $T$.
- [ ] To make $\theta$ a bounded formula.

  The formula $\tau \in t \wedge \mathrm{len}(\tau) = \ell$ is already bounded.
- [ ] Because $T$ is not closed under prefixes.

  $T$ is a tree; the condition is about the elements of $\mathrm{Ack}(t)$ above $I$, which are not in $T$.
:::

## Scott sets

The two closure properties of the standard system are those of the following notion, named after Scott.

:::definition{#def-scott-set}
A **Scott set** is a Turing ideal $\mathcal X \subseteq \mathcal P(\nat)$ (:ref{#def-turing-ideal}) such that every infinite binary tree $T \subseteq 2^{<\nat}$ in $\mathcal X$ has an infinite path in $\mathcal X$.
:::

Since a Turing ideal is closed under computable translations, the coding of strings used to view trees as sets of numbers does not matter. Scott sets are the Scott ideals of the course on the Big Five (:ref{to="big-five/wkl0"}), that is, the ω-models of $\mathsf{WKL}_0$.

:::corollary{#cor-ssy-scott-set}
For every non-standard model $M$ of $\mathrm I\Delta_0 + \mathrm{exp}$, $\mathrm{SSy}(M)$ is a Scott set.
:::

:::proof{of=cor-ssy-scott-set}
By :ref{#thm-ssy-turing-ideal}, $\mathrm{SSy}(M)$ is a Turing ideal. The standard cut is proper and exponential. An infinite binary tree $T \in \mathrm{SSy}(M)$ is unbounded in $\nat$, so by :ref{#thm-scott-wkl-cut} it has an unbounded branch $B \in \mathrm{SSy}(M)$. The set $B$ contains exactly one string of each length, and these strings are the initial segments of a path $P$ of $T$, with $P(i) = \sigma(i)$ for the string $\sigma \in B$ of length $i + 1$. So $P$ is computable in $B$, and $P \in \mathrm{SSy}(M)$.
:::

## Exercises

::::exercise{#ex-exp-cut-closed difficulty=1}
Show that an exponential cut of a model of $\mathrm I\Delta_0 + \mathrm{exp}$ is closed under addition and multiplication.

:::solution
Let $a, b \in I$ and $m = \max(a, b)$. Then $a + b \leq 2m < 2^{m+1}$, which belongs to $I$ since $m + 1 \in I$; so $a + b \in I$. Then $a \cdot b \leq m \cdot m < 2^m \cdot 2^m = 2^{2m}$, which belongs to $I$ since $2m \in I$.
:::
::::

::::exercise{#ex-subset-sum difficulty=2}
Show in $\mathrm I\Delta_0 + \mathrm{exp}$: if $u, v < 2^a$ and every element of $u$ belongs to $v$, then $v = u + w$, where $w < 2^a$ codes the elements of $v$ that are not in $u$. Deduce that $u \leq v$, and that $u < v$ if some element of $v$ is not in $u$.

:::solution
By :ref{#thm-delta0-comprehension}, let $w < 2^a$ code $\{ i < a : i \in v \wedge i \notin u \}$. Prove by bounded induction on $x \leq a$, with the parameters $u, v, w$, that the remainders $u_x, v_x, w_x$ of $u, v, w$ modulo $2^x$ satisfy $v_x = u_x + w_x$. For $x = 0$, all are $0$. If the claim holds at $x < a$: by the splitting property of :ref{#lem-ack-basic}, the remainder modulo $2^{x+1}$ of a code $c$ is $c_x + 2^x$ if $x \in c$ and $c_x$ otherwise. At most one of $u$ and $w$ contains $x$, and $v$ contains $x$ if and only if one of them does; so $v_{x+1} = u_{x+1} + w_{x+1}$. At $x = a$, the remainders are the codes themselves. If some $i \in v$ is not in $u$, then $i \in w$, so $w \geq 2^i > 0$ and $u < v$.
:::
::::

## Notes and references

:ref{#thm-scott-wkl-cut} is Theorem 3.5 of Wong's notes ("essentially Scott"), proved in his Lecture 4; Wong states it for coded subsets of proper exponential cuts, with the same coding of strings, and observes that $\mathrm{exp}$ in $M$ can be avoided. Scott sets are named after Scott (1962), who characterized the sets representable in complete extensions of arithmetic. Wong's Lecture 4 also proves a converse of :ref{#thm-scott-wkl-cut} for countable models of $\mathsf{WKL}_0$ by the arithmetized completeness theorem (Scott; Tanaka), which belongs to the next course of the track.

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 3 and 4.
- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in Recursive Function Theory, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
