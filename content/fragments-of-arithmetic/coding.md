---
title: Coded finite sequences
summary: Finite sequences coded as finite graphs in IΔ₀ + exp; length and entries are bounded relations; the bound on codes, definable sequences, concatenation and restriction; the finite pigeonhole principle.
duration: 25
prerequisites: [ackermann-coding, models-of-computation/coding-sequences]
---

With finite sets coded, a finite sequence is coded as its graph, a finite set of pairs. The relations "$s$ codes a sequence of length $\ell$" and "the $i$-th entry of $s$ is $v$" are then bounded, and the operations on sequences are given by comprehension. The one quantitative fact to remember is the bound on codes: a sequence of length $\ell$ with entries below $b$ has a code below $2^{\langle \ell, b \rangle}$. It is what keeps induction formulas bounded when they quantify over sequences, as in the finite pigeonhole principle at the end of the lesson. We work in $\mathrm I\Delta_0 + \mathrm{exp}$, as in the previous lesson.

## Finite sequences

A finite sequence is coded as the graph of a function on an initial interval, a set of pairs $\langle i, v \rangle$ coded by the pairing function of :ref{#fact-pairing}. We write $\langle i, v \rangle \in s$ for the bounded formula $\exists z < s + 1\ (z = \langle i, v \rangle \wedge z \in s)$.

:::definition{#def-coded-sequence}
$\mathrm{Seq}(s, \ell)$, "$s$ codes a sequence of length $\ell$", is the conjunction of
$$
\begin{gathered}
\forall z < s\ \big( z \in s \rightarrow \exists i < \ell\ \exists v < z + 1\ (z = \langle i, v \rangle) \big), \qquad \forall i < \ell\ \exists v < s\ (\langle i, v \rangle \in s), \\
\forall i < \ell\ \forall v < s\ \forall v' < s\ \big( \langle i, v \rangle \in s \wedge \langle i, v' \rangle \in s \rightarrow v = v' \big).
\end{gathered}
$$
:::

The formula is bounded, since $v \leq \langle i, v \rangle < s$ for every pair in $s$. If $\mathrm{Seq}(s, \ell)$ and $\mathrm{Seq}(s, \ell')$, then $\ell = \ell'$: if $\ell < \ell'$, some pair $\langle \ell, v \rangle$ belongs to $s$, but all pairs in $s$ have a first component less than $\ell$. We write $\mathrm{lh}(s) = \ell$ and, for $i < \ell$, $(s)_i$ for the unique $v$ with $\langle i, v \rangle \in s$. Since $\ell \leq s$, the formula $\mathrm{Seq}(s) \equiv \exists \ell < s + 1\ \mathrm{Seq}(s, \ell)$ is bounded, and so are the graphs of $\mathrm{lh}$ and of $(s)_i$. The empty sequence is coded by $0$.

:::proposition{#prop-seq-basic}
$\mathrm I\Delta_0 + \mathrm{exp}$ proves:

1. (**bound**) if $\mathrm{Seq}(s, \ell)$ and $(s)_i < b$ for every $i < \ell$, then $s < 2^{\langle \ell, b \rangle}$;
2. (**definable sequences**) for every $\Delta_0$ formula $\varphi(i, v, \bar p)$: if $\forall i < \ell\ \exists! v < b\ \varphi(i, v, \bar p)$, then there is a sequence $s$ of length $\ell$ with $\varphi(i, (s)_i, \bar p)$ for every $i < \ell$;
3. (**concatenation**) for every sequence $s$ of length $\ell$ and every $v$, there is a sequence $s^\frown v$ of length $\ell + 1$ with $(s^\frown v)_i = (s)_i$ for $i < \ell$ and $(s^\frown v)_\ell = v$;
4. (**restriction**) for every sequence $s$ of length $\ell$ and every $k \leq \ell$, there is a sequence $s \restriction k$ of length $k$ with $(s \restriction k)_i = (s)_i$ for $i < k$.
:::

:::proof{of=prop-seq-basic}
1. Every element of $s$ is a pair $\langle i, v \rangle$ with $i < \ell$ and $v < b$, hence less than $\langle \ell, b \rangle$ by the monotonicity of pairing (:ref{#fact-pairing}). By item 3 of :ref{#lem-ack-basic}, $s < 2^{\langle \ell, b \rangle}$.

2. By :ref{#thm-delta0-comprehension} with $a = \langle \ell, b \rangle$, there is $s$ coding $\{ z < a : \exists i < \ell\ \exists v < b\ (z = \langle i, v \rangle \wedge \varphi(i, v, \bar p)) \}$. Every pair $\langle i, v \rangle$ with $i < \ell$ and $v < b$ is less than $a$, so $s$ contains exactly the pairs $\langle i, v \rangle$ with $i < \ell$, $v < b$ and $\varphi(i, v, \bar p)$. By the hypothesis, this is the graph of a function on $[0, \ell)$, and the three clauses of :ref{#def-coded-sequence} hold.

3. and 4. For item 3, apply item 2, with length $\ell + 1$ and $b = s + v + 1$, to the formula $(i < \ell \wedge w = (s)_i) \vee (i = \ell \wedge w = v)$ in the variables $i$ and $w$. For item 4, apply it, with length $k$ and $b = s$, to the formula $w = (s)_i$; the entries of $s$ are below $s$, since $v \leq \langle i, v \rangle < s$.
:::

:::quiz[coded sequences]
In the proof of item 2 of :ref{#prop-seq-basic}, why is the hypothesis that the values $v$ are bounded by $b$ needed?

- [x] Comprehension produces codes of subsets of a bounded interval $[0, a)$; the pairs $\langle i, v \rangle$ of the graph must all lie in such an interval, which requires a bound on $v$.
- [ ] To make the function $i \mapsto v$ total.

  Totality on $[0, \ell)$ is part of the hypothesis $\forall i < \ell\ \exists! v$; the bound plays no role in it.
- [ ] To make the formula $\varphi$ bounded.

  $\varphi$ is bounded by hypothesis; the bound $b$ concerns the size of the code.
:::

## Exercises

::::exercise{#ex-finite-pigeonhole difficulty=2}
(**Finite pigeonhole principle.**) Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves: if $s$ is a sequence of length $a + 1$ with $(s)_i < a$ for every $i \leq a$, then $(s)_i = (s)_j$ for some $i < j \leq a$.

:::solution
Fix $a$ and the parameter $B = 2^{\langle a + 1, a \rangle}$. By item 1 of :ref{#prop-seq-basic} and the monotonicity of pairing, $B$ bounds the codes of all sequences of length $x + 1 \leq a + 1$ with values below $x \leq a$. Let $\psi(x)$ say: if $x \leq a$, no $s < B$ is an injective sequence of length $x + 1$ with values below $x$. It is bounded, with parameters $a$ and $B$. $\psi(0)$ holds, since no value is below $0$. We show that $\psi(x)$ implies $\psi(x + 1)$. Suppose that $x + 1 \leq a$ and that $\psi(x + 1)$ fails, witnessed by an injective $s$ of length $x + 2$ with values below $x + 1$. If no entry of $s$ equals $x$, or if $(s)_{x+1} = x$, then $s \restriction (x + 1)$ is injective with values below $x$. If $(s)_j = x$ with $j \leq x$, let $s'$ be the sequence of length $x + 1$ equal to $s$ except that $(s')_j = (s)_{x+1}$, given by item 2 of :ref{#prop-seq-basic}; it is injective with values below $x$, because $(s)_{x+1} \neq x$. In each case the new sequence is below $B$, by the choice of $B$, and $\psi(x)$ fails. By bounded induction, $\psi(a)$ holds. The given sequence $s$ has length $a + 1$ and values below $a$, so $s < B$, and it is not injective.
:::
::::

## Notes and references

The development follows Hájek and Pudlák, Chapter I, Section 1(b) (sequences, Definition I.1.42 and Theorem I.1.43; the pigeonhole principle for finite sets, Theorem I.1.41), where exponentiation is a function symbol of the language. Codings of sequences that work without exponentiation, or without any induction, exist: see Hájek and Pudlák, Chapter V, Section 3, and Jeřábek (2012).

- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(b).
- E. Jeřábek, *Sequence coding without induction*, Mathematical Logic Quarterly 58 (2012), 244–248.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 2 and 3.
