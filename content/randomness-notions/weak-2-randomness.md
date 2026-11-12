---
title: Weak 2-randomness
summary: Sequences avoiding every null Π⁰₂ class; 2-randomness implies weak 2-randomness, which implies Martin-Löf randomness, both strictly; no universal test; the theorem of Downey, Nies, Weber and Yu and of Hirschfeldt and Miller that a random sequence is weakly 2-random exactly when it computes no non-computable c.e. set.
duration: 45
prerequisites: [relative-randomness, martin-lof-randomness/upper-cones, martingales/randomness-hierarchy]
---

A Martin-Löf test describes a null $\Pi^0_2$ class $\bigcap_n \mathcal U_n$ whose measures converge to $0$ at a computable rate. Dropping the condition on the rate gives a stronger notion: a sequence is **weakly 2-random** if it avoids every null $\Pi^0_2$ class. The notion lies strictly between Martin-Löf randomness and 2-randomness. It has a characterization in terms of computational power: a random sequence is weakly 2-random exactly when it computes no non-computable c.e. set. Random sequences that are not weakly 2-random, such as $\Omega$, are thus exactly those that carry information about the halting problem.

## Definition and position

:::definition{#def-weak-2-random}
A sequence is **weakly 2-random** if it belongs to no null $\Pi^0_2$ class, that is, to no class $\bigcap_n \mathcal U_n$ with $(\mathcal U_n)$ uniformly $\Sigma^0_1$ and $\lambda(\bigcap_n \mathcal U_n) = 0$.
:::

Replacing $\mathcal U_n$ by $\mathcal U_0 \cap \cdots \cap \mathcal U_n$, one may assume the classes decreasing, so that $\lambda(\mathcal U_n)$ tends to $0$; such a sequence of classes is called a **generalized Martin-Löf test**. The name comes from Kurtz, who called a sequence **weakly $n$-random** if it belongs to every $\Sigma^0_n$ class of measure $1$. For $n = 1$, these are the Kurtz random sequences, which avoid every null $\Pi^0_1$ class; for $n = 2$, passing to complements gives the definition above.

:::example{#ex-null-pi02}
1. If $(\mathcal U_n)$ is a Martin-Löf test, $\bigcap_n \mathcal U_n$ is a null $\Pi^0_2$ class.
2. If $A$ is computable, $\{ A \}$ is a null $\Pi^0_1$ class, hence $\Pi^0_2$. More generally, for every $\Delta^0_2$ set $A$, the class $\{ A \}$ is $\Pi^0_2$: this is shown in :ref{#prop-weak-2-position} (2) below.
3. For a reduction $\Phi$ and a non-computable $\Delta^0_2$ set $A$, the class $\{ X : \Phi^X = A \}$ is a null $\Pi^0_2$ class: this is used in :ref{#thm-dnwy}. Its measure is $0$ by Sacks's theorem. It need not be contained in a Martin-Löf test: if $\Phi^\Omega = \emptyset'$, the class for $A = \emptyset'$ contains the random sequence $\Omega$.
:::

:::proposition{#prop-weak-2-position}
1. Every 2-random sequence is weakly 2-random, and every weakly 2-random sequence is Martin-Löf random.
2. No $\Delta^0_2$ sequence is weakly 2-random. In particular $\Omega$ is random but not weakly 2-random.
3. There is no universal test for weak 2-randomness: no single null $\Pi^0_2$ class contains every sequence that is not weakly 2-random.
:::

:::proof{of=prop-weak-2-position}
1. A Martin-Löf test describes a null $\Pi^0_2$ class. Let $\bigcap_n \mathcal U_n$ be null, with decreasing $\mathcal U_n$. The relation $\lambda(\mathcal U_n) \leq 2^{-k}$ is $\Pi^0_1$, since $\lambda(\mathcal U_n)$ is left-c.e. uniformly in $n$; so $\emptyset'$ computes, for each $k$, the least $n_k$ with $\lambda(\mathcal U_{n_k}) \leq 2^{-k}$, which exists since $\lambda(\mathcal U_n)$ tends to $0$. The classes $\mathcal U_{n_k}$ form a Martin-Löf test relative to $\emptyset'$ containing $\bigcap_n \mathcal U_n$.
2. Let $A = \lim_s A_s$ with $(A_s)$ computable. The classes $\mathcal U_{\langle n, t \rangle} = \bigcup_{s > t} [A_s \uh n]$ are uniformly $\Sigma^0_1$, and their intersection is $\{ A \}$: a sequence $X$ in all of them agrees, for every $n$, with $A_s \uh n$ for infinitely many $s$, hence with $A \uh n$. This is a null $\Pi^0_2$ class containing $A$.
3. Let $\bigcap_n \mathcal U_n$ be null. Some $\mathcal U_n$ has measure less than $1$, so its complement is a non-empty $\Pi^0_1$ class, whose leftmost member is $\Delta^0_2$. By (2), it is not weakly 2-random, yet it is outside $\bigcap_n \mathcal U_n$.
:::

The proof of (1) shows what is lost when the rate of convergence is dropped: $\emptyset'$ can find, for each $k$, a component of measure at most $2^{-k}$, but no computable procedure can. Statement (2), due to Martin, uses the opposite phenomenon. A $\Delta^0_2$ set is described by its approximations, and the class $\{ A \}$ is $\Pi^0_2$, but the stage after which $A_s \uh n$ is correct is not computable, so the measures of the classes $\mathcal U_{\langle n, t \rangle}$ do not tend to $0$ at a computable rate. Statement (3), due to Downey, Nies, Weber and Yu, contrasts with the existence of a universal Martin-Löf test.

:::quiz[the position of weak 2-randomness]
In the proof of :ref{#prop-weak-2-position} (2), why does a sequence $X$ in every class $\mathcal U_{\langle n, t \rangle}$ agree with $A$?

- [x] For each $n$, $X \uh n = A_s \uh n$ for some $s > t$, for every $t$; since $A_s \uh n = A \uh n$ for all large $s$, this gives $X \uh n = A \uh n$.
- [ ] Because the classes $\mathcal U_{\langle n, t \rangle}$ have measure tending to $0$.

  Nullness is a consequence: the intersection is a single point. The agreement comes from the fact that the approximation settles on each prefix.
- [ ] Because $A$ is c.e.

  Only the convergence of the approximation is used; $A$ is an arbitrary $\Delta^0_2$ set.
:::

Weak 2-randomness is not Kurtz randomness relative to $\emptyset'$, although both strengthen Kurtz randomness by one quantifier. A sequence that meets every dense set of strings c.e. in $\emptyset'$ is Kurtz random relative to $\emptyset'$, by the relativization of :ref{#ex-kurtz}; such sequences exist, built by finite extensions with oracle $\emptyset''$. Such a sequence is in particular weakly 1-generic, so it is not Schnorr random (:ref{#prop-kurtz-not-schnorr}), and a fortiori not weakly 2-random.

## The Downey–Nies–Weber–Yu theorem

:::theorem[Downey, Nies, Weber, Yu; Hirschfeldt, Miller]{#thm-dnwy}
For a Martin-Löf random sequence $Z$, the following are equivalent:

1. $Z$ is not weakly 2-random;
2. $Z$ computes a non-computable c.e. set;
3. $Z$ computes a non-computable $\Delta^0_2$ set.
:::

The direction (3 ⇒ 1) is a measure argument: the oracles that compute a given non-computable $\Delta^0_2$ set form a null $\Pi^0_2$ class. The direction (1 ⇒ 2) is a construction. Given a null $\Pi^0_2$ class containing $Z$, we enumerate a simple set $A$, and we make $Z$ able to decide $A$ by allowing a number $n$ to enter $A$ only at a stage where $Z$ is not yet in the $n$-th component. Then $Z$ decides whether $n \in A$ by waiting until it enters the $n$-th component. This fails when $n$ enters $A$ after $Z$ has entered the component; to make this rare, each enumeration is charged with the measure of the current approximation of the component, and the charges form a Solovay test, which the random sequence $Z$ fails only finitely often.

:::proof{of=thm-dnwy}
(2 ⇒ 3) Every c.e. set is $\Delta^0_2$.

(3 ⇒ 1) Let $A = \lim_s A_s$ be non-computable and $\Delta^0_2$, with $\Phi^Z = A$. The classes $\mathcal U_{\langle n, t \rangle} = \bigcup_{s > t} \{ X : \Phi^X \uh n = A_s \uh n \}$ are uniformly $\Sigma^0_1$, and, as in :ref{#prop-weak-2-position} (2), their intersection is $\{ X : \Phi^X = A \}$, which is null by Sacks's theorem (:ref{#thm-sacks}). It contains $Z$.

(1 ⇒ 2) Let $Z \in \bigcap_n \mathcal U_n$, a null $\Pi^0_2$ class with decreasing $\mathcal U_n$, and let $\mathcal U_{n,t}$ be the clopen approximation of $\mathcal U_n$ at stage $t$, generated by the strings enumerated by stage $t$; it increases with $t$, and $\mathcal U_n = \bigcup_t \mathcal U_{n,t}$. We enumerate a set $A$, together with classes $\mathcal V_e$. At stage $t$, for each $e \leq t$ such that no element has been enumerated for $e$ and $W_{e,t} \cap A_t = \emptyset$, if there is $n \in W_{e,t}$ with $n > 2e$ and $\lambda(\mathcal U_{n,t}) < 2^{-e}$, enumerate the least such $n$ into $A$, and let $\mathcal V_e = \mathcal U_{n,t}$. If $e$ never acts, $\mathcal V_e = \emptyset$.

*$A$ is simple, hence not computable.* Each $e$ enumerates at most one element, larger than $2e$, so $A$ has infinite complement. If $W_e$ is infinite, it contains $n > 2e$ with $\lambda(\mathcal U_n) < 2^{-e}$, since these measures tend to $0$, and then $\lambda(\mathcal U_{n,t}) < 2^{-e}$ for every $t$. At every stage $t \geq e$ with $n \in W_{e,t}$, either $W_{e,t}$ already meets $A_t$, or $e$ has already acted, or $e$ acts; in each case $A$ meets $W_e$ (when $e$ acts, it enumerates an element of $W_{e,t}$).

*$Z$ computes $A$.* The classes $\mathcal V_e$ are clopen, uniformly c.e. in $e$, with $\lambda(\mathcal V_e) < 2^{-e}$: a Solovay test. Since $Z$ is random, $Z$ belongs to $\mathcal V_e$ for finitely many $e$ only (:ref{#thm-solovay}), and these $e$ enumerate finitely many elements. Let $m$ exceed them. For $n \geq m$, if $n$ enters $A$ at stage $t$, then $Z \notin \mathcal U_{n,t}$. To decide whether $n \geq m$ belongs to $A$, search for the least stage $t$ with $Z \in \mathcal U_{n,t}$, which exists since $Z \in \mathcal U_n$; then $n \in A$ if and only if $n \in A_t$, since $\mathcal U_{n,t}$ increases with $t$.
:::

The construction makes the enumeration of $n$ into $A$ costly for $Z$: it can only happen while $Z$ is still outside $\mathcal U_n$, and the Solovay test charges each such enumeration with the measure of the current approximation. The same idea, charging each enumeration with a measure, underlies the **cost functions** used to build K-trivial sets. The requirements and the condition $n > 2e$ are those of Post's simple set; the added condition $\lambda(\mathcal U_{n,t}) < 2^{-e}$ keeps the total charge finite, and it is met by some element of every infinite $W_e$ because the measures tend to $0$, at whatever rate.

:::quiz[the DNWY theorem]
In (1 ⇒ 2) of :ref{#thm-dnwy}, why does $Z$ belong to only finitely many classes $\mathcal V_e$?

- [x] Because they form a Solovay test, with $\lambda(\mathcal V_e) < 2^{-e}$, and $Z$ is Martin-Löf random.
- [ ] Because $Z$ belongs to every $\mathcal U_n$.

  This is why $Z$ eventually enters each $\mathcal U_n$; finiteness comes from the Solovay test.
- [ ] Because $A$ is simple.

  Simplicity concerns the complement of $A$; the classes $\mathcal V_e$ are controlled by measure.

---

Why does the search for the least $t$ with $Z \in \mathcal U_{n,t}$ terminate?

- [x] Because $Z$ belongs to the open class $\mathcal U_n$, so some prefix of $Z$ is enumerated into it at a finite stage.
- [ ] Because $\mathcal U_n$ has positive measure.

  Positive measure does not imply that $Z$ belongs to it; the hypothesis $Z \in \bigcap_n \mathcal U_n$ does.
- [ ] Because $n \in A$.

  The search is used to decide whether $n \in A$; it terminates in both cases.

---

Where is the randomness of $Z$ used in (3 ⇒ 1)?

- [x] It is not used: every sequence that computes a non-computable $\Delta^0_2$ set lies in a null $\Pi^0_2$ class. Randomness is needed only in (1 ⇒ 2).
- [ ] To apply Sacks's theorem.

  Sacks's theorem bounds the measure of the class $\{ X : \Phi^X = A \}$; it does not concern $Z$.
- [ ] To show that the classes $\mathcal U_{\langle n, t \rangle}$ are $\Sigma^0_1$.

  They are $\Sigma^0_1$ because $\Phi$ is a reduction and $(A_s)$ is computable.
:::

Item (3) says that, for random sequences, weak 2-randomness amounts to forming a **minimal pair** with $\emptyset'$: every set computable both in $Z$ and in $\emptyset'$ is computable. Downey, Nies, Weber and Yu proved (3 ⇒ 1) in this form, for every weakly 2-random sequence, with a majority vote argument in place of Sacks's theorem. Hirschfeldt and Miller proved (1 ⇒ 2) in a stronger form: for every null $\Sigma^0_3$ class, there is a single non-computable c.e. set computed by all its random members. The hypothesis that $Z$ is random cannot be dropped in (1 ⇒ 2): a non-computable computably dominated sequence that is not random, such as a computably dominated completion of Peano arithmetic, is not weakly 2-random, yet computes no non-computable c.e. set, since such a set is not computably dominated.

## Exercises

::::exercise{difficulty=1}
Show that a weakly 2-random sequence is not computable in $\emptyset'$, and that a 2-random sequence computes no non-computable c.e. set.

:::solution
A set computable in $\emptyset'$ is $\Delta^0_2$, hence not weakly 2-random by :ref{#prop-weak-2-position} (2). A 2-random sequence is weakly 2-random and random, so by :ref{#thm-dnwy} it computes no non-computable c.e. set.
:::
::::

::::exercise{difficulty=1}
Let $Z$ be weakly 2-random and $Y \leq_T Z$ Martin-Löf random. Show that $Y$ is weakly 2-random.

:::solution
By :ref{#thm-dnwy} applied to $Z$, which is random by :ref{#prop-weak-2-position} (1), $Z$ computes no non-computable c.e. set. Neither does $Y$, since a set computed by $Y$ is computed by $Z$. As $Y$ is random, :ref{#thm-dnwy} shows that $Y$ is weakly 2-random. The hypothesis that $Y$ is random is needed: a weakly 2-random sequence computes non-random sequences, for instance the computable ones.
:::
::::

::::exercise{difficulty=2}
Show that there is a weakly 2-random sequence that is not 2-random.

:::solution
By :ref{#cor-mlr-structure} (3), there is a random sequence $Z$ that is computably dominated. It computes no non-computable c.e. set $A$: the settling function $m(x) = \min \{ s : A_s \cap \{0, \dots, x\} = A \cap \{0, \dots, x\} \}$ is computable in $A$, hence in $Z$, so there are a computable function $g$ and a number $x_0$ with $m(x) \leq g(x)$ for $x \geq x_0$. Then $x \in A \iff x \in A_{g(x)}$ for $x \geq x_0$, which makes $A$ computable. By :ref{#thm-dnwy}, $Z$ is weakly 2-random. By Kurtz's theorem, every 2-random sequence has hyperimmune degree, that is, is not computably dominated; so $Z$ is not 2-random. Kurtz's theorem is admitted, as stated in the previous lesson.
:::
::::

## Notes and references

Weak 2-randomness appears in Kurtz's thesis (1981), as the case $n = 2$ of weak $n$-randomness, and in print in Gaifman and Snir (1982); Martin's proof that no $\Delta^0_2$ set is weakly 2-random is in Solovay's unpublished notes (Downey–Hirschfeldt, Corollary 7.2.9). Downey, Nies, Weber and Yu (2006) proved that weakly 2-random sequences form a minimal pair with $\emptyset'$ and that there is no universal generalized Martin-Löf test; Hirschfeldt and Miller proved the converse for random sequences, published in the same paper (Downey–Hirschfeldt, Theorems 7.2.8 and 7.2.11, Corollaries 7.2.10 and 7.2.12; Nies, Section 3.6). The proof of (1 ⇒ 2) given here is the special case of a single null $\Pi^0_2$ class of Hirschfeldt and Miller's proof.

- H. Gaifman and M. Snir, *Probabilities over rich languages, testing and randomness*, Journal of Symbolic Logic 47 (1982), 495–548.
- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana–Champaign, 1981.
- R. Downey, A. Nies, R. Weber and L. Yu, *Lowness and Π⁰₂ nullsets*, Journal of Symbolic Logic 71 (2006), 1044–1052.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 7.2.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 3.6.
