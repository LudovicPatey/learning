---
title: Equivalence of all the models
summary: Five models of computation, Turing machines, register machines, WHILE programs, partial recursive functions and λ-terms, compute the same partial functions; the simulation of register machines by Turing machines closes the cycle of implications; a direct arithmetization of register machines.
duration: 15
prerequisites: [while-programs, lambda-definability]
---

The core course proved that Turing machines compute exactly the partial recursive functions (:ref{#thm-tm-pr}). This course has added three more models, each with its own equivalence with the partial recursive functions or with another model. This lesson assembles them into one theorem, by a simulation of register machines on Turing machines. The equivalence of so many independent definitions is the main evidence for the Church–Turing thesis.

:::theorem[Equivalence of the models]{#thm-equivalence-models}
For a partial function $f : \nat^k \rightharpoonup \nat$, the following are equivalent:

1. $f$ is Turing-computable;
2. $f$ is URM-computable;
3. $f$ is WHILE-computable;
4. $f$ is partial recursive;
5. $f$ is λ-definable.
:::

:::figure[The implications proved in this course. The equivalence of (1) and (4) is proved in the core course on models of computation, the other implications in this course.]
<svg class="fig" viewBox="0 0 660 260" width="660" role="img" aria-label="Implications between the five models of computation"><defs><marker id="ah-eqv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect class="node" x="25.0" y="31.0" width="150" height="38" rx="8"/><text x="100" y="55" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(1) Turing machines</text><rect class="node" x="295.0" y="31.0" width="150" height="38" rx="8"/><text x="370" y="55" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(4) partial recursive</text><rect class="node" x="295.0" y="191.0" width="150" height="38" rx="8"/><text x="370" y="215" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(3) WHILE programs</text><rect class="node" x="25.0" y="191.0" width="150" height="38" rx="8"/><text x="100" y="215" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(2) register machines</text><rect class="node" x="520.0" y="31.0" width="120" height="38" rx="8"/><text x="580" y="55" text-anchor="middle" class="label" style="fill: currentColor; font-size: 13px">(5) λ-terms</text><line x1="177.0" y1="50.0" x2="292.0" y2="50.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="235" y="40" text-anchor="middle" class="label">arithmetization</text><line x1="370.0" y1="71.0" x2="370.0" y2="188.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="380" y="134" text-anchor="start" class="label">compilation</text><line x1="293.0" y1="210.0" x2="178.0" y2="210.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="235" y="200" text-anchor="middle" class="label">translation</text><line x1="100.0" y1="189.0" x2="100.0" y2="72.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="90" y="134" text-anchor="end" class="label">simulation</text><line x1="447.0" y1="42.0" x2="517.0" y2="42.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="482" y="32" text-anchor="middle" class="label">definability</text><line x1="518.0" y1="58.0" x2="448.0" y2="58.0" class="ink-stroke" stroke-width="1.4" marker-end="url(#ah-eqv)"/><text x="482" y="82" text-anchor="middle" class="label">normal order</text></svg>
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

The following implications are established:
$$
(1) \Longleftrightarrow (4) \Longrightarrow (3) \Longrightarrow (2) \Longrightarrow (1), \qquad (4) \Longleftrightarrow (5).
$$
Indeed, (1) ⇔ (4) is :ref{#thm-tm-pr}; (4) ⇒ (3) is :ref{#thm-while-partial-recursive}; (3) ⇒ (2) is :ref{#prop-while-urm}; (2) ⇒ (1) is :ref{#prop-urm-tm}; and (4) ⇔ (5) is :ref{#thm-recursive-lambda-definable} with :ref{#thm-lambda-definable-recursive}. All five classes coincide. Another route from (2) to (4), without Turing machines, is :ref{#ex-urm-arithmetization}.

:::quiz[the cycle of implications]
Why does the proof go around a cycle of implications rather than proving each equivalence separately?

- [x] Because a cycle of implications between all the models proves every equivalence at once: from any model one reaches any other by following the arrows, so $n$ implications suffice instead of $n(n-1)$.
- [ ] Because some equivalences are false.

  All the equivalences hold; the cycle is an economy of proofs.
- [ ] Because register machines cannot simulate Turing machines directly.

  They can, by coding the tape in registers; it is simply not needed for the theorem.
:::

::::exercise{#ex-urm-arithmetization difficulty=2  objective="Arithmetize register machines directly, to show that URM-computable functions are partial recursive without Turing machines."}
Let $P = I_1, \dots, I_s$ be a URM program computing $f : \nat^k \rightharpoonup \nat$, and $\rho = \max(\rho(P), k)$. Code the configuration $(i, r)$ by $\langle i, [r(1), \dots, r(\rho)] \rangle$. Show that the step function on codes is primitive recursive, and deduce that $f$ is partial recursive.

:::solution
Registers of index $> \rho$ contain $0$ initially and are never mentioned by $P$, so they stay $0$, and the code determines the configuration. For a code $c$, let $i = \pi_0(c)$ and $v = \pi_1(c)$; register $R_n$ is the entry $(v)'_{n-1}$. Define $\mathrm{Next}_P(c) = c$ if $i = 0$ or $i > s$, and otherwise by cases on $i \in \{1, \dots, s\}$, according to the instruction $I_i$:

- $Z(n)$: $\langle i + 1, \mathrm{set}(v, n - 1, 0) \rangle$; $S(n)$: $\langle i + 1, \mathrm{set}(v, n - 1, (v)'_{n-1} + 1) \rangle$;
- $T(m, n)$: $\langle i + 1, \mathrm{set}(v, n - 1, (v)'_{m-1}) \rangle$;
- $J(m, n, q)$: $\langle q, v \rangle$ if $(v)'_{m-1} = (v)'_{n-1}$, and $\langle i + 1, v \rangle$ otherwise.

This is a definition by finitely many cases from the primitive recursive operations of :ref{#prop-seq-operations}, so $\mathrm{Next}_P$ is primitive recursive, and by :ref{#def-urm-semantics} it maps the code of a configuration to the code of its successor. Let $\mathrm{Conf}(\vec x, 0) = \langle 1, [x_1, \dots, x_k, 0, \dots, 0] \rangle$ (with $\rho$ entries) and $\mathrm{Conf}(\vec x, t + 1) = \mathrm{Next}_P(\mathrm{Conf}(\vec x, t))$, a primitive recursion. Then
$$
f(\vec x) \simeq \Big(\pi_1\big(\mathrm{Conf}(\vec x, \mu t\, [\pi_0(\mathrm{Conf}(\vec x, t)) > s])\big)\Big)'_0 ,
$$
since the program halts exactly when the instruction index exceeds $s$, and the output is the content of $R_1$. This is the route followed by Monin and Patey; it gives (2) ⇒ (4) of :ref{#thm-equivalence-models} directly.
:::
::::

## Notes and references

The equivalences were established in 1936–1937 by Kleene (general recursiveness and λ-definability) and Turing (λ-definability and his machines); register machines are due to Shepherdson and Sturgis (1963), and the LOOP and WHILE languages to Meyer and Ritchie (1967). The cycle of simulations follows Cutland's textbook.

- N. Cutland, *Computability: An Introduction to Recursive Function Theory*, Cambridge University Press, 1980.
- J. C. Shepherdson and H. E. Sturgis, *Computability of recursive functions*, Journal of the ACM 10 (1963), 217–255.
- A. M. Turing, *Computability and λ-definability*, Journal of Symbolic Logic 2 (1937), 153–163.

