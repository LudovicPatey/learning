---
title: The Ackermann function
summary: A total computable function which is not primitive recursive. Monotonicity properties, the majorization theorem, and a diagonal argument.
duration: 40
prerequisites: [coding-sequences]
---

The primitive recursive functions are total and computable. Are they all the total computable functions? In 1928 Ackermann, a student of Hilbert, gave a negative answer by exhibiting a function defined by a nested recursion on two variables, which grows faster than every primitive recursive function. We use the simplified version due to Rózsa Péter (1935).

## Definition and computability

:::definition{#def-ackermann}
The **Ackermann–Péter function** $A : \nat^2 \to \nat$ is defined by
$$
\begin{aligned}
A(0, y) &= y + 1, \\
A(x + 1, 0) &= A(x, 1), \\
A(x + 1, y + 1) &= A(x, A(x + 1, y)).
\end{aligned}
$$
:::

These equations define a unique total function. Indeed, order $\nat^2$ lexicographically: $(x', y') <_{\mathrm{lex}} (x, y)$ if $x' < x$, or $x' = x$ and $y' < y$. This is a well-order. In each equation, the right-hand side only involves values of $A$ at pairs lexicographically smaller than the left-hand side: $(x, 1) <_{\mathrm{lex}} (x+1, 0)$, $(x+1, y) <_{\mathrm{lex}} (x+1, y+1)$, and $(x, z) <_{\mathrm{lex}} (x+1, y+1)$ whatever $z = A(x+1, y)$ is. By well-founded induction along $<_{\mathrm{lex}}$, $A(x, y)$ is defined for all $(x, y)$.

The first rows are easy to compute (see the exercises):
$$
A(1, y) = y + 2, \qquad A(2, y) = 2y + 3, \qquad A(3, y) = 2^{y+3} - 3,
$$
and $A(4, y) + 3$ is a tower of $y + 3$ twos: $A(4, 2) = 2^{65536} - 3$.

**$A$ is computable.** The equations can be used as rewriting rules. Represent the current state of the computation by a stack of integers $[z_1, \dots, z_r]$, standing for the expression $A(z_1, A(z_2, \dots A(z_{r-1}, z_r) \dots))$. Start with $[x, y]$ and, while the stack has at least two elements, rewrite its last two elements $z_{r-1}, z_r$:

- if $z_{r-1} = 0$, replace them by $z_r + 1$;
- if $z_{r-1} > 0$ and $z_r = 0$, replace them by $z_{r-1} - 1, 1$;
- if $z_{r-1} > 0$ and $z_r > 0$, replace them by $z_{r-1} - 1, z_{r-1}, z_r - 1$.

Each step preserves the value of the represented expression. Termination follows from the well-foundedness argument above: the steps of the algorithm are the nodes of the evaluation tree of $A(x, y)$, which is finite since it is finitely branching and has no infinite branch. When one element remains, it is $A(x, y)$. Using the coding of the previous lesson, the stack is a single integer and each step is a primitive recursive operation on it; only the number of steps is not bounded in advance.

## Monotonicity

:::lemma{#lem-ack-monotone}
For all $x, y$:

1. $A(x, y) > y$;
2. $A(x, y + 1) > A(x, y)$;
3. $A(x + 1, y) \geq A(x, y + 1)$;
4. $A(x + 1, y) > A(x, y)$.

Consequently $A$ is strictly increasing in each argument.
:::

:::proof{of=lem-ack-monotone}
1. By induction on $x$, and for each $x$ by induction on $y$. For $x = 0$, $A(0, y) = y + 1 > y$. Suppose the claim holds for $x$. Then $A(x + 1, 0) = A(x, 1) > 1 > 0$, and if $A(x + 1, y) > y$, then $A(x + 1, y + 1) = A(x, A(x + 1, y)) > A(x + 1, y) > y$, so $A(x+1, y+1) \geq y + 2$.
2. For $x = 0$ this is clear. For $x + 1$: $A(x + 1, y + 1) = A(x, A(x + 1, y)) > A(x + 1, y)$ by 1.
3. By induction on $y$. For $y = 0$ both sides are equal to $A(x, 1)$. Suppose $A(x + 1, y) \geq A(x, y + 1)$. By 1, $A(x, y + 1) \geq y + 2$, hence $A(x + 1, y) \geq y + 2$, and by 2 (applied repeatedly), $A(x + 1, y + 1) = A(x, A(x + 1, y)) \geq A(x, y + 2)$.
4. By 3 and 2: $A(x + 1, y) \geq A(x, y + 1) > A(x, y)$.
:::

:::lemma{#lem-ack-nesting}
For all $x_1, x_2, y$: $A(x_1, A(x_2, y)) < A(x_1 + x_2 + 2, y)$.
:::

:::proof{of=lem-ack-nesting}
Let $x = \max(x_1, x_2)$. By monotonicity,
$$
\begin{aligned}
A(x_1, A(x_2, y)) &\leq A(x, A(x, y)) \\
&< A(x, A(x + 1, y)) \\
&= A(x + 1, y + 1) \\
&\leq A(x + 2, y) \\
&\leq A(x_1 + x_2 + 2, y),
\end{aligned}
$$
using successively monotonicity in both arguments, item 4 inside item 2 of :ref{#lem-ack-monotone}, the definition of $A$, item 3, and $x + 2 \leq x_1 + x_2 + 2$.
:::

:::quiz[the nesting lemma]
Which step of the chain of inequalities in :ref{#lem-ack-nesting} uses the defining equation $A(x+1, y+1) = A(x, A(x+1, y))$?

- [x] $A(x, A(x+1, y)) = A(x+1, y+1)$.
- [ ] $A(x+1, y+1) \leq A(x+2, y)$.

  This is item 3 of :ref{#lem-ack-monotone}, applied with $x + 1$ in place of $x$.
- [ ] $A(x_1, A(x_2, y)) \leq A(x, A(x, y))$.

  This is monotonicity in both arguments.
:::

## Majorization

For $\vec x = (x_1, \dots, x_k)$ we write $|\vec x| = \max(x_1, \dots, x_k)$.

:::theorem[Majorization]{#thm-ack-majorization}
For every primitive recursive function $f : \nat^k \to \nat$ there is $n \in \nat$ such that $f(\vec x) < A(n, |\vec x|)$ for all $\vec x$.
:::

:::proof{of=thm-ack-majorization}
By induction on a derivation of $f$. Say that $f$ is **bounded by $n$** if $f(\vec x) < A(n, |\vec x|)$ for all $\vec x$. Since $A$ is increasing in its first argument, a function bounded by $n$ is bounded by every $n' \geq n$.

*Basic functions.* $Z(x) = 0 < A(0, x)$; $S(x) = x + 1 < x + 2 = A(1, x)$; and $p^k_i(\vec x) = x_i \leq |\vec x| < A(0, |\vec x|)$.

*Composition.* Let $f(\vec x) = h(g_1(\vec x), \dots, g_m(\vec x))$, where $h, g_1, \dots, g_m$ are all bounded by $n$. Then $\max_i g_i(\vec x) < A(n, |\vec x|)$, hence by monotonicity and :ref{#lem-ack-nesting},
$$
f(\vec x) < A\big(n, \max_i g_i(\vec x)\big) < A\big(n, A(n, |\vec x|)\big) < A(2n + 2, |\vec x|).
$$

*Primitive recursion.* Let $f(\vec x, 0) = g(\vec x)$ and $f(\vec x, y + 1) = h(\vec x, y, f(\vec x, y))$, with $g$ and $h$ bounded by $n$. We first show by induction on $y$ that
$$
f(\vec x, y) < A(n + 1, |\vec x| + y). \qquad (\ast)
$$
For $y = 0$: $f(\vec x, 0) = g(\vec x) < A(n, |\vec x|) < A(n + 1, |\vec x|)$. Suppose $(\ast)$ holds for $y$, and let $w = A(n + 1, |\vec x| + y)$. By :ref{#lem-ack-monotone} (1), $|\vec x| + y < w$, and by induction hypothesis $f(\vec x, y) < w$; so $|(\vec x, y, f(\vec x, y))| < w$. Hence
$$
f(\vec x, y + 1) < A\big(n, |(\vec x, y, f(\vec x, y))|\big) < A(n, w) = A(n + 1, |\vec x| + y + 1).
$$
Now let $K = |(\vec x, y)|$. Then $|\vec x| + y \leq 2K < 2K + 3 = A(2, K)$, and by $(\ast)$ and :ref{#lem-ack-nesting},
$$
f(\vec x, y) < A(n + 1, A(2, K)) < A(n + 5, K).
$$
So $f$ is bounded by $n + 5$.
:::

:::quiz[the majorization theorem]
In the primitive recursion case, why is the auxiliary bound $(\ast)$ stated with $|\vec x| + y$ rather than directly with $|(\vec x, y)|$?

- [x] The induction step increases the second argument of $A(n + 1, \cdot)$ by exactly one, matching the step from $y$ to $y + 1$; this works with $|\vec x| + y$, but $|(\vec x, y)|$ does not always increase when $y$ does.
- [ ] Because $|(\vec x, y)|$ is not primitive recursive.

  The maximum is primitive recursive, but that is irrelevant here.
- [ ] It is a matter of taste: $(\ast)$ could equally be proved with $|(\vec x, y)|$.

  For instance, if $y < |\vec x|$, then $|(\vec x, y)| = |(\vec x, y + 1)|$, and the inductive step would need $f(\vec x, y + 1) < A(n+1, |\vec x|)$ from $f(\vec x, y) < A(n+1, |\vec x|)$, which does not follow.

---

In the composition case, where is :ref{#lem-ack-nesting} used?

- [x] To bound the double application $A(n, A(n, |\vec x|))$ by a single value $A(2n + 2, |\vec x|)$.
- [ ] To bound each $g_i(\vec x)$.

  This is the induction hypothesis.
- [ ] To show that $h$ is bounded.

  This is also the induction hypothesis.
:::

:::corollary{#cor-ack-not-pr}
The function $a(n) = A(n, n)$ is total and computable, but not primitive recursive. Hence $A$ is not primitive recursive either.
:::

:::proof{of=cor-ack-not-pr}
If $a$ were primitive recursive, by :ref{#thm-ack-majorization} there would be $m$ such that $a(n) < A(m, n)$ for all $n$. For $n = m$, this gives $A(m, m) < A(m, m)$, a contradiction. If $A$ were primitive recursive, so would be $a = A \circ (p^1_1, p^1_1)$.
:::

The argument is a diagonalization: $a$ escapes each function $A(m, \cdot)$ at the point $m$. The majorization theorem says more: every primitive recursive function is eventually dominated by $a$, since $f(x) < A(m, x) \leq A(x, x)$ for $x \geq m$.

## A diagonal argument

The same conclusion can be obtained without any growth estimate, by a direct diagonalization over derivations. Derivations of unary primitive recursive functions are finite objects; fix a computable coding of them by integers, and let $f_0, f_1, f_2, \dots$ be the list of the functions they define (the integers that do not code derivations being assigned the zero function, say).

:::theorem{#thm-pr-diagonal}
The function $d(n) = f_n(n) + 1$ is total and computable, but not primitive recursive.
:::

:::proof{of=thm-pr-diagonal}
To compute $d(n)$, decode the derivation coded by $n$ and evaluate it on $n$ following :ref{#prop-pr-total-computable}; this always terminates. If $d$ were primitive recursive, it would be $f_e$ for some $e$, and then $d(e) = f_e(e) + 1 = d(e) + 1$.
:::

:::quiz[the diagonal argument]
The function $(n, x) \mapsto f_n(x)$ is total and computable. What does the theorem imply about it?

- [x] It is not primitive recursive: otherwise $d(n) = f_n(n) + 1$ would be primitive recursive by composition.

  The evaluation function of a class of total functions cannot belong to the class, if the class is closed under composition with the successor.
- [ ] It is primitive recursive, since each $f_n$ is.

  Each function $x \mapsto f_n(x)$ is, but not the function of two variables.
- [ ] It is not computable.

  It is computable: decode and evaluate.

---

Why does the same argument not show that some total computable function is not computable?

- [x] There is no computable enumeration of exactly the total computable functions. An enumeration of all programs contains programs that do not halt, and for those, $d(n) = \Phi_n(n) + 1$ is undefined.

  This obstacle is made precise in the course on fundamentals, with the halting problem.
- [ ] Because the total computable functions are uncountable.

  There are countably many programs, so countably many computable functions.
- [ ] Because $d$ grows too fast.
:::

Thus unbounded loops are necessary to compute all total computable functions — and with unbounded loops comes the possibility of non-termination. The next lesson adds unbounded search to the primitive recursive functions.

## Exercises

::::exercise{difficulty=1}
Prove that $A(1, y) = y + 2$, $A(2, y) = 2y + 3$ and $A(3, y) = 2^{y + 3} - 3$.

:::solution
By induction on $y$ in each case. $A(1, 0) = A(0, 1) = 2$ and $A(1, y + 1) = A(0, A(1, y)) = A(1, y) + 1$. Then $A(2, 0) = A(1, 1) = 3$ and $A(2, y + 1) = A(1, A(2, y)) = A(2, y) + 2$. Finally $A(3, 0) = A(2, 1) = 5 = 2^3 - 3$ and $A(3, y + 1) = A(2, A(3, y)) = 2 A(3, y) + 3 = 2(2^{y+3} - 3) + 3 = 2^{y+4} - 3$.
:::
::::

::::exercise{difficulty=2}
For each $n$, show that the function $y \mapsto A(n, y)$ is primitive recursive. Why does this not contradict :ref{#cor-ack-not-pr}?

:::solution
By induction on $n$. $A(0, \cdot)$ is the successor. If $g = A(n, \cdot)$ is primitive recursive, then $A(n + 1, \cdot)$ satisfies $A(n + 1, 0) = g(1)$ and $A(n + 1, y + 1) = g(A(n + 1, y))$, a primitive recursion. Each row is primitive recursive, but each requires a derivation of its own, and the length of these derivations grows with $n$. A single derivation cannot handle all rows, which is what :ref{#cor-ack-not-pr} says: the diagonal $n \mapsto A(n, n)$ uses rows of every level.
:::
::::

::::exercise{difficulty=2}
Show that the graph $G = \{(x, y, z) : A(x, y) = z\}$ of the Ackermann function is a primitive recursive predicate.

:::hint
A computation of $A(x, y)$ can be recorded as a finite set of triples $(x', y', A(x', y'))$, all of whose values are bounded by $z$.
:::

:::solution
Call a finite set $T$ of triples **closed** if for each $(x', y', z') \in T$, the equations defining $A(x', y')$ are witnessed in $T$: if $x' = 0$ then $z' = y' + 1$; if $x' > 0$, $y' = 0$ then $(x' - 1, 1, z') \in T$; if $x', y' > 0$ then there is $w$ with $(x', y' - 1, w) \in T$ and $(x' - 1, w, z') \in T$. By induction along $<_{\mathrm{lex}}$, every triple in a closed set is in $G$; conversely, the set of triples occurring in the evaluation of $A(x, y)$ is closed and contains $(x, y, A(x, y))$. All triples occurring in that evaluation have components at most $z = A(x, y)$, by monotonicity. Coding $T$ as a sequence of triples, the code is bounded by a primitive recursive function of $z$, and $G(x, y, z)$ holds iff there is a closed $T$ with code below this bound containing $(x, y, z)$: a bounded search over a primitive recursive predicate.
:::
::::

## Notes and references

Ackermann's original function had three arguments; the two-argument version used here is due to Péter. The majorization argument follows the standard textbook proof. The stratification of the primitive recursive functions by growth rate leads to the Grzegorczyk hierarchy.

- W. Ackermann, *Zum Hilbertschen Aufbau der reellen Zahlen*, Mathematische Annalen 99 (1928), 118–133.
- R. Péter, *Konstruktion nichtrekursiver Funktionen*, Mathematische Annalen 111 (1935), 42–60.
- A. Grzegorczyk, *Some classes of recursive functions*, Rozprawy Matematyczne 4 (1953).
