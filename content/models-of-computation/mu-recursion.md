---
title: Minimization and partial recursive functions
summary: The minimization operator, the partial recursive functions, recursive functions and predicates, and the statement of Kleene's normal form theorem.
duration: 35
prerequisites: [ackermann-function]
---

Primitive recursion corresponds to `for` loops: the number of iterations is fixed before the loop starts. The Ackermann function shows that this is not enough to obtain all total computable functions. What is missing is the `while` loop, or equivalently the **unbounded search**: try $y = 0, 1, 2, \dots$ until some condition holds. Adding this operation leads to the class of partial recursive functions, introduced by Kleene in 1936.

## The minimization operator

:::definition{#def-mu}
Let $g : \nat^{k+1} \rightharpoonup \nat$ be a partial function. The partial function $f : \nat^k \rightharpoonup \nat$ obtained from $g$ by **minimization**, written
$$
f(\vec x) \simeq \mu y\, [g(\vec x, y) = 0],
$$
is defined as follows: $f(\vec x)\converge = y$ if and only if

- $g(\vec x, y)\converge = 0$, and
- for every $z < y$, $g(\vec x, z)\converge$ and $g(\vec x, z) \neq 0$.

If there is no such $y$, then $f(\vec x)\diverge$.
:::

The definition describes exactly the result of the following procedure: compute $g(\vec x, 0)$, then $g(\vec x, 1)$, and so on, and return the first $y$ for which the value is $0$. The procedure fails to return in two different ways: either all values are defined and non-zero, or some computation $g(\vec x, z)$ does not terminate before a zero has been found.

For a predicate $P \subseteq \nat^{k+1}$ we write $\mu y\, P(\vec x, y)$ for $\mu y\, [\overline{\mathrm{sg}}(\chi_P(\vec x, y)) = 0]$, the least $y$ such that $P(\vec x, y)$.

:::quiz[the minimization operator]
Why does the definition require $g(\vec x, z)\converge$ for all $z < y$, rather than simply taking the least $y$ such that $g(\vec x, y) = 0$?

- [x] Because the search evaluates $g(\vec x, 0), g(\vec x, 1), \dots$ in order: if some $g(\vec x, z)$ with $z$ smaller than the least zero diverges, the search never gets past $z$.

  With the other definition, minimization would not preserve computability. Let $g(x, 0) \simeq 0$ if the program of code $x$ halts on input $x$, undefined otherwise, and $g(x, y) = 0$ for $y \geq 1$. Then $g$ is partial computable, and "the least zero of $g(x, \cdot)$" is $0$ or $1$ according to whether the program $x$ halts on $x$: it would decide the halting problem, which is impossible (see the lesson :ref{to="fundamentals/halting-problem"}).
- [ ] To ensure that $f$ is total.

  $f$ may be undefined, for instance when $g(\vec x, \cdot)$ has no zero.
- [ ] It is needed already when $g$ is total, to make $f(\vec x)$ the least zero of $g(\vec x, \cdot)$.

  When $g$ is total, the condition $g(\vec x, z)\converge$ holds automatically and the two definitions agree; the requirement only matters for partial $g$.
:::

## Partial recursive functions

The schemes of composition and primitive recursion extend to partial functions, with the convention that an expression is undefined as soon as one of its subexpressions is:

- **composition:** $f(\vec x) \simeq h(g_1(\vec x), \dots, g_m(\vec x))$;
- **primitive recursion:** $f(\vec x, 0) \simeq g(\vec x)$ and $f(\vec x, y + 1) \simeq h(\vec x, y, f(\vec x, y))$. In particular, if $f(\vec x, y)\diverge$ then $f(\vec x, y')\diverge$ for all $y' \geq y$.

:::definition{#def-partial-recursive}
The class of **partial recursive** functions is the smallest class of partial functions $\nat^k \rightharpoonup \nat$ ($k \geq 1$) containing the basic functions $Z$, $S$, $p^k_i$, and closed under composition, primitive recursion and minimization. A partial recursive function which is total is called a **(total) recursive** function. A predicate is **recursive** if its characteristic function is recursive.
:::

The terminology varies: *partial recursive* is also called *partial computable*, and *recursive* is also called *computable*, the modern usage preferred in the following courses. In Kleene's original work, the total functions obtained from Herbrand–Gödel systems of equations were called *general recursive*; Kleene proved that they are exactly the total partial recursive functions.

:::proposition{#prop-partial-recursive-computable}
Every partial recursive function is computable: there is an algorithm which, on input $\vec x$, terminates with output $f(\vec x)$ if $f(\vec x)\converge$, and does not terminate otherwise.
:::

:::proof{of=prop-partial-recursive-computable}
By induction on the definition of $f$, as for :ref{#prop-pr-total-computable}, with one additional case: for minimization, the algorithm runs the computations of $g(\vec x, 0), g(\vec x, 1), \dots$ one after the other, as described above. In the composition and recursion cases, the algorithm computes the subexpressions in order and does not terminate if one of them does not. A precise version of this proof, for WHILE programs, is given in the lesson :ref{to="models-of-computation/while-programs"}.
:::

Every primitive recursive function is recursive. The converse fails:

:::proposition{#prop-ackermann-recursive}
The Ackermann function is recursive.
:::

:::proof{of=prop-ackermann-recursive}
By the last exercise of the lesson :ref{to="models-of-computation/ackermann-function"}, the graph $G = \{(x, y, z) : A(x, y) = z\}$ is primitive recursive. Hence $A(x, y) = \mu z\, G(x, y, z)$, and the search terminates since $(x, y, A(x, y)) \in G$.
:::

This is an instance of a general principle: a total function whose graph is recursive is recursive, by searching for the value.

:::quiz[recursive functions]
Let $f$ be a total function whose graph $\{(\vec x, z) : f(\vec x) = z\}$ is recursive. Which statements are correct?

- [x] $f$ is recursive, as $f(\vec x) = \mu z\, [(\vec x, z) \in \mathrm{graph}(f)]$, and the search terminates because $f$ is total.
- [ ] $f$ is primitive recursive.

  The Ackermann function is a counterexample: its graph is primitive recursive, but it is not.
- [x] If $f$ is partial and has a recursive graph, the same search shows that $f$ is partial recursive.

  When $f(\vec x)\diverge$, no $z$ satisfies $(\vec x, z) \in \mathrm{graph}(f)$ and the search diverges, as it should.
:::

## Examples

1. $\mu y\, [x \dotminus y = 0] = x$, since $x \dotminus y = 0$ iff $y \geq x$.
2. With $|a - b| = (a \dotminus b) + (b \dotminus a)$, the function $r(x) \simeq \mu y\, [\,|y \cdot y - x| = 0\,]$ is the square root of $x$ if $x$ is a perfect square, and is undefined otherwise.
3. $\mu y\, [x + y + 1 = 0]$ is the nowhere defined function of $x$. In particular the empty function is partial recursive.
4. If $f : \nat \to \nat$ is a recursive bijection, its inverse $f^{-1}(y) = \mu x\, [f(x) = y]$ is recursive.

:::quiz[examples of minimization]
Which statements are correct?

- [x] $\mu y\, [\,|y \cdot y - 9| = 0\,] = 3$.
- [ ] $\mu y\, [\,|y \cdot y - 8| = 0\,] = 2$.

  $8$ is not a perfect square: the search never ends. The integer square root $\lfloor \sqrt 8 \rfloor = 2$ is a different, total, function.
- [x] $\mu y\, [x \dotminus y = 0] = x$.

  $x \dotminus y = 0$ if and only if $y \geq x$.
- [ ] $\mu y\, [x + y + 1 = 0] = 0$.

  $x + y + 1$ is never $0$: the value is undefined.
:::

## Regular minimization

Kleene originally defined the total recursive functions using minimization only in the **regular** case.

:::definition{#def-regular-mu}
A total function $g : \nat^{k+1} \to \nat$ is **regular** if for every $\vec x$ there is $y$ with $g(\vec x, y) = 0$.
:::

Minimization applied to a regular total function yields a total function. Let $\mathcal{R}$ be the smallest class of **total** functions containing the basic functions and closed under composition, primitive recursion and regular minimization. Every function of $\mathcal{R}$ is recursive, since regular minimization is a special case of minimization. The converse — every total partial recursive function belongs to $\mathcal{R}$ — is not obvious: a partial recursive definition of a total function may use partial functions in intermediate steps. It is a consequence of the normal form theorem below.

## Kleene's normal form

The following theorem, proved in the lesson :ref{to="models-of-computation/equivalence-of-models"}, shows that a single unbounded search suffices to compute any partial recursive function.

:::theorem[Kleene's normal form, statement]{#thm-kleene-normal-form}
There are a primitive recursive predicate $T_k \subseteq \nat^{k+2}$ for each $k \geq 1$, and a primitive recursive function $U : \nat \to \nat$, such that for every partial recursive $f : \nat^k \rightharpoonup \nat$ there is $e \in \nat$ with
$$
f(\vec x) \simeq U\big(\mu s\, T_k(e, \vec x, s)\big) \quad \text{for all } \vec x.
$$
:::

Informally: $e$ codes a program for $f$; $T_k(e, \vec x, s)$ states that $s$ codes a complete halting computation of the program $e$ on input $\vec x$; and $U(s)$ extracts the output from the computation $s$. Checking that a given number codes a correct halting computation only requires bounded loops, hence $T_k$ is primitive recursive. Only **finding** the computation requires an unbounded search.

:::corollary{#cor-regular-mu}
Every total recursive function belongs to the class $\mathcal{R}$ defined with regular minimization.
:::

:::proof{of=cor-regular-mu}
If $f$ is total, then for every $\vec x$ there is $s$ with $T_k(e, \vec x, s)$, so the function $(\vec x, s) \mapsto \overline{\mathrm{sg}}(\chi_{T_k}(e, \vec x, s))$ is regular. Hence $f = U \circ \mu s\, [\overline{\mathrm{sg}}(\chi_{T_k}(e, \vec x, s)) = 0]$ is obtained from primitive recursive functions by one regular minimization and one composition.
:::

:::quiz[the normal form theorem]
In $f(\vec x) \simeq U(\mu s\, T_k(e, \vec x, s))$, which part makes $f$ partial?

- [x] The search $\mu s$, which does not terminate when the program $e$ does not halt on $\vec x$.
- [ ] The function $U$.

  $U$ is primitive recursive, hence total.
- [ ] The predicate $T_k$.

  $T_k$ is primitive recursive: checking a candidate computation always terminates.

---

According to the theorem, how many applications of the minimization operator suffice to define an arbitrary partial recursive function?

- [x] One.
- [ ] As many as in some given definition of the function.

  The normal form theorem gives a single minimization for every partial recursive function, whatever the number used in a given definition.
- [ ] None, since $T_k$ and $U$ are primitive recursive.

  Without minimization only total functions can be defined.
:::

## Exercises

::::exercise{difficulty=1}
Show that the recursive predicates are closed under the boolean connectives and bounded quantification, and that the recursive functions are closed under bounded minimization over recursive predicates.

:::solution
The total recursive functions contain the primitive recursive functions and are closed under composition and primitive recursion, since these operations preserve totality. The proofs given for primitive recursive predicates and functions in the lesson :ref{to="models-of-computation/primitive-recursion"} only use these closure properties, applied to characteristic functions, which are total. They therefore apply verbatim to recursive predicates and functions.
:::
::::

::::exercise{difficulty=2}
Let $g : \nat \to \nat$ be recursive and strictly increasing. Show that its range is a recursive set, and that the function $h(y) = $ "the least $x$ such that $g(x) \geq y$" is recursive.

:::solution
Since $g$ is strictly increasing, $g(x) \geq x$, so $y \in \operatorname{im} g \iff \exists x \leq y\ g(x) = y$, a bounded quantification over a recursive predicate. The function $h(y) = \mu x\, [g(x) \geq y]$ is a minimization of a recursive predicate, which is regular since $g(y) \geq y$; hence $h$ is recursive (and even $h(y) = \mu x \leq y\, [g(x) \geq y]$).
:::
::::

::::exercise{difficulty=2}
Let $f(x) \simeq \mu y\, [g(x, y) = 0]$ for a partial recursive $g$. Is it true that $\dom f = \{x : \exists y\ g(x, y) = 0\}$? Give a proof or a counterexample.

:::solution
It is false in general: we always have $\dom f \subseteq \{x : \exists y\ g(x, y) = 0\}$, but the converse fails when $g(x, z)$ diverges for some $z$ smaller than every zero. For example, let $g(x, y) \simeq \mu z\, [z + \overline{\mathrm{sg}}(y) = 0]$. For $y \geq 1$, $\overline{\mathrm{sg}}(y) = 0$ and $g(x, y) = 0$; for $y = 0$, the search $\mu z\, [z + 1 = 0]$ diverges. Then $\exists y\ g(x, y) = 0$ holds for all $x$, but $f$ is nowhere defined, since the search for $f(x)$ is stuck at $y = 0$.
:::
::::

## Notes and references

The general recursive functions were defined by Gödel in 1934, following a suggestion of Herbrand, through systems of equations. Kleene gave the characterization by minimization and proved the normal form theorem in 1936.

- S. C. Kleene, *General recursive functions of natural numbers*, Mathematische Annalen 112 (1936), 727–742.
- S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952, chapters XI–XII.
