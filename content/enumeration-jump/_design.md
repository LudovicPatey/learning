# Design log: The enumeration jump

This file is the memory of the course (see "Designing tracks and courses" in `AGENTS.md`).
It is not rendered.

## 1. Objectives

Second course of the track "Enumeration degrees". After it, a student can prove the
properties of Cooper's jump and its agreement with the Turing jump on total degrees, describe
the degrees below 0′ₑ as those of Σ⁰₂ sets with their approximations, define the skip and
prove that it characterizes ≤ₑ, and recognize cototal sets.

## 2. Prerequisites assumed

`enumeration-reducibility`; `arithmetic-hierarchy` (Post's theorem); `cohen-genericity`
(Friedberg's jump inversion, `cor-jump-inversion`); `turing-degrees` (generic sets are
GL₁, `thm-generic-low`).

## 3. Results, lesson by lesson

1. **enumeration-jump** — `def-e-jump`, `lem-ka`, `thm-e-jump` (strictness by diagonalization,
   monotonicity by 1-reductions, totality, agreement with the Turing jump), `thm-e-jump-range`,
   `prop-low-quasi-minimal`; the local structure: `prop-below-zero-jump`,
   `prop-sigma2-approximation` (full proof), nontotal degrees below 0′ₑ, survey of density,
   embeddings, theory and definability (stated). Featured: `ex-e-jump-join`,
   `ex-delta2-e-degree`.
2. **skip-and-cototality** — `def-skip`, `prop-skip-basic` (A ≤ₑ B iff A♦ ≤₁ B♦, a short proof
   from `lem-ka`), `def-cototal`, `prop-cototal-skip`, `prop-independent-cototal`,
   `prop-subshift-cototal` (Jeandel, using Birkhoff's uniform recurrence, admitted); the other
   characterizations stated. Featured: `ex-cototal-total-not-converse`.

## 4. Proof techniques

Diagonalization; 1-reductions transferred to complements; Σ⁰₂ approximations from a Σ⁰₂
definition; combinatorial definitions turned into enumeration reductions (independent sets,
subshifts).

## 5. Choices

- Lessons 1 and 2 of the first draft (the jump; the local structure) were each about 15
  minutes and were merged (2026-11-18). The label `ex-jump-join` was renamed
  `ex-e-jump-join` (it collided with an exercise of `cohen-genericity`).
- Cooper's density theorem for the Σ⁰₂ degrees is stated, not proved: it is a long priority
  argument, and the track favors the structural results.
- The skip is presented after the jump, following Andrews et al., who argue it is in some
  respects the better analogue of the Turing jump.

## 6. Sources

Soskova's survey (Sections 3.1, 3.3, 4.2); Cooper (1984); McEvoy (1985); Andrews, Ganchev,
Kuyper, Lempp, Miller, A. Soskova, M. Soskova (2019); McCarthy (2018); Miller–Soskova (2018);
Jeandel (2015); the papers on the local structure cited in the survey.

## 7. History

- 2026-11-18: course written (three lessons, merged into two the same day).
