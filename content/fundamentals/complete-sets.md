---
title: Closure properties and complete sets
summary: Closure properties of the c.e. sets, the selection and graph theorems, and the m-completeness of the halting set.
duration: 35
prerequisites: [ce-sets]
---

By :ref{#thm-ce-characterizations}, a c.e. set is the projection of a computable relation: an element belongs to it when some witness exists, and witnesses can be searched for. This lesson draws two kinds of consequences from that representation. The first are closure properties: unions, intersections, projections, bounded universal quantifiers and preimages of c.e. sets are c.e., and a partial computable function can select a witness for each element. Each proof is a dovetailed search, as in the previous lesson. The second is the position of the halting set among c.e. sets: every c.e. set many-one reduces to it. Together with the reductions of the lesson on the halting problem, this gives the first examples of sets that are neither c.e. nor co-c.e.

## Closure properties

:::proposition{#prop-ce-closure}
1. If $A$ and $B$ are c.e., so are $A \cup B$ and $A \cap B$.
2. If $R \subseteq \nat^{k+1}$ is c.e., so is its projection $\{ \vec x : \exists y\ R(\vec x, y) \}$.
3. If $R \subseteq \nat^{k+1}$ is c.e., so is $\{ (\vec x, y) : \forall z < y\ R(\vec x, z) \}$.
4. If $A$ is c.e. and $f$ is partial computable, then $f^{-1}(A) = \{ x : f(x)\converge \in A \}$ and $f(A) = \{ f(x) : x \in A,\ f(x)\converge \}$ are c.e.
:::

:::proof{of=prop-ce-closure}
By :ref{#thm-ce-characterizations}, write each c.e. set or relation as the projection of a computable relation, using a c.e. approximation for item 3.

1. If $x \in A \iff \exists s\ P(x, s)$ and $x \in B \iff \exists t\ Q(x, t)$, then $x \in A \cup B \iff \exists s\ (P(x, s) \vee Q(x, s))$, and $x \in A \cap B \iff \exists n\ (P(x, \pi_0(n)) \wedge Q(x, \pi_1(n)))$.
2. If $R(\vec x, y) \iff \exists s\ Q(\vec x, y, s)$, then $\exists y\ R(\vec x, y) \iff \exists n\ Q(\vec x, \pi_0(n), \pi_1(n))$.
3. Let $(R_s)$ be a c.e. approximation of $R$. Then $\forall z < y\ R(\vec x, z)$ holds if and only if $\exists s\ \forall z < y\ R_s(\vec x, z)$. Indeed, if each $z < y$ has a stage $s_z$ with $R_{s_z}(\vec x, z)$, then $s = \max_{z < y} s_z$ works since the approximation is increasing; the converse is clear. The relation $\forall z < y\ R_s(\vec x, z)$ of $\vec x, y, s$ is computable, by bounded quantification (:ref{#prop-computable-closure}).
4. Let $f = \Phi_i$ and let $(A_s)$ be a c.e. approximation of $A$. Then $x \in f^{-1}(A) \iff \exists s\ (\Phi_i(x)[s]\converge \wedge \Phi_i(x)[s] \in A_s)$, and $y \in f(A) \iff \exists x\, \exists s\ (x \in A_s \wedge \Phi_i(x)[s]\converge = y)$; both are projections of computable relations.
:::

The c.e. sets are not closed under complement, and the relations they define are not closed under **unbounded** universal quantification: $e \notin \emptyset' \iff \forall s\ \Phi_e(e)[s]\diverge$, and $\nat \setminus \emptyset'$ is not c.e. (:ref{#thm-halting-ce}).

:::quiz[closure properties]
In item 3, where is it used that the approximation $(R_s)$ is **increasing**?

- [x] To find a single stage $s$ at which all the finitely many instances $R(\vec x, z)$, $z < y$, are already confirmed.

  Each instance is confirmed at its own stage $s_z$; monotonicity keeps it confirmed at the maximum of these stages.
- [ ] To show that the relation $\forall z < y\ R_s(\vec x, z)$ is computable.

  This only uses the uniform computability of the approximation and bounded quantification.
- [ ] It is not used.

  Without monotonicity, the instances confirmed at different stages might not all hold at a common stage, and the equivalence would fail.

---

Why does the same argument fail for an unbounded quantifier $\forall z\ R(\vec x, z)$?

- [x] Infinitely many instances have to be confirmed, and there is in general no single stage at which all of them are.

  The maximum of infinitely many stages need not exist.
- [ ] Because $\forall z\ R_s(\vec x, z)$ is not computable.

  This is also true in general, but the first obstacle is the absence of a common stage.
- [ ] Because c.e. relations are not closed under complement.

  This is a consequence of the failure, not its cause.
:::

## The graph and selection theorems

:::proposition[Selection]{#prop-selection}
For every c.e. relation $R \subseteq \nat^2$, there is a partial computable function $g$ with $\mathrm{dom}(g) = \{ x : \exists y\ R(x, y) \}$ and $R(x, g(x))$ for every $x \in \mathrm{dom}(g)$.
:::

:::proof{of=prop-selection}
Write $R(x, y) \iff \exists s\ Q(x, y, s)$ with $Q$ computable, and let $g(x) \simeq \pi_0\big(\mu n\ Q(x, \pi_0(n), \pi_1(n))\big)$. The search terminates exactly when some pair $(y, s)$ satisfies $Q(x, y, s)$, that is, when $\exists y\ R(x, y)$, and then $g(x) = y$ for such a pair, so that $R(x, g(x))$.
:::

The function $g$ **selects** a witness $y$ for each $x$, namely the first one found by the dovetailed search. In general, it is not the least witness: finding the least $y$ with $R(x, y)$ would require knowing that smaller $y$ are not witnesses, which is not confirmed at any finite stage.

:::proposition[Graph theorem]{#prop-graph}
A partial function $f : \nat \rightharpoonup \nat$ is partial computable if and only if its graph is c.e.
:::

:::proof{of=prop-graph}
If $f = \Phi_e$, its graph is $\{ (x, y) : \exists s\ \Phi_e(x)[s]\converge = y \}$, c.e. by :ref{#thm-ce-characterizations}. Conversely, if the graph $G$ of $f$ is c.e., apply :ref{#prop-selection} to $G$: the function $g$ has domain $\mathrm{dom}(f)$ and satisfies $G(x, g(x))$, that is, $g(x) = f(x)$, since $G$ is the graph of a function.
:::

:::quiz[selection]
Let $R(x, y)$ be "$\Phi_y(x)\converge$". What can be said of $g(x)$ given by :ref{#prop-selection}?

- [x] It is an index $y$ such that $\Phi_y(x)$ converges, the first one confirmed by the search; it is defined for every $x$, since some index computes a total function.
- [ ] It is the least $y$ such that $\Phi_y(x)\converge$.

  The search returns the first pair $(y, s)$ in the order of the pairing function, which favors small stages as well as small $y$.
- [ ] It is undefined for $x \notin \emptyset'$.

  The relation $R$ concerns $\Phi_y(x)$ for all $y$, not $\Phi_x(x)$.
:::

## The halting set is m-complete

:::proposition{#prop-ce-downward}
If $A \leq_m B$ and $B$ is c.e., then $A$ is c.e.
:::

:::proof{of=prop-ce-downward}
If $f$ reduces $A$ to $B$, then $A = f^{-1}(B)$, which is c.e. by :ref{#prop-ce-closure}.
:::

:::definition{#def-m-complete}
A c.e. set $A$ is **m-complete** if $B \leq_m A$ for every c.e. set $B$.
:::

:::example{#ex-m-complete}
No computable set is m-complete: if $\emptyset' \leq_m A$ with $A$ computable, then $\emptyset'$ would be computable (:ref{#prop-many-one}). An m-complete set is therefore a c.e. set of the highest possible difficulty for many-one reductions. The theorem below shows that the halting set is one, and :ref{#cor-tot-not-ce} gives others.
:::

:::theorem{#thm-halting-complete}
The halting set $\emptyset'$ is m-complete.
:::

The question "$x \in W_a$?" asks whether one computation, $\Phi_a(x)$, halts. The question "$y \in \emptyset'$?" asks whether the program $y$ halts on its own index. The reduction builds, from $x$, a program that runs $\Phi_a(x)$ whatever its input, so that its behavior on its own index is that of $\Phi_a(x)$. This is the method of the reductions of :ref{#prop-halting-variants}: the SMN theorem hides the computation to be tested inside a program.

:::proof{of=thm-halting-complete}
Let $B = W_a$. By :ref{#cor-smn-parameters}, there is a total computable $f$ such that $\Phi_{f(x)}(y) \simeq \Phi_a(x)$ for all $x$ and $y$: the program $f(x)$ ignores its input and runs $\Phi_a$ on $x$. Then
$$
x \in B \iff \Phi_a(x)\converge \iff \Phi_{f(x)}(f(x))\converge \iff f(x) \in \emptyset',
$$
so $f$ reduces $B$ to $\emptyset'$.
:::

:::quiz[m-completeness]
In the proof of :ref{#thm-halting-complete}, why does the program $f(x)$ ignore its input?

- [x] So that $\Phi_{f(x)}(f(x))$, the only computation that membership in $\emptyset'$ looks at, converges exactly when $\Phi_a(x)$ does.

  Whatever input is given to $f(x)$, in particular its own index, the behavior is that of $\Phi_a(x)$.
- [ ] To make $f$ total.

  $f$ is total by the parameter form of SMN, whatever the program it describes.
- [ ] Because $\Phi_a$ has no input.

  $\Phi_a$ is applied to $x$, which is built into the program $f(x)$.
:::

:::corollary{#cor-tot-not-ce}
1. A c.e. set $A$ is m-complete if and only if $\emptyset' \leq_m A$. The sets $H$, $\{ e : \Phi_e(0)\converge \}$ and $\{ e : W_e \neq \emptyset \}$ are m-complete.
2. Neither $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$ nor its complement is c.e.
:::

:::proof{of=cor-tot-not-ce}
1. If $A$ is m-complete, then $\emptyset' \leq_m A$ since $\emptyset'$ is c.e. (:ref{#thm-halting-ce}). Conversely, if $\emptyset' \leq_m A$, every c.e. set reduces to $\emptyset'$ by :ref{#thm-halting-complete}, hence to $A$ by transitivity. The three sets are c.e., since $\langle e, x \rangle \in H \iff \exists s\ \Phi_e(x)[s]\converge$ and $W_e \neq \emptyset \iff \exists n\ \Phi_e(\pi_0(n))[\pi_1(n)]\converge$, and $\emptyset'$ reduces to them by :ref{#prop-halting-variants}.
2. By :ref{#prop-halting-variants}, $\nat \setminus \emptyset' \leq_m \mathrm{Tot}$, and $\emptyset' \leq_m \mathrm{Tot}$, which gives $\nat \setminus \emptyset' \leq_m \nat \setminus \mathrm{Tot}$. If $\mathrm{Tot}$ or its complement were c.e., then $\nat \setminus \emptyset'$ would be c.e. by :ref{#prop-ce-downward}, contradicting :ref{#thm-halting-ce}.
:::

:::figure[The c.e. and co-c.e. sets. Their intersection is the class of computable sets (:ref{#prop-computable-iff-ce-coce}). The halting set is c.e. and not co-c.e., its complement is co-c.e. and not c.e., and the index sets $\mathrm{Tot}$ and $\mathrm{Inf} = \{ e : W_e \text{ is infinite} \}$ are neither (:ref{#cor-tot-not-ce} and the exercises).]
<svg class="fig" viewBox="0 0 520 250" width="520" role="img" aria-label="Two overlapping regions, the c.e. sets and the co-c.e. sets, inside the box of all sets; their intersection is the computable sets"><rect x="4" y="4" width="512" height="242" rx="8" class="track-outline"/><text x="18" y="26" class="label">all subsets of ℕ</text><ellipse cx="200" cy="128" rx="140" ry="88" class="soft-fill" fill-opacity="0.6"/><ellipse cx="320" cy="128" rx="140" ry="88" class="soft-fill" fill-opacity="0.6"/><ellipse cx="200" cy="128" rx="140" ry="88" class="accent-stroke" stroke-width="1.3"/><ellipse cx="320" cy="128" rx="140" ry="88" class="accent-stroke" stroke-width="1.3"/><text x="112" y="92" text-anchor="middle" class="label">c.e.</text><text x="408" y="92" text-anchor="middle" class="label">co-c.e.</text><text x="260" y="88" text-anchor="middle" class="label">computable</text><text x="260" y="122" text-anchor="middle" class="mrm" font-size="15">∅, ℕ, evens</text><text x="130" y="128" text-anchor="middle" class="mrm" font-size="15">∅′, <tspan class="math">H</tspan></text><text x="130" y="152" text-anchor="middle" class="mrm" font-size="13">{<tspan class="math">e</tspan> : <tspan class="math">W</tspan><tspan class="math" font-size="9" dy="3">e</tspan><tspan dy="-3"> ≠ ∅}</tspan></text><text x="390" y="128" text-anchor="middle" class="mrm" font-size="15">ℕ ∖ ∅′</text><text x="390" y="152" text-anchor="middle" class="mrm" font-size="13">{<tspan class="math">e</tspan> : <tspan class="math">W</tspan><tspan class="math" font-size="9" dy="3">e</tspan><tspan dy="-3"> = ∅}</tspan></text><text x="500" y="26" text-anchor="end" class="label">neither: <tspan class="mrm" font-size="14">Tot, Inf</tspan></text></svg>
:::

Post asked in 1944 whether every c.e. set that is not computable is m-complete, or at least as hard as $\emptyset'$ in a weaker sense. For m-reducibility he answered negatively himself, with the **simple sets**; for Turing reducibility the question, known as **Post's problem**, was solved by Friedberg and Muchnik with the priority method. These results are the subject of later courses.


## Exercises

::::exercise{difficulty=2}
(Reduction principle.) Show that for all c.e. sets $A$ and $B$, there are disjoint c.e. sets $A' \subseteq A$ and $B' \subseteq B$ with $A' \cup B' = A \cup B$.

:::solution
Fix c.e. approximations $(A_s)$ and $(B_s)$. For $x \in A \cup B$, let $s_x$ be the least $s$ with $x \in A_s \cup B_s$. Let $A' = \{ x : x \in A_{s_x} \}$ and $B' = \{ x : x \notin A_{s_x} \text{ and } x \in B_{s_x} \}$: an element is assigned to the set in which it appears first, with priority to $A$ in case of a tie. Both sets are c.e., since $x \in A' \iff \exists s\ (x \in A_s \wedge \forall t < s\ x \notin A_t \cup B_t)$, and similarly for $B'$. They are disjoint, contained in $A$ and $B$ respectively, and every $x \in A \cup B$ belongs to one of them.
:::
::::

::::exercise{difficulty=2}
Show that the set $\{ e : W_e \text{ is infinite} \}$ is neither c.e. nor co-c.e.

:::hint
Use the two reductions of :ref{#ex-inf-reductions}.
:::

:::solution
By :ref{#ex-inf-reductions}, $\emptyset'$ and $\nat \setminus \emptyset'$ both reduce to this set. As in the proof of :ref{#cor-tot-not-ce}, if the set or its complement were c.e., then $\nat \setminus \emptyset'$ would be c.e.
:::
::::

## Notes and references

Post's paper of 1944 introduced many-one and one-one reducibility, complete sets and simple sets, and asked the question now called Post's problem. In Soare's textbook, the selection theorem is the uniformization theorem (Theorem 2.1.8), followed by the graph theorem (Theorem 2.1.9), the union theorem (Theorem 2.1.11) and the reduction principle (Corollary 2.1.12); complete sets are treated in Sections 1.6 and 2.4.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 2.1 and 2.4.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
