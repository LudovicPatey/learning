---
title: Computably enumerable sets
summary: Characterizations of the computably enumerable sets, closure properties, the graph and selection theorems, and the m-completeness of the halting set.
duration: 45
prerequisites: [halting-problem]
---

The halting set is not computable, but membership in it can be confirmed: if $\Phi_e(e)\converge$, simulating the computation eventually establishes it. Sets with this property are the **computably enumerable** sets. They are the sets that an algorithm can list, the domains of partial computable functions, and the projections of computable relations. Examples outside computability theory include the set of theorems of a computably axiomatized theory, and the set of solvable Diophantine equations. This lesson proves the equivalence of these descriptions, the closure properties of the class, and the fact that the halting set is the hardest computably enumerable set.

## Definition and characterizations

:::definition{#def-ce}
The **$e$-th computably enumerable set** is $W_e = \mathrm{dom}(\Phi_e) = \{ x : \Phi_e(x)\converge \}$. A set $A \subseteq \nat$ is **computably enumerable**, or **c.e.**, if $A = W_e$ for some $e$. Its approximation at stage $s$ is $W_e[s] = \{ x : \Phi_e(x)[s]\converge \}$.
:::

Older texts say *recursively enumerable*, or *r.e.* By the conventions on stages (:ref{#def-stage}), $W_e[s]$ is a finite subset of $\{0, \dots, s - 1\}$, computable from $e$ and $s$, and $W_e[0] \subseteq W_e[1] \subseteq \cdots$ with $\bigcup_s W_e[s] = W_e$.

:::definition{#def-ce-approx}
A **c.e. approximation** of a set $A$ is a uniformly computable sequence of sets $A_0 \subseteq A_1 \subseteq A_2 \subseteq \cdots$ with $\bigcup_s A_s = A$.
:::

A relation $R \subseteq \nat^k$ is c.e. if the set $\{ \langle x_1, \dots, x_k \rangle : \vec x \in R \}$ is.

:::theorem{#thm-ce-characterizations}
For every $A \subseteq \nat$, the following are equivalent.

1. $A$ is computably enumerable.
2. $A = \{ x : \exists y\ R(x, y) \}$ for some computable relation $R \subseteq \nat^2$.
3. $A = \emptyset$, or $A$ is the range of a total computable function.
4. $A$ is the range of a partial computable function.
5. $A$ has a c.e. approximation.

Moreover, in item 2 the relation $R$ can be taken primitive recursive.
:::

:::proof{of=thm-ce-characterizations}
(1 ⇒ 2) If $A = W_e$, then $x \in A \iff \exists s\ \Phi_e(x)[s]\converge$, and the relation $\Phi_e(x)[s]\converge$ of $x$ and $s$ is primitive recursive (:ref{#prop-stage-properties}).

(2 ⇒ 3) Suppose $A \neq \emptyset$ and fix $a \in A$. Let $f(n) = \pi_0(n)$ if $R(\pi_0(n), \pi_1(n))$, and $f(n) = a$ otherwise. This $f$ is total computable, its values lie in $A$, and every $x \in A$ is a value: if $R(x, y)$, then $x = f(\langle x, y \rangle)$.

(3 ⇒ 4) A total function is partial, and $\emptyset$ is the range of the nowhere defined function.

(4 ⇒ 1) Let $A$ be the range of $\Phi_i$. The partial function $g(x) \simeq \mu n\ [\Phi_i(\pi_0(n))[\pi_1(n)]\converge = x]$ is partial computable, by :ref{#prop-computable-closure} and :ref{#prop-stage-properties}. It is defined if and only if $\Phi_i(y)\converge = x$ for some $y$, that is, if and only if $x \in A$. So $A = \mathrm{dom}(g)$ is c.e.

(1 ⇒ 5) If $A = W_e$, the sequence $(W_e[s])_s$ is a c.e. approximation.

(5 ⇒ 2) If $(A_s)$ is a c.e. approximation, then $x \in A \iff \exists s\ x \in A_s$, and the relation $x \in A_s$ is computable.
:::

Item 2 says that the c.e. sets are the sets definable by an **existential** quantifier over a computable relation: they are the $\Sigma^0_1$ sets of the arithmetic hierarchy. Item 3 justifies the name: a non-empty c.e. set is listed, possibly with repetitions, by an algorithm $f(0), f(1), f(2), \dots$. The proof of (2 ⇒ 3) runs through all pairs $(x, y)$ in the order of the pairing function, which interleaves the searches for witnesses of all $x$ at once. This technique is called **dovetailing**: running the searches one after the other would fail, since the search for a witness of some $x \notin A$ never ends.

:::quiz[the characterizations]
In (2 ⇒ 3), why does $f$ test single pairs $n = \langle x, y \rangle$, instead of searching for a witness $y$ of each $x$ in turn?

- [x] A search for a witness of some $x \notin A$ never terminates, and would block the enumeration of all later elements; testing one pair at a time keeps $f$ total.
- [ ] To make $f$ injective.

  $f$ is not injective: it takes the value $a$ infinitely often.
- [ ] Because $R$ is only defined on pairs.

  $R$ is a relation on pairs either way; the issue is termination.

---

In (4 ⇒ 1), what does the search $\mu n\ [\Phi_i(\pi_0(n))[\pi_1(n)]\converge = x]$ range over?

- [x] Pairs $(y, s)$ of an argument and a stage, until a computation $\Phi_i(y)$ is found to converge to $x$ at stage $s$.

  Searching over arguments $y$ only, by computing $\Phi_i(0), \Phi_i(1), \dots$, could get stuck on a divergent computation.
- [ ] Indices of programs computing $x$.

  The search ranges over arguments and stages of the fixed function $\Phi_i$; indices of other programs play no role.
- [ ] Stages at which $x$ enters $W_i$.

  This would describe the domain of $\Phi_i$, not its range.
:::

:::proposition{#prop-ce-range}
An infinite set $A$ is computably enumerable if and only if it is the range of an injective total computable function.
:::

:::proof{of=prop-ce-range}
The range of a total computable function is c.e. by :ref{#thm-ce-characterizations}. Conversely, let $f$ be total computable with range $A$. Define $g(0) = f(0)$, and $g(n+1) = f(m_{n+1})$, where $m_{n+1}$ is the least $m$ with $f(m) \notin \{ g(0), \dots, g(n) \}$. The search terminates since $A$ is infinite, so $g$ is total computable, and it is injective by construction. Let $m_0 = 0$. By induction on $n$, $\{ f(0), \dots, f(m_n) \} = \{ g(0), \dots, g(n) \}$: the values $f(m)$ for $m_n < m < m_{n+1}$ are already listed, by minimality of $m_{n+1}$. Hence $m_0 < m_1 < \cdots$, and every value of $f$ is a value of $g$.
:::

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

The c.e. sets are not closed under complement, and the relations they define are not closed under **unbounded** universal quantification: $e \notin \emptyset' \iff \forall s\ \Phi_e(e)[s]\diverge$, and the next section shows that $\nat \setminus \emptyset'$ is not c.e.

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

## Computable and c.e. sets

:::proposition{#prop-computable-iff-ce-coce}
A set $A$ is computable if and only if both $A$ and $\nat \setminus A$ are computably enumerable.
:::

:::proof{of=prop-computable-iff-ce-coce}
If $A$ is computable, $A = \{ x : \exists y\ \chi_A(x) = 1 \}$ is the projection of a computable relation (with a dummy variable), hence c.e.; and $\nat \setminus A$ is computable as well.

Conversely, let $A = W_a$ and $\nat \setminus A = W_b$. On input $x$, search for the least $s$ such that $x \in W_a[s]$ or $x \in W_b[s]$, and output $1$ in the first case, $0$ in the second. The search terminates, since $x$ belongs to one of the two sets and hence appears in its approximation at some stage; the two cases do not overlap, since the sets are disjoint. So this algorithm computes $\chi_A$.
:::

:::theorem{#thm-halting-ce}
The halting set $\emptyset'$ is computably enumerable, and its complement $\nat \setminus \emptyset'$ is not.
:::

:::proof{of=thm-halting-ce}
$\emptyset' = \{ e : \exists s\ \Phi_e(e)[s]\converge \}$ is c.e. If its complement were c.e., then $\emptyset'$ would be computable by :ref{#prop-computable-iff-ce-coce}, contradicting :ref{#thm-halting}.
:::

So the computable sets form a proper subclass of the c.e. sets, and the c.e. sets are not closed under complement. A set whose complement is c.e. is called **co-c.e.**

:::quiz[computable and c.e. sets]
In the proof of :ref{#prop-computable-iff-ce-coce}, why are the two approximations examined stage by stage, rather than by running $\Phi_a(x)$ to completion first?

- [x] If $x \notin A$, the computation of $\Phi_a(x)$ never halts, and the algorithm would never consider $W_b$.

  Examining both at each stage is a form of dovetailing.
- [ ] Because $\Phi_a$ is total.

  $\Phi_a$ diverges exactly outside $A$.
- [ ] To output the answer faster.

  Speed is irrelevant; termination is the point.

---

Which statements are correct?

- [x] Every computable set is c.e., but not conversely.
- [x] If $A$ is c.e. and not computable, then $\nat \setminus A$ is not c.e.
- [ ] The complement of a c.e. set is never c.e.

  It is c.e. exactly when the set is computable.
- [ ] Every subset of a c.e. set is c.e.

  $\nat$ is c.e., and $\nat \setminus \emptyset'$ is a subset of it which is not c.e.
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

:::theorem{#thm-halting-complete}
The halting set $\emptyset'$ is m-complete.
:::

:::proof{of=thm-halting-complete}
Let $B = W_a$. By :ref{#cor-smn-parameters}, there is a total computable $f$ such that $\Phi_{f(x)}(y) \simeq \Phi_a(x)$ for all $x$ and $y$: the program $f(x)$ ignores its input and runs $\Phi_a$ on $x$. Then
$$
x \in B \iff \Phi_a(x)\converge \iff \Phi_{f(x)}(f(x))\converge \iff f(x) \in \emptyset',
$$
so $f$ reduces $B$ to $\emptyset'$.
:::

:::corollary{#cor-tot-not-ce}
1. A c.e. set $A$ is m-complete if and only if $\emptyset' \leq_m A$. The sets $H$, $\{ e : \Phi_e(0)\converge \}$ and $\{ e : W_e \neq \emptyset \}$ are m-complete.
2. Neither $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$ nor its complement is c.e.
:::

:::proof{of=cor-tot-not-ce}
1. If $A$ is m-complete, then $\emptyset' \leq_m A$ since $\emptyset'$ is c.e. (:ref{#thm-halting-ce}). Conversely, if $\emptyset' \leq_m A$, every c.e. set reduces to $\emptyset'$ by :ref{#thm-halting-complete}, hence to $A$ by transitivity. The three sets are c.e., since $\langle e, x \rangle \in H \iff \exists s\ \Phi_e(x)[s]\converge$ and $W_e \neq \emptyset \iff \exists n\ \Phi_e(\pi_0(n))[\pi_1(n)]\converge$, and $\emptyset'$ reduces to them by :ref{#prop-halting-variants}.
2. By :ref{#prop-halting-variants}, $\nat \setminus \emptyset' \leq_m \mathrm{Tot}$, and $\emptyset' \leq_m \mathrm{Tot}$, which gives $\nat \setminus \emptyset' \leq_m \nat \setminus \mathrm{Tot}$. If $\mathrm{Tot}$ or its complement were c.e., then $\nat \setminus \emptyset'$ would be c.e. by :ref{#prop-ce-downward}, contradicting :ref{#thm-halting-ce}.
:::

Post asked in 1944 whether every c.e. set that is not computable is m-complete, or at least as hard as $\emptyset'$ in a weaker sense. For m-reducibility he answered negatively himself, with the **simple sets**; for Turing reducibility the question, known as **Post's problem**, was solved by Friedberg and Muchnik with the priority method. These results are the subject of later courses.

:::quiz[m-completeness]
In the proof of :ref{#thm-halting-complete}, why does the program $f(x)$ ignore its input?

- [x] So that $\Phi_{f(x)}(f(x))$, the only computation that membership in $\emptyset'$ looks at, converges exactly when $\Phi_a(x)$ does.

  Whatever input is given to $f(x)$, in particular its own index, the behavior is that of $\Phi_a(x)$.
- [ ] To make $f$ total.

  $f$ is total by the parameter form of SMN, whatever the program it describes.
- [ ] Because $\Phi_a$ has no input.

  $\Phi_a$ is applied to $x$, which is built into the program $f(x)$.
:::

## Exercises

::::exercise{difficulty=1}
An infinite set $A$ is **enumerable in increasing order** if $A = f(\nat)$ for some total computable $f$ with $f(n) < f(n+1)$ for all $n$. Show that an infinite set is computable if and only if it is enumerable in increasing order.

:::solution
If $A$ is infinite and computable, its principal function $p_A$ (:ref{#lem-subsets-of-n}) is computable, by $p_A(0) = \mu x\, (x \in A)$ and $p_A(n+1) = \mu x\, (x > p_A(n) \wedge x \in A)$, and it enumerates $A$ in increasing order. Conversely, to decide whether $x \in A$, compute $f(0), f(1), \dots$ until a value greater than $x$ appears, which happens since $f(n) \geq n$; then $x \in A$ if and only if $x$ is among the values computed, since later values are larger.
:::
::::

::::exercise{difficulty=1}
Show that every infinite c.e. set contains an infinite computable subset.

:::solution
Let $f$ be a total computable function with range $A$. Let $g(0) = f(0)$, and $g(n+1) = f(m)$ for the least $m$ with $f(m) > g(n)$, which exists since $A$ is infinite. Then $g$ is total computable and strictly increasing, and its range is an infinite subset of $A$, computable by the previous exercise.
:::
::::

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

Computably enumerable sets were introduced in the 1930s, in the work of Church, Kleene and Post on recursive functions; Post's paper of 1944 made them a subject of study in their own right, introduced many-one and one-one reducibility, the notion of complete set, and simple sets. The selection theorem is due to Kleene. Soare's textbook is the standard reference for the theory of c.e. sets.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
