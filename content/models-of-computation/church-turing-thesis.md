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

Church proposed the identification of effective calculability with λ-definability, and then with general recursiveness, in 1934–1936. Gödel was initially not convinced, precisely because no argument showed that these definitions exhausted all effective procedures. It was Turing's paper of 1936 that convinced him, and most of the community.

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

Under these constraints, a step of computation can be decomposed into elementary steps of a Turing machine: the two-dimensional sheet of paper can be replaced by a one-dimensional tape, and observing a bounded region can be simulated by moving the head back and forth. Turing concludes that machines with a single head on a single tape compute everything that a human computer can compute.

In 1980, Gandy isolated principles under which a **discrete deterministic mechanical device**, possibly acting in parallel on many parts, is equivalent to a Turing machine. His principles include a bound on the propagation speed of causal effects, and the requirement that the state of the device be built from finitely many parts of bounded complexity. Sieg later refined this analysis into an axiomatic presentation of computability.

## Evidence

The thesis is supported by three kinds of evidence.

- **Convergence of definitions.** Every proposed formalization of computability has turned out to be equivalent to Turing computability: recursive functions, λ-calculus, Turing machines, Post systems, Markov algorithms, register machines, cellular automata, and all general-purpose programming languages. Their starting intuitions are very different, which makes the convergence significant.
- **Conceptual analysis.** Turing's and Gandy's arguments derive the thesis from explicit, plausible properties of mechanical computation.
- **Absence of counterexamples.** No algorithm computing a non-Turing-computable function has been found in ninety years of intensive use of algorithms.

## Variants

Several stronger statements are sometimes called the Church–Turing thesis. They should be distinguished from the thesis above.

- **The physical Church–Turing thesis.** Every function computable by a physical system is Turing-computable. This is a statement about the laws of physics, not about mechanical procedures. It is open; proposed counterexamples rely on idealizations such as infinitely precise real numbers or supertasks, whose physical realizability is doubtful.
- **The extended (complexity-theoretic) thesis.** Every reasonable model of computation can be simulated by a Turing machine with at most polynomial overhead in time. This is a statement about efficiency. Quantum computing is widely believed to violate it — Shor's algorithm factors integers in polynomial time, which is not known to be possible classically — while it does not violate the Church–Turing thesis: quantum computers compute exactly the Turing-computable functions.

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

## Notes and references

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- S. C. Kleene, *Introduction to Metamathematics*, 1952, chapters XI–XIII.
- R. Gandy, *Church's thesis and principles for mechanisms*, in J. Barwise, H. J. Keisler, K. Kunen (eds.), The Kleene Symposium, North-Holland, 1980, 123–148.
- W. Sieg, *On computability*, in A. Irvine (ed.), Philosophy of Mathematics, Handbook of the Philosophy of Science, Elsevier, 2009, 535–630.
- R. Soare, *Turing Computability: Theory and Applications*, 2016, chapters 1 and 3.
- N. Cutland, *Computability: An Introduction to Recursive Function Theory*, 1980, for register machines.
- H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, 1984, for the λ-calculus.
