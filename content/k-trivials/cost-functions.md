---
title: Cost functions and a c.e. K-trivial set
summary: The standard cost function; a set with a computable approximation obeying it is K-trivial; a simple K-trivial set, built by Post's construction restricted to cheap enumerations.
duration: 50
prerequisites: [k-trivial-sets, kolmogorov-complexity/coding-theorem, ce-degrees/simple-sets]
---

A K-trivial set is described by a prefix-free machine that, for each $n$, outputs $A \uh n$ on an input of length about $K(n)$. If $A$ is given by a computable approximation, such a machine can be built with the KC theorem: whenever a shorter description of $n$ appears, or the approximation of $A \uh n$ changes, request a new description of the current $A \uh n$, of length about the current value of $K(n)$. The requests of the first kind cost no more than the descriptions of numbers given by $U$ itself. The requests of the second kind are a waste: each change of the approximation makes the descriptions of the prefixes it affects useless, and they must be paid for again. The **cost function** measures this waste, and a set whose approximation wastes a finite total weight is K-trivial.

The method gives a construction of a non-computable c.e. K-trivial set: run Post's construction of a simple set, but enumerate an element only when it is cheap. The construction has no injury, and the K-triviality of the set it builds will later show that the set is Turing incomplete: this is a solution to Post's problem without priority.

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

The cost $c_K(x_s, s+1)$ is the weight of the current descriptions of the numbers $n$ whose prefixes $A \uh n$ have just changed: these are the lengths $n > x_s$, since a prefix of length $n$ contains the positions below $n$. Only the lengths $n \leq s + 1$ are counted; longer prefixes have not been described yet.

:::figure[The cost of a change. The approximations at stages $s$ and $s + 1$ first differ at position $x = 4$, so the prefixes of all lengths $n > 4$ change. Each length $n$ carries the weight $2^{-K_{s+1}(n)}$ of its current shortest description (illustrative values); the cost $c_K(4, s+1)$ is the sum of the highlighted weights. Changes at large positions are cheap, since only lengths beyond the position count.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Two consecutive approximations of A that first differ at position 4; below, bars of height proportional to 2 to the minus K_s of n for the lengths n from 1 to 12, the bars for n greater than 4 being highlighted: their sum is the cost"><text x="20.0" y="37.0" text-anchor="start" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">s</tspan></text><rect x="110" y="20" width="38" height="24" class="cell"/><text x="129.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="148" y="20" width="38" height="24" class="cell"/><text x="167.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="186" y="20" width="38" height="24" class="cell"/><text x="205.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="224" y="20" width="38" height="24" class="cell"/><text x="243.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="262" y="20" width="38" height="24" class="cell"/><text x="281.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="300" y="20" width="38" height="24" class="cell"/><text x="319.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="338" y="20" width="38" height="24" class="cell"/><text x="357.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="376" y="20" width="38" height="24" class="cell"/><text x="395.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="414" y="20" width="38" height="24" class="cell"/><text x="433.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="452" y="20" width="38" height="24" class="cell"/><text x="471.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="490" y="20" width="38" height="24" class="cell"/><text x="509.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="528" y="20" width="38" height="24" class="cell"/><text x="547.0" y="37.0" text-anchor="middle" class="mrm" font-size="13">0</text><text x="20.0" y="69.0" text-anchor="start" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">s+1</tspan></text><rect x="110" y="52" width="38" height="24" class="cell"/><text x="129.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="148" y="52" width="38" height="24" class="cell"/><text x="167.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="186" y="52" width="38" height="24" class="cell"/><text x="205.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="224" y="52" width="38" height="24" class="cell"/><text x="243.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="262" y="52" width="38" height="24" class="head-cell"/><text x="281.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="300" y="52" width="38" height="24" class="cell"/><text x="319.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="338" y="52" width="38" height="24" class="head-cell"/><text x="357.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="376" y="52" width="38" height="24" class="cell"/><text x="395.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="414" y="52" width="38" height="24" class="cell"/><text x="433.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="452" y="52" width="38" height="24" class="cell"/><text x="471.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">0</text><rect x="490" y="52" width="38" height="24" class="cell"/><text x="509.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">1</text><rect x="528" y="52" width="38" height="24" class="head-cell"/><text x="547.0" y="69.0" text-anchor="middle" class="mrm" font-size="13">1</text><text x="129.0" y="96" text-anchor="middle" class="label">0</text><text x="167.0" y="96" text-anchor="middle" class="label">1</text><text x="205.0" y="96" text-anchor="middle" class="label">2</text><text x="243.0" y="96" text-anchor="middle" class="label">3</text><text x="281.0" y="96" text-anchor="middle" class="label">4</text><text x="319.0" y="96" text-anchor="middle" class="label">5</text><text x="357.0" y="96" text-anchor="middle" class="label">6</text><text x="395.0" y="96" text-anchor="middle" class="label">7</text><text x="433.0" y="96" text-anchor="middle" class="label">8</text><text x="471.0" y="96" text-anchor="middle" class="label">9</text><text x="509.0" y="96" text-anchor="middle" class="label">10</text><text x="547.0" y="96" text-anchor="middle" class="label">11</text><text x="20" y="96" class="label">position</text><rect x="141.0" y="110.0" width="14" height="140.0" class="soft-fill"/><text x="148.0" y="266" text-anchor="middle" class="label">1</text><rect x="179.0" y="180.0" width="14" height="70.0" class="soft-fill"/><text x="186.0" y="266" text-anchor="middle" class="label">2</text><rect x="217.0" y="215.0" width="14" height="35.0" class="soft-fill"/><text x="224.0" y="266" text-anchor="middle" class="label">3</text><rect x="255.0" y="180.0" width="14" height="70.0" class="soft-fill"/><text x="262.0" y="266" text-anchor="middle" class="label">4</text><rect x="293.0" y="232.5" width="14" height="17.5" class="accent-fill"/><text x="300.0" y="266" text-anchor="middle" class="label">5</text><rect x="331.0" y="215.0" width="14" height="35.0" class="accent-fill"/><text x="338.0" y="266" text-anchor="middle" class="label">6</text><rect x="369.0" y="241.2" width="14" height="8.8" class="accent-fill"/><text x="376.0" y="266" text-anchor="middle" class="label">7</text><rect x="407.0" y="232.5" width="14" height="17.5" class="accent-fill"/><text x="414.0" y="266" text-anchor="middle" class="label">8</text><rect x="445.0" y="241.2" width="14" height="8.8" class="accent-fill"/><text x="452.0" y="266" text-anchor="middle" class="label">9</text><rect x="483.0" y="245.6" width="14" height="4.4" class="accent-fill"/><text x="490.0" y="266" text-anchor="middle" class="label">10</text><rect x="521.0" y="241.2" width="14" height="8.8" class="accent-fill"/><text x="528.0" y="266" text-anchor="middle" class="label">11</text><rect x="559.0" y="245.6" width="14" height="4.4" class="accent-fill"/><text x="566.0" y="266" text-anchor="middle" class="label">12</text><line x1="110" y1="250" x2="576" y2="250" class="axis"/><text x="20" y="266" class="label">length n</text><text x="20" y="160" class="label">weight</text><text x="20" y="180" class="math" font-size="13">2<tspan class="mrm" font-size="9" dy="-6">−K</tspan><tspan class="mrm" font-size="7" dy="3">s+1</tspan><tspan class="mrm" font-size="9" dy="-3">(n)</tspan></text><line x1="262.0" y1="84" x2="262.0" y2="250" class="muted-stroke" stroke-width="1" stroke-dasharray="4 3"/><text x="268.0" y="120" class="label">prefixes of length n &gt; 4 change</text><text x="110" y="290" class="label">highlighted: the lengths n with x &lt; n ≤ s + 1; the sum of their weights is the cost</text></svg>
:::

The cost function has two monotonicity properties used below: $c_K(x, s)$ is non-decreasing in $s$, since terms are added and $K_s$ decreases, and non-increasing in $x$. Moreover $c_K(x, s) \leq \sum_{n > x} 2^{-K(n)}$, since $K_s \geq K$; this tail tends to $0$ as $x$ tends to infinity, by the Kraft inequality for $K$. This **limit condition** says that changes at large positions are cheap, whatever the stage.

:::example{#ex-cost-ck}
1. A computable set $A$ has the constant approximation $A_s = A$, which never changes and has total cost $0$.
2. Every approximation of a finite set that changes finitely often has finite cost, since each term is at most $\sum_n 2^{-K(n)} \leq 1$. Obeying $c_K$ is a restriction on approximations that change infinitely often, such as the enumerations of infinite c.e. sets.
3. Chaitin's $\Omega$ is $\Delta^0_2$, but no computable approximation of $\Omega$ obeys $c_K$: by the next theorem, $\Omega$ would be K-trivial, which it is not (:ref{#ex-k-trivial}). The natural approximation $\Omega_s$ changes small positions at late stages, when many lengths carry weight.
:::

## Obeying the cost function implies K-triviality

:::theorem{#thm-obey-ktrivial}
If a set $A$ has a computable approximation that obeys $c_K$, then $A$ is K-trivial.
:::

The proof builds a request set and bounds its weight by charging each request to one of two accounts: the descriptions of numbers given by $U$, and the total cost of the approximation. This accounting is the standard way of applying the KC theorem.

:::proof{of=thm-obey-ktrivial}
Let $(A_s)$ be such an approximation, $S$ the total cost, and $d \geq 2$ such that $2^{1-d} + 2^{-d} S \leq 1$. We enumerate a request set $R$. At stage $s \geq 1$, for each $n \leq s$ with $K_s(n) < \infty$ such that
$$
A_s \uh n \neq A_{s-1} \uh n \quad \text{or} \quad K_s(n) < K_{s-1}(n),
$$
enumerate the request $(A_s \uh n, K_s(n) + d)$; for $n = s$, which was not considered before, the second condition is replaced by $K_s(n) < \infty$. $R$ is c.e.

*Weight.* Split the requests into two kinds. A request at stage $s$ for $n$ with $A_s \uh n = A_{s-1} \uh n$ is caused by a new value of $K_s(n)$. The values $K_s(n)$, for fixed $n$, are pairwise distinct at these stages and at least $K(n)$, so these requests weigh at most $\sum_n \sum_{k \geq K(n)} 2^{-k-d} = 2^{1-d} \sum_n 2^{-K(n)} \leq 2^{1-d}$. A request at stage $s$ for $n$ with $A_s \uh n \neq A_{s-1} \uh n$ has $x_{s-1} < n \leq s$; the requests of this kind at stage $s$ weigh at most $2^{-d} c_K(x_{s-1}, s)$, and in total at most $2^{-d} S$. So $R$ is a bounded request set.

*Descriptions.* Fix $n$, and let $s \geq n$ be the last stage with $s = n$, or $A_s \uh n \neq A_{s-1} \uh n$, or $K_s(n) < K_{s-1}(n)$; it exists since $A \uh n$ and $K_s(n)$ change finitely often. At this stage, $A_s \uh n = A \uh n$ and $K_s(n) = K(n) < \infty$, since neither changes after $s$. Moreover $s \geq 1$, since $K_0(n) = \infty$: no computation halts at stage $0$. So the request $(A \uh n, K(n) + d)$ is enumerated at stage $s$. By the KC theorem (:ref{#thm-kc}), $K(A \uh n) \leq K(n) + d + O(1)$.
:::

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

Nies proved the converse: every K-trivial set has a computable approximation that obeys $c_K$. The proof is part of the "golden run" analysis described in the last lesson, and is admitted here (Nies, Theorem 5.5.2; Downey and Hirschfeldt, Theorem 11.5.3). So the standard cost function characterizes the K-trivial sets. Cost functions are now a general tool: many classes of $\Delta^0_2$ sets are characterized by the cost functions their approximations obey.

## A simple K-trivial set

To build a non-computable K-trivial set, it suffices to make a c.e. set simple (:ref{#def-simple}), hence non-computable, while keeping the total cost of its enumeration finite. Post's construction (:ref{#thm-post-simple}) makes $A$ meet each infinite $W_e$ by enumerating an element of $W_e$ larger than $2e$. Here the element must also be cheap: the requirement for $W_e$ may spend at most $2^{-e}$, so that the total cost is finite. The limit condition guarantees that an infinite $W_e$ contains cheap elements.

:::theorem[Solovay; Zambella]{#thm-solovay-ktrivial}
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

The construction has no injury: requirements do not interact, and the index $e$ only fixes the budget $2^{-e}$. Kučera summarized such constructions as "do what is cheap".

:::quiz[the construction of a simple K-trivial set]
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

::::exercise{difficulty=2}
Let $B$ be a non-computable c.e. set. Modify the construction of :ref{#thm-solovay-ktrivial} to build a K-trivial c.e. set $A$ that is not computable and satisfies $A \leq_T B$.

:::hint
Enumerate $x$ for the requirement $e$ only at a stage at which $B$ changes below $x$, and use the non-computability of $B$ to show that an infinite $W_e$ is met. This is permitting.
:::

:::solution
Fix a computable enumeration $(B_s)$ of $B$. At stage $s + 1$, for each $e \leq s$ that has not acted, if there is $x \in W_{e,s}$ with $x > 2e$, $c_K(x, s+1) < 2^{-e}$, and $B_{s+1} \uh x \neq B_s \uh x$, enumerate the least such $x$ into $A$ and declare that $e$ has acted. The cost and co-infiniteness arguments are those of :ref{#thm-solovay-ktrivial}, so $A$ is K-trivial and co-infinite.

*$A \leq_T B$.* Given $x$, use $B$ to find a stage $s \geq x$ with $B_s \uh (x+1) = B \uh (x+1)$. An element $x$ enumerated at a stage $t + 1 > s$ requires $B_{t+1} \uh x \neq B_t \uh x$, which is impossible after $s$. So $x \in A$ if and only if $x \in A_s$.

*$A$ meets every infinite $W_e$.* Suppose that $W_e$ is infinite and $e$ never acts. Let $x_0 > 2e$ be such that $c_K(x, s) < 2^{-e}$ for all $x \geq x_0$ and all $s$. Then for every $x \geq x_0$ in $W_e$, entering $W_e$ at stage $s_x$, say, $B$ does not change below $x$ after stage $\max(s_x, e)$: otherwise $e$ would act at such a stage. So, given $y$, one computes $B \uh y$ by searching for $x \in W_e$ with $x \geq \max(x_0, y)$ and reading $B_{\max(s_x, e)} \uh y$. This makes $B$ computable, a contradiction. So every infinite $W_e$ is met, and $A$ is simple, hence non-computable.
:::
::::

## Notes and references

Solovay (1975) built the first non-computable K-trivial set, in an unpublished manuscript; Zambella (1990) adapted the construction to obtain a c.e. one. The cost function form given here, with the theorem that obeying $c_K$ implies K-triviality, is due to Downey, Hirschfeldt, Nies and Stephan (2003); Kummer found a similar construction independently, and Kučera and Terwijn (1999) had used the same idea to build a non-computable c.e. set that is low for randomness. Nies developed the general theory of cost functions and proved that every K-trivial set obeys $c_K$. The permitting construction of the third exercise is one of the variations of the construction noted by Downey, Hirschfeldt, Nies and Stephan (see Downey and Hirschfeldt, Section 11.1.1): every non-zero c.e. degree bounds a non-computable c.e. K-trivial set.

The material is in Nies, *Computability and Randomness*, Section 5.3 (Definitions 5.3.1–5.3.4, Theorem 5.3.10, Proposition 5.3.11) and Section 5.5 (Theorem 5.5.2), and in Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Sections 11.1 (Theorem 11.1.5) and 11.5 (Definition 11.5.1, Theorem 11.5.3).

- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished manuscript, IBM Thomas J. Watson Research Center, 1975.
- D. Zambella, *On sequences with simple initial segments*, ILLC Technical Report ML-1990-05, University of Amsterdam, 1990.
- A. Kučera and S. A. Terwijn, *Lowness for the class of random sets*, Journal of Symbolic Logic 64 (1999), 1396–1402.
- R. G. Downey, D. R. Hirschfeldt, A. Nies and F. Stephan, *Trivial reals*, in: Proceedings of the 7th and 8th Asian Logic Conferences, 2003, 103–131.
- A. Nies, *Lowness properties and randomness*, Advances in Mathematics 197 (2005), 274–305.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 5.3 and 5.5.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 11.1 and 11.5.
