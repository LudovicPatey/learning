---
title: Arithmetic genericity
summary: n-generic sets meet or avoid every Σ⁰ₙ set of strings; their n-th jump is computed from the set and the n-th jump of the empty set; they decide every Σ⁰ₙ property by a prefix; the hierarchy of genericity notions.
duration: 45
prerequisites: [one-genericity, arithmetic-hierarchy/post-theorem]
---

The notions of the previous lessons relativize. A set that is 1-generic relative to $\emptyset^{(n-1)}$ meets or avoids every $\Sigma^0_n$ set of strings, and this is enough to control its first $n$ jumps and to decide every $\Sigma^0_n$ property by a finite prefix. This lesson proves these facts, builds $n$-generic sets of the smallest possible complexity, and shows that the notions of genericity introduced in the course form a strict hierarchy.

The method is to iterate the lowness of 1-generic sets, one jump at a time, rather than to define a forcing relation for arithmetic formulas of every complexity. The forcing relation, due to Feferman, is the subject of the course on effective forcing; here it appears only through its consequence, :ref{#thm-n-generic-decides}.

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
The proof of the second half shows where the quantifier is spent: avoiding a $\Sigma^0_n$ set is a $\Pi^0_n$ condition, so the dense set $W \cup W^\perp$ is one level higher than $W$. None of the implications can be reversed; this is shown at the end of the lesson.

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

The hypothesis is used at the step from $k$ to $k+1$ only through genericity relative to $\emptyset^{(k)}$, which is why $n$-genericity controls exactly the first $n$ jumps. It cannot control more: the weakly $(n+1)$-generic set $A$ used at the end of the lesson is $n$-generic, and $A^{(n+1)} \not\equiv_T A \oplus \emptyset^{(n+1)}$.

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

Taking negations, the same holds for $\Pi^0_n$ properties. The restriction to $(n-1)$-generic extensions cannot be removed for $n \geq 2$: the $\Sigma^0_2$ property "$X$ is finite" fails for every 1-generic set, but every string has a finite extension, so no string has only infinite extensions. Some genericity of the extensions is needed to make the $\Pi^0_2$ property "$X$ is infinite" hold on all of them, since the dense sets that make a set infinite must be met.

:::example{#ex-n-generic-decides}
Let $G$ be 2-generic and consider the $\Sigma^0_2$ property "$\Phi^X_e$ is not total". By the theorem, if $\Phi^G_e$ is total, some prefix of $G$ makes $\Phi^X_e$ total for every 1-generic $X$ extending it. This can be seen directly. For each $x$, let $R_x = \{ \rho : \Phi^\rho_e(x)\converge \}$, and let $V$ be the set of strings $\tau$ that avoid some $R_x$; it is $\Sigma^0_2$. If $G$ met $V$, some prefix of $G$ would avoid some $R_x$, and $\Phi^G_e(x)$ would diverge. Since $G$ is 2-generic, some prefix $\sigma$ of $G$ therefore avoids $V$: no extension of $\sigma$ avoids any $R_x$. Let $X \succ \sigma$ be 1-generic and $x \in \nat$. No prefix of $X$ avoids $R_x$: a prefix extending $\sigma$ cannot, and a shorter prefix avoiding $R_x$ would make $\sigma$ avoid it too. So $X$ meets $R_x$, and $\Phi^X_e(x)\converge$.
:::

## n-generic sets below the n-th jump

:::theorem{#thm-low-generic-exists}
For every $n \geq 1$, there is an $n$-generic set $G \leq_T \emptyset^{(n)}$. Such a set satisfies $G^{(n)} \equiv_T \emptyset^{(n)}$.
:::

:::proof{of=thm-low-generic-exists}
Let $(W_e)$ be an enumeration of the $\Sigma^0_n$ sets of strings, uniform in the sense that $\{ (e, \tau) : \tau \in W_e \}$ is $\Sigma^0_n$; for instance $W_e$ is the $e$-th set of strings c.e. relative to $\emptyset^{(n-1)}$. Build $\sigma_0 = \varepsilon \preceq \sigma_1 \preceq \cdots$ with oracle $\emptyset^{(n)}$. At step $e$, ask whether $\sigma_e$ has an extension in $W_e$; this is a $\Sigma^0_n$ question, answered by $\emptyset^{(n)}$. If yes, search for such an extension $\tau$, using $\emptyset^{(n)}$ to decide membership in $W_e$, and let $\sigma_{e+1} = \tau\, 0$ for the first one found. If no, $\sigma_e$ avoids $W_e$, and $\sigma_{e+1} = \sigma_e\, 0$. The lengths increase strictly, so the limit $G$ is a set; it meets or avoids every $W_e$, so it is $n$-generic, and $G \leq_T \emptyset^{(n)}$. By :ref{#thm-generic-jumps}, $G^{(n)} \equiv_T G \oplus \emptyset^{(n)} \equiv_T \emptyset^{(n)}$.
:::

For $n = 1$, this is the existence of low 1-generic sets, already seen in the course on Turing degrees. A set $G$ with $G^{(n)} \equiv_T \emptyset^{(n)}$ is called **$\mathrm{low}_n$**. A set that is $n$-generic for every $n$ is **arithmetically generic**; the same construction, run for all $n$ at once with the oracle $\emptyset^{(\omega)} = \{ \langle n, x \rangle : x \in \emptyset^{(n)} \}$, gives an arithmetically generic set computable in $\emptyset^{(\omega)}$ (Downey and Hirschfeldt 2010, §2.24).

## Separating the notions

:::figure[The hierarchy of :ref{#prop-generic-hierarchy}, for the first two levels. Each arrow is an implication, and the set named below it shows that the converse fails.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The chain of implications: 2-generic implies weakly 2-generic implies 1-generic implies weakly 1-generic, with the sets separating each pair"><defs><marker id="gh-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="14" y="34" width="104" height="44" rx="6" class="state"/><text x="66.0" y="53" text-anchor="middle" class="label">weakly</text><text x="66.0" y="68" text-anchor="middle" class="label">1-generic</text><rect x="164" y="34" width="104" height="44" rx="6" class="state"/><text x="216.0" y="61" text-anchor="middle" class="label">1-generic</text><rect x="314" y="34" width="104" height="44" rx="6" class="state"/><text x="366.0" y="53" text-anchor="middle" class="label">weakly</text><text x="366.0" y="68" text-anchor="middle" class="label">2-generic</text><rect x="464" y="34" width="104" height="44" rx="6" class="state"/><text x="516.0" y="61" text-anchor="middle" class="label">2-generic</text><line x1="160" y1="56" x2="124" y2="56" class="ink-stroke" stroke-width="1.3" marker-end="url(#gh-arrow)"/><line x1="310" y1="56" x2="274" y2="56" class="ink-stroke" stroke-width="1.3" marker-end="url(#gh-arrow)"/><line x1="460" y1="56" x2="424" y2="56" class="ink-stroke" stroke-width="1.3" marker-end="url(#gh-arrow)"/><text x="578" y="60" class="mrm muted" font-size="16">⋯</text><line x1="141.0" y1="64" x2="141.0" y2="92" class="muted-stroke" stroke-width="1" stroke-dasharray="2 2"/><text x="141.0" y="106" text-anchor="middle" class="label">not conversely: a weakly 1-generic</text><text x="141.0" y="120" text-anchor="middle" class="label">set of degree 0′</text><line x1="291.0" y1="64" x2="291.0" y2="126" class="muted-stroke" stroke-width="1" stroke-dasharray="2 2"/><text x="291.0" y="140" text-anchor="middle" class="label">not conversely: a 1-generic</text><text x="291.0" y="154" text-anchor="middle" class="label">set computable in ∅′</text><line x1="441.0" y1="64" x2="441.0" y2="92" class="muted-stroke" stroke-width="1" stroke-dasharray="2 2"/><text x="441.0" y="106" text-anchor="middle" class="label">not conversely: a weakly 2-generic</text><text x="441.0" y="120" text-anchor="middle" class="label">set of jump degree 0″</text></svg>
:::

*Weak $(n+1)$-genericity is stronger than $n$-genericity.* By :ref{#thm-low-generic-exists}, there is an $n$-generic set computable in $\emptyset^{(n)}$, and by the relativization of :ref{#cor-delta2-weak-generic}, no weakly $(n+1)$-generic set is computable in $\emptyset^{(n)}$.

*$n$-genericity is stronger than weak $n$-genericity.* We use a theorem of Kurtz, admitted here: for every $n \geq 0$, there is a weakly $(n+1)$-generic set $A$ with $A^{(n)} \equiv_T \emptyset^{(n+1)}$ (Downey and Hirschfeldt 2010, Theorem 2.24.14; for $n = 0$ it says that some weakly 1-generic set has the degree of $\emptyset'$). Such a set is not $(n+1)$-generic. Indeed $A \leq_T A^{(n)} \equiv_T \emptyset^{(n+1)}$, so $A \oplus \emptyset^{(n+1)} \equiv_T \emptyset^{(n+1)}$, while $A^{(n+1)} \equiv_T \emptyset^{(n+2)}$; if $A$ were $(n+1)$-generic, :ref{#thm-generic-jumps} would give $A^{(n+1)} \equiv_T A \oplus \emptyset^{(n+1)}$, that is, $\emptyset^{(n+2)} \leq_T \emptyset^{(n+1)}$, which is false. For $n = 0$, the exercise on left-c.e. sets of the previous lesson gives another route, through the existence of a weakly 1-generic left-c.e. set, also admitted, and :ref{#thm-generic-not-dnc} a third one, since a set of the degree of $\emptyset'$ computes a DNC function.

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

The argument shows more generally: if $G$ is 1-generic relative to $Z$ and $C$ is c.e. in $Z$ but not computable in $Z$, then $C \not\leq_T G \oplus Z$. Unlike :ref{#thm-generic-cone}, this only requires genericity relative to $Z$, not relative to $C \oplus Z$. For $Z = \emptyset$, it says that a 1-generic set computes no non-computable c.e. set, a result of Jockusch and Posner (Soare 2016, Exercise 6.3.5); in particular no 1-generic set has c.e. degree.
:::
::::

## Notes and references

The forcing relation for arithmetic sentences, its definability for Cohen forcing (:ref{#thm-cohen-forcing-definable}) and the equivalence with the definition of n-genericity by dense sets (:ref{#thm-cohen-n-generic}) are treated in the course on effective forcing.

The arithmetic forcing relation was defined by Feferman (1965), and $n$-generic sets were studied systematically by Jockusch (1980), who proved most of the results of this lesson; the computation of the jumps is Theorem 2.24.3 of Downey and Hirschfeldt (2010). Kurtz (1981, 1983) introduced weak $n$-genericity, proved the implications of :ref{#prop-generic-hierarchy} and separated the notions (Downey and Hirschfeldt 2010, Theorems 2.24.11–2.24.14 and Corollary 2.24.20). Monin and Patey develop the forcing relation for arithmetic formulas and derive the same results from it.

- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana-Champaign, 1981.
- S. A. Kurtz, *Notions of weak genericity*, Journal of Symbolic Logic 48 (1983), 764–770.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.24.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §6.3.
- B. Monin and L. Patey, *Computability theory*, chapter *Cohen forcing*, sections on $\Sigma^0_n$ forcing and on arbitrarily generic sets.
