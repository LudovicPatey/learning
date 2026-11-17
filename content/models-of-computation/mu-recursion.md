---
title: Minimization and partial recursive functions
summary: The minimization operator, the partial recursive functions, recursive functions and predicates, and the statement of Kleene's normal form theorem.
duration: 25
prerequisites: [ackermann-function]
---

Primitive recursion corresponds to `for` loops: the number of iterations is fixed before the loop starts. The Ackermann function shows that this is not enough to obtain all total computable functions. What is missing is the `while` loop, or equivalently the **unbounded search**: try $y = 0, 1, 2, \dots$ until some condition holds. Adding this operation leads to the class of partial recursive functions. Kleene introduced the search operator $\mu$ in 1936, applied to functions for which the search always succeeds; in 1938 he proposed to apply it to arbitrary partial functions, accepting that the search may run forever.

The price of unbounded search is partiality: a function defined with it may be undefined at some arguments, and this cannot be avoided (the lesson :ref{to="fundamentals/halting-problem"} shows that there is no algorithm deciding when the search terminates). The lesson defines the operator with its exact convention on partial arguments, gives examples, and states Kleene's normal form theorem: one search suffices for every partial recursive function.

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

:::figure[Two runs of the search $\mu y\, [g(x, y) = 0]$. In run (a) the search stops at the first zero, $y = 2$. In run (b) the computation of $g(x, 1)$ does not terminate, and the search never reaches the zero at $y = 2$: $f(x)$ is undefined.]
<svg class="fig" viewBox="0 0 520 200" width="520" role="img" aria-label="Two runs of the search for the least zero"><defs><marker id="ah-mu" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="173.0" y="22" text-anchor="middle" class="math" font-size="16">y<tspan class="mrm"> = 0</tspan></text><text x="219.0" y="22" text-anchor="middle" class="math" font-size="16">y<tspan class="mrm"> = 1</tspan></text><text x="265.0" y="22" text-anchor="middle" class="math" font-size="16">y<tspan class="mrm"> = 2</tspan></text><text x="311.0" y="22" text-anchor="middle" class="math" font-size="16">y<tspan class="mrm"> = 3</tspan></text><text x="357.0" y="22" text-anchor="middle" class="math" font-size="16">y<tspan class="mrm"> = 4</tspan></text><text x="12" y="80" class="label">run (a)</text><rect class="cell" x="150" y="52" width="46" height="46" rx="3"/><text x="173.0" y="81" text-anchor="middle" class="mrm" font-size="18">4</text><rect class="cell" x="196" y="52" width="46" height="46" rx="3"/><text x="219.0" y="81" text-anchor="middle" class="mrm" font-size="18">1</text><rect class="cell head-cell" x="242" y="52" width="46" height="46" rx="3"/><text x="265.0" y="81" text-anchor="middle" class="mrm" font-size="18">0</text><rect class="cell" x="288" y="52" width="46" height="46" rx="3"/><text x="311.0" y="81" text-anchor="middle" class="mrm muted" font-size="18">7</text><rect class="cell" x="334" y="52" width="46" height="46" rx="3"/><text x="357.0" y="81" text-anchor="middle" class="mrm muted" font-size="18">0</text><path d="M179.0,48 Q196.0,34 213.0,48" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-mu)"/><path d="M225.0,48 Q242.0,34 259.0,48" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-mu)"/><text x="398" y="81" class="math" font-size="17">f<tspan class="mrm">(</tspan>x<tspan class="mrm">)</tspan> <tspan class="mrm">=</tspan> <tspan class="mrm">2</tspan></text><text x="12" y="160" class="label">run (b)</text><rect class="cell" x="150" y="132" width="46" height="46" rx="3"/><text x="173.0" y="161" text-anchor="middle" class="mrm" font-size="18">3</text><rect class="cell head-cell" x="196" y="132" width="46" height="46" rx="3"/><text x="219.0" y="161" text-anchor="middle" class="mrm" font-size="18">↑</text><rect class="cell" x="242" y="132" width="46" height="46" rx="3"/><text x="265.0" y="161" text-anchor="middle" class="mrm muted" font-size="18">0</text><rect class="cell" x="288" y="132" width="46" height="46" rx="3"/><text x="311.0" y="161" text-anchor="middle" class="mrm muted" font-size="18">0</text><rect class="cell" x="334" y="132" width="46" height="46" rx="3"/><text x="357.0" y="161" text-anchor="middle" class="mrm muted" font-size="18">5</text><path d="M179.0,128 Q196.0,114 213.0,128" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-mu)"/><text x="398" y="161" class="math" font-size="17">f<tspan class="mrm">(</tspan>x<tspan class="mrm">)</tspan><tspan class="mrm">↑</tspan></text><text x="150" y="194" class="label">values after the stopping point are never computed</text></svg>
:::

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
By :ref{#ex-ack-graph}, the graph $G = \{(x, y, z) : A(x, y) = z\}$ is primitive recursive. Hence $A(x, y) = \mu z\, G(x, y, z)$, and the search terminates since $(x, y, A(x, y)) \in G$.
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

Minimization applied to a regular total function yields a total function. Let $\mathcal{R}$ be the smallest class of **total** functions containing the basic functions and closed under composition, primitive recursion and regular minimization. Every function of $\mathcal{R}$ is recursive, since regular minimization is a special case of minimization. The class $\mathcal{R}$ has a defect as a definition: whether a given total function is regular is in general not decidable, so the derivations of functions of $\mathcal{R}$ cannot be recognized effectively. Partial functions, proposed by Kleene (1938), remove this difficulty: every derivation of a partial recursive function defines a function. The converse — every total partial recursive function belongs to $\mathcal{R}$ — is not obvious: a partial recursive definition of a total function may use partial functions in intermediate steps. It is a consequence of the normal form theorem below.

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

::::exercise{#ex-mu-domain difficulty=2 objective="See why the domain of a minimization is not the set of arguments where a zero exists."}
Let $f(x) \simeq \mu y\, [g(x, y) = 0]$ for a partial recursive $g$. Is it true that $\dom f = \{x : \exists y\ g(x, y) = 0\}$? Give a proof or a counterexample.

:::solution
It is false in general: we always have $\dom f \subseteq \{x : \exists y\ g(x, y) = 0\}$, but the converse fails when $g(x, z)$ diverges for some $z$ smaller than every zero. For example, let $g(x, y) \simeq \mu z\, [z + \overline{\mathrm{sg}}(y) = 0]$. For $y \geq 1$, $\overline{\mathrm{sg}}(y) = 0$ and $g(x, y) = 0$; for $y = 0$, the search $\mu z\, [z + 1 = 0]$ diverges. Then $\exists y\ g(x, y) = 0$ holds for all $x$, but $f$ is nowhere defined, since the search for $f(x)$ is stuck at $y = 0$.
:::
::::

## Notes and references

The general recursive functions were defined by Gödel in 1934, following a suggestion of Herbrand, through systems of equations. Kleene gave the characterization by minimization and proved the normal form theorem in 1936; partial recursive functions, with minimization applied to partial functions, appear in Kleene (1938). The historical account in Soare (2016, §§17.2.4–17.2.5) states these dates, and Monin and Patey (chapter "Church–Turing thesis") define the general recursive functions with the same convention on partial arguments as :ref{#def-mu}.

- S. C. Kleene, *General recursive functions of natural numbers*, Mathematische Annalen 112 (1936), 727–742.
- S. C. Kleene, *On notation for ordinal numbers*, Journal of Symbolic Logic 3 (1938), 150–155.
- S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952, chapters XI–XII.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §17.2.
- B. Monin, L. Patey, *Computability theory*, chapter "Church–Turing thesis".

:::::exercises
::::exercise{#ex-mu-recursive-closure difficulty=1 objective="Transfer the closure properties of primitive recursive predicates to recursive predicates."}
Show that the recursive predicates are closed under the boolean connectives and bounded quantification, and that the recursive functions are closed under bounded minimization over recursive predicates.

:::solution
The total recursive functions contain the primitive recursive functions and are closed under composition and primitive recursion, since these operations preserve totality. The proofs given for primitive recursive predicates and functions in the lesson :ref{to="models-of-computation/primitive-recursion"} only use these closure properties, applied to characteristic functions, which are total. They therefore apply verbatim to recursive predicates and functions.
:::
::::

::::exercise{#ex-mu-increasing difficulty=2 objective="Bound a search by monotonicity, and recognize a regular minimization."}
Let $g : \nat \to \nat$ be recursive and strictly increasing. Show that its range is a recursive set, and that the function $h(y) = $ "the least $x$ such that $g(x) \geq y$" is recursive.

:::solution
Since $g$ is strictly increasing, $g(x) \geq x$, so $y \in \operatorname{im} g \iff \exists x \leq y\ g(x) = y$, a bounded quantification over a recursive predicate. The function $h(y) = \mu x\, [g(x) \geq y]$ is a minimization of a recursive predicate, which is regular since $g(y) \geq y$; hence $h$ is recursive (and even $h(y) = \mu x \leq y\, [g(x) \geq y]$).
:::
::::

::::exercise{#ex-mu-compute difficulty=1 objective="Compute minimizations of total and partial functions from the definition."}
Determine the following partial functions.

1. $f_1(x) \simeq \mu y\, [x \dotminus 2y = 0]$.
2. $f_2(x) \simeq \mu y\, [\,|2y - x| = 0\,]$, where $|a - b| = (a \dotminus b) + (b \dotminus a)$.
3. $g(x, y) \simeq \mu z\, [z + (y \dotminus x) = 0]$, then $f_3(x) \simeq \mu y\, [g(x, y) = 0]$ and $f_4(x) \simeq \mu y\, [g(x, y + x + 1) = 0]$.

:::solution
1. $x \dotminus 2y = 0$ if and only if $2y \geq x$, so $f_1(x) = \lceil x / 2 \rceil$, a total function.
2. $|2y - x| = 0$ if and only if $2y = x$. So $f_2(x) = x / 2$ if $x$ is even; if $x$ is odd, all values are defined and non-zero, and $f_2(x)\diverge$.
3. If $y \leq x$, then $y \dotminus x = 0$ and $g(x, y) = 0$, found at $z = 0$. If $y > x$, then $z + (y \dotminus x) \geq 1$ for all $z$, and $g(x, y)\diverge$. Hence $f_3(x) = 0$ for all $x$: the search stops at $y = 0$, since $g(x, 0) = 0$, before reaching the arguments where $g(x, \cdot)$ diverges. On the other hand $g(x, y + x + 1)\diverge$ for every $y$, so the search for $f_4(x)$ is stuck at $y = 0$, and $f_4$ is the empty function.
:::
::::

::::exercise{#ex-mu-inverse-hypotheses difficulty=1 objective="See what the search for an inverse computes when a recursive function is only injective, or only surjective."}
Let $f : \nat \to \nat$ be recursive and $g(y) \simeq \mu x\, [f(x) = y]$.

1. If $f$ is injective, show that $g$ is a partial recursive function with domain $\operatorname{im} f$ and $g(f(x)) = x$ for all $x$.
2. If $f$ is surjective, show that $g$ is recursive and $f(g(y)) = y$ for all $y$, and give an example where $g(f(x)) \neq x$ for some $x$.

:::solution
$g$ is partial recursive, as a minimization of the recursive function $(y, x) \mapsto \overline{\mathrm{sg}}(\chi_=(f(x), y))$, which is total, so $g(y)\converge$ if and only if some $x$ satisfies $f(x) = y$, and then $g(y)$ is the least such $x$, with $f(g(y)) = y$.

1. The domain of $g$ is $\operatorname{im} f$. For $y = f(x)$, injectivity makes $x$ the only solution, so $g(f(x)) = x$.
2. Every $y$ is in the image, so $g$ is total and $f(g(y)) = y$. For $f(x) = \lfloor x / 2 \rfloor$, $g(y) = 2y$, and $g(f(1)) = g(0) = 0 \neq 1$: $g$ is a right inverse of $f$, not an inverse.
:::
::::

::::exercise{#ex-mu-graph-sigma difficulty=2 objective="Characterize the partial recursive functions by their graphs, using the normal form theorem."}
Show that a partial function $f : \nat^k \rightharpoonup \nat$ is partial recursive if and only if there is a primitive recursive predicate $R \subseteq \nat^{k+2}$ such that, for all $\vec x$ and $y$, $f(\vec x)\converge = y$ if and only if $\exists s\ R(\vec x, y, s)$.

:::solution
Suppose $f$ is partial recursive. By :ref{#thm-kleene-normal-form}, $f(\vec x) \simeq U(\mu s\, T_k(e, \vec x, s))$ for some $e$. Let
$$
R(\vec x, y, s) \iff T_k(e, \vec x, s) \wedge \forall s' < s\ \neg T_k(e, \vec x, s') \wedge U(s) = y,
$$
which is primitive recursive. Then $\exists s\ R(\vec x, y, s)$ holds if and only if the least $s$ with $T_k(e, \vec x, s)$ exists and $U$ maps it to $y$, that is, if and only if $f(\vec x)\converge = y$.

Conversely, given $R$, let $f'(\vec x) \simeq \pi_0\big(\mu z\, R(\vec x, \pi_0(z), \pi_1(z))\big)$, which is partial recursive. If $f(\vec x)\converge = y$, there is $s$ with $R(\vec x, y, s)$, so the search, over a total predicate, terminates; it returns some $z$ with $R(\vec x, \pi_0(z), \pi_1(z))$, and then $f(\vec x) = \pi_0(z)$ by the hypothesis, so $f'(\vec x) = f(\vec x)$. If $f(\vec x)\diverge$, no pair satisfies $R(\vec x, \cdot, \cdot)$ and the search diverges. Hence $f = f'$. (The search may find a $z$ other than $\langle y, s \rangle$ for the least $s$, but its first component is always $y$.)
:::
::::

::::exercise{#ex-mu-regular-not-pr difficulty=1 lessons="ackermann-function" objective="Show that the primitive recursive functions are not closed under regular minimization."}
Give a primitive recursive regular function $g : \nat^2 \to \nat$ such that $x \mapsto \mu z\, [g(x, z) = 0]$ is not primitive recursive.

:::solution
Let $G$ be the graph of the Ackermann function, primitive recursive by :ref{#ex-ack-graph}, and $g(x, z) = 1 \dotminus \chi_G(\pi_0(x), \pi_1(x), z)$. It is primitive recursive and regular, since $g(x, z) = 0$ for $z = A(\pi_0(x), \pi_1(x))$, and this is the only zero. So $f(x) = \mu z\, [g(x, z) = 0] = A(\pi_0(x), \pi_1(x))$. If $f$ were primitive recursive, so would be $A(a, b) = f(\langle a, b \rangle)$, contradicting :ref{#cor-ack-not-pr}.
:::
::::

::::exercise{#ex-mu-partial-cases difficulty=2 lessons="register-machines" objective="Use the normal form theorem to define partial recursive functions by cases without evaluating the case that does not apply."}
Let $f_1, f_2 : \nat^k \rightharpoonup \nat$ be partial recursive and $P \subseteq \nat^k$ recursive. Show that the partial function $f$ with $f(\vec x) \simeq f_1(\vec x)$ if $P(\vec x)$ and $f(\vec x) \simeq f_2(\vec x)$ otherwise is partial recursive. Why does the formula $f_1(\vec x) \cdot \chi_P(\vec x) + f_2(\vec x) \cdot \chi_{\neg P}(\vec x)$ not work?

:::solution
By :ref{#thm-kleene-normal-form}, there are $e_1, e_2$ with $f_i(\vec x) \simeq U(\mu s\, T_k(e_i, \vec x, s))$. Let
$$
f'(\vec x) \simeq U\big(\mu s\, [(P(\vec x) \wedge T_k(e_1, \vec x, s)) \vee (\neg P(\vec x) \wedge T_k(e_2, \vec x, s))]\big).
$$
The predicate in brackets is recursive, by :ref{#ex-mu-recursive-closure}, so $f'$ is partial recursive. If $P(\vec x)$, the predicate reduces to $T_k(e_1, \vec x, s)$ and $f'(\vec x) \simeq f_1(\vec x)$; otherwise $f'(\vec x) \simeq f_2(\vec x)$. Hence $f = f'$. The arithmetic formula is defined only when both $f_1(\vec x)$ and $f_2(\vec x)$ are, by the convention on undefined subexpressions: if $P(\vec x)$ holds and $f_2(\vec x)\diverge$, the formula is undefined while $f(\vec x) \simeq f_1(\vec x)$ may be defined. The normal form replaces the evaluation of both functions by a single search, which looks only for a computation of the function of the case that applies; :ref{#ex-urm-cases} does the same with a branching program.
:::
::::
:::::
