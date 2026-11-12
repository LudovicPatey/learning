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

The translation into register machines introduces jumps; the last exercise of this lesson goes in the other direction and eliminates them. A $\mathtt{WHILE}$ loop becomes a test at the top and a jump back at the bottom; a $\mathtt{LOOP}$ instruction needs two extra registers, one to keep the number of iterations fixed on entry and one to count them.

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

::::exercise{difficulty=2}
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

