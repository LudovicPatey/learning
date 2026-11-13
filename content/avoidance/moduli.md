---
title: Moduli and preservation of hyperimmunity
summary: Moduli and the duality between computing a set and computing fast-growing functions; a problem preserves hyperimmunity if its solutions never compute a function dominating a given hyperimmune one; this implies cone avoidance, and is equivalent to it by a theorem of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky.
duration: 35
prerequisites: [non-sigma1-definitions, turing-degrees/limit-computability, immunity-growth/immune-sets]
---

There is a duality between computing sets and computing fast-growing functions. A set computes $\emptyset'$ if and only if it computes a function dominating the modulus of the standard enumeration of $\emptyset'$ (:ref{#cor-complete-domination}); more generally, a non-computable $\Delta^0_2$ set is computed by every function dominating its computation function (:ref{#thm-computation-function}). The lower bounds for Ramsey's theorem use this duality: the homogeneous sets of the coloring of triples of :ref{#prop-rt32-jump} compute $\emptyset'$ because they are sparse, so that their principal functions dominate a modulus. A problem that can force its solutions to compute fast-growing functions is a candidate for encoding sets. This lesson defines the corresponding avoidance property, the **preservation of hyperimmunity**, and relates it to cone avoidance through moduli. The next lesson proves it for the problems of the course with **compact** forcing questions.

Recall that a function $f$ is **hyperimmune** if no computable function dominates it (:ref{#def-hyperimmune-fn}), where $g$ dominates $f$ if $g(x) \geq f(x)$ for every $x$. Relative to a set $W$, $f$ is **$W$-hyperimmune** if no $W$-computable function dominates it. Changing finitely many values of a dominating function does not change its degree, so "dominates" may equivalently be read as "dominates from some point on".

## Moduli

:::definition{#def-relative-modulus}
Let $Z$ be a set. A function $m$ is a **modulus of $C$ relative to $Z$** if $C \leq_T Z \oplus g$ for every function $g$ that dominates $m$.
:::

By :ref{#cor-complete-domination}, the modulus of the standard approximation of $\emptyset'$ is a modulus of $\emptyset'$ relative to $\emptyset$. A modulus of a set relative to $Z$ is a growth rate beyond which every function, together with $Z$, knows the set. Not every set has one: Solovay showed that the sets having a modulus relative to $\emptyset$ are exactly the hyperarithmetic sets. The $\Delta^0_2$ sets have moduli that are computable in them.

:::lemma{#lem-delta2-modulus}
Let $C \leq_T Z'$. There is a function $m \leq_T C \oplus Z$ that is a modulus of $C$ relative to $Z$.
:::

:::proof{of=lem-delta2-modulus}
By the limit lemma relativized to $Z$ (:ref{#thm-limit-lemma}), $C$ has a $Z$-computable approximation $(C_s)$. Let $m$ be its computation function (:ref{#def-modulus}): $m(x)$ is the least $s \geq x$ with $C_s \uh x = C \uh x$, which is found with oracle $C \oplus Z$. The proof of :ref{#thm-computation-function} relativized to $Z$ shows that for every $g$ dominating $m$, $C$ is computable in $g \oplus Z$: the function $M$ of that proof is computable in $g$ and the approximation.
:::

:::lemma{#lem-modulus-hyperimmune}
Let $m$ be a modulus of $C$ relative to $Z$, and $Y$ a set.

1. If $C \not\leq_T Z \oplus Y$, then $m$ is $(Z \oplus Y)$-hyperimmune.
2. If $m \leq_T C \oplus Z$ and $m$ is $(Z \oplus Y)$-hyperimmune, then $C \not\leq_T Z \oplus Y$.
:::

:::proof{of=lem-modulus-hyperimmune}
1. If a function $g \leq_T Z \oplus Y$ dominated $m$, then $C \leq_T Z \oplus g \leq_T Z \oplus Y$.
2. If $C \leq_T Z \oplus Y$, then $m \leq_T C \oplus Z \leq_T Z \oplus Y$, and $m$ dominates itself.
:::

For a set $C \leq_T Z'$ with $C \not\leq_T Z$ and the modulus $m$ of :ref{#lem-delta2-modulus}, the two items say that a set $Y$ avoids the cone above $C$ together with $Z$ if and only if $m$ remains hyperimmune relative to $Z \oplus Y$. For such sets, cone avoidance is a statement about the growth of the functions computed by the solutions.

## Preservation of hyperimmunity

:::definition{#def-preserve-hyperimmunity}
A problem $\mathsf P$ admits **preservation of hyperimmunity** if for every set $Z$, every $Z$-hyperimmune function $f$, and every instance $X \leq_T Z$ of $\mathsf P$, there is a solution $Y$ to $X$ such that $f$ is $(Z \oplus Y)$-hyperimmune. It admits **strong** preservation of hyperimmunity if the same holds for every instance $X$.
:::

For a fixed $f$, the class of sets $W$ such that $f$ is $W$-hyperimmune is closed downwards, so this is again the preservation of a family of weakness properties. The problem $\mathsf J$ does not admit it: the modulus of $\emptyset'$ is hyperimmune, by :ref{#lem-modulus-hyperimmune} with $Z = Y = \emptyset$, and it is computable in $\emptyset'$. Unlike preservation of non-$\Sigma^0_1$ definitions, preservation of hyperimmunity has no immediate relation with cone avoidance: a hyperimmune function need not be a modulus of any non-computable set relative to $\emptyset$. For instance, let $G$ be Cohen generic for all the hyperarithmetic dense sets of strings. Its principal function $p_G$ is hyperimmune, and $G$ computes no non-computable hyperarithmetic set. If $p_G$ were a modulus of a set $A$, then $A$ would be hyperarithmetic by Solovay's theorem, and computable in $p_G$, which dominates itself, hence in $G$; so $A$ is computable. The relation appears after relativizing, through the theorem that every set is $\Delta^0_2$ relative to a set avoiding a cone.

:::theorem[Downey, Greenberg, Harrison-Trainor, Patey, Turetsky]{#thm-hyperimmunity-cone}
If a problem admits preservation of hyperimmunity, it admits cone avoidance.
:::

:::proof{of=thm-hyperimmunity-cone}
Let $C \not\leq_T Z$, and $X \leq_T Z$ an instance. By :ref{#thm-delta2-cone-avoidance}, there is a set $W$ with $C \not\leq_T Z \oplus W$ and $C \leq_T W' \leq_T (Z \oplus W)'$. By :ref{#lem-delta2-modulus} relative to $Z \oplus W$, $C$ has a modulus $m$ relative to $Z \oplus W$ with $m \leq_T C \oplus Z \oplus W$. By :ref{#lem-modulus-hyperimmune} (1) with $Y = \emptyset$, $m$ is $(Z \oplus W)$-hyperimmune. The instance $X$ is computable in $Z \oplus W$, so preservation of hyperimmunity relative to $Z \oplus W$ gives a solution $Y$ such that $m$ is $(Z \oplus W \oplus Y)$-hyperimmune. By :ref{#lem-modulus-hyperimmune} (2), $C \not\leq_T Z \oplus W \oplus Y$, hence $C \not\leq_T Z \oplus Y$.
:::

The set $W$ is the price of relativization: $C$ itself need not have a modulus relative to $Z$, but it has one relative to $Z \oplus W$, and $W$ was chosen so as not to help computing $C$. The converse uses a construction in the opposite direction, which we admit.

:::theorem[Downey, Greenberg, Harrison-Trainor, Patey, Turetsky]{#thm-hyperimmune-modulus}
For every set $Z$ and every non-decreasing $Z$-hyperimmune function $f$, there are sets $W$ and $A$ such that $A \not\leq_T Z \oplus W$ and $f$ is a modulus of $A$ relative to $W$.
:::

:::corollary{#cor-hyperimmunity-equivalence}
A problem admits preservation of hyperimmunity if and only if it admits cone avoidance.
:::

:::proof{of=cor-hyperimmunity-equivalence}
One direction is :ref{#thm-hyperimmunity-cone}. Conversely, assume cone avoidance, and let $f$ be $Z$-hyperimmune and $X \leq_T Z$ an instance. By the first exercise, we may assume that $f$ is non-decreasing. Let $W$ and $A$ be given by :ref{#thm-hyperimmune-modulus}. Cone avoidance relative to $Z \oplus W$ gives a solution $Y$ with $A \not\leq_T Z \oplus W \oplus Y$. If some $g \leq_T Z \oplus Y$ dominated $f$, then $A \leq_T W \oplus g \leq_T Z \oplus W \oplus Y$. So $f$ is $(Z \oplus Y)$-hyperimmune.
:::

:::quiz[hyperimmunity and cone avoidance]
In the proof of :ref{#thm-hyperimmunity-cone}, why is the set $W$ needed?

- [x] Because $C$ is arbitrary and need not have a modulus relative to $Z$ at all (by Solovay's theorem, only hyperarithmetic sets have one relative to $\emptyset$); $W$ makes $C$ a $\Delta^0_2$ set relative to $Z \oplus W$, which gives a modulus computable from $C \oplus Z \oplus W$, without making $C$ computable in $Z \oplus W$.
- [ ] Because the instance $X$ is not computable in $Z$.

  $X$ is computable in $Z$, hence in $Z \oplus W$.
- [ ] Because preservation of hyperimmunity only applies to computable instances.

  The definition is relativized to every $Z$; $W$ serves to produce a modulus.

---

Where is item 2 of :ref{#lem-modulus-hyperimmune} used, and why does it need $m \leq_T C \oplus Z$?

- [x] In the last step: if the solution computed $C$ together with $Z \oplus W$, it would compute $m$, which dominates itself; a modulus not computable from $C$ would give no contradiction.
- [ ] In the choice of $W$.

  $W$ comes from :ref{#thm-delta2-cone-avoidance}, independently of the modulus.
- [ ] To show that $m$ is hyperimmune relative to $Z \oplus W$.

  That is item 1.
:::

## Exercises

::::exercise{difficulty=1}
For a function $f$, let $F(n) = \max_{i \leq n} f(i)$. Show that for every set $W$, $f$ is $W$-hyperimmune if and only if $F$ is.

:::solution
Since $F \geq f$, a function dominating $F$ dominates $f$; so if $f$ is $W$-hyperimmune, so is $F$. Conversely, if $g \leq_T W$ dominates $f$, then $G(n) = \max_{i \leq n} g(i)$ is $W$-computable and $G(n) \geq g(i) \geq f(i)$ for every $i \leq n$, so $G$ dominates $F$.
:::
::::

::::exercise{difficulty=1}
Let $A$ be a non-computable computably dominated set (:ref{#def-computably-dominated}), and let $\mathsf P$ be the problem with the single instance $\emptyset$, whose single solution is $A$. Show that for every hyperimmune function $f$, $f$ is $A$-hyperimmune, but that $\mathsf P$ does not admit cone avoidance. Why does this not contradict :ref{#cor-hyperimmunity-equivalence}?

:::solution
Every $A$-computable function is dominated by a computable function, so a function dominating $f$ and computable in $A$ would give a computable function dominating $f$. The solution $A$ computes the non-computable set $A$, so cone avoidance fails with $Z = \emptyset$ and $C = A$. There is no contradiction: the property shown is the unrelativized version of preservation of hyperimmunity. Relative to $Z = A$ and with the instance $\emptyset \leq_T A$, the relativized version holds trivially, but relative to suitable other sets $Z$ it fails, as it must by :ref{#thm-hyperimmunity-cone}. This example is used by Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (Theorem 2.12) to separate the unrelativized versions.
:::
::::

## Notes and references

The duality between moduli and coding, and preservation of one hyperimmunity, follow the section *Preserving hyperimmunities* of the chapter *Cone avoidance* of Patey's monograph. :ref{#thm-hyperimmunity-cone} is Corollary 2.10 of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022), whose proof (their Lemma 2.9) goes through a variant of :ref{#thm-delta2-cone-avoidance} (their Lemma 2.8, attributed to Patey) and the modulus of a $\Delta^0_2$ set; :ref{#thm-hyperimmune-modulus} is their Lemma 2.6, and :ref{#cor-hyperimmunity-equivalence} their Corollary 2.7. The separations of the unrelativized versions are their Theorems 2.11 and 2.12; the problem of the last exercise is the one of Theorem 2.12. The characterization of the sets with a modulus as the hyperarithmetic sets is due to Solovay (1978).

- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- R. M. Solovay, *Hyperarithmetically encodable sets*, Transactions of the American Mathematical Society 239 (1978), 99–122.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Preserving hyperimmunities*.
