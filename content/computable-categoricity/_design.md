# Design log: Computable categoricity

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

The question: when are all computable copies of a structure computably isomorphic? After
the course, a student can prove that relative computable categoricity is equivalent to a
c.e. existential Scott family over parameters, decide relative categoricity for linear
orders, vector spaces and Boolean algebras, explain categoricity on a cone, prove
Nurtazin's theorem, state Goncharov's theorems, and compute the computable dimension and
the strong degree of categoricity of ω.

**Role.** Third course of the computable structure theory track (`tracks-design.md`). It
reuses the failed diagonalization of `intrinsic-definability` for isomorphisms, and
introduces the first finite injury construction of the track (Nurtazin). The next course,
`degree-spectra`, uses generic presentations and the same copies ω_X.

## 2. Prerequisites assumed

`computable-structures` (presentations, pull-backs, decidable structures, the effective
back-and-forth method, Δ⁰₂-categoricity of ω); `intrinsic-definability` (r.i.c.e.
relations, Ash–Nerode for vector spaces); the Friedberg–Muchnik construction (`ce-degrees`)
for infinitely many incomparable c.e. sets.

## 3. Results, lesson by lesson

1. **scott-families** — `lem-rcc-formulations`, `def-scott-family`, `ex-scott-families`,
   `prop-scott-rcc` (effective back-and-forth). Featured: `ex-omega-no-scott`. Further:
   `ex-random-graph-scott`, `ex-integers-scott`.
2. **relative-categoricity** — `thm-rcc-scott` (AKMS, Chisholm), relativized form,
   `cor-rcc-constants`, `cor-rcc-definable-relations`. Further: `ex-rcc-delta2-omega`,
   `ex-rcc-equivalence-structure`.
3. **classical-examples** — `lem-finite-adjacencies` (figure), `thm-lo-rcc` (relative
   version proved, plain version admitted), `prop-vector-not-cc` (from Ash–Nerode),
   `prop-ba-finitely-many-atoms`; table of characterizations; Π¹₁-completeness and
   Σ⁰₃-completeness stated. Featured: `ex-ba-infinitely-many-atoms`. Further:
   `ex-lo-examples`, `ex-lo-parameters-needed`, `ex-ba-examples`, `ex-vector-not-rcc`.
4. **relative-vs-plain** — `def-cc-cone`, `thm-cc-cone` (Montalbán), `def-effectively-atomic`,
   `prop-atomic-decidable-cc`, `thm-goncharov-cc-not-rcc` (admitted). Further:
   `ex-cone-omega`, `ex-cone-linear-orders`.
5. **nurtazin-theorem** — `thm-nurtazin` (full finite injury proof),
   `thm-goncharov-2-decidable` (admitted, with the changes to the proof). Further:
   `ex-nurtazin-dlo`.
6. **dimension-and-degrees** — `def-computable-dimension`, `lem-omega-x` (figure),
   `prop-omega-dimension`, `thm-finite-dimension` (admitted), `def-degree-categoricity`,
   `prop-omega-degree`; survey of degrees of categoricity and the open question. Featured:
   `ex-integers-degree`. Further: `ex-degree-zero`, `ex-omega-x-degrees`.

## 4. Proof techniques

Effective back-and-forth with existential formulas; a failed diagonalization against all
Turing functionals, producing a Scott family; moving the witnesses of an existential
formula by an embedding (linear orders, Boolean algebras, vector spaces, equivalence
structures) to show that no existential Scott family exists; relativization and cones;
finite injury with bets certified in the limit (Nurtazin); coding a c.e. set into
adjacencies (ω_X).

## 5. Choices

- **Relative before plain.** The course starts from the relative notion, which has a
  structural characterization, and treats plain categoricity as the harder, less robust
  notion. Ash–Knight (Chapter 12) start from Goncharov's theorem for 2-decidable
  structures, historically first; Montalbán (Chapter VIII) starts, like this course, from
  the relative notion.
- **The hard direction of the main theorem** is proved by the diagonalization of
  `thm-akms-chisholm-1` instead of Montalbán's 2-generic enumeration. Only correctness of
  the functional has to be forced: totality is used only to show that every tuple
  satisfies a formula of the family. This keeps the proof parallel to the previous course
  and avoids forcing totality, a Σ⁰₂ property.
- **Classical examples: relative versions proved, plain versions admitted.** The negative
  direction for plain categoricity (Dzgoev–Goncharov, Remmel for linear orders; Goncharov,
  La Roche for Boolean algebras) is a priority construction per class, whose published
  presentations (Ash–Knight 12.11, 12.13) are sketches; a careful write-up for linear
  orders was attempted and its restraint scheme found delicate (the remapping of an
  interval may move an element infinitely often unless the actions of a requirement are
  bounded, which needs more care than the sketches give). The relative versions follow
  from the main theorem by a uniform technique (moving witnesses), which the course wants
  to teach. For vector spaces, the plain version is proved, from Ash–Nerode.
- **Nurtazin rather than Goncharov.** Nurtazin's theorem (decidable copies) is proved in
  full, since its construction is clean: the checks are decidable because the structure is
  decidable. Goncharov's theorem for 2-decidable structures is stated with the changes to
  the proof. Goncharov's counterexample (computably categorical, not relatively so) and
  finite computable dimension are admitted: they need Goncharov's families of c.e. sets,
  a topic for a specialized course.
- **Requirements in Nurtazin's proof** act only when a check fails (Montalbán also lets
  them search for opportunities directly); this suffices for both outcomes and simplifies
  the verification.
- **Degrees of categoricity**: ω is treated in full (strong degree 0′, through ω_K); the
  general results are surveyed with their dates, and the open question is stated.

## 6. Comparison with the literature

Montalbán, *Within the Arithmetic*, Chapter VIII (Theorems VIII.4, VIII.8, VIII.11,
VIII.13, VIII.14, Table 1); Ash–Knight, Chapters 10 and 12; Fokina, Harizanov, Melnikov,
*Computable model theory* (Turing's Legacy, 2014), Section on categoricity; Downey–Melnikov
(2025) treat the same material with more examples from algebra.

## 7. Sources and state of the literature (checked 2026-11-18)

AKMS (1989); Chisholm (1990); Goncharov (1975, 1977, 1980); Nurtazin (1974); Kudinov
(1996); Dzgoev–Goncharov (1980); Remmel (1981); Cholak–Goncharov–Khoussainov–Shore (1999);
Downey–Kach–Lempp–Turetsky (2013); Downey–Kach–Lempp–Lewis-Pye–Montalbán–Turetsky (2015);
Hirschfeldt–Khoussainov–Shore–Slinko (2002); Fokina–Kalimullin–Miller (2010);
Csima–Franklin–Shore (2013); Anderson–Csima (2016); Csima–Harrison-Trainor (2017);
Csima–Ng (every Δ⁰₂ degree is a strong degree of categoricity; cited from the authors'
preprint of 2022, venue to be checked). The question whether every degree of categoricity
is strong is still stated as open in recent papers (checked 2026-11-18). Bibliographic
details of the Russian papers checked against the bibliography of Ash–Knight.

## 8. History

- 2026-11-18: course written (six lessons). The first draft had four lessons; the lessons
  on relative categoricity and on relative versus plain categoricity exceeded 45 minutes
  and were each split into two.
- **2026-11-18 (polishing pass).** Polishing: featured exercises in the text of `relative-categoricity` (`ex-rcc-delta2-omega`), `relative-vs-plain` (`ex-cone-omega`) and `nurtazin-theorem` (`ex-nurtazin-dlo`); quizzes added to `relative-vs-plain` (categoricity on a cone) and `dimension-and-degrees` (the degree of categoricity of ω and the copies ω_X). Exercises moved between the text and the further exercises keep their text, hence their hash and endorsements.
