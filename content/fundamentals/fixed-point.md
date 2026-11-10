---
title: Kleene's fixed point theorem
summary: Every total computable transformation of codes has an extensional fixed point. Self-referential programs.
duration: 20
prerequisites: [universal-program-smn]
---

Kleene's fixed point theorem, also called the **recursion theorem**, states that every total computable transformation of codes has a fixed point up to extensional equality. Its main use is to construct programs that have access to their own code, a technique used throughout computability theory.

:::theorem[Fixed point theorem]{#thm-fixed-point}
For every total computable function $f : \nat \to \nat$, there is an $e \in \nat$ such that for every $n$,
$$
\Phi_{f(e)}(n) = \Phi_e(n).
$$
:::

In words: for any computable way $f$ of transforming programs, some program $e$ behaves exactly like its transform $f(e)$.

## Why this gives self-reference

Suppose a program $M$ uses a variable `x` initialized to some value. Let $f(n)$ be the code of $M$ with `x` initialized to $n$; $f$ is total computable. A fixed point $e$ behaves like $f(e)$, i.e. like $M$ running with `x` set to $e$, its own code. Formally:

:::corollary{#cor-self-reference}
For every partial computable $g : \nat^2 \to \nat$ there is an $e$ such that for every $n$,
$$
\Phi_e(n) = g(e, n).
$$
:::

:::proof{of=cor-self-reference}
Let $i$ be a code with $\Phi_i(x, n) = g(x, n)$. By the :ref{#thm-smn}, $\Phi_{S^1_1(i, x)}(n) = \Phi_i(x, n)$ for all $x, n$. Let $f(x) = S^1_1(i, x)$, a total computable function. By :ref{#thm-fixed-point} there is an $e$ with $\Phi_{f(e)} = \Phi_e$, so
$$
\Phi_e(n) = \Phi_{f(e)}(n) = \Phi_i(e, n) = g(e, n). \qquad
$$
:::

Before the formal proof, here is how a programmer would write a program that knows its own text. Both ellipses must contain the same code; `replace` substitutes the first occurrence of `#` with the content of `v`.

```js
function fct() {
  let v = `
function fct() {
  let v = '#'
  v = v.replace('#', v)
  ... // my code
}`
  v = v.replace('#', v)
  ... // my code
}
```

When it runs, `v` contains the program itself (up to the kind of quotes). The formal proof follows the same pattern: a program that receives a code, and applies it to itself.

:::proof{of=thm-fixed-point}
Let $a$ be the code of a one-input program which, on input $n$, returns the code of the following one-input program, on input $m$:

1. compute $\Phi_n(n)$, then $f(\Phi_n(n))$;
2. if this halts, run the program of code $f(\Phi_n(n))$ on input $m$ and return its result.

Formally, for all $n, m$:
$$
\Phi_{\Phi_a(n)}(m) = \Phi_{f(\Phi_n(n))}(m),
$$
where, if $\Phi_n(n)\diverge$, the right-hand side denotes the nowhere defined function.

Note that $\Phi_a$ is **total**: computing $\Phi_a(n)$ does not perform steps 1 and 2, it only *writes down the code* of a program that performs them. Such an $a$ exists by the SMN theorem: the function $(n, m) \mapsto \Phi_{f(\Phi_n(n))}(m)$ is partial computable, say with code $b$, and $\Phi_a(n) = S^1_1(b, n)$.

The fixed point is $e = \Phi_a(a)$. Indeed, taking $n = a$:
$$
\forall m\quad \Phi_{\Phi_a(a)}(m) = \Phi_{f(\Phi_a(a))}(m). \qquad
$$
:::

:::quiz
Why is $\Phi_a$ a **total** function, even though $\Phi_n(n)$ may diverge?

- [x] Computing $\Phi_a(n)$ only produces a code, via the SMN theorem; it never runs $\Phi_n(n)$.

  Divergence of $\Phi_n(n)$ is pushed inside the program whose code is returned.
- [ ] Because $f$ is total.

  Totality of $f$ plays no role here: $\Phi_a(n) = S^1_1(b, n)$ is total for any $b$.
- [ ] Because $\Phi_n(n)$ converges for every $n$.

  It doesn't — that would make the halting problem trivial.
- [ ] Because $a$ is chosen to be a fixed point.

  $a$ is fixed before any fixed point is mentioned; the fixed point is $\Phi_a(a)$.

---

The final line is obtained from $\Phi_{\Phi_a(n)}(m) = \Phi_{f(\Phi_n(n))}(m)$ by…

- [x] instantiating $n := a$, which is legitimate as an equality between programs because $\Phi_a(a)\converge$.

  This is the diagonal step: the program $a$ is fed its own code.
- [ ] instantiating $m := a$.

  $m$ remains a free input: we need the equality for **all** $m$.
- [ ] applying $f$ to both sides.

  $f$ acts on codes, and it already appears on the right-hand side.

---

Where does the proof use that $f$ is **total**?

- [x] To make sure $f(\Phi_a(a))$ is defined, so that $f(e)$ is an actual program to compare with $e$.

  For partial $f$, the same construction only gives: *if* $f(e)\converge$ then $\Phi_{f(e)} = \Phi_e$.
- [ ] To show that $\Phi_a$ is total.

  See the first question: $\Phi_a$ is total regardless of $f$.
- [ ] To apply the SMN theorem.

  SMN applies to any partial computable function.
:::

:::remark[Fixed points and paradoxes]
The barber who shaves exactly those who do not shave themselves, or Russell's set $S$ of all sets that do not belong to themselves, are paradoxes built on self-reference. Why doesn't the fixed point theorem produce a paradox?

Try the same pattern: by :ref{#cor-self-reference}, build $e$ such that $\Phi_e(n) = \Phi_e(n) + 1$. This is not a contradiction, because **partial functions** escape it: the equation is satisfied when $\Phi_e(n)$ is undefined.
:::

:::quiz
By :ref{#cor-self-reference} applied to $g(x, n) = \Phi_x(n) + 1$ (computable by the universal program), there is an $e$ with $\Phi_e(n) = \Phi_e(n) + 1$ for all $n$. What follows?

- [x] $\Phi_e(n)\diverge$ for every $n$.

  If $\Phi_e(n)\converge = y$ we would get $y = y + 1$. Both sides being undefined is the only option, by the convention on equality of partial functions.
- [ ] The corollary is contradictory, so the theorem is false.

  Equality of partial functions holds when both sides are undefined.
- [ ] $\Phi_e(n) = 0$ for every $n$.

  Then the right-hand side would be $1$.
:::

In the next lesson, the fixed point theorem gives a short proof of **Rice's theorem**: no non-trivial property of the behavior of programs is decidable.
