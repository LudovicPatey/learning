---
title: Weakly 1-generic sets
summary: Sets meeting every dense c.e. set of strings; Kurtz's theorem identifies their degrees with the hyperimmune degrees; weak n-genericity.
duration: 40
prerequisites: [baire-category]
---

The first effective level of genericity asks a set to meet every dense set of strings that can be enumerated by an algorithm. These **weakly 1-generic** sets are not computable, and Kurtz showed that the degrees that compute one are exactly the degrees computing a function that escapes domination by every computable function. Genericity, a topological notion, thus coincides at this level with a notion of growth. This lesson proves Kurtz's theorem and introduces the hierarchy of weak $n$-genericity.

## Definition

We fix a computable enumeration $(W_e)$ of the c.e. sets of strings, through codes of strings, with finite approximations $W_e[t]$ computable from $(e, t)$ and increasing in $t$.

:::definition{#def-weakly-generic}
A set $G$ is **weakly 1-generic** if it meets every dense c.e. set of strings. More generally, $G$ is **weakly $n$-generic** if it meets every dense $\Sigma^0_n$ set of strings.
:::

There are countably many c.e. sets of strings, so weakly 1-generic sets exist, and the class of weakly $n$-generic sets is co-meager for every $n$ (:ref{#prop-generic-comeager}). A weakly 1-generic set is not computable: for a computable $X$, the set $\{ \sigma : \sigma \not\prec X \}$ is dense and computable. Since the family of dense $\Sigma^0_{n+1}$ sets contains the dense $\Sigma^0_n$ sets, weak $(n+1)$-genericity implies weak $n$-genericity.

## Hyperimmune functions

:::definition{#def-hyperimmune-function}
A function $f : \nat \to \nat$ is **hyperimmune** if no computable function dominates it, that is, for every computable $g$ there is $n$ with $f(n) > g(n)$. A set has **hyperimmune degree** if it computes a hyperimmune function.
:::

Equivalently, a set has hyperimmune degree if and only if it is not computably dominated (:ref{#def-computably-dominated}). A hyperimmune function exceeds every computable function at infinitely many points: if $f(n) \leq g(n)$ for all $n \geq n_0$, a finite modification of $g$ dominates $f$ everywhere. These functions and the corresponding sets are studied in the course on immunity and growth of functions (:ref{to="immunity-growth/immune-sets"}). Every non-computable $\Delta^0_2$ set has hyperimmune degree, since it computes its computation function, which no computable function dominates (:ref{#thm-computation-function}).

## Kurtz's theorem

:::theorem[Kurtz]{#thm-kurtz}
For every set $X$, the following are equivalent:

1. $X$ has hyperimmune degree;
2. $X$ computes a function $h$ that is equal to every computable function at infinitely many points;
3. $X$ computes a weakly 1-generic set.
:::

:::proof{of=thm-kurtz}
(3 ⇒ 2) Let $G \leq_T X$ be weakly 1-generic. For each $m$, the set of strings with a $1$ at some position at least $m$ is dense and computable, so $G$ is infinite. Let $h(n)$ be the number of zeros of $G$ that follow position $n - 1$ before the next $1$: the largest $k$ such that $(G \uh n)\, 0^k \prec G$. It is $G$-computable. Let $f$ be computable and $m \in \nat$. The set $\{ \sigma\, 0^{f(|\sigma|)}\, 1 : |\sigma| \geq m \}$ is dense and computable, so $G$ has a prefix $\sigma\, 0^{f(n)}\, 1$ with $n = |\sigma| \geq m$, and then $h(n) = f(n)$. So $h$ equals $f$ at infinitely many points.

(2 ⇒ 1) If $h$ equals every computable function infinitely often, then $h + 1$ exceeds every computable function at some point.

(1 ⇒ 3) Let $f \leq_T X$ be hyperimmune. We build $G$ with oracle $f$, one bit per stage: at stage $s$, the prefix $\sigma_s = G \uh s$ is known. Say that $e$ is **met** at stage $s$ if some prefix of $\sigma_s$ belongs to $W_e[f(s)]$; once met, $e$ stays met. The construction may have a **target**: a pair $(\tau, e)$ with $\tau \succeq \sigma_s$ and $\tau \in W_e$.

*Stage $s$.* Look for the least $e \leq s$ such that $e$ is not met at stage $s$ and some $\tau \succeq \sigma_s$ belongs to $W_e[f(s)]$. If there is one, and there is no current target or the current target has an index larger than $e$, make $(\tau, e)$ the current target, for the first such $\tau$. Then let $G(s)$ be the bit of the current target at position $s$ if the target is longer than $s$, and $0$ otherwise. When the target is a prefix of $\sigma_{s+1}$, it is achieved, $e$ is met, and there is no current target.

The construction is computable in $f$, so $G \leq_T X$. We show that $G$ meets every dense c.e. set $W_e$.

*Each index sets a target finitely often.* An index $e$ sets a target only when it is not met; its target is then copied bit by bit, and is achieved unless it is replaced by a target of smaller index. By induction on $e$: if the indices smaller than $e$ set targets finitely often, then after they stop and their last targets are achieved or replaced, any target of $e$ is achieved, after which $e$ is met and never sets a target again.

*Dense sets are met.* Suppose $W_e$ is dense and $e$ is never met. Let $s_0 \geq e$ be a stage after which no index smaller than $e$ sets a target and none of their targets is current. If at some stage $s \geq s_0$ some $\tau \succeq \sigma_s$ belonged to $W_e[f(s)]$, then $e$ would be the least index with a candidate, would set a target, and this target would be achieved, so $e$ would be met. Hence, for every $s \geq s_0$, no extension of $\sigma_s$ belongs to $W_e[f(s)]$. Now let $g(s)$ be the least $t$ such that every string of length $s$ has an extension in $W_e[t]$; $g$ is computable and total, since $W_e$ is dense and there are finitely many strings of length $s$. Since $\sigma_s$ has length $s$, the previous observation gives $f(s) < g(s)$ for all $s \geq s_0$, so a finite modification of $g$ dominates $f$, contradicting the hyperimmunity of $f$.
:::

The construction of (1 ⇒ 3) is a finite injury argument without restraints: an index may lose its target to an index of smaller code, but only finitely often. The hyperimmune function $f$ serves as a bound on the search for extensions: a dense c.e. set that is never met would provide a computable bound on $f$.

:::corollary{#cor-delta2-weak-generic}
1. Every non-computable $\Delta^0_2$ set, in particular every non-computable c.e. set, computes a weakly 1-generic set.
2. A computably dominated set computes no weakly 1-generic set; in particular, no weakly 1-generic set is computably dominated.
3. No weakly 2-generic set is computable in $\emptyset'$.
:::

:::proof{of=cor-delta2-weak-generic}
1. A non-computable $\Delta^0_2$ set has hyperimmune degree, as recalled above.
2. By the theorem, a set computing a weakly 1-generic set has hyperimmune degree.
3. If $X \leq_T \emptyset'$, the set $\{ \sigma : \sigma \not\prec X \}$ is dense and computable in $\emptyset'$, hence $\Sigma^0_2$; a weakly 2-generic set meets it, so it is not $X$.
:::

:::quiz[Kurtz's theorem]
In (3 ⇒ 2), why is the dense set restricted to strings $\sigma$ of length at least $m$?

- [x] To obtain points $n \geq m$ where $h(n) = f(n)$, for every $m$, hence infinitely many such points.
- [ ] To make the set computable.

  The set is computable with or without the restriction.
- [ ] To make the set dense.

  The set without the restriction is dense as well.

---

In (1 ⇒ 3), why does the construction add exactly one bit per stage?

- [x] So that $\sigma_s$ has length exactly $s$, and the computable function $g$, defined from the strings of length $s$, bounds the search time for $\sigma_s$.

  If the length of $\sigma_s$ were not computably bounded, no computable function could bound the time needed to find an extension of $\sigma_s$ in $W_e$.
- [ ] To make $G$ computable.

  $G$ is computable in $f$, not computable.
- [ ] To avoid conflicts between targets.

  Conflicts are resolved by priority, whatever the speed of the construction.

---

Where is the hyperimmunity of $f$ used?

- [x] In the last step: if a dense $W_e$ were never met, the computable function $g$ would exceed $f$ from some point on.
- [ ] To show that each index sets a target finitely often.

  This holds for every function $f$.
- [ ] To show that $G$ is computable in $X$.

  This holds for every $f \leq_T X$.
:::

## Exercises

::::exercise{difficulty=1}
Show that if $G$ is weakly 1-generic, then so is its complement $\nat \setminus G$.

:::solution
For a set of strings $W$, let $\bar W = \{ \bar\sigma : \sigma \in W \}$, where $\bar\sigma$ flips all bits of $\sigma$. If $W$ is c.e. and dense, so is $\bar W$, since $\sigma \mapsto \bar\sigma$ is a computable bijection preserving the prefix relation. $G$ meets $\bar W$, so $\nat \setminus G$ meets $W$.
:::
::::

::::exercise{difficulty=2}
Show that the principal function $p_G$ of a weakly 1-generic set $G$ is hyperimmune.

:::solution
Let $f$ be computable. The set $D = \{ \sigma\, 0^{f(|\sigma|) + 1} : \sigma \in \bstr \}$ is dense and computable, so $G$ has a prefix $\sigma\, 0^{f(n) + 1}$, with $n = |\sigma|$. At most $n$ elements of $G$ lie below $n$, so the elements of index $0, \dots, n$ in increasing order cannot all lie below $n$, and $p_G(n) \geq n$. No element of $G$ lies in the interval $[n, n + f(n)]$, so $p_G(n) \geq n + f(n) + 1 > f(n)$. Hence no computable function dominates $p_G$.
:::
::::

## Notes and references

Weakly 1-generic sets and the equivalence with hyperimmune degrees are due to Kurtz (1981), in his thesis on randomness and genericity; the presentation of (1 ⇒ 3) by one bit per stage follows the standard modern proofs. Andrews, Gerdes and Miller showed that the analogy between weak genericity and escaping functions breaks down from the level of weak 3-genericity. Downey and Hirschfeldt's book treats these notions in detail.

- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana-Champaign, 1981.
- U. Andrews, P. Gerdes and J. S. Miller, *The degrees of bi-hyperhyperimmune sets*, Annals of Pure and Applied Logic 165 (2014), 803–811.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010.
