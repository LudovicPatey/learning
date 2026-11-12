---
title: Parallelization
summary: The parallelization of a problem solves countably many instances at once; the jump is parallel LPO and weak König's lemma is parallel LLPO; separations of the Turing degrees transfer to problems that admit computable solutions; a single application against finitely many.
duration: 45
prerequisites: [weihrauch]
---

The omniscience principles of the previous lesson have numbers as solutions, and admit computable solutions: their strength is invisible to ω-reducibility and computable reducibility. **Parallelization** makes it visible. It asks for solutions to countably many instances at once, given together, and requires an answer to all of them. A single instance of $\mathsf{LPO}$ answers one $\Sigma^0_1$ question; countably many answer all the $\Sigma^0_1$ questions about a set, that is, compute its jump. In the same way, countably many instances of $\mathsf{LLPO}$ choose a path through a binary tree, one branching at a time. The two parallelizations are the jump and weak König's lemma, and the separation of these two problems in ω-models transfers back to the omniscience principles.

## Parallelization

:::definition{#def-parallelization}
The **parallelization** of a problem $\mathsf P$ is the problem $\widehat{\mathsf P}$ whose instances are the sequences $\bigoplus_n X_n$ of instances of $\mathsf P$, and whose solutions are the sequences $\bigoplus_n Y_n$ with $Y_n$ a solution to $X_n$ for every $n$.
:::

When the solutions of $\mathsf P$ are numbers in $\{ 0, 1 \}$, as for $\mathsf{LPO}$ and $\mathsf{LLPO}$, a solution $\bigoplus_n Y_n$ to $\widehat{\mathsf P}$ is identified with the set $\{ n : Y_n = \{ 0 \} \}$, the sequence of the values of the solutions. Each of the two codings is computable from the other, uniformly, so the identification does not affect Weihrauch reducibility.

The instances of $\widehat{\mathsf P}$ are given all at once, and the solutions to them are independent: the instance $X_{n+1}$ cannot depend on the solution chosen for $X_n$. Parallelization is thus different from repeated application, in which each instance is computed from the previous solutions; the jump of the jump is not a parallel use of the jump. Some examples:

- $\widehat{\mathsf{Id}} \equiv_W \mathsf{Id}$, and more generally $\widehat{\mathsf P} \equiv_W \mathsf P$ whenever $\mathsf P$ uniformly admits computable solutions: apply the solving functional to each coordinate.
- $\widehat{\mathsf J} \equiv_W \mathsf J$: the jump of $\bigoplus_n X_n$ computes the jump of each $X_n$, uniformly in $n$.
- $\widehat{\mathsf{RT}^1_2}$ does not admit computable solutions, although $\mathsf{RT}^1_2$ does: a computable sequence of colorings can be built so that the colors of the infinite homogeneous sets form the halting set (third exercise). Parallelization does not preserve the property of admitting computable solutions, only its uniform version.

If $\mathsf P \leq_W \mathsf Q$ via $\Phi$ and $\Psi$, then $\widehat{\mathsf P} \leq_W \widehat{\mathsf Q}$ via the functionals applying $\Phi$ and $\Psi$ to each coordinate. This is where uniformity is needed: a computable reduction gives, for each $X_n$, some reduction, but not a single procedure that handles all of them. So parallelization is an operation on Weihrauch degrees, and it turns the omniscience principles into familiar problems.

:::theorem{#thm-jump-lpo}
$\mathsf J \equiv_W \widehat{\mathsf{LPO}}$.
:::

:::proof{of=thm-jump-lpo}
($\mathsf J \leq_W \widehat{\mathsf{LPO}}$) Given $X$, let $\Phi^X = \bigoplus_e p_e$, with $p_e(s) = 1$ if $\Phi^X_e(e)[s]\converge$ and $0$ otherwise. The solution to $p_e$ is $1$ exactly when $e \in X'$, so the solution to $\Phi^X$ is $X'$, and $\Psi^{X \oplus Y} = Y$.

($\widehat{\mathsf{LPO}} \leq_W \mathsf J$) Let $\Phi$ be the identity. By the parameter theorem, uniformly in the oracle, there is a computable function $g$ such that for every $Z = \bigoplus_n p_n$, $\Phi^Z_{g(n)}(g(n))$ converges if and only if $p_n(s) = 1$ for some $s$. Let $\Psi^{Z \oplus Y}$ be the sequence whose $n$-th term is $Y(g(n))$. For $Y = Z'$, this is the sequence of solutions to the $p_n$.
:::

Both reductions are strong: the backward functionals only use the solution. For weak König's lemma, the idea is to follow the tree from the root, and to decide at each node which successor to take. The right decision, an extendible successor, cannot be computed from the tree, but it can be obtained from one instance of $\mathsf{LLPO}$: the instance watches the two successors, and records the first one found to die; any solution avoids it.

:::theorem{#thm-wkl-llpo}
$\mathsf{WKL} \equiv_W \widehat{\mathsf{LLPO}}$.
:::

:::proof{of=thm-wkl-llpo}
($\widehat{\mathsf{LLPO}} \leq_W \mathsf{WKL}$) Given $\bigoplus_n p_n$, let $T$ be the tree of strings $\sigma$ such that $p_n(2m + \sigma(n)) = 0$ for all $n, m$ with $n < |\sigma|$ and $2m + \sigma(n) < |\sigma|$. It is computable uniformly in the instance. It is infinite, since a sequence of solutions to the $p_n$ gives strings of every length in $T$, and its paths are exactly the sequences of solutions. So $\Psi^{X \oplus Y} = Y$ works.

($\mathsf{WKL} \leq_W \widehat{\mathsf{LLPO}}$) Let $T$ be an infinite binary tree. For a string $\sigma$ and $i < 2$, say that $\sigma^\frown i$ **dies at stage $s$** if $T$ has no extension of $\sigma^\frown i$ of length $|\sigma| + 1 + s$. Let $q_\sigma(2s + i) = 1$ if $s$ is the least stage at which one of $\sigma^\frown 0$, $\sigma^\frown 1$ dies, and $i$ is the least $j$ such that $\sigma^\frown j$ dies at $s$; all other values are $0$. Then $q_\sigma$ has at most one $1$, and $\Phi^T = \bigoplus_\sigma q_\sigma$, indexed by a computable enumeration of strings, is an instance of $\widehat{\mathsf{LLPO}}$.

Let $\bigoplus_\sigma i_\sigma$ be a solution. If $\sigma$ is **extendible**, that is, has extensions in $T$ of every length, then $\sigma^\frown i_\sigma$ is extendible. Indeed, one of the two successors is extendible. If one of them dies, $q_\sigma$ has a $1$ at $2s + i$ for the first one found dead, and $i_\sigma \neq i$, so $\sigma^\frown i_\sigma$ is the other successor, which does not die at the stage $s$; since $\sigma$ is extendible and $\sigma^\frown i$ is not, $\sigma^\frown i_\sigma$ is extendible. If none dies, both successors are extendible. Let $\Psi^{T \oplus Y}$ be the path $\rho_0 = \varepsilon$, $\rho_{k+1} = \rho_k {}^\frown i_{\rho_k}$. The empty string is extendible since $T$ is infinite, so every $\rho_k$ is extendible, and the limit is a path through $T$.
:::

:::figure[The instance $q_\sigma$ of :ref{#thm-wkl-llpo} for a node $\sigma$ whose left successor dies at stage $2$, while the right one survives. The $1$ at position $2 \cdot 2 + 0$ excludes the solution $0$, and the path continues through $\sigma^\frown 1$. If neither successor died, $q_\sigma$ would be $0^\infty$, and both answers would be correct.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Left: a node sigma whose left successor dies at stage 2 while the right successor is extendible. Right: the instance q sigma of LLPO, with a single 1 at position 4 = 2 times 2 plus 0, whose only solution is 1"><defs><marker id="ah-llpo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="190" y1="30" x2="120.0" y2="74" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="120.0" y1="74" x2="78.8" y2="118" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="120.0" y1="74" x2="161.2" y2="118" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="190" y1="30" x2="260.0" y2="74" class="accent-stroke" stroke-width="2.0"/><line x1="260.0" y1="74" x2="218.8" y2="118" class="ink-stroke" stroke-width="1.2"/><line x1="260.0" y1="74" x2="301.2" y2="118" class="accent-stroke" stroke-width="2.0"/><line x1="218.8" y1="118" x2="194.6" y2="162" class="ink-stroke" stroke-width="1.2"/><line x1="301.2" y1="118" x2="277.0" y2="162" class="ink-stroke" stroke-width="1.2"/><line x1="301.2" y1="118" x2="325.4" y2="162" class="accent-stroke" stroke-width="2.0"/><line x1="194.6" y1="162" x2="180.4" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="277.0" y1="162" x2="262.7" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="325.4" y1="162" x2="311.2" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="325.4" y1="162" x2="339.6" y2="206" class="accent-stroke" stroke-width="2.0"/><circle cx="190" cy="30" r="3.5" class="ink-fill"/><circle cx="120.0" cy="74" r="3.5" class="muted-fill"/><circle cx="78.8" cy="118" r="3.5" class="muted-fill"/><circle cx="161.2" cy="118" r="3.5" class="muted-fill"/><circle cx="260.0" cy="74" r="3.5" class="ink-fill"/><circle cx="218.8" cy="118" r="3.5" class="ink-fill"/><circle cx="301.2" cy="118" r="3.5" class="ink-fill"/><circle cx="194.6" cy="162" r="3.5" class="ink-fill"/><circle cx="277.0" cy="162" r="3.5" class="ink-fill"/><circle cx="325.4" cy="162" r="3.5" class="ink-fill"/><circle cx="180.4" cy="206" r="3.5" class="ink-fill"/><circle cx="262.7" cy="206" r="3.5" class="ink-fill"/><circle cx="311.2" cy="206" r="3.5" class="ink-fill"/><circle cx="339.6" cy="206" r="3.5" class="ink-fill"/><text x="202" y="26" text-anchor="start" class="math" font-size="16">σ</text><line x1="71.8" y1="126" x2="85.8" y2="126" class="muted-stroke" stroke-width="1.4"/><line x1="154.2" y1="126" x2="168.2" y2="126" class="muted-stroke" stroke-width="1.4"/><text x="16" y="150" text-anchor="start" class="label">σ⌢0 dies at stage 2:</text><text x="16" y="166" text-anchor="start" class="label">no extension of length |σ| + 3</text><text x="339.6" y="228" text-anchor="middle" class="mrm muted" font-size="15">⋮</text><text x="354" y="99" text-anchor="end" class="math" font-size="17">q</text><text x="354" y="104" class="math" font-size="11">σ</text><rect x="372" y="80" width="25" height="25" class="cell"/><text x="384.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="384.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">0</text><rect x="397" y="80" width="25" height="25" class="cell"/><text x="409.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="409.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">1</text><rect x="422" y="80" width="25" height="25" class="cell"/><text x="434.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="434.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">2</text><rect x="447" y="80" width="25" height="25" class="cell"/><text x="459.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="459.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">3</text><rect x="472" y="80" width="25" height="25" class="cell head-cell"/><text x="484.5" y="98" text-anchor="middle" class="mrm" font-size="14">1</text><text x="484.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">4</text><rect x="497" y="80" width="25" height="25" class="cell"/><text x="509.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="509.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">5</text><rect x="522" y="80" width="25" height="25" class="cell"/><text x="534.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="534.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">6</text><rect x="547" y="80" width="25" height="25" class="cell"/><text x="559.5" y="98" text-anchor="middle" class="mrm" font-size="14">0</text><text x="559.5" y="119" text-anchor="middle" class="mrm muted" font-size="11">7</text><text x="578" y="98" class="mrm muted" font-size="15">⋯</text><text x="372" y="66" text-anchor="start" class="label">position 2s + i = 4: s = 2, i = 0</text><text x="372" y="156" text-anchor="start" class="label">the only solution to this instance is 1:</text><text x="372" y="174" text-anchor="start" class="label">the path is extended by σ⌢1</text></svg>
:::

The backward functional uses only the solution, so the reductions are again strong; Brattka and Gherardi proved $\mathsf{WKL} \equiv_{sW} \widehat{\mathsf{LLPO}}$. The proof of the second reduction is a uniform version of the proof that weak König's lemma holds: the non-uniform step "choose an extendible successor" is isolated, and handed to $\mathsf{LLPO}$ once for each node.

:::corollary{#cor-lpo-not-llpo}
$\mathsf{LPO} \not\leq_W \mathsf{LLPO}$. So $\mathsf{LLPO} <_W \mathsf{LPO}$.
:::

:::proof{of=cor-lpo-not-llpo}
If $\mathsf{LPO} \leq_W \mathsf{LLPO}$, then $\widehat{\mathsf{LPO}} \leq_W \widehat{\mathsf{LLPO}}$, so $\mathsf J \leq_W \mathsf{WKL}$ by :ref{#thm-jump-lpo} and :ref{#thm-wkl-llpo}. This would give $\mathsf J \leq_\omega \mathsf{WKL}$, which fails by :ref{#cor-wkl-not-j}.
:::

The proof transfers a separation of ω-reducibility, obtained from the cone avoidance basis theorem, to a separation between two problems that admit computable solutions, which ω-reducibility and computable reducibility do not distinguish. Parallelization thus connects the uniform world of Weihrauch reducibility with the non-uniform world of Turing degrees. The third exercise of the previous lesson proves the same separation by a continuity argument; the two proofs illustrate the two main methods of the subject.

:::quiz[parallelization]
In the proof that $\mathsf{WKL} \leq_W \widehat{\mathsf{LLPO}}$, why is the instance $q_\sigma$ defined from the first stage at which a successor dies, rather than from the extendibility of the successors?

- [x] Because extendibility is a $\Pi^0_1$ property of the tree, not computable from it, while the instance must be computed uniformly; the first death is found by a search, and $\mathsf{LLPO}$ only needs to avoid the side found dead.
- [ ] Because both successors may die.

  If $\sigma$ is extendible, at most one successor dies; the definition handles the other cases arbitrarily.
- [ ] Because $\mathsf{LLPO}$ instances must have exactly one $1$.

  They may have none, in which case both answers are solutions.

---

Why does :ref{#cor-lpo-not-llpo} pass through the parallelizations?

- [x] Because $\mathsf{LPO}$ and $\mathsf{LLPO}$ admit computable solutions, so ω-reducibility and computable reducibility do not separate them; their parallelizations are $\mathsf J$ and $\mathsf{WKL}$, which are separated in ω-models by the cone avoidance basis theorem.
- [ ] Because Weihrauch reducibility is only defined for parallel problems.

  It is defined for all problems.
- [ ] Because $\mathsf{LLPO}$ has two solutions on some instances.

  Multiple solutions are allowed in all reducibilities.

---

Why does a computable reduction $\mathsf P \leq_c \mathsf Q$ not give $\widehat{\mathsf P} \leq_c \widehat{\mathsf Q}$ in general?

- [x] Because the reduction may use a different procedure for each instance $X_n$, and the sequence of these procedures need not be computable from $\bigoplus_n X_n$.
- [ ] Because $\widehat{\mathsf Q}$ has no computable instance.

  It has one when $\mathsf Q$ has one: the constant sequence.
- [ ] Because the solutions to the $X_n$ are not independent.

  They are independent: each $Y_n$ is any solution to $X_n$.
:::

## Exercises

::::exercise{difficulty=1}
Show that if $\mathsf P$ uniformly admits computable solutions, then so does $\widehat{\mathsf P}$. Deduce from :ref{#thm-wkl-llpo} a second proof that $\mathsf{LLPO}$ does not uniformly admit computable solutions.

:::solution
If $\Phi^X$ solves $\mathsf P$, then the functional $\bigoplus_n X_n \mapsto \bigoplus_n \Phi^{X_n}$ solves $\widehat{\mathsf P}$. If $\mathsf{LLPO}$ uniformly admitted computable solutions, so would $\widehat{\mathsf{LLPO}}$, and so would $\mathsf{WKL} \leq_W \widehat{\mathsf{LLPO}}$; in particular every infinite computable binary tree would have a computable path. But some infinite computable binary tree has no computable path (:ref{#thm-dnc2-no-computable}).
:::
::::

::::exercise{difficulty=1}
Show that $\mathsf P \leq_W \widehat{\mathsf P}$ and $\widehat{\widehat{\mathsf P}} \equiv_W \widehat{\mathsf P}$ for every problem $\mathsf P$, so that parallelization is a closure operator on the Weihrauch degrees.

:::solution
For the first reduction, send $X$ to the constant sequence $\bigoplus_n X$, and read the first coordinate of a solution. For the second, $\widehat{\mathsf P} \leq_W \widehat{\widehat{\mathsf P}}$ is the first reduction applied to $\widehat{\mathsf P}$. Conversely, an instance of $\widehat{\widehat{\mathsf P}}$ is a double sequence $\bigoplus_m \bigoplus_n X_{m, n}$; send it to the single sequence $\bigoplus_k X_{k_0, k_1}$, where $k \mapsto (k_0, k_1)$ is a computable bijection from $\nat$ to $\nat^2$, and rearrange a solution in the same way.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf J \leq_W \widehat{\mathsf{RT}^1_2}$. Deduce that $\widehat{\mathsf{RT}^1_2}$ does not admit computable solutions, although $\mathsf{RT}^1_2$ does.

:::solution
Given $X$, let $f_e(s) = 1$ if $\Phi^X_e(e)[s]$ converges, and $f_e(s) = 0$ otherwise, and let $\Phi^X = \bigoplus_e f_e$, an instance of $\widehat{\mathsf{RT}^1_2}$ computable in $X$, uniformly. If $e \in X'$, then $f_e(s) = 1$ for almost all $s$, so every infinite homogeneous set for $f_e$ has color $1$; otherwise $f_e$ is constant $0$. Given a solution $\bigoplus_e H_e$, let $\Psi$ output the set of $e$ with $f_e(\min H_e) = 1$, the colors of the $H_e$; it is $X'$. For $X = \emptyset$, the computable instance $\Phi^\emptyset$ has no computable solution, since every solution computes $\emptyset'$.
:::
::::

::::exercise{difficulty=2}
For a problem $\mathsf P$ and $n \geq 1$, let $\mathsf P^n$ be the product of $n$ copies of $\mathsf P$. Show that if $\mathsf P$ admits computable solutions, so does $\mathsf P^n$, and that $\mathsf J \not\leq_c \mathsf Q$ for every problem $\mathsf Q$ that admits computable solutions. Deduce that $\widehat{\mathsf{LPO}} \not\leq_W \mathsf{LPO}^n$ for every $n$: finitely many parallel applications of $\mathsf{LPO}$ do not suffice.

:::solution
An instance $X_1 \oplus \cdots \oplus X_n$ of $\mathsf P^n$ computes each $X_i$, hence a solution $Y_i$ to each, hence $Y_1 \oplus \cdots \oplus Y_n$. If $\mathsf J \leq_c \mathsf Q$ with $\mathsf Q$ admitting computable solutions, then for every $X$, the instance $\widetilde X \leq_T X$ has a solution $\widetilde Y \leq_T \widetilde X$, and $X \oplus \widetilde Y \leq_T X$ computes $X'$, which is impossible. Since $\mathsf{LPO}$ admits computable solutions, so does $\mathsf{LPO}^n$; and $\widehat{\mathsf{LPO}} \leq_W \mathsf{LPO}^n$ would give $\mathsf J \leq_c \mathsf{LPO}^n$ by :ref{#thm-jump-lpo}.
:::
::::

::::exercise{difficulty=2}
Let $\mathsf J^{(2)}$ be the problem whose instances are all sets, the only solution to $X$ being $X''$. Show that $\mathsf{KL} \leq_W \mathsf J^{(2)}$, while $\mathsf{KL} \not\leq_c \mathsf J$ (:ref{#prop-kl-not-c-j}).

:::solution
Let $\Phi^T = T$. For a node $\sigma$ and a number $m$, whether $T$ contains some $\sigma^\frown n$ with $n \geq m$ is a $\Sigma^0_1(T)$ question, answered by $T'$ uniformly. Since $T$ is finitely branching, searching for the least $m$ with a negative answer gives, computably in $T'$ and uniformly, a function $h$ bounding the successors of every node. Then $T \oplus h \leq_T T'$ uniformly, and by the solution of the second exercise of the previous lesson, $(T \oplus h)'$ computes a path through $T$, uniformly. Since $(T \oplus h)' \leq_T T''$ uniformly, $\Psi^{T \oplus T''}$ can compute this path.
:::
::::

## Notes and references

Parallelization was used by Brattka in computable analysis (in his 1999 dissertation and a 2003 survey), and studied as an operation on Weihrauch degrees by Brattka and Gherardi (2011), who proved $\mathsf{WKL} \equiv_{sW} \widehat{\mathsf{LLPO}}$ (their Theorem 8.2); the equivalence of $\widehat{\mathsf{LPO}}$ with the limit operation and with the jump is Theorem 6.7 of the survey of Brattka, Gherardi and Pauly, which gives the history of both results. Dzhafarov and Mummert define parallelization in Section 3.1 (Definition 3.1.5), state the third exercise as their Exercise 3.9.4, and treat reductions to several applications in Section 4.5, where they also define the **compositional product** $\mathsf Q * \mathsf P$, the problem of applying $\mathsf P$ and then $\mathsf Q$ to an instance computed from the solution; it was introduced by Brattka, Gherardi and Marcone (2012), who showed that the Bolzano–Weierstrass theorem is Weihrauch equivalent to the jump of $\mathsf{WKL}$. The Weihrauch analysis of Ramsey's theorem for all exponents and numbers of colors is due to Brattka and Rakotoniaina (2017).

- V. Brattka and G. Gherardi, *Weihrauch degrees, omniscience principles and weak computability*, Journal of Symbolic Logic 76 (2011), 143–176.
- V. Brattka, G. Gherardi and A. Pauly, *Weihrauch complexity in computable analysis*, in Handbook of Computability and Complexity in Analysis, Springer, 2021, 367–417.
- V. Brattka, G. Gherardi and A. Marcone, *The Bolzano–Weierstrass theorem is the jump of weak Kőnig's lemma*, Annals of Pure and Applied Logic 163 (2012), 623–655.
- V. Brattka and T. Rakotoniaina, *On the uniform computational content of Ramsey's theorem*, Journal of Symbolic Logic 82 (2017), 1278–1316.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 3.1 and 4.5.
