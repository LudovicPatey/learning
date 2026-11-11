---
title: Simple sets and Post's problem
summary: Post's problem; simple sets and Post's construction; productive and creative sets; simple sets are not many-one complete.
duration: 35
prerequisites: [turing-degrees/turing-reducibility, arithmetic-hierarchy/index-sets]
---

In 1944, Post observed that all the non-computable c.e. sets known at the time — the halting set, the set of theorems of a sufficiently strong computably axiomatized theory such as Peano arithmetic — are Turing equivalent to $\emptyset'$. He asked whether this is always the case.

:::definition{#def-post-problem}
**Post's problem** asks whether there is a c.e. set $A$ with $\emptyset <_T A <_T \emptyset'$, that is, a c.e. set which is neither computable nor Turing complete.
:::

Post's approach, known as **Post's program**, was to find a structural property of the complement of a c.e. set that forces the set to be incomplete. His first such property, simplicity, is the subject of this lesson. It yields c.e. sets that are not computable and not complete for many-one reducibility, but it does not settle Post's problem for Turing reducibility. That required a new method, the priority method of the next lessons.

## Simple sets

:::definition{#def-simple}
An infinite set $C$ is **immune** if it contains no infinite c.e. subset. A c.e. set $A$ is **simple** if $\nat \setminus A$ is immune; that is, $\nat \setminus A$ is infinite and meets every infinite c.e. set.
:::

A simple set is not computable: if it were, its complement would be an infinite computable, hence c.e., subset of itself. The complement of a simple set is thin: it is infinite, but no algorithm can list infinitely many of its elements.

:::theorem[Post]{#thm-post-simple}
There is a simple set.
:::

:::proof{of=thm-post-simple}
For each $e$, let $x_e$ be an element $x > 2e$ of $W_e$ found by a fixed search, if there is one: the element $x$ of the least pair $\langle x, s \rangle$ (for the pairing function) with $x > 2e$ and $x \in W_e[s]$; $x_e$ is undefined if $W_e$ has no element greater than $2e$. Let $S = \{ x_e : x_e \text{ is defined} \}$.

*$S$ is c.e.* The relation "$x_e$ is defined and equal to $x$" is c.e., since it is witnessed by a finite search; $S$ is its projection.

*The complement of $S$ is infinite.* Since $x_e > 2e$, an element $x_e \leq 2n$ satisfies $e < n$. So $S \cap \{0, \dots, 2n\}$ has at most $n$ elements, and at least $n + 1$ of the numbers $0, \dots, 2n$ are outside $S$, for every $n$.

*The complement of $S$ meets every infinite c.e. set.* If $W_e$ is infinite, it has elements greater than $2e$, so $x_e$ is defined, and $x_e \in W_e \cap S$. Hence $W_e \not\subseteq \nat \setminus S$.
:::

The bound $x_e > 2e$ is what keeps $S$ small: each $W_e$ contributes at most one element, and only a large one. The construction is a priority-free version of a pattern that recurs throughout the course: each requirement "$W_e$ is not contained in the complement" acts at most once, and the acting is restricted so that the requirements together cannot fill the complement.

:::quiz[Post's simple set]
Why does the construction require $x_e > 2e$, rather than taking the first element of $W_e$?

- [x] To keep the complement of $S$ infinite: with this bound, $S$ contains at most $n$ of the numbers $0, \dots, 2n$.

  Without a bound, every number $n$ is the chosen element of any index $e$ with $W_e = \{ n \}$, so $S$ would be all of $\nat$.
- [ ] To make $S$ c.e.

  $S$ would be c.e. with any computable choice of the element.
- [ ] To ensure that $x_e \in W_e$.

  This holds by definition, whatever the bound.

---

Why does each infinite $W_e$ meet $S$?

- [x] An infinite set has elements above $2e$, so $x_e$ is defined, and it belongs to both $W_e$ and $S$.
- [ ] Because $S$ is cofinite.

  $S$ is coinfinite; it meets $W_e$ because one element of $W_e$ was put into it on purpose.
- [ ] Because $W_e \subseteq S$.

  Only one element of $W_e$ is put into $S$.
:::

## Productive and creative sets

To see that a simple set is not many-one complete, we isolate the property of the complement of $\emptyset'$ that simple sets lack.

:::definition{#def-productive}
A set $P$ is **productive** if there is a total computable function $p$, a **productive function** for $P$, such that for every $e$: if $W_e \subseteq P$, then $p(e) \in P \setminus W_e$. A c.e. set is **creative** if its complement is productive.
:::

A productive set is not c.e.: if $P = W_e$, then $p(e) \in P \setminus W_e = \emptyset$. More than that, every c.e. subset of $P$ is effectively witnessed to be a proper subset.

:::proposition{#prop-halting-creative}
The halting set $\emptyset'$ is creative, with the identity as productive function for its complement.
:::

:::proof{of=prop-halting-creative}
Suppose $W_e \subseteq \nat \setminus \emptyset'$. If $e \in W_e$, then $\Phi_e(e)\converge$, so $e \in \emptyset'$, contradicting the inclusion. So $e \notin W_e$, which means $\Phi_e(e)\diverge$, that is, $e \in \nat \setminus \emptyset'$. Hence $e \in (\nat \setminus \emptyset') \setminus W_e$.
:::

:::lemma{#lem-productive-infinite}
Every productive set contains an infinite c.e. subset.
:::

:::proof{of=lem-productive-infinite}
Let $p$ be a productive function for $P$. By the parameter form of SMN, there is a computable $h$ with $W_{h(n)} = D_n$, the finite set of canonical index $n$. Define $x_0 = p(h(0))$, where $D_0 = \emptyset$, and $x_{k+1} = p(h(n_k))$ where $n_k$ is the canonical index of $\{ x_0, \dots, x_k \}$. By induction on $k$, the set $\{ x_0, \dots, x_k \}$ is contained in $P$, so that $x_{k+1} = p(h(n_k))$ belongs to $P$ and is different from $x_0, \dots, x_k$. The sequence $(x_k)$ is computable and injective, so its range is an infinite c.e. subset of $P$.
:::

:::proposition{#prop-productive-reduction}
If $A \leq_m B$ and $\nat \setminus A$ is productive, then $\nat \setminus B$ is productive. In particular, the complement of every m-complete set is productive, and every m-complete set is creative.
:::

:::proof{of=prop-productive-reduction}
Let $f$ reduce $A$ to $B$, and $p$ be a productive function for $\nat \setminus A$. By the parameter form of SMN, there is a computable $q$ with $W_{q(e)} = f^{-1}(W_e)$. Let $p'(e) = f(p(q(e)))$. If $W_e \subseteq \nat \setminus B$, then $f^{-1}(W_e) \subseteq \nat \setminus A$, so $x = p(q(e))$ lies in $\nat \setminus A$ and not in $f^{-1}(W_e)$. Hence $f(x) \notin B$ and $f(x) \notin W_e$, that is, $p'(e) \in (\nat \setminus B) \setminus W_e$. The second statement follows from :ref{#prop-halting-creative}, since $\emptyset' \leq_m A$ for every m-complete set $A$.
:::

:::theorem{#thm-simple-not-complete}
No simple set is many-one complete. In particular, Post's simple set is a c.e. set which is neither computable nor m-complete.
:::

:::proof{of=thm-simple-not-complete}
If $A$ is m-complete, the complement of $A$ is productive by :ref{#prop-productive-reduction}, hence contains an infinite c.e. subset by :ref{#lem-productive-infinite}, so $A$ is not simple.
:::

The converse of the second statement of :ref{#prop-productive-reduction} also holds: Myhill showed in 1955 that the creative sets are exactly the m-complete c.e. sets, and that any two creative sets are computably isomorphic. We admit this (Myhill 1955; see also Soare's book of 1987).

:::quiz[creative sets]
In the proof of :ref{#lem-productive-infinite}, why is the productive function applied to indices of finite sets that grow along the construction?

- [x] Each new element must avoid all the elements already produced; a productive function only guarantees an element outside the given c.e. subset, so the subset must contain all previous elements.
- [ ] Because a productive function is only defined on indices of finite sets.

  It is total; finite sets are used because their indices are computable from the elements produced.
- [ ] To make the sequence increasing.

  The sequence need not be increasing, only injective.

---

Does :ref{#thm-simple-not-complete} solve Post's problem?

- [ ] Yes: a simple set is not computable and not complete.

  It is not many-one complete. Simple sets can be Turing complete: every non-computable c.e. degree, including $\obf'$, contains a simple set.
- [x] No: it concerns many-one reducibility, and some simple sets are Turing equivalent to $\emptyset'$.

  Post's problem asks about Turing reducibility. It was solved by the priority method.
:::

Post introduced stronger thinness properties, such as **hypersimplicity**, and showed that hypersimple sets are not complete for truth-table reducibility, a reducibility between many-one and Turing. But the thinness properties Post considered do not ensure Turing incompleteness: Dekker showed that every non-computable c.e. degree contains a hypersimple set (Dekker 1954), so that Post's program in its original form could not succeed. We admit these results; see Odifreddi's book or Soare's book of 1987.

## Exercises

::::exercise{difficulty=1}
Show that every creative set is not computable, and that its complement is not c.e.

:::solution
Let $p$ be a productive function for the complement $P$ of the creative set. If $P = W_e$, then $W_e \subseteq P$ gives $p(e) \in P \setminus W_e = \emptyset$, a contradiction. So $P$ is not c.e., and the creative set, whose complement is not c.e., is not computable.
:::
::::

::::exercise{difficulty=1}
Show that the join $A \oplus B$ of two simple sets is simple.

:::solution
$A \oplus B$ is c.e., and its complement $\{ 2n : n \notin A \} \cup \{ 2n + 1 : n \notin B \}$ is infinite. Let $W$ be an infinite c.e. set contained in the complement. Then $W$ contains infinitely many even numbers or infinitely many odd numbers. In the first case, $\{ n : 2n \in W \}$ is an infinite c.e. set contained in $\nat \setminus A$, contradicting the simplicity of $A$; the second case is symmetric.
:::
::::

::::exercise{difficulty=2}
Show that the index set $\{ e : W_e \text{ is simple} \}$ is $\Pi^0_3$.

:::solution
$W_e$ is simple if and only if its complement is infinite and $\forall i\ (W_i \text{ infinite} \to W_i \cap W_e \neq \emptyset)$. The first condition is "$\forall n\ \exists x > n\ x \notin W_e$", which is $\Pi^0_3$: the relation $x \notin W_e$ is $\Pi^0_1$, so $\exists x > n\ x \notin W_e$ is $\Sigma^0_2$. In the second condition, "$W_i$ infinite" is $\Pi^0_2$ and "$W_i \cap W_e \neq \emptyset$" is $\Sigma^0_1$, so the implication is $\Sigma^0_2$, and its universal closure is $\Pi^0_3$. The conjunction of two $\Pi^0_3$ conditions is $\Pi^0_3$.
:::
::::

## Notes and references

Post's problem, simple sets and the program of finding thinness properties of complements are in Post's paper of 1944, which also introduced creative sets. Productive sets are due to Dekker (1955), and the characterization of creative sets as m-complete sets to Myhill (1955). Odifreddi's book gives a detailed history of Post's program.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- J. C. E. Dekker, *A theorem on hypersimple sets*, Proceedings of the American Mathematical Society 5 (1954), 791–796.
- J. C. E. Dekker, *Productive sets*, Transactions of the American Mathematical Society 78 (1955), 129–149.
- J. Myhill, *Creative sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 1 (1955), 97–108.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
