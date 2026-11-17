---
title: The Church–Turing thesis
summary: Formulation and status of the Church–Turing thesis, Turing's analysis of human computation, Gandy's principles, physical and complexity-theoretic variants, and the use of the thesis in proofs.
duration: 25
prerequisites: [equivalence-of-models]
---

The previous lesson established that five independent formalizations of computability define the same class of partial functions. The **Church–Turing thesis** asserts that this class is the right one.

:::aside[The Church–Turing thesis]
A partial function $f : \nat^k \rightharpoonup \nat$ is computable by an effective procedure — in the informal sense of an algorithm executed mechanically by a human with unlimited time and paper — if and only if it is Turing-computable (equivalently, partial recursive).
:::

## Status of the thesis

One direction is uncontroversial: every Turing machine describes an effective procedure. The substance of the thesis is the converse: **every** effective procedure can be simulated by a Turing machine.

The thesis is not a mathematical theorem, since one of its terms — "effective procedure" — is informal. It is a claim about the adequacy of a definition, of the same nature as the claim that the ε-δ definition captures continuity. Such claims cannot be proved, but they can be supported by arguments, and they could in principle be refuted by exhibiting an evidently effective procedure computing a non-Turing-computable function.

Church proposed the identification of effective calculability with λ-definability, and then with general recursiveness, in 1934–1936. Gödel was initially not convinced, precisely because no argument showed that these definitions exhausted all effective procedures. It was Turing's paper of 1936 that convinced him, and most of the community. The name *Church's thesis* is due to Kleene (1952, §62); since the argument that made it convincing is Turing's, Soare and others prefer to speak of *Turing's thesis* for the version about Turing machines.

:::quiz[the status of the thesis]
Which of the following would refute the Church–Turing thesis?

- [x] An effective procedure, recognized as mechanical by everyone, computing a function which is not Turing-computable.
- [ ] A function $\nat \to \nat$ which is not Turing-computable.

  Such functions exist in abundance (there are uncountably many functions and countably many machines). The thesis asserts that they are not computable by any effective procedure either.
- [ ] A programming language in which some algorithms are much shorter or faster than on Turing machines.

  The thesis is about which functions are computable, not about the length or speed of programs.
- [ ] A physical device whose behavior cannot be predicted by a Turing machine.

  This would bear on a *physical* version of the thesis (see below), not on the thesis about human computation.
:::

## Turing's analysis

Turing did not only propose a model; he argued that any computation carried out by a human following fixed rules can be performed by one of his machines. The argument, in §9 of his paper, rests on explicit constraints on the human computer:

1. **Boundedness.** The computer can only observe a bounded number of symbols at once, and can only be in one of finitely many "states of mind". Symbols are drawn from a finite alphabet, since symbols too close to each other would be indistinguishable.
2. **Locality.** In a single step, the computer can only change symbols that are observed, and can only shift attention to symbols within a bounded distance of those observed.
3. **Determinacy.** The action taken depends only on the current state of mind and the observed symbols.

Under these constraints, a step of computation can be decomposed into elementary steps of a Turing machine: the two-dimensional sheet of paper can be replaced by a one-dimensional tape, and observing a bounded region can be simulated by moving the head back and forth. Turing concludes that machines with a single head on a single tape compute everything that a human computer can compute. The constraints are where the argument can be discussed: once they are granted, the reduction to Turing machines is a mathematical argument, of the same kind as the simulations of this course. Gandy went as far as to say that Turing's analysis proves a theorem (quoted by Soare, 2016, §17.3.4).

:::quiz[Turing's analysis]
In Turing's analysis, what justifies the use of a finite alphabet?

- [x] The boundedness constraint: a human can only distinguish finitely many symbols in a bounded region, since symbols that differ arbitrarily little could not be told apart.
- [ ] The determinacy constraint.

  Determinacy concerns how the next action is chosen, not how many symbols there are.
- [ ] The locality constraint.

  Locality bounds where the computer can look and write in one step, not the number of distinct symbols.
- [ ] The finiteness of the tape.

  The tape is unbounded: Turing's machines model a computer with unlimited paper.
:::

In 1980, Gandy isolated principles under which a **discrete deterministic mechanical device**, possibly acting in parallel on many parts, is equivalent to a Turing machine. His principles include a bound on the propagation speed of causal effects, and the requirement that the state of the device be built from finitely many parts of bounded complexity. Sieg later refined this analysis into an axiomatic presentation of computability.

A related line of work axiomatizes the notion of **algorithm** itself, rather than of computing agent. Gurevich (2000) characterized sequential algorithms, through three postulates on states and steps, as the sequential abstract state machines. Dershowitz and Gurevich (2008) added a postulate requiring the initial states to contain only basic operations given in advance, and proved from these postulates that every algorithm on the integers computes a partial recursive function. Such results do not prove the thesis outright: they move the informal content into the postulates, which must in turn be accepted as a correct description of algorithms. They make explicit, however, which properties of mechanical computation the thesis depends on.

## Evidence

The thesis is supported by three kinds of evidence.

- **Convergence of definitions.** Every proposed formalization of computability has turned out to be equivalent to Turing computability: recursive functions, λ-calculus, Turing machines, Post systems, Markov algorithms, register machines, cellular automata, and all general-purpose programming languages. Their starting intuitions are very different, which makes the convergence significant.
- **Conceptual analysis.** The arguments of Turing, Gandy, Sieg, and Dershowitz and Gurevich derive the thesis from explicit, plausible properties of mechanical computation.
- **Absence of counterexamples.** No algorithm computing a non-Turing-computable function has been found in ninety years of intensive use of algorithms.

## Variants

Several stronger statements are sometimes called the Church–Turing thesis. They should be distinguished from the thesis above.

- **The physical Church–Turing thesis.** Every function computable by a physical system is Turing-computable. This is a statement about the laws of physics, not about mechanical procedures. It is open; proposed counterexamples rely on idealizations such as infinitely precise real numbers or supertasks, whose physical realizability is doubtful.
- **The extended (complexity-theoretic) thesis.** Every reasonable model of computation can be simulated by a Turing machine with at most polynomial overhead in time. This is a statement about efficiency. Quantum computing is widely believed to violate it — Shor's algorithm factors integers in polynomial time, which is not known to be possible classically — while it does not violate the Church–Turing thesis: quantum computers compute exactly the Turing-computable functions. For the λ-calculus, the question whether counting β-steps is a reasonable measure of time remained open for a long time, since a single step may duplicate a large term; Accattoli and Dal Lago (2016) showed that the number of steps of normal order reduction to normal form is a reasonable cost measure, polynomially related to the time of Turing machines, by an implementation with sharing of subterms.

:::quiz[variants of the thesis]
Quantum computers can be simulated by Turing machines, possibly with exponential slowdown. What does this imply?

- [x] Quantum computation does not contradict the Church–Turing thesis, though it may contradict the extended, complexity-theoretic thesis.
- [ ] Quantum computation refutes the Church–Turing thesis.

  It computes no new functions.
- [ ] Quantum computation proves the extended thesis.

  A simulation with exponential slowdown gives no support to the extended thesis, which requires a polynomial overhead.
:::

## Using the thesis in proofs

In practice, computability theorists rarely write Turing machines. To show that a function is computable, one describes an algorithm informally, and invokes the thesis — or, more precisely, relies on the fact that the reader could translate the description into a formal model given enough patience. Proofs of this kind are called **proofs by Church's thesis**.

This usage is safe because of the equivalence theorem: the reader may choose the most convenient model for the formalization. WHILE programs and the closure properties of partial recursive functions make the translation routine for any algorithm described precisely. In this sense the thesis is not an assumption of the theory: every theorem proved "by Church's thesis" can in principle be proved formally.

In the following courses, we adopt this practice. A function is **computable** if it is computed by some program, described in pseudo-code; we fix an enumeration $\Phi_0, \Phi_1, \Phi_2, \dots$ of the partial computable functions, given by the universal function of the previous lesson, and study its properties. The first question addressed is the one that motivated the whole enterprise: the existence of problems that are **not** computable. This is the starting point of the lesson :ref{to="fundamentals/programs-as-numbers"}.

## Exercises

::::exercise{#ex-ct-pi-sevens difficulty=2 objective="Distinguish the existence of an algorithm from the knowledge of one, on a function defined from the decimal expansion of $\pi$."}
Let $h(n) = 1$ if the decimal expansion of $\pi$ contains $n$ consecutive digits $7$ somewhere, and $h(n) = 0$ otherwise. Show that $h$ is computable. Does the proof provide a program for $h$?

:::solution
Let $S = \{n : h(n) = 1\}$. It contains $0$ (the empty block), and it is downward closed: a block of $n + 1$ sevens contains a block of $n$ sevens. A downward closed subset of $\nat$ is either $\nat$ or a finite initial segment $\{0, \dots, n_0\}$. In the first case $h$ is the constant function $1$. In the second case, $h(n) = 1$ if $n \leq n_0$ and $0$ otherwise, which is computed by a program comparing $n$ with the constant $n_0$. In both cases $h$ is computable.

The proof is not constructive: it shows that one program in an explicit infinite list (the constant $1$, and the threshold programs for $n_0 = 0, 1, 2, \dots$) computes $h$, without saying which. It uses nothing about $\pi$, and which case holds depends on the decimal expansion of $\pi$. The procedure "compute the digits of $\pi$ until a block of $n$ sevens appears" is an algorithm, since $\pi$ is a computable real, but it only halts when $h(n) = 1$. Computability is a property of the function, not of a given description of it; the definition does not require that a program be known.
:::
::::

## Notes and references

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- S. C. Kleene, *Introduction to Metamathematics*, North-Holland, 1952, §62 (Church's thesis).
- R. Gandy, *Church's thesis and principles for mechanisms*, in J. Barwise, H. J. Keisler, K. Kunen (eds.), The Kleene Symposium, North-Holland, 1980, 123–148.
- W. Sieg, *On computability*, in A. Irvine (ed.), Philosophy of Mathematics, Handbook of the Philosophy of Science, Elsevier, 2009, 535–630.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §1.1 and §§17.2–17.3, for the history of the thesis and Turing's analysis.
- B. Monin, L. Patey, *Computability theory*, chapter "Church–Turing thesis", for the thesis and its proper use.
- Y. Gurevich, *Sequential abstract-state machines capture sequential algorithms*, ACM Transactions on Computational Logic 1 (2000), 77–111.
- N. Dershowitz, Y. Gurevich, *A natural axiomatization of computability and proof of Church's thesis*, Bulletin of Symbolic Logic 14 (2008), 299–350.
- P. W. Shor, *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer*, SIAM Journal on Computing 26 (1997), 1484–1509.
- B. Accattoli, U. Dal Lago, *(Leftmost-outermost) beta reduction is invariant, indeed*, Logical Methods in Computer Science 12 (2016), 1:4.

:::::exercises
::::exercise{#ex-ct-goldbach difficulty=1 objective="See that a function whose definition involves an unsolved problem may still be computable, and compare with a bounded version."}
Goldbach's conjecture states that every even number $\geq 4$ is a sum of two primes. Let $g(x) = 1$ for all $x$ if the conjecture is true, and $g(x) = 0$ for all $x$ otherwise. Let $g'(x) = 1$ if every even number $2y$ with $2 \leq y \leq x$ is a sum of two primes, and $g'(x) = 0$ otherwise. Show that $g$ is computable and that $g'$ is primitive recursive.

:::solution
Whatever the truth value of the conjecture, $g$ is one of the two constant functions $0$ and $1$, both computable; the argument gives no way of telling which program computes $g$. For $g'$,
$$
g'(x) = 1 \iff \forall y \leq x\ \big(y \geq 2 \rightarrow \exists p \leq 2y\ \exists q \leq 2y\ (\mathrm{Prime}(p) \wedge \mathrm{Prime}(q) \wedge p + q = 2y)\big),
$$
a predicate built from primitive recursive predicates by bounded quantification and connectives, so $g'$ is primitive recursive. The conjecture holds if and only if $g'$ is the constant $1$; but computing each value of $g'$ requires no knowledge of the conjecture.
:::
::::

::::exercise{#ex-ct-infinite-states difficulty=1 objective="See why the finiteness of the set of states is essential, by computing every function with infinitely many states."}
Allow "machines" as in :ref{#def-turing-machine}, with the alphabet $\{\sqcup, 1\}$ but an **infinite** set of states. Show that every partial function $f : \nat \rightharpoonup \nat$ is computed by such a machine. Which requirement of Turing's analysis fails?

:::solution
Take the states $q_i$ ($i \in \nat$, with $q_0$ initial), $w_j$ ($j \in \nat$), $b$, $d$ and $q_h$, and the transitions, for every symbol $a$:

- $\delta(q_i, 1) = (q_{i+1}, \sqcup, R)$; $\delta(q_i, \sqcup) = (w_{f(i-1)}, 1, R)$ if $i \geq 1$ and $f(i - 1)\converge$, and $\delta(q_i, \sqcup) = (d, \sqcup, R)$ otherwise;
- $\delta(w_j, a) = (w_{j-1}, 1, R)$ for $j \geq 1$, and $\delta(w_0, a) = (b, a, L)$;
- $\delta(b, 1) = (b, 1, L)$, $\delta(b, \sqcup) = (q_h, \sqcup, R)$, and $\delta(d, a) = (d, a, R)$.

On input $x$, the states $q_i$ erase the cells $0, \dots, x$, counting them, and reach the blank cell $x + 1$ in state $q_{x+1}$. If $f(x)\diverge$, the machine enters $d$ and moves right forever. Otherwise it writes $1$ on cell $x + 1$, and the states $w_{f(x)}, \dots, w_1$ write $1$ on the cells $x + 2, \dots, x + 1 + f(x)$; in state $w_0$ it reaches the blank cell $x + 2 + f(x)$ and turns back, and $b$ moves left over the $1$s to the erased cell $x$ and halts on cell $x + 1$. The tape contains exactly $f(x) + 1$ ones from the head: the output is $f(x)$. The machine is a table with infinitely many rows, which stores the whole function: this violates the finiteness of the description and Turing's boundedness requirement (finitely many states of mind). Every set of states that can be used by a human computer is finite.
:::
::::

::::exercise{#ex-ct-real-register difficulty=2 objective="See how a model storing an exact real number decides every set, which shows why infinite precision is excluded."}
Consider register machines with the URM instructions on integer registers, and one more register $X$ holding a real number, with the instructions $X \leftarrow 3X$, $X \leftarrow X - 1$, and "if $X \geq 1$, the next instruction is $I_q$". The initial value of $X$ is a real number $\alpha$ fixed with the machine. Show that for every set $A \subseteq \nat$ there are such a machine and $\alpha$ computing the characteristic function of $A$.

:::solution
Let $\alpha = \sum_{m \in A} 3^{-(m+1)}$, and for $i \in \nat$ let $r_i = \sum_{m \in A,\, m \geq i} 3^{-(m - i + 1)}$, so that $r_0 = \alpha$ and $0 \leq r_i \leq \sum_{j \geq 1} 3^{-j} = 1/2$. Then
$$
3 r_i = \chi_A(i) + r_{i+1}, \qquad 0 \leq r_{i+1} \leq 1/2,
$$
so $3 r_i \geq 1$ if and only if $i \in A$, and $3 r_i - \chi_A(i) = r_{i+1}$. With the input $n$ in $R_1$, a counter $R_2$ and $R_3 = 0$ used for unconditional jumps, the program is

| | | |
| --- | --- | --- |
| $I_1$ | $X \leftarrow 3X$ | |
| $I_2$ | if $X \geq 1$, go to $I_6$ | |
| $I_3$ | $J(1, 2, 10)$ | digit $0$ at position $n$ |
| $I_4$ | $S(2)$ | |
| $I_5$ | $J(3, 3, 1)$ | |
| $I_6$ | $J(1, 2, 12)$ | digit $1$ at position $n$ |
| $I_7$ | $X \leftarrow X - 1$ | |
| $I_8$ | $S(2)$ | |
| $I_9$ | $J(3, 3, 1)$ | |
| $I_{10}$ | $Z(1)$ | output $0$ |
| $I_{11}$ | $J(3, 3, 14)$ | halt |
| $I_{12}$ | $Z(1)$ | |
| $I_{13}$ | $S(1)$ | output $1$ |

By induction on $i \leq n$, the program reaches $I_1$ with $R_2 = i$ and $X = r_i$: after $I_1$, $X = \chi_A(i) + r_{i+1}$; if $i < n$, the program subtracts $1$ when $X \geq 1$, that is when $i \in A$, so that $X = r_{i+1}$, and increments $R_2$. At $i = n$ it outputs $1$ if $X \geq 1$, that is if $n \in A$, and $0$ otherwise. So every set, including non-computable ones, is decided by such a machine. A single register holding an exact real stores infinitely much information, which violates the boundedness requirement of Turing's analysis; proposed counterexamples to the physical thesis rely on idealizations of this kind.
:::
::::

::::exercise{#ex-ct-twin-primes difficulty=1 lessons="mu-recursion" objective="Translate an informal algorithm into a definition by minimization, as in a proof by Church's thesis."}
Informally, the following algorithm computes on input $n$ the $n$-th twin prime (counting from $0$): enumerate $p = 0, 1, 2, \dots$, count the $p$ such that $p$ and $p + 2$ are both prime, and return the $p$ at which the count reaches $n + 1$. Define the function it computes as a partial recursive function, and say when it is total.

:::solution
Let $P(p) \iff \mathrm{Prime}(p) \wedge \mathrm{Prime}(p + 2)$, a primitive recursive predicate, and $c(p) = \sum_{q < p} \chi_P(q)$, the number of $q < p$ with $P(q)$, which is primitive recursive. The function computed is
$$
t(n) \simeq \mu p\, \big(P(p) \wedge c(p) = n\big),
$$
a minimization of a primitive recursive predicate, hence partial recursive. Indeed the algorithm returns the $p$ such that $P(p)$ holds and exactly $n$ smaller numbers satisfy $P$, which is the least $p$ satisfying the condition, and it runs forever if there is no such $p$. The function $t$ is total if and only if there are infinitely many twin primes. The translation of the informal description is routine, as the lesson says: the only unbounded loop becomes the minimization.
:::
::::
:::::
