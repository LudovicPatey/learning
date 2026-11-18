---
title: Enumeration operators
summary: Enumeration reducibility, defined by c.e. sets of axioms; enumeration operators are monotone and compact; the enumeration degrees, their least element and joins; c.e. in as enumeration reducibility to a set and its complement; total sets and the embedding of the Turing degrees.
duration: 30
prerequisites: [turing-degrees/turing-reducibility, fundamentals/ce-sets]
---

Turing reducibility uses an oracle that answers questions: is $n$ in $B$, yes or no. In many situations only half of this information is available. A c.e. set is given by an enumeration, which eventually confirms that $n$ belongs to it but never confirms that $n$ does not. The existential type of a tuple in a structure is given in the same way, by the witnesses that a copy can find. Enumeration reducibility is the notion of relative computability adapted to this situation: $A$ is enumeration reducible to $B$ if an enumeration of $B$ can be turned, by a fixed procedure, into an enumeration of $A$. The procedure may only use positive facts about $B$, finitely many at a time, and it may only produce positive facts about $A$.

## Enumeration reducibility

Let $(D_u)_{u \in \nat}$ be the canonical listing of the finite subsets of $\nat$: $D_u$ is the set whose characteristic function is the binary expansion of $u$.

:::definition[Friedberg, Rogers]{#def-enumeration-reducibility}
An **enumeration operator** is a map $\Gamma_W : \mathcal P(\nat) \to \mathcal P(\nat)$ given by a c.e. set $W$ of pairs:
$$
\Gamma_W(X) = \{ n : \exists u\, ( \langle n, u \rangle \in W \text{ and } D_u \subseteq X ) \}.
$$
A pair $\langle n, u \rangle \in W$ is an **axiom**: it says that $n$ is enumerated as soon as the finite set $D_u$ has been seen in the oracle. A set $A$ is **enumeration reducible** to $B$, written $A \leq_e B$, if $A = \Gamma_W(B)$ for some c.e. set $W$. We write $\Gamma_e$ for $\Gamma_{W_e}$.
:::

The procedure behind an operator is simple: given an enumeration $b_0, b_1, \ldots$ of $B$, at stage $s$ enumerate every $n$ such that some axiom $\langle n, u \rangle$ enumerated in $W$ by stage $s$ has $D_u \subseteq \{ b_0, \ldots, b_{s-1} \}$. Every element of $\Gamma_W(B)$ is eventually enumerated, and nothing else. The procedure does not depend on the order in which $B$ is enumerated, nor on repetitions.

:::example{#ex-enumeration-reductions}
1. A set is enumeration reducible to $\emptyset$ if and only if it is c.e.: $\Gamma_W(\emptyset) = \{ n : \langle n, 0 \rangle \in W \}$, since $D_0 = \emptyset$, and every c.e. set has this form.
2. Every c.e. set is enumeration reducible to every set, by the same operator.
3. $A \leq_e A$, and $\{ 2n : n \in A \} \leq_e A$, by the axioms $\langle n, \{n\} \rangle$ and $\langle 2n, \{n\} \rangle$, writing $\{n\}$ for the code of the singleton.
4. Let $f$ be a total function and $G_f = \{ \langle n, m \rangle : f(n) = m \}$ its graph. The range of $f$ is enumeration reducible to $G_f$, by the axioms $\langle m, \{ \langle n, m \rangle \} \rangle$. The complement of the graph is enumeration reducible to the graph: $\langle n, m \rangle \notin G_f$ if and only if $\langle n, m' \rangle \in G_f$ for some $m' \neq m$.
:::

:::proposition{#prop-operator-properties}
Let $\Gamma = \Gamma_W$ be an enumeration operator.
1. (Monotonicity) If $X \subseteq Y$, then $\Gamma(X) \subseteq \Gamma(Y)$.
2. (Compactness) $n \in \Gamma(X)$ if and only if $n \in \Gamma(F)$ for some finite $F \subseteq X$.
3. (Composition) If $\Delta$ is another enumeration operator, $\Delta \circ \Gamma$ is an enumeration operator, and an index for it is computed from indices of $\Gamma$ and $\Delta$.
4. $\Gamma(X)$ is c.e. in $X$, uniformly in $X$ and in an index of $\Gamma$.
:::

:::proof{of=prop-operator-properties}
1 and 2 are immediate from the definition: an axiom uses a finite subset of the oracle. For 3, let $V$ be the set of pairs $\langle n, u \rangle$ such that there are a finite set $D_v$ and, for each $m \in D_v$, an axiom $\langle m, u_m \rangle \in W$ with $D_{u_m} \subseteq D_u$, and an axiom $\langle n, v \rangle$ of $\Delta$. It is c.e. If $\langle n, u \rangle \in V$ and $D_u \subseteq X$, then $D_v \subseteq \Gamma(X)$ and $n \in \Delta(\Gamma(X))$. Conversely, if $n \in \Delta(\Gamma(X))$, an axiom $\langle n, v \rangle$ of $\Delta$ has $D_v \subseteq \Gamma(X)$; each $m \in D_v$ has an axiom $\langle m, u_m \rangle$ of $\Gamma$ with $D_{u_m} \subseteq X$, and the union $D_u$ of these finitely many sets gives $\langle n, u \rangle \in V$. So $\Delta \circ \Gamma = \Gamma_V$. For 4, $n \in \Gamma(X)$ if and only if some axiom $\langle n, u \rangle$ appears in $W$ with $D_u \subseteq X$, which $X$ can check.
:::

By 3, $\leq_e$ is transitive, and it is reflexive by the identity operator. The **enumeration degree** of $A$ is its class $\deg_e(A)$ under $\equiv_e$, and $\mathcal D_e$ is the partial order of the enumeration degrees.

:::proposition{#prop-e-degrees-basic}
1. The c.e. sets form the least enumeration degree, $\mathbf 0_e$.
2. $A \oplus B = \{ 2n : n \in A \} \cup \{ 2n + 1 : n \in B \}$ is a least upper bound of $A$ and $B$ for $\leq_e$, so $\mathcal D_e$ is an upper semilattice.
3. If $A \leq_e B$ and $B$ is c.e., then $A$ is c.e.
:::

:::proof{of=prop-e-degrees-basic}
1 and 3 follow from :ref{#ex-enumeration-reductions}, items 1 and 2, and from composition: if $A = \Gamma(B)$ and $B = \Gamma'(\emptyset)$, then $A = (\Gamma \circ \Gamma')(\emptyset)$ is c.e. For 2, $A$ and $B$ are reducible to $A \oplus B$ by the axioms $\langle n, \{2n\} \rangle$ and $\langle n, \{2n+1\} \rangle$. If $A = \Gamma(C)$ and $B = \Delta(C)$, then $A \oplus B$ is enumerated from $C$ by the axioms $\langle 2n, u \rangle$ for the axioms $\langle n, u \rangle$ of $\Gamma$, and $\langle 2n + 1, u \rangle$ for those of $\Delta$.
:::

:::quiz[enumeration operators]
Why is the complement of a non-computable c.e. set never enumeration reducible to the set itself?

- [x] A set enumeration reducible to a c.e. set is c.e.; if $\overline{W} \leq_e W$, then $\overline W$ is c.e., and $W$ is computable.
- [ ] Because operators are monotone.

  Monotonicity alone does not prevent a reduction; the argument uses that $W$ is c.e.
- [ ] Because $\overline W$ is infinite.

  Infinite sets can be enumeration reducible to each other; for instance $\nat \leq_e \emptyset$.

---

In the proof that composition gives an operator, why is the union of the sets $D_{u_m}$ finite?

- [x] It is a union over the finitely many elements $m$ of the finite set $D_v$, each contributing one finite set.
- [ ] Because $X$ is finite.

  $X$ is arbitrary; compactness of each axiom is what matters.
- [ ] Because $W$ is finite.

  $W$ is c.e., usually infinite; each axiom is finite.
:::

## Positive and negative information

Turing reducibility and "c.e. in" both use an oracle that gives positive and negative answers. They become enumeration reducibilities once the negative information is written positively, as membership in the complement.

:::proposition{#prop-ce-in-e}
For all sets $A$ and $B$:
1. $A$ is c.e. in $B$ if and only if $A \leq_e B \oplus \overline B$;
2. $A \leq_T B$ if and only if $A \oplus \overline A \leq_e B \oplus \overline B$.
:::

:::proof{of=prop-ce-in-e}
1. If $A = W^B_e$, then $n \in A$ if and only if the oracle machine halts on $n$ with some finite oracle string $\sigma \prec B$, that is, with the finite sets $\{ x < |\sigma| : \sigma(x) = 1 \} \subseteq B$ and $\{ x < |\sigma| : \sigma(x) = 0 \} \subseteq \overline B$. The pairs $\langle n, u \rangle$ such that $D_u$ codes these two sets inside $B \oplus \overline B$, for a halting computation, form a c.e. set of axioms. Conversely, if $A = \Gamma(B \oplus \overline B)$, then $B$ can enumerate $A$, since $B$ decides membership in $B \oplus \overline B$.
2. $A \leq_T B$ if and only if $A$ and $\overline A$ are both c.e. in $B$, by the relativized form of Post's theorem that a set is computable if and only if it and its complement are c.e. By 1, this holds if and only if $A$ and $\overline A$ are enumeration reducible to $B \oplus \overline B$, that is, by :ref{#prop-e-degrees-basic}, if and only if $A \oplus \overline A \leq_e B \oplus \overline B$.
:::

:::definition{#def-total}
A set $A$ is **total** if $\overline A \leq_e A$. An enumeration degree is **total** if it contains a total set.
:::

The sets $B \oplus \overline B$ are total, since their complement is a computable permutation of themselves. A total set $A$ satisfies $A \equiv_e A \oplus \overline A$. So the total degrees are exactly the degrees of the sets $B \oplus \overline B$. By :ref{#ex-enumeration-reductions}, the graph of a total function is total, and its degree is that of $G_f \oplus \overline{G_f}$, which has the Turing degree of $f$.

:::theorem[Myhill]{#thm-myhill-embedding}
The map $\iota(\deg_T(B)) = \deg_e(B \oplus \overline B)$ is well defined and is an embedding of the Turing degrees into the enumeration degrees, which preserves the order and the joins. Its range is the set of total degrees.
:::

:::proof{of=thm-myhill-embedding}
By :ref{#prop-ce-in-e}, item 2, $A \leq_T B$ if and only if $\iota(\deg_T A) \leq \iota(\deg_T B)$: the map is well defined, injective and order preserving. For joins, $(A \oplus B) \oplus \overline{A \oplus B}$ and $(A \oplus \overline A) \oplus (B \oplus \overline B)$ are computable permutations of each other, hence enumeration equivalent. The range consists of the degrees of the sets $B \oplus \overline B$, which are the total degrees.
:::

The least degree is total: $\mathbf 0_e = \iota(\mathbf 0)$. The degree $\iota(\mathbf 0')$ is denoted $\mathbf 0'_e$; it contains $\overline K$, since $K \oplus \overline K \equiv_e \overline K$ when $K$ is c.e. In the enumeration degrees, $\deg_e(K) = \mathbf 0_e < \deg_e(\overline K) = \mathbf 0'_e$, while $K$ and $\overline K$ have the same Turing degree. Enumeration reducibility separates a set from its complement.

Are all enumeration degrees total? Medvedev showed that they are not; a set that is neither c.e. nor total in a strong way will be built in the lesson on quasi-minimal degrees. Selman's theorem, in the next lesson, shows that the total degrees nevertheless determine the whole structure.

::::exercise{#ex-graph-degree difficulty=1 objective="Identify the enumeration degree of the graph of a function with the image of its Turing degree."}
Let $f$ be a total function. Show that $G_f \equiv_e G_f \oplus \overline{G_f}$, and that $\deg_e(G_f) = \iota(\deg_T(f))$. Conversely, show that every total degree contains the graph of a total function.

:::solution
By :ref{#ex-enumeration-reductions}, item 4, $\overline{G_f} \leq_e G_f$, so $G_f$ is total and $G_f \equiv_e G_f \oplus \overline{G_f}$. The set $G_f \oplus \overline{G_f}$ has the Turing degree of $G_f$, which is that of $f$ (the graph and the function compute each other). So $\deg_e(G_f) = \iota(\deg_T(f))$. Conversely, a total degree is $\iota(\deg_T(B))$ for some set $B$; the characteristic function $\chi_B$ is a total function of the same Turing degree, so $\deg_e(G_{\chi_B}) = \iota(\deg_T(B))$.
:::
::::

## Notes and references

Enumeration reducibility was introduced by Friedberg and Rogers (1959), in the form given here; Myhill (1961) and Selman (1971) arrived at it independently, as a natural extension of relative computability to partial functions. :ref{#thm-myhill-embedding} is due to Myhill (1961). The presentation follows Soskova's survey, Section 1.

- R. M. Friedberg and H. Rogers, Jr., *Reducibility and completeness for sets of integers*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 5 (1959), 117–125.
- J. Myhill, *Note on degrees of partial functions*, Proceedings of the American Mathematical Society 12 (1961), 519–521.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Section 1.

:::::exercises
::::exercise{#ex-e-not-t difficulty=1 objective="Compare enumeration and Turing reducibility on a c.e. set and its complement."}
Let $K$ be the halting set. Show that $K \leq_e \overline K$ and $\overline K \not\leq_e K$, although $K \equiv_T \overline K$. Show more generally that if $A$ is c.e., then $A \leq_e X$ for every $X$.

:::solution
Let $A$ be c.e. The operator with the axioms $\langle n, 0 \rangle$ for $n \in A$ is given by a c.e. set of axioms, and it outputs $A$ on every oracle $X$, since $D_0 = \emptyset \subseteq X$; so $A \leq_e X$, and in particular $K \leq_e \overline K$. If $\overline K \leq_e K$, then $\overline K$ would be c.e. by :ref{#prop-e-degrees-basic}, item 3, and $K$ would be computable. The Turing equivalence holds since a set and its complement compute each other.
:::
::::

::::exercise{#ex-operator-not-uniform-union difficulty=2 objective="See that enumeration operators commute with increasing unions but not with complements."}
Let $\Gamma$ be an enumeration operator. Show that $\Gamma(\bigcup_i X_i) = \bigcup_i \Gamma(X_i)$ for every increasing sequence $X_0 \subseteq X_1 \subseteq \cdots$. Give an operator $\Gamma$ and a set $X$ with $\Gamma(\overline X) \neq \overline{\Gamma(X)}$.

:::solution
By monotonicity, $\Gamma(X_i) \subseteq \Gamma(\bigcup_i X_i)$. Conversely, if $n \in \Gamma(\bigcup_i X_i)$, an axiom $\langle n, u \rangle$ has $D_u \subseteq \bigcup_i X_i$; since $D_u$ is finite and the sequence is increasing, $D_u \subseteq X_i$ for some $i$, and $n \in \Gamma(X_i)$. For the second part, take the operator with the axioms $\langle n, 0 \rangle$ for all $n$, which outputs $\nat$ on every oracle: for any $X$, $\Gamma(\overline X) = \nat \neq \emptyset = \overline{\Gamma(X)}$. Operators only transform positive information; they do not commute with complementation.
:::
::::

::::exercise{#ex-total-closure difficulty=1 objective="Check the closure properties of total sets under join."}
Show that if $A$ and $B$ are total, then $A \oplus B$ is total, and that the join of two total degrees is total.

:::solution
If $\overline A = \Gamma(A)$ and $\overline B = \Delta(B)$, then $\overline{A \oplus B} = \overline A \oplus \overline B$ is enumerated from $A \oplus B$ by applying $\Gamma$ to the even part and $\Delta$ to the odd part. So $A \oplus B$ is total, and $\deg_e(A) \vee \deg_e(B) = \deg_e(A \oplus B)$ is total.
:::
::::
:::::
