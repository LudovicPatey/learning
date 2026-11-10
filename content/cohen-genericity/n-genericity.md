---
title: Arithmetic genericity
summary: n-generic sets meet or avoid every Σ⁰ₙ set of strings; their n-th jump is computed from the set and the n-th jump of the empty set; they decide every Σ⁰ₙ property by a prefix; the hierarchy of genericity notions.
duration: 35
prerequisites: [one-genericity, arithmetic-hierarchy/post-theorem]
---

The notions of the previous lessons relativize. A set that is 1-generic relative to $\emptyset^{(n-1)}$ meets or avoids every $\Sigma^0_n$ set of strings, and this is enough to control its first $n$ jumps and to decide every $\Sigma^0_n$ property by a finite prefix. This lesson proves these facts, compares the notions of genericity introduced in the course, and builds $n$-generic sets of the smallest possible complexity.

Recall from :ref{#def-relative-genericity} that $G$ is **$n$-generic**, for $n \geq 1$, if it is 1-generic relative to $\emptyset^{(n-1)}$; by Post's theorem, the $\emptyset^{(n-1)}$-c.e. sets of strings are exactly the $\Sigma^0_n$ ones. Every set is considered **$0$-generic**.

## Comparison of the notions

:::proposition{#prop-generic-hierarchy}
For every $n \geq 1$, every $n$-generic set is weakly $n$-generic, and every weakly $(n+1)$-generic set is $n$-generic.
:::

:::proof{of=prop-generic-hierarchy}
If $W$ is a dense $\Sigma^0_n$ set of strings, no string avoids $W$, so $W^\perp = \emptyset$, and an $n$-generic set meets $W \cup W^\perp = W$.

Let $G$ be weakly $(n+1)$-generic and $W$ a $\Sigma^0_n$ set of strings. The set $W^\perp = \{ \sigma : \forall \tau \succeq \sigma\ \tau \notin W \}$ is $\Pi^0_n$. So $W \cup W^\perp$ is the union of a $\Sigma^0_n$ and a $\Pi^0_n$ set, hence $\Delta^0_{n+1}$, in particular $\Sigma^0_{n+1}$. It is dense. So $G$ meets it.
:::

This gives the chain
$$
\text{weakly 1-generic} \Leftarrow \text{1-generic} \Leftarrow \text{weakly 2-generic} \Leftarrow \text{2-generic} \Leftarrow \cdots
$$
None of these implications can be reversed. For the implications from weak $(n+1)$-genericity to $n$-genericity, this follows from :ref{#thm-low-generic-exists} below together with the relativization of :ref{#cor-delta2-weak-generic}: there is an $n$-generic set computable in $\emptyset^{(n)}$, and no weakly $(n+1)$-generic set is computable in $\emptyset^{(n)}$. For the implications from $n$-genericity to weak $n$-genericity, the separation is due to Kurtz and is admitted here. For $n = 1$, it follows from two results also admitted: every hyperimmune degree contains a weakly 1-generic set (Kurtz), so some weakly 1-generic set has c.e. degree, while no 1-generic set has c.e. degree (Jockusch).

## The jumps of an n-generic set

The lowness property of 1-generic sets relativizes.

:::lemma{#lem-relative-generic-low}
If $G$ is 1-generic relative to $A$, then $(G \oplus A)' \leq_T G \oplus A'$.
:::

:::proof{of=lem-relative-generic-low}
For each $e$, let $W_e = \{ \sigma : \Phi^{\sigma \oplus A}_e(e)\converge \}$, where the computation with oracle $\sigma \oplus A$ only queries the $G$-side below $|\sigma|$. The sets $W_e$ are $A$-c.e., uniformly in $e$. Since $G$ is 1-generic relative to $A$, it has a prefix in $W_e$ or a prefix avoiding $W_e$. Both questions are decided by $A'$, uniformly in $e$ and in the prefix: "$\sigma \in W_e$" is $\Sigma^0_1(A)$, and "$\sigma$ avoids $W_e$" is $\Pi^0_1(A)$. With oracle $G \oplus A'$, search through the prefixes $G \uh k$ for one that is in $W_e$ or avoids $W_e$; the search terminates. In the first case $\Phi^{G \oplus A}_e(e)$ converges; in the second case, it diverges, since a convergent computation would have its $G$-use below some $k' \geq |G \uh k|$, and $G \uh k'$ would be an extension of $G \uh k$ in $W_e$.
:::

:::theorem{#thm-generic-jumps}
Let $n \geq 1$ and let $G$ be $n$-generic. Then $G^{(k)} \equiv_T G \oplus \emptyset^{(k)}$ for every $k \leq n$.
:::

:::proof{of=thm-generic-jumps}
By induction on $k$. For $k = 0$ there is nothing to prove. Let $k < n$ and suppose $G^{(k)} \equiv_T G \oplus \emptyset^{(k)}$. The jump is invariant under Turing equivalence, so $G^{(k+1)} \equiv_T (G \oplus \emptyset^{(k)})'$. Since $k \leq n - 1$, $G$ is 1-generic relative to $\emptyset^{(k)}$: indeed it is 1-generic relative to $\emptyset^{(n-1)}$, and every $\emptyset^{(k)}$-c.e. set is $\emptyset^{(n-1)}$-c.e. By :ref{#lem-relative-generic-low} with $A = \emptyset^{(k)}$, $(G \oplus \emptyset^{(k)})' \leq_T G \oplus \emptyset^{(k+1)}$. Conversely, $G \leq_T (G \oplus \emptyset^{(k)})'$ and $\emptyset^{(k+1)} \leq_T (G \oplus \emptyset^{(k)})'$, since the jump of a set computes the jump of every set below it. Hence $G^{(k+1)} \equiv_T G \oplus \emptyset^{(k+1)}$.
:::

The hypothesis is used at the step from $k$ to $k+1$ only through genericity relative to $\emptyset^{(k)}$, which is why $n$-genericity controls exactly the first $n$ jumps.

:::quiz[the jumps of an n-generic set]
In the induction step of :ref{#thm-generic-jumps}, where is the hypothesis $k < n$ used?

- [x] To know that $G$ is 1-generic relative to $\emptyset^{(k)}$, which is needed to apply :ref{#lem-relative-generic-low}.
- [ ] To know that $\emptyset^{(k+1)} \leq_T (G \oplus \emptyset^{(k)})'$.

  This holds for every set $G$ and every $k$.
- [ ] To know that the jump is invariant under Turing equivalence.

  This holds for all sets.

---

In the proof of :ref{#lem-relative-generic-low}, why does the search need the oracle $G$ and not only $A'$?

- [x] Because it examines the prefixes of $G$; $A'$ alone decides, for a given string, whether it is in $W_e$ or avoids $W_e$, but does not know which strings are prefixes of $G$.
- [ ] Because $W_e$ is not $A$-c.e.

  It is $A$-c.e., uniformly in $e$.
- [ ] Because the question "$\sigma$ avoids $W_e$" is not decided by $A'$.

  It is a $\Pi^0_1(A)$ question, decided by $A'$.
:::

## Deciding Σ⁰ₙ properties

A **$\Sigma^0_n$ property** of sets is a property $P(X)$ defined by a $\Sigma^0_n$ formula of arithmetic with a set parameter $X$. By the relativized form of Post's theorem, there is an index $e$ such that $P(X)$ holds if and only if $\Phi^{X^{(n-1)}}_e(0)\converge$, for every set $X$. For $(n-1)$-generic sets, the oracle $X^{(n-1)}$ can be replaced by $X \oplus \emptyset^{(n-1)}$, and 1-genericity relative to $\emptyset^{(n-1)}$ decides the resulting $\Sigma^0_1(\emptyset^{(n-1)})$ property.

:::theorem{#thm-n-generic-decides}
Let $n \geq 1$, let $P$ be a $\Sigma^0_n$ property, and let $G$ be $n$-generic. There is a prefix $\sigma$ of $G$ such that either every $(n-1)$-generic set extending $\sigma$ satisfies $P$, or no $(n-1)$-generic set extending $\sigma$ satisfies $P$. In particular, $P(G)$ holds if and only if $P$ holds for every $(n-1)$-generic set extending some prefix of $G$.
:::

:::proof{of=thm-n-generic-decides}
Let $e$ be such that $P(X) \iff \Phi^{X^{(n-1)}}_e(0)\converge$ for every $X$. The reduction $X^{(n-1)} \leq_T X \oplus \emptyset^{(n-1)}$ of :ref{#thm-generic-jumps}, for $(n-1)$-generic sets $X$, is given by a procedure that does not depend on $X$: the proof of :ref{#lem-relative-generic-low} describes it uniformly, and the induction composes these procedures. So there is an index $d$ such that $P(X) \iff \Phi^{X \oplus \emptyset^{(n-1)}}_d(0)\converge$ for every $(n-1)$-generic set $X$. For $n = 1$ we take $d = e$, and the equivalence holds for every set.

Let $W = \{ \tau : \Phi^{\tau \oplus \emptyset^{(n-1)}}_d(0)\converge \}$, a $\Sigma^0_n$ set of strings. Since $G$ is $n$-generic, it has a prefix $\sigma \in W$ or a prefix $\sigma$ avoiding $W$. In the first case, every set $X \succ \sigma$ satisfies $\Phi^{X \oplus \emptyset^{(n-1)}}_d(0)\converge$, so every $(n-1)$-generic $X \succ \sigma$ satisfies $P$. In the second case, no $X \succ \sigma$ satisfies $\Phi^{X \oplus \emptyset^{(n-1)}}_d(0)\converge$, since a convergent computation would place a prefix of $X$ extending $\sigma$ in $W$; so no $(n-1)$-generic $X \succ \sigma$ satisfies $P$. Since $G$ is itself $(n-1)$-generic and extends $\sigma$, $P(G)$ holds exactly in the first case.
:::

Taking negations, the same holds for $\Pi^0_n$ properties. The restriction to $(n-1)$-generic extensions cannot be removed for $n \geq 2$: the $\Sigma^0_2$ property "$X$ is finite" fails for every 1-generic set, but every string has a finite extension, so no string has only infinite extensions.

## n-generic sets below the n-th jump

:::theorem{#thm-low-generic-exists}
For every $n \geq 1$, there is an $n$-generic set $G \leq_T \emptyset^{(n)}$. Such a set satisfies $G^{(n)} \equiv_T \emptyset^{(n)}$.
:::

:::proof{of=thm-low-generic-exists}
Let $(W_e)$ be an enumeration of the $\Sigma^0_n$ sets of strings, uniform in the sense that $\{ (e, \tau) : \tau \in W_e \}$ is $\Sigma^0_n$; for instance $W_e$ is the $e$-th set of strings c.e. relative to $\emptyset^{(n-1)}$. Build $\sigma_0 = \varepsilon \preceq \sigma_1 \preceq \cdots$ with oracle $\emptyset^{(n)}$. At step $e$, ask whether $\sigma_e$ has an extension in $W_e$; this is a $\Sigma^0_n$ question, answered by $\emptyset^{(n)}$. If yes, search for such an extension, using $\emptyset^{(n)}$ to decide membership in $W_e$, and let $\sigma_{e+1}$ be the first one found. If no, $\sigma_e$ avoids $W_e$, and $\sigma_{e+1} = \sigma_e\, 0$. The limit $G$ meets or avoids every $W_e$, so it is $n$-generic, and $G \leq_T \emptyset^{(n)}$. By :ref{#thm-generic-jumps}, $G^{(n)} \equiv_T G \oplus \emptyset^{(n)} \equiv_T \emptyset^{(n)}$.
:::

For $n = 1$, this is the existence of low 1-generic sets, already seen in the course on Turing degrees. A set $G$ with $G^{(n)} \equiv_T \emptyset^{(n)}$ is called **$\mathrm{low}_n$**.

## Exercises

::::exercise{difficulty=1}
A set $G$ is **$\mathrm{GL}_n$** if $G^{(n)} \equiv_T (G \oplus \emptyset')^{(n-1)}$. Show that every $n$-generic set is $\mathrm{GL}_n$.

:::solution
Since $G \oplus \emptyset' \leq_T G'$, we have $(G \oplus \emptyset')^{(n-1)} \leq_T G^{(n)}$ for every set. Conversely, $G \leq_T (G \oplus \emptyset')^{(n-1)}$ and $\emptyset^{(n)} = (\emptyset')^{(n-1)} \leq_T (G \oplus \emptyset')^{(n-1)}$, so by :ref{#thm-generic-jumps}, $G^{(n)} \equiv_T G \oplus \emptyset^{(n)} \leq_T (G \oplus \emptyset')^{(n-1)}$.
:::
::::

::::exercise{difficulty=2}
Let $G$ be 2-generic. Show that $G$ is not computable in $\emptyset'$, and that $G$ is not high, that is, $\emptyset'' \not\leq_T G'$.

:::hint
For a Turing functional $\Phi_e$, consider the set of strings $\tau$ such that $\Phi^{\tau \oplus \emptyset'}_e(x)\converge = 0$ for some $x \in \emptyset''$.
:::

:::solution
By :ref{#prop-generic-hierarchy}, a 2-generic set is weakly 2-generic, so it is not computable in $\emptyset'$ by :ref{#cor-delta2-weak-generic}.

By :ref{#thm-generic-jumps}, $G' \equiv_T G \oplus \emptyset'$, so it suffices to show $\Phi^{G \oplus \emptyset'}_e \neq \emptyset''$ for every $e$. Let
$$
U_e = \{ \tau : \exists x\ (\Phi^{\tau \oplus \emptyset'}_e(x)\converge = 0 \text{ and } x \in \emptyset'') \}.
$$
The first condition is $\Sigma^0_1(\emptyset')$, hence $\Sigma^0_2$, and $\emptyset''$ is $\Sigma^0_2$, so $U_e$ is $\Sigma^0_2$. If $G$ meets $U_e$, then $\Phi^{G \oplus \emptyset'}_e(x) = 0$ for some $x \in \emptyset''$, so $\Phi^{G \oplus \emptyset'}_e \neq \emptyset''$. Otherwise some prefix $\sigma$ of $G$ avoids $U_e$. Suppose, for a contradiction, that $\Phi^{G \oplus \emptyset'}_e = \emptyset''$. Then
$$
x \notin \emptyset'' \iff \exists \tau \succeq \sigma\ \Phi^{\tau \oplus \emptyset'}_e(x)\converge = 0.
$$
Indeed, if $x \notin \emptyset''$, a long enough prefix of $G$ gives the value $0$; if $x \in \emptyset''$, no extension of $\sigma$ gives $0$, since $\sigma$ avoids $U_e$. The right-hand side is $\Sigma^0_1(\emptyset')$, so the complement of $\emptyset''$ is $\Sigma^0_2$, and $\emptyset''$ is $\Delta^0_2$, that is, computable in $\emptyset'$. This contradicts the hierarchy theorem.

The argument shows more generally: if $G$ is 1-generic relative to $Z$ and $C$ is c.e. in $Z$ but not computable in $Z$, then $C \not\leq_T G \oplus Z$.
:::
::::

## Notes and references

The arithmetic forcing relation was defined by Feferman (1965), and $n$-generic sets were studied systematically by Jockusch (1980), who proved most of the results of this lesson. Kurtz (1981) introduced weak $n$-genericity and separated it from $n$-genericity. Jockusch showed that 1-generic degrees are never c.e.; Kurtz showed that every hyperimmune degree contains a weakly 1-generic set.

- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana-Champaign, 1981.
