# Design log: Computable structures

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

The two first questions of the subject, on concrete examples: which structures have
computable copies, and are two computable copies computably isomorphic? After the
course, a student can work with presentations and pull-backs, prove Knight's coding
theorem, build decidable models of complete decidable theories and low models of
computable theories, give a computable field without a splitting algorithm, run the
effective back-and-forth argument, and explain why ω is Δ⁰₂- but not computably
categorical.

**Role.** First course of the computable structure theory track (2026-11-18). The track
is ordered by questions (`content/tracks-design.md`); this course gives the examples on
which the general theory of the next courses is tested: orders (ℚ, ω, ζ), the random
graph, vector spaces, Boolean algebras, groups G_X, fields.

## 2. Prerequisites assumed

turing-degrees, fundamentals, arithmetic-hierarchy; pi01-classes (low basis theorem,
PA degrees) for lesson 2. Basic first-order logic (formulas, completeness theorem,
quantifier elimination for DLO and ACF₀ as known facts). Tennenbaum's theorem is cited
from the models of arithmetic track.

## 3. Results, lesson by lesson

1. **presentations** — `def-omega-presentation`, `ex-computable-structures`,
   `prop-two-copies-omega`, variants of presentations, `lem-ce-substructure`,
   `thm-knight-coding`. Featured: `ex-group-copy-degree`.
2. **computable-models** — decidable structures, `ex-decidable-structures`,
   `thm-decidable-model` (effective Henkin construction), `cor-low-model` (Jockusch–Soare;
   PA degrees), Tennenbaum as a limit, `prop-no-splitting` (Fröhlich–Shepherdson; the
   linear independence of square roots of primes is admitted), Rabin's theorem stated.
   Featured: `ex-decidable-dlo-model`.
3. **back-and-forth** — `def-computably-categorical` (with relative and Δ⁰ₙ versions),
   `thm-effective-cantor`, figure `back-and-forth`, `ex-computably-categorical` (random
   graph, finite-dimensional vector spaces, (ℕ; S)), `prop-omega-delta2`. Featured:
   `ex-random-graph`. Further: ζ is Δ⁰₂- and not computably categorical; the atomless
   Boolean algebra.

## 4. Proof techniques

Pull-backs of enumerations; Knight's coding by the order of two tuples; Henkin
constructions with a decidable consistency test; trees of completions and basis
theorems; Cantor's back-and-forth argument with terminating searches.

## 5. Choices

- The course does not follow one book (author's request, 2026-11-18): it combines
  Montalbán I (presentations, Knight), Ash–Knight 3 and 12 (models of theories, examples
  of categoricity) and classical computable algebra (Fröhlich–Shepherdson, Rabin).
- The material on r.i.c.e. and complete relations, first written as lessons 2 and 3 of
  this course, moved to the course `intrinsic-definability`, which answers the question
  "which relations can every copy enumerate"; the labels were kept.
- The non-categoricity of infinite-dimensional vector spaces and the characterization of
  computably categorical linear orders are left to `computable-categoricity`.

## 6. Sources

Montalbán, *Within the Arithmetic*, Chapter I and Sections III.3, VIII.1; Ash–Knight,
Chapters 3 and 12; Knight (1986); Jockusch–Soare (1972); Fröhlich–Shepherdson (1956);
Rabin (1960); Fokina–Harizanov–Melnikov (2014); Downey–Melnikov (2025).

## 7. History

- 2026-11-18: course created (presentations, then r.i.c.e. and complete relations); the
  same day, restructured by questions: the two lessons on relations moved to
  `intrinsic-definability`, and two new lessons written, `computable-models` and
  `back-and-forth`. Drafts corrected: the finite case of `ex-group-copy-degree`, the
  statement of `ex-no-computable-model`, the random graph and ζ solutions.
