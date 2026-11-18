# Design log: Other models of computation

Not a lesson: files starting with `_` are not rendered. Read this file before revising
the course, keep to its objectives, and record every decision in the history.

## 1. Objectives

After the course, a student can:

- program unlimited register machines, LOOP and WHILE programs, and prove programs
  correct by invariants;
- prove that LOOP programs compute exactly the primitive recursive functions (Meyer and
  Ritchie), and that WHILE programs compute the partial recursive functions;
- compute with λ-terms, state and use the Church–Rosser theorem and the standardization
  (normal order) theorem, and prove that the λ-definable functions are exactly the
  partial recursive functions, including the proof that a term has no normal form when
  the function is undefined;
- assemble the simulations into the equivalence of the five classical models.

**Role.** Specialized course, not in a track. It follows the core course
`models-of-computation`, which gives the two models that the rest of the site uses
(Turing machines and partial recursive functions). This course is for readers who want
the robustness of the notion of computability argued from more models, or who need the
λ-calculus (proof theory, type theory, functional programming) or register machines
(complexity, the Blum–Shub–Smale model mentioned in the thesis lesson).

## 2. Choices

- **Why a separate course.** Until 2026-11-18 the six lessons belonged to the entry course
  of the computability track, which had 16 lessons. No later course uses them: all later
  courses use $\Phi_e$, the normal form and primitive recursive coding. Moving them out
  makes the entry course a ten-lesson course on one question (what is a computable
  function, and why the two formalizations agree), and keeps these lessons intact for the
  readers who want them. See `models-of-computation/_design.md`, history of 2026-11-18,
  and `tracks-design.md`.
- **Order.** Register machines first (closest to Turing machines, and the simplest
  simulation), then LOOP and WHILE (structured programs, matching primitive and partial
  recursion scheme by scheme), then the λ-calculus (a model without state), and the cycle
  of simulations last.
- **Equivalence lesson.** `all-models` collects the five models in one theorem
  (`thm-equivalence-models`) proved by a cycle of simulations, each proved in an earlier
  lesson or in the core course. It received `prop-urm-tm` (register machines by
  multi-tape machines), the cycle figure and the exercise `ex-urm-arithmetization` from
  the former `equivalence-of-models`.
- **Excluded.** Post systems, Markov algorithms, cellular automata, combinatory logic
  beyond an exercise: they add no technique, and the thesis lesson of the core course
  mentions them.

## 3. Sources

The lessons are those of `models-of-computation` before the split; their sources and
recent literature are recorded in sections 8–9 of `models-of-computation/_design.md`
(Shepherdson–Sturgis 1963 and Cutland for register machines, Meyer–Ritchie 1967 for
LOOP programs, Barendregt and Hindley–Seldin for the λ-calculus, Kleene 1936 for
λ-definability).

## 4. History

- **2026-11-18.** Course created from six lessons of `models-of-computation` (labels
  unchanged) and the new lesson `all-models`. `register-machines` and `lambda-calculus`
  now require `models-of-computation/equivalence-of-models`.
- **2026-11-18 (polishing pass).** `all-models` had no featured exercise: `ex-urm-arithmetization` moved into the text. Exercises moved between the text and the further exercises keep their text, hence their hash and endorsements.
