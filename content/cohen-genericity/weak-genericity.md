---
title: Weakly 1-generic sets
summary: Sets meeting every dense c.e. set of strings; Kurtz's theorem identifies their degrees with the hyperimmune degrees; weak n-genericity.
duration: 45
prerequisites: [baire-category, immunity-growth/immune-sets]
---

The first effective level of genericity asks a set to meet every dense set of strings that can be enumerated by an algorithm. These **weakly 1-generic** sets are not computable, and Kurtz showed that the degrees that compute one are exactly the degrees computing a function that escapes domination by every computable function. Genericity, a topological notion, thus coincides at this level with a notion of growth. This lesson proves Kurtz's theorem and introduces the hierarchy of weak $n$-genericity.

## Definition

We fix a computable enumeration $(W_e)$ of the c.e. sets of strings, through codes of strings, with finite approximations $W_e[t]$ computable from $(e, t)$ and increasing in $t$.

:::definition{#def-weakly-generic}
A set $G$ is **weakly 1-generic** if it meets every dense c.e. set of strings. More generally, $G$ is **weakly $n$-generic** if it meets every dense $\Sigma^0_n$ set of strings.
:::

There are countably many c.e. sets of strings, so weakly 1-generic sets exist, and the class of weakly $n$-generic sets is co-meager for every $n$ (:ref{#prop-generic-comeager}). Since the family of dense $\Sigma^0_{n+1}$ sets contains the dense $\Sigma^0_n$ sets, weak $(n+1)$-genericity implies weak $n$-genericity.

:::example{#ex-weakly-generic}
Let $G$ be weakly 1-generic.

1. $G$ is not computable: for a computable $X$, the set $\{ \sigma : \sigma \not\prec X \}$ is dense and computable.
2. $G$ is infinite and coinfinite, and contains blocks $1^k$ and $0^k$ of every length: the corresponding sets of strings of :ref{#ex-generic-properties} are dense and computable.
3. Every finite modification of $G$ is weakly 1-generic. If $\tilde G$ differs from $G$ exactly on the finite set $F$, and $W$ is a dense c.e. set of strings, let $W_F$ be the set of strings obtained from a string of $W$ longer than every element of $F$ by flipping its bits at the positions in $F$. It is dense and c.e., $G$ meets it, so $\tilde G$ meets $W$.

The definition only constrains $G$ through dense sets. A c.e. set of strings that is not dense, such as $\{ \sigma : \sigma(0) = 1 \}$, may or may not be met. The next lesson adds the requirement that such sets be met or avoided.
:::

## Hyperimmune functions

:::definition{#def-hyperimmune-function}
Recall from :ref{#def-hyperimmune-fn} that a function $f : \nat \to \nat$ is **hyperimmune** if no computable function dominates it, that is, for every computable $g$ there is $n$ with $f(n) > g(n)$, and that a set has **hyperimmune degree** if it computes a hyperimmune function.
:::

Equivalently, a set has hyperimmune degree if and only if it is not **computably dominated**, that is, if some total function it computes is dominated by no computable function (:ref{#def-computably-dominated}). A hyperimmune function exceeds every computable function at infinitely many points: if $f(n) \leq g(n)$ for all $n \geq n_0$, a finite modification of $g$ dominates $f$ everywhere. Every non-computable $\Delta^0_2$ set has hyperimmune degree, since it computes its computation function, which no computable function dominates (:ref{#thm-computation-function}). On the other side, computably dominated non-computable sets exist (:ref{to="immunity-growth/computably-dominated"}).

## Kurtz's theorem

:::theorem[Kurtz]{#thm-kurtz}
For every set $X$, the following are equivalent:

1. $X$ has hyperimmune degree;
2. $X$ computes a function $h$ that is equal to every computable function at infinitely many points;
3. $X$ computes a weakly 1-generic set.
:::

The direction (3 ⇒ 2) reads a function off the generic set: a dense set of strings can prescribe the length of a block of zeros, so the lengths of the blocks of zeros of $G$ agree with every computable function infinitely often. The direction (1 ⇒ 3) is a construction. To meet a dense c.e. set $W_e$, a construction by finite extensions would ask whether the current string has an extension in $W_e$, a $\Sigma^0_1$ question that a hyperimmune function cannot answer. Instead, the construction searches for an extension in $W_e$ for a number of steps given by the hyperimmune function $f$. If the search failed at almost every stage, the time needed to find extensions in $W_e$, which is a computable function of the stage since $W_e$ is dense, would dominate $f$. Since $f$ escapes this computable function infinitely often, the search succeeds at infinitely many stages; priorities between the indices ensure that one of these successes is used.

:::proof{of=thm-kurtz}
(3 ⇒ 2) Let $G \leq_T X$ be weakly 1-generic. By :ref{#ex-weakly-generic}, $G$ is infinite. Let $h(n)$ be the number of zeros of $G$ that follow position $n - 1$ before the next $1$: the largest $k$ such that $(G \uh n)\, 0^k \prec G$. It is $G$-computable. Let $f$ be computable and $m \in \nat$. The set $\{ \sigma\, 0^{f(|\sigma|)}\, 1 : |\sigma| \geq m \}$ is dense and computable, so $G$ has a prefix $\sigma\, 0^{f(n)}\, 1$ with $n = |\sigma| \geq m$, and then $h(n) = f(n)$. So $h$ equals $f$ at infinitely many points.

(2 ⇒ 1) If $h$ equals every computable function infinitely often, then $h + 1$ exceeds every computable function at some point.

(1 ⇒ 3) Let $f \leq_T X$ be hyperimmune. We build $G$ with oracle $f$, one bit per stage: at stage $s$, the prefix $\sigma_s = G \uh s$ is known. Say that $e$ is **met** at stage $s$ if some prefix of $\sigma_s$ belongs to $W_e[f(t)]$ for some $t \leq s$; once met, $e$ stays met, since $\sigma_s \prec \sigma_{s+1}$. The construction may have a **target**: a pair $(\tau, e)$ with $\tau \succeq \sigma_s$ and $\tau \in W_e$.

*Stage $s$.* Look for the least $e \leq s$ such that $e$ is not met at stage $s$ and some $\tau \succeq \sigma_s$ belongs to $W_e[f(s)]$. If there is one, and there is no current target or the current target has an index larger than $e$, make $(\tau, e)$ the current target, for the first such $\tau$. Then let $G(s)$ be the bit of the current target at position $s$ if the target is longer than $s$, and $0$ otherwise. When the target is a prefix of $\sigma_{s+1}$, it is achieved, $e$ is met, and there is no current target.

The construction is computable in $f$, so $G \leq_T X$. We show that $G$ meets every dense c.e. set $W_e$.

*Each index sets a target finitely often.* An index $e$ sets a target only when it is not met; its target is then copied bit by bit, and is achieved unless it is replaced by a target of smaller index. By induction on $e$: if the indices smaller than $e$ set targets finitely often, then after they stop and their last targets are achieved or replaced, any target of $e$ is achieved, after which $e$ is met and never sets a target again.

*Dense sets are met.* Suppose $W_e$ is dense and $e$ is never met. Let $s_0 \geq e$ be a stage after which no index smaller than $e$ sets a target and none of their targets is current. If at some stage $s \geq s_0$ some $\tau \succeq \sigma_s$ belonged to $W_e[f(s)]$, then $e$ would be the least index with a candidate (a smaller index with a candidate would set a target at stage $s$, since no target of smaller index is current), $e$ would set a target unless its own target is current, and this target would be achieved, so $e$ would be met. Hence, for every $s \geq s_0$, no extension of $\sigma_s$ belongs to $W_e[f(s)]$. Now let $g(s)$ be the least $t$ such that every string of length $s$ has an extension in $W_e[t]$; $g$ is computable and total, since $W_e$ is dense and there are finitely many strings of length $s$. Since $\sigma_s$ has length $s$, the previous observation gives $f(s) < g(s)$ for all $s \geq s_0$, so a finite modification of $g$ dominates $f$, contradicting the hyperimmunity of $f$.
:::

:::figure[The dense set used in (3 ⇒ 2) of :ref{#thm-kurtz}. The set $\{ \sigma\, 0^{f(|\sigma|)}\, 1 \}$ prescribes, after a prefix of length $n$, a block of exactly $f(n)$ zeros. A weakly 1-generic $G$ has such a prefix, and the function $h$, which counts the zeros of $G$ after position $n - 1$, takes the value $f(n)$ at $n$.]
<svg class="fig" viewBox="0 0 600 118" width="600" role="img" aria-label="A prefix of G: a string sigma of length n, followed by f(n) zeros and a one; the number of zeros after position n-1 is h(n) = f(n)"><rect x="30" y="40" width="26" height="26" class="cell"/><rect x="56" y="40" width="26" height="26" class="cell"/><rect x="82" y="40" width="26" height="26" class="cell"/><rect x="108" y="40" width="26" height="26" class="cell"/><rect x="134" y="40" width="26" height="26" class="cell"/><rect x="160" y="40" width="26" height="26" class="cell head-cell"/><text x="173.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="186" y="40" width="26" height="26" class="cell head-cell"/><text x="199.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="212" y="40" width="26" height="26" class="cell head-cell"/><text x="225.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="238" y="40" width="26" height="26" class="cell head-cell"/><text x="251.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="264" y="40" width="26" height="26" class="cell head-cell"/><text x="277.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="290" y="40" width="26" height="26" class="cell head-cell"/><text x="303.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="316" y="40" width="26" height="26" class="cell head-cell"/><text x="329.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="342" y="40" width="26" height="26" class="cell head-cell"/><text x="355.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="368" y="40" width="26" height="26" class="cell head-cell"/><text x="381.0" y="58" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="394" y="40" width="26" height="26" class="cell"/><text x="407.0" y="58" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="420" y="40" width="26" height="26" class="cell" stroke-dasharray="3 3"/><rect x="446" y="40" width="26" height="26" class="cell" stroke-dasharray="3 3"/><rect x="472" y="40" width="26" height="26" class="cell" stroke-dasharray="3 3"/><text x="506" y="58" class="mrm muted" font-size="15">⋯</text><text x="95.0" y="58" text-anchor="middle" class="math" font-size="16">σ</text><text x="160" y="32" text-anchor="middle" class="label">position n</text><line x1="160" y1="36" x2="160" y2="70" class="accent-stroke" stroke-width="1.2" stroke-dasharray="2 2"/><path d="M31,72 L31,78 L159,78 L159,72" class="muted-stroke" stroke-width="1.2"/><text x="95.0" y="94" text-anchor="middle" class="label">G↾n = σ, of length n</text><path d="M161,72 L161,78 L393,78 L393,72" class="muted-stroke" stroke-width="1.2"/><text x="277.0" y="94" text-anchor="middle" class="label">f(n) zeros: h(n) = f(n)</text></svg>
:::

The construction of (1 ⇒ 3) is a finite injury argument without restraints, in the sense of the course on c.e. degrees: an index may lose its target to an index of smaller code, but only finitely often. The hyperimmune function serves as a bound on the search for extensions, and the verification is an **escape argument**, as in the course on immunity and growth: a dense c.e. set that is never met would provide a computable function dominating $f$.

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

Item 2 shows that the hypothesis of (1 ⇒ 3) cannot be weakened: below a non-computable computably dominated set, there is no weakly 1-generic set. Item 3 relativizes: no weakly $(n+1)$-generic set is computable in $\emptyset^{(n)}$, since $\{ \sigma : \sigma \not\prec X \}$ is $\Sigma^0_{n+1}$ for $X \leq_T \emptyset^{(n)}$.

Two strengthenings of Kurtz's theorem are admitted. The weakly 1-generic set can be taken of the same degree as $X$: every hyperimmune degree *contains* a weakly 1-generic set (Kurtz; Downey and Hirschfeldt 2010, Theorem 2.24.14 for $n = 0$ and Corollary 2.24.19). The proof codes $X$ into $G$ in the manner of the next lessons. And for c.e. sets, much more is true: every non-computable c.e. set computes a 1-generic set, by a permitting argument (Downey and Hirschfeldt 2010, Proposition 2.24.2).

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

## Higher levels

The direction (3 ⇒ 1) relativizes without change: a weakly $(n+1)$-generic set computes a function that is dominated by no $\emptyset^{(n)}$-computable function (second exercise below, relativized). The converse direction does not relativize at all levels. Andrews, Gerdes and Miller showed that a set computes a weakly 2-generic set if and only if it computes a function dominated by no $\Delta^0_2$ function, using the fact that $\Delta^0_2$ functions are limits of computable approximations. At the next level the analogy breaks down: for every countable family of functions $\mathcal F$, there is a function that escapes every member of $\mathcal F$ and computes no weakly 3-generic set (Andrews, Gerdes and Miller; Monin and Patey, chapter *Cohen forcing*). These results are admitted.

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
By :ref{#ex-weakly-generic}, $G$ is infinite, so $p_G(n)$, the $n$-th element of $G$ in increasing order (counting from $0$), is defined for every $n$. Let $f$ be computable. The set $D = \{ \sigma\, 0^{f(|\sigma|) + 1} : \sigma \in \bstr \}$ is dense and computable, so $G$ has a prefix $\sigma\, 0^{f(n) + 1}$, with $n = |\sigma|$. At most $n$ elements of $G$ lie below $n$, so the elements of index $0, \dots, n$ in increasing order cannot all lie below $n$, and $p_G(n) \geq n$. No element of $G$ lies in the interval $[n, n + f(n)]$, so $p_G(n) \geq n + f(n) + 1 > f(n)$. Hence no computable function dominates $p_G$.
:::
::::

## Notes and references

Weakly 1-generic sets and the equivalence with hyperimmune degrees are due to Kurtz (1981), in his thesis on randomness and genericity, and appear in his paper on weak genericity (1983). The presentation of (1 ⇒ 3) by one bit per stage follows the standard modern proofs; Monin and Patey use a recursive search procedure instead, and Downey and Hirschfeldt prove the degree form directly. The second exercise is the case $n = 0$ of Downey and Hirschfeldt (2010, Theorem 2.24.12). The results of Andrews, Gerdes and Miller are presented, with a proof of the second one, in Monin and Patey.

- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana-Champaign, 1981.
- S. A. Kurtz, *Notions of weak genericity*, Journal of Symbolic Logic 48 (1983), 764–770.
- U. Andrews, P. Gerdes and J. S. Miller, *The degrees of bi-hyperhyperimmune sets*, Annals of Pure and Applied Logic 165 (2014), 803–811.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.24.
- B. Monin and L. Patey, *Computability theory*, chapter *Cohen forcing*, section *Effective genericity*.
