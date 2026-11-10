---
title: The halting problem
summary: Undecidability of the halting problem; many-one reductions; undecidability of totality and of halting on a fixed input.
duration: 35
prerequisites: [universal-program-smn, countability/diagonal-argument]
---

This lesson proves that the halting problem is not computable, and introduces the main tool for transferring undecidability from one problem to another: many-one reductions. With them, the undecidability of the halting problem propagates to many other questions about programs — halting on a fixed input, totality, emptiness of the domain — and, outside computability theory, to problems of number theory, group theory and logic.

## The halting set

:::definition{#def-halting}
The **halting set**, or **halting problem**, is
$$
\emptyset' = \{ e \in \nat : \Phi_e(e)\converge \}.
$$
The set $H = \{ \langle e, x \rangle : \Phi_e(x)\converge \}$ is the **general halting set**.
:::

The notation $\emptyset'$, read "zero jump", comes from the theory of the Turing jump: $\emptyset'$ is the jump of the empty set. The restriction to the diagonal $x = e$ makes the diagonal argument direct; the general halting set has the same degree of difficulty, as shown below.

:::theorem{#thm-halting}
The set $\emptyset'$ is not computable.
:::

:::proof{of=thm-halting}
Suppose $\emptyset'$ is computable. Consider the following algorithm $D$: on input $x$, decide whether $x \in \emptyset'$; if so, enter an infinite loop; otherwise, halt with output $0$. By :ref{#prop-computable-closure}, $D$ computes a partial computable function, so it has an index $d$, and for every $x$,
$$
\Phi_d(x)\converge \iff x \notin \emptyset' \iff \Phi_x(x)\diverge.
$$
For $x = d$, this gives $\Phi_d(d)\converge \iff \Phi_d(d)\diverge$, a contradiction.
:::

This is Cantor's diagonal argument applied to the table whose rows are the partial functions $\Phi_e$: the algorithm $D$ differs from row $x$ at column $x$, by converging where it diverges and diverging where it converges. The same argument is presented in the course on countability in a slightly different form, through partial functions without total extensions (:ref{#cor-halting-diagonal}).

:::quiz[the proof of the theorem]
Where is the hypothesis "$\emptyset'$ is computable" used?

- [x] To make the test "$x \in \emptyset'$" in $D$ always terminate, so that $D$ halts whenever $\Phi_x(x)\diverge$.

  If the test could diverge, $D$ would diverge on such $x$ as well, and the equivalence $\Phi_d(x)\converge \iff \Phi_x(x)\diverge$ would fail.
- [ ] To show that $D$ has an index.

  Every partial computable function has an index. The issue is whether $D$ is partial computable with the required behavior.
- [ ] It is not used.

---

Why is the equivalence $\Phi_d(x)\converge \iff \Phi_x(x)\diverge$ applied with $x = d$?

- [x] So that the two sides concern the same computation, $\Phi_d(d)$: the row $d$ disagrees with the diagonal at its own column.
- [ ] Because $d$ is the least index of $D$.

  Any index of $D$ works.
- [ ] Any $x$ would give a contradiction.

  For $x \neq d$ the equivalence relates two different computations and is consistent.

---

Which step corresponds to "flipping the diagonal bit" in Cantor's argument?

- [x] $D$ loops on $x$ exactly when $\Phi_x(x)$ halts, and halts exactly when it loops.
- [ ] Deciding whether $x \in \emptyset'$.

  This only reads the diagonal entry.
- [ ] Choosing an index $d$ for $D$.

  This corresponds to the step "$Y$ would be one of the rows".
:::

## Many-one reductions

:::definition{#def-many-one}
Let $A, B \subseteq \nat$. A **many-one reduction** of $A$ to $B$ is a total computable function $f$ such that for all $x$,
$$
x \in A \iff f(x) \in B.
$$
We write $A \leq_m B$ if such an $f$ exists, and $A \equiv_m B$ if $A \leq_m B$ and $B \leq_m A$.
:::

The reduction transforms each question "$x \in A$?" into a question "$f(x) \in B$?" with the same answer. When $f$ is moreover injective, one speaks of a **one-one reduction**, written $A \leq_1 B$.

:::proposition{#prop-many-one}
1. The relation $\leq_m$ is reflexive and transitive.
2. $A \leq_m B$ if and only if $\nat \setminus A \leq_m \nat \setminus B$.
3. If $A \leq_m B$ and $B$ is computable, then $A$ is computable. Equivalently, if $A \leq_m B$ and $A$ is not computable, then $B$ is not computable.
:::

:::proof{of=prop-many-one}
1. The identity reduces $A$ to $A$. If $f$ reduces $A$ to $B$ and $g$ reduces $B$ to $C$, then $g \circ f$ is total computable and $x \in A \iff f(x) \in B \iff g(f(x)) \in C$.
2. The same $f$ works: $x \notin A \iff f(x) \notin B$.
3. $\chi_A = \chi_B \circ f$ is total computable.
:::

To show that a set $B$ is not computable, it therefore suffices to reduce a non-computable set, typically $\emptyset'$, to $B$. Most reductions from $\emptyset'$ are built with the SMN theorem: from $e$, one computes the index of a program whose behavior depends on whether $\Phi_e(e)$ converges.

:::proposition{#prop-halting-variants}
1. $\emptyset' \equiv_m H$.
2. $\emptyset' \leq_m \{ e : \Phi_e(0)\converge \}$, and $\emptyset' \leq_m \{ e : \mathrm{dom}(\Phi_e) \neq \emptyset \}$.
3. $\emptyset' \leq_m \mathrm{Tot}$ and $\nat \setminus \emptyset' \leq_m \mathrm{Tot}$, where $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$.

In particular, none of these sets is computable.
:::

:::proof{of=prop-halting-variants}
1. $e \mapsto \langle e, e \rangle$ reduces $\emptyset'$ to $H$. Conversely, let $z$ be the function of :ref{#ex-smn-uses}, with $\Phi_{z(e, x)}(y) \simeq \Phi_e(x)$ for all $y$. Then $\langle e, x \rangle \in H \iff \Phi_e(x)\converge \iff \Phi_{z(e, x)}(z(e, x))\converge \iff z(e, x) \in \emptyset'$, so $\langle e, x \rangle \mapsto z(e, x)$ reduces $H$ to $\emptyset'$. (The function $n \mapsto z(\pi_0(n), \pi_1(n))$ is total computable, since the inverses $\pi_0, \pi_1$ of the pairing function are.)
2. With the same $z$, the function $\Phi_{z(e, e)}$ is total if $e \in \emptyset'$ and nowhere defined otherwise. So $e \mapsto z(e, e)$ reduces $\emptyset'$ to both sets, and also to $\mathrm{Tot}$, which proves the first half of item 3.
3. For the second half, let $g$ be total computable, given by :ref{#cor-smn-parameters}, such that
$$
\Phi_{g(e)}(x) \simeq \begin{cases} 0 & \text{if } \Phi_e(e)[x]\diverge,\\ \text{undefined} & \text{if } \Phi_e(e)[x]\converge. \end{cases}
$$
This is a definition by cases with a computable condition (:ref{#prop-stage-properties}). If $e \notin \emptyset'$, then $\Phi_e(e)[x]\diverge$ for every $x$, and $\Phi_{g(e)}$ is total. If $e \in \emptyset'$, then $\Phi_e(e)[x]\converge$ for all large $x$, and $\Phi_{g(e)}$ is not total. So $g$ reduces $\nat \setminus \emptyset'$ to $\mathrm{Tot}$.
:::

The second half of item 3 is stronger than it looks. The lesson on computably enumerable sets shows that $\nat \setminus \emptyset'$ is not computably enumerable, and that sets reducible to a computably enumerable set are computably enumerable. Hence $\mathrm{Tot}$ is not computably enumerable; and by item 2 of :ref{#prop-many-one}, its complement is not either. Totality is strictly harder than halting, a fact made precise by the arithmetic hierarchy.

:::quiz[reductions from the halting set]
In the reduction of $\emptyset'$ to $\{ e : \Phi_e(0)\converge \}$, what does the program $z(e, e)$ do on input $0$?

- [x] It ignores its input and runs $\Phi_e(e)$, so it halts on $0$ if and only if $e \in \emptyset'$.
- [ ] It runs $\Phi_e(0)$.

  That would reduce the wrong set: it relates $\Phi_e(0)$, not $\Phi_e(e)$.
- [ ] It decides whether $e \in \emptyset'$.

  No program does that. The reduction only computes an index; the hard question is transferred to the target set.

---

In the reduction $g$ of $\nat \setminus \emptyset'$ to $\mathrm{Tot}$, why does $\Phi_{g(e)}(x)$ test convergence at stage $x$ instead of running $\Phi_e(e)$ to completion?

- [x] Because the test must be decidable, so that $\Phi_{g(e)}(x)$ converges when $e \notin \emptyset'$; running $\Phi_e(e)$ would diverge exactly in that case.

  The stage test is a bounded simulation, which always terminates.
- [ ] To make $g$ total.

  $g$ is total by the parameter form of SMN, whatever the program it describes.
- [ ] Because $\Phi_e(e)$ converges at stage $x$ for every $x$.

  It converges at all large stages if $e \in \emptyset'$, and at none otherwise.

---

Which statements are correct?

- [x] For each single $e$, some program outputs the correct answer to "$e \in \emptyset'$?".

  One of the two constant programs does. Undecidability concerns a single program answering for all $e$.
- [x] If $A \leq_m B$ and $B$ is computable, then $A$ is computable.
- [ ] If $A \leq_m B$ and $A$ is computable, then $B$ is computable.

  Every computable set reduces to $\emptyset'$, as to any set other than $\emptyset$ and $\nat$ (see the exercises).
:::

## Undecidable problems in mathematics

Reductions from the halting problem show that many natural mathematical problems are undecidable. The following results are admitted; each is proved by coding computations into the problem considered.

- **The Entscheidungsproblem.** The set of (codes of) valid formulas of first-order logic is not computable (Church, Turing, 1936). Later work showed that a language with a single binary relation symbol suffices.
- **The word problem for groups.** There is a finitely presented group for which the set of words equal to the identity is not computable (Novikov, 1955; Boone, 1959).
- **Hilbert's tenth problem.** The set of polynomial equations with integer coefficients having a solution in integers is not computable (Matiyasevich, 1970, completing work of Davis, Putnam and Robinson). More precisely, every computably enumerable set is Diophantine, and therefore $\emptyset'$ reduces to the solvability of Diophantine equations.

## Exercises

::::exercise{difficulty=1}
Show that if $A$ is computable and $B \neq \emptyset$, $B \neq \nat$, then $A \leq_m B$. What happens if $B = \emptyset$ or $B = \nat$?

:::solution
Fix $b_1 \in B$ and $b_0 \notin B$, and let $f(x) = b_1$ if $x \in A$ and $f(x) = b_0$ otherwise; $f$ is total computable and reduces $A$ to $B$. If $B = \emptyset$, then $A \leq_m B$ forces $A = \emptyset$, since no $f(x)$ lies in $B$; similarly, $A \leq_m \nat$ forces $A = \nat$.
:::
::::

::::exercise{difficulty=1}
Show that $\{ e : \Phi_e(e)\converge = 0 \}$ is not computable.

:::solution
Let $g$ be total computable with $\Phi_{g(e)}(y) \simeq 0$ if $\Phi_e(e)\converge$, and undefined otherwise; it exists by :ref{#cor-smn-parameters}, since the right-hand side is a partial computable function of $(e, y)$. Then $e \in \emptyset' \iff \Phi_{g(e)}(g(e))\converge = 0$, so $g$ reduces $\emptyset'$ to the set.
:::
::::

::::exercise{difficulty=2}
Let $\mathrm{Inf} = \{ e : \mathrm{dom}(\Phi_e) \text{ is infinite} \}$. Show that $\emptyset' \leq_m \mathrm{Inf}$ and $\nat \setminus \emptyset' \leq_m \mathrm{Inf}$.

:::solution
The reduction $e \mapsto z(e, e)$ of :ref{#prop-halting-variants} sends $e \in \emptyset'$ to an index of a total function, whose domain is infinite, and $e \notin \emptyset'$ to an index of the nowhere defined function. The reduction $g$ of item 3 sends $e \notin \emptyset'$ to an index of a total function, and $e \in \emptyset'$ to an index of a function whose domain is $\{ x : \Phi_e(e)[x]\diverge \}$, a finite initial segment of $\nat$.
:::
::::

## Notes and references

Turing proved in 1936 that no machine decides whether a given machine is circle-free, and deduced the unsolvability of the Entscheidungsproblem; Church obtained the latter independently with the λ-calculus. Many-one reducibility was introduced by Post in 1944, in the paper that founded the study of computably enumerable sets and their degrees. Davis' book on Hilbert's tenth problem and Lyndon and Schupp's on combinatorial group theory present the undecidability results listed above.

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- A. Church, *A note on the Entscheidungsproblem*, Journal of Symbolic Logic 1 (1936), 40–41.
- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- M. Davis, *Hilbert's tenth problem is unsolvable*, American Mathematical Monthly 80 (1973), 233–269.
- Y. V. Matiyasevich, *Hilbert's Tenth Problem*, MIT Press, 1993.
