---
title: Measure and cototality
summary: A cototal set determines each of its bits from the others, a form of autoreducibility; hence, by the Lebesgue density lemma, the cototal sets form a null Π⁰₂-definable class, and no weakly 2-random set is cototal; Ω is cototal; the optimal randomness bounds for cototal degrees and for introenumerable sets (Ang Li).
duration: 20
prerequisites: [variants-of-cototality, randomness-notions/weak-2-randomness, martin-lof-randomness/upper-cones]
---

How common are cototal sets? A set $A$ with $A \leq_e \overline A$ has a strong internal regularity: whether $n$ belongs to $A$ can be decided from the other bits of $A$. Sets with such a property are rare in the sense of measure, and sufficiently random sets avoid them. This lesson proves that the cototal sets form a null class, determines the least level of randomness that excludes cototality, and states the corresponding results for cototal degrees and for introenumerable sets.

## Cototal sets are autoreducible

Fix an enumeration operator $\Gamma$ and let $\mathcal C_\Gamma = \{ X : X = \Gamma(\overline X) \}$, the class of sets that $\Gamma$ enumerates from their complements. A set is cototal if and only if it belongs to some $\mathcal C_\Gamma$.

:::lemma{#lem-cototal-autoreducible}
If $X \in \mathcal C_\Gamma$, then for every $n$: $n \in X$ if and only if $n \in \Gamma(\overline{X \setminus \{ n \}})$.
:::

:::proof{of=lem-cototal-autoreducible}
The complement of $X \setminus \{ n \}$ is $\overline X \cup \{ n \}$. If $n \in X$, then $n \in \Gamma(\overline X) \subseteq \Gamma(\overline X \cup \{ n \})$ by monotonicity. If $n \notin X$, then $\overline X \cup \{ n \} = \overline X$, and $n \notin \Gamma(\overline X) = X$.
:::

So a member of $\mathcal C_\Gamma$ is determined at $n$ by its values elsewhere: two members of $\mathcal C_\Gamma$ that differ only at $n$ cannot exist. This property is called **autoreducibility**, after Trakhtenbrot, here with a procedure that need not be computable.

:::theorem[Li]{#thm-cototal-null}
The class of cototal sets is null, and it is a countable union of $\Pi^0_2$ classes.
:::

:::proof{of=thm-cototal-null}
*Complexity.* $X \in \mathcal C_\Gamma$ if and only if, for every $n$: if $n \in X$, some axiom $\langle n, D \rangle$ of $\Gamma$ has $D \cap X = \emptyset$; and if $n \notin X$, every axiom $\langle n, D \rangle$ of $\Gamma$ has $D \cap X \neq \emptyset$. The first clause is $\forall n\, \exists$ (an axiom enumerated at some stage, and a finite check), the second $\forall n\, \forall s$ (a finite check on the axioms enumerated by stage $s$). So $\mathcal C_\Gamma$ is a $\Pi^0_2$ class, in particular Borel.

*Measure.* Suppose $\lambda(\mathcal C_\Gamma) > 0$. By the Lebesgue density lemma (:ref{#lem-density}), there is a string $\sigma$ with $\lambda(\mathcal C_\Gamma \mid \sigma) > 1/2$. Let $n \geq |\sigma|$, and let $h$ be the map that changes the bit $n$: $h(X) = X \triangle \{ n \}$. It is a bijection of $[\sigma]$ onto itself that preserves measure, since $n$ is beyond $\sigma$. By :ref{#lem-cototal-autoreducible}, $X$ and $h(X)$ are not both in $\mathcal C_\Gamma$: they agree outside $n$, so the lemma gives them the same value at $n$, while they differ there. So $\mathcal C_\Gamma \cap [\sigma]$ and $h(\mathcal C_\Gamma \cap [\sigma])$ are disjoint subsets of $[\sigma]$, each of measure more than half the measure of $[\sigma]$: a contradiction. Hence each $\mathcal C_\Gamma$ is null, and so is their countable union.
:::

:::corollary[Li]{#cor-w2r-not-cototal}
No weakly 2-random set is cototal.
:::

:::proof{of=cor-w2r-not-cototal}
A weakly 2-random set belongs to no null $\Pi^0_2$ class (:ref{#def-weak-2-random}), and each $\mathcal C_\Gamma$ is one.
:::

:::quiz[cototal sets are rare]
In the proof of :ref{#thm-cototal-null}, why must the bit $n$ be chosen beyond $\sigma$?

- [x] So that changing it keeps every sequence inside $[\sigma]$; the map $h$ is then a measure-preserving bijection of $[\sigma]$, and the two disjoint images of $\mathcal C_\Gamma \cap [\sigma]$ cannot both fill more than half of $[\sigma]$.
- [ ] Because the bits of $\sigma$ are not determined by the others.

  Every bit of a member of $\mathcal C_\Gamma$ is determined; the bits of $\sigma$ are fixed by the cylinder, which is why they cannot be flipped inside it.
- [ ] To make $\mathcal C_\Gamma$ a $\Pi^0_2$ class.

  The complexity does not depend on $n$.

---

Where is monotonicity of enumeration operators used?

- [x] In :ref{#lem-cototal-autoreducible}: adding $n$ to the oracle $\overline X$ keeps $n$ in the output when $n \in X$.
- [ ] To show that $\mathcal C_\Gamma$ is Borel.

  Borelness comes from the arithmetic definition.
- [ ] To show that $h$ preserves measure.

  Flipping one bit beyond $\sigma$ preserves the uniform measure on $[\sigma]$; operators play no role there.
:::

## The optimal bounds

Weak 2-randomness is the right level: Chaitin's halting probability, which is random, is cototal.

:::proposition[Li]{#prop-omega-cototal}
Let $\Omega$ be identified with the set of positions of the $1$s in its binary expansion. Then $\Omega \leq_e \overline \Omega$; so there is a Martin-Löf random cototal set.
:::

:::proof{of=prop-omega-cototal}
$\Omega$ is left-c.e. and irrational (it is random): there is a computable increasing sequence of rationals $q_s$ converging to $\Omega$ (:ref{#def-omega}). Given an enumeration of $\overline \Omega$, compute the bits of $\Omega$ one after the other. If the first $k$ bits form the string $\sigma$, let $d$ be the dyadic rational $0.\sigma 1$. The bit $k$ is $1$ if and only if $\Omega > d$, which happens if and only if some $q_s$ exceeds $d$; it is $0$ if and only if $k \in \overline \Omega$. Wait for the first of these two events, which occurs. The procedure computes $\Omega$ from any enumeration of $\overline \Omega$, uniformly, so it enumerates $\Omega$ by an enumeration operator: $n \in \Omega$ if and only if, for some finite subset $D$ of $\overline \Omega$ and some stage $s$, the procedure, run with the zeros listed in $D$ and the approximations up to $q_s$, outputs $1$ at $n$.
:::

For degrees, the bound moves up by one level. Li proved that no weakly 3-random set has cototal degree, and that some 2-random set has cototal degree, so these bounds are optimal; the proof of the first uses the same autoreducibility argument with the skip in place of the complement, since a set has cototal degree if and only if $A \leq_e A^\diamond$.

An infinite set $X$ is **introenumerable** if every infinite subset $Y \subseteq X$ satisfies $X \leq_e Y$, and **uniformly introenumerable** if a single operator works for all infinite subsets. Every cototal degree is uniformly introenumerable, and the introenumerable degrees are contained in the hyper-cototal degrees, defined with Sanchis's hyperenumeration reducibility (Goh et al.). Li showed that all these classes of degrees are null, that no Martin-Löf random set is introenumerable, and that no weakly 3-random set has introenumerable degree, again optimally. Whether every introenumerable degree is uniformly introenumerable is open.

::::exercise{#ex-cototal-class-meager difficulty=2 objective="Show by a genericity argument that cototality also fails for typical sets in the sense of category."}
Show that no 1-generic set is cototal. *Hint:* for $G = \Gamma(\overline G)$, consider the strings $\sigma$ such that $\Gamma$ enumerates, from the zeros of $\sigma$, a position where $\sigma$ is $0$.

:::solution
Suppose $G$ is 1-generic and $G = \Gamma(\overline G)$. For a string $\sigma$, let $Z_\sigma = \{ m < |\sigma| : \sigma(m) = 0 \}$, and let $S$ be the c.e. set of strings $\sigma$ such that $\sigma(n) = 0$ for some $n \in \Gamma(Z_\sigma)$. No prefix $\sigma$ of $G$ is in $S$: $Z_\sigma \subseteq \overline G$, so such an $n$ would be in $\Gamma(\overline G) = G$ while $\sigma(n) = 0$. By genericity, a prefix $\sigma$ of $G$ has no extension in $S$. Since $G$ is infinite, choose $n \geq |\sigma|$ in $G$; as $n \in \Gamma(\overline G)$, there is a finite $D \subseteq \overline G$ with $n \in \Gamma(D)$. Let $\tau \supseteq \sigma$ be the string of length $\max(D \cup \{ n \}) + 1$ that is $0$ at $n$ and on $D$, and $1$ elsewhere beyond $\sigma$. It extends $\sigma$ consistently, since the elements of $D$ below $|\sigma|$ are zeros of $\sigma$, a prefix of $G$. Then $D \subseteq Z_\tau$, so $n \in \Gamma(Z_\tau)$ and $\tau(n) = 0$: $\tau \in S$, a contradiction.
:::
::::

## Notes and references

:ref{#thm-cototal-null}, :ref{#cor-w2r-not-cototal} and :ref{#prop-omega-cototal} are due to Ang Li (2024), whose proof of the measure statement splits the class according to the predicted bit; the proof given here instead uses the measure-preserving flip of one bit. The results on introenumerability are also from Li's paper, building on Jockusch, Greenberg et al. and Goh et al.

- A. Li, *Introenumerability, autoreducibility, and randomness*, Journal of Symbolic Logic, published online 2023; arXiv:2402.08247.
- B. A. Trakhtenbrot, *On autoreducibility*, Doklady Akademii Nauk SSSR 192 (1970), 1224–1227.

:::::exercises
::::exercise{#ex-total-not-null-meaning difficulty=1 objective="Transfer the measure result from cototal to total sets."}
Show that the class of total sets is null.

:::solution
If $X$ is total, $\overline X \leq_e X$, so $\overline X$ is cototal: it is enumeration reducible to its complement $X$. The map $X \mapsto \overline X$ preserves the uniform measure and sends the total sets into the cototal sets, which form a null class by :ref{#thm-cototal-null}.
:::
::::

::::exercise{#ex-omega-complement-not-ce difficulty=1 objective="Use the cototality of Ω to show that its complement is not c.e."}
Show that $\overline \Omega$ is not c.e.

:::solution
If $\overline \Omega$ were c.e., then $\Omega \leq_e \overline \Omega$ (:ref{#prop-omega-cototal}) would make $\Omega$ c.e. (:ref{#prop-e-degrees-basic}), so $\Omega$ and its complement would both be c.e., and $\Omega$ would be computable, while it is random.
:::
::::

::::exercise{#ex-2-random-not-cototal difficulty=1 objective="Apply the measure result to stronger randomness notions."}
Show that no 2-random set is cototal.

:::solution
Every 2-random set is weakly 2-random (course on notions of randomness), so :ref{#cor-w2r-not-cototal} applies.
:::
::::

:::::
