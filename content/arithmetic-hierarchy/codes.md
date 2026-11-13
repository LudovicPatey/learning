---
title: Codes for sets
summary: Indices of computable, c.e., finite and low sets; the information each kind of index provides, and fixed point arguments showing what cannot be recovered uniformly.
duration: 45
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

:::example{#ex-index-kinds}
1. The finite set $\{0, 2\}$ has canonical index $2^0 + 2^2 = 5$, so $D_5 = \{0, 2\}$; the empty set is $D_0$.
2. Let $a$ be an index of the program that outputs $1$ on $0$ and $2$, and $0$ elsewhere, and $b$ an index of the program that halts on $0$ and $2$ and runs forever elsewhere. Then $a$ is a $\Delta^0_1$ index and $b$ a $\Sigma^0_1$ index of $D_5$, and $a$ is not a $\Sigma^0_1$ index of $D_5$, since $W_a = \nat$.
3. Every index $e$ of a program that halts on no input is a $\Sigma^0_1$ index of $\emptyset$, and is not a $\Delta^0_1$ index of any set.
:::

The three kinds of index describe $D_5$ with decreasing information. From the canonical index $5$ one reads off the elements of $D_5$, and in particular that it has two elements and that $2$ is the largest. From $a$ one can decide membership of any given number, but not determine the size of the set, since one never knows whether a larger element remains. From $b$ one can only confirm membership, by waiting for the program to halt.

By :ref{#thm-post}, a set has a $\Sigma^0_{n+1}$ index if and only if it is $\Sigma^0_{n+1}$, and a $\Delta^0_{n+1}$ index if and only if it is $\Delta^0_{n+1}$. Conventions differ between books. Soare (Definition 4.2.4) defines a $\Sigma_n$ index of $B$, for $n \geq 1$, as an index of a one-one reduction of $B$ to $\emptyset^{(n)}$, and a $\Delta_n$ index as a pair formed of a $\Sigma_n$ index of $B$ and a $\Sigma_n$ index of its complement. The definitions above follow Monin and Patey. Every integer is a $\Sigma^0_1$ index of some set, but not every integer is a $\Delta^0_1$ index: the set of $\Delta^0_1$ indices is $\Pi^0_2$-complete (see the exercises). The notion of uniformity of the course on fundamentals can be expressed with indices.

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

The converse passages are not uniform. The proofs all have the same structure: a program, built with the fixed point theorem, waits for the alleged conversion procedure to answer about the program itself, and then behaves so as to make the answer wrong. This is the **diagonalization by self-reference** of the course on fundamentals, used there to prove Rice's theorem. Two points need care. The program must belong to the class on which the conversion is assumed to work, whatever the conversion does, so that its answer is guaranteed; and the program can only react to an answer after it has appeared, so its behavior before that point must already be acceptable.

:::figure[Conversions between kinds of indices. A solid arrow is a computable function that converts an index of one kind into an index of the other kind for the same set; a dashed arrow is a conversion that no partial computable function performs (:ref{#prop-no-size-from-delta}, :ref{#prop-no-delta-from-sigma} and :ref{#prop-no-lowness-index}).]
<svg class="fig" viewBox="0 0 600 205" width="600" role="img" aria-label="Conversions between kinds of indices: computable in one direction, not uniform in the other"><defs><marker id="ah-idx" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><rect x="7.0" y="30.0" width="136" height="40" rx="8" class="node"/><rect x="232.0" y="30.0" width="136" height="40" rx="8" class="node"/><rect x="457.0" y="30.0" width="136" height="40" rx="8" class="node"/><rect x="119.0" y="125.0" width="136" height="40" rx="8" class="node"/><rect x="344.0" y="125.0" width="136" height="40" rx="8" class="node"/><text x="75" y="55" text-anchor="middle" font-size="14">canonical index</text><text x="300" y="56" text-anchor="middle" font-size="17"><tspan class="mrm">Δ</tspan><tspan class="mrm" font-size="11" dy="-7">0</tspan><tspan class="mrm" font-size="11" dx="-6" dy="12">1</tspan><tspan font-size="14" dx="5" dy="-5">index</tspan></text><text x="525" y="56" text-anchor="middle" font-size="17"><tspan class="mrm">Σ</tspan><tspan class="mrm" font-size="11" dy="-7">0</tspan><tspan class="mrm" font-size="11" dx="-6" dy="12">1</tspan><tspan font-size="14" dx="5" dy="-5">index</tspan></text><text x="187" y="150" text-anchor="middle" font-size="14">lowness index</text><text x="412" y="151" text-anchor="middle" font-size="17"><tspan class="mrm">Δ</tspan><tspan class="mrm" font-size="11" dy="-7">0</tspan><tspan class="mrm" font-size="11" dx="-6" dy="12">2</tspan><tspan font-size="14" dx="5" dy="-5">index</tspan></text><line x1="146.0" y1="41" x2="227.0" y2="41" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-idx)"/><text x="186.5" y="35" text-anchor="middle" class="label">computable</text><line x1="229.0" y1="59" x2="148.0" y2="59" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 3" marker-end="url(#ah-idx)"/><text x="188.5" y="74" text-anchor="middle" class="label">not uniform</text><line x1="371.0" y1="41" x2="452.0" y2="41" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-idx)"/><text x="411.5" y="35" text-anchor="middle" class="label">computable</text><line x1="454.0" y1="59" x2="373.0" y2="59" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 3" marker-end="url(#ah-idx)"/><text x="413.5" y="74" text-anchor="middle" class="label">not uniform</text><line x1="258.0" y1="136" x2="339.0" y2="136" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-idx)"/><text x="298.5" y="130" text-anchor="middle" class="label">computable</text><line x1="341.0" y1="154" x2="260.0" y2="154" class="muted-stroke" stroke-width="1.3" stroke-dasharray="4 3" marker-end="url(#ah-idx)"/><text x="300.5" y="169" text-anchor="middle" class="label">not uniform</text><text x="300.0" y="199" text-anchor="middle" class="label">solid: a computable conversion; dashed: no partial computable conversion exists</text></svg>
:::

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

Codes of Turing ideals, and the computation of their members by a low code, are studied in the course on lowness (:ref{to="lowness/coded-ideals"}).

Canonical indices of finite sets are standard since Rogers' book; Nies calls them strong indices. Soare's *Turing Computability*, Section 2.3, studies the indices of finite and computable sets with a different terminology: what is called here a $\Delta^0_1$ index is his $\Delta_0$ index, or characteristic index, and his $\Delta_1$ index of $A$ is a pair formed of a $\Sigma_1$ index of $A$ and one of its complement. :ref{#prop-no-delta-from-sigma} is his Nonconversion Theorem 2.3.3, with the same proof, and :ref{#prop-no-size-from-delta} is equivalent to his Theorem 2.3.7 by his Exercise 2.3.13. The $\Sigma_n$ and $\Delta_n$ indices of higher levels are in his Definition 4.2.4. Lowness indices are used systematically in the constructions of low sets, for instance in the proofs of the low basis theorem and of the Sacks splitting theorem. The definitions and the two fixed point arguments for finite sets and lowness indices follow the section on arithmetic codes of Monin and Patey's book.

- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 2.3 and 4.2.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Arithmetic hierarchy*, section *Arithmetic codes*.
