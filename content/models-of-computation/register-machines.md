---
title: Register machines
summary: Unlimited register machines (URM), their operational semantics, examples, concatenation of programs, and closure of URM-computable functions under composition.
duration: 45
prerequisites: [what-is-an-algorithm]
---

Turing machines access their memory sequentially, one cell at a time. **Register machines** instead have a memory made of registers, each holding a natural number, accessed directly by their index. Several variants were introduced around 1960 by Melzak, Lambek, Minsky, and Shepherdson and Sturgis. We use the **unlimited register machine** (URM) of Shepherdson and Sturgis, in the form popularized by Cutland's textbook. Its instruction set is small, which makes proofs about it short, and close to an assembly language, which makes it easy to program.

## Definition

The machine has infinitely many **registers** $R_1, R_2, R_3, \dots$, each containing a natural number. There is no bound on the size of these numbers.

:::definition{#def-urm}
A **URM program** is a finite sequence $P = I_1, \dots, I_s$ of **instructions**, each of one of the following four types:

| instruction | name | effect |
| --- | --- | --- |
| $Z(n)$ | zero | $R_n \leftarrow 0$ |
| $S(n)$ | successor | $R_n \leftarrow R_n + 1$ |
| $T(m, n)$ | transfer | $R_n \leftarrow R_m$ |
| $J(m, n, q)$ | jump | if $R_m = R_n$, the next instruction is $I_q$; otherwise it is the following one |

where $m, n, q \geq 1$.
:::

The operational semantics is defined through configurations.

:::definition{#def-urm-semantics}
A **register state** is a function $r : \nat_{\geq 1} \to \nat$ with $r(n) = 0$ for all but finitely many $n$. A **configuration** of $P$ is a pair $(i, r)$ where $i \geq 1$ is the index of the next instruction and $r$ is a register state. It is **halting** if $i > s$.

If $i \leq s$, the successor $(i', r')$ of $(i, r)$ is given by:

- if $I_i = Z(n)$: $r' = r[n \mapsto 0]$ and $i' = i + 1$;
- if $I_i = S(n)$: $r' = r[n \mapsto r(n) + 1]$ and $i' = i + 1$;
- if $I_i = T(m, n)$: $r' = r[n \mapsto r(m)]$ and $i' = i + 1$;
- if $I_i = J(m, n, q)$: $r' = r$, and $i' = q$ if $r(m) = r(n)$, $i' = i + 1$ otherwise.

Here $r[n \mapsto v]$ denotes the state equal to $r$ except that register $n$ contains $v$. The **computation** of $P$ from a configuration is the sequence of successive configurations, which is infinite or ends at the first halting configuration.
:::

Jumping to an instruction index larger than $s$ is therefore a way of halting the program.

:::definition{#def-urm-computes}
Let $k \geq 1$. The partial function $\varphi^{(k)}_P : \nat^k \rightharpoonup \nat$ **computed by $P$** is defined as follows. Start from the configuration $(1, r_{\vec x})$, where $r_{\vec x}(n) = x_n$ for $n \leq k$ and $r_{\vec x}(n) = 0$ for $n > k$. If the computation halts, in a configuration $(i, r)$, then $\varphi^{(k)}_P(\vec x) = r(1)$; otherwise $\varphi^{(k)}_P(\vec x)\diverge$.

A partial function is **URM-computable** if it is $\varphi^{(k)}_P$ for some program $P$.
:::

Note the asymmetries of the instruction set: registers can only be incremented, never decremented, and the only test is equality between two registers.

## Examples

**Addition.** With $x$ in $R_1$ and $y$ in $R_2$, the following program uses $R_3$ as a counter $k$ and increments $R_1$ until $k = y$:

| | | |
| --- | --- | --- |
| $I_1$ | $J(2, 3, 5)$ | if $k = y$, halt |
| $I_2$ | $S(1)$ | |
| $I_3$ | $S(3)$ | $k \leftarrow k + 1$ |
| $I_4$ | $J(1, 1, 1)$ | go to $I_1$ |

The instruction $J(1, 1, 1)$ compares $R_1$ with itself and always jumps: it is an unconditional jump. By induction on $j \leq y$, the configuration $(1, r)$ with $r(1) = x + j$, $r(2) = y$, $r(3) = j$ is reached; for $j = y$ the program jumps to $I_5$ and halts with $x + y$ in $R_1$.

**Multiplication.** The product is obtained by two nested loops. Register $R_3$ accumulates the result, $R_4$ counts the rounds of the outer loop and $R_5$ those of the inner loop.

| | | |
| --- | --- | --- |
| $I_1$ | $J(4, 2, 9)$ | if $R_4 = y$, go to the end |
| $I_2$ | $Z(5)$ | |
| $I_3$ | $J(5, 1, 7)$ | if $R_5 = x$, leave the inner loop |
| $I_4$ | $S(3)$ | |
| $I_5$ | $S(5)$ | |
| $I_6$ | $J(1, 1, 3)$ | |
| $I_7$ | $S(4)$ | |
| $I_8$ | $J(1, 1, 1)$ | |
| $I_9$ | $T(3, 1)$ | $R_1 \leftarrow R_3$ |

:::proposition{#prop-urm-mult}
The program above computes $(x, y) \mapsto x \cdot y$.
:::

:::proof{of=prop-urm-mult}
We prove by induction on $j \leq y$ that the computation reaches the configuration $(1, r_j)$ where $r_j(1) = x$, $r_j(2) = y$, $r_j(3) = jx$, $r_j(4) = j$, and $r_j(n) = 0$ for $n > 5$. For $j = 0$ this is the initial configuration. Suppose it holds for $j < y$. Since $r_j(4) = j \neq y$, the jump $I_1$ is not taken, and $I_2$ sets $R_5$ to $0$. Then, by an inner induction on $\ell \leq x$, the configuration $(3, r)$ with $R_3 = jx + \ell$ and $R_5 = \ell$ is reached; for $\ell = x$, the jump $I_3$ leads to $I_7$, which increments $R_4$, and $I_8$ returns to $I_1$ with $R_3 = (j+1)x$ and $R_4 = j + 1$. For $j = y$, $I_1$ jumps to $I_9$, which copies $xy$ into $R_1$, and the program halts.
:::

:::quiz[the multiplication program]
Why does the program need instruction $I_2 = Z(5)$?

- [x] The inner counter must restart from $0$ at each round of the outer loop; after the first round, $R_5$ contains $x$.

  Without it, from the second round on the jump $I_3$ would be taken immediately, and the result would be $x$ instead of $xy$ (for $y \geq 1$).
- [ ] Registers other than the inputs might be non-zero initially.

  By definition all registers other than the inputs initially contain $0$.
- [ ] To make the program halt when $x = 0$.

  When $x = 0$ the inner loop exits immediately anyway.

---

What does the following program compute, with input $x$ in $R_1$?

| | |
| --- | --- |
| $I_1$ | $J(1, 2, 3)$ |
| $I_2$ | $J(1, 1, 1)$ |

- [x] The partial function defined only at $0$, with value $0$.

  $R_2 = 0$. If $x = 0$, $I_1$ jumps to $I_3$, which does not exist: the program halts with $R_1 = 0$. Otherwise it loops forever between $I_1$ and $I_2$.
- [ ] The constant function $0$.

  The program does not halt on $x \neq 0$.
- [ ] The identity.

  For $x \neq 0$, the jump $J(1, 2, 3)$ fails since $R_2 = 0$, and $J(1, 1, 1)$ returns to $I_1$ forever: the program diverges.
:::

::::exercise{#ex-urm-pred difficulty=1 objective="Decrement a register with an instruction set that only increments, using two counters."}
Write a URM program computing $x \dotminus 1$, where $x \dotminus 1 = x - 1$ if $x \geq 1$ and $0 \dotminus 1 = 0$. Prove that it is correct.

:::hint
There is no decrement instruction. Maintain two counters $k$ and $k + 1$ in $R_2$ and $R_3$.
:::

:::solution
| | | |
| --- | --- | --- |
| $I_1$ | $J(1, 2, 8)$ | if $x = 0$, halt with output $0$ |
| $I_2$ | $S(3)$ | $R_2 = k = 0$, $R_3 = k + 1 = 1$ |
| $I_3$ | $J(1, 3, 7)$ | if $x = k + 1$, go to $I_7$ |
| $I_4$ | $S(2)$ | |
| $I_5$ | $S(3)$ | |
| $I_6$ | $J(1, 1, 3)$ | |
| $I_7$ | $T(2, 1)$ | output $k$ |

If $x = 0$, the program halts at once with $R_1 = 0$. If $x \geq 1$, one shows by induction on $k \leq x - 1$ that the configuration $(3, r)$ with $r(2) = k$ and $r(3) = k + 1$ is reached; for $k = x - 1$ the jump is taken and $x - 1$ is copied into $R_1$. Without $I_1$, the program would loop forever on input $0$, since $k + 1 \geq 1$.
:::
::::

## Combining programs

To build complex programs from simpler ones, we need to run one program after another, and to run a program on arguments stored in arbitrary registers. Two technical points must be handled: jumps that halt a program by jumping far beyond its end, and registers used as scratch space.

:::definition{#def-urm-standard}
A program $P = I_1, \dots, I_s$ is in **standard form** if every jump $J(m, n, q)$ of $P$ satisfies $q \leq s + 1$. We write $\rho(P)$ for the largest register index mentioned in $P$.
:::

The addition and multiplication programs above are in standard form: their jumps go to instructions of the program or, for the halting jump $J(2, 3, 5)$ of the addition program, to $I_{s+1}$. The program $J(1, 1, 7), S(1)$ is not: it halts at once by jumping to $I_7$, far beyond its end.

Every program $P$ is equivalent to a program in standard form, obtained by replacing every jump $J(m, n, q)$ with $q > s + 1$ by $J(m, n, s + 1)$: the computations are the same, and when $P$ halts, the standard form program halts in the configuration $(s + 1, r)$ with the same registers.

:::definition{#def-urm-concat}
Let $P = I_1, \dots, I_s$ and $Q = I'_1, \dots, I'_t$ be programs in standard form. The **concatenation** $PQ$ is the program $I_1, \dots, I_s, I''_1, \dots, I''_t$ where $I''_j$ is $I'_j$ with every jump target $q$ replaced by $q + s$.
:::

:::lemma{#lem-urm-concat}
Let $P, Q$ be in standard form and $r$ a register state. If the computation of $P$ from $(1, r)$ does not halt, neither does that of $PQ$. If it halts with register state $r'$, then the computation of $PQ$ from $(1, r)$ continues as the computation of $Q$ from $(1, r')$, with instruction indices shifted by $s$.
:::

:::proof{of=lem-urm-concat}
As long as the computation of $P$ is at an instruction $i \leq s$, the computations of $P$ and $PQ$ coincide, since the first $s$ instructions are the same. Because $P$ is in standard form, when $P$ halts it is at instruction $s + 1$, which in $PQ$ is the first instruction of the shifted copy of $Q$. From there, a straightforward induction shows that a configuration $(j, r'')$ of $Q$ corresponds to the configuration $(j + s, r'')$ of $PQ$, since jump targets have been shifted accordingly.
:::

:::quiz[concatenation]
Why must $P$ be in standard form for :ref{#lem-urm-concat} to hold?

- [x] If $P$ halted by jumping to some $q > s + 1$, the concatenation would continue at instruction $q$ of $PQ$, in the middle of $Q$ or beyond it, instead of at the beginning of $Q$.
- [ ] Otherwise $P$ could use registers also used by $Q$.

  Register conflicts are a separate issue, dealt with below.
- [ ] Because $Q$ must start with a jump.

  $Q$ is arbitrary; the condition concerns how $P$ halts, not how $Q$ starts.
:::

To run a program on arguments located in arbitrary registers, and to place its result in a chosen register, we use the following notation. Let $P$ be a program in standard form computing a $k$-ary function, and let $\ell_1, \dots, \ell_k, \ell$ be registers with indices greater than $\rho(P)$ and $k$. We write $P[\ell_1, \dots, \ell_k \to \ell]$ for the program
$$
Z(1), \dots, Z(\rho(P)),\ T(\ell_1, 1), \dots, T(\ell_k, k),\ P,\ T(1, \ell),
$$
put in standard form (the concatenations being taken as above). It clears the registers used by $P$, copies the arguments into $R_1, \dots, R_k$, runs $P$, and copies the result into $R_\ell$.

:::lemma{#lem-urm-subroutine}
Let $P$ compute $f : \nat^k \rightharpoonup \nat$. Started in any register state $r$ with $r(\ell_i) = x_i$, the program $P[\ell_1, \dots, \ell_k \to \ell]$ halts if and only if $f(\vec x)\converge$; in that case it halts with $f(\vec x)$ in $R_\ell$, and with all registers $R_n$ for $n > \max(\rho(P), k)$, $n \neq \ell$, unchanged.
:::

:::proof{of=lem-urm-subroutine}
Since the $\ell_i$ are larger than $\rho(P)$ and $k$, the zeroing instructions do not affect them, and after the transfers the registers $R_1, \dots, R_{\max(\rho(P), k)}$ contain exactly the initial configuration of $P$ on input $\vec x$ restricted to these registers. The registers beyond $\rho(P)$ are never mentioned by $P$: they do not influence the computation and are not modified by it. Therefore the computation of $P$ proceeds as from its initial configuration on $\vec x$. The conclusion follows from :ref{#lem-urm-concat}.
:::

## Closure under composition

To compute $h(g_1(\vec x), \dots, g_m(\vec x))$, one runs the programs for $g_1, \dots, g_m$ in turn, then the program for $h$. The obstacle is interference: each program uses the low registers as scratch space, so running $G_1$ may destroy the input that $G_2$ needs, and running $G_2$ may destroy the value computed by $G_1$. The solution is to keep the input and the intermediate values in registers beyond the reach of all the programs involved, and to call each program as a subroutine.

:::theorem{#thm-urm-composition}
Let $g_1, \dots, g_m : \nat^k \rightharpoonup \nat$ and $h : \nat^m \rightharpoonup \nat$ be URM-computable. Then the partial function
$$
f(\vec x) \simeq h(g_1(\vec x), \dots, g_m(\vec x))
$$
is URM-computable.
:::

:::proof{of=thm-urm-composition}
Let $G_1, \dots, G_m, H$ be programs in standard form computing $g_1, \dots, g_m, h$. Let $N$ be larger than $k$, $m$ and the numbers $\rho(G_i)$, $\rho(H)$. We use the registers $R_{N+1}, \dots, R_{N+k}$ to save the input, and $R_{N+k+1}, \dots, R_{N+k+m}$ to store the values $g_i(\vec x)$, as in the figure below. Consider the program
$$
\begin{aligned}
& T(1, N{+}1),\ \dots,\ T(k, N{+}k), \\
& G_1[N{+}1, \dots, N{+}k \to N{+}k{+}1],\ \dots,\ G_m[N{+}1, \dots, N{+}k \to N{+}k{+}m], \\
& H[N{+}k{+}1, \dots, N{+}k{+}m \to 1].
\end{aligned}
$$
(The last block copies its result into $R_1$; the definition of $P[\dots \to \ell]$ is adapted in the obvious way when $\ell = 1$.) By :ref{#lem-urm-subroutine} and :ref{#lem-urm-concat}, if all $g_i(\vec x)$ converge, the program successively stores $g_1(\vec x), \dots, g_m(\vec x)$ in $R_{N+k+1}, \dots, R_{N+k+m}$ — the saved input being left unchanged — and then runs $H$ on these values, halting with $f(\vec x)$ in $R_1$ if $h$ converges, and not halting otherwise. If some $g_i(\vec x)$ diverges, the program does not halt, in accordance with the convention that $f(\vec x)\diverge$ in that case.
:::

:::figure[The registers in the proof of :ref{#thm-urm-composition}. The programs $G_i$ and $H$ mention only registers of index at most $N$; the saved input and the values $g_i(\vec x)$ lie above, and are written only by the transfers added around the subroutines.]
<svg class="fig" viewBox="0 0 610 150" width="610" role="img" aria-label="Registers used in the proof: scratch registers, saved input, values of the g_i"><rect x="14" y="40" width="46" height="38" rx="2" class="cell"/><text x="37.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="mrm" font-size="10" dy="4">1</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect x="64" y="40" width="46" height="38" rx="2" class="cell"/><text x="87.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="mrm" font-size="10" dy="4">2</tspan><tspan class="mrm" dy="-4"> </tspan></text><text x="131.0" y="64.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><rect x="152" y="40" width="46" height="38" rx="2" class="cell"/><text x="175.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="math" font-size="10" dy="4">N</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect x="202" y="40" width="62" height="38" rx="2" class="cell"/><text x="233.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="math" font-size="10" dy="4">N</tspan><tspan class="mrm" font-size="10">+1</tspan><tspan class="mrm" dy="-4"> </tspan></text><text x="285.0" y="64.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><rect x="306" y="40" width="62" height="38" rx="2" class="cell"/><text x="337.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="math" font-size="10" dy="4">N</tspan><tspan class="mrm" font-size="10">+</tspan><tspan class="math" font-size="10">k</tspan><tspan class="mrm" dy="-4"> </tspan></text><rect x="372" y="40" width="78" height="38" rx="2" class="cell"/><text x="411.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="math" font-size="10" dy="4">N</tspan><tspan class="mrm" font-size="10">+</tspan><tspan class="math" font-size="10">k</tspan><tspan class="mrm" font-size="10">+1</tspan><tspan class="mrm" dy="-4"> </tspan></text><text x="471.0" y="64.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><rect x="492" y="40" width="82" height="38" rx="2" class="cell"/><text x="533.0" y="64.0" text-anchor="middle" font-size="16"><tspan class="math">R</tspan><tspan class="math" font-size="10" dy="4">N</tspan><tspan class="mrm" font-size="10">+</tspan><tspan class="math" font-size="10">k</tspan><tspan class="mrm" font-size="10">+</tspan><tspan class="math" font-size="10">m</tspan><tspan class="mrm" dy="-4"> </tspan></text><path d="M14,86 L14,92 L198,92 L198,86" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="106.0" y="110" text-anchor="middle" class="label">the only registers that</text><text x="106.0" y="126" text-anchor="middle" font-size="14"><tspan class="math">G</tspan><tspan class="math" font-size="9" dy="4">i</tspan><tspan class="mrm" dy="-4"> </tspan><tspan class="mrm"> and </tspan><tspan class="math">H</tspan><tspan class="mrm"> mention</tspan></text><path d="M202,86 L202,92 L368,92 L368,86" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="285.0" y="110" text-anchor="middle" class="label">saved input</text><text x="285.0" y="126" text-anchor="middle" font-size="14"><tspan class="math">x</tspan><tspan class="mrm" font-size="9" dy="4">1</tspan><tspan class="mrm" dy="-4"> </tspan><tspan class="mrm">, …, </tspan><tspan class="math">x</tspan><tspan class="math" font-size="9" dy="4">k</tspan><tspan class="mrm" dy="-4"> </tspan></text><path d="M372,86 L372,92 L574,92 L574,86" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="473.0" y="110" text-anchor="middle" class="label">values of</text><text x="473.0" y="126" text-anchor="middle" font-size="14"><tspan class="math">g</tspan><tspan class="mrm" font-size="9" dy="4">1</tspan><tspan class="mrm" dy="-4"> </tspan><tspan class="mrm">, …, </tspan><tspan class="math">g</tspan><tspan class="math" font-size="9" dy="4">m</tspan><tspan class="mrm" dy="-4"> </tspan></text><text x="285.0" y="28" text-anchor="middle" class="label">not modified after the first transfers</text></svg>
:::

:::quiz[closure under composition]
Why are the inputs first saved in registers $R_{N+1}, \dots, R_{N+k}$, with $N \geq \rho(G_i)$ for all $i$?

- [x] Running $G_1$ may modify the registers $R_1, \dots, R_{\rho(G_1)}$, including those holding the input; the saved copy is out of reach of every $G_i$, so it is still available to compute $g_2(\vec x), \dots, g_m(\vec x)$.
- [ ] Because URM programs cannot read registers with small indices.

  URM programs can read every register; the issue is that running $G_1$ may overwrite the registers holding the input.
- [ ] To make the program halt when some $g_i(\vec x)$ diverges.

  The program does not halt in that case, whatever the registers used.

---

Suppose $g_1(\vec x)\diverge$ but $h$ is a constant function. What does the program do on $\vec x$?

- [x] It does not halt, and $f(\vec x)\diverge$, in accordance with the convention on composition of partial functions.
- [ ] It halts with the constant value of $h$.

  The program never reaches $H$: it is stuck in the computation of $G_1$.
:::

## Goto programs and assembly languages

The URM is a minimal example of a **goto program**: a numbered list of elementary instructions together with conditional jumps. Processors execute programs of this kind. Other common instruction sets, for instance with a decrement instruction $R_n \leftarrow R_n \dotminus 1$ and a test "if $R_n = 0$ go to $q$", lead to the same class of computable functions. The proof is a **simulation**, the technique of the lesson :ref{to="models-of-computation/multitape-machines"}: each instruction of one set is replaced by a block of instructions of the other, using auxiliary registers that the program does not mention, and jump targets are renumbered. :ref{#ex-urm-no-transfer} below is an instance, :ref{#ex-urm-pred} shows how to decrement without a decrement instruction, and :ref{#ex-urm-decrement-variant} carries out the simulation for the instruction set above.

In the lessons :ref{to="models-of-computation/loop-programs"} and :ref{to="models-of-computation/while-programs"} we consider **structured** programs, with `for` and `while` loops instead of jumps. They are more convenient to write, and the distinction between the two kinds of loops gives a characterization of the primitive recursive functions.

## Exercises

::::exercise{#ex-urm-no-transfer difficulty=2 objective="Eliminate an instruction by simulating it with the others, using an auxiliary register out of reach of the program."}
Consider the variant of the URM without the transfer instruction $T(m, n)$. Show that it computes the same functions.

:::solution
For $m \neq n$, the instruction $T(m, n)$ can be simulated with $Z$, $S$ and $J$ using as a counter a register $R_c$ with $c > \rho(P)$, where $P$ is the program being transformed: $Z(n)$, $Z(c)$, then the loop "if $R_c = R_m$, exit; $S(n)$; $S(c)$; go back", the backward jump being $J(c, c, \cdot)$. The case $m = n$ is a no-op. Replacing each $T$ instruction by such a block, and shifting all jump targets accordingly, gives a program without $T$ whose computations follow those of $P$ on the registers $R_1, \dots, R_{\rho(P)}$. Since $c > \rho(P) \geq 1$, the output register $R_1$ is never used as the counter, so both programs compute the same functions; the initial content of $R_c$, possibly an input, is irrelevant because $R_c$ is zeroed before each use and is not mentioned by $P$.
:::
::::

## Notes and references

Register machines were introduced around 1960 in several variants, by Melzak, Lambek, Minsky, and Shepherdson and Sturgis. The URM and its notation follow Cutland's textbook, which develops the whole of elementary computability theory on this model.

- J. C. Shepherdson, H. E. Sturgis, *Computability of recursive functions*, Journal of the ACM 10 (1963), 217–255.
- M. Minsky, *Computation: Finite and Infinite Machines*, Prentice-Hall, 1967.
- N. Cutland, *Computability: An Introduction to Recursive Function Theory*, Cambridge University Press, 1980.

:::::exercises
::::exercise{#ex-urm-sign difficulty=1 objective="Write a URM program with a test against a register known to contain $0$."}
Write a URM program computing the function $\mathrm{sg}(x)$, equal to $0$ if $x = 0$ and to $1$ otherwise.

:::solution
| | | |
| --- | --- | --- |
| $I_1$ | $J(1, 2, 4)$ | if $x = 0$, halt (output $0$) |
| $I_2$ | $Z(1)$ | |
| $I_3$ | $S(1)$ | output $1$ |
:::
::::

::::exercise{#ex-urm-cases difficulty=2 objective="Implement a definition by cases with a branching program, which evaluates only the case that applies."}
Prove that the URM-computable functions are closed under definition by cases: if $f_1, f_2 : \nat^k \rightharpoonup \nat$ are URM-computable partial functions and $P \subseteq \nat^k$ is a set whose characteristic function is URM-computable, then the partial function $f$ defined by $f(\vec x) \simeq f_1(\vec x)$ if $\vec x \in P$ and $f(\vec x) \simeq f_2(\vec x)$ otherwise is URM-computable.

:::solution
Let $C$, $F_1$, $F_2$ be programs in standard form computing $\chi_P$, $f_1$, $f_2$, and let $N$ be larger than $k$ and than $\rho(C)$, $\rho(F_1)$, $\rho(F_2)$. Write $c = N + k + 1$ and $z = N + k + 2$; these registers initially contain $0$, and $R_z$ is never written. Consider the program
$$
\begin{aligned}
& T(1, N{+}1),\ \dots,\ T(k, N{+}k),\ C[N{+}1, \dots, N{+}k \to c],\ J(c, z, a), \\
& F_1[N{+}1, \dots, N{+}k \to 1],\ J(1, 1, b),\ F_2[N{+}1, \dots, N{+}k \to 1],
\end{aligned}
$$
where $a$ is the index of the first instruction of the block for $F_2$ and $b$ is the length of the program plus one. By :ref{#lem-urm-subroutine} and :ref{#lem-urm-concat}, the block for $C$ halts, since $\chi_P$ is total, with $\chi_P(\vec x)$ in $R_c$ and the saved input unchanged. If $\vec x \notin P$, then $R_c = 0 = R_z$, and the program jumps to the block for $F_2$, which halts if and only if $f_2(\vec x)\converge$, with $f_2(\vec x)$ in $R_1$; the program then halts. If $\vec x \in P$, the jump is not taken, the block for $F_1$ halts if and only if $f_1(\vec x)\converge$, with $f_1(\vec x)$ in $R_1$, and $J(1, 1, b)$ then halts the program. In both cases the program halts exactly when $f(\vec x)\converge$, with output $f(\vec x)$. Only the function of the case that applies is evaluated, so the divergence of the other one is harmless, unlike in the arithmetic definition by cases of the lesson :ref{to="models-of-computation/primitive-recursion"}.
:::
::::

::::exercise{#ex-urm-steps difficulty=1 objective="Count the steps of the addition and multiplication programs from their loop invariants."}
Show that on input $(x, y)$ the addition program halts after $4y + 1$ steps, and the multiplication program after $y(4x + 5) + 2$ steps.

:::solution
*Addition.* Each pass through the loop, from $I_1$ back to $I_1$, executes $I_1, I_2, I_3, I_4$: $4$ steps. By the invariant of the text, there are $y$ passes, and then the jump $I_1$ is taken: $4y + 1$ steps.

*Multiplication.* By the proof of :ref{#prop-urm-mult}, each round $j < y$ of the outer loop executes $I_1$ and $I_2$, then $x$ passes through $I_3, I_4, I_5, I_6$, then $I_3$ (the jump is taken), $I_7$ and $I_8$: $2 + 4x + 3 = 4x + 5$ steps. After $y$ rounds, $I_1$ jumps to $I_9$, and $I_9$ is executed: $2$ more steps. The total is $y(4x + 5) + 2$. For instance, on $(1, 1)$ the program executes $I_1, I_2, I_3, I_4, I_5, I_6, I_3, I_7, I_8, I_1, I_9$: $11$ steps.
:::
::::

::::exercise{#ex-urm-leq difficulty=1 objective="Compare two registers with a counter that increases until it meets one of them."}
Write a URM program computing the characteristic function of $x \leq y$, and prove it correct.

:::solution
A counter $k$ in $R_3$ increases from $0$; the first of $x$, $y$ that it meets decides the answer.

| | | |
| --- | --- | --- |
| $I_1$ | $J(1, 3, 5)$ | if $k = x$, then $x \leq y$ |
| $I_2$ | $J(2, 3, 8)$ | if $k = y$, then $y < x$ |
| $I_3$ | $S(3)$ | |
| $I_4$ | $J(1, 1, 1)$ | |
| $I_5$ | $Z(1)$ | |
| $I_6$ | $S(1)$ | output $1$ |
| $I_7$ | $J(1, 1, 9)$ | halt |
| $I_8$ | $Z(1)$ | output $0$ |

By induction on $k \leq \min(x, y)$, the configuration $(1, r)$ with $r(1) = x$, $r(2) = y$, $r(3) = k$ is reached: for $k < \min(x, y)$ neither jump is taken, and $I_3$ increments the counter. At $k = \min(x, y)$: if $x \leq y$, then $k = x$ and $I_1$ jumps to $I_5$, which leads to output $1$; if $y < x$, then $k = y \neq x$, the first jump is not taken, and $I_2$ jumps to $I_8$, which gives output $0$. The program is in standard form, since its length is $8$ and its jumps go to $I_9$ at most.
:::
::::

::::exercise{#ex-urm-half difficulty=1 objective="Maintain several counters in step to compute a quotient by a register machine."}
Write a URM program computing $x \mapsto \lfloor x / 2 \rfloor$, and prove it correct.

:::solution
Keep $q$ in $R_2$, $2q$ in $R_3$ and $2q + 1$ in $R_4$, and stop when $x$ equals $2q$ or $2q + 1$.

| | | |
| --- | --- | --- |
| $I_1$ | $S(4)$ | $R_2 = 0$, $R_3 = 0$, $R_4 = 1$ |
| $I_2$ | $J(1, 3, 10)$ | if $x = 2q$, output $q$ |
| $I_3$ | $J(1, 4, 10)$ | if $x = 2q + 1$, output $q$ |
| $I_4$ | $S(2)$ | |
| $I_5$ | $S(3)$ | |
| $I_6$ | $S(3)$ | |
| $I_7$ | $S(4)$ | |
| $I_8$ | $S(4)$ | |
| $I_9$ | $J(1, 1, 2)$ | |
| $I_{10}$ | $T(2, 1)$ | |

By induction on $q \leq \lfloor x / 2 \rfloor$, the configuration $(2, r)$ with $r(1) = x$, $r(2) = q$, $r(3) = 2q$, $r(4) = 2q + 1$ is reached. For $q = 0$ this follows from $I_1$. If $q < \lfloor x/2 \rfloor$, then $x \geq 2q + 2$, so neither jump is taken, and $I_4, \dots, I_8$ produce the configuration for $q + 1$. For $q = \lfloor x / 2 \rfloor$, $x \in \{2q, 2q + 1\}$, so one of the jumps leads to $I_{10}$, which copies $q$ into $R_1$; the program halts.
:::
::::

::::exercise{#ex-urm-decrement-variant difficulty=2 objective="Simulate in both directions two instruction sets for register machines."}
Consider register machines with the instructions $S(n)$, $D(n)$: $R_n \leftarrow R_n \dotminus 1$, and $Z?(n, q)$: if $R_n = 0$ the next instruction is $I_q$, otherwise the following one. Programs, configurations and computed functions are defined as for the URM. Show that these machines compute exactly the URM-computable partial functions.

:::solution
In both directions, a program $P$ is translated instruction by instruction into blocks of the other instruction set, using auxiliary registers of index larger than $\rho(P)$ and $k$, which $P$ does not mention; jump targets are renumbered to the first instruction of the block of the target. One of the auxiliary registers, $R_z$, is never written: it contains $0$ throughout, and a test or comparison with it is an unconditional jump. By induction on the number of steps of $P$, the translated program reaches the beginning of the block of $I_i$ with the registers $R_1, \dots, R_{\rho(P)}$ as in the configuration $(i, r)$ of $P$, and the auxiliary registers other than $R_z$ hold values that are reset before use. So both programs halt on the same inputs, with the same value in $R_1$. Below, labels such as $\ell$ name instruction indices inside a block.

*From the new instructions to the URM.* $S(n)$ is kept. $Z?(n, q)$ becomes $J(n, z, q)$. $D(n)$ becomes the predecessor program of :ref{#ex-urm-pred} applied to $R_n$, with counters $R_a$, $R_b$:
$$
J(n, z, \mathrm{end}),\ Z(a),\ Z(b),\ S(b),\ \ell : J(n, b, \ell'),\ S(a),\ S(b),\ J(z, z, \ell),\ \ell' : T(a, n),
$$
where end is the index following the block. If $R_n = v \geq 1$, the loop maintains $R_b = R_a + 1$ and stops when $R_b = v$, so that $T(a, n)$ stores $v - 1$; if $v = 0$, nothing changes.

*From the URM to the new instructions.* $S(n)$ is kept. $Z(n)$ becomes $\ell : Z?(n, \mathrm{end}),\ D(n),\ Z?(z, \ell)$. For $T(m, n)$ with $m \neq n$, first empty $R_n$ as for $Z(n)$, then move $R_m$ into $R_n$ and an auxiliary $R_c$, then move $R_c$ back into $R_m$:
$$
\ell_1 : Z?(m, \ell_2),\ D(m),\ S(n),\ S(c),\ Z?(z, \ell_1),\ \ell_2 : Z?(c, \mathrm{end}),\ D(c),\ S(m),\ Z?(z, \ell_2).
$$
The first loop runs $r(m)$ times and leaves $R_m = 0$, $R_n = R_c = r(m)$; the second restores $R_m$ and leaves $R_c = 0$. ($T(m, m)$ is dropped, its block being empty.) For $J(m, n, q)$, copy $R_m$ into $R_a$ and $R_n$ into $R_b$ as for $T$, then decrement both together:
$$
\ell : Z?(a, \ell'),\ Z?(b, \mathrm{end}),\ D(a),\ D(b),\ Z?(z, \ell),\ \ell' : Z?(b, q),
$$
where $q$ stands for the first instruction of the block of $I_q$, and end for the instruction following the block. After $j$ passes, $R_a = r(m) - j$ and $R_b = r(n) - j$. If $r(m) = r(n)$, both reach $0$ together and the block jumps to $q$; if $r(m) < r(n)$, $R_a$ reaches $0$ first and $Z?(b, q)$ falls through to end; if $r(m) > r(n)$, $R_b$ reaches $0$ first and the block exits to end. This matches $J(m, n, q)$. Jumps beyond the end of $P$ are sent to the index following the translated program.
:::
::::

::::exercise{#ex-urm-primitive-recursion difficulty=2 objective="Program a primitive recursion on a register machine, as a loop around subroutine calls."}
Let $g : \nat^k \rightharpoonup \nat$ and $h : \nat^{k+2} \rightharpoonup \nat$ be URM-computable, with $k \geq 1$, and let $f : \nat^{k+1} \rightharpoonup \nat$ be defined by $f(\vec x, 0) \simeq g(\vec x)$ and $f(\vec x, y + 1) \simeq h(\vec x, y, f(\vec x, y))$; in particular $f(\vec x, y')\diverge$ for all $y' \geq y$ as soon as $f(\vec x, y)\diverge$. Show that $f$ is URM-computable.

:::solution
Let $G$, $H$ be programs in standard form computing $g$, $h$, and let $N$ be larger than $k + 2$, $\rho(G)$ and $\rho(H)$. The input $\vec x, y$ is saved in $R_{N+1}, \dots, R_{N+k+1}$; $R_c$ with $c = N + k + 2$ is a counter and $R_v$ with $v = N + k + 3$ holds the current value. Both initially contain $0$. The program is
$$
\begin{aligned}
& T(1, N{+}1),\ \dots,\ T(k{+}1, N{+}k{+}1),\ G[N{+}1, \dots, N{+}k \to v], \\
& \ell : J(c, N{+}k{+}1, \ell'),\ H[N{+}1, \dots, N{+}k, c, v \to v],\ S(c),\ J(1, 1, \ell), \\
& \ell' : T(v, 1).
\end{aligned}
$$
By :ref{#lem-urm-subroutine}, the calls to $G$ and $H$ leave the registers above $N$ unchanged, except the result register $v$. We show by induction on $j \leq y$: if $f(\vec x, j)\converge$, the program reaches $\ell$ with $R_c = j$ and $R_v = f(\vec x, j)$; and if $f(\vec x, j)\diverge$, it does not halt. For $j = 0$, the call to $G$ halts if and only if $g(\vec x)\converge$, and then stores $f(\vec x, 0)$ in $R_v$. For $j + 1 \leq y$, at $\ell$ we have $R_c = j \neq y$, so the jump is not taken, and the call to $H$ halts if and only if $h(\vec x, j, f(\vec x, j))\converge$, that is $f(\vec x, j + 1)\converge$, with this value in $R_v$; then $R_c$ becomes $j + 1$. At $j = y$, the jump to $\ell'$ is taken and $f(\vec x, y)$ is copied into $R_1$. So the program halts exactly when $f(\vec x, y)\converge$, with output $f(\vec x, y)$. Together with :ref{#thm-urm-composition}, and URM programs for the basic functions, this shows by induction on derivations that every primitive recursive function, defined in the next lesson, is URM-computable.
:::
::::
:::::
