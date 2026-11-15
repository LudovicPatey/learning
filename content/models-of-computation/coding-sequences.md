---
title: Coding finite sequences
summary: Primitive recursive coding of finite sequences of integers, operations on codes, course-of-values recursion, and Gödel's β-function.
duration: 30
prerequisites: [primitive-recursion]
---

Programs manipulate lists, stacks and arrays of unbounded size, while the functions we study take a fixed number of integer arguments. We now show that finite sequences of integers can be coded by single integers, in such a way that all the usual operations on sequences become primitive recursive. This coding is used constantly: to describe configurations of machines, to code programs and formulas, and to define functions by recursion on all previous values.

Cantor's pairing function already codes pairs, and by iteration tuples of a **fixed** length. Here the length is part of the data.

## Prime power coding

We write $p_0 = 2, p_1 = 3, p_2 = 5, \dots$ for the primes and $(x)_i$ for the exponent of $p_i$ in $x \geq 1$; both are primitive recursive by the previous lesson.

:::definition{#def-seq-code}
The **code** of the finite sequence $(a_0, \dots, a_{n-1})$ of integers is
$$
[a_0, \dots, a_{n-1}] = \prod_{i < n} p_i^{\,a_i + 1} = 2^{a_0 + 1} \cdot 3^{a_1 + 1} \cdots p_{n-1}^{\,a_{n-1} + 1}.
$$
The empty sequence has code $[\,] = 1$.
:::

For instance, $[1, 0, 2] = 2^{2} \cdot 3^{1} \cdot 5^{3} = 1500$, and conversely $1500$ is decoded by factoring it: the exponents $2, 1, 3$ of $p_0, p_1, p_2$ give the entries $1, 0, 2$, and the first prime with exponent $0$, here $p_3 = 7$, gives the length $3$.

By the uniqueness of prime factorizations, the coding is injective. The exponents are shifted by one so that a sequence ending with zeros, such as $(5, 0)$, has a different code from $(5)$: indeed $[5] = 2^6$ while $[5, 0] = 2^6 \cdot 3$. The coding is not surjective — $0$, $3$ or $10$ are not codes — but the set of codes is primitive recursive.

:::proposition{#prop-seq-operations}
The following functions and predicates are primitive recursive:

1. the **length** $\mathrm{lh}(s)$, equal to $n$ if $s = [a_0, \dots, a_{n-1}]$;
2. the **projection** $(s)'_i$, equal to $a_i$ if $s = [a_0, \dots, a_{n-1}]$ and $i < n$;
3. the predicate $\mathrm{Seq}(s)$: "$s$ is the code of a sequence";
4. the **concatenation** $s * t$, with $[a_0, \dots, a_{n-1}] * [b_0, \dots, b_{m-1}] = [a_0, \dots, a_{n-1}, b_0, \dots, b_{m-1}]$;
5. the **restriction** $s \upharpoonright m$, equal to $[a_0, \dots, a_{m-1}]$ for $m \leq n$;
6. the **update** $\mathrm{set}(s, i, v)$, equal to the code of the sequence obtained by replacing $a_i$ with $v$, for $i < n$.

(The values on arguments that are not codes, or out of range, are irrelevant; the definitions below give some primitive recursive value.)
:::

:::proof{of=prop-seq-operations}
1. The exponents of a code are non-zero exactly on an initial segment of the primes, so $\mathrm{lh}(s) = \mu i < s\ ((s)_i = 0)$. The bound is correct since $s \geq 2^{\mathrm{lh}(s)} > \mathrm{lh}(s)$ for a code $s$.
2. $(s)'_i = (s)_i \dotminus 1$.
3. $\mathrm{Seq}(s) \iff s \geq 1 \wedge \forall i < s\ \big( (s)_i \neq 0 \leftrightarrow i < \mathrm{lh}(s) \big)$. The quantifier can be bounded by $s$ since $(s)_i = 0$ for $p_i > s$, and $p_i > i$.
4. $s * t = s \cdot \prod_{j < \mathrm{lh}(t)} p_{\mathrm{lh}(s) + j}^{\,(t)_j}$.
5. $s \upharpoonright m = \prod_{i < m} p_i^{\,(s)_i}$.
6. $\mathrm{set}(s, i, v) = \lfloor s / p_i^{(s)_i} \rfloor \cdot p_i^{\,v + 1}$.

Each expression is built from primitive recursive functions using bounded sums, products and minimization.
:::

:::quiz[prime power coding]
Why is $\mathrm{lh}(s)$ defined by a **bounded** minimization, and why is the bound $s$ correct?

- [x] Bounded minimization keeps the function primitive recursive; and a code of a sequence of length $n$ is at least $2^n > n$, so the first zero exponent occurs at an index smaller than $s$.
- [ ] Because $\mathrm{lh}(s) \leq (s)_0$.

  The first entry $a_0$ has nothing to do with the length.
- [ ] The bound is not needed: unbounded minimization of a primitive recursive predicate is primitive recursive.

  It is not: unbounded search may produce partial functions.

---

Which sequences have codes $12$ and $18$, if any?

- [x] $12 = 2^2 \cdot 3$ codes $(1, 0)$, and $18 = 2 \cdot 3^2$ codes $(0, 1)$.
- [ ] $12$ codes $(2, 1)$.

  Exponents are shifted by one: exponent $e$ codes the value $e - 1$.
- [ ] Neither is a code.

  Both have non-zero exponents exactly at $p_0$ and $p_1$.
:::

## Course-of-values recursion

Primitive recursion defines $f(\vec x, y + 1)$ from the single previous value $f(\vec x, y)$. Many natural definitions use **all** previous values — the Fibonacci sequence uses two of them, and the definition of the code of a formula uses the codes of all its subformulas. Sequence coding reduces such definitions to primitive recursion: instead of $f$, one computes by primitive recursion the function which returns the code of the whole list of values computed so far, as in the figure below.

:::definition{#def-course-of-values}
For $f : \nat^{k+1} \to \nat$, its **course-of-values** function is
$$
\bar f(\vec x, y) = [f(\vec x, 0), f(\vec x, 1), \dots, f(\vec x, y - 1)].
$$
:::

:::figure[Course-of-values recursion, with the parameters $\vec x$ omitted. The values $f(0), \dots, f(y-1)$ are packed into one integer $\bar f(y)$; the function $h$ computes $f(y)$ from it, and the new value is appended to the code, giving $\bar f(y + 1)$. The passage from $\bar f(y)$ to $\bar f(y+1)$ is a primitive recursion.]
<svg class="fig" viewBox="0 0 560 170" width="560" role="img" aria-label="The values f(0) to f(y-1) are packed into one code, from which h computes f(y), which is appended"><defs><marker id="ah-cov" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="20" y="50" width="70" height="32" rx="2" class="cell"/><text x="55.0" y="72" text-anchor="middle" font-size="15"><tspan class="math">f</tspan><tspan class="mrm">(0)</tspan></text><rect x="94" y="50" width="70" height="32" rx="2" class="cell"/><text x="129.0" y="72" text-anchor="middle" font-size="15"><tspan class="math">f</tspan><tspan class="mrm">(1)</tspan></text><text x="188" y="72" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><rect x="208" y="50" width="96" height="32" rx="2" class="cell"/><text x="256.0" y="72" text-anchor="middle" font-size="15"><tspan class="math">f</tspan><tspan class="mrm">(</tspan><tspan class="math">y</tspan><tspan class="mrm"> − 1)</tspan></text><rect x="314" y="50" width="70" height="32" rx="2" class="cell head-cell"/><text x="349" y="72" text-anchor="middle" font-size="15"><tspan class="math">f</tspan><tspan class="mrm">(</tspan><tspan class="math">y</tspan><tspan class="mrm">)</tspan></text><path d="M20,42 L20,36 L304,36 L304,42" class="accent-stroke" fill="none" stroke-width="1.3"/><text x="164.0" y="28" text-anchor="middle" class="label">one integer: the code of all previous values</text><rect x="190" y="112" width="120" height="32" rx="8" class="soft-fill accent-stroke" stroke-width="1.3"/><text x="250" y="134" text-anchor="middle" font-size="15"><tspan class="math">h</tspan><tspan class="mrm">(</tspan><tspan class="math">y</tspan><tspan class="mrm">, ·)</tspan></text><path d="M164.0,86 L230,108" class="ink-stroke" fill="none" stroke-width="1.3" marker-end="url(#ah-cov)"/><path d="M312,128 C338,132 349,112 349,88" class="ink-stroke" fill="none" stroke-width="1.3" marker-end="url(#ah-cov)"/><text x="392" y="64" class="label">appended to</text><text x="392" y="80" class="label">the code</text></svg>
:::

:::theorem[Course-of-values recursion]{#thm-course-of-values}
Let $h : \nat^{k+2} \to \nat$ be primitive recursive. Then the function $f$ defined by
$$
f(\vec x, y) = h(\vec x, y, \bar f(\vec x, y))
$$
is primitive recursive.
:::

:::proof{of=thm-course-of-values}
The equation determines $f(\vec x, y)$ by induction on $y$, since $\bar f(\vec x, y)$ only involves values at arguments smaller than $y$. The function $\bar f$ satisfies the primitive recursion
$$
\begin{gathered}
\bar f(\vec x, 0) = 1, \\
\bar f(\vec x, y + 1) = \bar f(\vec x, y) \cdot p_y^{\,h(\vec x, y, \bar f(\vec x, y)) + 1},
\end{gathered}
$$
so $\bar f$ is primitive recursive. Finally $f(\vec x, y) = (\bar f(\vec x, y + 1))'_y$.
:::

:::quiz[course-of-values recursion]
In the proof, why is it necessary to work with $\bar f$ rather than with $f$ directly?

- [x] The primitive recursion scheme only passes the previous value to $h$; $\bar f(\vec x, y)$ packs all previous values into a single number, so $\bar f$ itself satisfies an ordinary primitive recursion.
- [ ] Because $f$ is not total.

  $f$ is total: it is defined by induction on $y$.
- [ ] Because $h$ needs to know the length of the sequence.

  The length is $y$, which $h$ receives anyway.
:::

As an example, the Fibonacci sequence satisfies $\mathrm{fib}(y) = h(y, \overline{\mathrm{fib}}(y))$ where $h(y, s) = y$ if $y \leq 1$ and $h(y, s) = (s)'_{y-1} + (s)'_{y-2}$ otherwise.

## Gödel's β-function

The prime power coding uses exponentiation. In the proof of the incompleteness theorems, Gödel needed to code sequences using only addition and multiplication, because these are the only operations of the language of arithmetic. His solution relies on the Chinese remainder theorem: a sequence $a_0, \dots, a_{n-1}$ is stored as the remainders of a single number $c$ modulo $n$ pairwise coprime moduli, each larger than the corresponding $a_i$. The moduli themselves must be described by a single parameter $d$, and the moduli $1 + (i + 1) d$ are pairwise coprime for a suitable $d$.

:::definition{#def-beta}
**Gödel's β-function** is $\beta(c, d, i) = c \bmod \big(1 + (i + 1) d\big)$.
:::

:::lemma[Gödel]{#lem-beta}
For every finite sequence $a_0, \dots, a_{n-1}$ of integers there exist $c, d$ such that $\beta(c, d, i) = a_i$ for all $i < n$.
:::

:::proof{of=lem-beta}
Let $m = \max(n, a_0, \dots, a_{n-1})$ and $d = m!$. We claim that the moduli $u_i = 1 + (i+1)d$, for $i < n$, are pairwise coprime. Suppose that a prime $q$ divides $u_i$ and $u_j$ with $i < j < n$. Then $q$ divides $u_j - u_i = (j - i) d$, so $q$ divides $j - i$ or $d$. Since $1 \leq j - i \leq n \leq m$, the integer $j - i$ divides $m! = d$; in both cases $q$ divides $d$. But then $q$ divides $u_i - (i+1)d = 1$, which is absurd.

By the Chinese remainder theorem there is $c$ such that $c \equiv a_i \pmod{u_i}$ for all $i < n$. Since $a_i \leq m \leq d < u_i$, the remainder of $c$ modulo $u_i$ is exactly $a_i$, that is $\beta(c, d, i) = a_i$.
:::

:::example{#ex-beta}
For the sequence $(2, 0, 1)$, the proof takes $m = 3$ and $d = 3! = 6$, hence the moduli $u_0 = 7$, $u_1 = 13$, $u_2 = 19$. The least $c$ with $c \equiv 2 \pmod 7$, $c \equiv 0 \pmod{13}$ and $c \equiv 1 \pmod{19}$ is $c = 1521 = 13 \cdot 117$; indeed $1521 = 7 \cdot 217 + 2 = 19 \cdot 80 + 1$. So $\beta(1521, 6, i)$ equals $2, 0, 1$ for $i = 0, 1, 2$. The factorial is a convenient choice, not always the smallest one: here $d = 1$ fails, since the remainder modulo $u_0 = 2$ cannot be $2$, but $d = 2$, with the pairwise coprime moduli $3, 5, 7$, works.
:::

:::quiz[the β-function lemma]
Where does the proof use the inequality $a_i < u_i$?

- [x] To conclude that the remainder of $c$ modulo $u_i$ is $a_i$ itself, and not only congruent to $a_i$.
- [ ] To prove that the moduli are pairwise coprime.

  Coprimality uses that $j - i$ divides $d$.
- [ ] To apply the Chinese remainder theorem.

  The Chinese remainder theorem only requires pairwise coprime moduli.

---

Why is $d$ chosen as a factorial, $d = m!$ with $m \geq n$?

- [x] So that every difference $j - i$ with $1 \leq j - i < n$ divides $d$, which forces any common prime factor of $u_i$ and $u_j$ to divide $d$.
- [ ] To make $d$ larger than the values $a_i$.

  This is also needed, but any large $d$ would achieve it; the factorial is needed for coprimality.
- [ ] Because $\beta$ must be primitive recursive.

  $\beta$ is primitive recursive for any $d$.
:::

The function $\beta$ is defined from $+$, $\cdot$ and the remainder, and the relation $\beta(c, d, i) = a$ is expressible by the arithmetic formula $\exists q \leq c\ \big(c = q \cdot (1 + (i+1) d) + a \wedge a < 1 + (i+1) d\big)$. This is how sequences, and hence computations, are represented in first-order arithmetic.

## Exercises

::::exercise{#ex-seq-sort difficulty=2 objective="Compute a function on codes by a bounded search for its value, after bounding the value."}
Show that the function which maps the code of a sequence to the code of the same sequence sorted in non-decreasing order is primitive recursive.

:::hint
Bound the code of the sorted sequence in terms of $s$, and search for it.
:::

:::solution
The sorted sequence has the same length $n$ and the same entries, so its code is at most $\prod_{i < n} p_i^{M + 1}$ where $M = \max_i (s)'_i$, a primitive recursive function $b(s)$ of $s$. The sorted code is $\mu t < b(s) + 1\ \big(\mathrm{Seq}(t) \wedge \mathrm{lh}(t) = \mathrm{lh}(s) \wedge t \text{ is non-decreasing} \wedge \forall v \leq M\ \#_v(t) = \#_v(s)\big)$, where $\#_v(s) = \sum_{i < \mathrm{lh}(s)} \chi_=((s)'_i, v)$ counts the occurrences of $v$. All of this is primitive recursive.
:::
::::

::::exercise{#ex-seq-bijective difficulty=2 objective="Define a bijective coding of sequences with the pairing function, and compute its operations by course-of-values recursion."}
Define a bijective coding of finite sequences: show that the function $\langle\!\langle \cdot \rangle\!\rangle$ given by $\langle\!\langle \, \rangle\!\rangle = 0$ and $\langle\!\langle a_0, \dots, a_{n} \rangle\!\rangle = 1 + \langle a_0, \langle\!\langle a_1, \dots, a_n \rangle\!\rangle \rangle$ is a bijection between finite sequences and $\nat$, and that its length and projection functions are primitive recursive.

:::solution
By induction on $z$: $z = 0$ codes only the empty sequence, and $z \geq 1$ codes exactly the sequences with first element $\pi_0(z - 1)$ followed by a sequence coded by $\pi_1(z - 1)$, which is smaller than $z$ since $\langle x, y \rangle \geq y$; by the induction hypothesis there is exactly one such sequence, which gives existence and uniqueness. The length satisfies $\mathrm{lh}(0) = 0$ and $\mathrm{lh}(z) = 1 + \mathrm{lh}(\pi_1(z - 1))$ for $z \geq 1$, a course-of-values recursion since $\pi_1(z - 1) < z$; by :ref{#thm-course-of-values}, $\mathrm{lh}$ is primitive recursive. For the projections, the parameter changes along the recursion, so it is simpler to iterate the tail: let $\mathrm{tl}(z, 0) = z$ and $\mathrm{tl}(z, i + 1) = \pi_1(\mathrm{tl}(z, i) \dotminus 1)$, a primitive recursion on $i$. If $z$ codes $(a_0, \dots, a_n)$ and $i \leq n$, then $\mathrm{tl}(z, i)$ codes $(a_i, \dots, a_n)$, so $a_i = \pi_0(\mathrm{tl}(z, i) \dotminus 1)$.
:::
::::

## Notes and references

The β-function lemma appears in Gödel's incompleteness paper of 1931, where it is used to express definitions by recursion in the language of arithmetic. Coding finite sequences by prime powers is also due to Gödel, and was used by Kleene to number derivations and computations (Soare, §17.2.2). Course-of-values recursion is treated in detail in Péter's monograph.

- R. Péter, *Rekursive Funktionen*, Akadémiai Kiadó, 1951.
- R. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §17.2.2.
- K. Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I*, Monatshefte für Mathematik und Physik 38 (1931), 173–198.
- S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952.

:::::exercises
::::exercise{#ex-seq-increasing-prefix difficulty=1 objective="Express properties of sequences by bounded quantification over the indices of their codes."}
Show that the following predicates are primitive recursive: "$s$ codes a strictly increasing sequence"; "$s$ codes a prefix of the sequence coded by $t$".

:::solution
$\mathrm{Seq}(s) \wedge \forall i < \mathrm{lh}(s)\ \forall j < \mathrm{lh}(s)\ (i < j \rightarrow (s)'_i < (s)'_j)$. For prefixes: $\mathrm{Seq}(s) \wedge \mathrm{Seq}(t) \wedge \mathrm{lh}(s) \leq \mathrm{lh}(t) \wedge \forall i < \mathrm{lh}(s)\ (s)'_i = (t)'_i$.
:::
::::

::::exercise{#ex-seq-decode difficulty=1 objective="Compute and decode prime power codes, and recognize integers that are not codes."}
Compute $[0, 2, 1]$. Decide whether $360$ and $140$ are codes of sequences, and if so of which ones.

:::solution
$[0, 2, 1] = 2^{1} \cdot 3^{3} \cdot 5^{2} = 1350$. Next, $360 = 2^3 \cdot 3^2 \cdot 5$: the exponents of $p_0, p_1, p_2$ are $3, 2, 1$, and all other exponents are $0$, so $360 = [2, 1, 0]$. Finally $140 = 2^2 \cdot 5 \cdot 7$: the exponent of $p_1 = 3$ is $0$ while those of $p_2$ and $p_3$ are not, so the non-zero exponents do not form an initial segment of the primes, and $140$ is not a code.
:::
::::

::::exercise{#ex-seq-cov-sum difficulty=1 objective="Apply course-of-values recursion to a recursion on all previous values."}
Let $f(0) = 1$ and $f(y + 1) = \sum_{z \leq y} f(z)$. Show that $f$ is primitive recursive by :ref{#thm-course-of-values}, and that $f(y) = 2^{y-1}$ for $y \geq 1$.

:::solution
$f(y) = h(y, \bar f(y))$ for $h(y, s) = 1$ if $y = 0$ and $h(y, s) = \sum_{i < y} (s)'_i$ if $y \geq 1$. Indeed $\bar f(y + 1) = [f(0), \dots, f(y)]$, whose $i$-th entry is $f(i)$. The function $h$ is primitive recursive, by cases and a bounded sum of the primitive recursive projection, so :ref{#thm-course-of-values} applies. For the closed form, $f(1) = f(0) = 1 = 2^0$, and if $f(z) = 2^{z-1}$ for $1 \leq z \leq y$, then $f(y + 1) = 1 + \sum_{z = 1}^{y} 2^{z - 1} = 1 + (2^y - 1) = 2^y$.
:::
::::

::::exercise{#ex-seq-reverse difficulty=1 objective="Define an operation on sequence codes by a bounded product of prime powers."}
Show that the function which maps the code of $(a_0, \dots, a_{n-1})$ to the code of $(a_{n-1}, \dots, a_0)$ is primitive recursive.

:::solution
Let $\mathrm{rev}(s) = \prod_{i < \mathrm{lh}(s)} p_i^{\,(s)_{\mathrm{lh}(s) \dotminus (i + 1)}}$. If $s = [a_0, \dots, a_{n-1}]$, then $\mathrm{lh}(s) = n$ and the exponent of $p_i$ is $(s)_{n - 1 - i} = a_{n-1-i} + 1$, so $\mathrm{rev}(s) = [a_{n-1}, \dots, a_0]$. It is a bounded product of a primitive recursive function, composed with primitive recursive functions.
:::
::::

::::exercise{#ex-seq-beta-search difficulty=2 objective="Turn the existence proof of the β-function lemma into a primitive recursive bound, and search below it."}
Show that there is a primitive recursive function $B$ such that, for every code $s$ of a sequence $(a_0, \dots, a_{n-1})$, $B(s) = \langle c, d \rangle$ with $\beta(c, d, i) = a_i$ for all $i < n$.

:::solution
Let $m(s) = \max(\mathrm{lh}(s), \max_{i < \mathrm{lh}(s)} (s)'_i)$, which is primitive recursive (the maximum over $i < \mathrm{lh}(s)$ is a bounded minimization: the least $v \leq s$ such that $(s)'_i \leq v$ for all $i < \mathrm{lh}(s)$). The proof of :ref{#lem-beta} gives $d = m(s)!$ and a solution $c$ of the Chinese remainder problem modulo $u_i = 1 + (i + 1) d$, $i < n$; the least non-negative solution satisfies $c < \prod_{i < n} u_i$. Since $\langle x, y \rangle$ is increasing in each argument, the pair satisfies $\langle c, d \rangle \leq b(s)$, where
$$
b(s) = \Big\langle \prod_{i < \mathrm{lh}(s)} \big(1 + (i + 1)\, m(s)!\big),\ m(s)! \Big\rangle
$$
is primitive recursive. Let
$$
B(s) = \mu z < b(s) + 1\ \forall i < \mathrm{lh}(s)\ \beta(\pi_0(z), \pi_1(z), i) = (s)'_i .
$$
The predicate is primitive recursive, and it holds for $z = \langle c, d \rangle \leq b(s)$, so the search finds a pair with the required property. By :ref{#prop-pr-bounded-mu}, $B$ is primitive recursive. Thus a sequence can be converted primitive recursively from its prime power code to a β-code, and back with $\beta$.
:::
::::

::::exercise{#ex-seq-string-concat difficulty=2 lessons="what-is-an-algorithm" objective="Show that the length and the concatenation of strings are primitive recursive on their codes in bijective numeration."}
Fix $m \geq 2$, and code strings over an alphabet of $m$ letters by bijective numeration, as in the lesson :ref{to="models-of-computation/what-is-an-algorithm"}. Let $N_\ell = (m^\ell - 1)/(m - 1) = \sum_{j < \ell} m^j$.

1. Show that the codes of the strings of length $\ell$ are exactly the integers $z$ with $N_\ell \leq z < N_{\ell + 1}$.
2. Deduce that the function $\mathrm{len}(z)$, the length of the string coded by $z$, is primitive recursive.
3. Show that the function giving the code of the concatenation $uv$ from the codes of $u$ and $v$ is primitive recursive.

:::solution
1. Write $c(w)$ for the code of $w$. A string of length $\ell$ has code $\sum_{j=1}^{\ell} i_j m^{\ell - j}$ with $1 \leq i_j \leq m$, which lies between $\sum_{j < \ell} m^j = N_\ell$ (all digits $1$) and $m \sum_{j < \ell} m^j = N_{\ell + 1} - 1$ (all digits $m$). So the codes of the $m^\ell$ strings of length $\ell$ are $m^\ell$ distinct integers (the coding is injective) in an interval of $N_{\ell + 1} - N_\ell = m^\ell$ integers: they fill it.
2. The intervals $[N_\ell, N_{\ell+1})$ partition $\nat$, so $\mathrm{len}(z)$ is the least $\ell$ with $z < N_{\ell + 1}$. Since $N_{\ell+1} \geq \ell + 1$, the least such $\ell$ is at most $z$, and $\mathrm{len}(z) = \mu \ell < z + 1\ \big(z < N_{\ell + 1}\big)$. The function $\ell \mapsto N_\ell = \lfloor (m^\ell - 1) / (m - 1) \rfloor$ is primitive recursive, hence so is $\mathrm{len}$.
3. If $u = u_1 \cdots u_k$ and $v = v_1 \cdots v_\ell$ (as digits), then
$$
c(uv) = \sum_{j=1}^{k} u_j m^{k + \ell - j} + \sum_{j=1}^{\ell} v_j m^{\ell - j} = m^{\ell}\, c(u) + c(v).
$$
Hence the code of $uv$ is $c(u) \cdot m^{\mathrm{len}(c(v))} + c(v)$, a primitive recursive function of $c(u)$ and $c(v)$.
:::
::::
:::::
