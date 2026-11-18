---
title: Pseudohierarchies and the perfect set theorem
summary: Well-foundedness is not a Σ¹₁ property, provably in ACA₀; consequently every Σ¹₁ property of all well-orderings holds of some ill-founded linear order, which gives pseudohierarchies; the Cantor–Bendixson derivative iterated along well-orderings, and the perfect set theorem for closed sets in ATR₀.
duration: 30
prerequisites: [well-orderings, hyperarithmetic/pseudo-well-orderings]
---

A recursion along a well-ordering always ends. Many proofs in $\mathsf{ATR}_0$ run a recursion whose ending proves the theorem, and must deal with the case where no well-ordering is long enough for it to end. The **method of pseudohierarchies** handles this case: a recursion that does not end along any well-ordering can be run along an ill-founded linear order, and a descending sequence of that order then gives the conclusion. The method rests on one fact: no $\Sigma^1_1$ formula defines the well-orderings. This lesson proves that fact in $\mathsf{ACA}_0$, then applies the method to the perfect set theorem: a closed set is countable or contains a perfect set.

## Well-foundedness is not Σ¹₁

In computability theory, the set of indices of computable well-orderings is $\Pi^1_1$-complete, hence not $\Sigma^1_1$ (:ref{to="computable-ordinals/trees-and-pi11"}). The formal version needs a normal form that is uniform in a set variable. A **code** is a set $A$ of pairs $(\rho, \tau)$ of strings of the same length, $\rho \in \bstr$ and $\tau \in \nat^{<\nat}$. For a set $X$, let $T_A(X)$ be the tree of the strings $\tau$ such that $(X \uh |\tau'|, \tau') \in A$ for every prefix $\tau' \preceq \tau$. It exists by $\Delta^0_1$ comprehension, uniformly in $A$ and $X$.

:::fact[Uniform normal form]{#fact-uniform-normal-form}
For every $\Sigma^1_1$ formula $\varphi(X)$, possibly with other parameters, there is a code $A$, defined from the parameters by a $\Delta^0_1$ formula, such that $\mathsf{ACA}_0$ proves: for every $X$, $\varphi(X)$ holds if and only if $T_A(X)$ has a path.
:::

This is the Kleene normal form of :ref{#fact-kleene-normal-form}, with the set $X$ as an argument instead of a number; the proof is the same, and we admit it (Simpson, Lemma V.1.4 and Theorem V.1.7).

:::theorem{#thm-wo-not-sigma11}
For every $\Sigma^1_1$ formula $\varphi(X)$, $\mathsf{ACA}_0$ proves that it is not the case that, for every $X$, $\varphi(X)$ holds if and only if $\mathrm{WO}(X)$.
:::

**Intuition.** This is a diagonal argument, as in the proof that the halting problem is not computable. If a $\Sigma^1_1$ formula defined the well-orderings, then "$T_X(X)$ has no path", which is $\Pi^1_1$, would be equivalent to a $\Sigma^1_1$ formula; its negation would then have a code by the normal form, and evaluating at that code gives a contradiction.

:::proof{of=thm-wo-not-sigma11}
We argue in $\mathsf{ACA}_0$ and suppose that $\varphi(X) \leftrightarrow \mathrm{WO}(X)$ for every $X$. Let $\psi(X)$ be the formula $\neg \varphi(\mathrm{KB}(T_X(X)))$. It is $\Pi^1_1$, so $\neg \psi$ is equivalent to a $\Sigma^1_1$ formula, and by :ref{#fact-uniform-normal-form} there is a code $A$ with
$$
\neg \psi(X) \iff T_A(X) \text{ has a path}
$$
for every $X$. Take $X = A$. By :ref{#prop-kb-aca} and the hypothesis,
$$
\psi(A) \iff T_A(A) \text{ has no path} \iff \mathrm{WO}(\mathrm{KB}(T_A(A))) \iff \varphi(\mathrm{KB}(T_A(A))) \iff \neg \psi(A),
$$
a contradiction.
:::

:::lemma[Pseudohierarchies]{#lem-pseudohierarchies}
The following is provable in $\mathsf{ACA}_0$. Let $\varphi(X)$ be a $\Sigma^1_1$ formula such that $\varphi(X)$ holds for every well-ordering $X$. Then $\varphi(X)$ holds for some linear order $X$ that is not a well-ordering.
:::

:::proof{of=lem-pseudohierarchies}
Otherwise $\mathrm{LO}(X) \wedge \varphi(X)$, a $\Sigma^1_1$ formula, would be equivalent to $\mathrm{WO}(X)$, contradicting :ref{#thm-wo-not-sigma11}.
:::

The typical use: $\varphi(X)$ says that there is a $\theta$-hierarchy along $X$ with some further $\Sigma^1_1$ property. In $\mathsf{ATR}_0$, hierarchies exist along every well-ordering; by the lemma, there is then such a hierarchy along an ill-founded linear order, a **pseudohierarchy**. Along an ill-founded order the defining equations are still meaningful, but they no longer determine the hierarchy (:ref{#ex-hierarchy-ill-founded}), and the columns along a descending sequence have no first one. In computability terms, this is why $\mathrm{HYP}$ is not a model of $\mathsf{ATR}_0$ (:ref{#prop-hyp-not-atr0}): $\mathrm{HYP}$ sees a computable pseudo-well-ordering as a well-ordering, but no hyperarithmetic set is a jump hierarchy along it.

:::quiz[pseudohierarchies]
In the proof of :ref{#thm-wo-not-sigma11}, why must $\psi$ be evaluated at the code $A$ itself?

- [x] Because this is the diagonal step: $A$ was chosen to describe $\neg \psi$ at every $X$, and at $X = A$ the hypothesis turns this description into $\psi(A)$.
- [ ] Because $T_A(X)$ is defined only for $X = A$.

  $T_A(X)$ is defined for every set $X$.
- [ ] Because $A$ is a well-ordering.

  $A$ is a code, a set of pairs of strings; whether $\mathrm{KB}(T_A(A))$ is a well-ordering is what the argument examines.

---

Why does :ref{#lem-pseudohierarchies} need $\varphi$ to be $\Sigma^1_1$?

- [x] Because the conclusion comes from :ref{#thm-wo-not-sigma11}, which concerns $\Sigma^1_1$ formulas; for $\varphi = \mathrm{WO}$ itself, a $\Pi^1_1$ formula, the conclusion fails.
- [ ] Because $\Sigma^1_1$ formulas are arithmetic.

  They are not: they begin with an existential set quantifier.
- [ ] Because otherwise $\varphi$ would not hold for every well-ordering.

  The hypothesis that $\varphi$ holds for every well-ordering is assumed, whatever its complexity.
:::

## The Cantor–Bendixson derivative

Closed subsets of the Baire space $\bs$ are the sets of paths of trees $T \subseteq \nat^{<\nat}$, and closed subsets of Cantor space those of trees $T \subseteq \bstr$. A tree $P$ is **perfect** if every node has two incompatible extensions in $P$. A non-empty perfect tree has continuum many paths: following the splittings gives an injection of $\cs$ into its set of paths. A tree $T$ has **countably many paths** if there is a sequence $(Y_n)$ such that every path of $T$ is some $Y_n$.

For a tree $S$, let $S'$ be the set of $\sigma \in S$ that have two incompatible extensions in $S$; it is arithmetic in $S$. Removing the other nodes removes, among others, the isolated paths. The **Cantor–Bendixson derivative** iterates this operation: classically, $T_0 = T$, $T_{\alpha+1} = T'_\alpha$, and $T_\lambda = \bigcap_{\alpha < \lambda} T_\alpha$ at limits. Along a countable linear order $X$, the iteration is given by the equations
$$
A_j = \{ \sigma \in T : \sigma \in A'_i \text{ for every } i <_X j \}, \qquad j \in F_X,
$$
which define a $\theta$-hierarchy for an arithmetic $\theta$. In $\mathsf{ATR}_0$, such a hierarchy exists along every well-ordering. The levels decrease: if $i <_X j$, then $A_j \subseteq A'_i \subseteq A_i$.

:::theorem[Perfect set theorem]{#thm-perfect-set-atr}
The following is provable in $\mathsf{ATR}_0$. Every tree $T \subseteq \nat^{<\nat}$ has countably many paths or a non-empty perfect subtree.
:::

**Intuition.** Iterate the derivative. If some level is empty, every path of $T$ was removed at some stage, and at that stage it was the only path through one of its nodes: so the paths are listed by the nodes. If no level is ever empty along a well-ordering, the method of pseudohierarchies gives a derivative sequence along an ill-founded order with all levels non-empty. Along a descending sequence $g(0) >_X g(1) >_X \cdots$, each level is contained in the derivative of the next one, so every node of a level splits in the next: this builds a perfect tree.

:::proof{of=thm-perfect-set-atr}
We argue in $\mathsf{ATR}_0$. Call a **derivative sequence along $X$** a family $(A_j)_{j \in F_X}$ satisfying the equations above.

*Case 1: for some well-ordering $X$, a derivative sequence along $X$ has an empty level $A_k$.* For $\sigma \in T$, there is some $i <_X k$ with $\sigma \notin A'_i$, since $\sigma \notin A_k$; let $i_\sigma$ be the $\leq_X$-least one. Then $\sigma \in A_{i_\sigma}$, since $\sigma \in A'_i$ for all $i <_X i_\sigma$, and $\sigma \notin A'_{i_\sigma}$: no two extensions of $\sigma$ in $A_{i_\sigma}$ are incompatible, so these extensions form a chain. Let $Y_\sigma(n) = \tau(n)$ for an extension $\tau$ of $\sigma$ in $A_{i_\sigma}$ with $|\tau| > n$, if there is one, and $Y_\sigma(n) = 0$ otherwise; the value does not depend on $\tau$, since the extensions form a chain. The sequence $(Y_\sigma)_{\sigma \in T}$ exists by arithmetic comprehension.

Let $Y$ be a path of $T$. The set of $i \in F_X$ such that some prefix of $Y$ is not in $A'_i$ is non-empty, since $Y \uh 0 \notin A_k$; let $i$ be its least element. For $i' <_X i$, every prefix of $Y$ is in $A'_{i'}$, so every prefix of $Y$ is in $A_i$. Let $\sigma = Y \uh m$ be a prefix not in $A'_i$. Then $i_\sigma = i$, and the prefixes $Y \uh n$, $n \geq m$, are extensions of $\sigma$ in $A_i$. Every extension $\tau$ of $\sigma$ in $A_i$ with $|\tau| > n$ is comparable with $Y \uh (n + 1)$, since they form a chain, so $\tau(n) = Y(n)$. Hence $Y_\sigma = Y$. So $T$ has countably many paths.

*Case 2: for every well-ordering $X$, every derivative sequence along $X$ has only non-empty levels.* Let $\varphi(X)$ be the $\Sigma^1_1$ formula: $X$ is a linear order and there is a derivative sequence along $X$ all of whose levels are non-empty. By arithmetic transfinite recursion and the case hypothesis, $\varphi(X)$ holds for every well-ordering $X$. By :ref{#lem-pseudohierarchies}, $\varphi(X)$ holds for some linear order $X$ that is not a well-ordering; fix such an $X$, a derivative sequence $(A_j)$ along $X$ with non-empty levels, and a descending sequence $g$ of $X$ (:ref{#ex-wo-descending}).

Since $g(n + 1) <_X g(n)$, the equations give $A_{g(n)} \subseteq A'_{g(n+1)}$: every node of $A_{g(n)}$ has two incompatible extensions in $A_{g(n+1)}$. Define $\tau_\rho$ for $\rho \in \bstr$ by recursion: $\tau_{\langle\rangle}$ is the least element of $A_{g(0)}$, and if $\tau_\rho \in A_{g(|\rho|)}$, then $\tau_{\rho 0}$ and $\tau_{\rho 1}$ are the first pair of incompatible extensions of $\tau_\rho$ in $A_{g(|\rho| + 1)}$. Let $P$ be the set of $\sigma$ that are prefixes of some $\tau_\rho$; it exists by arithmetic comprehension. It is a subtree of $T$, since every $A_j \subseteq T$; it is non-empty; and every $\sigma \in P$, being a prefix of some $\tau_\rho$, has the two incompatible extensions $\tau_{\rho 0}$ and $\tau_{\rho 1}$ in $P$. So $P$ is a non-empty perfect subtree of $T$.
:::

:::figure[Case 2 of the proof of :ref{#thm-perfect-set-atr}. The node $\tau_\rho$ lies in $A_{g(|\rho|)}$, which is contained in the derivative of $A_{g(|\rho|+1)}$, so it has two incompatible extensions $\tau_{\rho 0}$ and $\tau_{\rho 1}$ there. Along the descending sequence $g$, the splitting never stops.]
<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="A binary splitting: the node tau of the empty string lies in A of g of 0; it has two incompatible extensions tau 0 and tau 1 in A of g of 1, each of which has two incompatible extensions in A of g of 2, and so on. The nodes are joined by paths of the tree, drawn as curves"><path d="M300,52 C300,85 180,75 180,108" class="muted-stroke" fill="none" stroke-width="1.3"/><path d="M300,52 C300,85 420,75 420,108" class="muted-stroke" fill="none" stroke-width="1.3"/><path d="M180,132 C180,165 120,155 120,188" class="muted-stroke" fill="none" stroke-width="1.3"/><path d="M180,132 C180,165 240,155 240,188" class="muted-stroke" fill="none" stroke-width="1.3"/><path d="M420,132 C420,165 360,155 360,188" class="muted-stroke" fill="none" stroke-width="1.3"/><path d="M420,132 C420,165 480,155 480,188" class="muted-stroke" fill="none" stroke-width="1.3"/><circle cx="300" cy="40" r="11" class="node"/><text x="316" y="44" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">⟨⟩</tspan></text><circle cx="180" cy="120" r="11" class="node"/><text x="196" y="124" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><circle cx="420" cy="120" r="11" class="node"/><text x="436" y="124" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><circle cx="120" cy="200" r="11" class="node"/><text x="136" y="204" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">00</tspan></text><circle cx="240" cy="200" r="11" class="node"/><text x="256" y="204" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">01</tspan></text><circle cx="360" cy="200" r="11" class="node"/><text x="376" y="204" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">10</tspan></text><circle cx="480" cy="200" r="11" class="node"/><text x="496" y="204" class="math" font-size="14">τ<tspan class="mrm" font-size="10" dy="4">11</tspan></text><text x="590" y="44" text-anchor="end" class="label">in A_g(0)</text><text x="590" y="124" text-anchor="end" class="label">in A_g(1)</text><text x="590" y="204" text-anchor="end" class="label">in A_g(2)</text><line x1="120" y1="214" x2="120" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="240" y1="214" x2="240" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="360" y1="214" x2="360" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="480" y1="214" x2="480" y2="236" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="300" y="260" text-anchor="middle" class="label">each node of level d lies in A_g(d) ⊆ A′_g(d+1), so it splits inside A_g(d+1)</text></svg>
:::

:::quiz[the proof of the perfect set theorem]
In Case 2, why is a descending sequence of $X$ needed?

- [x] Because the splitting at level $n$ must happen inside a later level of the derivative, and the inclusion $A_{g(n)} \subseteq A'_{g(n+1)}$ holds when $g(n+1)$ is below $g(n)$; an infinite splitting needs infinitely many levels each below the previous one.
- [ ] Because a well-ordering has no levels.

  A derivative sequence along a well-ordering has levels; under the case hypothesis they are non-empty, but along an increasing sequence of indices each level is contained in the derivative of the earlier ones, not of the later ones.
- [ ] To make $P$ exist by arithmetic comprehension.

  $P$ exists once the nodes $\tau_\rho$ are defined; the descending sequence is what makes them definable.

---

In Case 1, why do the extensions of $\sigma$ in $A_{i_\sigma}$ form a chain?

- [x] Because $\sigma \in A_{i_\sigma}$ but $\sigma \notin A'_{i_\sigma}$: by the definition of the derivative, $\sigma$ has no two incompatible extensions in $A_{i_\sigma}$.
- [ ] Because $A_{i_\sigma}$ is a chain.

  $A_{i_\sigma}$ may contain many incompatible nodes; only the extensions of $\sigma$ are comparable.
- [ ] Because $T$ has countably many paths.

  This is what is being proved.
:::

The theorem is the closed case of the perfect set theorem for analytic sets, which $\mathsf{ATR}_0$ also proves (Simpson, Theorem V.4.3), by the same two cases applied to codes. In the lesson on unique paths, we show that the perfect set theorem for closed sets implies $\mathsf{ATR}_0$ over $\mathsf{ACA}_0$. The full Cantor–Bendixson theorem, which says moreover that the set of nodes of $T$ lying in no perfect subtree, the **perfect kernel**, exists, is stronger: it is equivalent to $\Pi^1_1\text{-}\mathsf{CA}_0$ (Simpson, Theorem VI.1.6).

::::exercise{#ex-derivative-example difficulty=1 objective="Compute the derivative sequence of a countable closed set, and see that infinitely many paths do not give a perfect subtree."}
Let $T$ be the tree of the strings $0^n$ and $0^n 1 0^m$, for $n, m \in \nat$.

1. Describe the paths of $T$.
2. Compute $T'$ and $T''$.
3. Show that $T$ has no non-empty perfect subtree, although it has infinitely many paths. For a path $Y$, give a node $\sigma$ and a level such that $Y = Y_\sigma$ in the notation of Case 1.

:::solution
1. The paths are $0^\omega$ and $0^n 1 0^\omega$ for each $n$: countably many.
2. A node $0^n$ has the incompatible extensions $0^{n+1}$ and $0^n 1$, so $0^n \in T'$. A node $0^n 1 0^m$ has only the extensions $0^n 1 0^{m'}$, $m' \geq m$, which form a chain; it is not in $T'$. So $T' = \{ 0^n : n \in \nat \}$, a single branch, and $T'' = \emptyset$.
3. A perfect subtree $P$ would satisfy $P \subseteq P'$, hence $P \subseteq T'$ and then $P \subseteq T''= \emptyset$. For $Y = 0^n 1 0^\omega$, take $\sigma = 0^n 1$ at level $0$: $\sigma \in T$, $\sigma \notin T'$, and its extensions form the chain of prefixes of $Y$. For $Y = 0^\omega$, take $\sigma = \langle\rangle$ at level $1$: $\sigma \in T'$, $\sigma \notin T''$, and its extensions in $T'$ are the prefixes of $0^\omega$.
:::
::::

## Notes and references

:ref{#thm-wo-not-sigma11} is the formal version of a theorem of Lusin and Sierpiński: the set of codes of countable well-orderings is not analytic. In $\mathsf{ACA}_0$ it is Simpson, Theorem V.1.9, and the method of pseudohierarchies is his Lemma V.4.12; pseudohierarchies were introduced by Spector and Gandy in hyperarithmetic theory, and studied by Harrison (1968). The proof of :ref{#thm-perfect-set-atr} specializes Simpson's proof of Theorem V.4.3 from analytic codes to trees.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.1, V.4 and VI.1.
- J. Harrison, *Recursive pseudo-well-orderings*, Transactions of the American Mathematical Society 131 (1968), 526–543.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Sections 6 and 27 (the classical Cantor–Bendixson and Lusin–Sierpiński theorems).

:::::exercises
::::exercise{#ex-pseudo-jump-hierarchy difficulty=1 objective="Apply the method of pseudohierarchies to jump hierarchies."}
Show in $\mathsf{ATR}_0$ that there is a linear order $X$ that is not a well-ordering, and a jump hierarchy along $X$: a set $H$ with $H^{[j]} = (H^{[<j]})'$ for every $j \in F_X$.

:::solution
Let $\theta(n, j, Y) \equiv \Phi^Y_n(n)\converge$, an arithmetic formula, and $\varphi(X)$ the $\Sigma^1_1$ formula "there is a $\theta$-hierarchy along $X$". By arithmetic transfinite recursion, $\varphi(X)$ holds for every well-ordering $X$. By :ref{#lem-pseudohierarchies}, it holds for some ill-founded linear order $X$.
:::
::::

::::exercise{#ex-perfect-tree-continuum difficulty=1 objective="Show that a non-empty perfect tree has uncountably many paths, by diagonalization against a given sequence."}
Show in $\mathsf{ACA}_0$ that if $P \subseteq \nat^{<\nat}$ is a non-empty perfect tree and $(Y_n)$ is a sequence of sets, then $P$ has a path different from every $Y_n$.

:::solution
Define $\tau_0$ as the least element of $P$, and $\tau_{n+1}$ as follows: $\tau_n$ has two incompatible extensions in $P$; at least one of them, say $\tau$, is not a prefix of $Y_n$, since two incompatible strings cannot both be prefixes of $Y_n$; let $\tau_{n+1}$ be the first such $\tau$ in a fixed enumeration. The sequence is defined by recursion with searches that terminate, relative to $P$ and $(Y_n)$, and $\tau_{n+1}$ properly extends $\tau_n$. Let $Y$ be the union. Every prefix of $Y$ is a prefix of some $\tau_n \in P$, so $Y$ is a path of $P$. And $Y \neq Y_n$, since $\tau_{n+1} \prec Y$ is not a prefix of $Y_n$.
:::
::::

::::exercise{#ex-derivative-rank difficulty=2 objective="Compute the length of the derivative sequence of a tree whose paths form a closed set of Cantor–Bendixson rank ω."}
For each $k$, let $S_k$ be the tree of the strings $0^{n_1} 1 0^{n_2} 1 \cdots 1 0^{n_j}$ and $0^{n_1} 1 \cdots 0^{n_j} 1$ with $j \leq k$ (at most $k$ ones). Let $T$ be the tree of the strings $1^k 0 \sigma$ with $\sigma \in S_k$, together with the strings $1^k$, for all $k$.

1. Show that $S'_k = S_{k-1}$ for $k \geq 1$, with $S_0 = \{ 0^n \}$ and $S'_0 = \emptyset$, where the derivative of $S_k$ is computed in $S_k$.
2. Deduce that the finite levels $T_n$ of the derivative of $T$ are all non-empty, that $T_\omega = \{ 1^k : k \in \nat \}$, and $T_{\omega + 1} = \emptyset$.

:::solution
1. A node of $S_k$ with fewer than $k$ ones can be extended by adding $0$ or by adding $1$, and both extensions are in $S_k$: it splits. A node with exactly $k$ ones has only extensions by zeros: it does not split. So $S'_k$ consists of the nodes with fewer than $k$ ones, which is $S_{k-1}$ as a set of strings. For $k = 0$, $S_0$ is the single branch of zeros, with no splitting node.
2. Inside $T$, the part above $1^k 0$ is a copy of $S_k$, and the derivative acts on it as on $S_k$, since a node above $1^k 0$ has the same extensions in $T$ as in the copy. A node $1^k$ has the incompatible extensions $1^m 0$ and $1^{m+1} 0$ for every $m \geq k$; so it stays in every finite level as long as, for infinitely many $m$, the copy above $1^m 0$ is non-empty, which holds at every finite level. By part 1, after $n$ derivatives the copy of $S_k$ becomes the copy of $S_{k-n}$ if $n \leq k$, and is empty after $k + 1$ derivatives. So $T_n$ contains the copies of $S_{k-n}$ for $k \geq n$: non-empty. $T_\omega = \bigcap_n T_n$ contains no node above any $1^k 0$, since the copy of $S_k$ is gone after $k + 1$ steps; it is $\{ 1^k \}$, a single branch, and $T_{\omega + 1} = \emptyset$.
:::
::::
:::::
