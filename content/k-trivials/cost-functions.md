---
title: Cost functions and Solovay's construction
summary: The standard cost function; a set with a computable approximation obeying it is K-trivial; Solovay's construction of a simple K-trivial set.
duration: 35
prerequisites: [k-trivial-sets, kolmogorov-complexity/coding-theorem, ce-degrees/simple-sets]
---

A K-trivial set is described by a prefix-free machine that, for each $n$, outputs $A \uh n$ on an input of length about $K(n)$. If $A$ is given by a computable approximation, such a machine can be built with the KC theorem: whenever a shorter description of $n$ appears, or the approximation of $A \uh n$ changes, request a new description of the current $A \uh n$. The descriptions requested for prefixes that later change are wasted. The **cost function** measures this waste, and a set whose approximation wastes a finite total weight is K-trivial. Solovay used this idea to build a non-computable K-trivial set.

## The standard cost function

Let $K_s(n)$ be the length of the shortest $\tau$ with $U(\tau)[s]\converge = n$, and $K_s(n) = \infty$ if there is none, with the convention $2^{-\infty} = 0$. Then $K_s(n)$ is computable in $(s, n)$, non-increasing in $s$, with limit $K(n)$.

:::definition{#def-cost-ck}
The **standard cost function** is
$$
c_K(x, s) = \sum_{x < n \leq s} 2^{-K_s(n)}.
$$
Let $(A_s)$ be a computable approximation of a $\Delta^0_2$ set $A$ (:ref{#def-delta2-approximation}). For each $s$ with $A_{s+1} \neq A_s$, let $x_s$ be the least $x$ with $A_{s+1}(x) \neq A_s(x)$. The approximation **obeys** $c_K$ if
$$
\sum_{s \,:\, A_{s+1} \neq A_s} c_K(x_s, s+1) < \infty.
$$
:::

The cost $c_K(x_s, s+1)$ is the weight of the current descriptions of the numbers $n$ whose prefixes $A \uh n$ have just changed. It has two monotonicity properties used below: $c_K(x, s)$ is non-decreasing in $s$, since terms are added and $K_s$ decreases, and non-increasing in $x$. Moreover $c_K(x, s) \leq \sum_{n > x} 2^{-K(n)}$, since $K_s \geq K$; this tail tends to $0$ as $x$ tends to infinity, by the Kraft inequality for $K$.

## Obeying the cost function implies K-triviality

:::theorem{#thm-obey-ktrivial}
If a set $A$ has a computable approximation that obeys $c_K$, then $A$ is K-trivial.
:::

:::proof{of=thm-obey-ktrivial}
Let $(A_s)$ be such an approximation, $S$ the total cost, and $d \geq 2$ such that $2^{1-d} + 2^{-d} S \leq 1$. We enumerate a request set $R$. At stage $s \geq 1$, for each $n \leq s$ with $K_s(n) < \infty$ such that
$$
A_s \uh n \neq A_{s-1} \uh n \quad \text{or} \quad K_s(n) < K_{s-1}(n),
$$
enumerate the request $(A_s \uh n, K_s(n) + d)$; for $n = s$, which was not considered before, the second condition is replaced by $K_s(n) < \infty$. $R$ is c.e.

*Weight.* Split the requests into two kinds. A request at stage $s$ for $n$ with $A_s \uh n = A_{s-1} \uh n$ is caused by a new value of $K_s(n)$. The values $K_s(n)$, for fixed $n$, are pairwise distinct at these stages and at least $K(n)$, so these requests weigh at most $\sum_n \sum_{k \geq K(n)} 2^{-k-d} = 2^{1-d} \sum_n 2^{-K(n)} \leq 2^{1-d}$. A request at stage $s$ for $n$ with $A_s \uh n \neq A_{s-1} \uh n$ has $x_{s-1} < n \leq s$; the requests of this kind at stage $s$ weigh at most $2^{-d} c_K(x_{s-1}, s)$, and in total at most $2^{-d} S$. So $R$ is a bounded request set.

*Descriptions.* Fix $n$, and let $s \geq n$ be the last stage with $s = n$, or $A_s \uh n \neq A_{s-1} \uh n$, or $K_s(n) < K_{s-1}(n)$; it exists since $A \uh n$ and $K_s(n)$ change finitely often. At this stage, $A_s \uh n = A \uh n$ and $K_s(n) = K(n) < \infty$, since neither changes after $s$. Moreover $s \geq 1$, since $K_0(n) = \infty$: no computation halts at stage $0$. So the request $(A \uh n, K(n) + d)$ is enumerated at stage $s$. By the KC theorem (:ref{#thm-kc}), $K(A \uh n) \leq K(n) + d + O(1)$.
:::

A request is enumerated for the current prefix whenever the information about $n$ or about $A \uh n$ improves. The first kind of request costs at most what $U$ itself spends on describing numbers. The second kind is the price of changes of $A$, which is what the cost function bounds.

:::quiz[obeying the cost function]
In the proof of :ref{#thm-obey-ktrivial}, why are the requests caused by new values of $K_s(n)$ of bounded weight?

- [x] Because for fixed $n$ their lengths $K_s(n) + d$ are pairwise distinct and at least $K(n) + d$, so they weigh at most $2^{1 - d - K(n)}$, and $\sum_n 2^{-K(n)} \leq 1$.
- [ ] Because $K_s(n)$ changes at most once.

  It may change many times; the geometric sum over the distinct values handles this.
- [ ] Because the approximation of $A$ obeys $c_K$.

  The cost function controls the requests caused by changes of $A$, not those caused by changes of $K_s$.

---

Why is a request enumerated for the current prefix $A_s \uh n$ also when only $K_s(n)$ changes?

- [x] Because the final description must have length $K(n) + d$: if the last change concerns $K_s(n)$, the prefix is already final and only its description must be shortened.
- [ ] Because otherwise the request set would not be c.e.

  It would still be c.e.; the issue is that the final value $K(n)$ would never be used.
- [ ] To make the weight finite.

  These requests add weight; they are needed for the upper bound on $K(A \uh n)$.
:::

## Solovay's theorem

To build a non-computable K-trivial set, it suffices to make a c.e. set non-computable while keeping the total cost of its enumeration finite. Simplicity (:ref{#def-simple}) is a convenient way to obtain non-computability: a simple set $A$ is not computable, since its complement is infinite and meets no infinite c.e. set, so it is not c.e.

:::theorem[Solovay]{#thm-solovay-ktrivial}
There is a simple K-trivial set. In particular, there is a non-computable c.e. K-trivial set.
:::

:::proof{of=thm-solovay-ktrivial}
We enumerate $A$ in stages, $A_0 = \emptyset$. At stage $s + 1$, for each $e \leq s$ such that no element has yet been enumerated for $e$, if there is $x \in W_{e,s}$ with
$$
x > 2e \quad \text{and} \quad c_K(x, s+1) < 2^{-e},
$$
enumerate the least such $x$ into $A$ and declare that $e$ has acted. Let $A_{s+1}$ be the result. The approximation $(A_s)$ is computable, and $A = \bigcup_s A_s$ is c.e.

*The cost is finite.* If $A_{s+1} \neq A_s$, then $x_s$ is the least element enumerated at stage $s+1$, enumerated for some $e$ that acts at this stage, and $c_K(x_s, s+1) < 2^{-e}$. Each $e$ acts at most once, so the total cost is less than $\sum_e 2^{-e} = 2$. By :ref{#thm-obey-ktrivial}, $A$ is K-trivial.

*The complement is infinite.* Each $e$ contributes at most one element, larger than $2e$. So the elements of $A$ smaller than $2k$ are contributed by some $e < k$, and there are at most $k$ of them: at least $k$ of the numbers below $2k$ are outside $A$.

*$A$ meets every infinite c.e. set.* Let $W_e$ be infinite. Choose $x_0$ with $\sum_{n > x_0} 2^{-K(n)} < 2^{-e}$; then $c_K(x, s) < 2^{-e}$ for all $x \geq x_0$ and all $s$. Let $x \in W_e$ with $x > \max(x_0, 2e)$, and $s \geq e$ with $x \in W_{e,s}$. If $e$ has not acted before stage $s+1$, it acts at stage $s+1$, since $x$ qualifies. In both cases some element of $W_e$ has been enumerated into $A$.
:::

The construction is a priority-free version of Post's construction of a simple set (:ref{#thm-post-simple}), with one extra condition: an element may enter $A$ only if it is cheap. The tail estimate guarantees that cheap elements are available in every infinite c.e. set. The construction has no injury: requirements do not interact.

:::quiz[Solovay's construction]
In the proof of :ref{#thm-solovay-ktrivial}, why is the condition $c_K(x, s+1) < 2^{-e}$ eventually satisfied by the elements of an infinite set $W_e$?

- [x] Because $c_K(x, s) \leq \sum_{n > x} 2^{-K(n)}$ for every $s$, and this tail of a convergent series is less than $2^{-e}$ for all large $x$.
- [ ] Because $K_s(n)$ is non-increasing in $s$.

  This makes the cost non-decreasing in $s$; the bound comes from comparing $K_s$ with $K$.
- [ ] Because $W_e$ contains small elements.

  Small elements are expensive; the argument uses large elements.

---

Why does the cost of the whole enumeration stay below $2$?

- [x] Because each $e$ enumerates at most one element, at a cost less than $2^{-e}$, and the cost of a stage is the cost of its least enumerated element.
- [ ] Because $A$ is simple.

  Simplicity is a consequence of the construction, unrelated to the cost bound.
- [ ] Because $\sum_n 2^{-K(n)} \leq 1$.

  This bound is used to find cheap elements; the total cost is bounded by the choice of the thresholds $2^{-e}$.
:::

Nies proved the converse of :ref{#thm-obey-ktrivial}: every K-trivial set has a computable approximation that obeys $c_K$. The proof is part of the "golden run" analysis mentioned in the last lesson, and is admitted here (Nies, *Computability and Randomness*, Chapter 5). Cost functions are now a general tool: many classes of $\Delta^0_2$ sets are characterized by the cost functions their approximations obey.

## Exercises

::::exercise{difficulty=1}
Show that there is a K-trivial set that is neither c.e. nor co-c.e.

:::solution
Let $A$ be a non-computable c.e. K-trivial set. By :ref{#prop-k-trivial-basic} and :ref{#prop-k-trivial-join}, $B = A \oplus \overline{A}$ is K-trivial. If $B$ were c.e., then $\overline{A} = \{ n : 2n + 1 \in B \}$ would be c.e., and $A$ would be computable. If $B$ were co-c.e., then $A = \{ n : 2n \in B \}$ would be co-c.e., hence computable since it is c.e.
:::
::::

::::exercise{difficulty=2}
Let $(A_s)$ be a computable approximation obeying $c_K$, and $f$ a computable strictly increasing function. Show that $(A_{f(s)})_s$ obeys $c_K$.

:::solution
Let $B_s = A_{f(s)}$. If $B_{s+1} \neq B_s$, then $A$ changes at some stages $t$ with $f(s) \leq t < f(s+1)$, and the least position $y_s$ at which $B_s$ and $B_{s+1}$ differ is at least the least $x_t$ over these stages $t$: a position where $A_{f(s)}$ and $A_{f(s+1)}$ differ has changed at some intermediate stage. Let $t$ be such a stage with $x_t \leq y_s$. Since $c_K$ is non-increasing in $x$ and non-decreasing in its second argument, and $s + 1 \leq f(s) + 1 \leq t + 1$,
$$
c_K(y_s, s+1) \leq c_K(x_t, s + 1) \leq c_K(x_t, t+1).
$$
Distinct $s$ give distinct $t$, since the intervals $[f(s), f(s+1))$ are disjoint. So the total cost of $(B_s)$ is at most that of $(A_s)$.
:::
::::

## Notes and references

Solovay's construction appears in his unpublished manuscript (1975). The cost function formulation is due to Nies, who developed the general theory of cost functions; Downey, Hirschfeldt, Nies and Stephan (2003) gave a published account of the construction.

- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished manuscript, IBM Thomas J. Watson Research Center, 1975.
- A. Nies, *Lowness properties and randomness*, Advances in Mathematics 197 (2005), 274–305.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Chapter 5.
