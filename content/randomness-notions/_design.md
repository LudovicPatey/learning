# Design log: Notions of randomness

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- work with randomness relative to an oracle and with n-randomness, and prove van
  Lambalgen's theorem with the two effective measure techniques of the track (averaging by
  Fubini's theorem; discarding bad oracles with a Solovay test);
- derive the consequences of van Lambalgen's theorem: random halves are Turing
  incomparable, 2-randomness is mutual randomness with Ω, no 2-random sequence computes ∅′;
- place weak 2-randomness strictly between 2-randomness and Martin-Löf randomness, and
  explain why it has no universal test;
- prove the Downey–Nies–Weber–Yu / Hirschfeldt–Miller theorem: a random sequence is weakly
  2-random if and only if it computes no non-computable c.e. (or Δ⁰₂) set;
- show that computable domination is the dividing line for Kurtz randomness: Kurtz
  randomness implies weak 2-randomness on computably dominated sequences (Nies–Stephan–
  Terwijn, Yu), and every set of hyperimmune degree computes a Kurtz random sequence that
  is not Schnorr random (Kurtz).

**Role.** A specialized course of the randomness area (`content/tracks-design.md`), after
the core track Kolmogorov complexity → Martin-Löf randomness → martingales. Since
2026-11-12 the core course `martingales` covers computable, Schnorr and Kurtz randomness by
martingales, the strict hierarchy of these four notions and the collapse of the upper three
outside the high degrees. This course takes the hierarchy in the two directions that the
core course leaves out:

- **upwards**, through relativization: relative randomness, van Lambalgen's theorem,
  2-randomness, weak 2-randomness — its own material, which no core course treats;
- **downwards at the level of degrees**: the interaction of Kurtz randomness with
  computable domination and hyperimmunity, which complements the highness results of the
  core course.

It does not redefine or re-prove what `martingales` proves; the lesson `schnorr-kurtz`
cites it.

## 2. Prerequisites assumed

- **Martin-Löf randomness:** tests and the universal test (`thm-universal-test`,
  `cor-mlr-structure`, including a low and a computably dominated random sequence), Solovay
  tests (`def-solovay-test`, `thm-solovay`), Kurtz randomness and weak 1-genericity
  (`ex-kurtz`), Ω (`thm-omega`, `cor-omega-random`), Sacks's theorem (`thm-sacks`),
  Levin–Schnorr (relativized, quoted).
- **Martingales:** Schnorr tests and the martingale definition (`def-schnorr-test`,
  `def-schnorr-random`, `thm-schnorr-tests-martingales`), the law of large numbers
  (`ex-schnorr-success`), the hierarchy (`prop-hierarchy`), weakly 1-generic sequences
  (`prop-kurtz-not-schnorr`), the Δ⁰₂ computably random sequence (`thm-cr-not-mlr`), the
  NST theorem (`thm-nst-nonhigh`).
- **Immunity and growth:** hyperimmune functions and degrees (`def-hyperimmune-fn`),
  computable domination, `cor-high-hyperimmune`.
- **Cohen genericity** (specialized, lesson-level prerequisite of `schnorr-kurtz` only):
  Kurtz's theorem `thm-kurtz` (a set of hyperimmune degree computes a weakly 1-generic set).
- Measure theory: Fubini's theorem and Markov's inequality, admitted (`fact-fubini`).

## 3. Results, lesson by lesson

1. **Relative randomness and van Lambalgen's theorem** (`relative-randomness`):
   `def-relative-ml`, `ex-relative-random` (computable oracles; Z ≤_T X is not X-random;
   Ω is not 2-random; strict hierarchy of n-randomness), `fact-fubini`, figure
   `fig-sections`, `thm-van-lambalgen`, relativized version (prose), failure for Schnorr
   and computable randomness (prose, admitted), `cor-van-lambalgen` (incomparable halves,
   2-random ⇔ A ⊕ Ω random). 2-randomness: hyperimmune degree (Kurtz, Kautz), GL₁
   (Kautz), plain complexity (Miller, NST) — all admitted. Exercises: halves; symmetry;
   Ω is random relative to every 2-random sequence.
2. **Weak 2-randomness** (`weak-2-randomness`): `def-weak-2-random`, generalized ML tests
   and Kurtz's weak n-randomness (prose), `ex-null-pi02`, `prop-weak-2-position`
   (2-random ⇒ W2R ⇒ MLR; no Δ⁰₂ W2R (Martin); no universal test (DNWY)), weak
   2-randomness ≠ Kurtz randomness relative to ∅′ (prose), `thm-dnwy`. Exercises: Δ⁰₂
   and c.e. sets; downward closure among random sequences; a weakly 2-random sequence that
   is not 2-random.
3. **Kurtz randomness and computable domination** (`schnorr-kurtz`): `def-schnorr-kurtz`
   (recall), `prop-notions-implications`, `prop-generic-kurtz` (pointer to
   `prop-kurtz-not-schnorr`), figure `fig-notions-map`, `thm-kurtz-ml-dominated` (NST),
   `thm-kurtz-w2r-dominated` (Yu), `cor-dominated-collapse`, `thm-hyperimmune-kurtz`
   (Kurtz, via `cohen-genericity`), `cor-kurtz-dichotomy`; degrees of Kurtz random
   sequences (prose). Exercises: the DNWY proof of the collapse; a Δ⁰₂ Kurtz random
   sequence that is not ML random; bi-immunity (Jockusch).

## 4. Proof techniques

- **Averaging (Fubini) and Markov's inequality** (lesson 1): a uniform family of relative
  tests is one test for pairs; a test for pairs gives relative tests outside a small class
  of oracles.
- **Solovay tests to discard exceptions** (lessons 1, 2): bad oracles in van Lambalgen's
  theorem; the charged enumerations in DNWY.
- **Π⁰₂ descriptions of Δ⁰₂ objects** (lesson 2): the class {A} and the class
  {X : Φ^X = A}, combined with Sacks's theorem.
- **Measure-charged enumeration** (lesson 2, DNWY): a Post-style simple set whose
  enumerations are paid by a Solovay test; announced as the germ of cost functions.
- **Bounding entry times by domination** (lesson 3): turning a (generalized) test into a
  closed null class; contrasted with the escape argument of `thm-nst-nonhigh` (domination
  almost everywhere gives a closed class, escape infinitely often gives a Solovay test).
- **Genericity versus randomness** (lesson 3): weakly 1-generic sequences as Kurtz random
  non-Schnorr random sequences; category versus measure.

## 5. Choices

- **Role after the martingale course (2026-11-12).** The previous version of `schnorr-kurtz`
  defined Schnorr tests, proved Martin-Löf ⇒ Schnorr ⇒ Kurtz, the law of large numbers for
  Schnorr randomness and the non-Schnorr-randomness of weakly 1-generic sequences, and
  admitted the NST theorem on non-high sequences: all of this is now in `martingales`. The
  lesson was refocused on what the core course does not treat: the interaction of Kurtz
  randomness with domination and hyperimmunity. It keeps its slug (linked from
  `martingales/randomness-hierarchy`) and all its labels: `def-schnorr-kurtz` is a recall
  with pointers, `prop-notions-implications` is proved by citation (and now includes
  computable randomness), `prop-generic-kurtz` is a pointer to `prop-kurtz-not-schnorr`.
  New title: "Kurtz randomness and computable domination".
- **Added: Yu's theorem and Kurtz's theorem.** Yu's strengthening (Kurtz random and
  computably dominated ⇒ weakly 2-random) has the same proof as NST's and gives the whole
  collapse at once; Kurtz's theorem (cited from `cohen-genericity`) gives the converse.
  Together they make computable domination the exact dividing line for Kurtz randomness
  (`cor-kurtz-dichotomy`, stated with "computable in X" so that it follows from the
  results proved on the platform; the degree version, which needs coding into the generic,
  is quoted from D–H 2.24.19 and Nies 1.8.50). This mirrors the role of highness in
  `martingales`, and gives the lesson a self-contained result of its own.
- **Kept: relative randomness, van Lambalgen, 2-randomness, weak 2-randomness.** These are
  the course's own material; they need the martingale course only for the remarks on
  Schnorr randomness and for the comparison with Kurtz randomness relative to ∅′.
- **Kept admitted:** Fubini/Markov; Kurtz's theorem that 2-random sequences have
  hyperimmune degree (proofs in Nies 3.6.15 via the NST plain-complexity characterization,
  or in D–H 8.21.1–8.21.2 via Martin's functional and Kautz's 0-1 law; both need material
  the course does not have); GL₁ for 2-random sets (Kautz; D–H 8.14.1); the plain
  complexity characterization of 2-randomness (D–H 6.11); the failure of van Lambalgen for
  Schnorr and computable randomness (D–H 8.11.14–8.11.15, needs NST for high degrees).
- **Excluded:** Demuth randomness (Nies 3.6.24–3.6.26) and difference randomness: they
  belong with K-triviality and lowness; lowness for the weak notions (Nies 8.3, Stephan–Yu,
  Greenberg–Miller): research-level, see `k-trivials`; Kautz's 0-1 law (every Π⁰₂ class of
  positive measure contains a translate of each 2-random sequence): candidate for a later
  lesson with the Martin–Kautz proof of hyperimmunity of 2-randoms.
- **Order.** Relativization first (needed for 2-randomness), then weak 2-randomness (needs
  2-randomness for its position), then the bottom of the hierarchy (needs weak
  2-randomness for Yu's theorem and the map of the six notions).
- **Prerequisite on `cohen-genericity`.** Only at lesson level (`schnorr-kurtz`), for one
  citation of `thm-kurtz`; duplicating Kurtz's construction here would add about 800 words
  for a theorem already proved on the platform.

## 6. Comparison with the literature

- **Downey–Hirschfeldt.** Sections 6.8–6.9 (relative randomness; van Lambalgen 6.9.1–6.9.3,
  Corollaries 6.9.4–6.9.6), 6.11 (2-randomness and plain complexity, 6.11.3–6.11.7), 7.2
  (weak n-randomness: Definition 7.2.1, Theorems 7.2.3–7.2.7, DNWY 7.2.8–7.2.10,
  Hirschfeldt–Miller 7.2.11, Corollary 7.2.12; Jockusch 7.2.23), 7.1.13 (van Lambalgen for
  weaker notions, one direction), 8.11 (8.11.7–8.11.12 for this course's last lesson,
  8.11.14–8.11.15 for the failure of van Lambalgen), 8.14 (GL₁), 8.21 (hyperimmunity of
  2-random sets). D–H prove DNWY's direction (3 ⇒ 1) by majority vote; the course uses
  Sacks's theorem, already proved in the core course.
- **Nies.** Section 3.6 (weak 2-randomness 3.6.1–3.6.4, 2-randomness 3.6.10–3.6.15, Demuth
  randomness), Remark 3.5.3 and Proposition 3.6.4 (weak randomness and domination), 1.8.48–
  1.8.50 (weakly 1-generic sets and hyperimmune degrees).
- **Monin–Patey.** The randomness chapter (`aleatoire-algorithmique.tex`) stops at
  Martin-Löf randomness, with remarks; this course goes beyond it.
- **Differences.** Van Lambalgen's theorem is proved in both directions through Fubini's
  theorem (D–H: universal oracle test for (⇒), Nies's argument for (⇐)); the proof is
  shorter given the admitted measure theory and makes the two techniques visible in one
  figure. The proof of (1 ⇒ 2) in DNWY is the special case of one Π⁰₂ class of
  Hirschfeldt–Miller's argument (D–H 7.2.11 handles Σ⁰₃ null classes), with explicit
  simplicity requirements.

## 7. Pedagogical plan

1. `relative-randomness`: example block (`ex-relative-random`) after the definition;
   figure `fig-sections` (an open class of pairs, a section, the oracles with large
   sections, and the section-measure function whose integral is the measure); intuition
   of both directions before the proof; techniques named after it; quizzes on the use of
   the randomness of A and on 𝒰_{2n}, and on the corollary.
2. `weak-2-randomness`: motivation (dropping the rate); generalized ML tests and Kurtz's
   terminology; example block `ex-null-pi02` (including a null Π⁰₂ class containing Ω);
   commentary on what each part of `prop-weak-2-position` shows; quiz on the Π⁰₂
   description of {A}; remark that weak 2-randomness is not Kurtz randomness relative to
   ∅′ (counterexample: ∅′-weakly 1-generic sequences); idea of both directions of DNWY
   before the proof; quizzes; why randomness is needed in (1 ⇒ 2) (counterexample).
3. `schnorr-kurtz`: example after the recalled definitions; category versus measure;
   figure `fig-notions-map` (six notions, reasons for strictness, the two dividing lines);
   intuition of the collapse; comparison of the domination and escape patterns; quizzes on
   the collapse and on the dichotomy.

Figures are generated by `scripts/figures/randomness-notions.py` (deterministic; the
script checks Fubini and Markov on the example drawn).

## 8. Sources, lesson by lesson (checked 2026-11-12 against the text files of the books)

1. `relative-randomness`: van Lambalgen 1987; D–H 6.9.1–6.9.3, 6.9.4, 6.9.5 (Kurtz: no
   minimal degree is random), 6.11.3, 6.11.6, 7.1.13, 8.11.14–8.11.15, 8.14.1, 8.21.2; Nies
   3.6.10, 3.6.15 (and the remark after it on Kurtz 1981); Miller, JSL 69 (2004);
   Nies–Stephan–Terwijn, JSL 70 (2005); Merkle–Miller–Nies–Reimann–Stephan, APAL 138
   (2006); Miyabe–Rute 2013.
2. `weak-2-randomness`: Kurtz 1981; Gaifman–Snir, JSL 47 (1982); D–H 7.2.1, 7.2.6, 7.2.7,
   7.2.8–7.2.12 (Martin's Corollary 7.2.9 via Solovay's notes); Nies 3.6.1–3.6.4;
   Downey–Nies–Weber–Yu, JSL 71 (2006).
3. `schnorr-kurtz`: Kurtz 1981; NST 2005; D–H 2.24.14–2.24.19, 7.2.23, 8.11.7–8.11.12; Nies
   1.8.48–1.8.50, Remark 3.5.3, Proposition 3.6.4.

**Corrections made on 2026-11-12.**
- The minimal-pair formulation of DNWY was attributed to Hirschfeldt and Miller. D–H
  (7.2.8, 7.2.11, 7.2.12) attribute the minimal pair theorem to Downey–Nies–Weber–Yu and
  the converse (a random non-weakly-2-random sequence computes a non-computable c.e. set)
  to Hirschfeldt and Miller. Fixed in the lesson, the theorem head and the summary.
- "Kurtz (1981) showed that every 2-random sequence has hyperimmune degree": Nies (3.6.15
  and the paragraph before 3.6.10) attributes it to Kurtz; D–H (8.21.2) to Kautz. Both
  are now mentioned.
- Miller 2004 and NST: D–H (6.11.6) says Miller proved that 2-random sets are infinitely
  often C-random (the direction in the title of his paper), NST both directions. Nies
  (p. 136) says Miller obtained the converse direction "⇐"; the lesson follows D–H and the
  title of Miller's paper. Open point below.
- `schnorr-kurtz` cited "the second exercise of martin-lof-randomness/measure" for
  Π⁰₁ null classes and the previous numbering of the Kurtz exercise; the lesson now cites
  `prop-hierarchy` and `ex-kurtz`.

## 9. Recent literature

Checked on 2026-11-12 (web search):

- **Van Lambalgen's theorem for weaker notions.** K. Miyabe and J. Rute, *Van Lambalgen's
  theorem for uniformly relative Schnorr and computable randomness*, Proceedings of the
  12th Asian Logic Conference (World Scientific, 2013; arXiv:1209.5478): the theorem holds
  for Schnorr randomness with uniform (truth-table) relativization. B. Bauwens, *Uniform
  van Lambalgen's theorem fails for computable randomness* (arXiv:1510.00554): the uniform
  version fails for computable randomness. The lesson cites Miyabe–Rute (one sentence);
  Bauwens is not cited (venue not checked).
- **Initial segment complexity of weak 2-randomness.** Nies's Problem 3.6.23 asks for a
  characterization of weak 2-randomness by initial segment complexity. Hölzl, Kräling,
  Stephan and Wu, *Initial segment complexities of randomness notions*, give such a
  characterization (per the abstract; journal version believed to be in Information and
  Computation, 2014 — not checked). Not cited in the lesson.
- **Degrees of Kurtz random sequences.** D–H (p. 290) state that the precise
  classification of the weakly 1-random degrees remains open. With Yu's theorem and
  Kurtz's theorem, a degree contains a Kurtz random sequence if and only if it is
  hyperimmune or contains a random sequence; the lesson states this reduction, not a
  classification. No later classification was found. Lowness for Kurtz randomness
  (Stephan–Yu 2006; Greenberg–Miller, JSL 2009) was found but is out of scope.
- No simpler proof of DNWY or of van Lambalgen's theorem was found.

## 10. Open points

- The attribution of the two directions of the plain-complexity characterization of
  2-randomness differs between D–H and Nies; check against Miller (2004) and NST (2005).
- `Miyabe–Rute 2013`: page numbers not checked.
- Possible addition: Kautz's 0-1 law and the Martin–Kautz proof that 2-random sequences
  have hyperimmune degree, which would remove the main admitted result of lesson 1.
- `relative-randomness` has about 2550 words of text (duration 45), at the upper limit.
- The "degree" version of Kurtz's theorem (every hyperimmune degree contains a weakly
  1-generic set) is quoted, not proved; `cohen-genericity` proves the "computes" version.
  If that course adds the coding version, cite it.

## 11. History

- **2026-11-12: design and pedagogy revision; initial log.**
  - Course: `martingales` added to the prerequisites; description, summary and objectives
    rewritten for the new role.
  - `relative-randomness`: example block `ex-relative-random`, figure `fig-sections`
    (new generator `scripts/figures/randomness-notions.py`), intuition and techniques of
    van Lambalgen's proof, relativized version, failure for Schnorr randomness, quiz on
    the corollary, references for the admitted results on 2-randomness, new exercise on Ω.
  - `weak-2-randomness`: generalized ML tests and Kurtz's terminology, example block
    `ex-null-pi02`, commentary and quiz on `prop-weak-2-position`, comparison with Kurtz
    randomness relative to ∅′, idea of the DNWY proof, third quiz, corrected attributions
    (DNWY / Hirschfeldt–Miller, Martin), new exercise on downward closure.
  - `schnorr-kurtz`: retitled "Kurtz randomness and computable domination"; overlap with
    `martingales` replaced by citations (`def-schnorr-test`,
    `thm-schnorr-tests-martingales`, `prop-hierarchy`, `ex-schnorr-success`,
    `prop-kurtz-not-schnorr`, `thm-nst-nonhigh`), all labels kept; new
    `thm-kurtz-w2r-dominated` (Yu), `cor-dominated-collapse`, `thm-hyperimmune-kurtz`,
    `cor-kurtz-dichotomy`, figure `fig-notions-map`, quiz on the dichotomy, exercise on
    bi-immunity.
