---
title: Primitive recursive functions
summary: Definition of the primitive recursive functions and predicates, and their closure under definition by cases, bounded sums and products, bounded quantification and bounded minimization.
duration: 45
prerequisites: [what-is-an-algorithm]
---

Machines describe computations step by step. A different approach, due to Dedekind, Skolem, Gödel, Herbrand and Kleene, describes computable functions by the way they are **defined**: one starts from a few functions whose computability is evident, and closes them under operations which evidently preserve computability. In this lesson we study the functions obtained using composition and recursion on one argument. They form a large class of total computable functions, and the tools developed here are used throughout the course.

## Definition

:::definition{#def-pr-basic}
The **basic functions** are:

- the **zero** function $Z : \nat \to \nat$, $Z(x) = 0$;
- the **successor** function $S : \nat \to \nat$, $S(x) = x + 1$;
- the **projections** $p^k_i : \nat^k \to \nat$, $p^k_i(x_1, \dots, x_k) = x_i$, for $1 \leq i \leq k$.
:::

:::definition{#def-pr-schemes}
1. **Composition.** Given $h : \nat^m \to \nat$ and $g_1, \dots, g_m : \nat^k \to \nat$, the function $f = h \circ (g_1, \dots, g_m) : \nat^k \to \nat$ is defined by
$$
f(\vec x) = h(g_1(\vec x), \dots, g_m(\vec x)).
$$
2. **Primitive recursion.** Given $g : \nat^k \to \nat$ and $h : \nat^{k+2} \to \nat$, the function $f : \nat^{k+1} \to \nat$ is defined by
$$
f(\vec x, 0) = g(\vec x), \qquad f(\vec x, y + 1) = h(\vec x, y, f(\vec x, y)).
$$
For $k = 0$, the scheme reads $f(0) = a$ and $f(y + 1) = h(y, f(y))$, for a constant $a \in \nat$.
:::

By induction on $y$, the equations of the recursion scheme define a unique total function $f$.

:::definition{#def-primitive-recursive}
The class of **primitive recursive** functions is the smallest class of functions $\nat^k \to \nat$ ($k \geq 1$) containing the basic functions and closed under composition and primitive recursion.
:::

Equivalently, a function is primitive recursive if it has a **derivation**: a finite sequence of functions $f_1, \dots, f_n$, each of which is a basic function or is obtained from earlier functions of the sequence by composition or primitive recursion, the last one being the function in question.

:::proposition{#prop-pr-total-computable}
Every primitive recursive function is total and computable.
:::

:::proof{of=prop-pr-total-computable}
By induction on derivations. Basic functions are total and computable. If $g_1, \dots, g_m$ and $h$ are, so is their composition: compute the values $g_i(\vec x)$, then $h$ on them. If $g$ and $h$ are, then $f(\vec x, y)$ is computed by the loop: $v \leftarrow g(\vec x)$; for $z = 0, \dots, y - 1$, $v \leftarrow h(\vec x, z, v)$; return $v$. This loop is executed exactly $y$ times, so it terminates.
:::

Derivations are finite objects, so there are countably many primitive recursive functions, and their derivations can be effectively listed. This remark is the starting point of the proof, in the lesson :ref{to="models-of-computation/ackermann-function"}, that not every total computable function is primitive recursive.

## First closure properties

:::lemma{#lem-pr-explicit}
The primitive recursive functions are closed under **explicit transformations**: if $f : \nat^m \to \nat$ is primitive recursive and $i_1, \dots, i_m \in \{1, \dots, k\}$, then $g(x_1, \dots, x_k) = f(x_{i_1}, \dots, x_{i_m})$ is primitive recursive. In particular one may permute variables, identify them, and add dummy variables. The constant functions $c^k_a(\vec x) = a$ are primitive recursive.
:::

:::proof{of=lem-pr-explicit}
$g = f \circ (p^k_{i_1}, \dots, p^k_{i_m})$. For constants, $c^1_a = S \circ \cdots \circ S \circ Z$ with $a$ applications of $S$, and $c^k_a = c^1_a \circ p^k_1$.
:::

From now on we write definitions informally, as systems of equations, and leave the explicit use of projections and constants to the reader.

**Arithmetic.** The following functions are primitive recursive:

- **addition:** $x + 0 = x$, $x + (y + 1) = S(x + y)$. Formally, $g = p^1_1$ and $h = S \circ p^3_3$.
- **multiplication:** $x \cdot 0 = 0$, $x \cdot (y + 1) = x \cdot y + x$.
- **exponentiation:** $x^0 = 1$, $x^{y+1} = x^y \cdot x$ (so that $0^0 = 1$).
- **factorial:** $0! = 1$, $(y + 1)! = y! \cdot (y + 1)$.
- **predecessor:** $\mathrm{pred}(0) = 0$, $\mathrm{pred}(y + 1) = y$.
- **truncated subtraction:** $x \dotminus 0 = x$, $x \dotminus (y + 1) = \mathrm{pred}(x \dotminus y)$. Thus $x \dotminus y = x - y$ if $x \geq y$ and $0$ otherwise.
- **sign functions:** $\mathrm{sg}(x) = 1 \dotminus (1 \dotminus x)$, equal to $0$ if $x = 0$ and $1$ otherwise, and $\overline{\mathrm{sg}}(x) = 1 \dotminus x$.
- **distance:** $|x - y| = (x \dotminus y) + (y \dotminus x)$; also $\min(x, y) = x \dotminus (x \dotminus y)$ and $\max(x, y) = x + (y \dotminus x)$.

:::quiz[the recursion scheme]
Multiplication is defined by $x \cdot 0 = 0$ and $x \cdot (y + 1) = x \cdot y + x$. Which function $h$ is used in the recursion scheme?

- [x] $h(x, y, z) = z + x$
- [ ] $h(x, y, z) = y + x$

  The previous value $f(x, y)$ is the **third** argument of $h$; the second argument is the counter $y$.
- [ ] $h(x, y, z) = z \cdot x$

  Starting from $f(x, 0) = 0$, this would give $f(x, y) = 0$ for every $y$.

---

Which identity defines truncated subtraction from the predecessor?

- [x] $x \dotminus (y + 1) = \mathrm{pred}(x \dotminus y)$
- [ ] $x \dotminus (y + 1) = \mathrm{pred}(x) \dotminus y$

  This is a true identity, but it is not an instance of the recursion scheme on $y$ with $x$ as parameter: the parameter must stay fixed.
- [ ] $(x + 1) \dotminus y = S(x \dotminus y)$

  False for $x < y$; moreover the recursion is on the wrong variable.
:::

## Predicates

:::definition{#def-pr-predicate}
A predicate (or relation) $P \subseteq \nat^k$ is **primitive recursive** if its characteristic function $\chi_P$, equal to $1$ on $P$ and to $0$ outside $P$, is primitive recursive.
:::

We write $P(\vec x)$ for $\vec x \in P$.

:::proposition{#prop-pr-predicates-boolean}
The relations $x = y$, $x \neq y$, $x < y$, $x \leq y$ are primitive recursive. Primitive recursive predicates are closed under $\neg$, $\wedge$, $\vee$, $\rightarrow$.
:::

:::proof{of=prop-pr-predicates-boolean}
$\chi_{<}(x, y) = \mathrm{sg}(y \dotminus x)$, $\chi_{\leq}(x, y) = \chi_<(x, y + 1)$, $\chi_=(x, y) = \overline{\mathrm{sg}}(|x - y|)$, and $\chi_{\neq} = 1 \dotminus \chi_=$. For the connectives, $\chi_{\neg P} = 1 \dotminus \chi_P$, $\chi_{P \wedge Q} = \chi_P \cdot \chi_Q$, $\chi_{P \vee Q} = \mathrm{sg}(\chi_P + \chi_Q)$, and $P \rightarrow Q$ is $\neg P \vee Q$.
:::

:::proposition[Definition by cases]{#prop-pr-cases}
Let $P_1, \dots, P_n \subseteq \nat^k$ be primitive recursive predicates such that every $\vec x$ satisfies exactly one of them, and let $g_1, \dots, g_n : \nat^k \to \nat$ be primitive recursive. Then the function $f$ defined by $f(\vec x) = g_i(\vec x)$ if $P_i(\vec x)$ is primitive recursive.
:::

:::proof{of=prop-pr-cases}
$f(\vec x) = g_1(\vec x) \cdot \chi_{P_1}(\vec x) + \cdots + g_n(\vec x) \cdot \chi_{P_n}(\vec x)$.
:::

:::quiz[definition by cases]
The proof of :ref{#prop-pr-cases} evaluates every $g_i(\vec x)$, including those of the cases that do not apply. Why is this harmless here?

- [x] Primitive recursive functions are total, so every $g_i(\vec x)$ is defined; multiplying by $\chi_{P_i}(\vec x) = 0$ then removes it.

  For **partial** functions this formula would be wrong: $0 \cdot g_i(\vec x)$ is undefined when $g_i(\vec x)$ is. Definition by cases for partial functions requires a genuine branching, as in the register machine exercise.
- [ ] Because only one predicate holds.

  This ensures that the sum has a single non-zero term, but it does not prevent the other terms from being undefined.
- [ ] Because multiplication by $0$ is not primitive recursive.
:::

## Bounded sums, products and quantifiers

:::proposition{#prop-pr-bounded-sums}
If $f : \nat^{k+1} \to \nat$ is primitive recursive, so are
$$
s(\vec x, y) = \sum_{z < y} f(\vec x, z) \qquad\text{and}\qquad p(\vec x, y) = \prod_{z < y} f(\vec x, z),
$$
with the conventions that the empty sum is $0$ and the empty product is $1$.
:::

:::proof{of=prop-pr-bounded-sums}
$s(\vec x, 0) = 0$ and $s(\vec x, y + 1) = s(\vec x, y) + f(\vec x, y)$; similarly $p(\vec x, 0) = 1$ and $p(\vec x, y + 1) = p(\vec x, y) \cdot f(\vec x, y)$.
:::

:::corollary{#cor-pr-bounded-quantifiers}
If $P \subseteq \nat^{k+1}$ is primitive recursive, so are the predicates
$$
\exists z < y\ P(\vec x, z) \qquad\text{and}\qquad \forall z < y\ P(\vec x, z),
$$
and likewise with $z \leq y$.
:::

:::proof{of=cor-pr-bounded-quantifiers}
The characteristic functions are $\mathrm{sg}\big(\sum_{z < y} \chi_P(\vec x, z)\big)$ and $\prod_{z < y} \chi_P(\vec x, z)$. For $z \leq y$, replace $y$ by $y + 1$.
:::

More generally, the bound may be any primitive recursive function of the parameters: $\exists z < b(\vec x)\ P(\vec x, z)$ is obtained by composing with $b$.

## Bounded minimization

:::definition{#def-bounded-mu}
For a predicate $P \subseteq \nat^{k+1}$, the **bounded minimization**
$$
\mu z < y\ P(\vec x, z)
$$
denotes the least $z < y$ such that $P(\vec x, z)$, if there is one, and $y$ otherwise.
:::

:::proposition{#prop-pr-bounded-mu}
If $P$ is primitive recursive, then $f(\vec x, y) = \mu z < y\ P(\vec x, z)$ is primitive recursive.
:::

:::proof{of=prop-pr-bounded-mu}
For $v < y$, the product $\prod_{u \leq v} \overline{\mathrm{sg}}(\chi_P(\vec x, u))$ equals $1$ if no $u \leq v$ satisfies $P(\vec x, u)$, and $0$ otherwise. Hence
$$
f(\vec x, y) = \sum_{v < y}\ \prod_{u \leq v} \overline{\mathrm{sg}}(\chi_P(\vec x, u))
$$
counts the $v < y$ that are smaller than every witness. If the least witness $z_0 < y$ exists, these are exactly the $v < z_0$, so the sum is $z_0$; otherwise all $v < y$ are counted and the sum is $y$. By :ref{#prop-pr-bounded-sums}, $f$ is primitive recursive.
:::

:::quiz[bounded minimization]
In the proof of :ref{#prop-pr-bounded-mu}, what does the term of the sum indexed by $v$ express?

- [x] That none of $0, 1, \dots, v$ satisfies $P(\vec x, \cdot)$.
- [ ] That $v$ satisfies $P(\vec x, \cdot)$.

  That would be $\chi_P(\vec x, v)$; summing it would count the witnesses, not locate the first one.
- [ ] That $v$ is the least witness.

---

Why is bounded minimization primitive recursive, whereas unbounded search ("the least $z$ such that $P(\vec x, z)$") is not available in this class?

- [x] The bound makes the search a loop with a number of iterations known in advance; an unbounded search may never terminate, and primitive recursive functions are total.
- [ ] Because unbounded search cannot be expressed with sums and products.

  This is true but it is a consequence, not the reason.
- [ ] Unbounded search is primitive recursive when $P$ is.

  Unbounded search applied to a primitive recursive predicate may produce a partial function, which cannot be primitive recursive.
:::

## Arithmetic functions and primes

With bounded minimization at hand, most functions of elementary number theory are seen to be primitive recursive.

- **Quotient and remainder.** $\lfloor x / y \rfloor = \mu q < x + 1\ \big( (q + 1) \cdot y > x \big)$ for $y \geq 1$ (and $0$ for $y = 0$, by cases), and $x \bmod y = x \dotminus y \cdot \lfloor x / y \rfloor$.
- **Divisibility.** $y \mid x \iff \exists q \leq x\ (q \cdot y = x)$.
- **Primality.** $\mathrm{Prime}(x) \iff x \geq 2 \wedge \forall y < x\ (y \mid x \rightarrow y \leq 1)$.
- **Integer square root.** $\lfloor \sqrt x \rfloor = \mu r < x + 1\ \big((r+1)^2 > x\big)$.
- **Cantor pairing.** $\langle x, y \rangle = \lfloor (x + y)(x + y + 1) / 2 \rfloor + y$, and its inverses $\pi_0(z) = \mu x \leq z\ \exists y \leq z\ \langle x, y \rangle = z$ and similarly for $\pi_1$.

:::proposition{#prop-pr-primes}
The function $n \mapsto p_n$, where $p_0 = 2, p_1 = 3, p_2 = 5, \dots$ is the increasing enumeration of the primes, is primitive recursive.
:::

:::proof{of=prop-pr-primes}
Euclid's argument shows that $p_n! + 1$ has a prime factor larger than $p_n$, so $p_{n+1} \leq p_n! + 1$. Hence
$$
p_0 = 2, \qquad p_{n+1} = \mu z < p_n! + 2\ \big(z > p_n \wedge \mathrm{Prime}(z)\big).
$$
This is a primitive recursion with $h(n, v) = \mu z < v! + 2\ (z > v \wedge \mathrm{Prime}(z))$, which is primitive recursive by :ref{#prop-pr-bounded-mu}.
:::

:::quiz[the enumeration of primes]
Why does the proof need the bound $p_{n+1} \leq p_n! + 1$?

- [x] Without an explicit primitive recursive bound, the search for the next prime would be an unbounded search, which is not one of the schemes defining primitive recursive functions.
- [ ] To prove that there are infinitely many primes.

  The bound implies it, but its role in the proof is to bound the search.
- [ ] Because the factorial is needed to test primality.

  Primality is tested by bounded quantification, without factorials.
:::

Finally, every $x \geq 1$ is uniquely a product $\prod_i p_i^{e_i}$. The **exponent of $p_i$ in $x$** is
$$
(x)_i = \mu e < x\ \neg\big(p_i^{e+1} \mid x\big) \quad \text{for } x \geq 1, \qquad (0)_i = 0,
$$
which is primitive recursive. These exponents are the basis of the coding of finite sequences in the next lesson.

## Exercises

::::exercise{difficulty=1}
Show that $\gcd(x, y)$ and $\mathrm{lcm}(x, y)$ are primitive recursive.

:::solution
$\gcd(x, y) = \mu d \leq x + y\ \big(d \mid x \wedge d \mid y \wedge \forall e \leq x + y\ (e \mid x \wedge e \mid y \rightarrow e \leq d)\big)$, which is correct for $(x, y) \neq (0, 0)$; set $\gcd(0, 0) = 0$ by cases. For $x, y \geq 1$, $\mathrm{lcm}(x, y) = \lfloor xy / \gcd(x, y) \rfloor$, and $\mathrm{lcm}(x, y) = 0$ if $x = 0$ or $y = 0$.
:::
::::

::::exercise{difficulty=1}
Show that the primitive recursive functions are closed under **simultaneous recursion**: if $g_1, g_2, h_1, h_2$ are primitive recursive, so are the functions $f_1, f_2$ defined by $f_i(\vec x, 0) = g_i(\vec x)$ and $f_i(\vec x, y + 1) = h_i(\vec x, y, f_1(\vec x, y), f_2(\vec x, y))$. Deduce that the Fibonacci sequence is primitive recursive.

:::solution
Let $F(\vec x, y) = \langle f_1(\vec x, y), f_2(\vec x, y) \rangle$. Then $F(\vec x, 0) = \langle g_1(\vec x), g_2(\vec x) \rangle$ and $F(\vec x, y + 1) = \langle h_1(\vec x, y, \pi_0(F), \pi_1(F)), h_2(\vec x, y, \pi_0(F), \pi_1(F)) \rangle$ where $F$ stands for $F(\vec x, y)$. This is a primitive recursion, and $f_i = \pi_{i-1} \circ F$. For Fibonacci, take $f_1(y) = \mathrm{fib}(y)$, $f_2(y) = \mathrm{fib}(y + 1)$, with $f_1(y + 1) = f_2(y)$ and $f_2(y + 1) = f_1(y) + f_2(y)$.
:::
::::

::::exercise{difficulty=2}
Show that if $f : \nat \to \nat$ is primitive recursive and strictly increasing, then its range is a primitive recursive set. Is it true for every primitive recursive $f$?

:::solution
If $f$ is strictly increasing, then $f(z) \geq z$, so $y \in \operatorname{im} f \iff \exists z \leq y\ f(z) = y$, a bounded quantification. Without monotonicity this fails in general: there are primitive recursive functions whose range is not even computable. Fix a code $a$ of a program which halts on input $a$, and let $f(\langle e, t \rangle) = e$ if the program of code $e$ halts on input $e$ within $t$ steps, and $f(\langle e, t \rangle) = a$ otherwise. Step-bounded simulation is primitive recursive (see the lesson :ref{to="models-of-computation/equivalence-of-models"}), so $f$ is primitive recursive, and its range is the halting set $\{e : \Phi_e(e)\converge\}$, which is not computable (see the course on fundamentals).
:::
::::

## Notes and references

Definitions by recursion go back to Dedekind (1888) and Skolem (1923). Gödel used the primitive recursive functions — he called them *recursive* — to arithmetize syntax in his incompleteness theorem; the modern name is due to Kleene. Rózsa Péter's monograph is the classical reference on the subject.

- K. Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte für Mathematik und Physik 38 (1931), 173–198.
- R. Péter, *Rekursive Funktionen*, Akadémiai Kiadó, 1951.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989, chapter I.
