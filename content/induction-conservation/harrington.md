---
title: Harrington's conservation theorem
summary: WKL₀ proves the same Π¹₁ sentences as RCA₀; a forcing construction over a countable non-standard model adds a path through an infinite tree while preserving Σ⁰₁ induction; consequences for the first-order part of WKL₀.
duration: 45
prerequisites: [first-order-parts, big-five/wkl0]
---

Weak König's lemma is not provable in $\mathsf{RCA}_0$: the computable sets form an ω-model of $\mathsf{RCA}_0$ in which it fails. Harrington proved that it nevertheless adds no new arithmetic consequences, nor even new $\Pi^1_1$ consequences. The proof shows that every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$. In an ω-model, adding a path through a tree only requires closing under Turing reducibility, since induction holds automatically. In a non-standard model, the path must be chosen so that $\Sigma^0_1$ induction survives, and this is achieved by forcing with infinite subtrees.

## Π¹₁ conservation

:::proposition{#prop-pi11-conservation-method}
Let $S \subseteq T$ be $\mathcal L_2$-theories. If every countable model of $S$ has an ω-extension satisfying $T$, then $T$ is $\Pi^1_1$-conservative over $S$.
:::

:::proof{of=prop-pi11-conservation-method}
Let $\forall X\, \varphi(X)$ be a $\Pi^1_1$ sentence, with $\varphi$ arithmetic, not provable in $S$. A countable model $\mathcal M$ of $S + \exists X\, \neg \varphi(X)$ contains a set $A$ with $\mathcal M \models \neg \varphi(A)$. Let $\mathcal N$ be an ω-extension of $\mathcal M$ satisfying $T$. Then $A$ belongs to $\mathcal N$, and $\mathcal N \models \neg \varphi(A)$ since $\varphi$ is arithmetic. So $T$ does not prove $\forall X\, \varphi(X)$.
:::

:::theorem[Harrington]{#thm-harrington}
Every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$. Consequently, $\mathsf{WKL}_0$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, and a conservative extension of $\mathrm I\Sigma_1$.
:::

The second statement follows from the first by :ref{#prop-pi11-conservation-method}, since every sentence of $\mathcal L_1$ is $\Pi^1_1$, and by :ref{#thm-rca0-isigma1}. The rest of the lesson proves the first statement.

## Setting

Fix a countable model $\mathcal M = (M, \mathcal S)$ of $\mathsf{RCA}_0$. Binary strings are coded by numbers, so that the length $|\sigma|$ and the bits $\sigma(i)$ are given by bounded formulas, and quantifiers over the strings of a given length are bounded, up to provable equivalence in $\mathsf{RCA}_0$; we use this coding without further comment. A **tree** is a set of strings closed under prefixes, and a tree $S \in \mathcal S$ is **$\mathcal M$-infinite** if $\mathcal M \models \forall n\ \exists \sigma \in S\ |\sigma| = n$. For binary trees, $\mathsf{RCA}_0$ proves that this is equivalent to being infinite as a set, since there are finitely many strings of each length.

A set $G \subseteq M$, not necessarily in $\mathcal S$, is a **path** through a tree $S \in \mathcal S$ if for every $n \in M$ there is $\sigma \in S$ of length $n$ with $\sigma(i) = 1 \leftrightarrow i \in G$ for $i < n$; this string is written $G \uh n$. We write $\mathcal M \cup \{ G \}$ for the ω-extension of $\mathcal M$ with second-order part $\mathcal S \cup \{ G \}$, and $\mathcal M[G]$ for the ω-extension whose sets are those $\Delta^0_1$-definable in $\mathcal M \cup \{ G \}$.

:::lemma{#lem-sigma1-normal-form}
Let $F(x, X)$ be a $\Sigma^0_1$ formula with parameters in $\mathcal M$ and a free set variable $X$. There is a bounded formula $H(x, \sigma)$ with parameters in $\mathcal M$ such that $H(x, \sigma)$ implies $H(x, \tau)$ whenever $\sigma \preceq \tau$, and such that for every tree $S \in \mathcal S$, every path $G$ through $S$, and every $x \in M$:
$$
\mathcal M \cup \{ G \} \models F(x, G) \iff \text{there is } k \in M \text{ with } \mathcal M \models H(x, G \uh k).
$$
:::

:::proof{of=lem-sigma1-normal-form}
Write $F = \exists y\, \delta(x, y, X)$ with $\delta$ bounded. By induction on $\delta$, there is a term $p(x, y)$ such that, for all values of the bounded variables within their bounds, every term $t$ of an atomic formula $t \in X$ of $\delta$ has a value less than $p(x, y)$: terms are polynomials with non-negative coefficients, which are monotone, so it suffices to replace each bounded variable by its bound. Let $\delta(x, y, \sigma)$ be the formula obtained by replacing $t \in X$ by "$t < |\sigma| \wedge \sigma(t) = 1$", and
$$
H(x, \sigma) \equiv \exists y < |\sigma|\ (p(x, y) \leq |\sigma| \wedge \delta(x, y, \sigma)).
$$
It is bounded and monotone in $\sigma$. If $|\sigma| \geq p(x, y)$ and $\sigma = G \uh |\sigma|$, then $\delta(x, y, G)$ and $\delta(x, y, \sigma)$ have the same truth value, by induction on $\delta$, since every atomic formula $t \in X$ is evaluated at some $t < p(x, y)$, where $\sigma$ and $G$ agree. If $\mathcal M \cup \{ G \} \models \delta(x, y, G)$, take $k$ larger than $y$ and $p(x, y)$. Conversely, if $H(x, G \uh k)$ holds with witness $y$, then $\delta(x, y, G)$ holds.
:::

The lemma does not use any induction in $\mathcal M \cup \{ G \}$: the translation is made formula by formula, in the metatheory. This is important, since induction in $\mathcal M \cup \{ G \}$ is what we must establish.

## Forcing with infinite subtrees

Fix an $\mathcal M$-infinite tree $T \in \mathcal S$. Let $\mathbb P$ be the set of $\mathcal M$-infinite trees $S \in \mathcal S$ with $S \subseteq T$, ordered by inclusion. A set $D \subseteq \mathbb P$ is **dense** if every $S \in \mathbb P$ has a subtree in $D$.

:::lemma{#lem-harrington-unique}
For every $n \in M$, the set $D_n$ of trees $S \in \mathbb P$ with exactly one string of length $n$ is dense.
:::

:::proof{of=lem-harrington-unique}
Let $S \in \mathbb P$. For each string $\sigma$ of length $n$, the tree $S^\sigma = \{ \tau \in S : \tau \preceq \sigma \vee \sigma \preceq \tau \}$ belongs to $\mathcal S$ by $\Delta^0_1$ comprehension, and has at most one string of length $n$. Suppose that none of them is $\mathcal M$-infinite: every $\sigma$ of length $n$ has some $m$ such that $S^\sigma$ has no string of length $m$. This is a bounded quantification of a $\Sigma^0_1$ formula, so by $\mathsf B\Sigma^0_1$, which holds in $\mathcal M$, there is $m^*$, which we may take at least $n$, such that every $S^\sigma$ has no string of some length $m < m^*$; since $S^\sigma$ is closed under prefixes, it has no string of length $m^*$ either. Then $S$ has no string $\rho$ of length $m^*$, since $\rho$ would belong to $S^{\rho \uh n}$. This contradicts the $\mathcal M$-infiniteness of $S$. So some $S^\sigma$ is $\mathcal M$-infinite; it belongs to $\mathbb P$, and its only string of length $n$ is $\sigma$, so it belongs to $D_n$.
:::

The second family of dense sets decides, with a single condition, a $\Sigma^0_1$ formula at all the numbers below a given bound $b$, which may be non-standard. For $S \in \mathbb P$, a bounded formula $H$ and $a \in M$, let
$$
\Phi_S(a) \equiv \exists m\ \forall \rho \in S\ (|\rho| = m \rightarrow \exists k \leq m\ H(a, \rho \uh k)), \qquad \Psi_S(a) \equiv \forall \rho \in S\ \forall k \leq |\rho|\ \neg H(a, \rho \uh k).
$$
The formula $\Phi_S$ is $\Sigma^0_1$ and $\Psi_S$ is $\Pi^0_1$, with parameters in $\mathcal M$. If $G$ is a path through $S$: if $\Phi_S(a)$ holds in $\mathcal M$, then $H(a, G \uh k)$ holds for some $k$, since $G \uh m \in S$; if $\Psi_S(a)$ holds, then $H(a, G \uh k)$ holds for no $k$.

:::lemma{#lem-harrington-decide}
Let $F(x, X)$ be a $\Sigma^0_1$ formula with parameters in $\mathcal M$, $H$ given by :ref{#lem-sigma1-normal-form}, and $b \in M$. The set $D_{F, b}$ of trees $S \in \mathbb P$ such that $\mathcal M \models \Phi_S(a) \vee \Psi_S(a)$ for every $a < b$ is dense.
:::

:::proof{of=lem-harrington-decide}
Let $S \in \mathbb P$. For every string $\sigma$ of length $b$, let
$$
S_\sigma = \{ \rho \in S : \forall a < b\ (\sigma(a) = 0 \rightarrow \forall k \leq |\rho|\ \neg H(a, \rho \uh k)) \}.
$$
It belongs to $\mathcal S$ by $\Delta^0_1$ comprehension, and it is a tree, since the condition is inherited by prefixes. The set $U$ of strings $\sigma$ of length $b$ such that $S_\sigma$ is $\mathcal M$-infinite is defined by a $\Pi^0_1$ formula, and contains the string $1^b$, since $S_{1^b} = S$. Code the strings of length $b$ so that the numerical order is the lexicographic order. By $\mathsf L\Pi^0_1$, which holds in $\mathcal M$ by :ref{#prop-least-number}, $U$ has a lexicographically least element $\sigma$. We show $S_\sigma \in D_{F, b}$; it belongs to $\mathbb P$ since $\sigma \in U$. Let $a < b$.

- If $\sigma(a) = 0$, then $\Psi_{S_\sigma}(a)$ holds by definition of $S_\sigma$.
- If $\sigma(a) = 1$, let $\tau$ be the string of length $b$ that agrees with $\sigma$ below $a$, has $\tau(a) = 0$, and $\tau(i) = 1$ for $a < i < b$. It is lexicographically smaller than $\sigma$, so $\tau \notin U$: there is $m$ such that $S_\tau$ has no string of length $m$. Let $\rho \in S_\sigma$ with $|\rho| = m$. The string $\rho$ satisfies the conditions of $S_\sigma$ at the positions below $a$, which are those of $S_\tau$ below $a$, and $S_\tau$ has no other condition except at $a$. Since $\rho \notin S_\tau$, the condition at $a$ fails: $H(a, \rho \uh k)$ for some $k \leq m$. So $\Phi_{S_\sigma}(a)$ holds, with this $m$.
:::

:::quiz[deciding with one condition]
Why must a single condition decide $F(a, G)$ for all $a < b$ at once, as in :ref{#lem-harrington-decide}, rather than each $a$ being decided by its own extension along the construction?

- [x] The proof of :ref{#lem-harrington-induction} needs one tree $S \in \mathcal S$ with $F(a, G) \leftrightarrow \Phi_S(a)$ for every $a \leq b$, so that induction in $\mathcal M$ applies to the single $\Sigma^0_1$ formula $\Phi_S$; when $b$ is non-standard, conditions chosen separately for infinitely many $a$ give no formula over $\mathcal M$. The lexicographically least element of $U$ provides such an $S$.
- [ ] Because a single $a$ cannot be decided.

  A single $a$ is decided by restricting to the subtree avoiding $H(a, \cdot)$, if it is $\mathcal M$-infinite, and by $S$ itself otherwise.
- [ ] Because the family of dense sets must be countable.

  It would be countable in any case: $M$ is countable, so the dense sets deciding one $a \in M$ at a time form a countable family.

---

Why does the lexicographic minimality of $\sigma$ give $\Phi_{S_\sigma}(a)$ when $\sigma(a) = 1$?

- [x] Because changing the bit at $a$ to $0$, and the later bits to $1$, gives a smaller string, whose tree is finite; every long enough string of $S_\sigma$ is excluded from that tree only by the condition at $a$, so it meets $H(a, \cdot)$.
- [ ] Because $\sigma(a) = 1$ means that $F(a, G)$ holds.

  The bit records a choice of subtree; the meaning is obtained from the minimality.
- [ ] Because $S_\sigma = S$.

  $S_\sigma$ may be a proper subtree of $S$.
:::

## The generic path

The sets $D_n$ for $n \in M$, and $D_{F, b}$ for $\Sigma^0_1$ formulas $F$ with parameters in $\mathcal M$ and $b \in M$, form a countable family, since $M$, $\mathcal S$ and the set of formulas are countable. List them as $E_0, E_1, \dots$, and build $T = S_0 \supseteq S_1 \supseteq \cdots$ in $\mathbb P$ with $S_{i+1} \in E_i$, by density.

For $n \in M$, let $S_i \in D_n$ and let $\rho_n$ be its unique string of length $n$. It does not depend on the choice of $i$: if $j \geq i$, then $S_j \subseteq S_i$ is $\mathcal M$-infinite, so it has a string of length $n$, which belongs to $S_i$ and is therefore $\rho_n$; so all the $S_j$ with $j \geq i$ have $\rho_n$ as their only string of length $n$. The same argument shows that $\rho_n$ belongs to every $S_j$, and that $\rho_n \preceq \rho_{n'}$ for $n \leq n'$. Let $G = \{ i \in M : \rho_{i+1}(i) = 1 \}$. Then $G \uh n = \rho_n$, and $G$ is a path through every $S_j$, in particular through $T$.

:::lemma{#lem-harrington-induction}
$\mathcal M \cup \{ G \}$ satisfies $\mathsf I\Sigma^0_1$.
:::

:::proof{of=lem-harrington-induction}
Let $F(x, G)$ be a $\Sigma^0_1$ formula with parameters in $\mathcal M$ and $G$, such that $F(0, G)$ and $\forall x\, (F(x, G) \rightarrow F(x+1, G))$ hold in $\mathcal M \cup \{ G \}$, and suppose $\neg F(b, G)$ for some $b \in M$. Let $S = S_j \in D_{F, b+1}$, and $H$ as in :ref{#lem-sigma1-normal-form}. For $a \leq b$, we claim that $F(a, G)$ holds if and only if $\mathcal M \models \Phi_S(a)$. If $\Phi_S(a)$, then $F(a, G)$ by the remark before :ref{#lem-harrington-decide} and :ref{#lem-sigma1-normal-form}. If $F(a, G)$, then $\Psi_S(a)$ fails, so $\Phi_S(a)$ holds since $S \in D_{F, b+1}$.

Hence, in $\mathcal M$: $\Phi_S(0)$ holds, $\Phi_S(a) \rightarrow \Phi_S(a+1)$ for every $a < b$, and $\neg \Phi_S(b)$. The formula $a \leq b \rightarrow \Phi_S(a)$ is $\Sigma^0_1$ with parameters in $\mathcal M$, so $\Sigma^0_1$ induction in $\mathcal M$ gives $\Phi_S(b)$: a contradiction.
:::

:::lemma{#lem-harrington-extension}
$\mathcal M[G]$ is an ω-extension of $\mathcal M$ satisfying $\mathsf{RCA}_0$, and $G \in \mathcal M[G]$ is a path through $T$ in the sense of $\mathcal M[G]$.
:::

:::proof{of=lem-harrington-extension}
Every set of $\mathcal S$, and $G$, is defined by a bounded formula, so belongs to $\mathcal M[G]$. By :ref{#lem-harrington-induction} and :ref{#thm-induction-collection}, $\mathcal M \cup \{ G \}$ satisfies $\mathsf B\Sigma^0_1$. So :ref{#lem-delta1-substitution} applies to $\mathcal M \cup \{ G \}$ and finitely many sets of $\mathcal M[G]$: every $\Sigma^0_1$ or $\Pi^0_1$ formula with parameters in $\mathcal M[G]$ is equivalent in $\mathcal M[G]$ to a formula of the same class with parameters in $\mathcal M \cup \{ G \}$. As in the proof of :ref{#thm-rca0-isigma1}, $\Sigma^0_1$ induction in $\mathcal M[G]$ reduces to :ref{#lem-harrington-induction}, and $\Delta^0_1$ comprehension holds because a set $\Delta^0_1$-definable with parameters in $\mathcal M[G]$ is $\Delta^0_1$-definable with parameters in $\mathcal M \cup \{ G \}$. Finally, "every initial segment of $G$ belongs to $T$" is an arithmetic statement about $G$ and $T$, true by construction.
:::

:::proof{of=thm-harrington}
Let $\mathcal M_0$ be a countable model of $\mathsf{RCA}_0$. We build countable ω-extensions $\mathcal M_0 \subseteq \mathcal M_1 \subseteq \cdots$, all models of $\mathsf{RCA}_0$, as follows. Fix a bijection $i \mapsto (i_0, i_1)$ from $\nat$ to $\nat^2$ with $i_0 \leq i$. At step $i$, consider the $i_1$-th set of $\mathcal M_{i_0}$, in a fixed enumeration of its sets. If it is an $\mathcal M_i$-infinite tree $T$, let $\mathcal M_{i+1} = \mathcal M_i[G]$ for a path $G$ through $T$ given by the construction above, applied to $\mathcal M_i$; otherwise let $\mathcal M_{i+1} = \mathcal M_i$. By :ref{#lem-harrington-extension}, every $\mathcal M_{i+1}$ is a model of $\mathsf{RCA}_0$; it is countable, since its sets are defined by formulas with parameters in the countable structure $\mathcal M_i \cup \{ G \}$.

Let $\mathcal N$ be the union: same first-order part, and the union of the second-order parts. Every instance of the axioms of $\mathsf{RCA}_0$ in $\mathcal N$ has finitely many set parameters, all in some $\mathcal M_i$, and is arithmetic apart from the conclusion of comprehension; it holds in $\mathcal M_i$, with the same meaning, and the set given by comprehension in $\mathcal M_i$ belongs to $\mathcal N$. So $\mathcal N \models \mathsf{RCA}_0$. If $T \in \mathcal N$ is an infinite tree in the sense of $\mathcal N$, it is the $i_1$-th set of some $\mathcal M_{i_0}$, and it is infinite in the sense of $\mathcal M_i$ at step $i$, since this is arithmetic; so a path through $T$ was added at step $i$, and it belongs to $\mathcal N$. So $\mathcal N \models \mathsf{WKL}_0$.
:::

## Consequences

By :ref{#thm-harrington}, $\mathsf{WKL}_0$ and $\mathsf{RCA}_0$ prove the same arithmetic sentences, and even the same $\Pi^1_1$ sentences. Compactness arguments in analysis, such as the boundedness of continuous functions on $[0, 1]$ or Gödel's completeness theorem, therefore have no consequences for the natural numbers beyond $\mathrm I\Sigma_1$. Since $\mathrm I\Sigma_1$ is $\Pi_2$-conservative over primitive recursive arithmetic, every $\Pi_2$ sentence of $\mathcal L_1$ provable in $\mathsf{WKL}_0$ is provable in primitive recursive arithmetic, a system regarded as finitistic in Hilbert's sense; Simpson presents this as a partial realization of Hilbert's program.

The theorem does not extend to $\Pi^1_2$ sentences: $\mathsf{WKL}$ itself is $\Pi^1_2$.

:::quiz[the generic extension]
Why is the extension $\mathcal M[G]$ taken, rather than $\mathcal M \cup \{ G \}$?

- [x] Because $\mathcal M \cup \{ G \}$ does not satisfy $\Delta^0_1$ comprehension in general: sets computable from $G$ and sets of $\mathcal M$, such as $G \oplus A$, must be added.
- [ ] Because $\mathcal M \cup \{ G \}$ does not satisfy $\Sigma^0_1$ induction.

  It does, by :ref{#lem-harrington-induction}; this is what makes $\mathcal M[G]$ a model.
- [ ] Because $G$ is not a path in $\mathcal M \cup \{ G \}$.

  It is a path in both structures, since the property is arithmetic.

---

Why does the proof of :ref{#thm-harrington} handle each tree at a stage $i$ with $i_0 \leq i$?

- [x] Because the tree must already belong to $\mathcal M_i$ when its path is added; the enumeration of pairs revisits every set of every $\mathcal M_{i_0}$ at a later stage.
- [ ] Because the trees must be handled in increasing order of size.

  The order is only a bookkeeping device.
- [ ] Because $\mathcal M_i$ is finite.

  Each $\mathcal M_i$ is countable and infinite.
:::

## Exercises

::::exercise{difficulty=1}
Let $\mathcal S$ be a countable ω-model of $\mathsf{RCA}_0$, that is, a countable Turing ideal. Show directly that $\mathcal S$ is contained in a countable ω-model of $\mathsf{WKL}_0$, and explain why the forcing argument is only needed for non-standard models.

:::solution
Let $T \in \mathcal S$ be an infinite binary tree. It has a path $G$ in $\mathcal P(\nat)$, and the class of sets computable in $G \oplus A$ for some $A \in \mathcal S$ is a countable Turing ideal containing $\mathcal S$ and $G$. Iterating as in the proof of :ref{#thm-harrington} gives a countable Turing ideal $\mathcal N \supseteq \mathcal S$ in which every infinite tree has a path, which is an ω-model of $\mathsf{WKL}_0$ by :ref{#thm-rca-turing-ideal}. No condition on $G$ is needed, because every ω-model satisfies full induction. In a non-standard model, the fact that every initial segment of $G$ belongs to the model does not guarantee $\Sigma^0_1$ induction for formulas mentioning $G$; the forcing construction is designed to ensure it.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{WKL}_0$ proves neither $\mathsf B\Sigma^0_2$ nor $\mathsf{RT}^1_{<\infty}$.

:::solution
By the theorem of Paris and Kirby recalled in the first lesson, there is a model of $\mathrm I\Sigma_1$ in which some instance of $\Sigma_2$ collection, an $\mathcal L_1$ sentence $\sigma$, fails. So $\mathrm I\Sigma_1$ does not prove $\sigma$, and by :ref{#thm-harrington}, neither does $\mathsf{WKL}_0$. Since $\sigma$ is an instance of $\mathsf B\Sigma^0_2$, $\mathsf{WKL}_0$ does not prove $\mathsf B\Sigma^0_2$. By :ref{#thm-hirst}, which holds over $\mathsf{RCA}_0 \subseteq \mathsf{WKL}_0$, it does not prove $\mathsf{RT}^1_{<\infty}$ either.
:::
::::

## Notes and references

Harrington's theorem was circulated in the late 1970s. The forcing proof presented here follows Monin and Patey; Simpson's monograph gives a detailed treatment, and discusses the relation with Hilbert's program.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section IX.2.
- S. G. Simpson, *Partial realizations of Hilbert's program*, Journal of Symbolic Logic 53 (1988), 349–363.
