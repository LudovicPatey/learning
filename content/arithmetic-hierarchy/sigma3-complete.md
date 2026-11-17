---
title: Σ⁰₃-complete sets
summary: Cof and Rec are Σ⁰₃-complete; marker constructions, and coding the halting set into the complement.
duration: 35
prerequisites: [index-sets]
---

At the third level, the classification of index sets requires constructions in stages. This lesson proves that the set $\mathrm{Cof}$ of indices of cofinite c.e. sets is $\Sigma^0_3$-complete, with a **marker argument**, and that the set $\mathrm{Rec}$ of indices of computable c.e. sets is $\Sigma^0_3$-complete, by adding to the same construction a strategy that codes $\emptyset'$. Both techniques recur in the study of c.e. sets and degrees.

## Cofinite sets

A $\Sigma^0_3$ statement $\exists n\ P(x, n)$, with $P$ in $\Pi^0_2$, is reduced to the question whether one of the c.e. sets $W_{g(x, 0)}, W_{g(x, 1)}, \dots$ is infinite, by :ref{#thm-fin-complete}. The set $V_x$ must then be cofinite if one of them is infinite, and coinfinite if all are finite. Its complement is controlled through **markers**, the numbers not yet enumerated: each new element of $W_{g(x, n)}$ is used to enumerate the markers beyond the first $n$. If $W_{g(x, n)}$ is infinite, this happens infinitely often and at most $n$ markers survive. If every set is finite, each marker is disturbed only finitely often, and infinitely many markers survive, provided the marker of rank $k$ can only be disturbed by the finitely many $n \leq k$. Arranging this is the point of the construction.

:::theorem{#thm-cof-complete}
The set $\mathrm{Cof} = \{ e : W_e \text{ is cofinite} \}$ is $\Sigma^0_3$-complete.
:::

:::proof{of=thm-cof-complete}
$\mathrm{Cof}$ is $\Sigma^0_3$ by :ref{#ex-arithmetic-examples}. Let $A$ be $\Sigma^0_3$: $x \in A \iff \exists n\ P(x, n)$ with $P$ a $\Pi^0_2$ relation. By :ref{#thm-fin-complete}, $\mathrm{Inf}$ is $\Pi^0_2$-complete, so there is a computable $g$ with $P(x, n) \iff W_{g(x, n)}$ is infinite. We build, uniformly in $x$, a c.e. set $V_x$ which is cofinite if and only if some $W_{g(x, n)}$ is infinite.

*Construction.* We enumerate $V_x$ by stages, starting with $V_x[0] = \emptyset$. At stage $s + 1$, let $n$ be the least $n \leq s$ such that $W_{g(x, n)}[s + 1] \neq W_{g(x, n)}[s]$, if there is one; we say that $n$ **acts** at stage $s + 1$. In that case, list the elements of $\{0, \dots, s - 1\} \setminus V_x[s]$ in increasing order, and enumerate into $V_x$ all of them except the first $n$. If no $n \leq s$ acts, do nothing. The construction is computable uniformly in $x$, so there is a computable $h$ with $W_{h(x)} = V_x$.

The numbers not in $V_x$ at stage $s$, in increasing order, are called the **markers** at stage $s$. A stage at which $n$ acts keeps the first $n$ markers below $s$ and removes the others.

*If some $W_{g(x, n)}$ is infinite, $V_x$ is cofinite.* Fix such an $n$. Then $W_{g(x, n)}$ receives new elements at infinitely many stages, and at each of them some $n' \leq n$ acts. Suppose $m_0 < m_1 < \dots < m_n$ are $n + 1$ numbers outside $V_x$. Take a stage $s + 1$ with $s > m_n$ at which some $n' \leq n$ acts. The numbers $m_0, \dots, m_n$ are all below $s$ and outside $V_x[s]$, and $m_n$ is not among the first $n$ markers below $s$, since $m_0, \dots, m_{n-1}$ precede it. So $m_n$ is enumerated into $V_x$, a contradiction. Hence the complement of $V_x$ has at most $n$ elements.

*If every $W_{g(x, n)}$ is finite, $V_x$ is coinfinite.* We show that for every $k$, the $k$-th marker (counting from $0$) eventually reaches a final value. Only actions of some $n \leq k$ remove the $k$-th marker or a smaller one, since an action of $n$ keeps the first $n$ markers. Each $n \leq k$ acts only finitely often, since $W_{g(x, n)}$ is finite. After the last action of the numbers $n \leq k$, the first $k + 1$ markers are never removed: they are final. So the complement of $V_x$ contains the final values of all markers, and is infinite.

Hence $x \in A \iff h(x) \in \mathrm{Cof}$.
:::

The construction is a first example of a **marker argument**: each $n$ may, when it acts, destroy all the markers below the current stage except the first $n$. If some $n$ acts infinitely often, at most $n$ markers survive; if every $n$ acts finitely often, each marker settles. Arguments of this kind, with priorities between the actors, are the subject of the course on Post's problem.

:::figure[A run of the construction of $V_x$, showing only the stages at which some number acts. In each row, the vertical bar marks the current stage $s$: only the numbers to its left are handled. When $n$ acts, the markers to the left of the bar, except the first $n$, are enumerated into $V_x$. Here $1$ acts again and again, and only the marker $0$ survives.]
<svg class="fig" viewBox="0 0 530 236" width="530" role="img" aria-label="A run of the marker construction: at each acting stage, the numbers below the stage outside V, except the first n, are enumerated into V"><text x="165.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="195.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="225.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="255.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="285.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">4</text><text x="315.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">5</text><text x="345.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">6</text><text x="375.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">7</text><text x="405.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">8</text><text x="435.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">9</text><text x="465.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">10</text><text x="495.0" y="30" text-anchor="middle" class="mrm muted" font-size="13">11</text><text x="10" y="60" class="label">stage 4: <tspan class="math" font-size="14">n</tspan><tspan class="mrm" font-size="14" dx="4">=&#160;2</tspan><tspan dx="4">acts</tspan></text><rect x="150" y="40" width="30" height="30" class="cell"/><circle cx="165.0" cy="55.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="180" y="40" width="30" height="30" class="cell"/><circle cx="195.0" cy="55.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="210" y="40" width="30" height="30" class="cell head-cell"/><rect x="240" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="270" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="300" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="330" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="360" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="390" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="420" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="450" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="480" y="40" width="30" height="30" class="cell" stroke-dasharray="2 3"/><line x1="240" y1="38" x2="240" y2="72" class="accent-stroke" stroke-width="2"/><text x="10" y="90" class="label">stage 6: <tspan class="math" font-size="14">n</tspan><tspan class="mrm" font-size="14" dx="4">=&#160;1</tspan><tspan dx="4">acts</tspan></text><rect x="150" y="70" width="30" height="30" class="cell"/><circle cx="165.0" cy="85.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="180" y="70" width="30" height="30" class="cell head-cell"/><rect x="210" y="70" width="30" height="30" class="cell"/><rect x="211" y="71" width="28" height="28" class="soft-fill"/><rect x="240" y="70" width="30" height="30" class="cell head-cell"/><rect x="270" y="70" width="30" height="30" class="cell head-cell"/><rect x="300" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="330" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="360" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="390" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="420" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="450" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="480" y="70" width="30" height="30" class="cell" stroke-dasharray="2 3"/><line x1="300" y1="68" x2="300" y2="102" class="accent-stroke" stroke-width="2"/><text x="10" y="120" class="label">stage 8: <tspan class="math" font-size="14">n</tspan><tspan class="mrm" font-size="14" dx="4">=&#160;2</tspan><tspan dx="4">acts</tspan></text><rect x="150" y="100" width="30" height="30" class="cell"/><circle cx="165.0" cy="115.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="180" y="100" width="30" height="30" class="cell"/><rect x="181" y="101" width="28" height="28" class="soft-fill"/><rect x="210" y="100" width="30" height="30" class="cell"/><rect x="211" y="101" width="28" height="28" class="soft-fill"/><rect x="240" y="100" width="30" height="30" class="cell"/><rect x="241" y="101" width="28" height="28" class="soft-fill"/><rect x="270" y="100" width="30" height="30" class="cell"/><rect x="271" y="101" width="28" height="28" class="soft-fill"/><rect x="300" y="100" width="30" height="30" class="cell"/><circle cx="315.0" cy="115.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="330" y="100" width="30" height="30" class="cell head-cell"/><rect x="360" y="100" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="390" y="100" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="420" y="100" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="450" y="100" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="480" y="100" width="30" height="30" class="cell" stroke-dasharray="2 3"/><line x1="360" y1="98" x2="360" y2="132" class="accent-stroke" stroke-width="2"/><text x="10" y="150" class="label">stage 10: <tspan class="math" font-size="14">n</tspan><tspan class="mrm" font-size="14" dx="4">=&#160;1</tspan><tspan dx="4">acts</tspan></text><rect x="150" y="130" width="30" height="30" class="cell"/><circle cx="165.0" cy="145.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="180" y="130" width="30" height="30" class="cell"/><rect x="181" y="131" width="28" height="28" class="soft-fill"/><rect x="210" y="130" width="30" height="30" class="cell"/><rect x="211" y="131" width="28" height="28" class="soft-fill"/><rect x="240" y="130" width="30" height="30" class="cell"/><rect x="241" y="131" width="28" height="28" class="soft-fill"/><rect x="270" y="130" width="30" height="30" class="cell"/><rect x="271" y="131" width="28" height="28" class="soft-fill"/><rect x="300" y="130" width="30" height="30" class="cell head-cell"/><rect x="330" y="130" width="30" height="30" class="cell"/><rect x="331" y="131" width="28" height="28" class="soft-fill"/><rect x="360" y="130" width="30" height="30" class="cell head-cell"/><rect x="390" y="130" width="30" height="30" class="cell head-cell"/><rect x="420" y="130" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="450" y="130" width="30" height="30" class="cell" stroke-dasharray="2 3"/><rect x="480" y="130" width="30" height="30" class="cell" stroke-dasharray="2 3"/><line x1="420" y1="128" x2="420" y2="162" class="accent-stroke" stroke-width="2"/><text x="10" y="180" class="label">stage 12: <tspan class="math" font-size="14">n</tspan><tspan class="mrm" font-size="14" dx="4">=&#160;1</tspan><tspan dx="4">acts</tspan></text><rect x="150" y="160" width="30" height="30" class="cell"/><circle cx="165.0" cy="175.0" r="7" class="ink-stroke" stroke-width="1.3"/><rect x="180" y="160" width="30" height="30" class="cell"/><rect x="181" y="161" width="28" height="28" class="soft-fill"/><rect x="210" y="160" width="30" height="30" class="cell"/><rect x="211" y="161" width="28" height="28" class="soft-fill"/><rect x="240" y="160" width="30" height="30" class="cell"/><rect x="241" y="161" width="28" height="28" class="soft-fill"/><rect x="270" y="160" width="30" height="30" class="cell"/><rect x="271" y="161" width="28" height="28" class="soft-fill"/><rect x="300" y="160" width="30" height="30" class="cell"/><rect x="301" y="161" width="28" height="28" class="soft-fill"/><rect x="330" y="160" width="30" height="30" class="cell"/><rect x="331" y="161" width="28" height="28" class="soft-fill"/><rect x="360" y="160" width="30" height="30" class="cell"/><rect x="361" y="161" width="28" height="28" class="soft-fill"/><rect x="390" y="160" width="30" height="30" class="cell"/><rect x="391" y="161" width="28" height="28" class="soft-fill"/><rect x="420" y="160" width="30" height="30" class="cell head-cell"/><rect x="450" y="160" width="30" height="30" class="cell head-cell"/><rect x="480" y="160" width="30" height="30" class="cell" stroke-dasharray="2 3"/><line x1="480" y1="158" x2="480" y2="192" class="accent-stroke" stroke-width="2"/><rect x="150" y="204" width="16" height="16" class="cell head-cell"/><text x="172" y="217" class="label">enumerated at this stage</text><rect x="320" y="204" width="16" height="16" class="cell"/><rect x="321" y="205" width="14" height="14" class="soft-fill"/><text x="342" y="217" class="label">already in V</text><circle cx="433" cy="212" r="7" class="ink-stroke" stroke-width="1.3"/><text x="447" y="217" class="label">marker</text></svg>
:::

:::quiz[the marker argument]
Why does an action of $n$ keep the first $n$ markers instead of removing all of them?

- [x] So that the marker of rank $k$ can only be removed by actions of the finitely many $n \leq k$, which is what makes every marker settle when all the sets $W_{g(x, n)}$ are finite.

  Infinitely many different $n$ may act, each finitely often. If every action removed all markers, the markers would be disturbed infinitely often even when every $W_{g(x, n)}$ is finite, and $V_x$ could be cofinite in that case.
- [ ] To make $V_x$ c.e.

  $V_x$ is c.e. however the markers are handled.
- [ ] Because the first $n$ markers belong to $W_{g(x, n)}$.

  Markers are numbers outside $V_x$; they are unrelated to the elements of $W_{g(x, n)}$.

---

Why is the least acting $n$ chosen at each stage?

- [x] So that, at every stage where $W_{g(x, n)}$ receives a new element, the action keeps at most $n$ markers.

  The acting number $n'$ is then at most $n$; with another choice, a larger number could act at that stage and keep more markers.
- [ ] To make the construction terminate.

  Each stage is finite in any case.
- [ ] Because $W_{g(x, 0)}$ is always infinite.

  Nothing is assumed about $W_{g(x, 0)}$; any of the sets may be finite or infinite.
:::

:::remark{#rem-one-marker}
Soare (*Turing Computability*, Theorem 4.3.3) uses a variant: when $W_{g(x, n)}$ receives a new element, only the marker of rank $n$ is enumerated, and the next marker takes its rank. If $W_{g(x, n)}$ is infinite, the marker of rank $n$ moves infinitely often, so at most $n$ markers are final; if all the sets are finite, the marker of rank $k$ settles once the markers of rank less than $k$ have settled and $W_{g(x, k)}$ has stopped growing. The two constructions rest on the same principle: the marker of rank $k$ is disturbed only on behalf of the finitely many $n \leq k$.
:::

::::exercise{#ex-coinf-inf difficulty=2 objective="Modify the reduction to $\mathrm{Cof}$ by a join with a fixed set, to classify the infinite coinfinite c.e. sets."}
1. Show that $\{ e : W_e \text{ is infinite and coinfinite} \}$ is $\Pi^0_3$-complete.
2. Deduce that $\mathrm{Fin} \cup \mathrm{Cof}$, the set of indices of c.e. sets that are finite or cofinite, is $\Sigma^0_3$-complete.

:::solution
1. Let $B$ be the set. $W_e$ is infinite is $\Pi^0_2$, hence $\Pi^0_3$, and $W_e$ is coinfinite is the complement of $\mathrm{Cof}$, which is $\Sigma^0_3$ (:ref{#ex-arithmetic-examples}); so $B$ is $\Pi^0_3$. Let $C$ be $\Pi^0_3$, and $A = \nat \setminus C$, a $\Sigma^0_3$ set. Let $h$ be the function built in the proof of :ref{#thm-cof-complete} for $A$: $W_{h(x)}$ is cofinite if $x \in A$ and coinfinite if $x \notin A$. The proof does not exclude that $W_{h(x)}$ is finite, so we join it with an infinite set. By :ref{#cor-smn-parameters}, there is a computable $k$ with
$$
W_{k(x)} = \{ 2m : m \in W_{h(x)} \} \cup \{ 2m + 1 : m \in \nat \}.
$$
Every $W_{k(x)}$ is infinite, and its complement is $\{ 2m : m \notin W_{h(x)} \}$, which is infinite if and only if $W_{h(x)}$ is coinfinite. So $x \in C \iff x \notin A \iff W_{h(x)}$ is coinfinite $\iff k(x) \in B$.
2. $\mathrm{Fin} \cup \mathrm{Cof}$ is the union of a $\Sigma^0_2$ and a $\Sigma^0_3$ set, hence $\Sigma^0_3$, and it is the complement of $B$. With $A$ and $k$ as in item 1, $x \in A \iff k(x) \notin B \iff k(x) \in \mathrm{Fin} \cup \mathrm{Cof}$.
:::
::::

## Computable sets

The set $\mathrm{Rec} = \{ e : W_e \text{ is computable} \}$ is $\Sigma^0_3$ (:ref{#ex-rec-sigma3}). A cofinite set is computable, so the reduction of :ref{#thm-cof-complete} already sends the elements of a $\Sigma^0_3$ set $A$ into $\mathrm{Rec}$. For $x \notin A$, the set $V_x$ is coinfinite, but it may well be computable. The construction is therefore modified so that, in that case, $V_x$ also computes $\emptyset'$. Coding $\emptyset'$ costs little: when $k$ enters $\emptyset'$, the number $k$ acts once more. This adds at most one action for each $k$, so the markers still settle, and the final position of the markers then tells when the enumeration of $\emptyset'$ below $k$ is complete. This is a **coding** strategy added to the marker argument; it only uses actions that are harmless when the main strategy wins.

:::theorem[Rogers]{#thm-rec-complete}
The set $\mathrm{Rec} = \{ e : W_e \text{ is computable} \}$ is $\Sigma^0_3$-complete. More precisely, for every $\Sigma^0_3$ set $A$ there is a computable $h$ such that $W_{h(x)}$ is cofinite if $x \in A$, and Turing equivalent to $\emptyset'$ if $x \notin A$.
:::

:::proof{of=thm-rec-complete}
Let $g$ be as in the proof of :ref{#thm-cof-complete}, with $x \in A \iff \exists n\ W_{g(x, n)}$ infinite, and let $\emptyset'[s] = \{ k : \Phi_k(k)[s]\converge \}$. The construction of $V_x$ is the same, except that at stage $s + 1$ a number $n \leq s$ **acts** if $W_{g(x, n)}[s + 1] \neq W_{g(x, n)}[s]$ or $n \in \emptyset'[s + 1] \setminus \emptyset'[s]$; as before, the least acting $n$ keeps the first $n$ markers below $s$ and enumerates the others. Let $h$ be computable with $W_{h(x)} = V_x$.

*If $x \in A$.* Some $W_{g(x, n)}$ is infinite, so at infinitely many stages some $n' \leq n$ acts. The argument of :ref{#thm-cof-complete} used nothing else, so $V_x$ has at most $n$ non-elements: it is cofinite, hence computable.

*If $x \notin A$.* Each $n$ acts only finitely often: when $W_{g(x, n)}$ grows, which happens finitely often, and at the stage at which $n$ enters $\emptyset'$, if it does. The argument of :ref{#thm-cof-complete} shows that each marker reaches a final value, so the complement of $V_x$ is infinite; let $c_0 < c_1 < \cdots$ be its elements, the final markers. We show $\emptyset' \leq_T V_x$. Given $k$, compute with the oracle $V_x$ the elements $c_0 < \dots < c_k$, by searching for the first $k + 1$ numbers outside $V_x$, then a stage $s > c_k$ such that $V_x[s] \cap [0, c_k] = V_x \cap [0, c_k]$. We claim that $k \in \emptyset' \iff k \in \emptyset'[s]$. Suppose that $k$ enters $\emptyset'$ at a stage $t + 1$ with $t \geq s$. Since $k \leq c_k < s \leq t$, the number $k$ acts at stage $t + 1$, and the least acting $n'$ satisfies $n' \leq k$. At stage $t$, the numbers $c_0 < \dots < c_k$ are the first $k + 1$ markers, and all are below $t$. The action of $n' \leq k$ enumerates the marker of rank $k$, that is $c_k$, into $V_x$: a contradiction. So $\emptyset' \leq_T V_x$, and $V_x \leq_T \emptyset'$ since $V_x$ is c.e. In particular $V_x$ is not computable.

Hence $x \in A \iff h(x) \in \mathrm{Rec}$, and $\mathrm{Rec}$ is $\Sigma^0_3$-complete.
:::

:::quiz[the coding strategy]
In the proof of :ref{#thm-rec-complete}, why do the extra actions not make $V_x$ cofinite when $x \notin A$?

- [x] Each $k$ enters $\emptyset'$ at most once, so it causes at most one extra action of $k$, and each $n$ still acts only finitely often.

  The proof that every marker settles only needs each $n$ to act finitely often.
- [ ] Because $\emptyset'$ is not computable.

  The argument would be the same for any c.e. set in place of $\emptyset'$; what matters is that each element enters once.
- [ ] Because the extra actions only enumerate numbers already in $V_x$.

  An action enumerates markers, which are by definition not yet in $V_x$.

---

How does the oracle $V_x$ know that the marker of rank $k$ has reached its final value $c_k$?

- [x] The final markers are the elements of the complement of $V_x$, so $c_0, \dots, c_k$ are read off $V_x$; a stage at which $V_x$ is correct up to $c_k$ is then found by comparing the enumeration with $V_x$.
- [ ] By waiting until $k$ enters $\emptyset'$.

  This is what the oracle is trying to decide; $k$ may never enter $\emptyset'$.
- [ ] It does not need to: $c_k = k$.

  The markers are usually far larger than their rank.
:::


::::exercise{#ex-cof-rec-hard difficulty=1 objective="Use the two outcomes of the reduction to $\mathrm{Rec}$ to obtain lower bounds for other index sets."}
Let $B$ be a set of indices that contains every index of a cofinite set and no index of a set Turing equivalent to $\emptyset'$.

1. Show that every $\Sigma^0_3$ set is many-one reducible to $B$, and that $B$ is not $\Pi^0_3$.
2. Deduce that the sets $\{ e : W_e \text{ is low} \}$ and $\{ e : W_e <_T \emptyset' \}$ are not $\Pi^0_3$, where a set $X$ is low if $X' \leq_T \emptyset'$, and that every $\Pi^0_3$ set is many-one reducible to $\{ e : W_e \equiv_T \emptyset' \}$.

:::solution
1. Let $A$ be $\Sigma^0_3$, and $h$ as in :ref{#thm-rec-complete}. If $x \in A$, $W_{h(x)}$ is cofinite, so $h(x) \in B$; if $x \notin A$, $W_{h(x)} \equiv_T \emptyset'$, so $h(x) \notin B$. Hence $A \leq_m B$. If $B$ were $\Pi^0_3$, every $\Sigma^0_3$ set would be $\Pi^0_3$ (:ref{#prop-sigma1-delta1}), contradicting :ref{#cor-hierarchy-strict}.
2. A cofinite set is computable, hence low and strictly below $\emptyset'$. A set $X \equiv_T \emptyset'$ is not low, since $X' \equiv_T \emptyset''$ and $\emptyset'' \not\leq_T \emptyset'$ (:ref{#thm-jump}), and it is not strictly below $\emptyset'$. So both sets satisfy the hypothesis on $B$. Finally, the set $\{ e : W_e \equiv_T \emptyset' \}$ contains every index of a set Turing equivalent to $\emptyset'$ and no index of a cofinite set, so with $h$ as above, $x \notin A \iff h(x) \in \{ e : W_e \equiv_T \emptyset' \}$, for every $\Sigma^0_3$ set $A$; the complements of the $\Sigma^0_3$ sets are the $\Pi^0_3$ sets.
:::
::::

## Summary

The following table collects the classification of the basic index sets, proved in this lesson, in the previous one, or in their exercises.

| Set | Definition | Complete for |
| --- | --- | --- |
| $\emptyset'$, $\{ e : W_e \neq \emptyset \}$ | $\Phi_e(e)\converge$; $\exists x\ x \in W_e$ | $\Sigma^0_1$ |
| $\{ e : W_e = \emptyset \}$ | $\forall x\ x \notin W_e$ | $\Pi^0_1$ |
| $\mathrm{Fin}$ | $\exists n\ \forall x > n\ \ x \notin W_e$ | $\Sigma^0_2$ |
| $\mathrm{Inf}$, $\mathrm{Tot}$, $\{ e : W_e = \nat \}$ | $\forall n\ \exists x > n\ \ x \in W_e$; $\forall x\ \Phi_e(x)\converge$ | $\Pi^0_2$ |
| $\mathrm{Cof}$ | $\exists n\ \forall x > n\ \ x \in W_e$ | $\Sigma^0_3$ |
| $\mathrm{Rec}$ | $\exists i\ \forall x\ (\Phi_i(x)\converge = 1 \leftrightarrow x \in W_e,\ \Phi_i(x)\converge = 0 \leftrightarrow x \notin W_e)$ | $\Sigma^0_3$ |

The degrees follow by :ref{#thm-post}: a $\Sigma^0_n$-complete or $\Pi^0_n$-complete set is Turing equivalent to $\emptyset^{(n)}$. So $\mathrm{Fin}$, $\mathrm{Inf}$ and $\mathrm{Tot}$ have the degree of $\emptyset''$, and $\mathrm{Cof}$ and $\mathrm{Rec}$ that of $\emptyset'''$.


## Notes and references

The $\Sigma^0_3$-completeness of $\mathrm{Cof}$ is in Soare's *Turing Computability* (Theorem 4.3.3), with the one-marker variant of :ref{#rem-one-marker}, and in Downey and Hirschfeldt (Theorem 2.6.5); Nies lists the completeness of $\mathrm{Cof}$ and $\mathrm{Rec}$ in Exercise 1.4.20, and :ref{#ex-tot-jump-complete} is his Exercise 1.4.21. The $\Sigma^0_3$-completeness of $\mathrm{Rec}$ is due to Rogers. The proof given here, which codes $\emptyset'$ into $V_x$ in the $\Pi^0_3$ case, is the one of Soare's Theorem 4.3.5 and Corollary 4.3.6, adapted to the construction of :ref{#thm-cof-complete}. Soare's Remark 4.3.8 explains how other properties can be coded in the same way, and Section 4.3.5 gives representations of $\Sigma^0_3$ sets used to guess at membership in priority constructions. Marker arguments, of which the proof for $\mathrm{Cof}$ is a simple instance, are a basic tool in the study of c.e. sets.

- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 4.3.2–4.3.5.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.6.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.4.

:::::exercises
::::exercise{#ex-cof-not-pi3 difficulty=1 objective="Deduce non-membership in $\Pi^0_3$ from $\Sigma^0_3$-completeness."}
Show that $\mathrm{Cof}$ is not $\Pi^0_3$.

:::solution
If $\mathrm{Cof}$ were $\Pi^0_3$, every $\Sigma^0_3$ set, being many-one reducible to $\mathrm{Cof}$, would be $\Pi^0_3$ by :ref{#prop-sigma1-delta1}, contradicting :ref{#cor-hierarchy-strict}.
:::
::::

::::exercise{#ex-tot-jump-complete difficulty=2 objective="Relativize the classification of $\mathrm{Tot}$ to $\emptyset'$, keeping the reduction computable."}
Show that $\{ e : \Phi^{\emptyset'}_e \text{ is total} \}$ is $\Pi^0_3$-complete.

:::solution
It is $\Pi^0_3$ by :ref{#ex-tot-jump-pi3}. Relativized to $\emptyset'$, the proof of :ref{#thm-tot-complete} shows that for every $\Pi^0_2(\emptyset')$ set $A$ there is a computable $f$ with $x \in A \iff \Phi^{\emptyset'}_{f(x)}$ total: the function $f$ is given by the parameter form of SMN for oracle machines, and is computable, not only $\emptyset'$-computable. By :ref{#thm-post}, the $\Sigma^0_2(\emptyset')$ sets are the sets c.e. in $\emptyset''$, that is, the $\Sigma^0_3$ sets; so the $\Pi^0_2(\emptyset')$ sets are the $\Pi^0_3$ sets, and all of them reduce to the given set.
:::
::::

::::exercise{#ex-marker-run difficulty=1 objective="Run the marker construction by hand and identify the markers that an action can no longer remove."}
In the construction of :ref{#thm-cof-complete}, suppose that no number acts at stages $1$, $2$ and $4$, that $0$ acts at stage $3$, $2$ acts at stage $5$ and $1$ acts at stage $6$.

1. Compute $V_x[6]$ and the markers at stage $6$.
2. Suppose that from stage $7$ on, only numbers $n \geq 3$ act. Which markers are final?

:::solution
1. $V_x[2] = \emptyset$, since nothing acts at stages $1$ and $2$. At stage $3 = s + 1$ with $s = 2$, the numbers below $2$ outside $V_x$ are $0, 1$; the action of $0$ keeps none of them, so $V_x[3] = \{ 0, 1 \}$. Stage $4$ changes nothing. At stage $5$, with $s = 4$, the numbers below $4$ outside $V_x$ are $2, 3$; the action of $2$ keeps the first two, so nothing is enumerated. At stage $6$, with $s = 5$, the numbers below $5$ outside $V_x$ are $2, 3, 4$; the action of $1$ keeps $2$ and enumerates $3$ and $4$. So $V_x[6] = \{ 0, 1, 3, 4 \}$, and the markers at stage $6$ are $2, 5, 6, 7, \dots$
2. An action of $n \geq 3$ at a stage $s + 1 \geq 7$ keeps the first $n$ markers below $s$, hence the first three. As long as $2$, $5$ and $6$ are markers, they are the three smallest markers, since every other number below $6$ is in $V_x$; so each of them that is below $s$ is among the first three markers below $s$, and is kept. Hence $2$, $5$ and $6$ are never enumerated: they are final. Nothing can be said about the later markers without more information on the actions.
:::
::::

::::exercise{#ex-marker-choices difficulty=1 objective="See by examples why an action keeps the first n markers and why the least acting number is chosen."}
Consider two modifications of the construction of :ref{#thm-cof-complete}, and describe the stages at which each set $W_{g(x, n)}$ receives a new element.

1. When $n$ acts, it enumerates all the markers below $s$. Give a behavior of the sets $W_{g(x, n)}$, all finite, for which $V_x$ is cofinite.
2. At each stage, the greatest acting $n \leq s$ acts, instead of the least. Give a behavior for which some $W_{g(x, n)}$ is infinite and $V_x$ is not cofinite.

:::solution
1. Suppose that each $W_{g(x, n)}$ receives exactly one element, at stage $n + 1$. At stage $n + 1$, with $s = n$, the number $n$ is the only acting number, and in the modified construction it enumerates every number below $n$ not yet in $V_x$. So $\{ 0, \dots, n - 1 \} \subseteq V_x$ for every $n$, and $V_x = \nat$ is cofinite, while every $W_{g(x, n)}$ is finite. In the construction of the lesson, the action of $n$ at stage $n + 1$ keeps the first $n$ markers below $n$, that is, all of them, and $V_x = \emptyset$.
2. Suppose that $W_{g(x, 0)}$ receives a new element at every stage, so that it is infinite, and that each $W_{g(x, n)}$ with $n \geq 1$ receives exactly one element, at stage $n + 1$. At stage $1$, only $0 \leq s = 0$ can act, and there is no number below $0$. At a stage $s + 1$ with $s \geq 1$, the numbers $0$ and $s$ both act, and the greatest one, $s$, keeps the first $s$ markers below $s$; there are at most $s$ numbers below $s$, so nothing is enumerated. Hence $V_x = \emptyset$, which is not cofinite. In the construction of the lesson, $0$ acts at every stage and enumerates every number below $s$, so $V_x = \nat$.
:::
::::

::::exercise[The one-marker construction]{#ex-one-marker-variant difficulty=2 objective="Prove the correctness of Soare's variant of the marker construction, in which only the marker of rank n moves."}
Let $g$ be as in the proof of :ref{#thm-cof-complete}. For a finite set $V$, the **marker of rank $k$** of $V$ is the $k$-th element (counting from $0$) of $\nat \setminus V$. Build $V_x$ in stages: $V_x[0] = \emptyset$, and at stage $s + 1$, for each $n \leq s$ with $W_{g(x, n)}[s + 1] \neq W_{g(x, n)}[s]$, enumerate into $V_x$ the marker of rank $n$ of $V_x[s]$. Show that $V_x$ is cofinite if some $W_{g(x, n)}$ is infinite, and coinfinite otherwise.

:::solution
At each stage, the markers of $V_x[s]$ are its non-elements in increasing order, and the rank of a non-element $m$ is the number of non-elements below $m$. Since $V_x$ only grows, the rank of a fixed non-element can only decrease.

*Some $W_{g(x, n)}$ is infinite.* Suppose that $m_0 < \dots < m_n$ are outside $V_x$. At every stage, $m_0, \dots, m_{n-1}$ are non-elements below $m_n$, so the rank of $m_n$ is at least $n$. At each stage $s + 1$ with $s \geq n$ at which $W_{g(x, n)}$ receives a new element, the marker of rank $n$ of $V_x[s]$ is enumerated; it is not $m_n$, which never enters $V_x$, and its rank is at most that of $m_n$, so it is a number smaller than $m_n$. Different stages enumerate different numbers, since a number enumerated at one stage is no longer a marker afterwards. There are infinitely many such stages, hence infinitely many numbers below $m_n$: a contradiction. So the complement of $V_x$ has at most $n$ elements.

*Every $W_{g(x, n)}$ is finite.* Fix $k$, and let $s_k$ be a stage after which no $W_{g(x, n)}$ with $n \leq k$ receives a new element. After stage $s_k$, every number enumerated is a marker of rank greater than $k$ at the previous stage, and enumerating it does not change the markers of rank at most $k$. So the markers of rank $0, \dots, k$ are the same at all stages after $s_k$, and are never enumerated. Their final values $c_0 < \dots < c_k$ lie outside $V_x$. Since $k$ is arbitrary, the complement of $V_x$ is infinite.

This is the construction of Soare (2016, Theorem 4.3.3), sketched in :ref{#rem-one-marker}.
:::
::::

::::exercise{#ex-almost-equal difficulty=1 objective="Classify almost inclusion and almost equality of c.e. sets by reducing $\mathrm{Cof}$ to them."}
Write $X \subseteq^* Y$ if $X \setminus Y$ is finite, and $X =^* Y$ if $X \subseteq^* Y$ and $Y \subseteq^* X$. Show that the sets $\{ \langle a, b \rangle : W_a \subseteq^* W_b \}$ and $\{ \langle a, b \rangle : W_a =^* W_b \}$ are $\Sigma^0_3$-complete.

:::solution
*Upper bounds.* $W_a \subseteq^* W_b$ if and only if
$$
\exists n\ \forall x\ \big( x \leq n \vee x \notin W_a \vee x \in W_b \big).
$$
The disjunction is of a computable, a $\Pi^0_1$ and a $\Sigma^0_1$ relation, all $\Pi^0_2$, so it is $\Pi^0_2$; with $\forall x$ it stays $\Pi^0_2$, and with $\exists n$ it is $\Sigma^0_3$. The relation $W_a =^* W_b$ is the intersection of two such relations, one with $a$ and $b$ exchanged, hence $\Sigma^0_3$. The sets of codes $\langle a, b \rangle$ are $\Sigma^0_3$ by substitution of the projections.

*Lower bounds.* Fix $c$ with $W_c = \nat$. Then $W_c \subseteq^* W_e$ if and only if $\nat \setminus W_e$ is finite, and $W_c =^* W_e$ holds in exactly the same case, since $W_e \subseteq^* \nat$ always holds. So $e \mapsto \langle c, e \rangle$ reduces $\mathrm{Cof}$ to both sets, and $\mathrm{Cof}$ is $\Sigma^0_3$-complete (:ref{#thm-cof-complete}). This is Soare (2016), Exercises 4.1.13 and 4.3.14.
:::
::::
:::::
