---
title: Martin's domination theorem
summary: A set is high if and only if it computes a function that eventually dominates every computable function; high sets list the computable functions; maximal sets are high; a set is high or DNC if and only if it computes a function that differs almost everywhere from every computable function.
duration: 40
prerequisites: [dnc-functions, turing-degrees/low-and-high, arithmetic-hierarchy/index-sets]
---

Hyperimmune functions escape every computable function infinitely often. A stronger growth property asks a function to be above every computable function from some point on. No function is above every computable function everywhere, since the constant functions are computable; but a function can **eventually dominate** each of them. Martin showed that the sets computing such a function are exactly the high sets, the sets whose jump computes $\emptyset''$. This lesson proves Martin's theorem and two applications: maximal sets are high, and the sets computing a function that differs almost everywhere from every computable function are exactly the sets that are high or compute a DNC function.

We write $\forall^\infty n$ for "for all but finitely many $n$" and $\exists^\infty n$ for "for infinitely many $n$".

:::definition{#def-dominant}
A function $g$ **eventually dominates** $f$ if $\forall^\infty n\ f(n) \leq g(n)$. A function is **dominant** if it eventually dominates every computable function.
:::

A dominant function is hyperimmune: a computable $g$ dominating it everywhere would be eventually dominated by it, and so would $g + 1$, which is impossible. Recall from :ref{#def-high} that $A$ is **high** if $A' \geq_T \emptyset''$, and from :ref{#thm-tot-complete} that $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$ is $\Pi^0_2$-complete, so $\mathrm{Tot} \equiv_T \emptyset''$.

## Martin's theorem

:::theorem[Martin]{#thm-martin-domination}
A set $A$ is high if and only if it computes a dominant function.
:::

:::proof{of=thm-martin-domination}
($\Rightarrow$) Since $A$ is high, $\mathrm{Tot} \leq_T \emptyset'' \leq_T A'$. By the limit lemma relative to $A$, there is an $A$-computable function $a(e, s)$ with $\lim_s a(e, s) = \mathrm{Tot}(e)$ for every $e$. Define $g(x)$ as follows. For each $e \leq x$, search for the least $s \geq x$ such that $\Phi_e(x)[s]\converge$ or $a(e, s) = 0$. The search terminates: if $\Phi_e$ is total, $\Phi_e(x)$ converges at some stage; otherwise $a(e, s) = 0$ for all large $s$. Let $v_e = \Phi_e(x)$ if the search ended with $\Phi_e(x)[s]\converge$, and $v_e = 0$ otherwise. Let $g(x) = \sum_{e \leq x} v_e$. It is $A$-computable.

Let $\Phi_e$ be total. Let $s_0$ be such that $a(e, s) = 1$ for all $s \geq s_0$. For $x \geq \max(e, s_0)$, the search for $e$ starts at $s \geq x \geq s_0$, never meets $a(e, s) = 0$, and ends with the convergence of $\Phi_e(x)$; so $v_e = \Phi_e(x)$ and $g(x) \geq \Phi_e(x)$. Hence $g$ eventually dominates $\Phi_e$.

($\Leftarrow$) Let $g \leq_T A$ be dominant. If $\Phi_e$ is total, the function $t_e(x)$, the least $s$ with $\Phi_e(x)[s]\converge$, is computable, so $\forall^\infty x\ t_e(x) \leq g(x)$. Hence
$$
e \in \mathrm{Tot} \iff \exists k\ \big[\ \forall x \geq k\ \ \Phi_e(x)[g(x)]\converge \ \text{ and } \ \forall x < k\ \ \Phi_e(x)\converge\ \big].
$$
If $e \in \mathrm{Tot}$, take $k$ such that $t_e(x) \leq g(x)$ for $x \geq k$. Conversely, the right-hand side states that $\Phi_e$ converges on every input. Inside the brackets, the first condition is $\Pi^0_1(A)$ and the second is $\Sigma^0_1$, so $\mathrm{Tot}$ is $\Sigma^0_2(A)$. It is also $\Pi^0_2$, hence $\Pi^0_2(A)$. So $\mathrm{Tot}$ is $\Delta^0_2(A)$, that is, computable in $A'$ by Post's theorem relative to $A$. Hence $\emptyset'' \leq_T A'$.
:::

:::corollary{#cor-high-hyperimmune}
Every high set has hyperimmune degree. No computably dominated set is high.
:::

The corollary follows from the remark that dominant functions are hyperimmune. Combined with :ref{#cor-ce-hyperimmune}, it shows that hyperimmunity is much weaker than highness: every non-zero c.e. degree is hyperimmune, while low c.e. sets are not high.

:::quiz[Martin's theorem]
In ($\Rightarrow$), why does the search for $e$ start at $s \geq x$, and not at $s = 0$?

- [x] So that, for large $x$, the search only looks at stages where the approximation $a(e, s)$ has already settled, and cannot stop on an early wrong value $0$.
- [ ] To make the search terminate.

  The search terminates whatever its starting point.
- [ ] To make $g$ increasing.

  $g$ need not be increasing, and this plays no role.

---

In ($\Leftarrow$), why is the clause "$\forall x < k\ \Phi_e(x)\converge$" needed?

- [x] Because the bound $g(x)$ only controls the computations from $k$ on; without the clause, a function diverging on a small input would satisfy the condition.
- [ ] Because $g$ may take the value $0$.

  The values of $g$ play no role below $k$.
- [ ] To make the condition $\Sigma^0_2(A)$.

  The clause is $\Sigma^0_1$; it is needed for correctness, and it keeps the condition $\Sigma^0_2(A)$.
:::

## Lists of computable functions

A high set can list the computable functions. Fix a dominant $g \leq_T A$. For each $e$, let $\psi_e(x) = \Phi_e(x)$ if $\Phi_e(x)[g(x)]\converge$, and $\psi_e(x) = 0$ otherwise. The sequence $(\psi_e)$ is uniformly $A$-computable and consists of total functions. If $\Phi_e$ is total, then $\psi_e$ equals $\Phi_e$ except at finitely many inputs; so the list of all finite modifications of the functions $\psi_e$, which is uniformly $A$-computable, contains every computable function. It may also contain non-computable functions, obtained from partial functions $\Phi_e$. Jockusch proved that high sets can list exactly the computable functions; we admit this.

:::theorem[Jockusch]{#thm-jockusch-lists}
A set $A$ is high if and only if there is a uniformly $A$-computable sequence of sets $(X_n)$ whose members are exactly the computable sets.
:::

The direction from a list to highness is the difficult one; a proof is in Soare's book. The easier analogues are the object of an exercise below.

## Maximal sets

A c.e. set $M$ is **maximal** if its complement is infinite and, for every c.e. set $W \supseteq M$, either $W \setminus M$ is finite or $W$ is cofinite. The existence of maximal sets is due to Friedberg, and is admitted here.

:::theorem[Martin]{#thm-maximal-high}
Every maximal set is high.
:::

:::proof{of=thm-maximal-high}
Let $M$ be maximal, and let $f(n)$ be the least $m$ such that $\nat \setminus M$ has at least $2n$ elements below $m$; $f$ is $M$-computable, since the complement of $M$ is infinite. We show that $f$ is dominant, so that $M$ is high by :ref{#thm-martin-domination}.

Suppose not, and let $g$ be computable with $\exists^\infty n\ g(n) > f(n)$. Replacing $g$ by $n \mapsto n + \sum_{i \leq n} g(i)$, we may assume that $g$ is strictly increasing. Let $I_n = [g(n), g(n+1))$; these intervals partition $[g(0), \infty)$.

*Infinitely many intervals contain two elements of $\nat \setminus M$.* Otherwise, let $n_0$ be such that each $I_n$ with $n \geq n_0$ contains at most one element of $\nat \setminus M$, and let $c$ be the number of elements of $\nat \setminus M$ below $g(n_0)$. For $n \geq n_0$, $\nat \setminus M$ has at most $c + (n - n_0)$ elements below $g(n)$. If $g(n) > f(n)$, it has at least $2n$ elements below $g(n)$, so $2n \leq c + n - n_0$, which holds for finitely many $n$ only. This contradicts $\exists^\infty n\ g(n) > f(n)$.

*A c.e. superset.* Let $W$ be the c.e. set obtained by enumerating $M$ and, at each stage $s$ and for each $n \leq s$, the least element of $I_n$ not in $M_s$, if there is one. If $I_n \not\subseteq M$, the least element of $I_n \setminus M$ is eventually enumerated into $W$, and the elements of $I_n$ enumerated into $W$ are, apart from this one, elements of $M$: an element enumerated at stage $s$ as the least element of $I_n \setminus M_s$ that is not the least element of $I_n \setminus M$ is smaller than it, hence in $M$. So $W \setminus M$ contains exactly one element of each $I_n \not\subseteq M$, and $W \setminus M$ is infinite, since infinitely many intervals meet $\nat \setminus M$. For each of the infinitely many $n$ such that $I_n$ contains two elements of $\nat \setminus M$, the larger ones are not in $W$; so $W$ is coinfinite. This contradicts the maximality of $M$.
:::

## High or DNC

A function $h$ is **almost everywhere different** from $f$ if $\forall^\infty n\ h(n) \neq f(n)$. Both high sets and DNC sets compute functions almost everywhere different from every computable function, for different reasons: a dominant function plus one is eventually above each computable function, and a DNC function can be strengthened to avoid, at $n$, all the values $\Phi_e(n)$ with $e \leq n$. Kjos-Hanssen, Merkle and Stephan showed that there is no other way.

:::theorem[Kjos-Hanssen, Merkle, Stephan]{#thm-high-or-dnc}
A set $X$ computes a function that is almost everywhere different from every computable function if and only if $X$ is high or computes a DNC function.
:::

:::proof{of=thm-high-or-dnc}
($\Leftarrow$) If $X$ is high, let $g \leq_T X$ be dominant; then $g + 1$ is almost everywhere different from every computable function. If $X$ computes a DNC function, let $h \leq_T X$ be as in :ref{#thm-dnc-effectively-immune} (2). Let $c(n)$ be an index, computable from $n$, of the c.e. set $\{ \Phi_e(n) : e \leq n,\ \Phi_e(n)\converge \}$, which has at most $n + 1$ elements. Let $k(n) = h(c(n), n + 1)$. Then $k(n) \neq \Phi_e(n)$ for every $e \leq n$ with $\Phi_e(n)\converge$. If $\Phi_e$ is total, $k(n) \neq \Phi_e(n)$ for every $n \geq e$.

($\Rightarrow$) Let $k \leq_T X$ be almost everywhere different from every computable function, and suppose that $X$ is not high. We first show that $\forall^\infty m\ k(m) \neq \Phi_m(m)$. Suppose instead that $k(m) = \Phi_m(m)$ for infinitely many $m$. Then the function $r(n)$, the least $t$ such that $k(m) = \Phi_m(m)[t]\converge$ for some $m$ with $n < m \leq t$, is total and $X$-computable. Since $X$ is not high, $r$ is not dominant (:ref{#thm-martin-domination}): there is a computable $b$ with $\exists^\infty n\ b(n) > r(n)$, and we may assume $b$ non-decreasing, replacing it by $n \mapsto \max_{i \leq n} b(i)$. Let $\psi(m) = \Phi_m(m)$ if $\Phi_m(m)[b(m)]\converge$, and $\psi(m) = 0$ otherwise; $\psi$ is computable. If $b(n) > r(n)$, there is $m$ with $n < m \leq r(n)$ and $\Phi_m(m)[r(n)]\converge = k(m)$; since $b(m) \geq b(n) > r(n)$, $\Phi_m(m)[b(m)]\converge$, so $\psi(m) = k(m)$. This happens for infinitely many $n$, with $m > n$, so $\psi(m) = k(m)$ for infinitely many $m$, a contradiction.

So there is $m_0$ with $k(m) \neq \Phi_m(m)$ for all $m \geq m_0$. Let $k'(m) = k(m)$ for $m \geq m_0$, and for $m < m_0$, let $k'(m) = \Phi_m(m) + 1$ if $\Phi_m(m)\converge$, and $k'(m) = 0$ otherwise. This modification involves finitely many values, so $k' \leq_T X$, and $k'$ is DNC.
:::

Each alternative of the theorem occurs without the other. There are PA sets that are computably dominated (:ref{#cor-pa-basis}), hence DNC and not high. There are high sets computing no DNC function, for instance high 1-generic sets, constructed in the course on Cohen genericity.

:::quiz[high or DNC]
In ($\Leftarrow$), why does the DNC case use the function $h$ of :ref{#thm-dnc-effectively-immune} rather than a DNC function directly?

- [x] Because at each $n$ the function must avoid up to $n + 1$ values $\Phi_e(n)$, $e \leq n$, and $h$ avoids any c.e. set of known bounded size.
- [ ] Because a DNC function may be partial.

  DNC functions are total by definition.
- [ ] Because a DNC function differs from $\Phi_e$ at the input $e$ only, and nothing is known at other inputs.

  This is the reason to avoid several values at each input, but it does not explain the choice of $h$: the point is that $h$ provides that avoidance uniformly.

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
Show that the following are equivalent for a set $A$: (1) $A$ computes a dominant function; (2) there is a uniformly $A$-computable sequence of total functions containing every computable function.

:::solution
(1 ⇒ 2) This is the construction of the section on lists: the finite modifications of the functions $\psi_e$.

(2 ⇒ 1) Let $(f_i)$ be the sequence and $g(n) = \sum_{i \leq n} f_i(n)$; it is $A$-computable. A computable function is some $f_i$, and $g(n) \geq f_i(n)$ for every $n \geq i$.
:::
::::

::::exercise{difficulty=2}
Show that a set $A$ is high if and only if $A$ computes a function $g$ such that, for every total computable function $\Phi_e$, $\forall^\infty x\ \Phi_e(x)[g(x)]\converge$.

:::solution
If $A$ is high, a dominant $g \leq_T A$ eventually dominates the computable function $t_e$, the convergence time of $\Phi_e$, so $\Phi_e(x)[g(x)]\converge$ for almost every $x$. Conversely, given such a $g$, the function $\hat g(x) = \max_{e \leq x} \Phi_e(x)[g(x)]$, where divergent computations count as $0$, is $A$-computable. For a total computable $f = \Phi_e$, $\Phi_e(x)[g(x)]\converge$ for almost every $x$, so $\hat g(x) \geq f(x)$ for almost every $x \geq e$. So $\hat g$ is dominant and $A$ is high by :ref{#thm-martin-domination}.
:::
::::

## Notes and references

Martin proved the domination theorem and the highness of maximal sets in 1966; the characterization by lists of computable sets is due to Jockusch (1972). Friedberg constructed maximal sets in 1958. The theorem on high or DNC sets is due to Kjos-Hanssen, Merkle and Stephan (2011), who arrived at it through the study of Kolmogorov complexity, treated in the course on algorithmic randomness.

- D. A. Martin, *Classes of recursively enumerable sets and degrees of unsolvability*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 12 (1966), 295–310.
- C. G. Jockusch, *Degrees in which the recursive sets are uniformly recursive*, Canadian Journal of Mathematics 24 (1972), 1092–1099.
- R. M. Friedberg, *Three theorems on recursive enumeration*, Journal of Symbolic Logic 23 (1958), 309–316.
- B. Kjos-Hanssen, W. Merkle and F. Stephan, *Kolmogorov complexity and the recursion theorem*, Transactions of the American Mathematical Society 363 (2011), 5465–5480.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
