---
title: Computably dominated degrees
summary: Sets all of whose functions are dominated by computable functions; a construction by forcing with computable function trees; the characterization of computably dominated sets by the coincidence of Turing and truth-table reducibility below them.
duration: 50
prerequisites: [hypersimple-sets, pi01-classes/basis-theorems]
---

A set is **computably dominated** (:ref{#def-computably-dominated}), or **hyperimmune-free**, if every function it computes is dominated by a computable function. By :ref{#def-hyperimmune-fn}, these are exactly the sets that are not of hyperimmune degree. Being computably dominated is closed downward under Turing reducibility: if $Y \leq_T X$, every $Y$-computable function is $X$-computable. Computable sets are computably dominated, and the computably dominated basis theorem (:ref{#thm-dominated-basis}) gives non-computable examples inside every $\Pi^0_1$ class without computable members.

This lesson gives a second construction, which does not use $\Pi^0_1$ classes, and then shows that below a computably dominated set, Turing reducibility coincides with truth-table reducibility (:ref{#def-tt}).

The construction cannot use finite extensions. A set built by finite extensions with the help of $\emptyset'$ is $\Delta^0_2$, and no non-computable $\Delta^0_2$ set is computably dominated (:ref{#thm-computation-function}). To make $\Phi^X_e$ dominated, a construction must either make it partial, or know a computable bound on all its values; a single string $\sigma \prec X$ cannot provide such a bound, since the values depend on the bits of $X$ not yet chosen. The solution, due to Spector for minimal degrees and adapted by Miller and Martin, is to keep a computable perfect set of candidates, given by a tree, and to shrink it step by step. On a well-chosen tree, every candidate computes values below a common computable bound.

## Function trees

:::definition{#def-function-tree}
A **function tree**, or **f-tree**, is a total function $T : \bstr \to \bstr$ such that for all strings $\rho, \mu$,
$$
\rho \preceq \mu \iff T(\rho) \preceq T(\mu).
$$
The strings $T(\rho)$ are the **nodes** of $T$. A set $X$ is a **path** of $T$ if infinitely many prefixes of $X$ are nodes of $T$; $[T]$ denotes the class of paths. An f-tree $S$ is a **subtree** of $T$ if every node of $S$ is a node of $T$.
:::

For every $\rho$, the nodes $T(\rho 0)$ and $T(\rho 1)$ strictly extend $T(\rho)$ (they extend it since $\rho \preceq \rho i$, and differ from it since $\rho i \not\preceq \rho$) and are incompatible: neither $\rho 0 \preceq \rho 1$ nor $\rho 1 \preceq \rho 0$, so neither node extends the other. If $S$ is a subtree of $T$, then $[S] \subseteq [T]$, directly from the definition of paths. For every $\rho$, the function $\mu \mapsto T(\rho \mu)$ is a subtree of $T$, computable if $T$ is, whose nodes all extend $T(\rho)$; we call it the **full subtree above** $T(\rho)$.

If $X \in [T]$ and $T(\rho_1) \prec T(\rho_2) \prec \cdots$ are the nodes of $T$ that are prefixes of $X$, then $\rho_1 \prec \rho_2 \prec \cdots$ by the definition (the inclusions are strict since $T$ is injective: $T(\rho) = T(\mu)$ gives $\rho \preceq \mu$ and $\mu \preceq \rho$). So for every $n$, if $\rho_i$ has length at least $n$ and $\rho$ is its prefix of length $n$, then $T(\rho) \preceq T(\rho_i) \prec X$. The identity $T(\rho) = \rho$ is a computable f-tree whose paths are all sets.

:::example{#ex-ftree}
For a set $Z$, let $T_Z(\rho)$ be the string of length $2|\rho|$ that interleaves $\rho$ with $Z$: $T_Z(\rho)(2i) = \rho(i)$ and $T_Z(\rho)(2i + 1) = Z(i)$ for $i < |\rho|$. It is an f-tree, computable if $Z$ is, and its paths are the sets $X \oplus Z$. Every path computes $Z$: an f-tree can constrain all its paths at once. The figure shows a less regular f-tree, in which the nodes $T(\rho 0)$ and $T(\rho 1)$ branch off at different heights above $T(\rho)$.
:::

:::figure[An f-tree $T$ inside the full binary tree, up to its nodes $T(\rho)$ with $|\rho| \leq 2$. Each node is a string; the thick edges are the prefixes of the nodes. The two successors $T(\rho 0)$ and $T(\rho 1)$ of a node are incompatible extensions of it, so the paths of $T$ form a perfect class, in bijection with $\cs$.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="An f-tree: the nodes T(rho) are strings placed in the full binary tree; T(rho 0) and T(rho 1) are incompatible extensions of T(rho)"><line x1="300.0" y1="30" x2="160.0" y2="74" class="accent-stroke" stroke-width="2"/><line x1="300.0" y1="30" x2="440.0" y2="74" class="accent-stroke" stroke-width="2"/><line x1="160.0" y1="74" x2="90.0" y2="118" class="accent-stroke" stroke-width="2"/><line x1="160.0" y1="74" x2="230.0" y2="118" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="74" x2="370.0" y2="118" class="accent-stroke" stroke-width="2"/><line x1="440.0" y1="74" x2="510.0" y2="118" class="muted-stroke" stroke-width="0.8"/><line x1="90.0" y1="118" x2="55.0" y2="162" class="muted-stroke" stroke-width="0.8"/><line x1="90.0" y1="118" x2="125.0" y2="162" class="accent-stroke" stroke-width="2"/><line x1="230.0" y1="118" x2="195.0" y2="162" class="muted-stroke" stroke-width="0.8"/><line x1="230.0" y1="118" x2="265.0" y2="162" class="muted-stroke" stroke-width="0.8"/><line x1="370.0" y1="118" x2="335.0" y2="162" class="muted-stroke" stroke-width="0.8"/><line x1="370.0" y1="118" x2="405.0" y2="162" class="accent-stroke" stroke-width="2"/><line x1="510.0" y1="118" x2="475.0" y2="162" class="muted-stroke" stroke-width="0.8"/><line x1="510.0" y1="118" x2="545.0" y2="162" class="muted-stroke" stroke-width="0.8"/><line x1="55.0" y1="162" x2="37.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="55.0" y1="162" x2="72.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="125.0" y1="162" x2="107.5" y2="206" class="accent-stroke" stroke-width="2"/><line x1="125.0" y1="162" x2="142.5" y2="206" class="accent-stroke" stroke-width="2"/><line x1="195.0" y1="162" x2="177.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="195.0" y1="162" x2="212.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="265.0" y1="162" x2="247.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="265.0" y1="162" x2="282.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="335.0" y1="162" x2="317.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="335.0" y1="162" x2="352.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="405.0" y1="162" x2="387.5" y2="206" class="accent-stroke" stroke-width="2"/><line x1="405.0" y1="162" x2="422.5" y2="206" class="accent-stroke" stroke-width="2"/><line x1="475.0" y1="162" x2="457.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="475.0" y1="162" x2="492.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="545.0" y1="162" x2="527.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="545.0" y1="162" x2="562.5" y2="206" class="muted-stroke" stroke-width="0.8"/><line x1="37.5" y1="206" x2="28.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="37.5" y1="206" x2="46.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="72.5" y1="206" x2="63.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="72.5" y1="206" x2="81.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="107.5" y1="206" x2="98.8" y2="250" class="accent-stroke" stroke-width="2"/><line x1="107.5" y1="206" x2="116.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="142.5" y1="206" x2="133.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="142.5" y1="206" x2="151.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="177.5" y1="206" x2="168.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="177.5" y1="206" x2="186.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="212.5" y1="206" x2="203.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="212.5" y1="206" x2="221.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="247.5" y1="206" x2="238.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="247.5" y1="206" x2="256.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="282.5" y1="206" x2="273.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="282.5" y1="206" x2="291.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="317.5" y1="206" x2="308.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="317.5" y1="206" x2="326.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="352.5" y1="206" x2="343.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="352.5" y1="206" x2="361.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="387.5" y1="206" x2="378.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="387.5" y1="206" x2="396.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="422.5" y1="206" x2="413.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="422.5" y1="206" x2="431.2" y2="250" class="accent-stroke" stroke-width="2"/><line x1="457.5" y1="206" x2="448.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="457.5" y1="206" x2="466.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="492.5" y1="206" x2="483.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="492.5" y1="206" x2="501.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="527.5" y1="206" x2="518.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="527.5" y1="206" x2="536.2" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="562.5" y1="206" x2="553.8" y2="250" class="muted-stroke" stroke-width="0.8"/><line x1="562.5" y1="206" x2="571.2" y2="250" class="muted-stroke" stroke-width="0.8"/><circle cx="160.0" cy="74" r="2" class="muted-fill"/><circle cx="440.0" cy="74" r="2" class="muted-fill"/><circle cx="90.0" cy="118" r="2" class="muted-fill"/><circle cx="230.0" cy="118" r="2" class="muted-fill"/><circle cx="510.0" cy="118" r="2" class="muted-fill"/><circle cx="55.0" cy="162" r="2" class="muted-fill"/><circle cx="195.0" cy="162" r="2" class="muted-fill"/><circle cx="265.0" cy="162" r="2" class="muted-fill"/><circle cx="335.0" cy="162" r="2" class="muted-fill"/><circle cx="405.0" cy="162" r="2" class="muted-fill"/><circle cx="475.0" cy="162" r="2" class="muted-fill"/><circle cx="545.0" cy="162" r="2" class="muted-fill"/><circle cx="37.5" cy="206" r="2" class="muted-fill"/><circle cx="72.5" cy="206" r="2" class="muted-fill"/><circle cx="107.5" cy="206" r="2" class="muted-fill"/><circle cx="177.5" cy="206" r="2" class="muted-fill"/><circle cx="212.5" cy="206" r="2" class="muted-fill"/><circle cx="247.5" cy="206" r="2" class="muted-fill"/><circle cx="282.5" cy="206" r="2" class="muted-fill"/><circle cx="317.5" cy="206" r="2" class="muted-fill"/><circle cx="352.5" cy="206" r="2" class="muted-fill"/><circle cx="422.5" cy="206" r="2" class="muted-fill"/><circle cx="457.5" cy="206" r="2" class="muted-fill"/><circle cx="492.5" cy="206" r="2" class="muted-fill"/><circle cx="527.5" cy="206" r="2" class="muted-fill"/><circle cx="562.5" cy="206" r="2" class="muted-fill"/><circle cx="28.8" cy="250" r="2" class="muted-fill"/><circle cx="46.2" cy="250" r="2" class="muted-fill"/><circle cx="63.8" cy="250" r="2" class="muted-fill"/><circle cx="81.2" cy="250" r="2" class="muted-fill"/><circle cx="116.2" cy="250" r="2" class="muted-fill"/><circle cx="133.8" cy="250" r="2" class="muted-fill"/><circle cx="151.2" cy="250" r="2" class="muted-fill"/><circle cx="168.8" cy="250" r="2" class="muted-fill"/><circle cx="186.2" cy="250" r="2" class="muted-fill"/><circle cx="203.8" cy="250" r="2" class="muted-fill"/><circle cx="221.2" cy="250" r="2" class="muted-fill"/><circle cx="238.8" cy="250" r="2" class="muted-fill"/><circle cx="256.2" cy="250" r="2" class="muted-fill"/><circle cx="273.8" cy="250" r="2" class="muted-fill"/><circle cx="291.2" cy="250" r="2" class="muted-fill"/><circle cx="308.8" cy="250" r="2" class="muted-fill"/><circle cx="326.2" cy="250" r="2" class="muted-fill"/><circle cx="343.8" cy="250" r="2" class="muted-fill"/><circle cx="361.2" cy="250" r="2" class="muted-fill"/><circle cx="378.8" cy="250" r="2" class="muted-fill"/><circle cx="396.2" cy="250" r="2" class="muted-fill"/><circle cx="413.8" cy="250" r="2" class="muted-fill"/><circle cx="448.8" cy="250" r="2" class="muted-fill"/><circle cx="466.2" cy="250" r="2" class="muted-fill"/><circle cx="483.8" cy="250" r="2" class="muted-fill"/><circle cx="501.2" cy="250" r="2" class="muted-fill"/><circle cx="518.8" cy="250" r="2" class="muted-fill"/><circle cx="536.2" cy="250" r="2" class="muted-fill"/><circle cx="553.8" cy="250" r="2" class="muted-fill"/><circle cx="571.2" cy="250" r="2" class="muted-fill"/><circle cx="300.0" cy="30" r="5.5" class="node"/><text x="310.0" y="34" class="math" font-size="13">T<tspan class="mrm">(ε) = ε</tspan></text><circle cx="125.0" cy="162" r="5.5" class="node"/><text x="135.0" y="166" class="math" font-size="13">T<tspan class="mrm">(0) = 001</tspan></text><circle cx="370.0" cy="118" r="5.5" class="node"/><text x="380.0" y="122" class="math" font-size="13">T<tspan class="mrm">(1) = 10</tspan></text><circle cx="98.8" cy="250" r="5.5" class="node"/><text x="108.8" y="254" class="math" font-size="13">T<tspan class="mrm">(00) = 00100</tspan></text><circle cx="142.5" cy="206" r="5.5" class="node"/><text x="152.5" y="210" class="math" font-size="13">T<tspan class="mrm">(01) = 0011</tspan></text><circle cx="387.5" cy="206" r="5.5" class="node"/><text x="397.5" y="210" class="math" font-size="13">T<tspan class="mrm">(10) = 1010</tspan></text><circle cx="431.2" cy="250" r="5.5" class="node"/><text x="441.2" y="254" class="math" font-size="13">T<tspan class="mrm">(11) = 10111</tspan></text><line x1="24" y1="290" x2="44" y2="290" class="accent-stroke" stroke-width="2"/><text x="50" y="294" class="label">prefixes of the nodes of T</text><circle cx="250" cy="290" r="5.5" class="node"/><text x="262" y="294" class="label">a node of T</text></svg>
:::

The construction shrinks a computable f-tree step by step, each step meeting one requirement for all the paths of the new tree at once. Making the paths non-computable is easy, since the two subtrees above $T(0)$ and $T(1)$ disagree somewhere.

:::lemma{#lem-ftree-noncomputable}
Let $T$ be a computable f-tree and $e \in \nat$. There is a computable subtree $S$ of $T$ such that $\Phi_e \neq X$ for every $X \in [S]$.
:::

:::proof{of=lem-ftree-noncomputable}
The nodes $T(0)$ and $T(1)$ are incompatible, so they differ at some position $i$. If $\Phi_e(i)\converge = T(0)(i)$, let $S$ be the full subtree above $T(1)$; otherwise, the full subtree above $T(0)$. In the first case, every $X \in [S]$ extends $T(1)$, so $X(i) = T(1)(i) \neq \Phi_e(i)$. In the second case, every $X \in [S]$ has $X(i) = T(0)(i)$, which differs from $\Phi_e(i)$ or $\Phi_e(i)$ diverges.
:::

The subtree is computable, but the choice between the two cases is not effective: the lemma asserts existence, not a uniform procedure.

Domination requires a dichotomy. Either some node forces $\Phi^X_e$ to be partial for all paths above it, or every node has extensions on which each computation converges. In the second case, a computable search builds a subtree on which the computation at $n$ already converges at every node of level $n$; since there are only $2^n$ such nodes, the largest of their values is a computable bound. This is the method of **forcing with computable perfect trees**: a node decides a property of all paths through the tree above it, as a string decides a property of all its extensions in the finite extension method.

:::lemma{#lem-ftree-domination}
Let $T$ be a computable f-tree and $e \in \nat$. There is a computable subtree $S$ of $T$ such that either $\Phi^X_e$ is partial for every $X \in [S]$, or there is a computable function $g$ that dominates $\Phi^X_e$ for every $X \in [S]$.
:::

:::proof{of=lem-ftree-domination}
*Case 1: there are a node $\sigma = T(\rho)$ and an input $x$ such that $\Phi^\tau_e(x)\diverge$ for every node $\tau \succeq \sigma$ of $T$.* Let $S$ be the full subtree above $\sigma$. If $X \in [S]$ had $\Phi^X_e(x)\converge$, with use $u$, then a node $\tau$ of $S$ that is a prefix of $X$ of length at least $u$ would satisfy $\Phi^\tau_e(x)\converge$, and $\tau \succeq \sigma$ is a node of $T$. So $\Phi^X_e(x)\diverge$ for all $X \in [S]$.

*Case 2: for every node $\sigma$ of $T$ and every input $x$, there is a node $\tau \succeq \sigma$ of $T$ with $\Phi^\tau_e(x)\converge$.* Define $S(\rho) = T(\mu_\rho)$ by induction on $\rho$. Let $\mu_\varepsilon$ be the first string found, in a computable search, with $\Phi^{T(\mu_\varepsilon)}_e(0)\converge$. Given $\mu_\rho$, for $i \in \{0, 1\}$, let $\mu_{\rho i}$ be the first string $\mu \succeq \mu_\rho\, i$ found with $\Phi^{T(\mu)}_e(|\rho| + 1)\converge$. The searches terminate by the hypothesis of Case 2, applied to the nodes $T(\varepsilon)$ and $T(\mu_\rho\, i)$, and the nodes $\tau \succeq T(\mu_\rho\, i)$ of $T$ are of the form $T(\mu)$ with $\mu \succeq \mu_\rho\, i$. So $S$ is computable. Since $\mu_{\rho i} \succeq \mu_\rho\, i$, the map $\rho \mapsto \mu_\rho$ preserves both the prefix relation and incompatibility, so $S$ is an f-tree, and it is a subtree of $T$.

By construction, $\Phi^{S(\rho)}_e(|\rho|)\converge$ for every $\rho$. Let $g(n) = \max \{ \Phi^{S(\rho)}_e(n) : |\rho| = n \}$, a computable function. Let $X \in [S]$ and $n \in \nat$. Some $\rho$ of length $n$ has $S(\rho) \prec X$, so $\Phi^X_e(n) = \Phi^{S(\rho)}_e(n) \leq g(n)$. Hence $\Phi^X_e$ is total and dominated by $g$.
:::

:::theorem[Miller–Martin]{#thm-martin-miller-ftrees}
There is a non-computable computably dominated set. Moreover, it can be taken computable in $\emptyset''$.
:::

:::proof{of=thm-martin-miller-ftrees}
Build computable f-trees $T_0, T_1, \dots$, each a subtree of the previous one. Let $T_0$ be the identity. Given $T_{2e}$, let $T_{2e+1}$ be given by :ref{#lem-ftree-noncomputable} for $T_{2e}$ and $e$. Given $T_{2e+1}$, let $T'$ be given by :ref{#lem-ftree-domination} for $T_{2e+1}$ and $e$, and let $T_{2e+2}$ be the full subtree of $T'$ above $T'(0)$. Each step replaces the tree by a subtree whose root $T_{k+1}(\varepsilon)$ strictly extends $T_k(\varepsilon)$: this holds for the full subtrees used at the odd steps, and is enforced at the even steps by passing to $T'(0)$.

The roots form a chain $T_0(\varepsilon) \prec T_1(\varepsilon) \prec \cdots$ of increasing lengths; let $X$ be their union. For each $k$, the roots $T_j(\varepsilon)$, $j \geq k$, are nodes of $T_k$ and prefixes of $X$, so $X \in [T_k]$. Since $X \in [T_{2e+1}]$, $X \neq \Phi_e$; so $X$ is not computable. Since $X \in [T_{2e+2}] \subseteq [T']$, either $\Phi^X_e$ is partial or it is dominated by a computable function. So $X$ is computably dominated.

For the bound, the construction makes two kinds of choices. At odd steps, it asks whether $\Phi_e(i)\converge = T(0)(i)$, a $\Sigma^0_1$ question. At even steps, it asks whether Case 1 holds, a $\Sigma^0_2$ question about an index of the computable tree; if so, a witness $(\rho, x)$ is found with $\emptyset''$ by asking, for each candidate, the $\Pi^0_1$ question that defines Case 1. Each new tree is then computable from these answers, uniformly. So the sequence of indices of the trees, and $X$, are computable in $\emptyset''$.
:::

The technique of f-trees is due to Spector, who used it to construct a minimal degree; it is used again in the course on the structure of the Turing degrees (:ref{to="degree-structure/minimal-degrees"}). The bound $\emptyset''$ is optimal: no non-computable $\Delta^0_2$ set is computably dominated. The two constructions of computably dominated sets, by $\Pi^0_1$ classes and by f-trees, follow the same pattern: a closed set of candidates is shrunk so that each functional becomes either partial on all candidates, or total on all of them, and compactness then gives a computable bound.

:::quiz[function trees]
In Case 2 of :ref{#lem-ftree-domination}, why does the computable function $g$ dominate $\Phi^X_e$ for **every** path $X$ of $S$?

- [x] Because each path extends some node $S(\rho)$ with $|\rho| = n$, on which the computation at $n$ already converges, and $g(n)$ is the maximum over the finitely many such nodes.
- [ ] Because $\Phi^X_e$ is total for every set $X$.

  Totality is only obtained for the paths of $S$, and it is a consequence of the construction, not an assumption.
- [ ] Because $g$ grows faster than every computable function.

  No computable function grows faster than every computable function; $g$ is tailored to $\Phi_e$ and $S$.

---

Why is Case 1 handled by a full subtree, rather than by a subtree built by search?

- [x] Because Case 1 provides a single node above which no node of $T$ makes the computation at $x$ converge; the full subtree above it inherits this property, and no search is needed.
- [ ] Because Case 1 is decidable.

  It is a $\Sigma^0_2$ property of the tree, not decidable in general.
- [ ] Because in Case 1 the functional $\Phi_e$ is partial with every oracle.

  Only the oracles in the subtree are concerned; other oracles may make $\Phi_e$ total.
:::

## Truth-table reducibility below computably dominated sets

By :ref{#prop-tt-total}, a truth-table reduction is a Turing reduction with a computable bound on its use and running time. For a general Turing reduction $\Phi^X_e = Y$, the time needed to compute $Y(n)$ is an $X$-computable function of $n$. If $X$ is computably dominated, this function is dominated by a computable one, and the reduction can be turned into a truth-table reduction. Conversely, a set that computes a function escaping every computable bound can diagonalize against all truth-table reductions, each of which has a computable running time. This is the content of the next theorem.

:::theorem[Jockusch, Martin]{#thm-dominated-tt}
A set $X$ is computably dominated if and only if $Y \leq_T X$ implies $Y \leq_{tt} X$ for every set $Y$.
:::

:::proof{of=thm-dominated-tt}
($\Rightarrow$) Let $Y = \Phi^X_e$, and let $t(n)$ be the least $s$ such that $\Phi^{X \uh s}_e(n)[s]\converge$. It is an $X$-computable total function, so a computable function $g$ dominates it. Let $\ell = g$ and let $\theta(n)(\sigma) = \Phi^\sigma_e(n)[g(n)]$ for $|\sigma| = g(n)$, replaced by $0$ if it diverges or is not in $\{0, 1\}$. Since $t(n) \leq g(n)$, the computation with oracle $X \uh g(n)$ converges within $g(n)$ steps to $Y(n)$, so $Y(n) = \theta(n)(X \uh g(n))$.

($\Leftarrow$) Suppose that $X$ is not computably dominated, and let $f \leq_T X$ be a function dominated by no computable function. Let $F(n) = \max_{m \leq n} f(m)$. Fix an enumeration of the pairs $(\ell_e, \theta_e)$ of partial computable functions. Define $Y$ on inputs $n = \langle e, k \rangle$ as follows. If $\ell_e(n)$ and $\theta_e(n)$ converge within $F(n)$ steps, and $\theta_e(n)$ codes a function on $\{0, 1\}^{\ell_e(n)}$, let $Y(n) = 1 - \theta_e(n)(X \uh \ell_e(n))$; otherwise let $Y(n) = 0$.
Then $Y \leq_T X$. Suppose $Y \leq_{tt} X$ via total $(\ell_e, \theta_e)$. Let $c(n)$ be the number of steps after which both $\ell_e(n)$ and $\theta_e(n)$ have converged; $c$ is computable. If $F(\langle e, k \rangle) \geq c(\langle e, k \rangle)$ for some $k$, then $Y(\langle e, k \rangle) = 1 - \theta_e(\langle e, k \rangle)(X \uh \ell_e(\langle e, k \rangle))$, contradicting the reduction. So $F(\langle e, k \rangle) < c(\langle e, k \rangle)$ for every $k$. For each $m$, let $k(m)$ be the least $k$ with $\langle e, k \rangle \geq m$, and $G(m) = c(\langle e, k(m) \rangle)$. Then $G$ is computable and $G(m) > F(\langle e, k(m) \rangle) \geq f(m)$ for every $m$, so $G$ dominates $f$, a contradiction.
:::

The theorem gives the separation of $\leq_{tt}$ and $\leq_T$ announced in :ref{to="immunity-growth/hypersimple-sets"}, with a complete proof: $\emptyset'$ is not computably dominated, so some $Y \leq_T \emptyset'$ satisfies $Y \not\leq_{tt} \emptyset'$. The set $Y$ of the proof is $\Delta^0_2$; Post's theorem on hypersimple sets gives a c.e. example.

Below a computably dominated set, every Turing reduction can be replaced by a reduction that reads a computably bounded amount of the oracle within a computably bounded time. This makes computably dominated sets behave, for many purposes, like compact objects; for instance, a computably dominated set that computes a DNC function computes one bounded by a computable function, since the DNC function itself is dominated.

:::quiz[truth-table reducibility]
In the proof of ($\Rightarrow$) in :ref{#thm-dominated-tt}, why is the hypothesis applied to the function $t$, and not to $Y$?

- [x] Because $t$ bounds both the time and the use of the computation of $Y(n)$, which is what a truth table needs; $Y$ is $\{0, 1\}$-valued and trivially dominated.
- [ ] Because $t$ is computable.

  $t$ is only $X$-computable; it is dominated by a computable function by hypothesis.
- [ ] Because $Y$ may not be total.

  $Y$ is a set, so its characteristic function is total.
:::

## Exercises

::::exercise{difficulty=1}
Show that a computably dominated set computable in $\emptyset'$ is computable, and that a computably dominated set computes no non-computable c.e. set.

:::solution
A non-computable $\Delta^0_2$ set computes its computation function, which no computable function dominates (:ref{#thm-computation-function}); so it is not computably dominated. If $X$ is computably dominated and $Y \leq_T X$, then $Y$ is computably dominated, by downward closure. A non-computable c.e. set $Y$ is $\Delta^0_2$, hence not computably dominated; so $X$ computes none.
:::
::::

::::exercise{difficulty=2}
Show that there are continuum many non-computable computably dominated sets.

:::solution
Fix, for each computable f-tree and each $e$, the subtree given by the proofs of :ref{#lem-ftree-noncomputable} and :ref{#lem-ftree-domination}, choosing the least witness in Case 1, so that the subtree is determined by the tree and $e$. Modify the construction of :ref{#thm-martin-miller-ftrees}: for $Z \in \cs$, build the trees $T^Z_k$ as before, except that at each step $k$, after applying the lemma, pass to the full subtree above the node $T(Z(k))$ of the tree $T$ obtained, rather than above a fixed node. Let $X_Z$ be the union of the roots. As before, $X_Z$ is non-computable and computably dominated. If $Z$ and $Z'$ first differ at position $k$, then the trees coincide up to step $k$, and $X_Z$, $X_{Z'}$ extend the nodes $T(0)$ and $T(1)$ of the same tree $T$, which are incompatible. So $Z \mapsto X_Z$ is injective.
:::
::::

## Notes and references

Computably dominated degrees were introduced by Miller and Martin (1968), who constructed them by forcing with computable perfect trees, a method due to Spector (1956); they also showed that there are continuum many such degrees. The name "hyperimmune-free" is the traditional one; "computably dominated" is used by Nies and Soare, among others (Downey and Hirschfeldt 2010, Section 2.17, footnote). The characterization by truth-table reducibility is due to Jockusch (1969) and, independently and unpublished, to Martin (Downey and Hirschfeldt 2010, Proposition 2.17.7; Soare 2016, Theorem 5.6.4). Monin and Patey give the f-tree construction and the characterization in the section *Computably dominated degrees* of their chapter *Immunity and function growth*.

- W. Miller and D. A. Martin, *The degrees of hyperimmune sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 159–166.
- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- C. G. Jockusch, *Relationships between reducibilities*, Transactions of the American Mathematical Society 142 (1969), 229–237.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.17.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 5.6.
- B. Monin and L. Patey, *Computability theory*, chapter *Immunity and function growth*.
