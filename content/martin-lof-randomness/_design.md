# Design log: Martin-Löf randomness

This file is the memory of the course (see "Designing tracks and courses" in
`AGENTS.md`). It is not rendered.

## 1. Objectives

After the course, a student can:

- compute with the uniform measure on Cantor space, represent effectively open classes by
  prefix-free generators, and place the measure of Σ⁰₁ and Π⁰₁ classes (left-c.e.,
  right-c.e., computable in ∅′);
- define Martin-Löf tests, explain why the definition requires uniformity and a computable
  rate, and build a universal test;
- prove statistical laws for random sequences (law of large numbers, normality) and use
  Solovay tests to show that a sequence is not random;
- prove the Levin–Schnorr theorem, the randomness of Ω, and the ample excess lemma;
- use relative measure: the density lemma, the majority vote (Sacks), and the branching
  lemma with leftmost/rightmost coding (Kučera–Gács);
- relate randomness to DNC functions through complexity.

**Role in the track.** The randomness track (`content/tracks-design.md`) is
Kolmogorov complexity → Martin-Löf randomness → martingales (planned). This course gives
the measure-theoretic paradigm and its equivalence with the incompressibility paradigm of
the previous course, and the first interplay of randomness with Turing degrees (Sacks,
Kučera–Gács, DNC). The techniques it teaches, in the terms of the track: effective measure
arguments, universal tests, and the interplay of randomness and degrees. The specialized
courses `randomness-notions`, `k-trivials` and `higher-randomness` build on it.

**Left to the martingale course** (planned, written separately): martingales and Ville's
theorem; c.e. (super)martingales and Schnorr's theorem that ML-randomness is the failure of
c.e. martingales (Downey–Hirschfeldt 6.3); the savings trick; computable randomness and
Schnorr randomness via martingales; the martingale proof of Kučera–Gács
(Downey–Hirschfeldt 8.3.2). This course only mentions Schnorr's characterization in prose
(notes of `levin-schnorr`) and the martingale proof of Kučera–Gács (notes of
`randomness-and-degrees`), as forthcoming, without `:ref`.

## 2. Prerequisites assumed

- **Kolmogorov complexity:** prefix-free machines, `prop-k-basic` (Kraft inequality for K,
  K(n) ≤⁺ 2 log n), approximation of K from above, the KC theorem `thm-kc`, Ω and
  `thm-omega`, `cor-no-c-random`.
- **Π⁰₁ classes:** Cantor space, cylinders, open/closed classes, `prop-pi01-equivalent`,
  `ex-pi01-classes` (DNC₂), the low and computably dominated basis theorems,
  `prop-oracle-stages`.
- **Immunity and growth:** DNC functions `def-dnc`, `thm-dnc-effectively-immune`,
  Arslanov's completeness criterion `thm-arslanov`, `def-computably-dominated`.
- **Measure theory:** existence and outer regularity of the Lebesgue measure are admitted
  (`fact-lebesgue-measure`), with a reference to Kechris.

## 3. Results, lesson by lesson

1. **Measure on Cantor space** (`measure`): `fact-lebesgue-measure`, prefix-free generators
   `lem-prefix-free-generator`, left-c.e. reals `ex-left-ce`, `prop-measure-effective`,
   null classes `def-null`, `ex-null-classes` (pairs, zeros on a computable set, DNC₂).
   Exercises: every left-c.e. real is the measure of a Σ⁰₁ class; null Π⁰₁ classes have
   computable clopen covers.
2. **Martin-Löf tests** (`martin-lof-tests`): `def-ml-test`, `ex-ml-tests`, why uniformity
   and a computable rate are needed (Δ⁰₂ sequences and weak 2-randomness),
   `lem-test-bound`, the universal test `thm-universal-test`, `cor-mlr-structure` (conull,
   Σ⁰₂, Π⁰₁ subclasses, low and computably dominated members). Exercises: runs of zeros;
   tails `ex-tails`; random sets are neither c.e. nor co-c.e. (new).
3. **Statistical laws and Solovay tests** (`solovay-tests`, new on 2026-11-12):
   `fact-hoeffding`, `prop-large-numbers`, normality (remark), `def-solovay-test`,
   Borel–Cantelli, `thm-solovay`. Exercises: no long runs of zeros (new); Kurtz randomness
   and weak 1-genericity `ex-kurtz`.
4. **The Levin–Schnorr theorem** (`levin-schnorr`): `thm-levin-schnorr`,
   `cor-explicit-universal`, `cor-omega-random`, `thm-ample-excess`, `cor-k-excess`.
   Exercises: computable subsequences; runs of length K(n); Rettinger's theorem.
5. **Upper cones are null** (`upper-cones`, new on 2026-11-12): relative measure,
   `lem-density`, `thm-sacks`, `cor-random-cone`. Exercises: relativized Sacks; the
   theorem of de Leeuw–Moore–Shannon–Shapiro (new).
6. **The Kučera–Gács theorem** (`randomness-and-degrees`, retitled): `lem-kucera-branching`,
   `thm-kucera-gacs`. Exercises: random sequences of the degrees of ∅⁽ⁿ⁾; members of
   positive-measure Π⁰₁ classes in every degree above 0′.
7. **Random sequences and DNC functions** (`random-dnc`, new on 2026-11-12):
   `thm-dnc-complexity`, `cor-random-dnc`, `rem-generic-random` (new). Exercises: infinite
   subsets of random sequences compute DNC functions (new); random sets of c.e. degree are
   complete.

## 4. Proof techniques

- **Prefix-free generators and continuity of measure** (lesson 1): used in every later
  measure computation.
- **Effective covers / tests** (lessons 1–2): a null class is shown effectively null by
  computing covers of measure 2⁻ⁿ; `lem-test-bound` lets any computable rate be used.
- **Universal objects by trimming and weighting** (lesson 2): trim each c.e. set into a test
  (checking the bound on finite approximations), then merge with weights 2⁻ᵉ⁻¹. The same
  pattern as the optimal machine of the Kolmogorov course.
- **Tail sums of probability estimates** (lesson 3, law of large numbers; exercises): a
  classical inequality, summed over lengths, gives a test.
- **Counting / Markov's inequality** (lesson 3, Solovay; lesson 4, ample excess): bound the
  measure of the sequences where a non-negative quantity is large by its average.
- **KC theorem as a machine-building tool** (lesson 4): turning a test into compressions.
- **Majority vote** (lesson 5): Sacks; de Leeuw et al. in an exercise.
- **Density and averaging of relative measure** (lessons 5–6): density lemma; Kučera's
  branching lemma.
- **Coding into a Π⁰₁ class with ∅′, decoding by co-c.e. approximations** (lesson 6): the
  leftmost/rightmost coding, with weak truth-table decoding.
- **Complexity as a substitute for diagonalization** (lesson 7): DNC ⇔ complex values.
- **Forcing with Π⁰₁ classes** is used (basis theorems in `cor-mlr-structure`), not taught.

## 5. Choices

- **Split of `martin-lof-tests` (2026-11-12).** With the intuition, the discussion of the
  definition and a figure, the lesson would have exceeded 3000 words. The law of large
  numbers, normality and Solovay tests form a new lesson `solovay-tests`, placed before
  `levin-schnorr` (which uses Solovay tests in an exercise). Moved labels: `fact-hoeffding`,
  `prop-large-numbers`, `def-solovay-test`, `thm-solovay`. All external citers reach the new
  lesson transitively through `levin-schnorr`.
- **Split of `randomness-and-degrees` (2026-11-12) into three lessons.** Relative measure
  and the density lemma moved from `measure` (where they were not used) to the new lesson
  `upper-cones`, with Sacks's theorem; the slug `randomness-and-degrees` keeps the
  Kučera–Gács theorem (cited by `k-trivials/lowness`), with Kučera's branching lemma; the
  DNC material forms the new lesson `random-dnc`. The density lemma is now next to its use,
  and the lesson lengths are 30–35 minutes. Moved labels: `lem-density`, `thm-sacks`,
  `cor-random-cone` (to `upper-cones`); `thm-dnc-complexity`, `cor-random-dnc` (to
  `random-dnc`). `upper-cones` is a prerequisite of `randomness-and-degrees`, so every
  external citer (higher-randomness/hyperdegrees, k-trivials/lowness,
  randomness-notions/weak-2-randomness) still reaches the labels.
- **1-generic sets and randomness.** The statement "no 1-generic set computes a random
  sequence" used a theorem of the specialized course `cohen-genericity`
  (REVIEW-2026-11). It was removed from `cor-random-dnc` and placed in a remark
  `rem-generic-random`, presented as a pointer to that course, so that the corollary
  depends only on prerequisites.
- **Discussion of the definition of tests.** Each requirement (uniformity, computable
  rate) is justified by a counterexample: without uniformity every sequence is captured;
  without a computable rate, every Δ⁰₂ sequence is captured (weak 2-randomness). This is
  the main pedagogical addition of the revision.
- **Infinite subsets of random sequences.** The easy direction (an infinite subset of a
  random set computes a DNC function) is now an exercise with a proof through K, in the
  framework of the lesson; the converse is admitted with the precise history.
- **Excluded:** martingales (next course); van Lambalgen's theorem, n-randomness, weak
  2-randomness, Schnorr and Kurtz randomness beyond one exercise (randomness-notions);
  K-triviality and lowness (k-trivials); the Miller–Yu theorem and K-degrees of randoms;
  Π⁰₁ classes of randoms beyond `cor-mlr-structure`; Kučera's "no gap" and Demuth's
  theorems; PA degrees and randomness beyond the statement of Stephan's theorem. These are
  research topics built on the core or covered elsewhere on the platform.
- **Admitted results (stated with references):** Lebesgue measure; Hoeffding's
  inequality; the characterization of left-c.e. random reals as halting probabilities
  (Calude–Hertling–Khoussainov–Wang, Kučera–Slaman); DNC degrees computing no random
  sequence; the converse of the infinite subset exercise; Stephan's theorem.

## 6. Comparison with the literature

- **Downey–Hirschfeldt.** Section 1.2 (measure, density theorem 1.2.3), Section 6.1
  (1-randomness via K, Ω random 6.1.3), Section 6.2 (Martin-Löf tests 6.2.1, Schnorr's
  theorem 6.2.3, universal test 6.2.5, Solovay tests 6.2.7–6.2.8), Section 6.3 (martingales,
  left to the next course), Section 6.6 (ample excess 6.6.1, Chaitin 6.6.2), Section 8.3
  (Kučera–Gács 8.3.2, via martingales and the space lemma), 8.8 (Kučera 8.8.1, Stephan
  8.8.4), 8.10 (DNC and subsets of randoms 8.10.2–8.10.3), 8.12 (de Leeuw et al. 8.12.1,
  Sacks 8.12.2), 8.16 (autocomplex sets). D–H start from incompressibility (6.1) and then
  tests (6.2); the course follows Martin-Löf's order (tests first), since the Kolmogorov
  course comes before and the measure-theoretic view is the one the degree-theoretic
  lessons use.
- **Nies.** Section 1.9 (measure; local measure and Theorem 1.9.4, the density lemma used
  here), Section 3.2 (ML tests 3.2.1–3.2.5, Schnorr's theorem 3.2.9, Ω 3.2.11, law of large
  numbers 3.2.13 via incompressibility, Solovay tests 3.2.19, runs 3.2.20, Chaitin 3.2.21,
  Rettinger 3.2.32), Section 3.3 (branching lemma 3.3.1, Kučera–Gács 3.3.2 by leftmost and
  rightmost extensions — the proof followed here), Section 3.5 (Kurtz randomness), Section
  4.1 (DNC; Theorem 4.1.9), Section 5.1 (Sacks 5.1.12). Nies proves the law of large
  numbers from incompressibility; the course proves it from a measure estimate, which
  works before the Levin–Schnorr theorem and models the later Solovay-test arguments.
- **Monin–Patey** (`external-data/monin-patey/parts/aleatoire-algorithmique.tex`). The
  chapter "Borel classes, measure and computability" (history of Borel, Lebesgue,
  Baire; Borel classes; Lebesgue measure and the computation of the measure of effective
  classes) corresponds to lesson 1; the chapter "Martin-Löf randomness" has four sections:
  intuitions and definitions (tests motivated by the law of large numbers through
  Hoeffding's inequality, normality as an exercise, Solovay tests, runs of length K(n),
  Rettinger as an exercise), Levin–Schnorr with low and computably dominated randoms,
  randomness and Turing degrees (density lemma, Sacks, Kučera's lemma, Kučera–Gács with a
  figure of the leftmost/rightmost coding), randomness and DNC degrees (DNC ⇔ complex
  values ⇔ infinite subset of a random, with Kučera's second lemma for the hard direction).
  Differences: the course separates measure, tests, statistical laws and the degree-theoretic
  results into shorter lessons; it adds the discussion of the requirements of the definition,
  the ample excess lemma, and the de Leeuw et al. exercise; it proves only the easy
  direction of the subsets-of-randoms characterization (exercise) and admits the
  Greenberg–Miller direction, which Monin–Patey prove. The history of Borel's and Lebesgue's
  work is left to the book.
- **Martin-Löf (1966)** for the definition, **Kučera (1985)** for the branching lemma and the
  DNC result, **Gács (1986)** for the coding with small use.

## 7. Pedagogical plan

1. `measure`: intuition of the uniform measure as coin tossing; idea of the prefix-free
   generator before the lemma, with a figure of the construction on four strings
   (`fig-prefix-free-generator`); examples of left-c.e. reals (`ex-left-ce`: computable
   reals, r_A for c.e. A); intuition of approximations from below and above; examples of
   null classes, including the uncountable DNC₂.
2. `martin-lof-tests`: statistical intuition (significance levels, rejection regions)
   before the definition; examples (computable sequences, the covers of lesson 1, DNC₂);
   counterexamples for each requirement; intuition of the universal test (trim, then
   weight); quizzes on trimming and the shift.
3. `solovay-tests`: the law of large numbers as the model of tail-sum arguments; the
   Solovay test as the abstraction of that argument; idea of the counting proof with a
   figure (`fig-solovay-counting`); exercises on runs and Kurtz randomness.
4. `levin-schnorr`: the two faces of K (Kraft + upper approximation; KC theorem) before the
   proof; schematic figure of K(Z↾n) − n (`fig-excess`); averaging intuition for the ample
   excess lemma; quizzes on prefix-freeness and on the choice of U₂c.
5. `upper-cones`: example of relative measure; density lemma with quiz; majority vote
   explained before Sacks's proof; exercise with the c.e. version (de Leeuw et al.).
6. `randomness-and-degrees`: averaging recalled; coding on perfect trees as the model;
   figure of two steps of the leftmost/rightmost coding (`fig-kucera-gacs`); remark on the
   use; quizzes on decoding and on the lengths.
7. `random-dnc`: intuition (DNC = unpredictable values, complexity = incompressible
   values); remark on 1-generics; exercise on infinite subsets.

Figures are generated by `scripts/figures/martin-lof-randomness.py` (deterministic).
Possible further figure: the majority vote in Sacks's proof (two classes U_{n,0}, U_{n,1}
inside a cylinder).

## 8. Sources, lesson by lesson (checked 2026-11-12)

1. `measure`: Kechris, *Classical Descriptive Set Theory*, Section 17 (measures, regularity);
   Downey–Hirschfeldt, Sections 1.2, 2.19, 5.1; Nies, Sections 1.8 (Definition 1.8.14 for
   left-c.e. reals, 1.8.26 for prefix-free generators) and 1.9.
2. `martin-lof-tests`: Martin-Löf, Inf. Control 9 (1966), 602–619; Jockusch–Soare, TAMS 173
   (1972), 33–56; Kurtz, thesis 1981 (weak n-randomness; Downey–Hirschfeldt, Section 7.2);
   Downey–Hirschfeldt 6.2.1, 6.2.5, 6.2.6, 8.1.2 (low randoms); Nies 3.2.1–3.2.5.
3. `solovay-tests`: Hoeffding, JASA 58 (1963), 13–30; Borel, Rend. Circ. Mat. Palermo 27
   (1909), 247–271; Solovay, unpublished notes, May 1975; Kurtz 1981;
   Downey–Hirschfeldt 6.2.7–6.2.8, 7.2.1; Nies 3.2.13, 3.2.19, 3.5.
4. `levin-schnorr`: Levin, Soviet Math. Dokl. 14 (1973), 1413–1416; Schnorr, JCSS 7 (1973),
   376–388, and Math. Systems Theory 5 (1971), 246–258; Chaitin, JACM 22 (1975), 329–340,
   and Adv. Appl. Math. 8 (1987), 119–146; Miller–Yu, TAMS 360 (2008), 3193–3210;
   Calude–Hertling–Khoussainov–Wang, STACS 98, LNCS 1373, 596–606; Kučera–Slaman, SIAM J.
   Comput. 31 (2001), 199–211. Downey–Hirschfeldt 6.1.1, 6.1.3, 6.2.3 (with footnote 9 on
   Levin and Schnorr), 6.3.4, 6.6.1–6.6.2, 9.2.2–9.2.4; Nies 3.2.9, 3.2.11, 3.2.20, 3.2.21,
   3.2.32.
5. `upper-cones`: Sacks 1963; de Leeuw–Moore–Shannon–Shapiro, Automata Studies (1956),
   183–212; Lebesgue 1904 (*Leçons sur l'intégration*) and Ann. ENS 27 (1910), 361–450;
   Downey–Hirschfeldt 1.2.3, 8.12.1–8.12.2; Nies 1.9.4, 5.1.12.
6. `randomness-and-degrees`: Kučera, LNM 1141 (1985), 245–259; Gács, Inf. Control 70
   (1986), 186–192; Merkle–Mihailović, MFCS 2002, LNCS 2420, 568–580;
   Barmpalias–Lewis-Pye, JCSS (2018), doi:10.1016/j.jcss.2017.06.009;
   Barmpalias–Lewis-Pye–Teutsch, Inf. Comput. 251 (2016), 287–300;
   Downey–Hirschfeldt 8.3.1–8.3.2; Nies 3.3.1–3.3.2.
7. `random-dnc`: Kučera 1985; Kjos-Hanssen–Merkle–Stephan, TAMS 363 (2011), 5465–5480
   (STACS 2006); Ambos-Spies–Kjos-Hanssen–Lempp–Slaman, JSL 69 (2004), 1089–1104;
   Kumabe–Lewis, JLMS 80 (2009), 785–797; Kjos-Hanssen, Math. Res. Lett. 16 (2009),
   103–110; Greenberg–Miller, JSL 74 (2009), 665–678; Stephan, LNL 27 (2006), 342–348.
   Downey–Hirschfeldt 8.8.1, 8.8.4, 8.10.2 (footnote 5 for the history), 8.10.3, 8.16.4;
   Nies 4.1.9, Exercise 8.3.6.

## 9. Recent literature

Checked on 2026-11-12:

- **Barmpalias, Lewis-Pye, *Optimal redundancy in computations from random oracles*, JCSS
  (2018), and Barmpalias, Lewis-Pye, Teutsch, Inf. Comput. 251 (2016).** The optimal use of
  the Kučera–Gács reduction: n + g(n) for computable non-decreasing g with Σ2^{-g(n)} < ∞,
  and not in general otherwise. Added to the notes of `randomness-and-degrees`; the former
  note "Barmpalias and Lewis-Pye studied the optimal use" was made precise.
- **Downey–Hirschfeldt, Theorem 8.10.2 and footnote 5.** Settles the history of the
  characterization of DNC degrees by infinite subsets of random sets (an open point of
  REVIEW-2026-11): Kjos-Hanssen proved subsets ⇒ DNC and the converse for slow-growing DNC
  functions; Greenberg–Miller the converse in general; a short proof is due to Miller.
  This led to the new exercise in `random-dnc`.
- **Effective density (Bienvenu, Hölzl, Miller, Nies, *Denjoy, Demuth and density*, J.
  Math. Logic 14 (2014); Day–Miller, *Density, forcing, and the covering problem*, Math.
  Res. Lett. 22 (2015)).** Randomness notions defined by the density theorem at effective
  closed classes. Not added: they need difference randomness and martingales; a candidate
  for a specialized course. The bibliographic details were written from memory and were
  not checked: verify before citing them in a lesson.
- No simpler proof of the Levin–Schnorr theorem, of Solovay's theorem or of the ample
  excess lemma was found; the proofs given are the standard ones.

## 10. Open points

- **Lebesgue's density theorem: 1904 or 1910.** The lessons now say "in dimension one as a
  consequence of his differentiation theorem (1904), and in general in 1910". Neither book
  dates it; the attribution rests on the standard history of the differentiation theorem
  (one-dimensional case in the *Leçons*, general case in Ann. ENS 1910), checked only
  through secondary web sources. Check against a history of measure theory (Hawkins,
  *Lebesgue's Theory of Integration*) if available.
- **Bibliography errors in Downey–Hirschfeldt:** their entry for Ambos-Spies et al. gives
  pages 102–143; Project Euclid and DBLP give JSL 69 (2004), no. 4, 1089–1104, used here.
- **Barmpalias–Lewis-Pye (2018):** volume and pages not confirmed (volume 92 likely); the
  DOI is given instead.
- **Greenberg–Miller direction** (DNC ⇒ computes an infinite subset of a random): admitted
  here, proved in Monin–Patey with a second lemma of Kučera. A candidate for an added
  section of `random-dnc` if the lesson is extended.
- **Forward pointers kept on purpose:** `martin-lof-tests` cites `cor-omega-random`
  (later lesson) in the discussion of weak 2-randomness; `random-dnc` cites
  `thm-generic-not-dnc` of the specialized course `cohen-genericity` in a remark. Both are
  presented as pointers.
- **Changes needed outside the course** (reported to the coordinator): 
  `randomness-notions/schnorr-kurtz.md` line 32 says "the third exercise of
  martin-lof-randomness/martin-lof-tests"; the exercise is now `ex-kurtz` in
  `solovay-tests` (use `:ref{#ex-kurtz}`). `pi01-classes/_design.md` mentions
  `martin-lof-randomness/measure` as citing `trees-and-classes` for cylinders; the link
  already points to `cantor-space`.

## 11. History

- **2026-11-12.** Design and pedagogy revision; initial log.
  - Structure: 4 → 7 lessons. New lessons `solovay-tests` (law of large numbers, normality,
    Solovay tests, Kurtz exercise, moved from `martin-lof-tests`), `upper-cones` (relative
    measure and density, moved from `measure`; Sacks, moved from
    `randomness-and-degrees`) and `random-dnc` (DNC material, moved from
    `randomness-and-degrees`). `randomness-and-degrees` retitled "The Kučera–Gács
    theorem". Labels moved, none renamed or removed.
  - Content: intuition paragraphs before the prefix-free generator, the definition of tests,
    the universal test, Solovay's theorem, the Levin–Schnorr theorem, Sacks's theorem,
    Kučera–Gács and the DNC characterization; justification of each requirement of the
    definition of tests by a counterexample; new examples `ex-left-ce`, DNC₂ as an
    uncountable effectively null class; new remark `rem-generic-random` (1-generics),
    replacing a clause of `cor-random-dnc` that depended on a non-prerequisite course.
  - Exercises added: random sets are neither c.e. nor co-c.e.; runs of zeros via Solovay
    tests; relativized Sacks; de Leeuw–Moore–Shannon–Shapiro; infinite subsets of random
    sets compute DNC functions. Labels `ex-tails`, `ex-kurtz` added.
  - Figures (new generator `scripts/figures/martin-lof-randomness.py`):
    `fig-prefix-free-generator`, `fig-solovay-counting`, `fig-excess`, `fig-kucera-gacs`.
  - References: every lesson now has notes with book sections checked against
    Downey–Hirschfeldt and Nies. Corrections: the form of the Levin–Schnorr theorem with K
    is credited to Schnorr (published by Chaitin 1975), and `cor-k-excess` to Chaitin
    (1987), not 1975; the use bound of Gács is n + O(√n log n) (the n + o(n) claim was
    imprecise), with Merkle–Mihailović and Barmpalias–Lewis-Pye(–Teutsch) for later
    improvements; the history of the subsets-of-randoms characterization corrected
    (REVIEW-2026-11); Kumabe–Lewis added for DNC degrees computing no random; the
    Calude–Hertling–Khoussainov–Wang / Kučera–Slaman statement split into its two
    directions; Rettinger's theorem located in both books; the density theorem dated.
  - Durations recomputed (words / 55).
