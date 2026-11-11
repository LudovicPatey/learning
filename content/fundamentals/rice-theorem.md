---
title: Rice's theorem
summary: Non-trivial index sets are not computable; the halting set reduces to them; c.e. index sets are monotone and determined by finite information.
duration: 40
prerequisites: [fixed-point, ce-sets]
---

The halting problem is one undecidable question about programs. Rice's theorem shows that it is typical: no question about the **function computed** by a program can be decided from its index, except the trivial ones. This lesson proves the theorem twice, by the fixed point theorem and by a reduction from the halting set, and then determines which questions about the function computed can at least be **confirmed**, that is, which index sets are computably enumerable.

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

:::quiz[the reduction]
In the proof of :ref{#prop-rice-reduction}, why must $z \notin P$ be assumed?

- [x] For $e \notin \emptyset'$, the program $g(e)$ computes the nowhere defined function, and the reduction needs $g(e) \notin P$ in that case.
- [ ] To ensure that $g$ is total.

  $g$ is total by SMN in any case.
- [ ] Because $P$ would otherwise be trivial.

  $P$ can be non-trivial and contain $z$, for instance $P = \{ e : W_e = \emptyset \}$.
:::

## Which index sets are c.e.

Some non-trivial index sets are c.e., for instance $\{ e : \Phi_e(3)\converge \}$ and $\{ e : W_e \neq \emptyset \}$; others are not, such as $\mathrm{Tot}$ (:ref{#cor-tot-not-ce}). The following theorem gives two necessary conditions. For partial functions, write $\theta \subseteq f$ if $f$ extends $\theta$, that is, $\theta(x)\converge = y$ implies $f(x)\converge = y$.

:::theorem[Rice–Shapiro, necessity]{#thm-rice-shapiro}
Let $\mathcal C$ be a class of unary partial computable functions such that $P = \{ e : \Phi_e \in \mathcal C \}$ is c.e. Then:

1. *(monotonicity)* if $f \in \mathcal C$ and $g$ is partial computable with $f \subseteq g$, then $g \in \mathcal C$;
2. *(finiteness)* if $f \in \mathcal C$, then some finite function $\theta \subseteq f$ belongs to $\mathcal C$.
:::

:::proof{of=thm-rice-shapiro}
In both cases, we reduce $\nat \setminus \emptyset'$ to $P$, which is impossible since $\nat \setminus \emptyset'$ is not c.e. (:ref{#thm-halting-ce}) while $P$ is (:ref{#prop-ce-downward}).

1. Suppose $f \in \mathcal C$, $f \subseteq g$, $g$ partial computable and $g \notin \mathcal C$. By :ref{#cor-smn-parameters}, there is a total computable $h$ such that the program $h(e)$, on input $x$, runs the computations of $f(x)$ and of $\Phi_e(e)$ in parallel, stage by stage: if $f(x)$ converges first (or at the same stage), it outputs $f(x)$; if $\Phi_e(e)$ converges first, it computes and outputs $g(x)$. If $e \notin \emptyset'$, the second case never occurs and $\Phi_{h(e)} = f \in \mathcal C$. If $e \in \emptyset'$, then $\Phi_{h(e)} = g$: on $x \in \mathrm{dom}(f)$, both cases give $f(x) = g(x)$; on $x \notin \mathrm{dom}(f)$, only the second case can occur, and gives $g(x)$. So $\Phi_{h(e)} \notin \mathcal C$, and $h$ reduces $\nat \setminus \emptyset'$ to $P$.
2. Suppose $f \in \mathcal C$ and no finite $\theta \subseteq f$ is in $\mathcal C$. Let $h$ be total computable such that $\Phi_{h(e)}(x) \simeq f(x)$ if $\Phi_e(e)[x]\diverge$, and $\Phi_{h(e)}(x)$ is undefined otherwise. If $e \notin \emptyset'$, then $\Phi_{h(e)} = f \in \mathcal C$. If $e \in \emptyset'$, let $s$ be the least stage with $\Phi_e(e)[s]\converge$; then $\Phi_{h(e)}$ is the restriction of $f$ to $\{0, \dots, s - 1\}$, a finite function contained in $f$, hence not in $\mathcal C$. So $h$ reduces $\nat \setminus \emptyset'$ to $P$.
:::

The converse also holds, with a suitable formulation: $P$ is c.e. if and only if $\mathcal C$ is the class of partial computable functions extending some member of a c.e. list of finite functions (given by canonical codes). We admit this sufficiency part, which is proved in Rogers' and Odifreddi's books (in the sections on index sets and the Rice–Shapiro theorem).

:::corollary{#cor-rice-shapiro-examples}
The following index sets are not c.e.: $\mathrm{Tot}$; $\{ e : W_e \text{ is infinite} \}$; $\{ e : W_e \text{ is finite} \}$; $\{ e : W_e = \emptyset \}$; $\{ e : \Phi_e = \Phi_a \}$ for any index $a$ of a total function.
:::

:::proof{of=cor-rice-shapiro-examples}
For $\mathrm{Tot}$, $\{ e : W_e \text{ infinite} \}$ and $\{ e : \Phi_e = \Phi_a \}$ with $\Phi_a$ total, finiteness fails: these classes contain an infinite function, total or with infinite domain, but no finite function. For $\{ e : W_e \text{ finite} \}$ and $\{ e : W_e = \emptyset \}$, monotonicity fails: the nowhere defined function belongs to the class, and its extension the constant function $0$ does not.
:::

:::quiz[Rice–Shapiro]
In part 1 of the proof, why are the computations of $f(x)$ and $\Phi_e(e)$ run in parallel, rather than computing $\Phi_e(e)$ first?

- [x] If $e \notin \emptyset'$, the program must still compute $f$; waiting for $\Phi_e(e)$ would make it diverge everywhere.
- [ ] To make $h$ total.

  $h$ is total by SMN, whatever the program described.
- [ ] Because $f$ is total.

  $f$ is not assumed total.

---

The set $\{ e : W_e \neq \emptyset \}$ is c.e. How does it satisfy the two conditions?

- [x] A function with non-empty domain has a one-point subfunction with non-empty domain, and every extension of it has non-empty domain.
- [ ] It does not satisfy them, which shows that the conditions are not necessary.

  The conditions are necessary: they hold for every c.e. index set.
- [ ] Only finiteness holds.

  Monotonicity holds too: extending a function enlarges its domain.
:::

## Consequences

Rice's theorem is a limitation on the automatic analysis of programs. Whether a program meets a behavioral specification — computes a given function, halts on all inputs, never outputs $0$ — is undecidable in general. In practice, program analysis tools either restrict the programs considered, or accept answers that may be inconclusive. The theorem is about **decidability** only. Questions of the form "does the program ever do this?" are often c.e., while questions about all inputs, such as totality, are typically not even c.e. Measuring their exact difficulty is the purpose of the arithmetic hierarchy, the subject of a later course.

## Exercises

::::exercise{difficulty=1}
Show that there is no algorithm which, given $a$ and $b$, decides whether $\Phi_a = \Phi_b$.

:::solution
Fix an index $z$ of the nowhere defined function. If equality were decidable, the set $\{ e : \Phi_e = \Phi_z \}$ would be computable. It is an index set, non-trivial since it contains $z$ and no index of the constant function $0$. This contradicts :ref{#thm-rice}.
:::
::::

::::exercise{difficulty=1}
Is $\{ e : \Phi_e(0)\converge \text{ and } \Phi_e(1)\diverge \}$ c.e.?

:::solution
No. It is an index set, and monotonicity fails: the function defined only at $0$ belongs to the class, and its extension defined at $0$ and $1$ does not. By :ref{#thm-rice-shapiro}, the set is not c.e.
:::
::::

::::exercise{difficulty=2}
Show that $\{ e : W_e \text{ is computable} \}$ is not c.e.

:::solution
It is an index set. Monotonicity fails: the nowhere defined function has the computable domain $\emptyset$, while its extension $g(x) \simeq 0$ if $x \in \emptyset'$, undefined otherwise, is partial computable with domain $\emptyset'$, which is not computable. By :ref{#thm-rice-shapiro}, the set is not c.e.
:::
::::

## Notes and references

Rice's theorem appeared in 1953, in a paper on classes of c.e. sets; Rice and Shapiro characterized independently, in 1956, the classes of c.e. sets whose index sets are c.e. The analogous result for partial computable functions is the Myhill–Shepherdson theorem (1955), which states that effective operations on partial computable functions are continuous, in the sense that their values depend on finite information.

- H. G. Rice, *Classes of recursively enumerable sets and their decision problems*, Transactions of the American Mathematical Society 74 (1953), 358–366.
- H. G. Rice, *On completely recursively enumerable classes and their key arrays*, Journal of Symbolic Logic 21 (1956), 304–308.
- N. Shapiro, *Degrees of computability*, Transactions of the American Mathematical Society 82 (1956), 281–299.
- J. Myhill and J. C. Shepherdson, *Effective operations on partial recursive functions*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 1 (1955), 310–317.
- H. Rogers, *Theory of Recursive Functions and Effective Computability*, McGraw-Hill, 1967.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989.
