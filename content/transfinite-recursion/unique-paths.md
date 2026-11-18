---
title: Unique paths and the reversal of the perfect set theorem
summary: A normal form for arithmetic formulas with unique witnesses, by minimal Skolem functions; over ACA₀, ATR₀ is equivalent to the perfect set theorem for closed sets, to the existence of the set of trees with a path in a sequence of trees with at most one path each, and to the corresponding scheme for arithmetic formulas with at most one witness.
duration: 25
prerequisites: [pseudohierarchies, sigma11-separation]
---

In $\mathsf{ACA}_0$, one can ask whether a tree has a path only by a $\Sigma^1_1$ formula, and $\mathsf{ACA}_0$ cannot form the set of trees, in a sequence, that have a path: that needs $\Pi^1_1$ comprehension (:ref{#thm-pi11-trees}). If each tree has at most one path, the question is easier, and the answer is exactly $\mathsf{ATR}_0$. This gives the reversal of the perfect set theorem: a tree with at most one path above each of its first-level nodes has no perfect subtree, so the perfect set theorem lists its paths. The technical step is a normal form with unique witnesses, which makes "there is a unique set such that…" into "this tree has a unique path".

## A normal form with unique witnesses

The normal form of an arithmetic formula $\varphi(X)$ introduces Skolem functions for its existential quantifiers. Different Skolem functions may witness the same formula. Choosing the least witness each time makes them unique.

:::lemma[Simpson]{#lem-unique-normal-form}
For every arithmetic formula $\varphi(X)$, possibly with other parameters, there is a $\Sigma^0_0$ formula $\theta(\rho, \tau)$ such that $\mathsf{ACA}_0$ proves, for every $X$:
1. $\varphi(X)$ holds if and only if there is a function $g$ with $\theta(X \uh m, g \uh m)$ for every $m$;
2. there is at most one such function $g$.
:::

:::proof{of=lem-unique-normal-form}
Write $\varphi$ with $\neg$, $\wedge$ and $\exists$ only, replacing $\forall n$ by $\neg \exists n\, \neg$. Let $\exists n\, \psi_k(\vec m_k, n)$, for $k < r$, be the subformulas of $\varphi$ beginning with an existential quantifier, where $\vec m_k$ lists their free number variables. Their **minimal Skolem functions** are $g_k(\vec m_k) = 0$ if $\neg \exists n\, \psi_k(\vec m_k, n)$, and $g_k(\vec m_k) = n_0 + 1$ if $n_0$ is the least $n$ with $\psi_k(\vec m_k, n)$. For functions $g_0, \ldots, g_{r-1}$ and a subformula $\chi$, let $\chi^g$ be obtained by replacing each maximal subformula of $\chi$ of the form $\exists n\, \psi_k(\vec m_k, n)$ by $g_k(\vec m_k) > 0$; $\chi^g$ has no quantifiers, and $\psi_k^g$ is obtained in the same way from $\psi_k$. Let $\mathrm{Sk}(g)$ say, for each $k < r$ and all $\vec m_k$ and $n$:
$$
\begin{aligned}
g_k(\vec m_k) = 0 &\rightarrow \neg \psi_k^g(\vec m_k, n), \\
g_k(\vec m_k) = n + 1 &\rightarrow \psi_k^g(\vec m_k, n) \wedge \forall n' < n\ \neg \psi_k^g(\vec m_k, n').
\end{aligned}
$$
This is a $\Pi^0_1$ condition on $X$ and $g$.

The minimal Skolem functions exist by arithmetic comprehension, and for them, $\chi^g \leftrightarrow \chi$ for every subformula $\chi$, by induction on $\chi$ in the metatheory; so they satisfy $\mathrm{Sk}$. Conversely, let $g$ satisfy $\mathrm{Sk}$. By induction on the number of nested quantifiers above $\psi_k$, counted from the inside: if the functions for the subformulas of $\psi_k$ are minimal, then $\psi_k^g \leftrightarrow \psi_k$, and $\mathrm{Sk}$ forces $g_k$ to be minimal. So $g$ is the tuple of minimal Skolem functions. Hence $\varphi(X)$ holds if and only if some $g$ satisfies $\mathrm{Sk}(g) \wedge \varphi^g$, and such a $g$ is unique. Coding the tuple $g$ as one function, the condition $\mathrm{Sk}(g) \wedge \varphi^g$ is $\Pi^0_1$ in $X$ and $g$, and can be written as $\forall m\, \theta(X \uh m, g \uh m)$ with $\theta$ bounded, as for every $\Pi^0_1$ formula.
:::

## Unique paths

:::theorem{#thm-unique-paths}
The following are equivalent over $\mathsf{ACA}_0$.
1. $\mathsf{ATR}_0$.
2. The **perfect set theorem**: every tree $T \subseteq \nat^{<\nat}$ with uncountably many paths has a non-empty perfect subtree.
3. For every sequence of trees $(T_i)$ each of which has at most one path, the set $\{ i : T_i \text{ has a path} \}$ exists.
4. For every arithmetic formula $\varphi(i, X)$ such that each $i$ has at most one $X$ with $\varphi(i, X)$, the set $\{ i : \exists X\, \varphi(i, X) \}$ exists.
:::

Here "$T$ has uncountably many paths" means that for every sequence $(Y_n)$, some path of $T$ differs from every $Y_n$.

:::proof{of=thm-unique-paths}
(1 ⇒ 2) This is :ref{#thm-perfect-set-atr}.

(2 ⇒ 3) Let $(T_i)$ be a sequence of trees with at most one path each, and $T$ the tree consisting of $\langle\rangle$ and the strings $\langle i \rangle \tau$ with $\tau \in T_i$. Suppose $P$ is a non-empty perfect subtree of $T$. The root of $P$ has two incompatible extensions, so some $\langle i \rangle$ is in $P$, and the nodes of $P$ above $\langle i \rangle$ form a perfect tree: they split in $P$, and their incompatible extensions are still above $\langle i \rangle$. A non-empty perfect tree has two different paths: from a node, take two incompatible extensions, and extend each to a path by always choosing an extension in the tree. This gives two different paths of $T_i$, a contradiction. So $T$ has no non-empty perfect subtree, and by 2, it has countably many paths: there is a sequence $(f_n)$ containing every path of $T$. By arithmetic comprehension, the set of $i$ such that some $f_n$ is a path of $T$ with $f_n(0) = i$ exists, and it is $\{ i : T_i \text{ has a path} \}$.

(3 ⇒ 4) Let $\varphi(i, X)$ have at most one witness for each $i$. Apply :ref{#lem-unique-normal-form} to $\varphi(i, X)$, with $i$ as a parameter; it gives $\theta(i, \rho, \tau)$ such that $\varphi(i, X)$ holds if and only if some $g$ satisfies $\theta(i, X \uh m, g \uh m)$ for all $m$, and then $g$ is unique. Let $T_i$ be the tree of the sequences of pairs $\langle (\rho(0), \tau(0)), \ldots, (\rho(k-1), \tau(k-1)) \rangle$ with $\rho \in \bstr$ and $\theta(i, \rho \uh m, \tau \uh m)$ for every $m \leq k$. Its paths are the pairs $(X, g)$ with $\theta(i, X \uh m, g \uh m)$ for all $m$. So $T_i$ has a path if and only if $\exists X\, \varphi(i, X)$, and it has at most one, since $X$ is unique and $g$ is unique for $X$. Apply 3.

(4 ⇒ 1) Let $W$ be a well-ordering and $\theta$ arithmetic. Let $\varphi(\langle j, n \rangle, Y)$ say that $Y$ is a $\theta$-hierarchy along $W \uh j$ and $\theta(n, j, Y)$. By :ref{#prop-hierarchy-unique}, each $\langle j, n \rangle$ has at most one witness. By 4, the set $Z = \{ \langle j, n \rangle : \exists Y\, \varphi(\langle j, n \rangle, Y) \}$ exists. As in the converse direction of :ref{#thm-atr-sigma11-separation}, arithmetic transfinite induction shows that for every $j \in F_W$, the part of $Z$ below $j$ is a hierarchy along $W \uh j$ and the column $Z^{[j]}$ is $\{ n : \theta(n, j, Z_j) \}$; so the restriction of $Z$ to the columns of $F_W$ is a $\theta$-hierarchy along $W$.
:::

:::quiz[unique paths]
In (2 ⇒ 3), where is the hypothesis that each $T_i$ has at most one path used?

- [x] To show that the combined tree $T$ has no non-empty perfect subtree, so that the perfect set theorem applies in its contrapositive form and lists the paths of $T$.
- [ ] To show that $T$ is a tree.

  $T$ is a tree for any sequence of trees.
- [ ] To decide, for each $i$, which $f_n$ is the path of $T_i$.

  Any $f_n$ that is a path with $f_n(0) = i$ will do; uniqueness is not needed for this step.

---

Why does :ref{#lem-unique-normal-form} use the **least** witnesses?

- [x] To make the Skolem functions unique, so that a formula with a unique witness $X$ becomes a tree with a unique path; arbitrary Skolem functions could give many paths for the same $X$.
- [ ] Because least witnesses are computable.

  They are computable from $X$ only with an arithmetic oracle; their existence uses arithmetic comprehension.
- [ ] Because otherwise the normal form would not be $\Pi^0_1$.

  The usual normal form, with arbitrary Skolem functions, is also $\Pi^0_1$; the minimality conditions are added for uniqueness.
:::

A tree with a unique path is the formal counterpart of a $\Pi^0_1$ singleton of Baire space, and in computability theory such a singleton is hyperarithmetic; the theorem says that $\mathsf{ATR}_0$ is what it takes to decide, uniformly, which of countably many such trees have their path. The equivalence of 1 and 2 holds even for trees in $\bstr$, by a coding of Baire space into Cantor space that preserves perfect subtrees (Simpson, Theorem V.5.5 and Lemma V.5.6); and 3 and 4 are equivalent to $\mathsf{ATR}_0$ over $\mathsf{RCA}_0$, since each implies arithmetic comprehension (:ref{#ex-unique-paths-aca}).

::::exercise{#ex-unique-paths-aca difficulty=1 objective="Show that the unique path principle implies arithmetic comprehension, by coding the complement of a range into trees with at most one path."}
Show in $\mathsf{RCA}_0$ that statement 3 of :ref{#thm-unique-paths} implies $\mathsf{ACA}_0$.

:::solution
Let $f$ be a function, and $T_i$ the tree of the strings $0^k$ such that $f(m) \neq i$ for every $m < k$. It exists, uniformly in $i$, by $\Delta^0_1$ comprehension, and it has at most one path, the constant function $0$. It has this path if and only if $f(m) \neq i$ for every $m$. By 3, the set $\{ i : i \notin \mathrm{ran}(f) \}$ exists, and its complement is the range of $f$. By :ref{#thm-aca-equivalents}, $\mathsf{ACA}_0$ holds.
:::
::::

## Notes and references

:ref{#lem-unique-normal-form} is Simpson, Lemma V.5.4, and :ref{#thm-unique-paths} combines his Theorems V.5.2 and V.5.5; Simpson proves the implication from $\mathsf{ATR}_0$ to statement 4 through the Borel domain theorem, while the proof given here passes through the perfect set theorem, following his proof of the reversal (Theorem V.5.5, 4 ⇒ 1). The equivalence of $\mathsf{ATR}_0$ with the perfect set theorem was announced by Friedman (1975); the other equivalences are due to Simpson.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section V.5.
- H. Friedman, *Some systems of second order arithmetic and their use*, Proceedings of the International Congress of Mathematicians, Vancouver, 1974, vol. 1, 1975, 235–242.

:::::exercises
::::exercise{#ex-perfect-subtree-two-paths difficulty=1 objective="Check that a non-empty perfect tree has two different paths, the step used in the reversal."}
Show in $\mathsf{RCA}_0$ that every non-empty perfect tree $P \subseteq \nat^{<\nat}$ has two different paths.

:::solution
The root has two incompatible extensions $\tau_0$ and $\tau_1$ in $P$. For $\tau \in P$, let $e(\tau)$ be the first proper extension of $\tau$ in $P$, in a fixed enumeration of strings; it exists since $\tau$ has two incompatible extensions, one of which is a proper extension. The sequence $\tau_i, e(\tau_i), e(e(\tau_i)), \ldots$ is defined by primitive recursion with terminating searches relative to $P$, and its union $Y_i$ is a path of $P$. The paths $Y_0$ and $Y_1$ differ, since they extend the incompatible strings $\tau_0$ and $\tau_1$.
:::
::::

::::exercise{#ex-unique-paths-pi11 difficulty=2 objective="Compare the unique path principle with Π¹₁ comprehension, which drops the uniqueness hypothesis."}
1. Show that $\Pi^1_1\text{-}\mathsf{CA}_0$ proves statement 3 of :ref{#thm-unique-paths}, directly from :ref{#thm-pi11-trees}.
2. Let $(T_i)$ be a sequence of trees with countably many paths each, given by sequences $(Y_{i,n})_n$ listing the paths of each $T_i$. Show in $\mathsf{ACA}_0$ that $\{ i : T_i \text{ has a path} \}$ exists. Why does this not contradict the fact that $\mathsf{ATR}_0$ is needed in statement 3?

:::solution
1. By :ref{#thm-pi11-trees}, $\Pi^1_1\text{-}\mathsf{CA}_0$ proves that $\{ i : T_i \text{ has a path} \}$ exists for every sequence of trees, without hypothesis on the number of paths.
2. $T_i$ has a path if and only if some $Y_{i,n}$ is a path of $T_i$, an arithmetic condition in the double sequence; the set exists by arithmetic comprehension. There is no contradiction: in statement 3, the paths are not given; the perfect set theorem, hence $\mathsf{ATR}_0$, is what provides a sequence listing them.
:::
::::
:::::
