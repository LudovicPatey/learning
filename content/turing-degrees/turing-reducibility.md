---
title: Turing reducibility and degrees
summary: Turing reducibility, the partial order of Turing degrees, the join as least upper bound, countability of lower cones, and relative computable enumerability.
duration: 35
prerequisites: [oracle-computation]
---

Relative computability compares sets by their computational power: $X$ is at most as powerful as $Y$ if every question about $X$ can be answered by an algorithm consulting $Y$. This is **Turing reducibility**, the most important of the reducibilities of computability theory. Identifying sets of the same power gives the **Turing degrees**, whose structure is one of the main subjects of the theory. This lesson sets up the basic definitions and the first properties of the degrees.

## Turing reducibility

:::definition{#def-turing-reducible}
Let $X, Y \in \cs$. The set $X$ is **Turing reducible** to $Y$, written $X \leq_T Y$, if $X$ is $Y$-computable: $\Phi^Y_e = X$ for some $e$, that is, $\Phi^Y_e(n)\converge = X(n)$ for every $n$. We write $X <_T Y$ if $X \leq_T Y$ and $Y \not\leq_T X$.
:::

:::proposition{#prop-turing-preorder}
1. $\leq_T$ is reflexive and transitive.
2. Transitivity is uniform: there is a computable function $c$ such that, if $\Phi^Y_a = X$, then $\Phi^Y_{c(a, b)} = \Phi^X_b$ as partial functions, for every $b$. In particular, if moreover $\Phi^X_b = Z$, then $\Phi^Y_{c(a, b)} = Z$.
3. If $A \leq_m B$, then $A \leq_T B$. Moreover $X \leq_T \nat \setminus X$, and every computable set is reducible to every set.
:::

:::proof{of=prop-turing-preorder}
1. Reflexivity: the machine that copies the bit $X(n)$ from its oracle tape computes $X$ with oracle $X$. Transitivity follows from item 2.
2. Let $\Phi^{c(a, b)}$ be the following oracle machine. On input $n$, with oracle $Y$, it runs the machine $b$ on input $n$, but whenever the machine $b$ needs the bit of its oracle at cell $k$, it computes $\Phi^Y_a(k)$ and uses the result. With $\Phi^Y_a = X$, every requested bit is computed correctly and the simulation follows the computation of $\Phi^X_b(n)$. Formally, the machine searches for $t$ and a string $\sigma$ such that $\Phi^Y_a(k)\converge = \sigma(k)$ for all $k < |\sigma|$, and $t$ codes a halting computation of $b$ on $n$ with oracle $\sigma$, then outputs its result. If $\Phi^Y_a = X$, the strings $\sigma$ found are prefixes of $X$. If $\Phi^X_b(n)\converge$, such a pair exists, namely the computation with oracle $X$ and $\sigma = X \uh u$ for $u$ its use, and by :ref{#prop-oracle-stages} any pair found gives the output $\Phi^X_b(n)$. If $\Phi^X_b(n)\diverge$, no pair exists, since a halting computation with oracle $\sigma \prec X$ would give $\Phi^X_b(n)\converge$ by the same proposition; so the search diverges. The machine does not depend on $Y$, and its code is obtained computably from $a$ and $b$.
3. If $f$ is a many-one reduction of $A$ to $B$, then $A(n) = B(f(n))$, computed by evaluating $f(n)$ and reading the oracle. The complement is computed by reading the bit and flipping it. A computable set is computed by a machine that ignores its oracle.
:::

:::quiz[the transitivity of Turing reducibility]
In item 2, the machine searches for a string $\sigma$ whose bits are confirmed by $\Phi^Y_a$. Why not simply compute $\Phi^Y_a(0), \Phi^Y_a(1), \dots$ up to some bound, and then run $b$?

- [x] No bound is known in advance on the cells that the computation of $b$ will read; the search finds a string long enough to contain them.

  The use of $\Phi^X_b(n)$ is not computable from $n$ alone, so the prefix of $X$ needed is discovered during the search.
- [ ] Because $\Phi^Y_a$ is partial.

  When $\Phi^Y_a = X$, it is total.
- [ ] Because $X$ is not $Y$-computable.

  It is, by hypothesis.

---

Many-one reducibility implies Turing reducibility. Which statement shows that the converse fails?

- [x] $\nat \setminus \emptyset' \leq_T \emptyset'$, while $\nat \setminus \emptyset' \not\leq_m \emptyset'$.

  A set many-one reducible to a c.e. set is c.e. (:ref{#prop-ce-downward}), and $\nat \setminus \emptyset'$ is not.
- [ ] $\emptyset' \leq_T \emptyset'$.

  This holds for both reducibilities.
- [ ] Every computable set is Turing reducible to $\emptyset'$.

  It is also many-one reducible to $\emptyset'$, as to every set other than $\emptyset$ and $\nat$; this does not separate the two notions.
:::

## Turing degrees

:::definition{#def-turing-degree}
Two sets $X$ and $Y$ are **Turing equivalent**, written $X \equiv_T Y$, if $X \leq_T Y$ and $Y \leq_T X$. The **Turing degree** of $X$ is its equivalence class $\deg_T(X) = \{ Y : Y \equiv_T X \}$. The set of Turing degrees is $\mathcal D$, ordered by $\deg_T(X) \leq \deg_T(Y)$ if and only if $X \leq_T Y$.
:::

The order on degrees is well defined, since $X \equiv_T X_1$ and $Y \equiv_T Y_1$ imply that $X \leq_T Y$ if and only if $X_1 \leq_T Y_1$, by transitivity. It is a partial order on $\mathcal D$. Degrees are written in bold: $\abf, \bbf, \dbf, \dots$. The least degree is $\obf$, the degree of the computable sets.

:::proposition{#prop-degree-countable}
1. For every $Y$, the **lower cone** $\{ X : X \leq_T Y \}$ is countable.
2. Every Turing degree is countably infinite, and is closed under finite modifications: if $X \in \dbf$ and $X \symdiff Z$ is finite, then $Z \in \dbf$.
3. For every sequence $(Y_n)_{n \in \nat}$ of sets, there is a set $Z$ with $Z \not\leq_T Y_n$ for every $n$. Hence no sequence of degrees contains every degree, and every degree has only countably many degrees below it.
:::

:::proof{of=prop-degree-countable}
1. Each $X \leq_T Y$ is $\Phi^Y_e$ for some $e$, so $e \mapsto \Phi^Y_e$, restricted to the indices of total $\{0,1\}$-valued functions, is a surjection from a subset of $\nat$ onto the lower cone.
2. A degree is contained in a lower cone, hence countable. If $X \symdiff Z$ is finite, a machine computes $Z$ from $X$ by copying the oracle except at the finitely many positions where $X$ and $Z$ differ, which are written in its table; and symmetrically. The finite modifications of $X$ form an infinite set, so the degree is infinite.
3. Let $Z(\langle e, n \rangle) = 1 - \Phi^{Y_n}_e(\langle e, n \rangle)$ if this value is defined and in $\{0, 1\}$, and $Z(\langle e, n \rangle) = 0$ otherwise. If $Z = \Phi^{Y_n}_e$, then $\Phi^{Y_n}_e(\langle e, n \rangle)\converge = Z(\langle e, n \rangle) \in \{0, 1\}$, and by definition $Z(\langle e, n \rangle) = 1 - Z(\langle e, n \rangle)$, a contradiction. For the second statement, given a sequence of degrees $(\dbf_n)$, apply this to a sequence of representatives $Y_n \in \dbf_n$; the degree of $Z$ is none of the $\dbf_n$, since otherwise $Z \leq_T Y_n$. The last statement is item 1.
:::

The choice of representatives in item 3 uses the axiom of countable choice. With the axiom of choice, $\mathcal D$ has the cardinality of the continuum, as a set of countable classes partitioning $\cs$. Without choice, a refinement of the finite extension method of a later lesson, which builds a perfect tree of strings instead of a single sequence, gives an explicit family of continuum many pairwise incomparable degrees; the exercises of that lesson treat the case of countably many.

:::quiz[the size of degrees]
In item 3, why is $Z$ defined by a diagonal argument indexed by pairs $\langle e, n \rangle$?

- [x] Each pair $(e, n)$ is a potential reduction $Z = \Phi^{Y_n}_e$ to be defeated, and each needs a position of its own.
- [ ] To make $Z$ computable.

  $Z$ is not computable in general: the pairing only assigns one position to each requirement.
- [ ] Because $\Phi^{Y_n}_e$ is only defined on pairs.

  The functionals are defined on all inputs; the pairing assigns one input to each requirement.
:::

## The join

:::definition{#def-join-degrees}
The **join** of $X$ and $Y$ is $X \oplus Y = \{ 2n : n \in X \} \cup \{ 2n + 1 : n \in Y \}$, as in :ref{#def-join}.
:::

:::proposition{#prop-join-lub}
For all $X$ and $Y$, $\deg_T(X \oplus Y)$ is the least upper bound of $\deg_T(X)$ and $\deg_T(Y)$. Hence $\mathcal D$ is an upper semilattice, and we write $\abf \vee \bbf$ for the least upper bound of $\abf$ and $\bbf$.
:::

:::proof{of=prop-join-lub}
$X(n) = (X \oplus Y)(2n)$ and $Y(n) = (X \oplus Y)(2n + 1)$, so $X$ and $Y$ are computable from $X \oplus Y$. If $X = \Phi^Z_a$ and $Y = \Phi^Z_b$, then $X \oplus Y$ is computed from $Z$ by: on input $m$, if $m = 2n$, compute $\Phi^Z_a(n)$; if $m = 2n + 1$, compute $\Phi^Z_b(n)$. So every upper bound of $\deg_T(X)$ and $\deg_T(Y)$ is above $\deg_T(X \oplus Y)$. The least upper bound depends only on the degrees, so $\abf \vee \bbf$ is well defined.
:::

The degrees do not form a lattice: there are pairs of degrees without a greatest lower bound, and no strictly increasing sequence of degrees has a least upper bound. These results go back to Kleene and Post (1954) and Spector (1956); we admit them here, and they are proved in the specialized course on the structure of the Turing degrees (:ref{#cor-not-lattice}).

:::quiz[the join]
Is the set $X \cup Y$ an upper bound of $\deg_T(X)$ and $\deg_T(Y)$?

- [ ] Yes, since it contains both sets.

  Containing a set does not mean computing it: from $X \cup Y$ one cannot tell which of the two sets an element comes from.
- [x] Not in general: for $Y = \nat \setminus X$, the union is $\nat$, which is computable.

  The join keeps the two sets apart, on the even and odd positions.
- [ ] Yes, and it is Turing equivalent to $X \oplus Y$.

  $X \cup Y$ need not compute $X$ or $Y$, and for $Y = \nat \setminus X$ it is computable, while $X \oplus Y \equiv_T X$.
:::

## Relative enumerability

By relativization (:ref{#def-relative-computability}), a set $A$ is **$Y$-c.e.** if $A = W^Y_e$ for some $e$, and the results on c.e. sets hold relative to $Y$: $A$ is $Y$-c.e. if and only if $A = \{ x : \exists s\ R(x, s) \}$ for some $Y$-computable relation $R$, and $A$ is $Y$-computable if and only if $A$ and $\nat \setminus A$ are $Y$-c.e.

:::proposition{#prop-ce-below-jump}
Every c.e. set is Turing reducible to $\emptyset'$. More generally, if $A$ is $Y$-c.e. and $Y \leq_T Z$, then $A$ is $Z$-c.e.
:::

:::proof{of=prop-ce-below-jump}
A c.e. set is many-one reducible to $\emptyset'$ (:ref{#thm-halting-complete}), hence Turing reducible to it. For the second statement, if $A = \{ x : \exists s\ R(x, s) \}$ with $R \leq_T Y \leq_T Z$, then $R$ is $Z$-computable and $A$ is $Z$-c.e.
:::

So the c.e. degrees, that is, the degrees of c.e. sets, all lie between $\obf$ and $\deg_T(\emptyset')$, written $\obf'$. Whether there are c.e. degrees strictly between $\obf$ and $\obf'$ is Post's problem, solved by the priority method in a later course.

## Exercises

::::exercise{difficulty=1}
Show that if $X \leq_T Y$ and $A \leq_T B$, then $X \oplus A \leq_T Y \oplus B$.

:::solution
$X \leq_T Y \leq_T Y \oplus B$ and $A \leq_T B \leq_T Y \oplus B$, so $Y \oplus B$ is an upper bound of $X$ and $A$, hence computes $X \oplus A$ by :ref{#prop-join-lub}.
:::
::::

::::exercise{difficulty=1}
Show that $X \leq_T Y$ if and only if $X \oplus (\nat \setminus X)$ is $Y$-c.e.

:::solution
If $X \leq_T Y$, then $X$ and its complement are $Y$-computable, so their join is $Y$-computable, hence $Y$-c.e. Conversely, if $X \oplus (\nat \setminus X)$ is $Y$-c.e., then $X = \{ n : 2n \in X \oplus (\nat \setminus X) \}$ and $\nat \setminus X = \{ n : 2n + 1 \in X \oplus (\nat \setminus X) \}$ are $Y$-c.e., as preimages under computable functions, so $X$ is $Y$-computable.
:::
::::

::::exercise{difficulty=2}
Let $X$ be infinite. Show that $X$ is Turing equivalent to its principal function $p_X$, used as an oracle, and to the set $\{ \langle n, p_X(n) \rangle : n \in \nat \}$.

:::solution
From $X$, compute $p_X(0) = \min X$ and $p_X(n+1) = \min \{ x > p_X(n) : x \in X \}$ by searching the oracle; the searches terminate since $X$ is infinite. Conversely, from $p_X$, decide $x \in X$ by computing $p_X(0), \dots, p_X(x)$, which exceed or reach $x$ since $p_X(n) \geq n$, and checking whether $x$ is among them. The set $\{ \langle n, p_X(n) \rangle \}$ is the graph $G_{p_X}$, equivalent to $p_X$ by definition of computation with a function oracle.
:::
::::

## Notes and references

Turing reducibility was defined by Post (1944) from Turing's oracle machines, and the degrees of unsolvability were introduced by Post and studied systematically by Kleene and Post (1954). Spector proved in 1956 that strictly increasing sequences of degrees have no least upper bound. Lerman's monograph studies the global structure of $\mathcal D$.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- M. Lerman, *Degrees of Unsolvability*, Springer, 1983.
