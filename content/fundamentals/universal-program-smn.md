---
title: The universal program and the SMN theorem
summary: Existence of a universal partial computable function, the SMN theorem, and the padding lemma.
duration: 15
prerequisites: [programs-as-numbers]
---

## The universal program

Turing's model defines one machine per computable function — as if one built a dedicated robot for each task. His first fundamental theorem says that a single machine can simulate all the others. This is the theoretical ancestor of the stored-program computer.

:::theorem[Universal program]{#thm-universal}
Let $n \geq 1$. There is a code $u$ such that for all $a, x_1, \dots, x_n$:

- $\Phi_u(a, x_1, \dots, x_n)\diverge$ if and only if $\Phi_a(x_1, \dots, x_n)\diverge$;
- $\Phi_u(a, x_1, \dots, x_n)\converge = y$ if and only if $\Phi_a(x_1, \dots, x_n)\converge = y$.
:::

Concretely, a universal program is an *interpreter* or a *virtual machine*: it decodes the program it receives and executes it step by step. For instance, the Java virtual machine runs any Java program.

The theorem lets us define functions that manipulate codes and run them. For example
$$
f(x, y) = \Phi_{x+1}(y+2)
$$
is a valid definition of a partial computable function, since $f(x, y) = \Phi_u(x+1, y+2)$.

## The SMN theorem

Given a program with $m + n$ inputs, we can "hard-code" the first $m$ inputs and obtain a program with $n$ inputs. The key point is that the new code is obtained **computably** from the old code and the hard-coded values.

:::theorem[SMN theorem]{#thm-smn}
For all $m, n \geq 1$ there is a **total** computable function $S^m_n : \nat^{m+1} \to \nat$ such that for all $e, x_1, \dots, x_m, y_1, \dots, y_n$:
$$
\Phi_{S^m_n(e, x_1, \dots, x_m)}(y_1, \dots, y_n) = \Phi_e(x_1, \dots, x_m, y_1, \dots, y_n).
$$
:::

:::proof{of=thm-smn}
Given $e, x_1, \dots, x_m$, decode $e$ to get the program $P_e$, edit it to add instructions assigning the values $x_1, \dots, x_m$ to the corresponding variables, and compute the code of the new program. For example, if $\Phi_e : \nat^4 \to \nat$ is

```js
function MyProgram(x1, x2, x3, x4) {
  // CODE
}
```

then $\Phi_{S^2_2(e, 5, 3)}$ is the program

```js
function MyProgram2(x3, x4) {
  x1 = 5;
  x2 = 3;
  // CODE
}
```
:::

:::quiz
Let $e$ be the code of a program that never halts on any input. Is $S^1_1(e, 7)$ defined?

- [x] Yes: computing $S^1_1(e, 7)$ only edits the text of the program; it never runs it.

  The result is the code of a program that also never halts — but the *code* exists. This distinction between producing a code and running it is the key to the fixed point theorem.
- [ ] No: $S^1_1(e, 7)$ diverges since $\Phi_e$ diverges.

  This confuses the program with its behavior. $S^m_n$ is total.
- [ ] It depends on whether $\Phi_e(7)$ halts.

  $S^1_1$ never looks at the behavior of $\Phi_e$.

---

Fix a code $e$ of a two-input program. What is the function $y \mapsto \Phi_{S^1_1(e, x)}(y)$?

- [x] $y \mapsto \Phi_e(x, y)$.
- [ ] $y \mapsto \Phi_e(y, x)$.

  The hard-coded value takes the place of the **first** input.
- [ ] $y \mapsto \Phi_x(e, y)$.

  The roles of program and data are swapped here.
:::

From now on the SMN theorem is used without being named, through sentences such as *"for every $x$, let $e_x$ be the code of the program which on input $y$ does … (something depending on $x$ and $y$)"*, it being understood that $e_x$ is obtained computably from $x$. We also say that the process is **uniform** in $x$.

## The padding lemma

Adding useless instructions to a program does not change what it computes. So every program has infinitely many equivalent codes, which can be computed from it.

:::lemma[Padding lemma]{#lem-padding}
There is a total computable function $h : \nat^2 \to \nat$ such that for all $e, n$, we have $h(e, n) \geq n$ and $\Phi_{h(e, n)} = \Phi_e$.
:::

:::proof{of=lem-padding}
Decode $e$ to get $P_e$, append enough instructions that do nothing (say, `skip;`) for the code of the resulting program to be at least $n$, and return that code.
:::

:::quiz
What is the point of the condition $h(e, n) \geq n$?

- [x] It guarantees that the codes $h(e, 0), h(e, 1), \dots$ are unbounded, so every partial computable function has **infinitely many** codes.
- [ ] It ensures that $h$ is total.

  Totality comes from the fact that editing a program always terminates.
- [ ] It ensures that $\Phi_{h(e, n)}$ runs for at least $n$ steps.

  The lemma says nothing about running time — and `skip` instructions placed after the code may never be executed.
:::

:::remark[Acceptable codings]
The universal program theorem and the SMN theorem do not hold for every coding of programs. Rogers proved that any coding satisfying both is obtained from the canonical one by a computable permutation. Friedberg, on the other hand, constructed a computable enumeration of all partial computable functions *without repetition* — so padding fails for it, and so does SMN.
:::
