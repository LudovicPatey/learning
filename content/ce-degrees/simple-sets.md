---
title: Simple sets and Post's problem
summary: Post's problem; simple sets and Post's construction; productive and creative sets; simple sets are not many-one complete.
duration: 40
prerequisites: [turing-degrees/turing-reducibility, arithmetic-hierarchy/index-sets]
---

In 1944, Post observed that all the non-computable c.e. sets known at the time — the halting set, the set of theorems of a sufficiently strong computably axiomatized theory such as Peano arithmetic — are Turing equivalent to $\emptyset'$. He asked whether this is always the case.

:::definition{#def-post-problem}
**Post's problem** asks whether there is a c.e. set $A$ with $\emptyset <_T A <_T \emptyset'$, that is, a c.e. set which is neither computable nor Turing complete.
:::

Post's approach, known as **Post's program**, was to find a structural property of the complement of a c.e. set that forces the set to be incomplete. His first such property, simplicity, is the subject of this lesson. It yields c.e. sets that are not computable and not complete for many-one reducibility, but it does not settle Post's problem for Turing reducibility. That required a new method, the priority method of the next lessons.

The lesson first builds a simple set, by a construction that already has the shape of the later priority arguments. It then shows that the complement of a many-one complete set is **productive**, a property that makes it contain an infinite c.e. set; so simple sets are not many-one complete.

## Simple sets

:::definition{#def-simple}
An infinite set $C$ is **immune** if it contains no infinite c.e. subset. A c.e. set $A$ is **simple** if $\nat \setminus A$ is immune; that is, $\nat \setminus A$ is infinite and meets every infinite c.e. set.
:::

A simple set is not computable: if it were, its complement would be an infinite computable, hence c.e., subset of itself. The complement of a simple set is thin: it is infinite, but no algorithm can list infinitely many of its elements.

:::example{#ex-not-simple}
1. A cofinite set is not simple, since its complement is finite; neither is a coinfinite computable set, by the remark above.
2. The halting set $\emptyset'$ is not simple. Let $p$ be the padding function of :ref{#lem-padding} and $e_0$ an index of the nowhere defined function. The numbers $p(e_0, n)$, for $n \in \nat$, are indices of the nowhere defined function, so they lie outside $\emptyset'$; they form a c.e. set, which is infinite since $p(e_0, n) \geq n$. Every m-complete set fails to be simple for a similar reason, as shown in :ref{#thm-simple-not-complete}.
:::

*The idea of the construction.* To make $A$ simple, we satisfy for each $e$ the requirement that an infinite $W_e$ meets $A$. Putting one element of $W_e$ into $A$ suffices, so each requirement acts at most once. The danger is that the elements put into $A$ fill the complement: every number $n$ belongs to some finite $W_e$, for instance $\{ n \}$, and if each $W_e$ contributed any element, $A$ could be all of $\nat$. The remedy is a size constraint: $W_e$ may only contribute an element greater than $2e$. An infinite $W_e$ has such elements, so it is still met, and the numbers $0, \dots, 2n$ can only receive the contributions of $W_0, \dots, W_{n-1}$.

:::theorem[Post]{#thm-post-simple}
There is a simple set.
:::

:::proof{of=thm-post-simple}
For each $e$, let $x_e$ be an element $x > 2e$ of $W_e$ found by a fixed search, if there is one: the element $x$ of the least pair $\langle x, s \rangle$ (for the pairing function) with $x > 2e$ and $x \in W_e[s]$; $x_e$ is undefined if $W_e$ has no element greater than $2e$. Let $S = \{ x_e : x_e \text{ is defined} \}$.

*$S$ is c.e.* The relation "$x_e$ is defined and equal to $x$" is c.e., since it is witnessed by a finite search; $S$ is its projection.

*The complement of $S$ is infinite.* Since $x_e > 2e$, an element $x_e \leq 2n$ satisfies $e < n$. So $S \cap \{0, \dots, 2n\}$ has at most $n$ elements, and at least $n + 1$ of the numbers $0, \dots, 2n$ are outside $S$, for every $n$.

*The complement of $S$ meets every infinite c.e. set.* If $W_e$ is infinite, it has elements greater than $2e$, so $x_e$ is defined, and $x_e \in W_e \cap S$. Hence $W_e \not\subseteq \nat \setminus S$.
:::

:::figure[Post's construction on the numbers $0, \dots, 14$, for five hypothetical sets $W_0, \dots, W_4$ (dots). The set $W_e$ may only contribute an element to the right of the bar placed after $2e$; it contributes the element $x_e$ found first by the search (framed), or nothing, as $W_3$ here. Below $2n + 1$, only $W_0, \dots, W_{n-1}$ can contribute.]
<svg class="fig" viewBox="0 0 590 245" width="590" role="img" aria-label="Post's simple set: each W_e contributes at most one element, and only an element greater than 2e"><text x="83.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="109.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="135.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="161.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="187.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="213.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">5</text><text x="239.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">6</text><text x="265.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">7</text><text x="291.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">8</text><text x="317.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">9</text><text x="343.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">10</text><text x="369.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">11</text><text x="395.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">12</text><text x="421.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">13</text><text x="447.0" y="30" text-anchor="middle" class="mrm muted" font-size="11">14</text><text x="44" y="57" text-anchor="middle" class="math" font-size="16">W<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="70" y="40" width="26" height="22" class="cell"/><rect x="73" y="43" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="83.0" cy="51.0" r="4" class="ink-fill"/><rect x="96" y="40" width="26" height="22" class="cell"/><rect x="122" y="40" width="26" height="22" class="cell head-cell"/><circle cx="135.0" cy="51.0" r="4" class="ink-fill"/><rect x="148" y="40" width="26" height="22" class="cell"/><rect x="174" y="40" width="26" height="22" class="cell"/><rect x="200" y="40" width="26" height="22" class="cell"/><circle cx="213.0" cy="51.0" r="4" class="ink-fill"/><rect x="226" y="40" width="26" height="22" class="cell"/><rect x="252" y="40" width="26" height="22" class="cell"/><rect x="278" y="40" width="26" height="22" class="cell"/><rect x="304" y="40" width="26" height="22" class="cell"/><rect x="330" y="40" width="26" height="22" class="cell"/><rect x="356" y="40" width="26" height="22" class="cell"/><rect x="382" y="40" width="26" height="22" class="cell"/><rect x="408" y="40" width="26" height="22" class="cell"/><circle cx="421.0" cy="51.0" r="4" class="ink-fill"/><rect x="434" y="40" width="26" height="22" class="cell"/><line x1="96" y1="37" x2="96" y2="65" class="accent-stroke" stroke-width="2"/><text x="474" y="55" class="label"><tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">0</tspan><tspan dy="-3"> = 2</tspan></text><text x="44" y="89" text-anchor="middle" class="math" font-size="16">W<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="70" y="72" width="26" height="22" class="cell"/><rect x="73" y="75" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="96" y="72" width="26" height="22" class="cell"/><rect x="99" y="75" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="109.0" cy="83.0" r="4" class="ink-fill"/><rect x="122" y="72" width="26" height="22" class="cell"/><rect x="125" y="75" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="148" y="72" width="26" height="22" class="cell"/><rect x="174" y="72" width="26" height="22" class="cell"/><rect x="200" y="72" width="26" height="22" class="cell"/><rect x="226" y="72" width="26" height="22" class="cell head-cell"/><circle cx="239.0" cy="83.0" r="4" class="ink-fill"/><rect x="252" y="72" width="26" height="22" class="cell"/><rect x="278" y="72" width="26" height="22" class="cell"/><rect x="304" y="72" width="26" height="22" class="cell"/><circle cx="317.0" cy="83.0" r="4" class="ink-fill"/><rect x="330" y="72" width="26" height="22" class="cell"/><rect x="356" y="72" width="26" height="22" class="cell"/><rect x="382" y="72" width="26" height="22" class="cell"/><rect x="408" y="72" width="26" height="22" class="cell"/><rect x="434" y="72" width="26" height="22" class="cell"/><line x1="148" y1="69" x2="148" y2="97" class="accent-stroke" stroke-width="2"/><text x="474" y="87" class="label"><tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">1</tspan><tspan dy="-3"> = 6</tspan></text><text x="44" y="121" text-anchor="middle" class="math" font-size="16">W<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="70" y="104" width="26" height="22" class="cell"/><rect x="73" y="107" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="96" y="104" width="26" height="22" class="cell"/><rect x="99" y="107" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="122" y="104" width="26" height="22" class="cell"/><rect x="125" y="107" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="148" y="104" width="26" height="22" class="cell"/><rect x="151" y="107" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="161.0" cy="115.0" r="4" class="ink-fill"/><rect x="174" y="104" width="26" height="22" class="cell"/><rect x="177" y="107" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="187.0" cy="115.0" r="4" class="ink-fill"/><rect x="200" y="104" width="26" height="22" class="cell"/><rect x="226" y="104" width="26" height="22" class="cell"/><rect x="252" y="104" width="26" height="22" class="cell"/><rect x="278" y="104" width="26" height="22" class="cell"/><rect x="304" y="104" width="26" height="22" class="cell"/><rect x="330" y="104" width="26" height="22" class="cell"/><rect x="356" y="104" width="26" height="22" class="cell head-cell"/><circle cx="369.0" cy="115.0" r="4" class="ink-fill"/><rect x="382" y="104" width="26" height="22" class="cell"/><rect x="408" y="104" width="26" height="22" class="cell"/><rect x="434" y="104" width="26" height="22" class="cell"/><line x1="200" y1="101" x2="200" y2="129" class="accent-stroke" stroke-width="2"/><text x="474" y="119" class="label"><tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">2</tspan><tspan dy="-3"> = 11</tspan></text><text x="44" y="153" text-anchor="middle" class="math" font-size="16">W<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="70" y="136" width="26" height="22" class="cell"/><rect x="73" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="96" y="136" width="26" height="22" class="cell"/><rect x="99" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="109.0" cy="147.0" r="4" class="ink-fill"/><rect x="122" y="136" width="26" height="22" class="cell"/><rect x="125" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="148" y="136" width="26" height="22" class="cell"/><rect x="151" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="174" y="136" width="26" height="22" class="cell"/><rect x="177" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="200" y="136" width="26" height="22" class="cell"/><rect x="203" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="213.0" cy="147.0" r="4" class="ink-fill"/><rect x="226" y="136" width="26" height="22" class="cell"/><rect x="229" y="139" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="252" y="136" width="26" height="22" class="cell"/><rect x="278" y="136" width="26" height="22" class="cell"/><rect x="304" y="136" width="26" height="22" class="cell"/><rect x="330" y="136" width="26" height="22" class="cell"/><rect x="356" y="136" width="26" height="22" class="cell"/><rect x="382" y="136" width="26" height="22" class="cell"/><rect x="408" y="136" width="26" height="22" class="cell"/><rect x="434" y="136" width="26" height="22" class="cell"/><line x1="252" y1="133" x2="252" y2="161" class="accent-stroke" stroke-width="2"/><text x="474" y="151" class="label"><tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">3</tspan><tspan dy="-3"> undefined</tspan></text><text x="44" y="185" text-anchor="middle" class="math" font-size="16">W<tspan class="mrm" font-size="10" dy="4">4</tspan></text><rect x="70" y="168" width="26" height="22" class="cell"/><rect x="73" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="96" y="168" width="26" height="22" class="cell"/><rect x="99" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="122" y="168" width="26" height="22" class="cell"/><rect x="125" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="148" y="168" width="26" height="22" class="cell"/><rect x="151" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="174" y="168" width="26" height="22" class="cell"/><rect x="177" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="200" y="168" width="26" height="22" class="cell"/><rect x="203" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="226" y="168" width="26" height="22" class="cell"/><rect x="229" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><circle cx="239.0" cy="179.0" r="4" class="ink-fill"/><rect x="252" y="168" width="26" height="22" class="cell"/><rect x="255" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="278" y="168" width="26" height="22" class="cell"/><rect x="281" y="171" width="20" height="16" class="muted-fill" opacity="0.25"/><rect x="304" y="168" width="26" height="22" class="cell head-cell"/><circle cx="317.0" cy="179.0" r="4" class="ink-fill"/><rect x="330" y="168" width="26" height="22" class="cell"/><rect x="356" y="168" width="26" height="22" class="cell"/><rect x="382" y="168" width="26" height="22" class="cell"/><rect x="408" y="168" width="26" height="22" class="cell"/><rect x="434" y="168" width="26" height="22" class="cell"/><circle cx="447.0" cy="179.0" r="4" class="ink-fill"/><line x1="304" y1="165" x2="304" y2="193" class="accent-stroke" stroke-width="2"/><text x="474" y="183" class="label"><tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="3">4</tspan><tspan dy="-3"> = 9</tspan></text><text x="44" y="225" text-anchor="middle" class="math" font-size="16">S</text><rect x="70" y="208" width="26" height="22" class="cell"/><rect x="96" y="208" width="26" height="22" class="cell"/><rect x="122" y="208" width="26" height="22" class="cell head-cell"/><circle cx="135.0" cy="219.0" r="4" class="accent-fill"/><rect x="148" y="208" width="26" height="22" class="cell"/><rect x="174" y="208" width="26" height="22" class="cell"/><rect x="200" y="208" width="26" height="22" class="cell"/><rect x="226" y="208" width="26" height="22" class="cell head-cell"/><circle cx="239.0" cy="219.0" r="4" class="accent-fill"/><rect x="252" y="208" width="26" height="22" class="cell"/><rect x="278" y="208" width="26" height="22" class="cell"/><rect x="304" y="208" width="26" height="22" class="cell head-cell"/><circle cx="317.0" cy="219.0" r="4" class="accent-fill"/><rect x="330" y="208" width="26" height="22" class="cell"/><rect x="356" y="208" width="26" height="22" class="cell head-cell"/><circle cx="369.0" cy="219.0" r="4" class="accent-fill"/><rect x="382" y="208" width="26" height="22" class="cell"/><rect x="408" y="208" width="26" height="22" class="cell"/><rect x="434" y="208" width="26" height="22" class="cell"/><text x="474" y="223" class="label">contributions of e ≤ 4</text></svg>
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

:::remark{#rem-post-set-complete}
Post's set $S$ is far from incomplete. If $W_e$ is contained in the complement of $S$, then $W_e$ has no element greater than $2e$, since otherwise $x_e$ would be defined and in $W_e \cap S$; so $|W_e| \leq 2e + 1$, a bound computable from the index $e$. Sets with this property are called **effectively simple**, and Martin showed in 1966 that every effectively simple set is Turing complete; this is proved in the course on immunity and growth (:ref{#cor-arslanov}). So $S \equiv_T \emptyset'$. The simple set of the lesson on low simple sets is not effectively simple, since it is low.
:::

## Productive and creative sets

To see that a simple set is not many-one complete, we isolate the property of the complement of $\emptyset'$ that simple sets lack. The complement of $\emptyset'$ is not c.e., and this failure is **effective**: given an index of a c.e. set contained in it, one can compute an element of the complement that the c.e. set misses. This is the diagonal argument of the unsolvability of the halting problem, read as an algorithm.

:::definition{#def-productive}
A set $P$ is **productive** if there is a total computable function $p$, a **productive function** for $P$, such that for every $e$: if $W_e \subseteq P$, then $p(e) \in P \setminus W_e$. A c.e. set is **creative** if its complement is productive.
:::

A productive set is not c.e.: if $P = W_e$, then $p(e) \in P \setminus W_e = \emptyset$. More than that, every c.e. subset of $P$ is effectively witnessed to be a proper subset. Some authors allow the productive function to be partial computable, defined at least on the indices $e$ with $W_e \subseteq P$; the two definitions give the same productive sets (Soare 2016, Theorem 2.4.4).

:::proposition{#prop-halting-creative}
The halting set $\emptyset'$ is creative, with the identity as productive function for its complement.
:::

:::proof{of=prop-halting-creative}
Suppose $W_e \subseteq \nat \setminus \emptyset'$. If $e \in W_e$, then $\Phi_e(e)\converge$, so $e \in \emptyset'$, contradicting the inclusion. So $e \notin W_e$, which means $\Phi_e(e)\diverge$, that is, $e \in \nat \setminus \emptyset'$. Hence $e \in (\nat \setminus \emptyset') \setminus W_e$.
:::

The proof is a **diagonalization**: the index $e$ of the c.e. set is itself the witness that the set misses. The next lemma iterates a productive function, feeding it the finite set of witnesses already produced, so as to produce new witnesses forever.

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

:::example{#ex-creative-index}
Let $\mathcal C$ be a class of c.e. sets that contains $\emptyset$ and omits some c.e. set $W_a$, and let $I = \{ e : W_e \in \mathcal C \}$. By the parameter form of SMN, there is a total computable $g$ such that the program $g(n)$, on input $y$, first runs $\Phi_n(n)$ and, if it halts, runs $\Phi_a(y)$. Then $W_{g(n)} = W_a$ if $n \in \emptyset'$, and $W_{g(n)} = \emptyset$ otherwise; so $n \in \emptyset'$ if and only if $g(n) \in \nat \setminus I$, and $\emptyset' \leq_m \nat \setminus I$. By :ref{#prop-productive-reduction}, $I$ is productive. For instance $\{ e : W_e = \emptyset \}$ and $\{ e : W_e \text{ is finite} \}$ are productive. This strengthens Rice's theorem for such classes: $I$ is not only non-computable, it is not even c.e., and this failure is witnessed effectively.
:::

:::theorem{#thm-simple-not-complete}
No simple set is many-one complete. In particular, Post's simple set is a c.e. set which is neither computable nor m-complete.
:::

:::proof{of=thm-simple-not-complete}
If $A$ is m-complete, the complement of $A$ is productive by :ref{#prop-productive-reduction}, hence contains an infinite c.e. subset by :ref{#lem-productive-infinite}, so $A$ is not simple.
:::

The converse of the second statement of :ref{#prop-productive-reduction} also holds: Myhill showed in 1955 that the creative sets are exactly the m-complete c.e. sets, and that any two creative sets are computably isomorphic. We admit this; a proof by the fixed point theorem is in Soare's book of 2016 (Theorem 2.4.6). Simple and creative sets are thus two kinds of non-computable c.e. sets at opposite ends: the complement of a creative set contains an infinite c.e. set, which can even be produced effectively, while the complement of a simple set contains none.

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

  It is not many-one complete. Simple sets can be Turing complete: Post's own simple set is (:ref{#rem-post-set-complete}).
- [x] No: it concerns many-one reducibility, and some simple sets are Turing equivalent to $\emptyset'$.

  Post's problem asks about Turing reducibility. It was solved by the priority method.
:::

Post introduced stronger thinness properties, such as **hypersimplicity**, and showed that hypersimple sets are not complete for truth-table reducibility, a reducibility between many-one and Turing. But the thinness properties Post considered do not ensure Turing incompleteness: Dekker showed that every non-computable c.e. set is Turing equivalent to a hypersimple set (Dekker 1954; :ref{#thm-deficiency-set} in the course on immunity and growth), so that Post's program in its original form could not succeed. In a revised form, it did succeed much later: Harrington and Soare (1991) found a property of c.e. sets, definable in the lattice of c.e. sets under inclusion, which is satisfied by some non-computable c.e. sets and by no Turing complete one.

## Exercises

::::exercise{#ex-simple-join difficulty=1 objective="Check that the join of two simple sets is simple."}
Show that the join $A \oplus B$ of two simple sets is simple.

:::solution
$A \oplus B$ is c.e., and its complement $\{ 2n : n \notin A \} \cup \{ 2n + 1 : n \notin B \}$ is infinite. Let $W$ be an infinite c.e. set contained in the complement. Then $W$ contains infinitely many even numbers or infinitely many odd numbers. In the first case, $\{ n : 2n \in W \}$ is an infinite c.e. set contained in $\nat \setminus A$, contradicting the simplicity of $A$; the second case is symmetric.
:::
::::

::::exercise{#ex-simple-index-set difficulty=2 objective="Count quantifiers to place the index set of the simple sets in the arithmetic hierarchy." lessons="arithmetic-hierarchy/index-sets"}
Show that the index set $\{ e : W_e \text{ is simple} \}$ is $\Pi^0_3$.

:::solution
$W_e$ is simple if and only if its complement is infinite and $\forall i\ (W_i \text{ infinite} \to W_i \cap W_e \neq \emptyset)$. The first condition is "$\forall n\ \exists x > n\ x \notin W_e$", which is $\Pi^0_3$: the relation $x \notin W_e$ is $\Pi^0_1$, so $\exists x > n\ x \notin W_e$ is $\Sigma^0_2$. In the second condition, "$W_i$ infinite" is $\Pi^0_2$ and "$W_i \cap W_e \neq \emptyset$" is $\Sigma^0_1$, so the implication is $\Sigma^0_2$, and its universal closure is $\Pi^0_3$. The conjunction of two $\Pi^0_3$ conditions is $\Pi^0_3$.
:::
::::

## Notes and references

Post's problem, simple sets and the program of finding thinness properties of complements are in Post's paper of 1944, which also introduced creative sets. Productive sets are due to Dekker (1955), and the characterization of creative sets as m-complete sets to Myhill (1955). The completeness of effectively simple sets is due to Martin (1966), and the eventual success of Post's program in a revised form to Harrington and Soare (1991). Soare's book of 2016 presents productive and creative sets in Section 2.4, Post's problem and Post's program in Section 5.1, simple sets in Section 5.2 (Post's construction is Theorem 5.2.3), hypersimple sets and Dekker's theorem in Section 5.3, and Martin's theorem in Section 5.4 (Theorem 5.4.1). Nies presents Post's construction and its effective simplicity in Section 1.6 of his book.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- J. C. E. Dekker, *A theorem on hypersimple sets*, Proceedings of the American Mathematical Society 5 (1954), 791–796.
- J. C. E. Dekker, *Productive sets*, Transactions of the American Mathematical Society 78 (1955), 129–149.
- J. Myhill, *Creative sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 1 (1955), 97–108.
- D. A. Martin, *Completeness, the recursion theorem and effectively simple sets*, Proceedings of the American Mathematical Society 17 (1966), 838–842.
- L. Harrington and R. I. Soare, *Post's program and incomplete recursively enumerable sets*, Proceedings of the National Academy of Sciences of the USA 88 (1991), 10242–10246.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.

:::::exercises
::::exercise{#ex-creative-not-ce difficulty=1 objective="Derive from the definition that a creative set is not computable."}
Show that every creative set is not computable, and that its complement is not c.e.

:::solution
Let $p$ be a productive function for the complement $P$ of the creative set. If $P = W_e$, then $W_e \subseteq P$ gives $p(e) \in P \setminus W_e = \emptyset$, a contradiction. So $P$ is not c.e., and the creative set, whose complement is not c.e., is not computable.
:::
::::

::::exercise{#ex-simple-filter difficulty=1 objective="Check that simple sets are closed under finite intersections and, up to cofinite sets, under c.e. supersets."}
Let $A$ and $B$ be simple sets. Show that $A \cap B$ is simple, and that every c.e. set $C \supseteq A$ is either simple or cofinite.

:::solution
*Supersets.* The complement of $C$ is contained in the complement of $A$. If it is finite, $C$ is cofinite. Otherwise, an infinite c.e. subset of $\nat \setminus C$ would be an infinite c.e. subset of $\nat \setminus A$, and there is none; so $C$ is simple.

*Intersections.* $A \cap B$ is c.e., and its complement $(\nat \setminus A) \cup (\nat \setminus B)$ contains $\nat \setminus A$, so it is infinite. Let $W$ be an infinite c.e. set contained in $(\nat \setminus A) \cup (\nat \setminus B)$. The set $W \cap A$ is c.e., and contained in $\nat \setminus B$, since an element of $W$ that lies in $A$ must lie outside $B$. As $B$ is simple, $W \cap A$ is finite. Then $W \setminus A = W \setminus (W \cap A)$ is an infinite set, c.e. since it is obtained from $W$ by removing finitely many elements, and contained in $\nat \setminus A$. This contradicts the simplicity of $A$. So $A \cap B$ is simple.

Soare (2016, Exercise 5.2.9) states this as follows: the simple sets and the cofinite sets together form a filter in the lattice of c.e. sets.
:::
::::

::::exercise{#ex-tot-productive difficulty=1 objective="Apply the transfer of productivity along many-one reductions to the index set of the total functions."}
Let $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$. Show that $\mathrm{Tot}$ and $\nat \setminus \mathrm{Tot}$ are both productive.

:::solution
By the parameter form of SMN, there are total computable functions $f$ and $g$ such that, for all $n$ and $y$:

- $\Phi_{f(n)}(y)$ runs $\Phi_n(n)$ for $y$ steps; if the computation has halted within these steps, it loops forever, and otherwise it outputs $0$;
- $\Phi_{g(n)}(y)$ runs $\Phi_n(n)$ and, if it halts, outputs $0$.

If $\Phi_n(n)\diverge$, then $\Phi_{f(n)}$ is total; if $\Phi_n(n)$ halts after $t$ steps, then $\Phi_{f(n)}(y)\diverge$ for every $y \geq t$. So $n \in \emptyset'$ if and only if $f(n) \in \nat \setminus \mathrm{Tot}$, that is, $\emptyset' \leq_m \nat \setminus \mathrm{Tot}$. Since $\nat \setminus \emptyset'$ is productive (:ref{#prop-halting-creative}), :ref{#prop-productive-reduction} shows that the complement of $\nat \setminus \mathrm{Tot}$, which is $\mathrm{Tot}$, is productive.

Similarly, $\Phi_{g(n)}$ is total if $n \in \emptyset'$ and nowhere defined otherwise, so $\emptyset' \leq_m \mathrm{Tot}$ via $g$, and $\nat \setminus \mathrm{Tot}$ is productive. In particular neither $\mathrm{Tot}$ nor its complement is c.e., and the failure is effective on both sides.
:::
::::

::::exercise{#ex-productive-uniform difficulty=2 objective="Make the proof that productive sets contain infinite c.e. sets uniform, and avoid a given c.e. subset."}
Let $P$ be a productive set. Show that there is a total computable function $f$ such that for every $e$: if $W_e \subseteq P$, then $W_{f(e)}$ is an infinite subset of $P$ disjoint from $W_e$.

:::solution
Let $p$ be a productive function for $P$. By the parameter form of SMN, there is a total computable $h$ with $W_{h(e, n)} = W_e \cup D_n$ for all $e$ and $n$, where $D_n$ is the finite set of canonical index $n$: the program $h(e, n)$, on input $y$, halts at once if $y \in D_n$, and otherwise runs $\Phi_e(y)$.

For each $e$, define by recursion on $k$:
$$
x^e_0 = p(h(e, 0)), \qquad x^e_{k+1} = p(h(e, n^e_k)),
$$
where $n^e_k$ is the canonical index of $\{ x^e_0, \dots, x^e_k \}$, and $D_0 = \emptyset$. Since $p$ and $h$ are total, $(e, k) \mapsto x^e_k$ is total computable, and by the parameter form of SMN there is a total computable $f$ with $W_{f(e)} = \{ x^e_k : k \in \nat \}$. The function $f$ is defined for every $e$, including those with $W_e \not\subseteq P$; this is necessary, since the inclusion $W_e \subseteq P$ cannot be decided.

Suppose $W_e \subseteq P$. We show by induction on $k$ that $x^e_k \in P \setminus W_e$ and $x^e_k \notin \{ x^e_0, \dots, x^e_{k-1} \}$. Assume it for all $j < k$. Then $W_e \cup \{ x^e_0, \dots, x^e_{k-1} \} \subseteq P$, and this set is $W_{h(e, m)}$ for the index $m$ used to define $x^e_k$. As $p$ is productive, $x^e_k = p(h(e, m))$ belongs to $P$ and not to $W_e \cup \{ x^e_0, \dots, x^e_{k-1} \}$. So the $x^e_k$ are pairwise distinct elements of $P \setminus W_e$, and $W_{f(e)}$ is an infinite subset of $P$ disjoint from $W_e$.

Adapted from Soare 2016, Exercise 2.4.10. With $W_e = \emptyset$, this is :ref{#lem-productive-infinite}.
:::
::::

::::exercise{#ex-inseparable-not-simple difficulty=2 objective="Prove that simple sets are not many-one complete through a computably inseparable pair, without productive sets."}
Two disjoint c.e. sets $C$ and $D$ are **computably inseparable** if there is no computable set $R$ with $C \subseteq R$ and $R \cap D = \emptyset$.

1. Show that $C = \{ e : \Phi_e(e)\converge = 0 \}$ and $D = \{ e : \Phi_e(e)\converge = 1 \}$ are computably inseparable.
2. Let $(C, D)$ be a computably inseparable pair and $S$ a c.e. set with $C \leq_m S$. Show that $S$ is not simple.
3. Deduce :ref{#thm-simple-not-complete}.

:::solution
1. Suppose $R$ is computable, $C \subseteq R$ and $R \cap D = \emptyset$. Let $e$ be an index of the total computable function equal to $1$ on $R$ and to $0$ outside $R$. If $e \in R$, then $\Phi_e(e) = 1$, so $e \in D$, which contradicts $R \cap D = \emptyset$. If $e \notin R$, then $\Phi_e(e) = 0$, so $e \in C \subseteq R$, a contradiction.

2. Let $f$ be a computable function with $x \in C \iff f(x) \in S$. The set $f(D) = \{ f(x) : x \in D \}$ is c.e. If $x \in D$, then $x \notin C$, so $f(x) \notin S$: hence $f(D) \subseteq \nat \setminus S$. Suppose $f(D)$ is finite. Then $R = \{ x : f(x) \notin f(D) \}$ is computable, since $f$ is computable and $f(D)$ is a fixed finite set. It contains $C$, because $x \in C$ gives $f(x) \in S$, while $f(D) \cap S = \emptyset$; and it is disjoint from $D$, by definition. This contradicts the inseparability of $(C, D)$. So $f(D)$ is an infinite c.e. subset of $\nat \setminus S$, and $S$ is not simple.

3. If $S$ is m-complete, then $C \leq_m S$ for the c.e. set $C$ of item 1, and $S$ is not simple by items 1 and 2.

Adapted from Soare 2016, Exercise 5.2.11.
:::
::::
:::::
