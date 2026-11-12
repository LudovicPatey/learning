---
title: Equivalence of the models
summary: Arithmetization of Turing machines, proof of Kleene's normal form theorem, simulation of register machines by Turing machines, and the universal partial recursive function.
duration: 50
prerequisites: [while-programs, lambda-definability, multitape-machines]
---

We have met five definitions of computable partial function. Some equivalences are already proved:

- WHILE-computable $\iff$ partial recursive (:ref{#thm-while-partial-recursive});
- partial recursive $\iff$ λ-definable (:ref{#thm-recursive-lambda-definable} and :ref{#thm-lambda-definable-recursive});
- WHILE-computable $\implies$ URM-computable (:ref{#prop-while-urm}); the converse follows from the other implications below, and is also the last exercise of the lesson on WHILE programs.

It remains to connect Turing machines to the other models. In this lesson we prove that every Turing-computable function is partial recursive, by **arithmetizing** the computations of Turing machines, and that every URM-computable function is Turing-computable, by simulation. Along the way we obtain Kleene's normal form theorem and a universal partial recursive function.

:::theorem[Equivalence of the models]{#thm-equivalence-models}
For a partial function $f : \nat^k \rightharpoonup \nat$, the following are equivalent:

1. $f$ is Turing-computable;
2. $f$ is URM-computable;
3. $f$ is WHILE-computable;
4. $f$ is partial recursive;
5. $f$ is λ-definable.
:::

:::figure[The implications proved in this course. The cycle through (1), (4), (3) and (2) is completed in this lesson; the equivalence of (4) and (5) is proved in the lesson on λ-definability.]
<svg class="fig" viewBox="0 0 660 260" width="660" role="img" aria-label="Implications between the five models of computation"><defs><marker id="ah-eqv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect class="node" x="25.0" y="31.0" width="150" height="38" rx="8"/><text x="100" y="55" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(1) Turing machines</text><rect class="node" x="295.0" y="31.0" width="150" height="38" rx="8"/><text x="370" y="55" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(4) partial recursive</text><rect class="node" x="295.0" y="191.0" width="150" height="38" rx="8"/><text x="370" y="215" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(3) WHILE programs</text><rect class="node" x="25.0" y="191.0" width="150" height="38" rx="8"/><text x="100" y="215" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(2) register machines</text><rect class="node" x="520.0" y="31.0" width="120" height="38" rx="8"/><text x="580" y="55" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(5) λ-terms</text><line x1="177.0" y1="50.0" x2="292.0" y2="50.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="235" y="40" text-anchor="middle" class="label">arithmetization</text><line x1="370.0" y1="71.0" x2="370.0" y2="188.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="380" y="134" text-anchor="start" class="label">compilation</text><line x1="293.0" y1="210.0" x2="178.0" y2="210.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="235" y="200" text-anchor="middle" class="label">translation</text><line x1="100.0" y1="189.0" x2="100.0" y2="72.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="90" y="134" text-anchor="end" class="label">simulation</text><line x1="447.0" y1="42.0" x2="517.0" y2="42.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="482" y="32" text-anchor="middle" class="label">definability</text><line x1="518.0" y1="58.0" x2="448.0" y2="58.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="482" y="82" text-anchor="middle" class="label">normal order</text></svg>
:::

The two new proofs use the two techniques that recur in every comparison of models. A **simulation** represents the data of one model in another, here registers on tapes, and replaces each instruction by a block of instructions. An **arithmetization** codes the configurations of a machine by integers, so that one step of the machine becomes a primitive recursive function on codes; the only part of a computation that is not primitive recursive is the search for the number of steps. This idea, from Gödel's coding of formulas in 1931, gives Kleene's normal form theorem, and through it the universal function on which the course :ref{to="fundamentals/programs-as-numbers"} is built.

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

If the machine $e$ halts on $\vec x$ in a standard configuration, $\mu s\, T_k(e, \vec x, s)$ is the code of its computation and $U$ returns the output. Otherwise no $s$ satisfies $T_k$, and the search diverges. The last statement follows once we know that every partial recursive function is Turing-computable. This is the chain of implications (4) ⇒ (3) ⇒ (2) ⇒ (1) of the last section, whose proof does not use the normal form theorem.
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

## From register machines to Turing machines

:::proposition{#prop-urm-tm}
Every URM-computable partial function is Turing-computable.
:::

:::proof{of=prop-urm-tm}
Let $P = I_1, \dots, I_s$ compute $f : \nat^k \rightharpoonup \nat$, and let $\rho = \max(\rho(P), k)$. We build a multi-tape Turing machine $N$ with $\rho + 1$ tapes, following the conventions of :ref{#def-multitape}: tape $1$ holds the input and the output, all heads start on cell $0$, the other tapes are initially blank, and during the simulation tape $n + 1$, for $1 \leq n \leq \rho$, holds the content of $R_n$ in unary, as $\ulcorner R_n \urcorner$ starting at the head position. The index of the current instruction is stored in the finite control of $N$.

1. *Initialization.* $N$ reads the input $\ulcorner x_1 \urcorner \sqcup \cdots \sqcup \ulcorner x_k \urcorner$ on tape $1$ and copies the $n$-th block to tape $n + 1$; the other register tapes receive $\ulcorner 0 \urcorner$.
2. *Simulation.* For each instruction, $N$ has a group of states:
   - $Z(n)$: erase tape $n + 1$ and write a single $1$;
   - $S(n)$: append a $1$ at the end of the block on tape $n + 1$, and return;
   - $T(m, n)$: erase tape $n + 1$ and copy the block of tape $m + 1$ onto it;
   - $J(m, n, q)$: scan the blocks of tapes $m + 1$ and $n + 1$ simultaneously from left to right; they have equal length iff both heads reach a blank at the same time. Return the heads, and enter the group of instruction $q$ or $i + 1$ accordingly.

   When the current index exceeds $s$, the simulation ends.
3. *Output.* $N$ erases tape $1$, copies the block of tape $2$ (the register $R_1$) onto it, and halts with head $1$ on its first cell.

By induction on the number of steps of $P$, after the simulation of $j$ instructions, the tapes of $N$ represent the registers of $P$ after $j$ steps. Hence $N$ computes $f$. By :ref{#thm-multitape-simulation}, so does some single-tape machine.
:::

## Proof of the equivalence

We can now complete the proof of :ref{#thm-equivalence-models}. The following implications are established:
$$
(1) \Longrightarrow (4) \Longrightarrow (3) \Longrightarrow (2) \Longrightarrow (1), \qquad (4) \Longleftrightarrow (5).
$$
Indeed, (1) ⇒ (4) is :ref{#prop-tm-partial-recursive}; (4) ⇒ (3) is :ref{#thm-while-partial-recursive}; (3) ⇒ (2) is :ref{#prop-while-urm}; (2) ⇒ (1) is :ref{#prop-urm-tm}; and (4) ⇔ (5) was proved in the previous lesson. All five classes coincide.

From now on, we call these functions the **partial computable** functions, and their total members the **computable** functions.

## The universal function

A consequence of the normal form theorem is that a single partial computable function evaluates all the others.

:::corollary[Universal function]{#cor-universal-function}
The function $\Phi(e, \vec x) \simeq U(\mu s\, T_k(e, \vec x, s))$ is partial computable, and for every partial computable $f : \nat^k \rightharpoonup \nat$ there is $e$ with $f(\vec x) \simeq \Phi(e, \vec x)$ for all $\vec x$. In particular, there is a **universal Turing machine**, which on input $(e, \vec x)$ simulates the machine coded by $e$ on $\vec x$.
:::

:::proof{of=cor-universal-function}
$\Phi$ is partial recursive, as it is obtained from primitive recursive functions by one minimization and one composition. By the equivalence, it is computed by some Turing machine. The second statement is :ref{#thm-kleene-normal-form-proof}.
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

::::exercise{difficulty=1}
Show that the function $\mathrm{Init}(\vec x)$ is primitive recursive.

:::solution
For a single argument, the code of $1^{x+1}$ is $\prod_{i \leq x} p_i^{2}$ (each entry $1$ is coded by exponent $2$), a bounded product. The code of a separator $[0]$ is $2$. The code of the whole word is obtained by concatenating these codes with the primitive recursive operation $*$, and $\mathrm{Init}(\vec x) = \langle 0, 1, w_{\vec x} \rangle$, where $1 = [\,]$.
:::
::::

::::exercise{difficulty=2}
Using the uniform step function of the normal form theorem, show that the predicate $H(e, x, t)$: "the machine of code $e$ halts on input $x$ within $t$ steps, in a standard final configuration" is primitive recursive, and that $\{(e, x) : \exists t\ H(e, x, t)\}$ is the domain of the universal function.

:::solution
Let $\mathrm{Conf}(e, x, t)$ be the uniform version of the iteration function, defined by primitive recursion from $\mathrm{Next}(e, c)$, hence primitive recursive in $e, x, t$. Since $\mathrm{Next}$ fixes halting configurations, $H(e, x, t) \iff \mathrm{Halt}(\mathrm{Conf}(e, x, t)) \wedge \mathrm{Std}(\mathrm{Conf}(e, x, t))$, a primitive recursive predicate. The machine halts on $x$ in a standard configuration iff some $t$ satisfies $H$, iff some $s$ satisfies $T_1(e, x, s)$, iff $\mu s\, T_1(e, x, s)$ converges, iff $(e, x) \in \dom \Phi$ (as $U$ is total).
:::
::::

::::exercise{difficulty=3}
Show that there is a total computable function $g : \nat^2 \to \nat$ such that the functions $g(e, \cdot)$ are exactly the primitive recursive functions of one argument, and deduce once more that $g$ is not primitive recursive.

:::solution
Code derivations of unary primitive recursive functions by integers, mapping non-codes to a fixed derivation of $Z$. Each derivation can be translated computably into a Turing machine computing the same function; let $t(e)$ be the code of the machine obtained from the derivation $e$. Then $g(e, x) = \Phi(t(e), x)$ is computable and total, since primitive recursive functions are total. If $g$ were primitive recursive, so would be $x \mapsto g(x, x) + 1$, which differs from every $g(e, \cdot)$ at $e$.
:::
::::

## Notes and references

Turing sketched in an appendix to his 1936 paper that the λ-definable functions are computable by his machines, and proved the equivalence of the two notions in 1937; Kleene proved the equivalence of λ-definability with general recursiveness in 1936. The predicate $T$ of the normal form theorem is often called *Kleene's $T$-predicate*. The arithmetization of computations given here follows the treatment of register and Turing machines in Cutland's and Odifreddi's textbooks. Soare (2016, §§1.5.2–1.5.3) codes Turing configurations as finite sequences of symbols and derives the enumeration theorem and the universal machine; Monin and Patey (chapter "Church–Turing thesis", subsection "Computable functions are recursive") arithmetize register machines instead, with a single minimization over the computation time.

- S. C. Kleene, *General recursive functions of natural numbers*, Mathematische Annalen 112 (1936), 727–742.
- A. M. Turing, *Computability and λ-definability*, Journal of Symbolic Logic 2 (1937), 153–163.
- N. Cutland, *Computability: An Introduction to Recursive Function Theory*, Cambridge University Press, 1980.
- P. Odifreddi, *Classical Recursion Theory*, North-Holland, 1989, chapter I.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §1.5.
- B. Monin, L. Patey, *Computability theory*, chapter "Church–Turing thesis".
