# Design log: Forcing over the hyperarithmetic sets

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- work with the ramified analytic hierarchy and its truth relation (Π¹₁ for existential
  sentences), and characterize the preservation of ω₁ᶜᵏ by Δ¹₁ comprehension (Kreisel);
- define Cohen forcing over the hyperarithmetic hierarchy, prove the truth lemma and
  Feferman's theorem, and build hyperarithmetically incomparable sets;
- prove the fusion lemma for hyperarithmetic perfect classes and the Gandy–Sacks theorem on
  minimal hyperdegrees.

**Role.** Last core course of the higher computability track (written 2026-11-17): the
forcing methods that structure the hyperdegrees, as Cohen and Sacks forcing structure the
Turing degrees in `effective-forcing`. Uses the uniformization and boundedness theorems
throughout.

## 2. Prerequisites assumed

`sigma11-basis` (hyperjump, Spector), `descriptive-set-theory` (Kreisel uniformization,
total Π¹₁ functions), `hyperarithmetic` (H-sequences, `cor-hyp-quantifier`),
`computable-ordinals` (boundedness), `effective-forcing` (forcing relation, Sacks forcing for
the Turing degrees).

## 3. Results, lesson by lesson

1. **ramified-hierarchy** — language and structure M(ω₁ᶜᵏ, T), full ordinal rank, truth Π¹₁
   (`lem-ramified-truth`), H-sets ranked-definable (`lem-h-ranked`), M(ω₁ᶜᵏ) = HYP
   (`thm-ramified-hyp`), Kreisel's characterization (`thm-ramified-comprehension`).
   Admitted: the set O₁ of unique notations (Sacks III.2.4), the uniform form of Kleene's
   theorem and Kreisel's least ω-model theorem (`fact-hyp-uniform`; Sacks II.5.6, III.4.10).
2. **cohen-forcing** — forcing (`def-cohen-forcing-hyp`), basic properties, Π¹₁ complexity,
   truth lemma, Feferman's theorem (`thm-feferman`), incomparable hyperdegrees
   (`thm-incomparable-hyp`).
3. **minimal-hyperdegree** — perfect forcing (`def-perfect-forcing-hyp`), fusion
   (`lem-hyp-fusion`), deciding sentences (`lem-perfect-decide`), truth lemma, Δ¹₁
   comprehension (`thm-perfect-comprehension`), Spector's dichotomy
   (`lem-constant-or-injective`), Gandy–Sacks (`thm-minimal-hyperdegree`).

## 4. Proof techniques

Forcing over a ranked language; the complexity of forcing relations; uniformization and
boundedness to bound ranks; fusion of hyperarithmetic perfect classes.

## 5. Choices

- **Sacks's presentation** (truth Π¹₁ by Σ¹₁ closure conditions) rather than Chong–Yu's,
  which goes through the Spector–Gandy theorem; the course is then independent of
  `admissible-sets`.
- **Genericity for perfect forcing** is defined by dense sets arithmetic in O (Chong–Yu),
  which Sacks proves equivalent to his definition (Theorem IV.5.3); this avoids Sacks's
  Lemma 5.2 on generically definable sets.
- **Incomparable hyperdegrees** are proved with Chong–Yu's construction (Proposition 5.2.7)
  instead of the halves of a generic set (Sacks, Exercise IV.3.15), whose proof needs an
  automorphism lemma for the forcing relation.
- **Excluded:** Steel forcing and Sacks's theorem on countable admissible ordinals (stated in
  `admissible-sets`); Simpson's Σ¹₁ class of minimal hyperdegrees; Louveau separation
  (Sacks IV.6); measure-theoretic uniformity (Sacks IV.1–2), which is close to
  `higher-randomness`.

## 6. Comparison with the literature

Sacks, Sections III.4 and IV.3–IV.5, checked in the PDF; Chong–Yu, Sections 5.1–5.3. Monin–
Patey has no chapter on forcing over HYP.

## 7. Pedagogical plan

Each lesson recalls the Turing-degree analogue (1-genericity; Spector's minimal degree).
No figure yet: a figure of the fusion family Q_{i,j} would help lesson 3 (open point).

## 8. Sources (checked 2026-11-17)

Sacks: III.4.1–4.16, IV.3.1–3.6, IV.4.1–4.8, IV.5.3–5.6; Sacks II.5.6 for the uniform
Kleene theorem. Chong–Yu: Sections 5.1–5.3 (Proposition 5.2.7, Theorem 5.3.12).
Bibliography from Sacks: Feferman 1965, Gandy–Sacks 1967, Kleene 1959, Kreisel 1962,
Spector 1956.

## 9. Recent literature

Forcing over the hyperarithmetic hierarchy underlies the study of the hyperdegrees (Chong–Yu,
Chapters 10 and 13) and of higher randomness (Chong–Nies–Yu, Monin); not developed here.

## 10. Open points

- Figure of the fusion construction.
- Proof of the automorphism lemma, which would allow Sacks's argument with the halves of a
  generic set.
- ~~Kleene 1959~~: checked against the bibliography of Chong–Yu (Compositio Math. 14
  (1959), 23–40).

## 11. Exercises

Featured: `ex-ramified-collapse`, `ex-generic-not-hyp`, `ex-perfect-generic-not-hyp`.
Further: first levels of the hierarchy, a generic set hyperarithmetic in O, sets of the
hyperdegree of a perfect generic.

## 12. History

- **2026-11-17: course written** (three lessons) from Sacks, with Chong–Yu, when the higher
  computability track was enlarged.
