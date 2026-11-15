---
title: Immune and hyperimmune sets
summary: Immune sets contain no infinite c.e. subset; hyperimmune sets escape every disjoint strong array, equivalently their principal function is dominated by no computable function; the sets of hyperimmune degree.
duration: 45
prerequisites: [turing-degrees/limit-computability, ce-degrees/simple-sets]
---

A computable set can be decided, and a c.e. set can be listed. An infinite set may fail both properties in a strong way: no algorithm lists infinitely many of its elements. Such sets are called **immune**. This lesson introduces immunity and its strengthening **hyperimmunity**, in which an algorithm cannot even point to infinitely many disjoint finite blocks each containing an element of the set.

The main result of the lesson translates hyperimmunity into a property of growth: an infinite set is hyperimmune exactly when the function listing its elements in increasing order is dominated by no computable function. Growth of functions, unlike immunity, is a property of Turing degrees, and it is the subject of the rest of the course.

## Immune sets

:::definition{#def-immune}
An infinite set $A \subseteq \nat$ is **immune** if it has no infinite c.e. subset.
:::

Every infinite c.e. set $W$ has an infinite computable subset: enumerate $W$, and keep each element that is larger than all the elements kept before. The kept elements appear in increasing order, so the set they form is computable, and it is infinite. Hence an infinite set is immune if and only if it has no infinite computable subset. An immune set is not computable, since it would be an infinite computable subset of itself.

:::example{#ex-immune-simple}
Recall from :ref{#def-simple} that a c.e. set is **simple** if its complement is immune. The complement of Post's simple set (:ref{#thm-post-simple}) is immune. It is co-c.e.: an immune set may be "almost computable", in the sense that its complement can be listed.
:::

Immunity is a property of sets, not of degrees. If $A$ is immune, the set $A \oplus \nat = \{ 2n : n \in A \} \cup \{ 2n + 1 : n \in \nat \}$ has the same degree and contains the infinite computable set of odd numbers. Conversely, immune sets exist in every non-zero degree. The idea of the proof is to replace a set by the set of its prefixes: an infinite computable family of prefixes of $A$ would compute $A$.

:::proposition{#prop-immune-every-degree}
Every non-computable set is Turing equivalent to an immune set.
:::

:::proof{of=prop-immune-every-degree}
Let $A$ be non-computable, and let $B = \{ \sigma \in \bstr : \sigma \prec A \}$, identified with a set of integers through a computable bijection between $\bstr$ and $\nat$. Then $B \equiv_T A$: $A(n)$ is the last bit of the prefix of $A$ of length $n + 1$, and $\sigma \in B$ is decided by comparing $\sigma$ with $A \uh |\sigma|$. If $C \subseteq B$ were infinite and computable, its elements would be prefixes of $A$ of unbounded length, and $A(n)$ would be computed by searching $C$ for a string of length greater than $n$. So $B$ is immune.
:::

## Hyperimmune sets

Let $D_n$ denote the finite set with **canonical index** $n$, that is, the finite set such that $n = \sum_{i \in D_n} 2^i$. From $n$, one computes the elements of $D_n$ and their number; from an index of a c.e. set, one does not even know whether it is empty.

An immune set defeats every attempt to list infinitely many of its elements. A weaker kind of information is a sequence of finite blocks, each guaranteed to contain an element of the set, without saying which one. The set of prefixes of a non-computable set $A$ (:ref{#prop-immune-every-degree}) is immune, but such blocks are easy to give for it: the block of all strings of length $n$ contains exactly one element of the set, the prefix of $A$ of length $n$. Hyperimmune sets are the sets for which no such sequence of blocks exists.

:::definition{#def-hyperimmune-set}
A **disjoint strong array** is a sequence $(F_n)$ of pairwise disjoint finite sets such that $F_n = D_{f(n)}$ for a total computable function $f$. An infinite set $A$ is **hyperimmune** if for every disjoint strong array $(F_n)$, there is $n$ with $F_n \cap A = \emptyset$. A c.e. set is **hypersimple** if its complement is hyperimmune.
:::

The two conditions on the array are needed.

- *Disjointness.* Without it, no infinite set would be hyperimmune: if $m = \min A$, the computable sequence $F_n = \{ 0, \dots, m \}$ meets $A$ at every $n$. Disjointness forces the blocks to move to infinity, so that infinitely many different elements of $A$ are located.
- *Canonical indices.* The array is given by the canonical indices of its members, so that the blocks are known entirely. Arrays given by c.e. indices $F_n = W_{f(n)}$ define the **hyperhyperimmune** sets of Post, a stronger notion that is not studied here.

A hyperimmune set is immune: if $\{ x_0, x_1, \dots \}$ is an infinite computable subset of $A$, listed without repetition, then $F_n = \{ x_n \}$ is a disjoint strong array meeting $A$ at every $n$. The converse fails.

:::example{#ex-immune-not-hyperimmune}
Let $A$ be non-computable and $B$ the set of its prefixes, as in :ref{#prop-immune-every-degree}. Let $F_n$ be the set of (the codes of) the $2^n$ strings of length $n$. Its canonical index is computable from $n$, the sets $F_n$ are pairwise disjoint, and $F_n \cap B = \{ A \uh n \}$. So $B$ is immune but not hyperimmune.
:::

## Principal functions

The **principal function** of an infinite set $A$ is the function $p_A$ such that $p_A(n)$ is the $n$-th element of $A$ in increasing order, starting from $p_A(0) = \min A$. It is strictly increasing, so $p_A(n) \geq n$. Recall that a function $g$ **dominates** $f$ if $f(n) \leq g(n)$ for every $n$.

:::definition{#def-hyperimmune-fn}
A function $f : \nat \to \nat$ is **hyperimmune** if no computable function dominates it. A set has **hyperimmune degree** if it computes a hyperimmune function.
:::

If $f(n) \leq g(n)$ for all $n \geq n_0$, with $g$ computable, then the function equal to $f$ below $n_0$ and to $g$ elsewhere is computable and dominates $f$. So $f$ is hyperimmune if and only if, for every computable $g$, there are infinitely many $n$ with $f(n) > g(n)$. A hyperimmune function need not be large: it only has to escape each computable function at infinitely many places, and may be small elsewhere (see the figure in :ref{to="immunity-growth/domination"}).

The next theorem relates the two notions. If $A$ is not hyperimmune, the blocks of an array meeting $A$ give upper bounds for the elements of $A$. Conversely, a computable bound $g$ on $p_A$ is turned into an array by cutting $\nat$ into consecutive intervals, each so long that the bound forces it to contain an element of $A$.

:::theorem[Kuznecov, Medvedev, Uspenskii]{#thm-hyperimmune-principal}
An infinite set $A$ is hyperimmune if and only if its principal function $p_A$ is hyperimmune.
:::

:::figure[The intervals of the proof of the theorem, for $h(x) = g(x) + x + 1$. They form a disjoint strong array. If the interval $F_n = [x, h(x))$ contains no element of $A$, then $p_A(x)$, which is at least $x$, is at least $h(x)$, hence larger than $g(x)$.]
<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="The numbers 0 to 34 cut into consecutive blocks F_0, F_1, and so on; the elements of A are shaded; the block F_4 contains no element of A"><rect x="20" y="70" width="16" height="16" class="cell"/><text x="28.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">0</text><rect x="36" y="70" width="16" height="16" class="cell head-cell"/><rect x="52" y="70" width="16" height="16" class="cell"/><rect x="68" y="70" width="16" height="16" class="cell head-cell"/><rect x="84" y="70" width="16" height="16" class="cell"/><rect x="100" y="70" width="16" height="16" class="cell"/><text x="108.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">5</text><rect x="116" y="70" width="16" height="16" class="cell head-cell"/><rect x="132" y="70" width="16" height="16" class="cell"/><rect x="148" y="70" width="16" height="16" class="cell head-cell"/><rect x="164" y="70" width="16" height="16" class="cell"/><rect x="180" y="70" width="16" height="16" class="cell"/><text x="188.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">10</text><rect x="196" y="70" width="16" height="16" class="cell head-cell"/><rect x="212" y="70" width="16" height="16" class="cell"/><rect x="228" y="70" width="16" height="16" class="cell"/><rect x="244" y="70" width="16" height="16" class="cell"/><rect x="260" y="70" width="16" height="16" class="cell"/><text x="268.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">15</text><rect x="276" y="70" width="16" height="16" class="cell"/><rect x="292" y="70" width="16" height="16" class="cell"/><rect x="308" y="70" width="16" height="16" class="cell"/><rect x="324" y="70" width="16" height="16" class="cell"/><rect x="340" y="70" width="16" height="16" class="cell"/><text x="348.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">20</text><rect x="356" y="70" width="16" height="16" class="cell head-cell"/><rect x="372" y="70" width="16" height="16" class="cell"/><rect x="388" y="70" width="16" height="16" class="cell"/><rect x="404" y="70" width="16" height="16" class="cell"/><rect x="420" y="70" width="16" height="16" class="cell head-cell"/><text x="428.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">25</text><rect x="436" y="70" width="16" height="16" class="cell"/><rect x="452" y="70" width="16" height="16" class="cell"/><rect x="468" y="70" width="16" height="16" class="cell"/><rect x="484" y="70" width="16" height="16" class="cell"/><rect x="500" y="70" width="16" height="16" class="cell head-cell"/><text x="508.0" y="100" text-anchor="middle" class="mrm muted" font-size="10">30</text><rect x="516" y="70" width="16" height="16" class="cell"/><rect x="532" y="70" width="16" height="16" class="cell"/><rect x="548" y="70" width="16" height="16" class="cell head-cell"/><rect x="564" y="70" width="16" height="16" class="cell"/><text x="586" y="82" class="mrm muted" font-size="14">⋯</text><path d="M22,64 L22,58 L50,58 L50,64" class="ink-stroke" stroke-width="1.1"/><text x="36.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">0</tspan></text><path d="M54,64 L54,58 L98,58 L98,64" class="ink-stroke" stroke-width="1.1"/><text x="76.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">1</tspan></text><path d="M102,64 L102,58 L162,58 L162,64" class="ink-stroke" stroke-width="1.1"/><text x="132.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">2</tspan></text><path d="M166,64 L166,58 L242,58 L242,64" class="ink-stroke" stroke-width="1.1"/><text x="204.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">3</tspan></text><path d="M246,64 L246,58 L338,58 L338,64" class="accent-stroke" stroke-width="1.8"/><text x="292.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">4</tspan></text><path d="M342,64 L342,58 L450,58 L450,64" class="ink-stroke" stroke-width="1.1"/><text x="396.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">5</tspan></text><path d="M454,64 L454,58 L578,58 L578,64" class="ink-stroke" stroke-width="1.1"/><text x="516.0" y="50" text-anchor="middle" class="math" font-size="14">F<tspan class="mrm" font-size="9" dy="4">6</tspan></text><text x="244" y="120" text-anchor="middle" class="math" font-size="13">x</text><text x="340" y="120" text-anchor="middle" class="math" font-size="13">h<tspan class="mrm">(</tspan>x<tspan class="mrm">)</tspan></text><line x1="244" y1="88" x2="244" y2="108" class="accent-stroke" stroke-dasharray="2 2"/><line x1="340" y1="88" x2="340" y2="108" class="accent-stroke" stroke-dasharray="2 2"/><rect x="20" y="132" width="12" height="12" class="cell head-cell"/><text x="38" y="142" class="label">element of A</text><text x="150" y="142" class="label">F₄ = [x, h(x)) contains no element of A</text></svg>
:::

:::proof{of=thm-hyperimmune-principal}
($\Rightarrow$) Let $g$ be computable; we show that $g$ does not dominate $p_A$. Let $h(x) = g(x) + x + 1$, and let $h^{(n)}$ be the $n$-th iterate of $h$, with $h^{(0)}(0) = 0$. The intervals $F_n = [h^{(n)}(0), h^{(n+1)}(0))$ are non-empty, pairwise disjoint, and their canonical indices are computable from $n$: they form a disjoint strong array. Since $A$ is hyperimmune, some $F_n$ is disjoint from $A$. Let $x = h^{(n)}(0)$. The element $p_A(x)$ is at least $x$, and it is not in $F_n = [x, h(x))$, so $p_A(x) \geq h(x) > g(x)$.

($\Leftarrow$) Suppose that $A$ is not hyperimmune, and let $(F_n)$ be a disjoint strong array with $F_n \cap A \neq \emptyset$ for every $n$. Let $g(n) = \max (F_0 \cup \dots \cup F_n)$; it is computable. The sets $F_0, \dots, F_n$ are disjoint and each contains an element of $A$, so $A$ has at least $n + 1$ elements smaller than or equal to $g(n)$, that is, $p_A(n) \leq g(n)$. So $g$ dominates $p_A$.
:::

The passage from a bound $g$ to the partition of $\nat$ into the intervals $[h^{(n)}(0), h^{(n+1)}(0))$ is a recurring device. It reappears in the proof that maximal sets are high (:ref{#thm-maximal-high}).

:::example{#ex-post-not-hypersimple}
Post's simple set $S$ (:ref{#thm-post-simple}) is not hypersimple. Its proof shows that at least $n + 1$ of the numbers $0, \dots, 2n$ are outside $S$, so $p_{\nat \setminus S}(n) \leq 2n$ for every $n$. The computable function $n \mapsto 2n$ dominates the principal function of the complement, which is therefore not hyperimmune. So simplicity does not imply hypersimplicity; hypersimple sets are constructed in :ref{to="immunity-growth/hypersimple-sets"}.
:::

:::quiz[hyperimmune sets and principal functions]
In the proof of ($\Rightarrow$) in :ref{#thm-hyperimmune-principal}, why is the function $h(x) = g(x) + x + 1$ used rather than $g$ itself?

- [x] To make the intervals $[x, h(x))$ non-empty and to ensure $h(x) > g(x)$, so that missing the interval forces $p_A(x) > g(x)$.

  With $g$ itself, the interval $[x, g(x))$ might be empty, and the iterates of $g$ might not even increase.
- [ ] To make $h$ computable.

  $g$ is already computable; the modification is about the shape of the intervals.
- [ ] Because $p_A(x) \geq x + 1$ for every $x$.

  Only $p_A(x) \geq x$ holds in general; for $A = \nat$, $p_A(x) = x$.

---

In the proof of ($\Leftarrow$), where is the disjointness of the sets $F_n$ used?

- [x] To count: $n + 1$ disjoint sets, each meeting $A$, provide $n + 1$ different elements of $A$ below $g(n)$.
- [ ] To make $g$ computable.

  $g$ is computable from the canonical indices, disjoint or not.
- [ ] To ensure that $A$ is infinite.

  $A$ is infinite by hypothesis.
:::

::::exercise{#ex-hyperimmune-intervals difficulty=1 objective="Recast hyperimmunity with arrays of consecutive intervals given by a computable function."}
Show that an infinite set $A$ is hyperimmune if and only if, for every strictly increasing computable function $f$, there is $n$ such that $A \cap [f(n), f(n+1)) = \emptyset$.

:::solution
If $A$ is hyperimmune, the intervals $[f(n), f(n+1))$ form a disjoint strong array, so one of them misses $A$. Conversely, suppose that the condition holds, and let $g$ be computable. Let $h(x) = g(x) + x + 1$ and $f(n) = h^{(n)}(0)$, which is strictly increasing and computable. Some interval $[f(n), f(n+1))$ misses $A$, and as in the proof of :ref{#thm-hyperimmune-principal}, $p_A(f(n)) > g(f(n))$. So no computable function dominates $p_A$, and $A$ is hyperimmune.
:::
::::

## Hyperimmune degrees

The principal function turns hyperimmune sets into hyperimmune functions. The converse direction requires a little care, since a function computable from $X$ must be turned into a set of the same degree as $X$ whose principal function is at least as large.

:::corollary{#cor-hyperimmune-degree}
For a set $X$, the following are equivalent: $X$ has hyperimmune degree; $X$ computes a hyperimmune set; $X$ is Turing equivalent to a hyperimmune set.
:::

:::proof{of=cor-hyperimmune-degree}
A hyperimmune set $A \leq_T X$ gives the hyperimmune function $p_A \leq_T X$, by :ref{#thm-hyperimmune-principal}. Conversely, let $f \leq_T X$ be hyperimmune. Let $g(n) = \langle f(n), X(n) \rangle$, where $\langle \cdot, \cdot \rangle$ is the Cantor pairing, so that $g(n) \geq f(n)$ and $g \equiv_T X$. Let $q(n) = n + \sum_{i \leq n} g(i)$ and $A$ the range of $q$. The function $q$ is strictly increasing, so $A \equiv_T q$, and $q \equiv_T g$, since $g(0) = q(0)$ and $g(n) = q(n) - q(n-1) - 1$ for $n \geq 1$. Hence $A \equiv_T X$. Finally $p_A = q \geq g \geq f$, so $p_A$ is hyperimmune, and $A$ is hyperimmune by :ref{#thm-hyperimmune-principal}.
:::

Being of hyperimmune degree is therefore a property of strength, closed upward under Turing reducibility: if $X$ computes a hyperimmune function, so does every set that computes $X$. By :ref{#thm-computation-function}, every non-computable $\Delta^0_2$ set has hyperimmune degree, since its computation function is dominated by no computable function. The opposite property, being **computably dominated** (:ref{#def-computably-dominated}), is a property of weakness; it is studied in :ref{to="immunity-growth/computably-dominated"}.

::::exercise{#ex-hyperimmune-degree-agreement difficulty=2 objective="Characterize the hyperimmune degrees by functions that agree infinitely often with every computable function."}
Show that a set $X$ has hyperimmune degree if and only if $X$ computes a function $h$ such that every computable function is equal to $h$ at infinitely many points.

:::hint
Reserve the inputs $\langle e, k \rangle$, $k \in \nat$, to the $e$-th partial computable function, and use a hyperimmune function to bound the time of the computations.
:::

:::solution
If $h$ equals every computable function infinitely often, then $h + 1$ exceeds every computable function at infinitely many points, so it is hyperimmune.

Conversely, let $f \leq_T X$ be hyperimmune and $F(n) = \max_{m \leq n} f(m)$. For $n = \langle e, k \rangle$, let $h(n) = \Phi_e(n)$ if $\Phi_e(n)[F(n)]\converge$, and $h(n) = 0$ otherwise. It is $X$-computable. Let $\Phi_e$ be total, and $t(n)$ the least $s$ with $\Phi_e(n)[s]\converge$, a computable function. Suppose that $h(\langle e, k \rangle) = \Phi_e(\langle e, k \rangle)$ for finitely many $k$ only; then $t(\langle e, k \rangle) > F(\langle e, k \rangle)$ for all $k \geq k_0$. For each $m$, let $k(m)$ be the least $k \geq k_0$ with $\langle e, k \rangle \geq m$, which exists since the Cantor pairing is increasing in $k$, and let $G(m) = t(\langle e, k(m) \rangle)$. Then $G$ is computable and $G(m) > F(\langle e, k(m) \rangle) \geq f(m)$ for every $m$, so $G$ dominates $f$, a contradiction.
:::
::::

## Notes and references

Immune and simple sets were introduced by Post (1944), who also defined hypersimple and hyperhypersimple sets. The characterization of hyperimmune sets through principal functions is due to Kuznecov, Medvedev and Uspenskii (Soare 2016, Theorem 5.3.3), and the study of hyperimmune degrees to Miller and Martin (1968). Soare treats arrays, hyperimmune sets and dominating functions in Section 5.3 of his book, and hyperimmune degrees in Section 5.6. Monin and Patey cover the same material in the sections *Immune sets* and *Hyperimmune functions* of their chapter *Immunity and function growth*.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- W. Miller and D. A. Martin, *The degrees of hyperimmune sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 159–166.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 5.3 and 5.6.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.17.
- B. Monin and L. Patey, *Computability theory*, chapter *Immunity and function growth*.

:::::exercises
::::exercise{#ex-hyperimmune-subsets difficulty=1 objective="Check that hyperimmunity passes to infinite subsets, and that a superset of a hyperimmune set need not be immune."}
Show that every infinite subset of a hyperimmune set is hyperimmune, and that a set containing a hyperimmune set need not be immune.

:::solution
If $B \subseteq A$ is infinite and $(F_n)$ is a disjoint strong array meeting $B$ at every $n$, it meets $A$ at every $n$. For the second statement, let $A$ be hyperimmune, for instance a hyperimmune set of the degree of $\emptyset'$ given by :ref{#cor-hyperimmune-degree}, and let $A_0 = \{ 2n : n \in A \}$. Then $p_{A_0}(n) = 2 p_A(n) \geq p_A(n)$, so $p_{A_0}$ is hyperimmune and $A_0$ is hyperimmune by :ref{#thm-hyperimmune-principal}. The set $A_0 \cup \{ 2n + 1 : n \in \nat \}$ contains $A_0$ and the infinite computable set of odd numbers, so it is not immune.
:::
::::

::::exercise{#ex-immune-injective-image difficulty=1 objective="Transport immunity along a computable injection, and see why injectivity is needed."}
Let $A$ be immune and $f$ a total computable injective function. Show that $f[A] = \{ f(x) : x \in A \}$ is immune. Show that the conclusion may fail, even with $f[A]$ infinite, if $f$ is computable but not injective.

:::solution
The set $f[A]$ is infinite, since $A$ is infinite and $f$ is injective. Suppose that $W \subseteq f[A]$ is an infinite c.e. set, and let $V = \{ x : f(x) \in W \}$. It is c.e.: $x \in V$ as soon as $f(x)$ appears in the enumeration of $W$. It is contained in $A$: if $f(x) \in W \subseteq f[A]$, then $f(x) = f(y)$ for some $y \in A$, and $x = y$ by injectivity. It is infinite: every element of $W$ is of the form $f(x)$, with $x \in V$, and distinct elements of $W$ have distinct preimages. So $V$ is an infinite c.e. subset of $A$, a contradiction.

For the second statement, let $X$ be non-computable and $B$ the set of prefixes of $X$, which is immune by :ref{#prop-immune-every-degree}. The function $f(\sigma) = |\sigma|$, read through the coding of strings by integers, is computable and not injective, and $f[B] = \nat$, since $X$ has a prefix of each length. The set $\nat$ is not immune.
:::
::::

::::exercise{#ex-running-maximum difficulty=2 objective="Compare a function with its running maximum and with its compositions, from the point of view of domination."}
For $f : \nat \to \nat$, let $\hat f(n) = \max_{m \leq n} f(m)$.

1. Show that $f$ is hyperimmune if and only if $\hat f$ is hyperimmune.
2. Let $g$ be a strictly increasing computable function. Show that $\hat f \circ g$ is hyperimmune whenever $f$ is. Give a hyperimmune function $f$ such that $f \circ g$ is not hyperimmune, for $g(n) = 2n$.

:::solution
1. A function above a hyperimmune function is hyperimmune, since a computable function dominating the larger one dominates the smaller one. If $f$ is hyperimmune, then $\hat f \geq f$ is hyperimmune. Conversely, suppose that a computable function $h$ dominates $f$. Then $\hat h$ is computable, and $\hat h(n) \geq h(m) \geq f(m)$ for every $m \leq n$, so $\hat h$ dominates $\hat f$. Hence if $\hat f$ is hyperimmune, so is $f$.
2. Since $g$ is strictly increasing, $g(n) \geq n$, and since $\hat f$ is non-decreasing, $\hat f(g(n)) \geq \hat f(n)$ for every $n$. So $\hat f \circ g \geq \hat f$, which is hyperimmune by 1.

   For the example, let $h$ be a hyperimmune function; there is one, for instance computable in $\emptyset'$, by :ref{#cor-hyperimmune-degree} and the remark that follows it. Let $f(2n) = 0$ and $f(2n + 1) = h(n)$. If a computable function $k$ dominated $f$, the computable function $n \mapsto k(2n + 1)$ would dominate $h$; so $f$ is hyperimmune. But $f(g(n)) = f(2n) = 0$ for every $n$, and $f \circ g$ is dominated by the constant function $0$.
:::
::::

::::exercise{#ex-hyperimmune-below-jump difficulty=1 objective="Build a hyperimmune set computable in $\emptyset'$ by diagonalizing against all partial computable functions at once."}
Define $p(n) = 1 + p(n - 1) + \max \{ \Phi_e(n) : e \leq n,\ \Phi_e(n)\converge \}$, where $p(-1) = 0$ and the maximum of the empty set is $0$. Show that $p$ is computable in $\emptyset'$, that its range $A$ is a hyperimmune set computable in $\emptyset'$, and that $p(n) > \Phi_e(n)$ for every $e$ such that $\Phi_e$ is total and every $n \geq e$.

:::solution
To compute $p(n)$ from $p(n - 1)$, the oracle $\emptyset'$ decides for each $e \leq n$ whether $\Phi_e(n)$ converges, and the convergent computations are then run. So $p \leq_T \emptyset'$. Since $p(n) \geq 1 + p(n - 1)$, $p$ is strictly increasing, so $p(x) \geq x$, and $x \in A$ if and only if $x \in \{ p(0), \dots, p(x) \}$; hence $A \leq_T \emptyset'$, and $p$ is the principal function of $A$.

If $\Phi_e$ is total and $n \geq e$, then $\Phi_e(n)$ is one of the values in the maximum, so $p(n) > \Phi_e(n)$. In particular, no computable function $g = \Phi_e$ dominates $p$, since $p(e) > g(e)$. So $p$ is hyperimmune, and $A$ is hyperimmune by :ref{#thm-hyperimmune-principal}. The function $p$ even exceeds each computable function from some point on, which is more than hyperimmunity requires.
:::
::::

::::exercise{#ex-hyperimmune-windows difficulty=1 objective="Characterize hyperimmunity by the gaps of a set: no computable function bounds, from every point, the distance to the next element."}
Show that an infinite set $A$ is hyperimmune if and only if there is no computable function $g$ such that $A \cap [n, g(n)] \neq \emptyset$ for every $n$.

:::solution
Suppose that $A$ is not hyperimmune. By :ref{#thm-hyperimmune-principal}, a computable function $g$ dominates $p_A$. Since $p_A(n) \geq n$, the element $p_A(n)$ of $A$ lies in $[n, g(n)]$, for every $n$.

Conversely, let $g$ be computable with $A \cap [n, g(n)] \neq \emptyset$ for every $n$; in particular $g(n) \geq n$. Let $x_0 = 0$ and $x_{k+1} = g(x_k) + 1$, a computable strictly increasing sequence, and let $F_k = [x_k, x_{k+1})$. These intervals are pairwise disjoint, their canonical indices are computable from $k$, and $F_k \supseteq [x_k, g(x_k)]$ meets $A$ for every $k$. So $A$ is not hyperimmune.
:::
::::
:::::
