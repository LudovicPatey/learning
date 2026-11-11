---
title: Codes for sets
summary: Indices of computable, c.e., finite and low sets; the information each kind of index provides, and fixed point arguments showing what cannot be recovered uniformly.
duration: 35
prerequisites: [post-theorem, fundamentals/fixed-point, turing-degrees/low-and-high]
---

Constructions in computability theory manipulate sets through finite descriptions: an index of a program computing the set, or enumerating it, or deciding it relative to $\emptyset'$. The same set has descriptions of several kinds, and they carry different amounts of information. An index of the characteristic function of a computable set tells more than an index of an enumeration of it; the list of the elements of a finite set tells more than an index of its characteristic function. This lesson defines the usual kinds of indices and proves, by fixed point arguments, that the passage from the poorer to the richer kinds is not uniform. Choosing the right kind of index is often the first decision in a construction.

## Kinds of indices

:::definition{#def-indices}
1. A **$\Delta^0_1$ index** of a set $A$ is an $e$ such that $\Phi_e$ is the characteristic function of $A$.
2. A **$\Sigma^0_1$ index** of $A$ is an $e$ such that $W_e = A$.
3. The **canonical index** of a finite set $F$ is $\sum_{x \in F} 2^x$. The finite set with canonical index $n$ is written $D_n$.
4. More generally, a **$\Delta^0_{n+1}$ index** of $A$ is an $e$ such that $\Phi^{\emptyset^{(n)}}_e$ is the characteristic function of $A$, and a **$\Sigma^0_{n+1}$ index** is an $e$ with $W^{\emptyset^{(n)}}_e = A$.
:::

By :ref{#thm-post}, a set has a $\Sigma^0_{n+1}$ index if and only if it is $\Sigma^0_{n+1}$, and a $\Delta^0_{n+1}$ index if and only if it is $\Delta^0_{n+1}$. Every integer is a $\Sigma^0_1$ index of some set, but not every integer is a $\Delta^0_1$ index: the set of $\Delta^0_1$ indices is $\Pi^0_2$-complete (see the exercises). The notion of uniformity of the course on fundamentals can be expressed with indices.

:::proposition{#prop-uniform-indices}
A sequence $(A_n)_{n \in \nat}$ of sets is uniformly computable if and only if there is a computable function $h$ such that $h(n)$ is a $\Delta^0_1$ index of $A_n$ for every $n$. Similarly, $(A_n)$ is uniformly c.e., that is, $\{ (n, x) : x \in A_n \}$ is c.e., if and only if $A_n = W_{h(n)}$ for some computable $h$.
:::

:::proof{of=prop-uniform-indices}
If $\chi(n, x)$ is the computable function deciding $x \in A_n$, the parameter form of SMN gives a computable $h$ with $\Phi_{h(n)}(x) = \chi(n, x)$. Conversely, if $h$ is computable and each $h(n)$ is a $\Delta^0_1$ index of $A_n$, then $\chi(n, x) = \Phi_{h(n)}(x)$ is computable by the universal function, and total. The c.e. case is the same, with domains in place of characteristic functions.
:::

:::proposition{#prop-canonical-indices}
The relations $x \in D_n$, $|D_n| = k$, $D_n \subseteq D_m$ and $\max D_n = x$ are computable. From the canonical index of a finite set one computes a $\Delta^0_1$ index and a $\Sigma^0_1$ index of it.
:::

:::proof{of=prop-canonical-indices}
$x \in D_n$ if and only if the binary digit of $n$ at position $x$ is $1$, that is, $\lfloor n / 2^x \rfloor$ is odd; and all elements of $D_n$ are smaller than $n + 1$, so the other relations are obtained by bounded quantification over $x \leq n$. The indices are obtained by the parameter form of SMN, applied to the computable functions $(n, x) \mapsto D_n(x)$ and to the partial function that converges on $(n, x)$ exactly when $x \in D_n$.
:::

## What cannot be recovered

The converse passages are not uniform. The proofs all have the same structure: a program, built with the fixed point theorem, waits for the alleged conversion procedure to answer about the program itself, and then behaves so as to make the answer wrong.

:::proposition{#prop-no-delta-from-sigma}
There is no partial computable function $f$ such that, for every $e$ with $W_e$ computable, $f(e)\converge$ and $f(e)$ is a $\Delta^0_1$ index of $W_e$.
:::

:::proof{of=prop-no-delta-from-sigma}
Suppose $f$ exists. By :ref{#cor-self-reference}, there is $e$ such that $\Phi_e(x)$ converges if and only if $x = 0$, $f(e)\converge$, and $\Phi_{f(e)}(0)\converge = 0$; the description is uniform in $e$, since $f$ and the universal function are partial computable. Then $W_e$ is $\{0\}$ or $\emptyset$, hence computable, so $f(e)\converge$ and $\Phi_{f(e)}$ is the characteristic function of $W_e$. If $\Phi_{f(e)}(0) = 0$, then $0 \in W_e$ by construction, while the characteristic function says $0 \notin W_e$. If $\Phi_{f(e)}(0) = 1$, then $W_e = \emptyset$, while the characteristic function says $0 \in W_e$. Both cases are contradictory.
:::

:::proposition{#prop-no-size-from-delta}
There is no partial computable function $f$ such that, for every $\Delta^0_1$ index $e$ of a finite set $F$, $f(e)\converge = |F|$.
:::

:::proof{of=prop-no-size-from-delta}
Suppose $f = \Phi_c$ exists. By :ref{#cor-self-reference}, there is $e$ such that for every $t$,
$$
\Phi_e(t) = \begin{cases} 1 & \text{if } t \text{ is the least stage with } f(e)[t]\converge, \text{ and } f(e) = 0,\\ 0 & \text{otherwise.} \end{cases}
$$
The conditions are decidable for each $t$, so $\Phi_e$ is total, with values in $\{0, 1\}$, and it is the characteristic function of a set $F$ with at most one element. So $e$ is a $\Delta^0_1$ index of a finite set, and $f(e)\converge = |F|$. If $f(e) = 0$, then $F$ contains the stage at which $f(e)$ converges, and $|F| = 1$. If $f(e) \geq 1$, then $F = \emptyset$ and $|F| = 0$. Both cases contradict $f(e) = |F|$.
:::

:::quiz[the fixed point arguments]
In the proof of :ref{#prop-no-delta-from-sigma}, why is $W_e$ computable whatever $f$ does?

- [x] Because $W_e$ is either $\{0\}$ or $\emptyset$: a finite set, hence computable, although we do not know which one.

  The argument only needs to know that $W_e$ satisfies the hypothesis, so that $f(e)$ must be correct.
- [ ] Because $f$ is total.

  $f$ is only assumed to converge on indices of computable sets.
- [ ] Because $e$ is a fixed point.

  The fixed point makes the self-reference possible; computability of $W_e$ comes from its being finite.

---

In the proof of :ref{#prop-no-size-from-delta}, why does the program $e$ wait for the least stage at which $f(e)$ converges, instead of computing $f(e)$ first?

- [x] Because $\Phi_e$ must be total to be a $\Delta^0_1$ index: it answers $0$ at every stage at which $f(e)$ has not yet converged.

  If $\Phi_e$ computed $f(e)$ first, it would be undefined everywhere in case $f(e)$ diverged, and $e$ would not be a $\Delta^0_1$ index.
- [ ] To make $F$ infinite.

  $F$ has at most one element.
- [ ] Because $f(e)$ diverges.

  Under the hypothesis on $f$, the argument shows that $f(e)$ converges.
:::

## Lowness indices

A low set $A$ is $\Delta^0_2$, so it has $\Delta^0_2$ indices. But lowness says more: $\emptyset'$ computes $A'$. An index carrying this information is a **lowness index**: an $e$ such that $\Phi^{\emptyset'}_e$ is the characteristic function of $A'$. From a lowness index, a $\Delta^0_2$ index is computable: by :ref{#thm-jump} there is a computable $g$, independent of the set, with $A(n) = A'(g(n))$ for every $A$, so if $\Phi^{\emptyset'}_e = A'$ then $n \mapsto \Phi^{\emptyset'}_e(g(n))$ computes $A$, with an index computable from $e$. The converse fails. Its proof uses the fixed point theorem for oracle machines.

:::lemma{#lem-relativized-fixed-point}
For every total computable $f$, there is $e$ such that $\Phi^X_{f(e)} = \Phi^X_e$ for every oracle $X$. Consequently, for every oracle machine computing a partial function $g(X, e, x)$, there is $e$ with $\Phi^X_e(x) \simeq g(X, e, x)$ for every $X$ and $x$.
:::

:::proof{of=lem-relativized-fixed-point}
The proof of :ref{#thm-fixed-point} uses only the universal function and the SMN theorem, which hold for oracle machines uniformly in the oracle (:ref{#thm-relativized-universal} and :ref{#thm-relativized-smn}). The same construction, with the functions $d$ and $f \circ d$ computable and independent of the oracle, gives a fixed point valid for every oracle. The second statement follows as :ref{#cor-self-reference} follows from the theorem.
:::

:::proposition{#prop-no-lowness-index}
There is no partial computable function $f$ such that, for every $\Delta^0_2$ index $e$ of a low set $A$, $f(e)\converge$ and $f(e)$ is a lowness index of $A$.
:::

:::proof{of=prop-no-lowness-index}
Suppose $f$ exists. By :ref{#thm-jump} applied to the uniformly $X$-c.e. set $\{ 0 : X \neq \emptyset \}$, there is $b$ such that $b \in X' \iff X \neq \emptyset$ for every $X$. By :ref{#lem-relativized-fixed-point}, there is $e$ such that for every oracle $Z$ and every $t$,
$$
\Phi^Z_e(t) = \begin{cases} 1 & \text{if } f(e)[t]\converge = i \text{ and } \Phi^Z_i(b)[t]\converge = 0 \text{ for some } i,\\ 0 & \text{otherwise.} \end{cases}
$$
With $Z = \emptyset'$, the function $\Phi^{\emptyset'}_e$ is total with values in $\{0, 1\}$; let $A$ be the set it computes. By monotonicity of stages, once the condition holds at some $t$, it holds at all larger $t$. So $A$ is empty or cofinite, hence computable and low, and $e$ is a $\Delta^0_2$ index of it. Hence $i = f(e)$ is defined and is a lowness index of $A$: $\Phi^{\emptyset'}_i(b) = A'(b)$, and $A'(b) = 1$ if and only if $A \neq \emptyset$. If $\Phi^{\emptyset'}_i(b) = 0$, then the condition holds for all large $t$, so $A \neq \emptyset$ and $A'(b) = 1$. If $\Phi^{\emptyset'}_i(b) = 1$, the condition never holds, so $A = \emptyset$ and $A'(b) = 0$. Both cases are contradictory.
:::

The information that distinguishes a lowness index from a $\Delta^0_2$ index is used in constructions that need to answer questions about $A'$ with the oracle $\emptyset'$ while $A$ is being built, for instance to iterate the construction of low sets.

## Exercises

::::exercise{difficulty=1}
Show that from a $\Delta^0_1$ index of $A$ one computes a $\Sigma^0_1$ index of $A$ and a $\Sigma^0_1$ index of $\nat \setminus A$.

:::solution
By the parameter form of SMN, there are computable $h_1$ and $h_0$ such that $\Phi_{h_i(e)}(x)$ converges if and only if $\Phi_e(x)\converge = i$. If $e$ is a $\Delta^0_1$ index of $A$, then $W_{h_1(e)} = A$ and $W_{h_0(e)} = \nat \setminus A$.
:::
::::

::::exercise{difficulty=2}
Show that the set $\{ e : e \text{ is a } \Delta^0_1 \text{ index of some set} \}$ is $\Pi^0_2$-complete.

:::solution
$e$ is a $\Delta^0_1$ index if and only if $\forall x\ \exists s\ (\Phi_e(x)[s]\converge \wedge \Phi_e(x)[s] \leq 1)$, a $\Pi^0_2$ condition. For completeness, let $A = \{ x : \forall y\ \exists z\ R(x, y, z) \}$ with $R$ computable, and let $f$ be computable with $\Phi_{f(x)}(y) \simeq 0$ if $\exists z\ R(x, y, z)$, the program searching for $z$ and diverging if there is none. Then $\Phi_{f(x)}$ is total, with values in $\{0, 1\}$, if and only if $x \in A$.
:::
::::

::::exercise{difficulty=2}
Show that there is no partial computable function $f$ such that, for every $\Sigma^0_1$ index $e$ of a finite set $F$, $f(e)\converge$ and $D_{f(e)} = F$.

:::solution
Suppose $f$ exists. By :ref{#cor-self-reference}, there is $e$ such that $\Phi_e(x)$ converges if and only if $x = 0$, $f(e)\converge$ and $0 \notin D_{f(e)}$. Then $W_e \subseteq \{0\}$ is finite, so $f(e)\converge$ with $D_{f(e)} = W_e$. If $0 \in D_{f(e)}$, then $W_e = \emptyset$, so $D_{f(e)} \neq W_e$. If $0 \notin D_{f(e)}$, then $W_e = \{0\}$, so $D_{f(e)} \neq W_e$. Both cases are contradictory.
:::
::::

## Notes and references

Canonical indices of finite sets are standard since Rogers' book. Lowness indices are used systematically in the constructions of low sets and low degrees, for instance in the proofs of the low basis theorem and of the Sacks splitting theorem; the examples of this lesson follow the presentation in Monin and Patey's book. Soare's textbook discusses the various kinds of indices.

- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.
