---
title: Forcing with infinite subtrees
summary: Given a countable model of RCA₀ and an infinite binary tree in it, a path chosen generically for forcing with infinite subtrees preserves Σ⁰₁ induction; a single condition decides a Σ⁰₁ formula at non-standardly many inputs.
duration: 50
prerequisites: [first-order-parts, big-five/wkl0]
---

Harrington's theorem, proved in the next lesson, states that every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$. Its core is a one-step result: a path can be added through one infinite tree without destroying $\Sigma^0_1$ induction (:ref{#thm-path-induction}). In an ω-model, any path would do, since induction holds automatically. In a non-standard model, an arbitrary path may destroy induction: the set of standard numbers is a path through the full binary tree, and it defines a cut (see the exercises). The path must therefore be chosen so that every $\Sigma^0_1$ formula about it behaves like a $\Sigma^0_1$ formula of the original model. This is achieved by **forcing with infinite subtrees**, the formalized version of forcing with $\Pi^0_1$ classes used for the basis theorems (:ref{#thm-low-basis}).

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

The second family of dense sets is the heart of the proof. In the proof of the low basis theorem (:ref{#thm-low-basis}), a single $\Sigma^0_1$ question, "does $\Phi^G_e(e)$ converge?", is decided by passing to the subtree of strings along which it does not converge, if that subtree is infinite. Here this is not enough: induction is about a formula $F(a, G)$ for all $a$ below some $b$, and $b$ may be non-standard, so infinitely many questions must be decided at once, by a single tree, in such a way that the answers are given by one formula over $\mathcal M$. The solution is to choose a string $\sigma$ of length $b$, which guesses the answers ($\sigma(a) = 0$ for "no"), as the lexicographically least guess whose tree is infinite.

The second family of dense sets decides, with a single condition, a $\Sigma^0_1$ formula at all the numbers below a given bound $b$, which may be non-standard. For $S \in \mathbb P$, a bounded formula $H$ and $a \in M$, let
$$
\Phi_S(a) \equiv \exists m\ \forall \rho \in S\ (|\rho| = m \rightarrow \exists k \leq m\ H(a, \rho \uh k)), \qquad \Psi_S(a) \equiv \forall \rho \in S\ \forall k \leq |\rho|\ \neg H(a, \rho \uh k).
$$
The formula $\Phi_S$ is $\Sigma^0_1$ and $\Psi_S$ is $\Pi^0_1$, with parameters in $\mathcal M$. If $G$ is a path through $S$: if $\Phi_S(a)$ holds in $\mathcal M$, then $H(a, G \uh k)$ holds for some $k$, since $G \uh m \in S$; if $\Psi_S(a)$ holds, then $H(a, G \uh k)$ holds for no $k$.

:::figure[The choice made in the proof of :ref{#lem-harrington-decide}, for $b = 3$. Each string $\sigma$ of length $b$ guesses which of $F(0, G), F(1, G), F(2, G)$ fail (bit $0$); its tree $S_\sigma$ keeps the strings of $S$ compatible with the guessed failures. The least $\sigma$ whose tree is infinite is chosen. A bit $1$ at $a$ is forced to be correct: the guess with $0$ at $a$ and $1$ after it is smaller, so its tree is finite.]
<svg class="fig" viewBox="0 0 600 210" width="600" role="img" aria-label="The eight strings of length 3 in lexicographic order; those whose tree is infinite are marked; the least of them, 011, is chosen; its bit 0 at position 0 forces the formula to fail at 0, its bits 1 at positions 1 and 2 force it to hold there"><text x="52" y="78" text-anchor="end" class="math" font-size="15">σ</text><text x="52" y="134" text-anchor="end" class="label">tree</text><rect x="60" y="54" width="60" height="36" class="cell"/><text x="90.0" y="78" text-anchor="middle" class="mrm" font-size="15">000</text><text x="90.0" y="134" text-anchor="middle" class="label muted">finite</text><rect x="120" y="54" width="60" height="36" class="cell"/><text x="150.0" y="78" text-anchor="middle" class="mrm" font-size="15">001</text><text x="150.0" y="134" text-anchor="middle" class="label muted">finite</text><rect x="180" y="54" width="60" height="36" class="cell"/><text x="210.0" y="78" text-anchor="middle" class="mrm" font-size="15">010</text><text x="210.0" y="134" text-anchor="middle" class="label muted">finite</text><rect x="240" y="54" width="60" height="36" class="cell head-cell"/><text x="270.0" y="78" text-anchor="middle" class="mrm" font-size="15">011</text><text x="270.0" y="134" text-anchor="middle" class="label">infinite</text><rect x="300" y="54" width="60" height="36" class="cell"/><text x="330.0" y="78" text-anchor="middle" class="mrm" font-size="15">100</text><text x="330.0" y="134" text-anchor="middle" class="label muted">finite</text><rect x="360" y="54" width="60" height="36" class="cell"/><text x="390.0" y="78" text-anchor="middle" class="mrm" font-size="15">101</text><text x="390.0" y="134" text-anchor="middle" class="label">infinite</text><rect x="420" y="54" width="60" height="36" class="cell"/><text x="450.0" y="78" text-anchor="middle" class="mrm" font-size="15">110</text><text x="450.0" y="134" text-anchor="middle" class="label">infinite</text><rect x="480" y="54" width="60" height="36" class="cell"/><text x="510.0" y="78" text-anchor="middle" class="mrm" font-size="15">111</text><text x="510.0" y="134" text-anchor="middle" class="label">infinite</text><text x="270.0" y="42" text-anchor="middle" class="label">least in U</text><line x1="60" y1="148" x2="540" y2="148" class="axis"/><text x="540" y="164" text-anchor="end" class="label">lexicographic order →</text><text x="60" y="190" class="label">bit 0 at a: every string of the tree avoids H(a, ·), so F(a, G) fails;</text><text x="60" y="208" class="label">bit 1 at a: the smaller string with 0 at a and 1 after it is finite, so F(a, G) holds.</text></svg>
:::

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

The lemma proves the main result of this lesson.

:::theorem{#thm-path-induction}
Let $\mathcal M$ be a countable model of $\mathsf{RCA}_0$ and $T \in \mathcal M$ an $\mathcal M$-infinite binary tree. There is a path $G$ through $T$ such that $\mathcal M \cup \{ G \}$ satisfies $\mathsf I\Sigma^0_1$.
:::

:::proof{of=thm-path-induction}
The path $G$ built above from $T$ is a path through $T$, and $\mathcal M \cup \{ G \}$ satisfies $\mathsf I\Sigma^0_1$ by :ref{#lem-harrington-induction}.
:::

## Exercises

::::exercise{difficulty=1}
Let $\mathcal M = (M, \mathcal S)$ be a non-standard model of $\mathsf{RCA}_0$, and $T$ the full binary tree. Show that the set $G = \nat$ of standard numbers is a path through $T$ such that $\mathcal M \cup \{ G \}$ does not satisfy $\mathsf I\Sigma^0_1$.

:::solution
Every string belongs to $T$, so every $G \subseteq M$ is a path through $T$. The bounded formula $x \in G$ holds at $0$, and if $x \in G$ then $x + 1 \in G$, since the successor of a standard number is standard; but it fails at every non-standard number. This is a failure of induction for a bounded formula with parameter $G$, hence of $\mathsf I\Sigma^0_1$. So paths must be chosen with care, which is the purpose of genericity.
:::
::::

::::exercise{difficulty=2}
In the proof of :ref{#lem-harrington-unique}, the tree $S^\sigma$ is defined for each of the strings $\sigma$ of length $n$, where $n$ may be non-standard. Explain why the argument would fail without $\mathsf B\Sigma^0_1$ in $\mathcal M$, and why it does not need $\mathsf B\Sigma^0_1$ when $n$ is standard.

:::solution
If no $S^\sigma$ is $\mathcal M$-infinite, each $\sigma$ has a length $m_\sigma$ at which $S^\sigma$ dies out. To conclude that $S$ dies out, one needs a single length above all the $m_\sigma$, that is, a common bound for a family of witnesses indexed by the $2^n$ strings of length $n$: this is an instance of $\mathsf B\Sigma^0_1$. When $n$ is standard, there are standardly many strings, and the maximum of finitely many witnesses exists without collection.
:::
::::

## Notes and references

The construction is Harrington's (1977, unpublished, communicated by Friedman), as presented by Simpson, Theorem IX.2.1, whose proof is inspired by the Jockusch–Soare proof of the low basis theorem. The presentation with a lexicographically least guess follows Monin and Patey, chapter *Induction and conservation*. Dzhafarov and Mummert, Section 7.7, and Hirschfeldt, Section 7.2, give the same theorem in the language of forcing in non-standard models.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section IX.2.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 7.6–7.7.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 7.2.
