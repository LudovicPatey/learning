# Design log: Intrinsic definability

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

The question: which relations can every copy of a structure enumerate or compute? After
the course, a student can prove the theorem of Ash, Knight, Manasse, Slaman and Chisholm
at level 1, explain the role of parameters, describe the sets a structure codes (Knight),
define the jump of a relation, find complete relations on classical structures, and
distinguish intrinsic from relatively intrinsic notions.

**Role.** Second course of the computable structure theory track. The next course uses
the same technique (failed diagonalization, Σᶜ₁ definitions with parameters) for
isomorphisms, and the same intrinsic/relative distinction for categoricity.

## 2. Prerequisites assumed

computable-structures (presentations, pull-backs, computable categoricity); enumeration
reducibility is defined in lesson 1.

## 3. Results, lesson by lesson

1. **intrinsic-relations** — `def-rice`, `def-sigma-c-1`, `thm-akms-chisholm-1`,
   `cor-uniform-rice`, `cor-knight-ce-coded`. Featured: `ex-sigma-c-1-examples`.
2. **complete-relations** — `def-kleene-relation`, `lem-kleene-complete`,
   `thm-kleene-not-computable`, structural and binary information, `prop-ld-complete`,
   `thm-adj-complete` (Dickson's lemma). Featured: `ex-jump-monotone`. Further:
   `ex-dlo-complete`.
3. **intrinsic-vs-relative** — `def-intrinsically-ce`, `prop-successor-not-ice` (direct
   construction, no priority), `thm-ash-nerode` (admitted, Ash–Knight 11.1),
   Manasse and Harizanov (stated), `prop-vector-space-intrinsic` (proved from
   Ash–Nerode). Featured: `ex-multiples-vector`.

## 4. Proof techniques

A failed diagonalization turned into a definition; Kleene's diagonal argument for
relations; transfer through an isomorphism with a canonical copy; well-quasi-orderings;
building a computable copy that defeats c.e. sets, requirement by requirement.

## 5. Choices

- Lessons 1 and 2 were first written for `computable-structures` and moved here when the
  track was reorganized by questions (2026-11-18).
- The Ash–Nerode theorem is admitted: its proof is a finite injury construction with
  remapping of witnesses whose correct presentation (Ash–Knight, Theorem 11.1) needs the
  formal machinery of Chapter 11; a full lesson on it is a possible addition. Its
  consequence for vector spaces is proved.

## 6. Sources

Montalbán, *Within the Arithmetic*, Chapter II; Ash–Knight, Chapters 10–11; Ash–Knight–
Manasse–Slaman (1989); Chisholm (1990); Knight (1986); Montalbán (2012); Vatev (2011);
Ash–Nerode (1981); Harizanov (1991).

## 7. History

- 2026-11-18: course created from two lessons of `computable-structures` and a new lesson
  `intrinsic-vs-relative`.
