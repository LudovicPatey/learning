---
title: Maximal sets and the high or DNC theorem
summary: Two applications of Martin's domination theorem; maximal sets are high, and a set computes a function almost everywhere different from every computable function if and only if it is high or computes a DNC function.
duration: 35
prerequisites: [domination, dnc-functions]
---

Martin's theorem (:ref{#thm-martin-domination}) turns highness into a growth property, which can be checked without computing the jump. This lesson gives two applications. The first concerns the thinnest co-infinite c.e. sets, the maximal sets: their complements are so sparse that the function counting them is dominant. The second characterizes the sets that compute a function escaping every computable function in the weakest sense, by differing from it almost everywhere: they are the sets that are high or compute a DNC function. In both proofs, a function computed by the set is shown to be dominant by turning a computable function that it fails to dominate into a contradiction.

We write $\forall^\infty n$ for "for all but finitely many $n$" and $\exists^\infty n$ for "for infinitely many $n$".

## Maximal sets

A c.e. set $M$ is **maximal** if its complement is infinite and, for every c.e. set $W \supseteq M$, either $W \setminus M$ is finite or $W$ is cofinite. A maximal set is simple: if $W_e$ were an infinite c.e. set disjoint from $M$, splitting it into two infinite c.e. halves $W$ and $W'$ would give the c.e. set $M \cup W$, which contains infinitely many elements outside $M$ and misses the infinite set $W'$. The existence of maximal sets is due to Friedberg; it is admitted here.

The complement of a maximal set cannot be split by any c.e. set into two infinite parts. The proof of the next theorem uses this as follows. If the function $f$ counting the complement were not dominant, a computable function $g$ would exceed it infinitely often. The intervals $[g(n), g(n+1))$ would then contain, infinitely often, two elements of the complement, and a c.e. set taking the least of them in each interval would split the complement.

:::theorem[Martin]{#thm-maximal-high}
Every maximal set is high.
:::

:::proof{of=thm-maximal-high}
Let $M$ be maximal, and let $f(n)$ be the least $m$ such that $\nat \setminus M$ has at least $2n$ elements below $m$; $f$ is $M$-computable, since the complement of $M$ is infinite. We show that $f$ is dominant, so that $M$ is high by :ref{#thm-martin-domination}.

Suppose not, and let $g$ be computable with $\exists^\infty n\ g(n) > f(n)$. Replacing $g$ by $n \mapsto n + \sum_{i \leq n} g(i)$, we may assume that $g$ is strictly increasing. Let $I_n = [g(n), g(n+1))$; these intervals partition $[g(0), \infty)$.

*Infinitely many intervals contain two elements of $\nat \setminus M$.* Otherwise, let $n_0$ be such that each $I_n$ with $n \geq n_0$ contains at most one element of $\nat \setminus M$, and let $c$ be the number of elements of $\nat \setminus M$ below $g(n_0)$. For $n \geq n_0$, $\nat \setminus M$ has at most $c + (n - n_0)$ elements below $g(n)$. If $g(n) > f(n)$, it has at least $2n$ elements below $g(n)$, so $2n \leq c + n - n_0$, which holds for finitely many $n$ only. This contradicts $\exists^\infty n\ g(n) > f(n)$.

*A c.e. superset.* Let $W$ be the c.e. set obtained by enumerating $M$ and, at each stage $s$ and for each $n \leq s$, the least element of $I_n$ not in $M_s$, if there is one. If $I_n \not\subseteq M$, the least element of $I_n \setminus M$ is eventually enumerated into $W$, and the elements of $I_n$ enumerated into $W$ are, apart from this one, elements of $M$: an element enumerated at stage $s$ as the least element of $I_n \setminus M_s$ that is not the least element of $I_n \setminus M$ is smaller than it, hence in $M$. So $W \setminus M$ contains exactly one element of each $I_n \not\subseteq M$, and $W \setminus M$ is infinite, since infinitely many intervals meet $\nat \setminus M$. For each of the infinitely many $n$ such that $I_n$ contains two elements of $\nat \setminus M$, the larger ones are not in $W$; so $W$ is coinfinite. This contradicts the maximality of $M$.
:::

The partition of $\nat$ into intervals defined from a computable function is the device used for hyperimmune sets (:ref{#thm-hyperimmune-principal}). The counting threshold $2n$ is chosen so that intervals containing at most one element of the complement each cannot keep up with $f$.

:::quiz[maximal sets]
Why does $f(n)$ wait for $2n$ elements of the complement, rather than $n$?

- [x] So that if the intervals from $n_0$ on each contained at most one element of the complement, the count $c + n - n_0$ below $g(n)$ would fall short of $2n$ for large $n$.

  With $n$ in place of $2n$, the inequality $n \leq c + n - n_0$ may hold for every $n$, and no contradiction follows.
- [ ] To make $f$ computable in $M$.

  $f$ is $M$-computable for any threshold, since the complement is infinite.
- [ ] To make $W$ co-infinite.

  The co-infiniteness of $W$ comes from the intervals containing two elements of the complement, whose existence is what the threshold provides.
:::

Yates constructed a maximal set in the degree of $\emptyset'$ (Soare 2016, Section 5.7), and Martin (1966) showed that the degrees of the maximal sets are exactly the high c.e. degrees. These results are admitted here.

## High or DNC

A function $h$ is **almost everywhere different** from $f$ if $\forall^\infty n\ h(n) \neq f(n)$. Both high sets and DNC sets compute functions almost everywhere different from every computable function, for different reasons: a dominant function plus one is eventually above each computable function, and a DNC function can be strengthened to avoid, at $n$, all the values $\Phi_e(n)$ with $e \leq n$ (:ref{#thm-dnc-effectively-immune}). Kjos-Hanssen, Merkle and Stephan showed that there is no other way.

The proof of the converse first shows that a function $k$ almost everywhere different from every computable function, computed by a non-high set, is almost everywhere different from the diagonal $m \mapsto \Phi_m(m)$. If $k$ agreed with the diagonal infinitely often, the times at which these agreements are observed would form a function computable from $k$. As the set is not high, some computable function exceeds this function infinitely often, and running the diagonal with this computable time bound produces a computable function that agrees with $k$ infinitely often.

:::theorem[Kjos-Hanssen, Merkle, Stephan]{#thm-high-or-dnc}
A set $X$ computes a function that is almost everywhere different from every computable function if and only if $X$ is high or computes a DNC function.
:::

:::proof{of=thm-high-or-dnc}
($\Leftarrow$) If $X$ is high, let $g \leq_T X$ be dominant; then $g + 1$ is almost everywhere different from every computable function. If $X$ computes a DNC function, let $h \leq_T X$ be as in :ref{#thm-dnc-effectively-immune} (2). Let $c(n)$ be an index, computable from $n$, of the c.e. set $\{ \Phi_e(n) : e \leq n,\ \Phi_e(n)\converge \}$, which has at most $n + 1$ elements. Let $k(n) = h(c(n), n + 1)$. Then $k(n) \neq \Phi_e(n)$ for every $e \leq n$ with $\Phi_e(n)\converge$. If $\Phi_e$ is total, $k(n) \neq \Phi_e(n)$ for every $n \geq e$.

($\Rightarrow$) Let $k \leq_T X$ be almost everywhere different from every computable function, and suppose that $X$ is not high. We first show that $\forall^\infty m\ k(m) \neq \Phi_m(m)$. Suppose instead that $k(m) = \Phi_m(m)$ for infinitely many $m$. Then the function $r(n)$, the least $t$ such that $k(m) = \Phi_m(m)[t]\converge$ for some $m$ with $n < m \leq t$, is total and $X$-computable. Since $X$ is not high, $r$ is not dominant (:ref{#thm-martin-domination}): there is a computable $b$ with $\exists^\infty n\ b(n) > r(n)$, and we may assume $b$ non-decreasing, replacing it by $n \mapsto \max_{i \leq n} b(i)$. Let $\psi(m) = \Phi_m(m)$ if $\Phi_m(m)[b(m)]\converge$, and $\psi(m) = 0$ otherwise; $\psi$ is computable. If $b(n) > r(n)$, there is $m$ with $n < m \leq r(n)$ and $\Phi_m(m)[r(n)]\converge = k(m)$; since $b(m) \geq b(n) > r(n)$, $\Phi_m(m)[b(m)]\converge$, so $\psi(m) = k(m)$. This happens for infinitely many $n$, with $m > n$, so $\psi(m) = k(m)$ for infinitely many $m$, a contradiction.

So there is $m_0$ with $k(m) \neq \Phi_m(m)$ for all $m \geq m_0$. Let $k'(m) = k(m)$ for $m \geq m_0$, and for $m < m_0$, let $k'(m) = \Phi_m(m) + 1$ if $\Phi_m(m)\converge$, and $k'(m) = 0$ otherwise. This modification involves finitely many values, so $k' \leq_T X$, and $k'$ is DNC.
:::

Each alternative of the theorem occurs without the other. There are PA sets that are computably dominated (:ref{#cor-pa-basis}); they compute DNC functions and are not high, by :ref{#cor-high-hyperimmune}. There are high sets that compute no DNC function, for instance the high 1-generic sets, constructed in the specialized course on Cohen genericity (:ref{#cor-high-not-dnc}).

:::quiz[high or DNC]
In ($\Leftarrow$), why does the DNC case use the function $h$ of :ref{#thm-dnc-effectively-immune} rather than a DNC function directly?

- [x] Because at each $n$ the function must avoid up to $n + 1$ values $\Phi_e(n)$, $e \leq n$, and $h$ avoids any c.e. set of known bounded size.
- [ ] Because a DNC function may be partial.

  DNC functions are total by definition.
- [ ] Because $h$ is computable, unlike a DNC function.

  $h$ is only $X$-computable. No computable function has property (2) of :ref{#thm-dnc-effectively-immune}, since by that theorem it would yield a computable DNC function.

---

In ($\Rightarrow$), where is the assumption that $X$ is not high used?

- [x] To obtain a computable $b$ exceeding the $X$-computable function $r$ infinitely often, which turns the agreements of $k$ with the diagonal into agreements with a computable function.
- [ ] To show that $k$ is total.

  $k$ is total by hypothesis.
- [ ] To show that $k'$ is $X$-computable.

  The finite modification is computable from $k$ for every $X$.
:::

## Exercises

::::exercise{difficulty=1}
Show that every maximal set is hypersimple.

:::solution
Let $M$ be maximal, $p$ the principal function of its complement, and $f$ the function of the proof of :ref{#thm-maximal-high}, which is dominant. For $n \geq 1$, $f(n) = p(2n - 1) + 1$. If a computable function $g$ dominated $p$, then $f(n) \leq g(2n - 1) + 1$ for every $n \geq 1$, while $f$ eventually dominates the computable function equal to $g(2n - 1) + 2$ at every $n \geq 1$, a contradiction. So $p$ is hyperimmune, and the complement of $M$ is hyperimmune by :ref{#thm-hyperimmune-principal}.
:::
::::

::::exercise{difficulty=1}
Show that a computably dominated set computes a function almost everywhere different from every computable function if and only if it computes a DNC function.

:::solution
A computably dominated set is not high, by :ref{#cor-high-hyperimmune}. So, by :ref{#thm-high-or-dnc}, it computes a function almost everywhere different from every computable function if and only if it computes a DNC function.
:::
::::

## Notes and references

Friedberg (1958) constructed maximal sets. Martin (1966) proved that maximal sets are high, and that every high c.e. degree contains a maximal set; Monin and Patey give the first result as an exercise, with the proof followed here. The theorem on high or DNC sets is Theorem 5.1 of Kjos-Hanssen, Merkle and Stephan (2011), with further equivalent conditions in terms of Kolmogorov complexity; they arrived at it through the study of the complexity of initial segments, treated in the course on algorithmic randomness. Monin and Patey prove it in the section *High or DNC degrees* of their chapter *Immunity and function growth*.

- R. M. Friedberg, *Three theorems on recursive enumeration*, Journal of Symbolic Logic 23 (1958), 309–316.
- D. A. Martin, *Classes of recursively enumerable sets and degrees of unsolvability*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 12 (1966), 295–310.
- B. Kjos-Hanssen, W. Merkle and F. Stephan, *Kolmogorov complexity and the recursion theorem*, Transactions of the American Mathematical Society 363 (2011), 5465–5480.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 5.7.
- B. Monin and L. Patey, *Computability theory*, chapter *Immunity and function growth*.
