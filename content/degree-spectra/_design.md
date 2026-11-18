# Design log: Degree spectra

Not rendered. See "Designing tracks and courses" in `AGENTS.md`.

## 1. Objectives
Fourth course of the track "Computable structure theory": which sets of Turing degrees are
degree spectra? One tool, generic presentations, used in both directions.

## 2. Results, lesson by lesson
- `generic-presentations`: degree spectrum, Turing and enumeration degree of a structure;
  X-generic enumerations (deciding X-r.i.c.e. sets of tuples), existence in the jump;
  a set c.e. in a Y-generic presentation is c.e.-coded (proved); Richter's theorem and its
  corollary (proved); linear orders have computable existential types (proved).
- `possible-spectra`: structures A_S coding families (three sorts, constants), spectrum =
  oracles enumerating S (proved); cones (proved); Slaman–Wehner (proved); state of the art
  (non-Δ⁰₂: Kalimullin; non-Δ⁰ₙ, n ≥ 3, impossible: ACKLMM; non-hyperarithmetic: GMS, a
  linear order; non-arithmetic: Harrison-Trainor 2025), stated.
- `impossible-spectra`: unions of enumeration cones (proved); 2-generic enumerations;
  Andrews–Miller (proved); F_σ theorem (proved); PA, DNC, ML-random not spectra (proved
  modulo Andrews–Miller Prop. 3.6, admitted); McCarthy (cototal) and Miller–Soskova
  (continuous) stated; low structures (stated).

## 3. Proof techniques
Forcing with generic enumerations (deciding r.i.c.e. and relatively intrinsically Σ⁰₂ sets
of tuples); coding families of sets; the Slaman–Wehner threat argument; the fixed point
theorem as an obstruction.

## 4. Choices
- Families are coded by the three-sorted structure of Montalbán's Exercise V.27 rather than
  by the bouquet graphs of Observation V.25. With graphs, recovering the family from a
  copy needs to locate the centers of the flowers, which is not decidable in the copy, and
  the naive decoding produces extra columns (for instance singletons from non-center
  nodes); the sorted structure avoids this. A remark says that graphs also work.
- In the Slaman–Wehner proof, the limit set in case of infinitely many threats is written
  F ∪ (X ⊕ X̄); Montalbán writes F ⊕ Y, a slip.
- Genericity: the existence lemma uses the jump of D(A) ⊕ X (simpler than Montalbán's
  bound by the complete r.i.c.e. relation); 2-generic enumerations are defined directly by
  relatively intrinsically Σ⁰₂ sets of tuples instead of genericity over (A, K_A).
- The jump of a structure and jump inversion are not proved: they belong with the theory
  beyond one jump; the low property is stated.
- Two solutions of the first draft (a set c.e. in all non-computable sets is c.e.; the
  intersection of two family spectra) were exploratory; they were rewritten before
  verification. The second now marks the side of each coded set by 0 or 1.

## 5. Sources
Montalbán, *Within the Arithmetic*, Chapters IV, V, X (read in the PDF of `external-data/`);
Richter (1981); Slaman (1998); Wehner (1998); Andrews–Miller (2015); Harrison-Trainor,
arXiv:2505.23613 (abstract and theorems read, v4 of September 2026; title changed from
*Relative to any non-arithmetic set* to *Unfriendly jump inversions*); Greenberg–Montalbán–
Slaman (JML, doi checked); ACKLMM (JSL 2016, doi checked); Damaj–Harrison-Trainor,
arXiv:2412.01071 (spectra of relations on (ω,<) on a cone, an intermediate spectrum; not
included, possible addition).

## 6. History
- 2026-11-18: course written (three lessons) after an exploration of the recent literature
  of computable structure theory, recorded in `tracks-design.md`.
