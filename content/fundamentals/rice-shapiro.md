---
title: The Rice–Shapiro theorem
summary: A c.e. index set is monotone and determined by finite information; the c.e. index sets are those given by c.e. lists of finite functions.
duration: 30
prerequisites: [rice-theorem]
---

By Rice's theorem, no non-trivial property of the function computed by a program is decidable. Some of them can nevertheless be **confirmed**: their index sets are computably enumerable. This lesson characterizes them. The answer is that a c.e. index set can only look at finitely many values of the function, and must accept every function that extends one it accepts. The necessity of these two conditions is proved by reductions from the complement of the halting set; their sufficiency, by a direct enumeration.

## Two necessary conditions

Some non-trivial index sets are c.e., for instance $\{ e : \Phi_e(3)\converge \}$ and $\{ e : W_e \neq \emptyset \}$; others are not, such as $\mathrm{Tot}$ (:ref{#cor-tot-not-ce}). The following theorem gives two necessary conditions. Heuristically, a c.e. index set accepts an index $e$ after a finite amount of computation, during which only finitely many values of $\Phi_e$ can have been observed. The proof makes this precise by reduction, with the technique of :ref{#prop-halting-variants}: a program is built that computes a function as long as a computation $\Phi_e(e)$ has not converged, and changes its behavior when it does. For partial functions, write $\theta \subseteq f$ if $f$ extends $\theta$, that is, $\theta(x)\converge = y$ implies $f(x)\converge = y$.

:::theorem[Rice–Shapiro, necessity]{#thm-rice-shapiro}
Let $\mathcal C$ be a class of unary partial computable functions such that $P = \{ e : \Phi_e \in \mathcal C \}$ is c.e. Then:

1. *(monotonicity)* if $f \in \mathcal C$ and $g$ is partial computable with $f \subseteq g$, then $g \in \mathcal C$;
2. *(finiteness)* if $f \in \mathcal C$, then some finite function $\theta \subseteq f$ belongs to $\mathcal C$.
:::

:::proof{of=thm-rice-shapiro}
In both cases, we reduce $\nat \setminus \emptyset'$ to $P$, which is impossible since $\nat \setminus \emptyset'$ is not c.e. (:ref{#thm-halting-ce}) while $P$ is (:ref{#prop-ce-downward}).

1. Suppose $f \in \mathcal C$, $f \subseteq g$, $g$ partial computable and $g \notin \mathcal C$. By :ref{#cor-smn-parameters}, there is a total computable $h$ such that the program $h(e)$, on input $x$, runs the computations of $f(x)$ and of $\Phi_e(e)$ in parallel, stage by stage: if $f(x)$ converges first (or at the same stage), it outputs $f(x)$; if $\Phi_e(e)$ converges first, it computes and outputs $g(x)$. If $e \notin \emptyset'$, the second case never occurs and $\Phi_{h(e)} = f \in \mathcal C$. If $e \in \emptyset'$, then $\Phi_{h(e)} = g$: on $x \in \mathrm{dom}(f)$, both cases give $f(x) = g(x)$; on $x \notin \mathrm{dom}(f)$, only the second case can occur, and gives $g(x)$. So $\Phi_{h(e)} \notin \mathcal C$, and $h$ reduces $\nat \setminus \emptyset'$ to $P$.
2. Suppose $f \in \mathcal C$ and no finite $\theta \subseteq f$ is in $\mathcal C$. Let $h$ be total computable such that $\Phi_{h(e)}(x) \simeq f(x)$ if $\Phi_e(e)[x]\diverge$, and $\Phi_{h(e)}(x)$ is undefined otherwise. If $e \notin \emptyset'$, then $\Phi_{h(e)} = f \in \mathcal C$. If $e \in \emptyset'$, let $s$ be the least stage with $\Phi_e(e)[s]\converge$; then $\Phi_{h(e)}$ is the restriction of $f$ to $\{0, \dots, s - 1\}$, a finite function contained in $f$, hence not in $\mathcal C$. So $h$ reduces $\nat \setminus \emptyset'$ to $P$.
:::

:::quiz[Rice–Shapiro]
In part 1 of the proof, why are the computations of $f(x)$ and $\Phi_e(e)$ run in parallel, rather than computing $\Phi_e(e)$ first?

- [x] If $e \notin \emptyset'$, the program must still compute $f$; waiting for $\Phi_e(e)$ would make it diverge everywhere.
- [ ] To make $h$ total.

  $h$ is total by SMN, whatever the program described.
- [ ] Because $f$ is total.

  $f$ is not assumed total.

---

The set $\{ e : W_e \neq \emptyset \}$ is c.e. How does it satisfy the two conditions?

- [x] A function with non-empty domain has a one-point subfunction with non-empty domain, and every extension of it has non-empty domain.
- [ ] It does not satisfy them, which shows that the conditions are not necessary.

  The conditions are necessary: they hold for every c.e. index set.
- [ ] Only finiteness holds.

  Monotonicity holds too: extending a function enlarges its domain.
:::

## The characterization

The two conditions characterize the c.e. index sets. To state this, finite functions are coded by integers. The **canonical index** of a finite set $F \subseteq \nat$ is $\sum_{z \in F} 2^z$. A finite function $\theta$ is coded by the canonical index of $\{ \langle x, y \rangle : \theta(x)\converge = y \}$, and we write $\theta_n$ for the finite function of code $n$. The set of codes of finite functions and the relation $\theta_n(x)\converge = y$ are computable, since they only require reading the binary expansion of $n$ and inverting the pairing function.

:::theorem[Rice–Shapiro]{#thm-rice-shapiro-converse}
Let $\mathcal C$ be a class of unary partial computable functions. The index set $P = \{ e : \Phi_e \in \mathcal C \}$ is c.e. if and only if there is a c.e. set $D$ of codes of finite functions such that, for every partial computable $f$,
$$
f \in \mathcal C \iff \theta_n \subseteq f \text{ for some } n \in D.
$$
:::

:::proof{of=thm-rice-shapiro-converse}
($\Leftarrow$) Let $(D_s)$ be a c.e. approximation of $D$. Then $e \in P$ if and only if there are $n$ and $s$ with $n \in D_s$ and $\Phi_e(x)[s]\converge = \theta_n(x)$ for every $x \in \mathrm{dom}(\theta_n)$. The condition on $n$ and $s$ is computable, since $\mathrm{dom}(\theta_n)$ is a finite set computed from $n$ and the stage relation is computable (:ref{#prop-stage-properties}). So $P$ is the projection of a computable relation, and it is c.e. by :ref{#thm-ce-characterizations}.

($\Rightarrow$) By :ref{#cor-smn-parameters}, there is a total computable $k$ such that $\Phi_{k(n)} = \theta_n$ for every code $n$ of a finite function: the program $k(n)$ looks up its input in the finite table coded by $n$, outputs the value if there is one, and loops otherwise. Let $D$ be the set of codes $n$ of finite functions with $\theta_n \in \mathcal C$, that is, with $k(n) \in P$. It is the intersection of a computable set with $k^{-1}(P)$, hence c.e. by :ref{#prop-ce-closure}. If $f \in \mathcal C$, some finite $\theta \subseteq f$ belongs to $\mathcal C$ by finiteness (:ref{#thm-rice-shapiro}), and its code is in $D$. Conversely, if $\theta_n \subseteq f$ with $n \in D$, then $\theta_n \in \mathcal C$, and $f \in \mathcal C$ by monotonicity.
:::

In other words, a property of programs that can be confirmed is a property that is confirmed by finitely many values of the function computed, from a computable list of finite patterns. This is the form taken in computability theory by the principle that computable operations are continuous, which reappears with oracles and in computable analysis.

## Examples

The necessary conditions are the practical tool: to show that an index set is not c.e., exhibit a function of the class with an extension outside it, or an infinite function of the class with no finite part in it.

:::corollary{#cor-rice-shapiro-examples}
The following index sets are not c.e.: $\mathrm{Tot}$; $\{ e : W_e \text{ is infinite} \}$; $\{ e : W_e \text{ is finite} \}$; $\{ e : W_e = \emptyset \}$; $\{ e : \Phi_e = \Phi_a \}$ for any index $a$ of a total function.
:::

:::proof{of=cor-rice-shapiro-examples}
For $\mathrm{Tot}$, $\{ e : W_e \text{ infinite} \}$ and $\{ e : \Phi_e = \Phi_a \}$ with $\Phi_a$ total, finiteness fails: these classes contain an infinite function, total or with infinite domain, but no finite function. For $\{ e : W_e \text{ finite} \}$ and $\{ e : W_e = \emptyset \}$, monotonicity fails: the nowhere defined function belongs to the class, and its extension the constant function $0$ does not.
:::

## Exercises

::::exercise{difficulty=1}
Is $\{ e : \Phi_e(0)\converge \text{ and } \Phi_e(1)\diverge \}$ c.e.?

:::solution
No. It is an index set, and monotonicity fails: the function defined only at $0$ belongs to the class, and its extension defined at $0$ and $1$ does not. By :ref{#thm-rice-shapiro}, the set is not c.e.
:::
::::

::::exercise{difficulty=2}
Show that $\{ e : W_e \text{ is computable} \}$ is not c.e.

:::solution
It is an index set. Monotonicity fails: the nowhere defined function has the computable domain $\emptyset$, while its extension $g(x) \simeq 0$ if $x \in \emptyset'$, undefined otherwise, is partial computable with domain $\emptyset'$, which is not computable. By :ref{#thm-rice-shapiro}, the set is not c.e.
:::
::::

::::exercise{difficulty=2 #ex-rice-shapiro-sets}
(Rice–Shapiro for c.e. sets.) Let $\mathcal A$ be a class of c.e. sets such that $\{ e : W_e \in \mathcal A \}$ is c.e. Show that if $A \in \mathcal A$ and $B \supseteq A$ is c.e., then $B \in \mathcal A$, and that every $A \in \mathcal A$ has a finite subset in $\mathcal A$.

:::hint
Apply :ref{#thm-rice-shapiro} to the class of partial computable functions whose domain is in $\mathcal A$.
:::

:::solution
Let $\mathcal C = \{ f \text{ partial computable} : \mathrm{dom}(f) \in \mathcal A \}$. Its index set $\{ e : W_e \in \mathcal A \}$ is c.e., so $\mathcal C$ satisfies the two conditions of :ref{#thm-rice-shapiro}. Let $A \in \mathcal A$ and $B \supseteq A$ be c.e. The partial functions $f$ and $g$ equal to $0$ on $A$ and on $B$ respectively, and undefined elsewhere, are partial computable, with $f \in \mathcal C$ and $f \subseteq g$. By monotonicity $g \in \mathcal C$, that is, $B \in \mathcal A$. By finiteness, some finite $\theta \subseteq f$ belongs to $\mathcal C$; its domain is a finite subset of $A$ that belongs to $\mathcal A$.
:::
::::

## Notes and references

The characterization of the classes of c.e. sets whose index set is c.e. was obtained independently by Rice and by Shapiro in 1956; the c.e. lists of finite sets in Rice's statement are its "key arrays". The version for classes of partial computable functions proved here implies the version for c.e. sets, by :ref{#ex-rice-shapiro-sets}. A related result is the Myhill–Shepherdson theorem (1955): effective operations on partial computable functions are continuous, in the sense that their values depend on finitely many values of their argument. Rogers' and Odifreddi's books contain many further results on index sets, whose exact complexity is determined in the course on the arithmetic hierarchy.

- H. G. Rice, *On completely recursively enumerable classes and their key arrays*, Journal of Symbolic Logic 21 (1956), 304–308.
- N. Shapiro, *Degrees of computability*, Transactions of the American Mathematical Society 82 (1956), 281–299.
- J. Myhill and J. C. Shepherdson, *Effective operations on partial recursive functions*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 1 (1955), 310–317.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989.
