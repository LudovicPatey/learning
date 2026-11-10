---
title: The universal function and the SMN theorem
summary: The universal partial computable function, the SMN theorem and its use with parameters, the padding lemma, and acceptable numberings.
duration: 40
prerequisites: [programs-as-numbers]
---

Two properties of the enumeration $(\Phi_e)$ make it the right framework for computability theory. The first is that it is itself computable: a single algorithm evaluates $\Phi_e(x)$ from $e$ and $x$. The second is that indices can be manipulated computably: from an index of a function of two arguments and a value $x$ of the first argument, one can compute an index of the function of the second argument obtained by fixing $x$. The first property is the **universal function theorem**, the second is the **SMN theorem**. Together they allow one to treat programs as data, which is what the rest of the course does.

## The universal function

:::theorem[Universal function]{#thm-universal}
For every $k \geq 1$, there is an index $u$ such that for all $e$ and $\vec x = (x_1, \dots, x_k)$,
$$
\Phi^{(k+1)}_u(e, \vec x) \simeq \Phi^{(k)}_e(\vec x).
$$
:::

:::proof{of=thm-universal}
By :ref{#cor-universal-function}, the function $(e, \vec x) \mapsto U(\mu s\ T_k(e, \vec x, s))$ is partial computable. Any of its indices is suitable.
:::

A machine of index $u$ is an interpreter: it receives the code of a machine and an input, decodes the machine, and simulates it step by step. The theorem justifies definitions such as
$$
f(x, y) \simeq \Phi_{x+1}(y + 2) \qquad\text{or}\qquad g(e) \simeq \Phi_e(e) + 1,
$$
which are partial computable as compositions of the universal function with computable functions. By contrast, no total computable function enumerates the total computable functions (:ref{#thm-effective-diagonal}): the universal function is necessarily partial.

## The SMN theorem

:::theorem[SMN theorem]{#thm-smn}
For all $m, n \geq 1$, there is a primitive recursive function $S^m_n : \nat^{m+1} \to \nat$ such that for all $e$, $\vec x = (x_1, \dots, x_m)$ and $\vec y = (y_1, \dots, y_n)$,
$$
\Phi^{(n)}_{S^m_n(e, \vec x)}(\vec y) \simeq \Phi^{(m+n)}_e(\vec x, \vec y).
$$
:::

The name comes from Kleene's notation $S^m_n$. The function $S^m_n$ **does not run** the machine $e$: it transforms its code into the code of another machine, which first writes $\vec x$ on the tape in front of its input, then behaves as the machine $e$. Computing this new code is a finite manipulation of a finite table.

:::proof{of=thm-smn}
We treat $m = n = 1$; the general case is identical, with $m$ blocks to write in front of $n$ blocks. Recall the input convention (:ref{#def-tm-computes}): the input $y$ is the block $\ulcorner y \urcorner = 1^{y+1}$ written from cell $0$, and the input $(x, y)$ is $\ulcorner x \urcorner \sqcup \ulcorner y \urcorner$.

For $x \in \nat$, let $P_x$ be a machine which, started on the tape $\ulcorner y \urcorner$ with the head on cell $0$, halts with the tape $\ulcorner x \urcorner \sqcup \ulcorner y \urcorner$ written from some cell $h$, with the head on cell $h$ and in its halting state. For instance, $P_x$ moves left from cell $0$, writes a blank separator on cell $-1$ (already blank), then writes $x + 1$ ones on the cells $-2, -3, \dots, -x - 2$, moving left after each of them, and finally moves one cell back to the right, halting on cell $h = -x - 2$. This takes $x + O(1)$ states, and the transition table of $P_x$ is obtained from $x$ by a primitive recursive function: it is a fixed table with a chain of $x + 1$ writing states inserted.

Let $M_e$ be the machine of code $e$. The machine $P_x ; M_e$ is obtained by renaming the states of $M_e$ so that they are distinct from those of $P_x$, and by identifying the halting state of $P_x$ with the initial state of $M_e$. Started on $\ulcorner y \urcorner$, it runs $P_x$, reaching the configuration in the initial state of $M_e$ with tape $\ulcorner x \urcorner \sqcup \ulcorner y \urcorner$ written from cell $h$ and head on $h$. This is the initial configuration of $M_e$ on input $(x, y)$, translated by $h$. By :ref{#lem-tm-translation}, the subsequent computation is the translate of the computation of $M_e$ on $(x, y)$: it halts in a standard final configuration with output $z$ if and only if $\Phi^{(2)}_e(x, y)\converge = z$. Hence $P_x ; M_e$ computes $y \mapsto \Phi^{(2)}_e(x, y)$.

Let $S^1_1(e, x)$ be the code of $P_x ; M_e$. Renaming states and merging two tables are operations on finite sequences of integers, and with the coding of machines by sequence codes they are primitive recursive (:ref{#prop-seq-operations}). So $S^1_1$ is primitive recursive.
:::

:::quiz[the SMN theorem]
Let $e$ be an index of a machine that never halts. Is $S^1_1(e, 7)$ defined?

- [x] Yes: computing $S^1_1(e, 7)$ only edits the transition table of the machine $e$; it never runs it.

  The result is the code of a machine that never halts either; but the code exists. The distinction between producing an index and running it is the key to the fixed point theorem.
- [ ] No: $S^1_1(e, 7)$ diverges since $\Phi^{(2)}_e(7, y)$ diverges.

  This confuses the program with its behavior. $S^1_1$ is primitive recursive, hence total.
- [ ] It depends on whether $\Phi^{(2)}_e(7, 0)$ converges.

  $S^1_1$ never looks at the behavior of the machine $e$.

---

Why does the proof need the translation lemma?

- [x] Because $P_x$ leaves the input $(x, y)$ written from a cell $h \neq 0$, while the input convention of $M_e$ places it at cell $0$.

  The computation of $M_e$ from a translated initial configuration is the translate of its usual computation, with the same output.
- [ ] To show that $S^1_1$ is primitive recursive.

  This follows from the description of the code, not from the behavior of the machine.
- [ ] Because $M_e$ might move to the left of cell $0$.

  The translation lemma holds whatever the moves of the machine; this is not the issue it addresses.

---

Fix an index $e$ of a two-argument function. What is $y \mapsto \Phi_{S^1_1(e, x)}(y)$?

- [x] $y \mapsto \Phi^{(2)}_e(x, y)$.
- [ ] $y \mapsto \Phi^{(2)}_e(y, x)$.

  The fixed value occupies the **first** argument.
- [ ] $y \mapsto \Phi^{(2)}_x(e, y)$.

  The roles of program and data are exchanged here.
:::

The SMN theorem is mostly used in the following form, which states that a family of partial computable functions, defined uniformly from a parameter, has indices computable from the parameter.

:::corollary[Parameter form]{#cor-smn-parameters}
Let $f : \nat^{1+n} \rightharpoonup \nat$ be partial computable. There is a primitive recursive function $s : \nat \to \nat$ such that for all $x$ and $\vec y$,
$$
\Phi^{(n)}_{s(x)}(\vec y) \simeq f(x, \vec y).
$$
:::

:::proof{of=cor-smn-parameters}
Let $i$ be an index of $f$, and let $s(x) = S^1_n(i, x)$.
:::

In proofs, the corollary is invoked by sentences such as: *"for every $x$, let $s(x)$ be an index of the program which, on input $y$, does … (something depending on $x$ and $y$)"*, it being understood that the description defines a partial computable function of $(x, y)$, and that $s$ is then total computable. We also say that $s(x)$ is obtained **uniformly** in $x$.

:::example{#ex-smn-uses}
1. *Composition of indices.* There is a total computable $c$ with $\Phi_{c(a, b)} = \Phi_a \circ \Phi_b$ for all $a, b$: apply the corollary to $f(\langle a, b \rangle, y) \simeq \Phi_a(\Phi_b(y))$, which is partial computable by the universal function, and compose with the pairing function.
2. *Constant functions.* There is a total computable $\kappa$ such that $\Phi_{\kappa(x)}$ is the constant function with value $x$.
3. *Programs that ignore their input.* There is a total computable $z$ such that $\Phi_{z(e, x)}(y) \simeq \Phi_e(x)$ for all $y$: the program $z(e, x)$ ignores its input and runs $\Phi_e$ on $x$. So $\Phi_{z(e, x)}$ is total if $\Phi_e(x)\converge$, and nowhere defined otherwise. This construction is used in many reductions.
:::

## The padding lemma

Every partial computable function has infinitely many indices: adding to a machine states that are never entered does not change what it computes. The indices can moreover be found computably, and above any given bound.

:::lemma[Padding lemma]{#lem-padding}
There is a primitive recursive function $p : \nat^2 \to \nat$ such that for all $e$ and $n$, $p(e, n) \geq n$ and $\Phi^{(k)}_{p(e, n)} = \Phi^{(k)}_e$ for every $k$.
:::

:::proof{of=lem-padding}
Let $M_e$ be the machine of code $e$ (the fixed never-halting machine if $e$ is not a code). For $j \in \nat$, let $M_{e, j}$ be $M_e$ with $j$ additional states, which are never entered and whose transitions are arbitrary, say "write a blank, move right, stay in the same state". Its computations are those of $M_e$, so it computes the same functions. The machines $M_{e, 0}, M_{e, 1}, \dots$ have different numbers of states, so their codes $c(e, j)$ are pairwise distinct, and $c$ is primitive recursive. Among the $n + 1$ distinct values $c(e, 0), \dots, c(e, n)$, at most $n$ lie below $n$, so one of them is at least $n$. Let $p(e, n) = c(e, j)$ for the least $j \leq n$ with $c(e, j) \geq n$, a bounded search.
:::

:::corollary{#cor-infinitely-many-indices}
Every partial computable function has infinitely many indices. Consequently, the set of indices of a given partial computable function is never finite, and for every $e$ the function $n \mapsto p(e, n)$ enumerates infinitely many of the indices of $\Phi_e$.
:::

:::proof{of=cor-infinitely-many-indices}
If $f = \Phi_e$, the indices $p(e, n)$, for $n \in \nat$, are unbounded since $p(e, n) \geq n$, hence infinitely many.
:::

:::quiz[the padding lemma]
What is the role of the condition $p(e, n) \geq n$?

- [x] It makes the indices $p(e, 0), p(e, 1), \dots$ unbounded, hence infinitely many, and it allows one to find an index of $\Phi_e$ above any given bound.

  The second use appears in constructions where an index must avoid a finite set of indices already used.
- [ ] It ensures that $p$ is total.

  Totality comes from the bounded search, whose bound is justified by the counting argument.
- [ ] It ensures that the machine $p(e, n)$ runs for at least $n$ steps.

  The added states are never entered: the running time is unchanged.

---

The proof searches for $j \leq n$. Why does some $j \leq n$ satisfy $c(e, j) \geq n$?

- [x] The $n + 1$ values $c(e, 0), \dots, c(e, n)$ are distinct, and only $n$ integers lie below $n$.

  The pigeonhole principle, in its simplest form.
- [ ] Because $c(e, j) \geq j$ for every $j$.

  This is not claimed; the code of a machine with more states need not be larger.
- [ ] Because $c$ is increasing in $j$.

  Monotonicity depends on details of the coding that the proof avoids.
:::

## Acceptable numberings

The results of this course depend on the enumeration $(\Phi_e)$ only through a few properties. It is useful to know which ones.

:::definition{#def-acceptable}
A **numbering** of the unary partial computable functions is a sequence $(\psi_e)_{e \in \nat}$ in which every unary partial computable function appears. It is **acceptable** if

1. the function $(e, x) \mapsto \psi_e(x)$ is partial computable, and
2. there is a total computable $t$ with $\psi_{t(e)} = \Phi_e$ for every $e$.
:::

:::proposition{#prop-acceptable}
The numbering $(\Phi_e)$ is acceptable. If $(\psi_e)$ is acceptable, there is a total computable $r$ with $\Phi_{r(e)} = \psi_e$ for every $e$, and $(\psi_e)$ satisfies the SMN theorem: there is a total computable $\sigma$ such that $\psi_{\sigma(e, x)}(y) \simeq \psi_e(\langle x, y \rangle)$.
:::

:::proof{of=prop-acceptable}
For $(\Phi_e)$, take the universal function and $t$ the identity. Let $(\psi_e)$ be acceptable. By :ref{#cor-smn-parameters} applied to $(e, x) \mapsto \psi_e(x)$, there is a total computable $r$ with $\Phi_{r(e)}(x) \simeq \psi_e(x)$. For SMN, apply :ref{#cor-smn-parameters} to $(\langle e, x \rangle, y) \mapsto \psi_e(\langle x, y \rangle)$, giving a total computable $s$ with $\Phi_{s(\langle e, x \rangle)}(y) \simeq \psi_e(\langle x, y \rangle)$, and let $\sigma(e, x) = t(s(\langle e, x \rangle))$.
:::

Rogers proved that any two acceptable numberings differ by a computable permutation of the indices: if $(\psi_e)$ is acceptable, there is a computable bijection $\pi : \nat \to \nat$ with $\psi_e = \Phi_{\pi(e)}$. We admit this **isomorphism theorem**. It shows that every result of this course that is stated in terms of indices holds for every acceptable numbering. Not every numbering is acceptable: Friedberg constructed a numbering satisfying the first condition in which each partial computable function appears **exactly once**. By the padding lemma, such a numbering cannot be acceptable.

## Exercises

::::exercise{difficulty=1}
Show that there is a total computable function $g$ such that $\Phi_{g(e)}(x) \simeq 2 \cdot \Phi_e(x)$ for all $e$ and $x$, and that $g$ can be chosen injective.

:::solution
Apply :ref{#cor-smn-parameters} to $f(e, x) \simeq 2 \cdot \Phi_e(x)$, to get $s$ with $\Phi_{s(e)} = 2 \cdot \Phi_e$. To make it injective, let $g(0) = s(0)$ and $g(e+1) = p(s(e+1), g(e) + 1)$, where $p$ is the padding function. Then $g(e+1) \geq g(e) + 1$, so $g$ is strictly increasing, hence injective, and $\Phi_{g(e)} = \Phi_{s(e)}$.
:::
::::

::::exercise{difficulty=2}
Show that there is no total computable function $f$ such that, for every $e$, $\Phi_{f(e)}$ is total, and $\Phi_{f(e)} = \Phi_e$ whenever $\Phi_e$ is total.

:::solution
Suppose $f$ exists. Then $\Phi_{f(0)}, \Phi_{f(1)}, \dots$ is a sequence of total functions, uniformly computable since $(e, x) \mapsto \Phi_{f(e)}(x)$ is partial computable and total. It contains every total computable function $\Phi_e$, as $\Phi_{f(e)}$. This contradicts :ref{#thm-effective-diagonal}.
:::
::::

## Notes and references

The universal function is Turing's universal machine (1936), and the SMN theorem is due to Kleene (1938). Acceptable numberings and the isomorphism theorem are due to Rogers (1958); Friedberg's numbering without repetitions appeared the same year.

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- S. C. Kleene, *On notation for ordinal numbers*, Journal of Symbolic Logic 3 (1938), 150–155.
- H. Rogers, *Gödel numberings of partial recursive functions*, Journal of Symbolic Logic 23 (1958), 331–341.
- R. M. Friedberg, *Three theorems on recursive enumeration*, Journal of Symbolic Logic 23 (1958), 309–316.
