---
title: Weihrauch reducibility
summary: Uniform computable reductions; uniformly true problems, and the pigeonhole principle as a problem that is computably but not uniformly true; the omniscience principles LPO and LLPO; parallelization, the jump as parallel LPO and weak König's lemma as parallel LLPO.
duration: 40
prerequisites: [computable-reducibility]
---

A computable reduction may depend on the instance in a non-uniform way: the proof that $\mathsf{RT}^1_2$ is computably true chooses a color class that is infinite, a choice that cannot be made by an algorithm reading the coloring. **Weihrauch reducibility** requires the reduction to be given by two fixed Turing functionals, one transforming the instance and one transforming the solution back. It was introduced by Weihrauch in computable analysis in the 1980s, and Gherardi and Marcone (2009) brought it to reverse mathematics, where it measures the uniform content of proofs.

## Definitions

:::definition{#def-weihrauch}
Let $\mathsf P$ and $\mathsf Q$ be problems.

1. $\mathsf P$ is **Weihrauch reducible** to $\mathsf Q$, written $\mathsf P \leq_W \mathsf Q$, if there are Turing functionals $\Phi$ and $\Psi$ such that, for every instance $X$ of $\mathsf P$, $\Phi^X$ is an instance of $\mathsf Q$, and for every solution $\widetilde Y$ to $\Phi^X$, $\Psi^{X \oplus \widetilde Y}$ is a solution to $X$.
2. $\mathsf P$ is **strongly Weihrauch reducible** to $\mathsf Q$, written $\mathsf P \leq_{sW} \mathsf Q$, if moreover $\Psi$ only uses $\widetilde Y$: $\Psi^{\widetilde Y}$ is a solution to $X$.
3. $\mathsf P$ is **uniformly true** if there is a Turing functional $\Phi$ such that $\Phi^X$ is a solution to $X$ for every instance $X$.
:::

In item 1, $\Phi^X$ and $\Psi^{X \oplus \widetilde Y}$ are required to be total, as characteristic functions of sets. Weihrauch reducibility implies computable reducibility, and strong Weihrauch reducibility implies strong computable reducibility. Together with the previous lessons, we have the implications
$$
\begin{gathered}
\mathsf P \leq_{sW} \mathsf Q \;\Rightarrow\; \mathsf P \leq_W \mathsf Q \;\Rightarrow\; \mathsf P \leq_c \mathsf Q \;\Rightarrow\; \mathsf P \leq_\omega \mathsf Q, \\
\mathsf P \leq_{sW} \mathsf Q \;\Rightarrow\; \mathsf P \leq_{sc} \mathsf Q \;\Rightarrow\; \mathsf P \leq_c \mathsf Q.
\end{gathered}
$$
As for computable reducibility, $\mathsf P$ is uniformly true if and only if $\mathsf P \leq_W \mathsf{Id}$: given $\Phi$, take the identity as forward functional and $\Psi^{X \oplus Y} = \Phi^X$; given $\Phi$ and $\Psi$, the functional $X \mapsto \Psi^{X \oplus \Phi^X}$ solves $\mathsf P$.

:::proposition{#prop-rt12-not-uniform}
$\mathsf{RT}^1_2$ is computably true but not uniformly true. Consequently, $\mathsf{RT}^1_2 \leq_c \mathsf{RT}^1_1$ but $\mathsf{RT}^1_2 \not\leq_W \mathsf{RT}^1_1$.
:::

:::proof{of=prop-rt12-not-uniform}
A coloring $f : \nat \to 2$ computes both color classes, and one of them is infinite. Suppose that $\Phi^f$ is an infinite homogeneous set for every $f$. Let $f_0$ be the constant coloring $0$. The set $\Phi^{f_0}$ is infinite; take $x \in \Phi^{f_0}$, and let $u$ be the use of the computation $\Phi^{f_0}(x) = 1$. Let $v = \max(u, x + 1)$ and $f_1$ the coloring with $f_1(n) = 0$ for $n < v$ and $f_1(n) = 1$ for $n \geq v$. Since $f_1$ agrees with $f_0$ below $u$, we have $x \in \Phi^{f_1}$, and $f_1(x) = 0$. A homogeneous set for $f_1$ containing $x$ has color $0$, so it is included in $\{ 0, \dots, v - 1 \}$ and is finite: a contradiction. The problem $\mathsf{RT}^1_1$ is uniformly true, with $\Phi^f = \nat$, and a problem Weihrauch reducible to a uniformly true problem is uniformly true; this gives the consequence.
:::

The argument is a **continuity argument**: a functional decides each bit of its output from a finite part of its input, so it cannot wait for information that is only available in the limit. Most proofs of non-reducibility in the Weihrauch degrees have this form. Brattka and Rakotoniaina, and independently Hirschfeldt and Jockusch, showed more generally that $\mathsf{RT}^1_{k+1} \not\leq_W \mathsf{RT}^1_k$ for every $k \geq 1$; we admit this result. Likewise, the intermediate value theorem is not uniformly true, although every computable instance has a computable solution (:ref{#thm-ivt-rca}): the computation of a root must decide, from a finite approximation of the function, near which root to look.

:::quiz[uniformity]
In the proof of :ref{#prop-rt12-not-uniform}, why can $\Phi^{f_1}$ not avoid the element $x$?

- [x] Because the computation $\Phi^{f_0}(x) = 1$ reads only $f_0 \uh u$, which is also an initial segment of $f_1$; so $\Phi^{f_1}(x) = 1$ by the use principle.
- [ ] Because $x$ has color $0$ for $f_1$.

  The color of $x$ is what makes its presence harmful; its presence comes from the use principle.
- [ ] Because $\Phi^{f_1}$ is infinite.

  Infinity is required of the output; it does not force $x$ into it.

---

Why does the computable reduction of $\mathsf{RT}^1_2$ to $\mathsf{RT}^1_1$ not yield a Weihrauch reduction?

- [x] Because the backward computation must decide which color class is infinite, a $\Pi^0_2$ property of the instance; a computable reduction may choose a different algorithm for each instance, a Weihrauch reduction may not.
- [ ] Because $\mathsf{RT}^1_1$ has no computable instance.

  Every constant coloring is a computable instance.
- [ ] Because the color classes are not computable from the coloring.

  They are computable, uniformly; what is not computable is which one is infinite.
:::

## The omniscience principles

The following problems, from constructive mathematics, have instances in $\{0, 1\}^\nat$ and solutions in $\{ 0, 1 \}$, coded as sets: $0$ by $\emptyset$ and $1$ by $\{ 0 \}$, so that a solution is read from the first bit of its code.

:::definition{#def-lpo-llpo}
1. The **limited principle of omniscience** $\mathsf{LPO}$: an instance is a sequence $p \in \{0, 1\}^\nat$; its solution is $1$ if $p(n) = 1$ for some $n$, and $0$ otherwise.
2. The **lesser limited principle of omniscience** $\mathsf{LLPO}$: an instance is a sequence $p \in \{0, 1\}^\nat$ with $p(n) = 1$ for at most one $n$; its solutions are the $i \in \{ 0, 1 \}$ such that $p(2m + i) = 0$ for every $m$.
:::

An instance of $\mathsf{LLPO}$ has one solution if it contains a $1$, at a position of parity opposite to the solution, and two solutions otherwise. Both problems are computably true, since their solutions are numbers; their content is entirely about uniformity.

:::proposition{#prop-llpo-lpo}
$\mathsf{LLPO} \leq_W \mathsf{LPO}$, and $\mathsf{LLPO}$ is not uniformly true.
:::

:::proof{of=prop-llpo-lpo}
Let $\Phi^p = p$, and let $\Psi^{p \oplus i}$ output $0$ if $i = 0$; if $i = 1$, it searches for $n$ with $p(n) = 1$ and outputs $1$ if $n$ is even and $0$ if $n$ is odd. If $p$ has no $1$, both values are solutions; if $p(n) = 1$, the search terminates, and the output has the parity opposite to $n$, as required.

Suppose that $\Phi^p$ is a solution for every instance $p$. Let $i = \Phi^{0^\infty}(0)$, the bit that determines the solution, and $u$ the use of this computation. Let $p_0$ and $p_1$ be the sequences with a single $1$, at positions $2u$ and $2u + 1$ respectively. Both agree with $0^\infty$ below $u$, so $\Phi^{p_0}(0) = \Phi^{p_1}(0) = i$, and $\Phi^{p_0}$ and $\Phi^{p_1}$ both code the solution $i$. But the only solution to $p_0$ is $1$, and the only solution to $p_1$ is $0$.
:::

## Parallelization

:::definition{#def-parallelization}
The **parallelization** of a problem $\mathsf P$ is the problem $\widehat{\mathsf P}$ whose instances are the sequences $\bigoplus_n X_n$ of instances of $\mathsf P$, and whose solutions are the sequences $\bigoplus_n Y_n$ with $Y_n$ a solution to $X_n$ for every $n$.
:::

When the solutions of $\mathsf P$ are numbers in $\{ 0, 1 \}$, as for $\mathsf{LPO}$ and $\mathsf{LLPO}$, a solution $\bigoplus_n Y_n$ to $\widehat{\mathsf P}$ is identified with the set $\{ n : Y_n = \{ 0 \} \}$, the sequence of the values of the solutions. Each of the two codings is computable from the other, uniformly, so the identification does not affect Weihrauch reducibility.

If $\mathsf P \leq_W \mathsf Q$ via $\Phi$ and $\Psi$, then $\widehat{\mathsf P} \leq_W \widehat{\mathsf Q}$ via the functionals applying $\Phi$ and $\Psi$ to each coordinate. So parallelization is an operation on Weihrauch degrees. It turns the omniscience principles into familiar problems.

:::theorem{#thm-jump-lpo}
$\mathsf J \equiv_W \widehat{\mathsf{LPO}}$.
:::

:::proof{of=thm-jump-lpo}
($\mathsf J \leq_W \widehat{\mathsf{LPO}}$) Given $X$, let $\Phi^X = \bigoplus_e p_e$, with $p_e(s) = 1$ if $\Phi^X_e(e)[s]\converge$ and $0$ otherwise. The solution to $p_e$ is $1$ exactly when $e \in X'$, so the solution to $\Phi^X$ is $X'$, and $\Psi^{X \oplus Y} = Y$.

($\widehat{\mathsf{LPO}} \leq_W \mathsf J$) Let $\Phi$ be the identity. By the parameter theorem, uniformly in the oracle, there is a computable function $g$ such that for every $Z = \bigoplus_n p_n$, $\Phi^Z_{g(n)}(g(n))$ converges if and only if $p_n(s) = 1$ for some $s$. Let $\Psi^{Z \oplus Y}$ be the sequence whose $n$-th term is $Y(g(n))$. For $Y = Z'$, this is the sequence of solutions to the $p_n$.
:::

:::theorem{#thm-wkl-llpo}
$\mathsf{WKL} \equiv_W \widehat{\mathsf{LLPO}}$.
:::

:::proof{of=thm-wkl-llpo}
($\widehat{\mathsf{LLPO}} \leq_W \mathsf{WKL}$) Given $\bigoplus_n p_n$, let $T$ be the tree of strings $\sigma$ such that $p_n(2m + \sigma(n)) = 0$ for all $n, m$ with $n < |\sigma|$ and $2m + \sigma(n) < |\sigma|$. It is computable uniformly in the instance. It is infinite, since a sequence of solutions to the $p_n$ gives strings of every length in $T$, and its paths are exactly the sequences of solutions. So $\Psi^{X \oplus Y} = Y$ works.

($\mathsf{WKL} \leq_W \widehat{\mathsf{LLPO}}$) Let $T$ be an infinite binary tree. For a string $\sigma$ and $i < 2$, say that $\sigma^\frown i$ **dies at stage $s$** if $T$ has no extension of $\sigma^\frown i$ of length $|\sigma| + 1 + s$. Let $q_\sigma(2s + i) = 1$ if $s$ is the least stage at which one of $\sigma^\frown 0$, $\sigma^\frown 1$ dies, and $i$ is the least $j$ such that $\sigma^\frown j$ dies at $s$; all other values are $0$. Then $q_\sigma$ has at most one $1$, and $\Phi^T = \bigoplus_\sigma q_\sigma$, indexed by a computable enumeration of strings, is an instance of $\widehat{\mathsf{LLPO}}$.

Let $\bigoplus_\sigma i_\sigma$ be a solution. If $\sigma$ is **extendible**, that is, has extensions in $T$ of every length, then $\sigma^\frown i_\sigma$ is extendible. Indeed, one of the two successors is extendible. If one of them dies, $q_\sigma$ has a $1$ at $2s + i$ for the first one found dead, and $i_\sigma \neq i$, so $\sigma^\frown i_\sigma$ is the other successor, which does not die at the stage $s$; since $\sigma$ is extendible and $\sigma^\frown i$ is not, $\sigma^\frown i_\sigma$ is extendible. If none dies, both successors are extendible. Let $\Psi^{T \oplus Y}$ be the path $\rho_0 = \varepsilon$, $\rho_{k+1} = \rho_k {}^\frown i_{\rho_k}$. The empty string is extendible since $T$ is infinite, so every $\rho_k$ is extendible, and the limit is a path through $T$.
:::

:::corollary{#cor-lpo-not-llpo}
$\mathsf{LPO} \not\leq_W \mathsf{LLPO}$. So $\mathsf{LLPO} <_W \mathsf{LPO}$.
:::

:::proof{of=cor-lpo-not-llpo}
If $\mathsf{LPO} \leq_W \mathsf{LLPO}$, then $\widehat{\mathsf{LPO}} \leq_W \widehat{\mathsf{LLPO}}$, so $\mathsf J \leq_W \mathsf{WKL}$ by :ref{#thm-jump-lpo} and :ref{#thm-wkl-llpo}. This would give $\mathsf J \leq_\omega \mathsf{WKL}$, which fails by :ref{#cor-wkl-not-j}.
:::

The proof transfers a separation of ω-reducibility, obtained from the cone avoidance basis theorem, to a separation between two computably true problems, which ω-reducibility and computable reducibility do not distinguish. Parallelization thus connects the uniform world of Weihrauch reducibility with the non-uniform world of Turing degrees.

:::quiz[parallelization]
In the proof that $\mathsf{WKL} \leq_W \widehat{\mathsf{LLPO}}$, why is the instance $q_\sigma$ defined from the first stage at which a successor dies, rather than from the extendibility of the successors?

- [x] Because extendibility is a $\Pi^0_1$ property of the tree, not computable from it, while the instance must be computed uniformly; the first death is found by a search, and $\mathsf{LLPO}$ only needs to avoid the side found dead.
- [ ] Because both successors may die.

  If $\sigma$ is extendible, at most one successor dies; the definition handles the other cases arbitrarily.
- [ ] Because $\mathsf{LLPO}$ instances must have exactly one $1$.

  They may have none, in which case both answers are solutions.

---

Why does :ref{#cor-lpo-not-llpo} pass through the parallelizations?

- [x] Because $\mathsf{LPO}$ and $\mathsf{LLPO}$ are computably true, so ω-reducibility and computable reducibility do not separate them; their parallelizations are $\mathsf J$ and $\mathsf{WKL}$, which are separated in ω-models by the cone avoidance basis theorem.
- [ ] Because Weihrauch reducibility is only defined for parallel problems.

  It is defined for all problems.
- [ ] Because $\mathsf{LLPO}$ has two solutions on some instances.

  Multiple solutions are allowed in all reducibilities.
:::

## Exercises

::::exercise{difficulty=1}
Show that $\mathsf{LLPO} \leq_{sW} \mathsf{LPO}$.

:::solution
Let $\Phi^p$ be the sequence $q$ with $q(n) = 1$ if $p(2m) = 1$ for some $2m \leq n$, and $0$ otherwise; and $\Psi^i = i$. The solution to $q$ is $1$ exactly when $p$ has a $1$ at an even position. In that case, $1$ is the only solution to $p$. Otherwise, $p$ has no $1$ at an even position, so $0$ is a solution to $p$. The backward functional does not use $p$.
:::
::::

::::exercise{difficulty=1}
Show that if $\mathsf P$ is uniformly true, then $\widehat{\mathsf P}$ is uniformly true. Deduce from :ref{#thm-wkl-llpo} a second proof that $\mathsf{LLPO}$ is not uniformly true.

:::solution
If $\Phi^X$ solves $\mathsf P$, then the functional $\bigoplus_n X_n \mapsto \bigoplus_n \Phi^{X_n}$ solves $\widehat{\mathsf P}$. If $\mathsf{LLPO}$ were uniformly true, $\widehat{\mathsf{LLPO}}$ would be uniformly true, hence computably true, and so would $\mathsf{WKL} \leq_W \widehat{\mathsf{LLPO}}$. But some computable infinite binary tree has no computable path (:ref{#thm-dnc2-no-computable}).
:::
::::

::::exercise{difficulty=2}
For a problem $\mathsf P$ and $n \geq 1$, let $\mathsf P^n$ be the product of $n$ copies of $\mathsf P$. Show that if $\mathsf P$ is computably true, so is $\mathsf P^n$, and that $\mathsf J \not\leq_c \mathsf Q$ for every computably true problem $\mathsf Q$. Deduce that $\widehat{\mathsf{LPO}} \not\leq_W \mathsf{LPO}^n$ for every $n$: finitely many applications of $\mathsf{LPO}$ do not suffice.

:::solution
An instance $X_1 \oplus \cdots \oplus X_n$ of $\mathsf P^n$ computes each $X_i$, hence a solution $Y_i$ to each, hence $Y_1 \oplus \cdots \oplus Y_n$. If $\mathsf J \leq_c \mathsf Q$ with $\mathsf Q$ computably true, then for every $X$, the instance $\widetilde X \leq_T X$ has a solution $\widetilde Y \leq_T \widetilde X$, and $X \oplus \widetilde Y \leq_T X$ computes $X'$, which is impossible. Since $\mathsf{LPO}$ is computably true, so is $\mathsf{LPO}^n$; and $\widehat{\mathsf{LPO}} \leq_W \mathsf{LPO}^n$ would give $\mathsf J \leq_c \mathsf{LPO}^n$ by :ref{#thm-jump-lpo}.
:::
::::

## Notes and references

Weihrauch reducibility comes from computable analysis, where it was developed by Weihrauch, Brattka, Gherardi and Pauly; the handbook chapter of Brattka, Gherardi and Pauly is a survey. Gherardi and Marcone (2009), Dorais, Dzhafarov, Hirst, Mileti and Shafer (2016), Brattka and Rakotoniaina (2017) and Hirschfeldt and Jockusch (2016) developed its use for combinatorial principles.

- V. Brattka, G. Gherardi and A. Pauly, *Weihrauch complexity in computable analysis*, in Handbook of Computability and Complexity in Analysis, Springer, 2021, 367–417.
- G. Gherardi and A. Marcone, *How incomputable is the separable Hahn–Banach theorem?*, Notre Dame Journal of Formal Logic 50 (2009), 393–425.
- V. Brattka and T. Rakotoniaina, *On the uniform computational content of Ramsey's theorem*, Journal of Symbolic Logic 82 (2017), 1278–1316.
- F. G. Dorais, D. D. Dzhafarov, J. L. Hirst, J. R. Mileti and P. Shafer, *On uniform relationships between combinatorial problems*, Transactions of the American Mathematical Society 368 (2016), 1321–1359.
- D. R. Hirschfeldt and C. G. Jockusch, *On notions of computability-theoretic reduction between Π¹₂ principles*, Journal of Mathematical Logic 16 (2016), 1650002.
