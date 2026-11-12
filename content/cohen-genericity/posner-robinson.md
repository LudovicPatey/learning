---
title: The Posner–Robinson theorem
summary: Coding a set into a 1-generic set so that it can be decoded with any non-computable set; the Posner–Robinson join theorem and Friedberg's jump inversion theorem.
duration: 40
prerequisites: [one-genericity]
---

Genericity is usually a tool for building sets with few computational abilities. Combined with **coding**, it also produces sets with prescribed strength. The idea is to build a 1-generic set $G$ that carries a given set $Z$ in its bits, in such a way that the coding can be read back with the help of an arbitrary non-computable set $A$. The resulting theorem, in the form given by Jockusch and Shore, has two classical consequences: the Posner–Robinson theorem, which says that every non-computable set joins with some set to compute the jump of the latter, and Friedberg's jump inversion theorem, admitted in the course on Turing degrees, which says that every degree above $\obf'$ is a jump.

The construction combines two techniques already met: the finite extension construction of a 1-generic set computable in $\emptyset'$ (:ref{#prop-1-generic}), and the coding of a set into the bits of a set built by finite extensions, as in the proof of the jump inversion theorem given by Soare (2016, Theorem 6.4.1). The difficulty lies in the decoding. To read $Z(e)$ from $G$, one must know where the block of step $e$ begins, hence how step $e - 1$ ended: by meeting $W_{e-1}$, after a search for an extension, or by avoiding it. Distinguishing the two cases is a $\Sigma^0_1$ question, answered by $\emptyset'$ but not by $G$. The construction arranges that the oracle $A$ answers it instead.

:::theorem[Jockusch–Shore]{#thm-jockusch-shore}
Let $A$ and $Z$ be sets, with $A$ not computable. There is a 1-generic set $G$ such that $Z \leq_T A \oplus G$, $Z \leq_T G \oplus \emptyset'$, and $G \leq_T A \oplus Z \oplus \emptyset'$.
:::

## The construction

We may assume that $A$ is not c.e. Indeed, if $A$ is c.e., then its complement is not c.e., since $A$ is not computable; and the complement is Turing equivalent to $A$, so it can replace $A$ in the statement. Fix an enumeration $(W_e)$ of the c.e. sets of strings.

We build strings $\sigma_0 \preceq \sigma_1 \preceq \cdots$, starting with $\sigma_0 = \varepsilon$, and let $G$ be their limit. At step $e$, given $\sigma_e$, write $i = Z(e)$ and consider the set
$$
D_e = \{ m : \text{some extension of } \sigma_e\, i\, 0^m\, 1 \text{ belongs to } W_e \}.
$$
It is c.e. Since $A$ is not c.e., $A \neq D_e$; so there is $m$ with either $m \in D_e \setminus A$ or $m \in A \setminus D_e$. Let $m$ be the least such number.

- If $m \in D_e \setminus A$, let $\sigma_{e+1}$ be the first extension of $\sigma_e\, i\, 0^m\, 1$ enumerated into $W_e$. Then $G$ meets $W_e$.
- If $m \in A \setminus D_e$, let $\sigma_{e+1} = \sigma_e\, i\, 0^m\, 1$. Then no extension of $\sigma_{e+1}$ belongs to $W_e$: $\sigma_{e+1}$ avoids $W_e$.

:::figure[Step $e$ of the construction. After $\sigma_e$, the block consists of the coded bit $i = Z(e)$, a run of $m$ zeros and a $1$. In case 1 it is extended to the first string of $W_e$ found above it; in case 2 it is left as it is, and avoids $W_e$. The run of zeros tells the decoder the number $m$, and the oracle $A$ tells it which case occurred.]
<svg class="fig" viewBox="0 0 600 196" width="600" role="img" aria-label="The block added at step e: the string sigma_e, the bit Z(e), m zeros and a one; in the first case it is extended further to a string of W_e"><defs><marker id="js-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><rect x="20" y="30" width="96" height="24" class="cell"/><text x="68" y="47" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">e</tspan></text><rect x="116" y="30" width="24" height="24" class="cell head-cell"/><text x="128.0" y="47" text-anchor="middle" class="mrm" font-size="13">i</text><rect x="140" y="30" width="24" height="24" class="cell"/><text x="152.0" y="47" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="164" y="30" width="24" height="24" class="cell"/><text x="176.0" y="47" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="188" y="30" width="24" height="24" class="cell"/><text x="200.0" y="47" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="212" y="30" width="24" height="24" class="cell"/><text x="224.0" y="47" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="236" y="30" width="24" height="24" class="cell"/><text x="248.0" y="47" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="260" y="30" width="24" height="24" class="cell"/><text x="272.0" y="47" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="284" y="30" width="24" height="24" class="cell"/><text x="296.0" y="47" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="308" y="30" width="24" height="24" class="cell" stroke-dasharray="3 3"/><rect x="332" y="30" width="24" height="24" class="cell" stroke-dasharray="3 3"/><rect x="356" y="30" width="24" height="24" class="cell" stroke-dasharray="3 3"/><rect x="380" y="30" width="24" height="24" class="cell" stroke-dasharray="3 3"/><rect x="404" y="30" width="24" height="24" class="cell" stroke-dasharray="3 3"/><text x="368.0" y="47" text-anchor="middle" class="math" font-size="15">τ</text><text x="440" y="46" class="label">m ∈ D<tspan font-size="9" dy="3">e</tspan><tspan dy="-3"> ∖ A</tspan></text><path d="M309,58 L309,64 L427,64 L427,58" class="muted-stroke" stroke-width="1.2"/><text x="368.0" y="80" text-anchor="middle" class="label">up to a string of W<tspan font-size="9" dy="3">e</tspan></text><path d="M141,58 L141,64 L283,64 L283,58" class="muted-stroke" stroke-width="1.2"/><text x="212.0" y="80" text-anchor="middle" class="label">m zeros</text><rect x="20" y="118" width="96" height="24" class="cell"/><text x="68" y="135" text-anchor="middle" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">e</tspan></text><rect x="116" y="118" width="24" height="24" class="cell head-cell"/><text x="128.0" y="135" text-anchor="middle" class="mrm" font-size="13">i</text><rect x="140" y="118" width="24" height="24" class="cell"/><text x="152.0" y="135" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="164" y="118" width="24" height="24" class="cell"/><text x="176.0" y="135" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="188" y="118" width="24" height="24" class="cell"/><text x="200.0" y="135" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="212" y="118" width="24" height="24" class="cell"/><text x="224.0" y="135" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="236" y="118" width="24" height="24" class="cell"/><text x="248.0" y="135" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="260" y="118" width="24" height="24" class="cell"/><text x="272.0" y="135" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="284" y="118" width="24" height="24" class="cell"/><text x="296.0" y="135" text-anchor="middle" class="mrm" font-size="14">1</text><text x="320" y="134" class="label">m ∈ A ∖ D<tspan font-size="9" dy="3">e</tspan><tspan dy="-3">: stop; the string avoids W</tspan><tspan font-size="9" dy="3">e</tspan></text><path d="M141,146 L141,152 L283,152 L283,146" class="muted-stroke" stroke-width="1.2"/><text x="212.0" y="168" text-anchor="middle" class="label">m zeros</text><text x="128.0" y="22" text-anchor="middle" class="label">i = Z(e)</text><text x="20" y="22" class="label">case 1</text><text x="20" y="110" class="label">case 2</text></svg>
:::

The number $m$ is the device that makes the decoding possible. It is written in $G$ as a run of zeros, so the decoder can read it. And it is chosen so that the answer of $A$ to the question "$m \in A$?" tells which case occurred: in case 1, $m \notin A$, and in case 2, $m \in A$.

:::proof{of=thm-jockusch-shore}
*$G$ is 1-generic.* At each step $e$, $G$ meets $W_e$ or has a prefix avoiding it, so $G$ meets $W_e \cup W_e^\perp$.

*$G \leq_T A \oplus Z \oplus \emptyset'$.* The bit $Z(e)$ is read from $Z$. The membership $m \in D_e$ is a c.e. question, answered by $\emptyset'$, and $m \in A$ is answered by $A$; so the least $m$ is found. In the first case, the first extension enumerated into $W_e$ is found by a computable search. So the sequence $(\sigma_e)$ is computable in $A \oplus Z \oplus \emptyset'$.

*$Z \leq_T A \oplus G$.* We compute the sequence $(\sigma_e)$ from $A \oplus G$, by induction. Suppose $\sigma_e$ is known. The bit of $G$ following $\sigma_e$ is $Z(e)$. Then read the number $m$ of zeros that follow, up to the next $1$; by construction it is the number chosen at step $e$. If $m \in A$, step $e$ was in the second case, and $\sigma_{e+1} = \sigma_e\, Z(e)\, 0^m\, 1$. If $m \notin A$, step $e$ was in the first case, so $m \in D_e$, and $\sigma_{e+1}$ is the first extension of $\sigma_e\, Z(e)\, 0^m\, 1$ enumerated into $W_e$, found by a computable search, which terminates. Hence $A \oplus G$ computes every bit $Z(e)$.

*$Z \leq_T G \oplus \emptyset'$.* The same decoding works with $\emptyset'$ in place of $A$: given $\sigma_e$, $Z(e)$ and $m$ are read from $G$ as above, and $\emptyset'$ decides whether $m \in D_e$, a c.e. question about $(e, \sigma_e, Z(e), m)$. If $m \in D_e$, step $e$ was in the first case, since in the second case $m \notin D_e$; otherwise it was in the second case. In both cases $\sigma_{e+1}$ is then obtained as before.
:::

The decoding from $A \oplus G$ uses $A$ for a single question at each step: is $m$ in $A$? The construction chose $m$ precisely so that the answer distinguishes the two cases, which is possible because $A$ is not c.e. A c.e. set $A$ could coincide with $D_e$, leaving no such $m$. Downey and Hirschfeldt present the same argument with an immune set in the role of the non-c.e. set: an immune set differs from every infinite c.e. set by an element of the c.e. set, and from every finite one by an element of its own.

:::quiz[the Jockusch–Shore construction]
Why does the construction need $A$ not to be c.e., rather than only non-computable?

- [x] Because it needs, at each step, a number on which $A$ and the c.e. set $D_e$ differ; if $A$ were c.e., it could equal $D_e$.

  The reduction to the non-c.e. case is harmless, since a non-computable c.e. set has a non-c.e. complement of the same degree.
- [ ] Because otherwise $G$ would not be 1-generic.

  Genericity is ensured in both cases at each step; the hypothesis is used to choose $m$.
- [ ] Because $\emptyset'$ cannot answer questions about c.e. sets.

  It can: membership in a c.e. set is a c.e. question.

---

When decoding, why does $m \notin A$ imply that step $e$ was in the first case?

- [x] The chosen $m$ is either in $D_e \setminus A$ (first case) or in $A \setminus D_e$ (second case); if $m \notin A$, only the first is possible.
- [ ] Because $m \notin A$ implies $m \notin D_e$.

  The opposite holds in the first case: $m \in D_e$ and $m \notin A$.
- [ ] Because the second case never happens.

  It happens whenever the least disagreement between $A$ and $D_e$ is an element of $A$.
:::

## Consequences

The three reductions of the theorem combine with the generalized lowness of 1-generic sets, $G' \equiv_T G \oplus \emptyset'$ (:ref{#thm-generic-low}), to control the jump of $G$.

:::corollary[Posner–Robinson]{#cor-posner-robinson}
Let $A$ be a non-computable set, and $Z \geq_T A \oplus \emptyset'$. There is a 1-generic set $G$ with $A \oplus G \equiv_T G' \equiv_T G \oplus \emptyset' \equiv_T Z$. In particular, taking $Z = A \oplus \emptyset'$, there is a 1-generic set $G$ with $A \oplus G \equiv_T G' \equiv_T G \oplus \emptyset'$.
:::

:::proof{of=cor-posner-robinson}
Apply :ref{#thm-jockusch-shore} to $A$ and $Z$: $G$ is 1-generic, $Z \leq_T A \oplus G$, $Z \leq_T G \oplus \emptyset'$, and $G \leq_T A \oplus Z \oplus \emptyset' \equiv_T Z$, the last equivalence since $A \oplus \emptyset' \leq_T Z$. From $G \leq_T Z$ and $A \leq_T Z$ we get $A \oplus G \leq_T Z$, so $A \oplus G \equiv_T Z$. From $G \leq_T Z$ and $\emptyset' \leq_T Z$ we get $G \oplus \emptyset' \leq_T Z$, so $G \oplus \emptyset' \equiv_T Z$. Finally $G' \equiv_T G \oplus \emptyset'$, since $G$ is 1-generic (:ref{#thm-generic-low}, with $G \oplus \emptyset' \leq_T G'$ for every set).
:::

So every non-computable set, however weak, bridges the gap between some set and its jump. For a low non-computable $A$, this gives a set $G$ with $A \oplus G \equiv_T G' \geq_T \emptyset'$ while $A$ alone is far from $\emptyset'$. The hypothesis that $A$ is not computable is necessary: for a computable $A$, the conclusion $A \oplus G \geq_T G'$ would give $G \geq_T G'$, which fails for every set.

:::corollary[Friedberg's jump inversion theorem]{#cor-jump-inversion}
For every set $Z \geq_T \emptyset'$, there is a 1-generic set $G$ with $G' \equiv_T Z$, and moreover $G \oplus \emptyset' \equiv_T Z$.
:::

:::proof{of=cor-jump-inversion}
Apply :ref{#thm-jockusch-shore} with $A = \emptyset'$, which is not computable: $G$ is 1-generic, $Z \leq_T \emptyset' \oplus G$ and $G \leq_T \emptyset' \oplus Z \oplus \emptyset' \equiv_T Z$. Hence $G \oplus \emptyset' \equiv_T Z$, and $G' \leq_T G \oplus \emptyset'$ since $G$ is 1-generic (:ref{#thm-generic-low}). The converse $G \oplus \emptyset' \leq_T G'$ holds for every set, so $G' \equiv_T Z$.
:::

This is also the case $A = \emptyset'$ of :ref{#cor-posner-robinson}. The hypothesis $Z \geq_T \emptyset'$ is necessary, since every jump computes $\emptyset'$.

:::corollary{#cor-high-not-dnc}
There is a high set that computes no DNC function; in particular, a high set that is not Turing complete.
:::

:::proof{of=cor-high-not-dnc}
By :ref{#cor-jump-inversion} with $Z = \emptyset''$, there is a 1-generic $G$ with $G' \equiv_T \emptyset''$, so $G$ is high. By :ref{#thm-generic-not-dnc}, $G$ computes no DNC function; since $\emptyset'$ computes one, $G$ does not compute $\emptyset'$.
:::

This gives a second construction of high incomplete sets, after :ref{#cor-high-incomplete}; the set obtained here is moreover 1-generic and computable in $\emptyset''$.

## Exercises

::::exercise{difficulty=1}
Show that every set $Z \geq_T \emptyset'$ is the join of $\emptyset'$ with a set $G$ such that $G \not\geq_T \emptyset'$.

:::solution
Take $G$ as in :ref{#cor-jump-inversion}: $Z \equiv_T G \oplus \emptyset'$, and $G$ is 1-generic, so it computes no DNC function, hence not $\emptyset'$.
:::
::::

::::exercise{difficulty=1}
Let $A \leq_T \emptyset'$ be non-computable. Show that there is a low 1-generic set $G$ with $A \oplus G \equiv_T \emptyset'$.

:::solution
Apply :ref{#thm-jockusch-shore} with $Z = \emptyset'$. Then $G$ is 1-generic, $\emptyset' \leq_T A \oplus G$, and $G \leq_T A \oplus \emptyset' \equiv_T \emptyset'$. Hence $A \oplus G \leq_T \emptyset'$, so $A \oplus G \equiv_T \emptyset'$. Since $G$ is 1-generic and $\Delta^0_2$, $G' \leq_T G \oplus \emptyset' \equiv_T \emptyset'$ by :ref{#thm-generic-low}, so $G$ is low.
:::
::::

::::exercise{difficulty=2}
Let $A$ be a set with $A \leq_T \emptyset'$ and $\emptyset' \not\leq_T A$, for instance a low set. Show that no 2-generic set $G$ satisfies $A \oplus G \geq_T G'$. So the set $G$ of :ref{#cor-posner-robinson} cannot in general be chosen 2-generic.

:::solution
Let $G$ be 2-generic, that is, 1-generic relative to $\emptyset'$. Since $A \leq_T \emptyset'$, we have $\emptyset' \oplus A \equiv_T \emptyset'$, so $G$ is 1-generic relative to $\emptyset' \oplus A$ (:ref{#ex-relative-genericity}). By :ref{#thm-generic-cone} with $C = \emptyset'$ and $Z = A$, using $\emptyset' \not\leq_T A$, we get $\emptyset' \not\leq_T G \oplus A$. Since $\emptyset' \leq_T G'$, also $G' \not\leq_T A \oplus G$.
:::
::::

## Notes and references

Posner and Robinson (1981) proved the join theorem: for every non-computable $A$ and every $Z \geq_T A \oplus \emptyset'$, there is $G$ with $G' \equiv_T G \oplus A \equiv_T Z$ (Downey and Hirschfeldt 2010, Theorem 2.16.2). The title of their paper refers to joins equal to $\obf'$; the case $A \leq_T \emptyset'$ is the second exercise. Their construction is a Cohen forcing construction, and the set it gives can be taken 1-generic (Day and Dzhafarov 2012, introduction; Downey and Hirschfeldt 2010, Theorem 2.24.4). The proof given here, through a non-c.e. set, is the one of Jockusch and Shore (1984), as presented by Monin and Patey, who state the theorem in the form of :ref{#thm-jockusch-shore}; Downey and Hirschfeldt give it with an immune set. Friedberg's jump inversion theorem dates from 1957 (Soare 2016, Theorem 6.4.1).

Shore and Slaman (1999) extended the join theorem to higher jumps: if $A \not\leq_T \emptyset^{(n-1)}$, there is $G$ with $A \oplus G \geq_T G^{(n)}$; they used it to show that the jump is definable in the partial order of the Turing degrees. Their proof uses a different notion of forcing, due to Kumabe and Slaman. Day and Dzhafarov showed that Cohen forcing cannot replace it: for $n \geq 2$, the set $G$ cannot in general be chosen $n$-generic, nor $2$-random. At the level $n = 1$, the last exercise shows that it cannot in general be chosen 2-generic; Day and Dzhafarov show that weak 2-genericity already prevents it.

- D. B. Posner and R. W. Robinson, *Degrees joining to 0′*, Journal of Symbolic Logic 46 (1981), 714–722.
- C. G. Jockusch and R. A. Shore, *Pseudo-jump operators II: transfinite iterations, hierarchies and minimal covers*, Journal of Symbolic Logic 49 (1984), 1205–1236.
- R. M. Friedberg, *A criterion for completeness of degrees of unsolvability*, Journal of Symbolic Logic 22 (1957), 159–160.
- R. A. Shore and T. A. Slaman, *Defining the Turing jump*, Mathematical Research Letters 6 (1999), 711–722.
- A. R. Day and D. D. Dzhafarov, *Limits to joining with generics and randoms*, preprint, arXiv:1209.3282, 2012.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.16 and §2.24.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §6.4.
- B. Monin and L. Patey, *Computability theory*, chapter *Cohen forcing*, section *Effective genericity*.
