---
title: WHILE programs
summary: Structured programs with unbounded loops. The WHILE-computable functions are the partial recursive functions, a single while loop suffices, and WHILE programs translate into register machines.
duration: 30
prerequisites: [loop-programs]
---

A $\mathtt{WHILE}$ loop repeats its body as long as a condition holds, without a bound fixed on entry. This is exactly what minimization does: search $y = 0, 1, 2, \dots$ until a value is $0$. The lesson proves that the WHILE programs, defined in the lesson :ref{to="models-of-computation/loop-programs"}, compute exactly the partial recursive functions. The proof extends the compilations of the theorem of Meyer and Ritchie (:ref{#thm-loop-pr}) by one case in each direction: minimization becomes a $\mathtt{WHILE}$ loop, and a $\mathtt{WHILE}$ loop becomes a search for its number of iterations. A consequence of Kleene's normal form theorem is that one $\mathtt{WHILE}$ loop suffices in every program. The lesson ends with a translation of WHILE programs into register machines, a step of the equivalence of all the models.

## WHILE programs compute the partial recursive functions

:::theorem{#thm-while-partial-recursive}
A partial function is WHILE-computable if and only if it is partial recursive.
:::

:::proof{of=thm-while-partial-recursive}
**Partial recursive ⇒ WHILE.** We extend the first part of the proof of :ref{#thm-loop-pr}. The constructions for composition and primitive recursion are unchanged; with partial functions, the program simply does not terminate when one of the subprograms does not, which matches the conventions for partial functions. For minimization, $f(\vec x) \simeq \mu y\, [g(\vec x, y) = 0]$, with fresh $Y$ and $T$:
$$
\begin{aligned}
& Y \mathbin{:=} 0 ;\ T \mathbin{:=} g(\vec X, Y) ; \\
& \mathtt{WHILE}\ T \neq 0\ \mathtt{DO} \\
& \qquad Y \mathbin{:=} Y + 1 ;\ T \mathbin{:=} g(\vec X, Y) \\
& \mathtt{END} ;\ X_o \mathbin{:=} Y.
\end{aligned}
$$
This program evaluates $g(\vec x, 0), g(\vec x, 1), \dots$ in order and stops at the first zero; it does not terminate if one of these computations does not, or if there is no zero. This is exactly the definition of minimization.

**WHILE ⇒ partial recursive.** As in the LOOP case, define for each subprogram $Q$ the partial function $F_Q$ on codes of states, and show by induction that it is partial recursive. Assignments, sequences and $\mathtt{LOOP}$ instructions are handled as before, now with partial functions (the iteration $G$ is defined by primitive recursion for partial functions). For $W = \mathtt{WHILE}\ X_i \neq 0\ \mathtt{DO}\ Q\ \mathtt{END}$, let $G(s, 0) \simeq s$ and $G(s, n + 1) \simeq F_Q(G(s, n))$. Then
$$
F_W(s) \simeq G\big(s,\ \mu n\, [\,(G(s, n))'_i = 0\,]\big).
$$
By the definition of minimization, the search succeeds at $n$ exactly when $G(s, m)$ is defined with $X_i \neq 0$ for $m < n$, and $G(s, n)$ is defined with $X_i = 0$: this matches the semantics of the $\mathtt{WHILE}$ instruction.
:::

:::quiz[WHILE and minimization]
In the program for minimization, why does the clause "$g(\vec x, z)$ defined for all $z < y$" in the definition of $\mu$ match the behavior of the program?

- [x] The program computes $g(\vec x, 0), g(\vec x, 1), \dots$ in order. If some $g(\vec x, z)$ diverges before a zero is found, the program never terminates, even if $g(\vec x, y) = 0$ for some larger $y$; the definition of $\mu$ makes $f(\vec x)$ undefined in exactly this case.
- [ ] Because WHILE programs are total.

  WHILE programs may not terminate.
- [ ] It does not fit; the proof uses a modified minimization.

  The proof uses exactly the minimization operator of :ref{#def-mu}.

---

Which instruction is responsible for the possibility of non-termination of WHILE programs?

- [x] $\mathtt{WHILE}$: the number of iterations is not fixed in advance.
- [ ] $\mathtt{LOOP}$, when the loop variable is modified in the body.

  The number of iterations of a $\mathtt{LOOP}$ is fixed on entry.
- [ ] Sequential composition.

  A sequential composition of terminating programs terminates; only unbounded iteration can run forever.
:::

:::corollary{#cor-one-while}
Every WHILE program is equivalent, for the computation of functions, to a WHILE program containing a single $\mathtt{WHILE}$ instruction.
:::

:::proof{of=cor-one-while}
The function computed by the program is partial recursive. By Kleene's normal form (:ref{#thm-kleene-normal-form}, proved in the lesson :ref{to="models-of-computation/equivalence-of-models"} without using this corollary), it can be written $U(\mu s\, T_k(e, \vec x, s))$ with $U$ and $T_k$ primitive recursive. By :ref{#thm-loop-pr}, $U$ and $\chi_{T_k}$ are computed by LOOP programs, and the construction above for the minimization uses one $\mathtt{WHILE}$ instruction.
:::

This is related to the **Böhm–Jacopini theorem** (1966): every flow diagram can be rewritten using only sequencing, conditionals and while loops, at the cost of auxiliary variables. The form in which a single while loop suffices is the "folk" version of this theorem discussed by Harel (1980).

## WHILE programs and register machines

The translation into register machines introduces jumps; :ref{#ex-while-urm} goes in the other direction and eliminates them. A $\mathtt{WHILE}$ loop becomes a test at the top and a jump back at the bottom; a $\mathtt{LOOP}$ instruction needs two extra registers, one to keep the number of iterations fixed on entry and one to count them.

:::figure[The register machine program $(\mathtt{LOOP}\ X_i\ \mathtt{DO}\ Q\ \mathtt{END})^*$, where $t$ is the length of $Q^*$. The register $R_a$ keeps the number of iterations fixed on entry, $R_b$ counts the iterations performed, and $R_1 = 0$ serves for the unconditional jump back to the test.]
<svg class="fig" viewBox="0 0 540 300" width="540" role="img" aria-label="Layout of the register machine program for a LOOP instruction"><defs><marker id="ah-loopurm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect class="cell" x="80" y="18" width="200" height="32" rx="3"/><text x="90" y="39" class="mrm muted" font-size="13">1</text><text x="268" y="39" text-anchor="end" class="mrm" font-size="14">T(i+2, a)</text><text x="342" y="39" class="label">save the number of iterations</text><rect class="cell" x="80" y="58" width="200" height="32" rx="3"/><text x="90" y="79" class="mrm muted" font-size="13">2</text><text x="268" y="79" text-anchor="end" class="mrm" font-size="14">Z(b)</text><text x="342" y="79" class="label">reset the counter</text><rect class="cell" x="80" y="98" width="200" height="32" rx="3"/><text x="90" y="119" class="mrm muted" font-size="13">3</text><text x="268" y="119" text-anchor="end" class="mrm" font-size="14">J(a, b, t+6)</text><text x="342" y="119" class="label">exit when the counter reaches it</text><rect class="cell head-cell" x="80" y="138" width="200" height="32" rx="3"/><text x="90" y="159" class="mrm muted" font-size="13">4 … t+3</text><text x="268" y="159" text-anchor="end" class="mrm" font-size="14">Q* shifted by 3</text><text x="342" y="159" class="label">body</text><rect class="cell" x="80" y="178" width="200" height="32" rx="3"/><text x="90" y="199" class="mrm muted" font-size="13">t+4</text><text x="268" y="199" text-anchor="end" class="mrm" font-size="14">S(b)</text><text x="342" y="199" class="label">count one iteration</text><rect class="cell" x="80" y="218" width="200" height="32" rx="3"/><text x="90" y="239" class="mrm muted" font-size="13">t+5</text><text x="268" y="239" text-anchor="end" class="mrm" font-size="14">J(1, 1, 3)</text><text x="342" y="239" class="label">back to the test</text><rect class="cell" x="80" y="258" width="200" height="32" rx="3" stroke-dasharray="4 3"/><text x="90" y="279" class="mrm muted" font-size="13">t+6</text><text x="342" y="279" class="label">next instruction</text><path d="M280,114.0 C330,114.0 330,274.0 284,274.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-loopurm)"/><path d="M80,234.0 C20,234.0 20,114.0 76,114.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-loopurm)"/></svg>
:::

:::proposition{#prop-while-urm}
Every WHILE-computable partial function is URM-computable.
:::

:::proof{of=prop-while-urm}
Let $P$ compute $f : \nat^k \rightharpoonup \nat$, and let $m$ be larger than $k$ and than the indices of all variables of $P$. The variable $X_i$, for $i < m$, is represented by the register $R_{i+2}$; the register $R_1$ is kept equal to $0$ and serves for unconditional jumps $J(1, 1, q)$ and for tests against $0$. Each occurrence of a $\mathtt{LOOP}$ instruction in $P$ receives two registers $R_a, R_b$ of its own, with indices larger than $m + 1$. For each subprogram $Q$ of $P$ we define a URM program $Q^*$ in standard form, by induction on $Q$; let $t$ denote the length of the translation of the body.

- $(X_i \mathbin{:=} 0)^* = Z(i+2)$, $(X_i \mathbin{:=} X_i + 1)^* = S(i+2)$, $(X_i \mathbin{:=} X_j)^* = T(j+2, i+2)$.
- $(Q ; Q')^*$ is the concatenation $Q^* Q'^*$ of :ref{#def-urm-concat}.
- $(\mathtt{WHILE}\ X_i \neq 0\ \mathtt{DO}\ Q\ \mathtt{END})^*$ is $J(i+2, 1, t+3)$, followed by $Q^*$ with all jump targets increased by $1$, followed by $J(1, 1, 1)$.
- $(\mathtt{LOOP}\ X_i\ \mathtt{DO}\ Q\ \mathtt{END})^*$, with the registers $R_a, R_b$ of this occurrence, is $T(i+2, a)$, $Z(b)$, $J(a, b, t+6)$, followed by $Q^*$ with all jump targets increased by $3$, followed by $S(b)$, $J(1, 1, 3)$.

In each case the jump targets are at most the length plus one, so $Q^*$ is in standard form. We show by induction on $Q$: if $Q^*$ is started at its first instruction in a register state $r$ with $r(1) = 0$ and $r(i+2) = \sigma(i)$ for all $i < m$, then $Q^*$ halts if and only if $[\![Q]\!](\sigma)\converge$, and in that case it halts in a state $r'$ with $r'(1) = 0$ and $r'(i+2) = [\![Q]\!](\sigma)(i)$ for all $i < m$. Assignments are immediate, and sequences follow from :ref{#lem-urm-concat}. For a $\mathtt{WHILE}$ instruction, by induction on $n$, the program reaches its first instruction for the $(n+1)$-th time if and only if $[\![Q]\!]^n(\sigma)\converge$ and $[\![Q]\!]^j(\sigma)(i) \neq 0$ for all $j < n$, and then the registers represent $[\![Q]\!]^n(\sigma)$; since $R_1 = 0$, the first jump exits exactly when the represented value of $X_i$ is $0$, as in :ref{#def-loop-while-semantics}. For a $\mathtt{LOOP}$ instruction, $R_a$ holds the value of $X_i$ on entry and is not modified by $Q^*$, which only uses the registers of the occurrences inside $Q$; by induction on $j$, the test $J(a, b, \cdot)$ is reached for the $(j+1)$-th time with $R_b = j$ and the registers representing $[\![Q]\!]^j(\sigma)$, so the program exits after $\sigma(i)$ iterations.

The program for $f$ consists of $T(k, k+2), T(k-1, k+1), \dots, T(1, 3)$, which move the input to the registers of $X_1, \dots, X_k$ (in decreasing order, so that no input is overwritten before it is copied), then $Z(1)$, $Z(2)$, then $P^*$, then $T(2, 1)$. After the first part, $R_1 = 0$ and $R_{i+2}$ holds $\sigma_{\vec x}(i)$ for every $i < m$, and the registers of the $\mathtt{LOOP}$ occurrences hold $0$ (they are not used before being set anyway). By the claim, the program halts if and only if $f(\vec x)\converge$, and then $R_1$ contains $[\![P]\!](\sigma_{\vec x})(0) = f(\vec x)$.
:::

## Exercises

::::exercise{#ex-while-urm difficulty=2 objective="Eliminate jumps by simulating a register machine with a single while loop over a program counter."}
Show directly, without using partial recursive functions, that every URM-computable partial function is WHILE-computable, by a WHILE program with a single $\mathtt{WHILE}$ instruction. (The converse is :ref{#prop-while-urm}.)

:::solution
Let $I_1, \dots, I_s$ compute $f : \nat^k \rightharpoonup \nat$, and let $\rho$ be the largest of $k$ and the register indices of the program. Represent $R_n$ by $X_n$ for $1 \leq n \leq \rho$, and use fresh variables $\mathrm{PC}$ (the index of the next instruction) and $H$. The program is: $\mathrm{PC} \mathbin{:=} 1$; $H \mathbin{:=} \chi_{\leq}(\mathrm{PC}, s)$; $\mathtt{WHILE}\ H \neq 0\ \mathtt{DO}\ B\ \mathtt{END}$; $X_0 \mathbin{:=} X_1$. The body $B$ executes the instruction of index $\mathrm{PC}$ and updates $\mathrm{PC}$: it first copies $\mathrm{PC}$ into a fresh variable $\mathrm{PC}'$, then performs a sequence of $s$ conditionals "if $\mathrm{PC}' = j$ then execute $I_j$", where $Z(n)$, $S(n)$, $T(m, n)$ become $X_n \mathbin{:=} 0$, $X_n \mathbin{:=} X_n + 1$, $X_n \mathbin{:=} X_m$ followed by $\mathrm{PC} \mathbin{:=} \mathrm{PC} + 1$, and $J(m, n, q)$ sets $\mathrm{PC}$ to $q$ if $X_m = X_n$ and to $j + 1$ otherwise. Since the conditionals test $\mathrm{PC}'$, which is not modified, exactly one of them applies in each pass (when $H \neq 0$, $1 \leq \mathrm{PC} \leq s$). At the end of $B$, $H \mathbin{:=} \chi_{\leq}(\mathrm{PC}, s)$. Equality tests, $\chi_\leq$ and the conditionals are LOOP-definable, by :ref{#thm-loop-pr} and the conditional of the section on programming in LOOP in the lesson :ref{to="models-of-computation/loop-programs"}. By induction on the number of steps, after $n$ passes through $B$ the variables $\mathrm{PC}, X_1, \dots, X_\rho$ hold the configuration of the URM after $n$ steps, so the loop terminates exactly when the URM halts, with $f(\vec x)$ in $X_1$.
:::
::::

## Notes and references

WHILE programs, as an extension of LOOP programs, are from Meyer and Ritchie. That structured programs with `for` and `while` loops compute all partial recursive functions, and those without `while` loops the primitive recursive ones, is credited by Monin and Patey to Wang (1957), Péter (1958) and Ershov (1958); their chapter "Church–Turing thesis" proves it with programs on registers, as in this lesson and the previous one. The elimination of jumps in favor of structured control flow is the subject of the Böhm–Jacopini theorem; Harel discusses its folk versions and their history.

- A. R. Meyer, D. M. Ritchie, *The complexity of loop programs*, Proceedings of the 22nd ACM National Conference (1967), 465–469.
- C. Böhm, G. Jacopini, *Flow diagrams, Turing machines and languages with only two formation rules*, Communications of the ACM 9 (1966), 366–371.
- D. Harel, *On folk theorems*, Communications of the ACM 23 (1980), 379–389.
- H. Wang, *A variant to Turing's theory of computing machines*, Journal of the ACM 4 (1957), 63–92.
- R. Péter, *Graphschemata und rekursive Funktionen*, Dialectica 12 (1958), 373–393.
- B. Monin, L. Patey, *Computability theory*, chapter "Church–Turing thesis", section on recursive functions.

:::::exercises
::::exercise{#ex-while-trace difficulty=1 objective="Determine the partial functions computed by WHILE programs, including a program that diverges on some inputs."}
Using the abbreviations of the lesson :ref{to="models-of-computation/loop-programs"} and the conditional of :ref{#ex-loop-if-else}, determine the unary partial functions computed by
$$
P:\ X_0 \mathbin{:=} 0 ;\ \mathtt{WHILE}\ X_1 \neq 0\ \mathtt{DO}\ X_1 \mathbin{:=} X_1 \dotminus 1 ;\ X_1 \mathbin{:=} X_1 \dotminus 1 ;\ X_0 \mathbin{:=} X_0 + 1\ \mathtt{END}
$$
and by the program $Q$ obtained from $P$ by replacing the first two instructions of the body by
$$
D \mathbin{:=} X_1 \dotminus 1 ;\ \mathtt{IF}\ D = 0\ \mathtt{THEN}\ X_1 \mathbin{:=} X_1 + 1 ;\ X_1 \mathbin{:=} X_1 + 1\ \mathtt{ELSE}\ X_1 \mathbin{:=} X_1 \dotminus 1 ;\ X_1 \mathbin{:=} X_1 \dotminus 1\ \mathtt{END}.
$$

:::solution
In $P$, each iteration decreases $X_1$ by $2$ (or to $0$ if $X_1 = 1$) and increases $X_0$ by $1$. Starting from $X_1 = x$, the loop stops after $\lceil x / 2 \rceil$ iterations: $P$ computes $x \mapsto \lceil x/2 \rceil$, a total function.

In $Q$, the body is executed only when $X_1 \neq 0$, so $D = 0$ means $X_1 = 1$. An iteration therefore replaces $X_1 = 1$ by $3$, and $X_1 \geq 2$ by $X_1 - 2$; it preserves the parity of $X_1$. If $x$ is even, $X_1$ takes the values $x, x - 2, \dots, 0$ and the loop stops after $x/2$ iterations, with $X_0 = x/2$. If $x$ is odd, $X_1$ is never $0$: it decreases to $1$, then alternates between $3$ and $1$, and the loop runs forever. So $Q$ computes the partial function $x \mapsto x/2$, defined exactly on the even numbers.
:::
::::

::::exercise{#ex-while-unfolding difficulty=2 objective="Characterize the semantics of a WHILE loop as the least solution of its unfolding equation."}
Let $W = \mathtt{WHILE}\ X_i \neq 0\ \mathtt{DO}\ P\ \mathtt{END}$.

1. Show that for every state $\sigma$, $[\![W]\!](\sigma) \simeq \sigma$ if $\sigma(i) = 0$, and $[\![W]\!](\sigma) \simeq [\![W]\!]([\![P]\!](\sigma))$ otherwise.
2. Call a partial function $F$ from states to states a **solution** if it satisfies the equations of 1 in place of $[\![W]\!]$. Show that every solution $F$ extends $[\![W]\!]$: if $[\![W]\!](\sigma)\converge$ then $F(\sigma) \simeq [\![W]\!](\sigma)$.
3. Give a program $P$ for which some solution differs from $[\![W]\!]$.

:::solution
1. If $\sigma(i) = 0$, then $n = 0$ is the least $n$ of :ref{#def-loop-while-semantics} (the condition on $m < n$ is empty), so $[\![W]\!](\sigma) = \sigma$. Let $\sigma(i) \neq 0$; then $n = 0$ does not qualify. If $[\![P]\!](\sigma)\diverge$, then $[\![P]\!]^m(\sigma)\diverge$ for every $m \geq 1$, no $n$ qualifies, and both sides are undefined. Otherwise let $\sigma' = [\![P]\!](\sigma)$. For $n \geq 1$, $[\![P]\!]^n(\sigma) \simeq [\![P]\!]^{n-1}(\sigma')$, and the conditions "$[\![P]\!]^m(\sigma)\converge$ with value $\neq 0$ at $i$ for all $m < n$" amount to $\sigma(i) \neq 0$ together with the same conditions for $\sigma'$ and $m < n - 1$. So $n$ qualifies for $\sigma$ if and only if $n - 1$ qualifies for $\sigma'$, and the least ones correspond: $[\![W]\!](\sigma) \simeq [\![W]\!](\sigma')$.
2. Suppose $[\![W]\!](\sigma)\converge$, with $n$ iterations. We show $F(\sigma) = [\![W]\!](\sigma)$ by induction on $n$. If $n = 0$, $\sigma(i) = 0$ and $F(\sigma) = \sigma = [\![W]\!](\sigma)$. If $n \geq 1$, then $\sigma(i) \neq 0$, $\sigma' = [\![P]\!](\sigma)$ is defined, and by the proof of 1, $[\![W]\!](\sigma') = [\![W]\!](\sigma)$ with $n - 1$ iterations. By the equation for $F$ and the induction hypothesis, $F(\sigma) \simeq F(\sigma') = [\![W]\!](\sigma)$.
3. Take $i = 1$ and $P = X_2 \mathbin{:=} X_2$, which does not change the state. Then $[\![W]\!](\sigma) = \sigma$ if $\sigma(1) = 0$, and $[\![W]\!](\sigma)\diverge$ otherwise. The identity function $F(\sigma) = \sigma$ is also a solution: when $\sigma(1) \neq 0$, $F([\![P]\!](\sigma)) = F(\sigma) = \sigma$. So the equation alone does not determine the semantics; $[\![W]\!]$ is its least solution. This description of loops as least fixed points is the starting point of denotational semantics.
:::
::::

::::exercise{#ex-while-ackermann difficulty=2 lessons="ackermann-function" objective="Implement the stack algorithm for the Ackermann function as a WHILE program with one loop."}
Write a WHILE program with a single $\mathtt{WHILE}$ instruction which computes the Ackermann function, using the stack algorithm of the lesson :ref{to="models-of-computation/ackermann-function"} and sequence codes. Why can no LOOP program compute it?

:::solution
Let $\mathrm{Step}(s)$ be the following function on sequence codes: with $n = \mathrm{lh}(s)$, $a = (s)'_{n-2}$, $b = (s)'_{n-1}$ and $r = s \upharpoonright (n - 2)$,
$$
\mathrm{Step}(s) = \begin{cases} r * [b + 1] & \text{if } a = 0, \\ r * [a - 1, 1] & \text{if } a > 0,\ b = 0, \\ r * [a - 1, a, b - 1] & \text{if } a > 0,\ b > 0. \end{cases}
$$
It is primitive recursive, by :ref{#prop-seq-operations} and definition by cases; on codes of stacks with at least two elements it performs one step of the stack algorithm. By :ref{#thm-loop-pr}, each assignment $V \mathbin{:=} g(\vec U)$ with $g$ primitive recursive is a LOOP program. The program is
$$
\begin{aligned}
& S \mathbin{:=} [X_1, X_2] ;\ L \mathbin{:=} \mathrm{lh}(S) \dotminus 1 ; \\
& \mathtt{WHILE}\ L \neq 0\ \mathtt{DO}\ S \mathbin{:=} \mathrm{Step}(S) ;\ L \mathbin{:=} \mathrm{lh}(S) \dotminus 1\ \mathtt{END} ; \\
& X_0 \mathbin{:=} (S)'_0 .
\end{aligned}
$$
By induction on the number of iterations, $S$ codes the stack after that many steps of the algorithm, and $L = 0$ exactly when the stack has one element. The lesson on the Ackermann function shows that from $[x, y]$ the algorithm reaches the stack $[A(x, y)]$ after finitely many steps, and continues while the stack has at least two elements. So the loop terminates with $S = [A(x, y)]$, and the program outputs $A(x, y)$. No LOOP program computes $A$: by :ref{#thm-loop-pr} it would be primitive recursive, contradicting :ref{#cor-ack-not-pr}.
:::
::::

::::exercise{#ex-while-bounded-pr difficulty=3 objective="Replace while loops by bounded loops when the number of iterations is bounded by a primitive recursive function."}
For a WHILE program $P$ and a state $\sigma$ with $[\![P]\!](\sigma)\converge$, let $\mathrm{it}_P(\sigma)$ be the total number of iterations of $\mathtt{WHILE}$ loops executed: $0$ for an assignment, $\mathrm{it}_Q(\sigma) + \mathrm{it}_R([\![Q]\!](\sigma))$ for $Q ; R$, the sum of the values of $\mathrm{it}_Q$ over the successive iterations for $\mathtt{LOOP}\ X_i\ \mathtt{DO}\ Q\ \mathtt{END}$, and the number $n$ of iterations plus the sum of the values of $\mathrm{it}_Q$ over them for $\mathtt{WHILE}\ X_i \neq 0\ \mathtt{DO}\ Q\ \mathtt{END}$. Suppose that $P$ computes a total function $f : \nat^k \to \nat$, and that there is a primitive recursive $b$ with $\mathrm{it}_P(\sigma_{\vec x}) \leq b(\vec x)$ for all $\vec x$. Show that $f$ is primitive recursive.

:::solution
Let $B$ be a variable not occurring in $P$. For a subprogram $Q$ of $P$, let $Q^B$ be obtained by replacing, from the innermost loops outwards, each $\mathtt{WHILE}\ X_i \neq 0\ \mathtt{DO}\ R\ \mathtt{END}$ by $\mathtt{LOOP}\ B\ \mathtt{DO}\ \mathtt{IF}\ X_i \neq 0\ \mathtt{THEN}\ R^B\ \mathtt{END}\ \mathtt{END}$, with the conditional of the lesson :ref{to="models-of-computation/loop-programs"} (each occurrence with its own fresh variable). $Q^B$ is a LOOP program, and $B$ is not modified by it.

*Claim.* If $[\![Q]\!](\sigma)\converge$ and $\mathrm{it}_Q(\sigma) \leq \sigma(B)$, then $[\![Q^B]\!](\sigma)$ agrees with $[\![Q]\!](\sigma)$ on the variables of $P$. By induction on $Q$. Assignments are unchanged. For $Q ; R$, both $\mathrm{it}_Q(\sigma)$ and $\mathrm{it}_R([\![Q]\!](\sigma))$ are at most $\sigma(B)$, and $B$ is not modified, so the induction hypothesis applies to both parts. For a $\mathtt{LOOP}$ instruction, the same argument applies to each iteration, by induction on the iterations. For $W = \mathtt{WHILE}\ X_i \neq 0\ \mathtt{DO}\ R\ \mathtt{END}$ with $n$ iterations, $n \leq \mathrm{it}_W(\sigma) \leq \sigma(B)$, and the value of $\mathrm{it}_R$ at each iteration is at most $\sigma(B)$. The replacement executes $\sigma(B) \geq n$ guarded iterations. During the first $n$, $X_i \neq 0$ at the start, so the body $R^B$ runs, and by the induction hypothesis it acts as $R$; after them, the state agrees with $[\![W]\!](\sigma)$, where $X_i = 0$. The remaining iterations then do nothing, since the guard fails and the body does not run. This proves the claim.

Now let $P^\ast$ be the LOOP program $B \mathbin{:=} b(X_1, \dots, X_k) ;\ P^B$, where the first part is given by the direction "primitive recursive ⇒ LOOP" of :ref{#thm-loop-pr}, with auxiliary variables not occurring in $P^B$. From $\sigma_{\vec x}$, the first part sets $B$ to $b(\vec x)$ and leaves the variables of $P$ unchanged. Since $\mathrm{it}_P(\sigma_{\vec x}) \leq b(\vec x)$, the claim gives $[\![P^\ast]\!](\sigma_{\vec x})(0) = [\![P]\!](\sigma_{\vec x})(0) = f(\vec x)$. So $f$ is LOOP-computable, hence primitive recursive by :ref{#thm-loop-pr}.
:::
::::
:::::
