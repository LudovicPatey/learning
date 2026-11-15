---
title: Rice's theorem
summary: Non-trivial index sets are not computable, and the halting set or its complement many-one reduces to each of them.
duration: 30
prerequisites: [fixed-point, complete-sets]
---

The halting problem is one undecidable question about programs. Rice's theorem shows that it is typical: no question about the **function computed** by a program can be decided from its index, except the trivial ones. This lesson proves the theorem twice, by the fixed point theorem and by a reduction from the halting set. The second proof gives more: the halting set, or its complement, many-one reduces to every non-trivial index set. The next lesson determines which questions about the function computed can at least be **confirmed**, that is, which index sets are computably enumerable.

## Index sets

A property of programs may concern their text — "does the program have fewer than $100$ states?", decidable by inspecting the code — or their behavior. The second kind is captured as follows.

:::definition{#def-index-set}
A set $P \subseteq \nat$ is an **index set** if, for all $a$ and $b$, $\Phi_a = \Phi_b$ and $a \in P$ imply $b \in P$. It is **non-trivial** if $P \neq \emptyset$ and $P \neq \nat$.
:::

Equivalently, $P$ is an index set if there is a class $\mathcal C$ of unary partial computable functions with $P = \{ e : \Phi_e \in \mathcal C \}$; it is non-trivial if $\mathcal C$ contains some but not all partial computable functions.

:::example{#ex-index-sets}
The following are non-trivial index sets: $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$; $\{ e : \Phi_e(0)\converge = 42 \}$; $\{ e : W_e = \emptyset \}$; $\{ e : W_e \text{ is finite} \}$; $\{ e : \Phi_e = \Phi_a \}$ for a fixed $a$. The set $\{ e : e < 100 \}$ is not an index set: it contains $0$, while by the padding lemma the function $\Phi_0$ also has the index $p(0, 100) \geq 100$, which is not in the set.
:::

:::quiz[index sets]
Which of these sets are index sets?

- [x] $\{ e : \Phi_e(3)\converge \}$.
- [x] $\{ e : W_e \text{ is finite} \}$.
- [ ] $\{ e : \text{the machine of code } e \text{ has fewer than } 100 \text{ states} \}$.

  This is a property of the code: padding a small machine gives a large one computing the same function.
- [ ] $\{ e : \Phi_e(e)\converge \}$.

  By the fixed point theorem there is $e$ with $W_e = \{ e \}$; by padding, there is $e' \neq e$ with $\Phi_{e'} = \Phi_e$, and then $e \in \emptyset'$ while $e' \notin \emptyset'$. The diagonal input depends on the index, not only on the function.
:::

## Rice's theorem

:::theorem[Rice]{#thm-rice}
No non-trivial index set is computable.
:::

Both hypotheses are needed. The trivial index sets $\emptyset$ and $\nat$ are computable. The set $\{ e : e < 100 \}$ is computable and neither empty nor everything, but it is not an index set (:ref{#ex-index-sets}). The proof is an application of the fixed point theorem in the pattern of :ref{#prop-halting-via-fixed-point}: if $P$ were computable, the transformation sending every index to a fixed index on the other side of $P$ would be computable, and it cannot have a fixed point.

:::proof{of=thm-rice}
Let $P$ be a non-trivial index set, and suppose it is computable. Fix $a \in P$ and $b \notin P$, and let $f(x) = b$ if $x \in P$, $f(x) = a$ if $x \notin P$. Since $P$ is computable, $f$ is total computable. By :ref{#thm-fixed-point}, there is $e$ with $\Phi_{f(e)} = \Phi_e$, so that $e \in P \iff f(e) \in P$, as $P$ is an index set. But by construction $f(e) \in P \iff e \notin P$. This is a contradiction.
:::

:::quiz[the proof of Rice's theorem]
Which property of $f$ makes the fixed point contradictory?

- [x] $f$ sends every index to the other side of $P$, while an index and its image under $f$ compute the same function at a fixed point, and must therefore lie on the same side.
- [ ] $f$ is injective.

  $f$ takes only two values.
- [ ] $f(e) = e$ for some $e$.

  The fixed point theorem gives $\Phi_{f(e)} = \Phi_e$, not $f(e) = e$; here $f(e) \neq e$ always, since $f(e)$ and $e$ lie on different sides of $P$.

---

Where is the computability of $P$ used?

- [x] To make $f$ computable, as required by the fixed point theorem.
- [ ] To choose $a \in P$ and $b \notin P$.

  This only uses non-triviality: two fixed numbers are chosen, no algorithm is needed.
- [ ] To show that $P$ is an index set.

  This is a hypothesis, unrelated to computability.
:::

::::exercise{#ex-equality-undecidable difficulty=1 objective="Apply Rice's theorem to the equivalence of programs."}
Show that there is no algorithm which, given $a$ and $b$, decides whether $\Phi_a = \Phi_b$.

:::solution
Fix an index $z$ of the nowhere defined function. If equality were decidable, the set $\{ e : \Phi_e = \Phi_z \}$ would be computable. It is an index set, non-trivial since it contains $z$ and no index of the constant function $0$. This contradicts :ref{#thm-rice}.
:::
::::

The fixed point proof shows that $P$ is not computable, but not how difficult it is. A reduction gives more information.

:::proposition{#prop-rice-reduction}
Let $P$ be a non-trivial index set, and let $z$ be an index of the nowhere defined function (since $P$ is an index set, whether $z \in P$ does not depend on the choice of $z$). If $z \notin P$, then $\emptyset' \leq_m P$. If $z \in P$, then $\emptyset' \leq_m \nat \setminus P$.
:::

:::proof{of=prop-rice-reduction}
Suppose $z \notin P$, and fix $a \in P$. By :ref{#cor-smn-parameters}, there is a total computable $g$ such that
$$
\Phi_{g(e)}(x) \simeq \begin{cases} \Phi_a(x) & \text{if } \Phi_e(e)\converge,\\ \text{undefined} & \text{otherwise,} \end{cases}
$$
the program $g(e)$ first computes $\Phi_e(e)$, and if this halts, computes $\Phi_a(x)$. If $e \in \emptyset'$, then $\Phi_{g(e)} = \Phi_a$, so $g(e) \in P$. If $e \notin \emptyset'$, then $\Phi_{g(e)} = \Phi_z$, so $g(e) \notin P$. Hence $g$ reduces $\emptyset'$ to $P$. If $z \in P$, apply this to the non-trivial index set $\nat \setminus P$, which does not contain $z$.
:::

This gives a second proof of :ref{#thm-rice}, since $\emptyset'$ is not computable. It also shows that every non-trivial index set not containing the indices of the nowhere defined function is at least as hard as the halting set; if it is c.e., it is m-complete.

:::example{#ex-rice-reductions}
1. $P = \{ e : \Phi_e(0)\converge = 42 \}$ does not contain the indices of the nowhere defined function, so $\emptyset' \leq_m P$. Since $P$ is c.e. ($e \in P \iff \exists s\ \Phi_e(0)[s]\converge = 42$), it is m-complete.
2. $P = \{ e : W_e = \emptyset \}$ contains them, so $\emptyset' \leq_m \nat \setminus P = \{ e : W_e \neq \emptyset \}$, as found directly in :ref{#prop-halting-variants}.
3. $\mathrm{Tot}$ does not contain them, so $\emptyset' \leq_m \mathrm{Tot}$. The proposition says nothing about $\nat \setminus \emptyset' \leq_m \mathrm{Tot}$, which also holds (:ref{#prop-halting-variants}): it only gives the reduction that the position of the nowhere defined function forces.
:::

:::quiz[the reduction]
In the proof of :ref{#prop-rice-reduction}, why must $z \notin P$ be assumed?

- [x] For $e \notin \emptyset'$, the program $g(e)$ computes the nowhere defined function, and the reduction needs $g(e) \notin P$ in that case.
- [ ] To ensure that $g$ is total.

  $g$ is total by SMN in any case.
- [ ] Because $P$ would otherwise be trivial.

  $P$ can be non-trivial and contain $z$, for instance $P = \{ e : W_e = \emptyset \}$.
:::

::::exercise{#ex-index-ce-coce difficulty=2 objective="Combine Rice's theorem, the index set theorem and the complementation theorem to locate the nowhere defined function with respect to a c.e. index set."}
Let $P$ be a non-trivial index set. Show that $P$ and $\nat \setminus P$ cannot both be c.e. Deduce that if $P$ is c.e., the indices of the nowhere defined function are not in $P$.

:::solution
If both were c.e., $P$ would be computable by :ref{#prop-computable-iff-ce-coce}, contradicting :ref{#thm-rice}. If $P$ is c.e. and contains an index $z$ of the nowhere defined function, then $\emptyset' \leq_m \nat \setminus P$ by :ref{#prop-rice-reduction}, that is, $\nat \setminus \emptyset' \leq_m P$ by item 2 of :ref{#prop-many-one}; so $\nat \setminus \emptyset'$ would be c.e. by :ref{#prop-ce-downward}, contradicting :ref{#thm-halting-ce}.
:::
::::

## Consequences

Rice's theorem is a limitation on the automatic analysis of programs. Whether a program meets a behavioral specification — computes a given function, halts on all inputs, never outputs $0$ — is undecidable in general. In practice, program analysis tools either restrict the programs considered, or accept answers that may be inconclusive. The theorem is about **decidability** only. Questions of the form "does the program ever do this?" are often c.e., while questions about all inputs, such as totality, are typically not even c.e.; the next lesson characterizes the c.e. index sets. Measuring their exact difficulty is the purpose of the arithmetic hierarchy, the subject of a later course.

## Notes and references

Rice's theorem appeared in 1953, in a paper on classes of c.e. sets. In Soare's textbook, the reduction of :ref{#prop-rice-reduction} is the index set theorem (Theorem 1.6.13), Rice's theorem is Corollary 1.6.14, and the proof by the fixed point theorem is Exercise 2.2.10. Monin and Patey present Rice's theorem in their chapter on the arithmetic hierarchy, and derive it from the fixed point theorem in an exercise of their chapter on the foundations of computability.

- H. G. Rice, *Classes of recursively enumerable sets and their decision problems*, Transactions of the American Mathematical Society 74 (1953), 358–366.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 1.6.3 and 2.2.
- B. Monin and L. Patey, *Computability theory*, chapter *Arithmetic hierarchy*, section *Rice's theorem*.

:::::exercises
::::exercise{#ex-which-index-sets difficulty=1 objective="Decide whether a set of indices is an index set, using padding and self-reference."}
Which of the following sets are index sets?

1. $\{ e : \Phi_e \text{ is total and } \Phi_e(0) = 0 \}$.
2. $\{ e : W_e \subseteq \{ 0, \dots, 9 \} \}$.
3. $\{ e : \Phi_e(0)\converge = e \}$.
4. The set of minimal indices, $\{ e : \Phi_i \neq \Phi_e \text{ for every } i < e \}$.

:::solution
1 and 2 are index sets: membership of $e$ depends only on the function $\Phi_e$, and on its domain $W_e$.

3 is not. By :ref{#cor-self-reference} with $g(e, x) = e$, there is $e$ with $\Phi_e(x) = e$ for all $x$, so $e$ belongs to the set. Let $e' = p(e, e + 1)$, with $p$ the padding function (:ref{#lem-padding}): then $\Phi_{e'} = \Phi_e$ and $e' \geq e + 1$, so $\Phi_{e'}(0) = e \neq e'$ and $e'$ does not belong to the set.

4 is not. Let $m$ be the least index of some partial computable function; $m$ is minimal. The index $e' = p(m, m + 1) > m$ computes the same function, and it is not minimal, since $m < e'$ and $\Phi_m = \Phi_{e'}$.
:::
::::

::::exercise{#ex-index-set-classify difficulty=1 objective="Apply the index set theorem to decide whether the halting set or its complement reduces to a given index set."}
For each of the following index sets $P$, check that $P$ is non-trivial, and determine which of $\emptyset' \leq_m P$ and $\emptyset' \leq_m \nat \setminus P$ follows from :ref{#prop-rice-reduction}.

1. $\{ e : W_e \text{ is finite} \}$.
2. $\{ e : \Phi_e(0)\diverge \}$.
3. $\{ e : \text{the range of } \Phi_e \text{ is infinite} \}$.
4. $\{ e : \Phi_e \circ \Phi_e = \Phi_e \}$.

:::solution
Let $z$ be an index of the nowhere defined function.

1. $z \in P$, and an index of a total function is not in $P$. So $\emptyset' \leq_m \nat \setminus P = \{ e : W_e \text{ is infinite} \}$, as found directly in :ref{#ex-inf-reductions}.
2. $z \in P$, and an index of the constant function $0$ is not. So $\emptyset' \leq_m \{ e : \Phi_e(0)\converge \}$, as in :ref{#prop-halting-variants}.
3. $z \notin P$, since the range of the nowhere defined function is empty, and an index of the identity is in $P$. So $\emptyset' \leq_m P$.
4. The nowhere defined function $\zeta$ satisfies $\zeta \circ \zeta = \zeta$, so $z \in P$; the successor function $\sigma$ does not, since $\sigma(\sigma(0)) = 2 \neq 1 = \sigma(0)$. So $\emptyset' \leq_m \nat \setminus P$.

In each case the proposition gives one reduction; it says nothing about the other one.
:::
::::

::::exercise{#ex-not-self-dual difficulty=2 objective="Apply the fixed point theorem to show that no index set reduces to its complement." lessons="fixed-point"}
A set $A$ is **self-dual** if $A \leq_m \nat \setminus A$. Show that no index set is self-dual, the trivial ones included. Deduce, using :ref{#ex-join-m}, that no index set is many-one equivalent to $\emptyset' \oplus (\nat \setminus \emptyset')$.

:::solution
Let $P$ be an index set, and suppose that $f$ reduces $P$ to $\nat \setminus P$: $x \in P \iff f(x) \notin P$ for every $x$. By :ref{#thm-fixed-point}, there is $e$ with $\Phi_e = \Phi_{f(e)}$. Since $P$ is an index set, $e \in P \iff f(e) \in P$, which contradicts $e \in P \iff f(e) \notin P$.

Self-duality is invariant under $\equiv_m$: if $P \equiv_m D$ and $D \leq_m \nat \setminus D$, then $P \leq_m D \leq_m \nat \setminus D \leq_m \nat \setminus P$, using item 2 of :ref{#prop-many-one} for the last step and transitivity. By :ref{#ex-join-m}, $D = \emptyset' \oplus (\nat \setminus \emptyset')$ is self-dual, so no index set is many-one equivalent to $D$.

Adapted from Soare 2016, Exercise 2.2.10.
:::
::::

::::exercise{#ex-rice-acceptable difficulty=2 objective="See that Rice's theorem holds in every acceptable numbering, and can fail in a numbering without repetitions." lessons="universal-program-smn"}
1. Let $(\psi_e)$ be an acceptable numbering (:ref{#def-acceptable}), and $\mathcal C$ a class of unary partial computable functions containing some but not all of them. Show that $\{ e : \psi_e \in \mathcal C \}$ is not computable.
2. Admit Friedberg's theorem: there is a numbering $(\psi_e)$ satisfying condition 1 of :ref{#def-acceptable} in which every unary partial computable function appears exactly once. Show that for this numbering, $\{ e : \psi_e = \psi_0 \}$ is computable, although the class $\{ \psi_0 \}$ contains some but not all partial computable functions. Which step of item 1 fails?

:::solution
1. Let $t$ be total computable with $\psi_{t(e)} = \Phi_e$, and $Q = \{ n : \psi_n \in \mathcal C \}$. Then $e \in P = \{ e : \Phi_e \in \mathcal C \} \iff t(e) \in Q$, so $P \leq_m Q$. The set $P$ is a non-trivial index set: every function of $\mathcal C$, and every function outside $\mathcal C$, has a standard index. By :ref{#thm-rice}, $P$ is not computable, so $Q$ is not computable (:ref{#prop-many-one}).
2. Since $\psi_0$ appears only once in the numbering, $\{ e : \psi_e = \psi_0 \} = \{ 0 \}$, which is computable. Item 1 uses condition 2 of :ref{#def-acceptable}, the translation $t$ of standard indices into the numbering. Friedberg's numbering has no such translation, as the lesson on the SMN theorem explains: in an acceptable numbering every function has infinitely many indices.
:::
::::
:::::
