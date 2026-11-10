---
title: The halting problem
summary: Undecidability of the halting problem, by diagonalization against the enumeration of partial computable functions.
duration: 15
prerequisites: [universal-program-smn, countability/diagonal-argument]
---

We now exhibit a concrete set which is not computable: the set of programs which halt on their own code. The proof, due to Turing (1936), is a diagonal argument against the enumeration $\Phi_0, \Phi_1, \Phi_2, \dots$ of all partial computable functions.

:::definition{#def-halting}
The **halting problem** is the set
$$
\emptyset' = \{ e \in \nat : \Phi_e(e)\converge \}
$$
of codes of programs that halt when given their own code as input.
:::

The choice of the input $e$ for the program $e$ corresponds to the diagonal of the table whose rows are the programs and whose columns are the inputs — the same table Cantor used, now with a computable row enumeration.

:::theorem{#thm-halting}
The set $\emptyset'$ is not computable.
:::

:::proof{of=thm-halting}
Suppose some total computable function $h$ decides $\emptyset'$. Consider the program $D$:

```js
function D(x) {
  if (h(x) == 1) {      // program x halts on x
    while (true) {}     // ... so loop forever
  }
  return 0;             // otherwise, halt
}
```

$D$ is computable, so it has a code $d$. For every $x$, $\Phi_d(x)\converge$ if and only if $x \notin \emptyset'$, that is, iff $\Phi_x(x)\diverge$. Taking $x = d$:
$$
\Phi_d(d)\converge \iff \Phi_d(d)\diverge,
$$
a contradiction. So no such $h$ exists.
:::

:::quiz
Where is the hypothesis "$h$ is total" used?

- [x] To make sure that $D$ itself halts whenever $\Phi_x(x)\diverge$: the test `h(x) == 1` must return.

  If $h(d)$ could diverge, then $\Phi_d(d)$ would simply diverge, and no contradiction would follow.
- [ ] To show that $D$ has a code.

  Every computable function has a code, total or not.
- [ ] It is not used.

---

Why is the equivalence $\Phi_d(x)\converge \iff \Phi_x(x)\diverge$ applied at $x = d$?

- [x] It makes $D$ answer about **itself**: the row $d$ of the table disagrees with the diagonal at column $d$, which is its own entry.
- [ ] Because $d$ is the smallest code of $D$.

  Any code of $D$ works.
- [ ] Any $x$ would give a contradiction.

  For $x \neq d$ the equivalence is consistent: it just relates two different programs.

---

Compare with Cantor's argument. Which part corresponds to "flipping the diagonal bit"?

- [x] $D$ loops on $x$ exactly when $\Phi_x$ halts on $x$, and halts exactly when it loops.
- [ ] Computing $h(x)$.

  $h$ only *reads* the diagonal entry.
- [ ] Choosing a code $d$ for $D$.

  That is the step "$Y$ would have to be one of the rows".
:::

## Many-one variants

The problem "does $\Phi_e$ halt on input $x$?" — the set $H = \{ \langle e, x \rangle : \Phi_e(x)\converge \}$ — is also undecidable: a decision procedure for $H$ would decide $\emptyset'$, since $e \in \emptyset'$ iff $\langle e, e \rangle \in H$. This idea of transferring undecidability from one problem to another is called a **reduction**. Many undecidable problems in mathematics — Hilbert's tenth problem, the word problem for groups, the validity of first-order formulas — are proved undecidable by reducing the halting problem to them.

:::quiz
Which statements are correct?

- [x] For each single $e$, the question "is $e \in \emptyset'$?" has an answer that some program outputs.

  One of the two constant programs (always $0$, always $1$) gives the right answer. Undecidability is about **one program answering for all $e$**.
- [x] There is no algorithm deciding, given $e$, whether $\Phi_e(0)\converge$.

  Reduce: from $e$, compute the code of the program that ignores its input and runs $\Phi_e(e)$. It halts on $0$ iff $e \in \emptyset'$.
- [ ] Since $\emptyset'$ is not computable, there is no program that halts exactly on the elements of $\emptyset'$.

  The program "on input $e$, run $\Phi_e(e)$" does exactly that. See the next lesson.
:::
