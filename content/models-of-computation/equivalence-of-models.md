---
title: Turing machines and partial recursive functions
summary: Arithmetization of Turing machines, so that every Turing-computable function is partial recursive; Kleene's normal form theorem; every partial recursive function is Turing-computable, by closure of multi-tape machines under composition, primitive recursion and minimization; the universal partial computable function.
duration: 40
prerequisites: [mu-recursion, multitape-machines]
---

We have met two definitions of computable partial function: the functions computed by Turing machines, defined by a machine model, and the partial recursive functions, defined by closure under three schemes. This lesson proves that they coincide. One direction **arithmetizes** Turing machines: configurations are coded by integers, so that one step of a machine is a primitive recursive function, and the only non-primitive recursive part of a computation is the search for the number of steps. This gives Kleene's normal form theorem, and through it the universal function on which the course :ref{to="fundamentals/programs-as-numbers"} is built. The other direction is a **simulation**: each scheme is implemented by a machine that runs other machines as subroutines on separate tapes.

:::theorem{#thm-tm-pr}
A partial function $f : \nat^k \rightharpoonup \nat$ is Turing-computable if and only if it is partial recursive.
:::

Other models, such as register machines, WHILE programs and the λ-calculus, compute the same functions; the specialized course :ref{to="other-models/all-models"} proves it.

## Arithmetization of Turing machines

Fix a Turing machine $M$. Without loss of generality its states are $0, 1, \dots, m$ with initial state $0$ and halting state $1$, and its alphabet is $\{0, 1, \dots, a\}$, where $0$ stands for the blank $\sqcup$ and $1$ for the symbol $1$. We use the sequence coding $[\ldots]$ of the lesson :ref{to="models-of-computation/coding-sequences"}, with the primitive recursive operations $\mathrm{lh}$, $(s)'_i$, concatenation $*$, and

- $\mathrm{cons}(b, s) = [b] * s$, which adds $b$ in front of $s$;
- $\mathrm{hd}(s) = (s)'_0$ if $\mathrm{lh}(s) > 0$, and $0$ otherwise;
- $\mathrm{tl}(s) = [(s)'_1, \dots, (s)'_{\mathrm{lh}(s) - 1}]$ if $\mathrm{lh}(s) > 0$, and $[\,]$ otherwise.

These are primitive recursive; for instance $\mathrm{tl}(s) = \prod_{i + 1 < \mathrm{lh}(s)} p_i^{(s)_{i+1}}$.

**Coding configurations.** A configuration $(q, \tau, h)$ is coded by a triple $\langle q, \ell, r \rangle$ where $r$ is the code of the sequence $\tau(h), \tau(h+1), \dots, \tau(h + j)$ and $\ell$ is the code of $\tau(h-1), \tau(h-2), \dots, \tau(h - i)$, for some $i, j$ large enough that all non-blank cells are covered. The left part is stored **in reverse order**, so that the cells adjacent to the head are at the front of both sequences.

:::figure[A configuration with the head on the cell containing $d$, coded by the sequences $\ell$ and $r$. Both sequences are read from the head outwards, so a move of the head only changes their first entries.]
<svg class="fig" viewBox="0 0 520 190" width="520" role="img" aria-label="A tape split at the head into a reversed left part and a right part"><defs><marker id="ah-conf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="46" y="69" class="mrm muted" font-size="18">⋯</text><rect class="cell" x="70" y="40" width="46" height="46" rx="3"/><text x="93.0" y="69" text-anchor="middle" class="math muted" font-size="18">⊔</text><rect class="cell" x="116" y="40" width="46" height="46" rx="3"/><text x="139.0" y="69" text-anchor="middle" class="math" font-size="18">a</text><rect class="cell" x="162" y="40" width="46" height="46" rx="3"/><text x="185.0" y="69" text-anchor="middle" class="math" font-size="18">b</text><rect class="cell" x="208" y="40" width="46" height="46" rx="3"/><text x="231.0" y="69" text-anchor="middle" class="math" font-size="18">c</text><rect class="cell head-cell" x="254" y="40" width="46" height="46" rx="3"/><text x="277.0" y="69" text-anchor="middle" class="math" font-size="18">d</text><rect class="cell" x="300" y="40" width="46" height="46" rx="3"/><text x="323.0" y="69" text-anchor="middle" class="math" font-size="18">e</text><rect class="cell" x="346" y="40" width="46" height="46" rx="3"/><text x="369.0" y="69" text-anchor="middle" class="math" font-size="18">f</text><rect class="cell" x="392" y="40" width="46" height="46" rx="3"/><text x="415.0" y="69" text-anchor="middle" class="math muted" font-size="18">⊔</text><text x="446" y="69" class="mrm muted" font-size="18">⋯</text><path d="M269.0,20 L285.0,20 L277.0,34 z" class="accent-fill"/><text x="277.0" y="14" text-anchor="middle" class="label">head</text><line x1="250.0" y1="116.0" x2="122.0" y2="116.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-conf)"/><text x="185.0" y="146" text-anchor="middle" class="math" font-size="17">ℓ <tspan class="mrm">= [</tspan>c<tspan class="mrm">, </tspan>b<tspan class="mrm">, </tspan>a<tspan class="mrm">]</tspan></text><line x1="258.0" y1="116.0" x2="386.0" y2="116.0" class="accent-stroke" stroke-width="1.4" marker-end="url(#ah-conf)"/><text x="323.0" y="146" text-anchor="middle" class="math" font-size="17">r <tspan class="mrm">= [</tspan>d<tspan class="mrm">, </tspan>e<tspan class="mrm">, </tspan>f<tspan class="mrm">]</tspan></text></svg>
:::

Several codes represent the same configuration, differing by trailing blanks; this causes no problem, since all functions below treat a missing cell as a blank, via $\mathrm{hd}$.

:::quiz[coding configurations]
Why is the left part of the tape stored in reverse order?

- [x] So that a move of the head only modifies the fronts of the two sequences: moving right transfers the front of $r$ to the front of $\ell$, and moving left does the converse. Both are expressed with $\mathrm{cons}$, $\mathrm{hd}$ and $\mathrm{tl}$.
- [ ] Because sequence codes can only be read backwards.

  Every entry of a sequence code is accessible by a primitive recursive projection; the order is chosen so that a move changes only the first entries.
- [ ] To make the coding injective.

  The coding is not injective anyway, because of trailing blanks.
:::

**One step.** Define $\mathrm{Next}(c)$ for $c = \langle q, \ell, r \rangle$ as follows. If $q = 1$ (halting), $\mathrm{Next}(c) = c$. Otherwise let $b = \mathrm{hd}(r)$ be the scanned symbol and $\delta(q, b) = (q', b', D)$. Then
$$
\mathrm{Next}(c) = \begin{cases} \langle q',\ \mathrm{cons}(b', \ell),\ \mathrm{tl}(r) \rangle & \text{if } D = R, \\ \langle q',\ \mathrm{tl}(\ell),\ \mathrm{cons}(\mathrm{hd}(\ell),\ \mathrm{cons}(b', \mathrm{tl}(r))) \rangle & \text{if } D = L. \end{cases}
$$
This is a definition by cases over the finitely many pairs $(q, b)$, plus one case for symbols $b$ out of range. Hence $\mathrm{Next}$ is primitive recursive.

**Iteration.** Let $\mathrm{Init}(\vec x) = \langle 0, [\,], w_{\vec x} \rangle$, where $w_{\vec x}$ is the code of the word $1^{x_1 + 1}\, 0\, 1^{x_2 + 1}\, 0 \cdots 0\, 1^{x_k + 1}$; it is primitive recursive (for instance as a concatenation of codes of constant sequences, computed by bounded products). Define by primitive recursion
$$
\begin{gathered}
\mathrm{Conf}(\vec x, 0) = \mathrm{Init}(\vec x), \\
\mathrm{Conf}(\vec x, t + 1) = \mathrm{Next}(\mathrm{Conf}(\vec x, t)).
\end{gathered}
$$
Then $\mathrm{Conf}(\vec x, t)$ codes the configuration after $t$ steps if $M$ has not halted before step $t$, and the halting configuration otherwise — this is why $\mathrm{Next}$ fixes halting configurations.

**Halting and output.** The predicates $\mathrm{Halt}(c) \iff \pi_0(c) = 1$ (where $\pi_0$ extracts the state from the triple) and $\mathrm{Std}(c)$: "every entry of $\ell$ is $0$, and $r$ consists of $y + 1$ entries equal to $1$ followed only by $0$s, for some $y$" are primitive recursive, by bounded quantification over the indices of $\ell$ and $r$. The output $\mathrm{Out}(c)$, the number of leading $1$s of $r$ minus one, is primitive recursive by bounded minimization.

:::proposition{#prop-tm-partial-recursive}
Every Turing-computable partial function is partial recursive.
:::

:::proof{of=prop-tm-partial-recursive}
Let $M$ compute $f$. Let $t_0(\vec x) \simeq \mu t\, \mathrm{Halt}(\mathrm{Conf}(\vec x, t))$ and $c(\vec x) \simeq \mathrm{Conf}(\vec x, t_0(\vec x))$, the final configuration. Then
$$
f(\vec x) \simeq \mathrm{Out}(c(\vec x)) + 0 \cdot \mu z\, [\chi_{\mathrm{Std}}(c(\vec x)) = 1].
$$
If $M$ does not halt, $t_0(\vec x)\diverge$. If it halts in a non-standard configuration, the second summand is a search which never succeeds, so the expression diverges — here we use the convention that $0 \cdot e$ is undefined when $e$ is. If it halts in a standard configuration, the second summand is $0$ and the value is the output. All functions involved are primitive recursive, except for the two minimizations.
:::

:::quiz[arithmetization]
Why is $\mathrm{Conf}(\vec x, t)$ primitive recursive, while the function computed by $M$ is in general only partial recursive?

- [x] $\mathrm{Conf}$ iterates the step function a **given** number $t$ of times, which is a primitive recursion; the number of steps before halting is not known in advance and must be found by an unbounded search.
- [ ] Because configurations cannot be coded primitive recursively.

  They can: this is what makes $\mathrm{Next}$ primitive recursive.
- [ ] Because $\mathrm{Next}$ is only partial recursive.

  $\mathrm{Next}$ is a definition by finitely many cases using primitive recursive operations.

---

What would go wrong if $\mathrm{Next}$ were left undefined on halting configurations?

- [x] $\mathrm{Conf}$ would be a partial function, defined by primitive recursion from a partial step function; it would no longer be primitive recursive, since primitive recursive functions are total.

  Making $\mathrm{Next}$ fix halting configurations keeps $\mathrm{Conf}$ total: it stabilizes on the final configuration.
- [ ] The machine would never halt.

  The behavior of the machine is not affected by how we code it.
- [ ] The function $\mathrm{Out}$ would be undefined.

  $\mathrm{Out}$ does not use $\mathrm{Next}$.
:::

## Kleene's normal form theorem

The construction above depends on the machine $M$ only through its transition table, a finite object. Code each machine by an integer $e$, say $e = [m, a, d]$ where $d$ codes the list of the transitions $\delta(q, b) = (q', b', D)$ as quintuples. Integers which do not code a machine are treated as coding a fixed machine that never halts. Then the step function $\mathrm{Next}(e, c)$ is primitive recursive **in both arguments**: the transition is found by a bounded search in the list $d$.

:::theorem[Kleene's normal form]{#thm-kleene-normal-form-proof}
For each $k \geq 1$ there are a primitive recursive predicate $T_k(e, \vec x, s)$ and a primitive recursive function $U(s)$ such that:

1. for every $e$ and $\vec x$, there is at most one $s$ with $T_k(e, \vec x, s)$;
2. for every Turing machine with code $e$, the function it computes is $\vec x \mapsto U(\mu s\, T_k(e, \vec x, s))$.

Consequently every partial recursive function $f$ can be written $f(\vec x) \simeq U(\mu s\, T_k(e, \vec x, s))$ for some $e$.
:::

:::proof{of=thm-kleene-normal-form-proof}
Let $T_k(e, \vec x, s)$ state that $s$ codes the **whole computation**: $s = [c_0, \dots, c_t]$ with $c_0 = \mathrm{Init}(\vec x)$, $c_{i+1} = \mathrm{Next}(e, c_i)$ for $i < t$, $c_t$ halting and standard, and $c_i$ not halting for $i < t$. This is a conjunction of bounded quantifications over $i < \mathrm{lh}(s)$, hence primitive recursive. Such an $s$ is unique: $c_0$ is fixed, each $c_{i+1}$ is determined by $c_i$, and $t$ is the first index of a halting configuration. Let $U(s) = \mathrm{Out}((s)'_{\mathrm{lh}(s) - 1})$, the output read on the last configuration.

If the machine $e$ halts on $\vec x$ in a standard configuration, $\mu s\, T_k(e, \vec x, s)$ is the code of its computation and $U$ returns the output. Otherwise no $s$ satisfies $T_k$, and the search diverges. The last statement follows once we know that every partial recursive function is Turing-computable, which is :ref{#prop-pr-tm} below; its proof does not use the normal form theorem.
:::

:::quiz[the normal form theorem]
Why does $s$ code the whole computation, rather than just the number of steps $t$?

- [x] So that the output can be extracted from $s$ alone by a function $U$ which does not depend on $e$ and $\vec x$.

  With $s = t$, the output would be $\mathrm{Out}(\mathrm{Conf}(e, \vec x, t))$, a function of $e$, $\vec x$ and $t$; Kleene's formulation asks for a single function $U$ of $s$.
- [ ] Because the number of steps is not primitive recursive.

  The point is not the complexity of the number of steps: the number of steps alone does not determine the output, while the code of the whole computation contains the final configuration.
- [ ] To guarantee that the search terminates.

  Termination depends only on whether the machine halts.
:::

## From partial recursive functions to Turing machines

Call a multi-tape machine **clean** if every halting computation ends with tape $1$ in a standard final configuration, holding only the output with the head on its first cell, and all other tapes blank. A clean machine can be used as a **subroutine**: if a larger machine has tapes $j_1, \ldots, j_r$ blank except for an input on tape $j_1$, written as for a machine input, it can run the subroutine on these tapes, with the other tapes and heads untouched, and resume with the output on tape $j_1$ and the tapes $j_2, \ldots, j_r$ blank again. This is the multi-tape analogue of the sequential composition of machines (:ref{#prop-tm-composition}), and it is proved in the same way, by renaming states and redirecting the halting transitions.

:::proposition{#prop-pr-tm}
Every partial recursive function is computed by a clean multi-tape Turing machine, hence by a single-tape Turing machine.
:::

:::proof{of=prop-pr-tm}
By induction on the definition of $f$ (:ref{#def-partial-recursive}). We use three elementary multi-tape routines, each a simple loop over unary blocks: **copy** a block from one tape to the end of the content of another, separated by a blank; **erase** a block; and **compare** two blocks, by moving two heads along them simultaneously (:ref{#ex-two-tape-equality}).

*Basic functions.* The zero function, the successor and the projections are computed by single-tape machines (:ref{#ex-tm-zero}, :ref{#prop-tm-successor}, :ref{#ex-tm-projection}), which can be made clean (:ref{#ex-tm-clean-halt}).

*Composition.* Let $f(\vec x) \simeq h(g_1(\vec x), \ldots, g_m(\vec x))$, with clean machines $G_1, \ldots, G_m$ and $H$, using at most $r$ tapes each. The machine for $f$ has a block of $r$ work tapes for each subroutine. For $i = 1, \ldots, m$, it copies the input from tape $1$ to the first work tape of block $i$ and runs $G_i$ there; if some $g_i(\vec x)$ diverges, the machine runs forever, as it should, since $f(\vec x)$ then diverges. It then copies the outputs $g_1(\vec x), \ldots, g_m(\vec x)$, in this order, to the first tape of the block of $H$, erases the work tapes, runs $H$, erases tape $1$, copies the result to tape $1$ and erases the work tape of $H$.

*Primitive recursion.* Let $f(\vec x, 0) \simeq g(\vec x)$ and $f(\vec x, y + 1) \simeq h(\vec x, y, f(\vec x, y))$. The machine keeps a counter $i$ on a tape, initially $0$, and a current value $v$ on another tape, initially the output of $g$ on $\vec x$, computed by a subroutine. While the counter differs from $y$, which it checks with the comparison routine, it runs $h$ on $\vec x, i, v$ (copied to a work tape), replaces $v$ by the result, and increments $i$. When $i = y$, it writes $v$ on tape $1$ as the output and erases everything else. By induction on $i$, after $i$ rounds the value tape holds $f(\vec x, i)$; if some value diverges, the machine runs forever.

*Minimization.* Let $f(\vec x) \simeq \mu z\, [g(\vec x, z) = 0]$. The machine keeps a candidate $z$, initially $0$, runs $g$ on $\vec x, z$, and checks whether the output is $0$, a block of a single $1$. If it is, it writes $z$ as the output and erases everything else; otherwise it increments $z$ and repeats. If $g(\vec x, z')$ diverges for some $z'$ before the first zero, the machine runs forever at that round, in accordance with the definition of $\mu$ (:ref{#def-mu}).

In each case the machine is clean. By :ref{#thm-multitape-simulation}, every multi-tape machine is simulated by a single-tape one.
:::

:::quiz[the simulation of the schemes]
Why are the machines required to be clean?

- [x] So that a machine can be used as a subroutine: its output is in a known place and its work tapes are blank afterwards, ready for the next call, as in the loop of the primitive recursion case.
- [ ] Because unclean machines compute different functions.

  A machine computes its function whatever it leaves on the other tapes; cleanliness is about reusing it.
- [ ] To make the machine halt.

  Cleanliness concerns the final configuration of the halting computations; it does not make a machine halt.
:::

## Proof of the equivalence

:ref{#thm-tm-pr} now follows: every Turing-computable function is partial recursive by :ref{#prop-tm-partial-recursive}, and every partial recursive function is Turing-computable by :ref{#prop-pr-tm}. From now on, we call these functions the **partial computable** functions, and their total members the **computable** functions.

## The universal function

A consequence of the normal form theorem is that a single partial computable function evaluates all the others.

:::corollary[Universal function]{#cor-universal-function}
The function $\Phi(e, \vec x) \simeq U(\mu s\, T_k(e, \vec x, s))$ is partial computable, and for every partial computable $f : \nat^k \rightharpoonup \nat$ there is $e$ with $f(\vec x) \simeq \Phi(e, \vec x)$ for all $\vec x$. In particular, there is a **universal Turing machine**, which on input $(e, \vec x)$ simulates the machine coded by $e$ on $\vec x$.
:::

:::proof{of=cor-universal-function}
$\Phi$ is partial recursive, as it is obtained from primitive recursive functions by one minimization and one composition. By :ref{#prop-pr-tm}, it is computed by some Turing machine. The second statement is :ref{#thm-kleene-normal-form-proof}.
:::

Writing $\Phi_e(\vec x) \simeq \Phi(e, \vec x)$, the sequence $\Phi_0, \Phi_1, \Phi_2, \dots$ is an enumeration of all partial computable functions. Its study is the subject of the course on the fundamentals of computability, starting with the lesson :ref{to="fundamentals/programs-as-numbers"}.

:::quiz[the universal function]
The diagonal argument of the lesson on the Ackermann function showed that the evaluation function of the primitive recursive functions is not primitive recursive. Why does the same argument not show that $\Phi$ is not partial computable?

- [x] The diagonal function $d(e) \simeq \Phi(e, e) + 1$ is partial computable, hence equal to some $\Phi_{e_0}$; but then $d(e_0) \simeq \Phi(e_0, e_0) + 1$ only shows that $\Phi(e_0, e_0)$ is undefined — no contradiction for partial functions.
- [ ] Because $\Phi$ is not total, so it cannot be diagonalized against.

  It can be: the argument yields information, namely that $\Phi(e_0, e_0)\diverge$.
- [ ] Because $\Phi$ has two arguments.

  The number of arguments plays no role: the argument restricts $\Phi$ to the diagonal $(e, e)$ in any case.
:::

## Exercises

::::exercise{#ex-step-bounded-halting difficulty=2 objective="Express halting within a given number of steps by a primitive recursive predicate, using the uniform step function."}
Using the uniform step function of the normal form theorem, show that the predicate $H(e, x, t)$: "the machine of code $e$ halts on input $x$ within $t$ steps, in a standard final configuration" is primitive recursive, and that $\{(e, x) : \exists t\ H(e, x, t)\}$ is the domain of the universal function.

:::solution
Let $\mathrm{Conf}(e, x, t)$ be the uniform version of the iteration function, defined by primitive recursion from $\mathrm{Next}(e, c)$, hence primitive recursive in $e, x, t$. Since $\mathrm{Next}$ fixes halting configurations, $H(e, x, t) \iff \mathrm{Halt}(\mathrm{Conf}(e, x, t)) \wedge \mathrm{Std}(\mathrm{Conf}(e, x, t))$, a primitive recursive predicate. The machine halts on $x$ in a standard configuration iff some $t$ satisfies $H$, iff some $s$ satisfies $T_1(e, x, s)$, iff $\mu s\, T_1(e, x, s)$ converges, iff $(e, x) \in \dom \Phi$ (as $U$ is total).
:::
::::

## Notes and references

Turing sketched in an appendix to his 1936 paper that the λ-definable functions are computable by his machines, and proved the equivalence of the two notions in 1937; Kleene proved the equivalence of λ-definability with general recursiveness in 1936. The predicate $T$ of the normal form theorem is often called *Kleene's $T$-predicate*. The arithmetization of computations given here follows the treatment of Turing machines in Cutland's and Odifreddi's textbooks; the simulation of the schemes by multi-tape machines is the standard one (see Odifreddi, Chapter I). Soare (2016, §§1.5.2–1.5.3) codes Turing configurations as finite sequences of symbols and derives the enumeration theorem and the universal machine; Monin and Patey (chapter "Church–Turing thesis", subsection "Computable functions are recursive") arithmetize register machines instead, with a single minimization over the computation time.

- S. C. Kleene, *General recursive functions of natural numbers*, Mathematische Annalen 112 (1936), 727–742.
- A. M. Turing, *Computability and λ-definability*, Journal of Symbolic Logic 2 (1937), 153–163.
- N. Cutland, *Computability: An Introduction to Recursive Function Theory*, Cambridge University Press, 1980.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989, chapter I.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §1.5.
- B. Monin, L. Patey, *Computability theory*, chapter "Church–Turing thesis".

:::::exercises
::::exercise{#ex-init-pr difficulty=1 objective="Check that the initial configuration of a Turing machine is a primitive recursive function of the input."}
Show that the function $\mathrm{Init}(\vec x)$ is primitive recursive.

:::solution
For a single argument, the code of $1^{x+1}$ is $\prod_{i \leq x} p_i^{2}$ (each entry $1$ is coded by exponent $2$), a bounded product. The code of a separator $[0]$ is $2$. The code of the whole word is obtained by concatenating these codes with the primitive recursive operation $*$, and $\mathrm{Init}(\vec x) = \langle 0, 1, w_{\vec x} \rangle$, where $1 = [\,]$.
:::
::::

::::exercise{#ex-pr-enumeration-universal difficulty=3 objective="Obtain a total computable enumeration of the primitive recursive functions from the universal function, and diagonalize against it."}
Show that there is a total computable function $g : \nat^2 \to \nat$ such that the functions $g(e, \cdot)$ are exactly the primitive recursive functions of one argument, and deduce once more that $g$ is not primitive recursive.

:::solution
Code derivations of unary primitive recursive functions by integers, mapping non-codes to a fixed derivation of $Z$. Each derivation can be translated computably into a Turing machine computing the same function; let $t(e)$ be the code of the machine obtained from the derivation $e$. Then $g(e, x) = \Phi(t(e), x)$ is computable and total, since primitive recursive functions are total. If $g$ were primitive recursive, so would be $x \mapsto g(x, x) + 1$, which differs from every $g(e, \cdot)$ at $e$.
:::
::::

::::exercise{#ex-tm-conf-example difficulty=1 objective="Compute the codes of the successive configurations of a machine with the step function."}
Number the states of the successor machine $M_S$ of the lesson :ref{to="models-of-computation/turing-machines"} as $q_0 \mapsto 0$, $q_h \mapsto 1$, $q_1 \mapsto 2$, and its symbols as $\sqcup \mapsto 0$, $1 \mapsto 1$. Compute $\mathrm{Conf}(1, t)$ for $t = 0, \dots, 6$, writing each code as a triple $\langle q, \ell, r \rangle$ of a state and two sequences, and check the result with $\mathrm{Halt}$, $\mathrm{Std}$ and $\mathrm{Out}$.

:::solution
$\mathrm{Init}(1) = \langle 0, [\,], [1, 1] \rangle$. The transitions used are $\delta(q_0, 1) = (q_0, 1, R)$, $\delta(q_0, \sqcup) = (q_1, 1, L)$, $\delta(q_1, 1) = (q_1, 1, L)$ and $\delta(q_1, \sqcup) = (q_h, \sqcup, R)$. Applying $\mathrm{Next}$:

| $t$ | state | $\ell$ | $r$ | scanned |
| --- | --- | --- | --- | --- |
| $0$ | $0$ | $[\,]$ | $[1, 1]$ | $1$ |
| $1$ | $0$ | $[1]$ | $[1]$ | $1$ |
| $2$ | $0$ | $[1, 1]$ | $[\,]$ | $0$ |
| $3$ | $2$ | $[1]$ | $[1, 1]$ | $1$ |
| $4$ | $2$ | $[\,]$ | $[1, 1, 1]$ | $1$ |
| $5$ | $2$ | $[\,]$ | $[0, 1, 1, 1]$ | $0$ |
| $6$ | $1$ | $[0]$ | $[1, 1, 1]$ | |

For instance, from $t = 2$, the scanned symbol is $\mathrm{hd}([\,]) = 0$, the move is $L$, and $\mathrm{Next}$ gives the state $2$, the left part $\mathrm{tl}([1, 1]) = [1]$ and the right part $\mathrm{cons}(1, \mathrm{cons}(1, [\,])) = [1, 1]$. From $t = 4$, $\mathrm{tl}([\,]) = [\,]$ and $\mathrm{hd}([\,]) = 0$: the head moves onto cell $-1$, which was not stored, and a blank is added in front of $r$. At $t = 6$ the state is $1$, so $\mathrm{Halt}$ holds and $\mathrm{Conf}(1, t)$ is constant from then on. $\mathrm{Std}$ holds: $\ell$ contains only blanks and $r$ is $[1, 1, 1]$. $\mathrm{Out}$ gives $3 - 1 = 2$, in agreement with :ref{#prop-tm-successor}, whose proof counts $2x + 4 = 6$ steps.
:::
::::

::::exercise{#ex-tm-time-bound-pr difficulty=1 objective="Deduce from the arithmetization that a machine running in primitive recursive time computes a primitive recursive function."}
Let a Turing machine $M$ compute a total function $f : \nat^k \to \nat$, and suppose that there is a primitive recursive $b$ such that $M$ halts on every input $\vec x$ within $b(\vec x)$ steps. Show that $f$ is primitive recursive.

:::solution
Since $f$ is total, $M$ halts on every $\vec x$ in a standard final configuration, after $t_0(\vec x) \leq b(\vec x)$ steps. Since $\mathrm{Next}$ fixes halting configurations, $\mathrm{Conf}(\vec x, t) = \mathrm{Conf}(\vec x, t_0(\vec x))$ for all $t \geq t_0(\vec x)$, in particular for $t = b(\vec x)$. Hence $f(\vec x) = \mathrm{Out}(\mathrm{Conf}(\vec x, b(\vec x)))$, a composition of primitive recursive functions: the unbounded search of :ref{#prop-tm-partial-recursive} is replaced by the bound.
:::
::::

::::exercise{#ex-nondeterministic-tm difficulty=2 objective="Arithmetize non-deterministic machines to show that they compute only partial recursive functions."}
A **non-deterministic** machine is defined as in :ref{#def-turing-machine}, except that $\delta$ is a finite relation: a set of quintuples $(q, a, q', b, D)$ with $q \neq q_h$. A configuration may then have several successors, or none, and a computation is any sequence of configurations each of which is a successor of the previous one. Suppose that for every input $\vec x$, all the computations from the initial configuration on $\vec x$ that end in a standard final configuration have the same output. Let $f(\vec x)$ be this output if there is such a computation, and undefined otherwise. Show that $f$ is partial recursive.

:::solution
For each quintuple $\theta = (q, a, q', b, D)$ of $\delta$, define $\mathrm{Next}_\theta(c)$ as $\mathrm{Next}$ in the lesson, with $q'$, $b$, $D$ given by $\theta$; it is primitive recursive. Let $\mathrm{Succ}(c, c')$ hold if, for some $\theta = (q, a, \dots) \in \delta$, the state of $c$ is $q$, its scanned symbol $\mathrm{hd}(r)$ is $a$, and $c' = \mathrm{Next}_\theta(c)$. This is a finite disjunction of primitive recursive predicates. Let $N(\vec x, s)$ state that $s = [c_0, \dots, c_t]$ with $c_0 = \mathrm{Init}(\vec x)$, $\mathrm{Succ}(c_i, c_{i+1})$ for all $i < t$, and $c_t$ halting and standard. It is primitive recursive, by bounded quantification over $i < \mathrm{lh}(s)$. Let $f'(\vec x) \simeq U(\mu s\, N(\vec x, s))$, with $U$ as in :ref{#thm-kleene-normal-form-proof}; $f'$ is partial recursive.

Every $s$ with $N(\vec x, s)$ codes a computation of the machine on $\vec x$ ending in a standard configuration, and conversely each such computation is coded by some $s$, obtained by coding each successor with $\mathrm{Next}_\theta$. If $f(\vec x)\converge$, such a computation exists, the search terminates, and it finds the code of some such computation, whose output is $f(\vec x)$ by hypothesis: $f'(\vec x) = f(\vec x)$. If $f(\vec x)\diverge$, no $s$ satisfies $N(\vec x, s)$ and the search diverges. Hence $f = f'$ is partial recursive, and by :ref{#thm-tm-pr} it is computed by an ordinary Turing machine. The search over codes of computations plays the role of the breadth-first simulation of the lesson :ref{to="models-of-computation/multitape-machines"}.
:::
::::
:::::
