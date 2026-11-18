# Design log: Enumeration reducibility

This file is the memory of the course (see "Designing tracks and courses" in `AGENTS.md`).
It is not rendered.

## 1. Objectives

First course of the secondary track "Enumeration degrees" (`tracks-design.md`). After it, a
student can work with enumeration operators, relate ≤ₑ to c.e. in and ≤_T, identify the total
degrees as the image of the Turing degrees, prove Selman's theorem, and prove that 1-generic
sets have quasi-minimal enumeration degrees.

## 2. Prerequisites assumed

`turing-degrees` (relativization, 1-generic sets and their properties `prop-1-generic`),
`fundamentals` (c.e. sets). Post's complementation theorem relativized is used in
`prop-ce-in-e`.

## 3. Results, lesson by lesson

1. **enumeration-operators** — `def-enumeration-reducibility` (Friedberg–Rogers),
   `ex-enumeration-reductions`, `prop-operator-properties` (monotone, compact, composition),
   `prop-e-degrees-basic`, `prop-ce-in-e`, `def-total`, `thm-myhill-embedding`. Featured:
   `ex-graph-degree`.
2. **selman-theorem** — `thm-selman` (full proof by forcing with finite enumerations),
   `cor-selman-degrees`, total degrees as automorphism base. Featured: `ex-selman-spectrum`.
3. **quasi-minimal-degrees** — `def-quasi-minimal`, `thm-generic-quasi-minimal` (full proof
   by forcing disjointness of two outputs), `thm-gutteridge` (admitted), embeddings and
   strong minimal covers (stated). Featured: `ex-generic-total-cover`.

## 4. Proof techniques

Compactness of operators; forcing with finite enumerations of a set (Selman); Cohen forcing
in which operators see only positive parts (quasi-minimality); diagonal arguments.

## 5. Choices

- The definition by axioms ⟨n, u⟩ (Friedberg–Rogers), as in Soskova's survey; the procedural
  reading is explained right after.
- Quasi-minimality is proved for every 1-generic set rather than by Medvedev's original
  construction: it reuses `prop-1-generic` and shows the mechanism (operators are monotone in
  the positive part) in a short proof.
- Gutteridge's theorem (no minimal degrees) is admitted: its proof is a delicate construction
  of a smaller degree below an arbitrary one, longer than a lesson.

## 6. Sources

Soskova's survey (Sections 1–2, Theorem 4.3); Friedberg–Rogers (1959); Myhill (1961); Selman
(1971); Medvedev (1955); Gutteridge (1971); Slaman–Sorbi (2014). No textbook was available;
Cooper's *Computability Theory* (2004) and Odifreddi's second volume treat the same material
and should be compared when available.

## 7. History

- 2026-11-18: course written (three lessons).
