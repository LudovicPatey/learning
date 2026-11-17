---
title: Weak 2-randomness
summary: Sequences avoiding every null Π⁰₂ class; 2-randomness implies weak 2-randomness, which implies Martin-Löf randomness, both strictly; no universal test; the theorem of Downey, Nies, Weber and Yu and of Hirschfeldt and Miller that a random sequence is weakly 2-random exactly when it computes no non-computable c.e. set.
duration: 35
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

::::exercise{#ex-w2r-downward difficulty=1 objective="Show with the characterization by computational weakness that weak 2-randomness is closed downward among random sequences."}
Let $Z$ be weakly 2-random and $Y \leq_T Z$ Martin-Löf random. Show that $Y$ is weakly 2-random.

:::solution
By :ref{#thm-dnwy} applied to $Z$, which is random by :ref{#prop-weak-2-position} (1), $Z$ computes no non-computable c.e. set. Neither does $Y$, since a set computed by $Y$ is computed by $Z$. As $Y$ is random, :ref{#thm-dnwy} shows that $Y$ is weakly 2-random. The hypothesis that $Y$ is random is needed: a weakly 2-random sequence computes non-random sequences, for instance the computable ones.
:::
::::

::::exercise{#ex-w2r-not-2-random difficulty=2 objective="Separate weak 2-randomness from 2-randomness with a computably dominated random sequence."}
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

:::::exercises
::::exercise{#ex-w2r-delta2-ce difficulty=1 objective="Apply Martin's theorem and the theorem of Downey, Nies, Weber and Yu to sequences computable in $\emptyset'$ and to 2-random sequences."}
Show that a weakly 2-random sequence is not computable in $\emptyset'$, and that a 2-random sequence computes no non-computable c.e. set.

:::solution
A set computable in $\emptyset'$ is $\Delta^0_2$, hence not weakly 2-random by :ref{#prop-weak-2-position} (2). A 2-random sequence is weakly 2-random and random, so by :ref{#thm-dnwy} it computes no non-computable c.e. set.
:::
::::

::::exercise[Generalized Martin-Löf tests]{#ex-generalized-tests difficulty=1 objective="Check that every null $\Pi^0_2$ class is given by a decreasing sequence of classes whose measures tend to $0$, and that without monotonicity the measures need not tend to $0$."}
Let $(\mathcal U_n)$ be uniformly $\Sigma^0_1$, and $\mathcal V_n = \mathcal U_0 \cap \cdots \cap \mathcal U_n$.

1. Show that $(\mathcal V_n)$ is a decreasing, uniformly $\Sigma^0_1$ sequence with $\bigcap_n \mathcal V_n = \bigcap_n \mathcal U_n$, and that $\bigcap_n \mathcal U_n$ is null if and only if $\lambda(\mathcal V_n)$ tends to $0$.
2. Give a uniformly $\Sigma^0_1$ sequence $(\mathcal U_n)$ with $\bigcap_n \mathcal U_n = \emptyset$ and $\lambda(\mathcal U_n) = \frac12$ for every $n$.

:::solution
1. If $\mathcal U = [W]^{\prec}$ and $\mathcal U' = [W']^{\prec}$ with $W$ and $W'$ c.e., then $\mathcal U \cap \mathcal U'$ is generated by the c.e. set of the strings $\tau$ such that $\tau = \sigma$ or $\tau = \sigma'$ for comparable $\sigma \in W$ and $\sigma' \in W'$, $\tau$ being the longer one: a sequence in both classes has a prefix in $W$ and a prefix in $W'$, which are comparable. An index of this set is computed from indices of $W$ and $W'$, so iterating gives the uniformity of $(\mathcal V_n)$. Clearly $\mathcal V_{n+1} \subseteq \mathcal V_n$, and a sequence belongs to every $\mathcal V_n$ if and only if it belongs to every $\mathcal U_n$. By continuity of the measure along a decreasing sequence, $\lambda(\bigcap_n \mathcal V_n) = \lim_n \lambda(\mathcal V_n)$, which gives the equivalence.
2. Let $\mathcal U_n = [0]$ for even $n$ and $\mathcal U_n = [1]$ for odd $n$. Each has measure $\frac12$, and $\bigcap_n \mathcal U_n \subseteq [0] \cap [1] = \emptyset$. Here $\mathcal V_n = \emptyset$ for $n \geq 1$.
:::
::::

::::exercise[Halves of a weakly 2-random sequence]{#ex-w2r-halves difficulty=1 objective="Pull back a null $\Pi^0_2$ class along the projection onto one half, and compare with the argument through van Lambalgen's theorem." lessons="relative-randomness"}
Show in two ways that if $A \oplus B$ is weakly 2-random, then $A$ and $B$ are weakly 2-random: directly from :ref{#def-weak-2-random}, and with :ref{#thm-van-lambalgen} and :ref{#ex-w2r-downward}. Show that the converse fails.

:::solution
*Directly.* Suppose that $A \in \bigcap_n \mathcal U_n$, with $(\mathcal U_n)$ uniformly $\Sigma^0_1$, decreasing, with $\lambda(\mathcal U_n) \to 0$ (:ref{#ex-generalized-tests}). Let $\mathcal U'_n = \{ X \oplus Y : X \in \mathcal U_n \}$. If $\mathcal U_n = [W_n]^{\prec}$, then $\mathcal U'_n$ is generated by the strings $\rho$ of length $2|\sigma|$ with $\rho(2i) = \sigma(i)$ for $i < |\sigma|$, for $\sigma \in W_n$; so the classes $\mathcal U'_n$ are uniformly $\Sigma^0_1$ and decreasing. The section of $\mathcal U'_n$ at $X$ is the whole space if $X \in \mathcal U_n$ and is empty otherwise, so $\lambda(\mathcal U'_n) = \lambda(\mathcal U_n)$ by :ref{#fact-fubini}. Hence $\bigcap_n \mathcal U'_n$ is a null $\Pi^0_2$ class, and it contains $A \oplus B$. The same argument with the odd positions applies to $B$.

*Through van Lambalgen's theorem.* A weakly 2-random sequence is random (:ref{#prop-weak-2-position} (1)), so $A$ is random and $B$ is random relative to $A$, hence random, by :ref{#thm-van-lambalgen}. Both are computable in $A \oplus B$, so they are weakly 2-random by :ref{#ex-w2r-downward}.

*The converse fails.* If $A$ is weakly 2-random, then $A \oplus A$ is not random, since $A$ is not random relative to $A$ (:ref{#ex-relative-random} (2) and :ref{#thm-van-lambalgen}); so it is not weakly 2-random.
:::
::::

::::exercise[Kurtz randomness relative to the jump]{#ex-w2r-kurtz-jump difficulty=2 objective="Express a $\Pi^0_1$ class relative to $\emptyset'$ as a $\Pi^0_2$ class, and deduce immunity properties of weakly 2-random sequences relative to the jump."}
A **$\Pi^0_1(\emptyset')$ class** is a class $[T]$ of the paths of a tree $T \subseteq \bstr$ computable in $\emptyset'$. A sequence is **Kurtz random relative to $\emptyset'$** if it belongs to no null $\Pi^0_1(\emptyset')$ class.

1. Show that every $\Pi^0_1(\emptyset')$ class is a $\Pi^0_2$ class. Deduce that every weakly 2-random sequence is Kurtz random relative to $\emptyset'$.
2. Let $B$ be an infinite $\Sigma^0_2$ set. Show that $\{ Z : B \subseteq Z \}$ is a null $\Pi^0_1(\emptyset')$ class. Deduce that neither a weakly 2-random sequence nor its complement contains an infinite $\Sigma^0_2$ set.

:::solution
1. Let $T$ be computable in $\emptyset'$. Then $T$ and its complement are c.e. in $\emptyset'$, hence $\Sigma^0_2$ by Post's theorem, so $T$ is $\Pi^0_2$: there is a computable relation $R$ with $\sigma \in T \iff \forall a\, \exists b\, R(\sigma, a, b)$. For $n$ and $a$, let $\mathcal V_{n, a}$ be the class generated by the strings $\sigma$ of length $n$ such that $\exists b\, R(\sigma, a, b)$; these sets of strings are c.e., uniformly in $(n, a)$, so the classes $\mathcal V_{n,a}$ are uniformly $\Sigma^0_1$. A sequence $X$ belongs to every $\mathcal V_{n,a}$ if and only if $\forall n\, \forall a\, \exists b\, R(X \uh n, a, b)$, that is, $X \uh n \in T$ for every $n$, that is, $X \in [T]$. So $[T] = \bigcap_{n, a} \mathcal V_{n,a}$ is $\Pi^0_2$. A weakly 2-random sequence avoids every null $\Pi^0_2$ class, in particular every null $\Pi^0_1(\emptyset')$ class.
2. The set $B$ is c.e. in $\emptyset'$ and infinite, so it is the range of an injective function $k \mapsto b_k$ computable in $\emptyset'$. Let $T$ be the set of the strings $\sigma$ such that $\sigma(b_k) = 1$ for every $k < |\sigma|$ with $b_k < |\sigma|$. It is a tree, computable in $\emptyset'$. If $B \subseteq Z$, every prefix of $Z$ is in $T$. Conversely, if $Z \in [T]$ and $k \in \nat$, the prefix of $Z$ of length $\max(k, b_k) + 1$ is in $T$, so $Z(b_k) = 1$; hence $B \subseteq Z$. So $\{ Z : B \subseteq Z \} = [T]$. For every $k$, this class is contained in the clopen class of the sequences equal to $1$ at the $k$ distinct positions $b_0, \dots, b_{k-1}$, of measure $2^{-k}$; so it is null. The same holds for $\{ Z : B \cap Z = \emptyset \}$, with $0$ in place of $1$. By (1), a weakly 2-random sequence $Z$ belongs to neither class, so $B \not\subseteq Z$ and $B \not\subseteq \nat \setminus Z$.

The converse of (1) fails, as explained after :ref{#prop-weak-2-position}. Both statements are Nies (2009), remarks before Exercise 3.6.6 and Exercise 3.6.7.
:::
::::

::::exercise[Computably dominated members of Π⁰₁ classes]{#ex-w2r-pi01-dominated difficulty=1 objective="Combine the computably dominated basis theorem with a $\Pi^0_1$ class of random sequences to place weakly 2-random sequences in every $\Pi^0_1$ class of positive measure."}
Let $\mathcal Q$ be a $\Pi^0_1$ class of positive measure. Show that $\mathcal Q$ contains a computably dominated weakly 2-random sequence.

:::solution
Let $(\mathcal U_n)$ be a universal Martin-Löf test and $\mathcal P_n = \cs \setminus \mathcal U_n$, a $\Pi^0_1$ class of random sequences of measure at least $1 - 2^{-n}$ (:ref{#cor-mlr-structure} (2)). Choose $n$ with $2^{-n} < \lambda(\mathcal Q)$. The class $\mathcal Q \cap \mathcal P_n$ is $\Pi^0_1$, as the class of paths of the intersection of two computable trees, and $\lambda(\mathcal Q \cap \mathcal P_n) \geq \lambda(\mathcal Q) - 2^{-n} > 0$; so it is non-empty. By the computably dominated basis theorem (:ref{#thm-dominated-basis}), it has a computably dominated member $Z$. It is random, as a member of $\mathcal P_n$, and computably dominated, so it is weakly 2-random by the argument of :ref{#ex-w2r-not-2-random}.
:::
::::

::::exercise[Weak 2-randomness is not a Σ⁰₂ property]{#ex-w2r-not-sigma2 difficulty=2 objective="Use leftmost paths of $\Pi^0_1$ classes of random sequences to strengthen the absence of a universal test, and contrast weak 2-randomness with Martin-Löf randomness."}
1. Show that for every null $\Pi^0_2$ class $\mathcal C$, there is a $\Delta^0_2$ Martin-Löf random sequence outside $\mathcal C$.
2. A **$\Sigma^0_2$ class** is a union of a uniform sequence of $\Pi^0_1$ classes. Show that the class of weakly 2-random sequences contains no non-empty $\Pi^0_1$ class and is not a $\Sigma^0_2$ class, although the class of Martin-Löf random sequences is $\Sigma^0_2$ (:ref{#cor-mlr-structure} (2)).

:::solution
1. Write $\mathcal C = \bigcap_n \mathcal V_n$ with $(\mathcal V_n)$ decreasing and $\lambda(\mathcal V_n) \to 0$ (:ref{#ex-generalized-tests}), and choose $n$ with $\lambda(\mathcal V_n) < \frac12$. Let $\mathcal P_1$ be the $\Pi^0_1$ class of random sequences of :ref{#cor-mlr-structure} (2), of measure at least $\frac12$. The class $\mathcal P_1 \setminus \mathcal V_n$ is $\Pi^0_1$, as the intersection of two $\Pi^0_1$ classes, and its measure is at least $\lambda(\mathcal P_1) - \lambda(\mathcal V_n) > \frac12 - \frac12 = 0$. So it is non-empty, and its leftmost member $Z$ is $\Delta^0_2$, as in the proof of :ref{#prop-weak-2-position} (3). It is random, and $Z \notin \mathcal V_n \supseteq \mathcal C$.
2. The leftmost member of a non-empty $\Pi^0_1$ class is $\Delta^0_2$, hence not weakly 2-random (:ref{#prop-weak-2-position} (2)); so no non-empty $\Pi^0_1$ class consists of weakly 2-random sequences. There are countably many $\Pi^0_2$ classes, so the sequences that are not weakly 2-random form a countable union of null classes, and the class of weakly 2-random sequences is conull. If it were the union of $\Pi^0_1$ classes $\mathcal Q_0, \mathcal Q_1, \dots$, one of them would have positive measure, hence be non-empty, and it would consist of weakly 2-random sequences, a contradiction.

Part (2) follows the proof of Downey–Hirschfeldt, Corollary 7.2.10.
:::
::::

::::exercise[Weak 3-randomness implies 2-randomness]{#ex-weak-3-random difficulty=2 objective="Compute the complexity of a Martin-Löf test relative to $\emptyset'$, and place 2-randomness below weak 3-randomness."}
A **$\Sigma^0_2$ class** is a union $\bigcup_k \mathcal Q_k$ of a uniform sequence of $\Pi^0_1$ classes, and a **$\Pi^0_3$ class** is an intersection $\bigcap_n \mathcal S_n$ of a uniform sequence of $\Sigma^0_2$ classes. A sequence is **weakly 3-random** if it belongs to no null $\Pi^0_3$ class. Show that every weakly 3-random sequence is 2-random.

:::solution
Let $Z$ be a sequence that is not 2-random, captured by a Martin-Löf test $(\mathcal U_n)$ relative to $\emptyset'$, with $\mathcal U_n = [W_n]^{\prec}$ for sets $W_n$ c.e. in $\emptyset'$ uniformly in $n$. By Post's theorem, the relation $\sigma \in W_n$ is $\Sigma^0_2$: there is a computable relation $R$ with $\sigma \in W_n \iff \exists a\, \forall b\, R(n, \sigma, a, b)$. For $n$, $\sigma$ and $a$, let $\mathcal Q_{n, \sigma, a}$ be the class of the paths of the computable tree of the strings $\rho$ comparable with $\sigma$ such that $R(n, \sigma, a, b)$ holds for every $b < |\rho|$. If $\forall b\, R(n, \sigma, a, b)$ holds, this class is $[\sigma]$; otherwise the tree is finite and the class is empty. These classes are uniformly $\Pi^0_1$, and $\mathcal U_n = \bigcup_{\sigma, a} \mathcal Q_{n, \sigma, a}$. So the classes $\mathcal U_n$ are uniformly $\Sigma^0_2$, and $\bigcap_n \mathcal U_n$ is a $\Pi^0_3$ class. It is null, since $\lambda(\mathcal U_n) \leq 2^{-n}$, and it contains $Z$. So $Z$ is not weakly 3-random.

This is the case $n = 2$ of Kurtz's theorem that every weakly $(n+1)$-random sequence is $n$-random (Downey–Hirschfeldt, Theorem 7.2.7); the case $n = 1$ is :ref{#prop-weak-2-position} (1).
:::
::::

::::exercise[The theorem of Hirschfeldt and Miller]{#ex-hirschfeldt-miller difficulty=3 objective="Adapt the construction of the Downey–Nies–Weber–Yu theorem to countably many null $\Pi^0_2$ classes at once, with a single c.e. set."}
Let $(\mathcal U_{i,n})_{i, n \in \nat}$ be uniformly $\Sigma^0_1$ classes such that, for each $i$, the class $\mathcal C_i = \bigcap_n \mathcal U_{i,n}$ is null.

1. Show that there is a non-computable c.e. set $A$ computable in every Martin-Löf random member of $\bigcup_i \mathcal C_i$.
2. Deduce that the set $A$ built in the proof of (1 ⇒ 2) in :ref{#thm-dnwy} is computable in every random member of the class $\bigcap_n \mathcal U_n$, and that for finitely many random sequences $Z_1, \dots, Z_k$ that are not weakly 2-random, there is a single non-computable c.e. set computable in each of them.

:::solution
1. Replacing $\mathcal U_{i,n}$ by $\mathcal U_{i,0} \cap \cdots \cap \mathcal U_{i,n}$, uniformly in $(i, n)$ (:ref{#ex-generalized-tests}), we may assume that each sequence $(\mathcal U_{i,n})_n$ is decreasing, so that $\lambda(\mathcal U_{i,n}) \to 0$ as $n \to \infty$. Let $\mathcal U_{i,n,t}$ be the clopen approximation of $\mathcal U_{i,n}$ at stage $t$, increasing with $t$. We enumerate $A$, with $A_t$ the set of the elements enumerated before stage $t$, together with classes $\mathcal V_e$. At stage $t$, for each $e \leq t$ such that $e$ has not acted and $W_{e,t} \cap A_t = \emptyset$, if there is $n \in W_{e,t}$ with $n > 2e$ and $\lambda(\bigcup_{i \leq e} \mathcal U_{i,n,t}) < 2^{-e}$, then $e$ **acts**: it enumerates the least such $n$ into $A$, and $\mathcal V_e = \bigcup_{i \leq e} \mathcal U_{i,n,t}$. If $e$ never acts, $\mathcal V_e = \emptyset$.

*$A$ is simple.* Each $e$ enumerates at most one element, larger than $2e$; so at most $k$ elements of $A$ are at most $2k$, and the complement of $A$ is infinite. Let $W_e$ be infinite. For each $i \leq e$, $\lambda(\mathcal U_{i,n}) \to 0$, so $\lambda(\bigcup_{i \leq e} \mathcal U_{i,n}) \leq \sum_{i \leq e} \lambda(\mathcal U_{i,n})$ tends to $0$, and there is $n \in W_e$ with $n > 2e$ and $\lambda(\bigcup_{i \leq e} \mathcal U_{i,n}) < 2^{-e}$; the same bound holds for the approximations at every stage. At a stage $t \geq e$ with $n \in W_{e,t}$, either $W_{e,t}$ meets $A_t$, or $e$ has acted, enumerating an element of $W_e$, or $e$ acts at $t$. In each case $A \cap W_e \neq \emptyset$. A simple set is not computable, since its complement would be an infinite c.e. set disjoint from it.

*$A$ is computable in every random $Z \in \bigcup_i \mathcal C_i$.* The classes $\mathcal V_e$ are clopen, uniformly c.e. in $e$, with $\sum_e \lambda(\mathcal V_e) \leq \sum_e 2^{-e} = 2$: a Solovay test. Let $Z$ be random with $Z \in \mathcal C_i$. By :ref{#thm-solovay}, $Z$ belongs to finitely many $\mathcal V_e$ only. Let $m$ exceed the elements enumerated by the indices $e < i$ and the elements enumerated by the indices $e$ with $Z \in \mathcal V_e$; there are finitely many of them. Let $n \geq m$ enter $A$ at stage $t$, for the index $e$. Then $e \geq i$ and $Z \notin \mathcal V_e \supseteq \mathcal U_{i,n,t}$, so $Z \notin \mathcal U_{i,n,t}$. To decide whether $n \geq m$ belongs to $A$, search for the least $t$ with $Z \in \mathcal U_{i,n,t}$, which exists since $Z \in \mathcal U_{i,n}$. If $n$ entered $A$ at a stage $t' \geq t$, then $Z \in \mathcal U_{i,n,t} \subseteq \mathcal U_{i,n,t'}$, which is impossible; so $n \in A$ if and only if $n \in A_t$. With the finite set $A \cap \{0, \dots, m-1\}$, this computes $A$ from $Z$.

2. If $\mathcal U_{i,n} = \mathcal U_n$ for every $i$, with $(\mathcal U_n)$ decreasing, then $\bigcup_{i \leq e} \mathcal U_{i,n,t} = \mathcal U_{n,t}$, and the construction above is that of the proof of :ref{#thm-dnwy}; the set $A$ does not depend on $Z$, and (1) shows that every random member of $\bigcap_n \mathcal U_n$ computes it. For $Z_1, \dots, Z_k$, choose null $\Pi^0_2$ classes $\bigcap_n \mathcal U_{j,n}$ containing $Z_j$, for $1 \leq j \leq k$, and let $\mathcal U_{i,n} = \mathcal U_{k,n}$ for $i > k$ and $\mathcal U_{0,n} = \mathcal U_{1,n}$; this is a uniform family, and (1) gives the set.

The union $\bigcup_i \mathcal C_i$ is a null $\Sigma^0_3$ class, and every null $\Sigma^0_3$ class has this form: (1) is the theorem of Hirschfeldt and Miller quoted after the proof of :ref{#thm-dnwy} (Downey–Hirschfeldt, Theorem 7.2.11, where the construction is organized differently).
:::
::::
:::::
