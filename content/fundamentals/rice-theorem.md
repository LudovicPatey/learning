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

## Consequences

Rice's theorem is a limitation on the automatic analysis of programs. Whether a program meets a behavioral specification — computes a given function, halts on all inputs, never outputs $0$ — is undecidable in general. In practice, program analysis tools either restrict the programs considered, or accept answers that may be inconclusive. The theorem is about **decidability** only. Questions of the form "does the program ever do this?" are often c.e., while questions about all inputs, such as totality, are typically not even c.e.; the next lesson characterizes the c.e. index sets. Measuring their exact difficulty is the purpose of the arithmetic hierarchy, the subject of a later course.

## Exercises

::::exercise{difficulty=1}
Show that there is no algorithm which, given $a$ and $b$, decides whether $\Phi_a = \Phi_b$.

:::solution
Fix an index $z$ of the nowhere defined function. If equality were decidable, the set $\{ e : \Phi_e = \Phi_z \}$ would be computable. It is an index set, non-trivial since it contains $z$ and no index of the constant function $0$. This contradicts :ref{#thm-rice}.
:::
::::

::::exercise{difficulty=2}
Let $P$ be a non-trivial index set. Show that $P$ and $\nat \setminus P$ cannot both be c.e. Deduce that if $P$ is c.e., the indices of the nowhere defined function are not in $P$.

:::solution
If both were c.e., $P$ would be computable by :ref{#prop-computable-iff-ce-coce}, contradicting :ref{#thm-rice}. If $P$ is c.e. and contains an index $z$ of the nowhere defined function, then $\emptyset' \leq_m \nat \setminus P$ by :ref{#prop-rice-reduction}, that is, $\nat \setminus \emptyset' \leq_m P$ by item 2 of :ref{#prop-many-one}; so $\nat \setminus \emptyset'$ would be c.e. by :ref{#prop-ce-downward}, contradicting :ref{#thm-halting-ce}.
:::
::::

## Notes and references

Rice's theorem appeared in 1953, in a paper on classes of c.e. sets. In Soare's textbook, the reduction of :ref{#prop-rice-reduction} is the index set theorem (Theorem 1.6.13), Rice's theorem is Corollary 1.6.14, and the proof by the fixed point theorem is Exercise 2.2.10. Monin and Patey present Rice's theorem in their chapter on the arithmetic hierarchy, and derive it from the fixed point theorem in an exercise of their chapter on the foundations of computability.

- H. G. Rice, *Classes of recursively enumerable sets and their decision problems*, Transactions of the American Mathematical Society 74 (1953), 358–366.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 1.6.3 and 2.2.
- B. Monin and L. Patey, *Computability theory*, chapter *Arithmetic hierarchy*, section *Rice's theorem*.
