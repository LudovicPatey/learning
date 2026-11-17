# Design log: Random sequences and Turing degrees

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- relate random sequences and c.e. sets in both directions: a c.e. set above a random
  sequence is complete (Kučera), and a random sequence below ∅′ computes a non-computable
  c.e. set (Kučera), which gives an injury-free solution to Post's problem;
- prove Stephan's theorem (a random PA sequence computes ∅′) and use the dichotomy between
  complete and incomplete random sequences;
- work with Martin-Löf randomness for a computable measure, and transfer it to the uniform
  measure through the representation of reals relative to the measure (Levin, Kautz);
- prove Demuth's theorem and its consequences for truth-table reducibility (Ω is not
  truth-table complete; a wtt-complete c.e. set that is not tt-complete);
- use translates and effective 0-1 laws to prove properties of every 2-random degree:
  hyperimmunity (Martin, Kautz) and generalized lowness (Kautz).

**Role.** Core course of the randomness track, added on 2026-11-17, after `left-ce-reals`
and before `k-trivials` (`content/tracks-design.md`). It covers the material of
Downey–Hirschfeldt Chapter 8 and Nies Chapter 4 that the course `martin-lof-randomness`
leaves out: that course has the Kučera–Gács theorem, the DNC functions computed by random
sequences, Sacks's theorem and the existence of random sequences in every degree above
0′; `randomness-notions` has van Lambalgen's theorem and weak 2-randomness.

## 2. Prerequisites assumed

- **Martin-Löf randomness:** tests, prefix-free generators, Solovay tests, Levin–Schnorr,
  `cor-random-dnc`, `cor-mlr-structure`, Sacks's theorem.
- **Notions of randomness:** relative randomness and 2-randomness (`def-relative-ml`),
  Yu's theorem on Kurtz randomness and computable domination (`thm-kurtz-w2r-dominated`),
  the DNWY theorem (`thm-dnwy`).
- **Left-c.e. reals:** left cuts and Turing degrees (`prop-cut-expansion`), Ω ≡_wtt ∅′.
- **Immunity and growth:** DNC and fixed-point free functions (`thm-dnc-fpf`,
  `ex-fpf-ce-indices`), Arslanov's criterion, hyperimmune functions, truth-table
  reducibility, Jockusch–Martin (`thm-dominated-tt`).
- **Π⁰₁ classes:** PA degrees (`thm-pa-characterization`, `ex-pa-extension`,
  `cor-pa-basis`), basis theorems, computable isolated members.
- **Kolmogorov complexity:** the KC theorem and the uniform family of request sets
  (`ex-request-weight`).
- **Fundamentals:** the fixed point theorem with parameters.

## 3. Results, lesson by lesson

1. **ce-sets** — Kučera's completeness theorem (`thm-kucera-ce-random`, with the wtt
   version), Kučera's theorem on fixed-point free functions below ∅′ (`thm-kucera-post`,
   simple set version), the priority-free solution to Post's problem (`cor-kucera-post`).
   Featured: two random sequences below ∅′ do not form a minimal pair (with the
   noncappability of promptly simple degrees admitted).
2. **stephan-theorem** — Stephan's theorem (`thm-stephan`), consequences
   (`cor-stephan`: DNC versus PA, non-random PA degrees, random degrees not closed upward).
   Featured: above every incomplete degree there is a non-random degree.
3. **computable-measures** — computable measures and ν-tests (`def-computable-measure`),
   atoms are computable (`lem-atoms-computable`), the ν-representation
   (`def-nu-interval`, `lem-seq-degree`), the Levin–Kautz theorem (`thm-levin-kautz`).
   Featured: Bernoulli sequences.
4. **demuth-theorem** — Demuth's theorem (`thm-demuth`), Kautz's random degree whose
   non-zero predecessors are random (`cor-kautz-random-cone`), Calude–Nies
   (`cor-omega-not-tt-complete`), Lachlan (`cor-lachlan-wtt-tt`).
5. **almost-every-degree** — Kolmogorov's 0-1 law (fact), Kučera's translation lemma
   (`lem-kucera-translate`), inner approximation of Π⁰₂ classes (`lem-pi02-inner`),
   Kautz's 0-1 law (`thm-kautz-01`), Martin's and Kautz's hyperimmunity theorem
   (`thm-martin-hyperimmune`), Kautz's generalized lowness (`thm-kautz-gl1`).

## 4. Proof techniques

- KC requests that force a random sequence to change (lesson 1), with a uniform family of
  request sets instead of the recursion theorem.
- The fixed point theorem with parameters in a construction (Kučera's injury-free
  method).
- Solovay tests built from a partial function that is hard to extend (Stephan).
- Transport of measures along truth-table functionals; representation of reals relative to
  a measure (Levin, Kautz).
- Risking measure: requirements that may get stuck on a small cylinder (Martin), and
  effective 0-1 laws through translates.

## 5. Choices

- **Lesson 1 avoids the recursion theorem** in Kučera's completeness theorem: the KC
  constant is fixed by a uniform family of request sets of weights 2^(-d) (`ex-request-weight`),
  then d is chosen equal to it. Downey–Hirschfeldt use the recursion theorem.
- **Kučera's Post solution is proved for simple sets**, not promptly simple ones; the
  fixed point with parameters is applied to a total function given by SMN, so that only the
  total version of the theorem (`thm-fixed-point-parameters`) is needed. Prompt simplicity
  and noncappability are admitted in an exercise.
- **Levin–Kautz with open intervals with computable endpoints** instead of the dyadic
  approximations (σ)_{ν,s} of Downey–Hirschfeldt; part 2 is stated with the common point of
  the intervals, which avoids the case of endpoints.
- **Demuth's theorem through Kautz's measure argument**, as in Downey–Hirschfeldt, rather
  than Demuth's original.
- **Martin's construction written with axioms** (τ, x, y), so that the consistency of the
  functional is visible; the witnesses for other cylinders are given value 0 at the stage
  equal to the witness.
- **Excluded:** Barmpalias–Lewis–Ng (every PA degree is the join of two random degrees),
  Kurtz's theorems on 1-generics and CEA degrees below almost every degree, Stillwell's
  decidability of the "almost all" theory, mass problems (Simpson), the
  Reimann–Slaman theory of randomness for non-computable measures. They are cited.

## 6. Comparison with the literature

- **Downey–Hirschfeldt:** 2.22.5 and 8.2 (lesson 1), 8.8 (lesson 2), 6.12 (lesson 3), 8.6
  (lesson 4), 6.10, 8.14, 8.21.1–8.21.2 (lesson 5).
- **Nies:** 4.2 (injury-free constructions), 4.3 (Stephan's theorem appears as Theorem
  4.3.8 in Nies's numbering, to be checked), 3.6 (2-randomness); the Levin–Kautz theory is
  not in Nies's book.
- **Monin–Patey**, chapter "Martin-Löf randomness", section "Randomness and Turing
  degrees": Kučera–Gács and random sequences and DNC; the rest of this course goes beyond.

## 7. Pedagogical plan

Each lesson states the intuition of the construction before the proof. Figures:
`scripts/figures/randomness-degrees.py` (Stephan's construction on an interval; the
ν-representation for a Bernoulli measure).

## 8. Sources (checked 2026-11-17)

- Downey–Hirschfeldt, checked in the PDF: Theorem 2.22.5 and the remark on Post's
  problem; Section 6.10 (Lemma 6.10.1, Theorem 6.10.2, Corollary 6.10.3); Section 6.12
  (Definitions 6.12.1–6.12.5, Lemmas 6.12.6–6.12.7, Theorem 6.12.9); Theorems 8.2.1, 8.6.1,
  8.8.1, 8.8.4, 8.14.1, 8.21.1, 8.21.2 and Corollaries 8.2.2, 8.6.2–8.6.4, 8.8.2–8.8.7.
- Original papers from DH's bibliography: Kučera 1985, 1986; Stephan 2006; Demuth 1988;
  Kautz 1991 (thesis); Calude–Nies 1997; Lachlan 1968; Barmpalias–Lewis–Ng 2010.

## 9. Recent literature

- The "two kinds of random sequences" (complete and incomplete) are now studied as
  difference randomness (Franklin–Ng 2011, DH Section 7.7) and through the
  Bienvenu–Day–Greenberg–Kučera–Miller–Nies–Turetsky work on Oberwolfach randomness and
  K-triviality (2016), which belongs to the course on K-trivial sets.

## 10. Open points

- Nies's section numbers for Stephan's theorem and Kučera's injury-free solution are not
  checked; the lessons cite Downey–Hirschfeldt only, except Nies Section 4.2.
- Possible addition: Barmpalias–Lewis–Ng (every PA degree is a join of two random
  degrees), whose proof uses Kučera coding into Π⁰₁ classes.

## 11. Exercises

Featured: `ex-two-random-no-minimal-pair` (1), `ex-stephan-above-incomplete` (2),
`ex-bernoulli-frequency` (3), `ex-tt-below-omega` (4), `ex-kucera-jump` (5). Further
exercises cover the wtt form of Kučera's theorem, Δ⁰₂ randoms and weak 2-randomness, PA
classes of measure zero, Δ⁰₂ random PA sequences, computable random sequences of a measure,
the representation for the uniform measure, columns of random sequences, computably
dominated random sequences, and degree-invariant Σ⁰₃ classes.

## 12. History

- **2026-11-17: course written** (five lessons) when the randomness track was enlarged.
- **2026-11-17: polishing pass.** All proofs checked again; sources checked against Downey–Hirschfeldt (Kautz's nontrivial measure, Section 6.12; the remark of Bienvenu and Porter after Theorem 8.6.1). Corrections: a remark in `ce-sets` said that the c.e. sets below a low random sequence are never above it, which is false for ∅′; replaced by the correct statement (the only c.e. degree above a random sequence is 0′). In `computable-measures`, the generating strings of the classes of part 2 of `thm-levin-kautz` are the minimal ones, not the maximal ones. A vague sentence of `stephan-theorem` rewritten. New further exercises: `ex-low-random-strictly-above`, `ex-measure-with-atom`, `ex-gl1-measure-one`.
