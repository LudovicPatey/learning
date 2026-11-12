---
title: The Markwald–Kleene theorem
summary: Every computable ordinal has a notation in Kleene's O, by effective transfinite recursion along a computable well-ordering; the conversion only gives upper bounds; relativization and the ordinals ω₁ˣ.
duration: 25
prerequisites: [kleene-o]
---

The previous lesson showed that every constructive ordinal is computable (:ref{#prop-constructive-computable}): the notations below a notation $a$ form a c.e. well-ordering of type $|a|$. This lesson proves the converse, due to Markwald and to Kleene. Given a computable well-ordering $R$, we assign notations to its elements by effective transfinite recursion along $R$, using the addition of notations (:ref{#lem-notation-sum}) to bound the notations already assigned. The conversion is uniform, but it gives only an upper bound for the order type; an exact uniform conversion is impossible.

## Bounding a c.e. set of notations

A c.e. set of notations need not have a largest element, and its elements need not be $<_{\mathcal O}$-comparable, as two notations of $\omega$ show (:ref{#ex-notations}). The supremum of their ordinals is nevertheless bounded by a single notation, computed from an index of the set: one adds up the notations enumerated so far, which yields a sequence that is $<_{\mathcal O}$-increasing by construction, and takes its limit.

:::lemma{#lem-notation-sup}
There is a total computable function $u$ such that if $W_e \subseteq \mathcal O$, then $u(e) \in \mathcal O$ and $|u(e)| \geq |c|$ for every $c \in W_e$.
:::

:::proof{of=lem-notation-sup}
Let $d_n$ be the sum, with $+_{\mathcal O}$ in the order of enumeration, of the elements of $W_{e,n}$, and $d_n = 1$ if $W_{e,n}$ is empty. Let $c_0 = 1$ and $c_{n+1} = c_n +_{\mathcal O} 2^{d_n}$. Then $c_n <_{\mathcal O} c_{n+1}$ by :ref{#lem-notation-sum}, the function $n \mapsto c_n$ is total computable with an index computed from $e$, and $u(e) = 3 \cdot 5^{(\text{this index})}$ belongs to $\mathcal O$ when $W_e \subseteq \mathcal O$. Every $c \in W_e$ is in some $W_{e,n}$, and $|c_{n+1}| \geq |d_n| \geq |c|$, since $|x +_{\mathcal O} y| = |x| + |y| \geq |y|$.
:::

## The theorem

The proof is an effective transfinite recursion along $R$ rather than along notations. One wants to assign to each element $x$ of the well-ordering $R$ a notation $g(x)$ above the notations of all its predecessors. The predecessors of $x$ form a c.e. set, so the notations $g(y)$, $y <_R x$, form a c.e. set as soon as $g$ is computable, and :ref{#lem-notation-sup} bounds them. The definition of $g$ uses $g$ itself, through the recursion theorem. As for the addition of notations, $g$ is total whatever $R$ is, and the well-ordering hypothesis is used only to prove, by induction along $R$, that its values are notations.

:::theorem[Markwald, Kleene]{#thm-markwald}
Every computable ordinal is constructive: from an index of a computable well-ordering $R$, one computes $a \in \mathcal O$ with $|a| \geq |R|$.
:::

:::proof{of=thm-markwald}
By the recursion theorem (:ref{#cor-self-reference}), there is a total computable function $g$ such that $g(x) = u(i_x)$, where $i_x$ is an index of the c.e. set $\{ 2^{g(y)} : y <_R x \}$, computed from $x$ and an index of $g$. We show by induction along the well-ordering $R$ that $g(x) \in \mathcal O$ and $|g(x)| \geq |R_{<x}|$, the type of the initial segment below $x$. If this holds for all $y <_R x$, then $W_{i_x} \subseteq \mathcal O$, and by :ref{#lem-notation-sup}, $g(x) \in \mathcal O$ and $|g(x)| \geq |g(y)| + 1 \geq |R_{<y}| + 1$ for all $y <_R x$; the supremum of the right-hand side is $|R_{<x}|$. Finally $a = u(i)$, with $i$ an index of $\{ 2^{g(x)} : x \text{ in the field of } R \}$, satisfies $|a| \geq |R|$. Since the constructive ordinals are closed downward, $|R|$ is constructive.
:::

:::corollary{#cor-constructive-computable}
The constructive ordinals are exactly the computable ordinals, that is, the ordinals below $\omega_1^{\mathrm{CK}}$.
:::

The two conversions are uniform, but the second one only gives an upper bound $|a| \geq |R|$. An exact uniform conversion is impossible (see the exercises): a notation contains more information than a well-ordering, namely the decomposition of the ordinal into successor and limit steps.

:::quiz[notations]
In the proof of :ref{#thm-markwald}, why does the set $W_{i_x}$ contain $2^{g(y)}$ rather than $g(y)$?

- [x] To obtain $|g(x)| \geq |g(y)| + 1$ for $y <_R x$, which is needed to reach the type $|R_{<x}| = \sup_{y <_R x} (|R_{<y}| + 1)$.
- [ ] Because $g(y)$ might not belong to $\mathcal O$.

  By the induction hypothesis, $g(y) \in \mathcal O$; the successor is needed for the inequality.
- [ ] To make the set $W_{i_x}$ infinite.

  The set may be finite; the function $u$ handles finite sets.

---

Why does the definition of $g$ not require deciding whether $R$ is a well-ordering?

- [x] Because $g$ is total for every $R$, by the recursion theorem; the well-ordering hypothesis is used only in the proof that its values are notations.
- [ ] Because every computable linear order is a well-ordering.

  Many computable linear orders, such as the order of $\mathbb Q$, are not well-orderings.
- [ ] Because $u$ checks that its input is a subset of $\mathcal O$.

  $u$ checks nothing; its output is a notation only when the input set consists of notations.
:::

## Relativization

All definitions relativize to an oracle $X$: an ordinal is **$X$-computable** if it is the type of an $X$-computable well-ordering, $\mathcal O^X$ is defined with $\Phi^X_e$ in place of $\Phi_e$, and the results of this lesson hold relative to $X$, with the same proofs. The least non-$X$-computable ordinal is written $\omega_1^X$. It is countable for every $X$, and every countable ordinal is $X$-computable for some $X$, namely for a set coding a well-ordering of that type; so $\omega_1$ is the supremum of the ordinals $\omega_1^X$. One has $\omega_1^X = \omega_1^{\mathrm{CK}}$ for many non-computable $X$, for instance every arithmetic $X$, and $\omega_1^X > \omega_1^{\mathrm{CK}}$ for $X = \mathcal O$. Both facts are proved in the lesson on the boundedness theorem (:ref{#prop-omega1-relative}).

## Exercises

::::exercise{difficulty=1}
Using :ref{#prop-wo-not-transparent}, show that no partial computable function $h$ maps every $e \in \mathrm{WO}$ to a notation of exactly $|L_e|$. Show on the other hand that $e \mapsto$ (the notation $a$ given by :ref{#thm-markwald}) and $a \mapsto 2^a$ give, uniformly, a notation of an ordinal strictly above $|L_e|$.

:::solution
Let $f$ be the function of :ref{#prop-wo-not-transparent}. If $h$ existed, then $h(f(n))$ would be a notation of $\omega$ or of $\omega + 1$. A notation of $\omega + 1$ has the form $2^c$ with $c \in \mathcal O$, while a notation of $\omega$ has the form $3 \cdot 5^e$, since $|1| = 0$ and $|2^c| = |c| + 1$ is a successor. So $n \in \emptyset'$ if and only if $h(f(n))$ is a power of $2$, which would make $\emptyset'$ computable. For the second part, if $a \in \mathcal O$ and $|a| \geq |L_e|$, then $2^a \in \mathcal O$ and $|2^a| = |a| + 1 > |L_e|$. Upper bounds can be computed uniformly; exact values cannot.
:::
::::

## Notes and references

Markwald (1954) proved that computable and constructive ordinals coincide, and Spector (1955) proved it independently; the uniform form of :ref{#thm-markwald} is the one used in the later lessons. Monin and Patey prove the theorem in the section *Effective ordinals* of their chapter on transfinite numbers, with the same structure: a supremum lemma for c.e. sets of notations, then a function defined by the recursion theorem along the well-ordering. Our supremum lemma uses the sequence $c_{n+1} = c_n +_{\mathcal O} 2^{d_n}$, which is increasing by :ref{#lem-notation-sum} whatever the enumeration. Monin and Patey also give the impossibility of an exact uniform conversion as an exercise. The ordinals $\omega_1^X$ are discussed by Nies (Section 9.1), who proves $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ in Exercise 9.1.8.

- W. Markwald, *Zur Theorie der konstruktiven Wohlordnungen*, Mathematische Annalen 127 (1954), 135–149.
- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- B. Monin and L. Patey, *Computability theory*, chapter *Transfinite numbers*, sections *Effective ordinals* and *Relativization*.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.1.
