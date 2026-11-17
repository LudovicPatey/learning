---
title: Kurtz randomness and computable domination
summary: The hierarchy of randomness notions from 2-randomness to Kurtz randomness; on computably dominated sequences, Kurtz randomness implies weak 2-randomness; every set of hyperimmune degree computes a Kurtz random sequence that is not Schnorr random; computable domination is the dividing line for Kurtz randomness, as highness is for Schnorr randomness.
duration: 30
prerequisites: [weak-2-randomness, martingales/randomness-hierarchy, cohen-genericity/weak-genericity, immunity-growth/immune-sets]
---

The course on martingales placed Martin-Löf, computable, Schnorr and Kurtz randomness in a strict hierarchy, and showed, following Nies, Stephan and Terwijn, that the first three coincide on sequences that are not high. The previous lessons added two notions above Martin-Löf randomness. This lesson completes the picture at the bottom of the hierarchy. Kurtz randomness, the weakest notion, collapses onto weak 2-randomness on computably dominated sequences, and every set of hyperimmune degree computes a Kurtz random sequence that is not even Schnorr random. So the line that separates Kurtz randomness from the stronger notions is computable domination, as highness is the line for Schnorr randomness.

## The notions and their order

For reference, we gather the two weakest notions, defined in the courses on Martin-Löf randomness and on martingales.

:::definition{#def-schnorr-kurtz}
1. A sequence is **Kurtz random**, or **weakly random**, if it belongs to no null $\Pi^0_1$ class (:ref{#ex-kurtz}).
2. A **Schnorr test** is a Martin-Löf test $(\mathcal U_n)$ such that the reals $\lambda(\mathcal U_n)$ are computable, uniformly in $n$ (:ref{#def-schnorr-test}). A sequence is **Schnorr random** if it passes every Schnorr test; by :ref{#thm-schnorr-tests-martingales}, this is equivalent to the definition of :ref{#def-schnorr-random}, by computable martingales that succeed at a computable rate.
:::

For example, a sequence $X$ with $X(2^k) = 0$ for every $k$ is not Kurtz random, since it belongs to the null $\Pi^0_1$ class of the sequences that vanish at every power of $2$ (:ref{#ex-kurtz-powers}). A sequence in which the frequency of ones tends to $\frac34$ is not Schnorr random, by the law of large numbers below.

:::proposition{#prop-notions-implications}
Every weakly 2-random sequence is Martin-Löf random; every Martin-Löf random sequence is computably random; every computably random sequence is Schnorr random; every Schnorr random sequence is Kurtz random.
:::

:::proof{of=prop-notions-implications}
The first implication is :ref{#prop-weak-2-position} (1), and the other three are :ref{#prop-hierarchy}.
:::

Schnorr random sequences satisfy the law of large numbers: the proportional betting strategy succeeds at an exponential rate along every sequence in which the frequency of ones exceeds $\frac12 + \delta$ infinitely often (:ref{#ex-schnorr-success} (1)). Kurtz random sequences need not satisfy it.

:::proposition{#prop-generic-kurtz}
Every weakly 1-generic sequence is Kurtz random, and no weakly 1-generic sequence is Schnorr random.
:::

:::proof{of=prop-generic-kurtz}
This is :ref{#prop-kurtz-not-schnorr}: a weakly 1-generic sequence avoids every null $\Pi^0_1$ class (:ref{#ex-kurtz}), and it has frequency of ones at least $\frac23$ at infinitely many lengths, so it fails the law of large numbers.
:::

Kurtz randomness is thus compatible with genericity, a notion of typicality in the sense of category rather than measure. A null $\Pi^0_1$ class is closed with empty interior, hence nowhere dense, so a sequence that is typical in the sense of category avoids it; a $\Sigma^0_1$ class of small measure, on the other hand, can be dense, and generic sequences meet it.

::::exercise{#ex-kurtz-bi-immune difficulty=1 objective="Use null $\Pi^0_1$ classes defined from c.e. sets to show that Kurtz random sequences are bi-immune."}
A set is **bi-immune** if neither it nor its complement contains an infinite c.e. set. Show that every Kurtz random sequence is bi-immune (Jockusch).

:::solution
Let $W$ be an infinite c.e. set. The class $\mathcal P = \{ X : \forall n \in W\ X(n) = 1 \}$ is $\Pi^0_1$: a sequence leaves it as soon as a bit $X(n) = 0$ is seen at some $n$ enumerated into $W$. For every $k$, $W$ has $k$ elements, and the sequences equal to $1$ at these positions form a class of measure $2^{-k}$; so $\mathcal P$ is null. A Kurtz random sequence $Z$ is not in $\mathcal P$, so $W \not\subseteq Z$. The class $\{ X : \forall n \in W\ X(n) = 0 \}$ shows in the same way that $W$ is not contained in the complement of $Z$.
:::
::::

:::figure[The six notions of randomness of the course, with the reason why each implication is strict. Martin-Löf, computable and Schnorr randomness coincide on sequences that are not high (:ref{#thm-nst-nonhigh}); the five notions from weak 2-randomness to Kurtz randomness coincide on computably dominated sequences (:ref{#cor-dominated-collapse}), on which 2-randomness never holds.]{#fig-notions-map}
<svg class="fig" viewBox="0 0 600 410" width="600" role="img" aria-label="Six notions of randomness from top to bottom: 2-random, weakly 2-random, Martin-Löf random, computably random, Schnorr random, Kurtz random, joined by implication arrows with the reason why each implication is strict. A bracket on the left marks that Martin-Löf, computable and Schnorr randomness coincide on sequences that are not high; a bracket on the right marks that weak 2-randomness and the four notions below it coincide on computably dominated sequences, where 2-randomness never holds"><defs><marker id="rn-map-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="150" y="14" width="230" height="42" rx="4" class="cell"/><text x="162" y="32" font-size="13">2-random</text><text x="162" y="48" class="label">Martin-Löf random relative to ∅′</text><rect x="150" y="82" width="230" height="42" rx="4" class="cell"/><text x="162" y="100" font-size="13">weakly 2-random</text><text x="162" y="116" class="label">in no null Π⁰₂ class</text><rect x="150" y="150" width="230" height="42" rx="4" class="cell"/><text x="162" y="168" font-size="13">Martin-Löf random</text><text x="162" y="184" class="label">passes every Martin-Löf test</text><rect x="150" y="218" width="230" height="42" rx="4" class="cell"/><text x="162" y="236" font-size="13">computably random</text><text x="162" y="252" class="label">no computable martingale succeeds</text><rect x="150" y="286" width="230" height="42" rx="4" class="cell"/><text x="162" y="304" font-size="13">Schnorr random</text><text x="162" y="320" class="label">passes every Schnorr test</text><rect x="150" y="354" width="230" height="42" rx="4" class="cell"/><text x="162" y="372" font-size="13">Kurtz random</text><text x="162" y="388" class="label">in no null Π⁰₁ class</text><line x1="180" y1="58" x2="180" y2="79" class="ink-stroke" stroke-width="1.3" marker-end="url(#rn-map-arrow)"/><text x="190" y="73.0" class="label">strict: computably dominated random sequences</text><line x1="180" y1="126" x2="180" y2="147" class="ink-stroke" stroke-width="1.3" marker-end="url(#rn-map-arrow)"/><text x="190" y="141.0" class="label">strict: Ω, and every Δ⁰₂ random sequence</text><line x1="180" y1="194" x2="180" y2="215" class="ink-stroke" stroke-width="1.3" marker-end="url(#rn-map-arrow)"/><text x="190" y="209.0" class="label">strict: a Δ⁰₂ computably random sequence</text><line x1="180" y1="262" x2="180" y2="283" class="ink-stroke" stroke-width="1.3" marker-end="url(#rn-map-arrow)"/><text x="190" y="277.0" class="label">strict: admitted (in every high degree)</text><line x1="180" y1="330" x2="180" y2="351" class="ink-stroke" stroke-width="1.3" marker-end="url(#rn-map-arrow)"/><text x="190" y="345.0" class="label">strict: weakly 1-generic sequences</text><path d="M138,156 L130,156 L130,322 L138,322" class="accent-stroke" stroke-width="1.5"/><text x="122" y="233.0" text-anchor="end" class="label">equal on sequences</text><text x="122" y="249.0" text-anchor="end" class="label">that are not high</text><path d="M386,88 L556,88 L556,390 L386,390" class="accent-stroke" stroke-width="1.5"/><text x="572" y="239.0" text-anchor="middle" transform="rotate(90 572 239.0)" class="label">equal on computably dominated sequences</text></svg>
:::

Each implication is strict. A computably dominated random sequence is weakly 2-random and not 2-random (:ref{#ex-w2r-not-2-random}). $\Omega$ is random and $\Delta^0_2$, hence not weakly 2-random (:ref{#prop-weak-2-position}). A $\Delta^0_2$ computably random sequence that is not Martin-Löf random is built in :ref{#thm-cr-not-mlr}. Every high degree contains a Schnorr random sequence that is not computably random, by a theorem of Nies, Stephan and Terwijn admitted in the course on martingales. Weakly 1-generic sequences are Kurtz random and not Schnorr random (:ref{#prop-generic-kurtz}).

## Collapse in computably dominated degrees

A sequence $Z$ captured by a test enters each component at some finite stage, and the function giving these stages is computable from $Z$. If $Z$ is computably dominated, a computable function bounds these stages, and cutting each component at the bounded stage gives a clopen class, computed from $n$, that still contains $Z$. An intersection of such classes is a $\Pi^0_1$ class. So $Z$ lies in a closed class that is effectively given, and it is not Kurtz random.

:::theorem[Nies, Stephan, Terwijn]{#thm-kurtz-ml-dominated}
If $Z$ is computably dominated and Kurtz random, then $Z$ is Martin-Löf random.
:::

:::proof{of=thm-kurtz-ml-dominated}
Suppose that $Z$ is captured by a Martin-Löf test $(\mathcal U_n)$; we show that $Z$ lies in a null $\Pi^0_1$ class. Let $\mathcal U_{n,s}$ be the clopen approximation of $\mathcal U_n$ at stage $s$, with $\mathcal U_n = \bigcup_s \mathcal U_{n,s}$. Let $f(n)$ be the least $s$ with $Z \in \mathcal U_{n,s}$; it exists since $Z \in \mathcal U_n$, and $f$ is computable in $Z$. Since $Z$ is computably dominated, there is a computable function $g$ and a number $N$ with $f(n) \leq g(n)$ for all $n \geq N$. Then $Z \in \mathcal U_{n, g(n)}$ for every $n \geq N$, so $Z$ belongs to
$$
\mathcal P = \bigcap_{n \geq N} \mathcal U_{n, g(n)}.
$$
Each $\mathcal U_{n, g(n)}$ is a clopen class computable uniformly in $n$, so $\mathcal P$ is a $\Pi^0_1$ class, and $\lambda(\mathcal P) \leq \lambda(\mathcal U_n) \leq 2^{-n}$ for every $n \geq N$, so $\mathcal P$ is null. Hence $Z$ is not Kurtz random.
:::

:::quiz[the collapse theorem]
In the proof of :ref{#thm-kurtz-ml-dominated}, why is the class $\mathcal P$ closed, while $\bigcap_n \mathcal U_n$ is only $\Pi^0_2$?

- [x] Because each component is replaced by a finite stage of its enumeration, a clopen class computable uniformly in $n$, and an effective intersection of clopen classes is $\Pi^0_1$.
- [ ] Because $\mathcal U_n$ is decreasing.

  The test need not be decreasing; the closedness comes from the finite stages.
- [ ] Because $Z$ is computably dominated.

  Domination makes $Z$ belong to $\mathcal P$; the closedness of $\mathcal P$ comes from the computability of $g$.

---

Where is the computable domination of $Z$ used?

- [x] To bound the $Z$-computable function $f$, giving the entry stages, by a computable $g$, so that the bounded stages define a computable sequence of clopen classes containing $Z$.
- [ ] To show that $\mathcal P$ is null.

  Nullness follows from the bounds $\lambda(\mathcal U_n) \leq 2^{-n}$.
- [ ] To show that $f$ is total.

  $f$ is total since $Z$ belongs to every $\mathcal U_n$.
:::

The bound $\lambda(\mathcal U_n) \leq 2^{-n}$ is used only to show that $\mathcal P$ is null, and for this the nullness of $\bigcap_n \mathcal U_n$ suffices. The same proof therefore gives more.

:::theorem[Yu]{#thm-kurtz-w2r-dominated}
If $Z$ is computably dominated and Kurtz random, then $Z$ is weakly 2-random.
:::

:::proof{of=thm-kurtz-w2r-dominated}
Suppose that $Z \in \bigcap_n \mathcal U_n$, a null $\Pi^0_2$ class with decreasing classes $\mathcal U_n$. Define $f$, $g$, $N$ and $\mathcal P$ as in the proof of :ref{#thm-kurtz-ml-dominated}. Then $\mathcal P$ is a $\Pi^0_1$ class containing $Z$, and $\mathcal P \subseteq \bigcap_{n \geq N} \mathcal U_n = \bigcap_n \mathcal U_n$, since the classes decrease. So $\mathcal P$ is null, and $Z$ is not Kurtz random.
:::

The proofs of :ref{#thm-kurtz-ml-dominated} and of the theorem of Nies, Stephan and Terwijn on non-high sequences (:ref{#thm-nst-nonhigh}) follow the same pattern, with different hypotheses on the entry function $f$. If a computable function bounds $f$ almost everywhere, the bounded components form a closed class, and Kurtz randomness fails. If a computable function exceeds $f$ only infinitely often, which is what non-highness provides by Martin's theorem, the bounded components contain $Z$ infinitely often and form a total Solovay test, and Schnorr randomness fails. Domination everywhere yields a closed class; domination infinitely often yields a test.

:::corollary{#cor-dominated-collapse}
On computably dominated sequences, Kurtz, Schnorr, computable, Martin-Löf and weak 2-randomness coincide, and no computably dominated sequence is 2-random. There are computably dominated weakly 2-random sequences.
:::

:::proof{of=cor-dominated-collapse}
The coincidence follows from :ref{#thm-kurtz-w2r-dominated} and :ref{#prop-notions-implications}. A 2-random sequence has hyperimmune degree by Kurtz's theorem, admitted in :ref{to="randomness-notions/relative-randomness"}, so it is not computably dominated. A computably dominated random sequence exists by :ref{#cor-mlr-structure} (3), and it is weakly 2-random by the first statement.
:::

::::exercise{#ex-kurtz-delta2 difficulty=2 objective="Separate Kurtz randomness from Martin-Löf randomness below $\emptyset'$, and see that the separating sequence is not computably dominated."}
Show that there is a Kurtz random sequence computable in $\emptyset'$ that is not Martin-Löf random. Show that it is not computably dominated, directly from :ref{#thm-kurtz-ml-dominated}.

:::solution
By :ref{#prop-1-generic}, there is a 1-generic set $G \leq_T \emptyset'$. It is weakly 1-generic, since a dense set of strings has no string without an extension in it, hence Kurtz random by :ref{#prop-generic-kurtz}, and not Schnorr random, hence not Martin-Löf random. If $G$ were computably dominated, it would be Martin-Löf random by :ref{#thm-kurtz-ml-dominated}, since it is Kurtz random.
:::
::::

## Hyperimmune degrees

Outside the computably dominated sets, the collapse fails as badly as possible: Kurtz showed that the sets of hyperimmune degree are exactly those that compute a weakly 1-generic sequence (:ref{#thm-kurtz}, proved in the course on Cohen genericity).

:::theorem[Kurtz]{#thm-hyperimmune-kurtz}
Every set of hyperimmune degree computes a Kurtz random sequence that is not Schnorr random.
:::

:::proof{of=thm-hyperimmune-kurtz}
By :ref{#thm-kurtz}, a set of hyperimmune degree computes a weakly 1-generic sequence, which is Kurtz random and not Schnorr random by :ref{#prop-generic-kurtz}.
:::

:::corollary{#cor-kurtz-dichotomy}
For every set $X$, the following are equivalent:

1. $X$ is computably dominated;
2. every Kurtz random sequence computable in $X$ is weakly 2-random;
3. every Kurtz random sequence computable in $X$ is Schnorr random.
:::

:::proof{of=cor-kurtz-dichotomy}
(1 ⇒ 2) A sequence $Y \leq_T X$ is computably dominated, since every $Y$-computable function is $X$-computable. If it is Kurtz random, it is weakly 2-random by :ref{#thm-kurtz-w2r-dominated}.

(2 ⇒ 3) Weak 2-randomness implies Schnorr randomness, by :ref{#prop-notions-implications}.

(3 ⇒ 1) If $X$ is not computably dominated, it has hyperimmune degree, and :ref{#thm-hyperimmune-kurtz} gives a Kurtz random sequence computable in $X$ that is not Schnorr random.
:::

:::quiz[the dichotomy]
In (1 ⇒ 2) of :ref{#cor-kurtz-dichotomy}, why is :ref{#thm-kurtz-w2r-dominated} applied to $Y$ rather than to $X$?

- [x] Because the theorem concerns a sequence that is both computably dominated and Kurtz random; $Y$ is Kurtz random by hypothesis, and computably dominated because computable domination is closed downward under Turing reducibility.
- [ ] Because $X$ is not computably dominated.

  $X$ is computably dominated by hypothesis (1); the point is that $X$ need not be Kurtz random.
- [ ] Because weak 2-randomness is closed upward under Turing reducibility.

  It is not: a weakly 2-random sequence $Z$ is computable in $Z \oplus \emptyset'$, which is not even Martin-Löf random, since its odd half $\emptyset'$ is not random (:ref{#thm-van-lambalgen}). In any case, the hypothesis of the theorem is about the sequence to which it is applied.
:::

Kurtz proved more: every hyperimmune degree contains a weakly 1-generic sequence, obtained by coding the given set into the generic sequence during the construction (Downey–Hirschfeldt, Corollary 2.24.19; Nies, Theorem 1.8.50). So a Turing degree contains a Kurtz random sequence that is not Schnorr random if and only if it is hyperimmune. With :ref{#thm-kurtz-w2r-dominated}, this reduces the degrees of Kurtz random sequences to known ones: a degree contains a Kurtz random sequence if and only if it is hyperimmune or contains a Martin-Löf random sequence, which is then weakly 2-random if the degree is computably dominated.

The two dividing lines are compatible: a high set has hyperimmune degree (:ref{#cor-high-hyperimmune}), so on a sequence that is not of hyperimmune degree the five notions of :ref{#fig-notions-map} coincide, while on a sequence that is of hyperimmune degree but not high, Kurtz randomness may differ from the three notions above it, which still coincide.

## Notes and references

Kurtz (1981) introduced weak randomness, proved that weakly 1-generic sets are weakly random, and characterized the hyperimmune degrees as the degrees of weakly 1-generic sets. Nies, Stephan and Terwijn (2005) proved :ref{#thm-kurtz-ml-dominated}; the strengthening :ref{#thm-kurtz-w2r-dominated} is due to Yu (unpublished; Downey–Hirschfeldt, Theorem 8.11.12; Nies, Proposition 3.6.4). Bi-immunity of Kurtz random sequences is due to Jockusch (see Kurtz 1981; Downey–Hirschfeldt, Theorem 7.2.23). Downey and Hirschfeldt present the separations and collapses of this lesson in Section 8.11 (Theorem 8.11.7, Corollaries 8.11.8 and 8.11.10, Theorems 8.11.11 and 8.11.12); Nies discusses the behavior of weak randomness in hyperimmune and computably dominated degrees in Remark 3.5.3 and Proposition 3.6.4.

- S. A. Kurtz, *Randomness and genericity in the degrees of unsolvability*, PhD thesis, University of Illinois at Urbana–Champaign, 1981.
- A. Nies, F. Stephan and S. A. Terwijn, *Randomness, relativization and Turing degrees*, Journal of Symbolic Logic 70 (2005), 515–535.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 2.24, 7.2 and 8.11.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 1.8, 3.5 and 3.6.

:::::exercises
::::exercise{#ex-dominated-dnwy difficulty=1 objective="Derive the collapse on computably dominated random sequences from the theorem of Downey, Nies, Weber and Yu." lessons="weak-2-randomness"}
Show that every computably dominated Martin-Löf random sequence is weakly 2-random by means of :ref{#thm-dnwy}, without using :ref{#thm-kurtz-w2r-dominated}.

:::solution
A computably dominated random sequence computes no non-computable c.e. set, as shown in :ref{#ex-w2r-not-2-random}, so it is weakly 2-random by :ref{#thm-dnwy}.
:::
::::

::::exercise[Halves of a Kurtz random sequence]{#ex-kurtz-halves difficulty=1 objective="Pull back a null $\Pi^0_1$ class along the projection onto one half, and see that the join of two Kurtz random sequences need not be Kurtz random."}
Show that if $A \oplus B$ is Kurtz random, then $A$ and $B$ are Kurtz random. Give a Kurtz random sequence $A$ such that $A \oplus A$ is not Kurtz random.

:::solution
Suppose that $A$ is not Kurtz random, and let $\mathcal P = [T]$ be a null $\Pi^0_1$ class containing $A$, with $T$ a computable tree. Let $T'$ be the set of the strings $\rho$ such that the string $\rho(0) \rho(2) \rho(4) \cdots$ of the bits of $\rho$ at even positions belongs to $T$. It is a computable tree, and $[T'] = \{ X \oplus Y : X \in \mathcal P \}$, which contains $A \oplus B$. Its complement $\{ X \oplus Y : X \notin \mathcal P \}$ is open, with section at $X$ equal to the whole space if $X \notin \mathcal P$ and empty otherwise; by :ref{#fact-fubini}, its measure is $\lambda(\cs \setminus \mathcal P) = 1$. So $[T']$ is null, and $A \oplus B$ is not Kurtz random. The same argument with the odd positions applies to $B$.

Let $A$ be Kurtz random, for instance Martin-Löf random. The sequence $A \oplus A$ belongs to the class of the sequences $Z$ with $Z(2i) = Z(2i+1)$ for every $i$. This class is $\Pi^0_1$, as the class of paths of the computable tree of the strings with this property, and for every $n$ it is contained in a clopen class of measure $2^n \cdot 2^{-2n} = 2^{-n}$, given by the strings of length $2n$ with the property; so it is null, and $A \oplus A$ is not Kurtz random.
:::
::::

::::exercise[Kurtz random sequences that are not Martin-Löf random]{#ex-kurtz-not-mlr-hyperimmune difficulty=1 objective="Apply the collapse theorems to locate Kurtz random sequences that are $\Delta^0_2$ or not Martin-Löf random in the hyperimmune degrees."}
1. Let $Z$ be Kurtz random and $\Delta^0_2$. Show that $Z$ has hyperimmune degree in two ways: with :ref{#thm-computation-function}, and with :ref{#thm-kurtz-w2r-dominated}.
2. Show that every Kurtz random sequence that is not Martin-Löf random computes a Kurtz random sequence that is not Schnorr random.

:::solution
1. A computable sequence $Z$ forms the null $\Pi^0_1$ class $\{ Z \}$, so a Kurtz random sequence is not computable. A non-computable $\Delta^0_2$ set computes its computation function, which no computable function dominates (:ref{#thm-computation-function}); so $Z$ has hyperimmune degree. Alternatively, if $Z$ were computably dominated, it would be weakly 2-random by :ref{#thm-kurtz-w2r-dominated}, which no $\Delta^0_2$ sequence is (:ref{#prop-weak-2-position} (2)).
2. Let $Z$ be Kurtz random and not Martin-Löf random. By :ref{#thm-kurtz-ml-dominated}, $Z$ is not computably dominated, so it has hyperimmune degree, and :ref{#thm-hyperimmune-kurtz} gives a Kurtz random sequence computable in $Z$ that is not Schnorr random.
:::
::::

::::exercise[Weakly 1-generic sequences have hyperimmune degree]{#ex-generic-hyperimmune-degree difficulty=1 objective="Combine the collapse theorem with the properties of weakly 1-generic sequences to recover one direction of Kurtz's theorem on hyperimmune degrees."}
Deduce from :ref{#thm-kurtz-ml-dominated} and :ref{#prop-generic-kurtz} that every weakly 1-generic sequence has hyperimmune degree. Compare with the proof of this fact in the course on Cohen genericity.

:::solution
Let $G$ be weakly 1-generic. By :ref{#prop-generic-kurtz}, $G$ is Kurtz random and not Schnorr random, hence not Martin-Löf random (:ref{#prop-notions-implications}). If $G$ were computably dominated, it would be Martin-Löf random by :ref{#thm-kurtz-ml-dominated}. So $G$ is not computably dominated, that is, it has hyperimmune degree.

In :ref{#thm-kurtz}, this direction is proved by reading a hyperimmune function off $G$: a dense set of strings prescribes long blocks of zeros, so the lengths of the blocks of zeros of $G$ escape every computable function. The argument above hides the same phenomenon in two steps: the failure of the law of large numbers, which comes from dense sets prescribing long blocks of ones, and the function giving the stages at which $G$ enters the components of a test, which no computable function dominates, by the proof of :ref{#thm-kurtz-ml-dominated}.
:::
::::

::::exercise[The collapse with Solovay tests]{#ex-kurtz-solovay-dominated difficulty=2 objective="Adapt the proof of the collapse theorem to Solovay tests, by bounding the stage at which the sequence is seen in a component of large index."}
Show directly, without Martin-Löf tests, that a computably dominated Kurtz random sequence $Z$ belongs to only finitely many components of every Solovay test.

:::solution
Let $(\mathcal S_m)$ be a Solovay test, with clopen approximations $\mathcal S_{m,s}$ increasing with $s$, and suppose that $Z \in \mathcal S_m$ for infinitely many $m$. Let $f(k)$ be the least $s$ such that $Z \in \mathcal S_{m,s}$ for some $m$ with $k \leq m \leq s$. It exists: choose $m \geq k$ with $Z \in \mathcal S_m$, and $s'$ with $Z \in \mathcal S_{m,s'}$; then $s = \max(m, s')$ works, since the approximations increase. The function $f$ is computable in $Z$, so there are a computable function $g$ and a number $N$ with $f(k) \leq g(k)$ for $k \geq N$. Let
$$
\mathcal C_k = \bigcup_{k \leq m \leq g(k)} \mathcal S_{m, g(k)}.
$$
It is a clopen class, computable from $k$, as a finite union of clopen classes given at stage $g(k)$. For $k \geq N$, some $m$ with $k \leq m \leq f(k) \leq g(k)$ satisfies $Z \in \mathcal S_{m, f(k)} \subseteq \mathcal S_{m, g(k)}$, so $Z \in \mathcal C_k$. Hence $Z$ belongs to the $\Pi^0_1$ class $\mathcal P = \bigcap_{k \geq N} \mathcal C_k$. Since $\lambda(\mathcal C_k) \leq \sum_{m \geq k} \lambda(\mathcal S_m)$, the tail of a convergent series, $\mathcal P$ is null. So $Z$ is not Kurtz random, a contradiction.

With :ref{#thm-solovay}, this gives another proof of :ref{#thm-kurtz-ml-dominated}. The entry function now looks for a component of index at least $k$, since the components containing $Z$ are not known in advance.
:::
::::

::::exercise[Hyperimmune sets]{#ex-random-not-hyperimmune difficulty=2 objective="Use a Solovay test and a dense set of strings to compare Martin-Löf and Kurtz random sets with respect to hyperimmunity."}
Recall that an infinite set $A$ is **hyperimmune** if for every disjoint strong array $(F_n)$ there is $n$ with $F_n \cap A = \emptyset$ (:ref{#def-hyperimmune-set}). Show that no Martin-Löf random set is hyperimmune, but that every weakly 1-generic set is hyperimmune. Deduce that some Kurtz random sets are hyperimmune.

:::solution
*Random sets.* Let $I_k$ be the interval of the $k + 1$ integers from $k(k+1)/2$ to $k(k+1)/2 + k$; the intervals $I_k$ are pairwise disjoint and computable from $k$. Let $\mathcal S_k$ be the clopen class of the sequences $X$ with $X \cap I_k = \emptyset$, of measure $2^{-(k+1)}$; then $(\mathcal S_k)$ is a Solovay test. Let $Z$ be random. By :ref{#thm-solovay}, there is $m$ with $Z \notin \mathcal S_k$ for every $k \geq m$, that is, $Z \cap I_k \neq \emptyset$ for $k \geq m$. The sequence $F_n = I_{m+n}$ is a disjoint strong array, each member of which meets $Z$. So $Z$, which is infinite since it is not computable, is not hyperimmune.

*Weakly 1-generic sets.* Let $G$ be weakly 1-generic; it is infinite (:ref{#ex-weakly-generic}). Let $(F_n)$ be a disjoint strong array. If some $F_n$ is empty, it does not meet $G$. Otherwise, given a string $\sigma$, only finitely many $F_n$ have an element below $|\sigma|$, since each number belongs to at most one of them; so there is a least $n$ with $\min F_n \geq |\sigma|$, found by computing the sets $F_n$ in turn. Let $\tau_\sigma = \sigma\, 0^{\max F_n - |\sigma| + 1}$. The set $\{ \tau_\sigma : \sigma \in \bstr \}$ is computable and dense, so $G$ has a prefix $\tau_\sigma$, and then $G(x) = 0$ for every $x \in F_n$: $F_n \cap G = \emptyset$. So $G$ is hyperimmune.

Weakly 1-generic sets exist, for instance the 1-generic sets of :ref{#prop-1-generic}, and they are Kurtz random (:ref{#prop-generic-kurtz}). The proof for random sets uses a Solovay test, which Kurtz randomness does not provide. That no random set is hyperimmune is folklore (Downey–Hirschfeldt, Theorem 9.14.15).
:::
::::
:::::
