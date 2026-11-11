---
title: Algorithms and partial functions
summary: Historical motivation for a formal notion of computability, partial functions and their notation, and the coding of finite objects by integers.
duration: 30
---

## The Entscheidungsproblem

Algorithms have been used since antiquity — Euclid's algorithm for the greatest common divisor, the sieve of Eratosthenes, Gaussian elimination — without any need for a definition of the word. As long as one only wishes to show that a problem *can* be solved mechanically, it suffices to exhibit a procedure that everybody accepts as mechanical.

The situation changed with the foundational program of Hilbert. In 1928, Hilbert and Ackermann formulated the *Entscheidungsproblem*: find a procedure which, given a formula of first-order logic, decides in finitely many steps whether this formula is universally valid. Gödel's incompleteness theorems (1931) made a positive answer increasingly implausible. But a negative answer requires proving that **no** algorithm solves the problem, and a statement about all algorithms can only be proved once the class of algorithms has been defined mathematically.

Several definitions were proposed between 1931 and 1936:

- the **general recursive functions** of Herbrand and Gödel (1934), studied systematically by Kleene;
- the **λ-definable functions** of Church and Kleene (1933–1936);
- the **Turing machines** (1936), together with the closely related machines of Post (1936).

Church (1936) and Turing (1936) independently gave a negative solution to the Entscheidungsproblem. The three classes of functions were quickly proved to coincide. Turing's analysis of what a human computer can do was decisive in convincing the community — including Gödel — that the definition was the right one.

Note that the first electronic computers were built a decade later. The notion being formalized is that of a function computable *by a human* following a finite set of instructions mechanically, with unlimited paper and time.

## Features of an algorithm

Any proposed definition should respect the following features of the informal notion.

1. **Finite description.** An algorithm is described by a finite text, fixed in advance, independent of the input.
2. **Discrete and deterministic steps.** The computation proceeds in steps. At each step, the next action is completely determined by the current situation, and each action is elementary — it requires no insight.
3. **Unbounded resources.** No bound is fixed in advance on the number of steps or on the amount of memory. A computation which terminates has however only performed finitely many steps, and therefore used only finitely much memory.
4. **Possible non-termination.** Nothing guarantees that a computation terminates. An algorithm therefore defines a **partial** function, undefined on the inputs on which the computation does not terminate.

Points 3 and 4 distinguish computability theory from complexity theory: we study what can be computed in principle, not what can be computed within given resources. Point 4 is not a defect of the definitions. We will see in the course on fundamentals that it cannot be avoided: there is no programming language with a computable interpreter whose programs compute exactly the total computable functions.

:::quiz[the requirements on algorithms]
Which of the following procedures satisfy the requirements above?

- [x] On input $x$, search for the least $n$ such that $n^2 > x$, trying $n = 0, 1, 2, \dots$ in turn.

  Finite description, elementary steps, and the search always terminates.
- [x] On input $x$, search for the least $n > x$ such that $n$ and $n + 2$ are both prime.

  This is an algorithm. Whether it terminates on every input is equivalent to the twin prime conjecture, which is open.
- [ ] On input $x$, return the $x$-th entry of an infinite table $f(0), f(1), f(2), \dots$ given in advance.

  An infinite table is not a finite description: every function $f$ would be computable in this sense.
- [ ] On input $x$, toss a fair coin to decide which branch of the computation to follow.

  The steps are not deterministic.
:::

## Partial functions

Throughout the course, $\nat = \{0, 1, 2, \dots\}$, and $\vec x$ abbreviates a tuple $(x_1, \dots, x_k)$ whose length is clear from the context.

:::definition{#def-partial-function}
A **partial function** $f : \nat^k \rightharpoonup \nat$ is a function from a subset $\dom f \subseteq \nat^k$, its **domain**, to $\nat$. We write $f(\vec x)\converge$ ("$f$ converges on $\vec x$") if $\vec x \in \dom f$, and $f(\vec x)\diverge$ ("$f$ diverges on $\vec x$") otherwise. We write $f(\vec x)\converge = y$ when $\vec x \in \dom f$ and $f(\vec x) = y$. A partial function is **total** if $\dom f = \nat^k$.
:::

Total functions are particular partial functions. The image of $f$ is $\operatorname{im} f = \{ f(\vec x) : \vec x \in \dom f \}$. The **empty function**, with empty domain, is denoted $\emptyset$ when no confusion is possible.

When partial functions are composed, an expression may be undefined. We adopt the following convention: an expression built from partial functions is defined only if all its subexpressions are defined. For instance, $g(f(x))\converge$ requires $f(x)\converge$ and $g$ to converge on the value $f(x)$. In particular, $0 \cdot f(x)$ is **undefined** when $f(x)\diverge$: we never evaluate an expression "lazily".

:::notation{#not-kleene-eq}
For two expressions $e_1, e_2$ built from partial functions, we write $e_1 \simeq e_2$ (**Kleene equality**) to mean that either both are undefined, or both are defined and have the same value.
:::

For instance, two partial functions $f, g$ are equal if and only if $f(\vec x) \simeq g(\vec x)$ for all $\vec x$. Some authors simply write $=$ for $\simeq$; we will do so in later courses, when no ambiguity can arise.

:::quiz[partial functions]
Let $f : \nat \rightharpoonup \nat$ be the partial function defined only on even numbers, with $f(2n) = n$. Which statements hold?

- [x] $f(f(8)) \simeq 2$.

  $f(8) = 4$ and $f(4) = 2$.
- [x] $f(f(6))\diverge$.

  $f(6) = 3$, and $f$ diverges on $3$.
- [ ] $0 \cdot f(3) \simeq 0$.

  By our convention, an expression is undefined as soon as one of its subexpressions is undefined.
- [ ] $f(3) \simeq f(5)$ is false, since $3 \neq 5$.

  Both sides are undefined, so $f(3) \simeq f(5)$ holds.
:::

## Coding finite objects by integers

Algorithms manipulate finite objects: integers, but also tuples, finite sequences, strings, formulas, graphs, and programs. We will mostly study functions on $\nat$. This is no restriction, because all these objects can be **coded** by integers in such a way that the usual operations on them become computable operations on the codes. The basic tool is a bijection between $\nat^2$ and $\nat$.

:::definition{#def-cantor-pairing}
**Cantor's pairing function** is the function $\langle \cdot, \cdot \rangle : \nat^2 \to \nat$ defined by
$$
\langle x, y \rangle = \frac{(x+y)(x+y+1)}{2} + y.
$$
:::

The pairs are enumerated diagonal by diagonal: $\langle 0,0 \rangle = 0$, $\langle 1,0 \rangle = 1$, $\langle 0,1 \rangle = 2$, $\langle 2,0 \rangle = 3$, $\langle 1,1 \rangle = 4$, $\langle 0,2 \rangle = 5$, and so on. Write $T(n) = n(n+1)/2$ for the $n$-th triangular number.

:::figure[The pairs $(x, y)$ with $x + y \leq 4$, labeled by $\langle x, y \rangle$. The enumeration follows each diagonal upwards, then jumps to the next diagonal.]
<svg class="fig" viewBox="0 0 330 300" width="330" role="img" aria-label="Cantor pairing: pairs numbered along diagonals"><defs><marker id="ah-cantor" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="42" y1="250" x2="302" y2="250" class="axis"/><line x1="60" y1="268" x2="60" y2="8" class="axis"/><text x="308" y="255" class="math" font-size="17">x</text><text x="55" y="2" class="math" font-size="17">y</text><text x="60" y="282" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="34" y="255" text-anchor="middle" class="mrm muted" font-size="13">0</text><text x="112" y="282" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="34" y="203" text-anchor="middle" class="mrm muted" font-size="13">1</text><text x="164" y="282" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="34" y="151" text-anchor="middle" class="mrm muted" font-size="13">2</text><text x="216" y="282" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="34" y="99" text-anchor="middle" class="mrm muted" font-size="13">3</text><text x="268" y="282" text-anchor="middle" class="mrm muted" font-size="13">4</text><text x="34" y="47" text-anchor="middle" class="mrm muted" font-size="13">4</text><line x1="75.0" y1="250.0" x2="95.0" y2="250.0" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-cantor)"/><line x1="101.4" y1="239.4" x2="72.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="73.4" y1="204.7" x2="148.8" y2="242.4" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-cantor)"/><line x1="153.4" y1="239.4" x2="124.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="101.4" y1="187.4" x2="72.0" y2="158.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="72.5" y1="154.3" x2="201.9" y2="240.6" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-cantor)"/><line x1="205.4" y1="239.4" x2="176.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="153.4" y1="187.4" x2="124.0" y2="158.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="101.4" y1="135.4" x2="72.0" y2="106.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="72.0" y1="103.0" x2="254.4" y2="239.8" class="muted-stroke" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah-cantor)"/><line x1="257.4" y1="239.4" x2="228.0" y2="210.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="205.4" y1="187.4" x2="176.0" y2="158.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="153.4" y1="135.4" x2="124.0" y2="106.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><line x1="101.4" y1="83.4" x2="72.0" y2="54.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-cantor)"/><circle cx="60" cy="250" r="14" class="node"/><text x="60" y="255" text-anchor="middle" class="mrm" font-size="14">0</text><circle cx="112" cy="250" r="14" class="node"/><text x="112" y="255" text-anchor="middle" class="mrm" font-size="14">1</text><circle cx="60" cy="198" r="14" class="node"/><text x="60" y="203" text-anchor="middle" class="mrm" font-size="14">2</text><circle cx="164" cy="250" r="14" class="node"/><text x="164" y="255" text-anchor="middle" class="mrm" font-size="14">3</text><circle cx="112" cy="198" r="14" class="node"/><text x="112" y="203" text-anchor="middle" class="mrm" font-size="14">4</text><circle cx="60" cy="146" r="14" class="node"/><text x="60" y="151" text-anchor="middle" class="mrm" font-size="14">5</text><circle cx="216" cy="250" r="14" class="node"/><text x="216" y="255" text-anchor="middle" class="mrm" font-size="14">6</text><circle cx="164" cy="198" r="14" class="node"/><text x="164" y="203" text-anchor="middle" class="mrm" font-size="14">7</text><circle cx="112" cy="146" r="14" class="node"/><text x="112" y="151" text-anchor="middle" class="mrm" font-size="14">8</text><circle cx="60" cy="94" r="14" class="node"/><text x="60" y="99" text-anchor="middle" class="mrm" font-size="14">9</text><circle cx="268" cy="250" r="14" class="node"/><text x="268" y="255" text-anchor="middle" class="mrm" font-size="14">10</text><circle cx="216" cy="198" r="14" class="node"/><text x="216" y="203" text-anchor="middle" class="mrm" font-size="14">11</text><circle cx="164" cy="146" r="14" class="node"/><text x="164" y="151" text-anchor="middle" class="mrm" font-size="14">12</text><circle cx="112" cy="94" r="14" class="node"/><text x="112" y="99" text-anchor="middle" class="mrm" font-size="14">13</text><circle cx="60" cy="42" r="14" class="node"/><text x="60" y="47" text-anchor="middle" class="mrm" font-size="14">14</text></svg>
:::

:::proposition{#prop-cantor-pairing-bijection}
The function $\langle \cdot, \cdot \rangle$ is a bijection from $\nat^2$ to $\nat$.
:::

:::proof{of=prop-cantor-pairing-bijection}
Fix $z \in \nat$. Since $T$ is strictly increasing with $T(0) = 0$, there is a unique $n$ such that $T(n) \leq z < T(n+1) = T(n) + n + 1$. Let $y = z - T(n)$, so that $0 \leq y \leq n$, and let $x = n - y$. Then $x + y = n$ and $\langle x, y \rangle = T(n) + y = z$, so the function is surjective.

For injectivity, suppose $\langle x, y \rangle = \langle x', y' \rangle = z$, and let $n = x + y$, $n' = x' + y'$. Since $0 \leq y \leq n$, we have $T(n) \leq z \leq T(n) + n < T(n+1)$, and similarly for $n'$. By uniqueness of $n$ above, $n = n'$; then $y = z - T(n) = y'$ and $x = n - y = x'$.
:::

The inverse functions $\pi_0, \pi_1 : \nat \to \nat$ with $\pi_0(\langle x, y \rangle) = x$ and $\pi_1(\langle x, y \rangle) = y$ are computed by the procedure of the proof: find $n$ with $T(n) \leq z < T(n+1)$ by trying $n = 0, 1, \dots, z$, then set $y = z - T(n)$ and $x = n - y$. Only a **bounded** search is needed, since $n \leq z$. This remark will become important when we study primitive recursive functions.

:::quiz[the pairing function]
What are $\pi_0(12)$ and $\pi_1(12)$?

- [x] $\pi_0(12) = 2$ and $\pi_1(12) = 2$.

  $T(4) = 10 \leq 12 < 15 = T(5)$, so $n = 4$, $y = 12 - 10 = 2$ and $x = 4 - 2 = 2$. Indeed $\langle 2, 2 \rangle = 10 + 2 = 12$.
- [ ] $\pi_0(12) = 3$ and $\pi_1(12) = 1$.

  $\langle 3, 1 \rangle = 10 + 1 = 11$.
- [ ] $\pi_0(12) = 0$ and $\pi_1(12) = 4$.

  $\langle 0, 4 \rangle = 10 + 4 = 14$.

---

In the injectivity part of the proof, why is it important that $y \leq n$?

- [x] It gives $T(n) \leq z < T(n+1)$, which determines $n = x + y$ from $z$ alone.
- [ ] It ensures that $x$ is non-negative.

  That is used in the surjectivity part, when defining $x = n - y$.
- [ ] It is not used.

  It is used: it gives $T(n) \leq z < T(n+1)$, which is what determines $n$ from $z$.
:::

Iterating the pairing function codes tuples of any fixed length: $\langle x_1, x_2, x_3 \rangle = \langle x_1, \langle x_2, x_3 \rangle \rangle$, and in general $\langle x_1, \dots, x_{k+1} \rangle = \langle x_1, \langle x_2, \dots, x_{k+1} \rangle \rangle$. For each $k \geq 1$ this gives a bijection $\nat^k \to \nat$. Finite sequences of arbitrary length require a little more care, since the length must be recoverable from the code; this is done in the lesson :ref{to="models-of-computation/coding-sequences"}.

Strings over a finite alphabet $\{a_1, \dots, a_m\}$ are coded by reading them as numerals in base $m$ with digits $1, \dots, m$ (*bijective numeration*): the string $a_{i_1} \cdots a_{i_\ell}$ is coded by $\sum_{j=1}^{\ell} i_j\, m^{\ell - j}$, which defines a bijection between strings and $\nat$, the empty string being coded by $0$. Programs, being strings, are coded the same way. With these codings, a function on finite objects is called computable if the corresponding function on codes is.

## Exercises

::::exercise{difficulty=1}
Show that the function $\nat^2 \to \nat$, $(x, y) \mapsto 2^x (2y + 1) - 1$ is a bijection. Compare it with Cantor's pairing function: which one is more economical, in the sense of the size of $\langle x, x \rangle$ as a function of $x$?

:::solution
Every integer $z \geq 1$ is uniquely of the form $2^x \cdot m$ with $m$ odd, that is $m = 2y + 1$. So $(x, y) \mapsto 2^x(2y+1)$ is a bijection from $\nat^2$ onto $\nat \setminus \{0\}$, and subtracting $1$ gives a bijection onto $\nat$. On the diagonal, $2^x(2x+1) - 1$ grows exponentially, whereas $\langle x, x \rangle = x(2x+1) + x$ is quadratic. Cantor's pairing is a polynomial bijection; by a theorem of Fueter and Pólya, it is, up to exchanging the coordinates, the only quadratic polynomial bijection from $\nat^2$ to $\nat$.
:::
::::

::::exercise{difficulty=1}
Show that $\langle x, y \rangle \geq x$ and $\langle x, y \rangle \geq y$ for all $x, y$, with equality only when $x = y = 0$, or $(x, y) = (1, 0)$ for the first inequality.

:::solution
$\langle x, y \rangle = T(x+y) + y$. Since $T(n) \geq n$, we get $\langle x, y \rangle \geq x + y + y \geq y$, and $\langle x, y \rangle \geq T(x) \geq x$. Since $\langle x, y \rangle \geq x + 2y$, equality $\langle x, y\rangle = x$ forces $y = 0$, and then $T(x) = x$, i.e. $x \in \{0, 1\}$. Equality $\langle x, y \rangle = y$ forces $T(x+y) = 0$, i.e. $x = y = 0$.
:::
::::

## Notes and references

The Entscheidungsproblem is formulated in Hilbert and Ackermann's textbook *Grundzüge der theoretischen Logik* (Springer, 1928). Its negative solution was obtained independently by Church and by Turing in 1936. The quadratic polynomial bijections $\nat^2 \to \nat$ were determined by Fueter and Pólya (1923): up to the exchange of coordinates, Cantor's pairing function is the only one.

- A. Church, *An unsolvable problem of elementary number theory*, American Journal of Mathematics 58 (1936), 345–363.
- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- R. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, chapter 1, for a historical account.
