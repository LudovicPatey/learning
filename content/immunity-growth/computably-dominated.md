---
title: Computably dominated degrees
summary: Sets all of whose functions are dominated by computable functions; a construction by computable function trees; truth-table reducibility, and the characterization of computably dominated sets by the coincidence of Turing and truth-table reducibility below them.
duration: 45
prerequisites: [immune-sets, pi01-classes/basis-theorems]
---

A set is **computably dominated** (:ref{#def-computably-dominated}), or **hyperimmune-free**, if every function it computes is dominated by a computable function. By :ref{#cor-hyperimmune-degree}, these are exactly the sets that are not of hyperimmune degree. Computable sets are computably dominated, and no non-computable $\Delta^0_2$ set is (:ref{#thm-computation-function}). The computably dominated basis theorem (:ref{#thm-dominated-basis}) gave non-computable examples inside $\Pi^0_1$ classes. This lesson gives a second construction, by **function trees**, which does not use $\Pi^0_1$ classes, and then shows that below a computably dominated set, Turing reducibility coincides with the much more restrictive **truth-table reducibility**.

Being computably dominated is closed downward under Turing reducibility: if $Y \leq_T X$, every $Y$-computable function is $X$-computable.

## Function trees

:::definition{#def-function-tree}
A **function tree**, or **f-tree**, is a total function $T : \bstr \to \bstr$ such that for all strings $\rho, \mu$,
$$
\rho \preceq \mu \iff T(\rho) \preceq T(\mu).
$$
The strings $T(\rho)$ are the **nodes** of $T$. A set $X$ is a **path** of $T$ if infinitely many prefixes of $X$ are nodes of $T$; $[T]$ denotes the class of paths. An f-tree $S$ is a **subtree** of $T$ if every node of $S$ is a node of $T$.
:::

For every $\rho$, the nodes $T(\rho 0)$ and $T(\rho 1)$ strictly extend $T(\rho)$ and are incompatible: neither $\rho 0 \preceq \rho 1$ nor $\rho 1 \preceq \rho 0$, so neither node extends the other. If $S$ is a subtree of $T$, then $[S] \subseteq [T]$, directly from the definition of paths. For every $\rho$, the function $\mu \mapsto T(\rho \mu)$ is a subtree of $T$, computable if $T$ is, whose nodes all extend $T(\rho)$; we call it the **full subtree above** $T(\rho)$.

If $X \in [T]$ and $T(\rho_1) \prec T(\rho_2) \prec \cdots$ are the nodes of $T$ that are prefixes of $X$, then $\rho_1 \prec \rho_2 \prec \cdots$ by the definition, so for every $n$ some string $\rho$ of length $n$ has $T(\rho) \prec X$. The identity $T(\rho) = \rho$ is a computable f-tree whose paths are all sets.

:::lemma{#lem-ftree-noncomputable}
Let $T$ be a computable f-tree and $e \in \nat$. There is a computable subtree $S$ of $T$ such that $\Phi_e \neq X$ for every $X \in [S]$.
:::

:::proof{of=lem-ftree-noncomputable}
The nodes $T(0)$ and $T(1)$ are incompatible, so they differ at some position $i$. If $\Phi_e(i)\converge = T(0)(i)$, let $S$ be the full subtree above $T(1)$; otherwise, the full subtree above $T(0)$. In the first case, every $X \in [S]$ extends $T(1)$, so $X(i) = T(1)(i) \neq \Phi_e(i)$. In the second case, every $X \in [S]$ has $X(i) = T(0)(i)$, which differs from $\Phi_e(i)$ or $\Phi_e(i)$ diverges.
:::

The subtree is computable, but the choice between the two cases is not effective: the lemma asserts existence, not a uniform procedure.

:::lemma{#lem-ftree-domination}
Let $T$ be a computable f-tree and $e \in \nat$. There is a computable subtree $S$ of $T$ such that either $\Phi^X_e$ is partial for every $X \in [S]$, or there is a computable function $g$ that dominates $\Phi^X_e$ for every $X \in [S]$.
:::

:::proof{of=lem-ftree-domination}
*Case 1: there are a node $\sigma = T(\rho)$ and an input $x$ such that $\Phi^\tau_e(x)\diverge$ for every node $\tau \succeq \sigma$ of $T$.* Let $S$ be the full subtree above $\sigma$. If $X \in [S]$ had $\Phi^X_e(x)\converge$, with use $u$, then a node $\tau$ of $S$ that is a prefix of $X$ of length at least $u$ would satisfy $\Phi^\tau_e(x)\converge$, and $\tau \succeq \sigma$ is a node of $T$. So $\Phi^X_e(x)\diverge$ for all $X \in [S]$.

*Case 2: for every node $\sigma$ of $T$ and every input $x$, there is a node $\tau \succeq \sigma$ of $T$ with $\Phi^\tau_e(x)\converge$.* Define $S(\rho) = T(\mu_\rho)$ by induction on $\rho$. Let $\mu_\varepsilon$ be the first string found, in a computable search, with $\Phi^{T(\mu_\varepsilon)}_e(0)\converge$. Given $\mu_\rho$, for $i \in \{0, 1\}$, let $\mu_{\rho i}$ be the first string $\mu \succeq \mu_\rho\, i$ found with $\Phi^{T(\mu)}_e(|\rho| + 1)\converge$. The searches terminate by the hypothesis of Case 2, applied to the nodes $T(\varepsilon)$ and $T(\mu_\rho\, i)$, and the nodes $\tau \succeq T(\mu_\rho\, i)$ of $T$ are of the form $T(\mu)$ with $\mu \succeq \mu_\rho\, i$. So $S$ is computable. Since $\mu_{\rho i} \succeq \mu_\rho\, i$, the map $\rho \mapsto \mu_\rho$ preserves both the prefix relation and incompatibility, so $S$ is an f-tree, and it is a subtree of $T$.

By construction, $\Phi^{S(\rho)}_e(|\rho|)\converge$ for every $\rho$. Let $g(n) = \max \{ \Phi^{S(\rho)}_e(n) : |\rho| = n \}$, a computable function. Let $X \in [S]$ and $n \in \nat$. Some $\rho$ of length $n$ has $S(\rho) \prec X$, so $\Phi^X_e(n) = \Phi^{S(\rho)}_e(n) \leq g(n)$. Hence $\Phi^X_e$ is total and dominated by $g$.
:::

:::theorem[Martin–Miller]{#thm-martin-miller-ftrees}
There is a non-computable computably dominated set. Moreover, it can be taken computable in $\emptyset''$.
:::

:::proof{of=thm-martin-miller-ftrees}
Build computable f-trees $T_0, T_1, \dots$, each a subtree of the previous one. Let $T_0$ be the identity. Given $T_{2e}$, let $T_{2e+1}$ be given by :ref{#lem-ftree-noncomputable} for $T_{2e}$ and $e$. Given $T_{2e+1}$, let $T'$ be given by :ref{#lem-ftree-domination} for $T_{2e+1}$ and $e$, and let $T_{2e+2}$ be the full subtree of $T'$ above $T'(0)$. Each step replaces the tree by a subtree whose root $T_{k+1}(\varepsilon)$ strictly extends $T_k(\varepsilon)$: this holds for the full subtrees used at the odd steps, and is enforced at the even steps by passing to $T'(0)$.

The roots form a chain $T_0(\varepsilon) \prec T_1(\varepsilon) \prec \cdots$ of increasing lengths; let $X$ be their union. For each $k$, the roots $T_j(\varepsilon)$, $j \geq k$, are nodes of $T_k$ and prefixes of $X$, so $X \in [T_k]$. Since $X \in [T_{2e+1}]$, $X \neq \Phi_e$; so $X$ is not computable. Since $X \in [T_{2e+2}] \subseteq [T']$, either $\Phi^X_e$ is partial or it is dominated by a computable function. So $X$ is computably dominated.

For the bound, the construction makes two kinds of choices. At odd steps, it asks whether $\Phi_e(i)\converge = T(0)(i)$, a $\Sigma^0_1$ question. At even steps, it asks whether Case 1 holds, a $\Sigma^0_2$ question about an index of the computable tree; if so, a witness $(\rho, x)$ is found with $\emptyset''$ by asking, for each candidate, the $\Pi^0_1$ question that defines Case 1. Each new tree is then computable from these answers, uniformly. So the sequence of indices of the trees, and $X$, are computable in $\emptyset''$.
:::

The technique of f-trees is a forcing with perfect trees, due to Spector for the construction of minimal degrees; it is used again in the study of the structure of the Turing degrees. The bound $\emptyset''$ is optimal: no non-computable $\Delta^0_2$ set is computably dominated.

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

## Truth-table reducibility

In a Turing reduction $\Phi^X = Y$, the procedure may diverge with oracles other than $X$, and the amount of the oracle it reads is not known in advance. A truth-table reduction fixes in advance, for each input, which bits of the oracle are read and how the answer depends on them.

:::definition{#def-tt}
A set $Y$ is **truth-table reducible** to $X$, written $Y \leq_{tt} X$, if there are total computable functions $\ell$ and $\theta$, where $\theta(n)$ is (a code of) a function from $\{0, 1\}^{\ell(n)}$ to $\{0, 1\}$, such that $Y(n) = \theta(n)(X \uh \ell(n))$ for every $n$.
:::

The function $\theta(n)$ is the **truth table** for the input $n$. Clearly $Y \leq_{tt} X$ implies $Y \leq_T X$. If $Y \leq_m X$ via $f$, then $Y \leq_{tt} X$ with $\ell(n) = f(n) + 1$ and the table that reads the last bit.

:::proposition{#prop-tt-total}
$Y \leq_{tt} X$ if and only if there is a functional $\Phi_e$ such that $\Phi^Z_e$ is total for every oracle $Z$, and $\Phi^X_e = Y$.
:::

:::proof{of=prop-tt-total}
($\Rightarrow$) The functional that, on input $n$ and with any oracle $Z$, computes $\ell(n)$ and $\theta(n)$, reads $Z \uh \ell(n)$ and outputs $\theta(n)(Z \uh \ell(n))$, is total on every oracle.

($\Leftarrow$) Fix $n$. The set $T_n = \{ \sigma : \Phi^\sigma_e(n)[|\sigma|]\diverge \}$ is a computable tree. A path $Z$ of $T_n$ would satisfy $\Phi^Z_e(n)\diverge$ by :ref{#prop-oracle-stages}, which is excluded. By :ref{#lem-weak-konig}, $T_n$ is finite, so there is a length $\ell$ such that every string $\sigma$ of length $\ell$ has $\Phi^\sigma_e(n)[\ell]\converge$. Let $\ell(n)$ be the least such $\ell$, found by a computable search, and let $\theta(n)(\sigma) = \Phi^\sigma_e(n)[\ell(n)]$ for $|\sigma| = \ell(n)$, with value replaced by $0$ if it is not in $\{0, 1\}$. Then $Y(n) = \Phi^X_e(n) = \theta(n)(X \uh \ell(n))$.
:::

The converse of the implications $\leq_m \Rightarrow \leq_{tt} \Rightarrow \leq_T$ fails. The complement of $\emptyset'$ is truth-table reducible to $\emptyset'$, with $\ell(n) = n + 1$ and the table that negates the last bit; it is not many-one reducible to $\emptyset'$, since a set many-one reducible to a c.e. set is c.e. (:ref{#def-many-one}). The failure of the second converse follows from the next theorem, since $\emptyset'$ is not computably dominated.

:::theorem[Jockusch, Martin]{#thm-dominated-tt}
A set $X$ is computably dominated if and only if $Y \leq_T X$ implies $Y \leq_{tt} X$ for every set $Y$.
:::

:::proof{of=thm-dominated-tt}
($\Rightarrow$) Let $Y = \Phi^X_e$, and let $t(n)$ be the least $s$ such that $\Phi^{X \uh s}_e(n)[s]\converge$. It is an $X$-computable total function, so a computable function $g$ dominates it. Let $\ell = g$ and let $\theta(n)(\sigma) = \Phi^\sigma_e(n)[g(n)]$ for $|\sigma| = g(n)$, replaced by $0$ if it diverges or is not in $\{0, 1\}$. Since $t(n) \leq g(n)$, the computation with oracle $X \uh g(n)$ converges within $g(n)$ steps to $Y(n)$, so $Y(n) = \theta(n)(X \uh g(n))$.

($\Leftarrow$) Suppose that $X$ is not computably dominated, and let $f \leq_T X$ be a function dominated by no computable function. Let $F(n) = \max_{m \leq n} f(m)$. Fix an enumeration of the pairs $(\ell_e, \theta_e)$ of partial computable functions. Define $Y$ on inputs $n = \langle e, k \rangle$ as follows. If $\ell_e(n)$ and $\theta_e(n)$ converge within $F(n)$ steps, and $\theta_e(n)$ codes a function on $\{0, 1\}^{\ell_e(n)}$, let $Y(n) = 1 - \theta_e(n)(X \uh \ell_e(n))$; otherwise let $Y(n) = 0$.
Then $Y \leq_T X$. Suppose $Y \leq_{tt} X$ via total $(\ell_e, \theta_e)$. Let $c(n)$ be the number of steps after which both $\ell_e(n)$ and $\theta_e(n)$ have converged; $c$ is computable. If $F(\langle e, k \rangle) \geq c(\langle e, k \rangle)$ for some $k$, then $Y(\langle e, k \rangle) = 1 - \theta_e(\langle e, k \rangle)(X \uh \ell_e(\langle e, k \rangle))$, contradicting the reduction. So $F(\langle e, k \rangle) < c(\langle e, k \rangle)$ for every $k$. For each $m$, let $k(m)$ be the least $k$ with $\langle e, k \rangle \geq m$, and $G(m) = c(\langle e, k(m) \rangle)$. Then $G$ is computable and $G(m) > F(\langle e, k(m) \rangle) \geq f(m)$ for every $m$, so $G$ dominates $f$, a contradiction.
:::

Below a computably dominated set, every Turing reduction can be replaced by a reduction that reads a computably bounded amount of the oracle within a computably bounded time. This makes computably dominated sets behave, for many purposes, like compact objects; for instance, a computably dominated set that computes a DNC function computes one bounded by a computable function, since the DNC function itself is dominated.

:::quiz[truth-table reducibility]
In the proof of ($\Leftarrow$) in :ref{#prop-tt-total}, where is the totality of $\Phi_e$ on **every** oracle used?

- [x] To show that the tree of strings on which the computation at $n$ has not yet converged has no path, hence is finite by König's lemma.
- [ ] To show that $\Phi^X_e = Y$.

  This is a hypothesis, independent of the behavior on other oracles.
- [ ] To make the search for $\ell(n)$ computable.

  The search is computable in any case; totality on every oracle is what makes it terminate.

---

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

Computably dominated degrees were introduced by Miller and Martin (1968), who constructed them by forcing with computable perfect trees, a method due to Spector (1956). The characterization by truth-table reducibility is due to Jockusch (1969) and Martin. Truth-table reducibility was introduced by Post (1944).

- W. Miller and D. A. Martin, *The degrees of hyperimmune sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 159–166.
- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- C. G. Jockusch, *Relationships between reducibilities*, Transactions of the American Mathematical Society 142 (1969), 229–237.
