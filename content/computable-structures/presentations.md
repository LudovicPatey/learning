---
title: Presentations of structures
summary: Countable structures presented on the natural numbers; the atomic diagram and the Turing degree of a presentation; computable structures and examples; two computable copies of the same structure need not be computably isomorphic; presentations on subsets of ℕ, congruence presentations and pull-backs of enumerations; Knight's theorem that a non-trivial structure has presentations of every degree above a given one.
duration: 35
prerequisites: [turing-degrees/turing-reducibility, fundamentals/ce-sets]
---

Computability theory studies sets of natural numbers. To study the complexity of a countable structure, such as a group, a field, a graph or a linear order, one places it on the natural numbers. There are many ways of doing so, and they can have very different computational properties, although they describe the same structure up to isomorphism. The interplay between the properties of presentations, which are computational, and the properties of isomorphism types, which are structural, is the main theme of computable structure theory. This lesson sets up the basic objects and proves a first theorem of this kind, due to Knight: the presentations of a non-trivial structure reach every degree above one of them.

All structures are countable. A **vocabulary** $\tau$ is a set of relation, function and constant symbols, each with an arity; a vocabulary is **computable** if the set of its symbols, with their arities, is computable. A $\tau$-structure $\mathcal A$ consists of a domain $A$ and interpretations of the symbols. A vocabulary is **relational** if it has only relation symbols. A function symbol of arity $n$ can be replaced by a relation symbol of arity $n + 1$ for its graph, and a constant by a unary relation; for computational purposes this changes nothing (:ref{#ex-relational-diagram}), and we often assume the vocabulary relational.

## Presentations and atomic diagrams

:::definition{#def-omega-presentation}
An **ω-presentation** is a structure whose domain is $\nat$. An ω-presentation of a structure $\mathcal A$, or a **copy** of $\mathcal A$, is an ω-presentation isomorphic to $\mathcal A$.

Fix an effective list $(\varphi^{\mathrm{at}}_i)_{i \in \nat}$ of the atomic $\tau$-formulas with variables among $x_0, x_1, \ldots$. The **atomic diagram** of an ω-presentation $\mathcal M$ is the set
$$
D(\mathcal M) = \{ i : \mathcal M \models \varphi^{\mathrm{at}}_i[x_j \mapsto j \text{ for all } j] \},
$$
the set of atomic facts true of the elements of $\mathcal M$, each element $j$ naming itself. The **Turing degree** of $\mathcal M$ is the degree of $D(\mathcal M)$, and $\mathcal M$ is **computable** if $D(\mathcal M)$ is computable. A structure is **computable**, or **computably presentable**, if it has a computable copy.
:::

Equivalently, $\mathcal M$ is computable if its relations, functions and constants are uniformly computable: the atomic diagram computes them, and conversely they decide every atomic formula. When we say that $\mathcal M$ is computable in $X$, low, or $\Delta^0_2$, we mean $D(\mathcal M)$.

:::example{#ex-computable-structures}
1. The ordered set $(\mathbb Q; <)$, coded by any computable bijection between $\mathbb Q$ and $\nat$, the group $(\mathbb Z; +)$, and the field $(\mathbb Q; +, \times)$ are computable structures.
2. The $\mathbb Q$-vector space of countable dimension, presented as the finitely supported sequences of rationals, is computable; so is every $\mathbb Q$-vector space of finite dimension.
3. For $X \subseteq \nat$, let $G_X = \bigoplus_{i \in X} \mathbb Z_{p_i}$, where $p_i$ is the $i$-th prime and $\mathbb Z_p$ the cyclic group of order $p$. If $X$ is c.e., $G_X$ is computable: enumerate $X$ and add a new generator of order $p_i$ when $i$ appears. Conversely, if $G_X$ has a computable copy, $X$ is c.e., since $i \in X$ if and only if some element has order $p_i$, which a search through the copy detects. So $G_X$ is computably presentable exactly when $X$ is c.e.
:::

A structure has, in general, many different computable copies, and they need not behave alike.

:::proposition{#prop-two-copies-omega}
There is a computable copy $\mathcal M$ of the linear order $\omega = (\nat; \leq)$ such that the successor function of $\mathcal M$ computes $\emptyset'$. Consequently, $\mathcal M$ is not computably isomorphic to $(\nat; \leq)$.
:::

:::proof{of=prop-two-copies-omega}
Let $k_0, k_1, \ldots$ be a computable injective enumeration of $\emptyset'$. Order the even numbers as usual: $2n \leq_{\mathcal M} 2m$ if $n \leq m$. Place the odd number $2s + 1$ between $2k_s$ and $2k_s + 2$, and order two odd numbers $2s + 1$, $2t + 1$ as $k_s$ and $k_t$ are ordered. The relation $\leq_{\mathcal M}$ is computable: $2n <_{\mathcal M} 2s + 1$ if and only if $n \leq k_s$. Every element has finitely many predecessors ($2n$ has at most $2n$, and $2s + 1$ at most $2k_s + 2$), and the order is linear and infinite without a last element, so it is isomorphic to $\omega$.

In $\mathcal M$, the successor of $2n$ is $2n + 2$ if and only if no odd number lies between them, that is, if and only if $n \notin \emptyset'$. So the successor function of $\mathcal M$ computes $\emptyset'$. In $(\nat; \leq)$ the successor function is computable. A computable isomorphism $f : (\nat; \leq) \to \mathcal M$ would make the successor of $\mathcal M$ computable, as $f \circ \mathrm{succ} \circ f^{-1}$.
:::

So the computable copies of one structure may be computationally different, because the isomorphisms between them are not computable. The questions "which structures have a computable copy" and "how different can two computable copies be" are the subjects of degree spectra and of computable categoricity, later in the track.

## Variants of presentations

Three variants simplify constructions; they change nothing essential.

*Presentations on subsets of ℕ.* A $(\subseteq\omega)$-presentation has a domain $M \subseteq \nat$; its atomic diagram is defined as before, with the formulas mentioning elements outside $M$ declared false, and it computes $M$. If $M = \{ m_0 < m_1 < \cdots \}$ is infinite, the bijection $i \mapsto m_i$ gives an ω-presentation computable in $D(\mathcal M)$. Finite structures are presented on initial segments of $\nat$.

*Congruence presentations.* A congruence ω-presentation interprets equality by an equivalence relation $=^{\mathcal M}$ compatible with the other symbols. Its quotient has an ω-presentation computable in $D(\mathcal M)$, with the least element of each class as representative, if there are infinitely many classes. For instance, if $R$ is a computable ring and $I$ a computable ideal, $R/I$ has a computable presentation.

*Pull-backs.* Let $\tau$ be relational. An **enumeration** of a structure $\mathcal M$ is a surjection $g : \nat \to M$. Its **pull-back** $g^{-1}(\mathcal M)$ is the congruence ω-presentation with $a \sim b \iff g(a) = g(b)$ and $R^{g^{-1}(\mathcal M)} = g^{-1}(R^{\mathcal M})$; it is an ω-presentation if $g$ is injective, and it is computable in $g \oplus D(\mathcal M)$. Most constructions of copies build an enumeration step by step, as a union of finite tuples $\bar p_0 \subseteq \bar p_1 \subseteq \cdots$ of elements of $\mathcal M$. The atomic diagram of the pull-back is then the union of the atomic diagrams of the tuples: writing $D_{\mathcal M}(\bar p)$ for the finite string recording the atomic facts true of $\bar p$ in $\mathcal M$ (in the first symbols of the vocabulary), we have $D(g^{-1}(\mathcal M)) = \bigcup_s D_{\mathcal M}(\bar p_s)$.

:::lemma{#lem-ce-substructure}
Let $\mathcal A$ be a computable structure in a relational vocabulary, and $M \subseteq A$ an infinite c.e. set. The substructure of $\mathcal A$ with domain $M$ has a computable copy.
:::

:::proof{of=lem-ce-substructure}
Let $g$ be a computable injective enumeration of $M$. The pull-back $g^{-1}(\mathcal M)$ is an ω-presentation, computable in $g \oplus D(\mathcal A)$, hence computable, and $g$ is an isomorphism onto the substructure.
:::

The vocabulary must be relational: in a structure with functions, the substructure generated by $M$ may be larger than $M$.

## Knight's theorem

A structure is **trivial** if some finite tuple $\bar c$ is such that every permutation of the domain fixing $\bar c$ is an automorphism. For example, a set with finitely many distinguished elements and no other structure is trivial, while $(\nat; \leq)$ is not. All copies of a trivial structure are computably isomorphic, up to the finite tuple, and in a finite vocabulary they are all computable. The other structures can code any set into their copies.

:::theorem[Knight]{#thm-knight-coding}
Let $\mathcal M$ be a non-trivial structure with an ω-presentation computable in a set $X$. Then $\mathcal M$ has an ω-presentation of Turing degree exactly that of $X$.
:::

**Intuition.** Build the copy as the pull-back of an $X$-computable enumeration, so that the copy is computable in $X$. To make it compute $X$, code the bit $X(s)$ at stage $s$ by the order in which two elements with different atomic types are listed: the atomic diagram of the copy then reveals which came first. Non-triviality guarantees that such elements, or at least such tuples, exist after any finite stage.

:::proof{of=thm-knight-coding}
We may assume $\tau$ relational. We build an $X$-computable injective enumeration $g = \bigcup_s \bar p_s$ of $\mathcal M$ and let $\mathcal A = g^{-1}(\mathcal M)$, which is computable in $X$. Let $\bar p_0$ be empty.

*Stage $s + 1$.* Since $\mathcal M$ is non-trivial, some permutation fixing $\bar p_s$ is not an automorphism, so there are tuples $\bar a$, $\bar b$ of the same length, disjoint from $\bar p_s$, with $D_{\mathcal M}(\bar p_s \bar a) \neq D_{\mathcal M}(\bar p_s \bar b)$. They can be taken disjoint from each other: a third tuple disjoint from both has a diagram different from that of $\bar a$ or of $\bar b$, and replaces the other one. Search, with oracle $X$, for such a pair, of some length $h$, and truncate it so that it is **minimal**: the diagrams of $\bar p_s a_0 \ldots a_{i-1}$ and $\bar p_s b_0 \ldots b_{i-1}$ agree for $i < h$. Name them so that $D_{\mathcal M}(\bar p_s \bar a)$ is lexicographically smaller. If $X(s) = 0$, let $\tilde p = \bar p_s a_0 b_0 a_1 b_1 \ldots a_{h-1} b_{h-1}$; if $X(s) = 1$, let $\tilde p = \bar p_s b_0 a_0 \ldots b_{h-1} a_{h-1}$. Finally let $\bar p_{s+1} = \tilde p\, c$, where $c$ is the least element of $M$ not in $\tilde p$, so that $g$ is onto.

*Decoding.* Let $k_s = |\bar p_s|$, and write $D_{\mathcal A}(n_0, \ldots, n_{r-1})$ for the diagram of a tuple of elements of $\mathcal A$. Given $k_s$, the number $k_{s+1}$ is computable from $D(\mathcal A)$: it is $k_s + 2h + 1$ for the least $h \geq 1$ such that
$$
D_{\mathcal A}(0, \ldots, k_s - 1, k_s, k_s + 2, \ldots, k_s + 2h - 2) \neq D_{\mathcal A}(0, \ldots, k_s - 1, k_s + 1, k_s + 3, \ldots, k_s + 2h - 1),
$$
by the minimality of the pair: the first tuple lists $g(k_s), g(k_s + 2), \ldots$, one of $\bar a$ and $\bar b$, the second the other one. And $X(s) = 0$ if and only if the first of these two strings is lexicographically smaller. So $X \leq_T D(\mathcal A)$, by recursion on $s$.
:::

:::quiz[Knight's theorem]
Why are the two tuples interleaved, $a_0 b_0 a_1 b_1 \ldots$, rather than listed one after the other?

- [x] So that the decoder, who sees only the atomic diagram of the copy, knows where each tuple sits: the elements of even offset form one tuple and those of odd offset the other, and the minimality of the pair tells him when to stop comparing.
- [ ] Because the two tuples are not disjoint.

  They are chosen disjoint; the interleaving concerns their positions in the copy, not their elements.
- [ ] To make the enumeration onto.

  Surjectivity comes from adding the least missing element at each stage.

---

Where is the non-triviality of $\mathcal M$ used?

- [x] To guarantee, at every stage, two tuples outside $\bar p_s$ with different diagrams over $\bar p_s$; without them, no bit could be coded after $\bar p_s$.
- [ ] To make the copy computable in $X$.

  The copy is computable in $X$ because the enumeration is; this holds for every structure computable in $X$.
- [ ] To make the copy isomorphic to $\mathcal M$.

  Every pull-back of an enumeration of $\mathcal M$ is isomorphic to $\mathcal M$ when the enumeration is injective.
:::

So the set of Turing degrees of the copies of a non-trivial structure, its **degree spectrum**, is closed upwards. A structure is computable when $\mathbf 0$ is in its spectrum; Knight's theorem says the spectrum is then the set of all degrees. The course on degree spectra studies which sets of degrees arise.

::::exercise{#ex-group-copy-degree difficulty=1 objective="Combine the example of the groups G_X with Knight's theorem to describe the degrees of the copies of a structure."}
Let $X$ be an infinite c.e. set and $G_X = \bigoplus_{i \in X} \mathbb Z_{p_i}$. Show that the Turing degrees of the copies of $G_X$ are exactly all the degrees. What happens if $X$ is not c.e.? Show that every copy of $G_X$ computes a function enumerating $X$.

:::solution
If $X$ is finite, $G_X$ is a finite group, presented on a finite initial segment of $\nat$, and all its copies are computable; assume $X$ infinite. Then $G_X$ is computable by :ref{#ex-computable-structures} (3), and it is not trivial: given a finite tuple, there are two non-zero elements outside the subgroup it generates with different orders $p_i \neq p_j$, and a permutation exchanging them and fixing everything else is not an automorphism. Every set computes the computable copy, so by Knight's theorem there are copies of every degree. If $X$ is not c.e., $G_X$ has no computable copy, so $\mathbf 0$ is not in the spectrum. In every copy, searching for elements of order $p_i$ enumerates $X$: the copy computes the function listing, in order of discovery, the indices $i$ for which an element of order $p_i$ has been found.
:::
::::

## Notes and references

The notions of this lesson follow Montalbán, *Computable Structure Theory: Within the Arithmetic*, Chapter I (Definitions I.1 and I.2, Observation I.3, Lemmas I.11 and I.14, Section I.1.7, Theorem I.16), and Ash and Knight, Chapter 3 (Sections 3.14 and 3.16). The example of the two copies of $\omega$ goes back to the early codings of sets into linear orders; Montalbán, Section I.1.2, cites Marker (1982). Knight's theorem is from Knight (1986); it was the starting point of the study of degree spectra.

- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Cambridge University Press, 2021 (draft of 2019 used here), Chapter I.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Elsevier, 2000, Chapter 3.
- J. F. Knight, *Degrees coded in jumps of orderings*, Journal of Symbolic Logic 51 (1986), 1034–1042.

:::::exercises
::::exercise{#ex-relational-diagram difficulty=1 objective="Check that replacing functions by their graphs does not change the degree of a presentation."}
Let $\mathcal M$ be an ω-presentation of a structure with a binary function symbol $f$, and $\tilde{\mathcal M}$ the same presentation with $f$ replaced by a ternary relation $R_f(x, y, z) \iff f(x, y) = z$. Show that $D(\mathcal M) \equiv_T D(\tilde{\mathcal M})$.

:::solution
From $D(\mathcal M)$, decide $R_f(a, b, c)$ by the atomic formula $f(x_a, x_b) = x_c$. Conversely, from $D(\tilde{\mathcal M})$, compute $f(a, b)$ by searching for the $c$ with $R_f(a, b, c)$, which exists and is unique; then every term built from $f$ can be evaluated, and every atomic formula of the original vocabulary, of the form $t_1 = t_2$ or $R(t_1, \ldots)$, can be decided by evaluating its terms.
:::
::::

::::exercise{#ex-finite-sizes difficulty=2 objective="See why finite structures are presented on initial segments of ℕ, by showing that sizes are not computable from presentations on arbitrary subsets."}
Build a computable sequence of finite structures $(\mathcal M_n)$, each presented on a finite subset $M_n \subseteq \nat$ (the sets $M_n$ and the relations being uniformly computable), such that no computable function gives the size of $\mathcal M_n$ from $n$.

:::solution
Let $M_n = \{ 0 \} \cup \{ \langle n, s \rangle + 1 : \Phi_n(n) \text{ halts at exactly stage } s \}$, with the empty vocabulary. Each $M_n$ has $1$ or $2$ elements and is uniformly computable: to decide whether $\langle n, s \rangle + 1 \in M_n$, run $\Phi_n(n)$ for $s$ steps. The size of $M_n$ is $2$ if and only if $n \in \emptyset'$, so a computable function giving the sizes would decide the halting problem.
:::
::::

::::exercise{#ex-trivial-copies difficulty=1 objective="Check that copies of a trivial structure in a finite vocabulary are all computable."}
Let $\mathcal M$ be a trivial structure in a finite relational vocabulary, with a tuple $\bar c$ such that every permutation fixing $\bar c$ is an automorphism. Show that every copy of $\mathcal M$ is computable.

:::solution
Let $\mathcal B$ be a copy, and $\bar d$ the image of $\bar c$ in it; every permutation of $B$ fixing $\bar d$ is an automorphism of $\mathcal B$. For a relation symbol $R$ of arity $k$ and a $k$-tuple $\bar e$ of elements, whether $R(\bar e)$ holds depends only on the pattern of $\bar e$: which coordinates are equal to each other and which are equal to which element of $\bar d$. Indeed, two tuples with the same pattern are mapped to each other by a permutation fixing $\bar d$. There are finitely many patterns for each arity, and finitely many symbols, so the whole structure is described by a finite table, together with the finite tuple $\bar d$. Both are finite data, so $D(\mathcal B)$ is computable.
:::
::::
:::::
