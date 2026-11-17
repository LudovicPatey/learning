---
title: The Markwald–Kleene theorem
summary: Every computable ordinal has a notation in Kleene's O, by effective transfinite recursion along a computable well-ordering; the conversion only gives upper bounds; relativization and the ordinals ω₁ˣ.
duration: 20
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

The two conversions are uniform, but the second one only gives an upper bound $|a| \geq |R|$. An exact uniform conversion is impossible (:ref{#ex-no-exact-conversion}): a notation contains more information than a well-ordering, namely the decomposition of the ordinal into successor and limit steps.

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

::::exercise{#ex-no-exact-conversion difficulty=1 objective="Show that no algorithm converts indices of well-orderings into notations of exactly the same ordinal, although notations of strict upper bounds can be computed."}
Using :ref{#prop-wo-not-transparent}, show that no partial computable function $h$ maps every $e \in \mathrm{WO}$ to a notation of exactly $|L_e|$. Show on the other hand that $e \mapsto$ (the notation $a$ given by :ref{#thm-markwald}) and $a \mapsto 2^a$ give, uniformly, a notation of an ordinal strictly above $|L_e|$.

:::solution
Let $f$ be the function of :ref{#prop-wo-not-transparent}. If $h$ existed, then $h(f(n))$ would be a notation of $\omega$ or of $\omega + 1$. A notation of $\omega + 1$ has the form $2^c$ with $c \in \mathcal O$, while a notation of $\omega$ has the form $3 \cdot 5^e$, since $|1| = 0$ and $|2^c| = |c| + 1$ is a successor. So $n \in \emptyset'$ if and only if $h(f(n))$ is a power of $2$, which would make $\emptyset'$ computable. For the second part, if $a \in \mathcal O$ and $|a| \geq |L_e|$, then $2^a \in \mathcal O$ and $|2^a| = |a| + 1 > |L_e|$. Upper bounds can be computed uniformly; exact values cannot.

Adapted from Monin and Patey, chapter *Transfinite numbers*, exercise of the section *Effective ordinals*.
:::
::::

## Relativization

All definitions relativize to an oracle $X$: an ordinal is **$X$-computable** if it is the type of an $X$-computable well-ordering, $\mathcal O^X$ is defined with $\Phi^X_e$ in place of $\Phi_e$, and the results of this lesson hold relative to $X$, with the same proofs. The least non-$X$-computable ordinal is written $\omega_1^X$. It is countable for every $X$, and every countable ordinal is $X$-computable for some $X$, namely for a set coding a well-ordering of that type; so $\omega_1$ is the supremum of the ordinals $\omega_1^X$. One has $\omega_1^X = \omega_1^{\mathrm{CK}}$ for many non-computable $X$, for instance every arithmetic $X$, and $\omega_1^X > \omega_1^{\mathrm{CK}}$ for $X = \mathcal O$. Both facts are proved in the lesson on the boundedness theorem (:ref{#prop-omega1-relative}).

## Notes and references

Markwald (1954) proved that computable and constructive ordinals coincide, and Spector (1955) proved it independently; the uniform form of :ref{#thm-markwald} is the one used in the later lessons. Monin and Patey prove the theorem in the section *Effective ordinals* of their chapter on transfinite numbers, with the same structure: a supremum lemma for c.e. sets of notations, then a function defined by the recursion theorem along the well-ordering. Our supremum lemma uses the sequence $c_{n+1} = c_n +_{\mathcal O} 2^{d_n}$, which is increasing by :ref{#lem-notation-sum} whatever the enumeration. Monin and Patey also give the impossibility of an exact uniform conversion as an exercise. The ordinals $\omega_1^X$ are discussed by Nies (Section 9.1), who proves $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ in Exercise 9.1.8.

- W. Markwald, *Zur Theorie der konstruktiven Wohlordnungen*, Mathematische Annalen 127 (1954), 135–149.
- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- B. Monin and L. Patey, *Computability theory*, chapter *Transfinite numbers*, sections *Effective ordinals* and *Relativization*.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.1.

:::::exercises
::::exercise{#ex-omega1x-degree difficulty=1 objective="Derive the first properties of the ordinals $\omega_1^X$ from the relativized closure properties of computable ordinals."}
Show that if $X \leq_T Y$, then $\omega_1^X \leq \omega_1^Y$, so that $\omega_1^X$ depends only on the Turing degree of $X$. Show that $\omega_1^X$ is a countable limit ordinal for every $X$.

:::solution
Relativized, :ref{#prop-computable-ordinals-basic} (1) says that the $X$-computable ordinals are closed downward; they form a set of ordinals, which is therefore the ordinal $\omega_1^X$, the least ordinal that is not $X$-computable. If $X \leq_T Y$, every $X$-computable relation is $Y$-computable, so every $X$-computable ordinal is $Y$-computable, and $\omega_1^X \subseteq \omega_1^Y$, that is, $\omega_1^X \leq \omega_1^Y$. If $X \equiv_T Y$, both inequalities hold. There are countably many $X$-computable relations, so $\omega_1^X$ is countable. It is not $0$, since $0$ is $X$-computable, and it is not a successor $\alpha + 1$: if $\alpha$ is $X$-computable, so is $\alpha + 1$, by :ref{#prop-computable-ordinals-basic} (2) relativized. So it is a limit.
:::
::::

::::exercise{#ex-o-not-ce difficulty=1 objective="Apply the supremum lemma to show that no c.e. set of notations reaches all constructive ordinals."}
Show that if $W_e \subseteq \mathcal O$, then some constructive ordinal has no notation in $W_e$, and the ordinals $|c|$, $c \in W_e$, are bounded below $\omega_1^{\mathrm{CK}}$. Deduce that $\mathcal O$ is not c.e.

:::solution
By :ref{#lem-notation-sup}, $u(e) \in \mathcal O$ and $|u(e)| \geq |c|$ for every $c \in W_e$. Then $2^{u(e)} \in \mathcal O$ is a notation of $|u(e)| + 1$, a constructive ordinal larger than every $|c|$, $c \in W_e$; so it has no notation in $W_e$. The ordinals $|c|$, $c \in W_e$, are bounded by the constructive ordinal $|u(e)|$, which is below $\omega_1^{\mathrm{CK}}$ by :ref{#cor-constructive-computable}. Since $\mathcal O$ contains a notation of every constructive ordinal, $\mathcal O$ is not of the form $W_e$.
:::
::::

::::exercise{#ex-ce-wo-bounded difficulty=2 objective="Bound the types of a c.e. set of computable well-orderings in two ways: by an ordered sum, and by the conversion into notations."}
Let $W \subseteq \mathrm{WO}$ be c.e. Show that $\sup \{ |L_e| : e \in W \} < \omega_1^{\mathrm{CK}}$, by computing from an index of $W$ an index of a computable well-ordering whose type bounds all the $|L_e|$, $e \in W$. Give two proofs: one with an ordered sum of the orders $L_e$, one with :ref{#thm-markwald} and :ref{#lem-notation-sup}.

:::solution
*Ordered sum.* Let $e_0, e_1, \dots$ be the elements of $W$ in order of enumeration (a finite list if $W$ is finite). Let $S$ be the relation whose field consists of the pairs $\langle k, x \rangle$ such that $e_k$ is enumerated and $x$ is in the field of $L_{e_k}$, with $\langle k, x \rangle \leq_S \langle k', x' \rangle$ if $k < k'$, or $k = k'$ and $(x, x') \in L_{e_k}$. It is c.e., uniformly in an index of $W$: one waits until $e_k$ is enumerated, and then $L_{e_k}$ is computable since $e_k \in \mathrm{WO}$. It is a linear order of its field, and a well-ordering: in a descending sequence, the first components are non-increasing, hence eventually constant, equal to some $k$, and from then on the second components descend in $L_{e_k}$, which is impossible. For each $k$, the pairs $\langle k, x \rangle$ form a copy of $L_{e_k}$, so $|S| \geq |L_{e_k}|$. Placing a copy of $\omega$ in front of $S$ gives a c.e. well-ordering with infinite field, of type $\omega + |S| \geq |S|$, and :ref{#prop-computable-ordinals-basic} (3) turns it into a computable well-ordering, uniformly.

*Notations.* Let $G$ be the total computable function given by :ref{#thm-markwald}: for $e \in \mathrm{WO}$, $G(e) \in \mathcal O$ and $|G(e)| \geq |L_e|$. The set $\{ G(e) : e \in W \}$ is c.e., with an index computed from an index of $W$, and it is contained in $\mathcal O$. :ref{#lem-notation-sup} gives a notation $b$ with $|b| \geq |G(e)| \geq |L_e|$ for every $e \in W$, and :ref{#prop-constructive-computable} turns $b$ into an index of a computable well-ordering of type $|b|$.

In both cases the bound is a computable ordinal, hence below $\omega_1^{\mathrm{CK}}$. The boundedness lesson extends this result from c.e. sets to $\Sigma^1_1$ sets of indices.
:::
::::

::::exercise{#ex-exact-conversion-predecessor difficulty=2 objective="Convert a computable well-ordering into exact notations by effective transfinite recursion when its decomposition into zero, successor and limit elements is computable."}
Let $R$ be a computable well-ordering of $\nat$, and suppose that the function $p$ is computable, where $p(x) = 0$ if $x$ is the least element, $p(x) = 1$ if $x$ is a limit element (it has predecessors but no immediate predecessor), and $p(x) = y + 2$ if $y$ is the immediate predecessor of $x$. Show that there is a total computable function $g$ such that for every $x$, $g(x) \in \mathcal O$ and $|g(x)| = |R_{<x}|$, and $g(y) <_{\mathcal O} g(x)$ whenever $y <_R x$. Compare with :ref{#ex-no-exact-conversion}.

:::solution
For a limit element $x$, let $y_0, y_1, \dots$ be the elements $<_R x$ in increasing numerical order. There are infinitely many, since $x$ has predecessors and $R_{<x}$ has no largest element (a largest one would be an immediate predecessor of $x$). Let $z_0 = y_0$, and let $z_{n+1} = y_k$ for the least $k$ such that $y_k >_R z_n$; such a $k$ exists since $z_n <_R x$ is not the largest element of $R_{<x}$. The sequence $(z_n)$ is computable from $x$ and $R$, and $<_R$-increasing.

By the recursion theorem, there is a partial computable function $g$ with $g(x) = 1$ if $p(x) = 0$; $g(x) = 2^{g(y)}$ if $p(x) = y + 2$; and $g(x) = 3 \cdot 5^{j(x)}$ if $p(x) = 1$, where $j(x)$ is an index, computed from $x$ and the index of $g$, of the function $n \mapsto g(z_n)$. The limit case only computes an index. The successor case calls $g$ on the immediate predecessor; the chain $x >_R y >_R \cdots$ of successive immediate predecessors is finite, since $R$ is a well-ordering, and ends at the least element or at a limit element. So $g$ is total.

We prove the properties by induction along $R$. If $x$ is the least element, $g(x) = 1$ and $|R_{<x}| = 0$. If $x$ is the immediate successor of $y$, then $g(x) = 2^{g(y)} \in \mathcal O$ with $|g(x)| = |R_{<y}| + 1 = |R_{<x}|$, since $R_{<x} = R_{<y} \cup \{ y \}$; and if $y' <_R x$, then $y' \leq_R y$, so $g(y') \leq_{\mathcal O} g(y) <_{\mathcal O} g(x)$. If $x$ is a limit, the induction hypothesis applied to $z_{n+1}$ gives $g(z_n) <_{\mathcal O} g(z_{n+1})$, so $g(x) \in \mathcal O$, with $|g(x)| = \sup_n |R_{<z_n}|$.

The sequence $(z_n)$ is cofinal in $R_{<x}$. Let $k_n$ be such that $z_n = y_{k_n}$. By the choice of $k_{n+1}$, every $y_j$ with $j < k_{n+1}$ satisfies $y_j \leq_R z_n$. In particular $k_{n+1} > k_n$, so $k_n \to \infty$, and every $y_j$ lies below some $z_n$. Hence, for $y <_R x$, there is $n$ with $y \leq_R z_n <_R z_{n+1}$, which gives $g(y) <_{\mathcal O} g(z_{n+1}) <_{\mathcal O} g(x)$ and $|R_{<y}| + 1 \leq |R_{<z_{n+1}}|$. Since $|R_{<x}| = \sup_{y <_R x} (|R_{<y}| + 1)$ and $z_n <_R x$, we get $|R_{<x}| = \sup_n |R_{<z_n}| = |g(x)|$.

The construction is uniform in indices of $R$ and of $p$, and gives exact notations of the proper initial segments of $R$. It does not give a notation of $|R|$ itself, which also depends on whether $R$ has a largest element. For the orders $L_{f(n)}$ of :ref{#prop-wo-not-transparent}, the function $p$ is computable uniformly in $n$: a number is a limit element exactly when it is the special number, which is decidable. The obstruction of :ref{#ex-no-exact-conversion} is therefore the existence of a largest element, a $\Sigma^0_2$ property (:ref{#ex-largest-sigma02}).
:::
::::
:::::
