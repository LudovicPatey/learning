---
title: Cone avoidance and low splittings
summary: The preservation strategy combined with other requirements; a simple set that does not compute a given non-computable c.e. set; the halves of a Sacks splitting are low; consequences and outlook for the c.e. degrees.
duration: 40
prerequisites: [sacks-splitting]
---

The Sacks preservation strategy of the previous lesson is a module: a requirement $\Phi^X_e \neq C$, for a non-computable c.e. set $C$, can be met inside any finite injury construction in which it is injured only finitely often. This lesson shows two uses of this observation. The first combines the strategy with the positive requirements of the low simple set, and yields a simple set outside the upper cone of $C$. The second applies the strategy, inside the splitting construction itself, to reductions chosen so that agreement with $B$ encodes the jump: this shows that the two halves of a Sacks splitting are low, at no extra cost. The lesson ends with consequences for the c.e. degrees and with what lies beyond finite injury.

Throughout, we use the notation of the previous lesson: a requirement $\Phi^X_e \neq C$ has a length of agreement and a restraint, defined as in :ref{#def-length-agreement}.

## Avoiding a cone with a simple set

:::theorem[Sacks]{#thm-sacks-cone-avoidance}
For every non-computable c.e. set $C$, there is a simple set $A$ such that $C \not\leq_T A$. In particular $\emptyset <_T A <_T \emptyset'$.
:::

In the course on Turing degrees, a set avoiding the cone above a non-computable set was built by finite extensions with the oracle $\emptyset'$ (:ref{#thm-cone-avoidance}). Here the set must be c.e., and the construction computable.

*Idea.* We take the construction of the low simple set and replace the lowness requirements by the requirements $\mathcal N_e : \Phi^A_e \neq C$, each with Sacks' restraint. The positive requirements act at most once, so a negative requirement is injured at most $e$ times, as in the low simple set; after its last injury, its restraint is respected, and the argument of :ref{#lem-sacks-main} shows that it is satisfied and that its restraint settles. The positive requirements then find room beyond the final restraints, as in :ref{#lem-low-positive}.

:::proof{of=thm-sacks-cone-avoidance}
*Requirements.* For every $e$:
$$
\mathcal P_e : W_e \text{ infinite} \Rightarrow W_e \cap A \neq \emptyset, \qquad \mathcal N_e : \Phi^A_e \neq C,
$$
in the priority order $\mathcal N_0 > \mathcal P_0 > \mathcal N_1 > \mathcal P_1 > \cdots$. Fix a c.e. approximation $(C_s)$ of $C$. Let $l(e, s)$ and $r(e, s)$ be the length of agreement and the restraint of :ref{#def-length-agreement}, with $A_s$ and $C_s$ in place of $A_{i,s}$ and $B_s$.

*Construction.* $A_0 = \emptyset$. At stage $s + 1$, say that $\mathcal P_e$ requires attention if $e \leq s$, $W_e[s] \cap A_s = \emptyset$, and some $x \in W_e[s]$ satisfies $x > 2e$ and $x > r(i, s)$ for every $i \leq e$. If some $\mathcal P_e$ requires attention, the least such $e$ enumerates the least such $x$ into $A$; otherwise $A_{s+1} = A_s$. Each $\mathcal P_e$ acts at most once, and $A$ is c.e.

*The complement of $A$ is infinite*, by the counting argument of :ref{#lem-low-coinfinite}: $\mathcal P_e$ enumerates at most one number, greater than $2e$.

*Each $\mathcal N_e$ is injured at most $e$ times.* Say that $\mathcal N_e$ is injured at stage $s + 1$ if a number $x \leq r(e, s)$ enters $A$ at that stage. A number enumerated by $\mathcal P_i$ with $i \geq e$ is greater than $r(e, s)$; so only the $\mathcal P_i$ with $i < e$ injure $\mathcal N_e$, each at most once.

*Each $\mathcal N_e$ is satisfied, and $r(e, s)$ is eventually constant.* Let $s_0$ be a stage after the last injury of $\mathcal N_e$. For $s \geq s_0$, no number at most $r(e, s)$ enters $A$ at stage $s + 1$. This is the preservation property on which the proofs of items 2 and 3 of :ref{#lem-sacks-main} rest; those proofs use nothing else about the construction, besides the facts that $C$ is c.e. and not computable. They apply verbatim, with $A$ and $C$ in place of $A_i$ and $B$, and give $\Phi^A_e \neq C$ and the convergence of $r(e, s)$.

*Each $\mathcal P_e$ is satisfied.* Suppose that $W_e$ is infinite. Let $s_1$ be a stage after which no $\mathcal P_i$ with $i < e$ acts and $r(i, s) = r_i$ for every $i \leq e$, where $r_i$ is the limit of $r(i, s)$. Let $m = \max(2e, r_0, \dots, r_e)$, and let $s \geq \max(s_1, e)$ be such that some $x > m$ belongs to $W_e[s]$. Either $W_e[s] \cap A_s \neq \emptyset$, or $\mathcal P_e$ requires attention at stage $s + 1$; in the second case no $\mathcal P_i$ with $i < e$ requires attention, since it would act, so $\mathcal P_e$ acts. In both cases $W_e \cap A \neq \emptyset$.

So $A$ is simple, and $\Phi^A_e \neq C$ for every $e$, that is, $C \not\leq_T A$. A simple set is not computable; and if $\emptyset' \leq_T A$, then $C \leq_T \emptyset' \leq_T A$, since $C$ is c.e. Hence $\emptyset <_T A <_T \emptyset'$.
:::

The theorem gives a fourth solution to Post's problem, from any non-computable c.e. set $C$, for instance a low one. The two finite injury patterns are now visible side by side. The positive requirements cause a **bounded** number of injuries, at most $e$ to $\mathcal N_e$, because each acts once. The negative requirements could a priori restrain more and more, and it is the non-computability of $C$ that bounds their restraints. In the splitting theorem, by contrast, every element of $A$ must be placed on one side, so the injuries depend on how many elements of $A$ fall below the final restraints of higher priority, and they are not bounded in advance.

:::quiz[cone avoidance]
Why is $\mathcal N_e$ injured at most $e$ times in the proof of :ref{#thm-sacks-cone-avoidance}?

- [x] Only positive requirements enumerate numbers; those of lower priority respect the restraint of $\mathcal N_e$, and each of $\mathcal P_0, \dots, \mathcal P_{e-1}$ acts at most once.
- [ ] Because the restraint of $\mathcal N_e$ is eventually constant.

  This is proved after, and using, the finiteness of the injuries.
- [ ] Because $C$ is c.e.

  The hypotheses on $C$ are used to show that $\mathcal N_e$ is satisfied once it is no longer injured, not to count the injuries.

---

Where is it used that $C$ is c.e., in the conclusion $A <_T \emptyset'$?

- [x] To get $C \leq_T \emptyset'$: if $A$ computed $\emptyset'$, it would compute $C$.
- [ ] To show that $A$ is c.e.

  $A$ is c.e. because the construction is computable; the approximation of $C$ is computable in any case.
- [ ] It is not used there.

  Without $C \leq_T \emptyset'$, the requirements $\mathcal N_e$ would not exclude $A \equiv_T \emptyset'$.
:::

## The halves of a Sacks splitting are low

:::theorem{#thm-low-splitting}
The sets $A_0$ and $A_1$ built in the proof of :ref{#thm-sacks-splitting} are low.
:::

*Idea.* The construction already contains, for each $e$, a requirement that settles on a finite outcome, and the proof of :ref{#lem-sacks-main} shows that the length of agreement converges. It suffices to choose a reduction whose length of agreement with $B$ is $1$ or $0$ according to whether $\Phi^{A_i}_e(e)$ converges. The limit of the length of agreement then gives a computable approximation of the jump.

:::proof{of=thm-low-splitting}
By the parameter form of the relativized SMN theorem (:ref{#thm-relativized-smn}), whose indices do not depend on the oracle, there is a total computable function $g$ such that for every $X$ and $e$: $\Phi^X_{g(e)}(0)\converge = B(0)$ if $\Phi^X_e(e)\converge$, $\Phi^X_{g(e)}(0)\diverge$ otherwise, and $\Phi^X_{g(e)}(y)\diverge$ for every $y \geq 1$. The bit $B(0)$ is a fixed constant, written into the program.

Fix $i$ and $e$, and let $p$ be the least number with $\Phi^{A_i}_{g(e)}(p) \neq B(p)$, a disagreement or a divergence. If $\Phi^{A_i}_e(e)\converge$, then $\Phi^{A_i}_{g(e)}(0) = B(0)$ and $\Phi^{A_i}_{g(e)}(1)\diverge$, so $p = 1$; otherwise $\Phi^{A_i}_{g(e)}(0)\diverge$, so $p = 0$. The proof of item 3 of :ref{#lem-sacks-main}, for the requirement $\mathcal R_{g(e), i}$, shows that $l(g(e), i, s) = p$ for all sufficiently large $s$. Hence
$$
A_i'(e) = \lim_s \min\big(l(g(e), i, s), 1\big),
$$
and the function $(e, s) \mapsto \min(l(g(e), i, s), 1)$ is computable. By the limit lemma (:ref{#thm-limit-lemma}), $A_i' \leq_T \emptyset'$.
:::

The number of injuries of a requirement is not computably bounded in this construction, and the halves cannot in general be made superlow: as recalled in the solution of :ref{#ex-low-splitting}, $\emptyset'$ is not the disjoint union of two superlow c.e. sets.

:::corollary{#cor-low-join}
Every non-zero c.e. degree is the join of two incomparable low c.e. degrees. In particular $\obf'$ is the join of two low c.e. degrees, so the join of two low degrees need not be low.
:::

:::proof{of=cor-low-join}
Let $A$ be a non-computable c.e. set, and apply the construction of :ref{#thm-sacks-splitting} with $B = A$. By :ref{#thm-low-splitting} the sets $A_0$ and $A_1$ are low; by :ref{#cor-splitting-post} and the proof of :ref{#cor-no-minimal-ce}, they are incomparable and $A_0 \oplus A_1 \equiv_T A$.
:::

:::corollary{#cor-incomparable-ce}
For every c.e. degree $\cbf$ with $\obf < \cbf < \obf'$, there is a c.e. degree incomparable with $\cbf$.
:::

:::proof{of=cor-incomparable-ce}
Let $C \in \cbf$ be c.e. Apply :ref{#thm-sacks-splitting} with $A = \emptyset'$ and $B = C$, which is not computable since $\cbf > \obf$: $\emptyset' = A_0 \sqcup A_1$ with $C \not\leq_T A_0$ and $C \not\leq_T A_1$. If both $A_0$ and $A_1$ were computable in $C$, then $\emptyset' \leq_T A_0 \oplus A_1 \leq_T C$, contradicting $\cbf < \obf'$. So some $A_i$ is not computable in $C$, and $C$ is not computable in $A_i$: the degree of $A_i$ is incomparable with $\cbf$.
:::

:::quiz[low splittings]
In the proof of :ref{#thm-low-splitting}, why is the reduction $\Phi_{g(e)}$ made to diverge at every $y \geq 1$?

- [x] So that the length of agreement is at most $1$: its limit is then exactly $1$ or $0$, according to whether $\Phi^{A_i}_e(e)$ converges.
- [ ] So that $\Phi^{A_i}_{g(e)} \neq B$.

  This holds for every reduction, by :ref{#lem-sacks-main}; the divergence is chosen to make the limit of the length of agreement readable.
- [ ] To make $g$ computable.

  Any program obtained by SMN is computable; the choice of values matters only for the length of agreement.

---

In :ref{#cor-incomparable-ce}, which hypothesis on $\cbf$ excludes that both halves of $\emptyset'$ are computable in $C$?

- [x] $\cbf < \obf'$: otherwise $C$ would compute $A_0 \oplus A_1 \equiv_T \emptyset'$.
- [ ] $\cbf > \obf$.

  This hypothesis makes $C$ non-computable, as the splitting theorem requires; it says nothing about what $C$ computes.
- [ ] That $C$ is c.e.

  It is used to apply the splitting theorem, not to compare the halves with $C$.
:::

## Beyond finite injury

The results of this course describe the c.e. degrees as a partial order with least element $\obf$ and greatest element $\obf'$, with no minimal element above $\obf$ (:ref{#cor-no-minimal-ce}), in which every element strictly between $\obf$ and $\obf'$ is incomparable with some other element (:ref{#cor-incomparable-ce}), and every non-zero element is the join of two incomparable low elements (:ref{#cor-low-join}). The structure is much richer. Sacks proved in 1964 that the c.e. degrees are **dense**: between any two c.e. degrees $\abf < \bbf$ there is a third. Lachlan and Yates proved independently in 1966 that there are **minimal pairs**: non-computable c.e. degrees $\abf$ and $\bbf$ whose only common lower bound is $\obf$. Both are proved by the **infinite injury** method, in which some requirements act infinitely often; in modern presentations the construction is organized along a tree of strategies. Minimal pairs are constructed in :ref{to="infinite-injury/minimal-pairs"}.

Monin and Patey place the Sacks strategy between the two methods. A requirement $\Phi^X_e \neq C$ could a priori act infinitely often, with ever larger restraints; in this course, the hypothesis that $C$ is not computable excludes this outcome. In a minimal pair construction, a requirement preserves agreements between two reductions $\Phi^A_e$ and $\Phi^B_e$, which may well be total and equal; no hypothesis excludes the infinite outcome, and the construction must be organized so that the requirements of lower priority survive it.

Priority arguments are not the only route to Post's problem. Kučera (1986) gave a solution without injury: there is a low set of diagonally non-computable degree, by the low basis theorem or by randomness, and every $\Delta^0_2$ set of diagonally non-computable degree computes a non-computable c.e. set, which is then low. The c.e. K-trivial sets of the course on K-trivial sets give another solution without injury (:ref{#thm-solovay-ktrivial}), at the price of a harder proof of incompleteness. Nies discusses these solutions, and whether any solution to Post's problem can be called natural, in Sections 1.6, 4.2 and 5.3 of his book.

## Exercises

::::exercise{#ex-ca-uniform-sequence difficulty=2 objective="Run the cone avoidance construction against a uniformly c.e. sequence of sets, and deduce that the non-zero c.e. degrees cannot be listed uniformly."}
Let $(C_j)_{j \in \nat}$ be a uniformly c.e. sequence of non-computable sets. Show that there is a simple set $A$ such that $C_j \not\leq_T A$ for every $j$. Deduce that there is no uniformly c.e. sequence of sets whose degrees are exactly the non-zero c.e. degrees.

:::solution
Replace the requirements $\mathcal N_e$ of :ref{#thm-sacks-cone-avoidance} by $\mathcal N_{\langle e, j \rangle} : \Phi^A_e \neq C_j$, with the length of agreement and the restraint computed from the uniform approximations $(C_{j,s})$, and the priority order $\mathcal N_0 > \mathcal P_0 > \mathcal N_1 > \mathcal P_1 > \cdots$ on the codes $\langle e, j \rangle$. The proof is unchanged: $\mathcal N_k$ is injured at most $k$ times, then satisfied with a convergent restraint, and each $\mathcal P_e$ finds room beyond the final restraints of $\mathcal N_0, \dots, \mathcal N_e$.

If $(C_j)$ were a uniformly c.e. sequence whose degrees are exactly the non-zero c.e. degrees, every $C_j$ would be non-computable, and the set $A$ just built would be a non-computable c.e. set with $A \not\equiv_T C_j$ for every $j$, since $C_j \not\leq_T A$. Its degree would be a non-zero c.e. degree outside the sequence, a contradiction.
:::
::::

## Notes and references

The cone avoidance theorem is due to Sacks, who introduced the preservation strategy to prove it and the splitting theorem (Sacks 1963). Soare's book of 2016 presents the cone avoidance theorem in Section 7.4 (Theorem 7.4.1) and the splitting theorem with low halves in Section 7.5 (Theorem 7.5.1, Lemma 7.5.7 for lowness, and Corollaries 7.5.3 and 7.5.6, which are :ref{#cor-low-join} and :ref{#cor-incomparable-ce}); :ref{#ex-ca-uniform-sequence} is a variant of his Exercise 7.6.3, which treats $\Delta^0_2$ sets $C_j$ and splittings. Monin and Patey prove a cone avoidance theorem, for a non-computable set rather than a simple one, in their chapter on the priority method and c.e. degrees. Nies gives the low splitting as Exercise 1.6.10, and attributes to Bickford and Mills the fact that $\emptyset'$ has no splitting into two superlow c.e. sets. The density theorem is due to Sacks (1964), and minimal pairs of c.e. degrees to Lachlan (1966) and Yates (1966); Downey and Hirschfeldt prove both, in Sections 2.15 and 2.14.2. Kučera's injury-free solution is in his paper of 1986, and is presented in Nies, Section 4.2.

- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010.
- A. Kučera, *An alternative, priority-free, solution to Post's problem*, in Mathematical Foundations of Computer Science 1986, Lecture Notes in Computer Science 233, Springer, 1986, 493–500.
- A. H. Lachlan, *Lower bounds for pairs of recursively enumerable degrees*, Proceedings of the London Mathematical Society (3) 16 (1966), 537–569.
- B. Monin and L. Patey, *Computability theory*, chapter *Priority method and c.e. degrees*.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009.
- G. E. Sacks, *On the degrees less than 0′*, Annals of Mathematics 77 (1963), 211–231.
- G. E. Sacks, *The recursively enumerable degrees are dense*, Annals of Mathematics 80 (1964), 300–312.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.
- C. E. M. Yates, *A minimal pair of recursively enumerable degrees*, Journal of Symbolic Logic 31 (1966), 159–168.

:::::exercises
::::exercise{#ex-ca-incomparable-pair difficulty=1 objective="Combine the results of the course to obtain two incomparable c.e. degrees strictly between $\mathbf 0$ and $\mathbf 0'$." lessons="low-simple-set"}
Show that there are c.e. sets $A$ and $C$ with $\emptyset <_T C <_T \emptyset'$ such that $C \not\leq_T A$ and $A \not\leq_T C$.

:::solution
Let $C$ be a low simple set (:ref{#thm-low-simple}), and apply :ref{#cor-incomparable-ce} to its degree, which lies strictly between $\obf$ and $\obf'$: it gives a c.e. set $A$ whose degree is incomparable with that of $C$.
:::
::::

::::exercise{#ex-ca-low-cone difficulty=2 objective="Combine lowness requirements, Sacks requirements and Post's requirements in one finite injury construction." lessons="low-simple-set"}
Let $C$ be a non-computable c.e. set. Show that there is a low simple set $A$ such that $C \not\leq_T A$.

:::solution
If $C$ is not low, any low simple set works, since a set computable in a low set is low. In general, use three kinds of requirements, for every $e$:
$$
\begin{aligned}
\mathcal L_e &: \Phi^{A_s}_e(e)[s]\converge \text{ for infinitely many } s \Rightarrow \Phi^A_e(e)\converge, \\
\mathcal N_e &: \Phi^A_e \neq C, \qquad \mathcal P_e : W_e \text{ infinite} \Rightarrow W_e \cap A \neq \emptyset,
\end{aligned}
$$
in the priority order $\mathcal L_0 > \mathcal N_0 > \mathcal P_0 > \mathcal L_1 > \mathcal N_1 > \mathcal P_1 > \cdots$. Let $r_{\mathcal L}(e, s)$ be the restraint of :ref{#def-restraint-function}, and $r_{\mathcal N}(e, s)$ the Sacks restraint of the proof of :ref{#thm-sacks-cone-avoidance}.

*Construction.* $A_0 = \emptyset$. At stage $s + 1$, say that $\mathcal P_e$ requires attention if $e \leq s$, $W_e[s] \cap A_s = \emptyset$, and some $x \in W_e[s]$ satisfies $x > 2e$, $x > r_{\mathcal L}(i, s)$ and $x > r_{\mathcal N}(i, s)$ for every $i \leq e$. The least such $e$, if any, enumerates the least such $x$ into $A$.

*Verification.* Each $\mathcal P_e$ acts at most once and enumerates a number greater than $2e$, so the complement of $A$ is infinite by the counting argument of :ref{#lem-low-coinfinite}. A requirement $\mathcal P_i$ with $i \geq e$ enumerates only numbers above the restraints of $\mathcal L_e$ and $\mathcal N_e$; so $\mathcal L_e$ and $\mathcal N_e$ are injured only by $\mathcal P_0, \dots, \mathcal P_{e-1}$, hence at most $e$ times. After the last injury of $\mathcal L_e$, the proof of :ref{#lem-low-negative} shows that $r_{\mathcal L}(e, s)$ converges and that $\lim_s g(e, s) = A'(e)$. After the last injury of $\mathcal N_e$, the proofs of items 2 and 3 of :ref{#lem-sacks-main} show that $\Phi^A_e \neq C$ and that $r_{\mathcal N}(e, s)$ converges; they use only the preservation property and the facts that $C$ is c.e. and not computable. Finally, if $W_e$ is infinite, take a stage $s_1$ after which no $\mathcal P_i$ with $i < e$ acts and all the restraints of $\mathcal L_i$ and $\mathcal N_i$, $i \leq e$, have reached their limits, with maximum $R$. Some $x > \max(2e, R)$ belongs to $W_e[s]$ for some $s \geq \max(s_1, e)$; as in :ref{#lem-low-positive}, either $W_e[s] \cap A_s \neq \emptyset$ or $\mathcal P_e$ acts at stage $s + 1$.

So $A$ is simple, low by the limit lemma, and $C \not\leq_T A$. The exercise has content when $C$ is low, for instance when $C$ is itself a low simple set.
:::
::::

::::exercise{#ex-ca-low-bounds difficulty=1 objective="Derive from the low splitting theorem the existence of low c.e. degrees below and beside given c.e. degrees."}
1. Show that every non-zero c.e. degree bounds a non-zero low c.e. degree.
2. Show that for every c.e. degree $\cbf$ with $\obf < \cbf < \obf'$, there is a low c.e. degree incomparable with $\cbf$.

:::solution
1. Let $\abf$ be a non-zero c.e. degree. By :ref{#cor-low-join}, $\abf$ is the join of two incomparable low c.e. degrees $\abf_0$ and $\abf_1$. Then $\abf_0 \leq \abf$, and $\abf_0 \neq \obf$, since otherwise $\abf_0 \leq \abf_1$.

2. In the proof of :ref{#cor-incomparable-ce}, the sets $A_0$ and $A_1$ are built by the construction of :ref{#thm-sacks-splitting}, with $A = \emptyset'$ and $B = C$. By :ref{#thm-low-splitting}, they are low. The proof shows that one of them has a degree incomparable with $\cbf$; this degree is low and c.e.
:::
::::

::::exercise{#ex-ca-halves-not-simple difficulty=1 objective="Compare the sets given by the splitting theorem and by the cone avoidance theorem." lessons="simple-sets, sacks-splitting"}
Let $A_0$ and $A_1$ be disjoint c.e. sets with $A_1$ infinite. Show that $A_0$ is not simple. Deduce that, for a non-computable c.e. set $A$, neither half of a splitting given by :ref{#cor-splitting-post} is simple.

:::solution
The set $A_1$ is an infinite c.e. set contained in $\nat \setminus A_0$, since $A_0 \cap A_1 = \emptyset$. So the complement of $A_0$ is not immune, and $A_0$ is not simple.

In :ref{#cor-splitting-post}, both halves are non-computable, hence infinite, and disjoint. By the first part, neither is simple. So the halves of a Sacks splitting are never simple sets, while :ref{#thm-sacks-cone-avoidance} gives simple sets: the two theorems produce sets of different kinds, although both avoid a cone with the same strategy.
:::
::::

::::exercise{#ex-ca-low-cover difficulty=2 objective="Use the low splitting of a universal c.e. set to bound every c.e. degree by two fixed low degrees." lessons="sacks-splitting"}
Show that there are low c.e. sets $A_0$ and $A_1$ such that every c.e. set $W$ is Turing equivalent to $W_0 \oplus W_1$ for some c.e. sets $W_0 \leq_T A_0$ and $W_1 \leq_T A_1$. In terms of degrees: there are low c.e. degrees $\abf_0$ and $\abf_1$ such that every c.e. degree is the join of a c.e. degree below $\abf_0$ and a c.e. degree below $\abf_1$.

:::solution
Let $K_0 = \{ \langle x, y \rangle : x \in W_y \}$, which is c.e. It is not computable: $n \in \emptyset'$ if and only if $n \in W_n$, if and only if $\langle n, n \rangle \in K_0$, so $\emptyset' \leq_m K_0$. Apply the construction of :ref{#thm-sacks-splitting} with $A = B = K_0$, and let $A_0$, $A_1$ be the halves; they are low by :ref{#thm-low-splitting}.

Let $W = W_e$, and $W_i = \{ x : \langle x, e \rangle \in A_i \}$ for $i \in \{0, 1\}$. These sets are c.e., and $W_i \leq_m A_i$ through $x \mapsto \langle x, e \rangle$, so $W_i \leq_T A_i$. They are disjoint, and $W_0 \cup W_1 = \{ x : \langle x, e \rangle \in K_0 \} = W_e$. So $W_e \leq_T W_0 \oplus W_1$, since $x \in W_e$ if and only if $x \in W_0$ or $x \in W_1$. Conversely, $W_i \leq_T W_e$: given $x$, if $x \notin W_e$ then $x \notin W_i$; otherwise, enumerate $W_0$ and $W_1$ until $x$ appears in one of them. Hence $W_e \equiv_T W_0 \oplus W_1$.

Adapted from Soare 2016, Exercise 7.6.5. Only the lowness of the halves is used; the cone avoidance of the splitting plays no role here.
:::
::::
:::::
