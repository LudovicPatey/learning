---
title: Kalimullin pairs
summary: Semi-computable sets (Jockusch) and their selectors; left cuts of computable linear orders; Kalimullin pairs, defined by a set of pairs separating A × B from the product of the complements; every Kalimullin pair relative to U is a minimal pair relative to every degree above U, robustly; a semi-computable set and its complement form a Kalimullin pair; nontrivial pairs below every total degree outside the Δ⁰₂ degrees.
duration: 25
prerequisites: [enumeration-jump/skip-and-cototality]
---

In the Turing degrees, a minimal pair is fragile: by the Posner–Robinson theorem, any two nonzero degrees become joined to the same jump above a suitable degree, and the property of having no common lower bound disappears above it. In the enumeration degrees, some pairs keep this property relative to every degree: they are minimal pairs **robustly**. Kalimullin characterized them by a simple combinatorial condition, and they turned out to be the key to definability in $\mathcal D_e$. The basic example comes from Jockusch's semi-computable sets, sets that can be decided between any two candidates.

## Semi-computable sets

:::definition[Jockusch]{#def-semi-computable}
A set $A$ is **semi-computable** if there is a total computable function $s$, a **selector**, such that for all $x$ and $y$: $s(x, y) \in \{ x, y \}$, and if $x \in A$ or $y \in A$, then $s(x, y) \in A$.
:::

A selector does not decide whether $x$ is in $A$; it only says which of two numbers is "more likely" to be in $A$, with the guarantee that it never picks an outsider when an element is offered.

:::example{#ex-left-cuts}
Let $\preceq$ be a computable linear order on $\nat$, and $A$ a left cut: if $y \in A$ and $x \preceq y$, then $x \in A$. Then $A$ is semi-computable, with the selector $s(x, y) = $ the $\preceq$-smaller of $x$ and $y$: if one of them is in $A$, the smaller one is. For instance, for a real $x \in (0, 1)$ that is not a dyadic rational, the set $L_x$ of (codes of) dyadic rationals below $x$ is a left cut of the computable order of the dyadic rationals, hence semi-computable. And $L_x \equiv_T X$, where $X$ is the binary expansion of $x$: the digits of $x$ are found by bisection using $L_x$, and conversely $q \in L_x$ is decided by comparing $q$ with enough digits of $x$, which differ from those of $q$ at some position since $x$ is not dyadic.
:::

Jockusch proved that every nonzero Turing degree contains a semi-computable set that is neither c.e. nor co-c.e. For the left cuts $L_x$ this is easy to see when $X$ is not computable in $\emptyset'$: if $L_x$ were c.e., $x$ would be the limit of an increasing computable sequence of rationals, hence computable in $\emptyset'$; symmetrically for the complement.

## Kalimullin pairs

:::definition[Kalimullin]{#def-k-pair}
Sets $A$ and $B$ form a **Kalimullin pair**, or **K-pair**, relative to a set $U$ if there is a set $W \leq_e U$ of pairs such that
$$
A \times B \subseteq W \qquad \text{and} \qquad \overline A \times \overline B \subseteq \overline W.
$$
A K-pair is a K-pair relative to $\emptyset$, that is, with $W$ c.e.
:::

The set $W$ separates the pairs taken in $A$ and $B$ from the pairs taken outside both. A K-pair is **trivial** if one of the sets is c.e. relative to $U$.

:::example{#ex-k-pairs}
1. If $A$ is c.e., then $A$ and any $B$ form a K-pair, with $W = A \times \nat$: it contains $A \times B$ and is disjoint from $\overline A \times \overline B$. These are the trivial K-pairs.
2. If $A$ is semi-computable with selector $s$, then $A$ and $\overline A$ form a K-pair, with the computable set $W = \{ (x, y) : s(x, y) = x \}$. If $x \in A$ and $y \notin A$, then $s(x, y) \in A$, so $s(x, y) = x$ and $(x, y) \in W$. If $x \notin A$ and $y \in A$, that is, $(x, y) \in \overline A \times \overline{\overline A}$, then $s(x, y) = y \neq x$, and $(x, y) \notin W$.
:::

The structural content of K-pairs is the following theorem; we prove the direction from the combinatorial condition to the degree-theoretic property, which is the one used in the applications of this course.

:::theorem[Kalimullin]{#thm-kalimullin-pairs}
Sets $A$ and $B$ form a K-pair relative to $U$ if and only if their degrees $\mathbf a$, $\mathbf b$, $\mathbf u$ satisfy: for every degree $\mathbf x \geq \mathbf u$, the meet $(\mathbf a \vee \mathbf x) \wedge (\mathbf b \vee \mathbf x)$ exists and equals $\mathbf x$.
:::

A pair satisfying the condition on degrees is a **robust minimal pair relative to $\mathbf u$**: above every $\mathbf x \geq \mathbf u$, joining with $\mathbf a$ and with $\mathbf b$ gives two degrees whose only common lower bounds are below $\mathbf x$.

**Intuition.** Suppose that a set $Z$ is enumerated both from $A \oplus X$ and from $B \oplus X$. To enumerate $Z$ from $X$ alone, guess finite pieces $F$ of $A$ and $G$ of $B$ that would enumerate $z$, and accept the guess only if $F \times G \subseteq W$. A wrong guess cannot have both pieces wrong: if some element of $F$ is outside $A$ and some element of $G$ outside $B$, the pair they form is outside $W$. So one of the two guesses is correct, and either way $z \in Z$.

:::proof[Proof of one direction]{of=thm-kalimullin-pairs}
Let $W \leq_e U$ witness that $A$ and $B$ form a K-pair relative to $U$, and let $X$ be a set with $U \leq_e X$. Then $A \oplus X$ and $B \oplus X$ are upper bounds of $\deg_e(X)$ joined with $\mathbf a$ and $\mathbf b$. Let $Z$ be a set with $Z = \Gamma(A \oplus X)$ and $Z = \Delta(B \oplus X)$; we show that $Z \leq_e X$, so that $\mathbf x$ is the greatest common lower bound. Let $Z^*$ be the set of $z$ for which there are finite sets $F$ and $G$ with
$$
z \in \Gamma(F \oplus X), \qquad z \in \Delta(G \oplus X), \qquad F \times G \subseteq W.
$$
Then $Z^* \leq_e X \oplus W \leq_e X$: the three conditions are positive conditions on $X$ and on $W$, checked on finite sets.

$Z \subseteq Z^*$: if $z \in Z$, compactness gives finite $F \subseteq A$ and $G \subseteq B$ with $z \in \Gamma(F \oplus X)$ and $z \in \Delta(G \oplus X)$, and $F \times G \subseteq A \times B \subseteq W$.

$Z^* \subseteq Z$: let $F$ and $G$ witness $z \in Z^*$. If $F \not\subseteq A$ and $G \not\subseteq B$, pick $f \in F \setminus A$ and $g \in G \setminus B$: then $(f, g) \in \overline A \times \overline B \subseteq \overline W$, contradicting $F \times G \subseteq W$. So $F \subseteq A$, and $z \in \Gamma(A \oplus X) = Z$, or $G \subseteq B$, and $z \in \Delta(B \oplus X) = Z$.

So $Z = Z^* \leq_e X$. The converse direction, from the degree condition to the existence of $W$, is due to Kalimullin and is admitted.
:::

:::quiz[Kalimullin pairs]
In the proof, why may $Z^*$ be enumerated from $X$ alone, although $W$ is only enumeration reducible to $U$?

- [x] $U \leq_e X$, so $W \leq_e X$, and the conditions defining $Z^*$ only use positive information about $W$: that finitely many pairs belong to it.
- [ ] Because $W$ is c.e.

  It is c.e. only in the unrelativized case; in general it is reducible to $U$, which suffices since $U \leq_e X$.
- [ ] Because $F$ and $G$ are finite.

  Finiteness makes the search possible; reducibility of $W$ to $X$ makes the test possible.

---

Where is the second condition, $\overline A \times \overline B \subseteq \overline W$, used?

- [x] To exclude a wrong guess in which both $F$ and $G$ contain an element outside their sets: such a pair of elements would lie outside $W$.
- [ ] To show that $Z \subseteq Z^*$.

  That inclusion uses the first condition, $A \times B \subseteq W$.
- [ ] To make $Z^*$ enumeration reducible to $X$.

  Reducibility comes from the form of the conditions; correctness comes from the second condition.
:::

Taking $\mathbf x = \mathbf 0_e$ and $U = \emptyset$, the degrees of a K-pair form a minimal pair: their only common lower bound is $\mathbf 0_e$. The theorem says much more: the property survives the join with any degree. In the Turing degrees, there is no such pair of nonzero degrees: by the Posner–Robinson theorem, for nonzero Turing degrees $\mathbf a$ and $\mathbf b$ there is $\mathbf g$ with $\mathbf a \vee \mathbf g = \mathbf b \vee \mathbf g = \mathbf g'$ (Soskova's survey, Section 3.1).

By :ref{#ex-k-pairs} and the remark after :ref{#ex-left-cuts}, for every set $X$ not computable in $\emptyset'$, the total degree $\iota(\deg_T X)$ is the join of the nontrivial K-pair formed by the degrees of $L_x$ and of its complement. With Jockusch's theorem, every nonzero total degree is the join of a nontrivial K-pair. The converse is not known to hold in this form: Kalimullin showed that the K-pairs are much more varied than the pairs given by semi-computable sets, and Andrews et al. showed that the joins of nontrivial K-pairs form a definable class of cototal degrees containing the total degrees. The definition of totality needs more: maximal K-pairs, in the next lesson.

::::exercise{#ex-k-pair-downward difficulty=1 objective="Check that the combinatorial condition defining K-pairs is preserved downwards."}
Let $A$ and $B$ form a K-pair, witnessed by a c.e. set $W$, and let $A_1 = \Gamma(A)$ and $B_1 = \Delta(B)$ for enumeration operators $\Gamma$ and $\Delta$. Show that $A_1$ and $B_1$ form a K-pair.

:::solution
Let $W_1$ be the set of pairs $(x, y)$ such that there are finite sets $F$ and $G$ with $x \in \Gamma(F)$, $y \in \Delta(G)$ and $F \times G \subseteq W$; it is c.e. If $x \in A_1$ and $y \in B_1$, compactness gives $F \subseteq A$ and $G \subseteq B$, and $F \times G \subseteq W$: so $(x, y) \in W_1$. If $x \notin A_1$ and $y \notin B_1$ and $(x, y) \in W_1$ with witnesses $F$ and $G$, then $F \not\subseteq A$ (otherwise $x \in \Gamma(A)$) and $G \not\subseteq B$, and an element of $F \setminus A$ with an element of $G \setminus B$ gives a pair in $\overline A \times \overline B$ inside $W$: a contradiction. So $W_1$ witnesses that $A_1$ and $B_1$ form a K-pair.
:::
::::

## Notes and references

Semi-computable sets were introduced by Jockusch (1968), who characterized them as the left cuts of computable linear orders and proved that every Turing degree contains one that is neither c.e. nor co-c.e. Arslanov, Cooper and Kalimullin (2003) observed that a semi-computable set and its complement form a robust minimal pair; Kalimullin (2003) introduced K-pairs and proved :ref{#thm-kalimullin-pairs}. The presentation follows Soskova's survey, Section 3.1.

- C. G. Jockusch, Jr., *Semirecursive sets and positive reducibility*, Transactions of the American Mathematical Society 131 (1968), 420–436.
- M. M. Arslanov, S. B. Cooper and I. Sh. Kalimullin, *Splitting properties of total enumeration degrees*, Algebra and Logic 42 (2003), 1–13.
- I. Sh. Kalimullin, *Definability of the jump operator in the enumeration degrees*, Journal of Mathematical Logic 3 (2003), 257–267.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Section 3.1.

:::::exercises
::::exercise{#ex-semi-computable-complement difficulty=1 objective="Check that semi-computability is preserved by complementation."}
Show that the complement of a semi-computable set is semi-computable.

:::solution
Let $s$ be a selector for $A$, and let $s'(x, y) = y$ if $x \neq y$ and $s(x, y) = x$, and $s'(x, y) = x$ otherwise; so $s'$ picks the element that $s$ rejects. Suppose $x \notin A$ (the case $y \notin A$ is symmetric). If $y \in A$, then $s(x, y) = y$, so $s'(x, y) = x \in \overline A$. If $y \notin A$, both candidates are in $\overline A$. So $s'$ is a selector for $\overline A$.
:::
::::

::::exercise{#ex-k-pair-comparable difficulty=1 objective="Use the minimal pair property of K-pairs to show that comparable K-pairs are trivial."}
Let $A$ and $B$ form a K-pair with $A \leq_e B$. Show that $A$ is c.e.

:::solution
By :ref{#thm-kalimullin-pairs} with $U = X = \emptyset$, the meet of $\mathbf a$ and $\mathbf b$ is $\mathbf 0_e$. Since $\mathbf a \leq \mathbf b$, this meet is $\mathbf a$; so $\mathbf a = \mathbf 0_e$ and $A$ is c.e.
:::
::::
:::::
