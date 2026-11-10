---
title: Immune and hyperimmune sets
summary: Immune sets contain no infinite c.e. subset; hyperimmune sets escape every computable array of disjoint finite sets, equivalently their principal function is not computably dominated; Dekker's deficiency sets give hypersimple sets in every non-zero c.e. degree.
duration: 40
prerequisites: [turing-degrees/limit-computability, ce-degrees/simple-sets]
---

A computable set can be decided, and a c.e. set can be listed. An infinite set may fail both properties in a strong way: no algorithm lists infinitely many of its elements. Such sets are called **immune**. This lesson introduces immunity and its strengthening **hyperimmunity**, in which an algorithm cannot even point to infinitely many disjoint finite blocks each containing an element of the set. Hyperimmunity turns out to be a property of growth: an infinite set is hyperimmune exactly when the function listing its elements in increasing order escapes domination by every computable function. This makes it a notion about degrees, studied in the rest of the course.

## Immune sets

:::definition{#def-immune}
An infinite set $A \subseteq \nat$ is **immune** if it has no infinite c.e. subset.
:::

Every infinite c.e. set $W$ has an infinite computable subset: enumerate $W$, and keep each element that is larger than all the elements kept before. The kept elements appear in increasing order, so the set they form is computable, and it is infinite. Hence an infinite set is immune if and only if it has no infinite computable subset. An immune set is not computable, since it would be an infinite computable subset of itself.

Recall from :ref{#def-simple} that a c.e. set is **simple** if its complement is immune. Immunity is a property of sets, not of degrees. If $A$ is immune, the set $A \oplus \nat = \{ 2n : n \in A \} \cup \{ 2n + 1 : n \in \nat \}$ has the same degree and contains the infinite computable set of odd numbers. Conversely, immune sets exist in every non-zero degree.

:::proposition{#prop-immune-every-degree}
Every non-computable set is Turing equivalent to an immune set.
:::

:::proof{of=prop-immune-every-degree}
Let $A$ be non-computable, and let $B = \{ \sigma \in \bstr : \sigma \prec A \}$, identified with a set of integers through a computable bijection between $\bstr$ and $\nat$. Then $B \equiv_T A$: $A(n)$ is the last bit of the prefix of $A$ of length $n + 1$, and $\sigma \in B$ is decided by comparing $\sigma$ with $A \uh |\sigma|$. If $C \subseteq B$ were infinite and computable, its elements would be prefixes of $A$ of unbounded length, and $A(n)$ would be computed by searching $C$ for a string of length greater than $n$. So $B$ is immune.
:::

## Hyperimmune sets

Let $D_n$ denote the finite set with **canonical index** $n$, that is, the finite set such that $n = \sum_{i \in D_n} 2^i$. From $n$, one computes the elements of $D_n$ and their number; from an index of a c.e. set, one does not even know whether it is empty.

:::definition{#def-hyperimmune-set}
A **disjoint strong array** is a sequence $(F_n)$ of pairwise disjoint finite sets such that $F_n = D_{f(n)}$ for a total computable function $f$. An infinite set $A$ is **hyperimmune** if for every disjoint strong array $(F_n)$, there is $n$ with $F_n \cap A = \emptyset$. A c.e. set is **hypersimple** if its complement is hyperimmune.
:::

A hyperimmune set is immune: if $\{ x_0, x_1, \dots \}$ is an infinite computable subset of $A$, listed without repetition, then $F_n = \{ x_n \}$ is a disjoint strong array meeting $A$ at every $n$. Hyperimmunity asks more: an algorithm cannot list infinitely many disjoint finite blocks, each guaranteed to contain an element of $A$.

The **principal function** of an infinite set $A$ is the function $p_A$ such that $p_A(n)$ is the $n$-th element of $A$ in increasing order, starting from $p_A(0) = \min A$. It is strictly increasing, so $p_A(n) \geq n$. Recall that a function $g$ **dominates** $f$ if $f(n) \leq g(n)$ for every $n$.

:::definition{#def-hyperimmune-fn}
A function $f : \nat \to \nat$ is **hyperimmune** if no computable function dominates it. A set has **hyperimmune degree** if it computes a hyperimmune function.
:::

If $f(n) \leq g(n)$ for all $n \geq n_0$, with $g$ computable, then the function equal to $f$ below $n_0$ and to $g$ elsewhere is computable and dominates $f$. So $f$ is hyperimmune if and only if, for every computable $g$, there are infinitely many $n$ with $f(n) > g(n)$.

:::theorem{#thm-hyperimmune-principal}
An infinite set $A$ is hyperimmune if and only if its principal function $p_A$ is hyperimmune.
:::

:::proof{of=thm-hyperimmune-principal}
($\Rightarrow$) Let $g$ be computable; we show that $g$ does not dominate $p_A$. Let $h(x) = g(x) + x + 1$, and let $h^{(n)}$ be the $n$-th iterate of $h$, with $h^{(0)}(0) = 0$. The intervals $F_n = [h^{(n)}(0), h^{(n+1)}(0))$ are non-empty, pairwise disjoint, and their canonical indices are computable from $n$: they form a disjoint strong array. Since $A$ is hyperimmune, some $F_n$ is disjoint from $A$. Let $x = h^{(n)}(0)$. The element $p_A(x)$ is at least $x$, and it is not in $F_n = [x, h(x))$, so $p_A(x) \geq h(x) > g(x)$.

($\Leftarrow$) Suppose that $A$ is not hyperimmune, and let $(F_n)$ be a disjoint strong array with $F_n \cap A \neq \emptyset$ for every $n$. Let $g(n) = \max (F_0 \cup \dots \cup F_n)$; it is computable. The sets $F_0, \dots, F_n$ are disjoint and each contains an element of $A$, so $A$ has at least $n + 1$ elements smaller than or equal to $g(n)$, that is, $p_A(n) \leq g(n)$. So $g$ dominates $p_A$.
:::

:::corollary{#cor-hyperimmune-degree}
For a set $X$, the following are equivalent: $X$ has hyperimmune degree; $X$ computes a hyperimmune set; $X$ is Turing equivalent to a hyperimmune set.
:::

:::proof{of=cor-hyperimmune-degree}
A hyperimmune set $A \leq_T X$ gives the hyperimmune function $p_A \leq_T X$, by :ref{#thm-hyperimmune-principal}. Conversely, let $f \leq_T X$ be hyperimmune. Let $g(n) = \langle f(n), X(n) \rangle$, where $\langle \cdot, \cdot \rangle$ is the Cantor pairing, so that $g(n) \geq f(n)$ and $g \equiv_T X$. Let $q(n) = n + \sum_{i \leq n} g(i)$ and $A$ the range of $q$. The function $q$ is strictly increasing, so $A \equiv_T q$, and $q \equiv_T g$, since $g(0) = q(0)$ and $g(n) = q(n) - q(n-1) - 1$ for $n \geq 1$. Hence $A \equiv_T X$. Finally $p_A = q \geq g \geq f$, so $p_A$ is hyperimmune, and $A$ is hyperimmune by :ref{#thm-hyperimmune-principal}.
:::

Being of hyperimmune degree is therefore a property of strength, closed upward under Turing reducibility. By :ref{#thm-computation-function}, every non-computable $\Delta^0_2$ set has hyperimmune degree. The opposite property, being **computably dominated** (:ref{#def-computably-dominated}), is the subject of the next lesson.

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

## Hypersimple sets

Post constructed hypersimple sets to show that a c.e. set can be very thin. Dekker observed that a hypersimple set can be found in every non-zero c.e. degree.

Let $A$ be an infinite c.e. set, and let $a$ be a computable injective function with range $A$; $a(s)$ is the element enumerated at stage $s$. A stage $s$ is **deficient** if some element smaller than $a(s)$ is enumerated later:
$$
B = \{ s : \exists t > s\ \ a(t) < a(s) \}.
$$
The set $B$ is the **deficiency set** of the enumeration. A stage $s \notin B$ is **non-deficient**: every element enumerated after stage $s$ is larger than $a(s)$.

:::theorem[Dekker]{#thm-deficiency-set}
Let $A$ be an infinite c.e. set, enumerated without repetition by a computable function $a$, and let $B$ be its deficiency set. Then $B$ is c.e., $B \equiv_T A$, and if $A$ is not computable, $B$ is hypersimple.
:::

:::proof{of=thm-deficiency-set}
The set $B$ is c.e.: $s \in B$ as soon as a later stage $t$ with $a(t) < a(s)$ is found.

*Non-deficient stages.* If $s_0 < s_1 < \cdots$ are the non-deficient stages, then $a(s_0) < a(s_1) < \cdots$, since $s_{i+1}$ comes after $s_i$ and $s_i$ is non-deficient. As $a$ is injective with values in $\nat$, $a(s_n) \geq n$. The complement of $B$ is infinite: for every $s$, the minimum of $\{ a(t) : t \geq s \}$ is attained at a unique stage $t_0 \geq s$, which is non-deficient.

*Key property.* If $s$ is non-deficient and $x \leq a(s)$, then $x \in A$ if and only if $x = a(t)$ for some $t \leq s$. Indeed, an element enumerated after $s$ is larger than $a(s)$.

*$B \leq_T A$.* To decide $s \in B$ with oracle $A$, determine the finitely many elements of $A$ smaller than $a(s)$ and the stages at which they are enumerated; $s \in B$ if and only if one of these stages is larger than $s$.

*$A \leq_T B$.* To decide $x \in A$ with oracle $B$, list the non-deficient stages $s_0 < s_1 < \cdots$ up to $s_x$. Since $a(s_x) \geq x$, the key property gives $x \in A$ if and only if $x \in \{ a(t) : t \leq s_x \}$.

*Hyperimmunity.* Suppose that the principal function of $\nat \setminus B$ is dominated by a computable function $g$, so that $s_n \leq g(n)$ for every $n$. Then $x \in A$ if and only if $x = a(t)$ for some $t \leq g(x)$: if $x = a(t)$ with $t > g(x) \geq s_x$, then $x$ is enumerated after the non-deficient stage $s_x$, so $x > a(s_x) \geq x$, which is absurd. This decides $A$ computably, contradicting the hypothesis. So the principal function of $\nat \setminus B$ is hyperimmune, and $\nat \setminus B$ is hyperimmune by :ref{#thm-hyperimmune-principal}.
:::

:::corollary{#cor-ce-hyperimmune}
Every non-computable c.e. set is Turing equivalent to a hypersimple set. In particular, every non-zero c.e. degree is hyperimmune.
:::

A non-computable c.e. set is infinite, so the theorem applies. The second statement also follows from :ref{#thm-computation-function}, since c.e. sets are $\Delta^0_2$. Hypersimple sets are simple, since hyperimmune sets are immune. They are not complete for truth-table reducibility, a result of Post admitted here; but they can be Turing complete, as the corollary shows for the deficiency set of $\emptyset'$.

:::quiz[deficiency sets]
Why are the values $a(s_0) < a(s_1) < \cdots$ of the non-deficient stages strictly increasing?

- [x] Because $s_{i+1} > s_i$, and every element enumerated after a non-deficient stage $s_i$ is larger than $a(s_i)$.
- [ ] Because $a$ is increasing.

  An enumeration of a non-computable c.e. set is never increasing, otherwise the set would be computable.
- [ ] Because $B$ is c.e.

  The enumerability of $B$ plays no role in this property.

---

Where is the non-computability of $A$ used in :ref{#thm-deficiency-set}?

- [x] Only in the hyperimmunity of the complement: a computable bound on the non-deficient stages would decide $A$.
- [ ] To show that the complement of $B$ is infinite.

  This holds for every infinite c.e. set: the stage of the minimum of a tail of the enumeration is non-deficient.
- [ ] To show that $A \leq_T B$.

  The reduction works for every infinite c.e. set.
:::

## Exercises

::::exercise{difficulty=1}
Show that an infinite set $A$ is hyperimmune if and only if, for every strictly increasing computable function $f$, there is $n$ such that $A \cap [f(n), f(n+1)) = \emptyset$.

:::solution
If $A$ is hyperimmune, the intervals $[f(n), f(n+1))$ form a disjoint strong array, so one of them misses $A$. Conversely, suppose that the condition holds, and let $g$ be computable. Let $h(x) = g(x) + x + 1$ and $f(n) = h^{(n)}(0)$, which is strictly increasing and computable. Some interval $[f(n), f(n+1))$ misses $A$, and as in the proof of :ref{#thm-hyperimmune-principal}, $p_A(f(n)) > g(f(n))$. So no computable function dominates $p_A$, and $A$ is hyperimmune.
:::
::::

::::exercise{difficulty=2}
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

Immune and simple sets were introduced by Post (1944), who also defined hypersimple sets. Dekker (1954) introduced deficiency sets. The characterization of hyperimmune sets through principal functions is due to Kuznecov, Medvedev and Uspenskii, and the study of hyperimmune degrees to Miller and Martin (1968). Soare's book contains a detailed treatment of these thinness properties.

- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- J. C. E. Dekker, *A theorem on hypersimple sets*, Proceedings of the American Mathematical Society 5 (1954), 791–796.
- W. Miller and D. A. Martin, *The degrees of hyperimmune sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 159–166.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
